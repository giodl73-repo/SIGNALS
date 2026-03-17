---
skill: quest-variate
skill_target: campaign-brief
round: 1
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-brief-rubric-v1-2026-03-16.md
---

# Variations — campaign-brief / Round 1

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

`campaign-brief` orchestrates four sub-skills in sequence — topic-new (register),
topic-plan (plan signals), topic-status (current coverage), topic-story (narrative
synthesis) — and delivers a complete topic dashboard. It bookends signal-gathering
sessions: run at the start to orient, run at the end to assess readiness.

The rubric's diagnostic core is C-02/C-03 (signal inventory + gap identification) and
C-04 (narrative arc that synthesizes signals *together*). The core failure mode to
prevent: a flat artifact list with no gaps named and no synthesis offered — which adds
no value over running `topic-status` alone.

R1 tests three single-axis variations (output format, lifecycle emphasis, phrasing
register) and two combinations (role sequence + inertia framing; output format +
lifecycle emphasis).

---

## V-01 — Axis: Output format (dashboard template declared upfront)

**Hypothesis**: Declaring the complete output template skeleton before running any
sub-skill forces the model to populate a known structure rather than invent one. This
makes C-02 (signal inventory), C-03 (gap identification), and C-08 (scannable format)
deterministic by structure. A model that sees named slots before it starts will fill
them; a model that invents its output shape often omits gap sections entirely.

---

You are running `campaign-brief` for topic: `{{topic}}`.

`campaign-brief` is the topic narrative campaign. It orchestrates four sub-skills in
sequence and delivers a complete topic dashboard. Run it at the start of a session to
orient, and at the end to assess readiness for commit.

**Your output must match this dashboard template exactly. Populate each section in
order. Do not omit any section.**

```
## Topic Brief — {{topic}}
Registered: <date>
Intent: <one-sentence description of what this topic is investigating>
Status: <ACTIVE | NEW | COMPLETE>

---

## Phase 1 — Registration (topic-new)
<Confirm: existing entry in TOPICS.md, or register a new one. Show name, date, intent.>

---

## Phase 2 — Signal Strategy (topic-plan)
Planned signals:
| Namespace | Skill | Item name | Priority | Status |
|-----------|-------|-----------|----------|--------|
| ...       | ...   | ...       | ...      | ...    |

---

## Phase 3 — Coverage Status (topic-status)
Signals found:
| Namespace | Artifact | Date |
|-----------|----------|------|
| ...       | ...      | ...  |

Signals missing (planned but absent):
| Namespace | Skill | Item name | Priority |
|-----------|-------|-----------|----------|
| ...       | ...   | ...       | ...      |

Coverage: X of Y planned signals present (Z%).

---

## Phase 4 — Narrative Arc (topic-story)
<2-4 paragraph synthesis. State what the signals say *together* toward the feature
decision. Do not list artifacts. Synthesize: what do we know, what do we not know,
and what does the gap mean for the commit decision?>

Narrative confidence: <LOW | MEDIUM | HIGH> — <one-sentence rationale>

---

## Readiness Verdict
<READY | NOT READY | CONDITIONAL>
Rationale: <one sentence>

Blocking gaps (must fill before commit):
- <item> — <why it blocks>

Optional gaps (can ship without):
- <item> — <what risk it carries>
```

**Execution steps:**

1. **topic-new**: Glob `simulations/TOPICS.md`. If `{{topic}}` exists, confirm the
   entry. If absent, create one with name, date, and intent. Populate Phase 1.

2. **topic-plan**: Glob `simulations/{{topic}}/strategy.md`. If absent, generate a
   signal strategy: list the planned signals across namespaces needed to commit on
   `{{topic}}`. Populate Phase 2.

3. **topic-status**: Glob `simulations/**/{{topic}}-*`. Match found artifacts against
   the strategy. Compute coverage. Populate Phase 3. Name every missing signal — do
   not leave the missing table empty if the topic is incomplete.

4. **topic-story**: Synthesize Phase 3 findings into a coherent narrative. The
   synthesis must state what the signals say *together*, not list them individually.
   Assign a confidence level. Populate Phase 4 and the Readiness Verdict.

Output the completed dashboard. Write the artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

---

## V-02 — Axis: Lifecycle emphasis (explicit phase gates with required-output checkpoints)

**Hypothesis**: Naming each sub-skill as a labeled phase with a mandatory "Required
output:" checkpoint after it prevents any phase from being silently skipped (C-01).
When the model must produce a named deliverable at each gate before advancing, topic
registration (C-05) and signal inventory (C-02) become deterministic — skipping them
produces an obviously incomplete output rather than a quietly thin one.

---

You are running `campaign-brief` for topic: `{{topic}}`.

`campaign-brief` orchestrates the full topic narrative campaign through four phases.
Complete each phase in order. Each phase has a required output — do not advance to
the next phase until that output is present in your response.

---

### PHASE 1 — Register (topic-new)

Glob `simulations/TOPICS.md`. Check whether `{{topic}}` is already registered.

- If registered: quote the existing entry (name, date, intent, status).
- If not registered: create the entry. Write name, today's date, and a one-sentence
  intent describing what decision this topic is building toward.

**Required output for Phase 1:**
```
TOPIC: <name>
DATE:  <registration date>
INTENT: <one sentence>
STATUS: <NEW | ACTIVE | COMPLETE>
```

Do not proceed to Phase 2 until this block is present.

---

### PHASE 2 — Plan (topic-plan)

Glob `simulations/{{topic}}/strategy.md`. If a strategy exists, display it. If absent,
generate the signal strategy now: for each namespace relevant to `{{topic}}`, list the
signals needed before commit. Include namespace, skill, item name, priority
(essential / recommended / optional), and owner role.

**Required output for Phase 2:**
A table with columns: Namespace | Skill | Item | Priority | Owner
Minimum 3 rows. If the strategy already exists, reproduce it from disk.

---

### PHASE 3 — Status (topic-status)

Glob `simulations/**/{{topic}}-*` to find all existing signal artifacts.

For each artifact found: list namespace, artifact filename, and date.
Then: compare found artifacts against the Phase 2 strategy. Identify every planned
signal that has no matching artifact. List them explicitly — do not omit gaps.

**Required output for Phase 3:**
```
FOUND (X signals):
  - <namespace>: <artifact-name> (<date>)
  ...

MISSING (Y signals):
  - <namespace>/<skill>: <item-name> [BLOCKING | OPTIONAL]
  ...

COVERAGE: X / (X+Y) = Z%
```

A missing section with zero items is only valid if all planned signals are present.
If the topic is new, all planned signals are missing — list them.

---

### PHASE 4 — Story (topic-story)

Synthesize all Phase 3 findings into a narrative arc. Do not enumerate artifacts.
Answer: What do the existing signals say *together*? What question do the missing
signals leave unanswered? What does the gap mean for the commit decision?

**Required output for Phase 4:**

**Narrative:** (2-4 paragraphs synthesizing the signals toward a decision)

**Confidence:** LOW | MEDIUM | HIGH
*Rationale:* (one sentence explaining the confidence level)

**Verdict:** READY | NOT READY | CONDITIONAL
*Rationale:* (one sentence)

**Blocking gaps** (must resolve before commit):
- <item>: <why it blocks the decision>

**Optional gaps** (can ship without):
- <item>: <what risk it carries>

---

After completing all four phases, write the full dashboard artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

The artifact must contain the output of all four phases in order.

---

## V-03 — Axis: Phrasing register (conversational imperative, second-person narrator voice)

**Hypothesis**: Addressing the model as the campaign narrator in second-person
imperative ("Your first act is to check whether this topic is registered...") reduces
task-ownership ambiguity. A model cast as the narrator of a story is more likely to
produce synthesis (C-04) than a model given a procedure list. The conversational
register also tends to produce shorter, denser prose — which benefits C-08 scannability.

---

You are the campaign narrator for topic: `{{topic}}`.

Your job is to run the full brief — registration, strategy, coverage, story — and
hand the team a complete picture of where this topic stands. They need to walk away
knowing what evidence exists, what's missing, and whether they can commit.

Here's what you do, in order:

**First: check whether this topic is registered.**
Look in `simulations/TOPICS.md`. If `{{topic}}` is there, note its name, start date,
and intent. If it isn't, register it now — name it, date it, write a sentence describing
what decision the investigation is building toward. You need a registered topic before
anything else makes sense.

**Second: confirm the signal strategy.**
Check `simulations/{{topic}}/strategy.md`. This file is the editorial plan — the list
of signals the team said they needed before committing. If it exists, use it. If it
doesn't, write it: for each namespace that matters to `{{topic}}`, name the signals
needed, mark each one essential, recommended, or optional, and note who owns each one.
This is the checklist you'll score coverage against.

**Third: score the coverage.**
Glob `simulations/**/{{topic}}-*` and find every artifact that exists. Then go through
the strategy list and mark what's present and what's absent. Be specific — don't say
"some signals are missing." Name each missing signal. Group by namespace. Note whether
each gap is blocking (the team can't answer the commit question without it) or optional
(they can ship and learn).

**Fourth: tell the story.**
Now synthesize. Don't list the artifacts again — the coverage table already did that.
Instead, tell the team what the signals say *together*. What picture do they form?
What does the missing evidence leave uncertain? And given all of that, what's your
verdict: are they ready to commit, not ready, or conditionally ready?

Give the narrative a confidence level — low, medium, or high — and say why. A lot of
evidence pointing the same direction is high confidence. A few signals with a major
gap is low confidence. Don't leave it unstated.

**Format the output as a dashboard.** Use section headers. Put the coverage table in
Phase 3. Put the narrative in Phase 4. End with the verdict on its own line. Make it
scannable — the team shouldn't have to read every paragraph to find the readiness call.

Write the artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

---

## V-04 — Axes: Role sequence + Inertia framing (status-before-story; inertia as commit-risk anchor)

**Hypothesis**: Running topic-status before topic-story — so the model has the full
coverage map in its context when it synthesizes the narrative — raises C-04 depth and
C-07 gap prioritization quality. When gaps are known before the narrative is written,
the synthesis can address what the gaps *mean* rather than discovering them
retrospectively. The inertia framing — "what happens if we commit without this signal?"
— forces C-07 blocking/optional prioritization to be grounded in real commit risk
rather than abstract completeness.

---

You are running `campaign-brief` for topic: `{{topic}}`.

`campaign-brief` produces a topic dashboard. The sequence matters: you gather the full
picture of what exists and what is missing *before* synthesizing the narrative, so the
story is informed by the gaps, not surprised by them.

**THE PRIMARY COMPETITOR IS INERTIA.** The team's alternative to gathering more signals
is to commit now on what they have — or to do nothing. Every gap analysis must name the
commit-risk of proceeding without that signal, not just note that it is absent. A gap
that doesn't affect the commit decision is optional. A gap that leaves a core question
unanswered is blocking.

---

### Step 1 — Register the topic

Glob `simulations/TOPICS.md`. Confirm or create the entry for `{{topic}}`.

Output:
```
TOPIC: <name>  |  DATE: <date>  |  STATUS: <status>
INTENT: <one sentence>
```

---

### Step 2 — Load the signal strategy

Glob `simulations/{{topic}}/strategy.md`. If present, load it. If absent, generate it:
list planned signals by namespace, with skill, item name, and priority. This is the
commit checklist.

Output: strategy table (Namespace | Skill | Item | Priority | Owner).

---

### Step 3 — Score coverage (topic-status)

Glob `simulations/**/{{topic}}-*`. Match found artifacts against the strategy.

Output:
```
FOUND (X):
  <namespace>/<artifact>  <date>
  ...

MISSING (Y):
  <namespace>/<skill>/<item>  [BLOCKING | OPTIONAL]  — <commit-risk if absent>
  ...

COVERAGE: X/(X+Y) = Z%
```

For every missing signal, state the commit-risk: what question does this gap leave
unanswered if the team commits today? A missing signal with no commit-risk consequence
is optional. A missing signal that leaves a core assumption untested is blocking.

---

### Step 4 — Synthesize the narrative (topic-story)

Now that you have the coverage map, write the story. The narrative must answer:
1. What do the existing signals say together — what case do they make?
2. What do the blocking gaps leave uncertain — what assumption remains untested?
3. Given that uncertainty, what is the team's real exposure if they commit now?

Do not enumerate artifacts in the narrative. The coverage table exists for that.

Assign confidence: LOW | MEDIUM | HIGH, with a one-sentence rationale.

End with the readiness verdict:

```
VERDICT: READY | NOT READY | CONDITIONAL
Rationale: <one sentence>

Inertia risk: <one sentence describing the cost of committing now vs. waiting>
```

---

Write the complete dashboard to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

---

## V-05 — Axes: Output format + Lifecycle emphasis (terminal-style compact output, strict economy)

**Hypothesis**: Combining strict compact format (each phase produces exactly one
structured block, no discursive prose except in the narrative phase) with explicit
lifecycle enforcement produces the most scan-friendly output (C-08) while still
enforcing orchestration completeness (C-01). The terminal-style format creates C-08
compliance by default — there is no room for a phase to get buried in prose — and
makes the readiness verdict (C-06) the closing line of the dashboard, where the eye
naturally lands.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Each phase produces one structured block.
Prose is confined to the STORY block. All other blocks are structured data.
Do not add narrative commentary outside the designated STORY block.
Do not skip any phase — an absent block is an incomplete dashboard.

---

Run the four phases in order. Produce exactly these blocks:

---

```
[TOPIC]
name:    {{topic}}
date:    <registration date>
intent:  <one sentence>
status:  NEW | ACTIVE | COMPLETE
source:  TOPICS.md (existing) | TOPICS.md (created)
```

Execution: Glob `simulations/TOPICS.md`. Confirm existing entry or create new one.
This block must be present before any other block.

---

```
[STRATEGY]
source: simulations/{{topic}}/strategy.md (<found> | <generated>)

| ns        | skill           | item                    | priority    |
|-----------|-----------------|-------------------------|-------------|
| <ns>      | <skill>         | <item-name>             | essential   |
| ...
```

Execution: Glob `simulations/{{topic}}/strategy.md`. Load or generate.
Minimum 3 rows. Every row must have all four columns populated.

---

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>
  ...

missing: Y signals
  <ns>/<skill>/<item>  BLOCKING | OPTIONAL
  ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy.
Every planned signal must appear in either the found or missing list.
An empty missing list is valid only when coverage = 100%.

---

```
[STORY]
<2-4 paragraphs. What do the existing signals say together? What do the gaps leave
uncertain? Do not list artifacts — synthesize.>

confidence: LOW | MEDIUM | HIGH — <one-sentence rationale>
```

Execution: Synthesize STATUS findings into a coherent narrative.
The story must address the gaps, not ignore them.

---

```
[VERDICT]
status:   READY | NOT READY | CONDITIONAL
rationale: <one sentence>

blocking:
  - <item>: <why>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY. State the verdict before the gap lists.
A CONDITIONAL verdict must name the condition explicitly.

---

Write all five blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

The file must contain all five blocks in the order: TOPIC, STRATEGY, STATUS, STORY, VERDICT.
