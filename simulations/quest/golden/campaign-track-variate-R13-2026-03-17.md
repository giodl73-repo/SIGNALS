---
skill: quest-variate
skill_target: campaign-track
round: 13
date: 2026-03-17
rubric: simulations/quest/rubrics/campaign-track-rubric-v12-2026-03-17.md
---

# Variations -- campaign-track / Round 13

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

R12 closed C-36 and C-37 with V-05 scoring against the v11 rubric. Two PASS+
excellence signals from R12 V-05 follow the multi-site reinforcement pattern --
the same causal framing deployed at additional structural locations with distinct
framing dimensions:

- C-38 (from R12 V-05 C-36 PASS+): Phase Boundary Summary as second consequence
  site. The Phase 4 obligation consequence appears not only at the Phase 4 obligation
  header but also at the Phase Boundary Summary, where it is framed as an ambiguity
  failure mode -- "downstream systems cannot distinguish an interrupted campaign from
  a completed one." Two-site coverage with two structurally distinct consequence
  framings: stale-value at obligation header, ambiguity failure mode at boundary
  summary.

- C-39 (from R12 V-05 C-37 PASS+): Phase Boundary Summary addresses receiving scope
  independently of cascading scope. Two orthogonal structural sites address two
  distinct scope dimensions: (1) the Cascade Rule governs cascade scope -- what Phase
  3 Step B re-run does NOT update; (2) the Phase Boundary Summary governs receiving
  scope -- what Phase 4 does NOT receive as inputs. "Phase 4 does NOT receive
  namespace counts -- those were finalized at Phase 3 Step A and Phase 4 cannot
  change them. They are Phase 3 domain." The two arguments are independent: cascade
  scope applies at re-run time; receiving scope applies at Phase 4 entry.

Aspirational count goes from 24 to 26; max from 137 to 143.

R13 variation axes:
- V-01: Single-axis -- C-38 (ambiguity failure mode framing at Phase Boundary Summary)
- V-02: Single-axis -- C-39 (receiving scope as named independent subsection)
- V-03: Single-axis -- Named scope sections (structural axis: explicit section headers
  for each scope concern at the Phase 3->4 boundary)
- V-04: Combined -- C-38 + C-39
- V-05: Full stack -- C-38 + C-39 + named scope sections + three-site coverage

All five inherit the R12 V-05 baseline (SHALL phrasing, Phase Boundary Summary,
Cascade Rule with WHY, Phase 4 obligation with stale-value consequence, all
C-01 through C-37). Differences isolated to the Phase Boundary Summary Phase 3->4
section, the Phase 4 obligation header, and (V-03/V-05) section header structure.

---

## V-01 -- Axis: Ambiguity failure mode at Phase Boundary Summary (C-38 maximum)

**Hypothesis**: The Phase 4 obligation consequence has two distinct framings available:
stale-value framing ("verdict_after becomes stale") and ambiguity failure mode framing
("downstream systems cannot distinguish an interrupted campaign from a completed one").
R12 V-05 used stale-value framing at the obligation header and ambiguity-adjacent
language at the Phase Boundary Summary. C-38 requires the explicit ambiguity framing
at the boundary site: both states produce `verdict_after = NOT YET REACHED`, making
them indistinguishable. V-01 adds only C-38 to the R12 V-05 baseline. The receiving
scope argument in the Phase Boundary Summary is unchanged; there is no named receiving
scope subsection (C-39 absent).

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. A phase SHALL NOT proceed until the current
phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Each field typed
as integer SHALL contain an integer. Each field typed as enumerated string SHALL
contain exactly one of the listed tokens.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
- topic_name: string (non-empty)
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
    - signal_name: string (matches strategy.md signal_name)
    - collection_purpose: string (one sentence)

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
- echoes: list of strings; if none, value SHALL be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

### Session Delta Contract -- delta.md
- session_number: integer >= 1
- signals_added: list of signal names (empty list [] if none this session)
- signals_removed: list of signal names (empty list [] if none this session)
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
- verdict_changed: string, exactly one of: YES | NO | N/A

---

## Two-Pass Delta Rule

delta.md SHALL be written in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. The Phase 4 verdict is not yet known. The campaign
SHALL NOT compute a verdict_after value before Phase 4 runs.

Pass 2 (Post-Phase-4): After story.md is written, update verdict_after to the
actual verdict_verb from story.md. This is the only post-Phase-4 write.

The terminal checklist item for verdict_after is order-dependent: placeholder
"NOT YET REACHED" after Phase 4 completes is a defect unless Phase 4 verdict_verb
is also "NOT YET REACHED".

---

## Cascade Rule

When Phase 3 Step B is re-run (triggered by a Phase 3 postcondition failure after
Phase 4 has already completed), only verdict_after in delta.md SHALL be updated.

The remaining delta.md fields SHALL NOT be modified because they were finalized at
Phase 3 Step B and Phase 4 cannot change them: session_number was assigned,
signals_added and signals_removed were computed from the session diff, verdict_before
was read from the prior run's verdict, and verdict_changed was derived from the
before/after pair. These are session-scoped facts that exist independently of what
Phase 4 concludes. Cascading them would overwrite finalized session history with
Phase 4 data that is not session-scoped.

Only verdict_after is Phase 4-dependent, which is why it is the only cascade target.

---

## Phase Boundary Summary

Each phase has explicit inputs and outputs. This boundary summary is the governing
contract for phase ordering; it takes precedence over any inferred sequencing.

### Phase 1 -> Phase 2 Boundary
- Phase 1 output to Phase 2: strategy.md (topic_name, namespace, priority,
  planned_signals)
- Phase 2 input from Phase 1: planned_signals list, used to build namespace_coverage

### Phase 2 -> Phase 3 Boundary
- Phase 2 output to Phase 3: roadmap.md (namespace_coverage with collection_purpose
  per signal)
- Phase 3 input from Phase 2: namespace_coverage, used to populate planned counts
  and missing signal names

### Phase 3 -> Phase 4 Boundary
- Phase 3 Step A output to Phase 4: readiness_verdict and coverage_ratio from
  status.md -- these are read-only inputs to Phase 4 for context
- Phase 3 Step B output to Phase 4: delta.md with verdict_after placeholder --
  Phase 4 must update this via the Post-Phase-4 write
- Phase 4 does NOT receive namespace counts (planned, collected, missing,
  zero_flag) -- these fields were finalized at Phase 3 Step A and Phase 4 cannot
  change them. They are Phase 3 domain. Receiving them as inputs would imply Phase 4
  could revise them, which it cannot.
- Phase 4 obligation: write story.md. If Phase 4 completes without writing
  story.md, downstream systems cannot distinguish an interrupted campaign from a
  completed one -- both states produce `verdict_after = NOT YET REACHED` in delta.md.
  A campaign that ran Phase 4 and skipped the story.md write is indistinguishable
  from a campaign that never reached Phase 4. The ambiguity cannot be resolved from
  the delta.md artifact alone.

### Post-Phase-4 -> Dashboard Boundary
- Post-Phase-4 output: delta.md updated with actual verdict_after and verdict_changed
- Dashboard input: all five artifacts confirmed written; TERMINAL checklist PASS

---

## Prohibition Parity Rule

Each role SHALL carry exactly 5 forbidden actions -- no more, no fewer. Numbered
list format required (1 through 5). A role with 4 or 6 items SHALL fail audit.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)
Owns strategy.md.

Forbidden actions (exactly 5):
1. SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
2. SHALL NOT synthesize or interpret signal content
3. SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
4. SHALL NOT invoke any sub-skill other than topic-new
5. SHALL NOT list signals not declared in planned_signals

### Planner (Phase 2 -- topic-plan)
Owns roadmap.md.

Forbidden actions (exactly 5):
1. SHALL NOT register, rename, or modify topic identity (Phase 1 domain)
2. SHALL NOT query or report which signals are collected (Phase 3 domain)
3. SHALL NOT produce readiness verdicts or coverage ratios
4. SHALL NOT synthesize findings or assign verdict verbs
5. SHALL NOT invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)
Owns status.md AND delta.md. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md.

Forbidden actions (exactly 5):
1. SHALL NOT add planned signals beyond Phase 2 roadmap
2. SHALL NOT produce verdict verbs from Phase 4 vocabulary
3. SHALL NOT interpret meaning from signal content or editorialize
4. SHALL NOT invoke any sub-skill other than topic-status
5. SHALL NOT use narrative counts where integers are required

### Narrator (Phase 4 -- topic-story)
Owns story.md.

Forbidden actions (exactly 5):
1. SHALL NOT modify coverage table, namespace counts, or coverage ratio (Phase 3)
2. SHALL NOT add, remove, or reorder planned signals (Phase 2 domain)
3. SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. SHALL NOT invoke any sub-skill other than topic-story
5. SHALL NOT paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.
Boundary: Phase 1 produces strategy.md for Phase 2 input.*

The Registrar SHALL invoke topic-new for {{topic}}.

The Registrar SHALL produce strategy.md per Phase 1 Contract:
- topic_name, namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields typed correctly.

GATE: The campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.
Boundary: Phase 2 receives planned_signals from strategy.md; produces roadmap.md for
Phase 3 input.*

The Planner SHALL invoke topic-plan for {{topic}}.

The Planner SHALL produce roadmap.md per Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose per signal.

GATE: The campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md. Boundary: Phase 3 receives namespace_coverage
from roadmap.md; produces status.md (readiness_verdict, coverage_ratio) and delta.md
(placeholder verdict_after) for Phase 4 input.*

### Step A -- Coverage Status

The Analyst SHALL invoke topic-status for {{topic}}.

The Analyst SHALL produce status.md per Phase 3 Contract:
- All 9 namespace rows -- no row SHALL be skipped
- planned and collected SHALL be integers (narrative counts fail)
- missing SHALL list signal names as strings, not counts
- zero_flag SHALL be "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

The Analyst SHALL produce delta.md per Session Delta Contract.

Two-pass protocol: verdict_after SHALL be "NOT YET REACHED" (placeholder; Phase 4
not yet run). All other fields SHALL be written as final values at this step.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md both present. status.md has 9 rows,
integer fields, readiness_verdict assigned. delta.md has placeholder verdict_after.

GATE: The campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition is
satisfied.

---

## Phase 4 -- Narrative (Narrator)

**Obligation**: The Narrator SHALL write story.md before declaring Phase 4 complete.
If Phase 4 completes without writing story.md, downstream systems cannot distinguish
an interrupted campaign from a completed one -- `verdict_after` in `delta.md` remains
"NOT YET REACHED" in both cases. The ambiguity cannot be resolved from delta.md alone.

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.
Boundary: Phase 4 receives readiness_verdict and coverage_ratio from status.md as
read-only context; receives delta.md placeholder for post-write update. Phase 4 does
NOT receive namespace counts -- those were finalized at Phase 3 Step A.*

The Narrator SHALL invoke topic-story for {{topic}}.

The Narrator SHALL produce story.md per Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (SHALL NOT paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, SHALL contain minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, the model SHALL update delta.md:
- Set verdict_after = verdict_verb value from story.md
- Set verdict_changed = YES if verdict_after != verdict_before; NO if equal;
  N/A if verdict_before = NONE

Only verdict_after and verdict_changed are updated at this step. See Cascade Rule
for the boundary justification.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases SHALL run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. Founding artifact.
Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals planned.

Phase 3 (Analyst):
  Step A: All rows SHALL have collected = 0 (integer). missing SHALL list all
    planned signals by signal_name. zero_flag SHALL be "NO SIGNALS" where planned
    = 0 AND collected = 0. readiness_verdict SHALL be "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED" (placeholder).
    verdict_changed = "N/A".

Phase 4 (Narrator): Obligation applies on first invocation -- story.md SHALL be
  written; without it, the ambiguity failure mode activates even on first run.
  verdict_verb = "NOT YET REACHED". hypothesis_mutation.current = "UNCHANGED".
  echoes = ["NONE"]. recommendations: top 3 signals from roadmap.md by priority.

Post-Phase-4: verdict_after updated to "NOT YET REACHED". verdict_changed = "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

The model SHALL verify each field before declaring the campaign complete. A field
satisfying its constraint PASSES. Failure triggers re-run of the affected phase only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md
[ ] topic_name: string present, non-empty -- FAIL: re-run Phase 1
[ ] namespace: exactly one of 9 namespace tokens -- FAIL: re-run Phase 1
[ ] priority: exactly one of {High|Medium|Low} -- FAIL: re-run Phase 1
[ ] planned_signals: count >= 3 -- FAIL: re-run Phase 1
[ ] planned_signals[*].target_skill: namespace/skill format -- FAIL: re-run Phase 1

### Phase 2 -- roadmap.md
[ ] namespace_coverage: at least one entry -- FAIL: re-run Phase 2
[ ] namespace_coverage[*].collection_purpose: string per signal -- FAIL: re-run Phase 2

### Phase 3 -- status.md
[ ] row count: exactly 9 rows -- FAIL: re-run Phase 3
[ ] planned: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] collected: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] missing: list of names in each row -- FAIL: re-run Phase 3
[ ] zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0 -- FAIL: re-run Phase 3
[ ] coverage_ratio: "X/N" format -- FAIL: re-run Phase 3
[ ] readiness_verdict: one of {READY|NOT READY|CONDITIONALLY READY} -- FAIL: re-run Phase 3

### Phase 4 -- story.md
[ ] verdict_verb: one of 5 tokens -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.s0: string present, non-empty -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.current: string present -- FAIL: re-run Phase 4
[ ] echoes: list present, minimum ["NONE"] -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: exactly 3 items -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].namespace: string present -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].gap_reason: string present -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B
[ ] verdict_after: one of {READY|NOT READY|CONDITIONALLY READY|NOT YET REACHED};
    SHALL reflect Phase 4 verdict_verb; placeholder SHALL NOT remain after Phase 4
    completes unless Phase 4 verdict_verb is also "NOT YET REACHED"
    FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-37 (full R12 V-05 baseline), **C-38** (Phase
Boundary Summary Phase 3->4 obligation entry uses explicit ambiguity failure mode
framing: "downstream systems cannot distinguish an interrupted campaign from a
completed one -- both states produce `verdict_after = NOT YET REACHED`"; additionally
reinforced at Phase 4 obligation header and empty-state section -- three scoring
surfaces for C-38). **Misses**: C-39 (receiving scope is present in Phase Boundary
Summary as a bullet, but not structured as an independent named subsection; the
cascade/receiving scope independence argument is implicit, not structurally explicit).
**Risk**: The "ambiguity cannot be resolved from delta.md alone" line at the Phase 4
header may score C-38 independently of the Phase Boundary Summary site. Three scoring
surfaces for the ambiguity framing maximizes C-38 density.

---

## V-02 -- Axis: Receiving scope as independent named subsection (C-39 maximum)

**Hypothesis**: C-39 requires two orthogonal structural sites: the Cascade Rule
addresses cascade scope (verdict_after is the only update target at re-run), and the
Phase Boundary Summary addresses receiving scope (what Phase 4 does NOT receive at
entry). R12 V-05 had both but as bullet points within a single section. Making
receiving scope a named independent subsection -- with a header distinct from the
cascade argument and with an explicit cross-reference stating the two arguments are
independent -- creates an auditable two-site structure. V-02 adds only C-39 structure
to the R12 V-05 baseline. The Phase 4 obligation header uses stale-value framing only
(C-38 ambiguity framing absent).

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. A phase SHALL NOT proceed until the current
phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Each field typed
as integer SHALL contain an integer. Each field typed as enumerated string SHALL
contain exactly one of the listed tokens.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
- topic_name: string (non-empty)
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
    - signal_name: string (matches strategy.md signal_name)
    - collection_purpose: string (one sentence)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0
  - collected: integer >= 0
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N"
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md
- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none, value SHALL be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

### Session Delta Contract -- delta.md
- session_number: integer >= 1
- signals_added: list of signal names (empty list [] if none this session)
- signals_removed: list of signal names (empty list [] if none this session)
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
- verdict_changed: string, exactly one of: YES | NO | N/A

---

## Two-Pass Delta Rule

delta.md SHALL be written in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. The Phase 4 verdict is not yet known. The campaign
SHALL NOT compute a verdict_after value before Phase 4 runs.

Pass 2 (Post-Phase-4): After story.md is written, update verdict_after to the
actual verdict_verb from story.md. This is the only post-Phase-4 write.

The terminal checklist item for verdict_after is order-dependent: placeholder
"NOT YET REACHED" after Phase 4 completes is a defect unless Phase 4 verdict_verb
is also "NOT YET REACHED".

---

## Cascade Rule

When Phase 3 Step B is re-run (triggered by a Phase 3 postcondition failure after
Phase 4 has already completed), only verdict_after in delta.md SHALL be updated.
The cascade target is verdict_after alone.

The remaining delta.md fields SHALL NOT be modified because they were finalized at
Phase 3 Step B and Phase 4 cannot change them: session_number was assigned,
signals_added and signals_removed were computed from the session diff, verdict_before
was read from the prior run's verdict, and verdict_changed was derived from the
before/after pair. These are session-scoped facts that exist independently of what
Phase 4 concludes. Cascading them would overwrite finalized session history with
Phase 4 data that is not session-scoped.

Only verdict_after is Phase 4-dependent, which is why it is the only cascade target.

---

## Phase Boundary Summary

Each phase has explicit inputs and outputs. This boundary summary is the governing
contract for phase ordering; it takes precedence over any inferred sequencing.

### Phase 1 -> Phase 2 Boundary
- Phase 1 output to Phase 2: strategy.md (topic_name, namespace, priority,
  planned_signals)
- Phase 2 input from Phase 1: planned_signals list, used to build namespace_coverage

### Phase 2 -> Phase 3 Boundary
- Phase 2 output to Phase 3: roadmap.md (namespace_coverage with collection_purpose
  per signal)
- Phase 3 input from Phase 2: namespace_coverage, used to populate planned counts
  and missing signal names

### Phase 3 -> Phase 4 Boundary

**Inputs to Phase 4:**
- From Phase 3 Step A: readiness_verdict and coverage_ratio from status.md
  (read-only context; Phase 4 does not modify these)
- From Phase 3 Step B: delta.md with verdict_after = "NOT YET REACHED"
  (placeholder; Phase 4 updates this via the Post-Phase-4 write)

**Receiving Scope** (what Phase 4 does NOT receive as inputs):
Phase 4 does NOT receive namespace counts -- planned, collected, missing, and
zero_flag were finalized at Phase 3 Step A and Phase 4 cannot change them. They are
Phase 3 domain. A phase that receives a field as input implicitly claims the right to
revise it; Phase 4 makes no such claim on namespace counts.

This receiving scope exclusion is independent of the Cascade Rule's cascade scope.
The cascade argument applies when Phase 3 Step B is re-run after Phase 4 has
completed. The receiving scope argument applies at Phase 4 entry, before Phase 4
runs. The two arguments address the same Phase 3/4 boundary from orthogonal
directions: cascade scope governs what a re-run updates; receiving scope governs
what an initial entry receives.

**Phase 4 Obligation:**
Write story.md. If Phase 4 completes without writing story.md, `verdict_after` in
delta.md remains stale -- the "NOT YET REACHED" placeholder persists and downstream
delta comparisons cannot resolve the campaign's readiness state.

### Post-Phase-4 -> Dashboard Boundary
- Post-Phase-4 output: delta.md updated with actual verdict_after and verdict_changed
- Dashboard input: all five artifacts confirmed written; TERMINAL checklist PASS

---

## Prohibition Parity Rule

Each role SHALL carry exactly 5 forbidden actions -- no more, no fewer. Numbered
list format required (1 through 5). A role with 4 or 6 items SHALL fail audit.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)
Owns strategy.md.

Forbidden actions (exactly 5):
1. SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
2. SHALL NOT synthesize or interpret signal content
3. SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
4. SHALL NOT invoke any sub-skill other than topic-new
5. SHALL NOT list signals not declared in planned_signals

### Planner (Phase 2 -- topic-plan)
Owns roadmap.md.

Forbidden actions (exactly 5):
1. SHALL NOT register, rename, or modify topic identity (Phase 1 domain)
2. SHALL NOT query or report which signals are collected (Phase 3 domain)
3. SHALL NOT produce readiness verdicts or coverage ratios
4. SHALL NOT synthesize findings or assign verdict verbs
5. SHALL NOT invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)
Owns status.md AND delta.md. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md.

Forbidden actions (exactly 5):
1. SHALL NOT add planned signals beyond Phase 2 roadmap
2. SHALL NOT produce verdict verbs from Phase 4 vocabulary
3. SHALL NOT interpret meaning from signal content or editorialize
4. SHALL NOT invoke any sub-skill other than topic-status
5. SHALL NOT use narrative counts where integers are required

### Narrator (Phase 4 -- topic-story)
Owns story.md.

Forbidden actions (exactly 5):
1. SHALL NOT modify coverage table, namespace counts, or coverage ratio (Phase 3)
2. SHALL NOT add, remove, or reorder planned signals (Phase 2 domain)
3. SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. SHALL NOT invoke any sub-skill other than topic-story
5. SHALL NOT paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.
Boundary: Phase 1 produces strategy.md for Phase 2 input.*

The Registrar SHALL invoke topic-new for {{topic}}.

The Registrar SHALL produce strategy.md per Phase 1 Contract:
- topic_name, namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields typed correctly.

GATE: The campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.
Boundary: Phase 2 receives planned_signals from strategy.md; produces roadmap.md for
Phase 3 input.*

The Planner SHALL invoke topic-plan for {{topic}}.

The Planner SHALL produce roadmap.md per Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose per signal.

GATE: The campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md. Boundary: Phase 3 receives namespace_coverage
from roadmap.md; produces status.md (readiness_verdict, coverage_ratio) and delta.md
(placeholder verdict_after) for Phase 4 input.*

### Step A -- Coverage Status

The Analyst SHALL invoke topic-status for {{topic}}.

The Analyst SHALL produce status.md per Phase 3 Contract:
- All 9 namespace rows -- no row SHALL be skipped
- planned and collected SHALL be integers (narrative counts fail)
- missing SHALL list signal names as strings, not counts
- zero_flag SHALL be "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

The Analyst SHALL produce delta.md per Session Delta Contract.

Two-pass protocol: verdict_after SHALL be "NOT YET REACHED" (placeholder; Phase 4
not yet run). All other fields SHALL be written as final values at this step.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md both present. status.md has 9 rows,
integer fields, readiness_verdict assigned. delta.md has placeholder verdict_after.

GATE: The campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition is
satisfied.

---

## Phase 4 -- Narrative (Narrator)

**Obligation**: The Narrator SHALL write story.md before declaring Phase 4 complete.
If Phase 4 completes without writing story.md, `verdict_after` in `delta.md` becomes
stale -- the "NOT YET REACHED" placeholder persists indefinitely, and downstream
delta comparisons cannot determine the campaign's actual readiness state.

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.
Receiving scope: Phase 4 does NOT receive namespace counts -- planned, collected,
missing, zero_flag were finalized at Phase 3 Step A and Phase 4 cannot change them.
Phase 4 receives readiness_verdict and coverage_ratio from status.md as read-only
context, and delta.md placeholder for post-write update.*

The Narrator SHALL invoke topic-story for {{topic}}.

The Narrator SHALL produce story.md per Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (SHALL NOT paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, SHALL contain minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, the model SHALL update delta.md:
- Set verdict_after = verdict_verb value from story.md
- Set verdict_changed = YES if verdict_after != verdict_before; NO if equal;
  N/A if verdict_before = NONE

Only verdict_after and verdict_changed are updated at this step. See Cascade Rule
for the boundary justification.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases SHALL run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. Founding artifact.
Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals planned.

Phase 3 (Analyst):
  Step A: All rows SHALL have collected = 0 (integer). missing SHALL list all
    planned signals by signal_name. zero_flag SHALL be "NO SIGNALS" where planned
    = 0 AND collected = 0. readiness_verdict SHALL be "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED" (placeholder).
    verdict_changed = "N/A".

Phase 4 (Narrator): Obligation applies on first invocation -- story.md SHALL be
  written; without it, verdict_after in delta.md remains the placeholder.
  verdict_verb = "NOT YET REACHED". hypothesis_mutation.current = "UNCHANGED".
  echoes = ["NONE"]. recommendations: top 3 signals from roadmap.md by priority.

Post-Phase-4: verdict_after updated to "NOT YET REACHED". verdict_changed = "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

The model SHALL verify each field before declaring the campaign complete. A field
satisfying its constraint PASSES. Failure triggers re-run of the affected phase only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md
[ ] topic_name: string present, non-empty -- FAIL: re-run Phase 1
[ ] namespace: exactly one of 9 namespace tokens -- FAIL: re-run Phase 1
[ ] priority: exactly one of {High|Medium|Low} -- FAIL: re-run Phase 1
[ ] planned_signals: count >= 3 -- FAIL: re-run Phase 1
[ ] planned_signals[*].target_skill: namespace/skill format -- FAIL: re-run Phase 1

### Phase 2 -- roadmap.md
[ ] namespace_coverage: at least one entry -- FAIL: re-run Phase 2
[ ] namespace_coverage[*].collection_purpose: string per signal -- FAIL: re-run Phase 2

### Phase 3 -- status.md
[ ] row count: exactly 9 rows -- FAIL: re-run Phase 3
[ ] planned: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] collected: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] missing: list of names in each row -- FAIL: re-run Phase 3
[ ] zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0 -- FAIL: re-run Phase 3
[ ] coverage_ratio: "X/N" format -- FAIL: re-run Phase 3
[ ] readiness_verdict: one of {READY|NOT READY|CONDITIONALLY READY} -- FAIL: re-run Phase 3

### Phase 4 -- story.md
[ ] verdict_verb: one of 5 tokens -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.s0: string present, non-empty -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.current: string present -- FAIL: re-run Phase 4
[ ] echoes: list present, minimum ["NONE"] -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: exactly 3 items -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].namespace: string present -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].gap_reason: string present -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B
[ ] verdict_after: one of {READY|NOT READY|CONDITIONALLY READY|NOT YET REACHED};
    SHALL reflect Phase 4 verdict_verb; placeholder SHALL NOT remain after Phase 4
    completes unless Phase 4 verdict_verb is also "NOT YET REACHED"
    FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-37 (full R12 V-05 baseline), **C-39** (Phase
Boundary Summary Phase 3->4 has a named "Receiving Scope" subsection that independently
addresses what Phase 4 does NOT receive; explicit cross-reference states the receiving
scope argument is independent of the Cascade Rule's cascade scope argument; the two
structural sites are named and the independence is asserted; Phase 4 active-role header
reinforces with "receiving scope" language -- two scoring surfaces for C-39).
**Misses**: C-38 (Phase 4 obligation header and Phase Boundary Summary obligation
entry use stale-value framing without the explicit "cannot distinguish interrupted
from completed" ambiguity framing).
**Risk**: The Cascade Rule's WHY explanation (C-37) and the Phase Boundary Summary's
Receiving Scope subsection (C-39) may be scored as a single compound criterion rather
than two independent ones. The explicit cross-reference sentence ("The cascade
argument applies when Phase 3 Step B is re-run... The receiving scope argument applies
at Phase 4 entry...") is the key structural independence claim.

---

## V-03 -- Axis: Named scope sections at Phase 3->4 boundary (structural axis)

**Hypothesis**: Receiving scope and cascade scope address orthogonal concerns but are
typically distributed across different sections (Cascade Rule, Phase Boundary Summary)
without naming the orthogonality explicitly. A structural axis that gives each scope
concern a named section header -- "Cascade Scope" and "Receiving Scope" -- within the
Phase Boundary Summary makes the two-dimensional coverage auditable at the section
level rather than requiring a reader to cross-reference Cascade Rule with Phase
Boundary Summary bullets. V-03 tests whether section-level naming of the two scope
dimensions produces a new excellence pattern beyond what C-39 requires. This also
tests the lifecycle emphasis axis: the Phase 3->4 boundary section expands to carry
more structural weight than any other boundary.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. A phase SHALL NOT proceed until the current
phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Each field typed
as integer SHALL contain an integer. Each field typed as enumerated string SHALL
contain exactly one of the listed tokens.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
- topic_name: string (non-empty)
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
    - signal_name: string (matches strategy.md signal_name)
    - collection_purpose: string (one sentence)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0
  - collected: integer >= 0
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N"
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md
- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none, value SHALL be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

### Session Delta Contract -- delta.md
- session_number: integer >= 1
- signals_added: list of signal names (empty list [] if none this session)
- signals_removed: list of signal names (empty list [] if none this session)
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
- verdict_changed: string, exactly one of: YES | NO | N/A

---

## Two-Pass Delta Rule

delta.md SHALL be written in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. The Phase 4 verdict is not yet known.

Pass 2 (Post-Phase-4): After story.md is written, update verdict_after to the
actual verdict_verb from story.md. This is the only post-Phase-4 write.

The terminal checklist item for verdict_after is order-dependent: placeholder
"NOT YET REACHED" after Phase 4 completes is a defect unless Phase 4 verdict_verb
is also "NOT YET REACHED".

---

## Cascade Rule

When Phase 3 Step B is re-run (triggered by a Phase 3 postcondition failure after
Phase 4 has already completed), only verdict_after in delta.md SHALL be updated.
The cascade target is verdict_after alone.

The remaining delta.md fields SHALL NOT be modified because they were finalized at
Phase 3 Step B and Phase 4 cannot change them: session_number was assigned,
signals_added and signals_removed were computed from the session diff, verdict_before
was read from the prior run's verdict, and verdict_changed was derived from the
before/after pair. These are session-scoped facts that exist independently of what
Phase 4 concludes. Cascading them would overwrite finalized session history with
Phase 4 data that is not session-scoped.

Only verdict_after is Phase 4-dependent, which is why it is the only cascade target.

---

## Phase Boundary Summary

Each phase has explicit inputs and outputs. This boundary summary is the governing
contract for phase ordering; it takes precedence over any inferred sequencing.

### Phase 1 -> Phase 2 Boundary
- Phase 1 output to Phase 2: strategy.md (topic_name, namespace, priority,
  planned_signals)
- Phase 2 input from Phase 1: planned_signals list, used to build namespace_coverage

### Phase 2 -> Phase 3 Boundary
- Phase 2 output to Phase 3: roadmap.md (namespace_coverage with collection_purpose)
- Phase 3 input from Phase 2: namespace_coverage, used to populate planned counts
  and missing signal names

### Phase 3 -> Phase 4 Boundary

#### Cascade Scope
Governs what a Phase 3 Step B re-run updates. Applies post-Phase-4 only.
- Update target: verdict_after in delta.md (Phase 4-dependent value)
- Excluded: session_number, signals_added, signals_removed, verdict_before,
  verdict_changed (finalized at Phase 3 Step B; see Cascade Rule for justification)

#### Receiving Scope
Governs what Phase 4 receives as inputs at entry. Applies pre-Phase-4.
- Phase 4 receives: readiness_verdict and coverage_ratio from status.md (read-only),
  delta.md with verdict_after placeholder (for post-write update)
- Phase 4 does NOT receive: namespace counts (planned, collected, missing, zero_flag)
  -- finalized at Phase 3 Step A; Phase 4 cannot change them; they are Phase 3 domain

These two scope dimensions are orthogonal. Cascade scope applies at re-run time after
Phase 4 has completed. Receiving scope applies at Phase 4 entry. They address the
same Phase 3/4 boundary from different temporal positions: one governs what flows
back on error recovery; the other governs what flows forward on first execution.

#### Transition Obligation
- Phase 4 SHALL write story.md. If Phase 4 exits without writing story.md, downstream
  systems cannot distinguish an interrupted campaign from a completed one -- both
  states produce `verdict_after = NOT YET REACHED` in delta.md. The ambiguity is
  unresolvable from the artifact alone.

### Post-Phase-4 -> Dashboard Boundary
- Post-Phase-4 output: delta.md updated with actual verdict_after and verdict_changed
- Dashboard input: all five artifacts confirmed written; TERMINAL checklist PASS

---

## Prohibition Parity Rule

Each role SHALL carry exactly 5 forbidden actions -- no more, no fewer. Numbered
list format required (1 through 5). A role with 4 or 6 items SHALL fail audit.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)
Owns strategy.md.

Forbidden actions (exactly 5):
1. SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
2. SHALL NOT synthesize or interpret signal content
3. SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
4. SHALL NOT invoke any sub-skill other than topic-new
5. SHALL NOT list signals not declared in planned_signals

### Planner (Phase 2 -- topic-plan)
Owns roadmap.md.

Forbidden actions (exactly 5):
1. SHALL NOT register, rename, or modify topic identity (Phase 1 domain)
2. SHALL NOT query or report which signals are collected (Phase 3 domain)
3. SHALL NOT produce readiness verdicts or coverage ratios
4. SHALL NOT synthesize findings or assign verdict verbs
5. SHALL NOT invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)
Owns status.md AND delta.md. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md.

Forbidden actions (exactly 5):
1. SHALL NOT add planned signals beyond Phase 2 roadmap
2. SHALL NOT produce verdict verbs from Phase 4 vocabulary
3. SHALL NOT interpret meaning from signal content or editorialize
4. SHALL NOT invoke any sub-skill other than topic-status
5. SHALL NOT use narrative counts where integers are required

### Narrator (Phase 4 -- topic-story)
Owns story.md.

Forbidden actions (exactly 5):
1. SHALL NOT modify coverage table, namespace counts, or coverage ratio (Phase 3)
2. SHALL NOT add, remove, or reorder planned signals (Phase 2 domain)
3. SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. SHALL NOT invoke any sub-skill other than topic-story
5. SHALL NOT paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.
Boundary: Phase 1 produces strategy.md for Phase 2 input.*

The Registrar SHALL invoke topic-new for {{topic}}.

The Registrar SHALL produce strategy.md per Phase 1 Contract:
- topic_name, namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields typed correctly.

GATE: The campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.
Boundary: Phase 2 receives planned_signals from strategy.md; produces roadmap.md for
Phase 3 input.*

The Planner SHALL invoke topic-plan for {{topic}}.

The Planner SHALL produce roadmap.md per Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose per signal.

GATE: The campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md. Boundary: Phase 3 receives namespace_coverage
from roadmap.md; produces status.md and delta.md for Phase 4 input per Phase Boundary
Summary (Cascade Scope + Receiving Scope).*

### Step A -- Coverage Status

The Analyst SHALL invoke topic-status for {{topic}}.

The Analyst SHALL produce status.md per Phase 3 Contract:
- All 9 namespace rows -- no row SHALL be skipped
- planned and collected SHALL be integers (narrative counts fail)
- missing SHALL list signal names as strings, not counts
- zero_flag SHALL be "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

The Analyst SHALL produce delta.md per Session Delta Contract.

Two-pass protocol: verdict_after SHALL be "NOT YET REACHED" (placeholder; Phase 4
not yet run). All other fields SHALL be written as final values at this step.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md both present. status.md has 9 rows,
integer fields, readiness_verdict assigned. delta.md has placeholder verdict_after.

GATE: The campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition is
satisfied.

---

## Phase 4 -- Narrative (Narrator)

**Obligation**: The Narrator SHALL write story.md before declaring Phase 4 complete.
If Phase 4 exits without writing story.md, the Transition Obligation at the Phase 3->4
boundary is violated -- downstream systems cannot distinguish an interrupted campaign
from a completed one.

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.
Receiving scope (from Phase Boundary Summary): Phase 4 does NOT receive namespace
counts -- those are Phase 3 domain. Phase 4 receives readiness_verdict and
coverage_ratio from status.md as read-only context.*

The Narrator SHALL invoke topic-story for {{topic}}.

The Narrator SHALL produce story.md per Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (SHALL NOT paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, SHALL contain minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, the model SHALL update delta.md:
- Set verdict_after = verdict_verb value from story.md
- Set verdict_changed = YES if verdict_after != verdict_before; NO if equal;
  N/A if verdict_before = NONE

Only verdict_after and verdict_changed are updated at this step. See Cascade Rule
for the boundary justification.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases SHALL run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. Founding artifact.
Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals planned.

Phase 3 (Analyst):
  Step A: All rows SHALL have collected = 0 (integer). missing SHALL list all
    planned signals by signal_name. zero_flag SHALL be "NO SIGNALS" where planned
    = 0 AND collected = 0. readiness_verdict SHALL be "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED" (placeholder).
    verdict_changed = "N/A".

Phase 4 (Narrator): Obligation applies on first invocation -- story.md SHALL be
  written; without it, the Transition Obligation is violated and the ambiguity failure
  mode activates. verdict_verb = "NOT YET REACHED". hypothesis_mutation.current =
  "UNCHANGED". echoes = ["NONE"]. recommendations: top 3 from roadmap.md by priority.

Post-Phase-4: verdict_after updated to "NOT YET REACHED". verdict_changed = "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

The model SHALL verify each field before declaring the campaign complete. A field
satisfying its constraint PASSES. Failure triggers re-run of the affected phase only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md
[ ] topic_name: string present, non-empty -- FAIL: re-run Phase 1
[ ] namespace: exactly one of 9 namespace tokens -- FAIL: re-run Phase 1
[ ] priority: exactly one of {High|Medium|Low} -- FAIL: re-run Phase 1
[ ] planned_signals: count >= 3 -- FAIL: re-run Phase 1
[ ] planned_signals[*].target_skill: namespace/skill format -- FAIL: re-run Phase 1

### Phase 2 -- roadmap.md
[ ] namespace_coverage: at least one entry -- FAIL: re-run Phase 2
[ ] namespace_coverage[*].collection_purpose: string per signal -- FAIL: re-run Phase 2

### Phase 3 -- status.md
[ ] row count: exactly 9 rows -- FAIL: re-run Phase 3
[ ] planned: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] collected: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] missing: list of names in each row -- FAIL: re-run Phase 3
[ ] zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0 -- FAIL: re-run Phase 3
[ ] coverage_ratio: "X/N" format -- FAIL: re-run Phase 3
[ ] readiness_verdict: one of {READY|NOT READY|CONDITIONALLY READY} -- FAIL: re-run Phase 3

### Phase 4 -- story.md
[ ] verdict_verb: one of 5 tokens -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.s0: string present, non-empty -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.current: string present -- FAIL: re-run Phase 4
[ ] echoes: list present, minimum ["NONE"] -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: exactly 3 items -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].namespace: string present -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].gap_reason: string present -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B
[ ] verdict_after: one of {READY|NOT READY|CONDITIONALLY READY|NOT YET REACHED};
    SHALL reflect Phase 4 verdict_verb; placeholder SHALL NOT remain after Phase 4
    completes unless Phase 4 verdict_verb is also "NOT YET REACHED"
    FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-37 (full R12 V-05 baseline), **C-38** (Transition
Obligation subsection in Phase Boundary Summary uses explicit "cannot distinguish an
interrupted campaign from a completed one" framing; additionally reinforced at Phase 4
obligation header via "Transition Obligation at the Phase 3->4 boundary is violated"
cross-reference; empty-state section also reinforces -- three surfaces), **C-39**
(Phase Boundary Summary has named Cascade Scope and Receiving Scope subsections with
explicit "orthogonal" framing; Phase 4 active-role header references "Receiving scope
(from Phase Boundary Summary)"; the named section structure makes the two-dimensional
coverage auditable at the header level).
**New pattern to watch**: The named Cascade Scope / Receiving Scope / Transition
Obligation triptych at the Phase 3->4 boundary creates a three-dimensional taxonomy.
If this structural taxonomy produces a PASS+ signal, it would extend C-38/C-39 into
a C-40 criterion around explicit scope-dimension naming at boundary sites.
**Risk**: V-03 is the longest variation. Named subsections add structure but may dilute
the causal framing that C-37/C-38/C-39 reward. The "orthogonal" label at the scope
dimensions is untested.

---

## V-04 -- Combined: C-38 + C-39 (ambiguity framing + independent receiving scope)

**Hypothesis**: C-38 and C-39 address the Phase 3/4 boundary from complementary angles:
C-38 names what happens if Phase 4 skips its write (ambiguity failure mode -- the two
states are indistinguishable); C-39 names what Phase 4 is not permitted to receive
(receiving scope exclusion independent of cascade scope). Together they close both
dimensions of the Phase 3/4 data contract: what flows forward (receiving scope) and
what breaks if the phase exits without fulfilling its obligation (consequence framing).
V-04 combines V-01's ambiguity framing with V-02's named Receiving Scope subsection,
without the V-03 structural naming overhead.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. A phase SHALL NOT proceed until the current
phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Each field typed
as integer SHALL contain an integer. Each field typed as enumerated string SHALL
contain exactly one of the listed tokens.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
- topic_name: string (non-empty)
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
    - signal_name: string (matches strategy.md signal_name)
    - collection_purpose: string (one sentence)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0
  - collected: integer >= 0
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N"
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md
- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none, value SHALL be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

### Session Delta Contract -- delta.md
- session_number: integer >= 1
- signals_added: list of signal names (empty list [] if none this session)
- signals_removed: list of signal names (empty list [] if none this session)
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
- verdict_changed: string, exactly one of: YES | NO | N/A

---

## Two-Pass Delta Rule

delta.md SHALL be written in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. The Phase 4 verdict is not yet known.

Pass 2 (Post-Phase-4): After story.md is written, update verdict_after to the
actual verdict_verb from story.md. This is the only post-Phase-4 write.

The terminal checklist item for verdict_after is order-dependent: placeholder
"NOT YET REACHED" after Phase 4 completes is a defect unless Phase 4 verdict_verb
is also "NOT YET REACHED".

---

## Cascade Rule

When Phase 3 Step B is re-run (triggered by a Phase 3 postcondition failure after
Phase 4 has already completed), only verdict_after in delta.md SHALL be updated.
The cascade target is verdict_after alone.

The remaining delta.md fields SHALL NOT be modified because they were finalized at
Phase 3 Step B and Phase 4 cannot change them: session_number was assigned,
signals_added and signals_removed were computed from the session diff, verdict_before
was read from the prior run's verdict, and verdict_changed was derived from the
before/after pair. These are session-scoped facts that exist independently of what
Phase 4 concludes. Cascading them would overwrite finalized session history with
Phase 4 data that is not session-scoped.

Only verdict_after is Phase 4-dependent, which is why it is the only cascade target.

---

## Phase Boundary Summary

Each phase has explicit inputs and outputs. This boundary summary is the governing
contract for phase ordering; it takes precedence over any inferred sequencing.

### Phase 1 -> Phase 2 Boundary
- Phase 1 output to Phase 2: strategy.md (topic_name, namespace, priority,
  planned_signals)
- Phase 2 input from Phase 1: planned_signals list, used to build namespace_coverage

### Phase 2 -> Phase 3 Boundary
- Phase 2 output to Phase 3: roadmap.md (namespace_coverage with collection_purpose)
- Phase 3 input from Phase 2: namespace_coverage, used to populate planned counts
  and missing signal names

### Phase 3 -> Phase 4 Boundary

**Inputs to Phase 4:**
- From Phase 3 Step A: readiness_verdict and coverage_ratio from status.md (read-only)
- From Phase 3 Step B: delta.md with verdict_after = "NOT YET REACHED" (placeholder)

**Receiving Scope** (what Phase 4 does NOT receive as inputs):
Phase 4 does NOT receive namespace counts -- planned, collected, missing, and
zero_flag were finalized at Phase 3 Step A and Phase 4 cannot change them. They are
Phase 3 domain. A phase that receives a field as input implicitly claims the right
to revise it; Phase 4 makes no such claim on namespace counts.

This receiving scope exclusion is independent of the Cascade Rule's cascade scope.
The cascade argument applies when Phase 3 Step B is re-run after Phase 4 has
completed. The receiving scope argument applies at Phase 4 entry, before Phase 4
runs. Two orthogonal directions at the same boundary: what flows forward on first
execution; what updates on error recovery.

**Phase 4 Obligation:**
Phase 4 SHALL write story.md. If Phase 4 completes without writing story.md,
downstream systems cannot distinguish an interrupted campaign from a completed one --
both states produce `verdict_after = NOT YET REACHED` in delta.md. A campaign that
ran Phase 4 and skipped the write is indistinguishable from a campaign that never
reached Phase 4. The ambiguity is unresolvable from delta.md alone.

### Post-Phase-4 -> Dashboard Boundary
- Post-Phase-4 output: delta.md updated with actual verdict_after and verdict_changed
- Dashboard input: all five artifacts confirmed written; TERMINAL checklist PASS

---

## Prohibition Parity Rule

Each role SHALL carry exactly 5 forbidden actions -- no more, no fewer. Numbered
list format required (1 through 5). A role with 4 or 6 items SHALL fail audit.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)
Owns strategy.md.

Forbidden actions (exactly 5):
1. SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
2. SHALL NOT synthesize or interpret signal content
3. SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
4. SHALL NOT invoke any sub-skill other than topic-new
5. SHALL NOT list signals not declared in planned_signals

### Planner (Phase 2 -- topic-plan)
Owns roadmap.md.

Forbidden actions (exactly 5):
1. SHALL NOT register, rename, or modify topic identity (Phase 1 domain)
2. SHALL NOT query or report which signals are collected (Phase 3 domain)
3. SHALL NOT produce readiness verdicts or coverage ratios
4. SHALL NOT synthesize findings or assign verdict verbs
5. SHALL NOT invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)
Owns status.md AND delta.md. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md.

Forbidden actions (exactly 5):
1. SHALL NOT add planned signals beyond Phase 2 roadmap
2. SHALL NOT produce verdict verbs from Phase 4 vocabulary
3. SHALL NOT interpret meaning from signal content or editorialize
4. SHALL NOT invoke any sub-skill other than topic-status
5. SHALL NOT use narrative counts where integers are required

### Narrator (Phase 4 -- topic-story)
Owns story.md.

Forbidden actions (exactly 5):
1. SHALL NOT modify coverage table, namespace counts, or coverage ratio (Phase 3)
2. SHALL NOT add, remove, or reorder planned signals (Phase 2 domain)
3. SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. SHALL NOT invoke any sub-skill other than topic-story
5. SHALL NOT paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.
Boundary: Phase 1 produces strategy.md for Phase 2 input.*

The Registrar SHALL invoke topic-new for {{topic}}.

The Registrar SHALL produce strategy.md per Phase 1 Contract:
- topic_name, namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields typed correctly.

GATE: The campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.
Boundary: Phase 2 receives planned_signals from strategy.md; produces roadmap.md for
Phase 3 input.*

The Planner SHALL invoke topic-plan for {{topic}}.

The Planner SHALL produce roadmap.md per Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose per signal.

GATE: The campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md. Boundary: Phase 3 receives namespace_coverage
from roadmap.md; produces status.md and delta.md for Phase 4 input per Phase Boundary
Summary.*

### Step A -- Coverage Status

The Analyst SHALL invoke topic-status for {{topic}}.

The Analyst SHALL produce status.md per Phase 3 Contract:
- All 9 namespace rows -- no row SHALL be skipped
- planned and collected SHALL be integers (narrative counts fail)
- missing SHALL list signal names as strings, not counts
- zero_flag SHALL be "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

The Analyst SHALL produce delta.md per Session Delta Contract.

Two-pass protocol: verdict_after SHALL be "NOT YET REACHED" (placeholder; Phase 4
not yet run). All other fields SHALL be written as final values at this step.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md both present. status.md has 9 rows,
integer fields, readiness_verdict assigned. delta.md has placeholder verdict_after.

GATE: The campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition is
satisfied.

---

## Phase 4 -- Narrative (Narrator)

**Obligation**: The Narrator SHALL write story.md before declaring Phase 4 complete.
If Phase 4 completes without writing story.md, downstream systems cannot distinguish
an interrupted campaign from a completed one -- `verdict_after` remains "NOT YET
REACHED" in both cases. The ambiguity cannot be resolved from delta.md alone.

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.
Receiving scope: Phase 4 does NOT receive namespace counts (planned, collected,
missing, zero_flag) -- those are Phase 3 domain, finalized at Phase 3 Step A.
Phase 4 receives readiness_verdict and coverage_ratio as read-only context.*

The Narrator SHALL invoke topic-story for {{topic}}.

The Narrator SHALL produce story.md per Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (SHALL NOT paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, SHALL contain minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, the model SHALL update delta.md:
- Set verdict_after = verdict_verb value from story.md
- Set verdict_changed = YES if verdict_after != verdict_before; NO if equal;
  N/A if verdict_before = NONE

Only verdict_after and verdict_changed are updated. See Cascade Rule for justification.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases SHALL run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. Founding artifact.
Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals planned.

Phase 3 (Analyst):
  Step A: All rows SHALL have collected = 0 (integer). missing SHALL list all
    planned signals by signal_name. zero_flag SHALL be "NO SIGNALS" where planned
    = 0 AND collected = 0. readiness_verdict SHALL be "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED" (placeholder).
    verdict_changed = "N/A".

Phase 4 (Narrator): Obligation applies on first invocation -- story.md SHALL be
  written; without it, the ambiguity failure mode activates even on first run.
  verdict_verb = "NOT YET REACHED". hypothesis_mutation.current = "UNCHANGED".
  echoes = ["NONE"]. recommendations: top 3 signals from roadmap.md by priority.

Post-Phase-4: verdict_after updated to "NOT YET REACHED". verdict_changed = "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

The model SHALL verify each field before declaring the campaign complete. A field
satisfying its constraint PASSES. Failure triggers re-run of the affected phase only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md
[ ] topic_name: string present, non-empty -- FAIL: re-run Phase 1
[ ] namespace: exactly one of 9 namespace tokens -- FAIL: re-run Phase 1
[ ] priority: exactly one of {High|Medium|Low} -- FAIL: re-run Phase 1
[ ] planned_signals: count >= 3 -- FAIL: re-run Phase 1
[ ] planned_signals[*].target_skill: namespace/skill format -- FAIL: re-run Phase 1

### Phase 2 -- roadmap.md
[ ] namespace_coverage: at least one entry -- FAIL: re-run Phase 2
[ ] namespace_coverage[*].collection_purpose: string per signal -- FAIL: re-run Phase 2

### Phase 3 -- status.md
[ ] row count: exactly 9 rows -- FAIL: re-run Phase 3
[ ] planned: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] collected: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] missing: list of names in each row -- FAIL: re-run Phase 3
[ ] zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0 -- FAIL: re-run Phase 3
[ ] coverage_ratio: "X/N" format -- FAIL: re-run Phase 3
[ ] readiness_verdict: one of {READY|NOT READY|CONDITIONALLY READY} -- FAIL: re-run Phase 3

### Phase 4 -- story.md
[ ] verdict_verb: one of 5 tokens -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.s0: string present, non-empty -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.current: string present -- FAIL: re-run Phase 4
[ ] echoes: list present, minimum ["NONE"] -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: exactly 3 items -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].namespace: string present -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].gap_reason: string present -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B
[ ] verdict_after: one of {READY|NOT READY|CONDITIONALLY READY|NOT YET REACHED};
    SHALL reflect Phase 4 verdict_verb; placeholder SHALL NOT remain after Phase 4
    completes unless Phase 4 verdict_verb is also "NOT YET REACHED"
    FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-37 (full R12 V-05 baseline), **C-38** (Phase
Boundary Summary Phase 4 Obligation entry: "downstream systems cannot distinguish an
interrupted campaign from a completed one -- both states produce `verdict_after = NOT
YET REACHED`"; Phase 4 obligation header uses same framing; empty-state reinforces
-- three surfaces), **C-39** (named "Receiving Scope" subsection in Phase Boundary
Summary with explicit independence claim: "This receiving scope exclusion is
independent of the Cascade Rule's cascade scope"; Phase 4 active-role header
reinforces receiving scope language -- two surfaces).
**Risk**: V-04 duplicates scoring surface coverage of V-05 without the lifecycle axis.
If the named section structure in V-03 turns out to be load-bearing for C-39 scoring,
V-04 will score lower than V-05 despite hitting both C-38 and C-39. The independence
claim sentence is the key testable element.

---

## V-05 -- Full stack: C-38 + C-39 + named scope sections + three-site coverage

**Hypothesis**: Maximum scoring surface density for C-38 and C-39 comes from three
properties acting together: (1) explicit ambiguity failure mode framing at Phase 4
obligation header AND Phase Boundary Summary Transition Obligation AND empty-state
section (three C-38 surfaces); (2) named independent receiving scope subsection at
Phase Boundary Summary with explicit cross-reference to Cascade Rule (C-39 maximum);
(3) named section structure -- Cascade Scope / Receiving Scope / Transition Obligation
-- that makes the three-dimensional boundary taxonomy auditable at the header level
(potential C-40 surface). V-05 is the full-stack baseline for R13.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. A phase SHALL NOT proceed until the current
phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Each field typed
as integer SHALL contain an integer. Each field typed as enumerated string SHALL
contain exactly one of the listed tokens.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
- topic_name: string (non-empty)
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
    - signal_name: string (matches strategy.md signal_name)
    - collection_purpose: string (one sentence)

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
- echoes: list of strings; if none, value SHALL be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

### Session Delta Contract -- delta.md
- session_number: integer >= 1
- signals_added: list of signal names (empty list [] if none this session)
- signals_removed: list of signal names (empty list [] if none this session)
- verdict_before: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NONE
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
- verdict_changed: string, exactly one of: YES | NO | N/A

---

## Two-Pass Delta Rule

delta.md SHALL be written in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. The Phase 4 verdict is not yet known. The campaign
SHALL NOT compute a verdict_after value before Phase 4 runs.

Pass 2 (Post-Phase-4): After story.md is written, update verdict_after to the
actual verdict_verb from story.md. This is the only post-Phase-4 write.

The terminal checklist item for verdict_after is order-dependent: placeholder
"NOT YET REACHED" after Phase 4 completes is a defect unless Phase 4 verdict_verb
is also "NOT YET REACHED".

---

## Cascade Rule

When Phase 3 Step B is re-run (triggered by a Phase 3 postcondition failure after
Phase 4 has already completed), only verdict_after in delta.md SHALL be updated.
The cascade target is verdict_after alone.

The remaining delta.md fields SHALL NOT be modified because they were finalized at
Phase 3 Step B and Phase 4 cannot change them: session_number was assigned,
signals_added and signals_removed were computed from the session diff, verdict_before
was read from the prior run's verdict, and verdict_changed was derived from the
before/after pair. These are session-scoped facts that exist independently of what
Phase 4 concludes. Cascading them would overwrite finalized session history with
Phase 4 data that is not session-scoped.

Only verdict_after is Phase 4-dependent, which is why it is the only cascade target.

---

## Phase Boundary Summary

Each phase has explicit inputs and outputs. This boundary summary is the governing
contract for phase ordering; it takes precedence over any inferred sequencing.

### Phase 1 -> Phase 2 Boundary
- Phase 1 output to Phase 2: strategy.md (topic_name, namespace, priority,
  planned_signals)
- Phase 2 input from Phase 1: planned_signals list, used to build namespace_coverage

### Phase 2 -> Phase 3 Boundary
- Phase 2 output to Phase 3: roadmap.md (namespace_coverage with collection_purpose
  per signal)
- Phase 3 input from Phase 2: namespace_coverage, used to populate planned counts
  and missing signal names

### Phase 3 -> Phase 4 Boundary

#### Cascade Scope
Governs what a Phase 3 Step B re-run updates. Applies when Phase 3 is re-run after
Phase 4 has already completed. Defined in Cascade Rule above.
- Update target: verdict_after in delta.md (Phase 4-dependent; sole cascade target)
- Excluded from cascade: session_number, signals_added, signals_removed,
  verdict_before, verdict_changed (finalized at Phase 3 Step B; Phase 4 does not own)

#### Receiving Scope
Governs what Phase 4 receives as inputs at entry. Applies before Phase 4 runs.
Independent of Cascade Scope: cascade scope is a re-run concern; receiving scope is
an entry concern. They address the same Phase 3/4 boundary from orthogonal temporal
positions.

- Phase 4 receives: readiness_verdict and coverage_ratio from status.md (read-only
  context; Phase 4 does not modify these values)
- Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED" (placeholder;
  Phase 4 updates this via the Post-Phase-4 write)
- Phase 4 does NOT receive: namespace counts (planned, collected, missing, zero_flag)
  -- finalized at Phase 3 Step A; Phase 4 cannot change them; they are Phase 3 domain.
  A phase that receives a field as input implicitly claims the right to revise it;
  Phase 4 makes no such claim on namespace counts.

#### Transition Obligation
The obligation that Phase 4 must fulfill before the boundary closes.

Phase 4 SHALL write story.md. If Phase 4 exits without writing story.md, downstream
systems cannot distinguish an interrupted campaign from a completed one -- both states
produce `verdict_after = NOT YET REACHED` in delta.md. A campaign that ran Phase 4
and skipped the story.md write is indistinguishable from a campaign that never reached
Phase 4 at all. The ambiguity is unresolvable from the delta.md artifact alone.

### Post-Phase-4 -> Dashboard Boundary
- Post-Phase-4 output: delta.md updated with actual verdict_after (verdict_verb from
  story.md) and verdict_changed
- Dashboard input: all five artifacts confirmed written; TERMINAL checklist PASS

---

## Prohibition Parity Rule

Each role SHALL carry exactly 5 forbidden actions -- no more, no fewer. Numbered
list format required (1 through 5). A role with 4 or 6 items SHALL fail audit.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)
Owns strategy.md.

Forbidden actions (exactly 5):
1. SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
2. SHALL NOT synthesize or interpret signal content
3. SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
4. SHALL NOT invoke any sub-skill other than topic-new
5. SHALL NOT list signals not declared in planned_signals

### Planner (Phase 2 -- topic-plan)
Owns roadmap.md.

Forbidden actions (exactly 5):
1. SHALL NOT register, rename, or modify topic identity (Phase 1 domain)
2. SHALL NOT query or report which signals are collected (Phase 3 domain)
3. SHALL NOT produce readiness verdicts or coverage ratios
4. SHALL NOT synthesize findings or assign verdict verbs
5. SHALL NOT invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)
Owns status.md AND delta.md. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md.

Forbidden actions (exactly 5):
1. SHALL NOT add planned signals beyond Phase 2 roadmap
2. SHALL NOT produce verdict verbs from Phase 4 vocabulary
3. SHALL NOT interpret meaning from signal content or editorialize
4. SHALL NOT invoke any sub-skill other than topic-status
5. SHALL NOT use narrative counts where integers are required

### Narrator (Phase 4 -- topic-story)
Owns story.md.

Forbidden actions (exactly 5):
1. SHALL NOT modify coverage table, namespace counts, or coverage ratio (Phase 3)
2. SHALL NOT add, remove, or reorder planned signals (Phase 2 domain)
3. SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. SHALL NOT invoke any sub-skill other than topic-story
5. SHALL NOT paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.
Boundary: Phase 1 produces strategy.md for Phase 2 input.*

The Registrar SHALL invoke topic-new for {{topic}}.

The Registrar SHALL produce strategy.md per Phase 1 Contract:
- topic_name, namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields typed correctly.

GATE: The campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.
Boundary: Phase 2 receives planned_signals from strategy.md; produces roadmap.md for
Phase 3 input.*

The Planner SHALL invoke topic-plan for {{topic}}.

The Planner SHALL produce roadmap.md per Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose per signal.

GATE: The campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md. Boundary: Phase 3 receives namespace_coverage
from roadmap.md; produces status.md and delta.md for Phase 4 input per Phase Boundary
Summary (Cascade Scope + Receiving Scope + Transition Obligation).*

### Step A -- Coverage Status

The Analyst SHALL invoke topic-status for {{topic}}.

The Analyst SHALL produce status.md per Phase 3 Contract:
- All 9 namespace rows -- no row SHALL be skipped
- planned and collected SHALL be integers (narrative counts fail)
- missing SHALL list signal names as strings, not counts
- zero_flag SHALL be "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

The Analyst SHALL produce delta.md per Session Delta Contract.

Two-pass protocol: verdict_after SHALL be "NOT YET REACHED" (placeholder; Phase 4
not yet run). All other fields SHALL be written as final values at this step.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md both present. status.md has 9 rows,
integer fields, readiness_verdict assigned. delta.md has placeholder verdict_after.

GATE: The campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition is
satisfied.

---

## Phase 4 -- Narrative (Narrator)

**Obligation**: The Narrator SHALL write story.md before declaring Phase 4 complete.
If Phase 4 completes without writing story.md, downstream systems cannot distinguish
an interrupted campaign from a completed one -- `verdict_after` remains "NOT YET
REACHED" in both cases. The Transition Obligation (Phase Boundary Summary, Phase 3->4)
is violated. The ambiguity cannot be resolved from the delta.md artifact alone.

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.
Receiving scope (Phase Boundary Summary, Phase 3->4): Phase 4 does NOT receive
namespace counts -- planned, collected, missing, zero_flag were finalized at Phase 3
Step A and Phase 4 cannot change them. They are Phase 3 domain. Phase 4 receives
readiness_verdict and coverage_ratio from status.md as read-only context.*

The Narrator SHALL invoke topic-story for {{topic}}.

The Narrator SHALL produce story.md per Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (SHALL NOT paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, SHALL contain minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, the model SHALL update delta.md:
- Set verdict_after = verdict_verb value from story.md
- Set verdict_changed = YES if verdict_after != verdict_before; NO if equal;
  N/A if verdict_before = NONE

Only verdict_after and verdict_changed are updated at this step. See Cascade Rule
for the boundary justification.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases SHALL run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. Founding artifact.
Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals planned.

Phase 3 (Analyst):
  Step A: All rows SHALL have collected = 0 (integer). missing SHALL list all
    planned signals by signal_name. zero_flag SHALL be "NO SIGNALS" where planned
    = 0 AND collected = 0. readiness_verdict SHALL be "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED" (placeholder).
    verdict_changed = "N/A".

Phase 4 (Narrator): The Transition Obligation applies on first invocation -- story.md
  SHALL be written; without it, downstream systems cannot distinguish an interrupted
  first session from a completed one. verdict_verb = "NOT YET REACHED".
  hypothesis_mutation.current = "UNCHANGED". echoes = ["NONE"].
  recommendations: top 3 signals from roadmap.md by priority.

Post-Phase-4: verdict_after updated to "NOT YET REACHED". verdict_changed = "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

The model SHALL verify each field before declaring the campaign complete. A field
satisfying its constraint PASSES. Failure triggers re-run of the affected phase only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md
[ ] topic_name: string present, non-empty -- FAIL: re-run Phase 1
[ ] namespace: exactly one of 9 namespace tokens -- FAIL: re-run Phase 1
[ ] priority: exactly one of {High|Medium|Low} -- FAIL: re-run Phase 1
[ ] planned_signals: count >= 3 -- FAIL: re-run Phase 1
[ ] planned_signals[*].target_skill: namespace/skill format -- FAIL: re-run Phase 1

### Phase 2 -- roadmap.md
[ ] namespace_coverage: at least one entry -- FAIL: re-run Phase 2
[ ] namespace_coverage[*].collection_purpose: string per signal -- FAIL: re-run Phase 2

### Phase 3 -- status.md
[ ] row count: exactly 9 rows -- FAIL: re-run Phase 3
[ ] planned: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] collected: integer in all 9 rows -- FAIL: re-run Phase 3
[ ] missing: list of names in each row -- FAIL: re-run Phase 3
[ ] zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0 -- FAIL: re-run Phase 3
[ ] coverage_ratio: "X/N" format -- FAIL: re-run Phase 3
[ ] readiness_verdict: one of {READY|NOT READY|CONDITIONALLY READY} -- FAIL: re-run Phase 3

### Phase 4 -- story.md
[ ] verdict_verb: one of 5 tokens -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.s0: string present, non-empty -- FAIL: re-run Phase 4
[ ] hypothesis_mutation.current: string present -- FAIL: re-run Phase 4
[ ] echoes: list present, minimum ["NONE"] -- FAIL: re-run Phase 4
[ ] next_signal_recommendations: exactly 3 items -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].namespace: string present -- FAIL: re-run Phase 4
[ ] next_signal_recommendations[*].gap_reason: string present -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B
[ ] verdict_after: one of {READY|NOT READY|CONDITIONALLY READY|NOT YET REACHED};
    SHALL reflect Phase 4 verdict_verb; placeholder SHALL NOT remain after Phase 4
    completes unless Phase 4 verdict_verb is also "NOT YET REACHED"
    FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-37 (full R12 V-05 baseline), **C-38** (Phase
Boundary Summary Transition Obligation: "downstream systems cannot distinguish an
interrupted campaign from a completed one"; Phase 4 obligation header: same framing
plus "Transition Obligation (Phase Boundary Summary, Phase 3->4) is violated";
empty-state section: "cannot distinguish an interrupted first session from a completed
one" -- three scoring surfaces), **C-39** (Phase Boundary Summary has named Receiving
Scope subsection with explicit "Independent of Cascade Scope" framing; Cascade Scope
named subsection cross-references Cascade Rule; Phase 4 active-role header: "Receiving
scope (Phase Boundary Summary, Phase 3->4)" -- two scoring surfaces; named subsection
structure creates structural independence at the header level), **potential C-40**
(three-dimensional boundary taxonomy: Cascade Scope / Receiving Scope / Transition
Obligation as named section headers; if this produces a PASS+ signal, C-40 would
reward explicit scope-dimension naming at phase boundaries).
**Risk**: V-05 is the longest variation. The three-dimensional taxonomy adds structural
weight but may not produce scoring gain if C-38/C-39 score presence only rather than
per-occurrence. The Phase 4 active-role header cross-reference "(Phase Boundary
Summary, Phase 3->4)" is the key distinguishing element over V-04.

---

## Variation Summary

| ID   | Primary Axes                                            | New Criteria Targeted | Key Differentiator                                                   |
|------|----------------------------------------------------------|-----------------------|----------------------------------------------------------------------|
| V-01 | C-38 only (ambiguity failure mode)                       | C-38                  | "cannot distinguish interrupted from completed" at PB Summary + P4   |
| V-02 | C-39 only (named receiving scope subsection)             | C-39                  | "Receiving Scope" named subsection + independence claim in PB Summary |
| V-03 | Named scope sections (structural axis)                   | C-38 + C-39 + C-40?   | Cascade/Receiving/Transition triptych as named section headers       |
| V-04 | C-38 + C-39 combined                                     | C-38 + C-39           | Ambiguity framing + independent receiving scope; no section headers  |
| V-05 | C-38 + C-39 + named sections + three-site coverage       | C-38 + C-39 + C-40?   | Full stack; three surfaces each; explicit independence cross-refs    |

**Predicted leaderboard going into quest-score**: V-05 > V-04 > V-03 > V-01 = V-02.

V-05 achieves maximum scoring surface density for C-38 and C-39, inherits the full
prior baseline, and introduces the three-dimensional taxonomy that may produce C-40.
V-04 hits both C-38 and C-39 without the structural overhead. V-03 tests the named
section structure against the rubric -- it targets C-38 and C-39 but via the
structural axis rather than the explicit ambiguity/independence framing, so it may
score lower than V-04 if the criteria reward specific causal language over structure.
V-01 and V-02 isolate one new criterion each; predicted to tie unless C-38 carries
higher weight than C-39 in v12.

The main open question: does the Transition Obligation named subsection in V-03/V-05
produce a C-40 signal around explicit scope-dimension naming at boundary sites, or
does it simply replicate C-38/C-39 coverage with more words?
