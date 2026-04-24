---
skill: quest-variate
skill_target: corps-leaderboard
round: 13
date: 2026-03-17
rubric_version: 11
---

# Variate R13 — corps-leaderboard

5 complete prompt body variations for the `corps-leaderboard` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

**R12 ceiling against v11**: All 5 variations achieve 100.00 (23/23). Universal ceiling. The
v11 rubric is no longer discriminating — all axes explored in R12 and prior round back-fill
produce equivalent scores. The next ceiling-breaking opportunity requires patterns not yet
captured in C-01–C-31.

**R12 seeds entering R13**:
- Seed A (v12-C-32): `resolves: {flag-name}` on inertia-flag-resolving actions — universal
  (5/5 R12 variations). Links the action layer explicitly to the trajectory dimension.
- Seed B (v12-C-33): Pre-synthesis cross-dimensional reconciliation pairing (one Health ×
  one Inertia observation + interaction statement) — 3/5 R12 variations (V-02, V-04, V-05).
- Seed D: Inertia severity tier column (`critical`/`warning`/`healthy`) — 3/5 (V-01, V-04, V-05).
- Seed E: Narrator confidence gate (`high`/`medium`/`low`) on reconciliation pairing — 2/5.
- Seed F: Action dependency chain (`requires: {action-N}`) — 2/5.
- Seed G: Co-contribution network map — 2/5.

**R13 design targets**:
- All 5 variations carry Seeds A+B as formalized requirements (they are the top v12 candidates
  and appeared in 5/5 and 3/5 R12 variations respectively; formalizing both raises the floor
  for the v12 rubric increment).
- V-01: Lifecycle emphasis (inertia-first ordering within Analyst). 3-role pipeline. Seeds A+B
  carried. Introduces Seed H (severity-ordered health topic reporting). Expected: 23/23.
- V-02: Role sequence (5-role: Archivist/Assessor/Inspector/Strategist/Narrator — splits
  Analyst into two dedicated single-phase roles with a cross-role discrepancy check). Seeds
  A+B carried. Introduces Seed I (cross-role inertia/health discrepancy validation table).
  Expected: 23/23.
- V-03: Phrasing register (specification-by-example — each section leads with a filled stub
  showing expected output shape). 3-role pipeline. Seeds A+B carried. Introduces Seed J
  (stub-conformance markers `[CONFORMS: {section}]`). Expected: 23/23.
- V-04: Combination (lifecycle emphasis + role sequence: 4-role inertia-first pipeline with
  severity-tiered action output). Seeds A+B+D+H carried. Introduces Seed K (tiered action
  output: `[CRITICAL]` / `[WARNING]` / `[ADVANCING]` sections). Expected: 23/23.
- V-05: Full integration (5-role + all seeds A+B+D+E+H+I+K formalized + Seed L: insight
  projection test). Expected: 23/23.

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
| Lifecycle emphasis (inertia-first phase order) + Seeds A+B + Seed H | V-01 |
| Role sequence (5-role: Assessor+Inspector split) + Seeds A+B + Seed I | V-02 |
| Phrasing register (spec-by-example stubs) + Seeds A+B + Seed J | V-03 |
| Combination: lifecycle + role sequence (4-role inertia-first) + Seeds A+B+D+H + Seed K | V-04 |
| Full integration: 5-role + inertia-first + Seeds A+B+D+E+H+I+K + Seed L | V-05 |

---

## V-01 — Inertia-First Lifecycle Emphasis + 3-Role Pipeline + Seeds A+B + Seed H

**Axis**: Lifecycle emphasis
**Hypothesis**: All prior R12 variations run the Health Phase before the Inertia Phase within
the Analyst role (or its equivalent). This variation reverses the Analyst sub-phase order:
Inertia Phase runs first, establishing a trajectory picture before any achievement counts are
assessed. The Health Phase then reports topics in descending inertia severity order (critical
topics first, then warning, then healthy) — Seed H. The hypothesis is that front-loading
trajectory analysis changes what the downstream roles treat as urgent synthesis targets, and
that severity-ordered health reporting surfaces critical topics before the model's context
window fills with lower-priority data. Seeds A (`resolves:`) and B (reconciliation pairing)
are formalized as required Publisher outputs, carrying the top two v12-C-32/C-33 candidates
into all R13 variations.

---

You are running the **Corps Leaderboard** skill in a 3-role inertia-first pipeline. Execute
each role completely before advancing to the next. No role may perform work assigned to
another role. Output each Gate checklist and Handoff artifact list verbatim before the next
role begins.

**Lifecycle note**: Inside the Analyst role, the Inertia Phase (trajectory assessment) runs
BEFORE the Health Phase (current-state assessment). Trajectory is established first; the
Health Phase then reports topics in descending inertia severity order — critical topics first,
then warning, then healthy. Within each severity tier, sort alphabetically by `topic_path`.
Alphabetical ordering across all topics (ignoring severity) fails.

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
then reports current state (Health Phase) in inertia-severity order. The sub-phases are
structurally separated — Inertia Phase content must not appear in the Health Phase and vice
versa. The Analyst does NOT rank contributors, write insights, or write actions.

### 2.1 — Inertia Phase (RUNS FIRST)

Reports trajectory and momentum only. Does NOT include file counts, achievement statuses, or
coverage totals — those are current-state data belonging to the Health Phase.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor signal present |
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

Reports current signal state only. Does NOT include trajectory claims, momentum language, or
inertia flag restatements — those are trajectory data belonging to the Inertia Phase.

**Topic ordering**: Report topics in descending severity tier order — `critical` topics first,
then `warning`, then `healthy`. Within each tier, sort alphabetically by `topic_path`. A
flat alphabetical ordering across all topics fails this requirement.

For each `topic_path` (in severity order), print:

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9
```

Evaluate all five achievements using exact names only. For every LOCKED achievement, state
the specific unlock requirement in the evidence cell — a cell containing only `LOCKED` without
an unlock path fails.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file in topic |
| Signal Depth | >= 3 files in topic |
| Full Sweep | signals span >= 3 distinct namespaces within topic |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

```
| Achievement   | Status  | Evidence / Unlock Path              |
|---------------|---------|-------------------------------------|
| First Signal  | ...     | ...                                 |
| Signal Depth  | ...     | ...                                 |
| Full Sweep    | ...     | ...                                 |
| Solo Pioneer  | ...     | ...                                 |
| Team Topic    | ...     | ...                                 |
```

When Solo Pioneer is EARNED and Team Topic is NOT YET: append
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]` after
that topic block.

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

Identify the topic-achievement pair closest to earning:

- **Level 1** — every topic exactly 1 unit away from any achievement threshold. State: topic
  name + achievement name + exact gap. Sort ascending by gap.
- **Level 2** — closest topic 2 units away. Write Level 2 ONLY when no Level 1 topic exists.
  Explicitly state "Level 1: no topics are 1 unit away" before listing Level 2.

Print: `topic | achievement | gap | level`

**Section 2.2 Gate** — Emit before transferring artifacts:

- [ ] Topics are reported in severity order (critical first, then warning, then healthy),
  alphabetical within tier; flat alpha ordering fails
- [ ] Every topic has a health header with severity tier label and `Namespace diversity: {N}/9`
- [ ] Every topic has all five achievement rows; LOCKED rows include specific unlock paths
- [ ] No trajectory language, momentum claims, or inertia flag restatements in Health Phase
- [ ] All three milestone names verbatim with non-empty evidence
- [ ] Debate starter proximity line and namespace leader table present
- [ ] Nearest-miss complete (Level 1, or Level 2 with "Level 1 empty" note), sorted ascending

**Analyst Handoff** — The following artifacts transfer from the Analyst to the Publisher:

1. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`, `severity`)
2. Stale signal table and velocity summary line
3. Per-topic Health Phase achievement blocks, in severity order (one block per `topic_path`)
4. Team milestone table (3 rows: milestone, status, evidence)
5. Debate starter proximity line and namespace leader table
6. Nearest-miss assessment table (columns: `topic`, `achievement`, `gap`, `level`)

The Publisher begins with these six artifacts plus the Archivist's three. It does not
re-evaluate achievements or re-assess inertia.

---

## ROLE 3: PUBLISHER

**Responsibility**: Synthesis, leaderboard, reconciliation, insight, and actions only. Works
from all prior output. Does NOT re-scan the workspace, re-evaluate achievements, or
re-assess inertia.

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

Before writing the Team Insight, select exactly one observation from the Health Phase and
exactly one from the Inertia Phase that interact with or bear on each other. State how
they interact.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase} | {one finding from Inertia Phase} | {how they connect} |
```

### 3.5 — Team Insight

**Skeptic gate**: A Skeptic who has read all Archivist and Analyst output already knows:
every achievement status, every milestone row, every inertia flag, every severity tier, every
trajectory note, the stale signal table, the velocity summary, the nearest-miss assessment,
the leaderboard, the collaboration map, and the reconciliation pairing in 3.4. The insight
MUST contain something the Skeptic would not already know from all of that material.

An insight that restates an achievement count, milestone status, inertia flag, severity tier,
velocity category, or reconciliation row fails. An insight that merely adjusts the framing
of the reconciliation pairing without adding new inference also fails. A passing insight
surfaces a second-order pattern — a risk, convergence, or cross-topic trajectory inference —
requiring synthesis across health and inertia data in a way no single output block or the
reconciliation pairing directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

### 3.6 — Pre-Write Check

Before writing any action:

1. Identify all zero-score conditions: topics with 0 files, empty registry, empty leaderboard.
   Record each explicitly.
2. Identify all open inertia flags from the Analyst's Inertia Phase table, grouped by
   severity tier. Record each flag by topic and severity.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action whose primary purpose is eliminating a state where the output
would score zero carries the `prevents:` prefix. Advancement actions do not.

An action whose primary purpose is resolving an inertia flag MUST declare
`resolves: {flag-name}` in the action row, where `{flag-name}` is the exact flag name
(`stuck-at-first`, `solo-hold`, or `namespace-thin`). Actions that do not resolve a specific
inertia flag leave `resolves:` blank.

### 3.7 — Next Actions

Write at least 3 actions. Each must name: (1) a specific namespace and topic path,
(2) the exact achievement or milestone it unlocks (exact names only; paraphrasing fails).
The `prevents:` rule is embedded inside each relevant action row below as the second
structurally independent enforcement point.

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
- [ ] Reconciliation pairing written: one Health observation, one Inertia observation,
  interaction note
- [ ] Team Insight written as one sentence; Skeptic gate verified — Skeptic knew every
  achievement, milestone, inertia flag, severity tier, trajectory note, stale signal, velocity,
  nearest-miss, leaderboard, collaboration, and reconciliation data; insight is a new
  cross-dimensional inference not derivable from any single block or the reconciliation pairing
- [ ] Pre-write check complete; zero-score conditions and open inertia flags identified before
  any action written; inertia flags grouped by severity tier in the pre-write log
- [ ] At least 3 actions; each names namespace + topic + exact achievement or milestone;
  `prevents:` applied per 3.6 and 3.7 (two independent enforcement points);
  `resolves:` applied to all inertia-flag-resolving actions with exact flag names; blank otherwise
- [ ] ACTIONS GATE line written with actual N count substituted

---

## V-02 — 5-Role Pipeline: Archivist/Assessor/Inspector/Strategist/Narrator + Seeds A+B + Seed I

**Axis**: Role sequence
**Hypothesis**: All R12 variations use a 3- or 4-role pipeline where a single Analyst role
runs both the Health Phase and Inertia Phase sequentially. This variation splits that role
into two single-phase roles: an Assessor (trajectory only — the Inertia Phase) and an
Inspector (current state only — the Health Phase). The Assessor runs first, the Inspector
runs second using the Assessor's output. This creates 4 handoffs (vs. 2–3 in R12), each with
a named artifact set — strengthening C-28 coverage. The key new pattern is Seed I: before
the Inspector's Gate, a cross-role discrepancy validation table checks whether any inertia
flag raised by the Assessor is contradicted by the Inspector's health data (e.g., Assessor
raises `stuck-at-first` for a topic the Inspector finds has 3 files — a discrepancy that
must be flagged and resolved before the Inspector's Gate passes). Seeds A and B are carried
as formalized Strategist and Narrator requirements.

---

You are running the **Corps Leaderboard** skill in a 5-role pipeline. Execute each role
completely before advancing to the next. No role may perform work assigned to another role.
Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. The Archivist scans the workspace, builds the signal
registry, and constructs the contributor index. The Archivist does NOT evaluate achievements,
assess trajectory, rank contributors, or write insights or actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path segment after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > frontmatter `contributor:` > filename prefix
  before first `-` > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. All subsequent roles
do not run.

Print registry as table: `topic_path | namespace | contributor | file`

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

The Assessor begins with these three artifacts. It does not re-scan the workspace.

---

## ROLE 2: ASSESSOR

**Responsibility**: Trajectory assessment only. The Assessor evaluates all inertia flags,
severity tiers, stale signals, and velocity trend. The Assessor does NOT evaluate
achievements, milestones, or current-state counts — those belong to the Inspector.

### 2.1 — Inertia Phase

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Print inertia table: `topic_path | flags | trajectory note`

A topic with no flags gets `flags = none` and a brief healthy momentum note.

Print stale signal table: `topic_path | stale_status` (`stale`, `active`, `date-unknown`).

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | Trend: {increasing/flat/stalled}`

(> 50% topics with `healthy-momentum` flag = increasing; < 25% = stalled; otherwise flat.)

### 2.2 — Nearest-Miss Assessment

- **Level 1**: every topic exactly 1 unit away from any achievement threshold. State: topic
  name + achievement name + exact gap. Sort ascending.
- **Level 2**: closest topic 2 units away. Write Level 2 ONLY when no Level 1 exists. State
  "Level 1: no topics are 1 unit away" first.

Print: `topic | achievement | gap | level`

**Assessor Gate** — Verify and emit:

- [ ] Inertia table present; every topic evaluated for all four flags; no file counts or
  achievement statuses in Assessor output (prohibited — current-state data)
- [ ] Stale signal table and velocity summary present
- [ ] Nearest-miss table complete (Level 1, or Level 2 with "Level 1 empty" prefix)

**Assessor Handoff** — Artifacts to Inspector:

1. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`)
2. Stale signal table and velocity summary
3. Nearest-miss table (columns: `topic`, `achievement`, `gap`, `level`)

The Inspector begins with these three artifacts plus the Archivist's three. It does not
re-assess trajectory.

---

## ROLE 3: INSPECTOR

**Responsibility**: Current-state assessment only. The Inspector evaluates achievements,
milestones, and health metrics. The Inspector does NOT restate inertia flags or trajectory
claims from the Assessor. After completing the health assessment, the Inspector runs a
cross-role discrepancy check against the Assessor's output.

### 3.1 — Health Phase

For each `topic_path`, print:

```
### topic: {topic_path}
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9
```

Evaluate all five achievements using exact names only. For every LOCKED achievement, state
the specific unlock requirement in the evidence cell — a cell containing only `LOCKED`
without an unlock path fails.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file in topic |
| Signal Depth | >= 3 files in topic |
| Full Sweep | signals span >= 3 distinct namespaces within topic |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

```
| Achievement   | Status  | Evidence / Unlock Path              |
|---------------|---------|-------------------------------------|
| First Signal  | ...     | ...                                 |
| Signal Depth  | ...     | ...                                 |
| Full Sweep    | ...     | ...                                 |
| Solo Pioneer  | ...     | ...                                 |
| Team Topic    | ...     | ...                                 |
```

When Solo Pioneer is EARNED and Team Topic is NOT YET: append
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]`.

Evaluate all three team milestones using exact names. Evidence must be non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file exists in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count` for each active namespace.

### 3.2 — Cross-Role Discrepancy Check

Before emitting the Inspector Gate, compare the Assessor's inertia flags against the
Inspector's health findings. A discrepancy exists when an inertia flag's precondition is
directly contradicted by the Inspector's data.

| Discrepancy type | Condition |
|------------------|-----------|
| stuck-at-first vs. Signal Depth EARNED | Assessor raised `stuck-at-first`; Inspector finds Signal Depth is EARNED |
| solo-hold vs. Team Topic EARNED | Assessor raised `solo-hold`; Inspector finds Team Topic is EARNED |
| namespace-thin vs. Full Sweep EARNED | Assessor raised `namespace-thin`; Inspector finds Full Sweep is EARNED |

If any discrepancy exists, emit a discrepancy row:

```
## Cross-Role Discrepancy Table

| topic_path | Assessor flag | Inspector finding | Resolution |
|------------|--------------|-------------------|------------|
| {topic}    | {flag}       | {contradicting health finding} | {which data is authoritative; why} |
```

Resolution rule: the Inspector's direct file count and attribute data is authoritative.
If `Signal Depth` is EARNED in the Health Phase, `stuck-at-first` is retracted for that
topic. State explicitly: `Assessor flag {flag-name} retracted for {topic_path}; Inspector
health data is authoritative.`

If no discrepancies exist: write one row `| none | — | — | no discrepancies detected |`.

**Inspector Gate** — Verify and emit:

- [ ] Every topic has a health header with `Namespace diversity: {N}/9` and all five
  achievement rows; LOCKED rows include specific unlock paths
- [ ] No trajectory language or inertia flag restatements in any Health Phase content
- [ ] All three milestone names verbatim with non-empty evidence; debate starter proximity
  and namespace leader table present
- [ ] Cross-role discrepancy check completed and table emitted (either discrepancy rows or
  "none" row)
- [ ] Any retracted Assessor flags explicitly documented with resolution statement

**Inspector Handoff** — Artifacts to Strategist:

1. Per-topic Health Phase achievement blocks (with tension markers and unlock paths)
2. Team milestone table (3 rows: milestone, status, evidence)
3. Debate starter proximity line and namespace leader table
4. Cross-role discrepancy table (with any retracted flag statements)

The Strategist begins with all five Archivist+Assessor+Inspector artifacts. It does not
re-evaluate achievements or re-assess trajectory.

---

## ROLE 4: STRATEGIST

**Responsibility**: Actions only. The Strategist produces the Next Actions list. The
Strategist does NOT produce the leaderboard, reconciliation pairing, or Team Insight —
those belong to the Narrator.

### 4.1 — Nearest-Miss Confirmation

Transcribe the nearest-miss table from the Assessor Handoff. Do not recompute.

### 4.2 — Pre-Write Check

Before writing any action:
1. Identify all zero-score conditions: topics with 0 files, empty registry, empty leaderboard.
2. Identify all open inertia flags from the Assessor's inertia table. If any flag was
   retracted in the discrepancy check, use the Inspector's resolution (retracted flags are
   closed; do not generate `resolves:` actions for retracted flags).

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action eliminating a zero-score condition carries the `prevents:`
prefix. Advancement actions do not.

An action whose primary purpose is resolving an open (non-retracted) inertia flag MUST
declare `resolves: {flag-name}` where `{flag-name}` is the exact inertia flag name.

### 4.3 — Next Actions

Write at least 3 actions. Each must name: (1) a specific namespace and topic path,
(2) the exact achievement or milestone it unlocks. The `prevents:` rule is embedded inside
each relevant action row below as the second structurally independent enforcement point.

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
- [ ] Pre-write check complete; zero-score conditions and open flags identified; retracted
  flags excluded from `resolves:` consideration
- [ ] At least 3 actions with namespace + topic + exact achievement; `prevents:` applied per
  4.2 and 4.3 (two independent enforcement points); `resolves:` applied with exact flag names
- [ ] ACTIONS GATE line written with actual N substituted

**Strategist Handoff** — Artifacts to Narrator:

1. Nearest-miss assessment (confirmed from Assessor)
2. Next Actions list (all rows with `prevents:` and `resolves:` annotations as written)
3. Pre-write check results (zero-score conditions and open flags)
4. ACTIONS GATE line

The Narrator begins with all output from Roles 1–4. It does not re-assess actions or inertia.

---

## ROLE 5: NARRATOR

**Responsibility**: Synthesis only. The Narrator produces the Contributor Leaderboard,
Collaboration Map, cross-dimensional reconciliation pairing, and Team Insight. The Narrator
does NOT re-scan the workspace, re-evaluate achievements, re-assess inertia, or modify actions.

### 5.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical. If all `unknown`:
`| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 5.2 — Collaboration Map

Print: `topic_path | contributors | collaboration_type` for topics where Team Topic is earned.
Types: `pair` (2), `ensemble` (3+). If none: `| none | — | no Team Topic earned yet |`.

### 5.3 — Cross-Dimensional Reconciliation

Before writing the Team Insight, select exactly one observation from the Inspector's Health
Phase and exactly one from the Assessor's Inertia Phase that interact. State how they
interact. If the discrepancy check retracted any Assessor flags, the selected Inertia
observation must be from a non-retracted flag or a trajectory note.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase} | {one finding from Inertia Phase} | {how they connect} |
```

### 5.4 — Team Insight

**Skeptic gate**: The Skeptic has read all output from the Archivist, Assessor, Inspector,
and Strategist — every achievement table, every milestone row, every inertia flag, every
trajectory note, the discrepancy table with retracted flags, the stale signal table, the
velocity summary, the nearest-miss assessment, all actions with `prevents:` and `resolves:`
annotations, the leaderboard, the collaboration map, and the reconciliation pairing in 5.3.
The insight MUST contain something the Skeptic would not already know.

An insight that restates an inertia flag (including retracted ones), milestone status,
reconciliation row, or discrepancy resolution fails. A passing insight surfaces a second-order
pattern requiring synthesis across health and inertia data — including the discrepancy
resolution layer — in a way no single block or the reconciliation pairing directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

**Narrator Gate** — Verify and emit:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Collaboration map present (or "none" row)
- [ ] Reconciliation pairing written with one Health observation, one Inertia observation
  (non-retracted), and interaction note
- [ ] Team Insight written as one sentence; Skeptic gate verified — Skeptic knew all
  achievement, milestone, inertia flag, trajectory, discrepancy, stale, velocity, action
  (with all annotations), leaderboard, collaboration, and reconciliation data; insight is
  a new cross-dimensional inference beyond all of that including the discrepancy layer

---

## V-03 — Specification-by-Example Phrasing Register + 3-Role Pipeline + Seeds A+B + Seed J

**Axis**: Phrasing register
**Hypothesis**: All prior variations use imperative prose (MUST/SHALL/does NOT) or numbered
RFC requirements. This variation shifts to a specification-by-example register: each
instruction step leads with a filled-in stub showing what correct output looks like, followed
by the fill-in directive. The hypothesis is that example-first phrasing reduces format
ambiguity at the cost of longer prompts, and that the model is more likely to produce
correctly-typed output when it can pattern-match against a concrete stub rather than infer
format from a prose description. Seed J is new: after completing each stub-driven section,
the model emits `[CONFORMS: {section-name}]` to assert that its output matches the stub
pattern. This creates a structural checkpoint that is distinct from the `[ ]` gate checklists
(which confirm content), testing whether per-section conformance markers add a second layer
of format discipline beyond gate-level review. Seeds A and B formalized.

---

You are running the **Corps Leaderboard** skill in a 3-role pipeline. Execute each role
completely before advancing to the next. No role may perform work assigned to another role.

This specification uses an example-first format: each section shows a filled-in stub
representing correct output, followed by a directive to fill in actual values. Replace stub
values with real data — do not emit stub rows in your output. After completing each
stub-driven section, emit `[CONFORMS: {section-name}]` to confirm your output matches the
stub's structural pattern. Output each Gate checklist and Handoff artifact list verbatim
before the next role begins.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. The Archivist scans the workspace, builds the
signal registry, and constructs the contributor index. The Archivist does NOT evaluate
achievements, assess trajectory, rank contributors, or write insights or actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path` (e.g., `scout`)
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. Roles 2 and 3 do not run.

**Expected output stub (replace with real rows):**

```
## Signal Registry

| topic_path         | namespace | contributor | file                                                    |
|--------------------|-----------|-------------|---------------------------------------------------------|
| scout/competitors  | scout     | alice       | simulations/scout/competitors/alice-scout-2026-03-10.md |
| flow/trigger       | flow      | bob         | simulations/flow/trigger/bob-flow-2026-03-12.md         |
```

Fill in actual rows in place of the stub. Then emit: `[CONFORMS: signal-registry]`

After the registry, print namespace coverage using this pattern:
`Namespaces active: 2 of 9 | Active: scout, flow | Empty: draft, review, trace, prove, listen, program, topic`
(fill in actual values)

The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

### 1.2 — Contributor Index

**Expected output stub (replace with real rows):**

```
## Contributor Index

| contributor | topic_path        | file_count |
|-------------|-------------------|------------|
| alice       | scout/competitors | 2          |
| bob         | flow/trigger      | 1          |
```

Fill in actual rows. Then emit: `[CONFORMS: contributor-index]`

**Archivist Gate** — Verify and emit before transferring artifacts:

- [ ] Signal registry printed and conforms to stub pattern; `[CONFORMS: signal-registry]`
  emitted
- [ ] Namespace coverage line present with active and empty namespace lists
- [ ] Contributor index printed and conforms to stub pattern; `[CONFORMS: contributor-index]`
  emitted

**Archivist Handoff** — The following artifacts transfer from the Archivist to the Analyst:

1. Signal registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line (active and empty namespace lists)
3. Contributor index table (columns: `contributor`, `topic_path`, `file_count`)

The Analyst begins with these three artifacts. It does not re-scan the workspace.

---

## ROLE 2: ANALYST

**Responsibility**: Evaluation only. The Analyst assesses registry data and reports current
state (Health Phase) then trajectory (Inertia Phase). These sub-phases are structurally
separated — Health Phase content must not appear in the Inertia Phase and vice versa. The
Analyst does NOT rank contributors, write insights, or write actions.

### 2.1 — Health Phase

Reports current signal state only: file counts, namespace coverage, achievement status per
topic. Does NOT report trajectory, momentum, or stall indicators.

**Expected topic block stub (repeat for each topic; replace with real values):**

```
### topic: scout/competitors
Health — Files: 2 | Namespaces: scout | Contributors: alice | Namespace diversity: 1/9

| Achievement   | Status   | Evidence / Unlock Path                          |
|---------------|----------|-------------------------------------------------|
| First Signal  | EARNED   | 2 files present                                 |
| Signal Depth  | LOCKED   | need 1 more file (currently 2/3)                |
| Full Sweep    | LOCKED   | need signals in 2 more namespaces (currently 1/3) |
| Solo Pioneer  | EARNED   | exactly 1 contributor: alice                    |
| Team Topic    | LOCKED   | need 1 more contributor with >= 1 signal        |
```

For every `topic_path` in the Archivist's registry, print a topic block following this
pattern. Achievement names must be exact — paraphrasing fails. LOCKED rows must include
specific unlock paths. Then emit: `[CONFORMS: health-phase]`

When Solo Pioneer is EARNED and Team Topic is NOT YET: append
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]`.

Evaluate all three team milestones. Use exact names. Evidence must be non-empty.

**Expected milestone table stub:**

```
| milestone         | status   | evidence                                     |
|-------------------|----------|----------------------------------------------|
| first team signal | EARNED   | simulations/scout/competitors/alice-scout-2026-03-10.md |
| shared coverage   | NOT YET  | need 1 more topic with 2+ distinct contributors (currently 0/2) |
| debate starter    | NOT YET  | need 1 topic with 3 distinct contributors (currently 0/3) |
```

Fill in actual values. Then emit: `[CONFORMS: milestones]`

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table:

**Expected stub:**

```
| namespace | leader | signal_count |
|-----------|--------|--------------|
| scout     | alice  | 2            |
| flow      | bob    | 1            |
```

Fill in actual values. Then emit: `[CONFORMS: namespace-leaders]`

### 2.2 — Inertia Phase

Reports trajectory and momentum only. Does NOT restate file counts, achievement statuses, or
coverage totals from the Health Phase.

**Expected inertia table stub:**

```
| topic_path        | flags                    | trajectory note                                   |
|-------------------|--------------------------|---------------------------------------------------|
| scout/competitors | stuck-at-first, solo-hold | stalled at 2 files; no second contributor in view |
| flow/trigger      | namespace-thin           | all 1 file in flow namespace; diversity not growing |
```

For every `topic_path`, evaluate all four inertia flags. A topic with no flags gets
`flags = none` and a brief healthy momentum note. Fill in actual values.
Then emit: `[CONFORMS: inertia-phase]`

Print stale signal table:

**Expected stub:**

```
| topic_path        | stale_status |
|-------------------|--------------|
| scout/competitors | active       |
| flow/trigger      | date-unknown |
```

Fill in actual values. Then emit: `[CONFORMS: stale-signals]`

Print velocity summary (fill in actual values):
`Signal velocity: {N_signals} / {N_topics} topics | Trend: {increasing/flat/stalled}`

### 2.3 — Nearest-Miss Assessment

- **Level 1**: every topic 1 unit away from any threshold (topic + achievement + exact gap).
  Sort ascending.
- **Level 2**: closest topic 2 units away. Only when no Level 1 exists. State "Level 1: no
  topics are 1 unit away" first.

**Expected stub:**

```
| topic             | achievement  | gap | level   |
|-------------------|--------------|-----|---------|
| scout/competitors | Signal Depth | 1   | Level 1 |
```

Fill in actual values. Then emit: `[CONFORMS: nearest-miss]`

**Analyst Gate** — Verify and emit before transferring artifacts:

- [ ] Every topic has a health block conforming to stub pattern; LOCKED rows include unlock
  paths; `[CONFORMS: health-phase]` emitted
- [ ] Milestone table conforms to stub pattern with exact names and non-empty evidence;
  `[CONFORMS: milestones]` emitted; debate starter proximity and namespace leader table present
- [ ] Inertia table conforms to stub pattern; no static counts from Health Phase restated;
  `[CONFORMS: inertia-phase]` emitted
- [ ] Stale signal table and velocity summary present; `[CONFORMS: stale-signals]` emitted
- [ ] Nearest-miss table complete (Level 1, or Level 2 with "Level 1 empty" note);
  `[CONFORMS: nearest-miss]` emitted

**Analyst Handoff** — The following artifacts transfer from the Analyst to the Publisher:

1. Per-topic Health Phase blocks (with tension markers and unlock paths)
2. Team milestone table (3 rows)
3. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`)
4. Stale signal table and velocity summary
5. Nearest-miss table (columns: `topic`, `achievement`, `gap`, `level`)

The Publisher begins with these five artifacts plus the Archivist's three. It does not
re-evaluate achievements or re-assess inertia.

---

## ROLE 3: PUBLISHER

**Responsibility**: Synthesis, leaderboard, reconciliation, insight, and actions only.
Works from all prior output. Does NOT re-scan, re-evaluate achievements, or re-assess inertia.

### 3.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical. If all `unknown`:
`| 1 | no contributor metadata found | — | — |`.

**Expected stub:**

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered     |
|------|-------------|---------------|--------------------|
| 1    | alice       | 2             | scout/competitors  |
| 2    | bob         | 1             | flow/trigger       |
```

Fill in actual values. Then emit: `[CONFORMS: leaderboard]`

### 3.2 — Collaboration Map

**Expected stub:**

```
| topic_path         | contributors   | collaboration_type |
|--------------------|----------------|--------------------|
| flow/trigger       | alice, bob     | pair               |
```

If no topic earned Team Topic: `| none | — | no Team Topic earned yet |`.
Fill in actual values. Then emit: `[CONFORMS: collaboration-map]`

### 3.3 — Nearest-Miss Confirmation

Transcribe the nearest-miss table from the Analyst Handoff. Do not recompute.

### 3.4 — Cross-Dimensional Reconciliation

Before writing the Team Insight, select one Health observation and one Inertia observation
that interact. State the interaction.

**Expected stub:**

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| solo/competitors: Solo Pioneer EARNED — only alice has contributed | solo-hold flag active for scout/competitors | Solo Pioneer achievement and solo-hold flag are the same structural condition seen from two angles; unlocking Team Topic resolves both simultaneously |
```

Fill in one row with actual observations and their interaction.
Then emit: `[CONFORMS: reconciliation]`

### 3.5 — Team Insight

**Skeptic gate**: A Skeptic who has completed all prior roles and read all output — every
achievement table, every milestone row, every inertia flag, every trajectory note, the
stale signal table, the velocity summary, the nearest-miss assessment, the leaderboard, the
collaboration map, and the reconciliation pairing in 3.4 — already knows all of that material.
The insight MUST contain something this Skeptic would not already know.

An insight that restates an achievement count, milestone status, inertia flag, velocity
category, or reconciliation interaction fails. A passing insight surfaces a second-order
pattern — a risk, convergence, or trajectory inference — that requires synthesizing across
health and inertia data in a way no single stub-conforming block or the reconciliation pairing
directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

### 3.6 — Pre-Write Check

Before writing any action:
1. Identify all zero-score conditions: topics with 0 files, empty registry, empty leaderboard.
2. Identify all open inertia flags from the Analyst's Inertia Phase table.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action eliminating a zero-score condition carries `prevents:`. Others
do not.

An action resolving an inertia flag MUST declare `resolves: {flag-name}` (exact flag name).
Other actions leave `resolves:` blank.

### 3.7 — Next Actions

Write at least 3 actions. Each must name: (1) namespace + topic path, (2) exact achievement
or milestone name. The `prevents:` rule is embedded inside each relevant action row as the
second structurally independent enforcement point.

**Expected stub:**

```
## Next Actions

1. prevents: `scout/competitors` -> unlocks **Signal Depth** [resolves: stuck-at-first]
2. `flow/trigger` -> unlocks **Full Sweep** [resolves: namespace-thin]
3. `flow/trigger` -> unlocks **Team Topic** [resolves: solo-hold]
```

Fill in actual actions. Then emit: `[CONFORMS: next-actions]`

After all actions:

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Publisher Gate** — Verify and emit after the ACTIONS GATE line:

- [ ] Leaderboard conforms to stub; ranked descending; `[CONFORMS: leaderboard]` emitted
- [ ] Collaboration map conforms to stub (or "none" row); `[CONFORMS: collaboration-map]`
  emitted
- [ ] Nearest-miss confirmation transcribed from Analyst Handoff
- [ ] Reconciliation pairing conforms to stub with one Health observation, one Inertia
  observation, and interaction note; `[CONFORMS: reconciliation]` emitted
- [ ] Team Insight written as one sentence; Skeptic gate verified — Skeptic knew every
  achievement, milestone, inertia flag, trajectory note, stale signal, velocity, nearest-miss,
  leaderboard, collaboration, and reconciliation data; insight is new cross-dimensional inference
- [ ] Pre-write check complete; zero-score conditions and open inertia flags identified
- [ ] At least 3 actions conforming to stub; `prevents:` applied per 3.6 and 3.7 (two
  independent enforcement points); `resolves:` applied with exact flag names; blank otherwise;
  `[CONFORMS: next-actions]` emitted
- [ ] ACTIONS GATE line written with actual N substituted

---

## V-04 — Combination: 4-Role Inertia-First + Severity-Tiered Action Output + Seeds A+B+D+H + Seed K

**Axis**: Lifecycle emphasis + role sequence + inertia framing
**Hypothesis**: V-01 tests inertia-first lifecycle in a 3-role pipeline with severity-ordered
health reporting (Seed H). V-04 combines that with the 4-role Archivist/Analyst/Strategist/
Narrator architecture from R12, adds the severity tier column to the inertia table (Seed D,
already proven in R12 V-01), and introduces Seed K: the Next Actions list is structured in
three tiered sections — `[CRITICAL]` (actions targeting topics with `critical` severity),
`[WARNING]` (targeting `warning` severity), and `[ADVANCING]` (targeting `healthy` topics
or earning new achievements). This tests whether tiered action output changes how the Narrator
synthesizes: a team that can see which actions address structural emergencies vs. which are
advancement investments has a different cognitive picture than a flat numbered list. Seeds A
and B are formalized in the Strategist and Narrator respectively.

---

You are running the **Corps Leaderboard** skill in a 4-role inertia-first pipeline. Execute
each role completely before advancing to the next. No role may perform work assigned to
another role. Output each Gate checklist and Handoff artifact list verbatim before the next
role begins.

**Lifecycle note**: Within the Analyst role, the Inertia Phase runs BEFORE the Health Phase.
The Health Phase then reports topics in severity-tier order (critical → warning → healthy).
Trajectory drives the order of current-state reporting.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. The Archivist scans the workspace, builds the
signal registry, and constructs the contributor index. The Archivist does NOT evaluate
achievements, assess trajectory, rank contributors, or write insights or actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path after `simulations/`
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. All subsequent roles
do not run.

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

**Responsibility**: Evaluation only. The Analyst runs the Inertia Phase first (establishes
severity tiers), then the Health Phase (reports topics in severity order). Sub-phases are
structurally separated. The Analyst does NOT rank contributors, write insights, or write
actions.

### 2.1 — Inertia Phase (RUNS FIRST)

Reports trajectory and momentum only. Does NOT include file counts, achievement statuses, or
coverage totals — those are current-state data for the Health Phase.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Assign a severity tier:
- `critical` — 2 or more flags raised (not counting healthy-momentum)
- `warning` — exactly 1 flag raised (not counting healthy-momentum)
- `healthy` — 0 non-momentum flags, or only healthy-momentum

Print inertia table: `topic_path | flags | trajectory note | severity`

Print stale signal table: `topic_path | stale_status` (`stale`, `active`, `date-unknown`).

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

**Section 2.1 Gate** — Emit before proceeding to Section 2.2:

- [ ] Inertia table with severity column; every topic evaluated; no file counts or achievement
  statuses (prohibited — current-state data)
- [ ] Stale signal table and velocity summary present

### 2.2 — Health Phase (RUNS SECOND — ordered by severity tier)

Reports current signal state only. Does NOT include trajectory claims, momentum language, or
inertia flag restatements.

**Topic ordering**: `critical` topics first, then `warning`, then `healthy`. Alphabetical
within each tier. Flat alphabetical ordering across tiers fails.

For each `topic_path` (in severity order), print:

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
| Full Sweep | >= 3 distinct namespaces within topic |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

```
| Achievement   | Status  | Evidence / Unlock Path              |
|---------------|---------|-------------------------------------|
```

When Solo Pioneer EARNED and Team Topic NOT YET: append
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]`.

Evaluate all three team milestones. Exact names. Evidence non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count`.

### 2.3 — Nearest-Miss Assessment

- **Level 1**: every topic 1 unit away (topic + achievement + exact gap). Sort ascending.
- **Level 2**: closest topic 2 units away. Only when no Level 1. State "Level 1: no topics
  are 1 unit away" first.

Print: `topic | achievement | gap | level`

**Section 2.2 Gate** — Emit before transferring artifacts:

- [ ] Topics reported in severity order (critical → warning → healthy); each health header
  includes severity tier label and `Namespace diversity: {N}/9`
- [ ] All five achievement rows per topic; LOCKED rows include unlock paths; no trajectory
  language in Health Phase
- [ ] All three milestone names verbatim with non-empty evidence; debate starter proximity
  and namespace leader table present
- [ ] Nearest-miss complete (Level 1, or Level 2 with "Level 1 empty" note)

**Analyst Handoff** — Artifacts to Strategist:

1. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`, `severity`)
2. Stale signal table and velocity summary
3. Per-topic Health Phase achievement blocks, in severity order (one block per `topic_path`)
4. Team milestone table (3 rows)
5. Nearest-miss table (columns: `topic`, `achievement`, `gap`, `level`)

The Strategist begins with these five artifacts plus the Archivist's three. It does not
re-evaluate achievements or re-assess inertia.

---

## ROLE 3: STRATEGIST

**Responsibility**: Actions only. The Strategist produces a tiered Next Actions list grouped
by inertia severity. The Strategist does NOT produce the leaderboard, reconciliation pairing,
or Team Insight.

### 3.1 — Nearest-Miss Confirmation

Transcribe the nearest-miss table from the Analyst Handoff. Do not recompute.

### 3.2 — Pre-Write Check

Before writing any action:
1. Identify all zero-score conditions: topics with 0 files, empty registry, empty leaderboard.
2. Identify all open inertia flags from the Analyst's Inertia Phase table, grouped by severity
   tier.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action eliminating a zero-score condition carries `prevents:`.
Advancement actions do not.

An action resolving an open inertia flag MUST declare `resolves: {flag-name}` (exact flag
name: `stuck-at-first`, `solo-hold`, or `namespace-thin`).

### 3.3 — Tiered Next Actions

Write at least 3 actions total. Actions are organized in three sections based on the inertia
severity tier of the target topic:

**[CRITICAL]** — Actions targeting topics with `critical` severity (2+ flags). List all
`[CRITICAL]` actions before any `[WARNING]` or `[ADVANCING]` actions. If no `critical`
topics exist, write `[CRITICAL]: no topics at critical severity.`

**[WARNING]** — Actions targeting topics with `warning` severity (1 flag). List after all
`[CRITICAL]` actions. If no `warning` topics exist, write `[WARNING]: no topics at warning
severity.`

**[ADVANCING]** — Actions targeting `healthy` topics (earning new achievements) or team
milestones. List last.

Within each section, the `prevents:` rule is embedded inside each relevant action row as the
second structurally independent enforcement point.

```
## Next Actions

### [CRITICAL]
1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank]
...

### [WARNING]
N. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank]
...

### [ADVANCING]
N. `{namespace}/{topic}` -> unlocks **{exact name}**
...
```

After all actions, output exactly this line (N = actual count of `prevents:`-prefixed actions
across all tiers):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Strategist Gate** — Verify and emit after the ACTIONS GATE line:

- [ ] Nearest-miss confirmation present
- [ ] Pre-write check complete; zero-score conditions and open flags identified; flags grouped
  by severity tier
- [ ] Tiered action structure present: `[CRITICAL]` section first, then `[WARNING]`, then
  `[ADVANCING]`; sections without qualifying topics include the "no topics at {tier} severity"
  line
- [ ] At least 3 actions total; each names namespace + topic + exact achievement or milestone;
  `prevents:` applied per 3.2 and 3.3 (two independent enforcement points);
  `resolves:` applied with exact flag names; blank otherwise
- [ ] ACTIONS GATE line written with actual N across all tiers substituted

**Strategist Handoff** — Artifacts to Narrator:

1. Nearest-miss assessment (confirmed)
2. Tiered Next Actions list (`[CRITICAL]` / `[WARNING]` / `[ADVANCING]` sections)
3. Pre-write check results (zero-score conditions and open inertia flags by tier)
4. ACTIONS GATE line

---

## ROLE 4: NARRATOR

**Responsibility**: Synthesis only. The Narrator produces the Contributor Leaderboard,
Collaboration Map, cross-dimensional reconciliation pairing, and Team Insight. Does NOT
re-scan, re-evaluate achievements, re-assess inertia, or modify the tiered action list.

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

Before writing the Team Insight, select exactly one observation from the Health Phase and
exactly one from the Inertia Phase that interact. State how they interact.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase} | {one finding from Inertia Phase} | {how they connect} |
```

### 4.4 — Team Insight

**Skeptic gate**: The Skeptic has read all Archivist, Analyst, and Strategist output —
every achievement table, every milestone row, every inertia flag, every severity tier, every
trajectory note, the stale signal table, the velocity summary, the nearest-miss assessment,
the tiered action list (with all `prevents:` and `resolves:` annotations), the leaderboard,
the collaboration map, and the reconciliation pairing in 4.3. The insight MUST contain
something the Skeptic would not already know.

An insight that restates an achievement count, severity tier, velocity category, tiered
action grouping, or reconciliation row fails. A passing insight surfaces a second-order
pattern — a risk, convergence, or trajectory inference — requiring synthesis across health
and inertia that neither the tiered action list nor the reconciliation pairing directly
reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

**Narrator Gate** — Verify and emit:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Collaboration map present (or "none" row)
- [ ] Reconciliation pairing written with one Health observation, one Inertia observation,
  and interaction note
- [ ] Team Insight written as one sentence; Skeptic gate verified — Skeptic knew every
  achievement, milestone, inertia flag, severity tier, trajectory note, stale signal, velocity,
  tiered action list (with annotations), leaderboard, collaboration, and reconciliation data;
  insight is new cross-dimensional inference beyond all of that

---

## V-05 — Full Integration: 5-Role + Inertia-First + All Seeds Formalized + Seed L

**Axis**: Full integration
**Hypothesis**: V-05 is the ceiling-holding integration variation for R13, combining the
strongest axes from V-01 through V-04 and formalizing all R13 seeds plus introducing Seed L
(insight projection test). Architecture: 5-role pipeline (Archivist → Assessor → Inspector
→ Strategist → Narrator) from V-02, with Assessor running inertia-first and Inspector running
health-phase in severity-ordered topic order (Seeds H + D from V-01/V-04). The Inspector's
cross-role discrepancy check is formalized (Seed I from V-02). The Strategist produces tiered
actions (Seed K from V-04) with `resolves:` annotations (Seed A). The Narrator produces a
reconciliation pairing with a confidence annotation (Seeds B + E from R12). Seed L is new:
before writing the Team Insight, the Narrator must pass a projection test — explicitly state
whether the second-order pattern identified in the insight applies only to existing topics
or projects forward to topics the team has not yet started. This forces the insight to either
anchor to current evidence or declare its extrapolation scope, preventing vague
"cross-topic patterns" that neither confirm nor deny applicability to the wider topic space.

---

You are running the **Corps Leaderboard** skill in a 5-role inertia-first pipeline. Execute
each role completely before advancing to the next. No role may perform work assigned to
another role. Output each Gate checklist and Handoff artifact list verbatim before the next
role begins.

**Pipeline note**: The Assessor runs the Inertia Phase first (severity tiers assigned before
any health data is assessed). The Inspector runs the Health Phase second, reporting topics in
severity-tier order driven by the Assessor's output. The Strategist produces tiered actions.
The Narrator produces synthesis, reconciliation with confidence annotation, and the Team
Insight with a projection test.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Scans workspace, builds signal registry, builds
contributor index. Does NOT evaluate achievements, assess trajectory, rank contributors, or
write insights or actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path after `simulations/`
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. All subsequent roles do not run.

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

**Responsibility**: Trajectory assessment only. Evaluates inertia flags, severity tiers,
stale signals, and velocity trend. Does NOT evaluate achievements, milestones, or current-
state counts — those belong to the Inspector.

### 2.1 — Inertia Phase

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Assign a severity tier:
- `critical` — 2 or more flags raised (not counting healthy-momentum)
- `warning` — exactly 1 flag raised (not counting healthy-momentum)
- `healthy` — 0 non-momentum flags, or only healthy-momentum

Print inertia table: `topic_path | flags | trajectory note | severity`

Print stale signal table: `topic_path | stale_status` (`stale`, `active`, `date-unknown`).

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

Print nearest-miss assessment:

- **Level 1**: every topic 1 unit away (topic + achievement + exact gap). Sort ascending.
- **Level 2**: closest topic 2 units away. Only when no Level 1. State "Level 1: no topics
  are 1 unit away" first.

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

---

## ROLE 3: INSPECTOR

**Responsibility**: Current-state assessment only. Evaluates achievements, milestones, and
health metrics. Reports topics in severity-tier order driven by Assessor output. Runs a
cross-role discrepancy check. Does NOT restate inertia flags or trajectory claims from the
Assessor.

### 3.1 — Health Phase (topics in Assessor severity order)

**Topic ordering**: `critical` first, then `warning`, then `healthy`. Alphabetical within
each tier.

For each `topic_path` (in severity order), print:

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9
```

Evaluate all five achievements. Exact names only. LOCKED rows include specific unlock paths.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file |
| Signal Depth | >= 3 files |
| Full Sweep | >= 3 distinct namespaces within topic |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

```
| Achievement   | Status  | Evidence / Unlock Path              |
|---------------|---------|-------------------------------------|
```

When Solo Pioneer EARNED and Team Topic NOT YET: append
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]`.

Evaluate all three team milestones. Exact names. Evidence non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count`.

### 3.2 — Cross-Role Discrepancy Check

Compare the Assessor's inertia flags against the Inspector's health findings.

| Discrepancy type | Condition |
|------------------|-----------|
| stuck-at-first vs. Signal Depth EARNED | Assessor raised `stuck-at-first`; Inspector finds Signal Depth is EARNED |
| solo-hold vs. Team Topic EARNED | Assessor raised `solo-hold`; Inspector finds Team Topic is EARNED |
| namespace-thin vs. Full Sweep EARNED | Assessor raised `namespace-thin`; Inspector finds Full Sweep is EARNED |

Emit a discrepancy table:

```
## Cross-Role Discrepancy Table

| topic_path | Assessor flag | Inspector finding | Resolution |
|------------|--------------|-------------------|------------|
```

If no discrepancies: one row `| none | — | — | no discrepancies detected |`.

For each discrepancy: state which flag is retracted and why the Inspector's data is
authoritative. Format: `Assessor flag {flag-name} retracted for {topic_path}; Inspector
health data is authoritative.`

**Inspector Gate** — Verify and emit:

- [ ] Topics reported in severity order (critical → warning → healthy); each health header
  includes severity tier label and `Namespace diversity: {N}/9`
- [ ] All five achievement rows per topic; LOCKED rows include unlock paths; no trajectory
  language in Health Phase
- [ ] All three milestone names verbatim with non-empty evidence; debate starter proximity
  and namespace leader table present
- [ ] Cross-role discrepancy table emitted; any retracted flags documented with resolution

**Inspector Handoff** — Artifacts to Strategist:

1. Per-topic Health Phase achievement blocks in severity order (with tension markers)
2. Team milestone table (3 rows)
3. Debate starter proximity line and namespace leader table
4. Cross-role discrepancy table (with retraction statements where applicable)

---

## ROLE 4: STRATEGIST

**Responsibility**: Tiered next actions only. Produces the Next Actions list in
`[CRITICAL]` / `[WARNING]` / `[ADVANCING]` sections. Does NOT produce the leaderboard,
reconciliation pairing, or Team Insight.

### 4.1 — Nearest-Miss Confirmation

Transcribe the nearest-miss table from the Assessor Handoff. Do not recompute.

### 4.2 — Pre-Write Check

Before writing any action:
1. Identify all zero-score conditions: topics with 0 files, empty registry, empty leaderboard.
2. Identify all open inertia flags from the Assessor's Inertia Phase table. If any flag was
   retracted by the Inspector's discrepancy check, exclude it from `resolves:` consideration.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action eliminating a zero-score condition carries `prevents:`.
Advancement actions do not.

An action resolving an open (non-retracted) inertia flag MUST declare `resolves: {flag-name}`
(exact flag name: `stuck-at-first`, `solo-hold`, or `namespace-thin`).

### 4.3 — Tiered Next Actions

Write at least 3 actions total in three sections:

**[CRITICAL]** — Actions targeting topics with `critical` severity. If no `critical` topics:
`[CRITICAL]: no topics at critical severity.`

**[WARNING]** — Actions targeting topics with `warning` severity. If no `warning` topics:
`[WARNING]: no topics at warning severity.`

**[ADVANCING]** — Actions targeting `healthy` topics or team milestones.

The `prevents:` rule is embedded inside each relevant action row as the second structurally
independent enforcement point.

```
## Next Actions

### [CRITICAL]
1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank]

### [WARNING]
N. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank]

### [ADVANCING]
N. `{namespace}/{topic}` -> unlocks **{exact name}**
```

After all actions:

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Strategist Gate** — Verify and emit after the ACTIONS GATE line:

- [ ] Nearest-miss confirmation present
- [ ] Pre-write check complete; zero-score conditions and open flags identified; retracted
  flags excluded
- [ ] Three tier sections present; sections without qualifying topics include the "no topics
  at {tier} severity" line
- [ ] At least 3 actions total; each names namespace + topic + exact achievement or milestone;
  `prevents:` applied per 4.2 and 4.3 (two independent enforcement points);
  `resolves:` applied with exact flag names (no retracted flags); blank otherwise
- [ ] ACTIONS GATE line written with actual N substituted

**Strategist Handoff** — Artifacts to Narrator:

1. Nearest-miss assessment (confirmed from Assessor)
2. Tiered Next Actions list (all rows with `prevents:` and `resolves:` as written)
3. Pre-write check results (zero-score conditions and open flags, with retractions noted)
4. ACTIONS GATE line

---

## ROLE 5: NARRATOR

**Responsibility**: Synthesis only. Produces the Contributor Leaderboard, Collaboration Map,
reconciliation pairing with confidence annotation, Team Insight with projection test. Does
NOT re-scan, re-evaluate achievements, re-assess inertia, or modify the action list.

### 5.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical.
If all `unknown`: `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 5.2 — Collaboration Map

Print: `topic_path | contributors | collaboration_type` for topics where Team Topic is earned.
Types: `pair` (2), `ensemble` (3+). If none: `| none | — | no Team Topic earned yet |`.

### 5.3 — Cross-Dimensional Reconciliation with Confidence Annotation

Before writing the Team Insight, select exactly one observation from the Inspector's Health
Phase and exactly one from the Assessor's Inertia Phase that interact. If the discrepancy
check retracted any Assessor flags, the selected Inertia observation must be from a
non-retracted flag or a trajectory note.

State how they interact. Immediately after the pairing, emit a confidence annotation:

- `confidence: high` — interaction directly supported by specific evidence in both phases;
  a skeptical reader would accept it without argument
- `confidence: medium` — plausible but requires one inferential step
- `confidence: low` — speculative; requires two or more inferential steps beyond the data

State the rationale for the confidence level in one sentence.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding} | {one finding} | {how they connect} |

Confidence: {high/medium/low} — {rationale sentence}
```

### 5.4 — Team Insight with Projection Test

**Skeptic gate**: The Skeptic has read all output from the Archivist, Assessor, Inspector,
and Strategist — every achievement table, every milestone row, every inertia flag, every
severity tier, every trajectory note, the discrepancy table, the stale signal table, the
velocity summary, the nearest-miss assessment, the tiered action list (with all `prevents:`
and `resolves:` annotations), the leaderboard, the collaboration map, and the reconciliation
pairing with its confidence annotation. The insight MUST contain something the Skeptic would
not already know from all of that material.

An insight that restates an inertia flag, severity tier, reconciliation pairing, confidence
annotation, or tiered action grouping fails. An insight that only adjusts the confidence
level without adding new inference also fails. A passing insight surfaces a second-order
pattern — a risk, convergence, or cross-topic trajectory inference — that requires
synthesizing across health and inertia in a way no single block, the tiered action list, or
the reconciliation pairing with its confidence annotation directly reveals.

**Projection test** — After writing the Team Insight sentence, emit a projection annotation
on a new line using one of two forms:

- `projection: local — this pattern applies only to {list of topic_paths} currently in the
  workspace` — when the insight is grounded in specific file/contributor/achievement data
  and does not extend beyond observed topics.
- `projection: forward — this pattern is likely to apply to topics the team has not yet
  started, specifically {description of expected topic type or namespace}` — when the insight
  identifies a structural tendency (e.g., a contributor pattern or namespace gap) that a new
  topic in the same domain would inherit.

The projection annotation is a separate, structured statement — not part of the insight
sentence itself. It forces the model to explicitly bound or extend the insight's scope.

Write one insight sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific
contributor or topic name. Then on a new line: the projection annotation.

**Narrator Gate** — Verify and emit:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Collaboration map present (or "none" row)
- [ ] Reconciliation pairing written with one Health observation (non-contradicted by
  discrepancy check), one Inertia observation (non-retracted), and interaction note
- [ ] Confidence annotation present (`high`/`medium`/`low`) with one-sentence rationale
- [ ] Team Insight written as one sentence; Skeptic gate verified — Skeptic knew every
  achievement, milestone, inertia flag, severity tier, trajectory, discrepancy, stale, velocity,
  tiered action (with all annotations), leaderboard, collaboration, reconciliation, AND
  confidence data; insight is a new cross-dimensional inference beyond all of that
- [ ] Projection annotation present: either `projection: local` with topic list or
  `projection: forward` with description; correctly bounding or extending the insight scope
