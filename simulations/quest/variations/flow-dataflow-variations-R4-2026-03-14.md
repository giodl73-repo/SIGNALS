Here are the 5 R4 variations, written against the v4 rubric with C-16/C-17/C-18 as primary targets:

---

## V-01 — Role sequence: Artifact-labeled dependency chain
**Axis:** Role sequence  
**Hypothesis:** Machine-readable `ARTIFACT:` headers make C-16 citations unambiguous and verifiable by token match. An `IMMUTABLE THRESHOLD` block names the prohibition scope (all roles after Role 2). INCUMBENT BASELINE leads (before DOMAIN CONTEXT), reversing R3 V-01 order to ground the contract in incumbent failures first.

## V-02 — Phrasing register: Numbered specification requirements
**Axis:** Phrasing register  
**Hypothesis:** Unique requirement IDs (R-01..R-13) let the model cite constraints by number, creating a structured C-16 mechanism verifiable by label. C-17 is split into two requirements: R-03 (declaration) and R-04 (prohibition) — matching the rubric's distinction between C-13 and C-17. C-18 is split into R-08 (field definition) and R-09 (deferral prohibition).

## V-03 — Inertia framing: Incumbent as structural anchor
**Axis:** Inertia framing (completing R3's incomplete V-03)  
**Hypothesis:** Every section derives from or responds to F-01/F-02. A `F-02 status` field in every BOUNDARY CHECK provides a running freshness verdict throughout the trace. Loss points are grounded in known failures, not abstract risk.

## V-04 — Phase gates + Finance-first role sequence
**Axis:** Lifecycle emphasis + Role sequence  
**Hypothesis:** Phase gate checklists must be ticked in output before proceeding — C-18 is enforced by the Phase 2 gate checking each boundary's elapsed field before Phase 3 begins. C-17 appears in both DOMAIN CONTEXT and the gate, creating two enforcement surfaces.

## V-05 — Table-primary (named-section fix) + Explicit C-16/C-17/C-18 fields
**Axis:** Output format + C-16/C-17/C-18 structural  
**Hypothesis:** R3 V-02 failed C-10/C-15 because table rows ≠ named sections. Fix: named section headers (`INCUMBENT BASELINE`, `DOMAIN CONTEXT`) wrap the tables. C-16 enforced by required `Citing:` row in every boundary table. C-17 enforced by required `LOCK` row in DOMAIN CONTEXT. C-18 enforced by named `Elapsed (cumulative)` row with an explicit deferral prohibition.
 one lateness or staleness failure of the incumbent. Include
  a time magnitude (e.g., "reconciliation reports were 18 hours stale").
- Downstream consumer: who received the output of the incumbent process,
  and what decision they made with it.

Label the failures F-01 and F-02 explicitly. They will be cited by label in
later roles.

---

## ROLE 2 — Domain Contract Setter

Open with: "Drawing from ARTIFACT: INCUMBENT BASELINE:"

Produce the DOMAIN CONTEXT artifact. Open with this header on its own line:

  ARTIFACT: DOMAIN CONTEXT

Declare using only entity names introduced in INCUMBENT BASELINE:

- Entity vocabulary: all in-scope business entity names (carry names from
  INCUMBENT BASELINE without substitution)
- Downstream consumer: (carry from INCUMBENT BASELINE)
- Business cadence: (carry from INCUMBENT BASELINE)
- Staleness threshold: "<entity> must not exceed <N> <unit> at <destination>"

Immediately below the threshold, write this block verbatim (fill in brackets):

  IMMUTABLE THRESHOLD — locked as of ARTIFACT: DOMAIN CONTEXT
  Value: [entity] must not exceed [N] [unit] at [destination]
  Locked after: ARTIFACT: DOMAIN CONTEXT is written
  Prohibited revisions: no role after this point may adjust this value.
    If analysis implies a tighter threshold is warranted, note it as a
    recommendation in Role 5 — do not change this value.
  Derivation: set at [N] because ARTIFACT: INCUMBENT BASELINE Failure F-02
    showed [X-duration] delays; [N] represents the maximum tolerable window.

---

## ROLE 3 — Pipeline Analyst

Open with: "Tracing against ARTIFACT: DOMAIN CONTEXT entity vocabulary:"

Trace the data through every stage. For each stage, write:

  STAGE N — [Stage Name]
  Schema in:  [field names and types at stage entry]
  Schema out: [all changes — list every rename, drop, and type change;
              if none: "schema unchanged"]
  Latency:    [value, range, or characterization — do not omit]
  Loss point: [specific condition — name the data item and the failure
              mechanism; "errors may occur" fails this field]
  F-analog:   [F-01 / F-02 / none — cite ARTIFACT: INCUMBENT BASELINE
              if this loss point has an incumbent predecessor]

After each consecutive stage pair, before writing the next stage, insert this
boundary block:

  BOUNDARY CHECK [Stage N → Stage N+1]
  Citing: ARTIFACT: DOMAIN CONTEXT
  Entity: [exact entity name from ARTIFACT: DOMAIN CONTEXT —
          "data" or "records" fails this field]
  Error handling: [specific mechanism] OR [NONE — flag for Role 4]
  Latency this boundary: [value]
  Elapsed (cumulative): [sum of all stage latencies and boundary latencies
                        recorded above — computed here, not in a later section]

The `Elapsed (cumulative)` field is a required field in this block. It must be
computed additively from the values already written above. Do not defer it to a
post-stage summary. Do not write Stage N+1 until this block is complete.

---

## ROLE 4 — Stale Data Analyst

Open with: "Evaluating against ARTIFACT: DOMAIN CONTEXT threshold and
Elapsed (cumulative) from final BOUNDARY CHECK in Role 3:"

Write a STALE ANALYSIS table with these exact columns:

| Entity | Threshold (ARTIFACT: DOMAIN CONTEXT) | Elapsed (Role 3 final boundary) | Delta | Status | Scenario |
|--------|--------------------------------------|---------------------------------|-------|--------|----------|

- Populate one row for normal-operation elapsed.
- Populate one row for failure-mode elapsed (e.g., one retry cycle).
- Status = WITHIN SLA or STALE. Delta = elapsed minus threshold.
- Derive all values from ARTIFACT: DOMAIN CONTEXT and Role 3 BOUNDARY CHECKs.
  Do not assert staleness from description alone.
- Close with: "ARTIFACT: INCUMBENT BASELINE F-02 showed [X-duration] delay.
  Under pipeline failure the elapsed is [Y]. SLA threshold is [N]. [PASS/FAIL]."

---

## ROLE 5 — Recovery Architect and Pattern Advisor

Open with: "Closing gaps identified in Role 3 BOUNDARY CHECKs and Role 1
ARTIFACT: INCUMBENT BASELINE failure vocabulary:"

### Recovery Prescriptions

For each BOUNDARY CHECK from Role 3 with Error handling = NONE, and for each
loss point named in Role 3 Stage blocks:

- Prescribe one specific recovery mechanism (not "add retry logic" — name the
  pattern: dead-letter queue, idempotent upsert, saga rollback, etc.).
- Where the loss point has a predecessor in ARTIFACT: INCUMBENT BASELINE,
  write: "ARTIFACT: INCUMBENT BASELINE [F-01/F-02]: [quote the failure].
  This prescription closes it by [mechanism]."

### Pattern Trade-Off

Name one alternative pipeline pattern. Provide this comparison table:

| Dimension | Current pipeline | Alternative: [name] | ARTIFACT: INCUMBENT BASELINE relevance |
|-----------|-----------------|---------------------|-----------------------------------------|
| [dimension 1 — latency or throughput] | | | [F-01 or F-02 citation, or "not applicable"] |
| [dimension 2 — failure mode or ops burden] | | | [F-01 or F-02 citation, or "not applicable"] |

At least one row must cite ARTIFACT: INCUMBENT BASELINE by name. A trade-off
table with no incumbent reference fails this section.

---

## Scenario

{scenario}

## Output order

ARTIFACT: INCUMBENT BASELINE (Role 1) ->
ARTIFACT: DOMAIN CONTEXT with IMMUTABLE THRESHOLD block (Role 2) ->
Stage blocks with interleaved BOUNDARY CHECK blocks (Role 3) ->
STALE ANALYSIS table (Role 4) ->
RECOVERY PRESCRIPTIONS + PATTERN TRADE-OFF (Role 5)
```

---

## V-02 — Axis: Phrasing register (Numbered specification requirements)

**Hypothesis:** R3 V-05 used conversational register with inline checkpoints. The opposite extreme — a formal specification style where each constraint has a unique requirement ID (R-01, R-02, ...) — may reduce interpretation latitude differently. When constraints are uniquely identified, a model can be instructed to cite requirement IDs in its output (e.g., "Per R-02 DOMAIN CONTEXT"), creating a structured citation mechanism for C-16 that is verifiable by label, not by prose matching. C-17 and C-18 are expressed as prohibition requirements separate from the declaration requirements they strengthen.

**Differs from prior variations in:** specification-style IDs for every constraint; citation syntax uses requirement numbers; C-17 is expressed as a prohibition requirement (R-04) separate from the declaration requirement (R-03); C-18 is expressed as a data-format requirement (R-08) with a separate deferral prohibition (R-09).

---

```
You are running the flow-dataflow skill.

Execute the following requirements in order. Where a requirement references a
prior requirement's output, cite that requirement by its ID (e.g., "Per R-02
DOMAIN CONTEXT"). Requirements without citations to their predecessors are
non-compliant.

---

## PHASE 1 — Pre-Trace Declarations

R-01  Write a section named INCUMBENT BASELINE. Identify: (a) the primary
      business entity by exact name — "data" and "records" are not entity
      names; (b) the manual or legacy process this pipeline replaces; (c) the
      business cadence of that process; (d) Failure F-01: a specific data loss
      or corruption failure; (e) Failure F-02: a specific lateness or staleness
      failure including a time magnitude; (f) the downstream consumer.
      Label failures F-01 and F-02 explicitly.

R-02  Write a section named DOMAIN CONTEXT. This section must use only entity
      names introduced in R-01 INCUMBENT BASELINE. Declare: (a) entity
      vocabulary; (b) downstream consumer (carry from R-01); (c) business
      cadence (carry from R-01); (d) staleness threshold: "[entity] must not
      exceed [N] [unit] at [destination]." Begin this section with the line:
      "Per R-01 INCUMBENT BASELINE:"

R-03  In R-02 DOMAIN CONTEXT, connect the staleness threshold to R-01 Failure
      F-02: "Threshold set at [N] because R-01 INCUMBENT BASELINE F-02
      established that [X-duration] delays caused [business harm]."

R-04  Immediately after the threshold in R-02 DOMAIN CONTEXT, write this
      sentence verbatim (fill in brackets): "This threshold is fixed as of
      R-02 DOMAIN CONTEXT. It may not be revised in any requirement below."
      This prohibition is required. A threshold declaration without an explicit
      post-declaration revision prohibition does not satisfy R-04.

---

## PHASE 2 — Pipeline Trace

R-05  For each pipeline stage, write a STAGE block with these fields:
        STAGE [N] — [Stage Name]
        Schema in:  [fields at stage entry — or diff from prior stage]
        Schema out: [all changes — renames, drops, type changes]
        Latency:    [value, range, or characterization]
        Loss point: [specific named risk — "errors may occur" fails]
        R-01 analog: [F-01 / F-02 / none]

R-06  After every consecutive stage pair, before writing the next stage, write
      a BOUNDARY CHECK block with these fields:
        BOUNDARY CHECK [Stage N -> Stage N+1]
        Per: R-02 DOMAIN CONTEXT
        Entity: [exact name from R-02 — "data" or "records" fails]
        Error handling: [mechanism] OR [NONE]
        Latency this boundary: [value]
        Elapsed (cumulative): [see R-08]

R-07  Every BOUNDARY CHECK block must include an Entity field naming a term
      from R-02 DOMAIN CONTEXT. A block with Entity = "data" or Entity =
      "records" is non-compliant with R-06 and must be corrected before the
      next stage is written.

R-08  The `Elapsed (cumulative)` field in each BOUNDARY CHECK block must
      contain the additive sum of all stage latencies and boundary latencies
      recorded in prior STAGE blocks and BOUNDARY CHECK blocks in this trace.
      This field is part of the BOUNDARY CHECK block structure — not a
      post-stage summary.

R-09  The `Elapsed (cumulative)` field required by R-08 may not be deferred to
      a post-stage summary section. A BOUNDARY CHECK block written without
      this field, or with this field appearing only in a post-trace summary,
      does not comply with R-08.

---

## PHASE 3 — Stale Analysis

R-10  After the final BOUNDARY CHECK, write a STALE ANALYSIS section. Begin
      with: "Per R-02 DOMAIN CONTEXT threshold and R-06 final BOUNDARY CHECK
      Elapsed (cumulative):" Then write this table:
        | Entity | R-02 threshold | R-06 final elapsed | Delta | Status |
      Status = WITHIN SLA or STALE. Delta = elapsed minus threshold.
      Values must derive from R-02 and R-06 outputs — not from independent
      assertion.

R-11  Add a second STALE ANALYSIS row for the failure-mode scenario (e.g., one
      retry or dead-letter reprocess cycle). Use the extended elapsed total.
      Cite R-01 INCUMBENT BASELINE F-02: "R-01 INCUMBENT BASELINE F-02:
      [quote]. Pipeline failure mode elapsed: [Y]. [PASS/FAIL]."

---

## PHASE 4 — Recovery and Trade-Off

R-12  Write a RECOVERY PRESCRIPTIONS section. For each BOUNDARY CHECK with
      Error handling = NONE and each loss point from R-05, write one specific
      prescription. Where R-01 INCUMBENT BASELINE contains an analogous
      failure, write: "R-01 INCUMBENT BASELINE [F-01/F-02]: [quote failure].
      Prescription closes it by [mechanism]."

R-13  Write a PATTERN TRADE-OFF section. Begin with: "Per R-01 INCUMBENT
      BASELINE failure vocabulary:" Name one alternative pattern. Provide a
      table with at least two comparison dimensions. At least one row must cite
      R-01 INCUMBENT BASELINE by requirement number:

        | Dimension | Current pipeline | Alternative: [name] | R-01 relevance |
        |-----------|-----------------|---------------------|----------------|

---

## Scenario

{scenario}

## Output order

R-01 INCUMBENT BASELINE ->
R-02 DOMAIN CONTEXT (with R-03 threshold derivation and R-04 prohibition line) ->
R-05/R-06 Stage blocks with interleaved BOUNDARY CHECK blocks ->
R-10/R-11 STALE ANALYSIS ->
R-12 RECOVERY PRESCRIPTIONS ->
R-13 PATTERN TRADE-OFF
```

---

## V-03 — Axis: Inertia framing (Incumbent process as structural anchor — completing R3 V-03)

**Hypothesis:** R3 V-03 was marked incomplete — only an axis label and hypothesis were generated, no prompt body. This variation completes it. The incumbent process is not context; it is the frame. Every section is written as a direct response to a named incumbent failure. C-16 is enforced by requiring each role to name the prior role's section before writing its own. C-17 is a LOCK block inside DOMAIN CONTEXT. C-18 is a named field in every BOUNDARY CHECK block with a "do not defer" instruction.

**Differs from prior variations in:** the analytical posture — analyst frames the pipeline as evidence that specific incumbent failures are solved. Loss points are grounded in known incumbent failures. Stale analysis closes back to the incumbent time magnitude. A F-02 status field in every boundary block provides a running freshness verdict throughout the trace.

---

```
You are running the flow-dataflow skill.

Frame: this pipeline exists because the incumbent failed in specific ways.
Do not describe the pipeline in the abstract — show that it solves the
failures of what it replaced. Every section derives from or responds to a
named incumbent failure. Sections that introduce risks not present in the
incumbent must explain why they are novel.

---

## ROLE 1 — Business Historian

Write the INCUMBENT BASELINE section before any pipeline stage. Answer:

- Entity name: the exact business name of what flows through this pipeline
  (e.g., Purchase Order, Settlement Record, Inventory Adjustment — not "data").
- Incumbent process: the manual or legacy process before this pipeline.
- Business cadence: how often the incumbent process ran.
- Failure F-01: a data loss or correctness failure — describe what was lost or
  wrong, and how often it occurred.
- Failure F-02: a lateness or staleness failure — include a time magnitude.
- Downstream consumer: who relied on the incumbent output, and for what
  decision.

Label failures F-01 and F-02 explicitly. Every subsequent section that
discusses data integrity traces to F-01. Every section discussing freshness
traces to F-02.

---

## ROLE 2 — Domain Context Setter

Begin: "Using entity vocabulary from INCUMBENT BASELINE:"

Write the DOMAIN CONTEXT section. Use only entity names introduced in
INCUMBENT BASELINE. Declare:

- Entity vocabulary (carry exact names from INCUMBENT BASELINE)
- Downstream consumer (carry from INCUMBENT BASELINE)
- Business cadence (carry from INCUMBENT BASELINE)
- Staleness threshold: "[entity] must not exceed [N] [unit] at [destination]"
- Incumbent connection: "Threshold set at [N] because INCUMBENT BASELINE F-02
  established [X-duration] delays produced [business harm]. [N] is the
  maximum tolerable window."

Write this LOCK block immediately after the threshold:

  LOCK — as of DOMAIN CONTEXT
  The staleness threshold above is fixed. No section after DOMAIN CONTEXT
  may revise it. If pipeline analysis implies the threshold should differ,
  note it as a recommendation in the final section only. The contract value
  remains [N] [unit].

---

## ROLE 3 — Pipeline Analyst

Begin: "Tracing the pipeline that responds to INCUMBENT BASELINE F-01 and
F-02:"

For each stage, write:

  STAGE N — [Stage Name]
  Schema in:  [field names and types — or diff from prior stage exit]
  Schema out: [all changes: renames, drops, type changes — "unchanged" if none]
  Latency:    [value, range, or characterization]
  Loss point: [specific named risk — if this is an F-01 analog, write:
              "INCUMBENT BASELINE F-01 analog: [how it resembles the failure]";
              if novel, write "novel risk: [description]"]

After each consecutive stage pair, write a BOUNDARY CHECK before the next
stage:

  BOUNDARY CHECK [Stage N -> Stage N+1]
  Citing: DOMAIN CONTEXT
  Entity: [exact name from DOMAIN CONTEXT — "data" or "records" fails]
  Error handling: [mechanism] OR [NONE — flag for recovery section]
  Latency this boundary: [value]
  Elapsed (cumulative): [running total of all stage and boundary latencies
                        above — computed in this block, not deferred]
  F-02 status: [WITHIN SLA / AT RISK / STALE — compare elapsed to DOMAIN
               CONTEXT threshold]

`Elapsed (cumulative)` and `F-02 status` are required fields in every block.
Do not write the next stage until this block is fully written.

---

## ROLE 4 — Stale Data Analyst

Begin: "Drawing from DOMAIN CONTEXT staleness threshold and Elapsed
(cumulative) from Role 3 BOUNDARY CHECKs:"

Write a STALE ANALYSIS table:

| Entity | DOMAIN CONTEXT threshold | Role 3 final elapsed | Delta | Status | Scenario |
|--------|--------------------------|----------------------|-------|--------|----------|
| [name] | [N unit] | [from last BOUNDARY CHECK] | [elapsed - N] | WITHIN SLA or STALE | Normal |
| [name] | [N unit] | [retry elapsed] | [delta] | [status] | Failure mode |

Close the loop: "INCUMBENT BASELINE F-02 produced [X-duration] delay.
Pipeline failure mode produces [Y]. DOMAIN CONTEXT threshold is [N].
F-02 [has been resolved / has not been resolved]."

---

## ROLE 5 — Recovery Architect and Pattern Advisor

Begin: "Closing open failure loops from Role 3 BOUNDARY CHECKs and INCUMBENT
BASELINE F-01 / F-02:"

### Recovery Prescriptions

For each BOUNDARY CHECK from Role 3 with Error handling = NONE, and each named
loss point:

- Prescribe a specific recovery mechanism.
- Close the incumbent loop: "INCUMBENT BASELINE [F-01/F-02]: [quote the
  failure]. This prescription addresses it by [mechanism]. Under the incumbent
  this failure [was not caught / caused X harm]; the prescription prevents
  recurrence by [Y]."

### Pattern Trade-Off

Name one alternative pattern. Compare on at least two dimensions. For each
dimension, state whether INCUMBENT BASELINE F-01 or F-02 is better or worse
addressed by the alternative:

| Dimension | Current pipeline | Alternative: [name] | Incumbent relevance |
|-----------|-----------------|---------------------|---------------------|
| [dimension 1] | | | INCUMBENT BASELINE [F-01/F-02]: [connection] |
| [dimension 2] | | | INCUMBENT BASELINE [F-01/F-02]: [connection] or "novel risk" |

At least one row must cite INCUMBENT BASELINE by name.

---

## Scenario

{scenario}

## Output order

INCUMBENT BASELINE ->
DOMAIN CONTEXT (with LOCK block) ->
Stage blocks with interleaved BOUNDARY CHECK blocks ->
STALE ANALYSIS ->
RECOVERY PRESCRIPTIONS ->
PATTERN TRADE-OFF
```

---

## V-04 — Axis combination: Lifecycle emphasis (phase gates) + Role sequence (Finance-first)

**Hypothesis:** Phase gates between phases function as mandatory verification checkpoints — the model must confirm required artifacts are present and correctly formed before advancing. Finance-first role sequencing ensures the staleness contract is established by the authoritative downstream consumer (AP / reporting), which may produce more realistic threshold values than a generic domain expert. The phase gate structure makes C-18 structurally enforced: the Phase 2 gate checks for incremental elapsed fields before the model is permitted to write Phase 3. C-17 appears in both DOMAIN CONTEXT and the Phase 1 gate, creating two enforcement surfaces.

**Differs from prior variations in:** phase gates are output checklists that must be ticked in the output before proceeding; Finance leads; C-17 prohibition appears in the gate itself; Phase 2 gate explicitly checks that every boundary block has an incremental elapsed field before Phase 3 may begin.

---

```
You are running the flow-dataflow skill.

This trace runs in three phases. Each phase ends with a PHASE GATE — a
checklist you must tick in your output before starting the next phase.
An unticked gate item means the phase is incomplete; repair the artifact,
then tick the item and proceed.

---

## PHASE 1 — Foundations

You are a Finance domain expert who receives the output of this pipeline for
AP reconciliation, financial close, or management reporting.

### INCUMBENT BASELINE

Write this section first. Name:

- Entity name: the exact business term for what this pipeline carries
  (e.g., Vendor Invoice, GL Journal Entry, Cost Allocation Record — not "data").
- Incumbent process: the manual or legacy process this pipeline replaced.
- Cadence: how often the incumbent process produced output.
- F-01: a specific data loss or posting-error failure of the incumbent.
- F-02: a specific lateness or stale-reporting failure. Include the time
  magnitude (e.g., "month-end close data was 22 hours stale entering the
  reporting database").
- Consumer: who received the incumbent output, and what close or decision
  cycle it fed.

### DOMAIN CONTEXT

Using entity names from INCUMBENT BASELINE, declare:

- Entity vocabulary (exact names — no substitution from INCUMBENT BASELINE)
- Downstream consumer (carry from INCUMBENT BASELINE)
- Business cadence (carry from INCUMBENT BASELINE)
- Staleness threshold: "[entity] must not exceed [N] [unit] at [destination]"

Immediately after the threshold, write:

  IMMUTABLE — Phase 1 DOMAIN CONTEXT
  This threshold is [N] [unit]. It is fixed as of this section.
  Roles in Phase 2 and Phase 3 may not revise this value.
  If Phase 2 timing analysis implies a tighter threshold is needed,
  record it as a Phase 3 recommendation. This contract value does not change.

Connect to incumbent: "The [N] threshold is derived from INCUMBENT BASELINE
F-02: [quote F-02]. [N] caps the failure window that F-02 allowed."

### PHASE 1 GATE

Before writing Phase 2, tick each item:

[ ] INCUMBENT BASELINE names at least two labeled failures (F-01 and F-02)
[ ] DOMAIN CONTEXT uses entity names from INCUMBENT BASELINE without substitution
[ ] Staleness threshold is stated as a contract with the IMMUTABLE block present
[ ] IMMUTABLE block names Phase 2 and Phase 3 as the scope of the prohibition
[ ] Threshold is connected to F-02 with a quoted time magnitude

All five must be ticked. If any is unchecked, complete the missing content
and tick it.

---

## PHASE 2 — Pipeline Trace

You are an operations engineer. Begin:

"Tracing from Phase 1 DOMAIN CONTEXT entity vocabulary:"

For each stage, write:

  STAGE N — [Stage Name]
  Schema in:  [field names and types — or diff from prior stage]
  Schema out: [all changes: renames, drops, type changes; "unchanged" if none]
  Latency:    [value, range, or characterization]
  Loss point: [specific condition — name the entity and failure mode;
              if this is an F-01 analog: "F-01 analog: [how it matches]"]

After each consecutive stage pair, before writing the next stage, write:

  BOUNDARY CHECK [Stage N -> Stage N+1]
  Phase 1 reference: DOMAIN CONTEXT
  Entity: [exact name from Phase 1 DOMAIN CONTEXT — "data" fails]
  Error handling: [mechanism] OR [NONE]
  Latency this boundary: [value]
  Elapsed (cumulative): [sum of all stage and boundary latencies written above]

`Elapsed (cumulative)` is a required field in every BOUNDARY CHECK block.
It must be computed here, incrementally, as a side effect of writing this
block. It may not be omitted or deferred to a post-stage section.

### PHASE 2 GATE

Before writing Phase 3, tick each item:

[ ] Every consecutive stage pair has an interleaved BOUNDARY CHECK
[ ] Every BOUNDARY CHECK names an Entity from Phase 1 DOMAIN CONTEXT
    (not "data" or "records")
[ ] Every BOUNDARY CHECK has an `Elapsed (cumulative)` field computed
    additively from the stage and boundary latencies above it
[ ] Every stage has a named loss point (not generic language)
[ ] No stage is missing a Schema out field

All five must be ticked. If any is unchecked, complete the missing content
and tick it.

---

## PHASE 3 — Analysis and Closure

You are a commerce or reporting analyst focused on data freshness and
downstream decision quality. Begin:

"Drawing from Phase 1 DOMAIN CONTEXT threshold and Phase 2 final BOUNDARY
CHECK Elapsed (cumulative):"

### Stale Analysis

| Entity | Phase 1 threshold | Phase 2 final elapsed | Delta | Status | Scenario |
|--------|------------------|-----------------------|-------|--------|----------|
| [name] | [N unit] | [from final boundary] | [elapsed - N] | WITHIN SLA or STALE | Normal |
| [name] | [N unit] | [retry elapsed] | [delta] | [status] | Failure mode |

Close: "Phase 1 INCUMBENT BASELINE F-02 produced [X]. Phase 2 pipeline under
failure mode produces [Y]. Phase 1 threshold is [N]: [PASS/FAIL]."

### Recovery Prescriptions

For each Phase 2 BOUNDARY CHECK with Error handling = NONE, and each loss
point from Phase 2 stages:

- Prescribe a specific recovery mechanism.
- Reference Phase 1 INCUMBENT BASELINE: "Phase 1 INCUMBENT BASELINE
  [F-01/F-02]: [quote failure]. Prescription: [mechanism]. This closes the
  failure loop because [Y]."

### Pattern Trade-Off

Name one alternative pipeline pattern. Compare on at least two dimensions:

| Dimension | Current pipeline | Alternative: [name] | Phase 1 INCUMBENT BASELINE relevance |
|-----------|-----------------|---------------------|--------------------------------------|
| [dimension 1] | | | Phase 1 [F-01/F-02]: [connection] |
| [dimension 2] | | | Phase 1 [F-01/F-02]: [connection] or "novel" |

At least one row must cite Phase 1 INCUMBENT BASELINE by name.

---

## Scenario

{scenario}

## Output order

Phase 1: INCUMBENT BASELINE -> DOMAIN CONTEXT -> PHASE 1 GATE
Phase 2: Stage blocks with interleaved BOUNDARY CHECK blocks -> PHASE 2 GATE
Phase 3: STALE ANALYSIS -> RECOVERY PRESCRIPTIONS -> PATTERN TRADE-OFF
```

---

## V-05 — Axis combination: Output format (table-primary, named-section fix) + Explicit C-16/C-17/C-18 table fields

**Hypothesis:** R3 V-02 scored 97.5 but failed C-10 and C-15 because it used table rows inside a "Pass 1 — Context Table" header rather than sections named DOMAIN CONTEXT and INCUMBENT BASELINE. The fix is minimal: named section headers wrap the table content rather than the table living inside a generic pass label. This variation also adds a `Citing:` row to every boundary table (enforcing C-16 as a format field), makes the LOCK line a named table row in DOMAIN CONTEXT (enforcing C-17 as a required cell, not just prose), and makes `Elapsed (cumulative)` a named table row in every boundary table (enforcing C-18 structurally with a deferral prohibition).

**Differs from R3 V-02 in:** (1) section headers are INCUMBENT BASELINE and DOMAIN CONTEXT, not "Pass 1 — Context Table"; (2) C-16 enforced by a required `Citing:` row in every boundary table; (3) C-17 enforced by a required `LOCK` row in the DOMAIN CONTEXT table; (4) C-18 enforced by a named `Elapsed (cumulative)` row in boundary tables with an explicit deferral prohibition; (5) INCUMBENT BASELINE is a named section with its own table, not rows inside a context table.

---

```
You are running the flow-dataflow skill.

Output is table-primary. Wherever structure can be expressed as a table, use
a table. Prose is for derivations and connections that tables cannot express.
Required sections are named headers — table content lives under named headers,
not instead of them. Use the section names below exactly.

---

## INCUMBENT BASELINE

Write this section before DOMAIN CONTEXT or any stage work.

| Field | Value |
|-------|-------|
| Entity name | [exact business name — "data" and "records" are not entity names] |
| Incumbent process | [name of the manual or legacy process replaced] |
| Business cadence | [how often the incumbent process ran] |
| Downstream consumer | [team name and decision type] |
| F-01 — data failure | [specific data loss or corruption failure of the incumbent] |
| F-02 — lateness failure | [specific staleness or delay failure — include time magnitude] |
| F-01 business cost | [characterization of impact] |
| F-02 business cost | [characterization of impact] |

Failure labels F-01 and F-02 will be cited by label in all subsequent sections.

---

## DOMAIN CONTEXT

Write this section before Stage 1. The first row of the table must be `Citing`.

| Field | Value |
|-------|-------|
| Citing | INCUMBENT BASELINE |
| Primary entity | [same name as INCUMBENT BASELINE Entity name] |
| In-scope entities | [all business entity names — carry from INCUMBENT BASELINE] |
| Downstream consumer | [carry from INCUMBENT BASELINE] |
| Business cadence | [carry from INCUMBENT BASELINE] |
| Staleness threshold | [entity] must not exceed [N] [unit] at [destination] |
| Threshold derivation | Derived from INCUMBENT BASELINE F-02: [quote F-02 time magnitude]. [N] caps this failure window. |
| LOCK | This threshold is fixed as of DOMAIN CONTEXT. No subsequent section may revise it. If analysis implies a different value, record it as a recommendation in Pattern Trade-Off only. |

The `Citing` and `LOCK` rows are required. A DOMAIN CONTEXT table without
either row is incomplete.

---

## Pipeline Stages and Boundary Checks

For each stage, write a STAGE block followed immediately by a BOUNDARY CHECK
table. Do not write the next stage until the BOUNDARY CHECK table for the
prior boundary is complete.

**STAGE block:**

```
STAGE [N] — [Stage Name]
Schema in:  [fields at stage entry — or diff from prior stage]
Schema out: [all changes: renames, drops, type changes; "unchanged" if none]
Latency:    [value, range, or characterization]
Loss point: [specific named risk — "errors may occur" fails this field]
F-analog:   [F-01 / F-02 / none — cite INCUMBENT BASELINE if applicable]
```

**BOUNDARY CHECK table (insert between every consecutive stage pair):**

| Field | Value |
|-------|-------|
| Boundary | Stage [N] -> Stage [N+1] |
| Citing | DOMAIN CONTEXT |
| Entity | [exact name from DOMAIN CONTEXT — "data" or "records" fails] |
| Error handling | [mechanism] OR [NONE] |
| Latency this boundary | [value] |
| Elapsed (cumulative) | [additive sum: all stage latencies + all prior boundary latencies] |
| F-02 status | [WITHIN SLA / AT RISK / STALE — vs. DOMAIN CONTEXT threshold] |
| INCUMBENT BASELINE ref | [F-01 / F-02 / none — cite if Error handling = NONE or loss analog exists] |

The `Citing`, `Elapsed (cumulative)`, and `F-02 status` rows are required in
every BOUNDARY CHECK table. The `Elapsed (cumulative)` value must be computed
here, incrementally — it may not be deferred to a post-stage section. A
BOUNDARY CHECK table that omits this row, or that references a post-stage
summary for this value, is non-compliant.

---

## Stale Analysis

After the final BOUNDARY CHECK table, write this section.

| Entity | DOMAIN CONTEXT threshold | Final boundary elapsed | Delta | Status | Scenario |
|--------|--------------------------|------------------------|-------|--------|----------|
| [name] | [N unit] | [from final BOUNDARY CHECK] | [elapsed - N] | WITHIN SLA or STALE | Normal |
| [name] | [N unit] | [retry/failure-mode elapsed] | [delta] | [status] | Failure mode |

Below the table, write one closing line:
"INCUMBENT BASELINE F-02: [quote]. Pipeline failure mode elapsed: [Y].
DOMAIN CONTEXT threshold: [N]. F-02 [resolved / not resolved]."

Derive all table values from DOMAIN CONTEXT and BOUNDARY CHECK tables.
Do not assert staleness from description alone.

---

## Recovery Prescriptions

| Item | BOUNDARY CHECK NONE or loss point | Recovery prescription | INCUMBENT BASELINE ref |
|------|----------------------------------|----------------------|------------------------|
| [stage/boundary] | [condition] | [specific named mechanism] | [F-01/F-02: "[quote failure]"] or "none" |

At least one row must cite INCUMBENT BASELINE by name where the failure has an
incumbent predecessor. A prescriptions table with no incumbent references fails
the loop closure requirement.

---

## Pattern Trade-Off

| Dimension | Current pipeline | Alternative: [name] | INCUMBENT BASELINE relevance |
|-----------|-----------------|---------------------|------------------------------|
| [dimension 1 — latency or throughput] | | | [F-01/F-02 citation] or "not applicable" |
| [dimension 2 — failure mode or ops] | | | [F-01/F-02 citation] or "not applicable" |

At least one row must cite INCUMBENT BASELINE by name.

---

## Scenario

{scenario}
```

---

## Variation Summary — Round 4

| ID | Primary Axis | Secondary Axis | Key Structural Innovation vs. R3 |
|----|-------------|---------------|----------------------------------|
| V-01 | Role sequence (artifact-labeled dependency chain) | — | Machine-readable ARTIFACT: headers; IMMUTABLE THRESHOLD block with scope names; F-analog field in stage blocks closes C-16 at stage level |
| V-02 | Phrasing register (numbered specification requirements) | — | Requirement IDs as citation tokens; C-17 as separate prohibition requirement (R-04) distinct from declaration (R-03); C-18 as format requirement (R-08) plus deferral prohibition (R-09) |
| V-03 | Inertia framing (incumbent-as-structural-anchor) | — | Completes R3 V-03 (no prompt body was generated in R3); LOCK block in DOMAIN CONTEXT; F-02 status field in every BOUNDARY CHECK as live freshness verdict |
| V-04 | Lifecycle emphasis (phase gates) | Role sequence (Finance-first) | Phase gates as mandatory output checklists; C-17 enforced in gate itself plus DOMAIN CONTEXT; Phase 2 gate checks per-boundary elapsed before Phase 3 begins |
| V-05 | Output format (table-primary with named-section fix) | Explicit C-16/C-17/C-18 table fields | Fixes R3 V-02 C-10/C-15 failure: named section headers wrap tables; `Citing:` row enforces C-16; `LOCK` row enforces C-17; `Elapsed (cumulative)` row with deferral prohibition enforces C-18 |
