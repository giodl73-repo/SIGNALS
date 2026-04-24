---
skill: quest-variate
skill_target: topic-achievements
round: 4
date: 2026-03-17
rubric_version: 4
basis: R3 V-04 and V-05 achieved Platinum (100) under v3 rubric. Under v4, V-05 still passes
       both new criteria (C-16: pre-printed skeleton; C-17: standalone floor sentence). V-04
       fails C-16 (rule-stated, not pre-printed). R3 excellence signals: (1) floor sentence
       must stand structurally independent from any conditional frame; (2) frontmatter state
       counts enable machine-readable STATE GATE audit trail. R4 targets C-16 and C-17 across
       all five variations and incorporates the frontmatter state count pattern as baseline.
---

# Variate R4 — topic-achievements

5 complete prompt body variations for the `topic-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Phrasing register (floor as session-level preamble invariant, no conditional section) | V-01, V-04 |
| Output format (pre-printed verbatim compliance block in instruction body) | V-02, V-04, V-05 |
| Lifecycle emphasis (SCAN GATE carries floor as numbered phase invariant) | V-03, V-05 |

---

## V-01 — Phrasing Register: Floor as Session-Level Preamble Invariant

**Axis**: Phrasing register
**Hypothesis**: Declaring the floor as a session-level invariant at the top of the prompt —
before any scan, classification, or Falsified-specific contract section — eliminates the
C-17 failure mode by position rather than by label surgery. The floor sentence appears under
the neutral heading "Session invariants:" (not under any conditional trigger phrase), and
is numbered alongside other prompt-level rules. There is no Falsified-specific section whose
conditional label could govern the floor, because the floor precedes all classification work.
C-16 is not targeted (requirements remain rule-stated), isolating C-17 for clean measurement.
A CLASSIFY step is included before STATE assignment (C-09 compliance from R3 V-03/V-04/V-05).

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — read before proceeding:**

Invariant 1 (State values): Each achievement carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values. No combined states.

Invariant 2 (Falsified floor): Namespace-level evidence from the `prove` namespace is always
acceptable and is the safe floor for the Falsified achievement. Any prove artifact containing
a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS, regardless of
whether a full synthesis exists.

Invariant 3 (Specificity): EARNED entries cite artifact filename and date. IN-PROGRESS entries
use `n of m` notation. LOCKED entries name the exact artifact type or count required.

---

**Step 1 — Scan**

Glob `simulations/**/{{topic}}-*.md`. For each file found:
- Extract the producing skill from `skill:` frontmatter (or parse from filename)
- Extract the date from `date:` frontmatter (or parse from filename)
- Extract `contributor:` or `author:` values; record "not set" if absent
- Note the namespace prefix (first segment of skill name: e.g., `prove` from `prove-synthesize`)

Internal scan record (not part of final output):
```
SCAN (internal)
Artifacts: [n]
  [filename] — skill: [skill] — namespace: [namespace] — date: [date] — contributor: [value]
```

If no artifacts found: state "SCAN: 0 artifacts for topic `{{topic}}`." Proceed with empty record.

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
| Corps/Crew | Artifacts with 2+ distinct contributor values across the scan record |

Classify output (internal, not part of final output):
```
CLASSIFY
  Exploration: [list or "none"]
  Depth total: [n] artifacts
  Coverage namespaces: [list] — [n] of 9
  Quality (Falsified candidates): [list or "none"]
  Chain links: hypothesis [present/absent], evidence [present/absent], synthesize [present/absent]
  Discovery: [list or "none"]
  Corps/Crew: [list or "none"]
```

---

**Step 3 — Assign States**

Using the CLASSIFY output and Session invariants, assign exactly one state to each achievement.

Achievement conditions:

| Category | Achievement | Condition |
|----------|-------------|-----------|
| Exploration | Spark | 1+ artifact in classify record |
| Depth | Signal Depth | 5+ total artifacts |
| Coverage | Namespace Sweep | 5+ of 9 namespaces in classify record |
| Quality | Falsified | See Falsified contract below |
| Chain | Hypothesis Chain | All 3 chain links present in classify record |
| Discovery | Echo Filed | topic-echo artifact in classify record |
| Corps/Crew | Team Contribution | 2+ distinct contributor values |

**Falsified achievement contract:**

Rule 1 (Earn): Falsified is EARNED when the Quality classify record contains a prove-synthesize
or topic-echo artifact that explicitly records a hypothesis revision — earlier assumptions
changed because evidence contradicted them.

Rule 2 (Describe): The EARNED detail must frame the achievement as investigative rigor: "followed
evidence over assumptions" or equivalent. Framing falsification as absence, failure, or as a
reflection on what the investigation did not yield fails this rule — including when framed as a
closing reflection appended to the synthesize output.

Rule 3 (Apply floor): Apply Session invariant 2 above. Any prove artifact with a counter-signal
qualifies Falsified for IN-PROGRESS. No synthesis required for IN-PROGRESS.

---

**Step 4 — Achievement Table**

Output this structure exactly. Apply Session invariants 1 and 3 to every row.

```markdown
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

Generic instructions ("continue the investigation", "add more signals") fail.

---

**Step 6 — Write Artifact**

Write the achievement table and next action to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

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

## V-02 — Output Format: Pre-Printed Verbatim Compliance Block in Instruction Body

**Axis**: Output format
**Hypothesis**: Pre-printing the entire Falsified compliance block — consequence clause, named
evasion surface, and floor declaration — as a verbatim instruction-body callout (not a table
cell) achieves C-16 through a different structural mechanism than V-05's template skeleton.
The block is labeled with a neutral heading ("FALSIFIED ACHIEVEMENT CONTRACT — PRE-PRINTED")
and the floor appears as Rule 3 without any conditional governing label, achieving C-17. The
model is instructed not to rewrite the block: it applies the rules to evidence, but the
compliance text itself is pre-printed and structurally present before any output is generated.
A CLASSIFY phase runs before state assignment (C-09). Frontmatter carries state counts.

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

Internal record (not output):
```
ARTIFACTS
  [filename] — skill: [skill] — namespace: [namespace] — date: [date] — contributor: [value]
```

If no artifacts: record this and proceed; all achievements will be LOCKED.

---

**Step 2 — Falsified Compliance Block**

The following block is pre-printed. Do not rewrite it, paraphrase it, or alter its structure.
Apply it when classifying and assigning state to the Falsified achievement. Reference the
rule numbers when writing the Falsified row detail.

```
FALSIFIED ACHIEVEMENT CONTRACT — PRE-PRINTED

Rule 1 (Earn): Falsified is EARNED when an artifact explicitly records that a hypothesis was
revised or abandoned because evidence contradicted it, and the narrative captures this
contradiction as a finding.

Rule 2 (Describe): Frame the EARNED achievement as investigative rigor — "followed evidence
over assumptions." Do not frame falsification as absence, failure, or lack of evidence.
A description that notes the topic "did not yield a falsification result" fails this rule —
including as a closing reflection appended to the synthesize output.

Rule 3 (Floor): Namespace-level evidence from the `prove` namespace is always acceptable and
is the safe floor. Any prove artifact containing a counter-signal or hypothesis revision
qualifies Falsified for IN-PROGRESS. No full synthesis is required for IN-PROGRESS.
```

---

**Step 3 — Classify**

Assign each artifact from Step 1 to exactly one category. Do not assign states yet.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo — Falsified candidates; apply the pre-printed block |
| Chain | prove-hypothesis, prove-websearch or prove-intelligence, prove-synthesize — each link |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values across the scan record |

Internal classify record (not output):
```
CLASSIFY
  Exploration: [list or "none"]
  Depth: [n] artifacts
  Coverage: [list namespaces] — [n] of 9
  Falsified candidates: [list or "none"]
  Chain: hypothesis [present/absent], evidence [present/absent], synthesize [present/absent]
  Discovery: [list or "none"]
  Corps/Crew: contributors [list or "none"], count [n]
```

---

**Step 4 — Assign States and Build Table**

Assign exactly one state (EARNED, IN-PROGRESS, or LOCKED) to each achievement using the
classify record from Step 3. For Falsified, apply the pre-printed contract from Step 2.

State rules:
- **EARNED**: All conditions met. Cite filename and date. A date-less EARNED fails.
- **IN-PROGRESS**: Some conditions met. Express as `n of m`. Qualitative-only text fails.
- **LOCKED**: No conditions met. Name the exact artifact type or count required.

Achievement conditions:

| Category | Achievement | Condition |
|----------|-------------|-----------|
| Exploration | Spark | 1+ artifact |
| Depth | Signal Depth | 5+ total artifacts |
| Coverage | Namespace Sweep | 5+ of 9 namespaces |
| Quality | Falsified | Apply pre-printed contract (Step 2) |
| Chain | Hypothesis Chain | All 3 chain links present |
| Discovery | Echo Filed | topic-echo artifact present |
| Corps/Crew | Team Contribution | 2+ distinct contributor values |

```markdown
## topic-achievements — {{topic}}

| Category | Achievement | State | Evidence / Progress / Unlock Condition |
|----------|-------------|-------|----------------------------------------|
| Exploration | Spark | [STATE] | [detail] |
| Depth | Signal Depth | [STATE] | [detail] |
| Coverage | Namespace Sweep | [STATE] | [detail] |
| Quality | Falsified | [STATE] | [detail — reference pre-printed contract rules by number] |
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

## V-03 — Lifecycle Emphasis: SCAN GATE Carries Floor as Numbered Phase Invariant

**Axis**: Lifecycle emphasis
**Hypothesis**: Elevating the floor declaration to a SCAN GATE invariant — output as a
numbered standing rule before classification begins — structurally separates the floor from
the Falsified-specific contract. The floor's governing label is "SCAN GATE" (a neutral phase
marker), not a conditional trigger phrase. Because the floor is declared at phase-gate level,
no Falsified section label can govern it: it precedes and is independent of all achievement-
specific rules. This achieves C-17 via architectural position, not label surgery. A CLASSIFY
GATE runs before STATE GATE (C-09). Frontmatter carries state counts.

---

You are running `topic-achievements` for topic: `{{topic}}`.

Work through four phases in order. Output each gate before proceeding to the next phase.

---

### PHASE 1 — SCAN

Glob `simulations/**/{{topic}}-*.md`. For each artifact, record:
- Filename
- Skill (from `skill:` frontmatter or filename)
- Namespace prefix
- Date (from `date:` frontmatter or filename)
- Contributor (`contributor:` or `author:` frontmatter, or "not set")

**SCAN GATE** — output exactly:
> "SCAN GATE: [n] artifacts found for topic `{{topic}}`."
> "Phase invariant 1: Each achievement carries exactly one state — EARNED, IN-PROGRESS, or LOCKED."
> "Phase invariant 2: Namespace-level evidence from the prove namespace is always acceptable and is the safe floor for the Falsified achievement."
> "Phase invariant 3: Any prove artifact containing a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS."

If n = 0: "SCAN GATE: 0 artifacts. All achievements will be LOCKED. Phase invariants apply."
Proceed to Phase 2 regardless.

---

### PHASE 2 — CLASSIFY

**Entry condition**: SCAN GATE confirmed.

Using the Phase 1 artifact list, assign each artifact to exactly one category. Do not assign
states. Commit to classifications before proceeding.

| Category | Qualifying Signals |
|----------|--------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo with a hypothesis revision |
| Chain | prove-hypothesis, prove-websearch or prove-intelligence, prove-synthesize — all three links |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values across artifacts |

Output:
```
CLASSIFY LOG
  Exploration: [list or "none"]
  Depth: [n] artifacts
  Coverage: [list namespaces] — [n] of 9
  Quality (Falsified candidates): [list or "none"]
  Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
  Discovery: [list or "none"]
  Corps/Crew: contributors [list or "none"] — count [n]
```

**CLASSIFY GATE** — output exactly:
> "CLASSIFY GATE: [n] of 7 categories have at least one artifact."

---

### PHASE 3 — STATE

**Entry condition**: CLASSIFY GATE confirmed. Apply phase invariants from SCAN GATE.

Assign exactly one state to each achievement using the CLASSIFY LOG.

State rules:
- **EARNED**: All required conditions in CLASSIFY LOG present. Cite filename and date.
  Date-less citation fails.
- **IN-PROGRESS**: Some required conditions met. Express as `n of m`. "Partially done" fails.
- **LOCKED**: No required conditions met. State the exact artifact type or count required.

Achievement conditions:

| Category | Achievement | Condition |
|----------|-------------|-----------|
| Exploration | Spark | 1+ artifact in CLASSIFY LOG |
| Depth | Signal Depth | 5+ total (Depth count in CLASSIFY LOG) |
| Coverage | Namespace Sweep | 5+ of 9 namespaces (Coverage in CLASSIFY LOG) |
| Quality | Falsified | Quality classify log non-empty AND artifact records hypothesis revision |
| Chain | Hypothesis Chain | All 3 chain links present (Chain in CLASSIFY LOG) |
| Discovery | Echo Filed | topic-echo in Discovery CLASSIFY LOG |
| Corps/Crew | Team Contribution | Contributor count >= 2 (Corps/Crew in CLASSIFY LOG) |

Falsified state rules:
1. EARNED when Quality classify log is non-empty AND the artifact records that earlier assumptions
   were revised because evidence contradicted them.
2. EARNED detail must say "followed evidence over assumptions" — never "did not yield this result"
   or equivalent absence framing, including as a closing reflection.
3. Apply phase invariants 2 and 3 from the SCAN GATE: any prove artifact with a counter-signal
   qualifies for IN-PROGRESS.

```markdown
## topic-achievements — {{topic}}

| Category | Achievement | State | Evidence / Progress / Unlock Condition |
|----------|-------------|-------|----------------------------------------|
| Exploration | Spark | [STATE] | [detail] |
| Depth | Signal Depth | [STATE] | [detail] |
| Coverage | Namespace Sweep | [STATE] | [detail] |
| Quality | Falsified | [STATE] | [detail — cite artifact; apply SCAN GATE phase invariants 2–3] |
| Chain | Hypothesis Chain | [STATE] | [detail] |
| Discovery | Echo Filed | [STATE] | [detail] |
| Corps/Crew | Team Contribution | [STATE] | [detail] |
```

**STATE GATE** — output exactly:
> "STATE GATE: [n] EARNED, [n] IN-PROGRESS, [n] LOCKED. Phase invariants applied."

---

### PHASE 4 — RECOMMEND AND WRITE

**Entry condition**: STATE GATE confirmed.

**Next action** — verify all three checks before writing:
1. Names the exact Signal skill (`/[skill]`)
2. Names the artifact it produces (`{{topic}}-[item]-{{date}}.md`)
3. Names the achievement category and achievement name advanced

```markdown
## Next Action

Run `/[skill]` to produce `{{topic}}-[item]-{{date}}.md`.
This advances [Category: Achievement] from [current state] toward [target state].
Why: [one sentence — links to the specific gap in the CLASSIFY LOG].
```

**Write artifact** to: `simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

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

**WRITE GATE** — output:
> "WRITE GATE: Artifact written to simulations/topic/achievements/{{topic}}-achievements-{{date}}.md"

---

## V-04 — Role Sequence + Output Format: Pre-Printed Block Embedded in Classifier Role

**Axes**: Role sequence (Artifact Analyst → Achievement Classifier) + output format
(pre-printed Falsified compliance block in Role 2 contract)
**Hypothesis**: R3 V-04 achieved Platinum under v3 via role separation but fails C-16 under
v4 because its Falsified contract is rule-stated. V-04 R4 adds a pre-printed compliance block
to Role 2, achieving C-16 via structural embedding. The block's neutral heading ("FALSIFIED
CONTRACT — PRE-PRINTED") ensures C-17: the floor appears as a numbered rule inside a block
labeled with a non-conditional heading. Role separation prevents state contamination (C-09).
Frontmatter state counts capture the STATE audit trail.

---

You are running `topic-achievements` for topic: `{{topic}}`.

Two roles execute in sequence. Complete Role 1 entirely before beginning Role 2.

---

### ROLE 1 — ARTIFACT ANALYST

Goal: build a complete evidence record. Assign no states. Make no achievement judgments.

**Scan**

Glob `simulations/**/{{topic}}-*.md`. For each file:
- Record filename
- Extract skill from `skill:` frontmatter (fall back to filename parsing)
- Extract namespace prefix (first segment of skill name)
- Extract date from `date:` frontmatter (fall back to filename)
- Extract contributor from `contributor:` or `author:` frontmatter (record "not set" if absent)

**Evidence Record** (output this section):

```markdown
## Artifact Analyst — {{topic}} — {{date}}

Total artifacts: [n]

| Filename | Skill | Namespace | Date | Contributor |
|----------|-------|-----------|------|-------------|
| [filename] | [skill] | [namespace] | [date] | [value or "not set"] |
```

If no artifacts: fill table with zero rows. Note: "No artifacts for `{{topic}}`. Role 2 assigns LOCKED to all."

**Supporting inventories** (output these sections, consumed by Role 2):

```
Namespace inventory:
  Represented: [list] — [n] of 9
  Missing: [list]

Chain links:
  prove-hypothesis: [filename + date, or "absent"]
  prove-websearch / prove-intelligence: [filename + date, or "absent"]
  prove-synthesize: [filename + date, or "absent"]

Falsified candidates:
  (prove-synthesize or topic-echo with hypothesis revision — list filenames or "none identified")

Contributor inventory:
  Distinct values: [list or "not detectable"]
  Count: [n or "unknown"]
```

---

### ROLE 2 — ACHIEVEMENT CLASSIFIER

Goal: assign exactly one state to each of the 7 achievements using only the Role 1 evidence
record and inventories. Do not re-scan. Do not look up new information.

**Falsified Compliance Block** — pre-printed. Apply to Falsified state assignment.
Do not rewrite or paraphrase this block.

```
FALSIFIED CONTRACT — PRE-PRINTED

Rule 1 (Earn): Falsified is EARNED when the Role 1 Falsified candidates list is non-empty
AND the identified artifact records that earlier assumptions were revised because evidence
contradicted them.

Rule 2 (Describe): The EARNED detail must describe the revision event — "followed evidence
over assumptions." It must not describe the investigation's completeness. Framing as absence,
as a goal not reached, or as a reflection on what the investigation did not yield fails this
rule — including as a closing reflection appended to the synthesize output.

Rule 3 (Floor): Namespace-level evidence from the prove namespace is always acceptable and
is the safe floor. A prove artifact containing a counter-signal or a stated revision of an
earlier claim qualifies Falsified for IN-PROGRESS. No full synthesis is required.
```

**Achievement conditions:**

| Category | Achievement | Condition |
|----------|-------------|-----------|
| Exploration | Spark | 1+ artifact in Role 1 evidence record |
| Depth | Signal Depth | 5+ total artifacts in Role 1 evidence record |
| Coverage | Namespace Sweep | 5+ in Role 1 namespace inventory |
| Quality | Falsified | Apply pre-printed contract above |
| Chain | Hypothesis Chain | All 3 chain links present in Role 1 chain links |
| Discovery | Echo Filed | topic-echo in Role 1 evidence record |
| Corps/Crew | Team Contribution | Contributor count >= 2 in Role 1 contributor inventory |

**State rules:**
- **EARNED**: Required conditions met per Role 1 evidence. Cite filename and date. Date-less fails.
- **IN-PROGRESS**: Some conditions met. Express as `n of m`. "Partially done" fails.
- **LOCKED**: No conditions met. Name the exact artifact type or count required. "Not yet started" fails.

**Achievement Table** (output this section):

```markdown
## topic-achievements — {{topic}}

| Category | Achievement | State | Evidence / Progress / Unlock Condition |
|----------|-------------|-------|----------------------------------------|
| Exploration | Spark | [STATE] | [detail] |
| Depth | Signal Depth | [STATE] | [detail] |
| Coverage | Namespace Sweep | [STATE] | [detail] |
| Quality | Falsified | [STATE] | [detail — apply pre-printed contract; cite Role 1 candidate] |
| Chain | Hypothesis Chain | [STATE] | [detail] |
| Discovery | Echo Filed | [STATE] | [detail] |
| Corps/Crew | Team Contribution | [STATE] | [detail] |
```

**Next Recommended Action**

Verify before writing:
1. Names the exact Signal skill (`/[skill]`)
2. Names the artifact it produces (`{{topic}}-[item]-{{date}}.md`)
3. Names the achievement category and name advanced

```markdown
## Next Action

Run `/[skill]` to produce `{{topic}}-[item]-{{date}}.md`.
This advances [Category: Achievement] from [current state] toward [target state].
Why: [one sentence — the specific gap in the Role 1 evidence record].
```

**Write Artifact**

`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [n from Role 1]
roles_completed: 2
earned: [n]
in_progress: [n]
locked: [n]
---
```

---

## V-05 — Golden Synthesis: Pre-Printed Skeleton + Preamble Invariant + SCAN GATE Invariant

**Axes**: Output format (pre-printed template skeleton) + phrasing register (floor as
session-level preamble invariant) + lifecycle emphasis (SCAN GATE repeats floor as phase
invariant) + frontmatter state counts
**Hypothesis**: Three-layer C-17 guarantee: (1) floor declared as preamble invariant before
any conditional classification work begins, (2) SCAN GATE repeats the floor as a numbered
phase invariant output, (3) floor pre-printed verbatim in the Falsified table cell. No
conditional section label can govern any of the three instances — the preamble label is
neutral, the SCAN GATE is a neutral phase marker, and the table cell has no governing header
at all. C-16 is guaranteed by the pre-printed table skeleton. CLASSIFY GATE before template
fill enforces C-09. Frontmatter state counts make the STATE GATE result durable.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout:**

Invariant A: Each achievement row carries exactly one state value: EARNED, IN-PROGRESS, or LOCKED.
Invariant B: Namespace-level evidence from the `prove` namespace is always acceptable and is
the safe floor for the Falsified achievement.
Invariant C: EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`. LOCKED rows
name the exact artifact type or count required.

---

### PHASE 1 — SCAN

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract:
- Filename, skill, namespace prefix, date, contributor

**SCAN GATE** — output exactly:
> "SCAN GATE: [n] artifacts found for topic `{{topic}}`."
> "Floor confirmed (Invariant B): Namespace-level evidence from the prove namespace is always acceptable and is the safe floor."

If n = 0: fill all STATE cells as LOCKED in Phase 3. Proceed.

---

### PHASE 2 — CLASSIFY

Assign each artifact to exactly one category. Commit before proceeding to Phase 3.

| Category | Qualifying Signals |
|----------|--------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis, prove-websearch or prove-intelligence, prove-synthesize — all 3 links |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values across artifacts |

**CLASSIFY GATE** — output exactly:
> "CLASSIFY GATE: [n] of 7 categories have at least one artifact. Proceeding to template fill."

---

### PHASE 3 — FILL TEMPLATE

Fill every `[PLACEHOLDER]` in the template below. Rules:

- Do not change any pre-printed text.
- Do not reorder rows. Do not add or remove rows.
- Apply Session invariants A, B, C to every row.
- EARNED: fill `[EARNED_ARTIFACT]` with `filename — date`. Date-less fill fails.
- IN-PROGRESS: fill `[N]` and `[M]` with actual count and total. "Partial" without numbers fails.
- LOCKED: the detail cell is pre-printed. Fill only `[SPECIFIC_GAP]` with the exact artifact or action.

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
Why: [SPECIFIC_GAP — one sentence linking to the classify result above].
```

**STATE GATE** — output exactly:
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
earned: [n from STATE GATE]
in_progress: [n from STATE GATE]
locked: [n from STATE GATE]
---
```

**WRITE GATE** — output:
> "WRITE GATE: Artifact written to simulations/topic/achievements/{{topic}}-achievements-{{date}}.md"
