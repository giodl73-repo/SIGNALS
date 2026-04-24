# flow-dataflow — Round 17 Variations

## R16 gap summary before writing

**C-50 target for R17**: R16 variations introduced C-48 (governed artifact tokens named in
every SC closed-chain entry) and C-49 (enforcement mechanism named in every SC closed-chain
entry). C-50 narrows the requirement to the four SCs that touch [A-01] in a load-bearing
way — SC-8, SC-9, SC-11, SC-13. For these four, the same [A-01] authority token must appear
in **both** the governed-token declaration slot **and** the enforcement-mechanism slot of the
same SC entry. C-48 required the governed artifact tokens to be named; C-50 requires that
for these four SCs, [A-01] is not only named as a governed artifact but also appears
explicitly inside the enforcement-mechanism description — dual-slot anchoring within a
single entry block. A variation where SC-11 says "governs [A-01]" (governed-token slot ✓)
but whose enforcement clause names only "positional lock" without the [A-01] token satisfies
C-48 but fails C-50.

**C-51 target for R17**: R16 required enforcement mechanisms to be named per C-49. C-51
adds a detectability-location requirement: the enforcement mechanism description must
explicitly name the structural location in the output where a violation would surface. A
description like "fails by token-match" is acceptable for C-49 but insufficient for C-51
because it does not say *where* the token-match check fires. C-51 requires the location to
be named — for example, "detectable from the header line alone", "detectable at the
column-header level without reading row contents", "detectable by token-match at the
role-opener line without reading the role body". Every SC entry in the closed-chain
paragraph must carry this location qualifier, not only SC-12 and SC-13.

Both C-50 and C-51 apply globally — C-50 to the four [A-01]-load-bearing SCs and C-51 to
every SC listed in the paragraph.

## Variation axes

- **V-01**: Role sequence (natural Finance→Operations→Commerce) — hotel F&B charges-to-
  revenue-ledger pipeline. C-50 dual-slot anchoring in SC-8, SC-9, SC-11, SC-13.
  C-51 detectability-location in all 13 SC entries. Tabular register.

- **V-02**: Role sequence (non-natural Operations→Finance→Commerce) — B2B distribution
  fulfillment-to-invoicing pipeline. Commerce (pos 3) cites Operations [A-04] (pos 1)
  skip-level. C-50 + C-51 throughout. Tabular register.

- **V-03**: Output format — prose register (C-50 + C-51 + SC-14 FORMAT MODE DECLARATION);
  SaaS subscription renewal/churn reporting pipeline. Finance → Operations → Commerce.
  SC-14 as named navigation entry in closed-chain paragraph; criterion substitution map
  in REGISTER DECLARATION Part C. C-51 location language adapted to prose register
  (e.g., "detectable from the opening sentence of the section").

- **V-04**: Inertia framing — maximum incumbent baseline prominence (C-50 + C-51);
  retail loyalty points-to-liability-ledger pipeline. Finance → Operations → Commerce.
  [A-01] requires ≥5 named manual steps with per-step durations. SC-8, SC-9, SC-11,
  SC-13 closed-chain entries maximally explicit about [A-01] dual-slot. Tabular register.

- **V-05**: Combined — non-natural role sequence (Operations→Commerce→Finance) + lifecycle
  depth (Phase Gate 0 added as pre-trace setup gate); telecom CDR-to-billing-to-GL
  pipeline. Finance (pos 3) cites Operations [A-04] (pos 1) skip-level. C-50 + C-51.
  Tabular register.

---

## V-01

**Axis**: C-50 dual-slot anchoring + C-51 detectability-location — natural role sequence,
tabular

**Hypothesis**: Finance → Operations → Commerce; hotel F&B charges-to-revenue-ledger
pipeline. A closed-chain paragraph where SC-8, SC-9, SC-11, SC-13 each carry [A-01] in
both the governed-token declaration and the enforcement mechanism — dual-slot anchoring —
and where every SC entry names the structural location where a violation surfaces, makes the
paragraph a complete self-describing authority map navigable by token match and location
index alone. Commerce (pos 3) cites Finance [A-04] (pos 1) skip-level per SC-12.

---

You are tracing data through a hotel food-and-beverage charges-to-revenue-ledger pipeline —
outlet POS capture through nightly batch settlement to AR ledger to Commerce BI. Three
expert roles run in the sequence **Finance → Operations → Commerce**. Finance establishes
the daily revenue-close SLA and the manual charge-posting baseline that all subsequent
roles must cite. Operations and Commerce cite Finance's artifacts by token; they may not
redeclare or re-derive either.

Commerce runs last and must cite Finance's boundary artifacts directly — two positions prior
in the Finance → Operations → Commerce sequence — as a required skip-level citation. A
Commerce `Citing:` line naming only Operations' artifacts without Finance's boundary checks
fails SC-12. Phase Gate 2 verifies this requirement by citing SC-12 by number.

The physical pipeline flows: outlet POS terminal → POS aggregation service → revenue
capture service → nightly settlement batch → AR ledger posting service → revenue
recognition engine → Commerce BI dashboard.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first; all subsequent
artifacts follow in token order. Every citation must use the `[A-xx]` token exactly as
spelled here. A citation to a token not listed here is a protocol violation.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Finance | Manual F&B charge-posting workflow replaced by this pipeline; ≥3 named steps with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Finance | Entity vocabulary, revenue-close SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Finance | Finance | POS terminal → POS aggregation → revenue capture → nightly settlement batch; stage tables per SC-7 |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01]; required skip-level target for Commerce (SC-12) |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all items ✓ before Operations begins |
| [A-06] | STAGE TRACE — Operations | Operations | Settlement batch → AR ledger posting → revenue recognition engine; stage tables per SC-7 |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends Elapsed (cumul.) from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Operations | Self-verification checklist; all items ✓ before Commerce begins; item [SC-12] verifies Commerce skip-level citation |
| [A-09] | STAGE TRACE — Commerce | Commerce | Revenue recognition entry → Commerce BI aggregation → executive revenue dashboard; stage tables per SC-7 |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends Elapsed (cumul.) from [A-07]; Incumbent Equiv. cells cite [A-01] |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point and no-handling annotation; formula: `Fall back to [A-01] if [condition]`; SC-13 applies |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions; SC-13 applies |

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
token-match at each role's opening `Citing:` line — a role block that omits the `Citing:`
line or uses prose-only back-references fails, and the violation is detectable from the
role-opener line without reading the role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] (stage tables) and
[A-04], [A-07], [A-10] (boundary tables); enforced by an inline lock at every stage
advance — Stage N+1 may not be written until the preceding boundary table is fully
populated per BOUNDARY BLOCK SCHEMA; the gate fires as a per-transition callback
detectable at the stage-boundary position without inspecting stage content.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (boundary tables, `Elapsed
(cumul.)` column); enforced by Part A column requirement — a boundary block with a missing
column or a zero-reset value fails, and the violation is detectable at the column-header
and cell-value level without reading row prose.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (boundary tables, `Verdict`
column); enforced by Part A string requirement — any cell value other than exactly `FRESH`
or exactly `STALE` fails, and the violation is detectable at the cell-value level without
reading surrounding prose.

**SC-5 STALENESS IMMUTABILITY** governs [A-02] (DOMAIN CONTEXT); enforced by verbatim
phrase requirement — absence of the exact phrase "This threshold is fixed. No subsequent
role may revise it after Stage 1 is written." fails, and the violation is detectable by
phrase-match scan within [A-02]'s body without searching other sections.

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08] (phase gates); enforced by a
gating callback at every role transition — an unchecked phase gate item blocks the next
role block, and the violation is detectable at the role-boundary line before reading any
role content.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09] (stage tables, `Stage Latency`
column); enforced by Part A column requirement — a stage table missing the `Stage Latency`
column fails, and the violation is detectable at the table-header row without reading row
contents.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] (TRADE-OFF ANALYSIS) requiring
[A-01] as a mandatory citation token inside [A-14]; enforced by a three-token check —
`[A-01]`, `[A-02]`, and `[A-13]` must all appear in [A-14]; absence of [A-01] is a
protocol violation detectable from [A-14]'s citation token list without prose
interpretation.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] (`Incumbent Equiv.`
column) requiring [A-01] as a mandatory token in every cell; enforced by Part A cell-form
requirement — a cell lacking the `[A-01]` token is a protocol violation detectable at the
cell level without reading surrounding prose.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] (INCUMBENT TOTAL); enforced by
Part B ordering requirement — [A-13] must appear immediately before [A-14] and carry a
Grand Total row; the violation is detectable by artifact-order check at the [A-14]
header position without reading cell values.

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
both [A-12] and [A-14] section headers that verify the [A-01] token by token match —
a section header lacking the [A-01] token is a protocol violation detectable from the
header line alone.

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
REGISTER DECLARATION Part A spellings exactly. Role instructions reference this section
by name only; they do not restate field requirements.

**Every boundary block must be a markdown table with these columns, in this order:**

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

A column absent, renamed, or not matching Part A header strings fails the schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Finance opens with
`Citing: [A-xx], [A-yy], ...` listing every token from prior roles this role builds on.
Citing [A-01] is required in every non-first role's Citing line. Prose back-references do
not satisfy SC-1. [Apply SC-1 at every non-first role opener.]

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding
BOUNDARY CHECK table is fully populated per BOUNDARY BLOCK SCHEMA. Confirm all seven
columns. Then write Stage N+1. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` is the sum of all prior stage latencies
and all prior boundary latencies at the time of writing. It may not be deferred to [A-11].
[Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE`, derived by comparing
Elapsed (cumul.) against the [A-02] threshold. Cite [A-02] by token; do not restate its
numeric value. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Finance appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written." Declare the SLA as an integer
with unit, derived from [A-01] total manual duration plus acceptable pipeline latency
headroom.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required outputs. Each is a
checklist; every item must be ticked ✓ or ✗. The next role may not begin until all items
are ✓. [Apply SC-6 before every role transition.]

**SC-7 — Stage table format**: Every stage block is a markdown table with columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. [Apply SC-7 at every stage.]

**SC-8 — Trade-off as required section**: [Per REGISTER DECLARATION Part B, TRADE-OFF
ANALYSIS row.] All three tokens required: [A-01], [A-02], [A-13]. ≥1 alternative pattern
named. ≥2 trade-off dimensions. [Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: [Per REGISTER DECLARATION Part A, `Incumbent
Equiv.` row.] Required form: `[A-01]: [named manual step + duration]`. Omitting the
[A-01] token is a protocol violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [Per REGISTER DECLARATION Part B, INCUMBENT
TOTAL row.] Produce [A-13] immediately before [A-14]. Sum all Incumbent Equiv. values from
[A-04], [A-07], [A-10]; show additive breakdown by role; Grand Total row required.
[Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] INCUMBENT BASELINE must be the first artifact
written. No boundary block and no stage trace may appear before [A-01] is fully produced.

**SC-12 — Skip-level citation in Commerce**: Commerce's `Citing:` line must include
`[A-04]` — Finance's boundary checks, produced two positions prior in the
Finance → Operations → Commerce sequence. Operations is Commerce's immediate predecessor;
a `Citing:` line naming only Operations' tokens without `[A-04]` fails SC-12. Position
distance is two: Commerce occupies position 3, Finance occupies position 1. A Phase Gate 2
verification item must cite [SC-12] by its numbered identifier in the item text.

**SC-13 — BASELINE CLOSURE**: [A-01] INCUMBENT BASELINE must appear as a citation token
in [A-12] RECOVERY PRESCRIPTIONS — every recovery formula must include the `[A-01]` token
— and in [A-14] TRADE-OFF ANALYSIS — `[A-01]` is one of the three required citation
tokens. [Per SC-13, cite [A-01] in [A-12].] [Per SC-13, cite [A-01] in [A-14].]

---

### ROLE 1 — Finance

[Finance runs first. No Citing line required. The incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST, before any domain context or stage trace.
Per SC-11: no boundary block and no stage trace may appear before [A-01] is fully produced.
Describe the manual F&B charge-posting workflow this pipeline replaces. Include ≥3 named
manual steps with durations (e.g., "F&B supervisor exports end-of-shift POS sales report
to spreadsheet and reconciles against register tape: 60 min", "Finance analyst keys
individual outlet totals into revenue journal in property management system: 45 min",
"Night auditor verifies AR ledger balance against daily F&B revenue summary: 30 min").
Use entity names that will reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 names from [A-01]): POS transaction, outlet revenue batch,
  settlement batch, AR ledger entry, revenue recognition entry, BI aggregation record
- Downstream consumer and business cadence (e.g., nightly revenue close at 23:59 local)
- Revenue-close SLA: integer with unit, derived from [A-01] total manual duration plus
  acceptable pipeline latency headroom
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 1: Outlet POS terminal → POS aggregation service
- Stage 2: Aggregated POS batch → Revenue capture service
- Stage 3: Captured revenue batch → Nightly settlement batch processor

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
- [ ] Every `Elapsed (cumul.)` is a computed numeric sum inside the block (SC-3)
- [ ] Every `Verdict` is FRESH or STALE, derived from [A-02] threshold (SC-4)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)

Operations may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 4: Settlement batch → AR ledger posting service
- Stage 5: AR ledger entry → Revenue recognition engine

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
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)
- [ ] [SC-12]: Commerce's `Citing:` line must include `[A-04]` — Finance's boundary
  checks, two positions prior in the Finance → Operations → Commerce sequence.
  Position distance is two: Commerce = position 3, Finance = position 1. Mark ✗ if
  [A-04] is absent from Commerce's Citing line.

Commerce may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] is required per SC-12 — Finance's boundary checks, two positions prior in the
Finance → Operations → Commerce sequence. Operations is Commerce's immediate predecessor;
citing only [A-07] without [A-04] fails SC-12. Position distance is two.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 6: Revenue recognition entry → Commerce BI aggregation layer
- Stage 7: BI aggregation → Executive revenue dashboard

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
condition]`. Cite [A-01] using this formula at least once.

**[A-13] INCUMBENT TOTAL** — [Per REGISTER DECLARATION Part B. Per SC-10.] Produce
immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Finance | | |
| Operations | | |
| Commerce | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01] in this section.] [Per REGISTER
DECLARATION Part B. Per SC-8.] Required named section. Cite `[A-01]`, `[A-02]`, and
`[A-13]` — all three tokens required. Name ≥1 alternative data propagation pattern.
Provide ≥2 trade-off dimensions using [A-13] Grand Total as the numeric comparison
endpoint.

---

---

## V-02

**Axis**: Role sequence — non-natural (Operations→Finance→Commerce), C-50 + C-51

**Hypothesis**: Operations (fulfillment) → Finance (payment settlement) → Commerce
(invoicing/AR reporting); B2B distribution fulfillment-to-invoicing pipeline. Commerce
runs last and must cite Operations' boundary artifacts directly — two positions prior in
the Operations → Finance → Commerce sequence — as a required skip-level citation. The
SC-12 entry in the closed-chain paragraph names [A-04] as the governed artifact token and
names the Phase Gate 2 enforcement mechanism including its detectability location. SC-8,
SC-9, SC-11, SC-13 entries carry [A-01] in both governed-token and enforcement-mechanism
slots (C-50). All SC entries carry detectability-location language (C-51). Tabular register.

---

You are tracing data through a B2B distribution fulfillment-to-invoicing pipeline —
warehouse pick-and-pack through payment settlement to AR invoicing to Commerce BI
reporting. Three expert roles run in the sequence **Operations → Finance → Commerce**.
Operations establishes the order fulfillment baseline and vocabulary; Finance settles
payments and posts to the ledger; Commerce generates invoices and AR reports.

Commerce runs last and must cite Operations' boundary artifacts directly — two positions
prior in the Operations → Finance → Commerce sequence — as a required skip-level citation.
A Commerce `Citing:` line naming only Finance's artifacts without Operations' boundary
checks fails SC-12. Phase Gate 2 verifies this by citing SC-12 by number.

The physical pipeline flows: warehouse management system (WMS) → pick-and-pack confirmation
→ shipment tracking service → payment authorization gateway → EFT settlement processor →
AR invoice generation → Commerce BI aggregation layer.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first. Every citation must
use the `[A-xx]` token exactly as spelled here.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Operations | Manual fulfillment-to-invoicing workflow replaced by this pipeline; ≥3 named steps with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, order-close SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Operations | Operations | WMS order → pick-and-pack confirmation → shipment tracking service → payment authorization gateway; stage tables per SC-7 |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01]; required skip-level target for Commerce (SC-12) |
| [A-05] | PHASE GATE 1 | Operations | Self-verification checklist; all items ✓ before Finance begins |
| [A-06] | STAGE TRACE — Finance | Finance | Payment authorization → EFT settlement processor → AR ledger posting; stage tables per SC-7 |
| [A-07] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends Elapsed (cumul.) from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Finance | Self-verification checklist; all items ✓ before Commerce begins; item [SC-12] verifies Commerce skip-level citation |
| [A-09] | STAGE TRACE — Commerce | Commerce | AR ledger entry → invoice generation → Commerce BI aggregation; stage tables per SC-7 |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends Elapsed (cumul.) from [A-07]; Incumbent Equiv. cells cite [A-01] |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point and no-handling annotation; formula: `Fall back to [A-01] if [condition]`; SC-13 applies |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions; SC-13 applies |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell form)
and C-35 (INCUMBENT TOTAL section format).**

**Exhaustive closed verification chain** — every SC listed with its governed artifact
tokens, enforcement mechanism, and violation detectability location:

**SC-1 CITATION OPENER** governs [A-06], [A-09] (all non-first role outputs); enforced by
token-match at each role's opening `Citing:` line — a role block that omits the `Citing:`
line or uses prose-only back-references fails, and the violation is detectable from the
role-opener line without reading the role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] (stage tables) and
[A-04], [A-07], [A-10] (boundary tables); enforced by an inline lock at every stage
advance — Stage N+1 blocked until the preceding boundary table is fully populated; the
gate fires as a per-transition callback detectable at the stage-boundary position.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (`Elapsed (cumul.)` column);
enforced by Part A column requirement — a missing column or zero-reset value fails, and
the violation is detectable at the column-header and cell-value level without reading row
prose.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (`Verdict` column); enforced by
Part A string requirement — any value other than exactly `FRESH` or exactly `STALE` fails,
and the violation is detectable at the cell-value level without reading surrounding prose.

**SC-5 STALENESS IMMUTABILITY** governs [A-02] (DOMAIN CONTEXT); enforced by verbatim
phrase requirement — absence of the exact phrase "This threshold is fixed. No subsequent
role may revise it after Stage 1 is written." fails, and the violation is detectable by
phrase-match scan within [A-02]'s body without searching other sections.

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08] (phase gates); enforced by a
gating callback at every role transition — an unchecked item blocks the next role block,
and the violation is detectable at the role-boundary line before reading any role content.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09] (`Stage Latency` column);
enforced by Part A column requirement — a stage table missing the `Stage Latency` column
fails, and the violation is detectable at the table-header row without reading row
contents.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] (TRADE-OFF ANALYSIS) requiring
[A-01] as a mandatory citation token inside [A-14]; enforced by a three-token check —
`[A-01]`, `[A-02]`, and `[A-13]` must all appear in [A-14]; absence of [A-01] is a
protocol violation detectable from [A-14]'s citation token list without prose
interpretation.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] (`Incumbent Equiv.`
column) requiring [A-01] as a mandatory token in every cell; enforced by Part A cell-form
requirement — a cell lacking the `[A-01]` token is a protocol violation detectable at the
cell level without reading surrounding prose.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] (INCUMBENT TOTAL); enforced by
Part B ordering requirement — [A-13] must appear immediately before [A-14] and carry a
Grand Total row; the violation is detectable by artifact-order check at the [A-14] header
position without reading cell values.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] (INCUMBENT BASELINE) as the required
first-produced artifact; enforced by a positional lock — [A-01] must appear before any
stage trace or boundary block; a violation is detectable from the artifact-order check at
the output head without reading artifact content.

**SC-12 SKIP-LEVEL CITATION IN COMMERCE** governs [A-04] (Operations' boundary checks) via
Commerce's `Citing:` line; enforced by the Phase Gate 2 checklist item citing [SC-12] by
number — absence of `[A-04]` in Commerce's `Citing:` line is a protocol violation
detectable by token-match at the Commerce role-opener line without reading the role body.
Commerce occupies position 3; Operations occupies position 1; the position distance is two.

**SC-13 BASELINE CLOSURE** governs [A-12] (RECOVERY PRESCRIPTIONS) and [A-14] (TRADE-OFF
ANALYSIS) requiring [A-01] as a citation token in both; enforced by inline callbacks at
both [A-12] and [A-14] section headers that verify the [A-01] token — a section header
lacking [A-01] is a protocol violation detectable from the header line alone.

Together, SC-1 through SC-13 form a complete closed verification chain.

**Part A — Field compliance markers (boundary block columns):**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric cumulative sum of all prior latencies, in minutes | Partial sum; reset to zero |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE` | Any other value |
| Error handling | `Error Handling` | Named mechanism, or exactly `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level changes, or exactly `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` | Bare duration; token omitted |
| Stage latency | `Stage Latency` | Explicit value, range, or characterization | Inferred from elapsed only |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Table with roles Operations, Finance, Commerce, Grand Total; all subtotals numeric | Prose-only; missing role row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | Tokens [A-01], [A-02], [A-13] all present; ≥1 alternative; ≥2 dimensions | Any token absent |

---

### BOUNDARY BLOCK SCHEMA

Every boundary block: markdown table with columns in order:

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

Column headers must match Part A exactly.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Operations opens with
`Citing: [A-xx], [A-yy], ...` listing prior tokens. [A-01] required in every non-first
role's Citing line. [Apply SC-1 at every non-first role opener.]

**SC-2 — Stage-write progression gate**: Stage N+1 only after preceding boundary table is
fully populated per BOUNDARY BLOCK SCHEMA. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` accumulates across all prior stage and
boundary latencies. Never reset within the run. [Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` vs [A-02] threshold. Cite
[A-02] by token. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Operations appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written." SLA as integer with unit.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] required; all items ✓ before next
role. [Apply SC-6 before every role transition.]

**SC-7 — Stage table format**: `Stage Latency | Schema In | Schema Out | Data Loss Flag`
in every stage block. [Apply SC-7 at every stage.]

**SC-8 — Trade-off as required section**: [A-14] required; [A-01], [A-02], [A-13] tokens
required; ≥1 alternative; ≥2 dimensions. [Apply SC-8 at [A-14].]

**SC-9 — Incumbent Equiv. cell form**: Form `[A-01]: [named step + duration]` required.
[Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [A-13] immediately before [A-14]. Additive
role breakdown. Grand Total row required. [Apply SC-10 before [A-14].]

**SC-11 — Baseline-first production**: [A-01] is first artifact. No stage trace or
boundary block before [A-01] is complete.

**SC-12 — Skip-level citation in Commerce**: Commerce's `Citing:` line must include
`[A-04]` — Operations' boundary checks, two positions prior in the
Operations → Finance → Commerce sequence. Finance is Commerce's immediate predecessor;
naming only Finance's tokens without `[A-04]` fails SC-12. Position distance is two:
Commerce = position 3, Operations = position 1. A Phase Gate 2 verification item must
cite [SC-12] by its numbered identifier.

**SC-13 — BASELINE CLOSURE**: [A-01] must appear as a citation token in [A-12] (formula:
`Fall back to [A-01] if [condition]`) and in [A-14] (alongside [A-02] and [A-13]).
[Apply SC-13 at [A-12] and [A-14].]

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required. Incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST. Describe the manual fulfillment-to-invoicing
workflow this pipeline replaces. Include ≥3 named steps with durations (e.g., "Warehouse
supervisor prints pick list from ERP and coordinates manual pack verification: 45 min",
"Shipping coordinator manually enters tracking details into freight portal and AR system:
30 min", "Finance analyst matches shipment confirmation to PO and keyed payment entry:
60 min"). Use entity names that will reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Entity vocabulary (reuse ≥2 names from [A-01]): WMS pick
record, shipment confirmation, payment authorization record, EFT settlement record, AR
ledger entry, invoice record, BI fulfillment summary. Downstream consumer and business
cadence. Order-close SLA: integer with unit, derived from [A-01] total duration plus
pipeline headroom. Per SC-5 verbatim append required.

**[A-03] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 1: WMS order → Pick-and-pack confirmation service
- Stage 2: Pack confirmation → Shipment tracking service
- Stage 3: Shipment confirmation → Payment authorization gateway

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3, SC-4, SC-9 apply.]

**[A-05] PHASE GATE 1** — Tick before Finance begins:
- [ ] [A-01] produced first; no trace or boundary block precedes it (SC-11)
- [ ] [A-01] ≥3 named steps with durations
- [ ] [A-02] SLA as integer with unit; SC-5 verbatim present
- [ ] Every stage in [A-03] has four columns per SC-7
- [ ] Every block in [A-04] has seven columns matching Part A headers
- [ ] Elapsed (cumul.) accumulates correctly (SC-3)
- [ ] Verdict FRESH or STALE (SC-4)
- [ ] Incumbent Equiv. cell form: `[A-01]: [step + duration]` (SC-9)

Finance may not begin until all ✓. [SC-6]

---

### ROLE 2 — Finance

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 4: Payment authorization → EFT settlement processor
- Stage 5: EFT settlement → AR ledger posting

**[A-07] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend from [A-04].] [SC-4.] [SC-9.]

**[A-08] PHASE GATE 2** — Tick before Commerce begins:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] has four columns per SC-7
- [ ] Every block in [A-07] has seven columns matching Part A headers
- [ ] Elapsed (cumul.) extends [A-04] final value; not reset (SC-3)
- [ ] Verdict FRESH or STALE from [A-02] threshold (SC-4)
- [ ] Incumbent Equiv. cell: `[A-01]: [step + duration]` (SC-9)
- [ ] [SC-12]: Commerce's `Citing:` line must include `[A-04]` — Operations' boundary
  checks, two positions prior. Position distance is two: Commerce = pos 3,
  Operations = pos 1. Mark ✗ if [A-04] absent.

Commerce may not begin until all ✓. [SC-6]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12 — Operations' boundary checks, two positions prior in the
Operations → Finance → Commerce sequence. Position distance is two.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 6: AR ledger entry → Invoice generation service
- Stage 7: Invoice record → Commerce BI aggregation layer

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend from [A-07].] [SC-4.] [SC-9.]

**[A-11] STALE ANALYSIS** — Final Elapsed (cumul.) from [A-10] vs [A-02] threshold.
Normal-operation and failure-mode rows. Cite [A-02] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Formula:
`Fall back to [A-01] if [specific failure condition]`. Every no-handling flag and
Data Loss Flag YES gets a named recovery citing [A-01].

**[A-13] INCUMBENT TOTAL** — [Per Part B. Per SC-10.] Immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Operations | | |
| Finance | | |
| Commerce | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] [Per Part B. Per SC-8.]
Tokens [A-01], [A-02], [A-13] required. ≥1 alternative pattern. ≥2 dimensions.

---

---

## V-03

**Axis**: Output format — prose register, SC-14 FORMAT MODE DECLARATION active (C-50 + C-51)

**Hypothesis**: Finance → Operations → Commerce; SaaS subscription renewal/churn reporting
pipeline. Prose (non-tabular) register. SC-14 FORMAT MODE DECLARATION is active and
appears as a named navigation entry in the closed-chain paragraph (C-47), naming its
governed artifact token ([A-15]) and enforcement mechanism with detectability location
(C-51). SC-8, SC-9, SC-11, SC-13 carry [A-01] in both governed-token and enforcement
slots (C-50). All SC entries carry detectability-location language (C-51). A criterion
substitution map in REGISTER DECLARATION Part C specifies which pass conditions apply
under prose register. Commerce (pos 3) cites Finance [A-04] skip-level per SC-12.

---

You are tracing data through a SaaS subscription renewal-and-churn reporting pipeline —
subscription event stream through renewal processing to churn attribution to Commerce
MRR/ARR dashboard. Three expert roles run in the sequence **Finance → Operations →
Commerce**. Finance establishes the MRR-close SLA and the manual renewal tracking baseline.
Operations processes renewal and cancellation events. Commerce produces MRR and churn
reports.

Commerce runs last and must cite Finance's boundary artifacts directly — two positions
prior in the Finance → Operations → Commerce sequence — as a required skip-level citation.
A Commerce `Citing:` line naming only Operations' artifacts without Finance's boundary
checks fails SC-12. Phase Gate 2 verifies this by citing SC-12 by number.

This output uses the **prose register**: all stage blocks and boundary sections are written
as structured prose paragraphs rather than markdown tables. SC-14 FORMAT MODE DECLARATION
is active. The REGISTER DECLARATION Part C criterion substitution map governs which pass
conditions apply.

The physical pipeline flows: subscription event webhook → event normalization service →
renewal decision engine → dunning/retry service → churn attribution service → MRR
aggregation → ARR forecasting model → Commerce dashboard.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first. Every citation must
use the `[A-xx]` token exactly as spelled here.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Finance | Manual subscription renewal tracking workflow replaced by this pipeline; ≥3 named steps with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Finance | Entity vocabulary, MRR-close SLA (immutable after Stage 1), downstream consumer, cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Finance | Finance | Webhook → event normalization → renewal decision engine → dunning service; prose stage blocks per SC-7 |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | Prose boundary sections per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. entries cite [A-01]; required skip-level target for Commerce (SC-12) |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all items ✓ before Operations begins |
| [A-06] | STAGE TRACE — Operations | Operations | Dunning service → churn attribution service → MRR aggregation; prose stage blocks per SC-7 |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | Prose boundary sections; extends Elapsed (cumul.) from [A-04]; Incumbent Equiv. entries cite [A-01] |
| [A-08] | PHASE GATE 2 | Operations | Self-verification checklist; all items ✓ before Commerce begins; item [SC-12] verifies Commerce skip-level citation |
| [A-09] | STAGE TRACE — Commerce | Commerce | MRR aggregation → ARR forecasting model → Commerce dashboard; prose stage blocks per SC-7 |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | Prose boundary sections; extends Elapsed (cumul.) from [A-07]; Incumbent Equiv. entries cite [A-01] |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold; prose format |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point and no-handling annotation; formula: `Fall back to [A-01] if [condition]`; SC-13 applies |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions; SC-13 applies |
| [A-15] | FORMAT MODE DECLARATION | Finance | Prose register active: names criterion substitution map, governed artifact tokens, and detectability location of format-mode violations; produced immediately before [A-03] |

---

### REGISTER DECLARATION

This output uses the **prose register**. All stage blocks and boundary sections are
written as structured prose paragraphs. Markdown tables are not used for stage or boundary
content. [A-13] INCUMBENT TOTAL is the only tabular output permitted, as it is a
structured summary, not a trace artifact.

**This section is the sole authoritative reference for C-34 (Incumbent Equiv. entry form)
and C-35 (INCUMBENT TOTAL section format). An evaluator may determine pass/fail for both
by reading this section alone.**

**Exhaustive closed verification chain** — every SC and SC-14 listed with its governed
artifact tokens, enforcement mechanism, and violation detectability location:

**SC-1 CITATION OPENER** governs [A-06], [A-09] (all non-first role outputs); enforced by
token-match at each role's opening `Citing:` line — a missing or prose-only opener fails,
and the violation is detectable from the role-opener line without reading the role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] (stage blocks) and
[A-04], [A-07], [A-10] (boundary sections); enforced by an inline lock — Stage N+1 blocked
until the preceding boundary section is fully written; the gate fires as a per-transition
callback detectable at the stage-transition sentence without inspecting stage content.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (boundary sections, Elapsed
(cumul.) sentence); enforced by Part A sentence-form requirement — a boundary section
missing the cumulative elapsed sentence or resetting to zero fails, and the violation is
detectable at the Elapsed (cumul.) sentence within the boundary section without reading
surrounding prose.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (boundary sections, Verdict
sentence); enforced by Part A string requirement — any verdict other than exactly `FRESH`
or exactly `STALE` fails, and the violation is detectable at the Verdict sentence level
without reading surrounding prose.

**SC-5 STALENESS IMMUTABILITY** governs [A-02] (DOMAIN CONTEXT); enforced by verbatim
phrase requirement — absence of the exact phrase "This threshold is fixed. No subsequent
role may revise it after Stage 1 is written." fails, and the violation is detectable by
phrase-match scan within [A-02]'s body without searching other sections.

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08] (phase gates); enforced by a
gating callback at every role transition — an unchecked item blocks the next role section,
and the violation is detectable at the role-boundary line before reading any role content.

**SC-7 STAGE BLOCK FORMAT** governs [A-03], [A-06], [A-09] (stage blocks); enforced by
Part C prose-mode requirement — each stage block must open with a labeled latency sentence
and a schema-state sentence; a stage block missing either opening sentence fails, and the
violation is detectable from the stage block's first two sentences without reading further.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] (TRADE-OFF ANALYSIS) requiring
[A-01] as a mandatory citation token inside [A-14]; enforced by a three-token check —
`[A-01]`, `[A-02]`, and `[A-13]` must all appear in [A-14]; absence of [A-01] is a
protocol violation detectable from [A-14]'s opening citation paragraph without reading
trade-off prose.

**SC-9 INCUMBENT EQUIV. ENTRY FORM** governs [A-04], [A-07], [A-10] (boundary sections,
Incumbent Equiv. sentence) requiring [A-01] as a mandatory token in every entry; enforced
by Part C sentence-form requirement — an entry lacking the `[A-01]` token is a protocol
violation detectable from the Incumbent Equiv. sentence without reading surrounding prose.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] (INCUMBENT TOTAL); enforced by
Part B ordering requirement — [A-13] must appear immediately before [A-14] and carry a
Grand Total row; the violation is detectable by artifact-order check at the [A-14] section
header without reading cell values.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] (INCUMBENT BASELINE) as the required
first-produced artifact; enforced by a positional lock — [A-01] must appear before any
stage block or boundary section; a violation is detectable from the artifact-order check at
the output head without reading artifact content.

**SC-12 SKIP-LEVEL CITATION IN COMMERCE** governs [A-04] (Finance's boundary checks) via
Commerce's `Citing:` line; enforced by the Phase Gate 2 checklist item citing [SC-12] by
number — absence of `[A-04]` in Commerce's `Citing:` line is a protocol violation
detectable by token-match at the Commerce role-opener line without reading the role body.
Commerce occupies position 3; Finance occupies position 1; the position distance is two.

**SC-13 BASELINE CLOSURE** governs [A-12] (RECOVERY PRESCRIPTIONS) and [A-14] (TRADE-OFF
ANALYSIS) requiring [A-01] as a citation token in both; enforced by inline callbacks at
both [A-12] and [A-14] section headers — a section header lacking the [A-01] token is a
protocol violation detectable from the header line alone.

**SC-14 FORMAT MODE DECLARATION** governs [A-15] (FORMAT MODE DECLARATION artifact) and
[A-03], [A-06], [A-09], [A-04], [A-07], [A-10] (prose-mode stage and boundary outputs);
enforced by [A-15] criterion substitution map, which must appear before [A-03] — the
substitution map's presence or absence is detectable from the artifact-order check at the
[A-03] section header without reading stage content.

Together, SC-1 through SC-14 form a complete closed verification chain.

**Part A — Sentence-form compliance markers (boundary sections):**

| Required Element | Sentence Label | Required Sentence Form | Disqualifying Form |
|-----------------|----------------|------------------------|--------------------|
| Domain entity | `Entity:` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.):` | Numeric sum of all prior stage and boundary latencies, in minutes | Partial sum; reset to zero |
| Freshness verdict | `Verdict:` | Exactly `FRESH` or exactly `STALE`, derived from [A-02] threshold | Any other value |
| Error handling | `Error Handling:` | Named mechanism, or exactly `no handling — see [A-12]` | Silence; omitted label |
| Schema change | `Schema Delta:` | Named field-level changes, or exactly `NONE` | Omitted label |
| Data loss | `Data Loss Flag:` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.:` | `[A-01]: [named manual step + duration]` | Bare duration; token omitted |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Table: `Role \| Incumbent Equiv. subtotal \| Steps cited`; Finance, Operations, Commerce, Grand Total rows | Prose-only; missing role row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | All three tokens [A-01], [A-02], [A-13] present; ≥1 alternative; ≥2 dimensions | Any token absent |

**Part C — Prose-mode criterion substitution map:**

The following criteria apply with substituted pass conditions under prose register:

| Criterion | Tabular Pass Condition | Prose-Mode Pass Condition |
|-----------|----------------------|--------------------------|
| C-04 (schema state) | Schema column in table | Schema-state sentence in each stage block opening |
| C-05 (latency) | `Stage Latency` column | Labeled latency sentence opening each stage block |
| C-11 (boundary gates) | 7-column markdown table | Prose section with all 7 labeled sentences per Part A |
| C-28 (named-column schema) | Column-header match | Label-string match per Part A |

A stage block lacking the labeled latency sentence or the schema-state sentence in its
first two sentences fails C-04 and C-05 under prose-mode substitution, detectable from
the stage block's opening without reading the remainder.

---

### BOUNDARY BLOCK SCHEMA

Every boundary section must be a prose paragraph with these seven labeled sentences, in
this order:

`Entity: ... | Elapsed (cumul.): ... | Verdict: ... | Error Handling: ... | Schema Delta: ... | Data Loss Flag: ... | Incumbent Equiv.: ...`

Label strings must match Part A spellings exactly. A missing or mislabeled sentence fails
the schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Finance opens with
`Citing: [A-xx], ...` listing every token from prior roles. [A-01] required in every
non-first role's Citing line. [Apply SC-1 at every non-first role opener.]

**SC-2 — Stage-write progression gate**: Stage N+1 only after preceding boundary section
is fully written per BOUNDARY BLOCK SCHEMA. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` accumulates from all prior stage and
boundary latencies. Never reset. [Apply SC-3 at every boundary section.]

**SC-4 — Binary verdict**: `Verdict:` = `FRESH` or `STALE`, derived vs [A-02] threshold.
Cite [A-02] by token. [Apply SC-4 at every boundary section.]

**SC-5 — Immutability**: Finance appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written." SLA as integer with unit.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] required; all items ✓ before next
role. [Apply SC-6 before every role transition.]

**SC-7 — Stage block format**: Each stage block opens with a labeled latency sentence
(e.g., "Stage latency: 3 min.") and a schema-state sentence. [Apply SC-7 at every stage.]

**SC-8 — Trade-off as required section**: [A-14] required; [A-01], [A-02], [A-13]
required; ≥1 alternative; ≥2 dimensions. [Apply SC-8 at [A-14].]

**SC-9 — Incumbent Equiv. entry form**: Form `[A-01]: [named step + duration]` required in
the `Incumbent Equiv.:` sentence. [Apply SC-9 at every boundary section.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [A-13] immediately before [A-14]. Additive
role breakdown. Grand Total row. [Apply SC-10 before [A-14].]

**SC-11 — Baseline-first production**: [A-01] is first artifact. No stage block or
boundary section before [A-01] is complete.

**SC-12 — Skip-level citation in Commerce**: Commerce's `Citing:` line must include
`[A-04]`. Position distance is two: Commerce = pos 3, Finance = pos 1. Phase Gate 2 item
must cite [SC-12] by numbered identifier. [Apply SC-12 at Commerce's Citing line.]

**SC-13 — BASELINE CLOSURE**: [A-01] in [A-12] (formula: `Fall back to [A-01] if
[condition]`) and in [A-14]. [Apply SC-13 at [A-12] and [A-14].]

**SC-14 — FORMAT MODE DECLARATION**: Produce [A-15] before [A-03]. [A-15] must name:
(a) the active register (prose); (b) the criterion substitution map (Part C reference);
(c) the governed artifacts. [Apply SC-14 before Stage 1.]

---

### ROLE 1 — Finance

[Finance runs first. No Citing line. Incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST. Describe the manual subscription renewal
tracking workflow this pipeline replaces. Include ≥3 named steps with durations (e.g.,
"Customer success rep manually exports renewal cohort from CRM and checks payment status
in billing portal: 40 min", "Finance analyst keys renewal or cancellation status into
revenue spreadsheet and flags churn for attribution: 30 min", "MRR report owner
consolidates outlet totals from spreadsheet tabs into monthly ARR model: 50 min"). Use
entity names that will reappear in [A-02].

**[A-15] FORMAT MODE DECLARATION** — Produce immediately after [A-01] and before [A-03].
State: (a) this output uses the prose register; (b) REGISTER DECLARATION Part C is the
criterion substitution map; (c) governed artifacts include [A-03], [A-04], [A-06], [A-07],
[A-09], [A-10]. Include the following statement verbatim: "Format-mode violations in prose
stage blocks are detectable from the stage block's first two sentences without reading
further."

**[A-02] DOMAIN CONTEXT** — Entity vocabulary (reuse ≥2 names from [A-01]): subscription
event, renewal decision record, dunning attempt, churn attribution record, MRR aggregation
entry, ARR forecast record. Downstream consumer and business cadence (e.g., monthly MRR
close on last day of month). MRR-close SLA: integer with unit, derived from [A-01] total
duration. Per SC-5 verbatim append required.

**[A-03] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Prose stage blocks.
- Stage 1: Subscription event webhook → Event normalization service
- Stage 2: Normalized event → Renewal decision engine
- Stage 3: Renewal decision → Dunning/retry service

**[A-04] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA. Prose sections.
[SC-3, SC-4, SC-9 apply.]

**[A-05] PHASE GATE 1** — Tick before Operations begins:
- [ ] [A-01] produced first; no stage block or boundary section precedes it (SC-11)
- [ ] [A-01] ≥3 named steps with durations
- [ ] [A-15] produced before [A-03]; contains active register, Part C reference, governed
  artifacts, verbatim detectability statement (SC-14)
- [ ] [A-02] SLA as integer with unit; SC-5 verbatim present
- [ ] Every stage in [A-03] opens with labeled latency and schema-state sentences (SC-7)
- [ ] Every section in [A-04] has seven labeled sentences per Part A (SC-3, SC-4, SC-9)

Operations may not begin until all ✓. [SC-6]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Per SC-7. Per SC-2. Prose stage blocks.
- Stage 4: Churn attribution service → MRR aggregation service
- Stage 5: MRR aggregation entry → ARR forecasting model

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA. Prose sections.
[SC-3: Elapsed (cumul.) extends [A-04] final value.] [SC-4.] [SC-9.]

**[A-08] PHASE GATE 2** — Tick before Commerce begins:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] opens with labeled latency and schema-state sentences (SC-7)
- [ ] Every section in [A-07] has seven labeled sentences; Elapsed extends [A-04] (SC-3)
- [ ] Verdict FRESH or STALE from [A-02] threshold (SC-4)
- [ ] Incumbent Equiv. sentence: `[A-01]: [step + duration]` (SC-9)
- [ ] [SC-12]: Commerce's `Citing:` line must include `[A-04]` — Finance's boundary
  checks, two positions prior. Position distance is two: Commerce = pos 3, Finance = pos 1.
  Mark ✗ if [A-04] absent.

Commerce may not begin until all ✓. [SC-6]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12 — Finance's boundary checks, two positions prior. Position
distance is two.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. Prose stage blocks.
- Stage 6: ARR forecasting model → Commerce MRR dashboard
- Stage 7: MRR dashboard → Executive ARR summary view

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend from [A-07].] [SC-4.] [SC-9.]

**[A-11] STALE ANALYSIS** — Final Elapsed (cumul.) from [A-10] vs [A-02] threshold. Write
as prose with normal-operation and failure-mode paragraphs. Cite [A-02] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] For every no-handling label
and Data Loss Flag YES, provide named recovery in prose. Formula:
`Fall back to [A-01] if [specific failure condition]`.

**[A-13] INCUMBENT TOTAL** — [Per Part B. Per SC-10.] Produce as table immediately before
[A-14] (tabular format permitted for this structured summary artifact):

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Finance | | |
| Operations | | |
| Commerce | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] [Per Part B. Per SC-8.]
Tokens [A-01], [A-02], [A-13] required. ≥1 alternative pattern. ≥2 dimensions.

---

---

## V-04

**Axis**: Inertia framing — maximum incumbent baseline prominence (C-50 + C-51)

**Hypothesis**: Finance → Operations → Commerce; retail loyalty-points-to-liability-ledger
pipeline. [A-01] requires ≥5 named manual steps with per-step durations (stronger than
standard ≥3), producing a richer baseline that amplifies the [A-01] signal across all
four dual-slot SCs. SC-8, SC-9, SC-11, SC-13 closed-chain entries are maximally explicit
about [A-01] dual-slot anchoring: SC-8 names [A-01] in both the governed-token declaration
("requiring [A-01] as a mandatory citation token") and the enforcement clause. SC-9 names
[A-01] in both the cell-form requirement and the detectability sentence. SC-11 names [A-01]
in both the positional lock specification and the violation description. SC-13 names [A-01]
in both the governed-artifact list and the header-callback enforcement. Commerce (pos 3)
cites Finance [A-04] (pos 1) skip-level per SC-12. Tabular register.

---

You are tracing data through a retail loyalty-points-to-liability-ledger pipeline — POS
points issuance through redemption processing to deferred revenue liability posting to
Commerce BI. Three expert roles run in the sequence **Finance → Operations → Commerce**.
Finance establishes the liability-close SLA and a detailed manual points-tracking baseline
with ≥5 named manual steps. Operations processes points transactions and redemptions.
Commerce aggregates liability data for executive reporting.

Commerce runs last and must cite Finance's boundary artifacts directly — two positions prior
in the Finance → Operations → Commerce sequence — as a required skip-level citation. A
Commerce `Citing:` line naming only Operations' artifacts without Finance's boundary checks
fails SC-12. Phase Gate 2 verifies this by citing SC-12 by number.

The physical pipeline flows: POS loyalty API → points issuance service → points ledger →
redemption validation engine → deferred revenue calculation → liability posting service →
Commerce BI aggregation.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first. Every citation must
use the `[A-xx]` token exactly as spelled here.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Finance | Manual loyalty-points tracking and liability-posting workflow; **≥5 named steps with per-step durations**; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Finance | Entity vocabulary, liability-close SLA (immutable after Stage 1), downstream consumer, cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Finance | Finance | POS loyalty API → points issuance → points ledger → redemption validation; stage tables per SC-7 |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01]; required skip-level target for Commerce (SC-12) |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all items ✓ before Operations begins |
| [A-06] | STAGE TRACE — Operations | Operations | Redemption validation → deferred revenue calculation → liability posting service; stage tables per SC-7 |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends Elapsed (cumul.) from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Operations | Self-verification checklist; all items ✓ before Commerce begins; item [SC-12] verifies Commerce skip-level citation |
| [A-09] | STAGE TRACE — Commerce | Commerce | Liability posting → Commerce BI aggregation → deferred revenue dashboard; stage tables per SC-7 |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends Elapsed (cumul.) from [A-07]; Incumbent Equiv. cells cite [A-01] |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point and no-handling annotation; formula: `Fall back to [A-01] if [condition]`; SC-13 applies |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions; SC-13 applies |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell form)
and C-35 (INCUMBENT TOTAL section format).**

**Exhaustive closed verification chain** — every SC listed with its governed artifact
tokens, enforcement mechanism, and violation detectability location:

**SC-1 CITATION OPENER** governs [A-06], [A-09]; enforced by token-match at each role's
opening `Citing:` line — a missing or prose-only opener fails, detectable from the
role-opener line without reading the role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] and [A-04], [A-07],
[A-10]; enforced by inline lock at every stage advance — Stage N+1 blocked until preceding
boundary table is fully populated; the gate fires as a per-transition callback detectable
at the stage-boundary position.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (`Elapsed (cumul.)` column);
enforced by Part A column requirement — missing column or zero-reset fails, detectable at
the column-header and cell-value level without reading row prose.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (`Verdict` column); enforced by
Part A string requirement — any non-`FRESH`/non-`STALE` value fails, detectable at the
cell-value level without reading surrounding prose.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; enforced by verbatim phrase requirement —
absence of the exact phrase fails, detectable by phrase-match scan within [A-02]'s body
without searching other sections.

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08]; enforced by gating callback —
unchecked item blocks next role, detectable at the role-boundary line before reading
role content.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09] (`Stage Latency` column);
enforced by Part A column requirement — missing `Stage Latency` column fails, detectable
at the table-header row without reading row contents.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] (TRADE-OFF ANALYSIS) requiring
[A-01] as a mandatory citation token inside [A-14] alongside [A-02] and [A-13]; enforced
by a three-token check — `[A-01]` must appear in [A-14] as one of the three required
citation tokens; absence of [A-01] is a protocol violation detectable from [A-14]'s
citation token list without prose interpretation.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] (`Incumbent Equiv.`
column) requiring [A-01] as a mandatory token in every Incumbent Equiv. cell; enforced by
Part A cell-form requirement — every cell must contain the `[A-01]` token in the form
`[A-01]: [named manual step + duration]`; a cell where [A-01] is absent is a protocol
violation detectable at the cell level without reading surrounding prose.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13]; enforced by Part B ordering
requirement — [A-13] must appear immediately before [A-14] with a Grand Total row;
violation detectable by artifact-order check at the [A-14] header position.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] (INCUMBENT BASELINE) as the required
first-produced artifact, mandating ≥5 named manual steps with per-step durations; enforced
by a positional lock — [A-01] must appear before any stage trace or boundary block, and
must contain ≥5 named steps; a violation where any output precedes [A-01] or where [A-01]
contains fewer than 5 named steps is detectable from the artifact-order check and the
step-count at the output head without reading artifact prose.

**SC-12 SKIP-LEVEL CITATION IN COMMERCE** governs [A-04] (Finance's boundary checks) via
Commerce's `Citing:` line; enforced by the Phase Gate 2 checklist item citing [SC-12] by
number — absence of `[A-04]` in Commerce's `Citing:` line is detectable by token-match at
the Commerce role-opener line without reading the role body. Commerce occupies position 3;
Finance occupies position 1; position distance is two.

**SC-13 BASELINE CLOSURE** governs [A-12] (RECOVERY PRESCRIPTIONS) and [A-14] (TRADE-OFF
ANALYSIS) requiring [A-01] as a citation token in both [A-12] and [A-14]; enforced by
inline callbacks at both [A-12] and [A-14] section headers — a section header where the
[A-01] token is absent is a protocol violation detectable from the header line alone.

Together, SC-1 through SC-13 form a complete closed verification chain.

**Part A — Field compliance markers (boundary block columns):**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum of all prior stage and boundary latencies, in minutes | Partial sum; reset to zero |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE` | Any other value |
| Error handling | `Error Handling` | Named mechanism, or exactly `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level changes, or exactly `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` | Bare duration; [A-01] token omitted |
| Stage latency | `Stage Latency` | Explicit value, range, or characterization | Inferred from elapsed only |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Table: `Role \| Incumbent Equiv. subtotal \| Steps cited`; Finance, Operations, Commerce, Grand Total rows | Prose-only; missing row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | Tokens [A-01], [A-02], [A-13] present; ≥1 alternative; ≥2 dimensions | Any token absent |

---

### BOUNDARY BLOCK SCHEMA

Every boundary block: markdown table with columns in order:

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

Column headers must match Part A exactly.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every non-Finance role opens with `Citing: [A-xx], ...` listing
prior tokens. [A-01] required. [Apply SC-1 at every non-first role opener.]

**SC-2 — Stage-write progression gate**: Stage N+1 only after preceding boundary table is
complete per BOUNDARY BLOCK SCHEMA. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` accumulates continuously. Never reset.
[Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` vs [A-02] threshold. Cite
[A-02] by token. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Finance appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written." SLA as integer with unit.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] required; all items ✓ before next
role. [Apply SC-6 before every role transition.]

**SC-7 — Stage table format**: `Stage Latency | Schema In | Schema Out | Data Loss Flag`.
[Apply SC-7 at every stage.]

**SC-8 — Trade-off as required section**: [A-14] required; [A-01], [A-02], [A-13]
required; ≥1 alternative; ≥2 dimensions. [Apply SC-8 at [A-14].]

**SC-9 — Incumbent Equiv. cell form**: `[A-01]: [named step + duration]`. [A-01] token
required. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [A-13] immediately before [A-14]. Additive
breakdown. Grand Total row. [Apply SC-10 before [A-14].]

**SC-11 — Baseline-first production**: [A-01] is first artifact and must contain ≥5 named
manual steps with per-step durations. No stage trace or boundary block before [A-01].

**SC-12 — Skip-level citation in Commerce**: Commerce's `Citing:` line must include
`[A-04]`. Position distance is two: Commerce = pos 3, Finance = pos 1. Phase Gate 2 item
must cite [SC-12] by identifier. [Apply SC-12 at Commerce's Citing line.]

**SC-13 — BASELINE CLOSURE**: [A-01] in [A-12] (formula: `Fall back to [A-01] if
[condition]`) and in [A-14]. [Apply SC-13 at [A-12] and [A-14].]

---

### ROLE 1 — Finance

[Finance runs first. No Citing line. Incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST. **This artifact requires ≥5 named manual
steps with per-step durations.** Describe the manual loyalty-points tracking and liability-
posting workflow this pipeline replaces. Include ≥5 named steps such as:
- "Loyalty program coordinator exports daily POS transaction report and manually assigns
  points per tier rule in spreadsheet: 60 min"
- "Finance analyst cross-references points issuance spreadsheet against POS system totals
  for discrepancy detection: 45 min"
- "Points ledger owner updates cumulative customer balances in master loyalty workbook
  and flags expiring points cohorts: 30 min"
- "Redemption team manually validates redemption requests against available balance in
  workbook and marks approved/rejected: 40 min"
- "Finance analyst calculates deferred revenue liability from approved redemptions and
  posts manual journal entry to GL: 50 min"
Use entity names that will reappear in [A-02]. Total manual duration from these steps
becomes the basis for [A-02]'s liability-close SLA.

**[A-02] DOMAIN CONTEXT** — Entity vocabulary (reuse ≥2 names from [A-01]): POS loyalty
transaction, points issuance record, points ledger entry, redemption request, deferred
revenue liability entry, BI aggregation record. Downstream consumer and business cadence
(e.g., daily liability close at end of business). Liability-close SLA: integer with unit,
derived from [A-01] total manual duration plus pipeline headroom. Per SC-5 verbatim append
required.

**[A-03] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 1: POS loyalty API → Points issuance service
- Stage 2: Points issuance → Points ledger
- Stage 3: Points ledger → Redemption validation engine

**[A-04] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3, SC-4, SC-9 apply. Each Incumbent Equiv. cell cites one of [A-01]'s ≥5 named steps.]

**[A-05] PHASE GATE 1** — Tick before Operations begins:
- [ ] [A-01] produced first; no trace or boundary block precedes it (SC-11)
- [ ] [A-01] contains ≥5 named manual steps with per-step durations (SC-11)
- [ ] [A-02] SLA derived from [A-01] total; SC-5 verbatim present
- [ ] Every stage in [A-03] has four columns per SC-7
- [ ] Every block in [A-04] has seven columns matching Part A headers
- [ ] Elapsed (cumul.) accumulates correctly (SC-3)
- [ ] Verdict FRESH or STALE (SC-4)
- [ ] Incumbent Equiv. cell: `[A-01]: [named step + duration]` from [A-01]'s step list (SC-9)

Operations may not begin until all ✓. [SC-6]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 4: Redemption validation → Deferred revenue calculation
- Stage 5: Deferred revenue entry → Liability posting service

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend from [A-04].] [SC-4.] [SC-9: cite [A-01] named steps.]

**[A-08] PHASE GATE 2** — Tick before Commerce begins:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] has four columns per SC-7
- [ ] Every block in [A-07] has seven columns matching Part A headers
- [ ] Elapsed (cumul.) extends [A-04] final value; not reset (SC-3)
- [ ] Verdict FRESH or STALE from [A-02] threshold (SC-4)
- [ ] Incumbent Equiv. cell: `[A-01]: [named step + duration]` (SC-9)
- [ ] [SC-12]: Commerce's `Citing:` line must include `[A-04]` — Finance's boundary
  checks, two positions prior. Position distance is two: Commerce = pos 3, Finance = pos 1.
  Mark ✗ if [A-04] absent.

Commerce may not begin until all ✓. [SC-6]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12 — Finance's boundary checks, two positions prior. Position
distance is two.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 6: Liability posting → Commerce BI aggregation
- Stage 7: BI aggregation → Deferred revenue dashboard

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend from [A-07].] [SC-4.] [SC-9.]

**[A-11] STALE ANALYSIS** — Final Elapsed (cumul.) from [A-10] vs [A-02] threshold.
Normal-operation and failure-mode rows. Cite [A-02] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] For every no-handling flag
and Data Loss Flag YES, provide a named recovery citing [A-01]. Formula:
`Fall back to [A-01] if [specific failure condition]`. The [A-01] baseline contains ≥5
named steps; recovery formulas may reference specific steps by name.

**[A-13] INCUMBENT TOTAL** — [Per Part B. Per SC-10.] Immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Finance | | |
| Operations | | |
| Commerce | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] [Per Part B. Per SC-8.]
Tokens [A-01], [A-02], [A-13] required. Use [A-13] Grand Total as the numeric comparison
endpoint. Name ≥1 alternative pattern. ≥2 dimensions.

---

---

## V-05

**Axis**: Combined — non-natural role sequence (Operations→Commerce→Finance) + lifecycle
depth (Phase Gate 0 added as pre-trace setup gate); C-50 + C-51

**Hypothesis**: Operations (CDR collection) → Commerce (rating/billing) → Finance (GL
posting); telecom CDR-to-billing-to-GL pipeline. Finance runs last and must cite
Operations' boundary artifacts directly — two positions prior in the
Operations → Commerce → Finance sequence — as a required skip-level citation. Phase Gate 0
is added as a new lifecycle gate: it fires before Role 1 begins and verifies that the
ARTIFACT REGISTRY, REGISTER DECLARATION, BOUNDARY BLOCK SCHEMA, and STRUCTURAL CONSTRAINTS
sections are all present and structurally complete. [A-00] PRE-TRACE SETUP CHECKLIST is
introduced as a new artifact produced before [A-01]. SC-8, SC-9, SC-11, SC-13 carry [A-01]
in both governed-token and enforcement slots (C-50). All SC entries carry detectability-
location language (C-51). Tabular register.

---

You are tracing data through a telecom CDR-to-billing-to-GL pipeline — raw call detail
record (CDR) collection through billing rating to revenue GL posting and Finance BI.
Three expert roles run in the sequence **Operations → Commerce → Finance**. Operations
establishes the billing-cycle SLA and the manual CDR processing baseline. Commerce rates
and invoices. Finance posts settled revenue to the GL.

Finance runs last and must cite Operations' boundary artifacts directly — two positions
prior in the Operations → Commerce → Finance sequence — as a required skip-level citation.
A Finance `Citing:` line naming only Commerce's artifacts without Operations' boundary
checks fails SC-12. Phase Gate 2 verifies this by citing SC-12 by number.

A Phase Gate 0 fires before any role output begins. Operations must produce [A-00]
PRE-TRACE SETUP CHECKLIST as the absolute first artifact, verifying that all structural
sections of this prompt are present before the trace begins.

The physical pipeline flows: CDR mediation layer → CDR normalization service → usage rating
engine → invoice generation service → payment processing gateway → GL posting service →
Finance BI aggregation layer.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-00] is produced first; [A-01] follows
immediately. Every citation must use the `[A-xx]` token exactly as spelled here.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-00] | PRE-TRACE SETUP CHECKLIST | Operations | Phase Gate 0: verifies ARTIFACT REGISTRY, REGISTER DECLARATION, BOUNDARY BLOCK SCHEMA, STRUCTURAL CONSTRAINTS sections are present before any trace output begins; produced BEFORE [A-01]. |
| [A-01] | INCUMBENT BASELINE | Operations | Manual CDR processing and billing workflow replaced by this pipeline; ≥3 named steps with durations; produced immediately after [A-00]. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, billing-cycle SLA (immutable after Stage 1), downstream consumer, cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Operations | Operations | CDR mediation → CDR normalization → usage rating engine → invoice generation; stage tables per SC-7 |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01]; required skip-level target for Finance (SC-12) |
| [A-05] | PHASE GATE 1 | Operations | Self-verification checklist; all items ✓ before Commerce begins |
| [A-06] | STAGE TRACE — Commerce | Commerce | Invoice generation → payment processing gateway → payment confirmation; stage tables per SC-7 |
| [A-07] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends Elapsed (cumul.) from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Commerce | Self-verification checklist; all items ✓ before Finance begins; item [SC-12] verifies Finance skip-level citation |
| [A-09] | STAGE TRACE — Finance | Finance | Payment confirmation → GL posting service → Finance BI aggregation; stage tables per SC-7 |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends Elapsed (cumul.) from [A-07]; Incumbent Equiv. cells cite [A-01] |
| [A-11] | STALE ANALYSIS | Finance | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery per loss point and no-handling annotation; formula: `Fall back to [A-01] if [condition]`; SC-13 applies |
| [A-13] | INCUMBENT TOTAL | Finance | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Finance | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions; SC-13 applies |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell form)
and C-35 (INCUMBENT TOTAL section format).**

**Exhaustive closed verification chain** — every SC listed with its governed artifact
tokens, enforcement mechanism, and violation detectability location:

**SC-0 PRE-TRACE SETUP GATE** governs [A-00] (PRE-TRACE SETUP CHECKLIST) as the absolute
first artifact, preceding [A-01]; enforced by a positional lock — any trace output
appearing before [A-00] is complete is a protocol violation detectable from the
artifact-order check at the output head without reading any content.

**SC-1 CITATION OPENER** governs [A-06], [A-09] (all non-first role outputs); enforced by
token-match at each role's opening `Citing:` line — a missing or prose-only opener fails,
detectable from the role-opener line without reading the role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] and [A-04], [A-07],
[A-10]; enforced by inline lock at every stage advance — Stage N+1 blocked until preceding
boundary table is fully populated; the gate fires as a per-transition callback detectable
at the stage-boundary position.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (`Elapsed (cumul.)` column);
enforced by Part A column requirement — missing column or zero-reset fails, detectable at
the column-header and cell-value level without reading row prose.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (`Verdict` column); enforced by
Part A string requirement — any non-`FRESH`/non-`STALE` value fails, detectable at the
cell-value level without reading surrounding prose.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; enforced by verbatim phrase requirement —
absence of the exact phrase fails, detectable by phrase-match scan within [A-02]'s body
without searching other sections.

**SC-6 PHASE GATE OBLIGATION** governs [A-00], [A-05], and [A-08] (all three phase gates);
enforced by gating callbacks at the pre-trace setup position and at every role transition —
any unchecked gate item or missing phase gate is a violation detectable at the gate
position without reading the subsequent role or trace content.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09] (`Stage Latency` column);
enforced by Part A column requirement — missing `Stage Latency` column fails, detectable
at the table-header row without reading row contents.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] (TRADE-OFF ANALYSIS) requiring
[A-01] as a mandatory citation token inside [A-14]; enforced by a three-token check —
`[A-01]`, `[A-02]`, and `[A-13]` must all appear in [A-14]; absence of [A-01] is a
protocol violation detectable from [A-14]'s citation token list without prose
interpretation.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] (`Incumbent Equiv.`
column) requiring [A-01] as a mandatory token in every cell; enforced by Part A cell-form
requirement — a cell lacking the `[A-01]` token is a protocol violation detectable at the
cell level without reading surrounding prose.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13]; enforced by Part B ordering
requirement — [A-13] must appear immediately before [A-14] with a Grand Total row;
detectable by artifact-order check at the [A-14] header position.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] (INCUMBENT BASELINE) as the required
first trace artifact, produced immediately after [A-00]; enforced by a positional lock —
[A-01] must appear before any stage trace or boundary block; a violation is detectable
from the artifact-order check at the [A-03] section header without reading artifact
content.

**SC-12 SKIP-LEVEL CITATION IN FINANCE** governs [A-04] (Operations' boundary checks) via
Finance's `Citing:` line; enforced by the Phase Gate 2 checklist item citing [SC-12] by
number — absence of `[A-04]` in Finance's `Citing:` line is a protocol violation
detectable by token-match at the Finance role-opener line without reading the role body.
Finance occupies position 3; Operations occupies position 1; the position distance is two.

**SC-13 BASELINE CLOSURE** governs [A-12] (RECOVERY PRESCRIPTIONS) and [A-14] (TRADE-OFF
ANALYSIS) requiring [A-01] as a citation token in both; enforced by inline callbacks at
both [A-12] and [A-14] section headers — a section header lacking the [A-01] token is a
protocol violation detectable from the header line alone.

Together, SC-0 through SC-13 form a complete closed verification chain.

**Part A — Field compliance markers (boundary block columns):**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum of all prior stage and boundary latencies, in minutes | Partial sum; reset to zero |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE` | Any other value |
| Error handling | `Error Handling` | Named mechanism, or exactly `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level changes, or exactly `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` | Bare duration; [A-01] token omitted |
| Stage latency | `Stage Latency` | Explicit value, range, or characterization | Inferred from elapsed only |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Table: `Role \| Incumbent Equiv. subtotal \| Steps cited`; Operations, Commerce, Finance, Grand Total rows | Prose-only; missing row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | Tokens [A-01], [A-02], [A-13] present; ≥1 alternative; ≥2 dimensions | Any token absent |

---

### BOUNDARY BLOCK SCHEMA

Every boundary block: markdown table with columns in order:

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

Column headers must match Part A exactly.

---

### STRUCTURAL CONSTRAINTS

**SC-0 — Pre-trace setup gate**: [A-00] PRE-TRACE SETUP CHECKLIST must be the absolute
first artifact. It must verify, by checklist, that ARTIFACT REGISTRY, REGISTER DECLARATION,
BOUNDARY BLOCK SCHEMA, and STRUCTURAL CONSTRAINTS sections are all present in this prompt.
No role output may begin until [A-00] is complete and all items are ✓.

**SC-1 — Citation opener**: Every role other than Operations opens with
`Citing: [A-xx], ...` listing prior tokens. [A-01] required. [Apply SC-1 at every
non-first role opener.]

**SC-2 — Stage-write progression gate**: Stage N+1 only after preceding boundary table is
complete. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` accumulates continuously. Never reset.
[Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` vs [A-02] threshold. Cite
[A-02] by token. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Operations appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written." SLA as integer with unit.

**SC-6 — Phase gate obligation**: [A-00], [A-05], and [A-08] required; all items ✓ before
each transition. [Apply SC-6 at every gate position.]

**SC-7 — Stage table format**: `Stage Latency | Schema In | Schema Out | Data Loss Flag`.
[Apply SC-7 at every stage.]

**SC-8 — Trade-off as required section**: [A-14] required; [A-01], [A-02], [A-13]
required; ≥1 alternative; ≥2 dimensions. [Apply SC-8 at [A-14].]

**SC-9 — Incumbent Equiv. cell form**: `[A-01]: [named step + duration]`. [A-01] token
required. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [A-13] immediately before [A-14]. Additive
breakdown. Grand Total row. [Apply SC-10 before [A-14].]

**SC-11 — Baseline-first production**: [A-01] is first trace artifact, produced immediately
after [A-00]. No stage trace or boundary block before [A-01].

**SC-12 — Skip-level citation in Finance**: Finance's `Citing:` line must include
`[A-04]` — Operations' boundary checks, two positions prior in the
Operations → Commerce → Finance sequence. Commerce is Finance's immediate predecessor;
naming only Commerce's tokens without `[A-04]` fails SC-12. Position distance is two:
Finance = position 3, Operations = position 1. Phase Gate 2 item must cite [SC-12] by
numbered identifier.

**SC-13 — BASELINE CLOSURE**: [A-01] in [A-12] (formula: `Fall back to [A-01] if
[condition]`) and in [A-14]. [Apply SC-13 at [A-12] and [A-14].]

---

### ROLE 0 — Pre-Trace Setup (Operations)

[Operations runs the pre-trace gate before any role output.]

**[A-00] PRE-TRACE SETUP CHECKLIST** — Write FIRST, before [A-01]. Per SC-0. Mark each
✓ or ✗:
- [ ] ARTIFACT REGISTRY section is present in this prompt and lists [A-00] through [A-14]
- [ ] REGISTER DECLARATION section is present with closed-chain paragraph covering SC-0
  through SC-13
- [ ] BOUNDARY BLOCK SCHEMA section is present with the 7-column schema defined
- [ ] STRUCTURAL CONSTRAINTS section is present with SC-0 through SC-13 defined
- [ ] [A-01] is designated as the second artifact (immediately after [A-00])

All items must be ✓ before [A-01] is written. [Apply SC-0.]

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required (after [A-00]).]

**[A-01] INCUMBENT BASELINE** — Write immediately after [A-00]. Per SC-11. Describe the
manual CDR processing and billing workflow this pipeline replaces. Include ≥3 named steps
with durations (e.g., "CDR mediation engineer manually collects raw CDR files from switch
and validates record count: 60 min", "Billing analyst loads CDR batch into rating
spreadsheet, applies rate card lookup per subscriber plan: 90 min", "Finance analyst
exports rated CDR totals from spreadsheet, manually posts revenue entries to GL: 45 min").
Use entity names that will reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Entity vocabulary (reuse ≥2 names from [A-01]): CDR record,
normalized CDR, rated usage record, invoice record, payment confirmation record, GL revenue
entry, BI aggregation entry. Downstream consumer and business cadence (e.g., monthly
billing cycle close on last business day). Billing-cycle SLA: integer with unit, derived
from [A-01] total duration plus pipeline headroom. Per SC-5 verbatim append required.

**[A-03] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 1: CDR mediation layer → CDR normalization service
- Stage 2: Normalized CDR → Usage rating engine
- Stage 3: Rated usage record → Invoice generation service

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3, SC-4, SC-9 apply.]

**[A-05] PHASE GATE 1** — Tick before Commerce begins:
- [ ] [A-00] complete and all items ✓ (SC-0)
- [ ] [A-01] produced immediately after [A-00]; no trace or boundary block between them
  (SC-11)
- [ ] [A-01] ≥3 named steps with durations
- [ ] [A-02] SLA as integer with unit; SC-5 verbatim present
- [ ] Every stage in [A-03] has four columns per SC-7
- [ ] Every block in [A-04] has seven columns matching Part A headers
- [ ] Elapsed (cumul.) accumulates correctly (SC-3)
- [ ] Verdict FRESH or STALE (SC-4)
- [ ] Incumbent Equiv. cell: `[A-01]: [step + duration]` (SC-9)

Commerce may not begin until all ✓. [SC-6]

---

### ROLE 2 — Commerce

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 4: Invoice generation → Payment processing gateway
- Stage 5: Payment gateway → Payment confirmation service

**[A-07] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend from [A-04].] [SC-4.] [SC-9.]

**[A-08] PHASE GATE 2** — Tick before Finance begins:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] has four columns per SC-7
- [ ] Every block in [A-07] has seven columns matching Part A headers
- [ ] Elapsed (cumul.) extends [A-04] final value; not reset (SC-3)
- [ ] Verdict FRESH or STALE from [A-02] threshold (SC-4)
- [ ] Incumbent Equiv. cell: `[A-01]: [step + duration]` (SC-9)
- [ ] [SC-12]: Finance's `Citing:` line must include `[A-04]` — Operations' boundary
  checks, two positions prior. Position distance is two: Finance = pos 3,
  Operations = pos 1. Mark ✗ if [A-04] absent from Finance's Citing line.

Finance may not begin until all ✓. [SC-6]

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12 — Operations' boundary checks, two positions prior in the
Operations → Commerce → Finance sequence. Position distance is two.)

**[A-09] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 6: Payment confirmation → GL posting service
- Stage 7: GL revenue entry → Finance BI aggregation layer

**[A-10] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend from [A-07].] [SC-4.] [SC-9.]

**[A-11] STALE ANALYSIS** — Final Elapsed (cumul.) from [A-10] vs [A-02] threshold.
Normal-operation and failure-mode rows. Cite [A-02] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Formula:
`Fall back to [A-01] if [specific failure condition]`. Every no-handling flag and
Data Loss Flag YES gets a named recovery citing [A-01].

**[A-13] INCUMBENT TOTAL** — [Per Part B. Per SC-10.] Immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Operations | | |
| Commerce | | |
| Finance | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] [Per Part B. Per SC-8.]
Tokens [A-01], [A-02], [A-13] required. ≥1 alternative pattern. ≥2 dimensions.
