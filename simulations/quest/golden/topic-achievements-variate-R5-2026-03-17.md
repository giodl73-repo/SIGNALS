---
skill: quest-variate
skill_target: topic-achievements
round: 5
date: 2026-03-17
rubric_version: 5
basis: R4 V-05 (Golden Synthesis) passes C-01 through C-17 under v4 rubric. Under v5, two
       new aspirational criteria are added: C-18 (preservation directive for pre-printed
       compliance text) and C-19 (gate-enforced phase completion with defined output per gate).
       R4 V-02 has a pre-printed block and a local "Do not rewrite" instruction — C-18
       candidate, but the directive is inline to the block header rather than stated in the
       instruction body as a named rule. R4 V-03 has gate architecture (SCAN GATE, CLASSIFY
       GATE, STATE GATE) but the gates do not define their required output format — they emit
       a count, not a structured record. R4 V-05 has both a pre-printed skeleton and phase
       gates, but: (a) the preservation directive appears only as "Do not change any pre-printed
       text" inside the phase 3 instructions rather than as a named invariant in the instruction
       body (C-18 borderline), and (b) the CLASSIFY GATE output is a summary count ("n of 7
       categories have at least one artifact") not a full per-category record (C-19 borderline).
       R5 targets C-18 and C-19 cleanly across all five variations. All R4 wins (C-01 through
       C-17, frontmatter state counts, CLASSIFY before STATE) are preserved as baseline.
---

# Variate R5 — topic-achievements

5 complete prompt body variations for the `topic-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Targets | Used In |
|------|---------|---------|
| Phrasing register (preservation directive as numbered session invariant in prompt preamble) | C-18 | V-01, V-04, V-05 |
| Output format (preservation directive as annotated first line inside the pre-printed block) | C-18 | V-02, V-04 |
| Lifecycle emphasis (gate architecture: each gate defines required output format, not just count) | C-19 | V-03, V-04, V-05 |

---

## V-01 — Phrasing Register: Preservation Directive as Numbered Session Invariant

**Axis**: Phrasing register
**Hypothesis**: Declaring "do not rewrite the pre-printed compliance block" as a numbered
session invariant at the top of the prompt — before any scan, classification, or Falsified-
specific section — achieves C-18 because the directive exists in the instruction body at
prompt level, governing the block from above rather than from within. The model reads the
preservation rule before encountering the block. The block (C-16) also labels itself
"PRE-PRINTED" but carries no local directive, making the session invariant the sole
structural anchor for C-18. CLASSIFY step produces per-category intermediate output before
STATE assignment (C-09, C-10). Floor is session invariant 2 (C-17). C-19 is not targeted —
phases are steps, not gates — isolating C-18 for clean measurement.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout:**

Invariant 1 (State): Each achievement row carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values. No combined states.

Invariant 2 (Floor): Namespace-level evidence from the `prove` namespace is always acceptable
and is the safe floor for the Falsified achievement. Any prove artifact containing a
counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS. No full synthesis
required for IN-PROGRESS.

Invariant 3 (Citation): EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`
notation. LOCKED rows name the exact artifact type or count required.

Invariant 4 (Preservation): The Falsified Achievement Contract block below is pre-printed
compliance text. Do not rewrite, rephrase, or restructure that block. Apply its rules to the
evidence. Do not alter its text.

---

**Step 1 — Scan**

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract:
- Filename
- Producing skill (from `skill:` frontmatter or filename parsing)
- Namespace prefix (first segment of skill name)
- Date (from `date:` frontmatter or filename)
- Contributor (`contributor:` or `author:` frontmatter, or "not set")

Internal scan record (not part of final output):
```
SCAN
  Artifacts: [n]
  [filename] — skill: [skill] — namespace: [ns] — date: [date] — contributor: [value]
```

If no artifacts: "SCAN: 0 artifacts for topic `{{topic}}`." Proceed with empty record.

---

**Step 2 — Classify**

Assign each artifact from Step 1 to exactly one category. Do not assign states yet.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis, prove-websearch or prove-intelligence, prove-synthesize — track each link |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values across the scan record |

Classify output (internal, not part of final output):
```
CLASSIFY
  Exploration: [list or "none"]
  Depth: [n] artifacts
  Coverage: [list namespaces] — [n] of 9
  Quality (Falsified candidates): [list or "none"]
  Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
  Discovery: [list or "none"]
  Corps/Crew: contributors [list or "none"] — count [n]
```

---

**Step 3 — Assign States**

Using the CLASSIFY output and Session invariants, assign exactly one state to each achievement.

Achievement conditions:

| Category | Achievement | Condition |
|----------|-------------|-----------|
| Exploration | Spark | 1+ artifact in classify record |
| Depth | Signal Depth | 5+ total artifacts |
| Coverage | Namespace Sweep | 5+ of 9 namespaces |
| Quality | Falsified | See pre-printed contract below |
| Chain | Hypothesis Chain | All 3 chain links present |
| Discovery | Echo Filed | topic-echo artifact in classify record |
| Corps/Crew | Team Contribution | 2+ distinct contributor values |

**Falsified Achievement Contract — PRE-PRINTED**
Apply Session invariant 4. Do not rewrite, rephrase, or restructure this block.

```
Rule 1 (Earn): Falsified is EARNED when an artifact in the Quality classify record
explicitly records that a hypothesis was revised or abandoned because evidence contradicted
it, and the narrative captures this contradiction as a finding.

Rule 2 (Describe): The EARNED row detail must frame the revision as investigative rigor:
"followed evidence over assumptions." Do not describe Falsified as absence, failure, or as
a reflection on what the investigation did not yield — including as a closing reflection
appended to the synthesize output.

Rule 3 (Floor): Apply Session invariant 2. Any prove artifact containing a counter-signal
or hypothesis revision qualifies Falsified for IN-PROGRESS. No full synthesis required.
```

---

**Step 4 — Achievement Table**

Output this structure. Apply Session invariants 1 and 3 to every row.

```markdown
## topic-achievements — {{topic}}

| Category | Achievement | State | Evidence / Progress / Unlock Condition |
|----------|-------------|-------|----------------------------------------|
| Exploration | Spark | [STATE] | [detail] |
| Depth | Signal Depth | [STATE] | [detail] |
| Coverage | Namespace Sweep | [STATE] | [detail] |
| Quality | Falsified | [STATE] | [detail — cite artifact; reference contract rules by number] |
| Chain | Hypothesis Chain | [STATE] | [detail] |
| Discovery | Echo Filed | [STATE] | [detail] |
| Corps/Crew | Team Contribution | [STATE] | [detail] |
```

---

**Step 5 — Next Recommended Action**

Verify before writing:
1. Names the exact Signal skill (e.g., `/prove-synthesize`)
2. Names the artifact it produces (e.g., `{{topic}}-synthesize-{{date}}.md`)
3. Names the achievement category and name it advances

```markdown
## Next Action

Run `/[skill]` to produce `{{topic}}-[item]-{{date}}.md`.
This advances [Category: Achievement] from [current state] toward [target state].
Why: [one sentence — the specific gap from the CLASSIFY output].
```

---

**Step 6 — Write Artifact**

Write to: `simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [n]
earned: [n]
in_progress: [n]
locked: [n]
---
```

---

## V-02 — Output Format: Preservation Directive as Block-Local Header Annotation

**Axis**: Output format
**Hypothesis**: Placing the preservation directive as the first line inside the pre-printed
compliance block — directly adjacent to the text it governs — creates the tightest possible
binding between directive and protected content. The model cannot read or process the block
without first encountering "THIS BLOCK IS PRE-PRINTED. Do not rewrite, rephrase, or
restructure any text in this block." The directive is stated in the instruction body as part
of the block (C-18). No separate session invariant — isolating block-local placement as the
single mechanism. CLASSIFY step produces per-category intermediate output before STATE
assignment (C-09, C-10). Floor is Rule 3 of the pre-printed block (C-17 via structural
independence from any conditional label). C-19 not targeted.

---

You are running `topic-achievements` for topic: `{{topic}}`.

---

**Step 1 — Scan**

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract:
- Filename
- Producing skill (from `skill:` frontmatter or filename segment)
- Namespace prefix (first segment of skill name)
- Date (from `date:` frontmatter or filename)
- Contributor (`contributor:` or `author:` frontmatter, or "not set")

Internal record (not part of final output):
```
ARTIFACTS
  [filename] — skill: [skill] — namespace: [ns] — date: [date] — contributor: [value]
```

If no artifacts: record "0 artifacts" and proceed; all achievements will be LOCKED.

---

**Step 2 — Classify**

Assign each artifact from Step 1 to exactly one category. Do not assign states yet.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis, prove-websearch or prove-intelligence, prove-synthesize — track each link |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values across the scan record |

Classify output (internal):
```
CLASSIFY
  Exploration: [list or "none"]
  Depth: [n] artifacts
  Coverage: [list namespaces] — [n] of 9
  Quality (Falsified candidates): [list or "none"]
  Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
  Discovery: [list or "none"]
  Corps/Crew: contributors [list or "none"] — count [n]
```

---

**Step 3 — Falsified Achievement Contract**

The following block is pre-printed. The first line is a directive that applies to the entire
block. Apply the rules to the evidence. Do not alter the block text.

```
THIS BLOCK IS PRE-PRINTED. Do not rewrite, rephrase, or restructure any text in this block.

FALSIFIED ACHIEVEMENT CONTRACT

Rule 1 (Earn): Falsified is EARNED when an artifact from the Falsified candidates list
explicitly records that a hypothesis was revised or abandoned because evidence contradicted
it, and the narrative captures this contradiction as a finding.

Rule 2 (Describe): The EARNED row detail must frame the revision as investigative rigor:
"followed evidence over assumptions." Do not describe Falsified as absence, failure, or as
a reflection on what the investigation did not yield — including as a closing reflection
appended to the synthesize output.

Rule 3 (Floor): Namespace-level evidence from the prove namespace is always acceptable and
is the safe floor. Any prove artifact containing a counter-signal or hypothesis revision
qualifies Falsified for IN-PROGRESS. No full synthesis required.
```

---

**Step 4 — Assign States and Build Table**

Assign exactly one state (EARNED, IN-PROGRESS, or LOCKED) to each achievement using the
classify record from Step 2. For Falsified, apply the pre-printed contract from Step 3.

State rules:
- **EARNED**: All conditions met. Cite filename and date. Date-less EARNED fails.
- **IN-PROGRESS**: Some conditions met. Express as `n of m`. Qualitative-only text fails.
- **LOCKED**: No conditions met. Name the exact artifact type or count required.

Achievement conditions:

| Category | Achievement | Condition |
|----------|-------------|-----------|
| Exploration | Spark | 1+ artifact |
| Depth | Signal Depth | 5+ total artifacts |
| Coverage | Namespace Sweep | 5+ of 9 namespaces |
| Quality | Falsified | Apply pre-printed contract (Step 3) |
| Chain | Hypothesis Chain | All 3 chain links present |
| Discovery | Echo Filed | topic-echo present |
| Corps/Crew | Team Contribution | 2+ distinct contributor values |

```markdown
## topic-achievements — {{topic}}

| Category | Achievement | State | Evidence / Progress / Unlock Condition |
|----------|-------------|-------|----------------------------------------|
| Exploration | Spark | [STATE] | [detail] |
| Depth | Signal Depth | [STATE] | [detail] |
| Coverage | Namespace Sweep | [STATE] | [detail] |
| Quality | Falsified | [STATE] | [detail — apply pre-printed contract rules by number] |
| Chain | Hypothesis Chain | [STATE] | [detail] |
| Discovery | Echo Filed | [STATE] | [detail] |
| Corps/Crew | Team Contribution | [STATE] | [detail] |
```

---

**Step 5 — Next Recommended Action**

Verify before writing:
1. Names the exact Signal skill
2. Names the artifact it produces
3. Names the achievement category and name advanced

```markdown
## Next Action

Run `/[skill]` to produce `{{topic}}-[item]-{{date}}.md`.
This advances [Category: Achievement] from [current state] toward [target state].
Why: [one sentence — the specific gap in the classify record].
```

---

**Step 6 — Write Artifact**

Write to: `simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [n]
earned: [n]
in_progress: [n]
locked: [n]
---
```

---

## V-03 — Lifecycle Emphasis: Gate Architecture with Defined Completion Output per Gate

**Axis**: Lifecycle emphasis
**Hypothesis**: A gate is not just a label — it is a barrier that cannot be cleared without
producing defined output. R4 V-03 emits "CLASSIFY GATE: [n] of 7 categories have at least
one artifact" — a count, not a structured per-category record. This passes C-19's gate label
requirement but may not satisfy its completion-output requirement: the count alone does not
force visible intermediate classification. V-03 R5 defines each gate with a required output
template showing what the model must produce (format, fields, all category lines) before the
gate is cleared. The CLASSIFY GATE requires a full per-category record, not just a count —
making phase completion both visible and auditable. No pre-printed block (C-16/C-18 not
targeted); C-19 isolated for clean measurement. Floor is declared as a SCAN GATE phase
invariant (C-17).

---

You are running `topic-achievements` for topic: `{{topic}}`.

Work through four phases in order. Each phase ends with a gate. A gate is a labeled barrier:
produce the specified gate output exactly as shown before proceeding to the next phase.

---

### PHASE 1 — SCAN

Glob `simulations/**/{{topic}}-*.md`. For each artifact, record:
- Filename
- Skill (from `skill:` frontmatter or filename)
- Namespace prefix (first segment of skill name)
- Date (from `date:` frontmatter or filename)
- Contributor (`contributor:` or `author:` frontmatter, or "not set")

**SCAN GATE** — required output to clear this gate. Produce exactly:

```
SCAN GATE CLEARED
Artifacts: [n]
Phase invariant 1: Each achievement carries exactly one state — EARNED, IN-PROGRESS, or LOCKED.
Phase invariant 2: Namespace-level evidence from the prove namespace is always acceptable
  and is the safe floor for the Falsified achievement.
Phase invariant 3: Any prove artifact containing a counter-signal or hypothesis revision
  qualifies Falsified for IN-PROGRESS. No full synthesis required.
```

If n = 0: produce the gate output above with n=0. All achievements will be LOCKED. Proceed.

---

### PHASE 2 — CLASSIFY

Entry condition: SCAN GATE CLEARED output present.

Assign each artifact from Phase 1 to exactly one category. Do not assign states yet.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis, prove-websearch or prove-intelligence, prove-synthesize — track each link |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values |

**CLASSIFY GATE** — required output to clear this gate. Produce all lines exactly:

```
CLASSIFY GATE CLEARED
Exploration: [list or "none"]
Depth: [n] artifacts
Coverage: [list namespaces] — [n] of 9
Quality (Falsified candidates): [list or "none"]
Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
Discovery: [list or "none"]
Corps/Crew: contributors [list or "none"] — count [n]
[n] of 7 categories have at least one artifact.
```

A CLASSIFY GATE output that contains only a summary count and omits category lines does not
clear this gate. All category lines must appear before Phase 3 may begin.

---

### PHASE 3 — STATE

Entry condition: CLASSIFY GATE CLEARED output present.

Apply Phase 1 invariants. Assign exactly one state to each achievement using the CLASSIFY
GATE output.

State rules:
- **EARNED**: All required conditions present in CLASSIFY GATE. Cite filename and date.
  Date-less EARNED fails.
- **IN-PROGRESS**: Some conditions met. Express as `n of m`. "Partially done" fails.
- **LOCKED**: No conditions met. Name the exact artifact type or count required.

Achievement conditions:

| Category | Achievement | Condition |
|----------|-------------|-----------|
| Exploration | Spark | Exploration line non-empty in CLASSIFY GATE |
| Depth | Signal Depth | Depth count >= 5 in CLASSIFY GATE |
| Coverage | Namespace Sweep | Coverage count >= 5 of 9 in CLASSIFY GATE |
| Quality | Falsified | Quality line non-empty AND artifact records hypothesis revision |
| Chain | Hypothesis Chain | All 3 chain links present in CLASSIFY GATE Chain line |
| Discovery | Echo Filed | Discovery line non-empty in CLASSIFY GATE |
| Corps/Crew | Team Contribution | Corps/Crew count >= 2 in CLASSIFY GATE |

Falsified state rules:
1. EARNED when Quality line is non-empty AND the artifact records that earlier assumptions
   were revised because evidence contradicted them.
2. EARNED detail must say "followed evidence over assumptions" — never "did not yield this
   result" or any absence framing, including as a closing reflection.
3. Apply Phase 1 invariants 2 and 3 from the SCAN GATE.

```markdown
## topic-achievements — {{topic}}

| Category | Achievement | State | Evidence / Progress / Unlock Condition |
|----------|-------------|-------|----------------------------------------|
| Exploration | Spark | [STATE] | [detail] |
| Depth | Signal Depth | [STATE] | [detail] |
| Coverage | Namespace Sweep | [STATE] | [detail] |
| Quality | Falsified | [STATE] | [detail — cite artifact; apply SCAN GATE invariants 2–3] |
| Chain | Hypothesis Chain | [STATE] | [detail] |
| Discovery | Echo Filed | [STATE] | [detail] |
| Corps/Crew | Team Contribution | [STATE] | [detail] |
```

**STATE GATE** — required output to clear this gate. Produce exactly:

```
STATE GATE CLEARED
EARNED: [n]
IN-PROGRESS: [n]
LOCKED: [n]
Phase invariants applied.
```

---

### PHASE 4 — WRITE

Entry condition: STATE GATE CLEARED output present.

**Next action** — verify all three checks before writing:
1. Names the exact Signal skill (`/[skill]`)
2. Names the artifact it produces (`{{topic}}-[item]-{{date}}.md`)
3. Names the achievement category and achievement name advanced

```markdown
## Next Action

Run `/[skill]` to produce `{{topic}}-[item]-{{date}}.md`.
This advances [Category: Achievement] from [current state] toward [target state].
Why: [one sentence — links to the specific gap in the CLASSIFY GATE output].
```

Write artifact to: `simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [n from SCAN GATE]
phases_completed: 4
earned: [n from STATE GATE]
in_progress: [n from STATE GATE]
locked: [n from STATE GATE]
---
```

**WRITE GATE** — required output to clear this gate. Produce exactly:

```
WRITE GATE CLEARED
Artifact written to: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md
```

---

## V-04 — Combination: Session Invariant + Block-Local Directive + CLASSIFY GATE with Full Output

**Axes**: Phrasing register (preservation directive as session invariant) + output format
(preservation directive as block-local annotation) + lifecycle emphasis (CLASSIFY GATE with
full per-category required output)
**Hypothesis**: Dual-layer C-18 guarantee: the preservation directive appears both as a
numbered session invariant (governing the block from the instruction body, above all phases)
and as the first line of the pre-printed block itself (block-local annotation). Neither layer
alone is necessary if the other is present; both together eliminate any interpretation where
the directive applies only locally or only globally. C-19 is targeted by a CLASSIFY GATE
that requires the full per-category record as defined completion output — not a count. C-16
is satisfied by the pre-printed block; C-17 by session invariant 2. All R4 wins preserved.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout all phases:**

Invariant 1 (State): Each achievement row carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values.

Invariant 2 (Floor): Namespace-level evidence from the `prove` namespace is always acceptable
and is the safe floor for the Falsified achievement. Any prove artifact containing a
counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS. No full synthesis
required.

Invariant 3 (Citation): EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`.
LOCKED rows name the exact artifact type or count required.

Invariant 4 (Preservation): The Falsified Achievement Contract block in Phase 3 is
pre-printed compliance text. Do not rewrite, rephrase, or restructure that block. Apply its
rules to evidence. Do not alter its text.

---

### PHASE 1 — SCAN

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract:
- Filename
- Skill (from `skill:` frontmatter or filename)
- Namespace prefix (first segment of skill name)
- Date (from `date:` frontmatter or filename)
- Contributor (`contributor:` or `author:` frontmatter, or "not set")

**SCAN GATE** — output exactly:
> "SCAN GATE: [n] artifacts found for topic `{{topic}}`."

If n = 0: output gate text. All achievements will be LOCKED. Proceed.

---

### PHASE 2 — CLASSIFY

Entry condition: SCAN GATE output present.

Assign each artifact to exactly one category. Do not assign states.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis, prove-websearch or prove-intelligence, prove-synthesize — track each link |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values |

**CLASSIFY GATE** — required output to clear this gate. All lines must appear:

```
CLASSIFY GATE CLEARED
Exploration: [list or "none"]
Depth: [n] artifacts
Coverage: [list namespaces] — [n] of 9
Quality (Falsified candidates): [list or "none"]
Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
Discovery: [list or "none"]
Corps/Crew: contributors [list or "none"] — count [n]
[n] of 7 categories have at least one artifact.
```

A CLASSIFY GATE output containing only a count and no per-category lines does not clear this
gate. Phase 3 may not begin until all category lines are present.

---

### PHASE 3 — STATE

Entry condition: CLASSIFY GATE CLEARED output present.

Apply Session invariants. Assign exactly one state per achievement.

**Falsified Achievement Contract — pre-printed. Apply Session invariant 4.**

```
THIS BLOCK IS PRE-PRINTED. Do not rewrite, rephrase, or restructure any text in this block.

FALSIFIED ACHIEVEMENT CONTRACT

Rule 1 (Earn): Falsified is EARNED when the CLASSIFY GATE Quality line is non-empty AND
the identified artifact explicitly records that a hypothesis was revised or abandoned because
evidence contradicted it.

Rule 2 (Describe): The EARNED row detail must frame the revision as investigative rigor:
"followed evidence over assumptions." Do not describe Falsified as absence, failure, or as
a reflection on what the investigation did not yield — including as a closing reflection
appended to the synthesize output.

Rule 3 (Floor): Apply Session invariant 2. Any prove artifact in the CLASSIFY GATE with a
counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS.
```

Achievement conditions:

| Category | Achievement | Condition |
|----------|-------------|-----------|
| Exploration | Spark | Exploration line non-empty in CLASSIFY GATE |
| Depth | Signal Depth | Depth count >= 5 |
| Coverage | Namespace Sweep | Coverage count >= 5 of 9 |
| Quality | Falsified | Apply pre-printed contract |
| Chain | Hypothesis Chain | All 3 chain links present in CLASSIFY GATE Chain line |
| Discovery | Echo Filed | Discovery line non-empty in CLASSIFY GATE |
| Corps/Crew | Team Contribution | Corps/Crew count >= 2 |

```markdown
## topic-achievements — {{topic}}

| Category | Achievement | State | Evidence / Progress / Unlock Condition |
|----------|-------------|-------|----------------------------------------|
| Exploration | Spark | [STATE] | [detail] |
| Depth | Signal Depth | [STATE] | [detail] |
| Coverage | Namespace Sweep | [STATE] | [detail] |
| Quality | Falsified | [STATE] | [detail — cite artifact; reference contract rules by number] |
| Chain | Hypothesis Chain | [STATE] | [detail] |
| Discovery | Echo Filed | [STATE] | [detail] |
| Corps/Crew | Team Contribution | [STATE] | [detail] |
```

**STATE GATE** — output exactly:
> "STATE GATE: [n] EARNED, [n] IN-PROGRESS, [n] LOCKED. Session invariants applied."

---

### PHASE 4 — WRITE

Entry condition: STATE GATE output present.

**Next action** — verify all three checks before writing:
1. Names the exact Signal skill
2. Names the artifact it produces
3. Names the achievement category and name advanced

```markdown
## Next Action

Run `/[skill]` to produce `{{topic}}-[item]-{{date}}.md`.
This advances [Category: Achievement] from [current state] toward [target state].
Why: [one sentence — the specific gap from the CLASSIFY GATE output].
```

Write artifact to: `simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [n from SCAN GATE]
phases_completed: 4
earned: [n from STATE GATE]
in_progress: [n from STATE GATE]
locked: [n from STATE GATE]
---
```

---

## V-05 — Golden Synthesis: Session Invariant + Pre-Printed Skeleton + Full Gate Architecture

**Axes**: Phrasing register (preservation directive as session invariant + floor as session
invariant) + output format (pre-printed template skeleton with Falsified block pre-printed
verbatim in LOCKED cell) + lifecycle emphasis (all gates define required output format with
full per-category record)
**Hypothesis**: Extends R4 V-05 with clean C-18 and C-19 guarantees. C-18: preservation
directive is Session invariant D (instruction body, above all phases) — explicit, named,
pointing to the pre-printed template. C-19: every gate now defines its required output as a
structured template with all fields specified — SCAN GATE emits artifact count + phase
invariants, CLASSIFY GATE emits full per-category record (not just a count), STATE GATE
emits state totals, WRITE GATE confirms artifact path. C-17: floor appears as Session
invariant B (preamble) and as a repeated confirmation in SCAN GATE output. C-16: Falsified
LOCKED cell pre-prints the compliance text verbatim including the evasion surface and floor
declaration. All R4 Platinum criteria preserved at baseline.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout all phases:**

Invariant A (State): Each achievement row carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values. No combined states.

Invariant B (Floor): Namespace-level evidence from the `prove` namespace is always acceptable
and is the safe floor for the Falsified achievement. Any prove artifact containing a
counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS. No full synthesis
required.

Invariant C (Citation): EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`.
LOCKED rows name the exact artifact type or count required.

Invariant D (Preservation): The achievement table template in Phase 3 contains pre-printed
compliance text — in the Falsified row and in LOCKED cell detail. Do not rewrite, rephrase,
or restructure that pre-printed text. Fill only the placeholders as instructed.

---

### PHASE 1 — SCAN

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract:
- Filename, skill, namespace prefix, date, contributor

**SCAN GATE** — required output to clear this gate. Produce exactly:

```
SCAN GATE CLEARED
Artifacts: [n]
Floor confirmed (Invariant B): Namespace-level evidence from the prove namespace is always
  acceptable and is the safe floor for the Falsified achievement.
```

If n = 0: produce the gate output above with n=0. Fill all STATE cells LOCKED in Phase 3.
Proceed.

---

### PHASE 2 — CLASSIFY

Entry condition: SCAN GATE CLEARED output present.

Assign each artifact to exactly one category. Do not assign states.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis, prove-websearch or prove-intelligence, prove-synthesize — track each link |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values |

**CLASSIFY GATE** — required output to clear this gate. Produce all lines exactly:

```
CLASSIFY GATE CLEARED
Exploration: [list or "none"]
Depth: [n] artifacts
Coverage: [list namespaces] — [n] of 9
Quality (Falsified candidates): [list or "none"]
Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
Discovery: [list or "none"]
Corps/Crew: contributors [list or "none"] — count [n]
[n] of 7 categories have at least one artifact. Proceeding to template fill.
```

A CLASSIFY GATE containing only a summary count without per-category lines does not clear
this gate. All category lines must appear before Phase 3 may begin.

---

### PHASE 3 — FILL TEMPLATE

Entry condition: CLASSIFY GATE CLEARED output present.

Fill every `[PLACEHOLDER]` in the template below. Rules:

- Apply Invariant D: do not rewrite any pre-printed text in this template.
- Do not reorder rows. Do not add or remove rows.
- Apply Invariants A, B, C to every row.
- EARNED: fill `[EARNED_ARTIFACT]` with `filename — date`. Date-less fill fails.
- IN-PROGRESS: fill `[N]` and `[M]` with actual counts. "Partial" without numbers fails.
- LOCKED: the detail text is pre-printed. Fill only `[SPECIFIC_GAP]` with the exact artifact
  type or action needed.

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

**STATE GATE** — required output to clear this gate. Produce exactly:

```
STATE GATE CLEARED
EARNED: [n]
IN-PROGRESS: [n]
LOCKED: [n]
All 7 rows filled. Invariants A–D applied.
```

---

### PHASE 4 — WRITE ARTIFACT

Entry condition: STATE GATE CLEARED output present.

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

**WRITE GATE** — required output to clear this gate. Produce exactly:

```
WRITE GATE CLEARED
Artifact written to: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md
```
