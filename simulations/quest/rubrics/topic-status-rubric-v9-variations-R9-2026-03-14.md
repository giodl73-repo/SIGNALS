
# Variations: `topic:status` -- Round 9
**Rubric:** v9 (max 225) | **Date:** 2026-03-14

---

## Design Context

R8 differentiating evidence: V-04 scored 220/225 against v9; V-05 scored 220/225 against v9.
Three Tier 8 criteria were extracted from R8 excellence signals:

- **C-32**: Named-exit labeling -- each exit branch carries a distinct declared name at the
  branch declaration site. R8 V-04 satisfied C-32 (Exit A / Exit B labels in PHASE 2 prose).
  R8 V-05 failed (numbered GUARD entries `(1)` / `(2)` in contract block).
- **C-33**: Preamble architectural invariant declaration -- a preamble block before the guard,
  physically separate, names the structural invariant. Both R8 V-04 and V-05 satisfied C-33.
- **C-34**: Axis-enumerated invariant declaration -- the preamble enumerates both axes,
  characterizes each trigger, asserts structural distinctness with distinct messages.
  R8 V-05 satisfied C-34 (canonical `file-absent and topic-absent are structurally distinct
  stop conditions with distinct messages`). R8 V-04 failed C-34 -- its preamble used a
  multi-sentence criterion-citing description (`PHASE 2 implements dual-axis exit: ...
  (C-30)`) rather than the axis-complete canonical declaration form.

**R8 gap:** No variant achieved 225. C-32 and C-34 were not jointly satisfied by any single
variant. V-04 had C-32 (named exits in execution prose) but not C-34 (preamble cited C-30 and
spread axis description across sentences). V-05 had C-34 (canonical preamble) but not C-32
(numbered GUARD entries) and carried a transcription error (cited C-31 instead of C-30).

**R9 hypothesis:** The gap closes by combining the C-32 mechanism from V-04 (named exits:
`Exit A -- file absent:` / `Exit B -- topic not registered:`) with the C-34 mechanism from V-05
(canonical preamble declaration) in a single variant. V-01 tests this minimum delta. If V-01
reaches 225, the gap is confirmed closed. V-02 withholds C-34 (isolation) to confirm the axis
enumeration form is independently necessary beyond property naming alone.

**Predicted score map:**

| Variant | C-32 | C-33 | C-34 | Predicted |
|---------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | 225/225   |
| V-02    | PASS | PASS | FAIL | 220/225   |
| V-03    | PASS | PASS | PASS | 225/225   |
| V-04    | PASS | PASS | PASS | 225/225   |
| V-05    | PASS | PASS | PASS | 225/225   |

Axis selection: canonical C-34 preamble + named exits (V-01, minimum delta from R8 V-04);
C-34 withheld isolation test (V-02); lifecycle emphasis + named GUARD exits + C-34 preamble
(V-03, single-axis); combination C-34 + C-32 + trigger characterization + inertia framing
(V-04); lifecycle + full Tier 7/8 + multi-site + R8 V-05 transcription repair (V-05).

---

## V-01: Single-axis -- C-34 canonical preamble (minimum delta from R8 V-04)

**Axis:** Preamble form only. R8 V-04's preamble used a multi-sentence criterion-citing
description that the scorer treated as failing C-34. This variant replaces that preamble line
with the canonical axis-complete declaration: `PHASE 2 dual-axis exit: file-absent and
topic-absent are structurally distinct stop conditions with distinct messages`. All other
structure is identical to R8 V-04: Exit A / Exit B named labels (C-32), same template, same
execution prose.

**Hypothesis:** The minimum delta from R8 V-04 is the single preamble line. If C-34 scores on
whether the preamble uses the canonical single-declaration axis-enumerated form (vs. a
multi-sentence criterion-citing description), replacing that line should move V-04 from 220 to
225. C-32 remains PASS (Exit A / Exit B labels unchanged). The delta between V-01 (225
predicted) and V-02 (220 predicted) isolates whether canonical axis enumeration is independently
necessary beyond naming the structural property.

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
stop conditions with distinct messages.
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

## V-02: Single-axis -- C-34 withheld (isolation test)

**Axis:** C-34 deliberately withheld. Preamble is present and names the structural property
(C-33 PASS) but uses a generic property-naming form without axis enumeration. Named exits are
retained (C-32 PASS). All other structure identical to V-01.

**Hypothesis:** If C-34 requires the canonical axis-enumerated form, this variant should score
220/225 -- passing C-32 (named exits) and C-33 (preamble present, structural property named)
but failing C-34 (preamble says "PHASE 2 implements the dual-axis exit as an architectural
invariant" -- property named, but no axis names, no trigger characterization, no distinctness
assertion). The expected delta between V-01 (225) and V-02 (220) confirms that C-33 and C-34
are independently necessary: naming the structural property satisfies C-33; enumerating both
axes in canonical form additionally satisfies C-34.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Vocabulary coherence invariant ---------------------------------------------
All execution phase names use consequence vocabulary (C-21).
All [LAYER N] enforcement labels use the vocabulary of the phase they govern (C-24).
[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form -- not only the
stake noun phrase -- because PER-SIGNAL is the scope quantifier at left-edge
position in the phase name (C-26, C-27).
PHASE 2 implements the dual-axis exit as an architectural invariant.
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

## V-03: Single-axis -- Lifecycle emphasis (named GUARD exits + C-34 preamble)

**Axis:** Lifecycle emphasis only. Phase contract blocks (INPUT / GUARD / OUTPUT) from the R8
V-03/V-05 structure. Delta from R8 V-03: (1) GUARD entries use named-exit format
`Exit A -- file absent ->` / `Exit B -- topic not registered ->` instead of numbered
`(1)` / `(2)`, satisfying C-32 within the contract block; (2) preamble uses the canonical C-34
axis-enumerated form. No inertia framing added (COMMIT DECISION remains threshold-only).

**Hypothesis:** The lifecycle phase contract structure is the highest-auditability path to C-32:
named exits appear inside labeled GUARD fields, so a scorer can identify each exit by name AND
by its GUARD-field position simultaneously. C-34 is satisfied by the preamble's canonical
declaration preceding the phase block. Predicts 225 via the lifecycle-emphasis structural path,
confirming the C-32 mechanism is form-agnostic -- named labels satisfy C-32 whether they appear
in inline execution prose (V-01) or inside GUARD contract fields (V-03).

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
stop conditions with distinct messages.
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
  Readiness: READY | PARTIAL | NOT READY
  Committing now means shipping without: {list of UNVERIFIED signals}

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
| GUARD:  Exit A -- file absent ->                                            |
|             output "No planned baseline -- commit exposure is               |
|             unquantifiable." and stop                                       |
|         Exit B -- topic not registered ->                                   |
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

## V-04: Combination -- C-34 + C-32 + explicit trigger characterization + inertia framing

**Axes:** Canonical C-34 preamble with explicit trigger characterization (C-34) + named exits
(C-32) + PRIMARY ADVERSARY inertia framing (C-16 deepening) + preamble extends canonical
declaration with named trigger conditions for each axis.

**Hypothesis:** V-04 tests whether the C-34 canonical form is satisfied when the preamble
provides the required single-declaration axis enumeration AND additionally characterizes each
trigger condition in supplementary sentences. C-34 requires: (1) both axes named, (2) each
trigger characterized, (3) structural distinctness asserted, (4) distinct messages asserted.
V-01's preamble satisfies all four in a single sentence. V-04's preamble satisfies all four in
the same sentence PLUS provides explicit trigger characterization in follow-on sentences.
If V-04 and V-01 both score 225, supplementary trigger characterization is compatible with
C-34 (the canonical sentence is sufficient; extra sentences do not confound). If V-04 scores
higher than V-01 in future rubric rounds, trigger characterization is an embryonic Tier 9
criterion.

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

## V-05: Combination -- Lifecycle + C-34 + named GUARD exits + multi-site + R8 transcription repair

**Axes:** Lifecycle emphasis + canonical C-34 preamble + named exits inside GUARD contract
entries (C-32) + multi-site declaration (PHASE 2 OUTPUT block echoes axis enumeration) +
corrects R8 V-05 transcription error (dual-axis rule cited as C-31 instead of C-30 in preamble).

**Hypothesis:** R8 V-05 scored 220 -- C-34 PASS, C-33 PASS, C-32 FAIL (numbered GUARD entries),
plus transcription error. V-05 repairs both: (1) replaces numbered `(1)` / `(2)` GUARD entries
with `Exit A -- file absent ->` / `Exit B -- topic not registered ->` named exits; (2) removes
the erroneous C-31 citation from the preamble's dual-axis line. Additionally, the PHASE 2 OUTPUT
block echoes the axis-enumeration claim ("file-absent and topic-absent exits are structurally
distinct with distinct messages"), creating a multi-site declaration -- the invariant is asserted
in the preamble (C-33/C-34), in the GUARD entries by name (C-32), and in the OUTPUT declaration.
This is the R8 V-05 repair variant: maximum auditability path to 225 via the lifecycle structure.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Vocabulary coherence invariant ---------------------------------------------
All execution phase names use consequence vocabulary (C-21).
[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form (C-26, C-27).
PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct
stop conditions with distinct messages. Each register row carries a
per-signal shipping consequence annotation (C-31). Stale evidence annotation
names the impaired execution phase (C-29).
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
| GUARD:  Exit A -- file absent ->                                            |
|             output "No planned baseline -- commit exposure is               |
|             unquantifiable." and stop                                       |
|         Exit B -- topic not registered ->                                   |
|             output "topic not registered: no planned signals for {topic}"   |
|             and stop before PHASE 3 (EXPOSURE COMPUTATION)                 |
| OUTPUT: VERIFIED | UNVERIFIED per planned signal;                           |
|         if UNVERIFIED: ships without this signal on commit;                 |
|         if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired       |
|         evidence; file-absent and topic-absent exits are structurally       |
|         distinct with distinct messages; no batch evaluation                |
+---------------------------------------------------------------------------+
  Read simulations/strategy.md. Apply GUARD exits in order.
  Extract planned signals for {topic}.
  For each planned signal P:
    If P matches a file in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Assert each signal individually.

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

| ID | Axis | C-32 | C-33 | C-34 | Score |
|----|------|------|------|------|-------|
| V-01 | C-34 canonical preamble -- minimum delta from R8 V-04 | PASS | PASS | PASS | 225/225 |
| V-02 | C-34 withheld -- isolation test, generic preamble | PASS | PASS | FAIL | 220/225 |
| V-03 | Lifecycle emphasis -- named GUARD exits + C-34 preamble | PASS | PASS | PASS | 225/225 |
| V-04 | C-34 + C-32 + trigger characterization + inertia framing | PASS | PASS | PASS | 225/225 |
| V-05 | Lifecycle + C-34 + named GUARD exits + multi-site + transcription repair | PASS | PASS | PASS | 225/225 |

**C-34 isolation test (V-01 vs V-02):** V-02 uses `PHASE 2 implements the dual-axis exit as an
architectural invariant` -- property named, C-33 PASS; no axis enumeration, C-34 FAIL. Expected
delta is exactly 5 points (C-34 weight). If the delta is 5, the axis-complete form is
independently necessary. If the delta is 0, C-33 and C-34 are not distinguishable by the scorer
and C-34 scoring is degenerate.

**C-32 form-agnosticism (V-01 vs V-03):** Both V-01 (inline prose) and V-03 (GUARD contract
entries) use named exits. If both score 225, C-32 is form-agnostic -- the declaration site is
the branch label, regardless of surrounding structure. If V-03 uniquely achieves C-32 (and V-01
fails), C-32 requires the exit name to appear in a labeled field (GUARD), not in prose.

**V-04 trigger-characterization check:** V-04's preamble adds explicit per-axis trigger
sentences after the canonical declaration. If V-04 scores 225, supplementary characterization
is compatible with C-34. If a Tier 9 criterion emerges from V-04's supplementary
characterization in future rounds, C-34 will be extended from axis-enumeration-present to
trigger-sentence-per-axis.

**V-05 transcription repair:** R8 V-05 preamble cited dual-axis exit as "(C-31)" -- an error.
V-05 removes the erroneous criterion citation entirely from the dual-axis declaration line,
keeping the axis-enumerated form clean. Multi-site OUTPUT block echo is not scored by any
current criterion (implied by C-31 + C-33 conjunction) but makes the invariant visible at three
structural sites simultaneously for the scorer.
