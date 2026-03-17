---
skill: quest-variate
skill_target: campaign-brief
round: 9
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-brief-rubric-v8-2026-03-16.md
---

# Variations — campaign-brief / Round 9

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

**R8 recap:** V-05 implemented all three new criteria (C-24, C-25, C-26) and is the
expected 260/260 ceiling candidate. The three structural additions in V-05: (1) dual-location
timestamp isolation rule — inline annotation on the `found` date field + STATUS execution
note restatement; (2) ZERO-SIGNAL SYNTHESIS RULE as a standalone named block with two
numbered clauses, placed between CONFIDENCE and STORY; (3) `action: commit with monitoring`
and `action: do not commit until resolved` sub-labels on `inertia_cost` in VERDICT.

**R9 rubric:** Unchanged at v8 — 26 criteria, 260 pts max. No new criteria are promoted.
R9 is a token-pressure and compression stress test of the R8 structural gains.

**R9 investigation candidates (carried from rubric):**

1. **C-25 token pressure risk:** Whether the ZERO-SIGNAL SYNTHESIS RULE (standalone named
   rule, two clauses, placed between CONFIDENCE and STORY) survives at higher token pressure
   than the embedded-clause form. In R8, the rule is mid-document. At high token pressure —
   many `found` signals + many blocking gaps — the model may reach the STORY synthesis
   path in its dominant non-empty mode and skip the rule that only fires for the zero-coverage
   edge case. The risk: a rule placed in a conditional-context position is context-sensitive;
   naming the pressure scenario explicitly may force unconditional processing.

2. **C-26 COMPRESSED x VERDICT survival:** Whether `action:` sub-labels on `inertia_cost`
   survive when COMPRESSED format is active and VERDICT is the last block processed. Under
   COMPRESSED, the model abbreviates blocking entries before reaching VERDICT. Token budget
   may be depleted, causing VERDICT to be written in condensed form — preserving bounded/
   unbounded classification (C-23 PASS) but dropping the `action:` sub-label (C-26 FAIL).
   A survival guard naming this failure mode explicitly may prevent the elision.

**R9 targets:** (a) Determine whether an explicit token-pressure guard clause on the
ZERO-SIGNAL SYNTHESIS RULE prevents edge-case suppression when `found` is non-empty and
large. (b) Determine whether an explicit VERDICT compression guard ("action sub-labels are
required even under COMPRESSED") prevents sub-label elision when VERDICT is processed last.
(c) Test whether preamble placement of the ZERO-SIGNAL SYNTHESIS RULE (before phase execution
begins) is more compression-resistant than mid-document placement.

---

## Variation axes selected

- **Single-axis:** C-25 token-pressure guard (V-01), C-26 COMPRESSED x VERDICT guard (V-02),
  C-25 preamble placement (V-03)
- **Combined:** C-25 token-pressure + C-26 guard (V-04), Full R9 sweep — preamble + pressure +
  VERDICT guard (V-05)

---

## V-01 — Axis: C-25 token-pressure guard (explicit unconditional-firing clause on ZERO-SIGNAL SYNTHESIS RULE)

**Hypothesis:** R8 V-05 placed the ZERO-SIGNAL SYNTHESIS RULE between CONFIDENCE and STORY.
The rule fires when `found` is empty. At high token pressure — large `found` sections with
many signals and many BLOCKING entries — the model processes the rule in a context where
`found` is clearly non-empty. Because the rule's conditions are satisfied by non-empty
coverage, the model may infer the rule is dormant and skip applying it. This is not a
COMPRESSED format issue; it is a conditional-context suppression issue. V-01 adds a third
clause to the ZERO-SIGNAL SYNTHESIS RULE: "This rule does not suspend when `found` is
non-empty — it fires unconditionally at any token budget. It is stated here to prevent
suppression at high token pressure, not as evidence of its own non-applicability."
The hypothesis: naming the failure mode (conditional-context suppression) prevents the
model from treating the rule as dormant. The preamble position (V-03 axis) and the
VERDICT guard (V-02 axis) are held at R8 V-05 form to isolate this axis.
Expected: C-24 PASS, C-25 PASS (token-pressure guard active), C-26 PASS — net 260/260.
Falsification: if C-25 still FAIL despite the guard clause, the issue is positional, not
conditional — the preamble placement hypothesis (V-03) becomes the primary investigation.

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
  <ns>/<artifact>  <date>   <- timestamp is structurally separate from blocking
                               entries; this field is NOT subject to COMPRESSED
                               abbreviation -- found dates must appear at item level
                               regardless of blocking gap count
  ...

missing: Y signals

  BLOCKING:

  [FULL FORMAT -- blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
    ...

  [COMPRESSED FORMAT -- blocking gaps > 4 (full fields in [BLOCKING-DETAIL] below):]
    - <ns>/<skill>/<item> -- <inertia risk, <=12 words>
    ...

  OPTIONAL:
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking gap, `Inertia risk:` is required. A gap with no articulable inertia risk is
optional. State explicitly when empty: `BLOCKING: none -- all gaps are optional`.
TIMESTAMP ISOLATION: per-signal dates in the `found` section are structurally
separate from blocking entries. COMPRESSED format applies only to blocking entry
verbosity -- `found` timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count. This is the second structural location for the
timestamp isolation rule; the first is the inline annotation on the date field above.

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
binding: <the dimension that determines the level -- lowest score, or tie-breaker>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically --
do not estimate. Standalone block; do not embed inside STORY.

---

ZERO-SIGNAL SYNTHESIS RULE

When the `found` section of STATUS contains zero signals across all namespaces,
two execution clauses apply unconditionally:

  1. Empty `found` is not grounds for omitting, hollowing, or shortening the STORY
     block. The LLM failure mode to avoid: "no signals found -- synthesis not
     possible." A STORY block that reports absence without characterizing what
     absence implies is a non-finding and fails this rule.

  2. Question 1 of the STORY narrative must characterize what uniform absence
     implies about the topic's investigation state. "The absence of any scout
     signal indicates the market surface has not been probed at all" is valid
     synthesis. "Insufficient data to synthesize" is not.

TOKEN-PRESSURE GUARD: This rule does not suspend when `found` is non-empty. It
fires unconditionally at any token budget. The rule is stated here regardless of
current `found` coverage to prevent conditional-context suppression -- a failure
mode in which the model treats the rule as dormant because `found` is large. The
guard is not evidence of the rule's non-applicability; it is a structural firewall
against its suppression.

Basis: uniform absence is itself evidence. The gap pattern -- no namespace has been
probed -- defines what the team does not know and why they are not ready. That
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
- No artifact filenames -- refer by category (e.g., "the flow signals").
- Do not restate the confidence level -- it is in [CONFIDENCE].
- Address inertia risk as a pattern across blocking gaps, not per gap.
- Sparse coverage: if found contains signals from only 1-2 namespaces, synthesize
  on available signals -- do not default to a coverage disclaimer.
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
verdict status -- even READY ("bounded: remaining risk is X and recoverable because Y
-- action: commit with monitoring"). Declare bounded or unbounded with the action
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

## V-02 — Axis: C-26 COMPRESSED x VERDICT survival guard (action sub-labels required regardless of compression state)

**Hypothesis:** R8 V-05 placed the `action:` sub-labels inside the VERDICT format spec
with a clear template. But VERDICT is always the last block processed. Under COMPRESSED
(> 4 blocking gaps), the model has already written abbreviated blocking entries, the
BLOCKING-DETAIL expansion, CONFIDENCE, and STORY before reaching VERDICT. Token budget
is depleted. The observed failure mode: the model preserves `bounded:` or `unbounded:`
classification (C-23 PASS — established in R7) but elides the `action:` sub-label because
the sub-label is a format extension, not the primary content, and COMPRESSED-mode
processing favors primary-content preservation. V-02 adds a VERDICT survival guard: an
explicit note in the VERDICT execution instruction stating "action sub-labels are required
at every verdict status regardless of COMPRESSED format state -- VERDICT is never
abbreviated and the `action:` field is not optional." The hypothesis: naming the failure
mode (COMPRESSED x last-block elision) in the VERDICT execution note forces the model to
treat the sub-label as invariant rather than as optional format extension. C-24 and C-25
are held at R8 V-05 form (dual-location timestamp, mid-document named rule) to isolate
this axis. Expected: C-24 PASS, C-25 PASS (unchanged from V-05 base), C-26 PASS with
VERDICT guard active -- net 260/260. Falsification: if C-26 still FAIL despite the guard,
the issue is token-budget depletion at the VERDICT generation step, not format inference --
the R10 investigation would target VERDICT block elevation (placing VERDICT before STORY).

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block -- an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. Every blocking gap must name the commit-risk --
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

verdict_shift: NO CHANGE | IMPROVED | DEGRADED -- <one sentence if changed, or N/A>
```

Execution: Glob `simulations/{{topic}}/campaign-brief-*.md` for the most recent prior
brief. Extract its STATUS (found/missing) and VERDICT. Compare to current state.
If this is the first run, write: prior_brief: NONE -- first run. Mark all remaining
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
  <ns>/<artifact>  <date>   <- timestamp is structurally separate from blocking
                               entries; this field is NOT subject to COMPRESSED
                               abbreviation -- found dates must appear at item level
                               regardless of blocking gap count
  ...

missing: Y signals

  BLOCKING:

  [FULL FORMAT -- blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
    ...

  [COMPRESSED FORMAT -- blocking gaps > 4 (full fields in [BLOCKING-DETAIL] below):]
    - <ns>/<skill>/<item> -- <inertia risk, <=12 words>
    ...

  OPTIONAL:
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking gap, `Inertia risk:` is required. A gap with no articulable inertia risk is
optional. State explicitly when empty: `BLOCKING: none -- all gaps are optional`.
TIMESTAMP ISOLATION: per-signal dates in the `found` section are structurally
separate from blocking entries. COMPRESSED format applies only to blocking entry
verbosity -- `found` timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count. This is the second structural location for the
timestamp isolation rule; the first is the inline annotation on the date field above.

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
binding: <the dimension that determines the level -- lowest score, or tie-breaker>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically --
do not estimate. Standalone block; do not embed inside STORY.

---

ZERO-SIGNAL SYNTHESIS RULE

When the `found` section of STATUS contains zero signals across all namespaces,
two execution clauses apply unconditionally:

  1. Empty `found` is not grounds for omitting, hollowing, or shortening the STORY
     block. The LLM failure mode to avoid: "no signals found -- synthesis not
     possible." A STORY block that reports absence without characterizing what
     absence implies is a non-finding and fails this rule.

  2. Question 1 of the STORY narrative must characterize what uniform absence
     implies about the topic's investigation state. "The absence of any scout
     signal indicates the market surface has not been probed at all" is valid
     synthesis. "Insufficient data to synthesize" is not.

Basis: uniform absence is itself evidence. The gap pattern -- no namespace has been
probed -- defines what the team does not know and why they are not ready. That
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
- No artifact filenames -- refer by category (e.g., "the flow signals").
- Do not restate the confidence level -- it is in [CONFIDENCE].
- Address inertia risk as a pattern across blocking gaps, not per gap.
- Sparse coverage: if found contains signals from only 1-2 namespaces, synthesize
  on available signals -- do not default to a coverage disclaimer.
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
verdict status -- even READY. Declare bounded or unbounded with the action sub-label.
VERDICT COMPRESSION GUARD: the `action:` sub-label on `inertia_cost` is required
regardless of COMPRESSED format state and regardless of token pressure. VERDICT is
never abbreviated. The action sub-label is not optional format -- it is the field that
makes VERDICT self-contained and enables the team to derive their commit posture from
this block alone without re-reading STORY or item-level gap entries. If COMPRESSED
was active for blocking entries, it does not extend to VERDICT fields. A CONDITIONAL
verdict must name the condition and what satisfies it; its `inertia_cost` must include
the `action:` sub-label specifying posture for the unresolved risk period.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-03 — Axis: C-25 preamble placement (ZERO-SIGNAL SYNTHESIS RULE elevated before phase execution)

**Hypothesis:** R8 placed the ZERO-SIGNAL SYNTHESIS RULE between CONFIDENCE and STORY --
a mid-document position. The model reads this rule after processing TOPIC, DELTA, STRATEGY,
and STATUS, having already entered block-execution mode. In block-execution mode, the model
applies rules in relation to the block being produced; a rule placed after CONFIDENCE may
be processed in the context of "about to write STORY" and discarded as non-applicable when
`found` is large. V-03 elevates the rule to preamble position: placed immediately after
the inertia framing statement and before "Run the phases in order." At the preamble
position, the model reads the rule before entering any block-execution mode -- the rule
is processed as a global execution constraint, not as a block-local note. The hypothesis:
global-constraint position prevents conditional-context suppression because the model has
not yet formed any synthesis expectation when it first encounters the rule. C-24 (dual-
location timestamps) is held at R8 V-05 form. C-25's preamble placement replaces the
mid-document placement but keeps the two-clause content. C-26 (action sub-labels) is
held at R8 V-05 form. Expected: C-24 PASS, C-25 PASS (preamble guard active), C-26 PASS
-- net 260/260. Falsification: if C-25 FAIL despite preamble placement, the failure mode
is content-based (rule wording does not produce the required synthesis behavior) rather
than position-based -- the token-pressure guard clause (V-01 axis) becomes the next test.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block -- an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. Every blocking gap must name the commit-risk --
what assumption the team is silently making if they ship today without that signal.

ZERO-SIGNAL SYNTHESIS RULE (global execution constraint -- applies to every run):

When the `found` section of STATUS contains zero signals across all namespaces,
two execution clauses apply unconditionally before any STORY synthesis begins:

  1. Empty `found` is not grounds for omitting, hollowing, or shortening the STORY
     block. The LLM failure mode to avoid: "no signals found -- synthesis not
     possible." A STORY block that reports absence without characterizing what
     absence implies is a non-finding and fails this rule.

  2. Question 1 of the STORY narrative must characterize what uniform absence
     implies about the topic's investigation state. "The absence of any scout
     signal indicates the market surface has not been probed at all" is valid
     synthesis. "Insufficient data to synthesize" is not.

Basis: uniform absence is itself evidence. The gap pattern -- no namespace has been
probed -- defines what the team does not know and why they are not ready. That
pattern is the evidence set. STORY must synthesize from it.

This rule is structurally distinct from the sparse-coverage rule (signals present
in only 1-2 namespaces). Both boundary conditions require synthesis. Neither permits
disclaimer substitution. This rule is stated here, before phase execution begins,
so that it is processed as a global constraint rather than as a block-local note.

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

verdict_shift: NO CHANGE | IMPROVED | DEGRADED -- <one sentence if changed, or N/A>
```

Execution: Glob `simulations/{{topic}}/campaign-brief-*.md` for the most recent prior
brief. Extract its STATUS (found/missing) and VERDICT. Compare to current state.
If this is the first run, write: prior_brief: NONE -- first run. Mark all remaining
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
  <ns>/<artifact>  <date>   <- timestamp is structurally separate from blocking
                               entries; this field is NOT subject to COMPRESSED
                               abbreviation -- found dates must appear at item level
                               regardless of blocking gap count
  ...

missing: Y signals

  BLOCKING:

  [FULL FORMAT -- blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
    ...

  [COMPRESSED FORMAT -- blocking gaps > 4 (full fields in [BLOCKING-DETAIL] below):]
    - <ns>/<skill>/<item> -- <inertia risk, <=12 words>
    ...

  OPTIONAL:
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking gap, `Inertia risk:` is required. A gap with no articulable inertia risk is
optional. State explicitly when empty: `BLOCKING: none -- all gaps are optional`.
TIMESTAMP ISOLATION: per-signal dates in the `found` section are structurally
separate from blocking entries. COMPRESSED format applies only to blocking entry
verbosity -- `found` timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count. This is the second structural location for the
timestamp isolation rule; the first is the inline annotation on the date field above.

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
binding: <the dimension that determines the level -- lowest score, or tie-breaker>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically --
do not estimate. Standalone block; do not embed inside STORY.

---

```
[STORY]
<2-4 paragraphs. Prose only.

Rules for this block:
- No tables, no bullet lists.
- No artifact filenames -- refer by category (e.g., "the flow signals").
- Do not restate the confidence level -- it is in [CONFIDENCE].
- Address inertia risk as a pattern across blocking gaps, not per gap.
- Sparse coverage: if found contains signals from only 1-2 namespaces, synthesize
  on available signals -- do not default to a coverage disclaimer.
- Zero coverage: governed by ZERO-SIGNAL SYNTHESIS RULE (stated in preamble above).

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
verdict status -- even READY. Declare bounded or unbounded with the action sub-label.
The action sub-label makes VERDICT self-contained: the team must be able to derive
their commit posture from this block alone without re-reading STORY or item-level gap
fields. A CONDITIONAL verdict must name the condition and what satisfies it; its
`inertia_cost` declares the recoverability class of the unresolved risk.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-04 — Axes: C-25 token-pressure guard + C-26 COMPRESSED x VERDICT guard (V-01 + V-02 combined; no C-25 preamble)

**Hypothesis:** V-01 isolates the C-25 token-pressure guard (expected 260/260: guard clause
prevents conditional-context suppression). V-02 isolates the C-26 VERDICT compression guard
(expected 260/260: named guard prevents action sub-label elision at last block). V-04
combines both without the C-25 preamble placement (V-03 axis) -- the mid-document position
is retained but hardened with the token-pressure guard clause. The goal: confirm that the
two guards are structurally independent and do not interact. A structural conflict would
appear as V-04 scoring lower than the sum of V-01 and V-02 lifts. The most likely
interaction: the token-pressure guard clause in the ZERO-SIGNAL SYNTHESIS RULE (between
CONFIDENCE and STORY) introduces additional instruction text that the model reads just
before STORY synthesis -- if the guard clause triggers STORY-mode processing too early,
the VERDICT compression guard (stated in VERDICT execution note, reached last) may be
consumed in a depleted-budget pass. If V-04 scores 260, both guards are confirmed as
additive. If V-04 scores lower, the guard clause's position-relative-to-VERDICT is the
investigation target.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block -- an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. Every blocking gap must name the commit-risk --
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

verdict_shift: NO CHANGE | IMPROVED | DEGRADED -- <one sentence if changed, or N/A>
```

Execution: Glob `simulations/{{topic}}/campaign-brief-*.md` for the most recent prior
brief. Extract its STATUS (found/missing) and VERDICT. Compare to current state.
If this is the first run, write: prior_brief: NONE -- first run. Mark all remaining
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
  <ns>/<artifact>  <date>   <- timestamp is structurally separate from blocking
                               entries; this field is NOT subject to COMPRESSED
                               abbreviation -- found dates must appear at item level
                               regardless of blocking gap count
  ...

missing: Y signals

  BLOCKING:

  [FULL FORMAT -- blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
    ...

  [COMPRESSED FORMAT -- blocking gaps > 4 (full fields in [BLOCKING-DETAIL] below):]
    - <ns>/<skill>/<item> -- <inertia risk, <=12 words>
    ...

  OPTIONAL:
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking gap, `Inertia risk:` is required. A gap with no articulable inertia risk is
optional. State explicitly when empty: `BLOCKING: none -- all gaps are optional`.
TIMESTAMP ISOLATION: per-signal dates in the `found` section are structurally
separate from blocking entries. COMPRESSED format applies only to blocking entry
verbosity -- `found` timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count. This is the second structural location for the
timestamp isolation rule; the first is the inline annotation on the date field above.

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
binding: <the dimension that determines the level -- lowest score, or tie-breaker>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically --
do not estimate. Standalone block; do not embed inside STORY.

---

ZERO-SIGNAL SYNTHESIS RULE

When the `found` section of STATUS contains zero signals across all namespaces,
two execution clauses apply unconditionally:

  1. Empty `found` is not grounds for omitting, hollowing, or shortening the STORY
     block. The LLM failure mode to avoid: "no signals found -- synthesis not
     possible." A STORY block that reports absence without characterizing what
     absence implies is a non-finding and fails this rule.

  2. Question 1 of the STORY narrative must characterize what uniform absence
     implies about the topic's investigation state. "The absence of any scout
     signal indicates the market surface has not been probed at all" is valid
     synthesis. "Insufficient data to synthesize" is not.

TOKEN-PRESSURE GUARD: This rule does not suspend when `found` is non-empty. It
fires unconditionally at any token budget. The rule is stated here regardless of
current `found` coverage to prevent conditional-context suppression -- a failure
mode in which the model treats the rule as dormant because `found` is large. The
guard is not evidence of the rule's non-applicability; it is a structural firewall
against its suppression.

Basis: uniform absence is itself evidence. The gap pattern -- no namespace has been
probed -- defines what the team does not know and why they are not ready. That
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
- No artifact filenames -- refer by category (e.g., "the flow signals").
- Do not restate the confidence level -- it is in [CONFIDENCE].
- Address inertia risk as a pattern across blocking gaps, not per gap.
- Sparse coverage: if found contains signals from only 1-2 namespaces, synthesize
  on available signals -- do not default to a coverage disclaimer.
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
verdict status -- even READY. Declare bounded or unbounded with the action sub-label.
VERDICT COMPRESSION GUARD: the `action:` sub-label on `inertia_cost` is required
regardless of COMPRESSED format state and regardless of token pressure. VERDICT is
never abbreviated. The action sub-label is not optional format -- it is the field that
makes VERDICT self-contained and enables the team to derive their commit posture from
this block alone without re-reading STORY or item-level gap entries. If COMPRESSED
was active for blocking entries, it does not extend to VERDICT fields. A CONDITIONAL
verdict must name the condition and what satisfies it; its `inertia_cost` must include
the `action:` sub-label specifying posture for the unresolved risk period.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-05 — Axes: Full R9 sweep (C-25 preamble + token-pressure guard + C-26 VERDICT guard)

**Hypothesis:** V-03 tests C-25 preamble placement (expected 260/260: global-constraint
position prevents block-execution-mode suppression). V-01 tests C-25 token-pressure guard
(expected 260/260: named guard prevents conditional dormancy at high coverage). V-02 tests
C-26 VERDICT compression guard (expected 260/260: named guard prevents action sub-label
elision at last block). V-05 combines all three: preamble placement of the ZERO-SIGNAL
SYNTHESIS RULE + token-pressure guard clause within the rule + VERDICT compression guard
in the VERDICT execution note. This is the strongest known form for R9 and the ceiling
candidate for confirming that all three R9 hardening mechanisms are non-conflicting. If
V-05 scores 260, the preamble + pressure guard + VERDICT guard combination is confirmed
as the production-grade form and the skill advances to R10 with rubric refinement as the
primary goal rather than structural repair. If V-05 scores lower than V-03 or V-04, a
three-way interaction is present -- the most likely culprit is the preamble rule consuming
instruction budget before phase execution begins, leaving the VERDICT guard with insufficient
model attention by the time VERDICT is produced.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block -- an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. Every blocking gap must name the commit-risk --
what assumption the team is silently making if they ship today without that signal.

ZERO-SIGNAL SYNTHESIS RULE (global execution constraint -- applies to every run):

When the `found` section of STATUS contains zero signals across all namespaces,
two execution clauses apply unconditionally before any STORY synthesis begins:

  1. Empty `found` is not grounds for omitting, hollowing, or shortening the STORY
     block. The LLM failure mode to avoid: "no signals found -- synthesis not
     possible." A STORY block that reports absence without characterizing what
     absence implies is a non-finding and fails this rule.

  2. Question 1 of the STORY narrative must characterize what uniform absence
     implies about the topic's investigation state. "The absence of any scout
     signal indicates the market surface has not been probed at all" is valid
     synthesis. "Insufficient data to synthesize" is not.

TOKEN-PRESSURE GUARD: This rule does not suspend when `found` is non-empty. It
fires unconditionally at any token budget. The rule is stated here regardless of
current `found` coverage to prevent conditional-context suppression -- a failure
mode in which the model treats the rule as dormant because `found` is large. The
guard is not evidence of the rule's non-applicability; it is a structural firewall
against its suppression.

Basis: uniform absence is itself evidence. The gap pattern -- no namespace has been
probed -- defines what the team does not know and why they are not ready. That
pattern is the evidence set. STORY must synthesize from it.

This rule is structurally distinct from the sparse-coverage rule (signals present
in only 1-2 namespaces). Both boundary conditions require synthesis. Neither permits
disclaimer substitution. This rule is stated here, before phase execution begins,
so that it is processed as a global constraint rather than as a block-local note.

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

verdict_shift: NO CHANGE | IMPROVED | DEGRADED -- <one sentence if changed, or N/A>
```

Execution: Glob `simulations/{{topic}}/campaign-brief-*.md` for the most recent prior
brief. Extract its STATUS (found/missing) and VERDICT. Compare to current state.
If this is the first run, write: prior_brief: NONE -- first run. Mark all remaining
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
  <ns>/<artifact>  <date>   <- timestamp is structurally separate from blocking
                               entries; this field is NOT subject to COMPRESSED
                               abbreviation -- found dates must appear at item level
                               regardless of blocking gap count
  ...

missing: Y signals

  BLOCKING:

  [FULL FORMAT -- blocking gaps <= 4:]
    - <ns>/<skill>/<item>
      Inertia risk: <what the team is silently assuming if they commit today>
    ...

  [COMPRESSED FORMAT -- blocking gaps > 4 (full fields in [BLOCKING-DETAIL] below):]
    - <ns>/<skill>/<item> -- <inertia risk, <=12 words>
    ...

  OPTIONAL:
    - <ns>/<skill>/<item>
      Trade-off: <what is accepted by skipping>
    ...

coverage: X/(X+Y) = Z%
```

Execution: Glob `simulations/**/{{topic}}-*`. Match against strategy. For every
blocking gap, `Inertia risk:` is required. A gap with no articulable inertia risk is
optional. State explicitly when empty: `BLOCKING: none -- all gaps are optional`.
TIMESTAMP ISOLATION: per-signal dates in the `found` section are structurally
separate from blocking entries. COMPRESSED format applies only to blocking entry
verbosity -- `found` timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count. This is the second structural location for the
timestamp isolation rule; the first is the inline annotation on the date field above.

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
binding: <the dimension that determines the level -- lowest score, or tie-breaker>
```

Execution: Score dimensions from STATUS data only. Derive average arithmetically --
do not estimate. Standalone block; do not embed inside STORY.

---

```
[STORY]
<2-4 paragraphs. Prose only.

Rules for this block:
- No tables, no bullet lists.
- No artifact filenames -- refer by category (e.g., "the flow signals").
- Do not restate the confidence level -- it is in [CONFIDENCE].
- Address inertia risk as a pattern across blocking gaps, not per gap.
- Sparse coverage: if found contains signals from only 1-2 namespaces, synthesize
  on available signals -- do not default to a coverage disclaimer.
- Zero coverage: governed by ZERO-SIGNAL SYNTHESIS RULE (stated in preamble above).

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
verdict status -- even READY. Declare bounded or unbounded with the action sub-label.
VERDICT COMPRESSION GUARD: the `action:` sub-label on `inertia_cost` is required
regardless of COMPRESSED format state and regardless of token pressure. VERDICT is
never abbreviated. The action sub-label is not optional format -- it is the field that
makes VERDICT self-contained and enables the team to derive their commit posture from
this block alone without re-reading STORY or item-level gap entries. If COMPRESSED
was active for blocking entries, it does not extend to VERDICT fields. A CONDITIONAL
verdict must name the condition and what satisfies it; its `inertia_cost` must include
the `action:` sub-label specifying posture for the unresolved risk period.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

**Key differentiators to watch in scoring:**

- **V-01** is the cleanest C-25 token-pressure test. If C-25 PASS with the guard clause
  and R8 V-05 was C-25 PASS at mid-document position, the guard clause is confirmed as
  providing additional protection against conditional-context suppression. If C-25 FAIL
  despite the guard, the issue is positional -- the mid-document location is being
  overridden before the rule text is processed, and V-03's preamble form becomes the
  primary mechanism.

- **V-02** is the cleanest C-26 VERDICT compression test. If C-26 PASS with the VERDICT
  guard and R8 V-05 was C-26 FAIL, the VERDICT execution note naming the COMPRESSED
  failure mode explicitly is confirmed as the mechanism that prevents action sub-label
  elision. If C-26 FAIL despite the guard, the issue is budget-based (not instruction-
  based) -- the investigation shifts to VERDICT block elevation as a structural remedy.

- **V-03** is the cleanest C-25 preamble-position test. If C-25 PASS with preamble form
  and FAIL with mid-document form (under identical token pressure), preamble position is
  confirmed as the compression-survival mechanism for the zero-signal synthesis mandate.
  If preamble position produces no improvement over mid-document, the rule wording is the
  variable, not the position -- the content-based guard (V-01 axis) is the primary lever.

- **V-04** tests C-25 pressure guard + C-26 VERDICT guard additivity. If V-04 scores 260
  (= V-01 lift + V-02 lift), the two guards are structurally independent. If V-04 scores
  lower, the guard clause interaction is the R10 investigation target.

- **V-05** is the 260-ceiling confirmation under full R9 hardening. If V-05 scores 260,
  preamble + pressure guard + VERDICT guard combination is confirmed non-conflicting and
  the production-grade form for the skill is established. If V-05 scores lower than V-03
  or V-04, the preamble's instruction budget effect on VERDICT attention is the primary
  R10 investigation -- most likely addressed by reducing the preamble rule length or
  by moving the VERDICT guard to a pre-VERDICT standalone note (mirroring V-03's preamble
  strategy, applied to the VERDICT block specifically).
