Written to `simulations/quest/variations/campaign-track-variations-R2-2026-03-16.md`.

---

## Round 2 Variations — Summary

**Context:** V-01 R1 scored 100. V-02 R1 scored 57 (failed on empty-spec table rows). C-11/C-12/C-13 from V-01's excellence patterns are now baked into rubric v2. R2 explores what's beyond those three patterns.

| ID | Axis | Hypothesis |
|----|------|-----------|
| **V-01** | Role sequence — prohibition-explicit | Hard DO-NOT lists per persona ("if you find yourself doing X, stop") are stronger than V-01 R1's soft "you do not editorialize" |
| **V-02** | Lifecycle — contract-first | Opening each phase with `INPUT / OUTPUT / EXIT CONDITION` before prose makes compliance checkable by inspection |
| **V-03** | Role sequence — dual-invocation routing | Explicit FIRST-RUN vs RETURN-RUN branching prevents spurious re-registration while preserving full orchestration |
| **V-04** | Output format (fixed) + roles + contracts | R1 V-02 died on under-specified templates. This combination fixes every table row with a concrete value spec — tests whether the failure was format-fatal or spec-fatal |
| **V-05** | Phrasing register (state-machine) + roles + gates | PRECONDITION / POSTCONDITION / INVARIANT / ERROR framing per phase, with a TERMINAL verification checklist; compliance is inspectable without reading prose |

**New patterns to watch for in quest-score R2:**
- Prohibition lists (V-01) — do they tighten or add noise?
- CONTRACT blocks (V-02) — do they materially change coverage vs V-01 R1 gates?
- Invocation-type detection (V-03) — does conditional routing score as C-05 pass or break C-01?
- State-machine TERMINAL checklist (V-05) — potential new aspirational criterion
pic}-strategy-{date}.md` containing:
- Topic name and one-sentence definition
- Central hypothesis: what you believe before gathering signals (falsifiable)
- Planned signals: for each of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic), name the signal artifact this topic will produce
- Session scope: which signals are in scope for this session

> GATE 1: strategy.md must be written to disk.
> Do not proceed to Phase 2 until the file exists.

---

## Phase 2 — PLANNER: topic-roadmap

**Your role:** Signal Roadmap Architect
**Permitted:** Ordering signals, assigning priorities, mapping dependencies between signals
**Prohibited:** Modifying the hypothesis (Registrar's artifact), measuring what exists (Analyst's job), interpreting signal meaning (Narrator's job)
**If you find yourself doing any prohibited action:** stop, note "deferred to Phase [N]", and return to roadmap tasks

Run /topic-roadmap for this topic.

Produce a roadmap (append to strategy.md or write `{topic}-roadmap-{date}.md`) containing:
- Ordered signal list by namespace
- Priority tiers: P1 (this session), P2 (next session), P3 (backlog)
- Dependencies: which signals must precede which (e.g., scout before draft)

> GATE 2: Roadmap with at least one P1 signal identified.
> Do not proceed to Phase 3 until the roadmap is written.

---

## Phase 3 — ANALYST: topic-status

**Your role:** Coverage Analyst
**Permitted:** Globbing for artifacts, counting collected vs planned, naming gaps
**Prohibited:** Changing the roadmap (Planner's artifact), narrating what signals mean (Narrator's job), editorializing about quality
**If you find yourself doing any prohibited action:** stop, note "deferred to Phase [N]", and return to measurement tasks

Run /topic-status for this topic.

Scan `simulations/` for all files matching `{topic}-*-{date}.md`.
Compare against the planned signals from Phase 2.

Produce a coverage report:

| Namespace | Planned Signals | Collected | Missing (named) |
|-----------|----------------|-----------|-----------------|
| scout     | N              | n         | {artifact names or —} |
| draft     | N              | n         | {artifact names or —} |
| review    | N              | n         | {artifact names or —} |
| flow      | N              | n         | {artifact names or —} |
| trace     | N              | n         | {artifact names or —} |
| prove     | N              | n         | {artifact names or —} |
| listen    | N              | n         | {artifact names or —} |
| program   | N              | n         | {artifact names or —} |
| topic     | N              | n         | {artifact names or —} |
| **TOTAL** | N              | X/N       | N-X gaps        |

Zero-signal namespaces: {list namespaces where collected = 0, or NONE}
Coverage ratio: X/N ({pct}%)
Readiness: READY / NOT READY / CONDITIONALLY READY — {one-sentence reason}

Empty-state rule: If coverage = 0, produce the full table with all rows at 0.
Readiness = NOT READY. Zero signals is a valid measurement, not an error.

> GATE 3: Coverage table with all 9 namespace rows present.
> Do not proceed to Phase 4 until the table is produced.

---

## Phase 4 — NARRATOR: topic-story

**Your role:** Narrative Synthesist
**Permitted:** Reading collected artifacts, interpreting what they say together, evolving the hypothesis, surfacing surprises
**Prohibited:** Adding new signals to the roadmap (Planner's job), changing coverage counts (Analyst's job), re-registering the topic (Registrar's job)
**If you find yourself doing any prohibited action:** stop, note "deferred to Phase [N]", and return to synthesis tasks

Run /topic-story for this topic.
Read all collected signal artifacts before writing.

**Verdict:** [CONFIRMS / CHALLENGES / EXTENDS / UNDERMINES / LEAVES OPEN]
the hypothesis that {hypothesis text from Phase 1}.

**What the signals say together:**
{2–4 sentences synthesizing findings across collected signal artifacts}

**Hypothesis mutation:**
- Before: {original hypothesis from Phase 1}
- After: {refined hypothesis after signals}
- Type: STRENGTHENED / NARROWED / PIVOTED / INVALIDATED / UNCHANGED

**Echo (unexpected findings):**
{Bullet each signal that returned differently from what was expected.
If none: NONE}

**Next signals (top 3):**
1. {namespace}/{skill} — {why this fills the highest-value gap}
2. {namespace}/{skill} — {why}
3. {namespace}/{skill} — {why}

Empty-state rule: If no signals collected, Verdict = NOT YET REACHED.
Populate hypothesis (from Phase 1) and Next signals (from Phase 2 roadmap P1 list).
Do not skip this phase because coverage is zero.

---

## Session Delta (if not first run)

If a prior strategy.md or status snapshot exists for this topic:
- Signals added this session: {list}
- Gaps closed this session: {list}
- New gaps opened (if any): {list}

If this is the first invocation, omit this section.

---

## Empty State Handling

When no signal artifacts exist (first invocation, coverage = 0/N):

**Phase 1 (REGISTRAR):** Runs fully. Writes strategy.md with hypothesis and all 9 namespace rows. This is the only output this phase can produce without signals.

**Phase 2 (PLANNER):** Runs fully. Builds roadmap from strategy.md. Assigns P1 signals for this session.

**Phase 3 (ANALYST):** Runs fully. All namespace rows show "0 collected." Every planned signal appears in the Missing column. Readiness = NOT READY.

**Phase 4 (NARRATOR):** Runs. Verdict = NOT YET REACHED. Hypothesis row populated from Phase 1. Next signals populated from Phase 2 P1 list. Mutation block: Before = original hypothesis, After = UNCHANGED, Type = UNCHANGED.

This is a valid and complete campaign-track output. A fully formed empty dashboard is the correct result when the session is just starting.
```

---

## V-02 — Axis: **Lifecycle Emphasis (contract-first phases)**
**Hypothesis:** Opening each phase with a formal INPUT / OUTPUT / EXIT CONDITION contract — before any instruction prose — makes orchestration failures detectable by inspection: the output contract defines exactly what artifact the next phase depends on, and a reviewer can check compliance without reading all the prose.

---

```markdown
You are running campaign-track for topic: $ARGUMENTS

This skill runs four phases in strict order.
Each phase opens with its contract: what it takes in, what it produces, and what condition exits it.
Complete the contract before reading the instructions.

---

## Phase 1: topic-new

```
CONTRACT
  INPUT:   Topic name from $ARGUMENTS
  OUTPUT:  simulations/topic/strategy/{topic}-strategy-{date}.md
  FIELDS:  topic name, hypothesis, 9-namespace signal list, session scope
  EXIT:    File written to disk with all fields populated
```

Role: Registrar — you register, you do not plan or analyze.

Instructions:
Run /topic-new for the topic named in $ARGUMENTS.

Write the strategy file with:
- Topic name (one clear noun phrase)
- Central hypothesis (what you believe before evidence — falsifiable)
- Planned signals: for all 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic), name the expected artifact per namespace
- Session scope: which signals are targeted this session

> GATE: EXIT condition must be met. If strategy.md is not on disk, do not advance.

---

## Phase 2: topic-roadmap

```
CONTRACT
  INPUT:   strategy.md from Phase 1
  OUTPUT:  Roadmap section (in strategy.md or companion {topic}-roadmap-{date}.md)
  FIELDS:  ordered signal list, priority tiers (P1/P2/P3), dependency edges
  EXIT:    P1 signal list non-empty
```

Role: Planner — you sequence and prioritize, you do not measure or narrate.

Instructions:
Run /topic-roadmap for this topic.

Produce the roadmap:
- Order signals by namespace and dependency
- Assign P1 (this session), P2 (next session), P3 (backlog) tiers
- Note dependencies: which signals must come before which

> GATE: EXIT condition must be met. P1 list must be non-empty before advancing.

---

## Phase 3: topic-status

```
CONTRACT
  INPUT:   Roadmap from Phase 2 + glob of simulations/ for {topic}-*
  OUTPUT:  Coverage table (9 namespace rows), coverage ratio, readiness statement
  FIELDS:  namespace, planned count, collected count, missing artifact names
  EXIT:    Table has all 9 namespace rows present
```

Role: Analyst — you measure gaps, you do not narrate or replan.

Instructions:
Run /topic-status for this topic.

Glob `simulations/` for all files matching `{topic}-*-{date}.md`.
Compare against planned signals from Phase 2.

Coverage table (all 9 rows required):

| Namespace | Planned | Collected | Missing (named) |
|-----------|---------|-----------|-----------------|
| scout     | N       | n         | {names or —}    |
| draft     | N       | n         | {names or —}    |
| review    | N       | n         | {names or —}    |
| flow      | N       | n         | {names or —}    |
| trace     | N       | n         | {names or —}    |
| prove     | N       | n         | {names or —}    |
| listen    | N       | n         | {names or —}    |
| program   | N       | n         | {names or —}    |
| topic     | N       | n         | {names or —}    |
| **TOTAL** | N       | X/N       | N-X gaps        |

Zero-signal namespaces: {list, or NONE}
Coverage ratio: X/N ({pct}%)
Readiness: READY / NOT READY / CONDITIONALLY READY — {one sentence reason}

Empty-state: All Collected = 0. All rows in Missing column populated. Readiness = NOT READY.
This satisfies the EXIT condition. Do not skip Phase 3 when no signals exist.

> GATE: EXIT condition must be met. 9-row table must be present before advancing.

---

## Phase 4: topic-story

```
CONTRACT
  INPUT:   Hypothesis from Phase 1 + collected signal artifacts
  OUTPUT:  Narrative synthesis with verdict, mutation block, echo, next-signal list
  FIELDS:  verdict verb, synthesis prose, original hypothesis, mutated hypothesis,
           mutation type, echo findings, top-3 next signals
  EXIT:    Verdict verb explicitly stated (even if NOT YET REACHED)
```

Role: Narrator — you synthesize, you do not plan or measure.

Instructions:
Run /topic-story for this topic.
Read all collected signal artifacts.

**Verdict:** [CONFIRMS / CHALLENGES / EXTENDS / UNDERMINES / LEAVES OPEN / NOT YET REACHED]
the hypothesis that {hypothesis from Phase 1}.

**Synthesis:** {2–4 sentences on what collected signals say together}

**Hypothesis mutation:**
- Before: {original hypothesis from Phase 1}
- After: {refined hypothesis}
- Type: STRENGTHENED / NARROWED / PIVOTED / INVALIDATED / UNCHANGED

**Echo:** {unexpected findings — things signals revealed that were not planned for.
List each as a bullet. Write NONE if no surprises.}

**Next signals (top 3):**
1. {namespace}/{skill} — {gap reason}
2. {namespace}/{skill} — {gap reason}
3. {namespace}/{skill} — {gap reason}

Empty-state: Verdict = NOT YET REACHED. Synthesis = "No signals collected yet."
Mutation: Before = original hypothesis, After = same, Type = UNCHANGED.
Next signals populated from Phase 2 P1 list.

> EXIT condition: Verdict verb stated. Phase complete.

---

## Session Delta

```
CONTRACT
  INPUT:   Prior strategy.md snapshot (if exists)
  OUTPUT:  Delta section appended to output
  FIELDS:  signals added this session, gaps closed, new gaps opened, verdict change
  EXIT:    Section present if prior invocation exists; section omitted if first run
```

If this is a return invocation, append:
- Signals added this session: {list by namespace/artifact}
- Gaps closed: {list}
- New gaps opened: {list, or NONE}
- Verdict change: {e.g., "Unchanged: LEAVES OPEN" or "Changed from NOT YET REACHED to CHALLENGES"}

---

## Empty State Handling

First invocation with zero collected signals: all four phases run fully.
Phase 1 and 2 produce their artifacts normally (no signals required for registration or planning).
Phase 3 produces a complete coverage table with all Collected = 0 and all Missing cells populated.
Phase 4 produces the synthesis skeleton: verdict = NOT YET REACHED, hypothesis from Phase 1, next signals from Phase 2 P1 list.
This is a complete, valid campaign-track output.
```

---

## V-03 — Axis: **Role Sequence (dual-invocation routing)**
**Hypothesis:** The standard four-phase sequence (register → plan → measure → narrate) is optimal for first invocations. For return invocations, Phase 1 (register) is a no-op if strategy.md already exists. Explicitly routing first-run and return-run to different phase behaviors avoids spurious re-registration while preserving full orchestration integrity.

---

```markdown
You are running campaign-track for topic: $ARGUMENTS

Before starting, determine your invocation type:

**FIRST RUN:** No strategy.md exists for this topic yet. Run all four phases.
**RETURN RUN:** strategy.md exists. Skip to Phase 2 validation, then run Phases 3 and 4.

Check: does `simulations/topic/strategy/{topic}-strategy-{date}.md` exist?
- Yes → RETURN RUN. Go to Phase 2.
- No → FIRST RUN. Start at Phase 1.

---

## [FIRST RUN ONLY] Phase 1 — REGISTRAR: topic-new

Role: Registrar. You register, you do not plan or analyze.

Run /topic-new for this topic.

Write `simulations/topic/strategy/{topic}-strategy-{date}.md`:
- Topic name and one-sentence definition
- Central hypothesis (what you believe before evidence — falsifiable)
- Planned signals: all 9 namespaces with expected artifact name per namespace
  (scout, draft, review, flow, trace, prove, listen, program, topic)
- Session scope: which signals are targeted this session

> GATE: strategy.md written to disk. Do not proceed until file exists.

---

## Phase 2 — PLANNER: topic-roadmap (validate or build)

Role: Planner. You sequence and prioritize, you do not measure or narrate.

**First run:** Build the roadmap from the strategy.md you just wrote.
**Return run:** Load the existing strategy.md. Validate the roadmap is still current.
  If new context has arrived since last run, update P1/P2 tiers before proceeding.
  If the roadmap is current, note "Roadmap validated — no changes" and proceed.

Output: roadmap section in strategy.md or `{topic}-roadmap-{date}.md`:
- Ordered signal list by namespace
- Priority tiers: P1 (this session), P2 (next session), P3 (backlog)
- Dependency edges between signals

> GATE: P1 signal list non-empty. Do not proceed until roadmap is ready.

---

## Phase 3 — ANALYST: topic-status

Role: Analyst. You measure gaps, you do not interpret or narrate.

Run /topic-status for this topic.
Glob `simulations/` for all files matching `{topic}-*`.
Compare against planned signals in the roadmap.

Coverage table (all 9 rows required — even if all show 0):

| Namespace | Planned | Collected | Missing (named) |
|-----------|---------|-----------|-----------------|
| scout     | N       | n         | {names or —}    |
| draft     | N       | n         | {names or —}    |
| review    | N       | n         | {names or —}    |
| flow      | N       | n         | {names or —}    |
| trace     | N       | n         | {names or —}    |
| prove     | N       | n         | {names or —}    |
| listen    | N       | n         | {names or —}    |
| program   | N       | n         | {names or —}    |
| topic     | N       | n         | {names or —}    |
| **TOTAL** | N       | X/N       |                 |

Zero-signal namespaces: {list, or NONE}
Coverage ratio: X/N ({pct}%)
Readiness: READY / NOT READY / CONDITIONALLY READY — {one sentence reason}

**Return run:** If this is not the first invocation, also show session delta here:
- Signals present this run that were absent last run: {list}
- Coverage change: {X/N last run} → {X/N this run}

> GATE: 9-row table present with all namespace rows filled. Do not proceed until done.

---

## Phase 4 — NARRATOR: topic-story

Role: Narrator. You synthesize, you do not plan or register.

Run /topic-story for this topic.
Read collected signal artifacts.

**Verdict:** [CONFIRMS / CHALLENGES / EXTENDS / UNDERMINES / LEAVES OPEN / NOT YET REACHED]
the hypothesis that {hypothesis text from strategy.md}.

**Synthesis:** {2–4 sentences on what signals say together}

**Hypothesis mutation:**
- Before: {original hypothesis}
- After: {refined hypothesis}
- Type: STRENGTHENED / NARROWED / PIVOTED / INVALIDATED / UNCHANGED

**Echo (unexpected findings):**
{Signals that returned differently than expected. NONE if no surprises.}

**Next signals (top 3):**
1. {namespace}/{skill} — {gap reason}
2. {namespace}/{skill} — {gap reason}
3. {namespace}/{skill} — {gap reason}

**Return run verdict change:**
{e.g., "Verdict unchanged: LEAVES OPEN" or "Updated from NOT YET REACHED to CHALLENGES
because 3 signals now collected in scout and draft namespaces"}

---

## Empty State Handling

**First invocation with zero signals:**

Phase 1: Runs fully — writes strategy.md.
Phase 2: Runs fully — builds roadmap, assigns P1 signals.
Phase 3: Runs fully — all rows show 0 collected. Readiness = NOT READY.
Phase 4: Runs. Verdict = NOT YET REACHED. Hypothesis from Phase 1.
  Next signals = P1 list from Phase 2. Mutation type = UNCHANGED.

A fully formed dashboard with zero signals is a valid first-run output.
It is not an error. It is the starting state of the campaign.
```

---

## V-04 — Axis: **Output Format (repaired dashboard) + Role-gated + Contract-first** *(combination)*
**Hypothesis:** R1 V-02 failed because dashboard tables had header rows only — the template was underspecified. V-04 R2 combines the dashboard format with role-gated phases and contract-first framing. A properly spec'd dashboard with roles and gates should score equivalently to V-01's prose form. This tests whether R1 V-02's failure was format-fatal or spec-fatal.

---

```markdown
You are running campaign-track for topic: $ARGUMENTS

Produce a TOPIC DASHBOARD as the final output.
Run four phases to populate it. Each phase has a role and a contract.

---

## Phase 1 — REGISTRAR: topic-new

```
ROLE:    Registrar (register, do not plan or analyze)
INPUT:   Topic name from $ARGUMENTS
OUTPUT:  strategy.md + Registration section of dashboard
GATE:    strategy.md written to disk before Phase 2
```

Run /topic-new. Write `simulations/topic/strategy/{topic}-strategy-{date}.md`.

Required fields:
- Topic name
- Central hypothesis (falsifiable, written as "I believe X because Y")
- Planned signals: list all 9 namespaces with one expected artifact each
- Session scope

Populate the Registration section of the dashboard (below).

> Do not proceed to Phase 2 until strategy.md is written.

---

## Phase 2 — PLANNER: topic-roadmap

```
ROLE:    Planner (sequence and prioritize, do not measure or narrate)
INPUT:   strategy.md from Phase 1
OUTPUT:  Roadmap (in strategy.md or companion file) + Signal Roadmap section of dashboard
GATE:    P1 signal list non-empty before Phase 3
```

Run /topic-roadmap. Produce the signal roadmap with P1/P2/P3 tiers and dependencies.

Populate the Signal Roadmap section of the dashboard (below).

> Do not proceed to Phase 3 until P1 list is non-empty.

---

## Phase 3 — ANALYST: topic-status

```
ROLE:    Analyst (measure gaps, do not narrate or replan)
INPUT:   Roadmap from Phase 2 + glob simulations/ for {topic}-*
OUTPUT:  Coverage table + Coverage Status section of dashboard
GATE:    All 9 namespace rows present in table before Phase 4
```

Run /topic-status. Glob and compare. Populate Coverage Status section (below).

> Do not proceed to Phase 4 until all 9 rows are present.

---

## Phase 4 — NARRATOR: topic-story

```
ROLE:    Narrator (synthesize, do not plan or measure)
INPUT:   Hypothesis from Phase 1 + collected signal artifacts
OUTPUT:  Narrative synthesis + Narrative section of dashboard
GATE:    Verdict verb stated before session delta
```

Run /topic-story. Read signals. Populate Narrative section (below).

---

## TOPIC DASHBOARD — {TOPIC NAME} — {DATE}

### Registration
| Field | Value |
|-------|-------|
| Topic | {name from Phase 1} |
| Hypothesis | {one-sentence hypothesis from Phase 1} |
| Strategy file | simulations/topic/strategy/{topic}-strategy-{date}.md |
| Session scope | {which signals are targeted this session} |

---

### Signal Roadmap
| Priority | Namespace | Skill | Artifact Name | Depends On |
|----------|-----------|-------|---------------|------------|
| P1 | {ns} | {skill} | {topic}-{signal}-{date}.md | {none or prior skill} |
| P1 | {ns} | {skill} | {topic}-{signal}-{date}.md | {dependency} |
| P2 | {ns} | {skill} | {topic}-{signal}-{date}.md | {dependency} |
| P3 | {ns} | {skill} | {topic}-{signal}-{date}.md | {dependency} |
*(continue for all signals)*

---

### Coverage Status
| Namespace | Planned | Collected | Missing (named) |
|-----------|---------|-----------|-----------------|
| scout     | N       | n         | {artifact names, or —} |
| draft     | N       | n         | {artifact names, or —} |
| review    | N       | n         | {artifact names, or —} |
| flow      | N       | n         | {artifact names, or —} |
| trace     | N       | n         | {artifact names, or —} |
| prove     | N       | n         | {artifact names, or —} |
| listen    | N       | n         | {artifact names, or —} |
| program   | N       | n         | {artifact names, or —} |
| topic     | N       | n         | {artifact names, or —} |
| **TOTAL** | N       | X/N       | N-X gaps        |

Zero-signal namespaces: {list, or NONE}
Coverage ratio: X/N ({pct}%)
Readiness: READY / NOT READY / CONDITIONALLY READY — {one sentence reason}

---

### Narrative Synthesis
| Field | Value |
|-------|-------|
| Verdict | {CONFIRMS / CHALLENGES / EXTENDS / UNDERMINES / LEAVES OPEN / NOT YET REACHED} the hypothesis |
| Synthesis | {2–3 sentences: what do collected signals say together?} |
| Original hypothesis | {exact text from Registration section} |
| Mutated hypothesis | {refined text after signals} |
| Mutation type | {STRENGTHENED / NARROWED / PIVOTED / INVALIDATED / UNCHANGED} |

---

### Echo
{Bullet list of signals that returned differently than planned. NONE if no surprises.}

---

### Next Actions
| Priority | Namespace | Skill | Gap Reason |
|----------|-----------|-------|-----------|
| 1 | {ns} | {skill} | {why this fills the most critical gap} |
| 2 | {ns} | {skill} | {why} |
| 3 | {ns} | {skill} | {why} |

---

### Session Delta
*(Omit if first invocation. For return runs:)*
| Change | Detail |
|--------|--------|
| Signals added | {list by namespace/artifact} |
| Gaps closed | {list, or NONE} |
| New gaps opened | {list, or NONE} |
| Verdict change | {e.g., "Unchanged: LEAVES OPEN" or "Updated: NOT YET REACHED → CHALLENGES"} |

---

## Empty State Handling

**First invocation, zero signals collected:**

Phase 1 (REGISTRAR): Runs fully. strategy.md written. All 9 namespace rows populated in the planned column of Coverage Status, all with 0 in Collected and artifact names in Missing.

Phase 2 (PLANNER): Runs fully. Signal Roadmap table populated with all P1/P2/P3 signals.

Phase 3 (ANALYST): Runs fully. Coverage Status table: all Collected = 0. All Missing cells filled with planned artifact names. Readiness = NOT READY.

Phase 4 (NARRATOR): Runs. Verdict = NOT YET REACHED. Synthesis = "No signals collected yet." Original hypothesis from Registration. Mutation type = UNCHANGED. Next Actions populated from P1 roadmap.

Session Delta: OMITTED (first invocation).

This is a complete, valid dashboard. The empty state is an accurate starting snapshot, not an error condition.
```

---

## V-05 — Axis: **Phrasing Register (formal/technical — state-machine framing) + Role-gated + Gates** *(combination)*
**Hypothesis:** Expressing each phase as a state machine — PRECONDITION / ACTION / POSTCONDITION / INVARIANT — borrowed from trace-state discipline, makes compliance checkable by inspection without reading prose. A reviewer who sees the postcondition knows exactly what artifact to verify. This is the most formal register possible and tests whether formalism aids or impedes the model's execution.

---

```markdown
campaign-track orchestrator for: $ARGUMENTS

Execution model: four-state machine. Each phase has a precondition, a postcondition,
and an invariant that must hold at all times. Phases execute in strict order.
Violations of preconditions or postconditions are named errors, not silent skips.

---

## STATE 1 — REGISTRATION

```
ROLE:          Registrar
PRECONDITION:  Topic name present in $ARGUMENTS
ACTION:        /topic-new
POSTCONDITION: simulations/topic/strategy/{topic}-strategy-{date}.md exists on disk
               File contains: topic name, hypothesis, 9-namespace signal list, session scope
INVARIANT:     Registrar does not prioritize, measure, or synthesize
ERROR:         If strategy.md cannot be written, halt and report the error before advancing
```

Execute /topic-new.

Strategy file MUST contain:
- `topic`: {name from $ARGUMENTS}
- `hypothesis`: one falsifiable sentence ("I believe X because Y")
- `signals`: for each of the 9 namespaces, the expected artifact name
  - scout: {topic}-scout-competitors-{date}.md (example; adjust to topic)
  - draft: ...
  - review: ...
  - flow: ...
  - trace: ...
  - prove: ...
  - listen: ...
  - program: ...
  - topic: ...
- `scope`: which signals are targeted this session

Transition condition: POSTCONDITION met → advance to STATE 2.

---

## STATE 2 — PLANNING

```
ROLE:          Planner
PRECONDITION:  STATE 1 POSTCONDITION met (strategy.md exists)
ACTION:        /topic-roadmap
POSTCONDITION: Roadmap written (in strategy.md or {topic}-roadmap-{date}.md)
               P1 signal list non-empty
INVARIANT:     Planner does not modify hypothesis, measure artifacts, or narrate
ERROR:         If P1 list is empty, diagnose and populate before advancing
```

Execute /topic-roadmap.

Roadmap MUST contain:
- Ordered list of signals, grouped by namespace
- Priority tier per signal: P1 (this session) / P2 (next session) / P3 (backlog)
- Dependency edges: {signal A} must precede {signal B} if B requires A's output

Transition condition: POSTCONDITION met (P1 non-empty) → advance to STATE 3.

---

## STATE 3 — MEASUREMENT

```
ROLE:          Analyst
PRECONDITION:  STATE 2 POSTCONDITION met (roadmap with P1 signals exists)
ACTION:        /topic-status
POSTCONDITION: Coverage table with all 9 namespace rows present, ratio computed
INVARIANT:     Analyst does not modify the roadmap, infer meaning, or make readiness arguments
               beyond the stated READY/NOT READY/CONDITIONALLY READY classification
ERROR:         If glob finds no artifacts, produce table with all Collected = 0; this is not an error
```

Execute /topic-status. Glob `simulations/` for `{topic}-*`.

Coverage table:

| Namespace | Planned | Collected | Missing (named artifacts) |
|-----------|---------|-----------|---------------------------|
| scout     | N       | n         | {names or —}              |
| draft     | N       | n         | {names or —}              |
| review    | N       | n         | {names or —}              |
| flow      | N       | n         | {names or —}              |
| trace     | N       | n         | {names or —}              |
| prove     | N       | n         | {names or —}              |
| listen    | N       | n         | {names or —}              |
| program   | N       | n         | {names or —}              |
| topic     | N       | n         | {names or —}              |
| **TOTAL** | N       | X/N       |                           |

Zero-signal namespaces: {list namespaces where Collected = 0, or NONE}
Coverage ratio: X of N signals collected ({pct}%)
Readiness classification:
  READY: all P1 signals collected
  CONDITIONALLY READY: P1 signals for critical namespaces collected, remainder P2+
  NOT READY: one or more P1 signals missing

Transition condition: POSTCONDITION met (9-row table exists) → advance to STATE 4.

---

## STATE 4 — SYNTHESIS

```
ROLE:          Narrator
PRECONDITION:  STATE 3 POSTCONDITION met (coverage table exists)
ACTION:        /topic-story
POSTCONDITION: Verdict verb explicitly stated; hypothesis mutation block present
INVARIANT:     Narrator does not add signals to the roadmap, modify coverage counts, or re-register
ERROR:         If no signals collected, verdict = NOT YET REACHED; this is a valid final state
```

Execute /topic-story. Read all collected signal artifacts.

**VERDICT:** {CONFIRMS / CHALLENGES / EXTENDS / UNDERMINES / LEAVES OPEN / NOT YET REACHED}
the hypothesis that: {hypothesis text from STATE 1}

**SYNTHESIS:** {2–4 sentences: what do collected signals say together?}

**HYPOTHESIS MUTATION:**
| Field | Value |
|-------|-------|
| Before | {original hypothesis} |
| After | {refined hypothesis} |
| Type | STRENGTHENED / NARROWED / PIVOTED / INVALIDATED / UNCHANGED |

**ECHO — unexpected findings:**
{List signals that returned differently than expected. NONE if no surprises.}

**NEXT SIGNALS (top 3 by gap priority):**
1. {namespace}/{skill} — {gap reason}
2. {namespace}/{skill} — {gap reason}
3. {namespace}/{skill} — {gap reason}

Transition condition: POSTCONDITION met (verdict stated) → STATE MACHINE COMPLETE.

---

## TERMINAL OUTPUT

After all 4 states complete, verify:

| Check | Status |
|-------|--------|
| strategy.md on disk | {PASS / FAIL} |
| Roadmap P1 non-empty | {PASS / FAIL} |
| Coverage table: 9 rows | {PASS / FAIL} |
| Verdict verb stated | {PASS / FAIL} |
| Hypothesis mutation present | {PASS / FAIL} |

If any check = FAIL, return to the failing state and complete it before declaring done.

---

## SESSION DELTA (if return invocation)

```
PRECONDITION:  Prior strategy.md snapshot exists
OUTPUT:        Delta section appended to terminal output
```

- Signals added this session: {list}
- Gaps closed: {list}
- Verdict change: {e.g., "Unchanged: LEAVES OPEN" / "Updated: NOT YET REACHED → EXTENDS"}

If first invocation: omit this section.

---

## EMPTY STATE MACHINE

**When no signals exist (first invocation, STATE 3 finds 0 artifacts):**

```
STATE 1 result: strategy.md written — PASS
STATE 2 result: roadmap with P1 list — PASS
STATE 3 result: coverage table, all Collected = 0, Readiness = NOT READY — PASS
STATE 4 result: verdict = NOT YET REACHED, hypothesis from STATE 1,
                next signals from STATE 2 P1 list — PASS
```

All states reach their POSTCONDITION. The state machine completes successfully.
This is a valid terminal output. Treat it as the campaign baseline, not an error.
```

---

## Variation Summary — Round 2

| ID | Axis | Hypothesis | Builds On | Key New Pattern |
|----|------|-----------|-----------|-----------------|
| V-01 | Role sequence (prohibition-explicit) | Bidirectional DO-NOT lists sharpen phase fidelity beyond positive framing | V-01 R1 (role-gated) | Explicit prohibition per persona |
| V-02 | Lifecycle (contract-first) | CONTRACT block before prose makes phases checkable by inspection | V-03 R1 (gates) | INPUT/OUTPUT/EXIT per phase as opening spec |
| V-03 | Role sequence (dual-invocation routing) | Routing FIRST-RUN vs RETURN-RUN to different behaviors avoids spurious re-registration | V-01 R1 | Invocation-type detection + conditional phase execution |
| V-04 | Output format (repaired) + roles + contracts | R1 V-02 failed on spec completeness, not format; fully-spec'd dashboard scores equivalently to prose | V-02 R1 (fixed) + V-01 R1 | Dashboard template with all rows fully specified |
| V-05 | Phrasing register (formal/state-machine) + roles + gates | PRECONDITION/POSTCONDITION/INVARIANT framing makes compliance checkable without prose reading | V-01 R1 + V-03 R1 | State-machine phase model with TERMINAL verification checklist |
