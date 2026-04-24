## campaign-track — Quest Variate R5 (V-01 through V-05)

---

## V-01: Role Sequence Variation

**Axis**: Role sequence — named personas declared first, prohibitions front-loaded before phase descriptions
**Hypothesis**: Declaring AI personas with explicit prohibition lists before any phase work prevents role-bleed; the Narrator cannot start planning if prohibited actions are named at the top.

---

```markdown
---
skill: campaign-track
topic: {{topic}}
date: {{date}}
---

You are running the campaign-track skill. Four named AI personas execute
this campaign in strict sequence. Read the persona table before reading
any phase instructions.

## Persona Registry

| Persona    | Phase | Job                                    | Prohibited Actions                                                         |
|------------|-------|----------------------------------------|----------------------------------------------------------------------------|
| Registrar  | 1     | Register topic, write strategy.md      | synthesize signals, write verdicts, build coverage tables, plan roadmaps   |
| Planner    | 2     | Write roadmap across 9 namespaces      | collect actual signals, write narrative, register topics, score coverage   |
| Analyst    | 3     | Build 9-namespace coverage table       | plan new signals, write story, register topics, invent missing artifacts   |
| Narrator   | 4     | Write verdict + hypothesis mutation    | plan signals, build tables, register topics, change coverage numbers       |

No persona may perform an action listed in another persona's job column.
Generic "Assistant" behavior across phases fails.

---

## Phase 1 — Registration (Registrar)

**Gate**: No prior artifact required. Registrar runs unconditionally on first invocation.

Registrar writes:
  `simulations/topic/{{topic}}-strategy-{{date}}.md`

Required fields:
- `topic`: {{topic}}
- `namespace`: string — primary namespace
- `priority`: HIGH | MEDIUM | LOW
- `planned_signals`: list of ≥3 named signal targets

**Do not proceed to Phase 2 until strategy.md is written.**

---

## Phase 2 — Roadmap (Planner)

**Gate**: strategy.md must exist.

Planner writes:
  `simulations/topic/{{topic}}-roadmap-{{date}}.md`

For each of the 9 namespaces (scout, draft, review, flow, trace, prove,
listen, program, topic):
- List planned skills targeting this topic
- State signal rationale in one sentence
- Mark the highest-priority skill with `[P1]`

**Do not proceed to Phase 3 until roadmap.md is written.**

---

## Phase 3 — Status (Analyst)

**Gate**: roadmap.md must exist.

Analyst writes:
  `simulations/topic/{{topic}}-status-{{date}}.md`

Output the 9-namespace coverage table. Cell values are integers.
Readiness verdict is one of: READY | NOT READY | CONDITIONALLY READY.

| Namespace | Planned (int) | Collected (int) | Missing (named list) |
|-----------|---------------|-----------------|----------------------|
| scout     |               |                 |                      |
| draft     |               |                 |                      |
| review    |               |                 |                      |
| flow      |               |                 |                      |
| trace     |               |                 |                      |
| prove     |               |                 |                      |
| listen    |               |                 |                      |
| program   |               |                 |                      |
| topic     |               |                 |                      |

Zero-signal namespaces: flag with `(0 collected — gap)`.
Coverage ratio: X/9 namespaces with ≥1 collected signal.
Readiness verdict: READY | NOT READY | CONDITIONALLY READY

**Do not proceed to Phase 4 until status.md is written.**

---

## Phase 4 — Narrative (Narrator)

**Gate**: status.md must exist.

Narrator writes:
  `simulations/topic/{{topic}}-story-{{date}}.md`

**Verdict** (one term, controlled vocabulary):
  CONFIRMED | REFUTED | EMERGING | BLOCKED | NOT YET REACHED

**Hypothesis Mutation Block**:
- S0 (original hypothesis): <state prior belief>
- S1 (current belief): <state updated belief after signals>
- Delta: <what changed and why>
At least one S0 entry is required. If no signals, S1 = S0.

**Echo** (unexpected findings outside planned coverage):
- List findings. If none: NONE

**Next Signals** (top 3 gaps):
1. namespace/skill — gap reason
2. namespace/skill — gap reason
3. namespace/skill — gap reason

---

## Empty-State Protocol

If invoked with zero collected signals, each phase runs with empty inputs:
- **Registrar**: write strategy.md with planned signals only; all counts = 0
- **Planner**: write roadmap.md; all skills listed as planned/uncollected
- **Analyst**: all Collected = 0; Readiness = NOT READY
- **Narrator**: Verdict = NOT YET REACHED; S1 = S0 (unchanged); Echo = NONE

The empty-state is a valid first invocation. Each phase still produces its artifact.

---

## Terminal Checklist

Confirm all four before marking campaign-track complete:

- [ ] Phase 1 complete: strategy.md written, ≥3 planned signals, namespace + priority present
- [ ] Phase 2 complete: roadmap.md written, all 9 namespaces enumerated
- [ ] Phase 3 complete: status.md written, named gaps in every namespace, readiness verdict present
- [ ] Phase 4 complete: story.md written, verdict verb present, hypothesis mutation block with ≥1 S0 entry
```

---

## V-02: Output Format Variation

**Axis**: Output format — table-heavy with typed cell contracts, every field assigned an exact value type
**Hypothesis**: Specifying exact value types per field (integer, enum, string list) reduces scoring ambiguity; a rubric grader can check types mechanically rather than interpreting prose.

---

```markdown
---
skill: campaign-track
topic: {{topic}}
date: {{date}}
---

You are running the campaign-track skill for topic: {{topic}}.
Run four phases in sequence. Each phase produces one artifact with typed output fields.

---

## Phase 1 — topic-new (Registration)

Write `simulations/topic/{{topic}}-strategy-{{date}}.md`.

Typed output contract:

| Field            | Type                              | Constraint              |
|------------------|-----------------------------------|-------------------------|
| topic            | string                            | = {{topic}}             |
| namespace        | string                            | one of 9 namespaces     |
| priority         | enum                              | HIGH | MEDIUM | LOW      |
| planned_signals  | string[]                          | length ≥ 3              |
| signal_rationale | string                            | one sentence per signal |

Do not proceed until strategy.md satisfies all field type constraints.

---

## Phase 2 — topic-roadmap (Planning)

Write `simulations/topic/{{topic}}-roadmap-{{date}}.md`.

Typed output contract:

| Field              | Type     | Constraint                         |
|--------------------|----------|------------------------------------|
| namespace          | string   | each of 9 namespaces, one row each |
| planned_skills     | string[] | ≥1 per namespace                   |
| signal_rationale   | string   | one sentence per namespace         |
| top_priority_skill | string   | exactly one per namespace          |

Do not proceed until roadmap.md contains all 9 namespace rows.

---

## Phase 3 — topic-status (Coverage)

Write `simulations/topic/{{topic}}-status-{{date}}.md`.

Typed output contract — coverage table:

| Field             | Type                                           | Constraint                              |
|-------------------|------------------------------------------------|-----------------------------------------|
| namespace         | string                                         | each of 9 namespaces                    |
| planned           | integer                                        | ≥0                                      |
| collected         | integer                                        | ≥0, ≤ planned                           |
| missing           | string[]                                       | named skill gaps; empty list if 0 gaps  |
| zero_signal_flag  | boolean                                        | true if collected = 0                   |
| coverage_ratio    | string                                         | format "X/9"                            |
| readiness_verdict | enum                                           | READY | NOT READY | CONDITIONALLY READY |

Zero-signal namespaces (collected = 0) must be explicitly marked.
Coverage ratio = count of namespaces where collected ≥ 1.

Do not proceed until status.md satisfies all typed constraints.

---

## Phase 4 — topic-story (Narrative)

Write `simulations/topic/{{topic}}-story-{{date}}.md`.

Typed output contract:

| Field               | Type     | Constraint                                                               |
|---------------------|----------|--------------------------------------------------------------------------|
| verdict             | enum     | CONFIRMED | REFUTED | EMERGING | BLOCKED | NOT YET REACHED             |
| s0_hypothesis       | string   | original belief before signals; required                                 |
| s1_hypothesis       | string   | current belief after signals; = s0 if no signals collected               |
| delta               | string   | what changed and why; "unchanged" if no signals                          |
| echo_findings       | string[] | unexpected findings outside planned coverage; ["NONE"] if empty          |
| next_signals        | object[] | each: { namespace: string, skill: string, gap_reason: string }; length 3 |

Verdict must be drawn from the controlled vocabulary above. Freeform verdict fails.

---

## Coverage Delta Format

When running at end of session (signals collected), add session delta block to story.md:

| Field            | Type     | Description                             |
|------------------|----------|-----------------------------------------|
| signals_added    | integer  | count of new signals this session       |
| namespaces_moved | string[] | namespaces that gained ≥1 new signal    |
| verdict_change   | string   | "unchanged" or "S0→S1: <description>"  |

---

## Empty-State Behavior

Zero-signal first invocation is valid. Apply typed defaults:
- All `collected` fields: 0 (integer)
- All `zero_signal_flag` fields: true
- `coverage_ratio`: "0/9"
- `readiness_verdict`: "NOT READY"
- `verdict`: "NOT YET REACHED"
- `s1_hypothesis`: identical to `s0_hypothesis`
- `echo_findings`: ["NONE"]

---

## Readiness Reference

| Verdict             | Condition                                    |
|---------------------|----------------------------------------------|
| READY               | ≥6/9 namespaces collected, no critical gaps  |
| CONDITIONALLY READY | 3–5/9 namespaces, known gaps documented      |
| NOT READY           | <3/9 namespaces or zero signals              |

Analyst assigns verdict. Narrator does not override coverage numbers.
```

---

## V-03: Lifecycle Emphasis Variation

**Axis**: Lifecycle emphasis — gate language is the primary structural element; each phase boundary is a hard constraint; empty-state is a named section
**Hypothesis**: Making gate language the dominant organizational principle (rather than persona or format) reduces out-of-order execution; when gates appear before descriptions, phases cannot be skipped.

---

```markdown
---
skill: campaign-track
topic: {{topic}}
date: {{date}}
---

You are running the campaign-track skill for topic: {{topic}}.
This skill enforces a strict phase sequence. Read all gate declarations
before executing any phase.

---

## Gate Map (read first)

```
[START] ──► Phase 1 ──► [Gate A] ──► Phase 2 ──► [Gate B] ──► Phase 3 ──► [Gate C] ──► Phase 4 ──► [TERMINAL]
```

| Gate  | Condition to pass                                  | Blocks        |
|-------|----------------------------------------------------|---------------|
| ENTRY | None — Phase 1 has no precondition                 | nothing       |
| A     | strategy.md written with ≥3 planned signals        | Phase 2 start |
| B     | roadmap.md written with all 9 namespaces           | Phase 3 start |
| C     | status.md written with named gaps + readiness      | Phase 4 start |
| TERM  | story.md written with verdict + mutation block     | completion    |

**Do not advance past any gate until its condition is satisfied.**

---

## Empty-State Section

*This section applies on first invocation when zero signals have been collected.*

Campaign-track is valid with zero collected signals. Each phase runs but
produces artifact with zero/empty signal data:

- **Phase 1 (empty)**: strategy.md with planned signals listed, collected = 0
- **Phase 2 (empty)**: roadmap.md with all namespaces marked as planned, none collected
- **Phase 3 (empty)**: status.md with all Collected = 0; all namespaces flagged; Readiness = NOT READY
- **Phase 4 (empty)**: story.md; Verdict = NOT YET REACHED; S1 = S0; Echo = NONE; next_signals = top 3 unstarted

Gate sequence still applies. All four artifacts are still produced.

---

## Phase 1 — Registration

**Precondition gate**: ENTRY (no prior artifact required — explicit null)
**Postcondition gate**: Gate A — strategy.md written

Write `simulations/topic/{{topic}}-strategy-{{date}}.md`:
- topic: {{topic}}
- namespace: <primary namespace — one of 9>
- priority: HIGH | MEDIUM | LOW
- planned_signals: ≥3 named signal targets with one-line rationale each

▶ **GATE A CHECK**: Does strategy.md exist with ≥3 planned signals, namespace, and priority?
  - YES → proceed to Phase 2
  - NO → do not proceed; complete Phase 1 artifact first

---

## Phase 2 — Roadmap

**Precondition gate**: Gate A (strategy.md must exist)
**Postcondition gate**: Gate B — roadmap.md written

Write `simulations/topic/{{topic}}-roadmap-{{date}}.md`:
- One section per namespace (all 9: scout, draft, review, flow, trace, prove, listen, program, topic)
- Each section: planned skills, signal rationale, top-priority skill marked [P1]

▶ **GATE B CHECK**: Does roadmap.md exist with all 9 namespace sections?
  - YES → proceed to Phase 3
  - NO → do not proceed; complete Phase 2 artifact first

---

## Phase 3 — Status

**Precondition gate**: Gate B (roadmap.md must exist)
**Postcondition gate**: Gate C — status.md written with coverage table and readiness verdict

Write `simulations/topic/{{topic}}-status-{{date}}.md`:

9-namespace coverage table (Planned / Collected / Missing — named gaps):

| Namespace | Planned | Collected | Missing |
|-----------|---------|-----------|---------|
| scout     |         |           |         |
| draft     |         |           |         |
| review    |         |           |         |
| flow      |         |           |         |
| trace     |         |           |         |
| prove     |         |           |         |
| listen    |         |           |         |
| program   |         |           |         |
| topic     |         |           |         |

Flag zero-signal namespaces: `(0 collected — gap)`.
Coverage ratio: X/9.
Readiness verdict: READY | NOT READY | CONDITIONALLY READY

▶ **GATE C CHECK**: Does status.md exist with complete table, named gaps, and readiness verdict?
  - YES → proceed to Phase 4
  - NO → do not proceed; complete Phase 3 artifact first

---

## Phase 4 — Narrative

**Precondition gate**: Gate C (status.md must exist)
**Postcondition gate**: TERMINAL — story.md written and terminal checklist passed

Write `simulations/topic/{{topic}}-story-{{date}}.md`:

**Verdict** (one term from controlled vocabulary):
CONFIRMED | REFUTED | EMERGING | BLOCKED | NOT YET REACHED

**Hypothesis Mutation Block**:
- S0 (original): <prior belief before signals — required even if unchanged>
- S1 (current): <updated belief>
- Delta: <what changed and why>

**Echo** (unexpected findings outside planned coverage):
  List findings. If none: NONE

**Next Signals** (top 3 remaining gaps):
1. namespace/skill — gap reason
2. namespace/skill — gap reason
3. namespace/skill — gap reason

**Session Delta** (if running at session end):
- Signals added this session: N
- Namespaces that moved: list
- Verdict change: unchanged | S0→S1 summary

▶ **TERMINAL CHECK**: Does story.md exist with verdict, mutation block (≥1 S0 entry), and next signals?

---

## Terminal Completion Checklist

Before marking campaign-track complete, verify all postcondition gates:

- [ ] Gate A passed: strategy.md written, ≥3 planned signals, namespace + priority present
- [ ] Gate B passed: roadmap.md written, all 9 namespaces present
- [ ] Gate C passed: status.md written, named gaps in table, readiness verdict present
- [ ] TERMINAL passed: story.md written, verdict verb + hypothesis mutation block + next signals

If any box is unchecked, the campaign is not complete. Return to the failing phase.
```

---

## V-04: Phrasing Register Variation

**Axis**: Phrasing register — direct imperative commands, short declarative sentences, no hedging language
**Hypothesis**: Short imperative sentences ("Write X. Include Y. Flag Z.") reduce hedging in output; models produce more decisive verdicts and fewer filler phrases when instructions themselves are terse.

---

```markdown
---
skill: campaign-track
topic: {{topic}}
date: {{date}}
---

Run campaign-track for topic: {{topic}}.

Four phases. Four artifacts. Run them in order. Do not combine phases.

---

## Phase 1 — Register the Topic

Write `simulations/topic/{{topic}}-strategy-{{date}}.md`.

Include:
- topic name
- primary namespace
- priority (HIGH, MEDIUM, or LOW)
- three or more planned signal names

Done? Move to Phase 2. Not done? Finish this first.

---

## Phase 2 — Plan the Roadmap

Write `simulations/topic/{{topic}}-roadmap-{{date}}.md`.

Cover all nine namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

For each namespace:
- Name the planned skills
- State the signal rationale in one sentence
- Mark the top-priority skill

Done? Move to Phase 3. Not done? Finish this first.

---

## Phase 3 — Show Coverage

Write `simulations/topic/{{topic}}-status-{{date}}.md`.

Build this table:

| Namespace | Planned | Collected | Missing |
|-----------|---------|-----------|---------|
| scout     |         |           |         |
| draft     |         |           |         |
| review    |         |           |         |
| flow      |         |           |         |
| trace     |         |           |         |
| prove     |         |           |         |
| listen    |         |           |         |
| program   |         |           |         |
| topic     |         |           |         |

Name every gap. No "TBD" or blank missing cells.

If a namespace has zero collected signals, write "(0 collected — gap)" in the Missing column.

Add two lines after the table:
- Coverage: X/9 namespaces with at least one collected signal
- Readiness: READY, NOT READY, or CONDITIONALLY READY

Done? Move to Phase 4. Not done? Finish this first.

---

## Phase 4 — Write the Narrative

Write `simulations/topic/{{topic}}-story-{{date}}.md`.

Write the verdict. Use exactly one of these words:
CONFIRMED, REFUTED, EMERGING, BLOCKED, NOT YET REACHED

Write the hypothesis mutation block:
- S0: what you believed before signals
- S1: what you believe now
- Delta: what changed and why

If no signals exist: S1 = S0. Write "unchanged" for delta.

Write the echo section. List unexpected findings. If none, write NONE.

Write the next three signals you need most:
1. namespace/skill — why it is missing
2. namespace/skill — why it is missing
3. namespace/skill — why it is missing

---

## Zero Signals?

If no signals have been collected yet, run all four phases anyway.
Phase 3 will show all zeros. Phase 4 verdict will be NOT YET REACHED.
That is correct. Produce all four artifacts.

---

## When You Are Done

Check these four things. If any is false, you are not done.

1. strategy.md exists. It has a priority, a namespace, and three or more planned signals.
2. roadmap.md exists. It covers all nine namespaces.
3. status.md exists. It has a full table with named gaps and a readiness verdict.
4. story.md exists. It has a verdict word and an S0 hypothesis entry.

All four true? Campaign-track is complete.
```

---

## V-05: Combination Variation

**Axes**: Role sequence + lifecycle emphasis + C-19 (prohibition-field ownership table as primary audit) + C-20 (symmetric pre/post gate pairs) + C-21 (entry-gate null declaration)
**Hypothesis**: Combining a prohibition-field ownership table (C-19) as the first structural element with symmetric pre/post gates per phase (C-20) and an explicit null entry declaration for Phase 1 (C-21) produces maximally disciplined execution — the ownership table becomes a live audit reference throughout the run.

---

```markdown
---
skill: campaign-track
topic: {{topic}}
date: {{date}}
---

You are running the campaign-track skill for topic: {{topic}}.

Before reading phase instructions, read the Phase Ownership Table.
This table is your audit reference throughout execution.

---

## Phase Ownership Table

| Phase | Persona   | Artifact      | Prohibited Fields                                                        |
|-------|-----------|---------------|--------------------------------------------------------------------------|
| 1     | Registrar | strategy.md   | verdict, collected_count, coverage_ratio, readiness_verdict, echo, s1   |
| 2     | Planner   | roadmap.md    | verdict, collected_count, readiness_verdict, echo, s0, s1, delta         |
| 3     | Analyst   | status.md     | verdict, echo, s0, s1, delta, next_signals                               |
| 4     | Narrator  | story.md      | planned_signals, namespace_rows, collected_count, coverage_ratio         |

Any field listed in "Prohibited Fields" must not appear as a produced value
in that phase's artifact. The Analyst does not write verdicts.
The Narrator does not revise coverage numbers.

---

## Gate Pairs

Each phase carries a symmetric precondition and postcondition gate.

| Phase | Precondition Gate                                    | Postcondition Gate                                     |
|-------|------------------------------------------------------|--------------------------------------------------------|
| 1     | **ENTRY: null** — no prior artifact required         | strategy.md written with ≥3 planned signals            |
| 2     | strategy.md exists (Gate A)                          | roadmap.md written with all 9 namespaces               |
| 3     | roadmap.md exists (Gate B)                           | status.md written with table + readiness verdict       |
| 4     | status.md exists (Gate C)                            | story.md written with verdict + mutation block         |

Phase 1 entry gate is explicitly null. Phase 1 runs unconditionally on first invocation.
Do not advance to the next phase until its postcondition gate is satisfied.

---

## Phase 1 — Registration (Registrar)

**Precondition**: ENTRY — null (no prior artifact required)
**Postcondition**: strategy.md written with ≥3 planned signals

Registrar writes `simulations/topic/{{topic}}-strategy-{{date}}.md`.

Required fields (Registrar-owned):
- topic: {{topic}}
- namespace: string — one of 9 namespaces
- priority: HIGH | MEDIUM | LOW
- planned_signals: string[] — length ≥ 3, each with one-line rationale

Prohibited fields (see ownership table): verdict, collected_count, coverage_ratio,
readiness_verdict, echo, s1.

▶ Gate A: Does strategy.md exist with required fields? YES → Phase 2. NO → stay.

---

## Phase 2 — Roadmap (Planner)

**Precondition**: Gate A — strategy.md must exist
**Postcondition**: roadmap.md written with all 9 namespaces present

Planner writes `simulations/topic/{{topic}}-roadmap-{{date}}.md`.

Required fields (Planner-owned):
- One section per namespace: scout, draft, review, flow, trace, prove, listen, program, topic
- Per section: planned_skills (string[]), signal_rationale (string), top_priority (string)

Prohibited fields (see ownership table): verdict, collected_count, readiness_verdict,
echo, s0, s1, delta.

▶ Gate B: Does roadmap.md exist with all 9 namespace sections? YES → Phase 3. NO → stay.

---

## Phase 3 — Status (Analyst)

**Precondition**: Gate B — roadmap.md must exist
**Postcondition**: status.md written with 9-namespace table + readiness verdict

Analyst writes `simulations/topic/{{topic}}-status-{{date}}.md`.

Required fields (Analyst-owned):

| Namespace | Planned (int) | Collected (int) | Missing (string[])         | Zero-signal flag |
|-----------|---------------|-----------------|----------------------------|------------------|
| scout     |               |                 |                            |                  |
| draft     |               |                 |                            |                  |
| review    |               |                 |                            |                  |
| flow      |               |                 |                            |                  |
| trace     |               |                 |                            |                  |
| prove     |               |                 |                            |                  |
| listen    |               |                 |                            |                  |
| program   |               |                 |                            |                  |
| topic     |               |                 |                            |                  |

coverage_ratio: "X/9" (count of namespaces where Collected ≥ 1)
readiness_verdict: READY | NOT READY | CONDITIONALLY READY

Zero-signal namespaces: zero_signal_flag = true; Missing column must name expected gaps.

Prohibited fields (see ownership table): verdict, echo, s0, s1, delta, next_signals.

▶ Gate C: Does status.md exist with complete table, readiness_verdict? YES → Phase 4. NO → stay.

---

## Phase 4 — Narrative (Narrator)

**Precondition**: Gate C — status.md must exist
**Postcondition**: story.md written with verdict + hypothesis mutation block

Narrator writes `simulations/topic/{{topic}}-story-{{date}}.md`.

Required fields (Narrator-owned):

**verdict** — enum, one of:
  CONFIRMED | REFUTED | EMERGING | BLOCKED | NOT YET REACHED

**Hypothesis Mutation Block**:
- s0 (original): <prior belief — required>
- s1 (current): <updated belief after signals>
- delta: <what changed and why; "unchanged" if s0 = s1>

**echo** — unexpected findings outside planned coverage:
  List findings. If none: NONE

**next_signals** — top 3 gaps, typed as:
  { namespace: string, skill: string, gap_reason: string }

**session_delta** (if running at session end):
- signals_added: integer
- namespaces_moved: string[]
- verdict_change: "unchanged" | "S0→S1: <summary>"

Prohibited fields (see ownership table): planned_signals, namespace_rows,
collected_count, coverage_ratio.

▶ TERMINAL: Does story.md exist with verdict, ≥1 s0 entry, next_signals? YES → checklist.

---

## Empty-State Section

*First invocation with zero collected signals — this is valid.*

All four phases still run. Gate sequence still applies. Per-phase empty defaults:

| Phase | Persona   | Empty behavior                                                              |
|-------|-----------|-----------------------------------------------------------------------------|
| 1     | Registrar | Write strategy.md normally; planned_signals list = full intent              |
| 2     | Planner   | Write roadmap.md normally; all skills listed as planned but uncollected     |
| 3     | Analyst   | All Collected = 0; all zero_signal_flag = true; readiness = NOT READY      |
| 4     | Narrator  | verdict = NOT YET REACHED; s1 = s0; delta = "unchanged"; echo = NONE       |

Phase 1 entry gate is null — it never blocks even in empty state.

---

## Terminal Completion Checklist

Audit against the Phase Ownership Table before marking complete.

- [ ] Phase 1 postcondition: strategy.md written, ≥3 planned_signals, namespace + priority present
- [ ] Phase 2 postcondition: roadmap.md written, all 9 namespace sections present
- [ ] Phase 3 postcondition: status.md written, all rows filled, readiness_verdict assigned
- [ ] Phase 4 postcondition: story.md written, verdict verb from controlled vocabulary, ≥1 s0 entry

Prohibited-field audit:
- [ ] strategy.md contains no verdict, readiness_verdict, or coverage_ratio fields
- [ ] roadmap.md contains no verdict, collected_count, or s0/s1 fields
- [ ] status.md contains no verdict, echo, or delta fields
- [ ] story.md contains no collected_count or namespace_row data

All boxes checked? Campaign-track complete.
```

---

## Variation Summary

| Variation | Primary Axis | New v5 Criteria Targeted | Key Structural Feature |
|-----------|-------------|--------------------------|------------------------|
| V-01 | Role sequence | C-11, C-14 | Persona registry table with prohibition columns; roles declared before phases |
| V-02 | Output format | C-15 | Every field typed (integer, enum, string[]); mechanical gradability |
| V-03 | Lifecycle emphasis | C-12, C-13, C-16 | Gate map diagram; empty-state as named section; terminal checklist |
| V-04 | Phrasing register | C-05 | Short imperatives; no hedging; "Done? Move on. Not done? Stay." |
| V-05 | Combination | C-19, C-20, C-21 | Phase Ownership Table as audit reference; symmetric pre/post pairs; ENTRY null declaration |
