# trace-state Skill — Quest Variations Round 12

**Skill**: trace-state
**Round**: 12 (building on R11 V-01 score: 98.97/100)
**Rubric**: v11 (31 aspirationals, 0.323 pts each)
**R12 target gaps**: C-17, C-21, C-25, C-36

## Variation Map

| Variation | Axis | Target Gaps | Phase 3E | ID Columns | PART 5 |
|-----------|------|-------------|----------|------------|--------|
| V-01 | Output format | C-17 | Abbreviated | 3 separate | No |
| V-02 | Lifecycle emphasis | C-36 | Fully expanded | Combined | No |
| V-03 | Role sequence | C-21 + C-25 | Abbreviated | Combined | Yes |
| V-04 | Compound (output + lifecycle) | C-17 + C-36 | Fully expanded | 3 separate | No |
| V-05 | Compound (all gaps + register) | C-17 + C-21 + C-25 + C-36 | Fully expanded | 3 separate | Yes |

---

## V-01: Output Format — Three Separate ID Columns

**Variation axis**: Output format — finding tables use three separate columns (OP-ID, S-ID,
INV-ID) instead of a combined `OP-ID / S-ID affected` column; a blank cell in any ID column
for a found-verdict row is a detectable structural gap, not an acceptable omission.

**Hypothesis**: Splitting the combined ID column into three independent columns creates a
symmetric ID contract: Phase 3C invariant-violation findings must populate INV-ID; Phase 3D
race-condition findings must populate both OP-IDs; Phase 3A findings must show the
(OP-ID, S-ID) transition pair. A finding that cannot populate any ID column does not have
sufficient evidence and should not be recorded. Blank-cell detection is mechanical.

**Target gaps**: C-17

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or
**Finance**. Choose the domain that best fits the scenario you are given. Your task is to
hand-compile state transitions, identify anomalies, and produce a structured trace-state
report. You play two roles throughout this analysis:

- **Role A (Anomaly Finder)**: runs detection passes and records findings
- **Role B (Evidence Steward)**: locks evidence standards before detection begins, then
  produces an unconditional Gap Record after each phase regardless of finding count

---

### PART 0: STANDARDS REGISTRY

Before PART 1 opens, declare the complete evidence standards for all five phases.
This registry is SEALED once declared — standards cannot be revised at any point
during analysis, including at phase entry and after findings are known.

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record explains why none qualified |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and the anomalous outcome not present in sequential execution | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch: a state, operation, or invariant referenced in trace or docs but absent from its registry | ≥ 1 | ≥ 1 finding at strength ≥ 1, OR Gap Record explains why none found |

**STANDARDS REGISTRY: SEALED → PART 1 now OPEN.**

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
REJECTED steps must confirm state immutability explicitly — do not omit the after-state.

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

**V-01 ID Contract — applies to all finding tables in this variation:**
Every finding table uses three separate ID columns: **OP-ID**, **S-ID**, **INV-ID**.
A blank cell in any of these columns for a found-verdict row is a detectable structural
gap. Populate each column with the relevant ID(s). Use `—` only if the anomaly type
genuinely does not implicate that ID class — and explain why in the finding description.
This contract makes cross-phase ID coverage mechanically auditable.

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
States that skip required intermediate states; or (S-ID → OP-ID → S-ID) transitions
implied by the registry that contradict documented state semantics.

If no finding in this pass: name the specific (OP-ID, S-ID) pairs you examined and why
each cleared.

**Pass 2: Trace-Diff**
Compare each PART 2 step against the Operation Registry. Look for: steps executing from
a state not in the OP's Valid From States; steps transitioning to a state not in Valid
To States; REJECTED steps where the rejection reason contradicts the declared guard.

If no finding in this pass: name the specific steps (Step N, OP-ID, from-S-ID) you
examined and why each cleared.

---

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|
| | | | | | | |

*Blank in OP-ID, S-ID, or INV-ID for a found-verdict row = detectable structural gap.*

---

**Role B (Evidence Steward) — Gap Record [UNCONDITIONAL]**
Fires regardless of finding count. Document what was examined but not found.
> Gap Record 3A: _____
> Specific entries examined and cleared: _____
> Why the absence of additional findings is credible: _____

**The Gap Record is the unlock signal for the Phase 3A exit gate.**

---

**Phase 3A Exit Certification**
☐ Findings List gate — all findings recorded with Finding-IDs
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 2, OR Gap Record explicitly explains why no finding met the threshold
☐ Gap Record gate — Gap Record present (unconditional)

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B (Evidence Steward) — Pre-Detection Commitment**
Restate the PART 0 registry row for Phase 3B verbatim:
> Phase 3B evidence standard: _____
> Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL** — same as Phase 3A. Score at point of discovery.

**Pass 1: Declaration-Only**
Examine the Operation Registry (1B). Look for: operations with preconditions that are
underdefined, absent, or that could evaluate to MET in a state where the operation
should be blocked; preconditions that overlap such that a false MET on one masks a
NOT MET on another.
If no finding: name the specific OP-IDs and precondition cells examined and cleared.

**Pass 2: Trace-Diff**
Examine PART 2 steps. Look for: steps where a precondition is NOT MET but the operation
proceeds PASS; steps missing any precondition-checked entries; REJECTED steps whose
guard text references a different condition than the OP-Registry preconditions list.
If no finding: name the specific steps and precondition rows examined and cleared.

**Finding Table — Phase 3B**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]**
> Gap Record 3B: _____

**The Gap Record is the unlock signal for the Phase 3B exit gate.**

**Phase 3B Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record explains why  ☐ Gap Record gate

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B (Evidence Steward) — Pre-Detection Commitment**
Restate the PART 0 registry row for Phase 3C verbatim:
> Phase 3C evidence standard: _____
> Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL** — same as Phase 3A. Score at point of discovery.

**Pass 1: Declaration-Only**
Examine the Invariant Registry (1C) and Operation Registry (1B). Look for: operations
whose postconditions could produce a state violating a declared invariant; INV-IDs
with numeric or temporal thresholds that could be breached by cumulative transitions
even if no single operation crosses the threshold alone.
If no finding: name specific (INV-ID, OP-ID) pairs examined and cleared.

**Pass 2: Trace-Diff**
Examine PART 2 steps. Look for: after-states that breach an invariant threshold;
postconditions marked VIOLATED that implicate an INV-ID; adjacent step pairs where the
delta across two after-states crosses a numeric threshold not crossed by either step alone.
If no finding: name specific steps and INV-IDs examined and cleared.

**Finding Table — Phase 3C**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]**
> Gap Record 3C: _____

**The Gap Record is the unlock signal for the Phase 3C exit gate.**

**Phase 3C Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B (Evidence Steward) — Pre-Detection Commitment**
Restate the PART 0 registry row for Phase 3D verbatim:
> Phase 3D evidence standard: _____
> Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL** — same as Phase 3A. Score at point of discovery.

**Pass 1: Declaration-Only**
Examine the Operation Registry (1B). Identify pairs of operations that share at least
one Valid From State (meaning both are legal to initiate from that state). For each
pair: describe the anomalous outcome that would result from concurrent execution on
the same entity — an outcome not reachable by either sequential ordering.
If no finding: name the OP-ID pairs constructed and why concurrent execution converges.

**Pass 2: Trace-Diff**
Select two steps from PART 2 that execute from the same or overlapping states, or
that modify the same field. Construct the concurrent interleaving. Compare the
concurrent after-state to the sequential after-state. If they diverge, that divergence
is the finding.
If no finding: name the step pairs constructed and the after-state comparison result.

**Finding Table — Phase 3D**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]**
> Gap Record 3D: _____

**The Gap Record is the unlock signal for the Phase 3D exit gate.**

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

Phase 3E is a full structural peer of Phases 3A–3D. Apply the complete phase mechanics:
Role B pre-detection commitment (restate PART 0 registry row for 3E verbatim) →
THE SCORING PROTOCOL → Pass 1 (Declaration-Only: scan registries 1A/1B/1C for internal
cross-reference gaps where one registry references an ID absent from another) →
Pass 2 (Trace-Diff: scan PART 2 steps and all prior finding tables for any S-ID,
OP-ID, or INV-ID that does not resolve to a registry entry) → Finding table (3 separate
ID columns per V-01 contract) → Role B Gap Record [UNCONDITIONAL] → Phase 3E Exit
Certification (three-gate: Findings List, Evidence Strength ≥ 1, Gap Record).

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-01 prompt body.*

---
---

## V-02: Lifecycle Emphasis — Phase 3E Fully Expanded

**Variation axis**: Lifecycle emphasis — Phase 3E receives a complete, fully-expanded
template body identical in structural depth to Phases 3A–3D; no abbreviation, no
reference to "same as prior phases"; every structural element is written out explicitly.

**Hypothesis**: The R11 PARTIAL on C-36 resulted from Phase 3E being described as a
peer in intent but abbreviated in template. A model following abbreviated instructions
will fill gaps with its own judgment about which structural elements are optional. A
fully-expanded template forces mechanical compliance by making every element a visible
slot — the model cannot skip what it cannot overlook.

**Target gaps**: C-36

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
This registry is SEALED once declared — standards cannot be revised at any point.

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record explains why |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and the anomalous outcome not present in sequential execution | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch: a state, operation, or invariant referenced in trace or docs but absent from its registry | ≥ 1 | ≥ 1 finding at strength ≥ 1, OR Gap Record explains why |

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

| INV-ID | Description | Scope | Type | Falsifiable Threshold |
|--------|-------------|-------|------|----------------------|
| INV-01 | | | | |
| INV-02 | | | | |

---

### PART 2: HAND-COMPILED TRACE

Minimum 6 numbered steps. At least one must be a `[REJECTED]` negative-path step.

**Trace step template:**

```
Step N: [OP-ID] [Operation Name]  [PASS / REJECTED]
  Before state:   [S-ID] [State Name] — { field: value, ... }
  Preconditions checked:
    - [text]: MET / NOT MET
  Guard condition: passes — continue  /  fires — reason: [text]
  After state:    [S-ID] [State Name] — { field: value, ... }
    [REJECTED: The entity must remain in its before-state after rejection.
     After state MUST equal before state field-for-field. Any deviation
     is a detectable anomaly independent of the rejection reason.]
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

**V-02 ID Contract — applies to all finding tables in this variation:**
Finding tables use a single combined column `OP-ID / S-ID affected` for referencing
impacted entities. List all relevant IDs in this column separated by commas.

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B (Evidence Steward) — Pre-Detection Commitment**
Restate the PART 0 registry row for Phase 3A verbatim:
> Phase 3A evidence standard: _____
> Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL:** Assign strength at discovery. Say: "I am scoring this [1/2/3]
because [specific reference]." Self-correction gate: incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan State Registry (1A) + Operation Registry (1B) for
invalid transitions declared in documentation.
If no finding: name the specific (OP-ID, S-ID) pairs cleared.

**Pass 2: Trace-Diff** — diff declared Valid From/To States against PART 2 steps.
If no finding: name the specific steps and state-IDs cleared.

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID / S-ID affected | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|-----------------------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]**
> Gap Record 3A: _____
The Gap Record is the unlock signal for the Phase 3A exit gate.

**Phase 3A Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record explains why  ☐ Gap Record gate

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment** (restate 3B registry row verbatim): _____

**THE SCORING PROTOCOL** — same as 3A.

**Pass 1: Declaration-Only** — scan OP-Registry for underdefined or absent preconditions.
If no finding: name OP-IDs cleared.

**Pass 2: Trace-Diff** — scan trace steps for NOT MET preconditions that allow PASS,
or missing precondition entries.
If no finding: name steps cleared.

**Finding Table — Phase 3B**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID / S-ID affected | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|-----------------------|--------------------------|

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

**Pass 1: Declaration-Only** — scan INV-Registry + OP-Registry for postconditions that
could breach a declared threshold.
If no finding: name (INV-ID, OP-ID) pairs cleared.

**Pass 2: Trace-Diff** — scan trace after-states against INV thresholds; check adjacent
step pairs for cumulative breaches.
If no finding: name steps and INV-IDs cleared.

**Finding Table — Phase 3C**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID / S-ID affected | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|-----------------------|--------------------------|

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

**Pass 1: Declaration-Only** — identify OP-ID pairs sharing Valid From States;
construct concurrent scenario; describe anomalous outcome vs sequential.
If no finding: name OP-ID pairs and convergence rationale.

**Pass 2: Trace-Diff** — select overlapping-state step pairs from PART 2; construct
interleaving; compare concurrent after-state vs sequential.
If no finding: name step pairs and comparison result.

**Finding Table — Phase 3D**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID / S-ID affected | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|-----------------------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]** > Gap Record 3D: _____
The Gap Record is the unlock signal for the Phase 3D exit gate.

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

**V-02 expansion**: Phase 3E is written with a complete template body. Every structural
element is expanded explicitly — no abbreviation, no reference to "same as prior phases."

**Role B (Evidence Steward) — Pre-Detection Commitment**
Restate the PART 0 registry row for Phase 3E **verbatim**:
> Phase 3E evidence standard: _____
> Min strength: _____
> Gate: _____

This commitment is locked. It cannot be adjusted after Pass 1 or Pass 2 begins.

---

**THE SCORING PROTOCOL — active for both passes:**
Assign evidence strength the moment you record a finding. Say aloud:
> "I am scoring this [1/2/3] because [specific cross-reference: registry entry X
> references ID Y, but Y does not appear in registry Z at row N]."

Self-correction gate: if you cannot identify the specific registry entry and the
specific missing target, the finding is not yet recordable. Resolve before proceeding.

---

**Pass 1: Declaration-Only**
Scan the three registries (1A, 1B, 1C) for internal cross-reference mismatches:
- 1B Valid From States or Valid To States: does each S-ID appear in 1A?
- 1C Scope field (if it references specific states): does each referenced S-ID appear in 1A?
- 1C description or threshold: does any OP-ID reference appear in 1B?
- 1B Preconditions or Postconditions: does any INV-ID reference appear in 1C?

If no finding in this pass: name the specific cross-reference cells you checked
(e.g., "OP-03 Valid From States: S-01, S-02, S-03 — all confirmed in 1A") and confirm
each resolved to a declared registry entry.

**Pass 2: Trace-Diff**
Scan PART 2 trace steps for any S-ID, OP-ID, or INV-ID that does not appear in its
corresponding registry. Then scan finding tables from Phases 3A–3D for any ID reference
in findings or gap records that cannot be resolved to a registry entry.

If no finding in this pass: name the specific trace steps checked, the IDs referenced
in each, and confirm each resolved to a declared entry.

---

**Finding Table — Phase 3E**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID / S-ID affected | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|-----------------------|--------------------------|
| | | | | |

*A "None" in either finding column requires an inline explanation of what was checked
and confirmed absent, not a bare "None" entry.*

---

**Role B (Evidence Steward) — Gap Record [UNCONDITIONAL]**
Fires regardless of finding count. Document what was cross-referenced and cleared.
> Gap Record 3E: _____
> Registries scanned: 1A (N states), 1B (N operations), 1C (N invariants)
> Trace steps audited: Steps 1–N
> Prior finding tables scanned: Phases 3A–3D finding tables
> Specific cross-references confirmed present: _____
> Why the absence of additional findings is credible: _____

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

---

**Phase 3E Exit Certification**
☐ Findings List gate — all findings recorded with Finding-IDs
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1, OR Gap Record explicitly explains why no finding met the threshold
☐ Gap Record gate — Gap Record present (unconditional)

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-02 prompt body.*

---
---

## V-03: Role Sequence — Post-Sweep Reconciliation Phase

**Variation axis**: Role sequence — after Phase 3E closes, Role A returns to the PART 3
Hypothesis Table and performs a structured reconciliation: each prediction is classified
using a three-value taxonomy (C / FP / FN), a calibration score is computed, and a
diagnostic is required when accuracy falls below threshold.

**Hypothesis**: C-21 (Surprise column) and C-25 (C/FP/FN taxonomy with calibration)
require a post-sweep artifact that pairs predictions to outcomes. Adding a mandatory
PART 5 that Role A executes after all phases close — with explicit C/FP/FN columns,
a computed calibration score, and a below-threshold diagnostic trigger — closes both
criteria simultaneously. The key structural insight is that Role A's detection role
makes it the natural author of reconciliation: the same agent that made predictions
is now confronting its calibration record.

**Target gaps**: C-21 + C-25

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or
**Finance**. Choose the domain that best fits the scenario you are given. Your task is to
hand-compile state transitions, identify anomalies, and produce a structured trace-state
report. You play two roles throughout:

- **Role A (Anomaly Finder)**: runs detection passes, records findings, and after all
  phases close, executes the post-sweep reconciliation in PART 5
- **Role B (Evidence Steward)**: locks evidence standards before detection begins, then
  produces an unconditional Gap Record after each phase

---

### PART 0: STANDARDS REGISTRY

Before PART 1 opens, declare the complete evidence standards for all five phases.
SEALED once declared — standards cannot be revised at any point during analysis.

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 at strength ≥ 2, OR Gap Record explains why |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and anomalous outcome | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch between registry and trace/docs | ≥ 1 | ≥ 1 at strength ≥ 1, OR Gap Record explains why |

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

| INV-ID | Description | Scope | Type | Falsifiable Threshold |
|--------|-------------|-------|------|----------------------|
| INV-01 | | | | |
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
     After state MUST equal before state field-for-field.]
  Postconditions verified:
    - [text]: HOLDS / VIOLATED
```

---

### PART 3: PRE-SWEEP HYPOTHESIS

Record predictions before PART 4 begins. Locked once any detection pass runs.
Role A will return to this table in PART 5 to reconcile each row.

| Phase | Anomaly Type | Predicted Count | Confidence (L/M/H) | Specific Predicted Scenario |
|-------|-------------|-----------------|--------------------|-----------------------------|
| 3A | Invalid state transitions | | | |
| 3B | Missing precondition checks | | | |
| 3C | Invariant violations | | | |
| 3D | Race conditions | | | |
| 3E | Undeclared references | | | |

---

### PART 4: ANOMALY SWEEP

**V-03 ID Contract:** Finding tables use combined `OP-ID / S-ID affected` column.

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B — Pre-Detection Commitment** (restate 3A registry row verbatim): _____

**THE SCORING PROTOCOL:** Score at discovery. "I am scoring this [1/2/3] because
[specific reference]." Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions.
If no finding: name (OP-ID, S-ID) pairs cleared.

**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps.
If no finding: name steps and states cleared.

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID / S-ID affected | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|-----------------------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]** > Gap Record 3A: _____
The Gap Record is the unlock signal for the Phase 3A exit gate.

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

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID / S-ID affected | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|-----------------------|--------------------------|

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
**Pass 1: Declaration-Only** — scan INV + OP for postconditions that breach thresholds. If no finding: name (INV-ID, OP-ID) pairs cleared.
**Pass 2: Trace-Diff** — scan after-states and adjacent pairs for cumulative breaches. If no finding: name steps and INV-IDs cleared.

**Finding Table — Phase 3C**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID / S-ID affected | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|-----------------------|--------------------------|

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
**Pass 1: Declaration-Only** — identify OP pairs sharing Valid From States; construct concurrent scenario. If no finding: name OP pairs and convergence rationale.
**Pass 2: Trace-Diff** — construct interleaving from overlapping-state step pairs. If no finding: name pairs and comparison result.

**Finding Table — Phase 3D**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID / S-ID affected | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|-----------------------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]** > Gap Record 3D: _____
The Gap Record is the unlock signal for the Phase 3D exit gate.

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

Phase 3E is a full structural peer of Phases 3A–3D. Apply complete phase mechanics:
Role B pre-detection commitment (restate 3E registry row verbatim) →
THE SCORING PROTOCOL → Pass 1 (scan 1A/1B/1C for internal cross-reference gaps) →
Pass 2 (scan trace steps and prior finding tables for undeclared IDs) →
Finding table (combined ID column per V-03 contract) →
Role B Gap Record [UNCONDITIONAL] →
Phase 3E Exit Certification (three-gate: Findings, Evidence Strength ≥ 1, Gap Record).

The Gap Record is the unlock signal for the Phase 3E exit gate.

**PHASE 3E: COMPLETE [Unlocks PART 5]**

---

### PART 5: POST-SWEEP RECONCILIATION

**Role A (Anomaly Finder) — Reconciliation Pass**

PART 4 is closed. Return to the PART 3 Hypothesis Table and reconcile each prediction
row against the actual findings from the completed sweep.

**Classification taxonomy** (three-value, mandatory for every row):
- **C** (Correct): Your prediction closely matched the actual count (within ±1) AND the
  specific predicted scenario you named in PART 3 materialized as a finding
- **FP** (False Positive): You predicted a finding that did not materialize — you
  over-predicted; the scenario you named was not found in either detection pass
- **FN** (False Negative): A finding materialized that you did not predict — you
  under-predicted; a finding exists in a phase where your predicted count was lower

**Surprise classification** (for each row, separate from C/FP/FN):
- **Expected**: This outcome is consistent with your prior experience analyzing this
  domain's state machine; the result did not require you to revise your mental model
- **Surprising**: This outcome contradicts a prior assumption; you would have bet
  differently before running the trace

**Reconciliation Table**

| Phase | Anomaly Type | Predicted Count | Actual Count | Outcome (C / FP / FN) | Surprising? (E / S) | Notes |
|-------|-------------|-----------------|--------------|----------------------|---------------------|-------|
| 3A | Invalid state transitions | | | | | |
| 3B | Missing precondition checks | | | | | |
| 3C | Invariant violations | | | | | |
| 3D | Race conditions | | | | | |
| 3E | Undeclared references | | | | | |

**Calibration Score Computation**
```
Calibration Score = (number of C outcomes) / (total rows)
```

**Diagnostic threshold**: If Calibration Score < 60%, trigger a structural diagnosis:
1. Name which anomaly types were systematically over- or under-predicted (FP-heavy
   vs FN-heavy)
2. Identify the bias mechanism: confirmation bias (predicted what you expected to find),
   anchoring (first finding in a phase stopped the search), or scope-tunnel (searched
   one detection mode more thoroughly than the other)
3. State one concrete change to the evidence standard or hypothesis practice that would
   improve calibration on the next trace execution

If Calibration Score ≥ 60%: record the score and note which predictions were most
accurate (C outcomes with Surprising = S are particularly informative — they indicate
the model is detecting real signals rather than just confirming priors).

---

*End of V-03 prompt body.*

---
---

## V-04: Compound — Output Format + Lifecycle Emphasis

**Variation axis**: Compound — three separate ID columns (C-17) combined with Phase 3E
fully expanded in template body (C-36). No PART 5 reconciliation.

**Hypothesis**: C-17 and C-36 are independent structural fixes that do not interact:
the ID column format change affects all five phases uniformly, and the Phase 3E
expansion is isolated to Phase 3E's template. Combining both in a single variation
tests whether they compound cleanly without introducing structural interference. A
score of 98.97 + 2 × 0.323 = 99.62 is the prediction if neither fix interferes
with the existing 25 passing aspirationals.

**Target gaps**: C-17 + C-36

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
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 at strength ≥ 2, OR Gap Record explains why |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and anomalous outcome | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch between registry and trace/docs | ≥ 1 | ≥ 1 at strength ≥ 1, OR Gap Record explains why |

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

| INV-ID | Description | Scope | Type | Falsifiable Threshold |
|--------|-------------|-------|------|----------------------|
| INV-01 | | | | |
| INV-02 | | | | |

---

### PART 2: HAND-COMPILED TRACE

Minimum 6 numbered steps. At least one `[REJECTED]` step required.

```
Step N: [OP-ID] [Operation Name]  [PASS / REJECTED]
  Before state:   [S-ID] [State Name] — { field: value, ... }
  Preconditions checked:
    - [text]: MET / NOT MET
  Guard condition: passes — continue  /  fires — reason: [text]
  After state:    [S-ID] [State Name] — { field: value, ... }
    [REJECTED: The entity must remain in its before-state after rejection.
     After state MUST equal before state field-for-field.]
  Postconditions verified:
    - [text]: HOLDS / VIOLATED
```

---

### PART 3: PRE-SWEEP HYPOTHESIS

Record predictions before PART 4 begins. Locked once detection starts.

| Phase | Anomaly Type | Predicted Count | Confidence (L/M/H) | Specific Predicted Scenario |
|-------|-------------|-----------------|--------------------|-----------------------------|
| 3A | | | | |
| 3B | | | | |
| 3C | | | | |
| 3D | | | | |
| 3E | | | | |

---

### PART 4: ANOMALY SWEEP

**V-04 ID Contract — applies to all finding tables:**
Three separate ID columns: **OP-ID**, **S-ID**, **INV-ID**. A blank cell in any column
for a found-verdict row is a detectable structural gap. Use `—` only when the anomaly
type genuinely does not implicate that ID class; explain why in the finding description.

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B — Pre-Detection Commitment** (restate 3A registry row verbatim): _____

**THE SCORING PROTOCOL:** Score at discovery. "I am scoring this [1/2/3] because
[specific reference]." Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions.
If no finding: name (OP-ID, S-ID) pairs cleared.

**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps.
If no finding: name steps cleared.

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]** > Gap Record 3A: _____
The Gap Record is the unlock signal for the Phase 3A exit gate.

**Phase 3A Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record explains why  ☐ Gap Record gate

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment** (restate 3B registry row verbatim): _____
**THE SCORING PROTOCOL** — same as 3A.
**Pass 1** — scan OP-Registry for absent/underdefined preconditions. If no finding: name OP-IDs cleared.
**Pass 2** — scan steps for NOT MET → PASS. If no finding: name steps cleared.

**Finding Table — Phase 3B**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]** > Gap Record 3B: _____
The Gap Record is the unlock signal for the Phase 3B exit gate.
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate
**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment** (restate 3C registry row verbatim): _____
**THE SCORING PROTOCOL** — same as 3A.
**Pass 1** — scan INV + OP for threshold-breaching postconditions. If no finding: name (INV-ID, OP-ID) pairs cleared.
**Pass 2** — scan after-states and adjacent pairs for cumulative breaches. If no finding: name steps and INV-IDs cleared.

**Finding Table — Phase 3C**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]** > Gap Record 3C: _____
The Gap Record is the unlock signal for the Phase 3C exit gate.
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate
**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment** (restate 3D registry row verbatim): _____
**THE SCORING PROTOCOL** — same as 3A.
**Pass 1** — identify OP pairs sharing Valid From States; construct concurrent scenario. If no finding: name pairs and convergence rationale.
**Pass 2** — construct interleaving from overlapping step pairs; compare after-states. If no finding: name pairs and comparison.

**Finding Table — Phase 3D**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]** > Gap Record 3D: _____
The Gap Record is the unlock signal for the Phase 3D exit gate.
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate
**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

**V-04 expansion**: Phase 3E is fully expanded. Every structural element written out
explicitly — no abbreviation.

**Role B (Evidence Steward) — Pre-Detection Commitment**
Restate the PART 0 registry row for Phase 3E **verbatim**:
> Phase 3E evidence standard: _____
> Min strength: _____
> Gate: _____

This commitment is locked. It cannot be adjusted after Pass 1 or Pass 2 begins.

---

**THE SCORING PROTOCOL — active for both passes:**
Say aloud: "I am scoring this [1/2/3] because [specific cross-reference: registry entry
X at row Y references ID Z, which does not appear in registry W]."
Self-correction gate: if the sentence is not completable with a specific registry entry
and specific missing target, do not record the finding.

---

**Pass 1: Declaration-Only**
Scan registries 1A, 1B, 1C for internal cross-reference mismatches:
- 1B Valid From/To States: confirm each S-ID appears in 1A
- 1C Scope or description: confirm any OP-ID or S-ID reference appears in its registry
- 1B Preconditions/Postconditions: confirm any INV-ID reference appears in 1C
- 1C Threshold: confirm any OP-ID reference appears in 1B

If no finding: name the specific cross-reference cells examined and confirm each
resolved (e.g., "OP-03 Valid From States S-01, S-02: both confirmed in 1A").

**Pass 2: Trace-Diff**
Scan PART 2 trace steps: for each S-ID, OP-ID, and INV-ID referenced, confirm it
appears in the corresponding registry. Then scan finding tables from Phases 3A–3D:
for each ID referenced in any finding or gap record, confirm it resolves to a declared
registry entry.

If no finding: name each trace step checked, list the IDs referenced, and confirm
each resolved. Name each prior finding table row checked.

---

**Finding Table — Phase 3E**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|
| | | | | | | |

*A "None" in either finding column requires an inline explanation of what was checked
and confirmed absent — not a bare "None" entry.*

---

**Role B (Evidence Steward) — Gap Record [UNCONDITIONAL]**
> Gap Record 3E: _____
> Registries scanned: 1A (N states), 1B (N operations), 1C (N invariants)
> Trace steps audited: Steps 1–N
> Prior finding tables scanned: Phases 3A, 3B, 3C, 3D
> Cross-references confirmed present: _____
> Why absence of additional findings is credible: _____

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

---

**Phase 3E Exit Certification**
☐ Findings List gate — all findings recorded with Finding-IDs
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1, OR Gap Record explains why no finding met the threshold
☐ Gap Record gate — Gap Record present (unconditional)

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-04 prompt body.*

---
---

## V-05: Compound — All Four Gaps + Conversational Register

**Variation axis**: Compound targeting all four remaining gaps simultaneously. Three
separate ID columns (C-17) + Phase 3E fully expanded (C-36) + Post-sweep reconciliation
with C/FP/FN taxonomy (C-21 + C-25). Secondary axis: conversational phrasing register —
instructions use direct first-person imperative framing rather than formal third-person
description, testing whether register affects model compliance with the mechanics.

**Hypothesis**: A single variation that closes all four gaps is the 100/100 candidate.
The conversational register is a risk hedge: if formal register in V-01–V-04 produces
any compliance failures on complex structural elements, conversational register may
reduce parsing friction. Predicted score: 98.97 + 4 × 0.323 = 100.26 → 100.00 (capped).

**Target gaps**: C-17 + C-21 + C-25 + C-36

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or
**Finance**. Pick the domain that fits your scenario. Hand-compile the state machine,
run the five-phase anomaly sweep, and close with a reconciliation pass.

You run two roles:
- **Role A (Anomaly Finder)**: detects, records, and reconciles
- **Role B (Evidence Steward)**: locks standards before each phase, closes each phase
  with an unconditional gap record

Start here: seal your standards registry before touching any declarations.

---

### PART 0: STANDARDS REGISTRY

Fill in this table completely. Once you declare "SEALED," you cannot touch it again —
not at phase entry, not after you see a finding. This is the pre-game commitment.

| Phase | Anomaly Type | Your Evidence Standard | Min Strength | Your Gate Condition |
|-------|-------------|------------------------|--------------|---------------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record explains why |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and the anomalous outcome | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch between registry and trace/docs | ≥ 1 | ≥ 1 finding at strength ≥ 1, OR Gap Record explains why |

**STANDARDS REGISTRY: SEALED → PART 1 now OPEN.**

---

### PART 1: DECLARATIONS

Build your state machine. You'll reference these IDs throughout the analysis — keep
them consistent.

#### 1A: States (minimum 4)

| S-ID | State Name | To enter this state, what must be true? | To leave this state, what must be true? |
|------|-----------|----------------------------------------|----------------------------------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |
| S-04 | | | |

#### 1B: Operations (minimum 5)

| OP-ID | Name | Preconditions | Postconditions | Can run from | Transitions to |
|-------|------|--------------|----------------|-------------|----------------|
| OP-01 | | | | | |
| OP-02 | | | | | |
| OP-03 | | | | | |
| OP-04 | | | | | |
| OP-05 | | | | | |

#### 1C: Invariants (minimum 2; at least one numeric or temporal — no vague directionals)

| INV-ID | What must always hold | Which states | Type | Threshold — state exactly when this is violated |
|--------|----------------------|-------------|------|------------------------------------------------|
| INV-01 | | | | |
| INV-02 | | | | |

---

### PART 2: TRACE

Write at least 6 steps. Include at least one `[REJECTED]` step where a guard fires.

For every step:

```
Step N: [OP-ID] [Operation Name]  [PASS / REJECTED]
  Before state:   [S-ID] [State Name] — { field: value, ... }
  Preconditions:
    - [text]: MET / NOT MET
  Guard: passes — continue  /  fires — reason: [text]
  After state:    [S-ID] [State Name] — { field: value, ... }
    [On REJECTED: Write the after-state anyway. It must match the before-state
     field-for-field — the entity doesn't move when rejected. If it does move,
     that's a finding, not a valid rejection.]
  Postconditions:
    - [text]: HOLDS / VIOLATED
```

---

### PART 3: HYPOTHESIS

Before you run any detection, write down what you expect to find. Be specific — name
the scenario, not just "probably one or two." You'll grade yourself in PART 5.

| Phase | What you're hunting | How many you predict | Confidence (L/M/H) | Describe the specific scenario you expect to find |
|-------|--------------------|--------------------|--------------------|-------------------------------------------------|
| 3A | Invalid transitions | | | |
| 3B | Missing precondition checks | | | |
| 3C | Invariant violations | | | |
| 3D | Race conditions | | | |
| 3E | Undeclared references | | | |

Locked. No edits after the first pass runs.

---

### PART 4: SWEEP

**V-05 ID Contract — three separate columns in every finding table:**
OP-ID | S-ID | INV-ID — listed separately. A blank in any column for a found-verdict
row is a structural gap. Use `—` only when genuinely not applicable (explain why).

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN]**

**Role B — lock your standard now.** Restate your PART 0 row for Phase 3A verbatim:
> Standard: _____  /  Strength: _____  /  Gate: _____
Can't change this after Pass 1 starts.

**Score-aloud rule:** When you find something, immediately say:
"Scoring this [1/2/3] because [the specific step or registry entry I'm pointing to]."
If the sentence won't complete, don't record — revise until it does or drop it.

**Pass 1 — look at the declarations only:**
Scan 1A and 1B. Find any (OP-ID → S-ID → next S-ID) transitions that shouldn't exist
according to the state semantics. An operation that lists a Valid From State where that
operation is conceptually blocked is a finding.
No finding? Name the (OP-ID, S-ID) pairs you checked and why each cleared.

**Pass 2 — diff declarations against the trace:**
Walk through PART 2 step by step. For each step: is this OP-ID in the Valid From States
for the before-S-ID? Is the after-S-ID in the Valid To States? If not, that's a finding.
No finding? Name the steps you checked and what you confirmed.

**Findings:**

| Finding-ID | Declaration-Only | Trace-Diff | OP-ID | S-ID | INV-ID | Strength |
|------------|-----------------|------------|-------|------|--------|---------|

**Role B — Gap Record (write this regardless of how many findings you have):**
> What I checked and didn't find a problem with: _____
> Why I'm confident nothing was missed: _____

The Gap Record opens the exit gate.

☐ Findings recorded  ☐ At least one strength ≥ 2 OR gap record explains why  ☐ Gap Record present

**PHASE 3A: COMPLETE → Phase 3B now OPEN.**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED — wait for PHASE 3A: COMPLETE above]**

**Role B — lock your standard:** Restate 3B row verbatim: _____

**Score-aloud rule** — same as 3A.

**Pass 1:** Scan 1B. Find preconditions that are absent, too vague to evaluate, or that
could read MET in a state where the operation should be blocked. A precondition entry
like "data is valid" without referencing a specific state field is a finding candidate.
No finding? Name OP-IDs and precondition cells cleared.

**Pass 2:** Walk PART 2. Find: any step marked PASS where a precondition row says NOT
MET; any step with a missing preconditions section; any REJECTED step whose guard reason
doesn't match the declared precondition text.
No finding? Name steps and precondition rows cleared.

**Findings:**

| Finding-ID | Declaration-Only | Trace-Diff | OP-ID | S-ID | INV-ID | Strength |
|------------|-----------------|------------|-------|------|--------|---------|

**Role B — Gap Record (unconditional):** > _____
The Gap Record opens the exit gate.
☐ Findings recorded  ☐ Strength gate  ☐ Gap Record

**PHASE 3B: COMPLETE → Phase 3C now OPEN.**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED — wait for PHASE 3B: COMPLETE]**

**Role B — lock your standard:** Restate 3C row verbatim: _____

**Score-aloud rule** — same as 3A.

**Pass 1:** Scan 1B postconditions against 1C thresholds. Find: any operation whose
postcondition could produce a state that breaches a declared invariant threshold.
The numeric/temporal invariant from 1C is your primary target here.
No finding? Name (INV-ID, OP-ID) pairs checked and cleared.

**Pass 2:** Walk PART 2 after-states. For each step: does the after-state breach any
INV-ID threshold? Do adjacent steps together produce a cumulative breach that neither
step individually crosses?
No finding? Name steps and INV-IDs checked and cleared.

**Findings:**

| Finding-ID | Declaration-Only | Trace-Diff | OP-ID | S-ID | INV-ID | Strength |
|------------|-----------------|------------|-------|------|--------|---------|

**Role B — Gap Record (unconditional):** > _____
The Gap Record opens the exit gate.
☐ Findings recorded  ☐ Strength gate  ☐ Gap Record

**PHASE 3C: COMPLETE → Phase 3D now OPEN.**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED — wait for PHASE 3C: COMPLETE]**

**Role B — lock your standard:** Restate 3D row verbatim: _____

**Score-aloud rule** — same as 3A.

**Pass 1:** Look at 1B and find OP pairs that can both start from the same S-ID.
For each pair: write out what happens if both execute simultaneously on the same entity.
Compare that to what happens if they execute sequentially (either order). If concurrent
produces a state the sequential orderings don't, that's your finding.
No finding? Name OP-ID pairs constructed and why sequential and concurrent converge.

**Pass 2:** Pick two steps from PART 2 that touch overlapping states or the same field.
Interleave them. Compare the concurrent after-state against the sequential one.
No finding? Name the step pairs, show the comparison, confirm convergence.

**Findings:**

| Finding-ID | Declaration-Only | Trace-Diff | OP-ID | S-ID | INV-ID | Strength |
|------------|-----------------|------------|-------|------|--------|---------|

**Role B — Gap Record (unconditional):** > _____
The Gap Record opens the exit gate.
☐ Findings recorded  ☐ Strength gate  ☐ Gap Record

**PHASE 3D: COMPLETE → Phase 3E now OPEN.**

---

#### Phase 3E: Undeclared References

**[STATUS: LOCKED — wait for PHASE 3D: COMPLETE]**

**V-05 expansion**: Full template — every structural element written out. No shortcuts.

**Role B — lock your standard.** Restate your PART 0 row for Phase 3E verbatim:
> Standard: _____
> Strength: _____
> Gate: _____
Can't revise this after Pass 1 starts.

**Score-aloud rule:** "I'm scoring this [1/2/3] because registry entry [X] at row [Y]
references ID [Z], but [Z] does not appear in registry [W]." If this sentence won't
complete with specifics, don't record the finding.

**Pass 1 — internal cross-reference scan:**
Go through 1A, 1B, 1C systematically:
- Every S-ID listed in 1B Valid From States or Valid To States: does it appear in 1A?
- Every S-ID listed in 1C Scope: does it appear in 1A?
- Every OP-ID reference in 1C: does it appear in 1B?
- Every INV-ID reference in 1B preconditions or postconditions: does it appear in 1C?

No finding? List the cross-reference cells you checked and confirm each resolved:
> "OP-02 Valid From States: S-01, S-03 — both in 1A. INV-01 Scope: S-02 — in 1A. ..."

**Pass 2 — trace and prior findings scan:**
Go through every step in PART 2. For each S-ID, OP-ID, and INV-ID appearing in any
step field: confirm it's in the corresponding registry. Then go through the finding
tables from Phases 3A, 3B, 3C, 3D. For every ID in any finding description or gap
record: confirm it resolves.

No finding? List the steps and finding rows checked, the IDs verified, confirmations.

**Findings:**

| Finding-ID | Declaration-Only | Trace-Diff | OP-ID | S-ID | INV-ID | Strength |
|------------|-----------------|------------|-------|------|--------|---------|
| | | | | | | |

*"None" in either finding column needs an inline explanation — not a bare "None."*

**Role B — Gap Record (unconditional — write this regardless of finding count):**
> What I cross-referenced and cleared:
>   1A: N states × 2 columns = N cells checked
>   1B: N operations × Valid From + Valid To = N ID references checked
>   1C: N invariants × Scope field = N references checked
>   PART 2: Steps 1–N, all IDs confirmed
>   Phase 3A–3D finding tables: all finding-description IDs confirmed
> Why I'm confident nothing was missed: _____

**The Gap Record opens the Phase 3E exit gate.**

☐ Findings recorded  ☐ At least one finding at strength ≥ 1 OR Gap Record explains why  ☐ Gap Record present

**PHASE 3E: COMPLETE → PART 5 now OPEN.**

---

### PART 5: RECONCILIATION

The sweep is done. Go back to your PART 3 Hypothesis Table and grade yourself.

For each prediction row, you need two things:

**1. Outcome classification (C / FP / FN):**
- **C** (Correct): Count was close (within ±1) AND the specific scenario you named
  actually appeared as a finding
- **FP** (False Positive): You predicted a finding that didn't exist — you over-called
- **FN** (False Negative): A real finding exists that you didn't predict — you missed it

**2. Surprise rating (E / S):**
- **E** (Expected): You would have predicted this outcome again given the same domain
- **S** (Surprising): This outcome revised something in your mental model

Fill in the reconciliation table:

| Phase | Predicted Count | Actual Count | C / FP / FN | E / S | What this tells me |
|-------|-----------------|--------------|-------------|-------|-------------------|
| 3A | | | | | |
| 3B | | | | | |
| 3C | | | | | |
| 3D | | | | | |
| 3E | | | | | |

**Calibration Score:**
```
Score = (C count) / 5
```

If Score < 60% (fewer than 3 correct): run this diagnosis —
1. Which phases were FP-heavy vs FN-heavy?
2. Name the bias: confirmation (predicted what you expected), anchoring (first finding
   stopped the search), scope-tunnel (one detection pass got more attention than the
   other), or domain-blind (missing knowledge about the domain's real failure modes)
3. What would you do differently in your PART 3 hypothesis on the next execution?

If Score ≥ 60%: record the score. Flag any C rows where Surprise = S — those are your
highest-signal predictions, the ones where the model is detecting real domain structure
rather than confirming prior expectations.

---

*End of V-05 prompt body.*
