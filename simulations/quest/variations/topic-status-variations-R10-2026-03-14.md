Now I have everything I need. R9 state: V-04 and V-05 score 230/235 under v10 (C-35 and C-36 each satisfied by exactly one variant, never jointly). The R10 gap is that no single variant satisfies both.

---

# Variations: `topic:status` — Round 10
**Rubric:** v10 (max 235) | **Date:** 2026-03-15

---

## Design Context

R9 differentiating evidence under v10 projection:

| Variant | C-35 | C-36 | Score (v10) |
|---------|------|------|-------------|
| V-01 | FAIL | FAIL | 225/235 |
| V-02 | FAIL | FAIL | 220/235 |
| V-03 | FAIL | FAIL | 225/235 |
| V-04 | **PASS** | FAIL | **230/235** |
| V-05 | FAIL | **PASS** | **230/235** |

**R9 gap:** C-35 and C-36 are not jointly satisfied by any single variant. V-04 satisfies C-35 (per-axis trigger sentences in preamble after canonical declaration) but fails C-36 (no third structural site). V-05 satisfies C-36 (preamble + GUARD entry names + PHASE 2 OUTPUT block = three-site chain) but fails C-35 (canonical single-line preamble, no trigger expansion).

**R10 hypothesis:** The gap closes by combining V-04's per-axis trigger sentences (C-35) with a third structural site (C-36). V-01 tests this minimum delta: take R9 V-04's preamble exactly and add the invariant echo to the COMMIT DECISION block in the output template — a commit-framing section, which is an explicitly named valid third site under C-36.

**Variation axes:**
- **C-35 presence** (trigger sentences present vs withheld): single-axis isolation V-01/V-02/V-03
- **C-36 third-site placement** (commit-framing vs OUTPUT block vs execution-body declaration): probed across V-01, V-04, V-05
- **Lifecycle emphasis** (inline prose vs GUARD contract blocks): V-04
- **Inertia framing depth** (COMMIT DECISION framing extended): V-05

**Predicted score map:**

| Variant | C-35 | C-36 | Total |
|---------|------|------|-------|
| V-01 | PASS | PASS | 235/235 |
| V-02 | FAIL | PASS | 230/235 |
| V-03 | PASS | FAIL | 230/235 |
| V-04 | PASS | PASS | 235/235 |
| V-05 | PASS | PASS | 235/235 |

**C-35 isolation (V-01 vs V-02):** both carry the COMMIT DECISION third-site echo (C-36 PASS); differ only by presence of per-axis trigger sentences. Expected 5-point gap confirms trigger sentences independently necessary beyond canonical axis names.

**C-36 isolation (V-01 vs V-03):** both carry per-axis trigger sentences (C-35 PASS); V-03 withholds the third site. Expected 5-point gap confirms three-site chain independently necessary beyond preamble + GUARD.

**C-36 third-site agnosticism:** V-01 uses COMMIT DECISION block, V-04 uses lifecycle PHASE 2 OUTPUT field, V-05 uses an explicit PHASE 2 OUTPUT DECLARATION in execution body. If all three satisfy C-36, the criterion is confirmed site-agnostic within the named categories. Candidate excellence signal for R10.

---

## V-01: Single-axis — Minimum delta (C-35 + C-36, minimum change from R9 V-04)

**Axis:** Third structural site added to R9 V-04. R9 V-04 satisfied C-35 (per-axis trigger sentences) but failed C-36 (no third site). The minimum delta is a single declaration line added to the COMMIT DECISION block in the output template. COMMIT DECISION is a commit-framing section — explicitly named as a valid third site under C-36. All other structure is identical to R9 V-04.

**Hypothesis:** R9 V-04 scores 230 under v10 (C-35 PASS, C-36 FAIL). Adding the `Dual-axis gate invariant:` line to COMMIT DECISION creates a third independently verifiable declaration site. A scorer reading only the COMMIT DECISION block sees both axis names, the distinctness assertion, and the distinct-messages claim — independently verifiable without consulting the preamble or GUARD entries. This moves V-04 from 230 to 235. The delta from V-02 (which adds the same third site but withholds trigger sentences) isolates whether C-35 is independently necessary.

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
  Dual-axis gate invariant: file-absent and topic-absent exits are structurally
  distinct stop conditions with distinct messages
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

## V-02: Single-axis — C-35 withheld, C-36 present (isolation test for C-35)

**Axis:** C-35 deliberately withheld. Preamble uses the canonical axis-complete declaration (C-34 PASS, C-33 PASS) but provides no per-axis trigger sentences. C-36 is satisfied identically to V-01: the same COMMIT DECISION block echo is present, producing the three-site chain (preamble + Exit A/Exit B labels + COMMIT DECISION). All other structure identical to V-01.

**Hypothesis:** If C-35 requires a dedicated trigger sentence per axis beyond what the canonical axis name conveys, this variant should score 230/235 — C-36 PASS (three sites), C-35 FAIL (no trigger expansion in preamble). The expected 5-point delta between V-01 (235) and V-02 (230) confirms that axis-name alone in the canonical declaration is insufficient for C-35: characterizing the trigger condition that fires each axis is independently necessary beyond naming it. If the delta is 0, C-34 and C-35 are not distinguishable by the scorer.

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
  Dual-axis gate invariant: file-absent and topic-absent exits are structurally
  distinct stop conditions with distinct messages
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

## V-03: Single-axis — C-36 withheld, C-35 present (isolation test for C-36)

**Axis:** C-36 deliberately withheld. Per-axis trigger sentences are present in the preamble (C-35 PASS). No third structural site is added: the COMMIT DECISION block carries no invariant echo, and the execution section adds no OUTPUT DECLARATION. This body is R9 V-04 exactly — reproduced here as the R10 isolation baseline.

**Hypothesis:** This variant projects to 230/235 under v10 — the same score R9 V-04 received in projection. It tests whether the three-site chain is independently necessary when C-35 is already satisfied. The expected 5-point delta between V-01 (235) and V-03 (230) confirms that per-axis trigger sentences do not substitute for multi-site declaration: a preamble with rich trigger characterization plus named GUARD exits constitutes only two sites, which is insufficient for C-36. The symmetric prediction (V-02 = 230 via C-35 withheld, V-03 = 230 via C-36 withheld) additionally confirms that C-35 and C-36 carry equal weight and are independently necessary.

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

## V-04: Combination — Lifecycle emphasis + C-35 (trigger sentences) + C-36 (OUTPUT block third site)

**Axes:** Lifecycle emphasis + C-35 + C-36 via PHASE 2 OUTPUT block. Base: R9 V-03 (lifecycle GUARD contract structure, canonical preamble, named GUARD exits, 225 under v9 / 225 under v10). Modifications: (1) preamble extended with per-axis trigger sentences (C-35); (2) PHASE 2 OUTPUT field extended with the invariant echo (C-36 third site). The three C-36 sites are: preamble (C-34 site), GUARD entry named labels (C-32 site), PHASE 2 OUTPUT field declaration. This probes whether a lifecycle OUTPUT field satisfies C-36 as a structurally distinct site — distinct from preamble and GUARD in that it is an execution-output declaration rather than a guard-condition or architectural declaration.

**Hypothesis:** The lifecycle structure provides maximum auditability for C-36: the three sites (preamble, GUARD entries, OUTPUT field) are each in separate labeled structural positions within the phase contract block, making the invariant echo legible at the contract level alone. C-35 is satisfied by the preamble trigger sentences (identical form to V-01). Predicts 235. Cross-check with V-01: if both score 235, the third-site placement (OUTPUT field vs COMMIT DECISION) is form-agnostic for C-36, yielding a structural-site-agnosticism excellence signal analogous to the R9 C-32 form-agnosticism finding.

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
| GUARD:  Exit A -- file absent ->                                            |
|             output "No planned baseline -- commit exposure is               |
|             unquantifiable." and stop                                       |
|         Exit B -- topic not registered ->                                   |
|             output "topic not registered: no planned signals for {topic}"   |
|             and stop before PHASE 3 (EXPOSURE COMPUTATION)                 |
| OUTPUT: VERIFIED | UNVERIFIED per planned signal; no batch evaluation;      |
|         if UNVERIFIED: ships without this signal on commit;                 |
|         if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired       |
|         evidence; file-absent and topic-absent exits are structurally       |
|         distinct with distinct messages                                     |
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

## V-05: Combination — Inertia framing deepened + C-35 + C-36 (execution-body OUTPUT DECLARATION third site)

**Axes:** Inertia framing depth + C-35 + C-36 via execution-body OUTPUT DECLARATION. The third structural site is placed directly in the PHASE 2 execution body — after the dual-axis GUARD exits and before signal extraction — as an explicit labeled declaration. This is structurally distinct from COMMIT DECISION (output template, V-01) and from the lifecycle OUTPUT block (contract field, V-04): it is an assertion within the execution prose itself, appended to the exit logic as a post-guard invariant confirmation. Additionally, the COMMIT DECISION PRIMARY ADVERSARY framing is extended to characterize the compound cost of inertia — each unchecked signal is a compounding commitment — deepening C-16.

**Hypothesis:** The execution-body placement for C-36 site 3 is the most tightly coupled to the guard mechanism: the invariant is asserted immediately after Exit A and Exit B are processed, in the same structural location where the exits fire. A scorer reading only the PHASE 2 execution block (without consulting the preamble or the output template) encounters the invariant echo as part of the execution narrative. If this form satisfies C-36 (scorer determines dual-axis property is enforced from site 3 alone), the criterion is confirmed fully site-agnostic. C-35 is satisfied identically to V-01 and V-04 via the preamble trigger sentences. Predicts 235. The combination of three distinct third-site placements across V-01, V-04, V-05 — all predicting 235 — would constitute the key R10 excellence signal: C-36 site-agnosticism within the named categories (OUTPUT block, commit-framing, execution-body assertion).

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
  incomplete signals is the default outcome when status is not checked;
  each unverified signal compounds exposure, making future checks less likely
  Readiness: READY | PARTIAL | NOT READY
  Committing now means shipping without: {list of UNVERIFIED signals}
  Committing now defeats: {N} signals not yet in evidence
  Committing now normalizes: shipping without checking as the default pattern

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
  [PHASE 2 OUTPUT DECLARATION: Exit A (file-absent) and Exit B (topic-absent)
  are structurally distinct stop conditions with distinct messages -- Exit A
  fires when strategy.md does not exist on disk; Exit B fires when strategy.md
  exists but contains no entry for {topic}; verifiable at this site independently]
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

## Predicted Score Summary

| ID | Axis | C-35 | C-36 | Score |
|----|------|------|------|-------|
| V-01 | Minimum delta — R9 V-04 + COMMIT DECISION third site | PASS | PASS | 235/235 |
| V-02 | C-35 withheld — canonical preamble + same COMMIT DECISION third site | FAIL | PASS | 230/235 |
| V-03 | C-36 withheld — R9 V-04 exact (trigger sentences, no third site) | PASS | FAIL | 230/235 |
| V-04 | Lifecycle + trigger sentences + PHASE 2 OUTPUT block third site | PASS | PASS | 235/235 |
| V-05 | Inertia deepened + trigger sentences + execution-body OUTPUT DECLARATION third site | PASS | PASS | 235/235 |

**C-35 isolation (V-01 vs V-02):** preambles differ by presence of two trigger sentences; C-36 structure is identical in both. Expected 5-point gap. Confirms trigger-sentence-per-axis is independently necessary beyond canonical axis naming.

**C-36 isolation (V-01 vs V-03):** preambles identical (both have trigger sentences, C-35 PASS); V-03 has no third site, V-01 has COMMIT DECISION echo. Expected 5-point gap. Confirms three-site chain is independently necessary beyond preamble + named exits.

**Symmetric gap test (V-02 vs V-03):** both predict 230 via different single-criterion failures. Confirms C-35 and C-36 are independently 5-point criteria with equal weight.

**C-36 third-site agnosticism (V-01 vs V-04 vs V-05):** three variants place the third site at structurally distinct locations — output template commit-framing section (V-01), lifecycle phase OUTPUT block (V-04), execution-body post-guard assertion (V-05). If all three score 235, C-36 is confirmed site-agnostic within the named categories. Candidate R10 excellence signal: multi-site chain is a structural property of the invariant, not of any particular location form.
