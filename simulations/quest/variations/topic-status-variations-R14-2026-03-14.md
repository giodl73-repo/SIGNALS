I have everything I need. Let me synthesize the R13 state and design the R14 variations.

**R13 state (under v13):**
- V-01/V-04/V-05 → 265/265 (C-41 + C-42 both satisfied)
- V-02/V-03 → 260/265 (one withheld each, orthogonality confirmed)
- Gap: "No R13 variant fails both C-41 and C-42" — that gap defines Round 14

**R14 design:** R13 maxes out v13. Round 14 probes the next layer beyond C-41/C-42.

**Candidate C-43:** PHASE 3 phase-entry adversary declaration. C-42 established the PHASE 2 execution-body adversary site. C-43 extends adversary framing to PHASE 3 entry — naming what PHASE 3 defeats ("inconsistent evidence propagation"), creating a three-site adversary chain (COMMIT DECISION + PHASE 2 entry + PHASE 3 entry). Implication: C-43 => C-42.

**Candidate C-44:** OUTPUT DECLARATION CHAIN as preamble invariant. C-41/C-38 established two execution-phase OUTPUT DECLARATION blocks. C-44 declares the chain itself as an architectural invariant in the preamble — explicitly naming both sites and asserting neither implies the other. Extends the preamble from dual-axis-exit-only (C-34/C-35) to also declare the output-declaration chain. Implication: C-44 => C-41.

---

# Variations: `topic:status` — Round 14
**Rubric:** v13 (max 265) | **Date:** 2026-03-15

---

## Design Context

R13 differentiating evidence: V-01, V-04, V-05 each scored 265/265 under v13;
V-02 and V-03 scored 260/265. Two Tier 12 criteria extracted from R13 signals:

- **C-41**: PHASE 3 OUTPUT DECLARATION with labeled sub-components and trigger
  characterization. Extends the output-declaration-residency and
  labeled-sub-component patterns from PHASE 2 to PHASE 3 as an independently
  necessary second-phase mechanism.

- **C-42**: PHASE 2 phase-entry adversary declaration. Extends adversary framing
  from the output-template site (COMMIT DECISION, C-16) into the PHASE 2
  execution body. Two-site adversary chain established.

**R13 gap:** No R13 variant fails both C-41 and C-42. R14 probes genuinely
new structural territory beyond the PHASE 2/PHASE 3 output declaration and
PHASE 2 adversary declaration patterns.

R14 introduces two new structural property candidates:

- **C-43 candidate**: PHASE 3 phase-entry adversary declaration. C-42
  established the two-site adversary chain: output-template (COMMIT DECISION)
  and PHASE 2 execution body. C-43 extends adversary framing to PHASE 3 entry,
  creating a three-site chain. PHASE 3's adversary is "inconsistent evidence
  propagation" (the consistency guard that PHASE 3 executes to defeat), distinct
  in character from PHASE 2's adversary ("inertia toward evidence-blind commits").
  Form-agnostic: inline ADVERSARY: line or titled block both satisfy.

- **C-44 candidate**: OUTPUT DECLARATION CHAIN as preamble architectural invariant.
  C-41 and C-38 each declare an execution-phase-resident OUTPUT DECLARATION
  (PHASE 3 and PHASE 2 respectively). C-44 explicitly declares the two-phase
  OUTPUT DECLARATION chain as a named architectural invariant in the preamble
  block — naming both phases, asserting that each carries its own independently
  declared output structure, and asserting that neither declaration implies the
  other. Extends the preamble from dual-axis-exit-only (C-34/C-35) to
  dual-axis-exit + output-declaration-chain.

**Orthogonality**: C-43 concerns PHASE 3 execution framing (adversary at phase
entry). C-44 concerns preamble-level architectural declaration (the output
declaration chain as invariant). A variant can carry PHASE 3 adversary without
a preamble chain declaration (C-43 PASS, C-44 FAIL) or a preamble chain
declaration without PHASE 3 adversary (C-43 FAIL, C-44 PASS).

**Predicted score map under v13 (current rubric):**

| Variant | C-41 | C-42 | C-43 | C-44 | Predicted |
|---------|------|------|------|------|-----------|
| V-01    | PASS | PASS | PASS | PASS | 265/265   |
| V-02    | PASS | PASS | FAIL | PASS | 265/265   |
| V-03    | PASS | PASS | PASS | FAIL | 265/265   |
| V-04    | PASS | PASS | PASS | PASS | 265/265   |
| V-05    | PASS | PASS | PASS | PASS | 265/265   |

All five variants score 265 under v13 — C-43 and C-44 are not yet criteria.

**Predicted score map under hypothetical v14 (+10 pts, max 275):**

| Variant | C-43 | C-44 | Predicted |
|---------|------|------|-----------|
| V-01    | PASS | PASS | 275/275   |
| V-02    | FAIL | PASS | 270/275   |
| V-03    | PASS | FAIL | 270/275   |
| V-04    | PASS | PASS | 275/275   |
| V-05    | PASS | PASS | 275/275   |

---

## V-01: Minimum delta — C-43 + C-44 in execution-prose/inline form

**Axis:** Minimum structural delta from R13 V-01. Two targeted additions:
(1) preamble block receives an `OUTPUT DECLARATION CHAIN:` declaration naming
both PHASE 2 and PHASE 3 as independently declared output structure sites and
asserting that neither declaration is implied by the other (C-44 candidate —
extends the preamble from dual-axis-exit invariant to also declare the
output-declaration chain as an architectural invariant); (2) PHASE 3 execution
body receives an `ADVERSARY:` clause at entry naming inconsistent evidence
propagation as what the phase defeats (C-43 candidate — extends adversary
framing from the PHASE 2 execution body to PHASE 3, completing a three-site
adversary chain: COMMIT DECISION output template + PHASE 2 entry + PHASE 3
entry). All other structure identical to R13 V-01.

**Hypothesis:** C-44 adds an OUTPUT DECLARATION CHAIN declaration to the
preamble block, making the two-phase output-declaration pattern explicitly
named as an architectural property. C-43 adds a single ADVERSARY: line at
PHASE 3 execution entry, extending the two-site adversary chain (C-16 + C-42)
to three sites. Under v13, V-01 scores 265 (C-43 and C-44 are not yet
criteria). The V-01 vs V-02 delta isolates C-43; the V-01 vs V-03 delta
isolates C-44. The delta between V-02 and V-03 should be 0 under v13 (both
265) — confirming C-43 and C-44 are independently observable, not implied
by each other.

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
OUTPUT DECLARATION CHAIN: PHASE 2 and PHASE 3 each carry an independently
declared OUTPUT DECLARATION block embedded in the execution body. PHASE 2
OUTPUT DECLARATION declares the dual-axis gate invariant with trigger
characterization; PHASE 3 OUTPUT DECLARATION declares the consistency guard
invariant with trigger characterization. Neither declaration is implied by the
other; each execution phase requires its own independently declared output
structure.
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
  ADVERSARY: inconsistent evidence propagation -- default when this phase skips
  the consistency guard: a computed percent=100% co-existing with UNVERIFIED
  signals produces a false-READY readiness verdict that ships without
  contradiction detection.
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

## V-02: Single-axis — C-43 withheld (isolation test)

**Axis:** C-43 deliberately withheld. The preamble block carries the OUTPUT
DECLARATION CHAIN declaration (C-44 PASS) but PHASE 3 has no adversary clause
at its entry. PHASE 3 begins directly with the percent computation — identical
in opening structure to R13 V-01's PHASE 3. The `ADVERSARY:` line that V-01
prepends to PHASE 3 execution is absent. All other structure identical to V-01.

**Hypothesis:** If C-43 requires an explicit adversary clause within the PHASE 3
execution body — extending the two-site adversary chain (COMMIT DECISION + PHASE 2
entry) to three sites — then removing that clause while retaining the preamble
chain declaration should fail C-43 while leaving C-44 intact. Under v13, both
V-01 and V-02 score 265 (C-43 is not yet a criterion). The observable structural
gap: V-01's PHASE 3 body opens with `ADVERSARY: inconsistent evidence
propagation...`; V-02's PHASE 3 opens with `percent = VERIFIED count / PLANNED
count * 100`. If a v14 rubric extracts C-43, V-02 scores 5 points below V-01.
Confirms that adversary framing at PHASE 2 entry (C-42) does not propagate to
PHASE 3 automatically: C-43 is independently necessary as a third-site mechanism.

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
OUTPUT DECLARATION CHAIN: PHASE 2 and PHASE 3 each carry an independently
declared OUTPUT DECLARATION block embedded in the execution body. PHASE 2
OUTPUT DECLARATION declares the dual-axis gate invariant with trigger
characterization; PHASE 3 OUTPUT DECLARATION declares the consistency guard
invariant with trigger characterization. Neither declaration is implied by the
other; each execution phase requires its own independently declared output
structure.
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

## V-03: Single-axis — C-44 withheld (isolation test)

**Axis:** C-44 deliberately withheld. PHASE 3 execution body carries the
adversary clause at entry (`ADVERSARY:` line — C-43 PASS) but the preamble
block has no OUTPUT DECLARATION CHAIN declaration. The preamble contains only
the vocabulary coherence invariant and dual-axis exit declaration that R13 V-01
established — it does not name the two-phase output-declaration pattern as an
architectural invariant. The `OUTPUT DECLARATION CHAIN:` sentence block that
V-01 adds to the preamble is absent. All other structure identical to V-01.

**Hypothesis:** If C-44 requires an explicit OUTPUT DECLARATION CHAIN declaration
in the preamble — naming both PHASE 2 and PHASE 3 as independently required
output structure sites and asserting neither implies the other — then removing
that declaration while retaining PHASE 3 adversary framing should fail C-44
while leaving C-43 intact. Under v13, both V-01 and V-03 score 265 (C-44 is
not yet a criterion). The observable structural gap: V-01's preamble closes
with `...each execution phase requires its own independently declared output
structure.`; V-03's preamble closes with `...stop message before PHASE 3
(EXPOSURE COMPUTATION).` If a v14 rubric extracts C-44, V-03 scores 5 points
below V-01. Confirms that the existence of PHASE 2 and PHASE 3 output
declarations (C-38/C-41) does not imply a preamble-level declaration of the
chain pattern: C-44 is independently necessary as a preamble-site architectural
invariant declaration.

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
  ADVERSARY: inconsistent evidence propagation -- default when this phase skips
  the consistency guard: a computed percent=100% co-existing with UNVERIFIED
  signals produces a false-READY readiness verdict that ships without
  contradiction detection.
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

## V-04: Combination — Lifecycle GUARD contract form with C-43 + C-44

**Axes:** Lifecycle emphasis (phase contract blocks with INPUT / GUARD / OUTPUT
fields) + C-44 via an `OUTPUT DECLARATION CHAIN:` declaration in the preamble
prose block (same content as V-01, in the same inline location) + C-43 via an
`ADVERSARY:` clause in the PHASE 3 execution prose below the PHASE 3 contract
box header. Tests whether C-43 and C-44 are form-agnostic across execution-prose
(V-01) and lifecycle contract (V-04) phase presentation styles. The ADVERSARY
clause appears in the execution prose section of PHASE 3 (not inside the box
header fields), and the OUTPUT DECLARATION CHAIN declaration appears in the
preamble block (not inside any phase box).

**Hypothesis:** C-42 was confirmed form-agnostic in R13: the ADVERSARY: line
in PHASE 2 execution prose satisfies C-42 whether the surrounding phase
structure uses execution-prose headers (V-01/V-03) or lifecycle contract boxes
(V-04/V-05). By the same logic, C-43 (PHASE 3 adversary) should be form-agnostic:
the ADVERSARY: line in PHASE 3 execution prose satisfies C-43 whether PHASE 3
uses a prose header or a lifecycle contract box. C-44's preamble location is
form-agnostic by construction (the preamble exists in the same dashes block
regardless of phase presentation style). If V-04 and V-01 both reach the same
score under hypothetical v14, C-43 and C-44 form-agnosticism is confirmed for
the lifecycle contract style.

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
OUTPUT DECLARATION CHAIN: PHASE 2 and PHASE 3 each carry an independently
declared OUTPUT DECLARATION block embedded in the execution body. PHASE 2
OUTPUT DECLARATION declares the dual-axis gate invariant with trigger
characterization; PHASE 3 OUTPUT DECLARATION declares the consistency guard
invariant with trigger characterization. Neither declaration is implied by the
other; each execution phase requires its own independently declared output
structure.
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
  ADVERSARY: inconsistent evidence propagation -- default when this phase skips
  the consistency guard: a computed percent=100% co-existing with UNVERIFIED
  signals produces a false-READY readiness verdict that ships without
  contradiction detection.
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

## V-05: Combination — Elevated titled blocks for PHASE 3 adversary + preamble output-declaration chain

**Axes:** Lifecycle emphasis + C-43 elevated to a `+-- PHASE 3 ADVERSARY
DECLARATION --+` titled block within PHASE 3's execution body + C-44 elevated
to a `+-- OUTPUT DECLARATION CHAIN INVARIANT --+` titled block appended to the
preamble section. Both new structural properties are presented as formally
demarcated titled boxes rather than inline prose lines. Extends the titled-block
pattern established for PHASE 2 ADVERSARY DECLARATION (R13 V-05, C-42 form) and
PHASE 2/PHASE 3 OUTPUT DECLARATION blocks to the new C-43 and C-44 structures.
A scorer reading either new block in isolation can verify the structural property
without consulting any other section.

**Hypothesis:** C-42's elevated titled-block form (R13 V-05) made PHASE 2
adversary framing at the execution-phase site independently verifiable. V-05
extends that: the `+-- PHASE 3 ADVERSARY DECLARATION --+` block makes three-site
adversary framing independently verifiable at PHASE 3 (scorer reads block,
confirms adversary named at PHASE 3 execution body, not only at PHASE 2 and
output template). The `+-- OUTPUT DECLARATION CHAIN INVARIANT --+` block makes
the chain-level architectural declaration independently verifiable (scorer reads
block, confirms both phases are named, independence asserted, chain declared as
architectural invariant). If V-05 and V-01 score identically under hypothetical
v14, C-43 and C-44 are form-agnostic across inline-prose and titled-block styles
-- consistent with C-42's R13 form-agnosticism confirmation.

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

+-- OUTPUT DECLARATION CHAIN INVARIANT ----------------------------------------+
| PHASE 2 and PHASE 3 each carry an independently declared OUTPUT DECLARATION    |
| block embedded in the execution body.                                           |
| PHASE 2 OUTPUT DECLARATION: declares the dual-axis gate invariant with trigger  |
|   characterization (file-absent and topic-absent trigger conditions named).     |
| PHASE 3 OUTPUT DECLARATION: declares the consistency guard invariant with       |
|   trigger characterization (guard firing condition named).                      |
| Architectural invariant: neither declaration is implied by the other.           |
|   Each execution phase requires its own independently declared output structure. |
+------------------------------------------------------------------------------+
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

  +-- PHASE 3 ADVERSARY DECLARATION ------------------------------------------+
  | ADVERSARY: inconsistent evidence propagation                                |
  | Trigger: fires when consistency guard is skipped or bypassed                |
  | Outcome if undefeated: percent=100% co-existing with UNVERIFIED signals     |
  |   produces a false-READY readiness verdict that ships without contradiction  |
  |   detection                                                                 |
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

| ID | Axis | C-43 | C-44 | v13 Score | v14 (predicted) |
|----|------|------|------|-----------|-----------------|
| V-01 | Min delta: C-43 + C-44 in inline/prose form | PASS | PASS | 265/265 | 275/275 |
| V-02 | C-43 withheld — preamble chain declared, no PHASE 3 adversary | FAIL | PASS | 265/265 | 270/275 |
| V-03 | C-44 withheld — PHASE 3 adversary declared, no preamble chain | PASS | FAIL | 265/265 | 270/275 |
| V-04 | Lifecycle GUARD contract form with C-43 + C-44 | PASS | PASS | 265/265 | 275/275 |
| V-05 | Lifecycle + elevated titled blocks for PHASE 3 adversary and chain invariant | PASS | PASS | 265/265 | 275/275 |

All five variants score 265/265 under v13 — C-43 and C-44 are not yet criteria;
they are observable structural patterns in R14's excellence signals.

**C-43 isolation test (V-01 vs V-02):** V-02 retains the full R13 V-01 structure
including C-41/C-42 and adds the preamble OUTPUT DECLARATION CHAIN declaration
(C-44 PASS) but withholds the PHASE 3 adversary clause. The observable gap:
V-01's PHASE 3 body opens with `ADVERSARY: inconsistent evidence propagation...`;
V-02's PHASE 3 body opens with `percent = VERIFIED count / PLANNED count * 100`.
If a v14 rubric extracts C-43, V-02 scores 5 points below V-01. Confirms that
adversary framing at PHASE 2 entry (C-42) does not propagate to PHASE 3 entry:
C-43 is independently necessary as a third-site mechanism.

**C-44 isolation test (V-01 vs V-03):** V-03 retains the full R13 V-01 structure
and adds the PHASE 3 adversary clause (C-43 PASS) but withholds the preamble
OUTPUT DECLARATION CHAIN declaration. The observable gap: V-01's preamble closes
with `...each execution phase requires its own independently declared output
structure.`; V-03's preamble closes with `...stop message before PHASE 3
(EXPOSURE COMPUTATION).` If a v14 rubric extracts C-44, V-03 scores 5 points
below V-01. Confirms that the existence of two execution-phase output declarations
(C-38/C-41) does not imply a preamble-level chain declaration: C-44 is
independently necessary as a preamble-site architectural invariant.

**Orthogonality test (V-02 vs V-03):** Both score 265/265 under v13. V-02 has
C-44 without C-43; V-03 has C-43 without C-44. Under v13 they are
indistinguishable. Under v14, if both C-43 and C-44 are extracted, V-02 and V-03
each trade: the criterion they satisfy offsets the one they withhold, confirming
the two criteria are orthogonal and independently necessary. Symmetric 5-point
delta from V-01 in both directions.

**Form-agnosticism tests (V-01 vs V-04 vs V-05):** V-01 uses inline prose for
both new properties; V-04 uses lifecycle contract boxes with prose-appended
adversary and output declarations; V-05 uses elevated titled blocks for both
the PHASE 3 adversary declaration and the preamble chain invariant. If all
three score identically under v14, C-43 and C-44 are form-agnostic across
prose, lifecycle-contract, and titled-block presentation styles — consistent
with R13's confirmation that C-41 and C-42 are form-agnostic.

**Adversary chain distinction (C-43):** The PHASE 3 adversary ("inconsistent
evidence propagation") is structurally distinct from the PHASE 2 adversary
("inertia toward evidence-blind commits") — the character of the adversary
differs by phase function. PHASE 2 defeats a behavioral default (inertia);
PHASE 3 defeats a computational corruption (inconsistency). This distinction is
intentional and required: the adversary clause at each phase site must name the
adversary appropriate to that phase's function, not repeat the prior phase's
adversary verbatim.

**C-44 preamble expansion pattern:** C-44 adds a second named architectural
invariant to the preamble block. The preamble previously declared one invariant
(PHASE 2 dual-axis exit, established by C-34/C-35). C-44 declares a second
(the OUTPUT DECLARATION CHAIN). The preamble grows from single-invariant to
dual-invariant scope — each invariant independently named, characterized, and
independently verifiable without consulting any phase execution body.
