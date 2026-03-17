# flow-dataflow — Round 10 Variations

Reading the R9 scorecard before writing.

## Key gaps from R9

**C-34 absent across all R9 variations** — V-04 introduced an `Incumbent Equiv.` column in
a 7-column boundary schema but enforced no cell form. The token citation requirement —
`[A-02]: [named manual step + duration]` — was never structurally specified. C-34 was not
scoreable in R9.

**C-35 absent across all R9 variations** — V-04's `SC-10` required an INCUMBENT TOTAL before
TRADE-OFF ANALYSIS but omitted: (a) registration of INCUMBENT TOTAL as a named `[A-xx]`
artifact, (b) additive breakdown by role, (c) mandatory citation of INCUMBENT TOTAL's own
token (not just `[A-02]`) in TRADE-OFF ANALYSIS. C-35 was not scoreable in R9.

**C-26 FAIL in V-01** — V-01 scored 98 but failed C-26 (non-natural ordering as citation
stress test). Natural Finance → Operations → Commerce allows context to be inferred; citation
laziness is not detectable as a missing token.

**C-16 PARTIAL in non-natural orderings** — V-02/V-04 scored 93/94 due to maximum citation
distance when Finance runs last. No R9 variation simultaneously passed C-16 and C-26.

## New criteria requiring structural support (C-34, C-35)

**C-34** — Per-boundary `Incumbent Equiv.` column. Required cell form: `[token]: [named
manual step + duration]`. Token citation is required at every boundary block; bare durations
without the `[A-02]` token are protocol violations.

**C-35** — INCUMBENT TOTAL as a named, registered artifact produced immediately before
TRADE-OFF ANALYSIS. Must: (a) sum all per-boundary Incumbent Equiv. values, (b) show
additive breakdown by role, (c) be cited by its own registry token in TRADE-OFF ANALYSIS
as the numeric comparison endpoint. Citing `[A-02]` directly in TRADE-OFF ANALYSIS without
first producing a computed INCUMBENT TOTAL fails C-35.

## Variation axes

- **V-01**: Lifecycle emphasis — C-34/C-35 added to R9 V-01 baseline (Finance → Operations
  → Commerce, tabular); 7th boundary column + INCUMBENT TOTAL artifact + SC-9 + SC-10
- **V-02**: Output format — REGISTER DECLARATION as the primary C-34/C-35 enforcement
  vehicle; compliance marker mapping expanded to cover cell-form and section-format
  requirements; natural order
- **V-03**: Inertia framing — INCUMBENT BASELINE produced as first artifact before DOMAIN
  CONTEXT; Operations → Finance → Commerce; inertia-first role structure maximizes token
  availability for C-34 citations
- **V-04**: Combined (role sequence + lifecycle) — Commerce → Operations → Finance
  (maximally non-natural); C-34 forward-citation stress test; Finance-last aggregates
  INCUMBENT TOTAL from upstream boundary blocks
- **V-05**: Combined (inertia framing + dual-register output format) — Finance (tabular)
  → Commerce (conversational) → Operations (tabular); REGISTER TRANSLATION TABLE extended
  to C-34/C-35 compliance markers; C-33 invariant for conversational Incumbent Equiv.

---

## V-01

**Axis**: Lifecycle emphasis — C-34 and C-35 structural additions to R9 V-01 baseline

**Hypothesis**: Adding a 7th column (`Incumbent Equiv.`) to the BOUNDARY BLOCK SCHEMA with
required cell form `[A-02]: [named step + duration]` satisfies C-34 via the same
column-existence enforcement already proven for C-21/C-28 in R8/R9. Registering INCUMBENT
TOTAL as artifact `[A-13]` with its own token and mandating SC-10 (produce [A-13] before
[A-14], cite [A-13] in TRADE-OFF by token) satisfies C-35 by converting aggregation from
narrative to registry-verifiable computation. Natural Finance → Operations → Commerce order
preserves C-16 PASS while isolating the lifecycle axis. C-26 FAIL is expected and accepted.

---

You are tracing data through a retail purchase-order-to-inventory pipeline. Three expert
roles run in the sequence **Finance → Operations → Commerce**. Finance establishes the PO
staleness SLA, the manual-process baseline, and the Incumbent Equiv. token that all
subsequent roles must cite. Operations and Commerce extend the elapsed chain and produce
boundary blocks that cite Finance's baseline by token — they may not redeclare or re-derive
either the staleness threshold or the incumbent artifact.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. Every citation anywhere in this output must use
the `[A-xx]` token exactly as spelled in this table. A citation to a target not listed here
is a protocol violation.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Finance | Entity vocabulary, staleness SLA (immutable after Stage 1), downstream consumer, business cadence |
| [A-02] | INCUMBENT BASELINE | Finance | Manual PO and AP process this pipeline replaces; ≥3 named steps with durations; ≥1 entity from [A-01] |
| [A-03] | STAGE TRACE — Finance | Finance | PO creation → AP accrual → GL posting; stage tables with Stage Latency column |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables (BOUNDARY BLOCK SCHEMA); interleaved between Finance stages; Incumbent Equiv. cells cite [A-02] |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all items ✓ before Operations begins |
| [A-06] | STAGE TRACE — Operations | Operations | Receiving dock scan → WMS stock-on-hand update; stage tables |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cells cite [A-02] |
| [A-08] | PHASE GATE 2 | Operations | Self-verification checklist; all items ✓ before Commerce begins |
| [A-09] | STAGE TRACE — Commerce | Commerce | WMS snapshot → Commerce platform cache → catalog availability flag; stage tables |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cells cite [A-02] |
| [A-11] | STALE ANALYSIS | Commerce | Elapsed-vs-threshold rows: normal-operation and failure-mode; cites [A-01] threshold by token |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point and "no handling" flag; formula: `Fall back to [A-02] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; additive breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required named section: ≥1 alternative pattern, ≥2 trade-off dimensions; cites [A-01], [A-02], and [A-13] by token |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout. All stage blocks and boundary blocks
are rendered as markdown tables. An evaluator may verify any required field by scanning
for the named column; no prose reading is required.

**Per-field compliance markers (tabular register):**

| Required Field | Compliance Marker | Disqualifying form |
|----------------|-------------------|--------------------|
| Domain entity at boundary | `Entity` column — named entity from [A-01] | "data" or "records" alone |
| Error handling | `Error Handling` column — named mechanism or `no handling — see [A-12]` | Silence / omitted column |
| Elapsed (cumulative) | `Elapsed (cumul.)` column — numeric sum of all prior stage and boundary latencies | Partial sum or deferred to [A-11] |
| Freshness verdict | `Verdict` column — `FRESH` or `STALE` derived from [A-01] threshold | Any value other than FRESH/STALE |
| Schema state | `Schema Delta` column — named field changes or `NONE` | Omitted column |
| Data loss flag | `Data Loss Flag` column — `YES — [named loss point]` or `NO` | Generic "errors may occur" |
| Stage latency | `Stage Latency` column (stage tables) — value, range, or characterization (real-time / near-real / batch / daily) | Inferred from boundary elapsed only |
| Incumbent equivalent | `Incumbent Equiv.` column — cell form: `[A-02]: [named manual step + duration]`; `[A-02]` token required | Bare duration without `[A-02]` token; omitted column |

---

### BOUNDARY BLOCK SCHEMA

This section is the sole authoritative definition of required boundary block fields. Role
instructions reference this section by name; they do not restate field requirements. An
evaluator verifies boundary block completeness by column existence alone, without consulting
role instructions.

**Every boundary block in this output must be a markdown table with the following columns,
in this order:**

| Column | Required Content |
|--------|-----------------|
| Entity | Named entity from [A-01] vocabulary. "data" or "records" alone fails. |
| Elapsed (cumul.) | Sum of all prior stage and boundary latencies, in minutes. Computed inside this block; not deferred to [A-11]. |
| Verdict | `FRESH` or `STALE` — derived by comparing Elapsed (cumul.) against the [A-01] threshold. Cite [A-01] by token; do not restate its numeric value. |
| Error Handling | Named retry / dead-letter / rollback mechanism, or `no handling — see [A-12]`. Silence fails. |
| Schema Delta | Named field-level changes at this boundary (type, name, added, removed), or `NONE`. |
| Data Loss Flag | `YES — [loss point name]` or `NO`. Generic "errors may occur" fails. |
| Incumbent Equiv. | `[A-02]: [named manual step + estimated duration]`. The `[A-02]` token is required; a cell that states a duration without citing `[A-02]` is a protocol violation. |

A boundary block that omits any column, or that is rendered as a labeled field list,
does not conform to this schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Finance opens with
`Citing: [A-xx], [A-yy], ...` listing every token from prior roles this role builds on.
Finance is first and has no prior tokens. Prose back-references ("as established above")
do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the BOUNDARY
CHECK table between Stage N and Stage N+1 is fully populated per the BOUNDARY BLOCK SCHEMA.
Write the table. Confirm all seven columns are populated. Then write Stage N+1.
[Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed computation**: The `Elapsed (cumul.)` column in each BOUNDARY
CHECK must be the sum of all prior stage latencies and all prior boundary latencies up to
and including this boundary. Compute it inside the boundary block; it may not be deferred
to [A-11]. [Apply SC-3 at every boundary block.]

**SC-4 — Binary freshness verdict**: Each boundary block `Verdict` must read `FRESH`
or `STALE`, derived by comparing the cumulative elapsed against the [A-01] threshold.
Cite [A-01] by token; do not restate its value. A block without a Verdict fails SC-4.
[Apply SC-4 at every boundary block.]

**SC-5 — Immutability of staleness threshold**: Finance must append to [A-01] verbatim:
"This threshold is fixed. No subsequent role may revise it after Stage 1 is written."
Operations and Commerce may not redeclare or adjust the threshold.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required outputs at the end of
Finance and Operations respectively. Each is a checklist with named criterion identifiers.
The next role may not begin until all items are ✓. [Apply SC-6 before role transitions.]

**SC-7 — Stage table format with Stage Latency**: Every stage block is a markdown table
with required columns: `Stage Latency | Schema In | Schema Out | Data Loss Flag`. Stage
Latency must be an explicit annotation (value, range, or characterization); it may not be
omitted or left to be inferred from boundary elapsed totals alone.
[Apply SC-7 at every stage block.]

**SC-8 — Trade-off analysis as required section**: [A-14] TRADE-OFF ANALYSIS is a
structurally required named section — not optional. It must cite [A-02] by token (manual
baseline), [A-01] by token (threshold dimension), and [A-13] by token (numeric incumbent
total). It must name ≥1 alternative data propagation pattern and supply ≥2 quantified or
qualified trade-off dimensions. A section that omits any of the three tokens fails SC-8.
[Apply SC-8 when producing [A-14].]

**SC-9 — Per-boundary incumbent equivalent cell form**: Every `Incumbent Equiv.` cell must
cite `[A-02]` by token and name the corresponding manual step from [A-02] along with its
duration. Required form: `[A-02]: [named step + duration]`. A bare duration without the
`[A-02]` token is a protocol violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Before writing [A-14], produce [A-13]
INCUMBENT TOTAL. Sum all `Incumbent Equiv.` cell values from [A-04], [A-07], and [A-10].
Show additive breakdown by role (Finance subtotal, Operations subtotal, Commerce subtotal,
Grand Total). [A-14] must cite [A-13] by token as the numeric comparison endpoint. A
TRADE-OFF ANALYSIS that cites [A-02] directly — or only prose — without first producing
and citing [A-13] fails SC-10. [Apply SC-10 before writing [A-14].]

---

### ROLE 1 — Finance

[Finance runs first. No Citing line required.]

**[A-01] DOMAIN CONTEXT** — Write this before Stage 1. Include:
- Entity vocabulary: purchase order (PO), AP accrual line, supplier receipt voucher,
  WMS stock-on-hand quantity, catalog availability flag
- Downstream consumer and business cadence (e.g., nightly GL close at 23:00)
- Staleness SLA: maximum elapsed time from supplier EDI confirmation to catalog
  availability flag update. Declare as an integer with unit.
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-02] INCUMBENT BASELINE** — Write immediately after [A-01] and before Stage 1.
Describe the manual PO-to-inventory process this pipeline replaces. Include ≥3 named
manual steps with their typical durations (e.g., "Manual PO fax to supplier: 2 h",
"Warehouse clerk stock count entry: 45 min"). Use ≥1 entity name from [A-01]. This
artifact is the source for all `Incumbent Equiv.` cells in [A-04], [A-07], and [A-10].

**[A-03] STAGE TRACE — Finance** — Trace PO creation → AP accrual → GL posting. Per SC-7:
each stage is a table with columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`.
Per SC-2: complete the BOUNDARY BLOCK SCHEMA table before writing each next stage.

- Stage 1: Supplier EDI confirmation → PO entry in ERP
- Stage 2: PO entry → AP accrual line creation
- Stage 3: AP accrual line → GL posting

**[A-04] BOUNDARY CHECKS — Finance** — Per SC-2: one block between Stage 1–Stage 2, one
between Stage 2–Stage 3, one after Stage 3. Each block conforms to BOUNDARY BLOCK SCHEMA
(7 columns). [SC-3 applies.] [SC-4 applies.] [SC-9 applies: every Incumbent Equiv. cell
must use form `[A-02]: [named step + duration]`.]

**[A-05] PHASE GATE 1** — Produce and tick before Operations begins. Mark each ✓ or ✗:
- [ ] [A-01] contains staleness SLA as integer with unit, plus SC-5 verbatim statement
- [ ] [A-02] includes ≥3 named manual steps with durations and ≥1 entity from [A-01]
- [ ] Every stage in [A-03] is a table with all four required columns per SC-7
- [ ] Every block in [A-04] has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] Every `Elapsed (cumul.)` is a computed numeric sum inside the block (SC-3)
- [ ] Every `Verdict` is FRESH or STALE derived from [A-01] threshold (SC-4)
- [ ] Every `Incumbent Equiv.` cell uses form `[A-02]: [named step + duration]` (SC-9)

Operations may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Trace receiving dock scan → WMS stock-on-hand update.
Per SC-7 (stage tables with Stage Latency column). Per SC-2, complete BOUNDARY BLOCK SCHEMA
tables before advancing. Use entity names from [A-01].

- Stage 4: AP accrual confirmation → Warehouse receiving dock scan
- Stage 5: Dock scan → WMS stock-on-hand update

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: Elapsed (cumul.) extends the final value in [A-04]; do not reset to zero.]
[SC-4: Verdict vs [A-01] threshold; do not redeclare threshold value.]
[SC-9: every Incumbent Equiv. cell form `[A-02]: [named step from [A-02] + duration]`.]

**[A-08] PHASE GATE 2** — Produce and tick before Commerce begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] is a table with all four required columns per SC-7
- [ ] Every block in [A-07] has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] final value; not reset (SC-3)
- [ ] Every Verdict derives from [A-01] threshold without redeclaring its value (SC-4, SC-5)
- [ ] Every `Incumbent Equiv.` cell uses form `[A-02]: [named step + duration]` (SC-9)

Commerce may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]
([A-04] is two roles prior — Finance boundary checks. Cite it explicitly to confirm the
elapsed chain is unbroken. Citing only [A-07] without [A-04] fails SC-1.)

**[A-09] STAGE TRACE — Commerce** — Trace WMS snapshot → Commerce platform cache →
catalog availability flag. Per SC-7. Per SC-2. Use entity names from [A-01].

- Stage 6: WMS stock-on-hand quantity → Commerce platform inventory cache
- Stage 7: Commerce platform cache → Storefront catalog availability flag

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: extend from final value in [A-07].]
[SC-4: Verdict vs [A-01] threshold.]
[SC-9: every Incumbent Equiv. cell form `[A-02]: [named step + duration]`.]

**[A-11] STALE ANALYSIS** — Using Elapsed (cumul.) values from [A-10] final row:

| Entity ([A-01]) | Normal elapsed | Failure-mode elapsed | [A-01] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

Produce separate rows for normal-operation and failure-mode staleness.
Cite [A-01] by token; do not restate the numeric threshold value.

**[A-12] RECOVERY PRESCRIPTIONS** — For every `no handling — see [A-12]` annotation in
[A-04]/[A-07]/[A-10] and every `Data Loss Flag: YES` in [A-03]/[A-06]/[A-09], provide a
specific named recovery action. Required formula structure:

`Fall back to [A-02] if [specific named failure condition]`

Cite [A-02] using this exact formula at least once.

**[A-13] INCUMBENT TOTAL** — Per SC-10: produce this section immediately before [A-14].

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Finance | [sum of [A-04] Incumbent Equiv. values] | [step names from [A-02]] |
| Operations | [sum of [A-07] Incumbent Equiv. values] | [step names from [A-02]] |
| Commerce | [sum of [A-10] Incumbent Equiv. values] | [step names from [A-02]] |
| **Grand Total** | | |

[A-14] must cite this table by token `[A-13]` as the numeric comparison endpoint.

**[A-14] TRADE-OFF ANALYSIS** — [SC-8 applies.] Required named section. Cite [A-01] for
the threshold dimension, [A-02] for manual baseline framing, and [A-13] as the numeric
pipeline-vs-manual total. Name ≥1 alternative data propagation pattern (e.g., event-driven
CDC, real-time dual-write). Provide ≥2 quantified or qualified trade-off dimensions using
the [A-13] Grand Total as the comparison endpoint. A section that cites [A-02] without
citing [A-13] fails SC-8 and SC-10.

---

---

## V-02

**Axis**: Output format — REGISTER DECLARATION as primary C-34/C-35 enforcement vehicle

**Hypothesis**: Concentrating C-34/C-35 compliance specification in the REGISTER DECLARATION
— via an explicit `Incumbent Equiv.` cell-form entry and a SECTION FORMAT row for
INCUMBENT TOTAL — creates a single-location authoritative reference. SC-9 and SC-10
exist but are callbacks to the REGISTER DECLARATION rather than primary declarations.
An evaluator can verify C-34 (cell form) and C-35 (section format) by consulting the
REGISTER DECLARATION alone, without reading structural constraints or role instructions.
Natural Finance → Operations → Commerce order preserves C-16 PASS, isolating the format
axis. C-26 FAIL (natural order) is expected.

---

You are tracing data through a retail purchase-order-to-inventory pipeline. Three expert
roles run in the sequence **Finance → Operations → Commerce**. Finance establishes the PO
staleness SLA and manual-process baseline. Operations and Commerce extend the trace and cite
Finance's artifacts by token; they may not redeclare or re-derive either the threshold or
the incumbent baseline.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Finance | Entity vocabulary, staleness SLA (immutable), downstream consumer, business cadence |
| [A-02] | INCUMBENT BASELINE | Finance | Manual PO and AP process; ≥3 named steps with durations; ≥1 entity from [A-01] |
| [A-03] | STAGE TRACE — Finance | Finance | PO creation → AP accrual → GL posting; stage tables |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | Boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-02] |
| [A-05] | PHASE GATE 1 | Finance | Checklist; all ✓ before Operations |
| [A-06] | STAGE TRACE — Operations | Operations | Dock scan → WMS update; stage tables |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | Boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cites [A-02] |
| [A-08] | PHASE GATE 2 | Operations | Checklist; all ✓ before Commerce |
| [A-09] | STAGE TRACE — Commerce | Commerce | WMS snapshot → platform cache → availability flag; stage tables |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | Boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cites [A-02] |
| [A-11] | STALE ANALYSIS | Commerce | Normal and failure-mode elapsed vs [A-01] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point; formula `Fall back to [A-02] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Commerce | Aggregates all Incumbent Equiv. cells; breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required section; cites [A-01], [A-02], [A-13] by token; ≥1 pattern; ≥2 dimensions |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout. The REGISTER DECLARATION is the
authoritative compliance reference for all field forms and section formats. Structural
constraints (SC-x) are callbacks to this section; they do not independently define
compliance requirements.

**Part A — Field compliance markers (boundary block columns):**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-01] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum of all prior stage and boundary latencies, in minutes | Partial sum; deferred total |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE` | Any other value; FRESH/STALE not derived from [A-01] |
| Error handling | `Error Handling` | Named retry/dead-letter/rollback mechanism, or exactly `no handling — see [A-12]` | Silence; "TBD"; omitted column |
| Schema change | `Schema Delta` | Named field-level additions, removals, or type changes, or exactly `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | "errors may occur"; generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-02]: [named manual step + duration]` — the `[A-02]` token is required; a cell omitting it is a protocol violation | Bare duration; token omitted; column absent |
| Stage latency | `Stage Latency` (stage table) | Explicit value, range, or characterization (real-time / near-real / batch / daily) | Inferred from boundary elapsed |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Markdown table with columns: Role \| Incumbent Equiv. subtotal \| Steps cited; rows for Finance, Operations, Commerce, and Grand Total; all values numeric | Prose-only summary; missing role breakdown; no Grand Total row |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | Must include token citations `[A-01]`, `[A-02]`, and `[A-13]` — all three required; ≥1 alternative pattern named; ≥2 trade-off dimensions | Missing any one of the three tokens; pattern not named |

---

### BOUNDARY BLOCK SCHEMA

Declared here as a standalone section before any role begins. Every required column is
named below. An evaluator verifies boundary block completeness by column existence alone;
role instructions reference this section by name only.

**Every boundary block must be a markdown table with these columns, in this order:**
`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

All column header names must match the REGISTER DECLARATION Part A spellings exactly.
A column that is absent, renamed, or rendered as a labeled field list fails the schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Finance opens with
`Citing: [A-xx], [A-yy], ...`. Prose back-references do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding
boundary table is fully populated per the BOUNDARY BLOCK SCHEMA. [Apply SC-2 before every
stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` is computed inside each boundary block;
not deferred. [Per REGISTER DECLARATION Part A, Elapsed (cumul.) row.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` from [A-01] threshold. Cite
[A-01] by token. [Per REGISTER DECLARATION Part A, Freshness verdict row.]

**SC-5 — Immutability**: Finance appends to [A-01] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written."

**SC-6 — Phase gate**: [A-05] and [A-08] are required checklists at phase transitions.
Next role may not begin until all items ✓.

**SC-7 — Stage table format**: Every stage block is a table with columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. [Per REGISTER DECLARATION
Part A, Stage latency row.] [Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [Per REGISTER DECLARATION Part B, TRADE-OFF
ANALYSIS row.] All three tokens required. Named alternative pattern required. ≥2 dimensions
required. [Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: [Per REGISTER DECLARATION Part A, Incumbent
equivalent row.] Form: `[A-02]: [named step + duration]`. Token omission is a protocol
violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [Per REGISTER DECLARATION Part B, INCUMBENT
TOTAL row.] Produce [A-13] immediately before [A-14]. [A-14] cites [A-13] by token.
[Apply SC-10 before writing [A-14].]

---

### ROLE 1 — Finance

[Finance runs first. No Citing line required.]

**[A-01] DOMAIN CONTEXT** — Write before Stage 1. Entity vocabulary: purchase order (PO),
AP accrual line, supplier receipt voucher, WMS stock-on-hand quantity, catalog availability
flag. Include downstream consumer, business cadence, and staleness SLA as an integer with
unit. Append SC-5 verbatim immutability statement.

**[A-02] INCUMBENT BASELINE** — Write immediately after [A-01] and before Stage 1. Describe
the manual PO-to-inventory process replaced by this pipeline. Include ≥3 named manual steps
with durations. Use ≥1 entity from [A-01]. This is the source artifact for all `Incumbent
Equiv.` cells across all roles.

**[A-03] STAGE TRACE — Finance** — Stage 1: Supplier EDI → PO entry. Stage 2: PO entry →
AP accrual. Stage 3: AP accrual → GL posting. Per SC-7 (stage tables). Per SC-2 (boundary
table before stage advance).

**[A-04] BOUNDARY CHECKS — Finance** — One boundary table after each stage per BOUNDARY
BLOCK SCHEMA. [SC-3, SC-4, SC-9 apply.] Column header spellings must match REGISTER
DECLARATION Part A exactly.

**[A-05] PHASE GATE 1** — Tick ✓ or ✗ before Operations:
- [ ] [A-01] SLA declared as integer with unit; SC-5 verbatim statement present
- [ ] [A-02] includes ≥3 named steps with durations; ≥1 entity from [A-01]
- [ ] Every stage in [A-03] has four required columns per SC-7
- [ ] Every block in [A-04] has all seven columns per BOUNDARY BLOCK SCHEMA; headers
      match REGISTER DECLARATION Part A spellings exactly
- [ ] Every `Incumbent Equiv.` cell form: `[A-02]: [named step + duration]` (SC-9)

Operations may not begin until all items ✓. [SC-6.]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Stage 4: AP accrual confirmation → Dock scan.
Stage 5: Dock scan → WMS stock-on-hand update. Per SC-7. Per SC-2.

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns, headers
match REGISTER DECLARATION Part A exactly). [SC-3: extend Elapsed (cumul.) from [A-04]
final value.] [SC-4, SC-9 apply.]

**[A-08] PHASE GATE 2** — Tick ✓ or ✗ before Commerce:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every [A-06] stage table has four required columns per SC-7
- [ ] Every [A-07] boundary table has seven columns; headers match REGISTER DECLARATION
- [ ] `Elapsed (cumul.)` extends [A-04] final value; no reset (SC-3)
- [ ] Every `Incumbent Equiv.` cell: `[A-02]: [named step + duration]` (SC-9)

Commerce may not begin until all items ✓. [SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

**[A-09] STAGE TRACE — Commerce** — Stage 6: WMS snapshot → Commerce platform cache.
Stage 7: Platform cache → Catalog availability flag. Per SC-7. Per SC-2.

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns, headers
match REGISTER DECLARATION Part A exactly). [SC-3: extend from [A-07].] [SC-4, SC-9.]

**[A-11] STALE ANALYSIS** — Table: Entity | Normal elapsed | Failure-mode elapsed |
[A-01] threshold | Verdict. Cite [A-01] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — Named recovery per loss point and no-handling flag.
Formula: `Fall back to [A-02] if [specific condition]`.

**[A-13] INCUMBENT TOTAL** — [Per REGISTER DECLARATION Part B, INCUMBENT TOTAL row.
Per SC-10.] Produce as a table immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Finance | | |
| Operations | | |
| Commerce | | |
| **Grand Total** | | |

Cite this section as `[A-13]` in [A-14].

**[A-14] TRADE-OFF ANALYSIS** — [Per REGISTER DECLARATION Part B, TRADE-OFF ANALYSIS row.
Per SC-8.] Required. Cite `[A-01]`, `[A-02]`, and `[A-13]` — all three tokens required.
Name ≥1 alternative pattern. Provide ≥2 trade-off dimensions with [A-13] Grand Total as
the numeric comparison endpoint.

---

---

## V-03

**Axis**: Inertia framing — INCUMBENT BASELINE as first-produced artifact before DOMAIN CONTEXT

**Hypothesis**: When the manual-process baseline is produced before any domain context or
stage trace, every subsequent artifact is written with the incumbent story already in scope.
The `Incumbent Equiv.` cells at each boundary can reference named steps from an artifact
visible since the first line of output — eliminating the forward-citation gap that arises
when roles must reference a baseline not yet written. Role sequence Operations → Finance →
Commerce is chosen because Operations is the natural custodian of the manual-process story
(it lives the steps daily); Finance then frames the SLA against that known cost; Commerce
closes at the customer-facing staleness consequence. The inertia-first structure also
satisfies C-16 (cross-role citation) naturally because the baseline is cited by all
subsequent roles from a shared, first-positioned artifact.

---

You are tracing data through a retail purchase-order-to-inventory pipeline. Three expert
roles run in the sequence **Operations → Finance → Commerce**. Operations runs first and
produces both the manual-process baseline and the domain context — establishing the
incumbent story before any pipeline stage is traced. Finance and Commerce cite Operations'
baseline and threshold artifacts; they may not redeclare or re-derive either.

The incumbent manual process is the primary competitive frame for this trace. Every
pipeline stage is evaluated against what the manual process would cost at the same point.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Operations | Manual PO and warehouse process replaced by this pipeline; ≥3 named steps with durations; produced FIRST, before [A-02] |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, staleness SLA (immutable after Stage 1), downstream consumer, business cadence; declares SLA with reference to [A-01] total duration |
| [A-03] | STAGE TRACE — Operations | Operations | Dock scan → WMS update; stage tables |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; Incumbent Equiv. cites [A-01] |
| [A-05] | PHASE GATE 1 | Operations | Checklist; all ✓ before Finance begins |
| [A-06] | STAGE TRACE — Finance | Finance | PO creation → AP accrual → GL posting; stage tables |
| [A-07] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cites [A-01] |
| [A-08] | PHASE GATE 2 | Finance | Checklist; all ✓ before Commerce begins |
| [A-09] | STAGE TRACE — Commerce | Commerce | WMS snapshot → platform cache → availability flag; stage tables |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cites [A-01] |
| [A-11] | STALE ANALYSIS | Commerce | Normal and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point; formula `Fall back to [A-01] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Commerce | Aggregates all Incumbent Equiv. cells from [A-04], [A-07], [A-10]; breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required section; cites [A-01], [A-02], and [A-13] by token; ≥1 alternative; ≥2 dimensions |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**Per-field compliance markers (tabular register):**

| Required Field | Compliance Marker | Disqualifying form |
|----------------|-------------------|--------------------|
| Domain entity at boundary | `Entity` column — named entity from [A-02] | "data" or "records" alone |
| Error handling | `Error Handling` column — named mechanism or `no handling — see [A-12]` | Silence / omitted |
| Elapsed (cumulative) | `Elapsed (cumul.)` column — numeric sum of all prior latencies | Deferred; partial |
| Freshness verdict | `Verdict` column — `FRESH` or `STALE` vs [A-02] threshold | Any other value |
| Schema state | `Schema Delta` column — named field changes or `NONE` | Omitted |
| Data loss flag | `Data Loss Flag` column — `YES — [named loss point]` or `NO` | Generic language |
| Stage latency | `Stage Latency` column (stage tables) — explicit value, range, or characterization | Inferred from boundary |
| Incumbent equivalent | `Incumbent Equiv.` column — form `[A-01]: [named step + duration]`; token required | Bare duration; token omitted |

---

### BOUNDARY BLOCK SCHEMA

Standalone section before any role output. Every boundary block must be a markdown table
with the following columns in this order. An evaluator verifies completeness by column
existence alone.

| Column | Required Content |
|--------|-----------------|
| Entity | Named entity from [A-02] vocabulary. Generic labels fail. |
| Elapsed (cumul.) | Sum of all prior stage and boundary latencies, in minutes. Computed inside this block. |
| Verdict | `FRESH` or `STALE` — vs [A-02] threshold. Cite [A-02] by token. |
| Error Handling | Named mechanism, or `no handling — see [A-12]`. Silence fails. |
| Schema Delta | Named field-level changes, or `NONE`. |
| Data Loss Flag | `YES — [named loss point]` or `NO`. Generic language fails. |
| Incumbent Equiv. | `[A-01]: [named manual step + duration]`. `[A-01]` token required; bare duration is protocol violation. |

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Operations opens with
`Citing: [A-xx], [A-yy], ...`. Citing `[A-01]` (INCUMBENT BASELINE) is required for every
subsequent role — it must appear in every Citing line. Prose back-references do not satisfy
SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding
BOUNDARY CHECK table is fully populated per BOUNDARY BLOCK SCHEMA.
[Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` computed inside each block; not deferred.
[Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` vs [A-02] threshold. Cite [A-02]
by token. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Operations must append to [A-02] verbatim: "This threshold is
fixed. No subsequent role may revise it after Stage 1 is written." The threshold value is
derived from [A-01] total duration plus pipeline latency headroom; it must be declared as
an integer with unit.

**SC-6 — Phase gate**: [A-05] and [A-08] are required checklists. Next role may not begin
until all items ✓.

**SC-7 — Stage table format**: Every stage block is a table with columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. Stage Latency must be explicit.
[Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [A-14] is a structurally required named section.
Must cite [A-01] (incumbent baseline), [A-02] (SLA dimension), and [A-13] (numeric total)
by token. Names ≥1 alternative pattern. ≥2 dimensions. All three tokens required.
[Apply SC-8 when producing [A-14].]

**SC-9 — Per-boundary incumbent equivalent**: Every `Incumbent Equiv.` cell form:
`[A-01]: [named manual step + duration]`. The `[A-01]` token is required; bare durations
are protocol violations. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Produce [A-13] immediately before [A-14].
Sum Incumbent Equiv. values from [A-04], [A-07], [A-10]; show role breakdown; cite [A-13]
in [A-14] as numeric comparison endpoint. [Apply SC-10 before writing [A-14].]

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required. The incumbent baseline leads.]

**[A-01] INCUMBENT BASELINE** — Write this FIRST, before any domain context or stage trace.
Describe the manual warehouse-and-procurement process this pipeline replaces. Include ≥3
named manual steps with their typical durations (e.g., "Paper PO fax to supplier: 4 h",
"Receiving clerk manual count and entry: 90 min", "Spreadsheet stock update to shared
drive: 30 min"). Use entity names that will reappear in [A-02]. This artifact is the source
for every `Incumbent Equiv.` cell in [A-04], [A-07], and [A-10]. All subsequent roles
must cite [A-01] in their opening Citing line.

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (must reuse ≥2 entity names from [A-01]): purchase order, receiving
  record, WMS stock-on-hand quantity, catalog availability flag
- Downstream consumer and business cadence
- Staleness SLA: declare as an integer with unit. The SLA must be derived from [A-01]:
  state explicitly "SLA = [A-01] total + [headroom]" to show the baseline anchors the
  threshold.
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Operations** — Trace dock scan → WMS update. Per SC-7 (stage
tables). Per SC-2 (boundary before stage advance).

- Stage 1: Supplier delivery arrival → Dock scan event capture
- Stage 2: Dock scan → WMS stock-on-hand quantity update

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3, SC-4.] [SC-9: every Incumbent Equiv. cell = `[A-01]: [named step + duration]`.]

**[A-05] PHASE GATE 1** — Tick ✓ or ✗ before Finance begins:
- [ ] [A-01] includes ≥3 named manual steps with durations
- [ ] [A-02] reuses ≥2 entity names from [A-01]; SLA derived from [A-01] total; SC-5
      verbatim statement present
- [ ] Every [A-03] stage table has four required columns per SC-7
- [ ] Every [A-04] boundary table has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)

Finance may not begin until all items ✓. [SC-6.]

---

### ROLE 2 — Finance

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Finance** — Trace PO creation → AP accrual → GL posting. Per SC-7.
Per SC-2. Use entity names from [A-02].

- Stage 3: Supplier EDI confirmation → PO entry in ERP
- Stage 4: PO entry → AP accrual line creation
- Stage 5: AP accrual line → GL posting

**[A-07] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: extend Elapsed (cumul.) from [A-04] final value; do not reset.]
[SC-4: Verdict vs [A-02] threshold; cite [A-02] by token.]
[SC-9: every Incumbent Equiv. cell = `[A-01]: [named step from [A-01] + duration]`.]

**[A-08] PHASE GATE 2** — Tick ✓ or ✗ before Commerce begins:
- [ ] Citing line includes [A-01] (SC-1)
- [ ] Every [A-06] stage table has four required columns per SC-7
- [ ] Every [A-07] boundary table has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] `Elapsed (cumul.)` extends [A-04] final value; not reset (SC-3)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)

Commerce may not begin until all items ✓. [SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

**[A-09] STAGE TRACE — Commerce** — Stage 6: WMS snapshot → Commerce platform cache.
Stage 7: Platform cache → Catalog availability flag. Per SC-7. Per SC-2.

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: extend from [A-07].] [SC-4: vs [A-02] threshold.] [SC-9: `[A-01]: [step + dur]`.]

**[A-11] STALE ANALYSIS** — Table: Entity | Normal elapsed | Failure-mode elapsed |
[A-02] threshold | Verdict. The [A-02] threshold was derived from [A-01] total per SC-5;
cite both tokens.

**[A-12] RECOVERY PRESCRIPTIONS** — Named recovery per loss point and no-handling flag.
Required formula: `Fall back to [A-01] if [specific condition]`.

**[A-13] INCUMBENT TOTAL** — Per SC-10. Produce immediately before [A-14].

| Role | Incumbent Equiv. subtotal | Steps cited from [A-01] |
|------|--------------------------|------------------------|
| Operations | | |
| Finance | | |
| Commerce | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — Per SC-8. Cite [A-01] (incumbent baseline origin), [A-02]
(SLA threshold), [A-13] (numeric total) — all three tokens required. Name ≥1 alternative
pattern. ≥2 trade-off dimensions using [A-13] Grand Total as the pipeline-vs-manual
comparison endpoint.

---

---

## V-04

**Axes (combined)**: Role sequence (Commerce → Operations → Finance, maximally non-natural)
+ Lifecycle emphasis (C-34 forward-citation stress test under knowledge asymmetry)

**Hypothesis**: When the role producing the incumbent baseline (Finance) runs last, Commerce
and Operations must produce `Incumbent Equiv.` cells citing `[A-02]` before Finance has
written that artifact. The `[A-02]` token is pre-declared in the ARTIFACT REGISTRY;
Commerce and Operations cite it as a forward reference using domain knowledge of manual
retail processes, not content knowledge of [A-02]. Finance runs last and: (a) writes
DOMAIN CONTEXT and INCUMBENT BASELINE, (b) traces its own pipeline stages, and (c)
aggregates INCUMBENT TOTAL from all three roles' boundary blocks — validating the
forward citations against the baseline it has now produced. This creates the strongest
possible C-34 citation stress: forward-token citation makes laziness detectable as a
missing `[A-02]` token, not a prose gap. C-16 PARTIAL risk (long citation chain) is
mitigated by requiring Finance's Citing line to enumerate all three prior artifact tokens.

---

You are tracing data through a retail purchase-order-to-inventory pipeline. Three expert
roles run in the sequence **Commerce → Operations → Finance**. Natural domain order would
be Finance → Operations → Commerce; running Finance last creates a forward-citation
requirement: Commerce and Operations must cite `[A-02]` (INCUMBENT BASELINE, produced by
Finance) in every `Incumbent Equiv.` boundary cell before Finance has written [A-02].

The `[A-02]` token is pre-declared in the ARTIFACT REGISTRY. Commerce and Operations must
cite it structurally (by registered token) using their domain knowledge of the manual
retail process. Finance will verify citation consistency when it produces [A-02] last.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Commerce | Entity vocabulary, staleness SLA (immutable), downstream consumer, business cadence |
| [A-02] | INCUMBENT BASELINE | Finance | Manual PO and AP process; ≥3 named steps with durations; ≥1 entity from [A-01]; produced last by Finance |
| [A-03] | STAGE TRACE — Commerce | Commerce | WMS snapshot → platform cache → availability flag; stage tables |
| [A-04] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; Incumbent Equiv. cites [A-02] FORWARD (Finance produces [A-02] after Commerce) |
| [A-05] | PHASE GATE 1 | Commerce | Checklist; all ✓ before Operations begins |
| [A-06] | STAGE TRACE — Operations | Operations | Dock scan → WMS update; stage tables |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cites [A-02] forward |
| [A-08] | PHASE GATE 2 | Operations | Checklist; all ✓ before Finance begins |
| [A-09] | STAGE TRACE — Finance | Finance | PO creation → AP accrual → GL posting; stage tables |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends elapsed from [A-07] |
| [A-11] | STALE ANALYSIS | Finance | Normal and failure-mode elapsed vs [A-01] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery; formula `Fall back to [A-02] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Finance | Aggregates Incumbent Equiv. cells from [A-04], [A-07], [A-10]; breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Finance | Required section; cites [A-01], [A-02], [A-13] by token; ≥1 alternative; ≥2 dimensions |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**Per-field compliance markers:**

| Required Field | Compliance Marker | Disqualifying form |
|----------------|-------------------|--------------------|
| Domain entity at boundary | `Entity` column — named entity from [A-01] | "data" or "records" alone |
| Error handling | `Error Handling` column — named mechanism or `no handling — see [A-12]` | Silence; omitted |
| Elapsed (cumulative) | `Elapsed (cumul.)` column — sum of all prior latencies | Deferred; partial |
| Freshness verdict | `Verdict` column — `FRESH` or `STALE` vs [A-01] threshold | Other values |
| Schema state | `Schema Delta` column — named changes or `NONE` | Omitted |
| Data loss flag | `Data Loss Flag` column — `YES — [loss point]` or `NO` | Generic language |
| Stage latency | `Stage Latency` column (stage tables) — explicit annotation | Inferred only |
| Incumbent equivalent | `Incumbent Equiv.` column — form `[A-02]: [named manual step + duration]`; token required even when [A-02] is not yet produced | Bare duration; token omitted |

---

### BOUNDARY BLOCK SCHEMA

Standalone pre-role section. Every boundary block must be a markdown table with the
following columns in this order:

| Column | Required Content |
|--------|-----------------|
| Entity | Named entity from [A-01]. Generic labels fail. |
| Elapsed (cumul.) | Sum of all prior latencies. Computed inside this block. |
| Verdict | `FRESH` or `STALE` — vs [A-01] threshold. Cite [A-01] by token. |
| Error Handling | Named mechanism, or `no handling — see [A-12]`. Silence fails. |
| Schema Delta | Named changes, or `NONE`. |
| Data Loss Flag | `YES — [loss point]` or `NO`. |
| Incumbent Equiv. | `[A-02]: [named manual step + duration]`. `[A-02]` token required. Commerce and Operations: cite [A-02] as a forward reference; use domain knowledge of the manual retail process to name the step and estimate duration. Finance will verify consistency when producing [A-02]. |

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Commerce opens with
`Citing: [A-xx], [A-yy], ...`. Finance (last) must cite [A-01] (Commerce, two roles prior),
[A-04] (Commerce boundaries), and [A-07] (Operations boundaries) — all three required.
Citing only [A-07] without [A-01] and [A-04] fails SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding
BOUNDARY CHECK table is fully populated per BOUNDARY BLOCK SCHEMA.
[Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` computed inside each block.
[Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` vs [A-01] threshold. Cite [A-01]
by token. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Commerce must append to [A-01] verbatim: "This threshold is
fixed. No subsequent role may revise it after Stage 1 is written." Operations and Finance
may not redeclare or adjust.

**SC-6 — Phase gate**: [A-05] and [A-08] are required checklists. Next role may not begin
until all items ✓.

**SC-7 — Stage table format**: Every stage block is a table with columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. Stage Latency must be explicit.
[Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [A-14] is required. Cites [A-01], [A-02], [A-13]
by token. ≥1 alternative. ≥2 dimensions. [Apply SC-8 when producing [A-14].]

**SC-9 — Per-boundary incumbent equivalent (forward-citation)**: Every `Incumbent Equiv.`
cell must cite `[A-02]` by token regardless of whether Finance has produced [A-02] yet.
Form: `[A-02]: [named manual step + estimated duration]`. Commerce and Operations: use
domain knowledge of manual retail processes. Finance-last will verify consistency.
Bare durations without `[A-02]` are protocol violations. [Apply SC-9 at every boundary.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Finance produces [A-13] immediately before
[A-14]. Sum Incumbent Equiv. values from [A-04], [A-07], [A-10]. Show breakdown by role.
[A-14] cites [A-13] by token as numeric comparison endpoint. Finance may also note whether
Commerce and Operations forward-citations were consistent with [A-02] named steps.
[Apply SC-10 before writing [A-14].]

---

### ROLE 1 — Commerce

[Commerce runs first. No Citing line required. `[A-02]` is pre-declared; Finance will
produce it last. Cite `[A-02]` in every Incumbent Equiv. cell as a forward reference.]

**[A-01] DOMAIN CONTEXT** — Write before Stage 1. Include:
- Entity vocabulary: WMS stock-on-hand quantity, Commerce platform inventory cache,
  catalog availability flag, purchase order, supplier receipt
- Downstream consumer and business cadence (e.g., customer-facing catalog refresh cycle)
- Staleness SLA: maximum elapsed time from supplier receipt to catalog flag update.
  Declare as an integer with unit.
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.

- Stage 1: WMS stock-on-hand quantity → Commerce platform inventory cache
- Stage 2: Platform cache → Storefront catalog availability flag

**[A-04] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3.] [SC-4: Verdict vs [A-01] threshold.]
[SC-9: FORWARD CITATION — `Incumbent Equiv.` cells must be form `[A-02]: [named step +
duration]`. Finance has not yet produced [A-02]; use domain knowledge of the manual retail
process. Finance will verify consistency when it writes [A-02] last.]

**[A-05] PHASE GATE 1** — Tick ✓ or ✗ before Operations begins:
- [ ] [A-01] contains SLA as integer with unit; SC-5 verbatim statement present
- [ ] Every [A-03] stage table has four required columns per SC-7
- [ ] Every [A-04] boundary table has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] Every `Incumbent Equiv.` cell uses form `[A-02]: [named step + duration]`; `[A-02]`
      token present even as a forward reference (SC-9)

Operations may not begin until all items ✓. [SC-6.]

---

### ROLE 2 — Operations

Citing: [A-01], [A-04]
([A-01] is Commerce's domain context. [A-04] is Commerce's boundary checks. Do not cite
`[A-02]` in the Citing line — it has not been produced yet. `[A-02]` appears only in
Incumbent Equiv. cells as a forward reference per SC-9.)

**[A-06] STAGE TRACE — Operations** — Per SC-7. Per SC-2.

- Stage 3: Supplier delivery arrival → Dock scan event capture
- Stage 4: Dock scan → WMS stock-on-hand quantity update

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: extend Elapsed (cumul.) from [A-04] final value.]
[SC-4: Verdict vs [A-01] threshold.]
[SC-9: FORWARD CITATION — every `Incumbent Equiv.` cell = `[A-02]: [named manual step +
duration]`. Finance will produce [A-02] after you. Use domain knowledge to name the step
and estimate duration.]

**[A-08] PHASE GATE 2** — Tick ✓ or ✗ before Finance begins:
- [ ] Citing line names [A-01], [A-04] (SC-1)
- [ ] Every [A-06] stage table has four required columns per SC-7
- [ ] Every [A-07] boundary table has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] `Elapsed (cumul.)` extends [A-04] final value; not reset (SC-3)
- [ ] Every `Incumbent Equiv.` cell: `[A-02]: [named step + duration]` — forward reference
      accepted (SC-9)

Finance may not begin until all items ✓. [SC-6.]

---

### ROLE 3 — Finance

Citing: [A-01], [A-04], [A-07]
([A-01] is Commerce's domain context, two roles prior. [A-04] and [A-07] are Commerce and
Operations boundary checks respectively. All three tokens required per SC-1.)

**[A-02] INCUMBENT BASELINE** — Produce this first in Finance's output. Describe the manual
PO-to-inventory process this pipeline replaces. Include ≥3 named manual steps with
durations. Use ≥1 entity from [A-01]. These named steps should correspond to the manual
steps Commerce and Operations cited (forward) in their `Incumbent Equiv.` cells. If a
forward citation names a step that does not appear here, note the discrepancy.

**[A-09] STAGE TRACE — Finance** — Per SC-7. Per SC-2.

- Stage 5: Supplier EDI confirmation → PO entry in ERP
- Stage 6: PO entry → AP accrual line creation
- Stage 7: AP accrual line → GL posting

**[A-10] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: extend from [A-07] final value.]
[SC-4: Verdict vs [A-01] threshold.]
[SC-9: Finance's own Incumbent Equiv. cells also cite [A-02] by token — no forward-citation
ambiguity here; Finance has now produced [A-02].]

**[A-11] STALE ANALYSIS** — Normal and failure-mode elapsed vs [A-01] threshold.
Cite [A-01] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — Named recovery per loss point and no-handling flag.
Formula: `Fall back to [A-02] if [specific condition]`.

**[A-13] INCUMBENT TOTAL** — Per SC-10. Produce immediately before [A-14].

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Commerce | [sum of [A-04] values] | |
| Operations | [sum of [A-07] values] | |
| Finance | [sum of [A-10] values] | |
| **Grand Total** | | |

Optionally note any Commerce/Operations forward citations that were inconsistent with [A-02]
named steps.

**[A-14] TRADE-OFF ANALYSIS** — Per SC-8. Required. Cite [A-01] (threshold), [A-02]
(baseline), [A-13] (numeric total) — all three tokens required. Name ≥1 alternative pattern.
≥2 trade-off dimensions with [A-13] Grand Total as the pipeline-vs-manual comparison
endpoint.

---

---

## V-05

**Axes (combined)**: Inertia framing + Output format (dual-register: Finance/Operations
tabular, Commerce conversational) via REGISTER TRANSLATION TABLE extended to C-34/C-35

**Hypothesis**: The REGISTER TRANSLATION TABLE — R9 V-05's strongest architectural
contribution — can accommodate C-34/C-35 by adding `Incumbent Equiv.` and INCUMBENT TOTAL
rows to its per-field compliance mapping. For tabular roles (Finance, Operations), C-34
compliance is verified by column existence (`Incumbent Equiv.` column header). For the
conversational role (Commerce), it is verified by the required bold marker
`**Incumbent equivalent:**` followed by the cell form `[A-02]: [step + duration]`. The
C-33 invariant section names how C-34/C-35 requirements survive the register switch.
The inertia framing axis: Finance opens with INCUMBENT BASELINE before DOMAIN CONTEXT,
establishing baseline tokens before any pipeline stages are traced, maximizing token
availability for Commerce's conversational `Incumbent Equiv.` markers. Role sequence
Finance → Commerce → Operations places the domain-vocabulary owner first, the
customer-facing conversational middle, and the warehouse tabular last.

---

You are tracing data through a retail purchase-order-to-inventory pipeline. Three expert
roles run in the sequence **Finance → Commerce → Operations**. Finance opens with the
incumbent manual-process baseline — establishing the competitive frame before any pipeline
stage is traced. Commerce runs in conversational register. Operations runs in tabular
register.

The incumbent manual process is the primary competitive frame. Every pipeline stage and
boundary is evaluated against what the manual process would cost at the same point.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Register | Description |
|-------|----------|-------|----------|-------------|
| [A-01] | INCUMBENT BASELINE | Finance | Tabular | Manual PO and AP process; ≥3 named steps with durations; produced FIRST before [A-02] |
| [A-02] | DOMAIN CONTEXT | Finance | Tabular | Entity vocabulary, staleness SLA (immutable, anchored to [A-01] total), downstream consumer, cadence |
| [A-03] | STAGE TRACE — Finance | Finance | Tabular | PO creation → AP accrual → GL posting; stage tables |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | Tabular | 7-column tables; Incumbent Equiv. cites [A-01] |
| [A-05] | PHASE GATE 1 | Finance | Tabular | Checklist; all ✓ before Commerce begins |
| [A-06] | STAGE TRACE — Commerce | Commerce | Conversational | WMS snapshot → platform cache → availability flag; paragraph-per-stage with required openers |
| [A-07] | BOUNDARY CHECKS — Commerce | Commerce | Conversational | Inline boundary paragraphs with required bold markers; Incumbent Equiv. bold marker present |
| [A-08] | PHASE GATE 2 | Commerce | Conversational | Prose checklist with required sentence openers; all items stated as compliant before Operations |
| [A-09] | STAGE TRACE — Operations | Operations | Tabular | Dock scan → WMS update; stage tables |
| [A-10] | BOUNDARY CHECKS — Operations | Operations | Tabular | 7-column tables; extends elapsed from [A-07]; Incumbent Equiv. cites [A-01] |
| [A-11] | STALE ANALYSIS | Operations | Tabular | Normal and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Operations | Tabular | Named recovery; formula `Fall back to [A-01] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Operations | Tabular | Aggregates Incumbent Equiv. values from [A-04], [A-07], [A-10]; breakdown by role; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Operations | Tabular | Required section; cites [A-01], [A-02], [A-13] by token; ≥1 alternative; ≥2 dimensions |

---

### REGISTER TRANSLATION TABLE

This section is the sole authoritative compliance reference for all output registers. It
simultaneously declares the boundary block schema (per C-31), maps per-field compliance
markers for all registers (per C-32), and identifies surviving invariants for non-tabular
registers (per C-33). An evaluator consults this table to verify any output, in any
register, without reading role instructions.

**Tabular register (Finance, Operations):**

| Required Field | Column Header | Required Cell Content | Disqualifying Form |
|----------------|--------------|----------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum of all prior latencies, in minutes | Deferred; partial |
| Freshness verdict | `Verdict` | `FRESH` or `STALE` vs [A-02] threshold; cite [A-02] by token | Other values |
| Error handling | `Error Handling` | Named mechanism or `no handling — see [A-12]` | Silence; omitted |
| Schema change | `Schema Delta` | Named field changes or `NONE` | Omitted |
| Data loss | `Data Loss Flag` | `YES — [loss point]` or `NO` | Generic language |
| Stage latency | `Stage Latency` (stage tables) | Explicit value, range, or characterization | Inferred from boundary |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]`; token required | Bare duration; token omitted; column absent |

**Conversational register (Commerce):**

| Required Field | Bold Marker / Sentence Opener | Required Form | Disqualifying Form |
|----------------|-------------------------------|---------------|--------------------|
| Domain entity at boundary | `**Entity:**` | Named entity from [A-02] following the marker | Generic label; marker absent |
| Elapsed (cumulative) | `**Elapsed:**` | Numeric cumulative total in minutes; sentence must open with this marker | Deferred to stale analysis |
| Freshness verdict | `**Verdict:**` | `FRESH` or `STALE` following the marker; cite [A-02] by token | Other values; marker absent |
| Error handling | `**Error handling:**` | Named mechanism or "no handling — see [A-12]" | Silence; marker absent |
| Schema change | `**Schema delta:**` | Named changes or "NONE" | Marker absent |
| Data loss | `**Data loss:**` | `YES — [loss point]` or `NO` | Generic; marker absent |
| Stage latency | `**Stage latency:**` (stage paragraphs) | Explicit annotation before other stage content | Inferred only |
| Incumbent equivalent | `**Incumbent equivalent:**` | `[A-01]: [named manual step + duration]` following the marker; `[A-01]` token required | Bare duration; token omitted; marker absent |

**INCUMBENT TOTAL section format by register:**

| Register | Section Form | Required Content |
|----------|-------------|-----------------|
| Tabular (Operations produces [A-13]) | Markdown table with columns: Role \| Incumbent Equiv. subtotal \| Steps cited | Rows for Finance, Commerce, Operations, Grand Total; all values numeric |
| Conversational (not applicable — [A-13] is produced by Operations in tabular register) | N/A | N/A |

---

### REGISTER INVARIANTS (non-tabular Commerce boundaries)

The following structural requirements survive the switch to conversational register for
Commerce. An evaluator verifies each requirement using the conversational check method,
not the tabular column-existence check.

| Criterion | Tabular check | Conversational equivalent check |
|-----------|--------------|--------------------------------|
| C-12 (domain entity per boundary) | `Entity` column present; named entity | `**Entity:**` marker present; named entity from [A-02] follows |
| C-18 (incremental elapsed) | `Elapsed (cumul.)` column; numeric sum inside block | `**Elapsed:**` marker present; numeric cumulative value follows; not deferred |
| C-21 (binary freshness verdict) | `Verdict` column; FRESH or STALE | `**Verdict:**` marker present; FRESH or STALE follows; [A-02] cited |
| C-34 (incumbent equivalent) | `Incumbent Equiv.` column; form `[A-01]: [step + dur]` | `**Incumbent equivalent:**` marker present; `[A-01]: [step + dur]` follows; token required |
| C-02 (error handling) | `Error Handling` column; named mechanism | `**Error handling:**` marker; named mechanism or no-handling follows |

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Finance opens with
`Citing: [A-xx], [A-yy], ...`. All prior-role artifact tokens required. Prose back-references
do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding
boundary block is fully populated per the REGISTER TRANSLATION TABLE compliance markers for
the active register. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: Elapsed (cumul.) is computed in each boundary block
(tabular: column; conversational: `**Elapsed:**` marker). Not deferred.
[Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: FRESH or STALE from [A-02] threshold. In conversational register:
`**Verdict:**` marker with `FRESH` or `STALE`; cite [A-02] by token.
[Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Finance appends to [A-02] verbatim: "This threshold is fixed. No
subsequent role may revise it after Stage 1 is written." The SLA must be derived from [A-01]
total duration; state "SLA = [A-01] total + [headroom]" to anchor the threshold to the
incumbent baseline.

**SC-6 — Phase gate**: [A-05] and [A-08] are required outputs at role transitions.
Next role may not begin until all items are stated as compliant.

**SC-7 — Stage format**: Tabular stages: table with `Stage Latency | Schema In | Schema Out |
Data Loss Flag` columns. Conversational stages: paragraph opening with
`**Stage latency:** [value]`. [Apply SC-7 at every stage block in active register.]

**SC-8 — Trade-off as required section**: [A-14] is required. Cite [A-01], [A-02], [A-13]
by token. ≥1 alternative. ≥2 dimensions. [Apply SC-8 when producing [A-14].]

**SC-9 — Per-boundary incumbent equivalent**: Tabular: `Incumbent Equiv.` column, form
`[A-01]: [step + duration]`. Conversational: `**Incumbent equivalent:**` marker followed by
`[A-01]: [step + duration]`. Token required in both registers; bare durations are protocol
violations. [Apply SC-9 at every boundary block in active register.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Operations produces [A-13] immediately before
[A-14] in tabular register (table with role breakdown). Sum Incumbent Equiv. values from
[A-04] (Finance tabular), [A-07] (Commerce conversational — extract numeric values from
`**Elapsed:**` entries), [A-10] (Operations tabular). [A-14] cites [A-13] by token.
[Apply SC-10 before writing [A-14].]

---

### ROLE 1 — Finance

[Finance runs first. No Citing line required. The incumbent baseline leads.]

**[A-01] INCUMBENT BASELINE** (tabular) — Write this FIRST, before domain context or
stage traces. Describe the manual PO-to-inventory process this pipeline replaces. Table
format:

| Step | Description | Duration |
|------|-------------|----------|
| [step name] | [what is done manually] | [time] |

Include ≥3 named steps with durations. Use entity names that will reappear in [A-02].
This artifact is the source for all `Incumbent Equiv.` cells across all three roles.

**[A-02] DOMAIN CONTEXT** (tabular) — Write after [A-01] and before Stage 1. Include
entity vocabulary (reuse ≥2 entity names from [A-01]), downstream consumer, business
cadence, and staleness SLA. State "SLA = [A-01] total + [headroom]" per SC-5. Append
SC-5 verbatim immutability statement.

**[A-03] STAGE TRACE — Finance** (tabular) — Per SC-7 (stage tables). Per SC-2.

- Stage 1: Supplier EDI confirmation → PO entry in ERP
- Stage 2: PO entry → AP accrual line creation
- Stage 3: AP accrual line → GL posting

**[A-04] BOUNDARY CHECKS — Finance** (tabular) — Per REGISTER TRANSLATION TABLE tabular
columns (7 columns). [SC-3.] [SC-4.] [SC-9: `Incumbent Equiv.` form `[A-01]: [step + dur]`.]

**[A-05] PHASE GATE 1** (tabular) — Tick ✓ or ✗ before Commerce begins:
- [ ] [A-01] includes ≥3 named steps with durations
- [ ] [A-02] SLA anchored to [A-01] total; SC-5 verbatim statement present
- [ ] Every [A-03] stage table has four required columns per SC-7
- [ ] Every [A-04] boundary table has all seven columns per REGISTER TRANSLATION TABLE
      tabular compliance markers
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)

Commerce may not begin until all items ✓. [SC-6.]

---

### ROLE 2 — Commerce (conversational register)

Citing: [A-01], [A-02], [A-04]

Commerce runs in conversational register. All structural requirements apply; compliance
is verified using the REGISTER TRANSLATION TABLE conversational markers, not column headers.
Consult the REGISTER INVARIANTS section for per-criterion conversational equivalents.

**[A-06] STAGE TRACE — Commerce** (conversational) — For each stage, write a paragraph
opening with `**Stage latency:** [value]`, followed by schema description and data loss
observation. Use entity names from [A-02]. Per SC-2: write each [A-07] BOUNDARY CHECK
paragraph before advancing to the next stage.

- Stage 4: WMS stock-on-hand quantity → Commerce platform inventory cache
- Stage 5: Platform cache → Storefront catalog availability flag

**[A-07] BOUNDARY CHECKS — Commerce** (conversational) — One boundary paragraph between
Stage 4 and Stage 5 and one after Stage 5. Each paragraph must include, in any order, all
of the following bold-marker lines per the REGISTER TRANSLATION TABLE conversational column:
`**Entity:**`, `**Elapsed:**`, `**Verdict:**`, `**Error handling:**`, `**Schema delta:**`,
`**Data loss:**`, `**Incumbent equivalent:**`.

For `**Incumbent equivalent:**`: write `[A-01]: [named manual step + duration]`.
The `[A-01]` token is required; a paragraph that states a duration without citing `[A-01]`
is a protocol violation per SC-9. [SC-3: **Elapsed:** extends from [A-04] final value.]
[SC-4: **Verdict:** = FRESH or STALE; cite [A-02] by token.]

**[A-08] PHASE GATE 2** (conversational) — State each compliance item as a sentence.
Each item must include the criterion marker and the compliance status. Required items:
- "Citing line includes [A-01], [A-02], [A-04]." [SC-1]
- "Each [A-06] stage paragraph opens with **Stage latency:** annotation." [SC-7]
- "Each [A-07] boundary paragraph contains all eight required bold markers." [REGISTER
  TRANSLATION TABLE conversational column]
- "Each **Elapsed:** value extends [A-04] final elapsed; not reset." [SC-3]
- "Each **Incumbent equivalent:** entry cites [A-01] by token with named step and
  duration." [SC-9]

Operations may not begin until all items are stated as compliant. [SC-6.]

---

### ROLE 3 — Operations (tabular register)

Citing: [A-01], [A-02], [A-04], [A-07]
([A-04] is Finance boundaries, two roles prior. [A-07] is Commerce conversational
boundaries. Cite both; citing only [A-07] without [A-04] fails SC-1.)

**[A-09] STAGE TRACE — Operations** (tabular) — Per SC-7 (stage tables). Per SC-2.

- Stage 6: AP accrual confirmation → Receiving dock scan
- Stage 7: Dock scan → WMS stock-on-hand quantity update

**[A-10] BOUNDARY CHECKS — Operations** (tabular) — Per REGISTER TRANSLATION TABLE tabular
columns (7 columns). [SC-3: extend Elapsed (cumul.) from the numeric value extracted from
[A-07]'s final `**Elapsed:**` marker.] [SC-4.] [SC-9: `Incumbent Equiv.` form
`[A-01]: [named step + duration]`.]

**[A-11] STALE ANALYSIS** (tabular) — Table: Entity | Normal elapsed | Failure-mode elapsed
| [A-02] threshold | Verdict. Note that [A-02] SLA was derived from [A-01] total; cite both.

**[A-12] RECOVERY PRESCRIPTIONS** (tabular) — Named recovery per loss point and
no-handling flag. Required formula: `Fall back to [A-01] if [specific condition]`.

**[A-13] INCUMBENT TOTAL** (tabular) — Per SC-10. Produce immediately before [A-14].

| Role | Register | Incumbent Equiv. subtotal | Steps cited from [A-01] |
|------|----------|--------------------------|------------------------|
| Finance | Tabular | [sum of [A-04] Incumbent Equiv. values] | |
| Commerce | Conversational | [sum of [A-07] **Incumbent equivalent:** values] | |
| Operations | Tabular | [sum of [A-10] Incumbent Equiv. values] | |
| **Grand Total** | | | |

Note: extract Commerce's incumbent values by scanning [A-07] for `**Incumbent equivalent:**`
markers. The REGISTER INVARIANTS section confirms C-34 is satisfied in conversational
register by marker presence rather than column existence.

**[A-14] TRADE-OFF ANALYSIS** (tabular) — Per SC-8. Required. Cite [A-01] (incumbent
baseline origin), [A-02] (SLA threshold, itself derived from [A-01]), and [A-13] (numeric
total) — all three tokens required. Name ≥1 alternative data propagation pattern. ≥2
trade-off dimensions using [A-13] Grand Total as the pipeline-vs-manual comparison endpoint.
