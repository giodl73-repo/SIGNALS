---
skill: quest-variate
skill_target: campaign-track
round: 12
date: 2026-03-17
rubric: simulations/quest/rubrics/campaign-track-rubric-v11-2026-03-17.md
---

# Variations -- campaign-track / Round 12

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

R10 closed C-33, C-34, and C-35 with V-05 scoring 131/131 and producing two PASS+
excellence signals that both follow the assertion->causal-explanation pattern
established by C-31/C-32, applied at two new declaration sites:

- C-36 (from R10 V-05 C-33 PASS+): Phase 4 obligation header goes beyond bare
  obligation declaration to naming the specific stale-value consequence --
  `verdict_after` in `delta.md` becomes stale if Phase 4 completes without the
  post-write. Assertion -> named consequence. Mirrors C-32's failure-path framing
  at the Phase 3 header.

- C-37 (from R10 V-05 C-35 PASS+): Cascade rule goes beyond naming trigger, target,
  and scope exclusion to explaining WHY non-cascade fields are excluded -- they were
  finalized at Phase 3 and Phase 4 cannot change them. Causal scope justification vs.
  bare enumeration. Mirrors C-31's upstream-dependency explanation.

Aspirational count goes from 19 to 24; max from 122 to 137.

R12 variation axes:
- V-01: Single-axis -- C-36 (stale-value consequence at Phase 4 obligation header)
- V-02: Single-axis -- C-37 (causal WHY in cascade scope exclusion rule)
- V-03: Single-axis -- Phrasing register (formal SHALL declarations throughout)
- V-04: Combined -- C-36 + C-37 (causal framing at both Phase 3/4 boundary sites)
- V-05: Full stack -- C-36 + C-37 + phrasing + lifecycle boundary emphasis

All five variations inherit the R10 V-05 baseline. Differences are isolated to the
Cascade Rule section, the Phase 4 obligation header, phrasing register, and (V-05
only) an explicit lifecycle boundary section.

---

## V-01 -- Axis: Stale-value consequence at Phase 4 obligation site (C-36 maximum)

**Hypothesis**: A bare obligation ("write story.md") can be treated as a reminder; an
obligation naming a specific downstream failure mode cannot. When the Phase 4 header
declares that skipping the post-write leaves `verdict_after` in `delta.md` stale --
causing all downstream delta comparisons to report the previous verdict as current --
the model enters Phase 4 knowing exactly what breaks if Phase 4 exits without the
write. The causal chain (assertion -> named consequence) is auditable: the criterion
either names the stale-value consequence or it does not. V-01 adds only C-36 to the
R10 V-05 baseline. The cascade rule is present but carries no WHY justification
(C-37 absent).

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Each field typed
as integer must contain an integer. Each field typed as enumerated string must
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
- echoes: list of strings; if none, value must be ["NONE"]
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

delta.md is written in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. The Phase 4 verdict is not yet known.

Pass 2 (Post-Phase-4): Update verdict_after to the actual verdict_verb from
story.md. This is the only post-Phase-4 write in the campaign.

The terminal checklist item for verdict_after is order-dependent: "NOT YET REACHED"
in verdict_after after Phase 4 completes is a defect unless Phase 4 verdict_verb is
also "NOT YET REACHED".

---

## Cascade Rule

When Phase 3 Step B is re-run, only verdict_after in delta.md is updated -- not the
other delta.md fields. session_number, signals_added, signals_removed, verdict_before,
and verdict_changed are not affected by the cascade.

---

## Prohibition Parity Rule

Each role carries exactly 5 forbidden actions -- no more, no fewer. Numbered list
format required (1 through 5). A role with 4 or 6 items fails audit.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)
Owns strategy.md.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not declared in planned_signals

### Planner (Phase 2 -- topic-plan)
Owns roadmap.md.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)
Owns status.md AND delta.md. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond Phase 2 roadmap
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "a few") where integers are required

### Narrator (Phase 4 -- topic-story)
Owns story.md.

Forbidden actions (exactly 5):
1. Must not modify coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md per Phase 1 Contract:
- topic_name, namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md per Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose present per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}.

Produce status.md per Phase 3 Contract:
- All 9 namespace rows -- no row skipped
- planned and collected: integers only (narrative counts fail)
- missing: signal names as strings, not counts
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md per Session Delta Contract.

Two-pass protocol:
- Write verdict_after = "NOT YET REACHED" (placeholder; Phase 4 not yet run)
- All other fields (session_number, signals_added, signals_removed, verdict_before,
  verdict_changed) are final at this step

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md both present. status.md has 9 rows,
integer fields, readiness_verdict assigned. delta.md has placeholder verdict_after.

GATE: Do not proceed to Phase 4 until Phase 3 postcondition is satisfied.

---

## Phase 4 -- Narrative (Narrator)

**Obligation**: Write story.md before declaring Phase 4 complete. If Phase 4 completes
without writing story.md, `verdict_after` in `delta.md` becomes stale -- the "NOT YET
REACHED" placeholder will persist indefinitely, causing all downstream delta
comparisons to report the campaign as incomplete rather than reflecting the actual
readiness state determined by this session.

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md per Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (no paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, update delta.md:
- Set verdict_after = verdict_verb value from story.md
- Set verdict_changed = YES if verdict_after != verdict_before; NO if equal;
  N/A if verdict_before = NONE

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. Founding artifact.
Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals planned.

Phase 3 (Analyst):
  Step A: All rows have collected = 0 (integer). missing lists all planned signals
    by signal_name. zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0.
    readiness_verdict = "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED" (placeholder).
    verdict_changed = "N/A".

Phase 4 (Narrator): Obligation applies -- story.md must be written even on first
  invocation; without it, verdict_after in delta.md remains the placeholder.
  verdict_verb = "NOT YET REACHED". hypothesis_mutation.current = "UNCHANGED".
  echoes = ["NONE"]. next_signal_recommendations: top 3 from roadmap.md by priority.

Post-Phase-4: verdict_after updated to "NOT YET REACHED" (coincides with placeholder
  on first invocation). verdict_changed = "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field before marking the campaign complete. A field satisfying its
constraint PASSES. Failure triggers re-run of the affected phase only.
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
[ ] missing: list of names in each row (not counts) -- FAIL: re-run Phase 3
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
    must reflect Phase 4 verdict_verb; placeholder "NOT YET REACHED" fails after
    Phase 4 completes unless Phase 4 verdict_verb is also "NOT YET REACHED"
    FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign complete. Dashboard ready to emit.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-35 (full R10 V-05 baseline), **C-36** (Phase 4
obligation header names specific stale-value consequence: `verdict_after` in
`delta.md` becomes stale, downstream delta comparisons report campaign as incomplete;
reinforced in empty-state with note that obligation applies on first invocation).
**Misses**: C-37 (cascade rule names trigger + target but gives no WHY for scope
exclusion -- "not affected by the cascade" is bare enumeration, not causal).
**Risk**: The consequence framing is strong at the Phase 4 header but may not score
C-36 at PASS+ unless the stale-value language is specific enough: "verdict_after
in delta.md becomes stale" names the exact field and artifact. The empty-state
reinforcement adds a second occurrence at the scoring surface. Scores cap at
baseline + C-36.

---

## V-02 -- Axis: Cascade scope justification with causal WHY (C-37 maximum)

**Hypothesis**: Naming what gets excluded from a cascade is weaker than explaining why
it gets excluded. "session_number is not cascaded" describes a rule; "session_number
is not cascaded because it was finalized at Phase 3 Step B and Phase 4 cannot change
it" creates an auditable boundary. A model that understands the boundary cannot
inadvertently update a finalized field during Phase 4 because the causal justification
names the exact mechanism. V-02 isolates C-37 against the R10 V-05 baseline. The
Phase 4 obligation header carries bare obligation only (C-36 absent).

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Each field typed
as integer must contain an integer. Each field typed as enumerated string must
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
- echoes: list of strings; if none, value must be ["NONE"]
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

delta.md is written in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. The Phase 4 verdict is not yet known.

Pass 2 (Post-Phase-4): Update verdict_after to the actual verdict_verb from
story.md. This is the only post-Phase-4 write in the campaign.

The terminal checklist item for verdict_after is order-dependent: "NOT YET REACHED"
in verdict_after after Phase 4 completes is a defect unless Phase 4 verdict_verb is
also "NOT YET REACHED".

---

## Cascade Rule

When Phase 3 Step B is re-run (triggered by a Phase 3 postcondition failure after
Phase 4 has already completed), only verdict_after in delta.md is updated.

The remaining delta.md fields are excluded from the cascade because they were
finalized at Phase 3 Step B: session_number was assigned, signals_added and
signals_removed were computed from the session diff, verdict_before was read from
the prior run's verdict, and verdict_changed was derived from the before/after pair.
Phase 4 cannot change any of these values -- they describe session-level facts that
exist independently of what Phase 4 concludes. Cascading them would overwrite
finalized session history with Phase 4 data that is not session-scoped.

Only verdict_after is Phase 4-dependent, which is why it alone cascades.

---

## Prohibition Parity Rule

Each role carries exactly 5 forbidden actions -- no more, no fewer. Numbered list
format required (1 through 5). A role with 4 or 6 items fails audit.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)
Owns strategy.md.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not declared in planned_signals

### Planner (Phase 2 -- topic-plan)
Owns roadmap.md.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)
Owns status.md AND delta.md. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond Phase 2 roadmap
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts where integers are required

### Narrator (Phase 4 -- topic-story)
Owns story.md.

Forbidden actions (exactly 5):
1. Must not modify coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md per Phase 1 Contract:
- topic_name, namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md per Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose present per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}.

Produce status.md per Phase 3 Contract:
- All 9 namespace rows -- no row skipped
- planned and collected: integers only
- missing: signal names as strings, not counts
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md per Session Delta Contract.

Two-pass protocol:
- Write verdict_after = "NOT YET REACHED" (placeholder; Phase 4 not yet run)
- All other fields are final at this step

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md both present. status.md has 9 rows,
integer fields, readiness_verdict assigned. delta.md has placeholder verdict_after.

GATE: Do not proceed to Phase 4 until Phase 3 postcondition is satisfied.

---

## Phase 4 -- Narrative (Narrator)

**Obligation**: Write story.md before declaring Phase 4 complete.

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md per Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (no paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, update delta.md:
- Set verdict_after = verdict_verb value from story.md
- Set verdict_changed = YES if verdict_after != verdict_before; NO if equal;
  N/A if verdict_before = NONE

Only verdict_after and verdict_changed are updated at this step. No other delta.md
fields are touched. See Cascade Rule for the justification of this scope.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. Founding artifact.
Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals planned.

Phase 3 (Analyst):
  Step A: All rows have collected = 0 (integer). missing lists all planned signals
    by signal_name. zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0.
    readiness_verdict = "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED" (placeholder).
    verdict_changed = "N/A".

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current =
  "UNCHANGED". echoes = ["NONE"]. recommendations: top 3 from roadmap.md by priority.

Post-Phase-4: verdict_after updated to "NOT YET REACHED". verdict_changed = "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field before marking the campaign complete. Failure triggers re-run of
the affected phase only. Implicit completion is not acceptable.

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
    must reflect Phase 4 verdict_verb; placeholder fails after Phase 4 completes
    FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign complete. Dashboard ready to emit.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-35 (full R10 V-05 baseline), **C-37** (cascade
rule names trigger (Phase 3 Step B re-run), cascade target (verdict_after only), AND
explains WHY non-cascade fields are excluded: they were finalized at Phase 3 Step B
and Phase 4 cannot change them; the explanation names each excluded field and gives
the specific reason for its exclusion -- session-scoped facts that exist independently
of Phase 4's conclusion).
**Misses**: C-36 (Phase 4 obligation header is bare "write story.md" with no
stale-value consequence named).
**Risk**: The cascade WHY explanation is at maximum length -- it names each excluded
field and gives the session-scoped finalization argument. The risk is verbosity
without scoring gain if the criterion only requires naming the finalization point
rather than justifying each field. The "cascading them would overwrite finalized
session history with Phase 4 data that is not session-scoped" line is the key
causal framing for the PASS+ pattern.

---

## V-03 -- Axis: Phrasing register -- formal SHALL declarations (new axis)

**Hypothesis**: Imperative phrasing ("write story.md") and SHALL declarations ("the
Narrator SHALL write story.md") address the same constraint but at different levels
of formality. SHALL is a term of art in protocol specifications (RFC 2119) meaning
"absolute requirement." A model processing a prompt with SHALL may treat the
requirement as non-negotiable where imperative phrasing leaves room for
interpretation. V-03 tests whether formal SHALL register at obligation sites --
Phase 4 header, cascade rule, gate statements -- activates constraint-following
behavior independently of whether the stale-value consequence or cascade WHY is
named. No C-36 or C-37 content; phrasing register is the single axis.

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
  - missing: list of strings (empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N"
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md
- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text)
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
This is a declared placeholder. The Phase 4 verdict is not yet known. The model
SHALL NOT compute a verdict_after value before Phase 4 runs.

Pass 2 (Post-Phase-4): After story.md is written, the model SHALL update
verdict_after to the actual verdict_verb from story.md. This is the only
post-Phase-4 write in the campaign.

The terminal checklist item for verdict_after is order-dependent: a "NOT YET
REACHED" placeholder in verdict_after after Phase 4 completes SHALL be treated as
a defect unless Phase 4 verdict_verb is also "NOT YET REACHED".

---

## Cascade Rule

When Phase 3 Step B is re-run, only verdict_after in delta.md SHALL be updated.
The remaining delta.md fields SHALL NOT be modified: session_number, signals_added,
signals_removed, verdict_before, and verdict_changed are outside the cascade scope.

---

## Prohibition Parity Rule

Each role SHALL carry exactly 5 forbidden actions -- no more, no fewer. Numbered
list format is required (1 through 5). A role with 4 or 6 items SHALL fail audit.

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
1. SHALL NOT modify coverage table or coverage ratio (Phase 3 domain)
2. SHALL NOT add, remove, or reorder planned signals (Phase 2 domain)
3. SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. SHALL NOT invoke any sub-skill other than topic-story
5. SHALL NOT paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

The Registrar SHALL invoke topic-new for {{topic}}.

The Registrar SHALL produce strategy.md per Phase 1 Contract:
- topic_name, namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all fields typed correctly.

GATE: The campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

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
Session Delta Contract governs delta.md.*

### Step A -- Coverage Status

The Analyst SHALL invoke topic-status for {{topic}}.

The Analyst SHALL produce status.md per Phase 3 Contract:
- All 9 namespace rows -- no row SHALL be skipped
- planned and collected SHALL be integers (narrative counts fail)
- missing SHALL list signal names as strings, not counts
- zero_flag SHALL be "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio SHALL be in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

The Analyst SHALL produce delta.md per Session Delta Contract.

Two-pass protocol:
- verdict_after SHALL be written as "NOT YET REACHED" (placeholder)
- All other fields SHALL be written as final values at this step

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md both present with all required fields.

GATE: The campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition is
satisfied.

---

## Phase 4 -- Narrative (Narrator)

**Obligation**: The Narrator SHALL write story.md before declaring Phase 4 complete.

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

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

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

Each phase SHALL run and produce its full artifact per its typed contract.

Phase 1: Create strategy.md normally. Founding artifact.
Phase 2: Create roadmap.md normally. All signals planned.
Phase 3 Step A: collected SHALL be 0 (integer) in all rows. missing SHALL list
  all planned signals by name. readiness_verdict SHALL be "NOT READY".
Phase 3 Step B: verdict_after SHALL be "NOT YET REACHED" (placeholder).
Phase 4: verdict_verb SHALL be "NOT YET REACHED". hypothesis_mutation.current
  SHALL be "UNCHANGED". echoes SHALL be ["NONE"].

---

## TERMINAL -- Field-Level Completion Checklist

The model SHALL verify each field before declaring the campaign complete. Implicit
completion is not acceptable. A field failing its constraint SHALL trigger re-run
of the affected phase only.

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

**Rubric targeting**: C-01 through C-35 (full R10 V-05 baseline). No new C-36 or
C-37 content. Phrasing register is the isolated axis: SHALL declarations replace
imperative phrasing at all obligation sites (phase gates, artifact writes, field
constraints, prohibition lists). "SHALL NOT" in prohibition lists vs. "Must not"
creates a uniform register throughout.
**New pattern to watch**: SHALL at the terminal checklist ("SHALL be emitted") and
SHALL NOT in prohibition lists may produce a new excellence signal around formal
register consistency -- or may have no scoring effect if the criteria are
content-based rather than phrasing-based.
**Risk**: Formal register adds no new structural content. If all C-36/C-37 patterns
depend on the specific causal language (stale-value consequence, finalization reason),
SHALL phrasing without that language fails both. Scores cap at R10 V-05 baseline
(no new criteria targeted). V-03's value is in discovering whether phrasing register
is a hidden axis in future rubric evolution.

---

## V-04 -- Combined: C-36 + C-37 (causal framing at both Phase 3/4 boundary sites)

**Hypothesis**: C-36 and C-37 address the Phase 3/4 boundary from different angles:
C-36 names what happens downstream (delta.md becomes stale) if Phase 4 skips its
write; C-37 names why Phase 4 cannot update the upstream fields (they were finalized
at Phase 3). Together they close the causal loop at the boundary: the
assertion is what Phase 4 must do, the consequence names why it matters, and the
cascade justification explains what is and is not in scope. V-04 tests whether both
axes together produce a compound PASS signal stronger than either axis alone,
without adding phrasing or lifecycle emphasis noise.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Each field typed
as integer must contain an integer. Each field typed as enumerated string must
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
  - missing: list of strings (empty list [] if none missing)
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
- echoes: list of strings; if none, value must be ["NONE"]
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

delta.md is written in two passes:

Pass 1 (Phase 3 Step B): Write delta.md with verdict_after = "NOT YET REACHED".
This is a declared placeholder. The Phase 4 verdict is not yet known.

Pass 2 (Post-Phase-4): Update verdict_after to the actual verdict_verb from
story.md. This is the only post-Phase-4 write in the campaign.

The terminal checklist item for verdict_after is order-dependent: "NOT YET REACHED"
in verdict_after after Phase 4 completes is a defect unless Phase 4 verdict_verb is
also "NOT YET REACHED".

---

## Cascade Rule

When Phase 3 Step B is re-run (triggered by a Phase 3 postcondition failure after
Phase 4 has already completed), only verdict_after in delta.md is updated. The
cascade target is verdict_after alone.

The remaining delta.md fields are excluded from the cascade because they were
finalized at Phase 3 Step B and Phase 4 cannot change them: session_number recorded
the session sequence, signals_added and signals_removed captured the session-level
diff, verdict_before read the prior run's verdict, and verdict_changed was derived
from the before/after pair. All of these are session facts -- they describe what
happened in this session, independent of what Phase 4 concludes. Phase 4 produces a
verdict about the topic; it does not revise the session record. Cascading non-cascade
fields would overwrite finalized session history with Phase 4-scoped data that was
never session-scoped to begin with.

Only verdict_after is Phase 4-dependent. That dependency is why it alone cascades.

---

## Prohibition Parity Rule

Each role carries exactly 5 forbidden actions -- no more, no fewer. Numbered list
format required (1 through 5). A role with 4 or 6 items fails audit.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)
Owns strategy.md.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not declared in planned_signals

### Planner (Phase 2 -- topic-plan)
Owns roadmap.md.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)
Owns status.md AND delta.md. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond Phase 2 roadmap
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts where integers are required

### Narrator (Phase 4 -- topic-story)
Owns story.md.

Forbidden actions (exactly 5):
1. Must not modify coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md per Phase 1 Contract:
- topic_name, namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md per Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}.

Produce status.md per Phase 3 Contract:
- All 9 namespace rows -- no row skipped
- planned and collected: integers only
- missing: signal names as strings, not counts
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md per Session Delta Contract.

Two-pass protocol: verdict_after = "NOT YET REACHED" (placeholder). All other
fields are final at this step.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md both present with all required fields.

GATE: Do not proceed to Phase 4 until Phase 3 postcondition is satisfied.

---

## Phase 4 -- Narrative (Narrator)

**Obligation**: Write story.md before declaring Phase 4 complete. If Phase 4 completes
without writing story.md, `verdict_after` in `delta.md` becomes stale -- the "NOT
YET REACHED" placeholder persists, and all downstream delta comparisons report the
campaign as incomplete rather than reflecting the actual readiness verdict from
this session.

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md per Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, update delta.md:
- Set verdict_after = verdict_verb value from story.md
- Set verdict_changed = YES if verdict_after != verdict_before; NO if equal;
  N/A if verdict_before = NONE

Only verdict_after and verdict_changed are updated at this step. See Cascade Rule
for the justification of what is and is not in scope.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. Founding artifact.
Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals planned.

Phase 3 (Analyst):
  Step A: collected = 0 in all rows. missing lists all planned signals by name.
    zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0.
    readiness_verdict = "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED" (placeholder).
    verdict_changed = "N/A".

Phase 4 (Narrator): Obligation applies on first invocation -- story.md must be
  written; without it, verdict_after in delta.md carries the placeholder only.
  verdict_verb = "NOT YET REACHED". hypothesis_mutation.current = "UNCHANGED".
  echoes = ["NONE"].

Post-Phase-4: verdict_after updated to "NOT YET REACHED". verdict_changed = "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field before marking the campaign complete. Failure triggers re-run of
the affected phase only. Implicit completion is not acceptable.

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
    must reflect Phase 4 verdict_verb; placeholder fails after Phase 4 completes
    FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign complete. Dashboard ready to emit.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-35 (full R10 V-05 baseline), **C-36** (Phase 4
obligation header names specific stale-value consequence: `verdict_after` in
`delta.md` becomes stale; extended to empty-state section), **C-37** (cascade rule
names trigger + target + WHY non-cascade fields excluded: they are session facts
finalized at Phase 3 Step B, independent of Phase 4's conclusion; causal scope
justification closes the "only verdict_after cascades" boundary).
**Structural note**: C-36 and C-37 bracket the Phase 3/4 boundary from opposite
directions. C-36 anchors Phase 4 entry (assertion -> consequence of skipping).
C-37 anchors the Post-Phase-4 update (assertion -> WHY scope is restricted). The
reference "See Cascade Rule for the justification" in the Post-Phase-4 section
creates a cross-reference that reinforces both directions without repeating the
full text.
**Risk**: The cascade WHY explanation is longer in V-04 than in V-02 (it names the
finalization reason per field rather than asserting it categorically). More specific
may score higher on C-37 or may score identically if the rubric only requires the
finalization point to be named once. V-05 will test whether adding the lifecycle
boundary section creates a third scoring site for both criteria.

---

## V-05 -- Full stack: C-36 + C-37 + phrasing register + lifecycle boundary emphasis

**Combined axes**: Stale-value consequence (C-36) + cascade WHY (C-37) + SHALL
phrasing at obligation sites + explicit phase boundary section naming what each
phase receives from the prior phase and what it passes to the next.

**Hypothesis**: The lifecycle boundary section creates additional scoring surfaces
for both C-36 and C-37 without repeating their full text. A boundary section that
states "Phase 4 receives from Phase 3: readiness_verdict and coverage_ratio (read-
only inputs); Phase 4 does not receive: namespace counts (finalized at Phase 3 Step
B, Phase 4 cannot change them)" activates C-37 at the boundary site, in addition
to the Cascade Rule section. Similarly, a boundary section that states "Phase 4
obligation: write story.md; if skipped, verdict_after in delta.md becomes stale"
activates C-36 at a second site. Dual-site scoring on both new criteria combined
with the full prior baseline should produce the highest score of any R12 variation.

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
  - missing: list of strings (empty list [] if none missing)
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

When Phase 3 Step B is re-run, only verdict_after in delta.md SHALL be updated.
The cascade target is verdict_after alone.

The remaining delta.md fields SHALL NOT be modified because they were finalized at
Phase 3 Step B and Phase 4 cannot change them: session_number recorded the session
sequence, signals_added and signals_removed captured the session-level diff,
verdict_before read the prior verdict, and verdict_changed was derived from the
before/after pair. These are session-scoped facts -- they describe what happened
in this session independently of what Phase 4 concludes about the topic. Phase 4
produces a topic verdict; it does not revise the session record. Cascading these
fields would overwrite finalized session history with data that Phase 4 does not
own.

Only verdict_after is Phase 4-dependent, which is why it is the only cascade target.

---

## Phase Boundary Summary

Each phase has explicit inputs (what it receives from the prior phase) and outputs
(what it passes to the next). This boundary summary is the governing contract for
phase ordering; it takes precedence over any inferred sequencing.

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
  story.md, `verdict_after` in `delta.md` becomes stale -- the placeholder persists
  and downstream delta comparisons cannot determine whether the campaign produced
  a real verdict or was interrupted.

### Post-Phase-4 -> Dashboard Boundary
- Post-Phase-4 output: delta.md updated with actual verdict_after (verdict_verb
  from story.md) and verdict_changed
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
stale -- the "NOT YET REACHED" placeholder persists indefinitely, and all downstream
delta comparisons will report this campaign as incomplete rather than reflecting the
actual readiness verdict determined by this session's signals.

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
  written; without it, verdict_after in delta.md remains the placeholder.
  verdict_verb = "NOT YET REACHED". hypothesis_mutation.current = "UNCHANGED".
  echoes = ["NONE"]. recommendations: top 3 signals from roadmap.md by priority.

Post-Phase-4: verdict_after updated to "NOT YET REACHED" (coincides with placeholder
  on first invocation). verdict_changed = "N/A".

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

**Rubric targeting**: C-01 through C-35 (full R10 V-05 baseline), **C-36** (Phase 4
obligation header names stale-value consequence at the obligation declaration site;
additionally named in Phase Boundary Summary at the Phase 3->Phase 4 boundary entry;
additionally named in empty-state section noting obligation applies on first
invocation -- three scoring surfaces), **C-37** (cascade rule names trigger + target
+ WHY with per-field finalization argument; additionally named in Phase Boundary
Summary: "Phase 4 does NOT receive namespace counts -- finalized at Phase 3 Step A,
Phase 4 cannot change them"; additionally named in Phase 4 active-role header:
"Phase 4 does NOT receive namespace counts -- those were finalized at Phase 3 Step A"
-- three scoring surfaces for C-37 as well).
**New pattern to watch**: The Phase Boundary Summary section creates a third scoring
site for both C-36 and C-37. If either criterion scores per-occurrence, V-05 has
the highest occurrence density. If criteria score presence only (binary), V-05 ties
V-04 on C-36/C-37 and must win on other dimensions (SHALL phrasing may generate a
new excellence signal, or the boundary section may reveal a new criterion around
explicit phase input/output declaration).
**Risk**: V-05 is the longest variation. The Phase Boundary Summary adds substantial
length. A model processing this prompt may exhibit "structural coverage without
substantive execution" -- filling all fields nominally while the boundary section
becomes decorative. The SHALL declarations throughout and the three-site scoring for
C-36/C-37 are the primary defenses.

---

## Variation Summary

| ID  | Primary Axes                                 | New Criteria Targeted | Key Differentiator                                              |
|-----|----------------------------------------------|-----------------------|-----------------------------------------------------------------|
| V-01 | C-36 only                                   | C-36                  | Phase 4 header names stale-value consequence; cascade bare      |
| V-02 | C-37 only                                   | C-37                  | Cascade WHY with per-field finalization argument; P4 header bare |
| V-03 | Phrasing register (SHALL)                   | none new              | SHALL at all obligation sites; tests phrasing as hidden axis    |
| V-04 | C-36 + C-37                                 | C-36 + C-37           | Both causal patterns at Phase 3/4 boundary; cross-reference P2P |
| V-05 | C-36 + C-37 + SHALL + lifecycle boundary    | C-36 + C-37 + new?    | Three scoring surfaces per new criterion; boundary section      |

**Predicted leaderboard going into quest-score**: V-05 > V-04 > V-01 = V-02 > V-03.

V-05 has the highest scoring surface density for C-36/C-37 and inherits the full
prior baseline. V-04 closes both new criteria without the overhead. V-01 and V-02
isolate one new criterion each and are predicted to tie; which scores higher depends
on whether C-36 or C-37 has a higher point weight in v11. V-03 explores a new axis
that produces no new criteria at R12 but may surface an excellence pattern for R13.

The main open question: does the Phase Boundary Summary section in V-05 activate
new criteria around explicit phase input/output declaration, or does it simply add
length without scoring gain? V-03's SHALL phrasing experiment will inform whether
phrasing register is a scoring axis in v12 or v13.
