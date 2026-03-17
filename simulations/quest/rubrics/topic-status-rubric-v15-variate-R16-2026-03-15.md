
# Variations: `topic:status` -- Round 16
**Rubric:** v15 (max 285) | **Date:** 2026-03-15

---

## Design Context

R15 differentiating evidence: V-01, V-03, V-04, V-05 each scored 285/285 under
v15; V-02 scored 280/285. The R15 scorecard confirms two new Tier 14 criteria:

- **C-45**: Preamble adversary chain declaration. The preamble carries an
  `ADVERSARY CHAIN:` block naming both the PHASE 2 and PHASE 3 adversaries as a
  two-element structural chain with independence assertion. Parallel to C-44's
  `OUTPUT DECLARATION CHAIN:` but applied to adversary declarations.

- **C-46**: Adversary defeat condition sub-component. Each adversary declaration
  at PHASE 2 and PHASE 3 entry carries an explicitly labeled `DEFEAT CONDITION:`
  sub-component. Extends the adversary block from two-part (adversary + trigger)
  to three-part form (adversary + trigger + defeat condition). Parallel to C-40's
  labeled sub-components in OUTPUT DECLARATION.

**R15 gap:** No R15 variant jointly fails C-45 and C-46 -- those are confirmed
criteria. R16 probes genuinely new structural territory.

R16 introduces two new structural properties:

- **C-47 candidate**: Labeled sub-components within the `ADVERSARY CHAIN:`
  preamble block. Instead of running prose, the block carries explicitly labeled
  entries: `P2-ADVERSARY:` and `P3-ADVERSARY:` (and `P1-ADVERSARY:` when C-48 is
  also present). This extends the preamble adversary chain from prose-form to
  labeled-form -- parallel to how C-40 extended OUTPUT DECLARATION from
  undifferentiated prose to labeled `INVARIANT:` and `OUTPUT FORM:` sub-components.
  Prerequisite: C-45 (the preamble ADVERSARY CHAIN block must exist before its
  sub-components can be labeled and independently addressable).

- **C-48 candidate**: PHASE 1 execution-body adversary declaration. PHASE 1
  (SIGNAL ACQUISITION) gains an `ADVERSARY:` clause with `DEFEAT CONDITION:`
  sub-component, extending the execution-body adversary chain from two-phase
  (P2+P3) to three-phase (P1+P2+P3). PHASE 1 adversary: inertia toward
  empty-glob assumption (default when PHASE 1 is skipped: coverage computed from
  zero disk signals without verification). DEFEAT CONDITION: DISK_SIGNALS
  populated from live glob result; if empty, execution stops with explicit message
  before commitment assertion or coverage computation runs. Prerequisite: C-46
  (the three-part adversary form must be established before it can be applied to
  PHASE 1).

**Orthogonality**: C-47 concerns preamble architecture (how the adversary chain
is declared before execution). C-48 concerns execution-body structure (which
phases carry adversaries). A variant can carry labeled preamble sub-components
without PHASE 1 adversary (C-47 PASS, C-48 FAIL -- V-03). A variant can carry
PHASE 1 adversary without labeled preamble sub-components (C-47 FAIL, C-48
PASS -- V-02).

**Asymmetric prerequisites** (returns to the normal pattern, unlike R15 where
both new criteria shared C-43): C-47 requires C-45; C-48 requires C-46. These
are different prerequisite criteria on different structural dimensions.

**Predicted score map under v15:**

| Variant | C-45 | C-46 | C-47 | C-48 | Predicted |
|---------|------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | PASS | 285/285   |
| V-02    | PASS | PASS | FAIL | PASS | 285/285   |
| V-03    | PASS | PASS | PASS | FAIL | 285/285   |
| V-04    | PASS | PASS | PASS | PASS | 285/285   |
| V-05    | PASS | PASS | PASS | PASS | 285/285   |

All five variants score 285 under v15 -- C-47 and C-48 are not yet criteria.

Axes: minimum delta adding C-47+C-48 in execution-prose form (V-01);
inertia framing axis -- C-47 withheld, C-48 present, 3-element prose ADVERSARY
CHAIN (V-02); output format axis -- C-48 withheld, C-47 present, readiness-first
template (V-03); lifecycle GUARD contract form with C-47+C-48 (V-04); elevated
titled adversary-declaration blocks with C-47+C-48 including PHASE 1 (V-05).

---

## V-01: Minimum delta -- C-47 + C-48 in execution-prose form

**Axis:** Minimum structural delta from R15 V-01. Two targeted additions:
(1) The preamble `ADVERSARY CHAIN:` block receives labeled `P1-ADVERSARY:`,
`P2-ADVERSARY:`, `P3-ADVERSARY:` sub-components, naming all three phase
adversaries as a three-element structural chain (C-47 candidate -- extends the
prose-form two-element ADVERSARY CHAIN block to labeled-form; each adversary
entry is independently addressable by label; the preamble now carries three
architectural invariant blocks, each with labeled sub-components: dual-axis exit
chain C-34, output declaration chain C-44, and now labeled adversary chain C-47;
prerequisite: C-45 must be present for labeled sub-components to be extractable).
(2) PHASE 1 execution body gains an `ADVERSARY:` clause with `DEFEAT CONDITION:`
sub-component (C-48 candidate -- extends the execution-body adversary chain from
two-phase P2+P3 to three-phase P1+P2+P3; PHASE 1 adversary is inertia toward
empty-glob assumption; three-part form mirrors C-46's three-part form at P2 and
P3 entry sites; prerequisite: C-46 must be established before the three-part form
can be applied at PHASE 1). All other structure identical to R15 V-01.

**Hypothesis:** C-47 adds labeled sub-components to the preamble ADVERSARY CHAIN
block, making each adversary entry independently addressable by its phase label
(P1-ADVERSARY:, P2-ADVERSARY:, P3-ADVERSARY:) -- parallel to how OUTPUT
DECLARATION CHAIN could carry labeled P2-OUTPUT: and P3-OUTPUT: entries. C-48
adds a three-part ADVERSARY block at PHASE 1, completing the adversary chain at
all three active execution phases. The V-01 vs V-02 delta isolates C-47 (V-02
withholds the labeled preamble sub-components while preserving the extended prose
chain and C-48). The V-01 vs V-03 delta isolates C-48 (V-03 withholds the PHASE
1 adversary while preserving the labeled preamble sub-components). The delta
between V-02 and V-03 should be 0 under v15 (both 285) -- confirming C-47 and
C-48 are independently observable and not implied by each other.

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
  Pre-display invariant: COMMIT RISK REGISTER has one row per planned signal.
  Render in template section order.
  Write no files.
```

---

## V-02: Single axis -- C-47 withheld (isolation test)

**Axis:** C-47 deliberately withheld. PHASE 1 gains a full `ADVERSARY:` /
`DEFEAT CONDITION:` block (C-48 PASS), so the ADVERSARY CHAIN block in the
preamble now names three adversaries -- but it does so in running prose form
rather than labeled sub-components. The preamble carries `ADVERSARY CHAIN:`
followed by an extended prose sentence covering P1, P2, and P3 adversaries, with
the three-element independence assertion. The structural property absent: no
`P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:` labeled entries within the
ADVERSARY CHAIN block. Execution bodies retain full three-part adversary blocks
(adversary + trigger + defeat condition) at all three phases. All other structure
identical to V-01. Inertia framing axis applied: adversary framing is made
maximally explicit and prominent throughout output section headers, but this
prominence is present in running prose rather than labeled sub-component form.

**Hypothesis:** If C-47 requires labeled `PN-ADVERSARY:` sub-components within
the preamble ADVERSARY CHAIN block -- making each adversary entry independently
addressable by phase label without prose scanning -- then extending the block to
three adversaries in running prose while withholding the labeled format should
fail C-47 while leaving C-48 intact. Under v15, both V-01 and V-02 score 285
(C-47 is not yet a criterion). Observable structural gap: V-01's ADVERSARY CHAIN
block uses `P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:` labeled lines;
V-02's ADVERSARY CHAIN block uses a single prose paragraph naming all three
adversaries without per-adversary labeling. If a v16 rubric extracts C-47, V-02
scores 5 points below V-01.

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
without verification); PHASE 2 adversary -- inertia toward evidence-blind commits
(default when PHASE 2 is skipped: unverified signals ship without explicit
assertion); PHASE 3 adversary -- inertia toward coverage-blind verdicts (default
when PHASE 3 is skipped: percent emitted without consistency guard verification).
Each adversary is independently declared at its phase entry; no phase's adversary
declaration implies any other's.
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
  Pre-display invariant: COMMIT RISK REGISTER has one row per planned signal.
  Render in template section order.
  Write no files.
```

---

## V-03: Single axis -- C-48 withheld (isolation test)

**Axis:** C-48 deliberately withheld. The preamble ADVERSARY CHAIN block carries
labeled `P2-ADVERSARY:` and `P3-ADVERSARY:` sub-components (C-47 PASS -- two-
element labeled chain), but PHASE 1 execution body has no `ADVERSARY:` clause and
no `DEFEAT CONDITION:` sub-component. The adversary chain remains a two-phase
chain (P2+P3) with labeled preamble sub-components but no P1-ADVERSARY: entry and
no P1 execution-body adversary block. All PHASE 2 and PHASE 3 adversary blocks
retain their full three-part structure (adversary + trigger + defeat condition).
Output format axis applied: the template is reordered so that the readiness
verdict and exposure summary appear FIRST (before the full COMMIT RISK REGISTER),
surfacing the headline conclusion before the row-level detail.

**Hypothesis:** If C-48 requires a PHASE 1 execution-body `ADVERSARY:` /
`DEFEAT CONDITION:` block -- extending the adversary chain to include signal
acquisition -- then withholding PHASE 1 adversary while adding labeled preamble
sub-components should fail C-48 while leaving C-47 intact. Under v15, both V-01
and V-03 score 285 (C-48 is not yet a criterion). Observable structural gap:
V-01's PHASE 1 body opens with `ADVERSARY: inertia toward empty-glob assumption`
followed by `DEFEAT CONDITION:` before the Glob instruction; V-03's PHASE 1 body
opens directly with `Glob:` with no adversary framing. If a v16 rubric extracts
C-48, V-03 scores 5 points below V-01. The delta between V-02 (C-47 withheld,
C-48 present) and V-03 (C-47 present, C-48 withheld) should be 0 under v15,
confirming orthogonality.

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

[LAYER 1 -- SEMANTIC: readiness verdict first; headline before row-level detail]
READINESS VERDICT -- {topic}

  Coverage: {found}/{planned} ({pct}%)
  Readiness: READY | PARTIAL | NOT READY
  Committing now defeats: {N} signals not yet in evidence

[LAYER 2 -- STRUCTURAL: primary gap artifact; follows verdict]
COMMIT RISK REGISTER -- {topic}

  strategy.md: [FOUND | NOT FOUND -- if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute]

  | # | Namespace | Signal   | Status                                                              | Date   |
  |---|-----------|----------|---------------------------------------------------------------------|--------|
  | 1 | {ns}      | {signal} | VERIFIED | UNVERIFIED -- if absent: ships without this signal on commit | {date} |

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

COMMIT DECISION
  PRIMARY ADVERSARY: commit without evidence -- inertia toward shipping on
  incomplete signals is the default outcome when status is not checked
  Committing now means shipping without: {list of UNVERIFIED signals}

STALE EVIDENCE
  {signal}: {date} ({N} days old -- if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence)
  None if all current.

HIGHEST PRIORITY RISK
  /{namespace}:{signal} {topic}

[LAYER 3 -- EXECUTION: DISPLAY GATE render order:
  READINESS VERDICT -> COMMIT RISK REGISTER -> COMMIT RISK BY NAMESPACE
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
  Pre-display invariant: COMMIT RISK REGISTER has one row per planned signal.
  Render in template section order: READINESS VERDICT first, then COMMIT RISK
  REGISTER, then remaining sections.
  Write no files.
```

---

## V-04: Combination -- Lifecycle GUARD contract form with C-47+C-48

**Axes:** Lifecycle emphasis (phase contract blocks with INPUT / GUARD / OUTPUT
fields) + C-47 via labeled `P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:`
sub-components in the preamble ADVERSARY CHAIN block (identical in content to
V-01) + C-48 via a three-part `ADVERSARY:` / `DEFEAT CONDITION:` block in PHASE
1 execution prose appended below the PHASE 1 contract box. The adversary
declarations appear in the execution prose section below each phase box -- PHASE
1, PHASE 2, and PHASE 3 each have their adversary block and defeat condition in
the prose section beneath their contract box, not inside the box header fields.
Tests whether C-47 and C-48 are form-agnostic across execution-prose (V-01) and
lifecycle-contract (V-04) execution formats.

**Hypothesis:** C-45 and C-46 were confirmed form-agnostic in R15 (lifecycle-
contract-appended adversary lines satisfy alongside plain execution-prose form).
By the same logic, C-47 and C-48 should be form-agnostic: the labeled preamble
ADVERSARY CHAIN block satisfies C-47 regardless of whether execution phases use
prose or lifecycle-contract format. The PHASE 1 adversary block in prose below
the PHASE 1 contract box satisfies C-48 whether the surrounding phase structure
uses prose (V-01) or lifecycle contracts (V-04). If V-04 and V-01 both reach the
same score under v16, C-47 and C-48 form-agnosticism is confirmed consistent with
R11-R15 form-agnosticism patterns.

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

+-- PHASE 1 -- SIGNAL ACQUISITION ------------------------------------------+
| INPUT:  topic argument                                                      |
| OUTPUT: DISK_SIGNALS (path, namespace, signal name, date) | empty set       |
+---------------------------------------------------------------------------+
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

+-- PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION ------------------------------+
| INPUT:  DISK_SIGNALS; simulations/strategy.md                               |
| GUARD:  Exit A -- file absent: fires when strategy.md does not exist        |
|             on disk ->                                                      |
|             output "No planned baseline -- commit exposure is               |
|             unquantifiable." and stop                                       |
|         Exit B -- topic not registered: fires when strategy.md present      |
|             but {topic} has no registered planned signals ->                |
|             output "topic not registered: no planned signals for {topic}"   |
|             and stop before PHASE 3 (EXPOSURE COMPUTATION)                 |
| OUTPUT: VERIFIED | UNVERIFIED per planned signal; no batch evaluation       |
+---------------------------------------------------------------------------+
  ADVERSARY: inertia toward evidence-blind commits -- default when this phase
  is skipped: each unverified signal ships without explicit assertion.
  DEFEAT CONDITION: all planned signals individually asserted (each receives
  VERIFIED or UNVERIFIED); no signal exits PHASE 2 without an explicit
  assertion state on the record.
  Read simulations/strategy.md. Apply GUARD exits in order.
  Extract planned signals for {topic}.
  For each planned signal P:
    If P matches a file in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Assert each signal individually.
  PHASE 2 OUTPUT DECLARATION:
    INVARIANT: Dual-axis gate -- file-absent and topic-absent exits are
      structurally distinct stop conditions with distinct messages.
      Trigger: file-absent fires when strategy.md does not exist on disk;
      topic-absent fires when strategy.md present but {topic} has no registered
      planned signals.
    OUTPUT FORM: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.

+-- PHASE 3 -- EXPOSURE COMPUTATION ----------------------------------------+
| INPUT:  VERIFIED/UNVERIFIED assertions from PHASE 2                         |
| OUTPUT: percent, readiness verdict                                          |
+---------------------------------------------------------------------------+
  ADVERSARY: inertia toward coverage-blind verdicts -- default when this phase
  is skipped: percent is emitted as computed without consistency guard verification.
  DEFEAT CONDITION: percent computed with consistency guard applied; any
  UNVERIFIED-non-empty and percent-100% contradiction detected and halted
  before readiness verdict is issued.
  percent = VERIFIED / PLANNED * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY
  PHASE 3 OUTPUT DECLARATION:
    INVARIANT: Consistency guard -- UNVERIFIED-non-empty and percent-100%
      contradiction halts computation before readiness verdict is issued.
      Trigger: guard fires when UNVERIFIED count > 0 and computed percent = 100%.
    OUTPUT FORM: percent (integer 0-100); readiness verdict
      (READY | PARTIAL | NOT READY).

+-- PHASE 4 -- DISPLAY GATE -------------------------------------------------+
| INPUT:  all phase outputs                                                   |
| GUARD:  COMMIT RISK REGISTER must have one row per planned signal           |
| OUTPUT: terminal display; no file written                                   |
+---------------------------------------------------------------------------+
  Pre-display invariant: row count = planned count.
  Render in template section order.
  Write no files.
```

---

## V-05: Combination -- Elevated titled adversary-declaration blocks with C-47+C-48

**Axes:** C-47 via labeled preamble sub-components (identical to V-01) + C-48
via a formally demarcated titled adversary-declaration block at PHASE 1 entry,
using the elevated titled-block pattern established in R14 V-05 and R15 V-05 for
PHASE 2 and PHASE 3 adversary declarations. All three active phases (PHASE 1,
PHASE 2, PHASE 3) receive a `+-- PHASE N ADVERSARY DECLARATION --+` titled box
at phase entry, containing labeled fields for `ADVERSARY:`, `TRIGGER:` (when the
adversary wins by default), and `DEFEAT CONDITION:` (how the adversary is
defeated). This extends the titled-block adversary pattern to PHASE 1,
completing a three-phase titled adversary chain. The preamble ADVERSARY CHAIN
block names all three adversaries with labeled P1-ADVERSARY:, P2-ADVERSARY:,
P3-ADVERSARY: sub-components. Tests whether C-47 and C-48 are form-agnostic
across execution-prose (V-01), lifecycle-contract (V-04), and elevated-titled-
block (V-05) presentation styles.

**Hypothesis:** C-46's titled-block form was confirmed in R15 (elevated titled
adversary blocks at PHASE 2 and PHASE 3 satisfy C-46 alongside plain execution-
prose form). By the same logic, C-48 should be form-agnostic: the
`+-- PHASE 1 ADVERSARY DECLARATION --+` titled box with `DEFEAT CONDITION:` field
satisfies C-48 in titled-block form. The labeled preamble ADVERSARY CHAIN block
satisfies C-47 regardless of whether execution phases use prose or titled-block
adversary declarations. If V-05 and V-01 score identically under v16, C-47 and
C-48 are confirmed form-agnostic across all three execution styles -- consistent
with R11-R15 form-agnosticism confirmations.

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

+-- PHASE 1 ADVERSARY DECLARATION -------------------------------------------+
| ADVERSARY:        inertia toward empty-glob assumption                      |
| TRIGGER:          PHASE 1 skipped -- coverage computed without disk         |
|                   verification; zero-signal coverage is the silent default  |
| DEFEAT CONDITION: DISK_SIGNALS populated from live glob result; empty glob  |
|                   stops execution with explicit message before commitment    |
|                   assertion or coverage computation runs                    |
+---------------------------------------------------------------------------+

PHASE 1 -- SIGNAL ACQUISITION
  Glob: simulations/**/{topic}-*
  Assign to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  Record per match: path, namespace, signal name, date.

+-- PHASE 2 ADVERSARY DECLARATION -------------------------------------------+
| ADVERSARY:        inertia toward evidence-blind commits                     |
| TRIGGER:          PHASE 2 skipped -- each unverified signal ships without   |
|                   explicit assertion; unverified is the silent default      |
| DEFEAT CONDITION: all planned signals individually asserted; each receives  |
|                   VERIFIED or UNVERIFIED; no signal exits without an        |
|                   explicit assertion state on the record                    |
+---------------------------------------------------------------------------+

PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION
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

+-- PHASE 3 ADVERSARY DECLARATION -------------------------------------------+
| ADVERSARY:        inertia toward coverage-blind verdicts                    |
| TRIGGER:          PHASE 3 skipped -- percent emitted as computed without    |
|                   consistency guard; unguarded percent is the silent default |
| DEFEAT CONDITION: percent computed with consistency guard applied; any      |
|                   UNVERIFIED-non-empty and percent-100% contradiction        |
|                   detected and halted before readiness verdict is issued    |
+---------------------------------------------------------------------------+

PHASE 3 -- EXPOSURE COMPUTATION
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
  Pre-display invariant: COMMIT RISK REGISTER has one row per planned signal.
  Render in template section order.
  Write no files.
```

---

## Score prediction summary

| Variant | Axis | C-45 | C-46 | C-47 | C-48 | Predicted (v15) |
|---------|------|------|------|------|------|-----------------|
| V-01 | Min delta, execution-prose | PASS | PASS | PASS | PASS | 285/285 |
| V-02 | Inertia framing, C-47 withheld | PASS | PASS | FAIL | PASS | 285/285 |
| V-03 | Output format, C-48 withheld | PASS | PASS | PASS | FAIL | 285/285 |
| V-04 | Lifecycle GUARD form | PASS | PASS | PASS | PASS | 285/285 |
| V-05 | Elevated titled adversary blocks | PASS | PASS | PASS | PASS | 285/285 |

All five variants score 285/285 under v15. C-47 and C-48 are not yet criteria.
V-01 vs V-02 isolates C-47. V-01 vs V-03 isolates C-48.
V-02 vs V-03 delta should be 0 under v15, confirming orthogonality.
