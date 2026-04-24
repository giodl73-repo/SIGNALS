# flow-dataflow — Round 19 Variations

## R18 gap summary before writing

**C-54 target for R19**: V-05 introduced Phase Gate 0 ([A-00]) as a structural pre-condition
before Role 1. The phase gate carries an explicit checklist item requiring the model to verify
DETECTABILITY INDEX row count = SC count before any role output is produced. C-54 mandates
this gate universally: any prompt declaring a DETECTABILITY INDEX (per C-52) must attach Phase
Gate 0 to [A-00] with an explicit row-count verification item. A DETECTABILITY INDEX without
Phase Gate 0 attached relies on author discipline and does not satisfy C-54. An [A-00] that
contains the index table but omits the Phase Gate 0 checklist item at the end fails C-54.

**C-55 target for R19**: V-05 introduced SC-0 to govern [A-00] itself as a first-class
artifact. SC-0 names [A-00] in both its governed-artifact slot and its enforcement clause,
making the DETECTABILITY INDEX subject to the same dual-slot anchoring (C-53) that governs
all content SCs. C-55 requires SC-0 as a mandatory SC in every prompt that carries [A-00]:
SC-0 must name [A-00] in both the governed-artifact position and the enforcement clause. An
SC governing [A-00] that omits [A-00] from its enforcement clause is a single-slot violation
for the index-governing SC and fails C-55.

Both C-54 and C-55 apply globally across all output format modes.

## Variation axes

- **V-01**: Lifecycle emphasis — Phase Gate 0 + SC-0 as clean reference, natural F→O→C;
  pharmaceutical distributor PO-to-revenue pipeline; 14 SCs (SC-0 through SC-13).

- **V-02**: Role sequence — non-natural O→C→F; energy utility smart-meter-to-cash pipeline;
  Phase Gate 0 + SC-0; skip-level citation crosses domain-role boundary (Finance pos 3 cites
  Operations [A-04] pos 1); 14 SCs.

- **V-03**: Output format — prose register (SC-14 FORMAT MODE DECLARATION); SaaS subscription
  usage-to-deferred-revenue pipeline; natural F→O→C; Phase Gate 0 described as numbered
  prose pre-condition; DETECTABILITY INDEX as prose enumeration; 14 SCs.

- **V-04**: Role sequence + inertia framing — non-natural C→F→O; retail inventory
  shrinkage-to-GL pipeline; max incumbent ≥7 named manual steps in Commerce's [A-01];
  Phase Gate 0 + SC-0; skip-level Operations (pos 3) cites Commerce [A-04] (pos 1); 14 SCs.

- **V-05**: Lifecycle emphasis + role sequence — non-natural O→F→C; CPG trade-promotion
  deduction-to-settlement pipeline; 15 SCs (SC-0 through SC-14); Phase Gate 0 multi-item
  (row count = 15 AND all rows have non-empty Responsible Role column); 3-column
  DETECTABILITY INDEX (SC | Violation Detectable At | Responsible Role); SC-14 ROLE
  ASSIGNMENT governs [A-00]'s third column; commerce (pos 3) cites Operations [A-04]
  (pos 1) skip-level.

---

## V-01

**Axis**: Lifecycle emphasis — Phase Gate 0 + SC-0 as clean reference implementation

**Hypothesis**: Finance → Operations → Commerce; pharmaceutical distributor
purchase-order-to-revenue pipeline. [A-00] DETECTABILITY INDEX is the first-class artifact
produced before any role output. Phase Gate 0 fires as the final checklist item of [A-00],
requiring the model to verify row count = 14 before Role 1 begins. SC-0 governs [A-00] with
dual-slot anchoring — [A-00] appears in both SC-0's governed-artifact slot and enforcement
clause. The 14-row DETECTABILITY INDEX is self-consistent: SC-0's own entry in the index
declares that SC-0 violations are detectable from the [A-00] row count and Phase Gate 0
checklist item before any role content is read. Commerce (pos 3) cites Finance [A-04]
(pos 1) skip-level; Phase Gate 2 item cites SC-12 by number.

---

You are tracing data through a pharmaceutical distributor purchase-order-to-revenue pipeline
— hospital pharmacy PO receipt through cold-chain 3PL fulfillment, DEA compliance
validation, and invoice-to-AR-to-revenue posting. Three expert roles run in the sequence
**Finance → Operations → Commerce**. Finance establishes the manual PO-processing and DEA
compliance-check baseline that all subsequent roles must cite. Operations handles cold-chain
fulfillment tracking; Commerce handles AR posting and revenue analytics.

Produce [A-00] DETECTABILITY INDEX before any role output. Phase Gate 0 is appended to
[A-00] and must be verified before Role 1 begins. Commerce runs last and must cite Finance's
boundary artifacts directly — two positions prior in the Finance → Operations → Commerce
sequence — as a required skip-level citation. A Commerce `Citing:` line naming only
Operations' artifacts without Finance's boundary checks fails SC-12. Phase Gate 2 verifies
this requirement by citing SC-12 by number.

The physical pipeline flows: hospital pharmacy PO portal → PO receipt service → DEA
compliance validator → cold-chain fulfillment service → 3PL dispatch tracker → delivery
confirmation service → invoice generation service → AR posting service → revenue analytics
dashboard.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-00] is produced FIRST — before any role
output, stage trace, or boundary block. Phase Gate 0 is appended to [A-00] and must be
verified ✓ before Role 1 begins. Every citation must use the `[A-xx]` token exactly as
spelled here. A citation to a token not listed here is a protocol violation.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-00] | DETECTABILITY INDEX | Pre-role | 14-row machine-scannable table (SC-0 through SC-13) with violation-detectability location per SC; Phase Gate 0 appended after the table; produced FIRST, before any role output. SC-0 applies. |
| [A-01] | INCUMBENT BASELINE | Finance | Manual PO-processing and DEA compliance-check workflow; ≥3 named steps with durations; produced first within Role 1. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Finance | Entity vocabulary, order-fill SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration. |
| [A-03] | STAGE TRACE — Finance | Finance | PO portal → PO receipt → DEA compliance validator → invoice staging; stage tables per SC-7. |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01]; required skip-level target for Commerce (SC-12). |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all items ✓ before Operations begins. SC-6 applies. |
| [A-06] | STAGE TRACE — Operations | Operations | Cold-chain fulfillment → 3PL dispatch → delivery confirmation; stage tables per SC-7. |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends Elapsed (cumul.) from [A-04]; Incumbent Equiv. cells cite [A-01]. |
| [A-08] | PHASE GATE 2 | Operations | Self-verification checklist; item [SC-12] verifies Commerce skip-level citation. SC-6 applies. |
| [A-09] | STAGE TRACE — Commerce | Commerce | Invoice generation → AR posting → revenue analytics dashboard; stage tables per SC-7. |
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

**Exhaustive closed verification chain** — every SC (SC-0 through SC-13) listed with its
governed artifact tokens, enforcement mechanism, and violation detectability location:

**SC-0 DETECTABILITY INDEX GATE** governs [A-00] (DETECTABILITY INDEX); enforced by
Phase Gate 0 row-count check appended to [A-00] — the model must verify row count = 14
before Role 1 begins; a [A-00] with fewer than 14 rows or a [A-00] missing the Phase Gate 0
checklist item is a protocol violation, and the violation is detectable from the [A-00] table
row count and Phase Gate 0 item before any role content is read.

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

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (`Elapsed (cumul.)` column);
enforced by Part A column requirement — a boundary block with a missing column or a
zero-reset value fails, and the violation is detectable at the column-header and cell-value
level without reading row prose.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (`Verdict` column); enforced by
Part A string requirement — any cell value other than exactly `FRESH` or exactly `STALE`
fails, and the violation is detectable at the cell-value level without reading surrounding
prose.

**SC-5 STALENESS IMMUTABILITY** governs [A-02] (DOMAIN CONTEXT); enforced by verbatim
phrase requirement — absence of the exact phrase "This threshold is fixed. No subsequent
role may revise it after Stage 1 is written." in [A-02] fails, and the violation is
detectable by phrase-match scan within [A-02]'s body without searching other sections.

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08] (phase gates); enforced by a
gating callback at every role transition — an unchecked [A-05] or [A-08] item blocks the
next role block, and the violation is detectable at the role-boundary line before reading
any role content.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09] (`Stage Latency` column);
enforced by Part A column requirement — a stage table missing the `Stage Latency` column
fails, and the violation is detectable at the table-header row without reading row contents.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] requiring [A-01], [A-02], and [A-13]
as mandatory citation tokens; enforced by a three-token check — absence of any of [A-01],
[A-02], [A-13] in [A-14] is a protocol violation detectable from [A-14]'s citation token
list without prose interpretation.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] (`Incumbent Equiv.`
column) requiring [A-01] in every cell; enforced by Part A cell-form requirement — a cell
lacking the `[A-01]` token is a protocol violation detectable at the cell level without
reading surrounding prose.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] in relation to [A-14]; enforced
by Part B ordering requirement — [A-13] must appear immediately before [A-14] and carry a
Grand Total row; the violation is detectable by artifact-order check at the [A-14] header
position without reading cell values.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] as the required first artifact within
Role 1; enforced by a positional lock — any output before [A-01] within Role 1 is a
positional protocol violation detectable from the Role 1 artifact-order head without reading
artifact content.

**SC-12 SKIP-LEVEL CITATION IN COMMERCE** governs [A-04] (Finance's boundary checks) via
Commerce's `Citing:` line; enforced by Phase Gate 2 checklist item citing [SC-12] by number
— absence of `[A-04]` in Commerce's `Citing:` line is a protocol violation detectable by
token-match at the Commerce role-opener line without reading the role body. Commerce occupies
position 3; Finance occupies position 1; the position distance is two.

**SC-13 BASELINE CLOSURE** governs [A-12] and [A-14] requiring [A-01] in both; enforced by
inline callbacks at both section headers — a [A-12] or [A-14] header lacking the [A-01]
token is a protocol violation detectable from the header line alone.

Together, SC-0 through SC-13 form a complete closed verification chain: every structural
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
REGISTER DECLARATION Part A spellings exactly.

**Every boundary block must be a markdown table with these columns, in this order:**

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

A column absent, renamed, or not matching Part A header strings fails the schema.

---

### DETECTABILITY INDEX

Standalone section declared before STRUCTURAL CONSTRAINTS. Produced as [A-00] before any
role output. Every SC in this prompt (SC-0 through SC-13) appears as exactly one row.
**Row count = 14 = SC count.** A DETECTABILITY INDEX with fewer than 14 rows is incomplete
and fails C-52. Evaluators locate violations using this index without reading SC prose bodies.

| SC | Violation Detectable At |
|----|------------------------|
| SC-0 | [A-00] table row count and presence of Phase Gate 0 checklist item — verified before any role content is read |
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
| SC-11 | The Role 1 artifact-order head — no artifact content reading required |
| SC-12 | Commerce role-opener `Citing:` line — no role body reading required |
| SC-13 | The [A-12] and [A-14] section header lines — no section body reading required |

**Phase Gate 0** — Verify before Role 1 begins. Mark ✓ or ✗:
- [ ] DETECTABILITY INDEX has exactly 14 rows (SC-0 through SC-13). Mark ✗ and halt if fewer than 14 rows.

---

### STRUCTURAL CONSTRAINTS

**SC-0 — DETECTABILITY INDEX gate**: [A-00] DETECTABILITY INDEX must be produced before any
role output. Phase Gate 0 appended to [A-00] must carry an explicit checklist item verifying
row count = 14. A [A-00] with fewer than 14 rows or without a Phase Gate 0 checklist item is
a protocol violation. [Apply SC-0 when producing [A-00].]

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
all prior stage and boundary latencies. It may not be deferred to [A-11]. A zero-reset value
is a protocol violation. [Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` in [A-04], [A-07], [A-10] = `FRESH` or `STALE`,
derived by comparing Elapsed (cumul.) against the [A-02] threshold. Any other value is a
protocol violation. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Finance appends to [A-02] verbatim: "This threshold is fixed. No
subsequent role may revise it after Stage 1 is written." Absence of this exact phrase is a
protocol violation.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required outputs. Each is a
checklist; every item must be ticked ✓ or ✗. An unchecked [A-05] item blocks Operations;
an unchecked [A-08] item blocks Commerce. [Apply SC-6 before every role transition.]

**SC-7 — Stage table format**: Every stage block in [A-03], [A-06], [A-09] is a markdown
table with columns `Stage Latency | Schema In | Schema Out | Data Loss Flag`. A stage table
missing the `Stage Latency` column is a protocol violation. [Apply SC-7 at every stage.]

**SC-8 — Trade-off as required section**: [A-14] TRADE-OFF ANALYSIS is a required named
section. Tokens [A-01], [A-02], and [A-13] must all appear in [A-14]. ≥1 alternative pattern.
≥2 trade-off dimensions. Omitting any of [A-01], [A-02], [A-13] from [A-14] is a protocol
violation. [Per REGISTER DECLARATION Part B.] [Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: Every `Incumbent Equiv.` cell in [A-04], [A-07],
[A-10] must use the form `[A-01]: [named manual step + duration]`. A cell lacking the
`[A-01]` token is a protocol violation. [Per REGISTER DECLARATION Part A.] [Apply SC-9 at
every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Produce [A-13] immediately before [A-14].
[A-13] sums all Incumbent Equiv. values from [A-04], [A-07], [A-10]; show additive breakdown
by role; Grand Total row required. [A-14] without a prior [A-13] is a protocol violation.
[Per REGISTER DECLARATION Part B.] [Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] INCUMBENT BASELINE must be the first artifact
written within Role 1. No boundary block and no stage trace may appear before [A-01] is
fully produced within Role 1. [Apply SC-11 at Role 1 start.]

**SC-12 — Skip-level citation in Commerce**: Commerce's `Citing:` line must include `[A-04]`
— Finance's boundary checks, produced two positions prior in the Finance → Operations →
Commerce sequence. A `Citing:` line naming only Operations' tokens without `[A-04]` fails
SC-12. Position distance is two: Commerce = position 3, Finance = position 1. A Phase Gate 2
item must cite [SC-12] by its numbered identifier. [Apply SC-12 at Commerce opener.]

**SC-13 — BASELINE CLOSURE**: [A-01] must appear as a citation token in [A-12] RECOVERY
PRESCRIPTIONS and in [A-14] TRADE-OFF ANALYSIS. Every recovery formula must include `[A-01]`.
[A-12] without `[A-01]` is a protocol violation. [A-14] without `[A-01]` is a protocol
violation. [Per SC-13, cite [A-01] in [A-12].] [Per SC-13, cite [A-01] in [A-14].]

---

### PRE-ROLE PRODUCTION

Produce [A-00] DETECTABILITY INDEX before Role 1 begins. The table must have exactly 14 rows
(SC-0 through SC-13). After the table, append and verify Phase Gate 0. Role 1 may not begin
until Phase Gate 0 item is ✓.

---

### ROLE 1 — Finance

[Finance runs first. No Citing line required. Phase Gate 0 must be ✓ before this role
begins. [A-01] leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST within Role 1, before any stage trace or boundary
block. Describe the manual PO-processing and DEA compliance-check workflow this pipeline
replaces. Include ≥3 named manual steps with durations (e.g., "Finance coordinator manually
reviews pharmacy PO for formulary compliance and DEA schedule status: 40 min"; "Finance clerk
keys PO line items into ERP and attaches DEA 222 form scan: 25 min"; "Finance analyst
generates paper invoice and posts AR entry manually: 20 min"). Use entity names that will
reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 names from [A-01]): pharmacy PO, controlled substance line
  item, DEA 222 form, cold-chain manifest, 3PL dispatch record, delivery confirmation, AR
  entry, revenue analytics record
- Downstream consumer and business cadence (e.g., daily order-fill close by 20:00)
- Order-fill SLA: integer with unit, derived from [A-01] total manual duration plus
  acceptable pipeline latency headroom
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 1: Pharmacy PO portal → PO receipt service
- Stage 2: PO receipt → DEA compliance validator
- Stage 3: Validated PO → invoice staging service

**[A-04] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA. One block after each stage.
[SC-3: Elapsed (cumul.) starts at 0 and accumulates from Stage 1 latency.]
[SC-4: Verdict vs [A-02] threshold; do not restate the numeric threshold value.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named manual step + duration]`.]

**[A-05] PHASE GATE 1** — Produce and tick before Operations begins. Mark each ✓ or ✗:
- [ ] [A-01] produced first within Role 1; no stage trace or boundary block precedes it (SC-11)
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
- Stage 4: Invoice staging → cold-chain fulfillment service
- Stage 5: Cold-chain fulfillment → 3PL dispatch tracker
- Stage 6: 3PL dispatch → delivery confirmation service

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: Elapsed (cumul.) extends the final value in [A-04]; do not reset to zero.]
[SC-4: Verdict vs [A-02] threshold; do not redeclare threshold numeric value.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named manual step + duration]`.]

**[A-08] PHASE GATE 2** — Produce and tick before Commerce begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] has four required columns per SC-7
- [ ] Every block in [A-07] has seven columns; headers match REGISTER DECLARATION Part A
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] final value; not reset (SC-3)
- [ ] Every `Verdict` derives from [A-02] threshold; threshold not redeclared (SC-4)
- [ ] Every `Incumbent Equiv.` cell in [A-07]: `[A-01]: [named step + duration]` (SC-9)
- [ ] [SC-12]: Commerce's `Citing:` line must include `[A-04]` — Finance's boundary checks,
  two positions prior. Position distance is two: Commerce = position 3, Finance = position 1.
  Mark ✗ if [A-04] absent.

Commerce may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] is required per SC-12 — Finance's boundary checks, two positions prior in the
Finance → Operations → Commerce sequence. A `Citing:` line naming only [A-07] without
[A-04] is a protocol violation. Position distance is two.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 7: Delivery confirmation → invoice generation service
- Stage 8: Invoice → AR posting service
- Stage 9: AR entry → revenue analytics dashboard

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend Elapsed (cumul.) from [A-07] final value.]
[SC-4: Verdict vs [A-02] threshold.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named manual step + duration]`.]

**[A-11] STALE ANALYSIS** — Using final Elapsed (cumul.) from [A-10]:

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

Produce separate rows for normal-operation and failure-mode staleness. Cite [A-02] by token;
do not restate the numeric threshold value.

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

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01] in this section.] Header:
`### [A-14] TRADE-OFF ANALYSIS`. Required tokens in body: [A-01], [A-02], [A-13]. Named
alternative pattern. ≥2 explicitly stated trade-off dimensions. Absence of any of [A-01],
[A-02], [A-13] is a protocol violation.

---

---

## V-02

**Axis**: Role sequence — non-natural O→C→F, skip-level crosses domain boundary

**Hypothesis**: Operations → Commerce → Finance; energy utility smart-meter-to-cash pipeline.
Operations runs first and owns [A-01] (the manual meter-reading and billing baseline),
establishing the vocabulary and SLA. Commerce handles rated-event aggregation and invoice
generation; Finance handles GL posting and revenue recognition. Finance (pos 3) must cite
Operations' [A-04] boundary checks (pos 1) directly — skipping Commerce (pos 2) — as a
required skip-level citation. The non-natural ordering forces the skip-level citation to
cross from last role (Finance) back to first role (Operations), stressing C-53 dual-slot on
SC-12 where [A-04] belongs to Operations not Finance. Phase Gate 2 (produced by Commerce)
verifies that Finance will include [A-04] in its Citing line. Phase Gate 0 + SC-0 + 14 SCs.

---

You are tracing data through an energy utility smart-meter-to-cash pipeline — interval
meter-read capture through rated-event aggregation, invoice generation, and GL revenue
posting. Three expert roles run in the sequence **Operations → Commerce → Finance**.
Operations establishes the manual meter-read and billing baseline; Commerce handles interval
aggregation and invoice generation; Finance handles GL posting and revenue recognition.

Produce [A-00] DETECTABILITY INDEX before any role output. Phase Gate 0 must be verified
before Role 1 (Operations) begins. Finance runs last and must cite Operations' boundary
artifacts directly — two positions prior in the Operations → Commerce → Finance sequence —
as a required skip-level citation. A Finance `Citing:` line naming only Commerce's artifacts
without Operations' boundary checks fails SC-12. Phase Gate 2 verifies this requirement by
citing SC-12 by number.

The physical pipeline flows: smart meter → AMI head-end → interval data repository →
rated-event engine → billing aggregation service → invoice generation service → payment
posting service → GL journal entry service → revenue analytics ledger.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-00] is produced FIRST. Phase Gate 0 is
appended to [A-00] and must be verified before Role 1 begins.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-00] | DETECTABILITY INDEX | Pre-role | 14-row machine-scannable table (SC-0 through SC-13); Phase Gate 0 appended; produced FIRST before any role output. SC-0 applies. |
| [A-01] | INCUMBENT BASELINE | Operations | Manual meter-reading and hand-keyed billing workflow; ≥3 named steps with durations; produced first within Role 1. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, billing-cycle SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration. |
| [A-03] | STAGE TRACE — Operations | Operations | Smart meter → AMI head-end → interval data repository → rated-event engine; stage tables per SC-7. |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01]; required skip-level target for Finance (SC-12). |
| [A-05] | PHASE GATE 1 | Operations | Self-verification checklist; all items ✓ before Commerce begins. SC-6 applies. |
| [A-06] | STAGE TRACE — Commerce | Commerce | Rated-event engine → billing aggregation → invoice generation service; stage tables per SC-7. |
| [A-07] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends Elapsed (cumul.) from [A-04]; Incumbent Equiv. cells cite [A-01]. |
| [A-08] | PHASE GATE 2 | Commerce | Self-verification checklist; item [SC-12] verifies Finance skip-level citation. SC-6 applies. |
| [A-09] | STAGE TRACE — Finance | Finance | Payment posting → GL journal entry → revenue analytics ledger; stage tables per SC-7. |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends Elapsed (cumul.) from [A-07]; Incumbent Equiv. cells cite [A-01]. |
| [A-11] | STALE ANALYSIS | Finance | Normal-operation and failure-mode elapsed vs [A-02] threshold. |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery per loss point; formula: `Fall back to [A-01] if [condition]`; SC-13 applies. |
| [A-13] | INCUMBENT TOTAL | Finance | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14]. |
| [A-14] | TRADE-OFF ANALYSIS | Finance | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions; SC-8 and SC-13 apply. |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**This section is the sole authoritative reference for C-34 and C-35.**

**Exhaustive closed verification chain** — SC-0 through SC-13:

**SC-0 DETECTABILITY INDEX GATE** governs [A-00]; enforced by Phase Gate 0 row-count check
appended to [A-00] — verify row count = 14 before Role 1 begins; a [A-00] with fewer than
14 rows or missing Phase Gate 0 is a protocol violation detectable from [A-00] before any
role content is read.

**SC-1 CITATION OPENER** governs [A-06], [A-09]; enforced by token-match at each role's
opening `Citing:` line — omitting the `Citing:` line fails; detectable from the role-opener
line without reading the role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] and [A-04], [A-07],
[A-10]; enforced by inline lock — Stage N+1 may not be written until preceding boundary
table is complete; detectable at the stage-boundary position without inspecting stage content.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (`Elapsed (cumul.)`); enforced
by Part A column requirement — missing column or zero-reset fails; detectable at column-header
and cell-value level without reading row prose.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (`Verdict`); enforced by Part A
string requirement — any non-binary value fails; detectable at cell-value level without
reading surrounding prose.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; enforced by verbatim phrase requirement —
absence of "This threshold is fixed. No subsequent role may revise it after Stage 1 is
written." in [A-02] fails; detectable by phrase-match scan within [A-02] without searching
other sections.

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08]; enforced by gating callback —
unchecked item blocks next role; detectable at role-boundary line before reading role content.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09] (`Stage Latency`); enforced by
Part A column requirement — missing `Stage Latency` column fails; detectable at table-header
row without reading row contents.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] requiring [A-01], [A-02], [A-13];
enforced by three-token check — absence of any token in [A-14] fails; detectable from
[A-14] citation token list without prose interpretation.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10] requiring [A-01] in every
cell; enforced by Part A cell-form — a cell lacking `[A-01]` fails; detectable at cell level
without reading surrounding prose.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] in relation to [A-14]; enforced
by Part B ordering — [A-13] immediately before [A-14] with Grand Total; detectable by
artifact-order check at [A-14] header without reading cell values.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] as required first artifact within Role 1;
enforced by positional lock — any output before [A-01] within Role 1 fails; detectable from
Role 1 artifact-order head without reading content.

**SC-12 SKIP-LEVEL CITATION IN FINANCE** governs [A-04] (Operations' boundary checks) via
Finance's `Citing:` line; enforced by Phase Gate 2 item citing [SC-12] by number — absence
of `[A-04]` in Finance's `Citing:` line fails; detectable by token-match at Finance
role-opener without reading role body. Finance = position 3; Operations = position 1;
position distance is two.

**SC-13 BASELINE CLOSURE** governs [A-12] and [A-14] requiring [A-01] in both; enforced by
inline callbacks at [A-12] and [A-14] headers — missing [A-01] token in either header fails;
detectable from the header line alone.

Together, SC-0 through SC-13 form a complete closed verification chain.

**Part A — Field compliance markers:** (same column structure as V-01 Part A)

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum, in minutes | Partial sum; reset to zero |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE` | Any other value |
| Error handling | `Error Handling` | Named mechanism or `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level changes or `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` | Token omitted; column absent |
| Stage latency (stage table) | `Stage Latency` | Explicit value, range, or characterization | Inferred from boundary elapsed only |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Table: Operations, Commerce, Finance, Grand Total rows | Prose-only; missing row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | [A-01], [A-02], [A-13] present; ≥1 pattern; ≥2 dimensions | Any token absent |

---

### BOUNDARY BLOCK SCHEMA

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

Declared before any role output. Headers must match Part A spellings exactly.

---

### DETECTABILITY INDEX

Row count = 14 = SC count. Produced as [A-00] before any role output.

| SC | Violation Detectable At |
|----|------------------------|
| SC-0 | [A-00] row count and Phase Gate 0 checklist item — before any role content is read |
| SC-1 | Each non-first role's opening `Citing:` line — no role body reading required |
| SC-2 | Each stage-advance transition position — no stage content reading required |
| SC-3 | The `Elapsed (cumul.)` column header and cell-value level — no row prose required |
| SC-4 | The `Verdict` cell-value level — no surrounding prose required |
| SC-5 | Phrase-match scan within [A-02] body — no other sections required |
| SC-6 | The role-boundary line before each role block — no role content required |
| SC-7 | The stage table header row — no row contents required |
| SC-8 | The [A-14] citation token list — no prose interpretation required |
| SC-9 | The `Incumbent Equiv.` cell level — no surrounding prose required |
| SC-10 | The artifact-order position at [A-14] header — no cell value reading required |
| SC-11 | The Role 1 artifact-order head — no artifact content required |
| SC-12 | Finance role-opener `Citing:` line — no role body reading required |
| SC-13 | The [A-12] and [A-14] section header lines — no section body required |

**Phase Gate 0** — Verify before Role 1 begins:
- [ ] DETECTABILITY INDEX has exactly 14 rows (SC-0 through SC-13). Mark ✗ and halt if fewer than 14 rows.

---

### STRUCTURAL CONSTRAINTS

**SC-0 — DETECTABILITY INDEX gate**: [A-00] produced before any role output; Phase Gate 0
appended; row count = 14; absence of Phase Gate 0 or fewer than 14 rows is a protocol
violation. [Apply SC-0 when producing [A-00].]

**SC-1 — Citation opener**: Every role other than Operations opens with
`Citing: [A-xx], [A-yy], ...`. Citing [A-01] required in every non-first role. [Apply SC-1
at every non-first role opener.]

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until preceding
boundary table is fully populated per BOUNDARY BLOCK SCHEMA. [Apply SC-2 before every stage
advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` may not reset to zero. [Apply SC-3 at
every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` only. [Apply SC-4 at every
boundary block.]

**SC-5 — Immutability**: Operations appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written."

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required; every item ✓ or ✗;
unchecked item blocks next role. [Apply SC-6 before every role transition.]

**SC-7 — Stage table format**: Every stage block has columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. [Apply SC-7 at every stage.]

**SC-8 — Trade-off as required section**: [A-14] requires [A-01], [A-02], [A-13] tokens;
≥1 pattern; ≥2 dimensions. [Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: Every `Incumbent Equiv.` cell:
`[A-01]: [named manual step + duration]`. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [A-13] immediately before [A-14] with Grand
Total row. [Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] must be first artifact within Role 1. [Apply
SC-11 at Role 1 start.]

**SC-12 — Skip-level citation in Finance**: Finance's `Citing:` line must include `[A-04]`
— Operations' boundary checks, produced two positions prior. Commerce is Finance's immediate
predecessor; a `Citing:` line naming only Commerce's tokens without `[A-04]` fails SC-12.
Position distance is two: Finance = position 3, Operations = position 1. Phase Gate 2 item
must cite [SC-12] by number. [Apply SC-12 at Finance opener.]

**SC-13 — BASELINE CLOSURE**: [A-01] in [A-12] and [A-14]; every recovery formula includes
`[A-01]`. [Apply SC-13 at [A-12] and [A-14].]

---

### PRE-ROLE PRODUCTION

Produce [A-00] before Role 1 begins. Verify Phase Gate 0 ✓ before continuing.

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required.]

**[A-01] INCUMBENT BASELINE** — Describe the manual meter-reading and hand-keyed billing
workflow this pipeline replaces. ≥3 named steps with durations (e.g., "Field technician
reads analog meter and records kWh on paper route sheet: 8 min/meter"; "Billing clerk
manually transcribes meter reads into billing system and calculates usage delta: 15
min/account"; "Billing coordinator generates paper invoice and mails to customer: 20
min/batch"). Use entity names that will reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Include entity vocabulary (reuse ≥2 from [A-01]): interval read,
AMI packet, rated event, billing period, invoice, payment receipt, GL journal entry, revenue
ledger entry. Downstream consumer and billing-cycle cadence. Billing-cycle SLA: integer with
unit, derived from [A-01] total duration. Per SC-5, append verbatim: "This threshold is
fixed. No subsequent role may revise it after Stage 1 is written."

**[A-03] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 1: Smart meter → AMI head-end
- Stage 2: AMI head-end → interval data repository
- Stage 3: Interval data → rated-event engine

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: Elapsed (cumul.) from 0.] [SC-4: Verdict vs [A-02] threshold.]
[SC-9: every Incumbent Equiv.: `[A-01]: [named step + duration]`.]

**[A-05] PHASE GATE 1** — Mark each ✓ or ✗ before Commerce begins:
- [ ] [A-01] first in Role 1; no stage or boundary precedes it (SC-11)
- [ ] [A-01] has ≥3 named steps with durations
- [ ] [A-02] SLA as integer with unit from [A-01]; SC-5 phrase present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every [A-03] stage has four columns (SC-7)
- [ ] Every [A-04] block has seven columns per Part A
- [ ] Every `Elapsed (cumul.)` is numeric sum (SC-3)
- [ ] Every `Verdict` is FRESH or STALE (SC-4)
- [ ] Every `Incumbent Equiv.`: `[A-01]: [step + duration]` (SC-9)

Commerce may not begin until all ✓. [SC-6.]

---

### ROLE 2 — Commerce

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 4: Rated-event engine → billing aggregation service
- Stage 5: Billing aggregation → invoice generation service
- Stage 6: Invoice → payment posting service

**[A-07] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-04] final Elapsed.] [SC-4.] [SC-9: `[A-01]: [step + duration]`.]

**[A-08] PHASE GATE 2** — Mark each ✓ or ✗ before Finance begins:
- [ ] Citing names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every [A-06] stage has four columns (SC-7)
- [ ] Every [A-07] block has seven columns per Part A
- [ ] `Elapsed (cumul.)` extends [A-04] final value (SC-3)
- [ ] Every `Verdict` from [A-02] threshold (SC-4)
- [ ] Every `Incumbent Equiv.` in [A-07]: `[A-01]: [step + duration]` (SC-9)
- [ ] [SC-12]: Finance's `Citing:` line must include `[A-04]` — Operations' boundary
  checks, two positions prior. Position distance is two: Finance = position 3,
  Operations = position 1. Mark ✗ if [A-04] absent.

Finance may not begin until all ✓. [SC-6.]

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12 — Operations' boundary checks, two positions prior. Commerce is
Finance's immediate predecessor; citing only [A-07] without [A-04] is a protocol violation.
Position distance is two.)

**[A-09] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 7: Payment posting → GL journal entry service
- Stage 8: GL journal → revenue analytics ledger
- Stage 9: Revenue ledger → financial close aggregator

**[A-10] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-07] final Elapsed.] [SC-4.] [SC-9: `[A-01]: [step + duration]`.]

**[A-11] STALE ANALYSIS** —

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

Normal-operation and failure-mode rows. Cite [A-02] by token; do not restate numeric value.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Named recovery per loss
point. Formula: `Fall back to [A-01] if [specific condition]`. [A-01] token in every formula.

**[A-13] INCUMBENT TOTAL** — [SC-10.] Header: `### [A-13] INCUMBENT TOTAL`.

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Operations | | |
| Commerce | | |
| Finance | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] Header:
`### [A-14] TRADE-OFF ANALYSIS`. Tokens [A-01], [A-02], [A-13] required. ≥1 pattern. ≥2
dimensions.

---

---

## V-03

**Axis**: Output format — prose register, SC-14 FORMAT MODE DECLARATION

**Hypothesis**: Finance → Operations → Commerce; SaaS subscription usage-to-deferred-revenue
pipeline. Prose output format with SC-14 FORMAT MODE DECLARATION. DETECTABILITY INDEX
produced as [A-00] in numbered prose enumeration form rather than markdown table — 14 prose
items, one per SC. Phase Gate 0 is described as a numbered pre-condition check at the end
of [A-00]: model must count prose items and verify count = 14 before Role 1 begins. C-54
stress: does Phase Gate 0 survive prose format? The prose enumeration lacks column-explicit
detectability-location fields, reducing machine-scannability relative to V-01. C-55: SC-0
governs [A-00] in prose form with dual-slot anchoring. SC-14 FORMAT MODE DECLARATION maps
criterion substitutions for non-tabular output registers; REGISTER DECLARATION closed-chain
paragraph names SC-14 as navigation entry.

---

You are tracing data through a SaaS subscription usage-to-deferred-revenue pipeline —
usage event capture through metered aggregation, invoice generation, deferred revenue
recognition, and GL posting. Three expert roles run in the sequence
**Finance → Operations → Commerce**. Finance establishes the manual usage-tracking and
deferred-revenue spreadsheet baseline; Operations handles metered aggregation and invoice
generation; Commerce handles ASC 606 recognition and GL posting.

Produce [A-00] DETECTABILITY INDEX before any role output. Phase Gate 0 is appended to
[A-00] and must be verified before Role 1 begins. This prompt uses the **prose register**:
all stage and boundary content is delivered as structured paragraphs, not markdown tables.
SC-14 FORMAT MODE DECLARATION governs criterion substitutions for prose output sections.
Commerce runs last with skip-level citation per SC-12.

The physical pipeline flows: usage event emitter → event ingestion service → metered
aggregation service → invoice generation service → deferred revenue ledger → ASC 606
recognition engine → GL journal entry service → financial reporting dashboard.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-00] is produced FIRST as a numbered prose
enumeration. Phase Gate 0 is a numbered prose pre-condition appended after the enumeration.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-00] | DETECTABILITY INDEX | Pre-role | 14-item numbered prose enumeration (SC-0 through SC-13), one item per SC, each naming the SC identifier and its violation-detectability location; Phase Gate 0 appended as a numbered pre-condition item verifying item count = 14; produced FIRST. SC-0 applies. |
| [A-01] | INCUMBENT BASELINE | Finance | Manual usage-tracking and deferred-revenue spreadsheet workflow; ≥3 named steps with durations; produced first within Role 1. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Finance | Entity vocabulary, recognition-cycle SLA (immutable after Stage 1), downstream consumer, cadence; SLA from [A-01] total duration. |
| [A-03] | STAGE TRACE — Finance | Finance | Usage event emitter → ingestion service → metered aggregation; prose stage paragraphs per SC-7 (prose substitution). |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | Prose boundary paragraphs per SC-14 substitution; Incumbent Equiv. prose phrase cites [A-01]; skip-level target for Commerce (SC-12). |
| [A-05] | PHASE GATE 1 | Finance | Prose checklist before Operations begins. SC-6 applies. |
| [A-06] | STAGE TRACE — Operations | Operations | Metered aggregation → invoice generation → deferred revenue ledger; prose stage paragraphs. |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | Prose boundary paragraphs; extends elapsed from [A-04]; Incumbent Equiv. cites [A-01]. |
| [A-08] | PHASE GATE 2 | Operations | Prose checklist; item [SC-12] verifies Commerce skip-level citation. SC-6 applies. |
| [A-09] | STAGE TRACE — Commerce | Commerce | ASC 606 recognition engine → GL journal entry → reporting dashboard; prose stage paragraphs. |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | Prose boundary paragraphs; extends elapsed from [A-07]; Incumbent Equiv. cites [A-01]. |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold; prose paragraphs. |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point; formula phrase: `Fall back to [A-01] if [condition]`; SC-13 applies. |
| [A-13] | INCUMBENT TOTAL | Commerce | Prose paragraph summing all Incumbent Equiv. durations from [A-04], [A-07], [A-10] by role with Grand Total; immediately before [A-14]. |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions. |

---

### REGISTER DECLARATION

This output uses the **prose register** throughout (SC-14 FORMAT MODE DECLARATION governs).
Stage and boundary content is delivered as structured paragraphs; markdown tables are not
used for stage or boundary output sections.

**This section is the sole authoritative reference for C-34 (Incumbent Equiv. prose phrase
form) and C-35 (INCUMBENT TOTAL prose section form).**

**Exhaustive closed verification chain** — SC-0 through SC-14:

**SC-0 DETECTABILITY INDEX GATE** governs [A-00]; enforced by Phase Gate 0 item-count
check appended to [A-00] prose enumeration — verify item count = 14 before Role 1 begins;
a [A-00] with fewer than 14 items or missing the Phase Gate 0 pre-condition prose item is a
protocol violation detectable by counting [A-00] enumeration items before reading any role
content.

**SC-1 CITATION OPENER** governs [A-06], [A-09]; enforced by token-match at each role's
opening `Citing:` prose phrase — omitting the `Citing:` opener fails; detectable at the
role-opener line without reading role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs stage paragraphs and boundary paragraphs;
enforced by prose gate — each stage paragraph must be followed by a boundary paragraph
before the next stage paragraph begins; detectable at the stage-boundary sequence position
without reading prose content.

**SC-3 INCREMENTAL ELAPSED** governs boundary paragraphs (`elapsed (cumul.)` prose phrase);
enforced by prose phrase requirement — a boundary paragraph with no cumulative elapsed phrase
or a zero-reset value fails; detectable by searching for the phrase "elapsed (cumul.)" in
each boundary paragraph.

**SC-4 BINARY VERDICT** governs boundary paragraphs (`FRESH` or `STALE` prose phrase);
enforced by prose phrase requirement — any boundary paragraph with neither `FRESH` nor
`STALE` as a verdict token fails; detectable by scanning for FRESH/STALE tokens in each
boundary paragraph.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; enforced by verbatim phrase — absence of
"This threshold is fixed. No subsequent role may revise it after Stage 1 is written." in
[A-02] fails; detectable by phrase-match within [A-02].

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08]; enforced by gating — unchecked
item blocks next role; detectable at role-boundary position before reading role content.

**SC-7 STAGE TABLE FORMAT (prose substitution)** governs [A-03], [A-06], [A-09]; per SC-14
substitution: each stage paragraph must name Stage Latency as an explicit value, range, or
characterization; a stage paragraph with no latency statement fails; detectable by scanning
for latency language in each stage paragraph.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] requiring [A-01], [A-02], [A-13]
tokens; enforced by token scan — any absent token fails; detectable from [A-14] prose body
token scan without prose interpretation.

**SC-9 INCUMBENT EQUIV. CELL FORM (prose substitution)** governs boundary paragraphs per
SC-14 substitution: each boundary paragraph must contain the prose phrase
`[A-01]: [named manual step + duration]`; a boundary paragraph lacking `[A-01]` token fails;
detectable by token scan in each boundary paragraph.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] in relation to [A-14]; enforced
by ordering — [A-13] paragraph immediately before [A-14] paragraph with Grand Total phrase;
detectable by artifact-order check at [A-14] header.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] as first artifact within Role 1;
positional lock; detectable at Role 1 output head.

**SC-12 SKIP-LEVEL CITATION IN COMMERCE** governs [A-04] via Commerce's `Citing:` phrase;
enforced by Phase Gate 2 item citing [SC-12] — `[A-04]` absent from Commerce `Citing:`
prose fails; detectable at Commerce role-opener. Position distance = two.

**SC-13 BASELINE CLOSURE** governs [A-12] and [A-14] requiring [A-01] in both; header-line
token check; detectable from header lines alone.

**SC-14 FORMAT MODE DECLARATION** governs this prompt's non-tabular output registers;
enforced by this REGISTER DECLARATION — all criterion substitutions for prose mode are
defined here; a stage or boundary section rendered as a markdown table when the prose
register is declared fails; detectable from section rendering before reading content.

Together, SC-0 through SC-14 form a complete closed verification chain. SC-13 BASELINE
CLOSURE and SC-14 FORMAT MODE DECLARATION are each named navigation entries in this
closed-chain paragraph.

**Part A (prose substitutions) — Boundary paragraph required phrases:**
- `Entity:` — named entity from [A-02] vocabulary ("data" or "records" alone fails)
- `Elapsed (cumul.):` — numeric cumulative minutes
- `Verdict:` — exactly `FRESH` or exactly `STALE`
- `Error handling:` — named mechanism or `no handling — see [A-12]`
- `Schema delta:` — named field-level changes or `NONE`
- `Data loss:` — `YES — [loss point name]` or `NO`
- `Incumbent Equiv.:` — `[A-01]: [named manual step + duration]`

**Part B (prose substitutions) — Section format:**
- INCUMBENT TOTAL [A-13]: prose paragraph naming Finance subtotal, Operations subtotal,
  Commerce subtotal, and Grand Total as labeled numeric values
- TRADE-OFF ANALYSIS [A-14]: prose section containing tokens [A-01], [A-02], [A-13]; named
  alternative pattern; ≥2 explicitly stated dimensions

---

### BOUNDARY BLOCK SCHEMA

**Prose register.** Every boundary block is a structured paragraph containing all seven
required phrase labels from Part A, in any order. A boundary paragraph missing any required
phrase label fails the schema.

---

### DETECTABILITY INDEX

Produced as [A-00] as a numbered prose enumeration. Each item names the SC identifier and
its violation-detectability location. **Item count = 14 = SC count.** A DETECTABILITY INDEX
prose enumeration with fewer than 14 items fails C-52.

1. SC-0 — Detectable by counting [A-00] enumeration items and verifying Phase Gate 0 prose pre-condition item — before any role content is read.
2. SC-1 — Detectable at each non-first role's opening `Citing:` prose phrase — no role body reading required.
3. SC-2 — Detectable at the stage-boundary sequence position — no prose content reading required.
4. SC-3 — Detectable by scanning for "elapsed (cumul.)" phrase in each boundary paragraph — no surrounding prose required.
5. SC-4 — Detectable by scanning for FRESH/STALE token in each boundary paragraph — no surrounding prose required.
6. SC-5 — Detectable by phrase-match within [A-02] body — no other sections required.
7. SC-6 — Detectable at role-boundary position before reading role content.
8. SC-7 (prose substitution) — Detectable by scanning for latency statement in each stage paragraph — no other content required.
9. SC-8 — Detectable by token scan in [A-14] prose body — no prose interpretation required.
10. SC-9 (prose substitution) — Detectable by scanning for `[A-01]` token in each boundary paragraph — no surrounding prose required.
11. SC-10 — Detectable by artifact-order check at [A-14] header — no cell value reading required.
12. SC-11 — Detectable at Role 1 output head — no artifact content reading required.
13. SC-12 — Detectable at Commerce role-opener `Citing:` prose phrase — no role body reading required.
14. SC-13 — Detectable at [A-12] and [A-14] header lines — no section body reading required.

**Phase Gate 0 (prose pre-condition)**: Count the numbered items above. Verify item count = 14.
If count < 14, halt and do not begin Role 1. If count = 14, continue to Role 1.

---

### STRUCTURAL CONSTRAINTS

**SC-0 — DETECTABILITY INDEX gate**: [A-00] prose enumeration produced before Role 1; item
count = 14; Phase Gate 0 prose pre-condition appended. Fewer than 14 items or missing Phase
Gate 0 is a protocol violation. [Apply SC-0 when producing [A-00].]

**SC-1 — Citation opener**: Every non-Finance role begins with the prose phrase
`Citing: [A-xx], [A-yy], ...`. Prose back-references without the `Citing:` token fail.
[Apply SC-1 at every non-first role opener.]

**SC-2 — Stage-write progression gate**: Each stage paragraph must be followed by a boundary
paragraph before the next stage paragraph begins. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: Every boundary paragraph includes `Elapsed (cumul.):` as a
running numeric total; zero-reset fails. [Apply SC-3 at every boundary paragraph.]

**SC-4 — Binary verdict**: Every boundary paragraph contains `Verdict: FRESH` or
`Verdict: STALE`. Any other verdict token fails. [Apply SC-4 at every boundary paragraph.]

**SC-5 — Immutability**: Finance appends to [A-02] verbatim: "This threshold is fixed. No
subsequent role may revise it after Stage 1 is written."

**SC-6 — Phase gate obligation**: [A-05] and [A-08] prose checklists; every item ✓ or ✗;
unchecked item blocks next role. [Apply SC-6 before every role transition.]

**SC-7 — Stage paragraph format (prose substitution per SC-14)**: Every stage paragraph
names Stage Latency as an explicit value, range, or characterization. [Apply SC-7 at every
stage paragraph.]

**SC-8 — Trade-off as required section**: [A-14] requires [A-01], [A-02], [A-13] tokens; ≥1
pattern; ≥2 dimensions. [Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. phrase form (prose substitution per SC-14)**: Every boundary
paragraph's Incumbent Equiv. phrase: `[A-01]: [named manual step + duration]`. [Apply SC-9
at every boundary paragraph.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [A-13] paragraph immediately before [A-14]
with Grand Total labeled value. [Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] first within Role 1. [Apply SC-11 at Role 1
start.]

**SC-12 — Skip-level citation in Commerce**: Commerce `Citing:` prose phrase must include
`[A-04]`. Position distance = two. Phase Gate 2 item cites [SC-12] by number. [Apply SC-12
at Commerce opener.]

**SC-13 — BASELINE CLOSURE**: [A-01] token in [A-12] and [A-14]. [Apply SC-13 at [A-12] and
[A-14].]

**SC-14 — FORMAT MODE DECLARATION**: This prompt uses the prose register. All stage and
boundary output is produced as structured paragraphs with labeled phrases. A section rendered
as a markdown table when the prose register is declared is a protocol violation. Criterion
substitutions are defined in REGISTER DECLARATION Part A and Part B.

---

### PRE-ROLE PRODUCTION

Produce [A-00] as a numbered prose enumeration of 14 items. Append Phase Gate 0 prose
pre-condition. Count items and verify = 14 before Role 1 begins.

---

### ROLE 1 — Finance

[Finance first. No Citing line. [A-01] leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Describe manual usage-tracking and deferred-revenue
spreadsheet workflow. ≥3 named steps with durations (e.g., "Finance analyst manually queries
usage logs and enters monthly consumption per subscription into Excel: 60 min"; "Finance
accountant calculates deferred revenue schedule per ASC 606 in spreadsheet: 45 min";
"Finance coordinator posts manual journal entries for recognized and deferred revenue: 30
min"). Prose paragraphs. Entity names reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Prose paragraph. Entity vocabulary (reuse ≥2 from [A-01]): usage
event, subscription entitlement, metered unit, invoice, deferred revenue balance, recognition
schedule, GL journal entry, financial report. Downstream consumer and cadence. Recognition-
cycle SLA: integer with unit from [A-01] total. Per SC-5 verbatim phrase.

**[A-03] STAGE TRACE — Finance** — Per SC-7 (prose). Per SC-2.
- Stage 1 paragraph: Usage event emitter → event ingestion service (latency stated explicitly)
- Stage 2 paragraph: Ingestion → metered aggregation service
- Stage 3 paragraph: Aggregation → invoice generation service

**[A-04] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA (prose). One paragraph
after each stage. [SC-3.] [SC-4.] [SC-9: `[A-01]: [step + duration]` in Incumbent Equiv.
phrase.]

**[A-05] PHASE GATE 1** — Prose checklist before Operations begins:
- [ ] [A-01] first within Role 1 (SC-11)
- [ ] [A-01] ≥3 named steps with durations
- [ ] [A-02] SLA integer with unit; SC-5 phrase present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every [A-03] stage paragraph states latency (SC-7 prose)
- [ ] Every [A-04] boundary paragraph has all seven Part A phrase labels
- [ ] Every `Elapsed (cumul.):` is numeric running sum (SC-3)
- [ ] Every `Verdict:` is FRESH or STALE (SC-4)
- [ ] Every `Incumbent Equiv.:` is `[A-01]: [step + duration]` (SC-9 prose)

Operations may not begin until all ✓. [SC-6.]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Per SC-7 (prose). Per SC-2.
- Stage 4 paragraph: Invoice generation → deferred revenue ledger (latency explicit)
- Stage 5 paragraph: Deferred revenue → ASC 606 recognition engine
- Stage 6 paragraph: Recognition engine → GL journal entry service

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (prose). Extends
elapsed from [A-04] final value. [SC-3.] [SC-4.] [SC-9.]

**[A-08] PHASE GATE 2** — Prose checklist before Commerce begins:
- [ ] Citing names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every [A-06] stage paragraph states latency (SC-7 prose)
- [ ] Every [A-07] boundary paragraph has all seven Part A phrase labels
- [ ] `Elapsed (cumul.):` extends [A-04] final value (SC-3)
- [ ] Every `Verdict:` from [A-02] threshold (SC-4)
- [ ] Every [A-07] `Incumbent Equiv.:` `[A-01]: [step + duration]` (SC-9)
- [ ] [SC-12]: Commerce's `Citing:` prose phrase must include `[A-04]`. Position distance
  two: Commerce = 3, Finance = 1. Mark ✗ if [A-04] absent.

Commerce may not begin until all ✓. [SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12 — Finance boundary checks, two positions prior.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7 (prose). Per SC-2.
- Stage 7: GL journal entry → financial reporting dashboard (latency explicit)
- Stage 8: Reporting dashboard → period-close aggregator
- Stage 9: Period-close → audit trail archive

**[A-10] BOUNDARY CHECKS — Commerce** — Extends elapsed from [A-07]. [SC-3.] [SC-4.] [SC-9.]

**[A-11] STALE ANALYSIS** — Prose paragraphs for normal-operation and failure-mode elapsed
vs [A-02] threshold. Cite [A-02] token; do not restate numeric value.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Named prose recovery per loss
point. Formula phrase: `Fall back to [A-01] if [specific condition]`.

**[A-13] INCUMBENT TOTAL** — [SC-10.] Prose paragraph: Finance subtotal, Operations subtotal,
Commerce subtotal, and Grand Total labeled numeric values. Header: `### [A-13] INCUMBENT
TOTAL`. Produced immediately before [A-14].

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] Header: `### [A-14] TRADE-OFF
ANALYSIS`. Tokens [A-01], [A-02], [A-13] in prose body. ≥1 named alternative pattern. ≥2
explicitly stated trade-off dimensions.

---

---

## V-04

**Axis**: Role sequence + inertia framing — non-natural C→F→O, max incumbent ≥7 steps

**Hypothesis**: Commerce → Finance → Operations; retail inventory shrinkage-to-GL pipeline.
Commerce runs first and owns [A-01] (the manual shrinkage counting and GL posting baseline),
with ≥7 named manual steps that make the incumbent baseline the strongest framing element
in the prompt. Finance handles variance analysis and journal entry; Operations handles
corporate GL consolidation and analytics. Operations (pos 3) must cite Commerce's [A-04]
boundary checks (pos 1) directly — skipping Finance (pos 2) — as required skip-level
citation. Phase Gate 2 produced by Finance verifies that Operations will include [A-04].
Phase Gate 0 + SC-0 + 14 SCs. Maximum incumbent prominence stresses C-15 (baseline must
surface in C-09 trade-off) and C-08 (recovery formulas cite [A-01]).

---

You are tracing data through a retail inventory shrinkage-to-GL pipeline — store-level cycle
count capture through shrinkage variance analysis, markdown/write-off posting, and corporate
GL consolidation. Three expert roles run in the sequence **Commerce → Finance → Operations**.
Commerce establishes the manual cycle-count and shrinkage-posting baseline (≥7 named manual
steps). Finance handles variance analysis and journal entry approval; Operations handles
corporate GL consolidation and shrinkage analytics.

Produce [A-00] DETECTABILITY INDEX before any role output. Phase Gate 0 must be verified
before Role 1 (Commerce) begins. Operations runs last and must cite Commerce's boundary
artifacts directly — two positions prior in the Commerce → Finance → Operations sequence —
as a required skip-level citation. A Operations `Citing:` line naming only Finance's
artifacts without Commerce's boundary checks fails SC-12. Phase Gate 2 verifies this
requirement by citing SC-12 by number.

The physical pipeline flows: handheld cycle-count device → count upload service → shrinkage
calculation engine → variance approval service → markdown/write-off posting service → GL
journal entry service → intercompany reconciliation service → corporate GL consolidation →
shrinkage analytics dashboard.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-00] | DETECTABILITY INDEX | Pre-role | 14-row machine-scannable table (SC-0 through SC-13); Phase Gate 0 appended; produced FIRST. SC-0 applies. |
| [A-01] | INCUMBENT BASELINE | Commerce | Manual cycle-count and shrinkage-posting workflow; **≥7 named steps with durations**; produced first within Role 1. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Commerce | Entity vocabulary, shrinkage-close SLA (immutable after Stage 1), downstream consumer, cadence; SLA from [A-01] total duration. |
| [A-03] | STAGE TRACE — Commerce | Commerce | Cycle-count device → upload service → shrinkage calculation → variance approval; stage tables per SC-7. |
| [A-04] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cites [A-01]; required skip-level target for Operations (SC-12). |
| [A-05] | PHASE GATE 1 | Commerce | Self-verification checklist; ≥7 [A-01] steps verified; all ✓ before Finance begins. SC-6 applies. |
| [A-06] | STAGE TRACE — Finance | Finance | Variance approval → markdown/write-off posting → GL journal entry; stage tables per SC-7. |
| [A-07] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends Elapsed (cumul.) from [A-04]; Incumbent Equiv. cites [A-01]. |
| [A-08] | PHASE GATE 2 | Finance | Self-verification checklist; item [SC-12] verifies Operations skip-level citation. SC-6 applies. |
| [A-09] | STAGE TRACE — Operations | Operations | GL journal → intercompany reconciliation → corporate GL consolidation → shrinkage analytics; stage tables per SC-7. |
| [A-10] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends Elapsed (cumul.) from [A-07]; Incumbent Equiv. cites [A-01]. |
| [A-11] | STALE ANALYSIS | Operations | Normal-operation and failure-mode elapsed vs [A-02] threshold. |
| [A-12] | RECOVERY PRESCRIPTIONS | Operations | Named recovery; formula: `Fall back to [A-01] if [condition]`; SC-13 applies. |
| [A-13] | INCUMBENT TOTAL | Operations | Sum from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14]. |
| [A-14] | TRADE-OFF ANALYSIS | Operations | Cites [A-01], [A-02], [A-13]; ≥1 pattern; ≥2 dimensions; SC-8 and SC-13 apply. |

---

### REGISTER DECLARATION

Tabular register throughout.

**Exhaustive closed verification chain** — SC-0 through SC-13:

**SC-0 DETECTABILITY INDEX GATE** governs [A-00]; enforced by Phase Gate 0 row-count check
appended to [A-00] — verify row count = 14 before Role 1 begins; fewer than 14 rows or
missing Phase Gate 0 is a protocol violation detectable from [A-00] before any role content
is read.

**SC-1 CITATION OPENER** governs [A-06], [A-09]; enforced by token-match at each role's
opening `Citing:` line; detectable from the role-opener line without reading the role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] and [A-04], [A-07],
[A-10]; enforced by inline lock — Stage N+1 may not be written until preceding boundary
table is complete; detectable at stage-boundary position without inspecting stage content.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (`Elapsed (cumul.)`); missing
column or zero-reset fails; detectable at column-header and cell-value level.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (`Verdict`); non-binary value fails;
detectable at cell-value level.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; verbatim phrase "This threshold is fixed. No
subsequent role may revise it after Stage 1 is written." required; detectable by phrase-match
in [A-02].

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08]; unchecked item blocks next role;
detectable at role-boundary line.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09]; missing `Stage Latency` column
fails; detectable at table-header row.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] requiring [A-01], [A-02], [A-13];
token absence fails; detectable from [A-14] citation token list.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10]; `[A-01]` token required
in every cell; detectable at cell level.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] before [A-14]; [A-13] immediately
before [A-14] with Grand Total; detectable by artifact-order check at [A-14] header.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] as first within Role 1; detectable at
Role 1 artifact-order head.

**SC-12 SKIP-LEVEL CITATION IN OPERATIONS** governs [A-04] (Commerce's boundary checks) via
Operations' `Citing:` line; enforced by Phase Gate 2 item citing [SC-12] — `[A-04]` absent
from Operations' `Citing:` line fails; detectable at Operations role-opener. Operations =
position 3; Commerce = position 1; position distance = two.

**SC-13 BASELINE CLOSURE** governs [A-12] and [A-14] requiring [A-01] in both; detectable
from [A-12] and [A-14] header lines.

Together, SC-0 through SC-13 form a complete closed verification chain.

**Part A — Field compliance markers:**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum, in minutes | Partial sum; reset to zero |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE` | Any other value |
| Error handling | `Error Handling` | Named mechanism or `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level changes or `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` | Token omitted; column absent |
| Stage latency (stage table) | `Stage Latency` | Explicit value, range, or characterization | Inferred only |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Table: Commerce, Finance, Operations, Grand Total rows | Missing row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | [A-01], [A-02], [A-13] present; ≥1 pattern; ≥2 dimensions | Any token absent |

---

### BOUNDARY BLOCK SCHEMA

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

---

### DETECTABILITY INDEX

Row count = 14 = SC count.

| SC | Violation Detectable At |
|----|------------------------|
| SC-0 | [A-00] row count and Phase Gate 0 item — before any role content is read |
| SC-1 | Each non-first role's opening `Citing:` line — no role body reading required |
| SC-2 | Each stage-advance transition position — no stage content reading required |
| SC-3 | The `Elapsed (cumul.)` column header and cell-value level — no row prose required |
| SC-4 | The `Verdict` cell-value level — no surrounding prose required |
| SC-5 | Phrase-match scan within [A-02] body — no other sections required |
| SC-6 | The role-boundary line before each role block — no role content required |
| SC-7 | The stage table header row — no row contents required |
| SC-8 | The [A-14] citation token list — no prose interpretation required |
| SC-9 | The `Incumbent Equiv.` cell level — no surrounding prose required |
| SC-10 | The artifact-order position at [A-14] header — no cell values required |
| SC-11 | The Role 1 artifact-order head — no content reading required |
| SC-12 | Operations role-opener `Citing:` line — no role body reading required |
| SC-13 | The [A-12] and [A-14] section header lines — no section body required |

**Phase Gate 0** — Verify before Role 1 begins:
- [ ] DETECTABILITY INDEX has exactly 14 rows (SC-0 through SC-13). Mark ✗ and halt if fewer.

---

### STRUCTURAL CONSTRAINTS

**SC-0** — [A-00] before any role; Phase Gate 0 appended; row count = 14. [Apply SC-0 at
[A-00] production.]

**SC-1** — Every non-Commerce role opens with `Citing: [A-xx], ...]`. [Apply SC-1 at every
non-first role opener.]

**SC-2** — Stage N+1 only after boundary table fully populated. [Apply SC-2 before every
stage advance.]

**SC-3** — `Elapsed (cumul.)` never resets. [Apply SC-3 at every boundary block.]

**SC-4** — `Verdict` = `FRESH` or `STALE` only. [Apply SC-4 at every boundary block.]

**SC-5** — Commerce appends to [A-02] verbatim: "This threshold is fixed. No subsequent role
may revise it after Stage 1 is written."

**SC-6** — [A-05] and [A-08] checklists; unchecked item blocks next role. [Apply SC-6 before
every transition.]

**SC-7** — Every stage table has `Stage Latency | Schema In | Schema Out | Data Loss Flag`.
[Apply SC-7 at every stage.]

**SC-8** — [A-14] requires [A-01], [A-02], [A-13]; ≥1 pattern; ≥2 dimensions. [Apply SC-8
at [A-14].]

**SC-9** — Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]`. [Apply SC-9 at
every boundary block.]

**SC-10** — [A-13] immediately before [A-14]; Grand Total row required. [Apply SC-10 before
[A-14].]

**SC-11** — [A-01] first within Role 1. [Apply SC-11 at Role 1 start.]

**SC-12 — Skip-level citation in Operations**: Operations' `Citing:` line must include
`[A-04]` — Commerce's boundary checks, produced two positions prior in the
Commerce → Finance → Operations sequence. Finance is Operations' immediate predecessor; a
`Citing:` line naming only Finance's tokens without `[A-04]` fails SC-12. Position distance
is two: Operations = position 3, Commerce = position 1. Phase Gate 2 item must cite [SC-12]
by its numbered identifier. [Apply SC-12 at Operations opener.]

**SC-13** — [A-01] token in [A-12] and [A-14]. [Apply SC-13 at [A-12] and [A-14].]

---

### PRE-ROLE PRODUCTION

Produce [A-00] before Role 1 begins. Verify Phase Gate 0 ✓ before continuing.

---

### ROLE 1 — Commerce

[Commerce runs first. No Citing line required. Phase Gate 0 ✓ before this role. [A-01] first
per SC-11. INCUMBENT BASELINE must include ≥7 named manual steps — this is the maximum
incumbent framing across all variations.]

**[A-01] INCUMBENT BASELINE** — Write FIRST. Describe the manual cycle-count and
shrinkage-posting workflow this pipeline replaces. Include **≥7 named manual steps with
durations** that cumulatively represent the incumbent process (e.g., "Store associate
physically counts items in assigned zone and records on paper tally sheet: 45 min";
"Department manager cross-checks tally against printed on-hand report from POS: 30 min";
"Store manager reviews and approves variance for write-off against shrinkage policy: 20 min";
"Loss prevention coordinator documents root-cause note on paper shrinkage form: 15 min";
"Finance clerk transcribes approved variance into shrinkage tracking spreadsheet: 25 min";
"Finance analyst generates markdown/write-off posting request in accounting system: 20 min";
"Finance manager reviews and manually posts GL journal entry for shrinkage: 35 min"). Use
entity names that will reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Include entity vocabulary (reuse ≥2 from [A-01]): cycle count
record, on-hand quantity, shrinkage variance, write-off amount, markdown posting, GL journal
entry, intercompany charge, shrinkage analytics record. Downstream consumer and cadence.
Shrinkage-close SLA: integer with unit, derived from [A-01] total duration. Per SC-5 append
verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is
written."

**[A-03] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 1: Handheld cycle-count device → count upload service
- Stage 2: Count upload → shrinkage calculation engine
- Stage 3: Calculation → variance approval service

**[A-04] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: Elapsed from 0.] [SC-4.] [SC-9: `[A-01]: [named step + duration]`.]

**[A-05] PHASE GATE 1** — Mark ✓ or ✗:
- [ ] [A-01] first within Role 1 (SC-11)
- [ ] [A-01] includes **≥7 named manual steps** with durations
- [ ] [A-02] SLA from [A-01] total; SC-5 phrase present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every [A-03] stage has four columns (SC-7)
- [ ] Every [A-04] block has seven columns per Part A
- [ ] Every `Elapsed (cumul.)` is numeric sum (SC-3)
- [ ] Every `Verdict` is FRESH or STALE (SC-4)
- [ ] Every [A-04] `Incumbent Equiv.`: `[A-01]: [step + duration]` (SC-9)

Finance may not begin until all ✓. [SC-6.]

---

### ROLE 2 — Finance

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 4: Variance approval → markdown/write-off posting service
- Stage 5: Write-off posting → GL journal entry service
- Stage 6: GL journal → intercompany reconciliation service

**[A-07] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-04] final.] [SC-4.] [SC-9.]

**[A-08] PHASE GATE 2** — Mark ✓ or ✗:
- [ ] Citing names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every [A-06] stage has four columns (SC-7)
- [ ] Every [A-07] block has seven columns per Part A
- [ ] `Elapsed (cumul.)` extends [A-04] final (SC-3)
- [ ] Every `Verdict` from [A-02] threshold (SC-4)
- [ ] Every [A-07] `Incumbent Equiv.`: `[A-01]: [step + duration]` (SC-9)
- [ ] [SC-12]: Operations' `Citing:` line must include `[A-04]` — Commerce's boundary
  checks, two positions prior. Position distance = two: Operations = position 3,
  Commerce = position 1. Mark ✗ if [A-04] absent.

Operations may not begin until all ✓. [SC-6.]

---

### ROLE 3 — Operations

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12 — Commerce's boundary checks, two positions prior in the
Commerce → Finance → Operations sequence. Finance is Operations' immediate predecessor;
citing only [A-07] without [A-04] is a protocol violation. Position distance = two.)

**[A-09] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 7: GL journal → intercompany reconciliation → corporate GL consolidation
- Stage 8: Corporate GL → shrinkage analytics dashboard
- Stage 9: Analytics → period shrinkage report

**[A-10] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-07] final.] [SC-4.] [SC-9.]

**[A-11] STALE ANALYSIS** —

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Formula:
`Fall back to [A-01] if [specific condition]`. [A-01] token in every formula.

**[A-13] INCUMBENT TOTAL** — Header: `### [A-13] INCUMBENT TOTAL`.

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Commerce | | |
| Finance | | |
| Operations | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] Header: `### [A-14] TRADE-OFF
ANALYSIS`. Tokens [A-01], [A-02], [A-13] required. ≥1 pattern. ≥2 dimensions.

---

---

## V-05

**Axis**: Lifecycle emphasis + role sequence — non-natural O→F→C, 15 SCs, 3-column
DETECTABILITY INDEX, Phase Gate 0 multi-item

**Hypothesis**: Operations → Finance → Commerce; CPG manufacturer trade-promotion
deduction-to-settlement pipeline. 15 SCs (SC-0 through SC-14). SC-14 ROLE ASSIGNMENT governs
a third column added to the DETECTABILITY INDEX — `Responsible Role` — making the index a
3-column machine-scannable table. Phase Gate 0 carries two checklist items: (1) row count =
15, and (2) every row has a non-empty Responsible Role value. SC-0 governs [A-00] with
dual-slot anchoring; SC-14 governs the third column of [A-00] with dual-slot anchoring —
both SC-0 and SC-14 name [A-00] in their governed-artifact and enforcement slots. Commerce
(pos 3) must cite Operations' [A-04] boundary checks (pos 1) skip-level; Phase Gate 2 item
cites SC-12 by number. This is the deepest lifecycle variation: 15 SCs, 3-column index,
Phase Gate 0 with two structural pre-conditions.

---

You are tracing data through a CPG manufacturer trade-promotion deduction-to-settlement
pipeline — retailer deduction capture through trade fund matching, dispute resolution, GL
adjustment, and promotional analytics. Three expert roles run in the sequence
**Operations → Finance → Commerce**. Operations establishes the manual deduction
reconciliation baseline; Finance handles GL adjustment and fund settlement; Commerce handles
trade spend analytics and promotional ROI reporting.

Produce [A-00] DETECTABILITY INDEX before any role output. [A-00] is a 3-column table:
`SC | Violation Detectable At | Responsible Role`. Phase Gate 0 is appended to [A-00] and
carries two verification items before Role 1 begins: (1) row count = 15, and (2) every row
has a non-empty Responsible Role value. Commerce runs last and must cite Operations' boundary
artifacts directly — two positions prior in the Operations → Finance → Commerce sequence —
as a required skip-level citation.

The physical pipeline flows: retailer deduction notice → deduction intake service → trade
fund matching engine → dispute resolution service → GL adjustment posting service → trade
settlement service → fund balance ledger → promotional analytics service → trade ROI
dashboard.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-00] | DETECTABILITY INDEX | Pre-role | 3-column machine-scannable table (SC \| Violation Detectable At \| Responsible Role), 15 rows (SC-0 through SC-14); Phase Gate 0 appended with two verification items; produced FIRST. SC-0 and SC-14 apply. |
| [A-01] | INCUMBENT BASELINE | Operations | Manual deduction reconciliation workflow; ≥3 named steps with durations; produced first within Role 1. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, settlement-cycle SLA (immutable after Stage 1), downstream consumer, cadence; SLA from [A-01] total. |
| [A-03] | STAGE TRACE — Operations | Operations | Deduction intake → trade fund matching → dispute resolution; stage tables per SC-7. |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cites [A-01]; required skip-level target for Commerce (SC-12). |
| [A-05] | PHASE GATE 1 | Operations | Checklist before Finance begins. SC-6 applies. |
| [A-06] | STAGE TRACE — Finance | Finance | Dispute resolution → GL adjustment posting → trade settlement service; stage tables per SC-7. |
| [A-07] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends Elapsed (cumul.) from [A-04]; Incumbent Equiv. cites [A-01]. |
| [A-08] | PHASE GATE 2 | Finance | Checklist; item [SC-12] verifies Commerce skip-level citation. SC-6 applies. |
| [A-09] | STAGE TRACE — Commerce | Commerce | Trade settlement → fund balance ledger → promotional analytics → trade ROI dashboard; stage tables per SC-7. |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends Elapsed (cumul.) from [A-07]; Incumbent Equiv. cites [A-01]. |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold. |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery; formula: `Fall back to [A-01] if [condition]`; SC-13 applies. |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum from [A-04], [A-07], [A-10]; immediately before [A-14]. |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Cites [A-01], [A-02], [A-13]; ≥1 pattern; ≥2 dimensions; SC-8 and SC-13 apply. |

---

### REGISTER DECLARATION

Tabular register throughout.

**Exhaustive closed verification chain** — SC-0 through SC-14:

**SC-0 DETECTABILITY INDEX GATE** governs [A-00]; enforced by Phase Gate 0 two-item
verification appended to [A-00] — (1) row count = 15, (2) every row has non-empty
Responsible Role — a [A-00] failing either check is a protocol violation detectable from
[A-00] table structure before any role content is read.

**SC-1 CITATION OPENER** governs [A-06], [A-09]; enforced by token-match at each role's
`Citing:` line; detectable at role-opener without reading role body.

**SC-2 STAGE-WRITE PROGRESSION GATE** governs [A-03], [A-06], [A-09] and [A-04], [A-07],
[A-10]; enforced by inline lock — Stage N+1 only after preceding boundary table complete;
detectable at stage-boundary position.

**SC-3 INCREMENTAL ELAPSED** governs [A-04], [A-07], [A-10] (`Elapsed (cumul.)`); zero-reset
fails; detectable at column-header and cell-value level.

**SC-4 BINARY VERDICT** governs [A-04], [A-07], [A-10] (`Verdict`); non-binary value fails;
detectable at cell-value level.

**SC-5 STALENESS IMMUTABILITY** governs [A-02]; verbatim phrase required; detectable by
phrase-match in [A-02].

**SC-6 PHASE GATE OBLIGATION** governs [A-05] and [A-08]; unchecked item blocks next role;
detectable at role-boundary line.

**SC-7 STAGE TABLE FORMAT** governs [A-03], [A-06], [A-09]; missing `Stage Latency` column
fails; detectable at table-header row.

**SC-8 TRADE-OFF AS REQUIRED SECTION** governs [A-14] requiring [A-01], [A-02], [A-13];
token absence fails; detectable from [A-14] token list.

**SC-9 INCUMBENT EQUIV. CELL FORM** governs [A-04], [A-07], [A-10]; `[A-01]` token required
per cell; detectable at cell level.

**SC-10 INCUMBENT TOTAL BEFORE TRADE-OFF** governs [A-13] before [A-14]; Grand Total row
required; detectable by artifact-order check at [A-14] header.

**SC-11 BASELINE-FIRST PRODUCTION** governs [A-01] as first within Role 1; detectable at
Role 1 artifact-order head.

**SC-12 SKIP-LEVEL CITATION IN COMMERCE** governs [A-04] (Operations' boundary checks) via
Commerce's `Citing:` line; enforced by Phase Gate 2 item citing [SC-12] by number — `[A-04]`
absent from Commerce's `Citing:` line fails; detectable at Commerce role-opener. Commerce =
position 3; Operations = position 1; position distance = two.

**SC-13 BASELINE CLOSURE** governs [A-12] and [A-14] requiring [A-01] in both; detectable
from [A-12] and [A-14] header lines.

**SC-14 DETECTABILITY INDEX ROLE ASSIGNMENT** governs [A-00] (third column `Responsible Role`
in DETECTABILITY INDEX); enforced by a per-row non-empty check in [A-00] — any row with an
empty or absent `Responsible Role` value is a protocol violation, detectable from [A-00]
column cells before any role content is read.

Together, SC-0 through SC-14 form a complete closed verification chain. SC-14 DETECTABILITY
INDEX ROLE ASSIGNMENT is named here as a navigation entry alongside SC-0 DETECTABILITY INDEX
GATE — both govern [A-00], one for row count and Phase Gate 0, one for role assignment
completeness per row.

**Part A — Field compliance markers:**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum, in minutes | Partial sum; reset to zero |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE` | Any other value |
| Error handling | `Error Handling` | Named mechanism or `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level changes or `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` | Token omitted; column absent |
| Stage latency (stage table) | `Stage Latency` | Explicit value, range, or characterization | Inferred only |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Table: Operations, Finance, Commerce, Grand Total rows | Missing row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | [A-01], [A-02], [A-13] present; ≥1 pattern; ≥2 dimensions | Any token absent |

---

### BOUNDARY BLOCK SCHEMA

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

---

### DETECTABILITY INDEX

Standalone 3-column table. [A-00] produced before any role output. **Row count = 15 = SC
count.** Every row must have a non-empty `Responsible Role` value. A DETECTABILITY INDEX
with fewer than 15 rows or any row with empty Responsible Role fails C-52 and SC-14.

| SC | Violation Detectable At | Responsible Role |
|----|------------------------|-----------------|
| SC-0 | [A-00] row count, Phase Gate 0 items, and Responsible Role completeness — before any role content is read | Pre-role |
| SC-1 | Each non-first role's opening `Citing:` line — no role body reading required | Operations (enforcer: all non-first roles) |
| SC-2 | Each stage-advance transition position — no stage content reading required | All roles |
| SC-3 | The `Elapsed (cumul.)` column header and cell-value level — no row prose required | All roles |
| SC-4 | The `Verdict` cell-value level — no surrounding prose required | All roles |
| SC-5 | Phrase-match within [A-02] body — no other sections required | Operations |
| SC-6 | The role-boundary line before each role block — no role content required | Operations, Finance |
| SC-7 | The stage table header row — no row contents required | All roles |
| SC-8 | The [A-14] citation token list — no prose interpretation required | Commerce |
| SC-9 | The `Incumbent Equiv.` cell level — no surrounding prose required | All roles |
| SC-10 | The artifact-order position at [A-14] header — no cell value reading required | Commerce |
| SC-11 | The Role 1 artifact-order head — no content reading required | Operations |
| SC-12 | Commerce role-opener `Citing:` line — no role body reading required | Commerce |
| SC-13 | The [A-12] and [A-14] section header lines — no section body required | Commerce |
| SC-14 | Each [A-00] row's `Responsible Role` column cell — no row prose reading required | Pre-role |

**Phase Gate 0** — Verify before Role 1 begins. Mark each ✓ or ✗:
- [ ] DETECTABILITY INDEX has exactly 15 rows (SC-0 through SC-14). Mark ✗ and halt if fewer.
- [ ] Every row has a non-empty `Responsible Role` value. Mark ✗ and halt if any cell is empty.

---

### STRUCTURAL CONSTRAINTS

**SC-0 — DETECTABILITY INDEX gate**: [A-00] produced before any role output; Phase Gate 0
appended with two items — row count = 15 and every row has non-empty Responsible Role; both
items must be ✓ before Role 1 begins. Failure on either item is a protocol violation. [Apply
SC-0 when producing [A-00].]

**SC-1** — Every non-Operations role opens with `Citing: [A-xx], ...]`. [Apply SC-1 at every
non-first role opener.]

**SC-2** — Stage N+1 only after boundary table complete. [Apply SC-2 before every stage.]

**SC-3** — `Elapsed (cumul.)` never resets. [Apply SC-3 at every boundary block.]

**SC-4** — `Verdict` = `FRESH` or `STALE`. [Apply SC-4 at every boundary block.]

**SC-5** — Operations appends to [A-02] verbatim: "This threshold is fixed. No subsequent
role may revise it after Stage 1 is written."

**SC-6** — [A-05] and [A-08] checklists; unchecked item blocks next role. [Apply SC-6.]

**SC-7** — Every stage table: `Stage Latency | Schema In | Schema Out | Data Loss Flag`.
[Apply SC-7 at every stage.]

**SC-8** — [A-14] requires [A-01], [A-02], [A-13]. [Apply SC-8 at [A-14].]

**SC-9** — Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]`. [Apply SC-9.]

**SC-10** — [A-13] immediately before [A-14]; Grand Total required. [Apply SC-10.]

**SC-11** — [A-01] first within Role 1. [Apply SC-11 at Role 1 start.]

**SC-12 — Skip-level citation in Commerce**: Commerce's `Citing:` line must include `[A-04]`
— Operations' boundary checks, produced two positions prior. Finance is Commerce's immediate
predecessor; citing only [A-07] without [A-04] fails SC-12. Position distance = two:
Commerce = position 3, Operations = position 1. Phase Gate 2 item must cite [SC-12] by
number. [Apply SC-12 at Commerce opener.]

**SC-13** — [A-01] in [A-12] and [A-14]. [Apply SC-13 at [A-12] and [A-14].]

**SC-14 — DETECTABILITY INDEX ROLE ASSIGNMENT**: Every row in [A-00] must have a non-empty
`Responsible Role` value in the third column. A row with an empty or absent Responsible Role
value is a protocol violation. [Apply SC-14 when producing [A-00].]

---

### PRE-ROLE PRODUCTION

Produce [A-00] as a 3-column table with 15 rows (SC-0 through SC-14). After the table,
append Phase Gate 0 and verify both items ✓ before Role 1 begins.

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required. Phase Gate 0 must show both items ✓. [A-01]
leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST within Role 1. Describe manual deduction
reconciliation workflow (e.g., "Operations analyst downloads retailer remittance advice and
manually matches deductions to open trade promotions in spreadsheet: 90 min"; "Operations
coordinator calls retailer deduction desk to verify claim codes: 45 min"; "Operations manager
approves dispute list and routes to Finance for GL adjustment: 30 min"). ≥3 named steps. Use
entity names reappearing in [A-02].

**[A-02] DOMAIN CONTEXT** — Entity vocabulary (≥2 from [A-01]): deduction notice, trade
promotion plan, fund balance, dispute claim, GL adjustment, trade settlement payment,
promotional ROI record. Downstream consumer and settlement cadence. Settlement-cycle SLA:
integer with unit from [A-01] total. Append SC-5 phrase verbatim.

**[A-03] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 1: Retailer deduction notice → deduction intake service
- Stage 2: Intake → trade fund matching engine
- Stage 3: Fund matching → dispute resolution service

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: Elapsed from 0.] [SC-4.] [SC-9: `[A-01]: [step + duration]`.]

**[A-05] PHASE GATE 1** — Mark ✓ or ✗:
- [ ] [A-01] first within Role 1 (SC-11)
- [ ] [A-01] ≥3 named steps with durations
- [ ] [A-02] SLA integer with unit; SC-5 phrase present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every [A-03] stage has four columns (SC-7)
- [ ] Every [A-04] block has seven columns per Part A
- [ ] `Elapsed (cumul.)` numeric sum (SC-3)
- [ ] `Verdict` FRESH or STALE (SC-4)
- [ ] [A-04] `Incumbent Equiv.`: `[A-01]: [step + duration]` (SC-9)

Finance may not begin until all ✓. [SC-6.]

---

### ROLE 2 — Finance

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 4: Dispute resolution → GL adjustment posting service
- Stage 5: GL adjustment → trade settlement service
- Stage 6: Trade settlement → fund balance ledger

**[A-07] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-04] final.] [SC-4.] [SC-9.]

**[A-08] PHASE GATE 2** — Mark ✓ or ✗:
- [ ] Citing names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every [A-06] stage has four columns (SC-7)
- [ ] Every [A-07] block has seven columns per Part A
- [ ] `Elapsed (cumul.)` extends [A-04] final (SC-3)
- [ ] `Verdict` from [A-02] threshold (SC-4)
- [ ] [A-07] `Incumbent Equiv.`: `[A-01]: [step + duration]` (SC-9)
- [ ] [SC-12]: Commerce's `Citing:` line must include `[A-04]` — Operations' boundary
  checks, two positions prior. Position distance = two: Commerce = position 3,
  Operations = position 1. Mark ✗ if [A-04] absent.

Commerce may not begin until all ✓. [SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12 — Operations' boundary checks, two positions prior. Finance is
Commerce's immediate predecessor; citing only [A-07] without [A-04] is a protocol violation.
Position distance = two.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 7: Fund balance ledger → promotional analytics service
- Stage 8: Analytics → trade ROI dashboard
- Stage 9: ROI dashboard → period trade spend report

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-07] final.] [SC-4.] [SC-9.]

**[A-11] STALE ANALYSIS** —

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01].] Formula:
`Fall back to [A-01] if [specific condition]`. [A-01] in every formula.

**[A-13] INCUMBENT TOTAL** — Header: `### [A-13] INCUMBENT TOTAL`.

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Operations | | |
| Finance | | |
| Commerce | | |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01].] Header: `### [A-14] TRADE-OFF
ANALYSIS`. Tokens [A-01], [A-02], [A-13] required. ≥1 named alternative pattern. ≥2
explicitly stated trade-off dimensions.
