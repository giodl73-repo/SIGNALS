---
skill: quest-variate
skill_target: corps-achievements
round: 1
date: 2026-03-16
rubric_version: 1
---

# Variate R1 — corps-achievements

5 complete prompt body variations for the `corps-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Output format (achievement grid table vs badge list vs prose dashboard) | V-01, V-05 |
| Phrasing register (imperative/structured vs conversational/game-badge) | V-02 |
| Lifecycle emphasis (implicit scan vs explicit named phase gates) | V-03, V-05 |
| Role sequence + inertia framing (skeptic role before leaderboard) | V-04 |
| Inertia framing (what stagnation looks like; cost of not acting) | V-04 |

---

## V-01 — Output Format: Achievement Grid Table

**Axis**: Output format
**Hypothesis**: A structured grid of achievements organized by rows (topics) × columns
(achievement types) makes C-02 and C-06 mechanically auditable; every discovered topic must
appear as a row by construction, so omissions are visible as blank rows rather than silent gaps.
The rigid column structure may flatten the qualitative C-10 insight, but the earned/available
split (C-06) is strongest here because it lives in distinct columns.

---

You are running `corps-achievements` for this workspace. No inputs — scan and compute.

**Step 1 — Scan**

Glob `simulations/` recursively. List every subdirectory that contains at least one `.md` file
as a discovered topic. Record the file count and any contributor metadata you can extract
(frontmatter `author:` or `contributor:` fields, or filename prefixes before `-`). If
`simulations/` is empty or absent, report this explicitly and proceed to Step 5 with no data.

Produce an internal working list (not part of final output):

```
SCAN RESULTS (internal)
Topics found: [n]
  - [topic path] — [file count] signals — contributors: [list or "unknown"]
Contributors found: [deduplicated list]
```

**Step 2 — Achievement Grid**

Build a Markdown table. One row per discovered topic. Use these exact columns:

| Topic | Signals | Earned Achievements | Available (Locked) Achievements | Top Contributor |
|-------|---------|--------------------|---------------------------------|-----------------|

Column rules:
- **Topic**: Path relative to `simulations/`, e.g. `scout/competitors`
- **Signals**: Count of `.md` files found in that topic path
- **Earned Achievements**: Badges already unlocked. Use format: `[badge name]`. If none: `—`
- **Available (Locked) Achievements**: Badges not yet earned; criteria clearly not met. Use format: `○ [badge name]`. If none possible: `—`
- **Top Contributor**: Contributor with the most signals for this topic. `unknown` if not determinable.

Achievement definitions to apply:
- **First Signal** — 1+ signal files exist for this topic (earned if count >= 1)
- **Signal Depth** — 3+ signal files exist for this topic (earned if count >= 3)
- **Full Sweep** — signals from 3+ distinct namespaces for this topic (check subdirectory names)
- **Solo Pioneer** — only one contributor detected for this topic across all signals (earned if contributor count == 1 and signals >= 1)
- **Team Topic** — 2+ contributors detected for this topic (earned if contributor count >= 2)

Every topic found in the scan must appear as a row. A topic with zero achievements writes `—`
in the Earned column, not an omitted row.

**Step 3 — Team Milestones**

Report a dedicated milestones section. Address all three milestones by exact name:

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|----------|
| first team signal | [EARNED / NOT YET] | [file path or "—"] |
| shared coverage | [EARNED / NOT YET] | [2+ contributors each with 2+ topics, or "—"] |
| debate starter | [EARNED / NOT YET] | [topic with signals from 2+ namespaces arguing different angles, or "—"] |
```

Do not rename, abbreviate, or paraphrase the milestone names. A milestone labeled "first signal
posted" instead of "first team signal" does not count.

**Step 4 — Contributor Leaderboard**

```
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Topics Covered | Total Signals | Namespaces Active |
|------|-------------|---------------|---------------|-------------------|
| 1 | [name or "unknown"] | [n] | [n] | [list] |
...
```

If no contributor metadata is extractable, write one row: `| — | (no contributor metadata found) | — | — | — |`
Do not omit the leaderboard section.

**Step 5 — Next Actions**

Write at least 3 recommended next actions. Each must name:
1. The specific action (namespace, topic, or contributor target)
2. The achievement or milestone it unlocks

Format:
```
## Next Actions

1. **[Action]** → unlocks **[Achievement/Milestone name]**
   _Why_: [one sentence — what gap this closes]

2. **[Action]** → unlocks **[Achievement/Milestone name]**
   _Why_: [one sentence]

3. **[Action]** → unlocks **[Achievement/Milestone name]**
   _Why_: [one sentence]
```

Generic advice ("add more signals") does not count. Name the namespace and topic.

**Step 6 — Close Gaps (1-away callouts)**

Before writing the artifact, scan for any achievement or milestone that is close to earned.
If any topic is 1 signal away from `Signal Depth`, or 1 contributor away from `Team Topic`,
or 1 namespace away from `shared coverage` — call it out with a quantified gap:

```
## Almost There

- [Topic/Milestone]: needs [exact count] more [thing] to unlock **[Achievement]**
```

If nothing is close, write: `No close-to-unlock gaps detected.`

**Step 7 — Write artifact**

Write the complete output to:
`simulations/corps/achievements-{{date}}.md`

Frontmatter:
```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
---
```

---

## V-02 — Phrasing Register: Conversational Game-Badge Framing

**Axis**: Phrasing register
**Hypothesis**: Reframing achievements as unlockable badges with playful but precise language
increases readability for team audiences (the `team` audience listed in the skill spec).
Conversational framing with visual badge markers (✓ earned / ○ locked) satisfies C-06 separation
naturally. The risk is weaker C-05 precision — game language may soften the specificity of next
actions. This variation prioritizes C-04 leaderboard completeness by making it the first thing
the team sees.

---

You are running `corps-achievements`. No inputs needed — you'll scan the workspace yourself.

Start by globbing `simulations/` for all signal artifacts. Collect topic paths (any subdirectory
with `.md` files) and note any contributor information embedded in frontmatter or filenames.
If the workspace is empty, say so up front and still produce all sections below.

---

**What the team has earned this sprint**

Open with a brief sentence (one line) stating the scan date and how many topics were found.
Example: "Scanned on {{date}} — found [n] active topics."

Then show the badge board. Group by earned (✓) vs locked (○):

```
### Earned Badges ✓

**[Topic name]**
  ✓ First Signal — first artifact filed
  ✓ Signal Depth — 3+ signals on record
  [list all earned badges for this topic]

**[Topic name]**
  ✓ ...

### Locked Badges ○ — what's next

**[Topic name]**
  ○ Signal Depth — need [n] more signals
  ○ Team Topic — need a second contributor
  [list locked badges and what's missing]

**[Topic name]**
  ○ ...
```

Every topic found in the scan must appear in one of the two groups. A topic not listed is an
error — if it has nothing earned and nothing locked, put it in the Locked group with a note.

Badge definitions:
- **First Signal** — earned at 1 signal
- **Signal Depth** — earned at 3 signals
- **Full Sweep** — earned when signals span 3+ distinct namespaces
- **Solo Pioneer** — earned when exactly one contributor owns all signals for this topic
- **Team Topic** — earned when 2+ contributors have each contributed at least one signal

---

**Team Milestones**

Check whether the team as a whole has hit these three milestones. Use their exact names:

- **first team signal** — Has any signal been filed by any contributor? ✓ earned / ○ not yet
- **shared coverage** — Have 2+ contributors each contributed to 2+ topics? ✓ earned / ○ not yet
- **debate starter** — Has any topic received signals from 2+ namespaces that raise different
  angles? ✓ earned / ○ not yet

For each: say what the evidence is (file path or "no evidence found") and what is needed
to earn it if not yet unlocked.

---

**Leaderboard — {{date}}**

Who's leading the signal count?

```
## Top Contributors

1. [Contributor or "unknown"] — [n] signals, [n] topics
2. ...
(show all detected contributors, even if just one)
```

If no contributor metadata is available in the workspace, write one entry:
`1. (no contributor metadata detected) — signals counted, names unknown`

---

**Unlock these next**

Pick the 3 highest-leverage next actions. For each, name what you do, and name the badge or
milestone it unlocks:

> **Do this**: [Specific action — what namespace, what topic, who should do it]
> **Unlocks**: [Badge or milestone name]
> **Gap**: [One sentence on why this is the highest-leverage next step]

No generic advice. If the action is "file a scout signal," say: "File a `scout-competitors`
signal for topic X" — not just "add more scout signals."

---

**One team-level insight**

Close with a single sentence that draws a cross-topic or cross-contributor conclusion:
something the numbers tell you that no single topic view would show. Examples:
- "Alice spans 4 topics — highest breadth on the team."
- "The `flow` namespace has 100% team participation — the only namespace with this."
- "Three topics are each 1 signal away from Signal Depth — a single focused sprint could unlock all three."

Write the insight as a named sentence, not as a bullet list of stats.

---

**Write the artifact**

Save to: `simulations/corps/achievements-{{date}}.md`

```yaml
---
skill: corps-achievements
date: {{date}}
---
```

---

## V-03 — Lifecycle Emphasis: Explicit Phase Gates

**Axis**: Lifecycle emphasis
**Hypothesis**: Naming each phase explicitly (SCAN → COMPUTE → MILESTONES → LEADERBOARD →
RECOMMENDATIONS) and requiring a gate check before proceeding forces completeness on C-01 and
C-02. Each phase has entry conditions that cannot be skipped. This is the variation most likely
to pass C-01 on a sparse workspace (it explicitly handles the empty case at SCAN gate).
The cost is verbosity — the phase structure may produce longer output but reduces the most
common failure mode: skipping a topic.

---

You are running `corps-achievements`. No arguments — the skill scans and computes from workspace
state.

Work through the phases in order. Each phase has an entry condition. If the entry condition is
not met, state why and halt with a diagnostic message rather than proceeding with incomplete data.

---

### PHASE 1 — SCAN

**Entry condition**: `simulations/` directory accessible.

Glob `simulations/**/*.md`. For each `.md` file found:
- Extract the topic path (the subdirectory under `simulations/`, e.g. `scout/competitors`)
- Extract contributor identity from frontmatter (`author:`, `contributor:`) or filename prefix
- Record the namespace (first path segment under `simulations/`)

Build an internal registry:
```
REGISTRY:
  topics: [list of unique topic paths]
  contributors: [deduplicated list or "not detectable"]
  namespaces_active: [list]
  total_signals: [n]
```

**SCAN GATE**: If `simulations/` is empty or absent, output:
> "SCAN GATE: No signal artifacts found. Workspace is empty or simulations/ is not present.
> All achievement sections will show as empty. Milestone statuses will be NOT YET. Proceeding."
Then continue to Phase 2 with an empty registry. Do not halt.

**SCAN GATE**: If `simulations/` has files, confirm:
> "SCAN GATE: [n] signals found across [n] topics, [n] namespaces, [n] contributors."
Then proceed to Phase 2.

---

### PHASE 2 — COMPUTE ACHIEVEMENTS

**Entry condition**: SCAN GATE confirmed.

For each topic in the registry, compute which achievements are earned:

| Achievement | Condition |
|-------------|-----------|
| First Signal | >= 1 signal file for this topic |
| Signal Depth | >= 3 signal files for this topic |
| Full Sweep | signals span >= 3 distinct namespaces for this topic |
| Solo Pioneer | exactly 1 contributor for this topic AND >= 1 signal |
| Team Topic | >= 2 contributors with >= 1 signal each for this topic |

Output section:

```
## Achievements by Topic — Sprint {{date}}

### Earned

[For each topic with at least one earned achievement:]
**[topic path]** ([n] signals)
  - [Achievement name]: [brief evidence — file count, contributor count, etc.]

### Available (not yet earned)

[For each topic with zero earned achievements, or achievements close to earning:]
**[topic path]** ([n] signals)
  - ○ [Achievement name]: needs [specific gap]
```

Every topic from the registry must appear in Earned or Available. Omitting a topic is a
PHASE 2 gate failure.

**COMPUTE GATE**: After listing all topics, state:
> "COMPUTE GATE: [n] topics processed. [n] achievements earned. [n] achievement gaps identified."

---

### PHASE 3 — MILESTONES

**Entry condition**: COMPUTE GATE confirmed.

Report all three named team milestones. Use their exact names as given here — do not rephrase:

```
## Team Milestones

**first team signal**
  Status: [EARNED / NOT YET]
  Evidence: [file path of first signal filed, or "none"]
  Missing: [what is needed, or "—"]

**shared coverage**
  Status: [EARNED / NOT YET]
  Condition: 2+ contributors each active in 2+ topics
  Evidence: [contributor names and topic counts, or "none"]
  Missing: [contributor or topic gap, or "—"]

**debate starter**
  Status: [EARNED / NOT YET]
  Condition: at least one topic has signals from 2+ namespaces
  Evidence: [topic path and namespace list, or "none"]
  Missing: [what namespace or topic is needed, or "—"]
```

**MILESTONES GATE**: After all three:
> "MILESTONES GATE: [n/3] milestones earned."

---

### PHASE 4 — LEADERBOARD

**Entry condition**: MILESTONES GATE confirmed.

```
## Contributor Leaderboard — {{date}}

| Rank | Contributor | Signals | Topics | Namespaces |
|------|-------------|---------|--------|------------|
| 1 | [name] | [n] | [n] | [list] |
...
```

If contributor metadata is unavailable: write one row indicating this explicitly. Do not omit
the section.

**LEADERBOARD GATE**: State:
> "LEADERBOARD GATE: [n] contributors ranked. Metadata source: [frontmatter / filename / not available]."

---

### PHASE 5 — RECOMMENDATIONS

**Entry condition**: LEADERBOARD GATE confirmed.

Write at least 3 recommended next actions. Each must pass this test before being written:
- Does it name a specific namespace and topic (not just "add signals")?
- Does it name the exact achievement or milestone it unlocks?

Format:
```
## Recommended Next Actions

1. **[Action — namespace, topic, contributor target]**
   → Unlocks: **[Achievement or Milestone name]**
   Rationale: [one sentence linking this action to the specific gap from Phase 2 or 3]

2. ...

3. ...
```

Then, add a close-to-unlock block:

```
## Almost There (1 away)

[List any achievement or milestone where the gap is exactly 1 unit:]
- [Topic/Milestone] — needs [1 more signal / 1 more contributor / 1 more namespace] to unlock **[Achievement]**

[If nothing is 1 away: "No single-step unlocks available — review Phase 2 gaps for multi-step paths."]
```

Then, add one cross-signal insight:

```
## Team Insight

[One sentence drawing a conclusion that spans topics or contributors — not a per-topic stat.
 Example: "Two contributors have disjoint topic coverage — pairing on one shared topic would
 unlock Team Topic across both."]
```

**RECOMMENDATIONS GATE**: State:
> "RECOMMENDATIONS GATE: [n] actions written. [n] close-to-unlock gaps identified."

---

### WRITE ARTIFACT

Write the complete output (all five phases) to:
`simulations/corps/achievements-{{date}}.md`

Frontmatter:
```yaml
---
skill: corps-achievements
date: {{date}}
phases_completed: 5
topics_scanned: [n]
---
```

---

## V-04 — Role Sequence + Inertia Framing (Combination)

**Axis**: Role sequence (skeptic before leaderboard) + inertia framing (stagnation as named competitor)
**Hypothesis**: Running a "signal skeptic" lens before building the team leaderboard surfaces the
status-quo competitor (teams that don't gather signals systematically) as a named threat. The
skeptic primes next actions to be explicitly anti-inertia — not just "add signals" but "break
the specific stagnation pattern identified." This combination is strongest on C-05 (action quality)
and C-10 (cross-contributor insight), because both emerge from a role that names the team's
inertia rather than just counting badges.

---

You are running `corps-achievements`. No inputs. Scan and compute.

You will work through three roles in sequence. Do not skip ahead to a role until the prior
role's output is complete.

---

### ROLE 1 — SIGNAL ARCHAEOLOGIST

Your job: find what exists. Produce only factual findings — no judgments yet.

Glob `simulations/**/*.md`. For each file, note:
- Topic path (directory under `simulations/`)
- Namespace (first segment)
- Contributor if detectable (frontmatter or filename)
- Date if detectable

Output:

```
## Signal Archaeology — {{date}}

Topics discovered: [n]
Namespaces active: [list]
Contributors identified: [list or "not detectable"]
Total signals: [n]

Signal inventory:
[For each topic:]
  [topic path] — [n] signals — contributors: [list or "unknown"] — namespaces: [list]
```

If `simulations/` is empty: "Signal Archaeology: workspace is empty. No signals on record."
Proceed to Role 2 anyway.

---

### ROLE 2 — STATUS-QUO CHALLENGER

**Null behavior**: What does a team that skips systematic signal gathering look like?

Before computing any achievements, name the stagnation pattern this workspace shows (or risks
showing). Answer these questions in 2-3 sentences:

1. What is the team doing instead of filing signals? (Implicit from the scan: few files? one
   contributor? one namespace? no activity at all?)
2. What decision quality does this produce compared to a team with full signal coverage?
3. What is the cost of continuing at the current rate — by the end of the sprint, what will
   be unknown?

Then state the **Stagnation Pattern** (one of: *Empty Start*, *Lone Wolf*, *Namespace Tunnel*,
*Stale Coverage*, or name your own if none fits) and carry it forward into the recommendations.

```
## Status-Quo Assessment

Stagnation Pattern: [name]
Evidence: [what in the scan supports this — file count, single contributor, etc.]
Cost of inertia: [one sentence — what stays unknown if nothing changes]
```

---

### ROLE 3 — ACHIEVEMENT COMPILER

Your job: produce the achievement dashboard from the archaeology findings. The stagnation
pattern from Role 2 must inform the next actions you generate.

**Achievements by Topic**

For each topic from the Signal Archaeology:

```
## Achievements

### Earned ✓
[topic] ([n] signals)
  ✓ [Badge name] — [evidence]

### Locked ○
[topic] ([n] signals)
  ○ [Badge name] — needs [gap]
```

Every topic must appear. No topic may be omitted.

Badge definitions:
- **First Signal** — >= 1 signal
- **Signal Depth** — >= 3 signals
- **Full Sweep** — signals span >= 3 namespaces
- **Solo Pioneer** — 1 contributor, >= 1 signal
- **Team Topic** — 2+ contributors with 1+ signal each

**Team Milestones**

Address all three by exact name:

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|----------|
| first team signal | EARNED / NOT YET | [evidence or "—"] |
| shared coverage | EARNED / NOT YET | [evidence or "—"] |
| debate starter | EARNED / NOT YET | [evidence or "—"] |
```

**Contributor Leaderboard — {{date}}**

```
| Rank | Contributor | Signals | Topics | Namespaces |
|------|-------------|---------|--------|------------|
```

If no metadata available: one row, explicit statement.

**Next Actions (anti-inertia)**

Generate 3+ actions. Each action must:
- Name a specific namespace and topic
- Name the achievement or milestone it unlocks
- Include one sentence that ties back to the **Stagnation Pattern** identified in Role 2

Format:
```
## Anti-Inertia Next Actions

1. **[Action — namespace, topic]**
   → Unlocks: **[Achievement/Milestone]**
   → Breaks: **[Stagnation Pattern]** because [one sentence]

2. ...

3. ...
```

**Close-to-unlock**

```
## Almost There

[Any gap of exactly 1 unit:]
- [topic/milestone]: needs [1 more X] to unlock **[Achievement]**

[If none: "No 1-step unlocks detected."]
```

**Team insight**

One sentence, cross-topic or cross-contributor, stated as a named conclusion. Must differ
from the stagnation pattern statement — this is a positive observation or structural finding,
not a problem statement.

**Write artifact**

`simulations/corps/achievements-{{date}}.md`

```yaml
---
skill: corps-achievements
date: {{date}}
stagnation_pattern: [name from Role 2]
---
```

---

## V-05 — Output Format + Lifecycle Emphasis (Combination)

**Axis**: Output format (prose dashboard with embedded headers) + lifecycle emphasis (phases
as explicit section headers that double as table of contents)
**Hypothesis**: Prose sections with named headers (rather than tables) produce richer C-10
cross-contributor insights because each section ends with a synthesizing sentence rather than
a cell value. The lifecycle phase headers create a scanning structure that satisfies C-06
(earned/available separation) and C-03 (milestones) without requiring separate tables. This
combination is strongest on C-10 and C-09, and weakest on C-02 auditability — a missing topic
is less visible in prose than in a table.

---

You are running `corps-achievements`. No arguments. Scan the workspace, then produce a
team achievement dashboard.

---

### Section 1 — Scan Summary _({{date}})_

Open with a two-sentence scan summary stating: how many topics were found, which namespaces
are active, and how many contributors are identifiable.

Then list discovered topics as a flat bullet list — one line each:
```
- simulations/[topic path] — [n] signals — [contributor(s) or "unknown"]
```

If `simulations/` is empty or absent, say so here and proceed with empty data.

This list is the scan record. Every topic in this list must appear in Section 2. A topic
present here that is absent in Section 2 is an error.

---

### Section 2 — Achievements by Topic

Write one subsection per discovered topic. Use `####` headers. Each subsection has two
paragraphs:

**Earned** paragraph: Name every earned achievement as inline bold text followed by brief
evidence. If nothing is earned, write: "No achievements earned yet."

**Available** paragraph: Name every locked achievement as inline text preceded by ○, with
the specific gap quantified. If all achievements are earned, write: "No locked achievements."

Achievement definitions:
- **First Signal** — earned at 1+ signal
- **Signal Depth** — earned at 3+ signals
- **Full Sweep** — earned when signals span 3+ distinct namespaces
- **Solo Pioneer** — earned when exactly 1 contributor, 1+ signal
- **Team Topic** — earned when 2+ contributors, 1+ signal each

Use these exact names. Do not paraphrase.

---

### Section 3 — Team Milestones

Write a paragraph for each of the three named milestones. Use the exact milestone name as
a bold inline label. State: earned or not-yet-earned, evidence (file path or contributor count),
and if not yet earned — what must happen to earn it.

**first team signal**: [earned/not-yet + evidence + gap if any]

**shared coverage**: [earned/not-yet + evidence + gap if any]

**debate starter**: [earned/not-yet + evidence + gap if any]

All three must be present. Do not rename or abbreviate.

---

### Section 4 — Contributor Leaderboard _(week of {{date}})_

Write a brief narrative opening: one sentence naming the most active contributor (or
"contributor metadata not available" if no attribution found).

Then a table:

```
| Rank | Contributor | Signals | Topics | Breadth (namespaces) |
|------|-------------|---------|--------|----------------------|
```

After the table, write one sentence drawing a contributor-level observation — not a repeat
of the table data, but a conclusion drawn from comparing rows. Example: "The gap between first
and second place is [n] signals — the leaderboard is [tight / spread]."

If no contributor metadata: one row indicating this, plus the sentence: "Attribution data is
unavailable; signal counts are topic-level only."

---

### Section 5 — Almost There (1-Away Gaps)

Write one paragraph. Name any achievement or milestone that requires exactly one more action
to unlock. Quantify each gap precisely: "1 more signal", "1 more contributor", "1 more namespace".

If no gaps are within 1 step: "No single-step unlocks available. The closest gap is [gap
description] in topic [name]."

---

### Section 6 — Next Actions

Write at least 3 next actions as a numbered list. Each must follow this format:

> **[Verb phrase — specific namespace and topic]** → unlocks **[Achievement or Milestone name]**
> [One sentence rationale linking the action to the specific gap in Section 2 or Section 3.]

No generic actions. "File a signal" must be followed by a namespace and topic name.

---

### Section 7 — Team Insight

Write exactly one paragraph (3-5 sentences) drawing a cross-topic or cross-contributor
conclusion. This insight must not be derivable from any single-topic view. Draw it from the
patterns visible across the full scan.

Name the insight in the opening sentence. Use specific numbers and topic/contributor names.
End with a recommended implication: what the team should do based on this insight.

---

### Write artifact

`simulations/corps/achievements-{{date}}.md`

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
milestones_earned: [n]/3
---
```
