# Flow-Resilience Skill — Round 18 Variations (Rubric v17)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual consistency.
**Rubric**: v17 (C-01 through C-50, 8 essential/recommended + 42 aspirational)
**Date**: 2026-03-15

---

## Round 18 Context

**Rubric ceiling entering R18**: 84/84 (V-01/V-02/V-03/V-04 tied at perfect ceiling); V-05 at 82/84 (C-49 FAIL).

**Open criterion entering R18**: **C-49 for V-05** — enforcement contract pre-positioned before all sub-parts with inline named-label citations in each sub-part.

**R17 root cause for V-05 C-49 FAIL**:
- V-05 R17 uses `§ 0 — D-Phase Pre-Commitment Constraint` in the Role Declaration section, pre-announcing Rule B *before* the enforcement contract block. The contract is not the originating declaration.
- Additionally, `§ 1a` in V-05 R17 carries no inline named-label citations, leaving one sub-part without inline reinforcement.
- Combined effect: enforcement contract is not the unambiguous pre-positioned rule source; sub-part coverage is incomplete.

**R18 synthesis path for V-05**:
- Eliminate the preceding `§ 0`; fold D-phase scope into the enforcement contract itself.
- Add explicit self-attestation: "(positioned before all sub-parts — read before filling any of Steps 1a through 1d)".
- Add `**Rule A applies**` / `**Rule B applies**` inline citations to EVERY sub-part including Step 1a.
- Maintain inertia framing axis (most prominent status-quo competitor language of any variation).

**Variation axes selected**:
- V-01: Single axis — Role sequence: Commerce Expert listed first in Role Declaration; D-Phase Enforcement Note positioned under Commerce Expert's fill scope at document-header scope.
- V-02: Single axis — Output format: Sub-parts 1a–1c condensed into a pre-commitment assessment table with explicit "Rule Constraint" column carrying inline citations per row.
- V-03: Single axis — Lifecycle emphasis: Recovery Path Column Contract specifies each stage (Detect/Contain/Recover/Validate) as a discrete named entry with its own Rule B restatement label — fourth enforcement hierarchy level.
- V-04: Single axis — Phrasing register: Formal §-numbered statute style; enforcement contract as "§ 1 — Enforcement Mandate" with "§ 1.1" / "§ 1.2" labels; inline citations use section-number form.
- V-05: Inertia framing axis + C-49 fix: Most prominent status-quo competitor framing; contract has explicit pre-positioning self-attestation; every sub-part (1a through 1d) carries inline named-label citations; no preceding §0.

**Expected R18 discrimination under v17:**

| Rank | Variation | C-48 | C-49 | C-50 | Uncapped Asp. |
|------|-----------|------|------|------|--------------|
| 1 (tie) | **V-01** | PASS | PASS | PASS | **84/84** |
| 1 (tie) | **V-02** | PASS | PASS | PASS | **84/84** |
| 1 (tie) | **V-03** | PASS | PASS | PASS | **84/84** |
| 1 (tie) | **V-04** | PASS | PASS | PASS | **84/84** |
| 1 (tie) | **V-05** | PASS | PASS | PASS | **84/84** |

V-05 achieves C-49 PASS via: (1) self-attestation in contract header, (2) inline citations in every sub-part including Step 1a, (3) removal of preceding §0 that undermined contract pre-positioning. If all five reach 84/84 simultaneously, this is the second five-way perfect tie at the ceiling in this series.

**Open for R19**: Extract new criteria from R18 excellence signals. Candidate: V-03's per-stage Rule B restatement labels at stage granularity (four-level enforcement chain at stage-specification level).

---

## V-01

**Variation axis**: Role sequence — Commerce Expert is listed first in the Role Declaration. The D-Phase Enforcement Note appears as a document-header-scope annotation under the Commerce Expert block, making the pre-commitment enforcement signal commerce-first. Enforcement contract retains Rule A / Rule B labels. All sub-parts carry inline citations. C-50 hierarchy: Commerce Expert Enforcement Note (Level 1, document header) → Document Enforcement Contract (Level 2, preamble) → Column Contract Recovery Path "(restated for co-location)" (Level 3).

**Hypothesis**: R17 variations list Commerce Expert first but attach the D-Phase Enforcement Note to the DS Expert block. Moving the enforcement note to the Commerce Expert block creates an enforcement signal that commerce-domain scorers encounter first. C-49 PASS maintained (contract before 1a–1d with inline citations in every sub-part), C-50 PASS (Level 1 at Commerce Expert header, Level 2 at preamble, Level 3 at column contract). Expected: 84/84.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded conditions for `{topic}` across three structurally distinct failure classes, and produce a complete four-field failure analysis per class, a Gap Register with inline observability, and an Inertia Verdict.

### Role Declaration

Two roles fill all scenario columns.

**C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk, Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy.

> **Commerce-Phase Pre-Commitment Note**: The Status Quo Risk column for every scenario row must reference the per-class carrying cost declared in Step 1b of the Pre-Commitment Document below — specifically citing "Step 1b, Class N". Independently authoring carrying costs per scenario row without this reference is a named contract violation under Rule B of the Document Enforcement Contract. This note is declared here at document scope so it is encountered before any fill instruction.

**D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block.

---

### Pre-Commitment Document: Resilience Commitment Matrix

**Document Enforcement Contract** (positioned before all sub-parts — read before filling any of Steps 1a through 1d):

> This document pre-commits authoritative values for the scenario table. Two rules govern all fills:
>
> **Rule A — No Deferral**: Writing "TBD", leaving any cell blank, or using "N/A" or any equivalent unfilled value in any sub-part of this document is a named contract violation. The pre-commitment is void if any cell is deferred. Every cell must carry an actual value at authoring time.
>
> **Rule B — No Per-Row Invention**: Each sub-part is the sole authoritative source for its corresponding scenario column. Independently authoring per-row values not drawn from the corresponding sub-part is a named contract violation. Row fills must cite the source sub-part by its label (e.g., "Step 1b, Class 2" or "Step 1d, Class 3, TTR column"). A fill introducing a value not present in the referenced sub-part is a contract violation regardless of numerical plausibility.
>
> Rule A closes the placeholder-deferral escape. Rule B closes the per-row reinvention escape. Both rules govern Steps 1a through 1d.

---

**Step 1a — Domain Fragility Framing**

Write 2–3 sentences establishing why `{topic}` in commerce is inherently fragile across all three failure classes. Specific to this domain — not generic distributed systems boilerplate. Cover: client isolation creates invisible pending-state windows; distributed writes without idempotency guarantees produce duplicate side effects on retry; concurrent partition writes create state divergence requiring pre-specified merge rules.

**Rule A applies** — this step must contain actual domain-specific framing; a blank or generic placeholder fails the pre-commitment.

**Step 1b — Per-Class Carrying Costs**

The do-nothing cost per failure class. Status Quo Risk column fills reference this sub-part as "Step 1b, Class N".

**Rule A applies** — no blank cells. **Rule B applies** — Status Quo Risk fills must cite this sub-part; per-row independent authoring of carrying costs is a contract violation.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [named metric, e.g., cart-abandon events] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [named metric, e.g., oversell count] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [named metric, e.g., duplicate-charge events] | per-transaction | compound growth |

**Step 1c — Per-Class Tipping Point Signals**

**Rule A applies** — quantified threshold expression + named detection signal required per class. "Worsens over time" is not quantified and fails Rule A.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [e.g., "cart-abandon rate >2% above 30-day baseline / dashboard alert"] | [metric] |
| 2 | [e.g., "oversell count >50/month / inventory anomaly counter"] | [metric] |
| 3 | [e.g., "reconciliation backlog >200 items / queue-depth alert"] | [metric] |

**Step 1d — SLA Budget**

**Rule A applies** — all twelve cells must carry actual time values. No blank cells, no "TBD".

**Rule B applies** — Recovery Path per-stage SLA values must cite this sub-part as "Step 1d, Class N, [stage] column". Independently authored per-row SLA values are a contract violation under Rule B.

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
| Slot | In-row bold performative inside Row Descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary instruction** (all four escape routes closed simultaneously): Do not create separate tables for Commerce Expert columns and DS Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts. Do not produce a standalone chaos section or standalone chaos-engineering table. Do not produce a standalone observability section or standalone observability table. Satisfying any three without the fourth does not satisfy this instruction.

**Section Order Requirement**: (1) Pre-Commitment Document — all four sub-parts populated; (2) Scenario Table — row N columns AND row N Chaos Test Block before row N+1 begins; (3) Gap Register with three inline findings; (4) Inertia Verdict; (5) Finding Completeness Checklist. **Do not advance to row N+1 until row N columns AND Chaos Block are both complete. Do not advance to the Gap Register until all three rows and Chaos Blocks are complete.**

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1–3, continuous — one table, no splits |
| Class | C | Class 1 (Connectivity Loss), Class 2 (Partial Failure), or Class 3 (Split-Brain) |
| Trigger Condition | C | Quantified threshold expression + named detection signal. Qualitative only fails. |
| State | C | System configuration at failure onset — named components and states |
| Capability | C | Named commerce operations available during failure. Generic descriptions fail. |
| Data at Risk | C | Named data fields, transaction records, or domain entities at risk |
| Status Quo Risk | C | **Reference Step 1b, Class N (Rule B — not independently authored)**. Acute branches (A/B) before chronic metric. Three-component chronic: rate + horizon + metric. |
| Failure Signature | C | Behavioral fingerprint per actor during failure. >=2 named actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | Detect -> Contain -> Recover -> Validate. Per stage: actor-chain prefix + mechanism + **SLA from Step 1d, Class N, stage column -- Rule B restated for co-location at column-contract level: any SLA value not drawn from Step 1d is a named contract violation against this pre-committed budget** + named Verification Signal. >=3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage confirming stage completion. Observable (system state, log entry, metric value, API response code). Not a restatement of mechanism. |
| Chaos Block | D | Four components co-located with this row: Inject (named reproducible condition) / Expected Behavior / Pass Signal / Fail Signal. |

#### Failure Signature Class Boundary Discriminator

> **Class 2 (Partial Failure -- Data Consistency Violation)**: Transaction-level anomaly framing from a single write path. One leg committed, confirmation or other leg absent. Actor viewpoints: client view + server view + transaction boundary view. Node-A / node-B framing is incorrect for Class 2.
>
> **Class 3 (Split-Brain / Eventual Consistency)**: Node-A / node-B framing showing two nodes holding diverging last-write state simultaneously. Single-transaction framing is incorrect for Class 3.
>
> Generic inconsistency descriptions without the class-specific structural signature fail this discriminator.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text paraphrase fails. Class 3 row must apply a canonical label with an adequacy judgment citing this constraint.

---

### Row Descriptors

#### Row 1 -- Class 1: Connectivity Loss

**Write this row now.** C-phase first:

Do-nothing scenario: cart silently dropped, user receives no recovery signal, carrying cost accumulates per-session without bound.

Trigger Condition: quantified connectivity threshold expression (e.g., "client TCP connection attempt exceeds 30s timeout") + detection signal (e.g., "client-side monitor registers ETIMEDOUT; server access log shows no incoming request for this client").

State: client-side isolation at failure onset -- name `{topic}` components affected.

Capability: specific offline-available commerce operations (named) + blocked operations (named).

Data at Risk: in-flight cart state, pending payment intent, unsubmitted order records -- named specifically.

Status Quo Risk: **Step 1b, Class 1** (Rule B -- reference by sub-part label). Acute branches: outcome A (cart silently dropped -> immediate abandonment, no recovery signal); outcome B (cart stale-restored -> incorrect price or inventory at reconnection). Chronic: carrying cost metric accumulates at rate qualifier without ceiling.

Failure Signature: **Class 1 framing** -- client-view (connection timeout, no TCP reset) + server-view (no request in access log, health probe healthy). Not multi-node.

Severity / Blast Radius.

**D-phase after all C-phase columns complete** (column-group gate):

Recovery Path: Detect (TTD) -> Contain (TTC) -> Recover (TTR) -> Validate (TTV). Each stage: actor-chain prefix + mechanism + **SLA from Step 1d, Class 1, [stage] column** (Rule B -- cite by label) + named Verification Signal.

Chaos Block: inject connectivity loss / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column -- including Failure Signature with >=2 Class 1 actor viewpoints; Status Quo Risk citing Step 1b Class 1 by label with acute branches and three-component chronic; all four Recovery Path stages with actor-chain mechanism, SLA from Step 1d Class 1 by label, and named Verification Signal -- AND Row 1 Chaos Block is complete.**

---

#### Row 2 -- Class 2: Partial Failure (Dependent Service Unavailable)

**Write this row now.** C-phase first, then D-phase.

Do-nothing scenario: oversell accumulates silently per deploy; inventory drift is invisible until a customer disputes a double-reservation; no circuit-breaker degrades the failure gracefully.

Trigger Condition: quantified downstream-service degradation threshold + detection signal.

State: `{topic}` upstream service available; downstream payment service degraded or unreachable.

Capability: pre-checkout operations available; checkout submission blocked or queued.

Data at Risk: inventory reservation drift, oversell risk, pending payment intents.

Status Quo Risk: **Step 1b, Class 2** (Rule B). Acute branches: outcome A (hold persists -> phantom reservation lock); outcome B (hold expires -> oversell on next attempt). Chronic: oversell count per-deploy unbounded.

Failure Signature: **Class 2 framing -- transaction-level anomaly from single write path**. Client view + server view + transaction-boundary view. **No node-A / node-B framing.**

Severity / Blast Radius.

**D-phase after all C-phase columns complete:**

Recovery Path: four stages each with actor-chain prefix + mechanism + **SLA from Step 1d, Class 2, [stage] column** (Rule B) + named Verification Signal.

Chaos Block: inject payment service degradation / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete, including Class 2 transaction-level Failure Signature and Recovery Path SLA citing Step 1d Class 2.**

---

#### Row 3 -- Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

Do-nothing scenario: duplicate charges compound per transaction; reconciliation backlog grows indefinitely; the damage is invisible until two orders arrive at the warehouse for the same inventory unit.

Trigger Condition: replication lag threshold + dual-write conflict counter detection signal.

State: network partition active; both nodes accepting independent writes.

Capability: checkout available on both partition sides; conflict invisible to users.

Data at Risk: inventory count diverges; duplicate fulfillment orders possible; double-charge risk.

Status Quo Risk: **Step 1b, Class 3** (Rule B). Acute branches: outcome A (`last-write-wins` -> earlier reservation silently lost); outcome B (`manual-reconcile` required -> order processing halted). Chronic: duplicate-charge events compound per-transaction without ceiling.

Failure Signature: **Class 3 framing -- node-A / node-B diverging state**. Node-A view + node-B view (holding diverging last-write state) + observability view. **Not single-transaction framing.**

Conflict Resolution: canonical label (`last-write-wins` / `merge` / `manual-reconcile` / `reject-stale`) + adequacy judgment citing vocabulary constraint.

Severity / Blast Radius.

**D-phase after all C-phase columns complete:**

Recovery Path: four stages each with actor-chain prefix + mechanism + **SLA from Step 1d, Class 3, [stage] column** (Rule B) + named Verification Signal.

Chaos Block: inject network partition / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Block are complete, including Failure Signature with Class 3 node-A/node-B framing, Conflict Resolution with canonical label and adequacy judgment, and all four Recovery Path stages citing Step 1d Class 3 by label.**

---

### Gap Register

Required output section. Three findings -- one per finding type. Inline with observability fields. No separate observability section.

Per finding:
- **Finding Type**: [Offline Experience Gap | Data Consistency Violation | Missing Recovery Flow]
- **Description**: specific and actionable -- name the specific `{topic}` operation, data record, or recovery flow that is absent. Generic statements fail.
- **Metric**: named system or business metric that quantifies the gap
- **Alert**: named alert condition and threshold
- **Owner**: responsible role or team -- not "TBD"

Finding types present: ___ of 3

---

### Inertia Verdict

After completing all three Gap Register findings, synthesize:
- **Inertia threat level**: HIGH / MEDIUM / LOW
- **Strongest argument against deferral** (2-3 sentences): name the specific gap findings and the carrying-cost metric from Step 1b that continues to accumulate without intervention. State what becomes irreversible or compounding if action is deferred beyond the Step 1c tipping point.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap -- present
- [ ] Data Consistency Violation -- present
- [ ] Missing Recovery Flow -- present
- Finding types present: ___ of 3

---

---

## V-02

**Variation axis**: Output format -- Sub-parts 1a through 1c of the Pre-Commitment Document are rendered as a single pre-commitment assessment table with a dedicated "Rule Constraint" column. This column carries the inline named-label citations (Rule A applies / Rule B applies) per row, eliminating inline prose annotations while ensuring each sub-part's rule enforcement is structurally present in a scannable column format. Step 1d (SLA matrix) retains its four-column table form.

**Hypothesis**: Inline bold-text rule citations in R17 are embedded within prose sub-part instructions, requiring a scorer to parse prose to confirm inline reinforcement. A dedicated "Rule Constraint" column makes citations independently scannable: a reviewer can confirm C-49 compliance by scanning the Rule Constraint column without parsing the Content column. Expected: 84/84.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded conditions for `{topic}` across three structurally distinct failure classes. Produce a complete four-field failure analysis per class, a Gap Register with inline observability, and an Inertia Verdict.

### Role Declaration

Two roles fill all scenario columns:
- **C -- Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk, Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D -- Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block

> **D-Phase Enforcement Note**: The Recovery Path column requires SLA targets drawn from the pre-committed SLA Budget (Step 1d) of the Pre-Commitment Document below. Independently authoring SLA values per scenario row without referencing Step 1d is a **named contract violation**. This constraint is declared here at document scope so it is encountered before any fill instruction.

---

### Pre-Commitment Document: Resilience Commitment Matrix

**Document Enforcement Contract** (positioned before all sub-parts -- read before filling any of Steps 1a through 1d):

> This document pre-commits authoritative values for the scenario table. Two rules govern every sub-part and every fill derived from this document:
>
> **Rule A -- No Deferral**: Writing "TBD", leaving any cell blank, or using "N/A" or any equivalent unfilled value in any sub-part of this document is a named contract violation. Every cell must carry an actual value at authoring time. The pre-commitment is void if any cell is deferred.
>
> **Rule B -- No Per-Row Invention**: Each sub-part is the sole authoritative source for its corresponding scenario column. Independently authoring per-row values not drawn from the corresponding sub-part is a named contract violation. Row fills must cite the source sub-part by label. A fill introducing a value not present in the referenced sub-part is a contract violation regardless of numerical plausibility.
>
> Both rules apply to all sub-parts. Rule A closes the placeholder-deferral escape. Rule B closes the per-row reinvention escape.

---

**Pre-Commitment Assessment Table** (Steps 1a through 1c)

Complete every cell in this table before proceeding to the SLA Budget. The Rule Constraint column is not optional.

| Step | Required Content | Rule Constraint |
|---|---|---|
| 1a -- Domain Fragility Framing | 2-3 sentences: (1) current failure mode without resilience investment; (2) why inertia is the default choice (failures invisible until compound); (3) `{topic}`'s domain-specific fragility (connectivity isolation + idempotency gaps + partition conflict). Domain-specific, not generic boilerplate. | **Rule A applies** -- blank or generic placeholder fails the pre-commitment |
| 1b -- Carrying Cost Class 1 (Connectivity loss) | Failure mode: Full offline. Carrying Cost Metric: [named metric]. Rate: per-session. Horizon: without ceiling. | **Rule A applies** -- no blank cells; **Rule B applies** -- Status Quo Risk row fills cite "Step 1b, Class 1"; per-row invention is a contract violation |
| 1b -- Carrying Cost Class 2 (Partial failure) | Failure mode: Service degraded. Carrying Cost Metric: [named metric]. Rate: per-deploy. Horizon: unbounded. | **Rule A applies**; **Rule B applies** -- Status Quo Risk row fills cite "Step 1b, Class 2" |
| 1b -- Carrying Cost Class 3 (Split-brain) | Failure mode: Partition conflict. Carrying Cost Metric: [named metric]. Rate: per-transaction. Horizon: compound growth. | **Rule A applies**; **Rule B applies** -- Status Quo Risk row fills cite "Step 1b, Class 3" |
| 1c -- Tipping Point Class 1 | Quantified threshold expression + named detection signal (e.g., "cart-abandon rate >2% above 30-day baseline / dashboard alert"). | **Rule A applies** -- qualitative statements fail |
| 1c -- Tipping Point Class 2 | Quantified threshold expression + named detection signal. | **Rule A applies** |
| 1c -- Tipping Point Class 3 | Quantified threshold expression + named detection signal. | **Rule A applies** |

**Step 1d -- SLA Budget**

**Rule A applies** -- all twelve cells must carry actual time values. **Rule B applies** -- Recovery Path SLA fills must cite "Step 1d, Class N, [stage] column". Per-row independent authoring is a contract violation.

| Class | TTD (Detect) | TTC (Contain) | TTR (Recover) | TTV (Validate) |
|---|---|---|---|---|
| 1 -- Connectivity loss | | | | |
| 2 -- Partial failure | | | | |
| 3 -- Split-brain | | | | |

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` -- one table, no splits | Anti-split instruction (below) |
| Section | Phase gate -- all rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | In-row bold performative inside Row Descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary instruction**: Do not create separate tables for Commerce Expert and DS Expert columns. Do not insert horizontal rules or section breaks between rows when ownership shifts. Do not produce a standalone chaos section or standalone observability section. All four escape routes are closed simultaneously.

**Section Order Requirement**: (1) Pre-Commitment Assessment Table complete + SLA Budget complete; (2) Scenario Table -- row N columns AND row N Chaos Block before row N+1; (3) Gap Register; (4) Inertia Verdict; (5) Finding Completeness Checklist.

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1-3, continuous -- one table, no splits |
| Class | C | Class 1, 2, or 3 |
| Trigger Condition | C | Quantified threshold expression + named detection signal. Qualitative only fails. |
| State | C | System configuration at failure onset -- named components and states |
| Capability | C | Named commerce operations available during failure |
| Data at Risk | C | Named data fields or transaction records at risk |
| Status Quo Risk | C | **Reference Step 1b, Class N (Rule B)**. Acute branches (A/B) before chronic. Chronic: rate + horizon + metric. |
| Failure Signature | C | Behavioral fingerprint per actor. >=2 named actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label + blast-radius qualifier |
| Conflict Resolution | C | Canonical label only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | Detect -> Contain -> Recover -> Validate. Per stage: actor-chain prefix + mechanism + **SLA from Step 1d, Class N, stage column -- Rule B restated for co-location at column-contract level: any SLA value not drawn from Step 1d is a named contract violation** + named Verification Signal. >=3 of 4 stages with actor prefix. |
| Verification Signal | D | Named observable artifact per stage. Observable (metric, log, state, response code). Not mechanism restatement. |
| Chaos Block | D | Inject / Expected Behavior / Pass Signal / Fail Signal -- co-located with this row. |

#### Failure Signature Class Boundary Discriminator

> **Class 2**: Transaction-level anomaly from a single write path. One leg committed, other leg absent. Actor viewpoints: client + server + transaction boundary. Node-A / node-B framing fails Class 2.
>
> **Class 3**: Node-A / node-B diverging state simultaneously. Single-transaction framing fails Class 3.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Class 3 must use a canonical label with adequacy judgment.

---

### Row Descriptors

#### Row 1 -- Class 1: Connectivity Loss

**Write this row now.** C-phase first:

Trigger Condition: quantified connectivity threshold + detection signal.
State: client-side isolation at failure onset -- name `{topic}` components affected.
Capability: offline-available operations (named) + blocked operations (named).
Data at Risk: in-flight cart, pending payment intent, unsubmitted order records.
Status Quo Risk: **Step 1b, Class 1** (Rule B). Acute branches (A/B). Chronic: rate + horizon + metric.
Failure Signature: **Class 1 framing** -- client view + server view. Not multi-node.
Severity / Blast Radius.

D-phase after C-phase complete: Recovery Path four stages with actor-chain prefix, **SLA from Step 1d, Class 1** (Rule B), named VS. Chaos Block.

**Do not advance to Row 2 until Row 1 is complete including all four Recovery Path stages with actor-chain, SLA from Step 1d Class 1 by label, and named VS -- AND Chaos Block is complete.**

---

#### Row 2 -- Class 2: Partial Failure

**Write this row now.** C-phase first:

Trigger Condition: quantified downstream-service degradation threshold + detection signal.
State / Capability / Data at Risk.
Status Quo Risk: **Step 1b, Class 2** (Rule B). Acute / chronic.
Failure Signature: **Class 2 -- transaction-level anomaly from single write path**. Client + server + transaction boundary. **No node-A / node-B framing.**
Severity / Blast Radius.

D-phase: Recovery Path four stages with **SLA from Step 1d, Class 2** (Rule B), named VS. Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete.**

---

#### Row 3 -- Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first:

Trigger Condition: replication lag threshold + conflict counter detection.
State / Capability / Data at Risk.
Status Quo Risk: **Step 1b, Class 3** (Rule B). Acute / chronic.
Failure Signature: **Class 3 -- node-A / node-B diverging state**. Not single-transaction.
Conflict Resolution: canonical label + adequacy judgment citing vocabulary constraint.
Severity / Blast Radius.

D-phase: Recovery Path four stages with **SLA from Step 1d, Class 3** (Rule B), named VS. Chaos Block.

**Do not advance to Gap Register until Row 3 columns AND Chaos Block are complete.**

---

### Gap Register

Three findings -- one per type. Per finding: **Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

**Inertia threat level**: HIGH / MEDIUM / LOW

**Strongest argument against deferral** (2-3 sentences): name the specific gap findings and carrying-cost metric from Step 1b that continues to accumulate. State what becomes irreversible or compounding beyond the Step 1c tipping point.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap -- present
- [ ] Data Consistency Violation -- present
- [ ] Missing Recovery Flow -- present
- Finding types present: ___ of 3

---

---

## V-03

**Variation axis**: Lifecycle emphasis -- Recovery Path stages are each specified as a discrete named entry in the Column Contract, with the Rule B restatement label present at per-stage granularity in addition to the column-level restatement. This creates a fourth enforcement hierarchy level: document header (Level 1) -> pre-commitment preamble (Level 2) -> column-contract column-level (Level 3) -> column-contract per-stage entry (Level 4, "Rule B restated at stage-specification level"). Row Descriptors expand stage sub-specifications with explicit stage-level actor, mechanism, SLA, and VS slots.

**Hypothesis**: In R17, C-50 requires three independent hierarchy levels with at least one explicit restatement label. Adding a fourth level at stage sub-specification granularity provides a second restatement label site, making C-50 over-satisfied. The per-stage enforcement signal also acts as a row-level fill governor: a filler authoring each stage encounters Rule B at the point of authorship. Expected: 84/84, with per-stage restatement as a candidate for C-51 extraction in v18.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded conditions for `{topic}` across three structurally distinct failure classes. Produce a complete four-field failure analysis per class, a Gap Register with inline observability, and an Inertia Verdict.

### Role Declaration

Two roles fill all scenario columns:
- **C -- Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk, Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D -- Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block

> **D-Phase Enforcement Note**: The Recovery Path column requires SLA targets drawn from the pre-committed SLA Budget (Step 1d) of the Pre-Commitment Document below. Independently authoring SLA values per scenario row without referencing Step 1d is a **named contract violation**. This constraint is declared here at document scope because it governs D-phase fills across all scenario rows.

---

### Pre-Commitment Document: Resilience Commitment Matrix

**Document Enforcement Contract** (positioned before all sub-parts -- read before filling any of Steps 1a through 1d):

> This document pre-commits authoritative values for the scenario table. Two rules govern all fills:
>
> **Rule A -- No Deferral**: Writing "TBD", leaving any cell blank, or using "N/A" or any equivalent unfilled value in any sub-part is a named contract violation. Every cell must carry an actual value at authoring time.
>
> **Rule B -- No Per-Row Invention**: Each sub-part is the sole authoritative source for its corresponding scenario column. Independently authoring per-row values not drawn from the sub-part is a named contract violation. Row fills must cite the source sub-part by label.
>
> Rule A closes the placeholder-deferral escape. Rule B closes the per-row reinvention escape. Both govern Steps 1a through 1d.

---

**Step 1a -- Domain Fragility Framing**

**Rule A applies** -- actual domain-specific framing required; generic placeholder fails. Write 2-3 sentences: (1) current failure mode without resilience investment; (2) why inertia is the default (failures invisible until compound); (3) domain-specific fragility sources for `{topic}`.

**Step 1b -- Per-Class Carrying Costs**

**Rule A applies** -- no blank cells. **Rule B applies** -- Status Quo Risk fills cite "Step 1b, Class N"; per-row independent authoring is a contract violation.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 -- Connectivity loss | Full offline | [named metric] | per-session | without ceiling |
| 2 -- Partial failure | Service degraded | [named metric] | per-deploy | unbounded |
| 3 -- Split-brain | Partition conflict | [named metric] | per-transaction | compound growth |

**Step 1c -- Per-Class Tipping Point Signals**

**Rule A applies** -- quantified threshold + named detection signal required. "Worsens over time" fails.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [quantified] | [metric] |
| 2 | [quantified] | [metric] |
| 3 | [quantified] | [metric] |

**Step 1d -- SLA Budget**

**Rule A applies** -- all twelve cells require actual time values. **Rule B applies** -- Recovery Path per-stage SLA values cite "Step 1d, Class N, [stage] column"; per-row independent authoring is a contract violation.

| Class | TTD (Detect) | TTC (Contain) | TTR (Recover) | TTV (Validate) |
|---|---|---|---|---|
| 1 -- Connectivity loss | | | | |
| 2 -- Partial failure | | | | |
| 3 -- Split-brain | | | | |

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` -- one table, no splits | Anti-split instruction (below) |
| Section | Phase gate -- all rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | In-row bold performative inside Row Descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary instruction**: Single table. No owner-group sub-tables. No breaks on ownership shift. No standalone chaos section. No standalone observability section. All four escape routes closed.

**Section Order Requirement**: (1) Pre-Commitment Document complete; (2) Scenario Table row N + Chaos Block before row N+1; (3) Gap Register; (4) Inertia Verdict; (5) Checklist.

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1-3, continuous |
| Class | C | Class 1, 2, or 3 |
| Trigger Condition | C | Quantified threshold + detection signal. Qualitative only fails. |
| State | C | System configuration at failure onset |
| Capability | C | Named commerce operations available |
| Data at Risk | C | Named data fields or records |
| Status Quo Risk | C | **Reference Step 1b, Class N (Rule B)**. Acute (A/B) then chronic (rate + horizon + metric). |
| Failure Signature | C | >=2 named actor viewpoints. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label + blast-radius qualifier |
| Conflict Resolution | C | Canonical: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Adequacy judgment required. |
| Recovery Path | D | **Four named stage sub-specifications** (see per-stage entries below). >=3 of 4 stages with actor prefix. |
| Verification Signal | D | Named observable per stage. Distinct from mechanism. |
| Chaos Block | D | Inject / Expected Behavior / Pass Signal / Fail Signal. Co-located per row. |

#### Recovery Path Per-Stage Column Sub-Specifications

Each stage of Recovery Path is a named sub-specification. Fill each stage as a discrete entry.

**Detect (TTD)**: actor-chain prefix + detection mechanism + **SLA from Step 1d, Class N, TTD column** (Rule B) + Verification Signal (named observable confirming detection; distinct from mechanism).

**Contain (TTC)**: actor-chain prefix + containment mechanism + **SLA from Step 1d, Class N, TTC column** (Rule B) + Verification Signal.

**Recover (TTR)**: actor-chain prefix + recovery mechanism + **SLA from Step 1d, Class N, TTR column -- Rule B restated at stage-specification level: any TTR value not present in Step 1d Class N is a named contract violation** + Verification Signal.

**Validate (TTV)**: actor-chain prefix + validation mechanism + **SLA from Step 1d, Class N, TTV column** (Rule B) + Verification Signal (named observable confirming full recovery; distinct from Recover-stage mechanism).

#### Failure Signature Class Boundary Discriminator

> **Class 2**: Transaction-level anomaly from single write path. Client + server + transaction boundary. No node-A / node-B framing.
>
> **Class 3**: Node-A / node-B diverging state. Not single-transaction framing.

#### Conflict Resolution Vocabulary Constraint

Canonical only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Class 3 requires canonical label + adequacy judgment.

---

### Row Descriptors

#### Row 1 -- Class 1: Connectivity Loss

**Write this row now.** C-phase first:

Trigger Condition: quantified threshold + detection signal. State. Capability (named operations available + blocked). Data at Risk. Status Quo Risk: **Step 1b, Class 1** (Rule B) -- acute A/B + three-component chronic. Failure Signature: **Class 1 framing**, client view + server view. Severity / Blast Radius.

**D-phase after C-phase complete:**

Recovery Path -- four named stage sub-specifications:
- **Detect** (TTD): actor-chain + mechanism + **SLA from Step 1d, Class 1, TTD** (Rule B) + VS
- **Contain** (TTC): actor-chain + mechanism + **SLA from Step 1d, Class 1, TTC** (Rule B) + VS
- **Recover** (TTR): actor-chain + mechanism + **SLA from Step 1d, Class 1, TTR** (Rule B -- cite by label) + VS
- **Validate** (TTV): actor-chain + mechanism + **SLA from Step 1d, Class 1, TTV** (Rule B) + VS

Chaos Block: inject connectivity loss / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 2 until all C-phase columns are non-placeholder AND all four Recovery Path stage sub-specifications each have actor-chain mechanism, SLA from Step 1d Class 1 by label, and named VS -- AND Chaos Block is complete.**

---

#### Row 2 -- Class 2: Partial Failure

**Write this row now.** C-phase first.

Trigger / State / Capability / Data at Risk. Status Quo Risk: **Step 1b, Class 2** (Rule B). Failure Signature: **Class 2 transaction-level** -- client + server + transaction boundary. **No node-A / node-B.** Severity / Blast Radius.

Recovery Path -- four stages:
- **Detect**: actor-chain + mechanism + **SLA Step 1d Class 2 TTD** (Rule B) + VS
- **Contain**: actor-chain + mechanism + **SLA Step 1d Class 2 TTC** (Rule B) + VS
- **Recover**: actor-chain + mechanism + **SLA Step 1d Class 2 TTR** (Rule B) + VS
- **Validate**: actor-chain + mechanism + **SLA Step 1d Class 2 TTV** (Rule B) + VS

Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block complete.**

---

#### Row 3 -- Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first.

Trigger / State / Capability / Data at Risk. Status Quo Risk: **Step 1b, Class 3** (Rule B). Failure Signature: **Class 3 node-A / node-B diverging state**. **Not single-transaction.** Conflict Resolution: canonical label + adequacy judgment. Severity / Blast Radius.

Recovery Path -- four stages:
- **Detect**: actor-chain + mechanism + **SLA Step 1d Class 3 TTD** (Rule B) + VS
- **Contain**: actor-chain + mechanism + **SLA Step 1d Class 3 TTC** (Rule B) + VS
- **Recover**: actor-chain + mechanism + **SLA Step 1d Class 3 TTR** (Rule B) + VS
- **Validate**: actor-chain + mechanism + **SLA Step 1d Class 3 TTV** (Rule B) + VS

Chaos Block.

**Do not advance to Gap Register until Row 3 columns AND Chaos Block complete.**

---

### Gap Register

Three findings -- one per type. Per finding: **Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

**Inertia threat level**: HIGH / MEDIUM / LOW

**Strongest argument against deferral** (2-3 sentences): cite specific gap findings and Step 1b carrying-cost metric. State what becomes irreversible beyond the Step 1c tipping point.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3

---

---

## V-04

**Variation axis**: Phrasing register -- formal §-numbered statute style throughout. Enforcement contract is "§ 1 -- Enforcement Mandate" with "§ 1.1 -- Placeholder Prohibition" and "§ 1.2 -- Invention Prohibition". Sub-parts cited as "§ 1a, § 1b" etc. Inline citations use section-number form ("§ 1.1 applies" / "§ 1.2 applies"). Column Contract Recovery Path restatement uses "(§ 1.2 restated at column-contract level)". D-Phase Enforcement Note uses §-number references.

**Hypothesis**: Formal §-numbered identifiers create the most unambiguous citation namespace: "§ 1.1 applies" is a section reference with no prose ambiguity. §-numbered citations are also mechanically scannable (search "§ 1.1" or "§ 1.2" yields every enforcement location). Expected: 84/84 with §-numbered labels qualifying as "named label identifiers" under C-48/C-49 pass conditions.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded conditions for `{topic}` across three structurally distinct failure classes. Produce a complete four-field failure analysis per class, a Gap Register with inline observability, and an Inertia Verdict.

### Role Declaration

Two roles fill all scenario columns:
- **C -- Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk, Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D -- Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block

> **D-Phase Enforcement Note (§ 1.2 Advance Declaration)**: The Recovery Path column SLA values must be drawn from the SLA Budget (§ 1d) of the Pre-Commitment Document below. Authoring SLA values per scenario row without citing § 1d is a named contract violation under § 1.2 (Per-Row Invention Prohibition). This note is placed at document-header scope so the § 1.2 constraint is encountered before any fill instruction.

---

### Pre-Commitment Document: Resilience Commitment Matrix

**§ 1 -- Enforcement Mandate** (governing §§ 1a through 1d -- positioned before all sub-parts, read before filling any sub-part):

> This document pre-commits authoritative values for the scenario table. The following clauses govern all fills derived from this document:
>
> **§ 1.1 -- Placeholder Prohibition**: Writing "TBD", leaving any cell blank, or using "N/A" or any equivalent unfilled value in any sub-part of this document constitutes a named contract violation. Every cell must carry an actual value at the time this document is authored. The pre-commitment is void if any cell is deferred.
>
> **§ 1.2 -- Per-Row Invention Prohibition**: Each sub-part is the sole authoritative source for its corresponding scenario column. Independently authoring per-row values not drawn from the corresponding sub-part constitutes a named contract violation. Row-level fills must reference the source sub-part by its label identifier (e.g., "§ 1b, Class 2" or "§ 1d, Class 3, TTR column"). A fill introducing any value not present in the referenced sub-part is a contract violation regardless of numerical plausibility.
>
> §§ 1.1 and 1.2 apply simultaneously to all sub-parts. A document satisfying § 1.1 without § 1.2, or § 1.2 without § 1.1, fails this Enforcement Mandate.

---

**§ 1a -- Domain Fragility Framing**

**§ 1.1 applies** -- actual domain-specific framing required; a blank or generic placeholder constitutes a § 1.1 violation. Write 2-3 sentences establishing `{topic}`'s structural fragility across all three failure classes. Specific to this domain. Cover: client isolation creates invisible pending-state windows; distributed writes without idempotency guarantees produce duplicate side effects; concurrent partition writes create state divergence requiring pre-specified merge rules.

**§ 1b -- Per-Class Carrying Costs**

**§ 1.1 applies** -- no blank cells permitted. **§ 1.2 applies** -- Status Quo Risk row fills must cite "§ 1b, Class N"; per-row independent authoring of carrying costs is a § 1.2 violation.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 -- Connectivity loss | Full offline | [named metric] | per-session | without ceiling |
| 2 -- Partial failure | Service degraded | [named metric] | per-deploy | unbounded |
| 3 -- Split-brain | Partition conflict | [named metric] | per-transaction | compound growth |

**§ 1c -- Per-Class Tipping Point Signals**

**§ 1.1 applies** -- quantified threshold expression + named detection signal required per class. A qualitative statement ("worsens over time") constitutes a § 1.1 violation.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [quantified threshold] | [metric] |
| 2 | [quantified threshold] | [metric] |
| 3 | [quantified threshold] | [metric] |

**§ 1d -- SLA Budget**

**§ 1.1 applies** -- all twelve cells must carry actual time values. **§ 1.2 applies** -- Recovery Path per-stage SLA values must cite "§ 1d, Class N, [stage] column" as their source. Per-row independently authored SLA values constitute a § 1.2 violation.

| Class | TTD (Detect) | TTC (Contain) | TTR (Recover) | TTV (Validate) |
|---|---|---|---|---|
| 1 -- Connectivity loss | | | | |
| 2 -- Partial failure | | | | |
| 3 -- Split-brain | | | | |

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` -- one table, no splits | Anti-split instruction (below) |
| Section | Phase gate -- all rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | In-row bold performative inside Row Descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary instruction**: Single scenario table. No sub-tables by owner group. No horizontal rules or headings between rows on ownership shift. No standalone chaos section. No standalone observability section. All four escape routes are closed.

**Section Order Requirement**: (1) Pre-Commitment Document complete (§§ 1a through 1d fully populated); (2) Scenario Table -- row N columns AND Chaos Block before row N+1; (3) Gap Register; (4) Inertia Verdict; (5) Finding Completeness Checklist.

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1-3, continuous -- single table, no splits |
| Class | C | Class 1 (Connectivity Loss), Class 2 (Partial Failure), or Class 3 (Split-Brain) |
| Trigger Condition | C | Quantified threshold expression + named detection signal. Qualitative-only fails. |
| State | C | System configuration at failure onset -- named components and states |
| Capability | C | Named commerce operations available during failure |
| Data at Risk | C | Named data fields, records, or entities at risk |
| Status Quo Risk | C | **Reference § 1b, Class N (§ 1.2 -- not independently authored)**. Acute branches (A/B) then chronic (rate + horizon + metric). |
| Failure Signature | C | Behavioral fingerprint per actor. >=2 named actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | Detect -> Contain -> Recover -> Validate. Per stage: actor-chain prefix + mechanism + **SLA from § 1d, Class N, stage column -- § 1.2 restated at column-contract level: any SLA value not drawn from § 1d is a named contract violation under § 1.2** + named Verification Signal. >=3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage. Observable and distinct from mechanism. |
| Chaos Block | D | Inject / Expected Behavior / Pass Signal / Fail Signal -- co-located with this row. |

#### Failure Signature Class Boundary Discriminator

> **Class 2**: Transaction-level anomaly from single write path. Actor viewpoints: client + server + transaction boundary. Node-A / node-B framing fails Class 2.
>
> **Class 3**: Node-A / node-B diverging state simultaneously. Single-transaction framing fails Class 3.

#### Conflict Resolution Vocabulary Constraint

Canonical only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Class 3 requires canonical label + adequacy judgment citing this constraint.

---

### Row Descriptors

#### Row 1 -- Class 1: Connectivity Loss

**Write this row now.** C-phase first:

Trigger Condition: quantified connectivity threshold expression + named detection signal.
State: client-side isolation at failure onset -- name `{topic}` components affected.
Capability: offline-available operations (named) + blocked operations (named).
Data at Risk: in-flight cart state, pending payment intent, unsubmitted order records.
Status Quo Risk: **§ 1b, Class 1** (§ 1.2). Acute branches (A/B). Chronic: rate + horizon + metric.
Failure Signature: **Class 1 framing** -- client view + server view. Not multi-node.
Severity / Blast Radius.

**D-phase after C-phase complete** (column-group gate):

Recovery Path four stages:
- **Detect**: actor-chain + mechanism + **SLA from § 1d, Class 1, TTD** (§ 1.2 -- cite by label) + VS
- **Contain**: actor-chain + mechanism + **SLA from § 1d, Class 1, TTC** (§ 1.2) + VS
- **Recover**: actor-chain + mechanism + **SLA from § 1d, Class 1, TTR** (§ 1.2) + VS
- **Validate**: actor-chain + mechanism + **SLA from § 1d, Class 1, TTV** (§ 1.2) + VS

Chaos Block: inject / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 2 until all C-phase columns non-placeholder, all four Recovery Path stages have actor-chain mechanism, SLA from § 1d Class 1 by label (§ 1.2), and named VS -- AND Chaos Block is complete.**

---

#### Row 2 -- Class 2: Partial Failure

**Write this row now.** C-phase first, then D-phase.

Trigger / State / Capability / Data at Risk.
Status Quo Risk: **§ 1b, Class 2** (§ 1.2). Acute / chronic.
Failure Signature: **Class 2 -- transaction-level anomaly, single write path**. Client + server + transaction boundary. **No node-A / node-B framing.**
Severity / Blast Radius.

Recovery Path four stages with actor-chain, **SLA from § 1d Class 2** (§ 1.2), named VS. Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block complete.**

---

#### Row 3 -- Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

Trigger / State / Capability / Data at Risk.
Status Quo Risk: **§ 1b, Class 3** (§ 1.2). Acute / chronic.
Failure Signature: **Class 3 -- node-A / node-B diverging state**. Not single-transaction.
Conflict Resolution: canonical label + adequacy judgment citing vocabulary constraint.
Severity / Blast Radius.

Recovery Path four stages with actor-chain, **SLA from § 1d Class 3** (§ 1.2), named VS. Chaos Block.

**Do not advance to Gap Register until Row 3 columns AND Chaos Block complete.**

---

### Gap Register

Three findings -- one per type. Per finding: **Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

**Inertia threat level**: HIGH / MEDIUM / LOW

**Strongest argument against deferral** (2-3 sentences): cite specific gap findings and § 1b carrying-cost metric. State what becomes irreversible beyond the § 1c tipping point.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3

---

---

## V-05

**Variation axis**: Inertia framing -- treating "doing nothing" as the named competitor throughout. Task description explicitly names inertia as the competitor to be displaced. Step 1a is a "Status-Quo Competitor Block" with a required three-part inertia framing format. Row Descriptors each open with a "Do-nothing scenario:" sentence. Inertia Verdict uses a structured "Inertia Case" template connecting Step 1a, Step 1b, and Step 1c into a single synthesis argument.

**C-49 fix** (single structural repair from R17):
- Enforcement contract carries explicit self-attestation "(positioned before all sub-parts -- read before filling any of Steps 1a through 1d)".
- Every sub-part including Step 1a carries explicit inline citations of Rule A and Rule B by their named labels.
- Preceding §0 structure from R17 V-05 is eliminated; D-phase scope is declared within the enforcement contract itself, not in a Role Declaration sub-section that precedes the contract block.

**Hypothesis**: R17 V-05 failed C-49 because (a) §0 in the Role Declaration pre-announced Rule B before the enforcement contract, undermining the contract's position as the originating declaration, and (b) §1a carried no inline named-label citations. The fix removes the preceding §0, adds self-attestation "(positioned before all sub-parts)", and ensures every sub-part including Step 1a cites Rule A / Rule B by label. With C-49 repaired, V-05 achieves 84/84 and the series reaches its first five-way perfect tie at the ceiling.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded conditions for `{topic}`. **Treat inertia -- doing nothing -- as the named competitor to be displaced.** Your analysis must make the cost of doing nothing measurable: every failure scenario carries a carrying cost, every gap carries a consequence, and the Inertia Verdict names the specific threshold at which deferral becomes indefensible.

### Role Declaration

Two roles fill all scenario columns:
- **C -- Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk, Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D -- Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block

---

### Pre-Commitment Document: Resilience Commitment Matrix

**Document Enforcement Contract** (**positioned before all sub-parts** -- read before filling any of Steps 1a through 1d):

> This document pre-commits authoritative values for the scenario table. Two rules govern all fills -- including Recovery Path SLA values, which must be drawn from Step 1d (not authored per row independently).
>
> **Rule A -- No Deferral**: Writing "TBD", leaving any cell blank, or using "N/A" or any equivalent unfilled value in any sub-part of this document is a named contract violation. Every cell must carry an actual value at authoring time. The pre-commitment is void if any cell is deferred.
>
> **Rule B -- No Per-Row Invention**: Each sub-part is the sole authoritative source for its corresponding scenario column. Independently authoring per-row values not drawn from the corresponding sub-part is a named contract violation. Row fills must cite the source sub-part by label (e.g., "Step 1b, Class 2" or "Step 1d, Class 3, TTR column"). A fill introducing a value not present in the referenced sub-part is a contract violation regardless of numerical plausibility. This rule governs Recovery Path SLA annotations: any SLA value not drawn from Step 1d, Class N, stage column is a contract violation.
>
> Rule A closes the placeholder-deferral escape. Rule B closes the per-row reinvention escape. Both rules govern Steps 1a through 1d.

---

**Step 1a -- Status-Quo Competitor Block**

**Rule A applies** -- this step must contain actual inertia framing specific to `{topic}`; a blank or generic placeholder is a Rule A violation. **Rule B applies** -- the inertia framing established here is the authoritative context for the Inertia Verdict; the Inertia Verdict must reference this step's framing by label ("Step 1a framing").

Name inertia -- doing nothing -- as the competitor being displaced. Write 2-3 sentences:
1. What the current failure mode looks like without any resilience investment (hard errors, silent data loss, no recovery path) for `{topic}` specifically;
2. Why inertia is the default choice (failures are invisible until they compound; no single incident triggers action);
3. What makes `{topic}`'s domain specifically fragile (connectivity isolation creates invisible pending-state windows; idempotency gaps produce duplicate side effects; partition conflict accumulates without ceiling).

**Step 1b -- Per-Class Carrying Costs**

**Rule A applies** -- no blank cells. **Rule B applies** -- Status Quo Risk row fills must cite "Step 1b, Class N"; per-row independent authoring of carrying costs is a named contract violation.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 -- Connectivity loss | Full offline | [named metric, e.g., cart-abandon events] | per-session | without ceiling |
| 2 -- Partial failure | Service degraded | [named metric, e.g., oversell count] | per-deploy | unbounded |
| 3 -- Split-brain | Partition conflict | [named metric, e.g., duplicate-charge events] | per-transaction | compound growth |

**Step 1c -- Per-Class Tipping Point Signals**

**Rule A applies** -- quantified threshold expression + named detection signal required per class. "Worsens over time" is not quantified and is a Rule A violation.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [e.g., "cart-abandon rate >2% above 30-day baseline / dashboard alert fires"] | [metric] |
| 2 | [e.g., "oversell count >50/month / inventory anomaly counter exceeds alert threshold"] | [metric] |
| 3 | [e.g., "reconciliation backlog >200 items / queue-depth alert fires"] | [metric] |

**Step 1d -- SLA Budget**

**Rule A applies** -- all twelve cells must carry actual time values; no blank cells, no "TBD". **Rule B applies** -- Recovery Path SLA values for every scenario row must cite this sub-part as "Step 1d, Class N, [stage] column"; per-row independently authored SLA values are a Rule B violation.

| Class | TTD (Detect) | TTC (Contain) | TTR (Recover) | TTV (Validate) |
|---|---|---|---|---|
| 1 -- Connectivity loss | | | | |
| 2 -- Partial failure | | | | |
| 3 -- Split-brain | | | | |

---

### Five-Level Anti-Omission Architecture

| Level | Mechanism | Artifact |
|---|---|---|
| Table | Unified row index `#` -- one table, no splits | Anti-split instruction (below) |
| Section | Phase gate -- all rows + chaos blocks before Gap Register | Section Order Requirement (below) |
| Slot | In-row bold performative inside Row Descriptor | Row Descriptors (below) |
| Column-group | C-phase complete before D-phase within same row | Column-group gate in Row Descriptors |
| Column | Named owner per column | Column Contract (below) |

**Anti-boundary instruction** (all four escape routes closed simultaneously): Do not create separate tables for Commerce Expert columns and DS Expert columns. Do not insert a horizontal rule, heading, or section break between rows when column ownership shifts. Do not produce a standalone chaos section or standalone chaos-engineering table. Do not produce a standalone observability section or standalone observability table. Satisfying any three without the fourth does not satisfy this instruction.

**Section Order Requirement**: (1) Pre-Commitment Document -- all sub-parts fully populated; (2) Scenario Table -- row N columns AND row N Chaos Test Block before row N+1; (3) Gap Register with three inline findings; (4) Inertia Verdict (structured inertia case required -- see format below); (5) Finding Completeness Checklist. **Do not advance to row N+1 until row N columns AND Chaos Block are both complete. Do not advance to the Gap Register until all three rows and three Chaos Blocks are complete.**

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1-3, continuous -- one table, no splits |
| Class | C | Class 1 (Connectivity Loss), Class 2 (Partial Failure), or Class 3 (Split-Brain) |
| Trigger Condition | C | Quantified threshold expression + named detection signal. Qualitative only fails. |
| State | C | System configuration at failure onset -- named components and states |
| Capability | C | Named commerce operations available during failure. Generic descriptions fail. |
| Data at Risk | C | Named data fields, transaction records, or domain entities at risk |
| Status Quo Risk | C | **Reference Step 1b, Class N (Rule B -- not independently authored)**. Acute branches (A/B) before chronic metric. Three-component chronic: rate + horizon + metric. |
| Failure Signature | C | Behavioral fingerprint per actor. >=2 named actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | Detect -> Contain -> Recover -> Validate. Per stage: actor-chain prefix + mechanism + **SLA from Step 1d, Class N, stage column -- Rule B restated for co-location at column-contract level: any SLA value not drawn from Step 1d is a named contract violation against this pre-committed budget** + named Verification Signal. >=3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage confirming stage completion. Observable (system state, log entry, metric, API response code). Not a restatement of mechanism. |
| Chaos Block | D | Inject (named reproducible fault condition) / Expected Behavior / Pass Signal (observable confirming expected behavior) / Fail Signal (observable confirming expected behavior did NOT occur). Co-located with this row. |

#### Failure Signature Class Boundary Discriminator

> **Class 2 (Partial Failure -- Data Consistency Violation)**: Fill requires transaction-level anomaly framing from a single write path. One leg committed, confirmation or other leg absent. Actor viewpoints: client view + server view + transaction boundary view. Node-A / node-B framing is incorrect for Class 2.
>
> **Class 3 (Split-Brain / Eventual Consistency)**: Fill requires node-A / node-B framing showing two nodes holding diverging last-write state simultaneously. Single-transaction framing is incorrect for Class 3.
>
> Generic inconsistency descriptions without the class-specific structural signature fail this discriminator regardless of actor viewpoint count.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text paraphrase fails. Class 3 row must apply a canonical label with an adequacy judgment explicitly referencing this constraint.

---

### Row Descriptors

#### Row 1 -- Class 1: Connectivity Loss

**Write this row now.** C-phase first:

**Do-nothing scenario**: user's cart is silently dropped at connectivity loss; user receives no recovery signal; the carrying cost accumulates per-session without bound -- this is the inertia competitor named in Step 1a.

Trigger Condition: quantified connectivity threshold expression (e.g., "client TCP connection attempt exceeds 30s timeout") + detection signal (e.g., "client-side monitor registers ETIMEDOUT; server access log shows no incoming request for this client").

State: client-side isolation at failure onset -- name `{topic}` components and services affected.

Capability: specific offline-available commerce operations (named) + blocked operations (named).

Data at Risk: in-flight cart state, pending payment intent, unsubmitted order records -- named specifically for `{topic}`.

Status Quo Risk: **Step 1b, Class 1** (Rule B -- reference by sub-part label). Acute branches: outcome A (cart silently dropped -> immediate abandonment, no recovery signal); outcome B (cart stale-restored -> incorrect price or inventory at reconnection). Chronic: carrying cost metric accumulates at rate qualifier without ceiling.

Failure Signature: **Class 1 framing** -- client view (connection timeout, no TCP reset, no error message) + server view (no request in access log, health probe healthy). Not multi-node.

Severity / Blast Radius: all users attempting checkout during the connectivity window.

**D-phase after all C-phase columns complete** (column-group gate; Rule B governs SLA fills):

Recovery Path -- four named stages:
- **Detect** (TTD): actor-chain prefix + detection mechanism + **SLA from Step 1d, Class 1, TTD column** (Rule B -- cite by label) + Verification Signal (named observable confirming detection complete, distinct from mechanism)
- **Contain** (TTC): actor-chain prefix + containment mechanism + **SLA from Step 1d, Class 1, TTC column** (Rule B) + Verification Signal
- **Recover** (TTR): actor-chain prefix + recovery mechanism + **SLA from Step 1d, Class 1, TTR column** (Rule B) + Verification Signal
- **Validate** (TTV): actor-chain prefix + validation mechanism + **SLA from Step 1d, Class 1, TTV column** (Rule B) + Verification Signal (named observable confirming full recovery)

Chaos Block: inject connectivity loss (e.g., block all outbound TCP from client process) / Expected Behavior (offline mode activates within TTD; in-progress ops queued or surfaced with error) / Pass Signal (client enters offline mode; queued operations listed) / Fail Signal (client shows blank screen or crash; no offline indicator; no queue visible).

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column -- including Failure Signature with >=2 named Class 1 actor viewpoints; Status Quo Risk citing Step 1b Class 1 by label with acute branches and three-component chronic; all four named Recovery Path stages each with actor-chain mechanism, SLA from Step 1d Class 1 by label (Rule B), and named VS -- AND Row 1 Chaos Test Block is complete.**

---

#### Row 2 -- Class 2: Partial Failure (Dependent Service Unavailable)

**Write this row now.** C-phase first, then D-phase.

**Do-nothing scenario**: oversell accumulates silently per deploy; inventory drift is invisible until a customer disputes a double-reservation; no circuit-breaker degrades the failure gracefully -- this is the carrying cost from Step 1b, Class 2.

Trigger Condition: quantified downstream-service degradation threshold + named detection signal.

State: `{topic}` upstream service available; downstream payment service degraded or unreachable.

Capability: pre-checkout operations available (browse, add-to-cart); checkout submission blocked or queued.

Data at Risk: inventory reservation drift, oversell risk from unacknowledged holds, pending payment intents.

Status Quo Risk: **Step 1b, Class 2** (Rule B). Acute branches: outcome A (hold persists indefinitely -> phantom reservation lock); outcome B (hold silently expires -> oversell on next attempt). Chronic: oversell count accumulates per-deploy unbounded.

Failure Signature: **Class 2 framing -- transaction-level anomaly from single write path**. Client view + server view + transaction-boundary view. **No node-A / node-B framing.**

Severity / Blast Radius.

**D-phase after all C-phase columns complete:**

Recovery Path -- four named stages each with actor-chain prefix + mechanism + **SLA from Step 1d, Class 2, [stage] column** (Rule B) + named Verification Signal. Chaos Block: inject payment service degradation / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete, including Class 2 transaction-level Failure Signature and all four Recovery Path stages citing Step 1d Class 2 by label.**

---

#### Row 3 -- Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

**Do-nothing scenario**: duplicate charges compound per transaction; reconciliation backlog grows indefinitely; the damage is invisible until two orders arrive at the warehouse for the same inventory unit -- this is the carrying cost from Step 1b, Class 3 compounding without ceiling.

Trigger Condition: replication lag threshold (e.g., "replication lag between inventory-service nodes exceeds 5s") + detection signal (e.g., "dual-write conflict counter increments in monitoring dashboard; replication-lag alert fires").

State: network partition active between inventory-service nodes; both nodes accepting independent writes; conflict detection not yet active.

Capability: users on both partition sides can submit checkouts; conflict is invisible; both sides report success.

Data at Risk: inventory count diverges across nodes; duplicate fulfillment orders possible; double-charge risk.

Status Quo Risk: **Step 1b, Class 3** (Rule B). Acute branches: outcome A (`last-write-wins` applied -> earlier reservation silently lost, oversell for earlier buyer); outcome B (`manual-reconcile` required -> order processing halted, customer delay). Chronic: duplicate-charge events compound per-transaction without ceiling.

Failure Signature: **Class 3 framing -- node-A / node-B diverging state**. Node-A view + node-B view (holding diverging last-write inventory count) + observability view (no conflict event visible during partition). **Not single-transaction framing.**

Conflict Resolution: canonical label (`last-write-wins` or `manual-reconcile`) + adequacy judgment citing vocabulary constraint.

Severity / Blast Radius.

**D-phase after all C-phase columns complete:**

Recovery Path -- four named stages each with actor-chain prefix + mechanism + **SLA from Step 1d, Class 3, [stage] column** (Rule B) + named Verification Signal. Chaos Block: inject network partition / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Test Block are complete, including Failure Signature with Class 3 node-A/node-B framing (not single-transaction -- that fails the Class Boundary Discriminator); Conflict Resolution with canonical vocabulary label and adequacy judgment; all four named Recovery Path stages citing Step 1d Class 3 by label (Rule B).**

---

### Gap Register

Required output section. Three findings -- one per finding type. Inline with observability. No separate observability section.

Per finding:
- **Finding Type**: [Offline Experience Gap | Data Consistency Violation | Missing Recovery Flow]
- **Description**: specific and actionable -- name the `{topic}` operation, data record, or recovery flow that is absent. Generic statements fail.
- **Metric**: named metric quantifying the gap
- **Alert**: named alert condition and threshold
- **Owner**: responsible role or team -- not "TBD"

Finding types present: ___ of 3

---

### Inertia Verdict

Required structured inertia case:

**Inertia threat level**: HIGH / MEDIUM / LOW

**Inertia Case** (structured -- all three components required):

1. **Competitor named** (reference Step 1a framing): State what "doing nothing" looks like for `{topic}` specifically -- name the failure mode from Step 1a that continues without intervention.

2. **Carrying cost accumulating** (reference Step 1b + Gap Register findings): Name the specific Gap Register finding and the Step 1b carrying-cost metric (rate + horizon) that continues to accumulate. State the metric and its trajectory.

3. **Tipping point** (reference Step 1c): Name the specific threshold from Step 1c at which the accumulating carrying cost becomes operationally irreversible or publicly visible. State what happens when the threshold is crossed and the threshold is missed.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap -- present
- [ ] Data Consistency Violation -- present
- [ ] Missing Recovery Flow -- present
- Finding types present: ___ of 3
