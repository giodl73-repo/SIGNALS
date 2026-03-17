# flow-dataflow — Round 18 Variations

## R17 gap summary before writing

**C-52 target for R18**: R17 required a detectability-location qualifier in every SC entry in
the REGISTER DECLARATION closed-chain paragraph (C-51). C-52 elevates this to a standalone
DETECTABILITY INDEX section — or an equivalent named table within STRUCTURAL CONSTRAINTS —
that lists every SC identifier with its violation-detection location phrase in a single
machine-scannable reference. The index must cover ALL SCs in the prompt, not only the
closed-chain entries. Coverage is verifiable by matching row count to SC count. Detectability
information embedded solely in individual SC prose bodies without a dedicated summary index
does not satisfy C-52.

**C-53 target for R18**: R16 required [A-01] dual-slot anchoring only for the four
[A-01]-load-bearing SCs (SC-8, SC-9, SC-11, SC-13). C-53 extends dual-slot anchoring to
every SC in the prompt that references any `[A-xx]` registry token. An SC that names [A-05],
[A-08], [A-13], or any other registry token in its governed-artifact slot must also name
that same token in its enforcement clause. A prompt where dual-slot is present for
[A-01]-bearing SCs but absent for SCs governing [A-04], [A-06], [A-07], etc. does not pass.

Both C-52 and C-53 apply globally across all output format modes.

## Variation axes

- **V-01**: DETECTABILITY INDEX as standalone named section before STRUCTURAL CONSTRAINTS +
  C-53 full dual-slot — natural Finance → Operations → Commerce, tabular;
  B2B wholesale order-to-cash pipeline.

- **V-02**: Non-natural role sequence (Operations → Finance → Commerce) — skip-level stress
  test; DETECTABILITY INDEX + C-53; food & beverage manufacturing ingredient procurement
  pipeline; [A-01] owned by Operations.

- **V-03**: Prose output format (SC-14 FORMAT MODE DECLARATION); DETECTABILITY INDEX as
  numbered prose enumeration; C-53 adapted to prose format; SaaS metered billing to
  deferred revenue pipeline; natural Finance → Operations → Commerce.

- **V-04**: Combined — maximum incumbent prominence (≥5 manual steps in [A-01]) + non-natural
  role sequence (Commerce → Finance → Operations); DETECTABILITY INDEX with
  incumbent-baseline visibility column; C-53 full dual-slot; retail store cash
  reconciliation pipeline.

- **V-05**: Combined — lifecycle depth (Phase Gate 0 + SC-0; 14 SCs total) + non-natural role
  sequence (Operations → Commerce → Finance); DETECTABILITY INDEX row-count verification as
  Phase Gate 0 checklist item; C-53 full dual-slot; telecom CDR-to-billing-to-GL pipeline.

---

## V-01

**Axis**: DETECTABILITY INDEX as standalone named section + C-53 full dual-slot —
natural role sequence, tabular

**Hypothesis**: Finance → Operations → Commerce; B2B wholesale distributor order-to-cash
pipeline. A standalone DETECTABILITY INDEX section placed before STRUCTURAL CONSTRAINTS
lists all 13 SCs with their violation-detection locations in a single machine-scannable
table — row count verifiable against SC count without reading any SC prose. C-53 extends
dual-slot anchoring from [A-01]-bearing SCs to every SC that references any [A-xx] token:
SC-1 names [A-06]/[A-09] in its enforcement clause; SC-2 names all six governed stage and
boundary tokens; SC-3/SC-4 name [A-04]/[A-07]/[A-10]; SC-6 names [A-05]/[A-08]; SC-7
names [A-03]/[A-06]/[A-09]. Commerce (pos 3) cites Finance [A-04] (pos 1) skip-level.

---

You are tracing data through a B2B wholesale distributor order-to-cash pipeline — customer
purchase order capture through order validation, warehouse fulfillment, and invoice
generation to AR posting and revenue analytics. Three expert roles run in the sequence
**Finance → Operations → Commerce**. Finance establishes the manual PO-processing SLA and
the incumbent order-entry baseline that all subsequent roles must cite. Operations and
Commerce cite Finance's artifacts by token; they may not redeclare or re-derive either.

Commerce runs last and must cite Finance's boundary artifacts directly — two positions prior
in the Finance → Operations → Commerce sequence — as a required skip-level citation. A
Commerce `Citing:` line naming only Operations' artifacts without Finance's boundary checks
fails SC-12. Phase Gate 2 verifies this requirement by citing SC-12 by number.

The physical pipeline flows: customer PO terminal → PO aggregation service → order
validation service → warehouse allocation service → pick/pack service → shipment dispatch →
invoice generation service → AR posting service → revenue analytics dashboard.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first; all subsequent
artifacts follow in token order. Every citation must use the `[A-xx]` token exactly as
spelled here. A citation to a token not listed here is a protocol violation.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Finance | Manual PO-entry and order-processing workflow replaced by this pipeline; ≥3 named steps with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Finance | Entity vocabulary, order-close SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration. |
| [A-03] | STAGE TRACE — Finance | Finance | PO terminal → PO aggregation → order validation → invoice staging; stage tables per SC-7. |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01]; required skip-level target for Commerce (SC-12). |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all items ✓ before Operations begins. |
| [A-06] | STAGE TRACE — Operations | Operations | Warehouse allocation → pick/pack service → shipment dispatch; stage tables per SC-7. |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends Elapsed (cumul.) from [A-04]; Incumbent Equiv. cells cite [A-01]. |
| [A-08] | PHASE GATE 2 | Operations | Self-verification checklist; all items ✓ before Commerce begins; item [SC-12] verifies Commerce skip-level citation. |
| [A-09] | STAGE TRACE — Commerce | Commerce | Invoice generation → AR posting service → revenue analytics dashboard; stage tables per SC-7. |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends Elapsed (cumul.) from [A-07]; Incumbent Equiv. cells cite [A-01]. |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold. |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point and no-handling annotation; formula: `Fall back to [A-01] if [condition]`; SC-13 applies. |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14]. |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions; SC-8 and SC-13 apply. |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout. All stage blocks and boundary blocks
are rendered as markdown tables.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell form)
and C-35 (INCUMBENT TOTAL section format). An evaluator may determine pass/fail for both
criteria by reading this section alone.**

**Exhaustive closed verification chain** — every SC listed with its governed artifact
tokens, enforcement mechanism, and violation detectability location:

**SC-1 CITATION OPENER** governs [A-06], [A-09] (all non-first role outputs); enforced by
token-match at each role's opening `Citing:` line — an [A-06] or [A-09] role block that
omits the `Citing:` line or uses prose-only back-references fails, and the violation is
detectable from the role-opener line without reading the role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] (stage tables) and
[A-04], [A-07], [A-10] (boundary tables); enforced by an inline lock at every stage advance
— [A-03]/[A-06]/[A-09] Stage N+1 may not be written until the preceding
[A-04]/[A-07]/[A-10] boundary table is fully populated per BOUNDARY BLOCK SCHEMA; the gate
fires as a per-transition callback detectable at the stage-boundary position without
inspecting stage content.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (boundary tables, `Elapsed
(cumul.)` column); enforced by Part A column requirement — a [A-04], [A-07], or [A-10]
boundary block with a missing column or a zero-reset value fails, and the violation is
detectable at the column-header and cell-value level without reading row prose.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (boundary tables, `Verdict`
column); enforced by Part A string requirement — any [A-04]/[A-07]/[A-10] cell value other
than exactly `FRESH` or exactly `STALE` fails, and the violation is detectable at the
cell-value level without reading surrounding prose.

**SC-5 STALENESS IMMUTABILITY** governs [A-02] (DOMAIN CONTEXT); enforced by verbatim
phrase requirement — absence of the exact phrase "This threshold is fixed. No subsequent
role may revise it after Stage 1 is written." in [A-02] fails, and the violation is
detectable by phrase-match scan within [A-02]'s body without searching other sections.

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08] (phase gates); enforced by a
gating callback at every role transition — an unchecked [A-05] or [A-08] item blocks the
next role block, and the violation is detectable at the role-boundary line before reading
any role content.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09] (stage tables, `Stage Latency`
column); enforced by Part A column requirement — a [A-03], [A-06], or [A-09] stage table
missing the `Stage Latency` column fails, and the violation is detectable at the
table-header row without reading row contents.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] (TRADE-OFF ANALYSIS) requiring
[A-01], [A-02], and [A-13] as mandatory citation tokens inside [A-14]; enforced by a
three-token check — [A-01], [A-02], and [A-13] must all appear in [A-14]; absence of any
of these tokens in [A-14] is a protocol violation detectable from [A-14]'s citation token
list without prose interpretation.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] (`Incumbent Equiv.`
column) requiring [A-01] as a mandatory token in every cell; enforced by Part A cell-form
requirement — a [A-04]/[A-07]/[A-10] cell lacking the `[A-01]` token is a protocol
violation detectable at the cell level without reading surrounding prose.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] (INCUMBENT TOTAL) in relation to
[A-14] (TRADE-OFF ANALYSIS); enforced by Part B ordering requirement — [A-13] must appear
immediately before [A-14] and carry a Grand Total row; the violation is detectable by
artifact-order check at the [A-14] header position without reading cell values.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] (INCUMBENT BASELINE) as the required
first-produced artifact; enforced by a positional lock — [A-01] must appear before any
stage trace or boundary block; a violation where any output precedes [A-01] is detectable
from the artifact-order check at the output head without reading artifact content.

**SC-12 SKIP-LEVEL CITATION IN COMMERCE** governs [A-04] (Finance's boundary checks) via
Commerce's `Citing:` line; enforced by the Phase Gate 2 checklist item citing [SC-12] by
number — absence of `[A-04]` in Commerce's `Citing:` line is a protocol violation
detectable by token-match at the Commerce role-opener line without reading the role body.
Commerce occupies position 3; Finance occupies position 1; the position distance is two.

**SC-13 BASELINE CLOSURE** governs [A-12] (RECOVERY PRESCRIPTIONS) and [A-14] (TRADE-OFF
ANALYSIS) requiring [A-01] as a citation token in both; enforced by inline callbacks at
both [A-12] and [A-14] section headers that verify the [A-01] token by token match — a
[A-12] or [A-14] section header lacking the [A-01] token is a protocol violation detectable
from the header line alone.

Together, SC-1 through SC-13 form a complete closed verification chain: every structural
failure mode has a named navigation path from this paragraph to its governing SC, its
governed artifact, its enforcement mechanism, and its detectability location.

**Part A — Field compliance markers (boundary block columns):**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum of all prior stage and boundary latencies, in minutes | Partial sum; deferred total; reset to zero |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE`, derived from [A-02] threshold | Any other value |
| Error handling | `Error Handling` | Named retry/dead-letter/rollback, or exactly `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level changes, or exactly `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` — `[A-01]` token required | Bare duration; token omitted; column absent |
| Stage latency (stage table) | `Stage Latency` | Explicit value, range, or characterization | Inferred from boundary elapsed only |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Markdown table: `Role \| Incumbent Equiv. subtotal \| Steps cited`; rows for Finance, Operations, Commerce, Grand Total; all subtotals numeric | Prose-only; missing role row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | All three tokens `[A-01]`, `[A-02]`, `[A-13]` present; ≥1 alternative pattern; ≥2 dimensions | Any token absent; no pattern named |

---

### BOUNDARY BLOCK SCHEMA

Standalone section declared before any role output. Column header strings must match
REGISTER DECLARATION Part A spellings exactly. Role instructions reference this section by
name only; they do not restate field requirements.

**Every boundary block must be a markdown table with these columns, in this order:**

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

A column absent, renamed, or not matching Part A header strings fails the schema.

---

### DETECTABILITY INDEX

Standalone section declared before STRUCTURAL CONSTRAINTS. Every SC in this prompt appears
as exactly one row. Row count = 13 = SC count; a DETECTABILITY INDEX with fewer than 13
rows is incomplete and fails C-52. Evaluators locate violations using this index without
reading SC prose bodies.

| SC | Violation Detectable At |
|----|------------------------|
| SC-1 | Each non-first role's opening `Citing:` line — no role body reading required |
| SC-2 | Each stage-advance transition position — no stage content reading required |
| SC-3 | The `Elapsed (cumul.)` column header and cell-value level — no row prose reading required |
| SC-4 | The `Verdict` cell-value level — no surrounding prose reading required |
| SC-5 | Phrase-match scan within [A-02] body — no other sections required |
| SC-6 | The role-boundary line before each role block — no role content reading required |
| SC-7 | The stage table header row — no row contents reading required |
| SC-8 | The [A-14] citation token list — no prose interpretation required |
| SC-9 | The `Incumbent Equiv.` cell level — no surrounding prose reading required |
| SC-10 | The artifact-order position at the [A-14] header — no cell value reading required |
| SC-11 | The output artifact-order head — no artifact content reading required |
| SC-12 | Commerce role-opener `Citing:` line — no role body reading required |
| SC-13 | The [A-12] and [A-14] section header lines — no section body reading required |

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Finance opens with
`Citing: [A-xx], [A-yy], ...` listing every token from prior roles this role builds on.
Citing [A-01] is required in every non-first role's Citing line. An [A-06] or [A-09] role
block that omits the `Citing:` line is a protocol violation. Prose back-references do not
satisfy SC-1. [Apply SC-1 at every non-first role opener.]

**SC-2 — Stage-write progression gate**: [A-03]/[A-06]/[A-09] Stage N+1 may not be written
until the preceding [A-04]/[A-07]/[A-10] boundary table is fully populated per BOUNDARY
BLOCK SCHEMA. Confirm all seven columns. Then write Stage N+1. [Apply SC-2 before every
stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` in [A-04], [A-07], [A-10] is the sum of
all prior stage latencies and all prior boundary latencies at the time of writing. It may
not be deferred to [A-11]. A [A-04]/[A-07]/[A-10] block with a zero-reset value is a
protocol violation. [Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` in [A-04], [A-07], [A-10] = `FRESH` or `STALE`,
derived by comparing Elapsed (cumul.) against the [A-02] threshold. A [A-04]/[A-07]/[A-10]
cell with any value other than `FRESH` or `STALE` is a protocol violation. [Apply SC-4 at
every boundary block.]

**SC-5 — Immutability**: Finance appends to [A-02] verbatim: "This threshold is fixed. No
subsequent role may revise it after Stage 1 is written." Declare the SLA as an integer with
unit, derived from [A-01] total manual duration plus acceptable pipeline latency headroom.
Absence of this exact phrase in [A-02] is a protocol violation.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required outputs. Each is a
checklist; every item must be ticked ✓ or ✗. An unchecked [A-05] item blocks Operations;
an unchecked [A-08] item blocks Commerce. [Apply SC-6 before every role transition.]

**SC-7 — Stage table format**: Every stage block in [A-03], [A-06], [A-09] is a markdown
table with columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`. A
[A-03]/[A-06]/[A-09] stage table missing the `Stage Latency` column is a protocol
violation. [Apply SC-7 at every stage.]

**SC-8 — Trade-off as required section**: [A-14] TRADE-OFF ANALYSIS is a required named
section. Tokens [A-01], [A-02], and [A-13] must all appear in [A-14]. ≥1 alternative
pattern named. ≥2 trade-off dimensions. Omitting any of [A-01], [A-02], [A-13] from [A-14]
is a protocol violation. [Per REGISTER DECLARATION Part B.] [Apply SC-8 when producing
[A-14].]

**SC-9 — Incumbent Equiv. cell form**: Every `Incumbent Equiv.` cell in [A-04], [A-07],
[A-10] must use the form `[A-01]: [named manual step + duration]`. A [A-04]/[A-07]/[A-10]
cell lacking the `[A-01]` token is a protocol violation. [Per REGISTER DECLARATION Part A.]
[Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Produce [A-13] immediately before [A-14].
[A-13] sums all Incumbent Equiv. values from [A-04], [A-07], [A-10]; show additive
breakdown by role; Grand Total row required. [A-14] without a prior [A-13] is a protocol
violation. [Per REGISTER DECLARATION Part B.] [Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] INCUMBENT BASELINE must be the first artifact
written. No boundary block and no stage trace may appear before [A-01] is fully produced.
Any output before [A-01] is a positional protocol violation.

**SC-12 — Skip-level citation in Commerce**: Commerce's `Citing:` line must include
`[A-04]` — Finance's boundary checks, produced two positions prior in the Finance →
Operations → Commerce sequence. Operations is Commerce's immediate predecessor; a
`Citing:` line naming only Operations' tokens without `[A-04]` fails SC-12. Position
distance is two: Commerce occupies position 3, Finance occupies position 1. Absence of
`[A-04]` in Commerce's `Citing:` line is a protocol violation. A Phase Gate 2 item must
cite [SC-12] by its numbered identifier.

**SC-13 — BASELINE CLOSURE**: [A-01] must appear as a citation token in [A-12] RECOVERY
PRESCRIPTIONS — every recovery formula must include the `[A-01]` token — and in [A-14]
TRADE-OFF ANALYSIS — `[A-01]` is one of the three required citation tokens. [A-12] without
`[A-01]` token is a protocol violation. [A-14] without `[A-01]` token is a protocol
violation. [Per SC-13, cite [A-01] in [A-12].] [Per SC-13, cite [A-01] in [A-14].]

---

### ROLE 1 — Finance

[Finance runs first. No Citing line required. The incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST, before any domain context or stage trace. Per
SC-11: no boundary block and no stage trace may appear before [A-01] is fully produced.
Describe the manual PO-entry and order-processing workflow this pipeline replaces. Include
≥3 named manual steps with durations (e.g., "Finance coordinator receives emailed POs and
manually keys order header and line items into ERP: 45 min"; "Finance analyst validates PO
against approved vendor list and credit limit in ledger system: 30 min"; "Finance clerk
generates paper invoice and posts AR entry manually: 20 min"). Use entity names that will
reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 names from [A-01]): purchase order, order line item, vendor
  record, warehouse allocation, pick/pack manifest, shipment record, AR entry, revenue
  analytics record
- Downstream consumer and business cadence (e.g., daily order-to-cash close by 18:00)
- Order-close SLA: integer with unit, derived from [A-01] total manual duration plus
  acceptable pipeline latency headroom
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 1: Customer PO terminal → PO aggregation service
- Stage 2: PO aggregation → order validation service
- Stage 3: Validated order → invoice staging service

**[A-04] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA. One block after each
stage.
[SC-3: Elapsed (cumul.) starts at 0 and accumulates from Stage 1 latency.]
[SC-4: Verdict vs [A-02] threshold; do not restate numeric value.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named manual step + duration]`.]

**[A-05] PHASE GATE 1** — Produce and tick before Operations begins. Mark each ✓ or ✗:
- [ ] [A-01] produced first; no stage trace or boundary block precedes it (SC-11)
- [ ] [A-01] includes ≥3 named manual steps with durations
- [ ] [A-02] SLA declared as integer with unit, derived from [A-01]; SC-5 verbatim present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every stage in [A-03] has four required columns per SC-7
- [ ] Every block in [A-04] has seven columns; headers match REGISTER DECLARATION Part A
- [ ] Every `Elapsed (cumul.)` is a computed numeric sum (SC-3)
- [ ] Every `Verdict` is FRESH or STALE, derived from [A-02] threshold (SC-4)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)

Operations may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 4: Invoice staging → warehouse allocation service
- Stage 5: Warehouse allocation → pick/pack service
- Stage 6: Pick/pack complete → shipment dispatch service

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: Elapsed (cumul.) extends the final value in [A-04]; do not reset to zero.]
[SC-4: Verdict vs [A-02] threshold; do not redeclare threshold numeric value.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named manual step + duration]`.]

**[A-08] PHASE GATE 2** — Produce and tick before Commerce begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] has four required columns per SC-7
- [ ] Every block in [A-07] has seven columns; headers match REGISTER DECLARATION Part A
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] final value; not reset (SC-3)
- [ ] Every `Verdict` derives from [A-02] threshold; threshold value not redeclared (SC-4)
- [ ] Every `Incumbent Equiv.` cell in [A-07]: `[A-01]: [named step + duration]` (SC-9)
- [ ] [SC-12]: Commerce's `Citing:` line must include `[A-04]` — Finance's boundary
  checks, two positions prior in Finance → Operations → Commerce. Position distance is
  two: Commerce = position 3, Finance = position 1. Mark ✗ if [A-04] absent.

Commerce may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] is required per SC-12 — Finance's boundary checks, two positions prior in the
Finance → Operations → Commerce sequence. Operations is Commerce's immediate predecessor;
citing only [A-07] without [A-04] is a protocol violation. Position distance is two.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 7: Shipment dispatch → invoice generation service
- Stage 8: Invoice → AR posting service
- Stage 9: AR entry → revenue analytics dashboard

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend Elapsed (cumul.) from [A-07] final value.]
[SC-4: Verdict vs [A-02] threshold.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named manual step + duration]`.]

**[A-11] STALE ANALYSIS** — Using final Elapsed (cumul.) from [A-10]:

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

Produce separate rows for normal-operation and failure-mode staleness. Cite [A-02] by
token; do not restate the numeric threshold value.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01] in this section.] For every
`no handling — see [A-12]` annotation and every `Data Loss Flag: YES`, provide a specific
named recovery action. Required formula: `Fall back to [A-01] if [specific named failure
condition]`. The [A-01] token must appear in every recovery formula.

**[A-13] INCUMBENT TOTAL** — [Per REGISTER DECLARATION Part B. Per SC-10.] Produce
immediately before [A-14]. Header: `### [A-13] INCUMBENT TOTAL`.

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Finance | | |
| Operations | | |
| Commerce | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01] in this section.] [Per REGISTER
DECLARATION Part B. Per SC-8.] Header: `### [A-14] TRADE-OFF ANALYSIS`. Required tokens
in body: [A-01], [A-02], [A-13]. Named alternative pattern. ≥2 explicitly stated
trade-off dimensions. Absence of any of [A-01], [A-02], [A-13] is a protocol violation.

---

---

## V-02

**Axis**: Non-natural role sequence (Operations → Finance → Commerce) — skip-level stress
test, tabular

**Hypothesis**: Operations → Finance → Commerce; food & beverage manufacturing ingredient
procurement pipeline. Operations runs first and owns [A-01] (the manual ingredient
purchasing baseline), establishing the vocabulary and SLA that Finance and Commerce must
cite. Commerce (pos 3) must cite Operations' [A-04] boundary checks (pos 1) directly,
skipping Finance (pos 2) — the non-natural ordering forces the skip-level citation to
cross domain-role boundaries rather than discipline boundaries. C-52 DETECTABILITY INDEX
covers all 13 SCs including the reorganized SC-12 (skip target is now Operations, not
Finance). C-53 dual-slot anchoring applied to all [A-xx]-referencing SCs; SC-12 names
[A-04] in both governed-token and enforcement slots.

---

You are tracing data through a food & beverage manufacturing ingredient procurement pipeline
— supplier EDI order transmission through 3-way match and AP posting to GL cost allocation
and procurement analytics. Three expert roles run in the sequence
**Operations → Finance → Commerce**. Operations establishes the manual ingredient
purchasing baseline and entity vocabulary that Finance and Commerce must cite. Finance
handles AP settlement and GL posting; Commerce handles procurement analytics and category
spend reporting.

Commerce runs last and must cite Operations' boundary artifacts directly — two positions
prior in the Operations → Finance → Commerce sequence — as a required skip-level citation.
A Commerce `Citing:` line naming only Finance's artifacts without Operations' boundary
checks fails SC-12. Phase Gate 2 verifies this requirement by citing SC-12 by number.

The physical pipeline flows: supplier EDI gateway → PO transmission service → goods receipt
service → 3-way match engine → AP invoice posting service → GL cost allocation engine →
procurement analytics dashboard.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first. Every citation must
use the `[A-xx]` token exactly as spelled here.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Operations | Manual ingredient purchasing and PO-processing workflow replaced by this pipeline; ≥3 named steps with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, procurement-close SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration. |
| [A-03] | STAGE TRACE — Operations | Operations | Supplier EDI gateway → PO transmission service → goods receipt service; stage tables per SC-7. |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01]; required skip-level target for Commerce (SC-12). |
| [A-05] | PHASE GATE 1 | Operations | Self-verification checklist; all items ✓ before Finance begins. |
| [A-06] | STAGE TRACE — Finance | Finance | 3-way match engine → AP invoice posting service → GL cost allocation engine; stage tables per SC-7. |
| [A-07] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends Elapsed (cumul.) from [A-04]; Incumbent Equiv. cells cite [A-01]. |
| [A-08] | PHASE GATE 2 | Finance | Self-verification checklist; all items ✓ before Commerce begins; item [SC-12] verifies Commerce skip-level citation. |
| [A-09] | STAGE TRACE — Commerce | Commerce | GL cost allocation → procurement analytics dashboard → category spend report; stage tables per SC-7. |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends Elapsed (cumul.) from [A-07]; Incumbent Equiv. cells cite [A-01]. |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold. |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point; formula: `Fall back to [A-01] if [condition]`; SC-13 applies. |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14]. |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions; SC-8 and SC-13 apply. |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell form)
and C-35 (INCUMBENT TOTAL section format). An evaluator may determine pass/fail for both
criteria by reading this section alone.**

**Exhaustive closed verification chain** — every SC with governed artifact tokens,
enforcement mechanism, and detectability location:

**SC-1 CITATION OPENER** governs [A-06], [A-09]; enforced by token-match at each role's
opening `Citing:` line — an [A-06] or [A-09] role block that omits the `Citing:` line
fails, detectable from the role-opener line without reading the role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] (stage tables) and
[A-04], [A-07], [A-10] (boundary tables); enforced by inline lock — [A-03]/[A-06]/[A-09]
Stage N+1 may not be written until the preceding [A-04]/[A-07]/[A-10] boundary table is
complete; detectable at the stage-boundary position without inspecting stage content.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10]; enforced by Part A column
requirement — a [A-04]/[A-07]/[A-10] block with missing column or zero-reset fails;
detectable at column-header and cell-value level without reading row prose.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10]; enforced by Part A string
requirement — any [A-04]/[A-07]/[A-10] non-binary cell value fails; detectable at
cell-value level without reading surrounding prose.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; enforced by verbatim phrase requirement —
absence of "This threshold is fixed. No subsequent role may revise it after Stage 1 is
written." in [A-02] fails; detectable by phrase-match scan within [A-02] body.

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08]; enforced by gating callback —
unchecked [A-05] or [A-08] item blocks next role block; detectable at the role-boundary
line before reading role content.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09]; enforced by Part A column
requirement — a [A-03]/[A-06]/[A-09] table missing `Stage Latency` fails; detectable at
the table-header row without reading row contents.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] requiring [A-01], [A-02], [A-13];
enforced by three-token check — absence of any of [A-01], [A-02], [A-13] in [A-14] fails;
detectable from [A-14] citation token list without prose interpretation.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] requiring [A-01] in
every cell; enforced by Part A cell-form — a [A-04]/[A-07]/[A-10] cell lacking `[A-01]`
fails; detectable at cell level without reading surrounding prose.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] in relation to [A-14]; enforced
by Part B ordering — [A-13] must appear immediately before [A-14]; [A-14] without prior
[A-13] fails; detectable by artifact-order check at [A-14] header.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] as required first artifact; enforced by
positional lock — any output before [A-01] is a violation; detectable from the output
artifact-order head without reading artifact content.

**SC-12 SKIP-LEVEL CITATION IN COMMERCE** governs [A-04] (Operations' boundary checks) via
Commerce's `Citing:` line; enforced by Phase Gate 2 checklist item citing [SC-12] by
number — absence of `[A-04]` in Commerce's `Citing:` line fails; detectable by token-match
at Commerce role-opener line. Commerce = position 3; Operations = position 1; distance = two.

**SC-13 BASELINE CLOSURE** governs [A-12] and [A-14] requiring [A-01] in both; enforced by
inline callbacks at [A-12] and [A-14] headers — a [A-12] or [A-14] header lacking [A-01]
fails; detectable from the header line alone.

**Part A — Field compliance markers:** (identical column structure to V-01 Part A)

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum in minutes | Partial sum; reset to zero |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE` | Any other value |
| Error handling | `Error Handling` | Named mechanism or `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level changes or `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` | Token omitted; column absent |
| Stage latency (stage table) | `Stage Latency` | Explicit value, range, or characterization | Inferred from boundary elapsed only |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Table with Operations, Finance, Commerce, Grand Total rows | Prose-only; missing row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | [A-01], [A-02], [A-13] all present; ≥1 pattern; ≥2 dimensions | Any token absent |

---

### BOUNDARY BLOCK SCHEMA

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

Column headers must match Part A spellings exactly. This section is declared before any
role output.

---

### DETECTABILITY INDEX

Row count = 13 = SC count. A DETECTABILITY INDEX with fewer than 13 rows is incomplete.

| SC | Violation Detectable At |
|----|------------------------|
| SC-1 | Each non-first role's opening `Citing:` line — no role body reading required |
| SC-2 | Each stage-advance transition position — no stage content reading required |
| SC-3 | The `Elapsed (cumul.)` column header and cell-value level — no row prose required |
| SC-4 | The `Verdict` cell-value level — no surrounding prose required |
| SC-5 | Phrase-match scan within [A-02] body — no other sections required |
| SC-6 | The role-boundary line before each role block — no role content required |
| SC-7 | The stage table header row — no row contents required |
| SC-8 | The [A-14] citation token list — no prose interpretation required |
| SC-9 | The `Incumbent Equiv.` cell level — no surrounding prose required |
| SC-10 | The artifact-order position at the [A-14] header — no cell values required |
| SC-11 | The output artifact-order head — no artifact content required |
| SC-12 | Commerce role-opener `Citing:` line — no role body reading required |
| SC-13 | The [A-12] and [A-14] section header lines — no section body required |

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Operations opens with
`Citing: [A-xx], [A-yy], ...`. Citing [A-01] is required in every non-first role's Citing
line. An [A-06] or [A-09] role block that omits the `Citing:` line is a protocol violation.
[Apply SC-1 at every non-first role opener.]

**SC-2 — Stage-write progression gate**: [A-03]/[A-06]/[A-09] Stage N+1 may not be written
until the preceding [A-04]/[A-07]/[A-10] boundary table is fully populated. Confirm all
seven columns. Then write Stage N+1. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` in [A-04], [A-07], [A-10] is the sum
of all prior latencies. A [A-04]/[A-07]/[A-10] block with a zero-reset is a protocol
violation. [Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` in [A-04], [A-07], [A-10] = `FRESH` or `STALE`. A
[A-04]/[A-07]/[A-10] cell with any other value is a protocol violation. [Apply SC-4 at
every boundary block.]

**SC-5 — Immutability**: Operations appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written." Absence of this phrase in
[A-02] is a protocol violation.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required outputs. Unchecked [A-05]
blocks Finance; unchecked [A-08] blocks Commerce. [Apply SC-6 before every role
transition.]

**SC-7 — Stage table format**: Every stage block in [A-03], [A-06], [A-09] is a markdown
table with `Stage Latency | Schema In | Schema Out | Data Loss Flag`. A
[A-03]/[A-06]/[A-09] table missing `Stage Latency` is a protocol violation. [Apply SC-7
at every stage.]

**SC-8 — Trade-off as required section**: [A-14] requires tokens [A-01], [A-02], [A-13]
all present. ≥1 alternative pattern. ≥2 dimensions. Omitting any token from [A-14] is a
protocol violation. [Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: Every `Incumbent Equiv.` cell in [A-04], [A-07],
[A-10] must use `[A-01]: [named manual step + duration]`. A cell lacking `[A-01]` token is
a protocol violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Produce [A-13] immediately before [A-14].
[A-13] sums [A-04], [A-07], [A-10] Incumbent Equiv. values; Grand Total row required.
[A-14] without prior [A-13] is a protocol violation. [Apply SC-10 before [A-14].]

**SC-11 — Baseline-first production**: [A-01] must be the first artifact written. Any
output before [A-01] is a positional protocol violation.

**SC-12 — Skip-level citation in Commerce**: Commerce's `Citing:` line must include
`[A-04]` — Operations' boundary checks, two positions prior in Operations → Finance →
Commerce. Finance is Commerce's immediate predecessor; citing only Finance's tokens without
`[A-04]` fails SC-12. Position distance is two: Commerce = position 3, Operations =
position 1. Absence of `[A-04]` in Commerce's `Citing:` line is a protocol violation.

**SC-13 — BASELINE CLOSURE**: [A-01] must appear as a citation token in [A-12] and in
[A-14]. [A-12] without `[A-01]` is a protocol violation. [A-14] without `[A-01]` is a
protocol violation. [Per SC-13, cite [A-01] in [A-12].] [Per SC-13, cite [A-01] in [A-14].]

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required. The incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST. Describe the manual ingredient purchasing
workflow replaced by this pipeline. Include ≥3 named manual steps with durations (e.g.,
"Procurement coordinator manually reviews inventory reorder threshold report and faxes PO
to approved supplier: 40 min"; "Warehouse receiving clerk matches paper delivery note
against PO line items and enters discrepancies in spreadsheet: 35 min"; "Accounts payable
analyst manually keys invoice details into AP system and routes for approval: 25 min").
Use entity names that will reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 names from [A-01]): supplier EDI order, PO line item,
  goods receipt record, 3-way match result, AP invoice, GL cost allocation entry,
  procurement analytics record
- Downstream consumer and business cadence (e.g., weekly procurement close by Friday 17:00)
- Procurement-close SLA: integer with unit, derived from [A-01] total duration plus
  acceptable pipeline headroom
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 1: Supplier EDI gateway → PO transmission service
- Stage 2: PO transmission → goods receipt service
- Stage 3: Goods receipt → 3-way match engine

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA. One block per stage.
[SC-3: Elapsed (cumul.) starts at 0.] [SC-4: Verdict vs [A-02].] [SC-9: [A-01] in every cell.]

**[A-05] PHASE GATE 1** — Tick before Finance begins:
- [ ] [A-01] produced first (SC-11)
- [ ] [A-01] ≥3 named manual steps with durations
- [ ] [A-02] SLA integer with unit; SC-5 phrase present
- [ ] [A-02] reuses ≥2 [A-01] entity names
- [ ] [A-03] stages have four columns (SC-7)
- [ ] [A-04] blocks have seven columns matching Part A
- [ ] [A-04] Elapsed (cumul.) computed numeric sum (SC-3)
- [ ] [A-04] Verdicts are FRESH or STALE (SC-4)
- [ ] [A-04] Incumbent Equiv. cells cite [A-01] (SC-9)

Finance may not begin until all ✓. [Apply SC-6.]

---

### ROLE 2 — Finance

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 4: 3-way match engine → AP invoice posting service
- Stage 5: AP invoice → GL cost allocation engine
- Stage 6: GL cost entry → period-close reconciliation service

**[A-07] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-04] final Elapsed.] [SC-4: Verdict vs [A-02].] [SC-9: [A-01] in every cell.]

**[A-08] PHASE GATE 2** — Tick before Commerce begins:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] [A-06] stages have four columns (SC-7)
- [ ] [A-07] blocks have seven columns matching Part A
- [ ] [A-07] Elapsed extends [A-04]; not reset (SC-3)
- [ ] [A-07] Verdicts are FRESH or STALE (SC-4)
- [ ] [A-07] Incumbent Equiv. cells cite [A-01] (SC-9)
- [ ] [SC-12]: Commerce's Citing line must include [A-04] — Operations' boundary checks,
  two positions prior. Commerce = pos 3, Operations = pos 1. Distance = two.

Commerce may not begin until all ✓. [Apply SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12 — Operations' boundary checks, two positions prior. Finance is
the immediate predecessor; citing only [A-07] without [A-04] is a protocol violation.
Position distance is two.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 7: GL cost allocation → procurement analytics dashboard
- Stage 8: Analytics dashboard → category spend report
- Stage 9: Category spend → executive procurement scorecard

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-07].] [SC-4: [A-02].] [SC-9: [A-01] in every cell.]

**[A-11] STALE ANALYSIS** — Normal-operation and failure-mode elapsed vs [A-02] threshold.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Formula:
`Fall back to [A-01] if [specific named failure condition]`. [A-01] required in every formula.

**[A-13] INCUMBENT TOTAL** — Per Part B. Header: `### [A-13] INCUMBENT TOTAL`. Rows:
Operations, Finance, Commerce, Grand Total.

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] Header: `### [A-14] TRADE-OFF
ANALYSIS`. Required: [A-01], [A-02], [A-13]. ≥1 alternative pattern. ≥2 dimensions.

---

---

## V-03

**Axis**: Prose output format + SC-14 FORMAT MODE DECLARATION

**Hypothesis**: Finance → Operations → Commerce; SaaS metered billing to deferred revenue
recognition pipeline. The prose register activates SC-14 FORMAT MODE DECLARATION as a
required named entry in the REGISTER DECLARATION closed-chain paragraph. The DETECTABILITY
INDEX is reformulated as a numbered prose enumeration (not a table) that preserves the
machine-scannable row-count requirement — 13 numbered items, one per SC. C-53 dual-slot
anchoring appears in both the closed-chain paragraph and the STRUCTURAL CONSTRAINTS SC
bodies, adapted to prose form (governed tokens named in the sentence that identifies the
constraint, enforcement tokens named in the sentence that describes detection). SC-14 adds
a criterion-substitution map specifying how each tabular criterion (C-28, C-32, C-34)
is satisfied in prose mode.

---

You are tracing data through a SaaS metered billing to deferred revenue recognition pipeline
— usage event ingestion through billing calculation, invoice generation, deferred revenue
posting, and recognized revenue reporting. Three expert roles run in the sequence
**Finance → Operations → Commerce**. Finance establishes the manual usage-reconciliation
baseline and SLA; Operations handles billing engine and invoice staging; Commerce handles
deferred revenue accounting and recognized revenue analytics.

Commerce runs last and must cite Finance's boundary artifacts directly — two positions prior
in the Finance → Operations → Commerce sequence — as a required skip-level citation. A
Commerce citation paragraph naming only Operations' outputs without Finance's boundary
checks fails SC-12. Phase Gate 2 verifies this by citing SC-12 by number.

The physical pipeline flows: usage event collector → event aggregation service → metered
billing engine → invoice generation service → deferred revenue posting service → revenue
recognition trigger → recognized revenue analytics dashboard.

**Output format**: This prompt uses the **prose register**. All stage blocks and boundary
descriptions are rendered as labeled paragraphs, not markdown tables. SC-14 FORMAT MODE
DECLARATION governs criterion substitution for tabular requirements.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first. Every citation must
use the `[A-xx]` token form exactly.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Finance | Manual usage-reconciliation workflow; ≥3 named steps with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Finance | Entity vocabulary, revenue-recognition SLA (immutable after Stage 1), downstream consumer, business cadence. |
| [A-03] | STAGE TRACE — Finance | Finance | Usage event collector → event aggregation → metered billing engine; labeled paragraphs per SC-7/SC-14. |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | Labeled prose boundary blocks per BOUNDARY BLOCK SCHEMA/SC-14; Incumbent Equiv. sentences cite [A-01]; skip-level target for Commerce (SC-12). |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all items ✓ before Operations begins. |
| [A-06] | STAGE TRACE — Operations | Operations | Billing engine → invoice generation → invoice staging service; labeled paragraphs per SC-7/SC-14. |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | Labeled prose boundary blocks; extends Elapsed from [A-04]; Incumbent Equiv. sentences cite [A-01]. |
| [A-08] | PHASE GATE 2 | Operations | Self-verification checklist; [SC-12] item verifies Commerce skip-level. |
| [A-09] | STAGE TRACE — Commerce | Commerce | Deferred revenue posting → revenue recognition trigger → analytics dashboard; labeled paragraphs per SC-7/SC-14. |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | Labeled prose boundary blocks; extends Elapsed from [A-07]; Incumbent Equiv. sentences cite [A-01]. |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold. |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point; formula: `Fall back to [A-01] if [condition]`; SC-13 applies. |
| [A-13] | INCUMBENT TOTAL | Commerce | Additive prose summary of Incumbent Equiv. durations from [A-04], [A-07], [A-10]; Grand Total stated numerically; before [A-14]. |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions. |

---

### REGISTER DECLARATION

This output uses the **prose register**. Stage blocks and boundary blocks are rendered as
labeled paragraphs, not markdown tables. SC-14 FORMAT MODE DECLARATION is active.

**This section is the sole authoritative reference for C-34 (Incumbent Equiv. sentence
form) and C-35 (INCUMBENT TOTAL section format in prose mode). An evaluator may determine
pass/fail for both criteria by reading this section alone.**

**Exhaustive closed verification chain:**

**SC-1 CITATION OPENER** governs [A-06], [A-09]; enforced by token-match at each role's
opening `Citing:` sentence — an [A-06] or [A-09] role block that omits the `Citing:`
sentence fails; detectable from the role-opener sentence without reading the role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] (stage blocks) and
[A-04], [A-07], [A-10] (boundary blocks); enforced by inline lock — [A-03]/[A-06]/[A-09]
Stage N+1 prose may not be written until the preceding [A-04]/[A-07]/[A-10] boundary block
is fully stated; detectable at the stage-advance sentence without reading stage prose.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10]; enforced by Part A sentence
requirement — a [A-04]/[A-07]/[A-10] boundary block omitting the Elapsed sentence or
resetting to zero fails; detectable at the Elapsed sentence position in each block.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10]; enforced by Part A token
requirement — any [A-04]/[A-07]/[A-10] block lacking the exact word `FRESH` or `STALE`
fails; detectable at the Verdict sentence in each block.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; enforced by verbatim phrase requirement —
absence of "This threshold is fixed. No subsequent role may revise it after Stage 1 is
written." in [A-02] fails; detectable by phrase-match scan in [A-02].

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08]; enforced by gating callback —
unchecked [A-05] or [A-08] item blocks next role; detectable at the role-boundary line.

**SC-7 STAGE BLOCK FORMAT** governs [A-03], [A-06], [A-09]; in prose mode (per SC-14
substitution), each stage block is a labeled paragraph opening with the stage name and
including a Stage Latency sentence, Schema In sentence, Schema Out sentence, and Data Loss
sentence; a [A-03]/[A-06]/[A-09] stage block missing the Stage Latency sentence fails;
detectable at the opening sentence of the stage block.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] requiring [A-01], [A-02], [A-13];
enforced by three-token check — absence of any of [A-01], [A-02], [A-13] in [A-14] fails;
detectable from [A-14] body token scan.

**SC-9 INCUMBENT EQUIV. SENTENCE FORM** governs [A-04], [A-07], [A-10] requiring [A-01]
in every Incumbent Equiv. sentence; enforced by Part A sentence form — a
[A-04]/[A-07]/[A-10] block with an Incumbent Equiv. sentence lacking `[A-01]` fails;
detectable at the Incumbent Equiv. sentence in each block.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] in relation to [A-14]; enforced
by Part B ordering — [A-13] must appear before [A-14] and state a Grand Total numeric;
[A-14] without prior [A-13] fails; detectable at [A-14]'s opening sentence.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01]; enforced by positional lock — any
output before [A-01] fails; detectable from the output artifact-order head.

**SC-12 SKIP-LEVEL CITATION IN COMMERCE** governs [A-04] via Commerce's opening `Citing:`
sentence; enforced by Phase Gate 2 item citing [SC-12] by number — absence of `[A-04]`
in Commerce's Citing sentence fails; detectable at Commerce role-opener sentence.
Commerce = pos 3, Finance = pos 1, distance = two.

**SC-13 BASELINE CLOSURE** governs [A-12] and [A-14] requiring [A-01] in both; enforced
by callbacks at [A-12] and [A-14] section openers — a section opener lacking `[A-01]`
fails; detectable from the section-opener sentence alone.

**SC-14 FORMAT MODE DECLARATION** governs the prose-register criterion substitution map;
enforced by Part C below — any tabular criterion applied in its table form in prose mode
fails; detectable from the presence of markdown table syntax in stage or boundary blocks.

**Part A — Field compliance markers (prose boundary block sentences):**

| Required Field | Required Sentence Form | Disqualifying Form |
|----------------|----------------------|--------------------|
| Domain entity | Opens with: "**Entity**: [named entity from [A-02]]" | "data" or "records" alone |
| Elapsed (cumulative) | "**Elapsed (cumul.)**: [numeric] min (sum of [stage latencies named])" | Partial sum; reset |
| Freshness verdict | "**Verdict**: FRESH" or "**Verdict**: STALE" | Any other word |
| Error handling | "**Error Handling**: [named mechanism]" or "**Error Handling**: no handling — see [A-12]" | Silence; omission |
| Schema change | "**Schema Delta**: [named field changes]" or "**Schema Delta**: NONE" | Omission |
| Data loss | "**Data Loss**: YES — [loss point name]" or "**Data Loss**: NO" | Generic language |
| Incumbent equivalent | "**Incumbent Equiv.**: [A-01]: [named manual step + duration]" | [A-01] token absent |
| Stage latency (stage block) | "**Stage Latency**: [value or characterization]" | Absent from stage block |

**Part B — Section format compliance markers (prose mode):**

INCUMBENT TOTAL ([A-13]): Must be a labeled section beginning `### [A-13] INCUMBENT TOTAL`
containing: one sentence per role naming its Incumbent Equiv. subtotal, and a Grand Total
sentence with numeric value. Missing any role sentence or the Grand Total sentence fails.

TRADE-OFF ANALYSIS ([A-14]): Must be a labeled section beginning
`### [A-14] TRADE-OFF ANALYSIS` containing [A-01], [A-02], [A-13] token citations, ≥1
named alternative pattern, and ≥2 explicitly stated trade-off dimensions.

**Part C — SC-14 FORMAT MODE DECLARATION (criterion substitution map):**

| Tabular Criterion | Prose-Mode Equivalent |
|-------------------|-----------------------|
| C-28 (named-column boundary block schema) | BOUNDARY BLOCK SCHEMA section lists required sentence labels in order; label strings match Part A exactly |
| C-32 (register-specific compliance marker mapping) | Part A maps each field to its required sentence form and disqualifying form |
| C-34 (per-boundary Incumbent Equiv. column) | Each boundary block contains one `Incumbent Equiv.` labeled sentence with [A-01] token |

---

### BOUNDARY BLOCK SCHEMA

Standalone prose enumeration declared before any role output. Each boundary block must
contain the following labeled sentences in this order:

1. **Entity**: [value]
2. **Elapsed (cumul.)**: [value]
3. **Verdict**: FRESH or STALE
4. **Error Handling**: [value]
5. **Schema Delta**: [value]
6. **Data Loss**: [value]
7. **Incumbent Equiv.**: [A-01]: [value]

A boundary block missing any labeled sentence or presenting labels out of order fails the
schema.

---

### DETECTABILITY INDEX

Numbered prose enumeration. Item count = 14 = SC count (SC-1 through SC-13 plus SC-14).
An enumeration with fewer than 14 items is incomplete and fails C-52.

1. SC-1: detectable at each non-first role's opening `Citing:` sentence without reading the
   role body.
2. SC-2: detectable at each stage-advance sentence without reading stage prose.
3. SC-3: detectable at the `Elapsed (cumul.)` sentence position in each boundary block.
4. SC-4: detectable at the `Verdict` sentence in each boundary block.
5. SC-5: detectable by phrase-match scan within [A-02] body.
6. SC-6: detectable at the role-boundary line before reading any role content.
7. SC-7: detectable at the opening sentence of each stage block.
8. SC-8: detectable from the [A-14] body token scan without prose interpretation.
9. SC-9: detectable at the `Incumbent Equiv.` sentence in each boundary block.
10. SC-10: detectable at [A-14]'s opening sentence position without reading [A-14] body.
11. SC-11: detectable from the output artifact-order head without reading any artifact.
12. SC-12: detectable at Commerce role-opener `Citing:` sentence without reading role body.
13. SC-13: detectable from the [A-12] and [A-14] section-opener sentences.
14. SC-14: detectable from the presence or absence of Part C in REGISTER DECLARATION.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Finance opens with a `Citing:` sentence
listing every token from prior roles it builds on. An [A-06] or [A-09] role block omitting
the `Citing:` sentence is a protocol violation. [Apply SC-1 at every non-first role opener.]

**SC-2 — Stage-write progression gate**: [A-03]/[A-06]/[A-09] Stage N+1 prose may not
begin until the preceding [A-04]/[A-07]/[A-10] boundary block is fully stated with all
seven labeled sentences. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: Each [A-04]/[A-07]/[A-10] boundary block must include a
`Elapsed (cumul.)` sentence stating the numeric sum. A block resetting to zero or omitting
the sentence is a protocol violation. [Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: Each [A-04]/[A-07]/[A-10] boundary block must include a
`Verdict` sentence containing exactly `FRESH` or exactly `STALE`. A block lacking either
word is a protocol violation. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Finance appends to [A-02] verbatim: "This threshold is fixed. No
subsequent role may revise it after Stage 1 is written." Absence from [A-02] is a protocol
violation.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required outputs. Unchecked [A-05]
blocks Operations; unchecked [A-08] blocks Commerce. [Apply SC-6 before every transition.]

**SC-7 — Stage block format**: In prose mode (SC-14 substitution), each stage block in
[A-03]/[A-06]/[A-09] is a labeled paragraph with required sentences: Stage Latency, Schema
In, Schema Out, Data Loss. A [A-03]/[A-06]/[A-09] block missing the Stage Latency sentence
is a protocol violation. [Apply SC-7 at every stage.]

**SC-8 — Trade-off as required section**: [A-14] must contain tokens [A-01], [A-02],
[A-13]. Omitting any from [A-14] is a protocol violation. [Apply SC-8 when producing
[A-14].]

**SC-9 — Incumbent Equiv. sentence form**: Every `Incumbent Equiv.` sentence in
[A-04]/[A-07]/[A-10] must contain `[A-01]: [named manual step + duration]`. A sentence
lacking `[A-01]` token is a protocol violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Produce [A-13] before [A-14]. [A-13] must
include a Grand Total numeric sentence. [A-14] without prior [A-13] is a protocol
violation. [Apply SC-10 before [A-14].]

**SC-11 — Baseline-first production**: [A-01] is the first artifact written. Any output
before [A-01] is a positional protocol violation.

**SC-12 — Skip-level citation in Commerce**: Commerce's `Citing:` sentence must include
`[A-04]` — Finance's boundary checks, two positions prior. Omitting `[A-04]` from
Commerce's Citing sentence is a protocol violation. Position distance is two. A Phase Gate
2 item must cite [SC-12] by number.

**SC-13 — BASELINE CLOSURE**: [A-12] and [A-14] must each contain `[A-01]`. A section
opener lacking `[A-01]` is a protocol violation. [Per SC-13, cite [A-01] in [A-12].] [Per
SC-13, cite [A-01] in [A-14].]

**SC-14 — FORMAT MODE DECLARATION**: This prompt is in prose register. Part C of REGISTER
DECLARATION governs criterion substitution for C-28, C-32, and C-34. Any output rendering
stage or boundary content as a markdown table rather than labeled paragraphs is a protocol
violation detectable from the presence of markdown table syntax in the output.

---

### ROLE 1 — Finance

[Finance runs first. No Citing sentence required. Incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST. Describe the manual usage-reconciliation
workflow this pipeline replaces. Include ≥3 named manual steps with durations (e.g.,
"Finance analyst exports raw usage logs from hosting platform to spreadsheet and sums
metered units per customer: 60 min"; "Finance coordinator cross-checks computed billable
units against contract entitlement table: 40 min"; "Finance manager keys invoice amounts
into billing system and schedules deferred revenue entry: 25 min"). Use entity names
that will reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 names from [A-01]): usage event, metered unit, billable unit,
  invoice record, deferred revenue entry, recognized revenue event, analytics record
- Downstream consumer and business cadence (e.g., monthly revenue close on last business day)
- Revenue-recognition SLA: integer with unit, derived from [A-01] total duration plus
  acceptable pipeline headroom
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Finance** — Per SC-7 (prose form). Per SC-2.
- Stage 1: Usage event collector → event aggregation service
- Stage 2: Event aggregation → metered billing engine
- Stage 3: Metered billing output → invoice generation service

**[A-04] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA (prose form). One block
per stage. [SC-3.] [SC-4.] [SC-9: Incumbent Equiv. sentence cites [A-01].]

**[A-05] PHASE GATE 1** — Tick before Operations begins:
- [ ] [A-01] first (SC-11); ≥3 named steps
- [ ] [A-02] SLA integer with unit; SC-5 phrase present; ≥2 [A-01] entity names reused
- [ ] [A-03] stage blocks have Stage Latency sentence (SC-7)
- [ ] [A-04] blocks have all 7 labeled sentences (SC-3, SC-4, SC-9)

Operations may not begin until all ✓.

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Per SC-7 (prose). Per SC-2.
- Stage 4: Invoice generation → invoice staging service
- Stage 5: Invoice staging → deferred revenue posting service
- Stage 6: Deferred revenue entry → revenue recognition trigger

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-04].] [SC-4.] [SC-9: [A-01] in Incumbent Equiv. sentence.]

**[A-08] PHASE GATE 2** — Tick before Commerce begins:
- [ ] Citing sentence names [A-01], [A-02], [A-04] (SC-1)
- [ ] [A-06] stage blocks have Stage Latency (SC-7)
- [ ] [A-07] blocks have all 7 sentences; Elapsed extends [A-04] (SC-3); Verdicts binary (SC-4)
- [ ] [A-07] Incumbent Equiv. sentences cite [A-01] (SC-9)
- [ ] [SC-12]: Commerce's Citing sentence must include [A-04]. Distance = two.

Commerce may not begin until all ✓.

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12. Finance = pos 1, Commerce = pos 3. Distance = two. Omitting
[A-04] from Citing sentence is a protocol violation.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7 (prose). Per SC-2.
- Stage 7: Revenue recognition trigger → recognized revenue posting service
- Stage 8: Recognized revenue → revenue analytics dashboard
- Stage 9: Analytics dashboard → executive revenue report

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-07].] [SC-4.] [SC-9: [A-01] in Incumbent Equiv. sentence.]

**[A-11] STALE ANALYSIS** — Normal-operation and failure-mode elapsed vs [A-02] threshold,
stated in labeled prose sentences. Cite [A-02] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Formula:
`Fall back to [A-01] if [specific named failure condition]`. [A-01] in every formula.

**[A-13] INCUMBENT TOTAL** — Per Part B. `### [A-13] INCUMBENT TOTAL`. One sentence per
role (Finance subtotal, Operations subtotal, Commerce subtotal) and a Grand Total sentence.

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] `### [A-14] TRADE-OFF ANALYSIS`.
Tokens [A-01], [A-02], [A-13] in body. ≥1 alternative pattern. ≥2 dimensions.

---

---

## V-04

**Axes**: Maximum incumbent prominence (≥5 named manual steps in [A-01]) + non-natural role
sequence (Commerce → Finance → Operations)

**Hypothesis**: Commerce → Finance → Operations; retail store daily cash reconciliation to
GL pipeline. Commerce runs first and owns [A-01] — the manual cash drawer reconciliation
process — with ≥5 named steps and per-step durations, making [A-01] the most structurally
dense artifact. Finance (pos 2) cites Commerce's artifacts; Operations (pos 3) must cite
Commerce's [A-04] boundary checks (pos 1) directly, skipping Finance (pos 2). C-53 dual-
slot anchoring is maximally stressed by the depth of [A-01]: SC-9 and SC-13 enforcement
clauses trace multiple recovery paths back to [A-01]'s 5-step structure. DETECTABILITY
INDEX includes an `Incumbent Baseline Visibility` column flagging each SC that requires a
model to have read [A-01] before the violation is detectable. Row count = 13 = SC count.

---

You are tracing data through a retail store daily cash reconciliation to GL pipeline —
POS transaction capture through cash drawer reconciliation, daily tender summary, AP
clearing, and GL posting to financial analytics. Three expert roles run in the sequence
**Commerce → Finance → Operations**. Commerce establishes the manual cash drawer
reconciliation baseline and POS vocabulary that Finance and Operations must cite. Finance
handles AR clearing and GL posting; Operations handles COGS allocation and financial
analytics reporting.

Operations runs last and must cite Commerce's boundary artifacts directly — two positions
prior in the Commerce → Finance → Operations sequence — as a required skip-level citation.
An Operations `Citing:` line naming only Finance's artifacts without Commerce's boundary
checks fails SC-12. Phase Gate 2 verifies this by citing SC-12 by number.

The physical pipeline flows: POS terminal → transaction aggregation service → cash drawer
reconciliation service → daily tender summary service → AP clearing engine → GL posting
service → COGS allocation engine → financial analytics dashboard.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Commerce | Manual cash drawer reconciliation workflow; **≥5 named steps with per-step durations**; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Commerce | Entity vocabulary, daily-close SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration. |
| [A-03] | STAGE TRACE — Commerce | Commerce | POS terminal → transaction aggregation → cash drawer reconciliation → daily tender summary; stage tables per SC-7. |
| [A-04] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; Incumbent Equiv. cells cite [A-01]; required skip-level target for Operations (SC-12). |
| [A-05] | PHASE GATE 1 | Commerce | Self-verification checklist; all items ✓ before Finance begins. |
| [A-06] | STAGE TRACE — Finance | Finance | Daily tender summary → AP clearing engine → GL posting service; stage tables per SC-7. |
| [A-07] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends Elapsed from [A-04]; Incumbent Equiv. cells cite [A-01]. |
| [A-08] | PHASE GATE 2 | Finance | Self-verification checklist; [SC-12] item verifies Operations skip-level. |
| [A-09] | STAGE TRACE — Operations | Operations | GL posting → COGS allocation engine → financial analytics dashboard; stage tables per SC-7. |
| [A-10] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends Elapsed from [A-07]; Incumbent Equiv. cells cite [A-01]. |
| [A-11] | STALE ANALYSIS | Operations | Normal-operation and failure-mode elapsed vs [A-02] threshold. |
| [A-12] | RECOVERY PRESCRIPTIONS | Operations | Named recovery per loss point; `Fall back to [A-01] if [condition]`; SC-13 applies. |
| [A-13] | INCUMBENT TOTAL | Operations | Sum from [A-04], [A-07], [A-10]; role breakdown; before [A-14]. |
| [A-14] | TRADE-OFF ANALYSIS | Operations | Cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions. |

---

### REGISTER DECLARATION

Tabular register throughout.

**This section is the sole authoritative reference for C-34 and C-35.**

**Exhaustive closed verification chain:**

**SC-1 CITATION OPENER** governs [A-06], [A-09]; enforced by token-match — an [A-06] or
[A-09] role block missing its `Citing:` line fails; detectable from the role-opener line.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] (stage tables) and
[A-04], [A-07], [A-10] (boundary tables); enforced by inline lock — [A-03]/[A-06]/[A-09]
Stage N+1 may not be written until the preceding [A-04]/[A-07]/[A-10] boundary is complete;
detectable at stage-boundary transition.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10]; enforced by column requirement
— a [A-04]/[A-07]/[A-10] block with missing or reset Elapsed fails; detectable at
column-header and cell level.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10]; enforced by string requirement —
any [A-04]/[A-07]/[A-10] non-binary Verdict cell fails; detectable at cell-value level.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; enforced by verbatim phrase — absence from
[A-02] fails; detectable by phrase-match in [A-02].

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08]; enforced by gating callback —
unchecked [A-05] or [A-08] blocks next role; detectable at role-boundary line.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09]; enforced by column requirement
— a [A-03]/[A-06]/[A-09] table missing `Stage Latency` fails; detectable at table header.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] requiring [A-01], [A-02], [A-13];
enforced by three-token check — absence of any token in [A-14] fails; detectable from
[A-14] token list.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] requiring [A-01]; enforced
by Part A cell-form — a [A-04]/[A-07]/[A-10] cell lacking `[A-01]` fails; detectable at cell
level. Note: [A-01] contains ≥5 named steps; each Incumbent Equiv. cell cites one of those
named steps by name — a cell referencing a step not in [A-01]'s named list is also a
violation.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] in relation to [A-14]; enforced
by ordering — [A-13] must precede [A-14] and carry Grand Total; [A-14] without prior
[A-13] fails; detectable at [A-14] header position.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01]; enforced by positional lock — any
output before [A-01] fails; detectable from output head.

**SC-12 SKIP-LEVEL CITATION IN OPERATIONS** governs [A-04] (Commerce's boundary checks)
via Operations' `Citing:` line; enforced by Phase Gate 2 item citing [SC-12] by number —
absence of `[A-04]` in Operations' `Citing:` fails; detectable at Operations role-opener.
Operations = pos 3, Commerce = pos 1, distance = two.

**SC-13 BASELINE CLOSURE** governs [A-12] and [A-14] requiring [A-01]; enforced by
callbacks at [A-12] and [A-14] headers — a header lacking `[A-01]` fails; detectable from
header line alone.

**Part A:** (identical column structure to V-01 Part A — same eight fields, same headers)

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum in minutes | Partial; reset |
| Freshness verdict | `Verdict` | `FRESH` or `STALE` | Any other value |
| Error handling | `Error Handling` | Named mechanism or `no handling — see [A-12]` | Silence; omission |
| Schema change | `Schema Delta` | Named changes or `NONE` | Omission |
| Data loss | `Data Loss Flag` | `YES — [name]` or `NO` | Generic |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named step from ≥5-step list + duration]` | Token absent; step not from [A-01] list |
| Stage latency | `Stage Latency` | Explicit value or characterization | Inferred |

**Part B:**

| Required Section | Header | Required Form | Disqualifying Form |
|------------------|--------|---------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Table: Commerce, Finance, Operations, Grand Total rows; numeric subtotals | Missing row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | [A-01], [A-02], [A-13] present; ≥1 pattern; ≥2 dimensions | Token absent |

---

### BOUNDARY BLOCK SCHEMA

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

---

### DETECTABILITY INDEX

Row count = 13 = SC count. The `Incumbent Baseline Visibility` column flags SCs where the
violation is detectable without having read [A-01] (`independent`) vs. only after reading
[A-01]'s named-step list (`[A-01]-dependent`).

| SC | Violation Detectable At | Incumbent Baseline Visibility |
|----|------------------------|-------------------------------|
| SC-1 | Commerce/Finance role-opener `Citing:` line | independent |
| SC-2 | Stage-advance transition position | independent |
| SC-3 | `Elapsed (cumul.)` column header and cell level | independent |
| SC-4 | `Verdict` cell-value level | independent |
| SC-5 | Phrase-match scan within [A-02] | independent |
| SC-6 | Role-boundary line before each role block | independent |
| SC-7 | Stage table header row | independent |
| SC-8 | [A-14] citation token list | independent |
| SC-9 | `Incumbent Equiv.` cell level — step name must match [A-01] named list | [A-01]-dependent |
| SC-10 | Artifact-order at [A-14] header | independent |
| SC-11 | Output artifact-order head | independent |
| SC-12 | Operations role-opener `Citing:` line | independent |
| SC-13 | [A-12] and [A-14] section header lines | independent |

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Commerce opens with `Citing: [A-xx], ...`.
An [A-06] or [A-09] role block missing the `Citing:` line is a protocol violation. [Apply
SC-1 at every non-first role opener.]

**SC-2 — Stage-write progression gate**: [A-03]/[A-06]/[A-09] Stage N+1 may not be written
until [A-04]/[A-07]/[A-10] preceding boundary table is fully populated. [Apply SC-2 before
every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` in [A-04], [A-07], [A-10] accumulates
all prior latencies. A [A-04]/[A-07]/[A-10] block resetting to zero is a protocol
violation. [Apply SC-3.]

**SC-4 — Binary verdict**: `Verdict` in [A-04], [A-07], [A-10] = `FRESH` or `STALE`. Any
other value in [A-04]/[A-07]/[A-10] is a protocol violation. [Apply SC-4.]

**SC-5 — Immutability**: Commerce appends to [A-02]: "This threshold is fixed. No
subsequent role may revise it after Stage 1 is written." Absence is a protocol violation.

**SC-6 — Phase gate obligation**: [A-05] blocks Finance; [A-08] blocks Operations.
[Apply SC-6 before every transition.]

**SC-7 — Stage table format**: Every [A-03]/[A-06]/[A-09] table has columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. A missing `Stage Latency`
column is a protocol violation. [Apply SC-7.]

**SC-8 — Trade-off as required section**: [A-14] requires [A-01], [A-02], [A-13]. Omitting
any token from [A-14] is a protocol violation. [Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: Every `Incumbent Equiv.` cell in
[A-04]/[A-07]/[A-10] must use `[A-01]: [named step + duration]`, where the named step
appears in [A-01]'s ≥5-step list. A cell lacking `[A-01]` or citing an unnamed step is a
protocol violation. [Apply SC-9.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [A-13] precedes [A-14]; Grand Total required.
[A-14] without prior [A-13] is a protocol violation. [Apply SC-10.]

**SC-11 — Baseline-first production**: [A-01] is the first artifact. [A-01] must include
≥5 named manual steps with per-step durations. Any output before [A-01] is a violation.

**SC-12 — Skip-level citation in Operations**: Operations' `Citing:` line must include
`[A-04]` — Commerce's boundary checks, two positions prior. Finance is Operations'
immediate predecessor; citing only Finance's tokens without `[A-04]` fails. Position
distance is two: Operations = pos 3, Commerce = pos 1. Absence of `[A-04]` is a protocol
violation.

**SC-13 — BASELINE CLOSURE**: [A-12] must contain `[A-01]`. [A-14] must contain `[A-01]`.
A section lacking `[A-01]` is a protocol violation. [Per SC-13, cite [A-01] in [A-12].]
[Per SC-13, cite [A-01] in [A-14].]

---

### ROLE 1 — Commerce

[Commerce runs first. No Citing line required. Incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST. **Describe the manual cash drawer
reconciliation workflow with ≥5 named steps, each with a per-step duration.** Example
steps (adapt to scenario vocabulary):
1. "Cashier prints Z-report from POS register at end of shift and counts physical cash
   drawer: 5 min"
2. "Store manager reconciles counted cash total against Z-report net sales figure: 15 min"
3. "Manager records daily tender breakdown (cash, card, voucher) in daily summary form: 10 min"
4. "Finance coordinator manually enters daily summary totals into AP clearing spreadsheet: 20 min"
5. "Finance manager reviews AP clearing entries and posts approved GL journal entries: 15 min"

Use entity names that will reappear in [A-02]. Total manual duration = sum of all 5+
step durations.

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 names from [A-01]): POS transaction, cash drawer count,
  daily tender summary, AP clearing entry, GL journal entry, COGS allocation record,
  financial analytics record
- Downstream consumer and business cadence (e.g., nightly daily-close by 23:00)
- Daily-close SLA: integer with unit, derived from [A-01] total duration plus headroom
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 1: POS terminal → transaction aggregation service
- Stage 2: Transaction aggregation → cash drawer reconciliation service
- Stage 3: Cash drawer reconciliation → daily tender summary service

**[A-04] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: starts at 0.] [SC-4: vs [A-02].] [SC-9: `[A-01]: [named step from ≥5-step list]`.]

**[A-05] PHASE GATE 1** — Tick before Finance begins:
- [ ] [A-01] produced first (SC-11); includes ≥5 named steps with durations
- [ ] [A-02] SLA integer with unit; SC-5 phrase present; ≥2 [A-01] entity names
- [ ] [A-03] stages have four columns per SC-7
- [ ] [A-04] blocks: seven columns; Elapsed starts at 0 (SC-3); binary Verdicts (SC-4);
     Incumbent Equiv. cites [A-01] and names step from ≥5-step list (SC-9)

Finance may not begin until all ✓. [Apply SC-6.]

---

### ROLE 2 — Finance

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 4: Daily tender summary → AP clearing engine
- Stage 5: AP clearing → GL posting service
- Stage 6: GL journal entry → period reconciliation service

**[A-07] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-04].] [SC-4.] [SC-9: `[A-01]: [named step]`.]

**[A-08] PHASE GATE 2** — Tick before Operations begins:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] [A-06] stages have four columns (SC-7)
- [ ] [A-07] blocks: seven columns; Elapsed extends [A-04] (SC-3); binary Verdicts (SC-4);
     Incumbent Equiv. cites [A-01] named step (SC-9)
- [ ] [SC-12]: Operations' Citing line must include [A-04] — Commerce's boundary checks,
  two positions prior. Commerce = pos 1, Operations = pos 3. Distance = two.

Operations may not begin until all ✓. [Apply SC-6.]

---

### ROLE 3 — Operations

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12 — Commerce's boundary checks, two positions prior. Finance is
the immediate predecessor; citing only Finance's tokens without [A-04] is a protocol
violation. Position distance is two.)

**[A-09] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 7: GL posting → COGS allocation engine
- Stage 8: COGS allocation → financial analytics dashboard
- Stage 9: Analytics dashboard → executive financial report

**[A-10] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-07].] [SC-4.] [SC-9: `[A-01]: [named step from ≥5-step list]`.]

**[A-11] STALE ANALYSIS** — Normal-operation and failure-mode elapsed vs [A-02] threshold.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Formula:
`Fall back to [A-01] if [specific named failure condition]`. [A-01] in every formula.
Recovery options may reference any of the ≥5 named manual steps in [A-01] as fallback
procedures.

**[A-13] INCUMBENT TOTAL** — `### [A-13] INCUMBENT TOTAL`. Rows: Commerce, Finance,
Operations, Grand Total. Numeric subtotals from [A-04], [A-07], [A-10] respectively.

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] `### [A-14] TRADE-OFF ANALYSIS`.
Tokens [A-01], [A-02], [A-13] required. Use [A-13] Grand Total as numeric comparison
baseline. ≥1 alternative pattern. ≥2 dimensions.

---

---

## V-05

**Axes**: Lifecycle depth (Phase Gate 0 + SC-0; 14 SCs total) + non-natural role sequence
(Operations → Commerce → Finance)

**Hypothesis**: Operations → Commerce → Finance; telecom CDR-to-billing-to-revenue-GL
pipeline. A Phase Gate 0 artifact [A-00] is added as the first required output, governed
by SC-0. SC-0 raises the total SC count to 14 (SC-0 through SC-13). The DETECTABILITY
INDEX must have exactly 14 rows — row count verifiable against SC count — and Phase Gate 0
includes an explicit checklist item requiring the model to verify that the DETECTABILITY
INDEX row count equals 14 before Role 1 begins. This makes C-52's machine-scannable
coverage requirement a first-class gated output. Finance (pos 3) must cite Operations'
[A-04] boundary checks (pos 1) directly — skip-level over Commerce (pos 2). C-53 dual-slot
applied to all 14 SCs.

---

You are tracing data through a telecom CDR (call detail record) to billing to revenue GL
pipeline — CDR collection through usage aggregation, billing calculation, invoice
generation, and revenue posting to GL and revenue analytics. Three expert roles run in the
sequence **Operations → Commerce → Finance**. Operations establishes the CDR collection
baseline and entity vocabulary; Commerce handles billing calculation and invoice staging;
Finance handles revenue GL posting and analytics.

Finance runs last and must cite Operations' boundary artifacts directly — two positions
prior in the Operations → Commerce → Finance sequence — as a required skip-level citation.
A Finance `Citing:` line naming only Commerce's artifacts without Operations' boundary
checks fails SC-12. Phase Gate 2 verifies this by citing SC-12 by number.

Before Role 1 begins, produce [A-00] PHASE GATE 0 — a pre-trace setup checklist verifying
that the DETECTABILITY INDEX is complete and that ARTIFACT REGISTRY is fully populated.

The physical pipeline flows: CDR collector → CDR aggregation service → usage normalization
service → billing calculation engine → invoice generation service → revenue posting service
→ GL recognition engine → revenue analytics dashboard.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-00] is produced first. Every citation must
use the `[A-xx]` token exactly as spelled here.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-00] | PHASE GATE 0 | Pre-trace | Pre-trace setup checklist verifying DETECTABILITY INDEX completeness and ARTIFACT REGISTRY population; produced before Role 1. SC-0 applies. |
| [A-01] | INCUMBENT BASELINE | Operations | Manual CDR processing and billing workflow; ≥3 named steps with durations; produced FIRST within Role 1. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, billing-close SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01]. |
| [A-03] | STAGE TRACE — Operations | Operations | CDR collector → CDR aggregation → usage normalization; stage tables per SC-7. |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; Incumbent Equiv. cells cite [A-01]; required skip-level target for Finance (SC-12). |
| [A-05] | PHASE GATE 1 | Operations | Self-verification checklist; all items ✓ before Commerce begins. |
| [A-06] | STAGE TRACE — Commerce | Commerce | Billing calculation engine → invoice generation → invoice staging; stage tables per SC-7. |
| [A-07] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends Elapsed from [A-04]; Incumbent Equiv. cells cite [A-01]. |
| [A-08] | PHASE GATE 2 | Commerce | Self-verification checklist; [SC-12] item verifies Finance skip-level. |
| [A-09] | STAGE TRACE — Finance | Finance | Revenue posting → GL recognition engine → revenue analytics dashboard; stage tables per SC-7. |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends Elapsed from [A-07]; Incumbent Equiv. cells cite [A-01]. |
| [A-11] | STALE ANALYSIS | Finance | Normal-operation and failure-mode elapsed vs [A-02] threshold. |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery per loss point; `Fall back to [A-01] if [condition]`; SC-13 applies. |
| [A-13] | INCUMBENT TOTAL | Finance | Sum from [A-04], [A-07], [A-10]; role breakdown; before [A-14]. |
| [A-14] | TRADE-OFF ANALYSIS | Finance | Cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions. |

---

### REGISTER DECLARATION

Tabular register throughout.

**This section is the sole authoritative reference for C-34 and C-35.**

**Exhaustive closed verification chain — SC-0 through SC-13 (14 SCs):**

**SC-0 PHASE GATE 0 OBLIGATION** governs [A-00] (PHASE GATE 0); enforced by a positional
lock — [A-00] must appear before Role 1 begins; absence of [A-00] is a protocol violation
detectable from the artifact-order head without reading any role content.

**SC-1 CITATION OPENER** governs [A-06], [A-09]; enforced by token-match — an [A-06] or
[A-09] role block missing its `Citing:` line fails; detectable from the role-opener line.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] (stage tables) and
[A-04], [A-07], [A-10] (boundary tables); enforced by inline lock — Stage N+1 for
[A-03]/[A-06]/[A-09] may not be written until the preceding [A-04]/[A-07]/[A-10] boundary
table is complete; detectable at stage-boundary position.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10]; enforced by column requirement
— a [A-04]/[A-07]/[A-10] block missing or resetting Elapsed fails; detectable at column
header and cell level.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10]; enforced by string requirement —
any [A-04]/[A-07]/[A-10] non-binary Verdict fails; detectable at cell-value level.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; enforced by verbatim phrase — absence from
[A-02] fails; detectable by phrase-match within [A-02].

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08]; enforced by gating callback —
unchecked [A-05] or [A-08] blocks next role; detectable at role-boundary line.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09]; enforced by column requirement
— a [A-03]/[A-06]/[A-09] table missing `Stage Latency` fails; detectable at table header.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] requiring [A-01], [A-02], [A-13];
enforced by three-token check — absence of any token in [A-14] fails; detectable from
[A-14] token list.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] requiring [A-01] in
every cell; enforced by Part A cell-form — a [A-04]/[A-07]/[A-10] cell lacking `[A-01]`
fails; detectable at cell level.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] in relation to [A-14]; enforced
by ordering — [A-14] without prior [A-13] fails; detectable at [A-14] header position.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01]; enforced by positional lock within
Role 1 — any Role 1 output before [A-01] is a violation; detectable from Role 1 opening.

**SC-12 SKIP-LEVEL CITATION IN FINANCE** governs [A-04] (Operations' boundary checks) via
Finance's `Citing:` line; enforced by Phase Gate 2 item citing [SC-12] by number — absence
of `[A-04]` in Finance's `Citing:` fails; detectable at Finance role-opener line.
Finance = pos 3, Operations = pos 1, distance = two.

**SC-13 BASELINE CLOSURE** governs [A-12] and [A-14] requiring [A-01]; enforced by
callbacks — a [A-12] or [A-14] header lacking `[A-01]` fails; detectable from header line.

**Part A:** (same eight-field structure as V-01)

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum in minutes | Partial; reset |
| Freshness verdict | `Verdict` | `FRESH` or `STALE` | Any other value |
| Error handling | `Error Handling` | Named mechanism or `no handling — see [A-12]` | Silence; omission |
| Schema change | `Schema Delta` | Named changes or `NONE` | Omission |
| Data loss | `Data Loss Flag` | `YES — [name]` or `NO` | Generic |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` | Token absent |
| Stage latency | `Stage Latency` | Explicit value or characterization | Inferred |

**Part B:**

| Required Section | Header | Required Form | Disqualifying Form |
|------------------|--------|---------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Rows: Operations, Commerce, Finance, Grand Total; numeric | Missing row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | [A-01], [A-02], [A-13] present; ≥1 pattern; ≥2 dimensions | Token absent |

---

### BOUNDARY BLOCK SCHEMA

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

---

### DETECTABILITY INDEX

Row count = **14** = SC count (SC-0 through SC-13). A DETECTABILITY INDEX with fewer than
14 rows is incomplete and fails C-52. [A-00] Phase Gate 0 verifies this row count before
Role 1 begins.

| SC | Violation Detectable At |
|----|------------------------|
| SC-0 | Output artifact-order head before Role 1 — absence of [A-00] detectable without reading any role |
| SC-1 | Each non-first role's opening `Citing:` line — no role body reading required |
| SC-2 | Each stage-advance transition position — no stage content reading required |
| SC-3 | `Elapsed (cumul.)` column header and cell-value level — no row prose required |
| SC-4 | `Verdict` cell-value level — no surrounding prose required |
| SC-5 | Phrase-match scan within [A-02] body — no other sections required |
| SC-6 | Role-boundary line before each role block — no role content required |
| SC-7 | Stage table header row — no row contents required |
| SC-8 | [A-14] citation token list — no prose interpretation required |
| SC-9 | `Incumbent Equiv.` cell level — no surrounding prose required |
| SC-10 | Artifact-order position at [A-14] header — no cell values required |
| SC-11 | Role 1 opening artifact order — no artifact content reading required |
| SC-12 | Finance role-opener `Citing:` line — no role body reading required |
| SC-13 | [A-12] and [A-14] section header lines — no section body required |

---

### STRUCTURAL CONSTRAINTS

**SC-0 — Phase Gate 0 obligation**: [A-00] PHASE GATE 0 must be produced before Role 1
begins. [A-00] is a required pre-trace artifact. Absence of [A-00] before [A-01] is a
positional protocol violation detectable from the output head. [Apply SC-0 before Role 1.]

**SC-1 — Citation opener**: Every role other than Operations opens with
`Citing: [A-xx], ...`. An [A-06] or [A-09] role block missing the `Citing:` line is a
protocol violation. [Apply SC-1 at every non-first role opener.]

**SC-2 — Stage-write progression gate**: [A-03]/[A-06]/[A-09] Stage N+1 may not be written
until the preceding [A-04]/[A-07]/[A-10] boundary table is fully populated. [Apply SC-2
before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` in [A-04], [A-07], [A-10] accumulates
all prior latencies. A reset is a protocol violation. [Apply SC-3.]

**SC-4 — Binary verdict**: `Verdict` in [A-04], [A-07], [A-10] = `FRESH` or `STALE`.
Any other value is a protocol violation. [Apply SC-4.]

**SC-5 — Immutability**: Operations appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written." Absence is a protocol violation.

**SC-6 — Phase gate obligation**: [A-05] blocks Commerce; [A-08] blocks Finance.
[Apply SC-6 before every transition.]

**SC-7 — Stage table format**: Every [A-03]/[A-06]/[A-09] table has
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. Missing `Stage Latency` is a
protocol violation. [Apply SC-7.]

**SC-8 — Trade-off as required section**: [A-14] requires [A-01], [A-02], [A-13]. Omitting
any is a protocol violation. [Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: Every `Incumbent Equiv.` cell in
[A-04]/[A-07]/[A-10] must use `[A-01]: [named step + duration]`. A cell lacking `[A-01]`
is a protocol violation. [Apply SC-9.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [A-13] precedes [A-14]; Grand Total required.
[A-14] without prior [A-13] is a violation. [Apply SC-10.]

**SC-11 — Baseline-first production within Role 1**: [A-01] is the first artifact written
inside Role 1. Any Role 1 content before [A-01] is a positional protocol violation.

**SC-12 — Skip-level citation in Finance**: Finance's `Citing:` line must include `[A-04]`
— Operations' boundary checks, two positions prior. Commerce is Finance's immediate
predecessor; citing only Commerce's tokens without `[A-04]` fails. Position distance is
two: Finance = pos 3, Operations = pos 1. Absence of `[A-04]` is a protocol violation.

**SC-13 — BASELINE CLOSURE**: [A-12] and [A-14] must each contain `[A-01]`. A section
lacking `[A-01]` is a protocol violation. [Per SC-13, cite [A-01] in [A-12].] [Per SC-13,
cite [A-01] in [A-14].]

---

### PRE-TRACE — Phase Gate 0

[Produce [A-00] before Role 1. This artifact verifies prompt structure completeness.]

**[A-00] PHASE GATE 0** — Mark each ✓ or ✗ before Role 1 begins:
- [ ] ARTIFACT REGISTRY contains 15 rows ([A-00] through [A-14])
- [ ] REGISTER DECLARATION is present and includes Parts A and B
- [ ] BOUNDARY BLOCK SCHEMA is present with seven named columns
- [ ] DETECTABILITY INDEX is present with exactly **14 rows** (= SC count SC-0 through
  SC-13); row count verified by counting rows before proceeding
- [ ] STRUCTURAL CONSTRAINTS lists SC-0 through SC-13 (14 constraints total)
- [ ] [A-00] is declared in ARTIFACT REGISTRY as a Phase Gate 0 artifact (SC-0)

Role 1 may not begin until all items are ✓. [Apply SC-0.]

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required. Produce [A-01] first per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST within Role 1. Describe the manual CDR
processing and billing workflow this pipeline replaces. Include ≥3 named manual steps with
durations (e.g., "Operations analyst exports CDR file from switch vendor portal and loads
into billing spreadsheet: 60 min"; "Billing coordinator manually maps each CDR record to
the correct rate plan and calculates charges in spreadsheet: 90 min"; "Finance analyst
keys computed invoice totals into billing system and posts AR entries: 30 min"). Use entity
names that will reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 names from [A-01]): CDR record, usage event, normalized
  usage record, billing calculation result, invoice record, revenue posting entry,
  GL recognition entry, analytics record
- Downstream consumer and business cadence (e.g., monthly billing close on the 1st)
- Billing-close SLA: integer with unit, derived from [A-01] total duration plus headroom
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 1: CDR collector → CDR aggregation service
- Stage 2: CDR aggregation → usage normalization service
- Stage 3: Normalized usage → billing calculation engine handoff

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA. One block per stage.
[SC-3: starts at 0.] [SC-4: vs [A-02].] [SC-9: `[A-01]: [named step + duration]`.]

**[A-05] PHASE GATE 1** — Tick before Commerce begins:
- [ ] [A-01] produced first (SC-11); ≥3 named steps
- [ ] [A-02] SLA integer; SC-5 phrase present; ≥2 [A-01] entity names
- [ ] [A-03] stage tables: four columns (SC-7)
- [ ] [A-04] boundary blocks: seven columns; Elapsed from 0 (SC-3); binary Verdicts (SC-4);
     Incumbent Equiv. cites [A-01] (SC-9)

Commerce may not begin until all ✓. [Apply SC-6.]

---

### ROLE 2 — Commerce

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 4: Billing calculation engine → invoice generation service
- Stage 5: Invoice generation → invoice staging service
- Stage 6: Invoice staging → revenue posting handoff

**[A-07] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-04].] [SC-4.] [SC-9: [A-01] in every cell.]

**[A-08] PHASE GATE 2** — Tick before Finance begins:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] [A-06] stage tables: four columns (SC-7)
- [ ] [A-07] blocks: seven columns; Elapsed extends [A-04] (SC-3); binary (SC-4);
     Incumbent Equiv. cites [A-01] (SC-9)
- [ ] [SC-12]: Finance's Citing line must include [A-04] — Operations' boundary checks,
  two positions prior. Finance = pos 3, Operations = pos 1. Distance = two.

Finance may not begin until all ✓. [Apply SC-6.]

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12 — Operations' boundary checks, two positions prior. Commerce is
the immediate predecessor; citing only Commerce's tokens without [A-04] is a protocol
violation. Position distance is two.)

**[A-09] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 7: Revenue posting → GL recognition engine
- Stage 8: GL recognition → revenue analytics dashboard
- Stage 9: Revenue analytics → executive billing summary report

**[A-10] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-07].] [SC-4.] [SC-9: [A-01] in every cell.]

**[A-11] STALE ANALYSIS** — Normal-operation and failure-mode elapsed vs [A-02] threshold.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Formula:
`Fall back to [A-01] if [specific named failure condition]`. [A-01] in every formula.

**[A-13] INCUMBENT TOTAL** — `### [A-13] INCUMBENT TOTAL`. Rows: Operations, Commerce,
Finance, Grand Total. Numeric subtotals from [A-04], [A-07], [A-10].

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] `### [A-14] TRADE-OFF ANALYSIS`.
Tokens [A-01], [A-02], [A-13] required. ≥1 alternative pattern. ≥2 dimensions.
