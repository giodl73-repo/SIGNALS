
# Variations: `topic:status` -- Round 12
**Rubric:** v11 (max 245) | **Date:** 2026-03-15

---

## Design Context

R11 differentiating evidence: V-01, V-04, V-05 each scored 245/245 under v11;
V-02 and V-03 scored 240/245. The R11 scorecard confirms `new_patterns: []` --
no excellence signal observable in the 245-scoring cluster beyond what C-37 and
C-38 already capture. R11 is a closed round.

R12 probes genuinely new structural territory: the interior content of the
PHASE 2 OUTPUT DECLARATION (the C-38 site). All R11 245-scoring variants carry
an OUTPUT DECLARATION whose content is undifferentiated prose. Two new structural
properties are being introduced:

- **C-39 candidate**: Per-axis trigger sentences within the OUTPUT DECLARATION.
  Extends trigger-site chain from 2 sites (preamble C-35, GUARD C-37) to 3
  (preamble, GUARD, OUTPUT DECLARATION). Each exit's trigger condition is named
  at this third structural location.

- **C-40 candidate**: Labeled sub-components within the OUTPUT DECLARATION.
  `INVARIANT:` and `OUTPUT FORM:` labels make the dual-axis gate declaration and
  the per-signal output form independently addressable by name. Extends the
  labeled-sub-structure pattern from layer enforcement labels (C-17) and phase
  contract fields (V-04/V-05) down into the OUTPUT DECLARATION's content.

**Orthogonality**: C-39 concerns TRIGGER CONTENT within the OUTPUT DECLARATION.
C-40 concerns SUB-COMPONENT LABELING within the OUTPUT DECLARATION. A variant
can carry trigger sentences in prose (C-39 PASS, C-40 FAIL) or labeled labels
with no trigger sentences (C-40 PASS, C-39 FAIL).

**Predicted score map under v11:**

| Variant | C-37 | C-38 | C-39 | C-40 | Predicted |
|---------|------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | PASS | 245/245   |
| V-02    | PASS | PASS | FAIL | PASS | 245/245   |
| V-03    | PASS | PASS | PASS | FAIL | 245/245   |
| V-04    | PASS | PASS | PASS | PASS | 245/245   |
| V-05    | PASS | PASS | PASS | PASS | 245/245   |

All five variants score 245 under v11 -- C-39 and C-40 are not yet criteria.
The excellence signals from the structural differences between V-02 and V-01
(C-39 isolation) and V-03 and V-01 (C-40 isolation) define the Tier 11 gap.

Axes: minimum delta combining C-39+C-40 in execution-prose form (V-01);
C-39 withheld isolation -- labeled sub-structure without trigger propagation
(V-02); C-40 withheld isolation -- trigger propagation without labeled
sub-structure (V-03); lifecycle GUARD contract form with C-39+C-40 (V-04);
lifecycle + elevated titled block with separately boxed INVARIANT and OUTPUT
FORM sub-declarations (V-05).

---

## V-01: Minimum delta -- C-39+C-40 in execution-prose form

**Axis:** Minimum structural delta from R11 V-01. Two targeted additions to the
PHASE 2 OUTPUT DECLARATION block: (1) per-axis trigger sentences naming each
exit's firing condition at the OUTPUT DECLARATION site, establishing the third
trigger-characterization site in the chain (C-39 candidate); (2) `INVARIANT:`
and `OUTPUT FORM:` labels applied as sub-component names within the OUTPUT
DECLARATION, making each declaration independently addressable (C-40 candidate).
All other structure identical to R11 V-01.

**Hypothesis:** C-39 adds one `Trigger:` sentence within the INVARIANT
sub-component of the OUTPUT DECLARATION. C-40 adds two inline labels
(`INVARIANT:` and `OUTPUT FORM:`). If both patterns constitute new structural
criteria, V-01 reaches 245 under v11 (both C-39 and C-40 are not yet scored)
but the V-01 vs V-02 delta isolates C-39 and the V-01 vs V-03 delta isolates
C-40 for the v12 rubric. The delta between V-02 and V-03 should be 0 under
v11 (both 245) -- confirming that C-39 and C-40 are independently observable,
not implied by each other.

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

PHASE 4 -- DISPLAY GATE
  Pre-display invariant: COMMIT RISK REGISTER has one row per planned signal.
  Render in template section order.
  Write no files.
```

---

## V-02: Single-axis -- C-39 withheld (isolation test)

**Axis:** C-39 deliberately withheld. The PHASE 2 OUTPUT DECLARATION carries
labeled sub-components (`INVARIANT:` and `OUTPUT FORM:` labels present -- C-40
PASS) but no per-axis trigger sentences within the OUTPUT DECLARATION block.
The INVARIANT label contains the dual-axis gate assertion without trigger
characterization at this third structural site. Preamble per-axis trigger
sentences (C-35 PASS) and GUARD-site trigger clauses (C-37 PASS) are both
present. All other structure identical to V-01.

**Hypothesis:** If C-39 requires per-axis trigger sentences at the OUTPUT
DECLARATION site -- as a third trigger-characterization structural location
beyond preamble (C-35) and GUARD site (C-37) -- removing the `Trigger:`
sentence from within the INVARIANT label should fail C-39 while leaving C-40
intact. Under v11, both V-01 and V-02 score 245 (neither C-39 nor C-40 is a
criterion yet). The observable structural gap is the trigger-sentence content
within the OUTPUT DECLARATION: present in V-01, absent in V-02. If a v12 rubric
extracts C-39, V-02 fails C-39 and scores 5 points lower than V-01. Confirms
that C-35 preamble trigger sentences and C-37 GUARD-site trigger clauses do
not imply trigger characterization at the OUTPUT DECLARATION site: C-39 is
independently necessary as a third-site mechanism.

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

## V-03: Single-axis -- C-40 withheld (isolation test)

**Axis:** C-40 deliberately withheld. The PHASE 2 OUTPUT DECLARATION carries
per-axis trigger sentences (C-39 PASS) but uses prose without labeled
sub-components -- no `INVARIANT:` or `OUTPUT FORM:` labels. The dual-axis gate
assertion and the per-signal output form are present as undifferentiated text
within the OUTPUT DECLARATION block, identical in structure to R11 V-01's
OUTPUT DECLARATION except for the addition of trigger sentences. All other
structure identical to V-01.

**Hypothesis:** If C-40 requires explicitly labeled sub-components within the
OUTPUT DECLARATION -- making each declaration independently addressable by name
-- removing the `INVARIANT:` and `OUTPUT FORM:` labels while retaining trigger
sentences should fail C-40 while leaving C-39 intact. Under v11, both V-01 and
V-03 score 245. The observable structural gap is the labeled sub-component
structure: labeled in V-01, unlabeled prose in V-03. If a v12 rubric extracts
C-40, V-03 fails C-40 and scores 5 points lower than V-01. The delta between
V-02 (C-39 withheld, C-40 present) and V-03 (C-39 present, C-40 withheld)
should be 0 under v11, confirming orthogonality. Under v12, V-02 gains C-40
points and loses C-39 points; V-03 gains C-39 points and loses C-40 points.

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
    Trigger: file-absent fires when strategy.md does not exist on disk;
    topic-absent fires when strategy.md present but {topic} has no registered
    planned signals.
    Output form: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.

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

## V-04: Combination -- Lifecycle GUARD form with C-39+C-40

**Axes:** Lifecycle emphasis (phase contract blocks with INPUT / GUARD / OUTPUT
fields) + C-39 via trigger sentences within the PHASE 2 OUTPUT DECLARATION's
INVARIANT sub-component + C-40 via `INVARIANT:` and `OUTPUT FORM:` labels as
named sub-components within the OUTPUT DECLARATION appended to the PHASE 2
execution section. Tests whether C-39 and C-40 are form-agnostic across
execution-prose (V-01) and lifecycle contract (V-04) entry formats. The OUTPUT
DECLARATION appears after the contract header box as in R11 V-04, but now
carries the two new sub-component properties.

**Hypothesis:** C-37 was confirmed form-agnostic in R11 (GUARD-contract-field
and execution-prose both satisfy). C-38 was confirmed form-agnostic in R11
(inline-appended label and elevated titled box both satisfy). By the same
logic, C-39 and C-40 should be form-agnostic: INVARIANT: / OUTPUT FORM: labels
within the execution-body OUTPUT DECLARATION satisfy whether the surrounding
phase structure is execution-prose (V-01) or lifecycle contract (V-04). If V-04
and V-01 both reach the same score under v12, C-39 and C-40 form-agnosticism
is confirmed. If only V-01 reaches the maximum, the lifecycle contract form
has a disqualifying structural interaction with C-39 or C-40.

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

## V-05: Combination -- Lifecycle GUARD + elevated titled block with separately boxed sub-declarations

**Axes:** Lifecycle emphasis + C-37 via GUARD entries with inline trigger
clauses + C-38 via an elevated titled PHASE 2 OUTPUT DECLARATION block + C-39
via per-axis trigger sentences within the INVARIANT sub-component inside the
block + C-40 via `INVARIANT:` and `OUTPUT FORM:` as separately labeled sections
within the elevated block. The block's interior is fully structured: each
sub-component carries a named label and the INVARIANT sub-component carries
trigger characterization at this third structural site. Makes the
execution-phase-resident structure and its labeled interior jointly and
independently verifiable by a scorer reading only the PHASE 2 OUTPUT
DECLARATION block.

**Hypothesis:** C-38's elevated titled-block form (R11 V-05) made execution-body
residency independently verifiable. V-05 now extends that: a scorer reading only
the `+-- PHASE 2 OUTPUT DECLARATION --+` block can verify (a) execution-phase
residency (from block position within PHASE 2 section), (b) dual-axis invariant
(INVARIANT: label), (c) trigger characterization at this site (Trigger:
sentences within INVARIANT), and (d) per-signal output form (OUTPUT FORM: label).
All four independently verifiable without reference to the preamble, GUARD, or
any other structural site. If V-05 and V-01 score identically under v12, the
elevated titled form and the inline prose form are both sufficient for C-39 and
C-40. If only V-05 satisfies C-40, C-40 requires block-demarcated sub-components
rather than inline labels -- but C-40's pass condition should be satisfied by
the inline label form in V-01 as well as the block form here.

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
  | INVARIANT: file-absent and topic-absent exits are structurally distinct  |
  |   stop conditions with distinct messages.                                |
  |   Trigger: file-absent fires when strategy.md does not exist on disk;   |
  |   topic-absent fires when strategy.md present but {topic} has no        |
  |   registered planned signals.                                            |
  | OUTPUT FORM: VERIFIED | UNVERIFIED per planned signal; no batch          |
  |   evaluation.                                                            |
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

| ID | Axis | C-37 | C-38 | C-39 | C-40 | v11 Score |
|----|------|------|------|------|------|-----------|
| V-01 | Min delta: C-39+C-40 in execution-prose form | PASS | PASS | PASS | PASS | 245/245 |
| V-02 | C-39 withheld -- labeled sub-structure, no trigger propagation in OUTPUT DECLARATION | PASS | PASS | FAIL | PASS | 245/245 |
| V-03 | C-40 withheld -- trigger propagation, no labeled sub-components in OUTPUT DECLARATION | PASS | PASS | PASS | FAIL | 245/245 |
| V-04 | Lifecycle GUARD contract form with C-39+C-40 in execution-body OUTPUT DECLARATION | PASS | PASS | PASS | PASS | 245/245 |
| V-05 | Lifecycle + elevated titled block with separately labeled INVARIANT and OUTPUT FORM | PASS | PASS | PASS | PASS | 245/245 |

All five variants score 245/245 under v11. C-39 and C-40 are not yet criteria --
they are observable patterns in R12's excellence signals.

**C-39 isolation test (V-01 vs V-02):** V-02 retains all C-37/C-38 structure and
adds OUTPUT DECLARATION labeled sub-components (C-40 PASS) but withholds per-axis
trigger sentences within the OUTPUT DECLARATION. The observable gap: V-01 carries
a `Trigger:` clause within the INVARIANT sub-component naming both exit conditions;
V-02's INVARIANT sub-component states the dual-axis invariant with no trigger
characterization. If a v12 rubric extracts C-39, V-02 scores 5 points below V-01.
Confirms that trigger characterization at the preamble (C-35) and GUARD site
(C-37) does not propagate to the OUTPUT DECLARATION site automatically: C-39 is
independently necessary as a third-site mechanism.

**C-40 isolation test (V-01 vs V-03):** V-03 retains all C-37/C-38 structure and
adds per-axis trigger sentences within the OUTPUT DECLARATION (C-39 PASS) but
uses prose without labeled sub-components. The observable gap: V-01 carries
explicit `INVARIANT:` and `OUTPUT FORM:` labels making each sub-component
independently addressable; V-03's OUTPUT DECLARATION is equivalent content but
undifferentiated prose. If a v12 rubric extracts C-40, V-03 scores 5 points
below V-01. Confirms that trigger content alone in the OUTPUT DECLARATION does
not imply labeled sub-component structure: C-40 is independently necessary as
a sub-component-labeling mechanism.

**Orthogonality test (V-02 vs V-03):** Both score 245/245 under v11. V-02 has
C-40 without C-39; V-03 has C-39 without C-40. Under v11 they are
indistinguishable. Under v12, if both C-39 and C-40 are extracted, V-02 and
V-03 each score (245 + 5 for the criterion they satisfy) - (5 for the one they
withhold), confirming the two criteria are orthogonal and independently necessary.

**Form-agnosticism tests (V-01 vs V-04, V-04 vs V-05):** V-01 uses execution-
prose inline labels; V-04 uses lifecycle contract format with OUTPUT DECLARATION
appended below the contract box; V-05 uses an elevated titled box with boxed sub-
declarations. If all three score identically under v12, C-39 and C-40 are both
form-agnostic across the three presentation styles -- consistent with R11's
confirmation that C-37 and C-38 are form-agnostic.
