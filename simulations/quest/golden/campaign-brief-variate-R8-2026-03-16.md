---
skill: quest-variate
skill_target: campaign-brief
round: 8
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-brief-rubric-v8-2026-03-16.md
---

# Variations — campaign-brief / Round 8

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

**R7 recap:** V-02 and V-05 tied at 230/260 (under v7, 23 criteria). Both passed
C-16 (per-signal timestamps in `found`), C-21 (sparse synthesis), C-22 (zero-signal
mandate — embedded clause form inside STORY execution note), and C-23 (bounded/unbounded
at verdict level, but unnamed action posture). The three patterns that reached 230
but not 260: (1) timestamp isolation stated at one structural location only — the STATUS
execution note — creating a single-point-of-failure when COMPRESSED elides that section
before reaching the note; (2) zero-signal rule embedded in STORY execution note rather
than promoted to standalone named rule, making it context-distant from synthesis entry
when `found` is large; (3) bounded/unbounded classification present but without explicit
action-posture sub-labels, requiring the team to infer the commit posture from the
category name alone.

**R8 rubric adds:** C-24 (dual-location timestamp isolation rule), C-25 (zero-signal
mandate as standalone named execution rule with two operational clauses), C-26
(action-posture sub-labels on bounded/unbounded inertia field). Max score climbs from
230 to 260.

**R8 targets:** Falsify the COMPRESSED x timestamp risk (C-24): verify that
dual-location instruction placement ensures timestamp survival when one location is
elided under COMPRESSED. Confirm that a named zero-signal rule outside STORY (C-25)
produces stronger synthesis than the embedded clause form. Verify that action-posture
sub-label syntax (C-26) is preserved in the VERDICT block when COMPRESSED abbreviates
the STATUS section.

**R9 investigation candidate from rubric:** Whether C-25's named-rule form survives
at higher token pressure than the embedded-clause form, and whether C-26's sub-label
syntax survives when COMPRESSED abbreviates the VERDICT block.

---

## Variation axes selected

- **Single-axis:** Timestamp dual-location (V-01), Zero-signal named rule (V-02),
  Action-posture sub-labels (V-03)
- **Combined:** C-24 + C-25 without C-26 (V-04), Full R8 sweep C-24 + C-25 + C-26 (V-05)

---

## V-01 — Axis: Timestamp dual-location (C-24 — isolation rule at two structural locations)

**Hypothesis:** R7 V-02 and V-05 stated the timestamp isolation instruction at one
location only — the STATUS execution note, placed after the blocking entry format
definitions. Under COMPRESSED (blocking gaps > 4), the model reads the STATUS block
format spec first and may abbreviate the found section before reaching the execution
note. V-01 adds a second instance of the isolation rule directly within the `found`
entry format spec — as an inline annotation on the date field — so the rule appears
at the point of format application, not just at the post-format execution note. The
hypothesis: a rule co-located with the field it protects survives COMPRESSED
abbreviation even when the execution note is elided, because the format spec itself
carries the invariant. The C-22 embedded clause (zero-signal, inside STORY execution
note) and C-23 bounded/unbounded (without action-posture sub-labels) are held at
R7 form to isolate the C-24 axis. Expected: C-24 PASS, C-25 FAIL, C-26 FAIL.
If V-01 scores 240/260, the dual-location mechanism is confirmed as sufficient.
If still 230, one of the two locations is being elided before the rule is processed —
a signal that location 1 must be in the STORY execution note (always reached last).

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. Every blocking gap must name the commit-risk —
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
prior_verdict: <READY | NOT READY | CONDITIONAL, or NONE>

signals_added:
  - <ns>/<artifact>  <date>
  (or: none)

gaps_closed:
  - <ns>/<skill>/<item>  (was: BLOCKING | OPTIONAL)
  (or: none)

verdict_shift: NO CHANGE | IMPROVED | DEGRADED — <one sentence if changed, or N/A>
```

Execution: Glob `simulations/{{topic}}/campaign-brief-*.md` for the most recent prior
brief. Extract its STATUS (found/missing) and VERDICT. Compare to current state.
If this is the first run, write: prior_brief: NONE — first run. Mark all remaining
delta fields as N/A. This block is required on first run.

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

STATUS density contract: Count blocking missing signals before formatting.
Use FULL format if blocking gaps <= 4. Use COMPRESSED + [BLOCKING-DETAIL] if > 4.

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>   ← timestamp is structurally separate from blocking
                               entries; this date field is NOT part of the blocking
                               entry format and must NOT be abbreviated, collapsed,
                               or omitted regardless of which format branch is active
  ...

missing: Y signals

  BLOCKING:

  [FULL FORMAT — blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
    ...

  [COMPRESSED FORMAT — blocking gaps > 4 (full fields in [BLOCKING-DETAIL] below):]
    - <ns>/<skill>/<item> — <inertia risk, <=12 words>
    ...

  OPTIONAL:
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking gap, `Inertia risk:` is required. A gap with no articulable inertia risk
is optional. State explicitly when empty: `BLOCKING: none — all gaps are optional`.
TIMESTAMP ISOLATION: per-signal dates in the `found` section are structurally
separate from blocking entries and must be preserved at item level. COMPRESSED format
applies only to blocking entry verbosity — `found` timestamps must not be collapsed
or summarized regardless of blocking gap count.

---

If COMPRESSED format was triggered, produce immediately after STATUS:

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
| Dimension      | Score (1-3) | Rationale                                                |
|----------------|-------------|----------------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+)        |
| Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong)|
| Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/opt.) |

average: (breadth + depth + severity) / 3 = X.X
level:   LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
binding: <the dimension that determines the level — lowest score, or tie-breaker>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically.
CONFIDENCE is a standalone block — do not embed inside STORY.

---

```
[STORY]
<2-4 paragraphs. Prose only.

Rules for this block:
- No tables, no bullet lists.
- No artifact filenames — refer by category (e.g., "the flow signals").
- Do not restate the confidence level — it is in [CONFIDENCE].
- Address inertia risk as a pattern across blocking gaps, not per gap.
- Sparse coverage: if found contains signals from only 1-2 namespaces, do not
  default to a coverage disclaimer — synthesize on the available signals.
- Zero coverage: if found is empty, uniform absence is itself evidence; question 1
  must characterize what uniform absence implies — not report absence as a non-answer.

The narrative must answer these three questions in continuous prose:
  1. What case do the signals make together?
  2. What do the gaps leave genuinely uncertain?
  3. What is the team's real exposure if they commit now?>
```

Execution: Synthesize STATUS and CONFIDENCE findings into a coherent narrative arc.
STORY owns cross-signal reasoning; STATUS and CONFIDENCE hold structured records.

---

```
[VERDICT]
status:       READY | NOT READY | CONDITIONAL
rationale:    <one sentence>
inertia_cost: bounded: <residual risk and why the team can detect and correct post-commit>
              OR
              unbounded: <failure class and why the failure propagates to an irreversible
                          state before detection is possible>

blocking:
  - <item>: <why it blocks>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` is required at every
verdict status — even READY. Declare bounded or unbounded: a verdict without this
classification forces the team to re-read all item-level gap fields to derive their
action posture. A CONDITIONAL verdict must name the condition and what satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-02 — Axis: Zero-signal named rule (C-25 — standalone execution rule with two operational clauses)

**Hypothesis:** R7 V-02 embedded the zero-signal mandate as a clause inside the STORY
execution note. This satisfies C-22 (embedded clause present) but not C-25 (standalone
named rule with two operational clauses). The failure mode for the embedded form: when
`found` contains many signals, the model enters STORY synthesis in its general-synthesis
mode — the zero-signal clause is context-distant and may be suppressed by the dominant
non-empty path. V-02 promotes the mandate to a standalone named rule — ZERO-SIGNAL
SYNTHESIS RULE — placed between [CONFIDENCE] and [STORY], outside either block's
execution note, with two explicitly numbered clauses. The hypothesis: a named rule
stated before the synthesis block creates a structural gate the model must resolve
regardless of `found` coverage level — the rule fires unconditionally, not only when
the model detects an empty `found` section. C-24 (dual-location timestamps) is
deliberately held at single-location form (execution note only, as in R7) to isolate
the C-25 axis. C-26 action-posture sub-labels are absent to further isolate.
Expected: C-24 FAIL, C-25 PASS, C-26 FAIL — net 240/260.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. Every blocking gap must name the commit-risk —
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
prior_verdict: <READY | NOT READY | CONDITIONAL, or NONE>

signals_added:
  - <ns>/<artifact>  <date>
  (or: none)

gaps_closed:
  - <ns>/<skill>/<item>  (was: BLOCKING | OPTIONAL)
  (or: none)

verdict_shift: NO CHANGE | IMPROVED | DEGRADED — <one sentence if changed, or N/A>
```

Execution: Glob `simulations/{{topic}}/campaign-brief-*.md` for the most recent prior
brief. If first run, write: prior_brief: NONE — first run, remaining fields N/A.

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

STATUS density contract: Count blocking missing signals before formatting.
Use FULL format if blocking gaps <= 4. Use COMPRESSED + [BLOCKING-DETAIL] if > 4.

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>
  ...

missing: Y signals

  BLOCKING:

  [FULL FORMAT — blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
    ...

  [COMPRESSED FORMAT — blocking gaps > 4 (full fields in [BLOCKING-DETAIL] below):]
    - <ns>/<skill>/<item> — <inertia risk, <=12 words>
    ...

  OPTIONAL:
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking gap, `Inertia risk:` is required. A gap with no articulable inertia risk is
optional. State explicitly when empty: `BLOCKING: none — all gaps are optional`.
Per-signal timestamps in the `found` section are structurally separate from blocking
entries and must appear at item level regardless of blocking gap count.

---

If COMPRESSED format was triggered, produce immediately after STATUS:

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
| Dimension      | Score (1-3) | Rationale                                                |
|----------------|-------------|----------------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+)        |
| Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong)|
| Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/opt.) |

average: (breadth + depth + severity) / 3 = X.X
level:   LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
binding: <the dimension that determines the level>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically.
Standalone block — do not embed inside STORY.

---

ZERO-SIGNAL SYNTHESIS RULE

When the `found` section of STATUS contains zero signals across all namespaces,
two execution clauses apply unconditionally:

  1. Empty `found` is not grounds for omitting, hollowing, or shortening the STORY
     block. The LLM failure mode to avoid: "no signals found — synthesis not
     possible." A STORY block that reports absence without characterizing what
     absence implies is a non-finding and fails this rule.

  2. Question 1 of the STORY narrative must characterize what uniform absence
     implies about the topic's investigation state. "The absence of any scout
     signal indicates the market surface has not been probed at all" is valid
     synthesis. "Insufficient data to synthesize" is not.

Basis: uniform absence is itself evidence. The gap pattern — no namespace has been
probed — defines what the team does not know and why they are not ready. That
pattern is the evidence set. STORY must synthesize from it.

This rule is distinct from the sparse-coverage rule (1-2 namespaces with signals):
sparse coverage has a partial evidence set; zero coverage has a complete absence
evidence set. Both require synthesis. Neither permits disclaimer substitution.

---

```
[STORY]
<2-4 paragraphs. Prose only.

Rules for this block:
- No tables, no bullet lists.
- No artifact filenames — refer by category (e.g., "the flow signals").
- Do not restate the confidence level — it is in [CONFIDENCE].
- Address inertia risk as a pattern across blocking gaps, not per gap.
- Sparse coverage: if found contains signals from only 1-2 namespaces, synthesize
  on available signals — do not default to a coverage disclaimer.
- Zero coverage: governed by ZERO-SIGNAL SYNTHESIS RULE above.

The narrative must answer these three questions in continuous prose:
  1. What case do the signals make together?
     (If found is empty: what does uniform absence imply about investigation state?)
  2. What do the gaps leave genuinely uncertain?
  3. What is the team's real exposure if they commit now?>
```

Execution: Synthesize STATUS and CONFIDENCE findings. STORY owns cross-signal
reasoning; STATUS and CONFIDENCE hold structured records.

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

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` required at every
verdict status. Declare bounded or unbounded. A CONDITIONAL verdict must name the
condition and what satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, [ZERO-SIGNAL SYNTHESIS RULE as execution rule, not output block],
STORY, VERDICT.

---

## V-03 — Axis: Action-posture sub-labels (C-26 — bounded/unbounded with explicit commit-posture names)

**Hypothesis:** R7 V-05 passed C-23 by declaring `bounded:` or `unbounded:` on the
`inertia_cost` field in VERDICT. But the rubric's C-26 pattern requires that the
sub-label carry the action-posture name — not just the category — so the team can
derive commit behavior from the VERDICT block alone without looking up the category
definition. The R7 form named recoverability but omitted the downstream action: "bounded"
tells the team what class of risk it is; "commit with monitoring" tells them what to do
about it. V-03 adds `action: commit with monitoring` and `action: do not commit until
resolved` as required sub-labels following the bounded/unbounded classification. The
hypothesis: explicit action-posture sub-labels make VERDICT self-contained — the team
does not re-read STORY or item-level inertia fields to know their posture. C-24 and C-25
are held at R7 form (single-location timestamp, embedded zero-signal clause) to isolate
the C-26 axis. Expected: C-24 FAIL, C-25 FAIL, C-26 PASS — net 240/260.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. Every blocking gap must name the commit-risk —
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
prior_verdict: <READY | NOT READY | CONDITIONAL, or NONE>

signals_added:
  - <ns>/<artifact>  <date>
  (or: none)

gaps_closed:
  - <ns>/<skill>/<item>  (was: BLOCKING | OPTIONAL)
  (or: none)

verdict_shift: NO CHANGE | IMPROVED | DEGRADED — <one sentence if changed, or N/A>
```

Execution: Glob `simulations/{{topic}}/campaign-brief-*.md`. If first run, write:
prior_brief: NONE — first run, remaining fields N/A.

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

STATUS density contract: Count blocking missing signals before formatting.
Use FULL format if blocking gaps <= 4. Use COMPRESSED + [BLOCKING-DETAIL] if > 4.

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>
  ...

missing: Y signals

  BLOCKING:

  [FULL FORMAT — blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
    ...

  [COMPRESSED FORMAT — blocking gaps > 4 (full fields in [BLOCKING-DETAIL] below):]
    - <ns>/<skill>/<item> — <inertia risk, <=12 words>
    ...

  OPTIONAL:
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking gap, `Inertia risk:` is required. A gap with no articulable inertia risk is
optional. State explicitly when empty: `BLOCKING: none — all gaps are optional`.
Per-signal timestamps in the `found` section are structurally separate from blocking
entries and must appear at item level regardless of blocking gap count.

---

If COMPRESSED format was triggered, produce immediately after STATUS:

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
| Dimension      | Score (1-3) | Rationale                                                |
|----------------|-------------|----------------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+)        |
| Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong)|
| Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/opt.) |

average: (breadth + depth + severity) / 3 = X.X
level:   LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
binding: <the dimension that determines the level>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically.
Standalone block — do not embed inside STORY.

---

```
[STORY]
<2-4 paragraphs. Prose only.

Rules for this block:
- No tables, no bullet lists.
- No artifact filenames — refer by category (e.g., "the flow signals").
- Do not restate the confidence level — it is in [CONFIDENCE].
- Address inertia risk as a pattern across blocking gaps, not per gap.
- Sparse coverage: if found contains signals from only 1-2 namespaces, synthesize
  on available signals — do not default to a coverage disclaimer.
- Zero coverage: if found is empty, uniform absence is itself evidence; question 1
  must characterize what uniform absence implies — not report absence as a non-answer.

The narrative must answer these three questions in continuous prose:
  1. What case do the signals make together?
     (If found is empty: what does uniform absence imply about investigation state?)
  2. What do the gaps leave genuinely uncertain?
  3. What is the team's real exposure if they commit now?>
```

Execution: Synthesize STATUS and CONFIDENCE findings. STORY owns cross-signal
reasoning; STATUS and CONFIDENCE hold structured records.

---

```
[VERDICT]
status:       READY | NOT READY | CONDITIONAL
rationale:    <one sentence>
inertia_cost:
  bounded: <residual risk and why the team can detect the failure post-commit
            and course-correct before it propagates>
    action: commit with monitoring
  OR
  unbounded: <failure class and why the failure propagates to an irreversible state
              before detection is possible>
    action: do not commit until resolved

blocking:
  - <item>: <why it blocks>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` is required at every
verdict status — even READY ("bounded: remaining risk is X and recoverable because Y
— action: commit with monitoring"). Declare bounded or unbounded with its action
sub-label. The action sub-label is what makes the VERDICT self-contained — the team
must be able to derive their commit posture from this block alone without re-reading
STORY or item-level gap entries. A CONDITIONAL verdict must name the condition and
what satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-04 — Axes: C-24 + C-25 combined (timestamp dual-location + zero-signal named rule; no C-26)

**Hypothesis:** V-01 isolates C-24 (expected 240/260: C-24 PASS, C-25 FAIL, C-26 FAIL).
V-02 isolates C-25 (expected 240/260: C-24 FAIL, C-25 PASS, C-26 FAIL). V-04 combines
both axes without C-26 — the cleanest additive test for the first two new criteria. The
goal is to confirm they co-exist without structural conflict: the dual-location timestamp
rule adds two notes to STATUS, the named zero-signal rule adds a standalone block between
CONFIDENCE and STORY. Neither competes for the same structural location. If additive,
V-04 should score 250/260 (C-24 PASS + C-25 PASS, C-26 FAIL). If V-04 scores lower than
the sum of individual scores, a structural interaction is present — the investigation
target would be whether the named rule's placement disrupts STORY execution when the
timestamp isolation note is also present. C-26 is deliberately absent to prevent a
three-way interaction from masking the C-24/C-25 additivity signal.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. Every blocking gap must name the commit-risk —
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
prior_verdict: <READY | NOT READY | CONDITIONAL, or NONE>

signals_added:
  - <ns>/<artifact>  <date>
  (or: none)

gaps_closed:
  - <ns>/<skill>/<item>  (was: BLOCKING | OPTIONAL)
  (or: none)

verdict_shift: NO CHANGE | IMPROVED | DEGRADED — <one sentence if changed, or N/A>
```

Execution: Glob `simulations/{{topic}}/campaign-brief-*.md`. If first run, write:
prior_brief: NONE — first run, remaining fields N/A.

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

STATUS density contract: Count blocking missing signals before formatting.
Use FULL format if blocking gaps <= 4. Use COMPRESSED + [BLOCKING-DETAIL] if > 4.

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>   ← timestamp is structurally separate from blocking
                               entries; must NOT be abbreviated or omitted under
                               any format branch — COMPRESSED applies to blocking
                               entries only, not to found item dates
  ...

missing: Y signals

  BLOCKING:

  [FULL FORMAT — blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
    ...

  [COMPRESSED FORMAT — blocking gaps > 4 (full fields in [BLOCKING-DETAIL] below):]
    - <ns>/<skill>/<item> — <inertia risk, <=12 words>
    ...

  OPTIONAL:
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking gap, `Inertia risk:` is required. A gap with no articulable inertia risk is
optional. State explicitly when empty: `BLOCKING: none — all gaps are optional`.
TIMESTAMP ISOLATION: per-signal dates in the `found` section are structurally
separate from blocking entries. COMPRESSED format governs blocking entry verbosity
only — found timestamps must appear at item level regardless of blocking gap count.

---

If COMPRESSED format was triggered, produce immediately after STATUS:

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
| Dimension      | Score (1-3) | Rationale                                                |
|----------------|-------------|----------------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+)        |
| Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong)|
| Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/opt.) |

average: (breadth + depth + severity) / 3 = X.X
level:   LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
binding: <the dimension that determines the level>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically.
Standalone block — do not embed inside STORY.

---

ZERO-SIGNAL SYNTHESIS RULE

When the `found` section of STATUS contains zero signals across all namespaces,
two execution clauses apply unconditionally:

  1. Empty `found` is not grounds for omitting, hollowing, or shortening the STORY
     block. The LLM failure mode to avoid: "no signals found — synthesis not
     possible." A STORY block that reports absence without characterizing what
     absence implies is a non-finding and fails this rule.

  2. Question 1 of the STORY narrative must characterize what uniform absence
     implies about the topic's investigation state. "The absence of any scout
     signal indicates the market surface has not been probed at all" is valid
     synthesis. "Insufficient data to synthesize" is not.

Basis: uniform absence is itself evidence. The gap pattern — no namespace has been
probed — defines what the team does not know and why they are not ready. That
pattern is the evidence set. STORY must synthesize from it.

This rule is structurally distinct from the sparse-coverage rule (signals in 1-2
namespaces). Both require synthesis. Neither permits disclaimer substitution.

---

```
[STORY]
<2-4 paragraphs. Prose only.

Rules for this block:
- No tables, no bullet lists.
- No artifact filenames — refer by category (e.g., "the flow signals").
- Do not restate the confidence level — it is in [CONFIDENCE].
- Address inertia risk as a pattern across blocking gaps, not per gap.
- Sparse coverage: if found contains signals from only 1-2 namespaces, synthesize
  on available signals — do not default to a coverage disclaimer.
- Zero coverage: governed by ZERO-SIGNAL SYNTHESIS RULE above.

The narrative must answer these three questions in continuous prose:
  1. What case do the signals make together?
     (If found is empty: what does uniform absence imply about investigation state?)
  2. What do the gaps leave genuinely uncertain?
  3. What is the team's real exposure if they commit now?>
```

Execution: Synthesize STATUS and CONFIDENCE findings. STORY owns cross-signal
reasoning; STATUS and CONFIDENCE hold structured records.

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

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` required at every
verdict status. Declare bounded or unbounded. A CONDITIONAL verdict must name
the condition and what satisfies it.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-05 — Axes: Full R8 sweep (C-24 + C-25 + C-26 on R7 best base)

**Hypothesis:** V-04 targets C-24 + C-25 and is expected at 250/260. V-05 adds C-26
(action-posture sub-labels) to produce the first variation designed to achieve 260/260.
The structural additions are: (1) inline timestamp annotation in `found` format + STATUS
execution note restatement (C-24), (2) ZERO-SIGNAL SYNTHESIS RULE standalone block
with two numbered clauses (C-25), (3) `action: commit with monitoring` / `action: do
not commit until resolved` sub-labels on `inertia_cost` in VERDICT (C-26). The R9
investigation candidate from the rubric applies here: whether C-26's sub-label syntax
survives when COMPRESSED abbreviates the VERDICT block at high token pressure. If V-05
scores 260, the three-criterion combination is confirmed as non-conflicting and the full
structural decomposition model holds. If V-05 scores lower than V-04, a three-way
interaction is present and becomes R9's primary investigation target — most likely
the `action:` sub-label in VERDICT being elided under compression because VERDICT is
always the last block processed.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block — an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. Every blocking gap must name the commit-risk —
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
prior_verdict: <READY | NOT READY | CONDITIONAL, or NONE>

signals_added:
  - <ns>/<artifact>  <date>
  (or: none)

gaps_closed:
  - <ns>/<skill>/<item>  (was: BLOCKING | OPTIONAL)
  (or: none)

verdict_shift: NO CHANGE | IMPROVED | DEGRADED — <one sentence if changed, or N/A>
```

Execution: Glob `simulations/{{topic}}/campaign-brief-*.md` for the most recent prior
brief. Extract its STATUS (found/missing) and VERDICT. If first run, write:
prior_brief: NONE — first run, remaining fields N/A. This block is required on first run.

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

STATUS density contract: Count blocking missing signals before formatting.
Use FULL format if blocking gaps <= 4. Use COMPRESSED + [BLOCKING-DETAIL] if > 4.

```
[STATUS]
found: X signals
  <ns>/<artifact>  <date>   ← timestamp is structurally separate from blocking
                               entries; this field is NOT subject to COMPRESSED
                               abbreviation — found dates must appear at item level
                               regardless of blocking gap count
  ...

missing: Y signals

  BLOCKING:

  [FULL FORMAT — blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
    ...

  [COMPRESSED FORMAT — blocking gaps > 4 (full fields in [BLOCKING-DETAIL] below):]
    - <ns>/<skill>/<item> — <inertia risk, <=12 words>
    ...

  OPTIONAL:
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking gap, `Inertia risk:` is required. A gap with no articulable inertia risk is
optional. State explicitly when empty: `BLOCKING: none — all gaps are optional`.
TIMESTAMP ISOLATION: per-signal dates in the `found` section are structurally
separate from blocking entries. COMPRESSED format applies only to blocking entry
verbosity — `found` timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count. This restatement is the second structural location
for this rule; the first is the inline annotation on the date field above.

---

If COMPRESSED format was triggered, produce immediately after STATUS:

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
| Dimension      | Score (1-3) | Rationale                                                |
|----------------|-------------|----------------------------------------------------------|
| Signal breadth | 1/2/3       | Namespaces with >=1 signal (1=1-2, 2=3-5, 3=6+)        |
| Signal depth   | 1/2/3       | Within-namespace corroboration (1=none, 2=some, 3=strong)|
| Gap severity   | 1/2/3       | Blocking gap count (1=critical, 2=moderate, 3=none/opt.) |

average: (breadth + depth + severity) / 3 = X.X
level:   LOW (<1.7) | MEDIUM (1.7-2.3) | HIGH (>2.3)
binding: <the dimension that determines the level — lowest score, or tie-breaker>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically —
do not estimate. Standalone block; do not embed inside STORY.

---

ZERO-SIGNAL SYNTHESIS RULE

When the `found` section of STATUS contains zero signals across all namespaces,
two execution clauses apply unconditionally:

  1. Empty `found` is not grounds for omitting, hollowing, or shortening the STORY
     block. The LLM failure mode to avoid: "no signals found — synthesis not
     possible." A STORY block that reports absence without characterizing what
     absence implies is a non-finding and fails this rule.

  2. Question 1 of the STORY narrative must characterize what uniform absence
     implies about the topic's investigation state. "The absence of any scout
     signal indicates the market surface has not been probed at all" is valid
     synthesis. "Insufficient data to synthesize" is not.

Basis: uniform absence is itself evidence. The gap pattern — no namespace has been
probed — defines what the team does not know and why they are not ready. That
pattern is the evidence set. STORY must synthesize from it.

This rule is structurally distinct from the sparse-coverage rule (signals present
in only 1-2 namespaces). Both boundary conditions require synthesis. Neither permits
disclaimer substitution for the synthesis obligation.

---

```
[STORY]
<2-4 paragraphs. Prose only.

Rules for this block:
- No tables, no bullet lists.
- No artifact filenames — refer by category (e.g., "the flow signals").
- Do not restate the confidence level — it is in [CONFIDENCE].
- Address inertia risk as a pattern across blocking gaps, not per gap.
- Sparse coverage: if found contains signals from only 1-2 namespaces, synthesize
  on available signals — do not default to a coverage disclaimer.
- Zero coverage: governed by ZERO-SIGNAL SYNTHESIS RULE above.

The narrative must answer these three questions in continuous prose:
  1. What case do the signals make together?
     (If found is empty: what does uniform absence imply about investigation state?)
  2. What do the gaps leave genuinely uncertain?
  3. What is the team's real exposure if they commit now?>
```

Execution: Synthesize STATUS and CONFIDENCE findings into a coherent narrative arc.
STORY owns cross-signal reasoning; every other block owns its own record.

---

```
[VERDICT]
status:       READY | NOT READY | CONDITIONAL
rationale:    <one sentence>
inertia_cost:
  bounded: <residual risk and why the team can detect the failure post-commit
            and course-correct before it propagates>
    action: commit with monitoring
  OR
  unbounded: <failure class and why the failure propagates to an irreversible
              state before detection is possible>
    action: do not commit until resolved

blocking:
  - <item>: <why it blocks>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` is required at every
verdict status — even READY ("bounded: remaining risk is X and recoverable because Y
— action: commit with monitoring"). Declare bounded or unbounded with the action
sub-label. The action sub-label makes VERDICT self-contained: the team must be able
to derive their commit posture from this block alone without re-reading STORY or
item-level gap fields. A CONDITIONAL verdict must name the condition and what satisfies
it; its `inertia_cost` declares the recoverability class of the unresolved risk.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

**Key differentiators to watch in scoring:**

- **V-01** is the cleanest C-24 test: dual-location timestamp rule — inline annotation
  on the `found` date field AND STATUS execution note restatement. If C-24 PASS and
  R7 V-02 was C-24 FAIL with single-location, the inline format annotation is confirmed
  as the mechanism that survives COMPRESSED. If still FAIL, the inline annotation is
  being overridden by COMPRESSED before the format spec is applied.

- **V-02** is the cleanest C-25 test: standalone named ZERO-SIGNAL SYNTHESIS RULE
  with two numbered clauses, placed between CONFIDENCE and STORY. If C-25 PASS here
  and FAIL in R7 (embedded clause form), the structural promotion — rule outside STORY
  execution note — is the mechanism. The gate hypothesis: the model resolves the
  named rule before entering STORY synthesis regardless of `found` coverage level.

- **V-03** is the cleanest C-26 test: `action: commit with monitoring` and
  `action: do not commit until resolved` sub-labels on `inertia_cost`. If C-26 PASS
  and R7 was C-26 FAIL (bounded/unbounded present but no action posture), the sub-label
  syntax is confirmed as the mechanism for VERDICT self-containment.

- **V-04** tests C-24 + C-25 additivity without C-26. If V-04 scores 250 (= V-01 + V-02
  lift), the two criteria are structurally independent. If V-04 scores lower than 250,
  a C-24/C-25 interaction is present — the named rule's placement between CONFIDENCE
  and STORY may disrupt the path the model uses to reach the STATUS execution note
  where the timestamp restatement appears.

- **V-05** is the 260-ceiling test. If V-05 scores 260, the full three-criterion
  combination is confirmed non-conflicting and R9 can target rubric refinement rather
  than structural repair. If V-05 scores lower than V-04 despite correct implementation
  of all three criteria, the R9 investigation is the COMPRESSED x VERDICT interaction:
  whether `action:` sub-labels survive when VERDICT is the last block processed at
  high token pressure.
