Now I have everything I need. Let me write the complete R16 variate document.

---

# Variate R16 — corps-leaderboard

```
skill: quest-variate
skill_target: corps-leaderboard
round: 16
date: 2026-03-17
rubric_version: 13
```

**R15 ceiling against v12**: All 5 variations scored 25/25 = 100.00. Seed N (milestone proximity ladders, C-32) and Seed S (echo detection, C-33) were universalized across all variations. New seeds T+U+V+W+X were introduced.

**R15 seeds entering R16** (carry universally):
- Seed A: `resolves: {flag-name}` on inertia-flag-resolving actions
- Seed B: Pre-synthesis cross-dimensional reconciliation pairing
- Seed H: Severity-ordered health topic reporting (critical → warning → healthy)
- Seed N: Milestone proximity ladder — per-precondition breakdown for NOT YET milestones
- Seed S: Echo detection — flag/achievement logical consistency scan with echo table and retraction statements

**R15 seeds entering R16** (carry selectively):
- Seed K: Tiered action output (`[CRITICAL]` / `[WARNING]` / `[ADVANCING]`) — carry in V-04, V-05
- Seed M: Action-to-gap binding (`[closes: {achievement} gap of {N} {unit} for {topic}]`) — carry in V-04, V-05
- Seed T: Achievement rate column (`rate = achievements / signals`) — carry in V-03, V-05
- Seed U: Contributor cohort classification (`specialist` / `generalist` / `focused`) — carry in V-01, V-05
- Seed V: Multi-round action sequencing (Round 1 / Round 2 / Round 3 by gap distance) — carry in V-02, V-05
- Seed W: Milestone coalition mapping (internal vs. external contributor path) — carry in V-04, V-05
- Seed X: Insight falsifiability contract (`[holds if:] [falsified by:]`) — carry in V-05

**New seeds introduced in R16**:
- **Seed Y**: Flag lifecycle annotation — each inertia flag in the Inertia Phase is tagged with a lifecycle status: `new` (flag raised; no prior-run baseline, or flag absent in baseline), `persistent` (flag present in prior-run baseline and still raised), or `resolved` (flag present in prior-run baseline, now gone). If no baseline file exists at `simulations/.leaderboard-baseline.md`, all flags receive `new`. A dedicated role or sub-phase produces the lifecycle column; the action-writing phase uses lifecycle status to prioritize `persistent` flags (they resisted one cycle) over `new` flags.
- **Seed Z**: Achievement co-occurrence matrix — after evaluating per-topic achievements, produce a 5×5 symmetric count table showing how often each achievement pair co-occurs on the same topic (diagonal = times each achievement is earned solo). Reveals structural coupling: if `First Signal + Solo Pioneer` always co-occur, the team is predominantly making solo starts.
- **Seed AA**: Namespace gap debt column — in the contributor leaderboard, add `gap_debt = 9 − (distinct contributor namespaces)`. A contributor active in 3 namespaces has `gap_debt = 6`, signaling 6 unexplored namespaces. Derived from the Archivist's contributor index.
- **Seed AB**: Milestone regression risk — for each EARNED milestone, compute whether any single contributor removal would cause the milestone to un-earn. Print a regression risk row: `milestone | earned | regression risk | at-risk contributor`. A milestone where no single removal would cause regression is `stable`; one where a specific contributor's absence would un-earn it is `fragile: {contributor}`.
- **Seed AC**: Contributor onboarding path — for every topic where `Solo Pioneer` is EARNED and `Team Topic` is NOT YET, produce a one-line onboarding prompt naming: (1) the topic, (2) the current sole contributor, (3) the exact namespace + signal type that would be the fastest unlock for `Team Topic`. Format: `Topic {path}: {contributor} holds solo. Fastest Team Topic unlock: 1 file in {namespace} from any new contributor.`

**R16 design targets**:
- All 5 variations carry Seeds A+B+H+N+S universally.
- V-01: Phrasing register (narrative briefing style). 3-role. Seeds A+B+H+N+S. New: Seed AA + Seed U (cohort). Expected: 25/25 → 100.00.
- V-02: Output format (structured schema blocks). 3-role. Seeds A+B+H+N+S+V. New: Seed Z. Expected: 25/25 → 100.00.
- V-03: Role sequence (4-role with dedicated Reconciler). Seeds A+B+H+N+S+T. New: Seed Y. Expected: 25/25 → 100.00.
- V-04: Combination (tiered actions + coalition + regression risk). 4-role. Seeds A+B+H+K+M+N+S+W. New: Seed AB. Expected: 25/25 → 100.00.
- V-05: Full integration (5-role + Seeds A+B+H+K+M+N+S+T+U+V+W+X + new Y+Z+AA+AB+AC). Expected: 25/25 → 100.00.

**Expected scoring against v12** (formula: `90 + (passed/25) × 10`):
- V-01 through V-05: 25/25 → **100.00**

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Phrasing register (narrative briefing blocks) + Seed AA (gap_debt) + Seed U (cohort) | V-01 |
| Output format (structured schema `::blocks::`) + Seed V (multi-round) + Seed Z (co-occurrence matrix) | V-02 |
| Role sequence (4-role + Reconciler between Analyst and Publisher) + Seed T (rate) + Seed Y (flag lifecycle) | V-03 |
| Combination: tiered actions + coalition mapping + Seed AB (milestone regression risk) + Seeds K+M+W | V-04 |
| Full integration: 5-role + all R15+R16 seeds | V-05 |

---

## V-01 — Narrative Briefing Register + Namespace Gap Debt + 3-Role + Seeds A+B+H+N+S + Seeds U+AA

**Axis**: Phrasing register
**Hypothesis**: R15 V-01 used "field-report prose blocks" — a documentary, form-filling register. This variation shifts to a **narrative briefing** register: each health block reads as a briefing note to a stakeholder ("Topic X is raising a concern — it has only 1 file and a single contributor, with no namespace diversity"). The hypothesis is that briefing language prompts higher-quality prose synthesis and surfaces the editorial voice earlier, while the same structural fields (achievements, milestones, proximity ladders) still satisfy all rubric criteria. New axis element: `gap_debt` column in leaderboard (Seed AA) changes team interpretation — a top contributor with `gap_debt = 7` signals breadth opportunity alongside their depth ranking. Seed U (cohort) retained from R15.

---

You are running the **Corps Leaderboard** skill in a 3-role pipeline. Execute each role completely before advancing. No role may perform work assigned to another. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: Within the Analyst role, the Inertia Phase (§2.1) runs BEFORE the Health Phase (§2.2). After the Inertia Phase assigns severity tiers, the Health Phase reports topics in descending severity order: critical first, then warning, then healthy. Within each tier, sort alphabetically by `topic_path`. A flat alphabetical ordering across all topics, ignoring severity, fails.

---

### ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. The Archivist scans the workspace, builds the signal registry, and constructs the contributor index. The Archivist does NOT evaluate achievements, assess trajectory, rank contributors, or write insights or actions.

#### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path segment after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path` (e.g., `scout`)
- `contributor` — resolve in priority order: frontmatter `author:` > frontmatter `contributor:` > filename prefix before first `-` > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write `REGISTRY: empty — no signal files found in simulations/` and stop. Roles 2 and 3 do not run.

Print registry as table: `topic_path | namespace | contributor | file`

After the registry, print namespace coverage:
`Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`

The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

#### 1.2 — Contributor Index

Build a contributor-to-topics index. For each contributor, record: `contributor | distinct_namespaces | topic_paths | file_count`. The `distinct_namespaces` count is the number of unique namespaces across all of this contributor's signal files — used by the Publisher to compute `gap_debt`.

**Archivist Gate**:

- [ ] Registry table printed with all four columns (`topic_path`, `namespace`, `contributor`, `file`)
- [ ] Namespace coverage line printed with active and empty namespace lists
- [ ] Contributor index printed with `distinct_namespaces` column populated for every contributor

**Archivist Handoff** — artifacts transferred to the Analyst:

1. Signal registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line (active and empty namespace lists)
3. Contributor index (columns: `contributor`, `distinct_namespaces`, `topic_paths`, `file_count`)

---

### ROLE 2: ANALYST

**Responsibility**: Evaluation only. The Analyst first establishes trajectory (§2.1 Inertia Phase), then reports current signal state in narrative briefing form (§2.2 Health Phase in severity order), then runs the Echo Detection scan (§2.4), then computes the Nearest-Miss Assessment (§2.3). The two sub-phases are structurally separated: Inertia Phase content must not appear in Health Phase briefing notes and vice versa. The Analyst does NOT rank contributors, write insights, or write actions.

#### 2.1 — Inertia Phase (RUNS FIRST)

Reports trajectory and momentum only. Does NOT include file counts, achievement statuses, or coverage totals — those are current-state data belonging to the Health Phase.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|---|---|
| `stuck-at-first` | exactly 1 file; Signal Depth not earned |
| `solo-hold` | exactly 1 contributor; no second contributor present |
| `namespace-thin` | all files in 1 namespace; Full Sweep not earned |
| `healthy-momentum` | Signal Depth earned AND >= 2 distinct contributors |

Assign a severity tier per topic:
- `critical` — 2 or more non-momentum flags raised
- `warning` — exactly 1 non-momentum flag raised
- `healthy` — 0 non-momentum flags, or only `healthy-momentum`

Print inertia table: `topic_path | flags | trajectory note | severity`

Print stale signal table: `topic_path | stale_status` (`stale` / `active` / `date-unknown` using file modification dates where accessible).

Print velocity summary:
`Signal velocity: {N_signals} signals / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`
Classification: > 50% topics healthy = increasing; < 25% = stalled; otherwise flat.

**Section 2.1 Gate** — emit before proceeding to Section 2.2:

- [ ] Inertia table present with severity column; every topic evaluated for all four flags
- [ ] No static file counts, achievement statuses, or coverage totals in Inertia Phase content
- [ ] Stale signal table and velocity summary present

#### 2.2 — Health Phase (RUNS SECOND — narrative briefing, severity order: critical → warning → healthy)

Reports current signal state only. Does NOT include trajectory claims, momentum language, or inertia flag restatements — those belong to the Inertia Phase.

**Topic ordering**: critical first, then warning, then healthy. Alphabetical within each tier.

For each `topic_path` (in severity order), write a **narrative briefing block** in this form:

```
### Briefing: {topic_path} [severity: {critical/warning/healthy}]
Status: {N} signal(s) across {M} namespace(s). Contributors: {list}. Namespace diversity: {N}/9.

{1–3 sentences describing the topic's signal state in editorial tone — what exists, 
what is missing, what the team has and has not done. Do NOT mention flags or trajectory.}

Achievements:
  - First Signal: {EARNED — {evidence}} / {LOCKED — needs at least 1 file}
  - Signal Depth: {EARNED — {evidence}} / {LOCKED — needs {X} more file(s) to reach 3}
  - Full Sweep: {EARNED — {evidence}} / {LOCKED — needs signals in {X} more namespace(s)}
  - Solo Pioneer: {EARNED — {evidence}} / {LOCKED — needs exactly 1 contributor with >= 1 file}
  - Team Topic: {EARNED — {evidence}} / {LOCKED — needs {X} more contributor(s) each with >= 1 file}
```

Achievement names must be exact — paraphrasing ("Team Coverage" for "Team Topic") fails. Every LOCKED achievement states the specific unlock requirement inline.

When `Solo Pioneer` is EARNED and `Team Topic` is NOT YET, append:
`[TENSION: solo hold — 1 additional contributor with >= 1 signal unlocks Team Topic]`

After all topic briefing blocks, evaluate all three team milestones using exact names:

| Milestone | Earned when |
|---|---|
| `first team signal` | any file exists in workspace |
| `shared coverage` | >= 2 topics each with >= 2 distinct contributors |
| `debate starter` | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

For every NOT YET milestone, print a **Milestone Proximity Ladder** immediately below its row:

- `first team signal` NOT YET: `Proximity ladder: 1 signal file in any namespace for any topic closes this milestone.`
- `shared coverage` NOT YET: `Proximity ladder: {N} qualifying topics found (need 2). Per-topic contributor deficit: {topic_A} needs {M} more contributor(s); {topic_B} needs {M} more contributor(s). [list all candidate topics individually]`
- `debate starter` NOT YET: `Proximity ladder: nearest topic is {path} at {N}/3 contributors. {M} more distinct contributor signal(s) close this gap.`

EARNED milestones do not receive a proximity ladder.

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count` for each active namespace.

#### 2.3 — Nearest-Miss Assessment

**Level 1 candidates** — every topic exactly 1 unit away from any achievement threshold. For each: topic name, achievement name, numeric gap. Sort ascending by gap.

**Level 2 fallback** — closest topic 2 units away. Report Level 2 ONLY when no Level 1 candidate exists for a given achievement type. State `Level 1: no topics are 1 unit away` explicitly before listing Level 2.

Print: `topic | achievement | gap | level`

#### 2.4 — Echo Detection (Logical Consistency Scan)

After completing §2.2 and §2.3, check every topic for logical mutual exclusion violations:

**Rule A** — `healthy-momentum` flag raised AND `Solo Pioneer` EARNED:
`healthy-momentum` requires >= 2 contributors; `Solo Pioneer` requires exactly 1. Both cannot be simultaneously true. Retract `healthy-momentum` and emit:
`ECHO RETRACTION: healthy-momentum on {topic_path} retracted — incompatible with Solo Pioneer EARNED (Solo Pioneer requires exactly 1 contributor).`

**Rule B** — Any inertia flag raised AND `First Signal` LOCKED (0 files):
Inertia flags evaluate signal properties requiring at least 1 file. Zero-file topics have no evaluable signals. Retract the flag and emit:
`ECHO RETRACTION: {flag-name} on {topic_path} retracted — First Signal is LOCKED; no files to evaluate; inertia flags require >= 1 file.`

Produce an echo table:

```
## Echo Detection Table
| topic_path | Rule violated | Flag retracted | Achievement | Resolution |
|---|---|---|---|---|
```

If no violations: one row `| none | — | — | — | — |`.

**Section 2.2–2.4 Gate** — emit before transferring artifacts:

- [ ] Topics in severity order (critical → warning → healthy); alphabetical within tier
- [ ] Every briefing block includes: Status line with namespace diversity {N}/9; all five achievement names exact and bold; LOCKED achievements include inline unlock requirements; EARNED achievements state evidence; no trajectory language or flag names in briefing prose
- [ ] Contamination check: Health Phase briefing blocks contain no trajectory claims, momentum notes, or inertia flag restatements; Inertia Phase table contains no file counts or achievement statuses
- [ ] All three milestone names verbatim with non-empty evidence; proximity ladders present for ALL NOT YET milestones with per-topic deficit breakdowns
- [ ] Nearest-miss present (Level 1 ascending; Level 2 only when Level 1 absent, with explicit "Level 1: no topics are 1 unit away" statement)
- [ ] Echo Detection Table emitted; Rule A and Rule B checked for every topic; retraction statements for each violation; "none detected" row if clean

**Analyst Handoff** — artifacts transferred to the Publisher:

1. Inertia Phase table (`topic_path`, `flags`, `trajectory note`, `severity`)
2. Stale signal table and velocity summary
3. Per-topic Health Phase briefing blocks in severity order
4. Team milestone table (3 rows) with proximity ladders for all NOT YET milestones
5. Debate starter proximity line and namespace leader table
6. Nearest-miss assessment table (`topic`, `achievement`, `gap`, `level`)
7. Echo Detection Table with retraction statements (or "none detected")

---

### ROLE 3: PUBLISHER

**Responsibility**: Synthesis and output. Works from all prior artifacts. Does NOT re-scan the workspace, re-evaluate achievements, or re-run echo detection.

#### 3.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical.

Compute per contributor:
- `cohort`: `specialist` if >= 50% of signals in 1 namespace; `generalist` if signals span >= 3 namespaces; `focused` if exactly 2 namespaces
- `gap_debt`: `9 − distinct_namespaces` (from Archivist's contributor index). A contributor active in 4 namespaces has `gap_debt = 5`.

If all contributors are `unknown`: one row `| 1 | no contributor metadata found | — | — | — | — |`.

Print leaderboard: `rank | contributor | signals | topics | cohort | gap_debt`

After the leaderboard:
- `Namespace leader: {contributor} leads {namespace} with {N} signals` (repeat per active namespace)
- `Solo Pioneer tension: [for each topic where Solo Pioneer EARNED and Team Topic NOT YET] topic {path} — {contributor} holds solo; 1 new contributor with >= 1 signal unlocks Team Topic`
- `Collaboration signal: {N} topic(s) have multi-contributor coverage | Highest: {topic} with {N} contributors`

#### 3.2 — Cross-Dimensional Reconciliation

Select exactly one observation from the Health Phase briefing blocks and one from the Inertia Phase table that interact. State the interaction.

```
## Reconciliation
| Health observation | Inertia observation | Interaction |
|---|---|---|
| {finding from Health Phase} | {finding from Inertia Phase} | {how they connect} |
```

#### 3.3 — Team Insight

**Skeptic gate**: A Skeptic who has read all prior output already knows: every achievement status (from briefing blocks), every milestone row (including all per-topic deficit breakdowns in proximity ladders), every inertia flag (including echo-retracted flags and their retraction reasons), every severity tier, every trajectory note, the stale signal table, the velocity summary, the nearest-miss assessment (Level 1 and Level 2), every cohort label, every `gap_debt` value, the collaboration signal table, and the reconciliation pairing. An insight that restates any of these fails. A passing insight surfaces a second-order pattern — a risk, convergence, or cross-topic trajectory inference — not derivable from any single block, any proximity ladder entry, or the reconciliation pairing.

Write one Team Insight sentence containing: (1) a cross-topic conclusion, (2) a concrete number, (3) a specific contributor or topic name.

#### 3.4 — Pre-Write Check

Before writing any action:
1. Identify all zero-score conditions: topics with 0 files, empty registry, empty leaderboard.
2. List all open inertia flags from the Inertia Phase table. Flags retracted in the Echo Detection Table are EXCLUDED — do NOT write `resolves:` actions targeting echo-retracted flags.

**prevents: prefix rule** (first of two independent enforcement points): any action whose primary purpose is eliminating a zero-score condition carries the `prevents:` prefix. Advancement actions do not.

An action resolving an open (non-retracted) inertia flag MUST declare `resolves: {exact-flag-name}` (`stuck-at-first`, `solo-hold`, or `namespace-thin`). Actions not resolving a flag leave `resolves:` blank.

#### 3.5 — Next Actions

Write at least 3 recommended actions. Each must name: (1) a specific namespace and topic path, (2) the exact achievement or milestone name it unlocks.

The **prevents: prefix rule** (second independent enforcement point): embed in each action row — an action targeting a zero-score condition carries `prevents:`, all others do not.

```
## Next Actions

1. [prevents: or omit] `{namespace}/{topic}` → unlocks **{exact achievement or milestone name}** [resolves: {flag-name} or omit]
2. ...
3. ...
```

After all actions, emit exactly (N = actual count of `prevents:`-prefixed actions written):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Publisher Gate**:

- [ ] Leaderboard present ranked descending; all six columns present (`rank`, `contributor`, `signals`, `topics`, `cohort`, `gap_debt`); cohort label and gap_debt value assigned per definition
- [ ] Namespace leader callout, solo pioneer tension, and collaboration signal lines present
- [ ] Reconciliation pairing: one Health briefing observation, one Inertia observation, interaction stated
- [ ] Team Insight as one sentence; Skeptic gate verified — insight is a new cross-dimensional inference not derivable from any briefing block, proximity ladder, echo retraction, or reconciliation row; contains a concrete number and a specific name
- [ ] Pre-write check complete; zero-score conditions and open (non-retracted) flags identified; echo-retracted flags excluded from `resolves:` targeting
- [ ] At least 3 actions; each names namespace + topic + exact achievement or milestone; `prevents:` at two independent enforcement points (§3.4 pre-write check and §3.5 action template); `resolves:` with exact flag names on non-retracted flag-resolving actions
- [ ] ACTIONS GATE line written with actual N substituted

---

## V-02 — Structured Schema Blocks + Achievement Co-Occurrence Matrix + 3-Role + Seeds A+B+H+N+S+V + Seed Z

**Axis**: Output format
**Hypothesis**: R15 V-02 used multi-round temporal action sequencing as the output format variation. This variation changes the output format at a more fundamental level: each phase emits **structured schema blocks** using explicit `::SCHEMA::` / `::END::` delimiters with named `key: value` fields, rather than prose paragraphs or markdown tables. The hypothesis is that schema-block format forces completeness (every declared field must be populated) and prevents omission by making missing fields visible. The new axis element is Seed Z (achievement co-occurrence matrix): a 5×5 symmetric count table emitted after the per-topic achievement table, revealing structural coupling between achievement types. Multi-round action sequencing from R15 V-02 (Seed V) is retained as the action-grouping structure.

---

You are running the **Corps Leaderboard** skill in a 3-role pipeline. Execute each role completely before advancing. No role may perform work assigned to another. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: Within the Analyst role, the Inertia Phase (§2.1) runs BEFORE the Health Phase (§2.2). The Health Phase reports topics in descending inertia severity order: critical first, then warning, then healthy. Within each tier, sort alphabetically. Each phase emits structured schema blocks — do not substitute free prose where a schema block is specified.

---

### ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Scans workspace, builds signal registry, constructs contributor index. Does NOT evaluate achievements, assess trajectory, rank contributors, or write insights or actions.

#### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path segment after `simulations/`
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-` > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, emit:
```
::REGISTRY::
status: empty
reason: no signal files found in simulations/
::END::
```
Roles 2 and 3 do not run.

Otherwise, emit a registry schema block for every matching file:

```
::REGISTRY_ENTRY::
topic_path: {value}
namespace: {value}
contributor: {value}
file: {value}
::END::
```

After all registry entries, emit:

```
::NAMESPACE_COVERAGE::
active_count: {N}
total: 9
active: {comma-separated list}
empty: {comma-separated list}
::END::
```

The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

#### 1.2 — Contributor Index

Emit one schema block per contributor:

```
::CONTRIBUTOR_ENTRY::
contributor: {value}
distinct_namespaces: {N}
file_count: {N}
topic_paths: {comma-separated list}
::END::
```

**Archivist Gate**:

- [ ] `::REGISTRY_ENTRY::` blocks present for every matching file (or `::REGISTRY:: status: empty` block)
- [ ] `::NAMESPACE_COVERAGE::` block present with `active`, `empty`, `active_count` fields
- [ ] `::CONTRIBUTOR_ENTRY::` blocks present with all four fields

**Archivist Handoff** — artifacts transferred to the Analyst:

1. All `::REGISTRY_ENTRY::` blocks
2. `::NAMESPACE_COVERAGE::` block
3. All `::CONTRIBUTOR_ENTRY::` blocks

---

### ROLE 2: ANALYST

**Responsibility**: Evaluation only. Runs Inertia Phase (§2.1) first, then Health Phase (§2.2) in severity order, then Nearest-Miss Assessment (§2.3), then Echo Detection (§2.4), then Co-Occurrence Matrix (§2.5). Structurally separated — Inertia Phase fields must not appear in Health Phase blocks and vice versa. Does NOT rank contributors, write insights, or write actions.

#### 2.1 — Inertia Phase (RUNS FIRST)

Reports trajectory and momentum only. No file counts, achievement statuses, or coverage totals.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|---|---|
| `stuck-at-first` | exactly 1 file; Signal Depth not earned |
| `solo-hold` | exactly 1 contributor; no second contributor present |
| `namespace-thin` | all files in 1 namespace; Full Sweep not earned |
| `healthy-momentum` | Signal Depth earned AND >= 2 distinct contributors |

Severity: `critical` = 2+ non-momentum flags; `warning` = 1 non-momentum flag; `healthy` = 0.

Emit one schema block per topic:

```
::INERTIA::
topic_path: {value}
flags: {comma-separated flag names, or "none"}
trajectory_note: {one-line momentum description}
severity: {critical/warning/healthy}
::END::
```

Emit one stale signal block per topic:

```
::STALE_CHECK::
topic_path: {value}
stale_status: {stale/active/date-unknown}
::END::
```

Emit velocity summary:

```
::VELOCITY::
signal_count: {N}
topic_count: {N}
healthy_topics: {N}
warning_topics: {N}
critical_topics: {N}
trend: {increasing/flat/stalled}
trend_rule: "> 50% healthy = increasing; < 25% = stalled; otherwise flat"
::END::
```

**Section 2.1 Gate** — emit before proceeding:

- [ ] `::INERTIA::` block present for every topic with all four fields
- [ ] No file counts, achievement statuses, or coverage totals in any `::INERTIA::` block
- [ ] All `::STALE_CHECK::` blocks and `::VELOCITY::` block present

#### 2.2 — Health Phase (RUNS SECOND — ordered by severity: critical → warning → healthy)

Reports current signal state only. No trajectory claims, momentum language, or inertia flag restatements.

For each `topic_path` in severity order (alphabetical within tier), emit:

```
::HEALTH::
topic_path: {value}
severity: {critical/warning/healthy}
file_count: {N}
namespaces: {comma-separated list}
contributors: {comma-separated list}
namespace_diversity: {N}/9
first_signal: {EARNED: {evidence} | LOCKED: needs >= 1 file}
signal_depth: {EARNED: {evidence} | LOCKED: needs {X} more file(s) to reach 3}
full_sweep: {EARNED: {evidence} | LOCKED: needs {X} more namespace(s) to reach 3}
solo_pioneer: {EARNED: {evidence} | LOCKED: needs exactly 1 contributor with >= 1 file}
team_topic: {EARNED: {evidence} | LOCKED: needs {X} more contributor(s) each with >= 1 file}
solo_tension: {YES: 1 additional contributor with >= 1 file unlocks Team Topic | NO}
::END::
```

Every field must be populated. `LOCKED` entries must include the specific unlock requirement. `EARNED` entries must include evidence. `solo_tension: YES` only when Solo Pioneer EARNED and Team Topic NOT YET.

After all `::HEALTH::` blocks, emit the team milestone table. Exact milestone names required:

```
::MILESTONE::
name: first team signal
status: {EARNED/NOT YET}
evidence: {non-empty value}
::END::

::MILESTONE::
name: shared coverage
status: {EARNED/NOT YET}
evidence: {non-empty value}
::END::

::MILESTONE::
name: debate starter
status: {EARNED/NOT YET}
evidence: {non-empty value}
::END::
```

For every NOT YET milestone, emit a proximity ladder block immediately after its `::MILESTONE::` block:

```
::PROXIMITY_LADDER::
milestone: {exact milestone name}
aggregate_gap: {description}
per_component:
  - {topic_or_contributor}: needs {M} {unit}
  - {topic_or_contributor}: needs {M} {unit}
  [list every candidate individually]
::END::
```

Every NOT YET milestone must have a proximity ladder. An aggregate gap without per-component breakdown fails.

Emit:
```
::DEBATE_PROXIMITY::
nearest_topic: {name}
current_contributors: {N}
threshold: 3
gap: {M}
::END::
```

Emit namespace leader block:
```
::NAMESPACE_LEADER::
namespace: {name}
leader: {contributor}
signal_count: {N}
::END::
```
(one block per active namespace)

#### 2.3 — Nearest-Miss Assessment

Emit one block per Level 1 candidate (topics exactly 1 unit from any threshold):

```
::NEAREST_MISS::
topic: {value}
achievement: {exact name}
current: {N}
threshold: {N}
gap: 1
level: 1
::END::
```

If no Level 1 candidate exists for a given achievement type, emit before Level 2:

```
::NEAREST_MISS_L1_ABSENT::
achievement: {exact name}
message: "Level 1: no topics are 1 unit away — reporting Level 2"
::END::
```

Then emit Level 2 block (gap = 2) for the closest candidate.

#### 2.4 — Echo Detection

Check every topic against two logical mutual exclusion rules.

**Rule A** — `healthy-momentum` raised AND `Solo Pioneer` EARNED: logically incompatible. Retract `healthy-momentum`.

**Rule B** — Any flag raised AND `First Signal` LOCKED (0 files): logically invalid. Retract the flag.

Emit:

```
::ECHO_DETECTION::
topic_path: {value}
rule_violated: {A/B/none}
flag_retracted: {flag-name or none}
achievement: {achievement-name or —}
resolution: {ECHO RETRACTION statement or "no violation"}
::END::
```

Emit one `::ECHO_DETECTION::` block per topic. If no violations on a topic, emit `rule_violated: none; flag_retracted: none`.

#### 2.5 — Achievement Co-Occurrence Matrix

Count how many topics have each pair of achievements both EARNED simultaneously. The five achievements are: `FS` (First Signal), `SD` (Signal Depth), `SW` (Full Sweep), `SP` (Solo Pioneer), `TT` (Team Topic).

Emit a 5×5 symmetric co-occurrence table (diagonal = count of topics earning that achievement):

```
## Achievement Co-Occurrence Matrix
| | First Signal | Signal Depth | Full Sweep | Solo Pioneer | Team Topic |
|---|---|---|---|---|---|
| First Signal | {count} | {count} | {count} | {count} | {count} |
| Signal Depth | — | {count} | {count} | {count} | {count} |
| Full Sweep | — | — | {count} | {count} | {count} |
| Solo Pioneer | — | — | — | {count} | {count} |
| Team Topic | — | — | — | — | {count} |
```

After the matrix, emit one interpretive note:
`Co-occurrence note: {observation about the most or least common co-occurrence pair and what it implies about team behavior}`

**Section 2.2–2.5 Gate**:

- [ ] All `::HEALTH::` blocks present in severity order (critical → warning → healthy); every field populated; no trajectory claims in any `::HEALTH::` block; no file counts in any `::INERTIA::` block (cross-contamination check)
- [ ] Three `::MILESTONE::` blocks with exact names and non-empty evidence; `::PROXIMITY_LADDER::` blocks present for ALL NOT YET milestones with per-component breakdowns
- [ ] `::NEAREST_MISS::` blocks present (Level 1, or Level 2 with `::NEAREST_MISS_L1_ABSENT::` stated first)
- [ ] `::ECHO_DETECTION::` blocks present for every topic; Rule A and Rule B checked; retraction statements written for violations
- [ ] Co-occurrence matrix present with all 15 distinct cells populated; interpretive note present

**Analyst Handoff** — artifacts transferred to the Publisher:

1. All `::INERTIA::` blocks and `::VELOCITY::` block
2. All `::STALE_CHECK::` blocks
3. All `::HEALTH::` blocks in severity order
4. All `::MILESTONE::` blocks with `::PROXIMITY_LADDER::` blocks for NOT YET milestones
5. `::DEBATE_PROXIMITY::` block and all `::NAMESPACE_LEADER::` blocks
6. All `::NEAREST_MISS::` blocks (and `::NEAREST_MISS_L1_ABSENT::` blocks where applicable)
7. All `::ECHO_DETECTION::` blocks with retraction statements
8. Achievement co-occurrence matrix and interpretive note

---

### ROLE 3: PUBLISHER

**Responsibility**: Synthesis, leaderboard, insight, and actions only. Works from all prior schema blocks. Does NOT re-scan the workspace or re-evaluate achievements.

#### 3.1 — Contributor Leaderboard

Rank contributors descending by signal count. Ties: alphabetical.

Emit leaderboard schema block:

```
::LEADERBOARD_ENTRY::
rank: {N}
contributor: {value}
signals: {N}
topics: {N}
round1_closes: {N actions that would take 1 signal to resolve}
cohort: {specialist/generalist/focused}
::END::
```

`cohort` label: `specialist` if >= 50% signals in 1 namespace; `generalist` if signals span >= 3 namespaces; `focused` if exactly 2 namespaces.

If no contributor metadata: one block with `contributor: no contributor metadata found` and all other fields `—`.

After all leaderboard blocks:
- `Namespace leader: {contributor} leads {namespace} with {N} signals` (one line per active namespace)
- `Solo Pioneer tension: [for each topic where Solo Pioneer EARNED + Team Topic NOT YET] {topic_path} — {contributor} sole; +1 contributor unlocks Team Topic`
- `Collaboration signal: {N} topics with multi-contributor coverage | Highest: {topic} ({N} contributors)`

#### 3.2 — Cross-Dimensional Reconciliation

Select one `::HEALTH::` observation and one `::INERTIA::` observation that interact. Emit:

```
::RECONCILIATION::
health_observation: {specific finding from a ::HEALTH:: block}
inertia_observation: {specific finding from an ::INERTIA:: block}
interaction: {how they connect and what they imply together}
::END::
```

#### 3.3 — Team Insight

**Skeptic gate**: A Skeptic who has read all prior schema blocks already knows every `::HEALTH::` field value, every `::MILESTONE::` status and evidence, every `::PROXIMITY_LADDER::` per-component entry, every `::INERTIA::` flag and trajectory note (including echo-retracted flags and retraction reasons), every `::STALE_CHECK::` status, the `::VELOCITY::` trend, every `::NEAREST_MISS::` entry, every cohort label, and the `::RECONCILIATION::` interaction. The Skeptic would reject any insight restating any field from any prior block. A passing insight requires a second-order inference — a pattern, risk, or trajectory convergence observable only by synthesizing across multiple schema blocks that no single block reveals. An insight that merely repeats a `::PROXIMITY_LADDER::` entry or a `::RECONCILIATION::` interaction fails.

Write one Team Insight sentence containing: (1) a cross-topic conclusion, (2) a concrete number, (3) a specific contributor or topic name.

#### 3.4 — Pre-Write Check

Identify all zero-score conditions. Identify all open (non-echo-retracted) inertia flags. Echo-retracted flags must be excluded from `resolves:` targeting.

**prevents: prefix rule** (first independent enforcement point): any action eliminating a zero-score condition carries `prevents:`. Advancement actions do not.

Inertia-flag-resolving actions MUST declare `resolves: {exact-flag-name}`.

#### 3.5 — Next Actions — Multi-Round Sequencing

Group actions into three rounds by gap distance:
- **Round 1** — exactly 1 signal or 1 contributor addition closes the gap (Level 1 nearest-miss or 1-unit proximity ladder entry)
- **Round 2** — 2–3 signals or coordinated additions needed
- **Round 3** — 4+ signals or multi-contributor coordination required

Write at least 3 actions total across all rounds. Each names a specific namespace + topic + exact achievement or milestone name.

**prevents: prefix rule** (second independent enforcement point): embed in the action format below — any action targeting a zero-score condition carries `prevents:`.

```
## Next Actions

### Round 1 (1 signal closes the gap)
1. [prevents: or omit] `{namespace}/{topic}` → unlocks **{exact name}** [resolves: {flag} or omit]

### Round 2 (2–3 signals needed)
2. [prevents: or omit] `{namespace}/{topic}` → unlocks **{exact name}** [resolves: {flag} or omit]

### Round 3 (4+ signals or coordination)
3. [prevents: or omit] `{namespace}/{topic}` → unlocks **{exact name}** [resolves: {flag} or omit]
```

If no actions exist for a round: `Round {N}: no actions at this gap distance.`

Emit: `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions` (N = actual count).

**Publisher Gate**:

- [ ] Leaderboard: `::LEADERBOARD_ENTRY::` blocks present ranked descending; all fields populated; cohort labels assigned per definition; "no contributor metadata" block if attribution unavailable
- [ ] Namespace leader, solo pioneer tension, and collaboration signal lines present
- [ ] `::RECONCILIATION::` block present with Health observation, Inertia observation, and interaction
- [ ] Team Insight: one sentence; Skeptic gate verified — no restatement of any prior schema block field or proximity ladder entry; cross-topic inference with concrete number and specific name
- [ ] Pre-write check complete; echo-retracted flags excluded from `resolves:` targeting
- [ ] Actions grouped into Round 1 / Round 2 / Round 3; empty round stated explicitly; at least 3 total; each names namespace + topic + exact name; `prevents:` at two independent locations (§3.4 and §3.5); `resolves:` with exact flag names on open flag-resolving actions
- [ ] `ACTIONS GATE` line with actual N substituted

---

## V-03 — 4-Role Pipeline with Reconciler + Flag Lifecycle Annotation + Seeds A+B+H+N+S+T + Seed Y

**Axis**: Role sequence
**Hypothesis**: In R15, cross-dimensional reconciliation, coalition mapping, and nearest-miss confirmation were all handled by the Publisher alongside leaderboard, insight, and actions — a large cognitive load for one role. This variation inserts a dedicated **Reconciler** role between the Analyst and Publisher. The Reconciler owns: cross-dimensional reconciliation, milestone coalition analysis, contributor onboarding paths, and nearest-miss confirmation. The Publisher then focuses purely on leaderboard, insight, and actions. Hypothesis: separating reconciliation into its own role with its own handoff prevents the insight-and-action phase from entangling synthesis with structural analysis. New axis element: Seed Y (flag lifecycle annotation) — the Analyst's Inertia Phase annotates each flag as `new` / `persistent` / `resolved` by comparing against a baseline file (`simulations/.leaderboard-baseline.md`) if one exists. Seed T (achievement rate column) from R15 is also retained.

---

You are running the **Corps Leaderboard** skill in a **4-role pipeline**: Archivist → Analyst → Reconciler → Publisher. Execute each role completely before advancing. No role may perform work assigned to another. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: The Analyst runs Inertia Phase before Health Phase. Health Phase topics are reported in descending severity order (critical → warning → healthy), alphabetical within tier. The Reconciler runs between Analyst and Publisher and handles cross-dimensional pairing, coalition analysis, and onboarding paths. The Publisher handles leaderboard, insight, and actions only.

---

### ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Scans workspace, builds signal registry, constructs contributor index. Does NOT evaluate achievements, assess trajectory, rank contributors, or write insights or actions.

#### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path segment after `simulations/`
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-` > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write `REGISTRY: empty — no signal files found in simulations/` and stop. Roles 2, 3, and 4 do not run.

Print registry: `topic_path | namespace | contributor | file`

Print namespace coverage: `Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`

The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

**Baseline check**: Attempt to read `simulations/.leaderboard-baseline.md`. If present, extract the prior inertia flag table from it (columns: `topic_path`, `flags`). Print: `Baseline found: {flag table row count} topic entries loaded` or `Baseline not found: all flags will be annotated as new`.

#### 1.2 — Contributor Index

Print: `contributor | distinct_namespaces | topic_paths | file_count`.

**Archivist Gate**:

- [ ] Registry table with all four columns
- [ ] Namespace coverage line with active and empty lists
- [ ] Contributor index with `distinct_namespaces` column populated
- [ ] Baseline status line present (`Baseline found` or `Baseline not found`)

**Archivist Handoff** — artifacts transferred to the Analyst:

1. Signal registry table (`topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line
3. Contributor index (`contributor`, `distinct_namespaces`, `topic_paths`, `file_count`)
4. Prior inertia flag table from baseline (columns: `topic_path`, `flags`) or `baseline: none`

---

### ROLE 2: ANALYST

**Responsibility**: Evaluation only. Runs Inertia Phase (§2.1, with flag lifecycle annotation), then Health Phase (§2.2 in severity order), then Nearest-Miss Assessment (§2.3), then Echo Detection (§2.4). Sub-phases structurally separated. Does NOT handle reconciliation, coalition analysis, ranking, insights, or actions.

#### 2.1 — Inertia Phase (RUNS FIRST)

Reports trajectory, momentum, and flag lifecycle only. No file counts, achievement statuses, or coverage totals.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|---|---|
| `stuck-at-first` | exactly 1 file; Signal Depth not earned |
| `solo-hold` | exactly 1 contributor; no second contributor present |
| `namespace-thin` | all files in 1 namespace; Full Sweep not earned |
| `healthy-momentum` | Signal Depth earned AND >= 2 distinct contributors |

Severity: `critical` = 2+ non-momentum flags; `warning` = 1; `healthy` = 0.

**Flag lifecycle annotation** — for each flag raised on a topic, annotate its lifecycle status by comparing against the baseline:
- `new` — flag is raised now; was absent in baseline (or no baseline exists)
- `persistent` — flag was raised in baseline AND is still raised now
- `resolved` — flag was raised in baseline but is NOT raised now (include these as resolved-flag rows even though the flag is no longer active)

Print inertia table: `topic_path | flags_raised | flag_lifecycle | trajectory note | severity`

The `flag_lifecycle` column lists each flag with its annotation, e.g.: `stuck-at-first(persistent), solo-hold(new)`. Resolved flags appear in a separate `resolved_flags` line below the topic row: `resolved since baseline: {flag-name}`.

If no baseline exists, all currently-raised flags are `new`; no resolved flags can be identified.

Print stale signal table: `topic_path | stale_status`

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`
Classification: > 50% healthy = increasing; < 25% = stalled; otherwise flat.

**Section 2.1 Gate**:

- [ ] Inertia table with flag lifecycle column; every topic evaluated for all four flags; `new`/`persistent`/`resolved` annotation present per flag
- [ ] No file counts, achievement statuses, or coverage totals in Inertia Phase content
- [ ] Stale signal table and velocity summary present

#### 2.2 — Health Phase (RUNS SECOND — severity order: critical → warning → healthy)

Reports current signal state only. No trajectory claims, momentum language, or flag restatements.

For each `topic_path` (severity order, alphabetical within tier):

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {N}/9

| Achievement | Status | Evidence / Unlock Path |
|---|---|---|
| First Signal | EARNED/LOCKED | {evidence or "needs >= 1 file"} |
| Signal Depth | EARNED/LOCKED | {evidence or "needs {X} more file(s)"} |
| Full Sweep | EARNED/LOCKED | {evidence or "needs {X} more namespace(s)"} |
| Solo Pioneer | EARNED/LOCKED | {evidence or "needs exactly 1 contributor with >= 1 file"} |
| Team Topic | EARNED/LOCKED | {evidence or "needs {X} more contributor(s) with >= 1 file"} |
```

Achievement names must be exact. LOCKED rows include the specific unlock requirement.

When Solo Pioneer EARNED and Team Topic NOT YET: append `[TENSION: solo hold — 1 additional contributor with >= 1 signal unlocks Team Topic]`

After all topic achievement blocks, evaluate all three team milestones:

| Milestone (exact name) | Earned when |
|---|---|
| `first team signal` | any file in workspace |
| `shared coverage` | >= 2 topics each with >= 2 distinct contributors |
| `debate starter` | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

For every NOT YET milestone, print a **Milestone Proximity Ladder** immediately following the row:

- `first team signal` NOT YET: `Proximity ladder: 1 signal file in any namespace for any topic closes this milestone.`
- `shared coverage` NOT YET: `Proximity ladder: {N} qualifying topics (need 2 total). Per-topic contributor deficit: {topic_A} needs {M} more contributor(s); {topic_B} needs {M} more contributor(s). [list every candidate topic individually]`
- `debate starter` NOT YET: `Proximity ladder: nearest is {topic_path} at {N}/3 contributors. {M} more distinct contributor signal(s) needed.`

EARNED milestones do not receive a proximity ladder.

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count`

#### 2.3 — Nearest-Miss Assessment

**Level 1** — every topic 1 unit from any threshold: topic + achievement + gap, ascending sort.

**Level 2** — closest 2-unit candidate; ONLY when no Level 1 exists for that achievement type. State `Level 1: no topics are 1 unit away` before Level 2 entries.

Print: `topic | achievement | gap | level`

#### 2.4 — Echo Detection

**Rule A** — `healthy-momentum` raised AND `Solo Pioneer` EARNED: retract `healthy-momentum`.
Emit: `ECHO RETRACTION: healthy-momentum on {topic} retracted — incompatible with Solo Pioneer EARNED.`

**Rule B** — Any flag raised AND `First Signal` LOCKED: retract the flag.
Emit: `ECHO RETRACTION: {flag} on {topic} retracted — First Signal LOCKED; no files to evaluate.`

```
## Echo Detection Table
| topic_path | Rule | Flag retracted | Achievement | Resolution |
|---|---|---|---|---|
```

If no violations: one row `| none | — | — | — | — |`.

**Section 2.2–2.4 Gate**:

- [ ] Topics in severity order; all five achievement names exact; LOCKED rows include unlock paths; no trajectory language in Health Phase blocks; no file counts in Inertia Phase (contamination check)
- [ ] All three milestone names verbatim with non-empty evidence; proximity ladders for ALL NOT YET milestones with per-topic/per-contributor deficit breakdowns
- [ ] Nearest-miss: Level 1 ascending, or Level 2 with "Level 1: no topics are 1 unit away" stated first
- [ ] Echo Detection Table present; Rule A and Rule B checked; retraction statements for violations; "none detected" row if clean

**Analyst Handoff** — artifacts transferred to the Reconciler:

1. Inertia Phase table with flag lifecycle annotations (`topic_path`, `flags_raised`, `flag_lifecycle`, `trajectory note`, `severity`)
2. Resolved flags list per topic
3. Stale signal table and velocity summary
4. Per-topic Health Phase achievement tables in severity order
5. Team milestone table (3 rows) with proximity ladders for all NOT YET milestones
6. Debate starter proximity line and namespace leader table
7. Nearest-miss assessment table (`topic`, `achievement`, `gap`, `level`)
8. Echo Detection Table with retraction statements

---

### ROLE 3: RECONCILER

**Responsibility**: Cross-dimensional synthesis preparation only. The Reconciler produces the reconciliation pairing, milestone coalition analysis, and contributor onboarding paths. The Reconciler does NOT rank contributors, write the Team Insight, or write actions.

#### 3.1 — Cross-Dimensional Reconciliation

Select one observation from the Health Phase achievement tables and one from the Inertia Phase table that interact. State the interaction:

```
## Reconciliation
| Health observation | Inertia observation | Interaction |
|---|---|---|
| {finding from Health Phase} | {finding from Inertia Phase} | {how they connect} |
```

#### 3.2 — Milestone Coalition Analysis

For each NOT YET milestone, identify two paths to closing the gap:

- **Internal coalition path**: Using only existing contributors (named from the contributor index), which contributor adds what signal in which topic to advance the milestone. Name the contributor + topic + action.
- **External path**: If no existing contributor can close the gap alone, which topic needs a new (unnamed) contributor. Name the topic and the required signal type.

```
## Coalition Analysis
| Milestone | Internal path | External path |
|---|---|---|
| {name} | {existing contributor: topic + action, or "not possible with current contributors"} | {topic needing new contributor, or "not needed — internal path available"} |
```

#### 3.3 — Contributor Onboarding Paths

For every topic where `Solo Pioneer` is EARNED and `Team Topic` is NOT YET, emit one onboarding path:

`Onboarding path — {topic_path}: {current_contributor} holds solo. Fastest Team Topic unlock: 1 file in {namespace} (any namespace not yet covered, or the most signal-sparse namespace) from any new contributor.`

If no such topics exist: `Onboarding paths: none — no topics with Solo Pioneer EARNED + Team Topic NOT YET.`

#### 3.4 — Flag Lifecycle Summary

Using the flag lifecycle annotations from the Analyst's Inertia Phase:

Print:
- `Persistent flags (resisted last cycle): {count} — {list of topic:flag pairs}`
- `New flags (appeared since last run): {count} — {list of topic:flag pairs}`
- `Resolved flags (cleared since last run): {count} — {list of topic:flag pairs}`
- `No baseline: all flags marked new — lifecycle tracking begins this run.` (if applicable)

**Reconciler Gate**:

- [ ] Reconciliation pairing present with one Health observation, one Inertia observation, and interaction
- [ ] Coalition analysis present for every NOT YET milestone with both internal and external paths assessed
- [ ] Onboarding paths present for every Solo Pioneer EARNED + Team Topic NOT YET topic (or "none" statement)
- [ ] Flag lifecycle summary present with counts for persistent, new, and resolved flags

**Reconciler Handoff** — artifacts transferred to the Publisher:

1. Reconciliation pairing table
2. Coalition analysis table
3. Contributor onboarding paths
4. Flag lifecycle summary (persistent / new / resolved counts)
5. All Analyst Handoff artifacts (pass-through)

---

### ROLE 4: PUBLISHER

**Responsibility**: Leaderboard, Team Insight, and actions only. Works from all prior artifacts. Does NOT re-evaluate achievements, re-run reconciliation, or re-assess flags.

#### 4.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical.

Per contributor, compute:
- `rate`: achievements earned / signals (e.g., `0.50` for 2 achievements / 4 signals; `--` if signals = 0)

Print: `rank | contributor | signals | topics | achievements | rate`

If no contributor metadata: one row `| 1 | no contributor metadata found | — | — | — | — |`.

After leaderboard:
- `Namespace leader: {contributor} leads {namespace} with {N} signals` (per active namespace)
- `Solo Pioneer tension:` [from Reconciler's onboarding paths, cite each topic]
- `Collaboration signal: {N} topics with multi-contributor coverage | Highest: {topic} ({N} contributors)`
- `Persistent flag watch: {count} flags persisted from prior run — see flag lifecycle summary`

#### 4.2 — Team Insight

**Skeptic gate**: A Skeptic who has read all prior output knows: every achievement status (from Health Phase tables), every milestone row (including all per-topic deficit breakdowns in proximity ladders), every inertia flag with lifecycle annotations (including `new`, `persistent`, `resolved`, and echo-retracted flags with retraction reasons), every severity tier, trajectory note, stale status, velocity summary, nearest-miss entry, reconciliation pairing, coalition analysis, onboarding paths, flag lifecycle summary, achievement rate, and `persistent flag watch` line. An insight restating any of these fails. A passing insight surfaces a second-order pattern observable only by synthesizing across the lifecycle annotations, health data, and reconciliation — a risk or convergence not visible in any single artifact.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor or topic name.

#### 4.3 — Pre-Write Check

Identify zero-score conditions. Identify open (non-echo-retracted) flags. Echo-retracted flags excluded from `resolves:` targeting. Flag `persistent` flags as higher-priority (they resisted one cycle).

**prevents: prefix rule** (first independent enforcement point): any action eliminating a zero-score condition carries `prevents:`.

Inertia-flag-resolving actions declare `resolves: {exact-flag-name}`.

#### 4.4 — Next Actions

Write at least 3 actions. Each names a specific namespace + topic + exact achievement or milestone name.

**prevents: prefix rule** (second independent enforcement point): embedded in action template — zero-score condition actions carry `prevents:`.

```
## Next Actions

1. [prevents: or omit] `{namespace}/{topic}` → unlocks **{exact name}** [resolves: {flag} or omit] [flag_lifecycle: persistent/new/omit]
2. ...
3. ...
```

`flag_lifecycle: persistent` on actions targeting persistent flags (to surface prioritization signal).

After all actions, emit: `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions`

**Publisher Gate**:

- [ ] Leaderboard present ranked descending with `rate` column; "no contributor metadata" row if attribution unavailable
- [ ] Namespace leader, solo pioneer tension (from onboarding paths), collaboration signal, and persistent flag watch lines present
- [ ] Team Insight one sentence; Skeptic gate verified — includes flag lifecycle + coalition + reconciliation in known context; insight is a new inference not restatable from any prior artifact
- [ ] Pre-write check complete; echo-retracted flags excluded; persistent flags prioritized
- [ ] At least 3 actions; each names namespace + topic + exact name; `prevents:` at two independent locations (§4.3 and §4.4); `resolves:` on open flag-resolving actions with exact flag names; `flag_lifecycle: persistent` on persistent-flag-resolving actions
- [ ] ACTIONS GATE line with actual N substituted

---

## V-04 — Combination: Tiered Actions + Coalition Mapping + Milestone Regression Risk + Seeds A+B+H+K+M+N+S+W + Seed AB

**Axis**: Combination
**Hypothesis**: R15 V-04 combined inertia-first ordering, `[CRITICAL]`/`[WARNING]`/`[ADVANCING]` action tiers, action-to-gap binding, and milestone coalition mapping. This variation carries those patterns and adds Seed AB (milestone regression risk) as the new element: for each EARNED milestone, compute whether removing any single contributor would un-earn it. A milestone where contributor X's removal collapses the contributor count below threshold is `fragile: X`; one where no single removal causes regression is `stable`. Regression risk completes the milestone lifecycle that proximity ladders begin: ladders show the path in; regression risk shows the path out. The hypothesis is that `fragile` milestones change the prioritization of `resolves: solo-hold` actions — stabilizing a fragile milestone by adding a second contributor is higher priority than advancing a gap-locked achievement.

---

You are running the **Corps Leaderboard** skill in a **4-role pipeline**: Archivist → Analyst → Strategist → Publisher. Execute each role completely before advancing. No role may perform work assigned to another. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: The Analyst runs Inertia Phase before Health Phase. Health Phase topics report in descending severity order (critical → warning → healthy), alphabetical within tier. The Strategist handles leaderboard, coalition analysis, and regression risk. The Publisher handles insight and actions.

---

### ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Scans workspace, builds signal registry, constructs contributor index. Does NOT evaluate achievements, assess trajectory, rank contributors, or write insights or actions.

Glob `simulations/**/*.md`. For every matching file:

- `topic_path` — path after `simulations/`
- `namespace` — first segment
- `contributor` — `author:` > `contributor:` > filename prefix before `-` > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write `REGISTRY: empty — no signal files found in simulations/` and stop. All downstream roles do not run.

Print registry: `topic_path | namespace | contributor | file`

Print: `Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`

The 9 namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

Print contributor index: `contributor | distinct_namespaces | topic_paths | file_count`

**Archivist Gate**:

- [ ] Registry table with all four columns
- [ ] Namespace coverage line with active and empty lists
- [ ] Contributor index with all four columns

**Archivist Handoff** to Analyst:

1. Signal registry (`topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line
3. Contributor index (`contributor`, `distinct_namespaces`, `topic_paths`, `file_count`)

---

### ROLE 2: ANALYST

**Responsibility**: Evaluation only. Inertia Phase first, then Health Phase in severity order, then Nearest-Miss Assessment, then Echo Detection. Structurally separated — no cross-phase content contamination. Does NOT rank contributors, analyze milestones for regression risk, or write insights or actions.

#### 2.1 — Inertia Phase (RUNS FIRST)

Trajectory and momentum only. No file counts, achievement statuses, or coverage totals.

| Inertia Flag | Condition |
|---|---|
| `stuck-at-first` | exactly 1 file; Signal Depth not earned |
| `solo-hold` | exactly 1 contributor; no second contributor present |
| `namespace-thin` | all files in 1 namespace; Full Sweep not earned |
| `healthy-momentum` | Signal Depth earned AND >= 2 distinct contributors |

Severity: `critical` = 2+ non-momentum flags; `warning` = 1; `healthy` = 0.

Print inertia table: `topic_path | flags | trajectory note | severity`

Print stale signal table: `topic_path | stale_status` (`stale` / `active` / `date-unknown`)

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`
Classification: > 50% healthy = increasing; < 25% = stalled; otherwise flat.

**Section 2.1 Gate**:

- [ ] Inertia table with severity column; all four flags evaluated per topic
- [ ] No file counts, achievement statuses, or coverage totals in Inertia Phase content
- [ ] Stale signal table and velocity summary present

#### 2.2 — Health Phase (RUNS SECOND — severity order: critical → warning → healthy)

Current signal state only. No trajectory claims or flag restatements.

For each `topic_path` (severity order, alphabetical within tier):

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {N}/9

| Achievement | Status | Evidence / Unlock Path |
|---|---|---|
| First Signal | EARNED/LOCKED | {evidence or unlock requirement} |
| Signal Depth | EARNED/LOCKED | {evidence or needs {X} more files} |
| Full Sweep | EARNED/LOCKED | {evidence or needs {X} more namespaces} |
| Solo Pioneer | EARNED/LOCKED | {evidence or needs exactly 1 contributor with >= 1 file} |
| Team Topic | EARNED/LOCKED | {evidence or needs {X} more contributor(s) with >= 1 file} |
```

When Solo Pioneer EARNED + Team Topic NOT YET: append `[TENSION: solo hold — 1 additional contributor with >= 1 signal unlocks Team Topic]`

**Team Milestones** (exact names required):

| Milestone | Status | Evidence |
|---|---|---|
| first team signal | EARNED/NOT YET | {non-empty} |
| shared coverage | EARNED/NOT YET | {non-empty} |
| debate starter | EARNED/NOT YET | {non-empty} |

For every NOT YET milestone, print a **Milestone Proximity Ladder** immediately following its row:

- `first team signal` NOT YET: `Proximity ladder: 1 signal file in any namespace for any topic closes this milestone.`
- `shared coverage` NOT YET: `Proximity ladder: {N} qualifying topics (need 2). Per-topic contributor deficit: {topic_A} needs {M} more contributor(s); {topic_B} needs {M} more contributor(s). [list every candidate individually]`
- `debate starter` NOT YET: `Proximity ladder: nearest is {path} at {N}/3 contributors. {M} more distinct contributor signal(s) needed.`

EARNED milestones do not receive a proximity ladder.

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count`

#### 2.3 — Nearest-Miss Assessment

**Level 1** — topics 1 unit from any threshold. Sort ascending: `topic | achievement | gap | level`

**Level 2** — closest 2-unit candidate; ONLY when no Level 1 exists for that type. State `Level 1: no topics are 1 unit away` first.

#### 2.4 — Echo Detection

**Rule A** — `healthy-momentum` raised AND `Solo Pioneer` EARNED: retract `healthy-momentum`.
`ECHO RETRACTION: healthy-momentum on {topic} retracted — incompatible with Solo Pioneer EARNED.`

**Rule B** — Any flag raised AND `First Signal` LOCKED: retract flag.
`ECHO RETRACTION: {flag} on {topic} retracted — First Signal LOCKED; no files to evaluate.`

```
## Echo Detection Table
| topic_path | Rule | Flag retracted | Achievement | Resolution |
|---|---|---|---|---|
```

No violations: one row `| none | — | — | — | — |`.

**Section 2.2–2.4 Gate**:

- [ ] Topics in severity order (critical → warning → healthy); all five achievement names exact; LOCKED rows include specific unlock paths; no trajectory language in Health Phase; no file counts in Inertia Phase (contamination check)
- [ ] All three milestone exact names with non-empty evidence; proximity ladders for ALL NOT YET milestones with per-component deficit breakdowns; Skeptic gate will include proximity ladder entries as known context
- [ ] Nearest-miss present (Level 1, or Level 2 with "Level 1 empty" stated first)
- [ ] Echo Detection Table present; Rule A and Rule B checked; retraction statements for violations

**Analyst Handoff** to Strategist:

1. Inertia Phase table (`topic_path`, `flags`, `trajectory note`, `severity`)
2. Stale signal table and velocity summary
3. Per-topic Health Phase achievement tables in severity order
4. Team milestone table with proximity ladders for NOT YET milestones
5. Debate starter proximity line and namespace leader table
6. Nearest-miss assessment (`topic`, `achievement`, `gap`, `level`)
7. Echo Detection Table with retraction statements

---

### ROLE 3: STRATEGIST

**Responsibility**: Leaderboard, coalition analysis, milestone regression risk, and cross-dimensional reconciliation. Does NOT write the Team Insight or write actions.

#### 3.1 — Contributor Leaderboard

Rank contributors descending by signal count. Ties: alphabetical.

Print: `rank | contributor | signals | topics`

If no contributor metadata: `| 1 | no contributor metadata found | — | — |`

After leaderboard:
- `Namespace leader: {contributor} leads {namespace} with {N} signals` (per active namespace)
- `Solo Pioneer tension: [per topic with Solo Pioneer EARNED + Team Topic NOT YET] {topic} — {contributor} holds solo; 1 new contributor unlocks Team Topic`
- `Collaboration signal: {N} topics multi-contributor | Highest: {topic} ({N} contributors)`

#### 3.2 — Milestone Coalition Analysis

For each NOT YET milestone, map the two paths using the contributor index and proximity ladder data:

```
## Coalition Analysis
| Milestone | Internal coalition path | External path |
|---|---|---|
| {name} | {contributor} adds {signal type} to {topic}: closes {gap description} | {topic needing new contributor, or "not needed — internal path available"} |
```

Internal path: an existing named contributor takes a specific action. External path: a new contributor must be recruited to a specific topic.

#### 3.3 — Milestone Regression Risk

For each EARNED milestone, compute whether removing any single contributor would cause the milestone to un-earn. Test each contributor in the contributor index.

For `first team signal`: stable unless removing the only contributor with files leaves workspace empty.
For `shared coverage`: fragile if removing contributor X drops any qualifying topic below 2 distinct contributors.
For `debate starter`: fragile if removing contributor X drops any qualifying topic below 3 contributors.

Print: `milestone | status | regression_risk | at_risk_contributor`

Where `regression_risk` = `stable` (no single removal causes regression) or `fragile: {contributor}` (removing this contributor un-earns the milestone).

If milestone is NOT YET: `regression_risk = N/A`.

#### 3.4 — Cross-Dimensional Reconciliation

```
## Reconciliation
| Health observation | Inertia observation | Interaction |
|---|---|---|
| {finding from Health Phase} | {finding from Inertia Phase} | {cross-dimensional connection} |
```

**Strategist Gate**:

- [ ] Leaderboard present ranked descending; namespace leader, solo pioneer tension, collaboration signal lines present
- [ ] Coalition analysis table present for every NOT YET milestone with internal and external paths assessed
- [ ] Regression risk table present for every EARNED milestone with `stable` or `fragile: {contributor}` assignments; NOT YET milestones show `N/A`
- [ ] Reconciliation pairing present

**Strategist Handoff** to Publisher:

1. Contributor leaderboard
2. Namespace leader lines, solo pioneer tension, collaboration signal
3. Coalition analysis table
4. Milestone regression risk table
5. Reconciliation pairing
6. All Analyst Handoff artifacts (pass-through)

---

### ROLE 4: PUBLISHER

**Responsibility**: Team Insight and actions only. Works from all prior artifacts. Does NOT re-evaluate achievements or re-run analysis.

#### 4.1 — Team Insight

**Skeptic gate**: A Skeptic who has read all prior output knows: every achievement status (Health Phase tables), every milestone row (including per-component deficit breakdowns in proximity ladders and coalition analysis), every inertia flag (including echo-retracted flags and reasons), every severity tier, trajectory note, stale status, velocity summary, nearest-miss entry, leaderboard, namespace leaders, solo pioneer tension lines, collaboration signal, coalition paths, milestone regression risk assignments, and reconciliation pairing. An insight restating any of these fails. An insight that only repeats a `fragile: {contributor}` regression risk assignment, a proximity ladder entry, or a coalition path also fails. A passing insight surfaces a second-order pattern — a risk, convergence, or cross-topic inference — requiring synthesis across the regression risk data, flag trajectory, and health state that no individual section reveals directly.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor or topic name.

#### 4.2 — Pre-Write Check

Identify all zero-score conditions. Identify all open (non-echo-retracted) inertia flags. Echo-retracted flags excluded from `resolves:` targeting.

**prevents: prefix rule** (first independent enforcement point): actions targeting zero-score conditions carry `prevents:`. Advancement actions do not.

Inertia-flag-resolving actions declare `resolves: {exact-flag-name}`. Milestone-regression-risk-addressing actions should note `[stabilizes: {milestone}]` where applicable.

#### 4.3 — Next Actions — Tiered by Severity

Group actions by tier:
- `[CRITICAL]` — actions targeting critical-severity topics
- `[WARNING]` — actions targeting warning-severity topics
- `[ADVANCING]` — actions targeting healthy topics or milestone gaps

Write at least 3 actions. Each names a specific namespace + topic + exact achievement or milestone name.

**prevents: prefix rule** (second independent enforcement point): actions targeting zero-score conditions carry `prevents:` as the opening prefix in the action template.

```
## Next Actions

1. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] `{namespace}/{topic}` → unlocks **{exact name}** [resolves: {flag} or omit] [closes: {achievement} gap of {N} {unit} for {topic}] [stabilizes: {milestone} or omit]
2. ...
3. ...
```

After all actions: `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions`

**Publisher Gate**:

- [ ] Team Insight one sentence; Skeptic gate verified — insight synthesizes across regression risk, flag trajectory, and health; includes concrete number and specific name; is not a restatement of any prior section including regression risk, proximity ladders, or coalition paths
- [ ] Pre-write check complete; zero-score conditions identified; echo-retracted flags excluded
- [ ] At least 3 tiered actions; tiers match topic severity; each names namespace + topic + exact name; `resolves:` with exact flag names; `closes:` binding present; `stabilizes:` where applicable; `prevents:` at two independent locations (§4.2 and §4.3)
- [ ] ACTIONS GATE line with actual N substituted

---

## V-05 — Full Integration: 5-Role + All R15+R16 Seeds

**Axis**: Full combination
**Hypothesis**: V-05 integrates all seeds from R15 (A+B+H+K+M+N+S+T+U+V+W+X) and all new seeds from R16 (Y+Z+AA+AB+AC) into a 5-role pipeline. Role specialization: Archivist (data), Analyst (evaluation), Reconciler (cross-dimensional synthesis + lifecycle), Strategist (leaderboard + coalition + regression + falsifiability), Publisher (insight + actions). The hypothesis is that full seed integration with a 5-role pipeline maximizes both the precision of each output section and the novelty bar for the Team Insight — the Skeptic gate encompasses the deepest possible known context (including flag lifecycle, co-occurrence matrix, regression risk, coalition analysis, and falsifiability contract), forcing the insight to operate at a higher inference level than any prior variation. New seeds AC (contributor onboarding paths, formalized from Seed W extension), Y (flag lifecycle), Z (co-occurrence matrix), AA (namespace gap debt), and AB (milestone regression risk) are all present. All 25 aspirational rubric criteria are expected to pass.

---

You are running the **Corps Leaderboard** skill in a **5-role pipeline**: Archivist → Analyst → Reconciler → Strategist → Publisher. Execute each role completely before advancing. No role may perform work assigned to another. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: The Analyst runs Inertia Phase (with flag lifecycle annotation) before Health Phase. Health Phase uses severity order (critical → warning → healthy), alphabetical within tier. The Reconciler handles cross-dimensional pairing, flag lifecycle summary, and co-occurrence analysis. The Strategist handles leaderboard, coalition analysis, and milestone regression risk. The Publisher handles Team Insight and actions.

---

### ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Scans workspace, builds signal registry, constructs contributor index. Does NOT evaluate achievements, assess trajectory, rank contributors, or write insights or actions.

Glob `simulations/**/*.md`. For every matching file:

- `topic_path` — path after `simulations/`
- `namespace` — first segment
- `contributor` — `author:` > `contributor:` > filename prefix before first `-` > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write `REGISTRY: empty — no signal files found in simulations/` and stop. Roles 2–5 do not run.

Print registry: `topic_path | namespace | contributor | file`

Print: `Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`

The 9 namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

Print contributor index: `contributor | distinct_namespaces | topic_paths | file_count`

**Baseline check**: Attempt to read `simulations/.leaderboard-baseline.md`. Extract prior inertia flag table (columns: `topic_path`, `flags`) if present.
Print: `Baseline found: {row count} topic entries` or `Baseline not found: flag lifecycle will mark all flags as new`.

**Archivist Gate**:

- [ ] Registry table with all four columns
- [ ] Namespace coverage line with active and empty lists
- [ ] Contributor index with `distinct_namespaces` column populated
- [ ] Baseline status line present

**Archivist Handoff** to Analyst:

1. Signal registry (`topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line
3. Contributor index (`contributor`, `distinct_namespaces`, `topic_paths`, `file_count`)
4. Prior inertia flag table from baseline (or `baseline: none`)

---

### ROLE 2: ANALYST

**Responsibility**: Evaluation only. Inertia Phase with flag lifecycle (§2.1) first, then Health Phase in severity order (§2.2), then Nearest-Miss (§2.3), then Echo Detection (§2.4). Structurally separated — no cross-phase content contamination. Does NOT reconcile, rank contributors, compute regression risk, write insights, or write actions.

#### 2.1 — Inertia Phase (RUNS FIRST — with flag lifecycle annotation)

Trajectory, momentum, and flag lifecycle only. No file counts, achievement statuses, or coverage totals.

| Inertia Flag | Condition |
|---|---|
| `stuck-at-first` | exactly 1 file; Signal Depth not earned |
| `solo-hold` | exactly 1 contributor; no second contributor present |
| `namespace-thin` | all files in 1 namespace; Full Sweep not earned |
| `healthy-momentum` | Signal Depth earned AND >= 2 distinct contributors |

Severity: `critical` = 2+ non-momentum flags; `warning` = 1; `healthy` = 0.

**Flag lifecycle annotation** — for each flag currently raised, compare against baseline:
- `new` — flag present now; absent in baseline (or no baseline)
- `persistent` — flag present in both baseline and current run
- `resolved` — flag present in baseline; NOT present in current run (report as resolved-flag row below topic)

Print inertia table: `topic_path | flags_raised(lifecycle) | trajectory note | severity`

`flags_raised(lifecycle)` format: `stuck-at-first(persistent), solo-hold(new)`. If no flags: `none`.

After the inertia table, list resolved flags: `resolved since baseline: {topic_path}: {flag-name}` (one line per resolved flag; omit section if no baseline or no resolved flags).

Print stale signal table: `topic_path | stale_status`

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`
Classification: > 50% healthy = increasing; < 25% = stalled; otherwise flat.

**Section 2.1 Gate**:

- [ ] Inertia table with `flags_raised(lifecycle)` column; all four flags evaluated per topic; lifecycle annotation present per raised flag
- [ ] No file counts, achievement statuses, or coverage totals in Inertia Phase content
- [ ] Resolved flags list present (or omitted with note if no baseline)
- [ ] Stale signal table and velocity summary present

#### 2.2 — Health Phase (RUNS SECOND — severity order: critical → warning → healthy)

Current signal state only. No trajectory claims, momentum language, or flag restatements.

For each `topic_path` (severity order, alphabetical within tier):

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {N}/9

| Achievement | Status | Evidence / Unlock Path |
|---|---|---|
| First Signal | EARNED/LOCKED | {evidence or "needs >= 1 file"} |
| Signal Depth | EARNED/LOCKED | {evidence or "needs {X} more file(s) to reach 3"} |
| Full Sweep | EARNED/LOCKED | {evidence or "needs {X} more namespace(s) to reach 3"} |
| Solo Pioneer | EARNED/LOCKED | {evidence or "needs exactly 1 contributor with >= 1 file"} |
| Team Topic | EARNED/LOCKED | {evidence or "needs {X} more contributor(s) each with >= 1 file"} |
```

Achievement names exact. LOCKED rows include specific unlock requirements. EARNED rows include evidence.

When Solo Pioneer EARNED + Team Topic NOT YET: `[TENSION: solo hold — 1 additional contributor with >= 1 signal unlocks Team Topic]`

**Team Milestones** (exact names):

| Milestone | Status | Evidence |
|---|---|---|
| `first team signal` | EARNED/NOT YET | {non-empty} |
| `shared coverage` | EARNED/NOT YET | {non-empty} |
| `debate starter` | EARNED/NOT YET | {non-empty} |

For every NOT YET milestone, print a **Milestone Proximity Ladder** immediately below:

- `first team signal` NOT YET: `Proximity ladder: 1 signal file in any namespace for any topic closes this milestone.`
- `shared coverage` NOT YET: `Proximity ladder: {N} qualifying topics (need 2). Per-topic contributor deficit: {topic_A} needs {M} more contributor(s); {topic_B} needs {M} more contributor(s). [list every candidate topic individually]`
- `debate starter` NOT YET: `Proximity ladder: nearest is {path} at {N}/3 contributors. {M} more distinct contributor signal(s) needed.`

EARNED milestones do not receive a proximity ladder.

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count`

#### 2.3 — Nearest-Miss Assessment

**Level 1** — every topic 1 unit from any threshold. Print: `topic | achievement | gap | level`, ascending.

**Level 2** — closest 2-unit candidate; ONLY when no Level 1 for a type. State `Level 1: no topics are 1 unit away` before Level 2.

#### 2.4 — Echo Detection

**Rule A** — `healthy-momentum` AND `Solo Pioneer` EARNED: logically incompatible. Retract `healthy-momentum`.
`ECHO RETRACTION: healthy-momentum on {topic} retracted — incompatible with Solo Pioneer EARNED (requires exactly 1 contributor).`

**Rule B** — Any flag raised AND `First Signal` LOCKED: retract flag.
`ECHO RETRACTION: {flag} on {topic} retracted — First Signal LOCKED; no files to evaluate.`

```
## Echo Detection Table
| topic_path | Rule | Flag retracted | Achievement | Resolution |
|---|---|---|---|---|
```

No violations: one row `| none | — | — | — | — |`.

**Section 2.2–2.4 Gate**:

- [ ] Topics in severity order; all five achievement names exact; LOCKED rows with specific unlock paths; no trajectory language in Health Phase; no file counts in Inertia Phase (contamination check enforced at gate)
- [ ] All three milestone exact names with non-empty evidence; proximity ladders for ALL NOT YET milestones with per-topic/per-contributor deficit breakdowns
- [ ] Nearest-miss Level 1 ascending; Level 2 only with "Level 1: no topics are 1 unit away" stated first
- [ ] Echo Detection Table; Rule A and Rule B checked for every topic; retraction statements for violations; "none detected" row if clean

**Analyst Handoff** to Reconciler:

1. Inertia Phase table (`topic_path`, `flags_raised(lifecycle)`, `trajectory note`, `severity`)
2. Resolved flags list
3. Stale signal table and velocity summary
4. Per-topic Health Phase achievement tables in severity order
5. Team milestone table with proximity ladders for all NOT YET milestones
6. Debate starter proximity line and namespace leader table
7. Nearest-miss table (`topic`, `achievement`, `gap`, `level`)
8. Echo Detection Table with retraction statements

---

### ROLE 3: RECONCILER

**Responsibility**: Cross-dimensional synthesis preparation, flag lifecycle summary, and co-occurrence analysis. Does NOT rank contributors, compute regression risk, write insights, or write actions.

#### 3.1 — Cross-Dimensional Reconciliation

```
## Reconciliation
| Health observation | Inertia observation | Interaction |
|---|---|---|
| {specific finding from Health Phase} | {specific finding from Inertia Phase} | {how they connect} |
```

#### 3.2 — Flag Lifecycle Summary

Using flag lifecycle annotations from §2.1:

- `Persistent flags (resisted last cycle): {count} — {list of topic:flag pairs}`
- `New flags (appeared this run): {count} — {list of topic:flag pairs}`
- `Resolved flags (cleared since last run): {count} — {list of topic:flag pairs}`

If no baseline: `Baseline not found — all flags marked new; lifecycle tracking begins this run.`

#### 3.3 — Achievement Co-Occurrence Matrix

Count how many topics have each pair of achievements both EARNED. Five achievements: `FS` (First Signal), `SD` (Signal Depth), `SW` (Full Sweep), `SP` (Solo Pioneer), `TT` (Team Topic). Diagonal = count of topics with that achievement EARNED.

```
## Achievement Co-Occurrence Matrix
| | First Signal | Signal Depth | Full Sweep | Solo Pioneer | Team Topic |
|---|---|---|---|---|---|
| First Signal | {N} | {N} | {N} | {N} | {N} |
| Signal Depth | — | {N} | {N} | {N} | {N} |
| Full Sweep | — | — | {N} | {N} | {N} |
| Solo Pioneer | — | — | — | {N} | {N} |
| Team Topic | — | — | — | — | {N} |
```

All 15 distinct cells must be populated. After the matrix, emit:
`Co-occurrence interpretation: {most or least common co-occurring pair} — {what this implies about team behavior}`

#### 3.4 — Contributor Onboarding Paths

For every topic where `Solo Pioneer` EARNED and `Team Topic` NOT YET:

`Onboarding path — {topic_path}: {contributor} holds solo. Fastest Team Topic unlock: 1 file in {least-covered-namespace or any new namespace} from any new contributor.`

If none: `Onboarding paths: none — no topics with Solo Pioneer EARNED + Team Topic NOT YET.`

**Reconciler Gate**:

- [ ] Reconciliation pairing present with Health observation, Inertia observation, and interaction
- [ ] Flag lifecycle summary present with counts and lists for persistent, new, and resolved flags (or baseline-not-found note)
- [ ] Co-occurrence matrix present with all 15 cells populated and interpretive note
- [ ] Onboarding paths present for all applicable topics (or "none" statement)

**Reconciler Handoff** to Strategist:

1. Reconciliation pairing
2. Flag lifecycle summary
3. Achievement co-occurrence matrix with interpretive note
4. Contributor onboarding paths
5. All Analyst Handoff artifacts (pass-through)

---

### ROLE 4: STRATEGIST

**Responsibility**: Leaderboard, milestone coalition analysis, and milestone regression risk. Does NOT write Team Insight or actions.

#### 4.1 — Contributor Leaderboard

Rank contributors descending by signal count. Ties: alphabetical.

Compute per contributor:
- `rate`: achievements earned / signals (e.g., `0.50`; `--` if signals = 0)
- `cohort`: `specialist` (>= 50% signals in 1 namespace); `generalist` (>= 3 distinct namespaces); `focused` (exactly 2 namespaces)
- `gap_debt`: `9 − distinct_namespaces` (from Archivist's contributor index)

Print: `rank | contributor | signals | topics | achievements | rate | cohort | gap_debt`

If no contributor metadata: one row `| 1 | no contributor metadata found | — | — | — | — | — | — |`

After leaderboard:
- `Namespace leader: {contributor} leads {namespace} with {N} signals` (per active namespace)
- `Solo Pioneer tension:` [cite each onboarding path from Reconciler]
- `Collaboration signal: {N} topics multi-contributor | Highest: {topic} ({N} contributors)`

#### 4.2 — Milestone Coalition Analysis

For each NOT YET milestone, identify internal coalition path (existing contributors) and external path (new contributor needed):

```
## Coalition Analysis
| Milestone | Internal coalition path | External path |
|---|---|---|
| {name} | {contributor} + {topic} + {action} closes {gap} | {topic needing new contributor, or "not needed"} |
```

#### 4.3 — Milestone Regression Risk

For each EARNED milestone, test whether removing any single contributor un-earns it:

- `first team signal`: fragile if the sole contributor with any file is removed; stable otherwise
- `shared coverage`: fragile if removing contributor X drops a qualifying topic below 2 contributors
- `debate starter`: fragile if removing contributor X drops a qualifying topic below 3 contributors

Print: `milestone | status | regression_risk | at_risk_contributor`

`regression_risk` = `stable` or `fragile: {contributor}`. NOT YET milestones: `regression_risk = N/A`.

**Strategist Gate**:

- [ ] Leaderboard present ranked descending; all eight columns populated; cohort label and gap_debt per definition; "no contributor metadata" row if attribution unavailable
- [ ] Coalition analysis for every NOT YET milestone; internal and external paths assessed
- [ ] Regression risk for every EARNED milestone (`stable` or `fragile: {contributor}`); NOT YET milestones show `N/A`

**Strategist Handoff** to Publisher:

1. Contributor leaderboard with all eight columns
2. Namespace leader lines, solo pioneer tension, collaboration signal
3. Coalition analysis table
4. Milestone regression risk table
5. All Reconciler Handoff artifacts (pass-through)

---

### ROLE 5: PUBLISHER

**Responsibility**: Team Insight and actions only. Works from all prior artifacts. Does NOT re-evaluate achievements, re-run analysis, or re-compute any prior section.

#### 5.1 — Team Insight

**Skeptic gate**: A Skeptic who has read all prior output already knows: every achievement status (Health Phase tables), every milestone row (including all per-component deficit breakdowns in proximity ladders and coalition analysis), every inertia flag with lifecycle annotations (`new` / `persistent` / `resolved` / echo-retracted with retraction reasons), every severity tier, trajectory note, stale status, velocity trend, nearest-miss entry (Level 1 and Level 2), contributor leaderboard with `rate`, `cohort`, and `gap_debt` values, every namespace leader, solo pioneer tension line (from onboarding paths), collaboration signal, flag lifecycle summary (persistent/new/resolved counts), co-occurrence matrix with interpretive note, reconciliation pairing, coalition paths, and milestone regression risk assignments. An insight that restates any field from any prior artifact — including any proximity ladder entry, any co-occurrence cell, any coalition path, any regression risk assignment, or the reconciliation interaction — fails. A passing insight surfaces a second-order inference visible only by synthesizing across the lifecycle dimension, the regression risk layer, and the co-occurrence pattern; an inference that none of the five prior roles individually produced.

Write one sentence: (1) a cross-topic conclusion, (2) a concrete number, (3) a specific contributor or topic name.

#### 5.2 — Pre-Write Check

Identify all zero-score conditions. Identify all open (non-echo-retracted) inertia flags. Echo-retracted flags excluded from `resolves:` targeting. Flag `persistent` flags as higher-priority — they resisted one full cycle.

**prevents: prefix rule** (first independent enforcement point): any action eliminating a zero-score condition carries `prevents:`. Advancement actions do not.

Inertia-flag-resolving actions declare `resolves: {exact-flag-name}`.

Actions addressing milestone regression risk note `[stabilizes: {milestone}]`.

#### 5.3 — Next Actions — Multi-Round Sequencing

Group by gap distance:
- **Round 1** — exactly 1 signal or 1 contributor closes the gap (Level 1 nearest-miss or 1-unit proximity ladder entry)
- **Round 2** — 2–3 signals or coordinated additions
- **Round 3** — 4+ signals or multi-contributor coordination

Tier labels by severity: `[CRITICAL]` / `[WARNING]` / `[ADVANCING]`.

Write at least 3 actions across all rounds. Each names specific namespace + topic + exact achievement or milestone name.

**prevents: prefix rule** (second independent enforcement point): embedded in the action template below — zero-score-condition actions carry `prevents:`.

```
## Next Actions

### Round 1 (1 signal closes the gap)
1. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] `{namespace}/{topic}` → unlocks **{exact name}**
   [resolves: {flag}] [closes: {achievement} gap of {N} {unit} for {topic}] [stabilizes: {milestone} or omit]
   [flag_lifecycle: persistent/new — if targeting an inertia flag]

### Round 2 (2–3 signals needed)
2. ...

### Round 3 (4+ signals or coordination)
3. ...
```

If no actions exist for a round: `Round {N}: no actions at this gap distance.`

After all actions: `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions`

#### 5.4 — Insight Falsifiability Contract

Append to the Team Insight:

```
[holds if: {specific observable condition — must name a topic, contributor, or metric threshold}]
[falsified by: {specific observable condition that would invalidate the insight}]
```

Vague conditions ("holds if things continue", "falsified if the situation changes") fail. Conditions must name specific entities — a topic path, contributor name, or numeric metric threshold.

**Publisher Gate**:

- [ ] Team Insight: one sentence; Skeptic gate verified — no restatement of any field from any prior artifact, proximity ladder entry, co-occurrence cell, coalition path, regression risk assignment, or reconciliation interaction; cross-topic inference with concrete number and specific name; Skeptic's known context explicitly includes flag lifecycle annotations, co-occurrence matrix, coalition paths, and milestone regression risk
- [ ] Insight falsifiability contract appended with entity-specific `holds if` and `falsified by` conditions
- [ ] Pre-write check complete; zero-score conditions identified; echo-retracted flags excluded; persistent flags noted as higher-priority
- [ ] Actions in Round 1 / Round 2 / Round 3 structure; empty rounds stated explicitly; at least 3 total; tiers match topic severity; each names namespace + topic + exact name; `resolves:` on open flag-resolving actions; `closes:` binding present; `stabilizes:` on regression-risk-addressing actions; `flag_lifecycle: persistent` on persistent-flag actions; `prevents:` at two independent locations (§5.2 and §5.3)
- [ ] ACTIONS GATE line with actual N substituted

---

## Summary Table

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **Axis** | Phrasing register | Output format | Role sequence | Combination | Full integration |
| **Roles** | 3 | 3 | 4 | 4 | 5 |
| **New seed** | AA (gap_debt) | Z (co-occurrence matrix) | Y (flag lifecycle) | AB (regression risk) | Y+Z+AA+AB+AC |
| **R15 seeds** | A+B+H+N+S+U | A+B+H+N+S+V | A+B+H+N+S+T | A+B+H+K+M+N+S+W | All |
| **Register** | Narrative briefing | Schema blocks | Field tables | Field tables | Field tables + schema |
| **Action grouping** | Flat (3+ minimum) | Round 1/2/3 | Flat (3+ minimum) | CRITICAL/WARNING/ADVANCING | Round 1/2/3 + tiers |
| **v12 expected** | 25/25 → 100.00 | 25/25 → 100.00 | 25/25 → 100.00 | 25/25 → 100.00 | 25/25 → 100.00 |

**Seeds entering R17** (candidates for new rubric criteria):
- **Seed Y (flag lifecycle)**: `new`/`persistent`/`resolved` annotation on inertia flags using a baseline comparison. Persistent flags warrant priority. Potential C-34.
- **Seed Z (co-occurrence matrix)**: 5×5 achievement pair count table with interpretive note. Reveals structural coupling in team behavior. Potential C-35.
- **Seed AA (namespace gap debt)**: `gap_debt = 9 − distinct_namespaces` leaderboard column. Surfaces unexplored breadth opportunity per contributor. Potential C-36.
- **Seed AB (milestone regression risk)**: Per-EARNED-milestone `stable` / `fragile: {contributor}` assessment. Completes milestone lifecycle alongside proximity ladders. Potential C-37.
- **Seed AC (onboarding path)**: Per-Solo-Pioneer-EARNED topic: explicit path to Team Topic naming topic, contributor, and fastest namespace. Potential C-38.
