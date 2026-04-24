---
skill: quest-variate
skill_target: corps-leaderboard
round: 15
date: 2026-03-17
rubric_version: 12
---

# Variate R15 — corps-leaderboard

5 complete prompt body variations for the `corps-leaderboard` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

**R14 ceiling against v12**: V-05 100.00 (25/25). V-04 99.60 (24/25 — fails C-33). V-01/02/03
99.20 (23/25 — fail both C-32 and C-33). The universal ceiling opportunity is to carry Seed N
(milestone proximity ladders, C-32) and Seed S (echo detection, C-33) into all 5 variations.

**R14 seeds entering R15**:
- Seed A: `resolves: {flag-name}` on inertia-flag-resolving actions — universal (5/5 R14).
- Seed B: Pre-synthesis cross-dimensional reconciliation pairing — universal (5/5 R14).
- Seed H: Severity-ordered health topic reporting (critical -> warning -> healthy) — universal.
- Seed I: Cross-role discrepancy validation table — 1/5 R14 (V-05). Carry in R15 V-05.
- Seed K: Tiered action output (`[CRITICAL]` / `[WARNING]` / `[ADVANCING]`) — 2/5 R14
  (V-04, V-05). Carry in R15 V-04, V-05.
- Seed L: Insight projection test (anchored vs. extrapolated scope) — 1/5 R14 (V-05).
  Carry in R15 V-05.
- Seed M: Action-to-gap binding (`[closes: {achievement} gap of {N} {unit} for {topic}]`) —
  2/5 R14 (V-04, V-05). Carry in R15 V-04, V-05.
- Seed N: Milestone proximity ladder — per-precondition breakdown for NOT YET milestones.
  Previously 2/5 R14 (V-04, V-05). **R15 target: universal (5/5).**
- Seed O: Insight confidence band (`[confidence: HIGH/MEDIUM/LOW] [supporting observations: N]`)
  — 2/5 R14 (V-01, V-05). Carry in R15 V-05.
- Seed R: Leaderboard velocity column — 1/5 R14 (V-05). Carry in R15 V-05.
- Seed S: Echo detection check — flag/achievement logical consistency scan with echo table and
  retraction statements. Previously 1/5 R14 (V-05). **R15 target: universal (5/5).**

**New seeds introduced in R15**:
- Seed T: Achievement rate column — `rate` column in leaderboard: achievements earned divided by
  total signal files (e.g., 2 achievements / 4 signals = 0.50). Measures unlock efficiency.
  A contributor accumulating signals without earning new achievements carries rate 0.00.
- Seed U: Contributor cohort classification — `cohort` column in leaderboard: `specialist` if
  >= 50% of contributor's signals are in a single namespace; `generalist` if signals span >= 3
  distinct namespaces; `focused` otherwise (exactly 2 namespaces). Single-namespace contributors
  are `specialist` by definition.
- Seed V: Multi-round action sequencing — actions grouped by gap distance rather than severity
  tier: Round 1 (exactly 1 signal closes the gap), Round 2 (2-3 signals), Round 3 (4+ signals
  or coordination required). Milestone proximity ladder data maps directly onto round boundaries.
- Seed W: Milestone coalition mapping — for each NOT YET milestone, after the proximity ladder,
  identify the internal coalition path (existing contributors can close the gap: name who adds
  what) vs. the external path (a new contributor must be recruited: name which topic needs one).
- Seed X: Insight falsifiability contract — Team Insight appends a two-line contract:
  `[holds if: {specific observable condition naming a topic, contributor, or metric threshold}]`
  `[falsified by: {specific observable condition that would invalidate the insight}]`.
  Vague conditions ("holds if things continue") fail — conditions must name specific entities.

**R15 design targets**:
- All 5 variations carry Seeds A+B+H+N+S as formalized universal requirements.
- V-01: Phrasing register (prose health blocks). 3-role. Seeds A+B+H+N+S. New: Seed U.
  Expected: 25/25 -> 100.00.
- V-02: Output format (multi-round action sequencing). 3-role. Seeds A+B+H+N+S. New: Seed V.
  Expected: 25/25 -> 100.00.
- V-03: Role sequence (early leaderboard role with achievement rate). 4-role. Seeds A+B+H+N+S.
  New: Seed T. Expected: 25/25 -> 100.00.
- V-04: Combination (inertia-first + tiered actions + coalition mapping). 4-role.
  Seeds A+B+H+K+M+N+S. New: Seed W. Expected: 25/25 -> 100.00.
- V-05: Full integration (5-role + Seeds A+B+H+I+K+L+M+N+O+R+S + new T+U+V+W+X).
  Expected: 25/25 -> 100.00.

**Expected scoring against v12** (formula: `90 + (passed/25) x 10`):
- V-01: 25/25 -> **100.00**
- V-02: 25/25 -> **100.00**
- V-03: 25/25 -> **100.00**
- V-04: 25/25 -> **100.00**
- V-05: 25/25 -> **100.00**

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Phrasing register (prose health blocks) + Seed U (cohort classification) | V-01 |
| Output format (multi-round action sequencing Round 1/2/3) + Seed V | V-02 |
| Role sequence (early leaderboard role before Analyst) + Seed T (achievement rate) | V-03 |
| Combination: inertia-first + tiered actions + coalition mapping + Seeds K+M+W | V-04 |
| Full integration: 5-role + Seeds K+L+M+O+R + new T+U+V+W+X | V-05 |

---

## V-01 — Field-Report Prose + Cohort Classification + 3-Role + Seeds A+B+H+N+S + Seed U

**Axis**: Phrasing register
**Hypothesis**: R14 V-01 used field-report prose for health blocks but lacked C-32 (proximity
ladders) and C-33 (echo detection), scoring 99.20. R15 V-01 adds both universally: milestone
proximity ladders inline after NOT YET milestone rows, and an Echo Detection section (§2.4)
after the Health Phase. New axis: contributor cohort classification (Seed U) — each leaderboard
row carries a `cohort` label (`specialist` if >= 50% signals in one namespace; `generalist` if
signals span >= 3 namespaces; `focused` otherwise). The hypothesis is that cohort framing
changes team interpretation of the leaderboard: a top-ranked `specialist` signals depth but
concentration risk; a top-ranked `generalist` signals breadth but potentially shallow coverage.

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

- [ ] Registry table printed with all four columns (`topic_path`, `namespace`, `contributor`,
  `file`)
- [ ] Namespace coverage line printed with active and empty namespace lists
- [ ] Contributor index printed with all three columns

**Archivist Handoff** — The following artifacts transfer from the Archivist to the Analyst:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line (active and empty namespace lists)
3. Contributor index table (columns: `contributor`, `topic_path`, `file_count`)

The Analyst begins with these three artifacts. It does not re-scan the workspace.

---

## ROLE 2: ANALYST

**Responsibility**: Evaluation only. The Analyst first establishes trajectory (Inertia Phase,
§2.1), then reports current signal state (Health Phase, §2.2) in inertia-severity order using
field-report prose, then runs the Echo Detection scan (§2.4) to verify logical consistency
between inertia flags and achievement claims, then computes the Nearest-Miss Assessment (§2.3).
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

A topic with no flags gets `flags = none`, a brief healthy note, and `severity = healthy`.

Print stale signal table: `topic_path | stale_status` (`stale` / `active` / `date-unknown`
using file modification dates where accessible).

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

Classification: > 50% topics at `healthy` = increasing; < 25% = stalled; otherwise flat.

**Section 2.1 Gate** — Emit before proceeding to Section 2.2:

- [ ] Inertia table present with severity column; every topic evaluated for all four flags
- [ ] No static file counts, achievement statuses, or coverage totals in Inertia Phase content
  (prohibited — these are current-state data belonging to the Health Phase)
- [ ] Stale signal table and velocity summary present

### 2.2 — Health Phase (RUNS SECOND — topics ordered by inertia severity)

Reports current signal state only using field-report prose. Does NOT include trajectory claims,
momentum language, or inertia flag restatements — those are trajectory data belonging to the
Inertia Phase.

**Topic ordering**: Report topics in descending severity order — `critical` first, then
`warning`, then `healthy`. Within each tier, sort alphabetically by `topic_path`.

For each `topic_path` (in severity order), write a health field report:

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Field Report — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9

{topic_path} currently has {N} signal file(s) across {M} namespace(s), contributed by
{contributor list}. **First Signal** is {EARNED — {evidence} / LOCKED — needs at least 1 file}.
**Signal Depth** is {EARNED — {evidence} / LOCKED — needs {X} more file(s) to reach 3}.
**Full Sweep** is {EARNED — {evidence} / LOCKED — needs signals in {X} more namespace(s) to
reach 3}. **Solo Pioneer** is {EARNED — {evidence} / LOCKED — needs exactly 1 contributor with
at least 1 file}. **Team Topic** is {EARNED — {evidence} / LOCKED — needs {X} more
contributor(s) each with at least 1 file}.
```

Achievement names must be exact and bold — paraphrasing fails. Every LOCKED achievement must
state the specific unlock requirement inline. EARNED achievements state the earned condition.

When Solo Pioneer is EARNED and Team Topic is NOT YET: append on a new line:
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]`

Evaluate all three team milestones using exact names. Evidence must be non-empty for every row.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file exists in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

For every NOT YET milestone, print a **Milestone Proximity Ladder** on the line immediately
following its table row:

- `first team signal` NOT YET:
  `Proximity ladder: 1 signal file in any namespace for any topic closes this milestone.`
- `shared coverage` NOT YET: count topics with >= 2 distinct contributors.
  `Proximity ladder: {N} qualifying topics (need 2 total). Per-topic contributor deficit:
  {topic_A} needs {M} more contributor(s); {topic_B} needs {M} more contributor(s); ...`
  List every topic that is a candidate (>= 1 existing contributor) with its individual
  deficit. Topics with 0 files are not candidates.
- `debate starter` NOT YET:
  `Proximity ladder: nearest is {topic_path} at {N}/3 contributors. Requires {M} more
  distinct contributor signal(s). Each additional distinct contributor on this topic closes
  1 unit of this gap.`

EARNED milestones do not receive a proximity ladder.

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count` for each active namespace.

### 2.3 — Nearest-Miss Assessment

- **Level 1** — every topic exactly 1 unit away from any achievement threshold. State: topic
  name + achievement name + exact gap. Sort ascending by gap.
- **Level 2** — closest topic 2 units away. Write Level 2 ONLY when no Level 1 topic exists.
  Explicitly state "Level 1: no topics are 1 unit away" before listing Level 2.

Print: `topic | achievement | gap | level`

### 2.4 — Echo Detection

After completing Sections 2.2 and 2.3, run a logical consistency scan across all topics.
Check every topic for the following mutual exclusion violations:

**Rule A** — `healthy-momentum` flag raised AND `Solo Pioneer` is EARNED:
`healthy-momentum` requires >= 2 distinct contributors; `Solo Pioneer` requires exactly 1
contributor. Both cannot simultaneously be true for the same topic. Violation: retract
`healthy-momentum` and state: `healthy-momentum flag retracted for {topic_path}; incompatible
with Solo Pioneer EARNED (exactly 1 contributor required by Solo Pioneer).`

**Rule B** — Any inertia flag raised AND `First Signal` is LOCKED:
Inertia flags evaluate signal properties that require at least one file. If `First Signal` is
LOCKED (0 files), no inertia flag can be meaningfully raised. Violation: retract the flag and
state: `{flag-name} flag retracted for {topic_path}; First Signal is LOCKED — no files to
evaluate; inertia flags require at least 1 file.`

Produce an echo table. If no violations are found, write one row: `| none | — | — | — | — |`.

```
## Echo Detection Table

| topic_path | Rule violated | Flag retracted | Achievement | Resolution |
|------------|---------------|----------------|-------------|------------|
```

For each retracted flag, append an explicit retraction statement on its own line:
`ECHO RETRACTION: {flag-name} on {topic_path} invalidated — {reason}.`

**Section 2.2–2.4 Gate** — Emit before transferring artifacts:

- [ ] Topics reported in severity order (critical first, then warning, then healthy);
  alphabetical within tier; flat alpha ordering across tiers fails
- [ ] Every topic's field report includes header with severity label and
  `Namespace diversity: {N}/9`; all five achievements named in bold with exact names; LOCKED
  achievements include inline unlock requirements; EARNED achievements state evidence
- [ ] No trajectory language, momentum claims, or inertia flag restatements in Health Phase
  field reports; Inertia Phase table contains no static file counts or achievement statuses
  (cross-contamination check: prohibited content absent from both phases)
- [ ] All three milestone names verbatim with non-empty evidence; proximity ladders present
  for ALL NOT YET milestones with per-component deficit breakdowns; debate starter proximity
  line and namespace leader table present
- [ ] Nearest-miss assessment present (Level 1, or Level 2 with "Level 1: no topics are 1
  unit away" stated first), sorted ascending by gap
- [ ] Echo Detection Table emitted; both Rule A and Rule B checked for every topic; retraction
  statements written for each violation; "none detected" row if no violations found

**Analyst Handoff** — The following artifacts transfer from the Analyst to the Publisher:

1. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`, `severity`)
2. Stale signal table and velocity summary line
3. Per-topic Health Phase field reports in severity order (one field report per `topic_path`)
4. Team milestone table (3 rows: milestone, status, evidence) with inline proximity ladders
   for all NOT YET milestones
5. Debate starter proximity line and namespace leader table
6. Nearest-miss assessment table (columns: `topic`, `achievement`, `gap`, `level`)
7. Echo Detection Table with all retraction statements (or "none detected")

The Publisher begins with all seven artifacts plus the Archivist's three. It does not
re-evaluate achievements, re-assess inertia, or re-run echo detection.

---

## ROLE 3: PUBLISHER

**Responsibility**: Synthesis, leaderboard, reconciliation, insight, and actions only. Works
from all prior output. Does NOT re-scan the workspace, re-evaluate achievements, or re-assess
inertia.

### 3.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical.

For each contributor, compute:
- `cohort` label: `specialist` if >= 50% of the contributor's signals are in a single
  namespace; `generalist` if the contributor's signals span >= 3 distinct namespaces;
  `focused` otherwise (exactly 2 namespaces). A contributor with all signals in 1 namespace
  is `specialist` by definition.

If all contributors are `unknown`: write one row
`| 1 | no contributor metadata found | — | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered | Cohort |
|------|-------------|---------------|----------------|--------|
```

### 3.2 — Collaboration Signal

Print: `topic_path | contributors | collaboration_type` for topics where Team Topic is EARNED.
Types: `pair` (exactly 2 contributors), `ensemble` (3+). If no topic earned Team Topic:
one row `| none | — | no Team Topic earned yet |`.

### 3.3 — Nearest-Miss Confirmation

Transcribe the nearest-miss table from the Analyst Handoff. Do not recompute.

### 3.4 — Cross-Dimensional Reconciliation

Select exactly one observation from the Health Phase field reports and exactly one from the
Inertia Phase table that interact with or bear on each other. State the interaction.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase field reports} | {one finding from Inertia Phase} | {how they connect} |
```

### 3.5 — Team Insight

**Skeptic gate**: A Skeptic who has read all Archivist and Analyst output already knows: every
achievement status (from field reports), every milestone row (including the per-component
deficit breakdowns in all proximity ladders), every inertia flag (including echo-retracted
flags and their retraction reasons), every severity tier, every trajectory note, the stale
signal table, the velocity summary, the nearest-miss assessment, the cohort classifications
in the leaderboard, the collaboration signal table, and the reconciliation pairing in 3.4.
The insight MUST contain something the Skeptic would not already know from all of that.

An insight that restates any field report achievement status, milestone status, proximity
ladder entry, inertia flag (retracted or active), severity tier, velocity category, cohort
label, or reconciliation row fails. A passing insight surfaces a second-order pattern — a
risk, convergence, or cross-topic trajectory inference — requiring synthesis across health,
inertia, and cohort data that no single field report, the proximity ladders, the echo
retractions, or the reconciliation pairing directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

### 3.6 — Pre-Write Check

Before writing any action:

1. Identify all zero-score conditions: topics with 0 files, empty registry, empty leaderboard.
   Record each explicitly.
2. Identify all open inertia flags from the Analyst's Inertia Phase table. Flags that were
   retracted in the Echo Detection Table are EXCLUDED — do NOT write `resolves:` actions
   targeting echo-retracted flags. Record post-retraction flag status for each topic.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action whose primary purpose is eliminating a state where the output
would score zero carries the `prevents:` prefix. Advancement actions do not.

An action resolving an open (non-retracted) inertia flag MUST declare
`resolves: {flag-name}` using the exact flag name (`stuck-at-first`, `solo-hold`, or
`namespace-thin`). Actions not resolving a specific flag leave `resolves:` blank.

### 3.7 — Next Actions

Write at least 3 actions. Each must name: (1) a specific namespace and topic path, (2) the
exact achievement or milestone name it unlocks. The `prevents:` rule is embedded inside each
relevant action row as the second structurally independent enforcement point.

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

- [ ] Leaderboard present with all five columns (Rank, Contributor, Total Signals, Topics
  Covered, Cohort), ranked descending; cohort label assigned per definition
- [ ] Collaboration signal table present (or "none" row if no Team Topic earned)
- [ ] Nearest-miss confirmation transcribed from Analyst Handoff (not recomputed)
- [ ] Reconciliation pairing: one Health observation (from field reports), one Inertia
  observation, interaction note
- [ ] Team Insight as one sentence; Skeptic gate verified — Skeptic knew every achievement
  (field reports), milestone (with proximity ladder breakdowns), inertia flag (including
  echo-retracted with reasons), severity tier, trajectory note, stale signal, velocity,
  nearest-miss, cohort labels, collaboration, and reconciliation data; insight is a new
  cross-dimensional inference not derivable from any single block, any proximity ladder, or
  the reconciliation pairing
- [ ] Pre-write check complete; zero-score conditions and open (non-retracted) inertia flags
  identified; echo-retracted flags explicitly excluded from `resolves:` targeting
- [ ] At least 3 actions; each names namespace + topic + exact achievement or milestone;
  `prevents:` applied per 3.6 and 3.7 (two independent enforcement points); `resolves:` with
  exact flag names on non-retracted flag-resolving actions; blank otherwise
- [ ] ACTIONS GATE line written with actual N count substituted

---

## V-02 — Multi-Round Action Sequencing + 3-Role + Seeds A+B+H+N+S + Seed V

**Axis**: Output format
**Hypothesis**: All R14 variations grouped actions by severity tier (CRITICAL/WARNING/ADVANCING)
or left them flat. This variation introduces a temporal sequencing model as the grouping axis:
Round 1 (exactly 1 signal closes the gap), Round 2 (2-3 signals needed), Round 3 (4+ signals
or coordination required across multiple contributors). The hypothesis is that temporal grouping
surfaces sequencing information that severity-tier grouping misses: a WARNING topic might be a
1-signal fix (Round 1 priority); a CRITICAL topic needing 4 coordinated contributor additions
belongs in Round 3. Proximity ladder data maps directly onto round boundaries — the per-topic
deficit counts from the ladder are the round assignment inputs. Seeds N and S are now universal.

---

You are running the **Corps Leaderboard** skill in a 3-role pipeline. Execute each role
completely before advancing to the next. No role may perform work assigned to another role.
Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: Within the Analyst role, the Inertia Phase (trajectory) runs BEFORE the
Health Phase (current state). The Health Phase reports topics in descending inertia severity
order — critical first, then warning, then healthy. Within each tier, sort alphabetically.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Scans workspace, builds signal registry, constructs
contributor index. Does NOT evaluate achievements, assess trajectory, rank contributors, or
write insights or actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path segment after `simulations/`
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first
  `-` > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. Roles 2 and 3 do not run.

Print registry: `topic_path | namespace | contributor | file`

Print namespace coverage:
`Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`

The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

### 1.2 — Contributor Index

Print: `contributor | topic_path | file_count`.

**Archivist Gate** — Verify and emit:

- [ ] Registry table with all four columns (`topic_path`, `namespace`, `contributor`, `file`)
- [ ] Namespace coverage line with active and empty namespace lists
- [ ] Contributor index with all three columns

**Archivist Handoff** — Artifacts to Analyst:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line (active and empty namespace lists)
3. Contributor index table (columns: `contributor`, `topic_path`, `file_count`)

---

## ROLE 2: ANALYST

**Responsibility**: Evaluation only. Runs Inertia Phase (§2.1) first, then Health Phase (§2.2)
with milestone proximity ladders, then Nearest-Miss Assessment (§2.3), then Echo Detection
(§2.4). Sub-phases structurally separated. Does NOT rank contributors, write insights, or
write actions.

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

Severity tiers:
- `critical` — 2+ non-momentum flags
- `warning` — exactly 1 non-momentum flag
- `healthy` — 0 non-momentum flags

Print inertia table: `topic_path | flags | trajectory note | severity`

Print stale signal table: `topic_path | stale_status` (`stale` / `active` / `date-unknown`).

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

> 50% healthy = increasing; < 25% healthy = stalled; otherwise flat.

**Section 2.1 Gate** — Emit before proceeding to Section 2.2:

- [ ] Inertia table with severity column; every topic evaluated for all four flags
- [ ] No file counts, achievement statuses, or coverage totals in Inertia Phase content
- [ ] Stale signal table and velocity summary present

### 2.2 — Health Phase (RUNS SECOND — ordered by severity tier)

Reports current signal state only. Does NOT include trajectory claims or inertia flag
restatements.

**Topic ordering**: critical first, then warning, then healthy. Alphabetical within each tier.

For each `topic_path` (in severity order):

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9
```

Evaluate all five achievements. Exact names only. LOCKED rows include unlock paths.

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

For every NOT YET milestone, print a **Milestone Proximity Ladder** immediately following:

- `first team signal` NOT YET:
  `Proximity ladder: 1 signal file in any namespace for any topic closes this milestone.`
- `shared coverage` NOT YET:
  `Proximity ladder: {N} qualifying topics (need 2 total). Per-topic contributor deficit:
  {topic_A} needs {M} more contributor(s); {topic_B} needs {M} more contributor(s); ...`
- `debate starter` NOT YET:
  `Proximity ladder: nearest is {topic_path} at {N}/3 contributors. {M} more distinct
  contributor signal(s) needed.`

EARNED milestones do not receive a proximity ladder.

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count`.

### 2.3 — Nearest-Miss Assessment

- **Level 1** — every topic 1 unit away from any threshold (topic + achievement + gap).
  Sort ascending.
- **Level 2** — closest 2 units away. ONLY when no Level 1 exists. State "Level 1: no
  topics are 1 unit away" before listing Level 2.

Print: `topic | achievement | gap | level`

### 2.4 — Echo Detection

Run a logical consistency scan on every topic for the two mutual exclusion rules:

**Rule A** — `healthy-momentum` flag raised AND `Solo Pioneer` EARNED:
`healthy-momentum` requires >= 2 contributors; `Solo Pioneer` requires exactly 1. Retract
`healthy-momentum` and state:
`ECHO RETRACTION: healthy-momentum on {topic_path} retracted — incompatible with Solo Pioneer
EARNED.`

**Rule B** — Any inertia flag raised AND `First Signal` LOCKED:
Inertia flags require at least 1 file; 0-file topics have no evaluable signals. Retract the
flag and state:
`ECHO RETRACTION: {flag-name} on {topic_path} retracted — First Signal LOCKED, no files to
evaluate.`

```
## Echo Detection Table

| topic_path | Rule violated | Flag retracted | Achievement | Resolution |
|------------|---------------|----------------|-------------|------------|
```

If no violations: one row `| none | — | — | — | — |`.

**Section 2.2–2.4 Gate** — Emit before transferring artifacts:

- [ ] Topics in severity order (critical -> warning -> healthy); alphabetical within tier;
  every topic has `Namespace diversity: {N}/9`; all five achievements with exact names;
  LOCKED rows include unlock paths; no trajectory language in Health Phase
- [ ] Inertia Phase table present; no static file counts or achievement statuses restated in
  Inertia Phase content; no trajectory claims in Health Phase (cross-contamination check)
- [ ] All three milestone names verbatim with non-empty evidence; proximity ladders for ALL
  NOT YET milestones with per-component deficit breakdowns
- [ ] Nearest-miss: Level 1 with ascending sort, or Level 2 with "Level 1 empty" note first
- [ ] Echo Detection Table emitted; Rule A and Rule B checked for every topic; retraction
  statements written for violations; "none detected" row if clean

**Analyst Handoff** — Artifacts to Publisher:

1. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`, `severity`)
2. Stale signal table and velocity summary
3. Per-topic Health Phase achievement blocks in severity order
4. Team milestone table (3 rows) with proximity ladders for all NOT YET milestones
5. Debate starter proximity line and namespace leader table
6. Nearest-miss assessment table (columns: `topic`, `achievement`, `gap`, `level`)
7. Echo Detection Table with retraction statements (or "none detected")

---

## ROLE 3: PUBLISHER

**Responsibility**: Synthesis, leaderboard, reconciliation, insight, and actions. Does NOT
re-scan, re-evaluate achievements, or re-assess inertia.

### 3.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical.
If all `unknown`: `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 3.2 — Collaboration Signal

Print: `topic_path | contributors | collaboration_type` for Team Topic EARNED topics.
Types: `pair` (2), `ensemble` (3+). If none: `| none | — | no Team Topic earned yet |`.

### 3.3 — Nearest-Miss Confirmation

Transcribe the nearest-miss table from the Analyst Handoff. Do not recompute.

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

**Skeptic gate**: The Skeptic has read all Archivist and Analyst output and already knows:
every achievement status, every milestone row (including all proximity ladder per-component
breakdowns), every inertia flag (including echo-retracted flags and their retraction reasons),
every severity tier, every trajectory note, the stale signal table, the velocity summary, the
nearest-miss assessment, the leaderboard, the collaboration signal table, and the reconciliation
pairing in 3.4. The insight MUST contain something the Skeptic would not already know.

An insight that restates any achievement, milestone, proximity ladder entry, inertia flag,
echo retraction, velocity, or reconciliation row fails. A passing insight surfaces a
second-order pattern requiring synthesis across health and inertia data in a way no single
block or the reconciliation pairing directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

### 3.6 — Pre-Write Check

Before writing any action:

1. Identify all zero-score conditions. Record explicitly.
2. Identify all open inertia flags from the Analyst's inertia table. Flags retracted in the
   Echo Detection Table are EXCLUDED — do NOT write `resolves:` actions for retracted flags.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action eliminating a zero-score condition carries `prevents:`.
Advancement actions do not.

An action resolving an open (non-retracted) inertia flag MUST declare `resolves: {flag-name}`
with the exact flag name. Other actions leave `resolves:` blank.

### 3.7 — Multi-Round Next Actions

Determine the round for each action based on the total gap it must close:
- **Round 1** — gap is exactly 1 signal (immediate win; achievable in one contribution)
- **Round 2** — gap is 2-3 signals (sprint-level; achievable within one iteration)
- **Round 3** — gap is 4+ signals, or requires coordination across multiple contributors
  (strategic; plan for next sprint boundary)

Use the nearest-miss table and milestone proximity ladder data as the gap source. Write at
least 3 actions. Each must name a specific namespace + topic and the exact achievement or
milestone it unlocks. `prevents:` rule is the second structurally independent enforcement
point embedded in each relevant row.

```
## Next Actions

### Round 1 — Immediate (1 signal closes the gap)
1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank]
...

### Round 2 — Sprint (2-3 signals needed)
N. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank]
...

### Round 3 — Strategic (4+ signals or coordination required)
N. `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: blank or {flag-name}]
...
```

If no actions fall in a round, write: `Round {N}: no actions at this horizon.`

After all actions (N = actual count of `prevents:`-prefixed actions across all rounds):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Publisher Gate** — Verify and emit after ACTIONS GATE:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Collaboration signal table present (or "none" row)
- [ ] Nearest-miss confirmation transcribed from Analyst Handoff
- [ ] Reconciliation pairing: one Health observation, one Inertia observation, interaction
- [ ] Team Insight as one sentence; Skeptic gate verified — Skeptic knew every achievement,
  milestone (with proximity ladders), inertia flag (with echo retractions), severity tier,
  velocity, nearest-miss, leaderboard, collaboration, and reconciliation data; insight is new
  cross-dimensional inference not derivable from any single block
- [ ] Pre-write check complete; echo-retracted flags excluded from `resolves:` targeting
- [ ] Actions grouped into Round 1 / Round 2 / Round 3; empty rounds noted; each action names
  namespace + topic + exact name; `prevents:` at two independent locations (3.6 and 3.7);
  `resolves:` with exact names on non-retracted flag actions; ACTIONS GATE with actual N

---

## V-03 — Early Leaderboard Role + 4-Role + Seeds A+B+H+N+S + Seed T (Achievement Rate)

**Axis**: Role sequence
**Hypothesis**: In all R14 variations, the contributor leaderboard is produced in the final
synthesis role, after health analysis. This variation moves leaderboard computation into Role
2 (Ranker), running before the Analyst — so contributor velocity data informs the Analyst's
inertia assessment. New Seed T: each leaderboard row includes an `achievement_rate` column
(achievements earned / total signal files; e.g., 2 achievements / 4 signals = 0.50). A
contributor accumulating signals without earning achievements carries rate 0.00 — potentially
adding narrow-namespace depth. Rate 1.00 indicates maximally efficient diversification. The
hypothesis is that early availability of achievement rate data allows the Analyst to enrich
trajectory notes — a `solo-hold` topic whose sole contributor has rate 0.00 implies a
different trajectory than one whose contributor has rate 0.75.

---

You are running the **Corps Leaderboard** skill in a 4-role pipeline. Execute each role
completely before advancing to the next. No role may perform work assigned to another role.
Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Pipeline note**: The Ranker (Role 2) computes the contributor leaderboard with achievement
rates before the Analyst runs — leaderboard data is available to the Analyst as context.
The Analyst (Role 3) runs Inertia Phase first, then Health Phase with proximity ladders, then
Echo Detection. The Publisher (Role 4) produces synthesis, insight, and actions.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Scans workspace, builds signal registry, constructs
contributor index. Does NOT evaluate achievements, rank contributors, assess trajectory, write
insights, or write actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path segment after `simulations/`
- `namespace` — first segment of `topic_path`
- `contributor` — `author:` > `contributor:` > filename prefix before first `-` > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. All other roles do not run.

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

**Archivist Handoff** — Artifacts to Ranker:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line (active and empty namespace lists)
3. Contributor index table (columns: `contributor`, `topic_path`, `file_count`)

---

## ROLE 2: RANKER

**Responsibility**: Contributor leaderboard only. Computes rank, signal count, topics covered,
and achievement rate for each contributor. Does NOT evaluate per-topic achievements, assess
trajectory, write insights, or write actions. The Ranker's leaderboard output is available to
the Analyst as contextual input.

### 2.1 — Contributor Leaderboard with Achievement Rate

For each contributor, count:
- `total_signals` — total files attributed to this contributor
- `topics_covered` — distinct `topic_path` values
- `achievements_earned` — count of distinct achievements this contributor has unlocked
  across all their topics (count once per topic per achievement: e.g., if contributor owns
  3 files across 2 topics and both have First Signal, that is 2 achievements)
- `achievement_rate` — `achievements_earned / total_signals`, rounded to 2 decimal places.
  If `total_signals` = 0, write `N/A`.

Rank descending by `total_signals`. Ties: alphabetical.
If all `unknown`: `| 1 | no contributor metadata found | — | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered | Achievement Rate |
|------|-------------|---------------|----------------|-----------------|
```

Print collaboration signal: `topic_path | contributors | collaboration_type` for Team Topic
EARNED topics. Types: `pair` (2), `ensemble` (3+). If none:
`| none | — | no Team Topic earned yet |`.

**Ranker Gate** — Verify and emit:

- [ ] Leaderboard present with all five columns (Rank, Contributor, Total Signals, Topics
  Covered, Achievement Rate); ranked descending; ties alphabetical
- [ ] `achievement_rate` is a computed decimal value (achievements / signals), not a category
- [ ] Collaboration signal table present (or "none" row)

**Ranker Handoff** — Artifacts to Analyst:

1. Registry table (from Archivist)
2. Namespace coverage line (from Archivist)
3. Contributor index table (from Archivist)
4. Contributor leaderboard (Rank, Contributor, Total Signals, Topics Covered,
   Achievement Rate)
5. Collaboration signal table

---

## ROLE 3: ANALYST

**Responsibility**: Evaluation only. Uses the Ranker's leaderboard as contextual input for
trajectory notes. Runs Inertia Phase (§3.1) first, then Health Phase (§3.2) with proximity
ladders, then Nearest-Miss (§3.3), then Echo Detection (§3.4). Does NOT re-rank contributors,
write insights, or write actions.

### 3.1 — Inertia Phase (RUNS FIRST)

Reports trajectory and momentum only. Does NOT include file counts, achievement statuses, or
coverage totals. May reference contributor achievement rates from the Ranker leaderboard in
trajectory notes (e.g., "sole contributor has achievement_rate 0.00 — adding files without
earning new achievements").

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Severity tiers:
- `critical` — 2+ non-momentum flags
- `warning` — 1 non-momentum flag
- `healthy` — 0 non-momentum flags

Print inertia table: `topic_path | flags | trajectory note | severity`

Print stale signal table: `topic_path | stale_status`.

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

**Section 3.1 Gate** — Emit before proceeding:

- [ ] Inertia table with severity column; all four flags evaluated per topic
- [ ] No file counts or achievement statuses in Inertia Phase content
- [ ] Stale signal table and velocity summary present

### 3.2 — Health Phase (RUNS SECOND — ordered by severity tier)

Reports current signal state only. Does NOT include trajectory claims or inertia flag
restatements.

**Topic ordering**: critical first, then warning, then healthy. Alphabetical within tier.

For each `topic_path` (in severity order), print:

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9
```

Evaluate all five achievements with exact names. LOCKED rows include unlock paths.

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

For every NOT YET milestone, print a **Milestone Proximity Ladder** immediately after its row:

- `first team signal` NOT YET:
  `Proximity ladder: 1 signal file in any namespace for any topic closes this milestone.`
- `shared coverage` NOT YET:
  `Proximity ladder: {N} qualifying topics (need 2 total). Per-topic deficit:
  {topic_A} needs {M} more contributor(s); {topic_B} needs {M} more contributor(s); ...`
- `debate starter` NOT YET:
  `Proximity ladder: nearest is {topic_path} at {N}/3 contributors. {M} more distinct
  contributor signal(s) needed.`

EARNED milestones do not receive a proximity ladder.

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count`.

### 3.3 — Nearest-Miss Assessment

- **Level 1** — every topic 1 unit away from any threshold. Sort ascending.
- **Level 2** — closest 2 units away. ONLY when no Level 1. State "Level 1: no topics are
  1 unit away" first.

Print: `topic | achievement | gap | level`

### 3.4 — Echo Detection

Check every topic for two mutual exclusion rules:

**Rule A** — `healthy-momentum` raised AND `Solo Pioneer` EARNED: retract `healthy-momentum`.
`ECHO RETRACTION: healthy-momentum on {topic_path} retracted — incompatible with Solo Pioneer
EARNED.`

**Rule B** — Any inertia flag raised AND `First Signal` LOCKED: retract the flag.
`ECHO RETRACTION: {flag-name} on {topic_path} retracted — First Signal LOCKED, no files to
evaluate.`

```
## Echo Detection Table

| topic_path | Rule violated | Flag retracted | Achievement | Resolution |
|------------|---------------|----------------|-------------|------------|
```

If no violations: `| none | — | — | — | — |`.

**Section 3.2–3.4 Gate** — Emit before transferring:

- [ ] Topics in severity order; alphabetical within tier; every topic has
  `Namespace diversity: {N}/9`; all five achievements with exact names; LOCKED rows include
  unlock paths; no trajectory language in Health Phase
- [ ] Inertia Phase table present; no file counts or achievement statuses in Inertia Phase;
  no trajectory claims in Health Phase (cross-contamination check)
- [ ] All three milestone names verbatim with non-empty evidence; proximity ladders for ALL
  NOT YET milestones
- [ ] Nearest-miss present (Level 1, or Level 2 with "Level 1 empty" note), sorted ascending
- [ ] Echo Detection Table emitted; both rules checked; retractions written; "none" if clean

**Analyst Handoff** — Artifacts to Publisher:

1. Inertia Phase table (`topic_path`, `flags`, `trajectory note`, `severity`)
2. Stale signal table and velocity summary
3. Per-topic Health Phase achievement blocks in severity order
4. Team milestone table (3 rows) with proximity ladders for all NOT YET milestones
5. Debate starter proximity line and namespace leader table
6. Nearest-miss table (`topic`, `achievement`, `gap`, `level`)
7. Echo Detection Table with retraction statements (or "none detected")

---

## ROLE 4: PUBLISHER

**Responsibility**: Synthesis, reconciliation, insight, and actions. Works from Ranker and
Analyst output. Does NOT re-scan, re-rank, re-evaluate achievements, or re-assess inertia.

### 4.1 — Confirm Leaderboard

Transcribe the leaderboard from the Ranker Handoff. Do not recompute.

### 4.2 — Cross-Dimensional Reconciliation

Select exactly one observation from the Health Phase and one from the Inertia Phase that
interact. State the interaction. If the Ranker's achievement rate data adds context to the
reconciliation (e.g., the inertia observation involves a contributor whose rate is informative),
include that context in the Interaction column.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase} | {one finding from Inertia Phase} | {how they connect} |
```

### 4.3 — Team Insight

**Skeptic gate**: The Skeptic has read all output from Roles 1–3 and already knows: every
achievement status, every milestone row (with proximity ladder breakdowns), every inertia
flag (including echo-retracted with reasons), every severity tier, every trajectory note,
the stale signal table, the velocity summary, the nearest-miss assessment, the full leaderboard
(with achievement rates), the collaboration signal table, and the reconciliation pairing.
The insight MUST contain something the Skeptic would not already know from all of that.

An insight that restates any achievement, milestone, proximity ladder entry, inertia flag,
achievement rate, velocity, or reconciliation row fails. A passing insight surfaces a
second-order pattern requiring synthesis across health, inertia, and achievement-rate data
that no single block or the reconciliation pairing directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

### 4.4 — Pre-Write Check

Before writing any action:

1. Identify all zero-score conditions. Record explicitly.
2. Identify open inertia flags. Flags retracted in Echo Detection are EXCLUDED — do NOT write
   `resolves:` actions for echo-retracted flags. Record post-retraction flag status.

**prevents: prefix rule** — first of two structurally independent enforcement points: any
action eliminating a zero-score condition carries `prevents:`. Advancement actions do not.

An action resolving an open (non-retracted) inertia flag MUST declare `resolves: {flag-name}`
with the exact name. Other actions leave `resolves:` blank.

### 4.5 — Next Actions

Write at least 3 actions. Each names a specific namespace + topic + exact achievement or
milestone name. `prevents:` rule is the second structurally independent enforcement point.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank]
2. ...
3. ...
```

After all actions (N = actual count of `prevents:`-prefixed actions):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Publisher Gate** — Verify and emit after ACTIONS GATE:

- [ ] Leaderboard transcribed from Ranker (with Achievement Rate column); not recomputed
- [ ] Reconciliation pairing: one Health observation, one Inertia observation, interaction;
  achievement rate context included where applicable
- [ ] Team Insight as one sentence; Skeptic gate verified — Skeptic knew every achievement,
  milestone (with proximity ladders), inertia flag (with echo retractions), velocity,
  nearest-miss, leaderboard (with achievement rates), collaboration, and reconciliation data;
  insight is new cross-dimensional inference not derivable from any single block
- [ ] Pre-write check complete; echo-retracted flags excluded from `resolves:` targeting
- [ ] At least 3 actions; namespace + topic + exact name; `prevents:` at two independent
  locations (4.4 and 4.5); `resolves:` with exact names on non-retracted actions; ACTIONS
  GATE with actual N

---

## V-04 — Milestone Coalition Mapping + 4-Role + Seeds A+B+H+K+M+N+S + Seed W

**Axis**: Lifecycle emphasis + inertia framing
**Hypothesis**: V-04 builds on the R14 V-04 combination (inertia-first, tiered actions, gap
binding) and makes C-32/C-33 universal. New axis: milestone coalition mapping (Seed W). After
each NOT YET milestone's proximity ladder, the Analyst identifies whether the gap is closable
using the existing contributor pool (internal coalition path) or requires recruiting a new
contributor (external path). For `shared coverage`: which existing contributors could add
signals to which deficit topics to close the gap. For `debate starter`: whether any existing
contributor not yet on the nearest topic can contribute there, or whether a new participant is
needed. Coalition mapping supplements proximity ladders by distinguishing "reachable with
current team" from "requires team growth" — a strategic input the Strategist can reference.

---

You are running the **Corps Leaderboard** skill in a 4-role inertia-first pipeline. Execute
each role completely before advancing to the next. No role may perform work assigned to another
role. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: The Analyst (Role 2) runs the Inertia Phase before any health data is
assessed. The Health Phase reports topics in severity order (critical -> warning -> healthy).
Echo detection runs after the Health Phase. The Strategist (Role 3) produces tiered, gap-bound
actions; the Narrator (Role 4) produces synthesis and insight.

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

**Responsibility**: Evaluation only. Runs Inertia Phase (§2.1) first, then Health Phase
(§2.2) with proximity ladders and coalition maps, then Echo Detection (§2.3). Sub-phases
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

Severity tiers:
- `critical` — 2+ non-momentum flags
- `warning` — 1 non-momentum flag
- `healthy` — 0 non-momentum flags

Print inertia table: `topic_path | flags | trajectory note | severity`

Print stale signal table: `topic_path | stale_status`.

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

**Section 2.1 Gate** — Emit before proceeding:

- [ ] Inertia table with severity column; all four flags evaluated; no file counts or
  achievement statuses in Inertia Phase content
- [ ] Stale signal table and velocity summary present

### 2.2 — Health Phase (RUNS SECOND — ordered by severity tier)

Reports current signal state only. Does NOT include trajectory claims or inertia flag
restatements.

**Topic ordering**: critical first, then warning, then healthy. Alphabetical within tier.

For each `topic_path` (in severity order), print:

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9
```

Evaluate all five achievements with exact names. LOCKED rows include unlock paths.

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

For every NOT YET milestone, print both a **Milestone Proximity Ladder** and a
**Coalition Map** immediately following:

**Proximity Ladder format**:
- `first team signal` NOT YET:
  `Proximity ladder: 1 signal file in any namespace for any topic closes this milestone.`
- `shared coverage` NOT YET:
  `Proximity ladder: {N} qualifying topics (need 2 total). Per-topic deficit:
  {topic_A} needs {M} more contributor(s); {topic_B} needs {M} more contributor(s); ...`
- `debate starter` NOT YET:
  `Proximity ladder: nearest is {topic_path} at {N}/3 contributors. {M} more distinct
  contributor signal(s) needed.`

**Coalition Map format** (immediately after the proximity ladder):
- `first team signal` NOT YET:
  `Coalition: any existing contributor can close this — internal path available.`
- `shared coverage` NOT YET: identify which existing contributors appear on fewer topics
  than needed and could bridge the deficit.
  `Coalition: internal path — {contributor_X} could add a signal to {topic_A} to qualify it;
  {contributor_Y} could add a signal to {topic_B}. External path needed if: {condition
  where no existing contributor bridges a particular topic deficit}.`
- `debate starter` NOT YET: identify whether any existing contributor not yet on the nearest
  topic could contribute there.
  `Coalition: internal path — {contributor_X} (currently not on {topic_path}) could contribute
  a signal. External path needed if all existing contributors are already on {topic_path}.`

EARNED milestones do not receive a proximity ladder or coalition map.

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count`.

### 2.3 — Nearest-Miss Assessment

- **Level 1** — every topic 1 unit away from any threshold. Sort ascending.
- **Level 2** — closest 2 units away. ONLY when no Level 1. State "Level 1: no topics are
  1 unit away" first.

Print: `topic | achievement | gap | level`

### 2.4 — Echo Detection

Check every topic for two mutual exclusion rules:

**Rule A** — `healthy-momentum` raised AND `Solo Pioneer` EARNED: retract `healthy-momentum`.
`ECHO RETRACTION: healthy-momentum on {topic_path} retracted — incompatible with Solo Pioneer
EARNED.`

**Rule B** — Any inertia flag raised AND `First Signal` LOCKED: retract the flag.
`ECHO RETRACTION: {flag-name} on {topic_path} retracted — First Signal LOCKED, no files.`

```
## Echo Detection Table

| topic_path | Rule violated | Flag retracted | Achievement | Resolution |
|------------|---------------|----------------|-------------|------------|
```

If no violations: `| none | — | — | — | — |`.

**Section 2.2–2.4 Gate** — Emit before transferring:

- [ ] Topics in severity order; alphabetical within tier; every topic has
  `Namespace diversity: {N}/9`; all five achievements with exact names and unlock paths for
  LOCKED rows; no trajectory language in Health Phase
- [ ] Inertia Phase table present; no file counts or achievement statuses in Inertia Phase;
  no trajectory claims in Health Phase (cross-contamination check: verify absence of
  prohibited content from each phase)
- [ ] All three milestone names verbatim with non-empty evidence; proximity ladders AND
  coalition maps for ALL NOT YET milestones
- [ ] Nearest-miss: Level 1 ascending, or Level 2 with "Level 1 empty" noted first
- [ ] Echo Detection Table emitted; both rules checked; retractions written; "none" if clean

**Analyst Handoff** — Artifacts to Strategist:

1. Inertia Phase table (`topic_path`, `flags`, `trajectory note`, `severity`)
2. Stale signal table and velocity summary
3. Per-topic Health Phase achievement blocks in severity order
4. Team milestone table (3 rows) with proximity ladders and coalition maps for NOT YET
   milestones
5. Debate starter proximity line and namespace leader table
6. Nearest-miss table (`topic`, `achievement`, `gap`, `level`)
7. Echo Detection Table with retraction statements (or "none detected")

---

## ROLE 3: STRATEGIST

**Responsibility**: Actions only. Produces tiered Next Actions list with gap-binding
annotations. Does NOT produce leaderboard, reconciliation, or Team Insight.

### 3.1 — Nearest-Miss Confirmation

Transcribe nearest-miss table from Analyst Handoff. Do not recompute.

### 3.2 — Pre-Write Check

Before writing any action:

1. Identify all zero-score conditions.
2. Identify all open inertia flags from the Analyst's inertia table. Flags retracted in the
   Echo Detection Table are EXCLUDED — do NOT write `resolves:` actions for retracted flags.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action eliminating a zero-score condition carries `prevents:`.

An action resolving an open (non-retracted) inertia flag MUST declare `resolves: {flag-name}`
with exact flag name. Other actions leave `resolves:` blank.

Each action MUST include a `[closes: ...]` annotation:
- Achievement-targeting: `[closes: {achievement} gap of {N} {unit} for {topic_path}]`
- Milestone-targeting: `[closes: {milestone} — {summary from proximity ladder}]`
- No quantifiable gap: `[closes: N/A]`

### 3.3 — Tiered Next Actions

Organize actions by severity tier of the target topic:

**[CRITICAL]** — Actions targeting `critical` severity topics. List first.
If none: `[CRITICAL]: no topics at critical severity.`

**[WARNING]** — Actions targeting `warning` severity topics. List second.
If none: `[WARNING]: no topics at warning severity.`

**[ADVANCING]** — Actions targeting `healthy` topics or team milestones. List last.

`prevents:` rule is the second structurally independent enforcement point for each row.

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

Write at least 3 actions total. After all (N = actual `prevents:`-prefixed count):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Strategist Gate** — Verify and emit after ACTIONS GATE:

- [ ] Nearest-miss confirmation transcribed
- [ ] Pre-write check: zero-score conditions and open (non-retracted) flags recorded;
  echo-retracted flags excluded from `resolves:` targeting
- [ ] Tiered structure: `[CRITICAL]` first, `[WARNING]` second, `[ADVANCING]` last; empty
  tiers noted
- [ ] At least 3 actions; each names namespace + topic + exact name; `prevents:` at two
  independent locations (3.2 and 3.3); `resolves:` with exact flag names on non-retracted
  actions; `[closes: ...]` on every row; ACTIONS GATE with actual N

**Strategist Handoff** — Artifacts to Narrator:

1. Nearest-miss assessment (confirmed from Analyst)
2. Tiered Next Actions list (CRITICAL / WARNING / ADVANCING) with all `prevents:`,
   `resolves:`, and `[closes: ...]` annotations
3. Pre-write check results (with post-retraction flag status)
4. ACTIONS GATE line

---

## ROLE 4: NARRATOR

**Responsibility**: Synthesis only. Produces the Contributor Leaderboard, cross-dimensional
reconciliation, and Team Insight. Does NOT re-scan, re-evaluate, re-assess, or modify actions.

### 4.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical.
If all `unknown`: `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

Print collaboration signal: `topic_path | contributors | collaboration_type` for Team Topic
EARNED topics. Types: `pair` (2), `ensemble` (3+). If none:
`| none | — | no Team Topic earned yet |`.

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

**Skeptic gate**: The Skeptic has read all output from Roles 1–3 — every achievement table,
every milestone row (including proximity ladders and coalition maps for all NOT YET
milestones), every inertia flag (including echo-retracted flags and reasons), every severity
tier, every trajectory note, the stale signal table, the velocity summary, the nearest-miss
assessment, the tiered action list (with `prevents:`, `resolves:`, and `[closes: ...]`),
the leaderboard, the collaboration signal table, and the reconciliation pairing in 4.2.
The insight MUST contain something the Skeptic would not already know from all of that.

An insight that restates any achievement, milestone, proximity ladder entry, coalition map
path, inertia flag, tiered tier grouping, `[closes: ...]` annotation, or reconciliation row
fails. A passing insight surfaces a second-order pattern requiring synthesis across health,
inertia, and coalition data that no single output block or the reconciliation pairing reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

**Narrator Gate** — Verify and emit:

- [ ] Leaderboard with all four columns, ranked descending; collaboration signal table present
- [ ] Reconciliation: one Health observation, one Inertia observation, interaction note
- [ ] Team Insight as one sentence; Skeptic gate verified — Skeptic knew every achievement,
  milestone (with proximity ladders and coalition maps), inertia flag (with echo retractions),
  velocity, nearest-miss, tiered actions (with all annotations), leaderboard, and
  reconciliation data; insight is new cross-dimensional inference beyond all of that

---

## V-05 — Full Integration: 5-Role + All Seeds + Seed X (Falsifiability Contract)

**Axis**: Full integration
**Hypothesis**: V-05 is the ceiling-holding integration variation for R15. The 5-role pipeline:
Archivist -> Assessor -> Inspector -> Strategist -> Narrator. All R14 seeds formalized
(A+B+H+I+K+L+M+N+O+R+S) plus all new R15 seeds (T+U+V+W+X). Seed X is the key new structural
element: the Team Insight appends a two-line falsifiability contract anchoring the insight to
testable boundary conditions — `[holds if: {specific observable condition}]` and `[falsified
by: {specific observable condition}]`. Conditions must name a specific topic, contributor, or
metric threshold; vague conditions ("holds if things continue") fail. The falsifiability
contract raises the bar beyond the confidence band (Seed O) and projection test (Seed L):
where those bound the insight's scope, the contract makes the insight directly falsifiable
by observable future state. The Inspector also runs all three integrity checks: cross-role
discrepancy (Seed I), echo detection (Seed S), and coalition mapping (Seed W).

---

You are running the **Corps Leaderboard** skill in a 5-role inertia-first pipeline. Execute
each role completely before advancing to the next. No role may perform work assigned to another
role. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Pipeline note**: The Assessor (Role 2) establishes severity tiers via the Inertia Phase
before any health data is assessed. The Inspector (Role 3) runs the Health Phase in severity
order with proximity ladders and coalition maps, then runs the cross-role discrepancy check,
echo detection check, and nearest-miss assessment. The Strategist (Role 4) produces tiered,
gap-bound, multi-round actions. The Narrator (Role 5) produces the leaderboard (with velocity,
cohort, and achievement rate columns), reconciliation pairing, and Team Insight with confidence
band, projection test, and falsifiability contract.

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

**Archivist Handoff** — Artifacts to Assessor:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line
3. Contributor index (columns: `contributor`, `topic_path`, `file_count`)

---

## ROLE 2: ASSESSOR

**Responsibility**: Inertia assessment only. Establishes severity tiers for all topics before
any health data is evaluated. Does NOT report file counts, achievement statuses, rank
contributors, write insights, or write actions.

### 2.1 — Inertia Phase

Reports trajectory and momentum only. Does NOT include file counts, achievement statuses, or
coverage totals.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Severity tiers:
- `critical` — 2+ non-momentum flags
- `warning` — 1 non-momentum flag
- `healthy` — 0 non-momentum flags

Print inertia table: `topic_path | flags | trajectory note | severity`

Print stale signal table: `topic_path | stale_status` (`stale` / `active` / `date-unknown`).

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

Classification: > 50% healthy = increasing; < 25% = stalled; otherwise flat.

**Assessor Gate** — Verify and emit:

- [ ] Inertia table with severity column; all four flags evaluated for every topic
- [ ] No file counts, achievement statuses, or coverage totals in Assessor output
- [ ] Stale signal table and velocity summary present

**Assessor Handoff** — Artifacts to Inspector:

1. Registry table (from Archivist)
2. Namespace coverage line (from Archivist)
3. Contributor index (from Archivist)
4. Inertia Phase table (`topic_path`, `flags`, `trajectory note`, `severity`)
5. Stale signal table and velocity summary

---

## ROLE 3: INSPECTOR

**Responsibility**: Health evaluation, proximity ladders, coalition maps, discrepancy check,
echo detection, and nearest-miss assessment. Uses the Assessor's severity tiers to order the
Health Phase. Does NOT rank contributors, write insights, or write actions.

### 3.1 — Health Phase (ordered by Assessor severity tiers)

Reports current signal state only. Does NOT include trajectory claims or inertia flag
restatements.

**Topic ordering**: critical first, then warning, then healthy. Alphabetical within tier.

For each `topic_path` (in severity order):

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9
```

Evaluate all five achievements with exact names. LOCKED rows include unlock paths.

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

For every NOT YET milestone, print a **Milestone Proximity Ladder** followed by a
**Coalition Map** immediately after its table row:

Proximity Ladder:
- `first team signal` NOT YET:
  `Proximity ladder: 1 signal file in any namespace for any topic closes this milestone.`
- `shared coverage` NOT YET:
  `Proximity ladder: {N} qualifying topics (need 2 total). Per-topic deficit:
  {topic_A} needs {M} more contributor(s); {topic_B} needs {M} more contributor(s); ...`
- `debate starter` NOT YET:
  `Proximity ladder: nearest is {topic_path} at {N}/3 contributors. {M} more distinct
  contributor signal(s) needed.`

Coalition Map:
- `first team signal` NOT YET:
  `Coalition: any existing contributor can close this — internal path available.`
- `shared coverage` NOT YET:
  `Coalition: internal path — {contributor_X} could add to {topic_A}; ... External path
  needed if: {condition}.`
- `debate starter` NOT YET:
  `Coalition: internal path — {contributor_X} (not yet on {topic_path}) could contribute.
  External path needed if all current contributors are already on {topic_path}.`

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count`.

### 3.2 — Nearest-Miss Assessment

- **Level 1** — every topic 1 unit away from any threshold. Sort ascending.
- **Level 2** — closest 2 units away. ONLY when no Level 1. State "Level 1: no topics are
  1 unit away" first.

Print: `topic | achievement | gap | level`

### 3.3 — Cross-Role Discrepancy Check

Compare the Assessor's inertia flag assignments against the Inspector's Health Phase findings.
For each topic, verify that the Assessor's flag assignments are consistent with the Health
Phase evidence. Flag any discrepancy where the Assessor assigned a flag that the Health Phase
data does not support (e.g., Assessor assigned `stuck-at-first` but Health Phase shows
Signal Depth EARNED).

```
## Discrepancy Table

| topic_path | Assessor flag | Inspector finding | Discrepancy? | Resolution |
|------------|---------------|-------------------|--------------|------------|
```

For each discrepancy, state: `Assessor flag {flag-name} retracted for {topic_path};
Inspector {finding} contradicts flag condition.`

If no discrepancies: one row `| none | — | — | no | — |`.

### 3.4 — Echo Detection

Check every topic for two mutual exclusion rules:

**Rule A** — `healthy-momentum` raised AND `Solo Pioneer` EARNED: retract `healthy-momentum`.
`ECHO RETRACTION: healthy-momentum on {topic_path} retracted — incompatible with Solo Pioneer
EARNED (Solo Pioneer requires exactly 1 contributor; healthy-momentum requires >= 2).`

**Rule B** — Any inertia flag raised AND `First Signal` LOCKED: retract the flag.
`ECHO RETRACTION: {flag-name} on {topic_path} retracted — First Signal LOCKED, no files to
evaluate; inertia flags require >= 1 file.`

```
## Echo Detection Table

| topic_path | Rule violated | Flag retracted | Achievement | Resolution |
|------------|---------------|----------------|-------------|------------|
```

If no violations: `| none | — | — | — | — |`.

**Inspector Gate** — Verify and emit before transferring:

- [ ] Topics in severity order (critical -> warning -> healthy); alphabetical within tier;
  every topic has `Namespace diversity: {N}/9`; all five achievements with exact names; LOCKED
  rows include unlock paths; no trajectory language in Health Phase
- [ ] Inertia Phase table present; no file counts or achievement statuses in Assessor Inertia
  Phase; no trajectory claims in Inspector Health Phase (cross-contamination check: Health
  Phase contains no trajectory claims; Inertia Phase contains no file-count restatements)
- [ ] All three milestone names verbatim with non-empty evidence; proximity ladders AND
  coalition maps for ALL NOT YET milestones with per-component deficits
- [ ] Nearest-miss: Level 1 ascending, or Level 2 with "Level 1 empty" noted first
- [ ] Discrepancy Table emitted; all Assessor flags compared to Inspector findings; retraction
  statements written for any discrepancies
- [ ] Echo Detection Table emitted; both Rule A and Rule B checked for every topic; retraction
  statements written; "none" if clean

**Inspector Handoff** — Artifacts to Strategist:

1. Assessor's Inertia Phase table (`topic_path`, `flags`, `trajectory note`, `severity`)
2. Assessor's stale signal table and velocity summary
3. Per-topic Health Phase achievement blocks in severity order
4. Team milestone table (3 rows) with proximity ladders and coalition maps for NOT YET rows
5. Debate starter proximity line and namespace leader table
6. Nearest-miss table (`topic`, `achievement`, `gap`, `level`)
7. Discrepancy Table with retraction statements (or "none detected")
8. Echo Detection Table with retraction statements (or "none detected")

---

## ROLE 4: STRATEGIST

**Responsibility**: Actions only. Produces multi-round, tiered Next Actions with gap-binding.
Does NOT produce leaderboard, reconciliation, or Team Insight.

### 4.1 — Nearest-Miss Confirmation

Transcribe nearest-miss table from Inspector Handoff. Do not recompute.

### 4.2 — Pre-Write Check

Before writing any action:

1. Identify all zero-score conditions. Record explicitly.
2. Identify all open inertia flags from the Assessor's inertia table. Flags retracted in
   either the Discrepancy Table or the Echo Detection Table are EXCLUDED — do NOT write
   `resolves:` actions for retracted or discrepancy-corrected flags. Record post-retraction,
   post-correction flag status for every topic.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action eliminating a zero-score condition carries `prevents:`.

An action resolving an open (non-retracted, non-corrected) inertia flag MUST declare
`resolves: {flag-name}` with the exact flag name. Other actions leave `resolves:` blank.

Each action MUST include a `[closes: ...]` annotation:
- Achievement-targeting: `[closes: {achievement} gap of {N} {unit} for {topic_path}]`
- Milestone-targeting: `[closes: {milestone} — {summary from proximity ladder}]`
- No quantifiable gap: `[closes: N/A]`

### 4.3 — Multi-Round Tiered Next Actions

Group actions by BOTH round (gap distance) AND severity tier:

**Round assignment**:
- Round 1 — gap is exactly 1 signal (1 contribution closes it)
- Round 2 — gap is 2-3 signals
- Round 3 — gap is 4+ signals or requires multi-contributor coordination

**Tier ordering within each round**: CRITICAL topics first, then WARNING, then ADVANCING.

`prevents:` rule is the second structurally independent enforcement point per row.

```
## Next Actions

### Round 1 — Immediate (1 signal closes the gap)
#### [CRITICAL]
1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag or blank}] [closes: {gap}]
#### [WARNING]
N. ...
#### [ADVANCING]
N. ...

### Round 2 — Sprint (2-3 signals needed)
#### [CRITICAL]
...
#### [WARNING]
...
#### [ADVANCING]
...

### Round 3 — Strategic (4+ signals or coordination required)
#### [CRITICAL]
...
#### [WARNING]
...
#### [ADVANCING]
...
```

Write at least 3 actions total. Empty round/tier combinations: state
`[No Round {N} / {tier} actions]`. After all actions:

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Strategist Gate** — Verify and emit after ACTIONS GATE:

- [ ] Nearest-miss confirmation transcribed from Inspector Handoff
- [ ] Pre-write check: zero-score conditions and open (non-retracted, non-corrected) flags
  identified; retracted and discrepancy-corrected flags excluded from `resolves:` targeting
- [ ] Actions grouped by round (1/2/3) with tier ordering (CRITICAL/WARNING/ADVANCING) within
  each round; empty combinations noted; at least 3 total actions
- [ ] Each action: namespace + topic + exact name; `prevents:` at two independent locations
  (4.2 and 4.3); `resolves:` with exact flag names; `[closes: ...]` on every row
- [ ] ACTIONS GATE line with actual N count

**Strategist Handoff** — Artifacts to Narrator:

1. Nearest-miss assessment (confirmed from Inspector)
2. Multi-round tiered Next Actions list with all `prevents:`, `resolves:`, and `[closes: ...]`
3. Pre-write check results (with post-retraction, post-correction flag status)
4. ACTIONS GATE line

---

## ROLE 5: NARRATOR

**Responsibility**: Synthesis only. Produces the Contributor Leaderboard (with velocity, cohort,
and achievement rate columns), collaboration signal, cross-dimensional reconciliation, and
Team Insight (with confidence band, projection test, and falsifiability contract). Does NOT
re-scan, re-evaluate, re-assess, or modify actions.

### 5.1 — Contributor Leaderboard (Multi-Column)

Rank contributors descending by total signal count. Ties: alphabetical.

For each contributor, compute:
- `velocity` — cross-reference against the stale signal table: `rising` if the contributor
  has active (non-stale) signals added recently; `stalled` if all the contributor's signals
  are stale; `steady` if a mix; `unknown` if modification dates are not available.
- `cohort` — `specialist` if >= 50% signals in one namespace; `generalist` if signals span
  >= 3 distinct namespaces; `focused` otherwise (2 namespaces).
- `achievement_rate` — achievements earned across all contributor's topics / total signal
  files, rounded to 2 decimal places. If total_signals = 0: `N/A`.

If all `unknown`: `| 1 | no contributor metadata found | — | — | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered | Velocity | Cohort | Achievement Rate |
|------|-------------|---------------|----------------|----------|--------|-----------------|
```

Print collaboration signal: `topic_path | contributors | collaboration_type`.
Types: `pair` (2), `ensemble` (3+). If none: `| none | — | no Team Topic earned yet |`.

### 5.2 — Cross-Dimensional Reconciliation

Select exactly one observation from the Inspector's Health Phase and one from the Assessor's
Inertia Phase that interact. If the Discrepancy or Echo Detection checks retracted any flags,
the inertia observation MUST come from a non-retracted, non-corrected flag or trajectory note.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase} | {one finding from Inertia Phase, non-retracted} | {how they connect} |
```

### 5.3 — Team Insight

**Skeptic gate**: The Skeptic has read all output from Roles 1–4 and already knows: every
achievement status (including tension markers), every milestone row (including proximity
ladders and coalition maps for all NOT YET milestones), every inertia flag (including
discrepancy-retracted and echo-retracted flags with their retraction reasons), every severity
tier, every trajectory note, the stale signal table, the velocity summary, the nearest-miss
assessment, the full multi-round tiered action list (with `prevents:`, `resolves:`, and
`[closes: ...]`), the leaderboard (with velocity, cohort, and achievement rate), the
collaboration signal table, and the reconciliation pairing in 5.2. The insight MUST contain
something the Skeptic would not already know from all of that.

An insight that restates any achievement, milestone status, proximity ladder entry, coalition
map path, inertia flag (retracted or active), echo retraction, velocity, cohort label,
achievement rate, tiered action grouping, `[closes: ...]` annotation, or reconciliation row
fails. A passing insight surfaces a second-order pattern requiring synthesis across health,
inertia, velocity, cohort, and coalition data in a way no single output block or the
reconciliation pairing directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

Then append the confidence band on a new line:
`[confidence: HIGH/MEDIUM/LOW] [supporting observations: {N}]`

Assign: HIGH = 3+ independent observations from both health and inertia data; MEDIUM = 2;
LOW = 1 or single-data-point inference. Substitute actual count for {N}.

Then append the projection test on a new line:
`[scope: anchored — applies to observed topics only / extrapolated — extends beyond observed
topics; extrapolation basis: {evidence}]`

Then append the falsifiability contract on the next two lines:
`[holds if: {specific observable condition naming a topic, contributor, or metric threshold}]`
`[falsified by: {specific observable condition that would invalidate the insight}]`

Both contract conditions must name a specific topic, contributor, or metric threshold.
Vague conditions ("holds if the trend continues" or "falsified by any data change") fail.

**Narrator Gate** — Verify and emit:

- [ ] Leaderboard with all seven columns (Rank, Contributor, Total Signals, Topics Covered,
  Velocity, Cohort, Achievement Rate), ranked descending; velocity/cohort/rate computed per
  definition; collaboration signal table present
- [ ] Reconciliation: one Health observation, one non-retracted Inertia observation,
  interaction note
- [ ] Team Insight as one sentence; Skeptic gate verified — Skeptic knew every achievement
  (with tension markers), milestone (with proximity ladders and coalition maps, including all
  NOT YET per-component deficits), inertia flag (including discrepancy-retracted and
  echo-retracted with reasons), severity tier, trajectory note, stale signal, velocity
  summary, nearest-miss, multi-round tiered actions (all annotations), leaderboard (all
  columns), collaboration, and reconciliation data; insight is new cross-dimensional inference
  not derivable from any single block, any proximity ladder, any coalition map, any
  retraction, or the reconciliation pairing
- [ ] Confidence band on next line with HIGH/MEDIUM/LOW and actual observation count N
- [ ] Projection test on next line with scope declaration (anchored / extrapolated + basis)
- [ ] Falsifiability contract on next two lines: `[holds if: ...]` and `[falsified by: ...]`;
  both conditions name a specific topic, contributor, or metric threshold (not vague)
