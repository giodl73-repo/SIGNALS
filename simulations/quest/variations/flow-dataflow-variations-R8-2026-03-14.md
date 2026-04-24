alternative; cites [A-02] and [A-03] by token |
| [A-16] | PHASE GATE CHECK — Role 3 | Role 3 | Final self-verification checklist |

---

### STRUCTURAL CONSTRAINTS

| ID | Constraint |
|----|-----------|
| SC-1 | **Citation tokens**: every handoff target cited uses its `[A-xx]` token. |
| SC-2 | **Stage-write gate**: Stage N+1 may not be written until the BOUNDARY CHECK between Stage N and Stage N+1 is complete with all seven named columns populated. Do not write Stage N+1 until this block is complete. |
| SC-3 | **SLA immutability**: [A-02] is fixed after Role 1, Stage 1. This threshold is fixed. You may not revise [A-02] after Stage 1 of Role 1. |
| SC-4 | **Incremental elapsed**: `Elapsed (cumul.)` = sum of all prior stage and boundary durations, computed incrementally as a named column field. |
| SC-5 | **Freshness verdict**: each `Verdict` column contains `FRESH` or `STALE` derived from comparison against [A-02]. |
| SC-6 | **Citation-opening rule**: every role after Role 1 opens its DOMAIN CONTEXT with `Citing:` naming specific `[A-xx]` tokens including ≥1 from a non-adjacent prior role. |
| SC-7 | **Boundary block schema**: every BOUNDARY CHECK is a Markdown table with exactly seven named columns as specified below. A block missing any column fails. |
| SC-8 | **Required TRADE-OFF ANALYSIS**: [A-15] is a required named section. ≥1 alternative, ≥2 dimensions, cites [A-02] and [A-03] by token. Apply SC-8 when producing [A-15]. |
| SC-9 | **Incumbent column sourcing**: every `Incumbent Equiv.` cell derives its value from [A-03]. A cell that estimates an incumbent duration without citing [A-03] is a protocol violation. |

---

### BOUNDARY BLOCK SCHEMA (SC-7) — Seven-Column Form

The `Incumbent Equiv.` column is the inertia-framing innovation. At every boundary the pipeline's automated elapsed is placed beside the manual-process equivalent, making the status-quo competitor structurally present in the audit trail — not deferred to trade-off analysis.

| Column | Required content |
|--------|-----------------|
| `Entity` | Named entity from scenario vocabulary |
| `Elapsed (cumul.)` | Running sum of all prior stage and boundary durations |
| `Verdict` | `FRESH` or `STALE` — derived from [A-02] |
| `Error Handling` | Named mechanism or `NONE — see [A-14]` |
| `Schema Delta` | Named field changes at this boundary, or `NONE` |
| `Data Loss Flag` | `YES — [named loss point]` or `NO` |
| `Incumbent Equiv.` | Time the equivalent manual step from [A-03] would require (e.g., `manual batch: 4 hr`) — cite [A-03] |

---

### SCENARIO

**Domain:** Retail e-commerce order-to-cash.
**Role sequence:** Finance → Operations → Commerce *(non-natural; natural order is Commerce → Operations → Finance).*

Finance runs first and anchors [A-02] (GL posting freshness SLA) and [A-03] (manual GL reconciliation baseline). Operations must cite [A-02] rather than declaring an inventory-specific threshold. Commerce must cite tokens from both non-adjacent predecessors and carries the highest incumbent-comparison burden in trade-off analysis.

The `Incumbent Equiv.` column in every boundary block makes [A-03] visible at every gate, not just in the closing analysis.

Each role traces four stages: (1) event / CDC extraction, (2) landing / staging, (3) transformation / enrichment, (4) target load.

---

### ROLE 1 — FINANCE DATA DOMAIN EXPERT

**Scenario:** Revenue Journal Entry pipeline — order events to general ledger.

**[A-01] DOMAIN CONTEXT** — Produce before Stage 1. Declare: entity (Revenue Journal Entry), downstream consumer (GL system), business cadence. ≥2 terms reappear in subsequent lineage.

**[A-02] STALE SLA CONTRACT** — Numeric stale threshold for Revenue Journal Entry (maximum age from order event to GL posting). State: *"This threshold is fixed. You may not revise [A-02] after Stage 1 of Role 1."* [SC-3 activates.]

**[A-03] INCUMBENT BASELINE** — Describe the manual GL reconciliation process this pipeline replaces. For each manual step, record its typical duration — these durations are the source values for every `Incumbent Equiv.` cell across all three roles. Include ≥1 term from [A-01]. Must be cited by token in [A-14] and [A-15].

**[A-04] LINEAGE TRACE — Finance** — *[Apply SC-2 at every boundary.]*

**Stage 1: Order Event Extraction**

**[A-05] BOUNDARY CHECK: Stage 1 → Stage 2** *[SC-7: seven columns | SC-4 | SC-5 vs [A-02] | SC-9: Incumbent Equiv. from [A-03] | SC-2: Stage 2 blocked]*

| Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv. |
|--------|-----------------|---------|----------------|-------------|----------------|-----------------|
| | | | | | | [A-03]: |

**Stage 2: Landing Zone**

**[A-05] BOUNDARY CHECK: Stage 2 → Stage 3** *[SC-7 | SC-4 | SC-5 | SC-9]*

| Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv. |
|--------|-----------------|---------|----------------|-------------|----------------|-----------------|
| | | | | | | [A-03]: |

**Stage 3: Revenue Recognition Rule Application**

**[A-05] BOUNDARY CHECK: Stage 3 → Stage 4** *[SC-7 | SC-4 | SC-5 | SC-9]*

| Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv. |
|--------|-----------------|---------|----------------|-------------|----------------|-----------------|
| | | | | | | [A-03]: |

**Stage 4: General Ledger Load**

**[A-06] PHASE GATE CHECK — Role 1** — *Produce and tick. Role 2 may not begin until all items are checked.*

- [ ] [A-02] declares a numeric threshold with explicit lock statement
- [ ] [A-03] records per-step manual durations that downstream roles can reference for `Incumbent Equiv.`
- [ ] Every BOUNDARY CHECK has all seven columns populated
- [ ] Every `Incumbent Equiv.` cell cites [A-03] by token
- [ ] Every Verdict is FRESH or STALE derived from [A-02]
- [ ] Every Data Loss Flag is `YES — [named point]` or `NO`
- [ ] Schema Delta is named or NONE — not blank

---

### ROLE 2 — OPERATIONS DATA DOMAIN EXPERT

**Scenario:** Inventory Position sync from WMS to demand-planning analytics warehouse.

**[A-07] DOMAIN CONTEXT** — *[SC-6: Open with `Citing: [A-02]` and [A-03].]*

**Citing:** [A-02] (Finance's STALE SLA CONTRACT — threshold = [value]), [A-03] (Finance's INCUMBENT BASELINE — source for `Incumbent Equiv.` values)

Declare entity (Inventory Position), consumer, cadence. [SC-3: use [A-02] for all Verdict fields.]

**[A-08] LINEAGE TRACE — Operations** — *[Apply SC-2.]* Four stages: CDC Extraction from WMS, Landing, Transformation / Enrichment, Analytics Warehouse Load.

**[A-09] BOUNDARY CHECKS — Operations** — Seven-column tables per [SC-7] between every stage pair. [SC-4 | SC-5 | SC-9: every `Incumbent Equiv.` cell cites [A-03].]

**[A-10] PHASE GATE CHECK — Role 2** — *Produce and tick. Role 3 may not begin.*

- [ ] DOMAIN CONTEXT opens with `Citing: [A-02]` and `[A-03]`
- [ ] All seven columns populated in every boundary block
- [ ] Every `Incumbent Equiv.` cell cites [A-03] — no estimated values without token
- [ ] All Verdicts from [A-02] — no Operations-specific re-declaration

---

### ROLE 3 — COMMERCE DATA DOMAIN EXPERT

**Scenario:** Catalog Snapshot pipeline — pricing engine to storefront cache.

**[A-11] DOMAIN CONTEXT** — *[SC-6: Citing tokens from both non-adjacent Role 1 and Role 2.]*

**Citing:** [A-02] (Finance's STALE SLA CONTRACT), [A-03] (Finance's INCUMBENT BASELINE), [A-08] (Operations' LINEAGE TRACE)

**[A-12] LINEAGE TRACE — Commerce** — *[Apply SC-2.]* Four stages: Price List Extraction, Landing, Price Rule Transformation, Storefront Cache Load.

**[A-13] BOUNDARY CHECKS — Commerce** — Seven-column tables per [SC-7]. [SC-4 | SC-5 | SC-9.]

**[A-14] RECOVERY PRESCRIPTIONS** — For every `NONE — see [A-14]` and every `YES` Data Loss Flag: name the loss point, prescribe specific recovery, include ≥1 formula: *"Fall back to [A-03] if [condition]"* by token.

**[A-15] TRADE-OFF ANALYSIS** — *[Apply SC-8. The `Incumbent Equiv.` column totals from all boundary blocks are available as evidence — incorporate them. Cite [A-02] and [A-03] by token.]*

| Dimension | Current pipeline | Alternative | Incumbent ([A-03]) |
|-----------|-----------------|-------------|-------------------|
| End-to-end freshness vs [A-02] | | | manual total: |
| Loss surface | | | [A-03] recovery: |

**[A-16] PHASE GATE CHECK — Role 3** — *Produce and tick.*

- [ ] DOMAIN CONTEXT cites [A-02], [A-03], and ≥1 Role 2 token
- [ ] All seven columns populated in every Role 3 boundary block
- [ ] [A-14] cites [A-03] by token in ≥1 recovery formula
- [ ] [A-15] incorporates `Incumbent Equiv.` column evidence and cites [A-02] and [A-03]

---
---

## V-05 — Full Combination: Finance → Commerce → Operations, Six-Column Schema, Dual-Register Declaration, Required Trade-Off

**Axes:** Role sequence (Finance → Commerce → Operations — most citation-stressful non-natural ordering) + output format (six-column schema) + phrasing register (dual-register declaration with format-specific compliance markers per role) + required TRADE-OFF ANALYSIS (C-29)
**Hypothesis:** Declaring two output registers — Finance uses table format; Commerce uses conversational prose — and specifying format-specific compliance markers for each register makes the structural completeness guarantee format-independent while a non-natural three-way ordering maximizes citation stress across all three roles.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT — Finance | Role 1 | Revenue Journal Entry vocabulary, consumer, cadence |
| [A-02] | STALE SLA CONTRACT | Role 1 | Pre-declared stale threshold — locked after Role 1, Stage 1 |
| [A-03] | INCUMBENT BASELINE | Role 1 | Manual GL reconciliation process this pipeline replaces |
| [A-04] | LINEAGE TRACE — Finance | Role 1 | Stage-by-stage Revenue Journal Entry lineage (table register) |
| [A-05] | BOUNDARY CHECKS — Finance | Role 1 | Interleaved 6-column boundary blocks, Role 1 |
| [A-06] | PHASE GATE CHECK — Role 1 | Role 1 | Self-verification checklist, end of Role 1 |
| [A-07] | DOMAIN CONTEXT — Commerce | Role 2 | Catalog Snapshot vocabulary with Citing: line |
| [A-08] | LINEAGE TRACE — Commerce | Role 2 | Stage-by-stage Catalog Snapshot lineage (conversational register) |
| [A-09] | BOUNDARY NARRATIONS — Commerce | Role 2 | Interleaved boundary paragraphs, Role 2 |
| [A-10] | PHASE GATE CHECK — Role 2 | Role 2 | Self-verification checklist, end of Role 2 |
| [A-11] | DOMAIN CONTEXT — Operations | Role 3 | Inventory Position vocabulary with Citing: line |
| [A-12] | LINEAGE TRACE — Operations | Role 3 | Stage-by-stage Inventory Position lineage (table register) |
| [A-13] | BOUNDARY CHECKS — Operations | Role 3 | Interleaved 6-column boundary blocks, Role 3 |
| [A-14] | RECOVERY PRESCRIPTIONS | Role 3 | Per-loss-point recovery with Fall-back-to-[A-03] formula |
| [A-15] | TRADE-OFF ANALYSIS | Role 3 | Required named section; cites [A-02] and [A-03] by token |
| [A-16] | PHASE GATE CHECK — Role 3 | Role 3 | Final self-verification checklist |

---

### STRUCTURAL CONSTRAINTS

| ID | Constraint |
|----|-----------|
| SC-1 | **Citation tokens**: every handoff target cited uses its `[A-xx]` token. |
| SC-2 | **Stage-write gate**: Stage N+1 may not be written until the boundary block or narration between Stage N and Stage N+1 is complete with all required fields present per its declared register. Do not write Stage N+1 until this boundary is complete. |
| SC-3 | **SLA immutability**: [A-02] is fixed after Role 1, Stage 1. This threshold is fixed. You may not revise [A-02] after Stage 1 of Role 1. |
| SC-4 | **Incremental elapsed**: cumulative elapsed is computed as a named field at every boundary — as a column value in table register or as `running total: X` in conversational register. |
| SC-5 | **Freshness verdict**: each boundary produces a binary freshness result derived from [A-02]. In table register: `Verdict` column with `FRESH` or `STALE`. In conversational register: one of the two verdict phrases from the REGISTER DECLARATION. |
| SC-6 | **Citation-opening rule**: every role after Role 1 opens its DOMAIN CONTEXT with `Citing:` naming tokens from prior roles, including ≥1 from a non-adjacent role. |
| SC-7 | **Register compliance**: each role outputs in its declared register. Switching register mid-role is a protocol violation. Completeness is verified using the compliance markers for the declared register. |
| SC-8 | **Required TRADE-OFF ANALYSIS**: [A-15] is a structurally required output section. Must name ≥1 alternative pattern, ≥2 qualified trade-off dimensions, and cite [A-02] and [A-03] by token. Apply SC-8 when producing [A-15]. |

---

### REGISTER DECLARATION

Two output registers are declared. Each role's register is assigned below and cannot be changed. Completeness verification uses register-specific markers — an evaluator applies the table check for table-register roles and the phrase check for conversational-register roles.

**Table register** (Roles 1 and 3) — boundary blocks are six-column Markdown tables:

| Column | Required content |
|--------|-----------------|
| `Entity` | Named entity from scenario vocabulary |
| `Elapsed (cumul.)` | Running sum with units |
| `Verdict` | `FRESH` or `STALE` vs [A-02] |
| `Error Handling` | Named mechanism or `NONE — see [A-14]` |
| `Schema Delta` | Named field changes or `NONE` |
| `Data Loss Flag` | `YES — [named point]` or `NO` |

**Conversational register** (Role 2) — boundary narrations are prose paragraphs containing these compliance phrases:

| Required field | PASS phrase |
|---------------|------------|
| Domain entity | Entity name in same sentence as verdict phrase |
| Cumulative elapsed | `running total: X` (with unit) |
| Verdict FRESH | `remains current at this boundary` |
| Verdict STALE | `has gone stale at this boundary` |
| Error handling | `on failure: [named mechanism]` |
| Schema delta | `schema change: [named change]` or `schema unchanged` |
| Data loss | `data loss: [named point]` or `no data loss at this boundary` |

**Role register assignments:**

| Role | Domain | Register |
|------|--------|----------|
| Role 1 | Finance | Table — six-column boundary blocks |
| Role 2 | Commerce | Conversational — boundary narration paragraphs |
| Role 3 | Operations | Table — six-column boundary blocks |

---

### SCENARIO

**Domain:** Retail e-commerce order-to-cash.
**Role sequence:** Finance → Commerce → Operations *(non-natural; natural order is Commerce → Operations → Finance).*

This is the most citation-stressful non-natural ordering:
- Finance runs first and anchors [A-02] and [A-03].
- Commerce (Role 2) runs second in conversational register; it must cite Finance's SLA even though Commerce is typically the transaction originator — it has no natural upstream to reference.
- Operations runs last (Role 3) and must cite artifacts from both non-adjacent Finance (Role 1) and Commerce (Role 2).

Each role traces four stages: (1) event / CDC extraction, (2) landing / staging, (3) transformation / enrichment, (4) target load.

---

### ROLE 1 — FINANCE DATA DOMAIN EXPERT (Table Register)

**Scenario:** Revenue Journal Entry pipeline — order events to general ledger.

**[A-01] DOMAIN CONTEXT** — Produce before Stage 1. Declare: entity (Revenue Journal Entry), downstream consumer (GL system), business cadence. ≥2 terms reappear verbatim in subsequent Finance lineage.

**[A-02] STALE SLA CONTRACT** — Numeric stale threshold for Revenue Journal Entry. State: *"This threshold is fixed. You may not revise [A-02] after Stage 1 of Role 1."* [SC-3 activates.]

**[A-03] INCUMBENT BASELINE** — Manual GL reconciliation process this pipeline replaces. Include ≥1 term from [A-01]. Cited by token in [A-14] and [A-15].

**[A-04] LINEAGE TRACE — Finance** — *[Register: table. Apply SC-2.]*

For each stage: source, operation, destination, latency, ≥1 named data loss point.

**Stage 1: Order Event Extraction**

**[A-05] BOUNDARY CHECK: Stage 1 → Stage 2** *[Table register: six-column | SC-4 | SC-5 vs [A-02] | SC-2: Stage 2 blocked]*

| Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag |
|--------|-----------------|---------|----------------|-------------|----------------|
| | | | | | |

**Stage 2: Landing Zone**

**[A-05] BOUNDARY CHECK: Stage 2 → Stage 3** *[Six columns | SC-4 | SC-5]*

| Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag |
|--------|-----------------|---------|----------------|-------------|----------------|
| | | | | | |

**Stage 3: Revenue Recognition Rule Application**

**[A-05] BOUNDARY CHECK: Stage 3 → Stage 4** *[Six columns | SC-4 | SC-5]*

| Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag |
|--------|-----------------|---------|----------------|-------------|----------------|
| | | | | | |

**Stage 4: General Ledger Load**

**[A-06] PHASE GATE CHECK — Role 1** — *Produce and tick. Role 2 may not begin until all items are checked.*

- [ ] [A-02] declares a numeric threshold with explicit lock statement
- [ ] [A-03] names ≥1 term from [A-01] and records manual process durations
- [ ] Every boundary block has all six columns populated — no blank cells
- [ ] Every Verdict is FRESH or STALE derived from [A-02]
- [ ] Every Data Loss Flag is `YES — [named point]` or `NO`
- [ ] Every Schema Delta is named or NONE

---

### ROLE 2 — COMMERCE DATA DOMAIN EXPERT (Conversational Register)

**Scenario:** Catalog Snapshot pipeline — pricing engine to storefront cache.

**[A-07] DOMAIN CONTEXT** — *[SC-6: Open with `Citing: [A-02]`. Commerce has no natural upstream in this ordering — Finance's SLA is the only declared anchor.]*

**Citing:** [A-02] (Finance's STALE SLA CONTRACT — threshold = [value]), [A-03] (Finance's INCUMBENT BASELINE)

Prose paragraph. Declare entity (Catalog Snapshot), downstream consumer (storefront), business cadence. ≥2 terms reappear in boundary narrations. [SC-3: do not introduce a Catalog-specific threshold. All freshness evaluations reference [A-02].]

**[A-08] LINEAGE TRACE — Commerce** — *[Register: conversational prose. Apply SC-2: Stage N+1 blocked until boundary narration is complete with all seven compliance phrases.]*

For each stage: a prose paragraph covering source, operation, destination, latency, ≥1 named data loss point. Entity name must appear in each stage paragraph.

**Stage 1: Price List Extraction from Pricing Engine** — [prose paragraph]

**[A-09] BOUNDARY NARRATION: Stage 1 → Stage 2** — *[Conversational register: all seven compliance phrases required (see REGISTER DECLARATION) | SC-4: `running total: X` | SC-5: one verdict phrase | SC-2: Stage 2 blocked]*

[Produce boundary narration. Must contain: entity name in verdict sentence, `running total: X`, one verdict phrase, `on failure: [mechanism]`, `schema change: [change]` or `schema unchanged`, `data loss: [point]` or `no data loss at this boundary`.]

**Stage 2: Landing Zone** — [prose paragraph]

**[A-09] BOUNDARY NARRATION: Stage 2 → Stage 3** — *[Conversational register: all seven phrases | SC-4: add Stage 2 duration to running total | SC-5]*

[Produce boundary narration.]

**Stage 3: Price Rule Transformation** — [prose paragraph]

**[A-09] BOUNDARY NARRATION: Stage 3 → Stage 4** — *[All seven phrases | SC-4 | SC-5]*

[Produce boundary narration.]

**Stage 4: Storefront Cache Load** — [prose paragraph]

**[A-10] PHASE GATE CHECK — Role 2** — *Produce and tick. Role 3 may not begin until all items are checked.*

- [ ] DOMAIN CONTEXT opens with `Citing: [A-02]` and `[A-03]` — no Catalog-specific threshold declared
- [ ] Every boundary narration contains `running total: X` with unit
- [ ] Every boundary narration contains exactly one verdict phrase (`remains current` or `has gone stale`)
- [ ] Every boundary narration contains `on failure: [named mechanism]`
- [ ] Every boundary narration contains `schema change: [change]` or `schema unchanged`
- [ ] Every boundary narration contains `data loss: [named point]` or `no data loss at this boundary`
- [ ] All verdict phrases reference [A-02] threshold, not a Commerce-specific value

---

### ROLE 3 — OPERATIONS DATA DOMAIN EXPERT (Table Register)

**Scenario:** Inventory Position sync from WMS to demand-planning analytics warehouse.

**[A-11] DOMAIN CONTEXT** — *[SC-6: Citing tokens from both Role 1 (Finance) and Role 2 (Commerce) — Operations is last and must aggregate from both non-adjacent predecessors.]*

**Citing:** [A-02] (Finance's STALE SLA CONTRACT), [A-03] (Finance's INCUMBENT BASELINE), [A-08] (Commerce's LINEAGE TRACE — conversational register, for cross-domain elapsed reference)

Declare entity (Inventory Position), downstream consumer, cadence. ≥2 terms reappear in Operations lineage. [SC-3: do not re-declare a threshold.]

**[A-12] LINEAGE TRACE — Operations** — *[Register: table. Apply SC-2.]* Four stages: CDC Extraction from WMS, Landing Zone, Transformation / Enrichment, Analytics Warehouse Load.

**[A-13] BOUNDARY CHECKS — Operations** — Six-column tables per table register specification between every stage pair. [SC-4 | SC-5: Verdict from [A-02].]

**[A-14] RECOVERY PRESCRIPTIONS** — For every `NONE — see [A-14]` annotation and every `YES` Data Loss Flag and every named data loss point from Role 2's conversational narrations: name the loss point (role + stage + event), prescribe a specific recovery mechanism, include ≥1 formula: *"Fall back to [A-03] if [condition]"* using the token.

**[A-15] TRADE-OFF ANALYSIS** — *[Apply SC-8: required named section — not optional. ≥1 alternative pattern, ≥2 qualified trade-off dimensions. Cite [A-02] and [A-03] by token in the section body. Note: Role 2's conversational narrations and Role 1's boundary blocks together provide elapsed evidence across both registers — draw on both.]*

| Dimension | Current pattern | Alternative |
|-----------|----------------|-------------|
| Freshness — evaluated against [A-02] | | |
| Recovery path — references [A-03] | | |
| Cross-register observability | | |

**[A-16] PHASE GATE CHECK — Role 3** — *Produce and tick. Final self-verification.*

- [ ] DOMAIN CONTEXT opens with `Citing:` naming [A-02], [A-03], and [A-08]
- [ ] All six columns populated in every Role 3 boundary block
- [ ] [A-14] covers loss points from both table-register roles and conversational-register Role 2
- [ ] [A-14] contains ≥1 `Fall back to [A-03] if [condition]` formula using the token
- [ ] [A-15] cites [A-02] and [A-03] by token — not by description
- [ ] End-to-end elapsed is computable by combining cumulative values from [A-05], [A-09] (running total phrases), and [A-13]

---

## Variation Summary

| Variation | Axes | Primary v8 innovations tested | Non-natural order |
|-----------|------|------------------------------|------------------|
| V-01 | Role sequence | C-26 (citation stress by non-natural ordering) | Ops → Finance → Commerce |
| V-02 | Output format | C-28 extended (6-column schema adds C-03/C-04 to column-existence check) | None (natural) |
| V-03 | Phrasing register | Format-independent compliance via phrase map | None (natural) |
| V-04 | Role sequence + Inertia framing | C-29 + incumbent-as-boundary-column (7-column, status-quo always visible) | Finance → Ops → Commerce |
| V-05 | Full combination | C-28 + C-29 + dual-register declaration + most-stressful citation ordering | Finance → Commerce → Ops |
