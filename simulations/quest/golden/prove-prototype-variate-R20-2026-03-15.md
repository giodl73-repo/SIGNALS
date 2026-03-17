# prove-prototype Variate — Round 20
**Date:** 2026-03-15
**Rubric:** v19 (C-51 + C-52 introduced)
**Target criteria:** C-51 (BUILD IMPLEMENTER/MEASURER sub-role split — generates Thread 2's Phase 7 handoff and Phase 8 gate markers, making C-49 5:5 depth parity a satisfiable structural property) and C-52 (violation-consequence clause in C-50 REQUIRED closure — names the document property retroactively voided by marker embedding, binding the pre-execution compliance claim to its post-violation state)
**R20 seed:** Both new criteria combined on the R19 base (which already satisfies C-01 through C-50).

---

## Round 20 Variation Map

| Variation | Axis | C-51 | C-52 | Notes |
|-----------|------|------|------|-------|
| V-01 | Role sequence | PASS | PASS | IMPLEMENTER/MEASURER split architecturally mirrored to CLOSE's COMPARATOR/AUDITOR split; C-52 consequence clause upgrades R19 V-01's "voids C-50" to "voids this C-50 inventory, retroactively invalidating this pre-execution compliance claim" |
| V-02 | Output format | PASS | PASS | All phase outputs in structured tables; IMPLEMENTER/MEASURER split added to BUILD (R19 V-02 used monolithic BUILDER and capped Thread 2 at three markers); Thread 2 declaration updated from three to five markers; C-52 consequence clause present |
| V-03 | Lifecycle emphasis (new axis) | PASS | PASS | Per-phase lifecycle state callouts at every phase body entry — competitor lifecycle state and active sub-role named at each phase, not only at container boundaries; BUILD sub-role state tracked at phase granularity (IMPLEMENTER active → IMPLEMENTER COMPLETE → MEASURER active); C-52 consequence clause present |
| V-04 | Role sequence + Phrasing register | PASS | PASS | IMPLEMENTER/MEASURER split in conversational second-person imperative throughout; C-52 consequence clause in direct-address second-person form ("voids this C-50 inventory you just wrote") |
| V-05 | Role sequence + Output format + Inertia framing (ceiling) | PASS | PASS | Three-axis combination; all phase outputs in tables; inertia competitor named in preamble title line and referenced on seven structural surfaces (five Thread 1 + two BUILD phase MEASURER B-00 references); C-52 consequence clause with maximum binding — names both the inventory and the pre-execution compliance assertion derived from it |

---

## V-01 — Role Sequence

**Axis:** Role sequence — BUILD container split into IMPLEMENTER and MEASURER sub-roles, architecturally mirrored to CLOSE's COMPARATOR/AUDITOR contamination guard. Each intra-container boundary carries explicit prohibitions, a model-written handoff declaration, and a downstream acknowledgment gate.

**Hypothesis:** C-52 adds a layer C-50 cannot reach: C-50's REQUIRED closure asserts compliance but does not state what happens to that assertion if a marker is embedded in prose. Adding the consequence clause ("voids this C-50 inventory, retroactively invalidating this pre-execution compliance claim") binds the opening contract to its post-violation state. The structural root cause identified in R19 — that a monolithic BUILD caps Thread 2 at three markers, making C-49 5:5 parity unreachable — is resolved by the IMPLEMENTER/MEASURER split in V-01. V-01 tests C-51 + C-52 in the cleanest single-axis form, using formal register throughout.

---

You are running a prototype signal for topic: **{{topic}}**

---

### MANIFEST PREAMBLE

The following two threads propagate through every CONTAINER COMPLETE boundary in this document and converge at the terminal CLOSE COMPLETE line.

**Thread declarations** — both threads are co-primary propagating commitments. Declare them as rows in the table below. Both rows MUST carry equivalent depth in every column — a row with single-phrase entries where the other row has multi-clause entries does not satisfy construction-enforced co-equality.

| Thread | Scope | Key structural markers | Terminal discharge obligation |
|--------|-------|----------------------|------------------------------|
| **Thread 1 — Competitor lifecycle** | Four-state progression: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED. Tracks the inertia competitor across all container boundaries, with identification gated at CALIBRATE and discharge confirmed at CLOSE COMPLETE. Lifecycle state tracked in the manifest Competitor Status column at every container. | Five surfaces: manifest Competitor Status column (one state per container row); CONTAINER COMPLETE lifecycle annotations naming the competitor's state at each boundary; CALIBRATE body naming the competitor explicitly (C-29); CALIBRATE COMPLETE embedding competitor name + B-00 + threshold (C-32); results table baseline column labeled with competitor name (C-34); CLOSE COMPLETE terminal arc record embedding competitor name (C-36). | CLOSE COMPLETE carries the verbatim four-state chain: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED confirming Thread 1 closure. |
| **Thread 2 — Role sequencing (BUILD + CLOSE)** | Two intra-container sub-role boundaries with symmetric structure: BUILD — IMPLEMENTER (Phase 7: prototype construction and delivery) hands off to MEASURER (Phase 8: measurement against B-00 and outperform threshold); CLOSE — COMPARATOR (Phases 9–10: comparison and verdict) hands off to AUDITOR (Phases 11–13: counter-evidence, limitations, replication). All four sub-roles carry explicit prohibitions with hard modal operators; both handoffs carry model-written declarations and downstream acknowledgment gates. | Five structural markers: Phase 7 IMPLEMENTER COMPLETE handoff declaration naming the artifact passed to MEASURER; Phase 8 MEASURER entry REQUIRED prerequisite gate confirming Phase 7 handoff is present; Phase 10 COMPARATOR COMPLETE handoff declaration naming the verdict passed to AUDITOR; Phase 11 AUDITOR entry REQUIRED prerequisite gate confirming Phase 10 handoff is present; CLOSE COMPLETE sub-role contract discharge confirmation for both intra-container boundaries. | CLOSE COMPLETE carries IMPLEMENTER/MEASURER contract: DISCHARGED and COMPARATOR/AUDITOR contract: DISCHARGED — two distinct discharge confirmations, each named separately from Thread 1 lifecycle chain and the C-36 arc record. |

---

### Structural Marker Inventory

This section appears before any container body executes. It catalogs every structural marker required by C-43, C-44, and C-45, establishing C-48 compliance as a verifiable document property before a reader encounters any container.

| Marker type | Required by | Location | Form |
|-------------|-------------|----------|------|
| Lifecycle framing paragraph | C-43 | Dedicated section before the manifest table — NOT merged with the manifest header or placed inside any container body | Standalone labeled section (## Competitor Lifecycle Framing) separate from all container content |
| Per-container incoming-state annotations | C-43 | Each container header line — NOT as a sentence within the first phase body paragraph | Labeled element on the container header: e.g., `incoming lifecycle state: NOT YET IDENTIFIED` |
| Phase 11 AUDITOR prerequisite gate | C-44 | Phase 11 entry point in CLOSE, before AUDITOR writes any content — NOT as a sentence within the Phase 11 instructional block | REQUIRED-prefixed standalone gate line: `REQUIRED: Confirm Phase 10 COMPARATOR handoff marker present before executing Phase 11` |
| CONTAINER COMPLETE thread labels | C-45 | Each CONTAINER COMPLETE line — NOT as paraphrased status notes embedded in completion prose | Explicitly labeled elements: `Thread 1: [state] | Thread 2: [status]` |

REQUIRED: All four marker types listed above MUST appear as standalone labeled elements in this document. A marker embedded only in prose — legible when the surrounding paragraph is read but not independently verifiable by scanning — fails C-48 and voids this C-50 inventory, retroactively invalidating the pre-execution compliance claim made by this section.

---

### Competitor Lifecycle Framing

The inertia competitor follows a four-state progression across this document: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED.

**Why each transition is gated at a specific container boundary:**

- **DESIGN boundary (NOT YET IDENTIFIED):** Naming the incumbent before measurement criteria are finalized allows known-competitor feature sets to contaminate scope decisions. The isolation purpose: DESIGN establishes what to measure and why — scope decisions MUST be driven by the hypothesis, not by the competitor's known capabilities. Competitor identification is FORBIDDEN in DESIGN.
- **CALIBRATE boundary (IDENTIFIED AND COMMITTED):** CALIBRATE names the competitor, measures its baseline (B-00), and commits an outperform threshold. Two sub-transitions occur here: NOT YET IDENTIFIED → IDENTIFIED (competitor named in body) and IDENTIFIED → IDENTIFIED AND COMMITTED (B-00 locked and threshold stated in CALIBRATE COMPLETE). Both sub-transitions are REQUIRED before BUILD begins. Allowing the competitor to remain unidentified through CALIBRATE would allow BUILD to execute without a committed baseline, enabling retroactive threshold adjustment after results are seen.
- **BUILD boundary (REFERENCED):** BUILD references the inertia competitor's committed baseline when executing measurements — it uses B-00 but MUST NOT alter it. Competitor baseline is FROZEN at CALIBRATE COMPLETE; any BUILD-phase reassessment fails the gate.
- **CLOSE boundary (DISCHARGED):** CLOSE references the competitor at the results table (baseline column labeled with competitor name, C-34) and at the terminal arc record (C-36). DISCHARGED status is confirmed when CLOSE COMPLETE carries the full four-state chain verbatim.

---

### Document Manifest

| Container | Principal purpose | Expected output | Competitor status |
|-----------|-------------------|-----------------|-------------------|
| DESIGN | Lock the hypothesis, scope, and measurement criteria before any construction begins | Hypothesis statement, scope boundary with named exclusion, success and failure thresholds | NOT YET IDENTIFIED |
| CALIBRATE | Identify the inertia competitor, measure its baseline (B-00), and commit the outperform threshold | Competitor name + rationale, B-00 value, outperform threshold — all locked before BUILD | IDENTIFIED AND COMMITTED |
| BUILD | IMPLEMENTER constructs the prototype artifact; MEASURER executes measurements and records raw data | Prototype artifact description (IMPLEMENTER output), raw measurement data and actual vs. predicted delta (MEASURER output) | REFERENCED |
| CLOSE | COMPARATOR compares prototype to inertia competitor and renders verdict; AUDITOR examines counter-evidence, limitations, and replication path | Comparison table, verdict, counter-evidence disposition, limitations, replication instructions | DISCHARGED |

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

VALUES MUST NOT be consumed before the producing phase executes. Gate markers enforce this ordering; Phase 7 REQUIRED to precede Phase 8 by IMPLEMENTER COMPLETE handoff; Phase 10 REQUIRED to precede Phase 11 by COMPARATOR handoff.

---

### CONTAINER: DESIGN
**incoming lifecycle state: NOT YET IDENTIFIED — competitor identification FORBIDDEN in this container**
**Entry contract:** This container MUST establish (1) a testable hypothesis, (2) a scope boundary with at least one named exclusion, and (3) explicit success and failure thresholds — before any BUILD or CALIBRATE content is produced.

**Role: DESIGNER**
DESIGNER writes: hypothesis, scope, measurement criteria.
DESIGNER MUST NOT write: competitor names, baseline measurements, prototype construction steps, results, or verdicts.

**Phase 1 — Hypothesis**
State the testable claim for {{topic}}. Name the behavior or property being tested. The claim must be falsifiable: a result that would confirm it and a result that would refute it must both be statable.

GATE: Hypothesis REQUIRED before Phase 2 executes.

**Phase 2 — Scope**
State what the prototype will and will not do. Name at least one deliberate exclusion and explain why that exclusion does not prevent testing the hypothesis.

GATE: Scope boundary REQUIRED before Phase 3 executes.

**Phase 3 — Measurement Criteria**
Define success and failure thresholds before any construction begins. State: what to measure, the unit of measurement, the value that confirms the hypothesis, and the value that refutes it.

GATE: Success and failure thresholds REQUIRED before DESIGN COMPLETE.

**DESIGN COMPLETE**
Record: hypothesis text (verbatim) | scope boundary | success threshold | failure threshold.
→ CALIBRATE receives: hypothesis text, measurement unit, success threshold, failure threshold.
Thread 1: NOT YET IDENTIFIED | Thread 2: BUILD and CLOSE sub-roles declared, no handoffs yet executed

---

### CONTAINER: CALIBRATE
**incoming lifecycle state: NOT YET IDENTIFIED — identification REQUIRED in this container, FORBIDDEN to carry forward unidentified**
**Entry contract:** This container MUST execute three steps in order: (1) name the inertia competitor with rationale, (2) measure B-00 against the same metric defined in DESIGN Phase 3, (3) commit an outperform threshold. All three REQUIRED before BUILD.

**Role: CALIBRATOR**
CALIBRATOR writes: competitor identification, baseline measurement, threshold commitment.
CALIBRATOR MUST NOT write: prototype construction steps, results from the prototype, or verdict language.

**Phase 4 — Inertia Competitor Identification**
Name the status-quo approach or tool that the prototype must outperform to justify adoption. State why this is the correct baseline: what problem it currently solves for {{topic}} and why teams would continue using it absent a compelling alternative.

GATE: Competitor name and rationale REQUIRED before Phase 5 executes.

**Phase 5 — Baseline Measurement (B-00)**
Measure the inertia competitor's performance on the exact metric defined in DESIGN Phase 3. Record the raw result as B-00. This is the committed baseline — it cannot be revised after CALIBRATE COMPLETE.

GATE: B-00 value REQUIRED before Phase 6 executes.

**Phase 6 — Outperform Threshold**
State the threshold the prototype must exceed to warrant displacing the inertia competitor. The threshold must be more stringent than B-00 by a margin that reflects genuine improvement, not noise.

GATE: Outperform threshold REQUIRED before CALIBRATE COMPLETE.

**CALIBRATE COMPLETE**
Record: competitor name | B-00 value | outperform threshold. All three values REQUIRED on this line.
→ BUILD receives: competitor name (for REFERENCED state), B-00 (frozen baseline), outperform threshold (pass criterion).
Thread 1: IDENTIFIED AND COMMITTED (competitor: [name], B-00: [value], threshold: [value]) | Thread 2: no handoffs yet executed

---

### CONTAINER: BUILD
**incoming lifecycle state: IDENTIFIED AND COMMITTED — competitor is named and baseline is locked; BUILD references B-00 but MUST NOT alter it**
**Entry contract:** BUILD executes in two sub-roles with a mandatory handoff at the Phase 7/8 boundary. IMPLEMENTER builds and delivers the prototype artifact; MEASURER receives it, executes measurements, and records raw data. Neither sub-role may perform the other's function.

**Sub-role IMPLEMENTER** (Phase 7)
IMPLEMENTER writes: prototype construction description, artifact deliverable.
IMPLEMENTER FORBIDDEN to: record measurements, interpret results, reference B-00 in comparison language, or produce any verdict-adjacent language.

**Phase 7 — Prototype Construction**
Build the minimal prototype that tests the hypothesis. Describe what was built: the key components, the approach, and any implementation decisions that affect what can and cannot be measured. The artifact must be sufficiently described that a reader could reproduce it.

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
Execute the measurements defined in DESIGN Phase 3 against the prototype artifact received from IMPLEMENTER. Record raw data. State the predicted result (from DESIGN thresholds) alongside the actual result. Record the delta.

GATE: Raw data and actual vs. predicted delta REQUIRED before BUILD COMPLETE.

**BUILD COMPLETE**
Record: prototype description | raw measurement result | predicted value | actual value | delta.
→ CLOSE receives: raw data, actual vs. predicted delta, competitor name (for REFERENCED → DISCHARGED transition).
Thread 1: REFERENCED (competitor baseline B-00 used in measurement) | Thread 2: IMPLEMENTER/MEASURER handoff executed and discharged

---

### CONTAINER: CLOSE
**incoming lifecycle state: REFERENCED — competitor transitions to DISCHARGED upon CLOSE COMPLETE**
**Entry contract:** CLOSE executes in two sub-roles. COMPARATOR (Phases 9–10) performs comparison and renders verdict. AUDITOR (Phases 11–13) examines counter-evidence, states limitations, and provides replication path. Cross-prohibitions enforced with hard modal operators throughout.

**Sub-role COMPARATOR** (Phases 9–10)
COMPARATOR writes: results comparison, verdict.
COMPARATOR FORBIDDEN to write: counter-evidence disposition, limitations, or replication content.

**Phase 9 — Results Table**
Produce a three-column results table: Metric | Inertia competitor ([name], B-00) | Prototype result. Include at least one quantified row. The baseline column MUST be labeled with the inertia competitor name, not a generic "Baseline" label.

GATE: Results table with competitor-named baseline column REQUIRED before Phase 10 executes.

**Phase 10 — Verdict**
State whether the hypothesis is confirmed, refuted, or inconclusive. The verdict MUST follow from the results table — cite the specific delta and whether it clears the outperform threshold. State the actual result vs. the predicted result explicitly.

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
- Competitor lifecycle: DISCHARGED

---

---

## V-02 — Output Format

**Axis:** Output format — all phase outputs anchored in structured tables; no prose bullet lists for enumerable information. The BUILD container now includes the IMPLEMENTER/MEASURER sub-role split (R19 V-02 used a monolithic BUILDER and capped Thread 2 at three structural markers, making C-49 5:5 parity unreachable). Adding IMPLEMENTER COMPLETE and MEASURER prerequisite gate as table elements makes the two new Thread 2 markers visually continuous with the document's structural convention.

**Hypothesis:** Table format and the BUILD sub-role split interact: when every phase output is already a table, the IMPLEMENTER COMPLETE handoff declaration and the MEASURER prerequisite gate read as table rows rather than prose annotations, preventing register drift between the structural handoff mechanism and the surrounding content. C-52 consequence clause ensures the inventory's REQUIRED closure names the document property voided — not just the criterion failed — binding the pre-execution compliance claim to its post-violation state.

---

You are running a prototype signal for topic: **{{topic}}**

---

### MANIFEST PREAMBLE

**Thread declarations** — Thread 1 and Thread 2 are co-primary propagating commitments. Declare them as rows in the table below. Both rows MUST carry equivalent depth in every column. A table where one row has multi-clause entries and the other has single-phrase entries does not satisfy C-49.

| Thread | Scope | Key structural markers | Terminal discharge obligation |
|--------|-------|----------------------|------------------------------|
| **Thread 1 — Competitor lifecycle** | Four-state progression: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED. Competitor identification gated at CALIBRATE; B-00 frozen at CALIBRATE COMPLETE; competitor referenced in BUILD measurements; lifecycle discharged at CLOSE COMPLETE. Lifecycle state tracked at every CONTAINER COMPLETE boundary. | Five structural surfaces: manifest Competitor Status column tracking state per container; CONTAINER COMPLETE lifecycle state annotations; CALIBRATE body (competitor name + rationale, C-29); CALIBRATE COMPLETE triple (competitor name + B-00 + threshold, C-32); results table baseline column labeled with competitor name (C-34); terminal arc record embedding competitor name (C-36). | CLOSE COMPLETE carries verbatim four-state chain: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED. |
| **Thread 2 — Role sequencing (BUILD + CLOSE)** | Four named sub-roles across two containers: IMPLEMENTER (Phase 7, BUILD, construction) and MEASURER (Phase 8, BUILD, measurement); COMPARATOR (Phases 9–10, CLOSE, comparison and verdict) and AUDITOR (Phases 11–13, CLOSE, counter-evidence and audit). All four sub-role phase scopes are disjoint; cross-contamination prohibited by hard modal operators at both container-level and phase-level markers. | Five structural markers: Phase 7 IMPLEMENTER COMPLETE handoff declaration (table row); Phase 8 MEASURER entry REQUIRED prerequisite gate (table row); Phase 10 COMPARATOR COMPLETE handoff declaration (table row); Phase 11 AUDITOR entry REQUIRED prerequisite gate (table row); CLOSE COMPLETE sub-role contract discharge table with both contracts listed. | CLOSE COMPLETE carries a sub-role contract table with two rows: IMPLEMENTER/MEASURER contract: DISCHARGED and COMPARATOR/AUDITOR contract: DISCHARGED. Both distinct from Thread 1 lifecycle chain. |

---

### Structural Marker Inventory

| Marker type | Required by | Location | Form |
|-------------|-------------|----------|------|
| Lifecycle framing paragraph | C-43 | Dedicated section before the manifest table — NOT merged with the manifest header, NOT placed inside any container body | Standalone labeled section with its own heading, separate from all container headers and phase bodies |
| Per-container incoming-state annotations | C-43 | Each container header line — NOT as a sentence within the first phase body paragraph or the container's entry contract | Labeled element directly on the container header line, e.g., `incoming lifecycle state: NOT YET IDENTIFIED` |
| Phase 11 AUDITOR prerequisite gate | C-44 | Phase 11 entry point, before AUDITOR writes any Phase 11 content — NOT embedded as a sentence within Phase 11's instructional prose | REQUIRED-prefixed standalone gate line appearing before the Phase 11 body |
| CONTAINER COMPLETE thread labels | C-45 | Each CONTAINER COMPLETE line — NOT as paraphrased status notes absorbed into the completion line's prose summary | Explicitly labeled elements: `Thread 1: [state] | Thread 2: [status]` as distinct labeled tokens on the COMPLETE line |

REQUIRED: All four marker types listed above MUST appear as standalone labeled elements in this document. A marker embedded only in prose — legible when the surrounding paragraph is read but not independently verifiable by scanning — fails C-48 and voids this C-50 inventory, retroactively invalidating the pre-execution compliance claim made by this section.

---

### Competitor Lifecycle Framing

| Container boundary | Incoming state | Gate | Contamination risk prevented | Isolation purpose |
|-------------------|---------------|------|------------------------------|-------------------|
| DESIGN entry | NOT YET IDENTIFIED | Competitor identification FORBIDDEN | Known competitor features contaminating scope and measurement criteria | Scope and measurement criteria driven by the hypothesis, not by competitive positioning |
| CALIBRATE entry | NOT YET IDENTIFIED | Identification REQUIRED in this container | Competitor remaining unidentified through CALIBRATE, enabling retroactive threshold adjustment after results are seen | Baseline and threshold committed before BUILD begins; outperform criterion independent of prototype results |
| BUILD entry | IDENTIFIED AND COMMITTED | B-00 FROZEN — MUST reference, MUST NOT alter | MEASURER re-assessing B-00 after observing prototype results | Measurement executed against a pre-committed baseline; delta is a genuine result |
| CLOSE entry | REFERENCED | Thread 1 REQUIRED to close with verbatim four-state chain at CLOSE COMPLETE | Competitor lifecycle closing implicitly without explicit confirmation | Explicit chain at CLOSE COMPLETE makes Thread 1 verifiable by scanning the terminal line |

---

### Document Manifest

| Container | Principal purpose | Expected output format | Competitor status |
|-----------|-------------------|----------------------|-------------------|
| DESIGN | Lock hypothesis, scope, measurement criteria | Hypothesis table, scope table, measurement criteria table | NOT YET IDENTIFIED |
| CALIBRATE | Name inertia competitor, lock B-00, commit outperform threshold | Competitor identification table, baseline measurement table, threshold commitment table | IDENTIFIED AND COMMITTED |
| BUILD | IMPLEMENTER constructs; MEASURER executes measurements | Construction table (IMPLEMENTER), measurement results table (MEASURER) | REFERENCED |
| CLOSE | COMPARATOR compares + verdicts; AUDITOR audits | Results comparison table, verdict table, counter-evidence table, limitations table, replication table | DISCHARGED |

---

### Value Flow Ledger

| Value | Produced in | First consumed in |
|-------|-------------|-------------------|
| Hypothesis text | DESIGN Phase 1 (hypothesis table) | CALIBRATE Phase 4 |
| Scope boundary + named exclusion | DESIGN Phase 2 (scope table) | BUILD Phase 7 (IMPLEMENTER) |
| Measurement unit | DESIGN Phase 3 (criteria table) | CALIBRATE Phase 5 (same unit for B-00) |
| Success threshold | DESIGN Phase 3 | CLOSE Phase 9 (comparison) |
| Failure threshold | DESIGN Phase 3 | CLOSE Phase 9 (comparison) |
| Predicted result | DESIGN Phase 3 | CLOSE Phase 10 (actual vs. predicted) |
| Competitor name | CALIBRATE Phase 4 | CALIBRATE COMPLETE, results table baseline label, CLOSE COMPLETE arc |
| B-00 | CALIBRATE Phase 5 | CALIBRATE COMPLETE, BUILD Phase 8 (MEASURER reference), CLOSE Phase 9 |
| Outperform threshold | CALIBRATE Phase 6 | CALIBRATE COMPLETE, CLOSE Phase 10 |
| Prototype artifact | BUILD Phase 7 (IMPLEMENTER) | BUILD Phase 8 (MEASURER handoff), CLOSE COMPLETE arc |
| Raw measurement data | BUILD Phase 8 (MEASURER) | CLOSE Phase 9 (COMPARATOR) |
| Actual vs. predicted delta | BUILD Phase 8 (MEASURER) | CLOSE Phase 10 (verdict) |
| Verdict word | CLOSE Phase 10 (COMPARATOR) | CLOSE COMPLETE arc |
| Counter-evidence disposition | CLOSE Phase 11 (AUDITOR) | CLOSE COMPLETE arc |

VALUES MUST NOT be consumed before the producing phase executes.

---

### CONTAINER: DESIGN
**incoming lifecycle state: NOT YET IDENTIFIED — competitor identification FORBIDDEN**
**Entry contract:** Produce three tables: (1) hypothesis table, (2) scope table, (3) measurement criteria table. All three REQUIRED before DESIGN COMPLETE. No prose bullets — all enumerable output goes in tables.

**Role: DESIGNER**
DESIGNER MUST write: hypothesis table, scope table, measurement criteria table.
DESIGNER FORBIDDEN to write: competitor names, baseline data, construction steps, results, or verdicts.

**Phase 1 — Hypothesis Table**

| Field | Value |
|-------|-------|
| Testable claim | (state the behavior or property to be tested for {{topic}}) |
| Confirming result | (what outcome confirms the hypothesis) |
| Refuting result | (what outcome refutes the hypothesis) |

GATE: Hypothesis table complete — proceeding to Phase 2.

**Phase 2 — Scope Table**

| Field | Value |
|-------|-------|
| What the prototype includes | (specific scope) |
| What is explicitly excluded | (at least one named exclusion) |
| Why exclusion preserves testability | (reason) |

GATE: Scope table complete — proceeding to Phase 3.

**Phase 3 — Measurement Criteria Table**

| Metric | Unit | Success threshold | Failure threshold | Predicted result |
|--------|------|-------------------|-------------------|-----------------|
| (fill) | (fill) | (fill) | (fill) | (fill) |

GATE: Measurement criteria table complete — proceeding to DESIGN COMPLETE.

**DESIGN COMPLETE**
Record: hypothesis (verbatim) | scope boundary | success threshold | failure threshold | predicted result.
→ CALIBRATE receives: hypothesis text, metric + unit, thresholds, predicted result.
Thread 1: NOT YET IDENTIFIED | Thread 2: four sub-roles declared (IMPLEMENTER, MEASURER, COMPARATOR, AUDITOR), no handoffs executed

---

### CONTAINER: CALIBRATE
**incoming lifecycle state: NOT YET IDENTIFIED — identification REQUIRED before CALIBRATE COMPLETE; FORBIDDEN to proceed to BUILD without committing all three values**
**Entry contract:** Three tables: (1) competitor identification table, (2) baseline measurement table, (3) threshold commitment table. All three REQUIRED before CALIBRATE COMPLETE.

**Role: CALIBRATOR**
CALIBRATOR MUST write: competitor identification table, B-00 table, threshold table.
CALIBRATOR FORBIDDEN to write: construction steps, prototype results, or verdict language.

**Phase 4 — Competitor Identification Table**

| Field | Value |
|-------|-------|
| Competitor name | (the status-quo tool or approach for {{topic}}) |
| Problem it currently solves | (specific to {{topic}}) |
| Adoption inertia rationale | (why teams continue using it absent a better alternative) |

GATE: Competitor identification table complete — proceeding to Phase 5.

**Phase 5 — Baseline Measurement Table (B-00)**

| Field | Value |
|-------|-------|
| Metric measured | (same as Phase 3) |
| B-00 value | (measured result for the inertia competitor) |
| Measurement method | (how B-00 was obtained) |
| Frozen status | COMMITTED — MUST NOT be altered after CALIBRATE COMPLETE |

GATE: B-00 table with COMMITTED status complete — proceeding to Phase 6.

**Phase 6 — Threshold Commitment Table**

| Field | Value |
|-------|-------|
| Outperform threshold | (value prototype must exceed) |
| Margin above B-00 | (the margin expressed as a delta) |
| Justification for margin | (why this margin reflects genuine improvement, not noise) |

GATE: Threshold table complete — proceeding to CALIBRATE COMPLETE.

**CALIBRATE COMPLETE**
Record: competitor name | B-00 | outperform threshold — all three REQUIRED.
→ BUILD receives: competitor name (REFERENCED state begins), B-00 (frozen), outperform threshold.
Thread 1: IDENTIFIED AND COMMITTED (competitor: [name], B-00: [value], threshold: [value]) | Thread 2: no handoffs yet executed

---

### CONTAINER: BUILD
**incoming lifecycle state: IDENTIFIED AND COMMITTED — B-00 is FROZEN; MEASURER MUST reference it, MUST NOT alter it**
**Entry contract:** IMPLEMENTER produces the construction table (Phase 7) and executes IMPLEMENTER COMPLETE handoff; MEASURER confirms the handoff gate and produces the measurement results table (Phase 8). Both tables and the handoff/gate sequence REQUIRED before BUILD COMPLETE.

**Sub-role IMPLEMENTER** (Phase 7)
IMPLEMENTER MUST write: construction table.
IMPLEMENTER FORBIDDEN to: record measurements, reference B-00 in comparison language, or produce verdict-adjacent content.

**Phase 7 — Prototype Construction Table**

| Field | Value |
|-------|-------|
| What was built | (prototype name and description) |
| Key components | (what the prototype consists of) |
| Implementation decisions affecting measurement | (choices that constrain what can and cannot be measured) |
| Artifact deliverable to MEASURER | (the artifact MEASURER will run measurements against) |

GATE: Construction table complete — proceeding to IMPLEMENTER COMPLETE.

**IMPLEMENTER COMPLETE — REQUIRED handoff to MEASURER**

| Handoff element | Value |
|-----------------|-------|
| Artifact delivered | (prototype name/description from Phase 7) |
| Handoff declaration | IMPLEMENTER responsibilities discharged — REQUIRED handoff to MEASURER for Phase 8 |
| Thread 2 | IMPLEMENTER handoff declared — MEASURER REQUIRED to confirm gate before Phase 8 |

**Sub-role MEASURER** (Phase 8)

| Gate | Status |
|------|--------|
| Phase 7 IMPLEMENTER handoff marker present? | REQUIRED — confirm before executing Phase 8 |

MEASURER MUST write: measurement results table.
MEASURER FORBIDDEN to: alter prototype behavior, modify B-00, adjust outperform threshold, or produce verdict language.

**Phase 8 — Measurement Results Table**

| Field | Value |
|-------|-------|
| Metric measured | (same as DESIGN Phase 3) |
| Predicted value | (from Phase 3 measurement criteria table) |
| Actual measured value | (raw result from prototype) |
| Delta (actual minus predicted) | (value) |
| B-00 reference | (competitor baseline, not re-measured — value from CALIBRATE Phase 5) |
| Outperform threshold | (from CALIBRATE Phase 6) |
| Outperform threshold cleared? | YES / NO |

GATE: Measurement results table complete — proceeding to BUILD COMPLETE.

**BUILD COMPLETE**
Record: prototype artifact | actual value | predicted value | delta | threshold cleared (YES/NO).
→ CLOSE receives: measurement results table, actual vs. predicted delta, competitor name (for REFERENCED → DISCHARGED transition).
Thread 1: REFERENCED (B-00 referenced in measurement, competitor: [name]) | Thread 2: IMPLEMENTER/MEASURER handoff executed and discharged

---

### CONTAINER: CLOSE
**incoming lifecycle state: REFERENCED — competitor MUST reach DISCHARGED at CLOSE COMPLETE**
**Entry contract:** COMPARATOR produces results comparison table + verdict table (Phases 9–10), then COMPARATOR COMPLETE handoff to AUDITOR for counter-evidence table + limitations table + replication table (Phases 11–13). All five tables and the handoff/gate sequence REQUIRED.

**Sub-role COMPARATOR** (Phases 9–10)
COMPARATOR MUST write: results comparison table, verdict table.
COMPARATOR FORBIDDEN to write: counter-evidence, limitations, or replication content.

**Phase 9 — Results Comparison Table**
Baseline column MUST be labeled with the inertia competitor name.

| Metric | Inertia competitor ([name], B-00) | Prototype result | Delta | Outperform threshold | Threshold cleared? |
|--------|-----------------------------------|-----------------|-------|---------------------|-------------------|
| (fill) | (fill) | (fill) | (fill) | (fill) | YES / NO |

GATE: Results table with competitor-named baseline written — proceeding to Phase 10.

**Phase 10 — Verdict Table**

| Field | Value |
|-------|-------|
| Verdict | CONFIRMED / REFUTED / INCONCLUSIVE |
| Evidence (cite delta and threshold) | (specific values from Phase 9) |
| Actual result | (from measurement results table) |
| Predicted result | (from DESIGN Phase 3) |
| Actual vs. predicted | (confirmation or mismatch) |

GATE: Verdict table complete — proceeding to COMPARATOR COMPLETE.

**COMPARATOR COMPLETE — REQUIRED handoff to AUDITOR**

| Handoff element | Value |
|-----------------|-------|
| Verdict | (word from Phase 10) |
| Delta | (value from Phase 9) |
| Threshold cleared | YES / NO |
| Handoff declaration | COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR for Phases 11–13 |
| Thread 2 | COMPARATOR handoff declared — AUDITOR REQUIRED to confirm gate before Phase 11 |

**Sub-role AUDITOR** (Phases 11–13)

| Gate | Status |
|------|--------|
| Phase 10 COMPARATOR handoff marker present? | REQUIRED — confirm before executing Phase 11 |

AUDITOR MUST write: counter-evidence table, limitations table, replication table.
AUDITOR FORBIDDEN to write: new measurement criteria, new comparison data, or verdict statements.

**Phase 11 — Counter-Evidence Table**
Binary disposition REQUIRED — both cases handled in the table structure:

| Field | Value |
|-------|-------|
| Counter-interpretation found? | YES / NO |
| Counter-interpretation (if YES) | (name it; leave blank if NO) |
| Rebuttal grounded in results (if YES) | (rebuttal; leave blank if NO) |
| Reason no counter-interpretation exists (if NO) | (explicit reason; leave blank if YES) |

GATE: Counter-evidence binary disposition table complete — proceeding to Phase 12.

**Phase 12 — Limitations Table**

| Limitation | Type | Effect on verdict validity |
|------------|------|---------------------------|
| (at least one row) | scope / fidelity / sample / instrument | (does it affect the verdict?) |

**Phase 13 — Replication Table**

| Step | Tool / Input / Command | Notes |
|------|----------------------|-------|
| (fill all reproduction steps; no implicit steps) | | |

GATE: Replication table complete — proceeding to CLOSE COMPLETE.

**CLOSE COMPLETE**
Record — all elements REQUIRED:

| Element | Value |
|---------|-------|
| Hypothesis verdict | CONFIRMED / REFUTED / INCONCLUSIVE |
| Arc record | competitor [name] \| B-00 [value] \| threshold [value] \| prototype result [value] \| delta [value] \| verdict [word] \| counter-evidence [disposition] |
| Value ledger | FULLY DISCHARGED / PARTIAL — [N] values unresolved |
| Thread 1 lifecycle chain (verbatim) | NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED |
| Thread 2 — IMPLEMENTER/MEASURER contract | DISCHARGED |
| Thread 2 — COMPARATOR/AUDITOR contract | DISCHARGED |
| Competitor lifecycle | DISCHARGED |

---

---

## V-03 — Lifecycle Emphasis

**Axis:** Lifecycle emphasis — per-phase lifecycle state callouts at every phase body entry. This axis is new to R20: prior variations annotate lifecycle state only at CONTAINER COMPLETE boundaries; V-03 annotates it at every individual phase entry. BUILD sub-role state is tracked at phase granularity (IMPLEMENTER active → IMPLEMENTER COMPLETE → MEASURER active), making the handoff transition visible at the moment it occurs rather than only at the BUILD COMPLETE boundary.

**Hypothesis:** Lifecycle drift — a phase executing without the model having recently processed its current lifecycle state — is a risk in long documents. Container-boundary annotations address drift at the macro level; per-phase callouts address it at the micro level. If a model mis-executes Phase 8 as IMPLEMENTER (recording construction decisions when it should be recording measurements), the Phase 8 callout line "Active sub-role: MEASURER | Gate: Phase 7 IMPLEMENTER handoff confirmed" forces an explicit sub-role acknowledgment before any Phase 8 content is written. C-52 ensures the inventory's pre-execution compliance claim is bound to its post-violation consequence.

---

You are running a prototype signal for topic: **{{topic}}**

---

### MANIFEST PREAMBLE

The following two threads propagate through every CONTAINER COMPLETE boundary in this document and converge at the terminal CLOSE COMPLETE line.

**Thread declarations** — both threads are co-primary propagating commitments. Declare them as rows in the table below. Both rows MUST carry equivalent depth in every column.

| Thread | Scope | Key structural markers | Terminal discharge obligation |
|--------|-------|----------------------|------------------------------|
| **Thread 1 — Competitor lifecycle** | Four-state progression: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED. Competitor identification gated at CALIBRATE; B-00 frozen at CALIBRATE COMPLETE; B-00 referenced in BUILD Phase 8; lifecycle discharged at CLOSE COMPLETE. Per-phase lifecycle callout line at every phase entry names the current state. | Five surfaces: per-phase lifecycle callout lines naming state at each phase entry; CONTAINER COMPLETE lifecycle annotations; CALIBRATE body (C-29); CALIBRATE COMPLETE triple (C-32); results table baseline column labeled with competitor name (C-34); CLOSE COMPLETE arc record embedding competitor name (C-36). | CLOSE COMPLETE carries verbatim four-state chain: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED. |
| **Thread 2 — Role sequencing (BUILD + CLOSE)** | IMPLEMENTER (Phase 7, construction) hands off to MEASURER (Phase 8, measurement) within BUILD; COMPARATOR (Phases 9–10, comparison and verdict) hands off to AUDITOR (Phases 11–13, counter-evidence and audit) within CLOSE. Per-phase callout lines name the active sub-role at each phase entry; handoff transitions are announced at phase granularity. | Five structural markers: Phase 7 IMPLEMENTER COMPLETE handoff declaration; Phase 8 MEASURER entry REQUIRED prerequisite gate; Phase 10 COMPARATOR COMPLETE handoff declaration; Phase 11 AUDITOR entry REQUIRED prerequisite gate; CLOSE COMPLETE sub-role contract discharge for both intra-container boundaries. | CLOSE COMPLETE carries IMPLEMENTER/MEASURER contract: DISCHARGED and COMPARATOR/AUDITOR contract: DISCHARGED — two distinct discharge confirmations, each named separately from Thread 1. |

---

### Structural Marker Inventory

This section appears before any container body executes. It catalogs every structural marker required by C-43, C-44, and C-45.

| Marker type | Required by | Location | Form |
|-------------|-------------|----------|------|
| Lifecycle framing paragraph | C-43 | Dedicated section before the manifest table — NOT merged with the manifest header or placed inside any container body | Standalone labeled section (## Competitor Lifecycle Framing) |
| Per-container incoming-state annotations | C-43 | Each container header line — NOT as a sentence within the first phase body paragraph | Labeled element on the container header: `incoming lifecycle state: [state]` |
| Phase 11 AUDITOR prerequisite gate | C-44 | Phase 11 entry point in CLOSE, before AUDITOR writes any content — NOT as a sentence within Phase 11 instructional prose | REQUIRED-prefixed standalone gate line at Phase 11 entry |
| CONTAINER COMPLETE thread labels | C-45 | Each CONTAINER COMPLETE line — NOT as paraphrased status notes embedded in completion prose | Explicitly labeled elements: `Thread 1: [state] | Thread 2: [status]` |

REQUIRED: All four marker types listed above MUST appear as standalone labeled elements in this document. A marker embedded only in prose — legible when the surrounding paragraph is read but not independently verifiable by scanning — fails C-48 and voids this C-50 inventory, retroactively invalidating the pre-execution compliance claim made by this section.

---

### Competitor Lifecycle Framing

The inertia competitor follows a four-state progression across this document: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED. Per-phase lifecycle callout lines annotate the current state at every phase entry, making state transitions visible at phase granularity rather than only at container boundaries.

- **NOT YET IDENTIFIED (DESIGN phases 1–3):** The competitor has not been named. Identification FORBIDDEN. Scope and measurement criteria are hypothesis-driven.
- **NOT YET IDENTIFIED → IDENTIFIED (CALIBRATE Phase 4):** The competitor is named in the CALIBRATE body. This is the first sub-transition.
- **IDENTIFIED → IDENTIFIED AND COMMITTED (CALIBRATE Phases 5–6 and CALIBRATE COMPLETE):** B-00 is measured and the outperform threshold is committed. CALIBRATE COMPLETE locks all three values. This is the second sub-transition.
- **REFERENCED (BUILD phases 7–8):** MEASURER references B-00 by value in Phase 8 but MUST NOT alter it. IMPLEMENTER does not reference B-00.
- **DISCHARGED (CLOSE phases 9–13 and CLOSE COMPLETE):** Competitor is referenced at the results table and arc record. Full four-state chain confirmed at CLOSE COMPLETE.

---

### Document Manifest

| Container | Principal purpose | Expected output | Competitor status |
|-----------|-------------------|-----------------|-------------------|
| DESIGN | Lock hypothesis, scope, measurement criteria | Hypothesis, scope with exclusion, measurement criteria | NOT YET IDENTIFIED |
| CALIBRATE | Name inertia competitor, lock B-00, commit outperform threshold | Competitor identification, B-00, threshold | IDENTIFIED AND COMMITTED |
| BUILD | IMPLEMENTER constructs; MEASURER executes measurements | Construction description, raw measurements, actual vs. predicted | REFERENCED |
| CLOSE | COMPARATOR compares + verdicts; AUDITOR audits | Results table, verdict, counter-evidence, limitations, replication | DISCHARGED |

---

### Value Flow Ledger

| Value | Produced in | First consumed in |
|-------|-------------|-------------------|
| Hypothesis text | DESIGN Phase 1 | CALIBRATE Phase 4 |
| Scope boundary + named exclusion | DESIGN Phase 2 | BUILD Phase 7 (IMPLEMENTER) |
| Success threshold | DESIGN Phase 3 | CLOSE Phase 9 (COMPARATOR) |
| Failure threshold | DESIGN Phase 3 | CLOSE Phase 9 (COMPARATOR) |
| Predicted result | DESIGN Phase 3 | CLOSE Phase 10 (actual vs. predicted) |
| Competitor name | CALIBRATE Phase 4 | CALIBRATE COMPLETE, results table label, CLOSE COMPLETE arc |
| B-00 | CALIBRATE Phase 5 | CALIBRATE COMPLETE, BUILD Phase 8 (MEASURER reference), CLOSE Phase 9 |
| Outperform threshold | CALIBRATE Phase 6 | CALIBRATE COMPLETE, CLOSE Phase 10 |
| Prototype artifact | BUILD Phase 7 (IMPLEMENTER) | BUILD Phase 8 (MEASURER handoff input), CLOSE COMPLETE arc |
| Raw measurement data | BUILD Phase 8 (MEASURER) | CLOSE Phase 9 (COMPARATOR) |
| Actual vs. predicted delta | BUILD Phase 8 (MEASURER) | CLOSE Phase 10 (verdict) |
| Verdict word | CLOSE Phase 10 (COMPARATOR) | CLOSE COMPLETE arc |
| Counter-evidence disposition | CLOSE Phase 11 (AUDITOR) | CLOSE COMPLETE arc |

VALUES MUST NOT be consumed before the producing phase executes.

---

### CONTAINER: DESIGN
**incoming lifecycle state: NOT YET IDENTIFIED — competitor identification FORBIDDEN in this container**
**Entry contract:** Establish (1) hypothesis, (2) scope with exclusion, (3) measurement criteria. All three REQUIRED before DESIGN COMPLETE.

**Role: DESIGNER**
DESIGNER writes: hypothesis, scope, measurement criteria.
DESIGNER MUST NOT write: competitor names, baseline measurements, construction steps, results, or verdicts.

**Phase 1 — Hypothesis**
`Phase callout: DESIGN Phase 1 | Competitor lifecycle: NOT YET IDENTIFIED | Active role: DESIGNER | Thread 2 state: declared, no handoffs executed`

State the testable claim for {{topic}}. Name the behavior or property being tested. State what result would confirm it and what result would refute it.

GATE: Hypothesis REQUIRED before Phase 2 executes.

**Phase 2 — Scope**
`Phase callout: DESIGN Phase 2 | Competitor lifecycle: NOT YET IDENTIFIED | Active role: DESIGNER | Thread 2 state: no handoffs executed`

State what the prototype will and will not do. Name at least one deliberate exclusion and explain why it does not prevent testing the hypothesis.

GATE: Scope boundary REQUIRED before Phase 3 executes.

**Phase 3 — Measurement Criteria**
`Phase callout: DESIGN Phase 3 | Competitor lifecycle: NOT YET IDENTIFIED | Active role: DESIGNER | Thread 2 state: no handoffs executed`

Define success and failure thresholds before any construction begins. State the metric, unit, confirming value, and refuting value.

GATE: Success and failure thresholds REQUIRED before DESIGN COMPLETE.

**DESIGN COMPLETE**
Record: hypothesis text (verbatim) | scope boundary | success threshold | failure threshold.
→ CALIBRATE receives: hypothesis text, measurement unit, success threshold, failure threshold.
Thread 1: NOT YET IDENTIFIED | Thread 2: BUILD and CLOSE sub-roles declared, no handoffs yet executed

---

### CONTAINER: CALIBRATE
**incoming lifecycle state: NOT YET IDENTIFIED — identification REQUIRED in this container**
**Entry contract:** (1) name competitor, (2) measure B-00, (3) commit outperform threshold. All three REQUIRED before CALIBRATE COMPLETE.

**Role: CALIBRATOR**
CALIBRATOR writes: competitor identification, baseline measurement, threshold commitment.
CALIBRATOR MUST NOT write: construction steps, prototype results, or verdict language.

**Phase 4 — Inertia Competitor Identification**
`Phase callout: CALIBRATE Phase 4 | Competitor lifecycle: NOT YET IDENTIFIED → transitioning to IDENTIFIED after this phase | Active role: CALIBRATOR | Thread 2 state: no handoffs executed`

Name the status-quo approach or tool the prototype must outperform to justify adoption. State the problem it solves for {{topic}} and why teams would continue using it absent a compelling alternative.

GATE: Competitor name and rationale REQUIRED before Phase 5 executes.

**Phase 5 — Baseline Measurement (B-00)**
`Phase callout: CALIBRATE Phase 5 | Competitor lifecycle: IDENTIFIED (competitor named in Phase 4) | Active role: CALIBRATOR | Thread 2 state: no handoffs executed`

Measure the inertia competitor's performance on the exact metric defined in DESIGN Phase 3. Record as B-00. This value is the committed baseline — it cannot be revised after CALIBRATE COMPLETE.

GATE: B-00 value REQUIRED before Phase 6 executes.

**Phase 6 — Outperform Threshold**
`Phase callout: CALIBRATE Phase 6 | Competitor lifecycle: IDENTIFIED (B-00 measured; threshold pending) | Active role: CALIBRATOR | Thread 2 state: no handoffs executed`

State the threshold the prototype must exceed to warrant displacing the inertia competitor. The margin above B-00 must reflect genuine improvement, not noise.

GATE: Outperform threshold REQUIRED before CALIBRATE COMPLETE.

**CALIBRATE COMPLETE**
Record: competitor name | B-00 value | outperform threshold. All three REQUIRED.
→ BUILD receives: competitor name (REFERENCED state begins), B-00 (frozen baseline), outperform threshold.
Thread 1: IDENTIFIED AND COMMITTED (competitor: [name], B-00: [value], threshold: [value]) | Thread 2: no handoffs yet executed

---

### CONTAINER: BUILD
**incoming lifecycle state: IDENTIFIED AND COMMITTED — B-00 is FROZEN; BUILD references it but MUST NOT alter it**
**Entry contract:** IMPLEMENTER (Phase 7) constructs the prototype and executes IMPLEMENTER COMPLETE handoff; MEASURER (Phase 8) confirms the handoff gate and executes measurements. Both phases REQUIRED.

**Sub-role IMPLEMENTER** (Phase 7)
IMPLEMENTER writes: prototype construction description, artifact deliverable.
IMPLEMENTER FORBIDDEN to: record measurements, interpret results, reference B-00 in comparison language, or produce verdict-adjacent language.

**Phase 7 — Prototype Construction**
`Phase callout: BUILD Phase 7 | Competitor lifecycle: IDENTIFIED AND COMMITTED | Active sub-role: IMPLEMENTER | BUILD sub-role state: CONSTRUCTION PHASE — no measurements in this phase | Thread 2 state: IMPLEMENTER active, no handoff yet`

Build the minimal prototype that tests the hypothesis. Describe what was built: key components, approach, and any implementation decisions that affect what can and cannot be measured.

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
`Phase callout: BUILD Phase 8 | Competitor lifecycle: REFERENCED (B-00 in use) | Active sub-role: MEASURER | BUILD sub-role state: MEASUREMENT PHASE — GATE: Phase 7 IMPLEMENTER handoff marker MUST be confirmed present before writing Phase 8 content | Thread 2 state: IMPLEMENTER COMPLETE, MEASURER executing`

Execute the measurements defined in DESIGN Phase 3 against the prototype artifact. Record raw data. State the predicted result alongside the actual result. Record the delta.

GATE: Raw data and actual vs. predicted delta REQUIRED before BUILD COMPLETE.

**BUILD COMPLETE**
Record: prototype description | raw measurement result | predicted value | actual value | delta.
→ CLOSE receives: raw data, actual vs. predicted delta, competitor name (for REFERENCED → DISCHARGED transition).
Thread 1: REFERENCED (competitor baseline B-00 used in measurement) | Thread 2: IMPLEMENTER/MEASURER handoff executed and discharged

---

### CONTAINER: CLOSE
**incoming lifecycle state: REFERENCED — competitor transitions to DISCHARGED upon CLOSE COMPLETE**
**Entry contract:** COMPARATOR (Phases 9–10) compares and verdicts; AUDITOR (Phases 11–13) audits counter-evidence, limitations, replication. Cross-prohibitions enforced throughout.

**Sub-role COMPARATOR** (Phases 9–10)
COMPARATOR writes: results comparison, verdict.
COMPARATOR FORBIDDEN to write: counter-evidence, limitations, or replication content.

**Phase 9 — Results Table**
`Phase callout: CLOSE Phase 9 | Competitor lifecycle: REFERENCED → transitioning to DISCHARGED by CLOSE COMPLETE | Active sub-role: COMPARATOR | Thread 2 state: COMPARATOR active, no handoff yet`

Produce a results table: Metric | Inertia competitor ([name], B-00) | Prototype result. Baseline column MUST be labeled with the competitor name.

GATE: Results table with competitor-named baseline REQUIRED before Phase 10 executes.

**Phase 10 — Verdict**
`Phase callout: CLOSE Phase 10 | Competitor lifecycle: REFERENCED | Active sub-role: COMPARATOR | Thread 2 state: COMPARATOR active`

State confirmed, refuted, or inconclusive. Cite the specific delta and whether it clears the outperform threshold. State actual vs. predicted explicitly.

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
`Phase callout: CLOSE Phase 11 | Competitor lifecycle: REFERENCED | Active sub-role: AUDITOR | BUILD sub-role state: N/A | GATE: Phase 10 COMPARATOR handoff marker MUST be confirmed present before writing Phase 11 content | Thread 2 state: COMPARATOR COMPLETE, AUDITOR executing`

Close the counter-evidence question with one of two explicit dispositions: (a) name a counter-interpretation and rebut it with reasoning grounded in the results, or (b) state explicitly that no plausible counter-interpretation exists, with a reason.

GATE: Binary counter-evidence disposition REQUIRED before Phase 12 executes.

**Phase 12 — Limitations**
`Phase callout: CLOSE Phase 12 | Competitor lifecycle: REFERENCED | Active sub-role: AUDITOR | Thread 2 state: AUDITOR executing`

State at least one limitation. Explain whether it affects the verdict's validity.

**Phase 13 — Replication Path**
`Phase callout: CLOSE Phase 13 | Competitor lifecycle: REFERENCED (approaching DISCHARGED at CLOSE COMPLETE) | Active sub-role: AUDITOR | Thread 2 state: AUDITOR executing`

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
- Competitor lifecycle: DISCHARGED

---

---

## V-04 — Role Sequence + Phrasing Register

**Axis:** Role sequence (IMPLEMENTER/MEASURER split in BUILD) combined with phrasing register (conversational second-person imperative throughout; model addressed directly at every structural command).

**Hypothesis:** Second-person imperative reduces the translation step between structural rule and self-directed action. "You are IMPLEMENTER — you MUST NOT write measurements in Phase 7" is more directly executable than "IMPLEMENTER MUST NOT write measurements." The C-52 consequence clause in second-person form ("a marker embedded in prose fails C-48 and voids this C-50 inventory you just wrote") binds the closure to the model's own prior action — making the consequence claim self-referential in a way the third-person form cannot. Combined with the BUILD sub-role split, this variation tests whether conversational directness amplifies contamination-guard compliance at the intra-container handoff boundaries.

---

You are running a prototype signal for topic: **{{topic}}**

---

### MANIFEST PREAMBLE

Before you write anything else, write a two-row thread declaration table. Use the exact column schema below. You MUST fill both rows with equivalent depth in every column — if your Thread 1 Scope entry covers three clauses, your Thread 2 Scope entry must also cover three clauses. This is construction-enforced co-equality.

| Thread | Scope | Key structural markers | Terminal discharge obligation |
|--------|-------|----------------------|------------------------------|
| **Thread 1 — Competitor lifecycle** | Four-state progression NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED, gated at CALIBRATE (identification) and CLOSE COMPLETE (discharge). Lifecycle state tracked at every CONTAINER COMPLETE boundary via the manifest Competitor Status column. | Five surfaces: manifest Competitor Status column; CONTAINER COMPLETE lifecycle annotations; CALIBRATE body (C-29); CALIBRATE COMPLETE triple — competitor name + B-00 + threshold (C-32); results table baseline column labeled with competitor name (C-34); CLOSE COMPLETE arc record (C-36). | At CLOSE COMPLETE: verbatim four-state chain NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED confirming Thread 1 fully closed. |
| **Thread 2 — Role sequencing (BUILD + CLOSE)** | Two intra-container handoff boundaries: (1) BUILD — you are IMPLEMENTER in Phase 7 (construction), then you become MEASURER in Phase 8 (measurement); (2) CLOSE — you are COMPARATOR in Phases 9–10 (comparison and verdict), then you become AUDITOR in Phases 11–13 (counter-evidence and audit). Each sub-role transition carries an explicit declaration and a downstream confirmation gate. | Five structural markers: Phase 7 IMPLEMENTER COMPLETE handoff declaration you write; Phase 8 MEASURER entry gate you confirm; Phase 10 COMPARATOR COMPLETE handoff declaration you write; Phase 11 AUDITOR entry gate you confirm; CLOSE COMPLETE sub-role contract discharge for both boundaries you write. | At CLOSE COMPLETE: IMPLEMENTER/MEASURER contract: DISCHARGED and COMPARATOR/AUDITOR contract: DISCHARGED — two explicit discharge confirmations you write, each distinct from Thread 1. |

---

### Structural Marker Inventory

Write this section now — before any container body begins. Write a four-column table cataloging every structural marker required by C-43, C-44, and C-45. This section is your pre-execution compliance claim: you are asserting here, before any container runs, that all four marker types will appear as standalone labeled elements.

**## Structural Marker Inventory**

| Marker type | Required by | Location | Form |
|-------------|-------------|----------|------|
| Lifecycle framing paragraph | C-43 | Write it as a dedicated section before the manifest table — do not merge it with the manifest header and do not put it inside any container body | Standalone labeled section with its own heading |
| Per-container incoming-state annotations | C-43 | Write them on each container header line — do not write them as a sentence inside the first phase body paragraph | Labeled element on the container header line: `incoming lifecycle state: [state]` |
| Phase 11 AUDITOR prerequisite gate | C-44 | Write it at Phase 11 entry, before you write any Phase 11 content — do not embed it as a sentence inside Phase 11 instructional prose | REQUIRED-prefixed standalone gate line |
| CONTAINER COMPLETE thread labels | C-45 | Write them on each CONTAINER COMPLETE line — do not paraphrase them into the completion summary | Explicitly labeled tokens: `Thread 1: [state] | Thread 2: [status]` |

REQUIRED: All four marker types above are present as standalone labeled elements in this document. A marker embedded only in prose — not independently verifiable by scanning — fails C-48 and voids this C-50 inventory you just wrote, retroactively invalidating the pre-execution compliance claim you made in this section.

---

### Competitor Lifecycle Framing

Write the lifecycle framing section. For each container boundary, explain the gate, the contamination risk it prevents, and the isolation purpose it achieves.

**DESIGN boundary — NOT YET IDENTIFIED:** You MUST NOT name the competitor in DESIGN. The contamination risk: if you name the competitor during DESIGN, its known feature set will pull your scope and measurement criteria toward what the competitor already does, rather than toward what the hypothesis requires. The isolation purpose: DESIGN establishes what to measure based only on the hypothesis.

**CALIBRATE boundary — IDENTIFIED AND COMMITTED:** You MUST name the competitor in CALIBRATE and commit B-00 and the outperform threshold before BUILD begins. Two sub-transitions occur: NOT YET IDENTIFIED → IDENTIFIED when you name the competitor in the CALIBRATE body (C-29), and IDENTIFIED → IDENTIFIED AND COMMITTED when you record all three values in CALIBRATE COMPLETE (C-32). Both REQUIRED before BUILD. The contamination risk of skipping: you would build without a committed baseline, enabling retroactive threshold adjustment to fit results.

**BUILD boundary — REFERENCED:** After CALIBRATE COMPLETE, B-00 is FROZEN. You MUST reference it in Phase 8 but MUST NOT alter it. The contamination risk: if you could re-assess B-00 after seeing prototype results, you could adjust the baseline to manufacture a favorable delta.

**CLOSE boundary — DISCHARGED:** You MUST close Thread 1 with the verbatim four-state chain at CLOSE COMPLETE. The contamination risk: implicit discharge without explicit confirmation leaves Thread 1 unauditable.

---

### Document Manifest

| Container | Purpose | Expected output | Competitor status |
|-----------|---------|-----------------|-------------------|
| DESIGN | Lock hypothesis, scope, and measurement criteria | Hypothesis, scope with named exclusion, measurement criteria | NOT YET IDENTIFIED |
| CALIBRATE | Name inertia competitor, lock B-00, commit threshold | Competitor identification, B-00, outperform threshold | IDENTIFIED AND COMMITTED |
| BUILD | IMPLEMENTER builds; MEASURER measures | Construction description (IMPLEMENTER), raw measurements and delta (MEASURER) | REFERENCED |
| CLOSE | COMPARATOR compares + verdicts; AUDITOR audits | Results table, verdict, counter-evidence, limitations, replication | DISCHARGED |

---

### Value Flow Ledger

| Value | Produced in | First consumed in |
|-------|-------------|-------------------|
| Hypothesis text | DESIGN Phase 1 | CALIBRATE Phase 4 |
| Scope + named exclusion | DESIGN Phase 2 | BUILD Phase 7 (you as IMPLEMENTER) |
| Measurement unit + thresholds | DESIGN Phase 3 | CALIBRATE Phase 5 (same unit for B-00); CLOSE Phase 9 (comparison) |
| Predicted result | DESIGN Phase 3 | CLOSE Phase 10 (actual vs. predicted) |
| Competitor name | CALIBRATE Phase 4 | CALIBRATE COMPLETE, BUILD Phase 8 (reference), results table label, CLOSE COMPLETE |
| B-00 | CALIBRATE Phase 5 | CALIBRATE COMPLETE, BUILD Phase 8 (you as MEASURER reference), CLOSE Phase 9 |
| Outperform threshold | CALIBRATE Phase 6 | CALIBRATE COMPLETE, CLOSE Phase 10 |
| Prototype artifact | BUILD Phase 7 (you as IMPLEMENTER) | BUILD Phase 8 (you as MEASURER handoff input), CLOSE COMPLETE arc |
| Raw measurement data | BUILD Phase 8 (you as MEASURER) | CLOSE Phase 9 (you as COMPARATOR input) |
| Actual vs. predicted delta | BUILD Phase 8 (you as MEASURER) | CLOSE Phase 10 (verdict) |
| Verdict word | CLOSE Phase 10 (you as COMPARATOR) | CLOSE COMPLETE arc |
| Counter-evidence disposition | CLOSE Phase 11 (you as AUDITOR) | CLOSE COMPLETE arc |

VALUES MUST NOT be consumed before the producing phase executes.

---

### CONTAINER: DESIGN
**incoming lifecycle state: NOT YET IDENTIFIED — you MUST NOT name a competitor in this container**
**Your entry contract: write (1) hypothesis, (2) scope with exclusion, (3) measurement criteria. All three REQUIRED before DESIGN COMPLETE.**

You are DESIGNER. You MUST write: hypothesis, scope, measurement criteria. You MUST NOT write: competitor names, baseline data, construction steps, results, or verdicts.

**Phase 1 — Hypothesis**
Write a testable claim about {{topic}}. A testable claim names a specific behavior and states what result would confirm it and what result would refute it. Write the confirming and refuting conditions explicitly — "it works better" is not testable; "it processes 1000 records under 2 seconds" is testable.

Write: `GATE: Hypothesis stated — proceeding to Phase 2.`

**Phase 2 — Scope**
Write what this prototype will and will not include. Name at least one explicit exclusion and explain why it still allows you to test the hypothesis.

Write: `GATE: Scope set with named exclusion — proceeding to Phase 3.`

**Phase 3 — Measurement Criteria**
Write your measurement criteria before you build anything. State: the metric and its unit, the value that confirms the hypothesis, the value that refutes it, and your predicted result before seeing any data.

Write: `GATE: Measurement criteria established — proceeding to DESIGN COMPLETE.`

**DESIGN COMPLETE**
Write: hypothesis (verbatim) | scope boundary | success threshold | failure threshold | predicted result.
Write: `→ CALIBRATE receives: hypothesis text, metric + unit, success threshold, failure threshold, predicted result.`
Write: `Thread 1: NOT YET IDENTIFIED | Thread 2: four sub-roles declared (IMPLEMENTER, MEASURER, COMPARATOR, AUDITOR), no handoffs executed`

---

### CONTAINER: CALIBRATE
**incoming lifecycle state: NOT YET IDENTIFIED — you MUST name the inertia competitor in this container; FORBIDDEN to proceed to BUILD without B-00 and outperform threshold**
**Your entry contract: (1) name the inertia competitor with rationale, (2) measure B-00, (3) commit the outperform threshold. All three REQUIRED.**

You are CALIBRATOR. You MUST write: competitor identification, B-00, threshold. You MUST NOT write: construction steps, prototype results, or verdict language.

**Phase 4 — Inertia Competitor**
Name the status-quo approach or tool for {{topic}}. Explain why teams use it today and why they would continue absent a better alternative.

Write: `GATE: Inertia competitor identified — proceeding to Phase 5.`

**Phase 5 — Baseline Measurement (B-00)**
Measure the inertia competitor on the same metric from Phase 3. Record the result as B-00. Write: `B-00: [value] — COMMITTED. You MUST NOT alter this after CALIBRATE COMPLETE.`

Write: `GATE: B-00 committed — proceeding to Phase 6.`

**Phase 6 — Outperform Threshold**
State the threshold your prototype must exceed to justify displacing the inertia competitor. Explain the margin above B-00.

Write: `GATE: Outperform threshold committed — proceeding to CALIBRATE COMPLETE.`

**CALIBRATE COMPLETE**
Write: competitor name | B-00 | outperform threshold — all three REQUIRED.
Write: `→ BUILD receives: competitor name (REFERENCED state begins), B-00 (frozen), outperform threshold.`
Write: `Thread 1: IDENTIFIED AND COMMITTED (competitor: [name], B-00: [value], threshold: [value]) | Thread 2: no handoffs yet executed`

---

### CONTAINER: BUILD
**incoming lifecycle state: IDENTIFIED AND COMMITTED — B-00 is FROZEN; you MUST reference it, MUST NOT alter it**
**Your entry contract: you are IMPLEMENTER in Phase 7 (construction only); you become MEASURER in Phase 8 (measurement only) after the IMPLEMENTER COMPLETE handoff. Handoff declaration REQUIRED; MEASURER gate REQUIRED.**

**You are IMPLEMENTER for Phase 7.**
You MUST write: prototype construction, artifact description. You MUST NOT write: measurements, raw data, comparison to B-00, or verdict-adjacent language.

**Phase 7 — Prototype Construction**
Build the minimal prototype that tests the hypothesis. Describe what you built: the key components, the approach, and any decisions that affect what can be measured. Be detailed enough that someone else could reproduce it.

Write: `GATE: Prototype artifact described — proceeding to IMPLEMENTER COMPLETE.`

**IMPLEMENTER COMPLETE — REQUIRED handoff to MEASURER**
Write: prototype artifact name/description.
Write: `IMPLEMENTER responsibilities discharged — REQUIRED handoff to MEASURER for Phase 8.`
Write: `Thread 2: IMPLEMENTER handoff declared — MEASURER REQUIRED to confirm before Phase 8`

**You are now MEASURER for Phase 8.**
Write: `REQUIRED: Confirming Phase 7 IMPLEMENTER handoff marker present — proceeding to Phase 8.`
You MUST write: measurement execution, raw data, actual vs. predicted comparison. You MUST NOT write: new construction decisions, alterations to B-00, or verdict language.

**Phase 8 — Measurement Execution**
Run the measurements from Phase 3 against your prototype. Record the predicted value (from Phase 3), the actual measured value, the delta, and whether the outperform threshold was cleared. Reference B-00 by value.

Write: `GATE: Raw data recorded, actual vs. predicted stated, threshold clearance noted — proceeding to BUILD COMPLETE.`

**BUILD COMPLETE**
Write: prototype description | actual value | predicted value | delta | threshold cleared (YES/NO).
Write: `→ CLOSE receives: raw data, actual vs. predicted delta, competitor name (for REFERENCED → DISCHARGED transition).`
Write: `Thread 1: REFERENCED (B-00 referenced, competitor: [name]) | Thread 2: IMPLEMENTER/MEASURER handoff executed and discharged`

---

### CONTAINER: CLOSE
**incoming lifecycle state: REFERENCED — competitor MUST transition to DISCHARGED at CLOSE COMPLETE**
**Your entry contract: you are COMPARATOR in Phases 9–10 (comparison and verdict); you become AUDITOR in Phases 11–13 after the COMPARATOR COMPLETE handoff. Both handoff declaration and AUDITOR gate REQUIRED.**

**You are COMPARATOR for Phases 9–10.**
You MUST write: results comparison, verdict. You MUST NOT write: counter-evidence, limitations, or replication content.

**Phase 9 — Results Table**
Write a comparison table. The baseline column MUST be labeled with the inertia competitor's name — not "Baseline."

| Metric | Inertia competitor ([name], B-00) | Prototype result | Delta | Outperform threshold | Threshold cleared? |
|--------|-----------------------------------|-----------------|-------|---------------------|-------------------|
| (fill) | (fill) | (fill) | (fill) | (fill) | YES / NO |

Write: `GATE: Results table with competitor-named baseline written — proceeding to Phase 10.`

**Phase 10 — Verdict**
State confirmed, refuted, or inconclusive. Cite the delta and threshold. State actual vs. predicted explicitly.

Write: `GATE: Verdict stated with evidence — proceeding to COMPARATOR COMPLETE.`

**COMPARATOR COMPLETE — REQUIRED handoff to AUDITOR**
Write: verdict word | delta | threshold cleared.
Write: `COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR for Phases 11–13.`
Write: `Thread 2: COMPARATOR handoff declared — AUDITOR REQUIRED to confirm before Phase 11`

**You are now AUDITOR for Phases 11–13.**
Write: `REQUIRED: Confirming Phase 10 COMPARATOR handoff marker present — proceeding to Phase 11.`
You MUST write: counter-evidence disposition, limitations, replication. You MUST NOT write: new measurements, new comparison data, or verdicts.

**Phase 11 — Counter-Evidence**
Close the counter-evidence question with one of two explicit dispositions: (a) name a counter-interpretation and rebut it with evidence, or (b) state explicitly that no plausible counter-interpretation exists, with a reason.

Write: `GATE: Counter-evidence question closed with binary disposition — proceeding to Phase 12.`

**Phase 12 — Limitations**
Name at least one limitation. State whether it affects the verdict.

**Phase 13 — Replication Path**
Name every tool, input, command, or step needed to reproduce the prototype and measurements. No implicit steps.

Write: `GATE: Replication path complete — proceeding to CLOSE COMPLETE.`

**CLOSE COMPLETE**
Write all of the following — every element REQUIRED:
- `Hypothesis verdict: [CONFIRMED / REFUTED / INCONCLUSIVE]`
- `Arc: competitor [name] | B-00 [value] | threshold [value] | prototype result [value] | delta [value] | verdict [word] | counter-evidence [disposition]`
- `Value ledger: FULLY DISCHARGED / PARTIAL — [N] values unresolved`
- `Thread 1 lifecycle chain (verbatim): NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED`
- `Thread 2: IMPLEMENTER/MEASURER contract: DISCHARGED | COMPARATOR/AUDITOR contract: DISCHARGED`
- `Competitor lifecycle: DISCHARGED`

---

---

## V-05 — Role Sequence + Output Format + Inertia Framing (Ceiling)

**Axis:** Three-axis combination — (1) BUILD split into IMPLEMENTER + MEASURER sub-roles; (2) all phase outputs table-anchored; (3) inertia competitor named in the document title line and tracked on seven structural surfaces: five Thread 1 surfaces (C-29, C-32, C-34, C-36, CONTAINER COMPLETE lifecycle annotations) plus two BUILD-phase MEASURER references to B-00 (Phase 8 measurement results table; BUILD COMPLETE arc).

**Hypothesis:** Ceiling case combining all R20 structural additions. C-51 generates the two Thread 2 markers that make C-49 5:5 parity reachable. C-52 binds the inventory's pre-execution claim to its post-violation consequence at maximum explicitness — naming both the inventory and every pre-execution compliance assertion derived from it. Table format makes the IMPLEMENTER COMPLETE handoff and MEASURER gate visually indistinguishable from other phase outputs, preventing handoff-as-annotation drift. Prominent inertia framing ensures the competitor lifecycle is never ambient — it is foregrounded at the document's first line and tracked exhaustively to CLOSE COMPLETE.

---

You are running a prototype signal for topic: **{{topic}}**
**Inertia competitor under investigation:** [TO BE IDENTIFIED IN CALIBRATE — identification FORBIDDEN before CALIBRATE container begins]

---

### MANIFEST PREAMBLE

**Step 1:** Write the two-row thread declaration table. Use the exact schema. Both rows MUST carry equivalent depth in every column — a row that cannot fill a column with equivalent depth indicates a structurally subordinate thread.

| Thread | Scope | Key structural markers | Terminal discharge obligation |
|--------|-------|----------------------|------------------------------|
| **Thread 1 — Competitor lifecycle** | Four-state progression: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED. Gated at CALIBRATE (identification required before BUILD); B-00 frozen at CALIBRATE COMPLETE; B-00 referenced in BUILD Phase 8 MEASURER output; lifecycle discharged at CLOSE COMPLETE. Competitor status column in manifest tracks state at each container boundary. | Seven surfaces: (1) document preamble title line naming competitor investigation (existence established); (2) manifest Competitor Status column — four-state tracking across all containers; (3) CALIBRATE body — competitor named with rationale (C-29); (4) CALIBRATE COMPLETE — triple: competitor name + B-00 + outperform threshold (C-32); (5) BUILD Phase 8 measurement results table — B-00 reference row (MEASURER output); (6) results table — baseline column labeled with competitor name, not "Baseline" (C-34); (7) CLOSE COMPLETE arc record — competitor name embedded in terminal element (C-36). | CLOSE COMPLETE carries verbatim four-state chain: NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED. All seven competitor surfaces MUST be present for Thread 1 to close fully. |
| **Thread 2 — Role sequencing (BUILD + CLOSE)** | Two intra-container role boundaries with symmetric structure: (1) BUILD — IMPLEMENTER (Phase 7, construction table) hands off to MEASURER (Phase 8, measurement results table); (2) CLOSE — COMPARATOR (Phases 9–10, comparison table + verdict table) hands off to AUDITOR (Phases 11–13, counter-evidence table + limitations table + replication table). Four named sub-roles; four explicit table-anchored prohibitions; two handoff declaration tables; two acknowledgment gate tables. | Five structural markers: (1) Phase 7 IMPLEMENTER COMPLETE handoff table with declaration row; (2) Phase 8 MEASURER entry gate table with confirmation row; (3) Phase 10 COMPARATOR COMPLETE handoff table with declaration row; (4) Phase 11 AUDITOR entry gate table with confirmation row; (5) CLOSE COMPLETE sub-role contract discharge table — both contracts as named rows with DISCHARGED status. | CLOSE COMPLETE carries a sub-role contract table with two rows: IMPLEMENTER/MEASURER contract: DISCHARGED and COMPARATOR/AUDITOR contract: DISCHARGED. Both REQUIRED; both distinct from Thread 1 lifecycle chain, C-42 value ledger discharge, and C-36 arc record. |

---

### Structural Marker Inventory

**Step 2:** Write this section now — before any container body. Write a four-column catalog of every structural marker required by C-43, C-44, and C-45. This section makes C-48 compliance a verifiable document property before any container executes.

**## Structural Marker Inventory**

| Marker type | Required by | Location | Form |
|-------------|-------------|----------|------|
| Lifecycle framing paragraph | C-43 | Dedicated section before the manifest table; not merged with manifest header; not inside any container body | Standalone labeled section (own heading, own section break) |
| Per-container incoming-state annotations | C-43 | On each container header line; not as a sentence in the first phase body paragraph | Labeled element on the container header: `incoming lifecycle state: [state]` |
| Phase 11 AUDITOR prerequisite gate | C-44 | Phase 11 entry point, before any Phase 11 content is written; not embedded in Phase 11 instructional prose | REQUIRED-prefixed standalone gate line appearing before the Phase 11 body |
| CONTAINER COMPLETE thread labels | C-45 | On each CONTAINER COMPLETE line; not paraphrased into the completion prose | Explicitly labeled elements: `Thread 1: [state] | Thread 2: [status]` |

**REQUIRED: All four marker types above are present as standalone labeled elements in this document. A marker embedded only in prose — readable by parsing a paragraph but not verifiable by scanning the document's structural elements — fails C-48, voids this C-50 inventory, and retroactively invalidates every pre-execution compliance assertion derived from this section, including the four-marker count declared in the table above.**

---

### Competitor Lifecycle Framing

| Container boundary | Incoming state | Constraint | Contamination risk | Isolation purpose |
|-------------------|---------------|------------|-------------------|-------------------|
| DESIGN entry | NOT YET IDENTIFIED | Competitor identification FORBIDDEN | Known competitor features contaminating scope and measurement criteria design | Measurement criteria derived from hypothesis alone, not from competitive positioning |
| CALIBRATE entry | NOT YET IDENTIFIED | Identification REQUIRED; FORBIDDEN to enter BUILD without B-00 + threshold | Prototype executing without committed baseline; retroactive threshold adjustment after results known | Baseline and threshold pre-committed; CALIBRATE COMPLETE locks all three values before BUILD executes |
| CALIBRATE sub-transition 1 | NOT YET IDENTIFIED → IDENTIFIED | Competitor named in CALIBRATE body (C-29) | N/A | Competitor identified before baseline measurement begins |
| CALIBRATE sub-transition 2 | IDENTIFIED → IDENTIFIED AND COMMITTED | B-00 measured and threshold committed; all three locked in CALIBRATE COMPLETE (C-32) | N/A | Triple locked before BUILD; no post-hoc adjustment possible |
| BUILD entry | IDENTIFIED AND COMMITTED | B-00 FROZEN — MEASURER MUST reference, MUST NOT alter | MEASURER re-assessing B-00 after observing prototype results | Measurement against pre-committed baseline; delta is a genuine result |
| CLOSE entry | REFERENCED | Thread 1 REQUIRED to close with verbatim four-state chain at CLOSE COMPLETE | Implicit discharge without explicit confirmation; Thread 1 unauditable | Explicit chain at CLOSE COMPLETE makes Thread 1 verifiable by scan |

---

### Document Manifest

| Container | Purpose | Expected output format | Competitor status |
|-----------|---------|----------------------|-------------------|
| DESIGN | Lock hypothesis, scope, measurement criteria | Hypothesis table, scope table, measurement criteria table | NOT YET IDENTIFIED |
| CALIBRATE | Name inertia competitor, lock B-00, commit outperform threshold | Competitor identification table, baseline measurement table, threshold commitment table | IDENTIFIED AND COMMITTED |
| BUILD | IMPLEMENTER constructs; MEASURER executes measurements | Construction table (IMPLEMENTER Phase 7), measurement results table (MEASURER Phase 8) | REFERENCED |
| CLOSE | COMPARATOR compares + verdicts; AUDITOR audits | Results comparison table, verdict table, counter-evidence table, limitations table, replication table | DISCHARGED |

---

### Value Flow Ledger

| Value | Produced in | First consumed in |
|-------|-------------|-------------------|
| Hypothesis text | DESIGN Phase 1 (hypothesis table) | CALIBRATE Phase 4 |
| Scope boundary + exclusion | DESIGN Phase 2 (scope table) | BUILD Phase 7 (IMPLEMENTER) |
| Measurement unit | DESIGN Phase 3 (criteria table) | CALIBRATE Phase 5 (same unit for B-00) |
| Success threshold | DESIGN Phase 3 | CLOSE Phase 9 (comparison) |
| Failure threshold | DESIGN Phase 3 | CLOSE Phase 9 (comparison) |
| Predicted result | DESIGN Phase 3 | CLOSE Phase 10 (actual vs. predicted) |
| Competitor name | CALIBRATE Phase 4 | CALIBRATE COMPLETE, BUILD Phase 8 (MEASURER reference row), results table baseline label, CLOSE COMPLETE arc |
| B-00 | CALIBRATE Phase 5 | CALIBRATE COMPLETE, BUILD Phase 8 (MEASURER measurement results table), CLOSE Phase 9 |
| Outperform threshold | CALIBRATE Phase 6 | CALIBRATE COMPLETE, CLOSE Phase 10 |
| Prototype artifact | BUILD Phase 7 (IMPLEMENTER) | BUILD Phase 8 (MEASURER handoff), CLOSE COMPLETE arc |
| Raw measurement data | BUILD Phase 8 (MEASURER) | CLOSE Phase 9 (COMPARATOR) |
| Actual vs. predicted delta | BUILD Phase 8 (MEASURER) | CLOSE Phase 10 (verdict) |
| Verdict word | CLOSE Phase 10 (COMPARATOR) | CLOSE COMPLETE arc |
| Counter-evidence disposition | CLOSE Phase 11 (AUDITOR) | CLOSE COMPLETE arc |

**VALUES MUST NOT be consumed before the producing phase executes.**

---

### CONTAINER: DESIGN
**incoming lifecycle state: NOT YET IDENTIFIED — competitor identification FORBIDDEN**
**Entry contract:** Produce three tables: (1) hypothesis table, (2) scope table, (3) measurement criteria table. All three REQUIRED before DESIGN COMPLETE. No prose bullets.

**Role: DESIGNER**
DESIGNER MUST write: hypothesis table, scope table, measurement criteria table.
DESIGNER FORBIDDEN to write: competitor names, baseline data, construction steps, results, or verdicts.

**Phase 1 — Hypothesis Table**

| Field | Value |
|-------|-------|
| Testable claim | (state the behavior or property to be tested for {{topic}}) |
| Confirming result | (what outcome confirms the hypothesis) |
| Refuting result | (what outcome refutes the hypothesis) |

`GATE: Hypothesis table complete — proceeding to Phase 2.`

**Phase 2 — Scope Table**

| Field | Value |
|-------|-------|
| What the prototype includes | (specific scope) |
| What is explicitly excluded | (at least one named exclusion) |
| Why exclusion preserves testability | (reason) |

`GATE: Scope table complete — proceeding to Phase 3.`

**Phase 3 — Measurement Criteria Table**

| Metric | Unit | Success threshold | Failure threshold | Predicted result |
|--------|------|-------------------|-------------------|-----------------|
| (fill) | (fill) | (fill) | (fill) | (fill) |

`GATE: Measurement criteria table complete — proceeding to DESIGN COMPLETE.`

**DESIGN COMPLETE**
Record: hypothesis (verbatim) | scope boundary | success threshold | failure threshold | predicted result.
→ CALIBRATE receives: hypothesis text, metric + unit, thresholds, predicted result.
Thread 1: NOT YET IDENTIFIED | Thread 2: four sub-roles declared (IMPLEMENTER, MEASURER, COMPARATOR, AUDITOR), no handoffs executed

---

### CONTAINER: CALIBRATE
**incoming lifecycle state: NOT YET IDENTIFIED — identification REQUIRED in this container; FORBIDDEN to proceed to BUILD without locking all three values**
**Entry contract:** Three tables: (1) competitor identification table, (2) baseline measurement table, (3) threshold commitment table. All three REQUIRED before CALIBRATE COMPLETE.

**Role: CALIBRATOR**
CALIBRATOR MUST write: competitor identification table, B-00 table, threshold table.
CALIBRATOR FORBIDDEN to write: construction steps, prototype results, or verdict language.

**Phase 4 — Competitor Identification Table**

| Field | Value |
|-------|-------|
| Competitor name | (the status-quo tool or approach for {{topic}}) |
| Problem it currently solves | (specific to {{topic}}) |
| Adoption inertia rationale | (why teams continue using it absent a better alternative) |
| Lifecycle state after this phase | IDENTIFIED |

`GATE: Competitor identification table complete — proceeding to Phase 5.`

**Phase 5 — Baseline Measurement Table (B-00)**

| Field | Value |
|-------|-------|
| Metric measured | (same as Phase 3) |
| B-00 value | (measured result for the inertia competitor) |
| Measurement method | (how B-00 was obtained) |
| Frozen status | COMMITTED — MUST NOT be altered after CALIBRATE COMPLETE |
| Lifecycle state after this phase | IDENTIFIED AND COMMITTED (pending threshold) |

`GATE: B-00 table complete with COMMITTED status — proceeding to Phase 6.`

**Phase 6 — Threshold Commitment Table**

| Field | Value |
|-------|-------|
| Outperform threshold | (value prototype must exceed) |
| Margin above B-00 | (the margin expressed as a delta) |
| Justification for margin | (why this margin reflects genuine improvement, not noise) |
| Lifecycle state after this phase | IDENTIFIED AND COMMITTED (both sub-transitions complete) |

`GATE: Threshold table complete — proceeding to CALIBRATE COMPLETE.`

**CALIBRATE COMPLETE**
Record: competitor name | B-00 | outperform threshold — all three REQUIRED.
→ BUILD receives: competitor name (REFERENCED state begins), B-00 (frozen), outperform threshold.
Thread 1: IDENTIFIED AND COMMITTED (competitor: [name], B-00: [value], threshold: [value]) | Thread 2: no handoffs yet executed

---

### CONTAINER: BUILD
**incoming lifecycle state: IDENTIFIED AND COMMITTED — B-00 is FROZEN; MEASURER MUST reference it, MUST NOT alter it**
**Entry contract:** IMPLEMENTER produces the construction table (Phase 7) and executes IMPLEMENTER COMPLETE handoff; MEASURER confirms the gate table and produces the measurement results table (Phase 8). Both tables and the handoff/gate sequence REQUIRED before BUILD COMPLETE.

**Sub-role IMPLEMENTER** (Phase 7)
IMPLEMENTER MUST write: construction table.
IMPLEMENTER FORBIDDEN to: record measurements, reference B-00 in comparison language, or produce verdict-adjacent content.

**Phase 7 — Prototype Construction Table**

| Field | Value |
|-------|-------|
| What was built | (prototype name and description) |
| Key components | (what the prototype consists of) |
| Implementation decisions affecting measurement | (choices that constrain what can and cannot be measured) |
| Artifact deliverable to MEASURER | (the artifact MEASURER will run measurements against) |

`GATE: Construction table complete — proceeding to IMPLEMENTER COMPLETE.`

**IMPLEMENTER COMPLETE — REQUIRED handoff to MEASURER**

| Handoff element | Value |
|-----------------|-------|
| Artifact delivered | (prototype name/description from Phase 7 construction table) |
| Handoff declaration | IMPLEMENTER responsibilities discharged — REQUIRED handoff to MEASURER for Phase 8 |
| Thread 2 | IMPLEMENTER handoff declared — MEASURER REQUIRED to confirm gate before Phase 8 |

**Sub-role MEASURER** (Phase 8)

| Gate | Status |
|------|--------|
| Phase 7 IMPLEMENTER handoff marker present? | REQUIRED — confirm YES before executing Phase 8 |

MEASURER MUST write: measurement results table.
MEASURER FORBIDDEN to: alter prototype behavior, modify B-00, adjust outperform threshold, or produce verdict language.

**Phase 8 — Measurement Results Table**

| Field | Value |
|-------|-------|
| Metric measured | (same as DESIGN Phase 3) |
| Predicted value | (from Phase 3 measurement criteria table) |
| Actual measured value | (raw result from prototype) |
| Delta (actual minus predicted) | (value) |
| B-00 reference | (competitor baseline — not re-measured; value from CALIBRATE Phase 5) |
| Outperform threshold | (from CALIBRATE Phase 6) |
| Outperform threshold cleared? | YES / NO |

`GATE: Measurement results table complete — proceeding to BUILD COMPLETE.`

**BUILD COMPLETE**
Record: prototype artifact | actual value | predicted value | delta | threshold cleared (YES/NO).
→ CLOSE receives: measurement results table, actual vs. predicted delta, competitor name (for REFERENCED → DISCHARGED transition).
Thread 1: REFERENCED (B-00 referenced in measurement, competitor: [name]) | Thread 2: IMPLEMENTER/MEASURER handoff executed and discharged

---

### CONTAINER: CLOSE
**incoming lifecycle state: REFERENCED — competitor MUST reach DISCHARGED at CLOSE COMPLETE**
**Entry contract:** COMPARATOR produces results comparison table + verdict table (Phases 9–10), then COMPARATOR COMPLETE handoff to AUDITOR for counter-evidence table + limitations table + replication table (Phases 11–13). All five tables and both handoff/gate sequences REQUIRED.

**Sub-role COMPARATOR** (Phases 9–10)
COMPARATOR MUST write: results comparison table, verdict table.
COMPARATOR FORBIDDEN to write: counter-evidence, limitations, or replication content.

**Phase 9 — Results Comparison Table**
Baseline column MUST be labeled with the inertia competitor name — a generic "Baseline" label fails C-34.

| Metric | Inertia competitor ([name], B-00) | Prototype result | Delta | Outperform threshold | Threshold cleared? |
|--------|-----------------------------------|-----------------|-------|---------------------|-------------------|
| (fill) | (fill) | (fill) | (fill) | (fill) | YES / NO |

`GATE: Results table with competitor-named baseline column written — proceeding to Phase 10.`

**Phase 10 — Verdict Table**

| Field | Value |
|-------|-------|
| Verdict | CONFIRMED / REFUTED / INCONCLUSIVE |
| Evidence (cite delta and threshold) | (specific values from Phase 9) |
| Actual result | (from measurement results table) |
| Predicted result | (from DESIGN Phase 3) |
| Actual vs. predicted | (confirmation or mismatch) |

`GATE: Verdict table complete — proceeding to COMPARATOR COMPLETE.`

**COMPARATOR COMPLETE — REQUIRED handoff to AUDITOR**

| Handoff element | Value |
|-----------------|-------|
| Verdict | (word from Phase 10) |
| Delta | (value from Phase 9) |
| Threshold cleared | YES / NO |
| Handoff declaration | COMPARATOR responsibilities discharged — REQUIRED handoff to AUDITOR for Phases 11–13 |
| Thread 2 | COMPARATOR handoff declared — AUDITOR REQUIRED to confirm gate before Phase 11 |

**Sub-role AUDITOR** (Phases 11–13)

| Gate | Status |
|------|--------|
| Phase 10 COMPARATOR handoff marker present? | REQUIRED — confirm YES before executing Phase 11 |

AUDITOR MUST write: counter-evidence table, limitations table, replication table.
AUDITOR FORBIDDEN to write: new measurement criteria, new comparison data, or verdict statements.

**Phase 11 — Counter-Evidence Table**
Binary disposition REQUIRED:

| Field | Value |
|-------|-------|
| Counter-interpretation found? | YES / NO |
| Counter-interpretation (if YES) | (name it; leave blank if NO) |
| Rebuttal grounded in results (if YES) | (rebuttal; leave blank if NO) |
| Reason no counter-interpretation exists (if NO) | (explicit reason; leave blank if YES) |

`GATE: Counter-evidence binary disposition table complete — proceeding to Phase 12.`

**Phase 12 — Limitations Table**

| Limitation | Type | Effect on verdict validity |
|------------|------|---------------------------|
| (at least one row) | scope / fidelity / sample / instrument | (does it affect the verdict?) |

**Phase 13 — Replication Table**

| Step | Tool / Input / Command | Notes |
|------|----------------------|-------|
| (fill all reproduction steps; no implicit steps) | | |

`GATE: Replication table complete — proceeding to CLOSE COMPLETE.`

**CLOSE COMPLETE**
Write all elements — every element REQUIRED:

| Element | Value |
|---------|-------|
| Hypothesis verdict | CONFIRMED / REFUTED / INCONCLUSIVE |
| Arc record | competitor [name] \| B-00 [value] \| threshold [value] \| prototype result [value] \| delta [value] \| verdict [word] \| counter-evidence [disposition] |
| Value ledger | FULLY DISCHARGED / PARTIAL — [N] values unresolved |
| Thread 1 lifecycle chain (verbatim) | NOT YET IDENTIFIED → IDENTIFIED AND COMMITTED → REFERENCED → DISCHARGED |
| Thread 2 — IMPLEMENTER/MEASURER contract | DISCHARGED |
| Thread 2 — COMPARATOR/AUDITOR contract | DISCHARGED |
| Competitor lifecycle | DISCHARGED |
