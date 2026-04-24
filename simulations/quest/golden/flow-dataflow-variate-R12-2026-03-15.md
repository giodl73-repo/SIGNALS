# flow-dataflow — Round 12 Variations (Rubric v10)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v10 (C-01 through C-24, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

Round 12 operates on a validated rubric. v10 = v9 — no new criteria. V-01 in R11 achieved
17/17 aspirational (97 composite), confirming C-24 (pre-declared complete output scaffold)
as the definitive differentiator. V-02 in R11 achieved 15/17 — gap was precisely C-24
(Scaffold Authority design lacked unified STEP 0 before domain roles began). C-24 is the
high-water mark anchor for all subsequent rounds.

**R12 goal**: stress-test the full rubric across three axes not yet explored as single-axis
controls — phrasing register (conversational vs imperative), lifecycle emphasis
(boundary-first vs stage-first), and inertia framing (incumbent-as-primary-narrative vs
incumbent-as-supporting-table). Secondary goal: determine whether any axis produces
scoring behavior the v10 rubric cannot capture, which would indicate a v11 candidate
criterion.

R11 V-03 explored formal protocol-contract phrasing (SHALL, MUST, SCAFFOLD VIOLATION).
R12 V-01 tests the opposite: fully conversational, question-driven register with no
imperative enforcement language. If C-24 compliance degrades under conversational phrasing,
that confirms the protocol-contract register is a load-bearing structural mechanism, not
cosmetic. If compliance holds, the scaffold constraint is axis-robust.

**R12 Hypothesis space:**

**H1 — Conversational/question-driven phrasing register (V-01)**
Replace all imperative protocol instructions with question-framed invitations ("Before you
begin, can you plan your output tables?", "What could go wrong at this boundary?"). The
scaffold requirement is present but framed as a "planning table" rather than a binding
contract. Tests whether scaffold compliance is robust to phrasing softness or requires
protocol-contract language to hold. Predicts: C-24 partial compliance — scaffold produced
but upstream-references column sparsely populated because "could you list..." does not
carry the enforcement weight of "MUST list T-NN tokens."

**H2 — Boundary-first lifecycle (V-02)**
The OUTPUT TABLE SCAFFOLD lists boundary blocks as first-class T-NN entries appearing
before stage trace tables in scaffold dependency order. After entity inventory, the prompt
produces the BOUNDARY INVENTORY TABLE (T-03) as a structural commitment — with NH-NN
placeholders, entity-at-risk at entity level, and latency column stubs. Stage trace tables
(T-04 onward) must then satisfy the row commitments made in T-03. The hypothesis: pre-
committing boundary rows before stage traces forces complete C-11 labeling (every boundary
pre-declared) and creates structural pressure to fill C-17/C-20 field citations during
stage tracing rather than as an afterthought. Predicts stronger C-11 compliance and higher
C-17 entity.field citation density than stage-first lifecycle.

**H3 — Incumbent-centric narrative framing (V-03)**
Every stage trace section opens with an "INCUMBENT EQUIVALENT" block citing the MS-NN step
that this stage replaces before describing what the pipeline does. Recovery prescriptions
are framed as "pipeline failure → revert to MS-NN" rather than "recovery mechanism." Stale
window analysis compares automated latency against incumbent step duration. The incumbent
baseline table is not just T-01 — it is the structural frame that every stage section
references. Tests whether incumbent-centric framing drives deeper C-14/C-15/C-16
compliance than treatment of the baseline as a standalone supporting table.

**H4 — Combined: conversational register + boundary-first lifecycle (V-04)**
Combines H1 (question-driven phrasing) with H2 (boundary-first lifecycle). Both axes
soften or restructure the dominant mechanics in R11 V-01. Tests whether the combined
softening produces a larger C-24 compliance gap than either axis alone, and whether
boundary-first lifecycle compensates for weakened scaffold enforcement by providing
alternative structural pressure (pre-declared boundary rows that stages must satisfy).

**H5 — Combined: scaffold-first + inertia-first + three-role sequence (V-05)**
Operations runs first and must produce T-01 (incumbent baseline) as its only output before
any pipeline content is written. Finance runs second, declares the SLA budget and entity
inventory. Commerce runs third, traces pipeline stages, boundary inventory, stale window
analysis, recovery audit, closure gate, and pattern assessment. A Scaffold Architect step
precedes all three roles and produces only the T-NN scaffold table — forbidden from domain
content. Tests whether anchoring T-01 = INCUMBENT BASELINE at the scaffold level
(pre-declared by a role whose sole job is the incumbent process) drives full C-14/C-15/C-16
traceability, since every downstream recovery entry that cites T-01 resolves against a
table whose rows were produced by the role most qualified to name them (Operations).

**Axes selected for R12:**

1. **Conversational phrasing register** — question-driven invitations replace imperatives;
   scaffold framed as planning table (single axis: V-01)
2. **Boundary-first lifecycle** — boundary inventory declared before stage trace tables as
   a structural commitment in T-03; stages must satisfy pre-committed boundary rows (single
   axis: V-02)
3. **Incumbent-centric narrative** — every stage section opens with INCUMBENT EQUIVALENT
   block; recovery framed as reversion; stale window compared against incumbent duration
   (single axis: V-03)
4. **Combined (H1 + H2)** — conversational register + boundary-first lifecycle (V-04)
5. **Combined (H5)** — scaffold-first + inertia-first + three-role sequence: Scaffold
   Architect → Operations → Finance → Commerce (V-05)

**New signal candidates for R12:**

1. **Phrasing-register scaffold decay** (V-01, V-04) — whether softening imperatives to
   questions causes upstream-references column to collapse to "none" for tables that
   structurally depend on prior tables. Success signal: V-01 recovery audit table declares
   T-NN tokens for Boundary Inventory and all Stage Trace entries. Failure signal: "none"
   appears in rows that structurally reference prior tables.

2. **Boundary pre-commitment quality** (V-02, V-04) — whether declaring T-03 (boundary
   inventory stub) before stage traces produces more complete B[N]->[N+1] labeling and
   more entity.field citations than stage-first lifecycle. Success signal: every boundary
   row in T-03 has a non-generic entity.field annotation after the stage trace sections
   populate it. Failure signal: entity-at-risk column remains at entity-level (no field
   citation) even after exit manifests are available.

3. **Incumbent-centric C-16 density** (V-03, V-05) — whether framing each stage as
   "what the incumbent did here" drives every recovery prescription to carry an MS-NN
   step citation (C-16 full compliance) rather than just "at least one" (C-14 pass
   condition). Success signal: every NH-NN and LP-NN recovery row in the audit table
   cites a specific MS-NN step. Failure signal: recovery rows that cite the process
   category ("manual QC process") without a step identifier.

4. **Role-separated incumbent quality** (V-05) — whether Operations producing T-01
   before Finance and Commerce begin results in richer, more domain-specific incumbent
   step descriptions than single-role designs. Success signal: MS-NN steps contain
   specific actor names (e.g., "DC receiving supervisor"), specific elapsed times (e.g.,
   "45 min per truck"), and named systems (e.g., "WMS receiving dock terminal"). Failure
   signal: MS-NN steps are generic workflow descriptions without actor or timing specifics.

---

## V-01 — Conversational/Question-Driven Phrasing Register

**Variation axis**: Phrasing register — every structural instruction is reframed as a
question or invitation. "MUST produce," "IS REQUIRED," and "SHALL NOT" are replaced with
"can you show me...," "what would you find here?," "walk me through...". The scaffold is
framed as a "planning table" rather than a binding contract, though the structural
requirements (T-NN tokens, upstream references, per-identifier closure) are preserved.

**Hypothesis**: Conversational phrasing reduces the enforcement signal of the scaffold
requirement. When "MUST list T-NN tokens" becomes "could you list which prior tables this
draws from?", the upstream-references column loses its penalty-cost framing. Predicts:
scaffold produced with correct table inventory, but upstream-references column populated
with prose descriptions or "none" rather than T-NN tokens, because the invitation register
does not communicate that an empty cell is a structural deficit. C-24 partial pass (table
inventory present, dependency graph incomplete). C-16 likely complete (MS-NN citation
requirement phrased as a reminder, not an enforcement gate). Tests whether R11 V-01's
17/17 result depends on protocol-contract phrasing or is robust to register softening.

Scenario: Finance — accounts payable invoice automation pipeline. Vendor invoices from a
supplier portal flow through OCR field extraction, PO three-way match, approval routing,
payment schedule generation, and GL AP posting to the accounts payable subledger. Stages:
Invoice Capture => OCR Field Extraction => PO Three-Way Match => Approval Routing =>
Payment Schedule Generation => GL AP Posting.

---

You are a Finance data domain expert. I'd like you to walk me through an accounts payable
invoice automation pipeline — from vendor invoice arrival at the supplier portal through
OCR extraction, PO matching, approval routing, payment scheduling, and GL posting to the
AP subledger.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Before You Begin — Planning Table

Before diving in, could you map out the tables you'll produce in this walkthrough? This
helps me navigate your analysis and understand how each piece connects to the others.

Please create a planning table as your very first output:

| Table # | Table Name | What it contains | Which prior tables does it draw from? |
|---------|------------|------------------|---------------------------------------|
| T-01 | [name] | [one sentence on purpose and which criteria it satisfies] | [list prior T-NN tokens this table references, or "none" if foundational] |
| T-02 | ... | ... | ... |
| ... | ... | ... | ... |

At minimum, I'd expect to see:
- The manual AP process this automation replaced (foundational — no prior tables)
- The entities you'll be tracing (foundational — no prior tables)
- One trace table per stage (draws from entity inventory)
- A boundary inventory covering all inter-stage handoffs (draws from stage trace tables)
- A recovery plan for every failure mode identified (draws from boundary inventory, stage
  tables, and the incumbent baseline)
- A final closure check confirming every failure mode has a recovery entry (draws from
  recovery plan)

For the "Which prior tables" column — if a table extends, references, or is derived from a
prior table, it would be helpful to list those by T-NN token. For example, the recovery
plan table depends on the boundary inventory and stage tables, so its entry might read
"T-03, T-04, T-05, T-06, T-07, T-08, T-09." "none" is appropriate only for tables that
don't reference any prior output.

I'll use the T-NN tokens from this planning table throughout our conversation to refer to
your outputs — so keeping that column complete will help everything connect cleanly.

---

### What did the manual AP process look like?

Before we trace the automated pipeline, I'd like to understand what the AP team was doing
manually before this system existed. Could you walk me through the incumbent process in a
table?

| Step ID | Manual Step | Who did it | How long it took |
|---------|-------------|------------|------------------|
| MS-01 | [step description] | [AP clerk / controller / etc.] | [time] |
| ... | ... | ... | ... |

I'm looking for at least five concrete, specific AP steps — things like "MS-01: AP clerk
downloads invoice PDFs from vendor email portal and manually keys header fields (vendor ID,
invoice number, amount, due date) into the ERP — 90 min per 40-invoice batch." Generic
descriptions like "review invoice data" are too vague to be useful.

After the table, could you tell me:
- What's the **INCUMBENT TOTAL** — the elapsed time if all these steps run sequentially?
  (We'll compare this against pipeline latency later.)
- What's the **AP close SLA** — the maximum elapsed time from invoice receipt to GL AP
  posting that keeps the monthly close on track? (Give me a number in hours. We'll use
  this to calculate how much SLA budget each pipeline boundary consumes.)

One more thing: in the recovery section later, it'll be helpful to link each failure
recovery to a specific MS-NN step. So keep this table handy — we'll be citing these step
IDs when we talk about what the team reverts to when the pipeline fails.

---

### What entities are in play?

What domain entities will you be tracing through this pipeline? Could you enumerate them
in a table before we start tracing?

| Entity Name | Domain area | Key fields | What role does it play? |
|-------------|-------------|------------|------------------------|

I'd expect to see at minimum: VendorInvoice, OCRExtract, POMatchResult, ApprovalDecision,
PaymentSchedule, GLAPEntry.

Please establish all in-scope entities here — any entity introduced mid-trace that wasn't
declared in this table would be a gap I'd want to flag.

Also, I'll need the **AP close SLA** declared here as well (the same value from the
planning section above) so we have an anchor for all downstream latency comparisons.

---

### Stage-by-stage walkthrough

Now let's trace the pipeline. For each stage, could you show me:

1. What fields are present at stage exit? (Using typed notation: `field_name: TYPE(precision)`)
2. Did the schema change at this stage? If yes, what specifically changed? If nothing
   changed, please confirm explicitly — something like "NONE — verified: no field added,
   removed, renamed, or retyped" is clearer than a bare "unchanged."
3. What could go wrong here that would cause data loss or corruption? Please be specific
   — assign an LP-NN identifier (e.g., "LP-01: VendorInvoice records with unresolvable
   vendor_id written to error queue — invoice not processed, payment delayed past due
   date"). "Errors may occur" is too vague.
4. How long does this stage take? A characterization is fine — real-time, micro-batch,
   hourly, daily.

Show me a stage table for each stage (please use the T-NN header from your planning
table):

| Field | Type at Exit | Schema Change? | Data Loss Risk | Stage Latency |
|-------|-------------|----------------|----------------|---------------|

After each stage table, a compact typed exit manifest would be helpful — it tells me
exactly what the downstream stage receives:

```
EXIT MANIFEST — Stage N: [entity name]
  fields: [count at exit]
  key field assertions:
    [field_name: TYPE(precision)]
    [field_name: TYPE(precision)]
    (at least two assertions)
```

When a stage has no error-handling mechanism, please flag it: `NH-NN: no handling —
risk accepted at [location]`. We'll address every NH-NN and LP-NN in the recovery section.

Stages to trace:
1. Invoice Capture — supplier portal → AP intake queue
2. OCR Field Extraction — AP intake queue → OCR extraction service
3. PO Three-Way Match — OCR extraction service → matching engine
4. Approval Routing — matching engine → approval workflow system
5. Payment Schedule Generation — approval workflow → payment engine
6. GL AP Posting — payment engine → AP subledger

---

### How do the inter-stage handoffs look?

Now that you've traced the stages, could you show me the boundaries between them? One row
per handoff (B1->2 through B5->6). I need every cell to have a value — could you leave
nothing blank here?

| Boundary | Error Handling | Schema Change? | Entity at Risk | Transport Latency (ms) | Processing Overhead (ms) | Total (ms) | SLA% This Boundary | Cumulative SLA% |
|----------|---------------|----------------|----------------|----------------------|--------------------------|------------|-------------------|-----------------|
| B1->2 | | | | | | | | |
| B2->3 | | | | | | | | |
| B3->4 | | | | | | | | |
| B4->5 | | | | | | | | |
| B5->6 | | | | | | | | |

A few things I'm specifically looking for:

- **Entity at Risk**: could you name both the entity AND the specific field from the
  upstream exit manifest? Format like `VendorInvoice.vendor_id — risk description`.
  Entity name alone isn't specific enough.
- **Transport and Processing Overhead**: I'd like these as separate numeric estimates in
  ms — even rough estimates are more useful than "negligible."
- **Total Latency**: should equal Transport + Processing Overhead.
- **SLA% columns**: fraction of the AP close SLA consumed at each boundary, and the
  running cumulative total.

After the table, which boundary dominates the SLA budget? Could you identify the first
boundary where the Cumulative SLA% crosses 50% of the AP close SLA, and explain in one
sentence why it dominates?

---

### How stale does the data get?

Could you walk me through the accumulated latency from Invoice Capture through GL AP
Posting, adding stage and boundary latencies as you go? Please show Transport and
Processing Overhead separately at each boundary step. Under normal operation — is the
final GL posting fresh or stale relative to the AP close SLA? What about under the worst
failure mode (name it, and tie it to an LP-NN or NH-NN you declared)?

---

### What's the recovery plan?

For every NH-NN and LP-NN you declared in the stage trace and boundary inventory, I'd
like to understand the recovery path. Could you organize these in a table?

| Trigger ID | What triggered it | Recovery mechanism | Which MS step? | Incumbent step (exact text from T-01) |
|------------|------------------|-------------------|----------------|---------------------------------------|

A few reminders:
- Each recovery entry should name a specific action at a specific boundary or stage —
  not just "manual review."
- Each entry should also cite the specific MS-NN step from the incumbent baseline that
  the team would revert to. The full step description from T-01, verbatim, helps confirm
  the link.

---

### Closure check

Before wrapping up, could you do a quick forward check? Go back through everything you've
declared — every NH-NN and LP-NN — and confirm whether each one has a recovery row.
Please don't derive this list from the recovery table — check back against where each
was originally declared.

| Identifier | Where declared | Recovery row present? | Status |
|------------|---------------|----------------------|--------|

A count summary ("all 6 are covered") isn't quite what I need here — a per-identifier
status helps me spot any gaps immediately.

---

### Pattern assessment

What integration pattern is this? Could you name one alternative pattern and give me at
least two trade-off dimensions — with at least one quantified or qualified in AP / finance
terms?

---

*Planning table contract: the planning table you produced at the start is the navigation
map for this walkthrough. Every cross-reference should use the T-NN token from that table.
If a table appears in the body that wasn't in the planning table, that's a gap I'd want
to flag. Please complete every cell — if a value is unknown, a rough estimate is better
than leaving it blank.*

---

## V-02 — Boundary-First Lifecycle

**Variation axis**: Lifecycle emphasis — the boundary inventory is declared as T-03
before any stage trace tables appear in the scaffold. After entity inventory, the prompt
produces a BOUNDARY INVENTORY TABLE stub (T-03) with all boundary rows pre-committed:
NH-NN placeholders for boundaries with no error handling, entity-at-risk annotations at
entity level, and latency column stubs requiring numeric values. Stage trace tables
(T-04 onward) must satisfy the row commitments made in T-03 — specifically, stage exit
manifests must supply the field citations required to complete the entity.field annotations
committed at each boundary row.

**Hypothesis**: Pre-committing boundary rows before stage traces forces complete C-11
boundary labeling (every inter-stage boundary must be named in the scaffold before content
begins) and creates structural pressure on C-17/C-20 field citation quality — the model
must return to fill T-03 row stubs with entity.field annotations derived from the exit
manifests it produces in T-04 through T-09. Predicts: stronger C-11 compliance (no
undeclared boundary labels mid-trace) and higher C-17/C-20 field citation density than
stage-first lifecycle. Risk: model may produce T-03 stubs with entity-only annotations
and fail to update them after exit manifests are available, exposing the stub-fill gap
as a scorable C-20 deficit.

Scenario: Operations — supplier ASN-to-DC-receiving pipeline. Supplier advance ship
notices flow through DC gate check, QC inspection, put-away validation, inventory system
update, and WMS-to-ERP sync. Stages: Supplier ASN Receipt => DC Gate Check => QC
Inspection => Put-Away Validation => Inventory System Update => WMS-to-ERP Sync.

---

You are an Operations data domain expert tracing data through a supplier ASN-to-DC-
receiving pipeline — advance ship notices from a supplier EDI gateway through DC gate
check, QC inspection, put-away, inventory update, and WMS-to-ERP synchronization.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### STEP 0 — OUTPUT TABLE SCAFFOLD

Declare every table that will appear in this response before producing any domain content.
**Boundaries are first-class scaffold entries**: declare the Boundary Inventory Table
(T-03) before any stage trace table. Stage trace tables (T-04 onward) must satisfy the
boundary row commitments pre-declared in T-03.

| Table # | Table Name | Purpose | Upstream Tables |
|---------|------------|---------|-----------------|
| T-01 | [table name] | [purpose + criteria satisfied] | [T-NN tokens or "none"] |
| T-02 | ... | ... | ... |
| ... | ... | ... | ... |

**Required scaffold entries in this order** (dependency order — no forward references):
- T-01: Incumbent Baseline Table (C-15) — upstream: none
- T-02: Entity Inventory Table (C-10) — upstream: none
- T-03: Boundary Inventory Table (C-11, C-17, C-21, C-22) — upstream: T-02 — NOTE: this
  table is declared before stage trace tables; entity-at-risk field citations will be
  updated after stage exit manifests are produced
- T-04 through T-09: Stage Trace Tables, one per stage (C-04, C-19) — upstream: T-02,
  T-03
- T-10: Recovery Audit Table (C-18, C-16) — upstream: T-01, T-03, T-04 through T-09
- T-11: Closure Gate Table (C-23) — upstream: T-10

**Citation rule**: every cross-table reference uses T-NN tokens from this scaffold.
A table appearing in the body without a scaffold entry is an undeclared artifact.

---

### SECTION 1 — INCUMBENT BASELINE TABLE [T-01]

Document the manual receiving and inventory process this pipeline replaces.

| Step ID | Manual Step | Actor/Team | Duration |
|---------|-------------|------------|----------|
| MS-01 | [step description] | [DC supervisor / QC inspector / etc.] | [time] |
| ... | ... | ... | ... |

**Minimum five distinct steps** specific to DC-to-ERP receiving operations (e.g.,
`MS-01: DC gate supervisor manually counts pallets against paper ASN and records
discrepancies on clip-board form — 30 min per truck`). Generic workflow steps
do not qualify.

After the table:
- **INCUMBENT TOTAL**: additive sum of all Duration values. Fixed at declaration.
- **DC Receiving SLA**: maximum elapsed time from supplier ASN receipt to ERP inventory
  update visible to procurement (numeric, in hours). Fixed at declaration — all
  downstream latency comparisons must cite this value by T-01 reference; do not
  re-declare.
- **Citation rule**: every recovery entry in T-10 must cite an MS-NN step ID from this
  table. An entry without an MS-NN citation fails C-16.

---

### SECTION 2 — ENTITY INVENTORY TABLE [T-02]

Enumerate all in-scope domain entities before the first stage trace.

| Entity Name | Domain | Key Fields | Role in Pipeline |
|-------------|--------|------------|-----------------|

Required entities: SupplierASN, DCReceiptEvent, QCInspectionRecord, PutAwayRecord,
InventoryLedgerEntry, ERPInventoryUpdate.

State the **receiving volume assumption**: ASN lines per day at peak receiving period.

---

### SECTION 3 — BOUNDARY INVENTORY TABLE [T-03] (Pre-Declared Stub)

**This table is produced before stage trace sections.** Entity-at-risk annotations are
declared at entity level here; field citations will be completed after stage exit manifests
are produced in Sections 4 through 9. A boundary row whose entity-at-risk annotation
remains at entity level only (no `entity.field_name` citation) after the stage trace
sections are complete fails C-20.

Produce one row per inter-stage boundary. All nine columns are required. Latency and SLA%
columns carry numeric stubs that will be confirmed or revised by stage exit manifest data.

| Boundary | Error Handling | Schema Change | Entity at Risk | Transport Latency (ms) | Processing Overhead (ms) | Total (ms) | SLA% This Boundary | Cumulative SLA% |
|----------|---------------|---------------|----------------|----------------------|--------------------------|------------|-------------------|-----------------|
| B1->2 | | | | | | | | |
| B2->3 | | | | | | | | |
| B3->4 | | | | | | | | |
| B4->5 | | | | | | | | |
| B5->6 | | | | | | | | |

**Column rules at pre-declaration stage**:
- **Error Handling**: named mechanism (retry, dead-letter, circuit-breaker) or
  `NH-NN: no handling — risk accepted`. Assign NH-NN identifiers sequentially here;
  cite these same identifiers in T-10. Silence fails C-02.
- **Entity at Risk**: declare the entity name drawn from T-02. After stage exit manifests
  are produced, update to `entity.field_name — risk description` format. Entity-only
  annotation at final scoring fails C-20.
- **Transport and Processing Overhead**: numeric ms estimates required; "negligible"
  does not qualify. Revise after stage latencies are confirmed.
- **Total**: must equal Transport + Processing Overhead.
- **SLA% and Cumulative SLA%**: derive from DC Receiving SLA declared in T-01.

**After the boundary table is complete** (post-stage-trace sections), append:
**DOMINATION POINT**: first boundary where Cumulative SLA% exceeds 50% of the DC
Receiving SLA, the exact cumulative percentage, and a one-sentence justification.

---

### SECTION 4 THROUGH 9 — STAGE TRACE TABLES [T-04 through T-09]

For each stage, produce a stage table using its scaffold-declared T-NN header:
`[T-NN] STAGE TRACE — Stage N: [Stage Name]`

**Required columns**:

| Field | Type | Schema Delta | Data Loss Risk | Stage Latency |
|-------|------|-------------|----------------|---------------|

- **Field + Type**: `field_name: TYPE(precision)` notation at stage exit. List all fields
  present at stage exit.
- **Schema Delta**: named changes or `NONE — verified: no field added, removed, renamed,
  or retyped`. A bare "NONE" without the verification clause fails C-12.
- **Data Loss Risk**: assign LP-NN identifier at first declaration. Concrete failure only
  — `LP-NN: [entity name] records with [specific condition] written to [destination] —
  [consequence in Operations terms]`. "Errors may occur" does not qualify.
- **Stage Latency**: value, range, or characterization. May not be omitted.

After each stage table, produce a **Typed Exit Manifest**:

```
EXIT MANIFEST — Stage N: [entity name]
  fields: [count at exit]
  key field assertions:
    [field_name: TYPE(precision)]
    [field_name: TYPE(precision)]
    (minimum two assertions)
```

The exit manifest is the authority for field citations in T-03 boundary rows. After
producing each manifest, update the corresponding boundary row in T-03 with the
`entity.field_name` citation.

**Stages**:
1. Supplier ASN Receipt — EDI gateway → DC intake queue
2. DC Gate Check — DC intake queue → gate verification service
3. QC Inspection — gate verification service → QC platform
4. Put-Away Validation — QC platform → WMS put-away engine
5. Inventory System Update — WMS → inventory ledger
6. WMS-to-ERP Sync — inventory ledger → ERP inventory module

---

### SECTION 10 — STALE WINDOW ANALYSIS

Accumulate stage and boundary latencies sequentially (show Transport and Processing
Overhead addends separately at each boundary step, citing T-03 boundary rows by B-label):

- After Stage 1: [elapsed]
- After B1->2: [Transport: X ms + Processing: Y ms = cumulative Z ms]
- After Stage 2: [elapsed]
- ... continue through Stage 6 ...

Compare final accumulated total against DC Receiving SLA (cite by T-01 reference):
1. **Normal operation**: FRESH or STALE with elapsed value
2. **Worst-case failure mode** (name the failure, cite LP-NN or NH-NN from T-03): FRESH
   or STALE

---

### SECTION 11 — RECOVERY AUDIT TABLE [T-10]

Begin this section with `[T-10] RECOVERY AUDIT TABLE`. Cite upstream tables by T-NN as
declared in the scaffold.

One row per NH-NN and per LP-NN declared in Sections 3 through 9. All five columns
required — a missing row is a structural gap.

| Trigger ID | Triggering Condition | Recovery Mechanism | MS Step ID | Incumbent Step (verbatim from T-01) |
|------------|---------------------|-------------------|------------|-------------------------------------|

Every recovery mechanism must name a specific action at a specific boundary or stage.
Every entry must cite an MS-NN step from T-01. Generic "manual intervention" without a
named incumbent step fails C-16.

---

### SECTION 12 — CLOSURE GATE TABLE [T-11]

Begin with `[T-11] CLOSURE GATE TABLE`. Structurally separate from T-10.

Enumerate every declared NH-NN and LP-NN independently — do not derive this list from
the T-10 rows. Check each against T-10.

| Identifier | Source (stage or boundary) | Recovery Row Present (YES/NO) | Status (CLOSED/OPEN) |
|------------|---------------------------|-------------------------------|----------------------|

An OPEN status indicates a structural deficit. A count summary does not qualify.

---

### SECTION 13 — PATTERN ASSESSMENT

Name the integration pattern (CDC stream, event-driven async, synchronous API chain,
etc.) and one alternative. State ≥2 trade-off dimensions with ≥1 quantified or qualified
in supply chain / Operations terms (e.g., "synchronous QC inspection gating adds ~120 ms
per ASN line but eliminates ~2.3% shrinkage discrepancy at annual peak receiving volume").

---

*Scaffold contract: T-03 (Boundary Inventory) is a pre-declared structural commitment.
Stage trace sections (T-04 through T-09) must satisfy T-03 boundary row requirements
by providing entity.field citations from their exit manifests. No table may appear for
the first time after the scaffold. Complete every cell — blank cells and "negligible"
latency values are structural gaps.*

---

## V-03 — Incumbent-Centric Narrative Framing

**Variation axis**: Inertia framing — the incumbent baseline is not a supporting section
but the primary narrative frame. Every stage trace section opens with an INCUMBENT
EQUIVALENT block citing the specific MS-NN step this stage replaces, describing what the
manual process did, and stating elapsed time from T-01. The pipeline trace follows as
"what the automation does instead." Recovery prescriptions are framed as "on pipeline
failure, revert to MS-NN." Stale window analysis compares automated cumulative latency
against INCUMBENT TOTAL. The domination point statement includes the incumbent equivalent
for context.

**Hypothesis**: Incumbent-centric framing makes every stage trace carry an implicit C-14
qualification — the manual fallback is named at the stage level before the recovery
section even begins. This structural repetition of incumbent context at each stage
(rather than in a standalone T-01 table) predicts full C-16 compliance: every recovery
prescription cites a specific MS-NN step because the incumbent step was declared in that
stage's INCUMBENT EQUIVALENT block immediately above. Tests whether narrative co-location
of automation and incumbent (at every stage) drives denser MS-NN citation behavior than
a single standalone T-01 table with no per-stage reinforcement.

Scenario: Commerce — ERP-to-storefront product catalog sync. Product master records from
an ERP system flow through item validation, pricing calculation, availability aggregation,
channel filtering, CDN distribution, and storefront cache update. Stages: ERP Product
Master Export => Item Validation => Pricing Calculation => Availability Aggregation =>
Channel Filtering => CDN Distribution.

---

You are a Commerce data domain expert tracing data through an ERP-to-storefront product
catalog synchronization pipeline — product master records from an ERP system through item
validation, pricing calculation, availability aggregation, channel filtering, CDN
distribution, and storefront cache update.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### STEP 0 — OUTPUT TABLE SCAFFOLD

Before any domain content, declare every table that will appear in this response. The
incumbent baseline table is T-01 and is the reference frame for every subsequent section
— all recovery prescriptions and stale window comparisons cite T-01 by T-NN token.

| Table # | Table Name | Purpose | Upstream Tables |
|---------|------------|---------|-----------------|
| T-01 | [table name] | [purpose + criteria satisfied] | [T-NN tokens or "none"] |
| T-02 | ... | ... | ... |
| ... | ... | ... | ... |

Required scaffold entries (dependency order):
- T-01: Incumbent Baseline Table (C-15) — upstream: none — **primary narrative anchor**
- T-02: Entity Inventory Table (C-10) — upstream: none
- T-03 through T-08: Stage Trace Tables, one per stage (C-04, C-19) — upstream: T-01,
  T-02 (each stage references its INCUMBENT EQUIVALENT from T-01)
- T-09: Boundary Inventory Table (C-11, C-17, C-21, C-22) — upstream: T-02, T-03–T-08
- T-10: Recovery Audit Table (C-18, C-16) — upstream: T-01, T-09, T-03–T-08
- T-11: Closure Gate Table (C-23) — upstream: T-10

**T-01 is the incumbent narrative anchor**: every stage table (T-03 through T-08) must
open with an INCUMBENT EQUIVALENT block citing the MS-NN step it replaces. Every recovery
entry in T-10 must cite an MS-NN step from T-01. The stale window analysis must compare
automated cumulative latency against T-01's INCUMBENT TOTAL.

---

### SECTION 1 — INCUMBENT BASELINE TABLE [T-01]

Document the manual product catalog management and pricing update process this pipeline
replaces. This is the **primary reference frame** for every stage trace and every recovery
prescription that follows.

| Step ID | Manual Step | Actor/Team | Duration |
|---------|-------------|------------|----------|
| MS-01 | [step description] | [catalog manager / pricing analyst / etc.] | [time] |
| ... | ... | ... | ... |

**Minimum five distinct steps** specific to ERP-to-storefront catalog operations (e.g.,
`MS-01: Catalog manager exports product master batch from ERP as CSV and manually maps
attribute fields to storefront schema using lookup spreadsheet — 3 hrs per weekly batch`).
Generic steps do not qualify.

After the table:
- **INCUMBENT TOTAL**: additive sum of all Duration values. Fixed at declaration. The
  stale window analysis will compare automated pipeline latency against this total.
- **Catalog publication SLA**: maximum elapsed time from ERP product master record change
  to storefront availability API reflecting the update (numeric, in hours or minutes).
  Fixed at declaration — cite this value by T-01 reference in all latency comparisons.
  Do not re-declare in downstream sections.
- **Narrative anchor rule**: each stage trace section (T-03 through T-08) must reference
  T-01 by token and cite at least one MS-NN step as the incumbent equivalent for that
  stage. A stage trace with no INCUMBENT EQUIVALENT block fails C-14 for that stage.

---

### SECTION 2 — ENTITY INVENTORY TABLE [T-02]

Enumerate all in-scope domain entities before the first stage trace. Upstream: none.

| Entity Name | Domain | Key Fields | Role in Pipeline |
|-------------|--------|------------|-----------------|

Required entities: ERPProductMaster, ValidationResult, PriceRecord, AvailabilityPayload,
ChannelFilteredRecord, CDNDistributionPackage, StorefrontCacheEntry.

**Catalog SLA restatement** (cite from T-01 — do not re-declare a different value):
- Catalog publication SLA: [cite T-01 reference]
- SKU volume assumption: items per weekly batch at peak catalog update

---

### SECTION 3 THROUGH 8 — STAGE TRACE TABLES [T-03 through T-08]

For each stage, produce a table using its scaffold-declared T-NN header:
`[T-NN] STAGE TRACE — Stage N: [Stage Name] (upstream: T-01, T-02)`

**Each stage table must open with an INCUMBENT EQUIVALENT block** before the stage trace
content:

```
INCUMBENT EQUIVALENT — Stage N: [Stage Name]
  Manual step replaced: [MS-NN] — [full step description verbatim from T-01]
  Incumbent elapsed time: [value from T-01 Duration column]
  What the pipeline replaces: [one sentence describing the automation]
```

A stage with no INCUMBENT EQUIVALENT block, or a block that cites a T-01 step by
process category without MS-NN identifier, fails C-14 for that stage.

After the INCUMBENT EQUIVALENT block, produce the stage trace table:

| Field | Type | Schema Delta | Data Loss Risk | Stage Latency |
|-------|------|-------------|----------------|---------------|

- **Field + Type**: `field_name: TYPE(precision)` at stage exit.
- **Schema Delta**: named changes or `NONE — verified: no field added, removed, renamed,
  or retyped`. Bare "NONE" without verification fails C-12.
- **Data Loss Risk**: assign LP-NN identifier. Example: `LP-01: ERPProductMaster records
  with null price_tier_id excluded from PriceRecord — item visible in storefront with
  stale pricing until next batch cycle`. "May fail" does not qualify.
- **Stage Latency**: value, range, or characterization. May not be omitted.

After the stage table, produce a **Typed Exit Manifest**:

```
EXIT MANIFEST — Stage N: [entity name]
  fields: [count at exit]
  key field assertions:
    [field_name: TYPE(precision)]
    [field_name: TYPE(precision)]
    (minimum two)
```

When no error-handling exists: `NH-NN: no handling — risk accepted at [location]`.

**Stages**:
1. ERP Product Master Export — ERP → catalog intake queue
2. Item Validation — catalog intake queue → validation service
3. Pricing Calculation — validation service → pricing engine
4. Availability Aggregation — pricing engine → availability service
5. Channel Filtering — availability service → channel distribution layer
6. CDN Distribution — channel layer → CDN edge cache

---

### SECTION 9 — BOUNDARY INVENTORY TABLE [T-09]

Begin with `[T-09] BOUNDARY INVENTORY TABLE`. One row per inter-stage boundary. All nine
columns required — blank cells are structural gaps.

| Boundary | Error Handling | Schema Change | Entity at Risk | Transport (ms) | Processing Overhead (ms) | Total (ms) | SLA% This Boundary | Cumulative SLA% |
|----------|---------------|---------------|----------------|---------------|--------------------------|------------|-------------------|-----------------|
| B1->2 | | | | | | | | |
| B2->3 | | | | | | | | |
| B3->4 | | | | | | | | |
| B4->5 | | | | | | | | |
| B5->6 | | | | | | | | |

- **Entity at Risk**: `entity.field_name — risk description`. Field must be from
  the upstream exit manifest. Entity-only annotations fail C-20.
- **Transport and Processing Overhead**: independent numeric ms estimates. "Negligible"
  does not qualify.
- **Total**: must equal Transport + Processing Overhead.
- **SLA% / Cumulative SLA%**: derive from catalog publication SLA cited in T-01.

After the table, state **DOMINATION POINT**: the boundary where Cumulative SLA% first
exceeds 50% of the catalog publication SLA. State the exact cumulative percentage and a
one-sentence justification. Include the incumbent equivalent elapsed time from T-01 for
context: "At B[N]->[N+1], cumulative automated latency is [X]% of the catalog SLA,
compared to [MS-NN] incumbent duration of [Y hrs] in T-01."

---

### SECTION 10 — STALE WINDOW ANALYSIS

Accumulate stage and boundary latencies sequentially (Transport and Processing Overhead
addends separate at each boundary step). Compare final total against:

1. **Catalog publication SLA** (cite T-01): FRESH or STALE
2. **INCUMBENT TOTAL** (cite T-01): does automated pipeline complete faster or slower
   than the incumbent sequential process?
3. **Worst-case failure mode** (cite LP-NN or NH-NN): FRESH or STALE

---

### SECTION 11 — RECOVERY AUDIT TABLE [T-10]

Begin with `[T-10] RECOVERY AUDIT TABLE`. Cite upstream T-NN tokens as declared in
the scaffold. One row per NH-NN and LP-NN. All five columns required.

| Trigger ID | Triggering Condition | Recovery Mechanism | MS Step ID | Incumbent Step (verbatim from T-01) |
|------------|---------------------|-------------------|------------|-------------------------------------|

**Incumbent-centric recovery framing**: every recovery entry must be written as
"On [condition], revert to [MS-NN]: [incumbent step description]." A recovery entry
that describes a technical mechanism (retry queue, dead-letter) without naming the
incumbent fallback step fails C-14. The MS-NN citation must match the step declared in
the INCUMBENT EQUIVALENT block for the same stage or boundary.

---

### SECTION 12 — CLOSURE GATE TABLE [T-11]

Begin with `[T-11] CLOSURE GATE TABLE`. Structurally separate from T-10.

Enumerate every NH-NN and LP-NN independently. Do not derive from T-10 rows.

| Identifier | Source (stage or boundary) | Recovery Row Present (YES/NO) | Status (CLOSED/OPEN) |
|------------|---------------------------|-------------------------------|----------------------|

Per-identifier status required — count summaries do not qualify.

---

### SECTION 13 — PATTERN ASSESSMENT

Name the integration pattern and one alternative. State ≥2 trade-off dimensions with ≥1
quantified or qualified in Commerce / catalog management terms. Cite the INCUMBENT TOTAL
from T-01 as the baseline comparison (e.g., "batch CDC pipeline completes in [X min]
vs incumbent [Y hrs], but introduces [Z min] stale window risk during CDN propagation
delay that the incumbent does not have — merchandising team must account for this in
flash sale timing").

---

*Narrative anchor contract: T-01 is the primary reference frame. Every stage trace
section cites its T-01 incumbent equivalent by MS-NN before tracing pipeline content.
Every recovery prescription frames reversion to the incumbent. The stale window analysis
compares against INCUMBENT TOTAL. A stage without an INCUMBENT EQUIVALENT block is
a structural deficit regardless of schema or latency coverage.*

---

## V-04 — Combined: Conversational Register + Boundary-First Lifecycle

**Variation axes**: Phrasing register (H1) + Lifecycle emphasis (H2). Question-driven
invitations replace all imperatives. The boundary inventory is produced as a structural
commitment (T-03) before stage trace tables, with entity-at-risk stubs requiring
entity.field update after stage exit manifests.

**Hypothesis**: Combining conversational phrasing with boundary-first lifecycle tests
whether the two axes compound or cancel. Boundary-first structure creates explicit
pre-committed row stubs that the model must return to fill — this structural pressure
may partially compensate for weakened scaffold enforcement from conversational phrasing.
Predicts: boundary pre-commitment drives C-11 labeling (all rows pre-declared), but
conversational phrasing weakens upstream-references column in scaffold (sparse T-NN
tokens). Net C-24 score between V-01 (17/17) and V-02 (15/17) in R11, but with a
different gap pattern — upstream references sparsely populated rather than scaffold
absent. C-17/C-20 outcome depends on whether model returns to T-03 stubs after producing
exit manifests.

Scenario: Finance — payroll processing pipeline. Timesheet events from a workforce
management system flow through pay calculation, deduction processing, tax withholding,
payment file generation, and GL payroll posting. Stages: Timesheet Capture => Pay
Calculation => Deduction Processing => Tax Withholding => Payment File Generation =>
GL Payroll Posting.

---

You are a Finance data domain expert. I'd like to walk through a payroll processing
pipeline with you — from workforce management timesheet events through pay calculation,
deductions, tax withholding, payment file generation, and GL payroll posting.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### Planning Table

Before we start, could you map out the tables you'll produce? I'd like to see boundaries
as a top-level planning entry — listed in the planning table before the stage trace tables,
since the boundaries are structural commitments that stage trace sections will need to
satisfy.

| Table # | What this table contains | Purpose (which criteria?) | Which prior tables feed into this? |
|---------|--------------------------|--------------------------|-------------------------------------|
| T-01 | [name] | [purpose] | [T-NN references or "none"] |
| T-02 | ... | ... | ... |
| ... | ... | ... | ... |

I'd expect something like:
- T-01: the manual payroll process before automation (foundational)
- T-02: the entities you'll trace (foundational)
- T-03: the boundary inventory, declared early as a structural commitment (draws from T-02)
- T-04 through T-09: stage trace tables that satisfy the boundary row commitments in T-03
- T-10: recovery audit (draws from T-01, T-03, and all stage tables)
- T-11: closure gate (draws from T-10)

Could you fill in the "Which prior tables feed into this?" column for every row? It helps
me understand how your outputs connect. If a table draws from prior tables, listing those
T-NN tokens is more useful than "see prior sections."

---

### What did manual payroll look like?

Before the automated pipeline, what did the payroll team do manually? Could you walk me
through the incumbent process in a table?

| Step ID | Manual Step | Who did it | How long |
|---------|-------------|------------|----------|
| MS-01 | [step description] | [payroll analyst / payroll manager / etc.] | [time] |
| ... | ... | ... | ... |

Five specific steps minimum — things like "MS-01: Payroll analyst manually exports
timesheet data from workforce management portal and validates hours against manager-
approved timecards in shared spreadsheet — 4 hrs per biweekly cycle." Generic steps
aren't specific enough.

After the table:
- What's the **INCUMBENT TOTAL** elapsed time?
- What's the **Payroll close SLA** — maximum elapsed time from timesheet lock to GL
  payroll posting and payment file transmission (numeric, in hours)?

When we get to the recovery section, we'll be linking each failure back to a specific
MS-NN step from this table — so please keep these step IDs handy.

---

### What entities are in play?

Could you enumerate the domain entities before we start tracing? I want everything in
scope declared here so nothing appears for the first time mid-trace.

| Entity Name | Domain | Key Fields | Role |
|-------------|--------|------------|------|

I'd expect at minimum: TimesheetRecord, PayCalculationResult, DeductionSummary,
TaxWithholdingEntry, PaymentFile, GLPayrollEntry.

Please also restate the payroll close SLA here as the anchor for all downstream
latency comparisons.

---

### Boundaries first — a structural commitment

Before we trace the stages, could you lay out the inter-stage boundaries as a
pre-committed structural table? Think of these as rows you're committing to fill
completely — including entity-at-risk at entity level now, and specific entity.field
citations after each stage's exit manifest is available.

| Boundary | Error Handling | Schema Change? | Entity at Risk | Transport (ms) | Processing Overhead (ms) | Total (ms) | SLA% | Cumulative SLA% |
|----------|---------------|----------------|----------------|---------------|--------------------------|------------|------|-----------------|
| B1->2 | | | | | | | | |
| B2->3 | | | | | | | | |
| B3->4 | | | | | | | | |
| B4->5 | | | | | | | | |
| B5->6 | | | | | | | | |

A few things I'm looking for in this pre-commitment:
- For **Error Handling**: named mechanism, or `NH-NN: no handling — risk accepted` (assign
  the NH-NN identifier here so we can cite it consistently later).
- For **Entity at Risk**: entity name from T-02 for now; please update to `entity.field_name
  — risk description` after each stage's exit manifest is produced.
- For **Transport and Processing Overhead**: rough numeric estimates are fine at this stage;
  update after stage trace confirms latency values.
- For **SLA% columns**: derive from payroll close SLA.

After you produce the stage trace sections below, please return here and update the Entity
at Risk column with entity.field citations from the stage exit manifests. A row that still
shows entity-name-only after exit manifests are available would be a gap.

After the full table (post-stage-trace): tell me which boundary dominates the SLA budget
— the first where Cumulative SLA% crosses 50%, with the exact percentage and a one-
sentence justification.

---

### Stage-by-stage trace

For each stage, could you show me the typed exit manifest and stage trace? Use the T-NN
header from the planning table (e.g., `[T-04] STAGE TRACE — Stage 1: Timesheet Capture`).

| Field | Type at Exit | Schema Change? | Data Loss Risk | Stage Latency |
|-------|-------------|----------------|----------------|---------------|

- **Schema change**: if no change, something like "NONE — verified: no field added,
  removed, renamed, or retyped" is clearer than just "unchanged."
- **Data Loss Risk**: please assign LP-NN identifiers here — specific enough to be
  actionable (e.g., "LP-01: TimesheetRecord entries with null manager_approval_id
  excluded from PayCalculation — employee underpaid, discovered at next cycle
  reconciliation").

After each table, the typed exit manifest:

```
EXIT MANIFEST — Stage N: [entity name]
  fields: [count]
  key field assertions:
    [field_name: TYPE(precision)]  (at least two)
```

When no error handling exists: `NH-NN: no handling — risk accepted at [location]`.

After producing each manifest, could you also return to the boundary pre-commitment table
above and update the Entity at Risk cell for the relevant boundary with the entity.field
citation?

Stages:
1. Timesheet Capture — workforce management → payroll intake queue
2. Pay Calculation — payroll intake queue → pay calculation engine
3. Deduction Processing — pay calculation engine → deduction service
4. Tax Withholding — deduction service → tax engine
5. Payment File Generation — tax engine → payment file service
6. GL Payroll Posting — payment file service → payroll GL subledger

---

### How stale does payroll data get?

Could you walk me through accumulated latency from Timesheet Capture through GL Payroll
Posting, showing Transport and Processing Overhead separately at each boundary? Under
normal operation — is the final GL posting fresh or stale against the payroll close SLA?
Under the worst failure (name it, cite LP-NN or NH-NN)?

---

### Recovery plan

For each NH-NN and LP-NN you've declared, what's the recovery path?

| Trigger ID | What triggered it | Recovery mechanism | Which MS step? | Incumbent step (verbatim) |
|------------|------------------|-------------------|----------------|--------------------------|

Each entry should link back to a specific MS-NN step from the incumbent baseline — the
actual step the payroll team would revert to if this failure occurred. Full verbatim step
text from T-01 helps confirm the link.

---

### Closure check

Before finishing, could you enumerate every NH-NN and LP-NN declared anywhere (not from
the recovery table — go back to where each was originally declared) and confirm coverage?

| Identifier | Where declared | Recovery row? | Status |
|------------|---------------|---------------|--------|

Per-identifier status, please — a count summary doesn't surface gaps.

---

### Pattern assessment

What's the integration pattern? One alternative pattern, ≥2 trade-off dimensions with
≥1 quantified in payroll / Finance terms.

---

*Planning table contract: the planning table is the navigational map for this walkthrough.
T-NN tokens from that table are the cross-reference currency for every citation that
follows. The boundary pre-commitment table (T-03) is a structural row-level commitment —
entity-at-risk fields must be updated with entity.field citations after each stage's exit
manifest is produced.*

---

## V-05 — Combined: Scaffold-First + Inertia-First + Three-Role Sequence

**Variation axes**: Output format (scaffold-first, C-24) + Inertia framing (incumbent-
centric, C-14/C-15/C-16) + Role sequence (Operations → Finance → Commerce, with a
Scaffold Architect pre-pass).

**Hypothesis**: V-02 in R11 scored 15/17 because the two-role Scaffold Authority design
did not produce a unified STEP 0 before domain roles began. V-05 tests a four-pass
architecture: Scaffold Architect (scaffold only) → Operations (incumbent baseline, T-01,
as its sole output before any pipeline content) → Finance (SLA budget + entity inventory)
→ Commerce (pipeline stages, boundary inventory, stale window, recovery audit, closure
gate). Anchoring T-01 = INCUMBENT BASELINE as an Operations-only output before Finance
and Commerce begin predicts full C-14/C-15/C-16 compliance — the role with deepest
incumbent knowledge declares the baseline table, and every downstream recovery
prescription cites T-01 by T-NN. Commerce, as the pipeline trace role, must cite T-01
MS-NN steps in recovery entries without having produced the table itself, which enforces
cross-role traceability rather than within-role traceability.

Scenario: Operations/Finance/Commerce — multi-tier inventory sync. Physical count events
from a warehouse management system flow through DC-level reconciliation, financial
inventory valuation, financial reserve calculation, commerce availability broadcast, and
storefront cache sync. Stages: Physical Count Event => DC Reconciliation => Inventory
Valuation => Financial Reserve Calculation => Commerce Availability Broadcast =>
Storefront Cache Sync.

---

You are tracing data through a multi-tier inventory synchronization pipeline. Four passes
run in the sequence **Scaffold Architect → Operations → Finance → Commerce**. Each pass
has an exclusive scope — a pass may not produce content outside its scope. Passes run in
this order; the sequence may not be reordered.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### SCAFFOLD ARCHITECT PASS

**The Scaffold Architect produces ONLY the OUTPUT TABLE SCAFFOLD below. It may not produce
any domain context, entity vocabulary, incumbent steps, SLA values, stage content, or any
table other than the scaffold. All domain content begins only after the scaffold is closed.
Any scaffold row that cites a T-NN token not yet declared earlier in the same scaffold
table is an out-of-order declaration — reorder before closing.**

Produce the scaffold as the following four-column table. Every table appearing anywhere
in this response must have a row here. No domain pass may introduce a table not registered
in this scaffold.

| Table # | Table Name | Purpose | Upstream Tables |
|---------|------------|---------|-----------------|
| T-01 | [table name] | [purpose + criteria] | [T-NN references or "none"] |
| T-02 | ... | ... | ... |
| ... | ... | ... | ... |

**Required scaffold entries in dependency order** (tables with no upstream references
first; tables that reference prior tables after):
- T-01: Incumbent Baseline Table (C-15) — upstream: none — **produced by Operations only**
- T-02: Entity Inventory Table (C-10) — upstream: none — produced by Finance
- T-03 through T-08: Stage Trace Tables, one per stage (C-04, C-19) — upstream: T-01, T-02
  — produced by Commerce
- T-09: Boundary Inventory Table (C-11, C-17, C-21, C-22) — upstream: T-02, T-03–T-08
  — produced by Commerce
- T-10: Recovery Audit Table (C-18, C-16) — upstream: T-01, T-09, T-03–T-08
  — produced by Commerce (must cite T-01 MS-NN steps produced by Operations)
- T-11: Closure Gate Table (C-23) — upstream: T-10 — produced by Commerce

**Upstream Tables column enforcement**: the "none" value is valid only for tables that
structurally draw from no prior table. T-10 (Recovery Audit) must list T-01, T-09, and
all stage T-NN tokens. T-11 (Closure Gate) must list T-10. A table that references prior
tables but declares "none" is an invalid scaffold entry.

After completing the scaffold table, append:
`SCAFFOLD CLOSED — [N] tables declared. Scaffold Architect pass complete. Proceed to
Operations.`

---

### OPERATIONS PASS

**Operations produces ONLY T-01 (Incumbent Baseline Table). Operations may not produce
entity inventory, stage trace content, SLA values, or any table not registered in the
scaffold. The incumbent baseline is the exclusive deliverable of this pass.**

Begin with: `Citing scaffold entry: T-01`

**[T-01] INCUMBENT BASELINE TABLE**

Document the manual inventory count and reconciliation process this pipeline replaces.
This table is the T-01 narrative anchor — Finance and Commerce must cite T-01 MS-NN steps
in all recovery prescriptions. Cite by T-01 reference; do not re-declare in downstream
passes.

| Step ID | Manual Step | Actor/Team | Duration |
|---------|-------------|------------|----------|
| MS-01 | [step description] | [DC supervisor / inventory analyst / etc.] | [time] |
| ... | ... | ... | ... |

**Minimum five distinct steps** specific to physical inventory count and DC reconciliation
operations (e.g., `MS-01: DC floor supervisor leads physical count team through warehouse
aisles, manually recording unit counts on paper count sheets — 6 hrs per annual full-count
cycle`). Generic steps do not qualify.

After the table:
- **INCUMBENT TOTAL**: additive sum of all Duration values. Fixed at declaration. Finance
  and Commerce must cite this value by T-01 reference; they may not re-derive.
- **MS-NN Citation requirement**: every recovery entry in T-10 must cite a specific MS-NN
  step from this table. Commerce (which produces T-10) is responsible for T-01 citation
  accuracy. An entry that names the process category without an MS-NN step identifier
  fails C-16.

After T-01 is complete, state: `T-01 COMPLETE. Operations pass closed. Proceed to Finance.`

---

### FINANCE PASS

**Finance produces T-02 (Entity Inventory Table) and declares the inventory reconciliation
SLA. Finance may not produce stage trace content, boundary tables, or recovery tables.
Finance may not produce any table not registered in the scaffold.**

Begin with: `Citing scaffold entries: T-02`

**[T-02] ENTITY INVENTORY TABLE**

| Entity Name | Domain | Key Fields | Role in Pipeline |
|-------------|--------|------------|-----------------|

Required entities: PhysicalCountEvent, DCReconciliationRecord, InventoryValuationEntry,
FinancialReserveAdjustment, CommerceAvailabilityPayload, StorefrontCacheUpdate.

After the entity inventory table, state the following **SLA DECLARATION** (immutable —
Commerce must cite these values by T-02 reference in all latency comparisons; Commerce
may not re-declare or adjust these values):
- **Inventory reconciliation SLA**: maximum elapsed time from physical count event capture
  to storefront availability reflecting updated stock (numeric, in hours)
- **Peak count volume assumption**: units counted per day during annual inventory audit

After T-02 is complete, state: `T-02 COMPLETE. Finance pass closed. Proceed to Commerce.`

---

### COMMERCE PASS

**Commerce produces T-03 through T-11. Commerce may not produce any table not registered
in the scaffold. Commerce must cite T-01 MS-NN steps by identifier in all recovery entries
in T-10 — not by process category. Commerce must cite T-02 SLA values by T-02 reference
in all latency comparisons.**

Begin with: `Citing scaffold entries: T-03, T-04, T-05, T-06, T-07, T-08, T-09, T-10,
T-11 (upstream from T-01 and T-02 as declared in scaffold)`

---

**[T-03 through T-08] STAGE TRACE — Stages 1 through 6**

For each stage, produce a table using its scaffold-declared T-NN header:
`[T-NN] STAGE TRACE — Stage N: [Stage Name]`

**Required columns**:

| Field | Type | Schema Delta | Data Loss Risk | Stage Latency |
|-------|------|-------------|----------------|---------------|

- **Field + Type**: `field_name: TYPE(precision)` at stage exit.
- **Schema Delta**: named changes or `NONE — verified: no field added, removed, renamed,
  or retyped`. Bare "NONE" without verification fails C-12.
- **Data Loss Risk**: assign LP-NN at declaration. Example: `LP-01: PhysicalCountEvent
  records with count_variance exceeding tolerance threshold written to exception queue —
  InventoryValuationEntry not produced; financial reserve calculation runs on stale
  balance`. "Errors may occur" does not qualify.
- **Stage Latency**: value, range, or characterization. May not be omitted.

After each stage table, produce a **Typed Exit Manifest**:

```
EXIT MANIFEST — Stage N: [entity name]
  fields: [count at exit]
  key field assertions:
    [field_name: TYPE(precision)]
    [field_name: TYPE(precision)]
    (minimum two)
```

When no error handling: `NH-NN: no handling — risk accepted at [location]`.

**Stages**:
1. Physical Count Event — WMS count terminal → reconciliation intake queue
2. DC Reconciliation — reconciliation intake → DC reconciliation engine
3. Inventory Valuation — DC reconciliation engine → valuation service
4. Financial Reserve Calculation — valuation service → reserve calculation engine
5. Commerce Availability Broadcast — reserve engine → commerce availability API
6. Storefront Cache Sync — availability API → CDN edge cache

---

**[T-09] BOUNDARY INVENTORY TABLE**

Begin with `[T-09] BOUNDARY INVENTORY TABLE`. One row per inter-stage boundary. All nine
columns required — blank cells are structural gaps.

| Boundary | Error Handling | Schema Change | Entity at Risk | Transport (ms) | Processing Overhead (ms) | Total (ms) | SLA% This Boundary | Cumulative SLA% |
|----------|---------------|---------------|----------------|---------------|--------------------------|------------|-------------------|-----------------|
| B1->2 | | | | | | | | |
| B2->3 | | | | | | | | |
| B3->4 | | | | | | | | |
| B4->5 | | | | | | | | |
| B5->6 | | | | | | | | |

- **Entity at Risk**: `entity.field_name — risk description`, entity from T-02, field from
  upstream exit manifest. Entity-only fails C-20.
- **Transport and Processing Overhead**: independent numeric ms estimates. "Negligible"
  does not qualify.
- **Total**: must equal Transport + Processing Overhead.
- **SLA% / Cumulative SLA%**: derive from inventory reconciliation SLA in T-02.

After the table, state **DOMINATION POINT**: first boundary where Cumulative SLA%
exceeds 50%, with exact crossing percentage and a one-sentence justification.

**Stale Window Analysis** (append after boundary table):

Accumulate stage and boundary latencies sequentially (Transport and Processing Overhead
separate at each boundary step):

- After Stage 1: [elapsed]
- After B1->2: [Transport: X ms + Processing: Y ms = cumulative Z ms]
- ... continue through Stage 6 ...

Compare final total against inventory reconciliation SLA (cite T-02) and INCUMBENT TOTAL
(cite T-01):
1. Normal operation: FRESH or STALE
2. Worst-case failure mode (cite LP-NN or NH-NN): FRESH or STALE
3. Incumbent comparison: is automated pipeline faster or slower than INCUMBENT TOTAL?

---

**[T-10] RECOVERY AUDIT TABLE**

Begin with `[T-10] RECOVERY AUDIT TABLE`. Cite upstream tables by T-NN. One row per
NH-NN and LP-NN. All five columns required — missing rows are structural gaps.

| Trigger ID | Triggering Condition | Recovery Mechanism | MS Step ID | Incumbent Step (verbatim from T-01) |
|------------|---------------------|-------------------|------------|-------------------------------------|

**T-01 citation requirement**: every row must cite a specific MS-NN step from T-01
(produced by Operations). The verbatim step text from T-01 must appear in the final
column. A recovery entry that names the incumbent process category without an MS-NN
step identifier fails C-16. Commerce is responsible for cross-role citation accuracy.

---

**[T-11] CLOSURE GATE TABLE**

Begin with `[T-11] CLOSURE GATE TABLE`. Structurally separate from T-10.

Enumerate every NH-NN and LP-NN independently — do not derive from T-10 rows. Check
each against T-10.

| Identifier | Source (stage or boundary) | Recovery Row in T-10 (YES/NO) | Status (CLOSED/OPEN) |
|------------|---------------------------|-------------------------------|----------------------|

Per-identifier status required. Count summaries ("9 of 10 covered") do not qualify.

**Pattern Assessment** (append after T-11):

Name the integration pattern and one alternative. State ≥2 trade-off dimensions with
≥1 quantified in inventory / Commerce terms. Cite T-01 INCUMBENT TOTAL as the comparison
baseline.

---

*Scaffold contract: the Scaffold Architect declares the complete table contract before
any domain pass begins. Operations produces only T-01. Finance produces only T-02.
Commerce produces T-03 through T-11. A pass that produces a table not registered in the
scaffold is a scaffold violation. A T-10 recovery entry that does not cite a T-01 MS-NN
step by identifier is a C-16 violation. Complete every table — no blank cells, no
"negligible" in numeric latency columns.*
