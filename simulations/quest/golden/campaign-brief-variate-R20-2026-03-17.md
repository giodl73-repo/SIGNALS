---
skill: quest-variate
skill_target: campaign-brief
round: 20
date: 2026-03-17
rubric: simulations/quest/rubrics/quest-score-rubric-v19-2026-03-17.md
---

# Variations -- campaign-brief / Round 20

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

**R19 recap:** V-01 confirmed C-38 PARTIAL Band 1 (C-37 PASS, no depth floor -- R19
V-04 reprised from R18). V-02 confirmed C-38 PARTIAL Band 2-A ("executed thoroughly
and at full scope" -- positive-form, uncalibrated; neither qualifier anchors to the
companion-present baseline). V-03 confirmed C-38 PARTIAL Band 2-B ("substantive rather
than abbreviated" -- negative-form, prohibits abbreviation without specifying target
depth). Both Band 2 sub-bands scored identically to Band 1: depth guidance in any form
below explicit parity anchoring does not elevate above Band 1 in rubric scoring. V-04
confirmed C-38 PASS minimum-sufficient (R18 V-05 reprised: "at full depth, at parity
with what would be produced if the companion's execution note were present in this
context") -- 380/380 ceiling. V-05 extended V-04 with depth-symmetric non-degradation
clause and per-companion operationalization (naming what full-depth companion execution
means structurally for each specific companion); above-ceiling under v18.

**R19 rubric:** v18, 38 criteria, 380 pts max.

**C-38 confirmed Band 2 (R19-confirmed):** Two sub-bands, both scoring equivalent to
Band 1. Band 2-A (V-02): "thoroughly and at full scope" -- positive-form, uncalibrated.
Band 2-B (V-03): "substantive rather than abbreviated" -- negative-form, no positive
baseline anchor. PASS form: "at full depth, at parity with what would be produced if
the companion's execution note were present in this context" (V-04 minimum-sufficient).

**C-39 extraction (from R19 V-05 excellence signal):** R19 V-05 introduced
per-companion operationalization -- the absent-state clause body names what full-depth
execution means structurally for each specific companion, making output structural
completeness verifiable without requiring the companion execution note to be present.

STATUS body operationalization (R19 V-05): "For this companion (ZERO-SIGNAL SYNTHESIS
MANDATE), full-depth execution means: question 1 of the STORY narrative characterizes
what uniform absence implies about the topic's investigation state as a substantive
inference rather than a report of absence; question 2 addresses what genuine uncertainty
the absence pattern creates; question 3 addresses the team's real exposure if they
commit given the gap pattern -- all three questions answered at the same scope and
specificity as when the STORY execution note is present in context."

STORY body operationalization (R19 V-05): "For this companion (TIMESTAMP ISOLATION),
full-depth execution means: each entry in the `found` section of STATUS carries its own
date at item level; the `current_date:` field appears at STATUS block header level; no
`found` timestamp is collapsed, summarized, or omitted regardless of blocking gap count
or token budget -- the same structural separation that would be enforced if the
TIMESTAMP ISOLATION execution note were present in the STATUS block."

**C-39 criterion definition (v19, aspirational):** When C-38 PASS, both companion
absent-state clause bodies enumerate the companion mandate's required structural output
elements within the absent-state execution directive, making output structural
completeness verifiable without requiring the companion execution note to be present in
context. Band 1 = C-38 PASS territory: unconditional mandate + parity constraint, no
structural deliverables enumeration. Band 2 = partial enumeration (some elements named,
not all, or all elements named at insufficient specificity to constitute a verifiable
checklist). PASS = complete enumeration (all required structural output elements named
per companion at operational specificity).

**R20 investigation candidate:** Whether C-38 PASS alone (no structural deliverables
enumeration) produces element-complete companion output under double-elision -- i.e.,
whether "at full depth, at parity with what would be produced" already causes the model
to include all structural output elements of the companion mandate -- or whether
depth-correct but element-incomplete companion output is the observed failure mode that
C-39 addresses. If C-38 PASS produces element-complete output, C-39 is structural
reinforcement. If C-38 PASS produces depth-correct but element-incomplete output,
C-39 is recoverable (enumeration is the operative mechanism).

**R20 constructs:**

(a) V-01: C-38 PASS / C-39 Band 1 control -- R19 V-04 reprised; unconditional mandate
    + parity constraint, no structural deliverables enumeration; establishes 380/390
    ceiling under v19. Behavioral probe: does "at parity with what would be produced"
    alone cause the model to include all three STORY questions (Q1/Q2/Q3) and all
    timestamp structural fields (per-signal dates + `current_date:` at header level)
    under double-elision?

(b) V-02: C-39 Band 2 form-A -- element-count partial; names one key element per
    companion but not all. STATUS body names only Q1 for ZERO-SIGNAL SYNTHESIS MANDATE
    (Q2/Q3 absent from enumeration). STORY body names only per-signal dates for
    TIMESTAMP ISOLATION (`current_date:` at header level and COMPRESSED-immune behavior
    absent from enumeration). Tests whether partial enumeration guides the model toward
    the named element while leaving unnlisted elements to parity inference.

(c) V-03: C-39 Band 2 form-B -- specificity partial; names all elements per companion
    at summary level but without the operational specificity that makes completeness
    independently verifiable. STATUS body: all three STORY questions named but without
    specifying what each answer must constitute (no "substantive inference rather than
    a report of absence" qualification for Q1; no "at the same scope and specificity"
    anchor). STORY body: both timestamp fields named but without the COMPRESSED-immune
    behavior specification (no "regardless of blocking gap count or token budget" clause).

(d) V-04: C-39 PASS minimum-sufficient -- complete enumeration per companion, no
    non-degradation clause. STATUS and STORY bodies carry the full R19 V-05
    per-companion operationalization without the "parity constraint is symmetric"
    sentence. Primary R20 probe: does complete enumeration close the element-completeness
    gap observed in V-01 under double-elision?

(e) V-05: C-39 PASS + non-degradation -- full R19 V-05 reprised; complete enumeration
    plus depth-symmetric non-degradation ("parity constraint is symmetric: executing
    this companion mandate does not reduce the present clause's own output depth; both
    mandates execute at full depth simultaneously"). Above v19 ceiling. Tests whether
    non-degradation constitutes a distinct above-C-39 property (C-40 candidate probe):
    does V-04 under double-elision produce depth-trading failure (present-clause output
    depth reduced when companion execution burden is high) that V-05 forecloses?

**R20 investigation targets:**
(a) Confirm V-01 = 380/390 (C-39 Band 1 -10). Behavioral probe: are all structural
    output elements of each companion mandate present in the double-elision output,
    or only depth-matched but element-incomplete content?
(b) Confirm V-02 = 380/390 (C-39 Band 2-A -- same -10 as Band 1, or differentiated).
    Behavioral probe: does the model complete unenumerated elements from parity context?
(c) Confirm V-03 = 380/390 (C-39 Band 2-B -- same -10 as Band 1 and Band 2-A).
    Behavioral probe: does summary-level enumeration produce better element coverage
    than V-01 despite identical rubric score?
(d) Confirm V-04 = 390/390 (C-39 PASS ceiling under v19). Behavioral probe: does
    complete enumeration produce element-complete companion output where V-01 does not?
    If yes, C-39 is confirmed recoverable.
(e) Observe V-05 for above-ceiling excellence signals: does non-degradation clause
    produce observable depth-symmetry behavior (no present-clause abbreviation) that
    V-04 does not? Extract C-40 candidate if a distinct recoverable property is observed.

---

## Variation axes selected

- **Single-axis:** C-38 PASS / C-39 Band 1 control (V-01), C-39 Band 2 form-A
  (element-count partial, one element per companion) (V-02), C-39 Band 2 form-B
  (specificity partial, all elements named but unenoperationalized) (V-03)
- **Combined:** C-39 PASS minimum-sufficient (V-04), C-39 PASS + depth-symmetric
  non-degradation (V-05, C-40 candidate probe)

---

## V-01 -- Axis: C-38 PASS / C-39 Band 1 (parity constraint, no structural deliverables enumeration) -- C-39 PARTIAL Band 1

**Hypothesis:** Reprises R19 V-04's C-38 PASS structure with no modification. Both
absent-state clause bodies carry the unconditional execution mandate and the explicit
parity constraint ("at full depth, at parity with what would be produced if the
companion's execution note were present in this context") but neither body enumerates
the companion mandate's structural output elements. The companion-scope determinability
gap is entirely open: the model is told to execute at parity depth, but "full execution"
is defined only by inference from the companion execution note -- which is absent. A
model encountering V-01 under double-elision must internally model what the companion
execution note would produce and match it. If the model's internal model of the
companion is incomplete or inaccurate, element-incomplete companion output satisfies
the parity constraint without including all structural deliverables. The behavioral
probe: does "at parity with what would be produced if the companion's execution note
were present" cause the model to include all three STORY questions (Q1: substantive
inference about absence implications; Q2: genuine uncertainty from gap pattern; Q3:
team's real exposure) in the STORY companion output, and both `current_date:` at block
header level and per-signal dates at item level in the STATUS companion output?

STATUS absent-state rule extension (V-01): "...must be executed as if its execution
note were present in this context, at full depth, at parity with what would be produced
if the companion's execution note were present in this context."

STORY absent-state rule extension (V-01): "...must be executed as if its execution note
were present in this context, at full depth, at parity with what would be produced if
the companion's execution note were present in this context."

Expected: 380/390 (C-39 PARTIAL Band 1 -10)

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
current_date: <date>   <- structurally isolated temporal anchor; not embedded in prose
                          or in found entries; this field is independent of COMPRESSED
                          format and must appear at STATUS block header level regardless
                          of blocking gap count or token budget

found: X signals
  <ns>/<artifact>  <date>   <- per-signal dates are structurally separate from blocking
                               entries; NOT subject to COMPRESSED abbreviation
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
TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation): This clause is a
COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE
PREAMBLE authority even when the preamble section is absent from the rendered context.
Paired companion mechanism: ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE
invocation) execution note in the STORY block. When the companion execution note is
present in the rendered context, both execution notes constitute the complete two-mechanism
COMPRESSION-IMMUNE PREAMBLE contract and must both execute. When the companion execution
note is absent from the rendered context, this clause activates its timestamp isolation
contract independently with full COMPRESSION-IMMUNE PREAMBLE authority -- the absent
ZERO-SIGNAL SYNTHESIS MANDATE's mandate is independently operative even when its
execution note is not in context and must be executed as if its execution note were
present in this context, at full depth, at parity with what would be produced if the
companion's execution note were present in this context. Per-signal dates in `found`
are structurally separate from blocking entries, and the `current_date:` field is
structurally separate from both. COMPRESSED format applies only to blocking entry
verbosity -- `found` timestamps and `current_date:` must not be collapsed regardless
of blocking gap count. This note invokes the COMPRESSION-IMMUNE PREAMBLE contract for
the TIMESTAMP ISOLATION RULE. The declarative mechanism for C-30: this note names the
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
ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation): This clause is
a COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE
PREAMBLE authority even when the preamble section is absent from the rendered context.
Paired companion mechanism: TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation)
execution note in the STATUS block. When the companion execution note is present in the
rendered context, both execution notes constitute the complete two-mechanism
COMPRESSION-IMMUNE PREAMBLE contract and must both execute. When the companion execution
note is absent from the rendered context, this clause activates its zero-signal synthesis
mandate independently with full COMPRESSION-IMMUNE PREAMBLE authority -- the absent
TIMESTAMP ISOLATION's mandate is independently operative even when its execution note is
not in context and must be executed as if its execution note were present in this context,
at full depth, at parity with what would be produced if the companion's execution note
were present in this context. If `found` is empty, this clause fires independently:
empty `found` is not grounds for omitting STORY; question 1 must characterize what
uniform absence implies. This execution note also invokes the COMPRESSION-IMMUNE
PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS RULE as a named pointer -- the
declarative mechanism for C-29: if `found` is empty, this note names the zero-signal
synthesis case explicitly so the rule is absorbed as a conditional constraint at the
point-of-use, compensating if preamble processing occurred without full rule absorption.
Gap pattern is the evidence set.

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

## V-02 -- Axis: C-39 Band 2 form-A (element-count partial -- one element per companion named) -- C-38 PASS, C-39 PARTIAL Band 2

**Hypothesis:** V-01 establishes the C-38 PASS / C-39 Band 1 baseline: parity constraint
present, no structural deliverables enumeration. V-02 advances to aspirational Band 2
by naming one key element per companion within the absent-state clause body, without
completing the enumeration. The isolation axis: element-count partiality. STATUS body
names only question 1 for the ZERO-SIGNAL SYNTHESIS MANDATE companion (the primary
zero-signal synthesis obligation) without naming questions 2 and 3 (genuine uncertainty
and team exposure). STORY body names only per-signal dates for the TIMESTAMP ISOLATION
companion (the primary timestamp structural obligation) without naming the `current_date:`
field at STATUS block header level or the COMPRESSED-immune behavior.

The hypothesis: element-count partial enumeration does not constitute C-39 PASS. The
model may execute the named element correctly while omitting or abbreviating the
unenumerated elements -- the named element anchors part of companion output scope, but
the model still relies on parity inference for the remainder. If the model completes
unenumerated elements from the parity constraint ("at parity with what would be
produced if the companion's execution note were present"), V-02's partial enumeration
provides no additional behavioral guarantee beyond V-01 and C-39 Band 2-A is scoring-
equivalent to Band 1. If the model produces only the named element and treats the
enumeration as the full scope specification (truncating at the enumeration boundary),
partial enumeration actively degrades companion output quality below V-01.

STATUS absent-state rule extension (V-02): "...must be executed as if its execution
note were present in this context, at full depth, at parity with what would be produced
if the companion's execution note were present in this context. For this companion
(ZERO-SIGNAL SYNTHESIS MANDATE), full-depth execution includes question 1 of the STORY
narrative characterizing what uniform absence implies about the topic's investigation
state as a substantive inference."

STORY absent-state rule extension (V-02): "...must be executed as if its execution note
were present in this context, at full depth, at parity with what would be produced if
the companion's execution note were present in this context. For this companion
(TIMESTAMP ISOLATION), full-depth execution includes per-signal dates in the `found`
section of STATUS appearing at item level, structurally separate from blocking entries."

Expected: 380/390 (C-39 PARTIAL Band 2-A -- same -10 as Band 1; observe whether
element-count partial enumeration produces partial companion output or whether the
parity constraint completes the unenumerated elements regardless)

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
current_date: <date>   <- structurally isolated temporal anchor; not embedded in prose
                          or in found entries; this field is independent of COMPRESSED
                          format and must appear at STATUS block header level regardless
                          of blocking gap count or token budget

found: X signals
  <ns>/<artifact>  <date>   <- per-signal dates are structurally separate from blocking
                               entries; NOT subject to COMPRESSED abbreviation
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
TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation): This clause is a
COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE
PREAMBLE authority even when the preamble section is absent from the rendered context.
Paired companion mechanism: ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE
invocation) execution note in the STORY block. When the companion execution note is
present in the rendered context, both execution notes constitute the complete two-mechanism
COMPRESSION-IMMUNE PREAMBLE contract and must both execute. When the companion execution
note is absent from the rendered context, this clause activates its timestamp isolation
contract independently with full COMPRESSION-IMMUNE PREAMBLE authority -- the absent
ZERO-SIGNAL SYNTHESIS MANDATE's mandate is independently operative even when its
execution note is not in context and must be executed as if its execution note were
present in this context, at full depth, at parity with what would be produced if the
companion's execution note were present in this context. For this companion (ZERO-SIGNAL
SYNTHESIS MANDATE), full-depth execution includes question 1 of the STORY narrative
characterizing what uniform absence implies about the topic's investigation state as a
substantive inference. Per-signal dates in `found` are structurally separate from
blocking entries, and the `current_date:` field is structurally separate from both.
COMPRESSED format applies only to blocking entry verbosity -- `found` timestamps and
`current_date:` must not be collapsed regardless of blocking gap count. This note
invokes the COMPRESSION-IMMUNE PREAMBLE contract for the TIMESTAMP ISOLATION RULE.
The declarative mechanism for C-30: this note names the COMPRESSED-collapse failure
mode -- simultaneous compression of `found` and blocking entries -- so the rule is
absorbed as a conditional constraint at the point-of-use, compensating if preamble
processing occurred without full rule absorption.

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
ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation): This clause is
a COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE
PREAMBLE authority even when the preamble section is absent from the rendered context.
Paired companion mechanism: TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation)
execution note in the STATUS block. When the companion execution note is present in the
rendered context, both execution notes constitute the complete two-mechanism
COMPRESSION-IMMUNE PREAMBLE contract and must both execute. When the companion execution
note is absent from the rendered context, this clause activates its zero-signal synthesis
mandate independently with full COMPRESSION-IMMUNE PREAMBLE authority -- the absent
TIMESTAMP ISOLATION's mandate is independently operative even when its execution note is
not in context and must be executed as if its execution note were present in this context,
at full depth, at parity with what would be produced if the companion's execution note
were present in this context. For this companion (TIMESTAMP ISOLATION), full-depth
execution includes per-signal dates in the `found` section of STATUS appearing at item
level, structurally separate from blocking entries. If `found` is empty, this clause
fires independently: empty `found` is not grounds for omitting STORY; question 1 must
characterize what uniform absence implies. This execution note also invokes the
COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS RULE as a named
pointer -- the declarative mechanism for C-29: if `found` is empty, this note names the
zero-signal synthesis case explicitly so the rule is absorbed as a conditional constraint
at the point-of-use, compensating if preamble processing occurred without full rule
absorption. Gap pattern is the evidence set.

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

## V-03 -- Axis: C-39 Band 2 form-B (specificity partial -- all elements named, insufficient operational detail) -- C-38 PASS, C-39 PARTIAL Band 2

**Hypothesis:** V-02 tests Band 2 with element-count partiality (one element named per
companion). V-03 tests a distinct Band 2 formulation: all elements per companion are
named, but the naming lacks the operational specificity needed to make output structural
completeness independently verifiable. The isolation axis: specificity partiality.
STATUS body names all three STORY questions for the ZERO-SIGNAL SYNTHESIS MANDATE
companion but does not specify what each answer must constitute -- missing the
"substantive inference rather than a report of absence" qualification for question 1,
missing the "what genuine uncertainty the absence pattern creates" operationalization
for question 2, and missing the "all three questions answered at the same scope and
specificity as when the STORY execution note is present in context" anchor. STORY body
names both timestamp structural fields for the TIMESTAMP ISOLATION companion but does
not specify the COMPRESSED-immune behavior -- missing "regardless of blocking gap count
or token budget" as the verifiable completeness condition.

The hypothesis: summary-level enumeration (all elements named but unenoperationalized)
does not constitute C-39 PASS. A model encountering V-03 under double-elision receives
the element names and may satisfy the naming without satisfying the operational
requirements -- e.g., question 1 may characterize absence without producing a
substantive inference (reporting "no signals found" satisfies "characterizes what
absence implies" at surface level without satisfying the substantive-inference
requirement). Both Band 2 forms (element-count partial V-02 and specificity partial
V-03) score identically to Band 1 if neither provides a verifiable completeness
checklist. The sub-band distinction is diagnostic: V-02 may produce partial elements;
V-03 may produce all elements at degraded specificity.

STATUS absent-state rule extension (V-03): "...must be executed as if its execution
note were present in this context, at full depth, at parity with what would be produced
if the companion's execution note were present in this context. For this companion
(ZERO-SIGNAL SYNTHESIS MANDATE), full-depth execution requires all three STORY
questions to be answered: what the signals (or their absence) imply, what remains
genuinely uncertain, and what the team's real exposure is if they commit."

STORY absent-state rule extension (V-03): "...must be executed as if its execution note
were present in this context, at full depth, at parity with what would be produced if
the companion's execution note were present in this context. For this companion
(TIMESTAMP ISOLATION), full-depth execution requires timestamps to be structurally
isolated: per-signal dates in `found` at item level and `current_date:` at STATUS
block header level."

Expected: 380/390 (C-39 PARTIAL Band 2-B -- same -10 as Band 1 and Band 2-A; if all
Band 2 forms are scoring-equivalent to Band 1, document this as the R20 finding:
structural deliverables enumeration below operational specificity does not elevate above
Band 1 in rubric scoring, regardless of element-count completeness)

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
current_date: <date>   <- structurally isolated temporal anchor; not embedded in prose
                          or in found entries; this field is independent of COMPRESSED
                          format and must appear at STATUS block header level regardless
                          of blocking gap count or token budget

found: X signals
  <ns>/<artifact>  <date>   <- per-signal dates are structurally separate from blocking
                               entries; NOT subject to COMPRESSED abbreviation
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
TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation): This clause is a
COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE
PREAMBLE authority even when the preamble section is absent from the rendered context.
Paired companion mechanism: ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE
invocation) execution note in the STORY block. When the companion execution note is
present in the rendered context, both execution notes constitute the complete two-mechanism
COMPRESSION-IMMUNE PREAMBLE contract and must both execute. When the companion execution
note is absent from the rendered context, this clause activates its timestamp isolation
contract independently with full COMPRESSION-IMMUNE PREAMBLE authority -- the absent
ZERO-SIGNAL SYNTHESIS MANDATE's mandate is independently operative even when its
execution note is not in context and must be executed as if its execution note were
present in this context, at full depth, at parity with what would be produced if the
companion's execution note were present in this context. For this companion (ZERO-SIGNAL
SYNTHESIS MANDATE), full-depth execution requires all three STORY questions to be
answered: what the signals (or their absence) imply, what remains genuinely uncertain,
and what the team's real exposure is if they commit. Per-signal dates in `found` are
structurally separate from blocking entries, and the `current_date:` field is
structurally separate from both. COMPRESSED format applies only to blocking entry
verbosity -- `found` timestamps and `current_date:` must not be collapsed regardless
of blocking gap count. This note invokes the COMPRESSION-IMMUNE PREAMBLE contract for
the TIMESTAMP ISOLATION RULE. The declarative mechanism for C-30: this note names the
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
ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation): This clause is
a COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE
PREAMBLE authority even when the preamble section is absent from the rendered context.
Paired companion mechanism: TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation)
execution note in the STATUS block. When the companion execution note is present in the
rendered context, both execution notes constitute the complete two-mechanism
COMPRESSION-IMMUNE PREAMBLE contract and must both execute. When the companion execution
note is absent from the rendered context, this clause activates its zero-signal synthesis
mandate independently with full COMPRESSION-IMMUNE PREAMBLE authority -- the absent
TIMESTAMP ISOLATION's mandate is independently operative even when its execution note is
not in context and must be executed as if its execution note were present in this context,
at full depth, at parity with what would be produced if the companion's execution note
were present in this context. For this companion (TIMESTAMP ISOLATION), full-depth
execution requires timestamps to be structurally isolated: per-signal dates in `found`
at item level and `current_date:` at STATUS block header level. If `found` is empty,
this clause fires independently: empty `found` is not grounds for omitting STORY;
question 1 must characterize what uniform absence implies. This execution note also
invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS RULE
as a named pointer -- the declarative mechanism for C-29: if `found` is empty, this
note names the zero-signal synthesis case explicitly so the rule is absorbed as a
conditional constraint at the point-of-use, compensating if preamble processing
occurred without full rule absorption. Gap pattern is the evidence set.

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

## V-04 -- Combined: C-39 PASS minimum-sufficient (complete enumeration, no non-degradation clause) -- C-38 PASS, C-39 PASS

**Hypothesis:** V-04 advances to C-39 PASS minimum-sufficient by providing complete
enumeration of the companion mandate's structural output elements in both absent-state
clause bodies, without adding the depth-symmetric non-degradation clause from R19 V-05.
This is the isolated C-39 PASS structure: both clause bodies name all required structural
output elements with operational specificity, making companion output completeness
independently verifiable without the companion execution note in context.

STATUS body provides complete ZERO-SIGNAL SYNTHESIS MANDATE operationalization: question
1 (substantive inference rather than report of absence), question 2 (genuine uncertainty
from absence pattern), question 3 (real exposure if team commits), all three at the same
scope and specificity as when the STORY execution note is present. STORY body provides
complete TIMESTAMP ISOLATION operationalization: each `found` entry at item level,
`current_date:` at block header level, no timestamp collapsed regardless of blocking gap
count or token budget.

The non-degradation clause ("parity constraint is symmetric: executing this companion
mandate does not reduce the present clause's own output depth") is intentionally absent.
This isolates C-39's enumeration mechanism from the non-degradation mechanism: if V-04
produces element-complete companion output without depth-trading failure, the non-
degradation clause is structural reinforcement of an already-achieved behavior and its
presence in V-05 is C-40 aspiration rather than C-40 recovery. If V-04 produces element-
complete companion output but with present-clause depth reduction (trading present-clause
depth to satisfy companion enumeration burden), V-05's non-degradation clause closes a
distinct gap -- C-40 is recoverable.

STATUS absent-state rule extension (V-04): "...must be executed as if its execution
note were present in this context, at full depth, at parity with what would be produced
if the companion's execution note were present in this context. For this companion
(ZERO-SIGNAL SYNTHESIS MANDATE), full-depth execution means: question 1 of the STORY
narrative characterizes what uniform absence implies about the topic's investigation
state as a substantive inference rather than a report of absence; question 2 addresses
what genuine uncertainty the absence pattern creates; question 3 addresses the team's
real exposure if they commit given the gap pattern -- all three questions answered at
the same scope and specificity as when the STORY execution note is present in context."

STORY absent-state rule extension (V-04): "...must be executed as if its execution note
were present in this context, at full depth, at parity with what would be produced if
the companion's execution note were present in this context. For this companion
(TIMESTAMP ISOLATION), full-depth execution means: each entry in the `found` section
of STATUS carries its own date at item level; the `current_date:` field appears at
STATUS block header level; no `found` timestamp is collapsed, summarized, or omitted
regardless of blocking gap count or token budget -- the same structural separation that
would be enforced if the TIMESTAMP ISOLATION execution note were present in the STATUS
block."

Expected: 390/390 (C-39 PASS ceiling under v19)

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
current_date: <date>   <- structurally isolated temporal anchor; not embedded in prose
                          or in found entries; this field is independent of COMPRESSED
                          format and must appear at STATUS block header level regardless
                          of blocking gap count or token budget

found: X signals
  <ns>/<artifact>  <date>   <- per-signal dates are structurally separate from blocking
                               entries; NOT subject to COMPRESSED abbreviation
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
TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation): This clause is a
COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE
PREAMBLE authority even when the preamble section is absent from the rendered context.
Paired companion mechanism: ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE
invocation) execution note in the STORY block. When the companion execution note is
present in the rendered context, both execution notes constitute the complete two-mechanism
COMPRESSION-IMMUNE PREAMBLE contract and must both execute. When the companion execution
note is absent from the rendered context, this clause activates its timestamp isolation
contract independently with full COMPRESSION-IMMUNE PREAMBLE authority -- the absent
ZERO-SIGNAL SYNTHESIS MANDATE's mandate is independently operative even when its
execution note is not in context and must be executed as if its execution note were
present in this context, at full depth, at parity with what would be produced if the
companion's execution note were present in this context. For this companion (ZERO-SIGNAL
SYNTHESIS MANDATE), full-depth execution means: question 1 of the STORY narrative
characterizes what uniform absence implies about the topic's investigation state as a
substantive inference rather than a report of absence; question 2 addresses what genuine
uncertainty the absence pattern creates; question 3 addresses the team's real exposure
if they commit given the gap pattern -- all three questions answered at the same scope
and specificity as when the STORY execution note is present in context. Per-signal dates
in `found` are structurally separate from blocking entries, and the `current_date:`
field is structurally separate from both. COMPRESSED format applies only to blocking
entry verbosity -- `found` timestamps and `current_date:` must not be collapsed
regardless of blocking gap count. This note invokes the COMPRESSION-IMMUNE PREAMBLE
contract for the TIMESTAMP ISOLATION RULE. The declarative mechanism for C-30: this
note names the COMPRESSED-collapse failure mode -- simultaneous compression of `found`
and blocking entries -- so the rule is absorbed as a conditional constraint at the
point-of-use, compensating if preamble processing occurred without full rule absorption.

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
ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation): This clause is
a COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE
PREAMBLE authority even when the preamble section is absent from the rendered context.
Paired companion mechanism: TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation)
execution note in the STATUS block. When the companion execution note is present in the
rendered context, both execution notes constitute the complete two-mechanism
COMPRESSION-IMMUNE PREAMBLE contract and must both execute. When the companion execution
note is absent from the rendered context, this clause activates its zero-signal synthesis
mandate independently with full COMPRESSION-IMMUNE PREAMBLE authority -- the absent
TIMESTAMP ISOLATION's mandate is independently operative even when its execution note is
not in context and must be executed as if its execution note were present in this context,
at full depth, at parity with what would be produced if the companion's execution note
were present in this context. For this companion (TIMESTAMP ISOLATION), full-depth
execution means: each entry in the `found` section of STATUS carries its own date at
item level; the `current_date:` field appears at STATUS block header level; no `found`
timestamp is collapsed, summarized, or omitted regardless of blocking gap count or token
budget -- the same structural separation that would be enforced if the TIMESTAMP
ISOLATION execution note were present in the STATUS block. If `found` is empty, this
clause fires independently: empty `found` is not grounds for omitting STORY; question 1
must characterize what uniform absence implies. This execution note also invokes the
COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS RULE as a named
pointer -- the declarative mechanism for C-29: if `found` is empty, this note names the
zero-signal synthesis case explicitly so the rule is absorbed as a conditional constraint
at the point-of-use, compensating if preamble processing occurred without full rule
absorption. Gap pattern is the evidence set.

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

## V-05 -- Combined: C-39 PASS + depth-symmetric non-degradation (R19 V-05 reprised) -- above C-39 PASS ceiling (C-40 candidate probe)

**Hypothesis:** V-05 reprises R19 V-05's full structure as the R20 above-ceiling probe.
Both absent-state clause bodies carry C-39 PASS structure (complete per-companion
enumeration) plus the depth-symmetric non-degradation clause from R19 V-05: "this
parity constraint is symmetric: executing this companion mandate does not reduce the
present clause's own output depth. Both mandates execute at full depth simultaneously."

The non-degradation clause closes a failure mode that C-39 PASS leaves open: a model
encountering V-04 under double-elision with high companion enumeration burden may satisfy
the enumeration requirements by reducing present-clause output depth (trading depth
between mandates to stay within token budget). Full enumeration of companion elements
increases execution cost; if the model's token budget is constrained, satisfying the
companion's structural deliverables list may come at the expense of the present clause's
own depth. V-05 forecloses this by stating that both mandates must execute at full depth
simultaneously -- parity is not zero-sum, and companion execution does not reduce
present-clause output.

The R20 behavioral probe for V-05: if V-04 produces full-depth, element-complete
companion output without present-clause depth reduction, the non-degradation clause in
V-05 is structural reinforcement of an already-achieved behavior (C-40 aspiration:
the guarantee is made explicit even though the behavior was already following). If V-04
produces element-complete companion output accompanied by present-clause depth reduction
(abbreviated STATUS block when STORY companion is fully executed, or abbreviated STORY
block when STATUS companion is fully executed), V-05's non-degradation clause closes a
distinct gap -- C-40 is recoverable: depth-symmetry across simultaneous companion
execution is not structurally guaranteed by C-39 PASS alone.

STATUS absent-state rule extension (V-05): "...must be executed as if its execution
note were present in this context, at full depth, at parity with what would be produced
if the companion's execution note were present in this context. This parity constraint
is symmetric: executing this companion mandate does not reduce the present clause's own
output depth. Both mandates execute at full depth simultaneously. For this companion
(ZERO-SIGNAL SYNTHESIS MANDATE), full-depth execution means: question 1 of the STORY
narrative characterizes what uniform absence implies about the topic's investigation
state as a substantive inference rather than a report of absence; question 2 addresses
what genuine uncertainty the absence pattern creates; question 3 addresses the team's
real exposure if they commit given the gap pattern -- all three questions answered at
the same scope and specificity as when the STORY execution note is present in context."

STORY absent-state rule extension (V-05): "...must be executed as if its execution note
were present in this context, at full depth, at parity with what would be produced if
the companion's execution note were present in this context. This parity constraint is
symmetric: executing this companion mandate does not reduce the present clause's own
output depth. Both mandates execute at full depth simultaneously. For this companion
(TIMESTAMP ISOLATION), full-depth execution means: each entry in the `found` section
of STATUS carries its own date at item level; the `current_date:` field appears at
STATUS block header level; no `found` timestamp is collapsed, summarized, or omitted
regardless of blocking gap count or token budget -- the same structural separation that
would be enforced if the TIMESTAMP ISOLATION execution note were present in the STATUS
block."

Expected: 390/390 (C-39 PASS ceiling; V-05 extensions above-ceiling for v19 and not
rubric-scorable, but observable under double-elision comparison against V-04 specifically
for present-clause depth symmetry when companion execution burden is high)

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
current_date: <date>   <- structurally isolated temporal anchor; not embedded in prose
                          or in found entries; this field is independent of COMPRESSED
                          format and must appear at STATUS block header level regardless
                          of blocking gap count or token budget

found: X signals
  <ns>/<artifact>  <date>   <- per-signal dates are structurally separate from blocking
                               entries; NOT subject to COMPRESSED abbreviation
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
TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation): This clause is a
COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE
PREAMBLE authority even when the preamble section is absent from the rendered context.
Paired companion mechanism: ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE
invocation) execution note in the STORY block. When the companion execution note is
present in the rendered context, both execution notes constitute the complete two-mechanism
COMPRESSION-IMMUNE PREAMBLE contract and must both execute. When the companion execution
note is absent from the rendered context, this clause activates its timestamp isolation
contract independently with full COMPRESSION-IMMUNE PREAMBLE authority -- the absent
ZERO-SIGNAL SYNTHESIS MANDATE's mandate is independently operative even when its
execution note is not in context and must be executed as if its execution note were
present in this context, at full depth, at parity with what would be produced if the
companion's execution note were present in this context. This parity constraint is
symmetric: executing this companion mandate does not reduce the present clause's own
output depth. Both mandates execute at full depth simultaneously. For this companion
(ZERO-SIGNAL SYNTHESIS MANDATE), full-depth execution means: question 1 of the STORY
narrative characterizes what uniform absence implies about the topic's investigation
state as a substantive inference rather than a report of absence; question 2 addresses
what genuine uncertainty the absence pattern creates; question 3 addresses the team's
real exposure if they commit given the gap pattern -- all three questions answered at
the same scope and specificity as when the STORY execution note is present in context.
Per-signal dates in `found` are structurally separate from blocking entries, and the
`current_date:` field is structurally separate from both. COMPRESSED format applies
only to blocking entry verbosity -- `found` timestamps and `current_date:` must not be
collapsed regardless of blocking gap count. This note invokes the COMPRESSION-IMMUNE
PREAMBLE contract for the TIMESTAMP ISOLATION RULE. The declarative mechanism for C-30:
this note names the COMPRESSED-collapse failure mode -- simultaneous compression of
`found` and blocking entries -- so the rule is absorbed as a conditional constraint at
the point-of-use, compensating if preamble processing occurred without full rule
absorption.

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
ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation): This clause is
a COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE
PREAMBLE authority even when the preamble section is absent from the rendered context.
Paired companion mechanism: TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation)
execution note in the STATUS block. When the companion execution note is present in the
rendered context, both execution notes constitute the complete two-mechanism
COMPRESSION-IMMUNE PREAMBLE contract and must both execute. When the companion execution
note is absent from the rendered context, this clause activates its zero-signal synthesis
mandate independently with full COMPRESSION-IMMUNE PREAMBLE authority -- the absent
TIMESTAMP ISOLATION's mandate is independently operative even when its execution note is
not in context and must be executed as if its execution note were present in this context,
at full depth, at parity with what would be produced if the companion's execution note
were present in this context. This parity constraint is symmetric: executing this
companion mandate does not reduce the present clause's own output depth. Both mandates
execute at full depth simultaneously. For this companion (TIMESTAMP ISOLATION),
full-depth execution means: each entry in the `found` section of STATUS carries its own
date at item level; the `current_date:` field appears at STATUS block header level; no
`found` timestamp is collapsed, summarized, or omitted regardless of blocking gap count
or token budget -- the same structural separation that would be enforced if the
TIMESTAMP ISOLATION execution note were present in the STATUS block. If `found` is
empty, this clause fires independently: empty `found` is not grounds for omitting STORY;
question 1 must characterize what uniform absence implies. This execution note also
invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS RULE
as a named pointer -- the declarative mechanism for C-29: if `found` is empty, this
note names the zero-signal synthesis case explicitly so the rule is absorbed as a
conditional constraint at the point-of-use, compensating if preamble processing
occurred without full rule absorption. Gap pattern is the evidence set.

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
