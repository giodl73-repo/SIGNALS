---
skill: quest-golden
skill_target: prove-prototype
date: 2026-03-14
rounds: 20
rubric_final: prove-prototype-rubric-v20-2026-03-14.md
score: 367
status: GOLDEN
---

# prove-prototype — Golden Prompt

**Simplified:** YES (QU5 simplification pass — 21% reduction, 2594 → 2059 words)
**Base variation:** V-01 (role-sequence axis)
**Rubric:** v20 (C-01 through C-52, ceiling 367 pts)

---

## Prompt Body

You are running a prototype signal for topic: **{{topic}}**

---

### MANIFEST PREAMBLE

**Thread declarations** — co-primary propagating commitments. Both rows MUST carry equivalent depth in every column.

| Thread | Scope | Key structural markers | Terminal discharge obligation |
|--------|-------|----------------------|------------------------------|
| **Thread 1 — Competitor lifecycle** | Four-state progression: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED. Identification gated at CALIBRATE; discharge confirmed at CLOSE COMPLETE. | Six surfaces: manifest Competitor Status column; CONTAINER COMPLETE lifecycle annotations; CALIBRATE body (C-29); CALIBRATE COMPLETE triple (C-32); results table baseline column (C-34); CLOSE COMPLETE arc record (C-36). | CLOSE COMPLETE carries the verbatim four-state chain: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED. |
| **Thread 2 — Role sequencing (BUILD + CLOSE)** | Two intra-container sub-role boundaries: BUILD — IMPLEMENTER (Phase 7) → MEASURER (Phase 8); CLOSE — COMPARATOR (Phases 9–10) → AUDITOR (Phases 11–13). Explicit prohibitions on all sub-roles; handoff declarations and acknowledgment gates at both boundaries. | Five structural markers: Phase 7 IMPLEMENTER COMPLETE handoff; Phase 8 MEASURER REQUIRED gate; Phase 10 COMPARATOR COMPLETE handoff; Phase 11 AUDITOR REQUIRED gate; CLOSE COMPLETE sub-role contract discharge. | CLOSE COMPLETE: IMPLEMENTER/MEASURER contract: DISCHARGED | COMPARATOR/AUDITOR contract: DISCHARGED — each distinct from Thread 1 lifecycle chain and C-36 arc record. |

---

### Structural Marker Inventory

| Marker type | Required by | Location | Form |
|-------------|-------------|----------|------|
| Lifecycle framing paragraph | C-43 | Dedicated section before the manifest table — NOT merged with the manifest header or placed inside any container body | Standalone labeled section (## Competitor Lifecycle Framing) separate from all container content |
| Per-container incoming-state annotations | C-43 | Each container header line — NOT as a sentence within the first phase body paragraph | Labeled element on the container header: e.g., `incoming lifecycle state: NOT YET IDENTIFIED` |
| Phase 11 AUDITOR prerequisite gate | C-44 | Phase 11 entry point in CLOSE, before AUDITOR writes any content — NOT as a sentence within the Phase 11 instructional block | REQUIRED-prefixed standalone gate line: `REQUIRED: Confirm Phase 10 COMPARATOR handoff marker present before executing Phase 11` |
| CONTAINER COMPLETE thread labels | C-45 | Each CONTAINER COMPLETE line — NOT as paraphrased status notes embedded in completion prose | Explicitly labeled elements: `Thread 1: [state] | Thread 2: [status]` |

REQUIRED: All four marker types listed above MUST appear as standalone labeled elements in this document. A marker embedded only in prose — legible when the surrounding paragraph is read but not independently verifiable by scanning — fails C-48 and voids this C-50 inventory, retroactively invalidating the pre-execution compliance claim made by this section.

---

### Competitor Lifecycle Framing

The inertia competitor follows a four-state progression: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED.

- **DESIGN (NOT YET IDENTIFIED):** Naming the competitor before measurement criteria are finalized allows its features to contaminate scope decisions. Isolation purpose: scope MUST be driven by the hypothesis, not competitor capabilities. Identification FORBIDDEN in DESIGN.
- **CALIBRATE (IDENTIFIED AND COMMITTED):** Two sub-transitions: NOT YET IDENTIFIED → IDENTIFIED (competitor named in body) and IDENTIFIED → IDENTIFIED AND COMMITTED (B-00 locked, threshold stated at CALIBRATE COMPLETE). Leaving the competitor unidentified through CALIBRATE enables retroactive threshold adjustment after results are seen.
- **BUILD (REFERENCED):** BUILD references B-00 but MUST NOT alter it. Any BUILD-phase reassessment fails the gate.
- **CLOSE (DISCHARGED):** Competitor referenced at results table (baseline column labeled with competitor name, C-34) and terminal arc record (C-36). DISCHARGED confirmed when CLOSE COMPLETE carries the full four-state chain verbatim.

---

### Document Manifest

| Container | Principal purpose | Competitor status |
|-----------|-------------------|-------------------|
| DESIGN | Lock hypothesis, scope, and measurement criteria before construction | NOT YET IDENTIFIED |
| CALIBRATE | Name inertia competitor, measure B-00, commit outperform threshold | IDENTIFIED AND COMMITTED |
| BUILD | IMPLEMENTER constructs prototype; MEASURER measures against B-00 and threshold | REFERENCED |
| CLOSE | COMPARATOR compares and verdicts; AUDITOR audits counter-evidence, limitations, replication | DISCHARGED |

---

### Value Flow Ledger

| Value | Produced in | First consumed in |
|-------|-------------|-------------------|
| Hypothesis text | DESIGN Phase 1 | CALIBRATE Phase 4 (measurement target) |
| Scope boundary + named exclusion | DESIGN Phase 2 | BUILD Phase 7 (IMPLEMENTER scope reference) |
| Success threshold | DESIGN Phase 3 | CLOSE Phase 9 (COMPARATOR comparison) |
| Failure threshold | DESIGN Phase 3 | CLOSE Phase 9 (COMPARATOR comparison) |
| Inertia competitor name | CALIBRATE Phase 4 | CALIBRATE COMPLETE (triple), results table (C-34), CLOSE COMPLETE (arc record) |
| B-00 (baseline measurement) | CALIBRATE Phase 5 | CALIBRATE COMPLETE (triple), BUILD Phase 8 (MEASURER reference), CLOSE Phase 9 (comparison delta) |
| Outperform threshold | CALIBRATE Phase 6 | CALIBRATE COMPLETE (triple), CLOSE Phase 9 (verdict criterion) |
| Prototype artifact description | BUILD Phase 7 (IMPLEMENTER) | BUILD Phase 8 (MEASURER handoff input), CLOSE COMPLETE (arc record) |
| Raw measurement data | BUILD Phase 8 (MEASURER) | CLOSE Phase 9 (COMPARATOR input) |
| Predicted result | DESIGN Phase 3 | CLOSE Phase 10 (actual vs. predicted delta) |
| Verdict word | CLOSE Phase 10 (COMPARATOR) | CLOSE COMPLETE (arc record, Thread 1 discharge) |
| Counter-evidence disposition | CLOSE Phase 11 (AUDITOR) | CLOSE COMPLETE (arc record) |

VALUES MUST NOT be consumed before the producing phase executes.

---

### CONTAINER: DESIGN
**incoming lifecycle state: NOT YET IDENTIFIED — competitor identification FORBIDDEN in this container**
**Entry contract:** This container MUST establish (1) a testable hypothesis, (2) a scope boundary with at least one named exclusion, and (3) explicit success and failure thresholds — before any BUILD or CALIBRATE content is produced.

**Role: DESIGNER**
DESIGNER writes: hypothesis, scope, measurement criteria.
DESIGNER MUST NOT write: competitor names, baseline measurements, prototype construction steps, results, or verdicts.

**Phase 1 — Hypothesis**
State the testable claim for {{topic}}. Name the behavior or property being tested.

GATE: Hypothesis REQUIRED before Phase 2 executes.

**Phase 2 — Scope**
State what the prototype will and will not do. Name at least one deliberate exclusion and explain why that exclusion does not prevent testing the hypothesis.

GATE: Scope boundary REQUIRED before Phase 3 executes.

**Phase 3 — Measurement Criteria**
Define success and failure thresholds before any construction begins. State: what to measure, the unit of measurement, the value that confirms the hypothesis, and the value that refutes it.

GATE: Success and failure thresholds REQUIRED before DESIGN COMPLETE.

**DESIGN COMPLETE**
Record: hypothesis text (verbatim) | scope boundary | success threshold | failure threshold.
Thread 1: NOT YET IDENTIFIED | Thread 2: BUILD and CLOSE sub-roles declared, no handoffs yet executed

---

### CONTAINER: CALIBRATE
**incoming lifecycle state: NOT YET IDENTIFIED — identification REQUIRED in this container, FORBIDDEN to carry forward unidentified**
**Entry contract:** Execute three steps in order: (1) name the inertia competitor with rationale, (2) measure B-00 against the metric defined in DESIGN Phase 3, (3) commit an outperform threshold. All three REQUIRED before BUILD.

**Role: CALIBRATOR**
CALIBRATOR writes: competitor identification, baseline measurement, threshold commitment.
CALIBRATOR MUST NOT write: prototype construction steps, results from the prototype, or verdict language.

**Phase 4 — Inertia Competitor Identification**
Name the status-quo approach or tool the prototype must outperform. State why it is the correct baseline: what problem it solves for {{topic}} and why teams continue using it absent a compelling alternative.

GATE: Competitor name and rationale REQUIRED before Phase 5 executes.

**Phase 5 — Baseline Measurement (B-00)**
Measure the inertia competitor's performance on the exact metric defined in DESIGN Phase 3. Record the raw result as B-00.

GATE: B-00 value REQUIRED before Phase 6 executes.

**Phase 6 — Outperform Threshold**
State the threshold the prototype must exceed to warrant displacing the inertia competitor. The threshold must be more stringent than B-00 by a margin that reflects genuine improvement, not noise.

GATE: Outperform threshold REQUIRED before CALIBRATE COMPLETE.

**CALIBRATE COMPLETE**
Record: competitor name | B-00 value | outperform threshold. All three values REQUIRED on this line.
Thread 1: IDENTIFIED AND COMMITTED (competitor: [name], B-00: [value], threshold: [value]) | Thread 2: no handoffs yet executed

---

### CONTAINER: BUILD
**incoming lifecycle state: IDENTIFIED AND COMMITTED — competitor is named and baseline is locked; BUILD references B-00 but MUST NOT alter it**
**Entry contract:** BUILD executes in two sub-roles with a mandatory handoff at the Phase 7/8 boundary. IMPLEMENTER builds and delivers the prototype; MEASURER receives it, executes measurements, and records raw data.

**Sub-role IMPLEMENTER** (Phase 7)
IMPLEMENTER writes: prototype construction description, artifact deliverable.
IMPLEMENTER FORBIDDEN to: record measurements, interpret results, reference B-00 in comparison language, or produce any verdict-adjacent language.

**Phase 7 — Prototype Construction**
Build the minimal prototype that tests the hypothesis. Describe what was built: the key components, the approach, and any implementation decisions that affect what can and cannot be measured.

GATE: Prototype artifact REQUIRED before IMPLEMENTER COMPLETE.

**IMPLEMENTER COMPLETE — REQUIRED handoff to MEASURER**
Record: prototype artifact name/description.
→ MEASURER receives: prototype artifact (the thing to measure against B-00 and the outperform threshold).
Thread 2: IMPLEMENTER responsibilities discharged — REQUIRED handoff to MEASURER for Phase 8

**Sub-role MEASURER** (Phase 8)
REQUIRED: Confirm Phase 7 IMPLEMENTER handoff marker present before executing Phase 8.
MEASURER writes: measurement execution, raw data, actual vs. predicted comparison.
MEASURER FORBIDDEN to: alter prototype behavior, modify B-00, adjust the outperform threshold, or produce verdict language.

**Phase 8 — Measurement Execution**
Execute the measurements defined in DESIGN Phase 3 against the prototype. Record raw data. State the predicted result alongside the actual result. Record the delta.

GATE: Raw data and actual vs. predicted delta REQUIRED before BUILD COMPLETE.

**BUILD COMPLETE**
Record: prototype description | raw measurement result | predicted value | actual value | delta.
Thread 1: REFERENCED (competitor baseline B-00 used in measurement) | Thread 2: IMPLEMENTER/MEASURER handoff executed and discharged

---

### CONTAINER: CLOSE
**incoming lifecycle state: REFERENCED — competitor transitions to DISCHARGED upon CLOSE COMPLETE**
**Entry contract:** CLOSE executes in two sub-roles. COMPARATOR (Phases 9–10) performs comparison and renders verdict. AUDITOR (Phases 11–13) examines counter-evidence, states limitations, and provides replication path.

**Sub-role COMPARATOR** (Phases 9–10)
COMPARATOR writes: results comparison, verdict.
COMPARATOR FORBIDDEN to write: counter-evidence disposition, limitations, or replication content.

**Phase 9 — Results Table**
Produce a three-column results table: Metric | Inertia competitor ([name], B-00) | Prototype result. Include at least one quantified row. The baseline column MUST be labeled with the inertia competitor name, not a generic "Baseline" label.

GATE: Results table with competitor-named baseline column REQUIRED before Phase 10 executes.

**Phase 10 — Verdict**
State whether the hypothesis is confirmed, refuted, or inconclusive. Cite the specific delta and whether it clears the outperform threshold. State the actual result vs. the predicted result explicitly.

GATE: Verdict REQUIRED before COMPARATOR COMPLETE.

**COMPARATOR COMPLETE — REQUIRED handoff to AUDITOR**
Record: verdict word | delta value | whether outperform threshold was cleared.
COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR for Phases 11–13.
Thread 2: COMPARATOR handoff declared — AUDITOR REQUIRED to confirm before executing Phase 11

**Sub-role AUDITOR** (Phases 11–13)
REQUIRED: Confirm Phase 10 COMPARATOR handoff marker present before executing Phase 11.
AUDITOR writes: counter-evidence disposition, limitations, replication path.
AUDITOR FORBIDDEN to write: new measurement criteria, new comparison data, or verdict statements.

**Phase 11 — Counter-Evidence**
Close the counter-evidence question with one of two explicit dispositions: (a) name a specific counter-interpretation and rebut it with reasoning grounded in the results, or (b) state explicitly that no plausible counter-interpretation exists, with a reason. Silence or an open-ended question does not pass.

GATE: Binary counter-evidence disposition REQUIRED before Phase 12 executes.

**Phase 12 — Limitations**
State at least one limitation of this prototype (scope, fidelity, sample size, or measurement instrument). Explain whether the limitation affects the verdict's validity.

**Phase 13 — Replication Path**
Name all tools, inputs, commands, or steps needed to reproduce the prototype and measurements. No implicit steps.

GATE: Replication path REQUIRED before CLOSE COMPLETE.

**CLOSE COMPLETE**
Record — all elements REQUIRED:
- Hypothesis verdict: [confirmed / refuted / inconclusive]
- Inertia competitor: [name] | B-00: [value] | outperform threshold: [value] | prototype result: [value] | delta: [value]
- Counter-evidence: [disposition]
- Value ledger: FULLY DISCHARGED / PARTIAL — [N] values unresolved
- Thread 1 lifecycle chain (verbatim): NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED
- Thread 2: IMPLEMENTER/MEASURER contract: DISCHARGED | COMPARATOR/AUDITOR contract: DISCHARGED

---

## What Made It Golden

### 1. Dual co-primary thread table with pre-execution commitment contracts

The manifest preamble declares two propagating threads — competitor lifecycle (Thread 1) and role sequencing (Thread 2) — as a symmetric table before any container executes. Both rows carry equivalent depth across all four columns. This means every CONTAINER COMPLETE line has two independently verifiable obligations, not one. Earlier rounds tracked competitor state only; the thread table made role-sequencing a first-class structural commitment with an explicit terminal discharge.

### 2. BUILD intra-container sub-role split with five structural markers (C-51)

BUILD is split into IMPLEMENTER (Phase 7) and MEASURER (Phase 8), each with hard-modal FORBIDDEN clauses. The IMPLEMENTER COMPLETE handoff declaration + Phase 8 REQUIRED acknowledgment gate enforce the boundary structurally — the model cannot begin measurement without confirming the handoff marker. This gave Thread 2 five distinct structural markers (vs. three in prior monolithic BUILDER rounds), enabling full C-51 compliance and making the handoff verifiable by inspection.

### 3. Structural Marker Inventory with retroactive void clause (C-50 + C-52)

The SMI pre-declares all four required marker types before any container executes — as a construction contract, not a description. The REQUIRED closure states that a marker embedded only in prose "voids this C-50 inventory, retroactively invalidating the pre-execution compliance claim made by this section." This makes compliance a falsifiable binary: either every marker type exists as a standalone labeled element, or the entire pre-execution compliance claim collapses.

### 4. Competitor lifecycle as a contamination-gated four-state machine (C-43, C-46)

The Competitor Lifecycle Framing section narrates each container boundary with contamination risk and isolation purpose — not just state names. Per-container incoming-state annotations on every container header make lifecycle state independently verifiable by scanning. The combination means every CONTAINER COMPLETE line carries both backward-looking state evidence (what was committed) and forward-looking contamination enforcement (what is forbidden next).

### 5. Six-surface competitor traceability chain with CLOSE COMPLETE arc record (C-29, C-32, C-34, C-36)

The inertia competitor appears at six named surfaces from identification through discharge. The CLOSE COMPLETE arc record is the terminal node: it encodes competitor name, B-00, outperform threshold, prototype result, delta, and counter-evidence disposition — all on explicitly labeled lines. Thread 1 is discharged via the verbatim four-state chain; Thread 2 is discharged via two separately labeled sub-role contracts. No element can be omitted without breaking a named criterion.

---

## Final Rubric Criteria Summary (v20)

| Tier | Criteria | Points | Description |
|------|----------|--------|-------------|
| **Essential** | C-01–C-05 | 60 | C-01 testable/falsifiable hypothesis; C-02 scope with named exclusion; C-03 measurement criteria (metric, unit, pass/fail thresholds); C-04 B-00 committed before BUILD; C-05 outperform threshold stated |
| **Recommended** | C-06–C-08 | 30 | C-06 results table baseline column labeled with competitor name; C-07 verdict cites delta + threshold; C-08 replication path with no implicit steps |
| **Aspirational** | C-09, C-10, C-16–C-52 | 267 | Container gates (C-16–C-19); gate markers (C-20–C-22); role contamination defense — existence/position/register (C-23, C-38, C-39); inertia competitor traceability chain (C-29, C-32, C-34, C-36); value-flow accountability (C-35, C-37, C-42); manifest competitor lifecycle column (C-40); CLOSE sub-role split COMPARATOR/AUDITOR (C-41); lifecycle framing + per-container annotations (C-43); Phase 11 AUDITOR prerequisite gate (C-44); CONTAINER COMPLETE thread labels (C-45); gate contamination rationale (C-46); structural marker inventory (C-48, C-50); thread depth parity (C-49); BUILD IMPLEMENTER/MEASURER split with five markers (C-51); SMI retroactive void clause (C-52) |
| **Excellence** | C-11–C-15 | 10 | Predictive pre-commitment; adversarial case coverage; cross-phase integrity; precision beyond minimum; construction-enforced co-equality |
| **Total** | | **367** | |

**R21 seed (ceiling 382):** Combine C-53 (per-phase lifecycle callout lines at every phase entry, +5), C-54 (CALIBRATE sub-transitions as distinct table rows, +5), and C-55 (extended competitor surfaces 6+7 — Phase 8 B-00 row labeled with competitor name; document preamble competitor declaration, +5) on the R20 V-01 base.
