---
skill: quest-variate
skill_target: campaign-track
round: 3
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-track-rubric-v3-2026-03-16.md
---

# Variations -- campaign-track / Round 3

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

First variate run for this skill. All aspirational criteria (C-11 through C-16) are
untested. R3 rubric adds C-14 (per-role prohibition lists), C-15 (typed output
contracts per phase), and C-16 (terminal completion checklist) on top of the R1
additions C-11 (role-gated phases), C-12 (explicit progression gates), C-13
(empty-state as named section). Variations explore three new R2 axes individually,
then combine them, with a full-stack close.

---

## V-01 -- Axis: Per-role prohibition lists (C-14 maximum)

**Hypothesis**: Enumerating specific forbidden actions per role -- not just a role
description -- prevents role bleed: synthesis leaking into planning, planning
contaminating registration, analysis preempting narration. Named prohibitions are
auditable at scoring time; a role description alone is not. V-01 establishes the
baseline prohibition pattern and tests whether explicit forbidden-action lists per
persona are sufficient to enforce role discipline without typed contracts or a
terminal checklist.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Four phases run in order. Do not proceed to the next phase until
the current phase artifact is written.

---

## Roles

Four named personas run this campaign. Each carries a list of forbidden actions that
define the boundary of their role.

### Registrar
Runs Phase 1 (topic-new).
Responsible for: creating the topic strategy artifact, naming the topic, assigning
namespace, listing planned signals with rationale, setting priority.

**Forbidden actions**:
- Must not produce coverage tables or signal counts
- Must not issue readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
- Must not synthesize findings across signals
- Must not invoke any sub-skill other than topic-new
- Must not assign verdict verbs (CONFIRMED / REFUTED / EVOLVING / INSUFFICIENT)

### Planner
Runs Phase 2 (topic-plan).
Responsible for: expanding the strategy into a per-namespace signal map, labeling
each planned signal with skill name and collection purpose.

**Forbidden actions**:
- Must not register or rename the topic (that is Phase 1)
- Must not query which signals have already been collected (that is Phase 3)
- Must not produce a readiness verdict or coverage ratio
- Must not synthesize findings or issue verdict verbs
- Must not invoke any sub-skill other than topic-plan

### Analyst
Runs Phase 3 (topic-status).
Responsible for: building the 9-namespace coverage table (planned / collected /
missing), naming each gap explicitly, computing the coverage ratio, issuing the
readiness verdict.

**Forbidden actions**:
- Must not add or modify planned signals beyond what Planner defined
- Must not produce a narrative verdict verb (that is Phase 4)
- Must not synthesize meaning from signal content or interpret findings
- Must not invoke any sub-skill other than topic-status
- Must not change the topic name or namespace

### Narrator
Runs Phase 4 (topic-story).
Responsible for: selecting a verdict verb from the controlled vocabulary, writing the
hypothesis mutation block, calling out echo findings, recommending top-3 next signals.

**Forbidden actions**:
- Must not modify the coverage table (that is Phase 3)
- Must not add or remove planned signals
- Must not re-register or re-name the topic
- Must not issue a readiness verdict (READY / NOT READY / CONDITIONALLY READY)
- Must not invoke any sub-skill other than topic-story

---

## Phase 1 -- Register (Registrar)

Invoke topic-new for {{topic}}.

Produce strategy.md:
- Topic name
- Namespace assignment
- Priority level (High / Medium / Low)
- >= 3 planned signals, each with: signal name, target skill, rationale

Gate: Do not proceed to Phase 2 until strategy.md is present and contains all
required fields.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

Invoke topic-plan for {{topic}}.

Produce roadmap.md:
- Per-namespace signal map
- Each planned signal labeled with: namespace, skill name, collection purpose, why
  this signal is necessary for a commit decision

Gate: Do not proceed to Phase 3 until roadmap.md is present.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

Invoke topic-status for {{topic}}.

Produce status.md:
- 9-namespace coverage table with columns: Namespace | Planned | Collected | Missing
- Named gap entries -- not just counts; each missing signal named explicitly
- Coverage ratio: X collected / N planned
- Readiness verdict: READY / NOT READY / CONDITIONALLY READY
- Zero-signal namespaces flagged explicitly with "NO SIGNALS"

Gate: Do not proceed to Phase 4 until status.md is present with all table rows
complete and readiness verdict assigned.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

Invoke topic-story for {{topic}}.

Produce story.md:
- Verdict verb from controlled vocabulary:
  CONFIRMED / REFUTED / EVOLVING / INSUFFICIENT / NOT YET REACHED
- Hypothesis mutation block: S0 (original hypothesis), current form, or "UNCHANGED"
- At least one echo entry (unexpected finding); if none: "NONE"
- Top-3 next-signal recommendations: each with namespace, skill, and gap reason

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Empty-State Handling

When {{topic}} has 0 signals collected, each phase still runs:

Phase 1 (Registrar): Create strategy.md normally. This is the founding artifact.
Phase 2 (Planner): Create roadmap.md normally. All signals are in planned state.
Phase 3 (Analyst): Coverage table shows 0 collected across all namespaces.
  Readiness = NOT READY.
Phase 4 (Narrator): Verdict = NOT YET REACHED. Hypothesis mutation block shows S0
  (original, unchanged). Echo = NONE.

---

## Output: Topic Dashboard

At completion, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
```

**Rubric targeting**: C-01 (four phases in order), C-02 (strategy.md with namespace
and priority), C-03 (9-namespace coverage table with named gaps), C-04 (verdict verb
+ S0 mutation block), C-05 (empty-state per-phase behavior), C-06 (top-3
recommendations), C-07 (coverage ratio + readiness label), C-08 (zero-signal
namespaces flagged), C-09 (echo section with NONE fallback), C-11 (four role labels),
C-12 (explicit gate between every adjacent phase), C-13 (empty-state as dedicated
section with per-phase behavior), C-14 (each role carries 5 named forbidden actions).
**Misses**: C-15 (output fields have no type specifications -- "string" vs
"integer" vs "enumerated set" not declared), C-16 (no terminal completion checklist).
**Risk**: Prohibition lists add length but may become boilerplate; a model reciting
forbidden actions without actually preventing bleed. C-15 and C-16 are structurally
absent; scores cap at 14/16 criteria.

---

## V-02 -- Axis: Typed output contracts per phase (C-15 maximum)

**Hypothesis**: Specifying exact value types for every output field -- integer cell
values in the coverage table, enumerated string constants for readiness and verdict,
required field names with types -- forces structured artifacts and makes every field
independently verifiable. A narrative description of what a phase "should produce"
leaves ambiguity that a typed contract eliminates. V-02 tests whether typed contracts
alone (without role prohibitions or a terminal checklist) produce verifiable artifacts.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Four phases run in order. Do not proceed to the next phase until
the current phase artifact is written.

---

## Typed Output Contracts

Each phase produces a typed artifact. The types below are binding -- a field that
should be an integer must not be a range or a narrative description.

### Phase 1 Contract (topic-new -> strategy.md)

Required fields and types:
- topic_name: string (non-empty)
- namespace: string, one of: scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, one of: High | Medium | Low
- planned_signals: list of >= 3 items, each item:
  - signal_name: string
  - target_skill: string (namespace/skill format, e.g. "scout/scout-competitors")
  - rationale: string (one sentence)

### Phase 2 Contract (topic-plan -> roadmap.md)

Required fields and types:
- per_namespace_map: list of up to 9 namespace entries, each entry:
  - namespace: string (one of the 9 namespaces)
  - planned_signals: list of strings (signal names)
  - collection_purpose: string (one sentence per signal)

### Phase 3 Contract (topic-status -> status.md)

Required fields and types:
Coverage table -- one row per namespace, all 9 rows required:
  - namespace: string
  - planned: integer >= 0
  - collected: integer >= 0
  - missing: list of strings (signal names, or empty list)
  - zero_signal_flag: boolean -- true if both planned = 0 and collected = 0

Summary fields:
  - coverage_ratio: string in format "X/N" where X and N are integers
  - readiness_verdict: string, one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract (topic-story -> story.md)

Required fields and types:
  - verdict_verb: string, one of:
    CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
  - hypothesis_mutation:
    - s0: string (original hypothesis text)
    - current: string (current hypothesis text, or "UNCHANGED" if unchanged)
  - echoes: list of strings (unexpected findings); if empty, list must contain "NONE"
  - next_signal_recommendations: list of exactly 3 items, each:
    - namespace: string
    - skill: string
    - gap_reason: string (one sentence)

---

## Roles

Four named personas run this campaign in phase order.

- Registrar (Phase 1): Runs topic-new. Produces strategy.md per Phase 1 Contract.
- Planner (Phase 2): Runs topic-plan. Produces roadmap.md per Phase 2 Contract.
- Analyst (Phase 3): Runs topic-status. Produces status.md per Phase 3 Contract.
- Narrator (Phase 4): Runs topic-story. Produces story.md per Phase 4 Contract.

---

## Phase 1 -- Register (Registrar)

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract. All fields required. planned
must contain >= 3 signal entries. Priority must be one of the three enumerated values.

Gate: Do not proceed to Phase 2 until strategy.md contains all required fields with
correct types.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract. All 9 namespaces may be present;
list only those with planned signals. Collection purpose is required per signal entry.

Gate: Do not proceed to Phase 3 until roadmap.md is present.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract. All 9 namespace rows required.
planned and collected must be integers -- not ranges, not "several", not "many".
missing must name each signal explicitly -- not "3 signals missing". zero_signal_flag
must be true for every namespace with planned = 0 and collected = 0.

Gate: Do not proceed to Phase 4 until all 9 table rows are present and
readiness_verdict is assigned.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract. verdict_verb must be exactly one of
the five enumerated tokens -- no paraphrasing ("likely confirmed" fails). echoes list
must contain at least "NONE" -- an absent echoes field fails. next_signal_
recommendations must contain exactly 3 entries.

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

Phase 1 (Registrar): Create strategy.md normally per Phase 1 Contract.
Phase 2 (Planner): Create roadmap.md normally per Phase 2 Contract.
Phase 3 (Analyst): All coverage table rows have collected = 0. All missing lists
  name the planned signals. zero_signal_flag = true for namespaces with no planned
  signals. readiness_verdict = "NOT READY".
Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current =
  "UNCHANGED". echoes = ["NONE"].

---

## Output: Topic Dashboard

At completion, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
```

**Rubric targeting**: C-01 (four phases in order), C-02 (strategy.md -- typed: >=3
signals, namespace field, priority field), C-03 (9-namespace table -- typed: integer
cells, named gaps as string lists), C-04 (verdict verb enumerated type + mutation
block with s0/current), C-05 (empty-state with typed field values), C-06 (top-3
recommendations typed), C-07 (coverage_ratio typed as "X/N" + readiness_verdict as
enumerated), C-08 (zero_signal_flag per namespace), C-09 (echoes list with "NONE"
fallback), C-11 (four role labels), C-12 (gate after each phase), C-13 (empty-state
as dedicated section), C-15 (each phase specifies exact value types and enumerated
sets -- typed contracts at maximum enforcement).
**Misses**: C-14 (roles described but no enumerated forbidden actions), C-16 (no
terminal completion checklist).
**Risk**: Typed contracts add structural rigor but may cause a model to produce
JSON-like output rather than readable Markdown. The contract format (field: type)
is human-readable but formal enough to pressure the model toward structured output.
Scores cap at 14/16 criteria.

---

## V-03 -- Axis: Terminal completion checklist (C-16 maximum)

**Hypothesis**: A named TERMINAL section after Phase 4 -- requiring explicit per-phase
postcondition confirmation before the result is marked complete -- closes the most
common failure mode: a model claiming completion after running only 2-3 phases, or
producing an artifact that omits a required field without triggering a failure signal.
The checklist makes completion an active assertion, not an implicit assumption.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Four phases run in order. Do not proceed to the next phase until
the current phase artifact is written.

---

## Roles

Four named personas run this campaign:
- Registrar (Phase 1): Runs topic-new
- Planner (Phase 2): Runs topic-plan
- Analyst (Phase 3): Runs topic-status
- Narrator (Phase 4): Runs topic-story

---

## Phase 1 -- Register (Registrar)

Invoke topic-new for {{topic}}.

Produce strategy.md:
- Topic name and namespace assignment
- Priority level (High / Medium / Low)
- >= 3 planned signals: each with signal name, target skill, rationale

Gate: Do not proceed to Phase 2 until strategy.md is present with >= 3 planned
signals, namespace, and priority.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

Invoke topic-plan for {{topic}}.

Produce roadmap.md:
- Per-namespace signal map (namespace, planned signals, collection purpose per signal)

Gate: Do not proceed to Phase 3 until roadmap.md is present.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

Invoke topic-status for {{topic}}.

Produce status.md:
- 9-namespace coverage table: Namespace | Planned | Collected | Missing
- Missing signals named explicitly (not just counted)
- Coverage ratio: X collected / N planned
- Readiness verdict: READY / NOT READY / CONDITIONALLY READY
- Zero-signal namespaces flagged with "NO SIGNALS"

Gate: Do not proceed to Phase 4 until status.md is present with all 9 namespace rows
and readiness verdict assigned.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

Invoke topic-story for {{topic}}.

Produce story.md:
- Verdict verb: CONFIRMED / REFUTED / EVOLVING / INSUFFICIENT / NOT YET REACHED
- Hypothesis mutation block: S0 (original), current form, or "UNCHANGED"
- Echo entries (unexpected findings); if none: "NONE"
- Top-3 next-signal recommendations: namespace + skill + gap reason each

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

When {{topic}} has no signals yet, each phase still runs fully:

Phase 1 (Registrar): Create strategy.md normally. This is the founding artifact.
  strategy.md must be written even when no signals exist.
Phase 2 (Planner): Create roadmap.md normally. All signals remain in planned state.
  roadmap.md must be written even when no signals exist.
Phase 3 (Analyst): All 9 namespace rows show Collected = 0. All planned signals
  appear in Missing column by name. Readiness verdict = NOT READY.
  status.md must be written even with zero collected signals.
Phase 4 (Narrator): Verdict = NOT YET REACHED. Hypothesis mutation block shows S0
  (original, unchanged). Echo = NONE.
  story.md must be written even with zero collected signals.

---

## TERMINAL -- Completion Checklist

Before marking the campaign complete, verify all four phase postconditions. This
checklist is mandatory -- implicit completion is not acceptable.

[ ] Phase 1 postcondition: strategy.md written AND contains topic name, namespace,
    priority, and >= 3 planned signals with rationale.
    Status: PASS / FAIL -- if FAIL, re-run Phase 1 before proceeding.

[ ] Phase 2 postcondition: roadmap.md written AND contains per-namespace signal map
    with at least one signal entry per namespace that has planned coverage.
    Status: PASS / FAIL -- if FAIL, re-run Phase 2 before proceeding.

[ ] Phase 3 postcondition: status.md written AND contains all 9 namespace rows,
    named missing signals (not just counts), coverage ratio, and readiness verdict.
    Status: PASS / FAIL -- if FAIL, re-run Phase 3 before proceeding.

[ ] Phase 4 postcondition: story.md written AND contains verdict verb from controlled
    vocabulary, hypothesis mutation block with S0 entry, echo list (or "NONE"),
    and top-3 next-signal recommendations.
    Status: PASS / FAIL -- if FAIL, re-run Phase 4 before proceeding.

Only when all four items show PASS is the campaign complete and the dashboard ready.

---

## Output: Topic Dashboard

At completion (all TERMINAL checks PASS), emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
```

**Rubric targeting**: C-01 (four phases in order), C-02 (strategy.md fields named),
C-03 (9-namespace table with named gaps), C-04 (verdict verb + S0 mutation block),
C-05 (empty-state as dedicated section with per-phase behavior -- all four phases
addressed individually), C-06 (top-3 recommendations), C-07 (coverage ratio +
readiness verdict), C-08 (zero-signal namespaces flagged), C-09 (echo with NONE
fallback), C-11 (four role labels), C-12 (explicit gate between every phase), C-13
(empty-state as dedicated section with per-phase behavior), C-16 (TERMINAL section
present, all four phases listed with explicit PASS/FAIL conditions and re-run
instruction).
**Misses**: C-14 (roles named but no enumerated forbidden actions), C-15 (output
fields described but not typed -- "integer" vs "string" not specified).
**Risk**: The TERMINAL checklist is explicit and auditable. Re-run instruction for
FAIL state adds recovery semantics. Scores cap at 14/16 criteria.

---

## V-04 -- Combined Axes: Per-role prohibitions + typed output contracts (C-14 + C-15)

**Hypothesis**: Role prohibitions close role bleed; typed contracts close artifact
ambiguity. These two axes address independent failure modes -- one behavioral, one
structural -- and combining them should produce stronger coverage on both C-14 and
C-15 without either axis weakening the other. V-04 tests whether this combination
reaches 15/16 criteria without a terminal checklist.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Four phases run in order. Do not proceed to the next phase until
the current phase artifact is written.

---

## Typed Output Contracts

Each phase produces a typed artifact. These are binding specifications -- a field
typed as integer must not be a narrative description; a verdict field typed as an
enumerated string must use exactly one of the listed tokens.

### Phase 1 Contract -- strategy.md
- topic_name: string (non-empty)
- namespace: string, one of the 9 Signal namespaces
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item has:
  - signal_name: string
  - target_skill: string (namespace/skill format)
  - rationale: string (one sentence)

### Phase 2 Contract -- roadmap.md
- namespace_entries: list of namespace entries, each with:
  - namespace: string
  - signals: list of { signal_name: string, collection_purpose: string }

### Phase 3 Contract -- status.md
Coverage table -- all 9 namespace rows required:
  - namespace: string
  - planned: integer (not a range, not prose)
  - collected: integer (not a range, not prose)
  - missing: list of strings (signal names explicitly named; empty list if none)
  - zero_flag: "NO SIGNALS" if planned = 0 and collected = 0, else omit

Summary:
  - coverage_ratio: string formatted as "X/N" (both integers)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md
- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none found, list = ["NONE"]
- next_signals: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

---

## Roles

Four named personas run this campaign. Each has exclusive responsibilities and a
list of explicitly forbidden actions.

### Registrar (Phase 1 -- topic-new)

Responsible for producing strategy.md per Phase 1 Contract.

**Forbidden actions**:
- Must not produce coverage tables, coverage ratios, or readiness verdicts
- Must not interpret or synthesize signal content
- Must not issue verdict verbs from Phase 4 vocabulary
- Must not invoke sub-skills other than topic-new
- Must not create signals not listed as planned in strategy.md

### Planner (Phase 2 -- topic-plan)

Responsible for producing roadmap.md per Phase 2 Contract.

**Forbidden actions**:
- Must not register or rename the topic (Phase 1 domain)
- Must not query which signals are collected (Phase 3 domain)
- Must not produce readiness verdicts or coverage ratios
- Must not synthesize findings or issue verdict verbs
- Must not invoke sub-skills other than topic-plan

### Analyst (Phase 3 -- topic-status)

Responsible for producing status.md per Phase 3 Contract.

**Forbidden actions**:
- Must not add planned signals beyond what Phase 2 roadmap defines
- Must not issue verdict verbs (Phase 4 domain)
- Must not interpret meaning from signal content
- Must not invoke sub-skills other than topic-status
- Must not use prose counts ("several", "many") where integers are required

### Narrator (Phase 4 -- topic-story)

Responsible for producing story.md per Phase 4 Contract.

**Forbidden actions**:
- Must not modify the coverage table or coverage ratio (Phase 3 domain)
- Must not add or remove planned signals (Phase 2 domain)
- Must not issue readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
- Must not invoke sub-skills other than topic-story
- Must not paraphrase verdict verbs ("likely confirmed" fails; must use exact token)

---

## Phase 1 -- Register (Registrar)

Invoke topic-new for {{topic}}.

Produce strategy.md per Phase 1 Contract. All fields required. planned_signals
must contain >= 3 entries with signal_name, target_skill, and rationale.

Gate: Do not proceed to Phase 2 until strategy.md contains all required typed fields.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

Invoke topic-plan for {{topic}}.

Produce roadmap.md per Phase 2 Contract. Include only namespaces with planned
coverage. Each signal entry requires a collection_purpose string.

Gate: Do not proceed to Phase 3 until roadmap.md is present.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

Invoke topic-status for {{topic}}.

Produce status.md per Phase 3 Contract. All 9 namespace rows required. planned and
collected must be integers. missing must name each signal -- not just count them.
zero_flag must appear as "NO SIGNALS" for namespaces with both planned = 0 and
collected = 0. readiness_verdict must be exactly one of the three enumerated tokens.

Gate: Do not proceed to Phase 4 until all 9 rows are present, all integer fields are
integers, and readiness_verdict is assigned.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

Invoke topic-story for {{topic}}.

Produce story.md per Phase 4 Contract. verdict_verb must be exactly one of the five
enumerated tokens. echoes must contain at least "NONE" -- absent field fails.
next_signals must contain exactly 3 items with all required sub-fields.

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract normally.
Phase 2 (Planner): Create roadmap.md per Phase 2 Contract normally.
Phase 3 (Analyst): All collected = 0 (integer). All missing lists name planned
  signals by string. All namespaces with planned = 0 and collected = 0 get
  zero_flag = "NO SIGNALS". readiness_verdict = "NOT READY".
Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"].

---

## Output: Topic Dashboard

At completion, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
```

**Rubric targeting**: C-01 (four phases), C-02 (strategy.md with typed namespace,
priority, >= 3 signals), C-03 (9-namespace table -- integer cells, named missing
lists), C-04 (verdict_verb enumerated + mutation s0/current), C-05 (empty-state with
typed field values per phase), C-06 (top-3 recommendations typed), C-07 (coverage
ratio typed "X/N" + readiness_verdict enumerated), C-08 (zero_flag "NO SIGNALS"),
C-09 (echoes list with "NONE"), C-11 (four role labels), C-12 (explicit gate per
phase), C-13 (empty-state as dedicated section), C-14 (each role carries 5 named
forbidden actions -- maximum enforcement), C-15 (each phase specifies exact types
and enumerated sets -- maximum enforcement).
**Misses**: C-16 (no terminal completion checklist).
**Risk**: This is the longest variation prior to V-05. Both prohibition lists and
typed contracts add structure; the combination should reinforce rather than conflict,
but total prompt length may cause a model to apply contracts without applying
prohibitions (or vice versa). Scores cap at 15/16 criteria.

---

## V-05 -- Full Stack: Per-role prohibitions + typed contracts + terminal checklist + lifecycle emphasis

**Combined axes**: Per-role prohibition lists (C-14) + Typed output contracts (C-15)
+ Terminal completion checklist (C-16) + Lifecycle emphasis (explicit phase weight)

**Hypothesis**: The full-stack combination targets all 16 criteria. Each axis
contributes independently without competing: prohibition lists close role bleed
(C-14), typed contracts close artifact ambiguity (C-15), terminal checklist closes
premature completion (C-16), and heavy lifecycle emphasis gives each phase its own
dedicated block that communicates the campaign structure to a model that might
otherwise compress or merge phases. This variation should produce the most verifiable,
gate-complete campaign run of any R3 variation.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until
the current phase artifact is written and verified complete.

---

## Typed Output Contracts

These contracts are binding. Every field typed as integer must contain an integer
(not prose, not a range). Every field typed as enumerated string must contain
exactly one of the listed tokens.

### Phase 1 Contract -- strategy.md
- topic_name: string
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items, each:
  - signal_name: string
  - target_skill: string (namespace/skill format, e.g. "scout/scout-competitors")
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md
- namespace_coverage: list of namespace entries, each:
  - namespace: string
  - signals: list, each item: { signal_name: string, collection_purpose: string }

### Phase 3 Contract -- status.md
Coverage table -- all 9 namespace rows, each row:
  - namespace: string
  - planned: integer >= 0
  - collected: integer >= 0
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: string "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N" (X and N are integers)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md
- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis at topic registration)
  - current: string (current form after signals, or literal string "UNCHANGED")
- echoes: list of strings; if no unexpected findings, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items, each:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

---

## Roles and Prohibitions

Four named personas run this campaign in phase order. Each role has an enumerated
list of forbidden actions. These prohibitions are enforced at the point of execution,
not retroactively.

### Registrar (Phase 1 -- topic-new)

Owns strategy.md. Produces Phase 1 Contract output.

Forbidden:
1. Must not produce coverage tables, ratios, or readiness verdicts
2. Must not synthesize or interpret signal content
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not defined in the strategy

### Planner (Phase 2 -- topic-plan)

Owns roadmap.md. Produces Phase 2 Contract output.

Forbidden:
1. Must not register, rename, or modify the topic (Phase 1 domain)
2. Must not query or report on collected signal state (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)

Owns status.md. Produces Phase 3 Contract output.

Forbidden:
1. Must not add planned signals beyond Phase 2 roadmap
2. Must not produce verdict verbs (Phase 4 domain)
3. Must not interpret meaning from signal content or editorialize
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "a few") where integers are required

### Narrator (Phase 4 -- topic-story)

Owns story.md. Produces Phase 4 Contract output.

Forbidden:
1. Must not modify the coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

---

## Phase 1 -- Register (Registrar)

*Registrar active. All Phase 1 forbidden actions apply.*

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract:
- topic_name, namespace (one of 9 tokens), priority (one of 3 tokens)
- >= 3 planned_signals, each with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present with all required typed fields.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. All Phase 2 forbidden actions apply.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract:
- namespace_coverage entries for all namespaces that have planned signals
- Each signal entry has signal_name and collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. All Phase 3 forbidden actions apply.*

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows -- every namespace in Signal, no row skipped
- planned and collected are integers -- no narrative, no ranges
- missing lists each signal by name -- counts alone fail
- zero_flag = "NO SIGNALS" for namespaces where planned = 0 AND collected = 0
- coverage_ratio as "X/N" format
- readiness_verdict as exactly one of: READY | NOT READY | CONDITIONALLY READY

Phase 3 postcondition: status.md present with 9 rows, integer fields verified,
readiness_verdict assigned.

GATE: Do not proceed to Phase 4 until Phase 3 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. All Phase 4 forbidden actions apply.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract:
- verdict_verb: exactly one of the five enumerated tokens
- hypothesis_mutation: s0 (original) + current (updated text or "UNCHANGED")
- echoes: list with at least "NONE" -- absent field fails
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Phase 4 postcondition: story.md present with verdict_verb from enumerated set,
mutation block with s0, echoes list, and 3-item recommendations.

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

When {{topic}} has no collected signals, each phase still runs and produces its full
artifact per its typed contract.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract normally.
  planned_signals must list >= 3 entries. This is the founding artifact.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract normally.
  All signals are in planned state. roadmap.md documents what will be collected.

Phase 3 (Analyst): All coverage table rows have collected = 0 (integer).
  missing lists name all planned signals from roadmap.md by signal_name.
  Namespaces with planned = 0 and collected = 0 get zero_flag = "NO SIGNALS".
  readiness_verdict = "NOT READY".

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED".
  hypothesis_mutation.current = "UNCHANGED".
  echoes = ["NONE"].
  next_signal_recommendations: top 3 signals from roadmap.md by priority.

---

## TERMINAL -- Completion Checklist

Before marking the campaign complete, verify each phase postcondition explicitly.
All four items must show PASS. If any item shows FAIL, re-run the failing phase
before marking complete. Implicit completion is not acceptable.

[ ] Phase 1 PASS condition: strategy.md written. Contains topic_name, namespace
    (one of 9 tokens), priority (one of 3 tokens), and >= 3 planned_signals with
    signal_name + target_skill + rationale each.
    Result: PASS / FAIL

[ ] Phase 2 PASS condition: roadmap.md written. Contains at least one namespace
    entry with signal_name and collection_purpose per signal.
    Result: PASS / FAIL

[ ] Phase 3 PASS condition: status.md written. All 9 namespace rows present.
    planned and collected are integers. missing names each signal (not counts).
    coverage_ratio formatted as "X/N". readiness_verdict is one of 3 tokens.
    Result: PASS / FAIL

[ ] Phase 4 PASS condition: story.md written. verdict_verb is one of 5 tokens.
    hypothesis_mutation has s0 field. echoes is a list (minimum ["NONE"]).
    next_signal_recommendations has exactly 3 items.
    Result: PASS / FAIL

Campaign is complete only when all four items show PASS.

---

## Output: Topic Dashboard

When all TERMINAL checks pass, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
```

**Rubric targeting**: C-01 (four phases in order with explicit structure), C-02
(strategy.md -- typed namespace token + priority token + >=3 signals), C-03
(9-namespace table -- integer cells, named missing lists), C-04 (verdict_verb
enumerated token + mutation s0/current), C-05 (empty-state as dedicated section
with per-phase typed behavior), C-06 (top-3 recommendations with namespace +
skill + gap_reason), C-07 (coverage_ratio "X/N" + readiness_verdict enumerated),
C-08 (zero_flag "NO SIGNALS" typed), C-09 (echoes list minimum ["NONE"]), C-11
(four role labels consistent throughout), C-12 (explicit GATE statement per phase
with postcondition), C-13 (empty-state as dedicated section with per-phase behavior
for all four phases), C-14 (each role carries 5 enumerated forbidden actions labeled
1-5), C-15 (each phase specifies exact types and enumerated token sets), C-16
(TERMINAL section with per-phase PASS conditions and re-run instructions).
**Risk**: This is the longest variation. All three new axes plus lifecycle emphasis
combine to produce a prompt that covers all 16 criteria but may overwhelm a model
with structure -- every section has a contract, every role has prohibitions, every
phase has a gate, and the terminal checklist requires active confirmation. A model
that treats the structure as boilerplate and fills fields nominally passes formally
but not substantively. The TERMINAL checklist is the most direct defense against
that failure mode.

---

## Variation Summary

| ID | Primary Axes | New Criteria Targeted | Criteria Covered | Key Risk |
|----|-------------|----------------------|-----------------|----------|
| V-01 | Per-role prohibition lists | C-14 (5 forbidden per role) | 14/16 | Misses C-15, C-16; prohibitions as boilerplate |
| V-02 | Typed output contracts | C-15 (typed fields + enums) | 14/16 | Misses C-14, C-16; output structured but roles bleed |
| V-03 | Terminal completion checklist | C-16 (PASS/FAIL per phase) | 14/16 | Misses C-14, C-15; checklist passes but artifacts untyped |
| V-04 | Prohibitions + typed contracts | C-14 + C-15 | 15/16 | Misses C-16; length may dilute attention |
| V-05 | Prohibitions + contracts + checklist + lifecycle | C-14 + C-15 + C-16 | 16/16 | Most complex; formal compliance without substantive fill |

**Predicted leaderboard going into quest-score**: V-05 > V-04 > V-01 = V-02 = V-03.

V-05 is the only variation covering all 16 criteria. V-04 reaches 15/16 with the
strongest dual enforcement on C-14 and C-15. V-01, V-02, V-03 each cap at 14/16
targeting one new axis individually; which of these scores highest on the non-new
criteria (C-01 through C-13) will determine the order between them.

The main open question for scoring: does C-14 require exactly enumerated named
prohibitions (favors V-01, V-04, V-05) or is a role description with implicit
prohibitions sufficient? The rubric says "named forbidden actions, not just a role
description" -- which requires explicit enumeration. V-02 and V-03 each have role
descriptions only and will fail C-14.
