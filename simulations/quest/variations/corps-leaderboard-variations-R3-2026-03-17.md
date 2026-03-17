R3 variations written. Here's the summary:

---

## R3 Variation Map

All 5 variations carry C-13 (named completion gate) and C-14 (N/A prohibition) as baseline — these are no longer differentiating axes.

| | Variation | Core Axis | Key Differentiator |
|--|-----------|-----------|-------------------|
| **V-01** | Achievement Matrix | Output format | Rows=topics, columns=5 achievement types; ✓ vs `–N` cell notation replaces per-topic prose sections |
| **V-02** | Signal Health Score | Inertia framing | 0–5 quantified score with urgency tier (Healthy/Monitor/Alert/Critical); score table uses pattern vocabulary as condition labels |
| **V-03** | CLI Terminal Dashboard | Phrasing register | Symbol-coded terse output (`//ROLE`, `//GATE`, `[1] unlocks:` etc.); tests whether register weakens C-09/C-10 |
| **V-04** | Leaderboard-First | Role sequence | Leaderboard runs before inertia diagnosis; tests C-11 with non-standard ordering (inertia before topic compilation is satisfied, just not before leaderboard) |
| **V-05** | SITREP Briefing | Output format + register | Military briefing template (SITUATION → ASSESSMENT → FINDINGS → ACTIONS → DEBRIEF); "ASSESSMENT must close before FINDINGS opens. No exceptions." |

**Expected scoring**: All 5 should score 100/100 against v3, since C-13/C-14 are explicitly built into every variation. The scorecard will reveal whether any axis introduces subtle failures — V-01 (C-09 risk in tabular format), V-02 (C-10 pattern naming prominence), V-03 (terse register vs prose-requiring criteria), V-04 (leaderboard-first sequencing), V-05 (DEBRIEF position for C-09).
 role gates |

---

## V-01 — Output Format: Achievement Matrix

**Axis**: Output format — single cross-tab achievement matrix replacing per-topic prose sections
**Hypothesis**: A topics × achievements matrix — rows are discovered topics, columns are the five
defined achievement types — makes C-01 and C-02 compliance structurally guaranteed: a missing
topic is a visible missing row, a missing achievement type is a missing column. The matrix
satisfies C-06 through cell-level notation (✓ vs gap count) rather than section separation.
The inertia role structure from R2 is carried forward to satisfy C-11, C-13, and C-14. Risk:
C-09 synthesis is harder in tabular format — compensated by a mandatory post-matrix Team Insight
step with cross-row constraint.

---

You are running `corps-leaderboard`. No inputs — scan and compute from workspace state.

---

### PRE-WORK — WORKSPACE SCAN

Glob `simulations/**/*.md`. For every `.md` file record:
- **topic** — subdirectory path under `simulations/` (e.g., `scout/competitors`)
- **namespace** — first path segment under `simulations/`
- **contributor** — `author:` or `contributor:` from YAML frontmatter; or filename prefix before
  first `-`; or `"unknown"`
- **date** — YYYY-MM-DD from filename

Build an internal artifact table:

```
ARTIFACT TABLE (internal)
  [topic path] | [signal count] | contributors: [list or "unknown"] | namespaces: [list]
  ...
  TOTALS: [n] topics | [n] signals | [n] namespaces | [n] contributors
```

If `simulations/` is empty or absent, record `workspace empty` and continue — all output
sections must still appear.

---

### ROLE 1 — INERTIA DIAGNOSTICIAN

**Position: Role 1. Completion gate required before Role 2 (Matrix Compiler) may begin.**

Using the Artifact Table, evaluate all five stagnation patterns:

| Pattern | Trigger |
|---------|---------|
| Empty Start | 0 artifacts total |
| Lone Wolf | one contributor accounts for >= 80% of all artifacts |
| Namespace Tunnel | one namespace accounts for >= 70% of all artifacts |
| Stale Coverage | all artifacts have dates >= 14 days before today |
| Shallow Spread | >= 5 distinct topics each with exactly 1 artifact |

Report all patterns that match. If multiple match, list all. If none match, write "None detected"
and cite the specific counts that clear each.

Write this block to output immediately:

```
## Inertia Diagnosis

**Detected Pattern(s)**: [name(s) or "None detected"]
**Evidence**: [one sentence per pattern — specific counts from Artifact Table]
**Blind Spot**: [one sentence — which achievement or milestone this pattern makes hardest to reach]
```

**Completion gate: Inertia Diagnosis block written. Role 2 (Matrix Compiler) may not begin
until this block appears in output.**

---

### ROLE 2 — MATRIX COMPILER

**Entry condition: Role 1 completion gate confirmed.**

Build a Markdown achievement matrix. One row per topic from the Artifact Table. Five achievement
columns.

Cell notation:
- `*` — achievement earned
- `–N sig` — locked, needs N more signals (e.g., `–2 sig`)
- `–N ns` — locked, needs N more namespaces
- `–N contrib` — locked, needs N more contributors
- `?` — cannot determine (metadata unavailable — add a footnote)

Achievement thresholds (use exact column names — paraphrasing fails):

| Column | Earned when |
|--------|------------|
| First Signal | signals >= 1 |
| Signal Depth | signals >= 3 |
| Full Sweep | distinct namespaces >= 3 |
| Solo Pioneer | contributors == 1 AND signals >= 1 |
| Team Topic | contributors >= 2, each with >= 1 signal |

```
## Achievement Matrix

| Topic | First Signal | Signal Depth | Full Sweep | Solo Pioneer | Team Topic |
|-------|-------------|-------------|-----------|-------------|-----------|
| [path] | * | –2 sig | –1 ns | * | –1 contrib |
```

Every topic from the Artifact Table must appear as a row. A topic in the Artifact Table but
absent from the matrix is a matrix gap.

Add a totals footer row:
```
| **TOTALS (earned)** | [n] | [n] | [n] | [n] | [n] |
```

If `simulations/` was empty, produce the header and column names with note:
"No topics found — all cells empty."

**Completion gate: Matrix written with one row per topic. Proceed to Role 3.**

---

### ROLE 3 — MILESTONE INSPECTOR

**Entry condition: Role 2 completion gate confirmed.**

Evaluate all three team milestones using exact names — do not paraphrase or abbreviate:

| Milestone | Earned if | Evidence to cite |
|---|---|---|
| first team signal | any artifact exists | path to earliest-dated file |
| shared coverage | any topic has >= 2 contributors | topic path + contributor count |
| debate starter | any topic has artifacts from >= 2 distinct namespaces | topic path + namespace list |

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|---------|
| first team signal | EARNED / NOT YET | [path or "none"] |
| shared coverage | EARNED / NOT YET | [topic + count or "none"] |
| debate starter | EARNED / NOT YET | [topic + namespaces or "none"] |
```

**Completion gate: All three milestones present with exact names. Proceed to Role 4.**

---

### ROLE 4 — LEADERBOARD BUILDER

**Entry condition: Role 3 completion gate confirmed.**

Aggregate contributors from the Artifact Table. Rank descending by total signal count. Ties
broken by topics covered (descending).

```
## Contributor Leaderboard

| Rank | Contributor | Signals | Topics | Namespaces |
|------|-------------|---------|--------|-----------|
| 1    | [name]      | [n]     | [n]    | [list]    |
```

If no contributor metadata is extractable from frontmatter or filename:
`| -- | no contributor metadata found | -- | -- | -- |`

Do not omit this section regardless of workspace state.

**Completion gate: Leaderboard written. Proceed to Role 5.**

---

### ROLE 5 — ACTION PLANNER

**Entry condition: Role 4 completion gate confirmed.**
**Input: Pattern(s) from Role 1 + locked matrix cells from Role 2 + NOT YET milestones from Role 3.**

Write at least 3 next actions. Each action uses this three-field template:

```
## Next Actions

1. **`{namespace}/{topic}`** — [action description]
   -> Field 1 — Unlocks: **{exact achievement or milestone name}**
   -> Field 2 — Breaks: **{pattern name from Role 1}**
   -> Field 3 — Why: [one sentence linking this action to the specific gap in the matrix]

2. ...

3. ...
```

**No action may omit Field 2. "N/A" is not valid.** If Role 1 detected no pattern, Field 2
names the pattern this action prevents and states why prevention matters now.

**Completion gate: >= 3 actions written, each with all three fields.**

---

### POST-ROLES — 1-AWAY GAPS

From locked cells in the matrix (Role 2) and NOT YET milestones (Role 3), list every item
exactly 1 unit from being earned:

```
## 1-Away Gaps

| Topic / Milestone | Achievement | Current | Needed | To unlock |
|---|---|---|---|---|
| [path] | Signal Depth | 2 signals | 3 | Add 1 signal in `{namespace}` |
```

If nothing is 1 step away: "No 1-away gaps found. Closest: [topic] needs [n] more [unit]
for **[Achievement]**."

---

### POST-ROLES — TEAM INSIGHT

Write one synthesizing sentence visible only by reading across multiple rows of the matrix —
not from any single row. Must reference >= 2 topics or contributors, cite >= 1 specific number,
and close with a recommended implication.

```
## Team Insight

[Synthesizing sentence + recommended implication]
```

---

### WRITE ARTIFACT

Write the complete output to: `simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [name or "none"]
---
```

---

## V-02 — Inertia Framing: Signal Health Score

**Axis**: Inertia framing — quantified stagnation score (0–5) as primary inertia mechanism
**Hypothesis**: Computing a numeric Signal Health Score (0–5, one point per fired stagnation
condition) provides richer inertia diagnosis than categorical naming alone — the score
communicates urgency intensity (0=Healthy through 5=Critical) and allows actions to address
scored conditions in priority order. The score table uses the pattern vocabulary as condition
labels, satisfying C-10 while adding quantitative weight. The score is the C-13 gate: "Signal
Health Score must appear before per-topic compilation begins." C-14 is satisfied through
per-action N/A prohibition. Risk: C-10 pass condition requires a named pattern — the score
table provides pattern names, but their prominence is different from a dedicated pattern
diagnosis block; this is the axis under test.

---

You are running `corps-leaderboard`. No inputs — scan and compute from workspace state.

Produce the Signal Health Score before any per-topic compilation begins.

---

### PRE-WORK — WORKSPACE SCAN

Glob `simulations/**/*.md`. For each file record:
- **topic** — subdirectory path under `simulations/`
- **namespace** — first path segment under `simulations/`
- **contributor** — `author:` or `contributor:` from YAML frontmatter; or filename prefix before
  first `-`; or `"unknown"`
- **date** — YYYY-MM-DD from filename

Internal registry:

```
SCAN REGISTRY (internal)
  topics: [list]
  per topic: { signal_count, contributors, namespaces, most_recent_date }
  all_contributors: [deduplicated]
  all_namespaces: [deduplicated]
  total_signals: [n]
  most_recent_date: [date or "none"]
```

If `simulations/` is empty or absent, record `{workspace: empty}` and continue through all
steps — every section must still appear.

---

### STEP 1 — SIGNAL HEALTH SCORE

**Position: first step. This block must appear in output before Step 3 (per-topic compilation)
begins. Step 3 may not begin until this block is written.**

Check each of the five stagnation conditions. Add one point for each condition that fires:

| Score | Condition Label | Fires when |
|-------|----------------|-----------|
| +1 | Empty Start | total_signals == 0 |
| +1 | Lone Wolf | one contributor accounts for >= 80% of total_signals (excluding "unknown") |
| +1 | Namespace Tunnel | one namespace accounts for >= 70% of total_signals |
| +1 | Stale Coverage | most_recent_date is >= 14 days before today |
| +1 | Shallow Spread | >= 5 topics each with exactly 1 signal |

Sum all fired conditions. Record specific evidence for each fired condition.

```
## Signal Health Score

| Condition | Fires? | Evidence |
|-----------|--------|---------|
| Empty Start | YES / NO | [count or "--"] |
| Lone Wolf | YES / NO | [contributor name + % or "--"] |
| Namespace Tunnel | YES / NO | [namespace + % or "--"] |
| Stale Coverage | YES / NO | [most recent date or "--"] |
| Shallow Spread | YES / NO | [topic count + single-signal count or "--"] |

**Score: [n]/5**

**Tier:**
- 0 -> Healthy -- no stagnation detected; deepen existing coverage
- 1-2 -> Monitor -- patterns emerging; address within the sprint
- 3-4 -> Alert -- signal discipline breaking down; prioritize intervention now
- 5 -> Critical -- full stagnation; team has lost signal momentum entirely

**Active patterns**: [list of fired condition labels, comma-separated, or "none"]
**Primary pattern**: [highest-priority fired condition, or "none"]
**What this blocks**: [one sentence -- which achievement or milestone is most at risk given the active patterns]
```

**Completion gate: Signal Health Score written. Step 3 may not begin until this block
appears in output.**

---

### STEP 2 — CONTRIBUTOR LEADERBOARD

Rank contributors descending by total signal count. Ties broken by topics covered.

```
## Contributor Leaderboard

| Rank | Contributor | Signals | Topics | Namespaces |
|------|-------------|---------|--------|-----------|
| 1    | [name]      | [n]     | [n]    | [list]    |
```

If no contributor metadata is extractable:
`| -- | no contributor metadata found | -- | -- | -- |`

Do not omit this section.

---

### STEP 3 — PER-TOPIC ACHIEVEMENTS

**Entry condition: Signal Health Score from Step 1 confirmed.**

For every topic in the scan registry, evaluate all five achievements. Show earned and locked
in separate subsections. State the exact gap for every locked achievement.

Achievement definitions (use exact names — paraphrasing fails):

| Achievement | Earned when |
|-------------|-----------|
| First Signal | signals >= 1 |
| Signal Depth | signals >= 3 |
| Full Sweep | distinct namespaces >= 3 |
| Solo Pioneer | contributors == 1 AND signals >= 1 |
| Team Topic | contributors >= 2, each with >= 1 signal |

```
## Per-Topic Achievements

### [topic path]

**Earned** (check)
- [Achievement name] -- [evidence]

**Locked** (circle)
- [Achievement name] -- needs [exact gap, e.g., "2 more signals", "1 more namespace"]
```

Every topic from the scan registry must appear. Do not merge earned and locked.

---

### STEP 4 — TEAM MILESTONES

Check all three milestones using exact names — do not paraphrase:

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|---------|
| first team signal | EARNED / NOT YET | [path or "none"] |
| shared coverage | EARNED / NOT YET | [topic + contributor count or "none"] |
| debate starter | EARNED / NOT YET | [topic + namespace list or "none"] |
```

---

### STEP 5 — 1-AWAY GAPS

From Steps 3 and 4, list every achievement or milestone exactly 1 unit from being earned:

```
## 1-Away Gaps

- [topic/milestone]: needs [1 more signal / 1 more contributor / 1 more namespace]
  to unlock **[Achievement name]**
```

If nothing is 1 step away: "No 1-away gaps. Closest: [topic] needs [n] more [unit]
for **[Achievement]**."

---

### STEP 6 — NEXT ACTIONS

Write at least 3 targeted actions. Each uses this three-field template — all fields required:

```
## Next Actions

1. **`{namespace}/{topic}`** -- [action description]
   -> Unlocks: **{exact achievement or milestone name}**
   -> Breaks: **{condition label from Step 1 Active Patterns list}**
   -> Priority: [score tier -- Critical / Alert / Monitor / Healthy]

2. ...

3. ...
```

**No action may omit the Breaks field. "N/A" is not valid.** If Step 1 detected no active
patterns (score = 0), the Breaks field writes `prevents: {pattern name}` and states the
prevention rationale in one clause.

Prioritize actions by health score tier: a score of 3 or higher means address all fired
conditions, not just the easiest.

---

### STEP 7 — TEAM INSIGHT

Write one sentence visible only by comparing across topics or contributors — not from any
single-topic section. Must reference >= 2 topics or contributors, cite >= 1 specific number,
and close with a recommended implication for the team.

```
## Team Insight

[Synthesizing sentence + recommended implication]
```

---

### WRITE ARTIFACT

`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
health_score: [n]/5
health_tier: [Healthy / Monitor / Alert / Critical]
active_patterns: [list or "none"]
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
---
```

---

## V-03 — Phrasing Register: CLI Terminal Dashboard

**Axis**: Phrasing register — terse terminal-output style with symbol-coded status
**Hypothesis**: A CLI-style register maximizes information density per line, making all
structural completeness criteria visible at a glance through symbol codes. The terse format
disciplines the output to put data before narrative. Risk: C-09 (synthesizing insight) and
C-10 (pattern narrative) require prose sentences that feel out of register — dedicated labeled
blocks (PATTERN:, INSIGHT:) compensate without breaking the dashboard aesthetic. C-13 is
satisfied through named gate annotations in the role labels. C-14 through the per-action
field-number prohibition. This variation tests whether register alone can cause criteria
failures when structural mechanisms are otherwise intact.

---

You are running `corps-leaderboard`. No arguments. Scan the workspace and produce a
terminal-style team signal dashboard. Output is terse: tables and symbol-coded blocks.
Prose is permitted only in the PATTERN block, the INSIGHT block, and action rationale fields.

---

### // SCAN

Glob `simulations/**/*.md`. For each file record:
- topic: subdirectory path under `simulations/`
- namespace: first path segment
- contributor: `author:` or `contributor:` from frontmatter; or filename prefix before
  first `-`; or `"unknown"`
- date: YYYY-MM-DD from filename

Internal artifact table. If `simulations/` is empty: record `{workspace: empty}` and produce
all sections with empty state.

---

### // ROLE 1 -- PATTERN DETECTOR
### // position: first -- completion gate fires before // ROLE 2 -- COMPILER begins

Evaluate all five stagnation conditions. Check all. Report all that match.

| Pattern | Condition | Status |
|---------|-----------|--------|
| Empty Start | total_signals == 0 | MATCH / -- |
| Lone Wolf | 1 contributor >= 80% signals | MATCH / -- |
| Namespace Tunnel | 1 namespace >= 70% signals | MATCH / -- |
| Stale Coverage | most recent artifact >= 14d old | MATCH / -- |
| Shallow Spread | >= 5 topics each with exactly 1 signal | MATCH / -- |

Write this block:

```
## PATTERN

active:     [pattern names, comma-separated, or "none"]
evidence:   [one sentence -- specific counts]
constraint: [one sentence -- which achievement or milestone this blocks]
```

**// GATE: PATTERN block written. // ROLE 2 -- COMPILER may not begin.**

---

### // ROLE 2 -- COMPILER
### // entry condition: // GATE from // ROLE 1 confirmed

For every topic in the artifact table, compute all five achievements. Output as compact
per-topic blocks.

Achievement codes:
- `*` -- earned
- `o -N` -- locked (N units short; N=0 impossible by definition)
- `?` -- indeterminate (metadata gap; add footnote)

Achievement definitions (exact names required -- paraphrasing fails):
- **First Signal** -- signals >= 1
- **Signal Depth** -- signals >= 3
- **Full Sweep** -- distinct namespaces >= 3
- **Solo Pioneer** -- contributors == 1, signals >= 1
- **Team Topic** -- contributors >= 2, each >= 1 signal

```
## ACHIEVEMENTS

[topic path]
  First Signal  : * / o -N sig / ?
  Signal Depth  : * / o -N sig / ?
  Full Sweep    : * / o -N ns / ?
  Solo Pioneer  : * / o -N contrib / ?
  Team Topic    : * / o -N contrib / ?

[next topic]
  ...
```

Every topic from the scan must appear. Missing topic = compiler gap.

**// GATE: All topics compiled. Proceed to // ROLE 3.**

---

### // ROLE 3 -- MILESTONE CHECK
### // entry condition: // GATE from // ROLE 2 confirmed

Check all three milestones using exact names -- renaming or abbreviating fails:

```
## MILESTONES

first team signal : EARNED [path] / NOT YET [what is needed]
shared coverage   : EARNED [topic + contributor count] / NOT YET [what is needed]
debate starter    : EARNED [topic + namespace pair] / NOT YET [what is needed]
```

**// GATE: All three milestones checked with exact names. Proceed to // ROLE 4.**

---

### // ROLE 4 -- LEADERBOARD
### // entry condition: // GATE from // ROLE 3 confirmed

Rank descending by signal count. Ties broken by topics covered.

```
## LEADERBOARD

rank  contributor           signals  topics  namespaces
----  --------------------  -------  ------  ----------
1     [name]                [n]      [n]     [list]
...
```

If no contributor metadata: one row:
`  --  no contributor metadata found  --  --  --`

Do not omit this section.

**// GATE: Leaderboard written. Proceed to // ROLE 5.**

---

### // ROLE 5 -- ACTIONS
### // entry condition: // GATE from // ROLE 4 confirmed
### // input: active patterns from // ROLE 1 + locked achievements from // ROLE 2
###           + NOT YET milestones from // ROLE 3

Write at least 3 next actions. Each uses this three-field format:

```
## ACTIONS

-> `{namespace}/{topic}` -- [action description]
   [1] unlocks: {exact achievement or milestone name}
   [2] breaks:  {pattern name from PATTERN block}
   [3] why:     [one sentence linking action to the specific gap]

-> ...
```

**No action may omit field [2]. "N/A" is not valid.** If PATTERN detected no active
patterns, field [2] writes `prevents: {pattern name}` and states the prevention rationale
in one clause.

---

### // 1-AWAY

From locked achievements and NOT YET milestones, list every item exactly 1 step from
unlocking:

```
## 1-AWAY

  [topic/milestone] -> +1 sig -> unlocks Signal Depth
  [topic/milestone] -> +1 contrib -> unlocks Team Topic
  ...
```

If nothing is 1 step away:
`no 1-away gaps | closest: [topic] needs [n] [unit] for {Achievement}`

---

### // INSIGHT

Write one sentence that requires reading across multiple topics or contributors simultaneously
-- not from any single topic. Must cite >= 1 number and >= 1 name. End with a recommended
action for the team.

```
## INSIGHT

[Synthesizing sentence + recommended implication]
```

---

### // WRITE

`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
active_patterns: [list or "none"]
---
```

---

## V-04 — Role Sequence: Leaderboard-First + Inertia Framing

**Axis**: Role sequence (leaderboard runs before inertia diagnosis) + inertia framing
**Hypothesis**: Running the leaderboard as Role 1 — before the Inertia Diagnostician — primes
the reader with the "who contributed" picture before the pattern is named. A Lone Wolf pattern
visible in the leaderboard data is confirmed rather than announced by the diagnosis. The
sequencing tests whether C-11 (inertia before topic compilation) passes when leaderboard
runs first: C-11 constrains inertia vs topic compilation order, not inertia vs leaderboard
order. C-13 is satisfied through the explicit gate between Role 2 (Inertia Diagnostician)
and Role 3 (Topic Compiler). C-14 through the per-action N/A prohibition in Role 5.

---

You are running `corps-leaderboard`. No inputs. Scan and compute from workspace state.

Five roles execute in pipeline order. Each role completes fully before the next begins.
Do not reorder roles.

---

### PRE-WORK — WORKSPACE SCAN

Glob `simulations/**/*.md`. For every file record:
- **topic** — subdirectory path under `simulations/`
- **namespace** — first path segment under `simulations/`
- **contributor** — `author:` or `contributor:` from YAML frontmatter; or filename prefix
  before first `-`; or `"unknown"`
- **date** — YYYY-MM-DD from filename

Artifact table:

```
ARTIFACT TABLE (internal)
  [topic] -- [n signals] -- contributors: [list or "unknown"] -- ns: [list]
  ...
  TOTALS: [n] topics | [n] signals | [n] contributors | [n] namespaces
```

If `simulations/` is empty or absent, record `workspace empty` and continue — all five
roles must still produce output.

---

### ROLE 1 — LEADERBOARD BUILDER

**Purpose: establish who is contributing before the team assesses the pattern.**

For each contributor in the artifact table compute: total signal count, distinct topics
covered (list), distinct namespaces used (list), most recent artifact date.

Rank descending by signal count. Ties broken by topics covered.

```
## Contributor Leaderboard

| Rank | Contributor | Signals | Topics | Namespaces | Last Active |
|------|-------------|---------|--------|-----------|------------|
| 1    | [name]      | [n]     | [n]    | [list]    | [date]     |
```

If no contributor metadata:
`| -- | no contributor metadata found | -- | -- | -- | -- |`

**Completion gate: Leaderboard written. Proceed to Role 2.**

---

### ROLE 2 — INERTIA DIAGNOSTICIAN

**Position: Role 2. Completion gate required before Role 3 (Topic Compiler) may begin.**

Reading the leaderboard from Role 1 alongside the Artifact Table, evaluate all five
stagnation patterns:

| Pattern | Trigger |
|---------|---------|
| Empty Start | 0 artifacts total |
| Lone Wolf | one contributor accounts for >= 80% of total signals |
| Namespace Tunnel | one namespace accounts for >= 70% of total signals |
| Stale Coverage | all artifacts have dates >= 14 days before today |
| Shallow Spread | >= 5 distinct topics each with exactly 1 artifact |

Report all matching patterns with evidence. If none match, write "None detected" and cite
the specific counts that clear each pattern. Where the leaderboard from Role 1 corroborates
a detected pattern, note the corroboration explicitly (e.g., "leaderboard confirms Lone Wolf:
[contributor] holds [n]/[total] signals").

Write this block to output immediately:

```
## Inertia Diagnosis

**Detected Pattern(s)**: [name(s) or "None detected"]
**Evidence**: [one sentence per pattern -- cite specific counts; reference leaderboard data
               where relevant]
**What this locks out**: [one sentence -- which achievement or milestone is hardest to reach
                         given this pattern]
```

**Completion gate: Inertia Diagnosis written. Role 3 (Topic Compiler) may not begin until
this block appears in output.**

---

### ROLE 3 — TOPIC COMPILER

**Entry condition: Role 2 completion gate confirmed.**

For every distinct topic in the Artifact Table, evaluate all five achievements. Show earned
and locked in separate subsections. State the exact numeric gap for every locked achievement.

Achievement definitions (use exact names):

| Achievement | Earned when |
|-------------|-----------|
| First Signal | signals >= 1 |
| Signal Depth | signals >= 3 |
| Full Sweep | distinct namespaces >= 3 |
| Solo Pioneer | contributors == 1, signals >= 1 |
| Team Topic | contributors >= 2, each >= 1 signal |

```
## Per-Topic Achievements

### [topic path]

**Earned** (check)
- [Achievement name] -- [evidence]

**Locked** (circle)
- [Achievement name] -- needs [exact gap]
```

Every topic from the Artifact Table must appear. Do not merge earned and locked.

**Completion gate: All topics have sections. Proceed to Role 4.**

---

### ROLE 4 — MILESTONE INSPECTOR

**Entry condition: Role 3 completion gate confirmed.**

Check all three milestones using exact names — do not paraphrase or abbreviate:

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|---------|
| first team signal | EARNED / NOT YET | [path or "none"] |
| shared coverage | EARNED / NOT YET | [topic + contributor count or "none"] |
| debate starter | EARNED / NOT YET | [topic + namespace list or "none"] |
```

**Completion gate: All three milestones present with exact names. Proceed to Role 5.**

---

### ROLE 5 — ACTION PLANNER

**Entry condition: Role 4 completion gate confirmed.**
**Input: Pattern(s) from Role 2 + locked achievements from Role 3 + NOT YET milestones
from Role 4.**

Write at least 3 next actions. Each action uses this three-field template:

```
## Next Actions

1. **`{namespace}/{topic}`** -- [action description]
   -> Unlocks: **{exact achievement or milestone name}**
   -> Breaks: **{pattern name from Role 2}**
   -> Rationale: [one sentence linking the action to the specific gap]

2. ...

3. ...
```

**No action may omit the Breaks field. "N/A" is not valid.** If Role 2 detected no pattern,
the Breaks field names the pattern this action prevents and states the prevention rationale
in one clause.

**Completion gate: >= 3 actions written, each with all three fields.**

---

### POST-ROLES — 1-AWAY GAPS

From locked achievements (Role 3) and NOT YET milestones (Role 4), extract every item
exactly 1 step from being earned:

```
## 1-Away Gaps

| Topic / Milestone | Achievement | Current | Needed | Next Move |
|---|---|---|---|---|
| [path] | Signal Depth | 2 of 3 signals | 3 | Add 1 signal in `{namespace}` |
```

If nothing is 1 step away: "No 1-away gaps. Closest: [topic] needs [n] more [unit]
for **[Achievement]**."

---

### POST-ROLES — TEAM INSIGHT

Write one synthesizing sentence drawing a conclusion only visible from comparing across
topics or contributors — not from any single-topic section. Reference >= 2 topics or
contributors, cite >= 1 specific number, close with a recommended implication.

```
## Team Insight

[Synthesizing sentence + recommended implication]
```

---

### WRITE ARTIFACT

`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [name or "none"]
---
```

---

## V-05 — Output Format + Phrasing Register: Signal Briefing

**Axes**: Output format (military briefing structure) + phrasing register (direct, declarative)
**Hypothesis**: A named briefing structure — SITUATION, ASSESSMENT, FINDINGS, ACTIONS, DEBRIEF
— enforces C-11 through the template itself: ASSESSMENT (inertia diagnosis) is a named section
that must close before FINDINGS (per-topic achievements) opens, making the ordering a template
constraint rather than a role pipeline. C-13 is satisfied by the explicit section constraint
("ASSESSMENT must close before FINDINGS opens. No exceptions."). The declarative register
disciplines completeness through briefing conventions — missing a section reads as a protocol
failure, not just an omission. C-14 through the per-action N/A prohibition in ACTIONS. Risk:
C-09 (synthesizing insight) surfaces in DEBRIEF after all findings, which is expected in
briefing format but tests whether the rubric's "not visible from any single-topic view"
constraint is satisfied from that position.

---

You are producing a Signal Briefing for the team. A Signal Briefing follows a five-section
structure. Each section is named. Each section closes before the next opens — this is a
briefing discipline constraint, not a formatting suggestion.

Work through the sections in order. When a section closes, state the closing indicator
before opening the next.

---

### PRE-BRIEF — WORKSPACE SCAN

Before producing any briefing section, scan the workspace.

Glob `simulations/**/*.md`. For each file record:
- **topic** — subdirectory path under `simulations/`
- **namespace** — first path segment
- **contributor** — `author:` or `contributor:` from YAML frontmatter; or filename prefix
  before first `-`; or `"unknown"`
- **date** — YYYY-MM-DD from filename

Internal inventory:

```
INVENTORY (internal)
  topics: [list]
  per topic: { signals, contributors, namespaces }
  all_contributors: [deduplicated]
  total_signals: [n]
  most_recent_date: [date or "none"]
```

If `simulations/` is empty or absent, record `{workspace: empty}` and produce all sections
with empty state.

---

### SECTION 1 — SITUATION

Open the briefing. Two paragraphs maximum.

**Paragraph 1**: State the scan results in plain declarative language — how many topics,
signals, contributors, namespaces. If workspace is empty, state this explicitly.

**Paragraph 2**: State what the contributor picture looks like at a glance. Produce the
ranked contributor table:

```
## SITUATION -- Contributor Leaderboard

| Rank | Contributor | Signals | Topics | Namespaces |
|------|-------------|---------|--------|-----------|
```

Rank descending by signal count. If no contributor metadata:
`| -- | no contributor metadata found | -- | -- | -- |`

**SITUATION closes here. ASSESSMENT opens next.**

---

### SECTION 2 — ASSESSMENT

**Position: second section. ASSESSMENT must close before FINDINGS opens. No exceptions.**

Assess the team's signal-gathering health. Name the stagnation pattern — or confirm there
is none.

Evaluate all five patterns:

| Pattern | Trigger |
|---------|---------|
| Empty Start | total_signals == 0 |
| Lone Wolf | one contributor >= 80% of total_signals |
| Namespace Tunnel | one namespace >= 70% of total_signals |
| Stale Coverage | most_recent_date >= 14 days before today |
| Shallow Spread | >= 5 topics each with exactly 1 signal |

Write this assessment block:

```
## ASSESSMENT

**Pattern**: [name(s) -- all that match -- or "None detected"]
**Evidence**: [one sentence per active pattern, with specific counts]
**Decision risk**: [one sentence -- which commitment or decision the team cannot safely
                   make at current signal coverage]
**What to watch for in FINDINGS**: [one sentence -- which locked achievements or milestones
                                   are most explained by this pattern]
```

If no pattern is active, state "None detected" and cite the evidence that clears each
condition.

**ASSESSMENT closes here. FINDINGS opens next.**

---

### SECTION 3 — FINDINGS

**Entry condition: ASSESSMENT closed.**

Report achievements per topic, team milestones, and 1-away gaps.

#### 3A — Per-Topic Achievements

For every topic from the inventory, evaluate all five achievements. Earned and locked in
separate subsections — do not merge. State exact gap for every locked achievement.

Achievement definitions (exact names required):

| Achievement | Earned when |
|-------------|-----------|
| First Signal | signals >= 1 |
| Signal Depth | signals >= 3 |
| Full Sweep | distinct namespaces >= 3 |
| Solo Pioneer | contributors == 1, signals >= 1 |
| Team Topic | contributors >= 2, each >= 1 signal |

```
## FINDINGS -- Per-Topic Achievements

### [topic path]
**Earned** (check): [list or "none"]
**Locked** (circle): [Achievement name] -- needs [exact gap]
```

Every topic must appear. A missing topic is a findings gap.

#### 3B — Team Milestones

Use exact milestone names. Do not paraphrase.

```
## FINDINGS -- Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|---------|
| first team signal | EARNED / NOT YET | [path or "none"] |
| shared coverage | EARNED / NOT YET | [topic + count or "none"] |
| debate starter | EARNED / NOT YET | [topic + namespaces or "none"] |
```

#### 3C — 1-Away Gaps

Every achievement or milestone exactly 1 step from being earned:

```
## FINDINGS -- 1-Away Gaps

- [topic/milestone]: needs [1 more X] to unlock **[Achievement name]**
```

If none: "No 1-away gaps. Closest: [topic] needs [n] more [unit] for **[Achievement]**."

**FINDINGS closes here. ACTIONS opens next.**

---

### SECTION 4 — ACTIONS

**Entry condition: FINDINGS closed.**

Write at least 3 prioritized actions. Each action uses this template — all three fields
required:

```
## ACTIONS

1. **`{namespace}/{topic}`** -- [action description]
   -> Unlocks: **{exact achievement or milestone name}**
   -> Breaks: **{pattern name from ASSESSMENT}**
   -> Context: [one sentence connecting this action to the specific gap identified in FINDINGS]

2. ...

3. ...
```

**No action may omit the Breaks field. "N/A" is not valid.** If ASSESSMENT detected no
active pattern, Breaks states `prevents: {pattern name}` and explains the prevention
rationale in one clause.

**ACTIONS closes here. DEBRIEF opens next.**

---

### SECTION 5 — DEBRIEF

**Entry condition: ACTIONS closed.**

Write one synthesizing statement visible only from the full briefing — not from any single
FINDINGS subsection. Must reference >= 2 topics or contributors, cite >= 1 specific number,
and close with a recommended implication for the team.

```
## DEBRIEF

[Synthesizing sentence + recommended implication]
```

---

### WRITE ARTIFACT

Write the complete briefing (Sections 1–5) to:
`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [name or "none"]
sections_completed: 5
---
```
