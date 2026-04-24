---
skill: quest-variate
skill_target: corps-leaderboard
round: 14
date: 2026-03-17
rubric_version: 11
---

# Variate R14 — corps-leaderboard

5 complete prompt body variations for the `corps-leaderboard` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

**R13 ceiling against v11**: All 5 variations achieve 100.00 (23/23). Universal ceiling holds.
The v11 rubric is fully saturated — all axes explored across R12 and R13 produce equivalent
scores. Ceiling-breaking opportunities require patterns not yet captured in C-01–C-31.

**R13 seeds entering R14**:
- Seed A: `resolves: {flag-name}` on inertia-flag-resolving actions — universal (5/5 R13).
- Seed B: Pre-synthesis cross-dimensional reconciliation pairing — universal (5/5 R13).
- Seed H: Severity-ordered health topic reporting (critical → warning → healthy) — universal
  (5/5 R13 design targets).
- Seed I: Cross-role discrepancy validation table (Assessor flag vs. Inspector health finding)
  — 2/5 R13 (V-02, V-05). Carry in R14 V-05.
- Seed J: Stub-conformance markers `[CONFORMS: {section}]` — 1/5 R13 (V-03). Not carried.
- Seed K: Tiered action output (`[CRITICAL]` / `[WARNING]` / `[ADVANCING]`) — 2/5 R13
  (V-04, V-05). Carry in R14 V-04, V-05.
- Seed L: Insight projection test (anchored vs. extrapolated scope declaration) — 1/5 R13
  (V-05). Carry in R14 V-05.

**New seeds introduced in R14**:
- Seed M: Action-to-gap binding — each action row declares `[closes: {achievement} gap of
  {N} {unit} for {topic_path}]`, binding the action directly to a quantified threshold delta
  rather than just an achievement name. Team milestone actions state `[closes: {milestone} —
  {requirement summary}]`. Actions with no quantifiable gap write `[closes: N/A]`.
- Seed N: Milestone proximity ladder — for each NOT YET milestone, a breakdown of the exact
  remaining preconditions with individual action counts needed. Extends nearest-miss coverage
  from the achievement dimension into the team milestone dimension.
- Seed O: Insight confidence band — the Team Insight sentence is followed on the next line by
  `[confidence: HIGH/MEDIUM/LOW] [supporting observations: {N}]`. HIGH = 3+ independent
  observations from health and inertia data; MEDIUM = 2; LOW = 1 or single-data-point inference.
- Seed R: Leaderboard velocity column — adds `velocity` column (`rising` / `steady` /
  `stalled` / `unknown`) to the contributor leaderboard, inferred by cross-referencing each
  contributor's files against the stale signal table.
- Seed S: Echo detection check — after the Health Phase, a consistency scan verifies that
  Health Phase achievement claims are not structurally contradicted by the Inertia Phase flag
  assignments in ways the discrepancy check does not cover (e.g., `healthy-momentum` raised
  AND Solo Pioneer EARNED — mutually exclusive conditions).

**R14 design targets**:
- All 5 variations carry Seeds A+B+H as formalized universal requirements.
- V-01: Phrasing register (conversational field-report prose for health blocks, replacing
  achievement tables). 3-role. Seeds A+B+H. New: Seed O. Expected: 23/23.
- V-02: Output format (ASCII gap progress bars on achievement table + nearest-miss). 3-role.
  Seeds A+B+H. New: Seed M. Expected: 23/23.
- V-03: Role sequence (leaderboard computed in Analyst with velocity column; 4-role). Seeds
  A+B+H. New: Seed R. Expected: 23/23.
- V-04: Combination (inertia-first lifecycle + tiered actions + milestone proximity ladder).
  4-role. Seeds A+B+H+K. New: Seeds M+N. Expected: 23/23.
- V-05: Full integration (5-role + inertia-first + Seeds A+B+H+I+K+L formalized + Seeds
  M+N+O+R+S all introduced). Expected: 23/23.

**Expected scoring against v11** (formula: `90 + (passed/23) × 10`):
- V-01: 23/23 → **100.00**
- V-02: 23/23 → **100.00**
- V-03: 23/23 → **100.00**
- V-04: 23/23 → **100.00**
- V-05: 23/23 → **100.00**

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Phrasing register (conversational field-report prose for health blocks) + Seed O | V-01 |
| Output format (ASCII gap progress bars) + Seed M | V-02 |
| Role sequence (early leaderboard in Analyst + velocity column) + Seed R | V-03 |
| Combination: inertia-first + tiered actions + Seeds M+N | V-04 |
| Full integration: 5-role + inertia-first + Seeds M+N+O+R+S | V-05 |

---

## V-01 — Field-Report Phrasing Register + 3-Role Pipeline + Seeds A+B+H + Seed O

**Axis**: Phrasing register
**Hypothesis**: All R13 variations use technical tabular format (5-row achievement table) for
per-topic health blocks. This variation replaces those tables with "field report" prose
assessments — each topic block is a structured narrative paragraph that states all five
achievements by their exact names in conversational prose rather than table rows. The hypothesis
is that prose-form health blocks force the model to compose rather than fill-in cells,
potentially producing more coherent LOCKED unlock-path explanations, and that removing the
table scaffold tests whether format structure (column headers, row alignment) is load-bearing
for achievement name accuracy. Seed O is new: the Team Insight sentence is followed on a new
line by a confidence band declaring the strength of the supporting evidence
(`HIGH`/`MEDIUM`/`LOW` with supporting observation count).

---

You are running the **Corps Leaderboard** skill in a 3-role pipeline. Execute each role
completely before advancing to the next. No role may perform work assigned to another role.
Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: Within the Analyst role, the Inertia Phase (trajectory) runs BEFORE the
Health Phase (current state). After the Inertia Phase assigns severity tiers, the Health Phase
reports topics in descending severity order — critical first, then warning, then healthy.
Within each tier, sort alphabetically by `topic_path`. A flat alphabetical ordering across all
topics (ignoring severity) fails.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. The Archivist scans the workspace, builds the signal
registry, and constructs the contributor index. The Archivist does NOT evaluate achievements,
assess trajectory, rank contributors, or write insights or actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path segment after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path` (e.g., `scout`)
- `contributor` — resolve in priority order: frontmatter `author:` > frontmatter
  `contributor:` > filename prefix before first `-` > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. Roles 2 and 3 do not run.

Print registry as table: `topic_path | namespace | contributor | file`

After the registry, print namespace coverage:
`Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`

The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

### 1.2 — Contributor Index

Build a contributor-to-topics index. Print: `contributor | topic_path | file_count`.

**Archivist Gate** — Verify and emit before transferring artifacts:

- [ ] Registry table printed with all four columns (`topic_path`, `namespace`, `contributor`, `file`)
- [ ] Namespace coverage line printed with active and empty namespace lists
- [ ] Contributor index printed with all three columns

**Archivist Handoff** — The following artifacts transfer from the Archivist to the Analyst:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line (active and empty namespace lists)
3. Contributor index table (columns: `contributor`, `topic_path`, `file_count`)

The Analyst begins with these three artifacts. It does not re-scan the workspace.

---

## ROLE 2: ANALYST

**Responsibility**: Evaluation only. The Analyst first establishes trajectory (Inertia Phase),
then reports current state (Health Phase) in inertia-severity order using field-report prose.
Sub-phases are structurally separated — Inertia Phase content must not appear in Health Phase
prose and vice versa. The Analyst does NOT rank contributors, write insights, or write actions.

### 2.1 — Inertia Phase (RUNS FIRST)

Reports trajectory and momentum only. Does NOT include file counts, achievement statuses, or
coverage totals — those are current-state data belonging to the Health Phase.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Assign a severity tier per topic:
- `critical` — 2 or more flags raised (not counting healthy-momentum)
- `warning` — exactly 1 flag raised (not counting healthy-momentum)
- `healthy` — 0 non-momentum flags, or only healthy-momentum

Print inertia table: `topic_path | flags | trajectory note | severity`

A topic with no flags gets `flags = none`, a brief healthy momentum note, and
`severity = healthy`.

Print stale signal table: `topic_path | stale_status` (`stale` / `active` / `date-unknown`,
using file modification dates where accessible).

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

Classification: > 50% topics at `healthy` = increasing; < 25% = stalled; otherwise flat.

**Section 2.1 Gate** — Emit before proceeding to Section 2.2:

- [ ] Inertia table present with severity column; every topic evaluated for all four flags
- [ ] No static file counts, achievement statuses, or coverage totals in Inertia Phase content
- [ ] Stale signal table and velocity summary present

### 2.2 — Health Phase (RUNS SECOND — topics ordered by inertia severity)

Reports current signal state only using field-report prose. Does NOT include trajectory claims,
momentum language, or inertia flag restatements — those are trajectory data belonging to the
Inertia Phase.

**Topic ordering**: Report topics in descending severity order — `critical` first, then
`warning`, then `healthy`. Within each tier, sort alphabetically by `topic_path`.

For each `topic_path` (in severity order), write a health field report using this structure:

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Field Report — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9

{topic_path} currently has {N} signal file(s) across {M} namespace(s), contributed by
{contributor list}. **First Signal** is {EARNED / LOCKED — needs at least 1 file}. **Signal
Depth** is {EARNED / LOCKED — needs {X} more file(s) to reach 3}. **Full Sweep** is
{EARNED / LOCKED — needs signals in {X} more namespace(s) to reach 3}. **Solo Pioneer** is
{EARNED / LOCKED — needs exactly 1 contributor with at least 1 file}. **Team Topic** is
{EARNED / LOCKED — needs {X} more contributor(s) each with at least 1 file}.
```

Achievement names must be exact and bold — paraphrasing fails. Every LOCKED achievement must
state the specific unlock requirement inline; a field report that writes only "LOCKED" without
a requirement fails. EARNED achievements state the earned condition as evidence.

When Solo Pioneer is EARNED and Team Topic is NOT YET: append on a new line
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]`

Evaluate all three team milestones using exact names. Evidence must be non-empty for every row.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file exists in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

After the milestones table, print:
`Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count` for each active namespace.

### 2.3 — Nearest-Miss Assessment

- **Level 1** — every topic exactly 1 unit away from any achievement threshold. State: topic
  name + achievement name + exact gap. Sort ascending by gap.
- **Level 2** — closest topic 2 units away. Write Level 2 ONLY when no Level 1 topic exists.
  Explicitly state "Level 1: no topics are 1 unit away" before listing Level 2.

Print: `topic | achievement | gap | level`

**Section 2.2 Gate** — Emit before transferring artifacts:

- [ ] Topics reported in severity order (critical first, then warning, then healthy),
  alphabetical within tier; flat alpha ordering across tiers fails
- [ ] Every topic has a field report header with severity tier label and `Namespace diversity: {N}/9`
- [ ] Every topic's field report names all five achievements in bold with exact names; LOCKED
  achievements include inline unlock requirements; EARNED achievements state evidence
- [ ] No trajectory language, momentum claims, or inertia flag restatements in Health Phase
  field reports
- [ ] Inertia Phase table present; no static counts from Health Phase restated in inertia
  content (cross-contamination check)
- [ ] All three milestone names verbatim with non-empty evidence; debate starter proximity line
  and namespace leader table present
- [ ] Nearest-miss complete (Level 1, or Level 2 with "Level 1 empty" note), sorted ascending

**Analyst Handoff** — The following artifacts transfer from the Analyst to the Publisher:

1. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`, `severity`)
2. Stale signal table and velocity summary line
3. Per-topic Health Phase field reports, in severity order (one report per `topic_path`)
4. Team milestone table (3 rows: milestone, status, evidence)
5. Debate starter proximity line and namespace leader table
6. Nearest-miss assessment table (columns: `topic`, `achievement`, `gap`, `level`)

The Publisher begins with these six artifacts plus the Archivist's three. It does not
re-evaluate achievements or re-assess inertia.

---

## ROLE 3: PUBLISHER

**Responsibility**: Synthesis, leaderboard, reconciliation, insight, and actions only. Works
from all prior output. Does NOT re-scan the workspace, re-evaluate achievements, or re-assess
inertia.

### 3.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical. If all contributors
are `unknown`: write one row `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 3.2 — Collaboration Signal

Print: `topic_path | contributors | collaboration_type` for topics where Team Topic is earned.
Types: `pair` (exactly 2 contributors), `ensemble` (3+). If no topic earned Team Topic:
one row `| none | — | no Team Topic earned yet |`.

### 3.3 — Nearest-Miss Confirmation

Transcribe the nearest-miss table from the Analyst Handoff. Do not recompute.

### 3.4 — Cross-Dimensional Reconciliation

Before writing the Team Insight, select exactly one observation from the Health Phase field
reports and exactly one from the Inertia Phase table that interact with or bear on each other.
State how they interact.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase field reports} | {one finding from Inertia Phase} | {how they connect} |
```

### 3.5 — Team Insight

**Skeptic gate**: A Skeptic who has read all Archivist and Analyst output already knows: every
achievement status (from field reports), every milestone row, every inertia flag, every severity
tier, every trajectory note, the stale signal table, the velocity summary, the nearest-miss
assessment, the leaderboard, the collaboration signal table, and the reconciliation pairing in
3.4. The insight MUST contain something the Skeptic would not already know from all of that
material — including from the field report prose.

An insight that restates any field report achievement status, milestone status, inertia flag,
severity tier, velocity category, or reconciliation row fails. A passing insight surfaces a
second-order pattern — a risk, convergence, or cross-topic trajectory inference — requiring
synthesis across health and inertia data in a way no single field report or the reconciliation
pairing directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

After the insight sentence, append the confidence band on a new line:
`[confidence: HIGH/MEDIUM/LOW] [supporting observations: {N}]`

Assign: HIGH = insight is supported by 3 or more independent observations drawn from both
health and inertia data; MEDIUM = 2 independent observations; LOW = 1 observation or inference
from a single data point. Substitute actual count for {N}.

### 3.6 — Pre-Write Check

Before writing any action:

1. Identify all zero-score conditions: topics with 0 files, empty registry, empty leaderboard.
   Record each explicitly.
2. Identify all open inertia flags from the Analyst's Inertia Phase table, grouped by severity
   tier. Record each flag by topic and severity.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action whose primary purpose is eliminating a state where the output
would score zero carries the `prevents:` prefix. Advancement actions do not.

An action whose primary purpose is resolving an inertia flag MUST declare
`resolves: {flag-name}` where `{flag-name}` is the exact flag name (`stuck-at-first`,
`solo-hold`, or `namespace-thin`). Actions that do not resolve a specific flag leave
`resolves:` blank.

### 3.7 — Next Actions

Write at least 3 actions. Each must name: (1) a specific namespace and topic path, (2) the
exact achievement or milestone it unlocks (exact names only; paraphrasing fails). The
`prevents:` rule is embedded inside each relevant action row below as the second structurally
independent enforcement point.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank]
2. ...
3. ...
```

After all actions, output exactly this line (N = actual count of `prevents:`-prefixed actions):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Publisher Gate** — Verify and emit after the ACTIONS GATE line:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Collaboration signal table present (or "none" row if no Team Topic)
- [ ] Nearest-miss confirmation transcribed from Analyst Handoff
- [ ] Reconciliation pairing written: one Health observation (from field reports), one Inertia
  observation, interaction note
- [ ] Team Insight written as one sentence; confidence band on next line with HIGH/MEDIUM/LOW
  and actual observation count; Skeptic gate verified — Skeptic knew every achievement status
  (field reports), milestone, inertia flag, severity tier, trajectory note, stale signal,
  velocity, nearest-miss, leaderboard, collaboration, and reconciliation data; insight is a new
  cross-dimensional inference not derivable from any single block or the reconciliation pairing
- [ ] Pre-write check complete; zero-score conditions and open inertia flags identified before
  any action written; inertia flags grouped by severity tier in the pre-write log
- [ ] At least 3 actions; each names namespace + topic + exact achievement or milestone;
  `prevents:` applied per 3.6 and 3.7 (two independent enforcement points); `resolves:` applied
  to all inertia-flag-resolving actions with exact flag names; blank otherwise
- [ ] ACTIONS GATE line written with actual N count substituted

---

## V-02 — Gap Progress Bars + 3-Role Pipeline + Seeds A+B+H + Seed M

**Axis**: Output format
**Hypothesis**: All R13 variations express achievement gaps as numeric counts in a table column
(`gap: 1`). This variation introduces ASCII progress bars as a visual format alongside the
existing gap column: `[######----] 2/3` shows current progress toward the nearest threshold
as filled vs. empty blocks. The hypothesis is that visual gap representation forces the model
to compute progress fractions explicitly before rendering, and that the scanning pattern
changes — teams reading the output see the nearest-miss as a bar chart rather than a number,
potentially surfacing relative distance more naturally. Seed M is new: each action row declares
a `[closes: ...]` annotation that binds the action to the specific quantified gap it
eliminates, making the action layer traceable to a threshold delta rather than just an
achievement name.

---

You are running the **Corps Leaderboard** skill in a 3-role pipeline. Execute each role
completely before advancing to the next. No role may perform work assigned to another role.
Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: Within the Analyst role, the Inertia Phase (trajectory) runs BEFORE the
Health Phase (current state). The Health Phase reports topics in descending inertia severity
order — critical first, then warning, then healthy. Within each tier, sort alphabetically by
`topic_path`.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Scans workspace, builds signal registry, constructs
contributor index. Does NOT evaluate achievements, assess trajectory, rank contributors, or
write insights or actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path segment after `simulations/`
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. Roles 2 and 3 do not run.

Print registry as table: `topic_path | namespace | contributor | file`

Print namespace coverage:
`Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`

The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

### 1.2 — Contributor Index

Print: `contributor | topic_path | file_count`.

**Archivist Gate** — Verify and emit before transferring artifacts:

- [ ] Registry table with all four columns
- [ ] Namespace coverage line with active and empty lists
- [ ] Contributor index with all three columns

**Archivist Handoff** — The following artifacts transfer from the Archivist to the Analyst:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line (active and empty namespace lists)
3. Contributor index table (columns: `contributor`, `topic_path`, `file_count`)

The Analyst begins with these three artifacts. It does not re-scan the workspace.

---

## ROLE 2: ANALYST

**Responsibility**: Evaluation only. The Analyst first establishes trajectory (Inertia Phase),
then reports current state (Health Phase) in inertia-severity order. Sub-phases are
structurally separated. The Analyst does NOT rank contributors, write insights, or write
actions.

### 2.1 — Inertia Phase (RUNS FIRST)

Reports trajectory and momentum only. Does NOT include file counts, achievement statuses, or
coverage totals.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Assign severity tier:
- `critical` — 2+ flags (not counting healthy-momentum)
- `warning` — 1 flag (not counting healthy-momentum)
- `healthy` — 0 non-momentum flags, or only healthy-momentum

Print inertia table: `topic_path | flags | trajectory note | severity`

Print stale signal table: `topic_path | stale_status` (`stale` / `active` / `date-unknown`).

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

**Section 2.1 Gate** — Emit before proceeding to Section 2.2:

- [ ] Inertia table with severity column; every topic evaluated for all four flags
- [ ] No static file counts, achievement statuses, or coverage totals in Inertia Phase content
- [ ] Stale signal table and velocity summary present

### 2.2 — Health Phase (RUNS SECOND — ordered by severity tier)

Reports current signal state only. Does NOT include trajectory claims, momentum language, or
inertia flag restatements.

**Topic ordering**: critical first, then warning, then healthy. Alphabetical within each tier.

For each `topic_path` (in severity order), print:

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9
```

Evaluate all five achievements using exact names only. For every LOCKED achievement, state the
specific unlock requirement — a cell containing only `LOCKED` without a path fails.

**Progress bar format**: For achievements with a numeric threshold (Signal Depth: 3 files;
Full Sweep: 3 namespaces; Team Topic: 2 contributors), add a `Progress` column rendered as a
10-character bar: `[######----] {current}/{threshold}` where `#` fills blocks proportional to
current/threshold (round down). EARNED achievements write `[##########] COMPLETE`. Binary or
non-numeric achievements (First Signal, Solo Pioneer) write `N/A` in the Progress column.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file in topic |
| Signal Depth | >= 3 files in topic |
| Full Sweep | signals span >= 3 distinct namespaces |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

```
| Achievement   | Status  | Evidence / Unlock Path              | Progress           |
|---------------|---------|-------------------------------------|--------------------|
| First Signal  | ...     | ...                                 | N/A                |
| Signal Depth  | ...     | ...                                 | [##--------] 2/3   |
| Full Sweep    | ...     | ...                                 | [##--------] 1/3   |
| Solo Pioneer  | ...     | ...                                 | N/A                |
| Team Topic    | ...     | ...                                 | [##########] COMPLETE |
```

(Replace stub with actual values. Bar scale: 1 `#` per filled 10%-unit of current/threshold,
rounded down. 0/3 = `[----------]`; 1/3 = `[###-------]`; 2/3 = `[######----]`; 3/3 = `[##########]`.)

When Solo Pioneer is EARNED and Team Topic is NOT YET: append
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]`

Evaluate all three team milestones using exact names. Evidence non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

After milestones, print:
`Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count` for each active namespace.

### 2.3 — Nearest-Miss Assessment

- **Level 1** — every topic exactly 1 unit away from any achievement threshold. State: topic
  name + achievement name + gap + progress bar. Sort ascending.
- **Level 2** — closest topic 2 units away. Write Level 2 ONLY when no Level 1 exists.
  State "Level 1: no topics are 1 unit away" first.

Print: `topic | achievement | gap | level | progress`

The `progress` column uses the same `[######----] current/threshold` format as health blocks.

**Section 2.2 Gate** — Emit before transferring artifacts:

- [ ] Topics reported in severity order (critical → warning → healthy); alphabetical within tier
- [ ] Every topic has a health header with severity tier label and `Namespace diversity: {N}/9`
- [ ] Every topic has all five achievement rows with exact names; LOCKED rows include unlock
  paths; progress bars present for numeric-threshold achievements using 10-char bar format
- [ ] No trajectory language, momentum claims, or inertia flag restatements in Health Phase
- [ ] Inertia Phase table present; no static counts from Health Phase restated in inertia
  content (cross-contamination check)
- [ ] All three milestone names verbatim with non-empty evidence; debate starter proximity and
  namespace leader table present
- [ ] Nearest-miss complete (Level 1, or Level 2 with "Level 1 empty" note), sorted ascending,
  with progress bars in the `progress` column

**Analyst Handoff** — The following artifacts transfer from the Analyst to the Publisher:

1. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`, `severity`)
2. Stale signal table and velocity summary
3. Per-topic Health Phase achievement blocks (with progress bars), in severity order
4. Team milestone table (3 rows)
5. Debate starter proximity line and namespace leader table
6. Nearest-miss assessment table (columns: `topic`, `achievement`, `gap`, `level`, `progress`)

The Publisher begins with these six artifacts plus the Archivist's three. It does not
re-evaluate achievements or re-assess inertia.

---

## ROLE 3: PUBLISHER

**Responsibility**: Synthesis, leaderboard, reconciliation, insight, and actions only. Works
from all prior output. Does NOT re-scan, re-evaluate achievements, or re-assess inertia.

### 3.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical.
If all `unknown`: `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 3.2 — Collaboration Signal

Print: `topic_path | contributors | collaboration_type` for topics where Team Topic is earned.
Types: `pair` (2), `ensemble` (3+). If none: `| none | — | no Team Topic earned yet |`.

### 3.3 — Nearest-Miss Confirmation

Transcribe the nearest-miss table (including progress bars) from the Analyst Handoff. Do not
recompute.

### 3.4 — Cross-Dimensional Reconciliation

Select exactly one observation from the Health Phase and one from the Inertia Phase that
interact. State the interaction.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase} | {one finding from Inertia Phase} | {how they connect} |
```

### 3.5 — Team Insight

**Skeptic gate**: A Skeptic who has read all Archivist and Analyst output already knows: every
achievement status (with progress bars), every milestone row, every inertia flag, every severity
tier, every trajectory note, the stale signal table, the velocity summary, the nearest-miss
assessment (with progress bars), the leaderboard, the collaboration signal table, and the
reconciliation pairing in 3.4. The insight MUST contain something the Skeptic would not already
know from all of that material — including from the progress bar values.

An insight that restates any achievement count, progress bar value, milestone status, inertia
flag, velocity category, or reconciliation row fails. A passing insight surfaces a second-order
pattern requiring synthesis across health and inertia data in a way no single output block or
the reconciliation pairing directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

### 3.6 — Pre-Write Check

Before writing any action:

1. Identify all zero-score conditions: topics with 0 files, empty registry, empty leaderboard.
2. Identify all open inertia flags from the Analyst's Inertia Phase table, grouped by severity.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action eliminating a zero-score condition carries `prevents:`.

An action resolving an inertia flag MUST declare `resolves: {flag-name}` (exact flag name).
Other actions leave `resolves:` blank.

### 3.7 — Next Actions

Write at least 3 actions. Each must name: (1) namespace + topic path, (2) exact achievement
or milestone. The `prevents:` rule is the second structurally independent enforcement point
embedded in each relevant row.

Each action MUST also include a `[closes: ...]` annotation binding the action to its
quantified gap. Format: `[closes: {achievement} gap of {N} {unit} for {topic_path}]`.
Examples: `[closes: Signal Depth gap of 1 file for scout/competitors]`,
`[closes: Full Sweep gap of 2 namespaces for flow/trigger]`. Actions targeting a team
milestone write: `[closes: {milestone} — {brief requirement summary}]`. Actions with no
measurable numeric gap write `[closes: N/A]`.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank] [closes: {gap description}]
2. ...
3. ...
```

After all actions, output exactly this line (N = actual count of `prevents:`-prefixed actions):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Publisher Gate** — Verify and emit after the ACTIONS GATE line:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Collaboration signal table present (or "none" row)
- [ ] Nearest-miss confirmation transcribed with progress bars
- [ ] Reconciliation pairing: one Health observation, one Inertia observation, interaction note
- [ ] Team Insight as one sentence; Skeptic gate verified — Skeptic knew every achievement
  status (with progress bars), milestone, inertia flag, severity tier, trajectory note, stale
  signal, velocity, nearest-miss (with progress bars), leaderboard, collaboration, and
  reconciliation data; insight is new cross-dimensional inference
- [ ] Pre-write check complete; zero-score conditions and open inertia flags identified; grouped
  by severity tier
- [ ] At least 3 actions; each names namespace + topic + exact achievement or milestone;
  `prevents:` applied per 3.6 and 3.7 (two independent enforcement points); `resolves:` with
  exact flag names; `[closes: ...]` annotation on every action row; blank `resolves:` for
  non-inertia-flag actions
- [ ] ACTIONS GATE line with actual N substituted

---

## V-03 — Early Leaderboard in Analyst + Velocity Column + 4-Role Pipeline + Seeds A+B+H + Seed R

**Axis**: Role sequence
**Hypothesis**: All R13 variations compute the contributor leaderboard in the final synthesis
role (Publisher or Narrator), making leaderboard data unavailable during action-writing. This
variation moves leaderboard computation to the Analyst role, after the Health Phase — producing
a ranked contributor table as a Phase 2 artifact available to the Strategist when writing
actions. The hypothesis is that action-writing with leaderboard data at hand changes targeting:
the Strategist can identify lagging contributors and explicitly prioritize actions for their
topics, or flag solo-contributor topics where lower-ranked contributors could accelerate team
milestones. The Publisher role is then reduced to reconciliation and insight only. Seed R is
new: the leaderboard includes a `velocity` column (`rising` / `steady` / `stalled` / `unknown`)
inferred by cross-referencing each contributor's files against the Analyst's stale signal table.

---

You are running the **Corps Leaderboard** skill in a 4-role pipeline. Execute each role
completely before advancing to the next. No role may perform work assigned to another role.
Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: Within the Analyst role, the Inertia Phase runs BEFORE the Health Phase.
The Health Phase reports topics in descending severity order. After the Health Phase, the
Analyst computes the Contributor Leaderboard (with velocity column) before handing off to the
Strategist.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Scans workspace, builds signal registry, constructs
contributor index. Does NOT evaluate achievements, assess trajectory, rank contributors, write
insights, or write actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path segment after `simulations/`
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. All subsequent roles do
not run.

Print registry: `topic_path | namespace | contributor | file`

Print namespace coverage:
`Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`

The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

### 1.2 — Contributor Index

Print: `contributor | topic_path | file_count`.

**Archivist Gate** — Verify and emit:

- [ ] Registry table with all four columns
- [ ] Namespace coverage line with active and empty lists
- [ ] Contributor index with all three columns

**Archivist Handoff** — Artifacts to Analyst:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line
3. Contributor index (columns: `contributor`, `topic_path`, `file_count`)

The Analyst begins with these three artifacts. It does not re-scan the workspace.

---

## ROLE 2: ANALYST

**Responsibility**: Evaluation and leaderboard computation. Runs Inertia Phase first, then
Health Phase (in severity order), then computes the Contributor Leaderboard with velocity
column. Sub-phases are structurally separated. The Analyst does NOT write insights or actions.

### 2.1 — Inertia Phase (RUNS FIRST)

Reports trajectory and momentum only. Does NOT include file counts, achievement statuses, or
coverage totals.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Assign severity tier:
- `critical` — 2+ flags (not counting healthy-momentum)
- `warning` — 1 flag (not counting healthy-momentum)
- `healthy` — 0 non-momentum flags

Print inertia table: `topic_path | flags | trajectory note | severity`

Print stale signal table: `topic_path | stale_status` (`stale` / `active` / `date-unknown`).

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

**Section 2.1 Gate** — Emit before proceeding to Section 2.2:

- [ ] Inertia table with severity column; every topic evaluated for all four flags
- [ ] No static file counts, achievement statuses, or coverage totals in Inertia Phase content
- [ ] Stale signal table and velocity summary present

### 2.2 — Health Phase (RUNS SECOND — ordered by severity tier)

Reports current signal state only. Does NOT include trajectory claims, momentum language, or
inertia flag restatements.

**Topic ordering**: critical first, then warning, then healthy. Alphabetical within each tier.

For each `topic_path` (in severity order), print:

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9
```

Evaluate all five achievements. Exact names only. LOCKED rows must include specific unlock
requirements.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file |
| Signal Depth | >= 3 files |
| Full Sweep | >= 3 distinct namespaces |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

```
| Achievement   | Status  | Evidence / Unlock Path |
|---------------|---------|------------------------|
```

When Solo Pioneer EARNED and Team Topic NOT YET: append
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]`

Evaluate all three team milestones using exact names. Evidence non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count` for each active namespace.

### 2.3 — Nearest-Miss Assessment

- **Level 1** — every topic 1 unit away from any threshold (topic + achievement + gap). Sort
  ascending.
- **Level 2** — closest 2 units away. ONLY when no Level 1. State "Level 1: no topics are 1
  unit away" first.

Print: `topic | achievement | gap | level`

### 2.4 — Contributor Leaderboard with Velocity Column

Rank contributors descending by total signal count. Ties: alphabetical. If all `unknown`:
one row `| 1 | no contributor metadata found | — | — | — |`.

**Velocity assignment** — cross-reference each contributor's files against the stale signal
table from Section 2.1:
- `rising` — contributor has >= 1 `active` file AND total signal count >= 2
- `steady` — contributor has >= 1 `active` file but total signals = 1, OR mixed
  `active`/`date-unknown` with no `stale` files
- `stalled` — all of the contributor's files are `stale` or all are `date-unknown` with no
  `active` file and at least one confirmed `stale`
- `unknown` — all files are `date-unknown` (cannot determine from stale table)

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered | Velocity |
|------|-------------|---------------|----------------|----------|
```

**Section 2.2 Gate** (covers Sections 2.2, 2.3, and 2.4) — Emit before transferring artifacts:

- [ ] Topics in severity order (critical → warning → healthy), alphabetical within tier; each
  health header has severity label and `Namespace diversity: {N}/9`; all five achievement rows
  with exact names; LOCKED rows include unlock paths; no trajectory language
- [ ] Inertia Phase table present; no static counts from Health Phase restated in inertia
  content (cross-contamination check)
- [ ] All three milestone names verbatim with non-empty evidence; debate starter proximity and
  namespace leader table present
- [ ] Nearest-miss complete (Level 1, or Level 2 with "Level 1 empty" note), sorted ascending
- [ ] Contributor Leaderboard with all five columns including Velocity; velocity assigned per
  stale signal table cross-reference; `unknown` used only when all files are `date-unknown`

**Analyst Handoff** — Artifacts to Strategist:

1. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`, `severity`)
2. Stale signal table and velocity summary
3. Per-topic Health Phase achievement blocks in severity order
4. Team milestone table (3 rows: milestone, status, evidence)
5. Debate starter proximity line and namespace leader table
6. Nearest-miss assessment table (columns: `topic`, `achievement`, `gap`, `level`)
7. Contributor Leaderboard with Velocity column (columns: Rank, Contributor, Total Signals,
   Topics Covered, Velocity)

The Strategist begins with these seven artifacts plus the Archivist's three. It does not
re-evaluate achievements, re-assess inertia, or recompute the leaderboard.

---

## ROLE 3: STRATEGIST

**Responsibility**: Actions only. Produces the Next Actions list, using leaderboard velocity
data to inform action targeting. Does NOT produce collaboration map, reconciliation pairing,
or Team Insight — those belong to the Publisher.

### 3.1 — Nearest-Miss Confirmation

Transcribe the nearest-miss table from the Analyst Handoff. Do not recompute.

### 3.2 — Pre-Write Check

Before writing any action:

1. Identify all zero-score conditions: topics with 0 files, empty registry, empty leaderboard.
2. Identify all open inertia flags from the Analyst's inertia table, grouped by severity tier.
3. Note any `stalled` contributors from the leaderboard — these are candidates for targeted
   actions on their specific topics.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action eliminating a zero-score condition carries `prevents:`.
Advancement actions do not.

An action resolving an inertia flag MUST declare `resolves: {flag-name}` (exact flag name).
Other actions leave `resolves:` blank.

### 3.3 — Next Actions

Write at least 3 actions. Each must name: (1) namespace + topic path, (2) exact achievement
or milestone. The `prevents:` rule is the second structurally independent enforcement point
embedded in each relevant row.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank]
2. ...
3. ...
```

After all actions:

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Strategist Gate** — Verify and emit after the ACTIONS GATE line:

- [ ] Nearest-miss confirmation transcribed
- [ ] Pre-write check complete; zero-score conditions, open inertia flags (by severity tier),
  and stalled contributors noted
- [ ] At least 3 actions; each names namespace + topic + exact achievement or milestone;
  `prevents:` applied per 3.2 and 3.3 (two independent enforcement points); `resolves:` with
  exact flag names; blank otherwise
- [ ] ACTIONS GATE line with actual N substituted

**Strategist Handoff** — Artifacts to Publisher:

1. Nearest-miss assessment (confirmed from Analyst)
2. Next Actions list (all rows with `prevents:` and `resolves:` annotations)
3. Pre-write check results (zero-score conditions, open flags, stalled contributors)
4. ACTIONS GATE line

The Publisher begins with all output from Roles 1–3. It does not re-assess actions, inertia,
or recompute the leaderboard.

---

## ROLE 4: PUBLISHER

**Responsibility**: Synthesis only. Produces the Collaboration Signal, cross-dimensional
reconciliation pairing, and Team Insight. Does NOT re-scan, re-evaluate achievements,
re-assess inertia, or modify actions or the leaderboard.

### 4.1 — Collaboration Signal

Print: `topic_path | contributors | collaboration_type` for topics where Team Topic is earned.
Types: `pair` (2), `ensemble` (3+). If none: `| none | — | no Team Topic earned yet |`.

### 4.2 — Cross-Dimensional Reconciliation

Select exactly one observation from the Health Phase and one from the Inertia Phase that
interact. State the interaction.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase} | {one finding from Inertia Phase} | {how they connect} |
```

### 4.3 — Team Insight

**Skeptic gate**: The Skeptic has read all output from Roles 1–3 — every achievement status,
every milestone row, every inertia flag, every severity tier, every trajectory note, the stale
signal table, the velocity summary, the nearest-miss assessment, the leaderboard (including the
velocity column), all actions with `prevents:` and `resolves:` annotations, the collaboration
signal table, and the reconciliation pairing in 4.2. The insight MUST contain something the
Skeptic would not already know from all of that material — including from the leaderboard
velocity column.

An insight that restates any achievement count, leaderboard velocity value, inertia flag,
or reconciliation row fails. A passing insight surfaces a second-order pattern requiring
synthesis across health and inertia — including the trajectory dimension captured by the
velocity column — in a way no single output block or the reconciliation pairing directly
reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

**Publisher Gate** — Verify and emit:

- [ ] Collaboration signal table present (or "none" row)
- [ ] Reconciliation pairing: one Health observation, one Inertia observation, interaction note
- [ ] Team Insight as one sentence; Skeptic gate verified — Skeptic knew every achievement,
  milestone, inertia flag, severity tier, trajectory note, stale signal, velocity (including
  leaderboard velocity column), nearest-miss, all actions (with annotations), leaderboard,
  collaboration, and reconciliation data; insight is new cross-dimensional inference beyond all
  of that including the leaderboard velocity dimension

---

## V-04 — Combination: Inertia-First + Tiered Actions + 4-Role + Seeds A+B+H+K + Seeds M+N

**Axis**: Lifecycle emphasis + inertia framing + output format
**Hypothesis**: V-04 combines inertia-first lifecycle ordering (H), the tiered action output
structure (Seed K from R13), action-to-gap binding (Seed M), and the milestone proximity ladder
(Seed N). Seed N is the key new element: after the team milestones table, for every NOT YET
milestone, a proximity ladder breaks down the remaining preconditions into individual action
counts — not just the aggregate gap but the specific per-topic and per-contributor steps needed
to close each precondition. The hypothesis is that milestone proximity ladders help teams
understand coordination requirements: capturing `shared coverage` is not one action but a set
of parallel contributor additions across multiple topics, and making this explicit changes how
the Strategist prioritizes tiered action output.

---

You are running the **Corps Leaderboard** skill in a 4-role inertia-first pipeline. Execute
each role completely before advancing to the next. No role may perform work assigned to another
role. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: Within the Analyst role, the Inertia Phase runs BEFORE the Health Phase.
The Health Phase reports topics in descending severity order (critical → warning → healthy).

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Scans workspace, builds signal registry, builds
contributor index. Does NOT evaluate achievements, assess trajectory, rank contributors, write
insights, or write actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path after `simulations/`
- `namespace` — first segment
- `contributor` — `author:` > `contributor:` > filename prefix before first `-` > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop.

Print registry: `topic_path | namespace | contributor | file`

Print namespace coverage:
`Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`

The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

### 1.2 — Contributor Index

Print: `contributor | topic_path | file_count`.

**Archivist Gate** — Verify and emit:

- [ ] Registry table with all four columns
- [ ] Namespace coverage line with active and empty lists
- [ ] Contributor index with all three columns

**Archivist Handoff** — Artifacts to Analyst:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line
3. Contributor index (columns: `contributor`, `topic_path`, `file_count`)

---

## ROLE 2: ANALYST

**Responsibility**: Evaluation only. Runs Inertia Phase first (severity tiers established),
then Health Phase (topics in severity order, with milestone proximity ladders). Sub-phases
structurally separated. Does NOT rank contributors, write insights, or write actions.

### 2.1 — Inertia Phase (RUNS FIRST)

Reports trajectory and momentum only. Does NOT include file counts, achievement statuses, or
coverage totals.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Assign severity tier:
- `critical` — 2+ flags (not counting healthy-momentum)
- `warning` — 1 flag (not counting healthy-momentum)
- `healthy` — 0 non-momentum flags

Print inertia table: `topic_path | flags | trajectory note | severity`

Print stale signal table: `topic_path | stale_status`.

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

**Section 2.1 Gate** — Emit before proceeding to Section 2.2:

- [ ] Inertia table with severity column; every topic evaluated; no file counts or achievement
  statuses in Inertia Phase content (prohibited — current-state data)
- [ ] Stale signal table and velocity summary present

### 2.2 — Health Phase (RUNS SECOND — ordered by severity tier)

Reports current signal state only. Does NOT include trajectory claims, momentum language, or
inertia flag restatements.

**Topic ordering**: critical first, then warning, then healthy. Alphabetical within each tier.

For each `topic_path` (in severity order), print:

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9
```

Evaluate all five achievements. Exact names only. LOCKED rows must include unlock paths.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file |
| Signal Depth | >= 3 files |
| Full Sweep | >= 3 distinct namespaces |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

```
| Achievement   | Status  | Evidence / Unlock Path |
|---------------|---------|------------------------|
```

When Solo Pioneer EARNED and Team Topic NOT YET:
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]`

Evaluate all three team milestones using exact names. Evidence non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

For every NOT YET milestone, print a **Milestone Proximity Ladder** on the line immediately
following its table row:

- `first team signal` NOT YET:
  `Proximity ladder: 1 signal file in any namespace for any topic closes this milestone`
- `shared coverage` NOT YET: Count how many topics currently have >= 2 distinct contributors.
  State: `Proximity ladder: {N} qualifying topics (need 2 total). Remaining gap: {describe
  per-topic contributor deficits — e.g., topic A needs 1 more contributor, topic B needs
  2 more contributors}.`
- `debate starter` NOT YET: Identify the topic with the highest contributor count.
  State: `Proximity ladder: nearest is {topic_path} at {N}/3 contributors. Requires {M}
  additional contributor signals (each must be a distinct contributor not already listed).`

The proximity ladder appears inline after the NOT YET milestone row. EARNED milestones do not
receive a proximity ladder.

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count` for each active namespace.

### 2.3 — Nearest-Miss Assessment

- **Level 1** — every topic 1 unit away from any threshold (topic + achievement + gap). Sort
  ascending.
- **Level 2** — closest 2 units away. ONLY when no Level 1. State "Level 1: no topics are 1
  unit away" first.

Print: `topic | achievement | gap | level`

**Section 2.2 Gate** — Emit before transferring artifacts:

- [ ] Topics in severity order (critical → warning → healthy); alphabetical within tier; each
  health header includes severity label and `Namespace diversity: {N}/9`
- [ ] All five achievement rows per topic; exact names; LOCKED rows include unlock paths; no
  trajectory language in Health Phase
- [ ] Inertia Phase table present; no static counts from Health Phase restated in inertia
  content (cross-contamination check)
- [ ] All three milestone names verbatim with non-empty evidence; proximity ladders present
  for ALL NOT YET milestones; debate starter proximity and namespace leader table present
- [ ] Nearest-miss complete (Level 1, or Level 2 with "Level 1 empty" note), sorted ascending

**Analyst Handoff** — Artifacts to Strategist:

1. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`, `severity`)
2. Stale signal table and velocity summary
3. Per-topic Health Phase achievement blocks in severity order
4. Team milestone table (3 rows) with proximity ladders for NOT YET milestones
5. Debate starter proximity line and namespace leader table
6. Nearest-miss table (columns: `topic`, `achievement`, `gap`, `level`)

The Strategist begins with these six artifacts plus the Archivist's three.

---

## ROLE 3: STRATEGIST

**Responsibility**: Actions only. Produces a tiered Next Actions list with gap-binding
annotations. Does NOT produce leaderboard, reconciliation pairing, or Team Insight.

### 3.1 — Nearest-Miss Confirmation

Transcribe nearest-miss table from Analyst Handoff. Do not recompute.

### 3.2 — Pre-Write Check

Before writing any action:

1. Identify all zero-score conditions: topics with 0 files, empty registry, empty leaderboard.
2. Identify all open inertia flags from the Analyst's inertia table, grouped by severity tier.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action eliminating a zero-score condition carries `prevents:`.
Advancement actions do not.

An action resolving an open inertia flag MUST declare `resolves: {flag-name}` (exact flag
name: `stuck-at-first`, `solo-hold`, or `namespace-thin`). Other actions leave `resolves:`
blank.

Each action MUST also include a `[closes: ...]` annotation: `[closes: {achievement} gap of
{N} {unit} for {topic_path}]` for achievement-targeting actions; `[closes: {milestone} —
{brief summary of remaining preconditions}]` for milestone-targeting actions; `[closes: N/A]`
for actions with no quantifiable numeric gap.

### 3.3 — Tiered Next Actions

Write at least 3 actions, organized in three sections based on the inertia severity tier of
the target topic:

**[CRITICAL]** — Actions targeting `critical` severity topics (2+ flags). List before WARNING
and ADVANCING. If no critical topics: `[CRITICAL]: no topics at critical severity.`

**[WARNING]** — Actions targeting `warning` severity topics (1 flag). List after CRITICAL.
If no warning topics: `[WARNING]: no topics at warning severity.`

**[ADVANCING]** — Actions targeting `healthy` topics (earning new achievements) or team
milestones. List last.

The `prevents:` rule is the second structurally independent enforcement point embedded in
each relevant row.

```
## Next Actions

### [CRITICAL]
1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank] [closes: {gap}]
...

### [WARNING]
N. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank] [closes: {gap}]
...

### [ADVANCING]
N. `{namespace}/{topic}` -> unlocks **{exact name}** [closes: {gap or N/A}]
...
```

After all actions (N = actual `prevents:`-prefixed count across all tiers):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Strategist Gate** — Verify and emit after ACTIONS GATE:

- [ ] Nearest-miss confirmation transcribed
- [ ] Pre-write check complete; zero-score conditions and open flags grouped by severity tier
- [ ] Tiered structure: `[CRITICAL]` first, `[WARNING]` second, `[ADVANCING]` last; empty
  tiers include the "no topics at {tier} severity" line
- [ ] At least 3 actions; each names namespace + topic + exact achievement or milestone;
  `prevents:` applied per 3.2 and 3.3 (two independent enforcement points); `resolves:` with
  exact flag names; `[closes: ...]` on every action row; ACTIONS GATE with actual N

**Strategist Handoff** — Artifacts to Narrator:

1. Nearest-miss assessment (confirmed from Analyst)
2. Tiered Next Actions list (`[CRITICAL]` / `[WARNING]` / `[ADVANCING]`) with all
   `prevents:`, `resolves:`, and `[closes: ...]` annotations
3. Pre-write check results
4. ACTIONS GATE line

---

## ROLE 4: NARRATOR

**Responsibility**: Synthesis only. Produces the Contributor Leaderboard, Collaboration Map,
cross-dimensional reconciliation, and Team Insight. Does NOT re-scan, re-evaluate, re-assess
inertia, or modify the tiered action list.

### 4.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical.
If all `unknown`: `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 4.2 — Collaboration Map

Print: `topic_path | contributors | collaboration_type` for topics where Team Topic is earned.
Types: `pair` (2), `ensemble` (3+). If none: `| none | — | no Team Topic earned yet |`.

### 4.3 — Cross-Dimensional Reconciliation

Select exactly one observation from the Health Phase and one from the Inertia Phase that
interact. State the interaction.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase} | {one finding from Inertia Phase} | {how they connect} |
```

### 4.4 — Team Insight

**Skeptic gate**: The Skeptic has read all output from Roles 1–3 — every achievement table,
every milestone row (including proximity ladders for all NOT YET milestones), every inertia
flag, every severity tier, every trajectory note, the stale signal table, the velocity summary,
the nearest-miss assessment, the tiered action list (with all `prevents:`, `resolves:`, and
`[closes: ...]` annotations), the leaderboard, the collaboration map, and the reconciliation
pairing in 4.3. The insight MUST contain something the Skeptic would not already know.

An insight that restates an achievement count, milestone proximity ladder entry, inertia flag,
tiered action grouping, `[closes: ...]` annotation, or reconciliation row fails. A passing
insight surfaces a second-order pattern requiring synthesis across health and inertia — including
the milestone proximity dimension — in a way no single block or the reconciliation pairing
directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

**Narrator Gate** — Verify and emit:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Collaboration map present (or "none" row)
- [ ] Reconciliation pairing: one Health observation, one Inertia observation, interaction note
- [ ] Team Insight as one sentence; Skeptic gate verified — Skeptic knew every achievement,
  milestone (with proximity ladders), inertia flag, severity tier, trajectory note, stale
  signal, velocity, nearest-miss, tiered actions (with all annotations), leaderboard,
  collaboration, and reconciliation data; insight is new cross-dimensional inference beyond all
  of that including the milestone proximity dimension

---

## V-05 — Full Integration: 5-Role + Inertia-First + All R13 Seeds + Seeds M+N+O+R+S

**Axis**: Full integration
**Hypothesis**: V-05 is the ceiling-holding integration variation for R14. Architecture: the
5-role pipeline (Archivist → Assessor → Inspector → Strategist → Narrator) from R13, with
Assessor running inertia-first and assigning severity tiers before any health data is assessed,
Inspector running health in severity order with milestone proximity ladders (Seed N) and a
cross-role discrepancy check (Seed I) plus a new echo detection check (Seed S), Strategist
producing tiered actions with gap-binding annotations (Seeds K+M), and Narrator producing a
leaderboard with a velocity column (Seed R), reconciliation pairing, and a Team Insight with a
confidence band (Seed O) and projection test (Seed L). All five R14 seeds formalized.

Echo detection (Seed S) is the key new structural element: after completing the Health Phase,
the Inspector runs a consistency scan checking whether any combination of Health Phase
achievement claims and Inertia Phase flag assignments is structurally impossible — not a
data-entry error but a logical contradiction (e.g., `healthy-momentum` requires >= 2
contributors but `Solo Pioneer` requires exactly 1; both cannot be simultaneously true for the
same topic). Echo conditions not caught by the discrepancy check are a different failure mode:
the discrepancy check catches flag/achievement contradictions; echo detection catches flag/flag
or achievement/achievement mutual exclusions.

---

You are running the **Corps Leaderboard** skill in a 5-role inertia-first pipeline. Execute
each role completely before advancing to the next. No role may perform work assigned to another
role. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Pipeline note**: The Assessor (Role 2) establishes severity tiers via the Inertia Phase before
any health data is assessed. The Inspector (Role 3) runs the Health Phase in severity order,
then runs cross-role discrepancy check (Seed I) and echo detection check (Seed S). The
Strategist (Role 4) produces tiered, gap-bound actions. The Narrator (Role 5) produces synthesis
with a leaderboard velocity column, reconciliation pairing, and a confidence-band insight with a
projection test.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Scans workspace, builds signal registry, builds
contributor index. Does NOT evaluate achievements, assess trajectory, rank contributors, write
insights, or write actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path after `simulations/`
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. All subsequent roles do
not run.

Print registry: `topic_path | namespace | contributor | file`

Print namespace coverage:
`Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`

The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

### 1.2 — Contributor Index

Print: `contributor | topic_path | file_count`.

**Archivist Gate** — Verify and emit:

- [ ] Registry table with all four columns
- [ ] Namespace coverage line with active and empty lists
- [ ] Contributor index with all three columns

**Archivist Handoff** — Artifacts to Assessor:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line
3. Contributor index (columns: `contributor`, `topic_path`, `file_count`)

---

## ROLE 2: ASSESSOR

**Responsibility**: Trajectory assessment only. Evaluates inertia flags, severity tiers, stale
signals, velocity trend, and nearest-miss assessment. Does NOT evaluate achievements, milestones,
or current-state counts — those belong to the Inspector.

### 2.1 — Inertia Phase

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Assign severity tier:
- `critical` — 2+ flags (not counting healthy-momentum)
- `warning` — 1 flag (not counting healthy-momentum)
- `healthy` — 0 non-momentum flags

Print inertia table: `topic_path | flags | trajectory note | severity`

Print stale signal table: `topic_path | stale_status` (`stale` / `active` / `date-unknown`).

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

### 2.2 — Nearest-Miss Assessment

- **Level 1** — every topic 1 unit away from any threshold (topic + achievement + gap). Sort
  ascending.
- **Level 2** — closest 2 units away. ONLY when no Level 1. State "Level 1: no topics are 1
  unit away" first.

Print: `topic | achievement | gap | level`

**Assessor Gate** — Verify and emit:

- [ ] Inertia table with severity column; every topic evaluated for all four flags
- [ ] No static file counts, achievement statuses, or coverage totals in Assessor output
- [ ] Stale signal table and velocity summary present
- [ ] Nearest-miss complete (Level 1, or Level 2 with "Level 1 empty" note)

**Assessor Handoff** — Artifacts to Inspector:

1. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`, `severity`)
2. Stale signal table and velocity summary
3. Nearest-miss table (columns: `topic`, `achievement`, `gap`, `level`)

The Inspector begins with these three artifacts plus the Archivist's three. It does not
re-assess trajectory.

---

## ROLE 3: INSPECTOR

**Responsibility**: Current-state assessment only. Evaluates achievements, milestones (with
proximity ladders), and health metrics. Reports topics in the severity order established by the
Assessor. After completing the health assessment, runs two consistency checks: a cross-role
discrepancy check (flag/achievement contradiction) and an echo detection check (flag/flag or
achievement/flag mutual exclusion). Does NOT restate inertia flags or trajectory claims.

### 3.1 — Health Phase (topics in Assessor's severity order)

**Topic ordering**: critical first, then warning, then healthy. Alphabetical within each tier.

For each `topic_path` (in Assessor severity order), print:

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9
```

Evaluate all five achievements. Exact names only. LOCKED rows must include specific unlock
paths.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file |
| Signal Depth | >= 3 files |
| Full Sweep | >= 3 distinct namespaces |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

```
| Achievement   | Status  | Evidence / Unlock Path |
|---------------|---------|------------------------|
```

When Solo Pioneer EARNED and Team Topic NOT YET:
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]`

Evaluate all three team milestones using exact names. Evidence non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

For every NOT YET milestone, print the **Milestone Proximity Ladder** immediately after its row:

- `first team signal` NOT YET:
  `Proximity ladder: 1 signal file in any namespace for any topic closes this milestone`
- `shared coverage` NOT YET:
  `Proximity ladder: {N} qualifying topics (need 2). {Per-topic deficit: list each topic
  below the 2-contributor threshold with how many more contributors it needs.}`
- `debate starter` NOT YET:
  `Proximity ladder: nearest is {topic_path} at {N}/3 contributors — needs {M} more
  distinct contributor signals`

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count`.

### 3.2 — Cross-Role Discrepancy Check

Compare Assessor's inertia flags against Inspector's health findings. A discrepancy exists when
an inertia flag's precondition is directly contradicted by the Inspector's data:

| Discrepancy type | Condition |
|------------------|-----------|
| stuck-at-first vs. Signal Depth EARNED | Assessor raised `stuck-at-first`; Inspector finds Signal Depth EARNED |
| solo-hold vs. Team Topic EARNED | Assessor raised `solo-hold`; Inspector finds Team Topic EARNED |
| namespace-thin vs. Full Sweep EARNED | Assessor raised `namespace-thin`; Inspector finds Full Sweep EARNED |

```
## Cross-Role Discrepancy Table

| topic_path | Assessor flag | Inspector finding | Resolution |
|------------|--------------|-------------------|------------|
```

If no discrepancies: `| none | — | — | no discrepancies detected |`

Resolution rule: Inspector's file count and attribute data is authoritative. Retracted flags
state explicitly: `Assessor flag {flag-name} retracted for {topic_path}; Inspector health
data is authoritative.`

### 3.3 — Echo Detection Check

After the discrepancy check, scan for echo conditions — structural incompatibilities between
Health Phase achievement claims and Inertia Phase flag assignments not caught by the discrepancy
check. The discrepancy check catches flag/achievement direct contradictions; echo detection
catches logical mutual exclusions:

| Echo condition | Detection rule |
|----------------|----------------|
| healthy-momentum raised + Solo Pioneer EARNED | `healthy-momentum` requires >= 2 contributors; Solo Pioneer requires exactly 1 — mutually exclusive; cannot coexist for the same topic |
| First Signal LOCKED + any non-healthy-momentum flag raised | No flag can be meaningfully raised on a topic with 0 files (flag conditions require at least 1 file to evaluate) |
| stuck-at-first raised AND solo-hold raised AND healthy-momentum raised | `healthy-momentum` condition (Signal Depth earned) is incompatible with `stuck-at-first` condition (Signal Depth not earned) — both cannot be simultaneously raised |

```
## Echo Detection Table

| topic_path | Condition A | Condition B | Echo type | Resolution |
|------------|-------------|-------------|-----------|------------|
```

If no echo conditions: `| none | — | — | — | no echo conditions detected |`

Resolution rule: For `healthy-momentum` + `Solo Pioneer` echo: `healthy-momentum` requires
retraction if Solo Pioneer is confirmed EARNED. State: `Assessor flag healthy-momentum
retracted for {topic_path}; incompatible with Inspector Solo Pioneer EARNED finding.`

**Inspector Gate** — Verify and emit:

- [ ] Every topic in severity order has a health header with `Namespace diversity: {N}/9`;
  all five achievement rows; LOCKED rows include unlock paths; no trajectory language
- [ ] All three milestone names verbatim with non-empty evidence; proximity ladders present
  for ALL NOT YET milestones; debate starter proximity and namespace leader table present
- [ ] Cross-role discrepancy check completed and table emitted; retracted flags documented
  with explicit retraction statements
- [ ] Echo detection check completed and table emitted; echo corrections documented with
  explicit retraction statements
- [ ] Inertia Phase table present; no static counts from Health Phase restated in inertia
  content (cross-contamination check)

**Inspector Handoff** — Artifacts to Strategist:

1. Per-topic Health Phase achievement blocks in severity order (with tension markers and unlock
   paths)
2. Team milestone table (3 rows) with proximity ladders for NOT YET milestones
3. Debate starter proximity line and namespace leader table
4. Cross-role discrepancy table (with retracted flag statements)
5. Echo detection table (with echo correction statements)

---

## ROLE 4: STRATEGIST

**Responsibility**: Actions only. Produces a tiered Next Actions list with gap-binding
annotations. Does NOT produce leaderboard, reconciliation pairing, or Team Insight.

### 4.1 — Nearest-Miss Confirmation

Transcribe the nearest-miss table from the Assessor Handoff. Do not recompute.

### 4.2 — Pre-Write Check

Before writing any action:

1. Identify all zero-score conditions: topics with 0 files, empty registry, empty leaderboard.
2. Identify all open inertia flags from the Assessor's inertia table. Flags retracted in the
   discrepancy check or corrected in the echo detection check are closed — do not generate
   `resolves:` actions for retracted or echo-corrected flags.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action eliminating a zero-score condition carries `prevents:`.
Advancement actions do not.

An action resolving an open (non-retracted, non-echo-corrected) inertia flag MUST declare
`resolves: {flag-name}` (exact flag name). Other actions leave `resolves:` blank.

Each action MUST include `[closes: {achievement} gap of {N} {unit} for {topic_path}]` when it
closes a measurable gap. Actions targeting a team milestone state `[closes: {milestone} —
{summary of remaining preconditions from proximity ladder}]`. Actions with no quantifiable
numeric gap write `[closes: N/A]`.

### 4.3 — Tiered Next Actions

Write at least 3 actions, organized in three sections:

**[CRITICAL]** — Actions for `critical` severity topics. If none: `[CRITICAL]: no topics at
critical severity.`

**[WARNING]** — Actions for `warning` severity topics. If none: `[WARNING]: no topics at
warning severity.`

**[ADVANCING]** — Actions for `healthy` topics or team milestones.

The `prevents:` rule is the second structurally independent enforcement point embedded in
each relevant row.

```
## Next Actions

### [CRITICAL]
1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank] [closes: {gap}]
...

### [WARNING]
N. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank] [closes: {gap}]
...

### [ADVANCING]
N. `{namespace}/{topic}` -> unlocks **{exact name}** [closes: {gap or N/A}]
...
```

After all actions (N = actual `prevents:`-prefixed count across all tiers):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Strategist Gate** — Verify and emit after ACTIONS GATE:

- [ ] Nearest-miss confirmation transcribed
- [ ] Pre-write check complete; zero-score conditions and open flags identified; retracted and
  echo-corrected flags excluded from `resolves:` consideration
- [ ] Tiered structure: `[CRITICAL]` / `[WARNING]` / `[ADVANCING]`; empty tiers include the
  "no topics at {tier} severity" line
- [ ] At least 3 actions; each names namespace + topic + exact achievement or milestone;
  `prevents:` applied per 4.2 and 4.3 (two independent enforcement points); `resolves:` with
  exact flag names; `[closes: ...]` on every action; ACTIONS GATE with actual N

**Strategist Handoff** — Artifacts to Narrator:

1. Nearest-miss assessment (confirmed from Assessor)
2. Tiered Next Actions list with all `prevents:`, `resolves:`, and `[closes: ...]` annotations
3. Pre-write check results (with post-retraction, post-correction flag status)
4. ACTIONS GATE line

---

## ROLE 5: NARRATOR

**Responsibility**: Synthesis only. Produces the Contributor Leaderboard (with velocity column),
Collaboration Map, cross-dimensional reconciliation pairing, and Team Insight (with confidence
band and projection test). Does NOT re-scan, re-evaluate achievements, re-assess inertia, or
modify actions.

### 5.1 — Contributor Leaderboard with Velocity Column

Rank contributors descending by total signal count. Ties: alphabetical.
If all `unknown`: `| 1 | no contributor metadata found | — | — | — |`.

**Velocity assignment** — cross-reference each contributor's files against the Assessor's
stale signal table:
- `rising` — contributor has >= 1 `active` file AND total signal count >= 2
- `steady` — contributor has >= 1 `active` file but total signals = 1, OR mixed
  `active`/`date-unknown` with no `stale` files
- `stalled` — all of the contributor's files are `stale` (at least one confirmed `stale`,
  none `active`)
- `unknown` — all files are `date-unknown` (cannot determine direction)

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered | Velocity |
|------|-------------|---------------|----------------|----------|
```

### 5.2 — Collaboration Map

Print: `topic_path | contributors | collaboration_type` for topics where Team Topic is earned.
Types: `pair` (2), `ensemble` (3+). If none: `| none | — | no Team Topic earned yet |`.

### 5.3 — Cross-Dimensional Reconciliation

Select exactly one observation from the Inspector's Health Phase and one from the Assessor's
Inertia Phase that interact. If the discrepancy or echo check retracted or corrected any
Assessor flags, the selected inertia observation must come from a non-retracted, non-corrected
flag or trajectory note. State the interaction.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase} | {one finding from Inertia Phase, non-retracted} | {how they connect} |
```

### 5.4 — Team Insight

**Skeptic gate**: The Skeptic has read all output from Roles 1–4 — every achievement table
(with tension markers), every milestone row (including proximity ladders), every inertia flag,
every severity tier, every trajectory note, the discrepancy table (with retraction statements),
the echo detection table (with correction statements), the stale signal table, the velocity
summary, the nearest-miss assessment, all tiered actions (with `prevents:`, `resolves:`, and
`[closes: ...]` annotations), the leaderboard (including velocity column), the collaboration
map, and the reconciliation pairing in 5.3. The insight MUST contain something the Skeptic
would not already know from all of that material.

An insight that restates an inertia flag (including retracted or echo-corrected ones), a
milestone proximity ladder entry, a tiered action tier grouping, a `[closes: ...]` annotation,
a leaderboard velocity value, or the reconciliation row fails. A passing insight surfaces a
second-order pattern requiring synthesis across health, inertia, discrepancy resolution, echo
correction, milestone proximity, and contributor velocity — in a way no single output block or
the reconciliation pairing directly reveals.

**Projection test** — Before writing the insight sentence, determine and state whether the
second-order pattern applies only to existing topics (anchored scope) or projects forward to
topics the team has not yet started (extrapolated scope). Write the scope declaration as:

`[scope: anchored — pattern applies to current {N} topics only]`

or

`[scope: extrapolated — pattern projects to future topics; assumption: {brief statement of
what must hold for the projection to be valid}]`

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

After the insight sentence, on separate lines, append:
- Scope declaration: `[scope: anchored/extrapolated ...]` as determined above
- Confidence band: `[confidence: HIGH/MEDIUM/LOW] [supporting observations: {N}]`
  - HIGH: 3 or more independent observations from health and inertia data support the insight
  - MEDIUM: 2 independent observations
  - LOW: 1 observation or single-data-point inference

**Narrator Gate** — Verify and emit:

- [ ] Leaderboard with all five columns (Rank, Contributor, Total Signals, Topics Covered,
  Velocity), ranked descending; velocity assigned per stale signal table cross-reference
- [ ] Collaboration map present (or "none" row)
- [ ] Reconciliation pairing: one Health observation, one Inertia observation (non-retracted,
  non-echo-corrected), interaction note
- [ ] Team Insight as one sentence; scope declaration written (anchored or extrapolated, with
  assumption if extrapolated) on next line; confidence band with HIGH/MEDIUM/LOW and actual
  observation count on next line; Skeptic gate verified — Skeptic knew every achievement
  (with proximity ladders), milestone, inertia flag (including retractions and echo
  corrections), severity tier, trajectory note, stale signal, velocity (including leaderboard
  velocity column), nearest-miss, all tiered actions (with all annotations), leaderboard,
  collaboration, and reconciliation data; insight is new cross-dimensional inference beyond all
  of that including the discrepancy, echo, proximity, and velocity dimensions
