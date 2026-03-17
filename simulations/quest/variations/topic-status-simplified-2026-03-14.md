---

## Simplified Prompt Body

```
Topic: $ARGUMENTS

DISPLAY ONLY. Write no files.

-- Preamble: structural invariants declared before execution ------------------
All execution phase names use consequence vocabulary.
All [LAYER N] enforcement labels use the vocabulary of the phase they govern.
[LAYER 2] carries the full PER-SIGNAL COMMITMENT ASSERTION form -- not only the
stake noun phrase.
PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct
stop conditions with distinct messages. File-absent trigger: strategy.md not
present on disk. Topic-absent trigger: {topic} has no registered planned signals.
OUTPUT DECLARATION CHAIN: PHASE 2 and PHASE 3 each declare their own output
structure independently. Neither phase's declaration implies the other.
ADVERSARY CHAIN:
  P1-ADVERSARY: inertia toward empty-glob assumption (default when PHASE 1 is
    skipped: coverage computed from zero disk signals without verification);
    DEFEAT CONDITION: DISK_SIGNALS populated from live glob result; zero-result
    case handled explicitly before PHASE 2 commitment assertion executes.
  P2-ADVERSARY: inertia toward evidence-blind commits (default when PHASE 2 is
    skipped: unverified signals ship without explicit assertion);
    DEFEAT CONDITION: all planned signals individually asserted with explicit
    VERIFIED or UNVERIFIED state; no signal exits without assertion on record.
  P3-ADVERSARY: inertia toward coverage-blind verdicts (default when PHASE 3 is
    skipped: percent emitted without consistency guard verification);
    DEFEAT CONDITION: percent computed with consistency guard applied;
    UNVERIFIED-non-empty and percent-100% contradiction halted before verdict.
------------------------------------------------------------------------------

== OUTPUT TEMPLATE ==============================================================

[LAYER 1 -- STRUCTURAL: primary gap artifact; first section]
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
  ADVERSARY: inertia toward empty-glob assumption.
  DEFEAT CONDITION: DISK_SIGNALS populated from live glob result; zero-result
  case handled explicitly before PHASE 2 commitment assertion executes.
  Glob: simulations/**/{topic}-*
  Assign to DISK_SIGNALS.
  If empty: output "No signals found for {topic}" and stop.
  Record per match: path, namespace, signal name, date.

PHASE 2 -- PER-SIGNAL COMMITMENT ASSERTION
  ADVERSARY: inertia toward evidence-blind commits.
  DEFEAT CONDITION: all planned signals individually asserted with explicit
  VERIFIED or UNVERIFIED state; no signal exits without assertion on record.
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
    INVARIANT: Dual-axis gate.
      Trigger: file-absent when strategy.md absent; topic-absent when {topic} unregistered.
    OUTPUT FORM: VERIFIED | UNVERIFIED per planned signal; no batch evaluation.

PHASE 3 -- EXPOSURE COMPUTATION
  ADVERSARY: inertia toward coverage-blind verdicts.
  DEFEAT CONDITION: percent computed with consistency guard applied;
  UNVERIFIED-non-empty and percent-100% contradiction halted before verdict.
  percent = VERIFIED count / PLANNED count * 100
  Consistency guard: if UNVERIFIED non-empty and percent = 100%,
  halt and recompute.
  Readiness: >=80% READY | 50-79% PARTIAL | <50% NOT READY
  PHASE 3 OUTPUT DECLARATION:
    INVARIANT: Consistency guard -- UNVERIFIED-non-empty and percent-100%
      contradiction halts before readiness verdict.
      Trigger: guard fires when UNVERIFIED count > 0 and computed percent = 100%.
    OUTPUT FORM: percent (integer 0-100); readiness verdict
      (READY | PARTIAL | NOT READY).

PHASE 4 -- DISPLAY GATE
  STOP CONDITION:
    (1) COMMIT RISK REGISTER has one row per planned signal
    [P2-ADVERSARY DEFEAT:] all planned signals individually asserted with
      explicit VERIFIED or UNVERIFIED state on the record
    [P3-ADVERSARY DEFEAT:] percent computed with consistency guard applied;
      UNVERIFIED-non-empty and percent-100% contradiction halted before verdict
    [P1-ADVERSARY DEFEAT:] DISK_SIGNALS populated from live glob result;
      zero-result case handled explicitly before PHASE 2 commitment assertion
  Render in template section order.
  Write no files.
```

---

## Simplification Report

**Word count: 1073 → 854 (−219 words, 20.4% reduction)**

All essential criteria verified: YES

### What was removed and why

| # | Cut | Words saved | Reason |
|---|-----|-------------|--------|
| 1 | Criterion ID annotations `(C-21)`, `(C-24)`, `(C-26, C-27)` | 6 | Pure rubric meta-commentary; do no behavioral work in the executed prompt |
| 2 | Explanatory clause from [LAYER 2] line: `-- because PER-SIGNAL is the scope quantifier at left-edge position in the phase name` | 14 | Explains the rationale but doesn't constrain execution; the instruction stands without it |
| 3 | PHASE 2 dual-axis preamble trigger output message specs: `-- output unquantifiable-exposure message and stop immediately` / `-- output topic-specific stop message` | 12 | Output messages are already specified precisely in Exit A and Exit B; preamble only needs the trigger condition |
| 4 | OUTPUT DECLARATION CHAIN structural sub-component descriptions: `(PHASE 2 OUTPUT DECLARATION with INVARIANT: and OUTPUT FORM: labeled sub-components and per-axis Trigger: sentences within INVARIANT)` and parallel PHASE 3 text | 48 | These describe the form of what follows; the forms themselves appear in the execution phases and do the actual work |
| 5 | `"Each adversary is independently declared at its phase entry; no phase's adversary declaration implies any other's."` | 15 | Meta-commentary; the structural independence is already implicit in the per-entry form |
| 6 | Consequence-of-skipping text from execution-phase ADVERSARY blocks (all 3 phases) | 40 | C-46 requires `ADVERSARY: {name}` + `DEFEAT CONDITION:`. The consequence-of-skipping is C-47's preamble requirement; the execution ADVERSARY blocks don't need it |
| 7 | Execution DEFEAT CONDITION wording aligned to tighter preamble forms (phases 1–3) | 31 | Each execution DEFEAT CONDITION had longer phrasing than the preamble version; aligned without semantic loss |
| 8 | PHASE 4 STOP CONDITION predicate verbosity: `-- not from memory or prior-round assumption`; `detected and`; `readiness verdict issued` → `verdict` | 18 | Restatements of what "live glob result" and "halted" already assert |
| 9 | PHASE 2 OUTPUT DECLARATION INVARIANT body: `file-absent and topic-absent exits are structurally distinct stop conditions with distinct messages.` | 11 | Already declared verbatim in the preamble; INVARIANT label + Trigger carries the required structural signal |
| 10 | PHASE 3 OUTPUT DECLARATION: `contradiction halts computation before readiness verdict is issued` → `contradiction halts before readiness verdict` | 5 | Wordier form of the same halting predicate |
| 11 | [LAYER 1] annotation: `precedes EXPOSURE SUMMARY` | 3 | Positional annotation, not a structural declaration |

### Criteria verified as still passing

| Criterion | Structural element | Status |
|-----------|-------------------|--------|
| C-21 | Consequence-vocabulary phase names | PASS — all 4 names unchanged |
| C-24 | LAYER N vocabulary labels | PASS — all 3 LAYER labels unchanged |
| C-26/C-27 | [LAYER 2] full PER-SIGNAL form | PASS — preamble line retained |
| C-33/C-34 | Dual-axis exit pattern | PASS — preamble + Exit A/B unchanged; Trigger in OUTPUT DECLARATION |
| C-44 | OUTPUT DECLARATION CHAIN | PASS — preamble block + PHASE 2/3 OUTPUT DECLARATION sections present |
| C-45 | Preamble ADVERSARY CHAIN | PASS — block with all 3 labeled entries unchanged |
| C-46 | Execution ADVERSARY + DEFEAT CONDITION | PASS — both sub-components at PHASE 1/2/3 |
| C-47 | Preamble two-part labeled entries | PASS — all 3 entries have name + consequence-of-skipping |
| C-48 | PHASE 1 adversary body | PASS — ADVERSARY: + DEFEAT CONDITION: at PHASE 1 |
| C-49 | 4th STOP predicate | PASS — `[P1-ADVERSARY DEFEAT:]` present |
| C-50 | Phase-labeled STOP predicates | PASS — `[P1/P2/P3-ADVERSARY DEFEAT:]` all present |
| C-51 | Preamble DEFEAT CONDITION sub-components | PASS — all 3 preamble entries carry DEFEAT CONDITION: |

```json
{"simplified_word_count": 854, "original_word_count": 1073, "all_essential_still_pass": true}
```
