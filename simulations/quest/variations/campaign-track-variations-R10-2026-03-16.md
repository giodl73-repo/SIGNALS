Written. Here's the summary:

---

## campaign-track R10 — Five Variations

**Baseline**: R9 V-05 at 122/122 (C-31 and C-32 already satisfied). All five variations inherit the full R9 V-05 foundation.

**Three new structural axes explored**:

| ID | Axis | New pattern | Expected |
|----|------|-------------|----------|
| V-01 | C-33 only | Phase 4 header declares Post-Phase-4 Delta Update as a Phase 4 obligation (not optional). Analogous to C-32 at Phase 3 header. | 122 + C-33 |
| V-02 | C-34 only | Terminal section OPENING execution-order protocol (before any items). Complements C-31's closing note — together they bracket the checklist. | 122 + C-34 |
| V-03 | C-35 only | Cascade invalidation rule: when Phase 3 Step B re-runs, Pass 2 must also re-run. Names cascade target (verdict_after only) and scope exclusions. | 122 + C-35 |
| V-04 | C-33 + C-34 | Minimum-sufficient combination of V-01 + V-02. | 122 + C-33 + C-34 |
| V-05 | C-33 + C-34 + C-35 extended | Full stack. C-33 extended adds "stale-value" framing; C-35 extended explains WHY non-cascade fields are excluded (finalized at Phase 3). Both follow the assertion→causal-explanation pattern established by C-31/C-32. | 122 + all three |

**Key scoping questions**: V-02 resolves whether a terminal opening protocol is structurally distinct from C-31 (terminal closing). V-03 resolves whether the cascade rule adds enforcement beyond the existing Pass 2 section.
 Delta Update must also be
  re-verified. The cascade target is verdict_after only (the only delta.md field
  that depends on Phase 4 output). Named as a cascade rule with explicit scope.

**Max score**: 122 (19 aspirational x 3 + 5 essential x 10 + 3 recommended x 5)
**Baseline score**: 122/122 (all five variations inherit this floor)

| ID | New axes | C-33 | C-34 | C-35 | Expected score |
|----|----------|------|------|------|----------------|
| **V-01** | Phase 4 obligation header only | PASS | FAIL | FAIL | 122 + C-33 |
| **V-02** | Terminal opening protocol only | FAIL | PASS | FAIL | 122 + C-34 |
| **V-03** | Cascade invalidation rule only | FAIL | FAIL | PASS | 122 + C-35 |
| **V-04** | V-01 + V-02 combined | PASS | PASS | FAIL | 122 + C-33 + C-34 |
| **V-05** | V-01 + V-02 + V-03 full stack | PASS | PASS | PASS | 122 + C-33 + C-34 + C-35 |

**Key question V-01 resolves**: Does declaring the Post-Phase-4 Delta Update as a
Phase 4 obligation at the Phase 4 header (before execution) improve Pass 2 completion
vs. declaring it only in the Post-Phase-4 section (after Phase 4)?

**Key question V-02 resolves**: Does an execution-order protocol at the terminal
section's opening (naming the normal order + verdict_after exception) produce a
distinct structural pattern from C-31 (the closing note)? If C-34 scoring is
independent of C-31 scoring, the combination (V-04) closes the bracket.

**Key question V-03 resolves**: Does naming the cascade invalidation target (verdict_after
only) in an explicit cascade rule add enforcement beyond the existing Pass 2 section?

---

## V-01 -- Axis: Phase 4 obligation declaration (C-33 candidate)

**Hypothesis**: The Post-Phase-4 Delta Update section declares "this is the only
post-Phase-4 write" but it appears AFTER the Phase 4 section -- a model may treat
Phase 4 as complete when story.md is written, before reading the Post-Phase-4 section.
Declaring the delta.md obligation at the Phase 4 header -- before execution begins --
forces the model to enter Phase 4 knowing it has a post-write obligation. Analogous
to C-32 (failure consequence at Phase 3 header before Phase 3 execution). V-01 tests
whether this forward declaration at the Phase 4 activation site is structurally
distinct from the Post-Phase-4 Update section. Everything else at R9 V-05 baseline;
C-34 and C-35 absent.

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

Phase 4 has two obligations: (1) produce story.md per Phase 4 Contract, and (2)
perform the Post-Phase-4 Delta Update (Pass 2). A model that writes story.md without
updating delta.md has completed Phase 4's artifact obligation but has not completed
Phase 4's campaign obligation. The Post-Phase-4 Delta Update is not optional
post-processing -- it is a required Phase 4 step. Phase 4 is not complete until
verdict_after in delta.md reflects the verdict_verb from story.md.

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

**Rubric targeting**: C-01 through C-32 (full R9 V-05 baseline), C-33 (Phase 4 header
declares Post-Phase-4 Delta Update as a required Phase 4 obligation: "A model that
writes story.md without updating delta.md has completed Phase 4's artifact obligation
but has not completed Phase 4's campaign obligation").
**Misses**: C-34 (no terminal opening execution-order protocol), C-35 (no cascade
invalidation rule).
**Risk**: The Phase 4 obligation declaration may overlap with the existing
Post-Phase-4 Update section. The structural test is whether the forward declaration
at the activation site (before story.md is written) adds enforcement beyond the
post-execution section.

---

## V-02 -- Axis: Terminal section opening execution-order protocol (C-34 candidate)

**Hypothesis**: C-31 places the execution-order rule at the terminal section's CLOSING
note. V-02 tests whether a complementary opening rule -- declaring the normal
verification order and the verdict_after exception at the START of the terminal
section -- creates a distinct structural pattern. C-31 (closing) says "verify
verdict_after last." C-34 (opening) says "verify in phase order, except verdict_after."
Together they bracket the checklist. V-02 targets C-34 alone (C-31 closing note
present at baseline; C-33 and C-35 absent).

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

Execution order: Verify items in phase order -- Phase 1, Phase 2, Phase 3 (status.md),
Phase 3 (delta.md), Phase 4. Exception: the verdict_after item must be verified last,
after all Phase 4 items pass and the Post-Phase-4 Delta Update completes. No phase
may be marked complete until all items for that phase PASS.

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

**Rubric targeting**: C-01 through C-32 (full R9 V-05 baseline), C-34 (terminal
section opening execution-order protocol: "Execution order: Verify items in phase
order... Exception: the verdict_after item must be verified last, after all Phase 4
items pass and the Post-Phase-4 Delta Update completes").
**Misses**: C-33 (no Phase 4 obligation declaration at Phase 4 header), C-35 (no
cascade invalidation rule).
**Risk**: C-34 may be subsumed by C-31 if evaluators treat the opening and closing
notes as equivalent. The structural distinction: C-31 is a closing note encountered
after all items are listed; C-34 is an opening protocol encountered before any items
are verified.

---

## V-03 -- Axis: Cascade invalidation rule (C-35 candidate)

**Hypothesis**: The current prompt says "FAIL: re-run Phase 3 Step B" for delta.md
failures but does not address the cascade consequence: when Phase 3 Step B is re-run,
verdict_after (which depends on Phase 4 output) must also be re-verified against the
current story.md. Without an explicit cascade rule, a model that re-runs Phase 3 Step
B may write a new delta.md with verdict_after = "NOT YET REACHED" (the Pass 1
placeholder) and stop, having technically re-run Phase 3 Step B but left verdict_after
unresolved. V-03 adds a cascade rule that names the cascade target (verdict_after
only) and the cascade action (re-run Pass 2). Everything else at R9 V-05 baseline;
C-33 and C-34 absent.

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

## Cascade Invalidation Rule

When Phase 3 Step B is re-run due to a terminal failure, the Post-Phase-4 Delta
Update (Pass 2) must also be re-run. Pass 2 is the step that sets verdict_after to
the Phase 4 verdict_verb. Re-running Phase 3 Step B resets verdict_after to the
"NOT YET REACHED" placeholder. The cascade target is verdict_after only: session_number,
signals_added, signals_removed, verdict_before, and verdict_changed do not depend on
Phase 4 output and do not require cascade re-verification. A re-run of Phase 3 Step B
is incomplete until Pass 2 has been re-executed and verdict_after reflects the current
story.md verdict_verb.

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
    FAIL: re-run Phase 3 Step B after Phase 4 completes (Pass 2); if Phase 3 Step B
    was re-run, the Cascade Invalidation Rule applies -- re-run Pass 2 before verifying

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

**Rubric targeting**: C-01 through C-32 (full R9 V-05 baseline), C-35 (Cascade
Invalidation Rule named as a top-level rule section; verdict_after terminal item
extended with "if Phase 3 Step B was re-run, the Cascade Invalidation Rule applies --
re-run Pass 2 before verifying").
**Misses**: C-33 (no Phase 4 obligation declaration at Phase 4 header), C-34 (no
terminal opening execution-order protocol).
**Risk**: C-35 may be dismissed as redundant with the existing Pass 2 section.
Structural distinction: the cascade rule names the trigger (Phase 3 Step B re-run),
the cascade target (verdict_after only), and the scope exclusion (other delta.md
fields are NOT cascade targets). The Pass 2 section describes the happy path; the
cascade rule describes the re-run recovery path.

---

## V-04 -- Combined: Phase 4 obligation declaration + terminal opening protocol

**Combined axes**: C-33 (Phase 4 header obligation declaration) + C-34 (terminal
opening execution-order protocol). Minimum-sufficient combination of V-01 and V-02.
Targets both header-site patterns without cascade rule. C-35 absent.

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

Phase 4 has two obligations: (1) produce story.md per Phase 4 Contract, and (2)
perform the Post-Phase-4 Delta Update (Pass 2). A model that writes story.md without
updating delta.md has completed Phase 4's artifact obligation but has not completed
Phase 4's campaign obligation. The Post-Phase-4 Delta Update is not optional
post-processing -- it is a required Phase 4 step. Phase 4 is not complete until
verdict_after in delta.md reflects the verdict_verb from story.md.

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

Execution order: Verify items in phase order -- Phase 1, Phase 2, Phase 3 (status.md),
Phase 3 (delta.md), Phase 4. Exception: the verdict_after item must be verified last,
after all Phase 4 items pass and the Post-Phase-4 Delta Update completes. No phase
may be marked complete until all items for that phase PASS.

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

**Rubric targeting**: C-01 through C-32 (full R9 V-05 baseline), C-33 (Phase 4
obligation declaration at Phase 4 header), C-34 (terminal opening execution-order
protocol).
**Misses**: C-35 (no cascade invalidation rule).
**Risk**: None beyond V-01 and V-02 individual risks. If C-33 and C-34 are both
binary, V-04 and V-05 score identically except for C-35. The extended forms in V-05
would then be R11 candidate patterns.

---

## V-05 -- Full stack: C-33 + C-34 + C-35 + extended forms

**Combined axes**: Phase 4 obligation declaration + terminal opening execution-order
protocol + cascade invalidation rule. All three new pattern axes. Extended forms where
structurally distinct from minimum-sufficient.

C-33 extended: Phase 4 header names the specific deficit: "A model that stops after
writing story.md has produced the Phase 4 artifact but has produced an inconsistent
campaign state: delta.md verdict_after still names 'NOT YET REACHED', a value that
was correct before Phase 4 ran but is now stale. Stale verdict_after is a terminal
defect." The extended form names the specific stale-value defect rather than only
naming the obligation.

C-35 extended: The cascade rule additionally names which fields are NOT cascade
targets and why: "session_number, signals_added, signals_removed, verdict_before, and
verdict_changed do not depend on Phase 4 output because they capture session-level
events that are finalized at Phase 3 completion. Only verdict_after bridges Phase 3
and Phase 4; it is the only cascade target."

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

## Cascade Invalidation Rule

When Phase 3 Step B is re-run due to a terminal failure, the Post-Phase-4 Delta
Update (Pass 2) must also be re-run. Pass 2 is the step that sets verdict_after to
the Phase 4 verdict_verb. Re-running Phase 3 Step B resets verdict_after to the
"NOT YET REACHED" placeholder.

The cascade target is verdict_after only. session_number, signals_added,
signals_removed, verdict_before, and verdict_changed do not depend on Phase 4 output
because they capture session-level events that are finalized at Phase 3 completion.
Only verdict_after bridges Phase 3 and Phase 4; it is the only cascade target. A
re-run of Phase 3 Step B that does not also re-run Pass 2 leaves verdict_after stale
and fails the terminal checklist.

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

Phase 4 has two obligations: (1) produce story.md per Phase 4 Contract, and (2)
perform the Post-Phase-4 Delta Update (Pass 2). A model that stops after writing
story.md has produced the Phase 4 artifact but has produced an inconsistent campaign
state: delta.md verdict_after still names "NOT YET REACHED", a value that was correct
before Phase 4 ran but is now stale. Stale verdict_after is a terminal defect. The
Post-Phase-4 Delta Update is not optional post-processing -- it is a required Phase 4
step. Phase 4 is not complete until verdict_after in delta.md reflects the verdict_verb
from story.md.

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

Execution order: Verify items in phase order -- Phase 1, Phase 2, Phase 3 (status.md),
Phase 3 (delta.md), Phase 4. Exception: the verdict_after item must be verified last,
after all Phase 4 items pass and the Post-Phase-4 Delta Update completes. No phase
may be marked complete until all items for that phase PASS.

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
    REACHED" fails after Phase 4 unless Phase 4 verdict_verb is also "NOT YET REACHED";
    if Phase 3 Step B was re-run, Cascade Invalidation Rule applies -- re-run Pass 2
    before verifying this field
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

**Rubric targeting**: C-01 through C-32 (full R9 V-05 baseline), C-33 extended (Phase
4 header names stale verdict_after as the specific defect), C-34 (terminal opening
execution-order protocol), C-35 extended (cascade rule names non-cascade fields with
causal explanation: "finalized at Phase 3 completion ... only verdict_after bridges
Phase 3 and Phase 4").
**Misses**: Nothing expected. V-05 is the maximum structural expression of the three
new pattern axes.
**Excellence signals for R11**: (1) C-33 extended introduces "stale-value" framing --
naming the specific incorrect state (verdict_after = "NOT YET REACHED" after Phase 4
ran) rather than only naming the obligation. (2) C-35 extended introduces
non-cascade-target exclusion reasoning -- explaining WHY the other fields are not
cascade targets (they are finalized at Phase 3), not just asserting they are excluded.
Both patterns follow the same structural logic as C-31/C-32: assertion -> causal
explanation.

Written to `simulations/quest/variations/campaign-track-variations-R10-2026-03-16.md`.
