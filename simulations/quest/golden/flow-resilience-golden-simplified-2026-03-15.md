Now I have everything I need. Let me write the simplified prompt.

## Simplified Prompt

```
You are a Commerce / distributed systems domain expert. Your task: simulate degraded
conditions for {topic} across three structurally distinct failure classes and produce a
complete failure analysis with a Gap Register, Inertia Synthesis, and Finding Completeness
Checklist.

### Role Declaration

**C — Commerce Expert** owns: #, Class, Trigger Condition, State, Capability, Data at Risk,
Status Quo Risk, Failure Signature, Severity/Blast Radius, Conflict Resolution Strategy.

**D — Distributed Systems Expert** owns: Recovery Path, Verification Signal, Chaos Block.

---

### Enforcement Rule

Recovery Path SLA values must be drawn exclusively from the SLA Budget (§1d) below — do not
author per-row SLA values independently. All §1 sub-parts must carry actual values — no blank
cells, no TBD. Status Quo Risk and Recovery Path fills must cite their source sub-part by label
(e.g., "§1b, Class 1"; "§1d, Class 2, TTR"). Independently authored values are a contract
violation.

---

### Pre-Commitment Document: Resilience Commitment Matrix

**§1a — Domain Fragility Framing**

Write 2–3 sentences establishing {topic}'s structural fragility across the three failure classes.
Domain-specific framing required — generic distributed-systems boilerplate fails. Cover: client
isolation creates invisible pending-state windows; idempotency gaps create retry-duplication side
effects; concurrent partition writes create state divergence requiring pre-specified merge rules
to avoid duplicate fulfillment or double-charge.

**§1b — Per-Class Carrying Costs**

Status Quo Risk fills must cite "§1b, Class N" by label — do not independently author carrying
cost values.

| Class | Failure Mode | Carrying Cost Metric | Rate | Horizon |
|---|---|---|---|---|
| 1 — Connectivity loss | Full offline | [named metric] | per-session | without ceiling |
| 2 — Partial failure | Service degraded | [named metric] | per-deploy | unbounded |
| 3 — Split-brain | Partition conflict | [named metric] | per-transaction | compound growth |

**§1c — Per-Class Tipping Point Signals**

Quantified threshold expression + named detection metric required per class. "Worsens over time"
is not quantified and fails.

| Class | Tipping Point (quantified threshold + detection signal) | Metric |
|---|---|---|
| 1 | [quantified threshold + detection signal] | [metric] |
| 2 | [quantified threshold + detection signal] | [metric] |
| 3 | [quantified threshold + detection signal] | [metric] |

**§1d — SLA Budget**

No blank cells. All twelve cells must carry actual time values. Recovery Path fills must cite
"§1d, Class N, stage column" — independently authored SLA values are a contract violation.

| Class | TTD (Detect) | TTC (Contain) | TTR (Recover) | TTV (Validate) |
|---|---|---|---|---|
| 1 — Connectivity loss | | | | |
| 2 — Partial failure | | | | |
| 3 — Split-brain | | | | |

---

**Anti-boundary instruction**: Do not create separate tables for Commerce Expert and Distributed
Systems Expert columns. Do not insert a heading or section break between rows when column
ownership shifts. Do not produce a standalone chaos section or standalone observability section.

**Section Order**: (1) Pre-Commitment Document complete; (2) Scenario Table — row N columns AND
Chaos Block before row N+1; (3) Gap Register with three inline findings; (4) §2 Inertia
Synthesis; (5) Finding Completeness Checklist. Do not advance to the Gap Register until all
three rows and Chaos Blocks are complete. Do not advance to §2 until Gap Register findings are
complete.

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
| Status Quo Risk | C | **Cite §1b, Class N** (not independently authored). Acute branches (A/B) before chronic metric. Three-component chronic: rate + horizon + metric from §1b. |
| Failure Signature | C | Behavioral fingerprint per actor during failure. ≥2 named actor viewpoints. Distinct from Trigger Condition and State. Class Boundary Discriminator below. |
| Severity / Blast Radius | C | Severity label (degraded / impaired / down) + blast-radius qualifier |
| Conflict Resolution | C | Canonical label only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`. Free-text fails. Adequacy judgment required. |
| Recovery Path | D | Detect → Contain → Recover → Validate. Per stage: actor-chain prefix + mechanism + **SLA citing §1d, Class N, stage column** (independently authored SLA is a contract violation) + named Verification Signal. ≥3 of 4 stages with labeled actor prefix. See Recovery Path Stage Contract below. |
| Verification Signal | D | Named observable artifact per stage confirming stage completion. Distinct from mechanism. |
| Chaos Block | D | Four components co-located with this row: Inject (named reproducible condition) / Expected Behavior / Pass Signal / Fail Signal. Not a separate section. |

#### Failure Signature Class Boundary Discriminator

> **Class 2 (Partial Failure)**: Transaction-level anomaly framing from a single write path.
> Observable at the transaction boundary. No inter-node divergence framing.
>
> **Class 3 (Split-Brain)**: Node-A / node-B framing showing two nodes holding diverging
> last-write state simultaneously. Single-transaction framing is incorrect for Class 3.
>
> Generic fills satisfying either class without the class-specific structural signature fail
> even with multiple actor viewpoints.

#### Conflict Resolution Vocabulary Constraint

Canonical terms only: `last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`.
Free-text paraphrase fails. Class 3 must apply a canonical label with adequacy judgment.

#### Recovery Path Stage Contract

Sequence: **Detect → Contain → Recover → Validate**. Per stage: actor-chain prefix
(`client ->`, `server ->`, `operator ->`, `user ->`) + mechanism + SLA from §1d (cite by
label) + named Verification Signal.

> | Stage | SLA Type | Contract |
> |---|---|---|
> | Detect | TTD from §1d | actor-chain + detection mechanism + named VS (health probe, alert, or metric threshold) |
> | Contain | TTC from §1d | actor-chain + containment action + named VS (circuit breaker open, queue depth falling) |
> | Recover | TTR from §1d | actor-chain + recovery mechanism + named VS (service 200, reconciliation delta = 0) |
> | Validate | TTV from §1d | actor-chain + validation check + named VS (conflict counter at 0, audit trail complete) |

Do not describe all four stages in a single sentence. Do not omit Validate. Do not substitute
"monitor and verify" for a named Verification Signal.

---

### Row Descriptors

#### Row 1 — Class 1: Connectivity Loss

**Write this row now.** C-phase first, then D-phase.

Trigger: quantified connectivity threshold + detection signal. State: client-side isolation —
name {topic} components affected. Capability: offline-available operations + blocked operations.
Data at Risk: in-flight cart state, pending payment intent, unsubmitted order records.
Status Quo Risk: cite **§1b, Class 1** by label. Acute: A (cart dropped) / B (cart
stale-restored). Chronic: rate + horizon + metric from §1b, Class 1. Failure Signature:
Class 1 — client-view (timeout, no TCP reset) + server-view (no request in log).
Severity / Blast Radius.

D-phase: Recovery Path citing **§1d, Class 1** by label — four stages per Stage Contract,
actor-chain ≥3 stages, named VS per stage. Chaos Block: inject connectivity loss / Expected
Behavior / Pass Signal / Fail Signal.

**Do not advance to Row 2 until Row 1 columns and Chaos Block are complete.**

---

#### Row 2 — Class 2: Partial Failure

**Write this row now.** C-phase first, then D-phase.

Trigger: downstream-service degradation threshold + detection signal. State: upstream available;
downstream payment degraded. Capability: browse/cart available; checkout blocked or queued.
Data at Risk: inventory reservation drift, oversell risk. Status Quo Risk: cite **§1b, Class 2**
by label. Acute: phantom hold / oversell. Chronic: named metric per-deploy from §1b, Class 2.
Failure Signature: **Class 2 — transaction-level anomaly** (single write path). No node-A /
node-B framing. Severity / Blast Radius.

D-phase: Recovery Path citing **§1d, Class 2** by label — four stages per Stage Contract,
named VS per stage. Chaos Block: inject downstream failure / Expected Behavior / Pass Signal /
Fail Signal.

**Do not advance to Row 3 until Row 2 columns and Chaos Block are complete.**

---

#### Row 3 — Class 3: Split-Brain / Eventual Consistency

**Write this row now.** C-phase first, then D-phase.

Trigger: replication lag threshold + dual-write conflict counter detection signal. State:
partition active, both nodes accepting independent writes. Capability: checkout available on
both partition sides; conflict invisible. Data at Risk: diverging inventory counts, duplicate
fulfillment orders, double-charge risk. Status Quo Risk: cite **§1b, Class 3** by label.
Acute: `last-write-wins` / `manual-reconcile`. Chronic: duplicate-charge events compound
per-transaction from §1b, Class 3. Failure Signature: **Class 3 — node-A / node-B diverging
state**. Conflict Resolution: canonical label + adequacy judgment. Severity / Blast Radius.

D-phase: Recovery Path citing **§1d, Class 3** by label — four stages per Stage Contract,
named VS per stage. Chaos Block: inject partition / Expected Behavior / Pass Signal / Fail
Signal.

**Do not advance to Gap Register until Row 3 columns and Chaos Block are complete. Do not
advance to §2 until Gap Register findings are complete.**

---

### Gap Register

Three findings inline — no separate observability section:

**Finding Type** | **Description** | **Metric** | **Alert** | **Owner**

Finding types present: ___ of 3

---

### §2 — Inertia Synthesis

Four components:

1. **Urgency label**: HIGH / MEDIUM / LOW
2. **Carrying cost citation**: cite §1b Class N — sub-part label, rate, horizon, metric
3. **Gap finding count**: how many of the three finding types are present; which finding
   creates the highest compounding risk
4. **Escalation**: owner + threshold that triggers action + consequence of missing it

---

### Finding Completeness Checklist

- [ ] Offline Experience Gap
- [ ] Data Consistency Violation
- [ ] Missing Recovery Flow
```

---

## Simplification Report

**Before**: ~1,810 words  
**After**: ~1,285 words  
**Reduction**: ~29%

### What was removed and why

| Cut | Approx. words | Reason |
|---|---|---|
| §0 section header + full blockquote (Enforcement Protocol 1/4 numbering, cross-references, "closed by §2" arc) | ~115 | Pure meta-machinery for aspirational C-59. Replaced by a single 3-sentence "Enforcement Rule" block that preserves the core SLA constraint. |
| §1 Enforcement Contract preamble protocol numbering: "(governing §§ 1a through 1d — read before filling any sub-part)", "*(§0 above is Enforcement Protocol 1/4 — the originating declaration)*", "This §1 preamble is Enforcement Protocol 2/4." | ~40 | Self-referential numbering system. Rule A and Rule B keep their substance. |
| **Five-Level Anti-Omission Architecture** table (entire section) | ~115 | Meta-description of the enforcement structure. Its actual behavioral instructions are fully restated in the Anti-boundary instruction and Section Order Requirement. |
| "(Enforcement Protocol 3/4 reinforced here)" in §1b; "Enforcement Protocol 3/4" in §1d heading; all "(Rule B — cite... by label)" mid-sentence parentheticals | ~35 | Protocol numbering cross-references. The rules themselves are kept; the numbering adds no LLM-behavior value. |
| Column Contract — Recovery Path entry: "(Enforcement Protocol 4/4 (restated for co-location at column-contract level): any SLA value not drawn from §1d is a named contract violation)" | ~25 | Redundant restatement of the Enforcement Rule already defined above. Core constraint kept. |
| Row 1 "Do not advance" condition: long checklist of every sub-criterion | ~55 | Collapsed to one sentence. The detailed sub-criteria are already in the Row Descriptors and Column Contract. |
| Row 2 "Do not advance" condition: same | ~45 | Same reason. |
| Row 3 "Do not advance" condition: long version with §1/§2 sequencing prose | ~50 | Collapsed to two sentences — one for the table gate, one for the §2 gate. |
| Scattered "(Enforcement Protocol 4/4 applies)" inline references in Row Descriptors | ~20 | The Enforcement Rule at top and column-contract entry already cover this; inline repetitions add length without new instruction. |
| Section Order Requirement: "Rule B (Enforcement Protocol 4/4) applies to every D-phase Recovery Path fill" | ~15 | Absorbed by the Enforcement Rule. |

### Essential criteria check (C-01 through C-05)

| Criterion | Still satisfied |
|---|---|
| C-01 Three failure classes | Yes — Row 1/2/3 with Class 1/2/3 labels preserved |
| C-02 Four-field structure | Yes — State, Capability, Data at Risk, Recovery Path in Column Contract and Row Descriptors |
| C-03 Gap identification | Yes — Gap Register with three finding types, Finding Completeness Checklist |
| C-04 Distributed systems accuracy | Yes — Stage Contract, Class Boundary Discriminator, Conflict Resolution vocabulary all preserved |
| C-05 Commerce domain grounding | Yes — §1a framing, commerce-specific Data at Risk content, cart/payment/inventory anchors in all rows |

```json
{"simplified_word_count": 1285, "original_word_count": 1810, "all_essential_still_pass": true, "reduction_pct": 29}
```
