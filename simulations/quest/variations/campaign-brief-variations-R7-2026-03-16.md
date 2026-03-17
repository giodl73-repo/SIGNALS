Written to `simulations/quest/variations/campaign-brief-variations-R7-2026-03-16.md`.

---

## campaign-brief / Round 7 — Variations

**Base:** R6 V-05 (210/210 on v6). Against v7 (23 criteria, 230 pts): **230/230** expected.

**Gap analysis:** C-22 and C-23 are the only new criteria in v7. R6 V-05 already contains the zero-signal synthesis clause (STORY question 1 body + execution note) and the bounded/unbounded `inertia_cost` format (VERDICT template + execution note). Both criteria were designed to score exactly what R6 V-05 introduced. V-01 should confirm 230/230 with no changes. No open rubric gaps remain.

**R7 scope shifts to structural hardening investigation (three axes):**

| Var | Axis | Key change | Expected |
|-----|------|-----------|---------|
| V-01 | Baseline (R6 V-05 verbatim) | No changes | **230/230** |
| V-02 | Output format — C-16 x COMPRESSED timestamp survival | `found:` timestamp isolation promoted to named rule stated at both density-contract level and STATUS template level | **230/230** |
| V-03 | C-22 structural hardening | Zero-signal mandate promoted from question 1 body text to standalone named execution rule with two explicit non-vacating clauses | **230/230** |
| V-04 | C-23 syntax enforcement | `inertia_cost` given explicit action-posture sub-labels (`action: commit with monitoring` / `action: do not commit until resolved`) | **230/230** |
| V-05 | All three axes | V-02 + V-03 + V-04 combined | **230/230** |

**Critical experiments:**
- V-01 = 230/230 confirms both new criteria PASS from R6 V-05's pre-existing clauses. If V-01 < 230, identify which criterion has a stricter gate before combining.
- V-03 is the highest-stakes single-axis test: if V-03 > V-01, C-22's PASS gate requires a *named rule*, not embedded question text — meaning V-01 is actually PARTIAL on C-22.
- V-04 vs V-01: if V-04 > V-01, C-23 requires explicit action-posture labels, not just bounded/unbounded syntax.
- V-05 is the preferred R8 base: maximum structural coverage, all three robustness axes, zero rubric cost.

**R8 candidate carried forward:** COMPRESSED format × `found` timestamp survival — live falsification at high gap count (>4 blocking entries). V-02 states the isolation rule at two locations; live execution at the COMPRESSED trigger threshold is needed to confirm timestamps are not dropped in practice.
-04 combined on R6 V-05 base | **230/230** |

**Critical experiments:**
- **V-01 = 230/230** confirms C-22 PASS from the zero-signal clause in question 1 body
  + execution note, and C-23 PASS from the bounded/unbounded `inertia_cost` advisory
  note. If V-01 < 230, one new criterion has a stricter gate than the existing language
  achieves — identify which before combining axes.
- **V-02/V-03/V-04 single-axis checks:** no scoring change expected (structural
  robustness only, no new rubric dimension opened). If any scores < 230, the axis
  introduces a conflict with an existing criterion — trace before combining.
- **V-05 vs V-04:** should score identically. Any difference traces to the C-16
  timestamp isolation interacting with C-16/C-15/C-20. Timestamp isolation operates
  on a different output section (found vs blocking), so no interaction is expected.

**R8 candidate carried forward:** COMPRESSED format x `found` timestamp survival —
live falsification at high gap count (>4 blocking entries). V-02 states the rule
explicitly; live output at the COMPRESSED trigger threshold is needed to confirm
timestamps are not dropped in practice.

---

## V-01 — Axis: Baseline (R6 V-05 verbatim — 210/210 on v6)

**Hypothesis:** R6 V-05 already contains the zero-signal synthesis mandate (in STORY
question 1 body and execution note) and the bounded/unbounded `inertia_cost` advisory
at VERDICT level. C-22 was designed to score exactly the zero-signal clause; C-23 was
designed to score exactly the bounded/unbounded clause. V-01 confirms both PASS at 10
pts each, bringing total to 230/230. If V-01 < 230, the new criterion gates are stricter
than the existing language achieves — re-read C-22 and C-23 definitions before proceeding.

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

Timestamps on found signals are not part of the density contract and must never be
dropped or abbreviated regardless of whether FULL or COMPRESSED format is active.

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
     Zero-signal rule: when `found` is empty (zero signals across all namespaces),
     do not write "no signals found — synthesis not possible." The gap pattern is
     the evidence set. State what the uniform absence of signals implies about what
     has not been probed.

  2. What do the gaps leave genuinely uncertain?
     What is the class of unknown the gaps represent — the assumption set that
     remains untested, not the list of missing artifacts?

  3. What is the team's real exposure if they commit now?
     Not a list of what is missing — what could go wrong that this evidence does
     not rule out, and why does the current signal set fail to address it?>
```

Execution: Write prose that answers all three questions through the PERMITTED forms
only. The three-question structure is required regardless of signal coverage — sparse
evidence makes question 1 brief, not absent; question 1 must state a direction. When
`found` is empty, the gap pattern is the evidence set; question 1 must characterize
what uniform absence implies rather than vacating synthesis. If any NOT PERMITTED form
appears in this block, the synthesis has failed. STORY owns the cross-signal
interpretation; every other block owns its own record.

---

```
[VERDICT]
status:       READY | NOT READY | CONDITIONAL
rationale:    <one sentence>
inertia_cost: bounded: <residual risk and why recoverable post-commit>
              OR
              unbounded: <failure class and why irreversible once committed>

blocking:
  - <item>: <why it blocks>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` must classify
recoverability: use `bounded:` when the team can detect and correct post-commit;
use `unbounded:` when commitment triggers an irreversible state before detection
is possible. Required at every verdict status — even READY must declare that
remaining risk is bounded and why. A CONDITIONAL verdict must name the condition
and what satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-02 — Axis: Output format — C-16 x COMPRESSED timestamp survival (named isolation rule)

**Hypothesis:** R6 V-05 added "timestamps on found signals are not part of the density
contract and must never be dropped or abbreviated regardless of FULL/COMPRESSED trigger"
as a single sentence in the density contract preamble. The R7 investigation candidate
asks whether this sentence is sufficient when the COMPRESSED trigger actually fires at
high gap count — the model may abbreviate the entire STATUS block, dropping `found`
timestamps alongside compressed blocking entries. V-02 elevates the isolation rule from
an inline sentence to a named structural constraint stated in two locations: (1) the
density contract preamble (where it already appears) and (2) a dedicated note before
the STATUS block template reiterating that `found:` signal timestamps are exempt from
any abbreviation. Making the rule visible at both the contract level and the template
level reduces the risk that model attention wanders from the preamble when executing
the COMPRESSED branch. Expected: 230/230 — structural robustness, not a new rubric
dimension. If V-02 still produces dropped timestamps in live output, the isolation
rule requires a structural mechanism (e.g., a separate [FOUND] block) rather than
a prose instruction.

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
one entry regardless of how many fields follow it. Per-entry field count is orthogonal
to the threshold.

**Found-signal timestamp isolation rule:** The density contract and FULL/COMPRESSED
format choice govern the BLOCKING section only. The `found:` section is exempt from
the density contract in all cases. Timestamps on found signals must appear in full
(`<ns>/<artifact>  <date>`) regardless of whether FULL or COMPRESSED format is active
for the BLOCKING section. Do not abbreviate, truncate, or omit found-signal timestamps
when COMPRESSED format is triggered.

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>          <- timestamps required; not subject to density contract
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
A gap that cannot be answered with both fields is reclassified as optional. When a
gap is reclassified, annotate in RECLASSIFIED sub-section. Write `RECLASSIFIED: none`
if no reclassifications occurred. State explicitly when BLOCKING is empty:
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
     Zero-signal rule: when `found` is empty (zero signals across all namespaces),
     do not write "no signals found — synthesis not possible." The gap pattern is
     the evidence set. State what the uniform absence of signals implies about what
     has not been probed.

  2. What do the gaps leave genuinely uncertain?
     What is the class of unknown the gaps represent — the assumption set that
     remains untested, not the list of missing artifacts?

  3. What is the team's real exposure if they commit now?
     Not a list of what is missing — what could go wrong that this evidence does
     not rule out, and why does the current signal set fail to address it?>
```

Execution: Write prose that answers all three questions through the PERMITTED forms
only. The three-question structure is required regardless of signal coverage — sparse
evidence makes question 1 brief, not absent; question 1 must state a direction. When
`found` is empty, the gap pattern is the evidence set; question 1 must characterize
what uniform absence implies rather than vacating synthesis. If any NOT PERMITTED form
appears in this block, the synthesis has failed.

---

```
[VERDICT]
status:       READY | NOT READY | CONDITIONAL
rationale:    <one sentence>
inertia_cost: bounded: <residual risk and why recoverable post-commit>
              OR
              unbounded: <failure class and why irreversible once committed>

blocking:
  - <item>: <why it blocks>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` must classify
recoverability: `bounded:` when the team can detect and correct post-commit;
`unbounded:` when commitment triggers an irreversible state before detection is
possible. Required at every verdict status — even READY must declare that remaining
risk is bounded and why. A CONDITIONAL verdict must name the condition and what
satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-03 — Axis: C-22 structural hardening — zero-signal mandate as named execution rule

**Hypothesis:** R6 V-05 placed the zero-signal rule inside STORY question 1's body
text: "Zero-signal rule: when `found` is empty... the gap pattern is the evidence set."
This is a behavioral advisory embedded in a question prompt. C-22 tests whether an
explicit synthesis mandate exists — it requires not just that the clause is present
but that it closes the specific failure mode: a model receiving zero signals writing
"no signals found — synthesis not possible" and vacating STORY. V-03 promotes the
zero-signal rule from a question-body note to a standalone named execution mandate
in the STORY execution note, stated as two explicit operational requirements rather
than advisory text. Hypothesis: the promotion changes the compliance signal from
"clause present" to "clause is an execution requirement" — PASS remains but the
failure mode is more explicitly foreclosed. If C-22 already scores PASS in V-01,
V-03 provides a structurally cleaner implementation for use as the R8 base.

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
one entry regardless of how many fields follow it. Per-entry field count is orthogonal
to the threshold. Timestamps on found signals are not part of the density contract
and must never be dropped or abbreviated regardless of FULL/COMPRESSED trigger.

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
A gap that cannot be answered with both fields is reclassified as optional. Annotate
reclassifications in the RECLASSIFIED sub-section. Write `RECLASSIFIED: none` if none.
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
only. The three-question structure is required regardless of signal coverage.

**Zero-signal synthesis mandate:** When `found` is empty (zero signals across all
namespaces), do not write "no signals found — synthesis not possible" and do not
omit or hollow the STORY block. This is a non-vacating requirement:
  (1) Empty `found` is not grounds for omitting synthesis — the gap pattern is the
      evidence set.
  (2) Question 1 must characterize what uniform absence implies: what surface of the
      problem has not been probed at all, and what that means for the decision. "The
      absence of any scout signal indicates the market surface has not been probed"
      is a valid answer; "insufficient data" is not.
Sparse evidence makes question 1 brief, not absent. Zero signals makes question 1 a
characterization of the gap pattern, not a non-answer.

---

```
[VERDICT]
status:       READY | NOT READY | CONDITIONAL
rationale:    <one sentence>
inertia_cost: bounded: <residual risk and why recoverable post-commit>
              OR
              unbounded: <failure class and why irreversible once committed>

blocking:
  - <item>: <why it blocks>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` must classify
recoverability: `bounded:` when the team can detect and correct post-commit;
`unbounded:` when commitment triggers an irreversible state before detection is
possible. Required at every verdict status — even READY must declare that remaining
risk is bounded and why. A CONDITIONAL verdict must name the condition and what
satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-04 — Axis: C-23 syntax enforcement — bounded/unbounded as required field grammar

**Hypothesis:** R6 V-05 restructured `inertia_cost` from "one sentence" to a
two-form template at the VERDICT block level: `bounded: <...>` OR `unbounded: <...>`.
The VERDICT execution note adds: "classify recoverability: use `bounded:` when...;
use `unbounded:` when...". C-23 tests that the team can derive their action posture
from the VERDICT block alone without re-reading item-level gap fields. V-01 confirms
C-23 PASS from R6 V-05. V-04 tests whether making the bounded/unbounded grammar even
more explicit — adding the consequence of each choice (action posture) directly to
the field definition — strengthens the rubric signal or simply adds redundant text.
The V-04 change: the VERDICT template explicitly states what each form licenses the
team to do: `bounded` = commit with monitoring; `unbounded` = do not commit until
resolved. This maps the field value directly to an action, making the C-23 compliance
signal unmistakable. If V-04 = V-01 in scoring, the action-posture text is redundant
and R8 can simplify. If V-04 > V-01, the action-posture text was supplying something
C-23 required that V-01 did not provide.

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
one entry regardless of how many fields follow it. Per-entry field count is orthogonal
to the threshold. Timestamps on found signals are not part of the density contract
and must never be dropped or abbreviated regardless of FULL/COMPRESSED trigger.

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
A gap that cannot be answered with both fields is reclassified as optional. Annotate
reclassifications in the RECLASSIFIED sub-section. Write `RECLASSIFIED: none` if none.
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
     Zero-signal rule: when `found` is empty (zero signals across all namespaces),
     do not write "no signals found — synthesis not possible." The gap pattern is
     the evidence set. State what the uniform absence of signals implies about what
     has not been probed.

  2. What do the gaps leave genuinely uncertain?
     What is the class of unknown the gaps represent — the assumption set that
     remains untested, not the list of missing artifacts?

  3. What is the team's real exposure if they commit now?
     Not a list of what is missing — what could go wrong that this evidence does
     not rule out, and why does the current signal set fail to address it?>
```

Execution: Write prose that answers all three questions through the PERMITTED forms
only. The three-question structure is required regardless of signal coverage — sparse
evidence makes question 1 brief, not absent; question 1 must state a direction. When
`found` is empty, the gap pattern is the evidence set; question 1 must characterize
what uniform absence implies rather than vacating synthesis. If any NOT PERMITTED form
appears in this block, the synthesis has failed.

---

```
[VERDICT]
status:       READY | NOT READY | CONDITIONAL
rationale:    <one sentence>
inertia_cost:
  bounded: <residual risk + why detectable and recoverable post-commit>
    action: commit with monitoring
  OR
  unbounded: <failure class + why it propagates to irreversible state before detection>
    action: do not commit until resolved

blocking:
  - <item>: <why it blocks>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` must declare the
recoverability class explicitly:

- Use `bounded:` when the team can observe the failure post-commit and course-correct
  before it cascades. State the residual risk and the detection mechanism. The action
  posture is: commit with monitoring.
- Use `unbounded:` when commitment triggers a state that becomes irreversible before
  detection is possible — an audit trail, a partner agreement, a public announcement,
  a data migration. State the failure class and why the propagation is irreversible.
  The action posture is: do not commit until this is resolved.

The team must be able to read the `inertia_cost` field alone and derive their action
posture without consulting any other block. Required at every verdict status — even
READY must declare that remaining risk is bounded and why. A CONDITIONAL verdict must
name the condition, what satisfies it, and what recoverability class applies if the
team proceeds before the condition is met.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-05 — Axes: All three (V-02 + V-03 + V-04 combined)

**Hypothesis:** V-02, V-03, and V-04 operate on structurally independent locations:
V-02 targets the STATUS density contract preamble (`found:` section exemption stated
twice); V-03 targets the STORY execution note (zero-signal mandate as named rule);
V-04 targets the VERDICT template (`inertia_cost` as action-posture field grammar).
No interaction effects are expected. V-05 = 230/230. If V-05 scores lower than V-04,
the combination introduces a conflict — trace which axis pair creates it. If V-05
= V-01 with no scoring difference, all three axes are pure robustness additions: the
rubric is fully satisfied by R6 V-05 and R7 has confirmed the structural hardening
candidates for R8 consideration. V-05 is the preferred R8 base: maximum structural
coverage, zero rubric cost, all known failure modes foreclosed at the template level.

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
one entry regardless of how many fields follow it. Per-entry field count is orthogonal
to the threshold.

**Found-signal timestamp isolation rule:** The density contract and FULL/COMPRESSED
format choice govern the BLOCKING section only. The `found:` section is exempt from
the density contract in all cases. Timestamps on found signals must appear in full
(`<ns>/<artifact>  <date>`) regardless of whether FULL or COMPRESSED format is active
for the BLOCKING section. Do not abbreviate, truncate, or omit found-signal timestamps
when COMPRESSED format is triggered.

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>          <- timestamps required; not subject to density contract
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
A gap that cannot be answered with both fields is reclassified as optional. Annotate
reclassifications in the RECLASSIFIED sub-section. Write `RECLASSIFIED: none` if none.
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
only. The three-question structure is required regardless of signal coverage.

**Zero-signal synthesis mandate:** When `found` is empty (zero signals across all
namespaces), do not write "no signals found — synthesis not possible" and do not
omit or hollow the STORY block. This is a non-vacating requirement:
  (1) Empty `found` is not grounds for omitting synthesis — the gap pattern is the
      evidence set.
  (2) Question 1 must characterize what uniform absence implies: what surface of the
      problem has not been probed at all, and what that means for the decision. "The
      absence of any scout signal indicates the market surface has not been probed"
      is a valid answer; "insufficient data" is not.
Sparse evidence makes question 1 brief, not absent. Zero signals makes question 1 a
characterization of the gap pattern, not a non-answer.

---

```
[VERDICT]
status:       READY | NOT READY | CONDITIONAL
rationale:    <one sentence>
inertia_cost:
  bounded: <residual risk + why detectable and recoverable post-commit>
    action: commit with monitoring
  OR
  unbounded: <failure class + why it propagates to irreversible state before detection>
    action: do not commit until resolved

blocking:
  - <item>: <why it blocks>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` must declare the
recoverability class explicitly:

- Use `bounded:` when the team can observe the failure post-commit and course-correct
  before it cascades. State the residual risk and the detection mechanism. The action
  posture is: commit with monitoring.
- Use `unbounded:` when commitment triggers a state that becomes irreversible before
  detection is possible. State the failure class and why the propagation is irreversible.
  The action posture is: do not commit until this is resolved.

The team must be able to read the `inertia_cost` field alone and derive their action
posture without consulting any other block. Required at every verdict status — even
READY must declare that remaining risk is bounded and why. A CONDITIONAL verdict must
name the condition, what satisfies it, and what recoverability class applies if the
team proceeds before the condition is met.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

**Key differentiators to watch in scoring:**

- **V-01** is the pure baseline — confirms C-22 and C-23 PASS from R6 V-05 alone.
  If V-01 = 230/230, R7's rubric additions are already fully satisfied by R6 V-05.
  All subsequent variations are structural hardening, not gap-closing.

- **V-02** is the cleanest C-16 timestamp isolation test under the COMPRESSED path.
  The change: isolation rule stated twice (density contract preamble and STATUS template
  comment). If V-02 = V-01 in scoring, the single-sentence version in V-01 is sufficient
  and the second instance adds no rubric signal. If V-02 > V-01 (unexpected), the
  second instance was supplying something C-16 required.

- **V-03** tests whether promoting the zero-signal mandate from question 1 body text
  to a named execution rule in the STORY execution note produces any scoring difference.
  Expected: V-03 = V-01. If V-03 > V-01, C-22's PASS gate requires a named rule, not
  embedded question text — the R6 V-05 clause was advisory, not structural. This would
  mean V-01 is actually PARTIAL on C-22 and V-03 is the real ceiling fix.

- **V-04** tests whether the action-posture labels (`action: commit with monitoring` /
  `action: do not commit until resolved`) attached to the bounded/unbounded sub-fields
  produce any C-23 scoring difference. C-23 PASS requires the team to derive action
  posture from the verdict block alone. V-01 provides the bounded/unbounded syntax;
  V-04 explicitly maps each to an action. If V-04 > V-01, action-posture derivability
  requires explicit labels. If V-04 = V-01, the bounded/unbounded syntax alone carries
  the action posture signal.

- **V-05** is the maximalist hardening sweep. Three structurally independent axes on
  the same base. Expected: 230/230, identical to V-01. V-05 is the preferred R8 base
  if the goal is maximum failure-mode coverage at zero rubric cost. If V-05 < V-04,
  the V-02 timestamp isolation annotation (the inline `<- timestamps required` comment
  in the STATUS template) interacts with a criterion that prohibits inline template
  comments — investigate C-01 (terminal dashboard format requirement).
