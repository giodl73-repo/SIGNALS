# flow-dataflow — Round 16 Variations

## R15 gap summary before writing

**C-48 target for R16**: R15 variations added SC-13 and SC-14 as named entries in the
REGISTER DECLARATION closed-chain paragraph, each with a governing authority statement.
C-48 generalizes this: every SC listed in the closed-chain paragraph must name by artifact
token every artifact it governs. In R15, SC-12's entry stated its phase-gate authority but
did not name the governed artifact token (e.g., `[A-04]`). SC-1 through SC-11 were not
listed in the closed-chain paragraph at all. C-48 requires the paragraph to be an exhaustive
self-index: register → SC → governed artifact, navigable by token match without reading
any SC body.

**C-49 target for R16**: C-49 generalizes the SC-13 enforcement description. In R15, SC-13's
entry named its enforcement mechanism ("inline callbacks at both section headers enforce the
[A-01] citation obligation by token match without output-prose inspection"). C-49 requires
the same treatment for every SC listed: each entry must name the enforcement pathway,
making the paragraph a self-describing authority map. An entry that states "SC-N NAME is
the governing authority" without naming how it enforces compliance does not pass.

Both C-48 and C-49 apply universally — to every SC listed in the closed-chain paragraph,
not only to SC-12 and SC-13.

## Variation axes

- **V-01**: Role sequence (C-48 + C-49 universal) — Finance → Operations → Commerce;
  retail e-commerce order-to-cash pipeline. Exhaustive closed-chain paragraph listing all
  SC-1 through SC-13 with governed artifact tokens and enforcement mechanisms. Commerce
  (pos 3) cites Finance [A-04] (pos 1) skip-level. Tabular register.

- **V-02**: Role sequence — non-natural Finance-last (C-48 + C-49); Healthcare claims
  adjudication pipeline. Commerce (intake) → Operations (adjudication) → Finance
  (settlement). Finance (pos 3) cites Commerce [A-04] (pos 1) skip-level per SC-12.
  Exhaustive closed-chain paragraph. SC-12 entry names governed artifact token and
  enforcement mechanism. Tabular register.

- **V-03**: Output format — prose register (C-48 + C-49 + C-47); SaaS subscription
  recurring billing pipeline. Finance → Operations → Commerce. Prose register. SC-14
  FORMAT MODE DECLARATION active. Closed-chain paragraph covers SC-1 through SC-14, each
  with governed tokens and enforcement mechanism. Commerce (pos 3) cites Finance [A-04]
  skip-level.

- **V-04**: Inertia framing — maximum incumbent baseline prominence (C-48 + C-49);
  manufacturing MRO procurement-to-pay pipeline. Finance → Operations → Commerce. [A-01]
  requires ≥5 named manual steps with per-step durations; every SC that touches [A-01]
  has that token named in its closed-chain entry. SC-13 closed-chain entry emphasizes
  the dual-callback enforcement with explicit [A-01] token reference. Tabular register.

- **V-05**: Combined — non-natural role sequence + lifecycle emphasis depth (C-48 + C-49);
  digital advertising spend reporting pipeline. Operations → Commerce → Finance.
  Finance (pos 3) cites Operations [A-04] (pos 1) skip-level. Adds Phase Gate 0
  (pre-artifact setup verification) as a third phase gate. Exhaustive closed-chain
  paragraph. Tabular register.

---

## V-01

**Axis**: Universal closed-chain paragraph (C-48 + C-49) — natural role sequence, tabular

**Hypothesis**: Finance → Operations → Commerce; retail e-commerce order-to-cash pipeline.
An exhaustive closed-chain paragraph naming governed artifact tokens and enforcement
mechanisms for all SC-1 through SC-13 makes REGISTER DECLARATION a complete self-describing
authority map — every structural failure mode has a navigable path from the register index
to its governing SC to its governed artifact, verifiable by token match without reading any
SC body or role instruction. Commerce (pos 3) cites Finance [A-04] two positions prior
(SC-12). Tabular register.

---

You are tracing data through a retail e-commerce order-to-cash pipeline — order capture
through payment settlement to revenue ledger to Commerce BI. Three expert roles run in the
sequence **Finance → Operations → Commerce**. Finance establishes the revenue recognition
SLA and the manual order-processing baseline that all subsequent roles must cite. Operations
and Commerce cite Finance's artifacts by token; they may not redeclare or re-derive either.

Commerce runs last and must cite Finance's boundary artifacts directly — two positions prior
in the Finance → Operations → Commerce sequence — as a required skip-level citation.
A Commerce `Citing:` line that names only Operations' artifacts without Finance's boundary
checks fails SC-12. Phase Gate 2 verifies this requirement by citing SC-12 by number before
Commerce may begin.

The physical pipeline flows: customer order capture → payment authorization service →
fraud detection engine → payment settlement processor → AR ledger posting → revenue
recognition engine → Commerce BI aggregation layer.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first; all subsequent
artifacts are produced in token order. Every citation anywhere in this output must use
the `[A-xx]` token exactly as spelled in this table. A citation to a target not listed
here is a protocol violation.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Finance | Manual order-to-cash processing workflow replaced by this pipeline; ≥3 named steps with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Finance | Entity vocabulary, revenue recognition SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Finance | Finance | Order capture → payment authorization → fraud detection → payment settlement processor; stage tables per SC-7 |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01]; required skip-level target for Commerce (SC-12) |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all items ✓ before Operations begins |
| [A-06] | STAGE TRACE — Operations | Operations | Payment settlement processor → AR ledger posting → revenue recognition engine; stage tables per SC-7 |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends Elapsed (cumul.) from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Operations | Self-verification checklist; all items ✓ before Commerce begins; item [SC-12] verifies Commerce skip-level citation |
| [A-09] | STAGE TRACE — Commerce | Commerce | Revenue recognition engine → Commerce BI aggregation → executive revenue dashboard; stage tables per SC-7 |
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
tokens and enforcement mechanism:

**SC-1 CITATION OPENER** governs [A-06], [A-09] (all non-first role outputs); enforced by
a token-match check at each role's opening `Citing:` line — a role block that omits the
`Citing:` line or references prior artifacts without `[A-xx]` tokens fails by absence of
the required line structure, without output-prose inspection.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] (stage tables) and
[A-04], [A-07], [A-10] (boundary tables); enforced by a hard lock at every stage advance
— Stage N+1 may not be written until the preceding boundary table is fully populated per
BOUNDARY BLOCK SCHEMA; the gate fires at every stage boundary as an inline callback, not
as a post-trace summary.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (boundary tables); enforced by
the `Elapsed (cumul.)` column requirement declared in Part A — any boundary block lacking
this column, or resetting to zero rather than accumulating, fails by column-header and
cell-value match without output-prose inspection.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (boundary tables); enforced by the
`Verdict` column requirement declared in Part A — any cell value other than exactly `FRESH`
or exactly `STALE` fails by string match without output-prose inspection.

**SC-5 STALENESS IMMUTABILITY** governs [A-02] (DOMAIN CONTEXT); enforced by a verbatim
append requirement — the exact phrase "This threshold is fixed. No subsequent role may
revise it after Stage 1 is written." must appear in [A-02]; absence or paraphrase fails
by phrase-match check.

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08] (phase gates); enforced by a
gating callback at every role transition — the next role block may not open until all
checklist items in the preceding phase gate are ✓; a role block that begins with any
unchecked item is a gate violation detectable at the role boundary.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09] (stage tables); enforced by
the `Stage Latency` column requirement declared in Part A — a stage table missing this
column fails by column-header match without reading row contents.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] (TRADE-OFF ANALYSIS); enforced by
a three-token check at [A-14] — `[A-01]`, `[A-02]`, and `[A-13]` must all appear as
citation tokens; absence of any one token fails by token-match without prose interpretation.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] (boundary tables,
Incumbent Equiv. column); enforced by the cell-form requirement declared in Part A —
required form is `[A-01]: [named manual step + duration]`; a bare duration without `[A-01]`
token fails by token-match check without inspecting surrounding prose.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] (INCUMBENT TOTAL); enforced by
the Part B ordering requirement — [A-13] must appear immediately before [A-14] and be
cited in [A-14] by token; [A-13] appearing elsewhere or without a Grand Total row fails
by position and structure check.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] (INCUMBENT BASELINE); enforced by a
positional lock — [A-01] must be the first artifact produced; any stage trace or boundary
block appearing before [A-01] is fully written fails by artifact-order check.

**SC-12 SKIP-LEVEL CITATION IN COMMERCE** governs [A-04] (Finance's boundary checks) via
Commerce's `Citing:` line; enforced by the Phase Gate 2 checklist item citing [SC-12] by
number — the item verifies that Commerce's `Citing:` line includes `[A-04]`; absence of
`[A-04]` in Commerce's `Citing:` line is detectable by token-match at the role opener
without reading role body. Commerce occupies position 3; Finance occupies position 1;
the position distance is two.

**SC-13 BASELINE CLOSURE** governs [A-12] (RECOVERY PRESCRIPTIONS) and [A-14]
(TRADE-OFF ANALYSIS); enforced by inline callbacks at both [A-12] and [A-14] section
headers that verify `[A-01]` citation by token match without output-prose inspection —
a section header lacking the [A-01] token is a protocol violation detectable from the
header line alone.

Together, SC-1 through SC-13 form a complete closed verification chain: every structural
failure mode has a named navigation path from this paragraph to its governing SC and its
governed artifact, verifiable by token match.

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
Citing [A-01] is required in every non-first role's Citing line. Prose back-references
do not satisfy SC-1. [Apply SC-1 at every non-first role opener.]

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding
BOUNDARY CHECK table is fully populated per BOUNDARY BLOCK SCHEMA. Write the table.
Confirm all seven columns are populated. Then write Stage N+1. [Apply SC-2 before every
stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` is computed inside each boundary block
as the sum of all prior stage latencies and all prior boundary latencies. It may not be
deferred to [A-11]. [Per REGISTER DECLARATION Part A, `Elapsed (cumul.)` row.]
[Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE`, derived by comparing
Elapsed (cumul.) against the [A-02] threshold. Cite [A-02] by token; do not restate its
numeric value. [Per REGISTER DECLARATION Part A, `Verdict` row.] [Apply SC-4 at every
boundary block.]

**SC-5 — Immutability**: Finance appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written." Declare the SLA as an integer
with unit, derived from [A-01] total manual duration plus acceptable pipeline latency
headroom.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required outputs. Each is a
checklist; every item must be ticked ✓ or ✗. The next role may not begin until all items
are ✓. [Apply SC-6 before every role transition.]

**SC-7 — Stage table format**: Every stage block is a markdown table with columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. [Per REGISTER DECLARATION
Part A, `Stage Latency` row.] [Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [Per REGISTER DECLARATION Part B,
TRADE-OFF ANALYSIS row.] All three tokens required: [A-01], [A-02], [A-13]. ≥1
alternative pattern named. ≥2 trade-off dimensions. [Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: [Per REGISTER DECLARATION Part A, `Incumbent
Equiv.` row.] Required form: `[A-01]: [named manual step + duration]`. Omitting the
[A-01] token is a protocol violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [Per REGISTER DECLARATION Part B,
INCUMBENT TOTAL row.] Produce [A-13] immediately before [A-14]. Sum all Incumbent Equiv.
values from [A-04], [A-07], [A-10]; show additive breakdown by role; Grand Total row
required. [A-14] must cite [A-13] as its numeric comparison endpoint. [Apply SC-10
before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] INCUMBENT BASELINE must be the first
artifact written. No boundary block and no stage trace may appear before [A-01] is fully
produced. Finance may not write Stage 1 until [A-01] is complete.

**SC-12 — Skip-level citation in Commerce**: Commerce's `Citing:` line must include
`[A-04]` — Finance's boundary checks, produced two positions prior in the
Finance → Operations → Commerce sequence. Operations is Commerce's immediate predecessor;
a `Citing:` line naming only Operations' tokens without `[A-04]` fails SC-12. The
position distance is two: Commerce occupies position 3, Finance occupies position 1.
A Phase Gate 2 verification item for this requirement must cite [SC-12] by its numbered
identifier in the item text itself.

**SC-13 — BASELINE CLOSURE**: [A-01] INCUMBENT BASELINE must appear as a named citation
token in two specific sections: (a) In [A-12] RECOVERY PRESCRIPTIONS — every recovery
formula must include the `[A-01]` token; a recovery that does not cite [A-01] is a
protocol violation. (b) In [A-14] TRADE-OFF ANALYSIS — `[A-01]` must be one of the
three required citation tokens alongside [A-02] and [A-13]. This SC is registered in
REGISTER DECLARATION as the governing authority for baseline-closure failures in [A-12]
and [A-14]; evaluators navigate to it from the closed-chain paragraph without searching
STRUCTURAL CONSTRAINTS. [Per SC-13, cite [A-01] in [A-12].] [Per SC-13, cite [A-01]
in [A-14].]

---

### ROLE 1 — Finance

[Finance runs first. No Citing line required. The incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST, before any domain context or stage trace.
Per SC-11: no boundary block and no stage trace may appear before [A-01] is fully produced.
Describe the manual order-to-cash workflow this pipeline replaces. Include ≥3 named manual
steps with durations (e.g., "Order processing team manually verifies payment authorization
against fraud rules in spreadsheet: 45 min", "Finance analyst posts payment settlement to
AR ledger by importing bank file: 90 min", "Revenue accountant reconciles daily AR entries
against order management system: 120 min"). Use entity names that will reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 names from [A-01]): customer order, payment authorization,
  fraud score, settlement batch, AR ledger entry, revenue recognition entry, BI aggregation
- Downstream consumer and business cadence (e.g., daily revenue close at 23:59 ET)
- Revenue recognition SLA: integer with unit, derived from [A-01] total manual duration
  plus acceptable pipeline latency headroom
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 1: Customer order capture → Payment authorization service
- Stage 2: Authorized payment → Fraud detection engine
- Stage 3: Fraud-cleared payment → Payment settlement processor

**[A-04] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA. One block after
Stage 1; one block after Stage 2; one block after Stage 3.
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
- Stage 4: Settlement batch → AR ledger posting
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
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named manual step + duration]` (SC-9)
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
`no handling — see [A-12]` annotation in [A-04]/[A-07]/[A-10] and every `Data Loss Flag:
YES` in [A-03]/[A-06]/[A-09], provide a specific named recovery action. Required formula:
`Fall back to [A-01] if [specific named failure condition]`. Cite [A-01] using this formula
at least once. SC-13 requires [A-01] to appear as a citation token in this section.

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
`[A-13]` — all three tokens required. SC-13 requires [A-01] to appear as a citation token.
Name ≥1 alternative data propagation pattern. Provide ≥2 trade-off dimensions using
[A-13] Grand Total as the numeric comparison endpoint.

---

---

## V-02

**Axis**: Role sequence — non-natural Finance-last, exhaustive closed-chain (C-48 + C-49)

**Hypothesis**: Commerce (claims intake) → Operations (adjudication) → Finance (settlement);
healthcare insurance claims adjudication pipeline. Finance runs last and must cite Commerce's
boundary artifacts [A-04] directly — two positions prior in the Commerce → Operations →
Finance sequence — as a required skip-level citation. The SC-12 closed-chain entry in
REGISTER DECLARATION names [A-04] as the governed artifact token (C-48) and names the
Phase Gate 2 enforcement mechanism by SC number (C-49), making Finance's skip-level
obligation discoverable from the register index without reading STRUCTURAL CONSTRAINTS.
All other SCs also have governed tokens and enforcement mechanisms in the closed-chain
paragraph. Tabular register.

---

You are tracing data through a healthcare insurance claims adjudication pipeline — claim
submission through clinical review to payment settlement. Three expert roles run in the
sequence **Commerce → Operations → Finance**. Commerce establishes the claims submission
baseline and vocabulary; Operations adjudicates; Finance settles and closes.

Finance runs last and must cite Commerce's boundary artifacts directly — two positions
prior in the Commerce → Operations → Finance sequence — as a required skip-level citation.
A Finance `Citing:` line that names only Operations' artifacts without Commerce's boundary
checks fails SC-12. Phase Gate 2 verifies this by citing SC-12 by number.

The physical pipeline flows: member claim submission portal → claims intake validator →
duplicate detection service → clinical adjudication engine → payment authorization →
EOB generation → EFT settlement processor → Finance ledger.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first. Every citation must
use the `[A-xx]` token exactly as spelled here.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Commerce | Manual claims intake and adjudication workflow replaced by this pipeline; ≥3 named steps with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Commerce | Entity vocabulary, adjudication SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Commerce | Commerce | Claim submission → claims intake validator → duplicate detection → adjudication engine intake; stage tables per SC-7 |
| [A-04] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; required skip-level target for Finance (SC-12) |
| [A-05] | PHASE GATE 1 | Commerce | Self-verification checklist; all items ✓ before Operations begins |
| [A-06] | STAGE TRACE — Operations | Operations | Clinical adjudication engine → payment authorization → EOB generation; stage tables per SC-7 |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends Elapsed (cumul.) from [A-04] |
| [A-08] | PHASE GATE 2 | Operations | Self-verification checklist; all items ✓ before Finance begins; item [SC-12] verifies Finance skip-level citation |
| [A-09] | STAGE TRACE — Finance | Finance | EOB generation → EFT settlement processor → Finance ledger posting; stage tables per SC-7 |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends Elapsed (cumul.) from [A-07] |
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
tokens and enforcement mechanism:

**SC-1 CITATION OPENER** governs [A-06], [A-09] (all non-first role outputs); enforced by
token-match at each role's opening `Citing:` line — absent or prose-only back-reference
fails by line-structure check without reading role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] (stage tables) and
[A-04], [A-07], [A-10] (boundary tables); enforced by an inline lock at every stage
advance — Stage N+1 may not be written until the preceding boundary table is fully
populated; gate fires as a per-transition callback.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (boundary tables, `Elapsed
(cumul.)` column); enforced by Part A column requirement — a missing column or zero-reset
value fails by column-header and cell-value match.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (boundary tables, `Verdict`
column); enforced by Part A string requirement — any value other than exactly `FRESH` or
`STALE` fails by string match.

**SC-5 STALENESS IMMUTABILITY** governs [A-02] (DOMAIN CONTEXT); enforced by verbatim
phrase requirement — the exact phrase "This threshold is fixed. No subsequent role may
revise it after Stage 1 is written." must appear; paraphrase or absence fails by
phrase-match.

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08] (phase gates); enforced by a
gating callback at every role transition — an unchecked item in the preceding phase gate
blocks the next role block; detectable at the role boundary without reading role content.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09] (stage tables, `Stage
Latency` column); enforced by Part A column requirement — a stage table missing the
`Stage Latency` column fails by column-header match.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] (TRADE-OFF ANALYSIS); enforced by
three-token check — `[A-01]`, `[A-02]`, `[A-13]` must all appear in [A-14]; absence of
any token fails by token-match.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] (`Incumbent Equiv.`
column); enforced by Part A cell-form requirement — `[A-01]` token must appear in every
cell; bare duration without token fails by token-match.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] (INCUMBENT TOTAL); enforced by
Part B ordering requirement — [A-13] must immediately precede [A-14] with a Grand Total
row; position and structure verified by artifact-order check.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] (INCUMBENT BASELINE); enforced by
positional lock — [A-01] must be the first artifact produced; any earlier stage trace or
boundary block fails by artifact-order check.

**SC-12 SKIP-LEVEL CITATION IN FINANCE** governs [A-04] (Commerce's boundary checks) via
Finance's `Citing:` line; enforced by the Phase Gate 2 item citing [SC-12] by number —
Finance's `Citing:` line must include `[A-04]`; absence is detectable by token-match at
the Finance role opener without reading role body. Finance occupies position 3; Commerce
occupies position 1; the position distance is two.

**SC-13 BASELINE CLOSURE** governs [A-12] (RECOVERY PRESCRIPTIONS) and [A-14]
(TRADE-OFF ANALYSIS); enforced by inline callbacks at both [A-12] and [A-14] section
headers that verify `[A-01]` citation by token match without output-prose inspection.

Together, SC-1 through SC-13 form a complete closed verification chain: every structural
failure mode is navigable from this paragraph by token match.

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
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Table with roles Commerce, Operations, Finance, Grand Total; all subtotals numeric | Prose-only; missing role row |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | Tokens [A-01], [A-02], [A-13] all present; ≥1 alternative; ≥2 dimensions | Any token absent |

---

### BOUNDARY BLOCK SCHEMA

Every boundary block: markdown table with columns in order:

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

Column headers must match Part A exactly.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Commerce opens with `Citing: [A-xx], ...`
listing prior tokens. [A-01] required in every non-first role's Citing line.
[Apply SC-1 at every non-first role opener.]

**SC-2 — Stage-write progression gate**: Stage N+1 only after preceding boundary table is
fully populated per BOUNDARY BLOCK SCHEMA. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` accumulates across all prior stage and
boundary latencies. Never reset within the run. [Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = exactly `FRESH` or `STALE` vs [A-02] threshold.
[Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Commerce appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written." SLA as integer with unit,
derived from [A-01] total duration.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required. Every item ✓ before
next role begins. [Apply SC-6 before every role transition.]

**SC-7 — Stage table format**: Columns `Stage Latency | Schema In | Schema Out | Data
Loss Flag` in every stage block. [Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [A-14] is required. Tokens [A-01], [A-02],
[A-13] all required. ≥1 alternative pattern. ≥2 dimensions. [Apply SC-8 at [A-14].]

**SC-9 — Incumbent Equiv. cell form**: Form `[A-01]: [named step + duration]` required.
[Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [A-13] immediately before [A-14].
Additive role breakdown. Grand Total row. [Apply SC-10 before [A-14].]

**SC-11 — Baseline-first production**: [A-01] is first artifact. No stage trace or
boundary block before [A-01] is complete.

**SC-12 — Skip-level citation in Finance**: Finance's `Citing:` line must include `[A-04]`
— Commerce's boundary checks, two positions prior in the Commerce → Operations → Finance
sequence. Operations is Finance's immediate predecessor; a `Citing:` line naming only
Operations' tokens without `[A-04]` fails SC-12. Position distance is two: Finance
occupies position 3, Commerce occupies position 1. A Phase Gate 2 verification item must
cite [SC-12] by its numbered identifier in the item text.

**SC-13 — BASELINE CLOSURE**: [A-01] must appear as a citation token in both [A-12]
(every recovery formula: `Fall back to [A-01] if [condition]`) and [A-14] (required
alongside [A-02] and [A-13]). Registered in REGISTER DECLARATION as governing authority
for baseline-closure failures in [A-12] and [A-14]. [Apply SC-13 at [A-12] and [A-14].]

---

### ROLE 1 — Commerce

[Commerce runs first. No Citing line. Incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — First artifact. Describe the manual claims intake and
adjudication workflow replaced. ≥3 named steps with durations (e.g., "Member services rep
manually logs claim from fax/portal into legacy adjudication system: 30 min", "Clinical
reviewer verifies medical codes against coverage policy in paper binder: 180 min",
"Finance analyst manually prepares EFT payment batch from adjudication printout: 60 min").
Use entity names that will reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Entity vocabulary (reuse ≥2 names from [A-01]): member claim,
intake validation record, duplicate flag, adjudication decision, EOB document, EFT payment
record, Finance ledger entry. Downstream consumer and business cadence (e.g., 24h claims
processing window for high-priority claims). Adjudication SLA: integer with unit.
Per SC-5 verbatim append required.

**[A-03] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 1: Claim submission portal → Claims intake validator
- Stage 2: Validated claim → Duplicate detection service
- Stage 3: Deduplicated claim → Adjudication engine intake queue

**[A-04] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3, SC-4, SC-9 apply.]

**[A-05] PHASE GATE 1** — Tick before Operations begins:
- [ ] [A-01] first artifact; no trace or boundary block precedes it (SC-11)
- [ ] [A-01] ≥3 named steps with durations
- [ ] [A-02] SLA as integer with unit; SC-5 verbatim present
- [ ] Every stage in [A-03] has four columns per SC-7
- [ ] Every block in [A-04] has seven columns matching Part A headers
- [ ] Elapsed (cumul.) accumulates correctly (SC-3)
- [ ] Verdict FRESH or STALE (SC-4)
- [ ] Incumbent Equiv. cell form: `[A-01]: [step + duration]` (SC-9)

Operations may not begin until all ✓. [SC-6]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 4: Adjudication engine → Clinical code review → Payment authorization
- Stage 5: Payment authorization → EOB generation

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend from [A-04] final Elapsed.] [SC-4.] [SC-9.]

**[A-08] PHASE GATE 2** — Tick before Finance begins:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] has four columns per SC-7
- [ ] Every block in [A-07] has seven columns matching Part A headers
- [ ] Elapsed (cumul.) extends [A-04] final value (SC-3)
- [ ] Verdict FRESH or STALE from [A-02] threshold (SC-4)
- [ ] Incumbent Equiv. cell: `[A-01]: [step + duration]` (SC-9)
- [ ] [SC-12]: Finance's `Citing:` line must include `[A-04]` — Commerce's boundary
  checks, two positions prior. Position distance is two: Finance = pos 3, Commerce = pos 1.
  Mark ✗ if [A-04] absent from Finance's Citing line.

Finance may not begin until all ✓. [SC-6]

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12 — Commerce's boundary checks, two positions prior in the
Commerce → Operations → Finance sequence. Position distance is two.)

**[A-09] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 6: EOB generation → EFT settlement processor
- Stage 7: EFT settlement → Finance ledger posting

**[A-10] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend from [A-07].] [SC-4.] [SC-9.]

**[A-11] STALE ANALYSIS** — Final Elapsed (cumul.) from [A-10] vs [A-02] threshold.
Normal-operation and failure-mode rows. Cite [A-02] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Formula:
`Fall back to [A-01] if [specific failure condition]`. Every no-handling flag and every
YES Data Loss Flag gets a named recovery action citing [A-01].

**[A-13] INCUMBENT TOTAL** — [Per Part B. Per SC-10.] Immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Commerce | | |
| Operations | | |
| Finance | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] [Per Part B. Per SC-8.]
Tokens [A-01], [A-02], [A-13] required. ≥1 alternative pattern. ≥2 dimensions.

---

---

## V-03

**Axis**: Output format — prose register, SC-14 active, exhaustive closed-chain (C-48 + C-49 + C-47)

**Hypothesis**: Finance → Operations → Commerce; SaaS subscription recurring billing
pipeline. Prose (non-tabular) register. SC-14 FORMAT MODE DECLARATION is active and must
appear in the closed-chain paragraph as a named navigation entry (C-47), naming its
governed artifact tokens and enforcement mechanism (C-48 + C-49). The criterion
substitution map in SC-14 lists which tabular criteria are replaced by prose equivalents.
All SC-1 through SC-14 entries in the closed-chain paragraph name governed tokens and
enforcement mechanisms. Commerce (pos 3) cites Finance [A-04] skip-level per SC-12.

---

You are tracing data through a SaaS subscription recurring billing pipeline — subscription
event to invoice to revenue recognition. Three expert roles run in the sequence
**Finance → Operations → Commerce**. Finance establishes the revenue recognition SLA and
the manual billing baseline. Operations and Commerce cite Finance's artifacts by token.

This output uses the **prose register**. All stage traces and boundary checks are written
as labeled prose paragraphs, not markdown tables. SC-14 FORMAT MODE DECLARATION is active.
Consult the criterion substitution map in REGISTER DECLARATION before writing any output.

Commerce runs last and must cite Finance's boundary artifacts [A-04] directly — two
positions prior — as a required skip-level citation (SC-12).

The physical pipeline flows: subscription event trigger → entitlement service → usage
aggregation → invoice generation engine → payment collection service → dunning processor
→ revenue recognition ledger → Commerce analytics platform.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first. Every citation uses
`[A-xx]` tokens exactly as spelled here. Prose references without tokens are violations.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Finance | Manual subscription billing workflow replaced; ≥3 named steps with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Finance | Entity vocabulary, revenue recognition SLA (immutable after Stage 1), cadence; SLA from [A-01] total duration |
| [A-03] | STAGE TRACE — Finance | Finance | Subscription trigger → entitlement service → usage aggregation → invoice generation; prose paragraphs per SC-7 prose form |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | Prose boundary paragraphs per BOUNDARY BLOCK SCHEMA prose form; required skip-level target for Commerce (SC-12) |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all items ✓ before Operations begins |
| [A-06] | STAGE TRACE — Operations | Operations | Invoice generation → payment collection → dunning processor; prose paragraphs |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | Prose boundary paragraphs; extends elapsed from [A-04] |
| [A-08] | PHASE GATE 2 | Operations | Checklist; all ✓ before Commerce; item [SC-12] verifies Commerce skip-level |
| [A-09] | STAGE TRACE — Commerce | Commerce | Dunning processor → revenue recognition ledger → Commerce analytics; prose paragraphs |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | Prose boundary paragraphs; extends elapsed from [A-07] |
| [A-11] | STALE ANALYSIS | Commerce | Prose narrative: normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Prose prescriptions; formula: `Fall back to [A-01] if [condition]`; SC-13 applies |
| [A-13] | INCUMBENT TOTAL | Commerce | Labeled prose summary: per-role incumbent subtotals and Grand Total; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Prose named section; cites [A-01], [A-02], [A-13]; SC-13 applies |

---

### REGISTER DECLARATION

This output uses the **prose register** throughout. SC-14 FORMAT MODE DECLARATION is
active. Consult the criterion substitution map below before writing any output.

**Criterion substitution map (SC-14):**

| Tabular criterion | Prose-register equivalent |
|-------------------|--------------------------|
| C-28 (named-column boundary schema) | Each boundary paragraph opens with a fixed-label sequence: `Entity:` / `Elapsed (cumul.):` / `Verdict:` / `Error Handling:` / `Schema Delta:` / `Data Loss Flag:` / `Incumbent Equiv.:` — labels must match Part A header strings exactly |
| C-30 (output register with field markers) | Part A lists required label strings and their required sentence form; Part B lists required section openings |
| C-32 (register compliance marker mapping) | Part A maps each required label to: Required Label (exact string), Required Sentence Form, Disqualifying Form |
| C-34 (Incumbent Equiv. cell with token citation) | Each `Incumbent Equiv.:` sentence must include `[A-01]: [named manual step + duration]` |
| C-37 (REGISTER DECLARATION as sole authority) | This section remains the sole authority for C-34 and C-35 prose equivalents |

**Prose-register invariant fields**: The following structural fields must appear in every
boundary paragraph regardless of format: Entity, Elapsed (cumul.), Verdict, Error Handling,
Schema Delta, Data Loss Flag, Incumbent Equiv. Absence of any field fails by label-search
without prose interpretation.

**This section is the sole authoritative reference for C-34 (Incumbent Equiv. sentence
form) and C-35 (INCUMBENT TOTAL section format). An evaluator determines pass/fail for
both criteria by reading this section alone.**

**Exhaustive closed verification chain** — every SC listed with its governed artifact
tokens and enforcement mechanism:

**SC-1 CITATION OPENER** governs [A-06], [A-09]; enforced by label-match at each non-first
role's opening `Citing:` sentence — absent Citing sentence or prose-only back-reference
fails by sentence-structure check.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] and [A-04], [A-07],
[A-10]; enforced by inline lock at every stage advance — Stage N+1 paragraph may not begin
until the preceding boundary paragraph's seven labels are all populated; gate fires per
stage transition.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (`Elapsed (cumul.):` label);
enforced by Part A label requirement — an absent label, or an elapsed value that does not
accumulate from the prior boundary paragraph's total, fails by label and value check.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (`Verdict:` label); enforced by
Part A string requirement — sentence must contain exactly `FRESH` or exactly `STALE`
derived from [A-02] threshold; any other value fails by string match.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; enforced by verbatim phrase requirement
in [A-02] — exact phrase "This threshold is fixed. No subsequent role may revise it after
Stage 1 is written." must appear; absence or paraphrase fails by phrase-match.

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08]; enforced by gating callback at
each role transition — next role paragraph may not open until all checklist items are ✓.

**SC-7 STAGE TABLE FORMAT (prose form)** governs [A-03], [A-06], [A-09]; enforced by
Part A label requirement — each stage paragraph must contain `Stage Latency:` label;
absence fails by label-search.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14]; enforced by three-token check —
`[A-01]`, `[A-02]`, `[A-13]` must appear in [A-14] prose; absence fails by token-match.

**SC-9 INCUMBENT EQUIV. SENTENCE FORM** governs [A-04], [A-07], [A-10] (`Incumbent
Equiv.:` label); enforced by Part A sentence-form requirement — sentence must include
`[A-01]: [named step + duration]`; bare duration without token fails by token-match.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13]; enforced by Part B ordering —
[A-13] must immediately precede [A-14]; Grand Total sentence required; position verified
by artifact-order check.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01]; enforced by positional lock — [A-01]
is the first artifact; any stage trace or boundary paragraph before [A-01] fails by
artifact-order check.

**SC-12 SKIP-LEVEL CITATION IN COMMERCE** governs [A-04] via Commerce's `Citing:` sentence;
enforced by Phase Gate 2 item citing [SC-12] by number — Commerce's `Citing:` sentence
must include `[A-04]`; absence is detectable by token-match at the Commerce role opener.
Position distance is two: Commerce = position 3, Finance = position 1.

**SC-13 BASELINE CLOSURE** governs [A-12] and [A-14]; enforced by inline callbacks at
both [A-12] and [A-14] section openings that verify `[A-01]` citation by token match
without output-prose inspection.

**SC-14 FORMAT MODE DECLARATION** governs [A-03], [A-04], [A-06], [A-07], [A-09], [A-10],
[A-13] (all non-tabular role outputs and summaries); enforced by criterion substitution
map completeness check — a prose output that lacks the required label sequence in any
boundary paragraph, or an [A-13] section without per-role labeled subtotals, fails by
the substitution map's prescribed form without prose interpretation.

Together, SC-1 through SC-14 form a complete closed verification chain: every structural
failure mode is navigable from this paragraph by token match or label-search.

**Part A — Field compliance markers (boundary paragraph labels):**

| Required Field | Label String | Required Sentence Form | Disqualifying Form |
|----------------|-------------|------------------------|--------------------|
| Domain entity | `Entity:` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.):` | Numeric sum of all prior latencies, in minutes | Partial sum; reset to zero |
| Freshness verdict | `Verdict:` | Sentence containing exactly `FRESH` or `STALE` | Any other value |
| Error handling | `Error Handling:` | Named mechanism or exactly `no handling — see [A-12]` | Silence; absent label |
| Schema change | `Schema Delta:` | Named field-level changes or exactly `NONE` | Absent label |
| Data loss | `Data Loss Flag:` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.:` | `[A-01]: [named manual step + duration]` | Bare duration; token absent |
| Stage latency | `Stage Latency:` | Explicit value, range, or characterization | Absent label |

**Part B — Section format compliance markers:**

| Required Section | Section Opening | Required Content Form | Disqualifying Form |
|------------------|-----------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Per-role labeled subtotals (Finance, Operations, Commerce) and Grand Total sentence; all subtotals numeric | No per-role breakdown; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | Tokens [A-01], [A-02], [A-13] present; ≥1 alternative pattern; ≥2 dimensions | Any token absent |

---

### BOUNDARY BLOCK SCHEMA (prose form)

Every boundary paragraph must contain the following labels in order, each on its own line:

```
Entity: [named entity from [A-02] vocabulary]
Elapsed (cumul.): [numeric cumulative sum, in minutes]
Verdict: [exactly FRESH or STALE]
Error Handling: [mechanism, or "no handling — see [A-12]"]
Schema Delta: [named changes, or "NONE"]
Data Loss Flag: [YES — [loss point name], or NO]
Incumbent Equiv.: [A-01]: [named manual step + duration]
```

Label strings must match Part A spellings exactly. A missing or renamed label fails the schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 through SC-14** — As described in REGISTER DECLARATION closed-chain paragraph.
Inline callbacks apply as noted per SC:
[Apply SC-1 at every non-first role opener.]
[Apply SC-2 before every stage advance.]
[Apply SC-3 at every boundary paragraph.]
[Apply SC-4 at every boundary paragraph.]
[Apply SC-5 in [A-02].]
[Apply SC-6 before every role transition.]
[Apply SC-7 at every stage paragraph.]
[Apply SC-8 at [A-14].]
[Apply SC-9 at every boundary paragraph.]
[Apply SC-10 before [A-14].]
[Apply SC-11 before Stage 1.]
[Apply SC-12 at Commerce role opener and Phase Gate 2.]
[Apply SC-13 at [A-12] and [A-14].]
[Apply SC-14 throughout — consult substitution map before every output artifact.]

---

### ROLE 1 — Finance

[Finance runs first. No Citing sentence required. [A-01] leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — First. Describe manual subscription billing workflow.
≥3 named steps with durations (e.g., "Billing analyst exports subscription events from
CRM into billing spreadsheet: 60 min", "Finance team manually calculates prorated charges
and credits for mid-cycle changes: 90 min", "Accountant generates paper invoices from
spreadsheet and emails to customers: 120 min"). Use entity names reappearing in [A-02].

**[A-02] DOMAIN CONTEXT** — Prose paragraph. Entity vocabulary (≥2 names from [A-01]):
subscription event, entitlement record, usage aggregate, invoice, payment attempt,
dunning record, revenue recognition entry, analytics event. Cadence (e.g., monthly billing
cycle closing on last day of month). Revenue recognition SLA: integer with unit. SC-5
verbatim append required.

**[A-03] STAGE TRACE — Finance** — Prose paragraphs. Per SC-7 prose form (Stage Latency
label required). Per SC-2.
- Stage 1: Subscription event trigger → Entitlement service
- Stage 2: Entitlement record → Usage aggregation
- Stage 3: Usage aggregate → Invoice generation engine

**[A-04] BOUNDARY CHECKS — Finance** — Prose paragraphs per BOUNDARY BLOCK SCHEMA
prose form. One paragraph after each of Stages 1, 2, 3.
[SC-3, SC-4, SC-9 apply per label requirements.]

**[A-05] PHASE GATE 1** — Tick before Operations:
- [ ] [A-01] first; no trace or boundary before it (SC-11)
- [ ] [A-01] ≥3 steps with durations
- [ ] [A-02] SLA as integer with unit; SC-5 verbatim present
- [ ] Every stage paragraph in [A-03] contains `Stage Latency:` label (SC-7 prose)
- [ ] Every boundary paragraph in [A-04] contains all 7 required labels per Part A
- [ ] `Elapsed (cumul.)` accumulates correctly in [A-04] (SC-3)
- [ ] `Verdict` is FRESH or STALE in every [A-04] paragraph (SC-4)
- [ ] `Incumbent Equiv.` form: `[A-01]: [step + duration]` in every [A-04] para (SC-9)

Operations may not begin until all ✓. [SC-6]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Prose. Per SC-7 prose form. Per SC-2.
- Stage 4: Invoice generation → Payment collection service
- Stage 5: Failed payment → Dunning processor

**[A-07] BOUNDARY CHECKS — Operations** — Prose per BOUNDARY BLOCK SCHEMA prose form.
[SC-3: Elapsed extends [A-04] final value.] [SC-4.] [SC-9.]

**[A-08] PHASE GATE 2** — Tick before Commerce:
- [ ] Citing sentence names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage paragraph has `Stage Latency:` label (SC-7)
- [ ] Every boundary paragraph has all 7 labels matching Part A (SC-14)
- [ ] Elapsed accumulates from [A-04] final (SC-3)
- [ ] Verdict FRESH or STALE (SC-4)
- [ ] `Incumbent Equiv.:` form correct (SC-9)
- [ ] [SC-12]: Commerce's `Citing:` sentence must include `[A-04]`. Position distance two:
  Commerce = pos 3, Finance = pos 1. Mark ✗ if [A-04] absent.

Commerce may not begin until all ✓. [SC-6]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] per SC-12 — Finance's boundary checks, two positions prior. Position distance is two.)

**[A-09] STAGE TRACE — Commerce** — Prose. Per SC-7 prose form. Per SC-2.
- Stage 6: Dunning processor → Revenue recognition ledger
- Stage 7: Revenue recognition entry → Commerce analytics platform

**[A-10] BOUNDARY CHECKS — Commerce** — Prose per BOUNDARY BLOCK SCHEMA prose form.
[SC-3, SC-4, SC-9 apply.]

**[A-11] STALE ANALYSIS** — Prose narrative comparing final Elapsed (cumul.) from [A-10]
against [A-02] threshold. Separate sentences for normal-operation and failure-mode.
Cite [A-02] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Prose prescriptions.
Formula: `Fall back to [A-01] if [specific failure condition]`. Every no-handling label
and every Data Loss Flag YES gets a named recovery citing [A-01].

**[A-13] INCUMBENT TOTAL** — [Per Part B. Per SC-10.] Prose section immediately before
[A-14]. Per-role labeled subtotals and Grand Total sentence:

```
Finance incumbent subtotal: [sum] min — Steps cited: [step names from [A-01]]
Operations incumbent subtotal: [sum] min — Steps cited: [step names from [A-01]]
Commerce incumbent subtotal: [sum] min — Steps cited: [step names from [A-01]]
Grand Total: [sum] min
```

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] [Per Part B. Per SC-8.]
Prose named section. Tokens [A-01], [A-02], [A-13] required. ≥1 alternative pattern.
≥2 dimensions using [A-13] Grand Total as numeric comparison endpoint.

---

---

## V-04

**Axis**: Inertia framing — maximum incumbent baseline prominence, exhaustive closed-chain (C-48 + C-49)

**Hypothesis**: Finance → Operations → Commerce; manufacturing MRO procurement-to-pay
pipeline. [A-01] INCUMBENT BASELINE is required to have ≥5 named manual steps with
per-step durations, and every SC in the closed-chain paragraph that governs an artifact
touching [A-01] names [A-01] explicitly in both its governed-token declaration and its
enforcement mechanism description. SC-13's closed-chain entry places maximum emphasis on
the dual-callback enforcement — the [A-01] token is named at both enforcement sites and
the token-match mechanism is stated explicitly. This tests whether heavy incumbent
baseline framing amplifies C-48/C-49 compliance by making [A-01] the visible anchor of
the closed-chain paragraph as a whole. Commerce (pos 3) cites Finance [A-04] skip-level
per SC-12. Tabular register.

---

You are tracing data through a manufacturing MRO (maintenance, repair, and operations)
procurement-to-pay pipeline — purchase requisition through goods receipt to supplier
payment. Three expert roles run in the sequence **Finance → Operations → Commerce**.
Finance establishes the payment terms SLA and the manual procurement baseline; Operations
handles receiving and matching; Commerce manages supplier portal data and Commerce BI.

The manual procurement process this pipeline replaces is complex and forms the core
comparison baseline for every downstream trade-off and recovery decision. Finance must
document ≥5 distinct manual steps with individual durations. All roles cite [A-01] by
token at every Incumbent Equiv. cell and wherever recovery or trade-off decisions are made.

Commerce runs last and must cite Finance's boundary artifacts [A-04] directly — two
positions prior — as a required skip-level citation (SC-12).

The physical pipeline flows: purchase requisition → approval workflow engine → supplier
purchase order transmission → goods receipt confirmation → three-way match engine →
invoice verification → payment run processor → ERP AP ledger → Commerce supplier portal.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first. Every citation uses
`[A-xx]` tokens. Prose references without tokens are violations.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Finance | Manual MRO procurement-to-pay workflow; **≥5 named steps with per-step durations**; produced FIRST. SC-11 applies. [A-01] is the primary citation anchor for all recovery, trade-off, and Incumbent Equiv. computations. |
| [A-02] | DOMAIN CONTEXT | Finance | Entity vocabulary, payment terms SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Finance | Finance | Requisition → approval workflow → PO transmission → goods receipt confirmation; stage tables per SC-7 |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; Incumbent Equiv. cells cite [A-01]; required skip-level target for Commerce (SC-12) |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all ✓ before Operations |
| [A-06] | STAGE TRACE — Operations | Operations | Goods receipt confirmation → three-way match engine → invoice verification; stage tables per SC-7 |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends Elapsed from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Operations | Checklist; all ✓ before Commerce; item [SC-12] verifies Commerce skip-level |
| [A-09] | STAGE TRACE — Commerce | Commerce | Invoice verification → payment run processor → ERP AP ledger → Commerce supplier portal; stage tables per SC-7 |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends Elapsed from [A-07]; Incumbent Equiv. cells cite [A-01] |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss/no-handling item; formula: `Fall back to [A-01] if [condition]`; SC-13 applies |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required section; cites [A-01], [A-02], [A-13]; SC-13 applies |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell form)
and C-35 (INCUMBENT TOTAL section format).**

**Exhaustive closed verification chain** — every SC listed with its governed artifact
tokens and enforcement mechanism. SCs governing artifacts that cite [A-01] are annotated
with [A-01] as the referenced anchor token:

**SC-1 CITATION OPENER** governs [A-06], [A-09]; enforced by token-match at each
non-first role's opening `Citing:` line — absent or prose-only reference fails by
line-structure check.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] and [A-04], [A-07],
[A-10]; enforced by inline lock at every stage advance — boundary table must be fully
populated before next stage; gate fires per-transition.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (`Elapsed (cumul.)` column);
enforced by Part A column requirement — absent column or zero-reset fails by column-header
and cell-value check.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (`Verdict` column); enforced by
Part A string requirement — value must be exactly `FRESH` or `STALE`; any other string
fails by value check.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; enforced by verbatim phrase requirement
— exact phrase required in [A-02]; absence or paraphrase fails by phrase-match.

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08]; enforced by gating callback
at each role transition — unchecked item blocks next role block.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09]; enforced by Part A `Stage
Latency` column requirement — absent column fails by header-match.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14]; enforced by three-token check —
`[A-01]`, `[A-02]`, `[A-13]` must appear; absence fails by token-match. [A-01] is the
incumbent baseline anchor; its absence in [A-14] is a protocol violation detectable from
[A-14] header alone.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] (`Incumbent Equiv.`
column); enforced by Part A cell-form requirement — `[A-01]: [named manual step +
duration]` required; bare duration without `[A-01]` token fails by token-match. [A-01]
is the authority for all incumbent step names and durations.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13]; enforced by Part B ordering —
[A-13] immediately before [A-14]; Grand Total row required; structure verified by
artifact-order and row-structure check.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01]; enforced by positional lock — [A-01]
is the first artifact produced, and it must contain ≥5 named manual steps; any stage trace
or boundary block before [A-01] is complete fails by artifact-order check.

**SC-12 SKIP-LEVEL CITATION IN COMMERCE** governs [A-04] (Finance's boundary checks) via
Commerce's `Citing:` line; enforced by Phase Gate 2 item citing [SC-12] by number —
Commerce's `Citing:` line must include `[A-04]`; absence detectable by token-match at
Commerce opener. Position distance is two: Commerce = pos 3, Finance = pos 1.

**SC-13 BASELINE CLOSURE** governs [A-12] (RECOVERY PRESCRIPTIONS) and [A-14]
(TRADE-OFF ANALYSIS); enforced by inline callbacks at both [A-12] and [A-14] section
headers that verify `[A-01]` citation by token match without output-prose inspection —
[A-01] is the procurement baseline authority; its absence at either header is a protocol
violation detectable from the header line alone, without reading recovery or trade-off
prose.

Together, SC-1 through SC-13 form a complete closed verification chain. SC-9, SC-11,
SC-13 are the primary [A-01]-anchored governance paths; their entries above name [A-01]
explicitly as the governed or enforced token.

**Part A — Field compliance markers:**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric cumulative sum, minutes | Partial sum; reset |
| Freshness verdict | `Verdict` | Exactly `FRESH` or `STALE` | Any other value |
| Error handling | `Error Handling` | Named mechanism or `no handling — see [A-12]` | Silence; absent |
| Schema change | `Schema Delta` | Named changes or `NONE` | Absent |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` | Bare duration; [A-01] absent |
| Stage latency | `Stage Latency` | Explicit value, range, or characterization | Inferred |

**Part B — Section format compliance markers:**

| Required Section | Header | Required Content | Disqualifying Form |
|------------------|--------|------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Role rows Finance/Operations/Commerce + Grand Total; subtotals numeric; steps cited from [A-01] | Missing role row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | [A-01], [A-02], [A-13] tokens present; ≥1 alternative; ≥2 dimensions | Any token absent |

---

### BOUNDARY BLOCK SCHEMA

Every boundary block: markdown table with columns in order:

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

Headers must match Part A exactly.

---

### STRUCTURAL CONSTRAINTS

**SC-1 through SC-13** — As described in REGISTER DECLARATION closed-chain paragraph.
Per-transition callbacks:
[Apply SC-1 at every non-first role opener.]
[Apply SC-2 before every stage advance.]
[Apply SC-3 at every boundary block.]
[Apply SC-4 at every boundary block.]
[Apply SC-5 in [A-02].]
[Apply SC-6 before every role transition.]
[Apply SC-7 at every stage block.]
[Apply SC-8 at [A-14].]
[Apply SC-9 at every boundary block.]
[Apply SC-10 before [A-14].]
[Apply SC-11 before Stage 1.]
[Apply SC-12 at Commerce role opener and Phase Gate 2.]
[Apply SC-13 at [A-12] and [A-14].]

---

### ROLE 1 — Finance

[Finance runs first. No Citing line. [A-01] leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — First artifact. Per SC-11. Describe the manual MRO
procurement-to-pay workflow replaced. **≥5 named manual steps with individual durations**:
e.g., "Purchasing agent receives maintenance request by email and manually enters into
requisition spreadsheet: 30 min", "Procurement manager reviews and approves requisition
in shared SharePoint folder: 60 min", "Buyer manually faxes purchase order to supplier
and logs confirmation call: 45 min", "Receiving clerk manually counts goods and compares
to paper PO — calls buyer if mismatch: 90 min", "AP analyst manually keys invoice into
ERP from paper copy, then routes to three-way match review: 120 min". Use entity names
that will reappear in [A-02]. All [A-01] step names are the source for every `Incumbent
Equiv.` cell across [A-04], [A-07], [A-10].

**[A-02] DOMAIN CONTEXT** — ≥2 entity names from [A-01]: purchase requisition, approved
PO, goods receipt record, three-way match result, verified invoice, payment run batch,
AP ledger entry, supplier portal record. Business cadence (e.g., payment run every 15 days
to meet net-30 terms). Payment terms SLA: integer with unit derived from [A-01] total.
SC-5 verbatim append required.

**[A-03] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 1: Purchase requisition → Approval workflow engine
- Stage 2: Approved requisition → Supplier PO transmission
- Stage 3: PO transmitted → Goods receipt confirmation

**[A-04] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3, SC-4 apply.] [SC-9: `Incumbent Equiv.` form `[A-01]: [named step from ≥5-step list + duration]`.]

**[A-05] PHASE GATE 1** — Tick before Operations:
- [ ] [A-01] first; ≥5 named steps with durations (SC-11 + [A-01] requirement)
- [ ] [A-02] SLA as integer; ≥2 entity names from [A-01]; SC-5 verbatim present
- [ ] Every stage in [A-03] has four columns per SC-7
- [ ] Every block in [A-04] has seven columns matching Part A headers
- [ ] Elapsed accumulates correctly (SC-3)
- [ ] Verdict FRESH or STALE (SC-4)
- [ ] Every Incumbent Equiv. cell: `[A-01]: [step + duration]` (SC-9)

Operations may not begin until all ✓. [SC-6]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 4: Goods receipt confirmation → Three-way match engine
- Stage 5: Three-way match result → Invoice verification

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend from [A-04] final.] [SC-4.] [SC-9: cite [A-01] step from ≥5-step list.]

**[A-08] PHASE GATE 2** — Tick before Commerce:
- [ ] Citing line: [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] has four columns per SC-7
- [ ] Every block in [A-07] has seven columns matching Part A
- [ ] Elapsed extends [A-04] final value (SC-3)
- [ ] Verdict from [A-02] threshold (SC-4)
- [ ] Incumbent Equiv.: `[A-01]: [step + duration]` (SC-9)
- [ ] [SC-12]: Commerce's `Citing:` line must include `[A-04]`. Position distance two.
  Mark ✗ if absent.

Commerce may not begin until all ✓. [SC-6]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] per SC-12 — two positions prior. Position distance is two.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 6: Verified invoice → Payment run processor
- Stage 7: Payment run batch → ERP AP ledger posting
- Stage 8: AP ledger entry → Commerce supplier portal update

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3, SC-4, SC-9 apply. SC-9: cite [A-01] step from ≥5-step list at every cell.]

**[A-11] STALE ANALYSIS** — Final Elapsed from [A-10] vs [A-02] threshold.
Normal-operation and failure-mode rows. Cite [A-02] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Formula:
`Fall back to [A-01] if [specific failure condition]`. Every no-handling flag and every
Data Loss Flag YES gets a named recovery. Because [A-01] has ≥5 named steps, map each
recovery to the specific manual step it falls back to.

**[A-13] INCUMBENT TOTAL** — [Per Part B. Per SC-10.] Immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited (from [A-01]) |
|------|--------------------------|--------------------------|
| Finance | | |
| Operations | | |
| Commerce | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] [Per Part B. Per SC-8.]
Tokens [A-01], [A-02], [A-13] required. Because [A-01] has ≥5 steps, the trade-off must
reference [A-01] total duration as the numeric baseline. ≥1 alternative pattern.
≥2 dimensions using [A-13] Grand Total as comparison endpoint.

---

---

## V-05

**Axis**: Combined — non-natural role sequence + lifecycle emphasis depth (C-48 + C-49)

**Hypothesis**: Operations → Commerce → Finance; digital advertising spend reporting
pipeline. Finance runs last and must cite Operations' boundary artifacts [A-04] two
positions prior (SC-12). A Phase Gate 0 (pre-artifact setup verification) is added as a
third phase gate, requiring the ARTIFACT REGISTRY, REGISTER DECLARATION, BOUNDARY BLOCK
SCHEMA, and STRUCTURAL CONSTRAINTS to be complete before any role begins. Phase Gate 0
is a first-class registry artifact ([A-00]). The exhaustive closed-chain paragraph
covers SC-1 through SC-13 with governed tokens and enforcement mechanisms; SC-12's
entry names [A-04] as the governed token and Phase Gate 2 enforcement by SC number
(C-48 + C-49). The added lifecycle gate tests whether C-48/C-49 compliance is maintained
under deeper structural scaffolding. Tabular register.

---

You are tracing data through a digital advertising spend reporting pipeline — ad impression
events through campaign performance aggregation to Finance budget reconciliation. Three
expert roles run in the sequence **Operations → Commerce → Finance**. Operations establishes
the event ingestion SLA and the manual campaign reporting baseline that all subsequent
roles must cite.

Finance runs last and must cite Operations' boundary artifacts [A-04] directly — two
positions prior in the Operations → Commerce → Finance sequence — as a required skip-level
citation. A Finance `Citing:` line naming only Commerce's artifacts without Operations'
boundary checks fails SC-12. Phase Gate 2 verifies this by citing SC-12 by number.

A **Phase Gate 0** precedes all role output. Phase Gate 0 verifies that the setup
artifacts (ARTIFACT REGISTRY, REGISTER DECLARATION, BOUNDARY BLOCK SCHEMA, STRUCTURAL
CONSTRAINTS) are complete and compliant before any role begins. Phase Gate 0 is
registered as [A-00] and must pass before ROLE 1 may begin.

The physical pipeline flows: ad impression event stream → event validation service →
deduplication buffer → campaign performance aggregation engine → budget pacing calculator
→ Finance budget reconciliation API → GL spend ledger → executive spend dashboard.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first (per SC-11); [A-00]
Phase Gate 0 is produced immediately after setup sections and before [A-01]. Every
citation uses `[A-xx]` tokens exactly. Prose references without tokens are violations.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-00] | PHASE GATE 0 | Setup | Pre-role setup verification checklist; confirms ARTIFACT REGISTRY, REGISTER DECLARATION, BOUNDARY BLOCK SCHEMA, STRUCTURAL CONSTRAINTS are complete; all ✓ required before [A-01] |
| [A-01] | INCUMBENT BASELINE | Operations | Manual campaign spend reporting workflow replaced; ≥3 named steps with durations; produced FIRST among role artifacts (after [A-00]). SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, event ingestion SLA (immutable after Stage 1), downstream consumer, business cadence; SLA from [A-01] total duration |
| [A-03] | STAGE TRACE — Operations | Operations | Ad impression stream → event validation → deduplication buffer → campaign aggregation engine; stage tables per SC-7 |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; required skip-level target for Finance (SC-12) |
| [A-05] | PHASE GATE 1 | Operations | Post-Operations self-verification checklist; all ✓ before Commerce |
| [A-06] | STAGE TRACE — Commerce | Commerce | Campaign aggregation → budget pacing calculator → spend forecast feed; stage tables |
| [A-07] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends Elapsed from [A-04] |
| [A-08] | PHASE GATE 2 | Commerce | Post-Commerce checklist; all ✓ before Finance; item [SC-12] verifies Finance skip-level citation |
| [A-09] | STAGE TRACE — Finance | Finance | Spend forecast feed → Finance budget reconciliation API → GL spend ledger → executive dashboard; stage tables |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends Elapsed from [A-07] |
| [A-11] | STALE ANALYSIS | Finance | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery per loss/no-handling item; formula: `Fall back to [A-01] if [condition]`; SC-13 applies |
| [A-13] | INCUMBENT TOTAL | Finance | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Finance | Required section; cites [A-01], [A-02], [A-13]; SC-13 applies |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell form)
and C-35 (INCUMBENT TOTAL section format).**

**Exhaustive closed verification chain** — every SC listed with its governed artifact
tokens and enforcement mechanism:

**SC-1 CITATION OPENER** governs [A-06], [A-09] (all non-first role outputs); enforced
by token-match at each non-first role's opening `Citing:` line — absent or prose-only
back-reference fails by line-structure check.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] and [A-04], [A-07],
[A-10]; enforced by inline lock at every stage advance — Stage N+1 may not be written
until the preceding boundary table is fully populated; gate fires per-transition.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (`Elapsed (cumul.)` column);
enforced by Part A column requirement — absent column or zero-reset fails by column-header
and cell-value check.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (`Verdict` column); enforced by
Part A string requirement — value must be exactly `FRESH` or `STALE`; any other string
fails by value check.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; enforced by verbatim phrase requirement
— exact phrase required; absence or paraphrase fails by phrase-match.

**SC-6 PHASE GATE OBLIGATION** governs [A-00], [A-05] and [A-08] (all three phase gates);
enforced by gating callback at every phase and role transition — an unchecked item in any
phase gate blocks the next output; detectable at the transition boundary.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09] (`Stage Latency` column);
enforced by Part A column requirement — absent column fails by header-match.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14]; enforced by three-token check —
`[A-01]`, `[A-02]`, `[A-13]` all required; absence of any token fails by token-match.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] (`Incumbent Equiv.`
column); enforced by Part A cell-form requirement — `[A-01]: [named step + duration]`
required; bare duration without token fails by token-match.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13]; enforced by Part B ordering
requirement — [A-13] immediately before [A-14]; Grand Total row required; verified by
artifact-order and row-structure check.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01]; enforced by positional lock — [A-01]
is the first role artifact produced (after [A-00] setup gate); any stage trace or boundary
block before [A-01] fails by artifact-order check.

**SC-12 SKIP-LEVEL CITATION IN FINANCE** governs [A-04] (Operations' boundary checks)
via Finance's `Citing:` line; enforced by the Phase Gate 2 checklist item citing [SC-12]
by number — Finance's `Citing:` line must include `[A-04]`; absence is detectable by
token-match at the Finance role opener without reading role body. Finance occupies
position 3; Operations occupies position 1; the position distance is two.

**SC-13 BASELINE CLOSURE** governs [A-12] (RECOVERY PRESCRIPTIONS) and [A-14]
(TRADE-OFF ANALYSIS); enforced by inline callbacks at both [A-12] and [A-14] section
headers that verify `[A-01]` citation by token match without output-prose inspection.

Together, SC-1 through SC-13, plus Phase Gate 0 gated by SC-6, form a complete closed
verification chain: every structural failure mode is navigable from this paragraph by
token match.

**Part A — Field compliance markers:**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric cumulative sum, minutes | Partial sum; reset |
| Freshness verdict | `Verdict` | Exactly `FRESH` or `STALE` | Any other value |
| Error handling | `Error Handling` | Named mechanism or `no handling — see [A-12]` | Silence; absent |
| Schema change | `Schema Delta` | Named changes or `NONE` | Absent |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named step + duration]` | Bare duration; token absent |
| Stage latency | `Stage Latency` | Explicit value, range, or characterization | Inferred |

**Part B — Section format compliance markers:**

| Required Section | Header | Required Content | Disqualifying Form |
|------------------|--------|------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Rows Operations/Commerce/Finance + Grand Total; subtotals numeric | Missing role row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | [A-01], [A-02], [A-13] tokens; ≥1 alternative; ≥2 dimensions | Token absent |

---

### BOUNDARY BLOCK SCHEMA

Every boundary block: markdown table with columns in order:

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

Headers must match Part A exactly.

---

### STRUCTURAL CONSTRAINTS

**SC-1 through SC-13** — As described in REGISTER DECLARATION closed-chain paragraph.
Per-transition callbacks:
[Apply SC-1 at every non-first role opener.]
[Apply SC-2 before every stage advance.]
[Apply SC-3 at every boundary block.]
[Apply SC-4 at every boundary block.]
[Apply SC-5 in [A-02].]
[Apply SC-6 before every phase gate and role transition, including [A-00].]
[Apply SC-7 at every stage block.]
[Apply SC-8 at [A-14].]
[Apply SC-9 at every boundary block.]
[Apply SC-10 before [A-14].]
[Apply SC-11 before Stage 1.]
[Apply SC-12 at Finance role opener and Phase Gate 2.]
[Apply SC-13 at [A-12] and [A-14].]

---

### PHASE GATE 0 [A-00] — Setup Verification

Before any role begins, verify that all setup sections are complete:
- [ ] ARTIFACT REGISTRY produced with all 15 rows (tokens [A-00] through [A-14]); all
  token names, owners, and descriptions present
- [ ] REGISTER DECLARATION produced; Parts A and B complete; closed-chain paragraph
  lists all SC-1 through SC-13 entries with governed artifact tokens and enforcement
  mechanisms (C-48, C-49)
- [ ] BOUNDARY BLOCK SCHEMA produced; 7 columns named; header strings match Part A exactly
- [ ] STRUCTURAL CONSTRAINTS produced; SC-1 through SC-13 present; each with inline
  callback directive

All items must be ✓ before ROLE 1 — Operations begins.

---

### ROLE 1 — Operations

[Operations runs first. No Citing line. [A-01] leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — First role artifact. Describe manual campaign spend
reporting workflow replaced. ≥3 named steps with durations (e.g., "Campaign operations
analyst exports impression data from three DSP portals into a unified Excel pivot table:
90 min", "Finance analyst manually calculates budget pacing by cost center from exported
totals: 60 min", "Budget manager reviews spend vs. plan in spreadsheet and sends email
report to executives: 45 min"). Entity names to reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — ≥2 entity names from [A-01]: ad impression event, validation
record, deduplication key, campaign aggregate, budget pacing signal, spend forecast,
GL spend entry, executive dashboard metric. Business cadence (e.g., hourly budget pacing
reports; daily GL close). Event ingestion SLA: integer with unit from [A-01] total.
SC-5 verbatim append required.

**[A-03] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 1: Ad impression event stream → Event validation service
- Stage 2: Validated events → Deduplication buffer
- Stage 3: Deduplicated events → Campaign aggregation engine

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3, SC-4, SC-9 apply.]

**[A-05] PHASE GATE 1** — Tick before Commerce:
- [ ] [A-01] first role artifact; ≥3 named steps with durations (SC-11)
- [ ] [A-02] SLA as integer; ≥2 names from [A-01]; SC-5 verbatim present
- [ ] Every stage in [A-03] has four columns per SC-7
- [ ] Every block in [A-04] has seven columns matching Part A headers
- [ ] Elapsed (cumul.) accumulates correctly in [A-04] (SC-3)
- [ ] Verdict FRESH or STALE (SC-4)
- [ ] Incumbent Equiv.: `[A-01]: [step + duration]` (SC-9)

Commerce may not begin until all ✓. [SC-6]

---

### ROLE 2 — Commerce

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 4: Campaign aggregation engine → Budget pacing calculator
- Stage 5: Budget pacing signal → Spend forecast feed

**[A-07] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend from [A-04] final.] [SC-4.] [SC-9.]

**[A-08] PHASE GATE 2** — Tick before Finance:
- [ ] Citing line: [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] has four columns per SC-7
- [ ] Every block in [A-07] has seven columns matching Part A headers
- [ ] Elapsed extends [A-04] final (SC-3)
- [ ] Verdict from [A-02] threshold (SC-4)
- [ ] Incumbent Equiv.: `[A-01]: [step + duration]` (SC-9)
- [ ] [SC-12]: Finance's `Citing:` line must include `[A-04]` — Operations' boundary
  checks, two positions prior in Operations → Commerce → Finance. Position distance is
  two: Finance = pos 3, Operations = pos 1. Mark ✗ if [A-04] absent.

Finance may not begin until all ✓. [SC-6]

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] per SC-12 — Operations' boundary checks, two positions prior. Position distance
is two: Finance = pos 3, Operations = pos 1.)

**[A-09] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 6: Spend forecast feed → Finance budget reconciliation API
- Stage 7: Reconciled budget → GL spend ledger posting
- Stage 8: GL spend entry → Executive spend dashboard

**[A-10] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend from [A-07].] [SC-4.] [SC-9.]

**[A-11] STALE ANALYSIS** — Final Elapsed from [A-10] vs [A-02] threshold.
Normal-operation and failure-mode rows. Cite [A-02] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Formula:
`Fall back to [A-01] if [specific failure condition]`. Every no-handling flag and every
YES Data Loss Flag gets a named recovery action citing [A-01].

**[A-13] INCUMBENT TOTAL** — [Per Part B. Per SC-10.] Immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Operations | | |
| Commerce | | |
| Finance | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] [Per Part B. Per SC-8.]
Tokens [A-01], [A-02], [A-13] required. ≥1 alternative pattern. ≥2 dimensions using
[A-13] Grand Total as numeric comparison endpoint.
