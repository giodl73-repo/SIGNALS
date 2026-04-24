---
skill: quest-variate
skill_target: topic-achievements
round: 3
date: 2026-03-17
rubric_version: 3
basis: R2 V-02 passed C-12 (consequence clause present) but missed C-14 (consequence clause did
       not name the specific evasion surface "including as a closing reflection"). R2 V-03 passed
       C-13 (fallback instruction present) but missed C-15 (fallback framed as conditional rather
       than declared as unconditional minimum "always acceptable and is the safe floor").
       R3 targets both new criteria across all five variations.
---

# Variate R3 — topic-achievements

5 complete prompt body variations for the `topic-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Phrasing register (formal imperative vs descriptive with examples) | V-01, V-04 |
| Output format (pre-printed template skeleton vs generated table) | V-02, V-05 |
| Lifecycle emphasis (explicit named phases with gate contracts) | V-03, V-04, V-05 |

---

## V-01 — Phrasing Register: Formal Imperative with Explicit Consequence Contracts

**Axis**: Phrasing register
**Hypothesis**: Formal imperative phrasing with an explicit stated pass/fail contract for every
output field — especially the Falsified row's consequence clause — produces reliable C-12 and
C-14 compliance because the model is told what constitutes a passing description, not just what
to do. Including the specific evasion surface ("including as a closing reflection") as a named
prohibited pattern in the Falsified contract eliminates the most common failure mode.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Step 1 — Scan**

Glob `simulations/**/{{topic}}-*.md`. For each file found:
- Record the skill that produced it (from the `skill:` frontmatter field or the filename segment
  before the date)
- Record the date (from the `date:` frontmatter field or the trailing date in the filename)
- Assign the file to one of the 7 achievement categories based on its skill namespace:
  - **Exploration**: scout-*, topic-new, prove-hypothesis
  - **Depth**: any skill with a follow-up or iteration count (3+ artifacts from same namespace)
  - **Coverage**: signals across 5+ of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic)
  - **Quality**: review-*, prove-synthesize, prove-publish
  - **Chain**: prove-hypothesis → prove-websearch/prove-intelligence → prove-synthesize all present
  - **Discovery**: topic-echo, prove-topic
  - **Corps/Crew**: org-*, mock-review (MOCK-ACCEPTED signals), 2+ contributors in frontmatter

If `simulations/` has no matching files, output: "SCAN: No artifacts found for topic `{{topic}}`."
Proceed to Step 2 with an empty artifact list.

Produce an internal working list (not part of final output):
```
SCAN (internal)
Artifacts found: [n]
  - [filename] → category: [category] — date: [date]
```

**Step 2 — Compute States**

For each of the 7 achievement categories, compute the state using these rules:

State assignment:
- **EARNED**: All required artifacts for this achievement are present. Cite the specific artifact(s).
- **IN-PROGRESS**: Some but not all required artifacts are present. Express progress as `n of m`
  (e.g., "3 of 5 namespaces covered"). Qualitative descriptions ("partially done") fail this field.
- **LOCKED**: No required artifacts are present. State the exact artifact type or count required
  to unlock. Statements like "not yet started" without specifics fail this field.

Achievement definitions per category:

| Category | Achievement | Condition |
|----------|-------------|-----------|
| Exploration | Spark | 1+ artifact exists for this topic |
| Depth | Signal Depth | 5+ total artifacts for this topic |
| Coverage | Namespace Sweep | Artifacts from 5+ of the 9 namespaces |
| Quality | **Falsified** | See Falsified contract below |
| Chain | Hypothesis Chain | prove-hypothesis + (prove-websearch or prove-intelligence) + prove-synthesize all present |
| Discovery | Echo Filed | topic-echo artifact present |
| Corps/Crew | Team Contribution | 2+ distinct contributor values in frontmatter across any artifacts |

**Falsified achievement contract — read carefully before assigning state:**

Falsified is EARNED when an artifact explicitly records that the investigation followed evidence
over earlier assumptions — meaning a hypothesis was revised or abandoned because evidence
contradicted it, and the final narrative captures this contradiction as a finding.

The Falsified state MUST be framed as evidence of investigative rigor: "followed evidence over
assumptions" or equivalent. Framing falsification as absence, failure, or lack of evidence fails
this requirement — including as a closing reflection that notes the topic "did not yield a
falsification result."

When evidence for Falsified is uncertain or partially present, namespace-level evidence from the
`prove` namespace is always acceptable and is the safe floor: any prove artifact that contains
a counter-signal or hypothesis revision qualifies for IN-PROGRESS.

**Step 3 — Achievement Table**

Output exactly this structure. One row per achievement. State column uses exactly one of the
three values: EARNED, IN-PROGRESS, LOCKED. Do not combine states in a row or use any other value.

```
## topic-achievements — {{topic}}

| Category | Achievement | State | Evidence / Progress / Unlock Condition |
|----------|-------------|-------|----------------------------------------|
| Exploration | Spark | [STATE] | [EARNED: artifact path + date] / [IN-PROGRESS: n of m] / [LOCKED: what artifact is needed] |
| Depth | Signal Depth | [STATE] | ... |
| Coverage | Namespace Sweep | [STATE] | ... |
| Quality | Falsified | [STATE] | [EARNED: artifact + "followed evidence over assumptions — [brief evidence]"] / [IN-PROGRESS: n of m prove artifacts contain counter-signals] / [LOCKED: "File a prove-synthesize or topic-echo artifact that explicitly records a hypothesis revision"] |
| Chain | Hypothesis Chain | [STATE] | ... |
| Discovery | Echo Filed | [STATE] | ... |
| Corps/Crew | Team Contribution | [STATE] | ... |
```

Rules:
- EARNED rows must include the artifact path and date. A date-less EARNED row fails.
- IN-PROGRESS rows must include `n of m` notation. "Partial" or "underway" fails.
- LOCKED rows must name the exact artifact type or action required. "Not yet started" without
  specifics fails.

**Step 4 — Next Recommended Action**

Name one next action. It must pass all three checks before being written:
1. Names the exact Signal skill to run (e.g., `/prove-synthesize`, `/topic-echo`)
2. Names the artifact it produces (e.g., `{{topic}}-synthesize-{{date}}.md`)
3. Names the achievement(s) it advances (by category name and achievement name)

Format:
```
## Next Action

Run `/[skill]` to produce `{{topic}}-[item]-{{date}}.md`.
This advances [Category: Achievement] from [current state] toward [target state].
Why: [one sentence linking this action to the specific gap in Step 2].
```

Generic instructions ("continue the investigation", "add more signals") fail this field.

**Step 5 — Write Artifact**

Write the complete table and next action to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

Frontmatter:
```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [n]
categories: [exploration, depth, coverage, quality, chain, discovery, corps-crew]
---
```

---

## V-02 — Output Format: Pre-Printed Template Skeleton

**Axis**: Output format
**Hypothesis**: Pre-printing the achievement table with all 7 category headers, the Falsified
row including the consequence clause text and the specific evasion surface verbatim, and the
IN-PROGRESS `n of m` scaffold means the model transcribes these elements rather than generating
them. The evasion surface "including as a closing reflection" appears in the pre-printed template
and cannot be omitted. The unconditional floor declaration "always acceptable and is the safe
floor" is pre-printed in the Falsified LOCKED row template. The model fills placeholders — it
does not rewrite structure.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Step 1 — Scan**

Glob `simulations/**/{{topic}}-*.md`. Collect every artifact. For each:
- Identify the producing skill from the `skill:` frontmatter field or filename
- Extract the date from the `date:` frontmatter field or filename trailing date
- Note any `author:` or `contributor:` frontmatter values

Internal working record (not output):
```
ARTIFACTS:
  [filename] — skill: [skill] — date: [date] — contributor: [value or "not set"]
```

If no artifacts found: state this and fill all table rows as LOCKED.

**Step 2 — Fill the Template**

Fill every `[PLACEHOLDER]` in the template below. Do not change any pre-printed text.
Do not reorder rows. Do not add or remove rows. If a state is EARNED, fill the evidence field
with the artifact path and date. If IN-PROGRESS, fill the `[N]` and `[M]` values. If LOCKED,
fill the unlock condition field.

```markdown
## topic-achievements — {{topic}}
_Scanned: {{date}} — Artifacts found: [TOTAL_COUNT]_

| Category | Achievement | State | Detail |
|----------|-------------|-------|--------|
| Exploration | Spark | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [artifact path] — [date] / IN-PROGRESS: [N] of [M] artifacts / LOCKED: File one artifact of any skill for this topic |
| Depth | Signal Depth | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] artifacts — earliest [date], latest [date] / IN-PROGRESS: [N] of 5 artifacts / LOCKED: File 5 artifacts across any skills for this topic |
| Coverage | Namespace Sweep | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [list namespaces] — [N] of 9 / IN-PROGRESS: [N] of 5 namespaces covered — missing: [list] / LOCKED: File artifacts from 5 of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) |
| Quality | Falsified | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [artifact path] — [date] — followed evidence over assumptions: [brief evidence of hypothesis revision] / IN-PROGRESS: [N] of [M] prove artifacts contain counter-signals — not yet synthesized / LOCKED: File a prove-synthesize or topic-echo artifact that records a hypothesis revision. Framing falsification as absence or lack of evidence — including as a closing reflection — does not earn this achievement. Namespace-level evidence from the prove namespace is always acceptable and is the safe floor. |
| Chain | Hypothesis Chain | [EARNED / IN-PROGRESS / LOCKED] | EARNED: prove-hypothesis [date] → prove-websearch/prove-intelligence [date] → prove-synthesize [date] / IN-PROGRESS: [N] of 3 chain links present — missing: [list] / LOCKED: File prove-hypothesis, then prove-websearch or prove-intelligence, then prove-synthesize — in that order |
| Discovery | Echo Filed | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [topic-echo artifact path] — [date] / IN-PROGRESS: topic-echo draft started but not finalized / LOCKED: Run /topic-echo to produce {{topic}}-echo-[date].md |
| Corps/Crew | Team Contribution | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] contributors: [list] — first joint artifact: [date] / IN-PROGRESS: [N] of 2 contributors active — second contributor needed / LOCKED: A second team member files any artifact for this topic |

## Next Action

Run `/[SKILL]` to produce `{{topic}}-[ITEM]-{{date}}.md`.
This advances [CATEGORY: ACHIEVEMENT] from [CURRENT STATE] toward [TARGET STATE].
Why: [One sentence — the specific gap from the table above that this action closes].
```

Do not fill a LOCKED row with generic text. Every LOCKED detail must name the exact artifact
type or count required. "Not yet started" without specifics fails.

Do not fill an EARNED row without a date. A date-less EARNED detail fails.

Do not fill an IN-PROGRESS row without `n of m` notation. Qualitative-only text fails.

**Step 3 — Write Artifact**

Write the filled template to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

Frontmatter:
```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [TOTAL_COUNT]
---
```

---

## V-03 — Lifecycle Emphasis: Explicit Phase Boundaries with Exit Contracts

**Axis**: Lifecycle emphasis
**Hypothesis**: Four explicitly named phases (SCAN → CLASSIFY → STATE → RECOMMEND) with
entry conditions and gate-check outputs force the model to commit to each step before
proceeding. The CLASSIFY phase requires separate classification of each artifact before
any state is assigned — preventing the common failure where LOCKED achievements receive
no evidence citation because classification and state assignment happen simultaneously.
The STATE phase declares the Falsified fallback as an unconditional phase-level contract
("always acceptable and is the safe floor"), making it a structural rule rather than an
inline note that can be overlooked.

---

You are running `topic-achievements` for topic: `{{topic}}`.

Work through the four phases in order. Each phase has an entry condition. Complete each
phase fully before reading the next.

---

### PHASE 1 — SCAN

**Entry condition**: Topic name provided.

Glob `simulations/**/{{topic}}-*.md`. For each artifact found, record:

```
SCAN LOG
  [filename]
    skill: [producing skill — from frontmatter or filename]
    date: [date — from frontmatter or filename]
    contributor: [value or "not set"]
```

**SCAN GATE**: State exactly:
> "SCAN GATE: [n] artifacts found for topic `{{topic}}`."

If n = 0: "SCAN GATE: 0 artifacts found. All achievements will be LOCKED. Proceeding."
Proceed to Phase 2 regardless.

---

### PHASE 2 — CLASSIFY

**Entry condition**: SCAN GATE confirmed.

Assign each artifact from the SCAN LOG to exactly one of these 7 categories. One artifact may
only appear in one category. If an artifact could fit multiple categories, assign it to the
most specific one (e.g., `prove-synthesize` goes to Chain before Quality).

Category assignment rules:

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | Any skill — count total; Depth earns at 5+ |
| Coverage | Any skill — track unique namespaces |
| Quality | review-*, prove-publish; Falsified earns via prove-synthesize or topic-echo with hypothesis revision |
| Chain | prove-hypothesis, prove-websearch, prove-intelligence, prove-synthesize (chain requires all three links) |
| Discovery | topic-echo, topic-story (when unexpected findings present) |
| Corps/Crew | org-*, artifacts with 2+ distinct contributor values |

Output:
```
CLASSIFY LOG
  Exploration: [list artifacts] or "none"
  Depth: [total artifact count across all categories] artifacts
  Coverage: [list unique namespaces represented]
  Quality (Falsified candidates): [list prove-synthesize or topic-echo artifacts, or "none"]
  Chain: [list prove-hypothesis, prove-evidence, prove-synthesize artifacts]
  Discovery: [list topic-echo artifacts, or "none"]
  Corps/Crew: [list artifacts with multi-contributor markers, or "none"]
```

**CLASSIFY GATE**: State exactly:
> "CLASSIFY GATE: [n] artifacts classified across [n] of 7 categories."

---

### PHASE 3 — STATE

**Entry condition**: CLASSIFY GATE confirmed.

Assign exactly one state to each achievement using these rules:

- **EARNED**: All required artifacts classified in Phase 2 are present. Cite at least one artifact by filename and date.
- **IN-PROGRESS**: Some but not all required conditions met. Express progress as `n of m`. Qualitative-only text ("partially done") fails.
- **LOCKED**: No required artifacts classified in Phase 2 are present. State the specific artifact type or count required.

**Falsified state rule — phase contract:**

Falsified is EARNED when the Quality classify log contains a prove-synthesize or topic-echo
artifact that records a hypothesis revision: earlier assumptions changed because evidence
contradicted them. The description in the STATE output must frame this as investigative
rigor ("followed evidence over assumptions"), never as absence or failure.

Framing Falsified as absence, failure, or a reflection on what the investigation did not
yield — including as a closing reflection — fails this rule. The state column must read
EARNED, IN-PROGRESS, or LOCKED; the detail column must cite the artifact and describe the
revision event, not the absence of one.

Fallback for uncertain Falsified evidence: Namespace-level evidence from the `prove` namespace
is always acceptable and is the safe floor. Any prove artifact that contains a counter-signal
or documents a revision qualifies for IN-PROGRESS, regardless of whether a full synthesis
exists.

Output:
```
## topic-achievements — {{topic}}

| Category | Achievement | State | Evidence / Progress / Unlock Condition |
|----------|-------------|-------|----------------------------------------|
| Exploration | Spark | [STATE] | [detail] |
| Depth | Signal Depth | [STATE] | [detail] |
| Coverage | Namespace Sweep | [STATE] | [detail] |
| Quality | Falsified | [STATE] | [detail — must name artifact and revision event, not absence] |
| Chain | Hypothesis Chain | [STATE] | [detail] |
| Discovery | Echo Filed | [STATE] | [detail] |
| Corps/Crew | Team Contribution | [STATE] | [detail] |
```

**STATE GATE**: State exactly:
> "STATE GATE: [n] EARNED, [n] IN-PROGRESS, [n] LOCKED."

---

### PHASE 4 — RECOMMEND

**Entry condition**: STATE GATE confirmed.

Write one recommended next action. Before writing, verify it passes all three checks:
1. Names the exact Signal skill (`/[skill]`)
2. Names the artifact it produces (`{{topic}}-[item]-{{date}}.md`)
3. Names the achievement category and achievement name it advances

```
## Next Action

Run `/[skill]` to produce `{{topic}}-[item]-{{date}}.md`.
This advances [Category: Achievement] from [STATE] toward [TARGET STATE].
Why: [One sentence — links to the specific gap in the CLASSIFY LOG or STATE output].
```

**RECOMMEND GATE**: State exactly:
> "RECOMMEND GATE: Next action written. Skill: /[skill]. Achievement advanced: [category: achievement]."

---

### WRITE ARTIFACT

Write the achievement table (Phase 3 output) and next action (Phase 4 output) to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [n from SCAN GATE]
phases_completed: 4
---
```

---

## V-04 — Role Sequence + Lifecycle Emphasis (Combination)

**Axes**: Role sequence (Artifact Analyst → Achievement Classifier) + lifecycle emphasis
(explicit phase boundaries within each role)
**Hypothesis**: Separating the artifact analysis role from the achievement classification role
prevents state contamination — the most common C-01 failure where IN-PROGRESS and LOCKED entries
get mixed because the model classifies and states simultaneously. The Analyst produces a
clean evidence record before the Classifier assigns states. The Classifier role carries the full
Falsified contract including both the consequence clause with the evasion surface named and the
unconditional floor declaration — both C-14 and C-15 targets are structural role instructions,
not inline notes.

---

You are running `topic-achievements` for topic: `{{topic}}`.

Work through two roles in sequence. Complete Role 1 entirely before beginning Role 2.

---

### ROLE 1 — ARTIFACT ANALYST

Your job: find what exists and build an evidence record. Assign no states. Make no judgments.
Produce only facts.

**Scan**

Glob `simulations/**/{{topic}}-*.md`. For each file:
- Record the filename
- Extract `skill:` and `date:` from frontmatter; fall back to filename parsing if frontmatter absent
- Extract `contributor:` or `author:` values; record "not set" if absent
- Note the namespace (first segment of the skill name, e.g., `prove` from `prove-synthesize`)

**Evidence Record** (output this section):

```
## Artifact Analyst — {{topic}} — {{date}}

Total artifacts: [n]

| Filename | Skill | Namespace | Date | Contributor |
|----------|-------|-----------|------|-------------|
| [filename] | [skill] | [namespace] | [date] | [value or "not set"] |
...
```

If no artifacts found: output the table with zero rows and the note:
"No artifacts found for topic `{{topic}}`. Role 2 will assign LOCKED to all achievements."

**Namespace inventory** (needed by Role 2):
```
Namespaces represented: [list] ([n] of 9)
Missing namespaces: [list]
```

**Chain links present** (needed by Role 2):
```
Chain — prove-hypothesis: [filename + date, or "absent"]
Chain — prove-websearch or prove-intelligence: [filename + date, or "absent"]
Chain — prove-synthesize: [filename + date, or "absent"]
```

**Falsified candidates** (needed by Role 2):
```
Falsified candidates (prove-synthesize or topic-echo with hypothesis revision):
  [list filenames, or "none identified"]
```

**Contributor inventory** (needed by Role 2):
```
Contributors: [deduplicated list, or "not detectable"]
Distinct contributor count: [n or "unknown"]
```

---

### ROLE 2 — ACHIEVEMENT CLASSIFIER

Your job: assign exactly one state (EARNED, IN-PROGRESS, or LOCKED) to each of the 7
achievements, using only the evidence from Role 1. Do not re-scan. Do not look up new information.

**State assignment rules:**

- **EARNED**: The Role 1 evidence record contains all required artifacts. Cite the filename and
  date. A date-less EARNED citation fails.
- **IN-PROGRESS**: Some required conditions are met. Express progress as `n of m`. A row that
  says "partially done" or "underway" without numeric notation fails.
- **LOCKED**: No required conditions are met in the Role 1 record. State the exact artifact type
  or count required. A row that says "not yet started" without specifics fails.

**Achievement conditions:**

| Category | Achievement | Condition |
|----------|-------------|-----------|
| Exploration | Spark | 1+ artifact in Role 1 evidence record |
| Depth | Signal Depth | 5+ total artifacts in Role 1 evidence record |
| Coverage | Namespace Sweep | 5+ namespaces in Role 1 namespace inventory |
| Quality | Falsified | See Falsified contract |
| Chain | Hypothesis Chain | All 3 chain links present in Role 1 chain inventory |
| Discovery | Echo Filed | topic-echo artifact in Role 1 evidence record |
| Corps/Crew | Team Contribution | Distinct contributor count >= 2 in Role 1 contributor inventory |

**Falsified achievement contract:**

Falsified is EARNED when the Role 1 Falsified candidates list is non-empty AND the identified
artifact records that earlier assumptions were revised because evidence contradicted them.
The EARNED detail must frame this as investigative rigor: the team "followed evidence over
assumptions." It must describe the revision event, not the investigation's completeness.

Framing Falsified as absence, as a goal not reached, or as a reflection on what the investigation
did not find — including as a closing reflection appended to the synthesize output — fails this
contract. The state is EARNED when a revision artifact exists; IN-PROGRESS when prove namespace
artifacts contain counter-signals that have not yet been synthesized; LOCKED when no prove
artifacts are present.

Namespace-level evidence from the `prove` namespace is always acceptable and is the safe floor.
A prove artifact need not be a full synthesis to qualify Falsified for IN-PROGRESS — any
prove artifact containing a counter-signal or a stated revision of an earlier claim counts.

**Achievement Table** (output this section):

```
## topic-achievements — {{topic}}

| Category | Achievement | State | Evidence / Progress / Unlock Condition |
|----------|-------------|-------|----------------------------------------|
| Exploration | Spark | [STATE] | [detail] |
| Depth | Signal Depth | [STATE] | [detail] |
| Coverage | Namespace Sweep | [STATE] | [detail] |
| Quality | Falsified | [STATE] | [detail] |
| Chain | Hypothesis Chain | [STATE] | [detail] |
| Discovery | Echo Filed | [STATE] | [detail] |
| Corps/Crew | Team Contribution | [STATE] | [detail] |
```

**Next Recommended Action**

Name one action. Verify it passes these three checks before writing:
1. Names the exact Signal skill (`/[skill]`)
2. Names the artifact it produces (`{{topic}}-[item]-{{date}}.md`)
3. Names the achievement category and achievement name it advances

```
## Next Action

Run `/[skill]` to produce `{{topic}}-[item]-{{date}}.md`.
This advances [Category: Achievement] from [current state] toward [target state].
Why: [one sentence — the specific gap identified in Role 1 evidence record].
```

**Write Artifact**

Write the Role 2 achievement table and next action to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [n from Role 1]
roles_completed: 2
---
```

---

## V-05 — Golden Synthesis: Pre-Printed Template + Phase Contracts + Pre-Printed Falsified Block

**Axes**: Output format (pre-printed skeleton) + lifecycle emphasis (explicit phase gates) +
phrasing register (consequence clause and floor declaration pre-printed verbatim, not instructed)
**Hypothesis**: The strongest structural guarantees on C-12, C-13, C-14, and C-15 come from
pre-printing every element the model might otherwise fail to generate. The Falsified LOCKED row
template pre-prints "including as a closing reflection" as the named evasion surface (C-14 cannot
fail — the text is already on the page). The fallback floor declaration "always acceptable and
is the safe floor" is pre-printed in the LOCKED template (C-15 cannot fail for the same reason).
Phase gates enforce artifact-grounded classification (C-03) and numeric IN-PROGRESS notation
(C-04). The model's only task is to fill placeholders; it cannot rewrite the pre-printed
structural text.

---

You are running `topic-achievements` for topic: `{{topic}}`.

---

### PHASE 1 — SCAN

Glob `simulations/**/{{topic}}-*.md`. Collect every artifact. For each, extract:
- `skill:` from frontmatter (or parse from filename)
- `date:` from frontmatter (or parse from filename)
- `contributor:` from frontmatter (or "not set")

**SCAN GATE**: Before proceeding to Phase 2, output:
> "SCAN GATE: [n] artifacts found for topic `{{topic}}`."

If n = 0, fill all table STATE cells as LOCKED and all detail cells with the pre-printed
LOCKED text. Do not halt.

---

### PHASE 2 — CLASSIFY

Assign each artifact to exactly one category using these rules:

| Category | Qualifying signals |
|----------|--------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis, prove-websearch/prove-intelligence, prove-synthesize — track presence of each link |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values across any artifacts |

**CLASSIFY GATE**: Before proceeding to Phase 3, output:
> "CLASSIFY GATE: Artifacts assigned. [n] of 7 categories have at least one artifact."

---

### PHASE 3 — FILL TEMPLATE

Fill every `[PLACEHOLDER]` in the template below. Rules:

- Do not change any pre-printed text.
- Do not reorder rows.
- Do not add or remove rows.
- EARNED: fill `[EARNED_ARTIFACT]` with `filename — date`. A date-less fill fails.
- IN-PROGRESS: fill `[N]` and `[M]` with the actual count and total. "Partial" without numbers fails.
- LOCKED: the detail text is pre-printed. Fill only `[SPECIFIC_GAP]` with the exact artifact or action needed.

```markdown
## topic-achievements — {{topic}}
_Scanned: {{date}} — Total artifacts: [TOTAL_COUNT]_

| Category | Achievement | State | Detail |
|----------|-------------|-------|--------|
| Exploration | Spark | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 1 artifact / LOCKED: File any one artifact for this topic using any Signal skill |
| Depth | Signal Depth | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] artifacts — [EARNED_ARTIFACT] (earliest) / IN-PROGRESS: [N] of 5 artifacts / LOCKED: File 5 total artifacts across any Signal skills for topic `{{topic}}` |
| Coverage | Namespace Sweep | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] of 9 namespaces — [LIST_NAMESPACES] / IN-PROGRESS: [N] of 5 namespaces — missing: [LIST_MISSING] / LOCKED: File artifacts from 5 of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) |
| Quality | Falsified | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] — followed evidence over assumptions: [REVISION_EVENT] / IN-PROGRESS: [N] of [M] prove artifacts contain counter-signals — not yet synthesized / LOCKED: File a prove-synthesize or topic-echo artifact that records a hypothesis revision. Framing falsification as absence or as a result the investigation did not yield — including as a closing reflection — does not earn this achievement. Namespace-level evidence from the prove namespace is always acceptable and is the safe floor. |
| Chain | Hypothesis Chain | [EARNED / IN-PROGRESS / LOCKED] | EARNED: prove-hypothesis [DATE1] → prove-evidence [DATE2] → prove-synthesize [DATE3] / IN-PROGRESS: [N] of 3 chain links — missing: [LIST_MISSING_LINKS] / LOCKED: File prove-hypothesis, then prove-websearch or prove-intelligence, then prove-synthesize — in that order |
| Discovery | Echo Filed | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: topic-echo started but not finalized / LOCKED: Run /topic-echo to produce `{{topic}}-echo-{{date}}.md` |
| Corps/Crew | Team Contribution | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] contributors — [LIST_CONTRIBUTORS] — first joint artifact: [DATE] / IN-PROGRESS: [N] of 2 contributors active — second contributor needed / LOCKED: A second team member files any artifact for topic `{{topic}}` |

## Next Action

Run `/[SKILL]` to produce `{{topic}}-[ITEM]-{{date}}.md`.
This advances [CATEGORY: ACHIEVEMENT] from [CURRENT_STATE] toward [TARGET_STATE].
Why: [SPECIFIC_GAP — one sentence linking to the classify or state result above].
```

**STATE GATE**: Before proceeding to Phase 4, output:
> "STATE GATE: [n] EARNED, [n] IN-PROGRESS, [n] LOCKED. All 7 rows filled."

---

### PHASE 4 — WRITE ARTIFACT

Write the filled template to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [TOTAL_COUNT]
phases_completed: 4
earned: [n]
in_progress: [n]
locked: [n]
---
```

**WRITE GATE**: Output:
> "WRITE GATE: Artifact written to simulations/topic/achievements/{{topic}}-achievements-{{date}}.md"
