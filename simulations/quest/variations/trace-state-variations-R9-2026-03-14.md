Now I have full context. The R8 V-01 scored 97 and established C-32/C-33/C-34. The primary gap was **C-25** (three-value surprise taxonomy — reconciliation stage was a placeholder). R9 variations need to incorporate C-32/C-33/C-34 as structural baselines and fix C-25/C-21/C-23 partials.

The three R8 partials to close:
- **C-23** — score-aloud as named cognitive behavioral discipline (not just a rule)
- **C-21** — Surprise column in reconciliation table (present but not structurally required)
- **C-25** — C/FP/FN + calibration score + threshold (completely absent in R8)

---

# trace-state Skill Body — Round 9 Variations

## Axes Selected

**Single-axis (3):**
- **V-01**: Role sequence — Role B fires pre-detection (pre-commitment before each phase sweep, not post-sweep)
- **V-02**: Output format — full rigid template scaffold with named placeholder blocks
- **V-03**: Lifecycle emphasis — each of the 4 anomaly phases written out fully and independently

**Combined (2):**
- **V-04**: Role sequence (B-first) + phrasing register (conversational imperative)
- **V-05**: Template scaffold + per-phase full instruction + C-25 reconciliation stage as primary axis

---

## V-01 — Role Sequence: Pre-Detection Role B Commitment

**Axis**: Role sequence
**Hypothesis**: Role B fires *before* Role A's detection pass on each phase. The Acquittal Advocate must pre-declare the exact evidence standard before searching begins, preventing post-hoc gap rationalization and producing stronger gap maps.

---

```
You are executing the trace-state skill for [TOPIC].

Domain: Choose one — Sales (opportunity, quote, order, account), Customer Service
(ticket, case, escalation, SLA), or Finance (invoice, payment, ledger entry,
approval). State your choice at the top and hold it for the entire session. All
entity names, state labels, and operation names must be recognizable to a
domain expert in that field.

---

STAGE 0 — DECLARATION

Build three registry tables before any trace work begins.

Table A — State Registry
| S-ID | State Name | Entry Condition | Exit Conditions | Invariants That Hold |

Table B — Operation Registry
| OP-ID | Operation Name | From States | To States | Preconditions | Postconditions |

Table C — Invariant Registry
| INV-ID | Invariant Statement | Scope (states) | Falsification Test |

Requirement: At least one INV must be numeric or temporal — a specific threshold
or duration that can be tested with a number (e.g., "INV-03: approval timeout
must not exceed 48 hours").

Phase 0 exit gate (check each):
[ ] Minimum 3 S-IDs, 3 OP-IDs, 3 INV-IDs declared
[ ] At least 1 numeric/temporal INV present
[ ] Entry Condition column populated for every state
[ ] No undeclared references exist at this point

STAGE 0: COMPLETE → STAGE 1: OPEN

---

STAGE 1 — PRE-SWEEP HYPOTHESIS

Before any detection work, record your predictions. You will reconcile these
against findings in Stage 4.

Hypothesis Table:
| H-ID | Anomaly Type | Predicted Finding | Predicted Severity | Confidence (L/M/H) |

Rules: Minimum 3 predictions, one per anomaly type. State specifically which
OP-IDs and S-IDs you expect to be involved. Vague predictions ("errors may
exist") are not valid.

STAGE 1: COMPLETE → STAGE 2: OPEN

---

STAGE 2 — TRACE

Produce a numbered step-by-step trace through the entity lifecycle.

Step Template (repeat for every operation):
  Step N — [OP-ID] [Operation Name]
  Before state: [S-ID] [State Name]
  Preconditions: [list each, state-specific — not "data is valid"]
  Operation: [what executes]
  Postconditions: [list each guaranteed fact after execution]
  After state: [S-ID] [State Name]
  Evidence strength: [1 = weak / 2 = moderate / 3 = strong — assign NOW,
    before writing the next step]

Requirements:
- Minimum 5 steps
- At least 1 negative-path step: an operation attempted from an invalid
  start state, showing exactly which precondition fails and why
- At least 1 concurrent-access step: two operations overlapping with a
  named window-of-vulnerability and stated resolution

STAGE 2: COMPLETE → STAGE 3: OPEN

---

STAGE 3 — ANOMALY SWEEP

The sweep runs as four top-level phases, executed sequentially. Each phase is
LOCKED until the prior phase emits its COMPLETE declaration.

ROLE PROTOCOL — applies to every phase, unconditionally:

  Before Role A begins detection on each phase:
  Role B — Acquittal Advocate fires first.

  Role B pre-commitment:
  "To find a [ANOMALY TYPE] in this domain, I would need to observe:
   [name specific trace steps, state conditions, or evidence that would
   constitute a finding — at minimum: which OP-ID, which S-ID transition,
   and which INV-ID or precondition would need to fail]"

  Role B then records the committed standard in the Gap Record template
  header BEFORE Role A searches.

  Role A — Detective then performs the detection sweep using the
  committed standard as the acceptance criterion.

  After Role A completes, Role B produces the Gap Record unconditionally:
  Gap Record fields:
    - Evidence standard committed: [from pre-commitment]
    - Evidence found: [what Role A located, or "None"]
    - What was searched but not found: [specific trace steps and states
      examined that did not meet the standard]
    - Conclusion: [FINDING CONFIRMED / FINDING NOT MET]

  The Gap Record is the unlock signal for the phase exit gate.
  The exit gate does not open until the Gap Record is signed by Role B.

---

PHASE 3A — INVALID STATE TRANSITIONS
STATUS: LOCKED (opens when STAGE 2: COMPLETE is emitted)

  Role B pre-commitment fires here (see ROLE PROTOCOL above).

  Role A — Detection:
  Pass 1 (Declaration-Only): Scan Table B for any OP-IDs whose listed
  "From States" include states where that operation should not be legal.
  Pass 2 (Trace-Diff): Scan the Step sequence for any step where the
  actual Before State does not match the declared From States for that OP-ID.

  Sweep Table:
  | OP-ID | Declaration-Only Finding | Trace-Diff Finding | Evidence Strength |
  A "None" in either column requires an inline gap record: exactly what
  was examined and why no finding met the committed standard.

  Findings List: [1. ... or None]
  Gap Record: [Role B produces, unconditionally — see ROLE PROTOCOL]

  Minimum expected findings: 1. If zero findings: the Gap Record must
  explain specifically why the state machine has no invalid transition risk,
  naming the structural properties that prevent it.

PHASE 3A: COMPLETE → PHASE 3B: OPEN

---

PHASE 3B — MISSING PRECONDITION CHECKS
STATUS: LOCKED

  Role B pre-commitment fires here.

  Role A — Detection:
  Pass 1 (Declaration-Only): For each OP-ID in Table B, verify that every
  declared precondition has a mechanism to be checked or enforced.
  Pass 2 (Trace-Diff): In the trace, find any step where the precondition
  list is vague, absent, or could be bypassed by a racing concurrent operation.

  Sweep Table:
  | OP-ID | Declaration-Only Finding | Trace-Diff Finding | Evidence Strength |

  Findings List: [1. ... or None]
  Gap Record: [Role B produces, unconditionally]

  Minimum expected findings: 1.

PHASE 3B: COMPLETE → PHASE 3C: OPEN

---

PHASE 3C — INVARIANT VIOLATIONS
STATUS: LOCKED

  Role B pre-commitment fires here.

  Role A — Detection:
  Pass 1 (Declaration-Only): For each INV-ID in Table C, check whether any
  operation in Table B could transition into a state where the invariant
  fails.
  Pass 2 (Trace-Diff): Walk the trace steps and test each INV against the
  after-state at every step.

  Sweep Table:
  | INV-ID | Declaration-Only Finding | Trace-Diff Finding | Evidence Strength |

  Findings List: [1. ... or None]
  Gap Record: [Role B produces, unconditionally]

  Minimum expected findings: 1.

PHASE 3C: COMPLETE → PHASE 3D: OPEN

---

PHASE 3D — RACE CONDITIONS
STATUS: LOCKED

  Role B pre-commitment fires here.

  Role A — Detection:
  Pass 1 (Declaration-Only): Identify operations in Table B that write the
  same state field and could interleave.
  Pass 2 (Trace-Diff): Using the concurrent step from Stage 2, document the
  exact window of vulnerability: which state field is contested, the time
  window, and the failure mode.

  Sweep Table:
  | OP-ID pair | Declaration-Only Finding | Trace-Diff Finding | Evidence Strength |

  Findings List: [1. ... or None]
  Gap Record: [Role B produces, unconditionally]

PHASE 3D: COMPLETE → STAGE 4: OPEN

---

STAGE 4 — RECONCILIATION

Score-Aloud Discipline (named behavioral constraint):
Before writing any reconciliation row, say the verdict aloud:
"Prediction H-[ID] — I am classifying this as [C / FP / FN] because [reason]."
Then write it. Do not compute the final calibration score first and work
backwards. If you catch yourself filling the table silently, stop, restate
the current row aloud, and correct.

Reconciliation Table:
| H-ID | Predicted Finding | Actual Finding | Verdict | Verdict Reason |

Verdict classifications:
- C (Correct): prediction was confirmed by a Phase 3A–3D finding
- FP (False Positive): prediction not confirmed — anomaly type absent
- FN (False Negative): finding emerged in sweep that was not predicted

Calibration Score = C / (C + FP + FN)
If Calibration Score < 0.5: the pre-sweep hypothesis showed structural
miscalibration. Document which anomaly type was most mispredicted and
state the structural diagnosis (e.g., "hypothesis was declaration-biased —
I predicted doc gaps but the trace-diff pass surfaced the real anomalies").

STAGE 4: COMPLETE

---

EXIT CERTIFICATION

[ ] All four anomaly phases completed and COMPLETE declared
[ ] Every phase has both a Findings List and a signed Gap Record
[ ] Gap Record present even for phases with findings (gap covers what was NOT found)
[ ] Reconciliation table complete with C/FP/FN verdicts and calibration score
[ ] Calibration score computed; structural diagnosis written if score < 0.5
[ ] All IDs in trace and sweep tables resolve to declared S-ID / OP-ID / INV-ID
```

---

## V-02 — Output Format: Rigid Fill-In Template Scaffold

**Axis**: Output format
**Hypothesis**: A rigid fill-in scaffold with explicitly named placeholder blocks mechanically enforces C-33's symmetric phase output contract. The Gap Record slot exists in the template whether or not findings were discovered, making its absence a visible structural error rather than an omission judgment call.

---

```
You are executing the trace-state skill for [TOPIC].

Domain lock: [SALES / CUSTOMER SERVICE / FINANCE — choose one, state here]
Domain entities in scope: [list 2-3 entity names from your chosen domain]

Complete every template block in sequence. Do not skip blocks. Blocks marked
GAP RECORD are required unconditionally regardless of finding count.

===================================================================
BLOCK 1 — STATE REGISTRY
===================================================================
| S-ID | State Name | Entry Condition | Exit Conditions | Invariants That Hold |
|------|------------|-----------------|-----------------|----------------------|
| S-01 | [name]     | [condition]     | [conditions]    | [INV-IDs]            |
| S-02 | ...        |                 |                 |                      |
| S-03 | ...        |                 |                 |                      |
[minimum 4 rows]

===================================================================
BLOCK 2 — OPERATION REGISTRY
===================================================================
| OP-ID | Operation Name | From States | To States | Preconditions | Postconditions |
|-------|----------------|-------------|-----------|---------------|----------------|
| OP-01 | [name]         | [S-IDs]     | [S-IDs]   | [list]        | [list]         |
[minimum 4 rows]

===================================================================
BLOCK 3 — INVARIANT REGISTRY
===================================================================
| INV-ID | Invariant Statement | Scope | Falsification Test |
|--------|---------------------|-------|--------------------|
| INV-01 | [statement]         | [S-IDs]| [test]            |
[minimum 3 rows — at least 1 must be numeric or temporal]

Numeric/temporal invariant gate:
  INV that meets the requirement: [INV-ID]
  The specific number or duration: [value + units]

BLOCK 1-3: COMPLETE → BLOCK 4: OPEN

===================================================================
BLOCK 4 — PRE-SWEEP HYPOTHESIS
===================================================================
| H-ID | Anomaly Type | Predicted Finding | Predicted OP-ID / S-ID | Confidence |
|------|-------------|-------------------|------------------------|------------|
| H-01 | [type]      | [description]     | [IDs]                  | [L/M/H]    |
| H-02 | ...         |                   |                        |            |
| H-03 | ...         |                   |                        |            |
[minimum 3 rows, one per anomaly type]

BLOCK 4: COMPLETE → BLOCK 5: OPEN

===================================================================
BLOCK 5 — TRACE SEQUENCE
===================================================================

For each step, fill the template completely. Evidence strength is assigned
at point of writing, not retroactively.

  STEP 01 — [OP-ID]: [Operation Name]
  Before state:    [S-ID] [State Name]
  Preconditions:   [1. ... 2. ...]
  Operation:       [description]
  Postconditions:  [1. ... 2. ...]
  After state:     [S-ID] [State Name]
  Evidence strength: [1 / 2 / 3]
  Score-aloud: "This step's evidence strength is [N] because [reason]."

  STEP 02 — ...
  [repeat template]

  [minimum 5 steps]

  NEGATIVE PATH STEP (required):
  STEP N — [OP-ID]: [Operation Name] — REJECTED
  Attempted from state: [S-ID]
  Rejection reason: [which precondition fails — state-specific]
  After state: [unchanged — S-ID]
  Evidence strength: [1 / 2 / 3]
  Score-aloud: "..."

  CONCURRENT STEP (required):
  STEP N — [OP-ID-A] || [OP-ID-B]: Concurrent Execution
  Contended state field: [field name]
  Window of vulnerability: [description of overlap window]
  Failure mode: [what breaks]
  Resolution mechanism: [lock / saga / retry / etc.]
  Evidence strength: [1 / 2 / 3]
  Score-aloud: "..."

BLOCK 5: COMPLETE → BLOCK 6: OPEN

===================================================================
BLOCK 6A — PHASE: INVALID STATE TRANSITIONS
STATUS: LOCKED until BLOCK 5: COMPLETE
===================================================================

SWEEP TABLE:
| OP-ID | Declaration-Only Finding | Trace-Diff Finding | Strength |
|-------|--------------------------|---------------------|----------|
| OP-01 | [finding or: None — gap: ...]| [finding or: None — gap: ...]| [1/2/3] |
[one row per OP-ID]

For any cell containing "None": replace with inline gap record:
  None — gap: [exact steps/states examined; why no finding met the standard]

FINDINGS LIST:
  1. [finding — or: None]

==================
GAP RECORD — BLOCK 6A [REQUIRED — UNCONDITIONAL]
==================
  What was searched: [list trace steps and declaration rows examined]
  Evidence threshold applied: [the specific criterion for a valid finding]
  What was not found: [what searched evidence failed to surface]
  Phases with findings still require this record: document what the
  sweep did NOT catch, not just what it did.
  Role B signature: ___________________

THIS GAP RECORD IS THE UNLOCK SIGNAL FOR BLOCK 6A EXIT GATE.
The exit gate does not open until the Gap Record is complete.

BLOCK 6A: COMPLETE → BLOCK 6B: OPEN

===================================================================
BLOCK 6B — PHASE: MISSING PRECONDITION CHECKS
STATUS: LOCKED until BLOCK 6A: COMPLETE
===================================================================

SWEEP TABLE:
| OP-ID | Declaration-Only Finding | Trace-Diff Finding | Strength |
[one row per OP-ID; inline gap records on any None cell]

FINDINGS LIST:
  1. [finding — or: None]

==================
GAP RECORD — BLOCK 6B [REQUIRED — UNCONDITIONAL]
==================
  What was searched: [...]
  Evidence threshold applied: [...]
  What was not found: [...]
  Role B signature: ___________________

BLOCK 6B: COMPLETE → BLOCK 6C: OPEN

===================================================================
BLOCK 6C — PHASE: INVARIANT VIOLATIONS
STATUS: LOCKED until BLOCK 6B: COMPLETE
===================================================================

SWEEP TABLE:
| INV-ID | Declaration-Only Finding | Trace-Diff Finding | Strength |
[one row per INV-ID; inline gap records on any None cell]

FINDINGS LIST:
  1. [finding — or: None]

==================
GAP RECORD — BLOCK 6C [REQUIRED — UNCONDITIONAL]
==================
  What was searched: [...]
  Evidence threshold applied: [...]
  What was not found: [...]
  Role B signature: ___________________

BLOCK 6C: COMPLETE → BLOCK 6D: OPEN

===================================================================
BLOCK 6D — PHASE: RACE CONDITIONS
STATUS: LOCKED until BLOCK 6C: COMPLETE
===================================================================

SWEEP TABLE:
| OP-ID Pair | Declaration-Only Finding | Trace-Diff Finding | Strength |
[one row per concurrent-capable pair; inline gap records on any None cell]

FINDINGS LIST:
  1. [finding — or: None]

==================
GAP RECORD — BLOCK 6D [REQUIRED — UNCONDITIONAL]
==================
  What was searched: [...]
  Evidence threshold applied: [...]
  What was not found: [...]
  Role B signature: ___________________

BLOCK 6D: COMPLETE → BLOCK 7: OPEN

===================================================================
BLOCK 7 — RECONCILIATION
===================================================================

Score-Aloud Behavioral Discipline:
For each row, say the verdict before writing:
"H-[ID]: I am classifying this as [C / FP / FN] because [reason]."
Name this discipline as you apply it. If you realize you've written a
row silently, mark it with [SILENT — RESTATE] and restate it before
continuing.

RECONCILIATION TABLE:
| H-ID | Predicted Finding | Actual Finding | Verdict (C/FP/FN) | Verdict Reason |
|------|------------------|----------------|-------------------|----------------|
| H-01 | [...]            | [...]          | [C/FP/FN]         | [reason]       |
| H-02 | ...              |                |                   |                |
| H-03 | ...              |                |                   |                |

Add FN rows for any sweep findings not predicted:
| FN-01 | [not predicted] | [actual finding] | FN | [why it wasn't predicted] |

Calibration Score: [C count] / ([C count] + [FP count] + [FN count]) = [score]

If score < 0.5:
  Structural diagnosis: [which anomaly type was most mispredicted and why]
  Recalibration note: [what hypothesis pattern would have been more accurate]

BLOCK 7: COMPLETE

===================================================================
EXIT CERTIFICATION
===================================================================
[ ] All four phases (6A–6D) have COMPLETE declarations
[ ] Every phase has both a Findings List and an unconditional Gap Record
[ ] Every "None" sweep cell has an inline gap record (not a bare "None")
[ ] Reconciliation table complete with C/FP/FN verdicts
[ ] Calibration score computed; diagnosis written if score < 0.5
[ ] All S-IDs, OP-IDs, INV-IDs cross-referenced to declarations
[ ] Score-aloud discipline applied and named in Block 7
```

---

## V-03 — Lifecycle Emphasis: Per-Phase Full Instruction Set

**Axis**: Lifecycle emphasis
**Hypothesis**: Writing the complete instruction set independently for each of the 4 anomaly phases — rather than defining the pattern once and saying "repeat" — prevents output compression in later phases and produces symmetric depth across all four.

---

```
You are executing the trace-state skill for [TOPIC].

Choose your domain now and state it at the top of your response.
Options: Sales (opportunity, quote, order, account) |
         Customer Service (ticket, case, escalation, SLA) |
         Finance (invoice, payment, ledger entry, approval).
Every entity name, state label, and operation name must belong to your
chosen domain. A domain expert would recognize your scenario as realistic.

---

PART 1 — DECLARATIONS

1A. State Registry
| S-ID | State Name | Entry Condition | Exit Conditions | Invariants That Hold |
Minimum 4 states. Entry Condition must be populated — not left blank.

1B. Operation Registry
| OP-ID | Operation Name | From States | To States | Preconditions | Postconditions |
Minimum 4 operations. At least one must describe a rejection path.

1C. Invariant Registry
| INV-ID | Invariant Statement | Scope | Falsification Test |
Minimum 3 invariants. At least one must be numeric or temporal with a
specific threshold you can test with a number. State it: "INV-XX requires
[value] [unit] limit."

1D. ID Coverage Check
Verify every S-ID, OP-ID, INV-ID is complete before proceeding.

PART 1: COMPLETE → PART 2: OPEN

---

PART 2 — PRE-SWEEP HYPOTHESIS

Before any detection begins, commit your predictions.
| H-ID | Anomaly Type | Predicted Finding | Involved OP-ID / S-ID | Confidence |
Minimum 3 predictions (one per anomaly class: invalid transition,
missing precondition, invariant violation, race condition). Predictions
must name specific IDs. You will reconcile these in Part 5.

PART 2: COMPLETE → PART 3: OPEN

---

PART 3 — TRACE

Trace the full entity lifecycle using the step template below.

Step Template:
  Step [N] — [OP-ID]: [Operation Name]
  Before state:   [S-ID] [State Name]
  Preconditions:  [list — domain-specific, state-specific; "data is valid" FAILS]
  Operation:      [what executes]
  Postconditions: [what is guaranteed after]
  After state:    [S-ID] [State Name]
  Evidence strength: [assign NOW — 1=weak / 2=moderate / 3=strong]

Minimum 5 steps. Include:
- At least 1 negative-path step (attempted invalid operation with rejection reason)
- At least 1 concurrent step (two OP-IDs interleaving, window-of-vulnerability named)

PART 3: COMPLETE → PART 4: OPEN

---

PART 4 — ANOMALY SWEEP

Four sequential phases. Each is fully self-contained below.
Each phase carries both a Findings List and a Gap Record.
The Gap Record is produced unconditionally — a phase with findings still
requires a Gap Record documenting what was NOT found.
The Gap Record is the unlock signal. The exit gate opens when and only
when the Gap Record is complete.

---

PART 4, PHASE A — INVALID STATE TRANSITIONS
STATUS: LOCKED until PART 3: COMPLETE

What we are hunting: any OP-ID whose From States in Table 1B include states
where that operation is not legally permitted, OR any trace step where the
actual before-state contradicts the declared From States.

Detection pass 1 (Declaration-Only):
Review Table 1B row by row. For each OP-ID, ask: does the declared From
States list include any state where this operation should fail? Record
every candidate.

Detection pass 2 (Trace-Diff):
Walk the trace steps from Part 3. For each step, check whether the
Before State matches the declared From States for that OP-ID. A mismatch
is a finding.

Sweep Table:
| OP-ID | Declaration-Only Finding | Trace-Diff Finding | Evidence Strength |
Each "None" cell must contain an inline gap record:
  "None — searched [steps/rows examined]; no finding because [specific reason]"

Findings List (Phase A):
  1. [finding with OP-ID, states involved, and evidence strength — or: None]

Gap Record (Phase A) — REQUIRED, UNCONDITIONAL:
  Evidence standard applied: [what would constitute a valid finding in this phase]
  Steps and tables searched: [list]
  What was not found despite searching: [specific state transitions examined
    that did not meet the standard — not "nothing found," but "these specific
    transitions were examined and ruled out because..."]
  This record unlocks Phase A.

PART 4, PHASE A: COMPLETE → PART 4, PHASE B: OPEN

---

PART 4, PHASE B — MISSING PRECONDITION CHECKS
STATUS: LOCKED until PHASE A: COMPLETE

What we are hunting: any OP-ID whose declared preconditions cannot be
verified from the available state information, are vague enough to be
bypassed, or are absent from the trace execution.

Detection pass 1 (Declaration-Only):
For each OP-ID in Table 1B, examine its Preconditions column. Is each
precondition checkable? Does it name a specific state property or field?
Mark any precondition that is vague, implicit, or unenforced.

Detection pass 2 (Trace-Diff):
In each trace step, examine the listed Preconditions. Is each precondition
explicitly checked? Could a concurrent operation (from the Part 3 concurrent
step) bypass the check between evaluation and execution?

Sweep Table:
| OP-ID | Declaration-Only Finding | Trace-Diff Finding | Evidence Strength |
Each "None" cell: inline gap record as above.

Findings List (Phase B):
  1. [finding — or: None]

Gap Record (Phase B) — REQUIRED, UNCONDITIONAL:
  Evidence standard applied: [...]
  Steps and tables searched: [...]
  What was not found despite searching: [...]
  This record unlocks Phase B.

PART 4, PHASE B: COMPLETE → PART 4, PHASE C: OPEN

---

PART 4, PHASE C — INVARIANT VIOLATIONS
STATUS: LOCKED until PHASE B: COMPLETE

What we are hunting: any state reachable via a legal or illegal operation
in which an invariant in Table 1C is false. Special attention to the
numeric/temporal invariant — test it with actual trace values.

Detection pass 1 (Declaration-Only):
For each INV-ID, scan Table 1B for operations that could produce a state
where the invariant fails. If any OP-ID could transition the entity into
a state violating the invariant's scope, that is a candidate finding.

Detection pass 2 (Trace-Diff):
Walk the trace steps. At each after-state, evaluate all INV-IDs whose
scope includes that state. Does the after-state satisfy the invariant?
Apply the numeric/temporal INV to any step with a time-sensitive
postcondition.

Sweep Table:
| INV-ID | Declaration-Only Finding | Trace-Diff Finding | Evidence Strength |
Each "None" cell: inline gap record as above.

Findings List (Phase C):
  1. [finding — or: None]

Gap Record (Phase C) — REQUIRED, UNCONDITIONAL:
  Evidence standard applied: [...]
  Steps and tables searched: [...]
  What was not found despite searching: [...]
  This record unlocks Phase C.

PART 4, PHASE C: COMPLETE → PART 4, PHASE D: OPEN

---

PART 4, PHASE D — RACE CONDITIONS
STATUS: LOCKED until PHASE C: COMPLETE

What we are hunting: pairs of OP-IDs that write the same state field and
could interleave in a multi-user or async context, producing a window of
vulnerability where the entity reaches an inconsistent state.

Detection pass 1 (Declaration-Only):
Scan Table 1B for OP-ID pairs where the To States or Postconditions write
the same entity field. Identify which pairs share a write target.

Detection pass 2 (Trace-Diff):
Using the concurrent step from Part 3, trace the exact interleaving:
  T=1: OP-A reads state [S-ID]
  T=2: OP-B reads state [S-ID]
  T=3: OP-A writes state [S-ID + new value]
  T=4: OP-B writes state [S-ID + different value] — OP-A's write is lost
Name the window of vulnerability, the contested field, and the failure mode.

Sweep Table:
| OP-ID Pair | Declaration-Only Finding | Trace-Diff Finding | Evidence Strength |
Each "None" cell: inline gap record as above.

Findings List (Phase D):
  1. [finding — or: None]

Gap Record (Phase D) — REQUIRED, UNCONDITIONAL:
  Evidence standard applied: [...]
  Steps and tables searched: [...]
  What was not found despite searching: [...]
  This record unlocks Phase D.

PART 4, PHASE D: COMPLETE → PART 5: OPEN

---

PART 5 — RECONCILIATION

Score-Aloud Behavioral Discipline (named cognitive constraint):
This is not a reminder. It is a required named behavioral protocol.
Label it "SCORE-ALOUD DISCIPLINE" at the start of this section.
For each reconciliation row, before writing the verdict, speak:
  "H-[ID]: I am classifying this [prediction] as [C/FP/FN] because [reason]."
Write the spoken verdict into the Verdict Reason column verbatim.
If you did not speak a row before writing it, annotate it [SILENT — RESTATE]
and restate it immediately.

RECONCILIATION TABLE:
| H-ID | Predicted Finding | Actual Outcome | Verdict (C/FP/FN) | Verdict Reason (spoken) |
|------|------------------|----------------|-------------------|------------------------|
[one row per H-ID; add FN rows for unplanned findings]

Verdict classification:
- C (Correct): prediction matched an actual finding
- FP (False Positive): predicted finding not confirmed
- FN (False Negative): actual finding not predicted

Calibration Score = C / (C + FP + FN)

If score < 0.5:
  Structural diagnosis required: name the anomaly type most mispredicted.
  State whether the hypothesis was declaration-biased, trace-biased, or
  systematically over- or under-predicted for a specific anomaly class.
  What hypothesis approach would have been better calibrated?

PART 5: COMPLETE

---

FINAL EXIT GATE
[ ] Parts 1–5 all carry COMPLETE declarations
[ ] Phases A, B, C, D each have: Findings List + Gap Record (both always present)
[ ] No "None" sweep cell without an inline gap record
[ ] Reconciliation table has C/FP/FN verdicts for every row
[ ] Calibration score computed; diagnosis present if score < 0.5
[ ] SCORE-ALOUD DISCIPLINE applied and labeled in Part 5
[ ] All references use declared S-ID / OP-ID / INV-ID
```

---

## V-04 — Combined: Role Sequence (B-First) + Conversational Register

**Axes**: Role sequence + phrasing register
**Hypothesis**: A conversational imperative register — "before you search, decide what you're hunting for" — with Role B leading creates active commitment rather than procedural compliance. The "you" voice makes each gate feel like a deliberate choice, not a checkbox.

---

```
You are executing trace-state for [TOPIC].

First: pick your domain. Write it at the top.
  - Sales: opportunity, quote, order, account
  - Customer Service: ticket, case, escalation, SLA
  - Finance: invoice, payment, ledger entry, approval

Stay in that domain the entire time. Every state name, operation name,
and entity must be something a real domain expert would use on the job.

---

STEP 1 — BUILD YOUR REGISTERS

You need three tables before you touch anything else.

States table — columns: S-ID, State Name, Entry Condition, Exit Conditions,
  Invariants That Hold
  (Fill in Entry Condition for every row. Blank = incomplete.)

Operations table — columns: OP-ID, Operation Name, From States, To States,
  Preconditions, Postconditions
  (Preconditions must name specific state properties — "data is valid" is not
  a precondition, it's a placeholder.)

Invariants table — columns: INV-ID, Invariant Statement, Scope, Falsification Test
  At least one invariant must be numeric or temporal. Name a real threshold:
  a duration, a count, a dollar limit. Make it falsifiable.

Minimums: 4 states, 4 operations, 3 invariants.

When you're done, check: can you trace every reference back to a declared ID?
If yes, write: STEP 1: COMPLETE

---

STEP 2 — COMMIT YOUR PREDICTIONS

Before you search for anything, write down what you expect to find.

| H-ID | Anomaly Class | What I Expect to Find | Which IDs Are Involved | My Confidence |

Three predictions minimum, one per anomaly class. Name the OP-IDs and S-IDs
you think will be involved. Vague predictions don't count — "errors may
exist" tells you nothing and will look bad when you reconcile.

When you're done: STEP 2: COMPLETE

---

STEP 3 — TRACE THE LIFECYCLE

Walk through your domain entity from creation to close. For each operation:

  Step N — [OP-ID]: [Operation Name]
  Before state:   [S-ID]
  Preconditions:  [list — be specific]
  Operation:      [what happens]
  Postconditions: [what's guaranteed now]
  After state:    [S-ID]
  Evidence strength: [1 / 2 / 3 — assign this NOW, before writing the next step]

Do this for at least 5 steps. Include:
- One step where the operation is rejected: which precondition fails, and why
- One step where two operations are running concurrently: name the contested
  state field, the window where they overlap, and what goes wrong

The evidence strength rule: assign it the moment you write the step.
If you're tempted to go back and assign strengths after the whole trace is
done, don't. You lose calibration signal when you score in hindsight.

STEP 3: COMPLETE

---

STEP 4 — SWEEP FOR ANOMALIES

Four phases, in order. Each phase is locked until the previous one finishes.

Here's the discipline for every phase, no exceptions:

  Before you look for anything, decide what a finding would look like.

  Ask yourself: "To find [ANOMALY TYPE] in this domain, I would need to see
  [describe specifically — which OP-ID, which state transition, which
  precondition or invariant would need to fail]. That's my acceptance
  criterion."

  Write that down first. That's your committed standard.

  Then search — declaration tables first, trace second.

  After you search, produce the Gap Record. Every phase gets one.
  Even if you found something, write what you did NOT find. The sweep
  covered territory that turned up nothing — document that territory.
  The Gap Record is not a consolation prize for when you come up empty.
  It's the record of what you looked at. It's also what opens the exit gate.
  The exit gate stays closed until you hand over the Gap Record.

---

PHASE 4A — INVALID STATE TRANSITIONS
STATUS: LOCKED (opens when Step 3: COMPLETE)

  Acceptance criterion (write yours here before searching):
  "To find an invalid state transition, I would need to observe: [...]"

  Search — Declaration-Only pass:
  Check every OP-ID in your Operations table. Are there From States listed
  where that operation shouldn't be legal?

  Search — Trace-Diff pass:
  Walk your trace steps. Does each step's Before State match the declared
  From States for that OP-ID?

  Sweep table:
  | OP-ID | Declaration-Only | Trace-Diff | Evidence Strength |
  Any cell with "None": explain inline what you looked at and why no
  finding met your acceptance criterion.

  Findings:
    1. [or None]

  Gap Record — Phase 4A (write this regardless of finding count):
    Acceptance criterion you committed to: [copy from above]
    What you actually searched: [trace steps and table rows]
    What you searched and didn't find: [be specific — these state
      transitions were examined and ruled out because...]
    
  This Gap Record opens Phase 4A's exit gate.

PHASE 4A: COMPLETE → PHASE 4B: OPEN

---

PHASE 4B — MISSING PRECONDITION CHECKS
STATUS: LOCKED

  Acceptance criterion (write yours here first):
  "To find a missing precondition check, I would need to see: [...]"

  Search — Declaration-Only pass:
  For each OP-ID, is every precondition checkable? Is there a mechanism
  that enforces it, or is it just a documented hope?

  Search — Trace-Diff pass:
  In each trace step, is the precondition explicitly checked? Could the
  concurrent step from Phase 3 bypass a check between evaluation and
  execution?

  Sweep table:
  | OP-ID | Declaration-Only | Trace-Diff | Evidence Strength |

  Findings:
    1. [or None]

  Gap Record — Phase 4B (unconditional):
    Acceptance criterion: [...]
    Searched: [...]
    Not found: [...]

PHASE 4B: COMPLETE → PHASE 4C: OPEN

---

PHASE 4C — INVARIANT VIOLATIONS
STATUS: LOCKED

  Acceptance criterion:
  "To find an invariant violation, I would need to see: [...]"
  (Include your numeric/temporal invariant — what value would need to be
  exceeded for it to fail?)

  Search — Declaration-Only pass:
  For each INV-ID, which operations could transition the entity into a
  state where the invariant fails?

  Search — Trace-Diff pass:
  At each after-state in your trace, test every INV whose scope includes
  that state. Apply the numeric invariant with actual trace values.

  Sweep table:
  | INV-ID | Declaration-Only | Trace-Diff | Evidence Strength |

  Findings:
    1. [or None]

  Gap Record — Phase 4C (unconditional):
    Acceptance criterion: [...]
    Searched: [...]
    Not found: [...]

PHASE 4C: COMPLETE → PHASE 4D: OPEN

---

PHASE 4D — RACE CONDITIONS
STATUS: LOCKED

  Acceptance criterion:
  "To find a race condition, I would need to see: [...]"
  (Name the specific state field and the two operations that could contest it.)

  Search — Declaration-Only pass:
  Find OP-ID pairs that write the same entity field. Which pairs share a
  write target?

  Search — Trace-Diff pass:
  Using your concurrent step from Step 3, trace the exact interleaving.
  Map it as a timeline: T=1, T=2, T=3, T=4. Name the window.

  Sweep table:
  | OP-ID Pair | Declaration-Only | Trace-Diff | Evidence Strength |

  Findings:
    1. [or None]

  Gap Record — Phase 4D (unconditional):
    Acceptance criterion: [...]
    Searched: [...]
    Not found: [...]

PHASE 4D: COMPLETE → STEP 5: OPEN

---

STEP 5 — RECONCILE YOUR PREDICTIONS

This is the SCORE-ALOUD DISCIPLINE. Don't skip it.

Before you write each row of the reconciliation table, say the verdict
out loud:
  "Prediction H-[ID]: I'm calling this [C / FP / FN] because [reason]."

Then write it. Not the other way around.

If you find yourself filling in the table silently, stop. Annotate that
row [SILENT — RESTATE] and restate it before moving on. The discipline
exists because it's easy to talk yourself into a verdict when you see
the answer first and work backwards. Saying it first commits you.

RECONCILIATION TABLE:
| H-ID | My Prediction | What Actually Happened | Verdict | Why (spoken first) |

Verdicts:
  C — my prediction matched a real finding
  FP — I predicted something that wasn't there
  FN — something was found that I didn't predict (add a row for each)

Calibration Score = C / (C + FP + FN)

If your score comes out below 0.5, something went wrong with your
hypothesis strategy. Write a diagnosis:
  - Which anomaly type did you get most wrong?
  - Were you declaration-biased (only expecting doc gaps, missing trace issues)?
  - Were you too conservative or too aggressive on a specific class?
  - What would a better-calibrated hypothesis have looked like?

STEP 5: COMPLETE

---

DONE WHEN:
[ ] All four phases have COMPLETE declarations
[ ] Every phase has a Findings List and a Gap Record — both, always
[ ] No sweep cell says "None" without an inline gap record
[ ] Reconciliation table has C/FP/FN verdicts and a calibration score
[ ] Score < 0.5 triggers a written structural diagnosis
[ ] SCORE-ALOUD DISCIPLINE labeled and applied in Step 5
[ ] Every ID in the trace resolves to a declared entry
```

---

## V-05 — Combined: Template Scaffold + Per-Phase Full Instruction + C-25 as Primary Axis

**Axes**: Output format (rigid template) + lifecycle emphasis (per-phase full instruction) + C-25 as structural spine
**Hypothesis**: Making the C/FP/FN reconciliation stage the design anchor — rather than a closing formality — propagates backwards: it forces hypothesis specificity in Stage 1 and evidence-strength discipline at every trace step, because the reconciliation table needs specific, assigned-at-discovery values to produce a valid calibration score.

---

```
You are executing the trace-state skill for [TOPIC].

Domain: [SALES / CUSTOMER SERVICE / FINANCE]
This selection is binding. All S-IDs, OP-IDs, and INV-IDs must use
domain-native vocabulary that a practitioner in your chosen field
would use without translation.

Design anchor for this session: the Reconciliation Stage in Section 5
requires a calibration score with C/FP/FN classification. Every structural
decision upstream — hypothesis precision, evidence strength assignment,
sweep depth — is an input to that score. Optimize for a high-quality
reconciliation, not a clean sweep table.

---

SECTION 1 — DECLARATIONS

Complete all three tables before proceeding. No forward references.

STATE REGISTRY
| S-ID | State Name | Entry Condition | Exit Conditions | Invariants That Hold |
| S-01 |            |                 |                 |                      |
[4+ rows]

OPERATION REGISTRY
| OP-ID | Operation Name | From States | To States | Preconditions | Postconditions |
| OP-01 |                |             |           |               |                |
[4+ rows]
Precondition quality standard: each precondition must name a specific
state property or field. "Data is valid" and "user is authenticated"
are not preconditions — they are assertions without a referent.

INVARIANT REGISTRY
| INV-ID | Invariant Statement | Scope | Falsification Test |
| INV-01 |                     |       |                    |
[3+ rows]

Numeric/temporal invariant gate:
  INV-ID meeting requirement: [ID]
  Exact threshold: [number + unit]
  Trace step where this threshold is most likely to be tested: [Step N — OP-ID]

SECTION 1: COMPLETE → SECTION 2: OPEN

---

SECTION 2 — HYPOTHESIS

This section directly determines your reconciliation calibration score.
Precision here = meaningful C/FP/FN classification in Section 5.
Vague predictions produce FP verdicts by design — they are unfalsifiable.

HYPOTHESIS TABLE
| H-ID | Anomaly Class | Specific Predicted Finding | Involved IDs (OP/S/INV) | Confidence (L/M/H) | What Evidence Would Confirm This |
| H-01 |               |                            |                         |                    |                                   |
| H-02 |               |                            |                         |                    |                                   |
| H-03 |               |                            |                         |                    |                                   |
[3+ rows; one per anomaly class; all ID columns must be populated]

"What Evidence Would Confirm This" column: name the specific trace step,
state transition, or invariant test that would confirm your prediction.
This becomes the acceptance criterion Role B uses in Section 3.

SECTION 2: COMPLETE → SECTION 3: OPEN

---

SECTION 3 — TRACE SEQUENCE

The evidence strength column is the feed for Section 5's calibration score.
Assign it at the moment of writing — point-of-discovery discipline.

SCORE-ALOUD BEHAVIORAL DISCIPLINE (required, named protocol):
Before writing each step's evidence strength, speak:
  "Step [N] evidence strength: [1/2/3] because [reason for this rating]."
Then write. If you assign strength silently, mark the step [SILENT — RESTATE]
and restate before continuing. This is not a reminder — it is a cognitive
commit protocol. Its purpose is to prevent score retroactive rationalization.
Label this discipline explicitly at the start of Section 3.

STEP TEMPLATE:
  STEP [N] — [OP-ID]: [Operation Name]
  Before state:    [S-ID] — [State Name]
  Preconditions:   [list — domain-specific, state-specific]
  Operation:       [description]
  Postconditions:  [list — guaranteed facts, not aspirations]
  After state:     [S-ID] — [State Name]
  Evidence strength: [1 / 2 / 3]
  Score-aloud record: "[verbatim spoken verdict]"

[5+ steps. Mark one NEGATIVE-PATH STEP and one CONCURRENT STEP clearly.]

NEGATIVE-PATH STEP:
  STEP [N] — [OP-ID]: REJECTED
  Attempted from: [S-ID]
  Which precondition failed: [name the specific precondition]
  Rejection state: [unchanged — S-ID]
  Evidence strength: [1/2/3]
  Score-aloud record: "..."

CONCURRENT STEP:
  STEP [N] — [OP-ID-A] || [OP-ID-B]: CONCURRENT
  Contested field: [name]
  Window of vulnerability: [T=1: ... T=2: ... T=3: ... T=4: ...]
  Failure mode: [what breaks]
  Resolution: [mechanism]
  Evidence strength: [1/2/3]
  Score-aloud record: "..."

SECTION 3: COMPLETE → SECTION 4: OPEN

---

SECTION 4 — ANOMALY SWEEP (4 phases, sequential)

Phase structure (identical for all four phases):
  Each phase = {Sweep Table} + {Findings List} + {Gap Record}
  This structural pair is not optional. It is the phase output contract.
  The Gap Record is the unlock signal. The exit gate opens when and only
  when the Gap Record is complete — not when the Findings List is written.

---

SECTION 4, PHASE A — INVALID STATE TRANSITIONS
STATUS: LOCKED until SECTION 3: COMPLETE

Detection:
  Pass 1 — Declaration-Only: Review each OP-ID's From States in the
  Operation Registry. Any From State where that operation should not
  legally execute is a candidate finding.
  Pass 2 — Trace-Diff: Compare each trace step's actual Before State
  against the declared From States for that OP-ID. Mismatch = finding.

SWEEP TABLE (Phase A):
| OP-ID | Declaration-Only Finding | Trace-Diff Finding | Evidence Strength |
| OP-01 |                          |                    |                   |
[one row per OP-ID]
Inline gap record format for any "None" cell:
  "None — [trace steps/declaration rows examined]; no finding because [specific reason]"

FINDINGS LIST (Phase A):
  1. [finding with OP-ID, states, evidence strength — or: None]

GAP RECORD (Phase A) — UNCONDITIONAL — THIS IS THE EXIT GATE UNLOCK:
  Evidence standard: [what would constitute a valid finding — copy from
    or derive from the H-ID whose class matches this phase]
  Searched: [list specific trace steps and declaration rows reviewed]
  Not found: [the specific transitions examined and ruled out]
  Phases with findings still produce this record: [document what your
    sweep could NOT detect, not just what it found]

SECTION 4, PHASE A: COMPLETE → PHASE B: OPEN

---

SECTION 4, PHASE B — MISSING PRECONDITION CHECKS
STATUS: LOCKED until PHASE A: COMPLETE

Detection:
  Pass 1 — Declaration-Only: For each OP-ID, examine the Preconditions
  column. Is each precondition specific enough to be checked? Vague or
  implicit preconditions with no enforcement mechanism are findings.
  Pass 2 — Trace-Diff: In each trace step, verify that preconditions are
  explicitly checked. Test: could the concurrent operation from Section 3
  bypass a precondition check between evaluation and execution?

SWEEP TABLE (Phase B):
| OP-ID | Declaration-Only Finding | Trace-Diff Finding | Evidence Strength |
[one row per OP-ID; inline gap records on any None cell]

FINDINGS LIST (Phase B):
  1. [or None]

GAP RECORD (Phase B) — UNCONDITIONAL — EXIT GATE UNLOCK:
  Evidence standard: [...]
  Searched: [...]
  Not found: [...]

SECTION 4, PHASE B: COMPLETE → PHASE C: OPEN

---

SECTION 4, PHASE C — INVARIANT VIOLATIONS
STATUS: LOCKED until PHASE B: COMPLETE

Detection:
  Pass 1 — Declaration-Only: For each INV-ID, identify which operations
  could produce after-states within the invariant's scope where the
  invariant is false.
  Pass 2 — Trace-Diff: Walk each trace step. Test every INV whose scope
  includes the after-state. Apply the numeric/temporal INV with actual
  values from the postconditions.

SWEEP TABLE (Phase C):
| INV-ID | Declaration-Only Finding | Trace-Diff Finding | Evidence Strength |
[one row per INV-ID; inline gap records on any None cell]

FINDINGS LIST (Phase C):
  1. [or None]

GAP RECORD (Phase C) — UNCONDITIONAL — EXIT GATE UNLOCK:
  Evidence standard: [...]
  Searched: [...]
  Not found: [...]

SECTION 4, PHASE C: COMPLETE → PHASE D: OPEN

---

SECTION 4, PHASE D — RACE CONDITIONS
STATUS: LOCKED until PHASE C: COMPLETE

Detection:
  Pass 1 — Declaration-Only: Identify OP-ID pairs that write the same
  state field. These are structural race candidates regardless of trace
  evidence.
  Pass 2 — Trace-Diff: Using the concurrent step from Section 3, produce
  an explicit interleaving timeline. Name: contested field, window start
  and end, failure mode, and whether the current design resolves or
  ignores the race.

SWEEP TABLE (Phase D):
| OP-ID Pair | Declaration-Only Finding | Trace-Diff Finding | Evidence Strength |
[one row per concurrent-capable pair; inline gap records on any None cell]

FINDINGS LIST (Phase D):
  1. [or None]

GAP RECORD (Phase D) — UNCONDITIONAL — EXIT GATE UNLOCK:
  Evidence standard: [...]
  Searched: [...]
  Not found: [...]

SECTION 4, PHASE D: COMPLETE → SECTION 5: OPEN

---

SECTION 5 — RECONCILIATION (C/FP/FN + CALIBRATION SCORE)

SCORE-ALOUD DISCIPLINE: active here as well.
For each reconciliation row, state the verdict before writing:
  "H-[ID]: I classify this as [C/FP/FN] because [reason]."
Write the spoken verdict into the Verdict Reason column verbatim.
Mark any silently-written row [SILENT — RESTATE] and restate it.

RECONCILIATION TABLE:
| H-ID | Predicted Finding | Actual Finding | Verdict (C/FP/FN) | Verdict Reason (spoken) |
[one row per H-ID from Section 2]
[additional FN rows for unplanned findings from Phases A–D]

Verdict classification:
  C (Correct): prediction confirmed by a Phase A–D finding
  FP (False Positive): prediction not confirmed in any phase
  FN (False Negative): phase finding not covered by any prediction

Calibration computation:
  C count: [N]
  FP count: [N]
  FN count: [N]
  Calibration Score = C / (C + FP + FN) = [score]

If score >= 0.5:
  Calibration note: [brief characterization of what the hypothesis got right]

If score < 0.5 (structural diagnosis required):
  Most mispredicted anomaly class: [class name]
  Diagnosis: [was the hypothesis declaration-biased? trace-biased?
    systematically over-predicting one class and under-predicting another?]
  Root cause: [what cognitive pattern produced the miscalibration]
  Better approach: [what a well-calibrated hypothesis for this domain
    and state machine structure would have looked like]

SECTION 5: COMPLETE

---

FINAL CERTIFICATION
[ ] Sections 1–5 all carry COMPLETE declarations
[ ] Phases A–D each have: {Sweep Table} + {Findings List} + {Gap Record}
[ ] Gap Record is present for phases with findings and phases without
[ ] No sweep cell contains bare "None" — all have inline gap records
[ ] Reconciliation table uses C/FP/FN for every row
[ ] FN rows added for unplanned findings
[ ] Calibration score computed
[ ] Structural diagnosis written if score < 0.5
[ ] SCORE-ALOUD DISCIPLINE applied and labeled in Sections 3 and 5
[ ] All IDs resolve to declared registry entries
```

---

## Variation Axis Summary

| Variation | Axis | Key Mechanism | Primary C-25 Approach | B-Fires |
|-----------|------|---------------|----------------------|---------|
| V-01 | Role sequence — B pre-detection | Role B commits acceptance criterion before Role A searches | Calibration score at close | Every phase |
| V-02 | Output format — rigid template | Named placeholder blocks for every structural component including Gap Record | Full C/FP/FN table + calibration in Block 7 | Every phase via GAP RECORD block |
| V-03 | Lifecycle emphasis — per-phase full instruction | Each phase written independently with its own detection instructions | C/FP/FN + spoken-first discipline in Part 5 | Every phase via Gap Record |
| V-04 | B-first + conversational register | "Decide what you're hunting for before you look" imperative | C/FP/FN + structural diagnosis in Step 5 | Every phase, framed as active choice |
| V-05 | Template + per-phase + C-25 as spine | Reconciliation accuracy as the design anchor propagated upstream | C/FP/FN + calibration + structural diagnosis as primary output | Every phase via EXIT GATE UNLOCK |

**Discriminating tests** the rubric will surface:
- **C-23** (score-aloud as named discipline): V-01 is weakest — it names the protocol but least prominently; V-02/V-03/V-04/V-05 all label it explicitly
- **C-25** (C/FP/FN + calibration threshold + structural diagnosis): all five variations include it; V-05 is deepest with the upstream propagation framing
- **C-33** (symmetric phase output contract): V-02 is strongest — the GAP RECORD block is visible in the template whether or not findings exist; V-01 is weakest — the protocol section must be followed but the template doesn't enforce absence detection visually
