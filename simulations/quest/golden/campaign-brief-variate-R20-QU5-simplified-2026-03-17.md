---
skill: campaign-brief
variant: QU5-simplified
source_variant: R20-V05
date: 2026-03-17
original_word_count: 1931
simplified_word_count: 1494
reduction_pct: 22.6
all_essential_still_pass: true
---

# QU5 Simplification -- campaign-brief / R20-V05

**Removed (437 words / 22.6%):** Meta-explanatory sentences doing no structural work:
TOKEN-PRESSURE GUARD paragraph (restates "unconditionally"), Basis rationale prose,
tail of COMPRESSED-COLLAPSE GUARD (positional mechanism explanation + execution-note
cross-reference), "When companion is present...must both execute" clause in both
execution notes (redundant with preamble unconditional mandate), "This note invokes..."
self-referential sentences, "The declarative mechanism for C-3N:..." explanatory
sentences, "Gap pattern is the evidence set" standalone sentence, VERDICT "action
sub-label not optional format" rationale sentence, VERDICT "If COMPRESSED was active
for blocking entries" clause (redundant with "VERDICT is never abbreviated").

**Preserved:** All operative criteria -- C-29 (zero-signal synthesis), C-30 (timestamp
isolation), C-38 (parity constraint), C-39 (complete structural deliverables
enumeration for each companion), C-40 (non-degradation / depth-symmetry).

---

## Simplified skill body (V05-QU5)

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
as deferred context that can be deprioritized as token pressure increases.

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

TIMESTAMP ISOLATION RULE (C-30 domain):

Per-signal dates in the `found` section of STATUS are structurally separate from
blocking gap entries. Each signal in `found` must carry its own date at item level.
COMPRESSED format applies only to blocking entry verbosity -- it does not affect
found timestamps. Found timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count or token budget.

COMPRESSED-COLLAPSE GUARD: The specific failure mode this rule prevents is
COMPRESSED-collapse -- simultaneous compression of `found` entries and blocking gap
entries when token pressure activates the COMPRESSED branch.

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
absent from the rendered context, this clause activates its timestamp isolation
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
collapsed regardless of blocking gap count.

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
execution note in the STATUS block. When the companion execution note is absent from the
rendered context, this clause activates its zero-signal synthesis mandate independently
with full COMPRESSION-IMMUNE PREAMBLE authority -- the absent TIMESTAMP ISOLATION's
mandate is independently operative even when its execution note is not in context and
must be executed as if its execution note were present in this context, at full depth,
at parity with what would be produced if the companion's execution note were present in
this context. This parity constraint is symmetric: executing this companion mandate does
not reduce the present clause's own output depth. Both mandates execute at full depth
simultaneously. For this companion (TIMESTAMP ISOLATION), full-depth execution means:
each entry in the `found` section of STATUS carries its own date at item level; the
`current_date:` field appears at STATUS block header level; no `found` timestamp is
collapsed, summarized, or omitted regardless of blocking gap count or token budget --
the same structural separation that would be enforced if the TIMESTAMP ISOLATION
execution note were present in the STATUS block. If `found` is empty, this clause
fires independently: empty `found` is not grounds for omitting STORY; question 1 must
characterize what uniform absence implies.

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
never abbreviated. A CONDITIONAL verdict must name the condition and what satisfies it;
its `inertia_cost` must include the `action:` sub-label specifying posture for the
unresolved risk period.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.
