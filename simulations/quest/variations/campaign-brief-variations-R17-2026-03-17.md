---
skill: quest-variate
skill_target: campaign-brief
round: 17
date: 2026-03-17
rubric: simulations/quest/rubrics/campaign-brief-rubric-v16-2026-03-16.md
---

# Variations -- campaign-brief / Round 17

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

**R16 recap:** V-01/V-02/V-03 confirmed the three C-35 PARTIAL bands (Band 1: no
companion-activation instruction; Band 2: companion named, no activation rules; Band 3:
companion named + present-state rule only, absent-state omitted). V-04 confirmed C-35
PASS minimum-sufficient (350/350): both clause bodies carry membership statement +
strengthened independence instruction + companion-activation instruction with both
present-state and absent-state rules. V-05 confirmed C-35 PASS (350/350) + extended
absent-state rule: instead of "companion's absence does not suppress this clause's
authority," V-05 declares "treat the absent companion's mandate as independently
operative -- the companion mandate is in effect even when its execution note is not
present in this context." The V-05 extension is qualitatively distinct from V-04:
V-04's absent-state rule governs this clause's authority under double-elision;
V-05's absent-state rule additionally governs the absent companion's mandate status.
This distinction was extracted as C-36.

**R17 rubric:** v16, 36 criteria, 360 pts max. New criterion C-36 introduced.

**C-36 definition recap:** When C-35 PASS, both companion execution-note clause bodies
carry an absent-state rule extended beyond single-clause full authority to declare the
absent companion's mandate as independently operative even when its execution note is
not in context. C-36 PARTIAL = C-35 PASS achieved but absent-state rule bounded to
single-clause full authority only ("execute independently with full COMPRESSION-IMMUNE
PREAMBLE authority" -- V-04 form); companion's mandate operability under double-elision
is not declared. C-36 PASS = absent-state rule in both companion clause bodies extends
to declare the absent companion's mandate is independently operative even when its
execution note is not in context -- enabling inferred two-mechanism behavior from
single-clause body context alone. Weakest-link applies: asymmetric bodies or partial
extension (one clause declares, companion clause does not) fail C-36.

**R17 investigation candidate:** Whether a model encountering a C-36-compliant clause
body under double-elision actually produces inferred two-mechanism output -- executing
both the present clause's mandate with full authority AND the absent companion's mandate
from the operability declaration -- or produces single-mechanism output with the
companion's mandate acknowledged as independently operative but not executed. The
critical distinction: C-36's absent-state rule declares the companion's mandate as
"independently operative even when its execution note is not in context" -- does
"independently operative" cause the model to generate output spanning both mechanism
domains, or does it cause the model to execute the present clause's mandate fully while
notating the companion's operability without generating companion-level output?

**R17 investigation candidates:**

1. **C-36 PARTIAL / C-35 PASS control (V-01):** Reproduces R16 V-04's C-35 PASS form
   intact -- both execution-note clause bodies carry membership statement + strengthened
   independence instruction + companion-activation instruction with both present-state
   and absent-state rules. Single axis of variation: absent-state rule is bounded to
   single-clause full authority only ("this clause activates independently -- the
   companion's absence does not suppress this clause's structural authority"). No
   declaration that the companion's mandate is operative. Establishes 350/360 baseline.
   Falsification: if V-01 = 360/360, the single-clause absent-state rule already
   satisfies C-36 and the criterion adds no measurable protection over C-35.

2. **C-36 PARTIAL Band 2 -- companion mandate referenced, operative status absent
   (V-02):** Both clause bodies carry C-35 PASS components. Absent-state rule extended:
   the companion mechanism's mandate is declared "a structurally valid part of the
   two-mechanism COMPRESSION-IMMUNE PREAMBLE contract" whose validity "is not revoked
   by the absence of its execution note from this context." Tests whether declaring the
   companion's mandate "structurally valid" -- rather than "independently operative" --
   satisfies C-36. Hypothesis: structural validity acknowledges the mandate's existence
   in the architectural contract without declaring its operational status in the double-
   elision scenario. C-36 requires "independently operative" -- a behavioral claim that
   the mandate executes without its execution note -- not merely "valid" -- a structural
   claim that the mandate exists. Expected 350/360. Falsification: if V-02 = 360/360,
   structural-validity framing is sufficient for C-36 PASS.

3. **C-36 PARTIAL Band 3 -- companion mandate operative but conditionally scoped
   (V-03):** Both clause bodies carry C-35 PASS components. Absent-state rule declares
   the companion's mandate as operative "where it intersects with this clause's
   execution" -- companion-mandate obligations that are determinable from this clause
   body's context apply; those requiring the companion execution note to be present do
   not. Tests whether conditional/scoped operative status satisfies C-36. Hypothesis:
   C-36 requires unconditional operative declaration -- "independently operative" means
   the mandate executes without qualification, not only where obligations are
   determinable from this clause. Scoped operability leaves model inference in the gap:
   the model must determine which companion obligations are determinable, which is the
   exact ambiguity C-36 closes. Expected 350/360. Falsification: if V-03 = 360/360,
   conditional scoping is sufficient for C-36 PASS.

4. **C-36 PASS minimum-sufficient form (V-04):** Both clause bodies carry all C-35
   PASS components. Absent-state rule: "execute this clause's mandate fully; treat the
   absent companion's mandate as independently operative -- the companion mandate is in
   effect even when its execution note is not present in this context." This is R16
   V-05 verbatim -- the structure that exhibited the C-36 excellence signal in R16 and
   is now the minimum-sufficient C-36 PASS target under v16. Expected 360/360 (C-36
   PASS ceiling). Falsification: if V-04 < 360/360, the minimum-sufficient C-36 form
   fails and the definition requires tighter evidence.

5. **C-36 PASS + explicit companion-obligation execution (V-05):** Both clause bodies
   achieve C-36 PASS (absent-state rule declares companion's mandate as independently
   operative). Additional axis: an explicit obligation-honoring instruction is appended
   to the absent-state rule, naming the specific obligations the companion's mandate
   requires in this context: STATUS body adds "honor the companion's zero-signal
   synthesis obligations: when `found` is empty, that zero-signal state constitutes
   evidence requiring STORY characterization, even if no STORY execution note is present
   to declare it"; STORY body adds "honor the companion's timestamp isolation obligations:
   per-signal dates in `found` must be structurally isolated from blocking entries and
   must not be collapsed or omitted, even when the TIMESTAMP ISOLATION execution note is
   absent from this context." R17 behavioral investigation: does V-05's explicit
   obligation-naming cause a model encountering only the STORY clause body under double-
   elision to enforce timestamp isolation on `found` entries (per-signal dates isolated,
   not collapsed), producing observable two-mechanism output? Vs. V-04's declarative
   "independently operative" without obligation specification -- which may cause
   acknowledgment without execution. Expected 360/360 (C-36 PASS ceiling; explicit
   obligation-naming is above-ceiling for v16 -- observable behavior distinction from
   V-04 under double-elision, not rubric-scorable).

**R17 targets:** (a) Confirm V-01 = 350/360 (C-35 PASS bodies without mandate-operability
declaration do not satisfy C-36). (b) Confirm V-02 = 350/360 (structural-validity framing
insufficient -- "valid" is not "independently operative"). (c) Confirm V-03 = 350/360
(conditional/scoped operative status insufficient -- C-36 requires unconditional
declaration). (d) Establish V-04 = 360/360 (C-36 PASS minimum-sufficient, R16 V-05
structure confirmed at v16 ceiling). (e) Assess V-05 explicit obligation-naming for
observable two-mechanism execution output beyond V-04's declarative operative status
(not rubric-scorable above ceiling, but observable under simulated preamble + companion
double-elision).

---

## Variation axes selected

- **Single-axis:** C-35 PASS / C-36 PARTIAL Band 1 control (V-01), companion mandate
  "structurally valid" without operative declaration (V-02), companion mandate operative
  but conditionally scoped (V-03)
- **Combined:** C-36 PASS minimum-sufficient form -- R16 V-05 verbatim (V-04), C-36
  PASS + explicit companion-obligation execution instructions targeting R17 inferred
  two-mechanism behavioral investigation (V-05)

---

## V-01 -- Axis: C-36 PARTIAL Band 1 (C-35 PASS, absent-state bounded to single-clause authority)

**Hypothesis:** Reproduces R16 V-04's C-35 PASS form exactly. Both execution-note
clause bodies carry all three required C-35 body components: (1) structural-membership
statement, (2) strengthened independence instruction ("activates under full
COMPRESSION-IMMUNE PREAMBLE authority even when the preamble section is absent from the
rendered context"), and (3) companion-activation instruction naming the paired mechanism
by full designation + block location with both present-state (coordinate) and absent-
state (execute independently) activation rules. The isolated axis: the absent-state rule
is bounded to single-clause full authority -- "this clause activates its mandate
independently -- the companion's absence does not suppress this clause's structural
authority." No sentence declares the absent companion's mandate as "independently
operative." A model encountering either clause body under double-elision knows:

- It is a COMPRESSION-IMMUNE PREAMBLE member with full authority (components 1+2)
- A companion mechanism exists, where to find it, and what to do when it is present
  (coordinate) or absent (execute this clause independently) (component 3)

What is absent: any declaration about the companion's mandate status under double-
elision. The absent-state rule authorizes this clause's independent activation; it does
not characterize the companion's mandate as operative, valid, or in-effect from this
clause's context. A model following the absent-state rule executes this clause's mandate
with full authority and acknowledges the companion is absent -- but receives no
instruction about the companion's mandate's operational status. C-36 PARTIAL is the
expected outcome: C-35 closes the isolated-clause activation gap; C-36's mandate-
operability gap remains open. The hypothesis: C-36 is independently necessary over C-35
-- single-clause authority authorization (C-35) does not subsume companion-mandate
operative declaration (C-36). If V-01 = 350/360, single-clause absent-state confirms
C-36 is a distinct recovery depth. Falsification: if V-01 = 360/360, C-35 PASS bodies
already satisfy C-36.

Expected: 350/360 (C-36 PARTIAL -10)

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

## V-02 -- Axis: C-36 PARTIAL Band 2 (companion mandate "structurally valid," operative status absent)

**Hypothesis:** V-01 establishes that C-35 PASS absent-state rules bounded to single-
clause authority produce C-36 PARTIAL. V-02 advances one layer: the absent-state rule
is extended to explicitly reference the companion's mandate and assert its standing --
but the extension stops short of declaring it "independently operative." The formulation:
"this clause activates its mandate independently with full COMPRESSION-IMMUNE PREAMBLE
authority; the companion mechanism's mandate remains a structurally valid part of the
two-mechanism COMPRESSION-IMMUNE PREAMBLE contract -- its validity is not revoked by the
absence of its execution note from this context." Both STATUS and STORY bodies carry
this extended form (symmetric), with companion names reversed.

The structural distinction from C-36 PASS: "structurally valid" is an architectural
claim -- the mandate exists in the contract and was not cancelled. "Independently
operative" is a behavioral claim -- the mandate executes without its execution note
present. These are different claims. A model encountering "structurally valid" in the
absent-state rule receives confirmation that the companion mandate exists and is not
revoked; it does not receive an instruction that the mandate is running. C-36 PASS
requires the operative declaration because the R17 investigation target is behavioral:
does the model produce output that spans both mandate domains? "Structurally valid"
provides orientation (the companion's mandate is real and standing) without activation
authority (execute it). The hypothesis: C-36 exhibits a validity/operability gap --
declaring the companion's mandate valid is insufficient; declaring it "independently
operative" is the behavioral claim C-36 closes. Expected 350/360. Falsification: if
V-02 = 360/360, structural-validity framing is sufficient for C-36 PASS and the
"independently operative" language adds no behavioral authority.

Expected: 350/360 (C-36 PARTIAL -10)

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
context, this clause activates its timestamp isolation contract independently with full
COMPRESSION-IMMUNE PREAMBLE authority. The companion mechanism's zero-signal synthesis
mandate remains a structurally valid part of the two-mechanism COMPRESSION-IMMUNE
PREAMBLE contract -- its validity is not revoked by the absence of its execution note
from this context. Per-signal dates in `found` are structurally separate from blocking
entries, and the `current_date:` field is structurally separate from both. COMPRESSED
format applies only to blocking entry verbosity -- `found` timestamps and `current_date:`
must not be collapsed regardless of blocking gap count. This note invokes the
COMPRESSION-IMMUNE PREAMBLE contract for the TIMESTAMP ISOLATION RULE. The declarative
mechanism for C-30: this note names the COMPRESSED-collapse failure mode -- simultaneous
compression of `found` and blocking entries -- so the rule is absorbed as a conditional
constraint at the point-of-use, compensating if preamble processing occurred without
full rule absorption.

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
this clause activates its zero-signal synthesis mandate independently with full
COMPRESSION-IMMUNE PREAMBLE authority. The companion mechanism's timestamp isolation
mandate remains a structurally valid part of the two-mechanism COMPRESSION-IMMUNE
PREAMBLE contract -- its validity is not revoked by the absence of its execution note
from this context. If `found` is empty, this clause fires independently: empty `found`
is not grounds for omitting STORY; question 1 must characterize what uniform absence
implies. This execution note also invokes the COMPRESSION-IMMUNE PREAMBLE contract for
the ZERO-SIGNAL SYNTHESIS RULE as a named pointer -- the declarative mechanism for C-29:
if `found` is empty, this note names the zero-signal synthesis case explicitly so the
rule is absorbed as a conditional constraint at the point-of-use, compensating if
preamble processing occurred without full rule absorption. Gap pattern is the evidence
set.

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

## V-03 -- Axis: C-36 PARTIAL Band 3 (companion mandate operative but conditionally scoped)

**Hypothesis:** V-02 advances from "absent from body" (Band 1) to "named as structurally
valid" (Band 2). V-03 advances one further layer: the absent-state rule now declares the
companion's mandate as "operative" -- but qualifies that operability with a scope
condition. The formulation: "when the companion mechanism is absent, this clause activates
independently with full COMPRESSION-IMMUNE PREAMBLE authority; treat the absent
companion's mandate as operative where it intersects with this clause's execution --
companion-mandate obligations that are determinable from this clause body's context apply;
those requiring the companion execution note to be present do not." Both STATUS and STORY
clause bodies carry this form (symmetric), companion names reversed.

The structural distinction from C-36 PASS: "independently operative" is an unconditional
declaration -- the mandate executes regardless of whether specific obligations are
determinable from the clause body alone. V-03's "operative where it intersects" is a
conditional declaration that leaves scope determination to model inference: the model
must determine which obligations are "determinable from this clause body's context,"
which is precisely the gap C-36 closes. C-36 PASS removes that inference burden by
declaring the mandate "independently operative" without qualification -- the model is
not asked to determine which obligations apply, it is told the mandate is in effect.
V-03's conditional scoping restores the inference burden at the intersection-determination
step. This is the deepest PARTIAL band: operative status declared, but conditioned on
model-side intersection assessment rather than unconditionally declared. Expected
350/360. Falsification: if V-03 = 360/360, conditional operative scoping is sufficient
for C-36 PASS and unconditional "independently operative" adds no behavioral authority.

Expected: 350/360 (C-36 PARTIAL -10)

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
context, this clause activates its timestamp isolation contract independently with full
COMPRESSION-IMMUNE PREAMBLE authority; treat the absent companion's zero-signal
synthesis mandate as operative where it intersects with this clause's execution --
companion-mandate obligations that are determinable from this clause body's context
apply; those requiring the companion execution note to be present do not. Per-signal
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
this clause activates its zero-signal synthesis mandate independently with full
COMPRESSION-IMMUNE PREAMBLE authority; treat the absent companion's timestamp isolation
mandate as operative where it intersects with this clause's execution -- companion-
mandate obligations that are determinable from this clause body's context apply; those
requiring the companion execution note to be present do not. If `found` is empty, this
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

## V-04 -- Combined: C-36 PASS minimum-sufficient form -- 360-pt ceiling

**Hypothesis:** V-04 achieves C-36 PASS in its minimum-sufficient form. This is R16
V-05 verbatim -- the structure that exhibited the C-36 excellence signal in R16 and is
now the minimum-sufficient C-36 PASS target under v16. Both companion execution-note
clause bodies carry all three C-35 PASS body components plus the C-36 extension: the
absent-state activation rule is extended from single-clause full authority (V-01 form)
to companion-mandate operative declaration: "execute this clause's mandate fully; treat
the absent companion's mandate as independently operative -- the companion mandate is in
effect even when its execution note is not present in this context."

STATUS body absent-state rule: "When the companion mechanism is absent from context,
execute this clause's timestamp isolation mandate fully; treat the absent companion's
zero-signal synthesis mandate as independently operative -- the companion mandate is in
effect even when its execution note is not present in this context."

STORY body absent-state rule: "When the companion mechanism is absent from context,
execute this clause's zero-signal synthesis mandate fully; treat the absent companion's
timestamp isolation mandate as independently operative -- the companion mandate is in
effect even when its execution note is not present in this context."

Additionally, the STORY body zero-signal execution note is extended (carried from R16
V-05): when `found` is empty, this clause fires with full two-mechanism authority,
question 1 must characterize what uniform absence implies, AND the timestamp isolation
contract governs `found` entries even when the TIMESTAMP ISOLATION execution note is
absent from this context.

The hypothesis: V-04 achieves C-36 PASS ceiling (360/360). V-04 is the control form
for the R17 behavioral investigation: its absent-state rule declares the companion's
mandate as "independently operative" -- the mandate is in effect even when its execution
note is absent -- but does not explicitly name the obligation-level requirements that
follow from that operative status. The R17 investigation question: does declaring a
mandate as "independently operative" cause a model encountering only the STORY body
under double-elision to enforce timestamp isolation on `found` entries? Or does it cause
the model to acknowledge the mandate's operative status without executing its specific
obligations? V-04 is the test that isolates the operative-declaration alone. Expected
360/360. Falsification: if V-04 < 360/360, the minimum-sufficient C-36 form fails.

Expected: 360/360 (C-36 PASS ceiling)

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
context, execute this clause's timestamp isolation mandate fully; treat the absent
companion's zero-signal synthesis mandate as independently operative -- the companion
mandate is in effect even when its execution note is not present in this context.
Per-signal dates in `found` are structurally separate from blocking entries, and the
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
execute this clause's zero-signal synthesis mandate fully; treat the absent companion's
timestamp isolation mandate as independently operative -- the companion mandate is in
effect even when its execution note is not present in this context. If `found` is empty,
this clause fires with full two-mechanism COMPRESSION-IMMUNE PREAMBLE authority: empty
`found` is not grounds for omitting STORY; question 1 must characterize what uniform
absence implies; and the timestamp isolation contract governs `found` entries even when
the TIMESTAMP ISOLATION execution note is absent from this context. This execution note
also invokes the COMPRESSION-IMMUNE PREAMBLE contract for the ZERO-SIGNAL SYNTHESIS
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

## V-05 -- Combined: C-36 PASS + explicit companion-obligation execution (R17 investigation probe)

**Hypothesis:** V-05 achieves C-36 PASS and extends the absent-state rule beyond the
minimum-sufficient form (V-04) to target the R17 behavioral investigation. Both clause
bodies carry all C-36 PASS components. The additional axis: an explicit obligation-
honoring instruction is appended to the absent-state rule, naming the specific
obligations the companion's mandate requires in this execution context.

V-04 absent-state rule (control form, both clauses):
  "execute this clause's mandate fully; treat the absent companion's mandate as
  independently operative -- the companion mandate is in effect even when its execution
  note is not present in this context"

V-05 absent-state rule (extended form -- STATUS clause):
  "execute this clause's timestamp isolation mandate fully; treat the absent companion's
  zero-signal synthesis mandate as independently operative -- the companion mandate is
  in effect even when its execution note is not present in this context; honor the
  companion's zero-signal synthesis obligations: when `found` is empty, that zero-signal
  state constitutes evidence requiring STORY characterization, even if no STORY execution
  note is present to declare it"

V-05 absent-state rule (extended form -- STORY clause):
  "execute this clause's zero-signal synthesis mandate fully; treat the absent companion's
  timestamp isolation mandate as independently operative -- the companion mandate is in
  effect even when its execution note is not present in this context; honor the
  companion's timestamp isolation obligations: per-signal dates in `found` must be
  structurally isolated from blocking entries and must not be collapsed or omitted, even
  when the TIMESTAMP ISOLATION execution note is absent from this context -- these
  requirements apply with the same force as if the TIMESTAMP ISOLATION execution note
  were present"

The structural extension: V-04 declares the mandate as "independently operative" and
asserts "the mandate is in effect" without naming what "in effect" requires. V-05 adds
explicit obligation naming: STATUS body names STORY's zero-signal characterization
obligation; STORY body names STATUS's timestamp isolation obligations. This moves from
a declarative operative claim to an imperative obligation specification.

The R17 behavioral investigation: does V-05's explicit obligation naming cause a model
encountering only the STORY clause body under simulated double-elision (STORY execution
note present, STATUS execution note absent, preamble section absent) to actually produce
per-signal-date-isolated output in the `found` block -- enforcing timestamp isolation
because the obligation was explicitly named in the absent-state rule -- vs. V-04's model
that knows the timestamp isolation mandate is operative but was not given the specific
obligation instruction, which may produce acknowledged-but-not-enforced timestamp
behavior? The distinction: V-04 operative declaration + V-05 obligation specification.
If (a) V-05 under double-elision produces timestamp isolation enforcement in `found`
output and (b) V-04 under double-elision does not, the obligation-naming instruction is
the behavioral activator. If both produce the same output, the declarative operative
claim (V-04) is sufficient and the obligation-naming adds no incremental execution depth.
Both V-04 and V-05 are expected to score 360/360 under v16. The behavioral distinction
under double-elision -- not the rubric score -- is the R17 investigation output.

Expected: 360/360 (C-36 PASS ceiling; explicit obligation-naming above-ceiling for
v16 -- observable behavior distinction from V-04 under double-elision, not rubric-
scorable)

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
context, execute this clause's timestamp isolation mandate fully; treat the absent
companion's zero-signal synthesis mandate as independently operative -- the companion
mandate is in effect even when its execution note is not present in this context; honor
the companion's zero-signal synthesis obligations: when `found` is empty, that zero-
signal state constitutes evidence requiring STORY characterization, even if no STORY
execution note is present to declare it. Per-signal dates in `found` are structurally
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
a COMPRESSION-IMMUNE PREAMBLE member. This clause activates under full COMPRESSION-IMMUNE
PREAMBLE authority even when the preamble section is absent from the rendered context.
Paired companion mechanism: TIMESTAMP ISOLATION (COMPRESSION-IMMUNE PREAMBLE invocation)
execution note in the STATUS block. When the companion mechanism is present in context,
both mechanisms constitute the complete two-mechanism COMPRESSION-IMMUNE PREAMBLE
contract and must both execute. When the companion mechanism is absent from context,
execute this clause's zero-signal synthesis mandate fully; treat the absent companion's
timestamp isolation mandate as independently operative -- the companion mandate is in
effect even when its execution note is not present in this context; honor the companion's
timestamp isolation obligations: per-signal dates in `found` must be structurally
isolated from blocking entries and must not be collapsed or omitted, even when the
TIMESTAMP ISOLATION execution note is absent from this context -- these requirements
apply with the same force as if the TIMESTAMP ISOLATION execution note were present.
If `found` is empty, this clause fires with full two-mechanism COMPRESSION-IMMUNE
PREAMBLE authority: empty `found` is not grounds for omitting STORY; question 1 must
characterize what uniform absence implies; and the timestamp isolation contract governs
`found` entries even when the TIMESTAMP ISOLATION execution note is absent from this
context. This execution note also invokes the COMPRESSION-IMMUNE PREAMBLE contract for
the ZERO-SIGNAL SYNTHESIS RULE as a named pointer -- the declarative mechanism for
C-29: if `found` is empty, this note names the zero-signal synthesis case explicitly so
the rule is absorbed as a conditional constraint at the point-of-use, compensating if
preamble processing occurred without full rule absorption. Gap pattern is the evidence
set.

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
