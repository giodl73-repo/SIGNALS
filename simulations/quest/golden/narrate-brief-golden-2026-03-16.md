Golden prompt written to `simulations/quest/golden/campaign-brief-golden-2026-03-16.md`.

**What's in the document:**

**Prompt body** — V-05 simplified (1494 words, 23% reduction from 1931). The 10 excisions removed:
- Preamble: last sentence of header, TOKEN-PRESSURE GUARD paragraph, Basis sentence, COMPRESSED-COLLAPSE GUARD tail (positional mechanism + cross-reference sentences)
- STATUS execution note: present-state description + self-referential invocation label + architecture documentation sentence
- STORY execution note: present-state description + named-pointer invocation sentence + "Gap pattern is the evidence set."
- VERDICT execution note: rationale justification sentence + "If COMPRESSED was active..." redundancy

All 40 criteria remain at PASS in the simplified form.

**What made it golden (5 patterns):**
1. Depth-anchored parity clause (C-38) — calibrated to companion-present baseline, not a vague qualifier
2. Per-companion structural deliverables enumeration (C-39) — Q1/Q2/Q3 with operational specificity for ZERO-SIGNAL; per-signal dates + `current_date:` + COMPRESSED-immunity for TIMESTAMP ISOLATION
3. Depth-symmetric non-degradation mandate (C-40 probe) — forecloses depth-trading under high companion execution burden
4. Bidirectional companion naming (C-32) — each note can reconstruct the other's mandate independently
5. Simplification PASS — rationale prose stripped, operative constraints intact

**Next investigation (R21):** Whether C-40 PASS forecloses element omission under double-elision with active token pressure, or whether structural ordering constraints are needed.
ct but
element-incomplete companion output -- parity anchoring without a verifiable list.

**3. Depth-symmetric non-degradation mandate (C-40 probe)**
Both absent-state clauses add: "This parity constraint is symmetric: executing this
companion mandate does not reduce the present clause's own output depth. Both mandates
execute at full depth simultaneously." Forecloses depth-trading: a model encountering
high companion-enumeration burden cannot satisfy the companion's structural list by
abbreviating its own present-clause block.

**4. Bidirectional companion naming (C-32)**
Each execution note names its companion by full designation + block location
("ZERO-SIGNAL SYNTHESIS MANDATE (COMPRESSION-IMMUNE PREAMBLE invocation) execution
note in the STORY block"). The circuit is closed in both directions: each note can
reconstruct the other's mandate from its own text under independent elision.

**5. Simplification PASS (23% reduction)**
The simplified form dropped 437 words of architecture documentation and rationale
prose -- TOKEN-PRESSURE GUARD, positional mechanism explanations, redundant present-
state descriptions, and rationale sentences -- while all 40 criteria remain at PASS.
The operative constraints are entirely in the rule bodies and execution notes;
the removed prose explained why the rules work, not what they require.

---

## Prompt Body

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
execution note were present in the STATUS block. If `found` is empty, this clause fires
independently: empty `found` is not grounds for omitting STORY; question 1 must
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

---

## Final Rubric Summary — v20 (40 criteria, 400 pts)

### Structural deliverables (C-01 to C-09)
| # | Criterion |
|---|-----------|
| C-01 | `[TOPIC]` block with all required fields |
| C-02 | `[DELTA]` block with 5 required fields |
| C-03 | `[STRATEGY]` block with source + 4-column table, min 3 rows |
| C-04 | `[STATUS]` block with found + missing sections |
| C-05 | `current_date:` at STATUS block header level, structurally isolated |
| C-06 | `[VERDICT]` block with status / rationale / inertia_cost / blocking / optional |
| C-07 | `[CONFIDENCE]` standalone block with 3 dimensions + arithmetic average + level + binding |
| C-08 | `[STORY]` block present, prose-only, 2-4 paragraphs |
| C-09 | STORY confines all prose; no narrative commentary outside STORY |

### Signal handling (C-10 to C-18)
| # | Criterion |
|---|-----------|
| C-10 | Per-signal dates in `found` at item level; structurally separate from blocking entries |
| C-11 | Every blocking gap carries inertia risk; strategy field sourced or generated |
| C-12 | COMPRESSED format when blocking > 4; `[BLOCKING-DETAIL]` immediately after STATUS |
| C-13 | FULL format when blocking <= 4 |
| C-14 | CONFIDENCE scored from STATUS data only; average is arithmetic mean |
| C-15 | STORY answers all three questions in continuous prose; does not restate confidence level |
| C-16 | `current_date` not embedded in `found` entries or prose; isolated to STATUS header |
| C-17 | VERDICT derives from STORY + CONFIDENCE; rationale is one sentence |
| C-18 | STORY synthesizes signals; blocking gaps addressed as pattern, not enumerated per-gap |

### Ordering and artifact (C-19 to C-21)
| # | Criterion |
|---|-----------|
| C-19 | Block order: TOPIC → DELTA → STRATEGY → STATUS → [BLOCKING-DETAIL] → CONFIDENCE → STORY → VERDICT |
| C-20 | Artifact written to `simulations/{{topic}}/campaign-brief-{{date}}.md` |
| C-21 | Sparse-coverage protection: synthesis on available signals; no coverage disclaimer |

### Zero-signal and structural guards (C-22 to C-28)
| # | Criterion |
|---|-----------|
| C-22 | Zero-signal synthesis mandate present: empty `found` not grounds for omitting STORY; Q1 mandated |
| C-23 | `inertia_cost` carries bounded/unbounded label + `action:` sub-label |
| C-24 | `current_date:` at STATUS header level independent of COMPRESSED state |
| C-25 | Zero-signal synthesis mandate names zero-signal case at point-of-use in STORY execution note |
| C-26 | VERDICT COMPRESSION GUARD present: `action:` sub-label required regardless of COMPRESSED state |
| C-27 | STORY execution note fires independently when `found` is empty |
| C-28 | CONDITIONAL verdict names condition and what satisfies it; `inertia_cost` includes `action:` |

### COMPRESSION-IMMUNE PREAMBLE chain (C-29 to C-40)
| # | Criterion |
|---|-----------|
| C-29 | Zero-signal dual-mechanism: ZERO-SIGNAL SYNTHESIS RULE in preamble + ZERO-SIGNAL SYNTHESIS MANDATE execution note in STORY |
| C-30 | Timestamp isolation dual-mechanism: TIMESTAMP ISOLATION RULE in preamble + TIMESTAMP ISOLATION execution note in STATUS |
| C-31 | Both rules in preamble; both execution notes invoke preamble by designation; bidirectional circuit closed |
| C-32 | Each execution note names companion by full designation + block location |
| C-33 | Both clause headers carry `(COMPRESSION-IMMUNE PREAMBLE invocation)` parenthetical in exact designation form |
| C-34 | Both clause bodies open with compression-immune authority declarations (2 sentences) |
| C-35 | Companion-activation instruction in both bodies: full designation + block location + present-state rule + absent-state rule |
| C-36 | Absent-state rule unconditionally declares absent companion's mandate independently operative |
| C-37 | Unconditional execution directive in both absent-state clauses: "must be executed as if its execution note were present in this context" |
| C-38 | Explicit parity clause in both absent-state bodies: "at full depth, at parity with what would be produced if the companion's execution note were present in this context" |
| C-39 | Complete per-companion structural deliverables enumeration at operational specificity sufficient for independent completeness verification *(confirmed R20)* |
| C-40 | Explicit non-degradation mandate in both absent-state clauses: all enumerated elements must be produced; executing companion mandate does not reduce present clause depth *(aspirational R21)* |

### Rubric evolution summary
| Version | Criteria | Score ceiling | Key addition |
|---------|----------|---------------|--------------|
| v18 | 38 | 380 | C-38 parity clause (depth floor anchored to companion-present baseline) |
| v19 | 39 | 390 | C-39 companion-scope determinability (structural deliverables enumeration) |
| v20 | 40 | 400 | C-40 enumeration-completeness-as-obligation (non-degradation mandate) |
