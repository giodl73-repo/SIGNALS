
# Variations: `topic:status` -- Round 11
**Rubric:** v11 (max 245) | **Date:** 2026-03-15

---

## Design Context

R10 differentiating evidence: V-01, V-04, V-05 each scored 235/235 under v10;
V-02 and V-03 scored 230/235. Two Tier 10 criteria were extracted from R10
excellence signals:

- **C-37**: GUARD-site trigger characterization. R10 V-04 satisfied C-37
  (lifecycle GUARD variant: each named exit carries an inline trigger clause at
  the GUARD declaration site, e.g. `Exit A -- file absent: fires when
  strategy.md does not exist on disk`). R10 V-01, V-02, V-03, V-05 failed C-37
  (exit names present but no inline trigger clauses at the GUARD declaration
  site; trigger characterization exists only in the preamble).

- **C-38**: Phase-output invariant declaration. R10 V-05 satisfied C-38 (an
  explicit PHASE 2 OUTPUT DECLARATION block embedded in the PHASE 2 execution
  body -- active during phase execution, not after all phases complete). R10
  V-01 used a COMMIT DECISION echo (post-execution commit-framing section:
  valid C-36 third site, fails C-38 -- outside any execution phase body). R10
  V-04 used a lifecycle PHASE 2 OUTPUT field in the contract block header
  (phase definition field: valid C-36 third site, fails C-38 -- structural
  header, not execution body). V-02, V-03 did not attempt C-38.

**R10 gap:** No R10 variant achieved 245.
- V-04 satisfies C-37 (GUARD-site trigger clauses) but not C-38 (lifecycle
  OUTPUT field in contract header, not execution body).
- V-05 satisfies C-38 (execution-body OUTPUT DECLARATION) but not C-37
  (execution-body trigger sentences; the GUARD field carries named exits without
  inline trigger characterization).
- C-37 and C-38 are structurally orthogonal. Neither is implied by the other.

**R11 hypothesis:** The gap closes by combining the C-37 mechanism from R10
V-04 (inline trigger clauses at GUARD exit declaration site) with the C-38
mechanism from R10 V-05 (execution-body PHASE 2 OUTPUT DECLARATION block) in a
single variant. V-01 tests this minimum delta in execution-prose form. V-02
withholds C-37 (isolation: exits named but not trigger-characterized at the
GUARD site). V-03 withholds C-38 (isolation: COMMIT DECISION echo as third C-36
site -- valid for C-36, but post-execution, so C-38 FAIL). V-04 tests both via
lifecycle GUARD contract form (C-37 form-agnosticism test). V-05 tests C-38 via
a formally titled, visually demarcated PHASE 2 OUTPUT DECLARATION block within
the execution body (C-38 block-form test).

**Predicted score map:**

| Variant | C-35 | C-36 | C-37 | C-38 | Predicted |
|---------|------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | PASS | 245/245   |
| V-02    | PASS | PASS | FAIL | PASS | 240/245   |
| V-03    | PASS | PASS | PASS | FAIL | 240/245   |
| V-04    | PASS | PASS | PASS | PASS | 245/245   |
| V-05    | PASS | PASS | PASS | PASS | 245/245   |

Axes: minimum delta combining C-37+C-38 in execution-prose form (V-01);
C-37 withheld isolation (V-02); C-38 withheld isolation (V-03); lifecycle GUARD
contract form with C-37+C-38 (V-04); lifecycle + elevated titled PHASE 2 OUTPUT
DECLARATION block (V-05).

---

## V-01: Minimum delta -- C-37+C-38 in execution-prose form

**Axis:** Minimum structural delta from R10 V-01. Two targeted changes: (1)
each exit declaration in PHASE 2 carries an inline trigger clause at the
declaration site (`Exit A -- file absent: fires when strategy.md does not exist
on disk`), satisfying C-37; (2) the C-36 third site is a PHASE 2 OUTPUT
DECLARATION block embedded within the PHASE 2 execution body (not a COMMIT
DECISION echo), satisfying C-38. All other structure identical to R10 V-01.

**Hypothesis:** C-37 requires one additional clause per exit line; C-38
requires relocating the invariant declaration from post-execution (COMMIT
DECISION) to within PHASE 2's execution body. If V-01 reaches 245, the
combination is confirmed compatible in execution-prose form and minimum delta
is sufficient. The delta between V-01 (245) and V-02 (240) isolates C-37. The
delta between V-01 (245) and V-03 (240) isolates C-38.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Vocabulary coherence invariant ---------------------------------------------
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
    Dual-axis gate invariant: file-absent and topic-absent exits are structurally
    distinct stop conditions with distinct messages.
    Output: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.

PHASE 3 -- EXPOSURE COMPUTATION
  percent = VERIFIED count / PLANNED count * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY

PHASE 4 -- DISPLAY GATE
  Pre-display invariant: COMMIT RISK REGISTER has one row per planned signal.
  Render in template section order.
  Write no files.
```

---

## V-02: Single-axis -- C-37 withheld (isolation test)

**Axis:** C-37 deliberately withheld. Exit declarations carry names only -- no
inline trigger clauses at the GUARD declaration site. C-38 present: execution-
body PHASE 2 OUTPUT DECLARATION is the C-36 third site. All other structure
identical to V-01, including preamble per-axis trigger sentences (C-35 PASS).

**Hypothesis:** If C-37 requires trigger characterization co-located at the
GUARD exit declaration site itself -- beyond what C-35 establishes at the
preamble site -- removing the inline "fires when..." clauses from each exit
declaration should fail C-37 while leaving C-38 intact. Expected 5-point gap
from V-01 (245). Preamble per-axis trigger sentences (C-35) are present: C-37
is independently necessary beyond the preamble-site characterization C-35
establishes. If the gap is 0, preamble trigger sentences satisfy both C-35 and
C-37 -- but this contradicts C-37's explicit GUARD-site co-location requirement.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Vocabulary coherence invariant ---------------------------------------------
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
  Read simulations/strategy.md.
  Exit A -- file absent:
    Output: "No planned baseline -- commit exposure is unquantifiable."
    Stop.
  Exit B -- topic not registered:
    If strategy.md present but contains no entry for {topic}:
    Output: "topic not registered: no planned signals for {topic}"
    Stop before PHASE 3.
  Extract planned signals for {topic}.
  For each planned signal P:
    If P matches a file in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Assert each signal individually. No batch evaluation.
  PHASE 2 OUTPUT DECLARATION:
    Dual-axis gate invariant: file-absent and topic-absent exits are structurally
    distinct stop conditions with distinct messages.
    Output: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.

PHASE 3 -- EXPOSURE COMPUTATION
  percent = VERIFIED count / PLANNED count * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY

PHASE 4 -- DISPLAY GATE
  Pre-display invariant: COMMIT RISK REGISTER has one row per planned signal.
  Render in template section order.
  Write no files.
```

---

## V-03: Single-axis -- C-38 withheld (isolation test)

**Axis:** C-38 deliberately withheld. Exit declarations carry inline trigger
clauses (C-37 present). Third C-36 site is the COMMIT DECISION block echo --
a post-execution commit-framing section (C-36 PASS: valid third site as
confirmed by R10 V-01; C-38 FAIL: post-execution, outside any execution phase
body). No PHASE 2 OUTPUT DECLARATION in the execution body. All other structure
identical to V-01.

**Hypothesis:** If C-38 requires the third C-36 site to be an execution-body
OUTPUT DECLARATION, replacing the execution-body PHASE 2 OUTPUT DECLARATION
with a COMMIT DECISION echo should fail C-38 while leaving C-37 and C-36
intact. Expected 5-point gap from V-01 (245). The COMMIT DECISION echo
satisfies C-36 (confirmed R10 V-01 at 235) -- C-38 is independently necessary
beyond C-36's minimum-sufficient third-site requirement. If the gap is 0,
execution-body residency is not independently required and C-38 is degenerate
with C-36 -- but this contradicts C-38's explicit execution-phase-resident form
requirement.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Vocabulary coherence invariant ---------------------------------------------
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
  Dual-axis gate invariant: file-absent and topic-absent exits are structurally distinct stop conditions with distinct messages

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

PHASE 3 -- EXPOSURE COMPUTATION
  percent = VERIFIED count / PLANNED count * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY

PHASE 4 -- DISPLAY GATE
  Pre-display invariant: COMMIT RISK REGISTER has one row per planned signal.
  Render in template section order.
  Write no files.
```

---

## V-04: Combination -- Lifecycle GUARD form with C-37+C-38

**Axes:** Lifecycle emphasis (phase contract blocks with INPUT / GUARD / OUTPUT
fields) + C-37 via GUARD field entries carrying inline trigger clauses at the
GUARD declaration site + C-38 via a PHASE 2 OUTPUT DECLARATION appended to the
PHASE 2 execution section (after the contract block header, within the execution
body). Tests whether C-37 is form-agnostic across execution-prose (V-01) and
lifecycle GUARD contract (V-04) entry formats.

**Hypothesis:** C-37 requires co-location of exit name and trigger clause at
the GUARD declaration site, form-agnostic. GUARD contract entries with inline
trigger clauses (`Exit A -- file absent: fires when strategy.md does not exist
on disk ->`) satisfy C-37 via the GUARD-field path, same as V-01 satisfies it
via inline execution prose. For C-38, the PHASE 2 OUTPUT DECLARATION block
appended to the execution section (the indented text below the contract header
box) is execution-body resident -- distinct from the OUTPUT field within the
contract header box (a phase-definition field, which is the R10 V-04 failure
case). If V-04 reaches 245, C-37 is confirmed form-agnostic. If V-04 reaches
245 and V-01 fails C-37, C-37 requires the GUARD-contract-field form.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Vocabulary coherence invariant ---------------------------------------------
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
  Read simulations/strategy.md. Apply GUARD exits in order.
  Extract planned signals for {topic}.
  For each planned signal P:
    If P matches a file in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Assert each signal individually.
  PHASE 2 OUTPUT DECLARATION:
    Dual-axis gate invariant: file-absent and topic-absent exits are structurally
    distinct stop conditions with distinct messages.
    Output: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.

+-- PHASE 3 -- EXPOSURE COMPUTATION ----------------------------------------+
| INPUT:  VERIFIED/UNVERIFIED assertions from PHASE 2                         |
| OUTPUT: percent, readiness verdict                                          |
+---------------------------------------------------------------------------+
  percent = VERIFIED / PLANNED * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY

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

## V-05: Combination -- Lifecycle GUARD + elevated titled PHASE 2 OUTPUT DECLARATION block

**Axes:** Lifecycle emphasis + C-37 via GUARD entries with inline trigger
clauses + C-38 via a formally titled, visually demarcated PHASE 2 OUTPUT
DECLARATION block embedded within the PHASE 2 execution section. The block is
elevated: it appears as an explicitly named box (`+-- PHASE 2 OUTPUT
DECLARATION --+`) within the execution body, making the execution-phase-resident
nature visually unambiguous and independently verifiable without reference to
the preamble or GUARD entries.

**Hypothesis:** C-38 requires an "explicitly declared OUTPUT DECLARATION block
embedded within the execution phase body." The elevated titled block form
(`+-- PHASE 2 OUTPUT DECLARATION -- dual-axis gate invariant -+`) is maximally
explicit about its execution-body-resident status. If V-05 reaches 245 alongside
V-01 and V-04, C-38 is form-agnostic across execution-body OUTPUT DECLARATION
styles (inline-appended V-01, inline-appended in lifecycle V-04, titled block
V-05). If only V-05 satisfies C-38 and V-01/V-04 fail, C-38 requires the
elevated titled-block form -- but C-38's rubric language ("explicitly declared")
is satisfied by all three forms, so uniform 245 is predicted.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Vocabulary coherence invariant ---------------------------------------------
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
  Read simulations/strategy.md. Apply GUARD exits in order.
  Extract planned signals for {topic}.
  For each planned signal P:
    If P matches a file in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Assert each signal individually.

  +-- PHASE 2 OUTPUT DECLARATION -- dual-axis gate invariant ---------------+
  | Dual-axis gate invariant: file-absent and topic-absent exits are          |
  | structurally distinct stop conditions with distinct messages.             |
  | Output: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.    |
  +--------------------------------------------------------------------------+

+-- PHASE 3 -- EXPOSURE COMPUTATION ----------------------------------------+
| INPUT:  VERIFIED/UNVERIFIED assertions from PHASE 2                         |
| OUTPUT: percent, readiness verdict                                          |
+---------------------------------------------------------------------------+
  percent = VERIFIED / PLANNED * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY

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

| ID | Axis | C-35 | C-36 | C-37 | C-38 | Score |
|----|------|------|------|------|------|-------|
| V-01 | Min delta: C-37+C-38 in execution-prose form | PASS | PASS | PASS | PASS | 245/245 |
| V-02 | C-37 withheld -- exits named, no inline trigger clauses | PASS | PASS | FAIL | PASS | 240/245 |
| V-03 | C-38 withheld -- COMMIT DECISION echo as third C-36 site | PASS | PASS | PASS | FAIL | 240/245 |
| V-04 | Lifecycle GUARD contract form with C-37+C-38 | PASS | PASS | PASS | PASS | 245/245 |
| V-05 | Lifecycle + elevated titled PHASE 2 OUTPUT DECLARATION block | PASS | PASS | PASS | PASS | 245/245 |

**C-37 isolation test (V-01 vs V-02):** V-02 retains preamble trigger sentences
(C-35 PASS) and execution-body OUTPUT DECLARATION (C-38 PASS) but withholds
inline trigger clauses at GUARD exit declaration sites. Expected 5-point gap
confirms that GUARD-site co-location of trigger characterization is independently
necessary beyond what C-35 establishes at the preamble site. If gap is 0,
C-35 and C-37 are degenerate (preamble trigger sentences satisfy both) --
contradicting C-37's explicit GUARD-site requirement.

**C-38 isolation test (V-01 vs V-03):** V-03 retains GUARD-site trigger clauses
(C-37 PASS) and uses COMMIT DECISION echo as the C-36 third site. C-36 PASS
(COMMIT DECISION is a valid third site, confirmed R10 V-01 at 235). Expected
5-point gap confirms that execution-body residency is independently necessary
beyond C-36's minimum-sufficient third-site requirement. If gap is 0, any valid
C-36 third site satisfies C-38 -- contradicting C-38's execution-phase-resident
form requirement.

**C-37 form-agnosticism (V-01 vs V-04):** V-01 uses execution-prose exit form;
V-04 uses lifecycle GUARD contract entries. If both score 245, C-37 is
form-agnostic across exit declaration styles (prose and contract-field both
satisfy when trigger clause is co-located at the exit declaration site). If
only V-04 reaches 245 and V-01 fails C-37, C-37 specifically requires the
GUARD-contract-field form.

**C-38 block-form agnosticism (V-01 vs V-04 vs V-05):** V-01 uses inline-
appended `PHASE 2 OUTPUT DECLARATION:` text in prose. V-04 uses the same inline
form in lifecycle structure. V-05 uses a formally titled `+-- PHASE 2 OUTPUT
DECLARATION --+` box. If all three score 245, C-38 is form-agnostic across
execution-body OUTPUT DECLARATION styles. If only V-05 satisfies C-38, C-38
requires the elevated titled-block form -- but rubric language ("explicitly
declared block") is satisfied by the inline label form as well as the box form.
Uniform 245 across V-01, V-04, V-05 is the predicted outcome.
