---
skill: quest-variate
skill_target: campaign-brief
round: 12
date: 2026-03-17
rubric: simulations/quest/rubrics/campaign-brief-rubric-v11-2026-03-17.md
---

# Variations -- campaign-brief / Round 12

Five complete, runnable skill body variations. Single-axis first (V-01, V-02, V-03),
then combined (V-04, V-05).

**R11 recap:** V-04 and V-05 both scored 300/300 under v10 rubric (ceiling). Both
implement C-30 full dual-mechanism: (1) TIMESTAMP ISOLATION RULE in preamble
(positional mechanism, counters location elision); (2) COMPRESSED-COLLAPSE GUARD in
STATUS execution note (declarative mechanism, counters positional processing without
rule absorption). V-03 confirmed C-30 declarative-only is insufficient (290/300,
C-30 PARTIAL). V-02 confirmed C-30 preamble-only is insufficient (290/300, C-30
PARTIAL). V-01 confirmed C-24 dual-location alone does not satisfy C-30 (290/300,
C-30 PARTIAL). R11 fully validated: C-30 requires orthogonal-failure-mode dual-
mechanism, independently of C-24's same-class dual-location.

**R12 rubric:** v11, 31 criteria, 310 pts max. New criterion C-31 introduced.

**C-31 definition recap:** When C-29 and C-30 both PASS, the shared positional
mechanism is explicitly designated as a compression-immune structural unit rather than
maintained as independent per-rule preamble placements. C-31 does not replace C-29 and
C-30 -- each still requires its own dual-mechanism. C-31 requires an additional layer:
the preamble section that houses both rules is explicitly named as a structural unit
that is immune to compression, rather than being a coincidental co-location of two
independently placed rules.

**R12 investigation candidates:**

1. **C-31 absent (V-01 control):** Whether R11's best form (V-04 clean dual-mechanism
   for both rules, distributed per-rule preamble placement) scores 300/310 under v11.
   Confirms C-31 is independently necessary and that distributed per-rule dual-mechanism
   does not automatically satisfy C-31 PASS. Falsification: if V-01 scores 310/310,
   C-31 is already satisfied by the distributed form and the criterion must be
   re-examined.

2. **Unified label without structural designation (V-02):** Whether grouping both rules
   under a shared "COMPRESSION-CRITICAL EXECUTION RULES" header (descriptive, not
   structural) achieves C-31 PASS. Tests whether the C-31 contract requires a specific
   designation ("COMPRESSION-IMMUNE") vs. any unified labeling. Expected: 300/310
   (C-31 PARTIAL -- label is descriptive, not a structural contract).

3. **COMPRESSION-IMMUNE designation without execution-note cross-reference (V-03):**
   Whether the explicit COMPRESSION-IMMUNE PREAMBLE section header, without execution
   notes referencing the section by designation, achieves C-31 PASS. Isolates the
   designation mechanism from the cross-reference mechanism. If V-03 scores 310/310,
   the designation alone is sufficient. If 300/310, cross-reference is independently
   necessary and V-05 becomes the definitive form.

4. **Three-rule distributed scale test (V-04):** Whether distributed per-rule dual-
   mechanism remains sufficient when three compression-critical rules coexist (C-29,
   C-30, and VERDICT action posture). Tests the hypothesis that distributed mechanisms
   degrade as rule count increases. C-31 PARTIAL by construction. If V-04 scores
   below 300 (e.g., 290), distributed dual-mechanism fails at three-rule scale, making
   C-31 consolidation necessary on structural grounds independent of explicit designation.

5. **Full C-31 PASS (V-05):** COMPRESSION-IMMUNE PREAMBLE designation + execution-note
   cross-references for both C-29 and C-30 rules. Establishes the 310-pt ceiling. If
   V-05 > V-04 > V-01 = 300, C-31 is independently necessary and consolidation adds
   protection beyond distributed dual-mechanism.

**R12 targets:** (a) Confirm V-01 = 300/310 (C-31 baseline). (b) Confirm V-02 = 300/310
(label insufficient for C-31 PASS). (c) Falsify or confirm V-03 PASS (designation
alone sufficient?). (d) Test V-04 scale degradation at three rules. (e) Establish
V-05 = 310/310 ceiling.

---

## Variation axes selected

- **Single-axis:** C-31 absent / V-04 form (V-01), unified label without COMPRESSION-IMMUNE
  designation (V-02), COMPRESSION-IMMUNE designation without cross-reference (V-03)
- **Combined:** Three-rule distributed scale + inertia framing foregrounded (V-04), Full
  C-31 PASS -- COMPRESSION-IMMUNE PREAMBLE + execution-note cross-references (V-05)

---

## V-01 -- Axis: C-31 absent (control) -- C-29 PASS, C-30 PASS, C-31 PARTIAL

**Hypothesis:** This variation reproduces R11's V-04 form exactly. C-29 PASS is
guaranteed: ZERO-SIGNAL SYNTHESIS RULE in preamble with TOKEN-PRESSURE GUARD (positional
mechanism) + zero-signal synthesis mandate in STORY execution note (declarative
mechanism). C-30 PASS is guaranteed: TIMESTAMP ISOLATION RULE in preamble (positional
mechanism) + COMPRESSED-COLLAPSE GUARD in STATUS execution note (declarative mechanism).
C-31 is not addressed: the two rules occupy separate preamble paragraphs -- they are
co-located by adjacency, not consolidated under an explicit structural contract. No
section header designates the preamble as COMPRESSION-IMMUNE. The hypothesis: C-31
requires the designation itself, not merely the co-location of two compliant rules.
If V-01 scores 300/310, C-31 is independently necessary. Falsification: if V-01 scores
310/310, distributed co-location in the preamble already satisfies C-31 and the explicit
designation criterion must be re-examined.

Expected: 300/310 (C-31 PARTIAL -10)

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

COMPRESSED-COLLAPSE GUARD: The specific failure mode this rule prevents is COMPRESSED-
collapse -- the model collapsing `found` signal entries into the blocking gap summary
when both are abbreviated simultaneously under token pressure. The two are structurally
independent: blocking entries may be compressed; found timestamps may not. This guard
clause names the failure mode so that the rule is absorbed as a conditional constraint,
not merely noted as a positional instruction. If preamble placement is processed
without rule absorption, this guard in the STATUS execution note compensates.

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
timestamp isolation rule; the first is the inline annotation on the date field above,
and the preamble statement is the third. COMPRESSED-COLLAPSE GUARD: the specific
failure mode this note prevents is simultaneous compression of `found` and blocking
entries -- this guard names the failure mode so the rule is absorbed as a conditional
constraint rather than a positional note.

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
STORY owns cross-signal reasoning; every other block owns its own record. Zero-signal
synthesis mandate: if `found` is empty, question 1 must characterize what uniform
absence implies -- gap pattern as evidence set. This clause is the second structural
location for the zero-signal rule; the preamble statement is the first.

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

## V-02 -- Axis: Unified label without COMPRESSION-IMMUNE designation -- C-29 PASS, C-30 PASS, C-31 PARTIAL

**Hypothesis:** V-01 establishes the C-31-absent baseline with two rules in adjacent
preamble paragraphs (no unified header). V-02 adds a shared descriptive section header
-- "COMPRESSION-CRITICAL EXECUTION RULES" -- that groups both the ZERO-SIGNAL SYNTHESIS
RULE and the TIMESTAMP ISOLATION RULE under a named section in the preamble. Per-rule
TOKEN-PRESSURE GUARD and COMPRESSED-COLLAPSE GUARD are preserved unchanged. The section
header is descriptive: it names the rules as compression-critical but does not designate
the section as structurally immune to compression. The hypothesis: C-31 PASS requires
the explicit structural designation ("COMPRESSION-IMMUNE"), not merely a shared
descriptive label. The label unifies presentation but does not constitute a contractual
structural designation. Expected: 300/310 (C-31 PARTIAL -- label present, designation
absent). Falsification: if V-02 scores 310/310, any shared label satisfies C-31 --
the specific COMPRESSION-IMMUNE designation is not independently necessary.

Expected: 300/310 (C-31 PARTIAL -10)

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block -- an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. Every blocking gap must name the commit-risk --
what assumption the team is silently making if they ship today without that signal.

--- COMPRESSION-CRITICAL EXECUTION RULES ---

The following two rules govern execution under token pressure. Both apply
unconditionally -- they do not suspend when signals are present, when coverage is high,
or when blocking gaps are few. They are stated here, before phase execution begins,
so they are processed as global structural constraints before any per-block context
accumulates.

ZERO-SIGNAL SYNTHESIS RULE:

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
mode in which the model treats the rule as dormant because `found` is large.

Basis: uniform absence is itself evidence. The gap pattern defines what the team
does not know and why they are not ready. That pattern is the evidence set.

This rule is structurally distinct from the sparse-coverage rule (signals present
in only 1-2 namespaces). Both boundary conditions require synthesis. Neither permits
disclaimer substitution.

TIMESTAMP ISOLATION RULE:

Per-signal dates in the `found` section of STATUS are structurally separate from
blocking gap entries. Each signal in `found` must carry its own date at item level.
COMPRESSED format applies only to blocking entry verbosity -- it does not affect
found timestamps. Found timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count or token budget.

COMPRESSED-COLLAPSE GUARD: The specific failure mode this rule prevents is
COMPRESSED-collapse -- the model collapsing `found` signal entries into the blocking
gap summary when both are abbreviated simultaneously under token pressure. Blocking
entries may be compressed; found timestamps may not. This guard names the failure
mode so that the rule is absorbed as a conditional constraint, not merely a
positional instruction.

--- END COMPRESSION-CRITICAL EXECUTION RULES ---

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
TIMESTAMP ISOLATION (second location): per-signal dates in `found` are structurally
separate from blocking entries. COMPRESSED format applies only to blocking entry
verbosity -- `found` timestamps must not be collapsed regardless of blocking gap count.
See COMPRESSION-CRITICAL EXECUTION RULES above for the full rule statement and
COMPRESSED-COLLAPSE GUARD.

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
STORY owns cross-signal reasoning; every other block owns its own record. Zero-signal
synthesis mandate (second location): if `found` is empty, question 1 must characterize
what uniform absence implies. See COMPRESSION-CRITICAL EXECUTION RULES above.

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

## V-03 -- Axis: COMPRESSION-IMMUNE PREAMBLE designation without execution-note cross-reference -- C-29 PASS, C-30 PASS, C-31 PARTIAL or PASS (falsification test)

**Hypothesis:** V-02 tests a descriptive label (COMPRESSION-CRITICAL EXECUTION RULES)
without structural designation. V-03 introduces the explicit structural designation --
"COMPRESSION-IMMUNE PREAMBLE" -- as the section header. Both rules are consolidated
under this designation. Per-rule TOKEN-PRESSURE GUARD and COMPRESSED-COLLAPSE GUARD are
preserved. The isolation axis: execution notes in STATUS and STORY do NOT reference the
preamble section by its designation. There is no "see COMPRESSION-IMMUNE PREAMBLE" or
"second location; COMPRESSION-IMMUNE PREAMBLE is the first" cross-reference. The
designation exists at the preamble header level only. The hypothesis: if C-31 PASS
requires only the structural designation (not the cross-reference from execution notes),
V-03 scores 310/310. If C-31 PASS requires that execution notes acknowledge the
designated section (making the designation a self-referential structural contract across
both the preamble and the point-of-use), V-03 scores 300/310. This is the primary
falsification target for R12. Outcome drives whether V-05's cross-reference mechanism
adds independent structural protection or is decorative.

Expected: UNCERTAIN -- 300/310 (C-31 PARTIAL, cross-reference independently necessary)
or 310/310 (C-31 PASS, designation alone sufficient). Falsification resolves which.

---

You are running `campaign-brief` for topic: `{{topic}}`.

Output format: compact terminal dashboard. Prose is confined to the STORY block. All
other blocks are structured data. Do not add narrative commentary outside STORY.
Do not skip any block -- an absent block is an incomplete dashboard.

THE PRIMARY COMPETITOR IS INERTIA. Every blocking gap must name the commit-risk --
what assumption the team is silently making if they ship today without that signal.

=== COMPRESSION-IMMUNE PREAMBLE ===

This section is a structural contract. Both rules below must be applied regardless
of token budget, output length, blocking gap count, or coverage state. This section
is processed before any phase block is generated. The rules in this section are
not block-local -- they govern every block that follows.

ZERO-SIGNAL SYNTHESIS RULE:

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
unconditionally at any token budget. The rule is stated in this preamble section
regardless of current `found` coverage to prevent conditional-context suppression --
the failure mode in which the model treats the rule as dormant because `found` is large.
The guard is a structural firewall, not a conditional annotation.

Basis: uniform absence is itself evidence. The gap pattern defines what the team
does not know and why they are not ready. Both the zero-signal case and the
sparse-coverage case require synthesis; neither permits disclaimer substitution.

TIMESTAMP ISOLATION RULE:

Per-signal dates in the `found` section of STATUS are structurally separate from
blocking gap entries. Each signal in `found` must carry its own date at item level.
COMPRESSED format applies only to blocking entry verbosity -- it does not affect
found timestamps. Found timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count or token budget.

COMPRESSED-COLLAPSE GUARD: The specific failure mode this rule prevents is
COMPRESSED-collapse -- simultaneous compression of `found` entries and blocking gap
entries when token pressure activates the COMPRESSED branch. Blocking entries may
be compressed; found timestamps may not. Each mechanism in this dual-requirement
guards a distinct failure mode: preamble position (here, in this section) ensures
the rule is encountered before blocking-gap context accumulates; the declarative
guard clause (restated in the STATUS execution note) ensures the rule is absorbed
as a conditional constraint even if encountered without full absorption on first
pass.

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
TIMESTAMP ISOLATION: per-signal dates in `found` are structurally separate from
blocking entries. COMPRESSED format applies only to blocking entry verbosity --
`found` timestamps must not be collapsed regardless of blocking gap count. COMPRESSED-
COLLAPSE GUARD: this note names the COMPRESSED-collapse failure mode explicitly so the
rule is absorbed as a conditional constraint even if preamble placement was processed
without full absorption.

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
STORY owns cross-signal reasoning; every other block owns its own record. Zero-signal
synthesis mandate: if `found` is empty, question 1 must characterize what uniform
absence implies -- gap pattern as evidence set. This clause restates the rule from
the preamble above.

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

## V-04 -- Combined: Three compression-critical rules, distributed per-rule (scale test) -- C-29 PASS, C-30 PASS, C-31 PARTIAL

**Hypothesis:** V-01 through V-03 test C-31 in the two-rule case (C-29 + C-30 domains).
V-04 introduces a third compression-critical rule -- VERDICT action posture isolation
(C-26/C-28 domain) -- and applies the distributed per-rule dual-mechanism pattern to
all three rules: each rule occupies its own preamble paragraph with a positional
mechanism, and each has a per-rule declarative guard in its block execution note.
No COMPRESSION-IMMUNE PREAMBLE designation is applied. The inertia framing is
foregrounded: the preamble opens with the inertia frame before listing rules. The
hypothesis tests whether distributed dual-mechanism degrades at three-rule scale.
If V-04 scores 300/310 (C-31 PARTIAL), the three-rule distributed form holds C-29
and C-30 but cannot achieve C-31 -- consistent with V-01. If V-04 scores below 300
(e.g., 290 or 280), distributed dual-mechanism fails at three-rule scale, making
consolidation necessary on structural grounds independent of the C-31 explicit-
designation criterion. Combined axes: three-rule scale + inertia framing foregrounded.

Expected: 300/310 (C-31 PARTIAL -10; scale holds for C-29/C-30, designation absent)

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
guard is a structural firewall against the rule's suppression.

Basis: uniform absence is itself evidence. The gap pattern defines what the team
does not know and why they are not ready. Both zero-signal and sparse-coverage
boundary conditions require synthesis; neither permits disclaimer substitution.

TIMESTAMP ISOLATION RULE (global execution constraint -- applies to every run):

Per-signal dates in the `found` section of STATUS are structurally separate from
blocking gap entries. Each signal in `found` must carry its own date at item level.
COMPRESSED format applies only to blocking entry verbosity -- it does not affect
found timestamps. Found timestamps must not be collapsed, summarized, or omitted
regardless of blocking gap count or token budget. This rule is stated here, before
phase execution begins, so that it is processed as a global structural constraint
rather than as a block-local annotation that may be elided when compression activates.

COMPRESSED-COLLAPSE GUARD: The specific failure mode this rule prevents is COMPRESSED-
collapse -- simultaneous compression of `found` entries and blocking gap entries when
token pressure activates the COMPRESSED branch. Blocking entries may be compressed;
found timestamps may not. This guard names the failure mode so the rule is absorbed
as a conditional constraint, not merely a positional instruction. The preamble position
compensates if the STATUS execution note guard is elided; the execution note guard
compensates if preamble placement is processed without rule absorption.

VERDICT ACTION POSTURE RULE (global execution constraint -- applies to every run):

The `inertia_cost` field in the VERDICT block must classify aggregate commit risk by
recoverability at every verdict status -- READY, NOT READY, and CONDITIONAL. Two
postures are available: bounded (team can detect failure post-commit and course-correct
before propagation) and unbounded (failure propagates to irreversible state before
detection). The classification determines the action sub-label: "action: commit with
monitoring" for bounded; "action: do not commit until resolved" for unbounded. A VERDICT
block with inertia named but recoverability unclassified forces the team to re-read all
item-level gap entries to derive their commit posture -- the VERDICT is not actionable
on its own.

VERDICT COMPRESSION GUARD: The specific failure mode this rule prevents is VERDICT-
abbreviation -- the model omitting or hollowing the `action:` sub-label on `inertia_cost`
when COMPRESSED format has been active for STATUS and the model treats compression as
extending to VERDICT. VERDICT is never abbreviated. The `action:` sub-label is not
optional format; it is the structural field that makes VERDICT self-contained. This
guard names the VERDICT-abbreviation failure mode so the rule is absorbed as a
conditional constraint. The preamble position compensates if the VERDICT execution
note guard is elided under token pressure.

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
TIMESTAMP ISOLATION (second location): per-signal dates in `found` are structurally
separate from blocking entries. COMPRESSED format applies only to blocking entry
verbosity -- `found` timestamps must not be collapsed regardless of blocking gap count.
COMPRESSED-COLLAPSE GUARD: this note names the COMPRESSED-collapse failure mode
explicitly -- simultaneous compression of `found` and blocking entries. The preamble
statement is the first location; this is the second.

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
STORY owns cross-signal reasoning; every other block owns its own record. Zero-signal
synthesis mandate (second location): if `found` is empty, question 1 must characterize
what uniform absence implies -- gap pattern is the evidence set. The preamble statement
is the first location; this mandate is the second.

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
VERDICT COMPRESSION GUARD (second location): the `action:` sub-label on `inertia_cost`
is required regardless of COMPRESSED format state and regardless of token pressure.
VERDICT is never abbreviated. If COMPRESSED was active for blocking entries, it does
not extend to VERDICT fields. A CONDITIONAL verdict must name the condition and what
satisfies it; its `inertia_cost` must include the `action:` sub-label specifying posture
for the unresolved risk period. The preamble statement is the first location for the
VERDICT ACTION POSTURE RULE; this is the second.

---

Write all blocks as a single artifact to:
`simulations/{{topic}}/campaign-brief-{{date}}.md`

Block order: TOPIC, DELTA, STRATEGY, STATUS, [BLOCKING-DETAIL if triggered],
CONFIDENCE, STORY, VERDICT.

---

## V-05 -- Combined: Full C-31 PASS -- COMPRESSION-IMMUNE PREAMBLE designation + execution-note cross-references -- C-29 PASS, C-30 PASS, C-31 PASS

**Hypothesis:** V-01 establishes distributed per-rule dual-mechanism at 300/310 (C-31
PARTIAL). V-03 tests whether designation alone (no cross-reference) achieves C-31 PASS.
V-05 tests the full C-31 contract: explicit COMPRESSION-IMMUNE PREAMBLE section
designation + execution notes in STATUS and STORY that reference the preamble section
by its structural designation. The cross-reference creates a bidirectional structural
contract: the preamble declares structural immunity; the execution notes acknowledge the
preamble as the authoritative statement of the rules they implement. This mirrors how
a function call references a specification rather than restating it inline -- the
execution note becomes a pointer to the structural contract, not a redundant prose
restatement. The hypothesis: V-05 scores 310/310, establishing the ceiling. If
V-03 also scores 310/310, the cross-reference is decorative and V-05 and V-03 are
equivalent. If V-03 scores 300/310 and V-05 scores 310/310, the cross-reference
is independently necessary for C-31 PASS. Combined axes: COMPRESSION-IMMUNE designation
+ execution-note cross-reference + inertia framing foregrounded.

Expected: 310/310 (C-29 PASS, C-30 PASS, C-31 PASS)

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
