# trace-state Skill — Quest Variations Round 15

**Skill**: trace-state
**Round**: 15 (building on R13 V-04 base; rubric v13, 35 aspirationals)
**Rubric**: v13 (C-01–C-43; aspirationals worth 10/35 = 0.286 pts each)
**R15 target gaps**: C-42 (phase scoring protocol with registry-specific application sentence), C-43 (Phase 3E Pass 2 entity-type stratification — P2-S/P2-O/P2-I as independent rows)

## Variation Map

| Variation | Axis | Target Gaps | Application Sentence | Phase 3E P2 | Gap Record | PART 5 |
|-----------|------|-------------|---------------------|-------------|------------|--------|
| V-01 | Output format | C-42 | Named inline per-phase (APPLICATION SENTENCE artifact) | 3-row combined | 5-field template | No |
| V-02 | Lifecycle emphasis | C-43 | Absent | 6-row split (P1-S/O/I + P2-S/O/I) | Prose | No |
| V-03 | Role sequence | C-42 | Pre-declared in PART 0.0C by Role B, sealed | 3-row combined | 5-field template | No |
| V-04 | Compound (output + lifecycle) | C-42 + C-43 | Named inline per-phase | 6-row split | 5-field template | No |
| V-05 | Compound (output + lifecycle + phrasing) | C-42 + C-43 | Named inline, imperative voice | 6-row split | 5-field template | Yes (C/FP/FN) |

---

## V-01: Output Format — Phase Scoring Protocol with Application Sentence

**Variation axis**: Output format — THE SCORING PROTOCOL section in each phase now
contains two named artifacts: (1) verbatim restate of the PART 0 registry row (C-35/C-38),
and (2) a named APPLICATION SENTENCE that maps the generic evidence threshold to the
phase-specific anomaly evidence shape. The application sentence is a required structural
element. A SCORING PROTOCOL that restates the registry row but omits the application
sentence is incomplete — it does not satisfy the phase-header standard.

**Hypothesis**: C-35 requires the verbatim restate. The restate is passive: it confirms the
standard exists but does not force the evaluator to articulate what the standard *means*
for this specific anomaly type. A model can restate "strength ≥ 2 required" for race
conditions and then score concurrent-execution findings against an implicit, unverifiable
interpretation of what strength ≥ 2 means for that anomaly class. Requiring an explicit
APPLICATION SENTENCE — "For Phase 3D race conditions, strength ≥ 2 means: a named
(OP-ID-A, OP-ID-B, shared-S-ID) triple with a named anomalous after-state under one
interleaving that is absent from both sequential orderings" — makes the evaluator's
threshold for that specific anomaly class mechanically traceable and auditable before any
finding is recorded.

**Target gaps**: C-42

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
| Field                           | Content |
|--------------------------------|---------|
| Examined                       | [Specific OP-IDs, S-IDs, INV-IDs, trace steps, or registry
|                                |  cells checked — named individually, not summarized] |
| Evidence Standard Applied      | [Verbatim restatement from PART 0.0B registry row] |
| What Was Not Found             | [Specific absence: anomaly type + IDs that did not trigger,
|                                |  named — "No violations found" is not acceptable] |
| What Would Constitute a Finding | [Phase-specific minimum evidence that would qualify —
|                                |  must name the trace-step pattern or registry condition,
|                                |  not a generic description] |
| Verdict                        | Acquitted — no qualifying evidence exists
|                                |   OR Partial — finding present below threshold: [specify
|                                |   which finding(s) and why they did not qualify] |
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

**V-01 ID Contract:** All finding tables use three separate ID columns (OP-ID, S-ID,
INV-ID). A blank cell in any of these columns for a found-verdict row is a detectable
structural gap. Use `—` only when the anomaly type genuinely does not implicate that
ID class, with a reason in the finding description.

**V-01 Gap Record Contract:** All Gap Records use the 5-field PART 0.0A template.
A Gap Record with any field blank or left as placeholder text is a structural failure.
The Gap Record is the unlock signal for the phase exit gate.

**V-01 Scoring Protocol Contract:** Each phase contains THE SCORING PROTOCOL section
with TWO named artifacts:
- **Restate** (verbatim from PART 0.0B): the registry row for this phase
- **APPLICATION SENTENCE**: maps the generic threshold to this phase's anomaly evidence
  shape — must be phase-specific, must name what the threshold means concretely for
  this anomaly class; cannot be satisfied by the restate alone

A SCORING PROTOCOL section that includes only the restate is incomplete.

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B — Pre-Detection Commitment**
> Phase 3A evidence standard (verbatim from PART 0.0B): _____
> Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3A**

*Restate*: _____

*APPLICATION SENTENCE*: For invalid state transitions, strength ≥ 2 means: a specific
(OP-ID, from-S-ID, to-S-ID) triple where from-S-ID is not listed in OP-ID's Valid From
States, or to-S-ID is not listed in OP-ID's Valid To States — both the operation and the
disqualifying state must be named by ID; prose description of a transition pattern does
not qualify.

Score at discovery. Say aloud: "I am scoring this [1/2/3] because [specific OP-ID,
from-S-ID, to-S-ID triple and the registry column that contradicts it]."
Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions.
If no finding: name specific (OP-ID, S-ID) pairs examined and cleared.

**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps.
If no finding: name specific steps and state-IDs examined and cleared.

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|
| | | | | | | |

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
☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific (not a restate paraphrase)

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim from PART 0.0B):
> Phase 3B: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3B**

*Restate*: _____

*APPLICATION SENTENCE*: For missing precondition checks, strength ≥ 2 means: a specific
(OP-ID, Step-N) pair where either (a) a precondition declared in the OP registry is
absent from the step's "Preconditions checked" list, or (b) a precondition appears with
verdict MET when the before-state field values should have produced NOT MET — the
operation, step number, and the specific precondition text must all be named.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID, Step-N, precondition
text, and why the verdict is wrong]." Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan OP-Registry for absent, underdefined, or
overlapping preconditions that could produce a false MET verdict.
If no finding: name specific OP-IDs and precondition cells examined and cleared.

**Pass 2: Trace-Diff** — scan PART 2 steps for: precondition NOT MET but operation PASS;
missing precondition entries; REJECTED guard text referencing different condition than
OP-Registry preconditions.
If no finding: name specific steps and precondition rows examined and cleared.

**Finding Table — Phase 3B**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|
| | | | | | | |

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
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields populated  ☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim from PART 0.0B):
> Phase 3C: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3C**

*Restate*: _____

*APPLICATION SENTENCE*: For invariant violations, strength ≥ 2 means: a specific
(INV-ID, Step-N) pair where the step's after-state field value crosses the numeric or
temporal threshold declared for INV-ID in 1C — the threshold value, the actual
after-state value, and the step number must all be named; an invariant that could
theoretically be breached does not qualify without the specific after-state values.

Score at discovery. "I am scoring this [1/2/3] because [INV-ID, threshold, Step-N
after-state value that crosses it]." Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan INV + OP for postconditions that could breach a
declared numeric or temporal threshold; check cumulative-transition breaches not visible
from any single operation.
If no finding: name specific (INV-ID, OP-ID) pairs examined and cleared.

**Pass 2: Trace-Diff** — scan PART 2 after-states against INV thresholds; check
adjacent step pairs where delta across two after-states crosses a threshold; check
postconditions marked VIOLATED.
If no finding: name specific steps and INV-IDs examined and cleared.

**Finding Table — Phase 3C**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|
| | | | | | | |

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
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields populated  ☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim from PART 0.0B):
> Phase 3D: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3D**

*Restate*: _____

*APPLICATION SENTENCE*: For race conditions, strength ≥ 2 means: a specific
(OP-ID-A, OP-ID-B, shared-S-ID) triple with a named anomalous after-state that
appears under one interleaving (A-then-B or B-then-A mid-operation) but not under
either fully-sequential ordering — both sequential orderings must be contrasted
against the interleaved outcome; a scenario that could cause problems does not
qualify without the contrasted after-states named.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID-A, OP-ID-B, the
interleaving, and the anomalous after-state vs both sequential outcomes]."
Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — identify OP-ID pairs sharing at least one Valid From
State; construct the concurrent interleaving scenario; describe anomalous outcome vs
sequential execution.
If no finding: name OP-ID pairs constructed and why concurrent execution converges.

**Pass 2: Trace-Diff** — select two steps from PART 2 executing from same or
overlapping states, or modifying the same field; construct concurrent interleaving;
compare concurrent after-state to both sequential orderings.
If no finding: name step pairs constructed and the after-state comparison result.

**Finding Table — Phase 3D**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|
| | | | | | | |

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
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields populated  ☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References — Entity-Type-Stratified

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

Phase 3E is a full structural peer of Phases 3A–3D. It receives the complete phase
mechanics including THE SCORING PROTOCOL with APPLICATION SENTENCE.

**Role B — Pre-Detection Commitment** (verbatim from PART 0.0B):
> Phase 3E: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3E**

*Restate*: _____

*APPLICATION SENTENCE*: For undeclared references, strength ≥ 1 means: the specific
registry cell (e.g., "1B row OP-03, Valid From States column") that contains the
reference, AND the specific ID that is absent from its target registry (e.g., "S-06
does not appear in 1A") — both the source cell and the missing target must be named
by location; a statement that "references may be missing" does not qualify.

Score at discovery. "I am scoring this [1/2/3] because [registry cell, referenced ID,
target registry, and confirmation the ID is absent]." Incomplete = not recordable.

**Pass 1: Declaration-Only — Three Independent Sub-Scans**

**Sub-scan P1-S: S-ID References**
Examine 1B Valid From States and Valid To States columns; 1C Scope column.
Does every S-ID cited appear as a declared row in 1A?
If no finding: list each cell checked and confirm S-ID resolution.

**Sub-scan P1-O: OP-ID References**
Examine 1C description and threshold fields; 1B precondition/postcondition
cross-operation references.
Does every OP-ID cited appear as a declared row in 1B?
If no finding: list each cell checked and confirm OP-ID resolution.

**Sub-scan P1-I: INV-ID References**
Examine 1B preconditions and postconditions; 1A entry and exit conditions.
Does every INV-ID cited appear as a declared row in 1C?
If no finding: list each cell checked and confirm INV-ID resolution.

**Pass 2: Trace-Diff — Three Independent Sub-Scans**

**Sub-scan P2-S:** Scan PART 2 step Before/After state fields and Phases 3A–3D S-ID cells.
Does every S-ID resolve to a 1A row? If no finding: list steps and S-IDs checked.

**Sub-scan P2-O:** Scan PART 2 step header OP-IDs and Phases 3A–3D OP-ID cells.
Does every OP-ID resolve to a 1B row? If no finding: list steps and OP-IDs checked.

**Sub-scan P2-I:** Scan PART 2 postcondition VIOLATED notes and Phases 3A–3D INV-ID cells.
Does every INV-ID resolve to a 1C row? If no finding: list entries and INV-IDs checked.

**Finding Table — Phase 3E**

Each row is an independent sweep unit. A verdict in one row does NOT satisfy another row.

| Entity Class | Declaration-Only Finding (P1 sub-scan) | Trace-Diff Finding (P2 sub-scan) | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|-------------|----------------------------------------|----------------------------------|-------|------|--------|--------------------------|
| S-ID references | | | — | | — | |
| OP-ID references | | | | — | — | |
| INV-ID references | | | — | — | | |

*A "None" in any cell requires an inline statement of what was checked and confirmed absent.*
*A finding in one row does not satisfy another row's sweep requirement.*

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

The Examined field must cover all three entity classes separately.

| Field | Content |
|-------|---------|
| Examined | [S-ID class: cells checked / OP-ID class: cells checked / INV-ID class: cells checked] |
| Evidence Standard Applied | |
| What Was Not Found | [Per entity class — S-ID: ___ / OP-ID: ___ / INV-ID: ___] |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

**Phase 3E Exit Certification**
☐ Findings List gate — all three entity-class rows populated with verdicts
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1 in any row, OR Gap Record covers all three entity classes
☐ Gap Record gate — all 5 template fields populated; Examined field covers all three entity classes
☐ Scoring Protocol gate — APPLICATION SENTENCE present and names the specific registry-cell + missing-ID evidence shape

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-01 prompt body.*

---
---

## V-02: Lifecycle Emphasis — Phase 3E 6-Row Finding Table (P1 and P2 Independently Stratified)

**Variation axis**: Lifecycle emphasis — Phase 3E's finding table is restructured from
3 rows (one per entity class, with Declaration-Only and Trace-Diff as columns) to 6 rows
(one per sub-scan: P1-S, P1-O, P1-I, P2-S, P2-O, P2-I). Each sub-scan row is an
independent sweep unit. A Pass 2 verdict cannot be satisfied by a Pass 1 row result.
A P2-O finding does not satisfy P2-S or P2-I.

**Hypothesis**: The R13 V-02 finding table has 3 entity-class rows each with a
"Trace-Diff Finding (Pass P2)" column. A model executing Phase 3E can fill the P2 column
of the S-ID row with a substantive finding, leave the P2 column cells for OP-ID and
INV-ID blank or as "None" (inline), and declare Phase 3E complete because the phase gate
reads "≥ 1 finding at strength ≥ 1 in any entity class." The P2-O and P2-I sub-scans
are never independently verified — the passing S-ID row absorbs the gate check. Splitting
Pass 2 into its own set of rows (P2-S, P2-O, P2-I) gives each P2 sub-scan an independent
verdict cell that must be populated and is detectable by row inspection.

**Target gaps**: C-43

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

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record explains why |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and anomalous outcome not present sequentially | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch per entity class (S-ID, OP-ID, or INV-ID) absent from its registry | ≥ 1 | ≥ 1 finding at strength ≥ 1 in any sub-scan row, OR Gap Record covers all six sub-scan rows |

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

**V-02 ID Contract:** Phases 3A–3D use three separate ID columns (OP-ID, S-ID, INV-ID).
Phase 3E uses the 6-row sub-scan structure defined below.

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B — Pre-Detection Commitment** (restate 3A registry row verbatim):
> Phase 3A evidence standard: _____  /  Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL:** Score at discovery. Say: "I am scoring this [1/2/3] because
[specific reference]." Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions.
If no finding: name specific (OP-ID, S-ID) pairs examined and cleared.

**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps.
If no finding: name specific steps and state-IDs examined and cleared.

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|
| | | | | | | |

**Role B — Gap Record [UNCONDITIONAL]**
> Entries examined: _____  /  Evidence standard applied: _____
> What was not found: _____  /  What would constitute a finding: _____

**The Gap Record is the unlock signal for the Phase 3A exit gate.**

**Phase 3A Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record explains why  ☐ Gap Record gate

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim): Phase 3B: _____  /  Min: _____  /  Gate: _____
**THE SCORING PROTOCOL** — same as 3A.
**Pass 1: Declaration-Only** — scan OP-Registry for absent/underdefined preconditions. If no finding: name OP-IDs cleared.
**Pass 2: Trace-Diff** — scan steps for NOT MET → PASS or missing entries. If no finding: name steps cleared.

**Finding Table — Phase 3B**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]**
> Examined: _____  /  Standard: _____  /  Not found: _____  /  Would constitute: _____

The Gap Record is the unlock signal for the Phase 3B exit gate.

**Phase 3B Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim): Phase 3C: _____  /  Min: _____  /  Gate: _____
**THE SCORING PROTOCOL** — same as 3A.
**Pass 1: Declaration-Only** — scan INV + OP for postconditions breaching thresholds. If no finding: name (INV-ID, OP-ID) pairs cleared.
**Pass 2: Trace-Diff** — scan after-states and adjacent pairs for cumulative breaches. If no finding: name steps and INV-IDs cleared.

**Finding Table — Phase 3C**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]**
> Examined: _____  /  Standard: _____  /  Not found: _____  /  Would constitute: _____

The Gap Record is the unlock signal for the Phase 3C exit gate.

**Phase 3C Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim): Phase 3D: _____  /  Min: _____  /  Gate: _____
**THE SCORING PROTOCOL** — same as 3A.
**Pass 1: Declaration-Only** — identify OP-ID pairs sharing Valid From States; construct concurrent scenario; describe anomalous outcome vs sequential. If no finding: name OP-ID pairs and convergence rationale.
**Pass 2: Trace-Diff** — construct step-pair interleaving; compare concurrent vs sequential after-state. If no finding: name step pairs and comparison result.

**Finding Table — Phase 3D**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL]**
> Examined: _____  /  Standard: _____  /  Not found: _____  /  Would constitute: _____

The Gap Record is the unlock signal for the Phase 3D exit gate.

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References — 6-Row Sub-Scan Table

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

**V-02 structure**: Phase 3E finding table has SIX independent rows — three for
Declaration-Only sub-scans (P1-S, P1-O, P1-I) and three for Trace-Diff sub-scans
(P2-S, P2-O, P2-I). Each row is an independent sweep unit. A verdict in any P2 row
cannot be satisfied by a P1 row of the same entity class. A verdict in P2-S cannot
satisfy P2-O or P2-I. All six rows must be populated for Phase 3E to close.

**Role B (Evidence Steward) — Pre-Detection Commitment**
Restate PART 0 registry row for Phase 3E verbatim:
> Phase 3E evidence standard: _____  /  Min strength: _____  /  Gate: _____

This commitment covers all six sub-scan rows. It cannot be adjusted after any sub-scan begins.

**THE SCORING PROTOCOL:**
Score at discovery. "I am scoring this [1/2/3] because [registry cell that contains
the reference, the referenced ID, and the target registry row that is absent]."
Incomplete sentence = not recordable.

---

**Pass 1 Sub-Scans: Declaration-Only**

**P1-S: S-ID Declaration-Only**
Examine: 1B Valid From States, Valid To States. Examine: 1C Scope column.
Question: Does every S-ID cited appear as a declared row in 1A?
If no finding: list each cell checked (e.g., "OP-01 Valid From States: S-01, S-02 —
both confirmed in 1A") and confirm each S-ID resolves.

**P1-O: OP-ID Declaration-Only**
Examine: 1C description and threshold fields for OP-ID references.
Examine: 1B preconditions/postconditions for cross-operation OP-ID references.
Question: Does every OP-ID cited appear as a declared row in 1B?
If no finding: list each cell checked and confirm each OP-ID resolves.

**P1-I: INV-ID Declaration-Only**
Examine: 1B preconditions and postconditions for INV-ID references.
Examine: 1A entry and exit conditions for INV-ID references.
Question: Does every INV-ID cited appear as a declared row in 1C?
If no finding: list each cell checked and confirm each INV-ID resolves.

---

**Pass 2 Sub-Scans: Trace-Diff**

**P2-S: S-ID Trace-Diff**
Scan every Before/After state field in PART 2 trace steps.
Scan S-ID cells in Phases 3A–3D finding tables.
Does every S-ID resolve to a declared row in 1A?
If no finding: list each trace step checked and confirm S-ID resolution.

**P2-O: OP-ID Trace-Diff**
Scan every step header OP-ID in PART 2 trace steps.
Scan OP-ID cells in Phases 3A–3D finding tables.
Does every OP-ID resolve to a declared row in 1B?
If no finding: list each trace step and finding table row checked.

**P2-I: INV-ID Trace-Diff**
Scan every Postcondition "VIOLATED" note in PART 2 for INV-ID references.
Scan INV-ID cells in Phases 3A–3D finding tables.
Does every INV-ID resolve to a declared row in 1C?
If no finding: list each trace step and finding table row checked.

---

**Finding Table — Phase 3E (6-Row Sub-Scan Structure)**

Each row is an independent sweep unit. A verdict in one row does NOT satisfy any other row.
All six rows must be populated for Phase 3E sweep to be complete.

| Sub-Scan ID | Pass | Entity Class | Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|------|-------------|---------|-------|------|--------|--------------------------|
| P1-S | Declaration-Only | S-ID | | — | | — | |
| P1-O | Declaration-Only | OP-ID | | | — | — | |
| P1-I | Declaration-Only | INV-ID | | — | — | | |
| P2-S | Trace-Diff | S-ID | | — | | — | |
| P2-O | Trace-Diff | OP-ID | | | — | — | |
| P2-I | Trace-Diff | INV-ID | | — | — | | |

*A blank row = incomplete Phase 3E sweep, independent of other rows.*
*A finding in P1-S does NOT satisfy P2-S, P1-O, or any other row.*
*A finding in P2-S does NOT satisfy P2-O or P2-I.*

---

**Role B (Evidence Steward) — Gap Record [UNCONDITIONAL]**

> Gap Record 3E:
> Sub-scans executed: P1-S, P1-O, P1-I, P2-S, P2-O, P2-I (all six)
> Registries checked per sub-scan: _____
> Trace steps and finding tables audited per P2 sub-scan: _____
> Specific cross-references confirmed present:
>   P1-S: _____  /  P1-O: _____  /  P1-I: _____
>   P2-S: _____  /  P2-O: _____  /  P2-I: _____
> Why absence of additional findings per sub-scan is credible: _____

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

**Phase 3E Exit Certification**
☐ Findings List gate — all six sub-scan rows populated with verdicts
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1 in any row, OR Gap Record covers all six sub-scan rows
☐ Gap Record gate — Gap Record lists all six sub-scan IDs with coverage confirmation

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-02 prompt body.*

---
---

## V-03: Role Sequence — Application Sentences Pre-Declared by Role B in PART 0

**Variation axis**: Role sequence — Role B's PART 0 responsibilities are expanded to
include a 0C section: Application Sentence Pre-Declaration. Before standards are sealed,
Role B declares the concrete meaning of the evidence threshold for each of the five
phases. These application sentences are sealed as part of PART 0 and cannot be revised
after Phase 3A begins. At each phase, Role B's pre-detection commitment has a Line 2
that references the sealed application sentence: "Applying the PART 0.0C application
sentence for this phase: [verbatim from 0C]."

**Hypothesis**: V-01 requires the application sentence to appear inline in each phase's
SCORING PROTOCOL at the time the phase runs. This creates a per-phase opportunity to
adjust the sentence: a model running Phase 3D can write a vague application sentence
without violating V-01's structural requirement (the sentence is present). Sealing all
five application sentences in PART 0 before any analysis begins — the same mechanism
C-38 uses for evidence standards — closes the post-hoc adjustment window. A model cannot
see what findings emerge in Phase 3A before committing to what strength ≥ 2 means for
Phase 3A invalid state transitions. The phase-order lock is the enforcement mechanism,
not the presence-of-sentence check.

**Target gaps**: C-42

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or
**Finance**. Choose the domain that best fits the scenario you are given. Your task is to
hand-compile state transitions, identify anomalies, and produce a structured trace-state
report. You play two roles throughout:

- **Role A (Anomaly Finder)**: runs detection passes and records findings
- **Role B (Evidence Steward)**: in PART 0, declares the Gap Record template, seals the
  evidence standards, AND declares concrete application sentences for all five phases
  before any analysis begins; at each phase, references the sealed application sentence
  in the pre-detection commitment; produces an unconditional structured Gap Record after
  each phase

---

### PART 0: PRE-GAME SEAL

Role B executes all three sections before PART 1 opens. All three are sealed together.

**0A: Role B — Gap Record Template Declaration**

```
GAP RECORD TEMPLATE (declared by Role B, pre-game):

| Field                           | Instruction |
|--------------------------------|-------------|
| Examined                       | List each OP-ID, S-ID, INV-ID, trace step, or registry cell
|                                | examined. "All entries" is not acceptable — name each one. |
| Evidence Standard Applied      | Copy verbatim from PART 0.0B registry row for this phase. |
| What Was Not Found             | Name the specific anomaly type and IDs absent — "No
|                                | violations found" is not acceptable. |
| What Would Constitute a Finding | Minimum evidence to trigger a finding in this phase —
|                                | phase-specific, must name the trace-step pattern or
|                                | registry condition, not a generic description. |
| Verdict                        | Acquitted — no qualifying evidence exists
|                                |   OR Partial — finding below threshold: [specify] |
```

**Role B declaration**: This template governs all Gap Records. A Gap Record with any
blank field is a structural failure and does not unlock the phase exit gate.

**0B: Standards Registry**

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record "Verdict" explains why |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and anomalous outcome not present sequentially | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch per entity class absent from its registry | ≥ 1 | ≥ 1 finding at strength ≥ 1 in any entity class, OR Gap Record covers all three classes |

**0C: Role B — Application Sentence Pre-Declaration**

Before any data is declared in PART 1, Role B commits to the concrete meaning of the
evidence threshold for each phase. These sentences cannot be revised after PART 0 is
sealed. At each phase, Role B will reference this table verbatim.

| Phase | Anomaly Type | Application Sentence — What strength ≥ N means for this specific anomaly class |
|-------|-------------|---------------------------------------------------------------------------------|
| 3A | Invalid state transitions | For invalid state transitions, strength ≥ 2 means: a specific (OP-ID, from-S-ID, to-S-ID) triple where from-S-ID is not listed in OP-ID's Valid From States or to-S-ID is not listed in Valid To States — all three IDs must be named; prose description without IDs does not qualify. |
| 3B | Missing precondition checks | For missing precondition checks, strength ≥ 2 means: a specific (OP-ID, Step-N) pair where a declared precondition is absent from the step's Preconditions checked list, or appears as MET when before-state field values require NOT MET — the OP-ID, step number, and precondition text must all be named. |
| 3C | Invariant violations | For invariant violations, strength ≥ 2 means: a specific (INV-ID, Step-N) pair where the step's after-state field value crosses the numeric or temporal threshold in 1C — the threshold value, the actual after-state value, and the step number must all be named. |
| 3D | Race conditions | For race conditions, strength ≥ 2 means: a specific (OP-ID-A, OP-ID-B, shared-S-ID) triple with a named anomalous after-state under one interleaving not present in either sequential ordering — both sequential orderings must be contrasted against the interleaved outcome by name. |
| 3E | Undeclared references | For undeclared references, strength ≥ 1 means: the specific registry cell (e.g., "1B row OP-03, Valid From States") containing the reference, and the specific absent ID (e.g., "S-06 not in 1A") — both source cell and missing target must be named by location. |

**Role B declaration**: These application sentences are sealed. I cannot revise them
after PART 0 closes. At each phase I will reference this table in the pre-detection
commitment before any pass begins.

**PART 0 SEALED (0A template + 0B standards + 0C application sentences) → PART 1 now OPEN.**

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
At each phase, Role B's commitment block has THREE lines:
- Line 1: restate the PART 0.0B standards row verbatim
- Line 2: restate the PART 0.0C application sentence for this phase verbatim
- Line 3: "I confirm: the Phase N Gap Record will use the PART 0.0A template. A blank field does not unlock the exit gate."

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim from PART 0.0B): Phase 3A: _____  /  Min: _____  /  Gate: _____
> Application sentence (verbatim from PART 0.0C): _____
> Template confirmation: I confirm the Phase 3A Gap Record will use the PART 0.0A template.

**THE SCORING PROTOCOL:** Score at discovery. "I am scoring this [1/2/3] because [specific reference matching the 0C application sentence criteria for Phase 3A]." Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions.
If no finding: name specific (OP-ID, S-ID) pairs examined and cleared.

**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps.
If no finding: name specific steps and state-IDs examined and cleared.

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|
| | | | | | | |

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
☐ Application Sentence gate — pre-detection commitment Line 2 is the PART 0.0C sentence verbatim

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim from PART 0.0B): Phase 3B: _____  /  Min: _____  /  Gate: _____
> Application sentence (verbatim from PART 0.0C): _____
> Template confirmation: I confirm the Phase 3B Gap Record will use the PART 0.0A template.

**THE SCORING PROTOCOL** — same as 3A; score against 0C sentence for Phase 3B.
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

The Gap Record is the unlock signal for the Phase 3B exit gate.

**Phase 3B Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields populated  ☐ Application Sentence gate

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim from PART 0.0B): Phase 3C: _____  /  Min: _____  /  Gate: _____
> Application sentence (verbatim from PART 0.0C): _____
> Template confirmation: I confirm the Phase 3C Gap Record will use the PART 0.0A template.

**THE SCORING PROTOCOL** — score against 0C sentence for Phase 3C.
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

The Gap Record is the unlock signal for the Phase 3C exit gate.

**Phase 3C Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate  ☐ Application Sentence gate

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim from PART 0.0B): Phase 3D: _____  /  Min: _____  /  Gate: _____
> Application sentence (verbatim from PART 0.0C): _____
> Template confirmation: I confirm the Phase 3D Gap Record will use the PART 0.0A template.

**THE SCORING PROTOCOL** — score against 0C sentence for Phase 3D.
**Pass 1: Declaration-Only** — identify OP-ID pairs sharing Valid From States; construct concurrent scenario. If no finding: name OP-ID pairs and convergence rationale.
**Pass 2: Trace-Diff** — construct step-pair interleaving; compare concurrent vs sequential. If no finding: name step pairs and comparison result.

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

The Gap Record is the unlock signal for the Phase 3D exit gate.

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate  ☐ Application Sentence gate

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim from PART 0.0B): Phase 3E: _____  /  Min: _____  /  Gate: _____
> Application sentence (verbatim from PART 0.0C): _____
> Template confirmation: I confirm the Phase 3E Gap Record will use the PART 0.0A template.
>   The Examined field must cover all three entity classes (S-ID, OP-ID, INV-ID).

**THE SCORING PROTOCOL** — score against 0C sentence for Phase 3E.

**Pass 1: Declaration-Only — Three Independent Sub-Scans (P1-S, P1-O, P1-I)**
*P1-S*: Examine 1B Valid From/To; 1C Scope. Does every S-ID cited appear in 1A? Name each cleared.
*P1-O*: Examine 1C descriptions; 1B cross-op references. Does every OP-ID cited appear in 1B? Name each cleared.
*P1-I*: Examine 1B preconditions/postconditions; 1A entry/exit. Does every INV-ID cited appear in 1C? Name each cleared.

**Pass 2: Trace-Diff — Three Independent Sub-Scans (P2-S, P2-O, P2-I)**
*P2-S*: Scan PART 2 Before/After states and 3A–3D S-ID cells. Name each step checked.
*P2-O*: Scan PART 2 step OP-IDs and 3A–3D OP-ID cells. Name each step checked.
*P2-I*: Scan PART 2 VIOLATED postconditions and 3A–3D INV-ID cells. Name each entry checked.

**Finding Table — Phase 3E**

| Entity Class | Declaration-Only Finding (P1 sub-scan) | Trace-Diff Finding (P2 sub-scan) | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|-------------|----------------------------------------|----------------------------------|-------|------|--------|--------------------------|
| S-ID references | | | — | | — | |
| OP-ID references | | | | — | — | |
| INV-ID references | | | — | — | | |

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

The Examined field must cover all three entity classes.

| Field | Content |
|-------|---------|
| Examined | [S-ID class: ___ / OP-ID class: ___ / INV-ID class: ___] |
| Evidence Standard Applied | |
| What Was Not Found | [S-ID: ___ / OP-ID: ___ / INV-ID: ___] |
| What Would Constitute a Finding | |
| Verdict | |

The Gap Record is the unlock signal for the Phase 3E exit gate.

**Phase 3E Exit Certification**
☐ Findings List gate — all three entity-class rows populated
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1 in any row, OR Gap Record covers all three classes
☐ Gap Record gate — all 5 fields populated; Examined covers all three entity classes
☐ Application Sentence gate — pre-detection commitment Line 2 is the PART 0.0C sentence verbatim

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-03 prompt body.*

---
---

## V-04: Compound — Application Sentence + 6-Row Phase 3E Finding Table

**Variation axis**: Compound — output format + lifecycle emphasis. Combines V-01's
named APPLICATION SENTENCE in each phase's scoring protocol with V-02's 6-row Phase 3E
finding table (P1-S, P1-O, P1-I, P2-S, P2-O, P2-I as independent rows).

**Hypothesis**: C-42 and C-43 are independent structural requirements. C-42 governs the
phase-level scoring protocol (present in all five phases). C-43 governs the Phase 3E
finding table structure (Pass 2 stratification). Neither implies the other. A variation
that addresses only C-42 leaves the P2 stratification gap. A variation that addresses
only C-43 leaves the application sentence gap. The compound variation closes both.
C-42's application sentence provides the evaluator's pre-stated interpretation of the
threshold before any finding is recorded. C-43's 6-row table makes absent P2 sub-scans
detectable by blank row rather than buried in a shared column.

**Target gaps**: C-42 + C-43

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

Every Gap Record uses this 5-field template. A Gap Record missing any field is a
structural failure and does not unlock the phase exit gate.

```
| Field                           | Content |
|--------------------------------|---------|
| Examined                       | [Specific IDs, trace steps, registry cells — named individually] |
| Evidence Standard Applied      | [Verbatim from PART 0.0B registry row for this phase] |
| What Was Not Found             | [Specific absence: anomaly type + IDs — "No violations found" not acceptable] |
| What Would Constitute a Finding | [Phase-specific minimum evidence — must name trace-step pattern or registry condition] |
| Verdict                        | Acquitted / Partial — [if partial: specify finding and why it did not qualify] |
```

**0B: Standards Registry**

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record "Verdict" explains why |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and anomalous outcome not present sequentially | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch per entity class absent from its registry | ≥ 1 | ≥ 1 finding at strength ≥ 1 in any sub-scan row, OR Gap Record covers all six sub-scan rows |

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

**V-04 ID Contract:** Phases 3A–3D use three separate ID columns (OP-ID, S-ID, INV-ID).
Phase 3E uses the 6-row sub-scan structure.

**V-04 Gap Record Contract:** All Gap Records use the 5-field PART 0.0A template.
The Gap Record is the unlock signal for the phase exit gate.

**V-04 Scoring Protocol Contract:** THE SCORING PROTOCOL in each phase includes:
- *Restate*: verbatim from PART 0.0B
- *APPLICATION SENTENCE*: phase-specific concrete meaning of the threshold for this
  anomaly class — must name the evidence shape, not paraphrase the registry row

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B — Pre-Detection Commitment** (verbatim from PART 0.0B):
> Phase 3A: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3A**

*Restate*: _____

*APPLICATION SENTENCE*: For invalid state transitions, strength ≥ 2 means: a specific
(OP-ID, from-S-ID, to-S-ID) triple where from-S-ID is not in OP-ID's Valid From States,
or to-S-ID is not in OP-ID's Valid To States — all three IDs named; prose description
without specific IDs does not qualify.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID, from-S-ID, to-S-ID and
which registry column contradicts the transition]." Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions.
If no finding: name specific (OP-ID, S-ID) pairs examined and cleared.

**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps.
If no finding: name specific steps and state-IDs examined and cleared.

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|
| | | | | | | |

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
☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim): Phase 3B: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3B**

*Restate*: _____

*APPLICATION SENTENCE*: For missing precondition checks, strength ≥ 2 means: a specific
(OP-ID, Step-N) pair where a declared precondition is absent from the step's
Preconditions checked list, or appears MET when before-state values require NOT MET —
OP-ID, step number, and precondition text must all be named.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID, Step-N, precondition text, and verdict mismatch]." Incomplete = not recordable.

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
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields populated  ☐ Scoring Protocol gate

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim): Phase 3C: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3C**

*Restate*: _____

*APPLICATION SENTENCE*: For invariant violations, strength ≥ 2 means: a specific
(INV-ID, Step-N) pair where the step's after-state field value crosses the numeric or
temporal threshold declared for INV-ID — the threshold value, actual after-state value,
and step number must all be named.

Score at discovery. "I am scoring this [1/2/3] because [INV-ID, threshold, Step-N after-state value]." Incomplete = not recordable.

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
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields  ☐ Scoring Protocol gate

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim): Phase 3D: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3D**

*Restate*: _____

*APPLICATION SENTENCE*: For race conditions, strength ≥ 2 means: a specific
(OP-ID-A, OP-ID-B, shared-S-ID) triple with a named anomalous after-state under one
interleaving not present in either sequential ordering — both sequential orderings must
be contrasted against the interleaved outcome by name.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID-A, OP-ID-B, the interleaving, anomalous vs sequential outcomes]." Incomplete = not recordable.

**Pass 1: Declaration-Only** — identify OP-ID pairs sharing Valid From States; construct concurrent scenario. If no finding: name OP-ID pairs and convergence rationale.
**Pass 2: Trace-Diff** — construct step-pair interleaving; compare concurrent vs sequential. If no finding: name step pairs and comparison result.

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
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields  ☐ Scoring Protocol gate

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References — Application Sentence + 6-Row Sub-Scan Table

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim from PART 0.0B):
> Phase 3E: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3E**

*Restate*: _____

*APPLICATION SENTENCE*: For undeclared references, strength ≥ 1 means: the specific
registry cell (e.g., "1B row OP-03, Valid From States") that contains the reference,
and the specific absent ID (e.g., "S-06 not in 1A") — both source cell and missing
target must be named by location; "references may exist" does not qualify.

Score at discovery. "I am scoring this [1/2/3] because [registry cell, referenced ID, target registry, absence confirmation]." Incomplete = not recordable.

---

**Pass 1 Sub-Scans: Declaration-Only**

**P1-S:** Examine 1B Valid From/To; 1C Scope. Does every S-ID cited appear in 1A?
If no finding: list each cell checked and confirm S-ID resolution.

**P1-O:** Examine 1C descriptions/thresholds; 1B cross-op references. Does every OP-ID cited appear in 1B?
If no finding: list each cell checked and confirm OP-ID resolution.

**P1-I:** Examine 1B preconditions/postconditions; 1A entry/exit. Does every INV-ID cited appear in 1C?
If no finding: list each cell checked and confirm INV-ID resolution.

**Pass 2 Sub-Scans: Trace-Diff**

**P2-S:** Scan PART 2 Before/After states and 3A–3D S-ID cells. Does every S-ID resolve to 1A?
If no finding: list each step checked and confirm resolution.

**P2-O:** Scan PART 2 step OP-IDs and 3A–3D OP-ID cells. Does every OP-ID resolve to 1B?
If no finding: list each step and finding table row checked.

**P2-I:** Scan PART 2 VIOLATED postconditions and 3A–3D INV-ID cells. Does every INV-ID resolve to 1C?
If no finding: list each entry checked and confirm resolution.

---

**Finding Table — Phase 3E (6-Row Sub-Scan Structure)**

All six rows must be populated. A verdict in any row does NOT satisfy any other row.
P2 row verdicts are independent of P1 row verdicts for the same entity class.

| Sub-Scan ID | Pass | Entity Class | Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|------|-------------|---------|-------|------|--------|--------------------------|
| P1-S | Declaration-Only | S-ID | | — | | — | |
| P1-O | Declaration-Only | OP-ID | | | — | — | |
| P1-I | Declaration-Only | INV-ID | | — | — | | |
| P2-S | Trace-Diff | S-ID | | — | | — | |
| P2-O | Trace-Diff | OP-ID | | | — | — | |
| P2-I | Trace-Diff | INV-ID | | — | — | | |

*Blank row = incomplete sweep, independent of other rows.*
*P1-S PASS does NOT satisfy P2-S. P2-S PASS does NOT satisfy P2-O or P2-I.*

---

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

The Examined field must cover all six sub-scans.

| Field | Content |
|-------|---------|
| Examined | [P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| Evidence Standard Applied | |
| What Was Not Found | [Per sub-scan — P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

**Phase 3E Exit Certification**
☐ Findings List gate — all six sub-scan rows populated
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1 in any row, OR Gap Record covers all six rows
☐ Gap Record gate — all 5 fields populated; Examined covers all six sub-scans
☐ Scoring Protocol gate — APPLICATION SENTENCE present and names source-cell + missing-target evidence shape

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-04 prompt body.*

---
---

## V-05: Compound — Application Sentence + 6-Row Table + Imperative Phrasing + PART 5

**Variation axis**: Compound — output format + lifecycle emphasis + phrasing register.
All of V-04 (C-42 application sentence + C-43 6-row Phase 3E table) plus imperative
command phrasing with STOP/MUST/ADVANCE markers, and PART 5 post-sweep C/FP/FN
reconciliation (C-21, C-25).

**Hypothesis**: The application sentence requirement and the 6-row Phase 3E table add
structural obligations. The phrasing register affects whether the model treats them as
obligations or as recommendations it can satisfy minimally. Imperative phrasing with
STOP markers at each APPLICATION SENTENCE and each Phase 3E sub-scan row forces the
model to treat these as blocking requirements rather than checkboxes. PART 5 closes the
C-21/C-25 criteria: the three-value C/FP/FN taxonomy tests whether the application
sentences were well-calibrated (a False Negative on Phase 3A with a stated APPLICATION
SENTENCE is more diagnostic than a False Negative without one — the sentence now serves
as evidence of miscalibration, not just absence).

**Target gaps**: C-42 + C-43 (primary); C-21 + C-25 (secondary via PART 5)

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or
**Finance**. Choose the domain that best fits the scenario you are given. Your task is to
hand-compile state transitions, identify anomalies, and produce a structured trace-state
report. You play two roles:

- **Role A (Anomaly Finder)**: runs detection passes, records findings, executes PART 5
  post-sweep reconciliation
- **Role B (Evidence Steward)**: declares Gap Record template and evidence standards
  in PART 0; at each phase issues the pre-detection commitment with APPLICATION SENTENCE;
  produces an unconditional structured Gap Record after each phase

---

### PART 0: STANDARDS REGISTRY AND GAP RECORD TEMPLATE

**0A: Gap Record Template** (sealed — cannot be revised after PART 0 closes)

```
| Field                           | Content |
|--------------------------------|---------|
| Examined                       | MUST name each OP-ID, S-ID, INV-ID, trace step, or registry
|                                | cell examined individually. "All entries" FAILS this gate. |
| Evidence Standard Applied      | MUST copy verbatim from PART 0.0B registry row. |
| What Was Not Found             | MUST name specific anomaly type and IDs. "No violations
|                                | found" FAILS this gate. |
| What Would Constitute a Finding | MUST name the phase-specific trace-step pattern or
|                                | registry condition. Generic description FAILS this gate. |
| Verdict                        | MUST choose: Acquitted / Partial — [if Partial: specify
|                                | finding and why threshold not met] |
```

**0B: Standards Registry**

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record "Verdict" explains why |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and anomalous outcome not present sequentially | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch per entity class absent from its registry | ≥ 1 | ≥ 1 finding at strength ≥ 1 in any sub-scan row, OR Gap Record covers all six rows |

**PART 0 SEALED → PART 1 now OPEN.**

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

MUST produce minimum 6 numbered steps. MUST include at least one `[REJECTED]` step.

```
Step N: [OP-ID] [Operation Name]  [PASS / REJECTED]
  Before state:   [S-ID] [State Name] — { field: value, ... }
  Preconditions checked:
    - [text]: MET / NOT MET
  Guard condition: passes — continue  /  fires — reason: [text]
  After state:    [S-ID] [State Name] — { field: value, ... }
    [REJECTED STEPS: The entity MUST remain in its before-state after rejection.
     After state MUST equal before state field-for-field.
     Any deviation IS a detectable anomaly. Document it as a finding in Phase 3A.]
  Postconditions verified:
    - [text]: HOLDS / VIOLATED
```

---

### PART 3: PRE-SWEEP HYPOTHESIS

MUST record predictions before PART 4 begins. This table is LOCKED once Phase 3A opens.

| Phase | Anomaly Type | Predicted Count | Confidence (L/M/H) | Specific Predicted Scenario |
|-------|-------------|-----------------|--------------------|-----------------------------|
| 3A | Invalid state transitions | | | |
| 3B | Missing precondition checks | | | |
| 3C | Invariant violations | | | |
| 3D | Race conditions | | | |
| 3E | Undeclared references | | | |

---

### PART 4: ANOMALY SWEEP

**STOP — before entering any phase, confirm:**
- PART 0 is sealed (both 0A template and 0B standards present)
- PART 3 predictions are recorded
- PART 1 registries have minimum entries (4 states, 5 operations, 2 invariants with ≥1 numeric/temporal)

**ID Contract (all phases):** Three separate ID columns (OP-ID, S-ID, INV-ID) in all
finding tables. A blank ID column cell in a found-verdict row IS a structural error.

**Gap Record Contract (all phases):** MUST use PART 0.0A 5-field template.
The Gap Record IS the unlock signal — a structurally incomplete Gap Record blocks the exit gate.

**Scoring Protocol Contract (all phases):** THE SCORING PROTOCOL MUST contain:
1. *Restate* — verbatim from PART 0.0B
2. *APPLICATION SENTENCE* — phase-specific evidence shape for this anomaly class
   The APPLICATION SENTENCE MUST NOT be a paraphrase of the restate.
   A SCORING PROTOCOL without an APPLICATION SENTENCE FAILS the Scoring Protocol gate.

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**STOP — Role B MUST complete pre-detection commitment before Pass 1 begins.**

**Role B — Pre-Detection Commitment**
> Standards (verbatim from PART 0.0B): _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3A** *(MUST include both artifacts below)*

*Restate*: _____

*APPLICATION SENTENCE*: For invalid state transitions, strength ≥ 2 means: a specific
(OP-ID, from-S-ID, to-S-ID) triple where from-S-ID is not in OP-ID's Valid From States,
or to-S-ID is not in OP-ID's Valid To States — all three IDs MUST be named; prose
without specific IDs FAILS the strength ≥ 2 threshold.

**STOP — confirm APPLICATION SENTENCE is above before proceeding to Pass 1.**

Score at discovery. MUST say: "I am scoring this [1/2/3] because [OP-ID, from-S-ID,
to-S-ID, and the registry column contradiction]." Cannot complete sentence = not recordable.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions.
MUST name specific (OP-ID, S-ID) pairs if no finding.

**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps.
MUST name specific steps and state-IDs if no finding.

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|
| | | | | | | |

**STOP — Role B MUST produce Gap Record before exit gate opens.**

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE — ALL FIELDS REQUIRED]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**ADVANCE only after Gap Record is structurally complete (no blank fields).**
**The Gap Record IS the unlock signal for the Phase 3A exit gate.**

**Phase 3A Exit Certification**
☐ Findings List gate
☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record "Verdict" explicitly explains why
☐ Gap Record gate — ALL 5 template fields populated; no placeholder text
☐ Scoring Protocol gate — APPLICATION SENTENCE present, phase-specific, not a restate paraphrase

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim): Phase 3B: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3B**

*Restate*: _____

*APPLICATION SENTENCE*: For missing precondition checks, strength ≥ 2 means: a specific
(OP-ID, Step-N) pair where a declared precondition is absent from the step's Preconditions
checked list, or appears MET when before-state field values require NOT MET — OP-ID, step
number, AND precondition text MUST all be named.

**STOP — confirm APPLICATION SENTENCE is above before proceeding to Pass 1.**

**Pass 1: Declaration-Only** — scan OP-Registry for absent/underdefined preconditions. MUST name OP-IDs if no finding.
**Pass 2: Trace-Diff** — scan steps for NOT MET → PASS or missing entries. MUST name steps if no finding.

**Finding Table — Phase 3B**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE — ALL FIELDS REQUIRED]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record IS the unlock signal for the Phase 3B exit gate.**

**Phase 3B Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — ALL 5 fields  ☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim): Phase 3C: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3C**

*Restate*: _____

*APPLICATION SENTENCE*: For invariant violations, strength ≥ 2 means: a specific
(INV-ID, Step-N) pair where the step's after-state field value crosses the numeric or
temporal threshold declared for INV-ID in 1C — the threshold value, actual after-state
value, AND step number MUST all be named; a threshold that could be crossed does not
qualify without the specific after-state values.

**STOP — confirm APPLICATION SENTENCE is above before proceeding to Pass 1.**

**Pass 1: Declaration-Only** — scan INV + OP for postconditions breaching thresholds. MUST name (INV-ID, OP-ID) pairs if no finding.
**Pass 2: Trace-Diff** — scan after-states and adjacent pairs for cumulative breaches. MUST name steps and INV-IDs if no finding.

**Finding Table — Phase 3C**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE — ALL FIELDS REQUIRED]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record IS the unlock signal for the Phase 3C exit gate.**

**Phase 3C Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — ALL 5 fields  ☐ Scoring Protocol gate

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim): Phase 3D: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3D**

*Restate*: _____

*APPLICATION SENTENCE*: For race conditions, strength ≥ 2 means: a specific
(OP-ID-A, OP-ID-B, shared-S-ID) triple with a named anomalous after-state that appears
under one interleaving but NOT under either sequential ordering — BOTH sequential
orderings MUST be contrasted against the interleaved outcome; a described interleaving
without the sequential contrasts FAILS the strength ≥ 2 threshold.

**STOP — confirm APPLICATION SENTENCE is above before proceeding to Pass 1.**

**Pass 1: Declaration-Only** — identify OP-ID pairs sharing Valid From States; construct concurrent scenario. MUST name OP-ID pairs if no finding.
**Pass 2: Trace-Diff** — construct step-pair interleaving; compare concurrent vs sequential. MUST name step pairs and comparison result if no finding.

**Finding Table — Phase 3D**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE — ALL FIELDS REQUIRED]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record IS the unlock signal for the Phase 3D exit gate.**

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — ALL 5 fields  ☐ Scoring Protocol gate

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References — Application Sentence + 6-Row Sub-Scan Table

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim from PART 0.0B):
> Phase 3E: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3E**

*Restate*: _____

*APPLICATION SENTENCE*: For undeclared references, strength ≥ 1 means: the specific
registry cell (e.g., "1B row OP-03, Valid From States") that contains the reference AND
the specific absent ID (e.g., "S-06 not in 1A") — BOTH source cell AND missing target
MUST be named by location; "references may exist" or "possible undeclared ID" FAILS
the strength ≥ 1 threshold.

**STOP — confirm APPLICATION SENTENCE is above before proceeding to P1-S.**

Score at discovery. MUST say: "I am scoring this [1/2/3] because [registry cell,
referenced ID, target registry, absence confirmation]." Incomplete = not recordable.

---

**Pass 1 Sub-Scans: Declaration-Only**
MUST execute each sub-scan independently. Do NOT combine.

**P1-S (STOP — execute fully before P1-O):**
Examine 1B Valid From States, Valid To States. Examine 1C Scope.
Question: Every S-ID cited → present in 1A?
MUST name each cell checked if no finding.

**P1-O (STOP — execute fully before P1-I):**
Examine 1C description/threshold fields. Examine 1B cross-op references.
Question: Every OP-ID cited → present in 1B?
MUST name each cell checked if no finding.

**P1-I:**
Examine 1B preconditions/postconditions. Examine 1A entry/exit conditions.
Question: Every INV-ID cited → present in 1C?
MUST name each cell checked if no finding.

---

**Pass 2 Sub-Scans: Trace-Diff**
MUST execute each sub-scan independently. P1 results do NOT satisfy P2 rows.

**P2-S (STOP — execute fully before P2-O):**
Scan PART 2 Before/After states AND 3A–3D S-ID cells.
Question: Every S-ID → present in 1A?
MUST name each step checked if no finding.

**P2-O (STOP — execute fully before P2-I):**
Scan PART 2 step OP-IDs AND 3A–3D OP-ID cells.
Question: Every OP-ID → present in 1B?
MUST name each step and finding table row checked if no finding.

**P2-I:**
Scan PART 2 VIOLATED postconditions AND 3A–3D INV-ID cells.
Question: Every INV-ID → present in 1C?
MUST name each entry checked if no finding.

---

**Finding Table — Phase 3E (6-Row Sub-Scan Structure)**

MUST populate ALL SIX rows. A blank row BLOCKS the Phase 3E exit gate.
P2 rows are independent of P1 rows. P2-O and P2-I are independent of P2-S.

| Sub-Scan ID | Pass | Entity Class | Finding (MUST be populated — "None" requires inline evidence of what was checked) | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|------|-------------|---|-------|------|--------|--------------------------|
| P1-S | Declaration-Only | S-ID | | — | | — | |
| P1-O | Declaration-Only | OP-ID | | | — | — | |
| P1-I | Declaration-Only | INV-ID | | — | — | | |
| P2-S | Trace-Diff | S-ID | | — | | — | |
| P2-O | Trace-Diff | OP-ID | | | — | — | |
| P2-I | Trace-Diff | INV-ID | | — | — | | |

---

**STOP — Role B MUST produce Gap Record before exit gate opens.**

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE — ALL FIELDS REQUIRED]**

The Examined field MUST cover all six sub-scans separately.

| Field | Content |
|-------|---------|
| Examined | [P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| Evidence Standard Applied | |
| What Was Not Found | [P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| What Would Constitute a Finding | |
| Verdict | |

**ADVANCE only after all six sub-scan entries are present in Examined and What Was Not Found.**
**The Gap Record IS the unlock signal for the Phase 3E exit gate.**

**Phase 3E Exit Certification**
☐ Findings List gate — ALL six sub-scan rows populated
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1 in any row, OR Gap Record covers all six rows
☐ Gap Record gate — ALL 5 fields; Examined and What Was Not Found name all six sub-scans
☐ Scoring Protocol gate — APPLICATION SENTENCE present, names source-cell + missing-target evidence shape, not a restate paraphrase

**PHASE 3E: COMPLETE [Sweep closed — ADVANCE to PART 5]**

---

### PART 5: POST-SWEEP RECONCILIATION

Role A compares PART 3 predictions against PART 4 findings using three-value taxonomy.

#### 5A: Reconciliation Table

| Phase | Predicted Count | Actual Count | Classification | Surprise | Calibration Note |
|-------|-----------------|--------------|----------------|----------|-----------------|
| 3A | | | C / FP / FN | Y / N | |
| 3B | | | C / FP / FN | Y / N | |
| 3C | | | C / FP / FN | Y / N | |
| 3D | | | C / FP / FN | Y / N | |
| 3E | | | C / FP / FN | Y / N | |

**Classification key:**
- **C** (Correct): predicted finding present with type matching, or predicted absence confirmed
- **FP** (False Positive): predicted finding not found
- **FN** (False Negative): finding discovered that was not predicted

#### 5B: Calibration Score

Calibration score = C / (C + FP + FN). Threshold: score < 0.6 triggers structural diagnosis.

Calibration score: ___  /  Threshold met: Y / N

If score < 0.6: identify which APPLICATION SENTENCE was most misaligned with the
actual evidence shape encountered. Revise the sentence for the domain scenario used —
do not revise retroactively in PART 4; record the revision here as a calibration artifact.

---

*End of V-05 prompt body.*
