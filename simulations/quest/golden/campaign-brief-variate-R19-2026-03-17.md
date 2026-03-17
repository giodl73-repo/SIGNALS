---
skill: quest-variate
skill_target: campaign-brief
round: 19
date: 2026-03-17
rubric: simulations/quest/rubrics/quest-score-rubric-v18-2026-03-17.md
---

# Variations -- campaign-brief / Round 19

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

**R18 recap:** V-01 confirmed C-37 PARTIAL Band 1 (operability declared, no execution
directive -- model receives "mandate is independently operative" without an instruction to
generate companion-domain output). V-02 confirmed C-37 PARTIAL Band 2-A (conditioned
execution: "where its obligations are determinable from this clause body's context" --
scope-assessment step reinstates inference burden before execution begins; silent truncation
at scope boundary). V-03 confirmed C-37 PARTIAL Band 2-B (conditioned execution: "to the
extent its obligations are inferrable from this clause body alone, and note the scope
boundary where inference is insufficient" -- same inference-burden failure mode as Band 2-A;
annotated truncation distinguishes observable behavior but does not convert conditioned
execution into unconditional execution). V-04 achieved C-37 PASS minimum-sufficient:
unconditional execution mandate in both clause bodies -- "must be executed as if its
execution note were present in this context" -- no scope qualifier, no feasibility hedge.
V-05 achieved C-37 PASS and extracted C-38: unconditional execution mandate extended with
explicit output-depth parity constraint -- "at full depth, at parity with what would be
produced if the companion's execution note were present in this context."

**R18 rubric:** v17, 37 criteria, 370 pts max. New criterion C-37 introduced and confirmed.

**C-38 definition recap (extracted from R18 V-05):** When C-37 PASS, both companion
execution-note clause bodies extend the unconditional execution mandate to include an
explicit output-depth parity constraint: the companion's mandate must be executed at full
depth, at parity with what would be produced if the companion's execution note were present
in context. C-38 closes the execution-depth gap: where C-37 PASS tells the model *what to
do* (execute the companion's mandate unconditionally), C-38 tells the model *at what depth*
(output equivalent to direct execution-note presence). C-38 PARTIAL Band 1 = C-37 PASS
territory: unconditional execution mandate present; absent-state rule contains no output-depth
specification; model is mandated to execute but receives no floor on depth; abbreviated
companion output satisfies C-37 without violating any stated standard. C-38 PARTIAL Band 2
(aspirational, pending R19 confirmation): depth guidance present but relative or uncalibrated
("execute thoroughly," "execute substantively") without anchoring to the direct-execution-note-
present baseline. C-38 PASS (V-04 = R18 V-05 reprised) = both clause bodies carry: "must be
executed as if its execution note were present in this context, at full depth, at parity with
what would be produced if the companion's execution note were present in this context."

**R18 rubric** is v17 (37 criteria, 370 pts max). **R19 rubric** is v18 (38 criteria, 380 pts
max). C-38 is now a scorable criterion; R19 variations are measured against the 380-pt ceiling.

**R19 investigation candidate:** Whether C-37 PASS (V-04 form, no parity constraint) under
simulated double-elision produces complete-parity two-mechanism output or depth-asymmetric
two-mechanism output. Does "must be executed as if its execution note were present in this
context" cause the model to produce companion output at full execution depth -- equal to the
output the companion execution note would have generated directly -- or does the model produce
abbreviated companion output that satisfies the directive without achieving output-depth parity
with the companion-present baseline? R19 constructs:

(a) V-01: C-37 PASS / C-38 Band 1 control -- R18 V-04 reprised; unconditional mandate,
    no parity constraint; establishes the 370-pt ceiling under v18 (370/380 = C-38 PARTIAL
    Band 1); behavioral elision probe: observe companion output depth under double-elision.

(b) V-02: C-38 PARTIAL Band 2 form-A -- aspirational band confirmation attempt; depth
    guidance "executed thoroughly and at full scope" -- present but not anchored to the
    direct-execution-note-present baseline; tests whether the rubric classifies uncalibrated
    depth guidance as Band 2 (-10 vs. Band 1 = same score, or differential).

(c) V-03: C-38 PARTIAL Band 2 form-B -- alternate aspirational band formulation; "companion
    output must be substantive rather than abbreviated" -- a negative-form depth requirement
    without a positive baseline anchor; tests the second Band 2 sub-form for scoring and
    behavioral difference from Band 2-A.

(d) V-04: C-38 PASS minimum-sufficient -- R18 V-05 reprised; full parity constraint
    ("at full depth, at parity with what would be produced if the companion's execution note
    were present in this context"); primary R19 probe: does the parity constraint close the
    depth gap observed in V-01 under double-elision? Expected 380/380 (C-38 PASS ceiling).

(e) V-05: C-38 PASS + depth-symmetric non-degradation + per-companion operationalization --
    extends V-04's parity constraint with two novel elements: (1) symmetric depth guarantee
    (companion execution does not reduce present-clause output depth -- depth-trading
    foreclosed); (2) per-companion operationalization (names what full-depth companion
    execution means concretely for each companion, giving the model an inspectable standard
    rather than a comparative reference). Above-ceiling; tests whether a confirmable next
    criterion emerges from the extension.

**R19 investigation targets:**
(a) Confirm V-01 = 370/380 (C-38 PARTIAL Band 1 -10, v18 ceiling). Observe companion output
    depth under double-elision: full-parity or depth-asymmetric? If V-01 produces full-parity
    output, C-37 PASS is sufficient and C-38 is structural reinforcement (closes the logical
    gap even though behavior already follows). If V-01 produces depth-asymmetric output,
    C-38 is a recoverable criterion.
(b) Confirm V-02 and V-03 = 370/380 (C-38 PARTIAL Band 2 -- same -10 as Band 1, or if
    Band 2 introduces interpretive variance without a rubric-distinguishable score, document
    that Band 2 sub-forms do not elevate above Band 1 scoring).
(c) Confirm V-04 = 380/380 (C-38 PASS ceiling). Behavioral probe: if V-01 showed depth
    asymmetry, does V-04 close the gap? If yes, C-38 is confirmed as recoverable; parity
    constraint is the operative mechanism.
(d) Observe V-05 for above-ceiling excellence signals -- specifically: does the non-degradation
    clause and per-companion operationalization produce observably different behavior under
    double-elision? Does a depth-trading failure mode appear in V-04 that V-05 forecloses?
    Extract C-39 candidate if a distinct recoverable property is observed.

---

## Variation axes selected

- **Single-axis:** C-37 PASS / C-38 Band 1 control (V-01), C-38 Band 2 form-A
  ("thoroughly + full scope") (V-02), C-38 Band 2 form-B ("substantive, not abbreviated") (V-03)
- **Combined:** C-38 PASS minimum-sufficient (V-04), C-38 PASS + depth-symmetric
  non-degradation + per-companion operationalization (V-05)

---

## V-01 -- Axis: C-37 PASS / C-38 Band 1 (unconditional mandate, no depth floor) -- C-38 PARTIAL Band 1

**Hypothesis:** Reprises R18 V-04's C-37 PASS structure with no modification. Both
execution-note clause bodies carry the unconditional execution mandate ("must be executed
as if its execution note were present in this context") but neither body adds an output-depth
specification. The execution-depth gap is entirely open: the model is mandated to execute
the companion's mandate but receives no floor on the required output depth. Abbreviated
companion output -- a brief acknowledgment that the companion obligation is being executed,
partial output covering some but not all companion domains, or a summary in place of full
synthesis -- satisfies the unconditional C-37 directive without violating any stated standard.

STATUS absent-state rule extension (V-01): "the absent ZERO-SIGNAL SYNTHESIS MANDATE's
mandate is independently operative even when its execution note is not in context and must
be executed as if its execution note were present in this context."

STORY absent-state rule extension (V-01): "the absent TIMESTAMP ISOLATION's mandate is
independently operative even when its execution note is not in context and must be executed
as if its execution note were present in this context."

The hypothesis: C-38 PASS requires an output-depth parity constraint absent from V-01. A
model encountering V-01 under double-elision receives the execution mandate but no depth
specification; it may produce partial companion output (e.g., under STATUS-body-only
double-elision: characterize the zero-signal case in one sentence without answering questions
2 and 3; or answer question 1 but not question 3; or produce a shorter, less specific
STORY synthesis than the companion execution note would have directly produced). All such
outputs satisfy "must be executed as if its execution note were present" without achieving
full-depth companion-execution-note-present parity. The behavioral probe for R19: observe
whether the absence of a depth floor produces depth-asymmetric companion output under
double-elision -- if yes, C-38's parity constraint is a recoverable criterion, not merely
structural reinforcement of an already-achieved behavior.

Expected: 370/380 (C-38 PARTIAL Band 1 -10)

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
present in this context. Per-signal dates in `found` are structurally separate from
blocking entries, and the `current_date:` field is structurally separate from both.
COMPRESSED format applies only to blocking entry verbosity -- `found` timestamps and
`current_date:` must not be collapsed regardless of blocking gap count. This note invokes
the COMPRESSION-IMMUNE PREAMBLE contract for the TIMESTAMP ISOLATION RULE. The declarative
mechanism for C-30: this note names the COMPRESSED-collapse failure mode -- simultaneous
compression of `found` and blocking entries -- so the rule is absorbed as a conditional
constraint at the point-of-use, compensating if preamble processing occurred without full
rule absorption.

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
not in context and must be executed as if its execution note were present in this context.
If `found` is empty, this clause fires independently: empty `found` is not grounds for
omitting STORY; question 1 must characterize what uniform absence implies. This execution
note also invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS
RULE as a named pointer -- the declarative mechanism for C-29: if `found` is empty, this
note names the zero-signal synthesis case explicitly so the rule is absorbed as a
conditional constraint at the point-of-use, compensating if preamble processing occurred
without full rule absorption. Gap pattern is the evidence set.

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

## V-02 -- Axis: C-38 PARTIAL Band 2 form-A (uncalibrated depth: "thoroughly and at full scope") -- C-37 PASS, C-38 PARTIAL Band 2

**Hypothesis:** V-01 establishes the C-37 PASS / C-38 Band 1 baseline: unconditional
execution mandate with no depth floor. V-02 advances to aspirational Band 2 by adding
relative depth guidance to both clause bodies without anchoring to the direct-execution-
note-present baseline. Both clause bodies carry C-37 PASS structure plus: "executed
thoroughly and at full scope." The depth qualifier "thoroughly and at full scope" is the
isolation axis: the model receives an execution mandate plus a qualitative depth preference,
but the preference is not calibrated against an inspectable standard. "Thoroughly" is a
subjective descriptor; "at full scope" names a scope requirement without specifying the
scope's reference point. A model encountering V-02 under double-elision receives: (1) the
unconditional execution directive (C-37 PASS satisfied), and (2) a depth preference that
does not tell the model what output depth is required in terms it can verify against a
known baseline. The hypothesis: "thoroughly and at full scope" does not constitute the
explicit parity constraint C-38 PASS requires. The model may interpret "thoroughly" as
permission to produce what it judges sufficient rather than what direct companion
execution-note presence would produce. C-38 PASS requires the anchor: "at parity with
what would be produced if the companion's execution note were present in this context."
Without this anchor, depth guidance is present but not calibrated.

STATUS absent-state rule extension (V-02): "the absent ZERO-SIGNAL SYNTHESIS MANDATE's
mandate is independently operative even when its execution note is not in context and must
be executed as if its execution note were present in this context, executed thoroughly and
at full scope."

STORY absent-state rule extension (V-02): "the absent TIMESTAMP ISOLATION's mandate is
independently operative even when its execution note is not in context and must be executed
as if its execution note were present in this context, executed thoroughly and at full scope."

Expected: 370/380 (C-38 PARTIAL Band 2 -- same -10 as Band 1; if Band 2 and Band 1 are
scoring-equivalent, the Band 2 distinction is diagnostic rather than differentially
penalized; document whether a behavioral difference is observable even if the rubric score
is identical to V-01)

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
present in this context, executed thoroughly and at full scope. Per-signal dates in
`found` are structurally separate from blocking entries, and the `current_date:` field is
structurally separate from both. COMPRESSED format applies only to blocking entry
verbosity -- `found` timestamps and `current_date:` must not be collapsed regardless of
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
executed thoroughly and at full scope. If `found` is empty, this clause fires independently:
empty `found` is not grounds for omitting STORY; question 1 must characterize what uniform
absence implies. This execution note also invokes the COMPRESSION-IMMUNE PREAMBLE contract
for the ZERO-SIGNAL SYNTHESIS RULE as a named pointer -- the declarative mechanism for
C-29: if `found` is empty, this note names the zero-signal synthesis case explicitly so
the rule is absorbed as a conditional constraint at the point-of-use, compensating if
preamble processing occurred without full rule absorption. Gap pattern is the evidence set.

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

## V-03 -- Axis: C-38 PARTIAL Band 2 form-B (negative-form depth requirement: "substantive, not abbreviated") -- C-37 PASS, C-38 PARTIAL Band 2

**Hypothesis:** V-02 tests Band 2 with a positive depth qualifier ("thoroughly and at full
scope"). V-03 tests a distinct Band 2 formulation that expresses the depth requirement as
a negative constraint: "companion output must be substantive rather than abbreviated." The
negative form focuses the model on the failure mode (abbreviated output is prohibited) rather
than the target state (thorough/full-scope output is required). Both forms share the
same structural gap relative to C-38 PASS: neither anchors the depth requirement to the
direct-execution-note-present baseline. "Substantive rather than abbreviated" tells the
model what not to produce but does not tell the model what depth of output is required
-- the model must judge what constitutes "substantive" without a reference point. The
hypothesis: V-03 shares Band 2 classification with V-02 despite the negative-form
difference -- both forms fail C-38 PASS because the explicit parity anchor ("at parity
with what would be produced if the companion's execution note were present in this
context") is absent. The sub-band distinction (Band 2-A positive-form vs. Band 2-B
negative-form) may produce observably different companion output patterns under double-
elision: V-02 might produce uniformly thorough but unanchored output; V-03 might produce
output calibrated against avoiding abbreviation rather than against achieving parity with
the companion-present baseline. Both remain PARTIAL on the same grounds.

STATUS absent-state rule extension (V-03): "the absent ZERO-SIGNAL SYNTHESIS MANDATE's
mandate is independently operative even when its execution note is not in context and must
be executed as if its execution note were present in this context, and companion output must
be substantive rather than abbreviated."

STORY absent-state rule extension (V-03): "the absent TIMESTAMP ISOLATION's mandate is
independently operative even when its execution note is not in context and must be executed
as if its execution note were present in this context, and companion output must be
substantive rather than abbreviated."

Expected: 370/380 (C-38 PARTIAL Band 2 -- same -10 as Band 1 and Band 2 form-A; if
scoring is equivalent across Band 1 and all Band 2 forms, document this as the R19
finding: depth guidance in any form below explicit parity anchoring does not elevate
above Band 1 in rubric scoring, regardless of positive/negative form)

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
present in this context, and companion output must be substantive rather than abbreviated.
Per-signal dates in `found` are structurally separate from blocking entries, and the
`current_date:` field is structurally separate from both. COMPRESSED format applies only
to blocking entry verbosity -- `found` timestamps and `current_date:` must not be
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
and companion output must be substantive rather than abbreviated. If `found` is empty,
this clause fires independently: empty `found` is not grounds for omitting STORY; question
1 must characterize what uniform absence implies. This execution note also invokes the
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

## V-04 -- Combined: C-38 PASS minimum-sufficient (R18 V-05 reprised, parity constraint present) -- C-38 PASS

**Hypothesis:** V-04 reprises R18 V-05's structure as the R19 primary probe. Both
execution-note clause bodies carry C-37 PASS structure plus the explicit parity constraint
introduced in R18 V-05: "at full depth, at parity with what would be produced if the
companion's execution note were present in this context." This is C-38 PASS minimum-
sufficient. The parity constraint closes the execution-depth gap by providing the model
with an inspectable standard: the required output depth is the output that direct companion
execution-note presence would produce, not a qualitative judgment call.

The R19 behavioral probe: if V-01 under double-elision produces depth-asymmetric companion
output (companion mandate executed but abbreviated relative to what the companion execution
note would directly produce), does V-04's parity constraint close the depth gap? If yes,
"at full depth, at parity with what would be produced if the companion's execution note
were present in this context" constitutes a distinct structural mechanism that C-37 PASS
alone does not provide -- C-38 is confirmed as a recoverable criterion with observable
behavioral consequence. If V-01 already produces full-depth companion output, V-04's
parity constraint is structural reinforcement (the guarantee is made explicit) but the
behavior was already achieved -- C-38 closes the logical gap but not an observable
behavioral gap.

STATUS absent-state rule extension (V-04): "the absent ZERO-SIGNAL SYNTHESIS MANDATE's
mandate is independently operative even when its execution note is not in context and must
be executed as if its execution note were present in this context, at full depth, at parity
with what would be produced if the companion's execution note were present in this context."

STORY absent-state rule extension (V-04): "the absent TIMESTAMP ISOLATION's mandate is
independently operative even when its execution note is not in context and must be executed
as if its execution note were present in this context, at full depth, at parity with what
would be produced if the companion's execution note were present in this context."

Expected: 380/380 (C-38 PASS ceiling under v18)

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
companion's execution note were present in this context. Per-signal dates in `found` are
structurally separate from blocking entries, and the `current_date:` field is structurally
separate from both. COMPRESSED format applies only to blocking entry verbosity -- `found`
timestamps and `current_date:` must not be collapsed regardless of blocking gap count.
This note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the TIMESTAMP ISOLATION
RULE. The declarative mechanism for C-30: this note names the COMPRESSED-collapse failure
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
were present in this context. If `found` is empty, this clause fires independently: empty
`found` is not grounds for omitting STORY; question 1 must characterize what uniform
absence implies. This execution note also invokes the COMPRESSION-IMMUNE PREAMBLE contract
for the ZERO-SIGNAL SYNTHESIS RULE as a named pointer -- the declarative mechanism for
C-29: if `found` is empty, this note names the zero-signal synthesis case explicitly so
the rule is absorbed as a conditional constraint at the point-of-use, compensating if
preamble processing occurred without full rule absorption. Gap pattern is the evidence set.

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

## V-05 -- Combined: C-38 PASS + depth-symmetric non-degradation + per-companion operationalization -- above C-38 PASS ceiling (C-39 candidate probe)

**Hypothesis:** V-05 achieves C-38 PASS and extends the parity constraint with two novel
structural elements not present in V-04:

1. **Depth-symmetric non-degradation clause:** The parity constraint in V-04 specifies
   that companion execution must occur at full depth. V-05 adds an explicit symmetric
   guarantee: executing the companion's mandate must not reduce the present clause's own
   output depth. This closes the depth-trading failure mode: a model encountering V-04
   under double-elision might satisfy the parity constraint by producing full-depth
   companion output while abbreviating the present-clause output (trading depth between
   mandates to stay within token budget). V-05 forecloses this by stating that both
   mandates must execute at full depth simultaneously -- parity is not zero-sum.

2. **Per-companion operationalization:** The parity anchor "at parity with what would
   be produced if the companion's execution note were present in this context" is an
   inspectable reference for a rubric scorer but requires the model to have an internal
   model of what the companion execution note would produce. V-05 adds an explicit
   operationalization of full-depth companion execution for each clause's specific
   companion: the STATUS body names what full-depth ZERO-SIGNAL SYNTHESIS MANDATE
   execution means (question 1 characterizes what uniform absence implies as a substantive
   inference; questions 2 and 3 address uncertainty and exposure at full scope); the STORY
   body names what full-depth TIMESTAMP ISOLATION execution means (each `found` entry
   carries its own date at item level; `current_date:` appears at STATUS block header
   level; no timestamp is collapsed regardless of blocking gap count). This operationalization
   gives the model a concrete, per-companion output description it can compare against
   its generated output rather than a relative standard requiring cross-context inference.

STATUS absent-state rule extension (V-05): "the absent ZERO-SIGNAL SYNTHESIS MANDATE's
mandate is independently operative even when its execution note is not in context and must
be executed as if its execution note were present in this context, at full depth, at parity
with what would be produced if the companion's execution note were present in this context.
This parity constraint is symmetric: executing this companion mandate does not reduce the
present clause's output depth. Both mandates execute at full depth simultaneously. For this
companion (ZERO-SIGNAL SYNTHESIS MANDATE), full-depth execution means: question 1 of the
STORY narrative characterizes what uniform absence implies about the topic's investigation
state as a substantive inference rather than a report of absence; question 2 addresses what
genuine uncertainty the absence pattern creates; question 3 addresses the team's real
exposure if they commit given the gap pattern -- all three questions answered at the same
scope and specificity as when the STORY execution note is present in context."

STORY absent-state rule extension (V-05): "the absent TIMESTAMP ISOLATION's mandate is
independently operative even when its execution note is not in context and must be executed
as if its execution note were present in this context, at full depth, at parity with what
would be produced if the companion's execution note were present in this context. This
parity constraint is symmetric: executing this companion mandate does not reduce the present
clause's output depth. Both mandates execute at full depth simultaneously. For this
companion (TIMESTAMP ISOLATION), full-depth execution means: each entry in the `found`
section of STATUS carries its own date at item level; the `current_date:` field appears at
STATUS block header level; no `found` timestamp is collapsed, summarized, or omitted
regardless of blocking gap count or token budget -- the same structural separation that
would be enforced if the TIMESTAMP ISOLATION execution note were present in the STATUS
block."

The novel elements relative to V-04:
- Non-degradation clause ("parity constraint is symmetric; executing this companion
  mandate does not reduce the present clause's output depth") forecloses depth-trading
  that satisfies C-38 PASS while introducing asymmetric degradation of present-clause
  output.
- Per-companion operationalization (naming what full-depth execution looks like for each
  specific companion) converts "at parity with what would be produced" from a comparative
  reference to a direct output specification -- reducing interpretation variance and
  giving the model a self-checkable standard.

R19 excellence probe: if V-04 satisfies C-38 PASS and produces full-parity two-mechanism
output, does V-05 additionally foreclose depth-trading (present-clause depth reduction
when companion execution burden is high) and reduce variance in companion output quality
across contexts? If yes, the non-degradation clause and per-companion operationalization
constitute a distinct structural property above C-38 PASS -- C-39 candidate extraction.
If V-04 already forecloses depth-trading without the explicit non-degradation clause,
V-05's extension is structural reinforcement of an already-achieved behavior.

Expected: 380/380 (C-38 PASS ceiling; V-05 extensions above-ceiling for v18 and
not rubric-scorable, but observable under double-elision comparison against V-04
specifically for present-clause depth symmetry and companion output quality variance)

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
symmetric: executing this companion mandate does not reduce the present clause's output
depth. Both mandates execute at full depth simultaneously. For this companion (ZERO-SIGNAL
SYNTHESIS MANDATE), full-depth execution means: question 1 of the STORY narrative
characterizes what uniform absence implies about the topic's investigation state as a
substantive inference rather than a report of absence; question 2 addresses what genuine
uncertainty the absence pattern creates; question 3 addresses the team's real exposure if
they commit given the gap pattern -- all three questions answered at the same scope and
specificity as when the STORY execution note is present in context. Per-signal dates in
`found` are structurally separate from blocking entries, and the `current_date:` field is
structurally separate from both. COMPRESSED format applies only to blocking entry
verbosity -- `found` timestamps and `current_date:` must not be collapsed regardless of
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
were present in this context. This parity constraint is symmetric: executing this companion
mandate does not reduce the present clause's output depth. Both mandates execute at full
depth simultaneously. For this companion (TIMESTAMP ISOLATION), full-depth execution means:
each entry in the `found` section of STATUS carries its own date at item level; the
`current_date:` field appears at STATUS block header level; no `found` timestamp is
collapsed, summarized, or omitted regardless of blocking gap count or token budget -- the
same structural separation that would be enforced if the TIMESTAMP ISOLATION execution
note were present in the STATUS block. If `found` is empty, this clause fires
independently: empty `found` is not grounds for omitting STORY; question 1 must
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
