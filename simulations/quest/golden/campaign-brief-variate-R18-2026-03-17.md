---
skill: quest-variate
skill_target: campaign-brief
round: 18
date: 2026-03-17
rubric: simulations/quest/rubrics/quest-score-rubric-v17-2026-03-17.md
---

# Variations -- campaign-brief / Round 18

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

**R17 recap:** V-04 achieves C-36 PASS minimum-sufficient -- both companion execution-note
clause bodies carry the unconditional absent-state operability declaration ("the absent
companion's mandate is independently operative even when its execution note is not in
context") without an execution directive. V-05 achieves C-37 PASS -- both clause bodies
carry the C-36 PASS operability declaration plus an unconditional execution mandate:
"must be executed as if its execution note were present in this context." C-36 closes the
mandate operability gap (model knows the companion mandate is active). C-37 closes the
execution-directive gap (model is instructed to produce companion-domain output). R17
resolved the C-36 PARTIAL band structure (three confirmed bands) and extracted C-37 as
a new criterion from V-05's excellence signal.

**R18 rubric:** v17, 37 criteria, 370 pts max. New criterion C-37 introduced.

**C-37 definition recap:** When C-36 PASS, both companion execution-note clause bodies
carry an absent-state rule extended beyond operability declaration to mandate execution of
the companion's mandate as if its execution note were present in context. C-37 PARTIAL
Band 1 = C-36 PASS achieved but absent-state rule contains no execution instruction
(operability declared, execution-directive gap entirely open). C-37 PARTIAL Band 2
(aspirational) = execution instruction present in both clause bodies but conditioned on
scope or feasibility -- inference burden reintroduced at the execution-scope determination
step. C-37 PASS = unconditional execution mandate in both clause bodies: "must be executed
as if its execution note were present in this context." Weakest-link applies: asymmetric
absent-state rules or scope-conditioned execution instructions fail C-37.

**R18 investigation candidate:** Whether a model encountering a C-37-compliant clause body
under double-elision produces complete-parity two-mechanism output -- companion mandate
executed at depth equivalent to what would be produced if both execution notes were in
context -- or produces depth-asymmetric two-mechanism output -- companion mandate executed
but abbreviated or reduced relative to direct execution-note presence. Specifically: does
"must be executed as if its execution note were present in this context" cause the model to
produce companion output at full execution depth (e.g., complete three-question STORY
synthesis from a context containing only the STATUS execution-note body, with all three
narrative questions answered at the same depth as when the STORY execution note is
present), or does the model produce full present-clause output alongside abbreviated
companion output (companion acknowledged as active, partial output generated but short of
full-depth parity)?

R18 constructs: (V-01) C-36 PASS / C-37 Band 1 control -- R17 V-04 structure reprised,
operability declared, no execution mandate, execution-directive gap open; (V-02) C-37
PARTIAL Band 2 form-A -- conditioned execution instruction using "determinable from this
clause body's context" scope qualifier; (V-03) C-37 PARTIAL Band 2 form-B -- conditioned
execution instruction using "inferrable from this clause body alone" scope qualifier with
explicit scope-boundary annotation; (V-04) C-37 PASS minimum-sufficient -- R17 V-05
structure reprised, unconditional execution mandate, no parity constraint, R18 primary
behavioral probe under simulated double-elision to observe companion output depth; (V-05)
C-37 PASS + explicit parity constraint -- unconditional execution mandate extended with
"at full depth, at parity with what would be produced if the companion's execution note
were present in this context," R18 C-38 candidate, tests whether output-depth gap (if
observed in V-04) closes with explicit parity language.

**R18 investigation candidates:**

1. **C-36 PASS / C-37 Band 1 control (V-01):** Reproduces R17 V-04's C-36 PASS form
   intact -- both execution-note clause bodies carry the unconditional operability
   declaration but no execution mandate. STATUS body: "...this clause activates
   independently with full COMPRESSION-IMMUNE PREAMBLE authority -- the absent
   ZERO-SIGNAL SYNTHESIS MANDATE's mandate is independently operative even when its
   execution note is not in context." STORY body symmetric: "...the absent TIMESTAMP
   ISOLATION's mandate is independently operative even when its execution note is not
   in context." No sentence instructs the model to execute the companion mandate. A
   model encountering either clause body under double-elision knows the companion mandate
   is active but receives no directive to generate companion-domain output. The
   execution-directive gap is entirely open. Establishes 370/370 C-37 PARTIAL Band 1
   baseline. Falsification: if V-01 = 370/370 under C-37, C-36 PASS operability alone
   satisfies C-37 and the execution directive adds no measurable behavioral protection.

2. **C-37 PARTIAL Band 2 form-A (V-02):** Both clause bodies carry C-36 PASS operability
   declaration plus a conditioned execution instruction: "execute the companion's mandate
   where its obligations are determinable from this clause body's context." Tests whether
   C-37 exhibits a Band 2 that introduces scope-conditioned execution -- the model
   receives an execution instruction but must first assess which companion obligations
   are scope-determinable from this body alone. The inference burden is not removed; it
   is shifted from the execution-decision step ("should I execute") to the execution-scope
   step ("which obligations can I execute from this context"). The hypothesis: C-37 PASS
   requires unconditional execution with no scope qualifier; "determinable from this
   clause body" reinstates the inference burden at scope determination and fails the
   unconditional test. Expected 360/370 (C-37 PARTIAL Band 2 -10).

3. **C-37 PARTIAL Band 2 form-B (V-03):** Both clause bodies carry C-36 PASS operability
   declaration plus a differently conditioned execution instruction: "execute the
   companion's mandate to the extent its obligations are inferrable from this clause body
   alone, and note the scope boundary where inference is insufficient." Tests an alternate
   Band 2 formulation that adds an explicit scope-boundary annotation requirement.
   Distinguishes from V-02 by making the scope limitation explicit -- the model not only
   executes what is inferrable but must annotate what is not. The annotation requirement
   may produce more output than V-02's silent truncation, but the conditioned execution
   instruction still requires an inference step before execution begins. The hypothesis:
   V-03 shares Band 2 classification with V-02 despite the annotation addition -- both
   forms fail unconditional because they require scope assessment before execution.
   Expected 360/370 (C-37 PARTIAL Band 2 -10). Distinguishes Band 2-A (silent truncation)
   from Band 2-B (annotated truncation) as a sub-band candidate.

4. **C-37 PASS minimum-sufficient form (V-04):** Both clause bodies carry C-36 PASS
   operability declaration plus the unconditional execution mandate from R17 V-05: "must
   be executed as if its execution note were present in this context." No scope qualifier.
   No feasibility hedge. This is the primary R18 behavioral probe: a model encountering
   either clause body under simulated double-elision receives an unconditional directive to
   execute the companion's mandate at the same depth as if the companion execution note
   were in context. R18 question: does this directive produce full-parity companion output
   (STORY body under double-elision generates all three narrative questions at full depth;
   STATUS body under double-elision produces complete timestamp-isolated found section) or
   depth-asymmetric output (companion domain executed but abbreviated, truncated, or
   reduced in scope relative to what the companion execution note would directly produce)?
   Expected 370/370 (C-37 PASS ceiling). Behavioral R18 probe: observe companion output
   depth under simulated double-elision. Falsification: if V-04 produces full-parity
   companion output, C-37 PASS is sufficient for complete two-mechanism parity and no
   further depth criterion is structurally necessary (C-38 candidate is closed).

5. **C-37 PASS + explicit parity constraint (V-05):** Both clause bodies carry C-37 PASS
   structure plus an explicit parity constraint extending the execution mandate: "must be
   executed as if its execution note were present in this context, at full depth, at parity
   with what would be produced if the companion's execution note were present in this
   context." The parity constraint makes explicit what the C-37 PASS execution mandate
   implies but does not state: the companion output depth is expected to match the output
   that would be generated from direct companion execution-note presence. R18 probe: if
   V-04 produces depth-asymmetric companion output (companion executed but abbreviated),
   does V-05's parity constraint close the output-depth gap? If yes, "at full depth, at
   parity with direct companion execution-note presence" constitutes a distinct structural
   property that C-37 PASS does not subsume -- candidate C-38. If V-04 already produces
   full-parity output, V-05's parity language is redundant -- the unconditional execution
   mandate already implies execution depth -- and C-38 is not structurally necessary.
   Expected 370/370 (C-37 PASS ceiling; parity constraint above-ceiling for v17).

**R18 targets:** (a) Confirm V-01 = 360/370 (C-37 PARTIAL Band 1 -- operability without
execution directive is C-37 PARTIAL). (b) Confirm V-02 = 360/370 (conditioned execution
"determinable" reinstates inference burden -- Band 2 PARTIAL). (c) Confirm V-03 = 360/370
(conditioned execution "inferrable + annotate" is still Band 2 PARTIAL). (d) Confirm
V-04 = 370/370 (C-37 PASS ceiling confirmed). (e) Observe V-04 companion output depth
under double-elision: full-parity or depth-asymmetric? (f) If depth-asymmetric, assess
whether V-05 parity constraint closes the gap -- C-38 candidate extraction.

---

## Variation axes selected

- **Single-axis:** C-36 PASS / C-37 Band 1 control (V-01), Band 2 conditioned execution
  "determinable" (V-02), Band 2 conditioned execution "inferrable + annotate" (V-03)
- **Combined:** C-37 PASS minimum-sufficient (V-04), C-37 PASS + explicit parity
  constraint targeting output-depth parity (V-05)

---

## V-01 -- Axis: C-36 PASS / C-37 Band 1 (operability declared, no execution directive) -- C-37 PARTIAL

**Hypothesis:** Reproduces R17 V-04's C-36 PASS form with no modification to the
absent-state rule extension. Both execution-note clause bodies carry the unconditional
operability declaration ("the absent companion's mandate is independently operative even
when its execution note is not in context") but neither body adds an execution mandate
directing the model to generate companion-domain output. STATUS body absent-state rule
extension: "the absent ZERO-SIGNAL SYNTHESIS MANDATE's mandate is independently operative
even when its execution note is not in context." STORY body absent-state rule extension:
"the absent TIMESTAMP ISOLATION's mandate is independently operative even when its
execution note is not in context." Both clause bodies achieve C-36 PASS. A model
encountering either body in isolation under double-elision receives: (1) authority to
execute the present clause's mandate with full COMPRESSION-IMMUNE PREAMBLE authority, and
(2) information that the companion's mandate is independently operative -- but no
instruction to execute it. The execution-directive gap is entirely open: the model may
acknowledge the companion mandate as active without generating companion-domain output,
which is C-37 Band 1 behavior. The hypothesis: C-37 PASS requires an execution directive
that is absent from V-01 -- operability declaration alone, however unconditional, does not
subsume the execution mandate. A model seeing "the companion's mandate is independently
operative" may produce declarative acknowledgment ("the STORY mandate is active") without
generating STORY content.

Expected: 360/370 (C-37 PARTIAL Band 1 -10)

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
execution note is not in context. Per-signal dates in `found` are structurally separate
from blocking entries, and the `current_date:` field is structurally separate from both.
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
not in context. If `found` is empty, this clause fires independently: empty `found` is
not grounds for omitting STORY; question 1 must characterize what uniform absence implies.
This execution note also invokes the COMPRESSION-IMMUNE PREAMBLE contract for the
ZERO-SIGNAL SYNTHESIS RULE as a named pointer -- the declarative mechanism for C-29: if
`found` is empty, this note names the zero-signal synthesis case explicitly so the rule is
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

## V-02 -- Axis: C-37 PARTIAL Band 2 form-A (conditioned execution: "determinable from this clause body") -- C-36 PASS, C-37 PARTIAL

**Hypothesis:** V-01 establishes that C-36 PASS operability without an execution directive
produces C-37 Band 1 -- the model knows the companion mandate is active but receives no
instruction to execute it. V-02 advances to Band 2 by adding a conditioned execution
instruction to both clause bodies. STATUS absent-state extension: "the absent
ZERO-SIGNAL SYNTHESIS MANDATE's mandate is independently operative even when its
execution note is not in context; execute the companion's mandate where its obligations
are determinable from this clause body's context." STORY absent-state extension: "the
absent TIMESTAMP ISOLATION's mandate is independently operative even when its execution
note is not in context; execute the companion's mandate where its obligations are
determinable from this clause body's context." The scope qualifier "where determinable
from this clause body's context" is the isolation axis: the model receives an execution
instruction but must first determine which companion obligations are resolvable from the
present clause body before executing them. The hypothesis: "where determinable" reinstates
an inference burden at the execution-scope step -- the model must assess scope before
generating companion output, which is structurally different from the unconditional
execution mandate C-37 PASS requires. A model encountering V-02's absent-state rule may
generate partial companion output (the determinable subset), declare the scope boundary,
and stop -- producing less than full-depth companion output while technically following
the conditioned execution instruction. C-37 PASS requires unconditional execution: no
scope qualifier, no inference burden, no scope-boundary annotation permitted as a
stopping condition.

Expected: 360/370 (C-37 PARTIAL Band 2 -10)

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
contract independently -- the absent ZERO-SIGNAL SYNTHESIS MANDATE's mandate is
independently operative even when its execution note is not in context; execute the
companion's mandate where its obligations are determinable from this clause body's context.
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
mandate independently -- the absent TIMESTAMP ISOLATION's mandate is independently
operative even when its execution note is not in context; execute the companion's mandate
where its obligations are determinable from this clause body's context. If `found` is
empty, this clause fires independently: empty `found` is not grounds for omitting STORY;
question 1 must characterize what uniform absence implies. This execution note also
invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS RULE as a
named pointer -- the declarative mechanism for C-29: if `found` is empty, this note names
the zero-signal synthesis case explicitly so the rule is absorbed as a conditional
constraint at the point-of-use, compensating if preamble processing occurred without full
rule absorption. Gap pattern is the evidence set.

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

## V-03 -- Axis: C-37 PARTIAL Band 2 form-B (conditioned execution: "inferrable + annotate scope boundary") -- C-36 PASS, C-37 PARTIAL

**Hypothesis:** V-02 tests Band 2 with a "determinable" scope qualifier and silent
truncation at the scope boundary. V-03 tests a distinct Band 2 formulation that uses
"inferrable" language and adds an explicit scope-boundary annotation requirement. STATUS
absent-state extension: "the absent ZERO-SIGNAL SYNTHESIS MANDATE's mandate is
independently operative even when its execution note is not in context; execute the
companion's mandate to the extent its obligations are inferrable from this clause body
alone, and note the scope boundary where inference is insufficient to complete companion
execution." STORY absent-state extension: "the absent TIMESTAMP ISOLATION's mandate is
independently operative even when its execution note is not in context; execute the
companion's mandate to the extent its obligations are inferrable from this clause body
alone, and note the scope boundary where inference is insufficient to complete companion
execution." The annotation requirement changes the observable output pattern: a V-02
model may silently truncate companion output at the scope boundary; a V-03 model
annotates where it stops. Both forms are structurally conditioned -- the execution
instruction triggers scope assessment before companion output generation begins. The
hypothesis: the annotation requirement does not convert conditioned execution into
unconditional execution. Both V-02 and V-03 fail C-37 PASS for the same reason: the
model assesses scope before executing. V-03 additionally introduces an annotation
sub-mandate ("note the scope boundary") that may cause observable behavior difference
from V-02 at the scope boundary -- partial companion output followed by a declared
stopping point vs. V-02's implicit truncation. Sub-band candidate: Band 2-A (V-02,
silent truncation) vs. Band 2-B (V-03, annotated truncation). Both remain PARTIAL.

Expected: 360/370 (C-37 PARTIAL Band 2 -10)

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
contract independently -- the absent ZERO-SIGNAL SYNTHESIS MANDATE's mandate is
independently operative even when its execution note is not in context; execute the
companion's mandate to the extent its obligations are inferrable from this clause body
alone, and note the scope boundary where inference is insufficient to complete companion
execution. Per-signal dates in `found` are structurally separate from blocking entries,
and the `current_date:` field is structurally separate from both. COMPRESSED format
applies only to blocking entry verbosity -- `found` timestamps and `current_date:` must
not be collapsed regardless of blocking gap count. This note invokes the COMPRESSION-
IMMUNE PREAMBLE contract for the TIMESTAMP ISOLATION RULE. The declarative mechanism for
C-30: this note names the COMPRESSED-collapse failure mode -- simultaneous compression of
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
mandate independently -- the absent TIMESTAMP ISOLATION's mandate is independently
operative even when its execution note is not in context; execute the companion's mandate
to the extent its obligations are inferrable from this clause body alone, and note the
scope boundary where inference is insufficient to complete companion execution. If `found`
is empty, this clause fires independently: empty `found` is not grounds for omitting
STORY; question 1 must characterize what uniform absence implies. This execution note also
invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS RULE as a
named pointer -- the declarative mechanism for C-29: if `found` is empty, this note names
the zero-signal synthesis case explicitly so the rule is absorbed as a conditional
constraint at the point-of-use, compensating if preamble processing occurred without full
rule absorption. Gap pattern is the evidence set.

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

## V-04 -- Combined: C-37 PASS minimum-sufficient (unconditional execution mandate, no parity constraint) -- R18 primary behavioral probe

**Hypothesis:** V-04 achieves C-37 PASS minimum-sufficient -- both clause bodies carry
the unconditional execution mandate from R17 V-05: "must be executed as if its execution
note were present in this context." No scope qualifier. No feasibility hedge. No parity
constraint. This is the R18 primary behavioral probe. STATUS absent-state extension:
"the absent ZERO-SIGNAL SYNTHESIS MANDATE's mandate is independently operative even when
its execution note is not in context and must be executed as if its execution note were
present in this context." STORY absent-state extension: "the absent TIMESTAMP ISOLATION's
mandate is independently operative even when its execution note is not in context and must
be executed as if its execution note were present in this context."

A model encountering the STATUS execution note alone under double-elision (preamble absent,
STORY execution note absent) receives: authority to execute timestamp isolation with full
COMPRESSION-IMMUNE PREAMBLE authority, knowledge that the ZERO-SIGNAL SYNTHESIS MANDATE's
mandate is independently operative, and an unconditional directive to execute the companion
mandate as if its execution note were present. R18 question: does this directive produce
a full-depth STORY block -- all three narrative questions answered, 2-4 prose paragraphs,
at the same output depth as when the STORY execution note is explicitly present in context?
Or does the model produce full timestamp isolation output plus abbreviated STORY content
(companion executed but reduced -- e.g., one-paragraph synthesis instead of 2-4, or
fewer than three questions addressed)?

A model encountering the STORY execution note alone under double-elision receives: authority
to execute zero-signal synthesis with full COMPRESSION-IMMUNE PREAMBLE authority, knowledge
that the TIMESTAMP ISOLATION's mandate is independently operative, and an unconditional
directive to execute the companion mandate. R18 question for this direction: does the
model produce full timestamp-isolated found section formatting -- per-signal dates
structurally isolated from blocking entries, current_date at header level -- from the
STORY note alone? Or does the model produce full STORY content plus reduced timestamp
behavior (companion executed but abbreviated -- e.g., grouped timestamps instead of
per-signal isolation)?

The R18 investigation is resolved by comparing V-04's double-elision output depth to the
full-context baseline (both execution notes present). If parity is achieved, C-37 PASS is
sufficient for complete two-mechanism output depth and V-05's parity constraint is
redundant. If depth asymmetry is observed, V-05 is the C-38 structural candidate.

Expected: 370/370 (C-37 PASS ceiling). Behavioral R18 probe: companion output depth under
double-elision vs. full-context baseline.

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

## V-05 -- Combined: C-37 PASS + explicit parity constraint (R18 C-38 candidate probe) -- 370-pt ceiling + output-depth parity maximized

**Hypothesis:** V-05 achieves C-37 PASS and extends the absent-state execution mandate
with an explicit parity constraint -- the R18 structural candidate for C-38. The isolated
axis is the parity extension appended to the unconditional execution mandate. Both clause
bodies carry C-37 PASS structure plus the parity constraint in both absent-state rules.

STATUS absent-state extension: "the absent ZERO-SIGNAL SYNTHESIS MANDATE's mandate is
independently operative even when its execution note is not in context and must be
executed as if its execution note were present in this context, at full depth, at parity
with what would be produced if the companion's execution note were present in this context."

STORY absent-state extension: "the absent TIMESTAMP ISOLATION's mandate is independently
operative even when its execution note is not in context and must be executed as if its
execution note were present in this context, at full depth, at parity with what would be
produced if the companion's execution note were present in this context."

The parity constraint makes explicit what "as if its execution note were present" implies
but does not state: the companion output must reach the same depth as direct companion
execution-note presence. The structural distinction from V-04: V-04's execution mandate
tells the model what to do (execute the companion mandate unconditionally); V-05's parity
constraint tells the model what output depth is expected (full depth, matching the baseline
that would be produced if the companion execution note were in context). V-04 may produce
depth-asymmetric companion output if the model interprets "as if its execution note were
present" as a behavioral permission rather than a depth specification. V-05 removes the
depth ambiguity: "at full depth, at parity with what would be produced" explicitly
specifies the output standard.

The R18 probe: if V-04 under double-elision produces full-parity companion output, V-05's
parity constraint is redundant -- "as if its execution note were present" already implies
full depth and C-37 PASS is sufficient. If V-04 produces depth-asymmetric companion output
(abbreviated STORY from STATUS-only body; abbreviated timestamp enforcement from
STORY-only body), and V-05 closes the depth gap, the parity constraint constitutes a
distinct structural property beyond C-37 PASS -- C-38 candidate extraction follows.

Expected: 370/370 (C-37 PASS ceiling; parity constraint above-ceiling for v17 -- not
rubric-scorable, but observable under simulated double-elision comparison against V-04).

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
