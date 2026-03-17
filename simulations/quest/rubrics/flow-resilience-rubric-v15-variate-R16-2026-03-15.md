# flow-resilience — Round 16 Variations (Rubric v15)

**Rubric**: v15 · 38 aspirational criteria · Ceiling entering R16: 37/38 → 99.74 (R15 V-05)
**Open criterion entering R16**: **C-45 only** — SLA Budget Placeholder Negation and Per-Row
Invention Prohibition. Both mechanisms must be present: (1) explicit "TBD fails" statement
making every cell in the class × stage matrix non-bypassable; (2) explicit naming of per-row
SLA invention as a contract violation.
**R15 V-05 deficit**: contract-violation language present; TBD placeholder negation absent.
**R16 objective**: All five variations carry the full R15 V-05 ceiling (37/38) and add C-45
using distinct structural placements and register choices. The 100.00 ceiling is achievable.

| Variation | Axis | Hypothesis | C-45 Placement |
|---|---|---|---|
| V-01 | C-45 TBD-negation placement (single-axis) | TBD-negation sentence at sub-part 1d header + existing invention prohibition satisfies C-45 | 1d header sentence + Column Contract |
| V-02 | C-45 enforcement blockquote (output format axis) | Both C-45 mechanisms co-located in a single blockquote inside sub-part 1d | Dedicated blockquote in sub-part 1d |
| V-03 | C-45 formal register with numbered enforcement clauses (phrasing register axis) | Numbered enforcement clauses make both mechanisms maximally unambiguous | Numbered clauses in sub-part 1d |
| V-04 | C-45 + inertia framing prominence (inertia framing + C-45 combined) | Document-level enforcement header covering both pre-commitment axes (carrying cost + SLA) | Document preamble enforcement block |
| V-05 | Full synthesis — all axes | TBD negation + invention prohibition in three locations simultaneously | sub-part 1d + Column Contract + row descriptors |

---

## V-01 — Single-Axis: TBD Negation Placement

**Axis**: C-45 only. The sole structural change from R15 V-05 is the addition of an explicit
TBD negation sentence at the top of sub-part 1d (before the SLA matrix). The invention
prohibition was already present in R15 V-05 as "Per-row SLA invention is a contract
violation." This variation isolates whether the TBD negation sentence alone closes the
remaining gap.

**Hypothesis**: Adding one sentence — "Writing 'TBD', leaving any cell blank, or using any
equivalent placeholder in this matrix fails the SLA Budget requirement; the pre-commitment is
void if any cell is deferred" — immediately before the class × stage matrix satisfies C-45's
first mechanism. The existing invention-prohibition language satisfies C-45's second mechanism.
Together, both are present, satisfying C-45 and reaching 38/38.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic} across three structurally distinct failure classes. Produce the full
four-field failure analysis per class, identify gaps, and assess inertia threat level.

Two specialist roles fill all columns:
- **C — Commerce Expert**: owns #, Class, Trigger Condition, State, Capability, Data at Risk,
  Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D — Distributed Systems Expert**: owns Recovery Path, Verification Signal, Chaos Block

---

### Pre-Commitment Document: Resilience Commitment Matrix

Complete all four sub-parts before writing any scenario table row. The scenario table draws
values from sub-parts 1b, 1c, and 1d — per-row independent authoring of values established
here is a contract violation.

**Step 1a — Domain Fragility Framing**

Write 2–3 sentences specific to {topic} establishing why the commerce domain is inherently
fragile across all three classes: (1) client isolation creates invisible pending-state windows
where in-flight transactions have no delivery confirmation; (2) distributed writes without
idempotency produce duplicate side effects on retry; (3) concurrent node operation during
partition produces state divergence requiring pre-specified business-level merge rules.

**Step 1b — Per-Class Carrying Costs**

Pre-commit the accumulation metric, rate, and horizon for each class. All three components
required per class. Status Quo Risk column fills must draw from this sub-part — do not author
per-row values independently.

| Class | Failure | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [commerce metric, e.g., cart-abandon events] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [commerce metric, e.g., oversell count] | per-deploy | unbounded |
| 3 — Split-brain | Eventual inconsistency | [commerce metric, e.g., duplicate-charge events] | per-transaction | compound growth |

Fill all three rows before advancing to Step 1c. Row descriptors reference this sub-part as
"Step 1b, Class N carrying cost" — reference by sub-part label, not section name alone.

**Step 1c — Per-Class Tipping Point Signals**

For each class, the observable threshold at which deferral becomes indefensible. Each must
include a quantified threshold expression AND a named metric being monitored. "Worsens over
time" is not a quantified threshold — it fails.

| Class | Tipping Point Signal (quantified threshold + detection signal) | Metric Monitored |
|---|---|---|
| 1 | e.g., "cart-abandon rate rises >2% above 30-day baseline / detected via abandonment-rate dashboard alert" | session abandonment rate |
| 2 | e.g., "oversell-event count exceeds 50/month / detected via inventory-service anomaly counter" | inventory oversell counter |
| 3 | e.g., "reconciliation backlog exceeds 200 open items / detected via reconciliation-queue depth alert" | reconciliation backlog depth |

Row descriptors reference this sub-part as "Step 1c, Class N tipping point."

**Step 1d — SLA Budget**

Writing "TBD", leaving any cell blank, or using any equivalent placeholder fails the SLA
Budget requirement — the pre-commitment is void if any cell is deferred. Fill every cell.

| Class | TTD (Detect) | TTC (Contain) | TTR (Recover) | TTV (Validate) |
|---|---|---|---|---|
| 1 — Connectivity loss | | | | |
| 2 — Partial failure | | | | |
| 3 — Split-brain | | | | |

Recovery Path SLA fills must reference this table by class row and stage column. Per-row SLA
invention is a contract violation against this pre-committed budget.

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` — one table, no splits | Anti-split instruction (below) |
| Section | Phase gate — all rows + chaos blocks complete before Gap Register | Section Order Requirement (below) |
| Slot | In-row bold imperative co-located inside Content descriptor | Row Descriptors (below) |
| Column-group | C-phase columns complete before D-phase columns within the same row | Column-group gate in each Row Descriptor |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary instruction** (all four escape routes closed simultaneously): Do not create
separate tables for Commerce Expert columns and Distributed Systems Expert columns. Do not
insert a horizontal rule, heading, or section break between rows when column ownership shifts.
Do not produce a standalone chaos section or standalone chaos-engineering table. Do not produce
a standalone observability section or standalone observability table — observability fields
appear inline with each Gap Register finding.

**Section Order Requirement**: (1) Step 1 Pre-Commitment Document complete; (2) Scenario
Table — all three rows, each row's Chaos Test Block complete before advancing to the next row;
(3) Gap Register — all three findings; (4) Inertia Verdict; (5) Finding Completeness Checklist.
**Do not begin any row until the previous row's scenario columns AND Chaos Test Block are
both complete. Do not begin the Gap Register until all three rows and all three Chaos Test
Blocks are complete.**

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer row index 1–3, continuous across all scenario classes |
| Class | C | Class 1 (Connectivity Loss), Class 2 (Partial Failure), or Class 3 (Split-Brain) |
| Trigger Condition | C | Two components required: (1) threshold expression — quantified condition activating the scenario; (2) detection signal — named observable mechanism by which the system identifies the threshold crossing. Qualitative descriptions without a threshold expression fail. |
| State | C | System configuration at failure onset — what state are the components in when the failure begins |
| Capability | C | What the user can still do during the failure. Named commerce operations only — generic "some functions degraded" fails. |
| Data at Risk | C | What specific data may be lost, stale, or inconsistent. Named fields or transaction records only. |
| Status Quo Risk | C | Chronic carrying cost. **Reference Step 1b, Class N carrying cost — do not author a new value per row.** At least one row must include acute consequence branches (outcome A / outcome B) positioned before the chronic metric. Three-component chronic framing required: rate + horizon + metric. |
| Failure Signature | C | Observable behavioral fingerprint per actor during the failure — distinct from Trigger Condition (which bounds entry threshold) and from State (which captures pre-failure configuration). Name at least two distinct actor viewpoints and describe what each observes while the failure is in progress. See Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius estimate or qualifier |
| Conflict Resolution Strategy | C | Canonical vocabulary only: `last-write-wins`, `merge`, `manual-reconcile`, or `reject-stale`. Free-text paraphrase ("the newest write wins") fails — canonical label required. |
| Recovery Path | D | Four stages: **Detect (TTD) → Contain (TTC) → Recover (TTR) → Validate (TTV)**. Per stage: actor-chain prefix (`client →`, `server →`, `operator →`, `user →`) + mechanism + **SLA target from Step 1d, class row, stage column — reference by sub-part label, not independently authored** + named Verification Signal. At least 3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per recovery stage confirming stage completion. Observable (system state, log entry, metric value, API response code) and distinct from a restatement of the mechanism. |
| Chaos Block | D | Four components co-located with this row: (1) Inject — named reproducible failure condition; (2) Expected Behavior; (3) Pass Signal — observable artifact confirming expected behavior; (4) Fail Signal — observable artifact confirming expected behavior did not occur. |

#### Failure Signature Class Boundary Discriminator

> **Class 2 (Data Consistency Violation — Partial Failure)**: Failure Signature must use
> transaction-level anomaly framing from a single write path. The inconsistency is observable
> at the transaction boundary — for example, a write completes to the inventory-reservation
> service but the confirmation ACK is absent, or a read returns a stale value immediately
> after a write to the same node. Multi-node state divergence framing (node-A / node-B) is
> incorrect for Class 2 — it collapses the operational distinction.
>
> **Class 3 (Split-Brain / Eventual Consistency)**: Failure Signature must use node-A /
> node-B framing showing two nodes holding diverging state simultaneously. The split is
> visible across node boundaries — node-A holds one last-write state, node-B holds a
> conflicting last-write state, and the observability layer shows no conflict event until
> partition heals. Single-transaction framing is incorrect for Class 3 — it collapses the
> operational distinction.
>
> Generic "data inconsistency" descriptions that could satisfy either class without
> distinguishing their operational signatures fail this discriminator even if they name
> multiple actor viewpoints.

#### Conflict Resolution Vocabulary Constraint

Canonical terms: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`.
Free-text paraphrases do not satisfy this constraint. The canonical label must appear as a
discrete term in the Conflict Resolution Strategy cell. At least one row descriptor must apply
a canonical label and include an adequacy judgment referencing this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** Anchor to a specific {topic} commerce operation (e.g., checkout
submission, inventory browse, order status polling). C-phase first:

Trigger Condition: threshold expression (e.g., "client TCP connection attempt exceeds 30s
timeout") + detection signal (e.g., "client-side connectivity monitor registers ETIMEDOUT;
server access log shows no incoming request").

State: describe client-side connectivity state at failure onset.

Capability: list specific commerce operations still available offline (e.g., cached-catalog
browse, local cart editing). Name what is blocked.

Data at Risk: in-flight cart state, pending payment intent, unsubmitted order — specific
named fields.

Status Quo Risk: **Step 1b, Class 1 carrying cost** (rate + horizon + metric). Acute branches
before chronic: outcome A (cart silently dropped → immediate abandonment); outcome B (cart
state stale-restored → incorrect price/inventory at re-connection). Chronic: metric accumulates
at rate, horizon qualifier.

Failure Signature: Class 1 actor framing — client-view (e.g., connection timeout, no TCP
reset) + server-view (e.g., no request registered in access log, health probe returns 200).
Not multi-node framing.

Severity / Blast Radius: all users attempting checkout during connectivity window.

D-phase after C-phase is complete — column-group gate enforced:
Recovery Path four stages with TTD/TTC/TTR/TTV from **Step 1d, Class 1 row**. Actor-chain
prefixes on at least 3 stages. Named Verification Signal per stage.
Chaos Block: inject connectivity loss (e.g., iptables DROP outbound), Expected Behavior,
Pass Signal, Fail Signal.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column
including: Failure Signature with ≥2 named actor viewpoints (Class 1 framing), all four
Recovery Path stages each with actor-chain mechanism, SLA target citing Step 1d Class 1,
and named Verification Signal — AND the Row 1 Chaos Test Block (Inject / Expected Behavior /
Pass Signal / Fail Signal) is complete.**

---

#### Row 2 — Class 2: Partial Failure (Dependent Service Unavailable)

**Write this row now.** C-phase first:

Trigger Condition: threshold expression (e.g., "payment API p99 latency exceeds 500ms") +
detection signal (e.g., "payment-provider timeout counter increments past alert threshold in
APM dashboard").

State: upstream commerce service (inventory reservation) available; downstream payment service
degraded or unreachable.

Capability: browse, add-to-cart available; checkout submission blocked or queued.

Data at Risk: inventory reservation drift — items reserved but order not confirmed; oversell
risk on unacknowledged holds.

Status Quo Risk: **Step 1b, Class 2 carrying cost**. Acute branches: outcome A (reservation
holds indefinitely → phantom inventory lock); outcome B (reservation silently drops → oversell
on next request). Chronic: oversell count accumulates per-deploy unbounded.

Failure Signature: **Class 2 framing — transaction-level anomaly from single write path**:
e.g., "client view: checkout spinner indefinitely, no error displayed; server view: payment
service returning 503, inventory-reservation service healthy; transaction boundary: write to
inventory-reservation committed but payment ACK absent." No node-A / node-B framing.

Severity / Blast Radius: all users attempting checkout while payment service is degraded.

D-phase:
Recovery Path four stages with TTD/TTC/TTR/TTV from **Step 1d, Class 2 row**. Actor-chain
prefixes. Named Verification Signal per stage (e.g., Detect VS: "payment-provider error rate
dashboard crosses alert threshold"; Contain VS: "circuit-breaker state changes to OPEN").
Chaos Block: inject payment service degradation, Expected Behavior (circuit breaker opens,
checkout fails gracefully), Pass Signal, Fail Signal.

**Do not advance to Row 3 until Row 2 contains non-placeholder content in every column
including: Failure Signature with Class 2 transaction-level framing (not inter-node framing),
all four Recovery Path stages each with actor-chain mechanism, SLA target citing Step 1d
Class 2, and named Verification Signal — AND Row 2 Chaos Test Block is complete.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first:

Trigger Condition: threshold expression (e.g., "replication lag between inventory nodes
exceeds 5s") + detection signal (e.g., "dual-write conflict counter increments in monitoring
dashboard").

State: network partition between inventory-service nodes; both nodes accepting writes
independently; no conflict detection active.

Capability: users on both partition sides can submit checkouts; conflict invisible until
partition heals.

Data at Risk: inventory count diverges across nodes; duplicate fulfillment orders possible;
payment double-charge risk.

Status Quo Risk: **Step 1b, Class 3 carrying cost**. Acute branches before chronic: outcome
A (last-write-wins applied → earlier reservation lost, oversell) — canonical resolution:
`last-write-wins`; outcome B (merge attempted → manual-reconcile required, order delay) —
canonical resolution: `manual-reconcile`. Chronic: duplicate-charge events compound
per-transaction without ceiling.

Failure Signature: **Class 3 framing — node-A / node-B diverging state**: e.g., "node-A
view: holds last-write inventory count reduced by checkout-A; node-B view: holds last-write
inventory count reduced by checkout-B (diverging from node-A); observability view: no conflict
event logged, both checkouts show success until partition heals." Not single-transaction
framing.

Conflict Resolution Strategy: `last-write-wins` (if recency wins) or `manual-reconcile` (if
business rules require human arbitration) — canonical label required with adequacy judgment.

Severity / Blast Radius: users distributed across partition segments during partition window.

D-phase:
Recovery Path four stages with TTD/TTC/TTR/TTV from **Step 1d, Class 3 row**. Actor-chain
prefixes. Named Verification Signal per stage (e.g., Validate VS: "dual-write conflict counter
resets to 0 for 60s, both nodes report identical inventory count").
Chaos Block: inject network partition between inventory nodes, Expected Behavior (partition
detection + quorum decision), Pass Signal (conflict counter resets to 0 for 60s), Fail Signal
(counter remains non-zero after TTR elapsed).

**Do not advance to the Gap Register until Row 3 columns AND Chaos Test Block are complete,
including: Failure Signature with Class 3 node-A/node-B framing, Conflict Resolution
Strategy using a canonical vocabulary label with adequacy judgment, Recovery Path SLA targets
citing Step 1d Class 3 row, and all four stages with actor-chain mechanism and named VS.**

---

### Gap Register

Required output section. Three findings required — one per type. Findings appear inline —
no separate observability section.

Per finding:
- **Finding Type**: [Offline Experience Gap | Data Consistency Violation | Missing Recovery Flow]
- **Description**: specific and actionable (not generic)
- **Metric**: named system or business metric to monitor
- **Alert**: named alert condition and threshold that fires when metric crosses threshold
- **Owner**: responsible role or team (not "TBD")

Finding types present: ___ of 3

---

### Inertia Verdict

After completing the Gap Register, synthesize gap findings + pre-committed carrying costs
from Steps 1b and 1c into:
- Inertia threat level: HIGH / MEDIUM / LOW
- Single strongest argument against deferral (2–3 sentences), naming the gap findings and
  the carrying-cost metric from Step 1b that continues to accumulate without intervention.

---

### Finding Completeness Checklist

Required output section. Model fills in:
- [ ] Offline Experience Gap — present
- [ ] Data Consistency Violation — present
- [ ] Missing Recovery Flow — present
- Finding types present: ___ of 3

---

## V-02 — Output Format Axis: Enforcement Blockquote

**Axis**: Both C-45 mechanisms are co-located in a single dedicated enforcement blockquote
inside sub-part 1d, rather than distributed across sub-part 1d header and Column Contract.
The blockquote makes both mechanisms a single structural element that is impossible to
satisfy one without the other.

**Hypothesis**: Co-locating the TBD negation and the invention prohibition in one named
structural element (blockquote) ensures both are read simultaneously and evaluated as a
unified enforcement contract. Distributing them across two locations (as in V-01) risks one
mechanism being scored as primary and the other as incidental. Single blockquote = single
pass/fail verdict covering both.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic} across three structurally distinct failure classes. Produce the full
four-field failure analysis, identify gaps, and assess inertia threat level.

Two roles fill all columns:
- **C — Commerce Expert**: #, Class, Trigger Condition, State, Capability, Data at Risk,
  Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D — Distributed Systems Expert**: Recovery Path, Verification Signal, Chaos Block

---

### Pre-Commitment Document: Resilience Commitment Matrix

Complete all four sub-parts before writing any scenario row.

**Step 1a — Domain Fragility Framing**

Write 2–3 sentences establishing why {topic} in commerce is inherently fragile across the
three failure classes, specific to this domain (not generic distributed systems boilerplate).

**Step 1b — Per-Class Carrying Costs**

Status Quo Risk column fills must reference this sub-part by label ("Step 1b, Class N").

| Class | Failure Mode | Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [named metric] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [named metric] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [named metric] | per-transaction | compound growth |

**Step 1c — Per-Class Tipping Point Signals**

Quantified threshold + named metric for each class. "Worsens over time" is not quantified.

| Class | Tipping Point (threshold expression + detection signal) | Metric |
|---|---|---|
| 1 | [quantified expression + detection signal] | [metric] |
| 2 | [quantified expression + detection signal] | [metric] |
| 3 | [quantified expression + detection signal] | [metric] |

**Step 1d — SLA Budget**

Fill the matrix. Then read the enforcement block below before proceeding.

| Class | TTD | TTC | TTR | TTV |
|---|---|---|---|---|
| 1 — Connectivity loss | | | | |
| 2 — Partial failure | | | | |
| 3 — Split-brain | | | | |

> **SLA Budget Enforcement**
>
> (1) **Placeholder Negation**: Writing "TBD", leaving any cell blank, or using any
> equivalent unfilled value in the matrix above fails the SLA Budget requirement. The
> pre-commitment is void if any cell is deferred — every cell must carry an actual time
> value at the point this document is authored.
>
> (2) **Per-Row Invention Prohibition**: Independently authoring SLA target values per
> scenario row is a named contract violation against this pre-committed budget. Recovery
> Path SLA annotations must reference this matrix by "Step 1d, Class N, stage column" —
> they must not introduce new values. A Recovery Path fill that carries SLA targets not
> present in this matrix fails the pre-commitment contract.

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` — one table, no splits | Anti-split instruction (below) |
| Section | Phase gate — all rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | In-row bold imperative inside Content descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary instruction**: Do not create separate tables for Commerce Expert columns and
Distributed Systems Expert columns. Do not insert a horizontal rule, heading, or section break
between rows when column ownership shifts. Do not produce a standalone chaos section or
standalone chaos-engineering table. Do not produce a standalone observability section or
standalone observability table — all four consolidation escape routes are closed simultaneously.

**Section Order Requirement**: (1) Pre-Commitment Document fully populated; (2) Scenario
Table — each row's columns AND chaos block complete before advancing to the next row;
(3) Gap Register with three inline findings; (4) Inertia Verdict; (5) Finding Completeness
Checklist. **Do not advance to any row N+1 until row N scenario columns AND Chaos Test Block
are both complete. Do not begin the Gap Register until all three rows and chaos blocks are
complete.**

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1–3, continuous |
| Class | C | Class 1, 2, or 3 |
| Trigger Condition | C | Threshold expression (quantified) + detection signal (observable). Qualitative only fails. |
| State | C | System configuration at failure onset |
| Capability | C | Named commerce operations available during failure |
| Data at Risk | C | Specific named data fields or transaction records at risk |
| Status Quo Risk | C | Reference **Step 1b, Class N** for carrying cost. Acute branches (outcome A / outcome B) before chronic metric. Three-component chronic framing: rate + horizon + metric. |
| Failure Signature | C | Observable behavioral fingerprint per actor during failure. Distinct from Trigger Condition and State. ≥2 named actor viewpoints. See Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label + blast-radius qualifier |
| Conflict Resolution Strategy | C | Canonical vocabulary only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale` |
| Recovery Path | D | Detect (TTD) → Contain (TTC) → Recover (TTR) → Validate (TTV). Each stage: actor-chain prefix (`client →`, `server →`, `operator →`, `user →`) + mechanism + **SLA target from Step 1d, Class N row, stage column — do not author independently** + named Verification Signal. |
| Verification Signal | D | Named observable artifact per stage, distinct from mechanism |
| Chaos Block | D | Inject / Expected Behavior / Pass Signal / Fail Signal — co-located with this row |

#### Failure Signature Class Boundary Discriminator

> **Class 2 fill requirement**: transaction-level anomaly from a single write path. The
> inconsistency is observable at the transaction boundary without multi-node state divergence.
> Example: "client view: no ACK received after checkout submission; server view: inventory
> write committed, payment service returned 503; transaction boundary: partial completion —
> reservation exists, order does not."
>
> **Class 3 fill requirement**: node-A / node-B framing showing two nodes holding diverging
> state simultaneously. Example: "node-A view: inventory count = 47 (checkout-A applied);
> node-B view: inventory count = 47 (checkout-B applied, diverging); observability: no
> conflict event logged until partition heals."
>
> A description that satisfies either class without the class-specific framing fails this
> discriminator regardless of actor-viewpoint count.

#### Conflict Resolution Vocabulary Constraint

Canonical terms: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text
paraphrase fails. Class 3 row must apply a canonical label with an adequacy judgment citing
this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first (Failure Signature first in C-phase — write what each
actor observes before writing Trigger Condition or State):

Failure Signature (Class 1): client-view + server-view actor framing. Client observes timeout
or connection refused; server observes no incoming request while its own health probe is
healthy. Not multi-node framing.

Trigger Condition: quantified connectivity threshold + detection signal.
State: client-side isolation at failure onset.
Capability: offline commerce operations available (named). What is blocked.
Data at Risk: in-flight cart, pending payment intent, unsubmitted order records.
Status Quo Risk: Step 1b Class 1 carrying cost. Acute branches (cart dropped / cart stale)
then chronic framing (rate + horizon + metric).
Severity / Blast Radius.

D-phase after C-phase complete:
Recovery Path: TTD/TTC/TTR/TTV from **Step 1d, Class 1 row**. Actor-chain prefixes.
Named Verification Signal per stage.
Chaos Block: inject, expected behavior, pass signal, fail signal.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column —
Failure Signature with Class 1 actor framing (≥2 viewpoints), Trigger Condition with
threshold + detection signal, Status Quo Risk citing Step 1b Class 1 by sub-part label,
Recovery Path SLA targets citing Step 1d Class 1, all four stages with actor-chain mechanism
and named Verification Signal — AND Row 1 Chaos Test Block is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first (Failure Signature first in C-phase):

Failure Signature (Class 2): **transaction-level anomaly framing** — single write path
inconsistency. Client view (checkout spinner or error) + server view (upstream service
healthy, downstream payment degraded) + transaction boundary (what committed, what did not).
No node-A / node-B framing — that collapses Class 2 into Class 3.

Trigger Condition: payment API latency threshold expression + APM alert detection signal.
State: upstream service available, downstream service degraded.
Capability: pre-checkout operations available; checkout submission blocked.
Data at Risk: inventory reservation holds, unconfirmed orders, oversell risk.
Status Quo Risk: Step 1b Class 2. Acute branches (phantom reservation hold / silent drop +
oversell). Chronic: oversell count per-deploy unbounded.
Severity / Blast Radius.

D-phase:
Recovery Path: TTD/TTC/TTR/TTV from **Step 1d, Class 2 row**. Actor-chain prefixes.
Named Verification Signal per stage.
Chaos Block.

**Do not advance to Row 3 until Row 2 contains non-placeholder content in every column —
Failure Signature with Class 2 transaction-level framing (not inter-node), Recovery Path
SLA targets citing Step 1d Class 2, all four stages with actor-chain mechanism and named
Verification Signal — AND Row 2 Chaos Test Block is complete.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first (Failure Signature first in C-phase):

Failure Signature (Class 3): **node-A / node-B diverging state framing**. Node-A view
(its last-write state) + node-B view (its diverging last-write state) + observability
view (no conflict event logged during partition). Not single-transaction framing — that
collapses Class 3 into Class 2.

Trigger Condition: replication lag threshold + dual-write conflict counter detection signal.
State: partition active, both nodes accepting independent writes.
Capability: checkout available on both sides; conflict invisible.
Data at Risk: diverging inventory counts, duplicate fulfillment orders.
Status Quo Risk: Step 1b Class 3. Acute branches: outcome A (`last-write-wins`) vs outcome B
(`manual-reconcile`). Chronic: duplicate-charge events per-transaction compound growth.
Conflict Resolution Strategy: canonical label (`last-write-wins` or `manual-reconcile`) +
adequacy judgment citing vocabulary constraint.
Severity / Blast Radius.

D-phase:
Recovery Path: TTD/TTC/TTR/TTV from **Step 1d, Class 3 row**. Actor-chain prefixes.
Named Verification Signal per stage (Validate VS: dual-write conflict counter = 0 for 60s).
Chaos Block: inject partition, expected behavior, pass signal, fail signal.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Test Block are complete,
including: Failure Signature with Class 3 node-A/node-B framing, Conflict Resolution using
a canonical label with adequacy judgment, Recovery Path SLA targets citing Step 1d Class 3.**

---

### Gap Register

Three findings inline. No separate observability section.

Per finding: **Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

HIGH / MEDIUM / LOW threat level + single strongest argument against deferral (2–3 sentences),
referencing gap findings and Step 1b carrying costs.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3

---

## V-03 — Phrasing Register Axis: Formal Numbered Enforcement Clauses

**Axis**: C-45 mechanisms expressed as numbered enforcement clauses inside sub-part 1d,
using formal contract language rather than prose description. Secondary axis: phrasing
register throughout the prompt shifts to formal technical specification mode.

**Hypothesis**: Numbered enforcement clauses — "Enforcement Clause 1: [TBD negation].
Enforcement Clause 2: [invention prohibition]." — are maximally unambiguous because:
(a) the clause label forces both to be evaluated independently rather than reading them
as a single combined statement, and (b) formal contract register reduces interpretive
flexibility that might allow a reader to score "contract violation language but no TBD
negation" as partial credit for C-45.

---

You are a Commerce / distributed systems domain expert operating in structured specification
mode. Your task: produce a complete resilience failure analysis for {topic} across three
failure classes, a Gap Register, and an Inertia Verdict.

Roles:
- **C — Commerce Expert**: #, Class, Trigger Condition, State, Capability, Data at Risk,
  Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D — Distributed Systems Expert**: Recovery Path, Verification Signal, Chaos Block

---

### Pre-Commitment Document: Resilience Commitment Matrix

This document must be completed in full before the scenario table begins. Values established
here are the authoritative sources for their respective columns — per-row independent
authoring is a contract violation where a reference source is named.

**Clause 1a — Domain Fragility Framing**

Produce 2–3 sentences establishing {topic}'s structural fragility across the three failure
classes. Framing must be domain-specific (not generic boilerplate). Required coverage:
client isolation creates pending-state windows, distributed writes create retry duplication
risk, concurrent partition writes create merge obligation.

**Clause 1b — Per-Class Carrying Cost Pre-Commitment**

The Status Quo Risk column is bound to the values in this table. Fill requirement per class:
carrying cost metric (named business metric) + accumulation rate qualifier + horizon qualifier.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [metric] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [metric] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [metric] | per-transaction | compound growth |

Row descriptors cite this clause as "Clause 1b, Class N" — not "the carrying cost section."

**Clause 1c — Per-Class Tipping Point Pre-Commitment**

The exit threshold at which deferral is indefensible. Quantified threshold expression +
named detection metric required per class. "Worsens over time" fails — it is not quantified.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [quantified threshold, e.g., "cart-abandon rate rises >2% above 30-day baseline"] | [metric] |
| 2 | [quantified threshold, e.g., "oversell count exceeds 50/month"] | [metric] |
| 3 | [quantified threshold, e.g., "reconciliation backlog exceeds 200 items"] | [metric] |

Row descriptors cite this clause as "Clause 1c, Class N."

**Clause 1d — SLA Budget Pre-Commitment**

| Class | TTD | TTC | TTR | TTV |
|---|---|---|---|---|
| 1 — Connectivity loss | | | | |
| 2 — Partial failure | | | | |
| 3 — Split-brain | | | | |

**Enforcement Clause E1 — Placeholder Negation**: Leaving any cell in the SLA Budget matrix
above blank, writing "TBD", writing "N/A", or using any equivalent unfilled value fails the
SLA Budget requirement. The pre-commitment is void if any cell is deferred. All twelve cells
must carry actual time values at the time this document is authored.

**Enforcement Clause E2 — Per-Row Invention Prohibition**: Independently authoring SLA
target values per scenario row — that is, writing TTD / TTC / TTR / TTV values in the
Recovery Path column that are not drawn from the matrix in Clause 1d above — is a named
contract violation. Recovery Path SLA fills must cite "Clause 1d, Class N, stage" as their
reference source. Any SLA value not present in the Clause 1d matrix is a contract violation
regardless of whether it is numerically plausible.

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` — one table, no splits or boundaries | Anti-split clause (below) |
| Section | Phase gate — all rows + chaos blocks before Gap Register | Section Order Requirement |
| Slot | In-row bold performative in Content descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary clause**: (1) Do not create separate tables for Commerce Expert columns and
Distributed Systems Expert columns. (2) Do not insert a horizontal rule, heading, or section
break between rows when column ownership shifts. (3) Do not produce a standalone chaos section
or standalone chaos-engineering table separate from row content. (4) Do not produce a
standalone observability section or standalone observability table separate from Gap Register
findings. All four structural escape routes are negated simultaneously.

**Section Order Requirement**: Pre-Commitment Document → Scenario Table (row N columns +
row N chaos block before row N+1) → Gap Register → Inertia Verdict → Finding Completeness
Checklist. **Advancing to row N+1 before row N's scenario columns AND chaos block are
complete is a section-order violation. Advancing to the Gap Register before all three rows
and chaos blocks are complete is a section-order violation.**

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1–3, continuous |
| Class | C | Class 1, 2, or 3 — named |
| Trigger Condition | C | Quantified threshold expression + named detection signal. Qualitative description alone fails. |
| State | C | System state at failure onset |
| Capability | C | Named commerce operations available. Generic descriptions fail. |
| Data at Risk | C | Named fields or records at risk |
| Status Quo Risk | C | **Reference Clause 1b, Class N — not independently authored.** Acute branches (outcome A / B) before chronic. Chronic: rate + horizon + metric. |
| Failure Signature | C | Behavioral fingerprint per actor during failure. ≥2 actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator applies — see below. |
| Severity / Blast Radius | C | Severity label + blast-radius qualifier |
| Conflict Resolution | C | Canonical label: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale` + adequacy judgment |
| Recovery Path | D | Four stages: Detect (TTD) → Contain (TTC) → Recover (TTR) → Validate (TTV). Each: actor-chain prefix + mechanism + **SLA from Clause 1d, Class N, stage (citing by label — per Enforcement Clause E2, independently authored values are a contract violation)** + named Verification Signal. ≥3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage, distinct from mechanism |
| Chaos Block | D | Inject / Expected Behavior / Pass Signal / Fail Signal — co-located with this row |

#### Failure Signature Class Boundary Discriminator

> **Class 2 specification** (Data consistency violation from partial failure): Transaction-level
> anomaly framing from a single write path. Observable at the transaction boundary — write
> committed on one leg of the transaction but confirmation absent. Multi-node divergence
> framing is incorrect for Class 2 and collapses the operational distinction.
>
> **Class 3 specification** (Split-brain / eventual consistency): Node-A / node-B framing
> with both nodes holding diverging last-write state simultaneously. Visible across node
> boundaries. Single-transaction framing is incorrect for Class 3 and collapses the
> operational distinction.
>
> Generic "data inconsistency" fills satisfying either class without the class-specific
> structural signature fail this discriminator.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first:

Trigger Condition: quantified connectivity threshold + detection signal.
State: client isolation at failure onset.
Capability: offline-available operations (named).
Data at Risk: in-flight cart, payment intent, order submission records.
Status Quo Risk: **Clause 1b, Class 1** — acute branches (cart dropped / cart stale-restored)
then chronic (rate + horizon + metric).
Failure Signature: Class 1 — client view (timeout, no TCP reset) + server view (no request in
access log, health probe healthy). Class 1 is not multi-node.
Severity / Blast Radius.

D-phase after C-phase:
Recovery Path: **Clause 1d, Class 1** SLA targets (citing by clause label per E2).
Actor-chain prefixes. Named Verification Signal per stage.
Chaos Block: inject / expected / pass signal / fail signal.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column —
Failure Signature with ≥2 named actor viewpoints (Class 1 framing), Recovery Path SLA
targets citing Clause 1d Class 1 by clause label (not independently authored), all four
stages with actor-chain mechanism and named Verification Signal — AND Row 1 Chaos Test
Block is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first:

Failure Signature: **Class 2 — transaction-level anomaly**: client spinner / server partial
commit / transaction boundary showing committed leg + missing leg. Clause 1d Class 2 applies.

Trigger Condition, State, Capability, Data at Risk, Status Quo Risk (**Clause 1b, Class 2**).
Acute branches (phantom reservation hold / oversell on silent drop). Chronic: oversell per-deploy.

D-phase: Recovery Path **Clause 1d, Class 2** SLA. Actor-chain. Named VS per stage. Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Test Block are complete, including
Failure Signature with Class 2 transaction-level framing and Recovery Path SLA citing
Clause 1d Class 2.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first:

Failure Signature: **Class 3 — node-A / node-B diverging state**: both nodes hold conflicting
last-write values simultaneously; observability layer shows no conflict during partition.
Clause 1d Class 3 applies.

Trigger Condition (replication lag threshold + dual-write counter detection).
State (partition active, both nodes accepting writes).
Capability (checkout available on both partition sides).
Data at Risk (diverging inventory, duplicate fulfillment).
Status Quo Risk: **Clause 1b, Class 3**. Acute branches: `last-write-wins` vs `manual-reconcile`.
Chronic: duplicate-charge per-transaction compound growth.
Conflict Resolution: canonical label + adequacy judgment.

D-phase: Recovery Path **Clause 1d, Class 3** SLA. Actor-chain. Named VS per stage.
Chaos Block: inject network partition / expected behavior / pass signal / fail signal.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Test Block are complete,
including Failure Signature with Class 3 node-A/node-B framing, Conflict Resolution with
canonical label and adequacy judgment, Recovery Path SLA citing Clause 1d Class 3.**

---

### Gap Register

Three findings inline (no separate observability section):
**Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

HIGH / MEDIUM / LOW + strongest argument against deferral (2–3 sentences) naming gap
findings and Clause 1b carrying costs.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3

---

## V-04 — Combined Axis: Inertia Framing Prominence + C-45 Document-Level Enforcement

**Axis**: Two axes combined. (A) Inertia framing: the pre-commitment document opens with an
explicit "Status Quo Risk Assessment" framing section that names the do-nothing competitor
before any failure classes are introduced — the status quo is treated as a named competitor.
(B) C-45: both enforcement mechanisms appear in a document-level enforcement preamble that
applies to all four sub-parts simultaneously, then are reinforced inline in sub-part 1d.

**Hypothesis**: Leading with the status quo as a named competitor forces inertia framing to
be explicit at the document level, not just at the row level. The document-level enforcement
preamble covering both C-45 mechanisms creates a pre-read contract: before the model begins
filling any sub-part, it has already processed both TBD negation and invention prohibition.
Inline reinforcement in 1d ensures the mechanisms are also read at the point of SLA matrix
construction.

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
(1) what the current failure mode looks like without any resilience investment (the do-nothing
    state: failures surface as hard errors, data is silently lost, no recovery path exists);
(2) why inertia is the default choice (the failures are invisible until they compound);
(3) what makes {topic}'s domain specifically fragile (connectivity isolation + idempotency
    gaps + partition conflict).

**Step 1b — Per-Class Carrying Costs**

The do-nothing cost per class. Status Quo Risk column references this sub-part.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Offline | [metric, e.g., cart-abandon events] | per-session | without ceiling |
| 2 — Partial failure | Degraded service | [metric, e.g., oversell count] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [metric, e.g., duplicate-charge events] | per-transaction | compound growth |

No blanks — Rule A applies. Status Quo Risk fills reference "Step 1b, Class N" — Rule B
applies; per-row invention is a contract violation.

**Step 1c — Per-Class Tipping Point Signals**

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [quantified, e.g., "cart-abandon rate >2% above 30-day baseline / dashboard alert"] | [metric] |
| 2 | [quantified, e.g., "oversell count >50/month / inventory anomaly counter"] | [metric] |
| 3 | [quantified, e.g., "reconciliation backlog >200 / queue-depth alert"] | [metric] |

No blanks — Rule A applies.

**Step 1d — SLA Budget**

| Class | TTD | TTC | TTR | TTV |
|---|---|---|---|---|
| 1 — Connectivity loss | | | | |
| 2 — Partial failure | | | | |
| 3 — Split-brain | | | | |

Rule A applies: no cell may be blank or TBD — every cell requires an actual time value.
Rule B applies: Recovery Path SLA fills must reference "Step 1d, Class N, stage" — per-row
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
| Failure Signature | C | Behavioral fingerprint per actor during failure. ≥2 actor viewpoints. Distinct from Trigger Condition and from State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label + blast-radius qualifier |
| Conflict Resolution | C | Canonical: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale` + adequacy judgment |
| Recovery Path | D | Detect → Contain → Recover → Validate. Actor-chain prefix + mechanism + **SLA from Step 1d, Class N, stage (Rule B — independently authored values are a contract violation)** + named Verification Signal. ≥3 of 4 stages with actor prefix. |
| Verification Signal | D | Named observable artifact per stage, distinct from mechanism |
| Chaos Block | D | Inject / Expected Behavior / Pass Signal / Fail Signal — co-located per row |

#### Failure Signature Class Boundary Discriminator

> **Class 2**: Transaction-level anomaly framing from a single write path. The inconsistency
> is visible at the transaction boundary — one leg committed, other leg absent. No inter-node
> framing. Example fill: "client: checkout spinner with no confirmation; server: inventory
> write committed, payment 503; transaction boundary: partial — reservation exists, order null."
>
> **Class 3**: Node-A / node-B diverging state framing showing both nodes holding conflicting
> last-write values simultaneously. No single-transaction framing. Example fill: "node-A: holds
> inventory = 47 (checkout-A applied); node-B: holds inventory = 47 (checkout-B applied,
> diverging); observability: conflict event absent during partition, surfaces only at healing."
>
> Generic inconsistency descriptions that satisfy either class without the class-specific
> structural signature fail even with multiple actor viewpoints.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first.

Begin with: what does the do-nothing scenario look like here? Cart is silently dropped,
user gets no recovery signal, the cost accumulates per-session without bound.

Trigger Condition: quantified connectivity threshold + detection signal.
State: client isolation at failure onset.
Capability: named offline-available operations.
Data at Risk: in-flight cart, pending payment intent, order submission records.
Status Quo Risk: **Step 1b, Class 1** (Rule B). Acute: cart dropped → immediate abandonment;
cart stale-restored → incorrect inventory at reconnect. Chronic: carrying cost metric,
rate, horizon from Step 1b.
Failure Signature: Class 1 — client timeout + server shows no request in access log.
Severity / Blast Radius.

D-phase after C-phase is complete:
Recovery Path: **Step 1d, Class 1** (Rule B — cite by label). Actor-chain prefixes.
Named Verification Signal per stage.
Chaos Block: inject / expected / pass / fail.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column —
Failure Signature with ≥2 actor viewpoints (Class 1 framing), Status Quo Risk citing
Step 1b Class 1 by label, Recovery Path SLA citing Step 1d Class 1 by label per Rule B,
all four stages with actor-chain mechanism and named Verification Signal — AND Row 1 Chaos
Test Block is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first.

Do-nothing scenario: oversell accumulates silently per deploy; inventory drift is invisible
until a customer calls to dispute the double-reservation.

Failure Signature: **Class 2 — transaction-level anomaly** (single write path). Not inter-node.
Trigger Condition, State, Capability, Data at Risk.
Status Quo Risk: **Step 1b, Class 2** (Rule B). Acute: phantom hold / oversell on silent drop.
Chronic: oversell per-deploy unbounded.

D-phase: Recovery Path **Step 1d, Class 2** (Rule B). Actor-chain. Named VS. Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete, including
Class 2 transaction-level Failure Signature and Recovery Path SLA citing Step 1d Class 2.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first.

Do-nothing scenario: duplicate charges compound per transaction; reconciliation backlog grows
indefinitely; the damage is invisible until two orders arrive at the warehouse.

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
**Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

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

## V-05 — Full Synthesis: All C-45 Axes Combined

**Axis**: Full synthesis — TBD negation and invention prohibition appear in three locations
simultaneously: (1) sub-part 1d header (as in V-01), (2) a dedicated enforcement blockquote
inside sub-part 1d (as in V-02), and (3) row descriptors referencing both mechanisms by name
at the SLA annotation point (new location). Secondary axis: lifecycle emphasis — Recovery Path
stages are given expanded structural prominence via named per-stage specification.

**Hypothesis**: Maximum redundancy across three locations makes C-45 impossible to miss under
any scoring interpretation: a scorer reading sub-part 1d's header sentence finds TBD negation;
a scorer reading the blockquote finds both mechanisms co-located; a scorer reading row
descriptors finds the invention prohibition named at SLA fill point. If any single location
fails to satisfy C-45, another location provides independent evidence. Full synthesis also
carries all C-41 through C-44 and C-46 axes from R15 V-05, ensuring 38/38 = 100.00.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic} across three failure classes. Produce a complete four-field failure
analysis per class, a Gap Register with inline observability, and an Inertia Verdict.

Two roles fill all columns:
- **C — Commerce Expert**: #, Class, Trigger Condition, State, Capability, Data at Risk,
  Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D — Distributed Systems Expert**: Recovery Path, Verification Signal, Chaos Block

---

### Pre-Commitment Document: Resilience Commitment Matrix

Four labeled sub-parts. Complete all four before writing any scenario row. The scenario table
is bound to the values established here — per-row independent authoring is a contract violation
where a sub-part provides the reference source.

**Step 1a — Domain Fragility Framing**

Write 2–3 sentences establishing {topic}'s structural fragility across all three failure
classes. Specific to this domain: (1) client isolation creates invisible pending-state windows;
(2) distributed writes without idempotency produce duplicate side effects on retry; (3)
concurrent partition writes create state divergence requiring pre-specified merge rules.

**Step 1b — Per-Class Carrying Costs**

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [commerce metric] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [commerce metric] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [commerce metric] | per-transaction | compound growth |

Status Quo Risk column fills reference this sub-part as "Step 1b, Class N carrying cost" —
not independently authored.

**Step 1c — Per-Class Tipping Point Signals**

| Class | Tipping Point Signal (threshold expression + detection signal) | Metric |
|---|---|---|
| 1 | [quantified threshold, e.g., "cart-abandon rate >2% above baseline / dashboard alert"] | [metric] |
| 2 | [quantified threshold, e.g., "oversell count >50/month / inventory anomaly counter"] | [metric] |
| 3 | [quantified threshold, e.g., "reconciliation backlog >200 / queue-depth alert"] | [metric] |

**Step 1d — SLA Budget**

Writing "TBD", leaving any cell blank, or using any equivalent placeholder in the matrix
below fails the SLA Budget requirement — the pre-commitment is void if any cell is deferred.

| Class | TTD (Detect) | TTC (Contain) | TTR (Recover) | TTV (Validate) |
|---|---|---|---|---|
| 1 — Connectivity loss | | | | |
| 2 — Partial failure | | | | |
| 3 — Split-brain | | | | |

> **SLA Budget Enforcement — both mechanisms required**
>
> **(1) Placeholder Negation** (restated for co-location): Every cell in the matrix above
> must carry an actual time value. "TBD", blank, or any unfilled placeholder fails the SLA
> Budget requirement. This enforcement applies at the time of authoring this sub-part — not
> at the time of row construction.
>
> **(2) Per-Row Invention Prohibition**: Independently authoring SLA target values in the
> Recovery Path column that are not drawn from the matrix above is a named contract
> violation against this pre-committed SLA Budget. Recovery Path SLA fills must cite
> "Step 1d, Class N, stage column" as their reference source. A fill that introduces any
> time value not present in the matrix above — even if numerically consistent — violates
> this contract.

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` — one table, no splits | Anti-split instruction (below) |
| Section | Phase gate — all rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | In-row bold performative inside Content descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary instruction** (all four consolidation escape routes closed simultaneously):
Do not create separate tables for Commerce Expert columns and Distributed Systems Expert
columns. Do not insert a horizontal rule, heading, or section break between rows when column
ownership shifts. Do not produce a standalone chaos section or standalone chaos-engineering
table separate from each row's inline content. Do not produce a standalone observability
section or standalone observability table separate from Gap Register findings. All four escape
routes are negated; satisfying any three without the fourth does not satisfy this instruction.

**Section Order Requirement**: (1) Pre-Commitment Document — all four sub-parts populated;
(2) Scenario Table — each row's scenario columns AND chaos block complete before the next
row begins; (3) Gap Register with three inline findings; (4) Inertia Verdict; (5) Finding
Completeness Checklist. **Do not advance to row N+1 until row N columns AND chaos block are
both complete. Do not advance to the Gap Register until all three rows and three chaos blocks
are complete.**

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1–3, continuous — one table, no splits |
| Class | C | Class 1 (Connectivity Loss), Class 2 (Partial Failure), or Class 3 (Split-Brain) |
| Trigger Condition | C | Two required components: (1) quantified threshold expression activating the scenario; (2) named detection signal by which the system identifies the threshold crossing. Qualitative description without a threshold fails. |
| State | C | System configuration at failure onset — named components and their states |
| Capability | C | Named commerce operations available during the failure. "Some functions degraded" is not named — fails. |
| Data at Risk | C | Specific named data fields, transaction records, or domain entities at risk |
| Status Quo Risk | C | **Reference Step 1b, Class N carrying cost — do not author per-row values independently.** At least one row must contain acute consequence branches (outcome A / outcome B) before the chronic metric. Three-component chronic: rate + horizon + metric. |
| Failure Signature | C | Observable behavioral fingerprint per actor during the failure. Distinct from Trigger Condition (entry threshold) and from State (pre-failure configuration). ≥2 named actor viewpoints. Class Boundary Discriminator — see below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius estimate or qualifier |
| Conflict Resolution | C | Canonical label: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | **Four named stage specifications** — each stage as a discrete named sub-specification: **Detect** (→ TTD) / **Contain** (→ TTC) / **Recover** (→ TTR) / **Validate** (→ TTV). Per stage: actor-chain prefix (`client →`, `server →`, `operator →`, `user →`) + mechanism + **SLA target: reference Step 1d, Class N, stage column — per the SLA Budget Enforcement in Step 1d, independently authored SLA values are a contract violation** + named Verification Signal. ≥3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact confirming stage completion. Observable (system state, log entry, metric value, API response code). Not a restatement of the mechanism. |
| Chaos Block | D | Co-located with this row: (1) Inject — named reproducible condition; (2) Expected Behavior; (3) Pass Signal; (4) Fail Signal. Four components required. |

#### Failure Signature Class Boundary Discriminator

> **Class 2 (Data Consistency Violation — Partial Failure)**: Fill requirement is
> transaction-level anomaly framing from a single write path. The inconsistency is observable
> at the transaction boundary — one leg of the transaction committed, the other absent —
> without requiring multi-node state divergence. Actor viewpoints: client view + server view
> + transaction boundary view. Node-A / node-B framing is incorrect for Class 2 and collapses
> the Class 2 / Class 3 operational distinction.
>
> **Class 3 (Split-Brain / Eventual Consistency)**: Fill requirement is node-A / node-B
> framing showing two nodes holding diverging last-write state simultaneously. The split is
> visible across node boundaries. Actor viewpoints: node-A view + node-B view + observability
> view (conflict event absent during partition). Single-transaction framing is incorrect for
> Class 3 and collapses the Class 2 / Class 3 operational distinction.
>
> A Failure Signature that describes "data inconsistency" without the class-specific
> structural signature fails this discriminator regardless of how many actor viewpoints it
> names.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`.
Free-text paraphrase ("the newest write takes precedence") does not satisfy this constraint.
The canonical label must appear as a discrete term. Class 3 row must apply a canonical label
and include an adequacy judgment citing this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first:

Trigger Condition: quantified connectivity loss threshold expression + detection signal.
Example: "client TCP connection attempt exceeds 30s timeout" / "client-side connectivity
monitor registers ETIMEDOUT; server access log shows no incoming request."

State: client-side isolation at failure onset. Name {topic} components affected.

Capability: list specific commerce operations available offline (e.g., cached-catalog browse,
local cart editing, draft order save). List what is blocked (e.g., checkout submission,
payment processing, inventory confirmation).

Data at Risk: in-flight cart state, pending payment intent, unsubmitted order records —
named specifically.

Status Quo Risk: **Step 1b, Class 1 carrying cost** — reference by sub-part label. Acute
branches: outcome A (cart silently dropped → immediate abandonment, no recovery signal);
outcome B (cart stale-restored → incorrect price or inventory at reconnection). Chronic:
carrying cost metric accumulates at rate qualifier without ceiling.

Failure Signature: **Class 1 framing** — client-view actor (connection timeout, no TCP reset,
no error message) + server-view actor (no request registered in access log, health probe
returns 200, server unaware of client state). Not multi-node framing — Class 1 is
client-isolation, not partition.

Severity / Blast Radius: all users attempting checkout in the connectivity window.

**D-phase after all C-phase columns are complete** (column-group gate enforced):

Recovery Path — four named stage specifications:
- **Detect** (TTD): actor-chain prefix + mechanism + **SLA from Step 1d, Class 1, TTD column (citing by sub-part label — independent invention is a contract violation per Step 1d enforcement)** + Verification Signal (named observable confirming detection)
- **Contain** (TTC): actor-chain prefix + mechanism + SLA from Step 1d Class 1 TTC + Verification Signal
- **Recover** (TTR): actor-chain prefix + mechanism + SLA from Step 1d Class 1 TTR + Verification Signal
- **Validate** (TTV): actor-chain prefix + mechanism + SLA from Step 1d Class 1 TTV + Verification Signal

Chaos Block: inject connectivity loss (e.g., block all outbound TCP from client), Expected
Behavior (offline mode activates, in-progress operations queued or surfaced with error),
Pass Signal (client enters offline mode, queued operations listed), Fail Signal (client
shows blank screen or crashes, no offline indicator).

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column —
including: Failure Signature with ≥2 named actor viewpoints using Class 1 (client-isolation)
framing; Trigger Condition with quantified threshold + detection signal; Status Quo Risk
citing Step 1b Class 1 by sub-part label with acute branches and three-component chronic;
all four Recovery Path stages each with actor-chain mechanism, SLA target citing Step 1d
Class 1 by sub-part label (not independently authored), and named Verification Signal —
AND the Row 1 Chaos Test Block (Inject / Expected Behavior / Pass Signal / Fail Signal) is
complete.**

---

#### Row 2 — Class 2: Partial Failure (Dependent Service Unavailable)

**Write this row now.** C-phase first:

Trigger Condition: quantified downstream-service degradation threshold (e.g., "payment API
p99 latency exceeds 500ms") + detection signal (e.g., "payment-provider timeout counter
increments past threshold in APM dashboard, alert fires to on-call").

State: {topic} upstream service (e.g., inventory-reservation) available; payment service
(or other named downstream dependency) degraded. Name the specific {topic} service topology.

Capability: pre-checkout operations available (browse, cart); checkout submission blocked
or pending queue. Name the exact boundary.

Data at Risk: inventory reservation drift (items reserved but order unconfirmed), oversell
risk from unacknowledged holds, pending payment intents.

Status Quo Risk: **Step 1b, Class 2 carrying cost** — cite by sub-part label. Acute branches:
outcome A (inventory hold persists indefinitely → phantom reservation lock, downstream
stockout); outcome B (inventory hold silently expires → oversell on next reservation attempt).
Chronic: oversell count accumulates per-deploy unbounded.

Failure Signature: **Class 2 framing — transaction-level anomaly from single write path**.
Actor viewpoints: client-view (checkout spinner, no error surfaced) + server-view (inventory
write committed, payment-service returning 503, inventory-service health probe healthy) +
transaction-boundary view (reservation record exists in inventory-service, order record absent
in order-service). **Do not use node-A / node-B framing — that is Class 3 framing.**

Severity / Blast Radius: all users attempting checkout while downstream service is degraded.

**D-phase after all C-phase columns are complete:**

Recovery Path — four named stage specifications:
- **Detect** (TTD): actor-chain prefix + mechanism (e.g., `server → circuit-breaker probe detects payment-service error rate exceeds threshold`) + **SLA from Step 1d, Class 2, TTD column (cite Step 1d Class 2 — not independently authored)** + Verification Signal (e.g., "payment-provider error-rate dashboard crosses alert threshold; on-call notification fires")
- **Contain** (TTC): actor-chain + mechanism (e.g., `server → circuit-breaker opens, checkout requests return 503 with retry-after header`) + SLA Step 1d Class 2 TTC + VS (e.g., "circuit-breaker state = OPEN in service mesh dashboard")
- **Recover** (TTR): actor-chain + mechanism + SLA Step 1d Class 2 TTR + VS
- **Validate** (TTV): actor-chain + mechanism + SLA Step 1d Class 2 TTV + VS (e.g., "payment-service error rate drops below threshold for 5-minute window; circuit-breaker transitions to CLOSED")

Chaos Block: inject payment service degradation (e.g., add 2s artificial latency to payment
API), Expected Behavior (circuit-breaker opens within TTD; checkout returns 503 with retry
guidance), Pass Signal (circuit-breaker state changes to OPEN; customer sees retry message),
Fail Signal (checkout returns 500 with no user guidance; circuit-breaker remains CLOSED;
reservation holds accumulate silently).

**Do not advance to Row 3 until Row 2 contains non-placeholder content in every column —
including: Failure Signature with Class 2 transaction-level framing (not inter-node — that
fails the Class Boundary Discriminator); Recovery Path SLA targets citing Step 1d Class 2
by sub-part label with four stage specifications each including actor-chain mechanism and
named Verification Signal — AND Row 2 Chaos Test Block is complete.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first:

Trigger Condition: replication lag threshold expression (e.g., "replication lag between
inventory-service nodes exceeds 5s") + detection signal (e.g., "dual-write conflict counter
increments in {topic} monitoring dashboard; replication-lag alert fires").

State: network partition between inventory-service nodes (or equivalent {topic} distributed
state component); both nodes accepting independent writes; conflict detection not yet active.

Capability: users on both partition sides can submit checkouts; conflict is invisible to
users; both sides report success.

Data at Risk: inventory count diverges across nodes; duplicate fulfillment orders possible
(same inventory unit allocated to two customers); potential double-charge on payment
reconciliation.

Status Quo Risk: **Step 1b, Class 3 carrying cost** — cite by sub-part label. Acute branches:
outcome A (`last-write-wins` applied → earlier reservation silently lost, oversell for the
earlier buyer); outcome B (`manual-reconcile` required → order processing halted, customer
delay, operations team intervention). Chronic: duplicate-charge events compound per-transaction
without ceiling.

Conflict Resolution Strategy: `last-write-wins` (if recency determines winner) or
`manual-reconcile` (if business rules require human arbitration) — use canonical label, include
adequacy judgment citing vocabulary constraint.

Failure Signature: **Class 3 framing — node-A / node-B diverging state**. Actor viewpoints:
node-A view (holds last-write inventory count reflecting checkout-A) + node-B view (holds
last-write inventory count reflecting checkout-B, diverging from node-A) + observability
view (no conflict event logged during partition; both checkouts show confirmation to users;
divergence surfaces only when partition heals and reconciliation runs). **Do not use
single-transaction framing — that is Class 2 framing.**

Severity / Blast Radius: users distributed across both partition sides during the partition
window; blast radius scales with partition duration.

**D-phase after all C-phase columns are complete:**

Recovery Path — four named stage specifications:
- **Detect** (TTD): `server → partition-detection mechanism identifies replication-lag threshold exceeded` + **SLA from Step 1d, Class 3, TTD column (cite Step 1d Class 3 — independently authored SLA values are a contract violation per Step 1d enforcement block)** + Verification Signal (e.g., "dual-write conflict counter registers non-zero value in monitoring dashboard; replication-lag alert fires to on-call")
- **Contain** (TTC): `server → write quorum suspended on minority partition side; one-sided writes accepted only` + SLA Step 1d Class 3 TTC + VS (e.g., "minority-partition node shows write-suspended state in cluster health dashboard")
- **Recover** (TTR): `operator → conflict-resolution strategy applied (last-write-wins or manual-reconcile); partition healing initiated` + SLA Step 1d Class 3 TTR + VS (e.g., "dual-write conflict counter returns to 0; both nodes report identical inventory count")
- **Validate** (TTV): `operator → reconciliation audit confirms no duplicate fulfillment records; inventory count matches expected post-resolution value` + SLA Step 1d Class 3 TTV + VS (e.g., "dual-write conflict counter remains 0 for 60s sustained; fulfillment deduplication log shows 0 new duplicates")

Chaos Block: inject network partition between inventory-service nodes (e.g., iptables DROP
between node-A and node-B), Expected Behavior (partition detected within TTD; write quorum
applied; conflict-resolution strategy activates within TTC), Pass Signal (dual-write conflict
counter resets to 0 for 60s after partition heals; both nodes show identical inventory count),
Fail Signal (conflict counter remains non-zero after TTR elapsed; inventory count diverges
beyond tolerance threshold; duplicate fulfillment orders present in order-service).

**Do not advance to the Gap Register until Row 3 columns AND Chaos Test Block are complete,
including: Failure Signature with Class 3 node-A / node-B diverging state framing (not
single-transaction framing — that fails the Class Boundary Discriminator); Conflict Resolution
Strategy with canonical vocabulary label and adequacy judgment; all four Recovery Path stage
specifications each with actor-chain mechanism, SLA target citing Step 1d Class 3 by sub-part
label, and named Verification Signal — AND Row 3 Chaos Test Block is complete.**

---

### Gap Register

Required output section. Three findings required — one per type. Findings appear inline with
observability fields — no separate observability section, no standalone observability table.

Per finding format:
- **Finding Type**: [Offline Experience Gap | Data Consistency Violation | Missing Recovery Flow]
- **Description**: specific and actionable — name the specific {topic} operation, data record,
  or recovery flow that is missing. Generic statements ("offline support may be limited") fail.
- **Metric**: named system or business metric to monitor for this finding
- **Alert**: named alert condition and threshold that fires when the metric crosses the
  actionable threshold — specific to {topic}'s stack (not "monitor the logs")
- **Owner**: responsible role or team — not "TBD" or "engineering team"

Finding types present: ___ of 3

---

### Inertia Verdict

After completing all three Gap Register findings, synthesize:
- **Inertia threat level**: HIGH / MEDIUM / LOW
- **Strongest argument against deferral** (2–3 sentences): name the specific gap findings and
  reference the carrying-cost metric from Step 1b that continues to accumulate without
  intervention. State what becomes irreversible or compounding if action is deferred beyond
  the Step 1c tipping point.

---

### Finding Completeness Checklist

Required output section. Fill in all fields:
- [ ] Offline Experience Gap — present
- [ ] Data Consistency Violation — present
- [ ] Missing Recovery Flow — present
- Finding types present: ___ of 3
