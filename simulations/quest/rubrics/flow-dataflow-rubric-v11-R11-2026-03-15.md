# flow-dataflow — Round 11 Variations

## R10 gap summary before writing

**C-36 not satisfied in R10** — V-03 assigned [A-01] to INCUMBENT BASELINE and produced
it first, but the prompt contained no explicit sequencing prohibition: "no boundary block
may appear before [A-01] is fully produced." Without that prohibition, the model could
write a boundary block before completing [A-01] and still appear compliant. C-36 requires
the constraint to name the lowest-numbered token as a *sequencing guarantee*, not just an
ordering preference.

**C-37 not satisfied in R10** — V-02 introduced Parts A/B in the REGISTER DECLARATION,
but the section header did not assert single-location authority. The SC-9/SC-10 callbacks
referenced "Part A" and "Part B" by name, but an evaluator still needed to consult the
BOUNDARY BLOCK SCHEMA to confirm column header strings. C-37 requires the declaration
header to state explicitly: "An evaluator may determine C-34 and C-35 pass/fail by
reading this section alone." That language was absent in R10.

**C-38 not satisfied in R10** — V-04 (Commerce → Operations → Finance) required Finance
to cite [A-01] and [A-04] but the Citing line instruction was general. No SC named a
*specific token* from two-or-more positions prior, and no phase gate checklist item
verified that token by name. C-38 requires both: an SC naming the skip-level token and
a checklist item that fails if the token is absent.

## Variation axes

- **V-01**: Role sequence (C-38) — Operations → Commerce → Finance; SC-11 names [A-04]
  as required skip-level token; Phase Gate 2 checklist verifies it. C-36 and C-37 not
  targeted (DOMAIN CONTEXT first; no Parts A/B).
- **V-02**: Output format (C-37) — Finance → Operations → Commerce (natural); REGISTER
  DECLARATION Parts A/B with explicit "sole authority" header; SC-9/SC-10 as Part-only
  callbacks. C-36 and C-38 not targeted.
- **V-03**: Inertia framing (C-36) — Operations → Finance → Commerce; [A-01] = INCUMBENT
  BASELINE; SC-11 baseline-first production gate with explicit boundary-block prohibition.
  C-37 and C-38 not targeted.
- **V-04**: Combined (C-36 + C-37) — Operations → Finance → Commerce; [A-01] = INCUMBENT
  BASELINE + SC-11; REGISTER DECLARATION Parts A/B sole authority.
- **V-05**: Combined (C-36 + C-37 + C-38) — Commerce → Operations → Finance; Commerce
  produces [A-01] INCUMBENT BASELINE first; Parts A/B sole authority; SC-12 requires
  Finance to cite [A-04] (two roles prior); Phase Gate 2 verifies [A-04] by name.

---

## V-01

**Axis**: Role sequence — skip-level citation stress test (C-38)

**Hypothesis**: When Finance runs last after Operations → Commerce, its `Citing:` line
must reach back two positions to [A-04] (Operations boundary checks). SC-11 names [A-04]
as the required skip-level token; a Citing line with only Commerce's tokens fails by token
absence rather than prose ambiguity. Phase Gate 2 makes the check explicit. C-36 and C-37
are not targeted: [A-01] is DOMAIN CONTEXT, and the REGISTER DECLARATION uses standard
(non-Parts) format. This isolates the C-38 enforcement mechanism.

---

You are tracing data through a retail stock-replenishment-to-financial-settlement pipeline.
Three expert roles run in the sequence **Operations → Commerce → Finance**. Operations
establishes the domain context, manual-process baseline, and the staleness SLA that all
subsequent roles must cite. Commerce and Finance cite Operations' artifacts by token; they
may not redeclare or re-derive either the staleness threshold or the incumbent baseline.

The physical pipeline flows: stock replenishment trigger → warehouse receiving → WMS
stock-on-hand update → Commerce inventory cache → catalog availability flag → invoice
generation → AP matching → GL posting.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. Every citation anywhere in this output must use
the `[A-xx]` token exactly as spelled in this table. A citation to a target not listed
here is a protocol violation.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Operations | Entity vocabulary, staleness SLA (immutable after Stage 1), downstream consumer, business cadence |
| [A-02] | INCUMBENT BASELINE | Operations | Manual stock replenishment process replaced by this pipeline; ≥3 named steps with durations; ≥1 entity from [A-01] |
| [A-03] | STAGE TRACE — Operations | Operations | Replenishment trigger → dock scan → WMS update; stage tables |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; interleaved between Operations stages; Incumbent Equiv. cells cite [A-02] |
| [A-05] | PHASE GATE 1 | Operations | Self-verification checklist; all items ✓ before Commerce begins |
| [A-06] | STAGE TRACE — Commerce | Commerce | WMS snapshot → Commerce inventory cache → catalog availability flag; stage tables |
| [A-07] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cells cite [A-02] |
| [A-08] | PHASE GATE 2 | Commerce | Self-verification checklist; all items ✓ before Finance begins |
| [A-09] | STAGE TRACE — Finance | Finance | Catalog flag → invoice generation → AP matching → GL posting; stage tables |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cells cite [A-02] |
| [A-11] | STALE ANALYSIS | Finance | Normal-operation and failure-mode elapsed vs [A-01] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery per loss point and "no handling" annotation; formula: `Fall back to [A-02] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Finance | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; additive breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Finance | Required named section; cites [A-01], [A-02], and [A-13] by token; ≥1 alternative pattern; ≥2 trade-off dimensions |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout. All stage blocks and boundary blocks
are rendered as markdown tables. An evaluator may verify any required field by scanning
for the named column; no prose reading is required.

**Per-field compliance markers (tabular register):**

| Required Field | Compliance Marker | Disqualifying Form |
|----------------|-------------------|--------------------|
| Domain entity at boundary | `Entity` column — named entity from [A-01] | "data" or "records" alone |
| Error handling | `Error Handling` column — named mechanism or `no handling — see [A-12]` | Silence / omitted column |
| Elapsed (cumulative) | `Elapsed (cumul.)` column — numeric sum of all prior stage and boundary latencies | Partial sum or deferred to [A-11] |
| Freshness verdict | `Verdict` column — `FRESH` or `STALE` derived from [A-01] threshold | Any value other than FRESH/STALE |
| Schema state | `Schema Delta` column — named field changes or `NONE` | Omitted column |
| Data loss flag | `Data Loss Flag` column — `YES — [named loss point]` or `NO` | Generic "errors may occur" |
| Stage latency | `Stage Latency` column (stage tables) — explicit value, range, or characterization | Inferred from boundary elapsed only |
| Incumbent equivalent | `Incumbent Equiv.` column — form `[A-02]: [named manual step + duration]`; `[A-02]` token required | Bare duration without `[A-02]` token; omitted column |

---

### BOUNDARY BLOCK SCHEMA

Standalone section declared before any role output. Every required column is named here.
Role instructions reference this section by name; they do not restate field requirements.
An evaluator verifies boundary block completeness by column existence alone.

**Every boundary block must be a markdown table with the following columns, in this order:**

| Column | Required Content |
|--------|-----------------|
| Entity | Named entity from [A-01] vocabulary. "data" or "records" alone fails. |
| Elapsed (cumul.) | Sum of all prior stage and boundary latencies, in minutes. Computed inside this block; not deferred. |
| Verdict | `FRESH` or `STALE` — derived by comparing Elapsed (cumul.) against the [A-01] threshold. Cite [A-01] by token; do not restate its numeric value. |
| Error Handling | Named retry / dead-letter / rollback mechanism, or `no handling — see [A-12]`. Silence fails. |
| Schema Delta | Named field-level changes at this boundary, or `NONE`. |
| Data Loss Flag | `YES — [named loss point]` or `NO`. Generic language fails. |
| Incumbent Equiv. | `[A-02]: [named manual step + duration]`. `[A-02]` token required; bare duration is a protocol violation. |

A boundary block that omits any column, or is rendered as a labeled field list, fails
this schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Operations opens with
`Citing: [A-xx], [A-yy], ...` listing every token from prior roles this role builds on.
Operations is first and has no prior tokens. Prose back-references ("as established
above") do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the BOUNDARY
CHECK table between Stage N and Stage N+1 is fully populated per the BOUNDARY BLOCK
SCHEMA. Write the table. Confirm all seven columns are populated. Then write Stage N+1.
[Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed computation**: The `Elapsed (cumul.)` column in each
BOUNDARY CHECK must be the sum of all prior stage latencies and all prior boundary
latencies up to and including this boundary. Compute it inside the boundary block; it may
not be deferred to [A-11]. [Apply SC-3 at every boundary block.]

**SC-4 — Binary freshness verdict**: Each boundary block `Verdict` must read `FRESH` or
`STALE`, derived by comparing Elapsed (cumul.) against the [A-01] threshold. Cite [A-01]
by token; do not restate its value. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability of staleness threshold**: Operations must append to [A-01] verbatim:
"This threshold is fixed. No subsequent role may revise it after Stage 1 is written."
Commerce and Finance may not redeclare or adjust the threshold.

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required outputs at the end of
Operations and Commerce respectively. Each is a checklist with named criterion identifiers.
The next role may not begin until all items are ✓. [Apply SC-6 before role transitions.]

**SC-7 — Stage table format**: Every stage block is a markdown table with required
columns: `Stage Latency | Schema In | Schema Out | Data Loss Flag`. Stage Latency must be
an explicit annotation; it may not be omitted. [Apply SC-7 at every stage block.]

**SC-8 — Trade-off analysis as required section**: [A-14] TRADE-OFF ANALYSIS is a
structurally required named section. It must cite [A-02] (manual baseline), [A-01]
(threshold dimension), and [A-13] (numeric incumbent total) by token — all three required.
Name ≥1 alternative data propagation pattern. Provide ≥2 trade-off dimensions using
[A-13] Grand Total as the comparison endpoint. Omitting any token fails SC-8.
[Apply SC-8 when producing [A-14].]

**SC-9 — Per-boundary incumbent equivalent cell form**: Every `Incumbent Equiv.` cell must
cite `[A-02]` by token and name the corresponding manual step with its duration. Required
form: `[A-02]: [named step + duration]`. A bare duration without the `[A-02]` token is a
protocol violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Before writing [A-14], produce [A-13]
INCUMBENT TOTAL. Sum all `Incumbent Equiv.` cell values from [A-04], [A-07], and [A-10].
Show additive breakdown by role (Operations subtotal, Commerce subtotal, Finance subtotal,
Grand Total). [A-14] must cite [A-13] by token as the numeric comparison endpoint. A
TRADE-OFF ANALYSIS that cites [A-02] without first producing and citing [A-13] fails
SC-10. [Apply SC-10 before writing [A-14].]

**SC-11 — Skip-level citation in Finance**: Finance's `Citing:` line must include `[A-04]`
— Operations' boundary checks, produced two roles prior. Commerce is Finance's immediate
predecessor; a `Citing:` line that names only Commerce's tokens without `[A-04]` fails
SC-11. The Phase Gate 2 checklist ([A-08]) explicitly pre-announces this requirement; the
Finance role instructions name [A-04] in the required Citing line. Omitting [A-04] from
Finance's Citing line is detectable as a missing token, not a prose gap.

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required.]

**[A-01] DOMAIN CONTEXT** — Write this before Stage 1. Include:
- Entity vocabulary: stock replenishment trigger, warehouse receipt record, WMS
  stock-on-hand quantity, Commerce inventory cache entry, catalog availability flag,
  AP matching entry, GL accrual line
- Downstream consumer and business cadence (e.g., daily financial close at 17:00)
- Staleness SLA: maximum elapsed time from stock replenishment trigger to GL posting
  completion. Declare as an integer with unit.
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-02] INCUMBENT BASELINE** — Write immediately after [A-01] and before Stage 1.
Describe the manual stock replenishment and settlement process this pipeline replaces.
Include ≥3 named manual steps with durations (e.g., "Manual receiving count sheet and
supervisor sign-off: 2 h", "Spreadsheet stock update emailed to Commerce team: 45 min",
"Manual invoice matching and GL journal entry: 90 min"). Use ≥1 entity name from [A-01].
This artifact is the source for all `Incumbent Equiv.` cells in [A-04], [A-07], [A-10].

**[A-03] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 1: Stock replenishment trigger → Warehouse receiving dock scan
- Stage 2: Dock scan → WMS stock-on-hand quantity update

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns).
One block between Stage 1–Stage 2; one block after Stage 2.
[SC-3 applies.] [SC-4 applies.] [SC-9 applies.]

**[A-05] PHASE GATE 1** — Produce and tick before Commerce begins. Mark each ✓ or ✗:
- [ ] [A-01] contains staleness SLA as integer with unit, plus SC-5 verbatim statement
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
- Stage 3: WMS stock-on-hand quantity → Commerce platform inventory cache
- Stage 4: Commerce platform inventory cache → Storefront catalog availability flag

**[A-07] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: Elapsed (cumul.) extends the final value in [A-04]; do not reset to zero.]
[SC-4: Verdict vs [A-01] threshold; do not redeclare threshold value.]
[SC-9: every Incumbent Equiv. cell form `[A-02]: [named step + duration]`.]

**[A-08] PHASE GATE 2** — Produce and tick before Finance begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] is a table with all four required columns per SC-7
- [ ] Every block in [A-07] has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] final value; not reset (SC-3)
- [ ] Every `Verdict` derives from [A-01] threshold without redeclaring its value (SC-4)
- [ ] Every `Incumbent Equiv.` cell uses form `[A-02]: [named step + duration]` (SC-9)
- [ ] SC-11 pre-announcement: Finance's `Citing:` line must include `[A-04]`
  (Operations boundary checks, two roles prior) — note this requirement for Finance

Finance may not begin until all items are ✓. [Apply SC-6.]

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]
([A-04] is required per SC-11 — Operations boundary checks, two roles prior. Citing only
[A-07] without [A-04] fails SC-11. The elapsed chain in [A-10] must extend from the
final value in [A-07], which itself extended from [A-04].)

**[A-09] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Use entity names from [A-01].
- Stage 5: Catalog availability flag → Invoice generation trigger
- Stage 6: Invoice generation trigger → AP matching entry
- Stage 7: AP matching → GL accrual line posting

**[A-10] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: extend Elapsed (cumul.) from final value in [A-07].]
[SC-4: Verdict vs [A-01] threshold.]
[SC-9: every Incumbent Equiv. cell form `[A-02]: [named step + duration]`.]

**[A-11] STALE ANALYSIS** — Using Elapsed (cumul.) from [A-10] final boundary:

| Entity ([A-01]) | Normal elapsed | Failure-mode elapsed | [A-01] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

Produce separate rows for normal-operation and failure-mode staleness. Cite [A-01] by
token; do not restate the numeric threshold value.

**[A-12] RECOVERY PRESCRIPTIONS** — For every `no handling — see [A-12]` annotation in
[A-04]/[A-07]/[A-10] and every `Data Loss Flag: YES` in [A-03]/[A-06]/[A-09], provide a
specific named recovery action. Required formula structure:
`Fall back to [A-02] if [specific named failure condition]`
Cite [A-02] using this exact formula at least once.

**[A-13] INCUMBENT TOTAL** — Per SC-10. Produce immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Operations | [sum of [A-04] Incumbent Equiv. values] | [step names from [A-02]] |
| Commerce | [sum of [A-07] Incumbent Equiv. values] | [step names from [A-02]] |
| Finance | [sum of [A-10] Incumbent Equiv. values] | [step names from [A-02]] |
| **Grand Total** | | |

[A-14] must cite this table by token `[A-13]`.

**[A-14] TRADE-OFF ANALYSIS** — [SC-8 applies.] Required named section. Cite [A-01],
[A-02], and [A-13] — all three tokens required. Name ≥1 alternative pattern (e.g.,
event-driven CDC, real-time dual-write). Provide ≥2 trade-off dimensions using [A-13]
Grand Total as the numeric comparison endpoint.

---

---

## V-02

**Axis**: Output format — REGISTER DECLARATION Parts A/B as sole C-34/C-35 authority
(C-37)

**Hypothesis**: When the REGISTER DECLARATION header explicitly states "An evaluator may
determine C-34 and C-35 pass/fail by reading this section alone" and Parts A/B contain
the canonical compliance specifications, with SC-9 and SC-10 as callbacks to those Parts
rather than independent declarations, the model treats the REGISTER DECLARATION as the
binding source and the BOUNDARY BLOCK SCHEMA as a structural scaffold only. Natural
Finance → Operations → Commerce order preserves C-16 PASS while isolating the C-37 axis.
C-36 and C-38 are not targeted.

---

You are tracing data through a retail purchase-order-to-inventory pipeline. Three expert
roles run in the sequence **Finance → Operations → Commerce**. Finance establishes the PO
staleness SLA and manual-process baseline. Operations and Commerce extend the trace and
cite Finance's artifacts by token; they may not redeclare or re-derive either.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Finance | Entity vocabulary, staleness SLA (immutable after Stage 1), downstream consumer, business cadence |
| [A-02] | INCUMBENT BASELINE | Finance | Manual PO and AP process replaced by this pipeline; ≥3 named steps with durations; ≥1 entity from [A-01] |
| [A-03] | STAGE TRACE — Finance | Finance | PO creation → AP accrual → GL posting; stage tables |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | Boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-02] |
| [A-05] | PHASE GATE 1 | Finance | Checklist; all ✓ before Operations |
| [A-06] | STAGE TRACE — Operations | Operations | Dock scan → WMS stock-on-hand update; stage tables |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | Boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cites [A-02] |
| [A-08] | PHASE GATE 2 | Operations | Checklist; all ✓ before Commerce |
| [A-09] | STAGE TRACE — Commerce | Commerce | WMS snapshot → Commerce platform cache → catalog availability flag; stage tables |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | Boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cites [A-02] |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-01] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point; formula `Fall back to [A-02] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Commerce | Aggregates all Incumbent Equiv. cells; breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required section; cites [A-01], [A-02], [A-13] by token; ≥1 pattern; ≥2 dimensions |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell form)
and C-35 (INCUMBENT TOTAL section format). An evaluator may determine pass/fail for both
criteria by reading this section alone, without consulting the BOUNDARY BLOCK SCHEMA or
role instructions. Structural constraints SC-9 and SC-10 are callbacks to Parts A and B
respectively; they do not independently restate compliance requirements.**

**Part A — Field compliance markers (boundary block columns):**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-01] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum of all prior stage and boundary latencies, in minutes | Partial sum; deferred total |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE`, derived from [A-01] threshold | Any other value |
| Error handling | `Error Handling` | Named retry/dead-letter/rollback mechanism, or exactly `no handling — see [A-12]` | Silence; "TBD"; omitted column |
| Schema change | `Schema Delta` | Named field-level additions, removals, or type changes, or exactly `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | "errors may occur"; generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-02]: [named manual step + duration]` — `[A-02]` token required; cell omitting it is a protocol violation | Bare duration; token omitted; column absent |
| Stage latency | `Stage Latency` (stage table) | Explicit value, range, or characterization (real-time / near-real / batch / daily) | Inferred from boundary elapsed |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Markdown table with columns: `Role \| Incumbent Equiv. subtotal \| Steps cited`; rows for Finance, Operations, Commerce, and Grand Total; all subtotal values numeric | Prose-only summary; missing role breakdown; no Grand Total row |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | Must include all three token citations `[A-01]`, `[A-02]`, and `[A-13]`; ≥1 alternative pattern named; ≥2 trade-off dimensions | Any one of the three tokens absent; alternative pattern not named |

---

### BOUNDARY BLOCK SCHEMA

Standalone section before any role output. Lists required column names for boundary block
structural completeness verification. Column header strings must match REGISTER DECLARATION
Part A spellings exactly. Role instructions reference this section by name only.

**Every boundary block must be a markdown table with these columns, in this order:**
`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

A column that is absent, renamed, or does not match the Part A header string fails the
schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Finance opens with
`Citing: [A-xx], [A-yy], ...`. Prose back-references do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding
boundary table is fully populated per the BOUNDARY BLOCK SCHEMA. [Apply SC-2 before every
stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` is computed inside each boundary block;
not deferred. [Per REGISTER DECLARATION Part A, `Elapsed (cumul.)` row.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` from [A-01] threshold. Cite
[A-01] by token. [Per REGISTER DECLARATION Part A, `Verdict` row.]

**SC-5 — Immutability**: Finance appends to [A-01] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written."

**SC-6 — Phase gate**: [A-05] and [A-08] are required checklists at phase transitions.
Next role may not begin until all items ✓.

**SC-7 — Stage table format**: Every stage block is a table with columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. [Per REGISTER DECLARATION
Part A, `Stage Latency` row.] [Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [Per REGISTER DECLARATION Part B, TRADE-OFF
ANALYSIS row.] All three tokens required. Named alternative pattern required. ≥2
dimensions required. [Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: [Per REGISTER DECLARATION Part A, `Incumbent
Equiv.` row.] Form: `[A-02]: [named step + duration]`. Token omission is a protocol
violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [Per REGISTER DECLARATION Part B, INCUMBENT
TOTAL row.] Produce [A-13] immediately before [A-14]. [A-14] cites [A-13] by token as
the numeric comparison endpoint. [Apply SC-10 before writing [A-14].]

---

### ROLE 1 — Finance

[Finance runs first. No Citing line required.]

**[A-01] DOMAIN CONTEXT** — Write before Stage 1. Entity vocabulary: purchase order (PO),
AP accrual line, supplier receipt voucher, WMS stock-on-hand quantity, catalog availability
flag. Include downstream consumer, business cadence, and staleness SLA as an integer with
unit. Append SC-5 verbatim immutability statement.

**[A-02] INCUMBENT BASELINE** — Write immediately after [A-01] and before Stage 1.
Manual PO-to-inventory process replaced by this pipeline. ≥3 named steps with durations.
≥1 entity from [A-01]. This artifact is the source for all `Incumbent Equiv.` cells
across all roles. [Per REGISTER DECLARATION Part A, `Incumbent Equiv.` row.]

**[A-03] STAGE TRACE — Finance** — Stage 1: Supplier EDI → PO entry. Stage 2: PO entry
→ AP accrual. Stage 3: AP accrual → GL posting. Per SC-7. Per SC-2.

**[A-04] BOUNDARY CHECKS — Finance** — One boundary table after each stage, per BOUNDARY
BLOCK SCHEMA. Column header spellings must match REGISTER DECLARATION Part A exactly.
[SC-3, SC-4, SC-9 apply.]

**[A-05] PHASE GATE 1** — Tick ✓ or ✗ before Operations:
- [ ] [A-01] SLA declared as integer with unit; SC-5 verbatim statement present
- [ ] [A-02] includes ≥3 named steps with durations; ≥1 entity from [A-01]
- [ ] Every stage in [A-03] has four required columns per SC-7
- [ ] Every block in [A-04] has all seven columns; headers match REGISTER DECLARATION
      Part A spellings exactly
- [ ] Every `Incumbent Equiv.` cell: `[A-02]: [named step + duration]` (SC-9 / Part A)

Operations may not begin until all items ✓. [SC-6.]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Stage 4: AP accrual confirmation → Dock scan.
Stage 5: Dock scan → WMS stock-on-hand update. Per SC-7. Per SC-2.

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns; headers
match REGISTER DECLARATION Part A exactly). [SC-3: extend Elapsed (cumul.) from [A-04]
final value.] [SC-4, SC-9 apply.]

**[A-08] PHASE GATE 2** — Tick ✓ or ✗ before Commerce:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every [A-06] stage table has four required columns per SC-7
- [ ] Every [A-07] boundary table has seven columns; headers match REGISTER DECLARATION
      Part A exactly
- [ ] `Elapsed (cumul.)` extends [A-04] final value; no reset (SC-3)
- [ ] Every `Incumbent Equiv.` cell: `[A-02]: [named step + duration]` (SC-9 / Part A)

Commerce may not begin until all items ✓. [SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

**[A-09] STAGE TRACE — Commerce** — Stage 6: WMS snapshot → Commerce platform cache.
Stage 7: Platform cache → Catalog availability flag. Per SC-7. Per SC-2.

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns; headers
match REGISTER DECLARATION Part A exactly). [SC-3: extend from [A-07].] [SC-4, SC-9.]

**[A-11] STALE ANALYSIS** — Table: Entity | Normal elapsed | Failure-mode elapsed |
[A-01] threshold | Verdict. Cite [A-01] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — Named recovery per loss point and no-handling flag.
Formula: `Fall back to [A-02] if [specific condition]`.

**[A-13] INCUMBENT TOTAL** — [Per REGISTER DECLARATION Part B, INCUMBENT TOTAL row. Per
SC-10.] Produce immediately before [A-14]. Table with columns
`Role | Incumbent Equiv. subtotal | Steps cited`; rows for Finance, Operations, Commerce,
Grand Total. Cite as `[A-13]` in [A-14].

**[A-14] TRADE-OFF ANALYSIS** — [Per REGISTER DECLARATION Part B, TRADE-OFF ANALYSIS row.
Per SC-8.] Required. Cite `[A-01]`, `[A-02]`, and `[A-13]` — all three tokens required.
Name ≥1 alternative pattern. ≥2 trade-off dimensions with [A-13] Grand Total as numeric
comparison endpoint.

---

---

## V-03

**Axis**: Inertia framing — baseline-first artifact ordering (C-36)

**Hypothesis**: Assigning [A-01] to INCUMBENT BASELINE and adding SC-11 as an explicit
sequencing prohibition — "no boundary block may appear before [A-01] is fully produced"
— forces every `Incumbent Equiv.` cell to cite a fully-written artifact. The token
assignment is non-arbitrary: the ARTIFACT REGISTRY description states "(First artifact
produced — SC-11 applies)" on the [A-01] row, so the model treats lowest-numbered token
= first produced as a structural guarantee, not a suggestion. Role sequence Operations →
Finance → Commerce is non-natural (natural is Finance → Operations → Commerce), satisfying
C-26. C-37 and C-38 are not targeted.

---

You are tracing data through a retail purchase-order-to-inventory pipeline. Three expert
roles run in the sequence **Operations → Finance → Commerce**. Operations runs first and
produces both the incumbent manual-process baseline and the domain context — establishing
the inertia story before any pipeline stage is traced. Finance and Commerce cite
Operations' baseline and threshold by token; they may not redeclare or re-derive either.

The incumbent manual process is the primary competitive frame. Every boundary block
evaluates this pipeline against what the manual process costs at the same point.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. The lowest-numbered token ([A-01]) is produced
first; every subsequent artifact is produced in token order. A boundary block that appears
in the output before [A-01] is fully written is a sequencing violation (SC-11).

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Operations | Manual PO and warehouse process replaced by this pipeline; ≥3 named steps with durations; produced FIRST, before [A-02] and before any stage trace. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, staleness SLA (immutable after Stage 1), downstream consumer, business cadence; SLA declared with reference to [A-01] total manual duration |
| [A-03] | STAGE TRACE — Operations | Operations | Dock scan → WMS stock-on-hand update; stage tables |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | 7-column boundary tables; Incumbent Equiv. cells cite [A-01] |
| [A-05] | PHASE GATE 1 | Operations | Checklist; all ✓ before Finance begins |
| [A-06] | STAGE TRACE — Finance | Finance | PO creation → AP accrual → GL posting; stage tables |
| [A-07] | BOUNDARY CHECKS — Finance | Finance | 7-column boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Finance | Checklist; all ✓ before Commerce begins |
| [A-09] | STAGE TRACE — Commerce | Commerce | WMS snapshot → Commerce platform cache → catalog availability flag; stage tables |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | 7-column boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cells cite [A-01] |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point; formula `Fall back to [A-01] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; additive breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required section; cites [A-01], [A-02], and [A-13] by token; ≥1 alternative; ≥2 dimensions |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout. All stage blocks and boundary blocks
are rendered as markdown tables.

**Per-field compliance markers (tabular register):**

| Required Field | Compliance Marker | Disqualifying Form |
|----------------|-------------------|--------------------|
| Domain entity at boundary | `Entity` column — named entity from [A-02] | "data" or "records" alone |
| Error handling | `Error Handling` column — named mechanism or `no handling — see [A-12]` | Silence / omitted column |
| Elapsed (cumulative) | `Elapsed (cumul.)` column — numeric sum of all prior stage and boundary latencies | Partial sum or deferred |
| Freshness verdict | `Verdict` column — `FRESH` or `STALE` derived from [A-02] threshold | Any other value |
| Schema state | `Schema Delta` column — named field changes or `NONE` | Omitted column |
| Data loss flag | `Data Loss Flag` column — `YES — [named loss point]` or `NO` | Generic language |
| Stage latency | `Stage Latency` column (stage tables) — explicit value, range, or characterization | Inferred from boundary |
| Incumbent equivalent | `Incumbent Equiv.` column — form `[A-01]: [named step + duration]`; `[A-01]` token required | Bare duration; token omitted; column absent |

---

### BOUNDARY BLOCK SCHEMA

Standalone section declared before any role output. Every required column is named here.
An evaluator verifies completeness by column existence alone.

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

**SC-1 — Citation opener**: Every role other than Operations opens with
`Citing: [A-xx], [A-yy], ...`. Citing `[A-01]` (INCUMBENT BASELINE) is required in every
non-first role's Citing line — it must appear. Prose back-references do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding
BOUNDARY CHECK table is fully populated per BOUNDARY BLOCK SCHEMA.
[Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` computed inside each boundary block;
not deferred. [Apply SC-3 at every boundary block.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` vs [A-02] threshold. Cite
[A-02] by token. [Apply SC-4 at every boundary block.]

**SC-5 — Immutability**: Operations appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written." The threshold must be declared
as an integer with unit, derived from [A-01] total manual duration plus acceptable
pipeline latency headroom.

**SC-6 — Phase gate**: [A-05] and [A-08] are required checklists. Next role may not
begin until all items ✓.

**SC-7 — Stage table format**: Every stage block is a table with columns
`Stage Latency | Schema In | Schema Out | Data Loss Flag`. Stage Latency must be explicit.
[Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [A-14] is a structurally required named section.
Must cite [A-01] (manual baseline), [A-02] (SLA dimension), and [A-13] (numeric total)
by token — all three required. ≥1 alternative pattern. ≥2 dimensions.
[Apply SC-8 when producing [A-14].]

**SC-9 — Per-boundary incumbent equivalent**: Every `Incumbent Equiv.` cell form:
`[A-01]: [named manual step + duration]`. The `[A-01]` token is required; bare durations
are protocol violations. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: Produce [A-13] immediately before [A-14].
Sum Incumbent Equiv. values from [A-04], [A-07], [A-10]; show role breakdown (Operations
subtotal, Finance subtotal, Commerce subtotal, Grand Total); cite [A-13] in [A-14] as
numeric comparison endpoint. [Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] INCUMBENT BASELINE must be the first
artifact written in this output. No boundary block and no stage trace may appear in the
output before [A-01] is fully produced. Operations may not write Stage 1 until [A-01] is
complete. The ARTIFACT REGISTRY assigns token [A-01] to INCUMBENT BASELINE specifically
to enforce this sequencing: the lowest-numbered token is produced first, so every
`Incumbent Equiv.` cell that cites [A-01] references an artifact already fully written at
the time the boundary block is produced. A boundary block appearing before [A-01] is
complete — even if [A-01] is eventually produced — is a sequencing violation.

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required. The incumbent baseline leads.]

**[A-01] INCUMBENT BASELINE** — Write this FIRST, before any domain context or stage
trace. Per SC-11: no subsequent artifact in this output may be produced before [A-01] is
fully written. Describe the manual warehouse-and-procurement process this pipeline
replaces. Include ≥3 named manual steps with durations (e.g., "Paper PO fax to supplier:
4 h", "Receiving clerk manual count and entry: 90 min", "Spreadsheet stock update emailed
to Commerce team: 30 min"). Use entity names that will reappear in [A-02]. This is the
source for every `Incumbent Equiv.` cell in [A-04], [A-07], and [A-10]. All subsequent
roles must cite [A-01] in their opening Citing line.

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 entity names from [A-01]): purchase order, warehouse receipt
  record, WMS stock-on-hand quantity, catalog availability flag
- Downstream consumer and business cadence
- Staleness SLA: declare as an integer with unit. Derive from [A-01] total manual duration
  plus acceptable pipeline latency headroom.
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 1: AP accrual confirmation → Warehouse receiving dock scan
- Stage 2: Dock scan → WMS stock-on-hand quantity update

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns).
One block between Stage 1–Stage 2; one block after Stage 2.
[SC-3 applies.] [SC-4 applies.] [SC-9 applies: every cell cites [A-01] — a fully-written
artifact from line 1 of this output.]

**[A-05] PHASE GATE 1** — Produce and tick before Finance begins. Mark each ✓ or ✗:
- [ ] [A-01] was produced first, before any stage trace or boundary block (SC-11)
- [ ] [A-01] includes ≥3 named steps with durations
- [ ] [A-02] declares SLA as integer with unit derived from [A-01]; SC-5 verbatim present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every stage in [A-03] has four required columns per SC-7
- [ ] Every block in [A-04] has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] Every `Elapsed (cumul.)` computed inside block (SC-3)
- [ ] Every `Verdict` is FRESH/STALE vs [A-02] threshold (SC-4)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)

Finance may not begin until all items ✓. [Apply SC-6.]

---

### ROLE 2 — Finance

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 3: Supplier EDI confirmation → PO entry in ERP
- Stage 4: PO entry → AP accrual line creation
- Stage 5: AP accrual → GL posting

**[A-07] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: extend Elapsed (cumul.) from [A-04] final value; do not reset.]
[SC-4: Verdict vs [A-02] threshold; do not redeclare threshold value.]
[SC-9: every Incumbent Equiv. cell: `[A-01]: [named step + duration]`.]

**[A-08] PHASE GATE 2** — Produce and tick before Commerce begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1); [A-01] present in Citing line
- [ ] Every stage in [A-06] has four required columns per SC-7
- [ ] Every block in [A-07] has all seven columns per BOUNDARY BLOCK SCHEMA
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] final value; not reset (SC-3)
- [ ] Every `Verdict` derives from [A-02] threshold without redeclaring its value (SC-4)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9)

Commerce may not begin until all items ✓. [Apply SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

**[A-09] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 6: WMS stock-on-hand quantity → Commerce platform inventory cache
- Stage 7: Commerce platform cache → Storefront catalog availability flag

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns).
[SC-3: extend from [A-07] final value.] [SC-4: Verdict vs [A-02] threshold.] [SC-9.]

**[A-11] STALE ANALYSIS** — Table: Entity | Normal elapsed | Failure-mode elapsed |
[A-02] threshold | Verdict. Cite [A-02] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — Named recovery per loss point and no-handling flag.
Required formula: `Fall back to [A-01] if [specific condition]`. Cite [A-01] by token.

**[A-13] INCUMBENT TOTAL** — Per SC-10. Produce immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Operations | | |
| Finance | | |
| Commerce | | |
| **Grand Total** | | |

Cite as `[A-13]` in [A-14].

**[A-14] TRADE-OFF ANALYSIS** — Per SC-8. Required. Cite `[A-01]`, `[A-02]`, and
`[A-13]` — all three tokens required. ≥1 alternative pattern. ≥2 dimensions with [A-13]
Grand Total as numeric endpoint.

---

---

## V-04

**Axis**: Combined — C-36 (baseline-first) + C-37 (Parts A/B sole authority)

**Hypothesis**: The two format improvements are compatible and independently verifiable:
SC-11 enforces production sequencing (C-36) while the REGISTER DECLARATION Parts A/B
header enforces single-location C-34/C-35 authority (C-37). Neither requires a non-natural
role ordering beyond what C-26 demands; Operations → Finance → Commerce satisfies C-26
while keeping the elapsed chain coherent. The combined prompt is tested for any
interference between the two constraints — specifically whether SC-11's baseline-first
language competes with or reinforces the Part A/Part B callback structure. C-38 not
targeted.

---

You are tracing data through a retail purchase-order-to-inventory pipeline. Three expert
roles run in the sequence **Operations → Finance → Commerce**. Operations produces the
incumbent manual-process baseline as the first artifact in this output, followed by the
domain context. Finance and Commerce cite Operations' artifacts by token; they may not
redeclare or re-derive either the staleness threshold or the incumbent baseline.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. The lowest-numbered token ([A-01]) is produced
first; subsequent artifacts are produced in token order. A boundary block appearing before
[A-01] is fully written is a sequencing violation (SC-11).

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Operations | Manual PO and warehouse process replaced by this pipeline; ≥3 named steps with durations; produced FIRST before [A-02] and before any stage trace. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Operations | Entity vocabulary, staleness SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total duration |
| [A-03] | STAGE TRACE — Operations | Operations | Dock scan → WMS stock-on-hand update; stage tables |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | Boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01] |
| [A-05] | PHASE GATE 1 | Operations | Checklist; all ✓ before Finance |
| [A-06] | STAGE TRACE — Finance | Finance | PO creation → AP accrual → GL posting; stage tables |
| [A-07] | BOUNDARY CHECKS — Finance | Finance | Boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cites [A-01] |
| [A-08] | PHASE GATE 2 | Finance | Checklist; all ✓ before Commerce |
| [A-09] | STAGE TRACE — Commerce | Commerce | WMS snapshot → Commerce platform cache → catalog availability flag; stage tables |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | Boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cites [A-01] |
| [A-11] | STALE ANALYSIS | Commerce | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point; formula `Fall back to [A-01] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Commerce | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Commerce | Required section; cites [A-01], [A-02], and [A-13] by token; ≥1 alternative; ≥2 dimensions |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell form)
and C-35 (INCUMBENT TOTAL section format). An evaluator may determine pass/fail for both
criteria by reading this section alone, without consulting the BOUNDARY BLOCK SCHEMA or
role instructions. Structural constraints SC-9 and SC-10 are callbacks to Parts A and B
respectively; they do not independently restate compliance requirements.**

**Part A — Field compliance markers (boundary block columns):**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum of all prior stage and boundary latencies, in minutes | Partial sum; deferred total |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE`, derived from [A-02] threshold | Any other value |
| Error handling | `Error Handling` | Named retry/dead-letter/rollback, or exactly `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level changes, or exactly `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` — `[A-01]` token required; omission is a protocol violation | Bare duration; token omitted; column absent |
| Stage latency | `Stage Latency` (stage table) | Explicit value, range, or characterization | Inferred from boundary elapsed |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Markdown table: `Role \| Incumbent Equiv. subtotal \| Steps cited`; rows for Operations, Finance, Commerce, Grand Total; all subtotals numeric | Prose-only; missing role row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | All three tokens `[A-01]`, `[A-02]`, `[A-13]` present; ≥1 alternative pattern; ≥2 dimensions | Any token absent; no pattern named |

---

### BOUNDARY BLOCK SCHEMA

Standalone section before any role output. Column header strings must match REGISTER
DECLARATION Part A spellings exactly. Role instructions reference this section by name
only; they do not restate field requirements.

**Every boundary block must be a markdown table with these columns, in this order:**
`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

A column absent or renamed fails the schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Operations opens with
`Citing: [A-xx], [A-yy], ...`. Citing [A-01] (INCUMBENT BASELINE) is required in every
non-first role's Citing line. Prose back-references do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding
boundary table is fully populated per BOUNDARY BLOCK SCHEMA.
[Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` computed inside each block; not
deferred. [Per REGISTER DECLARATION Part A, `Elapsed (cumul.)` row.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` vs [A-02] threshold. Cite
[A-02] by token. [Per REGISTER DECLARATION Part A, `Verdict` row.]

**SC-5 — Immutability**: Operations appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written." Declare as integer with unit,
derived from [A-01] total manual duration plus pipeline headroom.

**SC-6 — Phase gate**: [A-05] and [A-08] are required checklists. Next role may not
begin until all items ✓.

**SC-7 — Stage table format**: Columns `Stage Latency | Schema In | Schema Out | Data
Loss Flag`. Stage Latency explicit. [Per REGISTER DECLARATION Part A, `Stage Latency`
row.] [Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [Per REGISTER DECLARATION Part B, TRADE-OFF
ANALYSIS row.] All three tokens required. ≥1 pattern. ≥2 dimensions.
[Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: [Per REGISTER DECLARATION Part A, `Incumbent
Equiv.` row.] Form: `[A-01]: [named step + duration]`. Token omission is a protocol
violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [Per REGISTER DECLARATION Part B, INCUMBENT
TOTAL row.] Produce [A-13] immediately before [A-14]; cite [A-13] in [A-14] as numeric
endpoint. [Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] INCUMBENT BASELINE must be the first
artifact written in this output. No boundary block and no stage trace may appear before
[A-01] is fully produced. Operations may not write Stage 1 until [A-01] is complete. The
ARTIFACT REGISTRY assigns token [A-01] to INCUMBENT BASELINE specifically to enforce this
sequencing: the lowest-numbered token is produced first, guaranteeing that every
`Incumbent Equiv.` cell citing [A-01] references a fully-written artifact. A boundary
block appearing before [A-01] is complete is a sequencing violation regardless of whether
[A-01] is eventually produced.

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required. The incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST, before any domain context or stage trace.
Per SC-11. Describe the manual warehouse-and-procurement process this pipeline replaces.
≥3 named steps with durations. Use entity names that will reappear in [A-02]. This is the
source for all `Incumbent Equiv.` cells across all roles. [Per REGISTER DECLARATION Part A,
`Incumbent Equiv.` row.]

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include entity vocabulary
(reuse ≥2 entity names from [A-01]), downstream consumer, business cadence, and staleness
SLA as an integer with unit derived from [A-01] total manual duration. Append SC-5
verbatim immutability statement.

**[A-03] STAGE TRACE — Operations** — Per SC-7. Per SC-2.
- Stage 1: AP accrual confirmation → Warehouse receiving dock scan
- Stage 2: Dock scan → WMS stock-on-hand quantity update

**[A-04] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns; headers
match REGISTER DECLARATION Part A exactly). [SC-3, SC-4, SC-9 apply. Per Part A,
`Incumbent Equiv.` row: every cell form `[A-01]: [named step + duration]`.]

**[A-05] PHASE GATE 1** — Tick ✓ or ✗ before Finance:
- [ ] [A-01] was produced first before any stage trace or boundary block (SC-11)
- [ ] [A-01] includes ≥3 named steps with durations
- [ ] [A-02] SLA declared as integer with unit, derived from [A-01]; SC-5 verbatim present
- [ ] Every stage in [A-03] has four required columns per SC-7
- [ ] Every block in [A-04] has seven columns; headers match REGISTER DECLARATION Part A
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9 / Part A)

Finance may not begin until all items ✓. [SC-6.]

---

### ROLE 2 — Finance

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 3: Supplier EDI confirmation → PO entry in ERP
- Stage 4: PO entry → AP accrual line creation
- Stage 5: AP accrual → GL posting

**[A-07] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA (7 columns; headers
match Part A exactly). [SC-3: extend from [A-04] final.] [SC-4, SC-9 / Part A apply.]

**[A-08] PHASE GATE 2** — Tick ✓ or ✗ before Commerce:
- [ ] Citing line names [A-01], [A-02], [A-04] — [A-01] present (SC-1)
- [ ] Every stage in [A-06] has four required columns per SC-7
- [ ] Every block in [A-07] has seven columns; headers match REGISTER DECLARATION Part A
- [ ] `Elapsed (cumul.)` extends [A-04] final value; not reset (SC-3 / Part A)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9 / Part A)

Commerce may not begin until all items ✓. [SC-6.]

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]

**[A-09] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 6: WMS stock-on-hand quantity → Commerce platform inventory cache
- Stage 7: Commerce platform cache → Storefront catalog availability flag

**[A-10] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns; headers
match Part A exactly). [SC-3: extend from [A-07].] [SC-4, SC-9 / Part A apply.]

**[A-11] STALE ANALYSIS** — Table: Entity | Normal elapsed | Failure-mode elapsed |
[A-02] threshold | Verdict. Cite [A-02] by token.

**[A-12] RECOVERY PRESCRIPTIONS** — Named recovery per loss point and no-handling flag.
Formula: `Fall back to [A-01] if [specific condition]`.

**[A-13] INCUMBENT TOTAL** — [Per REGISTER DECLARATION Part B. Per SC-10.] Produce
immediately before [A-14]. Table per Part B INCUMBENT TOTAL row. Cite as `[A-13]` in
[A-14].

**[A-14] TRADE-OFF ANALYSIS** — [Per REGISTER DECLARATION Part B. Per SC-8.] Required.
Cite `[A-01]`, `[A-02]`, `[A-13]`. ≥1 pattern. ≥2 dimensions with [A-13] Grand Total.

---

---

## V-05

**Axis**: Combined — C-36 + C-37 + C-38 (all three new criteria)

**Hypothesis**: Commerce-first ordering forces [A-01] INCUMBENT BASELINE to be owned by
the customer-facing domain (Commerce), which has the most direct visibility into manual
process costs (catalog updates, stock availability checks). This satisfies C-36
(baseline-first production) and creates a Commerce → Operations → Finance sequence where
Finance runs last two positions after Commerce, enabling C-38 (Finance must cite [A-04],
Commerce's boundary checks, as a skip-level token). Parts A/B in the REGISTER DECLARATION
satisfy C-37. SC-11 (baseline-first), SC-12 (skip-level citation), and the Part A/B
single-authority declaration all work from a single artifact registry where [A-01] is
Commerce-owned, produced first, and cited by all subsequent roles.

---

You are tracing data through a retail purchase-order-to-inventory pipeline. Three expert
roles run in the sequence **Commerce → Operations → Finance**. Commerce runs first and
produces the incumbent manual-process baseline as the first artifact — establishing the
cost-of-inertia story from the customer-facing domain before any pipeline stage is traced.
Operations and Finance cite Commerce's baseline and threshold by token; they may not
redeclare or re-derive either.

Finance runs last and must cite Commerce's boundary artifacts directly — two roles prior
— as a required skip-level citation. A Finance role that cites only Operations' artifacts
without reaching back to Commerce fails the citation protocol.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. [A-01] is produced first; all subsequent
artifacts are produced in token order. A boundary block appearing before [A-01] is fully
written is a sequencing violation (SC-11).

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | INCUMBENT BASELINE | Commerce | Manual catalog-update and stock-availability process replaced by this pipeline; ≥3 named steps with durations; produced FIRST, before [A-02] and before any stage trace. SC-11 applies. |
| [A-02] | DOMAIN CONTEXT | Commerce | Entity vocabulary, staleness SLA (immutable after Stage 1), downstream consumer, business cadence; SLA derived from [A-01] total manual duration |
| [A-03] | STAGE TRACE — Commerce | Commerce | WMS snapshot → Commerce platform inventory cache → catalog availability flag; stage tables |
| [A-04] | BOUNDARY CHECKS — Commerce | Commerce | Boundary tables per BOUNDARY BLOCK SCHEMA; Incumbent Equiv. cells cite [A-01] |
| [A-05] | PHASE GATE 1 | Commerce | Checklist; all ✓ before Operations |
| [A-06] | STAGE TRACE — Operations | Operations | AP accrual confirmation → dock scan → WMS stock-on-hand update; stage tables |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | Boundary tables; extends elapsed from [A-04]; Incumbent Equiv. cells cite [A-01] |
| [A-08] | PHASE GATE 2 | Operations | Checklist; all ✓ before Finance; includes SC-12 skip-level pre-announcement |
| [A-09] | STAGE TRACE — Finance | Finance | Supplier EDI confirmation → PO entry → AP accrual → GL posting; stage tables |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | Boundary tables; extends elapsed from [A-07]; Incumbent Equiv. cells cite [A-01] |
| [A-11] | STALE ANALYSIS | Finance | Normal-operation and failure-mode elapsed vs [A-02] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery per loss point; formula `Fall back to [A-01] if [condition]` |
| [A-13] | INCUMBENT TOTAL | Finance | Sum of all Incumbent Equiv. values from [A-04], [A-07], [A-10]; breakdown by role; produced immediately before [A-14] |
| [A-14] | TRADE-OFF ANALYSIS | Finance | Required section; cites [A-01], [A-02], and [A-13] by token; ≥1 alternative; ≥2 dimensions |

---

### REGISTER DECLARATION

This output uses the **tabular register** throughout.

**This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell form)
and C-35 (INCUMBENT TOTAL section format). An evaluator may determine pass/fail for both
criteria by reading this section alone, without consulting the BOUNDARY BLOCK SCHEMA or
role instructions. Structural constraints SC-9 and SC-10 are callbacks to Parts A and B
respectively; they do not independently restate compliance requirements.**

**Part A — Field compliance markers (boundary block columns):**

| Required Field | Column Header | Required Cell Form | Disqualifying Form |
|----------------|---------------|--------------------|--------------------|
| Domain entity | `Entity` | Named entity from [A-02] vocabulary | "data" or "records" alone |
| Elapsed (cumulative) | `Elapsed (cumul.)` | Numeric sum of all prior stage and boundary latencies, in minutes | Partial sum; deferred total |
| Freshness verdict | `Verdict` | Exactly `FRESH` or exactly `STALE`, derived from [A-02] threshold | Any other value |
| Error handling | `Error Handling` | Named retry/dead-letter/rollback, or exactly `no handling — see [A-12]` | Silence; omitted column |
| Schema change | `Schema Delta` | Named field-level changes, or exactly `NONE` | Omitted column |
| Data loss | `Data Loss Flag` | `YES — [loss point name]` or `NO` | Generic language |
| Incumbent equivalent | `Incumbent Equiv.` | `[A-01]: [named manual step + duration]` — `[A-01]` token required; omission is a protocol violation | Bare duration; token omitted; column absent |
| Stage latency | `Stage Latency` (stage table) | Explicit value, range, or characterization | Inferred from boundary elapsed |

**Part B — Section format compliance markers:**

| Required Section | Section Header | Required Content Form | Disqualifying Form |
|------------------|---------------|----------------------|--------------------|
| INCUMBENT TOTAL | `### [A-13] INCUMBENT TOTAL` | Markdown table: `Role \| Incumbent Equiv. subtotal \| Steps cited`; rows for Commerce, Operations, Finance, Grand Total; all subtotals numeric | Prose-only; missing role row; no Grand Total |
| TRADE-OFF ANALYSIS | `### [A-14] TRADE-OFF ANALYSIS` | All three tokens `[A-01]`, `[A-02]`, `[A-13]` present; ≥1 alternative pattern; ≥2 dimensions | Any token absent; no pattern named |

---

### BOUNDARY BLOCK SCHEMA

Standalone section before any role output. Column header strings must match REGISTER
DECLARATION Part A spellings exactly. Role instructions reference this section by name
only.

**Every boundary block must be a markdown table with these columns, in this order:**
`Entity | Elapsed (cumul.) | Verdict | Error Handling | Schema Delta | Data Loss Flag | Incumbent Equiv.`

A column absent, renamed, or not matching Part A header strings fails the schema.

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Commerce opens with
`Citing: [A-xx], [A-yy], ...`. Citing [A-01] (INCUMBENT BASELINE) is required in every
non-first role's Citing line. Prose back-references do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the preceding
boundary table is fully populated per BOUNDARY BLOCK SCHEMA.
[Apply SC-2 before every stage advance.]

**SC-3 — Incremental elapsed**: `Elapsed (cumul.)` computed inside each boundary block;
not deferred. [Per REGISTER DECLARATION Part A, `Elapsed (cumul.)` row.]

**SC-4 — Binary verdict**: `Verdict` = `FRESH` or `STALE` vs [A-02] threshold. Cite
[A-02] by token. [Per REGISTER DECLARATION Part A, `Verdict` row.]

**SC-5 — Immutability**: Commerce appends to [A-02] verbatim: "This threshold is fixed.
No subsequent role may revise it after Stage 1 is written." Declare as integer with unit,
derived from [A-01] total manual duration plus acceptable pipeline latency headroom.

**SC-6 — Phase gate**: [A-05] and [A-08] are required checklists. Next role may not
begin until all items ✓.

**SC-7 — Stage table format**: Columns `Stage Latency | Schema In | Schema Out | Data
Loss Flag`. Stage Latency explicit. [Per REGISTER DECLARATION Part A, `Stage Latency`
row.] [Apply SC-7 at every stage block.]

**SC-8 — Trade-off as required section**: [Per REGISTER DECLARATION Part B, TRADE-OFF
ANALYSIS row.] All three tokens required. ≥1 pattern. ≥2 dimensions.
[Apply SC-8 when producing [A-14].]

**SC-9 — Incumbent Equiv. cell form**: [Per REGISTER DECLARATION Part A, `Incumbent
Equiv.` row.] Form: `[A-01]: [named step + duration]`. Token omission is a protocol
violation. [Apply SC-9 at every boundary block.]

**SC-10 — INCUMBENT TOTAL before trade-off**: [Per REGISTER DECLARATION Part B, INCUMBENT
TOTAL row.] Produce [A-13] immediately before [A-14]; cite [A-13] in [A-14] as numeric
endpoint. [Apply SC-10 before writing [A-14].]

**SC-11 — Baseline-first production**: [A-01] INCUMBENT BASELINE must be the first
artifact written in this output. No boundary block and no stage trace may appear before
[A-01] is fully produced. Commerce may not write Stage 1 until [A-01] is complete. The
ARTIFACT REGISTRY assigns token [A-01] to INCUMBENT BASELINE to enforce this sequencing:
the lowest-numbered token is produced first, guaranteeing that every `Incumbent Equiv.`
cell citing [A-01] references a fully-written artifact. A boundary block appearing before
[A-01] is complete is a sequencing violation.

**SC-12 — Skip-level citation in Finance**: Finance's `Citing:` line must include `[A-04]`
— Commerce's boundary checks, produced two roles prior. Operations is Finance's immediate
predecessor; a `Citing:` line that names only Operations' tokens without `[A-04]` fails
SC-12. The Phase Gate 2 checklist ([A-08]) explicitly verifies that `[A-04]` appears in
Finance's `Citing:` line as a named item before Finance may begin. Omitting `[A-04]` from
Finance's Citing line is detectable as a missing token in the phase gate checklist, not
a prose ambiguity.

---

### ROLE 1 — Commerce

[Commerce runs first. No Citing line required. The incumbent baseline leads per SC-11.]

**[A-01] INCUMBENT BASELINE** — Write FIRST, before any domain context or stage trace.
Per SC-11: no boundary block and no stage trace may appear before [A-01] is complete.
Describe the manual catalog-update and stock-availability process this pipeline replaces
from the customer-facing domain perspective. Include ≥3 named manual steps with durations
(e.g., "Manual warehouse phone call to confirm stock count: 30 min", "Spreadsheet catalog
availability update: 45 min", "Email to Finance team for invoice trigger: 20 min"). Use
entity names that will reappear in [A-02]. This is the source for every `Incumbent Equiv.`
cell in [A-04], [A-07], and [A-10]. [Per REGISTER DECLARATION Part A, `Incumbent Equiv.`
row.] All subsequent roles must cite [A-01] in their opening Citing line.

**[A-02] DOMAIN CONTEXT** — Write immediately after [A-01]. Include:
- Entity vocabulary (reuse ≥2 entity names from [A-01]): WMS stock-on-hand quantity,
  Commerce platform inventory cache, catalog availability flag, purchase order,
  AP accrual line, GL accrual entry
- Downstream consumer and business cadence
- Staleness SLA: declare as an integer with unit, derived from [A-01] total manual
  duration plus acceptable pipeline headroom.
- Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it
  after Stage 1 is written."

**[A-03] STAGE TRACE — Commerce** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 1: WMS stock-on-hand quantity → Commerce platform inventory cache
- Stage 2: Commerce platform inventory cache → Storefront catalog availability flag

**[A-04] BOUNDARY CHECKS — Commerce** — Per BOUNDARY BLOCK SCHEMA (7 columns; headers
match REGISTER DECLARATION Part A exactly). One block between Stage 1–Stage 2; one block
after Stage 2. [SC-3, SC-4, SC-9 / Part A apply. Every `Incumbent Equiv.` cell cites
[A-01] — a fully-written artifact since line 1 of this output.]

**[A-05] PHASE GATE 1** — Produce and tick before Operations begins. Mark each ✓ or ✗:
- [ ] [A-01] was produced first, before any stage trace or boundary block (SC-11)
- [ ] [A-01] includes ≥3 named steps with durations
- [ ] [A-02] SLA declared as integer with unit, derived from [A-01]; SC-5 verbatim present
- [ ] [A-02] reuses ≥2 entity names from [A-01]
- [ ] Every stage in [A-03] has four required columns per SC-7
- [ ] Every block in [A-04] has seven columns; headers match REGISTER DECLARATION Part A
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9 / Part A)

Operations may not begin until all items ✓. [Apply SC-6.]

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Operations** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 3: AP accrual confirmation → Warehouse receiving dock scan
- Stage 4: Dock scan → WMS stock-on-hand quantity update

**[A-07] BOUNDARY CHECKS — Operations** — Per BOUNDARY BLOCK SCHEMA (7 columns; headers
match REGISTER DECLARATION Part A exactly).
[SC-3: extend Elapsed (cumul.) from [A-04] final value; do not reset to zero.]
[SC-4: Verdict vs [A-02] threshold; do not redeclare threshold value.]
[SC-9 / Part A: every Incumbent Equiv. cell: `[A-01]: [named step + duration]`.]

**[A-08] PHASE GATE 2** — Produce and tick before Finance begins. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] — [A-01] present (SC-1)
- [ ] Every stage in [A-06] has four required columns per SC-7
- [ ] Every block in [A-07] has seven columns; headers match REGISTER DECLARATION Part A
- [ ] `Elapsed (cumul.)` in [A-07] extends [A-04] final value; not reset (SC-3 / Part A)
- [ ] Every `Verdict` derives from [A-02] threshold; threshold value not redeclared (SC-4)
- [ ] Every `Incumbent Equiv.` cell: `[A-01]: [named step + duration]` (SC-9 / Part A)
- [ ] SC-12 pre-announcement: Finance's `Citing:` line must include `[A-04]` (Commerce
  boundary checks, two roles prior); a Citing line with only Operations' tokens fails
  SC-12 — this requirement is verified as item SC-12 below

Finance may not begin until all items above are ✓. [Apply SC-6.]

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]
([A-04] is required per SC-12 — Commerce's boundary checks, produced two roles prior.
Operations is Finance's immediate predecessor; citing only [A-07] without [A-04] fails
SC-12. The elapsed chain in [A-10] must extend from [A-07], which itself extended from
[A-04]. Citing [A-04] confirms the full elapsed chain is traceable.)

**[A-09] STAGE TRACE — Finance** — Per SC-7. Per SC-2. Use entity names from [A-02].
- Stage 5: Supplier EDI confirmation → PO entry in ERP
- Stage 6: PO entry → AP accrual line creation
- Stage 7: AP accrual line → GL accrual entry posting

**[A-10] BOUNDARY CHECKS — Finance** — Per BOUNDARY BLOCK SCHEMA (7 columns; headers
match REGISTER DECLARATION Part A exactly).
[SC-3: extend Elapsed (cumul.) from [A-07] final value.]
[SC-4: Verdict vs [A-02] threshold.]
[SC-9 / Part A: every Incumbent Equiv. cell: `[A-01]: [named step + duration]`.]

**[A-11] STALE ANALYSIS** — Using final Elapsed (cumul.) from [A-10]:

| Entity ([A-02]) | Normal elapsed | Failure-mode elapsed | [A-02] threshold | Verdict |
|-----------------|----------------|----------------------|------------------|---------|

Produce separate rows for normal-operation and failure-mode staleness. Cite [A-02] by
token; do not restate the numeric threshold value.

**[A-12] RECOVERY PRESCRIPTIONS** — For every `no handling — see [A-12]` annotation in
[A-04]/[A-07]/[A-10] and every `Data Loss Flag: YES` in [A-03]/[A-06]/[A-09], provide a
specific named recovery action. Required formula:
`Fall back to [A-01] if [specific named failure condition]`
Cite [A-01] using this formula at least once.

**[A-13] INCUMBENT TOTAL** — [Per REGISTER DECLARATION Part B, INCUMBENT TOTAL row. Per
SC-10.] Produce immediately before [A-14]:

| Role | Incumbent Equiv. subtotal | Steps cited |
|------|--------------------------|-------------|
| Commerce | [sum of [A-04] Incumbent Equiv. values] | [step names from [A-01]] |
| Operations | [sum of [A-07] Incumbent Equiv. values] | [step names from [A-01]] |
| Finance | [sum of [A-10] Incumbent Equiv. values] | [step names from [A-01]] |
| **Grand Total** | | |

Cite this section as `[A-13]` in [A-14].

**[A-14] TRADE-OFF ANALYSIS** — [Per REGISTER DECLARATION Part B, TRADE-OFF ANALYSIS row.
Per SC-8.] Required named section. Cite `[A-01]` (manual baseline), `[A-02]` (SLA
dimension), and `[A-13]` (numeric incumbent total) — all three tokens required. Name ≥1
alternative data propagation pattern. Provide ≥2 trade-off dimensions using [A-13] Grand
Total as the numeric comparison endpoint.

---

## Criterion targeting summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-26 (non-natural ordering) | PASS | FAIL | PASS | PASS | PASS |
| C-36 (baseline-first) | FAIL | FAIL | PASS | PASS | PASS |
| C-37 (Parts A/B sole authority) | FAIL | PASS | FAIL | PASS | PASS |
| C-38 (skip-level citation) | PASS | FAIL | FAIL | FAIL | PASS |
| C-16 (cross-role reference chain) | PASS | PASS | PASS | PASS | PASS |
| C-34 (Incumbent Equiv. cell form) | PASS | PASS | PASS | PASS | PASS |
| C-35 (INCUMBENT TOTAL artifact) | PASS | PASS | PASS | PASS | PASS |
