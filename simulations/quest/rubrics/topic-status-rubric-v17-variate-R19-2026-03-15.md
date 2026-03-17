# Variations: `topic:status` -- Round 19
**Rubric:** v17 (max 300) | **Date:** 2026-03-15

---

## Design Context

R18 differentiating evidence (projected under v17): V-01 → 300; V-02 → 295
(C-47 FAIL); V-03 → 295 (C-48 FAIL, C-49 vacuous PASS); V-04 → 295 (C-49
FAIL); V-05 → 290 (C-47+C-48 FAIL, C-49 vacuous PASS). Three variants tied
at 295, each isolating a different criterion from a different ablation axis.

**R18 gap:** No R18 variant fails all three of C-47, C-48, C-49 simultaneously.
The structural constraint explains why: when C-48 fails (no PHASE 1 adversary
body), C-49 is vacuously satisfied -- no PHASE 1 adversary is declared, so the
STOP CONDITION's compliance at the PHASE 1 predicate position is not in
question. True simultaneous failure of all three requires C-48 to be PASS
(so C-49 can be non-vacuously evaluated) while C-47 is also FAIL -- the
configuration C-47 FAIL + C-48 PASS + C-49 FAIL. That configuration was
not represented in R18. It is the gap that defines Round 19.

**R19 primary purpose:** Generate the cross-axis combination V-05 = C-47 FAIL
+ C-49 FAIL (C-48 PASS). This is the nearest achievable configuration to
"all three simultaneously" given the vacuous-PASS constraint. V-01 through
V-04 reconfirm the three single-criterion ablations and the full baseline;
V-05 closes the cross-axis gap.

**Ablation matrix for R19:**

| Variant | C-47 | C-48 | C-49 | Predicted |
|---------|------|------|------|-----------|
| V-01 | PASS | PASS | PASS | 300 |
| V-02 | FAIL | PASS | PASS | 295 |
| V-03 | PASS | FAIL | PASS* | 295 |
| V-04 | PASS | PASS | FAIL | 295 |
| V-05 | FAIL | PASS | FAIL | 290 |

*C-49 vacuous PASS: 4th STOP predicate present but references no declared
PHASE 1 adversary; criterion satisfied because predicate count does not
fall below adversary chain length -- the violation in V-04 is the inverse
(predicate absent while adversary declared).

**Variation axes:**
- V-02: Inertia framing -- adversaries named in prose without per-phase labels
- V-03: Lifecycle emphasis -- PHASE 1 body compressed; adversary framing omitted
- V-04: Role sequence -- DISPLAY GATE STOP CONDITION sequence truncated at P3
- V-05: Combination -- inertia framing (C-47 FAIL) + role sequence (C-49 FAIL)

**Orthogonality confirmed by V-05:** V-02 vs V-05 delta = 5 pts (C-49 absent
in V-05, present in V-02 -- isolates C-49 contribution within a C-47-failing
variant). V-04 vs V-05 delta = 5 pts (C-47 absent in V-05, present in V-04 --
isolates C-47 contribution within a C-49-failing variant). The symmetric
5-point deltas confirm C-47 and C-49 contribute independently whether or not
the other is present -- neither implies the other in either direction.

**C-49 structural recap:** The DISPLAY GATE (PHASE 4) STOP CONDITION carries
predicates gating on each declared adversary's defeat condition before output
is rendered. With the full three-phase adversary chain (C-48 PASS), the STOP
CONDITION requires four predicates: (1) COMMIT RISK REGISTER row-count guard,
(2) PHASE 2 adversary defeat gate, (3) PHASE 3 adversary defeat gate, (4)
PHASE 1 adversary defeat gate. C-49 requires predicate (4). V-04 retains
predicates (1)-(3) but omits (4). V-03 carries all four predicates but
predicate (4) is vacuous (no PHASE 1 adversary was declared to operationalize).

---

## V-01: Minimum delta -- full-stack baseline, execution-prose form

**Axis:** Minimum structural delta from R18 V-01 (identical body). Full-stack
baseline: preamble ADVERSARY CHAIN block carries labeled P1-ADVERSARY:,
P2-ADVERSARY:, P3-ADVERSARY: sub-entries (C-47 PASS); PHASE 1 execution body
opens with ADVERSARY: / DEFEAT CONDITION: three-part block (C-48 PASS); PHASE 4
DISPLAY GATE STOP CONDITION carries all four predicates including the PHASE 1
adversary defeat gate (C-49 PASS). All 49 criteria satisfied.

**Hypothesis:** V-01 is the R19 full-stack baseline. All three tier-16 criteria
satisfied. Expected: 300/300.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Preamble: structural invariants declared before execution ------------------
All execution phase names use consequence vocabulary (C-21).
All [LAYER N] enforcement labels use the vocabulary of the phase they govern (C-24).
[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form -- not only the
stake noun phrase -- because PER-SIGNAL is the scope quantifier at left-edge
position in the phase name (C-26, C-27).
PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct
stop conditions with distinct messages. File-absent trigger: strategy.md not
present on disk -- output unquantifiable-exposure message and stop immediately.
Topic-absent trigger: strategy.md present but {topic} has no registered planned
signals -- output topic-specific stop message before PHASE 3 (EXPOSURE COMPUTATION).
OUTPUT DECLARATION CHAIN: PHASE 2 declares its own output structure (PHASE 2
OUTPUT DECLARATION with INVARIANT: and OUTPUT FORM: labeled sub-components and
per-axis Trigger: sentences within INVARIANT); PHASE 3 declares its own output
structure independently (PHASE 3 OUTPUT DECLARATION with INVARIANT: and OUTPUT
FORM: labeled sub-components and a Trigger: sentence within INVARIANT). Neither
phase's output declaration implies the other; each execution phase owns its
independently declared output structure.
ADVERSARY CHAIN:
  P1-ADVERSARY: inertia toward empty-glob assumption (default when PHASE 1 is
    skipped: coverage computed from zero disk signals without verification);
  P2-ADVERSARY: inertia toward evidence-blind commits (default when PHASE 2 is
    skipped: unverified signals ship without explicit assertion);
  P3-ADVERSARY: inertia toward coverage-blind verdicts (default when PHASE 3 is
    skipped: percent emitted without consistency guard verification).
  Each adversary is independently declared at its phase entry; no phase's
  adversary declaration implies any other's.
------------------------------------------------------------------------------

== OUTPUT TEMPLATE ==============================================================

[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]
COMMIT RISK REGISTER -- {topic}

  strategy.md: [FOUND | NOT FOUND -- if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute]

  | # | Namespace | Signal   | Status                                                              | Date   |
  |---|-----------|----------|---------------------------------------------------------------------|--------|
  | 1 | {ns}      | {signal} | VERIFIED | UNVERIFIED -- if absent: ships without this signal on commit | {date} |

[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]
COMMIT RISK BY NAMESPACE

  | Namespace | Planned | Found | Pct |
  |-----------|---------|-------|-----|
  | scout     | 0       | 0     | --  |
  | draft     | 0       | 0     | --  |
  | review    | 0       | 0     | --  |
  | flow      | 0       | 0     | --  |
  | trace     | 0       | 0     | --  |
  | prove     | 0       | 0     | --  |
  | listen    | 0       | 0     | --  |
  | program   | 0       | 0     | --  |
  | topic     | 0       | 0     | --  |

EXPOSURE SUMMARY
  Coverage: {found}/{planned} ({pct}%)

COMMIT DECISION
  PRIMARY ADVERSARY: commit without evidence -- inertia toward shipping on
  incomplete signals is the default outcome when status is not checked
  Readiness: READY | PARTIAL | NOT READY
  Committing now means shipping without: {list of UNVERIFIED signals}
  Committing now defeats: {N} signals not yet in evidence

STALE EVIDENCE
  {signal}: {date} ({N} days old -- if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence)
  None if all current.

HIGHEST PRIORITY RISK
  /{namespace}:{signal} {topic}

[LAYER 3 -- EXECUTION: DISPLAY GATE render order:
  COMMIT RISK REGISTER -> COMMIT RISK BY NAMESPACE -> EXPOSURE SUMMARY
  -> COMMIT DECISION -> STALE EVIDENCE -> HIGHEST PRIORITY RISK]

== EXECUTION PHASES =============================================================

PHASE 1 -- SIGNAL ACQUISITION
  ADVERSARY: inertia toward empty-glob assumption -- default when this phase
  is skipped: coverage is computed from zero disk signals without any disk
  verification step.
  DEFEAT CONDITION: DISK_SIGNALS populated from live glob result; if glob
  returns empty, execution stops immediately with an explicit "No signals found"
  message before any commitment assertion or coverage computation runs.
  Glob: simulations/**/{topic}-*
  Assign to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  Record per match: path, namespace, signal name, date.

PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION
  ADVERSARY: inertia toward evidence-blind commits -- default when this phase
  is skipped: each unverified signal ships without explicit assertion.
  DEFEAT CONDITION: all planned signals individually asserted (each receives
  VERIFIED or UNVERIFIED); no signal exits PHASE 2 without an explicit
  assertion state on the record.
  Read simulations/strategy.md.
  Exit A -- file absent: fires when strategy.md does not exist on disk
    Output: "No planned baseline -- commit exposure is unquantifiable."
    Stop.
  Exit B -- topic not registered: fires when strategy.md present but {topic} has no registered planned signals
    Output: "topic not registered: no planned signals for {topic}"
    Stop before PHASE 3.
  Extract planned signals for {topic}.
  For each planned signal P:
    If P matches a file in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Assert each signal individually. No batch evaluation.
  PHASE 2 OUTPUT DECLARATION:
    INVARIANT: Dual-axis gate -- file-absent and topic-absent exits are
      structurally distinct stop conditions with distinct messages.
      Trigger: file-absent fires when strategy.md does not exist on disk;
      topic-absent fires when strategy.md present but {topic} has no registered
      planned signals.
    OUTPUT FORM: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.

PHASE 3 -- EXPOSURE COMPUTATION
  ADVERSARY: inertia toward coverage-blind verdicts -- default when this phase
  is skipped: percent is emitted as computed without consistency guard verification.
  DEFEAT CONDITION: percent computed with consistency guard applied; any
  UNVERIFIED-non-empty and percent-100% contradiction detected and halted
  before readiness verdict is issued.
  percent = VERIFIED count / PLANNED count * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY
  PHASE 3 OUTPUT DECLARATION:
    INVARIANT: Consistency guard -- UNVERIFIED-non-empty and percent-100%
      contradiction halts computation before readiness verdict is issued.
      Trigger: guard fires when UNVERIFIED count > 0 and computed percent = 100%.
    OUTPUT FORM: percent (integer 0-100); readiness verdict
      (READY | PARTIAL | NOT READY).

PHASE 4 -- DISPLAY GATE
  STOP CONDITION:
    (1) COMMIT RISK REGISTER has one row per planned signal
    (2) PHASE 2 adversary defeated: all planned signals individually asserted;
        each carries an explicit VERIFIED or UNVERIFIED state on the record
    (3) PHASE 3 adversary defeated: percent computed with consistency guard
        applied; UNVERIFIED-non-empty and percent-100% contradiction detected
        and halted before readiness verdict issued
    (4) PHASE 1 adversary defeated: DISK_SIGNALS populated from live glob
        result -- not from memory or prior-round assumption; zero-result case
        handled explicitly before PHASE 2 commitment assertion executed
  Render in template section order.
  Write no files.
```

---

## V-02: Single axis -- inertia framing (prose ADVERSARY CHAIN; C-47 withheld)

**Axis:** Inertia framing -- the ADVERSARY CHAIN preamble block is
de-structured into extended prose, naming all three adversaries in sequence
without per-phase labeled sub-entries. The running-prose form names the
P1, P2, and P3 adversaries (C-45 PASS: block exists, names all three) but
omits the `P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:` labeled sub-entry
form (C-47 FAIL: phase-label-addressable independent entries absent). All
three execution phases retain their full three-part ADVERSARY:/DEFEAT CONDITION:
blocks. PHASE 4 DISPLAY GATE retains all four STOP CONDITION predicates
including the PHASE 1 defeat gate (C-49 PASS). All structure identical to V-01
except the preamble ADVERSARY CHAIN block form.

**Hypothesis:** C-47 requires labeled PN-ADVERSARY: sub-component entries
within the preamble ADVERSARY CHAIN block. Running prose that names all three
adversaries satisfies C-45 but fails C-47. C-48 PASS (execution-body PHASE 1
adversary block intact). C-49 PASS (4th STOP predicate intact). Observable
structural gap: V-01 preamble has `P1-ADVERSARY:`, `P2-ADVERSARY:`,
`P3-ADVERSARY:` labeled lines; V-02 preamble has a single prose paragraph
covering the same content without per-adversary labels. Expected: 295/300.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Preamble: structural invariants declared before execution ------------------
All execution phase names use consequence vocabulary (C-21).
All [LAYER N] enforcement labels use the vocabulary of the phase they govern (C-24).
[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form -- not only the
stake noun phrase -- because PER-SIGNAL is the scope quantifier at left-edge
position in the phase name (C-26, C-27).
PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct
stop conditions with distinct messages. File-absent trigger: strategy.md not
present on disk -- output unquantifiable-exposure message and stop immediately.
Topic-absent trigger: strategy.md present but {topic} has no registered planned
signals -- output topic-specific stop message before PHASE 3 (EXPOSURE COMPUTATION).
OUTPUT DECLARATION CHAIN: PHASE 2 declares its own output structure (PHASE 2
OUTPUT DECLARATION with INVARIANT: and OUTPUT FORM: labeled sub-components and
per-axis Trigger: sentences within INVARIANT); PHASE 3 declares its own output
structure independently (PHASE 3 OUTPUT DECLARATION with INVARIANT: and OUTPUT
FORM: labeled sub-components and a Trigger: sentence within INVARIANT). Neither
phase's output declaration implies the other; each execution phase owns its
independently declared output structure.
ADVERSARY CHAIN: PHASE 1 adversary -- inertia toward empty-glob assumption
(default when PHASE 1 is skipped: coverage computed from zero disk signals
without verification); PHASE 2 adversary -- inertia toward evidence-blind
commits (default when PHASE 2 is skipped: unverified signals ship without
explicit assertion); PHASE 3 adversary -- inertia toward coverage-blind
verdicts (default when PHASE 3 is skipped: percent emitted without consistency
guard verification). Each adversary is independently declared at its phase
entry; no phase's adversary declaration implies any other's.
------------------------------------------------------------------------------

== OUTPUT TEMPLATE ==============================================================

[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]
COMMIT RISK REGISTER -- {topic}

  strategy.md: [FOUND | NOT FOUND -- if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute]

  | # | Namespace | Signal   | Status                                                              | Date   |
  |---|-----------|----------|---------------------------------------------------------------------|--------|
  | 1 | {ns}      | {signal} | VERIFIED | UNVERIFIED -- if absent: ships without this signal on commit | {date} |

[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]
COMMIT RISK BY NAMESPACE

  | Namespace | Planned | Found | Pct |
  |-----------|---------|-------|-----|
  | scout     | 0       | 0     | --  |
  | draft     | 0       | 0     | --  |
  | review    | 0       | 0     | --  |
  | flow      | 0       | 0     | --  |
  | trace     | 0       | 0     | --  |
  | prove     | 0       | 0     | --  |
  | listen    | 0       | 0     | --  |
  | program   | 0       | 0     | --  |
  | topic     | 0       | 0     | --  |

EXPOSURE SUMMARY
  Coverage: {found}/{planned} ({pct}%)

COMMIT DECISION
  PRIMARY ADVERSARY: commit without evidence -- inertia toward shipping on
  incomplete signals is the default outcome when status is not checked
  Readiness: READY | PARTIAL | NOT READY
  Committing now means shipping without: {list of UNVERIFIED signals}
  Committing now defeats: {N} signals not yet in evidence

STALE EVIDENCE
  {signal}: {date} ({N} days old -- if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence)
  None if all current.

HIGHEST PRIORITY RISK
  /{namespace}:{signal} {topic}

[LAYER 3 -- EXECUTION: DISPLAY GATE render order:
  COMMIT RISK REGISTER -> COMMIT RISK BY NAMESPACE -> EXPOSURE SUMMARY
  -> COMMIT DECISION -> STALE EVIDENCE -> HIGHEST PRIORITY RISK]

== EXECUTION PHASES =============================================================

PHASE 1 -- SIGNAL ACQUISITION
  ADVERSARY: inertia toward empty-glob assumption -- default when this phase
  is skipped: coverage is computed from zero disk signals without any disk
  verification step.
  DEFEAT CONDITION: DISK_SIGNALS populated from live glob result; if glob
  returns empty, execution stops immediately with an explicit "No signals found"
  message before any commitment assertion or coverage computation runs.
  Glob: simulations/**/{topic}-*
  Assign to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  Record per match: path, namespace, signal name, date.

PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION
  ADVERSARY: inertia toward evidence-blind commits -- default when this phase
  is skipped: each unverified signal ships without explicit assertion.
  DEFEAT CONDITION: all planned signals individually asserted (each receives
  VERIFIED or UNVERIFIED); no signal exits PHASE 2 without an explicit
  assertion state on the record.
  Read simulations/strategy.md.
  Exit A -- file absent: fires when strategy.md does not exist on disk
    Output: "No planned baseline -- commit exposure is unquantifiable."
    Stop.
  Exit B -- topic not registered: fires when strategy.md present but {topic} has no registered planned signals
    Output: "topic not registered: no planned signals for {topic}"
    Stop before PHASE 3.
  Extract planned signals for {topic}.
  For each planned signal P:
    If P matches a file in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Assert each signal individually. No batch evaluation.
  PHASE 2 OUTPUT DECLARATION:
    INVARIANT: Dual-axis gate -- file-absent and topic-absent exits are
      structurally distinct stop conditions with distinct messages.
      Trigger: file-absent fires when strategy.md does not exist on disk;
      topic-absent fires when strategy.md present but {topic} has no registered
      planned signals.
    OUTPUT FORM: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.

PHASE 3 -- EXPOSURE COMPUTATION
  ADVERSARY: inertia toward coverage-blind verdicts -- default when this phase
  is skipped: percent is emitted as computed without consistency guard verification.
  DEFEAT CONDITION: percent computed with consistency guard applied; any
  UNVERIFIED-non-empty and percent-100% contradiction detected and halted
  before readiness verdict is issued.
  percent = VERIFIED count / PLANNED count * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY
  PHASE 3 OUTPUT DECLARATION:
    INVARIANT: Consistency guard -- UNVERIFIED-non-empty and percent-100%
      contradiction halts computation before readiness verdict is issued.
      Trigger: guard fires when UNVERIFIED count > 0 and computed percent = 100%.
    OUTPUT FORM: percent (integer 0-100); readiness verdict
      (READY | PARTIAL | NOT READY).

PHASE 4 -- DISPLAY GATE
  STOP CONDITION:
    (1) COMMIT RISK REGISTER has one row per planned signal
    (2) PHASE 2 adversary defeated: all planned signals individually asserted;
        each carries an explicit VERIFIED or UNVERIFIED state on the record
    (3) PHASE 3 adversary defeated: percent computed with consistency guard
        applied; UNVERIFIED-non-empty and percent-100% contradiction detected
        and halted before readiness verdict issued
    (4) PHASE 1 adversary defeated: DISK_SIGNALS populated from live glob
        result -- not from memory or prior-round assumption; zero-result case
        handled explicitly before PHASE 2 commitment assertion executed
  Render in template section order.
  Write no files.
```

---

## V-03: Single axis -- lifecycle emphasis (compressed PHASE 1; C-48 withheld)

**Axis:** Lifecycle emphasis -- PHASE 1 body is compressed to its minimal
executable form: glob instruction, DISK_SIGNALS assignment, empty-result halt,
and record step. No ADVERSARY: clause and no DEFEAT CONDITION: sub-component
at PHASE 1 entry (C-48 FAIL). The adversary chain remains a two-phase execution
chain (PHASE 2 + PHASE 3). Preamble ADVERSARY CHAIN block carries
`P2-ADVERSARY:` and `P3-ADVERSARY:` labeled sub-entries only (C-47 PASS at
two-label count -- label count tracks chain length; the absence of P1-ADVERSARY:
is not a C-47 violation when no PHASE 1 adversary body is declared).
PHASE 4 DISPLAY GATE STOP CONDITION carries all four predicates including the
PHASE 1 defeat gate, but predicate (4) is vacuously satisfied: it references a
PHASE 1 defeat condition for which no PHASE 1 adversary was declared (C-49
vacuous PASS). No template reordering; all LAYER labels and consequence
vocabulary preserved. All other structure identical to V-01.

**Hypothesis:** C-48 requires an explicit ADVERSARY: / DEFEAT CONDITION: block
in the PHASE 1 execution body. Absence of the PHASE 1 adversary block costs
5 points (C-48 FAIL). C-47 PASS (two-label preamble chain compliant with
chain-length rule). C-49 vacuous PASS (4th predicate present; no PHASE 1
adversary declared to operationalize it -- not a C-49 violation). Observable
structural gap: V-01 PHASE 1 opens with ADVERSARY: + DEFEAT CONDITION: before
the Glob instruction; V-03 PHASE 1 opens directly with Glob: with no adversary
framing. Observable preamble gap: V-01 ADVERSARY CHAIN has three labeled
entries (P1, P2, P3); V-03 ADVERSARY CHAIN has two labeled entries (P2, P3).
Expected: 295/300.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Preamble: structural invariants declared before execution ------------------
All execution phase names use consequence vocabulary (C-21).
All [LAYER N] enforcement labels use the vocabulary of the phase they govern (C-24).
[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form -- not only the
stake noun phrase -- because PER-SIGNAL is the scope quantifier at left-edge
position in the phase name (C-26, C-27).
PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct
stop conditions with distinct messages. File-absent trigger: strategy.md not
present on disk -- output unquantifiable-exposure message and stop immediately.
Topic-absent trigger: strategy.md present but {topic} has no registered planned
signals -- output topic-specific stop message before PHASE 3 (EXPOSURE COMPUTATION).
OUTPUT DECLARATION CHAIN: PHASE 2 declares its own output structure (PHASE 2
OUTPUT DECLARATION with INVARIANT: and OUTPUT FORM: labeled sub-components and
per-axis Trigger: sentences within INVARIANT); PHASE 3 declares its own output
structure independently (PHASE 3 OUTPUT DECLARATION with INVARIANT: and OUTPUT
FORM: labeled sub-components and a Trigger: sentence within INVARIANT). Neither
phase's output declaration implies the other; each execution phase owns its
independently declared output structure.
ADVERSARY CHAIN:
  P2-ADVERSARY: inertia toward evidence-blind commits (default when PHASE 2 is
    skipped: unverified signals ship without explicit assertion);
  P3-ADVERSARY: inertia toward coverage-blind verdicts (default when PHASE 3 is
    skipped: percent emitted without consistency guard verification).
  Each adversary is independently declared at its phase entry; PHASE 2's
  adversary declaration does not imply PHASE 3's.
------------------------------------------------------------------------------

== OUTPUT TEMPLATE ==============================================================

[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]
COMMIT RISK REGISTER -- {topic}

  strategy.md: [FOUND | NOT FOUND -- if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute]

  | # | Namespace | Signal   | Status                                                              | Date   |
  |---|-----------|----------|---------------------------------------------------------------------|--------|
  | 1 | {ns}      | {signal} | VERIFIED | UNVERIFIED -- if absent: ships without this signal on commit | {date} |

[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]
COMMIT RISK BY NAMESPACE

  | Namespace | Planned | Found | Pct |
  |-----------|---------|-------|-----|
  | scout     | 0       | 0     | --  |
  | draft     | 0       | 0     | --  |
  | review    | 0       | 0     | --  |
  | flow      | 0       | 0     | --  |
  | trace     | 0       | 0     | --  |
  | prove     | 0       | 0     | --  |
  | listen    | 0       | 0     | --  |
  | program   | 0       | 0     | --  |
  | topic     | 0       | 0     | --  |

EXPOSURE SUMMARY
  Coverage: {found}/{planned} ({pct}%)

COMMIT DECISION
  PRIMARY ADVERSARY: commit without evidence -- inertia toward shipping on
  incomplete signals is the default outcome when status is not checked
  Readiness: READY | PARTIAL | NOT READY
  Committing now means shipping without: {list of UNVERIFIED signals}
  Committing now defeats: {N} signals not yet in evidence

STALE EVIDENCE
  {signal}: {date} ({N} days old -- if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence)
  None if all current.

HIGHEST PRIORITY RISK
  /{namespace}:{signal} {topic}

[LAYER 3 -- EXECUTION: DISPLAY GATE render order:
  COMMIT RISK REGISTER -> COMMIT RISK BY NAMESPACE -> EXPOSURE SUMMARY
  -> COMMIT DECISION -> STALE EVIDENCE -> HIGHEST PRIORITY RISK]

== EXECUTION PHASES =============================================================

PHASE 1 -- SIGNAL ACQUISITION
  Glob: simulations/**/{topic}-*
  Assign to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  Record per match: path, namespace, signal name, date.

PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION
  ADVERSARY: inertia toward evidence-blind commits -- default when this phase
  is skipped: each unverified signal ships without explicit assertion.
  DEFEAT CONDITION: all planned signals individually asserted (each receives
  VERIFIED or UNVERIFIED); no signal exits PHASE 2 without an explicit
  assertion state on the record.
  Read simulations/strategy.md.
  Exit A -- file absent: fires when strategy.md does not exist on disk
    Output: "No planned baseline -- commit exposure is unquantifiable."
    Stop.
  Exit B -- topic not registered: fires when strategy.md present but {topic} has no registered planned signals
    Output: "topic not registered: no planned signals for {topic}"
    Stop before PHASE 3.
  Extract planned signals for {topic}.
  For each planned signal P:
    If P matches a file in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Assert each signal individually. No batch evaluation.
  PHASE 2 OUTPUT DECLARATION:
    INVARIANT: Dual-axis gate -- file-absent and topic-absent exits are
      structurally distinct stop conditions with distinct messages.
      Trigger: file-absent fires when strategy.md does not exist on disk;
      topic-absent fires when strategy.md present but {topic} has no registered
      planned signals.
    OUTPUT FORM: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.

PHASE 3 -- EXPOSURE COMPUTATION
  ADVERSARY: inertia toward coverage-blind verdicts -- default when this phase
  is skipped: percent is emitted as computed without consistency guard verification.
  DEFEAT CONDITION: percent computed with consistency guard applied; any
  UNVERIFIED-non-empty and percent-100% contradiction detected and halted
  before readiness verdict is issued.
  percent = VERIFIED count / PLANNED count * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY
  PHASE 3 OUTPUT DECLARATION:
    INVARIANT: Consistency guard -- UNVERIFIED-non-empty and percent-100%
      contradiction halts computation before readiness verdict is issued.
      Trigger: guard fires when UNVERIFIED count > 0 and computed percent = 100%.
    OUTPUT FORM: percent (integer 0-100); readiness verdict
      (READY | PARTIAL | NOT READY).

PHASE 4 -- DISPLAY GATE
  STOP CONDITION:
    (1) COMMIT RISK REGISTER has one row per planned signal
    (2) PHASE 2 adversary defeated: all planned signals individually asserted;
        each carries an explicit VERIFIED or UNVERIFIED state on the record
    (3) PHASE 3 adversary defeated: percent computed with consistency guard
        applied; UNVERIFIED-non-empty and percent-100% contradiction detected
        and halted before readiness verdict issued
    (4) PHASE 1 adversary defeated: DISK_SIGNALS populated from live glob
        result; zero-result case handled before commitment assertion executed
  Render in template section order.
  Write no files.
```

---

## V-04: Single axis -- role sequence (DISPLAY GATE STOP CONDITION truncated; C-49 withheld)

**Axis:** Role sequence -- the DISPLAY GATE STOP CONDITION sequence is
truncated at predicate (3). The PHASE 1 adversary defeat predicate (4) is
absent from the STOP CONDITION, leaving it with three predicates: the row-count
guard and the PHASE 2 and PHASE 3 adversary defeat gates. PHASE 1 execution
body retains the full three-part ADVERSARY: / DEFEAT CONDITION: block (C-48
PASS). Preamble ADVERSARY CHAIN retains labeled P1-ADVERSARY:, P2-ADVERSARY:,
P3-ADVERSARY: sub-entries (C-47 PASS). The adversary chain and the STOP
CONDITION are out of sync: three adversaries declared (three-phase chain,
C-48 present) but only two adversary defeat predicates in the gate (PHASE 2
and PHASE 3 only). C-49 FAIL: PHASE 1 adversary defeat predicate absent from
STOP CONDITION while PHASE 1 adversary is declared. All other structure
identical to V-01.

**Hypothesis:** C-49 requires the STOP CONDITION to carry a predicate for
the PHASE 1 adversary defeat condition when C-48 is present. Omitting
predicate (4) while retaining the three-phase adversary chain (C-47 PASS,
C-48 PASS) leaves the adversary chain and the gate out of sync -- the PHASE 1
adversary is declared and commits a DEFEAT CONDITION, but no gate check
verifies that defeat before output renders. Expected: 295/300. Observable
structural gap: V-01 PHASE 4 has four predicates; V-04 PHASE 4 has three.
V-04 vs V-01 delta cleanly isolates C-49.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Preamble: structural invariants declared before execution ------------------
All execution phase names use consequence vocabulary (C-21).
All [LAYER N] enforcement labels use the vocabulary of the phase they govern (C-24).
[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form -- not only the
stake noun phrase -- because PER-SIGNAL is the scope quantifier at left-edge
position in the phase name (C-26, C-27).
PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct
stop conditions with distinct messages. File-absent trigger: strategy.md not
present on disk -- output unquantifiable-exposure message and stop immediately.
Topic-absent trigger: strategy.md present but {topic} has no registered planned
signals -- output topic-specific stop message before PHASE 3 (EXPOSURE COMPUTATION).
OUTPUT DECLARATION CHAIN: PHASE 2 declares its own output structure (PHASE 2
OUTPUT DECLARATION with INVARIANT: and OUTPUT FORM: labeled sub-components and
per-axis Trigger: sentences within INVARIANT); PHASE 3 declares its own output
structure independently (PHASE 3 OUTPUT DECLARATION with INVARIANT: and OUTPUT
FORM: labeled sub-components and a Trigger: sentence within INVARIANT). Neither
phase's output declaration implies the other; each execution phase owns its
independently declared output structure.
ADVERSARY CHAIN:
  P1-ADVERSARY: inertia toward empty-glob assumption (default when PHASE 1 is
    skipped: coverage computed from zero disk signals without verification);
  P2-ADVERSARY: inertia toward evidence-blind commits (default when PHASE 2 is
    skipped: unverified signals ship without explicit assertion);
  P3-ADVERSARY: inertia toward coverage-blind verdicts (default when PHASE 3 is
    skipped: percent emitted without consistency guard verification).
  Each adversary is independently declared at its phase entry; no phase's
  adversary declaration implies any other's.
------------------------------------------------------------------------------

== OUTPUT TEMPLATE ==============================================================

[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]
COMMIT RISK REGISTER -- {topic}

  strategy.md: [FOUND | NOT FOUND -- if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute]

  | # | Namespace | Signal   | Status                                                              | Date   |
  |---|-----------|----------|---------------------------------------------------------------------|--------|
  | 1 | {ns}      | {signal} | VERIFIED | UNVERIFIED -- if absent: ships without this signal on commit | {date} |

[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]
COMMIT RISK BY NAMESPACE

  | Namespace | Planned | Found | Pct |
  |-----------|---------|-------|-----|
  | scout     | 0       | 0     | --  |
  | draft     | 0       | 0     | --  |
  | review    | 0       | 0     | --  |
  | flow      | 0       | 0     | --  |
  | trace     | 0       | 0     | --  |
  | prove     | 0       | 0     | --  |
  | listen    | 0       | 0     | --  |
  | program   | 0       | 0     | --  |
  | topic     | 0       | 0     | --  |

EXPOSURE SUMMARY
  Coverage: {found}/{planned} ({pct}%)

COMMIT DECISION
  PRIMARY ADVERSARY: commit without evidence -- inertia toward shipping on
  incomplete signals is the default outcome when status is not checked
  Readiness: READY | PARTIAL | NOT READY
  Committing now means shipping without: {list of UNVERIFIED signals}
  Committing now defeats: {N} signals not yet in evidence

STALE EVIDENCE
  {signal}: {date} ({N} days old -- if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence)
  None if all current.

HIGHEST PRIORITY RISK
  /{namespace}:{signal} {topic}

[LAYER 3 -- EXECUTION: DISPLAY GATE render order:
  COMMIT RISK REGISTER -> COMMIT RISK BY NAMESPACE -> EXPOSURE SUMMARY
  -> COMMIT DECISION -> STALE EVIDENCE -> HIGHEST PRIORITY RISK]

== EXECUTION PHASES =============================================================

PHASE 1 -- SIGNAL ACQUISITION
  ADVERSARY: inertia toward empty-glob assumption -- default when this phase
  is skipped: coverage is computed from zero disk signals without any disk
  verification step.
  DEFEAT CONDITION: DISK_SIGNALS populated from live glob result; if glob
  returns empty, execution stops immediately with an explicit "No signals found"
  message before any commitment assertion or coverage computation runs.
  Glob: simulations/**/{topic}-*
  Assign to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  Record per match: path, namespace, signal name, date.

PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION
  ADVERSARY: inertia toward evidence-blind commits -- default when this phase
  is skipped: each unverified signal ships without explicit assertion.
  DEFEAT CONDITION: all planned signals individually asserted (each receives
  VERIFIED or UNVERIFIED); no signal exits PHASE 2 without an explicit
  assertion state on the record.
  Read simulations/strategy.md.
  Exit A -- file absent: fires when strategy.md does not exist on disk
    Output: "No planned baseline -- commit exposure is unquantifiable."
    Stop.
  Exit B -- topic not registered: fires when strategy.md present but {topic} has no registered planned signals
    Output: "topic not registered: no planned signals for {topic}"
    Stop before PHASE 3.
  Extract planned signals for {topic}.
  For each planned signal P:
    If P matches a file in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Assert each signal individually. No batch evaluation.
  PHASE 2 OUTPUT DECLARATION:
    INVARIANT: Dual-axis gate -- file-absent and topic-absent exits are
      structurally distinct stop conditions with distinct messages.
      Trigger: file-absent fires when strategy.md does not exist on disk;
      topic-absent fires when strategy.md present but {topic} has no registered
      planned signals.
    OUTPUT FORM: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.

PHASE 3 -- EXPOSURE COMPUTATION
  ADVERSARY: inertia toward coverage-blind verdicts -- default when this phase
  is skipped: percent is emitted as computed without consistency guard verification.
  DEFEAT CONDITION: percent computed with consistency guard applied; any
  UNVERIFIED-non-empty and percent-100% contradiction detected and halted
  before readiness verdict is issued.
  percent = VERIFIED count / PLANNED count * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY
  PHASE 3 OUTPUT DECLARATION:
    INVARIANT: Consistency guard -- UNVERIFIED-non-empty and percent-100%
      contradiction halts computation before readiness verdict is issued.
      Trigger: guard fires when UNVERIFIED count > 0 and computed percent = 100%.
    OUTPUT FORM: percent (integer 0-100); readiness verdict
      (READY | PARTIAL | NOT READY).

PHASE 4 -- DISPLAY GATE
  STOP CONDITION:
    (1) COMMIT RISK REGISTER has one row per planned signal
    (2) PHASE 2 adversary defeated: all planned signals individually asserted;
        each carries an explicit VERIFIED or UNVERIFIED state on the record
    (3) PHASE 3 adversary defeated: percent computed with consistency guard
        applied; UNVERIFIED-non-empty and percent-100% contradiction detected
        and halted before readiness verdict issued
  Render in template section order.
  Write no files.
```

---

## V-05: Combination -- inertia framing + role sequence (C-47 FAIL + C-49 FAIL; C-48 PASS)

**Axes:** Inertia framing (C-47 withheld: preamble ADVERSARY CHAIN in
running-prose form, no labeled sub-entries) + role sequence (C-49 withheld:
DISPLAY GATE STOP CONDITION truncated to three predicates, no PHASE 1 defeat
gate). PHASE 1 execution body retains the full three-part ADVERSARY:/DEFEAT
CONDITION: block (C-48 PASS): the adversary is declared and its defeat condition
committed in the execution body. The out-of-sync gap is doubled: preamble
adversary chain names all three adversaries but without phase-label-addressable
entries (C-47 FAIL), AND the STOP CONDITION carries only two adversary defeat
predicates (P2 and P3) while the execution body declares three adversaries
including the PHASE 1 block (C-49 FAIL). Neither C-47 failure implies C-49
failure; neither C-49 failure implies C-47 failure.

**Hypothesis:** V-05 closes the R18 cross-axis gap. C-47 and C-49 are
simultaneously and independently failed while C-48 is retained. Expected:
290/300 (10-point delta from V-01 = 5 pts C-47 + 5 pts C-49).

Observable deltas: V-05 vs V-02 delta = 5 pts (C-49 absent in V-05,
present in V-02 -- C-47-failing variants, C-49 contribution isolated).
V-05 vs V-04 delta = 5 pts (C-47 absent in V-05, present in V-04 -- C-49-
failing variants, C-47 contribution isolated). Both symmetric 5-pt deltas
confirm C-47 and C-49 are independently observable and independently
necessary regardless of whether the other is present.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Preamble: structural invariants declared before execution ------------------
All execution phase names use consequence vocabulary (C-21).
All [LAYER N] enforcement labels use the vocabulary of the phase they govern (C-24).
[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form -- not only the
stake noun phrase -- because PER-SIGNAL is the scope quantifier at left-edge
position in the phase name (C-26, C-27).
PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct
stop conditions with distinct messages. File-absent trigger: strategy.md not
present on disk -- output unquantifiable-exposure message and stop immediately.
Topic-absent trigger: strategy.md present but {topic} has no registered planned
signals -- output topic-specific stop message before PHASE 3 (EXPOSURE COMPUTATION).
OUTPUT DECLARATION CHAIN: PHASE 2 declares its own output structure (PHASE 2
OUTPUT DECLARATION with INVARIANT: and OUTPUT FORM: labeled sub-components and
per-axis Trigger: sentences within INVARIANT); PHASE 3 declares its own output
structure independently (PHASE 3 OUTPUT DECLARATION with INVARIANT: and OUTPUT
FORM: labeled sub-components and a Trigger: sentence within INVARIANT). Neither
phase's output declaration implies the other; each execution phase owns its
independently declared output structure.
ADVERSARY CHAIN: PHASE 1 adversary -- inertia toward empty-glob assumption
(default when PHASE 1 is skipped: coverage computed from zero disk signals
without verification); PHASE 2 adversary -- inertia toward evidence-blind
commits (default when PHASE 2 is skipped: unverified signals ship without
explicit assertion); PHASE 3 adversary -- inertia toward coverage-blind
verdicts (default when PHASE 3 is skipped: percent emitted without consistency
guard verification). Each adversary is independently declared at its phase
entry; no phase's adversary declaration implies any other's.
------------------------------------------------------------------------------

== OUTPUT TEMPLATE ==============================================================

[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]
COMMIT RISK REGISTER -- {topic}

  strategy.md: [FOUND | NOT FOUND -- if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute]

  | # | Namespace | Signal   | Status                                                              | Date   |
  |---|-----------|----------|---------------------------------------------------------------------|--------|
  | 1 | {ns}      | {signal} | VERIFIED | UNVERIFIED -- if absent: ships without this signal on commit | {date} |

[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]
COMMIT RISK BY NAMESPACE

  | Namespace | Planned | Found | Pct |
  |-----------|---------|-------|-----|
  | scout     | 0       | 0     | --  |
  | draft     | 0       | 0     | --  |
  | review    | 0       | 0     | --  |
  | flow      | 0       | 0     | --  |
  | trace     | 0       | 0     | --  |
  | prove     | 0       | 0     | --  |
  | listen    | 0       | 0     | --  |
  | program   | 0       | 0     | --  |
  | topic     | 0       | 0     | --  |

EXPOSURE SUMMARY
  Coverage: {found}/{planned} ({pct}%)

COMMIT DECISION
  PRIMARY ADVERSARY: commit without evidence -- inertia toward shipping on
  incomplete signals is the default outcome when status is not checked
  Readiness: READY | PARTIAL | NOT READY
  Committing now means shipping without: {list of UNVERIFIED signals}
  Committing now defeats: {N} signals not yet in evidence

STALE EVIDENCE
  {signal}: {date} ({N} days old -- if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence)
  None if all current.

HIGHEST PRIORITY RISK
  /{namespace}:{signal} {topic}

[LAYER 3 -- EXECUTION: DISPLAY GATE render order:
  COMMIT RISK REGISTER -> COMMIT RISK BY NAMESPACE -> EXPOSURE SUMMARY
  -> COMMIT DECISION -> STALE EVIDENCE -> HIGHEST PRIORITY RISK]

== EXECUTION PHASES =============================================================

PHASE 1 -- SIGNAL ACQUISITION
  ADVERSARY: inertia toward empty-glob assumption -- default when this phase
  is skipped: coverage is computed from zero disk signals without any disk
  verification step.
  DEFEAT CONDITION: DISK_SIGNALS populated from live glob result; if glob
  returns empty, execution stops immediately with an explicit "No signals found"
  message before any commitment assertion or coverage computation runs.
  Glob: simulations/**/{topic}-*
  Assign to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  Record per match: path, namespace, signal name, date.

PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION
  ADVERSARY: inertia toward evidence-blind commits -- default when this phase
  is skipped: each unverified signal ships without explicit assertion.
  DEFEAT CONDITION: all planned signals individually asserted (each receives
  VERIFIED or UNVERIFIED); no signal exits PHASE 2 without an explicit
  assertion state on the record.
  Read simulations/strategy.md.
  Exit A -- file absent: fires when strategy.md does not exist on disk
    Output: "No planned baseline -- commit exposure is unquantifiable."
    Stop.
  Exit B -- topic not registered: fires when strategy.md present but {topic} has no registered planned signals
    Output: "topic not registered: no planned signals for {topic}"
    Stop before PHASE 3.
  Extract planned signals for {topic}.
  For each planned signal P:
    If P matches a file in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Assert each signal individually. No batch evaluation.
  PHASE 2 OUTPUT DECLARATION:
    INVARIANT: Dual-axis gate -- file-absent and topic-absent exits are
      structurally distinct stop conditions with distinct messages.
      Trigger: file-absent fires when strategy.md does not exist on disk;
      topic-absent fires when strategy.md present but {topic} has no registered
      planned signals.
    OUTPUT FORM: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.

PHASE 3 -- EXPOSURE COMPUTATION
  ADVERSARY: inertia toward coverage-blind verdicts -- default when this phase
  is skipped: percent is emitted as computed without consistency guard verification.
  DEFEAT CONDITION: percent computed with consistency guard applied; any
  UNVERIFIED-non-empty and percent-100% contradiction detected and halted
  before readiness verdict is issued.
  percent = VERIFIED count / PLANNED count * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY
  PHASE 3 OUTPUT DECLARATION:
    INVARIANT: Consistency guard -- UNVERIFIED-non-empty and percent-100%
      contradiction halts computation before readiness verdict is issued.
      Trigger: guard fires when UNVERIFIED count > 0 and computed percent = 100%.
    OUTPUT FORM: percent (integer 0-100); readiness verdict
      (READY | PARTIAL | NOT READY).

PHASE 4 -- DISPLAY GATE
  STOP CONDITION:
    (1) COMMIT RISK REGISTER has one row per planned signal
    (2) PHASE 2 adversary defeated: all planned signals individually asserted;
        each carries an explicit VERIFIED or UNVERIFIED state on the record
    (3) PHASE 3 adversary defeated: percent computed with consistency guard
        applied; UNVERIFIED-non-empty and percent-100% contradiction detected
        and halted before readiness verdict issued
  Render in template section order.
  Write no files.
```

---

## Score prediction summary

| Variant | Axis | C-47 | C-48 | C-49 | Predicted (v17) |
|---------|------|------|------|------|-----------------|
| V-01 | Min delta, full-stack baseline | PASS | PASS | PASS | 300/300 |
| V-02 | Inertia framing -- prose ADVERSARY CHAIN | FAIL | PASS | PASS | 295/300 |
| V-03 | Lifecycle emphasis -- PHASE 1 compressed | PASS | FAIL | PASS* | 295/300 |
| V-04 | Role sequence -- DISPLAY GATE STOP truncated | PASS | PASS | FAIL | 295/300 |
| V-05 | Combination -- prose chain + truncated gate | FAIL | PASS | FAIL | 290/300 |

*Vacuous PASS: 4th predicate structurally present; no PHASE 1 adversary
declared to operationalize it -- C-49 compliant because predicate count
does not fall below adversary chain length.

**Three-way 295 tie:** V-02, V-03, V-04 all predicted at 295 -- each
isolating exactly one of the three tier-16 criteria. The symmetric three-way
tie confirms C-47, C-48, and C-49 are pairwise orthogonal: withholding any
one independently produces a 5-point penalty; the other two criteria are
unaffected.

**V-05 cross-axis confirmation:** V-05 is predicted at 290. The V-05 vs
V-02 delta = 5 pts confirms C-49 contributes 5 pts independently within a
C-47-failing variant. The V-05 vs V-04 delta = 5 pts confirms C-47
contributes 5 pts independently within a C-49-failing variant. Neither
criterion provides a shield for the other.

**Structural constraint restatement:** Simultaneously failing all three
of C-47, C-48, C-49 is structurally impossible: C-48 FAIL causes C-49
vacuous PASS. The V-05 configuration (C-47 FAIL + C-48 PASS + C-49 FAIL,
score 290) is the maximum-failure configuration achievable without triggering
the vacuous-PASS constraint. Round 19 closes this gap: no further
cross-axis combination between C-47, C-48, and C-49 remains untested.

**R20 gap forecast:** If R19 scores match predictions (300, 295, 295, 295,
290), the tier-16 criteria are fully characterized. A new criterion C-50
can only be extracted if a structural property is observable in R19 V-01
that is absent in all prior single-criterion ablations and that neither
V-02 nor V-03 nor V-04 nor V-05 independently captures. Candidates for
C-50 exploration: ADVERSARY CHAIN preamble block independence assertion
(the line "Each adversary is independently declared at its phase entry; no
phase's adversary declaration implies any other's") as a separately
assessable structural property from the labeled-sub-entry form (C-47).
No C-50 candidate is confirmed; R19 scoring evidence required.
