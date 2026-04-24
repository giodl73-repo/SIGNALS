# flow-resilience — Round 17 Variations (Rubric v16)

**Rubric**: v16 · 42 aspirational criteria · Ceiling entering R17: 41/42 → 99.76 (R16 V-04 and V-05 tied)

**Open criteria entering R17**: **C-49 and C-50 — mutually exclusive in the R16 field.**

- **C-49** requires: enforcement preamble positioned BEFORE all sub-parts, with at least one sub-part containing inline reinforcement citing preamble rules by their named labels.
- **C-50** requires: three or more structurally independent locations at different document hierarchy levels, with at least one location carrying an explicit restatement label (e.g., "(restated for co-location)").

**R16 diagnosis**:
- V-04 PASS C-49, FAIL C-50: Has preamble before all sub-parts and inline citations in 1b/1c/1d and Column Contract (3+ locations at 3 hierarchy levels). Sole gap: NO explicit restatement label on any location.
- V-05 FAIL C-49, PASS C-50: Has 3 locations with "(restated for co-location)" label. Sole gap: enforcement embedded WITHIN sub-part 1d — not before all sub-parts.

**R17 synthesis path**: V-04 structure is already C-50-eligible (3 locations at 3 hierarchy levels). Adding one explicit "(restated for co-location)" label to the Column Contract Recovery Path entry achieves C-50 PASS without disturbing C-49. The 100.00 ceiling (42/42) is achievable in R17.

| Variation | Axis | Hypothesis | C-49/C-50 Strategy |
|---|---|---|---|
| V-01 | C-49+C-50 synthesis (minimal — single-axis) | V-04 + restatement label on Column Contract entry closes C-50 | Preamble before 1a + sub-part inline cites + "(restated for co-location)" in Column Contract |
| V-02 | Phrasing register — formal legal enumeration | Formal § labels with (restated) marker make enforcement locations independently locatable and explicitly redundant | Same 3-location synthesis, formal register throughout |
| V-03 | Role sequence — D-phase named at document open | Declaring D-phase ownership at document header (before C-phase expansion) places enforcement in a fourth hierarchy level (role declaration) | Role-declaration preamble level + document preamble level + sub-part level + column contract level |
| V-04 | Lifecycle emphasis + synthesis | Per-stage named sub-specification with SLA reference and restatement label at stage granularity creates strongest possible enforcement chain | Synthesis + expanded Recovery Path stage sub-specs with inline Rule B restatement at stage level |
| V-05 | Full synthesis — all axes | All axes combined: inertia framing + formal register + lifecycle emphasis + role sequence + synthesis | All of the above |

---

## V-01 — Single-Axis: C-49+C-50 Minimal Synthesis

**Axis**: C-49+C-50 combination — minimal change from V-04 (R16). The sole structural addition is an explicit "(restated for co-location)" label on the Column Contract Recovery Path entry's Rule B reference. V-04 (R16) already has three independent enforcement locations at three distinct hierarchy levels (preamble, sub-part, column contract); it lacks only the explicit restatement label required for C-50.

**Hypothesis**: V-04 (R16) is already C-50-structurally compliant — it has 3+ independent locations spanning 3 hierarchy levels. The only gap is the missing explicit restatement label. Adding "(restated for co-location)" to the Column Contract Recovery Path Rule B reference closes C-50 without altering C-49. Result: 42/42.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic}, identify the real competitor (inertia — doing nothing), and produce
a complete failure analysis that makes the cost of inaction measurable.

Two roles fill all columns:
- **C — Commerce Expert**: #, Class, Trigger Condition, State, Capability, Data at Risk,
  Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D — Distributed Systems Expert**: Recovery Path, Verification Signal, Chaos Block

---

### Pre-Commitment Document: Resilience Commitment Matrix

**Document Enforcement Contract** (read before filling any sub-part):

> This document pre-commits values that bind the scenario table. Two rules govern all fills:
>
> **Rule A — No Deferral**: "TBD", blank cells, "N/A", or any equivalent placeholder in any
> sub-part of this document fails the pre-commitment requirement. Every cell must carry an
> actual value when this document is authored. Deferral to "fill in later" is not permitted.
>
> **Rule B — No Per-Row Invention**: Values established in this document's sub-parts are the
> authoritative sources for their respective scenario columns. Independently authoring values
> per scenario row that are not drawn from the corresponding sub-part is a named contract
> violation. Row fills must reference the sub-part by label; they must not introduce new
> values.
>
> Rule A closes the placeholder escape. Rule B closes the per-row reinvention escape.
> Both rules apply. A document that satisfies one without the other fails this enforcement
> contract.

---

**Step 1a — Status Quo Competitor: The Cost of Inaction**

Name the status quo — doing nothing — as the competitor being displaced. For {topic}, write
2–3 sentences establishing:
(1) what the current failure mode looks like without any resilience investment;
(2) why inertia is the default choice (failures are invisible until they compound);
(3) what makes {topic}'s domain specifically fragile (connectivity isolation + idempotency
    gaps + partition conflict).

**Step 1b — Per-Class Carrying Costs**

The do-nothing cost per class. Status Quo Risk column references this sub-part.
No blanks — **Rule A applies**. Status Quo Risk fills reference "Step 1b, Class N" —
**Rule B applies**; per-row invention is a contract violation.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Offline | [metric] | per-session | without ceiling |
| 2 — Partial failure | Degraded service | [metric] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [metric] | per-transaction | compound growth |

**Step 1c — Per-Class Tipping Point Signals**

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [quantified, e.g., "cart-abandon rate >2% above 30-day baseline / dashboard alert"] | [metric] |
| 2 | [quantified, e.g., "oversell count >50/month / inventory anomaly counter"] | [metric] |
| 3 | [quantified, e.g., "reconciliation backlog >200 / queue-depth alert"] | [metric] |

No blanks — **Rule A applies**.

**Step 1d — SLA Budget**

| Class | TTD | TTC | TTR | TTV |
|---|---|---|---|---|
| 1 — Connectivity loss | | | | |
| 2 — Partial failure | | | | |
| 3 — Split-brain | | | | |

**Rule A applies**: no cell may be blank or TBD — every cell requires an actual time value.
**Rule B applies**: Recovery Path SLA fills must reference "Step 1d, Class N, stage" — per-row
independently authored SLA values are a contract violation against this table.

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` — single table, no owner-group splits | Anti-split instruction (below) |
| Section | Phase gate — all rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | In-row bold performative inside Content descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary instruction**: Do not create separate tables for Commerce Expert columns and
Distributed Systems Expert columns. Do not insert a horizontal rule, heading, or section break
between rows when column ownership shifts. Do not create a standalone chaos section or
standalone chaos-engineering table. Do not create a standalone observability section or
standalone observability table. All four consolidation escape routes are closed.

**Section Order Requirement**: (1) Pre-Commitment Document — complete all four sub-parts;
(2) Scenario Table — row N columns AND row N Chaos Test Block before row N+1; (3) Gap Register;
(4) Inertia Verdict; (5) Finding Completeness Checklist. **Advancing to row N+1 before row N
columns and Chaos Block are complete is a sequencing violation. Advancing to the Gap Register
before all three rows and Chaos Blocks are complete is a sequencing violation.**

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1–3 |
| Class | C | Class 1, 2, or 3 |
| Trigger Condition | C | Quantified threshold expression + detection signal. Qualitative only fails. |
| State | C | System state at failure onset |
| Capability | C | Named commerce operations available during failure |
| Data at Risk | C | Named data fields or records at risk |
| Status Quo Risk | C | **Reference Step 1b, Class N (Rule B — not independently authored)**. Acute branches (A/B) before chronic. Chronic: rate + horizon + metric. |
| Failure Signature | C | Behavioral fingerprint per actor during failure. ≥2 actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label + blast-radius qualifier |
| Conflict Resolution | C | Canonical: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale` + adequacy judgment |
| Recovery Path | D | Detect → Contain → Recover → Validate. Actor-chain prefix + mechanism + **SLA from Step 1d, Class N, stage — Rule B applies (restated for co-location): independently authored SLA values are a named contract violation against this pre-committed budget** + named Verification Signal. ≥3 of 4 stages with actor prefix. |
| Verification Signal | D | Named observable artifact per stage, distinct from mechanism |
| Chaos Block | D | Inject / Expected Behavior / Pass Signal / Fail Signal — co-located per row |

#### Failure Signature Class Boundary Discriminator

> **Class 2**: Transaction-level anomaly framing from a single write path. The inconsistency
> is visible at the transaction boundary — one leg committed, other leg absent. No inter-node
> framing. Example: "client: checkout spinner with no confirmation; server: inventory write
> committed, payment 503; transaction boundary: partial — reservation exists, order null."
>
> **Class 3**: Node-A / node-B diverging state framing showing both nodes holding conflicting
> last-write values simultaneously. No single-transaction framing. Example: "node-A: holds
> inventory = 47 (checkout-A applied); node-B: holds inventory = 47 (checkout-B applied,
> diverging); observability: conflict event absent during partition, surfaces only at healing."
>
> Generic inconsistency descriptions satisfying either class without class-specific framing fail
> even with multiple actor viewpoints.

#### Conflict Resolution Vocabulary Constraint

Canonical terms: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text
paraphrase fails. Class 3 row must apply a canonical label with an adequacy judgment citing
this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first.

Do-nothing scenario: cart silently dropped, user gets no recovery signal, cost accumulates
per-session without bound.

Trigger Condition: quantified connectivity threshold + detection signal.
State: client isolation at failure onset.
Capability: named offline-available operations.
Data at Risk: in-flight cart, pending payment intent, order submission records.
Status Quo Risk: **Step 1b, Class 1** (Rule B). Acute: cart dropped → immediate abandonment;
cart stale-restored → incorrect inventory at reconnect. Chronic: carrying cost metric, rate,
horizon from Step 1b.
Failure Signature: Class 1 — client timeout + server shows no request in access log.
Severity / Blast Radius.

D-phase after C-phase is complete:
Recovery Path: **Step 1d, Class 1** (Rule B — cite by label). Actor-chain prefixes.
Named Verification Signal per stage.
Chaos Block: inject / expected / pass / fail.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column —
Failure Signature with ≥2 actor viewpoints (Class 1 framing), Status Quo Risk citing Step 1b
Class 1 by label, Recovery Path SLA citing Step 1d Class 1 by label per Rule B, all four
stages with actor-chain mechanism and named Verification Signal — AND Row 1 Chaos Test Block
is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first.

Do-nothing scenario: oversell accumulates silently per deploy; inventory drift is invisible
until a customer disputes the double-reservation.

Failure Signature: **Class 2 — transaction-level anomaly** (single write path). Not inter-node.
Trigger Condition, State, Capability, Data at Risk.
Status Quo Risk: **Step 1b, Class 2** (Rule B). Acute: phantom hold / oversell on silent drop.
Chronic: oversell per-deploy unbounded.

D-phase: Recovery Path **Step 1d, Class 2** (Rule B). Actor-chain. Named VS. Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete, including Class 2
transaction-level Failure Signature and Recovery Path SLA citing Step 1d Class 2.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first.

Do-nothing scenario: duplicate charges compound per transaction; reconciliation backlog grows
indefinitely; damage is invisible until two orders arrive at the warehouse.

Failure Signature: **Class 3 — node-A / node-B diverging state**. Not single-transaction.
Trigger Condition, State, Capability, Data at Risk.
Status Quo Risk: **Step 1b, Class 3** (Rule B). Acute: `last-write-wins` / `manual-reconcile`.
Chronic: duplicate-charge compound growth.
Conflict Resolution: canonical label + adequacy judgment.

D-phase: Recovery Path **Step 1d, Class 3** (Rule B). Actor-chain. Named VS per stage.
Chaos Block: inject partition / expected / pass / fail.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Block are complete.**

---

### Gap Register

Three findings inline — no separate observability section:

Per finding: **Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

HIGH / MEDIUM / LOW. Strongest argument against deferral naming the do-nothing scenario from
Step 1a, gap findings, and carrying costs from Step 1b (2–3 sentences).

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3

---

## V-02 — Phrasing Register Axis: Formal Legal Enumeration

**Axis**: Phrasing register throughout shifts to formal legal enumeration style. The enforcement
preamble becomes a numbered "§ 1 Enforcement Mandate" with numbered clauses. Inline sub-part
reinforcements cite "§ 1.1" and "§ 1.2" by section number. The Column Contract Recovery Path
entry carries the restatement label using formal "(§ 1.1 restated at column-contract level)".

**Hypothesis**: Formal § numbering creates the most unambiguous identifier space for the two
enforcement mechanisms — each can be cited by section number rather than by descriptive label,
reducing interpretive ambiguity. The formal register also clarifies that inline cross-references
are not paraphrases but cited-by-number restatements, making the C-50 multi-location chain
maximally explicit.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic} across three structurally distinct failure classes. Produce a complete
four-field failure analysis per class, a Gap Register, and an Inertia Verdict.

Two roles fill all columns:
- **C — Commerce Expert**: #, Class, Trigger Condition, State, Capability, Data at Risk,
  Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D — Distributed Systems Expert**: Recovery Path, Verification Signal, Chaos Block

---

### Pre-Commitment Document: Resilience Commitment Matrix

**§ 1 — Enforcement Mandate** (governing all sub-parts of this document):

> **§ 1.1 — Placeholder Prohibition**: "TBD", blank cells, "N/A", or any equivalent
> unfilled value in any sub-part of this document is a named contract violation. The
> pre-commitment is void if any cell is deferred. Every cell must carry an actual value
> at the time this document is authored, without exception.
>
> **§ 1.2 — Per-Row Invention Prohibition**: Values established in this document's
> sub-parts are the sole authoritative sources for their corresponding scenario columns.
> Independently authoring per-row values that are not drawn from the corresponding
> sub-part constitutes a named contract violation. All row-level fills must reference
> the source sub-part by its label (e.g., "Step 1b, Class 2" or "Step 1d, Class 3,
> TTR column"). A fill citing no sub-part label is a contract violation regardless of
> numerical plausibility.
>
> Both clauses apply simultaneously. A document satisfying § 1.1 without § 1.2, or
> § 1.2 without § 1.1, fails this Enforcement Mandate.

---

**Step 1a — Domain Fragility Framing**

Write 2–3 sentences establishing {topic}'s structural fragility across the three failure
classes. Domain-specific framing required — not generic distributed systems boilerplate.
Required coverage: client isolation creates invisible pending-state windows; distributed
writes without idempotency guarantees produce duplicate side effects on retry; concurrent
partition writes create state divergence requiring pre-specified merge rules.

**Step 1b — Per-Class Carrying Costs**

Status Quo Risk column fills reference this sub-part by label ("Step 1b, Class N").
§ 1.1 applies — no blank cells. § 1.2 applies — Status Quo Risk fills must cite this
sub-part; per-row invention is a contract violation.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [named metric] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [named metric] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [named metric] | per-transaction | compound growth |

**Step 1c — Per-Class Tipping Point Signals**

§ 1.1 applies — no blank cells. Quantified threshold expression + named detection metric
required per class. "Worsens over time" is not quantified and fails § 1.1.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [quantified threshold] | [metric] |
| 2 | [quantified threshold] | [metric] |
| 3 | [quantified threshold] | [metric] |

**Step 1d — SLA Budget**

§ 1.1 applies — no cell in this matrix may be blank, "TBD", or "N/A". Every cell requires
an actual time value when this sub-part is authored.

| Class | TTD (Detect) | TTC (Contain) | TTR (Recover) | TTV (Validate) |
|---|---|---|---|---|
| 1 — Connectivity loss | | | | |
| 2 — Partial failure | | | | |
| 3 — Split-brain | | | | |

§ 1.2 applies — Recovery Path SLA fills must cite "Step 1d, Class N, stage column" as
their source. Independently authored SLA values per scenario row are a contract violation
under § 1.2.

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` — one table, no splits | Anti-split instruction (below) |
| Section | Phase gate — all rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | In-row bold performative inside Content descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-split instruction** (four escape routes closed simultaneously): (1) Do not create
separate tables for Commerce Expert columns and Distributed Systems Expert columns. (2) Do not
insert a horizontal rule, heading, or section break between rows when column ownership shifts.
(3) Do not produce a standalone chaos section or standalone chaos-engineering table. (4) Do not
produce a standalone observability section or standalone observability table. All four forms
are negated — satisfying any three without the fourth does not satisfy this instruction.

**Section Order Requirement**: (1) Complete all four sub-parts of the Pre-Commitment Document;
(2) Scenario Table — row N columns AND row N Chaos Test Block before row N+1 begins; (3) Gap
Register with three inline findings; (4) Inertia Verdict; (5) Finding Completeness Checklist.
**Advancing to row N+1 before row N columns and Chaos Block are complete is a sequencing
violation. Advancing to the Gap Register before all three rows and Chaos Blocks are complete
is a sequencing violation.**

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1–3, continuous — one table, no splits |
| Class | C | Class 1 (Connectivity Loss), Class 2 (Partial Failure), or Class 3 (Split-Brain) |
| Trigger Condition | C | Quantified threshold expression + named detection signal. Qualitative description alone fails. |
| State | C | System configuration at failure onset — named components and states |
| Capability | C | Named commerce operations available. "Some functions degraded" fails. |
| Data at Risk | C | Specific named data fields or transaction records |
| Status Quo Risk | C | **Reference Step 1b, Class N — § 1.2 prohibits per-row invention**. Acute branches (A/B) before chronic metric. Chronic: rate + horizon + metric. |
| Failure Signature | C | Behavioral fingerprint per actor during failure. ≥2 named actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | Detect (TTD) → Contain (TTC) → Recover (TTR) → Validate (TTV). Per stage: actor-chain prefix (`client →`, `server →`, `operator →`, `user →`) + mechanism + **SLA from Step 1d, Class N, stage column — § 1.2 restated at column-contract level: any SLA value not drawn from Step 1d is a named contract violation** + named Verification Signal. ≥3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage, distinct from mechanism |
| Chaos Block | D | Inject / Expected Behavior / Pass Signal / Fail Signal — co-located with this row |

#### Failure Signature Class Boundary Discriminator

> **Class 2 specification** (Partial Failure — data consistency violation): Transaction-level
> anomaly framing from a single write path. Observable at the transaction boundary — one leg
> committed, confirmation absent or other leg missing — without requiring multi-node state
> divergence. Node-A / node-B framing is incorrect for Class 2 and collapses the operational
> distinction.
>
> **Class 3 specification** (Split-Brain / Eventual Consistency): Node-A / node-B framing
> showing two nodes holding diverging last-write state simultaneously. Visible across node
> boundaries. Single-transaction framing is incorrect for Class 3 and collapses the
> operational distinction.
>
> Generic "data inconsistency" fills satisfying either class without the class-specific
> structural signature fail this discriminator.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`.
Free-text paraphrase fails. Class 3 row must apply a canonical label with an adequacy
judgment explicitly referencing this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first:

Trigger Condition: quantified connectivity threshold (e.g., "TCP connection attempt exceeds
30s timeout") + detection signal (e.g., "client-side monitor registers ETIMEDOUT; server
access log shows no incoming request").
State: client isolation at failure onset — name {topic} components affected.
Capability: offline-available commerce operations (named) + operations blocked.
Data at Risk: in-flight cart state, pending payment intent, unsubmitted order records.
Status Quo Risk: **Step 1b, Class 1** (§ 1.2). Acute branches: outcome A (cart dropped →
immediate abandonment); outcome B (cart stale-restored → incorrect price/inventory at
reconnect). Chronic: rate + horizon + metric from Step 1b.
Failure Signature: Class 1 — client view (timeout, no TCP reset) + server view (no request
in access log, health probe healthy). Not multi-node framing.
Severity / Blast Radius.

D-phase after C-phase complete:
Recovery Path: **Step 1d, Class 1** (§ 1.2 — cite by label). Actor-chain prefixes ≥3 stages.
Named Verification Signal per stage.
Chaos Block: inject connectivity loss, Expected Behavior, Pass Signal, Fail Signal.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column —
Failure Signature with ≥2 Class 1 actor viewpoints, Status Quo Risk citing Step 1b Class 1
by label, Recovery Path SLA citing Step 1d Class 1 by label (§ 1.2), all four stages with
actor-chain mechanism and named Verification Signal — AND Row 1 Chaos Test Block is
complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first:

Trigger Condition: quantified downstream-service degradation threshold + detection signal.
State: upstream commerce service available; downstream payment service degraded.
Capability: browse/cart available; checkout submission blocked or queued.
Data at Risk: inventory reservation drift, unconfirmed orders, oversell risk.
Status Quo Risk: **Step 1b, Class 2** (§ 1.2). Acute: phantom hold / oversell on silent drop.
Chronic: oversell per-deploy unbounded.
Failure Signature: **Class 2 — transaction-level anomaly**: client-view + server-view +
transaction-boundary view. No node-A / node-B framing.
Severity / Blast Radius.

D-phase: Recovery Path **Step 1d, Class 2** (§ 1.2). Actor-chain. Named VS per stage.
Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete, including
Class 2 transaction-level Failure Signature and Recovery Path SLA citing Step 1d Class 2
by label.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first:

Trigger Condition: replication lag threshold + dual-write conflict counter detection.
State: partition active, both nodes accepting independent writes.
Capability: checkout available on both partition sides; conflict invisible.
Data at Risk: diverging inventory counts, duplicate fulfillment orders, double-charge risk.
Status Quo Risk: **Step 1b, Class 3** (§ 1.2). Acute: `last-write-wins` / `manual-reconcile`.
Chronic: duplicate-charge compound growth.
Failure Signature: **Class 3 — node-A / node-B diverging state**. Not single-transaction.
Conflict Resolution: canonical label + adequacy judgment referencing vocabulary constraint.
Severity / Blast Radius.

D-phase: Recovery Path **Step 1d, Class 3** (§ 1.2). Actor-chain. Named VS per stage.
Chaos Block: inject partition / expected / pass signal / fail signal.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Block are complete,
including: Failure Signature with Class 3 node-A/node-B framing, Conflict Resolution with
canonical label and adequacy judgment, Recovery Path SLA citing Step 1d Class 3 by label.**

---

### Gap Register

Required output section. Three findings inline — no separate observability section.

Per finding: **Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

HIGH / MEDIUM / LOW + strongest argument against deferral (2–3 sentences), naming gap
findings and Step 1b carrying costs as inputs.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3

---

## V-03 — Role Sequence Axis: D-Phase Named at Document Open

**Axis**: Role sequence — both roles are declared and their column ownership established
at the document header, before the Pre-Commitment Document sub-parts begin. The D-phase
role receives an explicit "D-Phase Enforcement Note" at the document header level
(a fourth distinct hierarchy level: document-header role declaration, above the pre-commitment
preamble). Enforcement Rule B appears in this role declaration at header level, in the
document enforcement preamble level, in sub-part 1d level, and in the Column Contract level
— four independent locations at four distinct hierarchy levels.

**Hypothesis**: Naming D-phase ownership and enforcement at the document header (before even
the enforcement preamble) adds a fourth enforcement location at a higher hierarchy level than
the preamble, ensuring four-location cross-level distribution. Scorers reading from the top
encounter Rule B's prohibition at the earliest possible point, before any fill instructions.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic} across three failure classes and produce a complete failure analysis.

### Role Declaration

Two roles fill all scenario columns. Roles are named here at document scope.

**C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk,
Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy.

**D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block.
> **D-Phase Enforcement Note**: The Recovery Path column requires SLA targets drawn from the
> pre-committed SLA Budget sub-part (Step 1d) of the Pre-Commitment Document below.
> Independently authoring SLA values per scenario row without referencing Step 1d is a
> **named contract violation**. This constraint is declared here at document scope because
> it governs D-phase behavior across all scenario rows.

---

### Pre-Commitment Document: Resilience Commitment Matrix

**Document Enforcement Contract** (read before filling any sub-part):

> This document pre-commits authoritative values for the scenario table.
>
> **Rule A — No Deferral**: Any cell left blank, "TBD", "N/A", or equivalent unfilled value
> in any sub-part of this document fails the pre-commitment requirement. Every cell must carry
> an actual value at authoring time.
>
> **Rule B — No Per-Row Invention**: Each sub-part is the sole authoritative source for its
> corresponding column. Per-row independent authoring is a named contract violation. Row fills
> must reference the source sub-part by label. (Rule B restated from D-Phase Enforcement Note
> above — see that note for governing scope.)

---

**Step 1a — Domain Fragility Framing**

Write 2–3 sentences establishing {topic}'s structural fragility across all three failure
classes. Specific to this domain, not generic boilerplate. Cover: client isolation creates
invisible pending-state windows; distributed writes create retry-duplication risk; concurrent
partition writes create state divergence.

**Step 1b — Per-Class Carrying Costs**

**Rule A applies** — no blank cells. **Rule B applies** — Status Quo Risk fills cite "Step 1b,
Class N"; per-row authoring is a contract violation.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [named metric] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [named metric] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [named metric] | per-transaction | compound growth |

**Step 1c — Per-Class Tipping Point Signals**

**Rule A applies** — quantified threshold + named detection metric required per class.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [quantified threshold] | [metric] |
| 2 | [quantified threshold] | [metric] |
| 3 | [quantified threshold] | [metric] |

**Step 1d — SLA Budget**

**Rule A applies** — no blank cells. **Rule B applies** — Recovery Path SLA fills cite
"Step 1d, Class N, stage column"; independent per-row authoring is a contract violation.

| Class | TTD | TTC | TTR | TTV |
|---|---|---|---|---|
| 1 — Connectivity loss | | | | |
| 2 — Partial failure | | | | |
| 3 — Split-brain | | | | |

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` — one table, no splits | Anti-split instruction (below) |
| Section | Phase gate — all rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | In-row bold performative inside Content descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary instruction**: Do not create separate tables for Commerce Expert columns and
Distributed Systems Expert columns. Do not insert a horizontal rule, heading, or section break
between rows when column ownership shifts. Do not produce a standalone chaos section or
standalone chaos-engineering table. Do not produce a standalone observability section or
standalone observability table. All four consolidation escape routes are closed.

**Section Order Requirement**: (1) Role Declaration and Pre-Commitment Document complete;
(2) Scenario Table — each row's scenario columns AND Chaos Test Block before the next row;
(3) Gap Register; (4) Inertia Verdict; (5) Finding Completeness Checklist. **Do not advance
to row N+1 until row N columns AND Chaos Block are both complete. Do not advance to the Gap
Register until all three rows and Chaos Blocks are complete.**

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1–3, continuous |
| Class | C | Class 1, 2, or 3 |
| Trigger Condition | C | Quantified threshold expression + detection signal. Qualitative only fails. |
| State | C | System configuration at failure onset |
| Capability | C | Named commerce operations available during failure |
| Data at Risk | C | Named data fields or transaction records |
| Status Quo Risk | C | **Reference Step 1b, Class N (Rule B)**. Acute branches (A/B) before chronic. Chronic: rate + horizon + metric. |
| Failure Signature | C | Behavioral fingerprint per actor during failure. ≥2 named actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label + blast-radius qualifier |
| Conflict Resolution | C | Canonical: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale` + adequacy judgment |
| Recovery Path | D | Detect → Contain → Recover → Validate. Actor-chain prefix + mechanism + **SLA from Step 1d, Class N, stage (Rule B restated for co-location at column-contract level: independently authored SLA values are a named contract violation against the Step 1d pre-committed budget)** + named Verification Signal. ≥3 of 4 stages with actor prefix. |
| Verification Signal | D | Named observable artifact per stage, distinct from mechanism |
| Chaos Block | D | Inject / Expected Behavior / Pass Signal / Fail Signal — co-located with this row |

#### Failure Signature Class Boundary Discriminator

> **Class 2**: Transaction-level anomaly from a single write path. Observable at the
> transaction boundary — one leg committed, other absent. No inter-node framing.
>
> **Class 3**: Node-A / node-B diverging state framing showing two nodes holding conflicting
> last-write values simultaneously. No single-transaction framing.
>
> Generic fills that satisfy either class without the class-specific structural signature fail.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`.
Class 3 row must apply a canonical label with adequacy judgment citing this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first. Then D-phase (per Role Declaration: D owns Recovery
Path, Verification Signal, Chaos Block).

Trigger Condition: quantified connectivity threshold + detection signal.
State: client isolation at failure onset.
Capability: offline-available commerce operations (named) + blocked operations.
Data at Risk: in-flight cart, pending payment intent, unsubmitted order records.
Status Quo Risk: **Step 1b, Class 1** (Rule B). Acute branches (cart dropped / cart stale)
then chronic framing.
Failure Signature: Class 1 — client view + server view. Not multi-node.
Severity / Blast Radius.

D-phase after all C-phase columns complete (per column-group gate):
Recovery Path: **Step 1d, Class 1** (Rule B — cite by label). Actor-chain ≥3 stages.
Named Verification Signal per stage.
Chaos Block: inject / expected behavior / pass signal / fail signal.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column
including all four Recovery Path stages with actor-chain mechanism, SLA citing Step 1d
Class 1 by label, and named Verification Signal — AND Row 1 Chaos Test Block is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first, then D-phase.

Failure Signature: **Class 2 — transaction-level anomaly** (single write path). Not
inter-node. Client view + server view + transaction boundary.
Trigger Condition, State, Capability, Data at Risk.
Status Quo Risk: **Step 1b, Class 2** (Rule B). Acute / chronic.

D-phase: Recovery Path **Step 1d, Class 2** (Rule B). Actor-chain. Named VS. Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete, including
Class 2 transaction-level Failure Signature and Recovery Path SLA citing Step 1d Class 2.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

Failure Signature: **Class 3 — node-A / node-B diverging state**. Not single-transaction.
Trigger Condition, State, Capability, Data at Risk.
Status Quo Risk: **Step 1b, Class 3** (Rule B). Acute: `last-write-wins` / `manual-reconcile`.
Chronic: duplicate-charge compound growth.
Conflict Resolution: canonical label + adequacy judgment.

D-phase: Recovery Path **Step 1d, Class 3** (Rule B). Actor-chain. Named VS. Chaos Block.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Block are complete,
including Failure Signature with Class 3 node-A/node-B framing, Conflict Resolution with
canonical label, and Recovery Path SLA citing Step 1d Class 3.**

---

### Gap Register

Three findings inline — no separate observability section:
**Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

HIGH / MEDIUM / LOW + strongest argument against deferral (2–3 sentences) naming gap
findings and Step 1b carrying costs.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3

---

## V-04 — Combined Axis: Lifecycle Emphasis + Synthesis

**Axis**: Two axes combined. (A) Lifecycle emphasis — Recovery Path stages are specified as
named per-stage sub-specifications (following V-05 R16's pattern), each stage as a discrete
named item with its own actor, mechanism, SLA reference, and Verification Signal slot.
(B) C-49+C-50 synthesis — the document enforcement preamble is positioned before all sub-parts
(C-49), and the per-stage Recovery Path specifications carry the explicit Rule B restatement
label at stage granularity (C-50's third independent location at stage-specification level).

**Hypothesis**: Per-stage named specifications create an additional enforcement anchor for
Rule B at a fine-grained structural level (stage sub-specification level) that is distinct
from preamble level, sub-part level, and column-contract level. The restatement label on
at least one stage sub-specification creates a fourth C-50 location, making the synthesis
robust across scoring interpretations. Combined with C-49's pre-sub-part preamble, all
forty-two criteria should pass.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic} across three structurally distinct failure classes. Produce a
complete four-field failure analysis per class, a Gap Register with inline observability,
and an Inertia Verdict.

Two roles fill all columns:
- **C — Commerce Expert**: #, Class, Trigger Condition, State, Capability, Data at Risk,
  Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D — Distributed Systems Expert**: Recovery Path, Verification Signal, Chaos Block

---

### Pre-Commitment Document: Resilience Commitment Matrix

**Document Enforcement Contract** (positioned before all sub-parts — read before filling
any of Steps 1a through 1d):

> This document pre-commits values that bind all scenario table fills. Two enforcement
> rules govern every sub-part:
>
> **Rule A — No Deferral**: Writing "TBD", leaving any cell blank, or using "N/A" or any
> equivalent unfilled value in any sub-part of this document is a named contract violation.
> The pre-commitment is void if any cell is deferred. Every cell must carry an actual value
> at the time this document is authored.
>
> **Rule B — No Per-Row Invention**: Each sub-part is the authoritative source for its
> corresponding scenario column. Independently authoring per-row values that are not drawn
> from the corresponding sub-part is a named contract violation. Row fills must cite the
> source sub-part by its label. A fill that introduces a value not present in the referenced
> sub-part is a contract violation regardless of whether the value is numerically plausible.
>
> Both rules apply to all sub-parts. Rule A closes the placeholder-deferral escape. Rule B
> closes the per-row reinvention escape.

---

**Step 1a — Domain Fragility Framing**

Write 2–3 sentences establishing why {topic} in commerce is inherently fragile across the
three failure classes. Specific to this domain — not generic distributed systems boilerplate.
Cover: client isolation creates invisible pending-state windows; idempotency gaps create
retry-duplication risk; concurrent partition writes create state divergence requiring
pre-specified merge rules.

**Step 1b — Per-Class Carrying Costs**

Status Quo Risk column fills reference this sub-part as "Step 1b, Class N".
**Rule A applies** — no blank cells. **Rule B applies** — independent per-row authoring
of carrying costs is a contract violation.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [named metric, e.g., cart-abandon events] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [named metric, e.g., oversell count] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [named metric, e.g., duplicate-charge events] | per-transaction | compound growth |

**Step 1c — Per-Class Tipping Point Signals**

**Rule A applies** — quantified threshold expression + named detection metric required.
"Worsens over time" is not quantified.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [e.g., "cart-abandon rate >2% above 30-day baseline / dashboard alert"] | [metric] |
| 2 | [e.g., "oversell count >50/month / inventory anomaly counter"] | [metric] |
| 3 | [e.g., "reconciliation backlog >200 items / queue-depth alert"] | [metric] |

**Step 1d — SLA Budget**

**Rule A applies** — no blank cells. All twelve cells must carry actual time values.
**Rule B applies** — Recovery Path per-stage SLA values must cite this sub-part as
"Step 1d, Class N, [stage] column". Independently authored SLA values per scenario row
are a contract violation under Rule B.

| Class | TTD (Detect) | TTC (Contain) | TTR (Recover) | TTV (Validate) |
|---|---|---|---|---|
| 1 — Connectivity loss | | | | |
| 2 — Partial failure | | | | |
| 3 — Split-brain | | | | |

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` — one table, no splits | Anti-split instruction (below) |
| Section | Phase gate — all rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | In-row bold performative inside Content descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary instruction** (all four escape routes closed simultaneously): Do not create
separate tables for Commerce Expert columns and Distributed Systems Expert columns. Do not
insert a horizontal rule, heading, or section break between rows when column ownership shifts.
Do not produce a standalone chaos section or standalone chaos-engineering table. Do not produce
a standalone observability section or standalone observability table. All four consolidation
escape routes are negated.

**Section Order Requirement**: (1) Pre-Commitment Document — all four sub-parts populated;
(2) Scenario Table — row N columns AND row N Chaos Test Block before row N+1 begins; (3) Gap
Register with three inline findings; (4) Inertia Verdict; (5) Finding Completeness Checklist.
**Do not advance to row N+1 until row N scenario columns AND Chaos Test Block are both
complete. Do not advance to the Gap Register until all three rows and all three Chaos Blocks
are complete.**

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1–3, continuous — one table, no splits |
| Class | C | Class 1 (Connectivity Loss), Class 2 (Partial Failure), or Class 3 (Split-Brain) |
| Trigger Condition | C | Two required components: quantified threshold expression + named detection signal. Qualitative only fails. |
| State | C | System configuration at failure onset — named components and states |
| Capability | C | Named commerce operations available during the failure. Generic descriptions fail. |
| Data at Risk | C | Specific named data fields, transaction records, or domain entities |
| Status Quo Risk | C | **Reference Step 1b, Class N (Rule B — not independently authored)**. Acute branches (A/B) before chronic metric. Three-component chronic: rate + horizon + metric. |
| Failure Signature | C | Behavioral fingerprint per actor during failure. ≥2 named actor viewpoints. Distinct from Trigger Condition (entry threshold) and from State (pre-failure config). Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | **Four named stage sub-specifications** (Detect / Contain / Recover / Validate). Per stage: actor-chain prefix + mechanism + SLA target (from Step 1d — **Rule B restated for co-location at column-contract level: any SLA value not drawn from Step 1d, Class N, stage column is a named contract violation**) + named Verification Signal. ≥3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage confirming stage completion. Observable and distinct from mechanism restatement. |
| Chaos Block | D | Four components co-located with this row: Inject (named reproducible condition) / Expected Behavior / Pass Signal / Fail Signal. |

#### Failure Signature Class Boundary Discriminator

> **Class 2 (Data Consistency Violation — Partial Failure)**: Fill uses transaction-level
> anomaly framing from a single write path. The inconsistency is observable at the transaction
> boundary — one leg committed, confirmation absent or other leg missing. Multi-node divergence
> framing (node-A / node-B) is incorrect for Class 2.
>
> **Class 3 (Split-Brain / Eventual Consistency)**: Fill uses node-A / node-B framing showing
> two nodes holding diverging last-write state simultaneously. Single-transaction framing is
> incorrect for Class 3.
>
> Generic "data inconsistency" fills satisfying either class without the class-specific
> structural signature fail this discriminator regardless of actor viewpoint count.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`.
Free-text paraphrase fails. Class 3 row must apply a canonical label with an adequacy
judgment citing this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first:

Trigger Condition: quantified connectivity loss threshold expression (e.g., "client TCP
connection attempt exceeds 30s timeout") + detection signal (e.g., "client-side connectivity
monitor registers ETIMEDOUT; server access log shows no incoming request").

State: client-side isolation at failure onset. Name {topic} components and services affected.

Capability: specific offline-available commerce operations (e.g., cached-catalog browse,
local cart editing). Name operations that are blocked (e.g., checkout submission, payment
processing, inventory confirmation).

Data at Risk: in-flight cart state, pending payment intent, unsubmitted order records —
named specifically.

Status Quo Risk: **Step 1b, Class 1 carrying cost** (Rule B — reference by sub-part label).
Acute branches: outcome A (cart silently dropped → immediate abandonment, no recovery
signal); outcome B (cart stale-restored → incorrect price or inventory at reconnection).
Chronic: carrying cost metric accumulates at rate qualifier without ceiling.

Failure Signature: **Class 1 framing** — client-view (connection timeout, no TCP reset,
no error message) + server-view (no request registered in access log, health probe returns
200, server unaware of client state). Not multi-node — Class 1 is client-isolation.

Severity / Blast Radius: all users attempting checkout during connectivity window.

**D-phase after all C-phase columns complete** (column-group gate):

Recovery Path — four named stage sub-specifications:
- **Detect** (TTD): actor-chain prefix + mechanism + **SLA from Step 1d, Class 1, TTD column** (Rule B — cite by label) + Verification Signal (named observable confirming detection complete)
- **Contain** (TTC): actor-chain prefix + mechanism + **SLA from Step 1d, Class 1, TTC column** + Verification Signal
- **Recover** (TTR): actor-chain prefix + mechanism + **SLA from Step 1d, Class 1, TTR column** + Verification Signal
- **Validate** (TTV): actor-chain prefix + mechanism + **SLA from Step 1d, Class 1, TTV column** + Verification Signal

Chaos Block: inject connectivity loss (e.g., block all outbound TCP from client), Expected
Behavior (offline mode activates, in-progress operations queued or surfaced with error),
Pass Signal (client enters offline mode, queued operations listed), Fail Signal (client
shows blank screen or crashes, no offline indicator).

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column —
including: Failure Signature with ≥2 named Class 1 actor viewpoints; Trigger Condition with
quantified threshold + detection signal; Status Quo Risk citing Step 1b Class 1 by label with
acute branches and three-component chronic; all four named Recovery Path stage sub-specifications
each with actor-chain mechanism, SLA from Step 1d Class 1 by label (Rule B), and named
Verification Signal — AND Row 1 Chaos Test Block is complete.**

---

#### Row 2 — Class 2: Partial Failure (Dependent Service Unavailable)

**Write this row now.** C-phase first:

Trigger Condition: quantified downstream-service degradation threshold (e.g., "payment API
p99 latency exceeds 500ms") + detection signal (e.g., "payment-provider timeout counter
increments past alert threshold in APM dashboard").

State: {topic} upstream service (e.g., inventory-reservation) available; downstream payment
service degraded or unreachable.

Capability: pre-checkout operations available (browse, cart); checkout submission blocked
or queued. Name the exact boundary.

Data at Risk: inventory reservation drift (items reserved but order unconfirmed), oversell
risk from unacknowledged holds, pending payment intents.

Status Quo Risk: **Step 1b, Class 2** (Rule B). Acute branches: outcome A (inventory hold
persists indefinitely → phantom reservation lock); outcome B (hold silently expires → oversell
on next reservation attempt). Chronic: oversell count accumulates per-deploy unbounded.

Failure Signature: **Class 2 framing — transaction-level anomaly from single write path**.
Client-view + server-view + transaction-boundary view. No node-A / node-B framing.

Severity / Blast Radius.

**D-phase after all C-phase columns complete:**

Recovery Path — four named stage sub-specifications:
- **Detect** (TTD): actor-chain prefix + mechanism (e.g., `server → circuit-breaker probe detects payment error rate threshold`) + **SLA from Step 1d, Class 2, TTD** (Rule B) + VS (e.g., "payment-provider error-rate dashboard alert fires")
- **Contain** (TTC): actor-chain + mechanism (e.g., `server → circuit-breaker opens, checkout returns 503 with retry-after`) + **SLA from Step 1d, Class 2, TTC** (Rule B) + VS (e.g., "circuit-breaker state = OPEN in service mesh dashboard")
- **Recover** (TTR): actor-chain + mechanism + **SLA from Step 1d, Class 2, TTR** (Rule B) + VS
- **Validate** (TTV): actor-chain + mechanism + **SLA from Step 1d, Class 2, TTV** (Rule B) + VS (e.g., "payment-service error rate below threshold for 5-minute window; circuit-breaker CLOSED")

Chaos Block: inject payment service degradation, Expected Behavior (circuit-breaker opens
within TTD; checkout fails gracefully with retry guidance), Pass Signal, Fail Signal.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete, including:
Failure Signature with Class 2 transaction-level framing (not inter-node — that fails the
Class Boundary Discriminator); all four named Recovery Path stage sub-specifications each
with actor-chain mechanism, SLA from Step 1d Class 2 by label (Rule B), and named
Verification Signal — AND Row 2 Chaos Test Block is complete.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first:

Trigger Condition: replication lag threshold (e.g., "replication lag between inventory-service
nodes exceeds 5s") + detection signal (e.g., "dual-write conflict counter increments in
monitoring dashboard").

State: network partition between inventory-service nodes; both nodes accepting independent
writes; no conflict detection active.

Capability: users on both partition sides can submit checkouts; conflict is invisible to
users; both sides report success.

Data at Risk: inventory count diverges across nodes; duplicate fulfillment orders possible;
double-charge risk on payment reconciliation.

Status Quo Risk: **Step 1b, Class 3** (Rule B). Acute branches: outcome A (`last-write-wins`
applied → earlier reservation silently lost, oversell for earlier buyer); outcome B
(`manual-reconcile` required → order processing halted, customer delay). Chronic:
duplicate-charge events compound per-transaction without ceiling.

Failure Signature: **Class 3 framing — node-A / node-B diverging state**. Node-A view +
node-B view (holding diverging last-write state) + observability view (no conflict event
during partition). Not single-transaction framing.

Conflict Resolution Strategy: `last-write-wins` or `manual-reconcile` — canonical label
required with adequacy judgment citing the vocabulary constraint.

Severity / Blast Radius.

**D-phase after all C-phase columns complete:**

Recovery Path — four named stage sub-specifications:
- **Detect** (TTD): actor-chain + mechanism + **SLA from Step 1d, Class 3, TTD** (Rule B) + VS (e.g., "dual-write conflict counter registers non-zero; replication-lag alert fires")
- **Contain** (TTC): actor-chain + mechanism + **SLA from Step 1d, Class 3, TTC** (Rule B) + VS (e.g., "minority-partition node shows write-suspended state in cluster dashboard")
- **Recover** (TTR): actor-chain + mechanism + **SLA from Step 1d, Class 3, TTR** (Rule B) + VS (e.g., "dual-write conflict counter returns to 0; both nodes report identical inventory count")
- **Validate** (TTV): actor-chain + mechanism + **SLA from Step 1d, Class 3, TTV** (Rule B) + VS (e.g., "conflict counter remains 0 for 60s sustained; fulfillment deduplication log shows 0 new duplicates")

Chaos Block: inject network partition between inventory-service nodes (e.g., iptables DROP
between node-A and node-B), Expected Behavior (partition detected within TTD; write quorum
applied; conflict-resolution activates within TTC), Pass Signal (conflict counter resets to 0
for 60s after partition heals; both nodes show identical inventory), Fail Signal (counter
remains non-zero after TTR; inventory count diverges beyond tolerance; duplicate fulfillment
orders present).

**Do not advance to the Gap Register until Row 3 columns AND Chaos Test Block are complete,
including: Failure Signature with Class 3 node-A / node-B framing (not single-transaction —
that fails the Class Boundary Discriminator); Conflict Resolution with canonical vocabulary
label and adequacy judgment; all four named Recovery Path stage sub-specifications each with
actor-chain mechanism, SLA from Step 1d Class 3 by label (Rule B), and named Verification
Signal — AND Row 3 Chaos Test Block is complete.**

---

### Gap Register

Required output section. Three findings — one per type. Inline with observability fields.
No separate observability section.

Per finding:
- **Finding Type**: [Offline Experience Gap | Data Consistency Violation | Missing Recovery Flow]
- **Description**: specific and actionable — name the specific {topic} operation, data record,
  or recovery flow that is missing. Generic statements fail.
- **Metric**: named system or business metric
- **Alert**: named alert condition and threshold
- **Owner**: responsible role or team — not "TBD"

Finding types present: ___ of 3

---

### Inertia Verdict

After completing all three Gap Register findings, synthesize:
- **Inertia threat level**: HIGH / MEDIUM / LOW
- **Strongest argument against deferral** (2–3 sentences): name the specific gap findings
  and the carrying-cost metric from Step 1b that continues to accumulate without intervention.
  State what becomes irreversible or compounding if action is deferred beyond the Step 1c
  tipping point.

---

### Finding Completeness Checklist

Required output section. Fill in all fields:
- [ ] Offline Experience Gap — present
- [ ] Data Consistency Violation — present
- [ ] Missing Recovery Flow — present
- Finding types present: ___ of 3

---

## V-05 — Full Synthesis: All Axes Combined

**Axis**: Full synthesis — C-49+C-50 synthesis, inertia framing (status quo as named
competitor), formal § enumeration register, expanded per-stage lifecycle specifications,
and role sequence with D-phase enforcement declared at document open. This variation
combines every axis explored in V-01 through V-04 plus V-04 (R16)'s inertia framing
prominence. The enforcement hierarchy spans five structural levels: document-header role
declaration → document enforcement preamble → sub-part 1d inline → column-contract entry
→ per-stage sub-specification. Four of these carry named Rule B content; at least one
carries an explicit "(restated for co-location)" label.

**Hypothesis**: Maximum structural redundancy and formal register across five hierarchy levels
makes every enforcement axis evaluable by an independent scorer path. Any four of the five
locations independently satisfy C-47/C-48/C-49 and C-50. The explicit restatement label
at two independent locations ensures C-50 passes even if one location is misread as
insufficient.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic}, treat inertia as the named competitor, and produce a complete failure
analysis that makes the cost of doing nothing measurable.

### Role Declaration and Enforcement Scope

Two roles fill all scenario columns.

**C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk,
Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy.

**D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block.
> **§ 0 — D-Phase Pre-Commitment Constraint**: The Recovery Path column SLA annotations must
> be drawn from the SLA Budget (§ 1d) of the Pre-Commitment Document below. Writing SLA
> values per scenario row without citing §1d is a named contract violation. This constraint
> governs D-phase fills across all scenario rows and is declared here at document scope so
> it is encountered before any sub-part fill instructions.

---

### Pre-Commitment Document: Resilience Commitment Matrix

**§ 1 — Enforcement Contract** (governing §§ 1a through 1d — read before filling any sub-part):

> **§ 1.1 — Placeholder Prohibition (Rule A)**: Writing "TBD", leaving any cell blank, or
> using "N/A" or any equivalent unfilled value in any sub-part is a named contract violation.
> Every cell must carry an actual value at the time this document is authored. The
> pre-commitment is void if any cell is deferred.
>
> **§ 1.2 — Per-Row Invention Prohibition (Rule B)**: Each sub-part is the sole authoritative
> source for its corresponding scenario column. Independently authoring per-row values that
> are not drawn from the corresponding sub-part is a named contract violation. Row fills must
> cite the source sub-part by label. A fill introducing any value not present in the referenced
> sub-part is a contract violation regardless of numerical plausibility.
>
> Both §§ 1.1 and 1.2 apply to all sub-parts. A document that satisfies one without the
> other fails this Enforcement Contract. (§ 0 above restates § 1.2 at document-header scope
> for D-phase advance notice.)

---

**§ 1a — Status Quo Competitor: The Cost of Inaction**

Name inertia — doing nothing — as the competitor being displaced. For {topic}, write 2–3
sentences establishing:
(1) what the current failure mode looks like without any resilience investment (hard errors,
    silent data loss, no recovery path);
(2) why inertia is the default choice (failures are invisible until they compound);
(3) what makes {topic}'s domain specifically fragile (connectivity isolation + idempotency
    gaps + partition conflict).

**§ 1b — Per-Class Carrying Costs**

The do-nothing cost per class. Status Quo Risk column references this sub-part as "§ 1b,
Class N". **§ 1.1 applies** — no blank cells. **§ 1.2 applies** — per-row independent
authoring of carrying costs is a contract violation.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [named metric, e.g., cart-abandon events] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [named metric, e.g., oversell count] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [named metric, e.g., duplicate-charge events] | per-transaction | compound growth |

**§ 1c — Per-Class Tipping Point Signals**

The observable threshold at which deferral becomes indefensible per class. **§ 1.1 applies**
— quantified threshold expression + named detection metric required. "Worsens over time"
is not quantified and fails § 1.1.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [e.g., "cart-abandon rate >2% above 30-day baseline / dashboard alert"] | [metric] |
| 2 | [e.g., "oversell count >50/month / inventory anomaly counter"] | [metric] |
| 3 | [e.g., "reconciliation backlog >200 items / queue-depth alert"] | [metric] |

**§ 1d — SLA Budget**

**§ 1.1 applies** — all twelve cells must carry actual time values. No blank cells. No "TBD".
**§ 1.2 applies** — Recovery Path SLA fills must cite "§ 1d, Class N, [stage] column"
as their source. Per-row independently authored SLA values are a contract violation under
§ 1.2. (§ 0 and § 1.2 are both in effect — this sub-part is the authoritative source for
all Recovery Path SLA annotations.)

| Class | TTD (Detect) | TTC (Contain) | TTR (Recover) | TTV (Validate) |
|---|---|---|---|---|
| 1 — Connectivity loss | | | | |
| 2 — Partial failure | | | | |
| 3 — Split-brain | | | | |

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` — one table, no splits | Anti-split instruction (below) |
| Section | Phase gate — all rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | In-row bold performative inside Content descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary instruction** (four escape routes closed simultaneously): Do not create
separate tables for Commerce Expert columns and Distributed Systems Expert columns. Do not
insert a horizontal rule, heading, or section break between rows when column ownership shifts.
Do not produce a standalone chaos section or standalone chaos-engineering table. Do not produce
a standalone observability section or standalone observability table. All four consolidation
escape routes are negated; satisfying any three without the fourth does not satisfy this
instruction.

**Section Order Requirement**: (1) Pre-Commitment Document — all sub-parts fully populated;
(2) Scenario Table — each row's scenario columns AND chaos block complete before the next row
begins; (3) Gap Register with three inline findings; (4) Inertia Verdict; (5) Finding
Completeness Checklist. **Do not advance to row N+1 until row N columns AND chaos block are
both complete. Do not advance to the Gap Register until all three rows and three chaos blocks
are complete.**

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1–3, continuous — one table, no splits |
| Class | C | Class 1 (Connectivity Loss), Class 2 (Partial Failure), or Class 3 (Split-Brain) |
| Trigger Condition | C | Quantified threshold expression + named detection signal. Qualitative description alone fails. |
| State | C | System configuration at failure onset — named components and states |
| Capability | C | Named commerce operations available during failure. "Some functions degraded" fails. |
| Data at Risk | C | Named data fields, transaction records, or domain entities at risk |
| Status Quo Risk | C | **Reference § 1b, Class N (§ 1.2 — not independently authored)**. Acute branches (A/B) before chronic metric. Three-component chronic: rate + horizon + metric. |
| Failure Signature | C | Behavioral fingerprint per actor during failure. ≥2 named actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | **Four named stage sub-specifications** (Detect / Contain / Recover / Validate). Per stage: actor-chain prefix (`client →`, `server →`, `operator →`, `user →`) + mechanism + **SLA from § 1d, Class N, stage column — § 1.2 restated for co-location at column-contract level: any SLA value not drawn from § 1d is a named contract violation against this pre-committed budget** + named Verification Signal. ≥3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage confirming stage completion. Observable (system state, log entry, metric value, API response code). Not a restatement of mechanism. |
| Chaos Block | D | Four components co-located with this row: Inject (named reproducible condition) / Expected Behavior / Pass Signal (observable confirming expected behavior) / Fail Signal (observable confirming expected behavior did NOT occur). |

#### Failure Signature Class Boundary Discriminator

> **Class 2 (Data Consistency Violation — Partial Failure)**: Fill requirement is
> transaction-level anomaly framing from a single write path. The inconsistency is observable
> at the transaction boundary — one leg committed, confirmation or other leg absent — without
> requiring multi-node state divergence. Actor viewpoints: client view + server view +
> transaction boundary view. Node-A / node-B framing is incorrect for Class 2.
>
> **Class 3 (Split-Brain / Eventual Consistency)**: Fill requirement is node-A / node-B
> framing showing two nodes holding diverging last-write state simultaneously. The split is
> visible across node boundaries. Actor viewpoints: node-A view + node-B view + observability
> view. Single-transaction framing is incorrect for Class 3.
>
> A Failure Signature that describes "data inconsistency" without the class-specific
> structural signature fails this discriminator regardless of actor viewpoint count.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`.
Free-text paraphrase fails. Class 3 row must apply a canonical label and include an adequacy
judgment explicitly referencing this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first. Then D-phase (§ 0 governs D-phase SLA fills).

Do-nothing scenario (§ 1a framing): cart silently dropped, user gets no recovery signal,
cost accumulates per-session without bound.

Trigger Condition: quantified connectivity threshold expression (e.g., "client TCP connection
attempt exceeds 30s timeout") + detection signal (e.g., "client-side connectivity monitor
registers ETIMEDOUT; server access log shows no incoming request").

State: client-side isolation at failure onset — name {topic} components affected.

Capability: specific offline-available commerce operations (e.g., cached-catalog browse,
local cart editing). Name what is blocked (e.g., checkout submission, payment processing,
inventory confirmation).

Data at Risk: in-flight cart state, pending payment intent, unsubmitted order records —
named specifically.

Status Quo Risk: **§ 1b, Class 1** (§ 1.2 — reference by label). Acute branches: outcome A
(cart silently dropped → immediate abandonment, no recovery signal); outcome B (cart
stale-restored → incorrect price or inventory at reconnection). Chronic: carrying cost metric
accumulates at rate qualifier without ceiling.

Failure Signature: **Class 1 framing** — client-view (connection timeout, no TCP reset, no
error message) + server-view (no request in access log, health probe returns 200, server
unaware of client state). Not multi-node — Class 1 is client-isolation, not partition.

Severity / Blast Radius: all users attempting checkout during connectivity window.

**D-phase after all C-phase columns complete** (column-group gate; § 0 applies):

Recovery Path — four named stage sub-specifications:
- **Detect** (TTD): actor-chain prefix + mechanism + **SLA from § 1d, Class 1, TTD column** (§ 1.2) + Verification Signal (named observable confirming detection)
- **Contain** (TTC): actor-chain prefix + mechanism + **SLA from § 1d, Class 1, TTC column** (§ 1.2) + Verification Signal
- **Recover** (TTR): actor-chain prefix + mechanism + **SLA from § 1d, Class 1, TTR column** (§ 1.2 restated for co-location at stage level: any TTR value not present in § 1d Class 1 is a contract violation) + Verification Signal
- **Validate** (TTV): actor-chain prefix + mechanism + **SLA from § 1d, Class 1, TTV column** (§ 1.2) + Verification Signal

Chaos Block: inject connectivity loss (e.g., block all outbound TCP), Expected Behavior
(offline mode activates, in-progress operations queued or surfaced with error), Pass Signal
(client enters offline mode, queued operations listed), Fail Signal (client shows blank screen
or crashes, no offline indicator).

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column —
including: Failure Signature with ≥2 named Class 1 actor viewpoints (client + server);
Trigger Condition with quantified threshold + detection signal; Status Quo Risk citing
§ 1b Class 1 by label with acute branches and three-component chronic; all four named
Recovery Path stage sub-specifications each with actor-chain mechanism, SLA from § 1d
Class 1 by label (§ 1.2), and named Verification Signal — AND Row 1 Chaos Test Block
(Inject / Expected Behavior / Pass Signal / Fail Signal) is complete.**

---

#### Row 2 — Class 2: Partial Failure (Dependent Service Unavailable)

**Write this row now.** C-phase first, then D-phase.

Do-nothing scenario: oversell accumulates silently per deploy; inventory drift is invisible
until a customer disputes a double-reservation; no circuit-breaker degrades the failure
gracefully.

Trigger Condition: quantified downstream-service degradation threshold (e.g., "payment API
p99 latency exceeds 500ms") + detection signal (e.g., "payment-provider timeout counter
increments past alert threshold in APM dashboard").

State: {topic} upstream service available; downstream payment service degraded or unreachable.

Capability: pre-checkout operations available (browse, add-to-cart); checkout submission
blocked or queued.

Data at Risk: inventory reservation drift (items reserved but order unconfirmed), oversell
risk from unacknowledged holds, pending payment intents.

Status Quo Risk: **§ 1b, Class 2** (§ 1.2). Acute branches: outcome A (inventory hold persists
indefinitely → phantom reservation lock); outcome B (hold silently expires → oversell on next
reservation attempt). Chronic: oversell count accumulates per-deploy unbounded.

Failure Signature: **Class 2 framing — transaction-level anomaly from single write path**.
Client-view (checkout spinner, no error surfaced) + server-view (inventory write committed,
payment service returning 503, inventory health probe healthy) + transaction-boundary view
(reservation record exists, order record absent). **No node-A / node-B framing.**

Severity / Blast Radius.

**D-phase after all C-phase columns complete:**

Recovery Path — four named stage sub-specifications:
- **Detect** (TTD): `server →` circuit-breaker probe detects payment error rate threshold exceeded + **SLA from § 1d, Class 2, TTD** (§ 1.2) + VS (e.g., "payment error-rate dashboard alert fires; on-call notification sent")
- **Contain** (TTC): `server →` circuit-breaker opens; checkout requests return 503 with retry-after + **SLA from § 1d, Class 2, TTC** (§ 1.2) + VS (e.g., "circuit-breaker state = OPEN in service mesh dashboard")
- **Recover** (TTR): actor-chain + mechanism + **SLA from § 1d, Class 2, TTR** (§ 1.2) + VS
- **Validate** (TTV): actor-chain + mechanism + **SLA from § 1d, Class 2, TTV** (§ 1.2) + VS (e.g., "payment error rate below threshold for 5-minute window; circuit-breaker transitions to CLOSED")

Chaos Block: inject payment service degradation (e.g., add 2s latency to payment API),
Expected Behavior (circuit-breaker opens within TTD; checkout returns 503 with retry
guidance), Pass Signal (circuit-breaker state = OPEN; customer sees retry message), Fail
Signal (checkout returns 500 with no guidance; circuit-breaker remains CLOSED; holds
accumulate silently).

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete, including:
Failure Signature with Class 2 transaction-level framing (not inter-node — that fails the
Class Boundary Discriminator); all four named Recovery Path stage sub-specifications each
with actor-chain mechanism, SLA from § 1d Class 2 by label (§ 1.2), and named Verification
Signal — AND Row 2 Chaos Test Block is complete.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

Do-nothing scenario: duplicate charges compound per transaction; reconciliation backlog grows
indefinitely; the damage is invisible until two orders arrive at the warehouse for the same
inventory unit.

Trigger Condition: replication lag threshold (e.g., "replication lag between inventory nodes
exceeds 5s") + detection signal (e.g., "dual-write conflict counter increments in monitoring
dashboard; replication-lag alert fires").

State: network partition between inventory-service nodes; both nodes accepting independent
writes; conflict detection not yet active.

Capability: users on both partition sides can submit checkouts; conflict is invisible; both
sides report success.

Data at Risk: inventory count diverges across nodes; duplicate fulfillment orders possible;
double-charge risk on payment reconciliation.

Status Quo Risk: **§ 1b, Class 3** (§ 1.2). Acute branches: outcome A (`last-write-wins`
applied → earlier reservation silently lost, oversell for earlier buyer); outcome B
(`manual-reconcile` required → order processing halted, customer delay, operations
intervention). Chronic: duplicate-charge events compound per-transaction without ceiling.

Failure Signature: **Class 3 framing — node-A / node-B diverging state**. Node-A view +
node-B view (holding diverging last-write inventory count) + observability view (no conflict
event logged during partition; divergence surfaces only at healing). Not single-transaction
framing.

Conflict Resolution Strategy: `last-write-wins` or `manual-reconcile` — canonical label
with adequacy judgment explicitly citing the vocabulary constraint.

Severity / Blast Radius.

**D-phase after all C-phase columns complete:**

Recovery Path — four named stage sub-specifications:
- **Detect** (TTD): `server →` partition-detection mechanism identifies replication-lag threshold exceeded + **SLA from § 1d, Class 3, TTD** (§ 1.2) + VS (e.g., "dual-write conflict counter registers non-zero; replication-lag alert fires to on-call")
- **Contain** (TTC): `server →` write quorum suspended on minority partition side + **SLA from § 1d, Class 3, TTC** (§ 1.2) + VS (e.g., "minority-partition node shows write-suspended state in cluster dashboard")
- **Recover** (TTR): `operator →` conflict-resolution strategy applied; partition healing initiated + **SLA from § 1d, Class 3, TTR** (§ 1.2) + VS (e.g., "conflict counter returns to 0; both nodes report identical inventory count")
- **Validate** (TTV): `operator →` reconciliation audit confirms no duplicate fulfillment; inventory count matches post-resolution expectation + **SLA from § 1d, Class 3, TTV** (§ 1.2) + VS (e.g., "conflict counter remains 0 for 60s sustained; fulfillment deduplication log shows 0 new duplicates")

Chaos Block: inject network partition between inventory-service nodes (e.g., iptables DROP
between node-A and node-B), Expected Behavior (partition detected within TTD; write quorum
applied; conflict-resolution activates within TTC), Pass Signal (conflict counter resets to 0
for 60s after healing; both nodes show identical inventory), Fail Signal (counter remains
non-zero after TTR; inventory diverges beyond tolerance; duplicate fulfillment orders present).

**Do not advance to the Gap Register until Row 3 columns AND Chaos Test Block are complete,
including: Failure Signature with Class 3 node-A / node-B framing (not single-transaction —
that fails the Class Boundary Discriminator); Conflict Resolution with canonical label and
adequacy judgment; all four named Recovery Path stage sub-specifications each with actor-chain
mechanism, SLA from § 1d Class 3 by label (§ 1.2), and named Verification Signal — AND Row 3
Chaos Test Block is complete.**

---

### Gap Register

Required output section. Three findings — one per type. Inline with observability fields.
No separate observability section, no standalone observability table.

Per finding format:
- **Finding Type**: [Offline Experience Gap | Data Consistency Violation | Missing Recovery Flow]
- **Description**: specific and actionable — name the specific {topic} operation, data record,
  or recovery flow that is missing. Generic statements ("offline support may be limited") fail.
- **Metric**: named system or business metric to monitor for this finding
- **Alert**: named alert condition and threshold that fires when the metric crosses the
  actionable threshold
- **Owner**: responsible role or team — not "TBD" or "the engineering team"

Finding types present: ___ of 3

---

### Inertia Verdict

After completing all three Gap Register findings, synthesize:
- **Inertia threat level**: HIGH / MEDIUM / LOW
- **Strongest argument against deferral** (2–3 sentences): name the specific gap findings,
  reference the carrying-cost metric from § 1b that continues to accumulate without
  intervention, and state what becomes irreversible or compounding if action is deferred
  beyond the § 1c tipping point. Name the do-nothing scenario from § 1a as the baseline
  being compared against.

---

### Finding Completeness Checklist

Required output section. Model fills in:
- [ ] Offline Experience Gap — present
- [ ] Data Consistency Violation — present
- [ ] Missing Recovery Flow — present
- Finding types present: ___ of 3
