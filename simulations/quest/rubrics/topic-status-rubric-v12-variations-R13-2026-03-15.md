
# Variations: `topic:status` -- Round 13
**Rubric:** v12 (max 255) | **Date:** 2026-03-15

---

## Design Context

R12 differentiating evidence: V-01, V-04, V-05 each scored 255/255 under v12;
V-02 and V-03 scored 250/255. The R12 scorecard confirms two new Tier 11
criteria extracted from R11 excellence signals:

- **C-39**: Per-axis trigger sentences within the OUTPUT DECLARATION INVARIANT
  sub-component. Third trigger-characterization site in the chain (preamble
  C-35, GUARD site C-37, OUTPUT DECLARATION site C-39). Each exit's trigger
  condition is named at this third structural location.

- **C-40**: Labeled sub-components within the OUTPUT DECLARATION -- `INVARIANT:`
  and `OUTPUT FORM:` labels make the dual-axis gate declaration and the per-signal
  output form independently addressable by name.

**R12 gap:** No R12 variant jointly fails C-41 and C-42 -- those criteria do
not yet exist. R13 probes genuinely new structural territory.

R13 introduces two new structural properties:

- **C-41 candidate**: PHASE 3 OUTPUT DECLARATION with labeled sub-components.
  An OUTPUT DECLARATION block embedded within PHASE 3's execution body --
  parallel to C-38 at PHASE 2. Contains `INVARIANT:` (consistency guard
  assertion with `Trigger:` sentence) and `OUTPUT FORM:` (percent, readiness
  verdict) labeled sub-components. Extends the output-declaration residency
  pattern from PHASE 2 to PHASE 3; extends the labeled-sub-structure pattern
  (C-40) to a second execution phase.

- **C-42 candidate**: Phase-entry adversary declaration within the PHASE 2
  execution body. An explicit `ADVERSARY:` clause at PHASE 2's execution
  section entry, naming inertia as what the phase defeats. Extends adversary
  framing from output-template-only (COMMIT DECISION, C-16) into the execution
  phase body. A two-site adversary chain: output template site (existing) and
  execution phase body site (new).

**Orthogonality**: C-41 concerns PHASE 3 output structure (OUTPUT DECLARATION
residency parallel). C-42 concerns PHASE 2 execution framing (adversary
declaration at phase entry). A variant can carry PHASE 3 OUTPUT DECLARATION
without adversary framing at PHASE 2 entry (C-41 PASS, C-42 FAIL) or
adversary framing at PHASE 2 entry without PHASE 3 OUTPUT DECLARATION
(C-41 FAIL, C-42 PASS).

**Predicted score map under v12:**

| Variant | C-39 | C-40 | C-41 | C-42 | Predicted |
|---------|------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | PASS | 255/255   |
| V-02    | PASS | PASS | FAIL | PASS | 255/255   |
| V-03    | PASS | PASS | PASS | FAIL | 255/255   |
| V-04    | PASS | PASS | PASS | PASS | 255/255   |
| V-05    | PASS | PASS | PASS | PASS | 255/255   |

All five variants score 255 under v12 -- C-41 and C-42 are not yet criteria.

Axes: minimum delta combining C-41+C-42 in execution-prose form (V-01);
C-41 withheld isolation -- adversary at PHASE 2 entry without PHASE 3 output
declaration (V-02); C-42 withheld isolation -- PHASE 3 output declaration
without adversary at PHASE 2 entry (V-03); lifecycle GUARD contract form with
C-41+C-42 (V-04); lifecycle + elevated titled blocks for PHASE 2 adversary and
PHASE 3 OUTPUT DECLARATION (V-05).

---

## V-01: Minimum delta -- C-41+C-42 in execution-prose form

**Axis:** Minimum structural delta from R12 V-01. Two targeted additions:
(1) PHASE 3 execution body receives a `PHASE 3 OUTPUT DECLARATION:` block with
`INVARIANT:` and `OUTPUT FORM:` labeled sub-components plus a `Trigger:`
sentence within the INVARIANT sub-component (C-41 candidate -- extends
output-declaration residency from PHASE 2 to PHASE 3, and extends C-39/C-40
labeled-trigger pattern to a second execution phase); (2) PHASE 2 execution
section entry receives an `ADVERSARY:` clause naming inertia as what the phase
defeats (C-42 candidate -- extends adversary framing from output-template-only
into the execution phase body). All other structure identical to R12 V-01.

**Hypothesis:** C-41 adds a PHASE 3 OUTPUT DECLARATION in execution-prose form
carrying INVARIANT:/OUTPUT FORM: sub-component labels and a Trigger: sentence
within the INVARIANT sub-component, parallel to PHASE 2's output declaration
from C-38/C-39/C-40. C-42 adds a single ADVERSARY: line at PHASE 2 execution
entry, making adversary framing present at two structurally distinct sites: the
output template (COMMIT DECISION) and the execution phase body. Under v12,
V-01 scores 255 (C-41 and C-42 are not yet criteria). The V-01 vs V-02 delta
isolates C-41; the V-01 vs V-03 delta isolates C-42. The delta between V-02
and V-03 should be 0 under v12 (both 255) -- confirming C-41 and C-42 are
independently observable, not implied by each other.

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

## V-02: Single-axis -- C-41 withheld (isolation test)

**Axis:** C-41 deliberately withheld. PHASE 2 execution section carries the
adversary clause at entry (`ADVERSARY:` line -- C-42 PASS) but PHASE 3 has
no OUTPUT DECLARATION. PHASE 3 remains as undifferentiated execution prose:
consistency guard condition stated, readiness thresholds listed, no labeled
sub-component structure. The `INVARIANT:` and `OUTPUT FORM:` labels and the
`Trigger:` sentence that V-01 adds to PHASE 3 are absent. All other structure
identical to V-01.

**Hypothesis:** If C-41 requires an OUTPUT DECLARATION block within the PHASE 3
execution body -- carrying `INVARIANT:` and `OUTPUT FORM:` labeled sub-components
with trigger characterization, parallel to PHASE 2's output declaration -- then
removing that structure while retaining adversary framing at PHASE 2 entry
should fail C-41 while leaving C-42 intact. Under v12, both V-01 and V-02 score
255 (C-41 is not yet a criterion). The observable structural gap: V-01's PHASE 3
body has a labeled, triggered output declaration; V-02's PHASE 3 body ends at the
readiness threshold line with no output declaration. If a v13 rubric extracts
C-41, V-02 scores 5 points below V-01. Confirms that the PHASE 2 output
declaration pattern (C-38/C-39/C-40) does not propagate to PHASE 3 automatically:
C-41 is independently necessary as a second-phase mechanism.

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

## V-03: Single-axis -- C-42 withheld (isolation test)

**Axis:** C-42 deliberately withheld. PHASE 3 execution body receives the
OUTPUT DECLARATION with `INVARIANT:` and `OUTPUT FORM:` labeled sub-components
and `Trigger:` sentence (C-41 PASS). PHASE 2 execution section carries no
adversary clause at its entry -- PHASE 2 begins directly with the strategy.md
read, identical in opening structure to R12 V-01's PHASE 2. The `ADVERSARY:`
line that V-01 prepends to PHASE 2 is absent. All other structure identical
to V-01.

**Hypothesis:** If C-42 requires an explicit adversary clause within the PHASE 2
execution body -- making the adversary framing present at the execution phase
site as well as the output template site -- then removing that clause while
retaining the PHASE 3 output declaration should fail C-42 while leaving C-41
intact. Under v12, both V-01 and V-03 score 255. The observable structural gap:
V-01's PHASE 2 execution body opens with `ADVERSARY:...`; V-03's PHASE 2 opens
with `Read simulations/strategy.md.` If a v13 rubric extracts C-42, V-03 scores
5 points below V-01. The delta between V-02 (C-41 withheld, C-42 present) and
V-03 (C-41 present, C-42 withheld) should be 0 under v12, confirming orthogonality.
Under v13, if both C-41 and C-42 are extracted, V-02 and V-03 each score
(255 + 5 for the criterion they satisfy) - (5 for the one they withhold).

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
    INVARIANT: Dual-axis gate -- file-absent and topic-absent exits are
      structurally distinct stop conditions with distinct messages.
      Trigger: file-absent fires when strategy.md does not exist on disk;
      topic-absent fires when strategy.md present but {topic} has no registered
      planned signals.
    OUTPUT FORM: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.

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

## V-04: Combination -- Lifecycle GUARD contract form with C-41+C-42

**Axes:** Lifecycle emphasis (phase contract blocks with INPUT / GUARD / OUTPUT
fields) + C-42 via an `ADVERSARY:` clause in PHASE 2's execution body below
the contract box + C-41 via a `PHASE 3 OUTPUT DECLARATION:` block in
execution-prose form appended to PHASE 3's execution body after the readiness
thresholds. Tests whether C-41 and C-42 are form-agnostic across
execution-prose (V-01) and lifecycle contract (V-04) entry formats. The
ADVERSARY clause appears in the execution prose below the PHASE 2 box (not
inside the box header), and the PHASE 3 OUTPUT DECLARATION appears after
PHASE 3's readiness thresholds (not inside the PHASE 3 box OUTPUT field).

**Hypothesis:** C-37 was confirmed form-agnostic in R11 (GUARD-contract-field
and execution-prose both satisfy). C-38 was confirmed form-agnostic in R11
(inline-appended label and elevated titled box both satisfy). By the same
logic, C-41 and C-42 should be form-agnostic: the `ADVERSARY:` line in PHASE 2
execution prose satisfies C-42 whether the surrounding phase structure is
execution-prose (V-01) or lifecycle contract (V-04). The `PHASE 3 OUTPUT
DECLARATION:` block satisfies C-41 whether PHASE 3 uses prose header (V-01)
or lifecycle contract box (V-04). If V-04 and V-01 both reach the same score
under v13, C-41 and C-42 form-agnosticism is confirmed. If only V-01 reaches
the maximum, the lifecycle contract form has a disqualifying structural
interaction with C-41 or C-42.

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
  ADVERSARY: inertia toward evidence-blind commits -- default when this phase
  is skipped: each unverified signal ships without explicit assertion.
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

## V-05: Combination -- Lifecycle GUARD + elevated titled blocks for adversary and PHASE 3 output

**Axes:** Lifecycle emphasis + C-42 elevated to a titled adversary block within
PHASE 2's execution body + C-41 elevated to a titled OUTPUT DECLARATION block
within PHASE 3's execution body. Both new structural properties are presented
as formally demarcated `+-- ... --+` titled boxes rather than inline prose
additions. Extends the titled-block pattern established for PHASE 2 OUTPUT
DECLARATION in R12 V-05 to two new structures: PHASE 3 OUTPUT DECLARATION
(C-41 titled form) and PHASE 2 ADVERSARY DECLARATION (C-42 titled form).
A scorer reading either block in isolation can identify its structural property
without consulting any other section.

**Hypothesis:** C-38's elevated titled-block form (R11/R12 V-05) made
execution-body residency independently verifiable. V-05 extends that: the
`+-- PHASE 2 ADVERSARY DECLARATION --+` block makes adversary framing at the
execution-phase site independently verifiable (scorer reads block, confirms
adversary is named in the execution body, not only in the output template).
The `+-- PHASE 3 OUTPUT DECLARATION --+` block makes PHASE 3 output structure
independently verifiable (scorer reads block, confirms INVARIANT: label,
Trigger: sentence, OUTPUT FORM: label are all present at PHASE 3 site). If
V-05 and V-01 score identically under v13, the titled-block form and the
inline-prose form are both sufficient for C-41 and C-42. If only V-05
satisfies C-42 (adversary in titled block but not in plain `ADVERSARY:` line),
C-42 requires block demarcation -- an additional constraint that V-01's
plain-line form would need to be re-examined against.

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

  +-- PHASE 2 ADVERSARY DECLARATION ------------------------------------------+
  | ADVERSARY: inertia toward evidence-blind commits                            |
  | Trigger: fires as default when PER-SIGNAL COMMITMENT ASSERTION is skipped   |
  | Outcome if undefeated: unverified signals ship without explicit assertion    |
  +---------------------------------------------------------------------------+

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

| ID | Axis | C-41 | C-42 | v12 Score |
|----|------|------|------|-----------|
| V-01 | Min delta: C-41+C-42 in execution-prose form | PASS | PASS | 255/255 |
| V-02 | C-41 withheld -- adversary at PHASE 2 entry, no PHASE 3 output declaration | FAIL | PASS | 255/255 |
| V-03 | C-42 withheld -- PHASE 3 output declaration, no adversary at PHASE 2 entry | PASS | FAIL | 255/255 |
| V-04 | Lifecycle GUARD contract form with C-41+C-42 in execution-body prose | PASS | PASS | 255/255 |
| V-05 | Lifecycle + elevated titled blocks for PHASE 2 adversary and PHASE 3 output declaration | PASS | PASS | 255/255 |

All five variants score 255/255 under v12. C-41 and C-42 are not yet criteria --
they are observable patterns in R13's excellence signals.

**C-41 isolation test (V-01 vs V-02):** V-02 retains all C-37/C-38/C-39/C-40
structure and adds adversary framing at PHASE 2 entry (C-42 PASS) but withholds
the PHASE 3 OUTPUT DECLARATION. The observable gap: V-01's PHASE 3 body closes
with a labeled, trigger-characterized output declaration; V-02's PHASE 3 body
ends at the `Readiness: >=80% READY | ...` line with no further structure. If a
v13 rubric extracts C-41, V-02 scores 5 points below V-01. Confirms that the
PHASE 2 output declaration pattern (C-38/C-39/C-40) does not propagate to PHASE 3
automatically: C-41 is independently necessary as a second-phase mechanism.

**C-42 isolation test (V-01 vs V-03):** V-03 retains all C-37/C-38/C-39/C-40
structure and adds the PHASE 3 OUTPUT DECLARATION (C-41 PASS) but withholds the
adversary clause at PHASE 2 entry. The observable gap: V-01's PHASE 2 execution
body opens with `ADVERSARY: inertia toward evidence-blind commits...`; V-03's
PHASE 2 opens with `Read simulations/strategy.md.` If a v13 rubric extracts C-42,
V-03 scores 5 points below V-01. Confirms that adversary framing in the output
template (COMMIT DECISION, C-16) does not imply adversary framing at the
execution-phase-body site: C-42 is independently necessary as a second-site
mechanism.

**Orthogonality test (V-02 vs V-03):** Both score 255/255 under v12. V-02 has
C-42 without C-41; V-03 has C-41 without C-42. Under v12 they are
indistinguishable. Under v13, if both C-41 and C-42 are extracted, V-02 and V-03
each trade: the criterion they satisfy offsets the one they withhold, confirming
the two criteria are orthogonal and independently necessary.

**Form-agnosticism tests (V-01 vs V-04 vs V-05):** V-01 uses execution-prose for
both new properties; V-04 uses lifecycle contract form with prose-appended output
declarations; V-05 uses elevated titled blocks for both the adversary declaration
and the PHASE 3 output declaration. If all three score identically under v13,
C-41 and C-42 are form-agnostic across prose, lifecycle-contract, and titled-block
presentation styles -- consistent with R11's confirmation that C-37 and C-38 are
form-agnostic.
