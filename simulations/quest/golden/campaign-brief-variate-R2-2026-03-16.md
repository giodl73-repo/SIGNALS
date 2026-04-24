---
skill: quest-variate
skill_target: campaign-brief
round: 2
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-brief-rubric-v2-2026-03-16.md
---

# Variations — campaign-brief / Round 2

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

**R1 recap:** V-04 and V-05 tied at 75/100. V-05 won on all-essential-PASS. Both scored
FAIL on C-09 (session delta) and FAIL/PARTIAL on C-10 (confidence level). V-04 was the
strongest C-07/C-11 performer. V-02's gate structure was the strongest C-13 signal.

**R2 rubric adds:** C-11 (commit-risk grounding per gap), C-12 (prose confinement),
C-13 (incompleteness detection). Max score is now 130.

**R2 targets:** Close the C-09 and C-10 gaps that every R1 variation missed. Confirm
C-11/C-12/C-13 when structurally combining winners. The aspirational tier is now
50 points — as large as the essential tier. A variation that misses all aspirational
criteria cannot exceed 80/130.

---

## Variation axes selected

- **Single-axis:** Session delta (V-01), Commit-risk grounding (V-02), Confidence
  engineering (V-03)
- **Combined:** R1 winner synthesis — V-05 blocks + V-04 inertia (V-04), Full
  aspirational sweep (V-05)

---

## V-01 — Axis: Session delta (C-09 — explicit record of what changed this session)

**Hypothesis:** Adding a DELTA block positioned immediately after TOPIC — before the
current strategy and status — orients the team to what they are picking up from.
The block compares the current state to the most recent prior campaign-brief: signals
added, gaps closed, and verdict shift. C-09 becomes deterministic (structural block with
named fields). Placing DELTA second — not last — makes the session progress the *frame*
for reading the current dashboard, not an afterthought. The structural requirement that
DELTA appears even on the first run ("prior_brief: NONE — first run") ensures the
pattern is never silently skipped.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

---

Run the five phases in order. Produce exactly these blocks:

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
[DELTA]
prior_brief:   <filename of most recent prior campaign-brief, or NONE>
prior_date:    <date of prior brief, or NONE>
prior_verdict: <prior verdict status (READY | NOT READY | CONDITIONAL), or NONE>

signals_added:
  - <ns>/<artifact>  <date>
  (or: none)

gaps_closed:
  - <ns>/<skill>/<item>  (was: BLOCKING | OPTIONAL)
  (or: none)

verdict_shift: NO CHANGE | IMPROVED | DEGRADED — <one sentence if changed, or N/A>
```

Execution: Glob `simulations/{{topic}}/campaign-brief-*.md` to find the most recent
prior brief. Extract its STATUS block (found/missing) and VERDICT block. Compare to
current state. If this is the first run, write:
  prior_brief: NONE — first run
and mark all remaining delta fields as N/A.

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

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. Every planned
signal must appear in either found or missing. An empty missing list is valid only
when coverage = 100%.

---

```
[STORY]
<2-4 paragraphs. What do the existing signals say together? What do the gaps leave
uncertain? Do not list artifacts — synthesize.>

confidence: LOW | MEDIUM | HIGH — <one-sentence rationale>
```

Execution: Synthesize STATUS findings into a coherent narrative. The story must address
the gaps, not ignore them.

---

```
[VERDICT]
status:    READY | NOT READY | CONDITIONAL
rationale: <one sentence>

blocking:
  - <item>: <why it blocks>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY. State the verdict before the gap lists. A CONDITIONAL
verdict must name the condition explicitly.

---

Write all six blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

The file must contain all six blocks in the order:
TOPIC, DELTA, STRATEGY, STATUS, STORY, VERDICT.

---

## V-02 — Axis: Commit-risk grounding (C-11 — per-gap "what if we commit without this?")

**Hypothesis:** V-04 in R1 introduced inertia as a general orientation ("the primary
competitor is inertia"). That produced strong C-07 but left C-11 as a judgment call —
the framing was theme-level, not per-gap. V-02 for R2 makes commit-risk grounding
*structural and mandatory per gap*: every blocking entry in the MISSING section must
answer two named questions: (1) what assumption are we making if we commit today? and
(2) what specific outcome becomes more likely? This forces decision-stakes reasoning
at the item level, not just at the dashboard level. A gap that cannot answer these
questions with a real consequence is re-classified as optional. The two-question
structure makes the rationale reproducible and prevents hand-waving.

---

You are running `campaign-brief` for topic: `{{topic}}`.

`campaign-brief` is a decision-support dashboard. Its purpose is not signal inventory
for its own sake — it is to tell the team whether they have enough evidence to commit.
Every gap that belongs in the blocking category must justify that placement with
specific commit-risk reasoning.

Output format: structured dashboard with named sections. Prose is confined to the
STORY section. All other sections are structured data.

---

### STEP 1 — Register (topic-new)

Glob `simulations/TOPICS.md`. Confirm or create the entry for `{{topic}}`.

Required output:
```
TOPIC:  <name>
DATE:   <registration date>
INTENT: <one sentence describing what decision this topic is building toward>
STATUS: NEW | ACTIVE | COMPLETE
```

Do not proceed to Step 2 until this block is present.

---

### STEP 2 — Load strategy (topic-plan)

Glob `simulations/{{topic}}/strategy.md`. Load if present; generate if absent.

Required output: strategy table with columns Namespace | Skill | Item | Priority | Owner.
Minimum 3 rows.

---

### STEP 3 — Score coverage with commit-risk grounding (topic-status)

Glob `simulations/**/{{topic}}-*`. Match against strategy.

For every **blocking** missing signal, answer both questions:
1. **Assumption:** If we commit today without this signal, what are we silently assuming?
2. **Consequence:** If that assumption is wrong, what specifically happens?

A missing signal that cannot answer Question 2 with a concrete outcome is optional,
not blocking. Reclassify it accordingly.

Required output:
```
FOUND (X signals):
  <ns>/<artifact>  <date>
  ...

MISSING (Y signals):

  BLOCKING:
    - <ns>/<skill>/<item>
      Assumption:   <what the team is implicitly accepting if they commit today>
      Consequence:  <what outcome becomes more likely if the assumption is wrong>
    ...

  OPTIONAL:
    - <ns>/<skill>/<item>
      Risk:  <what is accepted by skipping — no assumption/consequence required>
    ...

COVERAGE: X/(X+Y) = Z%
```

The BLOCKING section is required even when empty. If empty, write:
`BLOCKING: none — all remaining gaps are optional`.

---

### STEP 4 — Write the narrative (topic-story)

Synthesize all findings into a narrative arc. Do not re-enumerate artifacts.

Address in sequence:
1. What case do the existing signals make together?
2. What do the blocking gaps leave genuinely uncertain — what assumption set remains
   untested?
3. What is the team's real decision exposure if they commit on today's evidence?

Assign a confidence level with rationale.

Required output:

**Narrative:** (2-4 paragraphs)

**Confidence:** LOW | MEDIUM | HIGH
*Rationale:* (one sentence — name the specific evidence condition driving the level)

**Verdict:** READY | NOT READY | CONDITIONAL
*Rationale:* (one sentence)

**Blocking gaps** (must fill before commit):
- <item>: <assumption + consequence, abbreviated>

**Optional gaps** (can ship without):
- <item>: <risk accepted>

---

Write the complete dashboard to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

The artifact must contain all four steps' outputs in order. A step with no output
is an incomplete dashboard.

---

## V-03 — Axis: Confidence engineering (C-10 — multi-dimensional confidence with scored dimensions)

**Hypothesis:** Every R1 variation scored FAIL or PARTIAL on C-10. The problem: either
confidence was absent entirely, or it appeared as a hedging phrase in prose (PARTIAL)
rather than a named, reasoned field. V-03 engineers C-10 structurally by introducing
a three-dimension confidence rubric — signal breadth, signal depth, gap severity —
each rated 1-3, with an overall confidence derived from the average. This makes
confidence (a) deterministic (it cannot be omitted when the table must be filled),
(b) auditable (the team can inspect the dimension scores), and (c) calibrated (the
derived average removes guessing). The dimension table is part of the STORY block,
keeping prose confinement intact for C-12.

---

You are running `campaign-brief` for topic: `{{topic}}`.

`campaign-brief` delivers a complete topic dashboard: what signals exist, what is
missing, and what the evidence says about readiness to commit. The dashboard closes
with a calibrated confidence assessment and readiness verdict.

Output format: structured dashboard with named sections. Prose synthesis is confined
to the STORY section. All other sections are structured data.

---

### Phase 1 — Register (topic-new)

Glob `simulations/TOPICS.md`. Confirm or create the `{{topic}}` entry.

Output:
```
TOPIC:  <name>
DATE:   <registration date>
INTENT: <one sentence>
STATUS: NEW | ACTIVE | COMPLETE
```

---

### Phase 2 — Signal strategy (topic-plan)

Glob `simulations/{{topic}}/strategy.md`. Load or generate the planned signal list.

Output: table (Namespace | Skill | Item | Priority | Owner). Minimum 3 rows.

---

### Phase 3 — Coverage status (topic-status)

Glob `simulations/**/{{topic}}-*`. Match against strategy.

Output:

**Signals found:**
| Namespace | Artifact | Date |
|-----------|----------|------|
| ...       | ...      | ...  |

**Signals missing:**
| Namespace | Skill | Item | Priority |
|-----------|-------|------|----------|
| ...       | ...   | ...  | ...      |

**Coverage:** X of Y planned signals present (Z%).

If any namespace in the strategy has zero found signals, it must appear in the
missing table with all planned items. An empty missing table is valid only when
coverage = 100%.

---

### Phase 4 — Narrative and confidence assessment (topic-story)

**Narrative:** (2-4 paragraphs synthesizing what the signals say together. Do not
enumerate artifacts — synthesize the case the evidence makes. Address what the gaps
leave uncertain and what the team is risking if they commit on current evidence.)

**Confidence assessment:**

Rate each dimension on a 1–3 scale:

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Signal breadth | 1 (1–2 ns) / 2 (3–5 ns) / 3 (6+ ns) | How many namespaces have at least one signal? |
| Signal depth | 1 (no corroboration) / 2 (some) / 3 (strong) | Do multiple signals in the same namespace corroborate? |
| Gap severity | 1 (critical blocking gaps) / 2 (moderate) / 3 (none or optional only) | How severe are the remaining gaps? |

**Average:** (breadth + depth + severity) / 3 = X.X

**Overall confidence:**
- LOW if average < 1.7
- MEDIUM if average 1.7–2.3
- HIGH if average > 2.3

*Confidence level:* LOW | MEDIUM | HIGH
*Narrative rationale:* (one sentence naming which dimension drives the level)

---

**Verdict:** READY | NOT READY | CONDITIONAL
*Rationale:* (one sentence)

**Blocking gaps** (must fill before commit):
- <item>: <why it blocks>

**Optional gaps** (can ship without):
- <item>: <risk if absent>

---

Write the complete dashboard to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

---

## V-04 — Axes: V-05 blocks + V-04 inertia framing (R1 structural winner + R1 content winner)

**Hypothesis:** V-05 from R1 won the essential tier outright (all 5 PASS) via its
terminal block structure. V-04 from R1 produced the strongest C-07/C-11 performance
via inertia framing. These two axes did not co-occur in R1. Combining them should
deliver: full essential PASS (from V-05 block structure), strong C-06/C-07/C-11
(from V-04 inertia), C-12 PASS (prose confined to STORY by block identity), and
C-13 PASS (absent block is visually obvious incompleteness). The combination
increases expected score from 75 to ~100+/130. The variation still lacks C-09
(delta) and C-10 (confidence dimension table) — those are the ceiling differentiators
targeted by V-05 in this round.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Each phase produces one structured block.
Prose is confined to the STORY block. All other blocks are structured data.
Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

**THE PRIMARY COMPETITOR IS INERTIA.** The team's alternative to gathering more signals
is to commit now on incomplete evidence. Every blocking gap must name the commit-risk —
what assumption the team is silently making if they ship today without that signal.

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

  BLOCKING (commit with unknown):
    - <ns>/<skill>/<item>
      Inertia risk: <what happens if we commit today without this signal?>
    ...

  OPTIONAL (can ship and learn):
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy.
For every blocking missing signal, the `Inertia risk:` field is required — not the
label alone. State specifically what the team is assuming if they commit today.
An empty BLOCKING section is valid only when all remaining gaps are genuinely optional;
state this explicitly: `BLOCKING: none — all gaps are optional`.

---

```
[STORY]
<2-4 paragraphs. What do the existing signals say together? What do the blocking gaps
leave genuinely uncertain? What is the team's real exposure if they commit on current
evidence? Do not list artifacts — synthesize the case the evidence makes.>

confidence: LOW | MEDIUM | HIGH — <one-sentence rationale>
```

Execution: Synthesize STATUS findings. The narrative must address what the inertia risk
means across the blocking gap set as a whole — not per gap (that is STATUS's job), but
as a pattern: what class of unknowns remains, and what that means for the commit
decision.

---

```
[VERDICT]
status:       READY | NOT READY | CONDITIONAL
rationale:    <one sentence>
inertia_cost: <one sentence — what the team is specifically risking if they commit now>

blocking:
  - <item>: <why it blocks>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY. The `inertia_cost` field is required even when verdict
is READY — state that the remaining risk is acceptable and why. A CONDITIONAL verdict
must name the condition and what satisfies it.

---

Write all five blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

The file must contain all five blocks in the order: TOPIC, STRATEGY, STATUS, STORY, VERDICT.

---

## V-05 — Axes: Full aspirational sweep (V-05 base + C-09 delta + C-10 confidence dimensions + C-11 inertia per gap)

**Hypothesis:** No R1 variation scored above 75/100 under the v1 rubric. Under v2 (130
points), the aspirational tier is now 50 points — equal in weight to the essential tier.
A variation that passes all essentials (50) and recommended (30) but misses all
aspirational criteria scores only 80/130. V-05 targets all 13 criteria by engineering
each aspirational property structurally: DELTA block for C-09, confidence dimension
table in STORY for C-10, per-gap inertia fields in STATUS for C-11, prose confined to
STORY for C-12, terminal blocks making omission visible for C-13. This is the
maximalist variation — it tests whether all 13 criteria can co-exist without
overloading the skill prompt.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block.
All other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

**THE PRIMARY COMPETITOR IS INERTIA.** Every blocking gap must name the commit-risk —
what assumption the team is silently making if they ship today without that signal.

---

Run the six phases in order. Produce exactly these blocks:

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
[DELTA]
prior_brief:   <filename of most recent prior campaign-brief, or NONE>
prior_verdict: <prior verdict status, or NONE>

signals_added:
  - <ns>/<artifact>  <date>
  (or: none)

gaps_closed:
  - <ns>/<skill>/<item>  (was: BLOCKING | OPTIONAL)
  (or: none)

verdict_shift: NO CHANGE | IMPROVED | DEGRADED — <one sentence if changed, or N/A>
```

Execution: Glob `simulations/{{topic}}/campaign-brief-*.md` to find the most recent
prior brief. Extract its STATUS block (found/missing) and VERDICT status. Compare to
current state to produce the delta. If this is the first run, write:
  prior_brief: NONE — first run
and mark all remaining delta fields as N/A. This block is required on first run.

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

  BLOCKING (commit with unknown):
    - <ns>/<skill>/<item>
      Inertia risk: <what happens if we commit today without this signal?>
    ...

  OPTIONAL (can ship and learn):
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking missing signal, the `Inertia risk:` field is required. A gap with no
articulable inertia risk is optional. An empty BLOCKING section must be stated
explicitly: `BLOCKING: none — all gaps are optional`.

---

```
[STORY]
<2-4 paragraphs. What do the existing signals say together? What do the blocking gaps
leave genuinely uncertain? What is the team's real exposure if they commit on current
evidence? Do not list artifacts — synthesize.>

confidence_dimensions:
  | Dimension      | Score (1-3) | Rationale |
  |----------------|-------------|-----------|
  | Signal breadth | 1/2/3       | Namespaces with ≥1 signal (1=1-2, 2=3-5, 3=6+) |
  | Signal depth   | 1/2/3       | Cross-namespace corroboration (1=none, 2=some, 3=strong) |
  | Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/optional) |

  average: X.X
  confidence: LOW (<1.7) | MEDIUM (1.7–2.3) | HIGH (>2.3)
  rationale: <one sentence naming the binding dimension>
```

Execution: Synthesize STATUS findings. The narrative addresses what the inertia risk
means as a pattern across the blocking gaps. Confidence dimensions must be scored from
STATUS data — not asserted from feeling.

---

```
[VERDICT]
status:       READY | NOT READY | CONDITIONAL
rationale:    <one sentence>
inertia_cost: <one sentence — what specifically is risked if the team commits now>

blocking:
  - <item>: <why it blocks>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY. `inertia_cost` is required at every verdict status —
even READY ("remaining risk is X and is acceptable because Y"). A CONDITIONAL verdict
must name the condition and what satisfies it.

---

Write all six blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

The file must contain all six blocks in the order:
TOPIC, DELTA, STRATEGY, STATUS, STORY, VERDICT.

---

**Key differentiators to watch in scoring:**

- **V-01** is the only variation with a dedicated DELTA block and no other aspirational
  additions — cleanest C-09 test, no confounds.
- **V-02** is the only variation where commit-risk grounding is per-gap and
  *structurally mandatory* via named fields (Assumption + Consequence). Strongest C-11
  mechanism in the set.
- **V-03** is the only variation with a scored confidence dimension table — the
  strongest C-10 mechanism. Trade-off: the table adds length; watch whether it
  crowds the narrative.
- **V-04** is the cleanest combination from R1 without adding new aspirational
  complexity — tests whether combining the two R1 winners lifts the score predictably.
- **V-05** is the first variation designed to target all 13 criteria simultaneously.
  The ceiling test: does engineering all 13 properties co-exist without making the
  prompt unwieldy?
