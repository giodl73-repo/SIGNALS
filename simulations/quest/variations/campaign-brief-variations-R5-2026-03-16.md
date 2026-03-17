Written to `simulations/quest/variations/campaign-brief-variations-R5-2026-03-16.md`.

---

## campaign-brief / Round 5 — Variations

**Base:** R4 V-05 (180/180 on v4). Against v5 (20 criteria, 200 pts): **190/200**.

**Two remaining gaps:**
- **C-19 PARTIAL** (+5 available): Reclassification rule is stated in execution, but the output doesn't annotate *which* gaps were reclassified and why — the reclassification is silent in the output. PASS requires visibility.
- **C-20 PARTIAL** (+5 available): Density contract says "count blocking missing signals" (implies entries) but never explicitly states that per-entry field count is orthogonal to the threshold.

---

| Var | Axis | Key change | Expected |
|-----|------|-----------|---------|
| V-01 | C-20 only | Add explicit sentence: threshold counts entries, per-entry field count orthogonal | ~195/200 |
| V-02 | C-19 only | Add `[RECLASSIFIED from BLOCKING:]` sub-section with annotation per moved gap | ~195/200 |
| V-03 | C-18 sparse-breadth | Sparse-breadth clause in STORY question 1: must state direction, not decline | ~190/200 (robustness, not score) |
| V-04 | C-20 + C-19 | Both output-fidelity changes — rubric ceiling attempt | **200/200** |
| V-05 | C-20 + C-19 + C-18 | All three axes — ceiling + robustness hardening | **200/200** |

**Critical experiments:**
- V-01 and V-02 should each score ~195 independently (each closes one PARTIAL). Symmetric result confirms C-19 and C-20 are structurally independent axes.
- V-04 = 200/200 confirms the v5 rubric is complete with no unreachable criteria.
- V-04 vs V-05 should score identically — any difference means the sparse-breadth clause interacts with a scored criterion (trace C-04 or C-18).
 (V-03):** Does adding the sparse-breadth clause degrade any other criterion? If STORY's question 1 is permitted to be "brief," does C-04 PASS hold? Track interaction.
- **V-04 ceiling:** All rubric gaps closed. 200/200 confirms the v5 rubric structure is complete with no unreachable criteria.
- **V-05 vs V-04:** Should score identically at 200/200. The robustness hardening (C-18 sparse-breadth clause) should not add or subtract from the rubric score — it's a structural improvement to behavior at extreme inputs. If V-05 scores lower than V-04, the sparse-breadth clause introduces a contradiction with another criterion (investigate C-04 or C-18).

---

## Variation axes selected

- **Single-axis:** C-20 explicit entry-count statement (V-01), C-19 reclassification output annotation (V-02), C-18 sparse-breadth resilience clause (V-03)
- **Combined:** C-20 + C-19 jointly (V-04), full three-axis sweep (V-05)

Base for all variations: R4 V-05 (eight-block pipeline: TOPIC, DELTA, STRATEGY,
STATUS, [BLOCKING-DETAIL], CONFIDENCE, STORY, VERDICT).

---

## V-01 — Axis: C-20 explicit entry-count statement

**Hypothesis:** R4 V-05 says "Count blocking missing signals before formatting / Use FULL
format if blocking gaps <= 4." This implies entry count, but does not say it. C-20 PASS
requires the prompt to explicitly state that the threshold counts entries (blocking gaps),
and that per-entry field count is orthogonal — a three-line entry and a one-line entry
each count as one. V-01 inserts exactly one explicit sentence after the density contract
threshold line. Everything else is R4 V-05 unchanged. Expected: C-20 PASS (+5), C-19
PARTIAL (unchanged — reclassification annotation still absent from output), total 195/200.

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
if blocking gaps > 4. The threshold counts blocking gap *entries* — each gap path is
one entry regardless of how many fields follow it. A three-line entry (path +
`Assumption:` + `Consequence:`) counts as one toward the ceiling, not three.
Per-entry field count is orthogonal to the threshold.

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

## V-02 — Axis: C-19 reclassification output annotation

**Hypothesis:** R4 V-05 has the reclassification *rule* in the execution note ("A gap that
cannot be answered with both fields is reclassified as optional"). But when a gap moves
from BLOCKING to OPTIONAL, the output does not annotate why — the reclassification is
silent. C-19 PASS requires visibility in the output: the reader must be able to see which
gaps were reclassified and why. V-02 adds one output annotation format to OPTIONAL:
`[reclassified from BLOCKING: <field> not articulable]`. Everything else is R4 V-05
unchanged. Expected: C-19 PASS (+5), C-20 PARTIAL (unchanged — entry-count distinction
still unspecified), total 195/200. If C-19 PASS emerges without this annotation, the
criterion's visibility requirement is satisfied by the existing reclassification clause
alone — investigate and revise C-19 before R6.

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

  [RECLASSIFIED from BLOCKING:]
    - <ns>/<skill>/<item>  [reclassified: <Assumption | Consequence> not articulable]
    ...
    (or: none)

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking missing signal, both `Assumption:` and `Consequence:` fields are required.
A gap that cannot be answered with both fields is reclassified as optional — it cannot
be blocking if the commit-risk is not articulable. When a gap is reclassified, it must
appear in the RECLASSIFIED sub-section with an explicit annotation naming which field
could not be supplied. Do not silently move gaps to OPTIONAL without annotation. Write
`RECLASSIFIED: none` if all evaluated gaps could supply both fields.

State explicitly when BLOCKING is empty:
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

## V-03 — Axis: C-18 sparse-breadth resilience clause

**Hypothesis:** R4 guidance flagged that the three-question sequential mandate in STORY
was validated against rich signal landscapes (multiple namespaces). Under sparse coverage
— 1-2 namespaces with signals — question 1 ("What case do the signals make together?")
risks collapsing into "insufficient signals to synthesize" or a single sentence that
doesn't constitute a paragraph. V-03 adds an explicit sparse-breadth clause to the STORY
execution note: the three-question structure applies at all coverage levels; question 1
is permitted to be brief but must state what direction even partial evidence points —
the structure cannot be omitted. This is a robustness improvement, not a rubric-gap
closure. Expected score: ~190/200 — C-19 and C-20 unchanged. If the sparse-breadth
clause introduces a contradiction with C-04 or C-18, trace the interaction. The clause
must not give the model permission to omit synthesis on the grounds of sparse data.

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
     Sparse-breadth rule: when fewer than 3 namespaces have signals, answer what
     direction even partial evidence points toward — do not write "insufficient
     signals." The structure is required at all coverage levels.

  2. What do the gaps leave genuinely uncertain?
     What is the class of unknown the gaps represent — the assumption set that
     remains untested, not the list of missing artifacts?

  3. What is the team's real exposure if they commit now?
     Not a list of what is missing — what could go wrong that this evidence does
     not rule out, and why does the current signal set fail to address it?>
```

Execution: Write prose that answers all three questions through the PERMITTED forms
only. The three-question structure is required regardless of signal coverage — sparse
evidence makes question 1 brief, not absent. If any NOT PERMITTED form appears in this
block, the synthesis has failed. STORY owns the cross-signal interpretation; every other
block owns its own record.

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

## V-04 — Axes: C-20 + C-19 combined (output-fidelity pair — entry-count explicit + reclassification visible)

**Hypothesis:** V-01 tests C-20 alone (expected 195/200). V-02 tests C-19 alone (expected
195/200). V-04 combines them — both PARTIAL criteria closed simultaneously. If C-19 and
C-20 are independent (operating on different structural locations: C-20 in the density
contract execution note, C-19 in the STATUS OPTIONAL output format), they should not
interfere. Expected: C-19 PASS + C-20 PASS = 200/200. The absence of the V-03
sparse-breadth clause is intentional: V-04 tests whether the rubric ceiling is achievable
without robustness hardening. V-04 vs V-05 should score identically (both 200/200) —
any difference indicates the sparse-breadth clause interacts with a scored criterion.

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
if blocking gaps > 4. The threshold counts blocking gap *entries* — each gap path is
one entry regardless of how many fields follow it. A three-line entry (path +
`Assumption:` + `Consequence:`) counts as one toward the ceiling, not three.
Per-entry field count is orthogonal to the threshold.

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

  [RECLASSIFIED from BLOCKING:]
    - <ns>/<skill>/<item>  [reclassified: <Assumption | Consequence> not articulable]
    ...
    (or: none)

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking missing signal, both `Assumption:` and `Consequence:` fields are required.
A gap that cannot be answered with both fields is reclassified as optional — it cannot
be blocking if the commit-risk is not articulable. When a gap is reclassified, it must
appear in the RECLASSIFIED sub-section with an explicit annotation naming which field
could not be supplied. Do not silently move gaps to OPTIONAL without annotation. Write
`RECLASSIFIED: none` if all evaluated gaps could supply both fields.

State explicitly when BLOCKING is empty:
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

## V-05 — Axes: Full three-axis sweep (C-20 + C-19 + C-18 sparse-breadth resilience)

**Hypothesis:** V-04 applies both output-fidelity improvements (C-19 + C-20) for the
200/200 ceiling attempt. V-05 adds the C-18 sparse-breadth resilience clause on top.
V-04 and V-05 should score identically at 200/200 — the sparse-breadth clause operates
inside STORY execution, which is a behavior guarantee, not a new rubric dimension. The
clause makes the three-question mandate robust under adverse input conditions without
changing what the rubric measures. If V-05 scores lower than V-04, trace which criterion
is affected by the sparse-breadth clause — the clause must not inadvertently weaken C-04
(synthesis requirement) by making "brief" a synonym for "omitted." The clause's one
firm constraint: the question 1 answer must state a direction, not decline to answer.

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
if blocking gaps > 4. The threshold counts blocking gap *entries* — each gap path is
one entry regardless of how many fields follow it. A three-line entry (path +
`Assumption:` + `Consequence:`) counts as one toward the ceiling, not three.
Per-entry field count is orthogonal to the threshold.

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

  [RECLASSIFIED from BLOCKING:]
    - <ns>/<skill>/<item>  [reclassified: <Assumption | Consequence> not articulable]
    ...
    (or: none)

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking missing signal, both `Assumption:` and `Consequence:` fields are required.
A gap that cannot be answered with both fields is reclassified as optional — it cannot
be blocking if the commit-risk is not articulable. When a gap is reclassified, it must
appear in the RECLASSIFIED sub-section with an explicit annotation naming which field
could not be supplied. Do not silently move gaps to OPTIONAL without annotation. Write
`RECLASSIFIED: none` if all evaluated gaps could supply both fields.

State explicitly when BLOCKING is empty:
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
     Sparse-breadth rule: when fewer than 3 namespaces have signals, answer what
     direction even partial evidence points toward — do not write "insufficient
     signals." The three-question structure is required at all coverage levels.

  2. What do the gaps leave genuinely uncertain?
     What is the class of unknown the gaps represent — the assumption set that
     remains untested, not the list of missing artifacts?

  3. What is the team's real exposure if they commit now?
     Not a list of what is missing — what could go wrong that this evidence does
     not rule out, and why does the current signal set fail to address it?>
```

Execution: Write prose that answers all three questions through the PERMITTED forms
only. The three-question structure is required regardless of signal coverage — sparse
evidence makes question 1 brief, not absent; question 1 must state a direction.
If any NOT PERMITTED form appears in this block, the synthesis has failed.
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

- **V-01** tests whether explicit entry-count language alone closes C-20. If C-20 PASS:
  the "per-entry line count orthogonal" phrasing is the mechanism. If C-20 PARTIAL:
  the existing base language ("count blocking missing signals") may already be satisfying
  the criterion, and the new sentence adds nothing — investigate the C-20 PARTIAL
  assessment of the base before accepting.
- **V-02** tests whether the RECLASSIFIED output sub-section closes C-19. If C-19 PASS:
  output-level visibility is the gate. If C-19 PARTIAL: the rubric's "visible in the
  output" requirement is satisfied by mere presence in OPTIONAL — re-read C-19 before R6.
- **V-03** tests whether the sparse-breadth clause interacts with any scored criterion.
  Expected: no score change from base (~190/200). If score changes, trace C-04 or C-18.
- **V-04** is the 200/200 ceiling attempt without robustness hardening. If V-04 scores
  200/200: C-19 and C-20 were the only remaining gaps and the rubric is complete.
- **V-05** adds robustness hardening to the ceiling. V-04 and V-05 should score
  identically — any difference traces to the sparse-breadth clause's effect on a
  scored criterion. V-05 is the candidate for R5 base if robustness confirmation
  is needed before shipping the skill.
