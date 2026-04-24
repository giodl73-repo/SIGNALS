
# Variations: `topic:status` — Round 8
**Rubric:** v8 (max 210) | **Date:** 2026-03-14

---

## Design Context

R7 differentiating evidence: V-02 scored 195/195 against v7. Three Tier 7 criteria were extracted from R7 excellence signals:

- **C-29**: Stale evidence annotation must name the impaired C-21 phase — `if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence` — distinct verb from C-28 (`may rest on`, not `cannot execute`)
- **C-30**: PHASE 2 must implement two distinct stop conditions: file-absent (C-12) and topic-absent-within-file (new). Topic-absent branch emits a topic-specific message and stops before PHASE 3. Combined branch (`if absent or no topic entry`) does not satisfy.
- **C-31**: Each planned-signal row in COMMIT RISK REGISTER carries an inline commit-framed annotation — `VERIFIED | UNVERIFIED -- if absent: ships without this signal on commit` — one annotation per row, not one per template.

**R7 V-02 baseline against v8:** R7 V-02 already satisfied C-29 (stale evidence annotation extended to phase attribution) and C-31 (per-row register annotation). It fails C-30: its PHASE 2 used a combined `If absent or no topic entry` guard producing a single `"No planned baseline"` message — no distinction between file-absent and topic-absent, no topic-specific stop message.

R7 V-02 against v8 rubric: **205/210** (passes C-29, passes C-31, fails C-30).

**Predicted score map:**

| Variant | C-29 | C-30 | C-31 | Predicted |
|---------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | 210/210   |
| V-02    | PASS | FAIL | PASS | 205/210   |
| V-03    | PASS | PASS | PASS | 210/210   |
| V-04    | PASS | PASS | PASS | 210/210   |
| V-05    | PASS | PASS | PASS | 210/210   |

Axis selection: C-30 sequential guard (V-01), C-30 isolation/withheld (V-02), lifecycle emphasis with dual GUARD contract (V-03); combinations: C-30 + vocabulary coherence preamble + inertia framing (V-04), lifecycle emphasis + full tier 7 + inertia (V-05).

---

## V-01: Single-axis — C-30 (sequential guard, minimum delta from R7 V-02)

**Axis:** C-30 dual-axis exit implemented as two numbered sequential stop conditions in PHASE 2. All other structure is identical to R7 V-02.

**Hypothesis:** The minimum structural delta from R7 V-02 to satisfy C-30 is replacing the combined `If absent or no topic entry` branch with two sequentially numbered guards producing distinct output messages. Guard 1 handles file-absent; Guard 2 handles topic-absent-within-file with a topic-specific message. C-29 and C-31 pass unchanged from V-02. This isolates C-30 as the single independent criterion — satisfying it should move the score from 205 to 210.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

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

PHASE 1 -- SIGNAL ACQUISITION
  Glob: simulations/**/{topic}-*
  Assign to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  Record per match: path, namespace, signal name, date.

PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION
  Read simulations/strategy.md.
  Sequential stop conditions -- evaluate in order:
    1. If strategy.md absent:
         Output: "No planned baseline -- commit exposure is unquantifiable."
         Stop.
    2. If strategy.md present but contains no entry for {topic}:
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

## V-02: Single-axis — C-30 deliberately withheld (isolation test)

**Axis:** C-30 is intentionally NOT implemented — PHASE 2 retains the combined `If absent or no topic entry` branch from R7 V-02. All other tier 7 criteria (C-29, C-31) are present.

**Hypothesis:** If C-30 scores independently from C-12, V-02 should land at 205/210 — passing C-12 (file-absent early exit) but failing C-30 (no distinct topic-absent branch, no topic-specific message). This confirms that C-12 satisfaction does not imply C-30, and that distinguishing two PHASE 2 stop axes is independently necessary. The combined branch satisfies C-12 but is structurally insufficient for C-30 regardless of its text.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

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

PHASE 1 -- SIGNAL ACQUISITION
  Glob: simulations/**/{topic}-*
  Assign to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  Record per match: path, namespace, signal name, date.

PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION
  Read simulations/strategy.md.
  If absent or no entry for {topic}:
    Output: "No planned baseline -- commit exposure is unquantifiable."
    Stop.
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

## V-03: Single-axis — Lifecycle emphasis (phase boundary contracts, dual GUARD block)

**Axis:** Lifecycle emphasis — each execution phase carries an explicit INPUT / GUARD / OUTPUT contract block. PHASE 2's GUARD block declares both stop conditions as separate numbered entries, making the C-30 dual-axis exit a structurally named invariant rather than an inline prose instruction.

**Hypothesis:** When the two PHASE 2 stop conditions appear inside a formal GUARD block with labeled entries, the distinction is structurally unambiguous — a scorer cannot interpret a two-entry GUARD as a single combined branch. Phase boundary contracts also satisfy C-11/C-12 redundantly through the OUTPUT and GUARD fields, not only through execution prose. Combined with the full tier 6 + tier 7 vocabulary (C-29/C-31 in template), predicts 210/210.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

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
| GUARD:  (1) strategy.md absent ->                                           |
|             output "No planned baseline -- commit exposure is               |
|             unquantifiable." and stop                                       |
|         (2) strategy.md present but {topic} not registered ->               |
|             output "topic not registered: no planned signals for {topic}"   |
|             and stop before PHASE 3                                         |
| OUTPUT: VERIFIED | UNVERIFIED per planned signal; no batch evaluation       |
+---------------------------------------------------------------------------+
  Read simulations/strategy.md. Apply GUARD conditions in order.
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

## V-04: Combination — C-30 + vocabulary coherence preamble + inertia framing

**Axes:** Vocabulary coherence invariant preamble (from R7 V-05) extended to declare the dual-axis C-30 exit rule as an architectural invariant. Inertia framing in COMMIT DECISION (PRIMARY ADVERSARY named).

**Hypothesis:** Declaring C-30's two-branch logic as an explicit architectural rule in the preamble — alongside the C-26/C-27 declarations — makes the dual-axis exit a structural contract, not only an execution instruction. The preamble functions as a compressed specification: any implementation diverging from a declared invariant is an error detectable before execution. Combined with inertia naming in COMMIT DECISION (consequence-deepening), this is the most explicitly specified variant. Predicts 210/210 with highest structural redundancy for C-30.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Vocabulary coherence invariant ---------------------------------------------
All execution phase names use consequence vocabulary (C-21).
All [LAYER N] enforcement labels use the vocabulary of the phase they govern (C-24).
[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form -- not only the
stake noun phrase -- because PER-SIGNAL is the scope quantifier at left-edge
position in the phase name (C-26, C-27).
PHASE 2 implements dual-axis exit: strategy.md file-absent and topic-absent-
within-file are structurally distinct stop conditions with distinct output
messages. Topic-absent produces a topic-specific message and stops before
PHASE 3 (EXPOSURE COMPUTATION). File-absent stops immediately. (C-30)
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

## V-05: Combination — Lifecycle emphasis + full tier 7 + inertia framing

**Axes:** Lifecycle phase contracts + all three Tier 7 criteria explicitly woven into the phase contract blocks: C-29 named in PHASE 2 OUTPUT declaration, C-30 as two separate GUARD entries in PHASE 2 contract, C-31 as per-row annotation in register template. Inertia adversary named in COMMIT DECISION. Vocabulary coherence preamble.

**Hypothesis:** Full Tier 7 integration into a lifecycle-emphasis structure (phase contract blocks) is the most auditable variant. Each C-30 stop condition appears as a named GUARD entry with its distinct output message. C-31's row annotation appears in both the template section and the PHASE 2 OUTPUT declaration ("if UNVERIFIED: ships without this signal on commit"). C-29's stale annotation appears in both the STALE EVIDENCE template field and the PHASE 2 OUTPUT declaration ("if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence"). This redundancy across template and contract declarations ensures the three Tier 7 criteria are visible to a scorer at multiple structural sites simultaneously. Predicts 210/210 with highest auditability.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Vocabulary coherence invariant ---------------------------------------------
All execution phase names use consequence vocabulary (C-21).
[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form (C-26, C-27).
PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct
stop conditions with distinct messages (C-30). Each register row carries a
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
| GUARD:  (1) strategy.md absent ->                                           |
|             output "No planned baseline -- commit exposure is               |
|             unquantifiable." and stop                                       |
|         (2) strategy.md present but {topic} not registered ->               |
|             output "topic not registered: no planned signals for {topic}"   |
|             and stop before PHASE 3 (EXPOSURE COMPUTATION)                 |
| OUTPUT: VERIFIED | UNVERIFIED per planned signal;                           |
|         if UNVERIFIED: ships without this signal on commit;                 |
|         if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired       |
|         evidence; no batch evaluation                                       |
+---------------------------------------------------------------------------+
  Read simulations/strategy.md. Apply GUARD conditions in order.
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

| ID | Axis | C-29 | C-30 | C-31 | Score |
|----|------|------|------|------|-------|
| V-01 | C-30 sequential guard (minimum delta) | PASS | PASS | PASS | 210/210 |
| V-02 | C-30 withheld (isolation test) | PASS | FAIL | PASS | 205/210 |
| V-03 | Lifecycle emphasis + dual GUARD contract | PASS | PASS | PASS | 210/210 |
| V-04 | C-30 + preamble invariant + inertia framing | PASS | PASS | PASS | 210/210 |
| V-05 | Lifecycle + full tier 7 + inertia | PASS | PASS | PASS | 210/210 |

**C-30 isolation test (V-02 vs V-01):** V-02 retains the R7 V-02 combined branch (`if absent or no topic entry`) and should score 205/210, confirming that C-12 and C-30 are structurally independent — file-absent early exit does not imply topic-absent early exit, and a combined branch does not satisfy either separately.

**C-29/C-31 baseline:** All five variants include the R7 V-02 stale annotation (`if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence`) and the per-row register annotation (`if absent: ships without this signal on commit`). C-29 and C-31 should pass in all five variants, isolating C-30 as the sole differentiating criterion between V-01 and V-02.

**V-04/V-05 adversary check:** PRIMARY ADVERSARY appears in COMMIT DECISION in both V-04 and V-05. This does not add a new scoreable criterion (no Tier 8 criterion targets inertia framing alone) but deepens C-16 consequence framing — the readiness verdict is comparative, not just threshold-based.
