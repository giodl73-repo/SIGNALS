# flow-dataflow — Round 19 Variations (Rubric v16)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v16 (C-01 through C-41, essential/recommended/aspirational tiers, max 108.10)
**Date**: 2026-03-15

---

## Variation Design Notes

R19 targets the four criteria added in v16 from R18 evidence:

**C-38 — CMD register as scaffold entry zero**: R18 V-01 produced a CMD register
pre-declared in the scaffold, but the axis was CMD-first-in-scaffold without a
corresponding CMD-18 entry enforcing positional primacy. The compliance risk: a scaffold
that lists CMD after any T-NN row technically satisfies C-37 but subordinates the
compliance contract to the artifacts it governs. R19 must ensure the CMD register is
the literal first row — before T-01, before PG-01, before T-PARITY — and that this
primacy is enforced by a dedicated CMD entry with a named DO NOT prohibition.

**C-39 — CMD Binding column on every scaffold artifact row**: R18 V-01 introduced a
"CMD Binding" field in the scaffold table, but its pass condition requires the column
to appear on every T-NN, PG-NN, and T-PARITY row — not just selected rows. R18 scaffolds
carried CMD Binding for some rows (typically T-04, T-07) but not all. R19 must enforce
the column as a structural requirement of every scaffold row, not as an optional
annotation on high-risk tables.

**C-40 — Per-phase running total column in PG-NN gate blocks**: R18 produced PG-NN gate
tables with Required Table / Population Status / Go/No-Go columns (satisfying C-34).
The gap: no PG-NN gate table carried a "T-07 Running Total" column. C-40 requires an
intermediate parity tier — the running total at every phase boundary, not just at
T-PARITY. R19 must add this column to every PG-NN gate block and pre-declare it as
a Mandatory Column in the scaffold's PG-NN entries.

**C-41 — Dual-count checkpoint ([N] + [M])**: R18 produced CHECKPOINT [Stage ID] COMPLETE
-- [N] rows appended (satisfying C-32). The gap: no checkpoint carried [M] — the
cumulative running total through that stage. C-41 requires the form: CHECKPOINT [Stage ID]
COMPLETE -- [N] rows appended, [M] total. The dual count makes each checkpoint
self-verifying: [M] at stage k must equal [M] at stage k-1 plus [N] at stage k. R19
must add [M] to every checkpoint statement and add a corresponding CMD entry prohibiting
the [N]-only form.

---

**What R18 established:**

- CMD register pre-declared in scaffold (V-01) converts structural requirements into
  named CMD breaches, but positional primacy (C-38) and CMD Binding on every row (C-39)
  were not yet independent pass conditions — they were V-01's axis behavior, not guaranteed
  in all five variations.
- Per-phase running total in PG-NN gates (V-02) as a parity annotation appeared as a
  gate column note but was not pre-declared in scaffold Mandatory Columns — a gate column
  present but not pre-declared fails C-40.
- Three-role CMD slices (V-03) achieved role-attribution of CMD breaches but did not
  enforce C-40 (per-phase running total) or C-41 (dual-count checkpoint).
- Conversational + IB-NN anchoring (V-04) achieved C-14/C-16 reliably but CMD Binding
  column coverage was incomplete — narrative framing tends to produce CMD references
  for high-risk tables only.
- Criterion annotation column in scaffold (V-05) made C-35/C-36/C-37 legible from the
  scaffold but did not introduce the "CMD Binding on every row" pattern needed for C-39.

---

**R19 hypothesis space:**

**H1 — Three-tier accumulation protocol as lifecycle spine (V-01)**
The prompt's lifecycle is structured around three explicit accumulation checkpoints:
per-stage dual-count (C-41), per-phase gate running total (C-40), post-trace parity
(C-36). A dedicated ACCUMULATION PROTOCOL section in Phase 1 names all three tiers,
assigns each a CMD-NN entry, and requires a CMD entry prohibiting the single-count
form. Hypothesis: elevating the accumulation audit trail to lifecycle-spine status —
rather than treating it as a format annotation — forces [M] into every checkpoint and
the running-total column into every PG-NN gate.

**H2 — Scaffold column explosion: CMD Binding + RT-Col + satisfies columns simultaneously (V-02)**
The scaffold carries four columns beyond the baseline: Mandatory Columns (exact names),
CMD Binding, RT-Col? (Running Total Column required: YES/NO), and Satisfies Criterion.
The CMD register row is first (C-38). RT-Col? = YES on every PG-NN row forces the model
to declare the T-07 Running Total column in Mandatory Columns before any gate is produced.
Hypothesis: declaring RT-Col? in the scaffold at the same structural level as CMD Binding
eliminates the asymmetry where CMD Binding was enforced but Running Total column was not —
both are visible gaps if a scaffold row omits them.

**H3 — Two-role Finance/Operations split with role-owned accumulation tiers (V-03)**
Finance Controller owns Stages 1-3 and their PG-NN gates; Operations Analyst owns
Stages 4-6 and their PG-NN gates. CMD register is entry zero with a "Role Owner" column.
Each role's CMD slice includes the CMD entries that govern that role's stages and gates.
The CMD Binding column on scaffold rows names the role-owned CMD entries. Hypothesis:
role ownership of CMD slices + role ownership of PG-NN gates creates two independent
enforcement surfaces for C-40 — Finance's gate must carry running total because Finance's
CMD slice says so; Operations' gate must carry running total because Operations' CMD slice
says so. One structural failure is attributable to a named role.

**H4 — Phrasing register: coaching-imperative with explicit accumulation arithmetic (V-04)**
Instructional register ("As you close each stage, write both N and M, where M is the
sum of all N values through that stage"). The prompt names the arithmetic explicitly:
"M at stage k = M at stage k-1 + N at stage k." CMD is still entry zero; CMD Binding
column still on every scaffold row; running total column still pre-declared in every
PG-NN entry. Hypothesis: stating the arithmetic as a taught formula rather than a format
requirement produces correct [M] values (not just the structural presence of [M]) because
the model is oriented to the computation, not just the column name.

**H5 — Inertia-first framing with accumulation audit woven into IB-NN coverage count (V-05)**
Incumbent baseline produced before scaffold. The T-07 append-log rows carry an additional
"IB-NN Steps Covered" column. Every checkpoint reads: "CHECKPOINT [Stage ID] COMPLETE
-- [N] rows appended, [M] total, IB-NN steps covered through this stage: [list]." PG-NN
gates carry both T-07 Running Total AND IB-NN Step Coverage columns. CMD Binding on
every scaffold row names both the structural CMD entries AND the IB-NN anchor entries.
Hypothesis: weaving the accumulation audit into the incumbent baseline coverage count
creates compound enforcement pressure — a checkpoint missing [M] is simultaneously
missing IB-NN coverage evidence, making the dual-count failure visible from two angles.

---

## V-01 — Lifecycle Emphasis: Three-Tier Accumulation Protocol as Spine

**Axis**: Lifecycle emphasis — the accumulation audit trail is the primary structural
device of the lifecycle. Phase 1 declares an ACCUMULATION PROTOCOL naming all three
verification tiers: per-stage dual-count checkpoint (C-41), per-phase gate running
total column (C-40), post-trace parity gate (C-36). Every CMD entry governing these
tiers is declared in Phase 1. Scaffold column structure and format are secondary.
**Hypothesis**: treating accumulation verification as a first-class lifecycle concern
— with a named protocol section, dedicated CMD entries, and explicit arithmetic —
forces [M] into every checkpoint and T-07 Running Total into every PG-NN gate because
they are lifecycle steps, not format details.

---

```
You are a Finance / Operations / Commerce data domain expert. Produce a complete data
flow trace for the following pipeline:

{topic}

---

STRUCTURAL RULE: Your response is organized as five phases. Before Phase 2 begins,
you must satisfy Phase 1's gate (PG-01). Before Phase 3 begins, you must satisfy
Phase 2's gate (PG-02). And so on. A phase may not open until the prior phase's
gate shows all GO rows.

The CMD-NN Structural Compliance Register is the FIRST entry in your scaffold and
the FIRST table produced in your response. No T-NN, PG-NN, or T-PARITY entry may
appear in the scaffold before CMD. Every scaffold row below CMD carries a CMD Binding
column naming the CMD-NN entries that govern that artifact.

---

## PHASE 1: COMPLIANCE PROTOCOL DECLARATION

### STEP 0: Output Scaffold

First row: CMD (Structural Compliance Register). All other rows follow in sequence.
The CMD Binding column on every T-NN, PG-NN, and T-PARITY row names which CMD-NN
entries govern that artifact.

| T#       | Table Name                  | Purpose                                                       | Mandatory Columns (exact names)                                                                                              | CMD Binding          | Depends On         |
|----------|-----------------------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|----------------------|--------------------|
| CMD      | Structural Compliance Register | Meta-contract; declared first; every shortfall is a named CMD breach | CMD ID, Positive Imperative, DO NOT Prohibition                                                                     | —                    | —                  |
| T-01     | Entity Inventory            | Domain entities; all trace references bind to T-01 names      | Entity, Description, Key Fields                                                                                              | CMD-07               | —                  |
| T-02     | FM-NN Prediction Register   | Pre-trace failure hypotheses; resolved in T-09 only            | FM-NN, Anticipated Event, Domain Consequence, Expected Designation                                                           | CMD-03               | —                  |
| T-03     | Stage Enumeration           | Named and sequenced pipeline stages                            | Stage ID, Stage Name, Description                                                                                            | CMD-08               | —                  |
| T-04     | Boundary Inventory          | Boundaries with latency decomposition, entity-at-risk, SLA%   | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | CMD-09, CMD-10, CMD-11 | T-03            |
| T-05     | Incumbent Baseline          | Pre-automation process; IB-NN step IDs cited in T-10           | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency                                                               | CMD-13               | —                  |
| T-06     | Stage Exit Manifests        | One typed manifest per stage                                   | field_name, TYPE(precision), Notes                                                                                           | CMD-05               | T-03               |
| T-07     | FM-NN Append-Log            | Accumulating per-stage rows; dual-count checkpoint at each stage | FM-NN, Stage ID, Boundary / Condition, Deferral Statement                                                                  | CMD-04, CMD-17, CMD-19 | T-02, T-03       |
| T-08     | SLA Domination Point        | Standalone domination boundary                                 | Domination Boundary, Exact Cumulative SLA%, Justification                                                                    | CMD-12               | T-04               |
| T-09     | FM-NN Resolution Audit      | Post-trace FM-NN lifecycle resolution                          | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason                                                                       | CMD-03               | T-02, T-07         |
| T-10     | Recovery Audit Table        | NH-NN/LP-NN recovery with IB-NN step citations                 | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage                                      | CMD-13, CMD-14       | T-04, T-05, T-06   |
| T-11     | Closure Gate                | Per-identifier CLOSED / OPEN status for all NH-NN and LP-NN   | Identifier, Source (Stage / Boundary), T-10 Row, Status                                                                     | CMD-15               | T-10               |
| T-PARITY | Count Parity Gate           | Cross-stage arithmetic parity; Tier 3 of accumulation protocol | Stage ID, N Rows This Stage, Running Total, GO / FLAG                                                                       | CMD-06, CMD-18       | T-07               |
| PG-01    | Phase 1 Gate                | CMD completeness + scaffold declaration check                  | Required Artifact, Declaration Status, CMD Binding Status, T-07 Running Total, Go/No-Go                                      | CMD-01, CMD-16, CMD-20 | CMD, T-01–T-11, T-PARITY |
| PG-02    | Phase 2 Gate                | Pre-trace table population before Stage 1                      | Required Table, Population Status, T-07 Running Total, Go/No-Go                                                              | CMD-01, CMD-16, CMD-20 | T-01–T-05, T-08    |
| PG-03    | Phase 3 Gate                | Stage trace completeness + T-07 dual-count checkpoint verification | Required Artifact, Completion Status, T-07 Running Total, Go/No-Go                                                        | CMD-01, CMD-04, CMD-16, CMD-20 | T-03, T-06, T-07 |
| PG-04    | Phase 4 Gate                | Post-trace resolution completeness including T-PARITY          | Required Table, Population Status, T-07 Running Total, Go/No-Go                                                              | CMD-01, CMD-06, CMD-16, CMD-20 | T-09, T-10, T-11, T-PARITY |

Phase gates registered:
- PG-01 closes Phase 1: CMD completeness + scaffold declaration.
- PG-02 closes Phase 2: pre-trace table population.
- PG-03 closes Phase 3: stage trace completeness + dual-count checkpoint verification.
- PG-04 closes Phase 4: post-trace resolution + T-PARITY arithmetic.

Stage assignment: single-role design — C-25 satisfied by default.

---

### CMD: Structural Compliance Register

Produce this table immediately after the scaffold. It is the first substantive table
in your response. Every subsequent structural shortfall is citable by CMD ID.

ACCUMULATION PROTOCOL — three tiers, all required:
- Tier 1 (per-stage): CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total.
  [M] = sum of all [N] values through and including this stage.
- Tier 2 (per-phase): every PG-NN gate block carries a "T-07 Running Total" column
  showing the cumulative append-log count at that phase boundary.
- Tier 3 (post-trace): T-PARITY enumerates all per-stage N values, shows the arithmetic,
  and asserts GO (sum matches [M] from final checkpoint) or FLAG (discrepancy).

| CMD ID | Positive Imperative | DO NOT Prohibition |
|--------|--------------------|--------------------|
| CMD-01 | Pre-declare every phase gate as PG-NN in the scaffold before Phase 1 gate runs | DO NOT produce a gate block with no corresponding PG-NN scaffold entry |
| CMD-02 | Label the scaffold's column contract field exactly as "Mandatory Columns (exact names)" | DO NOT use "Key Columns," "Required Fields," or any descriptive variant |
| CMD-03 | Produce T-02 FM-NN Prediction Register before Stage 1; resolve in T-09 only | DO NOT write CONFIRMED / EXONERATED / NEW status inline during stage traces |
| CMD-04 | Append T-07 rows as table rows during each stage trace block; close with dual-count checkpoint | DO NOT embed FM-NN acknowledgments as prose bullets within stage sections |
| CMD-05 | Produce one T-06 typed exit manifest per stage with field_name: TYPE(precision) notation | DO NOT state schema state in prose without typed field assertions |
| CMD-06 | Produce T-PARITY as a standalone named table with per-stage N enumeration and arithmetic | DO NOT substitute a prose sentence or PG-NN column for T-PARITY |
| CMD-07 | List all domain entities in T-01 before Stage 1; all trace references bind to T-01 names | DO NOT introduce an entity during traces that was not declared in T-01 |
| CMD-08 | Enumerate all pipeline stages in T-03 before Stage 1 trace | DO NOT reference a stage in trace content that has no T-03 entry |
| CMD-09 | Label every inter-stage boundary B[N]->[N+1] in T-04 | DO NOT reference a boundary without the B[N]->[N+1] format |
| CMD-10 | Decompose boundary latency into Transport (ms) and Processing (ms) as separate columns | DO NOT use a single aggregate "Boundary Latency" column; "Negligible" is not a valid value |
| CMD-11 | Use entity.field_name format in T-04 from T-06 manifests; resolve stubs after T-06 is complete | DO NOT use "data," "records," or "payload" as entity-at-risk identifiers |
| CMD-12 | Produce T-08 SLA Domination Point as a standalone table separate from T-04 | DO NOT embed domination point as a prose note appended to T-04 |
| CMD-13 | Produce T-05 Incumbent Baseline with IB-NN Step IDs before writing any T-10 rows | DO NOT write recovery framing without citing a specific IB-NN step from T-05 |
| CMD-14 | Cite a specific IB-NN Step ID in every T-10 row | DO NOT name the process category only — "IB-03" not "AP reconciliation process" |
| CMD-15 | Produce T-11 Closure Gate with one row per NH-NN and LP-NN identifier | DO NOT substitute an aggregate count for per-row CLOSED / OPEN status |
| CMD-16 | Close each phase with a named PG-NN gate block listing all expected artifacts | DO NOT advance to the next phase until all PG-NN gate rows show GO |
| CMD-17 | Close every stage trace block with: CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total | DO NOT write a checkpoint with [N] only; the [M] cumulative total is required |
| CMD-18 | Declare CMD register as the first row of the scaffold, before T-01 | DO NOT list CMD after any T-NN artifact in the scaffold — positional primacy is required |
| CMD-19 | Carry T-07 Running Total column in every PG-NN gate block as a named column in Mandatory Columns | DO NOT produce a gate block without a T-07 Running Total column showing cumulative count |
| CMD-20 | Verify at every PG-NN gate that T-07 Running Total equals sum of all prior stage [N] values | DO NOT advance past a gate whose T-07 Running Total does not match the per-stage checkpoint arithmetic |

---

### PG-01: Phase 1 Gate

| Required Artifact | Declaration Status | CMD Binding Status | T-07 Running Total | Go/No-Go |
|------------------|--------------------|--------------------|-------------------|---------|
| CMD register (CMD-01 through CMD-20) as first scaffold row | | | n/a (pre-trace) | |
| CMD register produced before T-01 in response body | | | n/a | |
| T-01 through T-11 in scaffold with Mandatory Columns (exact names) | | | n/a | |
| T-PARITY declared as standalone scaffold row | | | n/a | |
| PG-01 through PG-04 declared with PG-NN identifiers | | | n/a | |
| Every T-NN, PG-NN, T-PARITY scaffold row carries CMD Binding column | | | n/a | |
| Every PG-NN scaffold entry declares T-07 Running Total in Mandatory Columns | | | n/a | |

Phase 2 may not begin if any row shows NO-GO.

---

## PHASE 2: PRE-TRACE DECLARATIONS

### T-01: Entity Inventory

List every in-scope domain entity before Stage 1. Domain vocabulary: Invoice,
PurchaseOrder, LedgerEntry, VendorInvoice, SKU, InventoryRecord, ShipmentAdvice,
CostCenter, GLAccount, RevenueEvent, etc. A trace reference to an undeclared entity
is a CMD-07 breach.

| Entity | Description | Key Fields |
|--------|-------------|-----------|

---

### T-02: FM-NN Prediction Register

Declare all anticipated failure modes before Stage 1. Minimum 3 entries.
Resolution in T-09 only — inline acknowledgments use T-07 rows only.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

### T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

### T-04: Boundary Inventory

Rules:
- "Negligible" is not a valid latency value — numeric ms required (CMD-10).
- Transport (ms) and Processing (ms) are independent; sum = Total (ms).
- entity.field stubs: write "→ back-fill from T-06.[Stage ID]" until manifest exists.
- Boundary labels: B[N]->[N+1] format (CMD-09).
- SLA%: compute against stated total pipeline SLA budget.

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

After completing T-04, add footnote: "Domination analysis: see T-08."

---

### T-08: SLA Domination Point (standalone — CMD-12)

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

One row. B[N]->[N+1] label from T-04. The boundary where cumulative SLA% first exceeds
50% of the SLA budget. One-sentence justification naming the specific domain operation.

---

### T-05: Incumbent Baseline (CMD-13)

Produce before any T-10 rows. IB-NN Step IDs are the citation anchors for T-10.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

Minimum 4 steps.

---

### PG-02: Phase 2 Gate

| Required Table | Population Status | T-07 Running Total | Go/No-Go |
|---------------|-------------------|--------------------|---------|
| T-01 Entity Inventory | | 0 (no stage traces yet) | |
| T-02 FM-NN Prediction Register (min 3 entries) | | 0 | |
| T-03 Stage Enumeration | | 0 | |
| T-04 Boundary Inventory | | 0 | |
| T-05 Incumbent Baseline (min 4 steps) | | 0 | |
| T-08 SLA Domination Point | | 0 | |

T-07 Running Total at PG-02 = 0 (no stage traces have run yet).
Phase 3 may not begin if any row shows NO-GO.

---

## PHASE 3: STAGE TRACES

For each stage declared in T-03:

**Per-stage protocol:**
1. Heading: ### Stage [ID]: [Name]
2. **Schema at entry**: fields received and their types.
3. **Processing**: transformations, filtrations, enrichments applied.
4. **Loss points (LP-NN)**: at least one concrete named loss point per stage.
5. **No-handling annotations (NH-NN)**: every boundary with no error-handling explicitly
   flagged as "NH-NN: no handling — risk accepted."
6. **Schema at exit**: produce or update T-06 typed exit manifest.
7. **T-07 append-log rows**: for every FM-NN that intersects this stage's boundary or
   processing, append one row to T-07 using the three-column format. Include FM-NN ID,
   this stage's ID and specific boundary/condition, and deferral statement citing T-09.
8. **Dual-count checkpoint (Tier 1)**:

```
CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total.
[M] = [M from prior checkpoint] + [N this stage].
```

[N] = rows appended to T-07 at this stage.
[M] = cumulative total through and including this stage.
If this is Stage 1, [M] = [N].

**After all stages are complete**, return to T-04 and back-fill entity.field stubs
from the T-06 manifests.

---

### PG-03: Phase 3 Gate

| Required Artifact | Completion Status | T-07 Running Total | Go/No-Go |
|------------------|-------------------|--------------------|---------|
| T-06 typed manifest produced for every T-03 stage | | [sum of all N] | |
| T-07 append-log rows present for every FM-NN intersection | | | |
| Dual-count checkpoint (CHECKPOINT [ID] COMPLETE -- [N] rows appended, [M] total) present for every stage | | | |
| T-04 entity.field stubs back-filled from T-06 manifests | | | |
| All error-handling boundaries annotated NH-NN or with mechanism | | | |
| At least one LP-NN per stage | | | |

T-07 Running Total at PG-03 = sum of all stage checkpoint [N] values.
Verify: [M] from final stage checkpoint = T-07 Running Total here.
Phase 4 may not begin if any row shows NO-GO.

---

## PHASE 4: POST-TRACE RESOLUTION

### T-09: FM-NN Resolution Audit (CMD-03)

Resolve every FM-NN from T-02. Statuses:
- CONFIRMED: materialized — cite the specific NH-NN or LP-NN it produced.
- EXONERATED: did not materialize — state the specific reason.
- NEW: emerged during trace without prior prediction — assign NH-NN or LP-NN retroactively.

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

---

### T-10: Recovery Audit Table (CMD-13, CMD-14)

Every NH-NN and LP-NN has exactly one row. Recovery mechanism names the specific
technical mechanism and boundary. IB-NN Step Cited names a specific step from T-05 —
"IB-03" not "the reconciliation process."

| NH/LP ID | Triggering Condition | Recovery Mechanism | IB-NN Step Cited | Boundary / Stage |
|----------|---------------------|--------------------|-----------------|-----------------|

---

### T-11: Closure Gate (CMD-15)

One row per NH-NN and LP-NN identifier from boundary inventory and stage traces.
CLOSED = corresponding T-10 row exists. OPEN = no T-10 row.

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

---

### T-PARITY: Count Parity Gate (Tier 3 of Accumulation Protocol — CMD-06)

Enumerate every stage by ID, its [N] rows appended, and running total. Show arithmetic.
Assert GO if sum matches [M] from final checkpoint; FLAG if discrepancy, naming the
stage whose count diverges.

| Stage ID | N Rows This Stage | Running Total | GO / FLAG |
|----------|------------------|---------------|-----------|

Final row: SUM([N1] + [N2] + ... + [Nk]) == [M final]. GO or FLAG.

---

### T-09 Trade-off Analysis

Name one alternative pattern (e.g., event streaming instead of batch ETL, CDC instead
of dual-write). State at least two trade-off dimensions, at least one quantified in
domain terms (e.g., "CDC adds 200-500ms replication lag per event vs. hourly batch
window; reduces AP ledger staleness window from 60min to <1min").

---

### PG-04: Phase 4 Gate

| Required Table | Population Status | T-07 Running Total | Go/No-Go |
|---------------|-------------------|--------------------|---------|
| T-09 FM-NN Resolution Audit (all FM-NN resolved) | | [final M] | |
| T-10 Recovery Audit Table (one row per NH-NN and LP-NN) | | [final M] | |
| T-11 Closure Gate (one row per identifier, CLOSED or OPEN) | | [final M] | |
| T-PARITY (standalone table, arithmetic shown, GO or FLAG) | | [final M] | |
| T-09 trade-off section (alternative pattern, >=2 trade-off dimensions) | | [final M] | |

T-07 Running Total at PG-04 = [M] from T-PARITY final row.
Verify: T-PARITY GO row confirms arithmetic.
```

---

## V-02 — Output Format: Scaffold Column Explosion (CMD Binding + RT-Col + Satisfies)

**Axis**: Output format — the scaffold carries four additional columns beyond the
baseline: Mandatory Columns (exact names), CMD Binding, RT-Col? (Running Total Column
required: YES/NO), and Satisfies Criterion. RT-Col? = YES on every PG-NN row forces
the T-07 Running Total column to be pre-declared before any gate block is produced.
The CMD register is the first scaffold row (C-38 enforced by column explosion: the
scaffold's own structure makes CMD-first legible from the header).
**Hypothesis**: four columns on every scaffold row make all four new criteria (C-38
positional primacy, C-39 CMD Binding on every row, C-40 running total declared, C-41
dual-count from CMD entries) visible as declarative gaps at scaffold read time — an
evaluator confirms all four from the scaffold alone before inspecting any trace content.

---

```
You are a Finance / Operations / Commerce data domain expert. Produce a complete data
flow trace for the following pipeline:

{topic}

---

STRUCTURAL RULE: Your scaffold carries five columns: T#, Table Name, Purpose,
Mandatory Columns (exact names), CMD Binding, RT-Col?, and Satisfies Criterion.
The CMD register is the FIRST row (T# = CMD). Every subsequent row carries a
CMD Binding column (naming CMD-NN entries that govern this artifact), an RT-Col?
column (YES if this artifact must carry a T-07 Running Total column), and a
Satisfies Criterion column (naming the rubric criterion this artifact primarily
satisfies). A scaffold row missing any of these five column entries is an
undeclared gap from the scaffold's own navigational contract.

---

## STEP 0: Output Scaffold

| T#       | Table Name                  | Purpose                                            | Mandatory Columns (exact names)                                                                                              | CMD Binding             | RT-Col? | Satisfies Criterion |
|----------|-----------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------|---------|---------------------|
| CMD      | Structural Compliance Register | Meta-contract; first artifact; every shortfall citable by CMD ID | CMD ID, Positive Imperative, DO NOT Prohibition                                                             | —                       | NO      | C-37, C-38          |
| T-01     | Entity Inventory            | Domain entities; all trace references bind here    | Entity, Description, Key Fields                                                                                              | CMD-07                  | NO      | C-07, C-10          |
| T-02     | FM-NN Prediction Register   | Pre-trace failure hypotheses; T-09 resolves        | FM-NN, Anticipated Event, Domain Consequence, Expected Designation                                                           | CMD-03                  | NO      | C-26                |
| T-03     | Stage Enumeration           | Named and sequenced stages                         | Stage ID, Stage Name, Description                                                                                            | CMD-08                  | NO      | C-01                |
| T-04     | Boundary Inventory          | Boundaries; latency; entity-at-risk; SLA%          | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | CMD-09, CMD-10, CMD-11 | NO      | C-02, C-11, C-17, C-20, C-21, C-22 |
| T-05     | Incumbent Baseline          | Pre-automation process; IB-NN step IDs             | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency                                                               | CMD-13                  | NO      | C-14, C-15          |
| T-06     | Stage Exit Manifests        | Typed exit manifest per stage                      | field_name, TYPE(precision), Notes                                                                                           | CMD-05                  | NO      | C-04, C-12, C-19    |
| T-07     | FM-NN Append-Log            | Per-stage accumulating rows; dual-count checkpoint | FM-NN, Stage ID, Boundary / Condition, Deferral Statement                                                                    | CMD-04, CMD-17, CMD-18  | NO      | C-28, C-29, C-31, C-32, C-41 |
| T-08     | SLA Domination Point        | Standalone domination boundary                     | Domination Boundary, Exact Cumulative SLA%, Justification                                                                    | CMD-12                  | NO      | C-22, C-30          |
| T-09     | FM-NN Resolution Audit      | Post-trace FM-NN lifecycle resolution              | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason                                                                       | CMD-03                  | NO      | C-26, C-27          |
| T-10     | Recovery Audit Table        | NH-NN/LP-NN recovery; IB-NN step citations         | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage                                      | CMD-13, CMD-14          | NO      | C-08, C-14, C-16, C-18 |
| T-11     | Closure Gate                | Per-identifier CLOSED / OPEN                       | Identifier, Source (Stage / Boundary), T-10 Row, Status                                                                     | CMD-15                  | NO      | C-23                |
| T-PARITY | Count Parity Gate           | Cross-stage arithmetic parity (Tier 3)             | Stage ID, N Rows This Stage, Running Total, GO / FLAG                                                                        | CMD-06, CMD-19          | NO      | C-36                |
| PG-01    | Phase 1 Gate                | CMD completeness + scaffold check                  | Required Artifact, Declaration Status, CMD Binding Status, T-07 Running Total, Go/No-Go                                      | CMD-01, CMD-16, CMD-20  | YES     | C-34, C-35, C-40    |
| PG-02    | Phase 2 Gate                | Pre-trace table population                         | Required Table, Population Status, T-07 Running Total, Go/No-Go                                                              | CMD-01, CMD-16, CMD-20  | YES     | C-34, C-35, C-40    |
| PG-03    | Phase 3 Gate                | Stage trace completeness + checkpoint verification  | Required Artifact, Completion Status, T-07 Running Total, Go/No-Go                                                           | CMD-01, CMD-04, CMD-16, CMD-20 | YES | C-34, C-35, C-40   |
| PG-04    | Phase 4 Gate                | Post-trace resolution + T-PARITY                   | Required Table, Population Status, T-07 Running Total, Go/No-Go                                                              | CMD-01, CMD-06, CMD-16, CMD-20 | YES | C-34, C-35, C-40   |

Notes:
- RT-Col? = YES means this artifact's Mandatory Columns include a T-07 Running Total column.
  A gate block produced without a T-07 Running Total column is a CMD-20 breach.
- The CMD row is the scaffold's first entry (C-38 satisfied).
- Every non-CMD row carries a CMD Binding column (C-39 satisfied at scaffold declaration time).
- Every PG-NN row carries RT-Col? = YES and declares T-07 Running Total in Mandatory Columns (C-40 satisfied at scaffold declaration time).
- CMD-18 requires CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total (C-41 satisfied when stage traces run).

Stage assignment: single-role design — C-25 satisfied by default.

---

### CMD: Structural Compliance Register

| CMD ID | Positive Imperative | DO NOT Prohibition |
|--------|--------------------|--------------------|
| CMD-01 | Pre-declare every phase gate as PG-NN in the scaffold before Phase 1 gate runs | DO NOT produce a gate block with no corresponding PG-NN scaffold entry |
| CMD-02 | Label scaffold column contract field exactly as "Mandatory Columns (exact names)" | DO NOT use "Key Columns," "Required Fields," or any descriptive variant |
| CMD-03 | Produce T-02 FM-NN Prediction Register before Stage 1; resolve every FM-NN in T-09 only | DO NOT write CONFIRMED / EXONERATED / NEW inline during stage traces |
| CMD-04 | Append T-07 rows as table rows during each stage trace; close each trace with dual-count checkpoint | DO NOT embed FM-NN acknowledgments as prose bullets |
| CMD-05 | Produce one T-06 typed manifest per stage; field_name: TYPE(precision) notation | DO NOT state schema in prose only |
| CMD-06 | Produce T-PARITY as a standalone table; enumerate per-stage N and show arithmetic | DO NOT substitute a prose sentence or gate column for T-PARITY |
| CMD-07 | List all domain entities in T-01 before Stage 1 | DO NOT introduce an entity during traces not declared in T-01 |
| CMD-08 | Enumerate all stages in T-03 before Stage 1 | DO NOT reference a stage in trace content with no T-03 entry |
| CMD-09 | Label every boundary B[N]->[N+1] in T-04 | DO NOT reference a boundary without the B[N]->[N+1] label |
| CMD-10 | Decompose latency: Transport (ms) and Processing (ms) as separate columns | DO NOT use a single "Boundary Latency" column; "Negligible" is not valid |
| CMD-11 | Use entity.field_name from T-06 in T-04; resolve stubs after T-06 complete | DO NOT use "data," "records," or "payload" as entity-at-risk |
| CMD-12 | Produce T-08 as standalone table separate from T-04 | DO NOT embed domination point as a prose note |
| CMD-13 | Produce T-05 with IB-NN Step IDs before writing T-10 rows | DO NOT write recovery without citing a specific IB-NN step |
| CMD-14 | Cite a specific IB-NN Step ID in every T-10 row | DO NOT name the process category only |
| CMD-15 | Produce T-11 with one row per NH-NN and LP-NN | DO NOT substitute an aggregate count for per-row status |
| CMD-16 | Close each phase with its named PG-NN gate | DO NOT advance until PG-NN gate shows all GO |
| CMD-17 | Declare CMD register as the scaffold's first row, before T-01 | DO NOT produce CMD after any T-NN in the scaffold |
| CMD-18 | Close every stage trace: CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total | DO NOT write a checkpoint with [N] only — [M] cumulative total is required |
| CMD-19 | Verify T-PARITY GO: final stage [M] matches T-PARITY sum | DO NOT mark T-PARITY GO if any stage [N] value is inconsistent |
| CMD-20 | Carry T-07 Running Total column in every PG-NN gate block (per scaffold RT-Col? = YES rows) | DO NOT produce a PG-NN gate without the T-07 Running Total column |

---

### PG-01: Phase 1 Gate

| Required Artifact | Declaration Status | CMD Binding Status | T-07 Running Total | Go/No-Go |
|------------------|--------------------|--------------------|-------------------|---------|
| CMD register as first scaffold row (RT-Col? = NO confirmed) | | | n/a | |
| All T-NN rows in scaffold with Mandatory Columns (exact names) label | | | n/a | |
| All PG-NN rows in scaffold with RT-Col? = YES and T-07 Running Total in Mandatory Columns | | | n/a | |
| Satisfies Criterion column populated on every scaffold row | | | n/a | |
| CMD Binding column populated on every non-CMD scaffold row | | | n/a | |
| T-PARITY declared as standalone scaffold row | | | n/a | |

Phase 2 may not begin if any row shows NO-GO.

---

## PHASE 2: PRE-TRACE DECLARATIONS

### T-01: Entity Inventory

Domain vocabulary: Invoice, PurchaseOrder, LedgerEntry, VendorInvoice, SKU,
InventoryRecord, ShipmentAdvice, CostCenter, GLAccount, RevenueEvent, etc.

| Entity | Description | Key Fields |
|--------|-------------|-----------|

---

### T-02: FM-NN Prediction Register

Minimum 3 failure mode predictions. Expected Designation names the NH-NN or LP-NN
this prediction will produce if it materializes.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

### T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

### T-04: Boundary Inventory

- Transport (ms) and Processing (ms) independent; sum = Total (ms). No "Negligible."
- entity.field stubs: "→ back-fill from T-06.[Stage ID]" until manifest exists.
- Boundary labels: B[N]->[N+1] format.
- SLA%: compute against stated total pipeline SLA budget.

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

---

### T-08: SLA Domination Point

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

---

### T-05: Incumbent Baseline

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

Minimum 4 IB-NN steps.

---

### PG-02: Phase 2 Gate

| Required Table | Population Status | T-07 Running Total | Go/No-Go |
|---------------|-------------------|--------------------|---------|
| T-01 | | 0 | |
| T-02 (min 3 entries) | | 0 | |
| T-03 | | 0 | |
| T-04 | | 0 | |
| T-05 (min 4 steps) | | 0 | |
| T-08 | | 0 | |

T-07 Running Total = 0 at PG-02 (no stage traces yet).
Phase 3 may not begin if any row shows NO-GO.

---

## PHASE 3: STAGE TRACES

For each stage in T-03:

1. Schema at entry — types of fields received.
2. Processing — transformations applied.
3. Loss points — at least one concrete LP-NN per stage.
4. No-handling annotations — every boundary with no error-handling flagged NH-NN.
5. T-06 typed exit manifest — produce for this stage now.
6. T-07 append-log rows — append rows during this trace (as table rows, not prose).
7. Dual-count checkpoint:

```
CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total.
```
[M] = [prior M] + [N this stage]. Show arithmetic.

After all stages: back-fill T-04 entity.field stubs from T-06 manifests.

---

### PG-03: Phase 3 Gate

| Required Artifact | Completion Status | T-07 Running Total | Go/No-Go |
|------------------|-------------------|--------------------|---------|
| T-06 manifest for every stage | | [cumulative N] | |
| T-07 rows appended for every FM-NN intersection | | | |
| Dual-count checkpoint present for every stage | | | |
| T-04 entity.field stubs back-filled | | | |
| At least one LP-NN per stage | | | |
| All boundaries annotated NH-NN or with mechanism | | | |

T-07 Running Total = sum of all stage [N] values.
Phase 4 may not begin if any row shows NO-GO.

---

## PHASE 4: POST-TRACE RESOLUTION

### T-09: FM-NN Resolution Audit

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

Status options: CONFIRMED (cite NH-NN or LP-NN), EXONERATED (state reason),
NEW (assign identifier retroactively).

---

### T-10: Recovery Audit Table

| NH/LP ID | Triggering Condition | Recovery Mechanism | IB-NN Step Cited | Boundary / Stage |
|----------|---------------------|--------------------|-----------------|-----------------|

Every NH-NN and LP-NN must have exactly one row. IB-NN Step Cited = specific step
from T-05 by Step ID.

---

### T-11: Closure Gate

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

---

### T-PARITY: Count Parity Gate

| Stage ID | N Rows This Stage | Running Total | GO / FLAG |
|----------|------------------|---------------|-----------|

Final assertion: SUM([N1]+[N2]+...+[Nk]) == [M final]. GO or FLAG.
Cross-check: [M final] must equal T-07 Running Total shown in PG-04.

---

### Trade-off Analysis

Name one alternative pattern. State at least two trade-off dimensions, at least one
quantified in domain terms.

---

### PG-04: Phase 4 Gate

| Required Table | Population Status | T-07 Running Total | Go/No-Go |
|---------------|-------------------|--------------------|---------|
| T-09 (all FM-NN resolved) | | [final M] | |
| T-10 (one row per NH-NN and LP-NN) | | [final M] | |
| T-11 (one row per identifier) | | [final M] | |
| T-PARITY (arithmetic shown, GO or FLAG) | | [final M] | |
| Trade-off analysis | | [final M] | |

T-07 Running Total at PG-04 = [M] from T-PARITY.
```

---

## V-03 — Role Sequence: Two-Role Finance/Operations with Role-Owned CMD Slices

**Axis**: Role sequence — Finance Controller owns Stages 1-3 and their phase gates;
Operations Analyst owns Stages 4-6 and their phase gates. The CMD register is entry
zero with a "Role Owner" column. Every CMD-NN entry is assigned to Finance, Operations,
or Shared. The CMD Binding column on every scaffold artifact row names both the CMD-NN
entries AND the role that owns them. Phase handoff gate (PG-02) is the Finance/Operations
boundary — before this gate, Finance owns all accumulation; after it, Operations takes
over the running total and must match Finance's [M] at handoff.
**Hypothesis**: role ownership of CMD slices + explicit handoff gate creates two
independent enforcement surfaces for C-40 and C-41 — Finance's stages produce dual-count
checkpoints because Finance's CMD slice says so; Operations must match the [M] handed
off from Finance's PG-02 gate, making T-07 Running Total in gates the arithmetic
continuity contract between roles.

---

```
You are coordinating a two-role data flow trace for the following pipeline:

{topic}

Role 1: Finance Controller — owns the upstream pipeline stages and their artifacts.
Role 2: Operations Analyst — owns the downstream pipeline stages and their artifacts.

The Finance Controller runs first. The Operations Analyst begins at the Phase 2
handoff gate and takes over from there. Each role owns a named CMD slice that governs
the stages and artifacts it is responsible for producing.

---

STRUCTURAL RULE: The CMD-NN Structural Compliance Register is the FIRST entry in the
scaffold and the first table in the response. Every subsequent scaffold row carries a
CMD Binding column AND a Role Owner column. The CMD register row itself carries
Role Owner = Shared. Every CMD-NN entry names its owner: Finance, Operations, or Shared.
A structural failure is attributable to a named role.

---

## STEP 0: Output Scaffold (Finance Controller produces this section)

| T#       | Table Name                  | Purpose                                            | Mandatory Columns (exact names)                                                                                              | CMD Binding             | Role Owner   | Depends On       |
|----------|-----------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------|--------------|------------------|
| CMD      | Structural Compliance Register | Meta-contract; first artifact; breaches are role-attributable | CMD ID, Role Owner, Positive Imperative, DO NOT Prohibition                                               | —                       | Shared       | —                |
| T-01     | Entity Inventory            | Domain entities; role-shared; trace references bind here | Entity, Description, Key Fields                                                                                         | CMD-07 (Shared)         | Shared       | —                |
| T-02     | FM-NN Prediction Register   | Pre-trace failure hypotheses; T-09 resolves        | FM-NN, Anticipated Event, Domain Consequence, Expected Designation                                                           | CMD-03 (Shared)         | Shared       | —                |
| T-03     | Stage Enumeration + Assignment Map | Named stages with role assignment per stage | Stage ID, Stage Name, Description, Assigned Role                                                                             | CMD-08 (Shared)         | Shared       | —                |
| T-04     | Boundary Inventory          | Boundaries; latency; entity-at-risk; SLA%          | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | CMD-09, CMD-10, CMD-11 (Shared) | Shared | T-03           |
| T-05     | Incumbent Baseline          | Pre-automation process; IB-NN step IDs             | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency                                                               | CMD-13 (Shared)         | Shared       | —                |
| T-06F    | Finance Stage Exit Manifests | Typed manifests for Finance-owned stages           | field_name, TYPE(precision), Notes                                                                                           | CMD-05 (Finance)        | Finance      | T-03             |
| T-06O    | Operations Stage Exit Manifests | Typed manifests for Operations-owned stages     | field_name, TYPE(precision), Notes                                                                                           | CMD-05 (Operations)     | Operations   | T-03             |
| T-07     | FM-NN Append-Log            | Accumulating rows; dual-count checkpoint each stage | FM-NN, Stage ID, Boundary / Condition, Deferral Statement                                                                   | CMD-04, CMD-17, CMD-19 (Shared) | Shared | T-02, T-03      |
| T-08     | SLA Domination Point        | Standalone domination boundary                     | Domination Boundary, Exact Cumulative SLA%, Justification                                                                    | CMD-12 (Finance)        | Finance      | T-04             |
| T-09     | FM-NN Resolution Audit      | Post-trace FM-NN lifecycle resolution              | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason                                                                       | CMD-03 (Operations)     | Operations   | T-02, T-07       |
| T-10     | Recovery Audit Table        | NH-NN/LP-NN recovery; IB-NN step citations         | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage                                      | CMD-13, CMD-14 (Shared) | Shared       | T-04, T-05       |
| T-11     | Closure Gate                | Per-identifier CLOSED / OPEN                       | Identifier, Source (Stage / Boundary), T-10 Row, Status                                                                     | CMD-15 (Operations)     | Operations   | T-10             |
| T-PARITY | Count Parity Gate           | Cross-stage arithmetic parity                      | Stage ID, N Rows This Stage, Running Total, GO / FLAG                                                                        | CMD-06, CMD-18 (Shared) | Shared       | T-07             |
| PG-01    | Phase 1 Gate (Finance)      | CMD + scaffold check; Finance produces             | Required Artifact, Status, T-07 Running Total, Go/No-Go                                                                      | CMD-01, CMD-16, CMD-20 (Finance) | Finance | CMD, T-01–T-05, T-08 |
| PG-02    | Finance/Operations Handoff Gate | Finance closes Stages 1-3; hands off to Operations | Required Artifact, Finance Status, T-07 Running Total at Handoff, Go/No-Go                                              | CMD-16, CMD-20 (Finance) | Finance     | T-06F, T-07      |
| PG-03    | Phase 3 Gate (Operations)   | Operations stages complete                         | Required Artifact, Status, T-07 Running Total, Go/No-Go                                                                      | CMD-01, CMD-16, CMD-20 (Operations) | Operations | T-06O, T-07    |
| PG-04    | Phase 4 Gate (Operations)   | Post-trace resolution complete                     | Required Table, Status, T-07 Running Total, Go/No-Go                                                                         | CMD-01, CMD-06, CMD-16, CMD-20 (Operations) | Operations | T-09–T-11, T-PARITY |

Stage assignment table (declare here, before Stage 1):

| Stage ID | Stage Name | Assigned Role |
|----------|------------|--------------|
| S-01 | [name] | Finance Controller |
| S-02 | [name] | Finance Controller |
| S-03 | [name] | Finance Controller |
| S-04 | [name] | Operations Analyst |
| S-05 | [name] | Operations Analyst |
| S-06 | [name] | Operations Analyst |

(Adjust stage count to match {topic}'s actual pipeline stages.)

---

### CMD: Structural Compliance Register

| CMD ID | Role Owner | Positive Imperative | DO NOT Prohibition |
|--------|-----------|--------------------|--------------------|
| CMD-01 | Shared | Declare CMD as first scaffold row before T-01 | DO NOT list any T-NN artifact before CMD in the scaffold |
| CMD-02 | Shared | Label scaffold column contract exactly as "Mandatory Columns (exact names)" | DO NOT use "Key Columns," "Required Fields," or any variant |
| CMD-03 | Shared | Produce T-02 before Stage 1; resolve FM-NN in T-09 only | DO NOT write CONFIRMED / EXONERATED / NEW inline in stage traces |
| CMD-04 | Shared | Append T-07 rows as table rows per stage; close each with dual-count checkpoint | DO NOT embed FM-NN acknowledgments as prose bullets |
| CMD-05 | Finance / Operations | Produce typed T-06F (Finance) or T-06O (Operations) exit manifest per owned stage | DO NOT state schema in prose without typed field assertions |
| CMD-06 | Shared | Produce T-PARITY as standalone table with per-stage N enumeration and arithmetic | DO NOT substitute a prose sentence or gate column for T-PARITY |
| CMD-07 | Shared | List all domain entities in T-01; all trace references bind to T-01 names | DO NOT introduce an undeclared entity during traces |
| CMD-08 | Shared | Enumerate all stages in T-03 with Assigned Role column before Stage 1 | DO NOT reference a stage with no T-03 and stage assignment row |
| CMD-09 | Shared | Label every boundary B[N]->[N+1] in T-04 | DO NOT reference a boundary without B[N]->[N+1] format |
| CMD-10 | Shared | Decompose latency into Transport (ms) and Processing (ms) as separate columns | DO NOT use single "Boundary Latency" column; "Negligible" is not valid |
| CMD-11 | Shared | Use entity.field_name in T-04 from typed manifests | DO NOT use "data," "records," or "payload" |
| CMD-12 | Finance | Produce T-08 SLA Domination Point as standalone table | DO NOT embed domination as a prose note |
| CMD-13 | Shared | Produce T-05 with IB-NN Step IDs before any T-10 rows | DO NOT write recovery without a specific IB-NN Step ID citation |
| CMD-14 | Shared | Cite specific IB-NN Step ID in every T-10 row | DO NOT name the process category only |
| CMD-15 | Operations | Produce T-11 with one row per NH-NN and LP-NN | DO NOT substitute an aggregate count for per-row status |
| CMD-16 | Finance / Operations | Close each phase with its named PG-NN gate | DO NOT advance until gate shows all GO |
| CMD-17 | Shared | CMD register is first scaffold row; all CMD Binding and Role Owner columns populated | DO NOT produce any scaffold row without CMD Binding AND Role Owner |
| CMD-18 | Shared | Produce T-PARITY GO: final [M] matches arithmetic sum of all stage [N] values | DO NOT mark T-PARITY GO if any per-stage N value is inconsistent |
| CMD-19 | Shared | Close every stage trace: CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total | DO NOT write a checkpoint with [N] only — [M] cumulative is required |
| CMD-20 | Shared | Carry T-07 Running Total column in every PG-NN gate block | DO NOT produce a PG-NN gate without T-07 Running Total column |

---

### PG-01: Phase 1 Gate (Finance Controller)

| Required Artifact | Status | T-07 Running Total | Go/No-Go |
|------------------|--------|--------------------|---------|
| CMD as first scaffold row (Role Owner = Shared) | | 0 | |
| All scaffold rows carry CMD Binding AND Role Owner | | 0 | |
| All PG-NN rows declare T-07 Running Total in Mandatory Columns | | 0 | |
| T-01 through T-11 and T-PARITY declared with Mandatory Columns | | 0 | |
| Stage assignment map in T-03 showing all stages assigned to a role | | 0 | |

Phase 2 may not begin if any row shows NO-GO.

---

## PHASE 2: FINANCE CONTROLLER — PRE-TRACE AND STAGES 1-3

### T-01: Entity Inventory (Shared)

| Entity | Description | Key Fields |
|--------|-------------|-----------|

---

### T-02: FM-NN Prediction Register (Shared)

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

### T-03: Stage Enumeration with Assignment Map (Shared)

| Stage ID | Stage Name | Description | Assigned Role |
|----------|------------|-------------|--------------|

---

### T-04: Boundary Inventory (Shared)

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

---

### T-08: SLA Domination Point (Finance)

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

---

### T-05: Incumbent Baseline (Shared)

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

---

### Finance Stage Traces: Stages 1-3

For each Finance-owned stage:

1. Schema at entry.
2. Processing.
3. Loss points (LP-NN).
4. No-handling annotations (NH-NN).
5. T-06F typed exit manifest.
6. T-07 append-log rows.
7. Dual-count checkpoint:
   ```
   CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total. (Finance CMD-19)
   ```

---

### PG-02: Finance/Operations Handoff Gate

| Required Artifact | Finance Status | T-07 Running Total at Handoff | Go/No-Go |
|------------------|----------------|------------------------------|---------|
| T-01, T-02, T-03, T-04, T-05, T-08 populated | | [M after Finance Stage 3] | |
| T-06F manifests for all Finance-owned stages | | | |
| T-07 dual-count checkpoints for Stages 1-3 | | | |
| T-04 entity.field stubs back-filled from T-06F | | | |

T-07 Running Total at handoff = [M after Stage 3].
Operations Analyst begins with this [M] as its starting running total.
Operations may not begin until all rows show GO.

---

## PHASE 3: OPERATIONS ANALYST — STAGES 4-6

Operations Analyst takes over from PG-02 handoff. The T-07 running total continues
from [M at handoff]. Operations' per-stage checkpoints carry [M] accumulating from
the Finance handoff value.

### Operations Stage Traces: Stages 4-6

For each Operations-owned stage:

1. Schema at entry (reference T-06F manifests for upstream field types).
2. Processing.
3. Loss points (LP-NN).
4. No-handling annotations (NH-NN).
5. T-06O typed exit manifest.
6. T-07 append-log rows.
7. Dual-count checkpoint:
   ```
   CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total. (Operations CMD-19)
   [M] = [M from prior checkpoint] + [N this stage].
   ```

After all Operations stages: back-fill T-04 entity.field stubs from T-06O manifests.

---

### PG-03: Phase 3 Gate (Operations Analyst)

| Required Artifact | Status | T-07 Running Total | Go/No-Go |
|------------------|--------|--------------------|---------|
| T-06O manifests for all Operations stages | | [cumulative M] | |
| Dual-count checkpoints for Stages 4-6 | | | |
| T-04 entity.field stubs back-filled from T-06O | | | |
| All boundaries annotated NH-NN or with mechanism | | | |
| At least one LP-NN per Operations stage | | | |

T-07 Running Total = [M] from Stage 6 checkpoint.
Phase 4 may not begin if any row shows NO-GO.

---

## PHASE 4: OPERATIONS ANALYST — POST-TRACE RESOLUTION

### T-09: FM-NN Resolution Audit (Operations produces)

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

---

### T-10: Recovery Audit Table (Shared)

| NH/LP ID | Triggering Condition | Recovery Mechanism | IB-NN Step Cited | Boundary / Stage |
|----------|---------------------|--------------------|-----------------|-----------------|

---

### T-11: Closure Gate (Operations produces)

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

---

### T-PARITY: Count Parity Gate (Shared)

| Stage ID | N Rows This Stage | Running Total | GO / FLAG |
|----------|------------------|---------------|-----------|

Include ALL stages (Finance + Operations). Final: SUM == [M final]. GO or FLAG.

---

### Trade-off Analysis

One alternative pattern; two trade-off dimensions; at least one quantified in
domain terms.

---

### PG-04: Phase 4 Gate (Operations Analyst)

| Required Table | Status | T-07 Running Total | Go/No-Go |
|---------------|--------|--------------------|---------|
| T-09 (all FM-NN resolved) | | [final M] | |
| T-10 (one row per NH-NN and LP-NN) | | [final M] | |
| T-11 (one row per identifier) | | [final M] | |
| T-PARITY (GO confirmed) | | [final M] | |

T-07 Running Total at PG-04 = [final M]. Must match T-PARITY sum.
```

---

## V-04 — Phrasing Register: Coaching-Imperative with Explicit Accumulation Arithmetic

**Axis**: Phrasing register — instructional/coaching rather than command-and-prohibit.
The prompt teaches the accumulation arithmetic explicitly ("M at stage k = M at stage
k-1 + N at stage k") and coaches the model through the running-total column as a
taught quantity rather than a named column contract. CMD is still entry zero; CMD
Binding still on every scaffold row; running total column still in every PG-NN entry.
But the language is "I need you to track two numbers" rather than "DO NOT omit [M]."
**Hypothesis**: orienting the model to the computation — naming the arithmetic as a
formula to be applied — produces correct [M] values (not just structural presence of [M])
because the model is coached to calculate [M], not just to emit a column named [M].

---

```
You are a Finance / Operations / Commerce data domain expert. I need you to trace
data through the following pipeline in careful, structured detail:

{topic}

I'm going to walk you through a five-phase protocol. Each phase has a gate you must
pass before moving to the next. Here's what I need you to track and why.

---

**The accumulation audit.** As you trace each stage, I need you to track two numbers
for the FM-NN append-log (T-07):

- N: how many rows did you add to T-07 at this stage?
- M: how many rows are in T-07 total, including all stages through this one?

The relationship is: M at stage k = M at stage k-1 + N at stage k.

At the close of every stage trace, write:

```
CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total.
```

Then, at the close of each phase gate, tell me the current T-07 running total — this
is the M from the most recent checkpoint. I'll call this the T-07 Running Total column
in every gate block. At the end, T-PARITY verifies that the sum of all N values equals
M final.

---

**The compliance contract.** I want you to write a CMD register before anything else —
it's the first row of the scaffold AND the first table you produce. Every other table
in your scaffold carries a CMD Binding column naming which CMD entries govern it. This
makes every structural shortfall attributable to a named contract obligation, not just
a missed instruction.

---

## STEP 0: Output Scaffold

The CMD register is your first scaffold row — before T-01, before any gate, before
T-PARITY. Every other row carries a CMD Binding column. Every PG-NN row also carries
the T-07 Running Total column in its Mandatory Columns (because I'll be asking for
that running total in every gate block).

| T#       | Table Name                  | Purpose                                             | Mandatory Columns (exact names)                                                                                              | CMD Binding              | Depends On        |
|----------|-----------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------|-------------------|
| CMD      | Structural Compliance Register | Your contract; produced first; shortfalls cite this by ID | CMD ID, Positive Imperative, DO NOT Prohibition                                                               | —                        | —                 |
| T-01     | Entity Inventory            | Every domain entity named before Stage 1           | Entity, Description, Key Fields                                                                                              | CMD-07                   | —                 |
| T-02     | FM-NN Prediction Register   | Your hypotheses about what will go wrong           | FM-NN, Anticipated Event, Domain Consequence, Expected Designation                                                           | CMD-03                   | —                 |
| T-03     | Stage Enumeration           | The pipeline stages, sequenced                     | Stage ID, Stage Name, Description                                                                                            | CMD-08                   | —                 |
| T-04     | Boundary Inventory          | What happens between stages — latency, risk, cost  | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | CMD-09, CMD-10, CMD-11 | T-03            |
| T-05     | Incumbent Baseline          | What people did before this pipeline existed        | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency                                                               | CMD-13                   | —                 |
| T-06     | Stage Exit Manifests        | The exact schema leaving each stage                | field_name, TYPE(precision), Notes                                                                                           | CMD-05                   | T-03              |
| T-07     | FM-NN Append-Log            | Your running record of where failures touched each stage | FM-NN, Stage ID, Boundary / Condition, Deferral Statement                                                               | CMD-04, CMD-17, CMD-18   | T-02, T-03        |
| T-08     | SLA Domination Point        | Where the SLA budget is consumed                   | Domination Boundary, Exact Cumulative SLA%, Justification                                                                    | CMD-12                   | T-04              |
| T-09     | FM-NN Resolution Audit      | Your verdict on each hypothesis                    | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason                                                                       | CMD-03                   | T-02, T-07        |
| T-10     | Recovery Audit Table        | What to do when things go wrong                    | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage                                      | CMD-13, CMD-14           | T-04, T-05, T-06  |
| T-11     | Closure Gate                | Confirm every risk has a recovery row              | Identifier, Source (Stage / Boundary), T-10 Row, Status                                                                     | CMD-15                   | T-10              |
| T-PARITY | Count Parity Gate           | Verify the accumulation math adds up               | Stage ID, N Rows This Stage, Running Total, GO / FLAG                                                                        | CMD-06, CMD-19           | T-07              |
| PG-01    | Phase 1 Gate                | Check that the contract and scaffold are complete  | Required Artifact, Declaration Status, CMD Binding Status, T-07 Running Total, Go/No-Go                                      | CMD-01, CMD-16, CMD-20   | CMD, T-01–T-11, T-PARITY |
| PG-02    | Phase 2 Gate                | Check that all pre-trace tables are filled         | Required Table, Population Status, T-07 Running Total, Go/No-Go                                                              | CMD-01, CMD-16, CMD-20   | T-01–T-05, T-08   |
| PG-03    | Phase 3 Gate                | Check that all stage traces are complete           | Required Artifact, Completion Status, T-07 Running Total, Go/No-Go                                                           | CMD-01, CMD-04, CMD-16, CMD-20 | T-03, T-06, T-07 |
| PG-04    | Phase 4 Gate                | Check that all post-trace work is complete         | Required Table, Population Status, T-07 Running Total, Go/No-Go                                                              | CMD-01, CMD-06, CMD-16, CMD-20 | T-09–T-11, T-PARITY |

About the scaffold:
- CMD is row one. That's the contract. Everything else is governed by it.
- CMD Binding on every row tells me which CMD entries govern that table.
- T-07 Running Total in every PG-NN Mandatory Columns means I expect you to tell me
  the current M in every gate block.

---

### CMD: Structural Compliance Register

Write this table first — before T-01, before any other table.

| CMD ID | Positive Imperative | DO NOT Prohibition |
|--------|--------------------|--------------------|
| CMD-01 | Declare CMD as scaffold row one — before T-01 | DO NOT list any T-NN, PG-NN, or T-PARITY before CMD in the scaffold |
| CMD-02 | Use "Mandatory Columns (exact names)" as the column contract label in the scaffold | DO NOT use "Key Columns," "Required Fields," or any descriptive paraphrase |
| CMD-03 | Produce T-02 FM-NN Prediction Register before Stage 1; hold all resolutions for T-09 | DO NOT write CONFIRMED / EXONERATED / NEW inline during stage traces |
| CMD-04 | Append T-07 rows as table rows during each stage trace; close with dual-count checkpoint | DO NOT embed FM-NN acknowledgments as prose bullets within stage sections |
| CMD-05 | Write one T-06 typed exit manifest per stage: field_name: TYPE(precision) | DO NOT describe schema state in prose without typed field assertions |
| CMD-06 | Produce T-PARITY as a standalone table showing per-stage N values and arithmetic | DO NOT substitute a prose sentence or gate column annotation for T-PARITY |
| CMD-07 | List every domain entity in T-01 before Stage 1 | DO NOT introduce an entity during traces that was not declared in T-01 |
| CMD-08 | List every pipeline stage in T-03 before Stage 1 | DO NOT reference a stage in trace content with no T-03 row |
| CMD-09 | Give every inter-stage boundary a B[N]->[N+1] label in T-04 | DO NOT reference a boundary without the B[N]->[N+1] label |
| CMD-10 | Report Transport (ms) and Processing (ms) as separate columns in T-04 | DO NOT use a single "Boundary Latency" column; do not write "Negligible" as a value |
| CMD-11 | Write entity.field in T-04 using field names from T-06 manifests | DO NOT use "data," "records," or "payload" as entity-at-risk |
| CMD-12 | Produce T-08 SLA Domination Point as its own standalone table | DO NOT embed the domination point as a prose footnote to T-04 |
| CMD-13 | Produce T-05 Incumbent Baseline with IB-NN step IDs before any T-10 rows | DO NOT write a recovery row without citing a specific IB-NN step ID |
| CMD-14 | Write a specific IB-NN Step ID in every T-10 "IB-NN Step Cited" cell | DO NOT write the process name only — write "IB-04" not "the reconciliation process" |
| CMD-15 | Write one T-11 row per NH-NN and LP-NN identifier | DO NOT replace per-row status with an aggregate count |
| CMD-16 | Close each phase with its PG-NN gate block | DO NOT begin the next phase until all gate rows show GO |
| CMD-17 | Carry CMD Binding column on every non-CMD scaffold row | DO NOT leave CMD Binding blank or write "—" on any T-NN, PG-NN, or T-PARITY row |
| CMD-18 | Close every stage trace with: CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total | DO NOT write just [N] — I need M = (prior M) + N, arithmetic shown |
| CMD-19 | Verify T-PARITY: sum of all N values equals final M from last checkpoint | DO NOT mark T-PARITY GO if the arithmetic does not close |
| CMD-20 | Include T-07 Running Total column in every PG-NN gate block | DO NOT produce a gate block without this column — it's how I track M at each phase |

---

### PG-01: Phase 1 Gate

Before I move to Phase 2, confirm:

| Required Artifact | Declaration Status | CMD Binding Status | T-07 Running Total | Go/No-Go |
|------------------|--------------------|--------------------|-------------------|---------|
| CMD register (CMD-01 through CMD-20) as first scaffold row | | | n/a | |
| Every scaffold row has CMD Binding populated | | | n/a | |
| Every PG-NN row declares T-07 Running Total in Mandatory Columns | | | n/a | |
| T-01 through T-11 and T-PARITY in scaffold with Mandatory Columns label | | | n/a | |

Phase 2 may not begin if any row shows NO-GO.

---

## PHASE 2: PRE-TRACE TABLES

### T-01: Entity Inventory

Name every domain entity that appears in this pipeline. Use domain vocabulary:
Invoice, PurchaseOrder, LedgerEntry, SKU, InventoryRecord, ShipmentAdvice,
VendorInvoice, CostCenter, GLAccount, RevenueEvent, etc.

| Entity | Description | Key Fields |
|--------|-------------|-----------|

---

### T-02: FM-NN Prediction Register

Before I look at any stage, I want your hypotheses. What do you think will break?
Minimum 3 entries. Write the Expected Designation you predict (will it be a
no-handling annotation NH-NN, or a data loss point LP-NN?).

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

### T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

### T-04: Boundary Inventory

For each inter-stage boundary:
- Split latency into Transport (ms) and Processing (ms) — two separate columns.
  Numbers only — not "Negligible." Their sum is Total (ms).
- Entity at Risk: name the domain entity from T-01.
- entity.field: use "→ back-fill from T-06.[Stage ID]" until you've written that stage's manifest.
- Boundary label: B[N]->[N+1] format.
- SLA%: what fraction of the total SLA budget does this boundary consume?

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

When T-04 is done, add a footnote: "See T-08 for domination analysis."

---

### T-08: SLA Domination Point

One row. Which boundary is where the cumulative SLA% first crosses 50%?

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

---

### T-05: Incumbent Baseline

What did people do before this pipeline existed? I need at least 4 named steps with
IB-NN identifiers. I'll cite these in T-10 — every recovery action needs to anchor
to one of these steps.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

---

### PG-02: Phase 2 Gate

| Required Table | Population Status | T-07 Running Total | Go/No-Go |
|---------------|-------------------|--------------------|---------|
| T-01 | | 0 | |
| T-02 (min 3 entries) | | 0 | |
| T-03 | | 0 | |
| T-04 | | 0 | |
| T-05 (min 4 steps) | | 0 | |
| T-08 | | 0 | |

T-07 Running Total = 0 at PG-02 (no stage traces have run yet).
Phase 3 may not begin if any row shows NO-GO.

---

## PHASE 3: STAGE TRACES

For each stage in T-03, work through these steps:

**Schema at entry** — what fields come in? What types?

**Processing** — what transformations, enrichments, or filtrations happen?

**Loss points** — name at least one specific thing that can drop data at this stage.
Use LP-NN identifiers (LP-01, LP-02, etc.).

**No-handling annotations** — if a boundary has no error recovery, write:
"NH-NN: [description] — no handling, risk accepted."

**Typed exit manifest (T-06)** — produce the exit manifest right here, for this stage:
| field_name | TYPE(precision) | Notes |

**T-07 append-log rows** — for each FM-NN from T-02 that touches this stage's boundary
or processing, add a row to T-07 now:
| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |

**Dual-count checkpoint** — close each stage with this exact form:
```
CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total.
```
Where M = (M from prior checkpoint) + N. Show that arithmetic.
For Stage 1: M = N (the running total starts here).
For Stage 2: M = (M from Stage 1) + N.
And so on.

After all stages: go back to T-04 and fill in the entity.field stubs from the
T-06 manifests you've now written.

---

### PG-03: Phase 3 Gate

| Required Artifact | Completion Status | T-07 Running Total | Go/No-Go |
|------------------|-------------------|--------------------|---------|
| T-06 exit manifest for every stage | | [M from final stage checkpoint] | |
| T-07 rows for every FM-NN that touched a stage | | | |
| Dual-count checkpoint (with both N and M) for every stage | | | |
| T-04 entity.field stubs back-filled | | | |
| At least one LP-NN per stage | | | |
| Every boundary annotated NH-NN or with a mechanism | | | |

T-07 Running Total here = M from the last stage checkpoint.
Phase 4 may not begin if any row shows NO-GO.

---

## PHASE 4: POST-TRACE RESOLUTION

### T-09: FM-NN Resolution Audit

Now resolve every hypothesis from T-02. Look at T-07 to see which stages each
FM-NN touched.

- CONFIRMED: it materialized. Cite the specific NH-NN or LP-NN identifier.
- EXONERATED: it didn't happen. Say exactly why not.
- NEW: something emerged during the trace that I didn't predict. Assign it an
  NH-NN or LP-NN identifier now.

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

---

### T-10: Recovery Audit Table

For every NH-NN and LP-NN, write a recovery row. The IB-NN Step Cited must be a
specific step from T-05 — write "IB-03", not "the manual reconciliation process."

| NH/LP ID | Triggering Condition | Recovery Mechanism | IB-NN Step Cited | Boundary / Stage |
|----------|---------------------|--------------------|-----------------|-----------------|

---

### T-11: Closure Gate

One row per identifier. CLOSED means T-10 has a row for it. OPEN means it doesn't.

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

---

### T-PARITY: Count Parity Gate

List every stage, its N (rows added at that stage), and the running total through
that stage. Show the arithmetic. The final running total must equal M from the last
stage checkpoint.

| Stage ID | N Rows This Stage | Running Total | GO / FLAG |
|----------|------------------|---------------|-----------|

Final line: SUM([N1]+[N2]+...+[Nk]) == [M final]. GO or FLAG.

---

### Trade-off Analysis

Name one alternative pipeline pattern. Give me two trade-off dimensions, at least
one in domain-specific terms (e.g., "hourly batch vs. real-time CDC: reduces invoice
staleness from 60min to <1min but adds 200-500ms per-event processing overhead").

---

### PG-04: Phase 4 Gate

| Required Table | Population Status | T-07 Running Total | Go/No-Go |
|---------------|-------------------|--------------------|---------|
| T-09 (all FM-NN resolved) | | [final M] | |
| T-10 (one row per NH-NN and LP-NN) | | [final M] | |
| T-11 (one row per identifier) | | [final M] | |
| T-PARITY (arithmetic shown, GO confirmed) | | [final M] | |
| Trade-off analysis | | [final M] | |

T-07 Running Total at PG-04 = M from T-PARITY. Must match.
```

---

## V-05 — Inertia Framing: Incumbent Baseline Before Scaffold, Accumulation Woven into IB-NN Coverage

**Axis**: Inertia framing — the incumbent baseline (T-05) is produced before the
scaffold is declared, and it is the structural anchor for both recovery prescriptions
(C-14/C-15/C-16) and the accumulation audit (C-40/C-41). Every T-07 checkpoint carries
three counts: [N] rows appended, [M] total, and [IB-NN steps covered through this stage].
Every PG-NN gate carries T-07 Running Total AND IB-NN Coverage columns. The CMD Binding
column on every scaffold row names both the structural CMD entries AND the IB-NN
anchoring CMD entries. CMD is still entry zero; its production is the only thing that
precedes T-05.
**Hypothesis**: weaving accumulation into IB-NN coverage creates compound enforcement
pressure — a checkpoint missing [M] is also missing IB-NN coverage evidence, making
the dual-count failure doubly visible; a gate missing T-07 Running Total is also missing
IB-NN coverage, so C-40 failure is simultaneously a C-15/C-16 traceability gap.

---

```
You are a Finance / Operations / Commerce data domain expert. Before tracing the
pipeline, establish what existed before it. The incumbent baseline anchors every
recovery action and every accumulation checkpoint.

Pipeline:

{topic}

---

STRUCTURAL RULE: Your first table is the CMD register. Your second table is the
Incumbent Baseline (T-05). Your third table is the output scaffold — declared only
after CMD and T-05 exist. The scaffold's first row (after CMD) is T-05 itself,
declared as pre-produced. Every subsequent scaffold row carries a CMD Binding column
naming the CMD-NN entries that govern it. CMD is pre-scaffold entry zero; its scaffold
row appears first.

---

## PRE-SCAFFOLD SECTION

### CMD: Structural Compliance Register

Produce this table first — before any scaffold, before T-05.

| CMD ID | Positive Imperative | DO NOT Prohibition |
|--------|--------------------|--------------------|
| CMD-01 | Declare CMD as the first scaffold row before any T-NN | DO NOT list any T-NN artifact before CMD in the scaffold |
| CMD-02 | Use "Mandatory Columns (exact names)" as scaffold column contract label | DO NOT use "Key Columns," "Required Fields," or any descriptive variant |
| CMD-03 | Produce T-02 FM-NN Prediction Register before Stage 1; resolve in T-09 only | DO NOT write CONFIRMED / EXONERATED / NEW inline during stage traces |
| CMD-04 | Append T-07 rows as table rows during each stage trace; close with triple-count checkpoint | DO NOT embed FM-NN acknowledgments as prose bullets |
| CMD-05 | Produce one T-06 typed exit manifest per stage | DO NOT state schema in prose without typed field assertions |
| CMD-06 | Produce T-PARITY as a standalone table with per-stage N and arithmetic | DO NOT substitute a prose sentence or gate column for T-PARITY |
| CMD-07 | List all domain entities in T-01 before Stage 1 | DO NOT introduce an entity during traces not declared in T-01 |
| CMD-08 | Enumerate all stages in T-03 before Stage 1 | DO NOT reference a stage with no T-03 row |
| CMD-09 | Label every boundary B[N]->[N+1] in T-04 | DO NOT reference a boundary without the B[N]->[N+1] label |
| CMD-10 | Decompose latency: Transport (ms) and Processing (ms) as separate columns | DO NOT use a single "Boundary Latency" column; "Negligible" is not valid |
| CMD-11 | Use entity.field from T-06 manifests in T-04 | DO NOT use "data," "records," or "payload" as entity-at-risk |
| CMD-12 | Produce T-08 SLA Domination Point as a standalone table | DO NOT embed domination as prose appended to T-04 |
| CMD-13 | Produce T-05 Incumbent Baseline with IB-NN Step IDs before the scaffold | DO NOT write the scaffold before T-05 exists |
| CMD-14 | Cite a specific IB-NN Step ID in every T-10 row | DO NOT name the process category only |
| CMD-15 | Produce T-11 with one row per NH-NN and LP-NN | DO NOT substitute an aggregate count for per-row status |
| CMD-16 | Close each phase with its named PG-NN gate block | DO NOT advance until the gate shows all GO |
| CMD-17 | Carry CMD Binding on every non-CMD scaffold row | DO NOT leave CMD Binding blank on any T-NN, PG-NN, or T-PARITY row |
| CMD-18 | Close every stage trace: CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total, IB-NN steps covered: [list] | DO NOT write a checkpoint with [N] only or with [M] only; IB-NN coverage is required |
| CMD-19 | Carry T-07 Running Total AND IB-NN Coverage columns in every PG-NN gate block | DO NOT produce a gate block without both T-07 Running Total and IB-NN Coverage columns |
| CMD-20 | Verify T-PARITY: sum of all N equals final M from last checkpoint | DO NOT mark T-PARITY GO if arithmetic does not close |

---

### T-05: Incumbent Baseline (produced before scaffold — CMD-13)

What process existed before this pipeline? Minimum 4 steps with IB-NN identifiers.
These are the anchors: every T-10 recovery row cites a specific IB-NN step. Every
stage trace checkpoint reports which IB-NN steps are covered through that stage.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

---

## STEP 0: Output Scaffold (produced after CMD and T-05 exist)

| T#       | Table Name                  | Purpose                                             | Mandatory Columns (exact names)                                                                                              | CMD Binding                    | Depends On         |
|----------|-----------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------|
| CMD      | Structural Compliance Register | Pre-scaffold meta-contract; produced before this scaffold | CMD ID, Positive Imperative, DO NOT Prohibition                                                               | —                              | —                  |
| T-05     | Incumbent Baseline          | Pre-scaffold; IB-NN step IDs anchor T-10 and checkpoints | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency                                                          | CMD-13                         | —                  |
| T-01     | Entity Inventory            | Domain entities; all trace references bind here    | Entity, Description, Key Fields                                                                                              | CMD-07                         | —                  |
| T-02     | FM-NN Prediction Register   | Pre-trace failure hypotheses; T-09 resolves        | FM-NN, Anticipated Event, Domain Consequence, Expected Designation                                                           | CMD-03                         | —                  |
| T-03     | Stage Enumeration           | Named and sequenced pipeline stages                | Stage ID, Stage Name, Description                                                                                            | CMD-08                         | —                  |
| T-04     | Boundary Inventory          | Boundaries; latency; entity-at-risk; SLA%          | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | CMD-09, CMD-10, CMD-11       | T-03               |
| T-06     | Stage Exit Manifests        | Typed exit manifest per stage                      | field_name, TYPE(precision), Notes                                                                                           | CMD-05                         | T-03               |
| T-07     | FM-NN Append-Log            | Accumulating per-stage rows; triple-count checkpoint | FM-NN, Stage ID, Boundary / Condition, Deferral Statement                                                                   | CMD-04, CMD-18                 | T-02, T-03         |
| T-08     | SLA Domination Point        | Standalone domination boundary                     | Domination Boundary, Exact Cumulative SLA%, Justification                                                                    | CMD-12                         | T-04               |
| T-09     | FM-NN Resolution Audit      | Post-trace FM-NN lifecycle resolution              | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason                                                                       | CMD-03                         | T-02, T-07         |
| T-10     | Recovery Audit Table        | NH-NN/LP-NN recovery; IB-NN step citations         | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage                                      | CMD-14, CMD-13                 | T-04, T-05, T-06   |
| T-11     | Closure Gate                | Per-identifier CLOSED / OPEN                       | Identifier, Source (Stage / Boundary), T-10 Row, Status                                                                     | CMD-15                         | T-10               |
| T-PARITY | Count Parity Gate           | Cross-stage arithmetic parity; Tier 3 verification | Stage ID, N Rows This Stage, Running Total, GO / FLAG                                                                        | CMD-06, CMD-20                 | T-07               |
| PG-01    | Phase 1 Gate                | CMD + T-05 pre-declaration + scaffold check        | Required Artifact, Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                      | CMD-01, CMD-16, CMD-17, CMD-19 | CMD, T-05, T-01–T-11, T-PARITY |
| PG-02    | Phase 2 Gate                | Pre-trace table population                         | Required Table, Population Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                              | CMD-01, CMD-16, CMD-19         | T-01–T-04, T-08    |
| PG-03    | Phase 3 Gate                | Stage trace completeness + checkpoint verification  | Required Artifact, Completion Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                           | CMD-01, CMD-04, CMD-16, CMD-19 | T-03, T-06, T-07   |
| PG-04    | Phase 4 Gate                | Post-trace resolution + T-PARITY                   | Required Table, Population Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                              | CMD-01, CMD-06, CMD-16, CMD-19 | T-09, T-10, T-11, T-PARITY |

Notes:
- CMD is scaffold row one (C-38 satisfied). CMD Binding on every non-CMD row (C-39 satisfied).
- Every PG-NN row declares T-07 Running Total AND IB-NN Coverage in Mandatory Columns (C-40 extended).
- CMD-18 requires triple-count checkpoint: [N], [M], and [IB-NN steps covered] (C-41 extended).
- T-05 appears as row 2 in the scaffold, marked as "produced before scaffold" — this signals
  its pre-production status to downstream citation checks.

---

### PG-01: Phase 1 Gate

| Required Artifact | Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|------------------|--------|--------------------|----------------|---------|
| CMD register produced before scaffold | | 0 | n/a | |
| T-05 Incumbent Baseline produced before scaffold (min 4 IB-NN steps) | | 0 | all IB-NN steps declared | |
| CMD as first scaffold row | | 0 | n/a | |
| Every scaffold row carries CMD Binding | | 0 | n/a | |
| Every PG-NN row declares T-07 Running Total AND IB-NN Coverage in Mandatory Columns | | 0 | n/a | |
| T-01 through T-11 and T-PARITY declared | | 0 | n/a | |

Phase 2 may not begin if any row shows NO-GO.

---

## PHASE 2: PRE-TRACE DECLARATIONS

### T-01: Entity Inventory

| Entity | Description | Key Fields |
|--------|-------------|-----------|

---

### T-02: FM-NN Prediction Register

For each prediction, consider whether it maps to a known T-05 incumbent process step —
do modern pipelines carry the same failure modes as manual processes, or do they
introduce new ones?

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

### T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

### T-04: Boundary Inventory

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

---

### T-08: SLA Domination Point

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

---

### PG-02: Phase 2 Gate

| Required Table | Population Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|---------------|-------------------|--------------------|----------------|---------|
| T-01 | | 0 | n/a | |
| T-02 (min 3 entries) | | 0 | n/a | |
| T-03 | | 0 | n/a | |
| T-04 | | 0 | n/a | |
| T-08 | | 0 | n/a | |

T-07 Running Total = 0. IB-NN Coverage = T-05 declared (IB-01 through IB-NN available).
Phase 3 may not begin if any row shows NO-GO.

---

## PHASE 3: STAGE TRACES

For each stage in T-03:

1. **Schema at entry** — field types received.
2. **Processing** — transformations applied.
3. **Loss points (LP-NN)** — at least one named data loss point.
4. **No-handling annotations (NH-NN)** — every unhandled boundary explicitly flagged.
5. **T-06 typed exit manifest** — produce here.
6. **T-07 append-log rows** — append for every FM-NN intersection.
7. **Triple-count checkpoint**:

```
CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total, IB-NN steps covered through this stage: [IB-01, IB-02, ...].
```

- [N] = rows appended at this stage.
- [M] = running total: (prior M) + N. Show arithmetic.
- IB-NN steps covered = cumulative list of all T-05 step IDs whose fallback process
  is now covered by a recovery action through this stage. This list grows as more
  NH-NN and LP-NN are assigned IB-NN anchors in T-10.

After all stages: back-fill T-04 entity.field stubs from T-06 manifests.

---

### PG-03: Phase 3 Gate

| Required Artifact | Completion Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|------------------|-------------------|--------------------|----------------|---------|
| T-06 manifest for every stage | | [M from final checkpoint] | [IB-NN steps covered] | |
| T-07 rows for all FM-NN intersections | | | | |
| Triple-count checkpoints (N, M, IB-NN) for every stage | | | | |
| T-04 entity.field stubs back-filled | | | | |
| At least one LP-NN per stage | | | | |
| All boundaries annotated NH-NN or with mechanism | | | | |

T-07 Running Total = M from last stage checkpoint.
IB-NN Coverage = cumulative list of T-05 steps with assigned recovery actions so far.
Phase 4 may not begin if any row shows NO-GO.

---

## PHASE 4: POST-TRACE RESOLUTION

### T-09: FM-NN Resolution Audit

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

---

### T-10: Recovery Audit Table

Every NH-NN and LP-NN. IB-NN Step Cited = specific T-05 Step ID. As you fill T-10,
the IB-NN steps covered list from your checkpoints should expand — every new IB-NN
citation is a step now covered by a named recovery action.

| NH/LP ID | Triggering Condition | Recovery Mechanism | IB-NN Step Cited | Boundary / Stage |
|----------|---------------------|--------------------|-----------------|-----------------|

---

### T-11: Closure Gate

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

---

### T-PARITY: Count Parity Gate

| Stage ID | N Rows This Stage | Running Total | GO / FLAG |
|----------|------------------|---------------|-----------|

Final: SUM([N1]+[N2]+...+[Nk]) == [M final]. GO or FLAG.
Cross-check: [M final] must match T-07 Running Total at PG-04.

---

### IB-NN Coverage Reconciliation

Enumerate every T-05 step. For each: is it cited in at least one T-10 row?

| IB-NN Step | Step Name | T-10 Row(s) Citing | Coverage Status |
|-----------|-----------|--------------------|----------------|

A T-05 step with no T-10 citation is UNCOVERED. This is a C-16 gap.

---

### Trade-off Analysis

One alternative pattern. Two trade-off dimensions, at least one quantified in
domain terms. Where possible, anchor the comparison to T-05 baseline metrics
(e.g., "batch pipeline adds 4-hour AP ledger latency vs. T-05 IB-03 same-day
manual reconciliation; CDC alternative reduces to <5min but doubles infrastructure
cost and eliminates the audit trail provided by IB-02 manual verification step").

---

### PG-04: Phase 4 Gate

| Required Table | Population Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|---------------|-------------------|--------------------|----------------|---------|
| T-09 (all FM-NN resolved) | | [final M] | [final coverage list] | |
| T-10 (one row per NH-NN and LP-NN) | | [final M] | | |
| T-11 (one row per identifier) | | [final M] | | |
| T-PARITY (arithmetic shown, GO) | | [final M] | | |
| IB-NN Coverage Reconciliation (all steps COVERED or gap cited) | | [final M] | all IB-NN steps | |
| Trade-off analysis (IB-baseline anchored) | | [final M] | | |

T-07 Running Total at PG-04 = [final M] from T-PARITY.
IB-NN Coverage at PG-04 = all T-05 steps with T-10 citations.
```
