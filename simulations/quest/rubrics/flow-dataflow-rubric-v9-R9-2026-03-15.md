# flow-dataflow — Round 9 Variations

Reading the R8 scorecard before writing.

## Key gaps from R8

**C-28 FAIL (V-01/V-03)** — labeled-line boundary blocks satisfy content requirements but
not column-existence verification. Field requirements are buried in role instructions;
no pre-declared schema section exists independently.

**C-28 PARTIAL (V-02)** — table boundary blocks are column-verifiable per role but the
schema is discovered by reading role instructions, not a standalone declared section.

**C-28 PARTIAL (V-05)** — Finance/Operations tables satisfy C-28; Commerce conversational
role structurally cannot have named table columns; C-28 fails for that role.

**C-29 FAIL (V-01/V-02/V-03)** — trade-off analysis is never structurally mandated as a
named required output; C-09 PARTIAL in all three confirms this.

**C-30 FAIL/PARTIAL** — register assumed or inferred; no explicit REGISTER DECLARATION
section with per-field compliance marker mapping.

**C-05 regression (V-04/V-05)** — R8 innovations placed structural requirements in
boundary block columns but removed explicit per-stage latency annotation; C-05 scores
PARTIAL because stage bodies have no required `Stage Latency` field.

## New criteria targeting these gaps (C-31, C-32, C-33)

**C-31** — pre-declared boundary block schema section (standalone section before any role
output; field requirements discoverable without reading role instructions).

**C-32** — register-specific compliance marker mapping per field (explicit enumeration of
the verification method for each required field in the declared register: column name for
tabular, sentence-opener or bold keyword for conversational).

**C-33** — register-invariant declaration when output register deviates from tabular default
(names which criteria still apply, how each is verified in the non-tabular register).

## Variation axes

- **V-01**: Output format — pre-declared BOUNDARY BLOCK SCHEMA section (C-31 fix) with
  per-field tabular compliance markers (C-32 fix) + explicit Stage Latency column (C-05 fix)
- **V-02**: Role sequence — Operations → Commerce → Finance (non-natural Finance-last) with
  same C-31/C-32/C-05 fixes as V-01
- **V-03**: Phrasing register — conversational throughout, with C-33 register-invariant
  declaration and C-32 per-field sentence-opener mapping
- **V-04**: Combined — role sequence (Commerce → Operations → Finance, maximally non-natural)
  + lifecycle emphasis (7-column boundary schema + INCUMBENT TOTAL closing artifact)
- **V-05**: Combined — output format (dual-register: Finance/Operations tabular, Commerce
  conversational) + inertia framing with REGISTER TRANSLATION TABLE

---

## V-01

**Axis**: Output format — pre-declared BOUNDARY BLOCK SCHEMA section + per-field compliance
marker mapping + explicit Stage Latency field in stage tables

**Hypothesis**: Adding a named BOUNDARY BLOCK SCHEMA section before any role begins —
separate from role instructions — satisfies C-31 by making field requirements discoverable
by section title alone. Pairing this with a REGISTER DECLARATION that enumerates each
required field and its column-name compliance marker satisfies C-32. Adding `Stage Latency`
as a required column in stage tables closes the C-05 regression introduced by R8's
boundary-column innovations. Role sequence (Finance → Operations → Commerce) is unchanged
from the proven R7 V-01 baseline, isolating the output-format axis.

---

You are tracing data through a retail purchase-order-to-inventory pipeline. Three expert
roles run in the sequence **Finance → Operations → Commerce**. Finance establishes the PO
staleness SLA and manual-process baseline before Operations or Commerce begin. Operations
and Commerce must cite Finance's pre-declared threshold — they may not redeclare or
re-derive it.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. Every citation anywhere in this output must use
the `[A-xx]` token exactly as spelled in this table. A citation to a target not listed here
is a protocol violation.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Finance | Entity vocabulary, staleness SLA (immutable after Stage 1), downstream consumer, business cadence |
| [A-02] | INCUMBENT BASELINE | Finance | Manual PO and AP process this pipeline replaces; uses ≥1 entity from [A-01] |
| [A-03] | STAGE TRACE — Finance | Finance | PO creation → AP accrual → GL posting; stage tables with Stage Latency column |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | Boundary tables conforming to BOUNDARY BLOCK SCHEMA; interleaved between Finance stages |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all items ✓ before Operations begins |
| [A-06] | STAGE TRACE — Operations | Operations | Receiving dock scan → WMS stock-on-hand update; stage tables |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | Boundary tables extending elapsed running total from [A-04] |
| [A-08] | PHASE GATE 2 | Operations | Self-verification checklist; all items ✓ before Commerce begins |
| [A-09] | STAGE TRACE — Commerce | Commerce | WMS snapshot → Commerce platform cache → catalog availability flag; stage tables |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | Boundary tables extending elapsed from [A-07] |
| [A-11] | STALE ANALYSIS | Commerce | Elapsed-vs-threshold rows: normal-operation and failure-mode; cites [A-01] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point and "no handling" flag; required formula: `Fall back to [A-02] if [condition]` |
| [A-13] | TRADE-OFF ANALYSIS | Commerce | Required named section: ≥1 alternative pattern, ≥2 trade-off dimensions, cites [A-01] and [A-02] by token |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout. All stage blocks and boundary blocks
are rendered as markdown tables. An evaluator may verify any required field by scanning
for the named column in the table; no prose reading is required.

**Per-field compliance markers (tabular register):**

| Required Field | Compliance Marker | Disqualifying form |
|----------------|-------------------|--------------------|
| Domain entity at boundary | `Entity` column — named entity from [A-01] | "data" or "records" alone |
| Error handling | `Error Handling` column — named mechanism or `no handling — see [A-12]` | Silence / omitted column |
| Elapsed (cumulative) | `Elapsed (cumul.)` column — numeric sum of all prior stage and boundary latencies | Partial sum or deferred |
| Freshness verdict | `Verdict` column — `FRESH` or `STALE` derived from [A-01] | Any value other than FRESH/STALE |
| Schema state | `Schema Delta` column — named field additions, removals, type changes, or `NONE` | Omitted column |
| Data loss flag | `Data Loss Flag` column — `YES — [named loss point]` or `NO` | Generic "errors may occur" |
| Stage latency | `Stage Latency` column (stage table) — value, range, or characterization (real-time / near-real / batch / daily) | Inferred from boundary elapsed only |

---

### BOUNDARY BLOCK SCHEMA

This section is declared before any role begins. It is the sole authoritative definition of
required boundary block fields. Role instructions reference this section by name; they do
not restate field requirements. An evaluator may verify boundary block completeness by
column existence alone, without consulting role instructions.

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

A boundary block that omits any column, or that is rendered as a labeled field list,
does not conform to this schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role opens with `Citing: [A-xx], [A-yy], ...` listing
every token from prior roles this role builds on. Finance is first and has no prior tokens.
Prose back-references ("as established above") do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the BOUNDARY
CHECK table between Stage N and Stage N+1 is fully populated per the BOUNDARY BLOCK SCHEMA
above. Write the table. Confirm all six columns are populated. Then write Stage N+1.
[Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed computation**: The `Elapsed (cumul.)` column in each BOUNDARY
CHECK must be the sum of all prior stage latencies and all prior boundary latencies up to
and including this boundary. Compute it inside the boundary block; it may not be deferred
to [A-11]. [Apply SC-3 at every boundary block.]

**SC-4 — Binary freshness verdict**: Each boundary block `Verdict` column must read `FRESH`
or `STALE`, derived by comparing the cumulative elapsed against the [A-01] threshold. Cite
[A-01] by token; do not restate its value. A block without a Verdict fails SC-4.
[Apply SC-4 at every boundary block.]

**SC-5 — Immutability of staleness threshold**: Finance must append to [A-01] verbatim:
"This threshold is fixed. No subsequent role may revise it after Stage 1 is written."
Operations and Commerce may not redeclare or adjust the threshold.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required outputs produced at the
end of Finance and Operations respectively. Each is a checklist with named criterion
identifiers. The next role may not begin until all items are ✓. [Apply SC-6 before role
transitions.]

**SC-7 — Stage table format with Stage Latency**: Every stage block is a markdown table
with required columns: `Stage Latency | Schema In | Schema Out | Data Loss Flag`. Stage
Latency must be a value, range, or characterization (real-time / near-real / batch /
daily); it may not be omitted or left to be inferred from boundary elapsed totals alone.
[Apply SC-7 at every stage block.]

**SC-8 — Trade-off analysis as required section**: [A-13] TRADE-OFF ANALYSIS is a
structurally required named section — not optional. It must cite [A-02] by token for the
comparison baseline, cite [A-01] by token for the threshold dimension, name ≥1 alternative
data propagation pattern, and supply ≥2 qualified or quantified trade-off dimensions. A
section that is present but does not cite both tokens fails SC-8. [Apply SC-8 when
producing [A-13].]

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

**[A-02] INCUMBENT BASELINE** — Describe the manual PO and AP process this pipeline
replaces. Use ≥1 entity name from [A-01]. This artifact will be cited by [A-12] (recovery
formula) and [A-13] (trade-off baseline) per SC-8.

**[A-03] STAGE TRACE — Finance** — Per SC-7: each stage is a table with columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. Per SC-2: write one [A-04]
BOUNDARY CHECK (conforming to BOUNDARY BLOCK SCHEMA) before advancing to each next stage.

- Stage 1: Supplier EDI confirmation → PO entry in ERP
- Stage 2: PO entry → AP accrual line creation
- Stage 3: AP accrual line → GL posting

**[A-04] BOUNDARY CHECKS — Finance** — Per SC-2: one block between Stage 1 and Stage 2,
one between Stage 2 and Stage 3, one after Stage 3. Each block conforms to the BOUNDARY
BLOCK SCHEMA (six required columns). [SC-3 applies — Elapsed (cumul.) is the sum of all
prior Stage Latency values and prior boundary latencies.] [SC-4 applies — Verdict = FRESH
or STALE, derived from [A-01] threshold.]

**[A-05] PHASE GATE 1** — Produce and tick this checklist before Operations begins.
Mark each ✓ or ✗:
- [ ] [A-01] contains staleness SLA with SC-5 verbatim immutability statement
- [ ] [A-02] uses ≥1 entity from [A-01]
- [ ] Every stage in [A-03] is a table with all four required columns per SC-7, including
      Stage Latency as an explicit annotation
- [ ] Every block in [A-04] has all six columns per BOUNDARY BLOCK SCHEMA (SC-2)
- [ ] Every `Elapsed (cumul.)` is a computed numeric sum inside the block (SC-3)
- [ ] Every `Verdict` is FRESH or STALE derived from [A-01] (SC-4)

Operations may not begin until all items are ✓.

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]
([A-04] is non-adjacent in natural domain order — extend Finance's elapsed running total;
do not recompute. Do not redeclare entity vocabulary from [A-01] or the staleness threshold.)

**[A-06] STAGE TRACE — Operations** — Per SC-7 (stage tables). Per SC-2, write one [A-07]
BOUNDARY CHECK (BOUNDARY BLOCK SCHEMA) before advancing.

- Stage 4: AP accrual confirmation → Warehouse receiving dock scan
- Stage 5: Dock scan → WMS stock-on-hand update

Each stage: table with columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`.
Use entity names from [A-01].

**[A-07] BOUNDARY CHECKS — Operations** — Per SC-2: one block between Stage 4 and Stage 5,
one after Stage 5. Each block conforms to the BOUNDARY BLOCK SCHEMA.
[SC-3: Elapsed (cumul.) extends the running total from the last entry in [A-04] — not a
fresh computation.]
[SC-4: Verdict = FRESH or STALE vs [A-01] threshold; do not redeclare threshold value.]

**[A-08] PHASE GATE 2** — Produce and tick before Commerce begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] is a table with all four required columns per SC-7, including
      Stage Latency as an explicit annotation
- [ ] Every block in [A-07] has all six columns per BOUNDARY BLOCK SCHEMA (SC-2)
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] running total, not a fresh computation
      (SC-3)
- [ ] Every Verdict derives from [A-01] threshold without redeclaring its value (SC-4,
      SC-5)
- [ ] All entity names in [A-06] and [A-07] are from [A-01] vocabulary

Commerce may not begin until all items are ✓.

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]
([A-04] is two roles prior — Finance boundary checks. Cite it explicitly to confirm the
elapsed chain is unbroken across all three roles. Citing only [A-07] without [A-04] fails
SC-1.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7 (stage tables). Per SC-2, write one [A-10]
BOUNDARY CHECK before advancing.

- Stage 6: WMS stock-on-hand quantity → Commerce platform inventory cache
- Stage 7: Commerce platform cache → Storefront catalog availability flag

Each stage: table with columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`.
Use entity names from [A-01].

**[A-10] BOUNDARY CHECKS — Commerce** — Per SC-2: one block between Stage 6 and Stage 7,
one after Stage 7. Each block conforms to the BOUNDARY BLOCK SCHEMA.
[SC-3: extend from the last entry in [A-07].]
[SC-4: Verdict vs [A-01] threshold.]

**[A-11] STALE ANALYSIS** — Using Elapsed (cumul.) values from [A-04], [A-07], [A-10]:

| Entity ([A-01]) | Normal elapsed | Failure-mode elapsed | [A-01] threshold | Verdict |
|-----------------|---------------|---------------------|-----------------|---------|

Produce separate rows for normal-operation and failure-mode staleness.

**[A-12] RECOVERY PRESCRIPTIONS** — For every `no handling — see [A-12]` annotation in
[A-04], [A-07], [A-10] and every `Data Loss Flag: YES` in [A-03], [A-06], [A-09], provide
a specific named recovery action. Required formula structure for manual-process fallbacks:

`Fall back to [A-02] if [specific named failure condition]`

Cite [A-02] using this exact formula at least once. A loose prose mention of [A-02] without
this formula does not satisfy this requirement.

**[A-13] TRADE-OFF ANALYSIS** — [SC-8 applies] Name one alternative data propagation
pattern (e.g., event-driven CDC, real-time dual-write). Provide ≥2 trade-off dimensions,
≥1 quantified. Cite [A-02] as the comparison baseline and [A-01] as the threshold reference
per SC-8. Both tokens are required; a section that omits either fails SC-8.

---

---

## V-02

**Axis**: Role sequence — Operations → Commerce → Finance (non-natural Finance-last)

**Hypothesis**: Reversing role sequence so Finance runs last forces Finance to cite
Operations and Commerce artifacts as non-adjacent predecessors — the longest possible
citation distance in a three-role sequence. C-31/C-32/C-05 fixes (BOUNDARY BLOCK SCHEMA
section, REGISTER DECLARATION, Stage Latency column) are applied identically to V-01 so
any score difference isolates the role-sequence effect on cross-role citation compliance
and non-adjacent token citation.

---

You are tracing data through a B2B procurement sync pipeline: purchase request approval
(Operations), supplier catalog price sync (Commerce), and invoice matching with GL accrual
(Finance). Roles run in the sequence **Operations → Commerce → Finance**. Natural domain
order would be Finance → Operations → Commerce; running Finance last forces it to cite
both prior roles as non-adjacent predecessors.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Operations | Entity vocabulary, procurement SLA (immutable), downstream consumer, business cadence |
| [A-02] | INCUMBENT BASELINE | Operations | Manual purchase-request and email-approval process this pipeline replaces; uses ≥1 entity from [A-01] |
| [A-03] | STAGE TRACE — Operations | Operations | Purchase request → approval → PO dispatch; stage tables |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | Boundary tables per BOUNDARY BLOCK SCHEMA; establishes elapsed baseline |
| [A-05] | PHASE GATE 1 | Operations | Self-verification checklist; all items ✓ before Commerce begins |
| [A-06] | STAGE TRACE — Commerce | Commerce | Supplier catalog pull → price reconciliation → line-item commit; stage tables |
| [A-07] | BOUNDARY CHECKS — Commerce | Commerce | Boundary tables extending elapsed from [A-04] |
| [A-08] | PHASE GATE 2 | Commerce | Self-verification checklist; all items ✓ before Finance begins |
| [A-09] | STAGE TRACE — Finance | Finance | Invoice receipt → PO matching → GL accrual posting; stage tables |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | Boundary tables extending elapsed from [A-07] |
| [A-11] | STALE ANALYSIS | Finance | Normal + failure-mode elapsed vs [A-01] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery per loss point and no-handling flag; formula `Fall back to [A-02] if [condition]` required |
| [A-13] | TRADE-OFF ANALYSIS | Finance | Required named section: ≥1 alternative, ≥2 dimensions, cites [A-01] and [A-02] by token |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout. Per-field compliance markers:

| Required Field | Compliance Marker | Disqualifying form |
|----------------|-------------------|--------------------|
| Domain entity at boundary | `Entity` column — named entity from [A-01] | "data" or "records" alone |
| Error handling | `Error Handling` column — named mechanism or `no handling — see [A-12]` | Omitted |
| Elapsed (cumulative) | `Elapsed (cumul.)` column — numeric sum of all prior stage and boundary latencies | Deferred or partial |
| Freshness verdict | `Verdict` column — `FRESH` or `STALE` | Any other value |
| Schema state | `Schema Delta` column — named changes or `NONE` | Omitted |
| Data loss flag | `Data Loss Flag` column — `YES — [named loss point]` or `NO` | Generic language |
| Stage latency | `Stage Latency` column (stage table) — value, range, or characterization | Inferred from elapsed only |

---

### BOUNDARY BLOCK SCHEMA

Declared here, before any role begins, as the authoritative definition of boundary block
field requirements. Role instructions reference this section by name only. An evaluator
verifies boundary block completeness by column existence; no role instruction reading
required.

**Every boundary block must be a markdown table with the following columns, in order:**

| Column | Required Content |
|--------|-----------------|
| Entity | Named entity from [A-01]. "data" or "records" alone fails. |
| Elapsed (cumul.) | Sum of all prior stage and boundary latencies, in minutes. Computed inside this block. |
| Verdict | `FRESH` or `STALE` — compared against [A-01] threshold by token citation. |
| Error Handling | Named mechanism, or `no handling — see [A-12]`. Silence fails. |
| Schema Delta | Named field-level changes at this boundary, or `NONE`. |
| Data Loss Flag | `YES — [loss point name]` or `NO`. Generic language fails. |

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Operations (first) opens with
`Citing: [A-xx], [A-yy], ...`. Finance must cite [A-01] (Operations, two roles prior) and
[A-07] (Commerce, immediate predecessor) — both are required. Citing only [A-07] fails
SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the BOUNDARY
CHECK table between Stage N and Stage N+1 is fully populated per BOUNDARY BLOCK SCHEMA.
[Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed computation**: `Elapsed (cumul.)` is the sum of all prior
stage and boundary latencies. Computed inside the block; not deferred. [Apply SC-3 at
every boundary block.]

**SC-4 — Binary freshness verdict**: `Verdict` = `FRESH` or `STALE` derived from [A-01]
threshold. Cite [A-01] by token; do not restate its value. [Apply SC-4 at every boundary
block.]

**SC-5 — Immutability**: Operations must append to [A-01] verbatim: "This threshold is
fixed. No subsequent role may revise it after Stage 1 is written."

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required checklist outputs at
phase transitions. The next role may not begin until all items are ✓.

**SC-7 — Stage table with Stage Latency**: Every stage block is a table with required
columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`. Stage Latency must be
an explicit annotation; it may not be omitted or inferred from boundary totals.

**SC-8 — Trade-off analysis as required section**: [A-13] is structurally required. It
must cite [A-02] by token (comparison baseline) and [A-01] by token (threshold dimension),
name ≥1 alternative pattern, supply ≥2 trade-off dimensions. Both tokens required; a
section omitting either fails SC-8. [Apply SC-8 when producing [A-13].]

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required.]

**[A-01] DOMAIN CONTEXT** — Write before Stage 1. Include:
- Entity vocabulary: purchase request (PR), approval workflow record, PO line item,
  supplier price list version, invoice receipt, GL accrual entry
- Downstream consumer and business cadence (e.g., weekly invoice batch at Friday 17:00)
- Procurement SLA: maximum elapsed time from purchase request submission to GL accrual
  posting. Declare as an integer with unit.
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-02] INCUMBENT BASELINE** — Describe the manual email-and-spreadsheet approval process
this pipeline replaces. Use ≥1 entity from [A-01]. Will be cited by [A-12] and [A-13].

**[A-03] STAGE TRACE — Operations** — Per SC-7 (stage tables). Per SC-2, write one [A-04]
BOUNDARY CHECK (BOUNDARY BLOCK SCHEMA) before advancing.

- Stage 1: Purchase request submission → Approval workflow routing
- Stage 2: Approval record → PO line item creation and dispatch to supplier

**[A-04] BOUNDARY CHECKS — Operations** — Per SC-2: one block between Stage 1 and Stage 2,
one after Stage 2. Each block conforms to BOUNDARY BLOCK SCHEMA.
[SC-3: Elapsed (cumul.) = sum of all Stage Latency values and prior boundary latencies.]
[SC-4: Verdict = FRESH or STALE vs [A-01] threshold.]

**[A-05] PHASE GATE 1** — Tick ✓ or ✗ before Commerce begins:
- [ ] [A-01] contains SLA with SC-5 verbatim immutability statement
- [ ] [A-02] uses ≥1 entity from [A-01]
- [ ] Every stage in [A-03] is a table with all four required columns per SC-7
- [ ] Every block in [A-04] has all six columns per BOUNDARY BLOCK SCHEMA (SC-2)
- [ ] Every `Elapsed (cumul.)` is a computed numeric sum inside the block (SC-3)
- [ ] Every `Verdict` is FRESH or STALE from [A-01] (SC-4)

Commerce may not begin until all items are ✓.

---

### ROLE 2 — Commerce

Citing: [A-01], [A-02], [A-04]
([A-04] is Operations' boundary checks — extend its elapsed running total. [A-01] is
non-adjacent in natural domain order; cite it explicitly to confirm vocabulary and SLA
lock.)

**[A-06] STAGE TRACE — Commerce** — Per SC-7 (stage tables). Per SC-2, write one [A-07]
BOUNDARY CHECK before advancing.

- Stage 3: PO dispatch → Supplier catalog price list pull
- Stage 4: Price list → Line-item price reconciliation
- Stage 5: Reconciled prices → Committed PO line item confirmation

Each stage: table with columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`.
Use entity names from [A-01].

**[A-07] BOUNDARY CHECKS — Commerce** — Per SC-2: one block between each consecutive stage
pair and one after Stage 5. Each block conforms to BOUNDARY BLOCK SCHEMA.
[SC-3: extend Elapsed (cumul.) from the last entry in [A-04].]
[SC-4: Verdict vs [A-01] threshold; do not redeclare threshold value.]

**[A-08] PHASE GATE 2** — Tick ✓ or ✗ before Finance begins:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] has all four required columns per SC-7
- [ ] Every block in [A-07] has all six columns per BOUNDARY BLOCK SCHEMA (SC-2)
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] totals, not a fresh computation (SC-3)
- [ ] Every Verdict derives from [A-01] without restating its value (SC-4, SC-5)

Finance may not begin until all items are ✓.

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]
([A-04] is two roles prior — Operations' boundary elapsed totals. Citing only [A-07] is
insufficient; SC-1 requires explicit citation of non-adjacent tokens. Finance does not
redeclare the entity vocabulary or procurement SLA from [A-01].)

**[A-09] STAGE TRACE — Finance** — Per SC-7 (stage tables). Per SC-2, write one [A-10]
BOUNDARY CHECK before advancing.

- Stage 6: Committed PO line item → Invoice receipt matching
- Stage 7: Invoice match → GL accrual entry posting

Each stage: table with columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`.
Use entity names from [A-01].

**[A-10] BOUNDARY CHECKS — Finance** — Per SC-2: one block between Stage 6 and Stage 7,
one after Stage 7. Each block conforms to BOUNDARY BLOCK SCHEMA.
[SC-3: extend Elapsed (cumul.) from the last entry in [A-07].]
[SC-4: Verdict vs [A-01] threshold.]

**[A-11] STALE ANALYSIS** — Using Elapsed (cumul.) values from [A-04], [A-07], [A-10]:

| Entity ([A-01]) | Normal elapsed | Failure-mode elapsed | [A-01] threshold | Verdict |
|-----------------|---------------|---------------------|-----------------|---------|

Produce separate rows for normal-operation and failure-mode staleness.

**[A-12] RECOVERY PRESCRIPTIONS** — For every `no handling — see [A-12]` annotation and
every `Data Loss Flag: YES` across all stage traces, provide a specific named recovery
action. Required formula for manual-process fallbacks:

`Fall back to [A-02] if [specific named failure condition]`

Cite [A-02] using this exact formula at least once.

**[A-13] TRADE-OFF ANALYSIS** — [SC-8 applies] Name one alternative procurement data
pattern (e.g., event-driven ERP webhook, API-first supplier portal). Provide ≥2 trade-off
dimensions, ≥1 quantified. Cite [A-02] as the comparison baseline and [A-01] as the
threshold reference per SC-8.

---

---

## V-03

**Axis**: Phrasing register — conversational throughout, with C-33 register-invariant
declaration and C-32 per-field sentence-opener / bold-keyword mapping

**Hypothesis**: A conversational register can satisfy C-33 (register-invariant declaration)
if a named REGISTER INVARIANT DECLARATION section explicitly maps every required boundary
field to a sentence-opener or bold-keyword compliance marker, and explicitly declares which
structural criteria still apply in conversational form. The evaluator can verify any field
by scanning for the declared marker rather than reading prose holistically. Role sequence
Commerce → Finance → Operations is unchanged from R7 V-03 baseline, isolating the
register-axis improvements.

---

Here is what you will do: trace data through a vendor marketplace payment clearing pipeline
from the perspective of three domain experts, working in the sequence **Commerce → Finance
→ Operations**. Commerce sets up the vocabulary and the incumbent-process baseline first —
then Finance extends the trace, then Operations closes it out.

The output is in **conversational register** throughout. Every structural requirement is
still enforced — but in prose form, not tables. The REGISTER INVARIANT DECLARATION section
below tells you exactly how to satisfy each requirement in this register. Read it before
writing anything.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Commerce | Vendor marketplace entity vocabulary; payment SLA (immutable); downstream consumers; cadence |
| [A-02] | INCUMBENT BASELINE | Commerce | Manual vendor payment process (email remittance + bank wire) this pipeline replaces |
| [A-03] | STAGE TRACE — Commerce | Commerce | Vendor invoice submission → payment authorization stages; conversational prose |
| [A-04] | BOUNDARY CHECKS — Commerce | Commerce | Interleaved boundary narrations; establishes elapsed baseline |
| [A-05] | PHASE GATE 1 | Commerce | Commerce self-check; all items ✓ before Finance begins |
| [A-06] | STAGE TRACE — Finance | Finance | Payment authorization → AP ledger → bank settlement stages; prose |
| [A-07] | BOUNDARY CHECKS — Finance | Finance | Interleaved boundary narrations; extends elapsed from [A-04] |
| [A-08] | PHASE GATE 2 | Finance | Finance self-check; all items ✓ before Operations begins |
| [A-09] | STAGE TRACE — Operations | Operations | Settlement confirmation → vendor portal update → fulfillment release stages; prose |
| [A-10] | BOUNDARY CHECKS — Operations | Operations | Interleaved boundary narrations; extends elapsed from [A-07] |
| [A-11] | STALE ANALYSIS | Operations | Elapsed-vs-threshold table; normal + failure-mode |
| [A-12] | RECOVERY PRESCRIPTIONS | Operations | Named recovery per loss point; formula `Fall back to [A-02] if [condition]` required |
| [A-13] | TRADE-OFF ANALYSIS | Operations | Required named section: ≥1 alternative, ≥2 dimensions, cites [A-01] and [A-02] by token |

---

### REGISTER DECLARATION

This output uses the **conversational register** throughout. Output is produced as prose
narration, not markdown tables. The criteria listed below still apply in this register.

This is a non-tabular register. The REGISTER INVARIANT DECLARATION section that follows
is mandatory per C-33: it names which criteria apply in this register and specifies the
exact verification method for each required field.

---

### REGISTER INVARIANT DECLARATION

The following table declares, for each required boundary field, the compliance marker
that takes the place of a table column in conversational output. An evaluator may verify
any field by scanning for the declared marker — no holistic prose reading required.

| Required Field | Applies in conversational register? | Compliance Marker |
|----------------|-------------------------------------|-------------------|
| Domain entity at boundary | YES | **Bold entity name** as the grammatical subject of the first sentence of the boundary narration paragraph. Must be a named entity from [A-01]. |
| Error handling | YES | Sentence explicitly opening with or containing **`Error handling:`** followed by named mechanism. `no handling — see [A-12]` is the permitted no-handling form. |
| Elapsed (cumulative) | YES | Sentence opening exactly with **`Running total: X min`** where X is a computed numeric sum of all prior stage and boundary latencies. |
| Freshness verdict | YES | Sentence opening exactly with **`Verdict: FRESH`** or **`Verdict: STALE`**, derived by comparing the running total against the [A-01] threshold. |
| Schema state | YES | Sentence explicitly containing **`Schema delta:`** followed by named field-level changes, or `Schema delta: NONE`. |
| Data loss flag | YES | Sentence explicitly containing **`Loss flag: YES — [loss point name]`** or **`Loss flag: NO`**. Generic language fails. |
| Stage latency | YES | Sentence explicitly containing **`Stage latency: [value or characterization]`** within the stage body narration — not deferred to the boundary block. |
| Named-column table schema (C-28) | DOES NOT APPLY — conversational register. | Compliance markers declared in this table are the register-equivalent substitutes. Evaluators verify by marker presence, not column existence. |

A boundary narration paragraph that omits any of the declared markers is incomplete
regardless of whether the corresponding information is inferrable from surrounding prose.

---

### PROTOCOL RULES

Keep these rules in mind throughout. I will reference them by name in each role's
instructions.

**PR-1 — Open with citations**: When Finance or Operations begins, the very first line is
`Citing: [A-xx], [A-yy], ...` listing every prior token this role builds on. Commerce
opens first and has no prior tokens. Any role that opens content without a Citing line has
skipped PR-1.

**PR-2 — Boundary-before-stage**: Stage N+1 may not be written until the BOUNDARY CHECK
narration for the boundary between Stage N and Stage N+1 contains all seven required
markers from the REGISTER INVARIANT DECLARATION. The boundary narration is a gate;
confirm all markers are present before advancing.

**PR-3 — Running elapsed total**: Each boundary narration must contain `Running total: X min`
where X is the cumulative sum of all prior stage and boundary latencies. Compute it in
the boundary narration; do not defer.

**PR-4 — Freshness verdict**: Each boundary narration must contain `Verdict: FRESH` or
`Verdict: STALE`, derived by comparing the running total against [A-01]. Do not restate
the threshold value; cite [A-01] by token.

**PR-5 — SLA is locked**: Once Commerce declares the payment SLA in [A-01] and writes
Stage 1, the value is frozen. Finance and Operations may not change it. Commerce appends
this sentence to [A-01] before Stage 1: "This threshold is fixed. No subsequent role may
revise it after Stage 1 is written."

**PR-6 — Phase gate output**: At the end of each of the first two roles, produce and tick
a self-check checklist. The next role does not begin until every item is ✓.

**PR-7 — Trade-off as required section**: [A-13] TRADE-OFF ANALYSIS is a structurally
required named section. It must cite [A-02] (comparison baseline) and [A-01] (threshold)
by token, name ≥1 alternative pattern, supply ≥2 dimensions. Both tokens required. A
section omitting either fails PR-7.

---

### ROLE 1 — Commerce

Commerce goes first. No Citing line needed.

**[A-01] DOMAIN CONTEXT** — Lock the vocabulary before writing Stage 1. In prose, describe:
entity names (vendor invoice, payment authorization record, AP ledger debit entry, bank
settlement confirmation, vendor portal release flag), downstream consumer, and business
cadence (e.g., daily payment run at 14:00). Then declare the payment SLA: how long from
vendor invoice submission to vendor portal release flag update is acceptable before data
goes stale? Give a specific number with units. Append before Stage 1: "This threshold is
fixed. No subsequent role may revise it after Stage 1 is written." (PR-5)

**[A-02] INCUMBENT BASELINE** — Describe the manual email-remittance and bank-wire process
this pipeline replaces. Name ≥1 entity from [A-01]. Finance and Operations will cite this.

**[A-03] STAGE TRACE — Commerce** — Narrate the following stages in prose. Per PR-2, write
a BOUNDARY CHECK narration (all seven markers from REGISTER INVARIANT DECLARATION) before
moving to the next stage. Include `Stage latency: [value]` within each stage narration.

- Stage 1: Vendor invoice submission → Payment gateway authorization request
- Stage 2: Payment gateway response → Payment authorization record creation

**[A-04] BOUNDARY CHECKS — Commerce** — Per PR-2: one narration between Stage 1 and Stage
2, one after Stage 2. Each narration paragraph must contain all seven compliance markers
from the REGISTER INVARIANT DECLARATION in the declared form.
[PR-3: `Running total: X min` — sum of Stage 1 and Stage 2 latencies + prior boundaries]
[PR-4: `Verdict: FRESH` or `Verdict: STALE` — vs [A-01] threshold, cited by token]

**[A-05] PHASE GATE 1** — Before Finance begins, tick ✓ or ✗:
- [ ] [A-01] has a specific SLA value and the PR-5 immutability sentence
- [ ] [A-02] names ≥1 entity from [A-01]
- [ ] Every stage narration in [A-03] contains `Stage latency: [value]` explicitly
- [ ] Every narration in [A-04] contains all seven markers from REGISTER INVARIANT DECLARATION
- [ ] Every narration contains `Running total: X min` as a numeric cumulative sum (PR-3)
- [ ] Every narration contains `Verdict: FRESH` or `Verdict: STALE` (PR-4)

Finance does not begin until all items are ✓.

---

### ROLE 2 — Finance

Citing: [A-01], [A-02], [A-04]
(PR-1 applies. [A-04] is Commerce's boundary narrations — extend the Running total from
the last entry in [A-04], not starting fresh.)

**[A-06] STAGE TRACE — Finance** — Narrate stages in prose. Per PR-2, write one BOUNDARY
CHECK narration before advancing. Include `Stage latency: [value]` within each stage.

- Stage 3: Payment authorization record → AP ledger debit entry
- Stage 4: AP ledger entry → Bank settlement instruction
- Stage 5: Bank settlement instruction → Settlement confirmation receipt

Use entity names from [A-01].

**[A-07] BOUNDARY CHECKS — Finance** — Per PR-2: one narration between each consecutive
stage pair (Stage 3–4, Stage 4–5) and one after Stage 5. Each narration contains all
seven compliance markers per REGISTER INVARIANT DECLARATION.
[PR-3: `Running total: X min` — extend from the last entry in [A-04]]
[PR-4: `Verdict: FRESH` or `Verdict: STALE` — vs [A-01]; do not restate threshold]

**[A-08] PHASE GATE 2** — Tick ✓ or ✗ before Operations begins:
- [ ] Citing line opens with [A-01], [A-02], [A-04] (PR-1)
- [ ] Every stage narration in [A-06] contains `Stage latency: [value]` explicitly
- [ ] Every narration in [A-07] has all seven markers from REGISTER INVARIANT DECLARATION
- [ ] `Running total` in [A-07] is an extension of [A-04] totals, not a restart (PR-3)
- [ ] All Freshness verdicts cite [A-01] by token without restating its value (PR-4, PR-5)

Operations does not begin until all items are ✓.

---

### ROLE 3 — Operations

Citing: [A-01], [A-02], [A-04], [A-07]
(PR-1 applies. [A-04] is two roles back — Commerce's boundary running totals. Cite it
explicitly; citing only [A-07] is insufficient under PR-1.)

**[A-09] STAGE TRACE — Operations** — Narrate stages in prose. Per PR-2, write one BOUNDARY
CHECK narration before advancing. Include `Stage latency: [value]` within each stage.

- Stage 6: Settlement confirmation receipt → Vendor portal payment status update
- Stage 7: Vendor portal update → Fulfillment release flag set

Use entity names from [A-01].

**[A-10] BOUNDARY CHECKS — Operations** — Per PR-2: one narration between Stage 6 and
Stage 7, one after Stage 7. Each narration contains all seven compliance markers per
REGISTER INVARIANT DECLARATION.
[PR-3: `Running total: X min` — extend from the last entry in [A-07]]
[PR-4: `Verdict: FRESH` or `Verdict: STALE` — vs [A-01] threshold]

**[A-11] STALE ANALYSIS** — Using Running total values from [A-04], [A-07], [A-10]:

| Entity | Normal elapsed | Failure-mode elapsed | [A-01] threshold | Verdict |
|--------|---------------|---------------------|-----------------|---------|

Two rows minimum: normal operation and failure mode.

**[A-12] RECOVERY PRESCRIPTIONS** — For every `no handling — see [A-12]` and every
`Loss flag: YES` across all stage traces, give a specific named recovery action. Required
formula for manual-process fallbacks:

`Fall back to [A-02] if [specific named failure condition]`

Use this formula at least once.

**[A-13] TRADE-OFF ANALYSIS** — [PR-7 applies] Name one alternative pattern, ≥2 trade-off
dimensions (≥1 quantified), [A-02] as baseline, [A-01] as threshold reference. Both tokens
required per PR-7.

---

---

## V-04

**Axes**: Role sequence (Commerce → Operations → Finance, maximally non-natural) + lifecycle
emphasis (7-column boundary schema with Incumbent Equiv. column + INCUMBENT TOTAL closing
artifact before TRADE-OFF ANALYSIS)

**Hypothesis**: Reversing the natural domain order fully (natural = Finance → Operations
→ Commerce; this sequence = Commerce → Operations → Finance) places the longest non-adjacent
citation burden on Finance, which must cite both Commerce [A-04] and Operations [A-07] as
predecessors. Adding an `Incumbent Equiv.` column to every boundary block, and requiring
a named INCUMBENT TOTAL artifact that sums those cells before the TRADE-OFF ANALYSIS,
closes the R8 V-04 gap: the manual-process comparison becomes a numeric, per-boundary
audit trail with a quantitative closing endpoint — not a narrative assertion at [A-15]
only. Per-stage latency as an explicit stage table column (SC-7) closes the C-05 regression.

---

You are tracing data through a store replenishment sync pipeline: storefront demand signal
to in-store inventory update (Commerce), distribution center pick and dispatch (Operations),
and finance cost-of-goods posting and GL inventory reconciliation (Finance). Roles run in
the sequence **Commerce → Operations → Finance**.

**INCUMBENT CONTEXT**: The process this pipeline replaces is a manually maintained
spreadsheet called REPLEN_TRACKER.xlsx, updated by the store operations team twice daily
at 06:00 and 18:00 to reflect DC shipments. Every role must place the comparable
REPLEN_TRACKER step beside each pipeline boundary in the `Incumbent Equiv.` column of the
BOUNDARY BLOCK SCHEMA. This column makes the pipeline-vs-manual comparison auditable at
every gate, not only at the closing trade-off analysis.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Commerce | Entity vocabulary; replenishment SLA (immutable after Stage 1); downstream consumer; cadence |
| [A-02] | STALE SLA CONTRACT | Commerce | Single-row immutable threshold declaration; appended verbatim lock phrase; cited by token at every Verdict cell |
| [A-03] | INCUMBENT BASELINE | Commerce | REPLEN_TRACKER.xlsx manual process: steps, cadence, known failure modes; ≥1 entity from [A-01]; required source for all Incumbent Equiv. cells |
| [A-04] | STAGE TRACE — Commerce | Commerce | Storefront demand signal → replenishment request stages; stage tables |
| [A-05] | BOUNDARY CHECKS — Commerce | Commerce | Boundary tables per 7-column BOUNDARY BLOCK SCHEMA; establishes elapsed baseline |
| [A-06] | PHASE GATE 1 | Commerce | Self-verification checklist; all ✓ before Operations begins |
| [A-07] | STAGE TRACE — Operations | Operations | DC pick list → carton dispatch stages; stage tables |
| [A-08] | BOUNDARY CHECKS — Operations | Operations | Boundary tables extending elapsed from [A-05]; Incumbent Equiv. derived from [A-03] |
| [A-09] | PHASE GATE 2 | Operations | Self-verification checklist; all ✓ before Finance begins |
| [A-10] | STAGE TRACE — Finance | Finance | Carton receipt confirmation → COGS posting → GL reconciliation stages; stage tables |
| [A-11] | BOUNDARY CHECKS — Finance | Finance | Boundary tables extending elapsed from [A-08]; Incumbent Equiv. derived from [A-03] |
| [A-12] | INCUMBENT TOTAL | Finance | Sum of all Incumbent Equiv. cells across [A-05], [A-08], [A-11]; required before [A-14] |
| [A-13] | STALE ANALYSIS | Finance | Normal + failure-mode elapsed vs [A-02] threshold |
| [A-14] | RECOVERY PRESCRIPTIONS | Finance | Named recovery per loss point; formula `Fall back to [A-03] if [condition]` required |
| [A-15] | TRADE-OFF ANALYSIS | Finance | Required named section: cites [A-02] and [A-12] as numeric comparison endpoints; ≥1 alternative, ≥2 dimensions |
| [A-16] | PHASE GATE 3 | Finance | Final self-verification checklist |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout. Per-field compliance markers:

| Required Field | Compliance Marker | Disqualifying form |
|----------------|-------------------|--------------------|
| Domain entity at boundary | `Entity` column — named entity from [A-01] | "data" or "records" alone |
| Error handling | `Error Handling` column — named mechanism or `no handling — see [A-14]` | Omitted |
| Elapsed (cumulative) | `Elapsed (cumul.)` column — numeric sum of all prior stage and boundary latencies | Partial or deferred |
| Freshness verdict | `Verdict` column — `FRESH` or `STALE` derived from [A-02] | Any other value |
| Schema state | `Schema Delta` column — named changes or `NONE` | Omitted |
| Data loss flag | `Data Loss Flag` column — `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent step | `Incumbent Equiv.` column — `[A-03]: [named manual step and duration]` | Cell that does not cite [A-03] by token |
| Stage latency | `Stage Latency` column (stage table) — value, range, or characterization | Inferred from elapsed only |

---

### BOUNDARY BLOCK SCHEMA

Declared here, before any role begins. Every boundary block is a markdown table with
the following seven columns, in order:

| Column | Required Content |
|--------|-----------------|
| Entity | Named entity from [A-01]. "data" or "records" alone fails. |
| Elapsed (cumul.) | Sum of all prior stage and boundary latencies, in minutes. Computed inside this block. |
| Verdict | `FRESH` or `STALE` — compared against [A-02] by token citation. |
| Error Handling | Named mechanism, or `no handling — see [A-14]`. Silence fails. |
| Schema Delta | Named field-level changes at this boundary, or `NONE`. |
| Data Loss Flag | `YES — [loss point name]` or `NO`. Generic language fails. |
| Incumbent Equiv. | `[A-03]: [named manual step and its duration from REPLEN_TRACKER]`. Cell that does not cite [A-03] by token is a protocol violation (SC-9). |

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Commerce (first) opens with
`Citing: [A-xx], [A-yy], ...`. Finance must cite [A-02] and [A-03] (Commerce artifacts,
two roles prior) and [A-08] (Operations, immediate predecessor) — all three required.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the BOUNDARY
CHECK table between Stage N and Stage N+1 is fully populated per the 7-column BOUNDARY
BLOCK SCHEMA. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed computation**: `Elapsed (cumul.)` = sum of all prior stage
and boundary latencies. Computed inside this block; not deferred to [A-13].
[Apply SC-3 at every boundary block.]

**SC-4 — Binary freshness verdict**: `Verdict` = `FRESH` or `STALE` derived from [A-02]
threshold. Cite [A-02] by token; do not restate its value. [Apply SC-4 at every boundary
block.]

**SC-5 — Immutability**: Commerce must append to [A-02] verbatim: "This threshold is
fixed. No subsequent role may revise it after Stage 1 is written."

**SC-6 — Phase gate obligation**: [A-06], [A-09], and [A-16] are required checklist outputs
at phase transitions. The next role may not begin until all items are ✓.

**SC-7 — Stage table with Stage Latency**: Every stage block is a table with required
columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`. Stage Latency must be
an explicit annotation in the stage table; it may not be omitted or inferred from
boundary totals.

**SC-8 — Trade-off analysis as required section**: [A-15] TRADE-OFF ANALYSIS is structurally
required. It must cite [A-02] (staleness threshold) and [A-12] (INCUMBENT TOTAL) by token,
name ≥1 alternative pattern, supply ≥2 dimensions. Finance must produce [A-12] before [A-15].
[Apply SC-8 when producing [A-15].]

**SC-9 — Incumbent Equiv. column derivation**: Every `Incumbent Equiv.` cell must derive
its value from [A-03] by explicit token citation: `[A-03]: [named manual step duration]`.
A cell that states a manual-process duration without citing [A-03] is a protocol violation.
[Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL artifact**: Finance must produce [A-12] INCUMBENT TOTAL
immediately before [A-15]. [A-12] states: "Incumbent Total: [sum of all Incumbent Equiv.
durations across all roles] min" — derived by summing every `Incumbent Equiv.` cell from
[A-05], [A-08], and [A-11]. This total is the numeric comparison endpoint for [A-15].
[Apply SC-10 before writing [A-15].]

---

### ROLE 1 — Commerce

[Commerce runs first. No Citing line required.]

**[A-01] DOMAIN CONTEXT** — Write before Stage 1. Include:
- Entity vocabulary: storefront out-of-stock signal, replenishment request record, DC pick
  list, carton manifest, store inventory count, COGS line item, GL inventory balance
- Downstream consumer and business cadence (e.g., nightly shelf restock at 21:00)

**[A-02] STALE SLA CONTRACT** — Declare the replenishment SLA as a single statement:
"Replenishment SLA: maximum elapsed time from storefront out-of-stock signal to store
inventory count update = [integer with units]." Per SC-5, append verbatim: "This threshold
is fixed. No subsequent role may revise it after Stage 1 is written."

**[A-03] INCUMBENT BASELINE** — Describe REPLEN_TRACKER.xlsx: update cadence (twice daily),
which entities it tracks, and ≥2 named failure modes (e.g., update lag, formula errors,
version conflicts). Use entity names from [A-01]. Every `Incumbent Equiv.` cell across all
three roles must derive from this artifact by token citation per SC-9.

**[A-04] STAGE TRACE — Commerce** — Per SC-7 (stage tables). Per SC-2, write one [A-05]
BOUNDARY CHECK (7-column BOUNDARY BLOCK SCHEMA) before advancing.

- Stage 1: Storefront out-of-stock signal → Replenishment request creation in OMS
- Stage 2: Replenishment request → DC pick list generation

**[A-05] BOUNDARY CHECKS — Commerce** — Per SC-2: one block between Stage 1 and Stage 2,
one after Stage 2. Each block conforms to the 7-column BOUNDARY BLOCK SCHEMA.
[SC-3: Elapsed (cumul.) = sum of Stage 1 and Stage 2 latencies + prior boundary latencies]
[SC-4: Verdict = FRESH or STALE vs [A-02] threshold]
[SC-9: Incumbent Equiv. = `[A-03]: [named REPLEN_TRACKER step and duration]`]

**[A-06] PHASE GATE 1** — Tick ✓ or ✗ before Operations begins:
- [ ] [A-02] contains SLA with SC-5 verbatim immutability statement
- [ ] [A-03] describes REPLEN_TRACKER with ≥2 failure modes and ≥1 entity from [A-01]
- [ ] Every stage in [A-04] is a table with all four required columns per SC-7
- [ ] Every block in [A-05] has all seven columns per BOUNDARY BLOCK SCHEMA (SC-2)
- [ ] Every `Elapsed (cumul.)` is a computed numeric sum inside the block (SC-3)
- [ ] Every `Verdict` is FRESH or STALE from [A-02] (SC-4)
- [ ] Every `Incumbent Equiv.` cell cites [A-03] by token (SC-9)

Operations may not begin until all items are ✓.

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-03], [A-05]
([A-02] and [A-03] are Commerce artifacts — cite them explicitly. Do not redeclare the SLA
or the REPLEN_TRACKER baseline. Extend the Elapsed (cumul.) running total from [A-05].)

**[A-07] STAGE TRACE — Operations** — Per SC-7 (stage tables). Per SC-2, write one [A-08]
BOUNDARY CHECK (7-column BOUNDARY BLOCK SCHEMA) before advancing.

- Stage 3: DC pick list → Carton manifest generation
- Stage 4: Carton manifest → Carrier handoff scan at DC dock

Each stage: table with columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`.
Use entity names from [A-01].

**[A-08] BOUNDARY CHECKS — Operations** — Per SC-2: one block between Stage 3 and Stage 4,
one after Stage 4. Each block conforms to the 7-column BOUNDARY BLOCK SCHEMA.
[SC-3: extend Elapsed (cumul.) from the last entry in [A-05]]
[SC-4: Verdict vs [A-02] threshold; do not redeclare its value]
[SC-9: Incumbent Equiv. = `[A-03]: [named REPLEN_TRACKER step and duration]`]

**[A-09] PHASE GATE 2** — Tick ✓ or ✗ before Finance begins:
- [ ] Citing line names [A-01], [A-02], [A-03], [A-05] (SC-1)
- [ ] Every stage in [A-07] has all four required columns per SC-7
- [ ] Every block in [A-08] has all seven columns per BOUNDARY BLOCK SCHEMA (SC-2)
- [ ] `Elapsed (cumul.)` in [A-08] extends [A-05] running total (SC-3)
- [ ] Every `Verdict` derives from [A-02] without restating its value (SC-4, SC-5)
- [ ] Every `Incumbent Equiv.` cell cites [A-03] by token (SC-9)

Finance may not begin until all items are ✓.

---

### ROLE 3 — Finance

Citing: [A-02], [A-03], [A-05], [A-08]
([A-02] and [A-03] are two roles prior — Commerce's SLA contract and REPLEN_TRACKER
baseline. Cite both explicitly; citing only [A-08] fails SC-1.)

**[A-10] STAGE TRACE — Finance** — Per SC-7 (stage tables). Per SC-2, write one [A-11]
BOUNDARY CHECK (7-column BOUNDARY BLOCK SCHEMA) before advancing.

- Stage 5: Carrier delivery confirmation → Store inventory count update
- Stage 6: Inventory count → COGS line item creation
- Stage 7: COGS line item → GL inventory balance reconciliation

Each stage: table with columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`.
Use entity names from [A-01].

**[A-11] BOUNDARY CHECKS — Finance** — Per SC-2: one block between each consecutive stage
pair and one after Stage 7. Each block conforms to the 7-column BOUNDARY BLOCK SCHEMA.
[SC-3: extend from the last entry in [A-08]]
[SC-4: Verdict vs [A-02] threshold]
[SC-9: Incumbent Equiv. = `[A-03]: [named REPLEN_TRACKER step and duration]`]

**[A-12] INCUMBENT TOTAL** — [SC-10 applies] Produce this artifact before [A-15]:
"Incumbent Total: [sum of all Incumbent Equiv. durations from [A-05], [A-08], and [A-11]
combined] min"
Show the additive breakdown by role. This total is the numeric pipeline-vs-manual
comparison endpoint for [A-15].

**[A-13] STALE ANALYSIS** — Using Elapsed (cumul.) values from [A-05], [A-08], [A-11]:

| Entity ([A-01]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|---------------|---------------------|-----------------|---------|

**[A-14] RECOVERY PRESCRIPTIONS** — For every `no handling — see [A-14]` and every
`Data Loss Flag: YES` across all stage traces, provide a specific named recovery action.
Required formula structure:

`Fall back to [A-03] if [specific named failure condition]`

Cite [A-03] using this exact formula at least once.

**[A-15] TRADE-OFF ANALYSIS** — [SC-8 applies] Name one alternative pattern (e.g.,
event-driven CDC, IoT shelf sensor direct-to-GL). Provide ≥2 trade-off dimensions, ≥1
quantified, using [A-12] INCUMBENT TOTAL as the numeric pipeline-vs-manual comparison
endpoint and [A-02] as the staleness threshold reference. Both [A-02] and [A-12] citations
required per SC-8.

**[A-16] PHASE GATE 3** — Tick ✓ or ✗:
- [ ] Citing line names [A-02], [A-03], [A-05], [A-08] (SC-1)
- [ ] Every stage in [A-10] has all four required columns per SC-7
- [ ] Every block in [A-11] has all seven columns per BOUNDARY BLOCK SCHEMA (SC-2)
- [ ] `Elapsed (cumul.)` in [A-11] extends [A-08] running total (SC-3)
- [ ] Every `Verdict` derives from [A-02] without restating it (SC-4, SC-5)
- [ ] Every `Incumbent Equiv.` cell cites [A-03] by token (SC-9)
- [ ] [A-12] INCUMBENT TOTAL produced before [A-15] with additive breakdown (SC-10)
- [ ] [A-15] cites both [A-02] and [A-12] by token (SC-8)

---

---

## V-05

**Axes**: Output format (dual-register: Finance/Operations tabular, Commerce conversational)
+ inertia framing (REGISTER TRANSLATION TABLE as the single structural section satisfying
C-31 + C-32 + C-33 simultaneously)

**Hypothesis**: A named REGISTER TRANSLATION TABLE section — mapping every required boundary
field to its compliance marker in each declared register (tabular and conversational) —
simultaneously satisfies C-31 (pre-declared schema), C-32 (per-field markers for both
registers), and C-33 (register-invariant declaration: enumerates criteria and their
verification form in the non-tabular register) via a single lookup structure. Role sequence
Finance → Commerce → Operations (maximally non-natural Finance-first) maximizes
non-adjacent citation distance from Operations to Finance, while the format shift at
Commerce stress-tests whether the REGISTER TRANSLATION TABLE survives a register transition
mid-sequence.

---

You are tracing data through a subscription billing-to-fulfillment pipeline: recurring
invoice generation (Finance), subscription entitlement activation and catalog access
(Commerce), and physical fulfillment dispatch and delivery confirmation (Operations). Roles
run in the sequence **Finance → Commerce → Operations**.

**Output registers by role:**
- Finance: tabular register (stage tables, boundary tables per BOUNDARY BLOCK SCHEMA)
- Commerce: conversational register (prose narrations with compliance markers per REGISTER
  TRANSLATION TABLE)
- Operations: tabular register (stage tables, boundary tables per BOUNDARY BLOCK SCHEMA)

The REGISTER TRANSLATION TABLE below governs compliance verification in both registers.
Read it before writing any role output.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Finance | Entity vocabulary; billing SLA (immutable after Stage 1); downstream consumer; cadence |
| [A-02] | STALE SLA CONTRACT | Finance | Single-row immutable threshold declaration; lock phrase appended; cited by token at every Verdict field |
| [A-03] | INCUMBENT BASELINE | Finance | Manual invoice-and-fulfillment process (PDF invoices + spreadsheet dispatch log) this pipeline replaces |
| [A-04] | STAGE TRACE — Finance | Finance | Invoice generation → payment capture stages; tabular register |
| [A-05] | BOUNDARY CHECKS — Finance | Finance | Boundary tables per BOUNDARY BLOCK SCHEMA; establishes elapsed baseline; tabular register |
| [A-06] | PHASE GATE 1 | Finance | Checklist; all ✓ before Commerce begins |
| [A-07] | STAGE TRACE — Commerce | Commerce | Payment confirmation → entitlement record activation stages; conversational register |
| [A-08] | BOUNDARY CHECKS — Commerce | Commerce | Boundary narrations per REGISTER TRANSLATION TABLE; extends elapsed from [A-05]; conversational register |
| [A-09] | PHASE GATE 2 | Commerce | Checklist; all ✓ before Operations begins |
| [A-10] | STAGE TRACE — Operations | Operations | Entitlement confirmation → fulfillment dispatch → delivery confirmation stages; tabular register |
| [A-11] | BOUNDARY CHECKS — Operations | Operations | Boundary tables per BOUNDARY BLOCK SCHEMA; extends elapsed from [A-08]; tabular register |
| [A-12] | STALE ANALYSIS | Operations | Normal + failure-mode elapsed vs [A-02] threshold |
| [A-13] | RECOVERY PRESCRIPTIONS | Operations | Named recovery per loss point; formula `Fall back to [A-03] if [condition]` required |
| [A-14] | TRADE-OFF ANALYSIS | Operations | Required named section: cites [A-02] and [A-03] by token; ≥1 alternative; ≥2 dimensions |
| [A-15] | PHASE GATE 3 | Operations | Final checklist |

---

### REGISTER TRANSLATION TABLE

This section is declared before any role begins and is the sole authoritative declaration
of boundary block field requirements and compliance markers for both registers. It
simultaneously satisfies the pre-declared schema requirement (C-31), the per-field
compliance marker mapping (C-32), and the register-invariant declaration for the
conversational register (C-33). An evaluator may verify any field in any register using
this table alone.

**Applies to:** Finance (tabular), Operations (tabular), Commerce (conversational)

| Required Field | Tabular Register (Finance, Operations) | Conversational Register (Commerce) | Disqualifying form (either register) |
|----------------|----------------------------------------|------------------------------------|---------------------------------------|
| Domain entity at boundary | `Entity` column — named entity from [A-01] | **Bold entity name** as grammatical subject of first sentence in boundary paragraph | "data" or "records" alone |
| Error handling | `Error Handling` column — named mechanism or `no handling — see [A-13]` | Sentence containing **`Error handling:`** followed by named mechanism | Silence / omission |
| Elapsed (cumulative) | `Elapsed (cumul.)` column — numeric sum of all prior stage and boundary latencies, in minutes | Sentence opening exactly with **`Running total: X min`** | Partial sum; deferred to stale analysis |
| Freshness verdict | `Verdict` column — `FRESH` or `STALE`, derived from [A-02] threshold by token | Sentence opening exactly with **`Verdict: FRESH`** or **`Verdict: STALE`**, derived from [A-02] | Any value other than FRESH/STALE; restating threshold value |
| Schema state | `Schema Delta` column — named field-level changes or `NONE` | Sentence containing **`Schema delta:`** followed by changes or `NONE` | Omission |
| Data loss flag | `Data Loss Flag` column — `YES — [loss point name]` or `NO` | Sentence containing **`Loss flag: YES — [name]`** or **`Loss flag: NO`** | Generic "errors may occur" |
| Stage latency | `Stage Latency` column in stage table — value, range, or characterization | Sentence containing **`Stage latency: [value]`** within stage narration | Inferred from elapsed only |

**Register-invariant note for Commerce (C-33):** Commerce uses conversational register.
The following criteria still apply; verification method is the compliance marker in the
right-hand column above, not column existence:
C-11 (interleaved boundary gates) — a boundary narration paragraph before every stage
advance; C-12 (domain entity at boundary) — bold entity name as first-sentence subject;
C-14 (additive elapsed) — `Running total: X min` marker; C-21 (binary freshness verdict)
— `Verdict: FRESH` or `Verdict: STALE` marker; C-28 (named-column schema) — DOES NOT APPLY
to Commerce; the conversational compliance markers in this table are the register-equivalent
substitute.

---

### BOUNDARY BLOCK SCHEMA (tabular register only)

For Finance and Operations roles, every boundary block is a markdown table with these
six columns, in order. Column requirements are defined in the REGISTER TRANSLATION TABLE
above; this section provides the column ordering for tabular render:

Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag

Commerce boundary blocks use prose narration with compliance markers from the REGISTER
TRANSLATION TABLE; this column schema does not apply to Commerce.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role after Finance opens with `Citing: [A-xx], [A-yy], ...`.
Operations must cite [A-02] (Finance, two roles prior) and [A-08] (Commerce, immediate
predecessor) — both required. Prose back-references fail SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the BOUNDARY
CHECK (table or narration per REGISTER TRANSLATION TABLE) between Stage N and Stage N+1
is fully populated. Confirm all required fields are present in the declared register
before advancing.

**SC-3 — Incremental elapsed computation**: Elapsed (cumul.) in tabular register and
`Running total: X min` in conversational register must be the sum of all prior stage and
boundary latencies. Computed inside each boundary block; not deferred.

**SC-4 — Binary freshness verdict**: Verdict in tabular register and `Verdict: FRESH/STALE`
in conversational must be derived from [A-02] by token citation. Value not restated.

**SC-5 — Immutability**: Finance must append to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written."

**SC-6 — Phase gate obligation**: [A-06], [A-09], and [A-15] are required checklist outputs.
Next role may not begin until all items ✓.

**SC-7 — Stage format per register**: Tabular roles: stage block is a table with columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. Conversational role: each stage
narration contains all seven compliance markers from REGISTER TRANSLATION TABLE, including
`Stage latency: [value]`. Stage Latency may not be omitted or inferred in either register.

**SC-8 — Trade-off analysis as required section**: [A-14] is structurally required. Must
cite [A-02] and [A-03] by token, name ≥1 alternative pattern, supply ≥2 dimensions. Both
tokens required. [Apply SC-8 when producing [A-14].]

---

### ROLE 1 — Finance (tabular register)

[Finance runs first. No Citing line required.]

**[A-01] DOMAIN CONTEXT** — Write before Stage 1. Include:
- Entity vocabulary: subscription invoice, payment capture record, entitlement activation
  event, fulfillment dispatch order, delivery confirmation record
- Downstream consumer and business cadence (e.g., monthly billing cycle close)

**[A-02] STALE SLA CONTRACT** — Declare: "Billing SLA: maximum elapsed time from
subscription invoice generation to delivery confirmation record = [integer with units]."
Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
after Stage 1 is written."

**[A-03] INCUMBENT BASELINE** — Describe the manual PDF-invoice and spreadsheet-dispatch-log
process this pipeline replaces. Use ≥1 entity from [A-01]. Will be cited by [A-13] and
[A-14] per SC-8.

**[A-04] STAGE TRACE — Finance** — Per SC-7 (tabular): stage table with columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. Per SC-2, write one [A-05]
BOUNDARY CHECK before advancing.

- Stage 1: Subscription renewal trigger → Invoice generation in billing system
- Stage 2: Invoice → Payment gateway capture request
- Stage 3: Payment capture confirmation → Payment capture record finalization

**[A-05] BOUNDARY CHECKS — Finance** — Per SC-2: one block between each consecutive stage
pair and one after Stage 3. Each is a tabular boundary block per BOUNDARY BLOCK SCHEMA
(column order: Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data
Loss Flag). Compliance markers per REGISTER TRANSLATION TABLE (tabular column).
[SC-3: Elapsed (cumul.) = sum of all prior Stage Latency values + prior boundary latencies]
[SC-4: Verdict = FRESH or STALE vs [A-02]; cite [A-02] by token]

**[A-06] PHASE GATE 1** — Tick ✓ or ✗ before Commerce begins:
- [ ] [A-02] contains SLA with SC-5 verbatim immutability statement
- [ ] [A-03] uses ≥1 entity from [A-01]
- [ ] Every stage in [A-04] is a table with all four required columns per SC-7
- [ ] Every block in [A-05] has all six columns per BOUNDARY BLOCK SCHEMA
- [ ] Every `Elapsed (cumul.)` is a computed numeric sum (SC-3)
- [ ] Every `Verdict` is FRESH or STALE from [A-02] (SC-4)

Commerce may not begin until all items are ✓.

---

### ROLE 2 — Commerce (conversational register)

Citing: [A-01], [A-02], [A-03], [A-05]
(PR opens this role. [A-05] is Finance's boundary blocks — extend the Running total from
the last entry in [A-05], not starting fresh. Conversational register applies for this
role; verify compliance using the right-hand column of the REGISTER TRANSLATION TABLE.)

**[A-07] STAGE TRACE — Commerce** — Narrate the following stages in prose. Per SC-2,
write a BOUNDARY CHECK narration before advancing to each next stage. Per SC-7
(conversational), include `Stage latency: [value]` within each stage narration and all
other required compliance markers.

- Stage 4: Payment capture record → Entitlement activation event creation
- Stage 5: Entitlement activation → Catalog access rights commit

Use entity names from [A-01].

**[A-08] BOUNDARY CHECKS — Commerce** — Per SC-2: one narration between Stage 4 and
Stage 5, one after Stage 5. Each narration paragraph must contain all seven compliance
markers from the REGISTER TRANSLATION TABLE (conversational column).
[SC-3: `Running total: X min` — extend from the last entry in [A-05]]
[SC-4: `Verdict: FRESH` or `Verdict: STALE` — derived from [A-02] threshold by token]

**[A-09] PHASE GATE 2** — Tick ✓ or ✗ before Operations begins:
- [ ] Citing line names [A-01], [A-02], [A-03], [A-05] (SC-1)
- [ ] Every stage narration in [A-07] contains `Stage latency: [value]` explicitly (SC-7)
- [ ] Every narration in [A-08] contains all seven compliance markers per REGISTER
      TRANSLATION TABLE (conversational column)
- [ ] Every narration contains `Running total: X min` as a cumulative sum extending
      [A-05] totals (SC-3)
- [ ] Every narration contains `Verdict: FRESH` or `Verdict: STALE` citing [A-02] (SC-4)

Operations may not begin until all items are ✓.

---

### ROLE 3 — Operations (tabular register)

Citing: [A-01], [A-02], [A-03], [A-05], [A-08]
([A-02] and [A-05] are Finance artifacts, two roles prior. Cite both explicitly. [A-08]
is Commerce's conversational boundary narrations; the elapsed running total in [A-08]
expressed as `Running total: X min` is the value to extend in this role's tabular
`Elapsed (cumul.)` column — convert from conversational marker to tabular column at the
first boundary block of this role.)

**[A-10] STAGE TRACE — Operations** — Per SC-7 (tabular): stage table with columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. Per SC-2, write one [A-11]
BOUNDARY CHECK before advancing.

- Stage 6: Catalog access rights confirmation → Fulfillment dispatch order creation
- Stage 7: Dispatch order → Carrier pickup and in-transit scan
- Stage 8: In-transit scan → Delivery confirmation record

Use entity names from [A-01].

**[A-11] BOUNDARY CHECKS — Operations** — Per SC-2: one block between each consecutive
stage pair and one after Stage 8. Each is a tabular boundary block per BOUNDARY BLOCK
SCHEMA. Compliance markers per REGISTER TRANSLATION TABLE (tabular column).
[SC-3: Elapsed (cumul.) extends the Running total value from the last entry in [A-08]]
[SC-4: Verdict = FRESH or STALE vs [A-02]; do not redeclare its value]

**[A-12] STALE ANALYSIS** — Using Elapsed (cumul.) from [A-05] (tabular), [A-08]
(`Running total` markers converted to minutes), and [A-11] (tabular):

| Entity ([A-01]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|---------------|---------------------|-----------------|---------|

**[A-13] RECOVERY PRESCRIPTIONS** — For every `no handling — see [A-13]` annotation and
every `Data Loss Flag: YES` or `Loss flag: YES` across all stage traces, provide a specific
named recovery action. Required formula:

`Fall back to [A-03] if [specific named failure condition]`

Cite [A-03] using this exact formula at least once.

**[A-14] TRADE-OFF ANALYSIS** — [SC-8 applies] Name one alternative billing-to-fulfillment
data pattern (e.g., event-sourced entitlement stream, real-time webhook dispatch chain).
Provide ≥2 trade-off dimensions, ≥1 quantified. Cite [A-02] and [A-03] by token per SC-8.
Both tokens required.

**[A-15] PHASE GATE 3** — Tick ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-03], [A-05], [A-08] (SC-1)
- [ ] Every stage in [A-10] is a table with all four required columns per SC-7
- [ ] Every block in [A-11] has all six columns per BOUNDARY BLOCK SCHEMA (SC-2)
- [ ] `Elapsed (cumul.)` in [A-11] extends the [A-08] Running total values (SC-3)
- [ ] Every `Verdict` derives from [A-02] without restating its value (SC-4, SC-5)
- [ ] [A-14] cites both [A-02] and [A-03] by token (SC-8)
- [ ] Register transition from conversational [A-08] to tabular [A-11] is explicitly
      documented at the first [A-11] boundary block (elapsed value carried forward)
