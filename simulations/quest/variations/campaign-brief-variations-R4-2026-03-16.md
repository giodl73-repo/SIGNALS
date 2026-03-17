Written to `simulations/quest/variations/campaign-brief-variations-R4-2026-03-16.md`.

---

## campaign-brief / Round 4 — Variations Summary

**Base:** R3 V-05 (140/150 on v3 rubric). Mapped to v4 rubric baseline: ~150/180.

**Remaining gaps (4 improvements, 30 pts):**
- C-04 PARTIAL → needs C-17 + C-18 jointly (+5)
- C-11 PARTIAL → needs dual `Assumption: / Consequence:` (+5)
- C-17 PARTIAL → needs explicit PERMITTED/NOT PERMITTED list (+10)
- C-18 PARTIAL → needs explicit three-question mandate (+10)

---

| Var | Axis | Key change | Expected score |
|-----|------|-----------|---------------|
| V-01 | C-17 only | PERMITTED/NOT PERMITTED list in STORY, no three-question | ~160/180 |
| V-02 | C-18 only | Three-question mandate in STORY, advisory prohibitions | ~160/180 |
| V-03 | C-11 only | `Assumption: / Consequence:` dual fields in FULL FORMAT + BLOCKING-DETAIL | ~160/180 |
| V-04 | C-17 + C-18 | Both STORY mechanisms, no C-11 change | ~170/180 |
| V-05 | C-11 + C-17 + C-18 | All four fixes simultaneously | **180/180** |

**The critical experiment:** V-01 and V-02 should each score C-04 PARTIAL independently, with V-04 scoring PASS — confirming the rubric's jointly-necessary claim. If either V-01 or V-02 achieves C-04 PASS alone, the claim needs revision before R5.

**Watch in scoring:** V-03's three-line FULL FORMAT entry (path + Assumption + Consequence vs. the old two-line path + Inertia) against the C-15 density ceiling. If the threshold of 4 entries degrades C-15, the R5 base may need to lower it to 3.
). Combine all three
axes in V-05 for the 180/180 ceiling attempt.

---

## Variation axes selected

- **Single-axis:** STORY prohibition list (V-01), STORY three-question structure
  (V-02), C-11 dual commit-risk fields (V-03)
- **Combined:** C-17 + C-18 jointly (V-04), full four-fix sweep — C-11 + C-17 +
  C-18 (V-05)

Base for all variations: R3 V-05 (eight-block pipeline: TOPIC, DELTA, STRATEGY,
STATUS, [BLOCKING-DETAIL], CONFIDENCE, STORY, VERDICT).

---

## V-01 — Axis: C-17 prohibition list (explicit PERMITTED/NOT PERMITTED in STORY, no three-question mandate)

**Hypothesis:** R3 V-05 had advisory STORY constraints ("Do not name artifact
filenames", "Do not restate confidence level"). Advisory phrasing is C-17 PARTIAL.
V-01 replaces the advisory text with an explicit PERMITTED/NOT PERMITTED list — the
structural form V-03 R3 used to achieve C-04 PASS. However, V-01 deliberately omits
the three-question sequential structure (C-18). The rubric states C-17 and C-18 are
jointly necessary for C-04 structural reliability: "a prohibition list without a
question sequence permits structured silence." V-01 should score C-17 PASS, C-18
FAIL, and C-04 PARTIAL — confirming the rubric's jointly-necessary claim. If V-01
scores C-04 PASS without the question sequence, the jointly-necessary claim is wrong
and R5 must investigate.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block.
All other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

**THE PRIMARY COMPETITOR IS INERTIA.** Every blocking gap must name the commit-risk —
what assumption the team is silently making if they ship today without that signal.

---

Run the phases in order. Produce exactly these blocks:

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
prior brief. Extract its STATUS (found/missing) and VERDICT. Compare to current state.
If this is the first run, write:
  prior_brief: NONE — first run
Mark all remaining delta fields as N/A. This block is required on first run.

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

**STATUS density contract:** Count blocking missing signals before formatting.
Use FULL format if blocking gaps <= 4. Use COMPRESSED format + [BLOCKING-DETAIL]
if blocking gaps > 4.

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>
  ...

missing: Y signals

  BLOCKING (commit with unknown):

  [FULL FORMAT — blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
    ...

  [COMPRESSED FORMAT — blocking gaps > 4 (see [BLOCKING-DETAIL] for full fields):]
    - <ns>/<skill>/<item> — <inertia risk, <=12 words>
    ...

  OPTIONAL (can ship and learn):
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking missing signal, `Inertia risk:` is required. A gap with no articulable
inertia risk is optional. State explicitly when empty:
  `BLOCKING: none — all gaps are optional`

If compressed format was triggered, produce immediately after STATUS:

```
[BLOCKING-DETAIL]
Full inertia fields for each compressed blocking entry:

  <ns>/<skill>/<item>
    Inertia risk: <full statement>
  ...
```

---

```
[CONFIDENCE]
| Dimension      | Score (1-3) | Rationale                                              |
|----------------|-------------|--------------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+)       |
| Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong) |
| Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/optional) |

average: (breadth + depth + severity) / 3 = X.X
level:   LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
binding: <the dimension that determines the level — lowest score, or tie-breaker>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically —
do not estimate. CONFIDENCE is a standalone block; do not embed inside STORY.

---

```
[STORY]
<Prose narrative only. Minimum 2 paragraphs. Maximum 4.

PERMITTED:
  - Paragraph prose.
  - References to signal categories by type (e.g., "the flow signals", "the
    feasibility evidence") — not artifact filenames.
  - Cross-signal reasoning: what patterns emerge across namespaces?
  - Discussion of the inertia risk as a pattern across the blocking gap set — what
    class of unknowns remains, not a per-gap accounting.

NOT PERMITTED:
  - Bullet lists or numbered lists of any kind.
  - Artifact filenames (those belong to STATUS).
  - Tables of any kind (confidence table belongs to CONFIDENCE).
  - The words LOW, MEDIUM, or HIGH to restate the confidence level
    (that belongs to CONFIDENCE).
  - Per-gap enumeration (that belongs to STATUS).

Write continuous interpretive prose. Do not use the three-question structure.>
```

Execution: Synthesize STATUS and CONFIDENCE findings into a coherent narrative arc.
STORY interprets the pattern; every other block owns its structured record.

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

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` is required at every
verdict status — even READY ("remaining risk is X and is acceptable because Y").
A CONDITIONAL verdict must name the condition and what satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-02 — Axis: C-18 three-question structure (explicit sequential mandate in STORY, no formal prohibition list)

**Hypothesis:** V-01 tests prohibition alone. V-02 tests structure alone. The rubric
states "a question sequence without prohibitions permits enumeration labeled as
synthesis." V-02 replaces the R3 V-05 STORY instructions with an explicit
three-question sequential mandate: (1) what case do signals make together, (2) what
do gaps leave uncertain, (3) what is the team's real exposure. But V-02 retains
advisory phrasing for the prohibitions ("do not" vs. explicit NOT PERMITTED list).
Expected scores: C-18 PASS, C-17 PARTIAL, C-04 PARTIAL. If C-04 emerges as PASS
despite the absence of C-17, the rubric's jointly-necessary claim requires revision.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block.
All other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

**THE PRIMARY COMPETITOR IS INERTIA.** Every blocking gap must name the commit-risk —
what assumption the team is silently making if they ship today without that signal.

---

Run the phases in order. Produce exactly these blocks:

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
prior brief. Extract its STATUS (found/missing) and VERDICT. Compare to current state.
If this is the first run, write:
  prior_brief: NONE — first run
Mark all remaining delta fields as N/A. This block is required on first run.

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

**STATUS density contract:** Count blocking missing signals before formatting.
Use FULL format if blocking gaps <= 4. Use COMPRESSED format + [BLOCKING-DETAIL]
if blocking gaps > 4.

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>
  ...

missing: Y signals

  BLOCKING (commit with unknown):

  [FULL FORMAT — blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
    ...

  [COMPRESSED FORMAT — blocking gaps > 4 (see [BLOCKING-DETAIL] for full fields):]
    - <ns>/<skill>/<item> — <inertia risk, <=12 words>
    ...

  OPTIONAL (can ship and learn):
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking missing signal, `Inertia risk:` is required. A gap with no articulable
inertia risk is optional. State explicitly when empty:
  `BLOCKING: none — all gaps are optional`

If compressed format was triggered, produce immediately after STATUS:

```
[BLOCKING-DETAIL]
Full inertia fields for each compressed blocking entry:

  <ns>/<skill>/<item>
    Inertia risk: <full statement>
  ...
```

---

```
[CONFIDENCE]
| Dimension      | Score (1-3) | Rationale                                              |
|----------------|-------------|--------------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+)       |
| Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong) |
| Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/optional) |

average: (breadth + depth + severity) / 3 = X.X
level:   LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
binding: <the dimension that determines the level — lowest score, or tie-breaker>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically —
do not estimate. CONFIDENCE is a standalone block; do not embed inside STORY.

---

```
[STORY]
<Prose narrative only. Do not include tables or bullet lists. Do not name artifact
filenames. Do not restate confidence level (it is in CONFIDENCE).

The narrative must answer these three questions in sequence, in continuous prose.
Do not use headers or numbered labels — write through them as paragraphs:

  1. What case do the signals make together?
     What direction does the aggregate evidence point? What picture forms across
     namespaces — not signal by signal, but as a set?

  2. What do the gaps leave genuinely uncertain?
     What is the class of unknown the gaps represent — the assumption set that
     remains untested, not the list of missing artifacts?

  3. What is the team's real exposure if they commit now?
     Not a list of what is missing — what could go wrong that this evidence does
     not rule out, and why does the current signal set fail to address it?

Minimum 2 paragraphs. Maximum 4.>
```

Execution: Write prose that answers all three questions as a flowing narrative.
Do not use bullets, headers, or tables inside this block. STORY is the synthesis;
STATUS and CONFIDENCE hold the structured records.

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

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` is required at every
verdict status — even READY ("remaining risk is X and is acceptable because Y").
A CONDITIONAL verdict must name the condition and what satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-03 — Axis: C-11 dual commit-risk fields (Assumption + Consequence in FULL FORMAT blocking entries)

**Hypothesis:** R3 V-05 used single `Inertia risk:` per blocking gap in FULL FORMAT.
This scored C-11 PARTIAL across R1, R2, and R3. The confirmed mechanism (R3 V-02) is
dual `Assumption: / Consequence:` fields where Assumption names what the team is
silently accepting and Consequence names what becomes more likely if that assumption
is wrong. A gap that cannot answer both fields is reclassified as optional — this
reclassification rule is what makes the format structurally enforcing rather than
advisory. V-03 applies this single change: FULL FORMAT gets dual fields; COMPRESSED
format stays single-line ≤12 words (scale-appropriate); BLOCKING-DETAIL upgrades to
carry both fields. STORY, CONFIDENCE, and DELTA are unchanged from R3 V-05. Expected:
C-11 PASS, C-04 PARTIAL (no C-17/C-18), all other criteria hold.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block.
All other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

**THE PRIMARY COMPETITOR IS INERTIA.** Every blocking gap must name the commit-risk —
what assumption the team is silently making if they ship today without that signal.

---

Run the phases in order. Produce exactly these blocks:

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
prior brief. Extract its STATUS (found/missing) and VERDICT. Compare to current state.
If this is the first run, write:
  prior_brief: NONE — first run
Mark all remaining delta fields as N/A. This block is required on first run.

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

**STATUS density contract:** Count blocking missing signals before formatting.
Use FULL format if blocking gaps <= 4. Use COMPRESSED format + [BLOCKING-DETAIL]
if blocking gaps > 4.

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>
  ...

missing: Y signals

  BLOCKING (commit with unknown):

  [FULL FORMAT — blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Assumption:   <what the team is silently accepting if they commit today>
      Consequence:  <what becomes more likely if this assumption is wrong>
    ...

  [COMPRESSED FORMAT — blocking gaps > 4 (see [BLOCKING-DETAIL] for full fields):]
    - <ns>/<skill>/<item> — <commit risk, <=12 words>
    ...

  OPTIONAL (can ship and learn):
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking missing signal, both `Assumption:` and `Consequence:` fields are required.
A gap that cannot be answered with both fields is reclassified as optional — it cannot
be blocking if the commit-risk is not articulable. State explicitly when empty:
  `BLOCKING: none — all remaining gaps are optional`

If compressed format was triggered, produce immediately after STATUS:

```
[BLOCKING-DETAIL]
Full commit-risk fields for each compressed blocking entry:

  <ns>/<skill>/<item>
    Assumption:   <full statement>
    Consequence:  <full statement>
  ...
```

---

```
[CONFIDENCE]
| Dimension      | Score (1-3) | Rationale                                              |
|----------------|-------------|--------------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+)       |
| Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong) |
| Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/optional) |

average: (breadth + depth + severity) / 3 = X.X
level:   LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
binding: <the dimension that determines the level — lowest score, or tie-breaker>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically —
do not estimate. CONFIDENCE is a standalone block; do not embed inside STORY.

---

```
[STORY]
<2-4 paragraphs. What do the existing signals say together? What do the blocking
gaps leave genuinely uncertain? What is the team's real exposure if they commit on
current evidence?

Constraints:
- Prose only. No tables or bullet lists in this block.
- Do not name artifact filenames — refer by category (e.g., "the flow signals").
- Do not restate confidence level — it is in CONFIDENCE.
- Do not enumerate gaps per item — STATUS holds that record.
- Do address the inertia risk as a pattern: what class of unknowns remains
  untested, and what that means for the commit decision as a whole.>
```

Execution: Synthesize STATUS and CONFIDENCE findings. The narrative must answer
what the inertia risk means as a pattern across the blocking gap set — not per gap.
STORY owns the cross-signal interpretation; every other block owns its own record.

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

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` is required at every
verdict status — even READY ("remaining risk is X and is acceptable because Y").
A CONDITIONAL verdict must name the condition and what satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-04 — Axes: C-17 + C-18 combined (jointly-necessary STORY purity pair, no C-11 change)

**Hypothesis:** V-01 tests C-17 alone (expected C-04 PARTIAL). V-02 tests C-18 alone
(expected C-04 PARTIAL). V-04 combines them — the rubric's claim is that both must
be simultaneously present for C-04 structural reliability. If V-04 achieves C-04
PASS where V-01 and V-02 each achieved PARTIAL, the jointly-necessary claim is
confirmed and the mechanism is clear. V-04 intentionally leaves C-11 unchanged
(single `Inertia risk:`) to isolate the STORY purity axis from the blocking-gap
format axis. Expected: C-04 PASS, C-17 PASS, C-18 PASS, C-11 PARTIAL. Compared to
V-05, V-04 should score 10 points lower (the C-11 gap).

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block.
All other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

**THE PRIMARY COMPETITOR IS INERTIA.** Every blocking gap must name the commit-risk —
what assumption the team is silently making if they ship today without that signal.

---

Run the phases in order. Produce exactly these blocks:

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
prior brief. Extract its STATUS (found/missing) and VERDICT. Compare to current state.
If this is the first run, write:
  prior_brief: NONE — first run
Mark all remaining delta fields as N/A. This block is required on first run.

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

**STATUS density contract:** Count blocking missing signals before formatting.
Use FULL format if blocking gaps <= 4. Use COMPRESSED format + [BLOCKING-DETAIL]
if blocking gaps > 4.

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>
  ...

missing: Y signals

  BLOCKING (commit with unknown):

  [FULL FORMAT — blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
    ...

  [COMPRESSED FORMAT — blocking gaps > 4 (see [BLOCKING-DETAIL] for full fields):]
    - <ns>/<skill>/<item> — <inertia risk, <=12 words>
    ...

  OPTIONAL (can ship and learn):
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking missing signal, `Inertia risk:` is required. A gap with no articulable
inertia risk is optional. State explicitly when empty:
  `BLOCKING: none — all gaps are optional`

If compressed format was triggered, produce immediately after STATUS:

```
[BLOCKING-DETAIL]
Full inertia fields for each compressed blocking entry:

  <ns>/<skill>/<item>
    Inertia risk: <full statement>
  ...
```

---

```
[CONFIDENCE]
| Dimension      | Score (1-3) | Rationale                                              |
|----------------|-------------|--------------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+)       |
| Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong) |
| Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/optional) |

average: (breadth + depth + severity) / 3 = X.X
level:   LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
binding: <the dimension that determines the level — lowest score, or tie-breaker>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically —
do not estimate. CONFIDENCE is a standalone block; do not embed inside STORY.

---

```
[STORY]
<Prose narrative only. Minimum 2 paragraphs. Maximum 4.

PERMITTED:
  - Paragraph prose.
  - References to signal categories by type (e.g., "the flow signals", "the
    feasibility evidence") — not artifact filenames.
  - Cross-signal reasoning: what patterns emerge across namespaces?
  - Discussion of the inertia risk as a pattern across the blocking gap set.

NOT PERMITTED:
  - Bullet lists or numbered lists of any kind.
  - Artifact filenames (those belong to STATUS).
  - Tables of any kind (confidence table belongs to CONFIDENCE).
  - The words LOW, MEDIUM, or HIGH to restate confidence level
    (that belongs to CONFIDENCE).
  - Per-gap enumeration (belongs to STATUS).

The narrative must answer these three questions in sequence, in continuous prose.
Do not label them with numbers or headers — write through them as paragraphs:

  1. What case do the signals make together?
     What direction does the aggregate evidence point? What picture forms across
     namespaces — not signal by signal, but as a set?

  2. What do the gaps leave genuinely uncertain?
     What is the class of unknown the gaps represent — the assumption set that
     remains untested, not the list of missing artifacts?

  3. What is the team's real exposure if they commit now?
     Not a list of what is missing — what could go wrong that this evidence does
     not rule out, and why does the current signal set fail to address it?>
```

Execution: Write prose that answers all three questions through the PERMITTED forms
only. If any NOT PERMITTED form appears in this block, the synthesis has failed.
STORY owns the cross-signal interpretation; every other block owns its own record.

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

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` is required at every
verdict status — even READY ("remaining risk is X and is acceptable because Y").
A CONDITIONAL verdict must name the condition and what satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-05 — Axes: Full 18-criterion sweep (C-11 + C-17 + C-18 — all four remaining improvements)

**Hypothesis:** V-04 applies the STORY purity pair (C-17 + C-18), closing C-04,
C-17, and C-18. V-03 applies dual commit-risk fields (C-11). V-05 combines all three
axes simultaneously on the R3 V-05 base. Expected score: 180/180. The ceiling test
for R4: can all four remaining improvements coexist without structural conflict? The
only potential interaction is between dual blocking-gap fields (C-11) and the density
contract (C-15): FULL FORMAT now has three lines per entry (gap path + Assumption +
Consequence) instead of two. The ceiling of 4 entries for FULL FORMAT should still
hold — but this must be verified. If C-15 PASS degrades to PARTIAL under dual fields,
the threshold may need to be lowered to 3 entries for the R5 base. Track for scoring.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block.
All other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

**THE PRIMARY COMPETITOR IS INERTIA.** Every blocking gap must name the commit-risk —
what assumption the team is silently making if they ship today without that signal.

---

Run the phases in order. Produce exactly these blocks:

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
prior brief. Extract its STATUS (found/missing) and VERDICT. Compare to current state.
If this is the first run, write:
  prior_brief: NONE — first run
Mark all remaining delta fields as N/A. This block is required on first run.

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

**STATUS density contract:** Count blocking missing signals before formatting.
Use FULL format if blocking gaps <= 4. Use COMPRESSED format + [BLOCKING-DETAIL]
if blocking gaps > 4.

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>
  ...

missing: Y signals

  BLOCKING (commit with unknown):

  [FULL FORMAT — blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Assumption:   <what the team is silently accepting if they commit today>
      Consequence:  <what becomes more likely if this assumption is wrong>
    ...

  [COMPRESSED FORMAT — blocking gaps > 4 (see [BLOCKING-DETAIL] for full fields):]
    - <ns>/<skill>/<item> — <commit risk, <=12 words>
    ...

  OPTIONAL (can ship and learn):
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking missing signal, both `Assumption:` and `Consequence:` fields are required.
A gap that cannot be answered with both fields is reclassified as optional — it cannot
be blocking if the commit-risk is not articulable. State explicitly when empty:
  `BLOCKING: none — all remaining gaps are optional`

If compressed format was triggered, produce immediately after STATUS:

```
[BLOCKING-DETAIL]
Full commit-risk fields for each compressed blocking entry:

  <ns>/<skill>/<item>
    Assumption:   <full statement>
    Consequence:  <full statement>
  ...
```

---

```
[CONFIDENCE]
| Dimension      | Score (1-3) | Rationale                                              |
|----------------|-------------|--------------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+)       |
| Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong) |
| Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/optional) |

average: (breadth + depth + severity) / 3 = X.X
level:   LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
binding: <the dimension that determines the level — lowest score, or tie-breaker>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically —
do not estimate. CONFIDENCE is a standalone block; do not embed inside STORY.

---

```
[STORY]
<Prose narrative only. Minimum 2 paragraphs. Maximum 4.

PERMITTED:
  - Paragraph prose.
  - References to signal categories by type (e.g., "the flow signals", "the
    feasibility evidence") — not artifact filenames.
  - Cross-signal reasoning: what patterns emerge across namespaces?
  - Discussion of the inertia risk as a pattern across the blocking gap set.

NOT PERMITTED:
  - Bullet lists or numbered lists of any kind.
  - Artifact filenames (those belong to STATUS).
  - Tables of any kind (confidence table belongs to CONFIDENCE).
  - The words LOW, MEDIUM, or HIGH to restate confidence level
    (that belongs to CONFIDENCE).
  - Per-gap enumeration (belongs to STATUS).

The narrative must answer these three questions in sequence, in continuous prose.
Do not label them with numbers or headers — write through them as paragraphs:

  1. What case do the signals make together?
     What direction does the aggregate evidence point? What picture forms across
     namespaces — not signal by signal, but as a set?

  2. What do the gaps leave genuinely uncertain?
     What is the class of unknown the gaps represent — the assumption set that
     remains untested, not the list of missing artifacts?

  3. What is the team's real exposure if they commit now?
     Not a list of what is missing — what could go wrong that this evidence does
     not rule out, and why does the current signal set fail to address it?>
```

Execution: Write prose that answers all three questions through the PERMITTED forms
only. If any NOT PERMITTED form appears in this block, the synthesis has failed.
STORY owns the cross-signal interpretation; every other block owns its own record.

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

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` is required at every
verdict status — even READY ("remaining risk is X and is acceptable because Y").
A CONDITIONAL verdict must name the condition and what satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

**Key differentiators to watch in scoring:**

- **V-01** tests whether PERMITTED/NOT PERMITTED alone (without three-question
  mandate) achieves C-04 PASS. If C-04 PARTIAL: the rubric's jointly-necessary claim
  is confirmed. If C-04 PASS: investigate why question structure is unnecessary.
- **V-02** tests whether three-question sequential structure alone (without formal
  prohibition list) achieves C-04 PASS. Same joint-necessity test from the other
  direction. PARTIAL here + PARTIAL at V-01 + PASS at V-04 confirms the model.
- **V-03** tests C-11 dual-field upgrade in complete isolation. If C-11 PASS here,
  it is confirmed portable into V-05 without side effects. Watch whether the three-
  line FULL FORMAT entry (path + Assumption + Consequence) strains the density
  contract ceiling — if C-15 degrades, the threshold needs review.
- **V-04** is the joint-necessity confirmation test. C-04 PASS here with V-01 and
  V-02 both scoring PARTIAL proves prohibition + structure are jointly necessary. C-11
  is the remaining gap vs. V-05 (-10 pts expected).
- **V-05** is the 18-criterion ceiling attempt: 180/180 target. The interaction to
  watch is C-11 dual fields x C-15 density ceiling. If both hold without degradation,
  the progressive decomposition model is confirmed at maximum scale for R4.
