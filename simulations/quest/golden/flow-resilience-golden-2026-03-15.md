---
skill: quest-golden
skill_target: flow-resilience
date: 2026-03-15
rounds: 20
rubric_final: flow-resilience-rubric-v20-2026-03-15.md
score: 100.0
status: GOLDEN
---

# flow-resilience — Golden Prompt (R20 V-05)

**Rubric**: v19 · 51 criteria · Score: 51/51 → 100.00
**Note**: v20 rubric (53 criteria) introduces C-60 and C-61 as open axes for R21.

---

## Prompt Body

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic} across three structurally distinct failure classes and produce a
complete failure analysis with a Gap Register, Inertia Synthesis, and Finding Completeness
Checklist.

### Role Declaration

Two roles fill all scenario columns.

**C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk,
Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy.

**D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block.

---

### §0 — Enforcement Mandate — Enforcement Protocol 1/4 *(originating declaration; restated as Enforcement Protocol 2/4 in the §1 Enforcement Contract preamble below)*

> Distributed Systems Expert: the Recovery Path column requires SLA targets drawn exclusively
> from the pre-committed SLA Budget (§1d) of the Pre-Commitment Document below. Independently
> authoring SLA values per scenario row without referencing §1d is a **named contract
> violation** at document-header scope. This §0 mandate is Enforcement Protocol 1/4 — the
> originating declaration for this constraint. The constraint is restated at Enforcement
> Protocol 2/4 (§1 Enforcement Contract preamble below), Protocol 3/4 (§1b and §1d
> sub-parts), and Protocol 4/4 (Column Contract Recovery Path entry). This mandate governs
> the pre-commitment structure (§1 below) and is closed by the Inertia Synthesis (§2 below).

---

### Pre-Commitment Document: Resilience Commitment Matrix

**§1 — Enforcement Contract — Enforcement Protocol 2/4** (governing §§ 1a through 1d —
read before filling any sub-part) *(§0 above is Enforcement Protocol 1/4 — the originating
declaration)*:

> This document pre-commits authoritative values for the scenario table.
>
> **Rule A — No Deferral**: Any cell left blank, "TBD", "N/A", or equivalent unfilled value
> in any sub-part of this document fails the pre-commitment requirement. Every cell must carry
> an actual value at authoring time.
>
> **Rule B — No Per-Row Invention** *(§0 above restates this rule at document-header scope as
> Enforcement Protocol 1/4)*: Each sub-part is the authoritative source for its corresponding
> scenario column. Independently authoring per-row values not drawn from the corresponding
> sub-part is a named contract violation. Row fills must reference the source sub-part by label.
>
> Both rules govern §§ 1a through 1d. This §1 preamble is Enforcement Protocol 2/4.

---

**§1a — Domain Fragility Framing**

Write 2–3 sentences establishing {topic}'s structural fragility across the three failure classes.
Domain-specific framing required — generic distributed-systems boilerplate fails. Cover: client
isolation creates invisible pending-state windows; idempotency gaps create retry-duplication side
effects; concurrent partition writes create state divergence requiring pre-specified merge rules
to avoid duplicate fulfillment or double-charge.

**§1b — Per-Class Carrying Costs**

Status Quo Risk fills reference this sub-part as "§1b, Class N".
**Rule A applies (Enforcement Protocol 3/4 reinforced here)** — no blank cells, no TBD, no
placeholders. **Rule B applies** — Status Quo Risk fills must cite "§1b, Class N" by label;
independently authored carrying cost values are a named contract violation.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [named metric] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [named metric] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [named metric] | per-transaction | compound growth |

**§1c — Per-Class Tipping Point Signals**

**Rule A applies** — quantified threshold expression + named detection metric required per class.
"Worsens over time" is not quantified and fails Rule A.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [quantified threshold + detection signal] | [metric] |
| 2 | [quantified threshold + detection signal] | [metric] |
| 3 | [quantified threshold + detection signal] | [metric] |

**§1d — SLA Budget** — Enforcement Protocol 3/4

**Rule A applies** — no blank cells. All twelve cells must carry actual time values at authoring.
**Rule B applies** — Recovery Path SLA fills must cite "§1d, Class N, stage column" by label;
independently authored per-row SLA values are a named contract violation at the column-contract
level (Enforcement Protocol 4/4).

| Class | TTD (Detect) | TTC (Contain) | TTR (Recover) | TTV (Validate) |
|---|---|---|---|---|
| 1 — Connectivity loss | | | | |
| 2 — Partial failure | | | | |
| 3 — Split-brain | | | | |

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` — one table, no owner-group splits | Anti-boundary instruction (below) |
| Section | Phase gate — all rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | In-row bold performative inside Content descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary instruction** (all four escape routes closed simultaneously): Do not create
separate tables for Commerce Expert columns and Distributed Systems Expert columns. Do not insert
a horizontal rule, heading, or section break between rows when column ownership shifts. Do not
produce a standalone chaos section or standalone chaos-engineering table. Do not produce a
standalone observability section or standalone observability table.

**Section Order Requirement**: (1) §0 complete; (2) Pre-Commitment Document — all four §1
sub-parts complete (Enforcement Protocols 3/4 satisfied at §1b and §1d); (3) Scenario Table
— row N scenario columns AND row N Chaos Test Block before row N+1; (4) Gap Register with three
inline findings; (5) §2 — Inertia Synthesis; (6) Finding Completeness Checklist. **Do not
advance to row N+1 until row N columns AND Chaos Block are both complete — Rule B (Enforcement
Protocol 4/4) applies to every D-phase Recovery Path fill. Do not advance to the Gap Register
until all three rows and all three Chaos Blocks are complete. Do not advance to §2 — Inertia
Synthesis until the Gap Register three findings are complete.**

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1–3, continuous — one unified table |
| Class | C | Class 1 (Connectivity Loss), Class 2 (Partial Failure), or Class 3 (Split-Brain) |
| Trigger Condition | C | Quantified threshold expression + named detection signal. Qualitative only fails. |
| State | C | System configuration at failure onset — named components and states |
| Capability | C | Named commerce operations available during failure. Generic descriptions fail. |
| Data at Risk | C | Specific named data fields, transaction records, or domain entities |
| Status Quo Risk | C | **Reference §1b, Class N (Rule B — not independently authored)**. Acute branches (A/B) before chronic metric. Three-component chronic: rate + horizon + metric from §1b. |
| Failure Signature | C | Behavioral fingerprint per actor during failure. ≥2 named actor viewpoints. Distinct from Trigger Condition and from State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | Detect → Contain → Recover → Validate. Per stage: actor-chain prefix (`client ->`, `server ->`, `operator ->`, `user ->`) + mechanism + **SLA from §1d, Class N, stage column — Enforcement Protocol 4/4 (restated for co-location at column-contract level): any SLA value not drawn from §1d is a named contract violation** + named Verification Signal. ≥3 of 4 stages with labeled actor prefix. See Recovery Path Stage Contract (below). |
| Verification Signal | D | Named observable artifact per stage confirming stage completion. Distinct from mechanism. |
| Chaos Block | D | Four components co-located with this row: Inject (named reproducible condition) / Expected Behavior / Pass Signal / Fail Signal. Not a separate section. Not a standalone table. |

#### Failure Signature Class Boundary Discriminator

> **Class 2 (Partial Failure — Data Consistency Violation)**: Transaction-level anomaly framing
> from a single write path. Observable at the transaction boundary. No inter-node divergence
> framing. Node-A / node-B framing is incorrect for Class 2.
>
> **Class 3 (Split-Brain / Eventual Consistency)**: Node-A / node-B framing showing two nodes
> holding diverging last-write state simultaneously. Single-transaction framing is incorrect
> for Class 3.
>
> Generic fills satisfying either class without the class-specific structural signature fail
> even with multiple actor viewpoints.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`.
Free-text paraphrase fails. Class 3 row must apply a canonical label with adequacy judgment
citing this constraint.

#### Recovery Path Stage Contract

Every Recovery Path fill must sequence through all four stages in order: **Detect → Contain →
Recover → Validate**. For each stage, three components are required at fill time:

> | Stage | SLA Type | Actor-chain + Mechanism + Verification Signal contract |
> |---|---|---|
> | Detect | TTD from §1d | actor-chain prefix + detection mechanism (how the system or operator identifies the failure) + named VS confirming detection complete (named health probe response, alert fired, or metric threshold crossed) |
> | Contain | TTC from §1d | actor-chain prefix + containment action (how blast radius is bounded) + named VS confirming containment achieved (circuit breaker open, queue depth falling, traffic re-routed) |
> | Recover | TTR from §1d | actor-chain prefix + recovery mechanism (how normal service is restored) + named VS confirming state restored (service returns 200, reconciliation delta reaches 0, inventory counts converge) |
> | Validate | TTV from §1d | actor-chain prefix + validation check (how the system confirms healthy end-state) + named VS confirming healthy end-state (dual-write conflict counter at 0 for 60s, audit trail complete, cart state consistent with committed inventory) |
>
> **Anti-collapse**: Do not describe all four stages in a single sentence. Do not omit the
> Validate stage. Do not substitute a generic "monitor and verify" for a named Verification
> Signal. The Recovery Path Stage Contract governs all three scenario rows.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first. Produce all C-phase columns before D-phase columns.

Trigger Condition: quantified connectivity threshold expression + detection signal (name the
signal). State: client-side isolation at failure onset — name {topic} components affected.
Capability: offline-available commerce operations (named) + blocked operations. Data at Risk:
in-flight cart state, pending payment intent, unsubmitted order records. Status Quo Risk:
**§1b, Class 1 carrying cost** (Rule B — cite "§1b, Class 1" by label). Acute branches:
outcome A (cart dropped → immediate abandonment); outcome B (cart stale-restored → incorrect
inventory at reconnect). Chronic: rate + horizon + metric from §1b, Class 1. Failure Signature:
Class 1 framing — client-view (timeout, no TCP reset) + server-view (no request in access log,
health probe healthy). Not multi-node framing. Severity / Blast Radius.

D-phase after all C-phase columns complete:
Recovery Path: **§1d, Class 1** — Rule B — **Enforcement Protocol 4/4 applies** — cite by
label; any SLA value not drawn from §1d Class 1 is a named contract violation. Per Recovery
Path Stage Contract: four stages in order, actor-chain ≥3 stages, SLA from §1d Class 1 by
label, named VS per stage.
Chaos Block: inject connectivity loss / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column —
including Failure Signature with ≥2 Class 1 actor viewpoints, Status Quo Risk citing §1b
Class 1 by label with acute branches and three-component chronic, all four Recovery Path stages
per Recovery Path Stage Contract with actor-chain mechanism, SLA from §1d Class 1 by label
(Enforcement Protocol 4/4), and named Verification Signal per stage — AND Row 1 Chaos Test
Block is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first, then D-phase.

Trigger Condition: quantified downstream-service degradation threshold + detection signal.
State: upstream available; downstream payment degraded. Capability: browse/cart available;
checkout blocked or queued. Data at Risk: inventory reservation drift, unconfirmed orders,
oversell risk. Status Quo Risk: **§1b, Class 2** (Rule B). Acute: phantom hold / oversell on
silent drop. Chronic: named metric accumulates per-deploy unbounded from §1b, Class 2. Failure
Signature: **Class 2 — transaction-level anomaly** (single write path). Client-view + server-view
+ transaction-boundary view. No node-A / node-B framing. Severity / Blast Radius.

D-phase: Recovery Path **§1d, Class 2** — Rule B — **Enforcement Protocol 4/4 applies** —
cite by label. Per Recovery Path Stage Contract. Actor-chain. Named VS per stage.
Chaos Block: inject downstream failure / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete, including Class 2
transaction-level Failure Signature with ≥2 actor viewpoints, Status Quo Risk citing §1b Class 2
by label, Recovery Path all four stages per Stage Contract, and SLA citing §1d Class 2 by label
(Enforcement Protocol 4/4).**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

Trigger Condition: replication lag threshold + dual-write conflict counter detection signal.
State: partition active, both nodes accepting independent writes. Capability: checkout available
on both partition sides; conflict invisible to users. Data at Risk: diverging inventory counts,
duplicate fulfillment orders, double-charge risk. Status Quo Risk: **§1b, Class 3** (Rule B).
Acute: `last-write-wins` / `manual-reconcile`. Chronic: duplicate-charge events compound
per-transaction from §1b, Class 3. Failure Signature: **Class 3 — node-A / node-B diverging
state**. Not single-transaction. Conflict Resolution: canonical label + adequacy judgment.
Severity / Blast Radius.

D-phase: Recovery Path **§1d, Class 3** — Rule B — **Enforcement Protocol 4/4 applies** —
cite by label. Per Recovery Path Stage Contract. Actor-chain. Named VS per stage.
Chaos Block: inject partition / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Block are complete,
including Class 3 node-A/node-B Failure Signature, canonical Conflict Resolution label with
adequacy judgment, Recovery Path all four stages per Stage Contract, and SLA citing §1d Class 3
by label (Enforcement Protocol 4/4). Do not advance to §2 — Inertia Synthesis until the Gap
Register three inline findings are complete.**

---

### Gap Register

Three findings inline — no separate observability section, no standalone observability table:

**Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### §2 — Inertia Synthesis

Structure the synthesis using four components:

1. **Urgency label**: HIGH / MEDIUM / LOW
2. **Carrying cost citation**: name the specific §1b Class N carrying cost driving the
   urgency — cite sub-part label, rate, horizon, and metric
3. **Gap finding count**: state how many of the three finding types are present and which
   finding creates the highest compounding risk
4. **Escalation recommendation**: name the owner, the threshold that triggers action, and
   the consequence of missing that threshold

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow

---

## What Made It Golden

Five structural patterns distinguish R20 V-05 from the minimal R20 V-01 (phrasing-register-only):

**1. §0 as independently navigable enforcement mandate (C-59)**
The enforcement constraint is a named `§0 — Enforcement Mandate — Enforcement Protocol 1/4`
section heading at document-header scope — not a blockquote nested inside the Role Declaration.
This makes the mandate independently locatable via structural scan without entering any section
body. Earlier rounds placed the constraint as an inline blockquote inside the D-role declaration,
satisfying enforcement intent but failing navigability.

**2. Point-of-use enforcement invocation at every D-phase row descriptor (C-57)**
Every row's D-phase fill instruction carries `Enforcement Protocol 4/4 applies — cite by label`
co-located at the Recovery Path fill site. This collapses the distance between the rule origin
(§0) and the rule application point (each row), making the contract violation visible at
authoring time rather than requiring a reader to back-reference §1d.

**3. Structured four-component §2 Inertia Verdict template (C-58)**
The Inertia Synthesis section uses a named §2 heading and a four-slot template (urgency label /
carrying-cost citation with sub-part label + rate + horizon + metric / gap finding count with
highest-risk finding identified / escalation with owner + threshold + consequence). Prior rounds
used evaluative prose for the verdict; the template converts it into a fill contract with
verifiable completeness.

**4. Recovery Path Stage Contract as column-contract structural pre-commitment (C-60)**
A dedicated Stage Contract blockquote in the Column Contract section pre-specifies per-stage
requirements (actor-chain type + mechanism type + SLA type + VS type) for all four lifecycle
stages before any row is filled. Parallels §1d's SLA Budget pre-commitment but operates at
stage-mechanic architecture granularity. Anti-collapse instructions explicitly negate
single-sentence stage collapse and Validate-stage omission.

**5. §0→§2 closed document arc (Axis E)**
§0 forward-references §2 by name: "This mandate governs the pre-commitment structure (§1
below) and is closed by the Inertia Synthesis (§2 below)." This creates a verifiable
mandate→commitment→synthesis chain traversable at document-header scope without entering
any section body — completing the §0↔§1 bidirectional circuit (C-56) with a §0→§2 document
arc closure.

---

## Final Rubric Criteria Summary (v20 — 53 criteria)

| Block | Criteria | Description |
|---|---|---|
| Essential | C-01–C-05 | Three failure classes / four-field structure / gap identification / DS accuracy / commerce grounding |
| Recommended | C-06–C-08 | Severity+blast radius / chaos test / observability hooks |
| Aspirational | C-09–C-56 | Actor-chain / vocab constraint / pre-commitment / section-order gate / enforcement cascade / inertia verdict / bidirectional §0↔§1 / ... |
| R19 new | C-57 | Point-of-use enforcement invocation co-located in D-phase row descriptors |
| R19 new | C-58 | Structured four-component Inertia Verdict template (urgency / cost / findings / escalation) |
| R19 new | C-59 | §0 as named section heading at document-header scope — independently navigable enforcement element |
| R20 new | C-60 | Recovery Path Stage Contract as pre-specified column-contract structural commitment (per-stage actor-chain + mechanism + SLA + VS) |
| R20 new | C-61 | §2 as second independently navigable document-scope verdict boundary (parallel structural peer to §0) |

**R20 V-05 score**: 51/51 = 100.00 (v19 rubric) · 51/53 = 96.23 (v20 rubric, C-60+C-61 open for R21)

**Open for R21**: A variation that satisfies both C-60 (Recovery Path Stage Contract) and C-61
(§2 named section heading) in a single prompt achieves 53/53 = 100.00 under v20. R20 V-05
carries both axes — the rubric confirmed them as independent passing criteria; the R21 task is
to verify the combination under a fresh scoring pass with the v20 denominator.
