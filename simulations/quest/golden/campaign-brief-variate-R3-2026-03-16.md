---
skill: quest-variate
skill_target: campaign-brief
round: 3
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-brief-rubric-v3-2026-03-16.md
---

# Variations — campaign-brief / Round 3

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

**R2 recap:** V-05 was the maximalist sweep targeting all 13 criteria. The structural
tension R2 exposed: embedding the confidence dimension table (C-10) inside STORY created
a conflict with C-12 (prose confinement) — the scoring table competed with narrative
synthesis for the same block. V-02 had the strongest per-gap commit-risk structure
(C-11) but no density ceiling. No R2 variation addressed C-14 or C-15 — both newly
added in v3 from R2 observations.

**R3 rubric adds:** C-14 (confidence block isolation) and C-15 (STATUS density ceiling).
Max score is now 150. The aspirational tier is now 70 points — largest single tier.

**R3 targets:** Resolve the STORY/CONFIDENCE structural conflict by extracting the
confidence table to a standalone block (C-14). Add an explicit density ceiling contract
to STATUS (C-15). Confirm whether STORY purity constraints lift C-04 from PARTIAL
to PASS independently of other axes (V-03). The aspirational tier now outweighs the
essential and recommended tiers combined — a variation missing all aspirational criteria
cannot exceed 80/150.

---

## Variation axes selected

- **Single-axis:** Confidence block isolation (V-01), STATUS density ceiling (V-02),
  STORY purity enforcement (V-03)
- **Combined:** V-01 + V-02 axes on a clean 6-block base (V-04), Full 15-criterion
  sweep — R2 V-05 + C-14 + C-15 (V-05)

---

## V-01 — Axis: Confidence block isolation (C-14 — standalone CONFIDENCE block)

**Hypothesis:** R2 V-03 and V-05 both embedded the confidence dimension table inside
STORY. This satisfied C-10 (derived, auditable metric) but created a structural conflict
with C-12 (prose confined to STORY) — a scoring table inside STORY means STORY is no
longer pure prose, and pure prose synthesis (C-04) has to share the block with a table.
V-01 resolves this by extracting confidence to a dedicated [CONFIDENCE] block between
STATUS and STORY. With the table gone, STORY gets uncontested prose space (C-12 PASS,
C-04 at full strength). CONFIDENCE gets its own structural identity (C-10 PASS, C-14
PASS). The block pipeline — STATUS feeds CONFIDENCE, CONFIDENCE informs STORY — creates
a natural evidence-to-calibration-to-narrative ordering. This variation deliberately
omits C-15 (no density ceiling) to isolate the C-14 axis.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

---

Run the seven phases in order. Produce exactly these blocks:

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

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>
  ...

missing: Y signals

  BLOCKING (commit with unknown):
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
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
[CONFIDENCE]
| Dimension      | Score (1-3) | Rationale                                       |
|----------------|-------------|--------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+) |
| Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong) |
| Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/optional) |

average: (breadth + depth + severity) / 3 = X.X
level:   LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
binding: <the dimension that determines the level — lowest score, or tie-breaker>
```

Execution: Score each dimension from STATUS data only. Derive average arithmetically.
Do not embed this block inside STORY — CONFIDENCE is a standalone block between STATUS
and STORY. Do not assert the level from intuition; derive it from the average.

---

```
[STORY]
<2-4 paragraphs. What do the existing signals say together? What do the blocking gaps
leave genuinely uncertain? What is the team's real exposure if they commit on current
evidence?

Rules for this block:
- Do not list artifact names — synthesize the case the evidence makes as a whole.
- Do not include tables or bullet lists — prose only.
- Do not restate the confidence level — it appears in [CONFIDENCE].
- Address the inertia risk as a pattern across blocking gaps, not per gap.>
```

Execution: Synthesize STATUS and CONFIDENCE findings into a coherent narrative arc.
The narrative must interpret what the signals mean together — not what each individual
signal contains. STORY owns the cross-signal reasoning; CONFIDENCE owns the calibration.

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

Write all seven blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, CONFIDENCE, STORY, VERDICT.

---

## V-02 — Axis: STATUS density ceiling (C-15 — explicit compression contract for blocking gaps)

**Hypothesis:** R2 V-02 introduced Assumption+Consequence per-gap fields (C-11), which
is the correct mechanism for commit-risk visibility. But per-gap fields grow linearly
with gap count — 8 blocking gaps produces an unreadable STATUS block that buries STORY
and VERDICT. C-15 requires an *explicit mechanism* that keeps STATUS scannable at scale
regardless of gap count. V-02 tests a two-tier density contract stated structurally in
the prompt: when blocking gaps <= 4, use the full Assumption+Consequence format; when
> 4, switch to compressed single-line entries for STATUS and produce a separate
[BLOCKING-DETAIL] block with full fields. The contract is stated as a prompt-level
structural rule — not a convention the model is expected to discover. The mechanism
being present proves C-15 intent regardless of current gap count. This variation
deliberately omits C-14 (confidence remains inside STORY) and C-09 (no DELTA) to
isolate the density ceiling axis.

---

You are running `campaign-brief` for topic: `{{topic}}`.

`campaign-brief` is a decision-support dashboard. Its purpose is not signal inventory
for its own sake — it is to tell the team whether they have enough evidence to commit.
Every gap in the blocking category must justify its placement with specific commit-risk
reasoning. The STATUS block must remain scannable regardless of gap count.

Output format: structured dashboard with named blocks. Prose is confined to the STORY
block. All other blocks are structured data.

---

```
[TOPIC]
name:    {{topic}}
date:    <registration date>
intent:  <one sentence describing what decision this topic is building toward>
status:  NEW | ACTIVE | COMPLETE
source:  TOPICS.md (existing) | TOPICS.md (created)
```

Execution: Glob `simulations/TOPICS.md`. Confirm or create the entry for `{{topic}}`.
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

Execution: Glob `simulations/{{topic}}/strategy.md`. Load if present; generate if absent.
Minimum 3 rows. Every row must have all four columns populated.

---

**STATUS density contract:** Before formatting the STATUS block, count the total number
of blocking missing signals.

- If blocking gaps <= 4: use FULL format (Assumption + Consequence per gap).
- If blocking gaps > 4: use COMPRESSED format for STATUS entries, then produce a
  [BLOCKING-DETAIL] block immediately after STATUS with full fields.

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>
  ...

missing: Y signals

  BLOCKING:

  [FULL FORMAT — if blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Assumption:   <what the team is silently accepting if they commit today>
      Consequence:  <what outcome becomes more likely if the assumption is wrong>
    ...

  [COMPRESSED FORMAT — if blocking gaps > 4 (full fields in [BLOCKING-DETAIL] below):]
    - <ns>/<skill>/<item> — <inertia risk, <=12 words>
    ...

  OPTIONAL:
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. A blocking gap
that cannot answer both Assumption and Consequence fields is reclassified as optional.
State explicitly when the section is empty:
  `BLOCKING: none — all remaining gaps are optional`

If compressed format was used, produce immediately after STATUS:

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
[STORY]
<2-4 paragraphs. What do the existing signals say together? What do the blocking gaps
leave genuinely uncertain? What is the team's real decision exposure if they commit now?
Do not re-enumerate artifacts — synthesize. Do not list gaps per item.>

confidence_dimensions:
  | Dimension      | Score (1-3) | Rationale |
  |----------------|-------------|-----------|
  | Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+) |
  | Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong) |
  | Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/optional) |

  average: X.X
  level: LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
  rationale: <one sentence naming the binding dimension>
```

Execution: Write the prose narrative first. Then score confidence dimensions from
STATUS data and derive the average. The table follows the prose in this block.

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

Execution: Derive from STORY. `inertia_cost` is required at every verdict status.
A CONDITIONAL verdict must name the condition and what satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered], STORY, VERDICT.

---

## V-03 — Axis: STORY purity enforcement (C-04/C-12 — prose quality through structural constraint)

**Hypothesis:** R2 variations consistently scored C-04 as PARTIAL — a synthesis appeared
but typically mixed enumeration with interpretation. Lists labeled "what the signals say
together" without actual cross-signal reasoning produce PARTIAL on C-04. The root cause:
no variation told the model what it *cannot* do in STORY. V-03 tests whether explicit
negative constraints on the STORY block improve synthesis quality — prohibiting bullet
lists, artifact filenames, and confidence level restatements forces the model to
actually synthesize rather than enumerate in prose form. A three-question constraint
makes STORY structure testable without using tables. The standalone [CONFIDENCE] block
is retained to satisfy C-14 (accepted as a side effect, not the primary axis). V-03
deliberately omits C-09 (no DELTA) and C-15 (no ceiling) to isolate the STORY purity
axis cleanly.

---

You are running `campaign-brief` for topic: `{{topic}}`.

`campaign-brief` delivers a complete topic dashboard: what signals exist, what is
missing, and what the evidence says about readiness to commit. The dashboard closes
with a calibrated confidence assessment and a readiness verdict.

Output format: compact terminal dashboard. All blocks except STORY contain structured
data only. STORY contains prose only — no tables, no bullet lists.

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

Execution: Glob `simulations/TOPICS.md`. Confirm or create the entry.
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
      Inertia risk: <what the team is silently assuming if they commit today>
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

---

```
[CONFIDENCE]
| Dimension      | Score (1-3) | Rationale                                       |
|----------------|-------------|--------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+) |
| Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong) |
| Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/optional) |

average: (breadth + depth + severity) / 3 = X.X
level:   LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
binding: <the dimension that determines the level>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically.
This block is the confidence record — STORY will not restate the level.

---

```
[STORY]
<Prose narrative only. Rules for this block:

PERMITTED:
  - Paragraph prose.
  - References to signal categories by type (e.g., "the flow signals", "the feasibility
    evidence") — not artifact filenames.
  - Cross-signal reasoning: what patterns emerge across namespaces?

NOT PERMITTED:
  - Bullet lists or numbered lists of any kind.
  - Artifact filenames (those belong to STATUS).
  - Tables of any kind (the confidence table belongs to CONFIDENCE).
  - The words LOW, MEDIUM, or HIGH to restate the confidence level.
  - Per-gap enumeration (that belongs to STATUS).

The narrative must answer these three questions in sequence, in continuous prose:

  1. What case do the signals make together?
     What direction does the aggregate evidence point? What picture of the feature
     do the signals form as a set — not individually, but together?

  2. What do the gaps leave genuinely uncertain?
     What is the *class* of unknown the gaps represent — not the list of missing
     artifacts, but the assumption set that remains untested?

  3. What is the team's real exposure if they commit now?
     Not a list of what is missing — a statement of what could go wrong that this
     evidence does not rule out.

Minimum 2 paragraphs. Maximum 4.>
```

Execution: Write prose that answers all three questions. Do not insert any table,
list, or structured element. STORY is the synthesis; STATUS and CONFIDENCE hold
the structured data.

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
verdict status. A CONDITIONAL verdict must name the condition and what satisfies it.

---

Write all six blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, STRATEGY, STATUS, CONFIDENCE, STORY, VERDICT.

---

## V-04 — Axes: C-14 + C-15 combined (confidence isolation + density ceiling, no DELTA)

**Hypothesis:** V-01 isolates C-14 (CONFIDENCE block) and produces a FAIL on C-15.
V-02 isolates C-15 (density ceiling) and produces a FAIL on C-14. V-04 combines both
axes onto a clean base without DELTA. The goal is to confirm that the two new criteria
are additive — that adding C-15 to a C-14-passing variation does not introduce
structural conflicts, and that adding C-14 to a C-15-passing variation does not crowd
the block sequence. Deliberately omitting C-09 (DELTA) removes a potential interaction
with the density ceiling (delta tracking changes the gap count per run, which is the
trigger condition for C-15 compressed format). Expected score lift over V-01: +10 points
(C-15 PASS). Expected score vs. V-05: -10 points (C-09 absent). If V-04 scores lower
than expected, the DELTA-ceiling interaction is the investigation target for R4.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
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

If compressed format was used, produce immediately after STATUS:

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
| Dimension      | Score (1-3) | Rationale                                       |
|----------------|-------------|--------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+) |
| Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong) |
| Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/optional) |

average: (breadth + depth + severity) / 3 = X.X
level:   LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
binding: <the dimension that determines the level>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically.
CONFIDENCE is a standalone block — do not embed inside STORY.

---

```
[STORY]
<2-4 paragraphs. What do the existing signals say together? What do the blocking gaps
leave genuinely uncertain? What is the team's real exposure if they commit on current
evidence?

Rules:
- Prose only. No tables or bullet lists.
- Do not name artifact filenames.
- Do not restate confidence level (it is in [CONFIDENCE]).
- Address inertia risk as a pattern across blocking gaps — what class of unknowns
  remains, not a per-gap list.>
```

Execution: Synthesize STATUS and CONFIDENCE findings into a coherent narrative arc.
STORY interprets the pattern; STATUS and CONFIDENCE hold the structured records.

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
verdict status — even READY. A CONDITIONAL verdict must name the condition and
what satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered], CONFIDENCE,
STORY, VERDICT.

---

## V-05 — Axes: Full 15-criterion sweep (R2 V-05 + C-14 + C-15)

**Hypothesis:** R2 V-05 was the first variation to target all 13 criteria simultaneously.
The two structural failures were C-14 (confidence table embedded inside STORY, conflicting
with C-12) and C-15 (no density ceiling stated). V-05 for R3 is the direct successor:
identical to R2 V-05 in all respects except (1) confidence dimension table extracted to
a standalone [CONFIDENCE] block after STATUS, and (2) STATUS density ceiling contract
added. Block count grows from 6 to 7 (plus optional [BLOCKING-DETAIL]). The ceiling
test: does engineering all 15 properties simultaneously produce a prompt that is too
long to follow, or does the structural separation of concerns — one concept per block —
actually make it simpler? If V-05 scores higher than V-04 (expected: +10 for C-09),
the additive model holds and R4 can target refinement. If V-05 scores lower despite
correct implementation, prompt complexity is the failure mode — a signal for structural
simplification in R4.

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
| Dimension      | Score (1-3) | Rationale                                       |
|----------------|-------------|--------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+) |
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
<2-4 paragraphs. What do the existing signals say together? What do the blocking gaps
leave genuinely uncertain? What is the team's real exposure if they commit on current
evidence?

Constraints:
- Prose only. No tables or bullet lists in this block.
- Do not name artifact filenames — refer by category (e.g., "the flow signals").
- Do not restate confidence level — it is in [CONFIDENCE].
- Do not enumerate gaps per item — STATUS holds that record.
- Do address inertia risk as a pattern: what class of unknowns remains untested, and
  what that means for the commit decision as a whole.>
```

Execution: Synthesize STATUS and CONFIDENCE findings. The narrative must answer what
the inertia risk means as a pattern across the blocking gap set — not per gap.
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

- **V-01** is the cleanest C-14 test: standalone CONFIDENCE block between STATUS and
  STORY, no density ceiling confound. If C-14 PASS here and FAIL in R2 V-05, the block
  boundary is confirmed as the mechanism — not the presence of the table.
- **V-02** is the cleanest C-15 test: explicit two-tier density contract, no C-14
  confound (confidence inside STORY). The PARTIAL/PASS boundary for C-15 is whether
  the mechanism is *stated* in the prompt — V-02 states it explicitly. If V-02 still
  scores PARTIAL, the rubric requires triggered execution, not stated intent.
- **V-03** tests whether STORY purity constraints (no bullets, no artifact names,
  three-question structure, no confidence restatement) lift C-04 from PARTIAL to PASS
  without any other axis changes. A C-04 lift here with no C-09/C-15 additions would
  confirm that explicit negative constraints are the right mechanism for synthesis quality.
- **V-04** confirms additivity: both new axes on a base without DELTA. Expected to score
  +10 over V-01 (C-15 adds) and -10 vs. V-05 (C-09 absent). If the delta deviates,
  an interaction effect is present and becomes R4's investigation target.
- **V-05** is the 15-criterion ceiling test. If block count 7+ (plus optional
  BLOCKING-DETAIL) produces a higher score than V-04 without adding cognitive load,
  the progressive structural decomposition model is confirmed. If it scores lower
  despite correct criterion targeting, prompt length is the failure mode — a signal
  that R4 should explore structural consolidation rather than further decomposition.
