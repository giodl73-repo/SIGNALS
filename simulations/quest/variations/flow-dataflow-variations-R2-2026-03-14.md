Written to `simulations/quest/variations/flow-dataflow-variations-R2-2026-03-14.md`.

---

## Round 2 Variations — flow-dataflow

**Axes used in R1:** Output format, Role sequence, Lifecycle emphasis
**Axes explored in R2:** Phrasing register, Inertia framing, State machine (deeper lifecycle variant)

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Phrasing register | STOP/WRITE/PROCEED imperative commands replace declarative `[GATE: ...]` instructions — same structure as R1-V-05, different instruction register |
| **V-02** | Inertia framing | Manual incumbent process documented first — seeds domain vocabulary via business narrative before any formal vocabulary gate fires |
| **V-03** | Lifecycle emphasis (state machine) | Named states (LIVE / IN-FLIGHT / STAGED / PERSISTED / STALE); STATE TRANSITION replaces BOUNDARY CHECK; STALE threshold declared as a contract before tracing begins |
| **V-04** | Phrasing register + Inertia framing | Imperative checkpoint commands + incumbent-first narrative |
| **V-05** | All three | Incumbent narrative + state machine transitions + STOP commands |

---

**Key design decisions:**

**C-11 skip-resistance ranking:** V-05 > V-03 > V-01/V-04 > V-02 ≈ R1-V-05. The state machine (V-03/V-05) is structurally harder to batch because each stage declares an exit-state that feeds the next transition as input. STOP commands (V-01/V-04) add a behavioral constraint on top.

**C-10 richness ranking:** V-05 > V-02/V-04 > V-03 > V-01 ≈ R1-V-05. Incumbent narrative seeds vocabulary from a business story before the template lock — entity names appear in a problem description, not just as filled blanks.

**New C-08 surface (V-03/V-05):** The "State-machine fit" column requires each recovery prescription to be anchored to a state contract ("prevents entity stranded IN-FLIGHT"), not just a gap description. This is a richer C-08 signal.

**C-06 mechanism change (V-03/V-05):** STALE is a named state with a threshold contract declared in PHASE 2 before any tracing begins. Normal and failure-mode staleness are derived from LIVE→PERSISTED elapsed time calculations, not synthesized from a separate section after the trace is complete.

**Open question for R3:** Does the state machine framing in V-03/V-05 produce measurably better C-06 and C-08 scores than R1-V-05? If yes, state machine becomes the new structural baseline and BOUNDARY CHECK is retired.
 Criterion coverage by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Lineage chain | stage sequence + pipeline path line | explicit LINEAGE CHAIN section | stage-state sequence + pipeline path | lineage section in PHASE 2 | stage-state sequence + pipeline path |
| C-02 Boundary error handling | BOUNDARY CHECK (STOP command) | BOUNDARY CHECK (STOP command) | STATE TRANSITION gate | BOUNDARY CHECK (STOP command) | STATE TRANSITION gate (STOP) |
| C-03 Loss points | stage block + boundary check | stage + boundary + incumbent compare | stage + state transition loss exposure | stage + boundary + incumbent compare | stage + transition + incumbent compare |
| C-04 Schema state | schema in/delta/out per stage | schema in/delta/out per stage | schema at stage entry/exit + transition delta | schema in/delta/out per stage | schema at stage entry/exit + transition delta |
| C-05 Latency | latency contribution per stage | latency contribution per stage | latency contribution + time-in-transition | latency contribution per stage | latency contribution + time-in-transition |
| C-06 Stale windows | dedicated section (normal + failure rows) | dedicated section + incumbent compare | STALE threshold contract + analysis (normal + failure) | dedicated section + incumbent compare | STALE threshold contract + incumbent compare |
| C-07 Domain framing | DOMAIN CONTEXT gate | INCUMBENT section + DOMAIN CONTEXT | DOMAIN CONTEXT gate + entity per transition | INCUMBENT + DOMAIN CONTEXT | INCUMBENT + DOMAIN CONTEXT |
| C-08 Recovery prescriptions | recovery table (no/NONE gaps) | recovery table + incumbent compare | recovery table + state-machine fit column | recovery table + incumbent compare | recovery table + state fit + incumbent compare |
| C-09 Pattern trade-off | 2-column table (current / alternative) | 3-column table (incumbent / current / alt) | state-machine framing: which states eliminated | 3-column (incumbent / current / alt) | 3-column + state-machine framing |
| C-10 Pre-trace domain gate | DOMAIN CONTEXT (STOP command) | INCUMBENT section + DOMAIN CONTEXT | DOMAIN CONTEXT + state machine contract | PHASE 1 incumbent + PHASE 2 DOMAIN CONTEXT | PHASE 1 incumbent + PHASE 2 state machine |
| C-11 Interleaved boundary gates | BOUNDARY CHECK (STOP before next stage) | BOUNDARY CHECK (STOP before next stage) | STATE TRANSITION (required before next stage) | BOUNDARY CHECK (STOP -- explicit) | STATE TRANSITION (STOP -- explicit) |
| C-12 Domain entity per boundary | "Domain entity at boundary:" line | "Domain entity at boundary:" line | "Entity:" required field in STATE TRANSITION | "Domain entity at boundary:" (STOP phrased) | "Entity:" required in STATE TRANSITION (STOP) |

---

## V-01: Phrasing Register -- Imperative Checkpoint Commands

**Axis:** Phrasing register -- every structural instruction is a second-person imperative STOP/WRITE/PROCEED command rather than a declarative format note
**Hypothesis:** Checkpoint commands ("STOP. Complete DOMAIN CONTEXT. Do not write Stage 1 until this block is done.") reduce model skip-optimism more than declarative instructions ("[GATE: complete before writing stages]"). Structural content is identical to R1-V-05; only the instruction register changes. The negative framing ("writing two consecutive stage blocks without a BOUNDARY CHECK is not permitted") adds a constraint that declarative format instructions do not express.

```
You are running /flow-dataflow.
You are a Finance / Operations / Commerce data domain expert.

STOP. Before you write a single stage block, you must complete DOMAIN CONTEXT below.
Do not write Stage 1 until DOMAIN CONTEXT is done.
Do not use "row", "record", or "item" where a domain entity name from DOMAIN CONTEXT applies.

At the end of every stage block, a BOUNDARY CHECK fires.
Complete the BOUNDARY CHECK before writing the next stage block.
Writing two consecutive stage blocks without a BOUNDARY CHECK between them is not permitted.
NONE error handling must be stated explicitly -- writing nothing is not acceptable.

---

## DOMAIN CONTEXT
STOP. Fill every field before proceeding to Stage 1.
All entity names, field names, and vocabulary established here are mandatory in every
stage block and every BOUNDARY CHECK.

Domain: [Finance / Operations / Commerce -- pick one]
Primary entity: [domain entity name -- "invoice record" / "inventory adjustment" / "order
  line" / "GL entry" / "purchase order" / "shipment event"]
Secondary entities: [other entities in scope -- list all, or "none"]
Pipeline purpose: [one sentence in domain terms -- what moves, between which systems, why]
Downstream consumer: [specific role or system and their use case]
Business cadence: [when downstream needs fresh data -- "end-of-day close" /
  "real-time order routing" / "weekly inventory reconciliation"]
Pipeline path: [source system] => [stage 2] => [stage 3...] => [destination]

PROCEED to Stage 1 only after every field above is filled.

---

## STAGE 1: SOURCE
STOP. Write this block completely before opening BOUNDARY CHECK 1->2.

Entity: [entity from DOMAIN CONTEXT -- not "record" or "data"]
Schema at source: [field: type -- use domain field names from DOMAIN CONTEXT vocabulary]
Read mechanism: [API poll / CDC / bulk extract / streaming event / file drop]
Latency contribution: [real-time / <Ns / batch-Nh / daily / polling-Nm]
Data loss risk: [specific -- "Deleted [entity] not captured -- CDC not enabled on [table]" /
  "Watermark drift: [entity] updated in last N sec before cutoff missed" --
  "errors may occur" does not qualify]

BOUNDARY CHECK 1->2: SOURCE -> [STAGE 2 NAME]
STOP. Complete all four lines before writing Stage 2.
  Error handling: [retry N attempts / dead-letter queue / circuit breaker / rollback] |
    [NONE -- no error handling at this boundary -- state explicitly]
  Schema delta: [fields added / removed / renamed / type-changed crossing this boundary,
    or "none"]
  Loss exposure: [what can be silently dropped or not replayed at this edge -- specific]
  Domain entity at boundary: [entity name from DOMAIN CONTEXT -- "data" or "records" fails]
PROCEED to Stage 2 only after all four lines are filled.

---

## STAGE 2: [STAGE NAME]
STOP. Write this block completely before opening BOUNDARY CHECK 2->3.

Entity: [entity name -- same as DOMAIN CONTEXT, or note if name changes at this stage]
Schema in: [fields and types -- must match Stage 1 output described in BOUNDARY CHECK 1->2]
Transform: [what changes -- field renames, type coercions, aggregations, enrichments,
  filtering -- in domain terms]
Schema out: [explicitly diff from schema in -- state what changed and why]
Latency contribution: [this stage's contribution to end-to-end latency]
Data loss risk: [specific -- "Rows with null [domain field] silently filtered" /
  "No idempotency key -- duplicate [entity] on retry" /
  "Records exceeding [N] bytes truncated"]

BOUNDARY CHECK 2->3: [STAGE 2] -> [STAGE 3 or DESTINATION]
STOP. Complete before writing the next stage.
  Error handling: [mechanism] | [NONE -- state explicitly]
  Schema delta: [delta or "none"]
  Loss exposure: [specific or "none -- [reason verified]"]
  Domain entity at boundary: [entity name from DOMAIN CONTEXT]

---

[Repeat: write STAGE BLOCK, then BOUNDARY CHECK, then next STAGE BLOCK.
Every consecutive stage pair must have a BOUNDARY CHECK between them.
Do not write two stage blocks in a row without a BOUNDARY CHECK. No exceptions.]

---

## STAGE [N]: DESTINATION
STOP. Write this block completely.

Entity: [entity name at destination -- from DOMAIN CONTEXT]
Schema at destination: [fields and types as written]
Write mechanism: [upsert / append / overwrite / merge / event publish]
Latency contribution: [write latency or propagation delay to downstream consumers]
Data loss risk: [dedupe failure / overwrite collision / missing idempotency key /
  constraint violation silent skip]

BOUNDARY CHECK [N-1]->[N]: [STAGE N-1] -> DESTINATION
STOP. Final boundary. Complete before proceeding to STALE DATA WINDOWS.
  Error handling: [mechanism] | [NONE -- state explicitly]
  Schema delta: [delta or "none"]
  Loss exposure: [specific or "none -- [reason verified]"]
  Domain entity at boundary: [entity name from DOMAIN CONTEXT]

---

## STALE DATA WINDOWS
STOP. Write two rows: normal-operation staleness AND failure-mode staleness.
Do not combine them. A single row covering both does not satisfy this section.

| Domain Entity | Normal staleness window | Failure-mode staleness (if [stage] fails) | Business impact on [downstream consumer] |
|---------------|------------------------|-------------------------------------------|------------------------------------------|
| [entity from DOMAIN CONTEXT] | [up to N units -- name dominant stage] | [up to N hr/days if [stage name] fails] | [consequence for [Business Cadence] cycle] |

[One row per entity with a different staleness profile. Primary entity required at minimum.]

---

## DATA LOSS INVENTORY
Aggregate every data loss risk from stage blocks and every loss exposure from boundary checks.
At least one entry per stage. Domain entity names required -- "data" or "records" does not pass.

| # | Location | Domain Entity | Loss Mechanism | Currently Recoverable? |
|---|----------|---------------|----------------|------------------------|
| 1 | [stage name or boundary N->N+1] | [entity from DOMAIN CONTEXT] | [specific mechanism] | [yes: [recovery mechanism]] / [no] |

---

## RECOVERY PRESCRIPTIONS
Required for every DATA LOSS INVENTORY row where "Currently Recoverable?" = no.
Required for every BOUNDARY CHECK where Error Handling = NONE.
"Add retry logic" does not qualify -- be specific.

| Gap reference | Prescribed mechanism | Domain rationale |
|---------------|----------------------|------------------|
| Loss #[N] / Boundary [N]->[N+1] | [idempotency key on [domain field] / replay log with
  [N-day retention] / saga compensation for [domain operation] / dead-letter queue on
  [event type] / outbox pattern on [table] / schema registry at [boundary]] | [one sentence:
  why this mechanism fits this domain operation and this specific gap] |

---

## PATTERN TRADE-OFF
Current pattern: [name -- ETL / sync / CDX / dual-write -- from pipeline path]
Alternative: [one specific named alternative -- e.g., event-sourced CDC instead of batch ETL]

| Dimension | Current ([pattern]) | Alternative ([pattern]) |
|-----------|---------------------|------------------------|
| Consistency | [consistency model -- eventual / strong / bounded staleness] | [consistency model] |
| Latency | [end-to-end from stage latencies vs Business Cadence tolerance] | [estimated for alternative] |
| Operational cost for [domain] | [specific: reconciliation runs, audit overhead, replay ops,
  CDC licensing] | [specific for alternative] |

---

Write artifact: simulations/flow/dataflow/{topic}-dataflow-{date}.md
Frontmatter: skill, topic, date, domain, primary_entity, pattern, stage_count,
boundary_count, none_handling_boundaries, loss_points_found.
```

---

## V-02: Inertia Framing -- Manual Incumbent First

**Axis:** Inertia framing -- before the automated pipeline trace, a mandatory INCUMBENT PROCESS section documents the manual/legacy method and its failure modes in domain terms
**Hypothesis:** Describing what analysts do without the pipeline forces domain entity names into context before any formal vocabulary gate fires, achieving C-10 via business narrative rather than a template instruction. Incumbent failure modes prime the C-03 loss point vocabulary -- the model frames automated pipeline losses against failures it has already named. The pattern trade-off section gains a third column (incumbent vs current vs alternative) that quantifies the improvement rather than comparing two abstractions.

```
You are running /flow-dataflow.
You are a Finance / Operations / Commerce data domain expert.

Before tracing the automated pipeline, document the manual incumbent -- the process
that exists without automation. This surfaces the domain vocabulary and the failure
modes that the automated pipeline was designed to solve.

All entity names established in INCUMBENT PROCESS and DOMAIN CONTEXT must propagate
through every stage trace, boundary check, and stale window entry.
Do not use "row", "record", or "item" where a domain entity name applies.
A BOUNDARY CHECK fires after every stage block and must be completed before the
next stage opens. NONE error handling must be stated explicitly.

---

## INCUMBENT PROCESS (Manual / Legacy)
[Complete before tracing the automated pipeline.]

Domain: [Finance / Operations / Commerce]
Primary entity: [domain entity name -- what this process handles]
Current manual process: [how this is done without the automated pipeline -- "Analysts export
  [entity] from ERP to Excel nightly, then upload to BI tool manually.
  Deletions are not captured. [entity] is reconciled monthly."]
Incumbent failure modes:
  - Freshness failure: [what goes stale, how stale, how often -- "invoice records are up to
    24h stale; end-of-month close uses prior-day AR balances"]
  - Loss failure: [what gets missed or corrupted -- "deleted invoices persist as phantom
    balances for up to N days after deletion in ERP"]
  - Schema drift failure: [when upstream changes fields, what breaks -- "[VendorId] renamed
    in ERP v12 upgrade; Excel formula returns null for 3 weeks before detection"]
  - Recovery failure: [how failures are discovered and fixed -- "finance analyst catches at
    month close; remediation requires full re-extract -- 4 hours manual effort per incident"]
Business cost of incumbent: [reconciliation hours / audit findings / SLA violations /
  customer escalations -- quantify or characterize]

[The automated pipeline replaces or augments this incumbent. Its trade-offs are legible
against the failure modes above.]

---

## DOMAIN CONTEXT
[Lock vocabulary. All names here must appear verbatim in stage trace, boundary checks,
and stale analysis. Complete before writing Stage 1.]

Primary entity: [entity name -- must match INCUMBENT PROCESS -- do not rename here]
Secondary entities: [other entities in scope, or "none"]
Pipeline purpose: [one sentence -- specifically state which INCUMBENT failure mode this
  pipeline addresses: "Replace manual [entity] export to eliminate [failure mode]"]
Downstream consumer: [specific role or system -- same consumer the incumbent served]
Business cadence: [when downstream needs fresh data -- replaces the manual cadence above]
Pipeline path: [source system] => [stage 2] => ... => [destination]

---

## DATA LINEAGE CHAIN
[Unbroken chain for each entity. Use names from DOMAIN CONTEXT throughout.]

[Primary entity]: [source system] => [Stage 1: describe in domain terms] => [Stage 2] =>
  ... => [Destination system]
[Secondary entity]: [chain, or "not in scope -- [reason]"]

[No entity named in DOMAIN CONTEXT may be omitted without an explicit "not in scope" note.]

---

## STAGE 1: SOURCE

Entity: [entity from DOMAIN CONTEXT]
Schema at source: [field: type -- use domain field names: "InvoiceDate: date",
  "VendorId: varchar(10)"]
Read mechanism: [API poll / CDC / bulk extract / streaming event / file drop]
Latency contribution: [real-time / <Ns / batch-Nh / daily]
Data loss risk: [specific -- compare to INCUMBENT: "CDC captures deletions that manual
  process missed" OR "Same watermark gap as incumbent -- not yet solved at source"]

### BOUNDARY CHECK 1->2: [STAGE 1] -> [STAGE 2]
Error handling: [mechanism] | [NONE -- explicit; does NONE reproduce an INCUMBENT
  recovery failure?]
Schema delta: [fields added / removed / renamed / type-changed, or "none"]
Loss exposure: [specific -- note if this reproduces an INCUMBENT failure mode]
Domain entity at boundary: [entity name from DOMAIN CONTEXT]

---

## STAGE 2: [STAGE NAME]

Entity: [entity name -- from DOMAIN CONTEXT; note if name changes at this stage]
Schema in: [fields and types -- must match Stage 1 output from BOUNDARY CHECK 1->2]
Transform: [what changes -- in domain terms: "InvoiceDate normalized to UTC for
  cross-region AR reporting", "TaxAmount rounded per Finance rounding policy"]
Schema out: [diff from schema in -- explicitly state what changed]
Latency contribution: [this stage]
Data loss risk: [specific -- note if new failure mode introduced by automation, or
  inherited from incumbent]

### BOUNDARY CHECK 2->3: [STAGE 2] -> [STAGE 3 or DESTINATION]
Error handling: [mechanism] | [NONE]
Schema delta: [delta or "none"]
Loss exposure: [specific]
Domain entity at boundary: [entity name from DOMAIN CONTEXT]

---

[Repeat STAGE + BOUNDARY CHECK for every intermediate stage.
Every stage block must be followed by its BOUNDARY CHECK before the next stage opens.]

---

## STAGE [N]: DESTINATION

Entity: [entity name at destination -- from DOMAIN CONTEXT]
Schema at destination: [fields and types as written]
Write mechanism: [upsert / append / overwrite / merge / event publish]
Latency contribution: [write latency or propagation delay]
Data loss risk: [dedupe failure / overwrite collision / constraint violation silent skip]

### BOUNDARY CHECK [N-1]->[N]: [STAGE N-1] -> DESTINATION
Error handling: [mechanism] | [NONE]
Schema delta: [delta or "none"]
Loss exposure: [specific]
Domain entity at boundary: [entity name from DOMAIN CONTEXT]

---

## STALE DATA WINDOWS
[Relate to INCUMBENT PROCESS cadence. Two rows required: normal-operation and failure-mode.
Do not combine. Compare to incumbent staleness.]

| Domain Entity | Normal staleness | Failure-mode staleness (if [stage] fails) | vs Incumbent | Impact on [downstream consumer] |
|---------------|-----------------|-------------------------------------------|--------------|----------------------------------|
| [entity from DOMAIN CONTEXT] | [up to N units -- dominant stage] | [up to N hr/days if [stage] fails] | [better by N hrs / same / worse] | [consequence for [Business Cadence]] |

---

## DATA LOSS INVENTORY
[Aggregate from all stage blocks and boundary checks.
Compare each entry to INCUMBENT failure modes. At least one entry per stage.]

| # | Location | Domain Entity | Loss Mechanism | vs Incumbent | Currently Recoverable? |
|---|----------|---------------|----------------|--------------|------------------------|
| 1 | [stage or boundary N->N+1] | [entity from DOMAIN CONTEXT] | [specific mechanism] | [new / inherited from incumbent: "[failure mode name]" / improved over incumbent] | [yes: [recovery mechanism] / no] |

---

## RECOVERY PRESCRIPTIONS
[For every "Currently Recoverable?" = no and every NONE boundary.
Where the incumbent had no recovery either, note whether the prescription also closes
the incumbent gap.]

| Gap reference | Prescribed mechanism | Domain rationale | Closes incumbent gap? |
|---------------|----------------------|------------------|----------------------|
| Loss #[N] / Boundary [N]->[N+1] | [idempotency key on [domain field] / replay log /
  saga compensation for [domain operation] / dead-letter queue on [event type] /
  outbox pattern on [table] / schema registry at [boundary]] | [one sentence] | [yes: closes
  "[INCUMBENT failure mode name]" / no: new gap introduced by automation] |

---

## PATTERN TRADE-OFF
Current automated pattern: [name -- ETL / sync / CDX / dual-write]
Alternative: [one specific alternative]

[Three-column comparison: incumbent as baseline -- quantifies improvement over manual process.]

| Dimension | Incumbent (manual) | Current ([pattern]) | Alternative ([pattern]) |
|-----------|-------------------|---------------------|------------------------|
| Freshness | [from INCUMBENT freshness failure] | [from stage latencies] | [estimated for alternative] |
| Consistency | [manual -- analyst-dependent; failure mode from INCUMBENT] | [consistency model] | [consistency model] |
| Operational cost for [domain] | [from INCUMBENT business cost above] | [reconciliation,
  monitoring, replay overhead] | [better / worse than current -- estimate] |

---

Write artifact: simulations/flow/dataflow/{topic}-dataflow-{date}.md
Frontmatter: skill, topic, date, domain, primary_entity, pattern, stage_count,
none_handling_boundaries, loss_points_found, incumbent_failure_modes_addressed.
```

---

## V-03: Lifecycle Emphasis -- Data State Machine

**Axis:** Lifecycle emphasis -- each stage is associated with a named data state (LIVE / IN-FLIGHT / STAGED / PERSISTED / STALE); STATE TRANSITION blocks replace BOUNDARY CHECK blocks between stages
**Hypothesis:** A state machine trace provides an alternative structural mechanism for C-11: the STATE TRANSITION is a required declaration of what happens to the entity as it moves between states, making batch-writing architecturally awkward because each stage has an explicit exit-state that feeds into the next transition. The STALE named state forces C-06 to emerge from an explicit threshold contract declared before tracing begins, not synthesized post-hoc. Recovery prescriptions (C-08) gain a "state-machine fit" column that frames each prescription as a state contract (rollback to IN-FLIGHT / replay from STAGED), producing more precise recovery guidance.

```
You are running /flow-dataflow.
You are a Finance / Operations / Commerce data domain expert tracing data through
a state machine.

Every data item has a named state at all times. Stages transform data; state transitions
happen at boundaries between stages. A STATE TRANSITION block must appear between every
consecutive stage pair. Do not write the next stage until its STATE TRANSITION is complete.
NONE error handling must be stated explicitly at every transition.

State vocabulary (use exactly these labels -- no variations):
  LIVE      -- entity exists authoritatively at source, not yet captured
  IN-FLIGHT -- entity is captured or queued, in transit, not yet committed to a store
  STAGED    -- entity has been transformed, landed in an intermediate store
  PERSISTED -- entity is written to destination, available to consumers
  CONSUMING -- entity is being read by a downstream consumer
  STALE     -- entity has not reached PERSISTED within the defined stale threshold

---

## DOMAIN CONTEXT
[Complete before writing Stage 1. Entity names and state thresholds established here
govern the entire trace.]

Domain: [Finance / Operations / Commerce]
Primary entity: [domain entity name]
Secondary entities: [other in-scope entities, or "none"]
Pipeline purpose: [one sentence in domain terms]
Downstream consumer: [specific role or system and business use case]
Business cadence: [when downstream needs fresh data -- determines when STALE is entered]
Pipeline path: [source system] => [Stage 2] => ... => [Destination system]

State machine contract:
  Initial state:   LIVE
  Target state:    PERSISTED
  Stale threshold: [primary entity] enters STALE if PERSISTED is not reached within
    [N sec / min / hr / days -- derive from Business Cadence above]
  [Secondary entity stale threshold, if different]: [N units]

---

## STATE MACHINE TRACE

### STAGE 1: SOURCE
Entity state entering: LIVE
Entity: [entity name from DOMAIN CONTEXT]
Schema at source: [field: type -- use domain field names]
Read mechanism: [API poll / CDC / bulk extract / streaming event / file drop]
Latency contribution: [real-time / <Ns / batch-Nh / daily]
Data loss risk: [specific -- what can be lost while entity is in LIVE state at source:
  "Deleted [entity] not captured -- CDC not enabled on [table]" /
  "Entity updated after batch cutoff missed until next window"]
Entity state exiting: IN-FLIGHT

### STATE TRANSITION 1->2: LIVE -> IN-FLIGHT -> [next state]
Entity: [entity name from DOMAIN CONTEXT -- not "data" or "records"]
Trigger: [what event moves entity from Stage 1 to Stage 2 -- API call / batch schedule /
  stream event / file handoff]
Error handling: [retry N attempts / dead-letter queue / rollback to LIVE / circuit breaker] |
  [NONE -- entity can be lost without recovery; estimate how many entities per window]
Schema delta: [fields added / removed / renamed / type-changed at this transition, or "none"]
Loss exposure: [what happens if transition fails -- silently dropped / stuck IN-FLIGHT /
  reverted to LIVE / partially written]
Time-in-flight window: [how long can entity remain IN-FLIGHT before STALE threshold is breached]

---

### STAGE 2: [STAGE NAME]
Entity state entering: [IN-FLIGHT / STAGED -- from prior STATE TRANSITION]
Entity: [entity name]
Schema in: [fields and types -- must match STATE TRANSITION 1->2 schema delta]
Transform: [what changes -- in domain terms]
Schema out: [diff from schema in -- explicit]
Latency contribution: [this stage's contribution to LIVE->PERSISTED elapsed time]
Data loss risk: [specific -- "null [domain field] rows filtered without DLQ" /
  "idempotency not enforced -- duplicate [entity] on retry"]
Entity state exiting: [STAGED / PERSISTED -- which state does this stage produce?]

### STATE TRANSITION 2->3: [FROM_STATE] -> [TO_STATE]
Entity: [entity name from DOMAIN CONTEXT]
Trigger: [event or mechanism that moves entity to next stage]
Error handling: [mechanism] | [NONE]
Schema delta: [delta or "none"]
Loss exposure: [specific]
Time-in-transition: [latency of this transition -- adds to LIVE->PERSISTED elapsed time]

---

[Repeat STAGE + STATE TRANSITION for every intermediate stage.
Every stage must be followed by its state transition before the next stage is written.
No two consecutive stage blocks without a STATE TRANSITION between them.]

---

### STAGE [N]: DESTINATION
Entity state entering: [FROM_STATE -- from prior STATE TRANSITION]
Entity: [entity name at destination -- from DOMAIN CONTEXT]
Schema at destination: [fields and types as written to destination]
Write mechanism: [upsert / append / overwrite / merge / event publish]
Latency contribution: [write latency or propagation delay to CONSUMING state]
Data loss risk: [dedupe failure / overwrite collision / missing idempotency / constraint skip]
Entity state exiting: PERSISTED (-> CONSUMING when downstream reads)

### STATE TRANSITION [N-1]->[N]: [FROM_STATE] -> PERSISTED
Entity: [entity name]
Trigger: [what commits entity to destination]
Error handling: [mechanism] | [NONE]
Schema delta: [delta or "none"]
Loss exposure: [specific]

---

## STALE STATE ANALYSIS
[Synthesize from all stage latency contributions and time-in-transition values.
Check against the stale threshold from DOMAIN CONTEXT.
Two rows required: normal operation and failure mode.]

Normal (LIVE -> PERSISTED under normal operation):
  Elapsed time: [sum of stage latencies + transition times -- break down by stage/transition]
  Dominant bottleneck: [stage or transition name -- largest contributor]
  vs STALE threshold: [elapsed time vs threshold -- state margin: "N min below threshold" /
    "threshold already breached under normal operation -- pipeline is latency-deficient"]
  Consumer impact: [what [downstream consumer] experiences during [Business Cadence]]

Failure (LIVE -> PERSISTED when [stage name] fails or delays N-fold):
  New elapsed: [N hr/days -- which stage/transition becomes the bottleneck?]
  Entity enters STALE: [at T + N units after source change]
  Consumer impact: [what [downstream consumer] experiences when entity is STALE during
    [Business Cadence] cycle -- specific business consequence]

---

## DATA LOSS INVENTORY
[Aggregate from every STAGE block "Data loss risk" and every STATE TRANSITION
"Loss exposure". At least one entry per stage. Domain entity names required.]

| # | Location | Domain Entity | State at Loss | Loss Mechanism | Currently Recoverable? |
|---|----------|---------------|---------------|----------------|------------------------|
| 1 | [stage or transition N->N+1] | [entity from DOMAIN CONTEXT] | [LIVE / IN-FLIGHT / STAGED] | [specific mechanism] | [yes: [recovery mechanism] / no] |

---

## RECOVERY PRESCRIPTIONS
[For every DATA LOSS INVENTORY row where "Currently Recoverable?" = no,
and for every STATE TRANSITION where Error Handling = NONE.
"Add retry logic" does not qualify. Include state-machine fit.]

| Gap | Prescribed mechanism | Domain rationale | State-machine fit |
|-----|----------------------|------------------|-------------------|
| Loss #[N] / Transition [N]->[N+1] | [idempotency key on [domain field] / replay log
  with [N-day retention] / saga compensation for [domain operation] / dead-letter queue
  on [event type] / outbox pattern on [table] / state checkpoint at [transition]] |
  [one sentence] | [which state does this protect -- "prevents entity stranded IN-FLIGHT" /
  "enables replay from STAGED without re-extracting LIVE"] |

---

## PATTERN TRADE-OFF
Current pattern: [name -- ETL / sync / CDX / dual-write]
Alternative: [one specific alternative]
[Frame trade-offs in terms of the state machine: which states are eliminated, shortened,
or made more recoverable by the alternative?]

| Dimension | Current ([pattern]) | Alternative ([pattern]) |
|-----------|---------------------|------------------------|
| Consistency | [which states are guaranteed consistent -- "PERSISTED is eventually
  consistent; STAGED may be stale for up to N min"] | [which states are guaranteed
  under the alternative] |
| Latency (LIVE->PERSISTED) | [end-to-end from STALE STATE ANALYSIS vs threshold] | [which
  stages or transitions are eliminated or shortened -- quantify or qualify] |
| Operational cost for [domain] | [cost of managing IN-FLIGHT and STALE states in current
  pattern -- DLQ ops, reconciliation, replay cost] | [state-management cost for alternative] |

---

Write artifact: simulations/flow/dataflow/{topic}-dataflow-{date}.md
Frontmatter: skill, topic, date, domain, primary_entity, pattern, stage_count,
state_transitions, none_handling_transitions, loss_points_found.
```

---

## V-04: Phrasing Register + Inertia Framing

**Axes:** Phrasing register (imperative STOP/PROCEED checkpoint commands) + Inertia framing (manual incumbent first)
**Hypothesis:** The combination anchors domain vocabulary through business narrative (incumbent section) before any formal gate fires, then enforces structural compliance through STOP commands. The incumbent section provides natural C-07/C-10 vocabulary seeding from a non-template source; the STOP commands prevent post-hoc boundary summarization (C-11). Tests whether narrative-first + command-enforcement is a more reliable path to golden than R1-V-05's structure-first approach for models that are susceptible to declarative-gate skipping.

```
You are running /flow-dataflow.
You are a Finance / Operations / Commerce data domain expert.

STOP. You will complete this skill in three phases:
PHASE 1: Document the manual incumbent. STOP -- do not proceed until PHASE 1 is done.
PHASE 2: Lock domain vocabulary. STOP -- do not proceed until PHASE 2 is done.
PHASE 3: Trace the automated pipeline. A BOUNDARY CHECK fires between every stage pair.
  Do not write two consecutive stage blocks without a BOUNDARY CHECK between them.

Do not use "row", "record", or "item" where a domain entity name applies.
NONE error handling must be stated explicitly -- writing nothing is not acceptable.

---

## PHASE 1: INCUMBENT PROCESS
STOP. Complete all fields before proceeding to PHASE 2.

Domain: [Finance / Operations / Commerce]
Primary entity: [domain entity name -- the thing this process handles]
What analysts do today: [one sentence -- the manual or legacy process in domain terms:
  "Analysts export [entity] from ERP to Excel nightly, then upload to BI tool manually"]
Incumbent failure modes:
  - Freshness failure: [what goes stale and how stale -- "invoice records are 24h stale at
    the time finance closes AR aging; same-day transactions not reflected"]
  - Loss failure: [what gets missed -- "CDC not enabled; deleted [entity] persist as phantom
    balances until monthly reconciliation"]
  - Recovery failure: [how failures are discovered and fixed -- "finance analyst catches at
    month close; remediation requires full re-extract -- 4 hours manual effort per incident"]
Business cost: [reconciliation hours / audit findings / SLA violations -- quantify or
  characterize]

PROCEED to PHASE 2 only after all fields above are filled.

---

## PHASE 2: DOMAIN CONTEXT
STOP. Lock vocabulary. All entity names established here are mandatory in every stage block,
boundary check, stale analysis, and recovery prescription. Complete before PHASE 3.

Primary entity: [entity name -- must match PHASE 1 -- do not rename]
Secondary entities: [other in-scope entities, or "none"]
Pipeline purpose: [one sentence -- specifically: which PHASE 1 failure mode does this pipeline
  address? "Replace manual [entity] export to solve [failure mode]"]
Downstream consumer: [specific role or system -- same consumer the incumbent served]
Business cadence: [when downstream needs fresh data -- replaces the manual cadence above]
Pipeline path: [source] => [stage 2] => ... => [destination]

PROCEED to PHASE 3 only after all fields above are filled.

---

## PHASE 3: PIPELINE TRACE

STOP. Follow the gated protocol: write Stage 1, then BOUNDARY CHECK, then Stage 2.
Do not batch all stage blocks first and then write boundary checks. Interleave them.

---

## STAGE 1: SOURCE
STOP. Write this block completely before opening BOUNDARY CHECK 1->2.

Entity: [entity from PHASE 2 -- not "record" or "data"]
Schema at source: [field: type -- domain field names: "InvoiceDate: date",
  "VendorId: varchar(10)"]
Read mechanism: [API poll / CDC / bulk extract / streaming event / file drop]
Latency contribution: [real-time / <Ns / batch-Nh / daily]
Data loss risk: [specific -- compare to PHASE 1: "CDC captures deletions that incumbent
  missed" / "Same watermark gap as incumbent -- not yet solved at source"]

BOUNDARY CHECK 1->2: SOURCE -> [STAGE 2 NAME]
STOP. Complete all four lines. Do not write Stage 2 until this check is done.
  Error handling: [retry N attempts / dead-letter / circuit breaker / rollback] |
    [NONE -- state explicitly; does NONE reproduce a PHASE 1 recovery failure?]
  Schema delta: [fields added / removed / renamed / type-changed, or "none"]
  Loss exposure: [specific -- does this reproduce a PHASE 1 loss failure?]
  Domain entity at boundary: [entity name from PHASE 2 -- "data" or "records" does not pass]
PROCEED to Stage 2.

---

## STAGE 2: [STAGE NAME]
STOP. Write completely before opening BOUNDARY CHECK 2->3.

Entity: [entity name -- from PHASE 2]
Schema in: [must match Stage 1 output as described in BOUNDARY CHECK 1->2]
Transform: [what changes -- in domain terms]
Schema out: [diff from schema in -- explicit]
Latency contribution: [this stage]
Data loss risk: [specific -- new automation-introduced failure, or inherited from PHASE 1?]

BOUNDARY CHECK 2->3: [STAGE 2] -> [STAGE 3 or DESTINATION]
STOP. Complete before writing next stage.
  Error handling: [mechanism] | [NONE]
  Schema delta: [delta or "none"]
  Loss exposure: [specific]
  Domain entity at boundary: [entity name from PHASE 2]

---

[Repeat: STAGE BLOCK then BOUNDARY CHECK then next STAGE BLOCK.
No consecutive stage blocks without a BOUNDARY CHECK. No exceptions.]

---

## STAGE [N]: DESTINATION
STOP. Write completely.

Entity: [entity at destination -- from PHASE 2]
Schema at destination: [fields and types]
Write mechanism: [upsert / append / overwrite / merge / event publish]
Latency contribution: [write latency]
Data loss risk: [specific]

BOUNDARY CHECK [N-1]->[N]: [STAGE N-1] -> DESTINATION
STOP. Final boundary. Complete before STALE DATA WINDOWS.
  Error handling: [mechanism] | [NONE]
  Schema delta: [delta or "none"]
  Loss exposure: [specific]
  Domain entity at boundary: [entity name from PHASE 2]

---

## STALE DATA WINDOWS
STOP. Two rows required: normal-operation AND failure-mode. Do not combine.
Compare to PHASE 1 incumbent staleness.

| Domain Entity | Normal staleness | Failure-mode staleness | vs Incumbent (PHASE 1) | Impact on [downstream consumer] |
|---------------|-----------------|------------------------|------------------------|----------------------------------|
| [entity from PHASE 2] | [up to N units -- dominant stage] | [up to N hr/days if [stage] fails] | [better by N hrs / same / worse] | [consequence for [Business Cadence]] |

---

## DATA LOSS INVENTORY
Aggregate every loss risk from stage blocks and every loss exposure from boundary checks.
At least one entry per stage. Compare to PHASE 1 failure modes.

| # | Location | Domain Entity | Loss Mechanism | vs Incumbent (PHASE 1) | Currently Recoverable? |
|---|----------|---------------|----------------|------------------------|------------------------|
| 1 | [stage or boundary N->N+1] | [entity from PHASE 2] | [specific] | [new / inherited: "[failure mode name]" / improved] | [yes: [mechanism] / no] |

---

## RECOVERY PRESCRIPTIONS
For every "Currently Recoverable?" = no and every NONE boundary.
"Add retry logic" does not qualify. Note whether prescription also closes a PHASE 1 gap.

| Gap reference | Prescribed mechanism | Domain rationale | Closes PHASE 1 gap? |
|---------------|----------------------|------------------|---------------------|
| Loss #[N] / Boundary [N]->[N+1] | [idempotency key on [domain field] / replay log /
  saga compensation / dead-letter queue on [event type] / outbox pattern on [table] /
  schema registry at [boundary]] | [one sentence] | [yes: closes "[PHASE 1 failure mode]" /
  no: new gap introduced by automation] |

---

## PATTERN TRADE-OFF
Current automated pattern: [name]
Alternative: [one specific alternative]

[Three-column: incumbent as baseline -- quantifies improvement, not abstract comparison.]

| Dimension | Incumbent (PHASE 1) | Current ([pattern]) | Alternative ([pattern]) |
|-----------|-------------------|---------------------|------------------------|
| Freshness | [from PHASE 1 freshness failure] | [from stage latencies] | [estimated] |
| Consistency | [manual -- analyst-dependent] | [consistency model] | [consistency model] |
| Operational cost for [domain] | [from PHASE 1 business cost] | [reconciliation,
  monitoring, replay overhead] | [better / worse -- estimate] |

---

Write artifact: simulations/flow/dataflow/{topic}-dataflow-{date}.md
Frontmatter: skill, topic, date, domain, primary_entity, pattern, stage_count,
none_handling_boundaries, loss_points_found, incumbent_failure_modes_addressed.
```

---

## V-05: Full Synthesis -- Phrasing Register + State Machine + Inertia Framing

**Axes:** Phrasing register (imperative STOP/PROCEED commands) + Lifecycle state machine (LIVE / IN-FLIGHT / STAGED / PERSISTED / STALE) + Inertia framing (manual incumbent first)
**Hypothesis:** Round 2 ceiling candidate. Incumbent framing seeds domain vocabulary from business narrative (deeper than a template vocabulary gate). The state machine protocol forces each boundary to be a named transition with a from-state/to-state contract, structurally harder to batch than BOUNDARY CHECK blocks. Imperative STOP commands add a behavioral constraint on top of the structural requirement. C-06 emerges from an explicit STALE threshold contract declared before tracing, not synthesized post-hoc. C-08 gains a "state-machine fit" column that anchors each recovery prescription to a state contract.

```
You are running /flow-dataflow.
You are a Finance / Operations / Commerce data domain expert.

STOP. You will complete this skill in three phases:
PHASE 1: Document the manual incumbent and lock domain vocabulary.
PHASE 2: Set up the data state machine -- states, entities, stale threshold.
PHASE 3: Trace the automated pipeline using STATE TRANSITIONS between every stage pair.

STOP at each phase gate. Do not proceed until the current phase is complete.
Do not write two consecutive stage blocks without a STATE TRANSITION between them.
Do not use "row", "record", or "item" where a domain entity name applies.
NONE error handling must be stated explicitly at every STATE TRANSITION.

---

## PHASE 1: INCUMBENT + DOMAIN CONTEXT
STOP. Complete all fields before proceeding to PHASE 2.

Domain: [Finance / Operations / Commerce]
Primary entity: [domain entity name -- the thing this process handles]
Manual incumbent: [one sentence -- what analysts do without the automated pipeline:
  "Analysts export [entity] from ERP to Excel nightly; deletions not captured; manual
  upload to BI tool; [entity] reconciled at month close"]
Incumbent failures:
  - Freshness: [what goes stale and how stale -- specific]
  - Loss: [what gets missed or corrupted -- specific]
  - Recovery: [how failures are discovered and fixed -- effort and time]
Business cost of incumbent: [reconciliation hours / audit findings / SLA violations]
Pipeline purpose: [one sentence -- which incumbent failure does this pipeline address?]
Downstream consumer: [specific role or system and use case]
Business cadence: [when downstream needs fresh data -- replaces the manual cadence]
Pipeline path: [source system] => [stage 2] => ... => [destination]

PROCEED to PHASE 2 only after all fields are filled.

---

## PHASE 2: STATE MACHINE SETUP
STOP. Define the state contracts before tracing begins. Complete before PHASE 3.

State vocabulary for this pipeline:
  LIVE       -- [entity name] exists authoritatively at source, not yet captured
  IN-FLIGHT  -- [entity name] is captured or queued, in transit, not yet committed
  STAGED     -- [entity name] has passed transformation, in intermediate store
  PERSISTED  -- [entity name] is written to destination, available to [downstream consumer]
  CONSUMING  -- [entity name] is being read by [downstream consumer]
  STALE      -- [entity name] has not reached PERSISTED within the stale threshold

State machine contract:
  Initial state:   LIVE
  Target state:    PERSISTED
  Stale threshold: [entity name] enters STALE if PERSISTED not reached within
    [N sec / min / hr / days -- derive from Business Cadence]
  Incumbent stale window: [from PHASE 1 -- the threshold this replaces]
  [Secondary entity stale threshold, if different]: [N units]

PROCEED to PHASE 3 only after state contract is complete.

---

## PHASE 3: PIPELINE TRACE

STOP. Follow the gated state machine protocol. Write STAGE 1, then STATE TRANSITION 1->2,
then STAGE 2. Do not batch stage blocks. Interleave. No two consecutive stage blocks
without a STATE TRANSITION between them. No exceptions.

---

### STAGE 1: SOURCE -- state: LIVE -> IN-FLIGHT
STOP. Write this block completely before opening STATE TRANSITION 1->2.

Entity: [entity from PHASE 1/PHASE 2 -- not "record" or "data"]
Schema at source: [field: type -- domain field names from PHASE 1 vocabulary:
  "InvoiceDate: date", "VendorId: varchar(10)"]
Read mechanism: [API poll / CDC / bulk extract / streaming event / file drop]
Latency contribution: [real-time / <Ns / batch-Nh / daily]
Data loss risk: [specific -- compare to PHASE 1: "CDC captures deletions that incumbent
  missed" / "Watermark gap inherited from incumbent -- not yet solved at source"]
Entity state exiting: IN-FLIGHT

### STATE TRANSITION 1->2: IN-FLIGHT -> [STAGED / PERSISTED]
STOP. Complete all fields before writing STAGE 2.
Entity: [entity name from PHASE 1 -- not "data" or "records"]
Trigger: [what event moves entity to next stage -- API call / batch schedule / stream event]
Error handling: [retry N attempts / dead-letter queue / rollback to LIVE / circuit breaker] |
  [NONE -- entity lost without recovery; estimate how many per window; does this reproduce
  a PHASE 1 recovery failure?]
Schema delta: [fields added / removed / renamed / type-changed at this transition, or "none"]
Loss exposure: [specific -- if lost here: PHASE 1 failure reproduced, or new failure?]
Time-in-flight window: [how long can entity stay IN-FLIGHT before STALE threshold is breached]
PROCEED to Stage 2.

---

### STAGE 2: [STAGE NAME] -- state: [IN-FLIGHT / STAGED]
STOP. Write completely before opening STATE TRANSITION 2->3.

Entity state entering: [IN-FLIGHT / STAGED -- from STATE TRANSITION 1->2]
Entity: [entity name from PHASE 1]
Schema in: [must match STATE TRANSITION 1->2 schema delta]
Transform: [what changes -- in domain terms]
Schema out: [diff from schema in -- explicit]
Latency contribution: [this stage's addition to LIVE->PERSISTED elapsed time]
Data loss risk: [specific -- new automation failure, or inherited from PHASE 1?]
Entity state exiting: [STAGED / PERSISTED]

### STATE TRANSITION 2->3: [FROM_STATE] -> [TO_STATE]
STOP. Complete before writing next stage.
Entity: [entity name from PHASE 1]
Trigger: [event or mechanism]
Error handling: [mechanism] | [NONE]
Schema delta: [delta or "none"]
Loss exposure: [specific]
Time-in-transition: [latency of this transition]
PROCEED to next stage.

---

[Repeat: STAGE block then STATE TRANSITION then next STAGE block.
Every stage must have a following STATE TRANSITION before the next stage opens.
No exceptions. No batching.]

---

### STAGE [N]: DESTINATION -- state: -> PERSISTED
STOP. Write completely.

Entity state entering: [FROM_STATE -- from prior STATE TRANSITION]
Entity: [entity at destination -- from PHASE 1]
Schema at destination: [fields and types as written]
Write mechanism: [upsert / append / overwrite / merge / event publish]
Latency contribution: [write latency or propagation delay]
Data loss risk: [dedupe failure / overwrite collision / constraint violation silent skip]
Entity state exiting: PERSISTED

### STATE TRANSITION [N-1]->[N]: [FROM_STATE] -> PERSISTED
STOP. Final transition. Complete before STALE STATE ANALYSIS.
Entity: [entity name from PHASE 1]
Trigger: [what commits entity to destination]
Error handling: [mechanism] | [NONE]
Schema delta: [delta or "none"]
Loss exposure: [specific]

---

## STALE STATE ANALYSIS
STOP. Two entries required: normal operation AND failure mode. Do not combine.
Compare against PHASE 1 incumbent staleness.

Normal (LIVE -> PERSISTED under normal operation):
  Elapsed time: [sum of stage latencies + transition times -- break down by component]
  Dominant bottleneck: [stage or transition name]
  vs STALE threshold: [elapsed vs threshold -- "N min margin" or "threshold breached:
    pipeline is latency-deficient under normal operation"]
  vs Incumbent: [faster by N hr / same / slower -- from PHASE 1 freshness failure]
  Consumer impact (normal): [what [downstream consumer] experiences for [Business Cadence]]

Failure (LIVE -> PERSISTED when [stage name] fails or delays N-fold):
  New elapsed: [N hr/days]
  Entity enters STALE: [at T + N units after source change]
  vs Incumbent failure: [better / same / worse than PHASE 1 staleness failure?]
  Consumer impact (failure): [specific consequence for [downstream consumer] during
    [Business Cadence] cycle]

---

## DATA LOSS INVENTORY
Aggregate every "Data loss risk" from stage blocks and every "Loss exposure" from state
transitions. At least one entry per stage. Domain entity names required.

| # | Location | Domain Entity | State at Loss | Loss Mechanism | vs Incumbent (PHASE 1) | Currently Recoverable? |
|---|----------|---------------|---------------|----------------|------------------------|------------------------|
| 1 | [stage or transition N->N+1] | [entity from PHASE 1] | [LIVE / IN-FLIGHT / STAGED] | [specific] | [new / inherited: "[failure mode]" / improved] | [yes: [mechanism] / no] |

---

## RECOVERY PRESCRIPTIONS
For every "Currently Recoverable?" = no and every STATE TRANSITION where Error
Handling = NONE. "Add retry logic" does not qualify. Frame in state-machine terms.

| Gap | Prescribed mechanism | Domain rationale | State-machine fit | Closes PHASE 1 gap? |
|-----|----------------------|------------------|-------------------|---------------------|
| Loss #[N] / Transition [N]->[N+1] | [idempotency key on [domain field] / replay log with
  [N-day retention] / saga compensation for [domain operation] / dead-letter queue on
  [event type] / outbox pattern on [table] / state checkpoint at [transition]] | [one sentence] |
  [which state does this protect: "prevents entity stranded IN-FLIGHT" / "enables replay
  from STAGED without re-extracting LIVE"] | [yes: closes "[PHASE 1 failure mode]" /
  no: new gap introduced by automation] |

---

## PATTERN TRADE-OFF
Current pattern: [name -- ETL / sync / CDX / dual-write]
Alternative: [one specific alternative]
[Three-column: incumbent as baseline. Frame in terms of the state machine: which states
does the alternative eliminate, shorten, or make more recoverable?]

| Dimension | Incumbent (PHASE 1) | Current ([pattern]) | Alternative ([pattern]) |
|-----------|-------------------|---------------------|------------------------|
| Freshness (LIVE->PERSISTED) | [from PHASE 1 staleness failure] | [from STALE STATE
  ANALYSIS] | [which stages or transitions shortened -- quantify or qualify] |
| Consistency | [manual -- analyst-dependent] | [consistency model + which states guaranteed] | [consistency model + which states differ] |
| Operational cost for [domain] | [from PHASE 1 business cost] | [IN-FLIGHT management,
  DLQ monitoring, replay cost] | [state-management cost for alternative -- better / worse?] |

---

Write artifact: simulations/flow/dataflow/{topic}-dataflow-{date}.md
Frontmatter: skill, topic, date, domain, primary_entity, pattern, stage_count,
state_transitions, none_handling_transitions, loss_points_found, incumbent_failure_modes_addressed.
```

---

## Round 2 Design Notes

### What's new in R2 vs R1

R1 ceiling (V-05) achieved 100/100 with: DOMAIN CONTEXT gate + interleaved BOUNDARY CHECK gates + domain entity per boundary + stage matrix table. The v2 rubric encoded these as C-10/C-11/C-12.

R2 keeps the structural guarantees and layers on:
1. **Imperative checkpoint phrasing** (V-01/V-04/V-05) -- tests whether STOP commands reduce skip-optimism vs declarative [GATE] instructions
2. **Incumbent-first framing** (V-02/V-04/V-05) -- tests whether domain vocabulary seeded via business narrative is more durable than a formal DOMAIN CONTEXT gate
3. **State machine transitions** (V-03/V-05) -- tests whether named states (LIVE/STALE/etc.) produce richer C-06 and C-08 than BOUNDARY CHECK + post-hoc STALE DATA synthesis

### C-11 structural guarantee comparison

| V | C-11 mechanism | Skip-resistance |
|---|---------------|-----------------|
| R1-V-05 | [GATE: complete before writing next stage] declarative | Moderate -- text instruction |
| V-01 | STOP command + "writing two consecutive blocks is not permitted" | Higher -- behavioral constraint + negative framing |
| V-02 | BOUNDARY CHECK (same structural form as R1-V-05) | Moderate |
| V-03 | STATE TRANSITION required (entity-state pair contract, exit state feeds next transition) | Higher -- structural: stage exit state is input to transition |
| V-04 | STOP command (same as V-01) | Higher |
| V-05 | STATE TRANSITION + STOP command + PROCEED gate | Highest -- structural + behavioral |

### C-10 richness comparison

| V | C-10 mechanism | Vocabulary seeding depth |
|---|---------------|--------------------------|
| R1-V-05 | DOMAIN CONTEXT template with field list | Template-forced -- model fills blanks |
| V-01 | Same as R1-V-05 | Template-forced |
| V-02 | INCUMBENT PROCESS section (narrative) + DOMAIN CONTEXT | Narrative-seeded -- entity names emerge from business story before template lock |
| V-03 | DOMAIN CONTEXT + state machine contract (threshold) | Template-forced + threshold contract |
| V-04 | INCUMBENT (narrative) + PHASE 2 DOMAIN CONTEXT | Same as V-02 -- narrative-first |
| V-05 | INCUMBENT (narrative) + state machine contract | Richest: narrative + threshold contract |

### New surfaces for C-08 (recovery prescriptions)

V-03 and V-05 add a "State-machine fit" column to recovery prescriptions. This column requires
the model to state which state the prescription protects -- "prevents entity stranded IN-FLIGHT"
/ "enables replay from STAGED without re-extracting LIVE." This anchors each recovery mechanism
to a state contract rather than a generic gap description, producing more precise C-08 coverage.

### V-golden candidate for R2

**V-05** is the direct synthesis target:
- PHASE 1 (incumbent) seeds domain vocabulary via business narrative -- richer than a template
- STATE TRANSITION gates replace BOUNDARY CHECK with a richer state-entry/exit contract -- C-11 is structural AND behavioral
- STOP commands make each gate an explicit behavioral constraint -- C-11 resistance is highest
- "Entity:" required field in every STATE TRANSITION enforces C-12 at the structurally required location
- STALE threshold declared in PHASE 2 before any stage is written -- C-06 is contractual, not synthetic
- State-machine fit column in recovery prescriptions -- C-08 is more precise

**Key open question for R3:** Does V-03/V-05 state machine framing measurably improve C-06 and C-08 scores relative to R1-V-05? If yes, state machine replaces BOUNDARY CHECK as the structural baseline going forward.
