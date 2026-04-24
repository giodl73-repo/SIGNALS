Now I have the full picture. R13 V-05 scored 100.00 under v12. Under v13, the baseline fails C-42 (application sentence) and C-43 (Phase 3E Pass 2 stratification). Both are worth 10/35 = 0.286 pts; getting both unlocks a perfect 100.00 under v13.

Variation axes chosen:
- **Single-axis**: Output Format (C-42), Lifecycle Emphasis (C-43), Phrasing Register (C-42)
- **Combined**: Output Format + Lifecycle Emphasis (C-42 + C-43), Lifecycle Emphasis + Phrasing Register (C-42 + C-43)

---

# trace-state Rubric v13 — Round 14 Variations

---

## V-01 | Axis: Output Format — Application Sentence as Mandatory Named Column

**Hypothesis**: Expressing the Application Sentence as a required column in a per-phase SCORING PROTOCOL table makes C-42 compliance structural rather than behavioral — a blank cell is a detectable failure, not a prose omission. The model cannot satisfy the table without producing the active binding.

**Targets**: C-42 (primary). C-43 untargeted (single-axis test).

---

```
You are executing the **trace-state** skill.
Topic: {topic} | Domain: {domain} — Sales / Customer Service / Finance

---

## PART 0 — Pre-Game Setup [Complete before any analysis begins]

### 0A — Gap Record Template (V-01 Contract)
All Gap Records in this trace use the following 5-field template.
A Gap Record with any field blank or left as a placeholder is a structural failure.

| Field | Instruction |
|-------|-------------|
| Examined | List every OP-ID, S-ID, or INV-ID scanned for this anomaly type |
| Evidence Standard Applied | Restate the Phase N registry row verbatim |
| Application Sentence | State exactly what strength ≥ 2 means for THIS anomaly type's evidence shape |
| What Was Not Found | Describe the specific trace steps / state conditions that would constitute a finding |
| Verdict | ACQUITTED (explain) or FINDING (cross-reference finding ID) |

**V-01 Application Sentence Rule**: The Application Sentence field in the Gap Record template
is not satisfied by the Evidence Standard Applied restate. The restate is passive ("Strength ≥ 2
required"). The Application Sentence is active: it names the specific evidence shape that would
meet the threshold for this anomaly class in this trace (e.g., "For IST findings, strength ≥ 2
means: a trace step shows a transition from S-A to S-B with no OP-ID in the Operation Registry
that permits S-A → S-B."). A Gap Record whose Application Sentence field reproduces the Evidence
Standard Applied field is a structural failure.

### 0B — Standards Registry
Produce the Standards Registry table. Seal it before PART 1 opens.
Each phase restates its exact registry row verbatim at phase entry.

| Phase | Anomaly Type | Min-Strength | Application Sentence |
|-------|-------------|--------------|---------------------|
| 3A | Invalid State Transition (IST) | ≥ 2 | *For IST: strength ≥ 2 means a trace step names a From-State S-ID and a To-State S-ID with no matching OP-ID in the Operation Registry permitting that transition for that actor.* |
| 3B | Missing Precondition Check (MPC) | ≥ 2 | *For MPC: strength ≥ 2 means a trace step executes an operation without a prior step asserting the required precondition, traceable to a specific INV-ID or state requirement in the declaration.* |
| 3C | Invariant Violation (IVC) | ≥ 2 | *For IVC: strength ≥ 2 means a post-step state value demonstrably violates a declared INV-ID threshold, with both the threshold and the violating value visible in the trace.* |
| 3D | Race Condition (RCS) | ≥ 2 | *For RCS: strength ≥ 2 means two concurrent trace steps share the same S-ID target with no intervening lock assertion or serialization gate between them.* |
| 3E | Undeclared Reference (URF) | ≥ 2 | *For URF: strength ≥ 2 means a reference appears in both the declaration tables and at least one trace step, with no corresponding declaration row for that entity class.* |

**REGISTRY SEALED — standards and Application Sentences cannot be revised after this point.**

---

## PART 1 — State Machine Construction

**1A — Entity-Class Registry**
| Entity-Class | Label (S / O / I) | Description |
|-------------|-------------------|-------------|

**1B — State Registry**
| S-ID | State Name | Entry Condition | Description | Entity-Class |
|------|-----------|-----------------|-------------|--------------|

**1C — Operation Registry**
| OP-ID | Operation | From-State (S-ID) | To-State (S-ID) | Actor | Precondition | Postcondition |
|-------|-----------|-------------------|-----------------|-------|--------------|---------------|
*Numeric/temporal invariant gate*: Declare at least one INV-ID with explicit falsifiable threshold.

**1D — Invariant Registry**
| INV-ID | Invariant | Type | Threshold |
|--------|-----------|------|-----------|

---

## PART 2 — Trace Construction

Produce a numbered step sequence (8–15 steps). Use this template per step:

**Step N** | Actor: ___ | OP-ID: ___ | From: ___ (S-ID) | To: ___ (S-ID)
- Precondition check: ___
- Postcondition verified: ___
- Invariants checked: ___
- [If REJECTED] After-state: *Entity remains in [From-State S-ID]. Rejection does not change state.*
  *(Any deviation from this is a detectable IST anomaly.)*

---

## PART 3 — Pre-Sweep Hypothesis

Before opening Phase 3A, record falsifiable predictions:

| Phase | Predicted Finding | Count | Predicted Anomaly IDs |
|-------|------------------|-------|----------------------|
| 3A IST | Yes / No | | |
| 3B MPC | Yes / No | | |
| 3C IVC | Yes / No | | |
| 3D RCS | Yes / No | | |
| 3E URF | Yes / No | | |

---

## PART 4 — Phase Execution

**Sequential Lock Rule**: 3A → 3B → 3C → 3D → 3E → PART 5.
Phase N remains LOCKED until Phase N-1 emits PHASE N-1: COMPLETE.

---

### Phase 3A — Invalid State Transitions (IST) [OPEN]

**SCORING PROTOCOL** *(complete this table before detection begins)*:

| Element | Content |
|---------|---------|
| Verbatim Restate | *Copy the Phase 3A Standards Registry row exactly* |
| Application Sentence | *Active binding: "For IST findings in this trace, strength ≥ 2 means: [specific evidence shape — which trace elements, which declaration gaps, what makes it traceable to a concrete step]"* |

*The Application Sentence must describe evidence shape, not restate the rule.
A sentence that reproduces the Verbatim Restate is a structural failure of this table.*

Role B pre-detection commitment: *"I require [specific evidence standard] before recording a finding."*

**Pass 1 — Declaration-Only**
| OP-ID / S-ID | Declaration-Only Finding | Strength (1/2/3) | Evidence |
|-------------|--------------------------|-----------------|---------|
*(Score-aloud rule: assign strength at moment of discovery, not end-of-pass. Incomplete sentence = not recordable.)*

**Pass 2 — Trace-Diff**
| Step | Trace-Diff Finding | Strength (1/2/3) | Evidence |
|------|--------------------|-----------------|---------|

**Findings List**: [consolidate; note any strength < 2]

**Evidence Strength Gate** ☐ At least one finding at strength ≥ 2, OR Gap Record explains why none met the standard.

**Gap Record** *(V-01 5-field template — mandatory regardless of finding count)*:
- Examined: ___
- Evidence Standard Applied: ___
- Application Sentence: ___  ← *must differ from Evidence Standard Applied*
- What Was Not Found: ___
- Verdict: ___

*The Gap Record is the unlock signal for the Phase 3A exit gate.*

**Phase 3A Exit Certification**
☐ Findings List produced
☐ Evidence Strength Gate satisfied
☐ Gap Record produced (all 5 fields populated)
☐ Gap Record Application Sentence distinct from Evidence Standard Applied restate

**PHASE 3A: COMPLETE → Phase 3B now OPEN**

---
*(Phases 3B, 3C, 3D follow identical anatomy. Each phase's SCORING PROTOCOL table
Application Sentence must match the Phase 3E registry entry for its anomaly type.)*

---

### Phase 3E — Undeclared References (URF) [LOCKED until PHASE 3D: COMPLETE]

**SCORING PROTOCOL**:
| Element | Content |
|---------|---------|
| Verbatim Restate | *Copy the Phase 3E Standards Registry row exactly* |
| Application Sentence | *Active binding for URF findings in this trace: what makes a cross-reference finding traceable at strength ≥ 2 — which declaration tables, which trace steps, which entity classes are in scope* |

**Pass 1 — Declaration Scan (stratified)**

*Pass 1-S (Subject class S-IDs)*
| Reference | Declaration-Only Finding | Strength | Evidence |

*Pass 1-O (Object class OP-IDs)*
| Reference | Declaration-Only Finding | Strength | Evidence |

*Pass 1-I (Identifier class INV-IDs)*
| Reference | Declaration-Only Finding | Strength | Evidence |

A finding in one entity-class row does not satisfy another row's sweep requirement.

**Pass 2 — Trace-Diff Scan**
*(single unified pass — see V-02 for stratified Pass 2)*
| Step | Trace-Diff Finding | Strength | Evidence |

**Findings List** | **Evidence Strength Gate** ☐ | **Gap Record** (5-field) | **Phase 3E Exit Certification** ☐ (all fields + Pass 1 three rows populated)

**PHASE 3E: COMPLETE → PART 5 now OPEN**

---

## PART 5 — Reconciliation

| Phase | Predicted | Actual | C / FP / FN | Surprise? |
|-------|-----------|--------|-------------|-----------|

**Calibration Score**: C / (C + FP + FN) = ___%.
If < 60%: (1) identify systematic over/under-prediction by anomaly type; (2) trace to
declaration registry row contributing the error; (3) diagnose: hypothesis methodology
gap or declaration completeness gap.

**Final Signal**: One-paragraph domain-grounded conclusion on system readiness.
```

---

## V-02 | Axis: Lifecycle Emphasis — Phase 3E Pass 2 Stratified Sub-Scans

**Hypothesis**: Writing Phase 3E's Pass 2 with three explicit independent sub-scans (P2-S, P2-O, P2-I) — each with its own named table section mirroring Pass 1 — closes the structural loophole where a unified Trace-Diff pass absorbs absent OP-ID or INV-ID checking into a passing S-ID result. The Application Sentence is present (via verbatim restate + registry column) but not independently enforced as a named table artifact.

**Targets**: C-43 (primary). C-42 elicited via registry column but not structurally separated.

---

```
You are executing the **trace-state** skill.
Topic: {topic} | Domain: {domain} — Sales / Customer Service / Finance

---

## PART 0 — Pre-Game Setup

### 0A — Gap Record Template
All Gap Records use the following 5-field template. A Gap Record missing any field is a
structural failure.
Fields: Examined | Evidence Standard Applied | What Was Not Found |
        What Would Constitute a Finding | Verdict

### 0B — Standards Registry
| Phase | Anomaly Type | Min-Strength | Application Sentence |
|-------|-------------|--------------|---------------------|
| 3A | Invalid State Transition (IST) | ≥ 2 | *[Bind: for IST in this trace, strength ≥ 2 means ___]* |
| 3B | Missing Precondition Check (MPC) | ≥ 2 | *[Bind: for MPC in this trace, strength ≥ 2 means ___]* |
| 3C | Invariant Violation (IVC) | ≥ 2 | *[Bind: for IVC in this trace, strength ≥ 2 means ___]* |
| 3D | Race Condition (RCS) | ≥ 2 | *[Bind: for RCS in this trace, strength ≥ 2 means ___]* |
| 3E | Undeclared Reference (URF) | ≥ 2 | *[Bind: for URF in this trace, strength ≥ 2 means ___]* |

**REGISTRY SEALED.**

---

## PART 1 — State Machine Construction

**1A — State Registry** | S-ID | State | Entry Condition | Entity-Class |
**1B — Operation Registry** | OP-ID | Operation | From (S-ID) | To (S-ID) | Actor | Pre | Post |
**1C — Invariant Registry** | INV-ID | Invariant | Type | Threshold |
*(At least one numeric/temporal invariant with falsifiable threshold required.)*

---

## PART 2 — Trace Construction

Numbered steps (8–15). Per step: Actor | OP-ID | From (S-ID) | To (S-ID) | Precondition | Postcondition | Invariants
*Rejection steps*: "Entity remains in [From-State S-ID] after rejection. Any state change on
rejection is a detectable IST anomaly."

---

## PART 3 — Pre-Sweep Hypothesis
| Phase | Predicted | Count | Anomaly IDs |
*(lock before Phase 3A opens)*

---

## PART 4 — Phase Execution

Sequential lock chain: 3A → 3B → 3C → 3D → 3E → PART 5.

### Phases 3A–3D Anatomy (identical for each)

Each phase follows this sequence:
1. Role B pre-detection commitment: restate registry row verbatim + evidence standard
2. Pass 1 (Declaration-Only): scan declaration tables; score-aloud at discovery
3. Pass 2 (Trace-Diff): diff declared behavior against traced steps
4. Findings List
5. Evidence Strength Gate ☐
6. Role B Gap Record (5-field template, unconditional)
7. Exit Certification ☐ (Findings + Strength Gate + Gap Record)
8. PHASE 3N: COMPLETE

---

### Phase 3E — Undeclared References (URF) [LOCKED until PHASE 3D: COMPLETE]

Phase 3E is a full peer phase in the lock chain. Complete all eight steps in sequence.

**Step 1 — Role B Pre-Detection Commitment**
Restate the Phase 3E Standards Registry row verbatim.
State the specific evidence standard for URF findings in this trace.

**Step 2 — Pass 1: Declaration Scan (stratified by entity class)**

Each entity class is an independent sub-scan. A passing sub-scan for one class
does not satisfy the sweep requirement for any other class.

*P1-S — Subject class (S-IDs)*
| S-ID Reference | Declaration-Only Finding | Strength (1/2/3) | Evidence |
|----------------|--------------------------|-----------------|---------|
*(Score at discovery. Blank verdict = incomplete sub-scan.)*

*P1-O — Object class (OP-IDs)*
| OP-ID Reference | Declaration-Only Finding | Strength (1/2/3) | Evidence |
|----------------|--------------------------|-----------------|---------|

*P1-I — Identifier class (INV-IDs)*
| INV-ID Reference | Declaration-Only Finding | Strength (1/2/3) | Evidence |
|-----------------|--------------------------|-----------------|---------|

All three P1 sub-scans must be populated before Pass 2 opens.

**Step 3 — Pass 2: Trace-Diff Scan (stratified by entity class)**

Mirror Pass 1 exactly. Each entity class receives its own independent Trace-Diff
sub-scan. A verdict in one P2 sub-scan does not satisfy another.
A passing P1-S result does not substitute for P2-O or P2-I.

*P2-S — Subject class (S-IDs): Trace-Diff*
| Step | S-ID Reference in Trace | Declared? | Strength (1/2/3) | Evidence |
|------|------------------------|-----------|-----------------|---------|

*P2-O — Object class (OP-IDs): Trace-Diff*
| Step | OP-ID Reference in Trace | Declared? | Strength (1/2/3) | Evidence |
|------|--------------------------|-----------|-----------------|---------|

*P2-I — Identifier class (INV-IDs): Trace-Diff*
| Step | INV-ID Reference in Trace | Declared? | Strength (1/2/3) | Evidence |
|------|---------------------------|-----------|-----------------|---------|

All three P2 sub-scans must be independently populated. An absent P2-O or P2-I
row is a structural gap regardless of P2-S results.

**Step 4 — Findings List**: Consolidate across all six sub-scans (P1-S/O/I + P2-S/O/I).
Note entity class and detection pass for each finding.

**Step 5 — Evidence Strength Gate** ☐
At least one finding at strength ≥ 2 across any sub-scan, OR Gap Record explains why none met the standard.

**Step 6 — Role B Gap Record** [UNCONDITIONAL — 5-field template]
- Examined: *(partition by entity class: S-IDs scanned: ___ / OP-IDs scanned: ___ / INV-IDs scanned: ___)*
- Evidence Standard Applied: ___
- What Was Not Found: *(partition by entity class)*
- What Would Constitute a Finding: *(per entity class)*
- Verdict: ___

*The Gap Record is the unlock signal for the Phase 3E exit gate.*

**Step 7 — Phase 3E Exit Certification**
☐ P1-S sub-scan populated
☐ P1-O sub-scan populated
☐ P1-I sub-scan populated
☐ P2-S sub-scan populated
☐ P2-O sub-scan populated
☐ P2-I sub-scan populated
☐ Evidence Strength Gate satisfied
☐ Gap Record produced (all 5 fields populated)

**Step 8 — PHASE 3E: COMPLETE → PART 5 now OPEN**

---

## PART 5 — Reconciliation

| Phase | Predicted | Actual | C / FP / FN | Surprise? |
Calibration Score: C / (C + FP + FN) = ___%. Threshold 60%. Below-threshold: diagnose
systematic prediction failure by anomaly type, trace to declaration registry source.
Final Signal: domain-grounded one-paragraph conclusion.
```

---

## V-03 | Axis: Phrasing Register — Coaching Voice for Application Sentence

**Hypothesis**: A coaching prompt that names the distinction between restating a rule and binding it to evidence shape ("Not what the rule says — what it means for finding this anomaly here") elicits C-42 via prompted self-distinction rather than structural constraint. Phase 3E Pass 2 is present but not explicitly coached as stratified.

**Targets**: C-42 (primary). C-43 untargeted.

---

```
You are executing the **trace-state** skill.
Topic: {topic} | Domain: {domain} — Sales / Customer Service / Finance

Your job is to hand-compile a state machine, trace it step-by-step, and run a structured
anomaly sweep. Read each instruction carefully before acting on it. Complete each part
fully before moving to the next.

---

## PART 0 — Pre-Game Setup

Before you write a single trace step, complete two setup artifacts. These are sealed
once PART 1 opens — you cannot revise them later.

### 0A — Gap Record Template

Every Gap Record you produce in this trace — for every phase, regardless of how many
findings it contains — must use this exact 5-field form. A Gap Record with any field
blank is a structural failure, not an acceptable incomplete.

```
Examined: [List every ID you scanned]
Evidence Standard Applied: [Verbatim restate of your registry row]
Application Sentence: [See below — this is NOT the same as Evidence Standard Applied]
What Was Not Found: [Specific trace steps or state conditions that would constitute a finding]
Verdict: [ACQUITTED / FINDING: cross-reference]
```

**About the Application Sentence field**: The Evidence Standard Applied tells you
the rule ("Strength ≥ 2 required"). The Application Sentence tells you what that rule
means here — for this specific anomaly type, in this specific trace. Ask yourself: if I
were explaining to a colleague what counts as a qualifying piece of evidence for *this*
phase, what would I say? Write that. It should name specific things you would look for
in the trace — trace step elements, state IDs, timing patterns, declaration gaps — not
reproduce the generic threshold statement. A sentence that copies the Evidence Standard
Applied field is not an Application Sentence.

### 0B — Standards Registry

For each phase, write a single row. Before you detect anything, commit to what counts
as evidence for each anomaly type. You will restate these rows verbatim when each phase
opens. Once you write the last row and seal, you cannot change any standard.

| Phase | Anomaly Type | Min-Strength | Application Sentence |
|-------|-------------|--------------|---------------------|
| 3A | IST | ≥ 2 | *What does strength ≥ 2 mean for an IST finding? Not the rule — the evidence shape.* |
| 3B | MPC | ≥ 2 | *What does it mean for a precondition check to be missing at strength ≥ 2?* |
| 3C | IVC | ≥ 2 | *What does it mean for an invariant to be violated at strength ≥ 2?* |
| 3D | RCS | ≥ 2 | *What does a race condition look like at strength ≥ 2 in a step sequence?* |
| 3E | URF | ≥ 2 | *What does an undeclared reference look like at strength ≥ 2 across both detection passes?* |

Seal the registry now. Write: **REGISTRY SEALED.**

---

## PART 1 — State Machine Construction

Construct the state machine vocabulary your Domain Expert will use throughout the sweep.
Each ID you declare here will be cross-referenced in the trace and sweep tables.

**1A** — State Registry (S-IDs). Include an Entry Condition column.
**1B** — Operation Registry (OP-IDs). Include From-State, To-State, Actor, Precondition, Postcondition.
**1C** — Invariant Registry (INV-IDs). Include Type and Threshold.

Before you move to PART 2: check that you have at least one numeric or temporal invariant
with a specific falsifiable threshold. If not, add one now. This is the last chance.

---

## PART 2 — Trace Construction

Write 8–15 numbered steps. For each step, think through the before-state, the operation,
and the after-state explicitly. Don't skip the postcondition — that's where invariant
violations hide.

When you write a rejection step, note: after a rejection, the entity's state does not
change. The after-state equals the before-state. If you find yourself writing a rejection
step where the state does change, that is a finding — flag it now.

---

## PART 3 — Pre-Sweep Hypothesis

Before you open Phase 3A, make your predictions. You must commit to a yes/no prediction
and estimated count for each anomaly type. You will compare these to your actual findings
in PART 5. Be honest — a calibration score below 60% triggers a structural diagnosis.

| Phase | Finding? | Count | Expected IDs |

---

## PART 4 — Phase Execution

Work through phases in order: 3A → 3B → 3C → 3D → 3E → PART 5. Do not open the next
phase until the current phase is declared COMPLETE.

### Opening any phase: three things before you detect

1. Restate your registry row verbatim (copy it exactly from PART 0).
2. Confirm your evidence standard: "For [anomaly type] findings, I require..."
3. Ask yourself: what does strength ≥ 2 concretely mean for this anomaly class in this
   trace? Write that as your Application Sentence. This is active and specific — name the
   trace elements, state IDs, or timing patterns that would qualify. If you wrote something
   that sounds like a restatement of step 1, rewrite it.

### Running each phase: two detection passes

**Pass 1 (Declaration-Only)**: Scan your declaration tables without looking at the trace.
What does the declared behavior alone tell you about potential anomalies?
Record each finding as you discover it — score strength at that moment.

**Pass 2 (Trace-Diff)**: Now compare the trace against your declarations.
What does the trace show that the declarations don't account for?
Or what do the declarations require that the trace doesn't demonstrate?

### Closing each phase: three gates

After both passes: collect your Findings List, check the Evidence Strength Gate (at least
one finding at strength ≥ 2, or your Gap Record explains why not), and produce the Role B
Gap Record using the 0A template. The Gap Record must be produced regardless of finding
count. Then complete the exit certification checkboxes and declare PHASE 3N: COMPLETE.

---

### Phase 3E — Undeclared References (URF) [LOCKED until PHASE 3D: COMPLETE]

Phase 3E works the same way as Phases 3A–3D. The difference is that Pass 1 and Pass 2
each cover three entity classes: S-IDs (Subject), OP-IDs (Object), and INV-IDs (Identifier).

For Pass 1: scan each entity class separately. A clear result for S-IDs doesn't tell
you anything about OP-IDs or INV-IDs. Populate separate sub-scan sections for each.

For Pass 2: mirror Pass 1. Run a separate Trace-Diff sub-scan for each entity class.
Ask yourself: does my pass 2 result for S-IDs cover what I might have missed in OP-IDs?
It doesn't. Run them independently.

Complete the three-gate exit and declare **PHASE 3E: COMPLETE**.

---

## PART 5 — Reconciliation

Compare your PART 3 predictions to your actual findings.
Label each outcome: C (Correct), FP (False Positive — predicted finding, none found),
FN (False Negative — didn't predict, found one).
Compute: Calibration Score = C / (C + FP + FN).
If below 60%: identify which anomaly type drove the error and trace it to a specific
declaration registry gap or hypothesis methodology problem.

**Final Signal**: Write a one-paragraph conclusion in domain vocabulary on what these
findings say about the system's correctness and readiness.
```

---

## V-04 | Combined: Output Format + Lifecycle Emphasis

**Hypothesis**: Application Sentence as a named table column (V-01) combined with Phase 3E Pass 2 explicitly written out as three independent sub-scans (V-02) catches both C-42 and C-43 simultaneously. Neither axis interferes with the other: the table column forces C-42 as a detectable structural element, and the Phase 3E anatomy expansion forces C-43 as six independently checkable rows.

**Targets**: C-42 + C-43 (both).

---

```
You are executing the **trace-state** skill.
Topic: {topic} | Domain: {domain} — Sales / Customer Service / Finance

---

## PART 0 — Pre-Game Setup [SEAL before PART 1 opens]

### 0A — Gap Record Template (V-04 Contract)
All Gap Records across all five phases use the following 5-field template.
A Gap Record with any field blank is a structural failure.

| Field | Rule |
|-------|------|
| Examined | List every OP-ID / S-ID / INV-ID scanned |
| Evidence Standard Applied | Verbatim restate of the phase registry row |
| Application Sentence | Active binding: what does strength ≥ 2 mean for this anomaly class's evidence shape in this trace? Must differ from Evidence Standard Applied. |
| What Was Not Found | Specific trace steps / state conditions that would constitute a finding |
| Verdict | ACQUITTED (explain) or FINDING (ID cross-reference) |

**Application Sentence Rule**: The Application Sentence field is not satisfied by copying
the Evidence Standard Applied field. The standard is passive ("Strength ≥ 2 required").
The application sentence is active ("For [anomaly type] in this trace, strength ≥ 2 means:
[specific evidence elements]"). A Gap Record whose Application Sentence reproduces the
Evidence Standard Applied is a structural failure.

### 0B — Standards Registry

| Phase | Anomaly Type | Min-Strength | Application Sentence |
|-------|-------------|--------------|---------------------|
| 3A | Invalid State Transition (IST) | ≥ 2 | *Active binding for IST evidence shape in this trace* |
| 3B | Missing Precondition Check (MPC) | ≥ 2 | *Active binding for MPC evidence shape* |
| 3C | Invariant Violation (IVC) | ≥ 2 | *Active binding for IVC evidence shape* |
| 3D | Race Condition (RCS) | ≥ 2 | *Active binding for RCS evidence shape* |
| 3E | Undeclared Reference (URF) | ≥ 2 | *Active binding for URF evidence shape* |

**REGISTRY SEALED — no standard or Application Sentence may be revised after this point.**

---

## PART 1 — State Machine Construction

**1A — State Registry** | S-ID | State | Entry Condition | Entity-Class (S/O/I) |
**1B — Operation Registry** | OP-ID | Op | From (S-ID) | To (S-ID) | Actor | Pre | Post |
**1C — Invariant Registry** | INV-ID | Invariant | Type | Threshold |
*(Numeric/temporal invariant gate: at least one INV-ID with falsifiable threshold required.)*

---

## PART 2 — Trace Construction

Produce 8–15 numbered steps. Template per step:
Step N | Actor | OP-ID | From (S-ID) | To (S-ID) | Pre checked | Post verified | INVs checked
[REJECTED steps]: *"Entity remains in [From-State]. Rejection does not change state.
Any deviation is a detectable IST anomaly."*

---

## PART 3 — Pre-Sweep Hypothesis
| Phase | Finding? | Count | IDs |
*(Sealed before Phase 3A opens.)*

---

## PART 4 — Phase Execution

Sequential lock chain: 3A → 3B → 3C → 3D → 3E → PART 5.

### Phase Anatomy (applies to Phases 3A–3D)

Each phase executes in this sequence:

**[1] SCORING PROTOCOL** *(before detection begins)*

| Element | Content |
|---------|---------|
| Verbatim Restate | *Copy the Phase N registry row exactly* |
| Application Sentence | *Active binding: for [anomaly type] findings in this trace, strength ≥ 2 means [specific evidence shape — which elements, which IDs, what pattern].* |

*The Application Sentence must describe the evidence shape, not restate the threshold.
A sentence that reproduces the Verbatim Restate is a structural failure of this table.*

Role B pre-detection commitment: *"I require [evidence] before recording any finding."*

**[2] Pass 1 — Declaration-Only**
| Reference | Finding | Strength (1/2/3) | Evidence |
*(Score at discovery.)*

**[3] Pass 2 — Trace-Diff**
| Step | Finding | Strength (1/2/3) | Evidence |

**[4] Findings List**

**[5] Evidence Strength Gate** ☐

**[6] Gap Record** (5-field template, unconditional)
Application Sentence field must differ from Evidence Standard Applied field.

**[7] Exit Certification** ☐ Findings ☐ Strength Gate ☐ Gap Record ☐ App Sentence distinct

**[8] PHASE 3N: COMPLETE → Phase N+1 now OPEN**

---

### Phase 3E — Undeclared References (URF) [LOCKED until PHASE 3D: COMPLETE]

Phase 3E is a full peer phase. It has the same 8-step anatomy as Phases 3A–3D,
with Pass 1 and Pass 2 each stratified by entity class.

**[1] SCORING PROTOCOL**

| Element | Content |
|---------|---------|
| Verbatim Restate | *Copy the Phase 3E Standards Registry row exactly* |
| Application Sentence | *Active binding for URF: strength ≥ 2 means [which declaration table + which trace step pattern + which entity class confirms the reference undeclared]* |

Role B pre-detection commitment.

**[2] Pass 1 — Declaration Scan (stratified)**

A verdict in one sub-scan does not satisfy another sub-scan's requirement.

*P1-S — Subject class (S-IDs)*
| S-ID Reference | Declaration-Only Finding | Strength | Evidence |

*P1-O — Object class (OP-IDs)*
| OP-ID Reference | Declaration-Only Finding | Strength | Evidence |

*P1-I — Identifier class (INV-IDs)*
| INV-ID Reference | Declaration-Only Finding | Strength | Evidence |

**[3] Pass 2 — Trace-Diff Scan (stratified)**

Mirror Pass 1. Each entity class gets its own independent Trace-Diff sub-scan.
A passing P1-S result does not substitute for P2-O or P2-I.
A passing P2-S result does not satisfy P2-O or P2-I.

*P2-S — Subject class (S-IDs): Trace-Diff*
| Step | S-ID in Trace | Declared? | Strength | Evidence |

*P2-O — Object class (OP-IDs): Trace-Diff*
| Step | OP-ID in Trace | Declared? | Strength | Evidence |

*P2-I — Identifier class (INV-IDs): Trace-Diff*
| Step | INV-ID in Trace | Declared? | Strength | Evidence |

All six sub-scans (P1-S/O/I + P2-S/O/I) must be populated independently.
An absent P2-O or P2-I row is a structural gap regardless of P2-S result.

**[4] Findings List** — note entity class and pass for each finding.

**[5] Evidence Strength Gate** ☐

**[6] Gap Record** (5-field template, unconditional)
- Examined: *(partition: S-IDs: ___ / OP-IDs: ___ / INV-IDs: ___)*
- Evidence Standard Applied: ___
- Application Sentence: ___  ← *active binding for URF; must differ from Evidence Standard Applied*
- What Was Not Found: *(per entity class)*
- Verdict: ___

**[7] Phase 3E Exit Certification**
☐ P1-S populated ☐ P1-O populated ☐ P1-I populated
☐ P2-S populated ☐ P2-O populated ☐ P2-I populated
☐ Evidence Strength Gate ☐ Gap Record (5 fields) ☐ App Sentence distinct from Verbatim Restate

**[8] PHASE 3E: COMPLETE → PART 5 now OPEN**

---

## PART 5 — Reconciliation

| Phase | Predicted | Actual | C / FP / FN | Surprise? |
Calibration Score = C / (C + FP + FN). Threshold 60%.
Below threshold: diagnose by anomaly type → trace to declaration registry source.
Final Signal: domain-grounded conclusion on system readiness.
```

---

## V-05 | Combined: Lifecycle Emphasis + Phrasing Register

**Hypothesis**: Full structural expansion of both the per-phase scoring protocol and Phase 3E Pass 2 anatomy (V-02 lifecycle expansion) combined with coaching language that explicitly names the distinction the model must make (V-03 register) produces the strongest elicitation signal for both C-42 and C-43. The coaching narrows the conceptual gap; the structural expansion removes the implementation loophole.

**Targets**: C-42 + C-43 (both).

---

```
You are executing the **trace-state** skill.
Topic: {topic} | Domain: {domain} — Sales / Customer Service / Finance

Work through this prompt sequentially. Each part must be complete before the next part
opens. The numbered steps within each phase are not optional — they are the minimum
structure for this type of analysis to produce a credible signal.

---

## PART 0 — Pre-Game Setup

Complete both artifacts before you write a single trace step. PART 0 is sealed once
you begin PART 1. Nothing declared here can be revised after the seal.

### 0A — Gap Record Template

Every Gap Record you produce — in every phase, whether you found something or nothing —
must fill in these five fields. A Gap Record with a blank field is structurally incomplete.

```
Examined: [Every ID you scanned for this phase's anomaly type]
Evidence Standard Applied: [Your registry row, word for word]
Application Sentence: [See below]
What Was Not Found: [Describe the specific evidence that would constitute a finding]
Verdict: [ACQUITTED — explain / FINDING — cross-reference ID]
```

**On the Application Sentence**: There's a difference between knowing a rule and knowing
what the rule means in a specific situation. The Evidence Standard Applied field holds the
rule. The Application Sentence holds what that rule means for *this* anomaly type in *this*
trace. When you write the Application Sentence, ask: if I had to show a finding to a skeptic,
what evidence would I need to point to? What would it look like in the trace? That's your
application sentence. If what you've written is just the rule restated, rewrite it.

### 0B — Standards Registry

Before you analyze anything, commit to how you'll score evidence in each phase.
Write one registry row per phase. Once you seal, these standards are fixed.

| Phase | Anomaly Type | Min-Strength | Application Sentence |
|-------|-------------|--------------|---------------------|
| 3A | Invalid State Transition (IST) | ≥ 2 | *Concretely: for IST in this trace, what does strength ≥ 2 look like?* |
| 3B | Missing Precondition Check (MPC) | ≥ 2 | *Concretely: for MPC in this trace, what does strength ≥ 2 look like?* |
| 3C | Invariant Violation (IVC) | ≥ 2 | *Concretely: for IVC in this trace, what does strength ≥ 2 look like?* |
| 3D | Race Condition (RCS) | ≥ 2 | *Concretely: for RCS in this trace, what does strength ≥ 2 look like?* |
| 3E | Undeclared Reference (URF) | ≥ 2 | *Concretely: for URF in this trace, what does strength ≥ 2 look like — per entity class?* |

**REGISTRY SEALED.** You cannot revise these after this point.

---

## PART 1 — State Machine Construction

Before you trace anything, declare the vocabulary you'll use throughout.

**1A — State Registry**
| S-ID | State Name | Entry Condition | Description | Entity-Class (S/O/I) |

**1B — Operation Registry**
| OP-ID | Operation | From (S-ID) | To (S-ID) | Actor | Precondition | Postcondition |

**1C — Invariant Registry**
| INV-ID | Invariant | Type | Threshold |

Check before continuing: do you have at least one invariant with a falsifiable numeric or
temporal threshold? If not, add one now.

---

## PART 2 — Trace Construction

Write 8–15 numbered steps. Make them realistic for the domain. For each step:
- Before-state (S-ID), operation (OP-ID), after-state (S-ID)
- Precondition checked, postcondition verified, invariants checked

For any step where the operation is rejected: write explicitly that the entity remains
in its before-state. If you find a rejection that changes state, that's a finding — note it.

---

## PART 3 — Pre-Sweep Hypothesis

Before Phase 3A opens, commit to predictions for all five phases. You'll reconcile
these against your actual findings in PART 5. A calibration score below 60% triggers
a diagnostic — so make real predictions, not conservative ones.

| Phase | Finding? | Count | Expected IDs |

---

## PART 4 — Phase Execution

Run phases in order: 3A → 3B → 3C → 3D → 3E → PART 5.
Declare each phase COMPLETE before opening the next. This is a sequential lock —
writing Phase 3B content before PHASE 3A: COMPLETE is declared is a structural error.

### At the start of every phase: your scoring protocol

Before your first detection pass, commit to two things:

1. **Verbatim Restate** — copy your registry row for this phase exactly.
2. **Application Sentence** — don't just restate the standard. Ask yourself: what would
   a qualifying piece of evidence actually look like in this trace, for this anomaly type?
   Write that down as your application sentence. It should be specific to this phase's
   anomaly class — specific enough that you could recognize a qualifying finding when you
   see it. A sentence that sounds like "strength ≥ 2 means a finding at strength 2 or
   above" has not answered the question.

Then your role B pre-detection commitment: "For [anomaly type] findings, I require..."

### Each phase: two detection passes

**Pass 1 (Declaration-Only)**: Look at your declaration tables only — don't look at the
trace yet. What do the declarations alone tell you about potential anomalies? Record each
finding as you discover it and assign a strength score immediately.

**Pass 2 (Trace-Diff)**: Now look at the trace against your declarations. What does the
trace show that the declarations don't account for? What do the declarations require
that the trace doesn't demonstrate? Each pass is independent — a clean Pass 1 doesn't
tell you Pass 2 will be clean.

### Each phase: three exit gates

After both passes: produce the Findings List, satisfy the Evidence Strength Gate (at
least one finding at strength ≥ 2, or your Gap Record explains why not), and produce the
Role B Gap Record using the PART 0.0A template. The Gap Record fires unconditionally —
even if you found ten things, the Gap Record documents what you didn't find. Declare
PHASE 3N: COMPLETE.

---

### Phase 3E — Undeclared References (URF) [LOCKED until PHASE 3D: COMPLETE]

Phase 3E is a full phase, not a verification gate. It has the same anatomy as Phases
3A–3D, with one structural addition: both Pass 1 and Pass 2 run three independent
entity-class sub-scans.

**Step 1 — Scoring Protocol**

Verbatim restate of your Phase 3E registry row. Then your Application Sentence: what
does a URF finding look like in this trace at strength ≥ 2? This one is worth being
specific about per entity class — an undeclared S-ID looks different from an undeclared
OP-ID, and both look different from an undeclared INV-ID. Write an Application Sentence
that covers all three. Role B pre-detection commitment.

**Step 2 — Pass 1: Declaration Scan (three independent sub-scans)**

Run a separate declaration scan for each entity class. Ask yourself before combining:
does a clean S-ID scan tell you anything about OP-IDs? It doesn't. Keep them separate.

*P1-S — Subject class (S-IDs)*: scan for undeclared S-ID references in the declaration tables.
| S-ID | Declaration-Only Finding | Strength | Evidence |

*P1-O — Object class (OP-IDs)*: scan for undeclared OP-ID references in the declaration tables.
| OP-ID | Declaration-Only Finding | Strength | Evidence |

*P1-I — Identifier class (INV-IDs)*: scan for undeclared INV-ID references.
| INV-ID | Declaration-Only Finding | Strength | Evidence |

A passing P1-S sub-scan does not satisfy P1-O or P1-I.

**Step 3 — Pass 2: Trace-Diff Scan (three independent sub-scans)**

Now mirror Pass 1 against the trace. This is where the structural discipline matters:
do not run a single trace scan that covers all three classes together. Run three
independent sub-scans. Ask before you start each one: have I looked at this entity class
specifically, or did I absorb it into the S-ID scan? Run them separately.

*P2-S — Subject class (S-IDs): Trace-Diff*
| Step | S-ID in Trace | Declared? | Strength | Evidence |

*P2-O — Object class (OP-IDs): Trace-Diff*
| Step | OP-ID in Trace | Declared? | Strength | Evidence |

*P2-I — Identifier class (INV-IDs): Trace-Diff*
| Step | INV-ID in Trace | Declared? | Strength | Evidence |

A clean P2-S result tells you nothing about P2-O or P2-I. Populate all three.
An absent P2-O or P2-I table is a structural gap regardless of P2-S results.

**Step 4 — Findings List**: Note entity class and detection pass for each finding.

**Step 5 — Evidence Strength Gate** ☐

**Step 6 — Gap Record** (5-field template — unconditional)
Partition the Examined and What Was Not Found fields by entity class.
- Examined: S-IDs: ___ / OP-IDs: ___ / INV-IDs: ___
- Evidence Standard Applied: ___
- Application Sentence: _(active binding per entity class — must differ from Evidence Standard Applied)_
- What Was Not Found: per entity class
- Verdict: ___

**Step 7 — Phase 3E Exit Certification**
☐ P1-S populated ☐ P1-O populated ☐ P1-I populated
☐ P2-S populated ☐ P2-O populated ☐ P2-I populated
☐ Evidence Strength Gate satisfied
☐ Gap Record: all 5 fields complete
☐ Gap Record Application Sentence distinct from Evidence Standard Applied

**Step 8 — PHASE 3E: COMPLETE → PART 5 now OPEN**

---

## PART 5 — Reconciliation

Look back at your PART 3 predictions. For each prediction, record what you actually
found and classify the outcome: C (Correct), FP (predicted a finding, found none),
FN (predicted none, found one).

| Phase | Predicted | Actual | C/FP/FN | Surprise? |

Calibration Score = C / (C + FP + FN). If below 60%: identify which anomaly type drove
the prediction failure, trace it to a specific declaration registry entry or trace
construction gap, and say whether the failure was hypothesis methodology or declaration
completeness.

**Final Signal**: One paragraph in domain vocabulary. What do these findings say about
the system's state machine correctness and the team's readiness to commit to this design?
```

---

## Variation Summary

| Variation | Axis | C-42 Target | C-43 Target | Mechanism |
|-----------|------|-------------|-------------|-----------|
| V-01 | Output Format | Named table column per phase (structural failure if blank) | Not targeted | SCORING PROTOCOL table with mandatory Application Sentence column |
| V-02 | Lifecycle Emphasis | Registry column present; not structurally separated | Named P2-S/P2-O/P2-I sub-scans symmetric with Pass 1 | Phase 3E 8-step anatomy with 6 independent tables |
| V-03 | Phrasing Register | Coaching question ("What would evidence look like?") + negative rule ("not a restatement") | Coaching instruction ("mirror Pass 1; run them independently") | Self-distinction prompt; no output-format enforcement |
| V-04 | Output Format + Lifecycle | Named table column, structural failure rule | Named P2-S/P2-O/P2-I sub-scans, 6 independent exit gate checkboxes | Both mechanisms simultaneously; no interaction between them |
| V-05 | Lifecycle + Phrasing | Full per-phase anatomy with Application Sentence step + active/passive distinction coaching | Full Pass 2 anatomy with coaching on entity-class independence | Structural expansion + conceptual guidance; highest elicitation signal |
