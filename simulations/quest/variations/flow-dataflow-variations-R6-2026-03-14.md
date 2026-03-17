Good context. R5 all 5 scored 100/100 at 14/14 aspirational, but C-22/C-23/C-24 were uncodified excellence signals. The v6 rubric now formalizes them. R6 variations must target all three new criteria simultaneously while varying axes.

**Key distinctions to nail:**
- **C-22** requires a pre-role *table* with token/owner/description columns — prefix declaration (V-01 R5) and flat label list (V-03 R5) no longer pass
- **C-23** requires the model to *produce and tick* a checklist inline — post-hoc audit doesn't qualify
- **C-24** requires both an upfront named constraint section *and* inline callbacks by ID at every enforcement point — one without the other fails

---

## flow-dataflow — Round 6 Variations

**Variation axes selected:**
- **Single-axis:** Role Sequence (V-01), Output Format (V-02), Phrasing Register (V-03)
- **Combined:** Role Sequence + Inertia Framing (V-04), Output Format + Lifecycle Emphasis (V-05)

---

## V-01 — Single axis: Role Sequence (Commerce → Finance → Operations)

**Axis:** Commerce domain expert runs first and owns the pipeline trace. Finance expert validates the threshold contract and closes Role 2. Operations expert closes with resilience and trade-off analysis. Tests that C-16 cross-role citation chain produces named handoffs in non-standard domain order.

**Hypothesis:** Resequencing domain roles away from the most-natural order (Operations-first) forces Role 2 and Role 3 to cite Role 1 outputs by token rather than inferring context, strengthening C-16 compliance.

---

```text
You are simulating three domain experts performing a data lineage trace for a nightly
inventory-sync pipeline at a mid-market omni-channel retailer. POS terminals capture
transactions to a local store cache, synced to a central Inventory Management System (IMS),
then pushed nightly to an ERP Finance Ledger. Finance closes books at 18:00 daily.

Role order: Commerce (trace owner) → Finance (threshold authority) → Operations (resilience).

══════════════════════════════════════════
ARTIFACT REGISTRY
══════════════════════════════════════════

Produce this table in full before writing any role output. Every artifact cited
downstream must appear as a row here. A citation to a target not in this table does
not pass.

| Token  | Artifact                     | Owner               | Description                                                         |
|--------|------------------------------|---------------------|---------------------------------------------------------------------|
| [A-01] | DOMAIN CONTEXT               | Role 1 (Commerce)   | Entity vocabulary, downstream consumer, cadence, staleness SLA      |
| [A-02] | INCUMBENT BASELINE           | Role 1 (Commerce)   | Prior manual process replaced by this pipeline                      |
| [A-03] | STAGE TRACE (Stages 1–3)     | Role 1 (Commerce)   | Lineage chain: schema in/out, transformation, latency, loss points  |
| [A-04] | BOUNDARY CHECKS (BC-1, BC-2) | Role 1 (Commerce)   | Error handling, cumulative elapsed, freshness verdict per boundary  |
| [A-05] | STALE ANALYSIS               | Role 1 (Commerce)   | Quantified stale windows — normal-operation and failure-mode        |
| [A-06] | RECOVERY PRESCRIPTIONS       | Role 1 (Commerce)   | Named recovery action per loss point and per no-handling annotation |
| [A-07] | THRESHOLD RATIFICATION       | Role 2 (Finance)    | Finance sign-off on [A-01] staleness SLA vs daily close requirement |
| [A-08] | PATTERN TRADE-OFF            | Role 3 (Operations) | Named alternative pattern with ≥2 trade-off dimensions              |
| [A-09] | PHASE GATE — POST ROLE 1     | Role 1 (Commerce)   | Self-verification checklist gating Role 2 entry                     |
| [A-10] | PHASE GATE — POST ROLE 2     | Role 2 (Finance)    | Self-verification checklist gating Role 3 entry                     |

══════════════════════════════════════════
STRUCTURAL CONSTRAINTS
══════════════════════════════════════════

SC-1  CITATION CONVENTION
      All artifact references use [A-xx] token form from the registry. Prose
      back-references ("as noted earlier", "as established above") do not pass.
      Every role must open with a "Citing:" line listing each [A-xx] it builds on.

SC-2  WRITE-ORDER GATE
      Stage N+1 may not be written until the BOUNDARY CHECK between Stage N and
      Stage N+1 is fully complete with all four required fields present: Boundary,
      Error handling, Elapsed total (cumulative), Freshness verdict.
      Apply SC-2: write BC-1 before Stage 2. Write BC-2 before Stage 3.

SC-3  ELAPSED ACCUMULATION
      Each BOUNDARY CHECK must include the field "Elapsed total (cumulative):"
      computed as the sum of all prior stage latencies plus all prior boundary
      overhead to this point. Compute this field inside the BOUNDARY CHECK block —
      it may not be deferred to STALE ANALYSIS.

SC-4  FRESHNESS VERDICT
      Each BOUNDARY CHECK must include "Freshness verdict: FRESH | STALE" derived
      by comparing the cumulative elapsed total against the threshold declared in
      [A-01]. A boundary that records elapsed time without a verdict does not pass.

SC-5  IMMUTABILITY
      The staleness threshold declared in [A-01] is fixed the moment Stage 1 is
      written. No role may revise it after that point. [A-01] must contain this
      statement verbatim: "This threshold is fixed. No role may revise it after
      Stage 1 is written."

══════════════════════════════════════════
ROLE 1 — COMMERCE DOMAIN EXPERT
══════════════════════════════════════════

You are a Commerce data analyst who owns the POS-to-IMS integration.

Step 1 — Write [A-01] DOMAIN CONTEXT.
  Lock the following before Stage 1 is written:
  - Entity names (e.g., SKU, POS transaction record, stock-on-hand quantity,
    store cache entry). Use these names verbatim in all subsequent content.
  - Downstream consumer: Finance team.
  - Business cadence: Finance daily close at 18:00.
  - Staleness SLA: "SKU stock-on-hand must be current within [N] minutes of
    POS capture at close time."
  Per SC-5, append: "This threshold is fixed. No role may revise it after
  Stage 1 is written."

Step 2 — Write [A-02] INCUMBENT BASELINE.
  Describe the prior process (e.g., end-of-day CSV export, manual store count
  submitted by store managers). Use at least one entity name from [A-01].
  This baseline will be cited by [A-06] or [A-08].

Step 3 — Write [A-03] STAGE TRACE.
  Stages: POS Terminal → Inventory Management System → ERP Finance Ledger.
  For each stage produce exactly this block:

    STAGE N — [Stage Name]
    Schema in:       [fields entering this stage, with types]
    Schema out:      [fields exiting — explicitly note any name or type changes]
    Transformation:  [what this stage does to the data]
    Latency:         [value, range, or characterization: real-time / near-real / batch / daily]
    Loss point:      [one concrete failure scenario — not "errors may occur"]
    Domain entity:   [named entity from [A-01] in scope]

  Apply SC-2 strictly. After Stage 1, write BC-1 before continuing to Stage 2.
  After Stage 2, write BC-2 before continuing to Stage 3.

  Boundary check format (write inline between stages, not post-hoc):

    BOUNDARY CHECK BC-N (Stage N → Stage N+1)  [A-04]
    Boundary:                   [the handoff point]
    Error handling:             [mechanism — or "no handling — see [A-06]"]
    Domain entity at boundary:  [named entity from [A-01] — not "data" or "records"]
    Elapsed total (cumulative): [Per SC-3: sum all prior latencies]  ← compute here
    Freshness verdict:          [Per SC-4: FRESH or STALE vs [A-01] threshold]

Step 4 — Write [A-05] STALE ANALYSIS.
  Citing [A-04] for elapsed totals and [A-01] for the threshold:
  - Quantify the normal-operation stale window (time from POS capture to ledger
    update under nominal conditions).
  - Address failure-mode staleness separately (e.g., what if BC-1 retries and
    adds 20 minutes; does the pipeline breach the SLA?).

Step 5 — Write [A-06] RECOVERY PRESCRIPTIONS.
  Citing [A-03] (loss points) and [A-04] (no-handling annotations):
  - For every concrete loss point in [A-03]: provide a named recovery mechanism.
  - For every "no handling" in [A-04]: provide a specific remedy.
  - Cite [A-02] at least once: "Fall back to [A-02] if [condition]."

Step 6 — Produce [A-09] PHASE GATE — POST ROLE 1.
  The model must write this checklist, tick each item ✓ or mark ✗ with a note,
  and confirm all items are ✓ before Role 2 may begin.

    PHASE GATE — POST ROLE 1  [A-09]
    [ ] C-01: Every stage has an unbroken source → destination chain.
    [ ] C-02: Every boundary has an error handling annotation or explicit "no handling."
    [ ] C-03: At least one concrete loss point per stage (not a generic phrase).
    [ ] C-04: Schema in and schema out documented for every stage.
    [ ] SC-2: BC-1 was written before Stage 2; BC-2 was written before Stage 3.
    [ ] SC-3: Every BOUNDARY CHECK has "Elapsed total (cumulative):" inside the block.
    [ ] SC-4: Every BOUNDARY CHECK has "Freshness verdict: FRESH | STALE."
    [ ] SC-5: [A-01] contains the immutability statement before Stage 1.
    [ ] SC-1: All citations use [A-xx] token form — no prose back-references.

  If any item is ✗, fix the gap before proceeding.

══════════════════════════════════════════
ROLE 2 — FINANCE DOMAIN EXPERT
══════════════════════════════════════════

Citing [A-01] (staleness SLA), [A-04] (elapsed totals), [A-05] (stale analysis).

Step 1 — Write [A-07] THRESHOLD RATIFICATION.
  - State the Finance close constraint: maximum acceptable data age at 18:00.
  - Compare the cumulative elapsed total from [A-04] against this constraint.
  - State a binary verdict: ACCEPTABLE or UNACCEPTABLE, with one sentence of
    reasoning.
  - If UNACCEPTABLE, identify which boundary or stage is the bottleneck.

Step 2 — Produce [A-10] PHASE GATE — POST ROLE 2.
  Tick each item ✓ or mark ✗ with a note. Role 3 may not begin until all items are ✓.

    PHASE GATE — POST ROLE 2  [A-10]
    [ ] C-16: [A-07] opened with a Citing: line naming [A-01], [A-04].
    [ ] SC-1: All citations in [A-07] use [A-xx] token form.
    [ ] C-07: Domain entity names from [A-01] appear in [A-07] (not purely generic).
    [ ] C-13: [A-05] evaluated staleness rows against [A-01] threshold — not asserted post-hoc.
    [ ] C-14: Stale window in [A-05] traces back to [A-04] elapsed totals numerically.

══════════════════════════════════════════
ROLE 3 — OPERATIONS DOMAIN EXPERT
══════════════════════════════════════════

Citing [A-01] (entities), [A-02] (incumbent), [A-06] (recovery), [A-07] (ratification).

Step 1 — Write [A-08] PATTERN TRADE-OFF.
  Name one alternative pipeline pattern (e.g., CDC via Kafka, micro-batch streaming,
  event sourcing).
  Compare this pipeline to the alternative on at least two dimensions (e.g., latency,
  operational complexity, cost, failure isolation) with quantified or qualified values.
  Reference [A-02] as one comparison anchor.

Step 2 — Write FINAL ASSESSMENT (3–5 sentences).
  Reference at least one finding from [A-04], [A-05], [A-06], and [A-07] by [A-xx] token.
  State whether this pipeline meets the Finance close SLA ratified in [A-07].
```

---

## V-02 — Single axis: Output Format (table-driven lineage with embedded boundary rows)

**Axis:** The stage trace is rendered as a single LINEAGE TABLE in which boundary check rows appear inline between stage rows. Every structural field becomes a column. Tests whether a tabular format carries all 24 criteria without losing the boundary gate enforcement of C-11, C-20, and the incremental computation of C-18.

**Hypothesis:** Embedding boundary checks as typed rows inside the lineage table forces column presence to be structurally verifiable (a missing "Freshness verdict" cell is visible in the table), making C-21 compliance easier to detect than in prose blocks.

---

```text
You are simulating two domain experts performing a data lineage trace for a CDX
(Customer Data Exchange) sync pipeline at a B2B commerce operator. The pipeline
pushes customer order data from an Order Management System (OMS) through a data
transformation layer to a downstream Finance settlement system. Settlement runs
at end-of-business daily.

Role order: Operations (trace and analysis) → Commerce (validation and trade-off).

══════════════════════════════════════════
ARTIFACT REGISTRY
══════════════════════════════════════════

Produce this table before any role output. Citations not in this table do not pass.

| Token  | Artifact                      | Owner               | Description                                                          |
|--------|-------------------------------|---------------------|----------------------------------------------------------------------|
| [A-01] | DOMAIN CONTEXT                | Role 1 (Operations) | Entity vocabulary, consumer, cadence, staleness SLA                  |
| [A-02] | INCUMBENT BASELINE            | Role 1 (Operations) | Prior manual/batch process this pipeline replaces                    |
| [A-03] | LINEAGE TABLE                 | Role 1 (Operations) | Unified table: stage rows + inline boundary check rows               |
| [A-04] | STALE ANALYSIS TABLE          | Role 1 (Operations) | Tabular stale windows — normal and failure-mode                      |
| [A-05] | RECOVERY TABLE                | Role 1 (Operations) | Tabular recovery prescriptions per loss point and no-handling flag   |
| [A-06] | PHASE GATE — POST ROLE 1      | Role 1 (Operations) | Self-verification checklist gating Role 2 entry                      |
| [A-07] | ENTITY VALIDATION TABLE       | Role 2 (Commerce)   | Per-boundary entity exposure audit                                   |
| [A-08] | PATTERN TRADE-OFF TABLE       | Role 2 (Commerce)   | Comparative table: this pipeline vs named alternative                |

══════════════════════════════════════════
STRUCTURAL CONSTRAINTS
══════════════════════════════════════════

SC-1  CITATION CONVENTION
      All artifact references use [A-xx] token form from the registry. Every role
      opens with "Citing: [A-xx], [A-xx], ..." listing its input artifacts.

SC-2  WRITE-ORDER GATE
      A BOUNDARY CHECK row may not be followed by the next STAGE row until all
      four required fields in that BOUNDARY CHECK row are present: Elapsed (cumul.),
      Freshness verdict, Error handling, Domain entity. Per SC-2, Stage N+1 may not
      be written until the boundary row between Stage N and Stage N+1 is complete.

SC-3  ELAPSED ACCUMULATION
      The "Elapsed (cumul.)" cell in every boundary row is the running sum of all
      prior stage latencies plus all prior boundary overhead. It must be filled in
      the boundary row itself — not derived retroactively in [A-04].

SC-4  FRESHNESS VERDICT
      Each boundary row must contain "FRESH" or "STALE" in the Freshness verdict
      column, derived by comparing "Elapsed (cumul.)" against the SLA in [A-01].

SC-5  IMMUTABILITY
      The staleness SLA declared in [A-01] is fixed before Stage 1 is added to
      [A-03]. Append to [A-01]: "This SLA is fixed. It may not be revised after
      Stage 1 is written."

══════════════════════════════════════════
ROLE 1 — OPERATIONS DOMAIN EXPERT
══════════════════════════════════════════

Step 1 — Write [A-01] DOMAIN CONTEXT.
  Declare: entity names (customer order, line item, settlement record, OMS
  transaction ID), downstream consumer (Finance settlement team), business cadence
  (end-of-business daily), staleness SLA (e.g., "Settlement records must reflect
  all OMS orders within [N] hours of business close").
  Per SC-5, append the immutability statement.

Step 2 — Write [A-02] INCUMBENT BASELINE.
  Describe the prior process (e.g., nightly SFTP file drop, manual reconciliation
  by Finance). Include at least one entity name from [A-01]. This baseline will
  be cited in [A-05] or [A-08].

Step 3 — Write [A-03] LINEAGE TABLE.
  Produce a single Markdown table with these columns:

  | Row type | Stage/Boundary | Schema in | Schema out | Transformation | Latency | Loss point | Domain entity | Error handling | Elapsed (cumul.) | Freshness verdict |

  Row types:
  - STAGE rows: fill Stage/Boundary, Schema in, Schema out, Transformation,
    Latency, Loss point, Domain entity. Leave Error handling, Elapsed (cumul.),
    Freshness verdict as "—".
  - BOUNDARY rows: fill Stage/Boundary (e.g., "BC-1: OMS → Transform"),
    Error handling, Domain entity, Elapsed (cumul.) [Per SC-3], Freshness
    verdict [Per SC-4]. Leave Schema in/out, Transformation, Latency, Loss
    point as "—".

  Apply SC-2: insert the BOUNDARY row for BC-1 before adding the Stage 2 row.
  Insert the BOUNDARY row for BC-2 before adding the Stage 3 row.

  Required rows in order:
    STAGE 1 — OMS Capture
    BOUNDARY CHECK BC-1 (OMS → Transform Layer)   ← SC-2 gate
    STAGE 2 — Transformation Layer
    BOUNDARY CHECK BC-2 (Transform Layer → Finance Settlement)  ← SC-2 gate
    STAGE 3 — Finance Settlement System

  Domain entity column must name a specific entity from [A-01] — not "data"
  or "records."

Step 4 — Write [A-04] STALE ANALYSIS TABLE.
  Citing [A-03] for elapsed values, citing [A-01] for threshold.

  | Scenario | Elapsed (cumul.) | SLA threshold | Stale? | Note |
  |----------|-----------------|---------------|--------|------|

  Row 1: normal-operation path.
  Row 2: failure-mode path (e.g., BC-1 retries for 30 min).
  Address failure-mode staleness separately from normal-operation.

Step 5 — Write [A-05] RECOVERY TABLE.
  Citing [A-03] (loss points and no-handling flags):

  | Loss point / No-handling source | Recovery mechanism | References |
  |---|----|---|

  For every Loss point cell in [A-03]: provide a specific named recovery action.
  For every "no handling" in Error handling column of [A-03]: provide a remedy.
  At least one row must cite [A-02]: "Fall back to [A-02] if [condition]."

Step 6 — Produce [A-06] PHASE GATE — POST ROLE 1.
  Write this checklist. Tick ✓ or mark ✗ with a note. Role 2 may not begin
  until all items are ✓.

    PHASE GATE — POST ROLE 1  [A-06]
    [ ] C-01: Every stage row has an unbroken source → destination path in the table.
    [ ] C-02: Every boundary row has a filled Error handling cell (not blank).
    [ ] C-03: Every stage row has a concrete Loss point cell (not "errors may occur").
    [ ] C-04: Every stage row has distinct Schema in and Schema out cells; changes noted.
    [ ] SC-2: BC-1 row precedes Stage 2 row; BC-2 row precedes Stage 3 row in [A-03].
    [ ] SC-3: Elapsed (cumul.) cell in each boundary row computed as running sum.
    [ ] SC-4: Freshness verdict cell in each boundary row is FRESH or STALE.
    [ ] SC-5: [A-01] contains the immutability statement.
    [ ] SC-1: All citations use [A-xx] token form.

══════════════════════════════════════════
ROLE 2 — COMMERCE DOMAIN EXPERT
══════════════════════════════════════════

Citing [A-01] (entities), [A-03] (lineage table), [A-05] (recovery table).

Step 1 — Write [A-07] ENTITY VALIDATION TABLE.
  For each boundary row in [A-03], confirm the Domain entity cell names a specific
  entity from [A-01] (not "data" or "records").

  | Boundary | Entity named in [A-03] | In [A-01] vocabulary? | Pass/Fail |
  |----|----|----|---|

Step 2 — Write [A-08] PATTERN TRADE-OFF TABLE.
  Name one alternative pipeline pattern (e.g., event sourcing, Kafka CDC).
  Produce a comparison table:

  | Dimension | This pipeline | [Alternative name] | [A-02] incumbent |
  |----|----|----|---|

  At least two dimension rows with qualified or quantified values.
  Include [A-02] as a comparison column to close the baseline loop.
```

---

## V-03 — Single axis: Phrasing Register (directive/imperative)

**Axis:** Every instruction is a direct imperative: short sentences, action-first, "Stop here. Do not continue. Check. Then proceed." Minimal section headers, no subordinate clauses. Tests whether directive register maintains full structural coverage without the scaffolding of formal block headers.

**Hypothesis:** Directive phrasing keeps the model from skipping gate requirements by making each step feel like a hard command rather than a suggestion inside a longer instruction block.

---

```text
You are a Finance, Operations, and Commerce data pipeline expert. Trace customer
order data through a dual-write ETL pipeline: source CRM → transformation stage →
destination data warehouse used for Finance revenue reporting. Finance reports run
at 06:00 each morning from the prior day's close.

Do exactly what each step says. Do not skip ahead. Do not batch steps.

══════════════════════════════════════════
PROTOCOL RULES
══════════════════════════════════════════

R-01  Build the ARTIFACT REGISTRY TABLE first. No role output before the table is done.
R-02  All citations use [A-xx] token form from the ARTIFACT REGISTRY TABLE. No exceptions.
      Every role opens with "Citing: [A-xx], [A-xx]..." listing its sources.
R-03  Stage N+1 may not be written until the BOUNDARY CHECK before it is fully written
      with all four fields present: Error handling, Domain entity, Elapsed (cumul.),
      Freshness verdict. Stop at the boundary. Fill it. Then advance.
R-04  Elapsed (cumul.) is computed inside each BOUNDARY CHECK as a running total of
      all prior stage latencies plus boundary overhead. Do not defer it.
R-05  Each BOUNDARY CHECK must state "Freshness verdict: FRESH | STALE" by comparing
      Elapsed (cumul.) against the SLA declared before Stage 1.
R-06  The staleness SLA declared before Stage 1 is immutable. State this in the SLA
      declaration: "This SLA cannot be revised after Stage 1 is written."
R-07  At each phase gate, produce a checklist. Tick each item. If any item fails,
      fix it before continuing.

══════════════════════════════════════════
ARTIFACT REGISTRY TABLE
══════════════════════════════════════════

Produce this now. Do not write any role output until the table is complete.

| Token  | Artifact                     | Owner                  | Description                                                         |
|--------|------------------------------|------------------------|---------------------------------------------------------------------|
| [A-01] | DOMAIN CONTEXT               | Role 1 (Operations)    | Entity names, consumer, cadence, staleness SLA with immutability    |
| [A-02] | INCUMBENT BASELINE           | Role 1 (Operations)    | Prior manual process this pipeline replaces                         |
| [A-03] | STAGE TRACE                  | Role 1 (Operations)    | Stage blocks: schema, latency, loss point, domain entity            |
| [A-04] | BOUNDARY CHECKS              | Role 1 (Operations)    | BC-1 and BC-2 inline blocks: error handling, elapsed, verdict       |
| [A-05] | STALE ANALYSIS               | Role 1 (Operations)    | Stale windows — normal and failure-mode                             |
| [A-06] | RECOVERY PRESCRIPTIONS       | Role 1 (Operations)    | Named recovery per loss point and no-handling flag                  |
| [A-07] | PHASE GATE — POST ROLE 1     | Role 1 (Operations)    | Checklist gating Role 2 entry                                       |
| [A-08] | ENTITY AUDIT                 | Role 2 (Commerce)      | Entity validation per boundary from [A-04]                          |
| [A-09] | PATTERN TRADE-OFF            | Role 2 (Commerce)      | Named alternative, ≥2 trade-off dimensions                          |
| [A-10] | FINANCE SIGN-OFF             | Role 3 (Finance)       | Threshold ratification vs revenue reporting cadence                 |

══════════════════════════════════════════
ROLE 1 — OPERATIONS
══════════════════════════════════════════

Step 1. Write [A-01] DOMAIN CONTEXT now.
  Name every entity: customer order, order line item, revenue record, CRM event,
  warehouse copy. Name the consumer: Finance reporting team. State the cadence:
  daily close, reporting at 06:00. State the staleness SLA for revenue records.
  Per R-06 append: "This SLA cannot be revised after Stage 1 is written."
  Stop. Do not write Stage 1 until [A-01] is done.

Step 2. Write [A-02] INCUMBENT BASELINE now.
  One paragraph. What did the team do before this pipeline? Use at least one
  entity name from [A-01]. You will cite this in [A-06] or [A-09].
  Stop. Then continue.

Step 3. Write STAGE 1 — CRM Source Extraction. [A-03]
  Schema in. Schema out. Transformation. Latency. Loss point (concrete — not
  "errors may occur"). Domain entity from [A-01].
  Stop. Do not write Stage 2 yet.

Step 4. Write BOUNDARY CHECK BC-1 now. [A-04]
  Per R-03, R-04, R-05:
    Boundary:                   CRM → Transformation
    Error handling:             [mechanism or "no handling — see [A-06]"]
    Domain entity at boundary:  [named entity from [A-01] — not "data" or "records"]
    Elapsed (cumul.):           [sum of Stage 1 latency only]
    Freshness verdict:          [FRESH | STALE vs [A-01] SLA]
  All five fields must be present. Tick them off mentally. Then write Stage 2.

Step 5. Write STAGE 2 — Transformation Layer. [A-03]
  Per R-03, you may write this now because BC-1 is complete.
  Schema in. Schema out. Note any field name or type change. Latency. Loss point.
  Domain entity from [A-01].
  Stop. Do not write Stage 3 yet.

Step 6. Write BOUNDARY CHECK BC-2 now. [A-04]
  Per R-03, R-04, R-05:
    Boundary:                   Transformation → Data Warehouse
    Error handling:             [mechanism or "no handling — see [A-06]"]
    Domain entity at boundary:  [named entity from [A-01] — not "data" or "records"]
    Elapsed (cumul.):           [sum of Stage 1 + BC-1 overhead + Stage 2 latency]
    Freshness verdict:          [FRESH | STALE vs [A-01] SLA]
  All five fields must be present. Then write Stage 3.

Step 7. Write STAGE 3 — Data Warehouse Load. [A-03]
  Schema in. Schema out. Latency. Loss point. Domain entity.
  Stop.

Step 8. Write [A-05] STALE ANALYSIS.
  Citing [A-04] for elapsed totals. Citing [A-01] for SLA.
  Row 1: normal-operation. Row 2: failure-mode (what if BC-1 retries 20 min?).
  Quantify at least one stale window. Address failure-mode separately.

Step 9. Write [A-06] RECOVERY PRESCRIPTIONS.
  Citing [A-03] loss points and [A-04] no-handling flags.
  One named recovery action per item. At least once cite [A-02]:
  "If [condition], fall back to [A-02]."

Step 10. Write [A-07] PHASE GATE — POST ROLE 1.
  Tick every item ✓ or mark ✗ with a note. Fix any ✗ before Role 2 begins.

    PHASE GATE — POST ROLE 1  [A-07]
    [ ] C-01: Unbroken source → destination chain across all three stages.
    [ ] C-02: Every boundary has an error handling annotation or "no handling."
    [ ] C-03: Every stage has a concrete loss point.
    [ ] C-04: Schema in and schema out present for every stage.
    [ ] R-03: BC-1 was completed before Stage 2; BC-2 completed before Stage 3.
    [ ] R-04: Elapsed (cumul.) computed inside BC-1 and BC-2.
    [ ] R-05: Freshness verdict FRESH or STALE in BC-1 and BC-2.
    [ ] R-06: Immutability statement present in [A-01].
    [ ] R-02: All citations use [A-xx] token form.

══════════════════════════════════════════
ROLE 2 — COMMERCE
══════════════════════════════════════════

Citing [A-01], [A-04]. Start with this Citing: line.

Step 1. Write [A-08] ENTITY AUDIT.
  For each boundary in [A-04], state the domain entity it named.
  Column check: was it a specific entity from [A-01], or a generic term like
  "data" or "records"? Mark pass or fail per boundary.

Step 2. Write [A-09] PATTERN TRADE-OFF.
  Name one alternative (e.g., event-driven CDC with Kafka).
  Two comparison dimensions with qualified or quantified values.
  Reference [A-02] as a baseline anchor.

══════════════════════════════════════════
ROLE 3 — FINANCE
══════════════════════════════════════════

Citing [A-01], [A-04], [A-05]. Start with this Citing: line.

Step 1. Write [A-10] FINANCE SIGN-OFF.
  State the Finance reporting cadence (06:00 pull). State the maximum acceptable
  data age. Compare against Elapsed (cumul.) from [A-04].
  State ACCEPTABLE or UNACCEPTABLE with one sentence of reasoning.
  Reference [A-05] failure-mode stale window by [A-xx] token.
```

---

## V-04 — Combined: Role Sequence (Finance-first) + Inertia Framing

**Axes:** Finance domain expert runs first and owns the staleness contract, incumbent baseline, and entity vocabulary before any trace begins. Operations traces the pipeline citing Finance's pre-declared framework. Commerce closes with validation and trade-off.

**Hypothesis:** When the staleness threshold and baseline originate in the first role (Finance) rather than the tracing role (Operations), the C-16 cross-role citation chain must carry a pre-declared value forward into the trace — stronger pressure on the C-13/C-17/C-16 conjunction than when the tracing role declares its own threshold.

---

```text
You are simulating three domain experts auditing a supply-chain sync pipeline for a
wholesale distributor. Inventory replenishment orders flow from a Demand Planning
System (DPS) through a Warehouse Management System (WMS) to an ERP Finance module.
Finance accruals run weekly (Monday 08:00). The business question: are inventory
positions current enough for accurate accrual?

Role order: Finance (contract authority) → Operations (pipeline tracer) → Commerce
(validation and trade-off). Finance runs first because the staleness contract and
incumbent baseline must be established before the trace begins.

══════════════════════════════════════════
ARTIFACT REGISTRY
══════════════════════════════════════════

Produce before any role output. Every citation target must be a row here.

| Token  | Artifact                      | Owner               | Description                                                           |
|--------|-------------------------------|---------------------|-----------------------------------------------------------------------|
| [A-01] | STALENESS CONTRACT            | Role 1 (Finance)    | Pre-declared SLA for inventory position freshness at accrual time     |
| [A-02] | INCUMBENT BASELINE            | Role 1 (Finance)    | Prior manual process for inventory reconciliation                     |
| [A-03] | DOMAIN CONTEXT                | Role 1 (Finance)    | Entity vocabulary, downstream consumer (Finance), cadence             |
| [A-04] | STAGE TRACE (Stages 1–3)      | Role 2 (Operations) | Lineage chain: schema, latency, loss points citing [A-03] vocabulary  |
| [A-05] | BOUNDARY CHECKS (BC-1, BC-2)  | Role 2 (Operations) | Inline boundary blocks: error handling, elapsed, verdict vs [A-01]    |
| [A-06] | STALE ANALYSIS                | Role 2 (Operations) | Stale windows derived from [A-05] elapsed totals vs [A-01] threshold  |
| [A-07] | RECOVERY PRESCRIPTIONS        | Role 2 (Operations) | Named recovery per loss point and no-handling flag; cites [A-02]      |
| [A-08] | PHASE GATE — POST ROLE 1      | Role 1 (Finance)    | Checklist confirming Finance deliverables before Operations begins     |
| [A-09] | PHASE GATE — POST ROLE 2      | Role 2 (Operations) | Checklist confirming trace deliverables before Commerce begins        |
| [A-10] | ENTITY EXPOSURE AUDIT         | Role 3 (Commerce)   | Per-boundary entity validation citing [A-05]                          |
| [A-11] | PATTERN TRADE-OFF             | Role 3 (Commerce)   | Named alternative pattern with ≥2 dimensions; cites [A-02]           |

══════════════════════════════════════════
STRUCTURAL CONSTRAINTS
══════════════════════════════════════════

SC-1  CITATION CONVENTION
      All artifact references use [A-xx] token form. Every role opens with
      "Citing: [A-xx], [A-xx]..." All references to prior outputs are by token.

SC-2  WRITE-ORDER GATE
      Stage N+1 may not be written until BOUNDARY CHECK BC-N is fully complete.
      Per SC-2: write BC-1 before Stage 2. Write BC-2 before Stage 3.

SC-3  ELAPSED ACCUMULATION
      Each BOUNDARY CHECK has "Elapsed (cumul.):" computed as running total of
      all prior stage and boundary latencies. Compute inside the block; do not
      defer to [A-06].

SC-4  FRESHNESS VERDICT
      Each BOUNDARY CHECK has "Freshness verdict: FRESH | STALE" comparing
      Elapsed (cumul.) to [A-01] threshold. Derive; do not assert.

SC-5  IMMUTABILITY
      [A-01] declares the staleness SLA before any stage is written. Once Role 2
      begins, that threshold is fixed. [A-01] must state: "This SLA is fixed. Role 2
      and Role 3 may not revise it."

══════════════════════════════════════════
ROLE 1 — FINANCE DOMAIN EXPERT
══════════════════════════════════════════

You are the Finance controller. Your job is to pre-declare the contract that all
downstream pipeline work must satisfy before the trace begins.

Step 1 — Write [A-03] DOMAIN CONTEXT.
  Lock entity vocabulary: replenishment order, inventory position, accrual entry,
  demand signal, WMS bin count. State downstream consumer (Finance accruals) and
  cadence (weekly Monday 08:00 close).

Step 2 — Write [A-01] STALENESS CONTRACT.
  Declare the SLA: "Inventory positions must be current within [N] hours of
  Monday 08:00 to be used in accruals."
  Per SC-5 append: "This SLA is fixed. Role 2 and Role 3 may not revise it."
  This is the threshold. Role 2's BOUNDARY CHECKs will be evaluated against it.

Step 3 — Write [A-02] INCUMBENT BASELINE.
  Describe the prior process: manual weekly inventory counts submitted by warehouse
  supervisors to Finance via spreadsheet. Surface at least two entity names from
  [A-03]. This baseline will be cited by [A-07] (recovery) or [A-11] (trade-off).

Step 4 — Produce [A-08] PHASE GATE — POST ROLE 1.
  Write this checklist. Tick ✓ or mark ✗. Operations may not begin until all ✓.

    PHASE GATE — POST ROLE 1  [A-08]
    [ ] SC-5: [A-01] contains the immutability statement naming Role 2 and Role 3.
    [ ] C-10: [A-03] names entity vocabulary, consumer, and cadence — all three fields.
    [ ] C-13: Staleness threshold is declared as an explicit SLA value in [A-01].
    [ ] C-15: [A-02] names at least two entities from [A-03] vocabulary.
    [ ] SC-1: All citations in Role 1 use [A-xx] token form.

══════════════════════════════════════════
ROLE 2 — OPERATIONS DOMAIN EXPERT
══════════════════════════════════════════

Citing [A-01] (SLA), [A-02] (baseline), [A-03] (entity vocabulary).

Step 1 — Write [A-04] STAGE TRACE.
  Stages: DPS Demand Signal → Warehouse Management System → ERP Finance Module.
  Use entity names from [A-03] verbatim. For each stage:

    STAGE N — [Name]
    Schema in:       [fields, types]
    Schema out:      [fields, types — note changes]
    Transformation:  [what this stage does]
    Latency:         [value or characterization]
    Loss point:      [one concrete scenario per stage]
    Domain entity:   [named entity from [A-03]]

  Apply SC-2: do not write Stage 2 until BC-1 is complete. Do not write Stage 3
  until BC-2 is complete.

  BOUNDARY CHECK BC-1 (DPS → WMS)  [A-05]
  Boundary:                   DPS → WMS handoff
  Error handling:             [mechanism or "no handling — see [A-07]"]
  Domain entity at boundary:  [named entity from [A-03]]
  Elapsed (cumul.):           [Per SC-3: Stage 1 latency only]
  Freshness verdict:          [Per SC-4: FRESH | STALE vs [A-01]]
  Citation:                   [A-05]

  BOUNDARY CHECK BC-2 (WMS → ERP Finance)  [A-05]
  [Same fields; Elapsed (cumul.) = Stage 1 + BC-1 overhead + Stage 2 latency]

Step 2 — Write [A-06] STALE ANALYSIS.
  Citing [A-05] for elapsed totals. Citing [A-01] for threshold.
  Normal-operation: use BC-2 Elapsed (cumul.) to determine stale window.
  Failure-mode: add a retry scenario; how much time does it add?

Step 3 — Write [A-07] RECOVERY PRESCRIPTIONS.
  Citing [A-04] (loss points) and [A-05] (no-handling flags).
  One specific recovery per item. Cite [A-02] at least once: "If recovery is
  not possible, revert to [A-02] manual count submission."

Step 4 — Produce [A-09] PHASE GATE — POST ROLE 2.
  Tick ✓ or mark ✗. Commerce may not begin until all ✓.

    PHASE GATE — POST ROLE 2  [A-09]
    [ ] C-01: Unbroken source → destination chain across all stages in [A-04].
    [ ] C-02: Every boundary in [A-05] has an error handling annotation.
    [ ] C-03: Every stage in [A-04] has a concrete loss point.
    [ ] C-04: Schema in and schema out present and differentiated for every stage.
    [ ] SC-2: BC-1 precedes Stage 2 in the output; BC-2 precedes Stage 3.
    [ ] SC-3: Elapsed (cumul.) computed inside BC-1 and BC-2.
    [ ] SC-4: Freshness verdict FRESH or STALE in BC-1 and BC-2.
    [ ] C-16: [A-06] and [A-07] cite [A-01], [A-02], [A-03] using [A-xx] tokens.
    [ ] C-15: [A-02] cited in [A-07] closing the baseline loop.

══════════════════════════════════════════
ROLE 3 — COMMERCE DOMAIN EXPERT
══════════════════════════════════════════

Citing [A-01] (SLA), [A-03] (entities), [A-05] (boundary checks).

Step 1 — Write [A-10] ENTITY EXPOSURE AUDIT.
  For each boundary in [A-05], confirm the domain entity named is from [A-03]
  vocabulary.

  | Boundary | Entity named | In [A-03]? | Pass/Fail |
  |----|----|----|---|

Step 2 — Write [A-11] PATTERN TRADE-OFF.
  Name one alternative pipeline pattern.
  Compare on at least two dimensions. Include [A-02] as one comparison anchor.
  Reference [A-01] threshold as a dimension (does the alternative meet the SLA?).

Step 3 — Write FINAL VERDICT (3 sentences).
  Citing [A-01], [A-06], [A-07]: does this pipeline satisfy the Finance accrual SLA?
```

---

## V-05 — Combined: Output Format (table throughout) + Lifecycle Emphasis (explicit phase model)

**Axes:** Explicit PHASE 0–4 model with named phase labels, entry prerequisites, and required deliverables. Every pipeline artifact rendered in table format. Multiple phase gate checklists (one per major phase transition). Tests whether the phase model plus table format carries all 24 criteria while creating a more granular C-23 compliance surface.

**Hypothesis:** A named phase model with required deliverables per phase makes C-23 checklist placement non-arbitrary — each gate is attached to a named phase boundary with a defined set of fields it must verify, reducing ambiguity about what "before next phase" means.

---

```text
You are simulating three domain experts auditing a Commerce-to-Finance data pipeline
for a subscription services company. Customer entitlement records flow from a Billing
System through an Entitlement Sync Engine to a Revenue Recognition module. Revenue
recognition runs at month-end close. The business question: are entitlement positions
current enough for accurate revenue recognition?

Roles: Operations (pipeline authority), Commerce (entity validator), Finance (close authority).
Lifecycle: PHASE 0 (setup) → PHASE 1 (contract) → PHASE 2 (trace) → PHASE 3 (analysis)
→ PHASE 4 (closure). Each phase has explicit prerequisites and deliverables.

══════════════════════════════════════════
PHASE 0 — SETUP
(Prerequisite: none. Deliverables: ARTIFACT REGISTRY, STRUCTURAL CONSTRAINTS.)
══════════════════════════════════════════

Produce both artifacts before PHASE 1 begins.

────────────────────────────────────────
ARTIFACT REGISTRY
────────────────────────────────────────

| Token  | Artifact                      | Owner               | Description                                                            |
|--------|-------------------------------|---------------------|------------------------------------------------------------------------|
| [A-01] | DOMAIN CONTEXT                | Role 1 (Operations) | Entity vocabulary, consumer, cadence, staleness SLA                    |
| [A-02] | INCUMBENT BASELINE            | Role 1 (Operations) | Prior manual process for entitlement reconciliation                    |
| [A-03] | LINEAGE TABLE                 | Role 1 (Operations) | Stage rows + inline boundary rows (all fields in columns)              |
| [A-04] | STALE ANALYSIS TABLE          | Role 1 (Operations) | Normal and failure-mode stale windows vs [A-01] SLA                   |
| [A-05] | RECOVERY TABLE                | Role 1 (Operations) | Named recovery per loss point and no-handling flag                     |
| [A-06] | PHASE 2 GATE                  | Role 1 (Operations) | Checklist gating PHASE 3 entry                                         |
| [A-07] | ENTITY VALIDATION TABLE       | Role 2 (Commerce)   | Per-boundary entity audit citing [A-03]                                |
| [A-08] | PATTERN TRADE-OFF TABLE       | Role 2 (Commerce)   | Named alternative vs this pipeline vs [A-02] on ≥2 dimensions         |
| [A-09] | PHASE 3 GATE                  | Role 2 (Commerce)   | Checklist gating PHASE 4 entry                                         |
| [A-10] | THRESHOLD RATIFICATION        | Role 3 (Finance)    | Finance month-end close sign-off on [A-01] SLA vs [A-04] windows      |

────────────────────────────────────────
STRUCTURAL CONSTRAINTS
────────────────────────────────────────

SC-1  CITATION CONVENTION
      All artifact references use [A-xx] token form. Every role, phase, and section
      that references prior output opens with "Citing: [A-xx], ..." using token form.

SC-2  WRITE-ORDER GATE
      Per SC-2: the BOUNDARY row for BC-N in [A-03] must be complete before the
      Stage N+1 row may be added. A Stage N+1 row written before its preceding
      boundary row is fully populated does not pass.

SC-3  ELAPSED ACCUMULATION
      The "Elapsed (cumul.)" column in each boundary row of [A-03] is computed as the
      running total of all prior stage latencies plus boundary overhead. Fill this
      cell inside the boundary row. Per SC-3: do not defer it to [A-04].

SC-4  FRESHNESS VERDICT
      Each boundary row in [A-03] must contain "FRESH" or "STALE" in the Freshness
      verdict column, derived by comparing Elapsed (cumul.) against [A-01] SLA.
      Per SC-4: a boundary row that has Elapsed (cumul.) but no verdict does not pass.

SC-5  IMMUTABILITY
      The SLA declared in [A-01] is fixed once PHASE 2 begins. Append to [A-01]:
      "This SLA is fixed. It may not be revised in PHASE 2 or later."

══════════════════════════════════════════
PHASE 1 — CONTRACT
(Prerequisite: PHASE 0 complete. Deliverables: [A-01], [A-02]. Owner: Operations.)
══════════════════════════════════════════

Step 1 — Write [A-01] DOMAIN CONTEXT.
  Produce a table:

  | Field            | Value                                                        |
  |------------------|--------------------------------------------------------------|
  | Entities         | [list: entitlement record, subscription tier, billing event, |
  |                  |  revenue line item, recognition date]                        |
  | Downstream       | Finance Revenue Recognition team                             |
  | Cadence          | Month-end close, last business day of month                  |
  | Staleness SLA    | Entitlement records must be current within [N] hours of      |
  |                  | month-end close timestamp                                    |
  | Immutability     | This SLA is fixed. It may not be revised in PHASE 2 or later.|

  Per SC-5: the Immutability row is required.

Step 2 — Write [A-02] INCUMBENT BASELINE.
  Produce a table:

  | Field                | Value                                          |
  |----------------------|------------------------------------------------|
  | Prior process        | [describe manual reconciliation process]       |
  | Entities surfaced    | [at least two from [A-01] entity list]         |
  | Cadence              | [how often it ran]                             |
  | Known limitation     | [one concrete failure mode of the prior process]|

  [A-02] will be cited in [A-05] (recovery) or [A-08] (trade-off) to close the loop.

══════════════════════════════════════════
PHASE 2 — TRACE
(Prerequisite: [A-01] and [A-02] complete. Deliverables: [A-03]. Owner: Operations.)
══════════════════════════════════════════

Write [A-03] LINEAGE TABLE.
Columns:

| Row type | Stage/Boundary | Schema in | Schema out | Transformation | Latency | Loss point | Domain entity | Error handling | Elapsed (cumul.) | Freshness verdict |

Row types:
- STAGE rows: fill Stage/Boundary through Domain entity; leave Error handling,
  Elapsed (cumul.), Freshness verdict as "—".
- BOUNDARY rows: fill Stage/Boundary (e.g., "BC-1"), Error handling, Domain entity,
  Elapsed (cumul.) [Per SC-3], Freshness verdict [Per SC-4]; leave schema/transformation/
  latency/loss point as "—".

Apply SC-2: insert the BC-1 boundary row before the Stage 2 row. Insert the BC-2
boundary row before the Stage 3 row. Per SC-2, a stage row written before its
preceding boundary row is populated does not pass.

Required rows in order:
  STAGE 1 — Billing System Export
  [BC-1 boundary row — complete before Stage 2]
  STAGE 2 — Entitlement Sync Engine
  [BC-2 boundary row — complete before Stage 3]
  STAGE 3 — Revenue Recognition Module

Domain entity column: named entity from [A-01] — not "data" or "records."

Produce [A-06] PHASE 2 GATE before PHASE 3 begins.
Tick ✓ or mark ✗. Fix any ✗. PHASE 3 may not begin until all ✓.

  PHASE 2 GATE  [A-06]
  [ ] C-01: [A-03] STAGE rows form an unbroken chain from Billing System to Revenue Rec.
  [ ] C-02: Every boundary row has a non-blank Error handling cell.
  [ ] C-03: Every STAGE row has a concrete Loss point cell.
  [ ] C-04: Every STAGE row has distinct Schema in and Schema out; changes noted.
  [ ] SC-2: BC-1 row precedes Stage 2 row; BC-2 row precedes Stage 3 row.
  [ ] SC-3: Elapsed (cumul.) cell computed in BC-1 and BC-2 boundary rows.
  [ ] SC-4: Freshness verdict cell is FRESH or STALE in BC-1 and BC-2 rows.
  [ ] SC-5: [A-01] Immutability row is present.
  [ ] SC-1: All citations use [A-xx] token form.

══════════════════════════════════════════
PHASE 3 — ANALYSIS
(Prerequisite: [A-06] all ✓. Deliverables: [A-04], [A-05]. Owner: Operations.)
══════════════════════════════════════════

Step 1 — Write [A-04] STALE ANALYSIS TABLE.
  Citing [A-03] (elapsed values), [A-01] (SLA threshold).

  | Scenario       | Elapsed (cumul.) | SLA threshold | Stale? | Note                 |
  |----------------|-----------------|---------------|--------|----------------------|
  | Normal ops     | [from BC-2]     | [from [A-01]] | Y/N    |                      |
  | Failure mode   | [+ retry time]  | [from [A-01]] | Y/N    | [describe scenario]  |

  Normal-operation and failure-mode rows must be distinct.

Step 2 — Write [A-05] RECOVERY TABLE.
  Citing [A-03] (loss points and no-handling flags).

  | Source                     | Recovery mechanism                         | References |
  |----------------------------|--------------------------------------------|------------|
  | [Loss point from Stage N]  | [specific named mechanism]                 | [A-03]     |
  | [No-handling in BC-N]      | [specific named remedy]                    | [A-03]     |
  | [At least one row]         | Fall back to [A-02] if [condition]         | [A-02]     |

══════════════════════════════════════════
PHASE 4 — CLOSURE
(Prerequisite: produce [A-09] PHASE 3 GATE, then Commerce and Finance roles run.)
══════════════════════════════════════════

Before Commerce begins, Operations produces [A-09] PHASE 3 GATE.
Tick ✓ or mark ✗. Fix any ✗. Commerce may not begin until all ✓.

  PHASE 3 GATE  [A-09]
  [ ] C-06: [A-04] has at least one quantified stale window; failure-mode row present.
  [ ] C-08: [A-05] has a recovery prescription for every loss point and no-handling flag.
  [ ] C-14: [A-04] stale window traces numerically to Elapsed (cumul.) in [A-03].
  [ ] C-15: [A-02] cited in [A-05] closing the baseline reference loop.
  [ ] SC-1: All citations in [A-04] and [A-05] use [A-xx] token form.

────────────────────────────────────────
ROLE 2 — COMMERCE (runs in PHASE 4)
────────────────────────────────────────

Citing [A-01] (entities), [A-03] (lineage table).

Step 1 — Write [A-07] ENTITY VALIDATION TABLE.

  | Boundary | Entity in [A-03] Domain entity cell | In [A-01] vocabulary? | Pass/Fail |
  |----|----|----|---|

Step 2 — Write [A-08] PATTERN TRADE-OFF TABLE.
  Citing [A-02] (incumbent), [A-01] (SLA).

  | Dimension                  | This pipeline | [Alternative name] | [A-02] incumbent |
  |------|------|------|---|

  At least two dimension rows. Include whether the alternative meets [A-01] SLA.

────────────────────────────────────────
ROLE 3 — FINANCE (runs in PHASE 4, after Commerce)
────────────────────────────────────────

Citing [A-01] (SLA), [A-03] (lineage), [A-04] (stale analysis).

Step 1 — Write [A-10] THRESHOLD RATIFICATION.

  | Field                    | Value                                                        |
  |--------------------------|--------------------------------------------------------------|
  | Finance close constraint | [max acceptable data age at month-end]                      |
  | Elapsed (cumul.) in [A-03] | [from BC-2]                                               |
  | [A-04] stale verdict     | [normal-ops: FRESH or STALE]                                |
  | Finance verdict          | ACCEPTABLE or UNACCEPTABLE                                  |
  | Bottleneck (if UNACCEPT) | [which stage or boundary drives the exceedance]             |
```

---

## Variation Summary

| Variation | Axis | Key C-22 mechanism | Key C-23 mechanism | Key C-24 mechanism |
|---|---|---|---|---|
| V-01 | Role Sequence (Commerce-first) | 10-row ARTIFACT REGISTRY with token/owner/description before roles | [A-09] + [A-10] checklists with named criterion per item, ticked inline | STRUCTURAL CONSTRAINTS with SC-1–SC-5; every role instruction references by ID |
| V-02 | Output Format (unified table) | 8-row ARTIFACT REGISTRY; table format makes token columns visually scannable | [A-06] PHASE GATE checklist with column-presence items (e.g., "Every BC row has Freshness verdict cell") | STRUCTURAL CONSTRAINTS SC-1–SC-5; column-presence language in role instructions |
| V-03 | Phrasing Register (directive) | 10-row ARTIFACT REGISTRY TABLE as explicit separate section before any role | [A-07] PHASE GATE with "Stop. Tick. Fix. Then continue." framing | PROTOCOL RULES R-01–R-07; inline callbacks: "Per R-03", "Per R-04", "Per R-05" at every enforcement point |
| V-04 | Role Seq + Inertia Framing | 11-row registry; Finance-owned [A-01]/[A-02]/[A-03] rows make contract artifacts first-class before any trace rows | [A-08] + [A-09] checklists; [A-08] verifies Finance contract deliverables; [A-09] verifies trace deliverables | STRUCTURAL CONSTRAINTS SC-1–SC-5; role instructions use "Apply SC-2", "Per SC-3", "Per SC-4" uniformly |
| V-05 | Output Format + Lifecycle Emphasis | 10-row registry in PHASE 0; table-format artifacts make all tokens column-verifiable | [A-06] PHASE 2 GATE + [A-09] PHASE 3 GATE; two checkpoints at named phase boundaries | STRUCTURAL CONSTRAINTS in PHASE 0; each phase instruction annotates: "Per SC-2:", "Per SC-3:", "Per SC-4:" at every use |

**C-22 differentiator across variations:** All five produce a formal registry table with token/owner/description columns before any role output — satisfying C-22's strictly-stronger requirement over C-19. Variations differ in table row count and which roles own which artifacts.

**C-23 differentiator across variations:** V-01 and V-04 have two checklist gates (one per role boundary). V-05 has two gates at named phase boundaries. V-02 has one post-trace gate. V-03 has one post-Role-1 gate with directive framing. All produce inline ticked checklists referencing named criteria — not post-hoc audits.

**C-24 differentiator across variations:** V-03 uses `R-NN` identifiers (Protocol Rules register) vs V-01/V-02/V-04/V-05 which use `SC-N` identifiers (Structural Constraints). All five include both the upfront declaration section and inline callbacks at every enforcement point, satisfying the two-level requirement.
