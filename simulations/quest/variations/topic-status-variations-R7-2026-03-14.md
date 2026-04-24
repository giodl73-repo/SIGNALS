---

# Variations: `topic:status` — Round 7
**Rubric:** v7 (max 195) | **Date:** 2026-03-14

---

## Design Premise

R6's differentiating tier was C-23 — V-02/V-05 passed by having `PER-SIGNAL COMMITMENT ASSERTION` with granularity as an integral left-edge token, not a parenthetical. The v7 rubric extracts three finer structural properties from that evidence:

| Criterion | What it tests |
|-----------|---------------|
| **C-26** | Is `PER-SIGNAL` the leftmost token? (not infix, not trailing) |
| **C-27** | Does the full C-23 form — including `PER-SIGNAL` — propagate into `[LAYER 2]`? |
| **C-28** | Does the field annotation name the specific impaired phase, not a generic epistemic consequence? |

---

## V-01 — Single-axis: Role sequence (discovery-first)

**Axis:** SIGNAL ACQUISITION runs completely before `strategy.md` is loaded.

**Hypothesis:** Deferring plan load until Phase 2 prevents the planned-signal list from anchoring discovery; the model enumerates ground truth, then judges gaps.

**Tier 6 targeting:** C-28 only — annotation reads `if absent: COMMITMENT ASSERTION cannot execute` (names the C-21 phase). C-23 not targeted; granularity stays parenthetical → C-26 and C-27 fail.

**Predicted:** 180/195 (fails C-23 → C-26 → C-27; passes C-28)

```
Topic: $ARGUMENTS
DISPLAY ONLY. Write no files.

== OUTPUT TEMPLATE ===========================================================

[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]
COMMIT RISK REGISTER -- {topic}

  strategy.md: [FOUND | NOT FOUND -- if absent: COMMITMENT ASSERTION cannot execute]

  | # | Namespace | Signal   | Status                | Date   |
  |---|-----------|----------|-----------------------|--------|
  | 1 | {ns}      | {signal} | VERIFIED | UNVERIFIED  | {date} |

[LAYER 2 -- SEMANTIC: COMMITMENT ASSERTION gate]
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
  {signal}: {date} ({N} days old)
  None if all current.

HIGHEST PRIORITY RISK
  /{namespace}:{signal} {topic}

[LAYER 3 -- EXECUTION: DISPLAY GATE render order:
  COMMIT RISK REGISTER -> COMMIT RISK BY NAMESPACE -> EXPOSURE SUMMARY
  -> COMMIT DECISION -> STALE EVIDENCE -> HIGHEST PRIORITY RISK]

== EXECUTION PHASES ==========================================================

PHASE 1 -- SIGNAL ACQUISITION
  Run discovery before loading strategy.md.
  Glob: simulations/**/{topic}-*
  Assign all matches to DISK_SIGNALS.
  If DISK_SIGNALS empty: output "No signals found for {topic}" and stop.
  For each match record: path, namespace (directory segment after simulations/),
  signal name, date.

PHASE 2 -- STRATEGY LOAD
  Now read simulations/strategy.md.
  Extract planned signals for this topic.
  If absent or no entry for this topic:
    Output: "No planned baseline -- commit exposure is unquantifiable."
    Stop execution.

PHASE 3 -- COMMITMENT ASSERTION (per signal -- no batch evaluation)
  For each planned signal P:
    If P matches a file in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Evaluate each signal individually before computing any aggregate.

PHASE 4 -- EXPOSURE COMPUTATION
  percent = VERIFIED count / PLANNED count * 100
  Consistency guard: if UNVERIFIED list non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY

PHASE 5 -- DISPLAY GATE
  Pre-display invariant: COMMIT RISK REGISTER contains exactly one row
  per planned signal.
  Render in template section order.
  Write no files.
```

---

## V-02 — Single-axis: Output format (full tier 6 compliance)

**Axis:** Structured execution layers. `PER-SIGNAL COMMITMENT ASSERTION` is the phase name with granularity at left-edge; full form propagates into `[LAYER 2]`; field annotations name the phase.

**Hypothesis:** When the granularity prefix is left-edge, propagating the full compressed form into the layer label and naming the phase in field annotations satisfy C-26, C-27, and C-28 simultaneously from a single structural commitment.

**Tier 6 targeting:** All three. C-26: `PER-SIGNAL` is leftmost token. C-27: `[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]` (not truncated to stake phrase). C-28: `if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute`.

**Predicted:** 195/195

```
Topic: $ARGUMENTS
DISPLAY ONLY. Write no files.

== OUTPUT TEMPLATE ===========================================================

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

== EXECUTION PHASES ==========================================================

PHASE 1 -- SIGNAL ACQUISITION
  Glob: simulations/**/{topic}-*
  Assign to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  Record for each: path, namespace, signal name, date.

PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION
  Read simulations/strategy.md.
  Extract planned signals for this topic.
  If absent or no topic entry:
    Output: "No planned baseline -- commit exposure is unquantifiable."
    Stop.
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

## V-03 — Single-axis: Lifecycle emphasis (explicit phase boundary contracts)

**Axis:** Each phase is wrapped in an explicit input contract, output contract, and guard statement. Phase boundaries are self-documenting.

**Hypothesis:** Contract blocks force explicit declaration of what each phase consumes and produces, making the assertion chain auditable at the boundary level. The guard annotation in Phase 2's contract block becomes the natural location for C-28 compliance — naming the impaired phase without requiring it to be in the phase name itself.

**Tier 6 targeting:** C-28 only (via Phase 2 GUARD line). C-23 not targeted.

**Predicted:** 180/195 (fails C-23 → C-26 → C-27; passes C-28)

```
Topic: $ARGUMENTS
DISPLAY ONLY. Write no files.

== OUTPUT TEMPLATE ===========================================================

[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]
COMMIT RISK REGISTER -- {topic}

  strategy.md: [FOUND | NOT FOUND -- if absent: COMMITMENT ASSERTION cannot execute]

  | # | Namespace | Signal   | Status                | Date   |
  |---|-----------|----------|-----------------------|--------|
  | 1 | {ns}      | {signal} | VERIFIED | UNVERIFIED  | {date} |

[LAYER 2 -- SEMANTIC: COMMITMENT ASSERTION gate]
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
  {signal}: {date} ({N} days old)
  None if all current.

HIGHEST PRIORITY RISK
  /{namespace}:{signal} {topic}

[LAYER 3 -- EXECUTION: DISPLAY GATE render order:
  COMMIT RISK REGISTER -> COMMIT RISK BY NAMESPACE -> EXPOSURE SUMMARY
  -> COMMIT DECISION -> STALE EVIDENCE -> HIGHEST PRIORITY RISK]

== EXECUTION PHASES ==========================================================

+-- PHASE 1 -- SIGNAL ACQUISITION ------------------------------------------+
| INPUT:  topic argument                                                      |
| OUTPUT: DISK_SIGNALS (path, namespace, signal name, date) | empty set       |
+---------------------------------------------------------------------------+
  Glob: simulations/**/{topic}-*
  Assign all matches to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  For each match record: path, namespace, signal name, date.

+-- PHASE 2 -- COMMITMENT ASSERTION (per signal -- no batch evaluation) ----+
| INPUT:  DISK_SIGNALS from Phase 1; strategy.md planned signals             |
| GUARD:  strategy.md must exist and have topic entry;                        |
|         if absent: COMMITMENT ASSERTION cannot execute                      |
| OUTPUT: VERIFIED | UNVERIFIED per planned signal                            |
+---------------------------------------------------------------------------+
  Read simulations/strategy.md.
  Extract planned signals for this topic.
  If absent or no topic entry: execute GUARD -- output
    "No planned baseline -- commit exposure is unquantifiable." and stop.
  For each planned signal P:
    If P in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Evaluate individually. No batch.

+-- PHASE 3 -- EXPOSURE COMPUTATION ----------------------------------------+
| INPUT:  VERIFIED/UNVERIFIED assertions from Phase 2                         |
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
  Pre-display invariant check: row count = planned count.
  Render in template section order.
  Write no files.
```

---

## V-04 — Combination: Role sequence + Output format (C-26 + C-28; C-27 isolated)

**Axes:** Discovery-first role sequence + PER-SIGNAL left-edge phase name. `[LAYER 2]` label carries stake phrase only — the full C-23 form is in the phase header but not propagated into the enforcement label.

**Hypothesis:** C-26 and C-28 can both be satisfied while C-27 is deliberately withheld. This isolates C-27 as the independently necessary propagation step — achieving left-edge positioning in the phase name does not automatically satisfy the requirement that the full form appear in the layer label.

**Tier 6 targeting:** C-26 PASS (PER-SIGNAL leftmost), C-27 FAIL (label truncated to stake phrase), C-28 PASS (annotation names PER-SIGNAL COMMITMENT ASSERTION phase).

**Predicted:** 190/195

```
Topic: $ARGUMENTS
DISPLAY ONLY. Write no files.

== OUTPUT TEMPLATE ===========================================================

[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]
COMMIT RISK REGISTER -- {topic}

  strategy.md: [FOUND | NOT FOUND -- if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute]

  | # | Namespace | Signal   | Status                                                              | Date   |
  |---|-----------|----------|---------------------------------------------------------------------|--------|
  | 1 | {ns}      | {signal} | VERIFIED | UNVERIFIED -- if absent: ships without this signal on commit | {date} |

[LAYER 2 -- SEMANTIC: COMMITMENT ASSERTION gate]
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
  {signal}: {date} ({N} days old -- if stale: EXPOSURE COMPUTATION may rest on expired evidence)
  None if all current.

HIGHEST PRIORITY RISK
  /{namespace}:{signal} {topic}

[LAYER 3 -- EXECUTION: DISPLAY GATE render order:
  COMMIT RISK REGISTER -> COMMIT RISK BY NAMESPACE -> EXPOSURE SUMMARY
  -> COMMIT DECISION -> STALE EVIDENCE -> HIGHEST PRIORITY RISK]

== EXECUTION PHASES ==========================================================

PHASE 1 -- SIGNAL ACQUISITION
  Run discovery before loading strategy.md.
  Glob: simulations/**/{topic}-*
  Assign to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  For each match: path, namespace, signal name, date.

PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION
  Now read simulations/strategy.md.
  Extract planned signals for this topic.
  If absent or no topic entry:
    Output: "No planned baseline -- commit exposure is unquantifiable."
    Stop.
  For each planned signal P:
    If P in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Assert each individually. No batch.

PHASE 3 -- EXPOSURE COMPUTATION
  percent = VERIFIED / PLANNED * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY

PHASE 4 -- DISPLAY GATE
  Pre-display invariant: one row per planned signal.
  Render in template section order.
  Write no files.
```

---

## V-05 — Combination: Lifecycle emphasis + Inertia framing (full tier 6 + adversary naming)

**Axes:** Explicit phase boundary contracts + Inertia framing — the primary competitor (`commit without evidence`) is named in COMMIT DECISION as the default outcome when status is not checked. Plus explicit vocabulary coherence invariant block (from R6 V-03/V-05 excellence pattern).

**Hypothesis:** Naming the status-quo adversary makes the readiness verdict a comparative judgment rather than a coverage threshold — "you are choosing between this evidence state and committing blind." Combined with full tier 6 compliance and the vocabulary coherence invariant declared as an architectural rule, this produces the highest structural depth.

**Tier 6 targeting:** All three. Identical tier 6 structure to V-02; additional depth via inertia framing and invariant block.

**Predicted:** 195/195

```
Topic: $ARGUMENTS
DISPLAY ONLY. Write no files.

-- Vocabulary coherence invariant -------------------------------------------
All execution phase names use consequence vocabulary (C-21).
All [LAYER N] enforcement labels use the vocabulary of the phase they govern.
[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form -- not only
the stake noun phrase -- because PER-SIGNAL is the scope quantifier at
left-edge position, not a trailing modifier.
----------------------------------------------------------------------------

== OUTPUT TEMPLATE ===========================================================

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

== EXECUTION PHASES ==========================================================

+-- PHASE 1 -- SIGNAL ACQUISITION ------------------------------------------+
| INPUT:  topic argument                                                      |
| OUTPUT: DISK_SIGNALS (path, namespace, signal name, date) | empty set       |
+---------------------------------------------------------------------------+
  Glob: simulations/**/{topic}-*
  Assign to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  Record per match: path, namespace, signal name, date.

+-- PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION ------------------------------+
| INPUT:  DISK_SIGNALS; strategy.md planned signals                          |
| GUARD:  strategy.md must exist and have topic entry;                        |
|         if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute           |
| OUTPUT: VERIFIED | UNVERIFIED per planned signal; no batch evaluation       |
+---------------------------------------------------------------------------+
  Read simulations/strategy.md.
  Extract planned signals for this topic.
  If absent or no topic entry: execute GUARD -- output
    "No planned baseline -- commit exposure is unquantifiable." and stop.
  For each planned signal P:
    If P in DISK_SIGNALS: VERIFIED
    Else: UNVERIFIED
  Assert each individually.

+-- PHASE 3 -- EXPOSURE COMPUTATION ----------------------------------------+
| INPUT:  VERIFIED/UNVERIFIED from Phase 2                                    |
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

| ID | Axis | C-26 | C-27 | C-28 | Score |
|----|------|------|------|------|-------|
| V-01 | Role sequence | FAIL | FAIL | PASS | 180/195 |
| V-02 | Output format | PASS | PASS | PASS | 195/195 |
| V-03 | Lifecycle emphasis | FAIL | FAIL | PASS | 180/195 |
| V-04 | Role seq + Output format | PASS | FAIL | PASS | 190/195 |
| V-05 | Lifecycle + Inertia | PASS | PASS | PASS | 195/195 |

**C-27 isolation (V-04 vs V-02):** V-04 has `PER-SIGNAL COMMITMENT ASSERTION` as the phase name (C-26 satisfied) but `[LAYER 2 -- SEMANTIC: COMMITMENT ASSERTION gate]` as the enforcement label (C-27 withheld). The 5-point gap between V-04 and V-02 confirms that left-edge positioning in the phase name does not imply propagation into the layer label — they are structurally independent.

**C-28 universality:** All five variants pass C-28. V-01/V-03 via `COMMITMENT ASSERTION cannot execute`; V-02/V-04/V-05 via `PER-SIGNAL COMMITMENT ASSERTION cannot execute`. C-28 requires any C-21 phase name in the annotation — it is independent of the C-23 → C-26 → C-27 chain.

**File written:** `simulations/quest/rubrics/topic-status-rubric-v7-variations-R7-2026-03-14.md`
