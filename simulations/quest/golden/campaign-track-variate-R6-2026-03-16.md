---
skill: quest-variate
skill_target: campaign-track
round: 6
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-track-rubric-v6-2026-03-16.md
---

# Variations -- campaign-track / Round 6

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

R3 closed C-14 (prohibition lists), C-15 (typed contracts), C-16 (terminal checklist).
R6 rubric adds three refinements:

- C-22 -- Prohibition-count parity: all 4 roles carry the same count (5) of named
  forbidden actions. Minimum viable was "at least one per role"; excellence is symmetric
  parity -- auditing one role tells you the format for all others.

- C-23 -- Full-phase type coverage: all 4 phases have typed output contracts, not just
  the 2-phase minimum C-15 required. A phase without a typed contract is incomplete.

- C-24 -- Terminal checklist quality: checklist items operate at field level (each named
  field independently verifiable) rather than phase level (phase artifact present, roughly
  complete). Field-level items are mechanically auditable; phase-level items are judgment
  calls.

R3 V-05 was the full-stack combination that covered C-01 through C-16. R6 variations
build on that baseline, isolating each refinement before combining.

---

## V-01 -- Axis: Prohibition-count parity (C-22 maximum)

**Hypothesis**: Equal prohibition count per role (5 per role, numbered, stated
explicitly) makes audit deterministic. A scorer checking C-22 does not need to count
per-role -- they verify the symmetric structure once and trust it applies uniformly.
R3 V-01 achieved C-14 with 5 prohibitions per role, but did not declare the parity
rule as a design constraint. V-01 tests whether making the symmetry explicit -- "each
role carries exactly 5 forbidden actions, no more, no fewer" -- produces a
mechanically auditable output where any deviation from parity is a visible defect.
The rest of the prompt stays minimal to isolate this axis: no typed contracts, no
field-level checklist.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Four phases run in order. Do not proceed to the next phase until
the current phase artifact is written.

---

## Prohibition Parity Rule

Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no
fewer. This count is fixed by design. The symmetry makes compliance auditable: a
role with 4 or 6 items has violated the parity contract and is structurally invalid.

---

## Roles

### Registrar (Phase 1 -- topic-new)

Produces strategy.md. Owns topic registration.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content across sources
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not defined in the strategy planned_signals field

### Planner (Phase 2 -- topic-plan)

Produces roadmap.md. Owns per-namespace signal map.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify the topic identity (Phase 1 domain)
2. Must not query or report on which signals have been collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs from Phase 4 vocabulary
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)

Produces status.md. Owns coverage table and readiness verdict.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond what Phase 2 roadmap defines
2. Must not produce verdict verbs from Phase 4 controlled vocabulary
3. Must not interpret meaning from signal content or editorialize on findings
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "a few", "many") where integers are required

### Narrator (Phase 4 -- topic-story)

Produces story.md. Owns verdict and narrative synthesis.

Forbidden actions (exactly 5):
1. Must not modify the coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

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

Gate: Do not proceed to Phase 4 until status.md is present with all 9 namespace
rows and readiness verdict assigned.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

Invoke topic-story for {{topic}}.

Produce story.md:
- Verdict verb: CONFIRMED / REFUTED / EVOLVING / INSUFFICIENT / NOT YET REACHED
- Hypothesis mutation block: S0 (original hypothesis), current form, or "UNCHANGED"
- Echo entries (unexpected findings); if none: "NONE"
- Top-3 next-signal recommendations: namespace + skill + gap reason each

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

Phase 1 (Registrar): Create strategy.md normally. This is the founding artifact.
Phase 2 (Planner): Create roadmap.md normally. All signals remain in planned state.
Phase 3 (Analyst): All 9 namespace rows show Collected = 0. All planned signals
  appear in Missing column by name. Readiness verdict = NOT READY.
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

**Rubric targeting**: C-01 (four phases in order), C-02 (strategy.md with >= 3 signals,
namespace, priority), C-03 (9-namespace coverage table with named gaps), C-04 (verdict
verb + S0 mutation block), C-05 (empty-state per phase), C-06 (top-3 recommendations),
C-07 (coverage ratio + readiness label), C-08 (zero-signal namespaces flagged), C-09
(echo with NONE fallback), C-11 (four role labels), C-12 (explicit gate per phase), C-13
(empty-state as dedicated section), C-14 (prohibitions per role), C-22 (parity rule
declared explicitly: exactly 5 per role, "no more, no fewer", structural invalidity of
deviations called out).
**Misses**: C-15 (no typed contracts), C-16 (no terminal checklist), C-23 (typed
contracts absent -- full-phase coverage not applicable), C-24 (no field-level checklist).
**Risk**: Parity declaration is explicit but a model that generates prohibition lists from
the parity rule forward may produce formulaic lists that satisfy count but not substance.
Forbidding "paraphrasing verdict verbs" in Narrator is the sharpest prohibition; the
weakest is Registrar's prohibition 5 (not listing unlisted signals -- trivially satisfied).

---

## V-02 -- Axis: Full-phase type coverage (C-23 maximum)

**Hypothesis**: Requiring typed output contracts for all four phases -- with an explicit
declaration that no phase is exempt -- produces a stronger structural guarantee than the
C-15 two-phase minimum. R3 V-02 typed all four phases in practice, but the criterion
(C-15) only required two, so the contract could degrade to two phases on any run. C-23
raises the standard: all four phases are fully typed and the prompt states this as an
invariant. V-02 tests whether declaring "full-phase type coverage is required -- partial
coverage fails" alongside the typed contracts for all four phases produces outputs that
maintain the four-phase structure under varying inputs, including edge cases where a model
might compress or skip phases.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Four phases run in order. Do not proceed to the next phase until
the current phase artifact is written.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. Partial coverage -- typing two phases
and leaving others unspecified -- is not acceptable. A phase without a typed
contract is an incomplete phase. Every field in every artifact must conform to its
declared type.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md

- topic_name: string (non-empty, human-readable label)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item:
  - signal_name: string (unique within strategy)
  - target_skill: string (namespace/skill format, e.g. "scout/scout-competitors")
  - rationale: string (one sentence max)

Partial contract (2 of 4 fields present) fails Phase 1.

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries covering planned signals; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list, each item:
    - signal_name: string (must match a signal_name from strategy.md)
    - collection_purpose: string (one sentence: why this signal is necessary)

Empty list fails Phase 2. Entries without collection_purpose fail Phase 2.

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0 (not a range, not prose)
  - collected: integer >= 0 (not a range, not prose)
  - missing: list of strings (signal names explicitly; empty list [] if none missing)
  - zero_flag: string "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N" (both X and N are integers)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

Fewer than 9 rows fails Phase 3. Prose counts in integer fields fail Phase 3.

### Phase 4 Contract -- story.md

- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal string "UNCHANGED")
- echoes: list of strings; if no unexpected findings, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

Absent echoes field fails Phase 4. Paraphrased verdict_verb fails Phase 4.

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

Produce strategy.md conforming to Phase 1 Contract. All fields required. priority
must be exactly one of three tokens. planned_signals must contain >= 3 entries.

Gate: Do not proceed to Phase 2 until strategy.md satisfies Phase 1 Contract.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract. Each signal entry requires
signal_name (matched to strategy.md) and collection_purpose.

Gate: Do not proceed to Phase 3 until roadmap.md satisfies Phase 2 Contract.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract. All 9 namespace rows required.
planned and collected must be integers -- not ranges, not prose. missing must name
each signal explicitly. zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0.

Gate: Do not proceed to Phase 4 until status.md satisfies Phase 3 Contract.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract. verdict_verb must be exactly one of
the five enumerated tokens. echoes list must contain at least "NONE".
next_signal_recommendations must contain exactly 3 items.

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases still run and produce their full artifacts per typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract normally.
Phase 2 (Planner): Create roadmap.md per Phase 2 Contract normally.
Phase 3 (Analyst): collected = 0 (integer) for all rows. missing lists each
  planned signal by signal_name. zero_flag = "NO SIGNALS" where applicable.
  readiness_verdict = "NOT READY".
Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. top 3 recommendations from roadmap.md by priority.

---

## Output: Topic Dashboard

At completion, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
```

**Rubric targeting**: C-01 (four phases in order), C-02 (strategy.md -- typed namespace
token, priority token, >= 3 signals), C-03 (9-namespace table -- integer cells, named
missing as string lists), C-04 (verdict_verb enumerated + mutation s0/current), C-05
(empty-state with typed field values for all phases), C-06 (top-3 recommendations typed),
C-07 (coverage_ratio "X/N" + readiness_verdict enumerated), C-08 (zero_flag typed),
C-09 (echoes minimum ["NONE"]), C-11 (four role labels), C-12 (gate per phase), C-13
(empty-state as dedicated section), C-15 (typed contracts per phase), C-23 (all four
phases typed -- full-phase coverage rule declared explicitly as invariant; partial
coverage called out as a failure mode).
**Misses**: C-14 (roles listed without prohibition lists), C-16 (no terminal checklist),
C-22 (no prohibition count declared), C-24 (no field-level checklist).
**Risk**: The "partial coverage fails" declaration reinforces C-23 but may produce a
model that satisfies the contract structure mechanically without verifying constraint
violations (e.g., prose where integer is required). The Phase 3 enforcement note
("prose counts in integer fields fail") provides some protection. Explicit fail
conditions per contract are the primary defense.

---

## V-03 -- Axis: Terminal checklist quality (C-24 maximum)

**Hypothesis**: A field-level terminal checklist -- each named field independently
verifiable, not a phase-level summary -- is mechanically auditable in a way that
phase-level postconditions are not. R3 V-03 had phase-level postconditions (e.g.,
"strategy.md written AND contains topic name, namespace, priority, and >= 3 planned
signals"). C-24 raises the bar to field granularity: each field in each artifact gets
its own named check with the specific type or value constraint it must satisfy. A
scorer can audit the checklist by reading the artifact and ticking each item without
any judgment. V-03 tests whether this field-level decomposition produces outputs that
better satisfy terminal conditions than phase-summary postconditions.

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

Gate: Do not proceed to Phase 2 until strategy.md is present with all required fields.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

Invoke topic-plan for {{topic}}.

Produce roadmap.md:
- Per-namespace signal map with namespace, planned signals, and collection purpose
  per signal

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

Gate: Do not proceed to Phase 4 until status.md is present with all 9 rows and
readiness verdict assigned.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

Invoke topic-story for {{topic}}.

Produce story.md:
- Verdict verb: CONFIRMED / REFUTED / EVOLVING / INSUFFICIENT / NOT YET REACHED
- Hypothesis mutation block: S0 (original hypothesis), current form, or "UNCHANGED"
- Echo entries (unexpected findings); if none: "NONE"
- Top-3 next-signal recommendations: namespace + skill + gap reason each

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

Phase 1 (Registrar): Create strategy.md normally. This is the founding artifact.
Phase 2 (Planner): Create roadmap.md normally. All signals are in planned state.
Phase 3 (Analyst): All rows show Collected = 0. All planned signals appear in
  Missing by name. Readiness = NOT READY. story.md must be written even with no
  collected signals.
Phase 4 (Narrator): Verdict = NOT YET REACHED. S0 unchanged. Echo = NONE.

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently before marking the campaign complete. Each item
is a named field check. A failed item triggers a targeted re-run of the affected
phase -- not a full campaign restart.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty, not a path or numeric value
    FAIL action: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL action: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low} -- no other values accepted
    FAIL action: re-run Phase 1

[ ] planned_signals: list with count >= 3 (integer count, not "several")
    FAIL action: re-run Phase 1

[ ] planned_signals[*].target_skill: each entry is in namespace/skill format
    FAIL action: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_entries: at least one namespace entry present (not empty list)
    FAIL action: re-run Phase 2

[ ] namespace_entries[*].collection_purpose: string present per signal (not omitted)
    FAIL action: re-run Phase 2

### Phase 3 -- status.md

[ ] namespace row count: exactly 9 rows present (not 8, not 10)
    FAIL action: re-run Phase 3

[ ] planned: integer value in all 9 rows (no prose, no ranges)
    FAIL action: re-run Phase 3

[ ] collected: integer value in all 9 rows (no prose, no ranges)
    FAIL action: re-run Phase 3

[ ] missing: list of signal names (not "3 signals missing" -- names required)
    FAIL action: re-run Phase 3

[ ] zero_flag: "NO SIGNALS" present for every row where planned = 0 AND collected = 0
    FAIL action: re-run Phase 3

[ ] coverage_ratio: string in "X/N" format (both X and N are integers)
    FAIL action: re-run Phase 3

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL action: re-run Phase 3

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL action: re-run Phase 4

[ ] hypothesis_mutation.s0: string present (original hypothesis text, non-empty)
    FAIL action: re-run Phase 4

[ ] hypothesis_mutation.current: string present ("UNCHANGED" or updated hypothesis)
    FAIL action: re-run Phase 4

[ ] echoes: list present; must contain at least one entry (minimum ["NONE"])
    FAIL action: re-run Phase 4

[ ] next_signal_recommendations: exactly 3 items (not 2, not 4)
    FAIL action: re-run Phase 4

[ ] next_signal_recommendations[*].namespace: string present for all 3 items
    FAIL action: re-run Phase 4

[ ] next_signal_recommendations[*].gap_reason: string present for all 3 items
    FAIL action: re-run Phase 4

All items PASS: campaign is complete and dashboard is ready to emit.
Any item FAIL: re-run the affected phase, then re-verify the failed item only.

---

## Output: Topic Dashboard

When all TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
```

**Rubric targeting**: C-01 (four phases in order), C-02 (strategy.md fields listed in
checklist), C-03 (9-namespace table -- named missing signals verified by checklist item),
C-04 (verdict_verb + s0 mutation each get dedicated checklist items), C-05 (empty-state
as dedicated section), C-06 (top-3 recommendations -- count verified as exactly 3 by
checklist), C-07 (coverage_ratio format + readiness_verdict each verified by checklist),
C-08 (zero_flag verified per namespace), C-09 (echoes list with minimum ["NONE"]
verified), C-11 (four role labels), C-12 (explicit gate per phase), C-13 (empty-state
section), C-16 (terminal checklist present), C-24 (field-level checklist: 22 individual
items each naming a specific artifact field with its type/value constraint and FAIL
action, independently verifiable without judgment).
**Misses**: C-14 (no prohibition lists), C-15 (no typed contracts in phase definitions),
C-22 (no prohibition count), C-23 (phases not declared typed).
**Risk**: 22 checklist items is long. A model may read the TERMINAL section as a summary
to emit rather than conditions to verify -- producing a dashboard and a checklist showing
all PASS without actually checking. The FAIL action per item adds structural authenticity
but cannot prevent nominal compliance. Field-level granularity is the main strength
(each item is specific) and the main risk (specificity may be skipped if treated as
boilerplate).

---

## V-04 -- Combined Axes: Prohibition-count parity + Full-phase type coverage (C-22 + C-23)

**Hypothesis**: Prohibition-count parity (C-22) and full-phase type coverage (C-23) are
orthogonal constraints. Parity controls behavioral structure: a model generating role
descriptions knows exactly how many prohibited actions to name, and can be audited by
count alone. Full-phase typing controls artifact structure: no phase produces an
untyped output, and partial coverage is declared invalid. These two axes address
different failure modes -- role bleed and artifact ambiguity -- and combining them
should not introduce conflict. V-04 tests whether the combination reaches C-22 + C-23
coverage simultaneously without requiring a field-level checklist (C-24).

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Four phases run in order. Do not proceed to the next phase until
the current phase artifact is written.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. Partial coverage -- typing fewer than
four phases -- is not acceptable and produces an incomplete campaign artifact. Each
field declared below is binding: integer means integer, enumerated string means
exactly one of the listed tokens.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md

- topic_name: string (non-empty)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item:
  - signal_name: string
  - target_skill: string (namespace/skill format)
  - rationale: string (one sentence)

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string
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
  - s0: string (original hypothesis)
  - current: string (updated hypothesis or literal "UNCHANGED")
- echoes: list of strings; if none, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

---

## Prohibition Parity Rule

Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no
fewer. Roles are listed in phase order. A role with fewer than 5 items or more than
5 items is structurally invalid.

---

## Roles

### Registrar (Phase 1 -- topic-new)

Produces strategy.md per Phase 1 Contract.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, ratios, or readiness verdicts
2. Must not synthesize or interpret signal content across sources
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not present in the strategy planned_signals field

### Planner (Phase 2 -- topic-plan)

Produces roadmap.md per Phase 2 Contract.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify the topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)

Produces status.md per Phase 3 Contract.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond what Phase 2 roadmap defines
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "many") where integers are required

### Narrator (Phase 4 -- topic-story)

Produces story.md per Phase 4 Contract.

Forbidden actions (exactly 5):
1. Must not modify the coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply.*

Invoke topic-new for {{topic}}.

Produce strategy.md per Phase 1 Contract. All fields required.

Gate: Do not proceed to Phase 2 until strategy.md satisfies Phase 1 Contract.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md per Phase 2 Contract. Include collection_purpose per signal.

Gate: Do not proceed to Phase 3 until roadmap.md satisfies Phase 2 Contract.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply.*

Invoke topic-status for {{topic}}.

Produce status.md per Phase 3 Contract. All 9 rows required. Integer fields must
be integers. Missing must name signals, not count them.

Gate: Do not proceed to Phase 4 until status.md satisfies Phase 3 Contract.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply.*

Invoke topic-story for {{topic}}.

Produce story.md per Phase 4 Contract. verdict_verb must be an exact token.
echoes must contain at least "NONE". next_signal_recommendations: exactly 3 items.

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract normally.
Phase 2 (Planner): Create roadmap.md per Phase 2 Contract normally.
Phase 3 (Analyst): collected = 0 (integer) for all rows. missing names all planned
  signals. zero_flag = "NO SIGNALS" where applicable. readiness_verdict = "NOT READY".
Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". current = "UNCHANGED".
  echoes = ["NONE"]. top 3 next signals from roadmap.md.

---

## Output: Topic Dashboard

At completion, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
```

**Rubric targeting**: C-01 (four phases in order), C-02 (strategy.md -- typed namespace,
priority, >= 3 signals), C-03 (9-namespace table -- integer cells, named missing lists),
C-04 (verdict_verb enumerated + mutation s0/current), C-05 (empty-state typed per phase),
C-06 (top-3 typed), C-07 (coverage_ratio "X/N" + readiness_verdict enumerated), C-08
(zero_flag typed), C-09 (echoes ["NONE"]), C-11 (four role labels), C-12 (gate per phase
with active-role annotation), C-13 (empty-state as dedicated section), C-14 (prohibition
lists per role), C-15 (typed contracts per phase), C-22 (parity rule declared: exactly 5
per role, structural invalidity of deviations stated, active-role annotation repeats the
count), C-23 (full-phase type coverage rule declared: partial coverage invalid,
all 4 phases have contracts).
**Misses**: C-16 (no terminal checklist), C-24 (no field-level checklist).
**Risk**: This is the longest single-combination variation and may cause a model to
apply the prohibition parity rule and the typed contracts independently without
integrating them -- producing roles that list 5 items but whose items do not match
the contract they govern. The active-role annotation ("Analyst active. Exactly 5
forbidden actions apply.") is designed to keep the prohibition count salient at the
point of execution, not just in the Roles section.

---

## V-05 -- Full Stack: Prohibition-count parity + Full-phase type coverage + Field-level checklist + Lifecycle emphasis

**Combined axes**: Prohibition-count parity (C-22) + Full-phase type coverage (C-23)
+ Field-level terminal checklist (C-24) + Lifecycle emphasis (each phase structured
as a named major section with active role annotation, postcondition, and gate)

**Hypothesis**: All three new refinements target independent failure modes:
- C-22 (parity rule) ensures audit is deterministic by count alone
- C-23 (full-phase coverage) ensures every artifact has declared type constraints
- C-24 (field-level checklist) makes terminal verification mechanical, not judgment-based
- Lifecycle emphasis ensures the campaign structure is legible to a model that might
  compress phases: each phase opens with its active role and closes with a gate that
  references the typed contract

Combined, these axes should produce the most verifiable, gate-complete campaign prompt
in any R6 variation. The field-level checklist is the primary defense against nominal
compliance: a model can claim completion without verifying; the checklist forces explicit
per-field confirmation with named FAIL actions.

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

Owns status.md. Produces Phase 3 Contract output.

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

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present -- no row skipped
- planned and collected are integers -- narrative counts fail
- missing lists each signal by name -- counts alone fail
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Phase 3 postcondition: status.md present, 9 rows with integer fields, readiness_verdict
assigned from enumerated set.

GATE: Do not proceed to Phase 4 until Phase 3 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (no paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Phase 4 postcondition: story.md present with verdict_verb from 5-token set, s0
field, echoes list, and 3-item recommendations.

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. planned_signals must
  list >= 3 entries. This is the founding artifact.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals are planned;
  none are collected. roadmap.md documents what will be collected.

Phase 3 (Analyst): All rows have collected = 0 (integer). missing lists all planned
  signals from roadmap.md by signal_name. zero_flag = "NO SIGNALS" for namespaces
  where planned = 0 AND collected = 0. readiness_verdict = "NOT READY".

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. next_signal_recommendations: top 3 signals from
  roadmap.md ordered by planned priority.

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

All 22 items PASS: campaign is complete. Dashboard ready to emit.
Any item FAIL: re-run the affected phase. Re-verify the failed item only.

---

## Output: Topic Dashboard

When all 22 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
```

**Rubric targeting**: C-01 (four phases in order with explicit structure and active-role
annotation), C-02 (strategy.md -- typed namespace token + priority token + >= 3 signals),
C-03 (9-namespace table -- integer cells, named missing lists), C-04 (verdict_verb
enumerated + mutation s0/current), C-05 (empty-state as dedicated section with per-phase
typed behavior), C-06 (top-3 recommendations with namespace + skill + gap_reason), C-07
(coverage_ratio "X/N" + readiness_verdict enumerated), C-08 (zero_flag typed), C-09
(echoes list minimum ["NONE"]), C-11 (four role labels, consistent active-role
annotation throughout phases), C-12 (explicit GATE per phase with postcondition
reference), C-13 (empty-state as dedicated section with per-phase behavior for all 4
phases), C-14 (prohibition lists per role, numbered 1-5), C-15 (typed contracts per
phase, all 4 phases), C-16 (TERMINAL section with per-phase PASS conditions and re-run
instructions), C-22 (parity rule declared: exactly 5 per role, structural invalidity
of deviations stated, active-role annotation reinforces count at point of execution),
C-23 (full-phase type coverage rule declared at top level: no phase exempt, partial
coverage explicitly fails), C-24 (22 individual field-level checklist items, each naming
a specific artifact field with its type or value constraint and a targeted FAIL action;
total count stated at the end: "All 22 items PASS").
**Risk**: This is the most complex variation. Three structural rules (parity,
full-phase coverage, field-level checklist) each add length independently. A model
that treats any of the three as boilerplate and fills fields nominally may pass
formally without satisfying the intent. The active-role annotation ("Narrator active.
Exactly 5 forbidden actions apply. Phase 4 Contract governs output.") keeps all three
rules salient at the point of execution, not only in their declaration sections. The
field-level checklist count (22 items) is the primary defense against nominal
compliance -- a model must produce 22 PASS/FAIL verdicts, not a single "all done"
statement.

---

## Variation Summary

| ID  | Primary Axes                                 | New Criteria Targeted   | Criteria Covered | Key Risk                                       |
|-----|----------------------------------------------|-------------------------|------------------|------------------------------------------------|
| V-01 | Prohibition-count parity                   | C-22                    | C-01..C-14, C-22 | Formulaic lists satisfying count but not substance |
| V-02 | Full-phase type coverage                   | C-23                    | C-01..C-13, C-15, C-23 | Model types 4 phases mechanically without verifying constraints |
| V-03 | Field-level terminal checklist             | C-24                    | C-01..C-13, C-16, C-24 | 22-item checklist treated as boilerplate output, not verification |
| V-04 | Prohibition parity + full-phase typing     | C-22 + C-23             | C-01..C-15, C-22, C-23 | Rules applied independently; parity lists don't match contracts |
| V-05 | Parity + full-phase typing + field checklist | C-22 + C-23 + C-24    | C-01..C-16, C-22..C-24 | Length complexity; three structural rules each risk nominal compliance |

**Predicted leaderboard going into quest-score**: V-05 > V-04 > V-03 > V-01 >= V-02.

V-05 is the only variation covering all 19 criteria (C-01 through C-16, C-22, C-23,
C-24). V-04 reaches 17/19 with the strongest dual enforcement on C-22 and C-23.
V-03 reaches 16/19 with the field-level checklist as the primary new contribution;
it misses C-22, C-23 but the checklist quality advantage over R3 V-03 should show in
scoring. V-01 covers C-22 but misses C-23 and C-24; V-02 covers C-23 but misses C-22
and C-24.

The key open question for scoring: does C-24 require the full 22-item count, or is a
partial field-level checklist sufficient? V-03 and V-05 both aim for exhaustive
coverage. Whether a model producing V-03's prompt generates all 22 items or compresses
to phase-level will determine whether V-03 outscores V-01 or ties it.
