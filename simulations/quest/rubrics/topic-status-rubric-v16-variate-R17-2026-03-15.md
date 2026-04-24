# Variations: `topic:status` -- Round 17
**Rubric:** v16 (max 295) | **Date:** 2026-03-15

---

## Design Context

R16 differentiating evidence: V-01/V-04/V-05 scored 295/295 under v16; V-02 scored
290/295 (C-47 FAIL); V-03 scored 280/295 (C-47 PASS, C-48 FAIL, C-12 FAIL, C-20 FAIL).
The v16 rubric confirms two Tier 15 criteria:

- **C-47**: Preamble adversary chain labeled sub-component entries. The preamble
  `ADVERSARY CHAIN:` block carries labeled `PN-ADVERSARY:` sub-entries making
  each phase adversary independently addressable by phase label. Label count
  tracks chain length: two labels (P2-ADVERSARY:, P3-ADVERSARY:) when C-48 absent;
  three labels (P1-ADVERSARY:, P2-ADVERSARY:, P3-ADVERSARY:) when C-48 present.
  Prerequisite: C-45.

- **C-48**: PHASE 1 execution-body adversary declaration. PHASE 1 gains an
  `ADVERSARY:` clause with `DEFEAT CONDITION:` sub-component, extending the
  execution-body adversary chain from two phases (P2+P3) to three (P1+P2+P3).
  Prerequisite: C-46.

**R16 gap:** The V-01 vs V-02 delta cleanly isolates C-47 (5-point delta,
V-02 fails C-47 only). The V-01 vs V-03 delta is contaminated: V-03 fails C-48
as intended but also fails C-12 and C-20 due to the readiness-first template
reordering axis applied in R16 (-10 pts contamination). C-48 isolation is
confirmed by the V-02/V-04/V-05 PASS evidence, but R17 must provide a clean V-03
with C-48 isolated as the sole failure. The V-02 vs V-03 symmetric delta (both
290) under v16 will confirm C-47 and C-48 orthogonality.

R17 primary purpose: redesign V-03 for clean C-48 isolation. V-01, V-02, V-04,
V-05 carry identical structure to their R16 counterparts (no new properties
introduced; all already achieved full-stack or single-clean-ablation scores).

**R17 V-03 redesign specification:**
- NO template reordering -- standard order preserved (LAYER 1 STRUCTURAL first)
- [LAYER 2] retains PER-SIGNAL COMMITMENT ASSERTION form and vocabulary
- Preamble ADVERSARY CHAIN block carries labeled P2-ADVERSARY: and P3-ADVERSARY:
  sub-entries (two-element labeled chain -- C-47 PASS; consistent with the rule
  that label count tracks chain length: two labels when C-48 absent)
- No P1-ADVERSARY: entry in preamble (consistent with no PHASE 1 execution body
  adversary; the absence of a P1-ADVERSARY: label is not a C-47 violation when
  no PHASE 1 adversary body has been declared)
- PHASE 1 execution body has no ADVERSARY: clause and no DEFEAT CONDITION:
  sub-component (C-48 FAIL -- isolated, no contamination)
- All other structure identical to V-01

**Orthogonality test for R17:**
V-01 vs V-02 delta = 5 pts (C-47). V-01 vs V-03 delta = 5 pts (C-48). V-02 vs
V-03 delta = 0 pts (symmetric 290 scores). This symmetric delta proves C-47 and
C-48 are independently observable -- neither implies the other.

**Predicted score map under v16:**

| Variant | C-47 | C-48 | C-12 | C-20 | Predicted |
|---------|------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | PASS | 295/295   |
| V-02    | FAIL | PASS | PASS | PASS | 290/295   |
| V-03    | PASS | FAIL | PASS | PASS | 290/295   |
| V-04    | PASS | PASS | PASS | PASS | 295/295   |
| V-05    | PASS | PASS | PASS | PASS | 295/295   |

V-02 and V-03 score symmetrically at 290 -- confirming C-47 and C-48 orthogonality.

---

## V-01: Minimum delta -- C-47 + C-48 in execution-prose form

**Axis:** Minimum structural delta from R16 V-01 (identical body). Full-stack
baseline: preamble ADVERSARY CHAIN block carries labeled P1-ADVERSARY:,
P2-ADVERSARY:, P3-ADVERSARY: sub-components (C-47 PASS); PHASE 1 execution body
opens with ADVERSARY: / DEFEAT CONDITION: three-part block (C-48 PASS).
All 48 criteria satisfied.

**Hypothesis:** V-01 is the full-stack baseline for R17. The V-01 vs V-02 delta
isolates C-47 (V-02 withholds labeled preamble sub-components). The V-01 vs V-03
delta isolates C-48 (V-03 withholds the PHASE 1 adversary block, no template
reordering contamination this round). V-04 and V-05 confirm form-agnosticism.
Expected: 295/295.

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
identical to V-01. Identical to R16 V-02 (clean C-47 isolation confirmed in R16).

**Hypothesis:** C-47 requires labeled `PN-ADVERSARY:` sub-components within
the preamble ADVERSARY CHAIN block. Running-prose enumeration of three adversaries
satisfies C-45 (the block exists, names both execution-phase adversaries) but
fails C-47 (no per-adversary label for independent addressability). C-48 intact:
PHASE 1 execution body carries full three-part adversary block. Under v16, V-02
scores 290 (C-47 FAIL, 5-point delta from V-01). Observable structural gap:
V-01's ADVERSARY CHAIN block uses `P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:`
labeled lines; V-02's block uses a single prose paragraph naming all three
adversaries without per-adversary labeling.

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

## V-03: Single axis -- C-48 withheld (redesigned clean isolation)

**Axis:** C-48 deliberately withheld -- PHASE 1 execution body carries no
`ADVERSARY:` clause and no `DEFEAT CONDITION:` sub-component. The adversary chain
remains a two-phase execution chain (P2+P3) with C-47-compliant labeled preamble
sub-components at those two phases only. Preamble ADVERSARY CHAIN block carries
`P2-ADVERSARY:` and `P3-ADVERSARY:` labeled sub-entries (two-element labeled
chain -- C-47 PASS; the rule that label count tracks chain length permits two
labels when no PHASE 1 adversary body is declared). No P1-ADVERSARY: entry in
preamble. Template order, LAYER labels, and all other structure identical to V-01.

**Redesign rationale (R16 contamination corrected):** R16 V-03 applied a
readiness-first template reordering axis alongside C-48 ablation, causing C-12
and C-20 failures unrelated to C-48. R17 V-03 applies NO additional axis: the
only structural difference from V-01 is the absence of the PHASE 1 adversary
block and the corresponding P1-ADVERSARY: preamble entry. This is the minimum
delta for C-48 isolation. C-12 passes because COMMIT RISK REGISTER remains LAYER
1 STRUCTURAL first section. C-20 passes because [LAYER 2] retains PER-SIGNAL
COMMITMENT ASSERTION vocabulary and form. C-47 passes because the preamble
ADVERSARY CHAIN block still carries labeled entries for the phases that have
execution-body adversary declarations (P2 and P3); the absence of P1-ADVERSARY:
is not a C-47 violation when PHASE 1 has no adversary body.

**Hypothesis:** V-03 scores 290/295 under v16 (C-48 FAIL, 5-point delta from
V-01). V-02 also scores 290/295 (C-47 FAIL). The symmetric 290/290 between V-02
and V-03 confirms C-47 and C-48 are orthogonal: withholding either independently
produces the same 5-point penalty; withholding both together (not tested in R17
directly) would produce a 10-point penalty. Observable structural gap: V-01's
PHASE 1 body opens with `ADVERSARY:` + `DEFEAT CONDITION:` before the Glob
instruction; V-03's PHASE 1 body opens directly with `Glob:` with no adversary
framing. Observable preamble gap: V-01's ADVERSARY CHAIN block has three labeled
entries (P1, P2, P3); V-03's block has two labeled entries (P2, P3).

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
  Pre-display invariant: COMMIT RISK REGISTER has one row per planned signal.
  Render in template section order.
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
Identical to R16 V-04 (form-agnosticism confirmed in R16). Tests whether C-47
and C-48 hold across lifecycle-contract execution style.

**Hypothesis:** C-47 and C-48 were confirmed form-agnostic in R16 -- lifecycle-
contract-appended adversary lines at all three phases satisfy alongside execution-
prose form (V-01). V-04 scores 295/295. If V-04 and V-01 score identically, C-47
and C-48 form-agnosticism is confirmed consistent with R11-R16 form-agnosticism
patterns. The labeled preamble ADVERSARY CHAIN block satisfies C-47 regardless
of whether execution phases use prose or lifecycle-contract format.

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
defeated). This extends the titled-block adversary pattern to PHASE 1, completing
a three-phase titled adversary chain. Identical to R16 V-05.

**Hypothesis:** C-46's titled-block form was confirmed in R15; C-48's titled-
block form was confirmed in R16. V-05 scores 295/295. If V-05 and V-01 score
identically, C-47 and C-48 are confirmed form-agnostic across execution-prose
(V-01), lifecycle-contract (V-04), and elevated-titled-block (V-05) presentation
styles -- consistent with R11-R16 form-agnosticism confirmations.

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

| Variant | Axis | C-47 | C-48 | C-12 | C-20 | Predicted (v16) |
|---------|------|------|------|------|------|-----------------|
| V-01 | Min delta, execution-prose (=R16 V-01) | PASS | PASS | PASS | PASS | 295/295 |
| V-02 | C-47 withheld, prose ADVERSARY CHAIN (=R16 V-02) | FAIL | PASS | PASS | PASS | 290/295 |
| V-03 | C-48 withheld only, no template reordering (redesigned) | PASS | FAIL | PASS | PASS | 290/295 |
| V-04 | Lifecycle GUARD contract form (=R16 V-04) | PASS | PASS | PASS | PASS | 295/295 |
| V-05 | Elevated titled adversary blocks (=R16 V-05) | PASS | PASS | PASS | PASS | 295/295 |

**Orthogonality confirmation:** V-02 and V-03 score symmetrically at 290/295.
Each single ablation (C-47 withheld or C-48 withheld) produces a 5-point penalty.
The delta between V-02 and V-03 is 0 -- confirming C-47 and C-48 are
independently observable: no phase's labeled preamble entry implies the other's
execution-body adversary block; no execution-body adversary block implies the
corresponding preamble labeled entry.

**Form-agnosticism:** V-04 and V-05 score identically to V-01 at 295/295 --
confirming C-47 and C-48 are satisfied by labeled preamble sub-components and
three-part phase adversary blocks across all three execution styles (prose,
lifecycle-contract, elevated-titled-block). Consistent with form-agnosticism
confirmed for all prior structural tier pairs in R11-R16.

**R17 primary result:** Clean C-48 isolation in V-03. The C-48 criterion is now
doubly confirmed: V-02/V-04/V-05 PASS evidence (C-48 present scores full points)
plus V-03 FAIL evidence (C-48 absent costs 5 points, no other criterion failed).
