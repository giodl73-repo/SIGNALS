---
skill: quest-variate
skill_target: campaign-track
round: 8
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-track-rubric-v8-2026-03-16.md
---

# Variations -- campaign-track / Round 8

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

R7 closed C-10 (dual-session delta) at all levels of structural quality -- prose,
typed, gated, two-pass. The five-way tie at 98/98 confirmed C-10 is binary (presence
only). Four excellence patterns from R7 V-05 did not split the score but were
structurally distinct enough to become new criteria in v8:

- C-25 -- Two-pass delta update: Phase 3 Step B writes delta.md with placeholder
  verdict_after ("NOT YET REACHED"); a declared post-Phase-4 step updates it with the
  actual verdict_verb. Terminal checklist item flags "placeholder fails" as the only
  order-dependent constraint in the campaign.

- C-26 -- Dual-contract active-role annotation: Phase 3 header names both Phase 3
  Contract AND Session Delta Contract at the execution site. A normative rule declares
  that when a phase produces two artifacts, both contracts must be named in the header.

- C-27 -- Conjunction progression gate: Phase 3 postcondition is a conjunction:
  "status.md AND delta.md both present." The AND-logic gate makes delta.md
  non-skippable -- a model writing status.md alone cannot advance to Phase 4.

- C-28 -- Empty-list sentinel type-tightening: Terminal checklist item for
  signals_added explicitly rejects the string "NONE" sentinel and requires empty list
  [] for zero-signal sessions. Closes the type-inconsistency gap carried from R7 V-01.

Aspirational count goes from 11 to 15; max from 98 to 110.

R7 V-05 was the full-stack baseline that contained all four patterns as excellence
signals. R8 variations isolate each axis before combining.

---

## V-01 -- Axis: Two-pass delta update (C-25 maximum)

**Hypothesis**: The two-pass protocol is the correct lifecycle for an artifact that
contains a value not yet known at write time. Making this protocol explicit as a
named structural pattern -- Phase 3 Step B writes delta.md with verdict_after =
"NOT YET REACHED" as a declared placeholder, then a post-Phase-4 update step
overwrites verdict_after with the actual verdict_verb from story.md -- prevents
two failure modes: (a) leaving the placeholder in place, and (b) prematurely
computing verdict_after before Phase 4 runs. The terminal checklist item for
verdict_after is uniquely order-dependent: "must reflect Phase 4 verdict_verb;
placeholder fails; FAIL: re-run Phase 3 Step B after Phase 4 completes." V-01
tests whether this single-axis declaration is sufficient to enforce the correct
lifecycle. Everything else at R7 baseline: status.md-only gate (no conjunction),
single-contract Phase 3 header (no dual-contract annotation), no signals_added
type note.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

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
- signals_added: list of signal names collected this session (empty list [] if none)
- signals_removed: list of signal names removed this session (empty list [] if none)
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
  (NONE = no prior session verdict)
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
  (NOT YET REACHED = placeholder written in Phase 3 Step B before Phase 4 runs;
   updated post-Phase 4 with actual verdict_verb from story.md)
- verdict_changed: string, exactly one of: YES | NO | N/A
  (N/A = first session with no prior verdict)

---

## Two-Pass Delta Rule

delta.md is written in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. The Phase 4 verdict is not yet known.

Pass 2 (Post-Phase 4): Update delta.md by setting verdict_after to the actual
verdict_verb value from story.md. This is the only post-Phase-4 write in the
campaign.

The terminal checklist item for verdict_after is order-dependent: it verifies that
the placeholder has been replaced. "NOT YET REACHED" in verdict_after after Phase 4
completes is a defect, not a valid verdict token.

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
collection_purpose present per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs output.*

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

IMPORTANT -- Two-pass protocol applies:
- Write verdict_after = "NOT YET REACHED" as a placeholder. Phase 4 has not run;
  the actual verdict is not yet known.
- All other fields (session_number, signals_added, signals_removed, verdict_before,
  verdict_changed) are final at this step.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md present with 9 rows, integer fields, readiness_verdict
assigned from enumerated set.

GATE: Do not proceed to Phase 4 until Phase 3 postcondition is satisfied.

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

After story.md is written, update delta.md:

- Set verdict_after = verdict_verb value from story.md
- Set verdict_changed = YES if verdict_after != verdict_before; NO if equal; N/A if
  verdict_before = NONE

This is the only write that occurs after Phase 4. The placeholder "NOT YET REACHED"
in verdict_after must be replaced. An un-updated placeholder is a defect caught by
the terminal checklist.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. planned_signals must
  list >= 3 entries. This is the founding artifact.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals are planned;
  none are collected. roadmap.md documents what will be collected.

Phase 3 (Analyst):
  Step A: All rows have collected = 0 (integer). missing lists all planned signals
    from roadmap.md by signal_name. zero_flag = "NO SIGNALS" for namespaces where
    planned = 0 AND collected = 0. readiness_verdict = "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED" (placeholder).
    verdict_changed = "N/A".

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. next_signal_recommendations: top 3 signals from
  roadmap.md ordered by planned priority.

Post-Phase-4 update: verdict_after in delta.md updated from placeholder to
  "NOT YET REACHED" (actual from story.md -- coincides with placeholder for first
  invocation). verdict_changed = "N/A".

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

[ ] signals_added: list present ([] permitted if no signals added this session)
    FAIL: re-run Phase 3 Step B

[ ] signals_removed: list present ([] permitted if no signals removed)
    FAIL: re-run Phase 3 Step B

[ ] verdict_before: exactly one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B

[ ] verdict_after: exactly one of {READY|NOT READY|CONDITIONALLY READY|NOT YET REACHED};
    must reflect Phase 4 verdict_verb; placeholder "NOT YET REACHED" fails after
    Phase 4 completes (unless Phase 4 verdict_verb is also "NOT YET REACHED")
    FAIL: re-run Phase 3 Step B after Phase 4 completes

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

**Rubric targeting**: C-01 through C-24 (full R7 V-05 baseline), C-25 (two-pass
delta rule declared as named structural pattern; Phase 3 Step B writes placeholder;
post-Phase-4 update step declared; terminal verdict_after item is order-dependent
with "placeholder fails" wording and "re-run Phase 3 Step B after Phase 4 completes"
FAIL action -- the only order-dependent item in the checklist).
**Misses**: C-26 (single-contract Phase 3 header, no dual-contract normative rule),
C-27 (status.md-only gate, delta not in conjunction), C-28 (signals_added item
permits "[]" but does not explicitly reject string "NONE" sentinel).
**Risk**: The two-pass protocol is explicit but a model may not treat the Post-Phase-4
update step as distinct from Phase 4 -- it may write story.md and update delta.md
atomically, collapsing the two passes into one. The phrasing "After story.md is
written, update delta.md" is designed to signal sequential execution, but the
terminal checklist is the primary enforcement: a model must produce a checklist item
confirming verdict_after has been updated from placeholder.

---

## V-02 -- Axis: Dual-contract active-role annotation (C-26 maximum)

**Hypothesis**: When a phase produces two artifacts under two contracts, naming both
contracts in the active-role header keeps all constraint visibility at the execution
site. A model executing Phase 3 sees "Phase 3 Contract governs status.md. Session
Delta Contract governs delta.md." at the phase header -- without navigating to the
Typed Output Contracts section. A normative rule -- "when a phase produces two
artifacts, both contracts must be named in the phase header" -- makes dual-naming a
structural requirement, not a formatting nicety. V-02 tests whether this single-axis
declaration reduces contract-skip (a model writing status.md while ignoring the delta
contract) compared to R7 baselines that named only one contract at the execution site.
Everything else at R7 baseline: status.md-only gate (no conjunction), no two-pass
protocol, no signals_added type note.

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
for that phase must name every contract governing output in that phase. Naming one
contract and omitting others is a structural defect. A model executing a multi-
artifact phase sees all governing contracts in the header, without navigating to the
contract sections.

This rule applies to Phase 3, which produces status.md (Phase 3 Contract) and
delta.md (Session Delta Contract). The Phase 3 header must name both.

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
- signals_added: list of signal names collected this session (empty list [] if none)
- signals_removed: list of signal names removed this session (empty list [] if none)
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
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
collection_purpose present per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply.*
*Phase 3 Contract governs status.md. Session Delta Contract governs delta.md.*

Phase 3 produces two artifacts under two contracts. Both contracts are named above
and govern their respective artifacts independently.

### Step A -- Coverage Status

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present -- no row skipped
- planned and collected are integers -- narrative counts fail
- missing lists each signal by name -- counts alone fail
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta

Produce delta.md conforming to Session Delta Contract.
All fields required. verdict_after reflects the current readiness_verdict from
Step A (the Phase 4 narrative verdict is not yet assigned -- use readiness_verdict
as proxy or "NOT YET REACHED" if not yet determinable).

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md present with 9 rows, integer fields, readiness_verdict
assigned from enumerated set.

GATE: Do not proceed to Phase 4 until Phase 3 postcondition is satisfied.

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

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract normally.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract normally.

Phase 3 (Analyst) [both contracts active per header]:
  Step A: All rows have collected = 0 (integer). missing lists all planned signals
    by signal_name. zero_flag = "NO SIGNALS" where applicable. readiness_verdict
    = "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED". verdict_changed
    = "N/A".

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. next_signal_recommendations: top 3 from roadmap.

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently before marking the campaign complete. A field
that fails triggers re-run of the affected phase only.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty
    FAIL: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low}
    FAIL: re-run Phase 1

[ ] planned_signals: count >= 3
    FAIL: re-run Phase 1

[ ] planned_signals[*].target_skill: each in namespace/skill format
    FAIL: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_coverage: at least one entry present
    FAIL: re-run Phase 2

[ ] namespace_coverage[*].collection_purpose: string present per signal
    FAIL: re-run Phase 2

### Phase 3 -- status.md

[ ] row count: exactly 9 namespace rows present
    FAIL: re-run Phase 3

[ ] planned: integer value in all 9 rows
    FAIL: re-run Phase 3

[ ] collected: integer value in all 9 rows
    FAIL: re-run Phase 3

[ ] missing: list of signal names in each row (names required, not counts)
    FAIL: re-run Phase 3

[ ] zero_flag: "NO SIGNALS" for every row where planned = 0 AND collected = 0
    FAIL: re-run Phase 3

[ ] coverage_ratio: "X/N" format
    FAIL: re-run Phase 3

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL: re-run Phase 3

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.s0: string present, non-empty
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.current: string present
    FAIL: re-run Phase 4

[ ] echoes: list present, minimum ["NONE"]
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

[ ] signals_added: list present
    FAIL: re-run Phase 3 Step B

[ ] signals_removed: list present
    FAIL: re-run Phase 3 Step B

[ ] verdict_before: exactly one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B

[ ] verdict_after: exactly one of {READY|NOT READY|CONDITIONALLY READY|NOT YET REACHED}
    FAIL: re-run Phase 3 Step B

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
5. Session delta summary
```

**Rubric targeting**: C-01 through C-24 (full R7 V-05 baseline), C-26 (Dual-Contract
Annotation Rule declared normatively: "when a phase produces two artifacts, both
contracts must be named in the phase header"; Phase 3 header names both Phase 3
Contract AND Session Delta Contract as the concrete application of the rule).
**Misses**: C-25 (no two-pass protocol; verdict_after written in Phase 3, no
post-Phase-4 update), C-27 (status.md-only gate, delta not in conjunction), C-28
(signals_added item does not reject string "NONE" sentinel).
**Risk**: The dual-contract annotation may be syntactically satisfied without
behavioral effect -- a model that names both contracts in the header but then only
produces status.md from that phase still "passes" the annotation check. C-26 is a
format criterion; it does not by itself enforce that delta.md is written. C-27 (the
conjunction gate) is the enforcement complement.

---

## V-03 -- Axis: Conjunction progression gate (C-27 maximum)

**Hypothesis**: Making delta.md structurally non-skippable requires placing it inside
a phase gate, not after the gate. "status.md AND delta.md both present, each
satisfying their contracts" as the Phase 3 postcondition means a model cannot advance
to Phase 4 by writing status.md alone -- the gate evaluates both artifacts. V-03 tests
whether the conjunction gate (AND-logic postcondition) produces more reliable delta.md
presence than either (a) post-Phase-4 appendage position or (b) gating on status.md
only, which treats delta.md as optional collateral. Everything else at R7 baseline:
no two-pass protocol (delta is written in one pass), single-contract Phase 3 header
(no dual-contract annotation), no signals_added type note.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

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
  - target_skill: string (namespace/skill format)
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches signal_name from strategy.md)
    - collection_purpose: string (one sentence)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0
  - collected: integer >= 0
  - missing: list of strings (signal names; empty list [] if none)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary:
  - coverage_ratio: string, format "X/N"
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md

- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text)
  - current: string (updated or literal "UNCHANGED")
- echoes: list of strings; if none, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

---

## Session Delta Contract -- delta.md

- session_number: integer >= 1
- signals_added: list of signal names collected this session ([] if none)
- signals_removed: list of signal names removed this session ([] if none)
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
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
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract.

Phase 1 postcondition: strategy.md present, all fields typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract.

Phase 2 postcondition: roadmap.md present with at least one entry and collection_purpose
per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs output.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present
- planned and collected are integers
- missing lists each signal by name
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N"; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta

Produce delta.md conforming to Session Delta Contract.
All fields required. verdict_after reflects the Phase 4 narrative verdict; if Phase 4
has not yet run, use readiness_verdict from Step A or "NOT YET REACHED".

Write delta to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md are BOTH present and satisfy their
respective contracts. Writing status.md alone does not satisfy this postcondition.
delta.md must be present with all Session Delta Contract fields populated.

GATE: Do not proceed to Phase 4 until BOTH status.md AND delta.md satisfy their
contracts.

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract.

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract normally.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract normally.

Phase 3 (Analyst):
  Step A: collected = 0 in all rows. missing lists all planned signals by name.
    zero_flag = "NO SIGNALS" where applicable. readiness_verdict = "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED". verdict_changed = "N/A".
  Both artifacts required to satisfy the conjunction postcondition.

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. top 3 recommendations from roadmap.md.

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently. A failed item triggers re-run of the
affected phase only.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty
    FAIL: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low}
    FAIL: re-run Phase 1

[ ] planned_signals: count >= 3
    FAIL: re-run Phase 1

[ ] planned_signals[*].target_skill: each in namespace/skill format
    FAIL: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_coverage: at least one entry present
    FAIL: re-run Phase 2

[ ] namespace_coverage[*].collection_purpose: string present per signal
    FAIL: re-run Phase 2

### Phase 3 -- status.md

[ ] row count: exactly 9
    FAIL: re-run Phase 3

[ ] planned: integer value in all 9 rows
    FAIL: re-run Phase 3

[ ] collected: integer value in all 9 rows
    FAIL: re-run Phase 3

[ ] missing: list of signal names (names required)
    FAIL: re-run Phase 3

[ ] zero_flag: "NO SIGNALS" for every row where planned = 0 AND collected = 0
    FAIL: re-run Phase 3

[ ] coverage_ratio: "X/N" format
    FAIL: re-run Phase 3

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL: re-run Phase 3

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.s0: string present, non-empty
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.current: string present
    FAIL: re-run Phase 4

[ ] echoes: list present, minimum ["NONE"]
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

[ ] signals_added: list present
    FAIL: re-run Phase 3 Step B

[ ] signals_removed: list present
    FAIL: re-run Phase 3 Step B

[ ] verdict_before: exactly one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B

[ ] verdict_after: exactly one of {READY|NOT READY|CONDITIONALLY READY|NOT YET REACHED}
    FAIL: re-run Phase 3 Step B

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
5. Session delta summary
```

**Rubric targeting**: C-01 through C-24 (full R7 V-05 baseline), C-27 (conjunction
gate declared as "status.md AND delta.md BOTH present and satisfy their respective
contracts"; "Writing status.md alone does not satisfy this postcondition" makes the
AND-logic explicit and normative; GATE sentence uses "BOTH" language).
**Misses**: C-25 (no two-pass protocol, delta written in one pass in Phase 3 Step B),
C-26 (single-contract Phase 3 header, no dual-contract annotation rule), C-28 (no
type-tightening on signals_added sentinel).
**Risk**: The conjunction gate is the strongest enforcement of the three single-axis
variations -- a model cannot skip delta.md and still advance. But the gate says
nothing about the order of writing delta.md vs. what Phase 4 produces. Without C-25's
two-pass protocol, verdict_after must be filled in Phase 3 Step B before Phase 4 has
run -- the instructions say "use readiness_verdict... or 'NOT YET REACHED'" which is
a judgment call, not a typed constraint.

---

## V-04 -- Combined Axes: Two-pass delta + Dual-contract annotation + Conjunction gate (C-25 + C-26 + C-27)

**Hypothesis**: C-25 (lifecycle order), C-26 (constraint visibility), and C-27
(structural necessity) address the same artifact from orthogonal angles. The gate
(C-27) ensures delta.md exists. The annotation (C-26) ensures both contracts are
visible when writing. The two-pass protocol (C-25) ensures the order-dependent field
is correctly deferred. Together they close three failure modes simultaneously:
omission (delta skipped), invisibility (delta contract not seen at execution), and
premature resolution (verdict_after filled before Phase 4 runs). V-04 tests whether
this three-axis combination produces the full structural robustness without the
type-tightening refinement of C-28 (signals_added sentinel rejection).

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
others is a structural defect. Phase 3 produces two artifacts (status.md and delta.md)
under two contracts; both contracts must appear in the Phase 3 header.

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
  - target_skill: string (namespace/skill format)
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches signal_name from strategy.md)
    - collection_purpose: string (one sentence)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0
  - collected: integer >= 0
  - missing: list of strings (signal names; empty list [] if none)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary:
  - coverage_ratio: string, format "X/N"
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md

- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text)
  - current: string (updated or literal "UNCHANGED")
- echoes: list of strings; if none, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

---

## Session Delta Contract -- delta.md

- session_number: integer >= 1
- signals_added: list of signal names collected this session ([] if none)
- signals_removed: list of signal names removed this session ([] if none)
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
  (Pass 1 placeholder: "NOT YET REACHED" until Phase 4 completes)
- verdict_changed: string, exactly one of: YES | NO | N/A

---

## Prohibition Parity Rule

Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no
fewer. This count is fixed. A role with 4 or 6 items is structurally invalid and
fails audit.

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
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract.

Phase 1 postcondition: strategy.md present, all fields typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract.

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply.*
*Phase 3 Contract governs status.md. Session Delta Contract governs delta.md.*

Phase 3 produces two artifacts under two contracts. Both are required to advance.

### Step A -- Coverage Status

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present
- planned and collected are integers
- missing lists each signal by name
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N"; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md conforming to Session Delta Contract.

Two-pass protocol applies:
- Set verdict_after = "NOT YET REACHED" (placeholder -- Phase 4 not yet run)
- All other fields (session_number, signals_added, signals_removed, verdict_before,
  verdict_changed) are final at this step

Write delta to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md are BOTH present, each satisfying
their respective contracts. Status.md alone does not satisfy this postcondition.

GATE: Do not proceed to Phase 4 until BOTH status.md AND delta.md satisfy their
contracts.

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract:
- verdict_verb: exactly one of the 5 tokens (no paraphrase)
- hypothesis_mutation: s0 + current
- echoes: minimum ["NONE"]
- next_signal_recommendations: exactly 3 items

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, update delta.md:

- Set verdict_after = verdict_verb from story.md (replaces placeholder)
- Set verdict_changed = YES if verdict_after != verdict_before; NO if equal;
  N/A if verdict_before = NONE

Update: simulations/topic/{{topic}}-delta-{{date}}.md

An un-updated placeholder ("NOT YET REACHED") in verdict_after after this step is a
defect caught by the terminal checklist.

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract normally.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract normally.

Phase 3 (Analyst):
  Step A: collected = 0 in all rows. missing lists all planned signals by name.
    readiness_verdict = "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED" (placeholder).
    verdict_changed = "N/A".
  Conjunction gate: both artifacts required before Phase 4.

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". current = "UNCHANGED".
  echoes = ["NONE"]. top 3 from roadmap.md.

Post-Phase-4 update: verdict_after = "NOT YET REACHED" (matches Phase 4 output).
  verdict_changed = "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently. A failed item triggers re-run of the
affected phase only.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty
    FAIL: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low}
    FAIL: re-run Phase 1

[ ] planned_signals: count >= 3
    FAIL: re-run Phase 1

[ ] planned_signals[*].target_skill: each in namespace/skill format
    FAIL: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_coverage: at least one entry present
    FAIL: re-run Phase 2

[ ] namespace_coverage[*].collection_purpose: string present per signal
    FAIL: re-run Phase 2

### Phase 3 -- status.md

[ ] row count: exactly 9
    FAIL: re-run Phase 3

[ ] planned: integer in all 9 rows
    FAIL: re-run Phase 3

[ ] collected: integer in all 9 rows
    FAIL: re-run Phase 3

[ ] missing: list of signal names (names required)
    FAIL: re-run Phase 3

[ ] zero_flag: "NO SIGNALS" for every row where planned = 0 AND collected = 0
    FAIL: re-run Phase 3

[ ] coverage_ratio: "X/N" format
    FAIL: re-run Phase 3

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL: re-run Phase 3

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.s0: string present, non-empty
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.current: string present
    FAIL: re-run Phase 4

[ ] echoes: list present, minimum ["NONE"]
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

[ ] signals_added: list present ([] permitted)
    FAIL: re-run Phase 3 Step B

[ ] signals_removed: list present ([] permitted)
    FAIL: re-run Phase 3 Step B

[ ] verdict_before: exactly one of {READY|NOT READY|CONDITIONALLY READY|NONE}
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
5. Session delta summary
```

**Rubric targeting**: C-01 through C-24 (full R7 V-05 baseline), C-25 (Two-Pass
Delta Rule section; "NOT YET REACHED" declared as placeholder in Session Delta
Contract; Post-Phase-4 update step; terminal verdict_after item with order-dependent
"placeholder fails" and "re-run Phase 3 Step B after Phase 4 completes (Pass 2)"
FAIL action), C-26 (Dual-Contract Annotation Rule section; Phase 3 header names both
contracts; normative statement that single-contract header is a structural defect),
C-27 (conjunction postcondition: "BOTH status.md AND delta.md ... Status.md alone
does not satisfy this postcondition"; GATE uses "BOTH" language).
**Misses**: C-28 (signals_added terminal item says "[] permitted" but does not
explicitly reject string "NONE" sentinel).
**Risk**: Three structural rules (two-pass, dual-contract annotation, conjunction
gate) address the same artifact from different angles. A model may satisfy all three
syntactically while still filling verdict_after in Phase 3 Step B with a judgment
value and skipping the post-Phase-4 update. The terminal checklist is the primary
defense -- the verdict_after item's "placeholder fails after Phase 4" wording catches
this. The conjunction gate is the strongest enforcement; the annotation is the weakest
(format, not behavior).

---

## V-05 -- Full Stack: C-25 + C-26 + C-27 + C-28 (all four new criteria on R7 V-05 baseline)

**Combined axes**: Two-pass delta update (C-25) + Dual-contract active-role annotation
(C-26) + Conjunction progression gate (C-27) + Empty-list sentinel type-tightening
(C-28)

**Hypothesis**: C-28 is the correctness refinement that closes the last type gap. It
addresses the scenario where a model trained on untyped prior variations (R7 V-01,
which used the string "NONE" as a first-invocation sentinel for signals_added) passes
the terminal checklist item "signals_added: list present" by writing a string "NONE"
value instead of an empty list []. The checklist item must explicitly reject the
string sentinel: "[] permitted; absent field or string 'NONE' fails." Combined with
C-25 (two-pass), C-26 (dual-contract annotation), and C-27 (conjunction gate), V-05
achieves maximum structural robustness for the delta artifact across four failure
modes: order dependency, constraint visibility, structural necessity, and type
consistency. This is the predicted top scorer for R8.

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
  (verdict_verb from Phase 4 -- coincides with placeholder for first invocation with
  no collected signals). verdict_changed remains "N/A".

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

**Rubric targeting**: C-01 through C-24 (full R7 V-05 baseline), C-25 (Two-Pass
Delta Rule section; "NOT YET REACHED" declared as placeholder in Session Delta
Contract definition; Phase 3 Step B instructs "Set verdict_after = NOT YET REACHED
(placeholder -- Phase 4 has not run)"; Post-Phase-4 update step declares verdict_after
replacement; terminal verdict_after item is order-dependent with "placeholder fails
after Phase 4" and "re-run Phase 3 Step B after Phase 4 completes (Pass 2)" FAIL
action; final note: "verdict_after item is the only order-dependent item: verify it
last"), C-26 (Dual-Contract Annotation Rule section declares normative requirement;
Phase 3 header: "Phase 3 Contract governs status.md. Session Delta Contract governs
delta.md."; explicit note "Both contracts are active at this phase"), C-27 (conjunction
postcondition: "status.md AND delta.md are BOTH present"; "Writing status.md alone
does not satisfy this postcondition"; GATE uses "BOTH ... satisfy their contracts"),
C-28 (Session Delta Contract definition notes "string 'NONE' is not a valid value"
for signals_added and signals_removed; terminal checklist item: "[] permitted; absent
field or string 'NONE' fails -- the empty-list type [] is required, not the string
sentinel"; Empty-State section contrasts the type distinction: signals_added = []
with comment "NOT the string 'NONE'" while verdict_before = "NONE" with comment
"this field is string-typed, unlike signals_added which is list-typed").
**Risk**: This is the most structurally complete variation. Four rules interact around
the same artifact (delta.md). A model producing the prompt may generate all four
sections but conflate the type distinction in C-28 -- since verdict_before legitimately
uses string "NONE" and signals_added must use [], the Empty-State section's explicit
"NOT the string 'NONE'" comment and the terminal item's "the empty-list type []
is required, not the string sentinel" wording are the primary differentiators. The
clarification in C-28's terminal item: "string 'NONE' is valid here -- this field is
string-typed, not list-typed" (for verdict_before) prevents over-applying the
rejection rule to both fields.

---

## Variation Summary

| ID  | Primary Axes                                | New Criteria Targeted | Criteria Covered | Key Risk |
|-----|---------------------------------------------|-----------------------|------------------|----------|
| V-01 | Two-pass delta update                      | C-25                  | C-01..C-24, C-25 | Model collapses two passes into one atomic write |
| V-02 | Dual-contract active-role annotation       | C-26                  | C-01..C-24, C-26 | Format criterion without behavior enforcement |
| V-03 | Conjunction progression gate               | C-27                  | C-01..C-24, C-27 | Verdict_after filled prematurely in Phase 3 Step B |
| V-04 | Two-pass + Dual-contract + Conjunction     | C-25 + C-26 + C-27    | C-01..C-24, C-25..C-27 | Three rules on one artifact; type gap in signals_added |
| V-05 | All four axes (full stack)                 | C-25..C-28            | C-01..C-28       | Type distinction for verdict_before vs signals_added "NONE" |

**Predicted leaderboard going into quest-score**: V-05 > V-04 > V-03 > V-01 >= V-02.

V-05 is the only variation covering all 23 criteria (C-01 through C-28). V-04 reaches
22/23 with three-axis delta enforcement, missing only the type-tightening note.
V-03 reaches 20/23 -- conjunction gate is the strongest single behavioral enforcement
but misses C-25 and C-26. V-01 and V-02 are single-axis: V-01 gets C-25 (lifecycle
order), V-02 gets C-26 (format). V-02 is the weakest single-axis because it is a
format criterion that does not inherently enforce delta.md presence.

The open question for scoring: does C-25 require the Post-Phase-4 update step to be
a declared named section, or is the terminal checklist item sufficient? V-01 has
both; V-04 and V-05 have both. Whether the terminal item alone would satisfy C-25
without the named update section will determine whether a minimal two-pass declaration
outscores the full structural pattern.
