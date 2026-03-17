---
skill: quest-variate
skill_target: campaign-brief
round: 11
date: 2026-03-17
rubric: simulations/quest/rubrics/campaign-brief-rubric-v10-2026-03-17.md
---

# Variations -- campaign-brief / Round 11

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

**R10 recap:** V-04 and V-05 both scored 290/290 under v9 rubric (ceiling). Both
implement: (1) ZERO-SIGNAL SYNTHESIS RULE in preamble with TOKEN-PRESSURE GUARD
(C-29 PASS); (2) VERDICT COMPRESSION GUARD in VERDICT execution note (C-26/C-28
PASS); (3) C-24 dual-location timestamp isolation (inline annotation + STATUS
execution note). R10 validated C-29 dual-mechanism independence: neither preamble
placement alone (V-01) nor declarative guard alone (V-02) achieves C-29 PASS.
V-03 confirmed C-29 is rule-domain specific: applying dual-mechanism to the
VERDICT `action:` rule does not substitute for the C-25 chain requirement.

**R11 rubric:** v10, 30 criteria, 300 pts max. New criterion C-30 introduced.

**C-30 definition recap:** Dual-mechanism independence generalized to the timestamp
isolation rule (C-24 domain). Two mechanisms required, guarding against orthogonal
failure modes: (1) preamble position -- rule encountered before token pressure
builds, countering location elision; (2) declarative clause naming COMPRESSED-collapse
as the failure mode, countering positional processing without rule absorption. C-24's
dual-location restatement (inline + execution note) provides structural redundancy
within the same failure-mode class. C-30 requires each mechanism guard against a
*different* failure mode so each compensates when the other's protection is unavailable.

**R11 investigation candidates:**

1. **C-30 necessity test (V-01 as control):** Whether C-30 is independently necessary
   or already covered by C-24's dual-location. V-01 holds R10's best form (C-29 PASS,
   C-24 PASS) while leaving C-30 at PARTIAL -- no preamble placement + no declarative
   COMPRESSED-COLLAPSE GUARD on the timestamp isolation rule. If V-01 scores 290/300
   (not 300), C-30 is independently necessary. If V-01 scores 300, C-24's dual-location
   already provides C-30-equivalent protection and the criterion should be re-examined.

2. **C-30 preamble-only test (V-02):** Whether positional mechanism alone (timestamp
   isolation rule in preamble) achieves C-30 PASS, mirroring R10's V-01 result for C-29.
   Expected: C-30 PARTIAL -- if preamble is processed without rule absorption, no guard
   clause compensates.

3. **C-30 declarative-only test (V-03):** Whether declarative COMPRESSED-COLLAPSE GUARD
   alone (mid-doc, no preamble placement) achieves C-30 PASS, mirroring R10's V-02
   result for C-29. Expected: C-30 PARTIAL -- if the guard clause itself is elided under
   token pressure, no positional fallback exists.

**R11 targets:** (a) Falsify or confirm C-30 independence from C-24 via V-01 control.
(b) Confirm that C-30's dual-mechanism requirement mirrors C-29's (V-02 + V-03 both
PARTIAL individually). (c) Establish 300/300 ceiling via V-04 (clean C-30 dual-mech)
and V-05 (both rules in shared compression-immune preamble block).

---

## Variation axes selected

- **Single-axis:** C-30 absent / C-24 only (V-01), C-30 preamble-only (V-02),
  C-30 declarative-only (V-03)
- **Combined:** C-30 full dual-mechanism (V-04), Full R11 sweep -- both rules in
  shared compression-immune preamble block (V-05)

---

## V-01 -- Axis: C-30 absent (control) -- C-29 PASS, C-30 PARTIAL

**Hypothesis:** This variation reproduces R10's best form exactly (R9 V-05, R10
V-04/V-05 equivalent). C-29 PASS is guaranteed: ZERO-SIGNAL SYNTHESIS RULE in
preamble with TOKEN-PRESSURE GUARD. C-24 PASS is guaranteed: inline annotation
on the `found` date field + TIMESTAMP ISOLATION execution note in STATUS. C-30
is not addressed: no preamble placement of the timestamp isolation rule, no
declarative COMPRESSED-COLLAPSE GUARD naming the failure mode. The hypothesis
is that C-24's dual-location (inline + execution note), while providing redundancy
within the same structural location class, does not satisfy C-30's orthogonal-
failure-mode requirement. C-30 requires the two mechanisms guard against *different*
failure modes -- C-24's two locations both guard against the same class (which
location is reached first under abbreviation). If V-01 scores 290/300 under v10,
C-30 is confirmed independently necessary. Falsification: if V-01 scores 300/300,
C-24's dual-location already covers C-30's protection contract and the criterion
should be re-examined for overlap with C-24.

Expected: 290/300 (C-30 PARTIAL -10)

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
verdict status -- even READY ("bounded: remaining risk is X and recoverable because Y
-- action: commit with monitoring"). Declare bounded or unbounded with the action
sub-label. VERDICT COMPRESSION GUARD: the `action:` sub-label on `inertia_cost` is
required regardless of COMPRESSED format state and regardless of token pressure.
VERDICT is never abbreviated. The action sub-label is not optional format -- it is
the field that makes VERDICT self-contained and enables the team to derive their
commit posture from this block alone without re-reading STORY or item-level gap
entries. If COMPRESSED was active for blocking entries, it does not extend to VERDICT
fields. A CONDITIONAL verdict must name the condition and what satisfies it; its
`inertia_cost` must include the `action:` sub-label specifying posture for the
unresolved risk period.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-02 -- Axis: C-30 preamble-only (timestamp isolation rule in preamble, no COMPRESSED-COLLAPSE GUARD)

**Hypothesis:** V-01 (control) holds C-30 at PARTIAL by providing only C-24's
dual-location restatement. V-02 adds the first C-30 mechanism: preamble placement
of the timestamp isolation rule (positional mechanism). The rule appears in the
preamble, before phase execution begins, so it is processed as a global structural
constraint before token pressure accumulates. The C-24 dual-location (inline
annotation + STATUS execution note) is preserved unchanged. No declarative
COMPRESSED-COLLAPSE GUARD is added -- this axis isolates the positional mechanism
alone. The hypothesis: preamble placement improves over V-01's C-24-only form but
does not achieve C-30 PASS because it does not guard against the orthogonal failure
mode (positional processing without rule absorption). If the preamble section is
processed and the rule is noted but not absorbed as a constraint, no guard clause
compensates. Mirrors R10's V-01 result for C-29 (preamble position alone insufficient
for dual-mechanism independence). Expected: 290/300 (C-30 PARTIAL -10). Falsification:
if V-02 scores 300/300, preamble placement alone satisfies C-30 -- the declarative
mechanism is not independently necessary and the criterion requires reexamination.

Expected: 290/300 (C-30 PARTIAL -10)

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

TIMESTAMP ISOLATION RULE (global execution constraint -- applies to every run):

Per-signal dates in the `found` section of STATUS are structurally separate from
blocking gap entries. Each signal in `found` must carry its own date at item level.
COMPRESSED format applies only to blocking entry verbosity -- it does not affect
found timestamps. Found timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count or token budget. This rule is stated here, before
phase execution begins, so that it is processed as a global structural constraint
rather than as a block-local annotation that may be elided when compression activates.

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
The preamble statement is the third location.

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

## V-03 -- Axis: C-30 declarative-only (COMPRESSED-COLLAPSE GUARD in STATUS execution note, no preamble placement)

**Hypothesis:** V-02 tests preamble-only placement of the timestamp isolation rule
(expected: C-30 PARTIAL -- positional alone insufficient). V-03 tests the declarative
mechanism alone: a COMPRESSED-COLLAPSE GUARD clause added to the STATUS execution
note, naming COMPRESSED-collapse as the specific failure mode the guard prevents. No
preamble placement of the timestamp isolation rule is added -- C-24's dual-location
(inline annotation + STATUS execution note) is preserved, and the COMPRESSED-COLLAPSE
GUARD is appended as a named extension of location 2. The ZERO-SIGNAL SYNTHESIS RULE
preamble form (C-29 PASS) is unchanged. The hypothesis: the declarative guard
improves over V-01's baseline but does not achieve C-30 PASS because it does not
guard against the orthogonal failure mode (location elision under token pressure).
The COMPRESSED-COLLAPSE GUARD appears mid-document in the STATUS execution note.
Under high token pressure with many blocking gaps, the STATUS block itself is
processed under COMPRESSED mode, and the execution note (appearing after the COMPRESSED
format rule definition) may be abbreviated or skipped before the guard clause is read.
No positional fallback exists. Mirrors R10's V-02 result for C-29 (declarative guard
alone insufficient). Expected: 290/300 (C-30 PARTIAL -10). Falsification: if V-03
scores 300/300, the declarative mechanism alone satisfies C-30 -- preamble placement
is not independently necessary.

Expected: 290/300 (C-30 PARTIAL -10)

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
COMPRESSED-COLLAPSE GUARD: This isolation rule fires unconditionally regardless of
COMPRESSED format state. The failure mode this guard prevents: COMPRESSED-collapse --
the model treats the `found` section as part of the general abbreviation pass triggered
by blocking gap count > 4, collapsing found timestamps into summary form or omitting
them alongside compressed blocking entries. The `found` timestamps are a structurally
separate domain from blocking entries; COMPRESSED scope does not extend to them. This
declarative guard is independent of format-branch inference -- it names the failure mode
explicitly so the model cannot resolve the ambiguity by treating found as abbreviatable.

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

## V-04 -- Axes: C-30 full dual-mechanism (preamble + COMPRESSED-COLLAPSE GUARD; C-29 unchanged)

**Hypothesis:** V-02 (preamble-only) and V-03 (declarative-only) are each expected to
score 290/300 (C-30 PARTIAL), confirming that neither mechanism alone is sufficient --
mirroring R10's V-01/V-02 result for C-29. V-04 combines both C-30 mechanisms: (1)
preamble placement of the TIMESTAMP ISOLATION RULE (positional -- rule encountered
before token pressure accumulates, before COMPRESSED branch activates); (2)
COMPRESSED-COLLAPSE GUARD within the TIMESTAMP ISOLATION RULE itself (declarative --
names COMPRESSED-collapse as the failure mode the guard prevents, providing independent
protection if preamble is processed without rule absorption). C-24's dual-location
(inline annotation + STATUS execution note) is preserved. C-29's ZERO-SIGNAL SYNTHESIS
RULE with TOKEN-PRESSURE GUARD remains in the preamble unchanged. The two preamble
rules are kept structurally separate (two distinct blocks) to isolate C-30 dual-mech
from the shared-block architecture (V-05's axis). The hypothesis: both mechanisms
together achieve C-30 PASS by guarding against orthogonal failure modes -- the
COMPRESSED-COLLAPSE GUARD compensates if preamble position is processed without
rule absorption; the preamble position compensates if the guard clause itself is
elided under token pressure at the STATUS execution note stage.

Expected: 300/300 (C-30 PASS)

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

TIMESTAMP ISOLATION RULE (global execution constraint -- applies to every run):

Per-signal dates in the `found` section of STATUS are structurally separate from
blocking gap entries. Each signal in `found` must carry its own date at item level.
COMPRESSED format applies only to blocking entry verbosity -- it does not extend to
found timestamps. Found timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count or token budget.

COMPRESSED-COLLAPSE GUARD: This rule fires unconditionally regardless of COMPRESSED
format state. The failure mode this guard prevents: COMPRESSED-collapse -- the model
treats the `found` section as part of the general abbreviation pass triggered when
blocking gap count exceeds 4, collapsing found timestamps into summary form or omitting
them alongside compressed blocking entries. The `found` timestamps occupy a structurally
separate domain from blocking entries; COMPRESSED scope does not reach them. This
declarative guard provides a mechanism independent of preamble position: if the preamble
is processed without this rule being absorbed as a constraint, this named guard clause
prevents COMPRESSED-collapse at the point where the STATUS block is actually produced.
The two mechanisms -- preamble position (this rule read before token pressure builds)
and this declarative guard (COMPRESSED-collapse named as the failure mode) -- guard
against orthogonal failure modes and each compensates when the other's protection is
unavailable.

This rule is stated here, before phase execution begins, so that it is processed as
a global structural constraint rather than as a block-local annotation.

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
The preamble TIMESTAMP ISOLATION RULE is the third location.

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

## V-05 -- Axes: Full R11 sweep (C-29 + C-30 both rules in shared compression-immune preamble block)

**Hypothesis:** V-04 confirms C-30 PASS with two structurally separate preamble
blocks. V-05 tests whether collapsing both rules into a single unified
COMPRESSION-IMMUNE PREAMBLE block creates a stronger structural contract than two
separate blocks. The generalization principle from R10's excellence signals (V-05
pattern): "applying positional + declarative dual-mechanism to all compression-critical
rules within a shared preamble block creates a compression-immune structural contract;
suppressing any single rule requires suppressing the entire preamble, not just a
mid-document section." With a single unified block, the preamble becomes an atomic
unit -- the model cannot selectively apply one rule without encountering the other.
Each rule within the block carries its own guard clause naming its specific failure
mode (conditional-context suppression for ZERO-SIGNAL; COMPRESSED-collapse for
TIMESTAMP ISOLATION). C-24's dual-location is preserved in the STATUS block with
the preamble block named as the primary location. The VERDICT COMPRESSION GUARD
is unchanged. The hypothesis: the unified preamble achieves 300/300 and may produce
stronger execution fidelity than V-04's two-block form if the unified block reduces
instruction-budget fragmentation between the two rules. Falsification: if V-05 scores
lower than V-04, the unified block introduces a preamble-length penalty that suppresses
one of the guard clauses -- the two-block form (V-04) would be the production architecture.

Expected: 300/300 (C-29 PASS, C-30 PASS, strongest possible form)

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block -- an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. Every blocking gap must name the commit-risk --
what assumption the team is silently making if they ship today without that signal.

COMPRESSION-IMMUNE PREAMBLE (global execution constraints -- both rules fire on every run):

The two rules below govern edge-case behavior that is suppressed by compression failure
modes. Each rule is independently guarded. Suppressing any rule in this block requires
suppressing the entire preamble. Read and apply both before beginning phase execution.

RULE 1 -- ZERO-SIGNAL SYNTHESIS:

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
pattern is the evidence set. STORY must synthesize from it. This rule is structurally
distinct from the sparse-coverage rule (signals present in only 1-2 namespaces). Both
boundary conditions require synthesis. Neither permits disclaimer substitution.

RULE 2 -- TIMESTAMP ISOLATION:

Per-signal dates in the `found` section of STATUS are structurally separate from
blocking gap entries. Each signal in `found` must carry its own date at item level.
COMPRESSED format applies only to blocking entry verbosity -- it does not extend to
found timestamps. Found timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count or token budget.

COMPRESSED-COLLAPSE GUARD: This rule fires unconditionally regardless of COMPRESSED
format state. The failure mode this guard prevents: COMPRESSED-collapse -- the model
treats the `found` section as part of the general abbreviation pass triggered when
blocking gap count exceeds 4, collapsing found timestamps into summary form or omitting
them alongside compressed blocking entries. The `found` timestamps occupy a structurally
separate domain from blocking entries; COMPRESSED scope does not reach them. This
declarative guard provides independent protection against COMPRESSED-collapse: if the
preamble position of this rule is processed without rule absorption, this named guard
clause prevents the failure mode at the point where the STATUS block is produced. The
preamble position guards against location elision; this guard clause guards against
processing-without-absorption -- orthogonal failure modes, each compensating when the
other's protection is unavailable.

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
                               regardless of blocking gap count; see COMPRESSION-IMMUNE
                               PREAMBLE Rule 2 for the primary isolation constraint
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
timestamp isolation rule; the primary location is in the COMPRESSION-IMMUNE PREAMBLE
above (Rule 2 -- TIMESTAMP ISOLATION).

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
- Zero coverage: governed by COMPRESSION-IMMUNE PREAMBLE Rule 1 (ZERO-SIGNAL
  SYNTHESIS) stated above.

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

- **V-01** is the C-30 necessity control. Score 290 confirms C-30 is independently
  necessary beyond C-24. Score 300 falsifies the criterion -- C-24's dual-location
  already covers the orthogonal-failure-mode requirement.

- **V-02** is the C-30 preamble-only test. Expected 290 (PARTIAL): preamble position
  alone fails if preamble is processed without rule absorption. Score 300 would falsify
  C-30's independence requirement by showing positional mechanism is sufficient alone.

- **V-03** is the C-30 declarative-only test. Expected 290 (PARTIAL): guard clause
  alone fails if it is itself elided under token pressure before STATUS processing.
  Score 300 would falsify C-30's independence requirement by showing declarative
  mechanism is sufficient alone.

- **V-04** is the clean C-30 dual-mechanism test. If V-04 scores 300, both mechanisms
  are confirmed necessary and sufficient together (independent failure-mode coverage
  validated). If V-04 scores less than 300 despite both mechanisms present, the failure
  is structural -- most likely the COMPRESSED-COLLAPSE GUARD text in the preamble TIMESTAMP
  ISOLATION RULE is not being read as a declarative clause with named failure-mode framing
  (which would require rewording to more closely match TOKEN-PRESSURE GUARD's pattern).

- **V-05** is the ceiling candidate for the unified preamble architecture. If V-05
  scores 300 and matches or exceeds V-04's execution fidelity in practice, the
  COMPRESSION-IMMUNE PREAMBLE pattern is confirmed as the production-grade architecture.
  If V-05 scores lower than V-04, the preamble length creates an instruction-budget
  penalty -- the two-block form (V-04) is the production architecture.
