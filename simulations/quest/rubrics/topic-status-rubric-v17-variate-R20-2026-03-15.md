# Variations: `topic:status` -- Round 20
**Rubric:** v17 (max 300) | **Date:** 2026-03-15

---

## Design Context

R19 differentiating evidence (confirmed under v17): V-01 → 300; V-02 → 295
(C-47 FAIL); V-03 → 295 (C-48 FAIL, C-49 vacuous PASS); V-04 → 295 (C-49
FAIL); V-05 → 290 (C-47 FAIL + C-49 FAIL, C-48 PASS).

**R19 closure:** R19 V-05 closed the final gap in the tier-16 ablation matrix
by generating the C-47 FAIL + C-49 FAIL (C-48 PASS) cross-axis combination.
After R19, all reachable tier-16 combinations are confirmed:

- C-47 solo ablation: R19 V-02 (295)
- C-48 solo ablation: R19 V-03 (295, C-49 vacuous)
- C-49 solo ablation: R19 V-04 (295)
- C-47 + C-48 cross-axis: R18 V-05 (290, C-49 vacuous)
- C-47 + C-49 cross-axis: R19 V-05 (290, C-48 PASS)
- C-48 + C-49 cross-axis: structurally impossible (C-48 FAIL yields C-49 vacuous PASS)

**R20 purpose:** Probe for v18 candidate criteria. The tier-16 ablation matrix
is exhausted under v17; all single-axis and feasible cross-axis combinations
have differentiating scores. R20 introduces two new structural elements in V-01
that V-02 through V-05 ablate for isolation. These elements are candidates for v18:

- **C-50 candidate** (output format axis): STOP CONDITION predicate entries
  carry phase-addressable labels matching the preamble ADVERSARY CHAIN labels
  -- `[P-N-ADVERSARY DEFEAT:]` prefixes on predicates (2)/(3)/(4), making each
  adversary defeat check independently addressable by its phase label. Predicate
  (1) retains the numbered form: COMMIT RISK REGISTER row-count is a structural
  completeness guard, not an adversary defeat check, and carries no adversary
  label. This is the STOP CONDITION parallel of C-47's labeled-entry extension
  of the preamble ADVERSARY CHAIN block: C-47 made preamble entries
  phase-addressable by label; C-50 makes STOP CONDITION adversary-defeat
  predicates phase-addressable by the same label set. Implication candidate:
  C-50 => C-49 (the PHASE 1 defeat predicate must exist before it can be
  labeled) and C-50 => C-47 (the preamble labels must exist before the STOP
  CONDITION labels can be defined as matching them).

- **C-51 candidate** (lifecycle emphasis axis): Preamble ADVERSARY CHAIN
  labeled entries carry nested `DEFEAT CONDITION:` sub-components forecasting
  the observable defeat property for each phase. The P-N-ADVERSARY entries
  currently carry adversary name and consequence description (C-47 form); C-51
  extends each entry with a nested DEFEAT CONDITION: sub-component carrying the
  same observable property that the execution-body adversary block's DEFEAT
  CONDITION declares. The preamble thereby functions as a complete architectural
  forecast: not only which adversary each phase faces and what default occurs
  when the phase is skipped, but what observable property constitutes defeat.
  This is the preamble parallel of C-46's addition of DEFEAT CONDITION to
  execution-body adversary blocks: C-46 extended execution-body blocks from
  two-part to three-part form; C-51 extends preamble entries from two-part
  (adversary name + consequence) to three-part (adversary name + consequence +
  defeat forecast). Implication candidates: C-51 => C-47 (labeled entries must
  exist before sub-components can be nested within them); C-51 => C-46
  (execution-body DEFEAT CONDITION must exist before the preamble can forecast
  it; preamble forecasts cannot precede the execution declarations they mirror).

**Under v17:** All five R20 variants that satisfy C-01 through C-49 score 300.
The C-50 and C-51 candidate elements are super-threshold under v17: they are
not evaluated by any v17 criterion and contribute 0 pts to v17 scores. The
ablation axes will yield differentiating scores when v18 is written from R20
excellence signals.

**Projected R20 scores under v17:**

| Variant | C-50 | C-51 | Under v17 | Notes |
|---------|------|------|-----------|-------|
| V-01 | PASS | PASS | 300 | Both v18 candidates present; richest prompt body |
| V-02 | FAIL | PASS | 300 | C-50 withheld: numbered STOP predicates |
| V-03 | PASS | FAIL | 300 | C-51 withheld: preamble entries lack DEFEAT forecast |
| V-04 | FAIL | FAIL | 300 | Both withheld; structurally equivalent to R19 V-01 |
| V-05 | PASS | PARTIAL | 300 | C-51 partial: P1 preamble DEFEAT CONDITION absent |

**Projected R20 scores under v18 (hypothetical, assuming 5 pts each):**

| Variant | C-50 | C-51 | Under v18 | Notes |
|---------|------|------|-----------|-------|
| V-01 | PASS | PASS | 310 | Full tier-17 baseline |
| V-02 | FAIL | PASS | 305 | C-50 withheld |
| V-03 | PASS | FAIL | 305 | C-51 withheld |
| V-04 | FAIL | FAIL | 300 | Pure v17 baseline |
| V-05 | PASS | PARTIAL | 305* | C-51 partial; partial-credit rule TBD by v18 |

*V-05 isolates whether C-51 is all-or-nothing (all three preamble entries must
carry DEFEAT CONDITION: sub-components for C-51 PASS) or admits partial credit
for two-of-three. The V-01 vs V-05 delta under v18 will answer this question.

**C-50 structural note:** The `[P-N-ADVERSARY DEFEAT:]` labels use bracket
notation to signal their role as phase-addressable defeat-check entries,
parallel to how `[LAYER N]` labels signal enforcement scope. The label matches
the preamble entry label exactly: P1-ADVERSARY, P2-ADVERSARY, P3-ADVERSARY.
The order in the STOP CONDITION is (1) row-count guard, then P2, P3, P1 --
retaining the R19 V-01 execution-completion order (P2 and P3 defeat checks
come from the evaluation phases whose results are being displayed; P1 defeat
check is the acquisition-phase gate that precedes all evaluation). The
phase-addressable label makes each predicate independently citable by phase,
regardless of the order in which they appear in the STOP CONDITION block.

**C-51 structural note:** The nested DEFEAT CONDITION: sub-components in the
preamble carry the same observable property text as the execution-body DEFEAT
CONDITION: declarations, condensed to a single phrase. The preamble is
necessarily terse -- it is a structural forecast, not an execution body -- so
the DEFEAT CONDITION sub-component in the preamble omits the conditional
grammar (the "if glob returns empty, execution stops..." narrative) and carries
only the core observable property (e.g., "DISK_SIGNALS populated from live
glob result; zero-result case handled before PHASE 2 executes"). The execution
body retains the full DEFEAT CONDITION: with conditional grammar.

**V-05 asymmetry probes P1 structural weight:** C-48 added the PHASE 1
adversary execution body; C-49 added the PHASE 1 STOP predicate; C-51 would
add the PHASE 1 preamble defeat forecast. In V-05, P1 specifically lacks the
preamble defeat forecast while P2 and P3 carry it. This tests whether P1
carries special structural weight in the preamble (because it is the most
recently added phase to the adversary chain) or whether C-51 applies uniformly
to all three phases.

**Variation axes:**
- V-02: Output format -- numbered STOP predicates without phase labels (C-50 FAIL)
- V-03: Lifecycle emphasis -- preamble entries carry no defeat forecast (C-51 FAIL)
- V-04: Baseline -- pure v17 max, no candidate tier-17 features (C-50 + C-51 FAIL)
- V-05: Lifecycle emphasis partial -- P1 preamble DEFEAT CONDITION absent only

---

## V-01: Full-stack baseline -- labeled STOP predicates + preamble defeat forecasts

**Axis:** Full tier-17 seeding baseline. Preamble ADVERSARY CHAIN carries
three-part sub-entries: each P-N-ADVERSARY: label is followed by (i) adversary
name with consequence description (C-47 form) and (ii) a nested DEFEAT
CONDITION: sub-component forecasting the observable defeat property for that
phase (C-51 candidate PASS). PHASE 4 DISPLAY GATE STOP CONDITION carries the
row-count guard as predicate (1) and three phase-labeled adversary defeat checks
as `[P2-ADVERSARY DEFEAT:]`, `[P3-ADVERSARY DEFEAT:]`, `[P1-ADVERSARY DEFEAT:]`
entries (C-50 candidate PASS). All tier-16 criteria (C-47, C-48, C-49) and all
prior criteria satisfied. The prompt body is a strict superset of R19 V-01.

**Hypothesis:** V-01 introduces the two candidate criteria for v18 in their
full form. Under v17: 300/300 (C-50 and C-51 are super-threshold, not scored).
Under v18 (projected): 310/310, serving as the tier-17 full-stack baseline.
Observable structural additions over R19 V-01: (a) preamble ADVERSARY CHAIN
entries carry nested DEFEAT CONDITION: sub-components; (b) STOP CONDITION
predicates (2)-(4) carry `[P-N-ADVERSARY DEFEAT:]` phase labels. Expected:
300/300 under v17.

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
    DEFEAT CONDITION: DISK_SIGNALS populated from live glob result; zero-result
    case handled explicitly before PHASE 2 commitment assertion executes.
  P2-ADVERSARY: inertia toward evidence-blind commits (default when PHASE 2 is
    skipped: unverified signals ship without explicit assertion);
    DEFEAT CONDITION: all planned signals individually asserted with explicit
    VERIFIED or UNVERIFIED state; no signal exits without assertion on record.
  P3-ADVERSARY: inertia toward coverage-blind verdicts (default when PHASE 3 is
    skipped: percent emitted without consistency guard verification);
    DEFEAT CONDITION: percent computed with consistency guard applied;
    UNVERIFIED-non-empty and percent-100% contradiction halted before verdict.
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
    [P2-ADVERSARY DEFEAT:] all planned signals individually asserted; each
      carries an explicit VERIFIED or UNVERIFIED state on the record
    [P3-ADVERSARY DEFEAT:] percent computed with consistency guard applied;
      UNVERIFIED-non-empty and percent-100% contradiction detected and halted
      before readiness verdict issued
    [P1-ADVERSARY DEFEAT:] DISK_SIGNALS populated from live glob result -- not
      from memory or prior-round assumption; zero-result case handled explicitly
      before PHASE 2 commitment assertion executed
  Render in template section order.
  Write no files.
```

---

## V-02: Single axis -- output format (numbered STOP predicates; C-50 withheld)

**Axis:** Output format -- the PHASE 4 DISPLAY GATE STOP CONDITION reverts
to the R19 V-01 numbered form: predicates (1) through (4) with no
`[P-N-ADVERSARY DEFEAT:]` phase labels (C-50 FAIL: STOP predicates not
phase-label-addressable). Preamble ADVERSARY CHAIN retains full three-part
sub-entries with nested DEFEAT CONDITION: sub-components (C-51 PASS). All
execution-body adversary blocks and execution logic identical to V-01.
C-47 PASS, C-48 PASS, C-49 PASS. Observable structural gap: V-01 STOP
CONDITION carries `[P2-ADVERSARY DEFEAT:]`, `[P3-ADVERSARY DEFEAT:]`,
`[P1-ADVERSARY DEFEAT:]` phase-labeled entries; V-02 STOP CONDITION carries
`(2) PHASE 2 adversary defeated:`, `(3) PHASE 3 adversary defeated:`,
`(4) PHASE 1 adversary defeated:` numbered entries. Preamble ADVERSARY CHAIN
entries are identical in both variants (three-part form with DEFEAT CONDITION).

**Hypothesis:** C-50 requires phase-addressable labels on STOP CONDITION
adversary defeat predicates. The numbered form carries the same semantic
content but lacks the phase-label-addressable structure that would allow each
predicate to be independently cited by its phase label. C-51 PASS: preamble
three-part entries intact. Under v17: 300 (C-50 not scored). Under v18
(projected): 305 (C-50 FAIL, -5). Expected: 300/300 under v17.

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
    DEFEAT CONDITION: DISK_SIGNALS populated from live glob result; zero-result
    case handled explicitly before PHASE 2 commitment assertion executes.
  P2-ADVERSARY: inertia toward evidence-blind commits (default when PHASE 2 is
    skipped: unverified signals ship without explicit assertion);
    DEFEAT CONDITION: all planned signals individually asserted with explicit
    VERIFIED or UNVERIFIED state; no signal exits without assertion on record.
  P3-ADVERSARY: inertia toward coverage-blind verdicts (default when PHASE 3 is
    skipped: percent emitted without consistency guard verification);
    DEFEAT CONDITION: percent computed with consistency guard applied;
    UNVERIFIED-non-empty and percent-100% contradiction halted before verdict.
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

## V-03: Single axis -- lifecycle emphasis (preamble two-part entries; C-51 withheld)

**Axis:** Lifecycle emphasis -- preamble ADVERSARY CHAIN labeled entries
retain the two-part form from R19 V-01: adversary name with consequence
description only, no nested DEFEAT CONDITION: sub-component (C-51 FAIL:
preamble entries do not forecast execution-body defeat properties). The
preamble ADVERSARY CHAIN is the same as R19 V-01 at the structural level.
PHASE 4 DISPLAY GATE STOP CONDITION retains phase-labeled adversary defeat
predicates (C-50 PASS). All execution-body adversary blocks and logic identical
to V-01. C-47 PASS (labeled entries present), C-48 PASS, C-49 PASS.
Observable structural gap: V-01 preamble each P-N-ADVERSARY: entry has a
nested DEFEAT CONDITION: sub-component; V-03 preamble each P-N-ADVERSARY:
entry carries adversary name and consequence only (two-part form).

**Hypothesis:** C-51 requires preamble ADVERSARY CHAIN labeled entries to
carry nested DEFEAT CONDITION: sub-components. The two-part entry form satisfies
C-47 (labeled entries present) but fails C-51 (no defeat forecast sub-component).
C-50 PASS (phase-labeled STOP predicates intact). Under v17: 300 (C-51 not
scored). Under v18 (projected): 305 (C-51 FAIL, -5). Expected: 300/300 under v17.

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
    [P2-ADVERSARY DEFEAT:] all planned signals individually asserted; each
      carries an explicit VERIFIED or UNVERIFIED state on the record
    [P3-ADVERSARY DEFEAT:] percent computed with consistency guard applied;
      UNVERIFIED-non-empty and percent-100% contradiction detected and halted
      before readiness verdict issued
    [P1-ADVERSARY DEFEAT:] DISK_SIGNALS populated from live glob result -- not
      from memory or prior-round assumption; zero-result case handled explicitly
      before PHASE 2 commitment assertion executed
  Render in template section order.
  Write no files.
```

---

## V-04: Baseline -- pure v17 max (C-50 + C-51 both withheld)

**Axis:** Baseline -- structurally equivalent to R19 V-01. Both candidate
tier-17 features withheld: preamble ADVERSARY CHAIN entries are two-part
form (no nested DEFEAT CONDITION sub-components; C-51 FAIL) and STOP CONDITION
predicates use the R19 numbered form (no phase labels; C-50 FAIL). All v17
criteria C-01 through C-49 satisfied: labeled preamble entries (C-47), PHASE 1
execution-body adversary block (C-48), four STOP CONDITION predicates including
PHASE 1 defeat gate (C-49). This variant establishes the pure v17 ceiling as
a reference point within R20, confirming that V-01 vs V-02 and V-01 vs V-03
deltas are entirely attributable to the two new structural elements and not to
any residual v17 structure.

**Hypothesis:** V-04 is the R20 baseline. It satisfies exactly v17's C-01
through C-49 and no more. Under v17: 300/300. Under v18 (projected): 300
(C-50 FAIL, C-51 FAIL; no tier-17 criteria satisfied). The V-01 vs V-04 delta
under v18 will measure the combined value of C-50 + C-51 (projected +10).
The V-02 vs V-04 delta under v18 will isolate C-51 (+5); the V-03 vs V-04
delta under v18 will isolate C-50 (+5). Expected: 300/300 under v17.

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

## V-05: Combination -- C-50 PASS + C-51 partial (P1 preamble defeat forecast absent)

**Axis:** Lifecycle emphasis partial -- PHASE 4 DISPLAY GATE STOP CONDITION
retains phase-labeled adversary defeat predicates (C-50 PASS). Preamble
ADVERSARY CHAIN carries DEFEAT CONDITION: sub-components for P2-ADVERSARY and
P3-ADVERSARY but not for P1-ADVERSARY (C-51 partial: three-part form present
at two of three entry sites). P1-ADVERSARY entry carries only the two-part
form (adversary name + consequence). P2-ADVERSARY and P3-ADVERSARY entries
carry the three-part form (adversary name + consequence + defeat forecast).
The asymmetry isolates whether C-51 requires all three preamble entries to
carry DEFEAT CONDITION: sub-components (all-or-nothing) or whether it can be
satisfied by two-of-three (partial credit).

**Hypothesis:** C-51 partial -- P1 is the most recently added phase to the
adversary chain (C-48 added the PHASE 1 execution-body adversary; C-49 added
the PHASE 1 STOP predicate). If C-51 is all-or-nothing, V-05 will score the
same as V-03 under v18 (C-51 FAIL, -5). If C-51 admits partial credit for
P2+P3 without P1, V-05 will score between V-01 and V-03. The V-03 vs V-05
delta under v18 resolves the all-or-nothing question. C-50 PASS (phase-labeled
STOP predicates intact). C-47 PASS (all three preamble entries labeled),
C-48 PASS, C-49 PASS. Under v17: 300. Under v18 (projected): 305 if C-51 is
all-or-nothing (same as V-03); TBD if partial credit applies. Expected:
300/300 under v17.

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
    DEFEAT CONDITION: all planned signals individually asserted with explicit
    VERIFIED or UNVERIFIED state; no signal exits without assertion on record.
  P3-ADVERSARY: inertia toward coverage-blind verdicts (default when PHASE 3 is
    skipped: percent emitted without consistency guard verification);
    DEFEAT CONDITION: percent computed with consistency guard applied;
    UNVERIFIED-non-empty and percent-100% contradiction halted before verdict.
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
    [P2-ADVERSARY DEFEAT:] all planned signals individually asserted; each
      carries an explicit VERIFIED or UNVERIFIED state on the record
    [P3-ADVERSARY DEFEAT:] percent computed with consistency guard applied;
      UNVERIFIED-non-empty and percent-100% contradiction detected and halted
      before readiness verdict issued
    [P1-ADVERSARY DEFEAT:] DISK_SIGNALS populated from live glob result -- not
      from memory or prior-round assumption; zero-result case handled explicitly
      before PHASE 2 commitment assertion executed
  Render in template section order.
  Write no files.
```
