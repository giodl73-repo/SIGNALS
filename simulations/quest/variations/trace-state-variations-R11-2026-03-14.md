Now I have the full picture: R10 scored 93.62 with the Standards Registry innovation (V-01), but left eight PARTIAL gaps: C-06 (negative-path step), C-14 (min-found threshold), C-16/C-36 (Phase 3E truncated), C-17 (anomaly register ID columns), C-21/C-25 (C/FP/FN reconciliation), C-23 (score-aloud as named discipline), C-29 (acquittal-advocate conditional).

R11 variations target those gaps with three single-axis and two combined-axis approaches.

---

# trace-state — Round 11 Variations

---

## V-01

**Variation axis**: Role sequence — Standards Registry (pre-game immutable lock for all 6 phases) + fully expanded Phase 3E peer template + negative-path step required in trace
**Hypothesis**: R10 V-01 locked Phase 3E's evidence standard in the Standards Registry but truncated the Phase 3E structural template (C-36 PARTIAL). Completing Phase 3E as a full peer template — its own sweep table, both detection passes, Role B commitment restated from registry, Gap Record, three-gate exit — repairs C-36 without restructuring the registry innovation. Adding a mandatory negative-path step in Part 2 closes C-06.

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or **Finance**. Choose one and state it now. You will hand-compile an entity state machine, trace a realistic operation sequence, then run a five-phase anomaly sweep using a structured two-role protocol.

**Role A — Detector**: runs both detection passes in each phase.
**Role B — Evidence Steward**: locks all evidence standards before detection begins; produces a Gap Record after every phase unconditionally.

---

## PART 0: STANDARDS REGISTRY [COMPLETE BEFORE PART 1 OPENS]

Before any declaration table is built, Role B locks the evidence standard for every phase. This registry is sealed the moment Part 1 opens. No standard may be revised after findings in any phase are known.

| Phase | Anomaly Type | Evidence Required (specific) | Minimum Strength | What Constitutes a Finding | What Does NOT |
|-------|-------------|------------------------------|-----------------|---------------------------|---------------|
| 3A | Invalid State Transitions | | ≥2 | | |
| 3B | Missing Precondition Checks | | ≥2 | | |
| 3C | Invariant Violations | | ≥2 | | |
| 3D | Race Conditions | | ≥2 | | |
| 3E | Undeclared References | | ≥2 | | |

Complete all cells before advancing. Role B signs: *"I commit to these standards. They are sealed."*

STANDARDS REGISTRY: SEALED → PART 1 now OPEN

---

## PART 1: DECLARATION TABLES [STATUS: OPEN]

### 1A. State Registry

| S-ID | State Name | Description | Entry Condition | Exit Condition |

Minimum 5 states. Use domain-specific names (e.g., `Qualified`, `Pending Approval`, `Overdue`).

### 1B. Operation Registry

| OP-ID | Operation | From State (S-ID) | To State (S-ID) | Actor | Guard Condition | Preconditions | Postconditions |

Minimum 6 operations. At least one operation must be **explicitly rejected** (attempted but blocked by guard condition) — label it `OP-XX [REJECTED]` and document the blocking guard.

### 1C. Invariant Registry

| INV-ID | Invariant | Scope (all states / named subset) | Type | Falsifiable Threshold |

Minimum 2 invariants. At least one must be **numeric or temporal** with a precise threshold (e.g., "invoice total never decreases after OP-04; threshold: any decrease > $0.00 is a violation").

PART 1: COMPLETE → PART 2 now OPEN

---

## PART 2: HAND-COMPILED TRACE [STATUS: LOCKED until PART 1: COMPLETE]

Pick a realistic scenario and trace it step by step. For each step:

```
Step N: [OP-ID] [Operation Name]
  Before state: [S-ID] [State] — {field: value, ...}
  Preconditions checked: [list each from OP-Registry, verdict: MET / NOT MET]
  State changes: {field: old → new}
  After state: [S-ID] [State] — {field: value, ...}
  Postconditions verified: [list each, verdict: HOLDS / VIOLATED]
  Invariants checked: [INV-IDs, verdict: HOLDS / VIOLATED]
```

Minimum 6 steps. Step sequence must include **at least one negative-path step**: a `[REJECTED]` operation where the guard condition fires, the before-state is shown, and the rejection reason is stated. The entity must remain in its before-state after rejection.

PART 2: COMPLETE → PART 3 now OPEN

---

## PART 3: PRE-SWEEP HYPOTHESIS [STATUS: LOCKED until PART 2: COMPLETE]

Before detection runs, record predictions. Each prediction must name a specific scenario (not "errors may occur").

| Phase | Anomaly Type | Predicted Count | Confidence (L/M/H) | Specific Predicted Scenario |
|-------|-------------|----------------|-------------------|----------------------------|
| 3A | Invalid State Transitions | | | |
| 3B | Missing Precondition Checks | | | |
| 3C | Invariant Violations | | | |
| 3D | Race Conditions | | | |
| 3E | Undeclared References | | | |

State which phase you predict will be most productive. State your overall prediction: how many total findings across all phases?

PART 3: COMPLETE → PHASE 3A now OPEN

---

## PHASE 3A: INVALID STATE TRANSITIONS [STATUS: LOCKED until PART 3: COMPLETE]

### Role B: Evidence Standard (from Standards Registry)

Restate the Phase 3A row from the Standards Registry verbatim:
> *"For Phase 3A I require: [evidence required], minimum strength [N], constitutes a finding: [X], does not constitute a finding: [Y]."*

This restatement confirms the pre-committed standard is active for this phase.

---

### Role A: DETECTION PASS 1 — Declaration-Only

Examine the State Registry and Operation Registry alone. Do not consult trace steps.

**THE SCORING PROTOCOL**: Assign evidence strength the moment you record a finding. Say: *"I am scoring this [1/2/3] because [specific reason]."* Do not defer scoring. If you cannot complete the sentence, the evidence is insufficient — do not record the finding.

| Finding-ID | Declaration-Only Finding | OP-ID / S-ID affected | Evidence Strength (1=circumstantial, 2=direct, 3=definitive) | Strength Rationale |

If no finding in this pass: name the specific declaration-table values (state pairs, guard conditions, column entries) that would need to exist to produce a finding.

---

### Role A: DETECTION PASS 2 — Trace-Diff

Compare declaration tables against the traced step sequence. A declared behavior not demonstrated in any trace step is a finding in this pass.

| Finding-ID | Trace-Diff Finding | Step(s) | OP-ID / S-ID affected | Evidence Strength | Strength Rationale |

Score at point of discovery. If no finding: name the specific trace steps and state conditions that would need to exist.

---

### Role B: GAP RECORD [UNCONDITIONAL — fires regardless of finding count]

```
GAP RECORD — Phase 3A
Total findings: [n] (Declaration-Only: [n], Trace-Diff: [n])
Pre-committed standard: [restate threshold from Standards Registry]
Did findings meet standard? [yes/no — if no, explain]
Detection gap: [what invalid transitions might exist that neither pass reached, given the declared op set and traced steps?]
Structural limit: [what constraint prevented broader detection?]
```

*The Gap Record is the unlock signal for the Phase 3A exit gate.*

---

### PHASE 3A EXIT CERTIFICATION

- [ ] Findings List complete — all Declaration-Only and Trace-Diff findings recorded with evidence strength assigned at point of discovery
- [ ] Evidence Strength gate — at least one finding at strength ≥ 2, OR Gap Record explicitly explains why no finding met the threshold
- [ ] Gap Record present and complete

**PHASE 3A: COMPLETE** [Unlocks Phase 3B]

---

## PHASE 3B: MISSING PRECONDITION CHECKS [STATUS: LOCKED until PHASE 3A: COMPLETE]

Apply the Phase 3A structure to Missing Precondition Checks:
- Role B restatement of Phase 3B Standards Registry row
- Pass 1: Declaration-Only sweep for operations with absent, vague, or unverifiable preconditions
- Pass 2: Trace-Diff sweep for trace steps where declared preconditions were not checked (field absent, verdict missing, or checked against wrong state)
- Role B Gap Record (unconditional)
- Three-gate exit certification

**PHASE 3B: COMPLETE** [Unlocks Phase 3C]

---

## PHASE 3C: INVARIANT VIOLATIONS [STATUS: LOCKED until PHASE 3B: COMPLETE]

Apply the Phase 3A structure to Invariant Violations. All INV-IDs from the Invariant Registry must appear in at least one sweep pass — if an invariant is not checked, that absence is itself a Pass 1 finding.

**PHASE 3C: COMPLETE** [Unlocks Phase 3D]

---

## PHASE 3D: RACE CONDITIONS [STATUS: LOCKED until PHASE 3C: COMPLETE]

Apply the Phase 3A structure to Race Conditions. For Pass 1: identify operations that share the same From/To state pair or that write the same fields without an ordering guard. For Pass 2: identify trace steps where concurrent interleaving of two operations would produce an invalid intermediate state.

**PHASE 3D: COMPLETE** [Unlocks Phase 3E]

---

## PHASE 3E: UNDECLARED REFERENCES [STATUS: LOCKED until PHASE 3D: COMPLETE]

Phase 3E is a full structural peer of Phases 3A–3D. It receives identical mechanical treatment: its own sweep table with dual-column detection, Role B pre-detection commitment restated from the Standards Registry, unconditional Gap Record, and three-gate exit certification.

### Role B: Evidence Standard (from Standards Registry)

Restate the Phase 3E row from the Standards Registry verbatim:
> *"For Phase 3E I require: [evidence required], minimum strength [N], constitutes a finding: [X], does not constitute a finding: [Y]."*

---

### Role A: DETECTION PASS 1 — Declaration-Only

Scan all trace steps for field names, state labels, operation names, or INV-IDs that appear in the trace but have no corresponding row in the State Registry, Operation Registry, or Invariant Registry.

| Finding-ID | Undeclared Reference (trace uses but tables lack) | Trace Step(s) | Evidence Strength | Strength Rationale |

Score at point of discovery using the SCORING PROTOCOL.

---

### Role A: DETECTION PASS 2 — Trace-Diff

Scan the declaration tables for S-IDs, OP-IDs, and INV-IDs that are declared but never appear in any trace step.

| Finding-ID | Declared-but-Unused Reference | Registry (State/Op/Inv) | Evidence Strength | Strength Rationale |

If no finding in either pass: name the specific trace-step positions or declaration-table entries that would need to exist to produce a finding.

---

### Role B: GAP RECORD [UNCONDITIONAL]

```
GAP RECORD — Phase 3E
Total findings: [n] (Pass 1 undeclared: [n], Pass 2 unused: [n])
Pre-committed standard: [restate from Standards Registry]
Did findings meet standard? [yes/no — explain if no]
Detection gap: [what undeclared references might exist that neither pass reached?]
Structural limit: [scope constraint that bounds detection]
```

*The Gap Record is the unlock signal for the Phase 3E exit gate.*

---

### PHASE 3E EXIT CERTIFICATION

- [ ] Findings List complete — both passes recorded with evidence strength assigned at point of discovery
- [ ] Evidence Strength gate — at least one finding at strength ≥ 2, OR Gap Record explicitly explains why no finding met the threshold
- [ ] Gap Record present and complete

**PHASE 3E: COMPLETE** [Unlocks Phase 4]

---

## PHASE 4: RECONCILIATION [STATUS: LOCKED until PHASE 3E: COMPLETE]

Compare predictions (Part 3) against actual findings. For each phase, classify the outcome:
- **C** (Correct): predicted and found, or predicted none and found none
- **FP** (False Positive): predicted a finding that did not materialize
- **FN** (False Negative): did not predict a finding that actually appeared

| Phase | Anomaly Type | Predicted Count | Actual Count | C / FP / FN | What I expected to find | What I actually found / missed |
|-------|-------------|----------------|-------------|-------------|------------------------|-------------------------------|
| 3A | Invalid State Transitions | | | | | |
| 3B | Missing Precondition Checks | | | | | |
| 3C | Invariant Violations | | | | | |
| 3D | Race Conditions | | | | | |
| 3E | Undeclared References | | | | | |

**Calibration Score**: [C count] / 5 = [score].

If score < 0.6: diagnose the structural reason predictions were inaccurate. Did the declaration tables lack information that made certain anomaly types invisible at hypothesis time? Did the trace steps create evidence the declaration tables alone could not predict?

PHASE 4: COMPLETE → PHASE 5 now OPEN

---

## PHASE 5: EXIT CERTIFICATION [STATUS: LOCKED until PHASE 4: COMPLETE]

| Phase | Findings List | Evidence Strength Gate | Gap Record | COMPLETE Signal |
|-------|--------------|----------------------|-----------|----------------|
| 3A | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3B | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3C | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3D | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3E | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |

Any ✗ blocks exit. Diagnose and repair before declaring complete.

**TRACE-STATE ANALYSIS: SEALED**

---

---

## V-02

**Variation axis**: Output format — Master Anomaly Register (single unified table with S-ID/OP-ID/INV-ID columns) replaces per-phase sweep tables; phases populate the register rather than generating independent tables
**Hypothesis**: C-17 requires an anomaly register with separate OP-ID/S-ID/INV-ID columns where a blank cell in a found-verdict row is a detectable gap. R10's per-phase sweep tables do not satisfy this because each table is scoped to its phase and uses a single "affected" column. A single master register spanning all phases, with dedicated ID columns, makes cross-phase ID coverage mechanically auditable and satisfies C-17 while also serving as the natural locus for the C-14 minimum-found threshold.

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or **Finance**. Choose one and state it now. You will declare an entity state machine, hand-compile a trace, then run an anomaly sweep that populates a single Master Anomaly Register across five phases.

**Role A — Detector**: populates the Master Anomaly Register during each phase.
**Role B — Evidence Steward**: commits to evidence standards before detection begins; produces a Gap Record after every phase unconditionally.

---

## PART 0: STANDARDS REGISTRY [COMPLETE BEFORE PART 1]

| Phase | Anomaly Type | Evidence Required | Min Strength | What Constitutes Finding | What Does NOT |
|-------|-------------|-------------------|-------------|-------------------------|---------------|
| 3A | Invalid State Transitions | | ≥2 | | |
| 3B | Missing Precondition Checks | | ≥2 | | |
| 3C | Invariant Violations | | ≥2 | | |
| 3D | Race Conditions | | ≥2 | | |
| 3E | Undeclared References | | ≥2 | | |

Role B: *"Standards sealed. No revision after Phase 3A begins."*

STANDARDS REGISTRY: SEALED → PART 1 OPEN

---

## MASTER ANOMALY REGISTER [OPEN — populated incrementally across phases]

This is the single source of truth for all findings. Each row represents one finding. Blank cells in any `OP-ID`, `S-ID`, or `INV-ID` column on a finding row are detectable gaps — a finding must reference at least one ID.

| Finding-ID | Phase | Pass (Decl-Only / Trace-Diff) | Anomaly Type | OP-ID(s) | S-ID(s) | INV-ID(s) | Finding Description | Evidence Strength (1/2/3) | Strength Rationale |
|------------|-------|-------------------------------|-------------|----------|---------|----------|--------------------|--------------------------|--------------------|

Minimum-found threshold: **at least 2 findings must appear across the full register by the end of Phase 3E**. If fewer than 2 findings exist at Phase 5 exit certification, the trace scope is insufficient — expand the operation set or trace before proceeding.

---

## PART 1: DECLARATION TABLES [STATUS: OPEN]

### 1A. State Registry

| S-ID | State Name | Description | Entry Condition | Exit Condition |

Minimum 5 states. Domain-specific names required.

### 1B. Operation Registry

| OP-ID | Operation | From S-ID | To S-ID | Actor | Guard Condition | Preconditions | Postconditions |

Minimum 6 operations. Include at least one that can be attempted but rejected by its guard.

### 1C. Invariant Registry

| INV-ID | Invariant Statement | Scope | Type (state/value/temporal) | Falsifiable Threshold |

Minimum 2 invariants. At least one numeric or temporal with stated threshold.

PART 1: COMPLETE → PART 2 OPEN

---

## PART 2: HAND-COMPILED TRACE [STATUS: LOCKED until PART 1: COMPLETE]

For each step, follow this template exactly:

```
Step N: [OP-ID] [Operation Name] — [EXECUTED / REJECTED]
  Before state: [S-ID] [State] — {field: value, ...}
  Preconditions: [list each, MET / NOT MET / UNCHECKED]
  State changes: {field: old → new}   [or: "No state change — operation rejected by [guard]"]
  After state: [S-ID] [State] — {field: value, ...}
  Postconditions: [list each, HOLDS / VIOLATED]
  Invariants: [INV-IDs, HOLDS / VIOLATED / NOT CHECKED]
```

Minimum 6 steps. At least 1 step must be labeled `[REJECTED]` — a negative-path step where the guard fires and the entity remains in its before-state.

PART 2: COMPLETE → PART 3 OPEN

---

## PART 3: PRE-SWEEP HYPOTHESIS [STATUS: LOCKED until PART 2: COMPLETE]

| Phase | Anomaly Type | Predicted Count | Confidence | Specific Predicted Scenario |
|-------|-------------|----------------|-----------|----------------------------|
| 3A | Invalid State Transitions | | | |
| 3B | Missing Precondition Checks | | | |
| 3C | Invariant Violations | | | |
| 3D | Race Conditions | | | |
| 3E | Undeclared References | | | |

Name the phase predicted to yield the most findings. State your total predicted finding count.

PART 3: COMPLETE → PHASE 3A OPEN

---

## PHASE 3A: INVALID STATE TRANSITIONS [STATUS: LOCKED until PART 3: COMPLETE]

### Role B: Standards Registry Restatement

Restate Phase 3A standards row verbatim. Standards are sealed; this restatement is confirmation only.

### Role A: Detection — Populate Master Anomaly Register

**SCORING PROTOCOL**: Assign evidence strength at the moment of each finding. Before writing the row, say: *"I am scoring this [1/2/3] because [specific reason about the evidence type]."* Deferred scoring is not permitted.

Run both passes for Phase 3A:

**Pass 1 — Declaration-Only**: Examine State Registry and Operation Registry without consulting trace steps. Add any findings to the Master Anomaly Register with `Pass = Decl-Only`. If no finding: record in this section why no declaration-table combination produced a valid finding under Phase 3A's pre-committed standard.

**Pass 2 — Trace-Diff**: Diff declaration tables against traced steps. A declared behavior absent from all trace steps is a Pass 2 finding. Add to Master Anomaly Register with `Pass = Trace-Diff`. If no finding: name the specific trace steps and state combinations that would need to exist.

### Role B: GAP RECORD — Phase 3A [UNCONDITIONAL]

```
GAP RECORD — Phase 3A
Findings added to register this phase: [n] (Decl-Only: [n], Trace-Diff: [n])
Evidence standard met? [yes/no — explain if no]
Detection gap: [what invalid transitions might exist beyond the declared op set?]
Structural limit: [what bounds detection in this phase?]
```

*The Gap Record is the Phase 3A exit gate unlock signal.*

### PHASE 3A EXIT CERTIFICATION

- [ ] Register rows for this phase complete with OP-ID/S-ID/INV-ID columns populated; no blank ID cells on finding rows
- [ ] Evidence Strength gate: at least one row at strength ≥ 2, OR Gap Record explains why not
- [ ] Gap Record present and complete

**PHASE 3A: COMPLETE** [Unlocks Phase 3B]

---

## PHASE 3B: MISSING PRECONDITION CHECKS [STATUS: LOCKED until PHASE 3A: COMPLETE]

Apply the Phase 3A structure. Both detection passes add rows to the Master Anomaly Register with `Phase = 3B`. Gap Record unconditional. Three-gate exit certification.

**PHASE 3B: COMPLETE** [Unlocks Phase 3C]

---

## PHASE 3C: INVARIANT VIOLATIONS [STATUS: LOCKED until PHASE 3B: COMPLETE]

Apply the Phase 3A structure. All INV-IDs must appear in at least one register row (Pass 1 or Pass 2) or in the Gap Record explaining their absence.

**PHASE 3C: COMPLETE** [Unlocks Phase 3D]

---

## PHASE 3D: RACE CONDITIONS [STATUS: LOCKED until PHASE 3C: COMPLETE]

Apply the Phase 3A structure. Pass 1: flag operation pairs sharing From/To states or shared field writes without ordering guards. Pass 2: identify trace-step interleavings that produce invalid intermediate states.

**PHASE 3D: COMPLETE** [Unlocks Phase 3E]

---

## PHASE 3E: UNDECLARED REFERENCES [STATUS: LOCKED until PHASE 3D: COMPLETE]

Phase 3E is a full structural peer of Phases 3A–3D. Populate the Master Anomaly Register with Phase 3E rows exactly as in prior phases.

### Role B: Standards Registry Restatement

Restate Phase 3E standards row verbatim.

### Role A: Detection

**Pass 1 — Declaration-Only**: Scan trace steps for any name (field, state, operation, invariant) used but absent from all declaration tables. Add each to the Master Anomaly Register with `Phase = 3E, Pass = Decl-Only`. ID columns: use the referenced entity's type to populate the correct column (S-ID if a state name, OP-ID if an operation name, INV-ID if an invariant reference).

**Pass 2 — Trace-Diff**: Scan declaration tables for declared S-IDs, OP-IDs, INV-IDs never referenced in any trace step. Add each to the register with `Pass = Trace-Diff`.

### Role B: GAP RECORD — Phase 3E [UNCONDITIONAL]

```
GAP RECORD — Phase 3E
Findings added this phase: [n] (Decl-Only: [n], Trace-Diff: [n])
Evidence standard met? [yes/no]
Detection gap: [what undeclared references might exist in a broader trace?]
Structural limit: [scope boundary on detection]
```

*The Gap Record is the Phase 3E exit gate unlock signal.*

### PHASE 3E EXIT CERTIFICATION

- [ ] Register rows for Phase 3E complete with ID columns populated
- [ ] Evidence Strength gate satisfied or explained in Gap Record
- [ ] Gap Record present and complete

**PHASE 3E: COMPLETE** [Unlocks Phase 4]

---

## PHASE 4: RECONCILIATION [STATUS: LOCKED until PHASE 3E: COMPLETE]

| Phase | Predicted | Actual | Outcome | Predicted Scenario | Actual Finding(s) / Gap |
|-------|----------|--------|---------|-------------------|------------------------|
| 3A | | | C / FP / FN | | |
| 3B | | | C / FP / FN | | |
| 3C | | | C / FP / FN | | |
| 3D | | | C / FP / FN | | |
| 3E | | | C / FP / FN | | |

**Calibration Score**: C-count / 5. If < 0.6: identify which declaration-table information was insufficient to support accurate prediction, and what changes to the hypothesis protocol would improve calibration.

**Master Register total-row count**: [n]. If < 2 (minimum-found threshold), expand scope now — add operations to the OP Registry and extend the trace before proceeding to Phase 5.

PHASE 4: COMPLETE → PHASE 5 OPEN

---

## PHASE 5: EXIT CERTIFICATION

| Phase | Register Rows Complete (ID cols populated) | Evidence Strength Gate | Gap Record | COMPLETE |
|-------|-------------------------------------------|----------------------|-----------|----------|
| 3A | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3B | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3C | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3D | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3E | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| Master Register ≥ 2 findings | ✓/✗ | — | — | — |

Any ✗ blocks exit.

**TRACE-STATE ANALYSIS: SEALED**

---

---

## V-03

**Variation axis**: Phrasing register — score-aloud elevated to a named standalone cognitive discipline ("THE ANOMALY SCORING PROTOCOL") with a self-correction rule and mandatory mid-sweep checkpoint, placed before the sweep phases as its own numbered section
**Hypothesis**: In R10, score-at-point-of-discovery (C-22) passed but score-aloud as a named cognitive behavioral discipline (C-23) was PARTIAL — the instruction appeared in Part 2 but was not named as a behavioral discipline with a self-correction checkpoint. Extracting the scoring protocol into its own numbered section — with a named discipline title, a required narration sentence, and a mid-sweep self-correction gate — makes it a first-class protocol element the model cannot treat as optional boilerplate.

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or **Finance**. Choose one and state it now. Hand-compile a state machine, trace a scenario, and run a structured anomaly sweep.

**Role A — Detector**: runs detection passes.
**Role B — Evidence Steward**: locks evidence standards pre-detection; produces unconditional Gap Records.

---

## PART 0: STANDARDS REGISTRY [COMPLETE BEFORE PART 1]

| Phase | Anomaly Type | Evidence Required | Min Strength | What Constitutes Finding | What Does NOT |
|-------|-------------|-------------------|-------------|-------------------------|---------------|
| 3A | Invalid State Transitions | | ≥2 | | |
| 3B | Missing Precondition Checks | | ≥2 | | |
| 3C | Invariant Violations | | ≥2 | | |
| 3D | Race Conditions | | ≥2 | | |
| 3E | Undeclared References | | ≥2 | | |

Role B seals registry before Part 1 opens.

STANDARDS REGISTRY: SEALED → PART 1 OPEN

---

## PART 1: DECLARATION TABLES

### 1A. State Registry

| S-ID | State Name | Description | Entry Condition | Exit Condition |

Minimum 5 states.

### 1B. Operation Registry

| OP-ID | Operation | From S-ID | To S-ID | Actor | Guard Condition | Preconditions | Postconditions |

Minimum 6 operations.

### 1C. Invariant Registry

| INV-ID | Invariant | Scope | Type | Falsifiable Threshold |

Minimum 2 invariants; at least 1 numeric or temporal.

PART 1: COMPLETE → PART 2 OPEN

---

## PART 2: HAND-COMPILED TRACE

```
Step N: [OP-ID] [Operation] — [EXECUTED / REJECTED]
  Before state: [S-ID] — {field: value, ...}
  Preconditions: [each declared precondition — MET / NOT MET / UNCHECKED]
  State changes: {field: old → new} or "Rejected — [guard]"
  After state: [S-ID] — {field: value, ...}
  Postconditions: [each — HOLDS / VIOLATED]
  Invariants: [INV-IDs — HOLDS / VIOLATED / NOT CHECKED]
```

Minimum 6 steps. At least 1 step must be `[REJECTED]` showing a negative-path transition attempt.

PART 2: COMPLETE → PART 3 OPEN

---

## PART 3: PRE-SWEEP HYPOTHESIS

| Phase | Anomaly Type | Predicted Count | Confidence | Specific Scenario |
|-------|-------------|----------------|-----------|-------------------|
| 3A | Invalid State Transitions | | | |
| 3B | Missing Precondition Checks | | | |
| 3C | Invariant Violations | | | |
| 3D | Race Conditions | | | |
| 3E | Undeclared References | | | |

PART 3: COMPLETE → PART 4 OPEN

---

## PART 4: THE ANOMALY SCORING PROTOCOL [STATUS: OPEN — read before any detection phase begins]

**This is a named behavioral discipline, not a table footnote.** It governs how Role A assigns evidence strength in every detection pass of every phase. Compliance is mandatory; skipping it is a detectable structural error.

**THE SCORING PROTOCOL**:

> Before writing any cell in the `Evidence Strength` column, Role A must narrate aloud:
> *"I am scoring this [1/2/3] because [specific reason referencing trace step numbers, field values, or declaration-table entries]."*
>
> The three strength levels are:
> - **1 — Circumstantial**: the anomaly is structurally possible given the declared operations but not directly observed
> - **2 — Direct**: a specific trace step or declaration-table entry demonstrates the condition
> - **3 — Definitive**: multiple independent evidence sources (declaration AND trace) confirm the condition
>
> If Role A cannot complete the narration sentence for a potential finding, the evidence is insufficient — do not record the finding.

**SELF-CORRECTION CHECKPOINT**: At the midpoint of each detection pass (after examining half the operations or steps), Role A must pause and review: *"Have I assigned any strength without narrating? If yes, add the narration now before continuing."*

**PROTOCOL ACKNOWLEDGMENT**: Before Phase 3A begins, Role A states:
> *"I have read and understood THE ANOMALY SCORING PROTOCOL. I will narrate strength assignments in real time and complete the mid-pass self-correction checkpoint."*

PART 4: COMPLETE — Protocol active → PHASE 3A OPEN

---

## PHASE 3A: INVALID STATE TRANSITIONS [STATUS: LOCKED until PART 4: COMPLETE]

### Role B: Evidence Standard Restatement

> *"Phase 3A standard (from sealed registry): [restate verbatim]."*

### Role A: Protocol Acknowledgment

> *"THE ANOMALY SCORING PROTOCOL is active for this phase."*

### Pass 1 — Declaration-Only

Examine State Registry and Operation Registry. For each potential finding, narrate strength aloud before recording.

| Finding-ID | Declaration-Only Finding | OP-ID / S-ID | Evidence Strength | Narration ("I scored this [N] because...") |

**Mid-pass self-correction checkpoint**: After examining half the operations — *"No deferred scorings detected / corrected [N] deferred scorings."*

If no finding: name the declaration-table values that would need to exist.

### Pass 2 — Trace-Diff

Diff declared behavior against trace steps. Score aloud per the protocol.

| Finding-ID | Trace-Diff Finding | Step(s) | OP-ID / S-ID | Evidence Strength | Narration |

**Mid-pass self-correction checkpoint**.

If no finding: name the trace steps and state conditions that would need to exist.

### Role B: GAP RECORD [UNCONDITIONAL]

```
GAP RECORD — Phase 3A
Findings: [n] (Decl-Only: [n], Trace-Diff: [n])
Pre-committed standard: [from Standards Registry]
Standard met? [yes/no]
Detection gap: [what wasn't reachable]
Structural limit: [scope bound]
```

*Gap Record is the exit gate unlock signal.*

### PHASE 3A EXIT CERTIFICATION

- [ ] Findings recorded with real-time narration; self-correction checkpoints completed for both passes
- [ ] Evidence Strength gate: ≥1 finding at strength ≥2, OR Gap Record explains absence
- [ ] Gap Record present and complete

**PHASE 3A: COMPLETE** [Unlocks Phase 3B]

---

## PHASE 3B–3D [LOCKED in sequence, each unlocked by prior COMPLETE signal]

Apply Phase 3A structure to each anomaly type. THE ANOMALY SCORING PROTOCOL remains active. Self-correction checkpoint required at midpoint of each pass.

- **3B**: Missing Precondition Checks
- **3C**: Invariant Violations (all INV-IDs must appear in a pass or Gap Record)
- **3D**: Race Conditions (focus on operation-pair interleaving and shared-field writes)

**PHASE 3B: COMPLETE** [Unlocks 3C] | **PHASE 3C: COMPLETE** [Unlocks 3D] | **PHASE 3D: COMPLETE** [Unlocks 3E]

---

## PHASE 3E: UNDECLARED REFERENCES [STATUS: LOCKED until PHASE 3D: COMPLETE]

Full structural peer of Phases 3A–3D. THE ANOMALY SCORING PROTOCOL active. Self-correction checkpoint required.

### Role B: Evidence Standard Restatement

> *"Phase 3E standard (from sealed registry): [restate verbatim]."*

### Role A: Protocol Acknowledgment

> *"THE ANOMALY SCORING PROTOCOL is active for Phase 3E."*

### Pass 1 — Declaration-Only

Scan trace steps for names absent from declaration tables.

| Finding-ID | Undeclared Reference (in trace, absent from tables) | Trace Step | Evidence Strength | Narration |

Mid-pass self-correction checkpoint.

### Pass 2 — Trace-Diff

Scan declaration tables for declared IDs never referenced in trace steps.

| Finding-ID | Declared-but-Unused Reference | Registry | Evidence Strength | Narration |

Mid-pass self-correction checkpoint.

### Role B: GAP RECORD [UNCONDITIONAL]

```
GAP RECORD — Phase 3E
Findings: [n]
Pre-committed standard: [from Standards Registry]
Standard met? [yes/no]
Detection gap: [scope limit]
```

*Gap Record is the exit gate unlock signal.*

### PHASE 3E EXIT CERTIFICATION

- [ ] Findings recorded with real-time narration; self-correction checkpoints completed
- [ ] Evidence Strength gate satisfied or explained
- [ ] Gap Record complete

**PHASE 3E: COMPLETE** [Unlocks Phase 4]

---

## PHASE 4: RECONCILIATION [STATUS: LOCKED until PHASE 3E: COMPLETE]

| Phase | Predicted | Actual | C / FP / FN | Surprise? | Diagnosis |
|-------|----------|--------|-------------|-----------|-----------|
| 3A | | | | | |
| 3B | | | | | |
| 3C | | | | | |
| 3D | | | | | |
| 3E | | | | | |

For each FP or FN, write one sentence naming the specific declaration-table gap or trace-step evidence that caused the misprediction.

**Calibration Score**: C / 5. If < 0.6, diagnose the root cause and state what change to the hypothesis process would improve accuracy.

PHASE 4: COMPLETE → PHASE 5 OPEN

---

## PHASE 5: EXIT CERTIFICATION

| Phase | Findings+Narration | Evidence Gate | Gap Record | Protocol Checkpoints | COMPLETE |
|-------|-------------------|--------------|-----------|---------------------|----------|
| 3A | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3B | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3C | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3D | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3E | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |

**TRACE-STATE ANALYSIS: SEALED**

---

---

## V-04

**Variation axes (combined)**: Lifecycle emphasis + Role sequence — explicit depth floors per phase (minimum operations examined before no-finding declared) + Role B pre-detection commitment elevated to a structured multi-field form with named commitment fields
**Hypothesis**: R10's Standards Registry locked evidence type and strength but did not constrain depth of examination — a model could declare "no finding" after examining 1–2 operations without violating the gate. Adding explicit depth floors ("examine at least 3 distinct operations / trace steps before declaring no finding in this pass") combined with a structured Role B commitment form (with fields for minimum operations to examine, not just evidence type) closes C-14's depth requirement and reduces shallow no-finding verdicts.

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or **Finance**. Choose one and state it now.

**Role A — Detector**: runs detection passes to stated depth.
**Role B — Evidence Steward**: completes a structured PRE-DETECTION COMMITMENT FORM before each phase; produces unconditional Gap Records.

---

## PART 0: STANDARDS REGISTRY [COMPLETE BEFORE PART 1]

| Phase | Anomaly Type | Evidence Type Required | Min Strength | Finding Definition | Non-Finding Definition |
|-------|-------------|----------------------|-------------|-------------------|----------------------|
| 3A | Invalid State Transitions | | ≥2 | | |
| 3B | Missing Precondition Checks | | ≥2 | | |
| 3C | Invariant Violations | | ≥2 | | |
| 3D | Race Conditions | | ≥2 | | |
| 3E | Undeclared References | | ≥2 | | |

Role B seals. No revision after Phase 3A begins.

STANDARDS REGISTRY: SEALED → PART 1 OPEN

---

## PART 1: DECLARATION TABLES

### 1A. State Registry

| S-ID | State Name | Description | Entry Condition | Exit Condition |

Minimum 6 states.

### 1B. Operation Registry

| OP-ID | Operation | From S-ID | To S-ID | Actor | Guard Condition | Preconditions | Postconditions |

Minimum 7 operations. Include at least one that is designed to be rejected by its guard condition.

### 1C. Invariant Registry

| INV-ID | Invariant | Scope | Type | Falsifiable Threshold |

Minimum 3 invariants; at least 1 numeric or temporal.

PART 1: COMPLETE → PART 2 OPEN

---

## PART 2: HAND-COMPILED TRACE

```
Step N: [OP-ID] [Operation] — [EXECUTED / REJECTED]
  Before state: [S-ID] — {field: value, ...}
  Preconditions: [each — MET / NOT MET / UNCHECKED]
  State changes: {field: old → new} or "Rejected — guard [name] fired"
  After state: [S-ID] — {field: value, ...}
  Postconditions: [each — HOLDS / VIOLATED]
  Invariants: [each INV-ID — HOLDS / VIOLATED / NOT CHECKED]
```

Minimum 8 steps. At least 1 step must be `[REJECTED]` — the entity remains in its before-state and the guard firing is explicitly named.

PART 2: COMPLETE → PART 3 OPEN

---

## PART 3: PRE-SWEEP HYPOTHESIS

| Phase | Anomaly Type | Predicted Count | Confidence | Predicted Scenario |
|-------|-------------|----------------|-----------|-------------------|
| 3A | Invalid State Transitions | | | |
| 3B | Missing Precondition Checks | | | |
| 3C | Invariant Violations | | | |
| 3D | Race Conditions | | | |
| 3E | Undeclared References | | | |

PART 3: COMPLETE → PHASE 3A OPEN

---

## PHASE 3A: INVALID STATE TRANSITIONS [STATUS: LOCKED until PART 3: COMPLETE]

### Role B: PRE-DETECTION COMMITMENT FORM — Phase 3A

*Complete this form before Role A examines any declaration table or trace step. All fields are binding.*

```
PRE-DETECTION COMMITMENT FORM — Phase 3A
Date of commitment: [before detection begins]
Anomaly type: Invalid State Transitions
Evidence standard (from Standards Registry): [restate verbatim]
Minimum operations to examine before declaring no finding in Pass 1: [N, minimum 3]
Minimum trace steps to examine before declaring no finding in Pass 2: [N, minimum 3]
What I will look for in Pass 1: [describe the specific declaration-table pattern that would constitute a finding]
What I will look for in Pass 2: [describe the specific trace-step pattern that would constitute a finding]
What I will NOT accept as a finding: [restate non-finding definition]
Role B commitment: sealed.
```

---

### Role A: Pass 1 — Declaration-Only

Examine the State Registry and Operation Registry. **Minimum depth**: examine every OP-ID for invalid From/To state pairs. Cannot declare "no finding" having examined fewer than 3 OP-IDs.

**SCORING PROTOCOL** (active for all passes): Score evidence strength at the moment of discovery. Narrate: *"Scoring this [1/2/3] because [specific evidence]."*

| Finding-ID | Declaration-Only Finding | OP-ID / S-ID | Evidence Strength | Rationale |

Operations examined: [list OP-IDs reviewed]. If no finding: state exactly which declaration-table conditions would need to exist to produce a finding.

---

### Role A: Pass 2 — Trace-Diff

Examine trace steps. **Minimum depth**: review every trace step's From/To state pair against the OP-Registry. Cannot declare "no finding" having reviewed fewer than 3 trace steps.

| Finding-ID | Trace-Diff Finding | Step(s) | OP-ID / S-ID | Evidence Strength | Rationale |

Steps examined: [list step numbers reviewed]. If no finding: name the specific step/state combinations that would be needed.

---

### Role B: GAP RECORD — Phase 3A [UNCONDITIONAL]

```
GAP RECORD — Phase 3A
Findings: [n] (Pass 1: [n], Pass 2: [n])
Depth compliance: Pass 1 examined [N] operations (minimum 3: MET/FAILED); Pass 2 examined [N] steps (minimum 3: MET/FAILED)
Evidence standard met? [yes/no]
Detection gap: [what wasn't reachable]
Structural limit: [scope bound]
```

*Gap Record is the Phase 3A exit gate unlock signal.*

---

### PHASE 3A EXIT CERTIFICATION

- [ ] Findings List complete with evidence strength assigned at discovery
- [ ] Depth floors met: Pass 1 ≥ 3 operations examined; Pass 2 ≥ 3 trace steps examined
- [ ] Evidence Strength gate: ≥1 finding at strength ≥2, OR Gap Record explains absence
- [ ] Gap Record present and complete

**PHASE 3A: COMPLETE** [Unlocks Phase 3B]

---

## PHASE 3B: MISSING PRECONDITION CHECKS [STATUS: LOCKED until PHASE 3A: COMPLETE]

Apply Phase 3A structure. Role B completes PRE-DETECTION COMMITMENT FORM for Phase 3B before any pass. Minimum depth: 3 operations (Pass 1), 3 trace steps (Pass 2). Pass 2 focus: trace steps where a declared precondition has verdict `UNCHECKED` or is absent from the step record.

**PHASE 3B: COMPLETE** [Unlocks Phase 3C]

---

## PHASE 3C: INVARIANT VIOLATIONS [STATUS: LOCKED until PHASE 3B: COMPLETE]

Apply Phase 3A structure. Role B PRE-DETECTION COMMITMENT FORM for Phase 3C. Minimum depth: all INV-IDs examined in Pass 1; all trace steps where `Invariants` field exists examined in Pass 2. An INV-ID with no `HOLDS/VIOLATED` verdict in the trace is itself a Pass 2 finding.

**PHASE 3C: COMPLETE** [Unlocks Phase 3D]

---

## PHASE 3D: RACE CONDITIONS [STATUS: LOCKED until PHASE 3C: COMPLETE]

Apply Phase 3A structure. Role B PRE-DETECTION COMMITMENT FORM for Phase 3D. Minimum depth: examine every pair of operations sharing a From S-ID in Pass 1; examine every pair of adjacent trace steps that write the same field in Pass 2.

**PHASE 3D: COMPLETE** [Unlocks Phase 3E]

---

## PHASE 3E: UNDECLARED REFERENCES [STATUS: LOCKED until PHASE 3D: COMPLETE]

Phase 3E is a full structural peer. Role B completes PRE-DETECTION COMMITMENT FORM for Phase 3E with the same binding structure.

### Role B: PRE-DETECTION COMMITMENT FORM — Phase 3E

```
PRE-DETECTION COMMITMENT FORM — Phase 3E
Evidence standard (from Standards Registry): [restate verbatim]
Minimum trace steps to scan for undeclared names in Pass 1: [N, minimum ALL steps]
Minimum declaration rows to check for declared-but-unused in Pass 2: [N, minimum ALL rows]
What I will look for in Pass 1: [specific — field names, state labels, operation names used in steps but absent from tables]
What I will look for in Pass 2: [specific — declared IDs never appearing in any trace step]
What I will NOT accept: [restate non-finding definition]
Role B commitment: sealed.
```

### Role A: Pass 1 — Scan all trace steps for undeclared names

| Finding-ID | Undeclared Reference | Trace Step | Evidence Strength | Rationale |

### Role A: Pass 2 — Scan all declaration rows for unused declared IDs

| Finding-ID | Declared-but-Unused | Registry Row | Evidence Strength | Rationale |

### Role B: GAP RECORD [UNCONDITIONAL]

```
GAP RECORD — Phase 3E
Findings: [n]
Depth compliance: Pass 1 examined [N] steps (all: MET/FAILED); Pass 2 examined [N] rows (all: MET/FAILED)
Evidence standard met? [yes/no]
Detection gap: [what additional trace scope would expand detection?]
```

*Gap Record is the exit gate unlock signal.*

### PHASE 3E EXIT CERTIFICATION

- [ ] Findings List complete with evidence strength at point of discovery
- [ ] Depth floors met: Pass 1 all steps; Pass 2 all declaration rows
- [ ] Evidence Strength gate satisfied or explained
- [ ] Gap Record present and complete

**PHASE 3E: COMPLETE** [Unlocks Phase 4]

---

## PHASE 4: RECONCILIATION [STATUS: LOCKED until PHASE 3E: COMPLETE]

| Phase | Predicted | Actual | C / FP / FN | What Drove the Misprediction |
|-------|----------|--------|-------------|------------------------------|
| 3A | | | | |
| 3B | | | | |
| 3C | | | | |
| 3D | | | | |
| 3E | | | | |

**Calibration Score**: C / 5. Threshold: if < 0.6, diagnose which declaration table or trace scope limitation made accurate prediction impossible, and what structural change would improve the hypothesis protocol.

PHASE 4: COMPLETE → PHASE 5 OPEN

---

## PHASE 5: EXIT CERTIFICATION

| Phase | Commitment Form | Depth Floors | Evidence Gate | Gap Record | COMPLETE |
|-------|----------------|-------------|--------------|-----------|----------|
| 3A | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3B | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3C | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3D | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3E | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |

**TRACE-STATE ANALYSIS: SEALED**

---

---

## V-05

**Variation axes (combined)**: Role sequence + Output format + Phrasing register — Standards Registry (pre-game lock for all 6 phases) + Master Anomaly Register with dedicated OP-ID/S-ID/INV-ID columns + named ANOMALY SCORING PROTOCOL cognitive discipline + C/FP/FN reconciliation table with calibration gate + full Phase 3E peer template + negative-path step required
**Hypothesis**: R10 left six open PARTIALs: C-06 (negative-path), C-17 (ID-column register), C-21/C-25 (C/FP/FN reconciliation), C-23 (score-aloud discipline), C-36 (Phase 3E full template). Combining three axis mutations simultaneously targets all six: the Standards Registry and full Phase 3E template close C-35/C-36; the Master Anomaly Register with dedicated ID columns closes C-17; the named SCORING PROTOCOL cognitive discipline closes C-23; the C/FP/FN reconciliation table with calibration gate closes C-21 and C-25; the negative-path trace requirement closes C-06.

---

You are a domain expert in one of three domains: **Sales**, **Customer Service**, or **Finance**. State your domain now. You will build a state machine, compile a trace, then run a structured five-phase anomaly sweep producing a Master Anomaly Register.

**Role A — Detector**: runs detection passes; populates the Master Anomaly Register; follows THE ANOMALY SCORING PROTOCOL.
**Role B — Evidence Steward**: locks all phase standards in Part 0; produces unconditional Gap Records; restates its committed standard at the start of each phase.

---

## PART 0: STANDARDS REGISTRY [MANDATORY — complete before any other part opens]

Role B locks the evidence standard for all six phases simultaneously. Once sealed, no standard may be revised after any detection pass begins anywhere in the session.

| Phase | Anomaly Type | Specific Evidence Required | Min Strength | What IS a Finding | What IS NOT a Finding |
|-------|-------------|---------------------------|-------------|------------------|-----------------------|
| 3A | Invalid State Transitions | | ≥2 | | |
| 3B | Missing Precondition Checks | | ≥2 | | |
| 3C | Invariant Violations | | ≥2 | | |
| 3D | Race Conditions | | ≥2 | | |
| 3E | Undeclared References | | ≥2 | | |

All cells completed. Role B declares: *"Standards Registry sealed. No revision permitted after any detection pass begins."*

STANDARDS REGISTRY: SEALED → THE ANOMALY SCORING PROTOCOL may now be read → PART 1 OPEN

---

## THE ANOMALY SCORING PROTOCOL [READ BEFORE PART 1 — ACTIVE FOR ALL DETECTION PASSES]

This is a named cognitive behavioral discipline governing how Role A assigns evidence strength. It is not a table footnote. Violation is a structural error detectable at exit certification.

> **Rule 1 — Score at discovery**: Assign evidence strength the moment a potential finding is identified, not after the full pass is complete.
>
> **Rule 2 — Narrate aloud**: Before writing any Evidence Strength value, say: *"I am scoring this [1/2/3] because [specific trace step number / field value / declaration-table row that constitutes the evidence]."*
>
> **Rule 3 — Strength scale**:
> - **1 — Circumstantial**: structurally possible from the declared op set but not observed in trace steps
> - **2 — Direct**: a specific trace step or table row demonstrates the condition without inference
> - **3 — Definitive**: multiple independent sources (both Declaration-Only and Trace-Diff) confirm the same condition
>
> **Rule 4 — Insufficient-evidence block**: If Role A cannot complete the narration sentence, the evidence is insufficient. Do not record the finding.
>
> **Rule 5 — Mid-pass self-correction checkpoint**: At the halfway point of each detection pass, Role A pauses and states: *"Self-correction checkpoint: I have reviewed [N] items. All strength assignments have real-time narration: [confirmed / corrected N items]."*

**Role A acknowledges before Phase 3A begins**: *"THE ANOMALY SCORING PROTOCOL is active. I will comply with all five rules."*

---

## MASTER ANOMALY REGISTER [OPENS NOW — populated throughout all phases]

All findings from all phases and all passes are recorded in this single register. A blank cell in the `OP-ID`, `S-ID`, or `INV-ID` column on any row where a finding is recorded is a detectable mechanical gap — every finding must reference at least one ID from the declaration tables.

| Finding-ID | Phase | Pass | Anomaly Type | OP-ID(s) | S-ID(s) | INV-ID(s) | Finding Description | Evidence Strength | Narration Summary |
|------------|-------|------|-------------|----------|---------|----------|---------------------|-----------------|-------------------|

---

## PART 1: DECLARATION TABLES

### 1A. State Registry

| S-ID | State Name | Description | Entry Condition | Exit Condition |

Minimum 6 states. Domain-realistic names required (e.g., `Qualified Prospect`, `Pending Contract`, `Closed-Won` for Sales).

### 1B. Operation Registry

| OP-ID | Operation | From S-ID | To S-ID | Actor | Guard Condition | Preconditions | Postconditions |

Minimum 7 operations. At least one operation must have a guard condition that can reject the transition.

### 1C. Invariant Registry

| INV-ID | Invariant | Scope | Type | Falsifiable Threshold |

Minimum 3 invariants. At least 1 numeric or temporal with a stated threshold (e.g., "INV-02: deal value never decreases after S-04 Contract Signed; threshold: any reduction > $0 is a violation").

PART 1: COMPLETE → PART 2 OPEN

---

## PART 2: HAND-COMPILED TRACE

For each step:

```
Step N: [OP-ID] [Operation] — [EXECUTED / REJECTED]
  Before state: [S-ID] [State Name] — {field: value, ...}
  Preconditions (from OP Registry): [each precondition — MET / NOT MET / UNCHECKED]
  State changes: {field: old → new}  OR  "Rejected — guard '[guard name]' fired; entity remains in [S-ID]"
  After state: [S-ID] [State Name] — {field: value, ...}
  Postconditions (from OP Registry): [each — HOLDS / VIOLATED]
  Invariants (from INV Registry): [each INV-ID — HOLDS / VIOLATED / NOT CHECKED]
```

Minimum 8 steps. Requirements:
- At least 1 step labeled `[REJECTED]` demonstrating a guard condition blocking a transition
- At least 1 step where a postcondition verdict is explicitly recorded
- At least 1 step where an invariant is explicitly checked with `HOLDS` or `VIOLATED`

PART 2: COMPLETE → PART 3 OPEN

---

## PART 3: PRE-SWEEP HYPOTHESIS

| Phase | Anomaly Type | Predicted Count | Confidence (L/M/H) | Specific Predicted Scenario | Most Productive Phase? |
|-------|-------------|----------------|--------------------|-----------------------------|----------------------|
| 3A | Invalid State Transitions | | | | |
| 3B | Missing Precondition Checks | | | | |
| 3C | Invariant Violations | | | | |
| 3D | Race Conditions | | | | |
| 3E | Undeclared References | | | | |

Mark exactly one row "Most Productive Phase." Total predicted findings: [N].

PART 3: COMPLETE → PHASE 3A OPEN

---

## PHASE 3A: INVALID STATE TRANSITIONS [STATUS: LOCKED until PART 3: COMPLETE]

### Role B: Evidence Standard Restatement

> *"Phase 3A — from sealed Standards Registry: [restate Phase 3A row verbatim]. This standard is sealed and cannot be revised."*

### Role A: Protocol Acknowledgment

> *"THE ANOMALY SCORING PROTOCOL active for Phase 3A. Rules 1–5 in force."*

### Pass 1 — Declaration-Only

Examine State Registry and Operation Registry. For each finding, add a row to the Master Anomaly Register with `Phase=3A, Pass=Decl-Only`. Apply the SCORING PROTOCOL — narrate before writing strength.

Mid-pass checkpoint after examining half the operations: *"Checkpoint: [N] ops reviewed. Narrations: [confirmed/corrected N]."*

If no finding in this pass: *name the declaration-table values (specific column entries, state-pair combinations, guard conditions) that would need to exist to produce a finding under the Phase 3A evidence standard.*

### Pass 2 — Trace-Diff

Diff declaration tables against trace steps. Add findings to Master Anomaly Register with `Phase=3A, Pass=Trace-Diff`. Apply SCORING PROTOCOL.

Mid-pass checkpoint after reviewing half the trace steps.

If no finding: name the specific trace steps and state conditions needed.

### Role B: GAP RECORD [UNCONDITIONAL — fires regardless of finding count]

```
GAP RECORD — Phase 3A
Findings this phase: [n] (Decl-Only: [n], Trace-Diff: [n])
Pre-committed standard: [from Standards Registry — cannot be changed now]
Findings met standard? [yes/no — if no, explain]
What was not reachable: [state the structural constraint — specific declared operations or trace steps that would need to exist to find more]
Detection limit: [scope bound on this phase]
```

*The Gap Record is the unlock signal for the Phase 3A exit gate.*

### PHASE 3A EXIT CERTIFICATION

- [ ] Master Anomaly Register: all Phase 3A rows have at least one of OP-ID / S-ID / INV-ID populated; no blank ID cells on finding rows
- [ ] SCORING PROTOCOL compliance: all findings have real-time narration; mid-pass checkpoints completed for both passes
- [ ] Evidence Strength gate: ≥1 finding at strength ≥2, OR Gap Record explicitly explains why no finding met threshold
- [ ] Gap Record present, complete, and filed before this checkbox is ticked

**PHASE 3A: COMPLETE** [Unlocks Phase 3B]

---

## PHASE 3B: MISSING PRECONDITION CHECKS [STATUS: LOCKED until PHASE 3A: COMPLETE]

Apply Phase 3A structure. Role B restatement from Standards Registry. SCORING PROTOCOL active with mid-pass checkpoints. Master Anomaly Register populated with `Phase=3B` rows. Pass 2 focus: trace steps where a declared precondition has verdict `UNCHECKED` or is entirely absent. Gap Record unconditional.

**PHASE 3B: COMPLETE** [Unlocks Phase 3C]

---

## PHASE 3C: INVARIANT VIOLATIONS [STATUS: LOCKED until PHASE 3B: COMPLETE]

Apply Phase 3A structure. Pass 1: check all INV-IDs for structural violations derivable from the state machine alone. Pass 2: check all trace steps where an invariant field is affected — an INV-ID with no verdict in the trace is a Pass 2 finding.

**PHASE 3C: COMPLETE** [Unlocks Phase 3D]

---

## PHASE 3D: RACE CONDITIONS [STATUS: LOCKED until PHASE 3C: COMPLETE]

Apply Phase 3A structure. Pass 1: enumerate operation pairs sharing a From S-ID or writing overlapping fields — identify pairs without ordering guards. Pass 2: identify trace-step pairs where concurrent execution would produce an invalid intermediate state.

**PHASE 3D: COMPLETE** [Unlocks Phase 3E]

---

## PHASE 3E: UNDECLARED REFERENCES [STATUS: LOCKED until PHASE 3D: COMPLETE]

Phase 3E is a full structural peer of Phases 3A–3D. Same template, same gates, same role protocol.

### Role B: Evidence Standard Restatement

> *"Phase 3E — from sealed Standards Registry: [restate Phase 3E row verbatim]. Standard sealed."*

### Role A: Protocol Acknowledgment

> *"THE ANOMALY SCORING PROTOCOL active for Phase 3E."*

### Pass 1 — Declaration-Only

Scan every trace step for field names, state labels, operation names, or invariant identifiers used in the step record but absent from the State Registry, Operation Registry, or Invariant Registry.

Add each finding to the Master Anomaly Register with `Phase=3E, Pass=Decl-Only`. Populate the ID column corresponding to the referenced entity type (S-ID if a state name, OP-ID if an operation name, INV-ID if an invariant). Apply SCORING PROTOCOL.

Mid-pass checkpoint at the halfway trace step.

If no finding: name which trace step fields were checked and what would need to appear in them.

### Pass 2 — Trace-Diff

Scan all declaration table rows for S-IDs, OP-IDs, and INV-IDs that appear in no trace step.

Add each to the Master Anomaly Register with `Phase=3E, Pass=Trace-Diff`. Apply SCORING PROTOCOL.

Mid-pass checkpoint at the halfway declaration row.

If no finding: name which declaration-table rows were checked and what usage pattern would need to appear in the trace.

### Role B: GAP RECORD [UNCONDITIONAL]

```
GAP RECORD — Phase 3E
Findings this phase: [n] (Pass 1 undeclared: [n], Pass 2 unused: [n])
Pre-committed standard: [from Standards Registry — cannot be changed]
Standard met? [yes/no]
What was not reachable in Pass 1: [trace steps where scope was too narrow to detect more undeclared names]
What was not reachable in Pass 2: [declaration-table rows where broader trace coverage would expose more unused declarations]
Detection limit: [scope bound]
```

*The Gap Record is the Phase 3E exit gate unlock signal.*

### PHASE 3E EXIT CERTIFICATION

- [ ] Master Anomaly Register: all Phase 3E rows have correct ID column populated; no blank ID cells on finding rows
- [ ] SCORING PROTOCOL compliance: narrations present; mid-pass checkpoints completed for both passes
- [ ] Evidence Strength gate: ≥1 finding at strength ≥2, OR Gap Record explains absence
- [ ] Gap Record present and complete

**PHASE 3E: COMPLETE** [Unlocks Phase 4]

---

## PHASE 4: RECONCILIATION [STATUS: LOCKED until PHASE 3E: COMPLETE]

Compare Part 3 predictions against all findings in the Master Anomaly Register.

| Phase | Anomaly Type | Predicted | Actual | Outcome | FP Diagnosis | FN Diagnosis |
|-------|-------------|----------|--------|---------|-------------|-------------|
| 3A | Invalid State Transitions | | | C / FP / FN | | |
| 3B | Missing Precondition Checks | | | C / FP / FN | | |
| 3C | Invariant Violations | | | C / FP / FN | | |
| 3D | Race Conditions | | | C / FP / FN | | |
| 3E | Undeclared References | | | C / FP / FN | | |

- **C** (Correct): prediction matched outcome
- **FP** (False Positive): predicted finding that did not materialize — name the declaration-table gap that made it seem plausible
- **FN** (False Negative): finding appeared without prediction — name the declaration-table signal that would have enabled prediction

**Calibration Score**: C-count / 5 = [score].

If score < 0.6: diagnose whether the deficit is in declaration-table coverage (FP-prone: the tables suggest anomalies that trace steps don't confirm) or trace-step coverage (FN-prone: the trace steps reveal anomalies the tables don't hint at). State one structural change to the hypothesis process that would address the dominant failure mode.

**Master Anomaly Register summary**: [N] total findings across all phases. At least 2 findings required; if fewer, the trace scope was insufficient — do not proceed to Phase 5 without expanding the operation set.

PHASE 4: COMPLETE → PHASE 5 OPEN

---

## PHASE 5: EXIT CERTIFICATION [STATUS: LOCKED until PHASE 4: COMPLETE]

| Phase | Register Rows (ID cols populated) | Narration Compliance | Evidence Gate | Gap Record | COMPLETE Signal |
|-------|----------------------------------|---------------------|--------------|-----------|----------------|
| 3A | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3B | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3C | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3D | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| 3E | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| Standards Registry sealed before Part 1 | ✓/✗ | | | | |
| Master Register ≥ 2 findings | ✓/✗ | | | | |
| Reconciliation calibration score computed | ✓/✗ | | | | |

Any ✗ blocks exit. All ✓: **TRACE-STATE ANALYSIS: SEALED**

---

---

## Variation Summary

| Var | Single/Combined | Axis(es) | Target Gaps | Key Structural Difference |
|-----|----------------|---------|-------------|--------------------------|
| V-01 | Single | Role sequence | C-06, C-36 | Standards Registry (R10 winner) + fully expanded Phase 3E peer template + negative-path required in trace |
| V-02 | Single | Output format | C-14, C-17, C-25 | Master Anomaly Register with S-ID/OP-ID/INV-ID columns replaces per-phase tables; minimum-found threshold enforced on register row count; C/FP/FN reconciliation |
| V-03 | Single | Phrasing register | C-06, C-23, C-25 | Named ANOMALY SCORING PROTOCOL cognitive discipline with 5 rules and self-correction checkpoint as a numbered Part; negative-path step; C/FP/FN reconciliation |
| V-04 | Combined | Lifecycle emphasis + Role sequence | C-14, C-36 | Explicit depth floors per phase (min 3 ops/steps before no-finding); Role B PRE-DETECTION COMMITMENT FORM as multi-field structured artifact per phase; full Phase 3E template |
| V-05 | Combined | Role sequence + Output format + Phrasing register | C-06, C-17, C-21, C-23, C-25, C-36 | All three axes combined: Standards Registry + Master Anomaly Register with ID columns + named SCORING PROTOCOL discipline + C/FP/FN reconciliation with calibration gate + negative-path + full Phase 3E |

**Predicted discriminators**: C-17 (ID-column register) splits V-02/V-05 from V-01/V-03/V-04. C-23 (named protocol discipline) splits V-03/V-05. C-25 (C/FP/FN with calibration score) is present in V-02, V-03, V-04, V-05 — only V-01 leaves it as simple reconciliation, which may be the V-01/rest discriminator at the top of the scoring band.
