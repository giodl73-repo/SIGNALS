---
skill: quest-variate
skill_target: topic-achievements
round: 6
date: 2026-03-17
rubric_version: 6
basis: R5 V-05 (Golden Synthesis) passes C-01 through C-19 under the v5 rubric. Under v6,
       two new aspirational criteria are added: C-20 (gate completion output schema declared)
       and C-21 (uniform gate architecture — no ungated phases). Analysis of R5 V-05 against
       v6 shows: all 4 phases are gated (C-21 baseline met), and all 4 gates carry labeled
       output templates (C-20 baseline met at varying precision). However, schema precision
       varies across gates — SCAN GATE schema has two fields (count + floor prose), WRITE GATE
       has one field (artifact path). Neither declares a structured verifiable schema in the
       sense C-20 intends ("verifiable by inspection against a known format"). R5 V-05 also
       declares schemas terminally (gate output block appears at the END of each phase, after
       the phase instructions). The question is whether schema preface placement, upfront gate
       registry, or explicit fail-surface closure produces stronger or more reliably verifiable
       C-20 compliance. R6 isolates three new axis dimensions: (1) lifecycle emphasis — schema
       preface (gate schema declared BEFORE phase instructions, as goal state); (2) output
       format — gate registry table (all 4 gate schemas declared in a single pre-printed table
       at prompt preamble before any phase begins); (3) phrasing register — fail-surface closure
       (each gate schema includes explicit FAIL conditions — what does NOT clear the gate —
       alongside the PASS format). All R5 V-05 baseline wins (C-01 through C-19, session
       invariants A-D, pre-printed Falsified contract, pre-printed table skeleton, CLASSIFY
       before STATE) are preserved as baseline across all variations.
---

# Variate R6 — topic-achievements

5 complete prompt body variations for the `topic-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Targets | Used In |
|------|---------|---------|
| Lifecycle emphasis (schema preface — gate schema declared BEFORE phase instructions) | C-20 | V-01, V-04, V-05 |
| Output format (gate registry table — all 4 gates and schemas declared upfront) | C-21, C-20 | V-02, V-04, V-05 |
| Phrasing register (fail-surface closure — explicit FAIL conditions per gate schema) | C-20 | V-03, V-04, V-05 |

---

## V-01 — Lifecycle Emphasis: Schema Preface

**Axis**: Lifecycle emphasis
**Hypothesis**: R5 variations declare gate schemas terminally — the output template appears
at the END of each phase section, after all instructions. This means the model executes
the phase before encountering the schema it must produce, treating the schema as a format
reminder rather than a goal state. V-01 inverts this: each phase section opens with a
`GATE SCHEMA:` block declaring the exact output required to clear the gate, BEFORE the
phase instructions begin. The model reads what it must produce before it starts working.
This tests whether schema preface placement produces more reliable and precise C-20
compliance than terminal placement. C-21 is achieved by uniform 4-phase gate architecture
(all phases gate-labeled). The pre-printed Falsified template and session invariants from
R5 V-05 are preserved at baseline.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout all phases:**

Invariant A (State): Each achievement row carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values. No combined states.

Invariant B (Floor): Namespace-level evidence from the `prove` namespace is always
acceptable and is the safe floor for the Falsified achievement. Any prove artifact
containing a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS.
No full synthesis required.

Invariant C (Citation): EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`.
LOCKED rows name the exact artifact type or count required.

Invariant D (Preservation): The achievement table template in Phase 3 contains pre-printed
compliance text — in the Falsified row and in LOCKED cell detail. Do not rewrite, rephrase,
or restructure that pre-printed text. Fill only the placeholders as instructed.

---

### PHASE 1 — SCAN

**SCAN GATE schema** — produce this output to clear this gate, before Phase 2 begins:

```
SCAN GATE CLEARED
Artifacts: [n]
Floor: active — Invariant B applies
```

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract:
- Filename
- Skill (from `skill:` frontmatter or filename)
- Namespace prefix (first segment of skill name)
- Date (from `date:` frontmatter or filename)
- Contributor (`contributor:` or `author:` frontmatter, or "not set")

If n = 0: produce the SCAN GATE schema above with n=0. All STATE cells will be LOCKED in
Phase 3. Proceed.

---

### PHASE 2 — CLASSIFY

Entry condition: SCAN GATE CLEARED output present.

**CLASSIFY GATE schema** — produce this output to clear this gate, before Phase 3 begins.
All 7 category lines are required; a summary count alone does not clear this gate:

```
CLASSIFY GATE CLEARED
Exploration: [list of qualifying artifact filenames, or "none"]
Depth: [n] artifacts
Coverage: [list of namespace prefixes] — [n] of 9
Quality (Falsified candidates): [list of qualifying artifact filenames, or "none"]
Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
Discovery: [list of qualifying artifact filenames, or "none"]
Corps/Crew: contributors [list or "none"] — count [n]
[n] of 7 categories have at least one artifact.
```

Assign each artifact from Phase 1 to exactly one category. Do not assign states.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis, then prove-websearch or prove-intelligence, then prove-synthesize |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values |

---

### PHASE 3 — FILL TEMPLATE

Entry condition: CLASSIFY GATE CLEARED output present.

**STATE GATE schema** — produce this output to clear this gate, before Phase 4 begins:

```
STATE GATE CLEARED
EARNED: [n]
IN-PROGRESS: [n]
LOCKED: [n]
All 7 rows filled. Invariants A–D applied.
```

Fill every `[PLACEHOLDER]` in the template below. Apply Invariant D: do not rewrite any
pre-printed text in this template. Apply Invariants A, B, C to every row. EARNED: fill
`[EARNED_ARTIFACT]` with `filename — date`. IN-PROGRESS: fill `[N]` and `[M]` with actual
counts. LOCKED: the detail text is pre-printed; fill only `[SPECIFIC_GAP]`.

```markdown
## topic-achievements — {{topic}}
_Scanned: {{date}} — Total artifacts: [TOTAL_COUNT]_

| Category | Achievement | State | Detail |
|----------|-------------|-------|--------|
| Exploration | Spark | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 1 artifact / LOCKED: File any one artifact for topic `{{topic}}` using any Signal skill |
| Depth | Signal Depth | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] artifacts — earliest [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 5 artifacts / LOCKED: File 5 total artifacts for topic `{{topic}}` across any Signal skills |
| Coverage | Namespace Sweep | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] of 9 namespaces — [LIST_NAMESPACES] / IN-PROGRESS: [N] of 5 namespaces — missing: [LIST_MISSING] / LOCKED: File artifacts from 5 of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) |
| Quality | Falsified | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] — followed evidence over assumptions: [REVISION_EVENT] / IN-PROGRESS: [N] of [M] prove artifacts contain counter-signals — not yet synthesized / LOCKED: File a prove-synthesize or topic-echo artifact that records a hypothesis revision. Framing falsification as absence or as a result the investigation did not yield — including as a closing reflection — does not earn this achievement. Namespace-level evidence from the prove namespace is always acceptable and is the safe floor. |
| Chain | Hypothesis Chain | [EARNED / IN-PROGRESS / LOCKED] | EARNED: prove-hypothesis [DATE1] → prove-evidence [DATE2] → prove-synthesize [DATE3] / IN-PROGRESS: [N] of 3 chain links — missing: [LIST_MISSING_LINKS] / LOCKED: File prove-hypothesis, then prove-websearch or prove-intelligence, then prove-synthesize — in that order |
| Discovery | Echo Filed | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: topic-echo started but not finalized / LOCKED: Run /topic-echo to produce `{{topic}}-echo-{{date}}.md` |
| Corps/Crew | Team Contribution | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] contributors — [LIST_CONTRIBUTORS] — first joint artifact: [DATE] / IN-PROGRESS: [N] of 2 contributors active — second contributor needed / LOCKED: A second team member files any artifact for topic `{{topic}}` |

## Next Action

Run `/[SKILL]` to produce `{{topic}}-[ITEM]-{{date}}.md`.
This advances [CATEGORY: ACHIEVEMENT] from [CURRENT_STATE] toward [TARGET_STATE].
Why: [SPECIFIC_GAP — one sentence linking to the CLASSIFY GATE output].
```

---

### PHASE 4 — WRITE ARTIFACT

Entry condition: STATE GATE CLEARED output present.

**WRITE GATE schema** — produce this output to clear this gate:

```
WRITE GATE CLEARED
Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md
Phases completed: 4
```

Write the filled template to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [TOTAL_COUNT]
phases_completed: 4
earned: [n from STATE GATE]
in_progress: [n from STATE GATE]
locked: [n from STATE GATE]
---
```

---

## V-02 — Output Format: Gate Registry Table

**Axis**: Output format
**Hypothesis**: R5 variations declare gate schemas inline within each phase section — to
see all 4 gate schemas, the model must read through the entire prompt. A gate registry
table at the prompt preamble pre-prints all 4 gate names and their required output schemas
in a single visible block before any phase begins. This achieves two things simultaneously:
C-21 — all 4 phases are named as gates before phase 1 starts, making the uniform gate
architecture visible at the outset; and C-20 — all 4 gate schemas are declared upfront,
so no gate schema is discoverable only mid-execution. The model can check any gate's schema
without scanning through the prompt. This tests whether registry-based pre-declaration
produces stronger C-20/C-21 compliance than per-phase inline declaration. Gate schemas
in the registry are authoritative; per-phase gate instructions reference the registry.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout:**

Invariant A (State): Each achievement row carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values.

Invariant B (Floor): Namespace-level evidence from the `prove` namespace is always
acceptable and is the safe floor for the Falsified achievement. Any prove artifact
containing a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS.
No full synthesis required.

Invariant C (Citation): EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`.
LOCKED rows name the exact artifact type or count required.

Invariant D (Preservation): The Falsified row and LOCKED cell text in the Phase 3 template
are pre-printed. Do not rewrite, rephrase, or restructure that text. Fill only placeholders.

---

**Gate Registry** — all 4 phase gates and their required output schemas:

| Phase | Gate | Required output to clear (schema) |
|-------|------|-----------------------------------|
| 1 — SCAN | SCAN GATE | `SCAN GATE CLEARED` / `Artifacts: [n]` / `Floor: active` |
| 2 — CLASSIFY | CLASSIFY GATE | `CLASSIFY GATE CLEARED` / one line per category: `Exploration: [list or "none"]`, `Depth: [n] artifacts`, `Coverage: [namespaces] — [n] of 9`, `Quality: [list or "none"]`, `Chain: hypothesis [p/a] — evidence [p/a] — synthesize [p/a]`, `Discovery: [list or "none"]`, `Corps/Crew: contributors [list] — count [n]` / `[n] of 7 categories populated` |
| 3 — FILL | STATE GATE | `STATE GATE CLEARED` / `EARNED: [n]` / `IN-PROGRESS: [n]` / `LOCKED: [n]` / `All 7 rows filled. Invariants A–D applied.` |
| 4 — WRITE | WRITE GATE | `WRITE GATE CLEARED` / `Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md` |

A phase is not complete until its gate schema output (as declared in this registry) is
produced. Phases must be completed in order. An entry condition for Phase N is the
gate output of Phase N-1.

---

### PHASE 1 — SCAN GATE

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract: filename, skill,
namespace prefix, date, contributor.

Produce the SCAN GATE schema from the registry above.

If n = 0: produce the gate output with n=0. All STATE cells will be LOCKED in Phase 3.

---

### PHASE 2 — CLASSIFY GATE

Entry condition: SCAN GATE output produced.

Assign each artifact from Phase 1 to exactly one category. Do not assign states.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis + (prove-websearch or prove-intelligence) + prove-synthesize |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values |

Produce the CLASSIFY GATE schema from the registry above. All 7 category lines and the
summary count line are required. A count line without category lines does not match the
registry schema and does not clear this gate.

---

### PHASE 3 — FILL TEMPLATE (STATE GATE)

Entry condition: CLASSIFY GATE output produced.

Fill every `[PLACEHOLDER]` in the template below. Apply Invariant D: do not rewrite any
pre-printed text. Apply Invariants A, B, C to every row.

```markdown
## topic-achievements — {{topic}}
_Scanned: {{date}} — Total artifacts: [TOTAL_COUNT]_

| Category | Achievement | State | Detail |
|----------|-------------|-------|--------|
| Exploration | Spark | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 1 artifact / LOCKED: File any one artifact for topic `{{topic}}` using any Signal skill |
| Depth | Signal Depth | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] artifacts — earliest [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 5 artifacts / LOCKED: File 5 total artifacts for topic `{{topic}}` across any Signal skills |
| Coverage | Namespace Sweep | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] of 9 namespaces — [LIST_NAMESPACES] / IN-PROGRESS: [N] of 5 namespaces — missing: [LIST_MISSING] / LOCKED: File artifacts from 5 of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) |
| Quality | Falsified | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] — followed evidence over assumptions: [REVISION_EVENT] / IN-PROGRESS: [N] of [M] prove artifacts contain counter-signals — not yet synthesized / LOCKED: File a prove-synthesize or topic-echo artifact that records a hypothesis revision. Framing falsification as absence or as a result the investigation did not yield — including as a closing reflection — does not earn this achievement. Namespace-level evidence from the prove namespace is always acceptable and is the safe floor. |
| Chain | Hypothesis Chain | [EARNED / IN-PROGRESS / LOCKED] | EARNED: prove-hypothesis [DATE1] → prove-evidence [DATE2] → prove-synthesize [DATE3] / IN-PROGRESS: [N] of 3 chain links — missing: [LIST_MISSING_LINKS] / LOCKED: File prove-hypothesis, then prove-websearch or prove-intelligence, then prove-synthesize — in that order |
| Discovery | Echo Filed | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: topic-echo started but not finalized / LOCKED: Run /topic-echo to produce `{{topic}}-echo-{{date}}.md` |
| Corps/Crew | Team Contribution | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] contributors — [LIST_CONTRIBUTORS] — first joint artifact: [DATE] / IN-PROGRESS: [N] of 2 contributors active — second contributor needed / LOCKED: A second team member files any artifact for topic `{{topic}}` |

## Next Action

Run `/[SKILL]` to produce `{{topic}}-[ITEM]-{{date}}.md`.
This advances [CATEGORY: ACHIEVEMENT] from [CURRENT_STATE] toward [TARGET_STATE].
Why: [SPECIFIC_GAP — one sentence linking to the CLASSIFY GATE output].
```

Produce the STATE GATE schema from the registry above.

---

### PHASE 4 — WRITE GATE

Entry condition: STATE GATE output produced.

Write the filled template to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [TOTAL_COUNT]
phases_completed: 4
earned: [n from STATE GATE]
in_progress: [n from STATE GATE]
locked: [n from STATE GATE]
---
```

Produce the WRITE GATE schema from the registry above.

---

## V-03 — Phrasing Register: Fail-Surface Closure

**Axis**: Phrasing register
**Hypothesis**: R5 gate schemas are positive-only — they specify what the gate output must
contain (PASS format) but say nothing about what fails. A gate that says "produce all 7
category lines" is weaker than a gate that also says "a summary count without category lines
does not clear this gate." V-03 adds explicit FAIL conditions to every gate schema: each
gate block contains a `PASS:` format specification and a `FAIL:` list of specific output
shapes that do NOT clear the gate. The model must navigate around named failure modes. This
tests whether fail-surface closure creates stronger C-20 compliance — making the schema
truly "verifiable by inspection" in both directions — than PASS-only schemas. C-21 is
achieved by uniform 4-phase gate architecture. No gate schema is purely positive.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout:**

Invariant A (State): Each achievement row carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values.

Invariant B (Floor): Namespace-level evidence from the `prove` namespace is always
acceptable and is the safe floor for the Falsified achievement. Any prove artifact
containing a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS.
No full synthesis required.

Invariant C (Citation): EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`.
LOCKED rows name the exact artifact type or count required.

Invariant D (Preservation): The Falsified row and LOCKED cell text in the Phase 3 template
are pre-printed. Do not rewrite, rephrase, or restructure that text. Fill only placeholders.

---

### PHASE 1 — SCAN GATE

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract: filename, skill,
namespace prefix, date, contributor.

**SCAN GATE contract:**

PASS — output contains exactly these lines:
```
SCAN GATE CLEARED
Artifacts: [n]
Floor: active — Invariant B applies
```

FAIL — any of the following does not clear this gate:
- Missing "SCAN GATE CLEARED" label
- Missing artifact count line
- Count and listed artifacts inconsistent
- Gate label present but no artifact count

---

### PHASE 2 — CLASSIFY GATE

Entry condition: SCAN GATE CLEARED produced.

Assign each artifact from Phase 1 to exactly one category. Do not assign states.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis + (prove-websearch or prove-intelligence) + prove-synthesize |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values |

**CLASSIFY GATE contract:**

PASS — output contains "CLASSIFY GATE CLEARED" followed by all 7 category lines and summary:
```
CLASSIFY GATE CLEARED
Exploration: [list or "none"]
Depth: [n] artifacts
Coverage: [namespaces list] — [n] of 9
Quality (Falsified candidates): [list or "none"]
Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
Discovery: [list or "none"]
Corps/Crew: contributors [list or "none"] — count [n]
[n] of 7 categories have at least one artifact.
```

FAIL — any of the following does not clear this gate:
- Only a count line ("3 of 7 categories populated") without the 7 labeled category lines
- Any category line missing (even if the category has "none")
- Summary count present but category lines absent or partial
- State assignments present (classify does not assign states)
- Gate label present but category lines absent

---

### PHASE 3 — FILL TEMPLATE (STATE GATE)

Entry condition: CLASSIFY GATE CLEARED produced.

Fill every `[PLACEHOLDER]` in the template below. Apply Invariant D. Apply Invariants A, B, C.

```markdown
## topic-achievements — {{topic}}
_Scanned: {{date}} — Total artifacts: [TOTAL_COUNT]_

| Category | Achievement | State | Detail |
|----------|-------------|-------|--------|
| Exploration | Spark | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 1 artifact / LOCKED: File any one artifact for topic `{{topic}}` using any Signal skill |
| Depth | Signal Depth | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] artifacts — earliest [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 5 artifacts / LOCKED: File 5 total artifacts for topic `{{topic}}` across any Signal skills |
| Coverage | Namespace Sweep | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] of 9 namespaces — [LIST_NAMESPACES] / IN-PROGRESS: [N] of 5 namespaces — missing: [LIST_MISSING] / LOCKED: File artifacts from 5 of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) |
| Quality | Falsified | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] — followed evidence over assumptions: [REVISION_EVENT] / IN-PROGRESS: [N] of [M] prove artifacts contain counter-signals — not yet synthesized / LOCKED: File a prove-synthesize or topic-echo artifact that records a hypothesis revision. Framing falsification as absence or as a result the investigation did not yield — including as a closing reflection — does not earn this achievement. Namespace-level evidence from the prove namespace is always acceptable and is the safe floor. |
| Chain | Hypothesis Chain | [EARNED / IN-PROGRESS / LOCKED] | EARNED: prove-hypothesis [DATE1] → prove-evidence [DATE2] → prove-synthesize [DATE3] / IN-PROGRESS: [N] of 3 chain links — missing: [LIST_MISSING_LINKS] / LOCKED: File prove-hypothesis, then prove-websearch or prove-intelligence, then prove-synthesize — in that order |
| Discovery | Echo Filed | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: topic-echo started but not finalized / LOCKED: Run /topic-echo to produce `{{topic}}-echo-{{date}}.md` |
| Corps/Crew | Team Contribution | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] contributors — [LIST_CONTRIBUTORS] — first joint artifact: [DATE] / IN-PROGRESS: [N] of 2 contributors active — second contributor needed / LOCKED: A second team member files any artifact for topic `{{topic}}` |

## Next Action

Run `/[SKILL]` to produce `{{topic}}-[ITEM]-{{date}}.md`.
This advances [CATEGORY: ACHIEVEMENT] from [CURRENT_STATE] toward [TARGET_STATE].
Why: [SPECIFIC_GAP — one sentence linking to the CLASSIFY GATE output].
```

**STATE GATE contract:**

PASS — output contains:
```
STATE GATE CLEARED
EARNED: [n]
IN-PROGRESS: [n]
LOCKED: [n]
All 7 rows filled. Invariants A–D applied.
```

FAIL — any of the following does not clear this gate:
- Missing numeric counts (qualitative summary only)
- EARNED + IN-PROGRESS + LOCKED counts do not sum to 7
- Missing "All 7 rows filled" confirmation
- Gate label present but state counts absent

---

### PHASE 4 — WRITE GATE

Entry condition: STATE GATE CLEARED produced.

Write the filled template to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [TOTAL_COUNT]
phases_completed: 4
earned: [n from STATE GATE]
in_progress: [n from STATE GATE]
locked: [n from STATE GATE]
---
```

**WRITE GATE contract:**

PASS — output contains:
```
WRITE GATE CLEARED
Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md
```

FAIL — any of the following does not clear this gate:
- Missing "WRITE GATE CLEARED" label
- Artifact path absent or path is wrong topic/date
- Gate label present but path absent

---

## V-04 — Combination: Gate Registry Table + Fail-Surface Closure

**Axes**: Output format (gate registry table) + phrasing register (FAIL conditions per gate)
**Hypothesis**: V-02 establishes the gate architecture visibility upfront (registry table)
but uses positive-only schemas; V-03 adds FAIL conditions but declares schemas inline
per-phase. V-04 combines: the registry table at the prompt preamble declares all 4 gate
schemas with PASS formats, and each per-phase gate block adds the FAIL conditions for that
gate. The registry gives C-21 structural visibility before Phase 1 begins; the per-phase
FAIL conditions close the failure surfaces that positive-only schemas leave open for C-20.
C-20 is now satisfied by two mechanisms simultaneously: the registry declares the structure
(what a gate output looks like), and the per-phase FAIL block declares what does not match
(what would fail inspection). Pre-printed Falsified template and session invariants A-D
preserved from R5 V-05.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout:**

Invariant A (State): Each achievement row carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values.

Invariant B (Floor): Namespace-level evidence from the `prove` namespace is always
acceptable and is the safe floor for the Falsified achievement. Any prove artifact
containing a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS.
No full synthesis required.

Invariant C (Citation): EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`.
LOCKED rows name the exact artifact type or count required.

Invariant D (Preservation): The Falsified row and LOCKED cell text in the Phase 3 template
are pre-printed. Do not rewrite, rephrase, or restructure that text. Fill only placeholders.

---

**Gate Registry** — all 4 phases are gated. PASS schema for each:

| Phase | Gate | PASS schema |
|-------|------|-------------|
| 1 — SCAN | SCAN GATE | `SCAN GATE CLEARED` / `Artifacts: [n]` / `Floor: active` |
| 2 — CLASSIFY | CLASSIFY GATE | `CLASSIFY GATE CLEARED` / 7 labeled category lines / `[n] of 7 categories populated` |
| 3 — FILL | STATE GATE | `STATE GATE CLEARED` / `EARNED: [n]` / `IN-PROGRESS: [n]` / `LOCKED: [n]` / `All 7 rows filled. Invariants A–D applied.` |
| 4 — WRITE | WRITE GATE | `WRITE GATE CLEARED` / `Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md` |

A phase is not complete until its gate schema output is produced as declared above.

---

### PHASE 1 — SCAN GATE

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract: filename, skill,
namespace prefix, date, contributor.

Produce the SCAN GATE PASS schema from the registry.

FAIL — does not clear SCAN GATE:
- Missing artifact count
- Count inconsistent with listed artifacts
- Gate label present but count absent

If n = 0: produce gate output with n=0; all STATE cells LOCKED in Phase 3.

---

### PHASE 2 — CLASSIFY GATE

Entry condition: SCAN GATE CLEARED produced.

Assign each artifact from Phase 1 to exactly one category. Do not assign states.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis + (prove-websearch or prove-intelligence) + prove-synthesize |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values |

Produce the CLASSIFY GATE PASS schema from the registry. All 7 labeled category lines and
the summary count are required.

FAIL — does not clear CLASSIFY GATE:
- Summary count only, without the 7 labeled category lines
- Any category line missing (even if "none")
- State assignments included (classify does not assign states)
- Gate label present but category lines absent

---

### PHASE 3 — FILL TEMPLATE (STATE GATE)

Entry condition: CLASSIFY GATE CLEARED produced.

Fill every `[PLACEHOLDER]` in the template below. Apply Invariant D. Apply Invariants A, B, C.

```markdown
## topic-achievements — {{topic}}
_Scanned: {{date}} — Total artifacts: [TOTAL_COUNT]_

| Category | Achievement | State | Detail |
|----------|-------------|-------|--------|
| Exploration | Spark | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 1 artifact / LOCKED: File any one artifact for topic `{{topic}}` using any Signal skill |
| Depth | Signal Depth | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] artifacts — earliest [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 5 artifacts / LOCKED: File 5 total artifacts for topic `{{topic}}` across any Signal skills |
| Coverage | Namespace Sweep | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] of 9 namespaces — [LIST_NAMESPACES] / IN-PROGRESS: [N] of 5 namespaces — missing: [LIST_MISSING] / LOCKED: File artifacts from 5 of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) |
| Quality | Falsified | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] — followed evidence over assumptions: [REVISION_EVENT] / IN-PROGRESS: [N] of [M] prove artifacts contain counter-signals — not yet synthesized / LOCKED: File a prove-synthesize or topic-echo artifact that records a hypothesis revision. Framing falsification as absence or as a result the investigation did not yield — including as a closing reflection — does not earn this achievement. Namespace-level evidence from the prove namespace is always acceptable and is the safe floor. |
| Chain | Hypothesis Chain | [EARNED / IN-PROGRESS / LOCKED] | EARNED: prove-hypothesis [DATE1] → prove-evidence [DATE2] → prove-synthesize [DATE3] / IN-PROGRESS: [N] of 3 chain links — missing: [LIST_MISSING_LINKS] / LOCKED: File prove-hypothesis, then prove-websearch or prove-intelligence, then prove-synthesize — in that order |
| Discovery | Echo Filed | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: topic-echo started but not finalized / LOCKED: Run /topic-echo to produce `{{topic}}-echo-{{date}}.md` |
| Corps/Crew | Team Contribution | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] contributors — [LIST_CONTRIBUTORS] — first joint artifact: [DATE] / IN-PROGRESS: [N] of 2 contributors active — second contributor needed / LOCKED: A second team member files any artifact for topic `{{topic}}` |

## Next Action

Run `/[SKILL]` to produce `{{topic}}-[ITEM]-{{date}}.md`.
This advances [CATEGORY: ACHIEVEMENT] from [CURRENT_STATE] toward [TARGET_STATE].
Why: [SPECIFIC_GAP — one sentence linking to the CLASSIFY GATE output].
```

Produce the STATE GATE PASS schema from the registry.

FAIL — does not clear STATE GATE:
- Numeric counts absent (n EARNED, n IN-PROGRESS, n LOCKED required)
- Counts do not sum to 7
- "All 7 rows filled" confirmation absent
- Gate label present but state counts absent

---

### PHASE 4 — WRITE GATE

Entry condition: STATE GATE CLEARED produced.

Write the filled template to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [TOTAL_COUNT]
phases_completed: 4
earned: [n from STATE GATE]
in_progress: [n from STATE GATE]
locked: [n from STATE GATE]
---
```

Produce the WRITE GATE PASS schema from the registry.

FAIL — does not clear WRITE GATE:
- Missing "WRITE GATE CLEARED" label
- Artifact path absent or path has wrong topic or date
- Gate label present but path absent

---

## V-05 — Golden Synthesis: Schema Preface + Gate Registry + Fail-Surface Closure

**Axes**: Lifecycle emphasis (schema preface — gate schema declared BEFORE phase
instructions) + output format (gate registry table at preamble) + phrasing register
(FAIL conditions per gate) + all R5 V-05 baseline wins preserved
**Hypothesis**: The strongest C-20/C-21 guarantee comes from three layers simultaneously:
(1) registry — the model sees all 4 gate schemas before Phase 1 begins (C-21 architectural
visibility; C-20 pre-declared schemas); (2) schema preface — each phase section opens with
its gate schema as goal state, before instructions (the model reads what it must produce
before doing the work); (3) fail-surface closure — each gate lists what does NOT clear it,
turning the schema into a two-sided verifiable contract. These three layers are mutually
reinforcing rather than redundant: registry gives overview, preface gives immediacy, FAIL
conditions give defensive closure. R5 V-05 baseline wins (C-01 through C-19: session
invariants A-D, pre-printed Falsified row, pre-printed LOCKED cell text, pre-printed table
skeleton, CLASSIFY before STATE, all phases gated) are preserved unchanged.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout all phases:**

Invariant A (State): Each achievement row carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values. No combined states.

Invariant B (Floor): Namespace-level evidence from the `prove` namespace is always
acceptable and is the safe floor for the Falsified achievement. Any prove artifact
containing a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS.
No full synthesis required.

Invariant C (Citation): EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`.
LOCKED rows name the exact artifact type or count required.

Invariant D (Preservation): The achievement table template in Phase 3 contains pre-printed
compliance text — in the Falsified row and in LOCKED cell detail. Do not rewrite, rephrase,
or restructure that pre-printed text. Fill only the placeholders as instructed.

---

**Gate Registry** — all 4 phases are gated. Declared before Phase 1 begins.

| Phase | Gate | PASS schema |
|-------|------|-------------|
| 1 — SCAN | SCAN GATE | `SCAN GATE CLEARED` / `Artifacts: [n]` / `Floor: active — Invariant B applies` |
| 2 — CLASSIFY | CLASSIFY GATE | `CLASSIFY GATE CLEARED` / `Exploration: [list or "none"]` / `Depth: [n] artifacts` / `Coverage: [namespaces] — [n] of 9` / `Quality (Falsified candidates): [list or "none"]` / `Chain: hypothesis [p/a] — evidence [p/a] — synthesize [p/a]` / `Discovery: [list or "none"]` / `Corps/Crew: contributors [list] — count [n]` / `[n] of 7 categories populated. Proceeding to template fill.` |
| 3 — FILL | STATE GATE | `STATE GATE CLEARED` / `EARNED: [n]` / `IN-PROGRESS: [n]` / `LOCKED: [n]` / `All 7 rows filled. Invariants A–D applied.` |
| 4 — WRITE | WRITE GATE | `WRITE GATE CLEARED` / `Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md` |

Phases must be completed in order. A phase is not complete until its gate schema output
is produced exactly as declared in this registry.

---

### PHASE 1 — SCAN GATE

**SCAN GATE schema** (preface — read before executing):
```
SCAN GATE CLEARED
Artifacts: [n]
Floor: active — Invariant B applies
```

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract: filename, skill
(from `skill:` frontmatter or filename), namespace prefix (first segment of skill name),
date (from `date:` frontmatter or filename), contributor (`contributor:` or `author:`
frontmatter, or "not set").

Produce the SCAN GATE schema above.

FAIL — does not clear SCAN GATE:
- Missing "SCAN GATE CLEARED" label
- Missing artifact count
- Missing floor confirmation line
- Count and artifact list inconsistent

If n = 0: produce gate output with n=0. All STATE cells will be LOCKED in Phase 3. Proceed.

---

### PHASE 2 — CLASSIFY GATE

Entry condition: SCAN GATE CLEARED output produced.

**CLASSIFY GATE schema** (preface — read before executing):
```
CLASSIFY GATE CLEARED
Exploration: [list or "none"]
Depth: [n] artifacts
Coverage: [namespaces list] — [n] of 9
Quality (Falsified candidates): [list or "none"]
Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
Discovery: [list or "none"]
Corps/Crew: contributors [list or "none"] — count [n]
[n] of 7 categories populated. Proceeding to template fill.
```

Assign each artifact from Phase 1 to exactly one category. Do not assign states.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis + (prove-websearch or prove-intelligence) + prove-synthesize |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values |

Produce the CLASSIFY GATE schema above.

FAIL — does not clear CLASSIFY GATE:
- Summary count only ("3 of 7 categories populated") without the 7 labeled category lines
- Any category line missing (even if the result is "none")
- State assignments included (this phase classifies only; it does not assign states)
- Gate label present but category lines absent or partial

---

### PHASE 3 — FILL TEMPLATE (STATE GATE)

Entry condition: CLASSIFY GATE CLEARED output produced.

**STATE GATE schema** (preface — read before executing):
```
STATE GATE CLEARED
EARNED: [n]
IN-PROGRESS: [n]
LOCKED: [n]
All 7 rows filled. Invariants A–D applied.
```

Fill every `[PLACEHOLDER]` in the template below. Rules:
- Apply Invariant D: do not rewrite any pre-printed text in this template.
- Do not reorder rows. Do not add or remove rows.
- Apply Invariants A, B, C to every row.
- EARNED: fill `[EARNED_ARTIFACT]` with `filename — date`. Date-less EARNED fails.
- IN-PROGRESS: fill `[N]` and `[M]` with actual counts. Qualitative text without numbers
  fails.
- LOCKED: the detail text is pre-printed. Fill only `[SPECIFIC_GAP]` with the exact
  artifact type or action needed.

```markdown
## topic-achievements — {{topic}}
_Scanned: {{date}} — Total artifacts: [TOTAL_COUNT]_

| Category | Achievement | State | Detail |
|----------|-------------|-------|--------|
| Exploration | Spark | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 1 artifact / LOCKED: File any one artifact for topic `{{topic}}` using any Signal skill |
| Depth | Signal Depth | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] artifacts — earliest [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 5 artifacts / LOCKED: File 5 total artifacts for topic `{{topic}}` across any Signal skills |
| Coverage | Namespace Sweep | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] of 9 namespaces — [LIST_NAMESPACES] / IN-PROGRESS: [N] of 5 namespaces — missing: [LIST_MISSING] / LOCKED: File artifacts from 5 of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) |
| Quality | Falsified | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] — followed evidence over assumptions: [REVISION_EVENT] / IN-PROGRESS: [N] of [M] prove artifacts contain counter-signals — not yet synthesized / LOCKED: File a prove-synthesize or topic-echo artifact that records a hypothesis revision. Framing falsification as absence or as a result the investigation did not yield — including as a closing reflection — does not earn this achievement. Namespace-level evidence from the prove namespace is always acceptable and is the safe floor. |
| Chain | Hypothesis Chain | [EARNED / IN-PROGRESS / LOCKED] | EARNED: prove-hypothesis [DATE1] → prove-evidence [DATE2] → prove-synthesize [DATE3] / IN-PROGRESS: [N] of 3 chain links — missing: [LIST_MISSING_LINKS] / LOCKED: File prove-hypothesis, then prove-websearch or prove-intelligence, then prove-synthesize — in that order |
| Discovery | Echo Filed | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: topic-echo started but not finalized / LOCKED: Run /topic-echo to produce `{{topic}}-echo-{{date}}.md` |
| Corps/Crew | Team Contribution | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] contributors — [LIST_CONTRIBUTORS] — first joint artifact: [DATE] / IN-PROGRESS: [N] of 2 contributors active — second contributor needed / LOCKED: A second team member files any artifact for topic `{{topic}}` |

## Next Action

Run `/[SKILL]` to produce `{{topic}}-[ITEM]-{{date}}.md`.
This advances [CATEGORY: ACHIEVEMENT] from [CURRENT_STATE] toward [TARGET_STATE].
Why: [SPECIFIC_GAP — one sentence linking to the CLASSIFY GATE output].
```

Produce the STATE GATE schema above.

FAIL — does not clear STATE GATE:
- Numeric counts absent
- Counts do not sum to 7
- "All 7 rows filled" confirmation absent
- Gate label present but state counts absent

---

### PHASE 4 — WRITE GATE

Entry condition: STATE GATE CLEARED output produced.

**WRITE GATE schema** (preface — read before executing):
```
WRITE GATE CLEARED
Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md
```

Write the filled template to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [TOTAL_COUNT]
phases_completed: 4
earned: [n from STATE GATE]
in_progress: [n from STATE GATE]
locked: [n from STATE GATE]
---
```

Produce the WRITE GATE schema above.

FAIL — does not clear WRITE GATE:
- "WRITE GATE CLEARED" label absent
- Artifact path absent
- Path contains wrong topic or wrong date
- Gate label present but path absent
