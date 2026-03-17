
# Variations: `topic:status` — Round 7
**Rubric:** v7 (max 195) | **Date:** 2026-03-14

---

## Design Context

R6 differentiating evidence: V-02 passed C-23 (`PER-SIGNAL COMMITMENT ASSERTION`); V-01/V-03/V-04 failed (granularity as parenthetical annotation). R6 excellence signals generated three new tier 6 criteria:

- **C-26**: Granularity prefix must be LEFT-EDGE in phase name — `PER-SIGNAL COMMITMENT ASSERTION` (scope before stake) not `COMMITMENT PER-SIGNAL ASSERTION`
- **C-27**: Full C-23 form must propagate into [LAYER 2] label — `[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]` not just `COMMITMENT ASSERTION gate`
- **C-28**: Field annotation must name the impaired C-21 phase — `if absent: PER-SIGNAL COMMITMENT ASSERTION cannot execute` not `if absent: commit exposure is unquantifiable`

R6 best performers (V-02/V-05) passed C-26 by construction (PER-SIGNAL was already leftmost) but likely fail C-27 and C-28 — C-27 because the layer label probably carried only the stake phrase, C-28 because the strategy.md annotation named no phase.

**Predicted score map:**

| Variant | C-26 | C-27 | C-28 | Predicted |
|---------|------|------|------|-----------|
| V-01    | FAIL | FAIL | PASS | 180/195   |
| V-02    | PASS | PASS | PASS | 195/195   |
| V-03    | FAIL | FAIL | PASS | 180/195   |
| V-04    | PASS | FAIL | PASS | 190/195   |
| V-05    | PASS | PASS | PASS | 195/195   |

Axis selection: role sequence (V-01), output format (V-02), lifecycle emphasis (V-03); combinations: role sequence + output format (V-04), lifecycle emphasis + inertia framing (V-05).

---

## V-01: Single-axis — Role sequence (discovery-first, strategy deferred)

**Axis:** Role sequence — SIGNAL ACQUISITION executes fully before strategy.md is loaded.

**Hypothesis:** Deferring strategy.md load until Phase 2 prevents the planned-signal list from anchoring the discovery step. The model enumerates what exists on disk, then judges gaps against the plan — not the reverse. C-23 not targeted (granularity stays parenthetical). C-28 upgraded: annotation names the COMMITMENT ASSERTION phase.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

== OUTPUT TEMPLATE ==============================================================

[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]
COMMIT RISK REGISTER -- {topic}

  strategy.md: [FOUND | NOT FOUND -- if absent: COMMITMENT ASSERTION cannot execute]

  | # | Namespace | Signal   | Status                | Date   |
  |---|-----------|----------|-----------------------|--------|
  | 1 | {ns}      | {signal} | VERIFIED | UNVERIFIED  | {date} |
  | 2 |           |          |                       |        |

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

== EXECUTION PHASES =============================================================

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

## V-02: Single-axis — Output format (full tier 6 structural compliance)

**Axis:** Output format — PER-SIGNAL COMMITMENT ASSERTION is the phase name with granularity at left-edge (C-26); the full compressed form propagates into [LAYER 2] enforcement label (C-27); field annotations cite the named phase as the impaired party (C-28).

**Hypothesis:** When the granularity prefix is left-edge in the phase name, that full form propagates into the [LAYER 2] label without truncation, and field annotations name the specific impaired phase rather than a generic epistemic consequence — satisfying C-26, C-27, and C-28 simultaneously from a single structural commitment.

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

## V-03: Single-axis — Lifecycle emphasis (explicit phase boundary contracts)

**Axis:** Lifecycle emphasis — each execution phase is delimited with an explicit input contract, output contract, and guard statement. Phase boundaries are self-documenting.

**Hypothesis:** Wrapping each phase in an input/output contract block forces explicit declaration of what each phase consumes and produces, making the assertion chain auditable at the phase boundary level. C-23 not targeted (granularity stays parenthetical). C-28 satisfied by naming the COMMITMENT ASSERTION phase in the guard annotation.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

== OUTPUT TEMPLATE ==============================================================

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

== EXECUTION PHASES =============================================================

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

## V-04: Combination — Role sequence + Output format (C-26 + C-28; C-27 isolated)

**Axes:** Discovery-first role sequence + Output format with PER-SIGNAL left-edge phase name. [LAYER 2] label carries stake phrase only — the full PER-SIGNAL form is in the phase header but NOT propagated into the enforcement label.

**Hypothesis:** C-26 (left-edge granularity prefix in phase name) and C-28 (phase-attributed field annotation) can both be satisfied while C-27 (full compressed form propagated into layer label) is deliberately withheld. This isolates C-27 as the independently necessary propagation step — a variant that achieves C-26 without C-27 should score 190/195, confirming that label propagation is not implied by phase-name positioning alone.

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

== EXECUTION PHASES =============================================================

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

## V-05: Combination — Lifecycle emphasis + Inertia framing (full tier 6 + adversary naming)

**Axes:** Explicit phase boundary contracts + Inertia framing — the primary competitor is "commit without evidence," named explicitly in the COMMIT DECISION output section.

**Hypothesis:** Naming the status-quo adversary ("commit without evidence") in the COMMIT DECISION section makes the readiness verdict a comparative judgment rather than a coverage threshold. Combined with full tier 6 compliance (PER-SIGNAL left-edge, full form in [LAYER 2] label, phase-attributed field annotations) and the vocabulary coherence invariant declared explicitly as an architectural rule, this produces the highest structural depth and most decision-actionable output.

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Vocabulary coherence invariant ---------------------------------------------
All execution phase names use consequence vocabulary (C-21).
All [LAYER N] enforcement labels use the vocabulary of the phase they govern (C-24).
[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form -- not only the
stake noun phrase -- because PER-SIGNAL is the scope quantifier occupying
left-edge position in the phase name, not a trailing modifier (C-26, C-27).
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

| ID | Axis | C-23 | C-24 | C-25 | C-26 | C-27 | C-28 | Score |
|----|------|------|------|------|------|------|------|-------|
| V-01 | Role sequence | FAIL | PASS | PASS | FAIL | FAIL | PASS | 180/195 |
| V-02 | Output format | PASS | PASS | PASS | PASS | PASS | PASS | 195/195 |
| V-03 | Lifecycle emphasis | FAIL | PASS | PASS | FAIL | FAIL | PASS | 180/195 |
| V-04 | Role seq + Output format | PASS | PASS | PASS | PASS | FAIL | PASS | 190/195 |
| V-05 | Lifecycle + Inertia | PASS | PASS | PASS | PASS | PASS | PASS | 195/195 |

**C-27 isolation test (V-04 vs V-02):** V-04 has PER-SIGNAL left-edge in phase name but [LAYER 2] carries only stake phrase. If C-27 scores independently, V-04 should land at 190/195, confirming that left-edge positioning of the granularity prefix does not automatically propagate into enforcement labels — the full form must be explicitly written into the label.

**C-28 universality:** All five variants satisfy C-28 — V-01/V-03 via `COMMITMENT ASSERTION cannot execute`, V-02/V-04/V-05 via `PER-SIGNAL COMMITMENT ASSERTION cannot execute`. C-28 requires a C-21 phase name in the annotation; it does not require the phase name to be C-26-compliant. This confirms C-28 is independent of the C-23 -> C-26 -> C-27 chain.
