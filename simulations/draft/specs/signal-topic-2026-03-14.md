# Topic Specification

**Topic**: signal
**Namespace**: /topic:
**Skills**: 6
**Default mode**: Lightweight
**Audience**: Anyone contributing to a shared feature investigation -- PMs, developers, architects,
team leads. The topic namespace is the vertical layer that ties everything else together.

## Purpose

Program orchestrates left to right -- scout to draft to review to trace to listen, stage by stage.
Topic manages top to bottom -- the accumulating narrative of what we know about a feature, from
first signal to design commit.

Every artifact produced by any namespace skill is a signal toward the topic's story. The topic
namespace answers the question every contributor wants answered:

> "Where are we in this story, what have we learned, and what do we still need?"

/topic: is not a simulation skill. It is the editorial layer above all namespaces. It gives each
contributor a sense of progress toward the complete feature narrative -- so that every signal they
add lands in context, not in a void.

---

## The Signal Model

A **signal** is any artifact that contributes to a topic's story. Signals come from every namespace:

| Namespace | Signal type |
|-----------|-------------|
| /scout:   | Market signal, feasibility signal, requirements signal |
| /draft:   | Design signal (spec, proposal) |
| /review:  | Validation signal (user, customer, design, code) |
| /flow:    | Process signal |
| /trace:   | System signal |
| /prove:   | Evidence signal (hypothesis, synthesis) |
| /listen:  | Adoption signal, feedback signal |
| /topic:   | Story signal (synthesis, echo) |

Every file named `{topic}-{item}-{date}.md` is a signal. The item names the angle. The topic
ties it to the story. The date orders it in the timeline.

**The topic is complete when all planned signals are gathered and a story exists.**

---

## Skills

### /topic:new

**What**: Register a new topic, name its strategy, and plan the signals needed to tell the
complete story and reach a design commit.
**Input**: Topic name, one-line description of the feature being investigated, and (optionally)
a target outcome (design commit, go/no-go decision, spec draft, etc.).
**Output**: Entry in TOPICS.md, a strategy file at `simulations/{topic}/strategy.md` listing
the planned signals and their rationale.
**Lifecycle**:
- Setup: Confirm topic name (short, memorable, no spaces -- e.g., `frogs`, `atlas`, `sim`).
  Confirm the one-line description and target outcome.
- Execute: Generate a strategy for the topic. Based on the description and target outcome,
  recommend which namespaces and skills will produce the most useful signals. Group signals
  into: essential (needed before design commit), recommended (deepen confidence), optional
  (only if time allows). Assign each signal an owner role (PM, developer, architect, etc.).
- Findings: The strategy document. A table of planned signals with namespace, skill, item name,
  owner role, and priority (essential / recommended / optional).
- Amend: User adjusts the signal plan -- adds, removes, re-prioritizes. The strategy is the
  editorial plan for the topic's investigation.
**Lightweight**: Auto-generates a minimal essential-only signal plan from the topic description.
  User confirms or adjusts in one pass.
**Artifact**: `simulations/{topic}/strategy.md`
**Example**:
```
User: /topic:new frogs "Real-time CRM sync between Dynamics and Salesforce"
> Topic registered: frogs
> Target outcome: go/no-go decision on 6-month build

> ## Signal Plan (frogs)
>
> ### Essential signals (needed before design commit)
> | Signal | Namespace | Skill | Owner | Item |
> |--------|-----------|-------|-------|------|
> | Competitive landscape | /scout: | competitors | PM | frogs-competitors-2026-03-14.md |
> | Technical feasibility | /scout: | feasibility | Architect | frogs-feasibility-2026-03-14.md |
> | User walkthrough | /review: | users | PM/UX | frogs-users-2026-03-14.md |
> | State trace | /trace: | state | Developer | frogs-state-2026-03-14.md |
> | Customer adoption | /listen: | adoption | PM | frogs-adoption-2026-03-14.md |
>
> ### Recommended signals
> | Signal | Namespace | Skill | Owner | Item |
> |--------|-----------|-------|-------|------|
> | Requirements validation | /scout: | requirements | PM | frogs-requirements-2026-03-14.md |
> | Integration simulation | /flow: | integration | Developer | frogs-integration-2026-03-14.md |
> | Design review | /review: | design | Architect | frogs-design-2026-03-14.md |
>
> ### Optional signals
> | Signal | Namespace | Skill | Owner | Item |
> |--------|-----------|-------|-------|------|
> | Compliance check | /scout: | compliance | Compliance | frogs-compliance-2026-03-14.md |
> | Academic synthesis | /prove: | synthesize | Researcher | frogs-synthesis-2026-03-14.md |
>
> Strategy written: simulations/frogs/strategy.md
> TOPICS.md updated.
```

### /topic:status

**What**: Show the current state of a topic in the terminal -- signal coverage, open gaps,
readiness for target outcome.
**Input**: Topic name.
**Output**: Terminal display (not written to disk). For a written artifact, use /topic:report.
**Lifecycle** (Lightweight, always):
- Read the topic's strategy.md to get the planned signal list.
- Glob `simulations/**/{topic}-*` to find all signals gathered so far.
- Cross-reference: which planned signals exist, which are missing, which are unplanned additions.
- Compute coverage: essential signals covered / total essential signals.
- Assess readiness for the target outcome (e.g., "4/5 essential signals gathered -- ready to
  draft spec once state trace is complete").
**Output format**:
```
Topic: frogs — Real-time CRM sync (Dynamics <-> Salesforce)
Target: go/no-go decision
Coverage: 4/5 essential | 2/3 recommended | 0/2 optional

Essential signals:
  [x] frogs-competitors-2026-03-14.md  (PM, scout)
  [x] frogs-feasibility-2026-03-14.md  (Architect, scout)
  [x] frogs-users-2026-03-14.md        (PM/UX, review)
  [ ] frogs-state-2026-03-14.md        (Developer, trace) -- OPEN
  [x] frogs-adoption-2026-03-14.md     (PM, listen)

Readiness: ALMOST READY -- one essential signal missing (state trace).
Next step: /trace:state on the CRM sync state model.
```
**Artifact**: None written. Status is read-only, displayed only.

### /topic:report

**What**: Write a shareable status document for a topic -- same information as /topic:status
but as a file that can be linked, pasted, or sent.
**Input**: Topic name. Optional `--format teams` for compact ASCII card output.
**Output**: Written artifact at `simulations/{topic}/status-{date}.md`. With `--format teams`,
also prints a compact ASCII card to terminal for paste into Teams or a standup doc.
**Lifecycle** (Lightweight, always):
- Read strategy.md and glob all signals for the topic.
- Compute coverage (same as /topic:status).
- Write the status document in a format suitable for sharing: progress table, open signals
  with owners, readiness statement, recommended next step.
- If `--format teams`, also produce:

  Signal: frogs | 4/5 essential | ALMOST READY
  [x] competitors  [x] feasibility  [x] users
  [x] adoption     [ ] state-trace  <- open (Dev)
  Next: /signal:trace on CRM state model

**Artifact**: `simulations/{topic}/status-{date}.md`

### /topic:plan

**What**: Interactively plan or revise the signal strategy for a topic. Use when the initial
strategy needs updating -- new information arrived, scope changed, or signals revealed unexpected
dimensions that need coverage.
**Input**: Topic name. Optionally, new context (e.g., "we found a compliance requirement we
hadn't anticipated").
**Output**: Updated strategy.md.
**Lifecycle**:
- Read the current strategy.md and all gathered signals.
- Identify: what has changed since the strategy was written? What do gathered signals reveal
  that the plan didn't anticipate? What new dimensions need coverage?
- Propose updates to the signal plan (add, remove, re-prioritize, re-assign owners).
- User reviews and confirms. Strategy.md is updated.
**Artifact**: Updated `simulations/{topic}/strategy.md`

### /topic:story

**What**: Synthesize all gathered signals into a single narrative -- the current state of what
we know about this feature, written as a coherent story rather than a list of findings.
**Input**: Topic name. Optionally, a target audience for the story (PM, executive, architect).
**Output**: A narrative synthesis at `simulations/{topic}/{topic}-story-{date}.md` that tells:
- What we set out to understand
- What each signal revealed (key finding per signal, not exhaustive)
- What the signals say together (the pattern, the insight, the recommendation)
- What remains uncertain (open questions, missing signals)
- The recommendation: proceed, pause, pivot, or abandon
**Lifecycle**:
- Read all signals gathered for the topic (glob `simulations/**/{topic}-*`).
- Read the strategy to understand what questions the signals were meant to answer.
- Write the story in three parts: what we learned, what it means, what we recommend.
- The story is NOT a summary of each artifact. It is an editorial synthesis -- the author's
  voice interpreting the signals, not transcribing them.
**Artifact**: `simulations/{topic}/{topic}-story-{date}.md`
**Example opening**:
```
# The Frogs Story — Real-time CRM Sync
*As of 2026-03-14. 4 of 5 essential signals gathered.*

## What We Set Out to Understand
Could we build real-time bidirectional sync between Dynamics 365 and Salesforce in 6 months,
and would customers actually adopt it?

## What the Signals Say
The competitive landscape signal (frogs-competitors) revealed one surprise: no incumbent owns
this space cleanly. The three existing solutions (MuleSoft, Boomi, custom) all require 3+ months
of professional services to configure -- meaning a zero-config option has genuine white space.

The feasibility signal (frogs-feasibility) complicated this optimism...
```

### /topic:echo

**What**: After all essential signals are gathered, synthesize the unexpected findings -- the
things the signals revealed that the strategy didn't anticipate. This is the topic-level echo,
distinct from the program-level echo (which runs at the end of a program execution).
**Input**: Topic name.
**Output**: Echo artifact at `simulations/{topic}/{topic}-echo-{date}.md`
**What the echo asks**: "What did we learn that we didn't expect?"
- Not a summary of findings. A synthesis of surprises.
- Each unexpected finding is named, traced to its source signal, and assessed for impact
  on the design direction.
- The echo is the most valuable output of the topic investigation. It is what the next team
  that explores this topic most needs to read.
**Lifecycle** (always Lightweight -- the echo should be fast and sharp):
- Read all gathered signals.
- For each signal, identify: what did it reveal that the strategy didn't predict?
- Rank surprises by impact on the design direction.
- Write the echo: name each surprise, quote the signal that revealed it, assess impact.
**Artifact**: `simulations/{topic}/{topic}-echo-{date}.md`

---

## How Topic Relates to Program

| Dimension | /topic: | /program: |
|-----------|---------|-----------|
| Direction | Top to bottom | Left to right |
| Question | "What do we know about this feature?" | "How do we execute this investigation?" |
| Unit | Signal (one artifact per angle) | Stage (one skill per step) |
| Output | Story + Echo | Staged plan + execution gates |
| Lifecycle | Accumulates over time | Executes in sequence |
| Who runs it | Anyone contributing | The lead orchestrating the program |
| When | Ongoing, any time | Upfront, once per initiative |

**A topic can exist without a program.** Contributors add signals organically. The topic
accumulates. The story is told when enough signals exist.

**A program always has a topic.** The program's stages produce the signals. The topic tracks
their narrative. The program's echo and the topic's echo are the same document.

---

## Artifact Layout

```
simulations/
  TOPICS.md                         <- topic registry (name, description, started, status)
  {topic}/
    strategy.md                     <- signal plan (planned signals, owners, priorities)
    {topic}-story-{date}.md         <- narrative synthesis (latest /topic:story run)
    {topic}-echo-{date}.md          <- unexpected findings (latest /topic:echo run)
  scout/competitors/
    {topic}-competitors-{date}.md   <- signal: competitive landscape
  review/users/
    {topic}-users-{date}.md         <- signal: user walkthrough
  [all other namespace outputs]
```

Topic-scoped artifacts (story, echo, strategy) live in `simulations/{topic}/` because they span
all namespaces. Signal artifacts live in their namespace directory because they belong to that
skill's output space. The topic prefix ties them together: glob `{topic}-*` finds everything.

---

## Roles

No stock roles for /topic: skills. The topic namespace is editorial, not simulation. It reads
and synthesizes artifacts produced by other skills. The "role" is the author making sense of
the signals -- that is always the human (or the session lead).

---

## Cross-Namespace Integration

/topic: is the integrating layer across all namespaces:

- Every `{namespace}/{skill}/{topic}-{item}-{date}.md` artifact is a signal in the topic's story
- /topic:status discovers signals by globbing -- no registration required, no coupling to producers
- /topic:story reads all signals and synthesizes them -- skills produce, topic narrates
- /topic:echo runs after the story and asks what surprised us -- it is always the last thing written
- /program:plan can reference a topic's strategy as its signal checklist -- stages map to signals
