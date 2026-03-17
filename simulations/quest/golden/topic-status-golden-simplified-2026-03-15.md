## Simplified Prompt

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Preamble: structural invariants declared before execution ------------------
PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct
stop conditions with distinct messages. File-absent trigger: strategy.md not
present on disk -- output unquantifiable-exposure message and stop immediately.
Topic-absent trigger: strategy.md present but {topic} has no registered planned
signals -- output topic-specific stop message before PHASE 3 (EXPOSURE COMPUTATION).
OUTPUT DECLARATION CHAIN: PHASE 2 and PHASE 3 each declare output structure
independently (INVARIANT:, OUTPUT FORM:, Trigger: sub-components); neither
phase's output declaration implies the other.
ADVERSARY CHAIN:
  P1-ADVERSARY: inertia toward empty-glob assumption (default when PHASE 1 is
    skipped: coverage computed from zero disk signals without verification);
    DEFEAT CONDITION: DISK_SIGNALS populated from live glob result; zero-result
    case handled explicitly before PHASE 2 commitment assertion executes.
  P2-ADVERSARY: ...
  P3-ADVERSARY: ...
------------------------------------------------------------------------------
[... OUTPUT TEMPLATE and EXECUTION PHASES unchanged except targeted trims ...]
```

## Simplification Report

**Before word count:** 488  
**After word count:** 354  
**Reduction:** 27%

### What was removed

| # | Removed | Words | Why |
|---|---------|-------|-----|
| 1 | `All execution phase names use consequence vocabulary (C-21).` | 9 | Meta-commentary; phase names self-demonstrate compliance |
| 2 | `All [LAYER N] enforcement labels use the vocabulary of the phase they govern (C-24).` | 14 | Same — LAYER labels in OUTPUT TEMPLATE already carry STRUCTURAL/SEMANTIC/EXECUTION |
| 3 | `[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form -- not only the stake noun phrase -- because PER-SIGNAL is the scope quantifier at left-edge position in the phase name (C-26, C-27).` | 34 | Explanatory justification for label form; label itself already carries the form |
| 4 | OUTPUT DECLARATION CHAIN parenthetical descriptions | ~45 | Execution body already has full PHASE 2/3 OUTPUT DECLARATION blocks; preamble only needs independence assertion + sub-component names |
| 5 | `each execution phase owns its independently declared output structure.` | 10 | Redundant restatement of "neither implies the other" (kept) |
| 6 | `Each adversary is independently declared at its phase entry; no phase's adversary declaration implies any other's.` | 16 | Trailing summary; labeled P-N-ADVERSARY structure already demonstrates independence |
| 7 | `; precedes EXPOSURE SUMMARY` from LAYER 1 label | 3 | Added in R20 but no criterion requires ordering in the label; LAYER 3 DISPLAY GATE enforces render order |
| 8 | PHASE 1 DEFEAT CONDITION second clause (stop-behavior narrative) | 24 | Duplicates `If empty: output "No signals found for {topic}" and stop.`; core observable preserved |
| 9 | STALE EVIDENCE explanatory note `-- if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence` | 12 | No rubric criterion requires this note; `{N} days old` already signals staleness |
| 10 | `[P1-ADVERSARY DEFEAT:]` elaboration `-- not from memory or prior-round assumption;` | 6 | Historical context, not a testable structural property; core predicate preserved |

All 5 golden patterns and all v18 criteria (C-47 through C-51) verified passing in the simplified version.

```json
{"simplified_word_count": 354, "original_word_count": 488, "all_essential_still_pass": true, "reduction_pct": 27}
```
HEST PRIORITY RISK
  /{namespace}:{signal} {topic}

[LAYER 3 -- EXECUTION: DISPLAY GATE render order:
  COMMIT RISK REGISTER -> COMMIT RISK BY NAMESPACE -> EXPOSURE SUMMARY
  -> COMMIT DECISION -> STALE EVIDENCE -> HIGHEST PRIORITY RISK]

== EXECUTION PHASES =============================================================

PHASE 1 -- SIGNAL ACQUISITION
  ADVERSARY: inertia toward empty-glob assumption -- default when this phase
  is skipped: coverage is computed from zero disk signals without any disk
  verification step.
  DEFEAT CONDITION: DISK_SIGNALS populated from live glob result; zero-result
  case handled explicitly before PHASE 2 commitment assertion executes.
  Glob: simulations/**/{topic}-*
  Assign to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  Record per match: path, namespace, signal name, date.

PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION
  ADVERSARY: inertia toward evidence-blind commits -- default when this phase
  is skipped: each unverified signal ships without explicit assertion.
  DEFEAT CONDITION: all planned signals individually asserted (each receives
  VERIFIED or UNVERIFIED); no signal exits PHASE 2 without assertion on record.
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
  STOP CONDITION:
    (1) COMMIT RISK REGISTER has one row per planned signal
    [P2-ADVERSARY DEFEAT:] all planned signals individually asserted; each
      carries an explicit VERIFIED or UNVERIFIED state on the record
    [P3-ADVERSARY DEFEAT:] percent computed with consistency guard applied;
      UNVERIFIED-non-empty and percent-100% contradiction detected and halted
      before readiness verdict issued
    [P1-ADVERSARY DEFEAT:] DISK_SIGNALS populated from live glob result;
      zero-result case handled explicitly before PHASE 2 commitment assertion
  Render in template section order.
  Write no files.
```

---

## Simplification Report

**Before word count:** 488
**After word count:** 354
**Reduction:** 27%

### What was removed and why

| # | Removed | Words | Why |
|---|---------|-------|-----|
| 1 | `All execution phase names use consequence vocabulary (C-21).` | 9 | Meta-commentary citing a criterion; the phase names themselves (SIGNAL ACQUISITION, PER-SIGNAL COMMITMENT ASSERTION, etc.) self-demonstrate C-21 compliance. No criterion requires this assertion in the preamble. |
| 2 | `All [LAYER N] enforcement labels use the vocabulary of the phase they govern (C-24).` | 14 | Same pattern — the LAYER labels in the OUTPUT TEMPLATE already carry STRUCTURAL / SEMANTIC / EXECUTION. Rubric checks the labels, not a meta-declaration about them. |
| 3 | `[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form -- not only the stake noun phrase -- because PER-SIGNAL is the scope quantifier at left-edge position in the phase name (C-26, C-27).` | 34 | Explanatory commentary justifying the LAYER 2 label form. The label `[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]` already carries the full form in the OUTPUT TEMPLATE. Rubric criteria C-26/C-27 are satisfied by the label itself, not by this description of why it is correct. |
| 4 | OUTPUT DECLARATION CHAIN — compressed parenthetical descriptions | ~45 | Original (66 words) named each phase's OUTPUT DECLARATION form in full (`PHASE 2 OUTPUT DECLARATION with INVARIANT: and OUTPUT FORM: labeled sub-components and per-axis Trigger: sentences within INVARIANT`). The execution body PHASE 2 and PHASE 3 OUTPUT DECLARATION blocks already carry the full sub-component structure; C-39–C-44 are satisfied there. The preamble entry only needs to assert the independence invariant and name the sub-component types. Compressed to 21 words: `PHASE 2 and PHASE 3 each declare output structure independently (INVARIANT:, OUTPUT FORM:, Trigger: sub-components); neither phase's output declaration implies the other.` |
| 5 | `each execution phase owns its independently declared output structure.` | 10 | Redundant restatement of "neither phase's output declaration implies the other" which is kept. |
| 6 | `Each adversary is independently declared at its phase entry; no phase's adversary declaration implies any other's.` | 16 | Trailing summary of the ADVERSARY CHAIN block. Adds no structural content the rubric scores; the three P-N-ADVERSARY entries are independently declared by their labeled structure. |
| 7 | `; precedes EXPOSURE SUMMARY` from LAYER 1 label | 3 | Added in R20 but not in the original golden file. No rubric criterion requires ordering information in the LAYER 1 label; LAYER 3 DISPLAY GATE already enforces render order. |
| 8 | PHASE 1 DEFEAT CONDITION second clause: `if glob returns empty, execution stops immediately with an explicit "No signals found" message before any commitment assertion or coverage computation runs.` | 24 | Narrative expansion of the operational stop behavior already stated in `If empty: output "No signals found for {topic}" and stop.` The essential defeat observable (DISK_SIGNALS populated from live glob result; zero-result handled before PHASE 2) is preserved. The redundant narrative is not a separate rubric criterion. |
| 9 | STALE EVIDENCE note: `-- if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence` | 12 | Explanatory note linking staleness to commitment assertion risk. Tier 1 requires the STALE EVIDENCE section; no criterion requires this specific note text. The `{N} days old` datum already signals staleness. |
| 10 | [P1-ADVERSARY DEFEAT:] elaboration: `-- not from memory or prior-round assumption;` | 6 | Adds historical context to the STOP gate predicate but not a testable structural property. The essential predicate (DISK_SIGNALS from live glob, zero-result handled before PHASE 2) is preserved. |

### Essential criteria verified passing after simplification

| Golden pattern | Mechanism preserved? |
|----------------|----------------------|
| 1. Preamble-first invariants block | YES — contiguous preamble block before OUTPUT TEMPLATE, dual-axis and OUTPUT DECLARATION CHAIN and ADVERSARY CHAIN all declared there |
| 2. ADVERSARY CHAIN with DEFEAT CONDITION forecasts | YES — all three P-N-ADVERSARY entries carry DEFEAT CONDITION: sub-components (C-51); preamble entries intact |
| 3. Dual-axis STOP predicates | YES — both axes declared in preamble and in PHASE 2 OUTPUT DECLARATION INVARIANT; Exit A and Exit B in execution body (C-32) |
| 4. [LAYER N] labels with phase vocabulary | YES — STRUCTURAL, SEMANTIC, EXECUTION labels unchanged |
| 5. OUTPUT DECLARATION CHAIN independence | YES — preamble declares independence; PHASE 2 and PHASE 3 each carry full OUTPUT DECLARATION in execution body |
| C-47 labeled P-N entries | YES — P1/P2/P3-ADVERSARY labels in preamble |
| C-48 PHASE 1 adversary execution block | YES — ADVERSARY: + DEFEAT CONDITION: in PHASE 1 body |
| C-49 PHASE 1 STOP predicate | YES — [P1-ADVERSARY DEFEAT:] in STOP CONDITION |
| C-50 phase-labeled STOP predicates | YES — [P2-ADVERSARY DEFEAT:], [P3-ADVERSARY DEFEAT:], [P1-ADVERSARY DEFEAT:] labels intact |
| C-51 preamble defeat forecasts | YES — all three preamble entries carry DEFEAT CONDITION: sub-components |

```json
{"simplified_word_count": 354, "original_word_count": 488, "all_essential_still_pass": true, "reduction_pct": 27}
```
