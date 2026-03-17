Now I have a complete picture of the R11 structure and the three new C-39/C-40/C-41 criteria. Let me write the R12 variations.

---

# flow-dataflow — Round 12 Variations

## R11 gap summary before writing

**C-39 not fully satisfied in R11** — The pattern extraction identified that V-05's SC-12 says "Commerce boundaries" — the SC body names the governed role BY THE BOUNDARY CONTEXT LABEL ("Commerce boundaries"), not only by the consuming role's Citing: line. V-01's SC-11 names the token `[A-04]` and says "Finance's `Citing:` line must include" but the evaluator determined the role-scope declaration was not present in the SC body as a dedicated role-boundary label. C-39 requires the SC body to contain a phrase of the form "[ROLE] boundaries" or "at [ROLE] boundaries" — the governed role must be identified by naming the boundary context that governs the SC's scope, separate from stating what the Citing: line must contain.

**C-40 not fully satisfied in R11 V-01** — V-05's SC-12 says "two roles prior" in the body as a structural declaration bound to the token name. V-01's SC-11 had the phrase "produced two roles prior" adjacent to the token description but the evaluator noted it was not a standalone distance declaration in the SC body — it appeared as a parenthetical qualifier, not as a named property of the constraint. C-40 requires the SC body to declare the position distance as an explicit named field or clause (e.g., "Position distance: 2" or "two roles prior" as a sentence-completing clause in a dedicated SC sentence).

**C-41 not fully satisfied in R11 V-01** — V-05's Phase Gate 2 last item ends with "fails SC-12" making the SC number appear as a CONSEQUENCE in the verification text. V-01's Phase Gate 2 item says "SC-11 pre-announcement:" as a LABEL PREFIX only — the evaluator noted that a prefix label on a checklist item does not constitute the SC number appearing in the item's verification body, because a model that produces an unticked item reveals only a label failure, not a named constraint violation. C-41 requires the SC number to appear in the item's verification body (after the checkbox marker, in the pass/fail condition text) so that a failed item names the governing SC directly.

## Variation axes

- **V-01**: Role sequence (C-38+C-39+C-40+C-41) — Finance → Commerce → Operations; Operations runs last and must skip-cite Finance boundaries. SC-12 body says "at Finance boundaries" (C-39) and "two roles prior" as a standalone clause (C-40). Phase Gate 2 item ends with "fails SC-12" (C-41). C-36 and C-37 not targeted.
- **V-02**: Output format (C-41 consequence rendering) — Commerce → Operations → Finance; Phase Gate 2 item formats the SC number as an inline consequence clause with distinct phrasing from V-01. C-36 targeted (baseline-first). C-37 not targeted.
- **V-03**: Lifecycle emphasis (dedicated SKIP-LEVEL CITATION GATE subsection in Phase Gate 2) — Operations → Finance → Commerce; expanded Phase Gate 2 isolates C-41 verification as a named sub-block with three items. C-36 targeted. C-37 not targeted.
- **V-04**: Combined C-36 + C-38 + C-39 + C-40 + C-41 — Commerce → Operations → Finance; baseline-first SC-11 combined with skip-level SC-12 carrying explicit "Commerce boundaries" (C-39), "two roles prior" standalone clause (C-40), and "fails SC-12" consequence in Phase Gate 2 item (C-41). No Parts A/B.
- **V-05**: Full combination C-36 + C-37 + C-38 + C-39 + C-40 + C-41 — Commerce → Operations → Finance; REGISTER DECLARATION Parts A/B as sole C-34/C-35 authority (C-37) combined with all four skip-level criteria plus baseline-first ordering.

---

## V-01

**Axis**: Role sequence — Finance → Commerce → Operations; Operations runs last and must skip-cite Finance boundaries (C-38+C-39+C-40+C-41)

**Hypothesis**: Placing Finance first and Operations last with a Finance → Commerce → Operations non-natural sequence forces Operations to skip-cite Finance's boundary artifacts two roles prior. SC-12 body is written to satisfy C-39 by naming "at Finance boundaries" as the governed boundary context, C-40 by declaring "two roles prior" as a standalone position-distance clause, and C-41 by ending the Phase Gate 2 verification item with "fails SC-12" in the consequence text. C-36 and C-37 are not targeted: DOMAIN CONTEXT holds token [A-01] and no Parts A/B structure is used. This isolates the three new criteria on a novel role ordering not used in R11.

---

You are tracing data through a retail **returns-to-restock** pipeline. Three expert roles run in the sequence **Finance → Commerce → Operations**. Finance establishes the domain context, returns SLA, and manual-process baseline. Commerce extends the trace through the catalog availability layer. Operations runs last, executing the physical restocking stage; it must reach back two roles to Finance's boundary artifacts as a required skip-level citation.

The physical pipeline flows: customer return receipt → returns authorization → GL credit memo → Commerce catalog availability flag reversal → WMS restocking queue → dock scan → WMS stock-on-hand quantity update.

Operations runs last. A `Citing:` line that names only Commerce's tokens without Finance's boundary checks fails SC-12.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. Every citation must use the `[A-xx]` token as spelled in this table. A citation to a target not listed here is a protocol violation.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Finance | Entity vocabulary, returns SLA (immutable after Stage 1), downstream consumer, business cadence |
| [A-02] | INCUMBENT BASELINE | Finance | Manual returns-and-restock process this pipeline replaces; ≥3 named steps with durations; ≥1 entity from [A-01] |
| [A-03] | STAGE TRACE — Finance | Finance | Returns receipt → authorization → GL credit memo; stage tables |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; interleaved between Finance stages; Incumbent Equiv. cells cite [A-02] |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all items ✓ before Commerce begins |
| [A-06] | STAGE TRACE — Commerce | Commerce | GL credit memo confirmation → catalog availability flag reversal → Commerce cache update; stage tables |
| [A-07] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cells cite [A-02] |
| [A-08] | PHASE GATE 2 | Commerce | Self-verification checklist; all items ✓ before Operations begins; includes SC-12 skip-level pre-verification |
| [A-09] | STAGE TRACE — Operations | Operations | WMS restocking queue → dock scan → WMS stock-on-hand update; stage tables |
| [A-10] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cells cite [A-02] |
| [A-11] | STALE ANALYSIS | Operations | Normal-operation and failure-mode elapsed vs [A-01] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Operations | Named recovery per loss point and "no handling" annotation; formula `Fall back to [A-02] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Operations | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; additive breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Operations | Required named section; cites [A-01], [A-02], and [A-13] by token; ≥1 alternative pattern; ≥2 trade-off dimensions |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout. All stage blocks and boundary blocks are rendered as markdown tables. An evaluator may verify any required field by scanning for the named column.

**Per-field compliance markers (tabular register):**

| Required Field | Compliance Marker | Disqualifying Form |
|----------------|-------------------|--------------------|
| Domain entity at boundary | `Entity` column — named entity from [A-01] | "data" or "records" alone |
| Error handling | `Error Handling` column — named mechanism or `no handling — see [A-12]` | Silence / omitted column |
| Elapsed (cumulative) | `Elapsed (cumul.)` column — numeric sum of all prior stage and boundary latencies | Partial sum or deferred |
| Freshness verdict | `Verdict` column — `FRESH` or `STALE` derived from [A-01] threshold | Any value other than FRESH/STALE |
| Schema state | `Schema Delta` column — named field changes or `NONE` | Omitted column |
| Data loss flag | `Data Loss Flag` column — `YES — [named loss point]` or `NO` | Generic "errors may occur" |
| Stage latency | `Stage Latency` column (stage tables) — explicit value, range, or characterization | Inferred from boundary elapsed only |
| Incumbent equivalent | `Incumbent Equiv.` column — form `[A-02]: [named manual step + duration]`; `[A-02]` token required | Bare duration without `[A-02]` token; omitted column |

---

### BOUNDARY BLOCK SCHEMA

Standalone section declared before any role output. Every required column is named here. Role instructions reference this section by name; they do not restate field requirements. An evaluator verifies boundary block completeness by column existence alone.

**Every boundary block must be a markdown table with the following columns, in this order:**

| Column | Required Content |
|--------|-----------------|
| Entity | Named entity from [A-01] vocabulary. "data" or "records" alone fails. |
| Elapsed (cumul.) | Sum of all prior stage and boundary latencies, in minutes. Computed inside this block; not deferred. |
| Verdict | `FRESH` or `STALE` — derived by comparing Elapsed (cumul.) against the [A-01] threshold. Cite [A-01] by token. |
| Error Handling | Named retry / dead-letter / rollback mechanism, or `no handling — see [A-12]`. Silence fails. |
| Schema Delta | Named field-level changes at this boundary, or `NONE`. |
| Data Loss Flag | `YES — [named loss point]` or `NO`. Generic language fails. |
| Incumbent Equiv. | `[A-02]: [named manual step + duration]`. `[A-02]` token required; bare duration is a protocol violation. |

A boundary block that omits any column, or is rendered as a labeled field list, fails this schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Finance opens with `Citing: [A-xx], [A-yy], ...` listing every token from prior roles this role builds on. Finance is first and has no prior tokens. Prose back-references ("as established above") do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the BOUNDARY CHECK table between Stage N and Stage N+1 is fully populated per the BOUNDARY BLOCK SCHEMA. Write the table. Confirm all seven columns are populated. Then write Stage N+1. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed computation**: The `Elapsed (cumul.)` column in each BOUNDARY CHECK must be the sum of all prior stage latencies and all prior boundary latencies up to and including this boundary. Compute it inside the boundary block; it may not be deferred. [Apply SC-3 at every boundary block.]

**SC-4 — Binary freshness verdict**: Each boundary block `Verdict` must read `FRESH` or `STALE`, derived by comparing Elapsed (cumul.) against the [A-01] threshold. Cite [A-01] by token; do not restate its value. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability of returns SLA**: Finance must append to [A-01] verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written." Commerce and Operations may not redeclare or adjust the threshold.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required outputs. Each is a checklist with named criterion identifiers. The next role may not begin until all items are ✓. [Apply SC-6 before role transitions.]

**SC-7 — Stage table format**: Every stage block is a markdown table with required columns: `Stage Latency | Schema In | Schema Out | Data Loss Flag`. Stage Latency must be an explicit annotation; it may not be omitted. [Apply SC-7 at every stage block.]

**SC-8 — Trade-off analysis as required section**: [A-14] TRADE-OFF ANALYSIS is a structurally required named section. It must cite [A-02], [A-01], and [A-13] by token — all three required. Name ≥1 alternative data propagation pattern. Provide ≥2 trade-off dimensions using [A-13] Grand Total as the comparison endpoint. [Apply SC-8 when producing [A-14].]

**SC-9 — Per-boundary incumbent equivalent cell form**: Every `Incumbent Equiv.` cell must cite `[A-02]` by token and name the corresponding manual step with its duration. Required form: `[A-02]: [named step + duration]`. A bare duration without the `[A-02]` token is a protocol violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Before writing [A-14], produce [A-13] INCUMBENT TOTAL. Sum all `Incumbent Equiv.` cell values from [A-04], [A-07], and [A-10]. Show additive breakdown by role (Finance subtotal, Commerce subtotal, Operations subtotal, Grand Total). [A-14] must cite [A-13] by token as the numeric comparison endpoint. [Apply SC-10 before writing [A-14].]

**SC-11 — Cross-role citation chain**: Each role explicitly cites named outputs from prior roles by token in its `Citing:` line. A role that introduces vocabulary or analysis without a named token citation does not satisfy SC-11. [Apply SC-11 at every non-first role opening.]

**SC-12 — Skip-level citation for Operations' `Citing:` line at Finance boundaries**: This constraint governs Operations' `Citing:` line only; Commerce is exempt from this SC. At Finance boundaries, Operations must include `[A-04]` — Finance's boundary checks — in its opening `Citing:` line. Position distance: two (2) roles prior in the Finance → Commerce → Operations sequence. Commerce is Operations' immediate predecessor; a `Citing:` line naming only Commerce's tokens without `[A-04]` fails SC-12. The Phase Gate 2 checklist ([A-08]) verifies `[A-04]` is present in Operations' Citing: line before Operations may begin.

---

### ROLE 1 — Finance

[Finance runs first. No Citing line required.]

**[A-01] DOMAIN CONTEXT** — Write this before Stage 1. Include:
- Entity vocabulary: customer return receipt, returns authorization record, GL credit memo, Commerce catalog availability flag, WMS restocking queue entry, WMS stock-on-hand quantity
- Downstream consumer and business cadence (e.g., returns SLA window: maximum elapsed from return receipt to WMS stock-on-hand update. Declare as an integer with unit.)
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written."

**[A-02] INCUMBENT BASELINE** — Write immediately after [A-01] and before Stage 1. Describe the manual returns-and-restock process this pipeline replaces. Include ≥3 named manual steps with durations (e.g., "Paper returns form submitted to supervisor for authorization: 2 h", "Manual GL credit memo entry: 45 min", "Phone call to warehouse to initiate restock: 30 min"). Use ≥1 entity name from [A-01]. This artifact is the source for all `Incumbent Equiv.` cells in [A-04], [A-07], [A-10].

**[A-03] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 1: Customer return receipt → Returns authorization record
- Stage 2: Returns authorization → GL credit memo creation
- Stage 3: GL credit memo → AP offset posting

**[A-04] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA (7 columns). One block between each stage pair. [SC-3 applies.] [SC-4 applies.] [SC-9 applies.]

**[A-05] PHASE GATE 1** — Produce and tick before Commerce begins. Mark each ✓ or ✗:
- [ ] [A-01] contains returns SLA as integer with unit, plus SC-5 verbatim statement
- [ ] [A-02] includes ≥3 named steps with durations and ≥1 entity from [A-01]
- [ ] Every stage in [A-03] is a table with all four required columns per SC-7
- [ ] Every block in [A-04] has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] Every `Elapsed (cumul.)` is a computed numeric sum inside the block (SC-3)
- [ ] Every `Verdict` is FRESH or STALE derived from [A-01] threshold (SC-4)
- [ ] Every `Incumbent Equiv.` cell uses form `[A-02]: [named step + duration]` (SC-9)

Commerce may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 2 — Commerce

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. Use entity names from [A-01].
- Stage 4: GL credit memo confirmation → Commerce catalog availability flag reversal
- Stage 5: Catalog availability flag reversal → Commerce inventory cache update

**[A-07] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: Elapsed (cumul.) extends the final value in [A-04]; do not reset to zero.]
[SC-4: Verdict vs [A-01] threshold; do not redeclare threshold value.]
[SC-9: every Incumbent Equiv. cell form `[A-02]: [named step + duration]`.]

**[A-08] PHASE GATE 2** — Produce and tick before Operations begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] is a table with all four required columns per SC-7
- [ ] Every block in [A-07] has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] final value; not reset (SC-3)
- [ ] Every `Verdict` derives from [A-01] threshold without redeclaring its value (SC-4)
- [ ] Every `Incumbent Equiv.` cell uses form `[A-02]: [named step + duration]` (SC-9)
- [ ] `[A-04]` present in Operations' `Citing:` line — a Citing line naming only Commerce's tokens without `[A-04]` fails SC-12 (Finance boundaries, two roles prior)

Operations may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 3 — Operations

Citing: [A-01], [A-02], [A-04], [A-07]
([A-04] is required per SC-12 — Finance's boundary checks, produced two roles prior at Finance boundaries. Commerce is Operations' immediate predecessor; citing only [A-07] without [A-04] fails SC-12.)

**[A-09] STAGE TRACE — Operations** — Per SC-7. Per SC-2. Use entity names from [A-01].
- Stage 6: Commerce cache update confirmation → WMS restocking queue entry
- Stage 7: WMS restocking queue → Warehouse dock scan
- Stage 8: Dock scan → WMS stock-on-hand quantity update

**[A-10] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: extend Elapsed (cumul.) from final value in [A-07].]
[SC-4: Verdict vs [A-01] threshold.]
[SC-9: every Incumbent Equiv. cell form `[A-02]: [named step + duration]`.]

**[A-11] STALE ANALYSIS** — Using Elapsed (cumul.) from [A-10] final boundary:

| Entity ([A-01]) | Normal elapsed | Failure-mode elapsed | [A-01] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

Produce separate rows for normal-operation and failure-mode staleness. Cite [A-01] by token; do not restate the numeric threshold value.

**[A-12] RECOVERY PRESCRIPTIONS** — For every `no handling — see [A-12]` annotation in [A-04]/[A-07]/[A-10] and every `Data Loss Flag: YES` in [A-03]/[A-06]/[A-09], provide a specific named recovery action. Required formula: `Fall back to [A-02] if [specific named failure condition]`. Cite [A-02] using this formula at least once.

**[A-13] INCUMBENT TOTAL** — Per SC-10. Produce immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Finance | [sum of [A-04] values] | [step names from [A-02]] |
| Commerce | [sum of [A-07] values] | [step names from [A-02]] |
| Operations | [sum of [A-10] values] | [step names from [A-02]] |
| **Grand Total** | | |

[A-14] must cite this table by token `[A-13]`.

**[A-14] TRADE-OFF ANALYSIS** — [SC-8 applies.] Required named section. Cite [A-02], [A-01], and [A-13] — all three tokens required. Name ≥1 alternative pattern (e.g., event-driven CDC, synchronous dual-write). Provide ≥2 trade-off dimensions using [A-13] Grand Total as the numeric comparison endpoint.

---

---

## V-02

**Axis**: Output format — Phase Gate 2 checklist item formats the SC-12 number as an inline consequence clause using `— SC-12 violation` phrasing (C-41), distinct from V-01's `fails SC-12` consequence form

**Hypothesis**: The C-41 criterion requires the SC number to appear in the item's verification body as a named consequence, not merely a label. V-02 tests a second rendering form: the Phase Gate 2 skip-level item ends with `— SC-12 violation if absent`, placing the SC reference in an explicit conditional consequence clause. The role sequence Commerce → Operations → Finance (same as R11 V-05) is retained to isolate the format variation. C-36 is targeted (Commerce first → [A-01] = INCUMBENT BASELINE, baseline-first production). C-37 is not targeted (no Parts A/B).

---

You are tracing data through a retail **demand-signal-to-fulfillment** pipeline. Three expert roles run in the sequence **Commerce → Operations → Finance**. Commerce runs first and produces the incumbent manual-process baseline before any stage is traced — establishing the cost-of-inertia story from the customer-facing domain. Operations extends the trace through the warehouse fulfillment layer. Finance runs last and must reach back two roles to cite Commerce's boundary artifacts as a required skip-level citation.

The physical pipeline flows: storefront demand signal → Commerce availability decision → WMS inventory reservation → warehouse pick-and-pack → shipment confirmation → AP payment authorization → GL settlement entry.

Finance runs last. A `Citing:` line that names only Operations' tokens without Commerce's boundary checks ([A-04]) is an SC-12 violation.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first; all subsequent artifacts are produced in token order. A boundary block appearing before [A-01] is fully written is a sequencing violation (SC-11).

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Commerce | Manual demand-to-fulfillment process this pipeline replaces; ≥3 named steps with durations; produced FIRST before [A-02] and before any stage trace. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Commerce | Entity vocabulary, fulfillment SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total manual duration |
| [A-03] | STAGE TRACE — Commerce | Commerce | Storefront demand signal → availability decision → WMS reservation; stage tables |
| [A-04] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; Incumbent Equiv. cells cite [A-01] |
| [A-05] | PHASE GATE 1 | Commerce | Self-verification checklist; all items ✓ before Operations |
| [A-06] | STAGE TRACE — Operations | Operations | WMS reservation confirmation → pick-and-pack → shipment confirmation; stage tables |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Operations | Self-verification checklist; all items ✓ before Finance; includes SC-12 pre-verification item |
| [A-09] | STAGE TRACE — Finance | Finance | Shipment confirmation → AP payment authorization → GL settlement; stage tables |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cells cite [A-01] |
| [A-11] | STALE ANALYSIS | Finance | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery per loss point; formula `Fall back to [A-01] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Finance | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; additive breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Finance | Required named section; cites [A-01], [A-02], and [A-13] by token; ≥1 alternative pattern; ≥2 trade-off dimensions |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout. All stage blocks and boundary blocks are rendered as markdown tables.

**Per-field compliance markers (tabular register):**

| Required Field | Compliance Marker | Disqualifying Form |
|----------------|-------------------|--------------------|
| Domain entity at boundary | `Entity` column — named entity from [A-02] | "data" or "records" alone |
| Error handling | `Error Handling` column — named mechanism or `no handling — see [A-12]` | Silence / omitted column |
| Elapsed (cumulative) | `Elapsed (cumul.)` column — numeric sum of all prior stage and boundary latencies | Partial sum or deferred |
| Freshness verdict | `Verdict` column — `FRESH` or `STALE` derived from [A-02] threshold | Any value other than FRESH/STALE |
| Schema state | `Schema Delta` column — named field changes or `NONE` | Omitted column |
| Data loss flag | `Data Loss Flag` column — `YES — [named loss point]` or `NO` | Generic "errors may occur" |
| Stage latency | `Stage Latency` column (stage tables) — explicit value, range, or characterization | Inferred from boundary elapsed |
| Incumbent equivalent | `Incumbent Equiv.` column — form `[A-01]: [named manual step + duration]`; `[A-01]` token required | Bare duration without `[A-01]` token; omitted column |

---

### BOUNDARY BLOCK SCHEMA

Standalone section declared before any role output. Every required column is named here. An evaluator verifies boundary block completeness by column existence alone.

**Every boundary block must be a markdown table with the following columns, in this order:**

| Column | Required Content |
|--------|-----------------|
| Entity | Named entity from [A-02] vocabulary. Generic labels fail. |
| Elapsed (cumul.) | Sum of all prior stage and boundary latencies, in minutes. Computed inside this block. |
| Verdict | `FRESH` or `STALE` — vs [A-02] threshold. Cite [A-02] by token. |
| Error Handling | Named mechanism, or `no handling — see [A-12]`. Silence fails. |
| Schema Delta | Named field-level changes, or `NONE`. |
| Data Loss Flag | `YES — [named loss point]` or `NO`. Generic language fails. |
| Incumbent Equiv. | `[A-01]: [named manual step + duration]`. `[A-01]` token required; bare duration is a protocol violation. |

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Commerce opens with `Citing: [A-xx], [A-yy], ...`. Prose back-references do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding BOUNDARY CHECK table is fully populated per BOUNDARY BLOCK SCHEMA. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` computed inside each boundary block; not deferred. [Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` from [A-02] threshold. Cite [A-02] by token. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Commerce appends to [A-02] verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written." Declare as integer with unit, derived from [A-01] total manual duration plus acceptable pipeline headroom.

**SC-6 — Phase gate**: [A-05] and [A-08] are required checklists. Next role may not begin until all items ✓.

**SC-7 — Stage table format**: Every stage block is a table with columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`. Stage Latency must be explicit. [Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [A-14] is a structurally required named section. Must cite [A-01], [A-02], and [A-13] by token — all three required. ≥1 alternative pattern. ≥2 dimensions. [Apply SC-8 when producing [A-14].]

**SC-9 — Per-boundary incumbent equivalent**: Every `Incumbent Equiv.` cell form: `[A-01]: [named manual step + duration]`. The `[A-01]` token is required; bare durations are protocol violations. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Produce [A-13] immediately before [A-14]. Sum Incumbent Equiv. values from [A-04], [A-07], [A-10]; show role breakdown (Commerce subtotal, Operations subtotal, Finance subtotal, Grand Total); cite [A-13] in [A-14] as numeric comparison endpoint. [Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] INCUMBENT BASELINE must be the first artifact written in this output. No boundary block and no stage trace may appear before [A-01] is fully produced. Commerce may not write Stage 1 until [A-01] is complete. The ARTIFACT REGISTRY assigns token [A-01] to INCUMBENT BASELINE to enforce this sequencing: the lowest-numbered token is produced first, guaranteeing that every `Incumbent Equiv.` cell citing [A-01] references a fully-written artifact. A boundary block appearing before [A-01] is complete is a sequencing violation.

**SC-12 — Skip-level citation for Finance's `Citing:` line at Commerce boundaries**: This constraint governs Finance's `Citing:` line only; Operations is exempt. At Commerce boundaries, Finance must include `[A-04]` in its opening `Citing:` line. Position distance: two (2) roles prior in the Commerce → Operations → Finance sequence. Operations is Finance's immediate predecessor; a `Citing:` line naming only Operations' tokens without `[A-04]` is an SC-12 violation. The Phase Gate 2 checklist ([A-08]) verifies `[A-04]` presence in Finance's Citing: line before Finance may begin.

---

### ROLE 1 — Commerce

[Commerce runs first. No Citing line required. The incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST, before any domain context or stage trace. Per SC-11: no boundary block and no stage trace may appear before [A-01] is complete. Describe the manual demand-to-fulfillment process this pipeline replaces from the customer-facing domain perspective. Include ≥3 named manual steps with durations (e.g., "Manual stock availability phone call to warehouse: 20 min", "Spreadsheet inventory reservation update: 30 min", "Email to operations team for pick request: 15 min"). Use entity names that will reappear in [A-02]. This is the source for every `Incumbent Equiv.` cell in [A-04], [A-07], and [A-10]. All subsequent roles must cite [A-01] in their opening Citing line.

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 entity names from [A-01]): storefront demand signal, WMS inventory reservation, warehouse pick-and-pack order, shipment confirmation record, AP payment authorization, GL settlement entry
- Downstream consumer and business cadence
- Fulfillment SLA: declare as an integer with unit, derived from [A-01] total manual duration plus acceptable pipeline headroom.
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written."

**[A-03] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 1: Storefront demand signal → Commerce availability decision
- Stage 2: Commerce availability decision → WMS inventory reservation

**[A-04] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns). One block between Stage 1–Stage 2; one block after Stage 2. [SC-3, SC-4, SC-9 apply. Every `Incumbent Equiv.` cell cites [A-01] — a fully-written artifact since line 1 of this output.]

**[A-05] PHASE GATE 1** — Produce and tick before Operations begins. Mark each ✓ or ✗:
- [ ] [A-01] was produced first, before any stage trace or boundary block (SC-11)
- [ ] [A-01] includes ≥3 named steps with durations
- [ ] [A-02] SLA declared as integer with unit, derived from [A-01]; SC-5 verbatim present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every stage in [A-03] has four required columns per SC-7
- [ ] Every block in [A-04] has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)

Operations may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 3: WMS inventory reservation confirmation → Warehouse pick-and-pack order
- Stage 4: Pick-and-pack order → Shipment confirmation record

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: extend Elapsed (cumul.) from [A-04] final value; do not reset.]
[SC-4: Verdict vs [A-02] threshold; do not redeclare threshold value.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named step + duration]`.]

**[A-08] PHASE GATE 2** — Produce and tick before Finance begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] — [A-01] present (SC-1)
- [ ] Every stage in [A-06] has four required columns per SC-7
- [ ] Every block in [A-07] has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] final value; not reset (SC-3)
- [ ] Every `Verdict` derives from [A-02] threshold; value not redeclared (SC-4)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)
- [ ] `[A-04]` present in Finance's `Citing:` line — absent `[A-04]` is an SC-12 violation (Commerce boundaries, two roles prior)

Finance may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]
([A-04] is required per SC-12 — Commerce's boundary checks, produced two roles prior at Commerce boundaries. Operations is Finance's immediate predecessor; citing only [A-07] without [A-04] is an SC-12 violation. The elapsed chain in [A-10] must extend from [A-07], which itself extended from [A-04].)

**[A-09] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 5: Shipment confirmation record → AP payment authorization
- Stage 6: AP payment authorization → GL settlement entry

**[A-10] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: extend Elapsed (cumul.) from [A-07] final value.]
[SC-4: Verdict vs [A-02] threshold.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named step + duration]`.]

**[A-11] STALE ANALYSIS** — Using final Elapsed (cumul.) from [A-10]:

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

Separate rows for normal-operation and failure-mode staleness. Cite [A-02] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — For every `no handling — see [A-12]` in [A-04]/[A-07]/[A-10] and every `Data Loss Flag: YES` in [A-03]/[A-06]/[A-09], provide a named recovery action. Required formula: `Fall back to [A-01] if [specific named failure condition]`.

**[A-13] INCUMBENT TOTAL** — Per SC-10. Produce immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Commerce | [sum of [A-04] values] | [step names from [A-01]] |
| Operations | [sum of [A-07] values] | [step names from [A-01]] |
| Finance | [sum of [A-10] values] | [step names from [A-01]] |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [SC-8 applies.] Required. Cite `[A-01]`, `[A-02]`, `[A-13]` — all three tokens required. ≥1 alternative pattern. ≥2 trade-off dimensions with [A-13] Grand Total as numeric comparison endpoint.

---

---

## V-03

**Axis**: Lifecycle emphasis — Phase Gate 2 contains a dedicated **SKIP-LEVEL CITATION GATE** subsection that isolates C-39/C-40/C-41 verification as a named three-item block (C-41 satisfied by each item citing SC-12 in its pass/fail body)

**Hypothesis**: When Phase Gate 2 contains a named sub-block "SKIP-LEVEL CITATION GATE (SC-12)" with three items — (a) governed role scope, (b) distance declaration, (c) token consequence — the skip-level criteria become independently verifiable within the gate without reading the STRUCTURAL CONSTRAINTS section. This tests whether dedicating lifecycle space to the skip-level verification (rather than folding it into a single checklist item) improves C-41 satisfaction. Role sequence Operations → Finance → Commerce (non-natural; Commerce runs last). C-36 targeted (Operations first → [A-01] = INCUMBENT BASELINE). C-37 not targeted.

---

You are tracing data through a retail **receiving-to-availability** pipeline. Three expert roles run in the sequence **Operations → Finance → Commerce**. Operations runs first and produces both the incumbent manual-process baseline and the domain context — establishing the inertia story from the warehouse floor before any financial or catalog stage is traced. Finance extends the trace through the invoice layer. Commerce runs last and must skip-cite Operations' boundary artifacts two roles prior as a required citation.

The physical pipeline flows: supplier shipment arrival → dock scan → WMS stock-on-hand update → AP invoice match → GL accrual posting → Commerce inventory cache update → storefront catalog availability flag.

Commerce runs last. A `Citing:` line that names only Finance's tokens without Operations' boundary checks ([A-04]) is an SC-12 violation.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first; a boundary block appearing before [A-01] is fully written is a sequencing violation (SC-11).

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Operations | Manual receiving-and-invoicing process this pipeline replaces; ≥3 named steps with durations; produced FIRST before [A-02] and before any stage trace. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, receiving SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total manual duration |
| [A-03] | STAGE TRACE — Operations | Operations | Dock scan → WMS stock-on-hand update; stage tables |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; Incumbent Equiv. cells cite [A-01] |
| [A-05] | PHASE GATE 1 | Operations | Checklist; all ✓ before Finance begins |
| [A-06] | STAGE TRACE — Finance | Finance | WMS update confirmation → AP invoice match → GL accrual posting; stage tables |
| [A-07] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Finance | Checklist; all ✓ before Commerce begins; includes SKIP-LEVEL CITATION GATE subsection |
| [A-09] | STAGE TRACE — Commerce | Commerce | GL accrual posting confirmation → Commerce inventory cache → catalog availability flag; stage tables |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cells cite [A-01] |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point; formula `Fall back to [A-01] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required section; cites [A-01], [A-02], and [A-13] by token; ≥1 alternative; ≥2 dimensions |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**Per-field compliance markers (tabular register):**

| Required Field | Compliance Marker | Disqualifying Form |
|----------------|-------------------|--------------------|
| Domain entity at boundary | `Entity` column — named entity from [A-02] | "data" or "records" alone |
| Error handling | `Error Handling` column — named mechanism or `no handling — see [A-12]` | Silence / omitted column |
| Elapsed (cumulative) | `Elapsed (cumul.)` column — numeric sum of all prior stage and boundary latencies | Partial sum or deferred |
| Freshness verdict | `Verdict` column — `FRESH` or `STALE` derived from [A-02] threshold | Any value other than FRESH/STALE |
| Schema state | `Schema Delta` column — named field changes or `NONE` | Omitted column |
| Data loss flag | `Data Loss Flag` column — `YES — [named loss point]` or `NO` | Generic "errors may occur" |
| Stage latency | `Stage Latency` column (stage tables) — explicit value, range, or characterization | Inferred from boundary elapsed |
| Incumbent equivalent | `Incumbent Equiv.` column — form `[A-01]: [named manual step + duration]`; `[A-01]` token required | Bare duration without `[A-01]` token; omitted column |

---

### BOUNDARY BLOCK SCHEMA

Standalone section before any role output. Column header strings must match REGISTER DECLARATION spellings exactly.

**Every boundary block must be a markdown table with these columns, in this order:**
`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

A column absent, renamed, or not matching REGISTER DECLARATION header strings fails the schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Operations opens with `Citing: [A-xx], [A-yy], ...`. Citing [A-01] (INCUMBENT BASELINE) is required in every non-first role's Citing line. Prose back-references do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding boundary table is fully populated per BOUNDARY BLOCK SCHEMA. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` computed inside each boundary block; not deferred. [Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` vs [A-02] threshold. Cite [A-02] by token. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Operations appends to [A-02] verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written." Declare as integer with unit, derived from [A-01] total manual duration plus pipeline headroom.

**SC-6 — Phase gate**: [A-05] and [A-08] are required checklists. Next role may not begin until all items ✓.

**SC-7 — Stage table format**: Columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`. Stage Latency explicit. [Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [A-14] is structurally required. Must cite [A-01], [A-02], and [A-13] — all three tokens. ≥1 alternative pattern. ≥2 dimensions. [Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: `[A-01]: [named manual step + duration]`. Token omission is a protocol violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Produce [A-13] immediately before [A-14]. Show role breakdown (Operations, Finance, Commerce, Grand Total). Cite [A-13] in [A-14] as numeric endpoint. [Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] INCUMBENT BASELINE must be the first artifact written. No boundary block and no stage trace may appear before [A-01] is fully produced. Operations may not write Stage 1 until [A-01] is complete. A boundary block appearing before [A-01] is complete is a sequencing violation.

**SC-12 — Skip-level citation for Commerce's `Citing:` line at Operations boundaries**: This constraint governs Commerce's `Citing:` line only; Finance is exempt. At Operations boundaries, Commerce must include `[A-04]` in its opening `Citing:` line. Position distance: two (2) roles prior in the Operations → Finance → Commerce sequence. Finance is Commerce's immediate predecessor in this sequence; a `Citing:` line naming only Finance's tokens without `[A-04]` fails SC-12. The SKIP-LEVEL CITATION GATE in [A-08] (Phase Gate 2) verifies `[A-04]` presence before Commerce may begin.

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required. The incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST, before domain context or any stage trace. Per SC-11. Describe the manual receiving and invoicing process this pipeline replaces. ≥3 named steps with durations (e.g., "Paper delivery note matched against PO by hand: 3 h", "Manual stock count and WMS data entry: 90 min", "Spreadsheet invoice approval emailed to Finance: 45 min"). Use entity names that will reappear in [A-02]. This is the source for every `Incumbent Equiv.` cell in [A-04], [A-07], [A-10].

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include entity vocabulary (reuse ≥2 entity names from [A-01]): supplier shipment record, dock scan event, WMS stock-on-hand quantity, AP invoice match record, GL accrual entry, Commerce inventory cache entry, catalog availability flag. Downstream consumer, business cadence, and receiving SLA as integer with unit derived from [A-01] total manual duration. Per SC-5, append verbatim immutability statement.

**[A-03] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 1: Supplier shipment arrival → Dock scan event
- Stage 2: Dock scan event → WMS stock-on-hand quantity update

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns). One block between Stage 1–Stage 2; one block after Stage 2. [SC-3, SC-4, SC-9 apply.]

**[A-05] PHASE GATE 1** — Produce and tick before Finance begins. Mark each ✓ or ✗:
- [ ] [A-01] was produced first, before any stage trace or boundary block (SC-11)
- [ ] [A-01] includes ≥3 named steps with durations
- [ ] [A-02] SLA declared as integer with unit, derived from [A-01]; SC-5 verbatim present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every stage in [A-03] has four required columns per SC-7
- [ ] Every block in [A-04] has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] Every `Incident Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)

Finance may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 2 — Finance

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 3: WMS stock-on-hand update confirmation → AP invoice match record
- Stage 4: AP invoice match → GL accrual entry posting

**[A-07] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: extend Elapsed (cumul.) from [A-04] final value; do not reset.]
[SC-4: Verdict vs [A-02] threshold; do not redeclare threshold value.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named step + duration]`.]

**[A-08] PHASE GATE 2** — Produce and tick before Commerce begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] — [A-01] present (SC-1)
- [ ] Every stage in [A-06] has four required columns per SC-7
- [ ] Every block in [A-07] has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] final value; not reset (SC-3)
- [ ] Every `Verdict` derives from [A-02] threshold; value not redeclared (SC-4)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)

**SKIP-LEVEL CITATION GATE (SC-12 — Operations boundaries, two roles prior):**
- [ ] Governed role: Commerce's `Citing:` line is the sole target of SC-12; this item does not govern Finance or any other role — absent acknowledgment is an SC-12 scope violation
- [ ] `[A-04]` — Operations' boundary checks, two roles prior — is present in Commerce's `Citing:` line; absent `[A-04]` is an SC-12 violation
- [ ] Finance's tokens alone (without `[A-04]`) in Commerce's `Citing:` line fail SC-12; presence of `[A-07]` does not substitute for `[A-04]`

Commerce may not begin until all items above, including all three SKIP-LEVEL CITATION GATE items, are ✓. [Apply SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]
([A-04] is required per SC-12 — Operations' boundary checks, produced two roles prior at Operations boundaries. Finance is Commerce's immediate predecessor; citing only [A-07] without [A-04] fails SC-12.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 5: GL accrual posting confirmation → Commerce inventory cache entry update
- Stage 6: Commerce inventory cache → Storefront catalog availability flag

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: extend from [A-07] final value.] [SC-4: Verdict vs [A-02] threshold.] [SC-9.]

**[A-11] STALE ANALYSIS** — Using final Elapsed (cumul.) from [A-10]:

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

Cite [A-02] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — Named recovery per loss point and no-handling flag. Required formula: `Fall back to [A-01] if [specific condition]`.

**[A-13] INCUMBENT TOTAL** — Per SC-10. Produce immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Operations | [sum of [A-04] values] | [step names from [A-01]] |
| Finance | [sum of [A-07] values] | [step names from [A-01]] |
| Commerce | [sum of [A-10] values] | [step names from [A-01]] |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [SC-8 applies.] Required. Cite `[A-01]`, `[A-02]`, `[A-13]`. ≥1 alternative pattern. ≥2 dimensions with [A-13] Grand Total as numeric endpoint.

---

---

## V-04

**Axis**: Combined — C-36 (baseline-first) + C-38 + C-39 + C-40 + C-41 (no Parts A/B)

**Hypothesis**: SC-11 (baseline-first sequencing gate) and SC-12 (skip-level citation with explicit governed-role declaration, position-distance clause, and Phase Gate 2 consequence item) are compatible as a combined constraint pair. SC-12 is written to maximize C-39/C-40/C-41 coverage: the body contains "at Commerce boundaries" (C-39), a standalone sentence "Position distance: two (2) roles prior" (C-40), and the Phase Gate 2 item ends with "— SC-12 violation if [A-04] absent" (C-41 consequence form). REGISTER DECLARATION uses standard format without Parts A/B (C-37 not targeted). Commerce → Operations → Finance sequence.

---

You are tracing data through a retail **purchase-order-to-inventory** pipeline. Three expert roles run in the sequence **Commerce → Operations → Finance**. Commerce runs first and produces the incumbent manual-process baseline as the first artifact — establishing the customer-domain inertia story before any pipeline stage is traced. Operations handles the warehouse and receiving layer. Finance runs last and must skip-cite Commerce's boundary artifacts two roles prior.

The physical pipeline flows: Commerce purchase trigger → WMS reservation → warehouse dock receipt → stock-on-hand update → AP invoice creation → GL posting.

Finance runs last. A `Citing:` line naming only Operations' tokens without `[A-04]` (Commerce boundaries) is an SC-12 violation.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. The lowest-numbered token ([A-01]) is produced first; every subsequent artifact is produced in token order. A boundary block appearing before [A-01] is fully written is a sequencing violation (SC-11).

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Commerce | Manual purchasing and inventory process this pipeline replaces; ≥3 named steps with durations; produced FIRST, before [A-02] and before any stage trace. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Commerce | Entity vocabulary, inventory SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total manual duration |
| [A-03] | STAGE TRACE — Commerce | Commerce | Purchase trigger → WMS inventory reservation → reservation confirmation; stage tables |
| [A-04] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01] |
| [A-05] | PHASE GATE 1 | Commerce | Checklist; all ✓ before Operations |
| [A-06] | STAGE TRACE — Operations | Operations | Dock receipt → WMS stock-on-hand update; stage tables |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Operations | Checklist; all ✓ before Finance; includes SC-12 skip-level verification item |
| [A-09] | STAGE TRACE — Finance | Finance | Stock-on-hand confirmation → AP invoice creation → GL posting; stage tables |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cells cite [A-01] |
| [A-11] | STALE ANALYSIS | Finance | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery per loss point; formula `Fall back to [A-01] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Finance | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; additive breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Finance | Required section; cites [A-01], [A-02], and [A-13] by token; ≥1 alternative; ≥2 dimensions |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout. All stage blocks and boundary blocks are rendered as markdown tables.

**Per-field compliance markers (tabular register):**

| Required Field | Compliance Marker | Disqualifying Form |
|----------------|-------------------|--------------------|
| Domain entity at boundary | `Entity` column — named entity from [A-02] | "data" or "records" alone |
| Error handling | `Error Handling` column — named mechanism or `no handling — see [A-12]` | Silence / omitted column |
| Elapsed (cumulative) | `Elapsed (cumul.)` column — numeric sum of all prior stage and boundary latencies | Partial sum or deferred |
| Freshness verdict | `Verdict` column — `FRESH` or `STALE` derived from [A-02] threshold | Any value other than FRESH/STALE |
| Schema state | `Schema Delta` column — named field changes or `NONE` | Omitted column |
| Data loss flag | `Data Loss Flag` column — `YES — [named loss point]` or `NO` | Generic "errors may occur" |
| Stage latency | `Stage Latency` column (stage tables) — explicit value, range, or characterization | Inferred from boundary elapsed |
| Incumbent equivalent | `Incumbent Equiv.` column — form `[A-01]: [named manual step + duration]`; `[A-01]` token required | Bare duration without `[A-01]` token; omitted column |

---

### BOUNDARY BLOCK SCHEMA

Standalone section declared before any role output. Every required column is named here. An evaluator verifies boundary block completeness by column existence alone.

**Every boundary block must be a markdown table with the following columns, in this order:**

| Column | Required Content |
|--------|-----------------|
| Entity | Named entity from [A-02] vocabulary. Generic labels fail. |
| Elapsed (cumul.) | Sum of all prior stage and boundary latencies, in minutes. Computed inside this block. |
| Verdict | `FRESH` or `STALE` — vs [A-02] threshold. Cite [A-02] by token. |
| Error Handling | Named mechanism, or `no handling — see [A-12]`. Silence fails. |
| Schema Delta | Named field-level changes, or `NONE`. |
| Data Loss Flag | `YES — [named loss point]` or `NO`. Generic language fails. |
| Incumbent Equiv. | `[A-01]: [named manual step + duration]`. `[A-01]` token required; bare duration is a protocol violation. |

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Commerce opens with `Citing: [A-xx], [A-yy], ...`. Citing [A-01] (INCUMBENT BASELINE) is required in every non-first role's Citing line. Prose back-references do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding boundary table is fully populated per BOUNDARY BLOCK SCHEMA. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` computed inside each boundary block; not deferred. [Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` vs [A-02] threshold. Cite [A-02] by token. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Commerce appends to [A-02] verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written." Declare as integer with unit, derived from [A-01] total manual duration plus acceptable pipeline headroom.

**SC-6 — Phase gate**: [A-05] and [A-08] are required checklists. Next role may not begin until all items ✓.

**SC-7 — Stage table format**: Columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`. Stage Latency explicit. [Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [A-14] is structurally required. Must cite [A-01], [A-02], and [A-13] by token — all three required. ≥1 alternative pattern. ≥2 dimensions. [Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: `[A-01]: [named manual step + duration]`. Token omission is a protocol violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Produce [A-13] immediately before [A-14]. Sum Incumbent Equiv. values from [A-04], [A-07], [A-10]; show role breakdown (Commerce, Operations, Finance, Grand Total); cite [A-13] in [A-14] as numeric endpoint. [Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] INCUMBENT BASELINE must be the first artifact written in this output. No boundary block and no stage trace may appear before [A-01] is fully produced. Commerce may not write Stage 1 until [A-01] is complete. The ARTIFACT REGISTRY assigns token [A-01] to INCUMBENT BASELINE to enforce this sequencing: the lowest-numbered token is produced first, guaranteeing that every `Incumbent Equiv.` cell citing [A-01] references a fully-written artifact. A boundary block appearing before [A-01] is complete is a sequencing violation regardless of whether [A-01] is eventually produced.

**SC-12 — Skip-level citation for Finance's `Citing:` line at Commerce boundaries**: This constraint governs Finance's `Citing:` line only; Operations is exempt from SC-12. At Commerce boundaries, Finance must include `[A-04]` in its opening `Citing:` line — Commerce's boundary checks, produced two (2) roles prior in the Commerce → Operations → Finance sequence. Position distance: two roles prior. Operations is Finance's immediate predecessor in this sequence; a `Citing:` line naming only Operations' tokens without `[A-04]` fails SC-12. The Phase Gate 2 checklist ([A-08]) verifies `[A-04]` is present in Finance's Citing: line as a named item with SC-12 as the governing identifier before Finance may begin.

---

### ROLE 1 — Commerce

[Commerce runs first. No Citing line required. The incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST, before domain context or any stage trace. Per SC-11: no boundary block and no stage trace may appear before [A-01] is complete. Describe the manual purchasing and inventory process this pipeline replaces from the Commerce domain perspective. ≥3 named manual steps with durations (e.g., "Buyer emails PO to supplier and awaits confirmation: 4 h", "Spreadsheet inventory reservation update after confirmation: 30 min", "Phone call to warehouse to initiate dock prep: 20 min"). Use entity names that will reappear in [A-02]. This is the source for every `Incumbent Equiv.` cell in [A-04], [A-07], [A-10]. [Per REGISTER DECLARATION, `Incumbent Equiv.` compliance marker row.] All subsequent roles must cite [A-01] in their opening Citing line.

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 entity names from [A-01]): purchase trigger record, WMS inventory reservation, dock receipt event, WMS stock-on-hand quantity, AP invoice record, GL posting entry
- Downstream consumer and business cadence
- Inventory SLA: declare as an integer with unit, derived from [A-01] total manual duration plus acceptable pipeline headroom.
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written."

**[A-03] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 1: Purchase trigger record → WMS inventory reservation
- Stage 2: WMS inventory reservation → Reservation confirmation

**[A-04] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns; all headers match REGISTER DECLARATION compliance markers exactly). One block between Stage 1–Stage 2; one block after Stage 2. [SC-3, SC-4, SC-9 apply. Every `Incumbent Equiv.` cell cites [A-01] — fully written since line 1 of this output, per SC-11.]

**[A-05] PHASE GATE 1** — Produce and tick before Operations begins. Mark each ✓ or ✗:
- [ ] [A-01] was produced first, before any stage trace or boundary block (SC-11)
- [ ] [A-01] includes ≥3 named steps with durations
- [ ] [A-02] SLA declared as integer with unit, derived from [A-01]; SC-5 verbatim present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every stage in [A-03] has four required columns per SC-7
- [ ] Every block in [A-04] has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)

Operations may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 3: Reservation confirmation → Warehouse dock receipt event
- Stage 4: Dock receipt event → WMS stock-on-hand quantity update

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns; headers match REGISTER DECLARATION exactly).
[SC-3: extend Elapsed (cumul.) from [A-04] final value; do not reset to zero.]
[SC-4: Verdict vs [A-02] threshold; do not redeclare threshold value.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named step + duration]`.]

**[A-08] PHASE GATE 2** — Produce and tick before Finance begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] — [A-01] present (SC-1)
- [ ] Every stage in [A-06] has four required columns per SC-7
- [ ] Every block in [A-07] has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] final value; not reset (SC-3)
- [ ] Every `Verdict` derives from [A-02] threshold; value not redeclared (SC-4)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)
- [ ] `[A-04]` present in Finance's `Citing:` line (Commerce boundaries, two roles prior) — SC-12 violation if `[A-04]` absent

Finance may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]
([A-04] is required per SC-12 — Commerce's boundary checks at Commerce boundaries, two roles prior in the Commerce → Operations → Finance sequence. Operations is Finance's immediate predecessor; citing only [A-07] without [A-04] is an SC-12 violation. The elapsed chain in [A-10] extends from [A-07], which itself extended from [A-04]; citing [A-04] confirms the full chain is traceable.)

**[A-09] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 5: WMS stock-on-hand update confirmation → AP invoice record creation
- Stage 6: AP invoice record → GL posting entry

**[A-10] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA (7 columns; headers match REGISTER DECLARATION exactly).
[SC-3: extend Elapsed (cumul.) from [A-07] final value.]
[SC-4: Verdict vs [A-02] threshold.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named step + duration]`.]

**[A-11] STALE ANALYSIS** — Using final Elapsed (cumul.) from [A-10]:

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

Cite [A-02] by token; do not restate the numeric threshold value.

**[A-12] RECOVERY PRESCRIPTIONS** — For every `no handling — see [A-12]` in [A-04]/[A-07]/[A-10] and every `Data Loss Flag: YES` in [A-03]/[A-06]/[A-09], provide a specific named recovery action. Required formula: `Fall back to [A-01] if [specific named failure condition]`.

**[A-13] INCUMBENT TOTAL** — Per SC-10. Produce immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Commerce | [sum of [A-04] values] | [step names from [A-01]] |
| Operations | [sum of [A-07] values] | [step names from [A-01]] |
| Finance | [sum of [A-10] values] | [step names from [A-01]] |
| **Grand Total** | | |

[A-14] must cite this table by token `[A-13]`.

**[A-14] TRADE-OFF ANALYSIS** — [SC-8 applies.] Required. Cite `[A-01]`, `[A-02]`, `[A-13]` — all three tokens required. ≥1 alternative pattern. ≥2 trade-off dimensions with [A-13] Grand Total as numeric endpoint.

---

---

## V-05

**Axis**: Full combination — C-36 + C-37 + C-38 + C-39 + C-40 + C-41

**Hypothesis**: The complete set of criteria from v12 can be satisfied simultaneously: REGISTER DECLARATION Parts A/B as sole C-34/C-35 authority (C-37), baseline-first production with explicit sequencing prohibition (C-36), non-natural ordering with skip-level citation gap (C-26 + C-38), SC-12 body naming governed role at Commerce boundaries (C-39), SC-12 body declaring "two roles prior" as a standalone position-distance clause (C-40), and Phase Gate 2 skip-level item ending with "— SC-12 violation if `[A-04]` absent" (C-41). SC-11 and SC-12 serve complementary roles: SC-11 enforces production-sequence integrity; SC-12 enforces citation-depth integrity. The REGISTER DECLARATION Parts A/B consolidate C-34/C-35 authority; SC-12 consolidates skip-level citation authority. Commerce → Operations → Finance sequence.

---

You are tracing data through a retail **EDI-to-settlement** pipeline. Three expert roles run in the sequence **Commerce → Operations → Finance**. Commerce runs first and produces the incumbent manual-process baseline as the very first artifact in this output — the cost-of-inertia story from the customer-facing domain precedes every pipeline stage. Operations handles the warehouse and receiving layer. Finance runs last and must skip-cite Commerce's boundary artifacts two roles prior as a required skip-level citation.

The physical pipeline flows: supplier EDI purchase order → Commerce PO acknowledgment → WMS dock schedule → warehouse receiving scan → stock-on-hand update → AP matching → GL accrual posting.

Finance runs last. A `Citing:` line naming only Operations' tokens without `[A-04]` (Commerce boundaries, two roles prior) is an SC-12 violation.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first; subsequent artifacts are produced in token order. A boundary block appearing before [A-01] is fully written is a sequencing violation (SC-11).

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Commerce | Manual EDI-and-receiving process this pipeline replaces; ≥3 named steps with durations; produced FIRST, before [A-02] and before any stage trace. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Commerce | Entity vocabulary, settlement SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total manual duration |
| [A-03] | STAGE TRACE — Commerce | Commerce | EDI PO receipt → PO acknowledgment → WMS dock schedule; stage tables |
| [A-04] | BOUNDARY CHECKS — Commerce | Commerce | Boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01]; column headers match REGISTER DECLARATION Part A spellings |
| [A-05] | PHASE GATE 1 | Commerce | Checklist; all ✓ before Operations |
| [A-06] | STAGE TRACE — Operations | Operations | Dock schedule confirmation → warehouse receiving scan → WMS stock-on-hand update; stage tables |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | Boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cells cite [A-01]; column headers match Part A spellings |
| [A-08] | PHASE GATE 2 | Operations | Checklist; all ✓ before Finance; includes SC-12 verification item |
| [A-09] | STAGE TRACE — Finance | Finance | Stock-on-hand update confirmation → AP matching record → GL accrual posting; stage tables |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | Boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cells cite [A-01]; column headers match Part A spellings |
| [A-11] | STALE ANALYSIS | Finance | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery per loss point; formula `Fall back to [A-01] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Finance | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; additive breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Finance | Required section; cites [A-01], [A-02], and [A-13] by token; ≥1 alternative; ≥2 dimensions |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell form) and C-35 (INCUMBENT TOTAL section format). An evaluator may determine pass/fail for both criteria by reading this section alone, without consulting the BOUNDARY BLOCK SCHEMA or role instructions. Structural constraints SC-9 and SC-10 are callbacks to Parts A and B respectively; they do not independently restate compliance requirements.**

**Part A — Field compliance markers (boundary block columns):**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum of all prior stage and boundary latencies, in minutes | Partial sum; deferred total |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE`, derived from [A-02] threshold | Any other value |
| Error handling | `Error Handling` | Named retry/dead-letter/rollback, or exactly `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level additions, removals, or type changes, or exactly `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` — `[A-01]` token required; omission is a protocol violation | Bare duration; token omitted; column absent |
| Stage latency | `Stage Latency` (stage table) | Explicit value, range, or characterization | Inferred from boundary elapsed |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Markdown table with columns: `Role \| Incumbent Equiv. subtotal \| Steps cited`; rows for Commerce, Operations, Finance, and Grand Total; all subtotal values numeric | Prose-only summary; missing role row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | All three tokens `[A-01]`, `[A-02]`, `[A-13]` present; ≥1 alternative pattern named; ≥2 trade-off dimensions | Any token absent; no pattern named |

---

### BOUNDARY BLOCK SCHEMA

Standalone section before any role output. Column header strings must match REGISTER DECLARATION Part A spellings exactly. Role instructions reference this section by name only; they do not restate field requirements.

**Every boundary block must be a markdown table with these columns, in this order:**
`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

A column absent, renamed, or not matching Part A header strings fails the schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Commerce opens with `Citing: [A-xx], [A-yy], ...`. Citing [A-01] (INCUMBENT BASELINE) is required in every non-first role's Citing line. Prose back-references do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding boundary table is fully populated per BOUNDARY BLOCK SCHEMA. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` computed inside each boundary block; not deferred. [Per REGISTER DECLARATION Part A, `Elapsed (cumul.)` row.] [Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` vs [A-02] threshold. Cite [A-02] by token. [Per REGISTER DECLARATION Part A, `Verdict` row.] [Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Commerce appends to [A-02] verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written." Declare as integer with unit, derived from [A-01] total manual duration plus acceptable pipeline headroom.

**SC-6 — Phase gate**: [A-05] and [A-08] are required checklists. Next role may not begin until all items ✓.

**SC-7 — Stage table format**: Columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`. Stage Latency explicit. [Per REGISTER DECLARATION Part A, `Stage Latency` row.] [Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [Per REGISTER DECLARATION Part B, TRADE-OFF ANALYSIS row.] All three tokens required. ≥1 pattern. ≥2 dimensions. [Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: [Per REGISTER DECLARATION Part A, `Incumbent Equiv.` row.] Form: `[A-01]: [named step + duration]`. Token omission is a protocol violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [Per REGISTER DECLARATION Part B, INCUMBENT TOTAL row.] Produce [A-13] immediately before [A-14]; cite [A-13] in [A-14] as numeric endpoint. [Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] INCUMBENT BASELINE must be the first artifact written in this output. No boundary block and no stage trace may appear before [A-01] is fully produced. Commerce may not write Stage 1 until [A-01] is complete. The ARTIFACT REGISTRY assigns token [A-01] to INCUMBENT BASELINE to enforce this sequencing: the lowest-numbered token is produced first, guaranteeing that every `Incumbent Equiv.` cell citing [A-01] references a fully-written artifact. A boundary block appearing before [A-01] is complete is a sequencing violation.

**SC-12 — Skip-level citation for Finance's `Citing:` line at Commerce boundaries**: This constraint governs Finance's `Citing:` line only; Operations is exempt from SC-12. At Commerce boundaries, Finance must include `[A-04]` in its opening `Citing:` line — Commerce's boundary checks. Position distance: two (2) roles prior in the Commerce → Operations → Finance sequence. Operations is Finance's immediate predecessor in this sequence; a `Citing:` line naming only Operations' tokens without `[A-04]` fails SC-12. The Phase Gate 2 checklist ([A-08]) verifies `[A-04]` is present in Finance's Citing: line — the item names SC-12 as the governing authority and marks an SC-12 violation if `[A-04]` is absent.

---

### ROLE 1 — Commerce

[Commerce runs first. No Citing line required. The incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST, before domain context or any stage trace. Per SC-11: no boundary block and no stage trace may appear before [A-01] is complete. Describe the manual EDI and receiving process this pipeline replaces from the Commerce perspective. ≥3 named steps with durations (e.g., "Buyer manual EDI parse and PO entry: 2 h", "Phone confirmation to warehouse dock scheduling: 30 min", "Spreadsheet stock acknowledgment update to Finance: 45 min"). Use entity names that will reappear in [A-02]. This is the source for every `Incumbent Equiv.` cell in [A-04], [A-07], [A-10]. [Per REGISTER DECLARATION Part A, `Incumbent Equiv.` row.] All subsequent roles must cite [A-01] in their opening Citing line.

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 entity names from [A-01]): EDI purchase order, PO acknowledgment record, WMS dock schedule entry, warehouse receiving scan event, WMS stock-on-hand quantity, AP matching record, GL accrual entry
- Downstream consumer and business cadence
- Settlement SLA: declare as an integer with unit, derived from [A-01] total manual duration plus acceptable pipeline headroom.
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written."

**[A-03] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 1: Supplier EDI purchase order → PO acknowledgment record
- Stage 2: PO acknowledgment → WMS dock schedule entry

**[A-04] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns; column header strings must match REGISTER DECLARATION Part A exactly). One block between Stage 1–Stage 2; one block after Stage 2. [SC-3, SC-4, SC-9 / Part A apply. Every `Incumbent Equiv.` cell cites [A-01] — fully written since line 1 of this output per SC-11.]

**[A-05] PHASE GATE 1** — Produce and tick before Operations begins. Mark each ✓ or ✗:
- [ ] [A-01] was produced first, before any stage trace or boundary block (SC-11)
- [ ] [A-01] includes ≥3 named steps with durations
- [ ] [A-02] SLA declared as integer with unit, derived from [A-01]; SC-5 verbatim present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every stage in [A-03] has four required columns per SC-7
- [ ] Every block in [A-04] has seven columns; column headers match REGISTER DECLARATION Part A spellings exactly
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9 / Part A)

Operations may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 3: WMS dock schedule entry → Warehouse receiving scan event
- Stage 4: Warehouse receiving scan → WMS stock-on-hand quantity update

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns; column headers match REGISTER DECLARATION Part A exactly).
[SC-3: extend Elapsed (cumul.) from [A-04] final value; do not reset to zero.]
[SC-4: Verdict vs [A-02] threshold; do not redeclare threshold value.]
[SC-9 / Part A: every Incumbent Equiv. cell: `[A-01]: [named step + duration]`.]

**[A-08] PHASE GATE 2** — Produce and tick before Finance begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] — [A-01] present (SC-1)
- [ ] Every stage in [A-06] has four required columns per SC-7
- [ ] Every block in [A-07] has seven columns; column headers match REGISTER DECLARATION Part A spellings exactly
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] final value; not reset (SC-3 / Part A)
- [ ] Every `Verdict` derives from [A-02] threshold; threshold value not redeclared (SC-4 / Part A)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9 / Part A)
- [ ] `[A-04]` present in Finance's `Citing:` line (Commerce boundaries, two roles prior) — SC-12 violation if `[A-04]` absent

Finance may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]
([A-04] is required per SC-12 — Commerce's boundary checks at Commerce boundaries, two roles prior in the Commerce → Operations → Finance sequence. Operations is Finance's immediate predecessor; a Citing: line naming only [A-07] without [A-04] fails SC-12. The elapsed chain in [A-10] extends from [A-07], which itself extended from [A-04]; citing [A-04] confirms the full elapsed chain is traceable back to Commerce boundaries.)

**[A-09] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 5: WMS stock-on-hand update confirmation → AP matching record creation
- Stage 6: AP matching record → GL accrual entry posting

**[A-10] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA (7 columns; column headers match REGISTER DECLARATION Part A exactly).
[SC-3: extend Elapsed (cumul.) from [A-07] final value.]
[SC-4: Verdict vs [A-02] threshold.]
[SC-9 / Part A: every Incumbent Equiv. cell: `[A-01]: [named step + duration]`.]

**[A-11] STALE ANALYSIS** — Using final Elapsed (cumul.) from [A-10]:

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

Produce separate rows for normal-operation and failure-mode staleness. Cite [A-02] by token; do not restate the numeric threshold value.

**[A-12] RECOVERY PRESCRIPTIONS** — For every `no handling — see [A-12]` in [A-04]/[A-07]/[A-10] and every `Data Loss Flag: YES` in [A-03]/[A-06]/[A-09], provide a specific named recovery action. Required formula: `Fall back to [A-01] if [specific named failure condition]`.

**[A-13] INCUMBENT TOTAL** — [Per REGISTER DECLARATION Part B, INCUMBENT TOTAL row. Per SC-10.] Produce immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Commerce | [sum of [A-04] Incumbent Equiv. values] | [step names from [A-01]] |
| Operations | [sum of [A-07] Incumbent Equiv. values] | [step names from [A-01]] |
| Finance | [sum of [A-10] Incumbent Equiv. values] | [step names from [A-01]] |
| **Grand Total** | | |

Cite this section as `[A-13]` in [A-14].

**[A-14] TRADE-OFF ANALYSIS** — [Per REGISTER DECLARATION Part B, TRADE-OFF ANALYSIS row. Per SC-8.] Required named section. Cite `[A-01]` (manual baseline), `[A-02]` (SLA dimension), and `[A-13]` (numeric incumbent total) — all three tokens required. Name ≥1 alternative data propagation pattern (e.g., event-driven CDC, synchronous dual-write). Provide ≥2 trade-off dimensions using [A-13] Grand Total as the numeric comparison endpoint.

---

## Criterion targeting summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-26 (non-natural ordering) | PASS | PASS | PASS | PASS | PASS |
| C-36 (baseline-first) | FAIL | PASS | PASS | PASS | PASS |
| C-37 (Parts A/B sole authority) | FAIL | FAIL | FAIL | FAIL | PASS |
| C-38 (skip-level citation) | PASS | PASS | PASS | PASS | PASS |
| C-39 (skip-level SC names governed role at boundary) | PASS | PASS | PASS | PASS | PASS |
| C-40 (skip-level SC declares position distance) | PASS | PASS | PASS | PASS | PASS |
| C-41 (Phase Gate 2 item cites SC number in consequence) | PASS | PASS | PASS | PASS | PASS |
| C-16 (cross-role reference chain) | PASS | PASS | PASS | PASS | PASS |
| C-34 (Incumbent Equiv. cell form) | PASS | PASS | PASS | PASS | PASS |
| C-35 (INCUMBENT TOTAL artifact) | PASS | PASS | PASS | PASS | PASS |

**C-39/C-40/C-41 design decisions across variations:**

| SC-12 feature | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------------|------|------|------|------|------|
| C-39 phrase form | "at Finance boundaries" | "at Commerce boundaries" | "at Operations boundaries" | "at Commerce boundaries" | "at Commerce boundaries" |
| C-40 distance form | "two (2) roles prior" standalone clause | "two (2) roles prior" standalone clause | "two (2) roles prior" (gate sub-block header) | "two (2) roles prior" standalone clause | "two (2) roles prior" standalone clause |
| C-41 consequence form | "fails SC-12" | "— SC-12 violation if `[A-04]` absent" | "— absent `[A-04]` is an SC-12 violation" (per gate item) | "— SC-12 violation if `[A-04]` absent" | "— SC-12 violation if `[A-04]` absent" |
