# Flow-Resilience Skill — Round 19 Variations (Rubric v18)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual consistency.
**Rubric**: v18 (C-01 through C-53, 8 essential/recommended + 45 aspirational)
**Date**: 2026-03-15

---

## Round 19 Context

**Rubric ceiling entering R19**: 86/90 (V-02/V-03/V-05 tied); V-01/V-04 at 84/90.

**Open criteria entering R19**:
- **C-51** (per-stage enforcement restatement at stage-specification level) — open for V-01, V-02, V-04, V-05
- **C-52** (Rule Constraint column in pre-commitment assessment table) — open for V-01, V-03, V-04, V-05
- **C-53** (Structured Inertia Case with mandatory step cross-references) — open for V-01, V-02, V-03, V-04

**R18 root causes for open criteria:**

- **V-01 misses C-51**: Column Contract Recovery Path uses a single inline Rule B restatement at column-contract level (L3). No per-stage entry carries a "restated at stage-specification level" label at TTR granularity (L4 absent).
- **V-01 misses C-52**: Sub-parts 1a–1c are prose blocks with inline bold annotations; no dedicated Rule Constraint column separates enforcement citations from fill instructions.
- **V-01 misses C-53**: Inertia Verdict is free-form prose; no labeled three-component template with named step cross-references.
- **V-02 misses C-51**: Pre-commitment assessment table carries Rule Constraint column (C-52 cracked), but Column Contract Recovery Path has no per-stage sub-specifications with TTR-level restatement label.
- **V-02 misses C-53**: Inertia Verdict is free-form prose without the three-component named template.
- **V-03 misses C-52**: Sub-parts 1a–1c are prose blocks; Column Contract has per-stage sub-specifications (C-51 cracked) but no dedicated Rule Constraint column in the pre-commitment document.
- **V-03 misses C-53**: Inertia Verdict is free-form prose.
- **V-04 misses C-51**: §-numbered sub-specifications exist but no per-stage Recover/TTR entry carries an explicit "§ 1.2 restated at stage-specification level" label.
- **V-04 misses C-52**: §§ 1a–1c are prose blocks with inline §-citation annotations; no dedicated table column separates enforcement from fill content.
- **V-04 misses C-53**: Inertia Verdict is free-form prose without labeled three-component template with § step identifiers.
- **V-05 misses C-51**: Recovery Path per-stage sub-specifications in Row Descriptors carry Rule B citations but Column Contract carries no dedicated per-stage entries with TTR-level restatement label.
- **V-05 misses C-52**: Sub-parts use prose with inline citations; no dedicated Rule Constraint column.

**R19 synthesis paths:**

- **V-01**: Add C-52 by converting Steps 1a–1c to a pre-commitment assessment table with Rule Constraint column. Add C-51 by expanding Column Contract Recovery Path into four named per-stage sub-specifications with "Rule B restated at stage-specification level" label on the Recover/TTR entry. Add C-53 by replacing free-form Inertia Verdict with labeled three-component template citing Step 1a / Step 1b + Gap Register / Step 1c by identifier. Expected: 90/90.
- **V-02**: Add C-51 by adding Recovery Path Per-Stage Column Sub-Specifications block (mirroring V-03's mechanism) with TTR-level restatement label, nested under the existing table architecture. Add C-53 by replacing free-form Inertia Verdict with three-component template. Maintain Rule Constraint column (C-52 already cracked). Expected: 90/90.
- **V-03**: Add C-52 by converting Steps 1a–1c to a pre-commitment assessment table with Rule Constraint column. The per-stage sub-specifications (C-51 already cracked) remain in Column Contract. Add C-53 by adding three-component Inertia Case template. Expected: 90/90.
- **V-04**: Add C-51 by extending §-numbered Recovery Path stage block with "§ 1.2 restated at stage-specification level" on the Recover (TTR) sub-entry. Add C-52 by converting §§ 1a–1c to a table with Rule Constraint column (using § notation). Add C-53 by adding three-component Inertia Case using §-numbered step identifiers. Expected: 90/90.
- **V-05**: Add C-51 by adding Recovery Path Per-Stage Column Sub-Specifications block in Column Contract with TTR-level restatement label at stage granularity. Add C-52 by converting Steps 1a–1c to a pre-commitment assessment table with Rule Constraint column while preserving inertia framing in the content column. Maintain structured Inertia Case (C-53 already cracked). Expected: 90/90.

**Variation axes preserved (single-axis identity unchanged from R18):**
- V-01: Role sequence — Commerce Expert listed first; enforcement note under Commerce Expert block
- V-02: Output format — pre-commitment as assessment table with Rule Constraint column
- V-03: Lifecycle emphasis — Recovery Path per-stage sub-specifications at fourth hierarchy level
- V-04: Phrasing register — formal §-numbered statute style throughout
- V-05: Inertia framing — named competitor displacing inertia; structured Inertia Case (C-53)

**Expected R19 discrimination under v18:**

| Rank | Variation | C-51 | C-52 | C-53 | Uncapped Asp. |
|------|-----------|------|------|------|--------------|
| 1 (tie) | **V-01** | PASS | PASS | PASS | **90/90** |
| 1 (tie) | **V-02** | PASS | PASS | PASS | **90/90** |
| 1 (tie) | **V-03** | PASS | PASS | PASS | **90/90** |
| 1 (tie) | **V-04** | PASS | PASS | PASS | **90/90** |
| 1 (tie) | **V-05** | PASS | PASS | PASS | **90/90** |

If all five crack all three open criteria simultaneously, this is the second five-way perfect tie at the uncapped ceiling in this series (first was R17 at 84/84 under v17). Open for v19: extract new criteria from R19 excellence signals. Candidate signals: V-01's per-stage sub-specs inside Row Descriptors (not only in Column Contract); V-02's Rule Constraint column combined with per-stage sub-specs in a unified structural assertion; V-04's §-numbered stage-level restatement with explicit §-citation in the TTR sub-entry.

---

## V-01

**Variation axis**: Role sequence — Commerce Expert is listed first in the Role Declaration. The D-Phase Enforcement Note appears under the Commerce Expert block at document-header scope, making the pre-commitment enforcement signal commerce-first. All three open criteria added: C-52 via pre-commitment assessment table with Rule Constraint column; C-51 via per-stage Recovery Path sub-specifications in Column Contract with TTR-level Rule B restatement label; C-53 via structured three-component Inertia Case citing Step 1a / Step 1b + Gap Register / Step 1c.

**Hypothesis**: Commerce-first enforcement combined with (a) column-scannable Rule Constraint, (b) stage-specification-level Rule B restatement at TTR, and (c) labeled Inertia Case with step identifiers produces all three new passes simultaneously. Each axis is structurally independent: column placement governs C-52; TTR sub-entry label governs C-51; Inertia Case template structure governs C-53. Expected: 90/90.

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

**Pre-Commitment Assessment Table** (Steps 1a through 1c)

Complete every cell in this table before proceeding to the SLA Budget. The Rule Constraint column is not optional — it is an enforcement obligation column, not a descriptor column.

| Step | Required Content | Rule Constraint |
|---|---|---|
| 1a — Domain Fragility Framing | 2–3 sentences: (1) current failure mode without resilience investment; (2) why inertia is the default choice (failures invisible until compound); (3) `{topic}`'s domain-specific fragility (connectivity isolation creates invisible pending-state windows; idempotency gaps produce duplicate side effects on retry; partition conflict accumulates without ceiling). Domain-specific — not generic boilerplate. | **Rule A applies** — blank or generic placeholder fails the pre-commitment |
| 1b — Carrying Cost Class 1 (Connectivity loss) | Failure mode: Full offline. Carrying Cost Metric: [named metric]. Rate: per-session. Horizon: without ceiling. | **Rule A applies** — no blank cells; **Rule B applies** — Status Quo Risk fills cite "Step 1b, Class 1"; per-row invention is a contract violation |
| 1b — Carrying Cost Class 2 (Partial failure) | Failure mode: Service degraded. Carrying Cost Metric: [named metric]. Rate: per-deploy. Horizon: unbounded. | **Rule A applies**; **Rule B applies** — Status Quo Risk fills cite "Step 1b, Class 2" |
| 1b — Carrying Cost Class 3 (Split-brain) | Failure mode: Partition conflict. Carrying Cost Metric: [named metric]. Rate: per-transaction. Horizon: compound growth. | **Rule A applies**; **Rule B applies** — Status Quo Risk fills cite "Step 1b, Class 3" |
| 1c — Tipping Point Class 1 | Quantified threshold expression + named detection signal (e.g., "cart-abandon rate >2% above 30-day baseline / dashboard alert"). | **Rule A applies** — qualitative statements fail |
| 1c — Tipping Point Class 2 | Quantified threshold expression + named detection signal. | **Rule A applies** |
| 1c — Tipping Point Class 3 | Quantified threshold expression + named detection signal. | **Rule A applies** |

**Step 1d — SLA Budget**

**Rule A applies** — all twelve cells must carry actual time values. No blank cells, no "TBD". **Rule B applies** — Recovery Path per-stage SLA values must cite this sub-part as "Step 1d, Class N, [stage] column". Independently authored per-row SLA values are a contract violation under Rule B.

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

**Section Order Requirement**: (1) Pre-Commitment Assessment Table complete + SLA Budget complete; (2) Scenario Table — row N columns AND row N Chaos Block before row N+1; (3) Gap Register with three inline findings; (4) Inertia Verdict (structured Inertia Case required — see format below); (5) Finding Completeness Checklist. **Do not advance to row N+1 until row N columns AND Chaos Block are both complete. Do not advance to the Gap Register until all three rows and Chaos Blocks are complete.**

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
| Failure Signature | C | Behavioral fingerprint per actor. >=2 named actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | **Four named per-stage sub-specifications** — see stage entries below. >=3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage confirming stage completion. Observable (system state, log entry, metric value, API response code). Not a restatement of mechanism. |
| Chaos Block | D | Four components co-located with this row: Inject (named reproducible condition) / Expected Behavior / Pass Signal / Fail Signal. |

#### Recovery Path Per-Stage Sub-Specifications

Each stage is a discrete named sub-specification. Fill each stage entry independently.

**Detect (TTD)**: actor-chain prefix + detection mechanism + **SLA from Step 1d, Class N, TTD column** (Rule B — cite by label) + named Verification Signal (distinct from mechanism).

**Contain (TTC)**: actor-chain prefix + containment mechanism + **SLA from Step 1d, Class N, TTC column** (Rule B) + named Verification Signal.

**Recover (TTR)**: actor-chain prefix + recovery mechanism + **SLA from Step 1d, Class N, TTR column — Rule B restated at stage-specification level: any TTR value not present in Step 1d, Class N is a named contract violation against the pre-committed SLA budget; this restatement fires at TTR fill time** + named Verification Signal.

**Validate (TTV)**: actor-chain prefix + validation mechanism + **SLA from Step 1d, Class N, TTV column** (Rule B) + named Verification Signal (confirms full recovery; distinct from Recover-stage mechanism).

#### Failure Signature Class Boundary Discriminator

> **Class 2 (Partial Failure — Data Consistency Violation)**: Transaction-level anomaly framing from a single write path. One leg committed, confirmation or other leg absent. Actor viewpoints: client view + server view + transaction boundary view. Node-A / node-B framing is incorrect for Class 2.
>
> **Class 3 (Split-Brain / Eventual Consistency)**: Node-A / node-B framing showing two nodes holding diverging last-write state simultaneously. Single-transaction framing is incorrect for Class 3.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text paraphrase fails. Class 3 row must apply a canonical label with an adequacy judgment citing this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first:

Do-nothing scenario: cart silently dropped, user receives no recovery signal, carrying cost accumulates per-session without bound.

Trigger Condition: quantified connectivity threshold expression (e.g., "client TCP connection attempt exceeds 30s timeout") + detection signal.

State: client-side isolation at failure onset — name `{topic}` components affected.

Capability: specific offline-available commerce operations (named) + blocked operations (named).

Data at Risk: in-flight cart state, pending payment intent, unsubmitted order records — named specifically.

Status Quo Risk: **Step 1b, Class 1** (Rule B — reference by sub-part label). Acute branches: outcome A (cart silently dropped → immediate abandonment, no recovery signal); outcome B (cart stale-restored → incorrect price or inventory at reconnection). Chronic: carrying cost metric accumulates at rate qualifier without ceiling.

Failure Signature: **Class 1 framing** — client view (connection timeout, no TCP reset) + server view (no request in access log, health probe healthy). Not multi-node.

Severity / Blast Radius.

**D-phase after all C-phase columns complete** (column-group gate):

Recovery Path — four per-stage sub-specifications:
- **Detect** (TTD): actor-chain + mechanism + **SLA from Step 1d, Class 1, TTD** (Rule B) + VS
- **Contain** (TTC): actor-chain + mechanism + **SLA from Step 1d, Class 1, TTC** (Rule B) + VS
- **Recover** (TTR): actor-chain + mechanism + **SLA from Step 1d, Class 1, TTR** (Rule B — restated at stage-specification level) + VS
- **Validate** (TTV): actor-chain + mechanism + **SLA from Step 1d, Class 1, TTV** (Rule B) + VS

Chaos Block: inject connectivity loss / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column — including Failure Signature with >=2 Class 1 actor viewpoints; Status Quo Risk citing Step 1b Class 1 by label with acute branches and three-component chronic; all four Recovery Path per-stage sub-specifications each with actor-chain, SLA from Step 1d Class 1 by label, and named VS — AND Row 1 Chaos Block is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first, then D-phase.

Do-nothing scenario: oversell accumulates silently per deploy; no circuit-breaker degrades the failure gracefully.

Trigger Condition: quantified downstream-service degradation threshold + detection signal.

State / Capability / Data at Risk.

Status Quo Risk: **Step 1b, Class 2** (Rule B). Acute branches: outcome A (hold persists → phantom reservation lock); outcome B (hold expires → oversell on next attempt). Chronic: oversell count per-deploy unbounded.

Failure Signature: **Class 2 framing — transaction-level anomaly from single write path**. Client + server + transaction-boundary view. **No node-A / node-B framing.**

Severity / Blast Radius.

Recovery Path — four per-stage sub-specifications with actor-chain, **SLA from Step 1d, Class 2** (Rule B), named VS. Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

Do-nothing scenario: duplicate charges compound per transaction; reconciliation backlog grows indefinitely.

Trigger Condition: replication lag threshold + dual-write conflict counter detection signal.

State / Capability / Data at Risk.

Status Quo Risk: **Step 1b, Class 3** (Rule B). Acute branches: outcome A (`last-write-wins` → earlier reservation silently lost); outcome B (`manual-reconcile` required → order processing halted). Chronic: duplicate-charge events compound per-transaction without ceiling.

Failure Signature: **Class 3 framing — node-A / node-B diverging state**. Node-A + node-B (diverging last-write state) + observability view. **Not single-transaction framing.**

Conflict Resolution: canonical label + adequacy judgment citing vocabulary constraint.

Severity / Blast Radius.

Recovery Path — four per-stage sub-specifications with actor-chain, **SLA from Step 1d, Class 3** (Rule B), named VS. Chaos Block.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Block are complete.**

---

### Gap Register

Required output section. Three findings — one per finding type. Inline with observability. No separate observability section.

Per finding:
- **Finding Type**: [Offline Experience Gap | Data Consistency Violation | Missing Recovery Flow]
- **Description**: specific and actionable — name the `{topic}` operation, data record, or recovery flow that is absent
- **Metric**: named metric quantifying the gap
- **Alert**: named alert condition and threshold
- **Owner**: responsible role or team — not "TBD"

Finding types present: ___ of 3

---

### Inertia Verdict

Required structured Inertia Case — all three components required. Fill each component with a labeled cross-reference to the indicated prior step.

**Inertia threat level**: HIGH / MEDIUM / LOW

**Inertia Case**:

1. **Competitor named** (cite Step 1a by identifier): State what "doing nothing" looks like for `{topic}` — name the specific failure mode established in Step 1a that continues without intervention.

2. **Carrying cost accumulating** (cite Step 1b, Class N by identifier + name a specific Gap Register finding): Name the Step 1b carrying-cost metric (rate + horizon) that is currently accumulating. Name the Gap Register finding that makes this accumulation observable.

3. **Tipping point** (cite Step 1c, Class N by identifier): Name the specific quantified threshold from Step 1c at which the accumulating cost becomes operationally irreversible. State what happens if the tipping point is crossed without intervention.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap — present
- [ ] Data Consistency Violation — present
- [ ] Missing Recovery Flow — present
- Finding types present: ___ of 3

---

---

## V-02

**Variation axis**: Output format — Sub-parts 1a through 1c of the Pre-Commitment Document are rendered as a single pre-commitment assessment table with a dedicated "Rule Constraint" column (C-52, already cracked in R18). R19 adds: C-51 via Recovery Path Per-Stage Column Sub-Specifications block in Column Contract with TTR-level "Rule B restated at stage-specification level" label; C-53 via structured three-component Inertia Case with explicit step identifiers. Step 1d retains its four-column table form.

**Hypothesis**: The Rule Constraint column (C-52) makes enforcement citations column-scannable at pre-commitment time. Adding per-stage sub-specifications with TTR-level restatement (C-51) extends the enforcement chain to stage-fill time. Adding the three-component Inertia Case template (C-53) closes the loop from pre-committed values to synthesis verdict. All three structural layers are architecturally independent and non-redundant. Expected: 90/90.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded conditions for `{topic}` across three structurally distinct failure classes. Produce a complete four-field failure analysis per class, a Gap Register with inline observability, and an Inertia Verdict.

### Role Declaration

Two roles fill all scenario columns:
- **C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk, Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block

> **D-Phase Enforcement Note**: The Recovery Path column requires SLA targets drawn from the pre-committed SLA Budget (Step 1d) of the Pre-Commitment Document below. Independently authoring SLA values per scenario row without referencing Step 1d is a **named contract violation**. This constraint is declared here at document scope so it is encountered before any fill instruction.

---

### Pre-Commitment Document: Resilience Commitment Matrix

**Document Enforcement Contract** (positioned before all sub-parts — read before filling any of Steps 1a through 1d):

> This document pre-commits authoritative values for the scenario table. Two rules govern every sub-part and every fill derived from this document:
>
> **Rule A — No Deferral**: Writing "TBD", leaving any cell blank, or using "N/A" or any equivalent unfilled value in any sub-part of this document is a named contract violation. Every cell must carry an actual value at authoring time. The pre-commitment is void if any cell is deferred.
>
> **Rule B — No Per-Row Invention**: Each sub-part is the sole authoritative source for its corresponding scenario column. Independently authoring per-row values not drawn from the corresponding sub-part is a named contract violation. Row fills must cite the source sub-part by label. A fill introducing a value not present in the referenced sub-part is a contract violation regardless of numerical plausibility.
>
> Both rules apply to all sub-parts. Rule A closes the placeholder-deferral escape. Rule B closes the per-row reinvention escape.

---

**Pre-Commitment Assessment Table** (Steps 1a through 1c)

Complete every cell in this table before proceeding to the SLA Budget. The Rule Constraint column is not optional.

| Step | Required Content | Rule Constraint |
|---|---|---|
| 1a — Domain Fragility Framing | 2–3 sentences: (1) current failure mode without resilience investment; (2) why inertia is the default choice (failures invisible until compound); (3) `{topic}`'s domain-specific fragility (connectivity isolation + idempotency gaps + partition conflict). Domain-specific, not generic boilerplate. | **Rule A applies** — blank or generic placeholder fails the pre-commitment |
| 1b — Carrying Cost Class 1 (Connectivity loss) | Failure mode: Full offline. Carrying Cost Metric: [named metric]. Rate: per-session. Horizon: without ceiling. | **Rule A applies** — no blank cells; **Rule B applies** — Status Quo Risk row fills cite "Step 1b, Class 1"; per-row invention is a contract violation |
| 1b — Carrying Cost Class 2 (Partial failure) | Failure mode: Service degraded. Carrying Cost Metric: [named metric]. Rate: per-deploy. Horizon: unbounded. | **Rule A applies**; **Rule B applies** — Status Quo Risk row fills cite "Step 1b, Class 2" |
| 1b — Carrying Cost Class 3 (Split-brain) | Failure mode: Partition conflict. Carrying Cost Metric: [named metric]. Rate: per-transaction. Horizon: compound growth. | **Rule A applies**; **Rule B applies** — Status Quo Risk row fills cite "Step 1b, Class 3" |
| 1c — Tipping Point Class 1 | Quantified threshold expression + named detection signal (e.g., "cart-abandon rate >2% above 30-day baseline / dashboard alert"). | **Rule A applies** — qualitative statements fail |
| 1c — Tipping Point Class 2 | Quantified threshold expression + named detection signal. | **Rule A applies** |
| 1c — Tipping Point Class 3 | Quantified threshold expression + named detection signal. | **Rule A applies** |

**Step 1d — SLA Budget**

**Rule A applies** — all twelve cells must carry actual time values. **Rule B applies** — Recovery Path SLA fills must cite "Step 1d, Class N, [stage] column". Per-row independent authoring is a contract violation.

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

**Anti-boundary instruction**: Do not create separate tables for Commerce Expert and DS Expert columns. Do not insert horizontal rules or section breaks between rows when ownership shifts. Do not produce a standalone chaos section or standalone observability section. All four escape routes are closed simultaneously.

**Section Order Requirement**: (1) Pre-Commitment Assessment Table complete + SLA Budget complete; (2) Scenario Table — row N columns AND row N Chaos Block before row N+1; (3) Gap Register; (4) Inertia Verdict (structured Inertia Case required — see format below); (5) Finding Completeness Checklist.

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1–3, continuous — one table, no splits |
| Class | C | Class 1, 2, or 3 |
| Trigger Condition | C | Quantified threshold expression + named detection signal. Qualitative only fails. |
| State | C | System configuration at failure onset — named components and states |
| Capability | C | Named commerce operations available during failure |
| Data at Risk | C | Named data fields or transaction records at risk |
| Status Quo Risk | C | **Reference Step 1b, Class N (Rule B)**. Acute branches (A/B) before chronic. Chronic: rate + horizon + metric. |
| Failure Signature | C | Behavioral fingerprint per actor. >=2 named actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label + blast-radius qualifier |
| Conflict Resolution | C | Canonical label only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | **Four named per-stage sub-specifications** — see stage entries below. >=3 of 4 stages with actor prefix. |
| Verification Signal | D | Named observable artifact per stage. Observable (metric, log, state, response code). Not mechanism restatement. |
| Chaos Block | D | Inject / Expected Behavior / Pass Signal / Fail Signal — co-located with this row. |

#### Recovery Path Per-Stage Column Sub-Specifications

Each Recovery Path stage is a named sub-specification. Fill each stage entry independently.

**Detect (TTD)**: actor-chain prefix + detection mechanism + **SLA from Step 1d, Class N, TTD column** (Rule B — cite by label) + named Verification Signal.

**Contain (TTC)**: actor-chain prefix + containment mechanism + **SLA from Step 1d, Class N, TTC column** (Rule B) + named Verification Signal.

**Recover (TTR)**: actor-chain prefix + recovery mechanism + **SLA from Step 1d, Class N, TTR column — Rule B restated at stage-specification level: any TTR value not drawn from Step 1d, Class N is a named contract violation; this restatement fires at TTR stage-fill time, not at column-scan time** + named Verification Signal.

**Validate (TTV)**: actor-chain prefix + validation mechanism + **SLA from Step 1d, Class N, TTV column** (Rule B) + named Verification Signal (confirms full recovery; distinct from Recover-stage mechanism).

#### Failure Signature Class Boundary Discriminator

> **Class 2**: Transaction-level anomaly from a single write path. One leg committed, other leg absent. Actor viewpoints: client + server + transaction boundary. Node-A / node-B framing fails Class 2.
>
> **Class 3**: Node-A / node-B diverging state simultaneously. Single-transaction framing fails Class 3.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Class 3 must use a canonical label with adequacy judgment.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first:

Trigger Condition: quantified connectivity threshold + detection signal.
State: client-side isolation at failure onset — name `{topic}` components affected.
Capability: offline-available operations (named) + blocked operations (named).
Data at Risk: in-flight cart, pending payment intent, unsubmitted order records.
Status Quo Risk: **Step 1b, Class 1** (Rule B). Acute branches (A/B). Chronic: rate + horizon + metric.
Failure Signature: **Class 1 framing** — client view + server view. Not multi-node.
Severity / Blast Radius.

**D-phase after C-phase complete**:

Recovery Path — four per-stage sub-specifications:
- **Detect** (TTD): actor-chain + mechanism + **SLA Step 1d Class 1 TTD** (Rule B) + VS
- **Contain** (TTC): actor-chain + mechanism + **SLA Step 1d Class 1 TTC** (Rule B) + VS
- **Recover** (TTR): actor-chain + mechanism + **SLA Step 1d Class 1 TTR** (Rule B — restated at stage-specification level) + VS
- **Validate** (TTV): actor-chain + mechanism + **SLA Step 1d Class 1 TTV** (Rule B) + VS

Chaos Block: inject connectivity loss / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 2 until Row 1 is complete including all four Recovery Path stage sub-specifications each with actor-chain, SLA from Step 1d Class 1 by label, and named VS — AND Chaos Block is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first:

Trigger / State / Capability / Data at Risk.
Status Quo Risk: **Step 1b, Class 2** (Rule B). Acute / chronic.
Failure Signature: **Class 2 — transaction-level anomaly from single write path**. Client + server + transaction boundary. **No node-A / node-B framing.**
Severity / Blast Radius.

Recovery Path — four stage sub-specifications with actor-chain, **SLA Step 1d Class 2** (Rule B), named VS. Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block complete.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first:

Trigger / State / Capability / Data at Risk.
Status Quo Risk: **Step 1b, Class 3** (Rule B). Acute / chronic.
Failure Signature: **Class 3 — node-A / node-B diverging state**. Not single-transaction.
Conflict Resolution: canonical label + adequacy judgment citing vocabulary constraint.
Severity / Blast Radius.

Recovery Path — four stage sub-specifications with actor-chain, **SLA Step 1d Class 3** (Rule B), named VS. Chaos Block.

**Do not advance to Gap Register until Row 3 columns AND Chaos Block complete.**

---

### Gap Register

Three findings — one per type. Per finding: **Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

Required structured Inertia Case — all three components required.

**Inertia threat level**: HIGH / MEDIUM / LOW

**Inertia Case**:

1. **Competitor named** (cite Step 1a by identifier): Name the specific failure mode from Step 1a that inertia perpetuates without intervention.

2. **Carrying cost accumulating** (cite Step 1b, Class N by identifier + name a specific Gap Register finding): Name the Step 1b carrying-cost metric and its accumulation rate. Name the Gap Register finding that makes this accumulation traceable.

3. **Tipping point** (cite Step 1c, Class N by identifier): Name the Step 1c quantified threshold at which the accumulating cost becomes irreversible. State what becomes unrecoverable once the threshold is crossed without intervention.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap — present
- [ ] Data Consistency Violation — present
- [ ] Missing Recovery Flow — present
- Finding types present: ___ of 3

---

---

## V-03

**Variation axis**: Lifecycle emphasis — Recovery Path stages are specified as discrete named per-stage sub-entries in the Column Contract, with Rule B restatement at TTR stage-specification level (C-51, already cracked in R18). R19 adds: C-52 via pre-commitment assessment table with Rule Constraint column (converting prose Steps 1a–1c to table form while preserving the per-stage sub-specification architecture); C-53 via structured three-component Inertia Case with named step identifiers. Hierarchy levels: document header (L1) → preamble enforcement contract (L2) → column-contract level (L3) → column-contract per-stage entry (L4, "restated at stage-specification level").

**Hypothesis**: Per-stage sub-specifications at TTR granularity (C-51) + Rule Constraint column in pre-commitment table (C-52) + three-component Inertia Case with step cross-references (C-53) are each structurally independent. C-52's column-scan path verifies pre-commitment enforcement. C-51's stage-specification restatement fires at TTR fill moment. C-53's labeled components close the synthesis loop to named step values. Expected: 90/90.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded conditions for `{topic}` across three structurally distinct failure classes. Produce a complete four-field failure analysis per class, a Gap Register with inline observability, and an Inertia Verdict.

### Role Declaration

Two roles fill all scenario columns:
- **C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk, Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block

> **D-Phase Enforcement Note**: The Recovery Path column requires SLA targets drawn from the pre-committed SLA Budget (Step 1d) of the Pre-Commitment Document below. Independently authoring SLA values per scenario row without referencing Step 1d is a **named contract violation**. This constraint is declared here at document scope because it governs D-phase fills across all scenario rows.

---

### Pre-Commitment Document: Resilience Commitment Matrix

**Document Enforcement Contract** (positioned before all sub-parts — read before filling any of Steps 1a through 1d):

> This document pre-commits authoritative values for the scenario table. Two rules govern all fills:
>
> **Rule A — No Deferral**: Writing "TBD", leaving any cell blank, or using "N/A" or any equivalent unfilled value in any sub-part is a named contract violation. Every cell must carry an actual value at authoring time.
>
> **Rule B — No Per-Row Invention**: Each sub-part is the sole authoritative source for its corresponding scenario column. Independently authoring per-row values not drawn from the sub-part is a named contract violation. Row fills must cite the source sub-part by label.
>
> Rule A closes the placeholder-deferral escape. Rule B closes the per-row reinvention escape. Both govern Steps 1a through 1d.

---

**Pre-Commitment Assessment Table** (Steps 1a through 1c)

Complete every cell in this table before proceeding to the SLA Budget. The Rule Constraint column is an enforcement obligation column — it is not optional and must not be left blank.

| Step | Required Content | Rule Constraint |
|---|---|---|
| 1a — Domain Fragility Framing | 2–3 sentences establishing why `{topic}` in commerce is structurally fragile across all three failure classes: (1) current failure mode without resilience investment; (2) why inertia is the default choice (failures invisible until compound); (3) `{topic}`-specific fragility sources. Not generic distributed systems boilerplate. | **Rule A applies** — actual domain-specific framing required; generic placeholder fails the pre-commitment |
| 1b — Carrying Cost Class 1 (Connectivity loss) | Failure mode: Full offline. Carrying Cost Metric: [named metric]. Rate: per-session. Horizon: without ceiling. | **Rule A applies** — no blank cells; **Rule B applies** — Status Quo Risk fills cite "Step 1b, Class 1"; per-row independent authoring is a contract violation |
| 1b — Carrying Cost Class 2 (Partial failure) | Failure mode: Service degraded. Carrying Cost Metric: [named metric]. Rate: per-deploy. Horizon: unbounded. | **Rule A applies**; **Rule B applies** — Status Quo Risk fills cite "Step 1b, Class 2" |
| 1b — Carrying Cost Class 3 (Split-brain) | Failure mode: Partition conflict. Carrying Cost Metric: [named metric]. Rate: per-transaction. Horizon: compound growth. | **Rule A applies**; **Rule B applies** — Status Quo Risk fills cite "Step 1b, Class 3" |
| 1c — Tipping Point Class 1 | Quantified threshold expression + named detection signal. | **Rule A applies** — "worsens over time" fails |
| 1c — Tipping Point Class 2 | Quantified threshold expression + named detection signal. | **Rule A applies** |
| 1c — Tipping Point Class 3 | Quantified threshold expression + named detection signal. | **Rule A applies** |

**Step 1d — SLA Budget**

**Rule A applies** — all twelve cells require actual time values. **Rule B applies** — Recovery Path per-stage SLA values cite "Step 1d, Class N, [stage] column"; per-row independent authoring is a contract violation.

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

**Anti-boundary instruction**: Single table. No owner-group sub-tables. No breaks on ownership shift. No standalone chaos section. No standalone observability section. All four escape routes closed.

**Section Order Requirement**: (1) Pre-Commitment Assessment Table complete + SLA Budget complete; (2) Scenario Table — row N + Chaos Block before row N+1; (3) Gap Register; (4) Inertia Verdict (structured Inertia Case required); (5) Checklist.

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1–3, continuous |
| Class | C | Class 1, 2, or 3 |
| Trigger Condition | C | Quantified threshold + detection signal. Qualitative only fails. |
| State | C | System configuration at failure onset |
| Capability | C | Named commerce operations available |
| Data at Risk | C | Named data fields or records |
| Status Quo Risk | C | **Reference Step 1b, Class N (Rule B)**. Acute (A/B) then chronic (rate + horizon + metric). |
| Failure Signature | C | >=2 named actor viewpoints. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label + blast-radius qualifier |
| Conflict Resolution | C | Canonical: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Adequacy judgment required. |
| Recovery Path | D | **Four named per-stage sub-specifications** (see stage entries below). >=3 of 4 stages with actor prefix. |
| Verification Signal | D | Named observable per stage. Distinct from mechanism. |
| Chaos Block | D | Inject / Expected Behavior / Pass Signal / Fail Signal. Co-located per row. |

#### Recovery Path Per-Stage Column Sub-Specifications

Each stage of Recovery Path is a named sub-specification. Fill each stage as a discrete entry.

**Detect (TTD)**: actor-chain prefix + detection mechanism + **SLA from Step 1d, Class N, TTD column** (Rule B) + Verification Signal (named observable confirming detection; distinct from mechanism).

**Contain (TTC)**: actor-chain prefix + containment mechanism + **SLA from Step 1d, Class N, TTC column** (Rule B) + Verification Signal.

**Recover (TTR)**: actor-chain prefix + recovery mechanism + **SLA from Step 1d, Class N, TTR column — Rule B restated at stage-specification level: any TTR value not present in Step 1d, Class N is a named contract violation; this restatement is positioned at TTR stage-fill granularity to fire at the exact fill moment** + Verification Signal.

**Validate (TTV)**: actor-chain prefix + validation mechanism + **SLA from Step 1d, Class N, TTV column** (Rule B) + Verification Signal (named observable confirming full recovery; distinct from Recover-stage mechanism).

#### Failure Signature Class Boundary Discriminator

> **Class 2**: Transaction-level anomaly from single write path. Client + server + transaction boundary. No node-A / node-B framing.
>
> **Class 3**: Node-A / node-B diverging state. Not single-transaction framing.

#### Conflict Resolution Vocabulary Constraint

Canonical only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Class 3 requires canonical label + adequacy judgment.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first:

Trigger Condition: quantified threshold + detection signal. State. Capability (named operations available + blocked). Data at Risk. Status Quo Risk: **Step 1b, Class 1** (Rule B) — acute A/B + three-component chronic. Failure Signature: **Class 1 framing**, client view + server view. Severity / Blast Radius.

**D-phase after C-phase complete:**

Recovery Path — four named per-stage sub-specifications:
- **Detect** (TTD): actor-chain + mechanism + **SLA Step 1d Class 1 TTD** (Rule B) + VS
- **Contain** (TTC): actor-chain + mechanism + **SLA Step 1d Class 1 TTC** (Rule B) + VS
- **Recover** (TTR): actor-chain + mechanism + **SLA Step 1d Class 1 TTR** (Rule B — restated at stage-specification level) + VS
- **Validate** (TTV): actor-chain + mechanism + **SLA Step 1d Class 1 TTV** (Rule B) + VS

Chaos Block: inject connectivity loss / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 2 until all C-phase columns are non-placeholder AND all four Recovery Path stage sub-specifications each have actor-chain, SLA from Step 1d Class 1 by label, and named VS — AND Chaos Block is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first.

Trigger / State / Capability / Data at Risk. Status Quo Risk: **Step 1b, Class 2** (Rule B). Failure Signature: **Class 2 transaction-level** — client + server + transaction boundary. **No node-A / node-B.** Severity / Blast Radius.

Recovery Path — four stage sub-specifications:
- **Detect**: actor-chain + mechanism + **SLA Step 1d Class 2 TTD** (Rule B) + VS
- **Contain**: actor-chain + mechanism + **SLA Step 1d Class 2 TTC** (Rule B) + VS
- **Recover**: actor-chain + mechanism + **SLA Step 1d Class 2 TTR** (Rule B — restated at stage-specification level) + VS
- **Validate**: actor-chain + mechanism + **SLA Step 1d Class 2 TTV** (Rule B) + VS

Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block complete.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first.

Trigger / State / Capability / Data at Risk. Status Quo Risk: **Step 1b, Class 3** (Rule B). Failure Signature: **Class 3 node-A / node-B diverging state**. **Not single-transaction.** Conflict Resolution: canonical label + adequacy judgment. Severity / Blast Radius.

Recovery Path — four stage sub-specifications:
- **Detect**: actor-chain + mechanism + **SLA Step 1d Class 3 TTD** (Rule B) + VS
- **Contain**: actor-chain + mechanism + **SLA Step 1d Class 3 TTC** (Rule B) + VS
- **Recover**: actor-chain + mechanism + **SLA Step 1d Class 3 TTR** (Rule B — restated at stage-specification level) + VS
- **Validate**: actor-chain + mechanism + **SLA Step 1d Class 3 TTV** (Rule B) + VS

Chaos Block.

**Do not advance to Gap Register until Row 3 columns AND Chaos Block complete.**

---

### Gap Register

Three findings — one per type. Per finding: **Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

Required structured Inertia Case — all three components required with explicit step identifiers.

**Inertia threat level**: HIGH / MEDIUM / LOW

**Inertia Case**:

1. **Competitor named** (cite Step 1a by identifier): Name the specific failure mode established in Step 1a that inertia perpetuates.

2. **Carrying cost accumulating** (cite Step 1b, Class N by identifier + name a specific Gap Register finding): Name the Step 1b carrying-cost metric, its rate, and its horizon. Name the Gap Register finding that makes this accumulation observable and actionable.

3. **Tipping point** (cite Step 1c, Class N by identifier): Name the Step 1c quantified threshold at which deferral becomes operationally irreversible. State what specific consequence becomes locked in once the threshold is crossed.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3

---

---

## V-04

**Variation axis**: Phrasing register — formal §-numbered statute style throughout. Enforcement contract is "§ 1 — Enforcement Mandate" with "§ 1.1 — Placeholder Prohibition" and "§ 1.2 — Invention Prohibition". Inline citations use section-number form ("§ 1.1 applies" / "§ 1.2 applies"). R19 adds all three open criteria: C-52 via pre-commitment assessment table with Rule Constraint column (§ citations in the constraint column); C-51 via Recovery Path per-stage sub-specifications with "§ 1.2 restated at stage-specification level" label on the Recover/TTR entry; C-53 via structured three-component Inertia Case citing §§ 1a / 1b / 1c by their § identifiers.

**Hypothesis**: §-numbered labels satisfy named-label requirements under C-48/C-49/C-50 (established in R17). Extending §-notation into the Rule Constraint column (C-52), the TTR stage-specification restatement label (C-51), and the Inertia Case component identifiers (C-53) applies the same identifier discipline uniformly across all three new structural layers. Expected: 90/90.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded conditions for `{topic}` across three structurally distinct failure classes. Produce a complete four-field failure analysis per class, a Gap Register with inline observability, and an Inertia Verdict.

### Role Declaration

Two roles fill all scenario columns:
- **C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk, Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block

> **D-Phase Enforcement Note (§ 1.2 Advance Declaration)**: The Recovery Path column SLA values must be drawn from the SLA Budget (§ 1d) of the Pre-Commitment Document below. Authoring SLA values per scenario row without citing § 1d is a named contract violation under § 1.2 (Per-Row Invention Prohibition). This note is placed at document-header scope so the § 1.2 constraint is encountered before any fill instruction.

---

### Pre-Commitment Document: Resilience Commitment Matrix

**§ 1 — Enforcement Mandate** (governing §§ 1a through 1d — positioned before all sub-parts, read before filling any sub-part):

> This document pre-commits authoritative values for the scenario table. The following clauses govern all fills derived from this document:
>
> **§ 1.1 — Placeholder Prohibition**: Writing "TBD", leaving any cell blank, or using "N/A" or any equivalent unfilled value in any sub-part of this document constitutes a named contract violation. Every cell must carry an actual value at the time this document is authored. The pre-commitment is void if any cell is deferred.
>
> **§ 1.2 — Per-Row Invention Prohibition**: Each sub-part is the sole authoritative source for its corresponding scenario column. Independently authoring per-row values not drawn from the corresponding sub-part constitutes a named contract violation. Row-level fills must reference the source sub-part by its label identifier (e.g., "§ 1b, Class 2" or "§ 1d, Class 3, TTR column"). A fill introducing any value not present in the referenced sub-part is a contract violation regardless of numerical plausibility.
>
> §§ 1.1 and 1.2 apply simultaneously to all sub-parts.

---

**Pre-Commitment Assessment Table** (§§ 1a through 1c)

Complete every cell in this table before proceeding to the SLA Budget. The Rule Constraint column carries § citation obligations and is not optional.

| Sub-Part | Required Content | Rule Constraint |
|---|---|---|
| § 1a — Domain Fragility Framing | 2–3 sentences establishing `{topic}`'s structural fragility across all three failure classes. Specific to this domain — not generic distributed systems boilerplate. Cover: client isolation creates invisible pending-state windows; distributed writes without idempotency guarantees produce duplicate side effects; concurrent partition writes create state divergence requiring pre-specified merge rules. | **§ 1.1 applies** — actual domain-specific framing required; blank or generic placeholder constitutes a § 1.1 violation |
| § 1b — Carrying Cost Class 1 (Connectivity loss) | Failure mode: Full offline. Carrying Cost Metric: [named metric]. Rate: per-session. Horizon: without ceiling. | **§ 1.1 applies** — no blank cells; **§ 1.2 applies** — Status Quo Risk fills cite "§ 1b, Class 1"; per-row independent authoring is a § 1.2 violation |
| § 1b — Carrying Cost Class 2 (Partial failure) | Failure mode: Service degraded. Carrying Cost Metric: [named metric]. Rate: per-deploy. Horizon: unbounded. | **§ 1.1 applies**; **§ 1.2 applies** — Status Quo Risk fills cite "§ 1b, Class 2" |
| § 1b — Carrying Cost Class 3 (Split-brain) | Failure mode: Partition conflict. Carrying Cost Metric: [named metric]. Rate: per-transaction. Horizon: compound growth. | **§ 1.1 applies**; **§ 1.2 applies** — Status Quo Risk fills cite "§ 1b, Class 3" |
| § 1c — Tipping Point Class 1 | Quantified threshold expression + named detection signal. | **§ 1.1 applies** — qualitative statement constitutes a § 1.1 violation |
| § 1c — Tipping Point Class 2 | Quantified threshold expression + named detection signal. | **§ 1.1 applies** |
| § 1c — Tipping Point Class 3 | Quantified threshold expression + named detection signal. | **§ 1.1 applies** |

**§ 1d — SLA Budget**

**§ 1.1 applies** — all twelve cells must carry actual time values. **§ 1.2 applies** — Recovery Path per-stage SLA values must cite "§ 1d, Class N, [stage] column" as their source. Per-row independently authored SLA values constitute a § 1.2 violation.

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

**Anti-boundary instruction**: Single scenario table. No sub-tables by owner group. No horizontal rules or headings between rows on ownership shift. No standalone chaos section. No standalone observability section. All four escape routes are closed.

**Section Order Requirement**: (1) Pre-Commitment Assessment Table complete (§§ 1a through 1c) + SLA Budget complete (§ 1d fully populated); (2) Scenario Table — row N columns AND Chaos Block before row N+1; (3) Gap Register; (4) Inertia Verdict (structured Inertia Case with §-numbered step citations required); (5) Finding Completeness Checklist.

---

### Column Contract

| Name | Owner | Fill Requirement |
|---|---|---|
| # | C | Integer 1–3, continuous — single table, no splits |
| Class | C | Class 1 (Connectivity Loss), Class 2 (Partial Failure), or Class 3 (Split-Brain) |
| Trigger Condition | C | Quantified threshold expression + named detection signal. Qualitative-only fails. |
| State | C | System configuration at failure onset — named components and states |
| Capability | C | Named commerce operations available during failure |
| Data at Risk | C | Named data fields, records, or entities at risk |
| Status Quo Risk | C | **Reference § 1b, Class N (§ 1.2 — not independently authored)**. Acute branches (A/B) then chronic (rate + horizon + metric). |
| Failure Signature | C | Behavioral fingerprint per actor. >=2 named actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | **Four named per-stage sub-specifications** — see § stage entries below. >=3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage. Observable and distinct from mechanism. |
| Chaos Block | D | Inject / Expected Behavior / Pass Signal / Fail Signal — co-located with this row. |

#### Recovery Path Per-Stage Column Sub-Specifications

Each Recovery Path stage is a named § sub-specification. Fill each stage entry independently.

**Detect (TTD)**: actor-chain prefix + detection mechanism + **SLA from § 1d, Class N, TTD column** (§ 1.2 — cite by label) + named Verification Signal.

**Contain (TTC)**: actor-chain prefix + containment mechanism + **SLA from § 1d, Class N, TTC column** (§ 1.2) + named Verification Signal.

**Recover (TTR)**: actor-chain prefix + recovery mechanism + **SLA from § 1d, Class N, TTR column — § 1.2 restated at stage-specification level: any TTR value not drawn from § 1d, Class N constitutes a named § 1.2 violation; this restatement is positioned within the TTR stage sub-specification to fire at TTR fill time** + named Verification Signal.

**Validate (TTV)**: actor-chain prefix + validation mechanism + **SLA from § 1d, Class N, TTV column** (§ 1.2) + named Verification Signal (confirms full recovery; distinct from Recover-stage mechanism).

#### Failure Signature Class Boundary Discriminator

> **Class 2**: Transaction-level anomaly from single write path. Actor viewpoints: client + server + transaction boundary. Node-A / node-B framing fails Class 2.
>
> **Class 3**: Node-A / node-B diverging state simultaneously. Single-transaction framing fails Class 3.

#### Conflict Resolution Vocabulary Constraint

Canonical only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Class 3 requires canonical label + adequacy judgment citing this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first:

Trigger Condition: quantified connectivity threshold expression + named detection signal.
State: client-side isolation at failure onset — name `{topic}` components affected.
Capability: offline-available operations (named) + blocked operations (named).
Data at Risk: in-flight cart state, pending payment intent, unsubmitted order records.
Status Quo Risk: **§ 1b, Class 1** (§ 1.2). Acute branches (A/B). Chronic: rate + horizon + metric.
Failure Signature: **Class 1 framing** — client view + server view. Not multi-node.
Severity / Blast Radius.

**D-phase after C-phase complete** (column-group gate):

Recovery Path — four per-stage sub-specifications:
- **Detect** (TTD): actor-chain + mechanism + **SLA from § 1d, Class 1, TTD** (§ 1.2 — cite by label) + VS
- **Contain** (TTC): actor-chain + mechanism + **SLA from § 1d, Class 1, TTC** (§ 1.2) + VS
- **Recover** (TTR): actor-chain + mechanism + **SLA from § 1d, Class 1, TTR** (§ 1.2 — restated at stage-specification level) + VS
- **Validate** (TTV): actor-chain + mechanism + **SLA from § 1d, Class 1, TTV** (§ 1.2) + VS

Chaos Block: inject / Expected Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 2 until all C-phase columns non-placeholder, all four Recovery Path stage sub-specifications have actor-chain, SLA from § 1d Class 1 by label (§ 1.2), and named VS — AND Chaos Block is complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first, then D-phase.

Trigger / State / Capability / Data at Risk.
Status Quo Risk: **§ 1b, Class 2** (§ 1.2). Acute / chronic.
Failure Signature: **Class 2 — transaction-level anomaly, single write path**. Client + server + transaction boundary. **No node-A / node-B framing.**
Severity / Blast Radius.

Recovery Path — four stage sub-specifications with actor-chain, **SLA § 1d Class 2** (§ 1.2), named VS. Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block complete.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

Trigger / State / Capability / Data at Risk.
Status Quo Risk: **§ 1b, Class 3** (§ 1.2). Acute / chronic.
Failure Signature: **Class 3 — node-A / node-B diverging state**. Not single-transaction.
Conflict Resolution: canonical label + adequacy judgment citing vocabulary constraint.
Severity / Blast Radius.

Recovery Path — four stage sub-specifications with actor-chain, **SLA § 1d Class 3** (§ 1.2), named VS. Chaos Block.

**Do not advance to Gap Register until Row 3 columns AND Chaos Block complete.**

---

### Gap Register

Three findings — one per type. Per finding: **Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### Inertia Verdict

Required structured Inertia Case — all three components required. Use § identifiers to cite prior steps.

**Inertia threat level**: HIGH / MEDIUM / LOW

**Inertia Case**:

1. **Competitor named** (cite § 1a by identifier): Name the specific failure mode from § 1a that inertia perpetuates without intervention.

2. **Carrying cost accumulating** (cite § 1b, Class N by identifier + name a specific Gap Register finding): Name the § 1b carrying-cost metric and its accumulation trajectory. Name the Gap Register finding that makes this accumulation traceable and auditable.

3. **Tipping point** (cite § 1c, Class N by identifier): Name the § 1c quantified threshold at which the accumulating cost becomes irreversible. State what becomes unrecoverable once the threshold is crossed.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
- Finding types present: ___ of 3

---

---

## V-05

**Variation axis**: Inertia framing — treating "doing nothing" as the named competitor throughout. Task description explicitly names inertia as the competitor to be displaced. Step 1a is a "Status-Quo Competitor Block". Row Descriptors each open with a "Do-nothing scenario:" sentence. Structured Inertia Case (C-53, already cracked in R18) connects Step 1a, Step 1b, and Step 1c into a labeled three-component synthesis verdict. R19 adds: C-51 via Recovery Path Per-Stage Column Sub-Specifications block in Column Contract with "Rule B restated at stage-specification level" label on Recover/TTR entry; C-52 via pre-commitment assessment table with Rule Constraint column (inertia framing preserved in the Required Content column; Rule A/B citations in the Rule Constraint column).

**Hypothesis**: C-53 is already cracked via the Inertia Case template with named step citations. Adding the Rule Constraint column (C-52) to the pre-commitment table makes enforcement column-scannable without displacing the inertia framing in the content column — the two columns are structurally independent. Adding per-stage sub-specifications with TTR-level Rule B restatement (C-51) extends the four-level hierarchy into the Column Contract stage entries. All three criteria are now independently verifiable. Expected: 90/90.

---

You are a Commerce / distributed systems domain expert. Your task: simulate degraded conditions for `{topic}`. **Treat inertia — doing nothing — as the named competitor to be displaced.** Your analysis must make the cost of doing nothing measurable: every failure scenario carries a carrying cost, every gap carries a consequence, and the Inertia Verdict names the specific threshold at which deferral becomes indefensible.

### Role Declaration

Two roles fill all scenario columns:
- **C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk, Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy
- **D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block

---

### Pre-Commitment Document: Resilience Commitment Matrix

**Document Enforcement Contract** (**positioned before all sub-parts** — read before filling any of Steps 1a through 1d):

> This document pre-commits authoritative values for the scenario table. Two rules govern all fills — including Recovery Path SLA values, which must be drawn from Step 1d (not authored per row independently).
>
> **Rule A — No Deferral**: Writing "TBD", leaving any cell blank, or using "N/A" or any equivalent unfilled value in any sub-part of this document is a named contract violation. Every cell must carry an actual value at authoring time. The pre-commitment is void if any cell is deferred.
>
> **Rule B — No Per-Row Invention**: Each sub-part is the sole authoritative source for its corresponding scenario column. Independently authoring per-row values not drawn from the corresponding sub-part is a named contract violation. Row fills must cite the source sub-part by label (e.g., "Step 1b, Class 2" or "Step 1d, Class 3, TTR column"). A fill introducing a value not present in the referenced sub-part is a contract violation regardless of numerical plausibility. This rule governs Recovery Path SLA annotations: any SLA value not drawn from Step 1d, Class N, stage column is a contract violation.
>
> Rule A closes the placeholder-deferral escape. Rule B closes the per-row reinvention escape. Both rules govern Steps 1a through 1d.

---

**Pre-Commitment Assessment Table** (Steps 1a through 1c)

Complete every cell in this table before proceeding to the SLA Budget. The Rule Constraint column is an enforcement obligation column — it is not optional.

| Step | Required Content | Rule Constraint |
|---|---|---|
| 1a — Status-Quo Competitor Block | Name inertia — doing nothing — as the competitor being displaced. Write 2–3 sentences: (1) what the current failure mode looks like without any resilience investment for `{topic}` specifically (hard errors, silent data loss, no recovery path); (2) why inertia is the default choice (failures are invisible until they compound; no single incident triggers action); (3) what makes `{topic}`'s domain specifically fragile (connectivity isolation creates invisible pending-state windows; idempotency gaps produce duplicate side effects; partition conflict accumulates without ceiling). | **Rule A applies** — this step must contain actual inertia framing specific to `{topic}`; a blank or generic placeholder is a Rule A violation. **Rule B applies** — the inertia framing established here is the authoritative context for the Inertia Verdict; the Inertia Case must reference this step by identifier ("Step 1a") |
| 1b — Carrying Cost Class 1 (Connectivity loss) | Failure mode: Full offline. Carrying Cost Metric: [named metric, e.g., cart-abandon events]. Rate: per-session. Horizon: without ceiling. | **Rule A applies** — no blank cells; **Rule B applies** — Status Quo Risk fills cite "Step 1b, Class 1"; per-row independent authoring is a contract violation |
| 1b — Carrying Cost Class 2 (Partial failure) | Failure mode: Service degraded. Carrying Cost Metric: [named metric, e.g., oversell count]. Rate: per-deploy. Horizon: unbounded. | **Rule A applies**; **Rule B applies** — Status Quo Risk fills cite "Step 1b, Class 2" |
| 1b — Carrying Cost Class 3 (Split-brain) | Failure mode: Partition conflict. Carrying Cost Metric: [named metric, e.g., duplicate-charge events]. Rate: per-transaction. Horizon: compound growth. | **Rule A applies**; **Rule B applies** — Status Quo Risk fills cite "Step 1b, Class 3" |
| 1c — Tipping Point Class 1 | Quantified threshold expression + named detection signal (e.g., "cart-abandon rate >2% above 30-day baseline / dashboard alert fires"). | **Rule A applies** — "worsens over time" is not quantified; qualitative statement fails |
| 1c — Tipping Point Class 2 | Quantified threshold expression + named detection signal. | **Rule A applies** |
| 1c — Tipping Point Class 3 | Quantified threshold expression + named detection signal. | **Rule A applies** |

**Step 1d — SLA Budget**

**Rule A applies** — all twelve cells must carry actual time values; no blank cells, no "TBD". **Rule B applies** — Recovery Path SLA values for every scenario row must cite this sub-part as "Step 1d, Class N, [stage] column"; per-row independently authored SLA values are a Rule B violation.

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

**Section Order Requirement**: (1) Pre-Commitment Assessment Table complete + SLA Budget complete; (2) Scenario Table — row N columns AND row N Chaos Test Block before row N+1; (3) Gap Register with three inline findings; (4) Inertia Verdict (structured Inertia Case required — see format below); (5) Finding Completeness Checklist. **Do not advance to row N+1 until row N columns AND Chaos Block are both complete. Do not advance to the Gap Register until all three rows and three Chaos Blocks are complete.**

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
| Failure Signature | C | Behavioral fingerprint per actor. >=2 named actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | **Four named per-stage sub-specifications** — see stage entries below. >=3 of 4 stages with labeled actor prefix. |
| Verification Signal | D | Named observable artifact per stage. Observable (system state, log entry, metric, API response code). Not a restatement of mechanism. |
| Chaos Block | D | Inject (named reproducible fault condition) / Expected Behavior / Pass Signal / Fail Signal. Co-located with this row. |

#### Recovery Path Per-Stage Column Sub-Specifications

Each stage is a named sub-specification. Fill each stage entry independently.

**Detect (TTD)**: actor-chain prefix + detection mechanism + **SLA from Step 1d, Class N, TTD column** (Rule B — cite by label) + Verification Signal (named observable confirming detection; distinct from mechanism).

**Contain (TTC)**: actor-chain prefix + containment mechanism + **SLA from Step 1d, Class N, TTC column** (Rule B) + Verification Signal.

**Recover (TTR)**: actor-chain prefix + recovery mechanism + **SLA from Step 1d, Class N, TTR column — Rule B restated at stage-specification level: any TTR value not drawn from Step 1d, Class N is a named contract violation; this restatement is positioned at TTR stage-fill granularity, making Rule B present at the exact moment the TTR cell is authored** + Verification Signal.

**Validate (TTV)**: actor-chain prefix + validation mechanism + **SLA from Step 1d, Class N, TTV column** (Rule B) + Verification Signal (named observable confirming full recovery; distinct from Recover-stage mechanism).

#### Failure Signature Class Boundary Discriminator

> **Class 2 (Partial Failure — Data Consistency Violation)**: Transaction-level anomaly framing from a single write path. One leg committed, confirmation or other leg absent. Actor viewpoints: client view + server view + transaction boundary view. Node-A / node-B framing is incorrect for Class 2.
>
> **Class 3 (Split-Brain / Eventual Consistency)**: Node-A / node-B framing showing two nodes holding diverging last-write state simultaneously. Single-transaction framing is incorrect for Class 3.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text paraphrase fails. Class 3 row must apply a canonical label with an adequacy judgment explicitly referencing this constraint.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first:

**Do-nothing scenario**: user's cart is silently dropped at connectivity loss; user receives no recovery signal; the carrying cost accumulates per-session without bound — this is the inertia competitor named in Step 1a.

Trigger Condition: quantified connectivity threshold expression (e.g., "client TCP connection attempt exceeds 30s timeout") + detection signal.

State: client-side isolation at failure onset — name `{topic}` components and services affected.

Capability: specific offline-available commerce operations (named) + blocked operations (named).

Data at Risk: in-flight cart state, pending payment intent, unsubmitted order records — named specifically for `{topic}`.

Status Quo Risk: **Step 1b, Class 1** (Rule B — reference by sub-part label). Acute branches: outcome A (cart silently dropped → immediate abandonment, no recovery signal); outcome B (cart stale-restored → incorrect price or inventory at reconnection). Chronic: carrying cost metric accumulates at rate qualifier without ceiling.

Failure Signature: **Class 1 framing** — client view (connection timeout, no TCP reset, no error message) + server view (no request in access log, health probe healthy). Not multi-node.

Severity / Blast Radius.

**D-phase after all C-phase columns complete** (column-group gate; Rule B governs SLA fills):

Recovery Path — four named per-stage sub-specifications:
- **Detect** (TTD): actor-chain prefix + detection mechanism + **SLA from Step 1d, Class 1, TTD column** (Rule B — cite by label) + VS (named observable confirming detection complete, distinct from mechanism)
- **Contain** (TTC): actor-chain prefix + containment mechanism + **SLA from Step 1d, Class 1, TTC column** (Rule B) + VS
- **Recover** (TTR): actor-chain prefix + recovery mechanism + **SLA from Step 1d, Class 1, TTR column** (Rule B — restated at stage-specification level) + VS
- **Validate** (TTV): actor-chain prefix + validation mechanism + **SLA from Step 1d, Class 1, TTV column** (Rule B) + VS (named observable confirming full recovery)

Chaos Block: inject connectivity loss (e.g., block all outbound TCP from client process) / Expected Behavior (offline mode activates within TTD; in-progress ops queued or surfaced with error) / Pass Signal (client enters offline mode; queued operations listed) / Fail Signal (client shows blank screen or crash; no offline indicator; no queue visible).

**Do not advance to Row 2 until Row 1 contains non-placeholder content in every column — including Failure Signature with >=2 named Class 1 actor viewpoints; Status Quo Risk citing Step 1b Class 1 by label with acute branches and three-component chronic; all four named Recovery Path stage sub-specifications each with actor-chain, SLA from Step 1d Class 1 by label (Rule B), and named VS — AND Row 1 Chaos Test Block is complete.**

---

#### Row 2 — Class 2: Partial Failure (Dependent Service Unavailable)

**Write this row now.** C-phase first, then D-phase.

**Do-nothing scenario**: oversell accumulates silently per deploy; inventory drift is invisible until a customer disputes a double-reservation; no circuit-breaker degrades the failure gracefully — this is the carrying cost from Step 1b, Class 2.

Trigger Condition: quantified downstream-service degradation threshold + named detection signal.

State / Capability / Data at Risk.

Status Quo Risk: **Step 1b, Class 2** (Rule B). Acute branches: outcome A (hold persists → phantom reservation lock); outcome B (hold silently expires → oversell on next attempt). Chronic: oversell count accumulates per-deploy unbounded.

Failure Signature: **Class 2 framing — transaction-level anomaly from single write path**. Client view + server view + transaction-boundary view. **No node-A / node-B framing.**

Severity / Blast Radius.

**D-phase after all C-phase columns complete:**

Recovery Path — four named stage sub-specifications each with actor-chain prefix + mechanism + **SLA from Step 1d, Class 2, [stage] column** (Rule B) + named VS. Chaos Block.

**Do not advance to Row 3 until Row 2 columns AND Chaos Block are complete.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

**Do-nothing scenario**: duplicate charges compound per transaction; reconciliation backlog grows indefinitely — this is the carrying cost from Step 1b, Class 3 compounding without ceiling.

Trigger Condition: replication lag threshold + detection signal.

State / Capability / Data at Risk.

Status Quo Risk: **Step 1b, Class 3** (Rule B). Acute branches: outcome A (`last-write-wins` → earlier reservation silently lost); outcome B (`manual-reconcile` required → order processing halted). Chronic: duplicate-charge events compound per-transaction without ceiling.

Failure Signature: **Class 3 framing — node-A / node-B diverging state**. Node-A + node-B (diverging last-write state) + observability view. **Not single-transaction framing.**

Conflict Resolution: canonical label + adequacy judgment citing vocabulary constraint.

Severity / Blast Radius.

**D-phase after all C-phase columns complete:**

Recovery Path — four named stage sub-specifications each with actor-chain prefix + mechanism + **SLA from Step 1d, Class 3, [stage] column** (Rule B) + named VS. Chaos Block.

**Do not advance to the Gap Register until Row 3 columns AND Chaos Test Block are complete.**

---

### Gap Register

Required output section. Three findings — one per finding type. Inline with observability. No separate observability section.

Per finding:
- **Finding Type**: [Offline Experience Gap | Data Consistency Violation | Missing Recovery Flow]
- **Description**: specific and actionable — name the `{topic}` operation, data record, or recovery flow that is absent
- **Metric**: named metric quantifying the gap
- **Alert**: named alert condition and threshold
- **Owner**: responsible role or team — not "TBD"

Finding types present: ___ of 3

---

### Inertia Verdict

Required structured Inertia Case — all three components required. Fill each component with a labeled cross-reference to the indicated prior step. Generic instructions that do not name a specific step by identifier fail this section.

**Inertia threat level**: HIGH / MEDIUM / LOW

**Inertia Case**:

1. **Competitor named** (cite Step 1a by identifier): State what "doing nothing" looks like for `{topic}` specifically — name the failure mode from Step 1a that continues without intervention.

2. **Carrying cost accumulating** (cite Step 1b, Class N by identifier + name a specific Gap Register finding by its Finding Type and description): Name the Step 1b carrying-cost metric (rate + horizon) that is currently accumulating. Name the Gap Register finding that makes this accumulation observable.

3. **Tipping point** (cite Step 1c, Class N by identifier): Name the specific quantified threshold from Step 1c at which the accumulating carrying cost becomes operationally irreversible or publicly visible. State what happens when the threshold is crossed and the tipping point is missed.

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap — present
- [ ] Data Consistency Violation — present
- [ ] Missing Recovery Flow — present
- Finding types present: ___ of 3

---
