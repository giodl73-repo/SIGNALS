# flow-dataflow — Round 20 Variations (Rubric v17)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v17 (C-01 through C-46, essential/recommended/aspirational tiers, max 111.35)
**Date**: 2026-03-15

---

## Variation Design Notes

R20 targets the five criteria added in v17 from R19 evidence:

**C-42 -- IB-NN Coverage column in PG-NN gate blocks**: R19 V-05 introduced the IB-NN
Coverage column alongside T-07 Running Total in gate blocks, but only as a V-05 axis
behavior. R20 must make this column a universal CMD entry with a named DO NOT prohibition,
pre-declared in Mandatory Columns for every PG-NN scaffold row.

**C-43 -- IB table precedes scaffold as artifact zero**: R19 produced T-05 as a
pre-trace artifact declared in the scaffold. The gap: T-05 always followed the scaffold
declaration, meaning the scaffold was the governing reference and IB was a downstream
artifact it declared. C-43 requires the IB table to appear before the scaffold. R20
must restructure Phase 1 into STEP 0a (IB Table) and STEP 0b (Scaffold), so that the
scaffold's T-05 entry references an already-existing artifact rather than declaring it
for the first time.

**C-44 -- Triple-count checkpoint**: R19 V-01 through V-05 produced dual-count
checkpoints (C-41 satisfied). The gap: no checkpoint carried the IB-NN coverage list.
R20 must add CMD-23 prohibiting the dual-count-only form and enforce the triple-count
form: CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total, IB-NN steps
covered: [list].

**C-45 -- Role-attributed rows in recovery audit table**: R19 recovery tables carried
four or five columns (triggering condition, recovery mechanism, IB-NN step cited,
boundary/stage reference) but no Responsible Role column. C-45 requires the role to be
drawn from C-10/C-15/C-25 vocabulary -- a generic label ("team," "system") fails. R20
must add CMD-24 and add Responsible Role as a mandatory column in the T-10 scaffold entry.

**C-46 -- Handoff continuity contract at role-transition boundaries**: R19 multi-role
variations (V-03) annotated role-transition boundaries with entity-at-risk (C-17) but
produced no bilateral contract. C-46 requires (1) sending role delivery guarantee and
(2) receiving role acceptance requirement, as named artifact columns or a dedicated
continuity table. R20 must add CMD-25 and pre-declare the continuity contract in the
scaffold -- either as extra columns on T-04 or as a standalone T-12.

---

**What R19 established:**

- Three-tier accumulation protocol as lifecycle spine (V-01) forces dual-count [M]
  into every checkpoint and T-07 Running Total into every PG-NN gate.
- Scaffold column explosion (V-02) with RT-Col? = YES on every PG-NN row made missing
  running-total columns structurally visible from the scaffold.
- Role-owned CMD slices (V-03) attributed structural failures to named roles, making
  gate failures traceable to the role responsible for that phase.
- Coaching-imperative arithmetic (V-04) reliably produced correct [M] values (not just
  column presence) because the arithmetic formula was stated explicitly.
- IB-NN anchoring (V-05) with IB-NN Steps Covered in checkpoints and IB-NN Coverage
  column in gates produced C-42 and C-44 behavior but not yet as universal CMD entries.

---

**R20 hypothesis space:**

**H1 -- IB-as-anchor-zero + triple-count as lifecycle spine (V-01)**
Phase 1 is split into STEP 0a (IB Table, before scaffold) and STEP 0b (Scaffold). The
scaffold's T-05 entry carries "Already produced above" as its Declaration Status, encoding
the before/after relationship structurally. The ACCUMULATION PROTOCOL section gains a
fourth element: IB-NN displacement tracking. Hypothesis: making the scaffold reference an
already-existing IB table forces the ordering -- a model that writes the scaffold first has
no "Already produced above" entry to reference, making the violation self-evident.

**H2 -- Scaffold column explosion: IB-Col? and HO-Col? metadata flags (V-02)**
The scaffold gains two flag columns: IB-Col? (YES/NO -- does this artifact require an
IB-NN Coverage column) and HO-Col? (YES/NO -- does this artifact require handoff contract
columns). Every PG-NN row has IB-Col? = YES; every boundary table row with a role transition
has HO-Col? = YES. Hypothesis: flag columns on scaffold rows create the same enforcement
pressure for IB-NN Coverage and handoff contracts that RT-Col? created for running totals
in R19 -- a scaffold row with IB-Col? = YES and no IB-NN Coverage column in Mandatory
Columns is a structurally visible gap.

**H3 -- Finance/Operations role split with role-owned handoff contracts (V-03)**
Finance Controller owns Stages 1-3 and PG-01/PG-02; Operations Analyst owns Stages 4-6
and PG-03/PG-04. At B3->4 (the role-transition boundary), a dedicated T-12 Handoff
Continuity Contract table captures: Finance Controller's delivery guarantee (named output
from T-06 manifest or scaffold) and Operations Analyst's acceptance requirement (named
precondition). CMD-25 governs T-12; CMD-24 governs the Responsible Role column in T-10.
Hypothesis: naming the handoff table T-12 with a specific scaffold entry and CMD binding
makes the bilateral contract as structurally required as the boundary inventory -- a
role-transition boundary with no T-12 row is a scorable gap.

**H4 -- Coaching-imperative with explicit triple-count arithmetic and role vocabulary (V-04)**
Instructional register. The triple-count arithmetic is taught as a formula: "M_k = M_(k-1)
+ N_k. The IB-NN list at stage k = IB-NN list at stage k-1 union any new IB steps automated
by stage k -- a list that does not grow monotonically is a contradiction." Recovery role
attribution is framed as a question: "For each recovery row, ask: which named role in your
T-05 table actually executes this recovery? Write that role name in the Responsible Role
column." Handoff contracts are framed as: "For each role-transition boundary, name what the
sending role hands off and what the receiving role requires before it can proceed."
Hypothesis: casting structural requirements as taught formulas and diagnostic questions
produces correct content (not just column presence) because the model is oriented to the
computation and the role vocabulary, not just the format label.

**H5 -- Combination: Inertia-first + role-attributed recovery + handoff continuity (V-05)**
IB table is the absolute first artifact produced (C-43). The scaffold's T-05 entry is marked
"Artifact zero -- produced above scaffold." Every T-10 recovery row cites an IB-NN step AND
names the Responsible Role who executes the recovery (C-45). At every role-transition
boundary, the continuity contract appears as two additional columns in T-04: Delivery
Guarantee (sending role, named artifact) and Acceptance Requirement (receiving role, named
precondition) (C-46). Checkpoints are triple-count throughout (C-44). IB-NN Coverage column
appears in every PG-NN gate (C-42). Hypothesis: anchoring the entire pipeline to the
incumbent baseline -- IB before scaffold, IB steps cited in recovery, IB coverage tracked at
every checkpoint and gate, IB vocabulary governing role attribution and handoff contracts --
creates compound enforcement pressure across all five C-42 to C-46 criteria simultaneously,
because they all trace back to the same T-05 table produced first.

---

## V-01 -- Lifecycle Emphasis: IB-as-Anchor-Zero + Triple-Count as Spine

**Axis**: Lifecycle emphasis -- Phase 1 is restructured so that the IB table (STEP 0a)
precedes the scaffold (STEP 0b), making IB the governing reference artifact. The ACCUMULATION
PROTOCOL gains a fourth tier: IB-NN displacement tracking. The scaffold's T-05 entry reads
"Already produced above" in its Declaration Status, encoding the before/after relationship
as a structural fact rather than an instruction.
**Hypothesis**: making the scaffold reference an already-existing IB table forces the
ordering; CMD-22 prohibits writing the scaffold before the IB table is complete; a model
that violates this has no "Already produced above" entry to populate.

---

```
You are a Finance / Operations / Commerce data domain expert. Produce a complete data
flow trace for the following pipeline:

{topic}

---

STRUCTURAL RULE: Your response is organized as five phases. A phase may not open until
the prior phase's gate shows all GO rows. The CMD-NN Structural Compliance Register is
the FIRST entry in your scaffold (STEP 0b) and the FIRST table produced in your response
body. No T-NN, PG-NN, or T-PARITY entry may appear in the scaffold before CMD.

ORDERING RULE: Phase 1 has two sub-steps. STEP 0a produces the Incumbent Baseline table
(T-05) BEFORE the scaffold is written. STEP 0b produces the scaffold, which references
T-05 as "Already produced above." The scaffold's T-05 entry must carry "Already produced
above" in its Declaration Status column. A scaffold that declares T-05 as a future artifact
when T-05 already exists violates CMD-22.

---

## PHASE 1: COMPLIANCE PROTOCOL DECLARATION

### STEP 0a: Incumbent Baseline Table (ARTIFACT ZERO -- produced before scaffold)

Before writing any scaffold, produce the structured Incumbent Baseline (IB) table. This
table is the governing reference from which the pipeline departs. Every scaffold entry
that follows is readable as "this automated artifact replaces or covers that manual step."

| IB-NN | Step Name | Responsible Role | Elapsed Time / Frequency |
|-------|-----------|-----------------|--------------------------|

Rules:
- Minimum 4 IB-NN entries covering every manual step the pipeline will automate.
- Responsible Role must be a named domain actor (AP Clerk, Finance Analyst,
  Operations Manager, Inventory Coordinator, etc.) -- not "team" or "user."
- Elapsed Time must be quantified (e.g., "2 hours," "daily at 17:00") -- not "varies."
- IB-NN identifiers must be sequential: IB-01, IB-02, ... These identifiers are the
  only valid citations in T-10 recovery rows (CMD-13), T-07 append-log rows (CMD-23),
  PG-NN IB-NN Coverage columns (CMD-21), and checkpoint triple-counts (CMD-23).

---

### STEP 0b: Output Scaffold

First row: CMD (Structural Compliance Register). All other rows follow.
The CMD Binding column on every T-NN, PG-NN, and T-PARITY row names the CMD-NN entries
governing that artifact.

| T#       | Table Name                      | Purpose                                                              | Mandatory Columns (exact names)                                                                                                                   | CMD Binding                    | Depends On               |
|----------|---------------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------|
| CMD      | Structural Compliance Register  | Meta-contract; declared first; every shortfall is a named CMD breach | CMD ID, Positive Imperative, DO NOT Prohibition                                                                                                   | --                             | --                       |
| T-01     | Entity Inventory                | Domain entities; all trace references bind to T-01 names            | Entity, Description, Key Fields                                                                                                                   | CMD-07                         | --                       |
| T-02     | FM-NN Prediction Register       | Pre-trace failure hypotheses; resolved in T-09 only                 | FM-NN, Anticipated Event, Domain Consequence, Expected Designation                                                                                | CMD-03                         | --                       |
| T-03     | Stage Enumeration               | Named and sequenced pipeline stages                                  | Stage ID, Stage Name, Description                                                                                                                 | CMD-08                         | --                       |
| T-04     | Boundary Inventory              | Boundaries with latency, entity-at-risk, SLA%, continuity contract  | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA%, Sending Role Delivery Guarantee, Receiving Role Acceptance Requirement | CMD-09, CMD-10, CMD-11, CMD-25 | T-03                     |
| T-05     | Incumbent Baseline              | Already produced above scaffold as artifact zero                     | IB-NN, Step Name, Responsible Role, Elapsed Time / Frequency                                                                                     | CMD-13, CMD-22                 | -- (produced in STEP 0a) |
| T-06     | Stage Exit Manifests            | One typed manifest per stage                                        | field_name, TYPE(precision), Notes                                                                                                                | CMD-05                         | T-03                     |
| T-07     | FM-NN Append-Log                | Accumulating per-stage rows; triple-count checkpoint at each stage  | FM-NN, Stage ID, Boundary / Condition, Deferral Statement                                                                                        | CMD-04, CMD-17, CMD-23         | T-02, T-03               |
| T-08     | SLA Domination Point            | Standalone domination boundary                                       | Domination Boundary, Exact Cumulative SLA%, Justification                                                                                         | CMD-12                         | T-04                     |
| T-09     | FM-NN Resolution Audit          | Post-trace FM-NN lifecycle resolution                                | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason                                                                                            | CMD-03                         | T-02, T-07               |
| T-10     | Recovery Audit Table            | NH-NN/LP-NN recovery with IB-NN step citations and role attribution | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage, Responsible Role                                         | CMD-13, CMD-14, CMD-24         | T-04, T-05, T-06         |
| T-11     | Closure Gate                    | Per-identifier CLOSED / OPEN status for all NH-NN and LP-NN        | Identifier, Source (Stage / Boundary), T-10 Row, Status                                                                                           | CMD-15                         | T-10                     |
| T-PARITY | Count Parity Gate               | Cross-stage arithmetic parity; Tier 3 of accumulation protocol      | Stage ID, N Rows This Stage, Running Total, GO / FLAG                                                                                             | CMD-06, CMD-18                 | T-07                     |
| PG-01    | Phase 1 Gate                    | IB-zero ordering + CMD completeness + scaffold declaration check    | Required Artifact, Declaration Status, CMD Binding Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                          | CMD-01, CMD-16, CMD-19, CMD-21 | CMD, T-01--T-11, T-PARITY |
| PG-02    | Phase 2 Gate                    | Pre-trace table population before Stage 1                           | Required Table, Population Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                                  | CMD-01, CMD-16, CMD-19, CMD-21 | T-01--T-05, T-08         |
| PG-03    | Phase 3 Gate                    | Stage trace completeness + triple-count checkpoint verification     | Required Artifact, Completion Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                               | CMD-01, CMD-04, CMD-16, CMD-19, CMD-21 | T-03, T-06, T-07  |
| PG-04    | Phase 4 Gate                    | Post-trace resolution completeness including T-PARITY               | Required Table, Population Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                                  | CMD-01, CMD-06, CMD-16, CMD-19, CMD-21 | T-09, T-10, T-11, T-PARITY |

Phase gates registered:
- PG-01 closes Phase 1: IB-zero ordering verified + CMD completeness + scaffold declaration.
- PG-02 closes Phase 2: pre-trace table population.
- PG-03 closes Phase 3: stage trace completeness + triple-count checkpoint verification.
- PG-04 closes Phase 4: post-trace resolution + T-PARITY arithmetic.

IB-NN Coverage column: present in every PG-NN gate block. At each phase gate, the
IB-NN Coverage cell names which IB-NN step identifiers have been automated through
and including the stages closed by that gate. The list must grow monotonically:
IB-NN Coverage at PG-k >= IB-NN Coverage at PG-(k-1).

Stage assignment: single-role design -- C-25 satisfied by default. Continuity contract
columns in T-04 apply at boundaries where a role transition is declared.

---

### CMD: Structural Compliance Register

Produce this table immediately after the scaffold. Every subsequent structural
shortfall is citable by CMD ID.

ACCUMULATION PROTOCOL -- four tiers, all required:
- Tier 1 (per-stage): CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total,
  IB-NN steps covered: [IB-NN identifier list].
  [M] = sum of all [N] values through and including this stage.
  IB-NN list at stage k = IB-NN list at stage k-1 union new IB steps automated at stage k.
  A list that does not grow monotonically across stages is a contradiction -- flag it.
- Tier 2 (per-phase): every PG-NN gate block carries "T-07 Running Total" AND "IB-NN
  Coverage" as named columns, showing cumulative append-log count and IB displacement
  progress at that phase boundary.
- Tier 3 (post-trace): T-PARITY enumerates all per-stage N values, shows arithmetic,
  asserts GO or FLAG.
- Tier 4 (IB anchor): T-05 was produced before scaffold (STEP 0a). Every T-10 row
  cites a specific IB-NN step. Every checkpoint triple-count lists IB-NN identifiers
  resolvable against T-05.

| CMD ID | Positive Imperative | DO NOT Prohibition |
|--------|--------------------|--------------------|
| CMD-01 | Pre-declare every phase gate as PG-NN in the scaffold before Phase 1 gate runs | DO NOT produce a gate block with no corresponding PG-NN scaffold entry |
| CMD-02 | Label the scaffold's column contract field exactly as "Mandatory Columns (exact names)" | DO NOT use "Key Columns," "Required Fields," or any descriptive variant |
| CMD-03 | Produce T-02 FM-NN Prediction Register before Stage 1; resolve in T-09 only | DO NOT write CONFIRMED / EXONERATED / NEW status inline during stage traces |
| CMD-04 | Append T-07 rows as table rows during each stage trace block; close with triple-count checkpoint | DO NOT embed FM-NN acknowledgments as prose bullets within stage sections |
| CMD-05 | Produce one T-06 typed exit manifest per stage with field_name: TYPE(precision) notation | DO NOT state schema state in prose without typed field assertions |
| CMD-06 | Produce T-PARITY as a standalone named table with per-stage N enumeration and arithmetic | DO NOT substitute a prose sentence or PG-NN column for T-PARITY |
| CMD-07 | List all domain entities in T-01 before Stage 1; all trace references bind to T-01 names | DO NOT introduce an entity during traces that was not declared in T-01 |
| CMD-08 | Enumerate all pipeline stages in T-03 before Stage 1 trace | DO NOT reference a stage in trace content that has no T-03 entry |
| CMD-09 | Label every inter-stage boundary B[N]->[N+1] in T-04 | DO NOT reference a boundary without the B[N]->[N+1] format |
| CMD-10 | Decompose boundary latency into Transport (ms) and Processing (ms) as separate columns | DO NOT use a single aggregate "Boundary Latency" column; "Negligible" is not a valid value |
| CMD-11 | Use entity.field_name format in T-04 from T-06 manifests; resolve stubs after T-06 is complete | DO NOT use "data," "records," or "payload" as entity-at-risk identifiers |
| CMD-12 | Produce T-08 SLA Domination Point as a standalone table separate from T-04 | DO NOT embed domination point as a prose note appended to T-04 |
| CMD-13 | Cite a specific IB-NN Step ID in every T-10 row; T-05 was produced before scaffold | DO NOT write recovery framing without citing a specific IB-NN step from T-05 |
| CMD-14 | Cite a specific IB-NN Step ID in every T-10 row -- identifier from T-05 only | DO NOT name the process category only -- "IB-03" not "AP reconciliation process" |
| CMD-15 | Produce T-11 Closure Gate with one row per NH-NN and LP-NN identifier | DO NOT substitute an aggregate count for per-row CLOSED / OPEN status |
| CMD-16 | Close each phase with a named PG-NN gate block listing all expected artifacts | DO NOT advance to the next phase until all PG-NN gate rows show GO |
| CMD-17 | Close every stage trace block with a triple-count checkpoint naming stage ID, N, M, and IB-NN list | DO NOT write a checkpoint with [N] only or [N]+[M] only; the IB-NN coverage list is required |
| CMD-18 | Declare CMD register as the first row of the scaffold, before T-01 | DO NOT list CMD after any T-NN artifact in the scaffold -- positional primacy required |
| CMD-19 | Carry T-07 Running Total column in every PG-NN gate block as a named column in Mandatory Columns | DO NOT produce a gate block without a T-07 Running Total column showing cumulative count |
| CMD-20 | Verify at every PG-NN gate that T-07 Running Total equals sum of all prior stage [N] values | DO NOT advance past a gate whose T-07 Running Total does not match checkpoint arithmetic |
| CMD-21 | Carry IB-NN Coverage column in every PG-NN gate block, pre-declared in scaffold Mandatory Columns | DO NOT produce a gate block with Running Total (CMD-19) but no IB-NN Coverage column |
| CMD-22 | Produce T-05 (IB table) as STEP 0a before writing the scaffold in STEP 0b | DO NOT declare T-05 as a future artifact in the scaffold when it already exists above |
| CMD-23 | Write every checkpoint as: CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total, IB-NN steps covered: [list] | DO NOT write a checkpoint with only [N]+[M]; the IB-NN identifier list is a required third element |
| CMD-24 | Include Responsible Role as the sixth column in every T-10 row, drawn from T-01/T-05 vocabulary | DO NOT use "team," "owner," "system," or any generic label in the Responsible Role column |
| CMD-25 | At every role-transition boundary in T-04, populate Sending Role Delivery Guarantee and Receiving Role Acceptance Requirement columns | DO NOT leave a role-transition boundary annotated with entity-at-risk only; the bilateral contract is required |

---

### PG-01: Phase 1 Gate

| Required Artifact | Declaration Status | CMD Binding Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|------------------|--------------------|--------------------|-------------------|---------------|---------|
| T-05 IB table produced as STEP 0a before scaffold | | CMD-22 | n/a (pre-trace) | T-05 entries confirmed | |
| CMD register (CMD-01 through CMD-25) as first scaffold row | | CMD-18 | n/a | n/a | |
| CMD-21 entry present (IB-NN Coverage column in PG-NN gates) | | CMD-21 | n/a | n/a | |
| T-01 through T-11 in scaffold with Mandatory Columns (exact names) | | CMD-02 | n/a | n/a | |
| T-04 scaffold entry includes Sending Role Delivery Guarantee + Receiving Role Acceptance Requirement in Mandatory Columns | | CMD-25 | n/a | n/a | |
| T-10 scaffold entry includes Responsible Role in Mandatory Columns | | CMD-24 | n/a | n/a | |
| Every PG-NN scaffold entry declares T-07 Running Total AND IB-NN Coverage in Mandatory Columns | | CMD-19, CMD-21 | n/a | n/a | |
| Every T-NN, PG-NN, T-PARITY scaffold row carries CMD Binding column | | CMD-18 | n/a | n/a | |

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
Resolution in T-09 only.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

### T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

### T-04: Boundary Inventory

Rules:
- "Negligible" is not a valid latency value -- numeric ms required (CMD-10).
- Transport (ms) and Processing (ms) are independent sub-components; sum = Total (ms).
- entity.field stubs: write "-> back-fill from T-06.[Stage ID]" until manifest exists.
- Boundary labels: B[N]->[N+1] format (CMD-09).
- SLA%: compute against stated total pipeline SLA budget.
- Continuity contract columns: at every boundary where the sending role differs from
  the receiving role, populate Sending Role Delivery Guarantee (specific artifact or
  field set from T-06 or scaffold) and Receiving Role Acceptance Requirement (named
  precondition). Use domain role vocabulary from T-05. Generic labels do not qualify.
  Same-role boundaries: write "Same role -- contract exempt" in both columns (CMD-25).

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% | Sending Role Delivery Guarantee | Receiving Role Acceptance Requirement |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|--------------------------------|--------------------------------------|

---

### T-05 (already produced in STEP 0a -- reference by IB-NN identifiers)

T-05 was produced before this scaffold. All citations use IB-NN identifiers from that
table. Do not re-produce T-05 here.

---

### T-08: SLA Domination Point (standalone -- CMD-12)

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

One row. B[N]->[N+1] label from T-04. The boundary where cumulative SLA% first exceeds
50% of the SLA budget. One-sentence justification naming the specific domain operation.

---

### PG-02: Phase 2 Gate

| Required Table | Population Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|---------------|-------------------|--------------------|---------------|---------|
| T-01 Entity Inventory | | 0 | n/a (pre-Stage-1) | |
| T-02 FM-NN Prediction Register | | 0 | n/a | |
| T-03 Stage Enumeration | | 0 | n/a | |
| T-04 Boundary Inventory | | 0 | n/a | |
| T-05 IB Table (STEP 0a) | Already produced | 0 | [all IB-NN entries] | |
| T-08 SLA Domination Point | | 0 | n/a | |

Phase 3 may not begin if any row shows NO-GO.

---

## PHASE 3: STAGE TRACES

For each stage in T-03:

1. Describe the processing step using T-01 entity names and domain terms.
2. Identify at least one concrete named data loss point (LP-NN) or no-handling annotation
   (NH-NN) -- generic "errors may occur" fails.
3. Annotate error handling at the stage's exit boundary from T-04 (B[N]->[N+1]).
4. Produce the T-06 typed exit manifest: one row per output field, format field_name:
   TYPE(precision). After T-06 is complete, back-fill any T-04 stub rows referencing
   this stage.
5. Append T-07 rows for any FM-NN entries whose failure modes intersect this stage.
   Each row: FM-NN identifier, Stage ID, specific boundary or condition touched,
   deferral statement citing T-09 by name.
6. Close with the triple-count checkpoint (CMD-23):
   CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total, IB-NN steps covered: [list]
   The IB-NN list names every incumbent baseline step automated through and including
   this stage. It must equal the list from the prior stage's checkpoint union any new
   IB steps automated at this stage. A shrinking list is a contradiction -- flag it.

---

### PG-03: Phase 3 Gate

| Required Artifact | Completion Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|------------------|-------------------|--------------------|---------------|---------|
| T-06 exit manifest for every stage in T-03 | | [running total] | [IB-NN list through final stage] | |
| T-04 entity.field stubs all back-filled | | | | |
| T-07 append-log has rows | | | | |
| Triple-count checkpoint closed every stage | | | | |

Phase 4 may not begin if any row shows NO-GO.

---

## PHASE 4: POST-TRACE RESOLUTION

### T-09: FM-NN Resolution Audit

Resolve every T-02 entry. Status: CONFIRMED (cites NH-NN or LP-NN produced) |
EXONERATED (states specific reason absent) | NEW (assigns formal identifier retroactively).

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

---

### T-10: Recovery Audit Table

One row per NH-NN and LP-NN identifier. IB-NN Step Cited must be a specific identifier
from T-05 -- "IB-03" not "AP reconciliation process" (CMD-14). Responsible Role must be
a named domain actor from T-01/T-05 -- "AP Clerk" not "team" (CMD-24).

| NH/LP ID | Triggering Condition | Recovery Mechanism | IB-NN Step Cited | Boundary / Stage | Responsible Role |
|---------|---------------------|-------------------|-----------------|-----------------|--------------------|

---

### T-11: Closure Gate

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|---------|--------|

CLOSED = row present in T-10 with valid IB-NN citation. OPEN = missing row.

---

### T-PARITY: Count Parity Gate

| Stage ID | N Rows This Stage | Running Total | GO / FLAG |
|----------|------------------|--------------|-----------|

Enumerate all per-stage N values. Show arithmetic. Assert GO (sum matches [M] from
final triple-count checkpoint) or FLAG (name the stage whose count diverges).

---

### PG-04: Phase 4 Gate

| Required Table | Population Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|---------------|-------------------|--------------------|---------------|---------|
| T-09 FM-NN Resolution Audit | | [final] | [final IB-NN list] | |
| T-10 Recovery Audit Table | | | | |
| T-11 Closure Gate | | | | |
| T-PARITY Count Parity Gate | | | | |

---

## PHASE 5: SYNTHESIS

Identify the dominant failure pattern across all LP-NN and NH-NN entries. Name one
alternative pipeline pattern with at least two trade-off dimensions, at least one
quantified or qualified in domain terms. Comment on the stale data window under
normal operation and under failure-mode conditions separately.
```

---

## V-02 -- Output Format: Scaffold Column Explosion with IB-Col? and HO-Col? Flags

**Axis**: Output format -- the scaffold carries two additional flag columns: IB-Col?
(YES/NO -- does this artifact require an IB-NN Coverage column in its output) and
HO-Col? (YES/NO -- does this artifact require handoff contract columns at role-transition
boundaries). Every PG-NN row has IB-Col? = YES; T-04 has HO-Col? = YES.
**Hypothesis**: flag columns on scaffold rows create visible gaps -- a scaffold row with
IB-Col? = YES and no IB-NN Coverage in Mandatory Columns is structurally self-contradicting;
HO-Col? = YES with no handoff contract columns in T-04 is similarly self-contradicting.

---

```
You are a Finance / Operations / Commerce data domain expert. Produce a complete data
flow trace for the following pipeline:

{topic}

---

STRUCTURAL RULE: Your response is organized as five phases with phase gates. The CMD-NN
Structural Compliance Register is the first scaffold row and the first table in the
response body. No T-NN, PG-NN, or T-PARITY row appears before CMD in the scaffold.

IB ORDERING RULE: Produce the Incumbent Baseline table (T-05) as STEP 0a before the
scaffold. The scaffold's T-05 entry carries IB-Col? = NO (the IB table has no IB-NN
Coverage column requirement; it IS the IB reference) and Declaration Status = "Artifact
zero -- produced above scaffold."

---

## PHASE 1: COMPLIANCE PROTOCOL DECLARATION

### STEP 0a: Incumbent Baseline (ARTIFACT ZERO)

Produce before the scaffold. Use IB-NN step identifiers (IB-01, IB-02, ...) throughout.

| IB-NN | Step Name | Responsible Role | Elapsed Time / Frequency |
|-------|-----------|-----------------|--------------------------|

---

### STEP 0b: Output Scaffold

The scaffold carries six columns: T#, Table Name, Purpose, Mandatory Columns (exact
names), CMD Binding, IB-Col?, HO-Col?.

- IB-Col? = YES means this artifact must include an IB-NN Coverage column. A scaffold
  row with IB-Col? = YES and no "IB-NN Coverage" in Mandatory Columns is a self-contradiction.
- HO-Col? = YES means this artifact must include handoff contract columns (Sending Role
  Delivery Guarantee + Receiving Role Acceptance Requirement). A scaffold row with
  HO-Col? = YES and no handoff contract columns in Mandatory Columns is a self-contradiction.

| T#       | Table Name                      | Purpose                                                              | Mandatory Columns (exact names)                                                                                                                   | CMD Binding                    | IB-Col? | HO-Col? |
|----------|---------------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|---------|---------|
| CMD      | Structural Compliance Register  | Meta-contract; first scaffold row                                    | CMD ID, Positive Imperative, DO NOT Prohibition                                                                                                   | --                             | NO      | NO      |
| T-01     | Entity Inventory                | Domain entities; all trace references bind to T-01 names            | Entity, Description, Key Fields                                                                                                                   | CMD-07                         | NO      | NO      |
| T-02     | FM-NN Prediction Register       | Pre-trace failure hypotheses                                        | FM-NN, Anticipated Event, Domain Consequence, Expected Designation                                                                                | CMD-03                         | NO      | NO      |
| T-03     | Stage Enumeration               | Named and sequenced pipeline stages                                 | Stage ID, Stage Name, Description                                                                                                                 | CMD-08                         | NO      | NO      |
| T-04     | Boundary Inventory              | Boundaries with latency, entity-at-risk, SLA%, handoff contracts    | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA%, Sending Role Delivery Guarantee, Receiving Role Acceptance Requirement | CMD-09, CMD-10, CMD-11, CMD-25 | NO      | YES     |
| T-05     | Incumbent Baseline              | Artifact zero -- produced above scaffold                            | IB-NN, Step Name, Responsible Role, Elapsed Time / Frequency                                                                                     | CMD-13, CMD-22                 | NO      | NO      |
| T-06     | Stage Exit Manifests            | One typed manifest per stage                                        | field_name, TYPE(precision), Notes                                                                                                                | CMD-05                         | NO      | NO      |
| T-07     | FM-NN Append-Log                | Accumulating per-stage rows; triple-count checkpoint at each stage  | FM-NN, Stage ID, Boundary / Condition, Deferral Statement                                                                                        | CMD-04, CMD-17, CMD-23         | NO      | NO      |
| T-08     | SLA Domination Point            | Standalone domination boundary                                      | Domination Boundary, Exact Cumulative SLA%, Justification                                                                                         | CMD-12                         | NO      | NO      |
| T-09     | FM-NN Resolution Audit          | Post-trace FM-NN lifecycle resolution                               | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason                                                                                            | CMD-03                         | NO      | NO      |
| T-10     | Recovery Audit Table            | NH-NN/LP-NN recovery with IB-NN citations and role attribution      | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage, Responsible Role                                         | CMD-13, CMD-14, CMD-24         | NO      | NO      |
| T-11     | Closure Gate                    | Per-identifier CLOSED / OPEN status                                | Identifier, Source (Stage / Boundary), T-10 Row, Status                                                                                           | CMD-15                         | NO      | NO      |
| T-PARITY | Count Parity Gate               | Cross-stage arithmetic parity                                       | Stage ID, N Rows This Stage, Running Total, GO / FLAG                                                                                             | CMD-06, CMD-18                 | NO      | NO      |
| PG-01    | Phase 1 Gate                    | IB ordering + CMD completeness + scaffold flag audit                | Required Artifact, Declaration Status, CMD Binding Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                          | CMD-01, CMD-16, CMD-19, CMD-21 | YES     | NO      |
| PG-02    | Phase 2 Gate                    | Pre-trace table population                                          | Required Table, Population Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                                  | CMD-01, CMD-16, CMD-19, CMD-21 | YES     | NO      |
| PG-03    | Phase 3 Gate                    | Stage trace completeness                                            | Required Artifact, Completion Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                               | CMD-01, CMD-04, CMD-16, CMD-19, CMD-21 | YES | NO   |
| PG-04    | Phase 4 Gate                    | Post-trace resolution completeness                                  | Required Table, Population Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                                  | CMD-01, CMD-06, CMD-16, CMD-19, CMD-21 | YES | NO   |

SCAFFOLD AUDIT: Before proceeding to CMD, verify every PG-NN row has IB-Col? = YES and
"IB-NN Coverage" in Mandatory Columns. Verify every row with HO-Col? = YES has both
handoff contract columns in Mandatory Columns. A scaffold row that contradicts its own
flag value is a CMD-02 breach.

---

### CMD: Structural Compliance Register

| CMD ID | Positive Imperative | DO NOT Prohibition |
|--------|--------------------|--------------------|
| CMD-01 | Pre-declare every phase gate as PG-NN in the scaffold before Phase 1 gate runs | DO NOT produce a gate block with no corresponding PG-NN scaffold entry |
| CMD-02 | Label the scaffold's column contract field exactly as "Mandatory Columns (exact names)" | DO NOT use "Key Columns," "Required Fields," or any descriptive variant |
| CMD-03 | Produce T-02 FM-NN Prediction Register before Stage 1; resolve in T-09 only | DO NOT write CONFIRMED / EXONERATED / NEW status inline during stage traces |
| CMD-04 | Append T-07 rows as table rows during each stage trace; close with triple-count checkpoint | DO NOT embed FM-NN acknowledgments as prose bullets |
| CMD-05 | Produce one T-06 typed exit manifest per stage with field_name: TYPE(precision) notation | DO NOT state schema state in prose without typed field assertions |
| CMD-06 | Produce T-PARITY as a standalone named table with per-stage N enumeration and arithmetic | DO NOT substitute a prose sentence for T-PARITY |
| CMD-07 | List all domain entities in T-01 before Stage 1 | DO NOT introduce an entity during traces that was not declared in T-01 |
| CMD-08 | Enumerate all pipeline stages in T-03 before Stage 1 trace | DO NOT reference a stage not in T-03 |
| CMD-09 | Label every inter-stage boundary B[N]->[N+1] in T-04 | DO NOT reference a boundary without the B[N]->[N+1] format |
| CMD-10 | Decompose boundary latency into Transport (ms) and Processing (ms) as separate columns | DO NOT use a single "Boundary Latency" column; "Negligible" is invalid |
| CMD-11 | Use entity.field_name format in T-04; resolve stubs after T-06 is complete | DO NOT use "data," "records," or "payload" as entity-at-risk identifiers |
| CMD-12 | Produce T-08 SLA Domination Point as a standalone table separate from T-04 | DO NOT embed domination point as a prose note in T-04 |
| CMD-13 | Cite a specific IB-NN Step ID in every T-10 row | DO NOT write recovery framing without a specific IB-NN citation from T-05 |
| CMD-14 | Use IB-NN identifier format (IB-03) not process category name | DO NOT write "AP reconciliation process" when "IB-03" is required |
| CMD-15 | Produce T-11 Closure Gate with one row per NH-NN and LP-NN identifier | DO NOT substitute an aggregate count for per-row CLOSED / OPEN status |
| CMD-16 | Close each phase with a named PG-NN gate block | DO NOT advance to next phase until all gate rows show GO |
| CMD-17 | Close every stage trace block with: CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total, IB-NN steps covered: [list] | DO NOT write a checkpoint with only [N] or only [N]+[M]; IB-NN list is required |
| CMD-18 | Declare CMD register as the first row of the scaffold, before T-01 | DO NOT list CMD after any T-NN artifact |
| CMD-19 | Carry T-07 Running Total column in every PG-NN gate block; declare it in Mandatory Columns | DO NOT produce a gate block without T-07 Running Total column |
| CMD-20 | Verify at every PG-NN gate that T-07 Running Total equals sum of all prior stage [N] | DO NOT advance past a gate with arithmetic mismatch |
| CMD-21 | Carry IB-NN Coverage column in every PG-NN gate block; declare it in Mandatory Columns | DO NOT produce a gate block with Running Total but no IB-NN Coverage column |
| CMD-22 | Produce T-05 as STEP 0a before the scaffold; scaffold T-05 entry reads "Artifact zero -- produced above scaffold" | DO NOT declare T-05 as a future artifact when it already exists above the scaffold |
| CMD-23 | Write every checkpoint as triple-count: [N] rows appended, [M] total, IB-NN steps covered: [list] | DO NOT write [N]+[M] only; the IB-NN identifier list is a required third element |
| CMD-24 | Include Responsible Role as sixth column in every T-10 row, drawn from T-01/T-05 vocabulary | DO NOT use "team," "owner," "system," or generic labels in Responsible Role column |
| CMD-25 | At every role-transition boundary in T-04, populate both handoff contract columns using domain role vocabulary | DO NOT leave a role-transition boundary with entity-at-risk annotation but no bilateral contract |

SCAFFOLD FLAG AUDIT (CMD-02 extension):
- Every PG-NN row in scaffold has IB-Col? = YES: [verify]
- Every IB-Col? = YES row declares "IB-NN Coverage" in Mandatory Columns: [verify]
- Every HO-Col? = YES row (T-04) declares both handoff contract columns in Mandatory Columns: [verify]

---

### PG-01: Phase 1 Gate

| Required Artifact | Declaration Status | CMD Binding Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|------------------|--------------------|--------------------|-------------------|---------------|---------|
| T-05 produced as STEP 0a before scaffold | Artifact zero above | CMD-22 | 0 (pre-trace) | [IB-NN entries from T-05] | |
| Scaffold IB-Col? = YES on all PG-NN rows | | CMD-21 | n/a | n/a | |
| Scaffold IB-NN Coverage in Mandatory Columns on all PG-NN rows | | CMD-21 | n/a | n/a | |
| Scaffold HO-Col? = YES on T-04 row | | CMD-25 | n/a | n/a | |
| T-04 Mandatory Columns includes both handoff contract columns | | CMD-25 | n/a | n/a | |
| T-10 Mandatory Columns includes Responsible Role | | CMD-24 | n/a | n/a | |
| CMD register is first scaffold row | | CMD-18 | n/a | n/a | |
| CMD Binding column on every T-NN, PG-NN, T-PARITY scaffold row | | CMD-18 | n/a | n/a | |

Phase 2 may not begin if any row shows NO-GO.

---

## PHASE 2: PRE-TRACE DECLARATIONS

Produce T-01, T-02, T-03, T-04, T-08 in sequence.

After T-04: verify every role-transition boundary row has both handoff contract columns
populated (CMD-25). If no role transitions exist, annotate boundary rows explicitly:
"Same role -- continuity contract exempt."

### PG-02: Phase 2 Gate

| Required Table | Population Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|---------------|-------------------|--------------------|---------------|---------|
| T-01 Entity Inventory | | 0 | n/a | |
| T-02 FM-NN Prediction Register | | 0 | n/a | |
| T-03 Stage Enumeration | | 0 | n/a | |
| T-04 Boundary Inventory with handoff contract columns | | 0 | n/a | |
| T-05 (artifact zero above scaffold) | Already produced | 0 | [all IB-NN entries] | |
| T-08 SLA Domination Point | | 0 | n/a | |

---

## PHASE 3: STAGE TRACES

For each stage: process description, LP-NN/NH-NN, boundary annotation, T-06 typed
manifest, T-07 append-log rows, triple-count checkpoint.

Triple-count form (CMD-23):
CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total, IB-NN steps covered: [list]

The IB-NN list grows monotonically across stages. A list that does not grow, or that
cites an IB-NN not present in T-05, is a contradiction -- flag it.

### PG-03: Phase 3 Gate

| Required Artifact | Completion Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|------------------|-------------------|--------------------|---------------|---------|
| T-06 exit manifest for every stage | | [final N sum] | [IB-NN list from final checkpoint] | |
| T-04 stubs all back-filled | | | | |
| Triple-count checkpoint closed every stage | | | | |
| IB-NN list grew monotonically across stages | | | | |

---

## PHASE 4: POST-TRACE RESOLUTION

Produce T-09, T-10, T-11, T-PARITY.

T-10 reminder: Responsible Role column (CMD-24) must use named domain actors from
T-01/T-05 vocabulary. If a row's Responsible Role would be "team" or "system," identify
which specific named role in T-05 is accountable and use that name.

### PG-04: Phase 4 Gate

| Required Table | Population Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|---------------|-------------------|--------------------|---------------|---------|
| T-09 FM-NN Resolution Audit | | [final] | [final IB-NN list] | |
| T-10 Recovery Audit Table with Responsible Role column | | | | |
| T-11 Closure Gate | | | | |
| T-PARITY Count Parity Gate | | | | |

---

## PHASE 5: SYNTHESIS

Pattern trade-off, stale data window analysis, dominant failure mode summary.
```

---

## V-03 -- Role Sequence: Finance/Operations Split with Role-Owned Handoff Contracts

**Axis**: Role sequence -- Finance Controller owns Stages 1-3 and PG-01/PG-02; Operations
Analyst owns Stages 4-6 and PG-03/PG-04. At B3->4 (the role-transition boundary), a
dedicated T-12 Handoff Continuity Contract table captures Finance's delivery guarantee
and Operations' acceptance requirement. CMD register has a "Role Owner" column.
**Hypothesis**: role ownership of CMD slices + role ownership of PG-NN gates creates two
independent enforcement surfaces for C-42 -- a handoff contract at B3->4 is a scorable
gap attributable to Finance (sending) and Operations (receiving) by name.

---

```
You are a Finance / Operations / Commerce data domain expert operating in a two-role
pipeline trace. Finance Controller owns the extraction and transformation stages.
Operations Analyst owns the load and distribution stages. Produce a complete data
flow trace for the following pipeline:

{topic}

---

STRUCTURAL RULE: Your response is organized as five phases. PG-NN gates enforce phase
transitions. The CMD-NN Structural Compliance Register is the first scaffold row and
first response table. The CMD register carries a Role Owner column identifying which
role is responsible for each CMD entry's compliance.

IB ORDERING RULE: Produce T-05 (Incumbent Baseline) as STEP 0a before the scaffold.
This establishes the manual process reference from which both Finance's stages and
Operations' stages depart. Responsible Role names in T-05 must distinguish Finance
roles (AP Clerk, Finance Analyst, Finance Controller) from Operations roles (Inventory
Coordinator, Operations Manager, Operations Analyst). This role vocabulary governs
T-10 Responsible Role column (CMD-24) and T-12 handoff contract role names (CMD-25).

ROLE ASSIGNMENT: Declare stage-to-role assignments in T-25. At every boundary where
Finance Controller hands off to Operations Analyst, T-04 must carry a Sending Role
Delivery Guarantee and Receiving Role Acceptance Requirement. T-12 provides the
bilateral contract for the primary role-transition boundary.

---

## PHASE 1: COMPLIANCE PROTOCOL DECLARATION

### STEP 0a: Incumbent Baseline (ARTIFACT ZERO)

| IB-NN | Step Name | Responsible Role | Elapsed Time / Frequency |
|-------|-----------|-----------------|--------------------------|

---

### STEP 0b: Output Scaffold

| T#       | Table Name                      | Purpose                                                              | Mandatory Columns (exact names)                                                                                                                   | CMD Binding                    | Depends On          |
|----------|---------------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|---------------------|
| CMD      | Structural Compliance Register  | Meta-contract with Role Owner column; first scaffold row            | CMD ID, Positive Imperative, DO NOT Prohibition, Role Owner                                                                                       | --                             | --                  |
| T-01     | Entity Inventory                | Domain entities                                                     | Entity, Description, Key Fields                                                                                                                   | CMD-07                         | --                  |
| T-02     | FM-NN Prediction Register       | Pre-trace failure hypotheses                                        | FM-NN, Anticipated Event, Domain Consequence, Expected Designation                                                                                | CMD-03                         | --                  |
| T-03     | Stage Enumeration               | Named and sequenced pipeline stages                                 | Stage ID, Stage Name, Description                                                                                                                 | CMD-08                         | --                  |
| T-04     | Boundary Inventory              | Boundaries with latency, entity-at-risk, SLA%, handoff contracts    | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA%, Sending Role Delivery Guarantee, Receiving Role Acceptance Requirement | CMD-09, CMD-10, CMD-11, CMD-25 | T-03 |
| T-05     | Incumbent Baseline              | Artifact zero -- produced above scaffold                            | IB-NN, Step Name, Responsible Role, Elapsed Time / Frequency                                                                                     | CMD-13, CMD-22                 | -- (STEP 0a)        |
| T-06     | Stage Exit Manifests            | One typed manifest per stage                                        | field_name, TYPE(precision), Notes                                                                                                                | CMD-05                         | T-03                |
| T-07     | FM-NN Append-Log                | Per-stage rows; triple-count checkpoint at each stage               | FM-NN, Stage ID, Boundary / Condition, Deferral Statement                                                                                        | CMD-04, CMD-17, CMD-23         | T-02, T-03          |
| T-08     | SLA Domination Point            | Standalone domination boundary                                      | Domination Boundary, Exact Cumulative SLA%, Justification                                                                                         | CMD-12                         | T-04                |
| T-09     | FM-NN Resolution Audit          | Post-trace lifecycle resolution                                     | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason                                                                                            | CMD-03                         | T-02, T-07          |
| T-10     | Recovery Audit Table            | NH-NN/LP-NN recovery with IB-NN citations and role attribution      | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage, Responsible Role                                         | CMD-13, CMD-14, CMD-24         | T-04, T-05, T-06    |
| T-11     | Closure Gate                    | Per-identifier CLOSED / OPEN status                                | Identifier, Source (Stage / Boundary), T-10 Row, Status                                                                                           | CMD-15                         | T-10                |
| T-12     | Handoff Continuity Contract     | Bilateral contract at Finance-to-Operations boundary               | Boundary, Sending Role, Delivery Guarantee (named artifact), Receiving Role, Acceptance Requirement (named precondition)                          | CMD-25                         | T-04, T-06          |
| T-25     | Stage Assignment Map            | Stage-to-role assignment for all pipeline stages                    | Stage ID, Stage Name, Assigned Role                                                                                                              | CMD-25                         | T-03                |
| T-PARITY | Count Parity Gate               | Cross-stage arithmetic parity                                       | Stage ID, N Rows This Stage, Running Total, GO / FLAG                                                                                             | CMD-06, CMD-18                 | T-07                |
| PG-01    | Phase 1 Gate (Finance)          | IB ordering + CMD completeness; Finance-role owned                 | Required Artifact, Declaration Status, CMD Binding Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                          | CMD-01, CMD-16, CMD-19, CMD-21 | CMD, T-01--T-12, T-25 |
| PG-02    | Phase 2 Gate (Finance)          | Pre-trace population; Finance-role owned                           | Required Table, Population Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                                  | CMD-01, CMD-16, CMD-19, CMD-21 | T-01--T-05, T-08    |
| PG-03    | Phase 3 Gate (Operations)       | Stage trace completeness; Operations-role owned                    | Required Artifact, Completion Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                               | CMD-01, CMD-04, CMD-16, CMD-19, CMD-21 | T-06, T-07   |
| PG-04    | Phase 4 Gate (Operations)       | Post-trace resolution; Operations-role owned                       | Required Table, Population Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                                  | CMD-01, CMD-06, CMD-16, CMD-19, CMD-21 | T-09--T-11, T-PARITY |

---

### CMD: Structural Compliance Register (with Role Owner column)

Finance CMD slice: CMD-07, CMD-08, CMD-09, CMD-10, CMD-11, CMD-12, CMD-13, CMD-14,
CMD-19, CMD-20, CMD-21, CMD-22.
Operations CMD slice: CMD-03, CMD-04, CMD-05, CMD-06, CMD-15, CMD-17, CMD-23, CMD-24.
Shared: CMD-01, CMD-02, CMD-16, CMD-18, CMD-25.

| CMD ID | Positive Imperative | DO NOT Prohibition | Role Owner |
|--------|--------------------|--------------------|------------|
| CMD-01 | Pre-declare every phase gate as PG-NN in scaffold | DO NOT produce a gate block without PG-NN scaffold entry | Shared |
| CMD-02 | Label scaffold column contract "Mandatory Columns (exact names)" | DO NOT use any descriptive variant | Shared |
| CMD-03 | Produce T-02 before Stage 1; resolve FM-NN in T-09 only | DO NOT write resolution status inline | Operations |
| CMD-04 | Append T-07 rows as table rows; close with triple-count checkpoint | DO NOT embed FM-NN acknowledgments as prose | Operations |
| CMD-05 | Produce one T-06 typed exit manifest per stage | DO NOT state schema in prose without typed fields | Operations |
| CMD-06 | Produce T-PARITY as standalone table with per-stage N and arithmetic | DO NOT substitute prose or PG-NN column for T-PARITY | Operations |
| CMD-07 | List all domain entities in T-01 before Stage 1 | DO NOT introduce undeclared entities in traces | Finance |
| CMD-08 | Enumerate all stages in T-03 before Stage 1 trace | DO NOT reference stages not in T-03 | Finance |
| CMD-09 | Label every boundary B[N]->[N+1] in T-04 | DO NOT use boundary references without B[N]->[N+1] format | Finance |
| CMD-10 | Decompose boundary latency into Transport (ms) + Processing (ms) | DO NOT use a single aggregate latency column; "Negligible" is invalid | Finance |
| CMD-11 | Use entity.field_name in T-04; resolve stubs after T-06 | DO NOT use "data" or "records" as entity-at-risk identifiers | Finance |
| CMD-12 | Produce T-08 SLA Domination Point as standalone table | DO NOT embed domination point in T-04 | Finance |
| CMD-13 | Cite a specific IB-NN Step ID in every T-10 row | DO NOT write recovery without specific IB-NN citation | Finance |
| CMD-14 | Use IB-NN identifier (IB-03), not process category name | DO NOT substitute process category for IB-NN identifier | Finance |
| CMD-15 | Produce T-11 Closure Gate with one row per NH-NN/LP-NN | DO NOT substitute aggregate count for per-row status | Operations |
| CMD-16 | Close each phase with named PG-NN gate block | DO NOT advance until all gate rows show GO | Shared |
| CMD-17 | Close every stage trace block with triple-count checkpoint | DO NOT omit [M] or IB-NN coverage list from checkpoint | Operations |
| CMD-18 | CMD register is first scaffold row, before T-01 | DO NOT list CMD after any T-NN artifact | Shared |
| CMD-19 | T-07 Running Total column in every PG-NN gate block | DO NOT produce gate block without Running Total column | Finance |
| CMD-20 | PG-NN Running Total must equal sum of all prior stage [N] | DO NOT advance past gate with arithmetic mismatch | Finance |
| CMD-21 | IB-NN Coverage column in every PG-NN gate block, declared in Mandatory Columns | DO NOT produce gate block with Running Total but no IB-NN Coverage column | Finance |
| CMD-22 | Produce T-05 as STEP 0a before scaffold | DO NOT declare T-05 as future artifact when it exists above | Finance |
| CMD-23 | Triple-count: CHECKPOINT [Stage ID] COMPLETE -- [N] appended, [M] total, IB-NN steps covered: [list] | DO NOT write [N]+[M] only; IB-NN list is required third element | Operations |
| CMD-24 | Responsible Role in every T-10 row from T-05 vocabulary | DO NOT use "team," "owner," "system" in Responsible Role | Operations |
| CMD-25 | T-04 role-transition boundaries carry bilateral handoff contract; T-12 provides primary contract | DO NOT annotate role-transition boundary with entity-at-risk only | Shared |

---

### PG-01: Phase 1 Gate (Finance Controller)

| Required Artifact | Declaration Status | CMD Binding Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|------------------|--------------------|--------------------|-------------------|---------------|---------|
| T-05 produced as STEP 0a | Artifact zero | CMD-22 (Finance) | 0 | [T-05 entries] | |
| T-25 Stage Assignment Map declared in scaffold | | CMD-25 | n/a | n/a | |
| T-12 Handoff Continuity Contract declared in scaffold | | CMD-25 | n/a | n/a | |
| CMD Role Owner column present on all CMD entries | | CMD-18 | n/a | n/a | |
| Every PG-NN scaffold entry: T-07 Running Total AND IB-NN Coverage in Mandatory Columns | | CMD-19, CMD-21 | n/a | n/a | |
| T-04 Mandatory Columns includes both handoff contract columns | | CMD-25 | n/a | n/a | |
| T-10 Mandatory Columns includes Responsible Role | | CMD-24 | n/a | n/a | |

---

## PHASE 2: PRE-TRACE DECLARATIONS (Finance Controller)

Produce T-01, T-02, T-25 (Stage Assignment Map), T-03, T-04, T-12, T-08.

### T-25: Stage Assignment Map

| Stage ID | Stage Name | Assigned Role |
|----------|------------|--------------|

Finance Controller: Stages 1-3. Operations Analyst: Stages 4-6 (or per {topic}).
The boundary between the last Finance stage and the first Operations stage is the
primary role-transition boundary requiring T-12.

### T-12: Handoff Continuity Contract

Produce after T-04 is complete.

| Boundary | Sending Role | Delivery Guarantee (named artifact from T-06 or scaffold) | Receiving Role | Acceptance Requirement (named precondition) |
|----------|-------------|----------------------------------------------------------|---------------|---------------------------------------------|

Rules:
- Sending Role and Receiving Role must be named domain actors from T-25/T-05 vocabulary.
  "Finance Controller" and "Operations Analyst" are valid; "upstream stage" is not.
- Delivery Guarantee must name a specific artifact or field set resolvable from T-06
  exit manifests. "Data ready" does not qualify.
- Acceptance Requirement must name the specific precondition. "Receives data" does not qualify.
- Boundaries where Assigned Role is the same (T-25) are exempt from T-12 entries.

### PG-02: Phase 2 Gate (Finance Controller)

| Required Table | Population Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|---------------|-------------------|--------------------|---------------|---------|
| T-01 Entity Inventory | | 0 | n/a | |
| T-02 FM-NN Prediction Register | | 0 | n/a | |
| T-25 Stage Assignment Map | | 0 | n/a | |
| T-03 Stage Enumeration | | 0 | n/a | |
| T-04 Boundary Inventory | | 0 | n/a | |
| T-12 Handoff Continuity Contract | | 0 | [IB-NN steps through Finance stages] | |
| T-05 (artifact zero) | Already produced | 0 | [all IB-NN entries] | |
| T-08 SLA Domination Point | | 0 | n/a | |

---

## PHASE 3: STAGE TRACES (dual-role)

### Finance Controller Stages (Stages 1-3)

Close each stage with triple-count checkpoint (CMD-23):
CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total, IB-NN steps covered: [list]

IB-NN list tracks Finance-owned incumbent steps automated by these stages.

### Role-Transition Boundary Annotation

After Stage 3 trace, add a boundary annotation for the Finance-to-Operations boundary:
"Finance Controller delivers [named artifact per T-12 Delivery Guarantee]. Operations
Analyst accepts when [named precondition per T-12 Acceptance Requirement] is confirmed.
Reference: T-12, CMD-25."

### Operations Analyst Stages (Stages 4-6)

Continue accumulating T-07 rows and triple-count checkpoints. IB-NN list expands to
include Operations-owned incumbent steps automated.

### PG-03: Phase 3 Gate (Operations Analyst)

| Required Artifact | Completion Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|------------------|-------------------|--------------------|---------------|---------|
| T-06 exit manifest for every stage | | [running N sum] | [IB-NN list: Finance + Operations stages] | |
| T-04 stubs back-filled | | | | |
| Triple-count checkpoint closed every stage | | | | |
| IB-NN list grew monotonically across stages | | | | |

---

## PHASE 4: POST-TRACE RESOLUTION (Operations Analyst)

T-10 note: Responsible Role must distinguish Finance roles from Operations roles using
T-25/T-05 vocabulary. Finance Controller recovery rows say "Finance Controller" (or
more specific roles from T-05); Operations Analyst recovery rows say "Operations Analyst."

Produce T-09, T-10, T-11, T-PARITY.

### PG-04: Phase 4 Gate (Operations Analyst)

| Required Table | Population Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|---------------|-------------------|--------------------|---------------|---------|
| T-09 FM-NN Resolution Audit | | [final] | [final IB-NN: all automated steps] | |
| T-10 Recovery with Responsible Role column | | | | |
| T-11 Closure Gate | | | | |
| T-PARITY | | | | |

---

## PHASE 5: SYNTHESIS

Trade-off analysis: this pipeline vs one alternative pattern (event-driven vs batch,
dual-write vs CDC, etc.). At least two trade-off dimensions, one quantified. Stale
data window: normal operation vs failure-mode staleness addressed separately.
```

---

## V-04 -- Phrasing Register: Coaching-Imperative with Explicit Arithmetic

**Axis**: Phrasing register -- instructional/coaching tone with explicit formula
statements for every compound structural requirement. The triple-count arithmetic is
taught as a formula. The IB-NN monotonic list rule is stated as a contradiction test.
The Responsible Role attribution is framed as a diagnostic question. The handoff
contract is framed as a two-question checklist. CMD is still entry zero; all structural
requirements remain; the register is less imperious and more explanatory.
**Hypothesis**: stating compound requirements as taught formulas and diagnostic questions
produces correct content (not just column presence) -- a model that understands why
M_k = M_(k-1) + N_k produces arithmetic-correct [M] values, not just a placeholder.

---

```
You are a Finance / Operations / Commerce data domain expert. Your task is to produce a
complete data flow trace for the following pipeline:

{topic}

---

This prompt uses a phase-gated structure. Think of each phase gate (PG-NN) as a quality
checkpoint: before moving to the next phase, verify that everything declared in the
prior phase is present and correct.

A note on structure before you begin: the Incumbent Baseline table (T-05) appears before
the scaffold. This makes T-05 the reference anchor -- everything the pipeline automates
is departing from T-05. When you later write the scaffold, the T-05 entry reads "Already
produced above." This ordering is what makes every other artifact interpretable as a
replacement for a specific manual step.

---

## PHASE 1: SETTING UP THE COMPLIANCE FRAMEWORK

### STEP 0a: Incumbent Baseline (write this first, before the scaffold)

Start here. Before any scaffold or pipeline trace, write the Incumbent Baseline table
showing the manual process this pipeline replaces.

| IB-NN | Step Name | Responsible Role | Elapsed Time / Frequency |
|-------|-----------|-----------------|--------------------------|

A few things to get right here:
- IB-NN identifiers (IB-01, IB-02, ...) are the citation keys you will use throughout
  the response. When a recovery row in T-10 needs to name a fallback process, it cites
  "IB-03" (for example) -- the table row is the reference, not a prose description.
- Responsible Role here means the actual person role (AP Clerk, Finance Analyst,
  Operations Manager) who performs that step today. This vocabulary becomes the legal
  set of role names for your T-10 Responsible Role column later.
- Elapsed Time should be quantified ("2 hours daily," "weekly on Friday at EOD") so
  it can be compared meaningfully to the pipeline's latency profile.

---

### STEP 0b: Output Scaffold (write after T-05 exists above)

The compliance register (CMD) is always the first row of the scaffold and the first
table in your response body. Think of it as the governing contract: if you later write
a T-07 checkpoint with only [N] and not [M], that is a CMD-17 breach. The CMD register
makes every structural shortfall citable by name rather than requiring the reader to
infer what rule was violated.

| T#       | Table Name                      | Purpose                                                              | Mandatory Columns (exact names)                                                                                                                   | CMD Binding                    | Depends On               |
|----------|---------------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------|
| CMD      | Structural Compliance Register  | Governing contract; declared first                                   | CMD ID, Positive Imperative, DO NOT Prohibition                                                                                                   | --                             | --                       |
| T-01     | Entity Inventory                | Domain entities named before trace begins                           | Entity, Description, Key Fields                                                                                                                   | CMD-07                         | --                       |
| T-02     | FM-NN Prediction Register       | Failure hypotheses before Stage 1                                   | FM-NN, Anticipated Event, Domain Consequence, Expected Designation                                                                                | CMD-03                         | --                       |
| T-03     | Stage Enumeration               | All stages named before any stage trace                             | Stage ID, Stage Name, Description                                                                                                                 | CMD-08                         | --                       |
| T-04     | Boundary Inventory              | Boundaries with latency, risk, SLA%, handoff contracts              | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA%, Sending Role Delivery Guarantee, Receiving Role Acceptance Requirement | CMD-09, CMD-10, CMD-11, CMD-25 | T-03                     |
| T-05     | Incumbent Baseline              | Already produced above as STEP 0a                                   | IB-NN, Step Name, Responsible Role, Elapsed Time / Frequency                                                                                     | CMD-13, CMD-22                 | -- (STEP 0a)             |
| T-06     | Stage Exit Manifests            | Typed field inventory at each stage exit                            | field_name, TYPE(precision), Notes                                                                                                                | CMD-05                         | T-03                     |
| T-07     | FM-NN Append-Log                | Running log of FM-NN intersections; triple-count at each stage      | FM-NN, Stage ID, Boundary / Condition, Deferral Statement                                                                                        | CMD-04, CMD-17, CMD-23         | T-02, T-03               |
| T-08     | SLA Domination Point            | The boundary that consumes >50% of SLA budget                       | Domination Boundary, Exact Cumulative SLA%, Justification                                                                                         | CMD-12                         | T-04                     |
| T-09     | FM-NN Resolution Audit          | Lifecycle close for every FM-NN entry                               | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason                                                                                            | CMD-03                         | T-02, T-07               |
| T-10     | Recovery Audit Table            | One row per NH-NN and LP-NN; IB-NN citation; role attribution       | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage, Responsible Role                                         | CMD-13, CMD-14, CMD-24         | T-04, T-05, T-06         |
| T-11     | Closure Gate                    | CLOSED / OPEN status for every NH-NN and LP-NN                     | Identifier, Source (Stage / Boundary), T-10 Row, Status                                                                                           | CMD-15                         | T-10                     |
| T-PARITY | Count Parity Gate               | Arithmetic check: do all the per-stage N counts sum to final M?     | Stage ID, N Rows This Stage, Running Total, GO / FLAG                                                                                             | CMD-06, CMD-18                 | T-07                     |
| PG-01    | Phase 1 Gate                    | Check: is the framework set up correctly?                           | Required Artifact, Declaration Status, CMD Binding Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                          | CMD-01, CMD-16, CMD-19, CMD-21 | CMD, T-01--T-11, T-PARITY |
| PG-02    | Phase 2 Gate                    | Check: are pre-trace tables populated?                              | Required Table, Population Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                                  | CMD-01, CMD-16, CMD-19, CMD-21 | T-01--T-05, T-08         |
| PG-03    | Phase 3 Gate                    | Check: did every stage trace close with a triple-count checkpoint?  | Required Artifact, Completion Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                               | CMD-01, CMD-04, CMD-16, CMD-19, CMD-21 | T-03, T-06, T-07  |
| PG-04    | Phase 4 Gate                    | Check: is T-PARITY arithmetic consistent with per-stage checkpoints? | Required Table, Population Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                                 | CMD-01, CMD-06, CMD-16, CMD-19, CMD-21 | T-09, T-10, T-11, T-PARITY |

A note on the IB-NN Coverage column in every PG-NN gate: this column lists which
incumbent baseline steps (IB-NN identifiers from T-05) have been automated through
and including the stages closed by this gate. Think of it as a displacement audit: at
each phase boundary you can read both how many FM-NN entries have been logged AND
which manual steps the automation has replaced. If the list at PG-03 includes IB-01
and IB-02 but not IB-03, that means IB-03 has not yet been automated through the
traced stages -- which may be expected or may be a coverage gap worth noting.

---

### CMD: Structural Compliance Register

Read through this before starting the traces. The goal is not just column presence but
correct content -- especially for the accumulation protocol.

TRIPLE-COUNT CHECKPOINT ARITHMETIC:
When you close each stage, write:
CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total, IB-NN steps covered: [list]

The arithmetic for M is: M_k = M_(k-1) + N_k
That is: the cumulative total through stage k equals the cumulative total through stage k-1
plus however many T-07 rows you appended at stage k.

The arithmetic for the IB-NN list is: IB_list_k = IB_list_(k-1) union {new IB steps automated at stage k}
A list at stage k that is shorter than the list at stage k-1 is a contradiction. If you
catch this, flag it explicitly rather than silently correcting it.

After the final stage, T-PARITY cross-checks the arithmetic: sum all [N] values
and confirm the total equals [M] from the final checkpoint.

The IB-NN Coverage column in each PG-NN gate is the phase-boundary version of the same
check: list which IB-NN steps have been automated through the stages closed by this gate.

| CMD ID | Positive Imperative | DO NOT Prohibition |
|--------|--------------------|--------------------|
| CMD-01 | Pre-declare every phase gate as PG-NN in the scaffold | DO NOT produce a gate block without a PG-NN scaffold entry |
| CMD-02 | Label scaffold column contract "Mandatory Columns (exact names)" | DO NOT use any label variant |
| CMD-03 | Declare FM-NN predictions before Stage 1 in T-02; resolve in T-09 only | DO NOT write resolution status inline |
| CMD-04 | Append T-07 rows as table rows during each stage; close with triple-count checkpoint | DO NOT embed FM-NN acknowledgments as prose bullets |
| CMD-05 | Produce one T-06 typed exit manifest per stage | DO NOT state schema in prose without typed field assertions |
| CMD-06 | Produce T-PARITY as standalone table; enumerate per-stage N values and show arithmetic | DO NOT substitute a prose sentence for T-PARITY |
| CMD-07 | Declare all domain entities in T-01 before Stage 1 | DO NOT introduce undeclared entities during traces |
| CMD-08 | Enumerate all stages in T-03 before Stage 1 | DO NOT reference a stage not in T-03 |
| CMD-09 | Label every inter-stage boundary B[N]->[N+1] in T-04 | DO NOT use boundary references without the B[N]->[N+1] format |
| CMD-10 | Transport (ms) and Processing (ms) as separate columns in T-04 | DO NOT use "Negligible" or a single aggregate latency column |
| CMD-11 | entity.field_name format in T-04; resolve stubs after T-06 is complete | DO NOT use "data," "records," or "payload" |
| CMD-12 | T-08 SLA Domination Point as a standalone table | DO NOT embed domination point in T-04 |
| CMD-13 | Every T-10 row cites a specific IB-NN from T-05 | DO NOT write recovery without a named IB-NN step citation |
| CMD-14 | Use the IB-NN identifier (IB-03), not the process category | DO NOT substitute process category for the step identifier |
| CMD-15 | T-11 Closure Gate: one row per NH-NN and LP-NN | DO NOT substitute an aggregate count |
| CMD-16 | Close each phase with a named PG-NN gate block | DO NOT advance until all gate rows are GO |
| CMD-17 | Triple-count checkpoint at every stage close | DO NOT write [N]+[M] only; the IB-NN coverage list is the third required element |
| CMD-18 | CMD is the first scaffold row, before T-01 | DO NOT list CMD after any T-NN artifact |
| CMD-19 | T-07 Running Total column in every PG-NN gate block; pre-declared in Mandatory Columns | DO NOT produce a gate block without a T-07 Running Total column |
| CMD-20 | At every PG-NN gate, T-07 Running Total must equal sum of all prior stage [N] | DO NOT advance past a gate whose Running Total mismatches the checkpoint arithmetic |
| CMD-21 | IB-NN Coverage column in every PG-NN gate block; pre-declared in Mandatory Columns | DO NOT produce a gate block with Running Total but no IB-NN Coverage column |
| CMD-22 | Produce T-05 as STEP 0a before the scaffold; scaffold entry reads "Already produced above" | DO NOT declare T-05 as a future scaffold artifact when it already exists |
| CMD-23 | Triple-count form: CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total, IB-NN steps covered: [list] | DO NOT write a checkpoint with only [N] or [N]+[M]; the IB-NN list is required |
| CMD-24 | Responsible Role in every T-10 row; named role from T-05 | DO NOT use "team," "owner," or generic labels -- ask "who specifically executes this recovery?" |
| CMD-25 | Populate handoff contract columns in T-04 at every role-transition boundary using named domain roles | DO NOT annotate a role-transition boundary with entity-at-risk only |

For CMD-24, a quick heuristic: for each T-10 row, ask yourself "which named role in
T-05 would be paged if this failure mode materialized at 3am?" That role is the
Responsible Role. If the answer is "it depends" or "a team," look at T-05's Responsible
Role column for the step being cited.

For CMD-25, a quick heuristic: for each role-transition boundary, ask two questions:
(1) "What does the sending role commit to delivering, specifically?" (2) "What does the
receiving role need to see before it starts processing?" Both answers must name specific
artifacts or field sets, not general readiness states.

---

### PG-01: Phase 1 Gate

| Required Artifact | Declaration Status | CMD Binding Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|------------------|--------------------|--------------------|-------------------|---------------|---------|
| T-05 produced as STEP 0a before scaffold | Artifact zero | CMD-22 | 0 | [IB-NN entries from T-05] | |
| CMD is first scaffold row | | CMD-18 | n/a | n/a | |
| Every PG-NN scaffold row: T-07 Running Total AND IB-NN Coverage in Mandatory Columns | | CMD-19, CMD-21 | n/a | n/a | |
| T-04 Mandatory Columns includes both handoff contract columns | | CMD-25 | n/a | n/a | |
| T-10 Mandatory Columns includes Responsible Role | | CMD-24 | n/a | n/a | |
| CMD-23 entry present (triple-count form) | | CMD-17 | n/a | n/a | |
| Every T-NN, PG-NN, T-PARITY scaffold row carries CMD Binding | | CMD-18 | n/a | n/a | |

---

## PHASE 2: PRE-TRACE DECLARATIONS

Produce T-01, T-02, T-03, T-04, T-08 in sequence.

For T-04 handoff contract columns: at boundaries where the sending role differs from
the receiving role, populate Sending Role Delivery Guarantee and Receiving Role
Acceptance Requirement. Apply the two questions from CMD-25: "What does the sending
role commit to delivering, specifically?" and "What does the receiving role need before
starting?" Use T-05 role vocabulary for role names.

### PG-02: Phase 2 Gate

| Required Table | Population Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|---------------|-------------------|--------------------|---------------|---------|
| T-01 | | 0 | n/a | |
| T-02 | | 0 | n/a | |
| T-03 | | 0 | n/a | |
| T-04 with handoff contract columns | | 0 | n/a | |
| T-05 (artifact zero above scaffold) | Already produced | 0 | [all IB-NN entries] | |
| T-08 | | 0 | n/a | |

---

## PHASE 3: STAGE TRACES

For each stage in T-03, in sequence:

1. Describe processing in domain terms (T-01 entity vocabulary).
2. Name concrete loss points (LP-NN) or no-handling annotations (NH-NN).
3. Annotate error handling at the stage exit boundary.
4. Produce T-06 typed exit manifest.
5. Append T-07 rows for any FM-NN predictions touching this stage.
6. Close with the triple-count checkpoint. Remember the arithmetic:
   - M_k = M_(k-1) + N_k  (if M does not follow this, flag the contradiction)
   - IB-NN list at k = IB-NN list at k-1 plus any new IB steps automated here

Form: CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total, IB-NN steps covered: [list]

### PG-03: Phase 3 Gate

| Required Artifact | Completion Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|------------------|-------------------|--------------------|---------------|---------|
| T-06 exit manifest for every stage | | [sum of all N] | [IB-NN list from final checkpoint] | |
| T-04 entity.field stubs back-filled | | | | |
| Triple-count checkpoint for every stage | | | | |
| IB-NN list grew monotonically (no shrinkage) | | | | |

---

## PHASE 4: POST-TRACE RESOLUTION

T-10 reminder: for each row, apply the "who gets paged?" heuristic (CMD-24). If the
Responsible Role you are about to write is "team" or "system," look at T-05's
Responsible Role column for the IB-NN step you are citing and use that role name.

Produce T-09, T-10, T-11, T-PARITY.

### PG-04: Phase 4 Gate

| Required Table | Population Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|---------------|-------------------|--------------------|---------------|---------|
| T-09 FM-NN Resolution Audit | | [final running total] | [final IB-NN list] | |
| T-10 Recovery Audit with Responsible Role column | | | | |
| T-11 Closure Gate | | | | |
| T-PARITY arithmetic verified | | | | |

---

## PHASE 5: SYNTHESIS

Name the dominant failure pattern. Identify one alternative pipeline pattern with at
least two trade-off dimensions (at least one quantified in domain terms). Discuss the
stale data window under normal operation and under failure-mode conditions separately.
```

---

## V-05 -- Combination: Inertia-First + Role-Attributed Recovery + Handoff Continuity

**Axis**: Combination -- IB-first framing (C-43) with inertia framing throughout
(every stage framed as a replacement of an IB step), role-attributed recovery (C-45,
Responsible Role drawn strictly from T-05 vocabulary), handoff continuity contracts
as T-04 columns and standalone T-12 (C-46), triple-count checkpoints (C-44), and
IB-NN Coverage columns in every PG-NN gate (C-42). T-03 gains an "IB-NN Steps
Replaced" column making displacement claims forward-declared before any trace begins.
**Hypothesis**: anchoring the entire response to the incumbent baseline creates
compound enforcement pressure across all five C-42 to C-46 criteria simultaneously --
they all trace back to the same T-05 table produced first.

---

```
You are a Finance / Operations / Commerce data domain expert. Your task is to trace
data through the following pipeline and show how each stage replaces a specific step
from the manual process that preceded it:

{topic}

---

The core framing for this response: the incumbent baseline (T-05) is the governing
reference that every subsequent artifact departs from. The pipeline does not add stages
to a blank canvas; it replaces named manual steps with automated ones. When you finish,
a reader should be able to look at any stage trace and ask "which IB step does this
replace?" and find the answer in the triple-count checkpoint and gate IB-NN Coverage column.

ORDERING RULE: Produce T-05 (Incumbent Baseline table) as STEP 0a, before the output
scaffold. The scaffold's T-05 entry reads "Artifact zero -- produced above scaffold"
because T-05 already exists when the scaffold is written.

---

## PHASE 1: COMPLIANCE PROTOCOL DECLARATION

### STEP 0a: Incumbent Baseline (ARTIFACT ZERO -- before scaffold)

Write this table before writing any scaffold rows.

| IB-NN | Step Name | Responsible Role | Elapsed Time / Frequency |
|-------|-----------|-----------------|--------------------------|

Design guidance:
- Map each IB-NN step to the pipeline stage(s) that automate it. The "IB-NN Steps
  Replaced" column in T-03 will make these displacement claims forward-declared.
- Responsible Role names here are the canonical vocabulary for T-10 Responsible Role
  (C-45) and for T-04 handoff contract role names (C-46). Use exactly these names
  in T-10 -- not "finance team" or "accounting staff."
- Elapsed Time enables comparison with the pipeline latency profile from T-04.

---

### STEP 0b: Output Scaffold

CMD is the first row. The scaffold's T-05 entry is "Already produced above."
T-03 includes an "IB-NN Steps Replaced" column to forward-declare displacement claims.

| T#       | Table Name                      | Purpose                                                              | Mandatory Columns (exact names)                                                                                                                   | CMD Binding                    | Depends On               |
|----------|---------------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|--------------------------|
| CMD      | Structural Compliance Register  | Meta-contract; first scaffold row                                    | CMD ID, Positive Imperative, DO NOT Prohibition                                                                                                   | --                             | --                       |
| T-01     | Entity Inventory                | Domain entities before any trace                                    | Entity, Description, Key Fields                                                                                                                   | CMD-07                         | --                       |
| T-02     | FM-NN Prediction Register       | Pre-trace failure hypotheses                                        | FM-NN, Anticipated Event, Domain Consequence, Expected Designation                                                                                | CMD-03                         | --                       |
| T-03     | Stage Enumeration               | Named and sequenced stages with IB displacement claims              | Stage ID, Stage Name, Description, IB-NN Steps Replaced                                                                                          | CMD-08                         | T-05                     |
| T-04     | Boundary Inventory              | Boundaries with latency, risk, SLA%, and handoff contracts          | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA%, Sending Role Delivery Guarantee, Receiving Role Acceptance Requirement | CMD-09, CMD-10, CMD-11, CMD-25 | T-03 |
| T-05     | Incumbent Baseline              | Artifact zero -- produced above scaffold                            | IB-NN, Step Name, Responsible Role, Elapsed Time / Frequency                                                                                     | CMD-13, CMD-22                 | -- (STEP 0a)             |
| T-06     | Stage Exit Manifests            | Typed field inventory per stage exit                                | field_name, TYPE(precision), Notes                                                                                                                | CMD-05                         | T-03                     |
| T-07     | FM-NN Append-Log                | Running log; triple-count checkpoint per stage                      | FM-NN, Stage ID, Boundary / Condition, Deferral Statement                                                                                        | CMD-04, CMD-17, CMD-23         | T-02, T-03               |
| T-08     | SLA Domination Point            | Boundary consuming >50% of SLA budget                               | Domination Boundary, Exact Cumulative SLA%, Justification                                                                                         | CMD-12                         | T-04                     |
| T-09     | FM-NN Resolution Audit          | Lifecycle close for every FM-NN entry                               | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason                                                                                            | CMD-03                         | T-02, T-07               |
| T-10     | Recovery Audit Table            | Recovery rows with IB-NN anchor citation and Responsible Role       | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage, Responsible Role                                         | CMD-13, CMD-14, CMD-24         | T-04, T-05, T-06         |
| T-11     | Closure Gate                    | CLOSED / OPEN per NH-NN and LP-NN                                   | Identifier, Source (Stage / Boundary), T-10 Row, Status                                                                                           | CMD-15                         | T-10                     |
| T-PARITY | Count Parity Gate               | Cross-stage arithmetic parity                                       | Stage ID, N Rows This Stage, Running Total, GO / FLAG                                                                                             | CMD-06, CMD-18                 | T-07                     |
| PG-01    | Phase 1 Gate                    | IB-zero ordering + CMD + scaffold completeness                      | Required Artifact, Declaration Status, CMD Binding Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                          | CMD-01, CMD-16, CMD-19, CMD-21 | CMD, T-01--T-11, T-PARITY |
| PG-02    | Phase 2 Gate                    | Pre-trace table population                                          | Required Table, Population Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                                  | CMD-01, CMD-16, CMD-19, CMD-21 | T-01--T-05, T-08         |
| PG-03    | Phase 3 Gate                    | Stage trace completeness + triple-count verification                | Required Artifact, Completion Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                               | CMD-01, CMD-04, CMD-16, CMD-19, CMD-21 | T-03, T-06, T-07  |
| PG-04    | Phase 4 Gate                    | Post-trace resolution completeness                                  | Required Table, Population Status, T-07 Running Total, IB-NN Coverage, Go/No-Go                                                                  | CMD-01, CMD-06, CMD-16, CMD-19, CMD-21 | T-09--T-11, T-PARITY |

IB-NN Coverage column in PG-NN gates: at each phase boundary, this column lists the
cumulative set of IB-NN steps automated through the stages closed by this gate. At
PG-04, the IB-NN Coverage column should contain every IB-NN step that T-03's
"IB-NN Steps Replaced" column claims to automate. A step claimed in T-03 but absent
from PG-04's IB-NN Coverage is a displacement claim that was never verified -- flag it.

---

### CMD: Structural Compliance Register

| CMD ID | Positive Imperative | DO NOT Prohibition |
|--------|--------------------|--------------------|
| CMD-01 | Pre-declare every phase gate as PG-NN in scaffold | DO NOT produce a gate block without PG-NN scaffold entry |
| CMD-02 | Label scaffold column contract "Mandatory Columns (exact names)" | DO NOT use descriptive label variants |
| CMD-03 | Produce T-02 before Stage 1; resolve FM-NN in T-09 only | DO NOT write resolution status inline |
| CMD-04 | Append T-07 rows as table rows; close with triple-count checkpoint | DO NOT embed FM-NN acknowledgments in prose |
| CMD-05 | Produce T-06 typed exit manifest per stage with field_name: TYPE(precision) | DO NOT state schema in prose without typed fields |
| CMD-06 | Produce T-PARITY as standalone table with per-stage N enumeration and arithmetic | DO NOT substitute prose or PG-NN column |
| CMD-07 | List domain entities in T-01 before Stage 1 | DO NOT introduce undeclared entities during traces |
| CMD-08 | Enumerate all stages in T-03 with IB-NN Steps Replaced column populated | DO NOT leave a stage's IB-NN Steps Replaced field blank without a justification |
| CMD-09 | Label every boundary B[N]->[N+1] in T-04 | DO NOT use boundary references without B[N]->[N+1] format |
| CMD-10 | Decompose boundary latency into Transport (ms) + Processing (ms) | DO NOT use single aggregate column or "Negligible" |
| CMD-11 | entity.field_name format in T-04; resolve stubs after T-06 | DO NOT use "data," "records," or "payload" |
| CMD-12 | T-08 SLA Domination Point as standalone table | DO NOT embed domination point in T-04 |
| CMD-13 | Every T-10 row cites a specific IB-NN step from T-05 | DO NOT write recovery without specific IB-NN step citation |
| CMD-14 | Use IB-NN identifier (IB-03), not process category name | DO NOT substitute process category for step identifier |
| CMD-15 | T-11 Closure Gate: one row per NH-NN and LP-NN | DO NOT substitute aggregate count for per-row status |
| CMD-16 | Close each phase with named PG-NN gate block | DO NOT advance until all gate rows show GO |
| CMD-17 | Triple-count checkpoint at every stage close | DO NOT write [N]+[M] only; IB-NN coverage list is required third element |
| CMD-18 | CMD is first scaffold row, before T-01 | DO NOT list CMD after any T-NN artifact |
| CMD-19 | T-07 Running Total column in every PG-NN gate; pre-declared in Mandatory Columns | DO NOT produce gate block without T-07 Running Total column |
| CMD-20 | PG-NN T-07 Running Total must equal sum of all prior stage [N] | DO NOT advance past gate with arithmetic mismatch |
| CMD-21 | IB-NN Coverage column in every PG-NN gate; pre-declared in Mandatory Columns | DO NOT produce gate block with Running Total but no IB-NN Coverage column |
| CMD-22 | Produce T-05 as STEP 0a before scaffold; scaffold T-05 entry reads "Artifact zero" | DO NOT declare T-05 as a future artifact when it already exists above the scaffold |
| CMD-23 | Triple-count form: CHECKPOINT [Stage ID] COMPLETE -- [N] appended, [M] total, IB-NN steps covered: [list] | DO NOT omit the IB-NN list; a list that shrinks across stages is a contradiction -- flag it |
| CMD-24 | Responsible Role in every T-10 row; must come from T-05 Responsible Role column | DO NOT use "team," "owner," "system" -- trace to the T-05 row cited and use its Responsible Role |
| CMD-25 | At every role-transition boundary in T-04, populate both handoff contract columns; use T-05 role vocabulary | DO NOT leave a role-transition boundary with entity-at-risk annotation only |

---

### PG-01: Phase 1 Gate

| Required Artifact | Declaration Status | CMD Binding Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|------------------|--------------------|--------------------|-------------------|---------------|---------|
| T-05 produced as STEP 0a, before scaffold | Artifact zero | CMD-22 | 0 (pre-trace) | [All IB-NN entries from T-05] | |
| CMD as first scaffold row | | CMD-18 | n/a | n/a | |
| T-03 Mandatory Columns includes "IB-NN Steps Replaced" | | CMD-08 | n/a | n/a | |
| T-04 Mandatory Columns includes both handoff contract columns | | CMD-25 | n/a | n/a | |
| T-10 Mandatory Columns includes "Responsible Role" | | CMD-24 | n/a | n/a | |
| Every PG-NN scaffold row: T-07 Running Total AND IB-NN Coverage in Mandatory Columns | | CMD-19, CMD-21 | n/a | n/a | |
| CMD-22, CMD-23, CMD-24, CMD-25 all present in CMD register | | CMD-18 | n/a | n/a | |

---

## PHASE 2: PRE-TRACE DECLARATIONS

Produce T-01, T-02, T-03, T-04, T-08 in sequence.

T-03 note: populate "IB-NN Steps Replaced" for every stage. If a stage does not
replace any IB step directly, write "IB-NN: none (infrastructure stage)" -- a blank
cell fails CMD-08.

T-04 note: for every role-transition boundary (where the sending role differs from the
receiving role), populate both handoff contract columns. Role names must come from
T-05's Responsible Role column, not generic labels. Same-role boundaries write
"Same role -- contract exempt" in both columns.

### PG-02: Phase 2 Gate

| Required Table | Population Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|---------------|-------------------|--------------------|---------------|---------|
| T-01 Entity Inventory | | 0 | n/a | |
| T-02 FM-NN Prediction Register | | 0 | n/a | |
| T-03 Stage Enumeration with IB-NN Steps Replaced populated | | 0 | n/a | |
| T-04 Boundary Inventory with handoff contract columns | | 0 | n/a | |
| T-05 (artifact zero, produced in STEP 0a) | Already produced | 0 | [all IB-NN entries] | |
| T-08 SLA Domination Point | | 0 | n/a | |

---

## PHASE 3: STAGE TRACES

For each stage in T-03:

1. Frame the stage as a replacement of its T-03 "IB-NN Steps Replaced" entries.
   Open with: "Stage [ID] automates IB-[NN]: [step name from T-05]."
2. Name domain entities (T-01 vocabulary), concrete LP-NN or NH-NN points.
3. Annotate boundary error handling.
4. Produce T-06 typed exit manifest. Back-fill T-04 stubs.
5. Append T-07 rows for intersecting FM-NN predictions.
6. Close with triple-count checkpoint:
   CHECKPOINT [Stage ID] COMPLETE -- [N] rows appended, [M] total, IB-NN steps covered: [list]
   The IB-NN list at this stage = prior list union T-03's "IB-NN Steps Replaced" for this stage.
   A list that does not include a step claimed in T-03's IB-NN Steps Replaced column is a
   contradiction between T-03's displacement claim and the checkpoint's coverage evidence.
   Flag the contradiction explicitly rather than silently correcting it.

---

### PG-03: Phase 3 Gate

| Required Artifact | Completion Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|------------------|-------------------|--------------------|---------------|---------|
| T-06 exit manifest for every stage | | [sum of all N] | [IB-NN list from final checkpoint] | |
| T-04 entity.field stubs back-filled | | | | |
| Triple-count checkpoint for every stage | | | | |
| IB-NN list at final checkpoint covers all T-03 "IB-NN Steps Replaced" claims | | | | |

---

## PHASE 4: POST-TRACE RESOLUTION

T-10 reminder: the Responsible Role column must use a role name from T-05's Responsible
Role column. For each T-10 row, trace to the IB-NN step cited in that row, find its
Responsible Role in T-05, and use that exact role name. If two IB steps with different
responsible roles feed into one recovery row, name the primary accountable role.

Produce T-09, T-10, T-11, T-PARITY.

### PG-04: Phase 4 Gate

| Required Table | Population Status | T-07 Running Total | IB-NN Coverage | Go/No-Go |
|---------------|-------------------|--------------------|---------------|---------|
| T-09 FM-NN Resolution Audit | | [final running total] | [full IB-NN list] | |
| T-10 Recovery Audit -- Responsible Role from T-05 vocabulary | | | | |
| T-11 Closure Gate | | | | |
| T-PARITY arithmetic verified | | | | |

---

## PHASE 5: SYNTHESIS

Name the dominant failure pattern across all LP-NN and NH-NN entries. Name the IB
step that represented the highest manual effort (by Elapsed Time in T-05) and confirm
whether it has been fully automated or partially displaced. Identify one alternative
pipeline pattern with at least two trade-off dimensions, one quantified. Stale data
window: normal operation vs failure-mode addressed separately.
```
