Both files written. Here's the R16 variation map:

---

## R16 Variation Map

| V | Axis | Target | Key structural change |
|---|------|--------|-----------------------|
| V-01 | Output format | C-44 | `PHASE N: COMPLETE is BLOCKED until all four gates below are satisfied` opens every exit certification; Scoring Protocol gate names restate-only SCORING PROTOCOL as the specific blocking condition |
| V-02 | Lifecycle emphasis | C-45 | Named `ANTI-MASKING RULE` callout block in Phase 3E header before Role B pre-detection; exit certification titled "Exit gate requires all six sub-scan rows populated" with individual per-row checkboxes |
| V-03 | Role sequence | C-44 + C-45 | PART 0 gains `0C: Per-Phase Exit Contract` (seals 4-gate model) and `0D: Phase 3E Row Independence Contract` (seals anti-masking rule) — both pre-game before PART 1 opens |
| V-04 | Compound output + lifecycle | C-44 + C-45 | V-01 blocking language + V-02 ANTI-MASKING RULE + per-row Phase 3E checkboxes |
| V-05 | Compound + phrasing | C-44 + C-45 | V-04 + MUST/BLOCKED/ADVANCE imperative throughout + PART 5 C/FP/FN reconciliation with calibration score |

**Key hypotheses:**
- **V-01 vs V-03**: Does the blocking gate need to fire at each phase exit (V-01 — post-findings) or does pre-sealing the contract before PART 1 (V-03 — pre-game) provide stronger enforcement?
- **V-02**: Does a labeled `ANTI-MASKING RULE` block in the phase header satisfy C-45's "named constraint before detection begins" requirement better than the narrative row-independence text R15 V-02 used in the table footer?
*Single-axis hypotheses tested:**
- V-01 vs V-03: Does blocking framing at each gate invocation (V-01) achieve C-44 better than pre-sealing the 4-gate contract before PART 1 (V-03)? Pre-sealing closes the loophole where the model forms findings before committing to what "all four gates required" means.
- V-02: Does naming the anti-masking constraint as a labeled rule callout before detection — vs. narrative text in the table footer — enforce C-45's "explicit named constraint in the phase header" requirement?

---

## V-01: Output Format — Blocking APPLICATION SENTENCE Gate (C-44)

**Variation axis**: Output format — each phase exit certification opens with a blocking declaration: "PHASE N: COMPLETE is BLOCKED until all four gates below are satisfied." The Scoring Protocol gate entry explicitly states that a SCORING PROTOCOL containing only a verbatim restate of the registry row — without a separate APPLICATION SENTENCE — holds this gate OPEN and prevents PHASE N: COMPLETE. Phase 3E uses the 6-row sub-scan table (C-43 preserved). APPLICATION SENTENCE appears inline per phase (C-42 preserved).

**Hypothesis**: R15 V-01 placed the APPLICATION SENTENCE as a 4th checkbox. The checkbox is present but framing is neutral — the gate says "check this if satisfied." A model that omits the APPLICATION SENTENCE then encounters the 4th gate as an obstacle but there is no declared consequence for leaving it unchecked. Without "BLOCKED until" language at the gate header — parallel to how LOCKED/OPEN enforces phase sequencing — the gate is a presence check, not a structural hard stop. The blocking framing at the certification opener prevents treating it as optional.

**Target gaps**: C-44

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or **Finance**. Choose the domain that best fits the scenario you are given. Your task is to hand-compile state transitions, identify anomalies, and produce a structured trace-state report. You play two roles throughout:

- **Role A (Anomaly Finder)**: runs detection passes and records findings
- **Role B (Evidence Steward)**: locks evidence standards and Gap Record template before detection begins, then produces an unconditional structured Gap Record after each phase

---

### PART 0: STANDARDS REGISTRY AND GAP RECORD TEMPLATE

**0A: Gap Record Template**

Every Gap Record in this analysis uses the following 5-field template. A Gap Record missing any field is a structural failure and does not unlock the phase exit gate.

```
| Field                            | Content |
|----------------------------------|---------|
| Examined                         | [Specific OP-IDs, S-IDs, INV-IDs, trace steps, or registry
|                                  |  cells checked — named individually, not summarized] |
| Evidence Standard Applied        | [Verbatim restatement from PART 0.0B registry row] |
| What Was Not Found               | [Specific absence: anomaly type + IDs — "No violations
|                                  |  found" is not acceptable] |
| What Would Constitute a Finding  | [Phase-specific minimum evidence — must name trace-step
|                                  |  pattern or registry condition, not a generic description] |
| Verdict                          | Acquitted — no qualifying evidence exists
|                                  |   OR Partial — finding below threshold: [specify] |
```

**0B: Standards Registry**

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record "Verdict" explains why |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and anomalous outcome not present sequentially | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch per entity class (S-ID, OP-ID, or INV-ID) absent from its registry | ≥ 1 | ≥ 1 finding at strength ≥ 1 in any sub-scan row, OR Gap Record covers all six sub-scan rows |

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

**V-01 ID Contract:** All finding tables use three separate ID columns (OP-ID, S-ID, INV-ID). A blank cell in any of these columns for a found-verdict row is a detectable structural gap. Use `—` only when the anomaly type genuinely does not implicate that ID class.

**V-01 Blocking Gate Contract:** Each phase exit certification opens with "PHASE N: COMPLETE is BLOCKED until all four gates below are satisfied." The Scoring Protocol gate text names a restate-only SCORING PROTOCOL as a gate-blocking condition.

**V-01 Scoring Protocol Contract:** Each phase's THE SCORING PROTOCOL section contains two named artifacts: (1) *Restate* — verbatim from PART 0.0B; (2) *APPLICATION SENTENCE* — maps the generic threshold to the phase's specific anomaly evidence shape. A SCORING PROTOCOL with only the restate satisfies neither the Scoring Protocol section nor the Scoring Protocol gate.

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B — Pre-Detection Commitment**
> Phase 3A evidence standard (verbatim from PART 0.0B): _____
> Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3A**

*Restate*: _____

*APPLICATION SENTENCE*: For invalid state transitions, strength ≥ 2 means: a specific (OP-ID, from-S-ID, to-S-ID) triple where from-S-ID is not listed in OP-ID's Valid From States, or to-S-ID is not listed in OP-ID's Valid To States — both the operation and the disqualifying state must be named by ID; prose description of a transition pattern does not qualify.

Score at discovery. Say aloud: "I am scoring this [1/2/3] because [specific OP-ID, from-S-ID, to-S-ID triple and the registry column that contradicts it]." Incomplete sentence = not recordable.

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

> **PHASE 3A: COMPLETE is BLOCKED until all four gates below are satisfied.**
> A gate that is not passed is a structural failure. PHASE 3A: COMPLETE cannot be declared with any gate open.

**Phase 3A Exit Certification**
☐ Findings List gate — at least one finding recorded or acquittal named
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 2, OR Gap Record "Verdict" explains why no finding met the standard
☐ Gap Record gate — all 5 PART 0.0A template fields populated; a blank field holds this gate OPEN
☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific, not a restate paraphrase; a SCORING PROTOCOL that contains only the registry restate without a separate APPLICATION SENTENCE holds this gate OPEN and PHASE 3A: COMPLETE cannot be declared

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Phase 3B evidence standard (verbatim from PART 0.0B): _____
> Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3B**

*Restate*: _____

*APPLICATION SENTENCE*: For missing precondition checks, strength ≥ 2 means: a specific (OP-ID, Step-N) pair where either (a) a precondition declared in the OP registry is absent from the step's "Preconditions checked" list, or (b) a precondition appears with verdict MET when the before-state field values should have produced NOT MET — the operation, step number, and specific precondition text must all be named.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID, Step-N, precondition text, and why the verdict is wrong]." Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan OP-Registry for absent, underdefined, or overlapping preconditions.
If no finding: name specific OP-IDs and precondition cells examined and cleared.

**Pass 2: Trace-Diff** — scan PART 2 steps for precondition NOT MET but operation PASS; missing precondition entries; REJECTED guard text referencing different condition.
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

> **PHASE 3B: COMPLETE is BLOCKED until all four gates below are satisfied.**

**Phase 3B Exit Certification**
☐ Findings List gate
☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record "Verdict" explains why
☐ Gap Record gate — all 5 PART 0.0A fields populated; blank field holds this gate OPEN
☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific; restate-only holds this gate OPEN

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Phase 3C evidence standard (verbatim from PART 0.0B): _____
> Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3C**

*Restate*: _____

*APPLICATION SENTENCE*: For invariant violations, strength ≥ 2 means: a specific (INV-ID, Step-N) pair where the step's after-state field value crosses the numeric or temporal threshold declared for INV-ID in 1C — the threshold value, the actual after-state value, and the step number must all be named; a theoretical breach without specific after-state values does not qualify.

Score at discovery. "I am scoring this [1/2/3] because [INV-ID, threshold, Step-N after-state value that crosses it]." Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — scan INV + OP for postconditions that could breach a declared threshold; check cumulative-transition breaches not visible from any single operation.
If no finding: name specific (INV-ID, OP-ID) pairs examined and cleared.

**Pass 2: Trace-Diff** — scan PART 2 after-states against INV thresholds; check adjacent step pairs for cumulative breaches; check postconditions marked VIOLATED.
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

> **PHASE 3C: COMPLETE is BLOCKED until all four gates below are satisfied.**

**Phase 3C Exit Certification**
☐ Findings List gate
☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record "Verdict" explains why
☐ Gap Record gate — all 5 PART 0.0A fields populated; blank field holds this gate OPEN
☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific; restate-only holds this gate OPEN

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Phase 3D evidence standard (verbatim from PART 0.0B): _____
> Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3D**

*Restate*: _____

*APPLICATION SENTENCE*: For race conditions, strength ≥ 2 means: a specific (OP-ID-A, OP-ID-B, shared-S-ID) triple with a named anomalous after-state that appears under one interleaving (A-then-B or B-then-A mid-operation) but not under either fully-sequential ordering — both sequential orderings must be contrasted against the interleaved outcome; a scenario that could cause problems does not qualify without the contrasted after-states named.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID-A, OP-ID-B, the interleaving, and the anomalous after-state vs both sequential outcomes]." Incomplete sentence = not recordable.

**Pass 1: Declaration-Only** — identify OP-ID pairs sharing at least one Valid From State; construct concurrent interleaving scenario; describe anomalous outcome vs sequential execution.
If no finding: name OP-ID pairs constructed and why concurrent execution converges.

**Pass 2: Trace-Diff** — select two steps from PART 2 executing from same or overlapping states or modifying the same field; construct concurrent interleaving; compare concurrent after-state to both sequential orderings.
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

> **PHASE 3D: COMPLETE is BLOCKED until all four gates below are satisfied.**

**Phase 3D Exit Certification**
☐ Findings List gate
☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record "Verdict" explains why
☐ Gap Record gate — all 5 PART 0.0A fields populated; blank field holds this gate OPEN
☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific; restate-only holds this gate OPEN

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References — Entity-Type-Stratified

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

Phase 3E is a full structural peer of Phases 3A–3D with the same four-gate exit model.

**Role B — Pre-Detection Commitment**
> Phase 3E evidence standard (verbatim from PART 0.0B): _____
> Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3E**

*Restate*: _____

*APPLICATION SENTENCE*: For undeclared references, strength ≥ 1 means: the specific registry cell (e.g., "1B row OP-03, Valid From States column") that contains the reference, AND the specific ID that is absent from its target registry (e.g., "S-06 does not appear in 1A") — both the source cell and the missing target must be named by location; a statement that "references may be missing" does not qualify.

Score at discovery. "I am scoring this [1/2/3] because [registry cell, referenced ID, target registry, and confirmation the ID is absent]." Incomplete = not recordable.

**Pass 1: Declaration-Only — Three Independent Sub-Scans**

*P1-S*: Examine 1B Valid From/To and 1C Scope. Does every S-ID cited appear in 1A? Name each cell checked and confirm S-ID resolution.
*P1-O*: Examine 1C descriptions/threshold fields and 1B cross-op references. Does every OP-ID cited appear in 1B? Name each cell checked.
*P1-I*: Examine 1B preconditions/postconditions and 1A entry/exit conditions. Does every INV-ID cited appear in 1C? Name each cell checked.

**Pass 2: Trace-Diff — Three Independent Sub-Scans**

*P2-S*: Scan PART 2 Before/After state fields and Phases 3A–3D S-ID cells. Does every S-ID resolve to a 1A row? Name each trace step checked.
*P2-O*: Scan PART 2 step header OP-IDs and Phases 3A–3D OP-ID cells. Does every OP-ID resolve to a 1B row? Name each step and finding table row checked.
*P2-I*: Scan PART 2 postcondition VIOLATED notes and Phases 3A–3D INV-ID cells. Does every INV-ID resolve to a 1C row? Name each entry checked.

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

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

The Examined field must cover all six sub-scan rows separately.

| Field | Content |
|-------|---------|
| Examined | [P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| Evidence Standard Applied | |
| What Was Not Found | [P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

> **PHASE 3E: COMPLETE is BLOCKED until all four gates below are satisfied.**

**Phase 3E Exit Certification**
☐ Findings List gate — all six sub-scan rows populated with verdicts; a blank row holds this gate OPEN
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1 in any row, OR Gap Record covers all six sub-scan rows
☐ Gap Record gate — all 5 PART 0.0A fields populated; Examined covers all six sub-scan rows; blank field holds this gate OPEN
☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific; restate-only holds this gate OPEN

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-01 prompt body.*

---
---

## V-02: Lifecycle Emphasis — Named ANTI-MASKING RULE in Phase 3E Header (C-45)

**Variation axis**: Lifecycle emphasis — Phase 3E gains two mandatory additions from C-45. First, a named ANTI-MASKING RULE block appears in the phase header before Role B pre-detection commitment and before any sub-scan begins. This block carries the rule as a named, labeled constraint — not narrative explanation. Second, the Phase 3E exit certification uses "Exit gate requires all six sub-scan rows populated" as a named certification title, with individual per-row checkboxes (one per sub-scan). APPLICATION SENTENCE appears inline per phase (C-42 base maintained). Phases 3A–3D use the standard exit certification format without blocking language (C-44 not targeted).

**Hypothesis**: R15 V-02 expressed the row-independence rule as narrative in the phase header ("Each row is an independent sweep unit. A verdict in any P2 row cannot be satisfied by a P1 row..."). C-45 requires the rule to be a named constraint appearing in the phase header before detection begins — not a description of the table structure. A model can read narrative explanation and still treat rows as cumulative because the narrative has no enforcement hook. A labeled ANTI-MASKING RULE block that appears as a phase constraint — parallel to a named invariant — makes violation of the rule a named detectable event rather than a narrative guideline. The per-row checkpoint model separately tests whether the "all six required" certification needs to be explicitly named as a certification condition (not just implied by having six rows).

**Target gaps**: C-45

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or **Finance**. Choose the domain that best fits the scenario you are given. Your task is to hand-compile state transitions, identify anomalies, and produce a structured trace-state report. You play two roles throughout:

- **Role A (Anomaly Finder)**: runs detection passes and records findings
- **Role B (Evidence Steward)**: locks evidence standards and Gap Record template before detection begins, then produces an unconditional structured Gap Record after each phase

---

### PART 0: STANDARDS REGISTRY AND GAP RECORD TEMPLATE

**0A: Gap Record Template**

Every Gap Record uses the following 5-field template. A Gap Record missing any field is a structural failure and does not unlock the phase exit gate.

```
| Field                            | Content |
|----------------------------------|---------|
| Examined                         | [Specific IDs, trace steps, registry cells — named individually] |
| Evidence Standard Applied        | [Verbatim from PART 0.0B registry row for this phase] |
| What Was Not Found               | [Specific absence: anomaly type + IDs — "No violations found" not acceptable] |
| What Would Constitute a Finding  | [Phase-specific minimum evidence — must name the trace-step
|                                  |  pattern or registry condition] |
| Verdict                          | Acquitted / Partial — [if partial: specify finding and why it did not qualify] |
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

**V-02 ID Contract:** All finding tables use three separate ID columns (OP-ID, S-ID, INV-ID). Phase 3E uses the 6-row sub-scan structure.

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B — Pre-Detection Commitment** (verbatim from PART 0.0B):
> Phase 3A: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3A**

*Restate*: _____

*APPLICATION SENTENCE*: For invalid state transitions, strength ≥ 2 means: a specific (OP-ID, from-S-ID, to-S-ID) triple where from-S-ID is not listed in OP-ID's Valid From States or to-S-ID is not listed in Valid To States — all three IDs must be named; prose description without IDs does not qualify.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID, from-S-ID, to-S-ID, and registry column that contradicts it]." Incomplete = not recordable.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions. If no finding: name (OP-ID, S-ID) pairs examined and cleared.
**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps. If no finding: name steps and state-IDs examined and cleared.

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
☐ Findings List gate  ☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record explains why  ☐ Gap Record gate — all 5 fields populated  ☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim): Phase 3B: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3B**

*Restate*: _____

*APPLICATION SENTENCE*: For missing precondition checks, strength ≥ 2 means: a specific (OP-ID, Step-N) pair where a declared precondition is absent from the step's Preconditions checked list, or appears as MET when before-state values require NOT MET — OP-ID, step number, and precondition text must all be named.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID, Step-N, precondition text, why verdict is wrong]." Incomplete = not recordable.

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
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields populated  ☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim): Phase 3C: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3C**

*Restate*: _____

*APPLICATION SENTENCE*: For invariant violations, strength ≥ 2 means: a specific (INV-ID, Step-N) pair where the step's after-state field value crosses the numeric or temporal threshold in 1C — the threshold value, the actual after-state value, and the step number must all be named.

Score at discovery. "I am scoring this [1/2/3] because [INV-ID, threshold, Step-N after-state value that crosses it]." Incomplete = not recordable.

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
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate  ☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment** (verbatim): Phase 3D: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3D**

*Restate*: _____

*APPLICATION SENTENCE*: For race conditions, strength ≥ 2 means: a specific (OP-ID-A, OP-ID-B, shared-S-ID) triple with a named anomalous after-state under one interleaving not present in either sequential ordering — both sequential orderings must be contrasted against the interleaved outcome by name.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID-A, OP-ID-B, interleaving, anomalous after-state vs both sequential outcomes]." Incomplete = not recordable.

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
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate  ☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

---

> **ANTI-MASKING RULE — Phase 3E (Active Before Any Sub-Scan Begins)**
>
> A finding in any sub-scan row does NOT satisfy any other row, regardless of shared entity class or pass number. P1-S findings do not satisfy P2-S, P1-O, P1-I, P2-O, or P2-I. P2-O findings do not satisfy P2-I or P2-S. Each sub-scan row has one and only one sweep unit that satisfies it: itself. Violation of this rule — using a finding in one row to declare another row satisfied — is a detectable structural error independent of finding count.

---

**Role B — Pre-Detection Commitment** (verbatim from PART 0.0B):
> Phase 3E: _____  /  Min: _____  /  Gate: _____

This commitment covers all six sub-scan rows. It cannot be adjusted after any sub-scan begins.

**THE SCORING PROTOCOL — Phase 3E**

*Restate*: _____

*APPLICATION SENTENCE*: For undeclared references, strength ≥ 1 means: the specific registry cell (e.g., "1B row OP-03, Valid From States") containing the reference, and the specific absent ID (e.g., "S-06 not in 1A") — both source cell and missing target must be named by location; "references may be missing" does not qualify.

Score at discovery. "I am scoring this [1/2/3] because [registry cell, referenced ID, target registry, confirmation the ID is absent]." Incomplete = not recordable.

**Pass 1 Sub-Scans: Declaration-Only**

**P1-S**: Examine 1B Valid From/To and 1C Scope. Does every S-ID cited appear in 1A? Name each cell checked and confirm S-ID resolution.

**P1-O**: Examine 1C descriptions/threshold fields and 1B cross-op references. Does every OP-ID cited appear in 1B? Name each cell checked.

**P1-I**: Examine 1B preconditions/postconditions and 1A entry/exit conditions. Does every INV-ID cited appear in 1C? Name each cell checked.

**Pass 2 Sub-Scans: Trace-Diff**

**P2-S**: Scan PART 2 Before/After state fields and Phases 3A–3D S-ID cells. Name each step checked.

**P2-O**: Scan PART 2 step header OP-IDs and Phases 3A–3D OP-ID cells. Name each step and finding table row checked.

**P2-I**: Scan PART 2 postcondition VIOLATED notes and Phases 3A–3D INV-ID cells. Name each entry checked.

**Finding Table — Phase 3E (6-Row Sub-Scan Structure)**

| Sub-Scan ID | Pass | Entity Class | Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|------|-------------|---------|-------|------|--------|--------------------------|
| P1-S | Declaration-Only | S-ID | | — | | — | |
| P1-O | Declaration-Only | OP-ID | | | — | — | |
| P1-I | Declaration-Only | INV-ID | | — | — | | |
| P2-S | Trace-Diff | S-ID | | — | | — | |
| P2-O | Trace-Diff | OP-ID | | | — | — | |
| P2-I | Trace-Diff | INV-ID | | — | — | | |

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | [P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| Evidence Standard Applied | |
| What Was Not Found | [P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

**Phase 3E Exit Certification — Exit gate requires all six sub-scan rows populated**

☐ P1-S row populated with verdict
☐ P1-O row populated with verdict
☐ P1-I row populated with verdict
☐ P2-S row populated with verdict
☐ P2-O row populated with verdict
☐ P2-I row populated with verdict
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1 in any row, OR Gap Record covers all six sub-scan rows
☐ Gap Record gate — all 5 PART 0.0A fields populated; Examined covers all six rows
☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-02 prompt body.*

---
---

## V-03: Role Sequence — Anti-Masking Contract and Exit Gate Contract Pre-Declared in PART 0 (C-44 + C-45)

**Variation axis**: Role sequence — PART 0 is expanded with two additional sections before PART 1 opens. "0C: Per-Phase Exit Contract" declares the four-gate model that every phase must satisfy before its COMPLETE declaration — sealed pre-game so the model cannot rationalize incomplete gates after seeing findings. "0D: Phase 3E Row Independence Contract" declares the anti-masking rule as a named named contract — sealed pre-game so the model cannot form a permissive interpretation of row independence after running Phase 3E sub-scans. At each phase, the exit certification references "per PART 0.0C contract." At Phase 3E, the ANTI-MASKING RULE references "per PART 0.0D contract."

**Hypothesis**: V-01 places the blocking gate language at each phase exit certification (after findings are known). V-02 places the ANTI-MASKING RULE in the Phase 3E header (after the phase is opened). Both framing sites are post-hoc relative to the analysis: the model can see what it found before declaring the gate. Sealing the exit gate contract and the row independence contract in PART 0 — the same mechanic as C-38's evidence standards seal — closes this window. A model that commits to "all four gates required" and "no cross-row satisfaction" before PART 1 opens cannot form a finding-informed interpretation of what those constraints mean.

**Target gaps**: C-44 + C-45

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or **Finance**. Choose the domain that best fits the scenario you are given. Your task is to hand-compile state transitions, identify anomalies, and produce a structured trace-state report. You play two roles throughout:

- **Role A (Anomaly Finder)**: runs detection passes and records findings
- **Role B (Evidence Steward)**: in PART 0, seals the Gap Record template, evidence standards, per-phase exit contract, and Phase 3E row independence contract before any analysis begins; at each phase produces an unconditional structured Gap Record

---

### PART 0: PRE-GAME SEAL

Role B executes all four sections. All are sealed together before PART 1 opens.

**0A: Gap Record Template**

```
| Field                            | Content |
|----------------------------------|---------|
| Examined                         | [Specific IDs, trace steps, registry cells — named individually] |
| Evidence Standard Applied        | [Verbatim from PART 0.0B registry row] |
| What Was Not Found               | [Specific absence: anomaly type + IDs — "No violations found" not acceptable] |
| What Would Constitute a Finding  | [Phase-specific minimum evidence — must name trace-step
|                                  |  pattern or registry condition] |
| Verdict                          | Acquitted / Partial — [if partial: specify] |
```

**0B: Standards Registry**

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record "Verdict" explains why |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and anomalous outcome not present sequentially | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch per entity class absent from its registry | ≥ 1 | ≥ 1 finding at strength ≥ 1 in any sub-scan row, OR Gap Record covers all six sub-scan rows |

**0C: Per-Phase Exit Contract** (declared by Role B, sealed pre-game)

Every phase from 3A through 3E must satisfy all four gates before its COMPLETE declaration unlocks the next phase. No exception is permitted regardless of finding count.

| Gate | Condition | Blocking rule |
|------|-----------|---------------|
| Findings List gate | At least one finding recorded, or named acquittal | A phase with no finding record and no acquittal name holds this gate open |
| Evidence Strength gate | ≥ 1 finding at strength ≥ 2 (≥ 1 for Phase 3E), OR Gap Record Verdict explains why | A Gap Record Verdict that says "Acquitted" without explaining the absence standard holds this gate open |
| Gap Record gate | All 5 PART 0.0A template fields populated | A single blank or placeholder field holds this gate open |
| Scoring Protocol gate | APPLICATION SENTENCE present and phase-specific, not a restate paraphrase | A SCORING PROTOCOL section containing only the registry restate without a separate APPLICATION SENTENCE holds this gate open |

**Role B declaration**: I commit to this four-gate model for all five phases. I cannot waive any gate after PART 0 is sealed.

**0D: Phase 3E Row Independence Contract** (declared by Role B, sealed pre-game)

Phase 3E sweep produces six independent rows (P1-S, P1-O, P1-I, P2-S, P2-O, P2-I). The following rules are sealed and cannot be revised after PART 0 closes:

1. A finding in any sub-scan row does NOT satisfy any other row, regardless of shared entity class or pass number.
2. A blank row in the Phase 3E finding table is an incomplete sweep for that sub-scan, independent of all other rows.
3. Phase 3E: COMPLETE cannot be declared unless all six rows are populated with verdicts.
4. The Gap Record Examined field must name all six sub-scan rows separately.

**Role B declaration**: I commit to these row independence rules for Phase 3E. I cannot interpret cross-row satisfaction or treat a populated row as satisfying any other row after PART 0 is sealed.

**PART 0 SEALED (0A template + 0B standards + 0C exit contract + 0D row independence) → PART 1 now OPEN.**

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

**V-03 ID Contract:** Three separate ID columns (OP-ID, S-ID, INV-ID) in all finding tables. Phase 3E uses the 6-row sub-scan structure per PART 0.0D contract.

**V-03 Phase exit format:** At each phase exit certification, Role B states: "Per PART 0.0C contract — checking all four gates." The four gates are listed and must all be satisfied before PHASE N: COMPLETE.

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim from PART 0.0B): Phase 3A: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3A**

*Restate*: _____

*APPLICATION SENTENCE*: For invalid state transitions, strength ≥ 2 means: a specific (OP-ID, from-S-ID, to-S-ID) triple where from-S-ID is not listed in OP-ID's Valid From States or to-S-ID is not listed in Valid To States — all three IDs must be named; prose description without IDs does not qualify.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID, from-S-ID, to-S-ID, and the registry column that contradicts it]." Incomplete = not recordable.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions. If no finding: name (OP-ID, S-ID) pairs examined and cleared.
**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps. If no finding: name steps and state-IDs examined and cleared.

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

**Per PART 0.0C contract — checking all four gates:**

**Phase 3A Exit Certification**
☐ Findings List gate — finding recorded or acquittal named
☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record Verdict explains why
☐ Gap Record gate — all 5 PART 0.0A fields populated
☐ Scoring Protocol gate — APPLICATION SENTENCE present, phase-specific, not a restate paraphrase

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim from PART 0.0B): Phase 3B: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3B**

*Restate*: _____

*APPLICATION SENTENCE*: For missing precondition checks, strength ≥ 2 means: a specific (OP-ID, Step-N) pair where a declared precondition is absent from the step's Preconditions checked list, or appears as MET when before-state values require NOT MET — OP-ID, step number, and precondition text must all be named.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID, Step-N, precondition text, why verdict is wrong]." Incomplete = not recordable.

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

**Per PART 0.0C contract — checking all four gates:**

**Phase 3B Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields  ☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim from PART 0.0B): Phase 3C: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3C**

*Restate*: _____

*APPLICATION SENTENCE*: For invariant violations, strength ≥ 2 means: a specific (INV-ID, Step-N) pair where the step's after-state field value crosses the numeric or temporal threshold in 1C — the threshold value, the actual after-state value, and the step number must all be named.

Score at discovery. "I am scoring this [1/2/3] because [INV-ID, threshold, Step-N after-state value that crosses it]." Incomplete = not recordable.

**Pass 1: Declaration-Only** — scan INV + OP for threshold-breaching postconditions. If no finding: name (INV-ID, OP-ID) pairs cleared.
**Pass 2: Trace-Diff** — scan after-states and adjacent pairs. If no finding: name steps and INV-IDs cleared.

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

**Per PART 0.0C contract — checking all four gates:**

**Phase 3C Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate  ☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Standards (verbatim from PART 0.0B): Phase 3D: _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3D**

*Restate*: _____

*APPLICATION SENTENCE*: For race conditions, strength ≥ 2 means: a specific (OP-ID-A, OP-ID-B, shared-S-ID) triple with a named anomalous after-state under one interleaving not present in either sequential ordering — both sequential orderings must be contrasted against the interleaved outcome by name.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID-A, OP-ID-B, interleaving, anomalous after-state vs both sequential outcomes]." Incomplete = not recordable.

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

**Per PART 0.0C contract — checking all four gates:**

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate  ☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

> **ANTI-MASKING RULE — Phase 3E (per PART 0.0D contract)**
> A finding in any sub-scan row does NOT satisfy any other row, regardless of shared entity class or pass number. This rule was sealed in PART 0 before any analysis began and cannot be revised.

**Role B — Pre-Detection Commitment**
> Standards (verbatim from PART 0.0B): Phase 3E: _____  /  Min: _____  /  Gate: _____
> Row independence: Per PART 0.0D contract — all six rows (P1-S, P1-O, P1-I, P2-S, P2-O, P2-I) must be populated. A blank row is an incomplete sub-scan. Cross-row satisfaction is prohibited.

**THE SCORING PROTOCOL — Phase 3E**

*Restate*: _____

*APPLICATION SENTENCE*: For undeclared references, strength ≥ 1 means: the specific registry cell (e.g., "1B row OP-03, Valid From States") containing the reference, and the specific absent ID (e.g., "S-06 not in 1A") — both source cell and missing target must be named by location; "references may be missing" does not qualify.

Score at discovery. "I am scoring this [1/2/3] because [registry cell, referenced ID, target registry, confirmation the ID is absent]." Incomplete = not recordable.

**Pass 1 Sub-Scans: Declaration-Only**

**P1-S**: Examine 1B Valid From/To and 1C Scope. Every S-ID cited must appear in 1A. Name each cell checked.
**P1-O**: Examine 1C descriptions and 1B cross-op references. Every OP-ID cited must appear in 1B. Name each cell checked.
**P1-I**: Examine 1B preconditions/postconditions and 1A entry/exit. Every INV-ID cited must appear in 1C. Name each cell checked.

**Pass 2 Sub-Scans: Trace-Diff**

**P2-S**: Scan PART 2 Before/After states and Phases 3A–3D S-ID cells. Name each step checked.
**P2-O**: Scan PART 2 step OP-IDs and Phases 3A–3D OP-ID cells. Name each step and finding table row checked.
**P2-I**: Scan PART 2 VIOLATED postconditions and Phases 3A–3D INV-ID cells. Name each entry checked.

**Finding Table — Phase 3E**

| Sub-Scan ID | Pass | Entity Class | Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|------|-------------|---------|-------|------|--------|--------------------------|
| P1-S | Declaration-Only | S-ID | | — | | — | |
| P1-O | Declaration-Only | OP-ID | | | — | — | |
| P1-I | Declaration-Only | INV-ID | | — | — | | |
| P2-S | Trace-Diff | S-ID | | — | | — | |
| P2-O | Trace-Diff | OP-ID | | | — | — | |
| P2-I | Trace-Diff | INV-ID | | — | — | | |

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | [P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| Evidence Standard Applied | |
| What Was Not Found | [P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

**Per PART 0.0C and 0.0D contracts — checking all gates:**

**Phase 3E Exit Certification — Exit gate requires all six sub-scan rows populated (per PART 0.0D)**
☐ P1-S row populated with verdict
☐ P1-O row populated with verdict
☐ P1-I row populated with verdict
☐ P2-S row populated with verdict
☐ P2-O row populated with verdict
☐ P2-I row populated with verdict
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1 in any row, OR Gap Record covers all six rows
☐ Gap Record gate — all 5 PART 0.0A fields; Examined covers all six sub-scan rows
☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific (per PART 0.0C)

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-03 prompt body.*

---
---

## V-04: Compound — Blocking Exit Gate + Named Anti-Masking Constraint (C-44 + C-45)

**Variation axis**: Compound — output format + lifecycle emphasis. Combines V-01's blocking APPLICATION SENTENCE gate language at each phase exit certification with V-02's named ANTI-MASKING RULE callout in the Phase 3E header and the per-row checkpoint exit certification. This is the full R16 baseline: every phase has "PHASE N: COMPLETE is BLOCKED until all four gates are satisfied" with the Scoring Protocol gate explicitly named as blocking; Phase 3E has the ANTI-MASKING RULE as a labeled named constraint before detection; the Phase 3E exit certification has individual row checkboxes under the named "Exit gate requires all six sub-scan rows populated" condition.

**Hypothesis**: C-44 and C-45 are independent structural requirements. C-44 governs the gate enforcement model for all five phases. C-45 governs Phase 3E's row independence enforcement and exit certification structure. Neither implies the other. The compound variation closes both gaps simultaneously: a model executing this prompt cannot skip the APPLICATION SENTENCE gate (blocked explicitly) and cannot satisfy the Phase 3E exit gate with fewer than six row verdicts (each row is an individually checked gate item under a named condition).

**Target gaps**: C-44 + C-45

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or **Finance**. Choose the domain that best fits the scenario you are given. Your task is to hand-compile state transitions, identify anomalies, and produce a structured trace-state report. You play two roles throughout:

- **Role A (Anomaly Finder)**: runs detection passes and records findings
- **Role B (Evidence Steward)**: locks evidence standards and Gap Record template before detection begins, then produces an unconditional structured Gap Record after each phase

---

### PART 0: STANDARDS REGISTRY AND GAP RECORD TEMPLATE

**0A: Gap Record Template**

Every Gap Record uses the following 5-field template. A Gap Record missing any field is a structural failure and does not unlock the phase exit gate.

```
| Field                            | Content |
|----------------------------------|---------|
| Examined                         | [Specific IDs, trace steps, registry cells — named individually] |
| Evidence Standard Applied        | [Verbatim from PART 0.0B registry row] |
| What Was Not Found               | [Specific absence: anomaly type + IDs — "No violations found" not acceptable] |
| What Would Constitute a Finding  | [Phase-specific minimum evidence — must name trace-step
|                                  |  pattern or registry condition] |
| Verdict                          | Acquitted / Partial — [if partial: specify] |
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

**V-04 ID Contract:** Three separate ID columns (OP-ID, S-ID, INV-ID) in all finding tables. Phase 3E uses 6-row sub-scan structure.

**V-04 Blocking Gate Contract:** Every phase exit certification opens with "PHASE N: COMPLETE is BLOCKED until all four gates below are satisfied." The Scoring Protocol gate text names a restate-only SCORING PROTOCOL as the specific condition that holds this gate open.

**V-04 Scoring Protocol Contract:** Each phase's THE SCORING PROTOCOL section contains: (1) *Restate* — verbatim from PART 0.0B; (2) *APPLICATION SENTENCE* — phase-specific mapping of the threshold to this anomaly class's evidence shape. Restate alone does not satisfy the gate.

**V-04 Phase 3E Contract:** A named ANTI-MASKING RULE appears in the Phase 3E header before detection begins. Phase 3E exit certification uses per-row checkboxes under the named condition "Exit gate requires all six sub-scan rows populated."

---

#### Phase 3A: Invalid State Transitions

**[STATUS: OPEN — no prerequisite]**

**Role B — Pre-Detection Commitment**
> Phase 3A (verbatim from PART 0.0B): _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3A**

*Restate*: _____

*APPLICATION SENTENCE*: For invalid state transitions, strength ≥ 2 means: a specific (OP-ID, from-S-ID, to-S-ID) triple where from-S-ID is not listed in OP-ID's Valid From States or to-S-ID is not listed in Valid To States — all three IDs must be named; prose description without IDs does not qualify.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID, from-S-ID, to-S-ID, registry column that contradicts it]." Incomplete = not recordable.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions. If no finding: name (OP-ID, S-ID) pairs examined and cleared.
**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps. If no finding: name steps and state-IDs examined and cleared.

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

> **PHASE 3A: COMPLETE is BLOCKED until all four gates below are satisfied.**
> A gate that is not passed is a structural failure. PHASE 3A: COMPLETE cannot be declared with any gate open.

**Phase 3A Exit Certification**
☐ Findings List gate — finding recorded or acquittal named
☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record "Verdict" explains why
☐ Gap Record gate — all 5 PART 0.0A fields populated; blank field holds this gate OPEN
☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific, not a restate paraphrase; a SCORING PROTOCOL containing only the registry restate without a separate APPLICATION SENTENCE holds this gate OPEN

**PHASE 3A: COMPLETE [Unlocks Phase 3B]**

---

#### Phase 3B: Missing Precondition Checks

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Phase 3B (verbatim from PART 0.0B): _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3B**

*Restate*: _____

*APPLICATION SENTENCE*: For missing precondition checks, strength ≥ 2 means: a specific (OP-ID, Step-N) pair where a declared precondition is absent from the step's Preconditions checked list, or appears as MET when before-state values require NOT MET — OP-ID, step number, and precondition text must all be named.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID, Step-N, precondition text, why verdict is wrong]." Incomplete = not recordable.

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

> **PHASE 3B: COMPLETE is BLOCKED until all four gates below are satisfied.**

**Phase 3B Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record explains why  ☐ Gap Record gate — all 5 fields; blank field holds this gate OPEN  ☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific; restate-only holds this gate OPEN

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Phase 3C (verbatim from PART 0.0B): _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3C**

*Restate*: _____

*APPLICATION SENTENCE*: For invariant violations, strength ≥ 2 means: a specific (INV-ID, Step-N) pair where the step's after-state field value crosses the numeric or temporal threshold in 1C — the threshold value, the actual after-state value, and the step number must all be named.

Score at discovery. "I am scoring this [1/2/3] because [INV-ID, threshold, Step-N after-state value that crosses it]." Incomplete = not recordable.

**Pass 1: Declaration-Only** — scan INV + OP for threshold-breaching postconditions. If no finding: name (INV-ID, OP-ID) pairs cleared.
**Pass 2: Trace-Diff** — scan after-states and adjacent pairs. If no finding: name steps and INV-IDs cleared.

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

> **PHASE 3C: COMPLETE is BLOCKED until all four gates below are satisfied.**

**Phase 3C Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields; blank field holds this gate OPEN  ☐ Scoring Protocol gate — APPLICATION SENTENCE present; restate-only holds this gate OPEN

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Phase 3D (verbatim from PART 0.0B): _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3D**

*Restate*: _____

*APPLICATION SENTENCE*: For race conditions, strength ≥ 2 means: a specific (OP-ID-A, OP-ID-B, shared-S-ID) triple with a named anomalous after-state under one interleaving not present in either sequential ordering — both sequential orderings must be contrasted against the interleaved outcome by name.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID-A, OP-ID-B, interleaving, anomalous after-state vs both sequential outcomes]." Incomplete = not recordable.

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

> **PHASE 3D: COMPLETE is BLOCKED until all four gates below are satisfied.**

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — all 5 fields; blank field holds this gate OPEN  ☐ Scoring Protocol gate — APPLICATION SENTENCE present; restate-only holds this gate OPEN

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

---

> **ANTI-MASKING RULE — Phase 3E (Active Before Any Sub-Scan Begins)**
>
> A finding in any sub-scan row does NOT satisfy any other row, regardless of shared entity class or pass number. P1-S findings do not satisfy P2-S, P1-O, P1-I, P2-O, or P2-I. P2-O findings do not satisfy P2-I or P2-S. Each sub-scan row has one and only one sweep unit that satisfies it: itself. Applying a verdict from one row to declare another row satisfied is a structural violation detectable by row-level inspection.

---

**Role B — Pre-Detection Commitment**
> Phase 3E (verbatim from PART 0.0B): _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3E**

*Restate*: _____

*APPLICATION SENTENCE*: For undeclared references, strength ≥ 1 means: the specific registry cell (e.g., "1B row OP-03, Valid From States") containing the reference, and the specific absent ID (e.g., "S-06 not in 1A") — both source cell and missing target must be named by location; "references may be missing" does not qualify.

Score at discovery. "I am scoring this [1/2/3] because [registry cell, referenced ID, target registry, confirmation the ID is absent]." Incomplete = not recordable.

**Pass 1 Sub-Scans: Declaration-Only**

**P1-S**: Examine 1B Valid From/To and 1C Scope. Every S-ID cited must appear in 1A. Name each cell checked.
**P1-O**: Examine 1C descriptions and 1B cross-op references. Every OP-ID cited must appear in 1B. Name each cell checked.
**P1-I**: Examine 1B preconditions/postconditions and 1A entry/exit. Every INV-ID cited must appear in 1C. Name each cell checked.

**Pass 2 Sub-Scans: Trace-Diff**

**P2-S**: Scan PART 2 Before/After states and Phases 3A–3D S-ID cells. Name each step checked.
**P2-O**: Scan PART 2 step OP-IDs and Phases 3A–3D OP-ID cells. Name each step and finding table row checked.
**P2-I**: Scan PART 2 VIOLATED postconditions and Phases 3A–3D INV-ID cells. Name each entry checked.

**Finding Table — Phase 3E**

| Sub-Scan ID | Pass | Entity Class | Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|------|-------------|---------|-------|------|--------|--------------------------|
| P1-S | Declaration-Only | S-ID | | — | | — | |
| P1-O | Declaration-Only | OP-ID | | | — | — | |
| P1-I | Declaration-Only | INV-ID | | — | — | | |
| P2-S | Trace-Diff | S-ID | | — | | — | |
| P2-O | Trace-Diff | OP-ID | | | — | — | |
| P2-I | Trace-Diff | INV-ID | | — | — | | |

**Role B — Gap Record [UNCONDITIONAL — PART 0.0A TEMPLATE]**

| Field | Content |
|-------|---------|
| Examined | [P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| Evidence Standard Applied | |
| What Was Not Found | [P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3E exit gate.**

> **PHASE 3E: COMPLETE is BLOCKED until all gates below are satisfied.**
> The ANTI-MASKING RULE is active: no cross-row satisfaction is permitted.

**Phase 3E Exit Certification — Exit gate requires all six sub-scan rows populated**

☐ P1-S row populated with verdict — a blank P1-S row holds this gate OPEN
☐ P1-O row populated with verdict — a blank P1-O row holds this gate OPEN
☐ P1-I row populated with verdict — a blank P1-I row holds this gate OPEN
☐ P2-S row populated with verdict — a blank P2-S row holds this gate OPEN
☐ P2-O row populated with verdict — a blank P2-O row holds this gate OPEN
☐ P2-I row populated with verdict — a blank P2-I row holds this gate OPEN
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1 in any row, OR Gap Record covers all six rows; blank field holds this gate OPEN
☐ Gap Record gate — all 5 PART 0.0A fields; Examined covers all six sub-scan rows; blank field holds this gate OPEN
☐ Scoring Protocol gate — APPLICATION SENTENCE present and phase-specific; restate-only holds this gate OPEN

**PHASE 3E: COMPLETE [Sweep closed]**

---

*End of V-04 prompt body.*

---
---

## V-05: Compound + Phrasing — MUST/BLOCKED/ADVANCE with PART 5 Reconciliation (C-44 + C-45)

**Variation axis**: Compound — output format + lifecycle emphasis + phrasing register. Builds on V-04 (blocking gate language + named ANTI-MASKING RULE + per-row checkboxes) and adds: (1) MUST/BLOCKED/ADVANCE imperative markers at each gate and sub-scan instruction; (2) explicit "ADVANCE to [next phase] ONLY WHEN: PHASE N: COMPLETE declared" advancement gate before each phase; (3) PART 5 reconciliation table with C/FP/FN classification and calibration score. The phrasing register shifts from descriptive ("holds this gate OPEN") to imperative ("You MUST NOT advance until this gate passes").

**Hypothesis**: V-04 uses blocking framing ("PHASE N: COMPLETE is BLOCKED until...") but the language is passive — it describes a state. A model can read "BLOCKED" and still advance because the consequence of not advancing (the next phase remaining LOCKED) is implicit rather than stated as a direct behavioral instruction. Imperative MUST/MUST NOT phrasing addresses the model directly as a behavioral agent rather than describing a gate state. The ADVANCE ONLY WHEN line at each phase opening additionally closes the gap where a model opens a phase before the prior COMPLETE is declared. PART 5 reconciliation with C/FP/FN tests whether prediction accountability changes the density of analysis in earlier phases.

**Target gaps**: C-44 + C-45 + phrasing register

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or **Finance**. Choose the domain that best fits the scenario you are given. Your task is to hand-compile state transitions, identify anomalies, and produce a structured trace-state report. You play two roles throughout:

- **Role A (Anomaly Finder)**: runs detection passes and records findings
- **Role B (Evidence Steward)**: locks evidence standards and Gap Record template before detection begins, then produces an unconditional structured Gap Record after each phase

---

### PART 0: STANDARDS REGISTRY AND GAP RECORD TEMPLATE

**0A: Gap Record Template**

You MUST use this 5-field template for every Gap Record. A Gap Record with any field blank or as placeholder text is a structural failure. You MUST NOT declare a phase exit gate passed if the Gap Record is incomplete.

```
| Field                            | Content |
|----------------------------------|---------|
| Examined                         | [Specific IDs, trace steps, registry cells — named individually;
|                                  |  "all entries" is NOT acceptable] |
| Evidence Standard Applied        | [Verbatim from PART 0.0B registry row — copy it exactly] |
| What Was Not Found               | [Specific absence: name the anomaly type and specific IDs;
|                                  |  "no violations found" is NOT acceptable] |
| What Would Constitute a Finding  | [Phase-specific minimum — MUST name the trace-step pattern
|                                  |  or registry condition; a generic description does NOT qualify] |
| Verdict                          | Acquitted — no qualifying evidence exists
|                                  |   OR Partial — [specify finding and why it did not qualify] |
```

**0B: Standards Registry**

| Phase | Anomaly Type | Evidence Standard | Min Strength | Phase Gate |
|-------|-------------|-------------------|--------------|------------|
| 3A | Invalid state transitions | Direct trace-step or declared-transition evidence mapping (OP-ID, S-ID) → next S-ID | ≥ 2 | ≥ 1 finding at strength ≥ 2, OR Gap Record "Verdict" explains why |
| 3B | Missing precondition checks | Trace-step evidence showing a precondition not evaluated or evaluated with wrong verdict | ≥ 2 | same |
| 3C | Invariant violations | INV-ID reference + trace-step or state-condition evidence of threshold breach | ≥ 2 | same |
| 3D | Race conditions | Concurrent-operation scenario naming both OP-IDs and anomalous outcome not present sequentially | ≥ 2 | same |
| 3E | Undeclared references | Cross-reference mismatch per entity class absent from its registry | ≥ 1 | ≥ 1 finding at strength ≥ 1 in any sub-scan row, OR Gap Record covers all six sub-scan rows |

**PART 0 SEALED. You MUST NOT revise these standards after this point. → PART 1 now OPEN.**

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

Minimum 6 numbered steps. You MUST include at least one `[REJECTED]` negative-path step.

```
Step N: [OP-ID] [Operation Name]  [PASS / REJECTED]
  Before state:   [S-ID] [State Name] — { field: value, ... }
  Preconditions checked:
    - [text]: MET / NOT MET
  Guard condition: passes — continue  /  fires — reason: [text]
  After state:    [S-ID] [State Name] — { field: value, ... }
    [REJECTED: The entity MUST remain in its before-state after rejection.
     After state MUST equal before state field-for-field. Any deviation is a
     detectable anomaly independent of the rejection reason.]
  Postconditions verified:
    - [text]: HOLDS / VIOLATED
```

---

### PART 3: PRE-SWEEP HYPOTHESIS

You MUST record predictions before PART 4 begins. These are LOCKED once any detection pass runs. You MUST NOT revise them after Phase 3A opens.

| Phase | Anomaly Type | Predicted Count | Confidence (L/M/H) | Specific Predicted Scenario |
|-------|-------------|-----------------|--------------------|-----------------------------|
| 3A | Invalid state transitions | | | |
| 3B | Missing precondition checks | | | |
| 3C | Invariant violations | | | |
| 3D | Race conditions | | | |
| 3E | Undeclared references | | | |

---

### PART 4: ANOMALY SWEEP

**V-05 ID Contract:** You MUST use three separate ID columns (OP-ID, S-ID, INV-ID) in all finding tables. A blank cell in a found-verdict row is a detectable structural gap. Phase 3E MUST use the 6-row sub-scan structure.

**V-05 Gate Rule:** You MUST NOT declare PHASE N: COMPLETE until all four gates are satisfied. A gate that is not passed BLOCKS the COMPLETE declaration. You MUST NOT open Phase N+1 until Phase N: COMPLETE is declared.

**V-05 Scoring Protocol Rule:** You MUST include THE SCORING PROTOCOL section in each phase with two artifacts: (1) verbatim restate from PART 0.0B, (2) APPLICATION SENTENCE mapping the threshold to this phase's specific anomaly evidence shape. You MUST NOT satisfy the Scoring Protocol gate with the restate alone.

**V-05 Phase 3E Anti-Masking Rule:** You MUST NOT apply a verdict from any sub-scan row to satisfy any other row. Each row MUST be independently verified and populated.

---

#### Phase 3A: Invalid State Transitions

**ADVANCE to Phase 3A ONLY WHEN: no prerequisite (this is the first phase)**

**[STATUS: OPEN]**

**Role B — Pre-Detection Commitment**
> Phase 3A evidence standard (verbatim from PART 0.0B): _____
> Min strength: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3A**

*Restate* (verbatim from PART 0.0B): _____

*APPLICATION SENTENCE* (MUST be phase-specific — a restate paraphrase does NOT satisfy this): For invalid state transitions, strength ≥ 2 means: a specific (OP-ID, from-S-ID, to-S-ID) triple where from-S-ID is not listed in OP-ID's Valid From States or to-S-ID is not listed in Valid To States — all three IDs MUST be named; prose description without IDs does NOT qualify.

You MUST score at the moment of discovery. Say aloud: "I am scoring this [1/2/3] because [specific OP-ID, from-S-ID, to-S-ID triple and registry column that contradicts it]." An incomplete sentence MUST NOT be recorded.

**Pass 1: Declaration-Only** — scan 1A + 1B for invalid declared transitions.
If no finding: you MUST name specific (OP-ID, S-ID) pairs examined and cleared.

**Pass 2: Trace-Diff** — diff Valid From/To against PART 2 steps.
If no finding: you MUST name specific steps and state-IDs examined and cleared.

**Finding Table — Phase 3A**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|
| | | | | | | |

**Role B — Gap Record [UNCONDITIONAL — you MUST complete all 5 fields of PART 0.0A template]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3A exit gate. You MUST complete it before checking any exit gate.**

> **PHASE 3A: COMPLETE is BLOCKED. You MUST NOT advance to Phase 3B until all four gates below are satisfied.**

**Phase 3A Exit Certification**
☐ Findings List gate — finding recorded or acquittal named; MUST be present
☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record "Verdict" MUST explain why no finding met the standard
☐ Gap Record gate — all 5 PART 0.0A fields populated; you MUST NOT check this gate if any field is blank
☐ Scoring Protocol gate — APPLICATION SENTENCE MUST be present and phase-specific; you MUST NOT check this gate if SCORING PROTOCOL contains only the registry restate

**PHASE 3A: COMPLETE [Unlocks Phase 3B — you MUST NOT proceed to Phase 3B until this is declared]**

---

#### Phase 3B: Missing Precondition Checks

**ADVANCE to Phase 3B ONLY WHEN: PHASE 3A: COMPLETE has been declared above**

**[STATUS: LOCKED until PHASE 3A: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Phase 3B (verbatim from PART 0.0B): _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3B**

*Restate*: _____

*APPLICATION SENTENCE* (MUST be phase-specific): For missing precondition checks, strength ≥ 2 means: a specific (OP-ID, Step-N) pair where a declared precondition is absent from the step's Preconditions checked list, or appears as MET when before-state values require NOT MET — OP-ID, step number, and precondition text MUST all be named.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID, Step-N, precondition text, why verdict is wrong]." Incomplete MUST NOT be recorded.

**Pass 1: Declaration-Only** — scan OP-Registry for absent/underdefined preconditions. If no finding: MUST name OP-IDs cleared.
**Pass 2: Trace-Diff** — scan steps for NOT MET → PASS or missing entries. If no finding: MUST name steps cleared.

**Finding Table — Phase 3B**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — MUST complete all 5 fields]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

> **PHASE 3B: COMPLETE is BLOCKED until all four gates are satisfied.**

**Phase 3B Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate — ≥ 1 at strength ≥ 2, OR Gap Record MUST explain why  ☐ Gap Record gate — all 5 fields; MUST NOT check if any field blank  ☐ Scoring Protocol gate — APPLICATION SENTENCE MUST be present; MUST NOT check if restate-only

**PHASE 3B: COMPLETE [Unlocks Phase 3C]**

---

#### Phase 3C: Invariant Violations

**ADVANCE to Phase 3C ONLY WHEN: PHASE 3B: COMPLETE has been declared above**

**[STATUS: LOCKED until PHASE 3B: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Phase 3C (verbatim from PART 0.0B): _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3C**

*Restate*: _____

*APPLICATION SENTENCE* (MUST be phase-specific): For invariant violations, strength ≥ 2 means: a specific (INV-ID, Step-N) pair where the step's after-state field value crosses the numeric or temporal threshold in 1C — the threshold value, the actual after-state value, and the step number MUST all be named.

Score at discovery. "I am scoring this [1/2/3] because [INV-ID, threshold, Step-N after-state value that crosses it]." Incomplete MUST NOT be recorded.

**Pass 1: Declaration-Only** — scan INV + OP for threshold-breaching postconditions. If no finding: MUST name (INV-ID, OP-ID) pairs cleared.
**Pass 2: Trace-Diff** — scan after-states and adjacent pairs. If no finding: MUST name steps and INV-IDs cleared.

**Finding Table — Phase 3C**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — MUST complete all 5 fields]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

> **PHASE 3C: COMPLETE is BLOCKED until all four gates are satisfied.**

**Phase 3C Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — MUST NOT check if any field blank  ☐ Scoring Protocol gate — APPLICATION SENTENCE MUST be present; MUST NOT check if restate-only

**PHASE 3C: COMPLETE [Unlocks Phase 3D]**

---

#### Phase 3D: Race Conditions

**ADVANCE to Phase 3D ONLY WHEN: PHASE 3C: COMPLETE has been declared above**

**[STATUS: LOCKED until PHASE 3C: COMPLETE]**

**Role B — Pre-Detection Commitment**
> Phase 3D (verbatim from PART 0.0B): _____  /  Min: _____  /  Gate: _____

**THE SCORING PROTOCOL — Phase 3D**

*Restate*: _____

*APPLICATION SENTENCE* (MUST be phase-specific): For race conditions, strength ≥ 2 means: a specific (OP-ID-A, OP-ID-B, shared-S-ID) triple with a named anomalous after-state under one interleaving not present in either sequential ordering — both sequential orderings MUST be contrasted against the interleaved outcome by name.

Score at discovery. "I am scoring this [1/2/3] because [OP-ID-A, OP-ID-B, interleaving, anomalous after-state vs both sequential outcomes]." Incomplete MUST NOT be recorded.

**Pass 1: Declaration-Only** — identify OP-ID pairs sharing Valid From States; construct concurrent scenario. If no finding: MUST name OP-ID pairs and convergence rationale.
**Pass 2: Trace-Diff** — construct step-pair interleaving; compare concurrent vs sequential. If no finding: MUST name step pairs and comparison result.

**Finding Table — Phase 3D**

| Finding-ID | Declaration-Only Finding | Trace-Diff Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|--------------------------|--------------------|----|-----|--------|--------------------------|

**Role B — Gap Record [UNCONDITIONAL — MUST complete all 5 fields]**

| Field | Content |
|-------|---------|
| Examined | |
| Evidence Standard Applied | |
| What Was Not Found | |
| What Would Constitute a Finding | |
| Verdict | |

> **PHASE 3D: COMPLETE is BLOCKED until all four gates are satisfied.**

**Phase 3D Exit Certification**
☐ Findings List gate  ☐ Evidence Strength gate  ☐ Gap Record gate — MUST NOT check if any field blank  ☐ Scoring Protocol gate — APPLICATION SENTENCE MUST be present; MUST NOT check if restate-only

**PHASE 3D: COMPLETE [Unlocks Phase 3E]**

---

#### Phase 3E: Undeclared References

**ADVANCE to Phase 3E ONLY WHEN: PHASE 3D: COMPLETE has been declared above**

**[STATUS: LOCKED until PHASE 3D: COMPLETE]**

---

> **ANTI-MASKING RULE — Phase 3E (You MUST enforce this before any sub-scan begins)**
>
> You MUST NOT apply a finding or verdict from any sub-scan row to satisfy any other row. A finding in P1-S does NOT satisfy P2-S, P1-O, P1-I, P2-O, or P2-I. A finding in P2-O does NOT satisfy P2-I or P2-S. Each sub-scan row MUST be independently verified. You MUST NOT declare Phase 3E: COMPLETE if any sub-scan row is blank, regardless of findings in other rows.

---

**Role B — Pre-Detection Commitment**
> Phase 3E (verbatim from PART 0.0B): _____  /  Min: _____  /  Gate: _____
> ANTI-MASKING RULE acknowledged: all six rows (P1-S, P1-O, P1-I, P2-S, P2-O, P2-I) MUST be independently populated.

**THE SCORING PROTOCOL — Phase 3E**

*Restate*: _____

*APPLICATION SENTENCE* (MUST be phase-specific): For undeclared references, strength ≥ 1 means: the specific registry cell (e.g., "1B row OP-03, Valid From States") containing the reference, and the specific absent ID (e.g., "S-06 not in 1A") — both source cell and missing target MUST be named by location; "references may be missing" does NOT qualify.

Score at discovery. "I am scoring this [1/2/3] because [registry cell, referenced ID, target registry, confirmation the ID is absent]." Incomplete MUST NOT be recorded.

**Pass 1 Sub-Scans: Declaration-Only**

**P1-S**: You MUST examine 1B Valid From/To and 1C Scope. Does every S-ID cited appear in 1A? Name each cell checked and confirm S-ID resolution. You MUST NOT leave this sub-scan implicit.

**P1-O**: You MUST examine 1C descriptions and 1B cross-op references. Does every OP-ID cited appear in 1B? Name each cell checked.

**P1-I**: You MUST examine 1B preconditions/postconditions and 1A entry/exit. Does every INV-ID cited appear in 1C? Name each cell checked.

**Pass 2 Sub-Scans: Trace-Diff**

**P2-S**: You MUST scan PART 2 Before/After states and Phases 3A–3D S-ID cells. Name each step checked.

**P2-O**: You MUST scan PART 2 step OP-IDs and Phases 3A–3D OP-ID cells. Name each step and finding table row checked.

**P2-I**: You MUST scan PART 2 VIOLATED postconditions and Phases 3A–3D INV-ID cells. Name each entry checked.

**Finding Table — Phase 3E**

| Sub-Scan ID | Pass | Entity Class | Finding | OP-ID | S-ID | INV-ID | Evidence Strength (1/2/3) |
|------------|------|-------------|---------|-------|------|--------|--------------------------|
| P1-S | Declaration-Only | S-ID | | — | | — | |
| P1-O | Declaration-Only | OP-ID | | | — | — | |
| P1-I | Declaration-Only | INV-ID | | — | — | | |
| P2-S | Trace-Diff | S-ID | | — | | — | |
| P2-O | Trace-Diff | OP-ID | | | — | — | |
| P2-I | Trace-Diff | INV-ID | | — | — | | |

**Role B — Gap Record [UNCONDITIONAL — MUST complete all 5 fields; Examined MUST cover all six sub-scans]**

| Field | Content |
|-------|---------|
| Examined | [P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| Evidence Standard Applied | |
| What Was Not Found | [P1-S: ___ / P1-O: ___ / P1-I: ___ / P2-S: ___ / P2-O: ___ / P2-I: ___] |
| What Would Constitute a Finding | |
| Verdict | |

**The Gap Record is the unlock signal for the Phase 3E exit gate. You MUST complete it before checking any exit gate.**

> **PHASE 3E: COMPLETE is BLOCKED until all gates below are satisfied.**
> The ANTI-MASKING RULE is active. You MUST NOT check any row checkbox by deriving it from another row's verdict.

**Phase 3E Exit Certification — Exit gate requires all six sub-scan rows populated**

☐ P1-S row populated — you MUST NOT check this from any other row's verdict
☐ P1-O row populated — you MUST NOT check this from any other row's verdict
☐ P1-I row populated — you MUST NOT check this from any other row's verdict
☐ P2-S row populated — you MUST NOT check this from any other row's verdict; a P1-S finding does NOT satisfy P2-S
☐ P2-O row populated — you MUST NOT check this from any other row's verdict; a P1-O finding does NOT satisfy P2-O
☐ P2-I row populated — you MUST NOT check this from any other row's verdict; a P1-I finding does NOT satisfy P2-I
☐ Evidence Strength gate — ≥ 1 finding at strength ≥ 1 in any row, OR Gap Record MUST cover all six sub-scan rows
☐ Gap Record gate — all 5 PART 0.0A fields; Examined MUST cover all six sub-scan rows; MUST NOT check if any field blank
☐ Scoring Protocol gate — APPLICATION SENTENCE MUST be present; MUST NOT check if SCORING PROTOCOL contains only the registry restate

**PHASE 3E: COMPLETE [Sweep closed]**

---

### PART 5: RECONCILIATION

Complete after all phases are closed. Compare PART 3 predictions against PART 4 findings.

**Calibration threshold**: A score below 60% Correct (C) requires structural diagnosis — the prediction model is unreliable and findings may be under-detected.

| Phase | Predicted Scenario (from PART 3) | Actual Finding | Classification | Notes |
|-------|----------------------------------|---------------|----------------|-------|
| 3A | | | C / FP / FN | |
| 3B | | | C / FP / FN | |
| 3C | | | C / FP / FN | |
| 3D | | | C / FP / FN | |
| 3E | | | C / FP / FN | |

**Calibration Score**: C count / total predictions = ____%

*C = Correct (prediction matched finding). FP = False Positive (predicted finding did not materialize). FN = False Negative (unpredicted finding appeared).*

If score < 60%: identify which phase predictions were structurally wrong and what assumption produced the error.

---

*End of V-05 prompt body.*
