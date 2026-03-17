# trace-state Skill — Quest Variations Round 13

**Skill**: trace-state
**Round**: 13 (building on R12 V-01 base score; rubric v12, 33 aspirationals)
**Rubric**: v12 (C-01–C-41; aspirationals worth 10/33 = 0.303 pts each)
**R13 target gaps**: C-40 (Gap Record structured field template), C-41 (Phase 3E entity-type-stratified scan)

## Variation Map

| Variation | Axis | Target Gaps | Phase 3E | Gap Record | ID Columns | PART 5 |
|-----------|------|-------------|----------|------------|------------|--------|
| V-01 | Output format | C-40 | Abbreviated | Structured 5-field template (all phases) | 3 separate | No |
| V-02 | Lifecycle emphasis | C-41 | Fully stratified (3 entity-class rows) | Prose | 3 separate | No |
| V-03 | Role sequence | C-40 | Abbreviated | Template declared in PART 0 by Role B before seal | 3 separate | No |
| V-04 | Compound (output + lifecycle) | C-40 + C-41 | Fully stratified (3 rows) | Structured 5-field template | 3 separate | No |
| V-05 | Compound (output + lifecycle + phrasing) | C-40 + C-41 | Fully stratified (3 rows) | Imperative form fields | 3 separate | Yes (C/FP/FN) |

---

## V-01: Output Format — Gap Record Structured Field Template

**Variation axis**: Output format — every Gap Record across all five phases uses a fixed
named-field table template rather than free-form prose. A Gap Record with any required
field blank is a structural failure equivalent to a missing Gap Record, detectable by
inspection rather than judgment.

**Hypothesis**: Free-form Gap Record prose allows the model to satisfy the gate with an
acquittal that omits the evidence standard it applied, omits specific IDs examined, or
omits the "what would constitute a finding" reasoning. Replacing prose with a 5-field
template makes each omission mechanically visible: a blank row in the template table is a
structural gap, not a style choice. Phase-to-phase Gap Record comparability is the
additional benefit — the Examined and What-Would-Constitute fields become auditable
across all five phases without full-text reading.

**Target gaps**: C-40

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or
**Finance**. Choose the domain that best fits the scenario you are given. Your task is to
hand-compile state transitions, identify anomalies, and produce a structured trace-state
report. You play two roles throughout:

- **Role A (Anomaly Finder)**: runs detection passes and records findings
- **Role B (Evidence Steward)**: locks evidence standards before detection begins, then
  produces an unconditional structured Gap Record after each phase regardless of finding count

---

### PART 0: STANDARDS REGISTRY AND GAP RECORD TEMPLATE

**0A: Gap Record Template — declared before Standards Registry is sealed**

Every Gap Record in this analysis must use the following 5-field template table.
A Gap Record that omits any required field is a structural failure equivalent to a missing
Gap Record — it does not unlock the phase exit gate.

```
| Field                          | Content |
|-------------------------------|---------|
| Examined                      | [Specific OP-IDs, S-IDs, INV-IDs, trace steps, or cross-
|                               |  references examined in this phase — list each by ID] |
| Evidence Standard Applied     | [Restate verbatim from PART 0 registry row for this phase] |
| What Was Not Found            | [The specific anomaly types or ID combinations absent;
|                               |  name what was looked for and confirm it was not found] |
| What Would Constitute a Finding | [Minimum evidence that would have triggered a finding:
|                               |  state what trace-step pattern or registry condition would
|                               |  qualify — must be phase-specific, not generic] |
| Verdict                       | Acquitted — no qualifying evidence exists
|                               |   OR
|                               | Partial — finding present but below evidence threshold:
|                               |  [explain which finding(s) and why they did not qualify] |
```

This template is part of the PART 0 pre-game seal. It cannot be revised after PART 0 closes.

**0B: Standards Registry**

Before PART 1 opens, declare the complete evidence standards for all five phases.
This registry is SEALED once declared — standards cannot be revised at any point
during analysis.

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record explains why none qualified |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and the anomalous outcome not present in sequential execution | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch: a state, operation, or invariant referenced in trace or docs but absent from its registry | ≥ 1 | ≥ 1 finding at strength ≥ 1, OR Gap Record explains why |

**PART 0 SEALED (template + standards) → PART 1 now OPEN.**

---

### PART 1: DECLARATIONS

#### 1A: State Registry

Declare every valid state for the entity being traced. Minimum 4 states.

| S-ID | State Name | Entry Condition | Exit Condition |
|------|-----------|----------------|----------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |
| S-04 | | | |

#### 1B: Operation Registry

Declare every operation the entity can receive. Minimum 5 operations.

| OP-ID | Operation Name | Preconditions | Postconditions | Valid From States | Valid To States |
|-------|---------------|--------------|----------------|-----------------|----------------|
| OP-01 | | | | | |
| OP-02 | | | | | |
| OP-03 | | | | | |
| OP-04 | | | | | |
| OP-05 | | | | | |

#### 1C: Invariant Registry

Declare at least 2 invariants. **At least one must be numeric or temporal with a precise
falsifiable threshold** (e.g., "any balance decrease > $0.00 on a closed account is a
violation"). Vague directional invariants do not satisfy this requirement.

| INV-ID | Description | Scope (All / S-ID list) | Type | Falsifiable Threshold |
|--------|-------------|------------------------|------|----------------------|
| INV-01 | | | Numeric / Temporal / Structural | |
| INV-02 | | | | |

---

### PART 2: HAND-COMPILED TRACE

Compile a minimum of 6 numbered steps. **At least one step must be a `[REJECTED]`
negative-path step** where a guard condition fires and the operation is rejected.

**Trace step template:**

```
Step N: [OP-ID] [Operation Name]  [PASS / REJECTED]
  Before state:   [S-ID] [State Name] — { field: value, field: value, ... }
  Preconditions checked:
    - [Precondition text]: MET / NOT MET
    - [Precondition text]: MET / NOT MET
  Guard condition: passes — continue  /  fires — reason: [specific guard text]
  After state:    [S-ID] [State Name] — { field: value, field: value, ... }
    [REJECTED steps: The entity must remain in its before-state after rejection.
     After state MUST equal before state field-for-field. Any deviation is a
     detectable anomaly independent of the rejection reason.]
  Postconditions verified:
    - [Postcondition text]: HOLDS / VIOLATED — [note if violated]
```

Number each step sequentially. Every step must have a before-state and after-state.
REJECTED steps must confirm state immutability explicitly.

---

### PART 3: PRE-SWEEP HYPOTHESIS

Before the anomaly sweep begins, record predictions for each phase. This record is locked
once PART 4 begins — predictions cannot be revised after any detection pass runs.

| Phase | Anomaly Type | Predicted Count | Confidence (L / M / H) | Specific Predicted Scenario |
|-------|-------------|-----------------|------------------------|------------------------------|
| 3A | Invalid state transitions | | | |
| 3B | Missing precondition checks | | | |
| 3C | Invariant violations | | | |
| 3D | Race conditions | | | |
| 3E | Undeclared references | | | |

---

### PART 4: ANOMALY SWEEP

**V-01 ID Contract — applies to all finding tables:**
Every finding table uses three separate ID columns: **OP-ID**, **S-ID**, **INV-ID**.
A blank cell in any of these columns for a found-verdict row is a detectable structural
gap. Populate each column with the relevant ID(s). Use `—` only if the anomaly type
genuinely does not implicate that ID class — and explain why in the finding description.

**V-01 Gap Record Contract — applies to all Gap Records:**
Every Gap Record uses the 5-field template declared in PART 0.0A.
A Gap Record with any required field blank is a structural failure.
The Gap Record is the unlock signal for the phase exit gate — it must be structurally
complete to trigger the unlock.

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — Phase 3A has no prerequisite]**

**Role B (Evidence Steward) — Pre-Detection Commitment**
Restate the PART 0 registry row for Phase 3A **verbatim**:
> Phase 3A evidence standard: _____
> Min strength: _____
> Gate: _____

This commitment is locked. It cannot be adjusted after Pass 1 or Pass 2 begins.

---

**THE SCORING PROTOCOL — active for both passes:**
Assign evidence strength the moment you record a finding. Say aloud:
> "I am scoring this [1/2/3] because [specific trace-step reference or registry entry]."

Self-correction gate: if you cannot complete the sentence with a specific, traceable
reference, the finding is not yet recordable. Revise or discard before proceeding.

---

**Pass 1: Declaration-Only**
Examine the State Registry (1A) and Operation Registry (1B). Look for: operations with
Valid From States that include states where that operation should be blocked; Valid To
States that skip required intermediate states; (S-ID → OP-ID → S-ID) transitions implied
by the registry that contradict documented state semantics.

If no finding in this pass: name the specific (OP-ID, S-ID) pairs you examined and why each cleared.

**Pass 2: Trace-Diff**
Compare each PART 2 step against the Operation Registry. Look for: steps executing from
a state not in the OP's Valid From States; steps transitioning to a state not in Valid To
States; REJECTED steps where the rejection reason contradicts the declared guard.

If no finding in this pass: name the specific steps (Step N, OP-ID, from-S-ID) you examined and why each cleared.

---

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|
| | | | | | | |

*Blank in OP-ID, S-ID, or INV-ID for a found-verdict row = detectable structural gap.*

---

**Role B (Evidence Steward) — Gap Record [UNCONDITIONAL — USE PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3A exit gate.**

---

**Phase 3A Exit Certification**
☐ Findings List gate — all findings recorded with Finding-IDs
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 2, OR Gap Record field "Verdict" explicitly explains why no finding met the threshold
☐ Gap Record gate — Gap Record present AND all 5 template fields populated

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment** (restate 3B registry row verbatim):
> Phase 3B evidence standard: _____  /  Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL** — same as Phase 3A. Score at point of discovery.

**Pass 1: Declaration-Only** — scan Operation Registry (1B) for absent, underdefined, or
overlapping preconditions that could produce a false MET verdict.
If no finding: name specific OP-IDs and precondition cells examined and cleared.

**Pass 2: Trace-Diff** — scan PART 2 steps for: precondition NOT MET but operation PASS;
missing precondition-checked entries; REJECTED guard text referencing different condition
than OP-Registry preconditions.
If no finding: name specific steps and precondition rows examined and cleared.

**Finding Table — Phase 3B**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — USE PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3B exit gate.**

**Phase 3B Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record "Verdict" explains why  ☐ Gap Record gate — all 5 fields populated

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment** (restate 3C registry row verbatim):
> Phase 3C evidence standard: _____  /  Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL** — same as Phase 3A.

**Pass 1: Declaration-Only** — scan Invariant Registry (1C) + Operation Registry (1B) for
postconditions that could breach a declared numeric or temporal threshold; check for
cumulative-transition breaches not visible from any single operation alone.
If no finding: name specific (INV-ID, OP-ID) pairs examined and cleared.

**Pass 2: Trace-Diff** — scan PART 2 after-states against INV thresholds; check adjacent
step pairs where the delta across two after-states crosses a threshold not crossed by
either step alone; check postconditions marked VIOLATED.
If no finding: name specific steps and INV-IDs examined and cleared.

**Finding Table — Phase 3C**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — USE PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3C exit gate.**

**Phase 3C Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record "Verdict" explains why  ☐ Gap Record gate — all 5 fields populated

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment** (restate 3D registry row verbatim):
> Phase 3D evidence standard: _____  /  Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL** — same as Phase 3A.

**Pass 1: Declaration-Only** — identify OP-ID pairs sharing at least one Valid From State;
construct the concurrent interleaving scenario for each pair; describe the anomalous
outcome that concurrent execution produces that sequential execution does not.
If no finding: name the OP-ID pairs constructed and why concurrent execution converges.

**Pass 2: Trace-Diff** — select two steps from PART 2 that execute from the same or
overlapping states, or that modify the same field; construct the concurrent interleaving;
compare concurrent after-state to both sequential orderings.
If no finding: name the step pairs constructed and the after-state comparison result.

**Finding Table — Phase 3D**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — USE PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3D exit gate.**

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record "Verdict" explains why  ☐ Gap Record gate — all 5 fields populated

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

Phase 3E is a full structural peer of Phases 3A–3D. Apply the complete phase mechanics:
Role B pre-detection commitment (restate PART 0 registry row for 3E verbatim) →
THE SCORING PROTOCOL → Pass 1 (Declaration-Only: scan registries 1A/1B/1C for internal
cross-reference gaps) → Pass 2 (Trace-Diff: scan PART 2 steps and prior finding tables
for any S-ID, OP-ID, or INV-ID that does not resolve to a registry entry) →
Finding table (3 separate ID columns per V-01 contract) →
Role B Gap Record [UNCONDITIONAL — 5-field template] → Phase 3E Exit Certification.

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-01 prompt body.*

---
---

## V-02: Lifecycle Emphasis — Phase 3E Entity-Type-Stratified Scan

**Variation axis**: Lifecycle emphasis — Phase 3E runs a stratified scan that issues
distinct Pass 1 scanning instructions per reference entity class (S-ID, OP-ID, INV-ID).
Each entity class receives its own sweep row in the Phase 3E finding table with
Declaration-Only and Trace-Diff columns. A verdict on one entity class row cannot satisfy
the sweep requirement for another entity class row.

**Hypothesis**: In R12, Phase 3E's finding table had a single row for "undeclared
references." A model that detects one undeclared S-ID reference can declare Phase 3E
complete while having conducted zero OP-ID or INV-ID scanning. Stratified rows make
entity-class-specific gaps detectable by row inspection: a blank OP-ID row is visible
without reading the phase narrative. The coverage gap is structural, not prose-level.

**Target gaps**: C-41

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or
**Finance**. Choose the domain that best fits the scenario you are given. Your task is to
hand-compile state transitions, identify anomalies, and produce a structured trace-state
report. You play two roles throughout:

- **Role A (Anomaly Finder)**: runs detection passes and records findings
- **Role B (Evidence Steward)**: locks evidence standards before detection begins, then
  produces an unconditional Gap Record after each phase

---

### PART 0: STANDARDS REGISTRY

Before PART 1 opens, declare the complete evidence standards for all five phases.
SEALED once declared — standards cannot be revised at any point during analysis.

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record explains why none qualified |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and the anomalous outcome not present in sequential execution | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch: a state, operation, or invariant referenced in trace or docs but absent from its registry | ≥ 1 | ≥ 1 finding at strength ≥ 1 in ANY entity class, OR Gap Record for that class explains why |

**STANDARDS REGISTRY: SEALED → PART 1 now OPEN.**

---

### PART 1: DECLARATIONS

#### 1A: State Registry (minimum 4 states)

| S-ID | State Name | Entry Condition | Exit Condition |
|------|-----------|----------------|----------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |
| S-04 | | | |

#### 1B: Operation Registry (minimum 5 operations)

| OP-ID | Operation Name | Preconditions | Postconditions | Valid From States | Valid To States |
|-------|---------------|--------------|----------------|-----------------|----------------|
| OP-01 | | | | | |
| OP-02 | | | | | |
| OP-03 | | | | | |
| OP-04 | | | | | |
| OP-05 | | | | | |

#### 1C: Invariant Registry (minimum 2; at least one numeric or temporal with threshold)

| INV-ID | Description | Scope (All / S-ID list) | Type | Falsifiable Threshold |
|--------|-------------|------------------------|------|----------------------|
| INV-01 | | | Numeric / Temporal / Structural | |
| INV-02 | | | | |

---

### PART 2: HAND-COMPILED TRACE

Minimum 6 numbered steps. At least one `[REJECTED]` negative-path step required.

```
Step N: [OP-ID] [Operation Name]  [PASS / REJECTED]
  Before state:   [S-ID] [State Name] — { field: value, ... }
  Preconditions checked:
    - [text]: MET / NOT MET
  Guard condition: passes — continue  /  fires — reason: [text]
  After state:    [S-ID] [State Name] — { field: value, ... }
    [REJECTED: The entity must remain in its before-state after rejection.
     After state MUST equal before state field-for-field. Any deviation is a
     detectable anomaly independent of the rejection reason.]
  Postconditions verified:
    - [text]: HOLDS / VIOLATED
```

---

### PART 3: PRE-SWEEP HYPOTHESIS

Record predictions before PART 4 begins. Locked once any detection pass runs.

| Phase | Anomaly Type | Predicted Count | Confidence (L/M/H) | Specific Predicted Scenario |
|-------|-------------|-----------------|--------------------|-----------------------------|
| 3A | Invalid state transitions | | | |
| 3B | Missing precondition checks | | | |
| 3C | Invariant violations | | | |
| 3D | Race conditions | | | |
| 3E | Undeclared references | | | |

---

### PART 4: ANOMALY SWEEP

**V-02 ID Contract:** Finding tables for Phases 3A–3D use three separate ID columns
(OP-ID, S-ID, INV-ID). Phase 3E uses the stratified entity-class row structure defined
in its expanded template below.

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B — Pre-Detection Commitment** (restate 3A registry row verbatim):
> Phase 3A evidence standard: _____  /  Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL:** Score at discovery. Say: "I am scoring this [1/2/3] because
[specific reference]." Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions.
If no finding: name specific (OP-ID, S-ID) pairs cleared.

**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps.
If no finding: name specific steps and state-IDs cleared.

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]**
> Gap Record 3A: _____
> Specific entries examined and cleared: _____
> Why absence of additional findings is credible: _____

**The Gap Record is the unlock signal for the Phase 3A exit gate.**

**Phase 3A Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record explains why  ☐ Gap Record gate

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment** (restate 3B registry row verbatim): _____
**THE SCORING PROTOCOL** — same as 3A.
**Pass 1: Declaration-Only** — scan OP-Registry for absent/underdefined preconditions. If no finding: name OP-IDs cleared.
**Pass 2: Trace-Diff** — scan steps for NOT MET → PASS or missing precondition entries. If no finding: name steps cleared.

**Finding Table — Phase 3B**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]** > Gap Record 3B: _____
The Gap Record is the unlock signal for the Phase 3B exit gate.

**Phase 3B Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment** (restate 3C registry row verbatim): _____
**THE SCORING PROTOCOL** — same as 3A.
**Pass 1: Declaration-Only** — scan INV + OP for postconditions breaching thresholds. If no finding: name (INV-ID, OP-ID) pairs cleared.
**Pass 2: Trace-Diff** — scan after-states and adjacent pairs for cumulative breaches. If no finding: name steps and INV-IDs cleared.

**Finding Table — Phase 3C**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]** > Gap Record 3C: _____
The Gap Record is the unlock signal for the Phase 3C exit gate.

**Phase 3C Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment** (restate 3D registry row verbatim): _____
**THE SCORING PROTOCOL** — same as 3A.
**Pass 1: Declaration-Only** — identify OP-ID pairs sharing Valid From States; construct concurrent scenario; describe anomalous outcome vs sequential. If no finding: name OP-ID pairs and convergence rationale.
**Pass 2: Trace-Diff** — select overlapping-state step pairs; construct interleaving; compare concurrent vs sequential after-state. If no finding: name step pairs and comparison result.

**Finding Table — Phase 3D**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]** > Gap Record 3D: _____
The Gap Record is the unlock signal for the Phase 3D exit gate.

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References — Entity-Type-Stratified Scan

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

**V-02 expansion**: Phase 3E runs a stratified scan with three independent entity-class
sub-scans. Each entity class has its own sweep row in the finding table. A verdict in one
entity class row does NOT satisfy the sweep requirement for any other entity class row.
A model that finds one S-ID undeclared reference cannot declare the OP-ID and INV-ID
rows satisfied — each must be independently populated.

**Role B (Evidence Steward) — Pre-Detection Commitment**
Restate the PART 0 registry row for Phase 3E **verbatim**:
> Phase 3E evidence standard: _____
> Min strength: _____
> Gate: _____

This commitment is locked. It cannot be adjusted after any Pass begins.

---

**THE SCORING PROTOCOL — active for both passes:**
Assign evidence strength the moment you record a finding. Say aloud:
> "I am scoring this [1/2/3] because [specific cross-reference: registry entry X
> references ID Y, but Y does not appear in registry Z at row N]."

Self-correction gate: if you cannot identify the specific registry entry and the
specific missing target, the finding is not yet recordable.

---

**Pass 1: Declaration-Only — Entity-Type-Stratified**

This pass runs three independent sub-scans. Execute each in order. Do not combine.

**Sub-scan P1-S: S-ID References**
Examine: Operation Registry 1B columns `Valid From States` and `Valid To States`.
Examine: Invariant Registry 1C column `Scope` (if it references specific state IDs).
Question: Does every S-ID cited in 1B or 1C appear as a declared row in the State
Registry 1A?
If no finding: list each cell checked (e.g., "OP-01 Valid From States: S-01, S-02 —
both confirmed in 1A") and confirm each S-ID resolves to a declared state.

**Sub-scan P1-O: OP-ID References**
Examine: Invariant Registry 1C descriptions or threshold fields for any OP-ID reference.
Examine: Operation Registry 1B preconditions or postconditions for cross-operation
OP-ID references.
Question: Does every OP-ID cited in 1C or in 1B cross-references appear as a declared
row in the Operation Registry 1B?
If no finding: list each cell checked and confirm each OP-ID resolves to a declared
operation.

**Sub-scan P1-I: INV-ID References**
Examine: Operation Registry 1B preconditions and postconditions for any INV-ID reference.
Examine: State Registry 1A entry or exit conditions for any INV-ID reference.
Question: Does every INV-ID cited in 1B or 1A appear as a declared row in the Invariant
Registry 1C?
If no finding: list each cell checked and confirm each INV-ID resolves to a declared
invariant.

---

**Pass 2: Trace-Diff — Entity-Type-Stratified**

This pass also runs three independent sub-scans.

**Sub-scan P2-S: S-ID References in Trace and Prior Findings**
Scan every Before/After state field in PART 2 trace steps. Scan S-ID cells in Phases
3A–3D finding tables. Does every S-ID referenced resolve to a declared row in 1A?
If no finding: list each trace step checked and confirm S-ID resolution.

**Sub-scan P2-O: OP-ID References in Trace and Prior Findings**
Scan every Step header OP-ID in PART 2 trace steps. Scan OP-ID cells in Phases 3A–3D
finding tables. Does every OP-ID referenced resolve to a declared row in 1B?
If no finding: list each trace step and finding table row checked.

**Sub-scan P2-I: INV-ID References in Trace and Prior Findings**
Scan every Postcondition "VIOLATED" note in PART 2 for INV-ID references. Scan INV-ID
cells in Phases 3A–3D finding tables. Does every INV-ID referenced resolve to a
declared row in 1C?
If no finding: list each trace step and finding table row checked.

---

**Finding Table — Phase 3E**

Each row is an independent sweep unit. A "None" verdict in any cell requires an inline
explanation of what was checked. A verdict on one row does NOT satisfy another row.

| Entity Class | Declaration-Only Finding (Pass P1) | Trace-Diff Finding (Pass P2) | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|-------------|-------------------------------------|------------------------------|-------|------|--------|--------------------------|
| S-ID references | | | — | | — | |
| OP-ID references | | | | — | — | |
| INV-ID references | | | — | — | | |

*Blank verdict in any row = incomplete Phase 3E sweep.*
*Finding in one row does not satisfy another row's sweep requirement.*

---

**Role B (Evidence Steward) — Gap Record [UNCONDITIONAL]**

> Gap Record 3E: _____
> Entity classes scanned: S-ID, OP-ID, INV-ID (all three)
> Registries checked (Pass 1): 1A (___ states), 1B (___ operations), 1C (___ invariants)
> Trace steps audited (Pass 2): Steps 1–N
> Prior finding tables scanned: Phases 3A–3D finding tables
> Specific cross-references confirmed present per entity class:
>   S-ID: _____  /  OP-ID: _____  /  INV-ID: _____
> Why absence of additional findings per entity class is credible: _____

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

---

**Phase 3E Exit Certification**
☐ Findings List gate — all three entity-class rows populated with verdicts
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1 in any entity class row, OR Gap Record explains why no row produced a qualifying finding
☐ Gap Record gate — Gap Record present and covers all three entity classes

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-02 prompt body.*

---
---

## V-03: Role Sequence — Role B Declares Gap Record Template in PART 0 Pre-Game

**Variation axis**: Role sequence — Role B's pre-game responsibilities are expanded.
Before sealing the evidence standards, Role B formally declares the Gap Record template
that will govern all five phases. The template declaration and the standards registry are
sealed together in a single PART 0 seal. At each phase, Role B's pre-detection commitment
now includes confirming that the phase's Gap Record will use the PART 0-declared template.

**Hypothesis**: C-35's per-phase pre-detection commitment anchors Role B's evidence
standard in the phase header. C-38's PART 0 seal elevates that commitment to a global
pre-game constraint. Neither criterion specifies that the *form* of the Gap Record is
itself a pre-game commitment. Requiring Role B to declare the Gap Record template in
PART 0 — before any standards are set, before any data is seen — achieves C-40's
machine-comparable Gap Record requirement via the role-sequence mechanism rather than
the output-format mechanism: the template is locked by the same seal that locks the
evidence standards.

**Target gaps**: C-40

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or
**Finance**. Choose the domain that best fits the scenario you are given. Your task is to
hand-compile state transitions, identify anomalies, and produce a structured trace-state
report. You play two roles throughout:

- **Role A (Anomaly Finder)**: runs detection passes and records findings
- **Role B (Evidence Steward)**: in PART 0, declares the Gap Record template AND seals the
  evidence standards before any analysis begins; at each phase, confirms template
  compliance in the pre-detection commitment block; produces an unconditional structured
  Gap Record after each phase

---

### PART 0: PRE-GAME SEAL

Role B executes PART 0 in full before PART 1 opens. Both sub-sections are sealed together.

**0A: Role B — Gap Record Template Declaration**

Role B declares the Gap Record template that will be used for all five phases.
This template cannot be revised after PART 0 is sealed.

```
GAP RECORD TEMPLATE (declared by Role B, pre-game):

| Field                          | Instruction |
|-------------------------------|-------------|
| Examined                      | List each OP-ID, S-ID, INV-ID, trace step reference,
|                               | or cross-reference cell examined in this phase.
|                               | "All entries" is not acceptable — name each one. |
| Evidence Standard Applied     | Copy verbatim from the PART 0 Standards Registry row
|                               | for this phase. Do not paraphrase. |
| What Was Not Found            | For each absence: name the specific anomaly type and
|                               | the specific IDs or patterns that were not present.
|                               | "No violations found" is not acceptable. |
| What Would Constitute a Finding | Describe the minimum evidence that would trigger a
|                               | finding in this phase — what trace-step pattern or
|                               | registry condition would qualify. Must be phase-specific. |
| Verdict                       | Choose one:
|                               |   Acquitted — no qualifying evidence exists
|                               |   Partial — finding exists below threshold: [specify
|                               |   which finding(s) and why they did not meet the standard] |
```

**Role B declaration**: I confirm this template governs all Gap Records in this analysis.
A Gap Record with any required field blank or left as placeholder text is a structural
failure. It does not unlock the phase exit gate regardless of its prose content.

**0B: Standards Registry**

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record "Verdict" explains why none qualified |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and the anomalous outcome not present in sequential execution | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch: a state, operation, or invariant referenced in trace or docs but absent from its registry | ≥ 1 | ≥ 1 finding at strength ≥ 1, OR Gap Record explains why |

**PART 0 SEALED (template 0A + standards 0B) → PART 1 now OPEN.**

---

### PART 1: DECLARATIONS

#### 1A: State Registry (minimum 4 states)

| S-ID | State Name | Entry Condition | Exit Condition |
|------|-----------|----------------|----------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |
| S-04 | | | |

#### 1B: Operation Registry (minimum 5 operations)

| OP-ID | Operation Name | Preconditions | Postconditions | Valid From States | Valid To States |
|-------|---------------|--------------|----------------|-----------------|----------------|
| OP-01 | | | | | |
| OP-02 | | | | | |
| OP-03 | | | | | |
| OP-04 | | | | | |
| OP-05 | | | | | |

#### 1C: Invariant Registry (minimum 2; at least one numeric or temporal)

| INV-ID | Description | Scope (All / S-ID list) | Type | Falsifiable Threshold |
|--------|-------------|------------------------|------|----------------------|
| INV-01 | | | Numeric / Temporal / Structural | |
| INV-02 | | | | |

---

### PART 2: HAND-COMPILED TRACE

Minimum 6 numbered steps. At least one `[REJECTED]` negative-path step required.

```
Step N: [OP-ID] [Operation Name]  [PASS / REJECTED]
  Before state:   [S-ID] [State Name] — { field: value, ... }
  Preconditions checked:
    - [text]: MET / NOT MET
  Guard condition: passes — continue  /  fires — reason: [text]
  After state:    [S-ID] [State Name] — { field: value, ... }
    [REJECTED: The entity must remain in its before-state after rejection.
     After state MUST equal before state field-for-field. Any deviation is a
     detectable anomaly independent of the rejection reason.]
  Postconditions verified:
    - [text]: HOLDS / VIOLATED
```

---

### PART 3: PRE-SWEEP HYPOTHESIS

Record predictions before PART 4 begins. Locked once any detection pass runs.

| Phase | Anomaly Type | Predicted Count | Confidence (L/M/H) | Specific Predicted Scenario |
|-------|-------------|-----------------|--------------------|-----------------------------|
| 3A | | | | |
| 3B | | | | |
| 3C | | | | |
| 3D | | | | |
| 3E | | | | |

---

### PART 4: ANOMALY SWEEP

**V-03 ID Contract:** Three separate ID columns (OP-ID, S-ID, INV-ID) in all finding tables.

**V-03 Role B pre-detection commitment — expanded format:**
At each phase, Role B's commitment block now has TWO lines:
- Line 1: restate the PART 0 standards row verbatim (as in prior rounds)
- Line 2: "I confirm: the Gap Record for this phase will use the PART 0.0A template.
  A Gap Record with any blank field does not unlock this phase's exit gate."

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim from PART 0.0B): Phase 3A evidence standard: _____  /  Min: _____  /  Gate: _____
> Template confirmation: I confirm the Phase 3A Gap Record will use the PART 0.0A template. A blank field does not unlock the exit gate.

**THE SCORING PROTOCOL:** Score at discovery. "I am scoring this [1/2/3] because [specific reference]." Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions.
If no finding: name specific (OP-ID, S-ID) pairs examined and cleared.

**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps.
If no finding: name specific steps and state-IDs examined and cleared.

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE REQUIRED]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3A exit gate.**

**Phase 3A Exit Certification**
☐ Findings List gate
☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record "Verdict" explains why
☐ Gap Record gate — all 5 fields of PART 0.0A template populated

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim): Phase 3B: _____  /  Min: _____  /  Gate: _____
> Template confirmation: I confirm the Phase 3B Gap Record will use the PART 0.0A template.

**THE SCORING PROTOCOL** — same as 3A.
**Pass 1: Declaration-Only** — scan OP-Registry for absent/underdefined preconditions. If no finding: name OP-IDs cleared.
**Pass 2: Trace-Diff** — scan steps for NOT MET → PASS or missing entries. If no finding: name steps cleared.

**Finding Table — Phase 3B**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE REQUIRED]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3B exit gate.**

**Phase 3B Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 template fields populated

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim): Phase 3C: _____  /  Min: _____  /  Gate: _____
> Template confirmation: I confirm the Phase 3C Gap Record will use the PART 0.0A template.

**THE SCORING PROTOCOL** — same as 3A.
**Pass 1: Declaration-Only** — scan INV + OP for postconditions breaching thresholds. If no finding: name (INV-ID, OP-ID) pairs cleared.
**Pass 2: Trace-Diff** — scan after-states and adjacent pairs for cumulative breaches. If no finding: name steps and INV-IDs cleared.

**Finding Table — Phase 3C**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE REQUIRED]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3C exit gate.**

**Phase 3C Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 template fields populated

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim): Phase 3D: _____  /  Min: _____  /  Gate: _____
> Template confirmation: I confirm the Phase 3D Gap Record will use the PART 0.0A template.

**THE SCORING PROTOCOL** — same as 3A.
**Pass 1: Declaration-Only** — identify OP-ID pairs sharing Valid From States; construct concurrent scenario; describe anomalous outcome vs sequential. If no finding: name OP-ID pairs and convergence rationale.
**Pass 2: Trace-Diff** — construct step-pair interleaving; compare concurrent vs sequential after-state. If no finding: name step pairs and comparison result.

**Finding Table — Phase 3D**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE REQUIRED]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3D exit gate.**

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 template fields populated

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim): Phase 3E: _____  /  Min: _____  /  Gate: _____
> Template confirmation: I confirm the Phase 3E Gap Record will use the PART 0.0A template.
>   The Examined field must cover all three entity classes (S-ID, OP-ID, INV-ID).

Apply the complete Phase 3E mechanics: THE SCORING PROTOCOL → Pass 1 (Declaration-Only:
scan registries 1A/1B/1C for internal cross-reference gaps, by entity class) →
Pass 2 (Trace-Diff: scan PART 2 steps and Phases 3A–3D finding tables for any ID
that does not resolve to its registry) → Finding table (3 separate ID columns) →
Role B Gap Record (5-field PART 0.0A template) → Phase 3E Exit Certification.

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-03 prompt body.*

---
---

## V-04: Compound — Structured Gap Record Template + Phase 3E Entity-Type-Stratified Scan

**Variation axis**: Compound — output format + lifecycle emphasis. Combines V-01's
structured 5-field Gap Record template with V-02's Phase 3E entity-type-stratified scan.

**Hypothesis**: C-40 and C-41 are independent structural requirements — one governs the
internal structure of Gap Records (all phases), the other governs the internal structure
of the Phase 3E finding table (one phase). Neither implies the other. A variation that
addresses only one will remain PARTIAL on the other. The compound variation closes both
simultaneously, using output-format enforcement for Gap Records and lifecycle enforcement
for Phase 3E.

**Target gaps**: C-40 + C-41

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or
**Finance**. Choose the domain that best fits the scenario you are given. Your task is to
hand-compile state transitions, identify anomalies, and produce a structured trace-state
report. You play two roles throughout:

- **Role A (Anomaly Finder)**: runs detection passes and records findings
- **Role B (Evidence Steward)**: locks evidence standards and Gap Record template before
  detection begins, then produces an unconditional structured Gap Record after each phase

---

### PART 0: STANDARDS REGISTRY AND GAP RECORD TEMPLATE

**0A: Gap Record Template**

Every Gap Record in this analysis uses the following 5-field template. A Gap Record
missing any field is a structural failure and does not unlock the phase exit gate.

```
| Field                          | Content |
|-------------------------------|---------|
| Examined                      | [Specific IDs, trace steps, or registry cells checked — named individually] |
| Evidence Standard Applied     | [Verbatim restatement from PART 0.0B registry row for this phase] |
| What Was Not Found            | [Specific absence: anomaly type + IDs that did not trigger, by name] |
| What Would Constitute a Finding | [Phase-specific minimum evidence that would qualify as a finding] |
| Verdict                       | Acquitted / Partial — [specify if partial, which finding and why it did not qualify] |
```

**0B: Standards Registry**

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record "Verdict" explains why |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and anomalous outcome not present sequentially | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch per entity class (S-ID, OP-ID, or INV-ID) absent from its registry | ≥ 1 | ≥ 1 finding at strength ≥ 1 in any entity class, OR Gap Record covers all three entity classes |

**PART 0 SEALED (0A template + 0B standards) → PART 1 now OPEN.**

---

### PART 1: DECLARATIONS

#### 1A: State Registry (minimum 4 states)

| S-ID | State Name | Entry Condition | Exit Condition |
|------|-----------|----------------|----------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |
| S-04 | | | |

#### 1B: Operation Registry (minimum 5 operations)

| OP-ID | Operation Name | Preconditions | Postconditions | Valid From States | Valid To States |
|-------|---------------|--------------|----------------|-----------------|----------------|
| OP-01 | | | | | |
| OP-02 | | | | | |
| OP-03 | | | | | |
| OP-04 | | | | | |
| OP-05 | | | | | |

#### 1C: Invariant Registry (minimum 2; at least one numeric or temporal)

| INV-ID | Description | Scope (All / S-ID list) | Type | Falsifiable Threshold |
|--------|-------------|------------------------|------|----------------------|
| INV-01 | | | Numeric / Temporal / Structural | |
| INV-02 | | | | |

---

### PART 2: HAND-COMPILED TRACE

Minimum 6 numbered steps. At least one `[REJECTED]` negative-path step required.

```
Step N: [OP-ID] [Operation Name]  [PASS / REJECTED]
  Before state:   [S-ID] [State Name] — { field: value, ... }
  Preconditions checked:
    - [text]: MET / NOT MET
  Guard condition: passes — continue  /  fires — reason: [text]
  After state:    [S-ID] [State Name] — { field: value, ... }
    [REJECTED: The entity must remain in its before-state after rejection.
     After state MUST equal before state field-for-field. Any deviation is a
     detectable anomaly independent of the rejection reason.]
  Postconditions verified:
    - [text]: HOLDS / VIOLATED
```

---

### PART 3: PRE-SWEEP HYPOTHESIS

Record predictions before PART 4 begins. Locked once any detection pass runs.

| Phase | Anomaly Type | Predicted Count | Confidence (L/M/H) | Specific Predicted Scenario |
|-------|-------------|-----------------|--------------------|-----------------------------|
| 3A | Invalid state transitions | | | |
| 3B | Missing precondition checks | | | |
| 3C | Invariant violations | | | |
| 3D | Race conditions | | | |
| 3E | Undeclared references | | | |

---

### PART 4: ANOMALY SWEEP

**V-04 ID Contract:** All finding tables for Phases 3A–3D use three separate ID columns
(OP-ID, S-ID, INV-ID). Phase 3E uses the stratified entity-class row structure.

**V-04 Gap Record Contract:** All Gap Records use the PART 0.0A 5-field template.
A Gap Record with any field blank or as placeholder text is a structural failure.
The Gap Record is the unlock signal for the phase exit gate — structural completeness
is required to trigger the unlock.

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B — Pre-Detection Commitment**
> Phase 3A evidence standard (verbatim from PART 0.0B): _____
> Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL:** Score at discovery. "I am scoring this [1/2/3] because [specific reference]." Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions.
If no finding: name specific (OP-ID, S-ID) pairs examined and cleared.

**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps.
If no finding: name specific steps and state-IDs examined and cleared.

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3A exit gate.**

**Phase 3A Exit Certification**
☐ Findings List gate
☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record "Verdict" explains why
☐ Gap Record gate — all 5 template fields populated

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim from PART 0.0B):
> Phase 3B: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL** — same as 3A.
**Pass 1: Declaration-Only** — scan OP-Registry for absent/underdefined preconditions. If no finding: name OP-IDs cleared.
**Pass 2: Trace-Diff** — scan steps for NOT MET → PASS or missing entries. If no finding: name steps cleared.

**Finding Table — Phase 3B**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3B exit gate.**

**Phase 3B Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields populated

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim from PART 0.0B):
> Phase 3C: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL** — same as 3A.
**Pass 1: Declaration-Only** — scan INV + OP for postconditions breaching thresholds. If no finding: name (INV-ID, OP-ID) pairs cleared.
**Pass 2: Trace-Diff** — scan after-states and adjacent pairs for cumulative breaches. If no finding: name steps and INV-IDs cleared.

**Finding Table — Phase 3C**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3C exit gate.**

**Phase 3C Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields populated

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim from PART 0.0B):
> Phase 3D: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL** — same as 3A.
**Pass 1: Declaration-Only** — identify OP-ID pairs sharing Valid From States; construct concurrent scenario; describe anomalous outcome vs sequential. If no finding: name OP-ID pairs and convergence rationale.
**Pass 2: Trace-Diff** — construct step-pair interleaving; compare concurrent vs sequential after-state. If no finding: name step pairs and comparison result.

**Finding Table — Phase 3D**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3D exit gate.**

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields populated

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References — Entity-Type-Stratified + Structured Gap Record

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim from PART 0.0B):
> Phase 3E: _____  /  Min: _____  /  Gate: _____

---

**THE SCORING PROTOCOL — active for both passes:**
Score at discovery. "I am scoring this [1/2/3] because [registry entry X references
ID Y, but Y is absent from registry Z]." Incomplete sentence = not recordable.

---

**Pass 1: Declaration-Only — Three Independent Sub-Scans**

**Sub-scan P1-S: S-ID References**
Examine 1B Valid From/To States and 1C Scope fields. Does every S-ID cited appear in 1A?
If no finding: list each cell checked and confirm S-ID resolution.

**Sub-scan P1-O: OP-ID References**
Examine 1C descriptions/thresholds and 1B cross-operation references. Does every OP-ID cited appear in 1B?
If no finding: list each cell checked and confirm OP-ID resolution.

**Sub-scan P1-I: INV-ID References**
Examine 1B preconditions/postconditions and 1A entry/exit conditions. Does every INV-ID cited appear in 1C?
If no finding: list each cell checked and confirm INV-ID resolution.

---

**Pass 2: Trace-Diff — Three Independent Sub-Scans**

**Sub-scan P2-S:** Scan PART 2 step Before/After states and Phases 3A–3D S-ID cells.
Does every S-ID resolve to a 1A row? If no finding: list steps and S-IDs checked.

**Sub-scan P2-O:** Scan PART 2 step headers (OP-IDs) and Phases 3A–3D OP-ID cells.
Does every OP-ID resolve to a 1B row? If no finding: list steps and OP-IDs checked.

**Sub-scan P2-I:** Scan PART 2 postcondition VIOLATED notes and Phases 3A–3D INV-ID cells.
Does every INV-ID resolve to a 1C row? If no finding: list entries and INV-IDs checked.

---

**Finding Table — Phase 3E**

Each row is an independent sweep unit. A verdict in one row does NOT satisfy another row.

| Entity Class | Declaration-Only Finding (P1 sub-scan) | Trace-Diff Finding (P2 sub-scan) | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|-------------|----------------------------------------|----------------------------------|-------|------|--------|--------------------------|
| S-ID references | | | — | | — | |
| OP-ID references | | | | — | — | |
| INV-ID references | | | — | — | | |

*A "None" in any cell requires an inline statement of what was checked and confirmed absent.*
*A finding in one row does not satisfy another row's sweep requirement.*

---

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

The Examined field must cover all three entity classes separately.

| Field | Content |
|-------|---------|
| Examined | [S-ID class: cells checked / OP-ID class: cells checked / INV-ID class: cells checked] |
| Evidence Standard Applied | |
| What Was Not Found | [Per entity class: S-ID — ___  / OP-ID — ___  / INV-ID — ___] |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

---

**Phase 3E Exit Certification**
☐ Findings List gate — all three entity-class rows populated with verdicts
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1, OR Gap Record "Verdict" covers all three entity classes
☐ Gap Record gate — all 5 template fields populated; Examined field covers all three entity classes

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-04 prompt body.*

---
---

## V-05: Compound — Structured Gap Record + Stratified Phase 3E + Imperative Phrasing + PART 5

**Variation axis**: Compound — output format + lifecycle emphasis + phrasing register.
Gap Record 5-field template (C-40) + Phase 3E stratified scan (C-41) + imperative command
phrasing with STOP/COMPLETE/ADVANCE markers + PART 5 post-sweep C/FP/FN reconciliation
(C-21, C-25).

**Hypothesis**: The phrasing register interacts with the structured template: imperative
STOP-COMPLETE-ADVANCE markers at each Gap Record section force the model to pause and
fill the form fields rather than skipping through them as boilerplate. The inertia framing
— each Gap Record's "What Was Not Found" field asks what a documentation reader would
have concluded vs what the state trace actually shows — grounds the absence record in
the domain context rather than producing generic acquittals. PART 5 reconciliation closes
the C-21 and C-25 criteria simultaneously.

**Target gaps**: C-40 + C-41 (primary); C-21 + C-25 (secondary via PART 5)

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or
**Finance**. Choose the domain that best fits the scenario you are given. Your task is to
hand-compile state transitions, identify anomalies, and produce a structured trace-state
report. You play two roles:

- **Role A (Anomaly Finder)**: runs detection passes, records findings, and executes
  the post-sweep reconciliation in PART 5
- **Role B (Evidence Steward)**: declares the Gap Record template and evidence standards
  before detection begins; produces an unconditional structured Gap Record after each phase

---

### PART 0: STANDARDS REGISTRY AND GAP RECORD TEMPLATE

**STOP. Role B completes PART 0 in full before any other part opens.**

**0A: Gap Record Template Declaration**

The following template governs every Gap Record in this analysis. Role B declares it
before seeing any entity data. It is locked when PART 0 is sealed.

A Gap Record with any required field blank, left as placeholder text, or filled with
"N/A" without explanation is a structural failure. It does not unlock the phase exit gate.

```
GAP RECORD FORM — complete every field:

Examined:
  [LIST by ID every OP-ID, S-ID, INV-ID, trace step, or registry cell you examined
   in this phase. Do not write "all entries." Name each one individually.
   Minimum: all IDs declared in the relevant registries for this phase's anomaly type.]

Evidence Standard Applied:
  [COPY VERBATIM from PART 0.0B registry row for this phase. Do not paraphrase.
   The verbatim copy makes the Gap Record auditable against the pre-game seal.]

What Was Not Found:
  [NAME the specific anomaly types or ID combinations that were absent.
   Contrast with what a documentation reader would have concluded:
   "A reader of the operation registry would expect X; the trace reveals Y was absent."
   Generic "no violations found" does not pass.]

What Would Constitute a Finding:
  [DESCRIBE the minimum evidence that would trigger a finding in this phase.
   Must be phase-specific and reference at least one ID from the declarations.
   Example: "A finding would require a PART 2 step executing from a state not listed
   in the OP's Valid From States, e.g., OP-03 executing from S-04."]

Verdict:
  [Choose EXACTLY ONE:
   Acquitted — no qualifying evidence exists. [Summarize the clearing evidence in
   one sentence referencing the Examined entries above.]
   Partial — finding exists but below evidence threshold: [name the finding,
   state which evidence standard criterion it fails, and explain why.]]
```

**0B: Standards Registry**

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record "Verdict" explains why none qualified |
| 3B | Missing precondition checks | Trace-step evidence showing precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and anomalous outcome not in sequential execution | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch per entity class absent from registry | ≥ 1 | ≥ 1 finding per any entity class, OR Gap Record covers all three entity classes |

**PART 0 SEALED. ADVANCE TO PART 1.**

---

### PART 1: DECLARATIONS

**STOP. Complete all three registries in full before advancing to PART 2.**

#### 1A: State Registry (minimum 4 states)

| S-ID | State Name | Entry Condition | Exit Condition |
|------|-----------|----------------|----------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |
| S-04 | | | |

#### 1B: Operation Registry (minimum 5 operations)

| OP-ID | Operation Name | Preconditions | Postconditions | Valid From States | Valid To States |
|-------|---------------|--------------|----------------|-----------------|----------------|
| OP-01 | | | | | |
| OP-02 | | | | | |
| OP-03 | | | | | |
| OP-04 | | | | | |
| OP-05 | | | | | |

#### 1C: Invariant Registry (minimum 2; at least one numeric or temporal with threshold)

| INV-ID | Description | Scope (All / S-ID list) | Type | Falsifiable Threshold |
|--------|-------------|------------------------|------|----------------------|
| INV-01 | | | Numeric / Temporal / Structural | |
| INV-02 | | | | |

**VERIFY: Does INV-01 or INV-02 contain a numeric or temporal threshold? YES / NO**
If NO — add an invariant with a numeric or temporal threshold before advancing.

**ADVANCE TO PART 2.**

---

### PART 2: HAND-COMPILED TRACE

**STOP. Compile all trace steps before advancing to PART 3. Minimum 6 steps required.**
**VERIFY: Does at least one step carry [REJECTED]? YES / NO. If NO — add a rejected step.**

```
Step N: [OP-ID] [Operation Name]  [PASS / REJECTED]
  Before state:   [S-ID] [State Name] — { field: value, ... }
  Preconditions checked:
    - [text]: MET / NOT MET
  Guard condition: passes — continue  /  fires — reason: [text]
  After state:    [S-ID] [State Name] — { field: value, ... }
    [REJECTED: The entity must remain in its before-state after rejection.
     After state MUST equal before state field-for-field.
     VERIFY: does after-state match before-state field-for-field? YES / NO.
     If NO — any deviation is a detectable anomaly; record it as a finding in Phase 3A.]
  Postconditions verified:
    - [text]: HOLDS / VIOLATED — [note]
```

**ADVANCE TO PART 3.**

---

### PART 3: PRE-SWEEP HYPOTHESIS

**STOP. Record all predictions before any detection pass begins. This table is locked.**
Role A will return to this table in PART 5 to reconcile each row.

| Phase | Anomaly Type | Predicted Count | Confidence (L/M/H) | Specific Predicted Scenario |
|-------|-------------|-----------------|--------------------|-----------------------------|
| 3A | Invalid state transitions | | | |
| 3B | Missing precondition checks | | | |
| 3C | Invariant violations | | | |
| 3D | Race conditions | | | |
| 3E | Undeclared references | | | |

**ADVANCE TO PART 4.**

---

### PART 4: ANOMALY SWEEP

**V-05 ID Contract:** Three separate ID columns (OP-ID, S-ID, INV-ID) in all finding tables.
**V-05 Gap Record Contract:** All Gap Records use the PART 0.0A template — complete every field.

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**STOP. Role B pre-detection commitment before any pass runs.**
> Phase 3A evidence standard (verbatim from PART 0.0B): _____
> Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL:** At the moment you record a finding, say:
> "I am scoring this [1/2/3] because [specific trace-step or registry reference]."
Self-correction gate: if you cannot name a specific reference, the finding is not yet
recordable. Revise or discard before proceeding.

**Pass 1: Declaration-Only**
Scan State Registry (1A) and Operation Registry (1B). Look for operations with Valid
From States where those operations should be blocked; Valid To States skipping required
intermediate states.
If no finding: name the specific (OP-ID, S-ID) pairs examined and why each cleared.

**Pass 2: Trace-Diff**
Compare PART 2 steps against Operation Registry Valid From/To States. Look for steps
executing from an undeclared state or transitioning to an undeclared state.
If no finding: name specific steps, OP-IDs, and state-IDs examined and cleared.

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**STOP. Role B: COMPLETE THE GAP RECORD FORM NOW. Do not advance until all fields are populated.**

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**VERIFY: Are all 5 fields populated with non-placeholder content? YES / NO.**
**If NO — return to the Gap Record form and complete the missing fields before proceeding.**

**The Gap Record is the unlock signal for the Phase 3A exit gate.**

**Phase 3A Exit Certification — check all three before declaring COMPLETE:**
☐ Findings List gate — all findings recorded with Finding-IDs
☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record "Verdict" field explains why none qualified
☐ Gap Record gate — all 5 template fields populated

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**STOP. Role B pre-detection commitment before any pass runs.**
> Phase 3B (verbatim): _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL** — same as 3A.

**Pass 1: Declaration-Only** — scan OP-Registry for absent, underdefined, or overlapping preconditions.
If no finding: name OP-IDs and precondition cells cleared.

**Pass 2: Trace-Diff** — scan steps for NOT MET → PASS, missing precondition entries, or guard text
mismatching OP-Registry preconditions.
If no finding: name steps and precondition rows cleared.

**Finding Table — Phase 3B**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**STOP. Role B: COMPLETE THE GAP RECORD FORM NOW.**

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3B exit gate.**

**Phase 3B Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields populated

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**STOP. Role B pre-detection commitment.**
> Phase 3C (verbatim): _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL** — same as 3A.

**Pass 1: Declaration-Only** — scan INV + OP for postconditions breaching thresholds; cumulative
transition scenarios.
If no finding: name (INV-ID, OP-ID) pairs cleared.

**Pass 2: Trace-Diff** — scan after-states against INV thresholds; check adjacent step pairs for
cumulative breaches; check postconditions marked VIOLATED.
If no finding: name steps and INV-IDs cleared.

**Finding Table — Phase 3C**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**STOP. Role B: COMPLETE THE GAP RECORD FORM NOW.**

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3C exit gate.**

**Phase 3C Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields populated

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**STOP. Role B pre-detection commitment.**
> Phase 3D (verbatim): _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL** — same as 3A.

**Pass 1: Declaration-Only** — identify OP-ID pairs sharing Valid From States; construct concurrent
scenario; name the anomalous outcome not reachable by either sequential ordering.
If no finding: name OP-ID pairs and convergence rationale.

**Pass 2: Trace-Diff** — select step pairs from PART 2 with overlapping states or shared fields;
construct the concurrent interleaving; compare concurrent after-state to both sequential orderings.
If no finding: name step pairs and comparison result.

**Finding Table — Phase 3D**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**STOP. Role B: COMPLETE THE GAP RECORD FORM NOW.**

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3D exit gate.**

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields populated

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References — Stratified + Structured Gap Record

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

**STOP. Role B pre-detection commitment.**
> Phase 3E (verbatim): _____  /  Min: _____  /  Gate: _____

---

**THE SCORING PROTOCOL — active for all six sub-scans:**
At the moment you record a finding: "I am scoring this [1/2/3] because [registry entry
X references ID Y, and Y is absent from registry Z]." Incomplete sentence = not recordable.

---

**Pass 1: Declaration-Only — Three Independent Sub-Scans**

**Sub-scan P1-S: S-ID References**
Examine 1B Valid From States, Valid To States; 1C Scope field.
Does every S-ID cited appear as a declared row in 1A?
If no finding: list each cell and the S-ID confirmed in 1A (e.g., "OP-01 Valid From:
S-01, S-02 — S-01 confirmed row 1 of 1A; S-02 confirmed row 2 of 1A").

**Sub-scan P1-O: OP-ID References**
Examine 1C descriptions/thresholds for OP-ID references; 1B cross-operation OP-ID cites.
Does every OP-ID cited appear as a declared row in 1B?
If no finding: list each cell and OP-ID confirmed in 1B.

**Sub-scan P1-I: INV-ID References**
Examine 1B preconditions/postconditions; 1A entry/exit conditions.
Does every INV-ID cited appear as a declared row in 1C?
If no finding: list each cell and INV-ID confirmed in 1C.

---

**Pass 2: Trace-Diff — Three Independent Sub-Scans**

**Sub-scan P2-S:** Scan PART 2 step Before/After states; Phases 3A–3D S-ID cells in finding tables.
Does every S-ID resolve to 1A? If no finding: list each step and finding table row checked.

**Sub-scan P2-O:** Scan PART 2 step headers (OP-IDs); Phases 3A–3D OP-ID cells.
Does every OP-ID resolve to 1B? If no finding: list each step and finding table row checked.

**Sub-scan P2-I:** Scan PART 2 postcondition VIOLATED notes for INV-ID references; Phases 3A–3D INV-ID cells.
Does every INV-ID resolve to 1C? If no finding: list each entry and INV-ID checked.

---

**Finding Table — Phase 3E**

Each row is independent. A verdict in one row does NOT satisfy another row's requirement.

| Entity Class | Declaration-Only Finding (P1 sub-scan) | Trace-Diff Finding (P2 sub-scan) | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|-------------|----------------------------------------|----------------------------------|-------|------|--------|--------------------------|
| S-ID references | | | — | | — | |
| OP-ID references | | | | — | — | |
| INV-ID references | | | — | — | | |

*"None" in any cell requires inline: what was checked and why it cleared.*
*A finding in one row does not satisfy another row.*

---

**STOP. Role B: COMPLETE THE GAP RECORD FORM NOW. The Examined field must address all three entity classes.**

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | [S-ID class: cells/steps checked — / OP-ID class: — / INV-ID class: —] |
| Evidence Standard Applied | |
| What Was Not Found | [Per entity class: S-ID: — / OP-ID: — / INV-ID: —] |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

**Phase 3E Exit Certification**
☐ Findings List gate — all three entity-class rows populated
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1, OR Gap Record "Verdict" covers all three classes
☐ Gap Record gate — all 5 template fields populated; Examined field covers all three entity classes

**PHASE 3E: COMPLETE [Sweep closed — advance to PART 5]**

---

### PART 5: POST-SWEEP RECONCILIATION

**[STATUS: LOCKED until PHASE 3E: COMPLETE]**

Role A returns to the PART 3 Hypothesis Table. For each prediction row, examine the
actual findings from Phases 3A–3E and classify the outcome:

- **C (Correct)** — predicted finding type matched an actual finding in the corresponding phase
- **FP (False Positive)** — predicted a finding that did not materialize (predicted count > 0, actual = 0)
- **FN (False Negative)** — a finding emerged that was not predicted (predicted count = 0, actual > 0)

**Reconciliation Table**

| Phase | Predicted Count | Actual Count | Classification (C / FP / FN) | Finding-IDs (if C or FN) | Surprise? (Expected / Surprising) |
|-------|-----------------|--------------|------------------------------|--------------------------|-----------------------------------|
| 3A | | | | | |
| 3B | | | | | |
| 3C | | | | | |
| 3D | | | | | |
| 3E | | | | | |

**Calibration Score**

```
C count:  ___
FP count: ___
FN count: ___
Total predictions: ___

Calibration score = C / (C + FP + FN) = ___ / ___ = ___
```

**Calibration threshold: 0.60**

If calibration score ≥ 0.60: analysis is well-calibrated. Note any surprising findings
for future hypothesis improvement.

If calibration score < 0.60: **structural diagnosis required**. Execute all three steps:

1. **Identify systematic over/under-prediction**: Which anomaly types were systematically
   mis-predicted? List each phase where FP or FN occurred and the direction of the error.

2. **Trace to declaration gaps**: For each mis-predicted type, identify which declaration
   registry (1A, 1B, or 1C) contributed to the hypothesis error — was the state machine
   underdeclared, were preconditions ambiguous, were invariants too qualitative?

3. **Record methodology verdict**: State whether the miscalibration indicates a gap in
   hypothesis methodology (the prediction process was flawed) or a gap in declaration
   completeness (the registries did not expose the anomalies clearly). This verdict
   becomes an input to the next analysis iteration.

---

*End of V-05 prompt body.*
