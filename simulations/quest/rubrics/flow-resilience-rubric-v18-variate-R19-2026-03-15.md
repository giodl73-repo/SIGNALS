# flow-resilience — Round 19 Variations (Rubric v18)

**Rubric**: v18 · 48 aspirational criteria · Ceiling entering R19: 47/48 → 99.79 (R18 V-03)

**Open criteria entering R19**: **C-54 + C-55 + C-56 must all pass simultaneously.**

- **C-54** requires: every enforcement location carries "Enforcement Instance K of N" (or
  equivalent), where K is the location's sequential position and N is the total count. C-53
  requires two self-labeled restatements at distinct levels; C-54 extends labeling to every
  location — even locations not carrying a self-restatement label must carry the count.
- **C-55** requires: the document-header enforcement element (C-52) carries an explicit
  self-label identifying it as the originating declaration — e.g., "(originating declaration)"
  or "Enforcement Instance 1 of N (originating declaration)".
- **C-56** requires: both the document-header element and the enforcement preamble name
  each other by label, creating a closed bidirectional reference circuit. C-52 requires
  preamble → document-header (one direction). C-56 adds document-header → preamble
  (the reciprocal direction).

**R18 diagnosis**:
- V-03 PASS C-54+C-55, FAIL C-56: Four locations labeled Instance 1/2/3/4 of 4; L1 carries
  "(originating declaration)". Sole gap: D-Phase Enforcement Note (L1) does not name the
  Document Enforcement Contract preamble (L2) by label — preamble → L1 exists, but L1 →
  preamble does not.
- V-02/V-04 PASS C-56, FAIL C-54+C-55: §0 names "§1 preamble Rule B"; preamble names "§0
  above". Sole gaps: locations do not carry sequential "Instance K of N" labels; §0 does not
  carry "(originating declaration)" self-label.

**R19 synthesis path**: V-03's numbered-instance architecture (C-54 PASS) + V-03's
originating-declaration self-label at L1 (C-55 PASS) + add L1's forward-pointer naming the
preamble by label (C-56 PASS). The sole structural delta from V-03 R18: L1 gains a forward
reference to the enforcement preamble. Three approaches to that forward reference (V-01 through
V-03), then two combined-axis variants using the §0-form pattern (V-04, V-05).

| Variation | Axis | Hypothesis | C-54/C-55/C-56 Strategy |
|---|---|---|---|
| V-01 | C-56 closure — inline forward-pointer parenthetical in L1 | Appending "(restated as Enforcement Instance 2 of 4 in the Document Enforcement Contract preamble below)" to L1 is the minimal delta that closes C-56 while leaving C-54+C-55 intact | V-03 R18 architecture + forward-pointer parenthetical in L1 |
| V-02 | C-56 closure — dedicated cross-reference sub-bullets at both ends | Explicit labeled cross-reference lines ("→ Cross-reference forward" in L1; "→ Cross-reference backward" in L2) are more structurally unambiguous than an inline parenthetical | V-03 architecture + explicit bidirectional cross-reference bullets in L1 and L2 |
| V-03 | Phrasing register — "Enforcement Clause K/N" compact notation | "Clause K/N" aligns with contract-law convention and is more compact; tests whether rubric criteria bind on structural position rather than specific terminology | Same forward-pointer as V-01 but with "Enforcement Clause K/N" replacing "Enforcement Instance K of N" throughout |
| V-04 | Combined: §0-form document-header + numbered instances everywhere + mutual reference | §0 as a named section heading (vs D-Phase blockquote) is a structurally stronger document-header element; adding sequential count labels at all four §0-form locations closes C-54+C-55+C-56 simultaneously | §0 Instance 1 of 4 (originating declaration; forward ref to §1 preamble as Instance 2); preamble Instance 2 of 4 naming §0; sub-part Instance 3; column Instance 4 |
| V-05 | Combined: §0-form + numbered instances + mutual reference + lifecycle emphasis + structured inertia framing | Per-row enforcement instance invocation within row descriptors reinforces the cascade at the point of use; structured inertia template (urgency + carrying-cost ref + gap count + recommendation) makes the verdict actionable | All of V-04's synthesis + row descriptors invoke Instance count; Inertia Verdict carries a four-component structured template |

---

## V-01 — Single-Axis: Inline Forward-Pointer Parenthetical in L1

**Axis**: C-56 closure via inline parenthetical appended to the L1 originating declaration.
The D-Phase Enforcement Note header gains a forward-pointer naming the preamble by label:
"(originating declaration; restated as Enforcement Instance 2 of 4 in the Document Enforcement
Contract preamble below)". All other structure is V-03 R18 verbatim.

**Hypothesis**: V-03 R18 already passes C-54 (four locations labeled Instance 1/2/3/4 of 4)
and C-55 (L1 carries "(originating declaration)"). The forward-pointer parenthetical is the
minimal single addition that closes C-56: L1 now names the preamble by label; the preamble
already names L1. The bidirectional circuit is closed. Result: 48/48 → 100.00.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic} across three structurally distinct failure classes and produce a
complete failure analysis with a Gap Register, Inertia Verdict, and Finding Completeness
Checklist.

### Role Declaration

Two roles fill all scenario columns.

**C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk,
Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy.

**D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block.

> **D-Phase Enforcement Note — Enforcement Instance 1 of 4 (originating declaration;
> restated as Enforcement Instance 2 of 4 in the Document Enforcement Contract preamble
> below)**: The Recovery Path column requires SLA targets drawn from the pre-committed SLA
> Budget (Step 1d) of the Pre-Commitment Document below. Independently authoring SLA values
> per scenario row without referencing Step 1d is a **named contract violation**. This is the
> originating declaration; it is restated at three additional enforcement levels within the
> pre-commitment document and column contract.

---

### Pre-Commitment Document: Resilience Commitment Matrix

**Document Enforcement Contract — Enforcement Instance 2 of 4** (governing §§ 1a through 1d
— read before filling any sub-part) *(restated from D-Phase Enforcement Note above, which is
Enforcement Instance 1 of 4 — the originating declaration)*:

> This document pre-commits authoritative values for the scenario table.
>
> **Rule A — No Deferral**: Any cell left blank, "TBD", "N/A", or equivalent unfilled value
> in any sub-part of this document fails the pre-commitment requirement. Every cell must carry
> an actual value at authoring time.
>
> **Rule B — No Per-Row Invention**: Each sub-part is the authoritative source for its
> corresponding scenario column. Independently authoring per-row values not drawn from the
> corresponding sub-part is a named contract violation. Row fills must reference the source
> sub-part by label.
>
> Both rules govern §§ 1a through 1d. This preamble is Enforcement Instance 2 of 4.

---

**Step 1a — Domain Fragility Framing**

Write 2–3 sentences establishing {topic}'s structural fragility across the three failure classes.
Domain-specific framing required. Cover: client isolation creates invisible pending-state windows;
idempotency gaps create retry-duplication risk; concurrent partition writes require pre-specified
merge rules.

**Step 1b — Per-Class Carrying Costs**

Status Quo Risk fills reference this sub-part as "Step 1b, Class N".
**Rule A applies (Enforcement Instance 3 of 4 reinforced here)** — no blank cells. **Rule B
applies** — Status Quo Risk fills must cite "Step 1b, Class N"; per-row invention is a contract
violation.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [named metric] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [named metric] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [named metric] | per-transaction | compound growth |

**Step 1c — Per-Class Tipping Point Signals**

**Rule A applies** — quantified threshold expression + named detection metric required per class.
"Worsens over time" is not quantified and fails Rule A.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [quantified threshold + detection signal] | [metric] |
| 2 | [quantified threshold + detection signal] | [metric] |
| 3 | [quantified threshold + detection signal] | [metric] |

**Step 1d — SLA Budget** — Enforcement Instance 3 of 4

**Rule A applies** — no blank cells. All twelve cells must carry actual time values at authoring.
**Rule B applies** — Recovery Path SLA fills must cite "Step 1d, Class N, stage column";
independently authored per-row SLA values are a contract violation.

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

**Section Order Requirement**: (1) Pre-Commitment Document — all four sub-parts; (2) Scenario
Table — row N scenario columns AND row N Chaos Test Block before row N+1; (3) Gap Register with
three inline findings; (4) Inertia Verdict; (5) Finding Completeness Checklist. **Advancing to
row N+1 before row N columns and Chaos Block are complete is a sequencing violation. Advancing
to the Gap Register before all three rows and Chaos Blocks are complete is a sequencing violation.**

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
| Status Quo Risk | C | **Reference Step 1b, Class N (Rule B — not independently authored)**. Acute branches (A/B) before chronic metric. Three-component chronic: rate + horizon + metric from Step 1b. |
| Failure Signature | C | Behavioral fingerprint per actor during failure. ≥2 named actor viewpoints. Distinct from Trigger Condition and from State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | Detect → Contain → Recover → Validate. Per stage: actor-chain prefix (`client ->`, `server ->`, `operator ->`, `user ->`) + mechanism + **SLA from Step 1d, Class N, stage column — Enforcement Instance 4 of 4 (restated for co-location at column-contract level): any SLA value not drawn from Step 1d is a named contract violation** + named Verification Signal. ≥3 of 4 stages with labeled actor prefix. |
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
> Generic fills satisfying either class without the class-specific structural signature fail.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`.
Free-text paraphrase fails. Class 3 row must apply a canonical label with an adequacy judgment
citing this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first. Produce all C-phase columns before D-phase columns.

Trigger Condition: quantified connectivity threshold expression + detection signal. State:
client-side isolation at failure onset — name {topic} components affected. Capability:
offline-available commerce operations (named) + blocked operations. Data at Risk: in-flight
cart state, pending payment intent, unsubmitted order records. Status Quo Risk: **Step 1b,
Class 1 carrying cost** (Rule B — cite sub-part label). Acute branches: outcome A (cart
dropped → immediate abandonment); outcome B (cart stale-restored → incorrect inventory at
reconnect). Chronic: rate + horizon + metric from Step 1b, Class 1. Failure Signature: Class 1
framing — client-view (timeout, no TCP reset) + server-view (no request in access log, health
probe healthy). Not multi-node framing. Severity / Blast Radius.

D-phase after all C-phase columns complete:
Recovery Path: **Step 1d, Class 1** (Rule B — cite by label). Actor-chain ≥3 stages.
Named Verification Signal per stage. Chaos Block: inject connectivity loss / Expected Behavior
/ Pass Signal / Fail Signal.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column —
including Failure Signature with ≥2 Class 1 actor viewpoints, Status Quo Risk citing Step 1b
Class 1 by label with acute branches and three-component chronic, all four Recovery Path stages
with actor-chain mechanism, SLA from Step 1d Class 1 by label (Rule B), and named Verification
Signal — AND Row 1 Chaos Test Block is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first, then D-phase.

Trigger Condition: quantified downstream-service degradation threshold + detection signal.
State: upstream service available; downstream payment service degraded. Capability:
browse/cart available; checkout submission blocked or queued. Data at Risk: inventory
reservation drift, unconfirmed orders, oversell risk. Status Quo Risk: **Step 1b, Class 2**
(Rule B). Acute: phantom hold / oversell on silent drop. Chronic: named metric accumulates
per-deploy unbounded from Step 1b, Class 2. Failure Signature: **Class 2 — transaction-level
anomaly** (single write path). Client-view + server-view + transaction-boundary view. No
node-A / node-B framing. Severity / Blast Radius.

D-phase: Recovery Path **Step 1d, Class 2** (Rule B — cite by label). Actor-chain. Named VS.
Chaos Block: inject downstream failure / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete, including Class 2
transaction-level Failure Signature with ≥2 actor viewpoints, Status Quo Risk citing Step 1b
Class 2 by label, Recovery Path SLA citing Step 1d Class 2 by label per Rule B.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

Trigger Condition: replication lag threshold + dual-write conflict counter detection signal.
State: partition active, both nodes accepting independent writes. Capability: checkout available
on both partition sides; conflict invisible to users. Data at Risk: diverging inventory counts,
duplicate fulfillment orders, double-charge risk. Status Quo Risk: **Step 1b, Class 3** (Rule B).
Acute: `last-write-wins` / `manual-reconcile`. Chronic: duplicate-charge events compound
per-transaction indefinitely from Step 1b, Class 3. Failure Signature: **Class 3 — node-A /
node-B diverging state**. Not single-transaction. Conflict Resolution: canonical label +
adequacy judgment referencing vocabulary constraint. Severity / Blast Radius.

D-phase: Recovery Path **Step 1d, Class 3** (Rule B — cite by label). Actor-chain. Named VS.
Chaos Block: inject partition / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Block are complete,
including Failure Signature with Class 3 node-A/node-B framing, Conflict Resolution with
canonical label and adequacy judgment, Recovery Path SLA citing Step 1d Class 3 by label.**

---

### Gap Register

Three findings inline — no separate observability section, no standalone observability table:

**Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

HIGH / MEDIUM / LOW + strongest argument against deferral (2–3 sentences), naming gap findings
and Step 1b carrying costs as inputs.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3

---

## V-02 — Single-Axis: Dedicated Bidirectional Cross-Reference Sub-Bullets at L1 and L2

**Axis**: C-56 closure via dedicated labeled cross-reference sub-bullets at both L1 and L2.
Rather than appending the forward reference as a parenthetical in L1's header text, L1 carries
a structured "→ Cross-reference forward" line as a sub-bullet within the blockquote body. L2
carries a reciprocal "→ Cross-reference backward" line. Both lines name the other element by
label explicitly. All other structure is V-03 R18 verbatim.

**Hypothesis**: Dedicated cross-reference sub-bullets are structurally more explicit than an
inline parenthetical — a scorer reading either element finds a clearly labeled cross-reference
line pointing to the other by name. This removes any ambiguity about whether the parenthetical
in V-01's L1 header constitutes a named cross-reference or merely a restatement label. Both
elements carry explicit bidirectional pointers. C-56 passes unambiguously.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic} across three structurally distinct failure classes and produce a
complete failure analysis with a Gap Register, Inertia Verdict, and Finding Completeness
Checklist.

### Role Declaration

Two roles fill all scenario columns.

**C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk,
Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy.

**D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block.

> **D-Phase Enforcement Note — Enforcement Instance 1 of 4 (originating declaration)**:
> The Recovery Path column requires SLA targets drawn from the pre-committed SLA Budget
> (Step 1d) of the Pre-Commitment Document below. Independently authoring SLA values per
> scenario row without referencing Step 1d is a **named contract violation**.
>
> → **Cross-reference forward**: this originating declaration is restated as Enforcement
> Instance 2 of 4 in the Document Enforcement Contract preamble below.
>
> This is Enforcement Instance 1 of 4 — the originating declaration. It is restated at
> Enforcement Instance 2 (preamble), Instance 3 (sub-part), and Instance 4 (column contract).

---

### Pre-Commitment Document: Resilience Commitment Matrix

**Document Enforcement Contract — Enforcement Instance 2 of 4** (governing §§ 1a through 1d
— read before filling any sub-part):

> → **Cross-reference backward**: this preamble restates the constraint from Enforcement
> Instance 1 of 4 — the D-Phase Enforcement Note above, which is the originating declaration.
>
> This document pre-commits authoritative values for the scenario table.
>
> **Rule A — No Deferral**: Any cell left blank, "TBD", "N/A", or equivalent unfilled value
> in any sub-part of this document fails the pre-commitment requirement. Every cell must carry
> an actual value at authoring time.
>
> **Rule B — No Per-Row Invention**: Each sub-part is the authoritative source for its
> corresponding scenario column. Independently authoring per-row values not drawn from the
> corresponding sub-part is a named contract violation. Row fills must reference the source
> sub-part by label.
>
> Both rules govern §§ 1a through 1d. This preamble is Enforcement Instance 2 of 4.

---

**Step 1a — Domain Fragility Framing**

Write 2–3 sentences establishing {topic}'s structural fragility across the three failure classes.
Domain-specific framing required. Cover: client isolation creates invisible pending-state windows;
idempotency gaps create retry-duplication risk; concurrent partition writes require pre-specified
merge rules.

**Step 1b — Per-Class Carrying Costs**

Status Quo Risk fills reference this sub-part as "Step 1b, Class N".
**Rule A applies (Enforcement Instance 3 of 4 reinforced here)** — no blank cells. **Rule B
applies** — Status Quo Risk fills must cite "Step 1b, Class N"; per-row invention is a contract
violation.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [named metric] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [named metric] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [named metric] | per-transaction | compound growth |

**Step 1c — Per-Class Tipping Point Signals**

**Rule A applies** — quantified threshold expression + named detection metric required per class.
"Worsens over time" is not quantified and fails Rule A.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [quantified threshold + detection signal] | [metric] |
| 2 | [quantified threshold + detection signal] | [metric] |
| 3 | [quantified threshold + detection signal] | [metric] |

**Step 1d — SLA Budget** — Enforcement Instance 3 of 4

**Rule A applies** — no blank cells. All twelve cells must carry actual time values at authoring.
**Rule B applies** — Recovery Path SLA fills must cite "Step 1d, Class N, stage column";
independently authored per-row SLA values are a contract violation.

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

**Section Order Requirement**: (1) Pre-Commitment Document — all four sub-parts; (2) Scenario
Table — row N scenario columns AND row N Chaos Test Block before row N+1; (3) Gap Register with
three inline findings; (4) Inertia Verdict; (5) Finding Completeness Checklist. **Do not advance
to row N+1 until row N columns AND Chaos Block are both complete. Do not advance to the Gap
Register until all three rows and all three Chaos Blocks are complete.**

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
| Status Quo Risk | C | **Reference Step 1b, Class N (Rule B — not independently authored)**. Acute branches (A/B) before chronic metric. Three-component chronic: rate + horizon + metric from Step 1b. |
| Failure Signature | C | Behavioral fingerprint per actor during failure. ≥2 named actor viewpoints. Distinct from Trigger Condition and from State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | Detect → Contain → Recover → Validate. Per stage: actor-chain prefix + mechanism + **SLA from Step 1d, Class N, stage column — Enforcement Instance 4 of 4 (restated for co-location at column-contract level): any SLA value not drawn from Step 1d is a named contract violation** + named Verification Signal. ≥3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage confirming stage completion. Distinct from mechanism. |
| Chaos Block | D | Four components co-located with this row: Inject / Expected Behavior / Pass Signal / Fail Signal. Not a separate section. Not a standalone table. |

#### Failure Signature Class Boundary Discriminator

> **Class 2**: Transaction-level anomaly from a single write path. No inter-node divergence
> framing. Node-A / node-B framing is incorrect for Class 2.
>
> **Class 3**: Node-A / node-B framing showing two nodes holding diverging last-write state
> simultaneously. Single-transaction framing is incorrect for Class 3.
>
> Generic fills satisfying either class without the class-specific structural signature fail.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`.
Class 3 row must apply a canonical label with adequacy judgment citing this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first. Produce all C-phase columns before D-phase columns.

Trigger Condition: quantified connectivity threshold + detection signal. State: client isolation
at failure onset — name {topic} components affected. Capability: offline-available operations
named. Data at Risk: in-flight cart, pending payment intent, unsubmitted order records. Status
Quo Risk: **Step 1b, Class 1** (Rule B — cite label). Acute: cart dropped / cart stale-restored.
Chronic: rate + horizon + metric from Step 1b, Class 1. Failure Signature: Class 1 — client-view
+ server-view. Not multi-node. Severity / Blast Radius.

D-phase: Recovery Path **Step 1d, Class 1** (Rule B — cite by label). Actor-chain ≥3 stages.
Named VS per stage. Chaos Block: inject / expected / pass / fail.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column including
all four Recovery Path stages with actor-chain mechanism, SLA from Step 1d Class 1 by label, and
named Verification Signal — AND Row 1 Chaos Test Block is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first, then D-phase.

Failure Signature: **Class 2 — transaction-level anomaly** (single write path). Not inter-node.
Trigger Condition, State, Capability, Data at Risk. Status Quo Risk: **Step 1b, Class 2**
(Rule B). Acute / chronic. Severity / Blast Radius.
D-phase: Recovery Path **Step 1d, Class 2** (Rule B). Actor-chain. Named VS. Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete, including Class 2
transaction-level Failure Signature and Recovery Path SLA citing Step 1d Class 2 by label.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

Failure Signature: **Class 3 — node-A / node-B diverging state**. Not single-transaction.
Status Quo Risk: **Step 1b, Class 3** (Rule B). Conflict Resolution: canonical label + adequacy
judgment. Severity / Blast Radius.
D-phase: Recovery Path **Step 1d, Class 3** (Rule B). Actor-chain. Named VS. Chaos Block.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Block are complete.**

---

### Gap Register

Three findings inline — no separate observability section, no standalone observability table:

**Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

HIGH / MEDIUM / LOW + strongest argument against deferral (2–3 sentences), naming gap findings
and Step 1b carrying costs as inputs.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3

---

## V-03 — Single-Axis: Phrasing Register Shift — "Enforcement Clause K/N" Compact Notation

**Axis**: Phrasing register. All "Enforcement Instance K of N" text is replaced with
"Enforcement Clause K/N" throughout. The mutual reference is implemented the same way as V-01
(forward-pointer parenthetical in L1). Register shifts from descriptive ("Instance") to
legal-contract ("Clause"); notation shifts from "K of N" to "K/N" (more compact).

**Hypothesis**: "Enforcement Clause" is conventional in contract-law writing and may produce
a stronger behavioral cue than "Enforcement Instance". The compact "K/N" notation is less
verbose. This variation tests whether rubric criteria bind on structural position and mutual-
reference completeness rather than on specific terminology — Clause 1/4 and Instance 1 of 4
are structurally equivalent. All three new criteria should pass identically to V-01.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic} across three structurally distinct failure classes and produce a
complete failure analysis with a Gap Register, Inertia Verdict, and Finding Completeness
Checklist.

### Role Declaration

Two roles fill all scenario columns.

**C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk,
Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy.

**D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block.

> **D-Phase Enforcement Note — Enforcement Clause 1/4 (originating declaration; restated
> as Enforcement Clause 2/4 in the Document Enforcement Contract preamble below)**: The
> Recovery Path column requires SLA targets drawn from the pre-committed SLA Budget (Step 1d)
> of the Pre-Commitment Document below. Independently authoring SLA values per scenario row
> without referencing Step 1d is a **named contract violation**. This is the originating
> clause; it is restated at three additional enforcement levels within the pre-commitment
> document and column contract.

---

### Pre-Commitment Document: Resilience Commitment Matrix

**Document Enforcement Contract — Enforcement Clause 2/4** (governing §§ 1a through 1d —
read before filling any sub-part) *(restated from D-Phase Enforcement Note above, which is
Enforcement Clause 1/4 — the originating declaration)*:

> This document pre-commits authoritative values for the scenario table.
>
> **Rule A — No Deferral**: Any cell left blank, "TBD", "N/A", or equivalent unfilled value
> in any sub-part of this document fails the pre-commitment requirement. Every cell must carry
> an actual value at authoring time.
>
> **Rule B — No Per-Row Invention**: Each sub-part is the authoritative source for its
> corresponding scenario column. Independently authoring per-row values not drawn from the
> corresponding sub-part is a named contract violation. Row fills must reference the source
> sub-part by label.
>
> Both rules govern §§ 1a through 1d. This preamble is Enforcement Clause 2/4.

---

**Step 1a — Domain Fragility Framing**

Write 2–3 sentences establishing {topic}'s structural fragility across the three failure classes.
Domain-specific framing required. Cover: client isolation creates invisible pending-state windows;
idempotency gaps create retry-duplication risk; concurrent partition writes require pre-specified
merge rules.

**Step 1b — Per-Class Carrying Costs**

Status Quo Risk fills reference this sub-part as "Step 1b, Class N".
**Rule A applies (Enforcement Clause 3/4 reinforced here)** — no blank cells. **Rule B
applies** — Status Quo Risk fills must cite "Step 1b, Class N"; per-row invention is a contract
violation.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [named metric] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [named metric] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [named metric] | per-transaction | compound growth |

**Step 1c — Per-Class Tipping Point Signals**

**Rule A applies** — quantified threshold expression + named detection metric required per class.
"Worsens over time" is not quantified and fails Rule A.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [quantified threshold + detection signal] | [metric] |
| 2 | [quantified threshold + detection signal] | [metric] |
| 3 | [quantified threshold + detection signal] | [metric] |

**Step 1d — SLA Budget** — Enforcement Clause 3/4

**Rule A applies** — no blank cells. All twelve cells must carry actual time values at authoring.
**Rule B applies** — Recovery Path SLA fills must cite "Step 1d, Class N, stage column";
independently authored per-row SLA values are a contract violation.

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

**Section Order Requirement**: (1) Pre-Commitment Document — all four sub-parts; (2) Scenario
Table — row N columns AND Chaos Block before row N+1; (3) Gap Register with three inline
findings; (4) Inertia Verdict; (5) Finding Completeness Checklist. **Do not advance to row N+1
until row N columns AND Chaos Block are both complete. Do not advance to the Gap Register until
all three rows and all three Chaos Blocks are complete.**

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
| Status Quo Risk | C | **Reference Step 1b, Class N (Rule B — not independently authored)**. Acute branches (A/B) before chronic metric. Three-component chronic: rate + horizon + metric from Step 1b. |
| Failure Signature | C | Behavioral fingerprint per actor during failure. ≥2 named actor viewpoints. Distinct from Trigger Condition and from State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | Detect → Contain → Recover → Validate. Per stage: actor-chain prefix + mechanism + **SLA from Step 1d, Class N, stage column — Enforcement Clause 4/4 (restated for co-location at column-contract level): any SLA value not drawn from Step 1d is a named contract violation** + named Verification Signal. ≥3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage confirming stage completion. Distinct from mechanism. |
| Chaos Block | D | Four components co-located with this row: Inject / Expected Behavior / Pass Signal / Fail Signal. Not a separate section. Not a standalone table. |

#### Failure Signature Class Boundary Discriminator

> **Class 2**: Transaction-level anomaly from a single write path. No inter-node divergence
> framing. Node-A / node-B framing is incorrect for Class 2.
>
> **Class 3**: Node-A / node-B framing showing two nodes holding diverging last-write state.
> Single-transaction framing is incorrect for Class 3.
>
> Generic fills satisfying either class without the class-specific structural signature fail.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`.
Class 3 row must apply a canonical label with adequacy judgment citing this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first. Produce all C-phase columns before D-phase columns.

Trigger Condition: quantified connectivity threshold + detection signal. State: client isolation
at failure onset. Capability: offline-available operations named. Data at Risk: in-flight cart,
pending payment intent, unsubmitted order records. Status Quo Risk: **Step 1b, Class 1**
(Rule B). Acute: cart dropped / cart stale-restored. Chronic: rate + horizon + metric from
Step 1b, Class 1. Failure Signature: Class 1 — client-view + server-view. Not multi-node.
Severity / Blast Radius.

D-phase: Recovery Path **Step 1d, Class 1** (Rule B — cite by label). Actor-chain ≥3 stages.
Named VS per stage. Chaos Block: inject / expected / pass / fail.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column
including all four Recovery Path stages with actor-chain mechanism, SLA from Step 1d Class 1
by label, and named Verification Signal — AND Row 1 Chaos Test Block is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first, then D-phase.

Failure Signature: **Class 2 — transaction-level anomaly** (single write path). Not inter-node.
Trigger Condition, State, Capability, Data at Risk. Status Quo Risk: **Step 1b, Class 2**
(Rule B). Acute / chronic. Severity / Blast Radius.
D-phase: Recovery Path **Step 1d, Class 2** (Rule B). Actor-chain. Named VS. Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

Failure Signature: **Class 3 — node-A / node-B diverging state**. Not single-transaction.
Status Quo Risk: **Step 1b, Class 3** (Rule B). Conflict Resolution: canonical + adequacy
judgment. Severity / Blast Radius.
D-phase: Recovery Path **Step 1d, Class 3** (Rule B). Actor-chain. Named VS. Chaos Block.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Block are complete.**

---

### Gap Register

Three findings inline — no separate observability section, no standalone observability table:

**Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

HIGH / MEDIUM / LOW + strongest argument against deferral (2–3 sentences), naming gap findings
and Step 1b carrying costs as inputs.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3

---

## V-04 — Combined: §0-Form Document-Header + Sequential Instance Labels Everywhere + Mutual Reference

**Axes**: Two axes combined. (A) Document-header element form: a named "§0 — Enforcement
Mandate" section positioned before the pre-commitment document, as a section heading (not a
D-Phase blockquote inside the role declaration). (B) All four enforcement locations carry
"Enforcement Instance K of 4" sequential count labels. (C) Mutual cross-reference: §0 carries
"(originating declaration)" and names "§1 Enforcement Contract preamble" as Instance 2 of 4;
§1 preamble carries backward reference naming "§0 above" as Instance 1 of 4.

**Hypothesis**: A named section heading (§0) is a structurally stronger document-header element
than a D-Phase note blockquote — it is discoverable by label, not just by position. Adding
Instance K of 4 labels at all four §0-form locations satisfies C-54; §0 carrying "(originating
declaration)" satisfies C-55; §0 naming §1 preamble + §1 preamble naming §0 satisfies C-56.
This combines V-02 R18's bidirectional §0/preamble structure with V-03 R18's sequential count
labels. All three new criteria pass simultaneously.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic} across three structurally distinct failure classes and produce a
complete failure analysis with a Gap Register, Inertia Verdict, and Finding Completeness
Checklist.

### Role Declaration

Two roles fill all scenario columns.

**C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk,
Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy.

**D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block.

---

### §0 — Enforcement Mandate — Enforcement Instance 1 of 4 *(originating declaration; restated as Enforcement Instance 2 of 4 in the §1 Enforcement Contract preamble below)*

> Distributed Systems Expert: the Recovery Path column requires SLA targets drawn from the
> pre-committed SLA Budget (§1d) of the Pre-Commitment Document below. Independently authoring
> SLA values per scenario row without referencing §1d is a **named contract violation** declared
> at document-header scope. This §0 clause is Enforcement Instance 1 of 4 — the originating
> declaration. It is restated at Enforcement Instance 2 of 4 (§1 Enforcement Contract preamble),
> Instance 3 of 4 (§1b and §1d sub-parts), and Instance 4 of 4 (Column Contract Recovery Path
> entry).

---

### Pre-Commitment Document: Resilience Commitment Matrix

**§1 — Enforcement Contract — Enforcement Instance 2 of 4** (governing §§ 1a through 1d —
read before filling any sub-part) *(§0 above is Enforcement Instance 1 of 4 — the originating
declaration)*:

> This document pre-commits authoritative values for the scenario table.
>
> **Rule A — No Deferral**: Any cell left blank, "TBD", "N/A", or equivalent unfilled value
> in any sub-part of this document fails the pre-commitment requirement. Every cell must carry
> an actual value at authoring time.
>
> **Rule B — No Per-Row Invention** *(§0 above restates this rule at document-header scope as
> Enforcement Instance 1 of 4)*: Each sub-part is the authoritative source for its corresponding
> scenario column. Independently authoring per-row values not drawn from the corresponding
> sub-part is a named contract violation. Row fills must reference the source sub-part by label.
>
> Both rules govern §§ 1a through 1d. This §1 preamble is Enforcement Instance 2 of 4.

---

**§1a — Domain Fragility Framing**

Write 2–3 sentences establishing {topic}'s structural fragility across the three failure classes.
Domain-specific framing required. Cover: client isolation creates invisible pending-state windows;
idempotency gaps create retry-duplication risk; concurrent partition writes require pre-specified
merge rules.

**§1b — Per-Class Carrying Costs**

Status Quo Risk fills reference this sub-part as "§1b, Class N".
**Rule A applies (Enforcement Instance 3 of 4 reinforced here)** — no blank cells. **Rule B
applies** — Status Quo Risk fills must cite "§1b, Class N"; per-row invention is a contract
violation.

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

**§1d — SLA Budget** — Enforcement Instance 3 of 4

**Rule A applies** — no blank cells. All twelve cells must carry actual time values at authoring.
**Rule B applies** — Recovery Path SLA fills must cite "§1d, Class N, stage column";
independently authored per-row SLA values are a contract violation.

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

**Section Order Requirement**: (1) §0 and Pre-Commitment Document complete — all four §1
sub-parts; (2) Scenario Table — row N scenario columns AND row N Chaos Test Block before row
N+1; (3) Gap Register with three inline findings; (4) Inertia Verdict; (5) Finding Completeness
Checklist. **Do not advance to row N+1 until row N columns AND Chaos Block are both complete.
Do not advance to the Gap Register until all three rows and all three Chaos Blocks are complete.**

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
| Recovery Path | D | Detect → Contain → Recover → Validate. Per stage: actor-chain prefix + mechanism + **SLA from §1d, Class N, stage column — Enforcement Instance 4 of 4 (restated for co-location at column-contract level): any SLA value not drawn from §1d is a named contract violation** + named Verification Signal. ≥3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage confirming stage completion. Distinct from mechanism. |
| Chaos Block | D | Four components co-located with this row: Inject / Expected Behavior / Pass Signal / Fail Signal. Not a separate section. Not a standalone table. |

#### Failure Signature Class Boundary Discriminator

> **Class 2**: Transaction-level anomaly from a single write path. No inter-node divergence
> framing. Node-A / node-B framing is incorrect for Class 2.
>
> **Class 3**: Node-A / node-B framing showing two nodes holding diverging last-write state.
> Single-transaction framing is incorrect for Class 3.
>
> Generic fills satisfying either class without the class-specific structural signature fail.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`.
Class 3 row must apply a canonical label with adequacy judgment citing this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first. Produce all C-phase columns before D-phase columns.

Trigger Condition: quantified connectivity threshold + detection signal. State: client isolation
at failure onset — name {topic} components affected. Capability: offline-available operations
named. Data at Risk: in-flight cart, pending payment intent, unsubmitted order records. Status
Quo Risk: **§1b, Class 1** (Rule B — cite label). Acute: cart dropped / cart stale-restored.
Chronic: rate + horizon + metric from §1b, Class 1. Failure Signature: Class 1 — client-view
+ server-view. Not multi-node. Severity / Blast Radius.

D-phase: Recovery Path **§1d, Class 1** (Rule B — Enforcement Instance 4 of 4 — cite by label).
Actor-chain ≥3 stages. Named VS per stage. Chaos Block: inject / expected / pass / fail.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column
including all four Recovery Path stages with actor-chain mechanism, SLA from §1d Class 1
by label, and named Verification Signal — AND Row 1 Chaos Test Block is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first, then D-phase.

Failure Signature: **Class 2 — transaction-level anomaly** (single write path). Not inter-node.
Trigger Condition, State, Capability, Data at Risk. Status Quo Risk: **§1b, Class 2** (Rule B).
Acute / chronic. Severity / Blast Radius.
D-phase: Recovery Path **§1d, Class 2** (Rule B — cite by label). Actor-chain. Named VS. Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete, including Class 2
transaction-level Failure Signature and Recovery Path SLA citing §1d Class 2 by label.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

Failure Signature: **Class 3 — node-A / node-B diverging state**. Not single-transaction.
Status Quo Risk: **§1b, Class 3** (Rule B). Conflict Resolution: canonical label + adequacy
judgment. Severity / Blast Radius.
D-phase: Recovery Path **§1d, Class 3** (Rule B — cite by label). Actor-chain. Named VS. Chaos Block.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Block are complete.**

---

### Gap Register

Three findings inline — no separate observability section, no standalone observability table:

**Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

HIGH / MEDIUM / LOW + strongest argument against deferral (2–3 sentences), naming gap findings
and §1b carrying costs as inputs.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3

---

## V-05 — Combined: §0-Form + Sequential Instances + Mutual Reference + Lifecycle Emphasis + Structured Inertia

**Axes**: All of V-04's synthesis, plus two additional axes. (D) Lifecycle emphasis: each Row
Descriptor's D-phase instruction explicitly cites the Enforcement Instance chain — "Recovery
Path: §1d, Class N (Rule B — Enforcement Instance 4 of 4 applies — cite by label)"; the Section
Order Requirement names enforcement instances in the sequencing prohibition. (E) Inertia framing:
the Inertia Verdict section carries a structured four-component template (urgency label + carrying
cost citation + gap finding count + escalation recommendation) rather than free-form prose.

**Hypothesis**: Per-row enforcement instance invocation within row descriptors reinforces the
cascade at the point of filling — a model constructing Row 2 D-phase content encounters the
"Enforcement Instance 4 of 4 applies" reminder at the exact moment it might otherwise invent
an SLA value. Structured inertia framing ensures the verdict is actionable (names an owner,
names a deadline, names a metric threshold) rather than evaluative-only. Both axes add behavioral
specificity without changing the enforcement structure.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic} across three structurally distinct failure classes and produce a
complete failure analysis with a Gap Register, Inertia Verdict, and Finding Completeness
Checklist.

### Role Declaration

Two roles fill all scenario columns.

**C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk,
Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy.

**D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block.

---

### §0 — Enforcement Mandate — Enforcement Instance 1 of 4 *(originating declaration; restated as Enforcement Instance 2 of 4 in the §1 Enforcement Contract preamble below)*

> Distributed Systems Expert: the Recovery Path column requires SLA targets drawn exclusively
> from the pre-committed SLA Budget (§1d) of the Pre-Commitment Document below. Independently
> authoring SLA values per scenario row without referencing §1d is a **named contract
> violation** at document-header scope. This §0 mandate is Enforcement Instance 1 of 4 — the
> originating declaration for this constraint. The constraint is restated at Enforcement
> Instance 2 of 4 (§1 Enforcement Contract preamble below), Instance 3 of 4 (§1b and §1d
> sub-parts), and Instance 4 of 4 (Column Contract Recovery Path entry).

---

### Pre-Commitment Document: Resilience Commitment Matrix

**§1 — Enforcement Contract — Enforcement Instance 2 of 4** (governing §§ 1a through 1d —
read before filling any sub-part) *(§0 above is Enforcement Instance 1 of 4 — the originating
declaration)*:

> This document pre-commits authoritative values for the scenario table.
>
> **Rule A — No Deferral**: Any cell left blank, "TBD", "N/A", or equivalent unfilled value
> in any sub-part of this document fails the pre-commitment requirement. Every cell must carry
> an actual value at authoring time.
>
> **Rule B — No Per-Row Invention** *(§0 above restates this rule at document-header scope as
> Enforcement Instance 1 of 4)*: Each sub-part is the authoritative source for its corresponding
> scenario column. Independently authoring per-row values not drawn from the corresponding
> sub-part is a named contract violation. Row fills must reference the source sub-part by label.
>
> Both rules govern §§ 1a through 1d. This §1 preamble is Enforcement Instance 2 of 4.

---

**§1a — Domain Fragility Framing**

Write 2–3 sentences establishing {topic}'s structural fragility across the three failure classes.
Domain-specific framing required — generic distributed-systems boilerplate fails. Cover: client
isolation creates invisible pending-state windows; idempotency gaps create retry-duplication side
effects; concurrent partition writes create state divergence requiring pre-specified merge rules
to avoid duplicate fulfillment or double-charge.

**§1b — Per-Class Carrying Costs**

Status Quo Risk fills reference this sub-part as "§1b, Class N".
**Rule A applies (Enforcement Instance 3 of 4 reinforced here)** — no blank cells, no TBD, no
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

**§1d — SLA Budget** — Enforcement Instance 3 of 4

**Rule A applies** — no blank cells. All twelve cells must carry actual time values at authoring.
**Rule B applies** — Recovery Path SLA fills must cite "§1d, Class N, stage column" by label;
independently authored per-row SLA values are a named contract violation at the column-contract
level (Enforcement Instance 4 of 4).

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
sub-parts complete (Enforcement Instances 3 of 4 satisfied at §1b and §1d); (3) Scenario Table
— row N scenario columns AND row N Chaos Test Block before row N+1; (4) Gap Register with three
inline findings; (5) Inertia Verdict; (6) Finding Completeness Checklist. **Do not advance to
row N+1 until row N columns AND Chaos Block are both complete — Rule B (Enforcement Instance 4
of 4) applies to every D-phase Recovery Path fill. Do not advance to the Gap Register until all
three rows and all three Chaos Blocks are complete.**

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
| Recovery Path | D | Detect → Contain → Recover → Validate. Per stage: actor-chain prefix (`client ->`, `server ->`, `operator ->`, `user ->`) + mechanism + **SLA from §1d, Class N, stage column — Enforcement Instance 4 of 4 (restated for co-location at column-contract level): any SLA value not drawn from §1d is a named contract violation** + named Verification Signal. ≥3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage confirming stage completion. Distinct from mechanism. |
| Chaos Block | D | Four components co-located with this row: Inject (named reproducible condition) / Expected Behavior / Pass Signal / Fail Signal. Not a separate section. Not a standalone table. |

#### Failure Signature Class Boundary Discriminator

> **Class 2**: Transaction-level anomaly from a single write path. Observable at the transaction
> boundary. No inter-node divergence framing. Node-A / node-B framing is incorrect for Class 2.
>
> **Class 3**: Node-A / node-B framing showing two nodes holding diverging last-write state
> simultaneously. Single-transaction framing is incorrect for Class 3.
>
> Generic fills satisfying either class without the class-specific structural signature fail
> even with multiple actor viewpoints.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`.
Free-text paraphrase fails. Class 3 row must apply a canonical label with adequacy judgment
citing this constraint.

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
Recovery Path: **§1d, Class 1** — Rule B — **Enforcement Instance 4 of 4 applies** — cite by
label; any SLA value not drawn from §1d Class 1 is a named contract violation. Actor-chain
≥3 stages. Named Verification Signal per stage.
Chaos Block: inject connectivity loss / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column —
including Failure Signature with ≥2 Class 1 actor viewpoints, Status Quo Risk citing §1b
Class 1 by label with acute branches and three-component chronic, all four Recovery Path stages
with actor-chain mechanism, SLA from §1d Class 1 by label (Enforcement Instance 4 of 4), and
named Verification Signal — AND Row 1 Chaos Test Block is complete.**

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

D-phase: Recovery Path **§1d, Class 2** — Rule B — **Enforcement Instance 4 of 4 applies** —
cite by label. Actor-chain. Named VS.
Chaos Block: inject downstream failure / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete, including Class 2
transaction-level Failure Signature with ≥2 actor viewpoints, Status Quo Risk citing §1b Class 2
by label, and Recovery Path SLA citing §1d Class 2 by label (Enforcement Instance 4 of 4).**

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

D-phase: Recovery Path **§1d, Class 3** — Rule B — **Enforcement Instance 4 of 4 applies** —
cite by label. Actor-chain. Named VS.
Chaos Block: inject partition / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Block are complete,
including Class 3 node-A/node-B Failure Signature, canonical Conflict Resolution label with
adequacy judgment, and Recovery Path SLA citing §1d Class 3 by label.**

---

### Gap Register

Three findings inline — no separate observability section, no standalone observability table:

**Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

Structure the verdict using four components:

1. **Urgency label**: HIGH / MEDIUM / LOW
2. **Carrying cost citation**: name the specific §1b Class N carrying cost driving the
   urgency — rate + horizon + metric
3. **Gap finding count**: state how many of the three finding types are present and which
   finding creates the highest compounding risk
4. **Escalation recommendation**: name the owner, the threshold that triggers action, and
   the consequence of missing that threshold

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3
