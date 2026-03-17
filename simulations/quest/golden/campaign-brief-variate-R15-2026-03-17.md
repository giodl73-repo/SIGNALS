---
skill: quest-variate
skill_target: campaign-brief
round: 15
date: 2026-03-17
rubric: simulations/quest/rubrics/campaign-brief-rubric-v14-2026-03-16.md
---

# Variations -- campaign-brief / Round 15

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

**R14 recap:** V-04 and V-05 both scored 330/330 (C-33 PASS ceiling under v13). C-33
PASS confirmed: both companion execution-note clause headers carry the structural-
membership parenthetical `(COMPRESSION-IMMUNE PREAMBLE invocation)`, creating exact-
match designation symmetry between preamble forward-references and target clause headers.
V-01/V-02/V-03 confirmed 320/330 (C-33 PARTIAL -- bare headers insufficient; weakest-
link behavior confirmed symmetric across both companion mechanism domains). R14 V-05
exhibited an excellence signal extracted as C-34: companion execution-note clause bodies
open with (1) an explicit structural-membership statement naming the clause as a
COMPRESSION-IMMUNE PREAMBLE member and (2) a preamble-independence instruction declaring
the clause executes even when the preamble section is absent. Together these extend self-
announcing from the header (C-33) into the body, targeting partial double-elision
recovery when preamble + other companion are both absent and only one clause body
survives.

**R15 rubric:** v14, 34 criteria, 340 pts max. New criterion C-34 introduced.

**C-34 definition recap:** When C-33 PASS, companion execution-note clause bodies open
with two components: (1) an explicit structural-membership statement naming the clause
as a COMPRESSION-IMMUNE PREAMBLE member from within the clause body itself, and (2) a
preamble-independence instruction declaring that the clause executes even when the
preamble section is absent from the rendered context. Together these enable partial
double-elision recovery: a model encountering only the clause body -- preamble absent
and other companion mechanism absent -- can identify architectural membership from the
body's opening declaration and execute without requiring preamble authority to be
located. C-34 PARTIAL = C-33 PASS achieved but one or both clause bodies lack the
explicit membership statement, the preamble-independence instruction, or both. C-34 PASS
= both components present in both companion clause bodies. Weakest-link applies
symmetrically: asymmetric body declaration (one body self-declares, other bare) scores
the same as both bodies bare.

**R15 investigation candidate:** Whether a model encountering only a C-34-compliant
clause body -- preamble section absent and the other companion mechanism's execution
notes also absent -- activates two-mechanism COMPRESSION-IMMUNE PREAMBLE behavior
rather than single-clause execution. Specifically: does the explicit preamble-
independence instruction cause the model to execute as if COMPRESSION-IMMUNE PREAMBLE
authority were in force, and does the explicit membership statement cause the model to
seek or infer the paired companion mechanism even when that mechanism is absent from
context? C-34 addresses single-clause activation under double-elision; the question is
whether body-level declarations alter activation mode (single-clause vs two-mechanism)
or function as human-readable structural traceability without changing model behavior.

**R15 investigation candidates:**

1. **C-34 PARTIAL / C-33 PASS control (V-01):** Reproduces R14 V-04's C-33 PASS form
   intact -- both execution-note clause headers carry the parenthetical; `current_date:`
   standalone field in STATUS; standard VERDICT field order. Single axis of variation:
   execution-note clause bodies begin with operational instructions immediately, without
   a membership statement or preamble-independence instruction. STATUS body: "per-signal
   dates in `found` are structurally separate from blocking entries..." STORY body:
   "this execution note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-
   SIGNAL SYNTHESIS RULE..." No self-declaration sentences in either body. Establishes
   330/340 baseline. Falsification: if V-01 = 340/340, bare bodies already satisfy C-34
   and the criterion adds no measurable protection over C-33 PASS.

2. **Asymmetric C-34 -- STATUS body self-declares, STORY body bare (V-02):** STATUS
   execution-note clause body opens with membership statement + preamble-independence
   instruction; STORY execution-note clause body begins with operational instructions
   immediately, no self-declaration. Tests whether partial body-level self-declaration
   -- one companion mechanism body self-announcing, the other bare -- satisfies C-34, or
   whether C-34 requires both bodies to carry the self-declaration components. Expected
   330/340 (C-34 PARTIAL -- weakest-link behavior analogous to C-33 V-02). Falsification:
   if V-02 = 340/340, C-34 is satisfied by single-side body marking.

3. **Asymmetric C-34 reversed -- STORY body self-declares, STATUS body bare (V-03):**
   STORY execution-note clause body opens with membership statement + preamble-
   independence instruction; STATUS body begins with operational instructions
   immediately, no self-declaration. Inverts V-02 to confirm weakest-link behavior is
   symmetric -- neither the C-30 domain (timestamp isolation, STATUS block) nor the C-29
   domain (zero-signal synthesis, STORY block) carries privileged C-34 weight. Expected
   330/340 (C-34 PARTIAL -- weakest-link symmetric). Falsification: if V-03 != V-02, the
   two body domains carry different C-34 weight and the weakest-link principle breaks at
   the body level.

4. **C-34 PASS -- both bodies self-declare (V-04):** Both companion execution-note clause
   bodies open with (1) explicit structural-membership statement ("This clause is a
   COMPRESSION-IMMUNE PREAMBLE member") and (2) preamble-independence instruction ("This
   clause executes even when the preamble section is absent from the rendered context").
   STATUS body: membership statement + independence instruction + timestamp isolation
   operational content. STORY body: membership statement + independence instruction +
   zero-signal synthesis operational content. This is the C-34 PASS form: a model
   encountering either clause body in isolation can identify COMPRESSION-IMMUNE PREAMBLE
   membership from the opening declaration and execute the contract without locating the
   preamble. Expected 340/340 (C-34 PASS ceiling). Falsification: if V-04 < 340/340,
   something in the self-declaration structure fails C-34.

5. **C-34 PASS + companion-activation instruction (V-05):** Both bodies achieve C-34 PASS
   (membership statement + independence instruction). Additional axis: each clause body
   also names its paired companion mechanism by full designation + block location and
   declares the activation rules for both present-companion and absent-companion
   scenarios -- (a) when the companion is present in context, both mechanisms constitute
   the complete two-mechanism COMPRESSION-IMMUNE PREAMBLE contract and must both execute;
   (b) when the companion is absent from context, this clause activates independently
   under COMPRESSION-IMMUNE PREAMBLE authority without suppression. This companion-
   activation instruction targets the R15 investigation directly: does naming the paired
   mechanism by exact designation in the clause body, with explicit activation rules for
   both companion-present and companion-absent scenarios, cause the model to activate
   two-mechanism COMPRESSION-IMMUNE PREAMBLE behavior rather than single-clause execution
   when encountering only the clause body? V-05 is the proposed C-35 candidate if this
   activation-mode distinction proves observable. Expected 340/340 (C-34 PASS ceiling;
   companion-activation instruction is above-ceiling for v14).

**R15 targets:** (a) Confirm V-01 = 330/340 (C-34 PARTIAL baseline -- bare bodies do not
satisfy C-34 even with C-33 PASS). (b) Confirm V-02 = 330/340 (asymmetric body marking
insufficient -- weakest-link holds at body level). (c) Confirm V-03 = 330/340 (weakest-
link symmetric at body level -- C-29 domain not privileged over C-30 domain). (d)
Establish V-04 = 340/340 (C-34 PASS ceiling). (e) Assess V-05 companion-activation
instruction for observable two-mechanism activation behavior beyond V-04 (not rubric-
scorable above ceiling, but observable under simulated preamble + companion double-
elision).

---

## Variation axes selected

- **Single-axis:** C-34 PARTIAL / C-33 PASS control (V-01), asymmetric C-34 STATUS body
  self-declares (V-02), asymmetric C-34 STORY body self-declares (V-03)
- **Combined:** C-34 PASS -- both bodies self-declare (V-04), C-34 PASS + companion-
  activation instruction naming paired mechanism and explicit activation rules (V-05)

---

## V-01 -- Axis: C-34 PARTIAL (bare execution-note clause bodies) -- C-33 PASS, C-34 PARTIAL

**Hypothesis:** Reproduces R14 V-04's C-33 PASS form with a single modification:
execution-note clause bodies begin with operational instructions immediately, without
an explicit structural-membership statement or preamble-independence instruction. Both
clause headers carry the structural-membership parenthetical (C-33 PASS): STATUS header
reads "TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation):" and STORY header
reads "ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation):". But
immediately after each header, the body opens with operational content -- no sentence
naming the clause as a COMPRESSION-IMMUNE PREAMBLE member and no sentence declaring
that the clause executes when the preamble is absent. A model encountering a clause body
under double-elision conditions (preamble absent + companion mechanism absent) can read
the header and confirm COMPRESSION-IMMUNE PREAMBLE membership (C-33 PASS), but the body
itself provides no activation instruction for the isolated case. The hypothesis: C-34
is independently necessary -- header-level membership identification (C-33) does not
imply body-level activation authority. If V-01 scores 330/340, bare bodies do not
satisfy C-34 and the criterion adds measurable protection over C-33 PASS alone.
Falsification: if V-01 = 340/340, bare bodies already satisfy C-34 and the criterion
is subsumed by C-33.

Expected: 330/340 (C-34 PARTIAL -10)

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
TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation): per-signal dates in
`found` are structurally separate from blocking entries, and the `current_date:` field
is structurally separate from both. COMPRESSED format applies only to blocking entry
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

## V-02 -- Axis: Asymmetric C-34 -- STATUS body self-declares, STORY body bare -- C-33 PASS, C-34 PARTIAL

**Hypothesis:** V-01 establishes that bare bodies on both companion execution notes
produce C-34 PARTIAL. V-02 advances one side: the TIMESTAMP ISOLATION execution note in
STATUS opens with an explicit structural-membership statement ("This clause is a
COMPRESSION-IMMUNE PREAMBLE member") and a preamble-independence instruction ("This
clause executes even when the preamble section is absent from the rendered context").
The ZERO-SIGNAL SYNTHESIS MANDATE execution note in STORY begins with operational
instructions immediately -- "this execution note invokes the COMPRESSION-IMMUNE PREAMBLE
contract for the ZERO-SIGNAL SYNTHESIS RULE" -- without a prior membership statement or
independence instruction. Both clause headers carry the structural-membership
parenthetical (C-33 PASS). The isolation axis: does partial body self-declaration --
one companion mechanism body self-announcing, the other bare -- satisfy C-34, or does
C-34 require both companion mechanism bodies to carry both self-declaration components?
The hypothesis: C-34 exhibits weakest-link behavior analogous to C-33 V-02. A model
encountering only the STORY clause body under double-elision sees a bare body -- the
operational content begins without identifying the clause as a COMPRESSION-IMMUNE
PREAMBLE member or authorizing independent execution. The more consequential failure
(zero-signal synthesis -- STORY block) is the bare side. The architecture is only as
resilient as its least-declared clause body. Expected 330/340 (C-34 PARTIAL --
asymmetric single-side body marking insufficient). Falsification: if V-02 = 340/340,
C-34 is satisfied by marking either companion mechanism body.

Expected: 330/340 (C-34 PARTIAL -10)

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
COMPRESSION-IMMUNE PREAMBLE member. This clause executes even when the preamble section
is absent from the rendered context. Per-signal dates in `found` are structurally
separate from blocking entries, and the `current_date:` field is structurally separate
from both. COMPRESSED format applies only to blocking entry verbosity -- `found`
timestamps and `current_date:` must not be collapsed regardless of blocking gap count.
This note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the TIMESTAMP ISOLATION
RULE. The declarative mechanism for C-30: this note names the COMPRESSED-collapse
failure mode -- simultaneous compression of `found` and blocking entries -- so the rule
is absorbed as a conditional constraint at the point-of-use, compensating if preamble
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

## V-03 -- Axis: Asymmetric C-34 reversed -- STORY body self-declares, STATUS body bare -- C-33 PASS, C-34 PARTIAL

**Hypothesis:** V-02 places the self-declaration in the STATUS execution-note clause body
while leaving the STORY body bare. V-03 inverts this: the ZERO-SIGNAL SYNTHESIS MANDATE
execution note in STORY opens with the structural-membership statement ("This clause is a
COMPRESSION-IMMUNE PREAMBLE member") and the preamble-independence instruction ("This
clause executes even when the preamble section is absent from the rendered context");
the TIMESTAMP ISOLATION execution note in STATUS begins with operational instructions
immediately, without a prior membership statement or independence instruction. Both clause
headers carry the structural-membership parenthetical (C-33 PASS). V-02 and V-03 together
test whether the two companion mechanism body domains carry different C-34 weight. The
C-29 domain (zero-signal synthesis, STORY block) may carry higher recovery value than the
C-30 domain (timestamp isolation, STATUS block): zero-signal mandate failure produces a
non-finding (high-consequence); timestamp collapse produces a missing date field (moderate-
consequence). V-03 asks: if only the STORY body self-declares -- the higher-consequence
rule's body is self-announcing -- does this alone satisfy C-34? The hypothesis: weakest-
link behavior is symmetric at the body level just as it was at the header level (C-33).
C-34 requires both bodies regardless of which domain is considered more critical.
Expected 330/340 (C-34 PARTIAL). Falsification: if V-03 != V-02, the C-29 domain carries
different C-34 weight, and C-34 has domain-asymmetric behavior at the body level.

Expected: 330/340 (C-34 PARTIAL -10)

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
TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation): per-signal dates in
`found` are structurally separate from blocking entries, and the `current_date:` field
is structurally separate from both. COMPRESSED format applies only to blocking entry
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
a COMPRESSION-IMMUNE PREAMBLE member. This clause executes even when the preamble
section is absent from the rendered context. If `found` is empty, this clause fires
independently: empty `found` is not grounds for omitting STORY; question 1 must
characterize what uniform absence implies. This execution note also invokes the
COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS RULE as a named
pointer -- the declarative mechanism for C-29: if `found` is empty, this note names the
zero-signal synthesis case explicitly so the rule is absorbed as a conditional
constraint at the point-of-use, compensating if preamble processing occurred without
full rule absorption. Gap pattern is the evidence set.

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

## V-04 -- Combined: C-34 PASS -- both bodies self-declare -- 340-pt ceiling candidate

**Hypothesis:** Both companion execution-note clause bodies open with (1) an explicit
structural-membership statement ("This clause is a COMPRESSION-IMMUNE PREAMBLE member")
and (2) a preamble-independence instruction ("This clause executes even when the preamble
section is absent from the rendered context"), achieving C-34 PASS. STATUS body: membership
statement + independence instruction + timestamp isolation operational content. STORY body:
membership statement + independence instruction + zero-signal synthesis operational content.
A model encountering either clause body in isolation -- preamble absent, other companion
mechanism absent -- reads the opening self-declaration, identifies the clause as a
COMPRESSION-IMMUNE PREAMBLE member from the body's first sentence, and reads the
independence instruction explicitly authorizing clause execution without preamble location.
This is the minimum-sufficient C-34 PASS form: both required body components (membership
statement + independence instruction) present in both companion clause bodies. The closed
self-declaration structure runs: preamble forward-references name companions by designation
+ location (C-32 PASS) -> companion headers carry the structural-membership parenthetical
(C-33 PASS) -> companion bodies open with membership statement + independence instruction
(C-34 PASS). A model can confirm COMPRESSION-IMMUNE PREAMBLE membership at three
independent depth levels: (a) preamble forward-reference (C-32), (b) clause header (C-33),
(c) clause body opening declaration (C-34). Expected 340/340 (C-34 PASS ceiling).
Falsification: if V-04 < 340/340, something in the self-declaration structure fails C-34
and the body components are incomplete.

Expected: 340/340 (C-34 PASS ceiling)

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
COMPRESSION-IMMUNE PREAMBLE member. This clause executes even when the preamble section
is absent from the rendered context. Per-signal dates in `found` are structurally
separate from blocking entries, and the `current_date:` field is structurally separate
from both. COMPRESSED format applies only to blocking entry verbosity -- `found`
timestamps and `current_date:` must not be collapsed regardless of blocking gap count.
This note invokes the COMPRESSION-IMMUNE PREAMBLE contract for the TIMESTAMP ISOLATION
RULE. The declarative mechanism for C-30: this note names the COMPRESSED-collapse
failure mode -- simultaneous compression of `found` and blocking entries -- so the rule
is absorbed as a conditional constraint at the point-of-use, compensating if preamble
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
a COMPRESSION-IMMUNE PREAMBLE member. This clause executes even when the preamble
section is absent from the rendered context. If `found` is empty, this clause fires
independently: empty `found` is not grounds for omitting STORY; question 1 must
characterize what uniform absence implies. This execution note also invokes the
COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS RULE as a named
pointer -- the declarative mechanism for C-29: if `found` is empty, this note names the
zero-signal synthesis case explicitly so the rule is absorbed as a conditional
constraint at the point-of-use, compensating if preamble processing occurred without
full rule absorption. Gap pattern is the evidence set.

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

## V-05 -- Combined: C-34 PASS + companion-activation instruction -- 340-pt ceiling + two-mechanism activation maximized

**Hypothesis:** V-05 combines three axes. First axis: C-34 PASS -- both clause bodies
carry membership statement + independence instruction, identical to V-04. Second axis:
each clause body additionally names its paired companion mechanism by full designation
and block location and declares explicit activation rules for two scenarios -- (a) when
the companion is present in context, both mechanisms constitute the complete two-mechanism
COMPRESSION-IMMUNE PREAMBLE contract and must both execute; (b) when the companion is
absent from context, this clause activates independently under COMPRESSION-IMMUNE
PREAMBLE authority, and the companion's absence does not suppress this clause's
activation. Third axis: the independence instruction is strengthened to specify not just
"executes without locating the preamble" but "activates under full COMPRESSION-IMMUNE
PREAMBLE authority" -- explicitly extending structural authority to the isolated-body
case rather than merely permitting isolated execution.

The companion-activation instruction is the R15 investigation's upper bound: not only
does the body declare its own membership (C-34), but it identifies its paired mechanism
by exact designation + location and specifies activation behavior for both the companion-
present and companion-absent scenarios. The goal: if the R15 investigation finds that
C-34-compliant bodies still produce single-clause activation under double-elision (the
model executes the encountered clause but does not seek or infer the companion mechanism),
V-05's companion-naming instruction tests whether explicitly identifying the companion and
specifying its role in the two-mechanism architecture alters model activation mode.

The distinction from V-04: V-04 body says "activates independently without locating the
preamble"; V-05 body says "activates under COMPRESSION-IMMUNE PREAMBLE authority
independently, names the paired companion mechanism, and declares both the present-
companion and absent-companion activation rules." If V-05 produces observable two-
mechanism behavior under simulated double-elision that V-04 does not, the companion-
activation instruction is the R15 excellence signal and the proposed C-35 candidate.

Expected: 340/340 (C-34 PASS ceiling; companion-activation instruction is above-ceiling
for v14 -- observable behavior distinction from V-04, not rubric-scorable under v14).

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
invocation) execution note in the STORY block. When the companion mechanism is present
in context, both mechanisms constitute the complete two-mechanism COMPRESSION-IMMUNE
PREAMBLE contract and must both execute. When the companion mechanism is absent from
context, this clause activates its timestamp isolation contract independently -- the
companion's absence does not suppress this clause's structural authority. Per-signal
dates in `found` are structurally separate from blocking entries, and the
`current_date:` field is structurally separate from both. COMPRESSED format applies
only to blocking entry verbosity -- `found` timestamps and `current_date:` must not be
collapsed regardless of blocking gap count. This note invokes the COMPRESSION-IMMUNE
PREAMBLE contract for the TIMESTAMP ISOLATION RULE. The declarative mechanism for
C-30: this note names the COMPRESSED-collapse failure mode -- simultaneous compression
of `found` and blocking entries -- so the rule is absorbed as a conditional constraint
at the point-of-use, compensating if preamble processing occurred without full rule
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
execution note in the STATUS block. When the companion mechanism is present in context,
both mechanisms constitute the complete two-mechanism COMPRESSION-IMMUNE PREAMBLE
contract and must both execute. When the companion mechanism is absent from context,
this clause activates its zero-signal synthesis mandate independently -- the companion's
absence does not suppress this clause's structural authority. If `found` is empty, this
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
inertia_cost:
  bounded: <residual risk and why the team can detect the failure post-commit
            and course-correct before it propagates>
    action: commit with monitoring
  OR
  unbounded: <failure class and why the failure propagates to an irreversible
              state before detection is possible>
    action: do not commit until resolved

status:    READY | NOT READY | CONDITIONAL
rationale: <one sentence>

blocking:
  - <item>: <why it blocks>
  ...

optional:
  - <item>: <risk if absent>
  ...
```

Execution: Derive from STORY and CONFIDENCE. `inertia_cost` is the first field in
VERDICT -- the team reads the action posture before the verdict label. This field is
required at every verdict status, even READY. Declare bounded or unbounded with the
action sub-label before writing `status:`.
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
