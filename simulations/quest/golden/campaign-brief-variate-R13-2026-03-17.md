---
skill: quest-variate
skill_target: campaign-brief
round: 13
date: 2026-03-17
rubric: simulations/quest/rubrics/campaign-brief-rubric-v12-2026-03-17.md
---

# Variations -- campaign-brief / Round 13

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

**R12 recap:** V-05 scored 310/310 (ceiling under v11). C-31 PASS achieved by
COMPRESSION-IMMUNE PREAMBLE designation + execution-note back-invocation by designation
name. The bidirectional circuit: preamble declares structural immunity; execution notes
invoke preamble by exact designation name ("COMPRESSION-IMMUNE PREAMBLE invocation").
V-01-V-04 scored 300/310 (C-31 PARTIAL). The three PARTIAL bands were resolved:
adjacency-only (V-01), descriptive label (V-02), one-directional contract (V-03).
R12 V-05 also exhibited an excellence signal: per-rule guards in the preamble contain
forward-references to their companion execution-note mechanisms -- but those references
name "the STORY execution note" and "the STATUS execution note" generically, without
using the companion mechanism's full clause designation or its location.

**R13 rubric:** v12, 32 criteria, 320 pts max. New criterion C-32 introduced.

**C-32 definition recap:** When C-31 PASS, the COMPRESSION-IMMUNE PREAMBLE section
contains forward-references naming each companion execution-note mechanism by its full
clause designation AND location, and each execution note names the preamble by its
structural designation (C-31 PASS already guarantees the execution-note side). This
creates a reference architecture navigable from either compression-survival entry point:
if execution notes are elided but preamble preserved, the model can navigate to companion
mechanisms by their exact clause designation and block location. C-32 PARTIAL = preamble
forward-references exist but use positional/generic language rather than full clause
designation and location. C-32 PASS = preamble forward-references name each companion
mechanism by its exact clause designation AND which block it lives in.

**R13 investigation candidates:**

1. **C-32 absent (V-01 control):** R12 V-05 reproduced exactly. Preamble guards
   forward-reference companions generically ("The STORY execution note", "The STATUS
   execution note") without naming their clause designations. Confirms 310/320 baseline
   (C-32 PARTIAL -10). Falsification: if V-01 scores 320/320, generic location reference
   in the preamble already satisfies C-32 and the criterion must be re-examined.

2. **Location-only forward-reference, no clause designation (V-02):** Preamble guards
   name the block location ("the declarative execution note in the STORY block", "the
   declarative execution note in the STATUS block") but not the clause designation.
   Tests whether location without clause name satisfies C-32. Expected 310/320 (C-32
   PARTIAL -- location present, designation absent).

3. **Clause designation without location (V-03):** Preamble guards name the clause
   designation exactly ("The ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE
   invocation) clause", "The TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation)
   clause") but omit the block location. Tests whether designation alone, without
   specifying which block the companion lives in, satisfies C-32. Expected 310/320
   (C-32 PARTIAL -- designation present, location absent).

4. **Asymmetric C-32 (V-04):** C-29 domain achieves full C-32 reference (designation +
   location: "...execution note in the STORY block"); C-30 domain achieves designation
   only (no location: "...clause"). Tests whether C-32 requires both axes on all rules
   or whether one rule achieving full designation+location satisfies the criterion.
   Expected 310/320 (C-32 PARTIAL -- circuit incomplete on C-30 domain side).

5. **Full C-32 PASS (V-05):** Both preamble guards forward-reference companion mechanisms
   by exact clause designation AND block location. TOKEN-PRESSURE GUARD names "The
   ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note
   in the STORY block"; COMPRESSED-COLLAPSE GUARD names "The TIMESTAMP ISOLATION
   (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STATUS block."
   Establishes the 320-pt ceiling. Falsification: if V-05 = V-01 = 310/320, the closed
   reference loop adds no measurable protection over generic location reference.

**R13 targets:** (a) Confirm V-01 = 310/320 (C-32 absent baseline). (b) Confirm V-02 =
310/320 (location without designation insufficient). (c) Confirm V-03 = 310/320
(designation without location insufficient). (d) Confirm V-04 = 310/320 (asymmetric
partial loop insufficient). (e) Establish V-05 = 320/320 ceiling.

---

## Variation axes selected

- **Single-axis:** C-32 absent / R12 V-05 form (V-01), location-only forward-reference
  (V-02), clause-designation-only forward-reference (V-03)
- **Combined:** Asymmetric C-32 (C-29 full, C-30 partial) + inertia framing
  foregrounded (V-04), full C-32 PASS -- designation + location in both preamble guards
  (V-05)

---

## V-01 -- Axis: C-32 absent (control) -- C-31 PASS, C-32 PARTIAL

**Hypothesis:** This variation reproduces R12's V-05 form exactly. C-31 PASS is
guaranteed: COMPRESSION-IMMUNE PREAMBLE designation present with "This section is a
structural contract" declaration; STATUS execution note invokes "COMPRESSION-IMMUNE
PREAMBLE" by exact designation for C-30; STORY execution note invokes "COMPRESSION-IMMUNE
PREAMBLE" by exact designation for C-29. The bidirectional circuit from C-31 is complete.
C-32 is not addressed: the preamble's TOKEN-PRESSURE GUARD and COMPRESSED-COLLAPSE GUARD
forward-reference their companion execution-note mechanisms generically -- "The STORY
execution note provides the declarative mechanism" and "The STATUS execution note provides
the declarative mechanism" -- without naming the companion mechanisms' clause designations
or explicitly stating which block they inhabit beyond the generic block name. The
hypothesis: C-32 requires both the clause designation and the block location to be present
in the preamble's forward-references. Generic block-name reference ("the STORY execution
note") does not constitute full clause designation. If V-01 scores 310/320, C-32 is
independently necessary. Falsification: if V-01 scores 320/320, generic block reference
already satisfies C-32 and the criterion is subsumed by C-31.

Expected: 310/320 (C-32 PARTIAL -10)

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block -- an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. The status quo is the default outcome when the team
commits without sufficient evidence. Every blocking gap names the silent assumption the
team makes if they ship today without that signal. Every VERDICT classifies whether
residual inertia risk is recoverable post-commit or propagates to irreversible state.

=== COMPRESSION-IMMUNE PREAMBLE ===

This section is a structural contract. The rules below apply regardless of token
budget, output length, blocking gap count, or coverage state. This section is
processed before any phase block is generated. The structural designation
COMPRESSION-IMMUNE means: this section and the rules it contains must not be treated
as deferred context that can be deprioritized as token pressure increases. When
execution notes in subsequent blocks reference this section by its designation, those
notes are pointers to this contract -- they do not restate the rule, they invoke it.

ZERO-SIGNAL SYNTHESIS RULE (C-29 domain):

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

TOKEN-PRESSURE GUARD: This rule does not suspend when `found` is non-empty. It fires
unconditionally at any token budget. The structural designation of this preamble as
COMPRESSION-IMMUNE is the positional mechanism for this rule: the rule is encountered
and absorbed as a global constraint before any phase accumulates token pressure.
The STORY execution note provides the declarative mechanism -- it references this
preamble by designation and names the zero-signal case explicitly, so the rule is
absorbed as a conditional constraint even if preamble processing occurred without full
rule absorption.

Basis: uniform absence is itself evidence. The gap pattern defines what the team does
not know and why they are not ready. Both zero-signal and sparse-coverage boundary
conditions require synthesis; neither permits disclaimer substitution.

TIMESTAMP ISOLATION RULE (C-30 domain):

Per-signal dates in the `found` section of STATUS are structurally separate from
blocking gap entries. Each signal in `found` must carry its own date at item level.
COMPRESSED format applies only to blocking entry verbosity -- it does not affect
found timestamps. Found timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count or token budget.

COMPRESSED-COLLAPSE GUARD: The specific failure mode this rule prevents is
COMPRESSED-collapse -- simultaneous compression of `found` entries and blocking gap
entries when token pressure activates the COMPRESSED branch. Blocking entries may be
compressed; found timestamps may not. The structural designation of this preamble as
COMPRESSION-IMMUNE is the positional mechanism for this rule: the timestamp isolation
contract is established here before blocking-gap context accumulates. The STATUS
execution note provides the declarative mechanism -- it references this preamble by
designation and names the COMPRESSED-collapse failure mode explicitly, so the rule is
absorbed as a conditional constraint even if the preamble was processed without full
absorption.

=== END COMPRESSION-IMMUNE PREAMBLE ===

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
TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation): per-signal dates in
`found` are structurally separate from blocking entries. COMPRESSED format applies only
to blocking entry verbosity -- `found` timestamps must not be collapsed regardless of
blocking gap count. This note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the
TIMESTAMP ISOLATION RULE. The declarative mechanism for C-30: this note names the
COMPRESSED-collapse failure mode -- simultaneous compression of `found` and blocking
entries -- so the rule is absorbed as a conditional constraint at the point-of-use,
compensating if preamble processing occurred without full rule absorption.

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
- Zero coverage: governed by ZERO-SIGNAL SYNTHESIS RULE (COMPRESSION-IMMUNE PREAMBLE).

The narrative must answer these three questions in continuous prose:
  1. What case do the signals make together?
     (If found is empty: what does uniform absence imply about investigation state?)
  2. What do the gaps leave genuinely uncertain?
  3. What is the team's real exposure if they commit now?>
```

Execution: Synthesize STATUS and CONFIDENCE findings into a coherent narrative arc.
STORY owns cross-signal reasoning; every other block owns its own record.
ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation): this execution
note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS
RULE. The declarative mechanism for C-29: if `found` is empty, this note names the
zero-signal synthesis case explicitly -- "empty `found` is not grounds for omitting
STORY; question 1 must characterize what uniform absence implies" -- so the rule is
absorbed as a conditional constraint at the point-of-use, compensating if preamble
processing occurred without full rule absorption. Gap pattern is the evidence set.

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

## V-02 -- Axis: Location-only preamble forward-reference (no clause designation) -- C-31 PASS, C-32 PARTIAL

**Hypothesis:** V-01 establishes the C-32-absent baseline with generic block-name
forward-references in preamble guards ("The STORY execution note", "The STATUS execution
note"). V-02 advances one step: preamble guards name the companion mechanism's location
explicitly using its block and role ("the declarative execution note in the STORY block",
"the declarative execution note in the STATUS block") but do not name the companion by
its clause designation. The clause designation is the exact heading under which the
companion mechanism appears -- "ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE
PREAMBLE invocation)" and "TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation)"
-- and V-02 omits these entirely. The isolation axis: is block-level location reference
without clause-designation sufficient for C-32 PASS? The hypothesis: C-32 requires both
axes. When compression elides execution notes, a model recovering from the preamble
alone cannot navigate to the companion mechanism by block name alone -- it must know
the clause designation to identify which execution note within that block to recover.
Expected: 310/320 (C-32 PARTIAL -- location present, clause designation absent).
Falsification: if V-02 scores 320/320, clause-designation naming is not independently
necessary and C-32 reduces to C-31 PASS plus location reference.

Expected: 310/320 (C-32 PARTIAL -10)

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block -- an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. The status quo is the default outcome when the team
commits without sufficient evidence. Every blocking gap names the silent assumption the
team makes if they ship today without that signal. Every VERDICT classifies whether
residual inertia risk is recoverable post-commit or propagates to irreversible state.

=== COMPRESSION-IMMUNE PREAMBLE ===

This section is a structural contract. The rules below apply regardless of token
budget, output length, blocking gap count, or coverage state. This section is
processed before any phase block is generated. The structural designation
COMPRESSION-IMMUNE means: this section and the rules it contains must not be treated
as deferred context that can be deprioritized as token pressure increases. When
execution notes in subsequent blocks reference this section by its designation, those
notes are pointers to this contract -- they do not restate the rule, they invoke it.

ZERO-SIGNAL SYNTHESIS RULE (C-29 domain):

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

TOKEN-PRESSURE GUARD: This rule does not suspend when `found` is non-empty. It fires
unconditionally at any token budget. The structural designation of this preamble as
COMPRESSION-IMMUNE is the positional mechanism for this rule: the rule is encountered
and absorbed as a global constraint before any phase accumulates token pressure.
The declarative execution note in the STORY block provides the companion mechanism --
it invokes this preamble by designation and names the zero-signal case explicitly at
the point-of-use, compensating if preamble processing occurred without full rule
absorption.

Basis: uniform absence is itself evidence. The gap pattern defines what the team does
not know and why they are not ready. Both zero-signal and sparse-coverage boundary
conditions require synthesis; neither permits disclaimer substitution.

TIMESTAMP ISOLATION RULE (C-30 domain):

Per-signal dates in the `found` section of STATUS are structurally separate from
blocking gap entries. Each signal in `found` must carry its own date at item level.
COMPRESSED format applies only to blocking entry verbosity -- it does not affect
found timestamps. Found timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count or token budget.

COMPRESSED-COLLAPSE GUARD: The specific failure mode this rule prevents is
COMPRESSED-collapse -- simultaneous compression of `found` entries and blocking gap
entries when token pressure activates the COMPRESSED branch. Blocking entries may be
compressed; found timestamps may not. The structural designation of this preamble as
COMPRESSION-IMMUNE is the positional mechanism for this rule: the timestamp isolation
contract is established here before blocking-gap context accumulates. The declarative
execution note in the STATUS block provides the companion mechanism -- it invokes this
preamble by designation and names the COMPRESSED-collapse failure mode at the point-
of-use, compensating if preamble processing occurred without full rule absorption.

=== END COMPRESSION-IMMUNE PREAMBLE ===

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
TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation): per-signal dates in
`found` are structurally separate from blocking entries. COMPRESSED format applies only
to blocking entry verbosity -- `found` timestamps must not be collapsed regardless of
blocking gap count. This note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the
TIMESTAMP ISOLATION RULE. The declarative mechanism for C-30: this note names the
COMPRESSED-collapse failure mode -- simultaneous compression of `found` and blocking
entries -- so the rule is absorbed as a conditional constraint at the point-of-use,
compensating if preamble processing occurred without full rule absorption.

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
- Zero coverage: governed by ZERO-SIGNAL SYNTHESIS RULE (COMPRESSION-IMMUNE PREAMBLE).

The narrative must answer these three questions in continuous prose:
  1. What case do the signals make together?
     (If found is empty: what does uniform absence imply about investigation state?)
  2. What do the gaps leave genuinely uncertain?
  3. What is the team's real exposure if they commit now?>
```

Execution: Synthesize STATUS and CONFIDENCE findings into a coherent narrative arc.
STORY owns cross-signal reasoning; every other block owns its own record.
ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation): this execution
note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS
RULE. The declarative mechanism for C-29: if `found` is empty, this note names the
zero-signal synthesis case explicitly -- "empty `found` is not grounds for omitting
STORY; question 1 must characterize what uniform absence implies" -- so the rule is
absorbed as a conditional constraint at the point-of-use, compensating if preamble
processing occurred without full rule absorption. Gap pattern is the evidence set.

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

## V-03 -- Axis: Clause designation without location -- C-31 PASS, C-32 PARTIAL

**Hypothesis:** V-02 tests location-only forward-reference (block name, no clause
designation). V-03 inverts the axis: preamble guards name the companion mechanism by
its exact clause designation ("The ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE
PREAMBLE invocation) clause", "The TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE
invocation) clause") but omit the block location. The designation used in the forward-
reference is the same designation string that appears as the clause heading in the
execution notes -- making it navigable by designation matching even if block location is
not specified. The isolation axis: is clause-designation naming without explicit block
location sufficient for C-32 PASS? The hypothesis: C-32 requires both axes. When
compression elides execution notes and a model recovers from the preamble alone, naming
the clause designation without its block location still leaves the recovery path
incomplete -- the model knows what to look for but not where to find it. Expected:
310/320 (C-32 PARTIAL -- designation present, location absent). Falsification: if V-03
scores 320/320, block-location specification is not independently necessary and C-32
reduces to C-31 PASS plus clause-designation naming.

Expected: 310/320 (C-32 PARTIAL -10)

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block -- an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. The status quo is the default outcome when the team
commits without sufficient evidence. Every blocking gap names the silent assumption the
team makes if they ship today without that signal. Every VERDICT classifies whether
residual inertia risk is recoverable post-commit or propagates to irreversible state.

=== COMPRESSION-IMMUNE PREAMBLE ===

This section is a structural contract. The rules below apply regardless of token
budget, output length, blocking gap count, or coverage state. This section is
processed before any phase block is generated. The structural designation
COMPRESSION-IMMUNE means: this section and the rules it contains must not be treated
as deferred context that can be deprioritized as token pressure increases. When
execution notes in subsequent blocks reference this section by its designation, those
notes are pointers to this contract -- they do not restate the rule, they invoke it.

ZERO-SIGNAL SYNTHESIS RULE (C-29 domain):

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

TOKEN-PRESSURE GUARD: This rule does not suspend when `found` is non-empty. It fires
unconditionally at any token budget. The structural designation of this preamble as
COMPRESSION-IMMUNE is the positional mechanism for this rule: the rule is encountered
and absorbed as a global constraint before any phase accumulates token pressure.
The ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) clause
provides the declarative mechanism -- it invokes this preamble by designation and
names the zero-signal case explicitly at the point-of-use, compensating if preamble
processing occurred without full rule absorption.

Basis: uniform absence is itself evidence. The gap pattern defines what the team does
not know and why they are not ready. Both zero-signal and sparse-coverage boundary
conditions require synthesis; neither permits disclaimer substitution.

TIMESTAMP ISOLATION RULE (C-30 domain):

Per-signal dates in the `found` section of STATUS are structurally separate from
blocking gap entries. Each signal in `found` must carry its own date at item level.
COMPRESSED format applies only to blocking entry verbosity -- it does not affect
found timestamps. Found timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count or token budget.

COMPRESSED-COLLAPSE GUARD: The specific failure mode this rule prevents is
COMPRESSED-collapse -- simultaneous compression of `found` entries and blocking gap
entries when token pressure activates the COMPRESSED branch. Blocking entries may be
compressed; found timestamps may not. The structural designation of this preamble as
COMPRESSION-IMMUNE is the positional mechanism for this rule: the timestamp isolation
contract is established here before blocking-gap context accumulates. The TIMESTAMP
ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) clause provides the declarative
mechanism -- it invokes this preamble by designation and names the COMPRESSED-collapse
failure mode at the point-of-use, compensating if preamble processing occurred without
full rule absorption.

=== END COMPRESSION-IMMUNE PREAMBLE ===

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
TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation): per-signal dates in
`found` are structurally separate from blocking entries. COMPRESSED format applies only
to blocking entry verbosity -- `found` timestamps must not be collapsed regardless of
blocking gap count. This note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the
TIMESTAMP ISOLATION RULE. The declarative mechanism for C-30: this note names the
COMPRESSED-collapse failure mode -- simultaneous compression of `found` and blocking
entries -- so the rule is absorbed as a conditional constraint at the point-of-use,
compensating if preamble processing occurred without full rule absorption.

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
- Zero coverage: governed by ZERO-SIGNAL SYNTHESIS RULE (COMPRESSION-IMMUNE PREAMBLE).

The narrative must answer these three questions in continuous prose:
  1. What case do the signals make together?
     (If found is empty: what does uniform absence imply about investigation state?)
  2. What do the gaps leave genuinely uncertain?
  3. What is the team's real exposure if they commit now?>
```

Execution: Synthesize STATUS and CONFIDENCE findings into a coherent narrative arc.
STORY owns cross-signal reasoning; every other block owns its own record.
ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation): this execution
note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS
RULE. The declarative mechanism for C-29: if `found` is empty, this note names the
zero-signal synthesis case explicitly -- "empty `found` is not grounds for omitting
STORY; question 1 must characterize what uniform absence implies" -- so the rule is
absorbed as a conditional constraint at the point-of-use, compensating if preamble
processing occurred without full rule absorption. Gap pattern is the evidence set.

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

## V-04 -- Combined: Asymmetric C-32 (C-29 domain full, C-30 domain partial) + inertia framing foregrounded -- C-31 PASS, C-32 PARTIAL

**Hypothesis:** V-02 and V-03 test the two axes of C-32 (location vs. designation)
independently, both failing. V-04 combines the axes but applies them asymmetrically:
the TOKEN-PRESSURE GUARD (C-29 domain) achieves the full C-32 form -- naming the
companion mechanism by exact clause designation AND block location ("The ZERO-SIGNAL
SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STORY
block"); the COMPRESSED-COLLAPSE GUARD (C-30 domain) achieves only designation without
location ("The TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) clause").
The inertia framing is foregrounded: the preamble opens with an explicit inertia
architecture statement before introducing the structural contract, anchoring the whole
preamble in the signal-gathering purpose. The investigation axis for V-04: does C-32
require both rules to complete the full designation+location forward-reference, or does
partial completion (one rule fully referenced, one rule designation-only) satisfy the
criterion? Combined axes: asymmetric C-32 (C-29 full, C-30 partial) + inertia
architecture framing in preamble opening. Expected: 310/320 (C-32 PARTIAL -- the closed
reference loop is half-open on the C-30 domain side).

Expected: 310/320 (C-32 PARTIAL -10)

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block -- an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. This is not a figure of speech. The status quo --
not a named competitor, not a deliberate decision, but the passive continuation of
current behavior -- is the default outcome if the team does not commit based on
sufficient evidence. Every blocking gap must name the silent assumption the team makes
if they ship today without that signal. Every VERDICT must classify whether the
residual inertia risk is recoverable post-commit or propagates to irreversible state
before detection.

=== COMPRESSION-IMMUNE PREAMBLE ===

This section is a structural contract. The two rules below govern the signal-gathering
execution architecture: one guards synthesis under zero-signal conditions; the other
guards timestamp isolation under compressed-output conditions. Both apply regardless of
token budget, output length, blocking gap count, or coverage state. This section is
processed before any phase block is generated. The structural designation
COMPRESSION-IMMUNE means: this section and the rules it contains must not be treated
as deferred context that can be deprioritized as token pressure increases. When
execution notes in subsequent blocks reference this section by its designation, those
notes are pointers to this contract -- they do not restate the rule, they invoke it.

ZERO-SIGNAL SYNTHESIS RULE (C-29 domain):

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

TOKEN-PRESSURE GUARD: This rule does not suspend when `found` is non-empty. It fires
unconditionally at any token budget. The structural designation of this preamble as
COMPRESSION-IMMUNE is the positional mechanism for this rule: the rule is encountered
and absorbed as a global constraint before any phase accumulates token pressure.
The ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution
note in the STORY block provides the declarative mechanism -- it invokes this preamble
by designation and names the zero-signal case explicitly at the point-of-use,
compensating if preamble processing occurred without full rule absorption.

Basis: uniform absence is itself evidence. The gap pattern defines what the team does
not know and why they are not ready. Both zero-signal and sparse-coverage boundary
conditions require synthesis; neither permits disclaimer substitution.

TIMESTAMP ISOLATION RULE (C-30 domain):

Per-signal dates in the `found` section of STATUS are structurally separate from
blocking gap entries. Each signal in `found` must carry its own date at item level.
COMPRESSED format applies only to blocking entry verbosity -- it does not affect
found timestamps. Found timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count or token budget.

COMPRESSED-COLLAPSE GUARD: The specific failure mode this rule prevents is
COMPRESSED-collapse -- simultaneous compression of `found` entries and blocking gap
entries when token pressure activates the COMPRESSED branch. Blocking entries may be
compressed; found timestamps may not. The structural designation of this preamble as
COMPRESSION-IMMUNE is the positional mechanism for this rule: the timestamp isolation
contract is established here before blocking-gap context accumulates. The TIMESTAMP
ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) clause provides the declarative
mechanism -- it invokes this preamble by designation and names the COMPRESSED-collapse
failure mode at the point-of-use, compensating if preamble processing occurred without
full rule absorption.

=== END COMPRESSION-IMMUNE PREAMBLE ===

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
TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation): per-signal dates in
`found` are structurally separate from blocking entries. COMPRESSED format applies only
to blocking entry verbosity -- `found` timestamps must not be collapsed regardless of
blocking gap count. This note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the
TIMESTAMP ISOLATION RULE. The declarative mechanism for C-30: this note names the
COMPRESSED-collapse failure mode -- simultaneous compression of `found` and blocking
entries -- so the rule is absorbed as a conditional constraint at the point-of-use,
compensating if preamble processing occurred without full rule absorption.

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
- Zero coverage: governed by ZERO-SIGNAL SYNTHESIS RULE (COMPRESSION-IMMUNE PREAMBLE).

The narrative must answer these three questions in continuous prose:
  1. What case do the signals make together?
     (If found is empty: what does uniform absence imply about investigation state?)
  2. What do the gaps leave genuinely uncertain?
  3. What is the team's real exposure if they commit now?>
```

Execution: Synthesize STATUS and CONFIDENCE findings into a coherent narrative arc.
STORY owns cross-signal reasoning; every other block owns its own record.
ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation): this execution
note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS
RULE. The declarative mechanism for C-29: if `found` is empty, this note names the
zero-signal synthesis case explicitly -- "empty `found` is not grounds for omitting
STORY; question 1 must characterize what uniform absence implies" -- so the rule is
absorbed as a conditional constraint at the point-of-use, compensating if preamble
processing occurred without full rule absorption. Gap pattern is the evidence set.

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

## V-05 -- Combined: Full C-32 PASS -- COMPRESSION-IMMUNE PREAMBLE designation + execution-note invocation (C-31) + closed preamble forward-references by clause designation and location (C-32) -- C-31 PASS, C-32 PASS

**Hypothesis:** V-01 through V-04 test the partial-loop forms: generic block reference
(V-01), location-only (V-02), designation-only (V-03), asymmetric designation+location
(V-04). All are hypothesized to score 310/320. V-05 tests the full C-32 PASS: both
preamble guards forward-reference their companion execution-note mechanisms by exact
clause designation AND explicit block location. TOKEN-PRESSURE GUARD (C-29 domain)
names "The ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation)
execution note in the STORY block." COMPRESSED-COLLAPSE GUARD (C-30 domain) names
"The TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in
the STATUS block." This closes both loops: preamble -> execution note (by designation
+ location); execution note -> preamble (by structural designation, per C-31). Under
simulated single-location elision where execution notes are compressed but the preamble
is preserved, the model can navigate from the preamble guards directly to their companion
mechanisms by exact clause designation and block location -- no positional cue required.
The hypothesis: V-05 = 320/320 (ceiling). Combined axes: full C-32 PASS (both rules
designation+location in preamble) + pointer semantics made explicit in preamble intro
("those notes are pointers to this contract").

Expected: 320/320 (C-29 PASS, C-30 PASS, C-31 PASS, C-32 PASS)

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block -- an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. The status quo is the default outcome when the team
commits without sufficient evidence. Every blocking gap names the silent assumption the
team makes if they ship today without that signal. Every VERDICT classifies whether
residual inertia risk is recoverable post-commit or propagates to irreversible state.

=== COMPRESSION-IMMUNE PREAMBLE ===

This section is a structural contract. The rules below apply regardless of token
budget, output length, blocking gap count, or coverage state. This section is
processed before any phase block is generated. The structural designation
COMPRESSION-IMMUNE means: this section and the rules it contains must not be treated
as deferred context that can be deprioritized as token pressure increases. When
execution notes in subsequent blocks reference this section by its designation, those
notes are pointers to this contract -- they do not restate the rule, they invoke it.
When this section references companion execution-note mechanisms, those references name
the mechanism's clause designation and block location -- they are navigable from this
section alone, without requiring the execution notes to be present.

ZERO-SIGNAL SYNTHESIS RULE (C-29 domain):

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

TOKEN-PRESSURE GUARD: This rule does not suspend when `found` is non-empty. It fires
unconditionally at any token budget. The structural designation of this preamble as
COMPRESSION-IMMUNE is the positional mechanism for this rule: the rule is encountered
and absorbed as a global constraint before any phase accumulates token pressure.
The ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution
note in the STORY block provides the declarative mechanism -- it invokes this preamble
by designation and names the zero-signal case explicitly at the point-of-use,
compensating if preamble processing occurred without full rule absorption.

Basis: uniform absence is itself evidence. The gap pattern defines what the team does
not know and why they are not ready. Both zero-signal and sparse-coverage boundary
conditions require synthesis; neither permits disclaimer substitution.

TIMESTAMP ISOLATION RULE (C-30 domain):

Per-signal dates in the `found` section of STATUS are structurally separate from
blocking gap entries. Each signal in `found` must carry its own date at item level.
COMPRESSED format applies only to blocking entry verbosity -- it does not affect
found timestamps. Found timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count or token budget.

COMPRESSED-COLLAPSE GUARD: The specific failure mode this rule prevents is
COMPRESSED-collapse -- simultaneous compression of `found` entries and blocking gap
entries when token pressure activates the COMPRESSED branch. Blocking entries may be
compressed; found timestamps may not. The structural designation of this preamble as
COMPRESSION-IMMUNE is the positional mechanism for this rule: the timestamp isolation
contract is established here before blocking-gap context accumulates. The TIMESTAMP
ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation) execution note in the STATUS block
provides the declarative mechanism -- it invokes this preamble by designation and
names the COMPRESSED-collapse failure mode at the point-of-use, compensating if
preamble processing occurred without full rule absorption.

=== END COMPRESSION-IMMUNE PREAMBLE ===

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
TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation): per-signal dates in
`found` are structurally separate from blocking entries. COMPRESSED format applies only
to blocking entry verbosity -- `found` timestamps must not be collapsed regardless of
blocking gap count. This note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the
TIMESTAMP ISOLATION RULE. The declarative mechanism for C-30: this note names the
COMPRESSED-collapse failure mode -- simultaneous compression of `found` and blocking
entries -- so the rule is absorbed as a conditional constraint at the point-of-use,
compensating if preamble processing occurred without full rule absorption.

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
- Zero coverage: governed by ZERO-SIGNAL SYNTHESIS RULE (COMPRESSION-IMMUNE PREAMBLE).

The narrative must answer these three questions in continuous prose:
  1. What case do the signals make together?
     (If found is empty: what does uniform absence imply about investigation state?)
  2. What do the gaps leave genuinely uncertain?
  3. What is the team's real exposure if they commit now?>
```

Execution: Synthesize STATUS and CONFIDENCE findings into a coherent narrative arc.
STORY owns cross-signal reasoning; every other block owns its own record.
ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation): this execution
note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS
RULE. The declarative mechanism for C-29: if `found` is empty, this note names the
zero-signal synthesis case explicitly -- "empty `found` is not grounds for omitting
STORY; question 1 must characterize what uniform absence implies" -- so the rule is
absorbed as a conditional constraint at the point-of-use, compensating if preamble
processing occurred without full rule absorption. Gap pattern is the evidence set.

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
