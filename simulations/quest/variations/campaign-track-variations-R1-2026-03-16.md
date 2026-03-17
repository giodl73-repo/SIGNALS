# `/campaign-track` Variate Round 1 — V-01 through V-05

---

## V-01 — Axis: **Role Sequence**
**Hypothesis:** Assigning a distinct named AI role to each sub-skill phase (Registrar → Planner → Analyst → Narrator) sharpens phase fidelity and prevents role bleed where the narrator starts editorializing during registration.

---

```markdown
You are running the campaign-track orchestrator for topic: $ARGUMENTS

This skill runs four phases in strict order. Each phase assigns you a different role.
Do not blend roles. Complete each fully before moving to the next.

---

## Phase 1 — REGISTRAR: topic-new

Your role: Topic Registration Clerk.
You are creating the permanent record for this topic.
You do not editorialize. You do not plan. You register.

Run /topic-new for the topic named in $ARGUMENTS.

Produce `simulations/topic/strategy/{topic}-strategy-{date}.md` containing:
- Topic name and one-sentence definition
- The central hypothesis (what we believe before gathering signals)
- Planned signal types: list each namespace (scout, draft, review, flow, trace,
  prove, listen, program, topic) and the signal artifact this topic will produce
  from each
- Session scope: what signals are in scope for this session

Do not proceed to Phase 2 until strategy.md is written to disk.

---

## Phase 2 — PLANNER: topic-roadmap

Your role: Signal Roadmap Architect.
You are building the signal plan. You do not analyze existing signals.
You plan what signals are needed and in what order.

Run /topic-roadmap for this topic.

Produce a roadmap section in the strategy artifact (or a companion
`{topic}-roadmap-{date}.md`) containing:
- Ordered list of signals to gather, grouped by namespace
- Dependency edges: which signals unlock which (e.g., scout before draft)
- Priority tier: P1 (this session), P2 (next session), P3 (backlog)

Do not proceed to Phase 3 until the roadmap is written.

---

## Phase 3 — ANALYST: topic-status

Your role: Coverage Analyst.
You are measuring the gap between what was planned and what exists.
You do not narrate. You measure and name gaps.

Run /topic-status for this topic.

Scan `simulations/` for all artifacts matching `{topic}-*-{date}.md`.
Produce a coverage report:

| Namespace | Planned Signals | Collected | Missing |
|-----------|----------------|-----------|---------|
| scout     | ...            | ...       | ...     |
| draft     | ...            | ...       | ...     |
| review    | ...            | ...       | ...     |
| flow      | ...            | ...       | ...     |
| trace     | ...            | ...       | ...     |
| prove     | ...            | ...       | ...     |
| listen    | ...            | ...       | ...     |
| program   | ...            | ...       | ...     |
| topic     | ...            | ...       | ...     |
| **TOTAL** | ...            | X/N       | N-X gaps|

Flag any namespace with zero collected signals as a ZERO-SIGNAL NAMESPACE.

Coverage ratio: X/N signals collected (N = total planned).
Readiness statement: READY / NOT READY / CONDITIONALLY READY + one-sentence reason.

Do not proceed to Phase 4 until the coverage table is produced.

---

## Phase 4 — NARRATOR: topic-story

Your role: Narrative Synthesist.
You are reading the signals that exist and writing what they say together.
You do not plan. You do not measure. You narrate.

Run /topic-story for this topic.

Produce the narrative synthesis:

**Verdict:** [verb phrase — CONFIRMS / CHALLENGES / EXTENDS / UNDERMINES /
LEAVES OPEN] the central hypothesis.

**What the signals say together:**
[2–4 sentences synthesizing findings across collected signal artifacts]

**Hypothesis mutation:**
- Original: [restate the hypothesis from Phase 1]
- Mutated: [refined version of the hypothesis after signals]
- Mutation type: [STRENGTHENED / NARROWED / PIVOTED / INVALIDATED / UNCHANGED]

**Unexpected findings (Echo):**
[Any signal that came back different from what was expected. If none, write NONE.]

**Next signals (top 3):**
1. [namespace/skill] — [why this fills the most critical gap]
2. [namespace/skill] — [why]
3. [namespace/skill] — [why]

---

## Session Delta (if this is not the first run)

If a prior strategy.md or status snapshot exists for this topic, append a
session delta section:
- Signals added this session: [list]
- Gaps closed this session: [list]
- New gaps opened: [list]

## Empty State Handling

If no signals exist yet (first invocation, coverage = 0/N):
- Complete Phases 1 and 2 fully
- Phase 3: produce the coverage table with all rows showing "0 collected"
- Phase 4: produce the narrative skeleton with hypothesis only, verdict = NOT YET REACHED
- This is a valid and useful output. Do not skip phases because no signals exist.
```

---

## V-02 — Axis: **Output Format**
**Hypothesis:** A single consolidated dashboard table as the terminal output artifact — rather than phase-by-phase prose sections — makes coverage state and readiness scannable in under 10 seconds, improving the skill's utility as a session bookend.

---

```markdown
Run the campaign-track orchestrator for topic: $ARGUMENTS

Execute these four sub-skills in order:
1. /topic-new → registers the topic, produces strategy.md
2. /topic-roadmap → plans signals, populates the roadmap
3. /topic-status → scans for collected artifacts, computes coverage
4. /topic-story → synthesizes signals into narrative verdict

After all four complete, produce the TOPIC DASHBOARD as your primary output.

---

## TOPIC DASHBOARD — {TOPIC NAME} — {DATE}

### Registration
| Field | Value |
|-------|-------|
| Topic | {name} |
| Hypothesis | {one sentence} |
| Strategy file | simulations/topic/strategy/{topic}-strategy-{date}.md |
| Session scope | {in-scope signals} |

---

### Signal Roadmap
| Order | Namespace | Skill | Priority | Dependency |
|-------|-----------|-------|----------|------------|
| 1 | scout | scout-competitors | P1 | none |
| 2 | draft | draft-spec | P1 | scout |
| ... | ... | ... | ... | ... |

---

### Coverage Status
| Namespace | Planned | Collected | Missing Artifacts |
|-----------|---------|-----------|-------------------|
| scout     | N       | n         | {names or —}      |
| draft     | N       | n         | {names or —}      |
| review    | N       | n         | {names or —}      |
| flow      | N       | n         | {names or —}      |
| trace     | N       | n         | {names or —}      |
| prove     | N       | n         | {names or —}      |
| listen    | N       | n         | {names or —}      |
| program   | N       | n         | {names or —}      |
| topic     | N       | n         | {names or —}      |
| **TOTAL** |         | **X/N**   |                   |

**Zero-signal namespaces:** {list, or NONE}
**Coverage ratio:** X/N ({pct}%)
**Readiness:** {READY / NOT READY / CONDITIONALLY READY} — {one sentence reason}

---

### Narrative Synthesis
| Field | Value |
|-------|-------|
| Verdict | {verb: CONFIRMS / CHALLENGES / EXTENDS / UNDERMINES / LEAVES OPEN} the hypothesis |
| Synthesis | {2–3 sentence summary of what collected signals say together} |
| Original hypothesis | {exact text from registration} |
| Mutated hypothesis | {refined text after signals} |
| Mutation type | {STRENGTHENED / NARROWED / PIVOTED / INVALIDATED / UNCHANGED} |

---

### Echo (Unexpected Findings)
{Bullet list of signals that came back different from expected, or NONE}

---

### Next Actions
| Priority | Namespace | Skill | Reason |
|----------|-----------|-------|--------|
| 1 | {ns} | {skill} | {fills gap X} |
| 2 | {ns} | {skill} | {fills gap Y} |
| 3 | {ns} | {skill} | {fills gap Z} |

---

### Session Delta
*(omit if first invocation)*
| Change | Detail |
|--------|--------|
| Signals added | {list} |
| Gaps closed | {list} |
| New gaps opened | {list} |

---

## Empty State Handling

If no signal artifacts exist yet (coverage = 0/N):
- Complete /topic-new and /topic-roadmap in full
- In the Coverage Status table: all "Collected" cells = 0, all namespaces appear
- In Narrative Synthesis: hypothesis row populated, all other rows = NOT YET REACHED
- Verdict = NOT YET REACHED
- Next Actions table: show P1 signals from the roadmap
- Produce the full dashboard. Zero signals is a valid state, not an error.
```

---

## V-03 — Axis: **Lifecycle Emphasis**
**Hypothesis:** Explicit phase gate instructions ("GATE: do not proceed until output X is confirmed on disk") prevent the most common failure mode — a partial run where the skill produces narrative without completing registration or status — and are worth the verbosity cost.

---

```markdown
You are the campaign-track orchestrator for: $ARGUMENTS

This skill has four phases and three gates. Gates are hard stops.
Do not advance past a gate until its condition is met.

===================================================================
PHASE 1: REGISTER THE TOPIC
Sub-skill: /topic-new
===================================================================

Invoke /topic-new with the topic name from $ARGUMENTS.

Required output:
  File: simulations/topic/strategy/{topic}-strategy-{date}.md
  Must contain:
    - Topic name
    - Central hypothesis (explicit, falsifiable)
    - Planned signals per namespace (all 9 namespaces listed)
    - Session scope declaration

> GATE 1: strategy.md must exist on disk before proceeding.
> If file write failed, resolve before continuing.

===================================================================
PHASE 2: BUILD THE SIGNAL ROADMAP
Sub-skill: /topic-roadmap
===================================================================

Invoke /topic-roadmap for this topic.

Required output (appended to strategy.md or separate roadmap file):
  - Ordered signal list (namespace → skill → artifact name)
  - Priority tiers: P1 this session / P2 next / P3 backlog
  - Dependencies between signals (which unlock which)

> GATE 2: Roadmap with at least P1 signals identified before proceeding.
> P1 list must be non-empty (there must be something to do this session).

===================================================================
PHASE 3: MEASURE COVERAGE
Sub-skill: /topic-status
===================================================================

Invoke /topic-status for this topic.

Scan simulations/ for all files matching {topic}-*-{date}.md.
Compare against planned signals from the roadmap.

Required output:
  Coverage table (all 9 namespaces, even if zero)
  Zero-signal namespace list (namespaces with no collected signals)
  Coverage ratio: X of N signals collected
  Readiness statement: READY / NOT READY / CONDITIONALLY READY + reason

Empty state rule: 0 collected is a valid state.
Produce the full table. Do not skip this phase because no artifacts exist.

> GATE 3: Coverage table with all 9 namespace rows present before proceeding.

===================================================================
PHASE 4: SYNTHESIZE THE NARRATIVE
Sub-skill: /topic-story
===================================================================

Invoke /topic-story for this topic.
Read collected signal artifacts before writing the synthesis.

Required output:

  VERDICT: [CONFIRMS / CHALLENGES / EXTENDS / UNDERMINES / LEAVES OPEN]
  the hypothesis that {hypothesis text}.

  SYNTHESIS: {2–4 sentences describing what collected signals say together}

  HYPOTHESIS MUTATION:
    Before: {original hypothesis}
    After:  {refined hypothesis}
    Type:   STRENGTHENED | NARROWED | PIVOTED | INVALIDATED | UNCHANGED

  ECHO (unexpected findings):
    {Bullet each signal that came back differently from expected}
    {Write NONE if no surprises}

  NEXT SIGNALS (top 3):
    1. {namespace}/{skill} — {reason it fills the highest-value gap}
    2. {namespace}/{skill} — {reason}
    3. {namespace}/{skill} — {reason}

Empty state rule: if no signals collected, verdict = NOT YET REACHED.
Produce hypothesis and next signals. Do not skip narrative because coverage is zero.

===================================================================
SESSION DELTA (if applicable)
===================================================================

If a prior strategy.md snapshot exists for this topic:
  - List signals added this session
  - List gaps closed this session
  - List any new gaps opened

If this is the first invocation: omit the delta section.

===================================================================
FINAL CHECK
===================================================================

Before outputting, verify:
  [ ] strategy.md written to disk (Gate 1 passed)
  [ ] Roadmap with P1 signals present (Gate 2 passed)
  [ ] Coverage table: all 9 rows present (Gate 3 passed)
  [ ] Verdict verb stated explicitly
  [ ] Hypothesis mutation recorded

If any check fails, complete the missing output before finishing.
```

---

## V-04 — Axis: **Phrasing Register (conversational) + Inertia Framing (status-quo competitor named)**
**Hypothesis:** Naming the default behavior ("the easy path is to just start building without gathering signals") as an explicit inertia competitor, combined with conversational phrasing, makes the skill feel like a deliberate choice rather than a bureaucratic gate — increasing honest engagement with gaps rather than perfunctory output.

---

```markdown
You're running campaign-track for: $ARGUMENTS

The default is to skip this and start building. You're here because you chose
not to do that. This skill makes that choice concrete.

Here's what happens: you register the topic so it has a home, build a signal
roadmap so you know what evidence you need, check what evidence you already
have, and then read what the signals say together. Four steps. Let's go.

---

### Step 1: Register the topic — /topic-new

Before you can gather evidence, the topic needs a permanent record.

Run /topic-new for {$ARGUMENTS} and write:
  simulations/topic/strategy/{topic}-strategy-{date}.md

This file is the source of truth. Put in it:
- What the topic is (one clear sentence)
- What you believe right now — the hypothesis you're testing
  (be honest; vague hypotheses produce vague signals)
- What signals you're planning to gather, namespace by namespace
  (all 9: scout, draft, review, flow, trace, prove, listen, program, topic)
- What's in scope for this session specifically

The alternative to writing this file is starting without knowing what
you're looking for. That's the inertia path. Write the file.

---

### Step 2: Plan the signal roadmap — /topic-roadmap

Run /topic-roadmap for this topic.

The roadmap answers: "If I had unlimited time, what evidence would I collect
and in what order?" You won't have unlimited time, so prioritize:

- P1: signals you'll collect this session
- P2: signals for the next session
- P3: eventual backlog

For each signal, name the namespace and skill. Note dependencies
(you can't draft a spec before scouting the space — usually).

Without a roadmap, you'll gather the easy signals and call it done.
The roadmap is what keeps you honest about gaps.

---

### Step 3: Check coverage — /topic-status

Run /topic-status for this topic.

Look through simulations/ for artifacts that match this topic.
Then compare what you found against what you planned.

Show this as a coverage table:

| Namespace | Planned | Collected | What's Missing |
|-----------|---------|-----------|----------------|
| scout     |         |           |                |
| draft     |         |           |                |
| review    |         |           |                |
| flow      |         |           |                |
| trace     |         |           |                |
| prove     |         |           |                |
| listen    |         |           |                |
| program   |         |           |                |
| topic     |         |           |                |
| TOTAL     |         | X/N       |                |

Call out zero-signal namespaces explicitly. A namespace with nothing
is a namespace where the inertia path won. Name it.

Coverage ratio: X/N.
Readiness: READY / NOT READY / CONDITIONALLY READY — one honest sentence about why.

If you have zero signals (first run), fill in the table with zeros.
That's not failure — that's an accurate picture of where you are.

---

### Step 4: Read the signals — /topic-story

Run /topic-story for this topic.

Read whatever signal artifacts exist, then write:

**Verdict:** [CONFIRMS / CHALLENGES / EXTENDS / UNDERMINES / LEAVES OPEN]
the hypothesis.

**What the signals say:** 2–4 sentences. What do the collected signals
actually say together? Not what you hoped they'd say — what they say.

**Hypothesis update:**
- You came in believing: {original hypothesis}
- After signals, you believe: {updated hypothesis}
- The update type: STRENGTHENED / NARROWED / PIVOTED / INVALIDATED / UNCHANGED

**Surprises (Echo):** Any signal that came back differently than expected.
This is the most valuable output — surprises are why you gathered signals
instead of just building. List them. If none, write NONE.

**Where to go next:** Three signals that would do the most to reduce
uncertainty. Name the namespace and skill for each.

If you have zero signals, the verdict is NOT YET REACHED. Write the
hypothesis and the next-signal recommendations. That's still useful.

---

### Session delta (if this isn't your first run)

If you've run campaign-track on this topic before, note:
- What signals came in this session
- Which gaps closed
- Whether any new gaps opened

The inertia path is to not run this at the end of the session.
The delta is what makes the next session faster.
```

---

## V-05 — Axis: **Output Format (compressed) + Lifecycle Emphasis (minimal, implicit)**
**Hypothesis:** A maximally compressed form with no phase headers, single-pass instructions, and a tightly bounded output template scores on par with verbose phase-gated versions on the essential rubric criteria (C-01 through C-05) while being materially shorter — testing whether the verbosity in V-01/V-03 is load-bearing or decorative.

---

```markdown
campaign-track for: $ARGUMENTS

Run in order: /topic-new → /topic-roadmap → /topic-status → /topic-story.
Produce this output and nothing else:

---

**TOPIC:** {name}
**HYPOTHESIS:** {one sentence — what you believe before gathering signals}
**STRATEGY FILE:** simulations/topic/strategy/{topic}-strategy-{date}.md

**ROADMAP (P1 this session):**
- {namespace}/{skill} → {artifact name}
- {namespace}/{skill} → {artifact name}
- (continue for all P1 signals)

**COVERAGE:**
scout {n}/{N} | draft {n}/{N} | review {n}/{N} | flow {n}/{N} | trace {n}/{N}
prove {n}/{N} | listen {n}/{N} | program {n}/{N} | topic {n}/{N}
Total: {X}/{N} — {pct}%
Zero-signal: {namespace list, or NONE}
Readiness: {READY / NOT READY / CONDITIONALLY READY} — {reason}

**VERDICT:** {CONFIRMS / CHALLENGES / EXTENDS / UNDERMINES / LEAVES OPEN} the hypothesis.

**SYNTHESIS:** {2–3 sentences on what collected signals say together}

**HYPOTHESIS MUTATION:**
Before: {original}
After: {refined}
Type: {STRENGTHENED / NARROWED / PIVOTED / INVALIDATED / UNCHANGED}

**ECHO:** {unexpected findings, or NONE}

**NEXT SIGNALS:**
1. {namespace}/{skill} — {reason}
2. {namespace}/{skill} — {reason}
3. {namespace}/{skill} — {reason}

**SESSION DELTA:** {signals added / gaps closed / new gaps, or FIRST RUN}

---

Empty state: if no signals exist, coverage = 0/N (show all namespaces),
verdict = NOT YET REACHED, populate NEXT SIGNALS from the P1 roadmap.
Write strategy.md to disk regardless of signal count.
```

---

## Variation Summary

| ID | Axis | Hypothesis | Length | Key Tradeoff |
|----|------|-----------|--------|-------------|
| V-01 | Role sequence | Named roles per phase prevent bleed | Long | Verbosity vs phase fidelity |
| V-02 | Output format | Dashboard table beats prose for scannability | Medium | Structure vs narrative flow |
| V-03 | Lifecycle emphasis | Explicit gates prevent partial runs | Long | Verbosity vs orchestration integrity |
| V-04 | Register (conversational) + Inertia framing | Naming the easy path increases honest gap reporting | Medium | Tone vs precision |
| V-05 | Compressed format + Implicit lifecycle | Minimal form scores on par with verbose on C-01–C-05 | Short | Brevity vs explicit guidance |
