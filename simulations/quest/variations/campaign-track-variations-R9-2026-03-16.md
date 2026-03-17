Written to `simulations/quest/variations/campaign-track-variations-R9-2026-03-16.md`.

---

## Variations -- campaign-track / Round 9

**Baseline**: R8 V-05 (110/110). Two new criteria from R8 V-05's excellence signals:
- **C-29** — Order-dependent item annotation (behavior): terminal section closing note names `verdict_after` as "the only order-dependent item" and instructs "verify it last"
- **C-30** — Postcondition-linked contract annotation (format): Phase 3 header bridges both contracts to the postcondition semantics — "Both artifacts are required to satisfy the Phase 3 postcondition"

**Max score**: 116 (17 aspirational × 3 + 5 essential × 10 + 3 recommended × 5)

| ID | Axes | C-29 | C-30 | Expected score |
|----|------|------|------|----------------|
| **V-01** | C-29 only (terminal closing note) | PASS | FAIL | 113/116 |
| **V-02** | C-30 only (header postcondition bridge) | FAIL | PASS | 113/116 |
| **V-03** | C-29 via pre-terminal named section (contrast) | **SCOPING Q** | FAIL | 110 or 113 |
| **V-04** | C-29 + C-30 minimum-sufficient | PASS | PASS | 116/116 |
| **V-05** | C-29 + C-30 extended forms | PASS+ | PASS+ | 116/116 |

**Key question V-03 resolves**: Does C-29 require the annotation to be a closing note *within* the TERMINAL section, or does a `## Checklist Execution Order` section placed *before* the TERMINAL section also satisfy it? V-01 (inside) vs V-03 (before) — same semantic content, two structural positions.

**C-30 structural distinction**: C-26 names both contracts in the Phase 3 header. C-27 states the conjunction gate at the GATE statement. C-30 places "Both artifacts are required to satisfy the Phase 3 postcondition" *in the header itself* — bridging contract names to postcondition semantics at the execution site, not at the gate.

**V-05 extended forms** add: (1) the reasoning clause explaining *why* `verdict_after` is the only order-dependent item, and (2) an explicit FAIL consequence in the Phase 3 header. If C-29/C-30 are binary, V-04 = V-05; the V-05 patterns become R10 candidate criteria.
checklist execution
order. C-25 declares the two-pass write protocol; C-29 closes the loop by declaring
which terminal checklist items are temporally constrained and why -- at the
verification site, not at the write-order site. A model running the TERMINAL section
in sequence will encounter the ordering rule only if it is declared inside the
terminal section. V-01 tests whether this single annotation is sufficient to satisfy
C-29. Everything else at R8 V-05 baseline: Phase 3 header names both contracts
(C-26 pass) but omits the postcondition-linking bridge (C-30 miss).

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

---

## Dual-Contract Annotation Rule

When a phase produces artifacts under more than one contract, the active-role header
for that phase must name every governing contract. Naming one contract and omitting
others is a structural defect. Phase 3 produces status.md (Phase 3 Contract) and
delta.md (Session Delta Contract); both contracts must appear in the Phase 3 header.

---

## Two-Pass Delta Rule

delta.md is produced in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. Phase 4 has not run; verdict_after cannot be
determined yet.

Pass 2 (Post-Phase 4): Update delta.md by setting verdict_after to the verdict_verb
from story.md. This is the only post-Phase-4 write in the campaign.

The terminal checklist item for verdict_after is order-dependent: a placeholder value
in verdict_after after Phase 4 completes is a defect. "NOT YET REACHED" in verdict_after
fails the terminal check unless Phase 4 verdict_verb is also "NOT YET REACHED".

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Partial coverage
fails. Each field typed as integer must contain an integer. Each field typed as
enumerated string must contain exactly one of the listed tokens.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md

- topic_name: string (non-empty, human-readable)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item:
  - signal_name: string (unique within strategy)
  - target_skill: string (namespace/skill format, e.g. "scout/scout-competitors")
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches signal_name from strategy.md)
    - collection_purpose: string (one sentence: why this signal matters)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0 (no prose, no ranges)
  - collected: integer >= 0 (no prose, no ranges)
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N" (X and N are integers)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md

- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

---

## Session Delta Contract -- delta.md

- session_number: integer >= 1
- signals_added: list of signal names collected this session;
  empty list [] if no signals added -- string "NONE" is not a valid value
- signals_removed: list of signal names removed this session;
  empty list [] if no signals removed -- string "NONE" is not a valid value
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
  (NONE = no prior session verdict; not a list -- this field is string-typed)
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
  (Pass 1 placeholder: "NOT YET REACHED" until Phase 4 completes)
- verdict_changed: string, exactly one of: YES | NO | N/A

---

## Prohibition Parity Rule

Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no
fewer. This count is fixed. A role with 4 or 6 items is structurally invalid and
fails audit. The numbered list format is required: each item labeled 1 through 5.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)

Owns strategy.md. Produces Phase 1 Contract output.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content across sources
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not declared in the strategy planned_signals field

### Planner (Phase 2 -- topic-plan)

Owns roadmap.md. Produces Phase 2 Contract output.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify the topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs from Phase 4 vocabulary
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)

Owns status.md AND delta.md. Produces Phase 3 Contract and Session Delta Contract output.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond what Phase 2 roadmap defines
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize on findings
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "a few", "many") where integers are
   required by contract

### Narrator (Phase 4 -- topic-story)

Owns story.md. Produces Phase 4 Contract output.

Forbidden actions (exactly 5):
1. Must not modify the coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid;
   "likely confirmed" or "essentially confirmed" both fail

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract:
- topic_name (string), namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields present and
typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply.*
*Phase 3 Contract governs status.md. Session Delta Contract governs delta.md.*

Phase 3 produces two artifacts under two contracts (see Dual-Contract Annotation
Rule). Both contracts are active at this phase.

### Step A -- Coverage Status

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present -- no row skipped
- planned and collected are integers -- narrative counts fail
- missing lists each signal by name -- counts alone fail
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md conforming to Session Delta Contract.

Two-pass protocol applies:
- Set verdict_after = "NOT YET REACHED" (placeholder -- Phase 4 has not run)
- All other fields are final at this step:
  - session_number: integer
  - signals_added: list ([] if none -- string "NONE" is invalid)
  - signals_removed: list ([] if none -- string "NONE" is invalid)
  - verdict_before: prior session readiness_verdict, or "NONE" for first session
  - verdict_changed: "N/A" for first session; defer to Pass 2 for subsequent sessions

Write delta to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md are BOTH present, each satisfying
their respective contracts. Writing status.md alone does not satisfy this
postcondition. A delta.md with missing fields or invalid types fails.

GATE: Do not proceed to Phase 4 until BOTH status.md AND delta.md satisfy their
contracts.

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (no paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, update delta.md (this is the only post-Phase-4 write):

- Set verdict_after = verdict_verb from story.md (replaces "NOT YET REACHED" placeholder)
- For subsequent sessions (session_number >= 2): set verdict_changed = YES if
  verdict_after != verdict_before; NO if equal
- For first session (verdict_before = NONE): verdict_changed = "N/A" (no prior to compare)

Update: simulations/topic/{{topic}}-delta-{{date}}.md

An un-updated placeholder in verdict_after is a terminal defect caught by the
checklist item for verdict_after.

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. planned_signals must
  list >= 3 entries.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals are planned;
  none collected.

Phase 3 (Analyst) [both contracts active]:
  Step A: All rows have collected = 0 (integer). missing lists all planned signals
    from roadmap.md by signal_name. zero_flag = "NO SIGNALS" where applicable.
    readiness_verdict = "NOT READY".
  Step B: session_number = 1. signals_added = [] (empty list -- NOT the string "NONE").
    signals_removed = []. verdict_before = "NONE" (string sentinel for first session --
    this field is string-typed, unlike signals_added which is list-typed).
    verdict_after = "NOT YET REACHED" (placeholder). verdict_changed = "N/A".
  Conjunction gate requires both artifacts before Phase 4.

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. next_signal_recommendations: top 3 from
  roadmap.md ordered by planned priority.

Post-Phase-4 update: verdict_after updated from placeholder to "NOT YET REACHED"
  (verdict_verb from Phase 4 -- coincides with placeholder for first invocation).
  verdict_changed remains "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently before marking the campaign complete. Each item
names a specific artifact field and its constraint. A field that satisfies the
constraint PASSES. A field that fails triggers re-run of the affected phase only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty
    FAIL: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low}
    FAIL: re-run Phase 1

[ ] planned_signals: count >= 3 (integer count, not estimated)
    FAIL: re-run Phase 1

[ ] planned_signals[*].target_skill: each in namespace/skill format
    FAIL: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_coverage: at least one entry present
    FAIL: re-run Phase 2

[ ] namespace_coverage[*].collection_purpose: string present per signal (not omitted)
    FAIL: re-run Phase 2

### Phase 3 -- status.md

[ ] row count: exactly 9 namespace rows present
    FAIL: re-run Phase 3

[ ] planned: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] collected: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] missing: list of signal names in each row (not a count -- names required)
    FAIL: re-run Phase 3

[ ] zero_flag: "NO SIGNALS" present for every row where planned = 0 AND collected = 0
    FAIL: re-run Phase 3

[ ] coverage_ratio: "X/N" format (X and N are both integers)
    FAIL: re-run Phase 3

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL: re-run Phase 3

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.s0: string present, non-empty
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.current: string present ("UNCHANGED" or updated hypothesis)
    FAIL: re-run Phase 4

[ ] echoes: list present with at least one entry (minimum ["NONE"])
    FAIL: re-run Phase 4

[ ] next_signal_recommendations: exactly 3 items
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].namespace: string present for all 3
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].gap_reason: string present for all 3
    FAIL: re-run Phase 4

### Session Delta -- delta.md

[ ] session_number: integer >= 1
    FAIL: re-run Phase 3 Step B

[ ] signals_added: list present ([] permitted; absent field or string "NONE" fails --
    the empty-list type [] is required, not the string sentinel)
    FAIL: re-run Phase 3 Step B

[ ] signals_removed: list present ([] permitted; absent field or string "NONE" fails)
    FAIL: re-run Phase 3 Step B

[ ] verdict_before: exactly one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    (string "NONE" is valid here -- this field is string-typed, not list-typed)
    FAIL: re-run Phase 3 Step B

[ ] verdict_after: exactly one of {READY|NOT READY|CONDITIONALLY READY|NOT YET REACHED};
    must reflect Phase 4 verdict_verb after Pass 2 completes; placeholder "NOT YET
    REACHED" fails after Phase 4 unless Phase 4 verdict_verb is also "NOT YET REACHED"
    FAIL: re-run Phase 3 Step B after Phase 4 completes (Pass 2)

[ ] verdict_changed: exactly one of {YES|NO|N/A}
    FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign is complete. Dashboard ready to emit.
Any item FAIL: re-run the affected phase. Re-verify the failed item only.
The verdict_after item is the only order-dependent item: verify it last, after
Phase 4 and the Post-Phase-4 Delta Update have both completed.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-28 (full R8 V-05 baseline), C-29 (terminal
closing note: "The verdict_after item is the only order-dependent item: verify it
last, after Phase 4 and the Post-Phase-4 Delta Update have both completed").
**Misses**: C-30 (Phase 3 header names both contracts per C-26, but omits the
postcondition-linking bridge: "Both artifacts are required to satisfy the Phase 3
postcondition" is absent from the header annotation).
**Risk**: Closing note appears after "Any item FAIL" -- a model scanning the
terminal section may not process it as normative if it treats the completion/failure
lines as the terminal boundary. The note must be read as part of the terminal
section, not appended commentary.

---

## V-02 -- Axis: Postcondition-linked contract annotation (C-30 maximum)

**Hypothesis**: Bridging the Phase 3 active-role header to state "Both artifacts are
required to satisfy the Phase 3 postcondition" creates a single-site enforcement
point where the model sees contract names, postcondition dependency, and the Phase 4
unlock implication in one location. C-26 names both contracts; C-27 states the
conjunction gate at the postcondition/GATE section; C-30 places the postcondition
link at the header -- the highest-visibility location in the phase execution block.
V-02 tests whether this header-level bridge alone improves Phase 3 completeness.
Phase 3 header has the bridge (C-30 pass); terminal section has no closing
order-dependency note (C-29 miss).

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

---

## Dual-Contract Annotation Rule

When a phase produces artifacts under more than one contract, the active-role header
for that phase must name every governing contract. Naming one contract and omitting
others is a structural defect. Phase 3 produces status.md (Phase 3 Contract) and
delta.md (Session Delta Contract); both contracts must appear in the Phase 3 header.

---

## Two-Pass Delta Rule

delta.md is produced in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. Phase 4 has not run; verdict_after cannot be
determined yet.

Pass 2 (Post-Phase 4): Update delta.md by setting verdict_after to the verdict_verb
from story.md. This is the only post-Phase-4 write in the campaign.

The terminal checklist item for verdict_after is order-dependent: a placeholder value
in verdict_after after Phase 4 completes is a defect. "NOT YET REACHED" in verdict_after
fails the terminal check unless Phase 4 verdict_verb is also "NOT YET REACHED".

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Partial coverage
fails. Each field typed as integer must contain an integer. Each field typed as
enumerated string must contain exactly one of the listed tokens.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md

- topic_name: string (non-empty, human-readable)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item:
  - signal_name: string (unique within strategy)
  - target_skill: string (namespace/skill format, e.g. "scout/scout-competitors")
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches signal_name from strategy.md)
    - collection_purpose: string (one sentence: why this signal matters)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0 (no prose, no ranges)
  - collected: integer >= 0 (no prose, no ranges)
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N" (X and N are integers)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md

- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

---

## Session Delta Contract -- delta.md

- session_number: integer >= 1
- signals_added: list of signal names collected this session;
  empty list [] if no signals added -- string "NONE" is not a valid value
- signals_removed: list of signal names removed this session;
  empty list [] if no signals removed -- string "NONE" is not a valid value
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
  (NONE = no prior session verdict; not a list -- this field is string-typed)
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
  (Pass 1 placeholder: "NOT YET REACHED" until Phase 4 completes)
- verdict_changed: string, exactly one of: YES | NO | N/A

---

## Prohibition Parity Rule

Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no
fewer. This count is fixed. A role with 4 or 6 items is structurally invalid and
fails audit. The numbered list format is required: each item labeled 1 through 5.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)

Owns strategy.md. Produces Phase 1 Contract output.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content across sources
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not declared in the strategy planned_signals field

### Planner (Phase 2 -- topic-plan)

Owns roadmap.md. Produces Phase 2 Contract output.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify the topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs from Phase 4 vocabulary
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)

Owns status.md AND delta.md. Produces Phase 3 Contract and Session Delta Contract output.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond what Phase 2 roadmap defines
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize on findings
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "a few", "many") where integers are
   required by contract

### Narrator (Phase 4 -- topic-story)

Owns story.md. Produces Phase 4 Contract output.

Forbidden actions (exactly 5):
1. Must not modify the coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid;
   "likely confirmed" or "essentially confirmed" both fail

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract:
- topic_name (string), namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields present and
typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply.*
*Phase 3 Contract governs status.md. Session Delta Contract governs delta.md.*

Phase 3 produces two artifacts under two contracts (see Dual-Contract Annotation
Rule). Both contracts are active at this phase. Both artifacts are required to
satisfy the Phase 3 postcondition.

### Step A -- Coverage Status

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present -- no row skipped
- planned and collected are integers -- narrative counts fail
- missing lists each signal by name -- counts alone fail
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md conforming to Session Delta Contract.

Two-pass protocol applies:
- Set verdict_after = "NOT YET REACHED" (placeholder -- Phase 4 has not run)
- All other fields are final at this step:
  - session_number: integer
  - signals_added: list ([] if none -- string "NONE" is invalid)
  - signals_removed: list ([] if none -- string "NONE" is invalid)
  - verdict_before: prior session readiness_verdict, or "NONE" for first session
  - verdict_changed: "N/A" for first session; defer to Pass 2 for subsequent sessions

Write delta to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md are BOTH present, each satisfying
their respective contracts. Writing status.md alone does not satisfy this
postcondition. A delta.md with missing fields or invalid types fails.

GATE: Do not proceed to Phase 4 until BOTH status.md AND delta.md satisfy their
contracts.

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (no paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, update delta.md (this is the only post-Phase-4 write):

- Set verdict_after = verdict_verb from story.md (replaces "NOT YET REACHED" placeholder)
- For subsequent sessions (session_number >= 2): set verdict_changed = YES if
  verdict_after != verdict_before; NO if equal
- For first session (verdict_before = NONE): verdict_changed = "N/A" (no prior to compare)

Update: simulations/topic/{{topic}}-delta-{{date}}.md

An un-updated placeholder in verdict_after is a terminal defect caught by the
checklist item for verdict_after.

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. planned_signals must
  list >= 3 entries.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals are planned;
  none collected.

Phase 3 (Analyst) [both contracts active]:
  Step A: All rows have collected = 0 (integer). missing lists all planned signals
    from roadmap.md by signal_name. zero_flag = "NO SIGNALS" where applicable.
    readiness_verdict = "NOT READY".
  Step B: session_number = 1. signals_added = [] (empty list -- NOT the string "NONE").
    signals_removed = []. verdict_before = "NONE" (string sentinel for first session --
    this field is string-typed, unlike signals_added which is list-typed).
    verdict_after = "NOT YET REACHED" (placeholder). verdict_changed = "N/A".
  Conjunction gate requires both artifacts before Phase 4.

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. next_signal_recommendations: top 3 from
  roadmap.md ordered by planned priority.

Post-Phase-4 update: verdict_after updated from placeholder to "NOT YET REACHED"
  (verdict_verb from Phase 4 -- coincides with placeholder for first invocation).
  verdict_changed remains "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently before marking the campaign complete. Each item
names a specific artifact field and its constraint. A field that satisfies the
constraint PASSES. A field that fails triggers re-run of the affected phase only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty
    FAIL: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low}
    FAIL: re-run Phase 1

[ ] planned_signals: count >= 3 (integer count, not estimated)
    FAIL: re-run Phase 1

[ ] planned_signals[*].target_skill: each in namespace/skill format
    FAIL: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_coverage: at least one entry present
    FAIL: re-run Phase 2

[ ] namespace_coverage[*].collection_purpose: string present per signal (not omitted)
    FAIL: re-run Phase 2

### Phase 3 -- status.md

[ ] row count: exactly 9 namespace rows present
    FAIL: re-run Phase 3

[ ] planned: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] collected: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] missing: list of signal names in each row (not a count -- names required)
    FAIL: re-run Phase 3

[ ] zero_flag: "NO SIGNALS" present for every row where planned = 0 AND collected = 0
    FAIL: re-run Phase 3

[ ] coverage_ratio: "X/N" format (X and N are both integers)
    FAIL: re-run Phase 3

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL: re-run Phase 3

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.s0: string present, non-empty
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.current: string present ("UNCHANGED" or updated hypothesis)
    FAIL: re-run Phase 4

[ ] echoes: list present with at least one entry (minimum ["NONE"])
    FAIL: re-run Phase 4

[ ] next_signal_recommendations: exactly 3 items
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].namespace: string present for all 3
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].gap_reason: string present for all 3
    FAIL: re-run Phase 4

### Session Delta -- delta.md

[ ] session_number: integer >= 1
    FAIL: re-run Phase 3 Step B

[ ] signals_added: list present ([] permitted; absent field or string "NONE" fails --
    the empty-list type [] is required, not the string sentinel)
    FAIL: re-run Phase 3 Step B

[ ] signals_removed: list present ([] permitted; absent field or string "NONE" fails)
    FAIL: re-run Phase 3 Step B

[ ] verdict_before: exactly one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    (string "NONE" is valid here -- this field is string-typed, not list-typed)
    FAIL: re-run Phase 3 Step B

[ ] verdict_after: exactly one of {READY|NOT READY|CONDITIONALLY READY|NOT YET REACHED};
    must reflect Phase 4 verdict_verb after Pass 2 completes; placeholder "NOT YET
    REACHED" fails after Phase 4 unless Phase 4 verdict_verb is also "NOT YET REACHED"
    FAIL: re-run Phase 3 Step B after Phase 4 completes (Pass 2)

[ ] verdict_changed: exactly one of {YES|NO|N/A}
    FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign is complete. Dashboard ready to emit.
Any item FAIL: re-run the affected phase. Re-verify the failed item only.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-28 (full R8 V-05 baseline), C-30 (Phase 3
active-role header: "Both contracts are active at this phase. Both artifacts are
required to satisfy the Phase 3 postcondition." -- bridges the dual-contract
declaration to the postcondition semantics at the execution site; distinct from
C-26 which names both contracts and C-27 which states the conjunction gate at the
postcondition/GATE section).
**Misses**: C-29 (terminal section ends with "Any item FAIL: re-run the affected
phase" with no closing note naming verdict_after as the only order-dependent item).
**Risk**: C-30 is a format criterion at the header level. Enforcement depends on
whether the model reads the header annotation before executing Step B. C-27's GATE
statement remains the primary behavioral enforcement; C-30 is the normative
declaration of the same constraint at the role activation site.

---

## V-03 -- Axis: C-29 via pre-terminal named section (structural scoping contrast)

**Hypothesis**: C-29's pass condition names verdict_after as the only order-dependent
item and instructs verify-last. The R8 V-05 implementation and V-01 above satisfy
this as a trailing note AFTER the terminal checklist items. V-03 tests whether the
same semantic content -- delivered as a dedicated `## Checklist Execution Order`
section placed BEFORE the TERMINAL section -- also satisfies C-29, or whether C-29
requires the annotation to be structurally part of the terminal section's closing
material. This is a structural scoping test: if C-29 requires terminal-section
placement, V-03 fails; if presence anywhere in the prompt satisfies C-29, V-03 and
V-01 score identically. V-03 also misses C-30 (same as V-01).

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

---

## Dual-Contract Annotation Rule

When a phase produces artifacts under more than one contract, the active-role header
for that phase must name every governing contract. Naming one contract and omitting
others is a structural defect. Phase 3 produces status.md (Phase 3 Contract) and
delta.md (Session Delta Contract); both contracts must appear in the Phase 3 header.

---

## Two-Pass Delta Rule

delta.md is produced in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. Phase 4 has not run; verdict_after cannot be
determined yet.

Pass 2 (Post-Phase 4): Update delta.md by setting verdict_after to the verdict_verb
from story.md. This is the only post-Phase-4 write in the campaign.

The terminal checklist item for verdict_after is order-dependent: a placeholder value
in verdict_after after Phase 4 completes is a defect.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Partial coverage
fails. Each field typed as integer must contain an integer. Each field typed as
enumerated string must contain exactly one of the listed tokens.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md

- topic_name: string (non-empty, human-readable)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item:
  - signal_name: string (unique within strategy)
  - target_skill: string (namespace/skill format, e.g. "scout/scout-competitors")
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches signal_name from strategy.md)
    - collection_purpose: string (one sentence: why this signal matters)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0 (no prose, no ranges)
  - collected: integer >= 0 (no prose, no ranges)
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N" (X and N are integers)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md

- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

---

## Session Delta Contract -- delta.md

- session_number: integer >= 1
- signals_added: list of signal names collected this session;
  empty list [] if no signals added -- string "NONE" is not a valid value
- signals_removed: list of signal names removed this session;
  empty list [] if no signals removed -- string "NONE" is not a valid value
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
  (NONE = no prior session verdict; not a list -- this field is string-typed)
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
  (Pass 1 placeholder: "NOT YET REACHED" until Phase 4 completes)
- verdict_changed: string, exactly one of: YES | NO | N/A

---

## Prohibition Parity Rule

Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no
fewer. This count is fixed. A role with 4 or 6 items is structurally invalid and
fails audit. The numbered list format is required: each item labeled 1 through 5.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)

Owns strategy.md. Produces Phase 1 Contract output.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content across sources
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not declared in the strategy planned_signals field

### Planner (Phase 2 -- topic-plan)

Owns roadmap.md. Produces Phase 2 Contract output.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify the topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs from Phase 4 vocabulary
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)

Owns status.md AND delta.md. Produces Phase 3 Contract and Session Delta Contract output.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond what Phase 2 roadmap defines
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize on findings
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "a few", "many") where integers are
   required by contract

### Narrator (Phase 4 -- topic-story)

Owns story.md. Produces Phase 4 Contract output.

Forbidden actions (exactly 5):
1. Must not modify the coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid;
   "likely confirmed" or "essentially confirmed" both fail

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract:
- topic_name (string), namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields present and
typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply.*
*Phase 3 Contract governs status.md. Session Delta Contract governs delta.md.*

Phase 3 produces two artifacts under two contracts (see Dual-Contract Annotation
Rule). Both contracts are active at this phase.

### Step A -- Coverage Status

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present -- no row skipped
- planned and collected are integers -- narrative counts fail
- missing lists each signal by name -- counts alone fail
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md conforming to Session Delta Contract.

Two-pass protocol applies:
- Set verdict_after = "NOT YET REACHED" (placeholder -- Phase 4 has not run)
- All other fields are final at this step:
  - session_number: integer
  - signals_added: list ([] if none -- string "NONE" is invalid)
  - signals_removed: list ([] if none -- string "NONE" is invalid)
  - verdict_before: prior session readiness_verdict, or "NONE" for first session
  - verdict_changed: "N/A" for first session; defer to Pass 2 for subsequent sessions

Write delta to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md are BOTH present, each satisfying
their respective contracts. Writing status.md alone does not satisfy this
postcondition. A delta.md with missing fields or invalid types fails.

GATE: Do not proceed to Phase 4 until BOTH status.md AND delta.md satisfy their
contracts.

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (no paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, update delta.md (this is the only post-Phase-4 write):

- Set verdict_after = verdict_verb from story.md (replaces "NOT YET REACHED" placeholder)
- For subsequent sessions (session_number >= 2): set verdict_changed = YES if
  verdict_after != verdict_before; NO if equal
- For first session (verdict_before = NONE): verdict_changed = "N/A" (no prior to compare)

Update: simulations/topic/{{topic}}-delta-{{date}}.md

An un-updated placeholder in verdict_after is a terminal defect caught by the
checklist item for verdict_after.

---

## Checklist Execution Order

The verdict_after item is the only order-dependent item in the terminal checklist.
It must be verified last -- after Phase 4 and the Post-Phase-4 Delta Update have
both completed. Verifying verdict_after before Phase 4 runs produces a false pass:
the placeholder value "NOT YET REACHED" satisfies the token set but does not reflect
the actual Phase 4 verdict. All other checklist items are order-independent and may
be verified in any sequence after their respective phase writes.

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. planned_signals must
  list >= 3 entries.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals are planned;
  none collected.

Phase 3 (Analyst) [both contracts active]:
  Step A: All rows have collected = 0 (integer). missing lists all planned signals
    from roadmap.md by signal_name. zero_flag = "NO SIGNALS" where applicable.
    readiness_verdict = "NOT READY".
  Step B: session_number = 1. signals_added = [] (empty list -- NOT the string "NONE").
    signals_removed = []. verdict_before = "NONE" (string sentinel for first session --
    this field is string-typed, unlike signals_added which is list-typed).
    verdict_after = "NOT YET REACHED" (placeholder). verdict_changed = "N/A".
  Conjunction gate requires both artifacts before Phase 4.

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. next_signal_recommendations: top 3 from
  roadmap.md ordered by planned priority.

Post-Phase-4 update: verdict_after updated from placeholder to "NOT YET REACHED"
  (verdict_verb from Phase 4 -- coincides with placeholder for first invocation).
  verdict_changed remains "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently before marking the campaign complete. Each item
names a specific artifact field and its constraint. A field that satisfies the
constraint PASSES. A field that fails triggers re-run of the affected phase only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty
    FAIL: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low}
    FAIL: re-run Phase 1

[ ] planned_signals: count >= 3 (integer count, not estimated)
    FAIL: re-run Phase 1

[ ] planned_signals[*].target_skill: each in namespace/skill format
    FAIL: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_coverage: at least one entry present
    FAIL: re-run Phase 2

[ ] namespace_coverage[*].collection_purpose: string present per signal (not omitted)
    FAIL: re-run Phase 2

### Phase 3 -- status.md

[ ] row count: exactly 9 namespace rows present
    FAIL: re-run Phase 3

[ ] planned: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] collected: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] missing: list of signal names in each row (not a count -- names required)
    FAIL: re-run Phase 3

[ ] zero_flag: "NO SIGNALS" present for every row where planned = 0 AND collected = 0
    FAIL: re-run Phase 3

[ ] coverage_ratio: "X/N" format (X and N are both integers)
    FAIL: re-run Phase 3

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL: re-run Phase 3

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.s0: string present, non-empty
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.current: string present ("UNCHANGED" or updated hypothesis)
    FAIL: re-run Phase 4

[ ] echoes: list present with at least one entry (minimum ["NONE"])
    FAIL: re-run Phase 4

[ ] next_signal_recommendations: exactly 3 items
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].namespace: string present for all 3
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].gap_reason: string present for all 3
    FAIL: re-run Phase 4

### Session Delta -- delta.md

[ ] session_number: integer >= 1
    FAIL: re-run Phase 3 Step B

[ ] signals_added: list present ([] permitted; absent field or string "NONE" fails --
    the empty-list type [] is required, not the string sentinel)
    FAIL: re-run Phase 3 Step B

[ ] signals_removed: list present ([] permitted; absent field or string "NONE" fails)
    FAIL: re-run Phase 3 Step B

[ ] verdict_before: exactly one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    (string "NONE" is valid here -- this field is string-typed, not list-typed)
    FAIL: re-run Phase 3 Step B

[ ] verdict_after: exactly one of {READY|NOT READY|CONDITIONALLY READY|NOT YET REACHED};
    must reflect Phase 4 verdict_verb after Pass 2 completes; placeholder "NOT YET
    REACHED" fails after Phase 4 unless Phase 4 verdict_verb is also "NOT YET REACHED"
    FAIL: re-run Phase 3 Step B after Phase 4 completes (Pass 2)

[ ] verdict_changed: exactly one of {YES|NO|N/A}
    FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign is complete. Dashboard ready to emit.
Any item FAIL: re-run the affected phase. Re-verify the failed item only.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-28 (full R8 V-05 baseline). Attempts C-29 via
a dedicated `## Checklist Execution Order` section placed BEFORE the terminal
section, naming verdict_after as "the only order-dependent item" and instructing
verify-last with explanation of why early verification produces a false pass.
**Misses (expected)**: C-29 (section declares correct semantic content but is NOT
placed within the TERMINAL section itself; if C-29 requires the annotation as the
terminal section's closing note, this fails; this is the structural scoping
hypothesis being tested). C-30 (same miss as V-01).
**Risk**: V-03 is explicitly designed as a structural contrast to V-01. The expected
outcome is C-29 FAIL -- the information is present but not at the terminal closing
site. V-01 (trailing note inside terminal section) vs V-03 (named section before
terminal) will resolve whether C-29's scoping requirement is positional (within
terminal section) or semantic (anywhere in prompt). If V-03 passes C-29 and ties
V-01, the criterion needs refinement to require terminal-section placement.

---

## V-04 -- Combined: C-29 + C-30 (minimum-sufficient forms)

**Combined axes**: Order-dependent item annotation (C-29) + Postcondition-linked
contract annotation (C-30)

**Hypothesis**: C-29 and C-30 address different structural locations (terminal
closing vs. Phase 3 header) and different enforcement mechanisms (checklist execution
order vs. contract-to-postcondition link). Neither interferes with the other;
applying both on the R8 V-05 baseline should produce a prompt scoring all 17 criteria
(116/116). C-30 at the header site tells the model both artifacts are postcondition-
gated; C-29 at the terminal site tells the model verification order for the one
temporally-constrained item. V-04 uses the minimum-sufficient forms of both criteria
before V-05 tests extended forms.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

---

## Dual-Contract Annotation Rule

When a phase produces artifacts under more than one contract, the active-role header
for that phase must name every governing contract. Naming one contract and omitting
others is a structural defect. Phase 3 produces status.md (Phase 3 Contract) and
delta.md (Session Delta Contract); both contracts must appear in the Phase 3 header.

---

## Two-Pass Delta Rule

delta.md is produced in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. Phase 4 has not run; verdict_after cannot be
determined yet.

Pass 2 (Post-Phase 4): Update delta.md by setting verdict_after to the verdict_verb
from story.md. This is the only post-Phase-4 write in the campaign.

The terminal checklist item for verdict_after is order-dependent: a placeholder value
in verdict_after after Phase 4 completes is a defect. "NOT YET REACHED" in verdict_after
fails the terminal check unless Phase 4 verdict_verb is also "NOT YET REACHED".

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Partial coverage
fails. Each field typed as integer must contain an integer. Each field typed as
enumerated string must contain exactly one of the listed tokens.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md

- topic_name: string (non-empty, human-readable)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item:
  - signal_name: string (unique within strategy)
  - target_skill: string (namespace/skill format, e.g. "scout/scout-competitors")
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches signal_name from strategy.md)
    - collection_purpose: string (one sentence: why this signal matters)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0 (no prose, no ranges)
  - collected: integer >= 0 (no prose, no ranges)
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N" (X and N are integers)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md

- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

---

## Session Delta Contract -- delta.md

- session_number: integer >= 1
- signals_added: list of signal names collected this session;
  empty list [] if no signals added -- string "NONE" is not a valid value
- signals_removed: list of signal names removed this session;
  empty list [] if no signals removed -- string "NONE" is not a valid value
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
  (NONE = no prior session verdict; not a list -- this field is string-typed)
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
  (Pass 1 placeholder: "NOT YET REACHED" until Phase 4 completes)
- verdict_changed: string, exactly one of: YES | NO | N/A

---

## Prohibition Parity Rule

Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no
fewer. This count is fixed. A role with 4 or 6 items is structurally invalid and
fails audit. The numbered list format is required: each item labeled 1 through 5.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)

Owns strategy.md. Produces Phase 1 Contract output.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content across sources
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not declared in the strategy planned_signals field

### Planner (Phase 2 -- topic-plan)

Owns roadmap.md. Produces Phase 2 Contract output.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify the topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs from Phase 4 vocabulary
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)

Owns status.md AND delta.md. Produces Phase 3 Contract and Session Delta Contract output.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond what Phase 2 roadmap defines
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize on findings
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "a few", "many") where integers are
   required by contract

### Narrator (Phase 4 -- topic-story)

Owns story.md. Produces Phase 4 Contract output.

Forbidden actions (exactly 5):
1. Must not modify the coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid;
   "likely confirmed" or "essentially confirmed" both fail

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract:
- topic_name (string), namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields present and
typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply.*
*Phase 3 Contract governs status.md. Session Delta Contract governs delta.md.*

Phase 3 produces two artifacts under two contracts (see Dual-Contract Annotation
Rule). Both contracts are active at this phase. Both artifacts are required to
satisfy the Phase 3 postcondition.

### Step A -- Coverage Status

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present -- no row skipped
- planned and collected are integers -- narrative counts fail
- missing lists each signal by name -- counts alone fail
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md conforming to Session Delta Contract.

Two-pass protocol applies:
- Set verdict_after = "NOT YET REACHED" (placeholder -- Phase 4 has not run)
- All other fields are final at this step:
  - session_number: integer
  - signals_added: list ([] if none -- string "NONE" is invalid)
  - signals_removed: list ([] if none -- string "NONE" is invalid)
  - verdict_before: prior session readiness_verdict, or "NONE" for first session
  - verdict_changed: "N/A" for first session; defer to Pass 2 for subsequent sessions

Write delta to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md are BOTH present, each satisfying
their respective contracts. Writing status.md alone does not satisfy this
postcondition. A delta.md with missing fields or invalid types fails.

GATE: Do not proceed to Phase 4 until BOTH status.md AND delta.md satisfy their
contracts.

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (no paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, update delta.md (this is the only post-Phase-4 write):

- Set verdict_after = verdict_verb from story.md (replaces "NOT YET REACHED" placeholder)
- For subsequent sessions (session_number >= 2): set verdict_changed = YES if
  verdict_after != verdict_before; NO if equal
- For first session (verdict_before = NONE): verdict_changed = "N/A" (no prior to compare)

Update: simulations/topic/{{topic}}-delta-{{date}}.md

An un-updated placeholder in verdict_after is a terminal defect caught by the
checklist item for verdict_after.

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. planned_signals must
  list >= 3 entries.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals are planned;
  none collected.

Phase 3 (Analyst) [both contracts active]:
  Step A: All rows have collected = 0 (integer). missing lists all planned signals
    from roadmap.md by signal_name. zero_flag = "NO SIGNALS" where applicable.
    readiness_verdict = "NOT READY".
  Step B: session_number = 1. signals_added = [] (empty list -- NOT the string "NONE").
    signals_removed = []. verdict_before = "NONE" (string sentinel for first session --
    this field is string-typed, unlike signals_added which is list-typed).
    verdict_after = "NOT YET REACHED" (placeholder). verdict_changed = "N/A".
  Conjunction gate requires both artifacts before Phase 4.

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. next_signal_recommendations: top 3 from
  roadmap.md ordered by planned priority.

Post-Phase-4 update: verdict_after updated from placeholder to "NOT YET REACHED"
  (verdict_verb from Phase 4 -- coincides with placeholder for first invocation).
  verdict_changed remains "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently before marking the campaign complete. Each item
names a specific artifact field and its constraint. A field that satisfies the
constraint PASSES. A field that fails triggers re-run of the affected phase only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty
    FAIL: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low}
    FAIL: re-run Phase 1

[ ] planned_signals: count >= 3 (integer count, not estimated)
    FAIL: re-run Phase 1

[ ] planned_signals[*].target_skill: each in namespace/skill format
    FAIL: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_coverage: at least one entry present
    FAIL: re-run Phase 2

[ ] namespace_coverage[*].collection_purpose: string present per signal (not omitted)
    FAIL: re-run Phase 2

### Phase 3 -- status.md

[ ] row count: exactly 9 namespace rows present
    FAIL: re-run Phase 3

[ ] planned: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] collected: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] missing: list of signal names in each row (not a count -- names required)
    FAIL: re-run Phase 3

[ ] zero_flag: "NO SIGNALS" present for every row where planned = 0 AND collected = 0
    FAIL: re-run Phase 3

[ ] coverage_ratio: "X/N" format (X and N are both integers)
    FAIL: re-run Phase 3

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL: re-run Phase 3

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.s0: string present, non-empty
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.current: string present ("UNCHANGED" or updated hypothesis)
    FAIL: re-run Phase 4

[ ] echoes: list present with at least one entry (minimum ["NONE"])
    FAIL: re-run Phase 4

[ ] next_signal_recommendations: exactly 3 items
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].namespace: string present for all 3
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].gap_reason: string present for all 3
    FAIL: re-run Phase 4

### Session Delta -- delta.md

[ ] session_number: integer >= 1
    FAIL: re-run Phase 3 Step B

[ ] signals_added: list present ([] permitted; absent field or string "NONE" fails --
    the empty-list type [] is required, not the string sentinel)
    FAIL: re-run Phase 3 Step B

[ ] signals_removed: list present ([] permitted; absent field or string "NONE" fails)
    FAIL: re-run Phase 3 Step B

[ ] verdict_before: exactly one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    (string "NONE" is valid here -- this field is string-typed, not list-typed)
    FAIL: re-run Phase 3 Step B

[ ] verdict_after: exactly one of {READY|NOT READY|CONDITIONALLY READY|NOT YET REACHED};
    must reflect Phase 4 verdict_verb after Pass 2 completes; placeholder "NOT YET
    REACHED" fails after Phase 4 unless Phase 4 verdict_verb is also "NOT YET REACHED"
    FAIL: re-run Phase 3 Step B after Phase 4 completes (Pass 2)

[ ] verdict_changed: exactly one of {YES|NO|N/A}
    FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign is complete. Dashboard ready to emit.
Any item FAIL: re-run the affected phase. Re-verify the failed item only.
The verdict_after item is the only order-dependent item: verify it last, after
Phase 4 and the Post-Phase-4 Delta Update have both completed.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-28 (full R8 V-05 baseline), C-29 (terminal
closing note: "The verdict_after item is the only order-dependent item: verify it
last, after Phase 4 and the Post-Phase-4 Delta Update have both completed"),
C-30 (Phase 3 active-role header: "Both contracts are active at this phase. Both
artifacts are required to satisfy the Phase 3 postcondition.").
**Misses**: Nothing expected. V-04 is the clean minimum-sufficient combination.
**Risk**: If V-04 ties V-05 at 116/116, the extended forms in V-05 are redundant
overhead and the next rubric revision should look for criteria orthogonal to the
current delta/header/terminal cluster. If V-05 scores higher, the extended forms
contain excellence signals for R10 criteria.

---

## V-05 -- Full Stack: C-29 + C-30 extended (maximum structural expression)

**Combined axes**: C-29 extended (terminal closing note with explanation) + C-30
extended (header bridge with explicit FAIL consequence) + all R8 V-05 criteria

**Hypothesis**: C-29's minimum form ("verify it last") and C-30's minimum form
("Both artifacts are required to satisfy the Phase 3 postcondition") are necessary.
V-05 tests whether adding explicit reasoning (C-29 extended) and explicit failure
consequence (C-30 extended) introduces structurally distinct patterns that could
become R10 criteria:

C-29 extended: The terminal closing note explains WHY verdict_after is the only
order-dependent item: "verdict_after alone depends on a value (Phase 4 verdict_verb)
not known until after the campaign's last artifact write." This converts the rule
from a bare instruction into a reasoned constraint, enabling a model to generalize
the ordering principle to novel scenarios.

C-30 extended: The Phase 3 header adds the explicit FAIL consequence: "A model that
writes status.md and advances to Phase 4 without delta.md has not satisfied the
Phase 3 postcondition." This makes the annotation normative-with-consequence rather
than declarative-only -- the failure condition is declared at the role activation
site before execution begins.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

---

## Dual-Contract Annotation Rule

When a phase produces artifacts under more than one contract, the active-role header
for that phase must name every governing contract. Naming one contract and omitting
others is a structural defect. Phase 3 produces status.md (Phase 3 Contract) and
delta.md (Session Delta Contract); both contracts must appear in the Phase 3 header.

---

## Two-Pass Delta Rule

delta.md is produced in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. Phase 4 has not run; verdict_after cannot be
determined yet.

Pass 2 (Post-Phase 4): Update delta.md by setting verdict_after to the verdict_verb
from story.md. This is the only post-Phase-4 write in the campaign.

The terminal checklist item for verdict_after is order-dependent: a placeholder value
in verdict_after after Phase 4 completes is a defect. "NOT YET REACHED" in verdict_after
fails the terminal check unless Phase 4 verdict_verb is also "NOT YET REACHED".

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Partial coverage
fails. Each field typed as integer must contain an integer. Each field typed as
enumerated string must contain exactly one of the listed tokens.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md

- topic_name: string (non-empty, human-readable)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item:
  - signal_name: string (unique within strategy)
  - target_skill: string (namespace/skill format, e.g. "scout/scout-competitors")
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches signal_name from strategy.md)
    - collection_purpose: string (one sentence: why this signal matters)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0 (no prose, no ranges)
  - collected: integer >= 0 (no prose, no ranges)
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N" (X and N are integers)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md

- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

---

## Session Delta Contract -- delta.md

- session_number: integer >= 1
- signals_added: list of signal names collected this session;
  empty list [] if no signals added -- string "NONE" is not a valid value
- signals_removed: list of signal names removed this session;
  empty list [] if no signals removed -- string "NONE" is not a valid value
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
  (NONE = no prior session verdict; not a list -- this field is string-typed)
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
  (Pass 1 placeholder: "NOT YET REACHED" until Phase 4 completes)
- verdict_changed: string, exactly one of: YES | NO | N/A

---

## Prohibition Parity Rule

Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no
fewer. This count is fixed. A role with 4 or 6 items is structurally invalid and
fails audit. The numbered list format is required: each item labeled 1 through 5.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)

Owns strategy.md. Produces Phase 1 Contract output.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content across sources
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not declared in the strategy planned_signals field

### Planner (Phase 2 -- topic-plan)

Owns roadmap.md. Produces Phase 2 Contract output.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify the topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs from Phase 4 vocabulary
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)

Owns status.md AND delta.md. Produces Phase 3 Contract and Session Delta Contract output.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond what Phase 2 roadmap defines
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize on findings
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "a few", "many") where integers are
   required by contract

### Narrator (Phase 4 -- topic-story)

Owns story.md. Produces Phase 4 Contract output.

Forbidden actions (exactly 5):
1. Must not modify the coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid;
   "likely confirmed" or "essentially confirmed" both fail

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract:
- topic_name (string), namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields present and
typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply.*
*Phase 3 Contract governs status.md. Session Delta Contract governs delta.md.*

Phase 3 produces two artifacts under two contracts (see Dual-Contract Annotation
Rule). Both contracts are active at this phase. Both artifacts are required to
satisfy the Phase 3 postcondition. A model that writes status.md and advances to
Phase 4 without delta.md has not satisfied the Phase 3 postcondition.

### Step A -- Coverage Status

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present -- no row skipped
- planned and collected are integers -- narrative counts fail
- missing lists each signal by name -- counts alone fail
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md conforming to Session Delta Contract.

Two-pass protocol applies:
- Set verdict_after = "NOT YET REACHED" (placeholder -- Phase 4 has not run)
- All other fields are final at this step:
  - session_number: integer
  - signals_added: list ([] if none -- string "NONE" is invalid)
  - signals_removed: list ([] if none -- string "NONE" is invalid)
  - verdict_before: prior session readiness_verdict, or "NONE" for first session
  - verdict_changed: "N/A" for first session; defer to Pass 2 for subsequent sessions

Write delta to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md are BOTH present, each satisfying
their respective contracts. Writing status.md alone does not satisfy this
postcondition. A delta.md with missing fields or invalid types fails.

GATE: Do not proceed to Phase 4 until BOTH status.md AND delta.md satisfy their
contracts.

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (no paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, update delta.md (this is the only post-Phase-4 write):

- Set verdict_after = verdict_verb from story.md (replaces "NOT YET REACHED" placeholder)
- For subsequent sessions (session_number >= 2): set verdict_changed = YES if
  verdict_after != verdict_before; NO if equal
- For first session (verdict_before = NONE): verdict_changed = "N/A" (no prior to compare)

Update: simulations/topic/{{topic}}-delta-{{date}}.md

An un-updated placeholder in verdict_after is a terminal defect caught by the
checklist item for verdict_after.

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. planned_signals must
  list >= 3 entries.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals are planned;
  none collected.

Phase 3 (Analyst) [both contracts active]:
  Step A: All rows have collected = 0 (integer). missing lists all planned signals
    from roadmap.md by signal_name. zero_flag = "NO SIGNALS" where applicable.
    readiness_verdict = "NOT READY".
  Step B: session_number = 1. signals_added = [] (empty list -- NOT the string "NONE").
    signals_removed = []. verdict_before = "NONE" (string sentinel for first session --
    this field is string-typed, unlike signals_added which is list-typed).
    verdict_after = "NOT YET REACHED" (placeholder). verdict_changed = "N/A".
  Conjunction gate requires both artifacts before Phase 4.

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. next_signal_recommendations: top 3 from
  roadmap.md ordered by planned priority.

Post-Phase-4 update: verdict_after updated from placeholder to "NOT YET REACHED"
  (verdict_verb from Phase 4 -- coincides with placeholder for first invocation).
  verdict_changed remains "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently before marking the campaign complete. Each item
names a specific artifact field and its constraint. A field that satisfies the
constraint PASSES. A field that fails triggers re-run of the affected phase only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty
    FAIL: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low}
    FAIL: re-run Phase 1

[ ] planned_signals: count >= 3 (integer count, not estimated)
    FAIL: re-run Phase 1

[ ] planned_signals[*].target_skill: each in namespace/skill format
    FAIL: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_coverage: at least one entry present
    FAIL: re-run Phase 2

[ ] namespace_coverage[*].collection_purpose: string present per signal (not omitted)
    FAIL: re-run Phase 2

### Phase 3 -- status.md

[ ] row count: exactly 9 namespace rows present
    FAIL: re-run Phase 3

[ ] planned: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] collected: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] missing: list of signal names in each row (not a count -- names required)
    FAIL: re-run Phase 3

[ ] zero_flag: "NO SIGNALS" present for every row where planned = 0 AND collected = 0
    FAIL: re-run Phase 3

[ ] coverage_ratio: "X/N" format (X and N are both integers)
    FAIL: re-run Phase 3

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL: re-run Phase 3

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.s0: string present, non-empty
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.current: string present ("UNCHANGED" or updated hypothesis)
    FAIL: re-run Phase 4

[ ] echoes: list present with at least one entry (minimum ["NONE"])
    FAIL: re-run Phase 4

[ ] next_signal_recommendations: exactly 3 items
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].namespace: string present for all 3
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].gap_reason: string present for all 3
    FAIL: re-run Phase 4

### Session Delta -- delta.md

[ ] session_number: integer >= 1
    FAIL: re-run Phase 3 Step B

[ ] signals_added: list present ([] permitted; absent field or string "NONE" fails --
    the empty-list type [] is required, not the string sentinel)
    FAIL: re-run Phase 3 Step B

[ ] signals_removed: list present ([] permitted; absent field or string "NONE" fails)
    FAIL: re-run Phase 3 Step B

[ ] verdict_before: exactly one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    (string "NONE" is valid here -- this field is string-typed, not list-typed)
    FAIL: re-run Phase 3 Step B

[ ] verdict_after: exactly one of {READY|NOT READY|CONDITIONALLY READY|NOT YET REACHED};
    must reflect Phase 4 verdict_verb after Pass 2 completes; placeholder "NOT YET
    REACHED" fails after Phase 4 unless Phase 4 verdict_verb is also "NOT YET REACHED"
    FAIL: re-run Phase 3 Step B after Phase 4 completes (Pass 2)

[ ] verdict_changed: exactly one of {YES|NO|N/A}
    FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign is complete. Dashboard ready to emit.
Any item FAIL: re-run the affected phase. Re-verify the failed item only.
The verdict_after item is the only order-dependent item: verify it last, after Phase 4
and the Post-Phase-4 Delta Update have both completed. Every other item may be verified
immediately after its phase writes the artifact -- verdict_after alone depends on a
value (Phase 4 verdict_verb) not known until after the campaign's last artifact write.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-28 (full R8 V-05 baseline), C-29 extended
(terminal closing note: "The verdict_after item is the only order-dependent item:
verify it last, after Phase 4 and the Post-Phase-4 Delta Update have both completed.
Every other item may be verified immediately after its phase writes the artifact --
verdict_after alone depends on a value not known until after the campaign's last
artifact write"), C-30 extended (Phase 3 header: "Both contracts are active at this
phase. Both artifacts are required to satisfy the Phase 3 postcondition. A model
that writes status.md and advances to Phase 4 without delta.md has not satisfied
the Phase 3 postcondition." -- adds explicit FAIL consequence to the declarative
bridge).
**Misses**: Nothing expected. V-05 is the maximum-expression full-stack variation.
**Risk**: Extended forms of C-29 and C-30 add explanatory/consequence content. If
criteria are binary (semantic content present or absent), V-04 and V-05 score
identically at 116/116. If the rubric rewards explanation depth, V-05 scores higher.
Excellence signals from V-05 will identify candidate R10 criteria -- analogous to
how R9 C-29 and C-30 were extracted from R8 V-05's excellence signals.

---

## Variation Summary

| ID  | Primary Axes                                    | New Criteria Targeted      | Criteria Covered               | Key Risk |
|-----|-------------------------------------------------|----------------------------|--------------------------------|----------|
| V-01 | C-29 only -- terminal closing note             | C-29                       | C-01..C-28, C-29               | Closing note after "Any item FAIL" may not be read as normative |
| V-02 | C-30 only -- header postcondition bridge       | C-30                       | C-01..C-28, C-30               | Format criterion without write-order enforcement |
| V-03 | C-29 via pre-terminal named section (contrast) | C-29 (scoping Q)           | C-01..C-28, C-29 (if anywhere) | Named section before terminal fails if C-29 requires terminal placement |
| V-04 | C-29 + C-30 minimum-sufficient forms           | C-29 + C-30                | C-01..C-30                     | If V-04 = V-05 score, extended forms are redundant |
| V-05 | C-29 + C-30 extended forms (max expression)    | C-29 + C-30 (extended)     | C-01..C-30                     | Binary criteria won't differentiate V-04 from V-05 |

**Predicted leaderboard going into quest-score**: V-05 >= V-04 > V-01 = V-02 > V-03.

V-04 and V-05 are the only variations covering both new criteria. If C-29 and C-30
are binary, they tie at 116/116. V-01 scores C-29 only (113/116). V-02 scores C-30
only (113/116). V-03 is the structural contrast variation: if C-29 requires terminal
section placement, V-03 fails C-29 and scores 110/116 (tied with R8 V-05 baseline).
If presence anywhere satisfies C-29, V-03 ties V-01 at 113/116.

The critical open question for scoring: does C-29 require the order-dependency
annotation to appear WITHIN the TERMINAL section (closing note after checklist items),
or does a dedicated section before the terminal section also satisfy C-29? V-01 vs
V-03 resolves this. Same semantic content, two structural positions. The score
difference (or equivalence) answers the scoping question for all future variations.
