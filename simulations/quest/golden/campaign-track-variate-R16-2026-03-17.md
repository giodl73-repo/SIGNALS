---
skill: quest-variate
skill_target: campaign-track
round: 16
date: 2026-03-17
rubric: simulations/quest/rubrics/campaign-track-rubric-v15-2026-03-17.md
---

# Variations -- campaign-track / Round 16

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

R15 closed with one scored variation (V-01 partial at ~92/158) and three excellence
signals from V-01 that become C-43, C-44, C-45 in rubric v15:

- C-43 (from R15 V-01 ES-1): Pre-phase PERSONA REGISTRY block. All four personas
  declared in a dedicated registry section before Phase 1 begins, each with ownership
  domain and enumerated prohibition list. Separates identity declaration from behavior
  description; prevents prohibition lists from being buried inside phase sections.

- C-44 (from R15 V-01 ES-2): Six-component Phase 4 story artifact. Extends the
  minimum four components (C-05) to six by explicitly adding coverage_ratio and
  session_delta as required typed fields in the Phase 4 output contract. Forces
  NARRATOR to include verifiable evidence alongside the verdict token.

- C-45 (from R15 V-01 ES-3): ANALYST closure statement inline. Single sentence at the
  Phase 3 boundary that explicitly closes the role's authority before handoff:
  "ANALYST closes at artifact write. ANALYST does not carry work into Phase 4."
  Prevents scope bleed without requiring a full prohibition restatement.

Aspirational count: 34. Max score: 167.

---

R16 variation axes:
- V-01: Single-axis -- C-43 maximum (pre-phase PERSONA REGISTRY with typed domain
  fields and cross-references; phases cite registry entry, not standalone prohibitions)
- V-02: Single-axis -- C-44 maximum (Phase 4 contract extended to six components;
  TERMINAL gains two new items for coverage_ratio and session_delta in story.md; 30
  TERMINAL items total)
- V-03: Single-axis -- C-45 maximum (closure statements at all three phase exit
  boundaries, not just Phase 3->4; Closure Parity Rule declared as a governing section)
- V-04: Combined -- C-43 + C-44 (persona registry + six-component Phase 4 contract)
- V-05: Full stack -- C-43 + C-44 + C-45 + Prohibition Anchoring (each prohibition
  carries an inline citation of the contract section or boundary it enforces; makes
  prohibition-to-contract traceability auditable per item)

All five inherit R14 V-05 baseline (all C-01 through C-42: four-phase structure,
nine-namespace coverage table, readiness verdict, typed output contracts, Two-Pass
Delta Rule, Cascade Rule, triptych Phase Boundary Summary Phase 3->4 with temporal
headers, four C-41 back-reference surfaces, Phase 3 Step A finalization annotation,
Cross-Phase Obligation Index, Prohibition Parity Rule). Differences isolated to:
pre-phase section, Phase 4 contract, phase boundary exit language, and per-prohibition
annotation format.

---

## V-01 -- Axis: Pre-phase PERSONA REGISTRY (C-43 maximum)

**Hypothesis**: R14 embedded each persona's prohibitions inside the phase section where
that persona activates. V-01 tests whether hoisting all four personas into a single
PERSONA REGISTRY section before Phase 1 -- each entry carrying role name, owned phase,
owned artifacts, domain description, and exactly 5 prohibitions -- makes role authority
auditable from one section without reading phase bodies. The registry becomes the source
of truth for role identity; phase headers cite it by name rather than restating it. A
reader who wants to know "what is the Analyst forbidden to do?" consults the registry,
not Phase 3. Phase 4 active-role header: R14 V-05 baseline. TERMINAL: 28 items.

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

## PERSONA REGISTRY

All four campaign personas are declared here. This registry is the authority for role
identity, ownership, and prohibitions. Phase headers cite this registry; they do not
restate it. Any behavior not listed as a prohibition is permitted within the persona's
declared domain.

### REGISTRAR
- Phase: 1 (Register)
- Owned artifact: strategy.md
- Domain: Topic identity, namespace assignment, signal planning
- Prohibitions (exactly 5):
  1. SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
  2. SHALL NOT synthesize or interpret signal content
  3. SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
  4. SHALL NOT invoke any sub-skill other than topic-new
  5. SHALL NOT list signals not declared in planned_signals

### PLANNER
- Phase: 2 (Plan)
- Owned artifact: roadmap.md
- Domain: Signal ordering, collection purpose, namespace routing
- Prohibitions (exactly 5):
  1. SHALL NOT register, rename, or modify topic identity (Phase 1 domain)
  2. SHALL NOT query or report which signals are collected (Phase 3 domain)
  3. SHALL NOT produce readiness verdicts or coverage ratios
  4. SHALL NOT synthesize findings or assign verdict verbs
  5. SHALL NOT invoke any sub-skill other than topic-plan

### ANALYST
- Phase: 3 (Status)
- Owned artifacts: status.md, delta.md
- Domain: Signal counting, coverage computation, session diff, readiness verdict
- Prohibitions (exactly 5):
  1. SHALL NOT add planned signals beyond Phase 2 roadmap
  2. SHALL NOT produce verdict verbs from Phase 4 vocabulary
  3. SHALL NOT interpret meaning from signal content or editorialize
  4. SHALL NOT invoke any sub-skill other than topic-status
  5. SHALL NOT use narrative counts where integers are required

### NARRATOR
- Phase: 4 (Narrative)
- Owned artifact: story.md
- Domain: Hypothesis mutation, echo synthesis, next-signal recommendations, verdict
- Prohibitions (exactly 5):
  1. SHALL NOT modify coverage table, namespace counts, or coverage ratio (Phase 3)
  2. SHALL NOT add, remove, or reorder planned signals (Phase 2 domain)
  3. SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
  4. SHALL NOT invoke any sub-skill other than topic-story
  5. SHALL NOT declare Phase 4 complete without writing story.md (violates Transition
     Obligation, Phase Boundary Summary, Phase 3->4)

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 active-role header |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 active-role header |
| Phase 4 receives readiness_verdict + coverage_ratio (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 does NOT receive namespace counts | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 SHALL write story.md before declaring complete | Phase Boundary Summary Phase 3->4 (Transition Obligation) | Phase 4 obligation block + TERMINAL |
| verdict_after updates after Phase 4 completes | Two-Pass Delta Rule | Post-Phase-4 section + TERMINAL |
| Cascade target is verdict_after only | Cascade Rule | Phase Boundary Summary Phase 3->4 (Cascade Scope) |

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
Governs what a Phase 3 Step B re-run updates. Applies when Phase 3 is re-run after
Phase 4 has already completed. Defined in Cascade Rule above.
- Update target: verdict_after in delta.md (Phase 4-dependent; sole cascade target)
- Excluded from cascade: session_number, signals_added, signals_removed,
  verdict_before, verdict_changed (finalized at Phase 3 Step B; Phase 4 does not own)

#### Receiving Scope (entry concern)
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

#### Transition Obligation (exit concern)
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

Prohibition lists are declared in the PERSONA REGISTRY above. Phase sections cite
the registry; they do not restate prohibitions.

---

## Phase 1 -- Register

*REGISTRAR active (see PERSONA REGISTRY for domain + prohibitions). Phase 1 Contract
governs output. Boundary: Phase 1 produces strategy.md for Phase 2 input.*

The REGISTRAR SHALL invoke topic-new for {{topic}}.

The REGISTRAR SHALL produce strategy.md per Phase 1 Contract:
- topic_name, namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields typed correctly.

GATE: The campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan

*PLANNER active (see PERSONA REGISTRY for domain + prohibitions). Phase 2 Contract
governs output. Boundary: Phase 2 receives planned_signals from strategy.md; produces
roadmap.md for Phase 3 input.*

The PLANNER SHALL invoke topic-plan for {{topic}}.

The PLANNER SHALL produce roadmap.md per Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose per signal.

GATE: The campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status

*ANALYST active (see PERSONA REGISTRY for domain + prohibitions). Phase 3 Contract
governs status.md. Session Delta Contract governs delta.md. Boundary: Phase 3 receives
namespace_coverage from roadmap.md; produces status.md and delta.md for Phase 4 input
per Phase Boundary Summary (Cascade Scope + Receiving Scope + Transition Obligation).*

### Step A -- Coverage Status

The ANALYST SHALL invoke topic-status for {{topic}}.

The ANALYST SHALL produce status.md per Phase 3 Contract:
- All 9 namespace rows -- no row SHALL be skipped
- planned and collected SHALL be integers (narrative counts fail)
- missing SHALL list signal names as strings, not counts
- zero_flag SHALL be "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

FINALIZATION: status.md fields (planned, collected, missing, zero_flag, coverage_ratio,
readiness_verdict) are finalized at this write. These fields are Phase 3 domain.
Per Receiving Scope (Phase Boundary Summary, Phase 3->4), Phase 4 does not receive
namespace counts and cannot modify them.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

The ANALYST SHALL produce delta.md per Session Delta Contract.

Two-pass protocol: verdict_after SHALL be "NOT YET REACHED" (placeholder; Phase 4
not yet run). All other fields SHALL be written as final values at this step.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md both present. status.md has 9 rows,
integer fields, readiness_verdict assigned. delta.md has placeholder verdict_after.

GATE: The campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition is
satisfied.

---

## Phase 4 -- Narrative

**Obligation**: The NARRATOR SHALL write story.md before declaring Phase 4 complete.
If Phase 4 completes without writing story.md, downstream systems cannot distinguish
an interrupted campaign from a completed one -- `verdict_after` remains "NOT YET
REACHED" in both cases. The Transition Obligation (Phase Boundary Summary, Phase 3->4)
is violated. The ambiguity cannot be resolved from the delta.md artifact alone.

*NARRATOR active (see PERSONA REGISTRY for domain + prohibitions). Phase 4 Contract
governs output. Receiving scope (Phase Boundary Summary, Phase 3->4): Phase 4 does NOT
receive namespace counts -- planned, collected, missing, zero_flag were finalized at
Phase 3 Step A and Phase 4 cannot change them. They are Phase 3 domain. Phase 4
receives readiness_verdict and coverage_ratio from status.md as read-only context.*

The NARRATOR SHALL invoke topic-story for {{topic}}.

The NARRATOR SHALL produce story.md per Phase 4 Contract:
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

Phase 1 (REGISTRAR): Create strategy.md per Phase 1 Contract. Founding artifact.
Phase 2 (PLANNER): Create roadmap.md per Phase 2 Contract. All signals planned.

Phase 3 (ANALYST):
  Step A: All rows SHALL have collected = 0 (integer). missing SHALL list all
    planned signals by signal_name. zero_flag SHALL be "NO SIGNALS" where planned
    = 0 AND collected = 0. readiness_verdict SHALL be "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
    verdict_before = "NONE". verdict_after = "NOT YET REACHED" (placeholder).
    verdict_changed = "N/A".

Phase 4 (NARRATOR): The Transition Obligation applies on first invocation -- story.md
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

**Rubric targeting**: C-01 through C-42 (full R14 V-05 baseline). **C-43** (PERSONA
REGISTRY section present before Phase 1; all four personas listed with Phase, Owned
artifact, Domain, and exactly 5 prohibitions; phase sections cite "see PERSONA
REGISTRY" rather than restating prohibitions; Prohibition Parity Rule references
registry as authority). **C-44** (Phase 4 contract at 4 components, not extended --
C-44 deliberately absent to isolate V-01 axis). **C-45** (ANALYST closure absent --
deliberate). **TERMINAL**: 28 items.

---

## V-02 -- Axis: Six-component Phase 4 contract (C-44 maximum)

**Hypothesis**: R15 V-01 ES-2 identified that explicitly naming coverage_ratio and
session_delta as required Phase 4 typed fields forces the NARRATOR to pull evidence
from prior phases rather than synthesizing in isolation. V-02 tests whether declaring
these as Phase 4 Contract fields -- with typed constraints -- and adding corresponding
TERMINAL checks creates a measurable link between status.md (Phase 3 output) and
story.md (Phase 4 output). The hypothesis is that NARRATOR is now constrained to
report Phase 3 evidence, not just assert a verdict. PERSONA REGISTRY: absent (isolates
axis). Closure statements: R14 V-05 baseline. TERMINAL: 30 items (2 new).

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

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 active-role header |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 active-role header |
| Phase 4 receives readiness_verdict + coverage_ratio (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 does NOT receive namespace counts | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 SHALL write story.md before declaring complete | Phase Boundary Summary Phase 3->4 (Transition Obligation) | Phase 4 obligation block + TERMINAL |
| verdict_after updates after Phase 4 completes | Two-Pass Delta Rule | Post-Phase-4 section + TERMINAL |
| Cascade target is verdict_after only | Cascade Rule | Phase Boundary Summary Phase 3->4 (Cascade Scope) |
| story.md SHALL carry coverage_ratio from status.md | Phase 4 Contract (six-component) | Phase 4 execution + TERMINAL |
| story.md SHALL carry session_delta from delta.md | Phase 4 Contract (six-component) | Phase 4 execution + TERMINAL |

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

### Phase 4 Contract -- story.md (six-component)

Component 1 -- verdict_verb:
  - verdict_verb: string, exactly one of:
    CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
  - (SHALL NOT paraphrase; exactly one token from controlled vocabulary)

Component 2 -- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration; SHALL NOT be empty)
  - current: string (updated hypothesis reflecting signal evidence, or literal
    "UNCHANGED" if no mutation)

Component 3 -- echoes:
  - echoes: list of strings (signals collected outside roadmap plan)
  - If none: value SHALL be ["NONE"] (NOT an empty list)

Component 4 -- next_signal_recommendations:
  - List of exactly 3 items; each item:
    - namespace: string (one of 9 Signal namespaces)
    - skill: string (skill name within namespace)
    - gap_reason: string (one sentence explaining the gap)

Component 5 -- coverage_context (read-only from status.md):
  - coverage_ratio: string (SHALL match coverage_ratio in status.md exactly; Phase 4
    does not recompute this value; copies from read-only Phase 3 output)
  - readiness_verdict: string (SHALL match readiness_verdict in status.md exactly;
    Phase 4 does not assign this; copies from read-only Phase 3 output)

Component 6 -- session_context (read-only from delta.md):
  - session_number: integer (SHALL match session_number in delta.md)
  - signals_added_count: integer >= 0 (count of signals_added list from delta.md)

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
Pass 2 (Post-Phase-4): After story.md is written, update verdict_after to the
actual verdict_verb from story.md. This is the only post-Phase-4 write.

The terminal checklist item for verdict_after is order-dependent: placeholder
"NOT YET REACHED" after Phase 4 completes is a defect unless Phase 4 verdict_verb
is also "NOT YET REACHED".

---

## Cascade Rule

When Phase 3 Step B is re-run after Phase 4 has already completed, only verdict_after
in delta.md SHALL be updated. The cascade target is verdict_after alone.

The remaining delta.md fields SHALL NOT be modified because they were finalized at
Phase 3 Step B and Phase 4 cannot change them. Cascading them would overwrite
finalized session history with Phase 4 data that is not session-scoped.

Only verdict_after is Phase 4-dependent, which is why it is the only cascade target.

---

## Phase Boundary Summary

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
Governs what a Phase 3 Step B re-run updates. Applies when Phase 3 is re-run after
Phase 4 has already completed.
- Update target: verdict_after in delta.md (Phase 4-dependent; sole cascade target)
- Excluded from cascade: session_number, signals_added, signals_removed,
  verdict_before, verdict_changed (finalized at Phase 3 Step B; Phase 4 does not own)

#### Receiving Scope (entry concern)
Governs what Phase 4 receives as inputs at entry. Independent of Cascade Scope.
- Phase 4 receives: readiness_verdict and coverage_ratio from status.md (read-only
  context; Phase 4 does not modify these values; carries them to story.md Component 5)
- Phase 4 receives: delta.md session_number and signals_added count (read-only;
  carries them to story.md Component 6)
- Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED" (placeholder;
  Phase 4 updates this via the Post-Phase-4 write)
- Phase 4 does NOT receive: namespace counts (planned, collected, missing, zero_flag)
  -- finalized at Phase 3 Step A; Phase 4 cannot change them; they are Phase 3 domain.

#### Transition Obligation (exit concern)
Phase 4 SHALL write story.md. If Phase 4 exits without writing story.md, downstream
systems cannot distinguish an interrupted campaign from a completed one -- both states
produce `verdict_after = NOT YET REACHED` in delta.md. The ambiguity is unresolvable
from the delta.md artifact alone.

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
Owns status.md AND delta.md.

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

The Planner SHALL produce roadmap.md per Phase 2 Contract.

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose per signal.

GATE: The campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md. Boundary: Phase 3 receives namespace_coverage
from roadmap.md; produces status.md and delta.md per Phase Boundary Summary (Cascade
Scope + Receiving Scope + Transition Obligation).*

### Step A -- Coverage Status

The Analyst SHALL invoke topic-status for {{topic}}.

The Analyst SHALL produce status.md per Phase 3 Contract:
- All 9 namespace rows -- no row SHALL be skipped
- planned and collected SHALL be integers; missing SHALL list signal names
- zero_flag SHALL be "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

FINALIZATION: status.md fields finalized at this write. Phase 4 reads coverage_ratio
and readiness_verdict as read-only context (Receiving Scope, Phase Boundary Summary,
Phase 3->4). Phase 4 carries these values into story.md Component 5 unchanged.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

The Analyst SHALL produce delta.md per Session Delta Contract.
verdict_after = "NOT YET REACHED" (placeholder). All other fields are final.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

ANALYST closes at delta.md write. ANALYST does not carry work into Phase 4.

Phase 3 postcondition: status.md AND delta.md both present, typed correctly.

GATE: The campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition is
satisfied.

---

## Phase 4 -- Narrative (Narrator)

**Obligation**: The Narrator SHALL write story.md before declaring Phase 4 complete.
If Phase 4 completes without writing story.md, downstream systems cannot distinguish
an interrupted campaign from a completed one. The Transition Obligation (Phase Boundary
Summary, Phase 3->4) is violated. The ambiguity cannot be resolved from delta.md alone.

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract (six-component)
governs output. Receiving scope (Phase Boundary Summary, Phase 3->4): Phase 4 does NOT
receive namespace counts -- finalized at Phase 3 Step A; Phase 4 domain excludes them.
Phase 4 receives readiness_verdict and coverage_ratio (read-only; Component 5) and
session_number + signals_added_count from delta.md (read-only; Component 6).*

The Narrator SHALL invoke topic-story for {{topic}}.

The Narrator SHALL produce story.md per Phase 4 Contract (six components required):
- Component 1: verdict_verb (exactly one of 5 tokens)
- Component 2: hypothesis_mutation (s0 + current)
- Component 3: echoes (list; ["NONE"] if empty)
- Component 4: next_signal_recommendations (exactly 3 items)
- Component 5: coverage_context (coverage_ratio + readiness_verdict from status.md,
  copied verbatim; SHALL NOT recompute)
- Component 6: session_context (session_number + signals_added_count from delta.md)

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

After story.md is written, update delta.md:
- Set verdict_after = verdict_verb from story.md
- Set verdict_changed = YES/NO/N/A per comparison with verdict_before

Only verdict_after and verdict_changed are updated. See Cascade Rule.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases SHALL run and produce full artifacts per typed contracts.

Phase 3 (Analyst):
  collected = 0 in all rows. missing = all planned signals. readiness_verdict = NOT READY.
  session_number = 1. signals_added = []. verdict_before = NONE.

Phase 4 (Narrator): verdict_verb = NOT YET REACHED. Component 5 coverage_ratio from
  status.md. Component 6 session_number = 1, signals_added_count = 0.

---

## TERMINAL -- Field-Level Completion Checklist

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
[ ] coverage_context.coverage_ratio: matches status.md coverage_ratio -- FAIL: re-run Phase 4
[ ] session_context.session_number: integer, matches delta.md -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B
[ ] verdict_after: reflects Phase 4 verdict_verb; placeholder NOT remaining after
    Phase 4 completes -- FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 30 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 30 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations +
   coverage_context + session_context (Phase 4, six components)
5. Session delta summary (session_number, signals_added count, verdict change)
```

**Rubric targeting**: C-01 through C-42 (full R14 V-05 baseline). **C-44** (Phase 4
contract explicitly named as "six-component"; Components 5 + 6 typed: coverage_context
carries coverage_ratio + readiness_verdict from status.md verbatim; session_context
carries session_number + signals_added_count from delta.md; TERMINAL gains two new
items for these fields; 30 TERMINAL items total; Receiving Scope updated to list both
new read-only inputs). **C-43** (PERSONA REGISTRY absent -- deliberate). **C-45**
(ANALYST closure statement present at Step B but not elevated to Closure Parity Rule).

---

## V-03 -- Axis: Closure Parity Rule (C-45 maximum)

**Hypothesis**: R15 V-01 ES-3 placed a closure statement at Phase 3->4 only. V-03
tests whether declaring a CLOSURE PARITY RULE -- mandating one closure statement at
the exit of every phase boundary, not just Phase 3->4 -- makes scope authority at
all three handoff points auditable without reading prohibition lists. Three surfaces:
Registrar closes (Phase 1 exit), Planner closes (Phase 2 exit), Analyst closes
(Phase 3 exit). The rule declares the pattern; the instances enforce it. A reader
can verify closure compliance by checking three line locations rather than re-reading
four prohibition lists. Phase 4 Contract: R14 V-05 baseline (4 components). PERSONA
REGISTRY: absent. TERMINAL: 28 items.

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

## Closure Parity Rule

Each phase SHALL carry exactly one closure statement at its exit boundary. Format:
"[ROLE] closes at [artifact] write. [ROLE] does not carry work into Phase [N+1]."

Three instances required -- one per Phase 1, 2, and 3 exit. The Phase 4 exit is
the Post-Phase-4 Delta Update; it is not a role-handoff boundary and does not carry
a closure statement.

A phase section that ends without a closure statement before the GATE SHALL fail
the Closure Parity Rule.

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 active-role header |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 active-role header |
| Phase 4 receives readiness_verdict + coverage_ratio (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 does NOT receive namespace counts | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 SHALL write story.md before declaring complete | Phase Boundary Summary Phase 3->4 (Transition Obligation) | Phase 4 obligation block + TERMINAL |
| verdict_after updates after Phase 4 completes | Two-Pass Delta Rule | Post-Phase-4 section + TERMINAL |
| Cascade target is verdict_after only | Cascade Rule | Phase Boundary Summary Phase 3->4 (Cascade Scope) |
| Registrar closes at strategy.md write | Closure Parity Rule | Phase 1 exit |
| Planner closes at roadmap.md write | Closure Parity Rule | Phase 2 exit |
| Analyst closes at delta.md write | Closure Parity Rule | Phase 3 exit |

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
  - planned: integer >= 0
  - collected: integer >= 0
  - missing: list of strings (signal names; [] if none)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N"
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md
- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis at registration)
  - current: string (updated or "UNCHANGED")
- echoes: list of strings; ["NONE"] if none
- next_signal_recommendations: list of exactly 3 items:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

### Session Delta Contract -- delta.md
- session_number: integer >= 1
- signals_added: list of signal names ([] if none)
- signals_removed: list of signal names ([] if none)
- verdict_before: string, exactly one of: READY | NOT READY | CONDITIONALLY READY | NONE
- verdict_after: string, exactly one of:
  READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
- verdict_changed: string, exactly one of: YES | NO | N/A

---

## Two-Pass Delta Rule

Pass 1 (Phase 3 Step B): verdict_after = "NOT YET REACHED" (placeholder).
Pass 2 (Post-Phase-4): Update verdict_after to verdict_verb from story.md.

---

## Cascade Rule

When Phase 3 Step B is re-run after Phase 4 has completed, only verdict_after updates.
All other delta.md fields are finalized at Phase 3 Step B and do not cascade.

---

## Phase Boundary Summary

### Phase 1 -> Phase 2 Boundary
- Output: strategy.md (planned_signals to Phase 2)
- Input: planned_signals list builds namespace_coverage

### Phase 2 -> Phase 3 Boundary
- Output: roadmap.md (namespace_coverage to Phase 3)
- Input: namespace_coverage populates planned counts and missing names

### Phase 3 -> Phase 4 Boundary

#### Cascade Scope (re-run concern)
- Update target: verdict_after in delta.md
- Excluded: session_number, signals_added, signals_removed, verdict_before,
  verdict_changed (Phase 3 Step B domain; not Phase 4-dependent)

#### Receiving Scope (entry concern)
- Phase 4 receives: readiness_verdict + coverage_ratio (read-only)
- Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED"
- Phase 4 does NOT receive: namespace counts (finalized Phase 3 Step A; Phase 3 domain)

#### Transition Obligation (exit concern)
Phase 4 SHALL write story.md. Without story.md, interrupted and completed campaigns
are indistinguishable from delta.md alone.

### Post-Phase-4 -> Dashboard Boundary
- delta.md updated with verdict_after + verdict_changed
- Dashboard: all five artifacts written; TERMINAL PASS

---

## Prohibition Parity Rule

Each role SHALL carry exactly 5 forbidden actions. Numbered list, 1 through 5.

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
Owns status.md AND delta.md.

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

The Registrar SHALL invoke topic-new for {{topic}} and produce strategy.md per Phase 1
Contract: topic_name, namespace (one of 9 tokens), priority (one of 3 tokens),
planned_signals (>= 3 items with signal_name, target_skill, rationale).

Phase 1 postcondition: strategy.md present, all fields typed correctly.

Registrar closes at strategy.md write. Registrar does not carry work into Phase 2.

GATE: The campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.
Boundary: Phase 2 receives planned_signals from strategy.md; produces roadmap.md for
Phase 3 input.*

The Planner SHALL invoke topic-plan for {{topic}} and produce roadmap.md per Phase 2
Contract: namespace_coverage entries for all namespaces with planned signals; each
signal entry has signal_name (matched to strategy.md) + collection_purpose.

Phase 2 postcondition: roadmap.md present with at least one namespace entry.

Planner closes at roadmap.md write. Planner does not carry work into Phase 3.

GATE: The campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition is
satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs status.md.
Session Delta Contract governs delta.md. Boundary: Phase 3 receives namespace_coverage
from roadmap.md; produces status.md and delta.md per Phase Boundary Summary (Cascade
Scope + Receiving Scope + Transition Obligation).*

### Step A -- Coverage Status

The Analyst SHALL invoke topic-status for {{topic}} and produce status.md per Phase 3
Contract: 9 namespace rows, integer fields, zero_flag, coverage_ratio, readiness_verdict.

FINALIZATION: status.md fields finalized at this write. Per Receiving Scope (Phase
Boundary Summary, Phase 3->4), Phase 4 does not receive namespace counts.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

The Analyst SHALL produce delta.md: session_number, signals_added, signals_removed,
verdict_before, verdict_after = "NOT YET REACHED" (placeholder), verdict_changed.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Phase 3 postcondition: status.md AND delta.md both present, typed correctly.

Analyst closes at delta.md write. Analyst does not carry work into Phase 4.

GATE: The campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition is
satisfied.

---

## Phase 4 -- Narrative (Narrator)

**Obligation**: The Narrator SHALL write story.md before declaring Phase 4 complete.
If Phase 4 completes without writing story.md, downstream systems cannot distinguish
an interrupted campaign from a completed one. The Transition Obligation (Phase Boundary
Summary, Phase 3->4) is violated.

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.
Receiving scope (Phase Boundary Summary, Phase 3->4): Phase 4 does NOT receive
namespace counts -- finalized at Phase 3 Step A; Phase 3 domain. Phase 4 receives
readiness_verdict and coverage_ratio from status.md as read-only context.*

The Narrator SHALL invoke topic-story for {{topic}} and produce story.md per Phase 4
Contract: verdict_verb, hypothesis_mutation, echoes, next_signal_recommendations.

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

Update delta.md: verdict_after = verdict_verb from story.md; verdict_changed per
comparison. Only these two fields update. See Cascade Rule.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All phases run. Phase 3: collected = 0 all rows; readiness_verdict = NOT READY.
Phase 4: verdict_verb = NOT YET REACHED. All closure statements apply.

---

## TERMINAL -- Field-Level Completion Checklist

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
[ ] verdict_after: reflects Phase 4 verdict_verb; placeholder NOT remaining after
    Phase 4 completes -- FAIL: re-run Phase 3 Step B after Phase 4 completes
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

**Rubric targeting**: C-01 through C-42 (full R14 V-05 baseline). **C-45** (Closure
Parity Rule declared as governing section; three closure statements present at Phase 1,
Phase 2, Phase 3 exits; format enforced: "[ROLE] closes at [artifact] write. [ROLE]
does not carry work into Phase [N+1]"; Cross-Phase Obligation Index carries three
closure obligation rows). **C-43** (PERSONA REGISTRY absent -- deliberate). **C-44**
(Phase 4 at 4 components -- deliberate). **TERMINAL**: 28 items.

---

## V-04 -- Combined: C-43 + C-44 (PERSONA REGISTRY + Six-component Phase 4)

**Hypothesis**: V-01 and V-02 in combination tests whether the persona registry
(C-43) and the six-component Phase 4 contract (C-44) reinforce each other: the
NARRATOR's prohibition list in the registry is now paired with a stronger story.md
obligation (6 components). The registry declares what the Narrator cannot do; the
extended contract declares what the Narrator must do. Prohibition parity and
component parity work together. Closure statements at R14 V-05 baseline (Phase 3
only). TERMINAL: 30 items.

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

## PERSONA REGISTRY

All four campaign personas are declared here. This registry is the authority for role
identity, ownership, and prohibitions. Phase headers cite this registry by entry name.

### REGISTRAR
- Phase: 1 (Register)
- Owned artifact: strategy.md
- Domain: Topic identity, namespace assignment, signal planning
- Prohibitions (exactly 5):
  1. SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
  2. SHALL NOT synthesize or interpret signal content
  3. SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
  4. SHALL NOT invoke any sub-skill other than topic-new
  5. SHALL NOT list signals not declared in planned_signals

### PLANNER
- Phase: 2 (Plan)
- Owned artifact: roadmap.md
- Domain: Signal ordering, collection purpose, namespace routing
- Prohibitions (exactly 5):
  1. SHALL NOT register, rename, or modify topic identity (Phase 1 domain)
  2. SHALL NOT query or report which signals are collected (Phase 3 domain)
  3. SHALL NOT produce readiness verdicts or coverage ratios
  4. SHALL NOT synthesize findings or assign verdict verbs
  5. SHALL NOT invoke any sub-skill other than topic-plan

### ANALYST
- Phase: 3 (Status)
- Owned artifacts: status.md, delta.md
- Domain: Signal counting, coverage computation, session diff, readiness verdict
- Prohibitions (exactly 5):
  1. SHALL NOT add planned signals beyond Phase 2 roadmap
  2. SHALL NOT produce verdict verbs from Phase 4 vocabulary
  3. SHALL NOT interpret meaning from signal content or editorialize
  4. SHALL NOT invoke any sub-skill other than topic-status
  5. SHALL NOT use narrative counts where integers are required

### NARRATOR
- Phase: 4 (Narrative)
- Owned artifact: story.md
- Domain: Hypothesis mutation, echo synthesis, next-signal recommendations,
  verdict, coverage evidence reporting (Components 5-6 from status.md + delta.md)
- Prohibitions (exactly 5):
  1. SHALL NOT modify coverage table, namespace counts, or coverage ratio (Phase 3)
  2. SHALL NOT add, remove, or reorder planned signals (Phase 2 domain)
  3. SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
  4. SHALL NOT invoke any sub-skill other than topic-story
  5. SHALL NOT declare Phase 4 complete without writing story.md (violates Transition
     Obligation, Phase Boundary Summary, Phase 3->4)

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 active-role header |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 active-role header |
| Phase 4 receives readiness_verdict + coverage_ratio (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 does NOT receive namespace counts | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 SHALL write story.md before declaring complete | Phase Boundary Summary Phase 3->4 (Transition Obligation) | Phase 4 obligation block + TERMINAL |
| verdict_after updates after Phase 4 completes | Two-Pass Delta Rule | Post-Phase-4 + TERMINAL |
| Cascade target is verdict_after only | Cascade Rule | Phase Boundary Summary Phase 3->4 (Cascade Scope) |
| story.md SHALL carry coverage_ratio from status.md | Phase 4 Contract Component 5 | Phase 4 execution + TERMINAL |
| story.md SHALL carry session_delta from delta.md | Phase 4 Contract Component 6 | Phase 4 execution + TERMINAL |

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
- topic_name: string (non-empty)
- namespace: string, exactly one of 9 Signal namespaces
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items (signal_name, target_skill, rationale)

### Phase 2 Contract -- roadmap.md
- namespace_coverage: list of namespace entries with signals (signal_name,
  collection_purpose per signal)

### Phase 3 Contract -- status.md
- 9 namespace rows: namespace, planned (int), collected (int), missing (list),
  zero_flag ("NO SIGNALS" where applicable)
- coverage_ratio: "X/N" format
- readiness_verdict: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md (six-component)

Component 1 -- verdict_verb: one of CONFIRMED | REFUTED | EVOLVING |
  INSUFFICIENT | NOT YET REACHED

Component 2 -- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")

Component 3 -- echoes: list of strings; ["NONE"] if none

Component 4 -- next_signal_recommendations: exactly 3 items (namespace + skill +
  gap_reason per item)

Component 5 -- coverage_context (read-only from status.md):
  coverage_ratio: string (copied verbatim from status.md; SHALL NOT recompute)
  readiness_verdict: string (copied verbatim from status.md; SHALL NOT reassign)

Component 6 -- session_context (read-only from delta.md):
  session_number: integer (from delta.md)
  signals_added_count: integer (count of signals_added list from delta.md)

### Session Delta Contract -- delta.md
- session_number: integer >= 1
- signals_added: list ([] if none)
- signals_removed: list ([] if none)
- verdict_before: READY | NOT READY | CONDITIONALLY READY | NONE
- verdict_after: READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
- verdict_changed: YES | NO | N/A

---

## Two-Pass Delta Rule

Pass 1 (Phase 3 Step B): verdict_after = "NOT YET REACHED".
Pass 2 (Post-Phase-4): Update verdict_after = verdict_verb from story.md.

---

## Cascade Rule

Re-run of Phase 3 Step B after Phase 4 completes: only verdict_after updates.
All other delta.md fields finalized at Phase 3 Step B; do not cascade.

---

## Phase Boundary Summary

### Phase 1 -> Phase 2 Boundary
- strategy.md planned_signals -> Phase 2 namespace_coverage input

### Phase 2 -> Phase 3 Boundary
- roadmap.md namespace_coverage -> Phase 3 planned counts + missing names

### Phase 3 -> Phase 4 Boundary

#### Cascade Scope (re-run concern)
- Update target: verdict_after only
- Excluded: session_number, signals_added, signals_removed, verdict_before,
  verdict_changed

#### Receiving Scope (entry concern)
- Phase 4 receives: readiness_verdict + coverage_ratio (read-only; Component 5)
- Phase 4 receives: session_number + signals_added count from delta.md (read-only;
  Component 6)
- Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED"
- Phase 4 does NOT receive: namespace counts (finalized Phase 3 Step A; Phase 3 domain)

#### Transition Obligation (exit concern)
Phase 4 SHALL write story.md. Interrupted + completed campaigns are indistinguishable
from delta.md alone if story.md is absent.

### Post-Phase-4 -> Dashboard Boundary
- delta.md: verdict_after + verdict_changed updated
- Dashboard: all artifacts written; TERMINAL PASS

---

## Prohibition Parity Rule

Each role carries exactly 5 prohibitions (declared in PERSONA REGISTRY). Phase
sections cite registry; they do not restate prohibitions.

---

## Phase 1 -- Register

*REGISTRAR active (see PERSONA REGISTRY). Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}. Produce strategy.md per Phase 1 Contract.

Phase 1 postcondition: strategy.md present, typed correctly.

GATE: Campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan

*PLANNER active (see PERSONA REGISTRY). Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}. Produce roadmap.md per Phase 2 Contract.

Phase 2 postcondition: roadmap.md present, at least one namespace entry.

GATE: Campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status

*ANALYST active (see PERSONA REGISTRY). Phase 3 Contract governs status.md. Session
Delta Contract governs delta.md. Phase Boundary Summary (Cascade Scope + Receiving
Scope + Transition Obligation) governs Phase 3->4.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}. Produce status.md: 9 rows, integer fields,
zero_flag, coverage_ratio, readiness_verdict.

FINALIZATION: status.md fields finalized at this write. Phase 4 reads coverage_ratio
and readiness_verdict as read-only (Component 5). Per Receiving Scope (Phase Boundary
Summary, Phase 3->4), Phase 4 does not receive namespace counts.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md: session_number, signals_added, signals_removed, verdict_before,
verdict_after = "NOT YET REACHED" (placeholder), verdict_changed.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

ANALYST closes at delta.md write. ANALYST does not carry work into Phase 4.

Phase 3 postcondition: status.md AND delta.md present, typed correctly.

GATE: Campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition satisfied.

---

## Phase 4 -- Narrative

**Obligation**: The NARRATOR SHALL write story.md before declaring Phase 4 complete.
The Transition Obligation (Phase Boundary Summary, Phase 3->4) is violated otherwise.
Interrupted and completed campaigns are indistinguishable from delta.md alone.

*NARRATOR active (see PERSONA REGISTRY). Phase 4 Contract (six-component) governs
output. Receiving scope (Phase Boundary Summary, Phase 3->4): Phase 4 does NOT receive
namespace counts. Phase 4 receives readiness_verdict + coverage_ratio (Component 5;
read-only) and session_number + signals_added_count (Component 6; from delta.md).*

Invoke topic-story for {{topic}}. Produce story.md per Phase 4 Contract (six
components: verdict_verb, hypothesis_mutation, echoes, next_signal_recommendations,
coverage_context, session_context).

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

Update delta.md: verdict_after = verdict_verb; verdict_changed per comparison.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All phases run. Phase 3: collected = 0; readiness_verdict = NOT READY; session_number
= 1; signals_added = []. Phase 4: verdict_verb = NOT YET REACHED; Component 5 from
status.md; Component 6: session_number = 1, signals_added_count = 0.

---

## TERMINAL -- Field-Level Completion Checklist

### Phase 1 -- strategy.md
[ ] topic_name: string present, non-empty -- FAIL: re-run Phase 1
[ ] namespace: exactly one of 9 tokens -- FAIL: re-run Phase 1
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
[ ] coverage_context.coverage_ratio: matches status.md -- FAIL: re-run Phase 4
[ ] session_context.session_number: integer, matches delta.md -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B
[ ] verdict_after: reflects Phase 4 verdict_verb; placeholder NOT remaining after
    Phase 4 completes -- FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 30 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 30 TERMINAL items show PASS, emit in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis + echoes + top-3 + coverage_context +
   session_context (Phase 4, six components)
5. Session delta summary
```

**Rubric targeting**: C-01 through C-42. **C-43** (PERSONA REGISTRY present with all
four roles, ownership, domain, exactly 5 prohibitions each; phase sections cite registry
rather than restate; NARRATOR domain description now explicitly mentions Components 5-6).
**C-44** (Phase 4 Contract six-component; TERMINAL gains 2 items; 30 total; Cross-Phase
Obligation Index carries two new rows for Component 5 + 6 obligations). **C-45** (ANALYST
closure at Phase 3 Step B but no Closure Parity Rule -- not elevated; single surface).

---

## V-05 -- Full stack: C-43 + C-44 + C-45 + Prohibition Anchoring

**Hypothesis**: V-04 combined C-43 + C-44. V-05 adds C-45 (Closure Parity Rule at
all three phase exits) and a new pattern: PROHIBITION ANCHORING. Each prohibition in
every role's list carries an inline citation of the contract section or boundary rule
it enforces. Format: "SHALL NOT [action] ([Section Reference])". The hypothesis is
that prohibition anchoring creates per-item traceability from the prohibition back to
its source authority -- readers can verify that each prohibition is grounded in a
contract, not asserted arbitrarily. This is distinct from C-41 (which is about Phase
Boundary Summary back-references at specific structural sites) -- anchoring applies
at every prohibition line, not just at Phase 4 obligation/header/TERMINAL surfaces.
This pattern is a candidate for C-46: Prohibition-to-contract traceability per item.
TERMINAL: 30 items.

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

## Closure Parity Rule

Each phase SHALL carry exactly one closure statement at its exit boundary, before
the GATE. Format: "[ROLE] closes at [artifact] write. [ROLE] does not carry work
into Phase [N+1]." Three instances required (Phase 1, 2, 3 exits). Phase 4 exit
is the Post-Phase-4 Delta Update; it is not a role-handoff boundary.

---

## PERSONA REGISTRY

Authority for role identity, ownership, and prohibitions. Phase headers cite this
registry. Each prohibition carries an anchored citation to the contract section or
boundary rule it enforces.

### REGISTRAR
- Phase: 1 (Register)
- Owned artifact: strategy.md
- Domain: Topic identity, namespace assignment, signal planning
- Prohibitions (exactly 5):
  1. SHALL NOT produce coverage tables, coverage ratios, or readiness verdicts
     (Phase 3 Contract domain; Analyst owns status.md)
  2. SHALL NOT synthesize or interpret signal content
     (Phase 4 Contract domain; Narrator owns story.md)
  3. SHALL NOT assign verdict verbs from Phase 4 controlled vocabulary
     (Phase 4 Contract: verdict_verb enumerated set)
  4. SHALL NOT invoke any sub-skill other than topic-new
     (Phase 1 domain; signal integrity)
  5. SHALL NOT list signals not declared in planned_signals
     (Phase 1 Contract: planned_signals list is exhaustive)

### PLANNER
- Phase: 2 (Plan)
- Owned artifact: roadmap.md
- Domain: Signal ordering, collection purpose, namespace routing
- Prohibitions (exactly 5):
  1. SHALL NOT register, rename, or modify topic identity
     (Phase 1 Contract domain; Registrar owns strategy.md)
  2. SHALL NOT query or report which signals are collected
     (Phase 3 Contract domain; Analyst owns status.md)
  3. SHALL NOT produce readiness verdicts or coverage ratios
     (Phase 3 Contract: readiness_verdict + coverage_ratio are Analyst outputs)
  4. SHALL NOT synthesize findings or assign verdict verbs
     (Phase 4 Contract domain; Narrator owns story.md)
  5. SHALL NOT invoke any sub-skill other than topic-plan
     (Phase 2 domain; signal integrity)

### ANALYST
- Phase: 3 (Status)
- Owned artifacts: status.md, delta.md
- Domain: Signal counting, coverage computation, session diff, readiness verdict
- Prohibitions (exactly 5):
  1. SHALL NOT add planned signals beyond Phase 2 roadmap
     (Phase 2 Contract: namespace_coverage is the planning authority)
  2. SHALL NOT produce verdict verbs from Phase 4 vocabulary
     (Phase 4 Contract: verdict_verb enumerated set is Narrator domain)
  3. SHALL NOT interpret meaning from signal content or editorialize
     (Phase 4 Contract domain; Narrator owns hypothesis_mutation + echoes)
  4. SHALL NOT invoke any sub-skill other than topic-status
     (Phase 3 domain; signal integrity)
  5. SHALL NOT use narrative counts where integers are required
     (Phase 3 Contract: planned, collected typed as integer >= 0)

### NARRATOR
- Phase: 4 (Narrative)
- Owned artifact: story.md
- Domain: Hypothesis mutation, echo synthesis, next-signal recommendations,
  verdict, coverage evidence (Component 5), session evidence (Component 6)
- Prohibitions (exactly 5):
  1. SHALL NOT modify coverage table, namespace counts, or coverage ratio
     (Phase 3 Contract: status.md fields finalized at Phase 3 Step A)
  2. SHALL NOT add, remove, or reorder planned signals
     (Phase 2 Contract: namespace_coverage is the planning authority)
  3. SHALL NOT assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
     (Phase 3 Contract: readiness_verdict is Analyst output; Phase 4 reads it
     read-only per Receiving Scope, Phase Boundary Summary, Phase 3->4)
  4. SHALL NOT invoke any sub-skill other than topic-story
     (Phase 4 domain; signal integrity)
  5. SHALL NOT declare Phase 4 complete without writing story.md
     (Transition Obligation, Phase Boundary Summary, Phase 3->4)

---

## Cross-Phase Obligation Index

| Obligation | Declared at | Assertion site |
|---|---|---|
| Phase 2 receives planned_signals from strategy.md | Phase Boundary Summary Phase 1->2 | Phase 2 active-role header |
| Phase 3 receives namespace_coverage from roadmap.md | Phase Boundary Summary Phase 2->3 | Phase 3 active-role header |
| Phase 4 receives readiness_verdict + coverage_ratio (read-only) | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 does NOT receive namespace counts | Phase Boundary Summary Phase 3->4 (Receiving Scope) | Phase 4 active-role header |
| Phase 4 SHALL write story.md before declaring complete | Phase Boundary Summary Phase 3->4 (Transition Obligation) | Phase 4 obligation block + TERMINAL |
| verdict_after updates after Phase 4 completes | Two-Pass Delta Rule | Post-Phase-4 + TERMINAL |
| Cascade target is verdict_after only | Cascade Rule | Phase Boundary Summary Phase 3->4 (Cascade Scope) |
| story.md SHALL carry coverage_ratio from status.md | Phase 4 Contract Component 5 | Phase 4 execution + TERMINAL |
| story.md SHALL carry session_delta from delta.md | Phase 4 Contract Component 6 | Phase 4 execution + TERMINAL |
| Registrar closes at strategy.md write | Closure Parity Rule | Phase 1 exit |
| Planner closes at roadmap.md write | Closure Parity Rule | Phase 2 exit |
| Analyst closes at delta.md write | Closure Parity Rule | Phase 3 exit |

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md
- topic_name: string (non-empty)
- namespace: string, exactly one of 9 Signal namespaces
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items (signal_name, target_skill, rationale)

### Phase 2 Contract -- roadmap.md
- namespace_coverage: entries with signals (signal_name + collection_purpose)

### Phase 3 Contract -- status.md
- 9 namespace rows: namespace, planned (int), collected (int), missing (list),
  zero_flag ("NO SIGNALS" where applicable)
- coverage_ratio: "X/N"
- readiness_verdict: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md (six-component)

Component 1 -- verdict_verb: one of CONFIRMED | REFUTED | EVOLVING |
  INSUFFICIENT | NOT YET REACHED

Component 2 -- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")

Component 3 -- echoes: list; ["NONE"] if none

Component 4 -- next_signal_recommendations: exactly 3 items (namespace + skill +
  gap_reason per item)

Component 5 -- coverage_context (read-only from status.md):
  coverage_ratio: string (copied verbatim; SHALL NOT recompute)
  readiness_verdict: string (copied verbatim; SHALL NOT reassign)

Component 6 -- session_context (read-only from delta.md):
  session_number: integer
  signals_added_count: integer >= 0

### Session Delta Contract -- delta.md
- session_number: integer >= 1; signals_added: list; signals_removed: list
- verdict_before: READY | NOT READY | CONDITIONALLY READY | NONE
- verdict_after: READY | NOT READY | CONDITIONALLY READY | NOT YET REACHED
- verdict_changed: YES | NO | N/A

---

## Two-Pass Delta Rule

Pass 1 (Phase 3 Step B): verdict_after = "NOT YET REACHED".
Pass 2 (Post-Phase-4): Update verdict_after = verdict_verb from story.md.

---

## Cascade Rule

Phase 3 Step B re-run after Phase 4 completes: only verdict_after updates.
Remaining delta.md fields finalized at Phase 3 Step B; do not cascade.

---

## Phase Boundary Summary

### Phase 1 -> Phase 2 Boundary
- strategy.md planned_signals -> Phase 2 namespace_coverage input

### Phase 2 -> Phase 3 Boundary
- roadmap.md namespace_coverage -> Phase 3 planned counts + missing names

### Phase 3 -> Phase 4 Boundary

#### Cascade Scope (re-run concern)
- Update target: verdict_after in delta.md only
- Excluded: session_number, signals_added, signals_removed, verdict_before,
  verdict_changed

#### Receiving Scope (entry concern)
- Phase 4 receives: readiness_verdict + coverage_ratio (read-only; Component 5)
- Phase 4 receives: session_number + signals_added count (read-only; Component 6)
- Phase 4 receives: delta.md with verdict_after = "NOT YET REACHED"
- Phase 4 does NOT receive: namespace counts (Phase 3 Step A domain)

#### Transition Obligation (exit concern)
Phase 4 SHALL write story.md. Interrupted + completed campaigns indistinguishable
from delta.md alone without story.md.

### Post-Phase-4 -> Dashboard Boundary
- delta.md: verdict_after + verdict_changed updated
- Dashboard: all artifacts written; TERMINAL PASS

---

## Prohibition Parity Rule

Each role carries exactly 5 prohibitions with anchored citations (declared in PERSONA
REGISTRY). Phase sections cite registry; prohibitions are not restated in phase bodies.

---

## Phase 1 -- Register

*REGISTRAR active (see PERSONA REGISTRY: domain + 5 anchored prohibitions).
Phase 1 Contract governs output. Boundary: strategy.md -> Phase 2.*

Invoke topic-new for {{topic}}. Produce strategy.md per Phase 1 Contract.

Phase 1 postcondition: strategy.md present, all fields typed correctly.

Registrar closes at strategy.md write. Registrar does not carry work into Phase 2.

GATE: Campaign SHALL NOT proceed to Phase 2 until Phase 1 postcondition satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan

*PLANNER active (see PERSONA REGISTRY: domain + 5 anchored prohibitions).
Phase 2 Contract governs output. Boundary: roadmap.md -> Phase 3.*

Invoke topic-plan for {{topic}}. Produce roadmap.md per Phase 2 Contract.

Phase 2 postcondition: roadmap.md present, at least one namespace entry.

Planner closes at roadmap.md write. Planner does not carry work into Phase 3.

GATE: Campaign SHALL NOT proceed to Phase 3 until Phase 2 postcondition satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status

*ANALYST active (see PERSONA REGISTRY: domain + 5 anchored prohibitions).
Phase 3 Contract governs status.md. Session Delta Contract governs delta.md.
Phase Boundary Summary (Cascade Scope + Receiving Scope + Transition Obligation)
governs Phase 3->4.*

### Step A -- Coverage Status

Invoke topic-status for {{topic}}. Produce status.md: 9 rows, integer fields,
zero_flag, coverage_ratio, readiness_verdict.

FINALIZATION: status.md fields finalized at this write. Phase 4 reads coverage_ratio
and readiness_verdict as read-only (Component 5). Per Receiving Scope (Phase Boundary
Summary, Phase 3->4), Phase 4 does not receive namespace counts.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

### Step B -- Session Delta (Pass 1)

Produce delta.md: session_number, signals_added, signals_removed, verdict_before,
verdict_after = "NOT YET REACHED" (placeholder), verdict_changed.

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

Analyst closes at delta.md write. Analyst does not carry work into Phase 4.

Phase 3 postcondition: status.md AND delta.md present, typed correctly.

GATE: Campaign SHALL NOT proceed to Phase 4 until Phase 3 postcondition satisfied.

---

## Phase 4 -- Narrative

**Obligation**: The NARRATOR SHALL write story.md before declaring Phase 4 complete.
The Transition Obligation (Phase Boundary Summary, Phase 3->4) is violated otherwise.
Interrupted and completed campaigns are indistinguishable from delta.md alone.

*NARRATOR active (see PERSONA REGISTRY: domain + 5 anchored prohibitions).
Phase 4 Contract (six-component) governs output. Receiving scope (Phase Boundary
Summary, Phase 3->4): Phase 4 does NOT receive namespace counts. Phase 4 receives
readiness_verdict + coverage_ratio (read-only; Component 5) and session_number +
signals_added_count (read-only; Component 6).*

Invoke topic-story for {{topic}}. Produce story.md per Phase 4 Contract:
- Component 1: verdict_verb (exactly one of 5 tokens)
- Component 2: hypothesis_mutation (s0 + current)
- Component 3: echoes (list; ["NONE"] if none)
- Component 4: next_signal_recommendations (exactly 3 items)
- Component 5: coverage_context (coverage_ratio + readiness_verdict from status.md,
  copied verbatim)
- Component 6: session_context (session_number + signals_added_count from delta.md)

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Post-Phase-4 Delta Update (Pass 2)

Update delta.md: verdict_after = verdict_verb; verdict_changed per comparison.
Only these two fields update. See Cascade Rule.

Update: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All phases run. All closure statements apply. Phase 3: collected = 0 all rows;
readiness_verdict = NOT READY; session_number = 1; signals_added = [].
Phase 4: verdict_verb = NOT YET REACHED; Component 5 from status.md;
Component 6: session_number = 1, signals_added_count = 0.

---

## TERMINAL -- Field-Level Completion Checklist

### Phase 1 -- strategy.md
[ ] topic_name: string present, non-empty -- FAIL: re-run Phase 1
[ ] namespace: exactly one of 9 tokens -- FAIL: re-run Phase 1
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
[ ] coverage_context.coverage_ratio: matches status.md -- FAIL: re-run Phase 4
[ ] session_context.session_number: integer, matches delta.md -- FAIL: re-run Phase 4

### Session Delta -- delta.md
[ ] session_number: integer >= 1 -- FAIL: re-run Phase 3 Step B
[ ] signals_added: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] signals_removed: list present ([] permitted) -- FAIL: re-run Phase 3 Step B
[ ] verdict_before: one of {READY|NOT READY|CONDITIONALLY READY|NONE}
    FAIL: re-run Phase 3 Step B
[ ] verdict_after: reflects Phase 4 verdict_verb; placeholder NOT remaining after
    Phase 4 completes -- FAIL: re-run Phase 3 Step B after Phase 4 completes
[ ] verdict_changed: one of {YES|NO|N/A} -- FAIL: re-run Phase 3 Step B

All 30 items PASS: campaign complete. Dashboard SHALL be emitted.

---

## Output: Topic Dashboard

When all 30 TERMINAL items show PASS, emit in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis + echoes + top-3 + coverage_context +
   session_context (Phase 4, six components)
5. Session delta summary
```

**Rubric targeting**: C-01 through C-42. **C-43** (PERSONA REGISTRY present; all four
roles with Phase, Owned artifact, Domain, exactly 5 prohibitions; phase sections cite
registry; Prohibition Parity Rule updated to reference registry). **C-44** (six-component
Phase 4 contract; TERMINAL 30 items). **C-45** (Closure Parity Rule declared as governing
section; three instances at Phase 1, 2, 3 exits; Cross-Phase Obligation Index carries
three closure rows). **C-46 candidate -- Prohibition Anchoring** (every prohibition in
every role carries an inline citation of the contract section or boundary rule it
enforces, format "[action] ([Section Reference])"; makes prohibition-to-contract
traceability auditable per item without cross-reference reading; four roles x 5
prohibitions = 20 anchored citations total; distinct from C-41 which anchors specific
structural back-reference sites).

---

## Predicted Leaderboard

V-05 > V-04 > V-03 > V-01 = V-02

**V-05** (full stack): Max C-43 + C-44 + C-45 + C-46 candidate. Highest structural
density. Prohibition anchoring is a new pattern type not present in any prior variation.

**V-04** (C-43 + C-44): Both registry and six-component story. Persona registry +
extended contract reinforce each other; NARRATOR prohibition in registry now explicitly
scoped to include Component 5/6 read-only domain.

**V-03** (C-45 maximum): Closure Parity Rule at all three boundaries. Structural
novelty (three sites vs. one) but single-axis; may surface as a standalone excellence
signal if not subsumed by V-05.

**V-01 = V-02** (single-axis): Each targets one new criterion in isolation. V-01
(registry) and V-02 (six-component) score equivalently on the current rubric since
neither stacks.
