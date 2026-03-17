Written to `simulations/quest/variations/campaign-brief-variations-R6-2026-03-16.md`.

---

## campaign-brief / Round 6 — Variations

**Base:** R5 V-05 (200/200 on v5). Against v6 (21 criteria, 210 pts): **210/210**.

**Gap analysis:** C-21 is the only new criterion in v6. R5 V-05 already contains the sparse-breadth clause in two locations (STORY question 1 body and execution note). C-21 was designed to score exactly what V-05 introduced. V-05 satisfies C-21 PASS immediately — no open gaps remain.

**R6 scope shifts to structural robustness investigation** (three axes):

| Var | Axis | Key change | Expected |
|-----|------|-----------|---------|
| V-01 | Baseline (v6 ceiling confirm) | R5 V-05 verbatim | **210/210** |
| V-02 | Output format — C-16 isolation | Explicit note: density contract applies to BLOCKING entries only; `found:` timestamps survive regardless of FULL/COMPRESSED trigger | **210/210** |
| V-03 | Lifecycle emphasis — zero-signal state | Zero-signal rule in STORY + execution note: when `found` is empty, gap pattern is the evidence set; question 1 must characterize what uniform absence implies | **210/210** |
| V-04 | Output format + lifecycle emphasis | V-02 + V-03 combined | **210/210** |
| V-05 | All three axes | V-02 + V-03 + bounded/unbounded `inertia_cost` scope distinguisher in VERDICT | **210/210** |

**Critical experiments:**
- V-01 = 210/210 confirms C-21 is satisfied by the pre-existing sparse clause. If V-01 < 210, C-21's PASS gate is stricter than the sparse clause achieves — re-read the definition.
- V-02/V-03 single-axis checks: no scoring change expected (structural robustness only, no new rubric dimension).
- V-05 vs V-04: any difference traces to the bounded/unbounded `inertia_cost` framing interacting with C-07.

**R7 candidates named:**
1. C-16 timestamp survival in COMPRESSED mode
2. Zero-signal STORY mandate (extension of C-21 to the 0-signal extreme)
3. Bounded/unbounded `inertia_cost` classification at VERDICT level
and zero-signal hardening together | **210/210** |
| V-05 | Output format + lifecycle + inertia framing | V-02 + V-03 + bounded/unbounded risk distinction in VERDICT inertia_cost | **210/210** |

**Critical experiments:**
- V-01 = 210/210 confirms C-21 is satisfied by R5 V-05's sparse-breadth clause with no further changes.
- V-02, V-03 should score 210/210 identically to V-01 (no new rubric gaps — structural robustness only).
- V-04 vs V-05: any scoring difference traces to the inertia_cost scope framing interacting with C-07.
- If V-02's C-16 isolation clause causes C-16 to score differently (higher or lower), the clause has
  a rubric interaction — trace C-16 definition before confirming as V-03 base.

---

## V-01 — Baseline: R5 V-05 verbatim (v6 ceiling confirmation)

**Variation axis:** None — baseline replication.

**Hypothesis:** R5 V-05 already satisfies C-21 PASS via its two sparse-breadth clauses.
Against v6 (21 criteria, 210 pts), V-05 scores 210/210 immediately. C-21 was designed to
score what V-05 introduced structurally in R5. No further changes required.

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

## V-02 — Axis: C-16 timestamp isolation from density contract (output format)

**Variation axis:** Output format — explicit scope boundary for the density contract.

**Hypothesis:** The density contract (FULL/COMPRESSED) applies to BLOCKING GAP entries.
C-16 timestamps on found signals are structurally independent. An LLM given the current
prompt might misread the density contract as applying to found signals at high gap counts
and drop dates from the found: section. Adding an explicit isolation sentence prevents
this. Expected: 210/210, same as V-01, with structural protection against a live-output
failure mode. If scoring differs from V-01, trace C-16 — the isolation sentence may have
introduced an unintended interpretation.

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

The density contract applies to BLOCKING GAP entries only. Found signal lines in the
`found:` section always use `<ns>/<artifact>  <date>` format regardless of whether
FULL or COMPRESSED format was triggered — timestamps on found signals are not part of
the density contract and must never be dropped or abbreviated.

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

## V-03 — Axis: Zero-signal lifecycle emphasis (lifecycle emphasis)

**Variation axis:** Lifecycle emphasis — explicit execution guidance for the 0-signal state.

**Hypothesis:** The sparse-breadth clause handles 1-2 namespace coverage. The 0-signal
state (topic registered, no artifacts found yet) is a distinct edge case. STORY must still
run and question 1 must answer what direction the gap pattern itself points — absence of
evidence is evidence of absent investment, not a non-answer. Without this clause, an LLM
may write "no signals found — synthesis not possible" and omit STORY. The 0-signal clause
closes this failure mode by treating the gap pattern as the signal set. Expected: 210/210.

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
     Zero-signal rule: when no signals are found, question 1 must answer what the
     gap pattern itself reveals — systematic absence of evidence signals absent
     investment, not neutral state. State what the gap distribution implies about
     the team's current understanding.

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
Zero signals is not an escape hatch: when found is empty, the gap pattern is the
evidence set. Question 1 must characterize what uniform absence implies.
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

## V-04 — Axes: C-16 isolation + zero-signal handling (output format + lifecycle emphasis)

**Variation axes:** Output format (V-02) + lifecycle emphasis (V-03) combined.

**Hypothesis:** Both V-02 (timestamp isolation from density contract) and V-03 (zero-signal
state handling) are independent structural additions. Combined, they protect against two
distinct live-output failure modes at high gap count and zero signal count respectively.
Expected: 210/210 with no interaction effects. If scores differ, trace which criterion is
affected — the two axes operate on different blocks (STATUS density contract note vs STORY
execution note) so interaction is unlikely.

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

The density contract applies to BLOCKING GAP entries only. Found signal lines in the
`found:` section always use `<ns>/<artifact>  <date>` format regardless of whether
FULL or COMPRESSED format was triggered — timestamps on found signals are not part of
the density contract and must never be dropped or abbreviated.

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
     Zero-signal rule: when no signals are found, question 1 must answer what the
     gap pattern itself reveals — systematic absence of evidence signals absent
     investment, not neutral state. State what the gap distribution implies about
     the team's current understanding.

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
Zero signals is not an escape hatch: when found is empty, the gap pattern is the
evidence set. Question 1 must characterize what uniform absence implies.
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

## V-05 — Axes: C-16 isolation + zero-signal + inertia framing scope (three-axis)

**Variation axes:** Output format (V-02) + lifecycle emphasis (V-03) + inertia framing.

**Hypothesis:** The third axis adds a bounded/unbounded risk distinction to `inertia_cost`
in the VERDICT execution note. Currently `inertia_cost` requires "what specifically is
risked if the team commits now" — one sentence. The distinction: a READY verdict's
inertia_cost should state that risk is bounded and why; a NOT READY verdict's should state
that risk is unbounded and what class of failure it enables. This strengthens C-07 (which
requires Assumption + Consequence per blocking gap) by surfacing the aggregate risk pattern
at verdict level. Expected: 210/210. If C-07 or C-06 scores differently from V-04, trace
whether the bounded/unbounded framing conflicts with either criterion's definition.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block.
All other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

**THE PRIMARY COMPETITOR IS INERTIA.** Every blocking gap must name the commit-risk —
what assumption the team is silently making if they ship today without that signal.
A bounded inertia cost (team can recover if wrong) differs from an unbounded one
(error propagates to irreversible state). Name which applies in VERDICT.

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

The density contract applies to BLOCKING GAP entries only. Found signal lines in the
`found:` section always use `<ns>/<artifact>  <date>` format regardless of whether
FULL or COMPRESSED format was triggered — timestamps on found signals are not part of
the density contract and must never be dropped or abbreviated.

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
     Zero-signal rule: when no signals are found, question 1 must answer what the
     gap pattern itself reveals — systematic absence of evidence signals absent
     investment, not neutral state. State what the gap distribution implies about
     the team's current understanding.

  2. What do the gaps leave genuinely uncertain?
     What is the class of unknown the gaps represent — the assumption set that
     remains untested, not the list of missing artifacts?

  3. What is the team's real exposure if they commit now?
     Not a list of what is missing — what could go wrong that this evidence does
     not rule out, and why does the current signal set fail to address it?
     State whether the exposure is bounded (team can recover post-commit if assumptions
     prove wrong) or unbounded (error propagates to an irreversible state). The
     distinction matters for the VERDICT's inertia_cost framing.>
```

Execution: Write prose that answers all three questions through the PERMITTED forms
only. The three-question structure is required regardless of signal coverage — sparse
evidence makes question 1 brief, not absent; question 1 must state a direction.
Zero signals is not an escape hatch: when found is empty, the gap pattern is the
evidence set. Question 1 must characterize what uniform absence implies.
If any NOT PERMITTED form appears in this block, the synthesis has failed.
STORY owns the cross-signal interpretation; every other block owns its own record.

---

```
[VERDICT]
status:       READY | NOT READY | CONDITIONAL
rationale:    <one sentence>
inertia_cost: <one sentence — bounded: <what risk remains and why it is recoverable> |
                              unbounded: <what class of failure becomes likely and why it
                              cannot be undone after commit>>

blocking:
  - <item>: <why it blocks>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` is required at every
verdict status. For READY: state residual risk and why it is bounded. For NOT READY:
state what class of failure the blocking gaps leave open and why it cannot be corrected
post-commit. For CONDITIONAL: name the condition and declare whether the current risk is
bounded (commit with the condition) or unbounded (do not commit until condition is met).

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## Score Summary (predicted)

| Var | Essential /50 | Recommended /30 | Aspirational /130 | Total /210 | Rank |
|-----|:---:|:---:|:---:|:---:|:---:|
| V-01 | **50** | **30** | **130** | **210** | 1 |
| V-02 | **50** | **30** | **130** | **210** | 1 |
| V-03 | **50** | **30** | **130** | **210** | 1 |
| V-04 | **50** | **30** | **130** | **210** | 1 |
| V-05 | **50** | **30** | **130** | **210** | 1 |

All five variants are predicted to score identically — R6 has no open rubric gaps.
The variations probe structural robustness at three live-output failure modes:
- V-02: density contract misapplied to found-signal timestamps
- V-03/V-04: STORY synthesis collapse at 0-signal state
- V-05: inertia_cost missing bounded/unbounded scope distinction

If any variant scores below 210, the criterion affected names the v7 candidate.

---

## Critical Experiments

**V-01 vs rubric:** Confirms 210/210 on v6. C-21 was designed to capture the sparse-breadth
clause already present in V-05. If V-01 < 210, C-21 PARTIAL means the clause is present but
not explicit enough — re-read C-21's PASS definition against V-05's exact phrasing.

**V-02 C-16 isolation:** No scoring change expected. If C-16 changes score, the isolation
sentence has a semantic effect on the criterion — inspect whether the note implies the base
prompt was violating C-16 in COMPRESSED mode (i.e., the note reveals a pre-existing PARTIAL).

**V-03 zero-signal state:** No scoring change expected. The zero-signal clause extends V-05's
sparse-breadth protection to its logical limit. If C-04 or C-18 scores change, trace whether
"gap pattern is the evidence set" conflicts with the synthesis requirement or the
three-question mandate.

**V-05 bounded/unbounded framing:** No scoring change expected. If C-07 changes score, the
framing has introduced a new interpretation axis on the Assumption/Consequence pair at VERDICT
level — this would be the R7 investigation candidate.

**R7 criterion candidates from R6 investigation:**
1. C-16 timestamp survival in COMPRESSED mode (V-02 axis) — if live output drops timestamps
   in COMPRESSED mode, this becomes a scored criterion.
2. Zero-signal STORY mandate (V-03 axis) — if live output omits STORY at 0 signals, this
   becomes a scored criterion (extension of C-21 to the 0-signal extreme).
3. Bounded/unbounded inertia_cost classification (V-05 axis) — if live output writes
   undifferentiated inertia_cost at READY vs NOT READY, classification becomes a criterion.

```json
{"base": "R5-V-05", "base_score_v5": 200, "predicted_score_v6": 210, "new_criteria_v6": ["C-21"],
 "c21_satisfied_by_base": true, "investigation_axes": ["C-16-timestamp-isolation", "zero-signal-story-mandate", "bounded-unbounded-inertia-cost"],
 "all_variations_predicted": "210/210", "r7_candidates": ["C-16-compressed-survival", "zero-signal-synthesis-mandate", "inertia-cost-scope-classification"]}
```
