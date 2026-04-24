
# Variations: `topic:status` -- Round 15
**Rubric:** v14 (max 275) | **Date:** 2026-03-15

---

## Design Context

R14 differentiating evidence: V-01, V-04, V-05 each scored 275/275 under v14;
V-02 and V-03 scored 270/275. The R14 scorecard confirms two new Tier 13
criteria extracted from R13 excellence signals:

- **C-43**: PHASE 3 execution-body adversary declaration. An explicit
  `ADVERSARY:` clause at PHASE 3 execution body entry, completing a two-phase
  adversary chain (PHASE 2 entry established by C-42; PHASE 3 entry established
  by C-43). Each phase's adversary is independently required.

- **C-44**: Preamble output declaration chain declaration. The preamble carries
  an `OUTPUT DECLARATION CHAIN:` block naming both the PHASE 2 output
  declaration and the PHASE 3 output declaration as a two-element structural
  chain, asserting their independence -- parallel to C-34's dual-axis exit
  enumeration.

**R14 gap:** No R14 variant jointly fails C-43 and C-44 -- those are confirmed
criteria. R15 probes genuinely new structural territory.

R15 introduces two new structural properties:

- **C-45 candidate**: Preamble adversary chain declaration. The preamble
  carries an `ADVERSARY CHAIN:` block naming both the PHASE 2 and PHASE 3
  adversaries as a two-element structural chain, asserting their independence
  -- directly parallel to C-44 (preamble OUTPUT DECLARATION CHAIN) but applied
  to adversary declarations rather than output declarations. Just as C-44 asserts
  before execution phases that each phase owns its output structure, C-45 asserts
  before execution phases that each phase owns its adversary. Requires C-43
  (both adversaries must be independently declared in execution bodies before the
  preamble can enumerate them as a chain).

- **C-46 candidate**: Adversary defeat condition sub-component. Each adversary
  declaration (at PHASE 2 entry and PHASE 3 entry) carries an explicitly labeled
  `DEFEAT CONDITION:` sub-component stating the observable result that confirms
  the adversary has been defeated by execution of that phase. This extends the
  adversary block from two-part form (adversary named + trigger characterized)
  to three-part form (adversary named + trigger characterized + defeat condition
  labeled), parallel to how C-40 extended the OUTPUT DECLARATION from
  undifferentiated prose to labeled `INVARIANT:` and `OUTPUT FORM:`
  sub-components. Requires C-43 (both adversary declaration sites must exist
  before their sub-components can be labeled and independently addressable).

**Orthogonality**: C-45 concerns preamble architecture (declaring the two-phase
adversary chain before execution implements it). C-46 concerns execution-body
structure (adding a labeled sub-component to each adversary declaration). A
variant can carry preamble adversary chain without defeat conditions in adversary
blocks (C-45 PASS, C-46 FAIL -- V-03). A variant can carry defeat conditions in
adversary blocks without preamble adversary chain (C-45 FAIL, C-46 PASS -- V-02).

**Predicted score map under v14:**

| Variant | C-43 | C-44 | C-45 | C-46 | Predicted |
|---------|------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | PASS | 275/275   |
| V-02    | PASS | PASS | FAIL | PASS | 275/275   |
| V-03    | PASS | PASS | PASS | FAIL | 275/275   |
| V-04    | PASS | PASS | PASS | PASS | 275/275   |
| V-05    | PASS | PASS | PASS | PASS | 275/275   |

All five variants score 275 under v14 -- C-45 and C-46 are not yet criteria.

Axes: minimum delta combining C-45+C-46 in execution-prose form (V-01);
C-45 withheld isolation -- defeat conditions in adversary blocks, no preamble
adversary chain (V-02); C-46 withheld isolation -- preamble adversary chain,
no defeat conditions (V-03); lifecycle GUARD contract form with C-45+C-46
(V-04); elevated titled blocks for adversary declarations with C-45+C-46 (V-05).

---

## V-01: Minimum delta -- C-45+C-46 in execution-prose form

**Axis:** Minimum structural delta from R14 V-01. Two targeted additions:
(1) the preamble receives an `ADVERSARY CHAIN:` block naming both the PHASE 2
adversary and the PHASE 3 adversary as a two-element structural chain with
independence assertion (C-45 candidate -- parallel to C-44's OUTPUT DECLARATION
CHAIN, applied to adversary declarations; asserts before execution phases that
each phase owns its independently declared adversary); (2) each execution-phase
adversary declaration receives a `DEFEAT CONDITION:` labeled sub-component
stating the observable result that confirms the adversary was defeated (C-46
candidate -- extends adversary blocks from two-part to three-part structure,
parallel to C-40's labeled sub-components in OUTPUT DECLARATION). All other
structure identical to R14 V-01.

**Hypothesis:** C-45 adds a preamble `ADVERSARY CHAIN:` block that names both
execution-phase adversaries and asserts their structural independence before
the execution phases implement them -- the adversary-chain parallel of C-44.
C-46 adds a `DEFEAT CONDITION:` labeled sub-component to each adversary
declaration, making the victory condition independently addressable at the
adversary block site -- the adversary-block parallel of C-40's labeled
sub-components. Under v14, V-01 scores 275 (C-45 and C-46 are not yet
criteria). The V-01 vs V-02 delta isolates C-45; the V-01 vs V-03 delta
isolates C-46. The delta between V-02 and V-03 should be 0 under v14
(both 275) -- confirming C-45 and C-46 are independently observable and
not implied by each other.

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
ADVERSARY CHAIN: PHASE 2 adversary -- inertia toward evidence-blind commits
(default when PHASE 2 is skipped: unverified signals ship without explicit
assertion); PHASE 3 adversary -- inertia toward coverage-blind verdicts (default
when PHASE 3 is skipped: percent emitted without consistency guard verification).
Each adversary is independently declared at its phase entry; PHASE 2's adversary
declaration does not imply PHASE 3's.
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
  Pre-display invariant: COMMIT RISK REGISTER has one row per planned signal.
  Render in template section order.
  Write no files.
```

---

## V-02: Single-axis -- C-45 withheld (isolation test)

**Axis:** C-45 deliberately withheld. Both execution-phase adversary declarations
carry the `DEFEAT CONDITION:` labeled sub-component at PHASE 2 and PHASE 3 entry
(C-46 PASS), but the preamble has no `ADVERSARY CHAIN:` block. The preamble
retains `OUTPUT DECLARATION CHAIN:` (C-44 PASS) and the dual-axis exit
declaration (C-33/C-34 PASS), but no adversary chain declaration is made before
execution phases begin. The PHASE 2 and PHASE 3 `ADVERSARY:` lines with
`DEFEAT CONDITION:` sub-components are present in execution bodies; the structural
property missing is the preamble-level declaration that chains them. All other
structure identical to V-01.

**Hypothesis:** If C-45 requires a preamble `ADVERSARY CHAIN:` block declaring
both execution-phase adversaries as a named two-element chain with independence
assertion -- parallel to C-44's `OUTPUT DECLARATION CHAIN:` but for adversary
declarations -- then removing that preamble block while retaining defeat
conditions in execution bodies should fail C-45 while leaving C-46 intact. Under
v14, both V-01 and V-02 score 275 (C-45 is not yet a criterion). The observable
structural gap: V-01's preamble contains both an OUTPUT DECLARATION CHAIN block
and an ADVERSARY CHAIN block; V-02's preamble contains OUTPUT DECLARATION CHAIN
but no ADVERSARY CHAIN. If a v15 rubric extracts C-45, V-02 scores 5 points
below V-01. Confirms that the preamble output declaration chain (C-44) does not
imply a preamble adversary chain: C-45 is independently necessary.

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
  Pre-display invariant: COMMIT RISK REGISTER has one row per planned signal.
  Render in template section order.
  Write no files.
```

---

## V-03: Single-axis -- C-46 withheld (isolation test)

**Axis:** C-46 deliberately withheld. The preamble carries the full `ADVERSARY
CHAIN:` block naming both execution-phase adversaries as a two-element chain with
independence assertion (C-45 PASS), but the PHASE 2 and PHASE 3 adversary
declarations contain no `DEFEAT CONDITION:` labeled sub-component. Both phases
open with the `ADVERSARY:` clause (C-42 and C-43 PASS -- the adversary lines
themselves are present), but each adversary block is in two-part form only
(adversary named + trigger characterized) rather than the three-part form V-01
adds (adversary named + trigger characterized + defeat condition labeled). The
`DEFEAT CONDITION:` lines that V-01 inserts immediately after each `ADVERSARY:`
line are absent. All other structure identical to V-01.

**Hypothesis:** If C-46 requires a `DEFEAT CONDITION:` labeled sub-component
within each adversary declaration -- making the victory condition independently
addressable at the adversary block site -- then removing those sub-components
while retaining the preamble adversary chain should fail C-46 while leaving
C-45 intact. Under v14, both V-01 and V-03 score 275 (C-46 is not yet a
criterion). The observable structural gap: V-01's PHASE 2 execution body
contains `ADVERSARY: ... / DEFEAT CONDITION: ...`; V-03's PHASE 2 body
contains `ADVERSARY: ...` with no further sub-component labeling. The same
structural gap appears at PHASE 3. If a v15 rubric extracts C-46, V-03 scores
5 points below V-01. The delta between V-02 (C-45 withheld, C-46 present) and
V-03 (C-45 present, C-46 withheld) should be 0 under v14, confirming
orthogonality.

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
ADVERSARY CHAIN: PHASE 2 adversary -- inertia toward evidence-blind commits
(default when PHASE 2 is skipped: unverified signals ship without explicit
assertion); PHASE 3 adversary -- inertia toward coverage-blind verdicts (default
when PHASE 3 is skipped: percent emitted without consistency guard verification).
Each adversary is independently declared at its phase entry; PHASE 2's adversary
declaration does not imply PHASE 3's.
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

## V-04: Combination -- Lifecycle GUARD contract form with C-45+C-46

**Axes:** Lifecycle emphasis (phase contract blocks with INPUT / GUARD / OUTPUT
fields) + C-45 via a preamble `ADVERSARY CHAIN:` block identical in content to
V-01 + C-46 via `DEFEAT CONDITION:` clauses in execution prose below the PHASE 2
and PHASE 3 contract boxes. Tests whether C-45 and C-46 are form-agnostic across
execution-prose (V-01) and lifecycle-contract (V-04) execution formats. The
`ADVERSARY:` and `DEFEAT CONDITION:` clauses appear in the execution prose
section below each phase box (not inside the box header fields). The preamble
`ADVERSARY CHAIN:` block is identical to V-01, preceding the OUTPUT TEMPLATE.

**Hypothesis:** C-43 was confirmed form-agnostic in R14 (lifecycle-contract-
appended `ADVERSARY:` line satisfies alongside plain execution-prose form). By
the same logic, C-45 and C-46 should be form-agnostic: the preamble `ADVERSARY
CHAIN:` block satisfies C-45 regardless of whether execution phases use prose
or lifecycle-contract format. The `DEFEAT CONDITION:` line in execution prose
below the PHASE 2 box satisfies C-46 whether the surrounding phase structure
is execution-prose (V-01) or lifecycle contract (V-04). If V-04 and V-01 both
reach the same score under v15, C-45 and C-46 form-agnosticism is confirmed
consistent with R11-R14 patterns.

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
ADVERSARY CHAIN: PHASE 2 adversary -- inertia toward evidence-blind commits
(default when PHASE 2 is skipped: unverified signals ship without explicit
assertion); PHASE 3 adversary -- inertia toward coverage-blind verdicts (default
when PHASE 3 is skipped: percent emitted without consistency guard verification).
Each adversary is independently declared at its phase entry; PHASE 2's adversary
declaration does not imply PHASE 3's.
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

## V-05: Combination -- Lifecycle GUARD + elevated titled blocks for adversary declarations

**Axes:** Lifecycle emphasis + C-45 via preamble `ADVERSARY CHAIN:` block
(identical to V-01) + C-46 elevated to a formally demarcated titled block
within each execution phase. Both PHASE 2 and PHASE 3 receive a
`+-- PHASE N ADVERSARY DECLARATION --+` titled box at phase entry, containing
labeled fields for `ADVERSARY:`, `TRIGGER:` (when the adversary wins), and
`DEFEAT CONDITION:` (how the adversary is defeated). This extends the titled-
block pattern established for PHASE 2 OUTPUT DECLARATION in R12 V-05 and the
PHASE 3 OUTPUT DECLARATION in R13 V-05, applying it to adversary declarations
at both phase sites. A scorer reading either titled adversary block in isolation
can identify all three structural properties -- adversary named, trigger
characterized, defeat condition labeled -- without consulting any other section.

**Hypothesis:** C-43's titled-block form (R14 V-05) confirmed that adversary
framing at execution-phase sites is form-agnostic. V-05 extends this: the
`+-- PHASE 2 ADVERSARY DECLARATION --+` titled box with an explicit `DEFEAT
CONDITION:` field satisfies C-46 in titled-block form. The `+-- PHASE 3
ADVERSARY DECLARATION --+` titled box satisfies C-43 (PHASE 3 adversary present)
and C-46 (DEFEAT CONDITION field present). If V-05 and V-01 score identically
under v15, C-45 and C-46 are confirmed form-agnostic across execution-prose,
lifecycle-contract, and elevated-titled-block presentation styles -- consistent
with R11-R14 form-agnosticism confirmations.

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
ADVERSARY CHAIN: PHASE 2 adversary -- inertia toward evidence-blind commits
(default when PHASE 2 is skipped: unverified signals ship without explicit
assertion); PHASE 3 adversary -- inertia toward coverage-blind verdicts (default
when PHASE 3 is skipped: percent emitted without consistency guard verification).
Each adversary is independently declared at its phase entry; PHASE 2's adversary
declaration does not imply PHASE 3's.
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

  +-- PHASE 2 ADVERSARY DECLARATION -------------------------------------------+
  | ADVERSARY:        inertia toward evidence-blind commits                      |
  | TRIGGER:          fires as default when PER-SIGNAL COMMITMENT ASSERTION is   |
  |                   skipped; unverified signals proceed to shipment without    |
  |                   explicit assertion state                                   |
  | DEFEAT CONDITION: all planned signals individually asserted (VERIFIED or     |
  |                   UNVERIFIED); no signal exits PHASE 2 without explicit      |
  |                   assertion state on the record                              |
  +--------------------------------------------------------------------------+

  Read simulations/strategy.md. Apply GUARD exits in order.
  Extract planned signals for {topic}.
  For each planned signal P:
    If P matches a file in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Assert each signal individually.

  +-- PHASE 2 OUTPUT DECLARATION -- dual-axis gate invariant ----------------+
  | INVARIANT: file-absent and topic-absent exits are structurally distinct   |
  |   stop conditions with distinct messages.                                 |
  |   Trigger: file-absent fires when strategy.md does not exist on disk;    |
  |   topic-absent fires when strategy.md present but {topic} has no         |
  |   registered planned signals.                                             |
  | OUTPUT FORM: VERIFIED | UNVERIFIED per planned signal; no batch           |
  |   evaluation.                                                             |
  +--------------------------------------------------------------------------+

+-- PHASE 3 -- EXPOSURE COMPUTATION ----------------------------------------+
| INPUT:  VERIFIED/UNVERIFIED assertions from PHASE 2                         |
| OUTPUT: percent, readiness verdict                                          |
+---------------------------------------------------------------------------+

  +-- PHASE 3 ADVERSARY DECLARATION -------------------------------------------+
  | ADVERSARY:        inertia toward coverage-blind verdicts                     |
  | TRIGGER:          fires as default when EXPOSURE COMPUTATION is skipped;     |
  |                   percent is emitted as computed without consistency guard   |
  |                   verification; UNVERIFIED-non-empty contradiction undetected|
  | DEFEAT CONDITION: percent computed with consistency guard applied; any       |
  |                   UNVERIFIED-non-empty and percent-100% contradiction        |
  |                   detected and halted before readiness verdict is issued     |
  +--------------------------------------------------------------------------+

  percent = VERIFIED / PLANNED * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY

  +-- PHASE 3 OUTPUT DECLARATION -- consistency guard invariant -------------+
  | INVARIANT: UNVERIFIED-non-empty and percent-100% is a contradiction --    |
  |   guard halts before readiness verdict when this state is detected.       |
  |   Trigger: guard fires when UNVERIFIED count > 0 and percent = 100%.     |
  | OUTPUT FORM: percent (integer 0-100); readiness verdict                   |
  |   (READY | PARTIAL | NOT READY).                                          |
  +--------------------------------------------------------------------------+

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

## Predicted Score Summary

| ID | Axis | C-45 | C-46 | v14 Score |
|----|------|------|------|-----------|
| V-01 | Min delta: C-45+C-46 in execution-prose form | PASS | PASS | 275/275 |
| V-02 | C-45 withheld -- defeat conditions present, no preamble adversary chain | FAIL | PASS | 275/275 |
| V-03 | C-46 withheld -- preamble adversary chain present, no defeat conditions | PASS | FAIL | 275/275 |
| V-04 | Lifecycle GUARD contract form with C-45+C-46 in execution-body prose | PASS | PASS | 275/275 |
| V-05 | Lifecycle + elevated titled blocks for PHASE 2 and PHASE 3 adversary declarations | PASS | PASS | 275/275 |

All five variants score 275/275 under v14. C-45 and C-46 are not yet criteria --
they are observable patterns in R15's excellence signals.

**C-45 isolation test (V-01 vs V-02):** V-02 retains all C-43/C-44 structure
and adds DEFEAT CONDITION sub-components in both execution-phase adversary blocks
(C-46 PASS) but withholds the preamble ADVERSARY CHAIN block. The observable
gap: V-01's preamble contains both OUTPUT DECLARATION CHAIN and ADVERSARY CHAIN;
V-02's preamble contains OUTPUT DECLARATION CHAIN only. If a v15 rubric extracts
C-45, V-02 scores 5 points below V-01. Confirms that the preamble output
declaration chain (C-44) does not imply a preamble adversary chain: C-45 is
independently necessary as a second preamble invariant block.

**C-46 isolation test (V-01 vs V-03):** V-03 retains all C-43/C-44 structure
and adds the preamble ADVERSARY CHAIN (C-45 PASS) but withholds DEFEAT CONDITION
sub-components from both adversary declarations. The observable gap: V-01's
PHASE 2 adversary block reads `ADVERSARY: ... / DEFEAT CONDITION: ...`; V-03's
PHASE 2 adversary block reads `ADVERSARY: ...` with no further sub-component
labeling. The same structural gap appears at PHASE 3. If a v15 rubric extracts
C-46, V-03 scores 5 points below V-01. Confirms that adversary declarations in
execution bodies (C-42/C-43) do not imply labeled DEFEAT CONDITION sub-components:
C-46 is independently necessary as a sub-component labeling mechanism.

**Orthogonality test (V-02 vs V-03):** Both score 275/275 under v14. V-02 has
C-46 without C-45; V-03 has C-45 without C-46. Under v14 they are
indistinguishable. Under v15, if both C-45 and C-46 are extracted, V-02 and V-03
each trade: the criterion they satisfy offsets the one they withhold, producing
a symmetric 5-point delta that confirms the two criteria are orthogonal and
independently necessary.

**Form-agnosticism tests (V-01 vs V-04 vs V-05):** V-01 uses execution-prose for
both new properties; V-04 uses lifecycle contract form with prose-appended
adversary declarations and defeat conditions; V-05 uses elevated titled adversary
declaration blocks with explicit ADVERSARY:/TRIGGER:/DEFEAT CONDITION: fields.
If all three score identically under v15, C-45 and C-46 are form-agnostic --
consistent with R11-R14 confirmations that all structural criteria are
form-agnostic across prose, lifecycle-contract, and titled-block presentation.
