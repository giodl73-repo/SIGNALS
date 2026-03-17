# flow-dataflow — Round 15 Variations

## R14 gap summary before writing

**C-46 target for R15**: R14 variations declared SC-13 BASELINE CLOSURE in STRUCTURAL
CONSTRAINTS but did not universally treat the closed-chain paragraph as a mandatory
navigation index for SC-13. R14 V-01 updated the paragraph to name SC-13 as a fourth
path — but this was a one-off execution decision, not a design-first commitment. C-46
requires that SC-13 BASELINE CLOSURE appear as a named navigation entry in the
REGISTER DECLARATION closed-chain paragraph at the moment SC-13 is introduced, making
baseline-closure failures reachable from the register index without scanning STRUCTURAL
CONSTRAINTS. The SC-13 entry in the closed-chain paragraph must identify SC-13 as the
governing authority and name the two enforcement sites ([A-12] and [A-14]).

**C-47 target for R15** (non-tabular variants only): R14 V-02 named SC-14 in the
closed-chain paragraph. C-47 formalizes this: for any non-tabular variation, SC-14
FORMAT MODE DECLARATION must be a named navigation entry in the closed-chain paragraph
identifying it as the governing authority for format-mode compliance failures.

## Variation axes

- **V-01**: Role sequence (C-46) — Finance → Operations → Commerce; freight billing
  and logistics cost allocation pipeline. SC-13 named in closed-chain paragraph as
  fourth navigation path. Commerce (pos 3) cites Finance [A-04] (pos 1) skip-level.
  Tabular register.

- **V-02**: Output format (C-46 + C-47) — Finance → Commerce → Operations; energy
  trade booking to settlement pipeline. Prose register. SC-13 + SC-14 both named in
  closed-chain paragraph as named navigation entries. Operations (pos 3) cites Finance
  [A-04] (pos 1) skip-level.

- **V-03**: Lifecycle emphasis (C-46) — Commerce → Finance → Operations; SaaS
  subscription revenue recognition pipeline with 4 stages per role (12 stages total,
  9 boundary blocks). Tabular register. SC-13 in closed-chain paragraph. Higher boundary
  density stress-tests SC-13's inline callbacks across a longer elapsed chain. Operations
  (pos 3) cites Commerce [A-04] (pos 1) skip-level.

- **V-04**: Combined (role sequence + inertia framing, C-46) — Operations → Commerce →
  Finance; pharmaceutical raw material procurement-to-payment pipeline. Maximum inertia
  prominence: [A-01] requires ≥5 named manual steps with durations. SC-13 in closed-chain
  paragraph. Finance (pos 3) cites Operations [A-04] (pos 1) skip-level. Tabular register.

- **V-05**: Combined (output format + phrasing register, C-46 + C-47) — Operations →
  Finance → Commerce; federal contracting requisition-to-payment pipeline. Prose register
  + imperative second-person voice throughout. SC-13 + SC-14 both named in closed-chain
  paragraph. Commerce (pos 3) cites Operations [A-04] (pos 1) skip-level.

---

## V-01

**Axis**: Role sequence — SC-13 closed-chain paragraph entry (C-46)

**Hypothesis**: Finance → Operations → Commerce; freight billing and logistics cost
allocation pipeline. SC-13 BASELINE CLOSURE is declared in STRUCTURAL CONSTRAINTS and
simultaneously registered in the REGISTER DECLARATION closed-chain paragraph as the
fourth named navigation path — alongside Parts A/B and SC-12 — at the time of SC-13's
introduction. This makes baseline-closure failures discoverable from the register index
without a sequential scan of STRUCTURAL CONSTRAINTS. Commerce (pos 3) cites Finance
[A-04] two positions prior (SC-12, C-43). Tabular register.

---

You are tracing data through a freight billing and logistics cost allocation pipeline —
carrier invoice receipt to cost center ledger posting. Three expert roles run in the
sequence **Finance → Operations → Commerce**. Finance establishes the cost allocation
SLA and the manual invoice-processing baseline that all subsequent roles must cite.
Operations and Commerce cite Finance's artifacts by token; they may not redeclare or
re-derive either.

Commerce runs last and must cite Finance's boundary artifacts directly — two positions
prior in the Finance → Operations → Commerce sequence — as a required skip-level
citation. A Commerce `Citing:` line that names only Operations' artifacts without
Finance's boundary checks fails SC-12. Phase Gate 2 verifies this requirement by
citing SC-12 by number before Commerce may begin.

The physical pipeline flows: carrier invoice receipt → invoice validation service →
freight audit engine → cost allocation processor → GL journal entry → cost center
ledger posting → management reporting feed.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first; all subsequent
artifacts are produced in token order. Every citation anywhere in this output must use
the `[A-xx]` token exactly as spelled in this table. A citation to a target not listed
here is a protocol violation.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Finance | Manual freight invoice processing and cost allocation workflow replaced by this pipeline; ≥3 named steps with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Finance | Entity vocabulary, cost allocation SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Finance | Finance | Carrier invoice receipt → invoice validation → freight audit engine → cost allocation processor; stage tables per SC-7 |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01]; required skip-level target for Commerce |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all items ✓ before Operations begins |
| [A-06] | STAGE TRACE — Operations | Operations | Cost allocation processor → GL journal entry → cost center ledger posting; stage tables |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Operations | Self-verification checklist; all items ✓ before Commerce begins; item [SC-12] verifies Commerce skip-level citation |
| [A-09] | STAGE TRACE — Commerce | Commerce | Cost center ledger posting → management reporting feed → executive cost dashboard; stage tables |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cells cite [A-01] |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point and no-handling annotation; formula: `Fall back to [A-01] if [condition]`; SC-13 applies |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions; SC-13 applies |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout. All stage blocks and boundary
blocks are rendered as markdown tables.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell
form) and C-35 (INCUMBENT TOTAL section format). An evaluator may determine pass/fail
for both criteria by reading this section alone. SC-9 and SC-10 are callbacks to Parts A
and B respectively; they do not independently restate compliance requirements.**

**Closed verification chain**: Every failed Phase Gate item in this output cites its
governing structural constraint by number in the item text. Part A is the governing
authority for every C-34 (`Incumbent Equiv.` column) failure. Part B is the governing
authority for every C-35 (INCUMBENT TOTAL) failure. SC-12 is the governing authority for
every skip-level citation failure; its Phase Gate 2 item cites [SC-12] by number.
**SC-13 BASELINE CLOSURE is the governing authority for every baseline-closure failure
in [A-12] and [A-14]**; its inline callbacks at both section headers enforce the
[A-01] citation obligation by token match without output-prose inspection. Together,
Parts A/B, the SC-12 Phase Gate 2 item, and SC-13's paired inline callbacks form a
complete closed chain: every structural failure mode has a named navigation path to its
governing SC reachable from this paragraph.

**Part A — Field compliance markers (boundary block columns):**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum of all prior stage and boundary latencies, in minutes | Partial sum; deferred total |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE`, derived from [A-02] threshold | Any other value |
| Error handling | `Error Handling` | Named retry/dead-letter/rollback, or exactly `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level changes, or exactly `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` — `[A-01]` token required | Bare duration; token omitted; column absent |
| Stage latency | `Stage Latency` (stage table) | Explicit value, range, or characterization | Inferred from boundary elapsed only |

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
do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding
BOUNDARY CHECK table is fully populated per BOUNDARY BLOCK SCHEMA. Write the table.
Confirm all seven columns are populated. Then write Stage N+1. [Apply SC-2 before every
stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` is computed inside each boundary
block as the sum of all prior stage latencies and all prior boundary latencies. It may
not be deferred to [A-11]. [Per REGISTER DECLARATION Part A, `Elapsed (cumul.)` row.]
[Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE`, derived by comparing
Elapsed (cumul.) against the [A-02] threshold. Cite [A-02] by token; do not restate its
numeric value. [Per REGISTER DECLARATION Part A, `Verdict` row.] [Apply SC-4 at every
boundary block.]

**SC-5 — Immutability**: Finance appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written." Declare as an integer with
unit, derived from [A-01] total manual duration plus acceptable pipeline latency headroom.

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
REGISTER DECLARATION as the fourth navigation path in the closed-chain paragraph;
evaluators navigate to it from the closed-chain paragraph without searching STRUCTURAL
CONSTRAINTS. [Per SC-13, cite [A-01] in [A-12].] [Per SC-13, cite [A-01] in [A-14].]

---

### ROLE 1 — Finance

[Finance runs first. No Citing line required. The incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST, before any domain context or stage trace.
Per SC-11: no boundary block and no stage trace may appear before [A-01] is fully
produced. Describe the manual freight invoice processing and cost allocation workflow
this pipeline replaces. Include ≥3 named manual steps with durations (e.g., "Logistics
coordinator manually enters carrier invoice line items into cost allocation spreadsheet:
120 min", "Finance analyst reviews and approves freight cost allocations by cost center:
90 min", "Accountant manually posts approved allocations to GL journal: 60 min"). Use
entity names that will reappear in [A-02]. This is the source for every `Incumbent
Equiv.` cell in [A-04], [A-07], [A-10].

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 names from [A-01]): carrier invoice, validation record,
  freight audit result, cost allocation entry, GL journal entry, cost center ledger
  line, management reporting feed
- Downstream consumer and business cadence (e.g., weekly cost reporting close every
  Friday at 18:00 ET)
- Cost allocation SLA: integer with unit, derived from [A-01] total manual duration
  plus acceptable pipeline latency headroom
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 1: Carrier invoice receipt → Invoice validation service
- Stage 2: Validated invoice → Freight audit engine
- Stage 3: Audited invoice → Cost allocation processor

**[A-04] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA. One block between
Stage 1–Stage 2; one block between Stage 2–Stage 3; one block after Stage 3.
[SC-3, SC-4, SC-9 / Part A apply.]

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
- Stage 4: Cost allocation entry → GL journal entry creation
- Stage 5: GL journal entry → Cost center ledger posting

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: Elapsed (cumul.) extends the final value in [A-04]; do not reset to zero.]
[SC-4: Verdict vs [A-02] threshold; do not redeclare threshold numeric value.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named step + duration]`.]

**[A-08] PHASE GATE 2** — Produce and tick before Commerce begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] has four required columns per SC-7
- [ ] Every block in [A-07] has seven columns; headers match REGISTER DECLARATION Part A
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] final value; not reset (SC-3)
- [ ] Every `Verdict` derives from [A-02] threshold; threshold value not redeclared (SC-4)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)
- [ ] [SC-12]: Commerce's `Citing:` line must include `[A-04]` — Finance's boundary
  checks, two positions prior in the Finance → Operations → Commerce sequence. A
  `Citing:` line naming only Operations' tokens without `[A-04]` fails SC-12. Mark ✗
  if [A-04] is absent from Commerce's Citing line.

Commerce may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] is required per SC-12 — Finance's boundary checks, two positions prior in the
Finance → Operations → Commerce sequence. Operations is Commerce's immediate predecessor;
citing only [A-07] without [A-04] fails SC-12.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 6: Cost center ledger posting → Management reporting feed consolidation
- Stage 7: Management reporting feed → Executive cost dashboard publication

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend Elapsed (cumul.) from [A-07] final value.]
[SC-4: Verdict vs [A-02] threshold.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named step + duration]`.]

**[A-11] STALE ANALYSIS** — Using final Elapsed (cumul.) from [A-10]:

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

Produce separate rows for normal-operation and failure-mode staleness. Cite [A-02] by
token; do not restate the numeric threshold value.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01] in this section.] For
every `no handling — see [A-12]` annotation in [A-04]/[A-07]/[A-10] and every
`Data Loss Flag: YES` in [A-03]/[A-06]/[A-09], provide a specific named recovery action.
Required formula: `Fall back to [A-01] if [specific named failure condition]`. Cite
[A-01] using this formula at least once. SC-13 requires [A-01] to appear as a citation
token in this section; absence is a protocol violation.

**[A-13] INCUMBENT TOTAL** — [Per REGISTER DECLARATION Part B. Per SC-10.] Produce
immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Finance | [sum of [A-04] values] | [step names from [A-01]] |
| Operations | [sum of [A-07] values] | [step names from [A-01]] |
| Commerce | [sum of [A-10] values] | [step names from [A-01]] |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01] in this section.] [Per
REGISTER DECLARATION Part B. Per SC-8.] Required named section. Cite `[A-01]` (manual
baseline), `[A-02]` (SLA dimension), and `[A-13]` (numeric incumbent total) — all three
tokens required. SC-13 requires [A-01] to appear as a citation token in this section.
Name ≥1 alternative data propagation pattern. Provide ≥2 trade-off dimensions using
[A-13] Grand Total as the numeric comparison endpoint.

---

---

## V-02

**Axis**: Output format — prose register with C-46 + C-47 closed-chain paragraph entries

**Hypothesis**: Finance → Commerce → Operations; energy trade booking to settlement
pipeline. Prose register. SC-13 BASELINE CLOSURE is named in the closed-chain paragraph
as the governing authority for baseline-closure failures (C-46). SC-14 FORMAT MODE
DECLARATION is named in the closed-chain paragraph as the governing authority for
format-mode compliance failures (C-47). Both are named navigation entries in the register
index — not just declarations in STRUCTURAL CONSTRAINTS. Operations (pos 3) cites Finance
[A-04] skip-level per SC-12.

---

You are tracing data through an energy trade booking to settlement pipeline — trade
entry to counterparty payment. Three expert roles run in the sequence
**Finance → Commerce → Operations**. Finance establishes the settlement SLA and the
manual trade confirmation baseline that all subsequent roles must cite. Commerce and
Operations cite Finance's artifacts by token; they may not redeclare or re-derive either.

Operations runs last and must cite Finance's boundary artifacts directly — two positions
prior in the Finance → Commerce → Operations sequence — as a required skip-level
citation. An Operations `Citing:` line that names only Commerce's artifacts without
Finance's boundary checks fails SC-12. Phase Gate 2 verifies this by citing SC-12 by
number before Operations may begin.

The physical pipeline flows: trade order entry → position validation service →
credit limit check → trade confirmation engine → settlement instruction generation →
nostro account funding → counterparty payment disbursement.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first. Every citation must
use the `[A-xx]` token exactly as spelled here. A citation to a target not listed here
is a protocol violation.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Finance | Manual trade confirmation and settlement workflow replaced by this pipeline; ≥3 named steps with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Finance | Entity vocabulary, settlement SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Finance | Finance | Trade order entry → position validation → credit limit check → trade confirmation engine; prose paragraphs per SC-7 prose form |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | Prose boundary paragraphs per BOUNDARY BLOCK SCHEMA; required skip-level target for Operations |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist; all items ✓ before Commerce begins |
| [A-06] | STAGE TRACE — Commerce | Commerce | Trade confirmation engine → settlement instruction generation → nostro funding notification; prose paragraphs |
| [A-07] | BOUNDARY CHECKS — Commerce | Commerce | Prose boundary paragraphs; extends elapsed from [A-04] |
| [A-08] | PHASE GATE 2 | Commerce | Self-verification checklist; all items ✓ before Operations begins; item [SC-12] verifies Operations skip-level citation |
| [A-09] | STAGE TRACE — Operations | Operations | Nostro funding notification → counterparty payment disbursement → settlement confirmation; prose paragraphs |
| [A-10] | BOUNDARY CHECKS — Operations | Operations | Prose boundary paragraphs; extends elapsed from [A-07] |
| [A-11] | STALE ANALYSIS | Operations | Normal-operation and failure-mode elapsed vs [A-02] threshold; narrative with labeled sentences |
| [A-12] | RECOVERY PRESCRIPTIONS | Operations | Named recovery per loss point; formula: `Fall back to [A-01] if [condition]`; SC-13 applies |
| [A-13] | INCUMBENT TOTAL | Operations | Sum of Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Operations | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions; SC-13 applies |

---

### REGISTER DECLARATION

This output uses the **conversational prose register** throughout. Boundary checks and
stage blocks are written as prose paragraphs, not markdown tables.

**This section is the sole authoritative reference for C-34 (`Incumbent equiv.` sentence
form) and C-35 (INCUMBENT TOTAL paragraph form). SC-9 and SC-10 are callbacks to Parts A
and B respectively; they do not independently restate compliance requirements.**

**Closed verification chain**: Part A is the governing authority for every C-34
(`Incumbent equiv.` sentence) failure. Part B is the governing authority for every C-35
(INCUMBENT TOTAL) failure. SC-12 is the governing authority for every skip-level
citation failure; its Phase Gate 2 item cites [SC-12] by number. **SC-13 BASELINE
CLOSURE is the governing authority for every baseline-closure failure in [A-12] and
[A-14]**; its inline callbacks at both section headers enforce the [A-01] citation
obligation by label-token match. **SC-14 FORMAT MODE DECLARATION is the governing
authority for every format-mode compliance failure**; its criterion substitution map
maps each affected criterion ID to its prose-mode evidence token. Together, Parts A/B,
the SC-12 Phase Gate 2 item, SC-13's paired callbacks, and SC-14's criterion
substitution map form a complete closed chain: every structural failure mode has a
named navigation path to its governing SC reachable from this paragraph.

**Part A — Field compliance markers (conversational prose register):**

| Required Field | Compliance Marker | Required Sentence Form | Disqualifying Form |
|----------------|-------------------|------------------------|--------------------|
| Domain entity | Paragraph opens with bold entity: `**[entity]**:` | `**[entity from [A-02]]**: [boundary content]` | "data" or "records" without named entity |
| Elapsed (cumulative) | Bold label `**Elapsed:**` | `**Elapsed:** [numeric total] min (cumulative)` | Partial sum; no label; deferred |
| Freshness verdict | Bold label `**Verdict:**` | `**Verdict:** FRESH` or `**Verdict:** STALE` vs [A-02] | Any other value |
| Error handling | Bold label `**Error handling:**` | `**Error handling:** [named mechanism]` or `no handling — see [A-12]` | Silence; no label |
| Schema change | Bold label `**Schema:**` | `**Schema:** [named field changes]` or `**Schema:** NONE` | Omitted |
| Data loss | Bold label `**Data loss:**` | `**Data loss:** YES — [loss point]` or `NO` | Generic language |
| Incumbent equivalent | Bold label `**Incumbent equiv.:**` with `[A-01]` token | `**Incumbent equiv.:** [A-01]: [named manual step + duration]` | Bare duration; `[A-01]` absent |
| Stage latency | Bold label `**Stage latency:**` | `**Stage latency:** [value, range, or characterization]` | Inferred only |

**Part B — Section format compliance markers (conversational prose register):**

| Required Section | Opening Marker | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` + bold role labels | One bold line per role: `**Finance:** [subtotal] min — [steps cited]`; closing `**Grand Total:** [sum] min` | Prose-only without role labels; missing role; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | All three tokens `[A-01]`, `[A-02]`, `[A-13]` present in prose; ≥1 alternative pattern; ≥2 dimensions | Any token absent; no pattern named |

---

### REGISTER INVARIANTS

Fields required in every boundary paragraph regardless of prose register variations.
Evaluator verifies by bold-label token presence only; prose context is not evaluated.

Required labels (must appear in every boundary paragraph):
`**[entity]**:` · `**Elapsed:**` · `**Verdict:**` · `**Error handling:**` · `**Schema:**` · `**Data loss:**` · `**Incumbent equiv.:**`

A boundary paragraph missing any declared label fails completeness, regardless of
whether the information appears in surrounding prose.

---

### BOUNDARY BLOCK SCHEMA

Standalone section declared before any role output. Field label strings must match
REGISTER DECLARATION Part A `Compliance Marker` spellings exactly.

**Every boundary paragraph must contain these labeled fields, in this order:**

`**[entity]**:` opening → `**Elapsed:**` → `**Verdict:**` → `**Error handling:**` →
`**Schema:**` → `**Data loss:**` → `**Incumbent equiv.:**`

A label absent, misspelled, or not matching Part A compliance marker strings fails the
schema. Field order is required.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Finance opens with
`Citing: [A-xx], [A-yy], ...` listing every token from prior roles this role builds on.
Citing [A-01] is required in every non-first role's Citing line.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding
boundary paragraph contains all required labels per BOUNDARY BLOCK SCHEMA. Confirm all
seven labels are present. Then write Stage N+1. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `**Elapsed:**` value is computed inside each boundary
paragraph as the sum of all prior stage latencies and boundary latencies. It may not be
deferred to [A-11]. [Per REGISTER DECLARATION Part A, `Elapsed` row.] [Apply SC-3 at
every boundary paragraph.]

**SC-4 — Binary verdict**: `**Verdict:**` = `FRESH` or `STALE`, derived by comparing
Elapsed against the [A-02] threshold. Cite [A-02] by token; do not restate its numeric
value. [Per REGISTER DECLARATION Part A, `Verdict` row.] [Apply SC-4 at every boundary
paragraph.]

**SC-5 — Immutability**: Finance appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written."

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required outputs. Every item
must be ticked ✓ or ✗. The next role may not begin until all items are ✓.

**SC-7 — Stage prose format**: Every stage paragraph opens with a bold stage label
(`**Stage N:**`) and includes labeled fields: `**Stage latency:**`, `**Schema in:**`,
`**Schema out:**`, `**Data loss:**`. [Per REGISTER DECLARATION Part A, `Stage latency`
row.] [Apply SC-7 at every stage paragraph.]

**SC-8 — Trade-off as required section**: [Per REGISTER DECLARATION Part B,
TRADE-OFF ANALYSIS row.] All three tokens required: [A-01], [A-02], [A-13]. [Apply SC-8
when producing [A-14].]

**SC-9 — Incumbent equiv. sentence form**: [Per REGISTER DECLARATION Part A, `Incumbent
equiv.` row.] Required: `**Incumbent equiv.:** [A-01]: [named manual step + duration]`.
Omitting `[A-01]` is a protocol violation. [Apply SC-9 at every boundary paragraph.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [Per REGISTER DECLARATION Part B,
INCUMBENT TOTAL row.] Produce [A-13] immediately before [A-14]; include one bold line
per role and a Grand Total line. [A-14] must cite [A-13]. [Apply SC-10 before writing
[A-14].]

**SC-11 — Baseline-first production**: [A-01] must be the first artifact written. No
boundary paragraph and no stage paragraph may appear before [A-01] is fully produced.

**SC-12 — Skip-level citation in Operations**: Operations' `Citing:` line must include
`[A-04]` — Finance's boundary checks, produced two positions prior in the
Finance → Commerce → Operations sequence. Commerce is Operations' immediate predecessor;
a `Citing:` line naming only Commerce's tokens without `[A-04]` fails SC-12. The
position distance is two: Operations occupies position 3, Finance occupies position 1.
A Phase Gate 2 verification item for this requirement must cite [SC-12] by its numbered
identifier in the item text itself.

**SC-13 — BASELINE CLOSURE**: [A-01] INCUMBENT BASELINE must appear as a named citation
token in two specific sections: (a) In [A-12] RECOVERY PRESCRIPTIONS — every recovery
formula must include the `[A-01]` token; absence is a protocol violation. (b) In [A-14]
TRADE-OFF ANALYSIS — `[A-01]` must be one of the three required citation tokens alongside
[A-02] and [A-13]. This SC is registered in REGISTER DECLARATION as a named navigation
entry in the closed-chain paragraph; evaluators navigate to it from the register index
without scanning STRUCTURAL CONSTRAINTS. [Per SC-13, cite [A-01] in [A-12].] [Per SC-13,
cite [A-01] in [A-14].]

**SC-14 — FORMAT MODE DECLARATION**: The output format for all role stage traces and
boundary checks is **PROSE**. Markdown tables are prohibited for stage and boundary
content. This SC is registered in REGISTER DECLARATION as a named navigation entry in
the closed-chain paragraph; evaluators navigate to it for any format-mode compliance
dispute.

Format: `PROSE` — applies to [A-03], [A-04], [A-06], [A-07], [A-09], [A-10].

Criterion substitution map (tabular-structural criteria applying in modified form for
this prose register):

| Criterion ID | Tabular Requirement | Prose-Mode Substitute |
|---|---|---|
| C-28 | Named column headers present by token match in boundary tables | Named bold labels present by token match in boundary paragraphs, per Part A compliance markers; evaluator verifies by label-string scan |
| C-30 | Field compliance verified by column-name presence in output table | Field compliance verified by bold-label presence per Part A; same token-match standard, different structural token |
| C-32 | Per-field column-header token as declared compliance marker | Per-field bold-label token as declared compliance marker; complete mapping in REGISTER DECLARATION Part A |

An evaluator determining compliance for C-28, C-30, or C-32 uses this criterion
substitution map to identify the prose-mode evidence token before inspecting output.
[Apply SC-14 throughout all role output.]

---

### ROLE 1 — Finance

[Finance runs first. No Citing line required. Incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST, before any domain context or stage trace.
Per SC-11. Describe the manual trade confirmation and settlement workflow this pipeline
replaces. Include ≥3 named manual steps with durations (e.g., "Trader manually phones
counterparty to confirm trade terms: 45 min", "Operations analyst manually checks credit
limit in spreadsheet and emails approval: 60 min", "Back-office coordinator manually
enters settlement instructions into payment system: 30 min"). Use entity names that will
reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 names from [A-01]): trade order, position validation
  record, credit limit check result, trade confirmation, settlement instruction,
  nostro funding record, counterparty payment
- Downstream consumer and business cadence (e.g., same-day settlement cutoff at 15:30 ET)
- Settlement SLA: integer with unit, derived from [A-01] total manual duration plus
  acceptable pipeline latency headroom
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Finance** — Per SC-7 prose form. Per SC-2. Use entity names from
[A-02].
- Stage 1: Trade order entry → Position validation service
- Stage 2: Validated position → Credit limit check
- Stage 3: Approved trade → Trade confirmation engine

**[A-04] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA. One prose boundary
paragraph between Stage 1–Stage 2; one between Stage 2–Stage 3; one after Stage 3.
[SC-3, SC-4, SC-9 / Part A apply.]

**[A-05] PHASE GATE 1** — Produce and tick before Commerce begins. Mark each ✓ or ✗:
- [ ] [A-01] produced first; no stage or boundary paragraph precedes it (SC-11)
- [ ] [A-01] includes ≥3 named manual steps with durations
- [ ] [A-02] SLA declared as integer with unit; SC-5 verbatim present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every stage paragraph in [A-03] has four required bold labels per SC-7
- [ ] Every boundary paragraph in [A-04] has seven required bold labels per BOUNDARY BLOCK SCHEMA
- [ ] Every `**Elapsed:**` is a computed numeric sum inside the paragraph (SC-3)
- [ ] Every `**Verdict:**` is FRESH or STALE, derived from [A-02] threshold (SC-4)
- [ ] Every `**Incumbent equiv.:**` sentence: `[A-01]: [named step + duration]` (SC-9)

Commerce may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 2 — Commerce

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Commerce** — Per SC-7 prose form. Per SC-2. Use entity names from
[A-02].
- Stage 4: Trade confirmation engine → Settlement instruction generation
- Stage 5: Settlement instruction → Nostro account funding notification

**[A-07] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: `**Elapsed:**` extends the final value from [A-04]; do not reset to zero.]
[SC-4: `**Verdict:**` vs [A-02] threshold; do not redeclare threshold numeric value.]
[SC-9: every `**Incumbent equiv.:**` sentence: `[A-01]: [named step + duration]`.]

**[A-08] PHASE GATE 2** — Produce and tick before Operations begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage paragraph in [A-06] has four required bold labels per SC-7
- [ ] Every boundary paragraph in [A-07] has seven required bold labels per BOUNDARY BLOCK SCHEMA
- [ ] `**Elapsed:**` in [A-07] extends [A-04] final value; not reset (SC-3)
- [ ] Every `**Verdict:**` derives from [A-02] threshold; threshold not redeclared (SC-4)
- [ ] Every `**Incumbent equiv.:**` sentence: `[A-01]: [named step + duration]` (SC-9)
- [ ] [SC-12]: Operations' `Citing:` line must include `[A-04]` — Finance's boundary
  checks, two positions prior in the Finance → Commerce → Operations sequence. Mark ✗
  if [A-04] is absent from Operations' Citing line.

Operations may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 3 — Operations

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] is required per SC-12 — Finance's boundary checks, two positions prior in the
Finance → Commerce → Operations sequence.)

**[A-09] STAGE TRACE — Operations** — Per SC-7 prose form. Per SC-2. Use entity names
from [A-02].
- Stage 6: Nostro account funding → Counterparty payment disbursement
- Stage 7: Payment disbursement → Settlement confirmation record

**[A-10] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend `**Elapsed:**` from [A-07] final value.]
[SC-4: `**Verdict:**` vs [A-02] threshold.]
[SC-9: every `**Incumbent equiv.:**` sentence: `[A-01]: [named step + duration]`.]

**[A-11] STALE ANALYSIS** — Using final `**Elapsed:**` from [A-10]. Write one labeled
narrative paragraph per scenario:

`**Entity:** [A-02] entity name | **Normal elapsed:** N min | **Failure-mode elapsed:**
N min | **Threshold:** [A-02] | **Verdict:** FRESH/STALE`

Produce separate sentences for normal-operation and failure-mode staleness. Cite [A-02]
by token; do not restate the numeric threshold value.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01] in this section.] For
every `no handling — see [A-12]` annotation in [A-04]/[A-07]/[A-10] and every
`**Data loss:** YES` in [A-03]/[A-06]/[A-09], provide a specific named recovery action.
Required formula: `Fall back to [A-01] if [specific named failure condition]`. Cite
[A-01] using this formula at least once. SC-13 requires [A-01] to appear as a citation
token in this section; absence is a protocol violation.

**[A-13] INCUMBENT TOTAL** — [Per REGISTER DECLARATION Part B. Per SC-10.] Produce
immediately before [A-14]:

`### [A-13] INCUMBENT TOTAL`
**Finance:** [subtotal] min — [steps from [A-01]]
**Commerce:** [subtotal] min — [steps from [A-01]]
**Operations:** [subtotal] min — [steps from [A-01]]
**Grand Total:** [sum] min

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01] in this section.] [Per
REGISTER DECLARATION Part B. Per SC-8.] Required named section. Cite `[A-01]` (manual
baseline), `[A-02]` (SLA dimension), and `[A-13]` (numeric incumbent total) — all three
tokens required. Name ≥1 alternative data propagation pattern. Provide ≥2 trade-off
dimensions using [A-13] Grand Total as the numeric comparison endpoint.

---

---

## V-03

**Axis**: Lifecycle emphasis — 4 stages per role (C-46, boundary density stress test)

**Hypothesis**: Commerce → Finance → Operations; SaaS subscription revenue recognition
pipeline. 12 total stages and 9 boundary blocks. The larger boundary count tests whether
SC-13's inline callbacks remain enforced across all 9 blocks, and whether the cumulative
elapsed computation stays consistent across 8 boundary-to-boundary increments. SC-13
is named in the closed-chain paragraph as the governing authority for baseline-closure
failures (C-46). Operations (pos 3) cites Commerce [A-04] (pos 1) skip-level per SC-12.
Tabular register.

---

You are tracing data through a SaaS subscription revenue recognition pipeline —
subscription event to deferred revenue schedule. Three expert roles run in the sequence
**Commerce → Finance → Operations**. Commerce establishes the revenue recognition SLA
and the manual billing process baseline that all subsequent roles must cite. Finance and
Operations cite Commerce's artifacts by token; they may not redeclare or re-derive either.

Operations runs last and must cite Commerce's boundary artifacts directly — two positions
prior in the Commerce → Finance → Operations sequence — as a required skip-level
citation. An Operations `Citing:` line that names only Finance's artifacts without
Commerce's boundary checks fails SC-12. Phase Gate 2 verifies this requirement by
citing SC-12 by number before Operations may begin.

The physical pipeline flows: subscription event ingestion → entitlement provisioning →
billing period calculation → invoice generation → payment collection → revenue
allocation → deferred revenue schedule → ASC 606 recognition posting → close-period
journal entry → reporting package.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first. Every citation must
use the `[A-xx]` token exactly as spelled here. A citation to a target not listed here
is a protocol violation.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Commerce | Manual subscription billing and revenue recognition process replaced by this pipeline; ≥3 named steps with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Commerce | Entity vocabulary, revenue recognition SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Commerce | Commerce | Subscription event → entitlement provisioning → billing period calculation → invoice generation; 4 stages; stage tables per SC-7 |
| [A-04] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01]; required skip-level target for Operations |
| [A-05] | PHASE GATE 1 | Commerce | Self-verification checklist; all items ✓ before Finance begins |
| [A-06] | STAGE TRACE — Finance | Finance | Payment collection → revenue allocation → deferred revenue schedule → ASC 606 recognition posting; 4 stages; stage tables |
| [A-07] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Finance | Self-verification checklist; all items ✓ before Operations begins; item [SC-12] verifies Operations skip-level citation |
| [A-09] | STAGE TRACE — Operations | Operations | ASC 606 recognition posting → close-period journal entry → reporting package → executive dashboard; 4 stages; stage tables |
| [A-10] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cells cite [A-01] |
| [A-11] | STALE ANALYSIS | Operations | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Operations | Named recovery per loss point and no-handling annotation; formula: `Fall back to [A-01] if [condition]`; SC-13 applies |
| [A-13] | INCUMBENT TOTAL | Operations | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Operations | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions; SC-13 applies |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell
form) and C-35 (INCUMBENT TOTAL section format). SC-9 and SC-10 are callbacks to Parts A
and B respectively.**

**Closed verification chain**: Part A is the governing authority for every C-34
(`Incumbent Equiv.` column) failure. Part B is the governing authority for every C-35
(INCUMBENT TOTAL) failure. SC-12 is the governing authority for every skip-level
citation failure; its Phase Gate 2 item cites [SC-12] by number. **SC-13 BASELINE
CLOSURE is the governing authority for every baseline-closure failure in [A-12] and
[A-14]**; its inline callbacks at both section headers make the [A-01] citation
obligation token-verifiable. Together, Parts A/B, the SC-12 Phase Gate 2 item, and
SC-13's paired inline callbacks form a complete closed chain.

**Part A — Field compliance markers (boundary block columns):**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum of all prior stage and boundary latencies, in minutes | Partial sum; deferred total |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE`, derived from [A-02] threshold | Any other value |
| Error handling | `Error Handling` | Named retry/dead-letter/rollback, or exactly `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level changes, or exactly `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` | Bare duration; token omitted; column absent |
| Stage latency | `Stage Latency` (stage table) | Explicit value, range, or characterization | Inferred from boundary elapsed only |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Markdown table: `Role \| Incumbent Equiv. subtotal \| Steps cited`; rows for Commerce, Finance, Operations, Grand Total | Prose-only; missing role row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | All three tokens `[A-01]`, `[A-02]`, `[A-13]` present; ≥1 alternative pattern; ≥2 dimensions | Any token absent |

---

### BOUNDARY BLOCK SCHEMA

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

Column headers must match REGISTER DECLARATION Part A spellings exactly. A column absent
or renamed fails the schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Commerce opens with
`Citing: [A-xx], [A-yy], ...`. Citing [A-01] is required in every non-first role's
Citing line.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding
BOUNDARY CHECK table is fully populated per BOUNDARY BLOCK SCHEMA. [Apply SC-2 before
every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` computed inside each boundary block
as the sum of all prior stage and boundary latencies. Not deferred to [A-11]. [Apply
SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE`, derived by comparing
Elapsed (cumul.) against [A-02] threshold. Cite [A-02] by token. [Apply SC-4 at every
boundary block.]

**SC-5 — Immutability**: Commerce appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written."

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required outputs. Every item
ticked ✓ or ✗ before next role begins.

**SC-7 — Stage table format**: Every stage block: markdown table with columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. [Apply SC-7 at every stage
block.]

**SC-8 — Trade-off as required section**: [Per REGISTER DECLARATION Part B.] All three
tokens required: [A-01], [A-02], [A-13]. ≥1 alternative pattern. ≥2 dimensions. [Apply
SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: [Per REGISTER DECLARATION Part A.] Required:
`[A-01]: [named manual step + duration]`. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [Per REGISTER DECLARATION Part B.]
Produce [A-13] immediately before [A-14]. Sum from [A-04], [A-07], [A-10]; Grand Total
row required. [Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] must be the first artifact written. No
boundary block or stage trace may appear before [A-01] is complete.

**SC-12 — Skip-level citation in Operations**: Operations' `Citing:` line must include
`[A-04]` — Commerce's boundary checks, produced two positions prior in the
Commerce → Finance → Operations sequence. Finance is Operations' immediate predecessor;
citing only Finance's tokens without `[A-04]` fails SC-12. The position distance is two:
Operations occupies position 3, Commerce occupies position 1. Phase Gate 2 item must
cite [SC-12] by its numbered identifier.

**SC-13 — BASELINE CLOSURE**: [A-01] must appear as a named citation token in: (a)
[A-12] RECOVERY PRESCRIPTIONS — every recovery formula must include `[A-01]`. (b) [A-14]
TRADE-OFF ANALYSIS — `[A-01]` must be one of the three required tokens alongside [A-02]
and [A-13]. This SC is registered in REGISTER DECLARATION's closed-chain paragraph as
the governing authority for baseline-closure failures; evaluators navigate to it from
the register index without scanning STRUCTURAL CONSTRAINTS. [Per SC-13, cite [A-01] in
[A-12].] [Per SC-13, cite [A-01] in [A-14].]

---

### ROLE 1 — Commerce

[Commerce runs first. No Citing line required. Incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST. Per SC-11. Describe the manual subscription
billing and revenue recognition process this pipeline replaces. Include ≥3 named manual
steps with durations (e.g., "Revenue analyst manually calculates pro-rated subscription
amounts in spreadsheet: 90 min", "Finance coordinator posts manual revenue allocation
entries by product line: 75 min", "Accountant manually updates deferred revenue schedule
in ERP: 60 min"). Use entity names that will reappear in [A-02].

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 names from [A-01]): subscription event, entitlement
  record, billing period, invoice, payment collection record, revenue allocation entry,
  deferred revenue schedule, recognition posting, close-period journal entry
- Downstream consumer and business cadence (e.g., monthly close on last business day)
- Revenue recognition SLA: integer with unit, derived from [A-01] total duration
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. 4 stages:
- Stage 1: Subscription event ingestion → Entitlement provisioning service
- Stage 2: Entitlement record → Billing period calculation engine
- Stage 3: Billing period → Invoice generation
- Stage 4: Invoice → Payment collection gateway

**[A-04] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA. One block between
each consecutive stage pair (3 inter-stage blocks) plus one block after Stage 4 (1
post-stage block) = 4 total boundary blocks. [SC-3, SC-4, SC-9 / Part A apply.]
Elapsed (cumul.) accumulates across all 4 blocks.

**[A-05] PHASE GATE 1** — Produce and tick before Finance begins. Mark each ✓ or ✗:
- [ ] [A-01] produced first (SC-11)
- [ ] [A-01] includes ≥3 named manual steps with durations
- [ ] [A-02] SLA declared as integer with unit; SC-5 verbatim present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] All 4 stages in [A-03] have four required columns per SC-7
- [ ] All 4 blocks in [A-04] have seven columns; headers match Part A
- [ ] Every `Elapsed (cumul.)` is incremental and internally computed (SC-3)
- [ ] Every `Verdict` is FRESH or STALE from [A-02] threshold (SC-4)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)

Finance may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 2 — Finance

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Finance** — Per SC-7. Per SC-2. 4 stages:
- Stage 5: Payment collection record → Revenue allocation processor
- Stage 6: Revenue allocation entry → Deferred revenue schedule builder
- Stage 7: Deferred revenue schedule → ASC 606 recognition posting engine
- Stage 8: Recognition posting → Close-period journal entry

**[A-07] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA. One block between
each consecutive stage pair (3 inter-stage blocks) plus one block after Stage 8 (1
post-stage block) = 4 total boundary blocks. [SC-3: Elapsed (cumul.) extends [A-04]
final value; do not reset.] [SC-4: Verdict vs [A-02] threshold.] [SC-9 applies.]

**[A-08] PHASE GATE 2** — Produce and tick before Operations begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] All 4 stages in [A-06] have four required columns per SC-7
- [ ] All 4 blocks in [A-07] have seven columns; headers match Part A
- [ ] `Elapsed (cumul.)` in [A-07] Block 1 extends [A-04] Block 4 final value (SC-3)
- [ ] Every `Verdict` derives from [A-02] threshold (SC-4)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)
- [ ] [SC-12]: Operations' `Citing:` line must include `[A-04]` — Commerce's boundary
  checks, two positions prior. Mark ✗ if [A-04] absent from Operations' Citing line.

Operations may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 3 — Operations

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] is required per SC-12 — Commerce's boundary checks, two positions prior in the
Commerce → Finance → Operations sequence.)

**[A-09] STAGE TRACE — Operations** — Per SC-7. Per SC-2. 4 stages:
- Stage 9: Close-period journal entry → Reporting package assembly
- Stage 10: Reporting package → Regulatory reporting feed
- Stage 11: Regulatory reporting → Audit trail archive
- Stage 12: Audit trail archive → Executive revenue dashboard

**[A-10] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA. 4 boundary blocks.
[SC-3: extend Elapsed (cumul.) from [A-07] final value.] [SC-4, SC-9 apply.]

**[A-11] STALE ANALYSIS** — Using final Elapsed (cumul.) from [A-10]:

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01] in this section.] For every
`no handling — see [A-12]` in [A-04]/[A-07]/[A-10] and every `Data Loss Flag: YES` in
[A-03]/[A-06]/[A-09], provide a specific named recovery action. Required formula:
`Fall back to [A-01] if [condition]`. SC-13 requires [A-01] to appear here; absence is
a protocol violation.

**[A-13] INCUMBENT TOTAL** — [Per REGISTER DECLARATION Part B. Per SC-10.]

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Commerce | [sum of [A-04] values] | [steps from [A-01]] |
| Finance | [sum of [A-07] values] | [steps from [A-01]] |
| Operations | [sum of [A-10] values] | [steps from [A-01]] |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01] in this section.] [Per
REGISTER DECLARATION Part B. Per SC-8.] Cite `[A-01]`, `[A-02]`, and `[A-13]` — all
three tokens required. Name ≥1 alternative pattern. ≥2 trade-off dimensions.

---

---

## V-04

**Axis**: Combined — role sequence + maximum inertia framing (C-46)

**Hypothesis**: Operations → Commerce → Finance; pharmaceutical raw material
procurement-to-payment pipeline. [A-01] INCUMBENT BASELINE requires ≥5 named manual
steps with durations — the highest inertia specification across all R15 variations.
SC-13 is named in the closed-chain paragraph as the governing authority for
baseline-closure failures (C-46). Finance (pos 3) cites Operations [A-04] (pos 1)
skip-level per SC-12. The dense incumbent baseline populates [A-13] INCUMBENT TOTAL
with a high Grand Total, amplifying the trade-off comparison. Tabular register.

---

You are tracing data through a pharmaceutical raw material procurement-to-payment
pipeline — purchase requisition to supplier payment. Three expert roles run in the
sequence **Operations → Commerce → Finance**. Operations establishes the procurement
SLA and the manual purchase order baseline that all subsequent roles must cite. Commerce
and Finance cite Operations' artifacts by token; they may not redeclare or re-derive
either.

Finance runs last and must cite Operations' boundary artifacts directly — two positions
prior in the Operations → Commerce → Finance sequence — as a required skip-level
citation. A Finance `Citing:` line that names only Commerce's artifacts without
Operations' boundary checks fails SC-12. Phase Gate 2 verifies this by citing SC-12 by
number before Finance may begin.

The physical pipeline flows: purchase requisition submission → supplier qualification
check → purchase order generation → goods receipt confirmation → quality inspection
hold → invoice matching → three-way match validation → payment authorization →
supplier payment disbursement.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Operations | Manual purchase order and payment processing workflow replaced by this pipeline; **≥5 named steps** with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, procurement SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Operations | Operations | Requisition submission → supplier qualification → PO generation → goods receipt confirmation; stage tables per SC-7 |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01]; required skip-level target for Finance |
| [A-05] | PHASE GATE 1 | Operations | Self-verification checklist; all items ✓ before Commerce begins |
| [A-06] | STAGE TRACE — Commerce | Commerce | Quality inspection hold → invoice matching → three-way match validation; stage tables |
| [A-07] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Commerce | Self-verification checklist; all items ✓ before Finance begins; item [SC-12] verifies Finance skip-level citation |
| [A-09] | STAGE TRACE — Finance | Finance | Three-way match result → payment authorization → supplier payment disbursement; stage tables |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cells cite [A-01] |
| [A-11] | STALE ANALYSIS | Finance | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery per loss point; formula: `Fall back to [A-01] if [condition]`; SC-13 applies |
| [A-13] | INCUMBENT TOTAL | Finance | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Finance | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions; SC-13 applies |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell
form) and C-35 (INCUMBENT TOTAL section format).**

**Closed verification chain**: Part A is the governing authority for every C-34
(`Incumbent Equiv.` column) failure. Part B is the governing authority for every C-35
(INCUMBENT TOTAL) failure. SC-12 is the governing authority for every skip-level
citation failure; its Phase Gate 2 item cites [SC-12] by number. **SC-13 BASELINE
CLOSURE is the governing authority for every baseline-closure failure in [A-12] and
[A-14]**; its inline callbacks at both section headers make the [A-01] citation
obligation mechanically verifiable. Together, Parts A/B, the SC-12 Phase Gate 2 item,
and SC-13's paired inline callbacks form a complete closed chain reachable from this
paragraph.

**Part A — Field compliance markers (boundary block columns):**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum of all prior stage and boundary latencies | Partial sum; deferred total |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE`, from [A-02] threshold | Any other value |
| Error handling | `Error Handling` | Named retry/dead-letter/rollback, or `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field changes, or exactly `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` | Token omitted; column absent |
| Stage latency | `Stage Latency` | Explicit value, range, or characterization | Inferred only |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | `Role \| Incumbent Equiv. subtotal \| Steps cited`; rows for Operations, Commerce, Finance, Grand Total | Missing row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | Tokens `[A-01]`, `[A-02]`, `[A-13]` present; ≥1 pattern; ≥2 dimensions | Any token absent |

---

### BOUNDARY BLOCK SCHEMA

`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Operations opens with
`Citing: [A-xx], [A-yy], ...`. Citing [A-01] required in every non-first role's line.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until preceding
boundary block is fully populated. [Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` computed inside each boundary block;
not deferred. [Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` from [A-02] threshold. [Apply
SC-4 at every boundary block.]

**SC-5 — Immutability**: Operations appends to [A-02] verbatim: "This threshold is
fixed. No subsequent role may revise it after Stage 1 is written."

**SC-6 — Phase gate obligation**: [A-05] and [A-08] required; every item ✓ or ✗ before
next role begins.

**SC-7 — Stage table format**: `Stage Latency | Schema In | Schema Out | Data Loss Flag`.
[Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [Per Part B.] Tokens [A-01], [A-02], [A-13]
required. ≥1 pattern. ≥2 dimensions. [Apply SC-8 at [A-14].]

**SC-9 — Incumbent Equiv. cell form**: `[A-01]: [named manual step + duration]`. [Apply
SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [Per Part B.] Produce [A-13] immediately
before [A-14]. Grand Total required. [Apply SC-10 before [A-14].]

**SC-11 — Baseline-first production**: [A-01] written first; no stage or boundary block
before it.

**SC-12 — Skip-level citation in Finance**: Finance's `Citing:` line must include `[A-04]`
— Operations' boundary checks, produced two positions prior in the
Operations → Commerce → Finance sequence. Commerce is Finance's immediate predecessor;
citing only Commerce's tokens without `[A-04]` fails SC-12. Position distance is two:
Finance occupies position 3, Operations occupies position 1. Phase Gate 2 item must
cite [SC-12] by number.

**SC-13 — BASELINE CLOSURE**: [A-01] must appear as a named citation token in: (a)
[A-12] RECOVERY PRESCRIPTIONS — every recovery formula must include `[A-01]`. (b) [A-14]
TRADE-OFF ANALYSIS — `[A-01]` must be one of three required tokens alongside [A-02] and
[A-13]. This SC is registered in REGISTER DECLARATION's closed-chain paragraph as the
governing authority for baseline-closure failures. [Per SC-13, cite [A-01] in [A-12].]
[Per SC-13, cite [A-01] in [A-14].]

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required. Incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST. Per SC-11. Describe the manual purchase
order and payment processing workflow this pipeline replaces. Include **≥5 named manual
steps with durations** — this is the maximum inertia specification; a baseline with
fewer than 5 steps is a protocol violation. Example steps: "Procurement analyst manually
creates purchase requisition in ERP and emails to manager for approval: 90 min",
"Supplier qualification coordinator checks vendor credentials in compliance database:
120 min", "Buyer manually drafts purchase order in ERP and emails to supplier: 60 min",
"Receiving coordinator manually counts inbound goods and enters receipt record: 45 min",
"Finance analyst manually reviews invoice against PO and goods receipt: 75 min". Use
entity names that will reappear in [A-02]. All subsequent roles must cite [A-01].

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 names from [A-01]): purchase requisition, supplier
  qualification record, purchase order, goods receipt record, quality inspection hold,
  invoice, three-way match result, payment authorization, supplier payment
- Downstream consumer and business cadence (e.g., net-30 supplier payment terms)
- Procurement SLA: integer with unit, derived from [A-01] total manual duration
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 1: Purchase requisition → Supplier qualification check
- Stage 2: Qualified supplier → Purchase order generation
- Stage 3: PO acknowledgment → Goods receipt confirmation

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA. [SC-3, SC-4, SC-9.]

**[A-05] PHASE GATE 1** — Mark each ✓ or ✗:
- [ ] [A-01] produced first (SC-11); includes ≥5 named manual steps with durations
- [ ] [A-02] SLA integer with unit; SC-5 verbatim present; ≥2 entity names from [A-01]
- [ ] All stages in [A-03]: four columns per SC-7
- [ ] All blocks in [A-04]: seven columns matching Part A; SC-3, SC-4, SC-9 satisfied

Commerce may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 2 — Commerce

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Commerce** — Per SC-7. Per SC-2.
- Stage 4: Goods receipt → Quality inspection hold resolution
- Stage 5: Cleared inspection → Invoice matching engine
- Stage 6: Matched invoice → Three-way match validation

**[A-07] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extends [A-04] final Elapsed; do not reset.] [SC-4, SC-9 apply.]

**[A-08] PHASE GATE 2** — Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] All stages in [A-06]: four columns per SC-7
- [ ] All blocks in [A-07]: seven columns; [A-07] Elapsed extends [A-04] final value
- [ ] SC-4 and SC-9 satisfied in [A-07]
- [ ] [SC-12]: Finance's `Citing:` line must include `[A-04]` — Operations' boundary
  checks, two positions prior. Mark ✗ if [A-04] absent from Finance's Citing line.

Finance may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] required per SC-12 — Operations' boundary checks, two positions prior.)

**[A-09] STAGE TRACE — Finance** — Per SC-7. Per SC-2.
- Stage 7: Three-way match result → Payment authorization review
- Stage 8: Authorized payment → Supplier payment disbursement

**[A-10] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend from [A-07].] [SC-4, SC-9 apply.]

**[A-11] STALE ANALYSIS** —

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: cite [A-01] in this section.] Named
recovery per loss point and no-handling annotation. Formula: `Fall back to [A-01] if
[specific failure condition]`. SC-13 requires [A-01] here; absence is a protocol
violation.

**[A-13] INCUMBENT TOTAL** — [Per Part B. Per SC-10.] Immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Operations | [sum of [A-04]] | [steps] |
| Commerce | [sum of [A-07]] | [steps] |
| Finance | [sum of [A-10]] | [steps] |
| **Grand Total** | | |

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: cite [A-01] in this section.] [Per Part B.
Per SC-8.] Cite `[A-01]`, `[A-02]`, `[A-13]`. ≥1 alternative pattern. ≥2 dimensions.
[A-13] Grand Total as numeric comparison endpoint.

---

---

## V-05

**Axis**: Combined — output format + phrasing register (C-46 + C-47), imperative voice

**Hypothesis**: Operations → Finance → Commerce; federal contracting requisition-to-
payment pipeline. Prose register + imperative second-person voice throughout (all role
instructions use "You must", "Write", "Do not", rather than declarative framing). SC-13
BASELINE CLOSURE and SC-14 FORMAT MODE DECLARATION are both named in the closed-chain
paragraph as navigation entries (C-46, C-47). Commerce (pos 3) cites Operations [A-04]
(pos 1) skip-level per SC-12. The imperative register stress-tests whether structural
obligations survive voice changes.

---

You are tracing data through a federal contracting requisition-to-payment pipeline —
purchase request to vendor payment certification. Three expert roles run in the sequence
**Operations → Finance → Commerce**. Operations establishes the payment certification
SLA and the manual requisition processing baseline that all subsequent roles must cite.
Finance and Commerce cite Operations' artifacts by token; they may not redeclare or
re-derive either.

Commerce runs last and must cite Operations' boundary artifacts directly — two positions
prior in the Operations → Finance → Commerce sequence — as a required skip-level
citation. A Commerce `Citing:` line that names only Finance's artifacts without
Operations' boundary checks fails SC-12. Phase Gate 2 verifies this by citing SC-12 by
number before Commerce may begin.

The physical pipeline flows: purchase request submission → obligation validation →
contract vehicle selection → vendor notification → delivery confirmation → invoice
submission → payment certification review → disbursement authorization → treasury
payment release.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first. Every citation must
use the `[A-xx]` token exactly as spelled here. A citation to a target not listed here
is a protocol violation.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Operations | Manual requisition and payment processing workflow replaced by this pipeline; ≥3 named steps with durations; produced FIRST. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, payment certification SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Operations | Operations | Purchase request → obligation validation → contract vehicle selection → vendor notification; prose paragraphs per SC-7 |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | Prose boundary paragraphs per BOUNDARY BLOCK SCHEMA; required skip-level target for Commerce |
| [A-05] | PHASE GATE 1 | Operations | Self-verification checklist; all items ✓ before Finance begins |
| [A-06] | STAGE TRACE — Finance | Finance | Vendor notification → delivery confirmation → invoice submission; prose paragraphs |
| [A-07] | BOUNDARY CHECKS — Finance | Finance | Prose boundary paragraphs; extends elapsed from [A-04] |
| [A-08] | PHASE GATE 2 | Finance | Self-verification checklist; all items ✓ before Commerce begins; item [SC-12] verifies Commerce skip-level citation |
| [A-09] | STAGE TRACE — Commerce | Commerce | Invoice submission → payment certification review → disbursement authorization → treasury payment release; prose paragraphs |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | Prose boundary paragraphs; extends elapsed from [A-07] |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point; formula: `Fall back to [A-01] if [condition]`; SC-13 applies |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum of Incumbent Equiv. values from [A-04], [A-07], [A-10]; role breakdown; immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required named section; cites [A-01], [A-02], [A-13]; ≥1 alternative pattern; ≥2 dimensions; SC-13 applies |

---

### REGISTER DECLARATION

This output uses the **conversational prose register** throughout. Stage traces and
boundary checks are prose paragraphs, not markdown tables.

**This section is the sole authoritative reference for C-34 (`Incumbent equiv.` sentence
form) and C-35 (INCUMBENT TOTAL paragraph form). SC-9 and SC-10 are callbacks to Parts A
and B; they do not independently restate compliance requirements.**

**Closed verification chain**: Part A is the governing authority for every C-34
(`Incumbent equiv.` sentence) failure. Part B is the governing authority for every C-35
(INCUMBENT TOTAL) failure. SC-12 is the governing authority for every skip-level
citation failure; its Phase Gate 2 item cites [SC-12] by number. **SC-13 BASELINE
CLOSURE is the governing authority for every baseline-closure failure in [A-12] and
[A-14]**; its inline callbacks at both section headers enforce the [A-01] citation
obligation by label-token match. **SC-14 FORMAT MODE DECLARATION is the governing
authority for every format-mode compliance failure**; its criterion substitution map
identifies the prose-mode evidence token for each affected criterion ID. Together,
Parts A/B, the SC-12 Phase Gate 2 item, SC-13's paired inline callbacks, and SC-14's
criterion substitution map form a complete closed chain: every structural failure mode
has a named navigation path reachable from this paragraph.

**Part A — Field compliance markers (conversational prose register):**

| Required Field | Compliance Marker | Required Sentence Form | Disqualifying Form |
|----------------|-------------------|------------------------|--------------------|
| Domain entity | `**[entity]**:` | `**[entity from [A-02]]**: [boundary content]` | "data" or "records" without named entity |
| Elapsed (cumulative) | `**Elapsed:**` | `**Elapsed:** [numeric total] min (cumulative)` | Partial sum; no label; deferred |
| Freshness verdict | `**Verdict:**` | `**Verdict:** FRESH` or `**Verdict:** STALE` | Any other value |
| Error handling | `**Error handling:**` | `**Error handling:** [named mechanism]` or `no handling — see [A-12]` | Silence; no label |
| Schema change | `**Schema:**` | `**Schema:** [named changes]` or `**Schema:** NONE` | Omitted |
| Data loss | `**Data loss:**` | `**Data loss:** YES — [loss point]` or `NO` | Generic language |
| Incumbent equivalent | `**Incumbent equiv.:**` + `[A-01]` | `**Incumbent equiv.:** [A-01]: [named step + duration]` | `[A-01]` absent |
| Stage latency | `**Stage latency:**` | `**Stage latency:** [value or characterization]` | Inferred only |

**Part B — Section format compliance markers (conversational prose register):**

| Required Section | Opening Marker | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` + bold role labels | `**Operations:** [subtotal] min — [steps]`; `**Finance:** ...`; `**Commerce:** ...`; `**Grand Total:** [sum] min` | Missing role label; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | Tokens `[A-01]`, `[A-02]`, `[A-13]` present; ≥1 pattern; ≥2 dimensions | Any token absent |

---

### REGISTER INVARIANTS

Required labels in every boundary paragraph:
`**[entity]**:` · `**Elapsed:**` · `**Verdict:**` · `**Error handling:**` · `**Schema:**` · `**Data loss:**` · `**Incumbent equiv.:**`

---

### BOUNDARY BLOCK SCHEMA

`**[entity]**:` → `**Elapsed:**` → `**Verdict:**` → `**Error handling:**` →
`**Schema:**` → `**Data loss:**` → `**Incumbent equiv.:**`

Labels must match REGISTER DECLARATION Part A spellings exactly. Order is required.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: You must open every role other than Operations with
`Citing: [A-xx], [A-yy], ...`. You must cite [A-01] in every non-first role's line.

**SC-2 — Stage-write progression gate**: Do not write Stage N+1 until you have written
the preceding boundary paragraph with all seven required labels per BOUNDARY BLOCK
SCHEMA. Confirm all labels present. Then write Stage N+1. [Apply SC-2 before every
stage advance.]

**SC-3 — Incremental elapsed**: You must compute `**Elapsed:**` inside each boundary
paragraph as the sum of all prior stage latencies and boundary latencies. Do not defer
it to [A-11]. [Per Part A, `Elapsed` row.] [Apply SC-3 at every boundary paragraph.]

**SC-4 — Binary verdict**: You must set `**Verdict:**` to exactly `FRESH` or `STALE` by
comparing Elapsed against [A-02]. Cite [A-02] by token; do not restate its numeric value.
[Apply SC-4 at every boundary paragraph.]

**SC-5 — Immutability**: You must append to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written."

**SC-6 — Phase gate obligation**: You must produce [A-05] and [A-08] as checklists.
Tick every item ✓ or ✗. Do not allow the next role to begin until all items are ✓.

**SC-7 — Stage prose format**: You must open every stage paragraph with a bold stage
label (`**Stage N:**`) and include: `**Stage latency:**`, `**Schema in:**`,
`**Schema out:**`, `**Data loss:**`. [Apply SC-7 at every stage paragraph.]

**SC-8 — Trade-off as required section**: [Per Part B.] You must cite `[A-01]`, `[A-02]`,
and `[A-13]` — all three required. Name ≥1 alternative pattern. Provide ≥2 dimensions.
[Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent equiv. sentence form**: [Per Part A.] You must write:
`**Incumbent equiv.:** [A-01]: [named manual step + duration]`. Do not omit `[A-01]`.
[Apply SC-9 at every boundary paragraph.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [Per Part B.] You must produce [A-13]
immediately before [A-14]. Sum from [A-04], [A-07], [A-10]. Include one bold line per
role and a Grand Total line. [Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: You must write [A-01] first. Do not write any
stage or boundary paragraph before [A-01] is complete.

**SC-12 — Skip-level citation in Commerce**: You must include `[A-04]` in Commerce's
`Citing:` line — Operations' boundary checks, produced two positions prior in the
Operations → Finance → Commerce sequence. Finance is Commerce's immediate predecessor;
citing only Finance's tokens without `[A-04]` fails SC-12. The position distance is
two: Commerce occupies position 3, Operations occupies position 1. Phase Gate 2 must
contain a verification item that cites [SC-12] by its numbered identifier.

**SC-13 — BASELINE CLOSURE**: You must include `[A-01]` as a named citation token in:
(a) [A-12] RECOVERY PRESCRIPTIONS — every recovery formula must include `[A-01]`; do
not omit it. (b) [A-14] TRADE-OFF ANALYSIS — `[A-01]` must be one of three required
citation tokens alongside [A-02] and [A-13]. This SC is registered in REGISTER
DECLARATION as a named navigation entry in the closed-chain paragraph; evaluators
navigate to it from the register index. [Per SC-13, cite [A-01] in [A-12].] [Per SC-13,
cite [A-01] in [A-14].]

**SC-14 — FORMAT MODE DECLARATION**: You must write all role stage traces and boundary
checks as prose paragraphs. Do not use markdown tables for stage or boundary content.
This SC is registered in REGISTER DECLARATION as a named navigation entry in the
closed-chain paragraph; evaluators navigate to it for any format-mode dispute.

Format: `PROSE` — applies to [A-03], [A-04], [A-06], [A-07], [A-09], [A-10].

Criterion substitution map:

| Criterion ID | Tabular Requirement | Prose-Mode Substitute |
|---|---|---|
| C-28 | Named column headers by token match in boundary tables | Named bold labels by token match in boundary paragraphs per Part A compliance markers |
| C-30 | Field compliance by column-name presence | Field compliance by bold-label presence per Part A; same token-match standard |
| C-32 | Per-field column-header token as compliance marker | Per-field bold-label token as compliance marker; complete mapping in Part A |

[Apply SC-14 throughout all role output.]

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required. You must write the incumbent baseline
first per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST, before any domain context or stage trace.
You must describe the manual requisition and payment processing workflow this pipeline
replaces. Include ≥3 named manual steps with durations (e.g., "Contracting officer
manually reviews purchase request and assigns contract vehicle: 120 min", "Procurement
analyst manually drafts and emails vendor notification: 45 min", "Finance coordinator
manually reconciles vendor invoice against contract line items in spreadsheet: 90 min").
Use entity names that will reappear in [A-02]. All subsequent roles must cite [A-01].

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 names from [A-01]): purchase request, obligation
  validation record, contract vehicle assignment, vendor notification, delivery
  confirmation, invoice submission, payment certification record, disbursement
  authorization, treasury payment
- Downstream consumer and business cadence (e.g., 30-day Prompt Payment Act deadline)
- Payment certification SLA: integer with unit, derived from [A-01] total duration
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Operations** — Per SC-7 prose form. Per SC-2.
- Stage 1: Purchase request → Obligation validation
- Stage 2: Validated obligation → Contract vehicle selection
- Stage 3: Contract vehicle → Vendor notification

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA. One prose boundary
paragraph between Stage 1–Stage 2; one between Stage 2–Stage 3; one after Stage 3.
[SC-3, SC-4, SC-9 / Part A apply.]

**[A-05] PHASE GATE 1** — Mark each ✓ or ✗. Do not allow Finance to begin until all
items are ✓.
- [ ] [A-01] written first; no stage or boundary paragraph precedes it (SC-11)
- [ ] [A-01] includes ≥3 named manual steps with durations
- [ ] [A-02] SLA declared as integer with unit; SC-5 verbatim present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every stage paragraph in [A-03] has four required bold labels per SC-7
- [ ] Every boundary paragraph in [A-04] has seven required bold labels per BOUNDARY BLOCK SCHEMA
- [ ] Every `**Elapsed:**` is an incremental computed sum (SC-3)
- [ ] Every `**Verdict:**` is FRESH or STALE from [A-02] threshold (SC-4)
- [ ] Every `**Incumbent equiv.:**` contains `[A-01]: [named step + duration]` (SC-9)

[Apply SC-6.]

---

### ROLE 2 — Finance

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Finance** — Per SC-7 prose form. Per SC-2.
- Stage 4: Vendor notification → Delivery confirmation receipt
- Stage 5: Delivery confirmation → Invoice submission intake

**[A-07] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: you must extend `**Elapsed:**` from [A-04] final value; do not reset.]
[SC-4: `**Verdict:**` vs [A-02] threshold; do not restate the numeric value.]
[SC-9: every `**Incumbent equiv.:**` must contain `[A-01]: [named step + duration]`.]

**[A-08] PHASE GATE 2** — Mark each ✓ or ✗. Do not allow Commerce to begin until all
items are ✓.
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage paragraph in [A-06] has four required bold labels per SC-7
- [ ] Every boundary paragraph in [A-07] has seven required bold labels
- [ ] `**Elapsed:**` in [A-07] extends [A-04] final value; not reset (SC-3)
- [ ] Every `**Verdict:**` from [A-02] threshold; threshold not restated (SC-4)
- [ ] Every `**Incumbent equiv.:**` contains `[A-01]: [named step + duration]` (SC-9)
- [ ] [SC-12]: You must verify that Commerce's `Citing:` line includes `[A-04]` —
  Operations' boundary checks, two positions prior. Mark ✗ if [A-04] absent.

[Apply SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

([A-04] is required per SC-12 — Operations' boundary checks, two positions prior in the
Operations → Finance → Commerce sequence. Do not cite only Finance's tokens.)

**[A-09] STAGE TRACE — Commerce** — Per SC-7 prose form. Per SC-2.
- Stage 6: Invoice submission → Payment certification review
- Stage 7: Certified payment → Disbursement authorization
- Stage 8: Authorization → Treasury payment release

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA.
[SC-3: extend `**Elapsed:**` from [A-07] final value.]
[SC-4, SC-9 apply.]

**[A-11] STALE ANALYSIS** — Using final `**Elapsed:**` from [A-10], write one labeled
narrative sentence per scenario citing [A-02] by token; do not restate its numeric value.
Cover normal-operation and failure-mode staleness separately.

**[A-12] RECOVERY PRESCRIPTIONS** — [Per SC-13: you must cite [A-01] in this section.]
For every `no handling — see [A-12]` in [A-04]/[A-07]/[A-10] and every `**Data loss:**
YES` in [A-03]/[A-06]/[A-09], write a specific named recovery action. You must use the
formula: `Fall back to [A-01] if [specific named failure condition]` at least once. Do
not omit [A-01]; SC-13 makes its presence mechanically required.

**[A-13] INCUMBENT TOTAL** — [Per Part B. Per SC-10.] Write immediately before [A-14]:

`### [A-13] INCUMBENT TOTAL`
**Operations:** [subtotal] min — [steps from [A-01]]
**Finance:** [subtotal] min — [steps from [A-01]]
**Commerce:** [subtotal] min — [steps from [A-01]]
**Grand Total:** [sum] min

**[A-14] TRADE-OFF ANALYSIS** — [Per SC-13: you must cite [A-01] in this section.] [Per
Part B. Per SC-8.] You must cite `[A-01]`, `[A-02]`, and `[A-13]` — all three required.
Name ≥1 alternative data propagation pattern. Provide ≥2 trade-off dimensions using
[A-13] Grand Total as the numeric comparison endpoint.
