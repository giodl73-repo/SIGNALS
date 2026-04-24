---
skill: quest-variate
skill_target: campaign-brief
round: 10
date: 2026-03-17
rubric: simulations/quest/rubrics/campaign-brief-rubric-v9-2026-03-16.md
---

# Variations -- campaign-brief / Round 10

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

**R9 recap:** V-04 and V-05 both scored 260/260 under v8. V-04 used mid-document
TOKEN-PRESSURE GUARD + VERDICT COMPRESSION GUARD. V-05 added preamble placement for
the ZERO-SIGNAL SYNTHESIS RULE (before "Run the phases in order") alongside both
guards. The R9 rubric could not distinguish them -- both reached ceiling. The single-
axis variations (V-01/V-02/V-03) each scored 255: every single-guard form left one
axis unguarded.

**R9 rubric change to v9:** Three new criteria promoted from R9 excellence signals:

| Criterion | What it tests |
|---|---|
| C-27 | TOKEN-PRESSURE GUARD on zero-signal rule: names conditional-dormancy failure mode, declares unconditional firing |
| C-28 | VERDICT COMPRESSION GUARD: action: sub-labels declared mandatory invariant against COMPRESSED x last-block |
| C-29 | Dual-mechanism independence: positional (preamble) + declarative (named guard) applied together to same compression-critical rule |

Max score advances from 260 to 290. C-01 through C-26 carry forward unchanged.

**R10 investigation candidate (from rubric v9):**

R9 could not falsify whether V-04 (mid-doc + both guards, 260) or V-05 (preamble +
both guards, 260) had different compression survival characteristics -- both hit
ceiling and both get C-25, C-26 PASS under v8. Under v9, C-29 requires BOTH
positional + declarative mechanisms on the SAME compression-critical rule.

R10 primary test: Is preamble position alone sufficient to satisfy C-29 (and produce
a C-27-like guard effect by virtue of position), or is the declarative TOKEN-PRESSURE
GUARD alone sufficient, or are both required? If preamble-only (V-01) and
declarative-only (V-02) each score below 290, C-29's independence requirement is
validated. If either alone reaches 290, C-29 should be narrowed.

R10 secondary test: Does applying C-29's dual-mechanism principle to the VERDICT
action: rule (V-03 axis) independently produce C-29 credit -- i.e., can a skill
satisfy C-29 via the VERDICT rule instead of the zero-signal rule?

---

## Variation axes selected

- **V-01 (single-axis):** C-29 positional-only -- preamble placement of ZERO-SIGNAL
  SYNTHESIS RULE with no TOKEN-PRESSURE GUARD clause. Tests whether position alone
  satisfies C-27 and C-29.

- **V-02 (single-axis):** C-29 declarative-only -- TOKEN-PRESSURE GUARD at mid-doc
  position, no preamble. Tests whether guard clause alone satisfies C-27 and C-29.

- **V-03 (single-axis):** C-29 generalized to VERDICT action: rule -- preamble
  declaration of VERDICT COMPLETION GUARANTEE + VERDICT COMPRESSION GUARD. Tests
  whether C-29 credit is earnable via the VERDICT compression-critical rule rather
  than only via the zero-signal rule.

- **V-04 (combined):** Full dual-mechanism on zero-signal rule only (= R9 V-05 form
  under v9 rubric). Preamble placement + TOKEN-PRESSURE GUARD for zero-signal rule;
  VERDICT COMPRESSION GUARD for VERDICT. Establishes v9 ceiling baseline.

- **V-05 (combined):** Maximum ceiling -- dual-mechanism applied to both compression-
  critical rules (zero-signal rule + VERDICT action: rule). Generalizes C-29 across
  the full skill architecture.

---

## V-01 -- Axis: C-29 positional-only (preamble placement, no TOKEN-PRESSURE GUARD)

**Hypothesis:** R9 V-03 showed preamble placement of the ZERO-SIGNAL SYNTHESIS RULE
scores 255/260 under v8 (C-25 PASS, C-26 PASS, C-24 PASS -- no v8-era deficit). Under
v9, preamble position alone must satisfy C-29's PASS definition, which requires BOTH
positional AND declarative mechanisms. The hypothesis to falsify: preamble position is
independently sufficient for C-29 because (a) global-constraint position forces the
model to hold the rule as active regardless of token pressure, and (b) the position
effect subsumes the declarative guard effect when the model reads the rule before any
block-execution context forms. If V-01 scores C-29 PARTIAL (positional mechanism only,
no declarative guard), the independence requirement is validated and V-04/V-05's
dual-mechanism forms are genuinely structurally necessary. If V-01 scores C-29 PASS
(preamble alone is sufficient), the criterion should be narrowed to require only
positional placement.

Secondary: C-27 requires a TOKEN-PRESSURE GUARD naming the conditional-dormancy
failure mode. V-01 has no such clause. Expected C-27 PARTIAL -- the positional
mechanism does not name the failure mode, it only prevents the position-dependent
form of suppression.

Expected: C-27 PARTIAL (5), C-28 PASS (10), C-29 PARTIAL (5) -- net 270/290.
Falsification threshold: if V-01 scores 280+ on C-27 or C-29, the declarative guard
is not independently required and V-02's axis becomes the primary investigation.

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
so that it is processed as a global execution constraint rather than as a block-local
note.

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

## V-02 -- Axis: C-29 declarative-only (mid-doc TOKEN-PRESSURE GUARD, no preamble)

**Hypothesis:** R9 V-01 showed TOKEN-PRESSURE GUARD at mid-document position scores
255/260 under v8 (C-25 PASS, no preamble). Under v9, the declarative mechanism alone
must satisfy C-29's PASS definition, which requires BOTH positional + declarative. The
hypothesis to falsify: a named guard clause that explicitly identifies the conditional-
dormancy failure mode and declares unconditional firing is independently sufficient for
C-29 because the model interprets "fires unconditionally at any token budget" as a
preamble-equivalent global directive regardless of document position. If the model
treats an unconditional-firing declaration as position-agnostic, C-29 PASS follows
without preamble placement.

Secondary: C-27 PASS requires the TOKEN-PRESSURE GUARD to name the conditional-dormancy
failure mode -- V-02 has this. C-28 PASS requires the VERDICT COMPRESSION GUARD -- V-02
has this. The only open question is C-29: does the declarative mechanism alone trigger
PASS, or does PARTIAL (one of two required mechanisms) apply?

Expected: C-27 PASS (10), C-28 PASS (10), C-29 PARTIAL (5) -- net 280/290.
Falsification threshold: if V-02 scores C-29 PASS (290/290), preamble position is not
independently necessary for C-29 and the criterion's positional requirement should be
re-examined. If V-02 scores C-29 PARTIAL (280/290), the declarative guard alone is not
sufficient -- V-04/V-05's combined form is required for the ceiling.

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

## V-03 -- Axis: C-29 generalized to VERDICT action: rule (dual-mechanism on VERDICT, not zero-signal rule)

**Hypothesis:** C-29 applies to any compression-critical boundary-condition rule, not
exclusively the zero-signal synthesis rule. The VERDICT action: sub-label is compression-
critical (must survive COMPRESSED x last-block) and fires on a boundary condition (the
COMPRESSED x last-block scenario is not triggered on every run). V-03 applies C-29's
dual-mechanism principle to the VERDICT action: rule specifically: (1) positional -- state
the VERDICT COMPLETION GUARANTEE at preamble level (before "Run the phases in order") so
the model processes it as a global execution constraint; (2) declarative -- VERDICT
COMPRESSION GUARD in the VERDICT execution note names the COMPRESSED x last-block failure
mode and declares action: as a mandatory invariant.

The zero-signal rule uses R9 V-04 form (mid-doc + TOKEN-PRESSURE GUARD) to satisfy C-25
and C-27, but is NOT elevated to preamble. This isolates the C-29 test to the VERDICT
rule: does dual-mechanism on VERDICT's action: rule produce C-29 PASS independently of
whether the same mechanism is applied to the zero-signal rule?

If V-03 scores C-29 PASS (290/290), C-29's criterion is earnable by either compression-
critical rule, not exclusively the zero-signal rule. If V-03 scores C-29 PARTIAL (280/290),
C-29 requires dual-mechanism specifically on the zero-signal rule (preamble + TOKEN-PRESSURE
GUARD is the only qualifying pairing), not on the VERDICT rule.

Expected: C-27 PASS (10), C-28 PASS (10), C-29 PASS or PARTIAL -- net 280-290/290.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block -- an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. Every blocking gap must name the commit-risk --
what assumption the team is silently making if they ship today without that signal.

VERDICT COMPLETION GUARANTEE (global execution constraint -- applies to every run):

The `action:` sub-label on `inertia_cost` in the VERDICT block is a mandatory output
field at every verdict status. It is not optional format -- it is the field that makes
VERDICT self-contained and enables the team to derive their commit posture from VERDICT
alone without re-reading STORY or item-level gap entries. This rule is stated here,
before phase execution begins, so that it is processed as a global execution constraint
rather than as a VERDICT-block-local note. It fires regardless of token pressure,
COMPRESSED format state, or whether VERDICT is the last block processed. The failure
mode this guards against: under COMPRESSED format + last-block token depletion, the
model preserves the bounded/unbounded classification but elides the `action:` sub-label
as optional format -- valid for C-23 but not for C-26. That elision is prohibited by
this rule.

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
this block alone without re-reading STORY or item-level gap entries. This guard and the
VERDICT COMPLETION GUARANTEE stated in the preamble are two structurally independent
mechanisms protecting the same mandatory field: the preamble declaration ensures the
rule is processed before block-execution context forms; this guard ensures elision
requires violating a named invariant even when VERDICT is reached last under depleted
token budget. If COMPRESSED was active for blocking entries, it does not extend to
VERDICT fields. A CONDITIONAL verdict must name the condition and what satisfies it;
its `inertia_cost` must include the `action:` sub-label specifying posture for the
unresolved risk period.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-04 -- Combined: Preamble + TOKEN-PRESSURE GUARD on zero-signal rule (R9 V-05 structural form under v9 rubric)

**Hypothesis:** R9 V-05 (preamble + TOKEN-PRESSURE GUARD + VERDICT COMPRESSION GUARD)
was the R9 ceiling form at 260/260 under v8. Under v9, this form must satisfy C-27
(TOKEN-PRESSURE GUARD names conditional-dormancy failure mode), C-28 (VERDICT
COMPRESSION GUARD names COMPRESSED x last-block failure mode), and C-29 (positional +
declarative dual-mechanism on the zero-signal rule). R9 V-05 contains all three:
(1) preamble position for the ZERO-SIGNAL SYNTHESIS RULE (positional mechanism for C-29);
(2) TOKEN-PRESSURE GUARD clause within the preamble rule (declarative mechanism for C-29,
and the named guard for C-27); (3) VERDICT COMPRESSION GUARD in the VERDICT execution
note (C-28). V-04 is structurally identical to R9 V-05 -- its function is to confirm
that the prior ceiling form now scores 290/290 under the expanded rubric, establishing
the v9 ceiling baseline and validating that no criteria were inadvertently broken between
rubric versions.

Expected: C-27 PASS (10), C-28 PASS (10), C-29 PASS (10) -- net 290/290.
If V-04 scores below 290, a v8-to-v9 transition gap exists and R9 V-05 does not
automatically satisfy the new criteria -- the deficit criterion is the R10 structural
investigation priority.

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
so that it is processed as a global execution constraint rather than as a block-local
note.

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

## V-05 -- Combined: Maximum ceiling -- dual-mechanism applied to both compression-critical rules

**Hypothesis:** V-04 applies C-29's dual-mechanism principle to the zero-signal synthesis
rule (preamble position + TOKEN-PRESSURE GUARD). V-03 applies it to the VERDICT action:
rule (preamble declaration + VERDICT COMPRESSION GUARD). V-05 applies it to both
simultaneously. The two compression-critical boundary-condition rules in this skill are:
(1) the zero-signal synthesis mandate -- fires when `found` is empty, at risk of
conditional-dormancy suppression under high `found` token pressure; and (2) the VERDICT
action: sub-label -- fires at every run but at risk of elision under COMPRESSED x last-
block token depletion. V-05 gives each rule its own named preamble declaration and its
own named block-level guard, so each rule has structurally independent survival architecture.

The two preamble declarations are sequenced: ZERO-SIGNAL SYNTHESIS RULE first (because
its failure mode is triggered by `found` content, which is processed before VERDICT),
then VERDICT COMPLETION GUARANTEE (because its failure mode is triggered by COMPRESSED +
last-block, which is a later-stage condition). The ordering makes the architectural
reasoning visible: rules are positioned relative to their failure mode contexts.

If V-05 matches V-04 at 290/290, the VERDICT dual-mechanism adds no rubric credit beyond
what V-04 already achieves -- C-29 is satisfied by the zero-signal rule alone and the
VERDICT-rule application is belt-and-suspenders beyond the rubric threshold. If V-05
scores higher (impossible under 29-criterion ceiling) or the scoring reveals a new
excellence signal, it indicates the C-29 architecture has room for another rubric
refinement in R11.

Expected: C-27 PASS (10), C-28 PASS (10), C-29 PASS (10) -- net 290/290.
Excellence signal target: whether naming both compression-critical rules at preamble
level with explicit failure-mode framing is a generalizable skill-architecture pattern
that should be codified as a new criterion.

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
so that it is processed as a global execution constraint rather than as a block-local
note.

VERDICT COMPLETION GUARANTEE (global execution constraint -- applies to every run):

The `action:` sub-label on `inertia_cost` in the VERDICT block is a mandatory output
field at every verdict status -- READY, NOT READY, and CONDITIONAL alike. It is not
optional format -- it is the field that makes VERDICT self-contained. This rule is
stated here, before phase execution begins, so that it is processed as a global
execution constraint rather than as a VERDICT-block-local note. The failure mode this
guards against: under COMPRESSED format combined with last-block token depletion, the
model preserves the bounded/unbounded classification but elides the `action:` sub-label
as optional format extension. That elision is prohibited. The `action:` sub-label is a
mandatory invariant field; its absence makes VERDICT not self-contained and forces the
team to re-read STORY and gap entries to derive commit posture.

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
this block alone without re-reading STORY or item-level gap entries. This guard and the
VERDICT COMPLETION GUARANTEE stated in the preamble are two structurally independent
mechanisms protecting the same mandatory field: the preamble guarantee ensures the
invariant is registered before block-execution mode begins; this guard ensures elision
requires violating a named invariant at the block level when VERDICT is produced under
depleted budget. If COMPRESSED was active for blocking entries, it does not extend to
VERDICT fields. A CONDITIONAL verdict must name the condition and what satisfies it;
its `inertia_cost` must include the `action:` sub-label specifying posture for the
unresolved risk period.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.
