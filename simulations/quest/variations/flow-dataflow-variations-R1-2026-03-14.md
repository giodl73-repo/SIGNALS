Written to `simulations/quest/variations/flow-dataflow-variations-R1-2026-03-14.md`.

---

## Round 1 Variations -- flow-dataflow

**Variation axes chosen:** output format (single-axis), role sequence/domain-first (single-axis), lifecycle emphasis/boundary gates (single-axis), then two combinations.

| V | Axis | Key structural mechanism |
|---|------|--------------------------|
| **V-01** | Output format | Pre-printed stage matrix table -- columns force C-01/C-04/C-05 into every row |
| **V-02** | Role sequence | DOMAIN CONTEXT gate runs before any tracing -- domain vocab locked in before stage-1 is written |
| **V-03** | Lifecycle emphasis | Gated BOUNDARY CHECK fires between every stage card -- C-02 omission becomes structurally impossible |
| **V-04** | Axes 1+2 | Stage matrix + DOMAIN CONTEXT gate -- table columns receive domain entity names |
| **V-05** | All three axes | Interleaved stage rows + BOUNDARY CHECK gates + DOMAIN CONTEXT -- maximum structural coverage |

**Key design rationale:**

- **C-02 (boundary error handling)** is the hardest essential to guarantee in prose. V-01/V-02/V-04 use separate boundary sections (moderate omission risk). V-03/V-05 use gated interleaved checks (low omission risk).
- **C-07 (domain framing)** is the recommended criterion most likely to be satisfied with generic terms. V-02/V-04/V-05 lock in entity names before any tracing via DOMAIN CONTEXT; V-01 has the highest C-07 omission risk.
- **C-04 (schema state)** is handled by the schema-in / transform-delta / schema-out column triple in V-01/V-04/V-05; by prose in/out fields in V-02/V-03.

**Predicted ceiling:** V-05. **Predicted C-02 floor:** V-01/V-02 (boundary section separate from stage trace). **Predicted C-07 floor:** V-01 (no domain framing gate).

- C-01 (lineage) and C-04 (schema) are most naturally satisfied by a table with schema-in/schema-out columns -- a prose trace can satisfy both but is easier to elide.
- C-02 (boundary error handling) is the hardest to enforce in prose; pre-printed boundary rows or gated BOUNDARY CHECK sections make omission structurally impossible.
- C-03 (loss points) is satisfied when the stage matrix has a dedicated "Data loss risk" column or the BOUNDARY CHECK forces a "Loss exposure" line.
- C-07 (domain framing) propagates more reliably when domain vocabulary is established before tracing begins (V-02 axis) vs. expected to emerge organically.
- C-06 (stale windows) requires a dedicated synthesis section because per-stage latency annotations alone do not guarantee the failure-mode staleness case is addressed.

**Predicted ceiling:** V-05 -- maximum structural coverage, no criterion left to model discretion.
**Predicted floor:** V-02 -- domain framing is correct but the output structure (prose + section headers) offers the most omission surface for C-02 and C-04.

---

## V-01: Output Format -- Stage Matrix Table

**Axis:** Output format -- pre-printed stage matrix table with one row per stage; dedicated columns for schema-in, transform delta, schema-out, latency, error handling, data loss risk
**Hypothesis:** A pre-printed table with fixed column headers structurally prevents omission of C-01 (lineage), C-04 (schema in/out and delta), C-05 (latency), and creates a surface for C-02 (error handling) and C-03 (loss risk) in every row. A model cannot satisfy "fill in all cells" while leaving schema or latency blank. Boundary annotations and stale windows require separate sections because the table captures per-stage data but not cross-boundary transitions.

```
You are running /flow-dataflow.
You are a Finance / Operations / Commerce data domain expert. Analyze the data flow described in the topic.

Fill in this structured template. All section headers and table column headers are fixed.
Do not reorder, rename, or remove any header, column, or template fragment.

---

## PIPELINE IDENTIFICATION
Pattern: [ETL / sync / CDX / dual-write -- identify which applies to this topic]
Domain: [Finance / Operations / Commerce -- identify which applies]
Scope: [One sentence: what data moves, between which systems, for what business purpose]

## STAGE MATRIX
[One row per stage. Do not merge stages. Complete every cell.
Write "NONE" in Error Handling only when you have verified no handling exists -- never as a default.
Write "none verified" in Data Loss Risk only when you have explicitly checked -- not as a default.]

| # | Stage Name | Stage Type | Domain Entity | Schema In (field: type) | Transform Delta | Schema Out (field: type) | Latency | Error Handling | Data Loss Risk |
|---|------------|------------|---------------|--------------------------|-----------------|--------------------------|---------|----------------|----------------|
| 1 | [name] | [extract / transform / load / sync / handoff] | [domain entity name] | [field: type, field: type] | [added/removed/renamed fields, type coercions, or "no change"] | [field: type, field: type] | [real-time / <Ns / batch-Nh / daily / polling-Nm] | [mechanism or NONE] | [specific: truncation / silent drop / no replay / watermark gap / etc.] |
| 2 | [name] | ... | ... | ... | ... | ... | ... | ... | ... |

[Add one row for every stage, from source read through destination write.
Minimum rows: source, at least one transform, destination.]

## BOUNDARY ANNOTATIONS
[One annotation per edge between consecutive stage matrix rows.
NONE error handling boundaries are the most important -- do not skip them.]

Boundary 1->2: [Stage 1 name] --> [Stage 2 name]
  Error handling: [repeat from stage matrix, or NONE]
  Loss exposure: [what can be silently dropped or not replayed at this edge]
  Schema delta: [field changes crossing this boundary, or "none"]
[Do not proceed past a boundary until all three lines are filled.]

Boundary 2->3: [Stage 2 name] --> [Stage 3 name]
  Error handling: [repeat or NONE]
  Loss exposure: [specific or "none -- [reason verified]"]
  Schema delta: [delta or "none"]

[Repeat for every boundary in the stage matrix.]

## STALE DATA WINDOWS
[Synthesize from stage matrix latencies. Two rows minimum per data item:
normal-operation staleness and failure-mode staleness must appear separately.]

| Domain Entity | Normal staleness window | Failure-mode staleness (if [stage] fails or delays) |
|---------------|------------------------|------------------------------------------------------|
| [entity name] | [up to N sec/min/hr under normal operation -- state why] | [up to N hr/days if [stage name] misses -- state why separately] |

[At least one entity row required. Failure-mode row must be a separate line from normal-operation row.]

## DATA LOSS INVENTORY
[Aggregate from Stage Matrix "Data Loss Risk" column and Boundary Annotations "Loss exposure" lines.
At least one entry per pipeline stage. Domain entity names required. Generic statements do not qualify.]

| # | Location | Domain Entity | Loss Mechanism | Currently Recoverable? |
|---|----------|---------------|----------------|------------------------|
| 1 | [stage name or boundary N->N+1] | [entity name] | [specific: truncation at N chars / silent drop on timeout / no replay window / no dedupe key / watermark drift] | [yes: [mechanism]] / [no] |

## RECOVERY PRESCRIPTIONS
[Required for every row in DATA LOSS INVENTORY where "Currently Recoverable?" = no,
AND for every boundary in BOUNDARY ANNOTATIONS where Error Handling = NONE.
Prescriptions must be specific -- "add retry logic" does not qualify.]

| Gap reference | Prescribed mechanism | Rationale |
|---------------|----------------------|-----------|
| Loss #[N] / Boundary [N]->[N+1] | [idempotency key on [field] / saga compensation for [operation] / replay log with [N-day retention] / schema registry for [entity] / dead-letter queue on [event type] / outbox pattern on [table]] | [one sentence: why this mechanism fits this specific gap] |

## PATTERN TRADE-OFF
Current pattern: [name from PIPELINE IDENTIFICATION]
Alternative: [name one specific alternative -- e.g., event-sourced CDC instead of batch ETL; streaming dual-write instead of nightly sync]

| Dimension | Current ([pattern name]) | Alternative ([pattern name]) |
|-----------|--------------------------|------------------------------|
| Consistency | [describe -- eventual / strong / bounded staleness] | [describe] |
| Latency | [characterize with numbers or bounds from stage matrix] | [characterize with numbers or bounds] |
| Operational cost for [domain] | [describe in domain terms: reconciliation effort, audit overhead, etc.] | [describe] |

---

Write artifact: simulations/flow/dataflow/{topic}-dataflow-{date}.md
Frontmatter: skill, topic, date, pattern, domain, stage_count, boundary_count,
none_handling_boundaries, loss_points_found.
```

---

## V-02: Role Sequence -- Domain Expert Leads

**Axis:** Role sequence -- a mandatory DOMAIN CONTEXT section establishes domain entity names and business vocabulary before any technical tracing begins; all subsequent sections must use the names defined there
**Hypothesis:** When domain framing is established as a first-class gate (C-07), the entity names defined there propagate into lineage chains, stage descriptions, schema field names, stale window statements, and recovery prescriptions. This produces richer C-07 coverage without requiring the model to retroactively introduce domain vocabulary into an already-written technical trace. Also tests whether domain-first ordering produces more accurate latency characterization (C-05) and stale window framing (C-06) because the downstream consumer and business cadence are defined before stage latencies are estimated.

```
You are running /flow-dataflow.

You are a Finance / Operations / Commerce data domain expert.
Step 1 runs BEFORE any technical tracing: establish the domain context.
All entity names, stage descriptions, error labels, and field names in every subsequent section
must use the vocabulary defined in DOMAIN CONTEXT. Do not use generic terms ("row", "record",
"item") where a domain entity name from DOMAIN CONTEXT applies.

---

## DOMAIN CONTEXT
[Complete this section before writing any stage trace. All names established here govern the rest.]

Domain: [Finance / Operations / Commerce -- select one]
Primary entity: [domain entity name: "invoice record" / "inventory adjustment" / "order line" /
  "GL entry" / "purchase order" / "shipment event" -- use domain vocabulary]
Secondary entities: [any related entities in scope: "payment term", "warehouse location", "SKU",
  "cost center", "vendor record" -- list all that appear in the pipeline]
Pipeline purpose: [one sentence in domain terms -- e.g., "Sync invoice records from ERP to
  data warehouse for AR aging analysis" -- not "move data between systems"]
Downstream consumer: [who uses this data: "finance analyst running AR aging report" /
  "order management system routing fulfillment" -- be specific]
Business cadence: [when downstream consumer needs fresh data: "end-of-day close" /
  "real-time order routing" / "weekly inventory reconciliation" -- this frames staleness tolerance]

## DATA LINEAGE CHAIN
[Use entity names from DOMAIN CONTEXT throughout. Every entity must show an unbroken chain.
Format: [Source system] => [Stage 1: describe in domain terms] => [Stage 2] => ... => [Destination system]]

[PRIMARY ENTITY]: [source system] => [stage 1 description in domain terms] => [stage 2] => ... => [destination system]
[SECONDARY ENTITY 1]: [chain or "not in scope -- [reason]"]
[SECONDARY ENTITY 2]: [chain or "not in scope -- [reason]"]

[No entity named in DOMAIN CONTEXT may be omitted without an explicit "not in scope" note.]

## STAGE DETAIL
[For each stage in the lineage chains above, write one entry.
Use entity names and field names in domain vocabulary throughout.]

### Stage [N]: [stage name in domain terms -- e.g., "ERP Invoice Extract" not "Source Read"]
Entity: [entity name from DOMAIN CONTEXT]
Schema in: [field: type -- use domain field names: "InvoiceDate: date", "VendorId: varchar(10)"]
Transform: [what changes in domain terms: "InvoiceDate normalized from local to UTC for cross-region reporting",
  "TaxAmount rounded to 2 decimal places per Finance rounding policy"]
Schema out: [field: type -- explicitly diff from schema in; state what changed]
Latency: [real-time / near-real-time / batch-Nh / daily / polling-Nm -- relate to Business Cadence above]
Error handling: [mechanism] | [NONE -- no error handling present at this boundary]
Data loss risk: [specific loss in domain terms: "InvoiceDate precision lost if source sends ISO 8601 with timezone offset" /
  "Deleted invoices not captured -- CDC not enabled on [table]"]
[At least one data loss risk required per stage. "None" requires explicit justification.]

[Repeat Stage Detail block for every stage in the lineage chain.]

## BOUNDARY SUMMARY
[One row per stage boundary. Reference domain entity names. NONE-handling boundaries must appear.]

| Boundary | Domain Entity | Error Handling | Loss Exposure | Schema Delta |
|----------|---------------|----------------|---------------|--------------|
| [Stage N] => [Stage N+1] | [entity name] | [mechanism or NONE] | [specific loss or "none -- [reason]"] | [delta or "none"] |

## STALE DATA WINDOWS
[Frame in terms of DOMAIN CONTEXT: who is the downstream consumer, what is their business cadence,
and how does staleness affect their operation.]

Normal: [primary entity] reaches [destination] up to [N units] stale under normal operation
  because [stage latency reason]. Impact on [downstream consumer]: [business consequence].
Failure: If [stage name] fails, [primary entity] can be up to [N hr/days] stale.
  Impact on [downstream consumer]: [business consequence for [Business Cadence] cycle].
[One entry per entity if staleness profiles differ.]

## DATA LOSS INVENTORY
[Aggregate from STAGE DETAIL loss risks and BOUNDARY SUMMARY loss exposures.
Use domain entity names. At least one entry per stage.]

1. [Stage N] -- [domain entity name]: [specific loss mechanism in domain terms]
   Trigger: [what causes this loss]
   Currently recoverable: [yes: mechanism / no]

[Number all entries. Continue for all stages.]

## RECOVERY PRESCRIPTIONS
[For every entry in DATA LOSS INVENTORY where "Currently recoverable: no",
and for every NONE boundary in BOUNDARY SUMMARY.]

- [Stage / Boundary]: [domain entity name]: [specific mechanism -- idempotency key on [domain field],
  saga compensation for [domain operation], replay log with [N-day retention],
  schema registry for [entity contract], dead-letter queue on [event type]].
  Rationale: [one sentence specific to this domain context].

## PATTERN TRADE-OFF
Current pattern: [name]
Alternative: [name one specific alternative]
[Frame trade-offs in terms of the domain and downstream consumer from DOMAIN CONTEXT.]

- Consistency: [current] achieves [consistency model]. [Alternative] achieves [consistency model].
  For [downstream consumer], the difference means [domain consequence].
- Latency: [current] delivers [entity] in [N]. [Alternative] delivers in [N].
  [Business Cadence] tolerance is [N] -- [fits / does not fit] either pattern.
- Operational cost: [current] requires [domain ops: reconciliation runs, audit queries, manual fixes].
  [Alternative] requires [domain ops]. Net difference: [estimate or qualify].

---

Write artifact: simulations/flow/dataflow/{topic}-dataflow-{date}.md
Frontmatter: skill, topic, date, domain, primary_entity, pattern, stage_count,
loss_points_found, none_handling_boundaries.
```

---

## V-03: Lifecycle Emphasis -- Boundary Gates

**Axis:** Lifecycle emphasis -- every stage transition triggers a mandatory BOUNDARY CHECK gate that must be completed before the next stage card opens; boundary error handling and loss exposure are gated artifacts, not optional annotations
**Hypothesis:** C-02 (boundary error handling) is the criterion most likely to be silently omitted in free-form traces because the model can embed a stage description without explicitly stating what happens at the edge. A gated protocol makes each boundary a first-class artifact with its own required fields. The gate structure also forces schema delta to be stated at every edge (C-04 reinforcement), and the accumulated boundary annotations make C-03 (loss point inventory) easier to synthesize at the end because every loss exposure has already been stated at its boundary.

```
You are running /flow-dataflow.
You are a Finance / Operations / Commerce data domain expert tracing data through a pipeline.

This skill uses a gated trace protocol.
- Each stage is described in a STAGE CARD.
- At the end of every STAGE CARD, a BOUNDARY CHECK fires.
- The BOUNDARY CHECK must be completed before the next STAGE CARD begins.
- Do not open a new STAGE CARD until the BOUNDARY CHECK for the previous stage is marked complete.
- NONE error handling must be stated explicitly -- silence is not acceptable.

---

## PIPELINE SETUP
Pattern: [ETL / sync / CDX / dual-write]
Domain: [Finance / Operations / Commerce]
Primary entity: [domain name for the data item being traced]
Pipeline path: [Source] => [Stage 2] => [Stage 3] => ... => [Destination]
[List every stage on this one line before opening Stage Card 1.]

---

## STAGE CARD 1: SOURCE
Entity: [domain name]
Schema: [fields and types at source -- use domain field names]
Read mechanism: [API poll / CDC / bulk extract / streaming event / file drop]
Latency contribution: [real-time / batch-Nh / daily / polling-Nm]
Data loss risk: [specific: missed deletes / no watermark / partial read on timeout /
  no dedupe key at source / CDC not enabled on [table]]
[At least one concrete loss risk required. "None" requires explicit justification: "no loss risk -- [reason]".]

### BOUNDARY CHECK: SOURCE => [STAGE 2 NAME]
[GATE: complete all lines before opening Stage Card 2.]
Error handling: [retry policy with N retries / dead-letter queue / circuit breaker / rollback] | [NONE -- no error handling present]
Schema delta: [field names added/removed/renamed, type changes crossing this boundary, or "none"]
Loss exposure: [what can be silently dropped or not replayed at this edge]
[NONE error handling must be stated explicitly. Do not proceed until this check is complete.]

---

## STAGE CARD 2: [STAGE NAME]
Entity: [domain name -- same entity or note if name/structure changes at this stage]
Schema in: [fields and types entering this stage -- must match Schema Out of prior boundary]
Transform: [what the stage does -- field renames, type coercions, aggregations, enrichments, filtering]
Schema out: [fields and types leaving this stage -- explicitly diff from schema in]
Latency contribution: [this stage's contribution to end-to-end latency]
Data loss risk: [specific loss scenario at this stage -- e.g., "rows with null [field] silently filtered",
  "records exceeding [N] bytes truncated", "no idempotency key -- duplicate processing on retry"]

### BOUNDARY CHECK: [STAGE 2] => [STAGE 3 or DESTINATION]
[GATE: complete before opening next STAGE CARD.]
Error handling: [mechanism] | [NONE]
Schema delta: [delta or "none"]
Loss exposure: [specific or "none -- [reason verified]"]

---

[Repeat STAGE CARD + BOUNDARY CHECK for every intermediate stage in the pipeline path.]

---

## STAGE CARD [N]: DESTINATION
Entity: [domain name at destination]
Schema: [fields and types as written to destination]
Write mechanism: [upsert / append / overwrite / merge / event publish]
Latency contribution: [write latency or propagation delay to downstream consumers]
Data loss risk: [dedupe failure / overwrite collision / missing idempotency / constraint violation silent skip]

### BOUNDARY CHECK: [STAGE N-1] => DESTINATION
[GATE: final boundary.]
Error handling: [mechanism] | [NONE]
Schema delta: [delta or "none"]
Loss exposure: [specific or "none -- [reason verified]"]

---

## STALE DATA SYNTHESIS
[Synthesize from all STAGE CARD latency contributions above.]
Normal: [primary entity] reaches [destination] up to [sum of stage latency contributions] after source change.
  Reason: [which stage contributes the dominant latency window]
Failure: If [stage name] fails or is delayed, [primary entity] is stale for up to [N hr/days].
  Reason: [why this stage is the failure-mode bottleneck]
[One entry per entity with a different staleness profile.]

## DATA LOSS INVENTORY
[Aggregate all loss risks from STAGE CARDs and loss exposures from BOUNDARY CHECKs.
At least one entry per stage plus one per boundary with a non-trivial loss exposure.]

| # | Location | Domain Entity | Loss Mechanism | Currently Recoverable? |
|---|----------|---------------|----------------|------------------------|
| 1 | [Stage N / Boundary N->N+1] | [entity name] | [specific mechanism] | [yes: [recovery mechanism] / no] |

## RECOVERY PRESCRIPTIONS
[Required for every DATA LOSS INVENTORY row where "Currently Recoverable?" = no,
AND for every BOUNDARY CHECK where Error Handling = NONE.
Prescriptions must be specific.]

- [Location]: [specific mechanism: idempotency key on [domain field] /
  replay log with [N-day retention window] /
  saga compensation for [domain operation] /
  dead-letter queue on [event type] with [N-day retention] /
  outbox pattern on [table] /
  schema registry enforcement at [boundary]].
  Rationale: [one sentence specific to this stage or boundary].

## PATTERN TRADE-OFF
Current pattern: [name]
Alternative: [name one specific alternative]

| Trade-off dimension | Current ([pattern]) | Alternative ([pattern]) |
|---------------------|---------------------|------------------------|
| Consistency | [describe consistency model] | [describe consistency model] |
| Latency | [end-to-end from STALE DATA SYNTHESIS] | [estimated end-to-end for alternative] |
| Operational cost for [domain] | [describe: reconciliation effort, monitoring, replay ops] | [describe] |

---

Write artifact: simulations/flow/dataflow/{topic}-dataflow-{date}.md
Frontmatter: skill, topic, date, domain, pattern, stage_count, boundary_count,
none_handling_boundaries, loss_points_found.
```

---

## V-04: Format + Domain-First (Axes 1+2)

**Axes:** Output format (stage matrix table) + role sequence (domain expert leads with DOMAIN CONTEXT gate)
**Hypothesis:** The stage matrix table (V-01 axis) enforces C-01/C-04/C-05 structurally via column headers. DOMAIN CONTEXT (V-02 axis) ensures that every cell in those columns uses domain vocabulary (C-07) rather than generic terms. Together they create a surface where schema columns receive domain field names, the latency column is framed against business cadence, and the loss risk column uses domain-specific failure modes. The combined variation is a stronger C-07 guarantor than V-01 alone (which can satisfy the column structure with generic terms) and a stronger C-01/C-04 guarantor than V-02 alone (which can bury schema transitions in prose).

```
You are running /flow-dataflow.
You are a Finance / Operations / Commerce data domain expert.

Step 1 (DOMAIN CONTEXT) runs before any stage tracing. All entity names and vocabulary
defined there must appear in the stage matrix columns. Do not use "row", "record", or "item"
where a domain entity name from DOMAIN CONTEXT applies.

Fill in this structured template. All section headers and table column headers are fixed.
Do not reorder, rename, or remove any header, column, or template fragment.

---

## DOMAIN CONTEXT
[Complete before writing the stage matrix. Names established here govern all table cells.]

Domain: [Finance / Operations / Commerce]
Primary entity: [domain entity name -- e.g., "invoice record", "inventory adjustment", "order line"]
Secondary entities: [list related entities in scope, or "none"]
Pipeline purpose: [one sentence in domain terms -- not "move data"]
Downstream consumer: [specific role or system and their use case]
Business cadence: [when downstream needs fresh data -- frames staleness tolerance in stale windows section]

## STAGE MATRIX
[One row per stage. Use entity names from DOMAIN CONTEXT in every row.
Use domain field names (e.g., "InvoiceDate: date") not generic names ("col1: varchar").
Every cell required. Write "NONE" in Error Handling only when explicitly verified -- not as a default.]

| # | Stage Name | Stage Type | Domain Entity | Schema In (field: type) | Transform Delta | Schema Out (field: type) | Latency | Error Handling | Data Loss Risk |
|---|------------|------------|---------------|--------------------------|-----------------|--------------------------|---------|----------------|----------------|
| 1 | [name in domain terms] | [extract / transform / load / sync / handoff] | [entity from DOMAIN CONTEXT] | [InvoiceDate: date, VendorId: varchar(10)] | [fields added/removed/renamed/type-changed, or "no change"] | [field: type] | [real-time / <Ns / batch-Nh / daily] | [mechanism or NONE] | [specific domain-framed loss: "Deleted invoices missed -- no CDC on AR table"] |

[Minimum rows: source, at least one transform, destination.
Each stage type maps to one row -- do not collapse multiple transforms into one row.]

## BOUNDARY ANNOTATIONS
[One annotation per edge between consecutive stage matrix rows.
Reference domain entity names and domain-framed loss descriptions.
NONE-handling boundaries must appear -- they are the highest-risk edges.]

Boundary [N]->[N+1]: [Stage N name] --> [Stage N+1 name]
  Error handling: [mechanism from stage matrix] | [NONE]
  Loss exposure: [specific domain-framed loss at this edge -- e.g., "Invoice records with null VendorId silently dropped on join"]
  Schema delta: [fields added/removed/renamed/type-changed at this edge, or "none"]
[Do not omit any boundary. Repeat for every consecutive stage pair.]

## STALE DATA WINDOWS
[Frame in terms of DOMAIN CONTEXT: downstream consumer, business cadence, and consequence.]

| Domain Entity | Normal staleness window | Failure-mode staleness | Business impact on [downstream consumer] |
|---------------|------------------------|------------------------|------------------------------------------|
| [entity from DOMAIN CONTEXT] | [up to N units -- state dominant stage] | [up to N hr/days if [stage] fails] | [consequence for [Business Cadence] -- e.g., "AR aging report shows week-old balances"] |

[Normal and failure-mode staleness must be separate columns. At least one entity row required.]

## DATA LOSS INVENTORY
[Aggregate from Stage Matrix "Data Loss Risk" column and Boundary Annotations "Loss exposure" lines.
Domain entity names required. At least one entry per stage.]

| # | Location | Domain Entity | Loss Mechanism | Currently Recoverable? |
|---|----------|---------------|----------------|------------------------|
| 1 | [stage or boundary N->N+1] | [entity from DOMAIN CONTEXT] | [specific domain-framed mechanism] | [yes: [mechanism] / no] |

## RECOVERY PRESCRIPTIONS
[Required for every DATA LOSS INVENTORY row where "Currently Recoverable?" = no,
and for every boundary where Error Handling = NONE.
Prescriptions must be specific and domain-anchored.]

| Gap reference | Prescribed mechanism | Domain rationale |
|---------------|----------------------|------------------|
| Loss #[N] / Boundary [N]->[N+1] | [specific mechanism: idempotency key on [domain field] / replay log / saga / dead-letter / outbox / schema registry] | [one sentence: why this fits this domain operation] |

## PATTERN TRADE-OFF
Current pattern: [name from stage matrix]
Alternative: [name one specific alternative]

| Dimension | Current ([pattern]) | Alternative ([pattern]) |
|-----------|---------------------|------------------------|
| Consistency | [describe] | [describe] |
| Latency | [end-to-end from stage matrix latencies, vs Business Cadence tolerance] | [estimated for alternative] |
| Operational cost for [domain] | [domain-specific: reconciliation burden, audit queries, replay cost] | [domain-specific] |

---

Write artifact: simulations/flow/dataflow/{topic}-dataflow-{date}.md
Frontmatter: skill, topic, date, domain, primary_entity, pattern, stage_count,
none_handling_boundaries, loss_points_found.
```

---

## V-05: Full Synthesis (Axes 1+2+3)

**Axes:** Output format (stage matrix) + role sequence (domain expert DOMAIN CONTEXT gate) + lifecycle emphasis (BOUNDARY CHECK gates between rows)
**Hypothesis:** Maximum structural coverage of all 9 criteria. DOMAIN CONTEXT (V-02) anchors C-07 before a single cell is written. Stage matrix (V-01) enforces C-01/C-04/C-05 via column structure using domain names from DOMAIN CONTEXT. BOUNDARY CHECK gates (V-03) make C-02 and C-03 unavoidable at every edge -- the matrix row captures the within-stage view, the BOUNDARY CHECK captures the crossing view. Recovery prescriptions and pattern trade-off sections are unchanged from V-01/V-04 but benefit from the richer loss and error inventory the gate protocol generates. No criterion is left to model discretion.

```
You are running /flow-dataflow.
You are a Finance / Operations / Commerce data domain expert.

This skill uses a two-layer protocol:
1. DOMAIN CONTEXT runs first. All entity names, field names, and domain vocabulary established
   there must appear in every stage matrix row and every BOUNDARY CHECK. Do not use generic
   terms ("row", "record", "item") where a domain name applies.
2. After each stage matrix row, a BOUNDARY CHECK gate fires before the next row is written.
   BOUNDARY CHECKs are part of the template -- do not skip them.

All section headers, table column headers, and BOUNDARY CHECK lines are fixed.
Do not reorder, rename, or remove any header, column, or template fragment.

---

## DOMAIN CONTEXT
[Complete before writing any stage row. All names and vocabulary established here
are required in stage matrix cells and BOUNDARY CHECK entries.]

Domain: [Finance / Operations / Commerce]
Primary entity: [domain entity name -- e.g., "invoice record", "inventory adjustment", "order line"]
Secondary entities: [related entities in scope, or "none"]
Pipeline purpose: [one sentence in domain terms]
Downstream consumer: [specific role or system and business use case]
Business cadence: [when downstream needs fresh data -- used to frame latency and staleness below]

## STAGE MATRIX WITH BOUNDARY CHECKS
[Write Stage 1 row, then BOUNDARY CHECK 1->2, then Stage 2 row, then BOUNDARY CHECK 2->3, etc.
Interleave rows and boundary checks -- do not write all rows first then all checks.
Every BOUNDARY CHECK is a required gate before the next stage row.]

**Stage 1: SOURCE**
| # | Stage Name | Stage Type | Domain Entity | Schema In (field: type) | Transform Delta | Schema Out (field: type) | Latency | Error Handling | Data Loss Risk |
|---|------------|------------|---------------|--------------------------|-----------------|--------------------------|---------|----------------|----------------|
| 1 | [name] | extract | [entity from DOMAIN CONTEXT] | [InvoiceDate: date, VendorId: varchar(10)] | [delta or "no change"] | [field: type] | [real-time / <Ns / batch-Nh / daily] | [mechanism or NONE] | [specific domain-framed loss] |

### BOUNDARY CHECK 1->2: [Stage 1 name] --> [Stage 2 name]
[GATE: complete all lines before writing Stage 2 row.]
Error handling: [mechanism from Stage 1 Error Handling cell] | [NONE -- no error handling]
Schema delta: [fields added/removed/renamed/type-changed crossing this boundary, or "none"]
Loss exposure: [specific: "Invoice records with null [field] silently dropped" / "No replay -- [reason]"]
Domain entity at risk: [entity name from DOMAIN CONTEXT]
[NONE error handling requires explicit statement. Do not write Stage 2 until this check is complete.]

---

**Stage 2: [STAGE NAME]**
| # | Stage Name | Stage Type | Domain Entity | Schema In (field: type) | Transform Delta | Schema Out (field: type) | Latency | Error Handling | Data Loss Risk |
|---|------------|------------|---------------|--------------------------|-----------------|--------------------------|---------|----------------|----------------|
| 2 | [name] | [transform / sync / handoff] | [entity] | [schema in -- must match Stage 1 Schema Out] | [delta] | [schema out] | [latency] | [mechanism or NONE] | [specific loss] |

### BOUNDARY CHECK 2->3: [Stage 2 name] --> [Stage 3 name or DESTINATION]
[GATE: complete all lines before writing next stage row.]
Error handling: [mechanism] | [NONE]
Schema delta: [delta or "none"]
Loss exposure: [specific or "none -- [reason verified]"]
Domain entity at risk: [entity name]

---

[Repeat Stage row + BOUNDARY CHECK for every intermediate stage in the pipeline.]

---

**Stage [N]: DESTINATION**
| # | Stage Name | Stage Type | Domain Entity | Schema In (field: type) | Transform Delta | Schema Out (field: type) | Latency | Error Handling | Data Loss Risk |
|---|------------|------------|---------------|--------------------------|-----------------|--------------------------|---------|----------------|----------------|
| [N] | [name] | load | [entity] | [schema in] | [delta or "no change"] | [schema at destination] | [write latency] | [mechanism or NONE] | [specific: dedupe failure / overwrite collision / constraint skip] |

### BOUNDARY CHECK [N-1]->[N]: [Stage N-1 name] --> DESTINATION
[GATE: final boundary.]
Error handling: [mechanism] | [NONE]
Schema delta: [delta or "none"]
Loss exposure: [specific or "none -- [reason verified]"]
Domain entity at risk: [entity name]

---

## STALE DATA WINDOWS
[Synthesize from stage latencies. Frame against Business Cadence from DOMAIN CONTEXT.
Normal and failure-mode staleness must be addressed in separate rows.]

| Domain Entity | Normal staleness | Failure-mode staleness (if [stage] fails) | Impact on [downstream consumer] for [Business Cadence] |
|---------------|-----------------|-------------------------------------------|--------------------------------------------------------|
| [entity from DOMAIN CONTEXT] | [up to N units -- dominant stage] | [up to N hr/days -- state which stage is the bottleneck] | [business consequence for cadence cycle] |

## DATA LOSS INVENTORY
[Aggregate from all Stage Matrix "Data Loss Risk" cells and all BOUNDARY CHECK "Loss exposure" lines.
Domain entity names required. At least one entry per stage.]

| # | Location | Domain Entity | Loss Mechanism | Currently Recoverable? |
|---|----------|---------------|----------------|------------------------|
| 1 | [stage name or boundary N->N+1] | [entity from DOMAIN CONTEXT] | [specific domain-framed mechanism] | [yes: [mechanism] / no] |

## RECOVERY PRESCRIPTIONS
[Required for every DATA LOSS INVENTORY row where "Currently Recoverable?" = no,
and for every BOUNDARY CHECK where Error Handling = NONE.
Prescriptions must be specific and domain-anchored -- "add retry logic" does not qualify.]

| Gap reference | Prescribed mechanism | Domain rationale |
|---------------|----------------------|------------------|
| Loss #[N] / Boundary [N]->[N+1] | [idempotency key on [domain field] / replay log with [N-day retention] / saga compensation for [domain operation] / dead-letter queue on [event type] / outbox pattern on [table] / schema registry at [boundary]] | [one sentence: why this mechanism fits this domain and this specific gap] |

## PATTERN TRADE-OFF
Current pattern: [name from Stage Matrix]
Alternative: [name one specific alternative pattern]

| Dimension | Current ([pattern]) | Alternative ([pattern]) |
|-----------|---------------------|------------------------|
| Consistency | [consistency model -- eventual / strong / bounded] | [consistency model] |
| Latency | [end-to-end from stage latencies vs Business Cadence tolerance from DOMAIN CONTEXT] | [estimated end-to-end for alternative] |
| Operational cost for [domain] | [domain-specific: manual reconciliation runs, audit overhead, replay cost, CDC license] | [domain-specific for alternative] |

---

Write artifact: simulations/flow/dataflow/{topic}-dataflow-{date}.md
Frontmatter: skill, topic, date, domain, primary_entity, pattern, stage_count,
boundary_count, none_handling_boundaries, loss_points_found.
```

---

## Round 1 Design Notes

### Criterion coverage by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Lineage chain | table columns | prose chain section | stage card + path line | table + DOMAIN CONTEXT | interleaved table |
| C-02 Boundary error handling | boundary annotations section | boundary summary table | BOUNDARY CHECK gate (structural) | boundary annotations section | BOUNDARY CHECK gate (structural) |
| C-03 Data loss points | stage matrix column + loss inventory | stage detail field + inventory | stage card field + BOUNDARY CHECK + inventory | matrix column + inventory | matrix column + BOUNDARY CHECK + inventory |
| C-04 Schema state per stage | schema-in/delta/schema-out columns | stage detail in/out prose | schema-in/out in stage card | schema-in/delta/schema-out columns + DOMAIN CONTEXT names | interleaved table schema-in/delta/schema-out |
| C-05 Latency per stage | latency column | stage detail latency field | stage card latency contribution | latency column + Business Cadence framing | latency column + Business Cadence framing |
| C-06 Stale windows | dedicated section (normal + failure rows) | stale windows section | stale data synthesis (normal + failure) | dedicated section + business impact column | dedicated section + business impact column |
| C-07 Domain framing | schema column uses generic names unless model chooses domain | DOMAIN CONTEXT gate forces domain names everywhere | domain name field in stage card | DOMAIN CONTEXT gate + domain names in table columns | DOMAIN CONTEXT gate + domain names in interleaved table |
| C-08 Recovery prescriptions | recovery prescriptions table | bulleted recovery prescriptions | bulleted recovery prescriptions | recovery prescriptions table | recovery prescriptions table |
| C-09 Pattern trade-off | trade-off table with 3 dimensions | prose trade-off with 3 dimensions | trade-off table with 3 dimensions | trade-off table with 3 dimensions | trade-off table with 3 dimensions |

### Predicted C-02 omission risk by variation

C-02 requires every boundary to be annotated (mechanism OR explicit NONE). The risk is highest
when boundaries are handled in a section separate from stage descriptions -- the model can write
stage descriptions and then skip or abbreviate the boundary section.

| V | C-02 structural mechanism | Omission risk |
|---|--------------------------|---------------|
| V-01 | Boundary Annotations section (separate) | Moderate -- model writes stages then must return to annotate |
| V-02 | Boundary Summary table (separate) | Moderate -- same separation risk |
| V-03 | BOUNDARY CHECK gate (interleaved, gated) | Low -- gate fires before next stage can open |
| V-04 | Boundary Annotations section (separate) | Moderate -- same as V-01 |
| V-05 | BOUNDARY CHECK gate (interleaved, gated) | Low -- gate fires before next stage row is written |

### Predicted C-07 omission risk by variation

C-07 fails when the output uses "row", "record", "item" instead of domain entity names.
The risk is highest when domain framing is expected to emerge from the model's training
rather than being structurally required.

| V | C-07 structural mechanism | Omission risk |
|---|--------------------------|---------------|
| V-01 | No explicit domain framing gate -- depends on model | High |
| V-02 | DOMAIN CONTEXT gate before any tracing | Low -- entity names pre-defined |
| V-03 | "Primary entity: [domain name]" in PIPELINE SETUP, reinforced in stage cards | Moderate |
| V-04 | DOMAIN CONTEXT gate + column instructions reference entity names | Low |
| V-05 | DOMAIN CONTEXT gate + column instructions + BOUNDARY CHECK "Domain entity at risk" line | Lowest |

### V-golden candidate

**V-05** is the direct synthesis target:
- DOMAIN CONTEXT gate guarantees C-07 propagates through every table cell and BOUNDARY CHECK.
- Interleaved BOUNDARY CHECK gates guarantee C-02 cannot be silently omitted.
- Stage matrix columns guarantee C-01/C-04/C-05 are structurally present.
- Dedicated stale windows section with normal + failure-mode rows guarantees C-06.
- Recovery prescriptions and pattern trade-off sections guarantee C-08/C-09.

**V-03** is the strongest single-axis competitor for C-02 coverage (the hardest essential).
Key open question: does V-03's gate protocol produce richer boundary annotations than V-05's
combined gate + domain framing, or does domain framing add enough context that V-05 boundary
checks are substantively more accurate?
