# flow-dataflow — Round 7 Variations

---

## V-01

**Axis**: Role sequence — Finance → Operations → Commerce (Finance-first)

**Hypothesis**: Natural order is Operations → Finance → Commerce. Running Finance first forces Operations to cite Finance's pre-declared PO SLA as the immutable staleness contract (non-adjacent citation), and forces Commerce to cite Finance artifacts produced two roles prior. Non-adjacency is maximally stressed because Commerce must explicitly cite [A-04] (Finance boundary checks) even though [A-07] (Operations) immediately precedes it.

---

You are tracing data through a retail purchase-order-to-inventory pipeline. Three expert roles run in the sequence **Finance → Operations → Commerce**. This order is intentional: Finance establishes the PO SLA and manual-process baseline before Operations or Commerce begin. Operations and Commerce must cite Finance's pre-declared threshold — they may not redeclare or re-derive it.

---

### ARTIFACT REGISTRY

Produce all artifacts in the order listed. Every citation anywhere in this output must use the `[A-xx]` token exactly as spelled in this table. A citation to a target not listed here is a protocol violation.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Finance | Entity vocabulary, staleness SLA (immutable after Stage 1), downstream consumer, business cadence |
| [A-02] | INCUMBENT BASELINE | Finance | Manual PO and AP process this pipeline replaces; uses ≥1 entity from [A-01] |
| [A-03] | STAGE TRACE — Finance | Finance | PO creation → AP accrual → GL posting stages with schema in/out, latency, loss point |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | Interleaved blocks between Finance stages: elapsed total, freshness verdict, domain entity, error handling |
| [A-05] | PHASE GATE 1 | Finance | Self-verification checklist produced at end of Finance role; all items must be ✓ before Operations begins |
| [A-06] | STAGE TRACE — Operations | Operations | Receiving dock scan → WMS stock-on-hand update stages |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | Interleaved blocks extending the elapsed running total from [A-04] |
| [A-08] | PHASE GATE 2 | Operations | Self-verification checklist produced at end of Operations role; all items must be ✓ before Commerce begins |
| [A-09] | STAGE TRACE — Commerce | Commerce | WMS snapshot → Commerce platform cache → catalog availability flag stages |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | Interleaved blocks extending elapsed from [A-07] |
| [A-11] | STALE ANALYSIS | Commerce | Elapsed-vs-threshold rows: normal operation and failure-mode, cites [A-01] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point and "no handling" flag; required formula: `Fall back to [A-02] if [condition]` |
| [A-13] | TRADE-OFF ANALYSIS | Commerce | Alternative pattern, ≥2 trade-off dimensions, [A-02] as comparison baseline |

---

### STRUCTURAL CONSTRAINTS

Declare all constraints here. Role instructions reference them by identifier at every point of application.

**SC-1 — Citation opener**: Every role opens with a line:
`Citing: [A-xx], [A-yy], ...`
listing every [A-xx] token from prior roles this role builds on. Finance is first and has no prior tokens. A role that begins without a Citing line fails SC-1. Prose back-references ("as established above") do not satisfy SC-1.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the BOUNDARY CHECK between Stage N and Stage N+1 is fully complete with all four required fields: `Domain entity at boundary`, `Error handling`, `Elapsed total (cumulative)`, `Freshness verdict`. Write the BOUNDARY CHECK block. Confirm it is complete. Then write Stage N+1.

**SC-3 — Incremental elapsed computation**: Each BOUNDARY CHECK block must contain `Elapsed total (cumulative):` computed as the sum of all prior stage latencies and all prior boundary latencies up to and including this boundary. Compute this field inside the boundary block — it may not be deferred to [A-11].

**SC-4 — Binary freshness verdict**: Each BOUNDARY CHECK block must contain `Freshness verdict: FRESH | STALE` derived by comparing the cumulative elapsed total against the staleness threshold in [A-01]. Cite [A-01] by token. Do not restate its value. A boundary block without a Freshness verdict fails SC-4.

**SC-5 — Immutability of staleness threshold**: Finance role must append to [A-01] verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written." Operations and Commerce may not redeclare or adjust the threshold.

**SC-6 — Phase gate obligation**: Phase gates [A-05] and [A-08] are required outputs produced by the completing role before the next role begins. Each gate is a checklist with named criterion identifiers. The next role may not begin until all items are ✓.

---

### ROLE 1 — Finance

[Finance runs first. No Citing line required.]

**[A-01] DOMAIN CONTEXT** — Write this before Stage 1. Include:
- Entity vocabulary: purchase order (PO), AP accrual line, supplier receipt voucher, WMS stock-on-hand quantity, catalog availability flag
- Downstream consumer and business cadence (e.g., nightly GL close at 23:00)
- Staleness SLA: the maximum elapsed time from supplier EDI confirmation to catalog availability flag update that keeps inventory current. Declare as an integer with unit. Per SC-5, append verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written."

**[A-02] INCUMBENT BASELINE** — Describe the manual PO and AP process this pipeline replaces. Use at least one entity name from [A-01]. This artifact will be cited by [A-12] and [A-13].

**[A-03] STAGE TRACE — Finance** — Trace the following stages. Per SC-2, write [A-04] BOUNDARY CHECK before advancing to each next stage.

- Stage 1: Supplier EDI confirmation → PO entry in ERP
- Stage 2: PO entry → AP accrual line creation
- Stage 3: AP accrual line → GL posting

For each stage:
```
Schema in:  [fields entering this stage]
Schema out: [fields exiting — note any field additions, removals, name or type changes]
Latency:    [value, range, or characterization: real-time / near-real / batch / daily]
Loss point: [one concrete named failure scenario — "errors may occur" does not qualify]
```

**[A-04] BOUNDARY CHECKS — Finance** — Per SC-2: one block between Stage 1 and Stage 2, one between Stage 2 and Stage 3, one after Stage 3. Do not write Stage N+1 until the preceding block is complete. Each block:
```
Domain entity at boundary: [named entity from [A-01] vocabulary — not "data" or "records"]
Error handling:             [named mechanism — or "no handling — see [A-12]"]
Elapsed total (cumulative): [per SC-3 — sum of all prior stage and boundary latencies, in minutes]
Freshness verdict:          FRESH | STALE [per SC-4 — compare against [A-01] threshold]
```

**[A-05] PHASE GATE 1** — Produce and tick this checklist. Mark each ✓ or ✗:
- [ ] [A-01] contains staleness SLA with verbatim immutability statement (SC-5)
- [ ] [A-02] uses ≥1 entity name from [A-01]
- [ ] Every stage in [A-03] has Schema in, Schema out, Latency, Loss point
- [ ] Every block in [A-04] has all four required fields (SC-2)
- [ ] Every block has `Elapsed total (cumulative)` as a computed numeric sum (SC-3)
- [ ] Every block has `Freshness verdict: FRESH | STALE` (SC-4)

Operations may not begin until all items are ✓.

---

### ROLE 2 — Operations

Citing: [A-01], [A-02], [A-04]
(Open with this line. [A-04] is a non-adjacent predecessor in natural domain order — you are citing Finance's boundary check elapsed totals to extend them, not recompute from scratch. Do not redeclare the entity vocabulary from [A-01] or the staleness threshold.)

**[A-06] STAGE TRACE — Operations** — Per SC-2, write [A-07] BOUNDARY CHECK before advancing to each next stage.

- Stage 4: AP accrual confirmation → Warehouse receiving dock scan
- Stage 5: Dock scan → WMS stock-on-hand update

For each stage: Schema in, Schema out, Latency, Loss point. Use entity names from [A-01].

**[A-07] BOUNDARY CHECKS — Operations** — Per SC-2: one block between Stage 4 and Stage 5, one after Stage 5. Each block:
```
Domain entity at boundary: [named entity from [A-01] vocabulary]
Error handling:             [named mechanism — or "no handling — see [A-12]"]
Elapsed total (cumulative): [per SC-3 — extend the running total from the last entry in [A-04]]
Freshness verdict:          FRESH | STALE [per SC-4 — compare against [A-01] threshold; do not redeclare value]
```

**[A-08] PHASE GATE 2** — Produce and tick this checklist. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] has Schema in, Schema out, Latency, Loss point
- [ ] Every block in [A-07] has all four required fields (SC-2)
- [ ] `Elapsed total (cumulative)` in [A-07] extends [A-04] running total, not a fresh computation (SC-3)
- [ ] Every Freshness verdict derives from [A-01] threshold without redeclaring it (SC-4, SC-5)
- [ ] All entity names in [A-06] and [A-07] are from [A-01] vocabulary

Commerce may not begin until all items are ✓.

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]
(Open with this line. [A-04] is two roles prior — Finance boundary checks. You must cite it explicitly to extend its elapsed totals through [A-07] into your own boundary blocks. Citing only [A-07] without [A-04] fails SC-1.)

**[A-09] STAGE TRACE — Commerce** — Per SC-2, write [A-10] BOUNDARY CHECK before advancing.

- Stage 6: WMS stock-on-hand quantity → Commerce platform inventory cache
- Stage 7: Commerce platform cache → Storefront catalog availability flag

For each stage: Schema in, Schema out, Latency, Loss point. Use entity names from [A-01].

**[A-10] BOUNDARY CHECKS — Commerce** — Per SC-2: one block between Stage 6 and Stage 7, one after Stage 7. Each block:
```
Domain entity at boundary: [named entity from [A-01] vocabulary]
Error handling:             [named mechanism — or "no handling — see [A-12]"]
Elapsed total (cumulative): [per SC-3 — extend the running total from the last entry in [A-07]]
Freshness verdict:          FRESH | STALE [per SC-4 — compare against [A-01] threshold]
```

**[A-11] STALE ANALYSIS** — Using cumulative elapsed totals from [A-04], [A-07], [A-10]:

| Entity (from [A-01]) | Normal elapsed | Failure-mode elapsed | Threshold (from [A-01]) | Verdict |
|----------------------|---------------|---------------------|-------------------------|---------|

Produce separate rows for normal-operation and failure-mode staleness.

**[A-12] RECOVERY PRESCRIPTIONS** — For every `"no handling — see [A-12]"` annotation in [A-04], [A-07], [A-10] and every Loss point in [A-03], [A-06], [A-09], provide a specific named recovery action. Required formula structure: every recovery action that falls back to the manual process must include:

`Fall back to [A-02] if [specific named failure condition]`

Cite [A-02] using this formula at least once. A loose prose mention of [A-02] without the formula does not satisfy this requirement.

**[A-13] TRADE-OFF ANALYSIS** — Name one alternative data propagation pattern (e.g., event-driven CDC, real-time dual-write). Provide ≥2 trade-off dimensions, at least one quantified. Cite [A-02] as the comparison baseline for at least one dimension.

---

---

## V-02

**Axis**: Output format — table-based stage and boundary blocks (Operations → Commerce → Finance)

**Hypothesis**: Rendering stage and boundary blocks as markdown tables — rather than labeled field lists — makes the required fields (Schema in/out, Latency, Loss point, Domain entity, Error handling, Elapsed total, Freshness verdict) column-verifiable. Natural order is Operations → Finance → Commerce; putting Commerce before Finance is non-natural and forces Finance to cite Commerce's accumulated elapsed total rather than establishing its own.

---

You are tracing data through an e-commerce returns pipeline: return authorization (Operations), platform inventory restock and availability update (Commerce), and finance credit memo and GL reversal (Finance). Three expert roles run in the sequence **Operations → Commerce → Finance**. Natural order would be Operations → Finance → Commerce; Commerce runs before Finance here, forcing Finance to cite Commerce's artifacts as non-adjacent predecessor outputs.

**Output format for all stage and boundary blocks: markdown tables, as specified per role. Do not use labeled field lists.**

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Operations | Entity vocabulary, returns SLA (immutable), downstream consumer, business cadence |
| [A-02] | INCUMBENT BASELINE | Operations | Manual returns process (email + spreadsheet) this pipeline replaces |
| [A-03] | STAGE TRACE — Operations | Operations | Return auth → OMS reversal stages (table format) |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | Interleaved table blocks; establishes elapsed baseline |
| [A-05] | PHASE GATE 1 | Operations | Post-Operations checklist; all items ✓ before Commerce begins |
| [A-06] | STAGE TRACE — Commerce | Commerce | Inventory restock → availability flag stages (table format) |
| [A-07] | BOUNDARY CHECKS — Commerce | Commerce | Interleaved table blocks; extends elapsed from [A-04] |
| [A-08] | PHASE GATE 2 | Commerce | Post-Commerce checklist; all items ✓ before Finance begins |
| [A-09] | STAGE TRACE — Finance | Finance | Credit memo → GL reversal stages (table format) |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | Interleaved table blocks; extends elapsed from [A-07] |
| [A-11] | STALE ANALYSIS | Finance | Normal + failure-mode elapsed vs [A-01] threshold (table) |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Recovery per loss point and "no handling" flag; formula: `Fall back to [A-02] if [condition]` |
| [A-13] | TRADE-OFF ANALYSIS | Finance | Alternative pattern, ≥2 dimensions, [A-02] as baseline |

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role opens with `Citing: [A-xx], [A-yy], ...`. Operations has no prior tokens. Finance must cite [A-01] (Operations, non-adjacent) and [A-07] (Commerce, immediate predecessor) — both are required.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the BOUNDARY CHECK table between Stage N and Stage N+1 contains all four required columns: `Domain entity`, `Error handling`, `Elapsed total (cumulative)`, `Freshness verdict`. Write the table. Confirm all columns are populated. Then write Stage N+1.

**SC-3 — Incremental elapsed computation**: The `Elapsed total (cumulative)` column in each BOUNDARY CHECK table must be computed as the sum of all prior stage and boundary latencies up to this point. Compute here; do not defer to [A-11].

**SC-4 — Binary freshness verdict**: The `Freshness verdict` column in each BOUNDARY CHECK table must read `FRESH` or `STALE`, derived by comparing the cumulative elapsed total against the [A-01] threshold. Cite [A-01] by token. A table row without a Freshness verdict fails SC-4.

**SC-5 — Immutability**: Operations role must append to [A-01] verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written."

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required checklist outputs at phase boundaries. The next role may not begin until all items are ✓.

**SC-7 — Table format enforcement**: Stage blocks use a table with columns: `Field | Value | Notes`. Boundary check blocks use a table with columns: `Field | Value`. No labeled field lists. A stage or boundary block rendered as a field list fails SC-7.

---

### ROLE 1 — Operations

[Operations runs first. No Citing line required.]

**[A-01] DOMAIN CONTEXT** — Write before Stage 1. Include:
- Entity vocabulary: return authorization (RA), OMS order reversal, WMS restock entry, commerce platform inventory count, customer credit memo
- Downstream consumer and business cadence
- Returns SLA: maximum elapsed time from RA creation to customer credit memo posting. Append verbatim per SC-5: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written."

**[A-02] INCUMBENT BASELINE** — Manual email + spreadsheet returns process. Use ≥1 entity from [A-01].

**[A-03] STAGE TRACE — Operations** — Per SC-7, each stage block is a table. Per SC-2, write [A-04] BOUNDARY CHECK table before advancing.

Stage 1: Return authorization request → OMS return order creation
Stage 2: OMS return order → carrier return label dispatch

Format per stage:
| Field | Value | Notes |
|-------|-------|-------|
| Schema in | | |
| Schema out | | (note field additions, removals, type changes) |
| Latency | | |
| Loss point | | (concrete named failure — not "errors may occur") |

**[A-04] BOUNDARY CHECKS — Operations** — Per SC-7: boundary check is a table. Per SC-2: one block between Stage 1 and Stage 2, one after Stage 2. Do not write Stage N+1 until the preceding block is complete.

| Field | Value |
|-------|-------|
| Domain entity at boundary | [named entity from [A-01] — not "data" or "records"] |
| Error handling | [named mechanism — or "no handling — see [A-12]"] |
| Elapsed total (cumulative) | [per SC-3, in minutes] |
| Freshness verdict | FRESH or STALE [per SC-4, vs [A-01] threshold] |

**[A-05] PHASE GATE 1** — Produce and tick. Mark each ✓ or ✗:
- [ ] [A-01] contains SLA with verbatim immutability statement (SC-5)
- [ ] [A-02] uses ≥1 entity from [A-01]
- [ ] Every stage in [A-03] is a table with all four rows populated (SC-7)
- [ ] Every block in [A-04] is a table with all four rows populated (SC-2, SC-7)
- [ ] Every block has `Elapsed total (cumulative)` as a numeric sum (SC-3)
- [ ] Every block has `Freshness verdict: FRESH or STALE` (SC-4)

Commerce may not begin until all items are ✓.

---

### ROLE 2 — Commerce

Citing: [A-01], [A-02], [A-04]

**[A-06] STAGE TRACE — Commerce** — Per SC-7 (table format). Per SC-2, write [A-07] BOUNDARY CHECK before advancing.

Stage 3: Carrier receipt scan → WMS restock entry
Stage 4: WMS restock entry → Commerce platform inventory count update

Per stage (table format as [A-03]).

**[A-07] BOUNDARY CHECKS — Commerce** — Per SC-7, per SC-2: one block between Stage 3 and Stage 4, one after Stage 4.

| Field | Value |
|-------|-------|
| Domain entity at boundary | [named entity from [A-01]] |
| Error handling | [mechanism — or "no handling — see [A-12]"] |
| Elapsed total (cumulative) | [per SC-3 — extend [A-04] running total] |
| Freshness verdict | FRESH or STALE [per SC-4 vs [A-01] threshold] |

**[A-08] PHASE GATE 2** — Produce and tick. Mark each ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] is a table with all four rows (SC-7)
- [ ] Every block in [A-07] is a table with all four rows (SC-2, SC-7)
- [ ] `Elapsed total (cumulative)` extends [A-04] totals (SC-3)
- [ ] All Freshness verdicts derive from [A-01] threshold (SC-4, SC-5)

Finance may not begin until all items are ✓.

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]
(Finance is last. [A-04] is non-adjacent — Operations produced it two roles prior. Cite it explicitly; do not re-derive elapsed history from [A-07] alone.)

**[A-09] STAGE TRACE — Finance** — Per SC-7, per SC-2.

Stage 5: Commerce platform inventory count confirmation → Customer credit memo creation
Stage 6: Credit memo → GL reversal entry posting

Per stage (table format as [A-03]).

**[A-10] BOUNDARY CHECKS — Finance** — Per SC-7, per SC-2: one block between Stage 5 and Stage 6, one after Stage 6.

| Field | Value |
|-------|-------|
| Domain entity at boundary | [named entity from [A-01]] |
| Error handling | [mechanism — or "no handling — see [A-12]"] |
| Elapsed total (cumulative) | [per SC-3 — extend [A-07] running total] |
| Freshness verdict | FRESH or STALE [per SC-4 vs [A-01] threshold] |

**[A-11] STALE ANALYSIS** — Using totals from [A-04], [A-07], [A-10]:

| Entity | Normal elapsed | Failure-mode elapsed | Threshold ([A-01]) | Verdict |
|--------|---------------|---------------------|---------------------|---------|

Normal-operation and failure-mode as separate rows.

**[A-12] RECOVERY PRESCRIPTIONS** — For every "no handling" annotation and every Loss point across [A-03], [A-06], [A-09], provide a specific named recovery action. Required formula for manual fallbacks:

`Fall back to [A-02] if [specific named failure condition]`

[A-02] must appear using this formula at least once.

**[A-13] TRADE-OFF ANALYSIS** — One alternative pattern, ≥2 trade-off dimensions, ≥1 quantified, [A-02] as baseline.

---

---

## V-03

**Axis**: Phrasing register — conversational/guiding (Commerce → Finance → Operations)

**Hypothesis**: A conversational, guiding phrasing register ("Here is what you need to produce first...") can enforce all 27 structural criteria as reliably as formal/imperative phrasing, provided constraint identifiers (SC-x) are maintained and inline callbacks are preserved. Natural order is Operations → Finance → Commerce; Commerce runs first, forcing Finance and Operations to cite Commerce's SLA and baseline as non-adjacent predecessors.

---

Here is what you will do: trace data through a vendor marketplace payment clearing pipeline from the perspective of three domain experts, working in the sequence **Commerce → Finance → Operations**. Commerce sets up the vocabulary and the incumbent-process baseline first — then Finance extends the trace, then Operations closes it out. The ordering matters: Finance and Operations will need to reach back and cite Commerce's foundational artifacts rather than re-establish them.

The structural rules are listed in the PROTOCOL RULES section. I'll point you back to them by name each time they apply.

---

### ARTIFACT REGISTRY

Everything you produce gets a token here. Use these tokens every time you cite a prior output — exact match, no paraphrasing.

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Commerce | Vendor marketplace entity vocabulary; payment SLA (immutable); downstream consumers; cadence |
| [A-02] | INCUMBENT BASELINE | Commerce | Manual vendor payment process (email remittance + bank wire) this pipeline replaces |
| [A-03] | STAGE TRACE — Commerce | Commerce | Vendor invoice submission → payment authorization stages |
| [A-04] | BOUNDARY CHECKS — Commerce | Commerce | Interleaved blocks; establishes elapsed baseline |
| [A-05] | PHASE GATE 1 | Commerce | Commerce self-check; all items ✓ before Finance begins |
| [A-06] | STAGE TRACE — Finance | Finance | Payment authorization → AP ledger → bank settlement stages |
| [A-07] | BOUNDARY CHECKS — Finance | Finance | Interleaved blocks; extends elapsed from [A-04] |
| [A-08] | PHASE GATE 2 | Finance | Finance self-check; all items ✓ before Operations begins |
| [A-09] | STAGE TRACE — Operations | Operations | Settlement confirmation → vendor portal update → fulfillment release stages |
| [A-10] | BOUNDARY CHECKS — Operations | Operations | Interleaved blocks; extends elapsed from [A-07] |
| [A-11] | STALE ANALYSIS | Operations | Elapsed-vs-threshold table; normal + failure-mode |
| [A-12] | RECOVERY PRESCRIPTIONS | Operations | Specific recovery per loss point; formula `Fall back to [A-02] if [condition]` required |
| [A-13] | TRADE-OFF ANALYSIS | Operations | Alternative pattern; ≥2 dimensions; [A-02] as baseline |

---

### PROTOCOL RULES

Keep these in mind throughout. I'll reference them by name in each role's instructions.

**PR-1 — Open with citations**: When Finance or Operations begins, the very first line is `Citing: [A-xx], [A-yy], ...` listing every prior token this role builds on. Commerce opens first, so it doesn't need this line. Any role that launches into content without a Citing line has skipped PR-1 — go back and add it before continuing.

**PR-2 — Boundary-before-stage**: You may not write Stage N+1 until you have fully written the BOUNDARY CHECK between Stage N and N+1 — meaning all four fields are present: `Domain entity`, `Error handling`, `Elapsed total (cumulative)`, `Freshness verdict`. Think of the boundary block as a gate you have to pass through before moving on.

**PR-3 — Running elapsed total**: Each boundary block needs an `Elapsed total (cumulative)` — a running sum of every stage latency and every boundary overhead you have written up to that point. Compute it fresh in the boundary block itself; do not skip ahead and fill it in later.

**PR-4 — Freshness verdict**: Each boundary block must also include `Freshness verdict: FRESH | STALE`. You get this by comparing the cumulative elapsed total against the payment SLA you declared in [A-01]. Do not restate the SLA value — reference [A-01]. A boundary block without this verdict is incomplete.

**PR-5 — SLA is locked**: Once Commerce declares the payment SLA in [A-01] and writes Stage 1, that value is frozen. Finance and Operations may not change it. Commerce should append this sentence to [A-01] before Stage 1: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written."

**PR-6 — Phase gate output**: At the end of each of the first two roles, produce and tick a self-check checklist. The next role does not begin until every item is ✓.

---

### ROLE 1 — Commerce

Commerce goes first. No citation line needed here.

Here is what you produce, in order:

**[A-01] DOMAIN CONTEXT** — Lock the vocabulary before anything else. Include: entity names (vendor invoice, payment authorization record, AP ledger entry, bank settlement confirmation, vendor portal release flag), downstream consumer, and the business cadence (e.g., daily payment run at 14:00). Then declare the payment SLA: how long from vendor invoice submission to vendor portal release flag update is acceptable before data goes stale? Give a specific number with units. Per PR-5, append before Stage 1: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written."

**[A-02] INCUMBENT BASELINE** — Describe the manual email-remittance and bank-wire process this pipeline replaces. Name at least one entity from [A-01]. Finance and Operations will need to refer back to this.

**[A-03] STAGE TRACE — Commerce** — Walk through these stages. Per PR-2, write a BOUNDARY CHECK block before moving to the next stage:

- Stage 1: Vendor invoice submission → payment gateway authorization request
- Stage 2: Payment gateway response → payment authorization record creation

For each stage, include:
- `Schema in:` — fields entering the stage
- `Schema out:` — fields leaving the stage (note any field name changes, type changes, or new fields added)
- `Latency:` — how long this stage takes, with a value, range, or characterization
- `Loss point:` — one specific thing that can go wrong here and cause data loss (not a generic "errors may occur")

**[A-04] BOUNDARY CHECKS — Commerce** — Per PR-2: one block between Stage 1 and Stage 2, one after Stage 2. For each:
```
Domain entity at boundary: [an entity from [A-01] — not "data" or "records"]
Error handling:             [the specific mechanism, or "no handling — see [A-12]"]
Elapsed total (cumulative): [per PR-3 — sum everything up to here, in minutes]
Freshness verdict:          FRESH | STALE [per PR-4 — compare against [A-01]]
```

**[A-05] PHASE GATE 1** — Before Finance begins, run this self-check. Tick each item ✓ or mark ✗:
- [ ] [A-01] has a specific SLA value and the PR-5 immutability sentence
- [ ] [A-02] names at least one entity from [A-01]
- [ ] Every stage in [A-03] has Schema in, Schema out, Latency, Loss point
- [ ] Every block in [A-04] has all four required fields (PR-2)
- [ ] Every block has a numeric cumulative elapsed sum (PR-3)
- [ ] Every block has `Freshness verdict: FRESH | STALE` (PR-4)

Finance does not begin until all items are ✓.

---

### ROLE 2 — Finance

Open with: Citing: [A-01], [A-02], [A-04]
(PR-1 applies here. [A-04] is Commerce's boundary check output — you are extending its elapsed running total, not starting fresh.)

Now here is what Finance produces:

**[A-06] STAGE TRACE — Finance** — Per PR-2, write a boundary block before advancing.

- Stage 3: Payment authorization record → AP ledger debit entry
- Stage 4: AP ledger entry → bank settlement instruction
- Stage 5: Bank settlement instruction → settlement confirmation receipt

Use entity names from [A-01]. Schema in, Schema out, Latency, Loss point for each stage.

**[A-07] BOUNDARY CHECKS — Finance** — Per PR-2: one block between each consecutive stage pair (Stage 3–4, Stage 4–5) and one after Stage 5. Each block uses the same format as [A-04]:
```
Domain entity at boundary: [from [A-01] vocabulary]
Error handling:             [mechanism, or "no handling — see [A-12]"]
Elapsed total (cumulative): [per PR-3 — extend the running total from the last [A-04] entry]
Freshness verdict:          FRESH | STALE [per PR-4 — compare against [A-01]; do not restate threshold]
```

**[A-08] PHASE GATE 2** — Self-check before Operations. Tick ✓ or ✗:
- [ ] Citing line opens with [A-01], [A-02], [A-04] (PR-1)
- [ ] Every stage in [A-06] has all four required fields
- [ ] Every block in [A-07] has all four required fields (PR-2)
- [ ] `Elapsed total (cumulative)` in [A-07] is an extension of [A-04] totals, not a restart (PR-3)
- [ ] All Freshness verdicts cite [A-01] without restating its value (PR-4, PR-5)

Operations does not begin until all items are ✓.

---

### ROLE 3 — Operations

Open with: Citing: [A-01], [A-02], [A-04], [A-07]
(PR-1 applies. [A-04] is two roles back — Commerce's elapsed totals. You need to cite it to show the elapsed chain is unbroken across all three roles. Just citing [A-07] is not enough.)

Here is what Operations produces:

**[A-09] STAGE TRACE — Operations** — Per PR-2.

- Stage 6: Settlement confirmation receipt → Vendor portal payment status update
- Stage 7: Vendor portal update → Fulfillment release flag set

Use entity names from [A-01]. Schema in, Schema out, Latency, Loss point per stage.

**[A-10] BOUNDARY CHECKS — Operations** — Per PR-2: one block between Stage 6 and Stage 7, one after Stage 7.
```
Domain entity at boundary: [from [A-01]]
Error handling:             [mechanism, or "no handling — see [A-12]"]
Elapsed total (cumulative): [per PR-3 — extend [A-07] running total]
Freshness verdict:          FRESH | STALE [per PR-4 vs [A-01] threshold]
```

**[A-11] STALE ANALYSIS** — Using totals from [A-04], [A-07], [A-10]:

| Entity | Normal elapsed | Failure-mode elapsed | [A-01] threshold | Verdict |
|--------|---------------|---------------------|------------------|---------|

Two rows minimum: normal operation and failure mode.

**[A-12] RECOVERY PRESCRIPTIONS** — For every "no handling" annotation and every Loss point across all stages, give a specific named recovery action. Every recovery that falls back to the manual process must use this formula:

`Fall back to [A-02] if [specific named failure condition]`

Use this formula at least once. A general mention of [A-02] without this structure does not count.

**[A-13] TRADE-OFF ANALYSIS** — One alternative pattern, ≥2 trade-off dimensions (at least one quantified), [A-02] as baseline for at least one dimension.

---

---

## V-04

**Axes**: Role sequence (Operations → Commerce → Finance) + Inertia framing (manual TRACKER spreadsheet prominently featured)

**Hypothesis**: Foregrounding the incumbent manual process — giving it its own section before any role begins and naming its concrete failure modes — makes the C-27 recovery formula and C-15 baseline linkage more structurally demanding. Every role is required to reference the manual process explicitly, not just the recovery role. Natural order is Operations → Finance → Commerce; Commerce before Finance is non-natural, forcing Finance to cite Commerce's artifacts as a non-adjacent predecessor.

---

You are tracing data through a store replenishment sync pipeline: distribution center (DC) pick/pack (Operations), store inventory and POS availability update (Commerce), and finance posting of inventory cost (Finance). Roles run in the sequence **Operations → Commerce → Finance**.

**IMPORTANT — Inertia context**: Before the roles begin, the current state of the world is a manually maintained Excel spreadsheet called REPLEN_TRACKER.xlsx, updated by the store operations team twice daily (06:00 and 18:00) to reflect DC shipments. The pipeline described in this trace replaces REPLEN_TRACKER. Every role must acknowledge REPLEN_TRACKER at least once — the manual process is the baseline everything is measured against.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Operations | Entity vocabulary; replenishment SLA (immutable); downstream consumer; business cadence |
| [A-02] | INCUMBENT BASELINE | Operations | REPLEN_TRACKER.xlsx manual process — entity names, update cadence, known failure modes |
| [A-03] | STAGE TRACE — Operations | Operations | DC pick list generation → carton dispatch stages |
| [A-04] | BOUNDARY CHECKS — Operations | Operations | Interleaved blocks; establishes elapsed baseline |
| [A-05] | PHASE GATE 1 | Operations | Post-Operations checklist; all ✓ before Commerce begins |
| [A-06] | STAGE TRACE — Commerce | Commerce | Carton receipt scan → store inventory count → POS availability update stages |
| [A-07] | BOUNDARY CHECKS — Commerce | Commerce | Interleaved blocks; extends elapsed from [A-04] |
| [A-08] | PHASE GATE 2 | Commerce | Post-Commerce checklist; all ✓ before Finance begins |
| [A-09] | STAGE TRACE — Finance | Finance | Store inventory confirmation → cost of goods → GL inventory posting stages |
| [A-10] | BOUNDARY CHECKS — Finance | Finance | Interleaved blocks; extends elapsed from [A-07] |
| [A-11] | STALE ANALYSIS | Finance | Normal + failure-mode elapsed vs [A-01] threshold |
| [A-12] | RECOVERY PRESCRIPTIONS | Finance | Named recovery per loss point; formula `Fall back to [A-02] if [condition]` required; cite [A-02] |
| [A-13] | TRADE-OFF ANALYSIS | Finance | Alternative pattern, ≥2 dimensions, [A-02] as comparison |

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Operations (first) opens with `Citing: [A-xx], [A-yy], ...`. Finance must cite [A-01] (Operations, non-adjacent) and [A-07] (Commerce, immediate predecessor).

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the BOUNDARY CHECK between Stage N and Stage N+1 has all four required fields: `Domain entity at boundary`, `Error handling`, `Elapsed total (cumulative)`, `Freshness verdict`. Write the block. Confirm it is complete. Then write Stage N+1.

**SC-3 — Incremental elapsed computation**: `Elapsed total (cumulative)` in each BOUNDARY CHECK is computed as the sum of all prior stage and boundary latencies. Compute inside the boundary block. May not be deferred to [A-11].

**SC-4 — Binary freshness verdict**: Each BOUNDARY CHECK contains `Freshness verdict: FRESH | STALE` derived from the [A-01] threshold. Do not restate the threshold value; cite [A-01].

**SC-5 — Immutability**: Operations must append to [A-01] verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written."

**SC-6 — Phase gate obligation**: [A-05] and [A-08] are required role outputs before the next role begins.

**SC-7 — REPLEN_TRACKER acknowledgment**: Every role — Operations, Commerce, Finance — must reference REPLEN_TRACKER or [A-02] by name at least once within its content (not just in the Citing line). The reference must be substantive: it must state what REPLEN_TRACKER did or failed to do in relation to the stage being traced or the analysis being produced.

---

### ROLE 1 — Operations

[Operations runs first. No Citing line.]

**[A-01] DOMAIN CONTEXT** — Write before Stage 1. Include:
- Entity vocabulary: DC pick list, carton dispatch record, store receiving entry, POS available-to-sell quantity, inventory cost posting
- Downstream consumer and business cadence (store replenishment window, e.g., nightly shelf restock at 21:00)
- Replenishment SLA: maximum elapsed time from DC pick list generation to POS available-to-sell quantity update. Declare as integer with units. Per SC-5, append: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written."
- Per SC-7, note where REPLEN_TRACKER provided this data before the pipeline existed

**[A-02] INCUMBENT BASELINE** — Describe REPLEN_TRACKER.xlsx in detail: how it is maintained (manual, twice-daily updates), which entities it tracks, and at least two known failure modes (e.g., update lag, merge conflicts, formula errors). Use entity names from [A-01].

**[A-03] STAGE TRACE — Operations** — Per SC-2.

- Stage 1: Warehouse management system pick list → Carton manifest generation
- Stage 2: Carton manifest → DC dispatch scan (carrier handoff)

For each stage: Schema in, Schema out, Latency, Loss point (concrete named failure).

**[A-04] BOUNDARY CHECKS — Operations** — Per SC-2: one block between Stage 1 and Stage 2, one after Stage 2.
```
Domain entity at boundary: [named entity from [A-01]]
Error handling:             [mechanism — or "no handling — see [A-12]"]
Elapsed total (cumulative): [per SC-3, in minutes]
Freshness verdict:          FRESH | STALE [per SC-4 vs [A-01] threshold]
```

**[A-05] PHASE GATE 1** — Tick ✓ or ✗:
- [ ] [A-01] has SLA with immutability statement (SC-5)
- [ ] [A-02] describes REPLEN_TRACKER with ≥2 failure modes and ≥1 entity from [A-01]
- [ ] Every stage in [A-03] has Schema in, Schema out, Latency, Loss point
- [ ] Every block in [A-04] has all four required fields (SC-2)
- [ ] Cumulative elapsed is a numeric sum in each block (SC-3)
- [ ] Freshness verdict is FRESH or STALE in each block (SC-4)
- [ ] REPLEN_TRACKER or [A-02] referenced substantively in role content (SC-7)

Commerce may not begin until all items are ✓.

---

### ROLE 2 — Commerce

Citing: [A-01], [A-02], [A-04]

Per SC-7, acknowledge where REPLEN_TRACKER previously handled the store-side visibility this role now provides.

**[A-06] STAGE TRACE — Commerce** — Per SC-2.

- Stage 3: Store receiving dock scan → Store inventory count update
- Stage 4: Inventory count update → POS available-to-sell quantity publish
- Stage 5: POS quantity → Storefront product availability flag

For each stage: Schema in, Schema out, Latency, Loss point.

**[A-07] BOUNDARY CHECKS — Commerce** — Per SC-2: one block between each consecutive stage pair and one after Stage 5. Each block:
```
Domain entity at boundary: [from [A-01]]
Error handling:             [mechanism — or "no handling — see [A-12]"]
Elapsed total (cumulative): [per SC-3 — extend [A-04] running total]
Freshness verdict:          FRESH | STALE [per SC-4 vs [A-01] threshold]
```

**[A-08] PHASE GATE 2** — Tick ✓ or ✗:
- [ ] Citing line names [A-01], [A-02], [A-04] (SC-1)
- [ ] Every stage in [A-06] has all four fields
- [ ] Every block in [A-07] has all four fields (SC-2)
- [ ] Elapsed totals extend [A-04] baseline (SC-3)
- [ ] Freshness verdicts derive from [A-01] without re-declaration (SC-4, SC-5)
- [ ] REPLEN_TRACKER or [A-02] referenced substantively (SC-7)

Finance may not begin until all items are ✓.

---

### ROLE 3 — Finance

Citing: [A-01], [A-02], [A-04], [A-07]
([A-04] is from Operations, two roles prior and non-adjacent to Finance in natural order. Cite it explicitly to extend the elapsed chain. Per SC-7, acknowledge what REPLEN_TRACKER did or failed to do regarding inventory cost visibility.)

**[A-09] STAGE TRACE — Finance** — Per SC-2.

- Stage 6: POS quantity confirmation → Cost of goods calculation
- Stage 7: Cost of goods → GL inventory posting

For each stage: Schema in, Schema out, Latency, Loss point.

**[A-10] BOUNDARY CHECKS — Finance** — Per SC-2: one block between Stage 6 and Stage 7, one after Stage 7.
```
Domain entity at boundary: [from [A-01]]
Error handling:             [mechanism — or "no handling — see [A-12]"]
Elapsed total (cumulative): [per SC-3 — extend [A-07] running total]
Freshness verdict:          FRESH | STALE [per SC-4 vs [A-01] threshold]
```

**[A-11] STALE ANALYSIS** — Using totals from [A-04], [A-07], [A-10]:

| Entity | Normal elapsed | Failure-mode elapsed | [A-01] threshold | Verdict |
|--------|---------------|---------------------|------------------|---------|

Normal-operation and failure-mode as separate rows.

**[A-12] RECOVERY PRESCRIPTIONS** — For every "no handling" annotation and every Loss point, provide a specific named recovery action. Required formula for manual fallbacks:

`Fall back to [A-02] if [specific named failure condition]`

The formula must appear for at least one recovery action. Cite [A-02] substantively — note what a return to REPLEN_TRACKER would require operationally.

**[A-13] TRADE-OFF ANALYSIS** — One alternative pattern, ≥2 trade-off dimensions (≥1 quantified), [A-02] as comparison baseline. At minimum, one dimension must compare pipeline performance against REPLEN_TRACKER's twice-daily update cadence from [A-02].

---

---

## V-05

**Axes**: Lifecycle emphasis (explicit multi-phase transitions with scoring columns) + Output format (boundary checks include `Risk score: 1–5` column)

**Hypothesis**: Adding a numeric risk score column to each BOUNDARY CHECK block extends the binary freshness verdict (C-21) into a risk-weighted gate and gives the scorer an ordinal signal for prioritizing recovery prescriptions. Extra-explicit lifecycle phase transitions with phase summary tables increase the audit surface for C-23/C-25. Natural order is Operations → Finance → Commerce; Finance before Commerce is natural, but Finance running before Operations (Finance-first) is non-natural, forcing Operations to cite Finance's SLA as the immutable constraint.

---

You are tracing data through a procurement-to-POS pricing pipeline across three roles in the sequence **Finance → Operations → Commerce**. Finance runs first to establish the vendor cost SLA and incumbent baseline. Operations and Commerce must cite Finance's pre-declared SLA — they may not re-derive or re-declare it.

**Output protocol**: Boundary check blocks include a five-field format with a `Risk score: 1–5` column, where 1 = low risk (FRESH, strong error handling) and 5 = critical risk (STALE, no handling). Phase gates include a risk-summary row.

---

### ARTIFACT REGISTRY

| Token | Artifact | Owner | Description |
|-------|----------|-------|-------------|
| [A-01] | DOMAIN CONTEXT | Finance | Entity vocabulary; vendor cost SLA (immutable); downstream consumer; cadence |
| [A-02] | INCUMBENT BASELINE | Finance | Manual pricing spreadsheet (PRICE_BOOK.xlsx) this pipeline replaces |
| [A-03] | STAGE TRACE — Finance | Finance | Vendor cost feed → price model → approved price master stages |
| [A-04] | BOUNDARY CHECKS — Finance | Finance | Five-field blocks (entity, error handling, elapsed, verdict, risk score) |
| [A-05] | PHASE GATE 1 | Finance | Finance self-check with risk summary; all ✓ before Operations begins |
| [A-06] | STAGE TRACE — Operations | Operations | Price master → distribution → store price label stages |
| [A-07] | BOUNDARY CHECKS — Operations | Operations | Five-field blocks extending elapsed from [A-04] |
| [A-08] | PHASE GATE 2 | Operations | Operations self-check with risk summary; all ✓ before Commerce begins |
| [A-09] | STAGE TRACE — Commerce | Commerce | Store price label → POS price sync → e-commerce listing price stages |
| [A-10] | BOUNDARY CHECKS — Commerce | Commerce | Five-field blocks extending elapsed from [A-07] |
| [A-11] | STALE ANALYSIS | Commerce | Elapsed-vs-threshold table; normal + failure-mode; includes risk scores |
| [A-12] | RECOVERY PRESCRIPTIONS | Commerce | Named recovery per loss point; highest-risk items first; formula `Fall back to [A-02] if [condition]` |
| [A-13] | TRADE-OFF ANALYSIS | Commerce | Alternative pattern, ≥2 dimensions, [A-02] baseline |

---

### STRUCTURAL CONSTRAINTS

**SC-1 — Citation opener**: Every role other than Finance opens with `Citing: [A-xx], ...`. Finance has no prior tokens. Operations must cite [A-01] and [A-04]. Commerce must cite [A-01], [A-04], and [A-07]. [A-04] is non-adjacent to Commerce (Finance produced it two roles prior); cite it explicitly — do not infer elapsed baseline from [A-07] alone.

**SC-2 — Stage-write progression gate**: Stage N+1 may not be written until the BOUNDARY CHECK between Stage N and Stage N+1 is complete with all five required fields present: `Domain entity`, `Error handling`, `Elapsed total (cumulative)`, `Freshness verdict`, `Risk score`. Write the block, confirm it is complete, then write Stage N+1.

**SC-3 — Incremental elapsed computation**: `Elapsed total (cumulative)` is computed inside each BOUNDARY CHECK as the sum of all prior stage and boundary latencies. Compute here — may not be deferred to [A-11].

**SC-4 — Binary freshness verdict**: Each BOUNDARY CHECK contains `Freshness verdict: FRESH | STALE` derived from the [A-01] threshold. Cite [A-01] by token.

**SC-5 — Risk score assignment**: Each BOUNDARY CHECK contains `Risk score: 1–5` assigned as follows:
- 5: Freshness verdict STALE and Error handling is "no handling"
- 4: Freshness verdict STALE and error handling mechanism present
- 3: Freshness verdict FRESH and error handling is "no handling"
- 2: Freshness verdict FRESH and partial handling (retry only, no dead-letter)
- 1: Freshness verdict FRESH and full handling (retry + dead-letter or equivalent)

**SC-6 — Immutability**: Finance must append to [A-01]: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written."

**SC-7 — Phase gate with risk summary**: Phase gates [A-05] and [A-08] include, after the checklist, a risk summary row: `Highest risk score in this role: [N] at [boundary name]`. The next role must acknowledge this risk in its Citing line commentary.

---

### ROLE 1 — Finance

[Finance runs first. No Citing line.]

**[A-01] DOMAIN CONTEXT** — Write before Stage 1. Include:
- Entity vocabulary: vendor cost record, approved price master, store price label, POS item price, e-commerce listing price
- Downstream consumer and cadence (e.g., weekly price change cycle closing Friday 17:00)
- Vendor cost SLA: maximum elapsed time from vendor cost feed receipt to POS item price activation. Integer with units. Per SC-6, append: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written."

**[A-02] INCUMBENT BASELINE** — Describe PRICE_BOOK.xlsx: maintained manually by the pricing team, updated weekly, distributed via email. Use ≥1 entity from [A-01]. Document at least two failure modes.

**[A-03] STAGE TRACE — Finance** — Per SC-2.

- Stage 1: Vendor EDI cost file → Price model input normalization
- Stage 2: Price model output → Approved price master creation
- Stage 3: Approved price master → Price change approval workflow

For each stage: Schema in, Schema out, Latency, Loss point.

**[A-04] BOUNDARY CHECKS — Finance** — Per SC-2: one block between Stage 1 and Stage 2, one between Stage 2 and Stage 3, one after Stage 3. Each block has five fields:
```
Domain entity at boundary: [named entity from [A-01]]
Error handling:             [mechanism — or "no handling — see [A-12]"]
Elapsed total (cumulative): [per SC-3, in hours]
Freshness verdict:          FRESH | STALE [per SC-4 vs [A-01] threshold]
Risk score:                 1–5 [per SC-5 scoring table]
```

**[A-05] PHASE GATE 1** — Produce, tick ✓ or ✗, and append risk summary:
- [ ] [A-01] has SLA with immutability statement (SC-6)
- [ ] [A-02] has ≥2 failure modes and ≥1 entity from [A-01]
- [ ] Every stage in [A-03] has Schema in, Schema out, Latency, Loss point
- [ ] Every block in [A-04] has all five fields (SC-2)
- [ ] Elapsed totals are numeric sums (SC-3)
- [ ] Freshness verdicts are FRESH or STALE (SC-4)
- [ ] Risk scores follow SC-5 table

Risk summary: `Highest risk score in this role: [N] at [boundary name]`

Operations may not begin until all items are ✓.

---

### ROLE 2 — Operations

Citing: [A-01], [A-04]
(Finance's highest risk score was [N] at [boundary]. Operations will extend the elapsed chain from [A-04].)

**[A-06] STAGE TRACE — Operations** — Per SC-2.

- Stage 4: Approved price master → Store distribution system price push
- Stage 5: Distribution system → Store shelf label print queue

For each stage: Schema in, Schema out, Latency, Loss point.

**[A-07] BOUNDARY CHECKS — Operations** — Per SC-2: one block between Stage 4 and Stage 5, one after Stage 5. Five-field format:
```
Domain entity at boundary: [from [A-01]]
Error handling:             [mechanism — or "no handling — see [A-12]"]
Elapsed total (cumulative): [per SC-3 — extend [A-04] running total]
Freshness verdict:          FRESH | STALE [per SC-4 vs [A-01] threshold]
Risk score:                 1–5 [per SC-5]
```

**[A-08] PHASE GATE 2** — Tick ✓ or ✗, append risk summary:
- [ ] Citing line names [A-01], [A-04] (SC-1)
- [ ] Every stage in [A-06] has all four fields
- [ ] Every block in [A-07] has all five fields (SC-2)
- [ ] Elapsed extends [A-04] totals (SC-3)
- [ ] Freshness verdicts from [A-01] threshold (SC-4, SC-6)
- [ ] Risk scores follow SC-5

Risk summary: `Highest risk score in this role: [N] at [boundary name]`

Commerce may not begin until all items are ✓.

---

### ROLE 3 — Commerce

Citing: [A-01], [A-02], [A-04], [A-07]
(Operations highest risk score was [N] at [boundary]. Finance's [A-04] is non-adjacent to Commerce — cite it to show the elapsed chain is unbroken from Stage 1.)

**[A-09] STAGE TRACE — Commerce** — Per SC-2.

- Stage 6: Store shelf label print → POS item price activation
- Stage 7: POS price activation → E-commerce listing price sync

For each stage: Schema in, Schema out, Latency, Loss point.

**[A-10] BOUNDARY CHECKS — Commerce** — Per SC-2: one block between Stage 6 and Stage 7, one after Stage 7. Five-field format:
```
Domain entity at boundary: [from [A-01]]
Error handling:             [mechanism — or "no handling — see [A-12]"]
Elapsed total (cumulative): [per SC-3 — extend [A-07] running total]
Freshness verdict:          FRESH | STALE [per SC-4 vs [A-01] threshold]
Risk score:                 1–5 [per SC-5]
```

**[A-11] STALE ANALYSIS** — Using totals from [A-04], [A-07], [A-10]:

| Entity | Normal elapsed | Failure-mode elapsed | [A-01] threshold | Verdict | Max risk score |
|--------|---------------|---------------------|------------------|---------|----------------|

Normal-operation and failure-mode as separate rows. Include the max risk score observed for each entity.

**[A-12] RECOVERY PRESCRIPTIONS** — For every "no handling" annotation and every Loss point, provide a specific named recovery. Order prescriptions by risk score (highest first). Required formula for manual fallbacks:

`Fall back to [A-02] if [specific named failure condition]`

Cite [A-02] with this formula at least once. Prescriptions for Risk score 4–5 must include a time-to-recover estimate.

**[A-13] TRADE-OFF ANALYSIS** — One alternative pattern, ≥2 dimensions (≥1 quantified), [A-02] as baseline. Compare at minimum against PRICE_BOOK.xlsx's weekly update cadence from [A-02].

---
