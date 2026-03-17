---
skill: quest-variate
skill_target: campaign-track
round: 14
date: 2026-03-17
rubric: simulations/quest/rubrics/campaign-track-rubric-v13-2026-03-17.md
---

# Variations -- campaign-track / Round 14

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

R13 closed C-38 and C-39 with V-05 scoring at max against the v12 rubric. Two PASS+
excellence signals from R13 V-05 follow the multi-site reinforcement pattern -- each
representing a structural density pattern not captured by any existing criterion:

- C-40 (from R13 V-05 triptych structure): Phase 3->4 boundary taxonomy with
  temporal-axis independence labels. Three named subsections (Cascade Scope /
  Receiving Scope / Transition Obligation) each framed with a temporal label making
  orthogonality auditable at the section-header level without reading body text.
  "Cascade scope is a re-run concern; receiving scope is an entry concern; Transition
  Obligation is an exit concern." The triptych makes scope-dimension scanning possible
  without cross-reference reading.

- C-41 (from R13 V-05 double back-reference): Phase 4 active-role header
  cross-references Phase Boundary Summary subsections by name, creating traceable
  obligation links between declaration site (Phase Boundary Summary) and assertion
  site (Phase 4 header). "Receiving scope (Phase Boundary Summary, Phase 3->4)" at
  entry; "The Transition Obligation (Phase Boundary Summary, Phase 3->4) is violated"
  at exit. Bidirectional traceability between declaration and assertion.

Aspirational count goes from 28 to 30; max from 149 to 155.

---

R14 variation axes:
- V-01: Single-axis -- C-40 maximum (temporal labels embedded directly in triptych
  section header text; Phase 3 postcondition scope-state annotation as fourth surface)
- V-02: Single-axis -- C-41 maximum (back-references extended to Narrator prohibition
  #5 and new TERMINAL story.md existence check item; 28 TERMINAL items total)
- V-03: Single-axis -- Obligation provenance (Phase 3 Step A finalization annotation
  closes provenance loop between constraint-finalization site and exclusion site)
- V-04: Combined -- C-40 + C-41 (V-01 temporal headers + V-02 prohibition and
  TERMINAL extensions)
- V-05: Full stack -- C-40 + C-41 + provenance annotation + Cross-Phase Obligation
  Index (pre-phase table mapping all inter-phase obligations to declaration and
  assertion sites)

All five inherit R13 V-05 baseline (triptych structure, double back-references at
Phase 4 header, Phase 3 active-role header triptych reference, all C-01 through C-39).
Differences isolated to: Phase Boundary Summary Phase 3->4 header text, Phase 3
postcondition, Phase 3 Step A write annotation, Narrator prohibition #5, TERMINAL
Phase 4 checklist, and (V-03/V-05) new sections.

---

## V-01 -- Axis: Temporal labels embedded in triptych section headers (C-40 maximum)

**Hypothesis**: R13 V-05 placed temporal-axis labels as the *body opener* of each
triptych subsection. V-01 tests whether embedding the label directly in the *section
header* text -- `#### Cascade Scope (re-run concern)` -- makes C-40 auditable at the
outline level: a reader scanning only headers sees three distinct temporal concerns
without reading body content. Additionally, Phase 3 postcondition names all three
triptych concerns in a scope-state annotation, creating a fourth C-40 surface outside
the Phase Boundary Summary. Empty-state reinforces at a fifth surface. Phase 4
active-role header: R13 V-05 baseline (C-41 satisfied at baseline level, not
extended). TERMINAL: R13 V-05 baseline (27 items).

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

#### Cascade Scope (re-run concern)
Re-run concern: governs what a Phase 3 Step B re-run updates. Applies only on the
recovery path, after Phase 4 has already completed. Not an initial-execution concern.
- Update target: verdict_after in delta.md (Phase 4-dependent; sole cascade target)
- Excluded from cascade: session_number, signals_added, signals_removed,
  verdict_before, verdict_changed (finalized at Phase 3 Step B; Phase 4 does not own)
See Cascade Rule above for the full WHY.

#### Receiving Scope (entry concern)
Entry concern: governs what Phase 4 receives as inputs at initial execution entry.
Applies before Phase 4 runs. Independent of Cascade Scope: cascade scope is a re-run
concern; receiving scope is an entry concern. They address the same Phase 3/4 boundary
from orthogonal temporal positions.
- Phase 4 receives: readiness_verdict and coverage_ratio from status.md (read-only;
  Phase 4 does not modify)
- Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED" (placeholder;
  Phase 4 updates via Post-Phase-4 write)
- Phase 4 does NOT receive: namespace counts (planned, collected, missing, zero_flag)
  -- finalized at Phase 3 Step A; Phase 4 cannot change them; they are Phase 3 domain.
  A phase that receives a field as input implicitly claims the right to revise it;
  Phase 4 makes no such claim on namespace counts.

#### Transition Obligation (exit concern)
Exit concern: governs the write-confirmation requirement at Phase 4 exit. Applies
before the phase boundary closes, on Phase 4's way out. Not an entry or re-run concern.
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
Scope state at Phase 3 close: Cascade Scope (re-run concern) boundary is now open --
verdict_after will accept Phase 4 update. Receiving Scope (entry concern) boundary is
now set -- namespace counts finalized; not propagated to Phase 4. Transition Obligation
(exit concern) is now pending -- story.md write required before Phase 4 exits.

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
  Scope state: Cascade Scope (re-run concern) boundary open; Receiving Scope
    (entry concern) boundary set (all counts are 0; not propagated to Phase 4);
    Transition Obligation (exit concern) pending.

Phase 4 (Narrator): The Transition Obligation (exit concern, Phase Boundary Summary,
  Phase 3->4) applies on first invocation -- story.md SHALL be written; without it,
  downstream systems cannot distinguish an interrupted first session from a completed
  one. verdict_verb = "NOT YET REACHED". hypothesis_mutation.current = "UNCHANGED".
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

**Rubric targeting**: C-01 through C-39 (full R13 V-05 baseline). **C-40** (temporal
labels embedded in section header text: `#### Cascade Scope (re-run concern)`,
`#### Receiving Scope (entry concern)`, `#### Transition Obligation (exit concern)`;
triptych headers auditable at outline level without body reading; Phase 3 postcondition
scope-state annotation names all three concerns as fourth surface; Empty-state Phase 3
scope-state annotation is fifth surface; Empty-state Phase 4 cites "Transition
Obligation (exit concern, Phase Boundary Summary, Phase 3->4)" with temporal label
inline). **C-41** (Phase 4 obligation block: "Transition Obligation (Phase Boundary
Summary, Phase 3->4) is violated"; Phase 4 active-role header: "Receiving scope
(Phase Boundary Summary, Phase 3->4)" -- both back-references at R13 V-05 baseline
level). **Misses C-41 extension**: Narrator prohibition #5 and TERMINAL do not
reference Phase Boundary Summary by section name.

---

## V-02 -- Axis: C-41 extension to Narrator prohibition and TERMINAL (C-41 maximum)

**Hypothesis**: C-41 scoring surfaces in R13 V-05 are two: obligation block and
active-role italic header. V-02 tests whether extending back-references into the
Narrator's prohibition list (#5) and the TERMINAL Phase 4 checklist creates two
additional C-41 scoring surfaces. Narrator prohibition #5 becomes an obligation
cross-reference: "SHALL NOT declare Phase 4 complete without writing story.md
(violates Transition Obligation, Phase Boundary Summary, Phase 3->4)." TERMINAL adds
a story.md existence check referencing the same section path. Total C-41 surfaces: 4
(obligation block, active-role header, prohibition #5, TERMINAL). Phase Boundary
Summary Phase 3->4: R13 V-05 triptych baseline (no temporal labels in headers; C-40
at baseline level not maximized). TERMINAL: 28 items.

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
5. SHALL NOT declare Phase 4 complete without writing story.md (violates Transition
   Obligation, Phase Boundary Summary, Phase 3->4)

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
[ ] story.md written before Phase 4 declared complete (Transition Obligation,
    Phase Boundary Summary, Phase 3->4) -- FAIL: re-run Phase 4
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

All 28 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 28 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-39 (full R13 V-05 baseline). **C-41** (four
scoring surfaces: obligation block "Transition Obligation (Phase Boundary Summary,
Phase 3->4) is violated"; active-role header "Receiving scope (Phase Boundary Summary,
Phase 3->4)"; Narrator prohibition #5 "SHALL NOT declare Phase 4 complete without
writing story.md (violates Transition Obligation, Phase Boundary Summary, Phase 3->4)";
TERMINAL Phase 4 first item "story.md written before Phase 4 declared complete
(Transition Obligation, Phase Boundary Summary, Phase 3->4)"). **C-40** (triptych
present at R13 V-05 baseline level -- three named subsections, independence label in
Receiving Scope body opener -- but temporal labels NOT in section headers; outline-
level auditability absent). **Misses**: C-40 is not elevated beyond R13 V-05 baseline.

---

## V-03 -- Axis: Phase 3 Step A finalization annotation (obligation provenance)

**Hypothesis**: The receiving scope exclusion (Phase 4 does not receive namespace
counts) is declared at the consumption boundary (Phase Boundary Summary, Phase 3->4,
Receiving Scope) but not at the production boundary (Phase 3 Step A, where those
fields are finalized). V-03 adds a FINALIZATION annotation immediately after the
Phase 3 Step A write statement, declaring the fields finalized and cross-referencing
the Receiving Scope section by path. This closes the provenance loop: the constraint
is now visible at its origin (Phase 3 Step A) and at its exclusion point (Phase 4
entry). Tests whether source-site annotation creates a new C-42 pattern: obligation
provenance tracing from finalization event to exclusion event without requiring
cross-section reading. Phase Boundary Summary, Phase 4 header, Narrator prohibition,
TERMINAL: all R13 V-05 baseline. TERMINAL: 27 items.

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

FINALIZATION: The coverage table fields written above (planned, collected, missing,
zero_flag for all 9 namespace rows) are finalized at this step. They are Phase 3
Step A domain. They do not propagate to Phase 4 as inputs -- see Receiving Scope
(Phase Boundary Summary, Phase 3->4) for the exclusion rationale. Phase 4 makes no
claim to revise these fields; receiving them as Phase 4 inputs would imply revision
authority that Phase 4 does not hold.

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
    FINALIZATION applies: all counts are 0 but are still finalized Phase 3 domain.
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

**Rubric targeting**: C-01 through C-39 (full R13 V-05 baseline). **C-40** (triptych
at R13 V-05 baseline -- three named subsections, independence label in body openers --
temporal labels NOT in section headers). **C-41** (Phase 4 obligation block and
active-role header back-references at R13 V-05 baseline). **C-42 candidate** (Phase 3
Step A FINALIZATION annotation: namespace count fields declared finalized at their
write site with explicit cross-reference to "Receiving Scope (Phase Boundary Summary,
Phase 3->4)"; closes provenance loop between constraint-finalization event and
constraint-exclusion declaration; no prior variation placed the scope exclusion
rationale at the production site; Empty-state reinforces with "FINALIZATION applies"
at Step A). **Misses**: C-40 temporal labels not in headers; C-41 not extended to
prohibition or TERMINAL.

---

## V-04 -- Combined: C-40 temporal headers + C-41 prohibition and TERMINAL extensions

**Hypothesis**: V-01's temporal labels embedded in triptych headers and V-02's
Narrator prohibition cross-reference and TERMINAL story.md existence check can be
combined without structural conflict. The resulting prompt has: (1) C-40 at maximum
density -- temporal labels in section headers, Phase 3 postcondition scope-state
annotation, empty-state reinforcement with temporal labels; (2) C-41 at maximum
density -- obligation block back-reference, active-role header back-reference,
Narrator prohibition #5 back-reference, TERMINAL story.md existence check back-
reference. Both criteria at four+ scoring surfaces. TERMINAL: 28 items.

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

#### Cascade Scope (re-run concern)
Re-run concern: governs what a Phase 3 Step B re-run updates. Applies only on the
recovery path, after Phase 4 has already completed. Not an initial-execution concern.
- Update target: verdict_after in delta.md (Phase 4-dependent; sole cascade target)
- Excluded from cascade: session_number, signals_added, signals_removed,
  verdict_before, verdict_changed (finalized at Phase 3 Step B; Phase 4 does not own)
See Cascade Rule above for the full WHY.

#### Receiving Scope (entry concern)
Entry concern: governs what Phase 4 receives as inputs at initial execution entry.
Applies before Phase 4 runs. Independent of Cascade Scope: cascade scope is a re-run
concern; receiving scope is an entry concern. They address the same Phase 3/4 boundary
from orthogonal temporal positions.
- Phase 4 receives: readiness_verdict and coverage_ratio from status.md (read-only;
  Phase 4 does not modify)
- Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED" (placeholder;
  Phase 4 updates via Post-Phase-4 write)
- Phase 4 does NOT receive: namespace counts (planned, collected, missing, zero_flag)
  -- finalized at Phase 3 Step A; Phase 4 cannot change them; they are Phase 3 domain.
  A phase that receives a field as input implicitly claims the right to revise it;
  Phase 4 makes no such claim on namespace counts.

#### Transition Obligation (exit concern)
Exit concern: governs the write-confirmation requirement at Phase 4 exit. Applies
before the phase boundary closes, on Phase 4's way out. Not an entry or re-run concern.
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
5. SHALL NOT declare Phase 4 complete without writing story.md (violates Transition
   Obligation, Phase Boundary Summary, Phase 3->4)

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
Scope state at Phase 3 close: Cascade Scope (re-run concern) boundary is now open --
verdict_after will accept Phase 4 update. Receiving Scope (entry concern) boundary is
now set -- namespace counts finalized; not propagated to Phase 4. Transition Obligation
(exit concern) is now pending -- story.md write required before Phase 4 exits.

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
  Scope state: Cascade Scope (re-run concern) boundary open; Receiving Scope
    (entry concern) boundary set (all counts are 0; not propagated to Phase 4);
    Transition Obligation (exit concern) pending.

Phase 4 (Narrator): The Transition Obligation (exit concern, Phase Boundary Summary,
  Phase 3->4) applies on first invocation -- story.md SHALL be written; without it,
  downstream systems cannot distinguish an interrupted first session from a completed
  one. verdict_verb = "NOT YET REACHED". hypothesis_mutation.current = "UNCHANGED".
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
[ ] story.md written before Phase 4 declared complete (Transition Obligation,
    Phase Boundary Summary, Phase 3->4) -- FAIL: re-run Phase 4
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

All 28 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 28 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-39 (full R13 V-05 baseline). **C-40** (temporal
labels in section headers: `#### Cascade Scope (re-run concern)`, `#### Receiving
Scope (entry concern)`, `#### Transition Obligation (exit concern)`; Phase 3
postcondition scope-state annotation (fourth surface); empty-state Phase 3 scope-state
(fifth surface); empty-state Phase 4 "Transition Obligation (exit concern, Phase
Boundary Summary, Phase 3->4)" (sixth surface)). **C-41** (obligation block, active-
role header, Narrator prohibition #5, TERMINAL story.md existence check -- four
surfaces; each names "Transition Obligation, Phase Boundary Summary, Phase 3->4" or
"Receiving scope, Phase Boundary Summary, Phase 3->4" explicitly). **Misses**: C-42
provenance annotation absent (Phase 3 Step A has no FINALIZATION note).

---

## V-05 -- Full integration: C-40 + C-41 + provenance annotation + Cross-Phase Obligation Index

**Hypothesis**: Maximum scoring surface density across all R14 criteria comes from
four properties acting together: (1) temporal labels in triptych headers (C-40,
V-01); (2) back-references in Narrator prohibition and TERMINAL (C-41, V-02); (3)
Phase 3 Step A finalization annotation closing the provenance loop (C-42 candidate,
V-03); (4) a Cross-Phase Obligation Index table placed before the phase sections,
providing a global audit trail of all inter-phase obligations with declaration site,
assertion site, and violation consequence. The Index is a new structural pattern: a
table-level obligation map that makes traceability scannable without reading individual
phase sections. Tests whether table-mediated obligation traceability (C-43 candidate)
produces a new excellence pattern beyond back-references in prose. TERMINAL: 28 items
with story.md existence check referencing both Obligation Index and Phase Boundary
Summary by path.

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

## Cross-Phase Obligation Index

This index maps all inter-phase obligations. Use to locate any obligation without
reading individual phase sections.

| Obligation | Phase | Declaration Site | Assertion Site | Violation Consequence |
|------------|-------|-----------------|----------------|----------------------|
| Write story.md before Phase 4 exits | Phase 4 | Phase Boundary Summary -- Transition Obligation (exit concern) | Phase 4 obligation block; Narrator prohibition #5; TERMINAL Phase 4 row 1 | verdict_after remains "NOT YET REACHED"; interrupted campaign indistinguishable from completed campaign |
| Exclude namespace counts from Phase 4 inputs | Phase 3->4 | Phase Boundary Summary -- Receiving Scope (entry concern); Phase 3 Step A FINALIZATION | Phase 4 active-role header | Phase 4 implicitly claims revision authority over Phase 3 Step A domain |
| Update only verdict_after on Phase 3 Step B re-run | Phase 3 re-run | Cascade Rule; Phase Boundary Summary -- Cascade Scope (re-run concern) | Phase 3 Step B re-run instruction | Session history overwritten with non-session-scoped Phase 4 data |
| Write verdict_after placeholder on Step B first pass | Phase 3 Step B | Two-Pass Delta Rule | Phase 3 Step B instruction | verdict_after computed before Phase 4 verdict is known |
| Emit dashboard only after all 28 TERMINAL items PASS | Post-Phase-4 | TERMINAL section | Dashboard emit instruction | Dashboard emitted with unverified field values |

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

#### Cascade Scope (re-run concern)
Re-run concern: governs what a Phase 3 Step B re-run updates. Applies only on the
recovery path, after Phase 4 has already completed. Not an initial-execution concern.
- Update target: verdict_after in delta.md (Phase 4-dependent; sole cascade target)
- Excluded from cascade: session_number, signals_added, signals_removed,
  verdict_before, verdict_changed (finalized at Phase 3 Step B; Phase 4 does not own)
See Cascade Rule above for the full WHY.

#### Receiving Scope (entry concern)
Entry concern: governs what Phase 4 receives as inputs at initial execution entry.
Applies before Phase 4 runs. Independent of Cascade Scope: cascade scope is a re-run
concern; receiving scope is an entry concern. They address the same Phase 3/4 boundary
from orthogonal temporal positions.
- Phase 4 receives: readiness_verdict and coverage_ratio from status.md (read-only;
  Phase 4 does not modify)
- Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED" (placeholder;
  Phase 4 updates via Post-Phase-4 write)
- Phase 4 does NOT receive: namespace counts (planned, collected, missing, zero_flag)
  -- finalized at Phase 3 Step A (see FINALIZATION note); Phase 4 cannot change them;
  they are Phase 3 domain. A phase that receives a field as input implicitly claims
  the right to revise it; Phase 4 makes no such claim on namespace counts.

#### Transition Obligation (exit concern)
Exit concern: governs the write-confirmation requirement at Phase 4 exit. Applies
before the phase boundary closes, on Phase 4's way out. Not an entry or re-run concern.
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
5. SHALL NOT declare Phase 4 complete without writing story.md (violates Transition
   Obligation, Phase Boundary Summary, Phase 3->4; see Cross-Phase Obligation Index,
   row 1)

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

FINALIZATION: The coverage table fields written above (planned, collected, missing,
zero_flag for all 9 namespace rows) are finalized at this step. They are Phase 3
Step A domain. They do not propagate to Phase 4 as inputs -- see Receiving Scope
(Phase Boundary Summary, Phase 3->4) and Cross-Phase Obligation Index row 2. Phase 4
makes no claim to revise these fields; receiving them as Phase 4 inputs would imply
revision authority that Phase 4 does not hold.

### Step B -- Session Delta (Pass 1)

The Analyst SHALL produce delta.md per Session Delta Contract.

Two-pass protocol: verdict_after SHALL be "NOT YET REACHED" (placeholder; Phase 4
not yet run). All other fields SHALL be written as final values at this step.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md both present. status.md has 9 rows,
integer fields, readiness_verdict assigned. delta.md has placeholder verdict_after.
Scope state at Phase 3 close: Cascade Scope (re-run concern) boundary is now open --
verdict_after will accept Phase 4 update. Receiving Scope (entry concern) boundary is
now set -- namespace counts finalized; not propagated to Phase 4. Transition Obligation
(exit concern) is now pending -- story.md write required before Phase 4 exits.

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
Step A (see FINALIZATION note and Cross-Phase Obligation Index row 2) and Phase 4
cannot change them. They are Phase 3 domain. Phase 4 receives readiness_verdict and
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
    FINALIZATION applies: all counts are 0 but are still finalized Phase 3 domain;
    they do not propagate to Phase 4.
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED" (placeholder).
    verdict_changed = "N/A".
  Scope state: Cascade Scope (re-run concern) boundary open; Receiving Scope
    (entry concern) boundary set (zero counts finalized; not propagated to Phase 4);
    Transition Obligation (exit concern) pending.

Phase 4 (Narrator): The Transition Obligation (exit concern, Phase Boundary Summary,
  Phase 3->4; Cross-Phase Obligation Index row 1) applies on first invocation --
  story.md SHALL be written; without it, downstream systems cannot distinguish an
  interrupted first session from a completed one. verdict_verb = "NOT YET REACHED".
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
[ ] story.md written before Phase 4 declared complete (Transition Obligation,
    Phase Boundary Summary, Phase 3->4; Cross-Phase Obligation Index row 1)
    -- FAIL: re-run Phase 4
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

All 28 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 28 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-39 (full R13 V-05 baseline). **C-40** (temporal
labels in section headers -- `#### Cascade Scope (re-run concern)`, `#### Receiving
Scope (entry concern)`, `#### Transition Obligation (exit concern)` -- plus Phase 3
postcondition scope-state, empty-state scope-state, empty-state Phase 4 reference
with temporal label inline; six surfaces). **C-41** (obligation block, active-role
header, Narrator prohibition #5 with Obligation Index cross-reference, TERMINAL
story.md existence check with Obligation Index cross-reference; four surfaces, two
of which trace through the Index creating index-mediated traceability). **C-42
candidate** (Phase 3 Step A FINALIZATION annotation cites both "Receiving Scope
(Phase Boundary Summary, Phase 3->4)" and "Cross-Phase Obligation Index row 2";
Receiving Scope body also cites the FINALIZATION note back; closed bidirectional
provenance loop between constraint-finalization site and constraint-exclusion site).
**C-43 candidate** (Cross-Phase Obligation Index: five-row table mapping all inter-
phase obligations to declaration site, assertion site, and violation consequence;
table-level obligation traceability scannable without reading individual phase sections;
Narrator prohibition #5 and TERMINAL story.md item both cite "Cross-Phase Obligation
Index row 1", creating index-mediated back-reference chains distinct from direct
Phase Boundary Summary back-references; new structural pattern not present in any
prior variation).
