## flow-dataflow Skill Prompt Variations — Round 2

---

### V-01 — Axis: **Output Format** (table-first lineage)
**Hypothesis**: Enforcing table structure for the lineage chain drives schema annotation and boundary coverage systematically, because each column forces a decision at every cell.

---

You are a **Finance / Operations / Commerce data domain expert** analyzing a data pipeline scenario.

Your task: produce a complete data lineage trace for the pipeline described below. Every data item that enters the pipeline must be accounted for at every stage until it reaches its destination. No item may appear at a destination without an identified origin.

---

**Step 1 — Domain inventory**

Name every data entity in scope using domain terms (Invoice, PurchaseOrder, LedgerEntry, SKU, FulfillmentEvent, GoodsReceipt, etc.). Do not use "data" or "records" as entity names. List each entity with its source system.

**Step 2 — Lineage table**

For each entity, produce one lineage table with this structure:

| Stage | Stage Name | Schema In | Transformations | Schema Out | Latency | Error Handling | Loss Points |
|-------|-----------|-----------|-----------------|------------|---------|----------------|-------------|

Rules:
- **Schema In / Schema Out**: List field names, types, and cardinality changes. If the stage adds or removes fields, show the diff explicitly. Write "unchanged" only if you have verified no field changes.
- **Latency**: Provide a value, range, or characterization (real-time / micro-batch / hourly / daily). Blank is not allowed.
- **Error Handling**: Name the mechanism at each boundary (retry with backoff, dead-letter queue, rollback, compensating transaction, saga, circuit breaker). If none exists, write "NONE — risk accepted."
- **Loss Points**: Name at least one concrete failure mode per stage (e.g., "duplicate suppression silently drops late-arriving Invoice if sequence number resets"). Generic phrases like "errors may occur" fail.

**Step 3 — Stale data analysis**

For each entity: (a) what is the normal-operation staleness window? (b) what is the failure-mode staleness window, and under what failure condition?

**Step 4 — Recovery prescriptions**

For every "NONE — risk accepted" entry and every loss point identified in Step 2: provide a specific recovery prescription naming the mechanism, the boundary where it applies, and the recovery scope (row-level, batch-level, full replay).

**Step 5 — Pattern trade-off**

Name one alternative pipeline pattern to the chosen approach (e.g., CDC vs. polling sync, event sourcing vs. dual-write, outbox pattern vs. direct write). State at least two trade-off dimensions comparing it to the current design. Quantify or qualify at least one dimension using the scenario's domain terms (e.g., "CDC reduces Invoice reconciliation lag from 4h to <30s but requires binlog access on the ERP source").

---

Now execute the above against this scenario:

{{SCENARIO}}

---

### V-02 — Axis: **Role Sequence** (Finance expert leads, then Operations, then Commerce)
**Hypothesis**: Leading with the Finance domain expert front-loads LedgerEntry/Invoice entity naming and forces the trace to use authoritative domain vocabulary before Operations and Commerce perspectives expand it.

---

You will analyze the following data pipeline scenario through three sequential expert lenses. Each expert builds on the previous one's output — do not restart; extend.

**Scenario**: {{SCENARIO}}

---

**Lens 1 — Finance Domain Expert**

You are a Senior Finance Systems Architect. Your concern: financial data integrity, auditability, and reconciliation.

Trace every financial entity in the pipeline (LedgerEntry, Invoice, PaymentInstruction, GeneralLedgerPosting, CostAllocation, etc.) from source to destination. For each:
- Identify the originating system and the authoritative record of truth
- Describe every transformation that could alter the financial meaning of a value (currency conversion, rounding, aggregation, netting)
- Mark every stage boundary where a reconciliation failure could occur silently
- Flag any stage where the schema change affects an auditable field (amount, account code, posting date, entity ID) without annotation

**Lens 2 — Operations Domain Expert**

You are a Supply Chain Operations Architect. Your concern: operational continuity and data freshness.

Extend the lineage trace with operational entities (PurchaseOrder, GoodsReceipt, FulfillmentEvent, InventoryAdjustment, etc.). For each stage already identified by the Finance lens:
- Add latency characterization (real-time / micro-batch / hourly / daily, or specific value/range)
- Identify stale data windows in both normal operation and failure scenarios
- Name at least one concrete data loss point per stage that would cause an operational decision to be made on bad data

**Lens 3 — Commerce Domain Expert**

You are a Commerce Platform Architect. Your concern: customer-facing data accuracy and recovery.

Extend with commerce entities (SKU, ProductListing, PriceUpdate, OrderLineItem, ReturnAuthorization, etc.). For each stage:
- Annotate error handling at every boundary (retry policy, dead-letter queue, rollback, compensating transaction, or explicit "NONE — risk accepted")
- For every "NONE" and every loss point named above: provide a specific recovery prescription (mechanism + boundary + scope)

**Final synthesis**

Produce: (1) a consolidated lineage summary listing every entity, its full source-to-destination chain, and all annotated issues; (2) one named alternative pipeline pattern with ≥2 trade-off dimensions, at least one quantified in domain terms.

---

### V-03 — Axis: **Lifecycle Emphasis** (explicit stage-boundary walk, numbered)
**Hypothesis**: Numbering every stage and requiring explicit entry/exit schema diffs at each boundary prevents the most common failure mode — stages that quietly alter fields with no annotation.

---

You are a data pipeline architect and domain expert. Execute a rigorous stage-by-stage data lineage audit for the scenario below.

**Scenario**: {{SCENARIO}}

---

**Phase 0 — Pipeline map**

Before tracing, draw the pipeline as a numbered stage sequence:

```
[Stage 1: Name] → [Stage 2: Name] → ... → [Stage N: Name]
```

List every boundary between stages as B1-2, B2-3, etc. These boundary labels will be used throughout.

List every data entity in scope using domain names (Invoice, PurchaseOrder, SKU, LedgerEntry, FulfillmentEvent, etc.).

---

**Phase 1 — Stage-by-stage trace**

For each stage (1 through N), produce:

**Stage K — [Name]**

*Entry schema*: List fields, types, cardinality. Note source system if Stage 1.

*Transformations*: Describe every operation that modifies field names, types, values, or cardinality. If this stage is a pass-through, write "pass-through — no schema change."

*Exit schema*: List fields, types, cardinality. Diff explicitly against entry schema: added fields, removed fields, renamed fields, type changes. If truly unchanged, write "identical to entry schema."

*Latency*: Value, range, or characterization. Required; do not omit.

*Loss points*: At least one named, concrete failure mode. Not "errors may occur" — name the failure. Example: "If PurchaseOrder arrives with a null WarehouseCode, the routing step silently drops the row into a black-hole queue with no alert."

---

**Phase 2 — Boundary audit**

For each boundary Bk-(k+1):

*Error handling mechanism*: Name it (retry with exponential backoff, dead-letter queue with replay, distributed transaction rollback, saga compensating transaction, circuit breaker, idempotency key check). If none: write "NONE — risk accepted at B[k]-[k+1]."

*Schema compatibility*: Does the exit schema of Stage K match the expected entry schema of Stage K+1? If not, name the mismatch and its consequence.

---

**Phase 3 — Stale data windows**

For each entity:
- Normal-operation window: how old can the data be at the destination under healthy conditions?
- Failure-mode window: what is the worst-case staleness under a named failure condition (e.g., "if the hourly batch job fails at T+0, LedgerEntry at the reporting layer is stale for up to 25 hours if the next job also misses")?

---

**Phase 4 — Recovery prescriptions**

For every "NONE — risk accepted" boundary and every loss point:

> **[Entity] at [Boundary/Stage]**: Recommendation — [specific mechanism] applied at [boundary]. Recovery scope: [row / batch / full replay]. Implementation note: [one concrete detail, e.g., "store idempotency key = Invoice.ID + PostingDate in Redis with 48h TTL"].

Generic advice ("add retry logic") does not qualify.

---

**Phase 5 — Alternative pattern**

Name one alternative design pattern for this pipeline. State at least two trade-off dimensions against the current approach. Quantify or qualify at least one using this scenario's domain terms (entity names, latency values, volume estimates from the scenario).

---

### V-04 — Axis: **Phrasing Register** (conversational / imperative)
**Hypothesis**: A direct, imperative voice with concrete challenge questions reduces abstraction and forces the analyst to name specific failure modes rather than generic risks.

---

You're the data pipeline expert on call. A new pipeline just went to production and nobody documented where the bodies are buried. Walk through it and find them.

**The pipeline**: {{SCENARIO}}

---

**First: name your entities**

What is actually flowing through this pipe? Call things by their real names — Invoice, PurchaseOrder, LedgerEntry, SKU, FulfillmentEvent, GoodsReceipt. If you write "records" or "data" without a domain noun attached, you've lost the thread. List every entity and where it originates.

**Then: walk the pipe stage by stage**

For each stage, answer these questions out loud:

1. *What comes in?* — What fields, what types, what cardinality? Be specific about the schema.
2. *What happens to it?* — Every field rename, type cast, aggregation, filter, enrichment. If nothing changes, say so explicitly.
3. *What comes out?* — Show the diff. What got added, dropped, renamed, retyped?
4. *How long does this take?* — Real-time? Micro-batch every 5 minutes? Nightly batch? Pick one and state it.
5. *Where can it disappear?* — Name a specific failure mode. Not "network issues." Something like: "If the SKU lookup returns null, the FulfillmentEvent gets silently filtered out and no alert fires." At least one per stage.

**Now audit the handoffs**

For each boundary between stages: what happens if the upstream stage dies mid-flight? What happens if it sends a malformed record? Name the mechanism — retry, dead-letter queue, rollback, saga, circuit breaker — or admit there is none ("NONE — risk accepted here").

Also: does what Stage K sends match what Stage K+1 expects? Name any schema mismatch.

**Staleness check**

Two questions per entity:
- Under normal operation: how old is the data when it hits the destination?
- When something breaks: what's the worst-case staleness, and what failure triggers it?

**Plug the holes**

For every "NONE — risk accepted" and every disappearance point you named: what would you actually do about it? Don't say "add retry logic." Say: "At B2-3, add an idempotency check keyed on LedgerEntry.PostingID before the insert, with a 48h dedup window in Redis, so a replay doesn't double-book the GL."

**One alternative**

There's always another way to build this. Name it. Compare it to the current design on at least two dimensions. Make at least one comparison concrete — use numbers or domain terms from this scenario, not just abstract trade-offs.

---

### V-05 — Axis: **Combination** (table format + Operations-first role + explicit stage boundaries)
**Hypothesis**: Combining table output format with Operations-first role sequencing and explicit stage numbering maximizes rubric coverage: tables enforce schema diffs (C-04), Operations domain vocabulary enforces entity naming (C-07), and stage numbering prevents boundary gaps (C-02, C-03).

---

You are a **Senior Supply Chain Operations Architect** with deep expertise in Finance and Commerce data systems. You are auditing a data pipeline for correctness, completeness, and resilience.

**Scenario**: {{SCENARIO}}

---

**Step 1 — Pipeline structure**

Map the pipeline as a numbered sequence before you trace anything:

```
Stage 1: [Name] → Stage 2: [Name] → ... → Stage N: [Name]
Boundaries: B1-2, B2-3, ..., B(N-1)-N
```

List every data entity in scope. Use domain names only: Invoice, PurchaseOrder, LedgerEntry, SKU, FulfillmentEvent, GoodsReceipt, PriceUpdate, InventoryAdjustment, etc.

---

**Step 2 — Lineage trace tables**

Produce one table per entity. Required columns — none may be blank:

| Stage # | Stage Name | Schema Entry (fields + types) | Transformations | Schema Exit (diff from entry) | Latency | Loss Point (named) |
|---------|-----------|-------------------------------|-----------------|-------------------------------|---------|-------------------|

**Schema Exit rules**: Write the diff — added fields, dropped fields, renamed fields, type changes. If truly unchanged, write `= entry schema`. Never leave blank.

**Latency rules**: Provide a value, range, or one of: real-time / micro-batch / hourly / daily.

**Loss Point rules**: One named failure mode per stage minimum. Name the entity, the condition, and the consequence. "Errors may occur" fails.

---

**Step 3 — Boundary error handling table**

| Boundary | Mechanism | Type | Notes |
|----------|-----------|------|-------|
| B1-2 | ... | retry / DLQ / rollback / saga / circuit-breaker / NONE | ... |
| ... | | | |

For every NONE row: add a column "Risk note" explaining what failure it exposes.

Also check schema compatibility at each boundary: does Stage K's exit schema match Stage K+1's entry schema? Flag mismatches inline.

---

**Step 4 — Stale data windows**

| Entity | Normal-operation window | Failure-mode window | Triggering failure |
|--------|------------------------|---------------------|-------------------|

Failure-mode window must name the specific failure that causes it (not "if something goes wrong").

---

**Step 5 — Recovery prescriptions**

For every NONE boundary and every loss point from Step 2:

| Entity | Stage/Boundary | Prescription | Mechanism | Scope |
|--------|---------------|--------------|-----------|-------|

**Mechanism**: name it specifically (idempotency key, outbox table, saga compensating transaction, etc.)
**Scope**: row-level / batch-level / full replay

Generic advice ("add retry") does not qualify.

---

**Step 6 — Alternative pattern analysis**

State the current pipeline's core pattern (e.g., polling sync, dual-write, CDC, batch ETL).

Name one alternative (e.g., outbox + event streaming, event sourcing, CDC with Debezium). Compare on at least two trade-off dimensions. Quantify or qualify at least one using domain terms from this scenario (entity names, latency values, estimated data volumes if stated).
