# trace-state Rubric v8 — Variation Set V-01 through V-05

---

## V-01
**Axis**: Role sequence
**Hypothesis**: Front-loading the Acquittal Advocate as a *co-active* role from Phase 1 (rather than activating only on "no finding") forces richer gap documentation because the advocate must produce a search record regardless of outcome, not just when the analyst gives up.

---

You are conducting a hand-compiled state transition analysis. Two roles operate throughout this session. Both are active from the start.

**Role A — Domain Analyst** (Sales / Customer Service / Finance — choose one domain and hold it for the entire session): Declares entity states, traces operations step by step, asserts preconditions, postconditions, and invariants, and identifies anomalies. All entity names, state labels, and operation names must be recognizable vocabulary in your chosen domain.

**Role B — Acquittal Advocate** (active throughout, not only on no-finding): For every phase, before Role A closes the phase, Role B must produce a signed Gap Record. The Gap Record names: (a) the specific trace steps examined, (b) the state conditions that were present, and (c) the exact evidence that would have been required to produce a finding if one had been possible. The Gap Record is not optional. The Gap Record is the unlock signal for the phase exit gate.

---

### DECLARATION STAGE — PHASE: OPEN

Produce the following tables before any trace work begins.

**State Registry** — assign each state an S-ID (S-01, S-02, …):

| S-ID | State Name | Entry Condition | Terminal? |
|------|------------|-----------------|-----------|
| S-01 | … | … | … |

**Operation Registry** — assign each operation an OP-ID (OP-01, OP-02, …):

| OP-ID | Operation Name | Allowed From States | Produces State |
|-------|----------------|--------------------:|----------------|
| OP-01 | … | … | … |

**Invariant Registry** — assign each invariant an INV-ID (INV-01, INV-02, …). At least one invariant must be numeric or temporal (a falsifiable threshold, duration, or count — not a qualitative rule):

| INV-ID | Invariant Statement | Scope (states or lifecycle-wide) | Numeric/Temporal? |
|--------|--------------------|------------------------------------|-------------------|
| INV-01 | … | … | Yes / No |

**Pre-Sweep Hypothesis** — before the trace runs, state:
- Which anomaly type you predict will produce the most findings and why.
- Which invariant you expect to be most vulnerable and why.
- One operation you predict will have a missing precondition check.

Record the prediction. You will reconcile it after the sweep.

**DECLARATION STAGE: COMPLETE** ← emit this exact line to unlock Phase 1.

---

### TRACE STAGE — PHASE: OPEN

Produce a numbered step-by-step trace of the normal lifecycle. For each step:

**Step N — [OP-ID] Operation Name**
- Before state: [S-ID] State Name | key fields: …
- Preconditions: (list each, state-specific — not vague)
- Operation: what executes
- After state: [S-ID] State Name | key fields: …
- Postconditions: (list each, guaranteed facts after execution)
- Invariant check: list every INV-ID that must hold; mark HOLDS / VIOLATION

Minimum three operations must be traced. At least one negative path must appear: an operation attempted from a disallowed state, showing the rejection reason (which precondition fails or which invariant would be violated).

**TRACE STAGE: COMPLETE** ← emit this exact line to unlock Phase 1.

---

### PHASE 1 — INVALID STATE TRANSITIONS | STATUS: LOCKED

> Phase 1 is locked until TRACE STAGE: COMPLETE has been emitted.

**Role A** runs the sweep in two independent passes:

| OP-ID | Declaration-Only Finding | Trace-Diff Finding |
|-------|--------------------------|-------------------|
| OP-01 | … | … |

*Declaration-Only*: examine the Operation Registry and State Registry alone. Does any declared operation reference a state transition that contradicts stated entry conditions?
*Trace-Diff*: compare what the declaration tables claim against the traced step sequence. Does any declaration appear that is not demonstrated in the trace?

A "None" in either cell requires an inline gap record in that cell: name the steps examined, the conditions present, and the evidence that would be required for a finding.

Evidence strength: assign 1 (weak — circumstantial), 2 (moderate — behavioral), or 3 (strong — direct state proof) when each finding is first recorded, not retroactively. At least one finding must score ≥ 2 for the phase to count as substantive. Minimum expected findings: 1.

**Role B Gap Record — Phase 1**
Regardless of finding count, Role B produces a signed Gap Record before the exit gate opens:
> Gap Record P1: Steps examined: [list OP-IDs]. Conditions present: [list S-IDs]. Evidence required for a finding that was absent: [specific state conditions, timing windows, or declaration contradictions that would have constituted a finding].

**Phase 1 Exit Gate Checklist**:
- [ ] Op Registry cross-referenced against trace (C-12 satisfied)
- [ ] Both detection columns populated per row (C-30 satisfied)
- [ ] Role B Gap Record produced and signed (C-29 satisfied)
- [ ] Evidence strength assigned at point of discovery (C-22 satisfied)
- [ ] Numeric/temporal invariant gate: at least one INV with Numeric/Temporal = Yes was checked in this phase (C-20 satisfied)

**PHASE 1: COMPLETE** ← emit this exact line to unlock Phase 2.

---

### PHASE 2 — MISSING PRECONDITION CHECKS | STATUS: LOCKED

> Phase 2 is locked until PHASE 1: COMPLETE has been emitted.

**Role A** runs the dual-pass sweep:

| OP-ID | Declaration-Only Finding | Trace-Diff Finding |
|-------|--------------------------|-------------------|
| OP-01 | … | … |

*Declaration-Only*: Does any operation in the registry lack a declared precondition, or declare a precondition that is vague (not state-specific)?
*Trace-Diff*: Does the trace demonstrate any operation executing without verifying its declared preconditions?

Evidence strength assigned at point of discovery. Minimum expected findings: 1.

**Role B Gap Record — Phase 2** (required before exit gate opens):
> Gap Record P2: Steps examined: [list]. Conditions present: [list]. Evidence required for a missing-precondition finding that was absent: [specific].

**Phase 2 Exit Gate Checklist**:
- [ ] Both detection columns populated (C-30)
- [ ] Role B Gap Record produced (C-29)
- [ ] Evidence strength scored at discovery (C-22)
- [ ] At least one numeric/temporal invariant checked in this phase (C-20)

**PHASE 2: COMPLETE** ← emit this exact line to unlock Phase 3.

---

### PHASE 3 — INVARIANT VIOLATIONS | STATUS: LOCKED

> Phase 3 is locked until PHASE 2: COMPLETE has been emitted.

**Role A** runs the dual-pass sweep:

| INV-ID | Declaration-Only Finding | Trace-Diff Finding |
|--------|--------------------------|-------------------|
| INV-01 | … | … |

*Declaration-Only*: Does any invariant in the Invariant Registry contradict the declared state machine (e.g., a state that is reachable but the invariant forbids it)?
*Trace-Diff*: Does any traced step demonstrate a state that violates a declared invariant?

Evidence strength at point of discovery. Minimum expected findings: 1.

**Role B Gap Record — Phase 3** (required):
> Gap Record P3: INV-IDs examined: [list]. State conditions present: [list]. Evidence required for a violation that was absent: [specific].

**Phase 3 Exit Gate Checklist**:
- [ ] Both detection columns populated (C-30)
- [ ] Role B Gap Record produced (C-29)
- [ ] Evidence strength scored at discovery (C-22)
- [ ] Numeric/temporal invariant was focal in this phase (C-20)

**PHASE 3: COMPLETE** ← emit this exact line to unlock Phase 4.

---

### PHASE 4 — RACE CONDITIONS | STATUS: LOCKED

> Phase 4 is locked until PHASE 3: COMPLETE has been emitted.

**Role A** constructs a concurrent scenario: two operations initiated against the same entity before either completes. Trace the interleaving. Document the window of vulnerability.

| Scenario | Declaration-Only Finding | Trace-Diff Finding |
|----------|--------------------------|-------------------|
| Concurrent OP-XX + OP-YY | … | … |

Evidence strength at point of discovery. Minimum expected findings: 1.

**Role B Gap Record — Phase 4** (required):
> Gap Record P4: Concurrent scenarios examined: [list]. Window conditions present: [describe]. Evidence required for a race condition that was absent: [specific timing or ordering conditions].

**Phase 4 Exit Gate Checklist**:
- [ ] Both detection columns populated (C-30)
- [ ] Role B Gap Record produced (C-29)
- [ ] Evidence strength scored at discovery (C-22)

**PHASE 4: COMPLETE** ← emit this exact line to unlock Phase 5.

---

### PHASE 5 — UNDECLARED REFERENCES | STATUS: LOCKED

> Phase 5 is locked until PHASE 4: COMPLETE has been emitted.

**Role A** scans the trace for any S-ID, OP-ID, or INV-ID referenced in a step that does not appear in a registry. An undeclared reference is an anomaly of its own class.

| Reference Found | Type (S/OP/INV) | Declaration-Only Finding | Trace-Diff Finding |
|-----------------|-----------------|--------------------------|-------------------|
| … | … | … | … |

**Role B Gap Record — Phase 5** (required):
> Gap Record P5: References scanned: [list]. Undeclared references absent because: [specific].

**PHASE 5: COMPLETE** ← emit this exact line to unlock the Reconciliation Stage.

---

### RECONCILIATION STAGE — PHASE: LOCKED

> Reconciliation is locked until PHASE 5: COMPLETE has been emitted.

**Consolidated Anomaly Register**:

| Finding-ID | Phase | OP-ID / S-ID / INV-ID | Anomaly Type | Evidence Strength | Discovery Score |
|------------|-------|----------------------|--------------|------------------|-----------------|
| F-01 | … | … | … | 1/2/3 | … |

**Hypothesis Reconciliation** — return to each pre-sweep prediction:

| Prediction | Outcome | Classification | Notes |
|------------|---------|---------------|-------|
| Most findings in [phase] | [actual] | C / FP / FN | … |
| [INV-ID] most vulnerable | [actual] | C / FP / FN | … |
| [OP-ID] missing precondition | [actual] | C / FP / FN | … |

*Classification key*: C = Correct prediction, FP = predicted finding that didn't materialize, FN = finding occurred that was not predicted.

**Calibration score** = C / (C + FP + FN). If calibration < 0.5, diagnose the structural reason: was the hypothesis based on surface features (operation name) rather than structural properties (entry condition gaps, invariant scope)?

---

## V-02
**Axis**: Output format
**Hypothesis**: Leading with the sweep table as the primary structure (table-first) and filling in prose only as annotations to table cells forces mechanical compliance from the first output token, reducing the pattern of producing rich prose that then fails to populate required table columns.

---

You are conducting a hand-compiled state transition analysis. Domain: choose one of Sales, Customer Service, or Finance and hold it for the entire session. All entity names, state labels, and operation names must be realistic vocabulary from that domain.

Two roles:
- **Role A — Domain Analyst**: traces states, operations, preconditions, postconditions, invariants, and anomalies.
- **Role B — Acquittal Advocate**: activates when any anomaly-type phase reaches a "no finding" verdict; produces a Gap Record before the phase exit gate opens; cannot be bypassed.

---

### OUTPUT CONTRACT

Every major output in this session is a **table first**. Prose appears only as annotations inside table cells or in labeled footnotes beneath a table. A prose paragraph that is not anchored to a table cell does not satisfy any criterion.

---

### TABLE 1 — State Registry

| S-ID | State Name | Entry Condition | Terminal? |
|------|------------|-----------------|-----------|
| S-01 | | | |

*Populate fully before proceeding. Minimum 3 states.*

### TABLE 2 — Operation Registry

| OP-ID | Operation Name | Allowed-From S-IDs | Produces S-ID | Preconditions | Postconditions |
|-------|----------------|-------------------|---------------|---------------|----------------|
| OP-01 | | | | | |

*Preconditions and postconditions must be state-specific — not vague. Minimum 3 operations.*

### TABLE 3 — Invariant Registry

| INV-ID | Invariant Statement | Scope | Numeric/Temporal? | Threshold or Duration |
|--------|--------------------|----|---|---|
| INV-01 | | | | |

*At least one invariant must have Numeric/Temporal = Yes with a concrete threshold or duration.*

### TABLE 4 — Pre-Sweep Predictions

| Prediction Target | Prediction | Reasoning |
|-------------------|------------|-----------|
| Phase with most findings | | |
| Most vulnerable invariant | | |
| Operation missing precondition | | |

*Fill before running any trace. These are locked predictions — do not revise retroactively.*

**DECLARATION STAGE: COMPLETE**

---

### TABLE 5 — Step-by-Step Trace

| Step | OP-ID | Before S-ID | Before Key Fields | Precondition Check | Operation | After S-ID | After Key Fields | Postcondition Check | INV-IDs Checked | Result |
|------|-------|-------------|------------------|-------------------|-----------|-----------|-----------------|--------------------|--------------------|--------|
| 1 | | | | | | | | | | PASS/FAIL |

*Minimum 3 steps including at least one rejected transition. A rejected transition shows Before S-ID, the attempted OP-ID, the failing precondition, and Result = REJECTED.*

**TRACE STAGE: COMPLETE**

---

### TABLE 6 — Phase 1 Sweep: Invalid State Transitions | PHASE 1 STATUS: LOCKED → OPEN after TRACE STAGE: COMPLETE

| OP-ID | Declaration-Only Finding | Evidence Str. (1/2/3) | Trace-Diff Finding | Evidence Str. (1/2/3) |
|-------|--------------------------|----------------------|--------------------|----------------------|
| OP-01 | | | | |

*Rules:*
- *"None" in Declaration-Only Finding: write inline gap record — steps examined, conditions present, evidence required.*
- *"None" in Trace-Diff Finding: same.*
- *Evidence strength assigned now, not retroactively.*
- *Minimum 1 finding with strength ≥ 2.*

**Phase 1 Exit Gate**:

| Gate | Criterion | Status |
|------|-----------|--------|
| G-P1-1 | Op Registry cross-referenced against trace | ☐ |
| G-P1-2 | Both detection columns populated per row | ☐ |
| G-P1-3 | Role B Gap Record produced (if no-finding verdict) | ☐ |
| G-P1-4 | Evidence strength scored at point of discovery | ☐ |
| G-P1-5 | At least one numeric/temporal invariant checked | ☐ |

**PHASE 1: COMPLETE**

---

### TABLE 7 — Phase 2 Sweep: Missing Precondition Checks | PHASE 2 STATUS: LOCKED → OPEN after PHASE 1: COMPLETE

| OP-ID | Declaration-Only Finding | Evidence Str. | Trace-Diff Finding | Evidence Str. |
|-------|--------------------------|--------------|-------------------|--------------|
| OP-01 | | | | |

*Same inline gap record rule for "None" cells. Evidence strength at discovery.*

**Phase 2 Exit Gate**:

| Gate | Criterion | Status |
|------|-----------|--------|
| G-P2-1 | Both detection columns populated | ☐ |
| G-P2-2 | Role B Gap Record produced if no-finding | ☐ |
| G-P2-3 | Evidence strength at discovery | ☐ |
| G-P2-4 | Numeric/temporal invariant checked | ☐ |

**PHASE 2: COMPLETE**

---

### TABLE 8 — Phase 3 Sweep: Invariant Violations | PHASE 3 STATUS: LOCKED → OPEN after PHASE 2: COMPLETE

| INV-ID | Declaration-Only Finding | Evidence Str. | Trace-Diff Finding | Evidence Str. |
|--------|--------------------------|--------------|-------------------|--------------|
| INV-01 | | | | |

*Numeric/temporal invariants must appear as focal rows.*

**Phase 3 Exit Gate**:

| Gate | Criterion | Status |
|------|-----------|--------|
| G-P3-1 | Both detection columns populated | ☐ |
| G-P3-2 | Role B Gap Record produced if no-finding | ☐ |
| G-P3-3 | Evidence strength at discovery | ☐ |
| G-P3-4 | Numeric/temporal invariant was focal | ☐ |

**PHASE 3: COMPLETE**

---

### TABLE 9 — Phase 4 Sweep: Race Conditions | PHASE 4 STATUS: LOCKED → OPEN after PHASE 3: COMPLETE

| Scenario (OP-IDs) | Interleaving Description | Declaration-Only Finding | Evidence Str. | Trace-Diff Finding | Evidence Str. |
|-------------------|--------------------------|--------------------------|--------------|-------------------|--------------|
| | | | | | |

*Construct at least one concurrent scenario: two operations against the same entity before either completes.*

**Phase 4 Exit Gate**:

| Gate | Criterion | Status |
|------|-----------|--------|
| G-P4-1 | Both detection columns populated | ☐ |
| G-P4-2 | Role B Gap Record produced if no-finding | ☐ |
| G-P4-3 | Evidence strength at discovery | ☐ |

**PHASE 4: COMPLETE**

---

### TABLE 10 — Phase 5 Sweep: Undeclared References | PHASE 5 STATUS: LOCKED → OPEN after PHASE 4: COMPLETE

| Reference Found in Trace | Type (S/OP/INV) | Appears in Registry? | Declaration-Only Finding | Trace-Diff Finding |
|--------------------------|-----------------|----------------------|--------------------------|-------------------|
| | | | | |

**PHASE 5: COMPLETE**

---

### TABLE 11 — Consolidated Anomaly Register | RECONCILIATION STATUS: LOCKED → OPEN after PHASE 5: COMPLETE

| F-ID | Phase | OP-ID / S-ID / INV-ID | Anomaly Type | Evidence Str. | Blank-cell check |
|------|-------|----------------------|--------------|--------------|------------------|
| F-01 | | | | | (blank = detectable gap) |

*Any blank cell in a row with a finding verdict is a mechanical gap. Flag it.*

### TABLE 12 — Hypothesis Reconciliation

| Prediction | Actual Outcome | Classification (C / FP / FN) | Notes |
|------------|---------------|------------------------------|-------|
| Most findings: [phase] | | | |
| Vulnerable invariant: [INV-ID] | | | |
| Missing precondition: [OP-ID] | | | |

**Calibration score** = C ÷ (C + FP + FN) = ___

If < 0.50: diagnose structural cause — was prediction based on surface feature (name) rather than structural property (entry condition gap, invariant scope boundary)?

---

## V-03
**Axis**: Lifecycle emphasis
**Hypothesis**: Making phase LOCKED/OPEN status a dominant visual banner — appearing as the first line of every section rather than embedded inline — reduces phase-skipping because the model must actively emit the status before producing any content, creating a mandatory acknowledge-before-proceeding ceremony.

---

You are conducting a hand-compiled state transition analysis.

**Domain**: Select Sales, Customer Service, or Finance. Hold this domain for the entire session. Domain vocabulary governs all entity names, state labels, and operation names.

**Roles**:
- **Role A — Domain Analyst**: declares the state machine, traces operations, identifies anomalies.
- **Role B — Acquittal Advocate**: activates automatically when any phase reaches a preliminary no-finding verdict; produces a mandatory Gap Record; the Gap Record is the mechanical unlock signal for that phase's exit gate.

---

## ══════════════════════════════════════════
## DECLARATION STAGE
## PHASE STATUS: ██ OPEN ██
## ══════════════════════════════════════════

**State Registry** (S-IDs: S-01, S-02, …):

| S-ID | State Name | Entry Condition | Terminal? |
|------|------------|-----------------|-----------|

**Operation Registry** (OP-IDs: OP-01, OP-02, …):

| OP-ID | Operation | Allowed-From S-IDs | Produces S-ID | Preconditions | Postconditions |
|-------|-----------|-------------------|---------------|---------------|----------------|

**Invariant Registry** (INV-IDs: INV-01, INV-02, …):

| INV-ID | Invariant Statement | Scope | Numeric/Temporal? | Threshold |
|--------|--------------------|----|---|---|

Requirement: at least one invariant must have Numeric/Temporal = Yes with a stated threshold or duration.

**Pre-Sweep Predictions** (locked — do not revise after the trace runs):

| Target | Prediction | Structural Reason |
|--------|------------|-------------------|
| Phase producing most findings | | |
| Most vulnerable invariant | | |
| Operation most likely missing a precondition check | | |

---

## ══ DECLARATION STAGE: COMPLETE ══
## (Emitting this line unlocks the Trace Stage)
## ══════════════════════════════════════════

---

## ══════════════════════════════════════════
## TRACE STAGE
## PHASE STATUS: ██ OPEN ██ (unlocked by DECLARATION STAGE: COMPLETE)
## ══════════════════════════════════════════

Produce a numbered trace. Each step:

**Step N — [OP-ID] [Operation Name]**
- Before state: [S-ID] — key fields: …
- Preconditions verified: (state-specific, one per bullet)
- After state: [S-ID] — key fields: …
- Postconditions guaranteed: (state-specific, one per bullet)
- Invariant check: [INV-IDs] → HOLDS / VIOLATION

Include at least one rejected transition (an operation attempted from a disallowed state, documenting which precondition fails).

---

## ══ TRACE STAGE: COMPLETE ══
## (Emitting this line unlocks Phase 1)
## ══════════════════════════════════════════

---

## ══════════════════════════════════════════
## PHASE 1 — INVALID STATE TRANSITIONS
## PHASE STATUS: ██ LOCKED ██
## Unlock condition: TRACE STAGE: COMPLETE emitted above
## ══════════════════════════════════════════

*(Do not produce Phase 1 content until the unlock condition is confirmed in the prior stage.)*

**Dual-pass sweep table**:

| OP-ID | Declaration-Only Finding | Evid. Str. | Trace-Diff Finding | Evid. Str. |
|-------|--------------------------|-----------|-------------------|-----------|
| OP-01 | | | | |

Rules:
- "None" in any finding cell = inline gap record required in that cell: (steps examined / conditions present / evidence that would constitute a finding).
- Evidence strength: 1 weak / 2 moderate / 3 strong — assigned when the finding is first recorded. At least one finding must score ≥ 2.
- Minimum expected findings: 1.

**Score-Aloud Protocol**: Before closing each row, Role A states aloud: "I am assigning evidence strength [N] because [specific state evidence]. I am not adjusting this after reviewing later rows."

**Acquittal Advocate Activation**: If Phase 1 produces a no-finding preliminary verdict in either column, Role B activates immediately and produces:
> **Gap Record P1-[col]**: Steps examined: … | S-IDs in scope: … | OP-IDs in scope: … | Evidence that would constitute a finding: (state transition claim + which entry condition would need to be violated) …

**Phase 1 Exit Gate** — all gates must be checked before PHASE 1: COMPLETE is emitted:
- [ ] Op Registry cross-referenced against trace (C-12)
- [ ] Both detection columns populated per row (C-30)
- [ ] No bare "None" — each "None" cell contains an inline gap record (C-27/C-30)
- [ ] Score-aloud protocol executed per row (C-23)
- [ ] Evidence strength scored at discovery, not retroactively (C-22)
- [ ] At least one numeric/temporal invariant was checked in this phase (C-20)
- [ ] Role B Gap Record produced for any no-finding column (C-29)

---

## ══ PHASE 1: COMPLETE ══
## (Emitting this line unlocks Phase 2)
## ══════════════════════════════════════════

---

## ══════════════════════════════════════════
## PHASE 2 — MISSING PRECONDITION CHECKS
## PHASE STATUS: ██ LOCKED ██
## Unlock condition: PHASE 1: COMPLETE emitted above
## ══════════════════════════════════════════

**Dual-pass sweep table**:

| OP-ID | Declaration-Only Finding | Evid. Str. | Trace-Diff Finding | Evid. Str. |
|-------|--------------------------|-----------|-------------------|-----------|

*"None" cell rule, score-aloud protocol, Role B activation: same as Phase 1.*

**Phase 2 Exit Gate**:
- [ ] Both detection columns populated (C-30)
- [ ] No bare "None" in any cell (C-27)
- [ ] Score-aloud per row (C-23)
- [ ] Role B Gap Record if no-finding (C-29)
- [ ] Numeric/temporal invariant checked (C-20)

---

## ══ PHASE 2: COMPLETE ══
## (Emitting this line unlocks Phase 3)
## ══════════════════════════════════════════

---

## ══════════════════════════════════════════
## PHASE 3 — INVARIANT VIOLATIONS
## PHASE STATUS: ██ LOCKED ██
## Unlock condition: PHASE 2: COMPLETE emitted above
## ══════════════════════════════════════════

**Dual-pass sweep table**:

| INV-ID | Declaration-Only Finding | Evid. Str. | Trace-Diff Finding | Evid. Str. |
|--------|--------------------------|-----------|-------------------|-----------|

*Numeric/temporal invariants must appear as focal rows. "None" cell rule applies.*

**Phase 3 Exit Gate**:
- [ ] Both detection columns populated (C-30)
- [ ] Numeric/temporal invariant was focal (C-20)
- [ ] Score-aloud per row (C-23)
- [ ] Role B Gap Record if no-finding (C-29)

---

## ══ PHASE 3: COMPLETE ══
## (Emitting this line unlocks Phase 4)
## ══════════════════════════════════════════

---

## ══════════════════════════════════════════
## PHASE 4 — RACE CONDITIONS
## PHASE STATUS: ██ LOCKED ██
## Unlock condition: PHASE 3: COMPLETE emitted above
## ══════════════════════════════════════════

Construct a concurrent scenario: two operations initiated against the same entity before either completes. Trace the interleaving. Document the vulnerability window.

**Dual-pass sweep table**:

| Scenario | Declaration-Only Finding | Evid. Str. | Trace-Diff Finding | Evid. Str. |
|----------|--------------------------|-----------|-------------------|-----------|

**Phase 4 Exit Gate**:
- [ ] Both detection columns populated (C-30)
- [ ] Score-aloud per row (C-23)
- [ ] Role B Gap Record if no-finding (C-29)

---

## ══ PHASE 4: COMPLETE ══
## (Emitting this line unlocks Phase 5)
## ══════════════════════════════════════════

---

## ══════════════════════════════════════════
## PHASE 5 — UNDECLARED REFERENCES
## PHASE STATUS: ██ LOCKED ██
## Unlock condition: PHASE 4: COMPLETE emitted above
## ══════════════════════════════════════════

Scan the trace for any S-ID, OP-ID, or INV-ID that appears in a step but does not appear in the corresponding registry. An undeclared reference is an anomaly class of its own.

| Reference | Type | In Registry? | Declaration-Only Finding | Trace-Diff Finding |
|-----------|------|-------------|--------------------------|-------------------|

**Phase 5 Exit Gate**:
- [ ] All trace references checked against registries (C-16)
- [ ] Role B Gap Record if no-finding (C-29)

---

## ══ PHASE 5: COMPLETE ══
## (Emitting this line unlocks Reconciliation)
## ══════════════════════════════════════════

---

## ══════════════════════════════════════════
## RECONCILIATION STAGE
## PHASE STATUS: ██ LOCKED ██
## Unlock condition: PHASE 5: COMPLETE emitted above
## ══════════════════════════════════════════

**Consolidated Anomaly Register**:

| F-ID | Phase | OP-ID/S-ID/INV-ID | Type | Evid. Str. | Blank-cell check |
|------|-------|------------------|------|-----------|-----------------|
| F-01 | | | | | |

A blank cell in any found-verdict row is a detectable mechanical gap — flag it.

**Hypothesis Reconciliation**:

| Prediction | Actual | C / FP / FN | Diagnosis |
|------------|--------|-------------|-----------|
| Most findings: [phase] | | | |
| Vulnerable invariant: [INV-ID] | | | |
| Missing precondition: [OP-ID] | | | |

Calibration = C ÷ (C + FP + FN) = ___

If calibration < 0.50: perform a structural diagnosis — was the prediction based on a surface feature (operation name, domain familiarity) or a structural property (entry condition gap, invariant boundary)?

---

## ══ RECONCILIATION STAGE: COMPLETE ══
## ══════════════════════════════════════════

---

## V-04
**Axes**: Role sequence + Phrasing register (combo)
**Hypothesis**: A conversational register with explicit role-activation ceremony language — where the model narrates which role is speaking before each output block — reduces silent role-merging (the failure mode where Role A and Role B collapse into a single voice that never challenges its own conclusions). Making the handoff audible forces genuine adversarial separation.

---

We're going to hand-compile a state transition analysis together. Pick one domain — Sales, Customer Service, or Finance — and stay in it. The entity names, state labels, and operation names you use should be things a practitioner in that domain would recognize without explanation.

There are two voices in this analysis.

**Voice A (Domain Analyst)** is the one who builds the state machine and runs the trace. Voice A produces registries, steps, and sweep findings.

**Voice B (Acquittal Advocate)** speaks up whenever a phase is about to close with no finding. Voice B doesn't just say "nothing found" — Voice B names the specific steps, states, and conditions that were searched, and the exact evidence that would have been needed to produce a finding if the conditions had been different. Voice B's statement is what unlocks the phase gate. Without it, the gate stays closed.

When you switch between voices, say so. Write "Voice A:" or "Voice B:" before each block. Don't let them merge into a single narrator.

---

### Getting started: build your declaration tables

Voice A, set up three tables before the trace begins.

**State table** — give each state an S-ID:

| S-ID | State Name | Entry Condition | Terminal? |
|------|------------|-----------------|-----------|

**Operation table** — give each operation an OP-ID:

| OP-ID | Operation | Allowed-From S-IDs | Produces S-ID | Preconditions | Postconditions |
|-------|-----------|-------------------|---------------|---------------|----------------|

Preconditions and postconditions need to be specific to actual field values or state conditions — "data is valid" doesn't count.

**Invariant table** — give each invariant an INV-ID. At least one has to be numeric or temporal — a specific count, threshold, or duration that a domain expert could verify:

| INV-ID | Invariant Statement | Scope | Numeric/Temporal? | Threshold |
|--------|--------------------|----|---|---|

Before running the trace, state your predictions:

> "I expect Phase [N] to produce the most findings because [structural reason]. I expect [INV-ID] to be most vulnerable because [why]. I expect [OP-ID] to be missing a precondition check because [why]."

Lock these predictions. You'll come back to them.

**Voice A:** "Declaration tables complete. Emitting DECLARATION STAGE: COMPLETE."

---

### Run the trace

Voice A, trace the lifecycle step by step. For each step:

> **Step N — [OP-ID] [Operation Name]**
> Before: [S-ID], fields: …
> Preconditions: (each one specific)
> After: [S-ID], fields: …
> Postconditions: (each one specific)
> Invariants checked: [INV-IDs] → HOLDS or VIOLATION

Include at least one step where an operation is attempted from the wrong state. Show which precondition fails and why the operation is rejected.

**Voice A:** "Trace complete. Emitting TRACE STAGE: COMPLETE."

---

### Phase 1 — Invalid state transitions (Phase 1 STATUS: LOCKED until TRACE STAGE: COMPLETE)

Voice A, run two independent passes through the evidence.

First pass — look at your declaration tables only. Does any operation claim a transition that contradicts the entry conditions of its target state?

Second pass — compare what your tables say against what the trace actually showed. Did any declaration fail to appear in the trace?

Put both passes in a single table so they're independently auditable:

| OP-ID | Voice A — Declaration-Only Finding | Strength (1/2/3) | Voice A — Trace-Diff Finding | Strength (1/2/3) |
|-------|-----------------------------------|-----------------|------------------------------|-----------------|

Assign evidence strength when you first record the finding — not after you've seen all the results. Say it out loud: "I'm giving this a [strength] because [specific evidence]. I'm not revisiting this score."

If either column has "None" in any row, that's where Voice B comes in.

**Voice B activation check**: Did any row get "None" in either column?

If yes — Voice B speaks:

> "Voice B: Acquittal Gap Record P1-[col]. I examined steps [list]. The states in scope were [S-IDs]. The operations in scope were [OP-IDs]. For a declaration-only finding to exist, I would need to see [specific contradiction in the declaration tables]. For a trace-diff finding, I would need to see [specific behavior in the trace that contradicts a declaration]. Neither condition was present because [specific structural reason, not 'everything looks fine']."

Phase 1 gate — before Voice A emits PHASE 1: COMPLETE, check:
- [ ] Both detection columns filled per row
- [ ] No bare "None" — each "None" is a Voice B gap record
- [ ] Evidence strength assigned at discovery
- [ ] At least one numeric/temporal invariant was verified in this phase
- [ ] Op IDs cross-referenced between tables and trace

**Voice A:** "Phase 1 gate cleared. Emitting PHASE 1: COMPLETE."

---

### Phase 2 — Missing precondition checks (Phase 2 STATUS: LOCKED until PHASE 1: COMPLETE)

Voice A, same two passes:

| OP-ID | Voice A — Declaration-Only Finding | Strength | Voice A — Trace-Diff Finding | Strength |
|-------|-----------------------------------|---------|------------------------------|---------|

Declaration-only pass: does any operation in your table lack a precondition, or have one that's vague rather than state-specific?

Trace-diff pass: does the trace show any operation executing without verifying its declared preconditions?

Voice B activates on any "None" column verdict. Same gap record format as Phase 1.

Phase 2 gate:
- [ ] Both columns filled
- [ ] Voice B gap record for any no-finding column
- [ ] Evidence strength at discovery
- [ ] Numeric/temporal invariant checked

**Voice A:** "Phase 2 gate cleared. Emitting PHASE 2: COMPLETE."

---

### Phase 3 — Invariant violations (Phase 3 STATUS: LOCKED until PHASE 2: COMPLETE)

Voice A, run the passes against your invariant table:

| INV-ID | Voice A — Declaration-Only Finding | Strength | Voice A — Trace-Diff Finding | Strength |
|--------|-----------------------------------|---------|------------------------------|---------|

Your numeric/temporal invariants should be focal rows here — they have falsifiable thresholds, so the check is specific.

Voice B activates on any "None" column verdict.

Phase 3 gate:
- [ ] Both columns filled
- [ ] Numeric/temporal invariant was focal
- [ ] Voice B gap record for any no-finding column
- [ ] Evidence strength at discovery

**Voice A:** "Phase 3 gate cleared. Emitting PHASE 3: COMPLETE."

---

### Phase 4 — Race conditions (Phase 4 STATUS: LOCKED until PHASE 3: COMPLETE)

Voice A, construct a concurrent scenario: two operations against the same entity, both initiated before either completes. Walk through the interleaving. Name the vulnerability window.

| Scenario | Voice A — Declaration-Only Finding | Strength | Voice A — Trace-Diff Finding | Strength |
|----------|-----------------------------------|---------|------------------------------|---------|

Voice B activates on any "None" column verdict.

Phase 4 gate:
- [ ] Concurrent scenario constructed and traced
- [ ] Both columns filled
- [ ] Voice B gap record for any no-finding column
- [ ] Evidence strength at discovery

**Voice A:** "Phase 4 gate cleared. Emitting PHASE 4: COMPLETE."

---

### Phase 5 — Undeclared references (Phase 5 STATUS: LOCKED until PHASE 4: COMPLETE)

Voice A, scan the trace. Any S-ID, OP-ID, or INV-ID that appears in a step but doesn't exist in a registry is its own category of anomaly.

| Reference in Trace | Type | In Registry? | Declaration-Only Finding | Trace-Diff Finding |
|-------------------|------|-------------|--------------------------|-------------------|

Voice B activates on any "None" column verdict.

**Voice A:** "Phase 5 gate cleared. Emitting PHASE 5: COMPLETE."

---

### Reconciliation (STATUS: LOCKED until PHASE 5: COMPLETE)

Voice A, consolidate:

| F-ID | Phase | ID Referenced | Anomaly Type | Strength | Any blank cells? |
|------|-------|--------------|--------------|---------|-----------------|

Any blank cell in a finding row is a detectable gap — call it out.

Return to your predictions:

| Prediction | What Actually Happened | C / FP / FN | Structural Diagnosis |
|------------|----------------------|-------------|---------------------|

C = Correct, FP = predicted finding that didn't materialize, FN = finding that appeared unpredicted.

Calibration = C ÷ (C + FP + FN).

If < 0.50 — Voice A diagnoses: "My predictions were based on [surface feature / structural property]. The actual findings came from [structural source]. Next time I would look at [specific structural property] first."

---

## V-05
**Axes**: Output format + Lifecycle emphasis (combo)
**Hypothesis**: A maximally compressed format — where every phase fits on one screen with headers carrying the lock status and exit gate checkboxes integrated as the final row of each sweep table — reduces the surface area for omission because there is no structural gap between the sweep and its gate check; they are the same object.

---

You are conducting a hand-compiled state transition analysis. Domain: Sales / Customer Service / Finance (choose one, hold it). Roles: **A** (Analyst), **B** (Acquittal Advocate — activates on no-finding verdict in any column, produces Gap Record, Gap Record is the unlock artifact).

All output is tabular. Prose only inside table cells. No standalone paragraphs.

---

### BLOCK 1 — DECLARATIONS | STATUS: OPEN

**S-Table**:

| S-ID | Name | Entry Condition | Terminal? |
|------|------|-----------------|-----------|
| S-01 | | | |

**OP-Table**:

| OP-ID | Name | From S-IDs | To S-ID | Preconditions | Postconditions |
|-------|------|-----------|---------|---------------|----------------|
| OP-01 | | | | | |

**INV-Table** (≥1 row: Numeric/Temporal = Yes):

| INV-ID | Statement | Scope | N/T? | Threshold |
|--------|-----------|-------|------|-----------|
| INV-01 | | | | |

**PRED-Table** (locked predictions):

| Target | Prediction | Structural Basis |
|--------|------------|-----------------|
| Most findings phase | | |
| Vulnerable invariant | | |
| Missing precondition op | | |

| Gate | Status |
|------|--------|
| S/OP/INV registries complete with IDs | ☐ |
| ≥1 numeric/temporal invariant declared | ☐ |
| Predictions locked | ☐ |

**DECLARATION STAGE: COMPLETE**

---

### BLOCK 2 — TRACE | STATUS: OPEN (unlocked by DECLARATION STAGE: COMPLETE)

| Step | OP-ID | Before S-ID | Before Fields | Precond. Check | After S-ID | After Fields | Postcond. Check | INV-IDs | Result |
|------|-------|-------------|--------------|----------------|-----------|-------------|-----------------|---------|--------|
| 1 | | | | | | | | | PASS |
| 2 | | | | | | | | | PASS |
| REJ | | | | FAILS: … | — | — | — | — | REJECTED |

(≥3 ops; ≥1 rejection row)

| Gate | Status |
|------|--------|
| ≥3 operations traced | ☐ |
| ≥1 rejection row with failing precondition named | ☐ |
| All INV-IDs from INV-Table checked | ☐ |

**TRACE STAGE: COMPLETE**

---

### BLOCK 3 — PHASE 1: INVALID STATE TRANSITIONS | STATUS: LOCKED → OPEN after TRACE STAGE: COMPLETE

| OP-ID | Decl-Only Finding | Str | Trace-Diff Finding | Str | A-score-aloud |
|-------|------------------|-----|--------------------|-----|---------------|
| OP-01 | | | | | "Str=[N] because [evidence]" |

*"None" in Decl-Only or Trace-Diff = inline Gap Record in that cell: (steps / conditions / evidence-required)*

| Gate | Status |
|------|--------|
| Both columns populated per row | ☐ |
| No bare "None" (each has gap record) | ☐ |
| Score-aloud in every row | ☐ |
| ≥1 finding with Str ≥ 2 | ☐ |
| ≥1 numeric/temporal INV checked | ☐ |
| OP-IDs cross-ref between OP-Table and trace | ☐ |
| B Gap Record produced for any no-finding column | ☐ |

**PHASE 1: COMPLETE**

---

### BLOCK 4 — PHASE 2: MISSING PRECONDITION CHECKS | STATUS: LOCKED → OPEN after PHASE 1: COMPLETE

| OP-ID | Decl-Only Finding | Str | Trace-Diff Finding | Str | A-score-aloud |
|-------|------------------|-----|--------------------|-----|---------------|
| OP-01 | | | | | |

*"None" = inline gap record. B activates on no-finding column verdict.*

| Gate | Status |
|------|--------|
| Both columns per row | ☐ |
| No bare "None" | ☐ |
| Score-aloud per row | ☐ |
| ≥1 numeric/temporal INV checked | ☐ |
| B Gap Record if no-finding | ☐ |

**PHASE 2: COMPLETE**

---

### BLOCK 5 — PHASE 3: INVARIANT VIOLATIONS | STATUS: LOCKED → OPEN after PHASE 2: COMPLETE

| INV-ID | Decl-Only Finding | Str | Trace-Diff Finding | Str | A-score-aloud |
|--------|------------------|-----|--------------------|-----|---------------|
| INV-01 | | | | | |

*Numeric/temporal INV rows must appear. "None" = inline gap record.*

| Gate | Status |
|------|--------|
| Both columns per row | ☐ |
| N/T invariant focal | ☐ |
| No bare "None" | ☐ |
| Score-aloud per row | ☐ |
| B Gap Record if no-finding | ☐ |

**PHASE 3: COMPLETE**

---

### BLOCK 6 — PHASE 4: RACE CONDITIONS | STATUS: LOCKED → OPEN after PHASE 3: COMPLETE

| Scenario (OP-IDs) | Window Description | Decl-Only Finding | Str | Trace-Diff Finding | Str | A-score-aloud |
|-------------------|--------------------|------------------|-----|--------------------|-----|---------------|
| OP-XX ∥ OP-YY | | | | | | |

*Construct ≥1 concurrent scenario. "None" = inline gap record.*

| Gate | Status |
|------|--------|
| ≥1 concurrent scenario traced | ☐ |
| Both columns per row | ☐ |
| No bare "None" | ☐ |
| Score-aloud per row | ☐ |
| B Gap Record if no-finding | ☐ |

**PHASE 4: COMPLETE**

---

### BLOCK 7 — PHASE 5: UNDECLARED REFERENCES | STATUS: LOCKED → OPEN after PHASE 4: COMPLETE

| Ref in Trace | Type | In Registry? | Decl-Only Finding | Trace-Diff Finding |
|-------------|------|-------------|------------------|-------------------|

*Any ref not in its registry = anomaly.*

| Gate | Status |
|------|--------|
| All trace refs scanned against registries | ☐ |
| B Gap Record if no-finding | ☐ |

**PHASE 5: COMPLETE**

---

### BLOCK 8 — RECONCILIATION | STATUS: LOCKED → OPEN after PHASE 5: COMPLETE

**Anomaly Register**:

| F-ID | Phase | Ref-ID | Type | Str | Blank-cell? |
|------|-------|--------|------|-----|-------------|
| F-01 | | | | | |

*Any blank cell in a finding row = flag it.*

**Hypothesis Reconciliation**:

| Prediction | Actual | C/FP/FN | Structural Diagnosis |
|------------|--------|---------|---------------------|
| Most findings: [phase] | | | |
| Vulnerable: [INV-ID] | | | |
| Missing precond: [OP-ID] | | | |

**Calibration** = C ÷ (C + FP + FN) = ___

If < 0.50:

| Failure Mode | Evidence | Fix |
|-------------|----------|-----|
| Predicted on surface feature | | |
| Missed structural property | | |

**RECONCILIATION STAGE: COMPLETE**

---

*End of variation set V-01 through V-05.*
