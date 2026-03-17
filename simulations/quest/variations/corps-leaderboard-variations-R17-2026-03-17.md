Written to `simulations/quest/variations/corps-leaderboard-variations-R17-2026-03-17.md` (1597 lines).

---

## Variate R17 — corps-leaderboard

**Round mandate**: Universalize C-34, C-35, C-36 across all five variations — the three criteria that held V-01 through V-04 at 98.93 in R16.

### Variation axes

| | Axis | Roles | C-35 mechanism | New seed |
|--|------|-------|----------------|----------|
| **V-01** | Phrasing register (conversational advisory) | 3 | Publisher §3.0 Inspector phase | AD — Rate Tier Stratification (`high-converter / mid-converter / low-converter`) |
| **V-02** | Output format (`::SCHEMA::` blocks throughout) | 3 | Publisher §3.0 Inspector phase | AE — Echo Contributor Detection (contributor-pair overlap table) |
| **V-03** | Role sequence (dedicated Inspector as ROLE 3) | 4 | Dedicated ROLE 3: Inspector | AF — Achievement Readiness Score per topic (ARS = earned/5, ranked ascending) |
| **V-04** | Combination (tiered + coalition + regression + momentum) | 4 | Strategist §3.0 Inspector sub-phase | AG — Namespace Momentum Vector (active/stalled per namespace) |
| **V-05** | Full integration | 5 | Dedicated ROLE 4: Inspector | AD+AE+AF+AG+AH — Cross-Namespace Pairing Pattern (top-3/bottom-3 co-occurring pairs) |

### Universal changes from R16

All 5 variations now carry:
- **C-34**: Falsifiability contract (`[holds if:]` / `[falsified by:]`) appended to every Team Insight
- **C-35**: An Inspector phase in a role structurally separate from the Analyst (Publisher in 3-role; dedicated role in 4/5-role)
- **C-36**: 2D Round × Tier matrix — every action row indexed by BOTH Round 1/2/3 (gap distance) AND `[CRITICAL]`/`[WARNING]`/`[ADVANCING]` (severity tier)
- Seeds Y+Z+AA+AB+AC universalized (were selective in R16)

### Seeds entering R18 (candidates C-37 through C-41)

- **C-37 candidate**: Seed AD — rate tier distribution (volume × conversion as independent risk axes)
- **C-38 candidate**: Seed AE — echo contributor table (redundant coverage patterns)
- **C-39 candidate**: Seed AF — ARS per-topic priority list (orthogonal to severity tiers)
- **C-40 candidate**: Seed AG — namespace momentum vector (active vs stalled)
- **C-41 candidate**: Seed AH — cross-namespace pairing (structural workflow break detection)

**Expected scoring**: All 5 variations → 28/28 → **100.00**
eed AC: Contributor onboarding paths (per Solo Pioneer EARNED + Team Topic NOT YET) -- **universalized in R17**

**New seeds introduced in R17**:
- **Seed AD**: Rate Tier Stratification -- classify each contributor as `high-converter` (rate >= 0.50), `mid-converter` (rate 0.25-0.49), or `low-converter` (rate < 0.25). Print a Rate Tier Distribution Summary: `high: {N} | mid: {N} | low: {N}`. A team of all low-converters with high volume signals breadth without depth; a high-converter with few signals may be over-achieving on easy topics. Creates a 2D reading: volume x conversion rate as independent risk axes.
- **Seed AE**: Echo Contributor Detection -- identify any two contributors whose covered `{topic_path, namespace}` pairs overlap >= 80%. Print an Echo Contributor Table: `contributor_A | contributor_B | shared_pairs | total_union | overlap_pct | echo_classification`. `echo_classification`: `full-echo` (100%), `partial-echo` (>= 80%), `independent` (< 80%). Full-echo pairs are flagged in the action section: adding signals in the same pattern extends echo rather than diversity.
- **Seed AF**: Achievement Readiness Score per topic -- `ARS = earned_achievements / 5`. Print a ranked ARS table: `rank | topic_path | earned | ARS | intervention_priority` sorted ascending by ARS. `intervention_priority`: `immediate` (0.00), `high` (0.20-0.39), `medium` (0.40-0.59), `low` (0.60-0.79), `minimal` (0.80-1.00). Produces a topic-level intervention priority list distinct from the inertia severity tier.
- **Seed AG**: Namespace Momentum Vector -- for each active namespace, print: `namespace | last_contributor | last_signal_recency | momentum`. `momentum` = `active` if last signal file is within the most recent 25% of all files by modification order, else `stalled`. Surfaces namespaces with historic coverage but no recent investment.
- **Seed AH**: Cross-Namespace Pairing Pattern -- count how many topics have signals in BOTH namespace A and namespace B. Print top-3 co-occurring pairs and bottom-3 (least co-occurring). Top pairs reveal the team's natural sequencing; bottom pairs reveal where the team never follows through from one namespace to another.

**R17 design targets**:

| Variation | Roles | Architecture | New seed | Axis |
|-----------|-------|--------------|----------|------|
| V-01 | 3 | Archivist -> Analyst -> Publisher (Publisher ss3.0 Inspector) | AD (rate tier) | Phrasing register (conversational advisory) |
| V-02 | 3 | Archivist -> Analyst -> Publisher (Publisher ss3.0 Inspector) | AE (echo contributor) | Output format (schema blocks) |
| V-03 | 4 | Archivist -> Analyst -> Inspector -> Publisher | AF (ARS per topic) | Role sequence (dedicated Inspector) |
| V-04 | 4 | Archivist -> Analyst -> Strategist -> Publisher (Strategist ss3.0 Inspector) | AG (namespace momentum) | Combination (tiered + coalition + regression + momentum) |
| V-05 | 5 | Archivist -> Analyst -> Reconciler -> Inspector -> Publisher | AD+AE+AF+AG+AH | Full integration |

**Expected scoring against v13** (formula: `90 + (passed/28) x 10`):
- V-01 through V-05: 28/28 -> **100.00**

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Phrasing register (conversational advisory -- stakeholder-addressed advisory prose) | V-01 |
| Output format (schema `::BLOCK::` delimiters throughout all phases) | V-02 |
| Role sequence (dedicated Inspector ROLE 3 between Analyst and Publisher) | V-03 |
| Combination: tiered + coalition + regression risk + namespace momentum | V-04 |
| Full integration: 5-role + all R15+R16+R17 seeds | V-05 |

---

## V-01 -- Conversational Advisory Register + 3-Role + Publisher Inspector Phase + All R16 Seeds + Seed AD

**Axis**: Phrasing register
**Hypothesis**: R16 V-01 used narrative briefing blocks -- editorial, third-person. This variation shifts to a **conversational advisory** register: each health block addresses the team directly ("Your team has one contributor covering this topic -- adding a second signal from a different person unlocks Team Topic"). Advisory language surfaces the actionable interpretation at briefing time, reducing cognitive distance between observation and response. The Publisher (ROLE 3) performs the Inspector Discrepancy Check in ss3.0 before any synthesis -- satisfying C-35 as a role structurally distinct from the Analyst (ROLE 2). The falsifiability contract (Seed X) satisfies C-34. The 2D Round x Tier action matrix satisfies C-36. New: Seed AD (rate tier stratification) in the leaderboard.

---

You are running the **Corps Leaderboard** skill in a **3-role pipeline**: Archivist -> Analyst -> Publisher. Execute each role completely before advancing. No role may perform work assigned to another. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: Within the Analyst role, the Inertia Phase (ss2.1) runs BEFORE the Health Phase (ss2.2). Health Phase topics report in descending severity order: critical first, then warning, then healthy. Alphabetical within each tier. The Publisher opens with an Inspector sub-phase (ss3.0) that checks the Analyst's flag assignments against Health Phase data before any synthesis work begins.

---

### ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Does NOT evaluate achievements, assess trajectory, rank contributors, or write insights or actions.

#### 1.1 -- Signal File Scan

Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` -- path segment after `simulations/` (e.g., `scout/competitors`)
- `namespace` -- first path segment of `topic_path` (e.g., `scout`)
- `contributor` -- resolve: frontmatter `author:` > `contributor:` > filename prefix before first `-` > `unknown`
- `file` -- full relative path

**Empty-workspace halt**: If zero files match, write `REGISTRY: empty -- no signal files found in simulations/` and stop. Roles 2 and 3 do not run.

Print registry as table: `topic_path | namespace | contributor | file`

After the registry, print:
`Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`

The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

**Baseline check**: Attempt to read `simulations/.leaderboard-baseline.md`. Extract prior inertia flag table (columns: `topic_path`, `flags`) if present.
Print: `Baseline found: {row count} topic entries` or `Baseline not found: flag lifecycle will mark all flags as new`.

#### 1.2 -- Contributor Index

For each contributor, record: `contributor | distinct_namespaces | topic_paths | file_count`

The `distinct_namespaces` count is the number of unique namespaces across this contributor's signal files.

**Archivist Gate**:

- [ ] Registry table with all four columns
- [ ] Namespace coverage line with active and empty lists
- [ ] Contributor index with `distinct_namespaces` column per contributor
- [ ] Baseline status line present

**Archivist Handoff** to Analyst:

1. Signal registry table
2. Namespace coverage line
3. Contributor index
4. Prior inertia flag table from baseline (or `baseline: none`)

---

### ROLE 2: ANALYST

**Responsibility**: Evaluation only. Inertia Phase with lifecycle (ss2.1) first, then Health Phase (ss2.2), then Nearest-Miss (ss2.3), then Echo Detection (ss2.4). Structurally separated phases. Does NOT perform discrepancy checks, rank contributors, write insights, or write actions.

#### 2.1 -- Inertia Phase (RUNS FIRST -- with flag lifecycle annotation)

Reports trajectory and momentum only. Does NOT include file counts, achievement statuses, or coverage totals.

| Inertia Flag | Condition |
|---|---|
| `stuck-at-first` | exactly 1 file; Signal Depth not earned |
| `solo-hold` | exactly 1 contributor; no second contributor present |
| `namespace-thin` | all files in 1 namespace; Full Sweep not earned |
| `healthy-momentum` | Signal Depth earned AND >= 2 distinct contributors |

Assign severity per topic:
- `critical` -- 2 or more non-momentum flags raised
- `warning` -- exactly 1 non-momentum flag raised
- `healthy` -- 0 non-momentum flags, or only `healthy-momentum`

**Flag lifecycle annotation** against baseline:
- `new` -- flag present now; absent in baseline (or no baseline)
- `persistent` -- flag present in both baseline and current run
- `resolved` -- flag in baseline; NOT present in current run (list separately)

Print inertia table: `topic_path | flags_raised(lifecycle) | trajectory note | severity`

Format: `stuck-at-first(persistent), solo-hold(new)`. No flags: `none`.

List resolved flags: `resolved since baseline: {topic_path}: {flag-name}` (one line per; omit if no baseline or none resolved).

Print stale signal table: `topic_path | stale_status` (`stale` / `active` / `date-unknown`)

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`
Classification: > 50% healthy = increasing; < 25% = stalled; otherwise flat.

**Section 2.1 Gate**:

- [ ] Inertia table with `flags_raised(lifecycle)` column; all four flags evaluated; lifecycle annotation per raised flag
- [ ] No file counts, achievement statuses, or coverage totals in ss2.1
- [ ] Resolved flags section present (or noted as omitted)
- [ ] Stale signal table and velocity summary present

#### 2.2 -- Health Phase (RUNS SECOND -- conversational advisory, severity order: critical -> warning -> healthy)

Reports current signal state only. Does NOT include trajectory claims, momentum language, or flag names.

**Topic ordering**: critical first, then warning, then healthy. Alphabetical within each tier.

For each `topic_path` (in severity order), write a **conversational advisory block** addressing the team:

```
### Advisory: {topic_path} [severity: {critical/warning/healthy}]
Coverage: {N} signal file(s) across {M} namespace(s). Contributors active: {list}. Namespace diversity: {N}/9.

{1-3 sentences in advisory register -- address the team directly about what they have, what is missing,
and what specific action would change the picture. Do NOT name inertia flags or use trajectory language.}

Achievements:
  - **First Signal**: {EARNED -- {evidence}} / {LOCKED -- add at least 1 signal file}
  - **Signal Depth**: {EARNED -- {evidence}} / {LOCKED -- add {X} more file(s) to reach 3}
  - **Full Sweep**: {EARNED -- {evidence}} / {LOCKED -- add signals in {X} more namespace(s)}
  - **Solo Pioneer**: {EARNED -- {evidence}} / {LOCKED -- needs exactly 1 contributor with >= 1 file}
  - **Team Topic**: {EARNED -- {evidence}} / {LOCKED -- add {X} more contributor(s) each with >= 1 file}
```

Achievement names must be exact. Every LOCKED achievement states the specific unlock requirement inline.

When `Solo Pioneer` EARNED and `Team Topic` NOT YET: `[TENSION: solo hold -- 1 additional contributor with >= 1 signal unlocks Team Topic]`

After all topic blocks, evaluate all three team milestones using exact names:

| Milestone | Status | Evidence |
|---|---|---|
| `first team signal` | EARNED/NOT YET | {non-empty} |
| `shared coverage` | EARNED/NOT YET | {non-empty} |
| `debate starter` | EARNED/NOT YET | {non-empty} |

For every NOT YET milestone, print a **Milestone Proximity Ladder** immediately below its row:

- `first team signal` NOT YET: `Proximity ladder: 1 signal file in any namespace for any topic closes this milestone.`
- `shared coverage` NOT YET: `Proximity ladder: {N} qualifying topics (need 2). Per-topic contributor deficit: {topic_A} needs {M} more contributor(s); {topic_B} needs {M} more. [list every candidate individually]`
- `debate starter` NOT YET: `Proximity ladder: nearest topic is {path} at {N}/3 contributors. {M} more distinct contributor signal(s) close this gap.`

EARNED milestones do not receive a proximity ladder.

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`
Print namespace leader table: `namespace | leader | signal_count` for each active namespace.

#### 2.3 -- Nearest-Miss Assessment

**Level 1** -- every topic exactly 1 unit from any achievement threshold. Print: `topic | achievement | gap | level`, ascending.

**Level 2** -- closest 2-unit candidate per type; ONLY when no Level 1 candidate for that type. State `Level 1: no topics are 1 unit away` explicitly before any Level 2 entry.

#### 2.4 -- Echo Detection

**Rule A** -- `healthy-momentum` raised AND `Solo Pioneer` EARNED: logically incompatible. Retract `healthy-momentum`.
`ECHO RETRACTION: healthy-momentum on {topic_path} retracted -- incompatible with Solo Pioneer EARNED (requires exactly 1 contributor).`

**Rule B** -- Any inertia flag raised AND `First Signal` LOCKED: retract flag.
`ECHO RETRACTION: {flag-name} on {topic_path} retracted -- First Signal LOCKED; no files to evaluate.`

```
## Echo Detection Table
| topic_path | Rule violated | Flag retracted | Achievement | Resolution |
|---|---|---|---|---|
```

No violations: one row `| none | -- | -- | -- | -- |`.

**Section 2.2-2.4 Gate**:

- [ ] Topics in severity order; all five achievement names exact and bold; LOCKED achievements include specific unlock requirements; no flag names or trajectory language in advisory prose
- [ ] Contamination check: advisory blocks contain no trajectory claims; Inertia Phase table contains no file counts or achievement statuses
- [ ] All three milestone exact names with non-empty evidence; proximity ladders for ALL NOT YET milestones with per-topic deficit breakdowns
- [ ] Nearest-miss Level 1 ascending; Level 2 with "Level 1: no topics are 1 unit away" before Level 2
- [ ] Echo Detection Table; Rules A+B checked; retraction statements for violations; "none" row if clean

**Analyst Handoff** to Publisher:

1. Inertia Phase table (`topic_path`, `flags_raised(lifecycle)`, `trajectory note`, `severity`)
2. Resolved flags list and baseline status
3. Stale signal table and velocity summary
4. Per-topic Health Phase advisory blocks in severity order
5. Team milestone table with proximity ladders for NOT YET milestones
6. Debate starter proximity line and namespace leader table
7. Nearest-miss table (`topic`, `achievement`, `gap`, `level`)
8. Echo Detection Table with retraction statements

---

### ROLE 3: PUBLISHER

**Responsibility**: Inspector Discrepancy Check (ss3.0), leaderboard and synthesis (ss3.1-ss3.3), Team Insight with falsifiability contract (ss3.4), and actions (ss3.5-ss3.6). Does NOT re-scan the workspace or re-evaluate achievements.

#### 3.0 -- Inspector Discrepancy Check (RUNS BEFORE ALL OTHER PUBLISHER SECTIONS)

The Publisher is a structurally distinct role from the Analyst (who assigned inertia flags). Before performing any synthesis, the Publisher performs an adversarial empirical check: compare the Analyst's flag assignments against Health Phase data to catch flags raised but contradicted by actual signal data.

For each topic with raised flags, check:

| Flag | Contradiction if Health Phase shows |
|---|---|
| `stuck-at-first` | Signal Depth: EARNED |
| `solo-hold` | >= 2 distinct contributors |
| `namespace-thin` | Full Sweep: EARNED |

Emit a discrepancy retraction for each contradiction found:
`DISCREPANCY RETRACTION: {flag-name} on {topic_path} retracted -- Health Phase shows {contradicting evidence}. Flag assignment was inconsistent with signal data.`

```
## Discrepancy Table
| topic_path | Flag raised | Health Phase evidence | Contradiction? | Disposition |
|---|---|---|---|---|
```

No contradictions: one row `| none | -- | -- | no | -- |`.

Emit effective flag list:
`Effective open flags: {list of topic:flag pairs}` (Analyst flags minus echo-retracted minus discrepancy-retracted)

**Inspector Gate**:

- [ ] Discrepancy Table present; every raised flag in Analyst's inertia table checked against Health Phase data
- [ ] Retraction statements for each contradiction; "none" row if clean
- [ ] Effective open flag list printed

#### 3.1 -- Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical.

Per contributor:
- `rate`: `achievements_earned / signals` (e.g., `0.50`; `--` if 0 signals)
- `rate_tier`: `high-converter` (rate >= 0.50), `mid-converter` (0.25-0.49), `low-converter` (< 0.25), `--` if no signals
- `cohort`: `specialist` (>= 50% signals in 1 namespace), `generalist` (>= 3 namespaces), `focused` (2 namespaces)
- `gap_debt`: `9 - distinct_namespaces`

If all contributors `unknown`: one row `| 1 | no contributor metadata found | -- | -- | -- | -- | -- | -- |`.

Print: `rank | contributor | signals | topics | rate | rate_tier | cohort | gap_debt`

After leaderboard:
- **Rate Tier Distribution**: `high-converter: {N} | mid-converter: {N} | low-converter: {N}`
- `Namespace leader: {contributor} leads {namespace} with {N} signals` (per active namespace)
- `Solo Pioneer tension: [per Solo Pioneer EARNED + Team Topic NOT YET] {topic_path} -- {contributor} holds solo; 1 new contributor unlocks Team Topic`
- `Collaboration signal: {N} topic(s) multi-contributor | Highest: {topic} ({N} contributors)`

#### 3.2 -- Achievement Co-Occurrence Matrix

```
## Achievement Co-Occurrence Matrix
|   | First Signal | Signal Depth | Full Sweep | Solo Pioneer | Team Topic |
|---|---|---|---|---|---|
| First Signal | {N} | {N} | {N} | {N} | {N} |
| Signal Depth | -- | {N} | {N} | {N} | {N} |
| Full Sweep   | -- | -- | {N} | {N} | {N} |
| Solo Pioneer | -- | -- | -- | {N} | {N} |
| Team Topic   | -- | -- | -- | -- | {N} |
```

All 15 distinct cells populated. `Co-occurrence interpretation: {pair} -- {team behavior implication}`

#### 3.3 -- Cross-Dimensional Reconciliation + Regression Risk + Coalition + Onboarding

**Reconciliation**:
```
## Reconciliation
| Health observation | Inertia observation | Interaction |
|---|---|---|
| {finding} | {finding} | {connection} |
```

**Milestone regression risk**:
Print: `milestone | status | regression_risk | at_risk_contributor`
`regression_risk` = `stable` or `fragile: {contributor}`. NOT YET: `N/A`.

**Coalition analysis** (per NOT YET milestone):
```
## Coalition Analysis
| Milestone | Internal path | External path |
|---|---|---|
```

**Contributor onboarding paths**: Per Solo Pioneer EARNED + Team Topic NOT YET:
`Onboarding path -- {topic_path}: {contributor} holds solo. Fastest unlock: 1 file in {namespace} from any new contributor.`
If none: `Onboarding paths: none.`

#### 3.4 -- Team Insight + Falsifiability Contract

**Skeptic gate**: A Skeptic who has read all prior output already knows: every achievement status (advisory blocks), every milestone row (including all proximity ladder per-topic deficit breakdowns), every inertia flag with lifecycle annotations (new, persistent, resolved, echo-retracted, and discrepancy-retracted with reasons), every severity tier, trajectory note, stale status, velocity summary, nearest-miss entries, leaderboard columns (rate, rate_tier, cohort, gap_debt), rate tier distribution, namespace leaders, solo pioneer tension, collaboration signal, co-occurrence matrix with interpretive note, reconciliation pairing, regression risk assignments, coalition paths, and contributor onboarding paths. An insight restating any field fails. A passing insight surfaces a second-order pattern requiring synthesis across at least two distinct analysis layers simultaneously.

Write one Team Insight sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor or topic name.

Append:
```
[holds if: {specific observable condition -- must name a topic path, contributor, or numeric threshold}]
[falsified by: {specific observable condition -- must name a topic path, contributor, or numeric threshold}]
```

#### 3.5 -- Pre-Write Check

Effective open flags from ss3.0. Zero-score conditions identified.

**prevents: prefix rule** (first of two independent enforcement points): zero-score condition actions carry `prevents:`.

Effective open flag-resolving actions declare `resolves: {exact-flag-name}`.

#### 3.6 -- Next Actions -- 2D Round x Tier Matrix

Both Round (gap distance) AND Tier (severity) present simultaneously per action row.

- Round 1: 1 signal or 1 contributor closes the gap
- Round 2: 2-3 signals or coordinated additions
- Round 3: 4+ signals or multi-contributor coordination
- Tier: `[CRITICAL]`, `[WARNING]`, `[ADVANCING]`

```
## Next Actions

### Round 1 (1 signal closes the gap)
1. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] `{namespace}/{topic}` -> unlocks **{exact name}**
   [resolves: {flag}] [closes: {achievement} gap of {N} {unit} for {topic}] [flag_lifecycle: persistent/new]

### Round 2 (2-3 signals needed)
2. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] `{namespace}/{topic}` -> unlocks **{exact name}**

### Round 3 (4+ signals or coordination)
3. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] `{namespace}/{topic}` -> unlocks **{exact name}**
```

Empty rounds: `Round {N}: no actions at this gap distance.`

**prevents: prefix rule** (second of two independent enforcement points): in the action template -- zero-score-condition actions carry `prevents:`.

`ACTIONS GATE: prevents: prefix used for {N} zero-score conditions`

**Publisher Gate**:

- [ ] Discrepancy Table (ss3.0) present; every raised flag checked; retraction statements; "none" row if clean; effective open flag list present
- [ ] Leaderboard: all eight columns; rate tier distribution present
- [ ] Co-occurrence matrix (all 15 cells), reconciliation pairing, regression risk, coalition analysis, onboarding paths present
- [ ] Team Insight one sentence; Skeptic gate verified; falsifiability contract with entity-specific conditions
- [ ] Pre-Write Check identifies zero-score conditions; effective open flags only for `resolves:`
- [ ] Actions in Round x Tier 2D structure; at least 3; each names namespace + topic + exact name; `prevents:` at two independent locations (ss3.5 and ss3.6)
- [ ] ACTIONS GATE with actual N

---

## V-02 -- Schema Block Format + 3-Role + Publisher Inspector Phase + All R16 Seeds + Seed AE

**Axis**: Output format
**Hypothesis**: Every phase emits structured `::SCHEMA:: / ::END::` blocks with explicit named fields rather than prose or markdown tables. Schema blocks force completeness: every declared field must be populated; missing fields are visible as gaps rather than hidden in prose. The Publisher (ROLE 3) performs the Inspector Discrepancy Check (ss3.0) -- satisfying C-35 as a role distinct from the Analyst. New: Seed AE (echo contributor detection) reveals contributor-level redundancy invisible to signal count. C-34 (falsifiability) and C-36 (2D action matrix) carried in Publisher.

---

You are running the **Corps Leaderboard** skill in a **3-role pipeline**: Archivist -> Analyst -> Publisher. Execute each role completely before advancing. No role may perform work assigned to another. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: The Analyst runs Inertia Phase (with flag lifecycle) before Health Phase. Health Phase uses severity order (critical -> warning -> healthy), alphabetical within tier. The Publisher opens with an Inspector Discrepancy Check (ss3.0). Every phase output uses `::SCHEMA::` / `::END::` block format throughout.

---

### ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Does NOT evaluate achievements, rank contributors, or write insights or actions.

Glob `simulations/**/*.md`. Zero matches: emit `::REGISTRY:: status: empty reason: no signal files found ::END::` and stop.

For each matching file:
```
::REGISTRY_ENTRY::
topic_path: {value}
namespace: {value}
contributor: {author: > contributor: > filename-prefix > unknown}
file: {full relative path}
::END::
```

After all entries:
```
::NAMESPACE_COVERAGE::
active_count: {N}
total: 9
active: {comma-separated list}
empty: {comma-separated list}
namespaces_reference: scout, draft, review, flow, trace, prove, listen, program, topic
::END::
```

Baseline check:
```
::BASELINE_STATUS::
found: {true/false}
topic_entries: {count or 0}
note: {Baseline found: N entries / Baseline not found: all flags marked new}
::END::
```

Per contributor:
```
::CONTRIBUTOR_ENTRY::
contributor: {value}
distinct_namespaces: {N}
file_count: {N}
topic_paths: {comma-separated}
::END::
```

**Archivist Gate**:

- [ ] `::REGISTRY_ENTRY::` blocks for every file (or empty block)
- [ ] `::NAMESPACE_COVERAGE::` with all five fields
- [ ] `::BASELINE_STATUS::` block present
- [ ] `::CONTRIBUTOR_ENTRY::` blocks with all four fields

**Archivist Handoff** to Analyst: all blocks above.

---

### ROLE 2: ANALYST

**Responsibility**: Evaluation only. Inertia Phase with lifecycle (ss2.1) first, Health Phase in severity order (ss2.2), Nearest-Miss (ss2.3), Echo Detection (ss2.4). Does NOT perform discrepancy checks, detect echo contributors, or write insights or actions.

#### 2.1 -- Inertia Phase (RUNS FIRST)

Trajectory and flag lifecycle only. No file counts, achievement statuses, or coverage totals.

Flags: `stuck-at-first` (1 file, SD not earned), `solo-hold` (1 contributor), `namespace-thin` (1 namespace, FS not earned), `healthy-momentum` (SD earned AND >= 2 contributors).
Severity: `critical` = 2+ non-momentum; `warning` = 1; `healthy` = 0.
Lifecycle: `new` / `persistent` / `resolved` against baseline.

```
::INERTIA::
topic_path: {value}
flags_raised: {flag(lifecycle), ... or "none"}
trajectory_note: {one-line}
severity: {critical/warning/healthy}
::END::
```

```
::RESOLVED_FLAGS::
resolved: {topic:flag, ... or "none"}
::END::
```

```
::STALE_CHECK::
topic_path: {value}
stale_status: {stale/active/date-unknown}
::END::
```
(one per topic)

```
::VELOCITY::
signal_count: {N}
topic_count: {N}
healthy: {N}
warning: {N}
critical: {N}
trend: {increasing/flat/stalled}
::END::
```

**Section 2.1 Gate**:
- [ ] `::INERTIA::` blocks with lifecycle notation per flag; no file counts or achievement statuses
- [ ] `::RESOLVED_FLAGS::`, `::STALE_CHECK::` blocks, and `::VELOCITY::` present

#### 2.2 -- Health Phase (schema blocks, severity order: critical -> warning -> healthy)

Current state only. No trajectory claims or flag names.

```
::TOPIC_HEALTH::
topic_path: {value}
severity: {critical/warning/healthy}
files: {N}
namespaces_active: {list}
contributors: {list}
namespace_diversity: {N}/9
::END::

::ACHIEVEMENTS::
topic_path: {value}
First_Signal: {EARNED -- {evidence} / LOCKED -- needs >= 1 file}
Signal_Depth: {EARNED -- {evidence} / LOCKED -- needs {X} more files}
Full_Sweep: {EARNED -- {evidence} / LOCKED -- needs {X} more namespaces}
Solo_Pioneer: {EARNED -- {evidence} / LOCKED -- needs exactly 1 contributor >= 1 file}
Team_Topic: {EARNED -- {evidence} / LOCKED -- needs {X} more contributors}
tension: {[TENSION: solo hold -- 1 additional contributor unlocks Team Topic] or "none"}
::END::
```

```
::TEAM_MILESTONES::
first_team_signal_status: {EARNED/NOT YET}
first_team_signal_evidence: {non-empty}
first_team_signal_ladder: {Proximity ladder text or "N/A -- EARNED"}
shared_coverage_status: {EARNED/NOT YET}
shared_coverage_evidence: {non-empty}
shared_coverage_ladder: {Proximity ladder: N qualifying (need 2). Per-topic deficit: topic_A needs M; ... or "N/A -- EARNED"}
debate_starter_status: {EARNED/NOT YET}
debate_starter_evidence: {non-empty}
debate_starter_ladder: {Proximity ladder: nearest {path} at {N}/3. {M} more needed. or "N/A -- EARNED"}
debate_starter_line: Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)
::END::
```

```
::NAMESPACE_LEADER::
namespace: {value}
leader: {contributor}
signal_count: {N}
::END::
```
(per active namespace)

#### 2.3 -- Nearest-Miss Assessment

```
::NEAREST_MISS::
topic: {value}
achievement: {exact name}
gap: {N}
level: {1 or 2}
level2_note: {Level 1: no topics are 1 unit away -- if level 2, else empty}
::END::
```

#### 2.4 -- Echo Detection

```
::ECHO_DETECTION::
topic_path: {value}
rule: {A / B / none}
flag_retracted: {name or "--"}
achievement: {name or "--"}
resolution: {retraction statement or "--"}
::END::
```

**Section 2.2-2.4 Gate**:
- [ ] `::TOPIC_HEALTH::` and `::ACHIEVEMENTS::` blocks in severity order; all five achievement names exact; LOCKED fields with specific unlock paths; no trajectory language; contamination check passed
- [ ] `::TEAM_MILESTONES::` with proximity ladders for all NOT YET milestones
- [ ] `::NAMESPACE_LEADER::` blocks for all active namespaces
- [ ] `::NEAREST_MISS::` blocks (Level 1; Level 2 with level2_note)
- [ ] `::ECHO_DETECTION::` blocks; Rules A+B checked

**Analyst Handoff** to Publisher: all blocks above.

---

### ROLE 3: PUBLISHER

**Responsibility**: Inspector Discrepancy Check (ss3.0), leaderboard and echo contributor analysis (ss3.1-ss3.2), supplementary analysis (ss3.3), Team Insight with falsifiability contract (ss3.4), and actions (ss3.5-ss3.6).

#### 3.0 -- Inspector Discrepancy Check (RUNS FIRST)

Publisher is structurally distinct from Analyst. Compare each `::INERTIA::` flag against `::ACHIEVEMENTS::` data:

| Flag | Contradiction if |
|---|---|
| `stuck-at-first` | Signal_Depth: EARNED |
| `solo-hold` | >= 2 contributors in `::TOPIC_HEALTH::` |
| `namespace-thin` | Full_Sweep: EARNED |

```
::DISCREPANCY_CHECK::
topic_path: {value}
flag_checked: {name or "none raised"}
health_evidence: {relevant field and value}
contradiction: {yes/no}
action: {DISCREPANCY RETRACTION: ... / "no action"}
::END::
```

```
::EFFECTIVE_FLAGS::
open_flags: {topic:flag pairs after echo and discrepancy retractions}
excluded_echo: {list or "none"}
excluded_discrepancy: {list or "none"}
::END::
```

**Inspector Gate**:
- [ ] `::DISCREPANCY_CHECK::` blocks for all flagged topics; retraction statements for contradictions
- [ ] `::EFFECTIVE_FLAGS::` block present

#### 3.1 -- Contributor Leaderboard

```
::LEADERBOARD_ENTRY::
rank: {N}
contributor: {value}
signals: {N}
topics: {N}
achievements: {N}
rate: {value or "--"}
rate_tier: {high-converter/mid-converter/low-converter/"--"}
cohort: {specialist/generalist/focused}
gap_debt: {9 - distinct_namespaces}
::END::
```

```
::RATE_TIER_DISTRIBUTION::
high_converter: {N}
mid_converter: {N}
low_converter: {N}
interpretation: {team-level note}
::END::
```

```
::NAMESPACE_LEADER::
namespace: {value}
leader: {contributor}
signal_count: {N}
::END::
```

```
::COLLABORATION_SIGNAL::
multi_contributor_topics: {N}
highest_topic: {path}
highest_contributors: {N}
tensions: {topic:contributor pairs where SP EARNED + TT NOT YET, or "none"}
::END::
```

#### 3.2 -- Echo Contributor Detection

For each contributor pair, compute `{topic_path, namespace}` covered pair overlap:

```
::ECHO_CONTRIBUTOR_CHECK::
contributor_A: {value}
contributor_B: {value}
shared_pairs: {N}
total_union: {N}
overlap_pct: {N%}
echo_classification: {full-echo/partial-echo/independent}
::END::
```

Single contributor: `::ECHO_CONTRIBUTOR_CHECK:: note: single contributor -- not applicable ::END::`.

`Echo summary: {N} full-echo, {N} partial-echo, {N} independent.`
`Echo risk: {advisory note or "none"}`

#### 3.3 -- Supplementary Analysis

```
::RECONCILIATION::
health_observation: {finding}
inertia_observation: {finding}
interaction: {connection}
::END::
```

Co-occurrence matrix (table within fenced block; all 15 cells populated):
```
## Achievement Co-Occurrence Matrix
|   | First Signal | Signal Depth | Full Sweep | Solo Pioneer | Team Topic |
|---|---|---|---|---|---|
| First Signal | {N} | {N} | {N} | {N} | {N} |
| Signal Depth | -- | {N} | {N} | {N} | {N} |
| Full Sweep   | -- | -- | {N} | {N} | {N} |
| Solo Pioneer | -- | -- | -- | {N} | {N} |
| Team Topic   | -- | -- | -- | -- | {N} |
```
`Co-occurrence interpretation: {pair} -- {implication}`

```
::REGRESSION_RISK::
milestone: {name}
status: {EARNED/NOT YET}
regression_risk: {stable / fragile:{contributor} / N/A}
at_risk_contributor: {name or "--"}
::END::
```
(per milestone)

```
::COALITION_ANALYSIS::
milestone: {name}
internal_path: {contributor + topic + action}
external_path: {topic needing new contributor or "not needed"}
::END::
```
(per NOT YET milestone)

Contributor onboarding paths (plain text): per Solo Pioneer EARNED + Team Topic NOT YET.
If none: `Onboarding paths: none.`

#### 3.4 -- Team Insight + Falsifiability Contract

**Skeptic gate**: Skeptic knows every field from every block above -- all `::ACHIEVEMENTS::`, `::TEAM_MILESTONES::`, `::INERTIA::`, `::ECHO_DETECTION::`, `::DISCREPANCY_CHECK::`, `::EFFECTIVE_FLAGS::`, `::LEADERBOARD_ENTRY::`, `::RATE_TIER_DISTRIBUTION::`, `::COLLABORATION_SIGNAL::`, `::ECHO_CONTRIBUTOR_CHECK::`, `::RECONCILIATION::`, co-occurrence matrix, `::REGRESSION_RISK::`, `::COALITION_ANALYSIS::`, and onboarding paths. An insight restating any block field fails. A passing insight surfaces an inference visible only across multiple distinct analysis layers.

Write one Team Insight sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor or topic name.

```
[holds if: {entity-specific condition -- topic path, contributor, or numeric threshold}]
[falsified by: {entity-specific condition -- topic path, contributor, or numeric threshold}]
```

#### 3.5 -- Pre-Write Check

From `::EFFECTIVE_FLAGS::`. Zero-score conditions identified.

**prevents: prefix rule** (first enforcement point): zero-score condition actions carry `prevents:`.

#### 3.6 -- Next Actions -- 2D Round x Tier Matrix

```
## Next Actions

### Round 1 (1 signal closes the gap)
1. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] `{namespace}/{topic}` -> unlocks **{exact name}**
   [resolves: {flag}] [closes: {achievement} gap of {N} {unit} for {topic}]

### Round 2 (2-3 signals needed)
2. [CRITICAL/WARNING/ADVANCING] `{namespace}/{topic}` -> unlocks **{exact name}**

### Round 3 (4+ signals or coordination)
3. [CRITICAL/WARNING/ADVANCING] `{namespace}/{topic}` -> unlocks **{exact name}**
```

Empty rounds: `Round {N}: no actions at this gap distance.`

**prevents: prefix rule** (second enforcement point): in action template.

`ACTIONS GATE: prevents: prefix used for {N} zero-score conditions`

**Publisher Gate**:
- [ ] ss3.0 Inspector: `::DISCREPANCY_CHECK::` blocks for flagged topics; `::EFFECTIVE_FLAGS::` present
- [ ] `::LEADERBOARD_ENTRY::` blocks with all nine fields; `::RATE_TIER_DISTRIBUTION::` present
- [ ] `::ECHO_CONTRIBUTOR_CHECK::` blocks; echo summary and advisory present
- [ ] `::RECONCILIATION::`, co-occurrence matrix (15 cells), `::REGRESSION_RISK::`, `::COALITION_ANALYSIS::`, onboarding paths present
- [ ] Team Insight one sentence; Skeptic gate verified; falsifiability contract with entity-specific conditions
- [ ] Actions Round x Tier 2D; at least 3; `prevents:` at two independent locations; ACTIONS GATE with actual N

---

## V-03 -- Dedicated Inspector ROLE + 4-Role Pipeline + All R16 Seeds + Seed AF

**Axis**: Role sequence
**Hypothesis**: A 4-role pipeline with a dedicated **Inspector** as ROLE 3 between Analyst and Publisher. The Inspector's sole job is the adversarial discrepancy check plus ARS ranking -- maximally cleanly satisfying C-35 (Inspector is architecturally specialized for adversarial verification, wholly separate from the Analyst). New seed AF (Achievement Readiness Score per topic) is computed by the Inspector as a topic-level priority list. C-34 (falsifiability) and C-36 (2D action matrix) are in the Publisher.

---

You are running the **Corps Leaderboard** skill in a **4-role pipeline**: Archivist -> Analyst -> Inspector -> Publisher. Execute each role completely before advancing. No role may perform work assigned to another. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: Analyst runs Inertia Phase (with flag lifecycle) before Health Phase. Health Phase uses severity order (critical -> warning -> healthy), alphabetical within tier. Inspector performs adversarial discrepancy check and ARS ranking. Publisher handles leaderboard, supplementary analysis, Team Insight, and actions.

---

### ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. Does NOT evaluate achievements, rank contributors, or write insights or actions.

Glob `simulations/**/*.md`. Zero matches: `REGISTRY: empty -- no signal files found in simulations/` and stop.

Print registry: `topic_path | namespace | contributor | file`
Print: `Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`
The 9 namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.
Print contributor index: `contributor | distinct_namespaces | topic_paths | file_count`
Baseline check: print `Baseline found: {N} entries` or `Baseline not found: all flags marked new`.

**Archivist Gate**:
- [ ] Registry table; namespace coverage line; contributor index; baseline status line

**Archivist Handoff** to Analyst: registry, coverage, contributor index, baseline flag table (or `baseline: none`).

---

### ROLE 2: ANALYST

**Responsibility**: Evaluation only. Inertia Phase with lifecycle (ss2.1), Health Phase in severity order (ss2.2), Nearest-Miss (ss2.3), Echo Detection (ss2.4). Does NOT perform discrepancy checks, compute ARS, or write insights or actions.

#### 2.1 -- Inertia Phase (RUNS FIRST)

Trajectory and flag lifecycle only. No file counts, achievement statuses, or coverage totals.

| Inertia Flag | Condition |
|---|---|
| `stuck-at-first` | exactly 1 file; Signal Depth not earned |
| `solo-hold` | exactly 1 contributor |
| `namespace-thin` | all files in 1 namespace; Full Sweep not earned |
| `healthy-momentum` | Signal Depth earned AND >= 2 contributors |

Severity: `critical` = 2+ non-momentum; `warning` = 1; `healthy` = 0.

Flag lifecycle against baseline: `new` / `persistent` / `resolved`.

Print: `topic_path | flags_raised(lifecycle) | trajectory note | severity`

Resolved flags list (or omit). Stale signal table: `topic_path | stale_status`.
Velocity: `Signal velocity: {N} / {N} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

**Section 2.1 Gate**:
- [ ] Inertia table with lifecycle notation; no file counts or achievement statuses; resolved flags; stale table; velocity summary

#### 2.2 -- Health Phase (severity order: critical -> warning -> healthy)

Current state only. No trajectory claims or flag names.

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health -- Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {N}/9

| Achievement | Status | Evidence / Unlock Path |
|---|---|---|
| First Signal  | EARNED/LOCKED | ... |
| Signal Depth  | EARNED/LOCKED | ... |
| Full Sweep    | EARNED/LOCKED | ... |
| Solo Pioneer  | EARNED/LOCKED | ... |
| Team Topic    | EARNED/LOCKED | ... |
```

When Solo Pioneer EARNED + Team Topic NOT YET: `[TENSION: solo hold -- 1 additional contributor with >= 1 signal unlocks Team Topic]`

Team milestones: exact names `first team signal`, `shared coverage`, `debate starter`. Proximity ladders for all NOT YET milestones. EARNED milestones: no ladder.

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`
Namespace leader table: `namespace | leader | signal_count`

#### 2.3 -- Nearest-Miss Assessment

Level 1: 1-unit, ascending. Level 2: 2-unit, only when no Level 1 for type; state `Level 1: no topics are 1 unit away` first.

#### 2.4 -- Echo Detection

Rule A: `healthy-momentum` + Solo Pioneer EARNED -> retract. Rule B: any flag + First Signal LOCKED -> retract.

Echo Detection Table: 5 columns. `| none | -- | -- | -- | -- |` if clean.

**Section 2.2-2.4 Gate**:
- [ ] Severity order; five exact achievement names; LOCKED with unlock paths; contamination check; proximity ladders for all NOT YET milestones; nearest-miss; echo table

**Analyst Handoff** to Inspector: all evaluation output (8 artifacts as in V-01).

---

### ROLE 3: INSPECTOR

**Responsibility**: Adversarial discrepancy check (ss3.1) and Achievement Readiness Score ranking (ss3.2) only. Does NOT rank contributors, synthesize observations, write insights, or write actions.

#### 3.1 -- Discrepancy Check (Adversarial Flag Validation)

Compare each raised flag in Analyst's inertia table against Health Phase achievement tables:

| Flag | Contradiction if Health Phase shows |
|---|---|
| `stuck-at-first` | Signal Depth: EARNED |
| `solo-hold` | >= 2 distinct contributors |
| `namespace-thin` | Full Sweep: EARNED |

```
## Discrepancy Table
| topic_path | Flag raised | Health Phase evidence | Contradiction? | Disposition |
|---|---|---|---|---|
```

Emit `DISCREPANCY RETRACTION: {flag-name} on {topic_path} retracted -- Health Phase shows {evidence}.` for each contradiction.
No contradictions: one row `| none | -- | -- | no | -- |`.

Emit:
`Effective open flags: {topic:flag pairs}` (Analyst flags minus echo-retracted minus discrepancy-retracted)
`Discrepancy-retracted flags: {list or "none"}`

#### 3.2 -- Achievement Readiness Score Ranking

`ARS = earned_achievements / 5` per topic. Rank ascending:

```
## Achievement Readiness Score
| rank | topic_path | earned | ARS | intervention_priority |
|---|---|---|---|---|
```

`intervention_priority`: `immediate` (0.00), `high` (0.20-0.39), `medium` (0.40-0.59), `low` (0.60-0.79), `minimal` (0.80-1.00).

`ARS distribution: {N} immediate, {N} high, {N} medium, {N} low, {N} minimal`

**Inspector Gate**:

- [ ] Discrepancy Table present; every raised flag checked; retraction statements; "none" row if clean
- [ ] Effective open flag list and discrepancy-retracted list present
- [ ] ARS table sorted ascending; intervention_priority assigned; distribution summary present

**Inspector Handoff** to Publisher:

1. Discrepancy Table and retraction statements
2. Effective open flag list
3. ARS table and distribution summary
4. All Analyst Handoff artifacts (pass-through)

---

### ROLE 4: PUBLISHER

**Responsibility**: Leaderboard, supplementary analysis, Team Insight with falsifiability contract, and 2D actions. Does NOT re-evaluate achievements or re-run prior analysis.

#### 4.1 -- Contributor Leaderboard

Rank descending by signal count. Per contributor: `rate`, `cohort`, `gap_debt`. Print: `rank | contributor | signals | topics | achievements | rate | cohort | gap_debt`.

Namespace leaders, solo pioneer tension, collaboration signal. Contributor onboarding paths (per Solo Pioneer EARNED + Team Topic NOT YET).

#### 4.2 -- Supplementary Analysis

**Reconciliation** (one Health + one Inertia observation). **Co-occurrence matrix** (5x5, all 15 cells). **Regression risk** per milestone. **Coalition analysis** per NOT YET milestone.

#### 4.3 -- Team Insight + Falsifiability Contract

**Skeptic gate**: Skeptic knows every Health Phase achievement status, every milestone row (proximity ladders), every inertia flag with lifecycle (echo-retracted and discrepancy-retracted with reasons), effective open flag list, velocity, nearest-miss, leaderboard (rate, cohort, gap_debt), namespace leaders, tension, collaboration signal, co-occurrence matrix, reconciliation, regression risk, coalition analysis, contributor onboarding paths, ARS table (rank, topic, earned, ARS, intervention_priority), and ARS distribution. An insight restating any prior field fails. A passing insight synthesizes across at least two distinct analysis layers -- ARS rankings, regression risk, flag lifecycle, or co-occurrence -- producing an inference none of the four roles individually surfaced.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor or topic name.

Append:
```
[holds if: {entity-specific -- topic, contributor, or threshold}]
[falsified by: {entity-specific -- topic, contributor, or threshold}]
```

#### 4.4 -- Pre-Write Check

Effective open flags from Inspector Handoff. Zero-score conditions. Discrepancy-retracted and echo-retracted excluded from `resolves:`. ARS `immediate` and `high` topics flagged as higher-priority.

**prevents: prefix rule** (first enforcement point).

#### 4.5 -- Next Actions -- 2D Round x Tier Matrix

Both Round AND Tier present simultaneously per action row.

```
## Next Actions

### Round 1 (1 signal closes the gap)
1. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] `{namespace}/{topic}` -> unlocks **{exact name}**
   [resolves: {flag}] [closes: {gap}] [ARS priority: immediate/high -- if applicable]

### Round 2 (2-3 signals)
2. ...

### Round 3 (4+ or coordination)
3. ...
```

Empty rounds: `Round {N}: no actions at this gap distance.`

**prevents: prefix rule** (second enforcement point).

`ACTIONS GATE: prevents: prefix used for {N} zero-score conditions`

**Publisher Gate**:

- [ ] Leaderboard eight columns; namespace leaders, tension, collaboration signal, onboarding paths
- [ ] Reconciliation, co-occurrence (15 cells), regression risk, coalition analysis present
- [ ] ARS-guided action framing note present
- [ ] Team Insight one sentence; Skeptic gate verified; falsifiability contract with entity-specific conditions; Skeptic context includes ARS ranks
- [ ] Actions in Round x Tier 2D; at least 3; `resolves:` effective open flags only; `prevents:` two independent locations; ACTIONS GATE

---

## V-04 -- Combination: Tiered Actions + Coalition + Regression Risk + Namespace Momentum + All R16 Seeds + Seed AG

**Axis**: Combination
**Hypothesis**: R16 V-04 combined tiered actions, coalition mapping, and regression risk. This variation adds Seed AG (namespace momentum vector): per-namespace `last_contributor` and `momentum` (active/stalled), surfacing namespaces with historic coverage but no recent investment. The Strategist (ROLE 3) performs the Inspector Discrepancy Check (ss3.0) before producing leaderboard and strategic analysis -- satisfying C-35 as a structurally distinct role from Analyst. C-34 (falsifiability) and C-36 (2D action matrix) in the Publisher. Combined with flag lifecycle and regression risk, namespace momentum creates a third prioritization dimension: a CRITICAL topic in a stalled namespace is a different risk than one in an active namespace.

---

You are running the **Corps Leaderboard** skill in a **4-role pipeline**: Archivist -> Analyst -> Strategist -> Publisher. Execute each role completely before advancing. No role may perform work assigned to another. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: Analyst runs Inertia Phase (with flag lifecycle) before Health Phase. Health Phase uses severity order (critical -> warning -> healthy). Strategist opens with Inspector Discrepancy Check (ss3.0) then produces leaderboard and strategic analysis. Publisher handles Team Insight and actions.

---

### ROLE 1: ARCHIVIST

**Responsibility**: Data collection only.

Glob `simulations/**/*.md`. Zero matches: `REGISTRY: empty` and stop.

Print registry: `topic_path | namespace | contributor | file`
Print: `Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`
Print contributor index: `contributor | distinct_namespaces | topic_paths | file_count`
Baseline check: `Baseline found: {N}` or `Baseline not found`.

Namespace recency index: for each active namespace, identify most recent file (by modification date or filename order as proxy). Print:
`Namespace recency: {namespace} | last_file | contributor` (one line per active namespace)

**Archivist Gate**:
- [ ] Registry; namespace coverage; contributor index; baseline status; namespace recency lines

**Archivist Handoff** to Analyst: registry, coverage, contributor index, baseline flag table, namespace recency index.

---

### ROLE 2: ANALYST

**Responsibility**: Evaluation only. Inertia Phase with lifecycle (ss2.1), Health Phase in severity order (ss2.2), Nearest-Miss (ss2.3), Echo Detection (ss2.4). Does NOT perform discrepancy checks, compute momentum, or write insights or actions.

(Sections 2.1 through 2.4 follow the same structure as V-03 ROLE 2 above, with identical gate checklist and handoff artifacts. The Analyst does not have access to the namespace recency index and does not produce any momentum output.)

**Analyst Handoff** to Strategist: 8 evaluation artifacts (same as V-03).

---

### ROLE 3: STRATEGIST

**Responsibility**: Inspector Discrepancy Check (ss3.0), leaderboard (ss3.1), namespace momentum vector (ss3.2), reconciliation (ss3.3), co-occurrence matrix (ss3.4), regression risk + coalition analysis (ss3.5), and contributor onboarding paths (ss3.6). Does NOT write Team Insight or actions.

#### 3.0 -- Inspector Discrepancy Check (RUNS FIRST)

Strategist is structurally distinct from Analyst. Compare each raised flag against Health Phase data:

| Flag | Contradiction if |
|---|---|
| `stuck-at-first` | Signal Depth: EARNED |
| `solo-hold` | >= 2 contributors |
| `namespace-thin` | Full Sweep: EARNED |

```
## Discrepancy Table
| topic_path | Flag raised | Health Phase evidence | Contradiction? | Disposition |
|---|---|---|---|---|
```

Emit `DISCREPANCY RETRACTION: ...` for each contradiction. `| none | -- | -- | no | -- |` if clean.

`Effective open flags: {list}` (post-echo, post-discrepancy)

**Inspector Gate** (within ss3.0):
- [ ] Discrepancy Table present; effective open flag list present

#### 3.1 -- Contributor Leaderboard

Rank descending by signal count. Per contributor: `rate`, `cohort`, `gap_debt`.
Print: `rank | contributor | signals | topics | achievements | rate | cohort | gap_debt`

Namespace leaders, solo pioneer tension, collaboration signal.

#### 3.2 -- Namespace Momentum Vector

Using Archivist's namespace recency index:
- `last_contributor`: contributor of most recent file in namespace
- `last_signal_recency`: `recent` (last file in most recent 25% of all files by sort order) or `older`
- `momentum`: `active` / `stalled`

```
## Namespace Momentum Vector
| namespace | last_contributor | last_signal_recency | momentum |
|---|---|---|---|
```

`Active namespaces: {N} active | {N} stalled | {N} empty`

#### 3.3 -- Cross-Dimensional Reconciliation

```
## Reconciliation
| Health observation | Inertia observation | Interaction |
|---|---|---|
```

#### 3.4 -- Achievement Co-Occurrence Matrix

5x5 matrix, all 15 cells populated. Interpretive note.

#### 3.5 -- Milestone Regression Risk + Coalition Analysis

**Regression risk**: Per EARNED milestone: `milestone | status | regression_risk | at_risk_contributor`
`regression_risk` = `stable` or `fragile: {contributor}`. NOT YET: `N/A`.

**Coalition analysis** per NOT YET milestone: `milestone | internal path | external path`

#### 3.6 -- Contributor Onboarding Paths

Per Solo Pioneer EARNED + Team Topic NOT YET:
`Onboarding path -- {topic_path}: {contributor} holds solo. Fastest unlock: 1 file in {stalled namespace preferred} from any new contributor.`
If none: `Onboarding paths: none.`

**Strategist Gate**:

- [ ] Discrepancy Table (ss3.0); effective open flag list present
- [ ] Leaderboard eight columns; namespace leaders, tension, collaboration signal
- [ ] Namespace Momentum Vector table; active/stalled/empty summary
- [ ] Reconciliation; co-occurrence matrix (15 cells); regression risk; coalition analysis; onboarding paths

**Strategist Handoff** to Publisher: all above plus all Analyst Handoff artifacts (pass-through).

---

### ROLE 4: PUBLISHER

**Responsibility**: Team Insight with falsifiability contract, and 2D actions. Does NOT re-evaluate or re-run prior analysis.

#### 4.1 -- Team Insight + Falsifiability Contract

**Skeptic gate**: Skeptic knows: every achievement status (Health tables), every milestone row (proximity ladders), every inertia flag with lifecycle (echo-retracted, discrepancy-retracted with reasons, effective open flag list), velocity, nearest-miss, leaderboard (rate, cohort, gap_debt), namespace leaders, tension, collaboration signal, Namespace Momentum Vector (per-namespace last_contributor, last_signal_recency, momentum, active/stalled/empty summary), reconciliation, co-occurrence matrix (15 cells + interpretation), regression risk, coalition paths, contributor onboarding paths. An insight restating any field -- including namespace momentum labels, regression risk assignments, or coalition paths -- fails. A passing insight synthesizes across namespace momentum data, flag lifecycle, and regression risk to surface an inference visible only at their intersection.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor or topic name.

Append:
```
[holds if: {entity-specific -- topic, contributor, or threshold}]
[falsified by: {entity-specific -- topic, contributor, or threshold}]
```

#### 4.2 -- Pre-Write Check

Effective open flags from Strategist Handoff. Zero-score conditions. Discrepancy-retracted excluded from `resolves:`.

**prevents: prefix rule** (first enforcement point).

Stalled namespace actions: annotate with `[reactivates: {namespace}]` where applicable.

#### 4.3 -- Next Actions -- 2D Round x Tier Matrix

Both Round AND Tier per action row.

```
## Next Actions

### Round 1 (1 signal closes the gap)
1. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] `{namespace}/{topic}` -> unlocks **{exact name}**
   [resolves: {flag}] [closes: {gap}] [flag_lifecycle: persistent/new] [stabilizes: {milestone}] [reactivates: {ns}]

### Round 2 (2-3 signals)
2. [CRITICAL/WARNING/ADVANCING] `{namespace}/{topic}` -> unlocks **{exact name}**

### Round 3 (4+ or coordination)
3. [CRITICAL/WARNING/ADVANCING] `{namespace}/{topic}` -> unlocks **{exact name}**
```

Empty rounds: `Round {N}: no actions at this gap distance.`

**prevents: prefix rule** (second enforcement point).

`ACTIONS GATE: prevents: prefix used for {N} zero-score conditions`

**Publisher Gate**:

- [ ] Team Insight one sentence; Skeptic gate verified; namespace momentum labels, regression risk, coalition paths all in known context; no restatement; falsifiability contract with entity-specific conditions
- [ ] Pre-Write Check; effective open flags only for `resolves:`; stalled namespace note
- [ ] Actions Round x Tier 2D; at least 3; `resolves:`, `reactivates:`, `flag_lifecycle:`, `stabilizes:` where applicable; `prevents:` two independent locations; ACTIONS GATE

---

## V-05 -- Full Integration: 5-Role + All R15+R16+R17 Seeds

**Axis**: Full combination
**Hypothesis**: V-05 integrates all seeds from R15 (A+B+H+K+M+N+S+T+U+V+W+X), all seeds from R16 (Y+Z+AA+AB+AC), and all new seeds from R17 (AD+AE+AF+AG+AH) into a 5-role pipeline. Role specialization: Archivist (data + baseline + recency), Analyst (evaluation), Reconciler (cross-dimensional synthesis + flag lifecycle summary + co-occurrence matrix + echo contributor detection + onboarding paths), Inspector (adversarial discrepancy check + ARS ranking), Publisher (leaderboard + rate tier + namespace momentum + regression risk + coalition + cross-namespace pairing + Team Insight + falsifiability + 2D action matrix). The Skeptic gate encompasses all analysis layers -- flag lifecycle, co-occurrence, echo contributor classification, ARS rankings, namespace momentum, and cross-namespace pairing -- forcing second-order inference at the deepest possible level. All 28 v13 aspirational criteria expected to pass.

---

You are running the **Corps Leaderboard** skill in a **5-role pipeline**: Archivist -> Analyst -> Reconciler -> Inspector -> Publisher. Execute each role completely before advancing. No role may perform work assigned to another. Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

**Lifecycle note**: Analyst runs Inertia Phase (with flag lifecycle) before Health Phase. Health Phase uses severity order (critical -> warning -> healthy). Reconciler handles cross-dimensional synthesis, flag lifecycle summary, co-occurrence matrix, echo contributor detection, and onboarding paths. Inspector handles adversarial discrepancy check and ARS ranking. Publisher handles leaderboard, namespace momentum, rate tier, regression risk, coalition, cross-namespace pairing, Team Insight, falsifiability contract, and 2D Round x Tier actions.

---

### ROLE 1: ARCHIVIST

**Responsibility**: Data collection only.

Glob `simulations/**/*.md`. Zero matches: `REGISTRY: empty` and stop (Roles 2-5 do not run).

Print registry: `topic_path | namespace | contributor | file`
Print: `Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`
The 9 namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.
Print contributor index: `contributor | distinct_namespaces | topic_paths | file_count`
Baseline check: `Baseline found: {N} entries` or `Baseline not found`.
Namespace recency index: `{namespace} | last_file | contributor` per active namespace.

**Archivist Gate**:
- [ ] Registry; namespace coverage line; contributor index with `distinct_namespaces`; baseline status; namespace recency lines

**Archivist Handoff** to Analyst: registry, coverage, contributor index, baseline flag table (or `baseline: none`), namespace recency index.

---

### ROLE 2: ANALYST

**Responsibility**: Evaluation only. ss2.1 (Inertia with lifecycle) -> ss2.2 (Health in severity order) -> ss2.3 (Nearest-Miss) -> ss2.4 (Echo Detection). Structurally separated phases. Does NOT reconcile, perform discrepancy checks, compute ARS, rank contributors, or write insights or actions.

#### 2.1 -- Inertia Phase (RUNS FIRST)

Trajectory and flag lifecycle only. No file counts, achievement statuses, or coverage totals.

| Inertia Flag | Condition |
|---|---|
| `stuck-at-first` | exactly 1 file; Signal Depth not earned |
| `solo-hold` | exactly 1 contributor |
| `namespace-thin` | all files in 1 namespace; Full Sweep not earned |
| `healthy-momentum` | Signal Depth earned AND >= 2 contributors |

Severity: `critical` = 2+ non-momentum; `warning` = 1; `healthy` = 0.

Flag lifecycle against baseline: `new` / `persistent` / `resolved`.

Print: `topic_path | flags_raised(lifecycle) | trajectory note | severity`
Resolved flags list (or omit).
Stale signal table: `topic_path | stale_status`.
Velocity: `Signal velocity: {N} / {N} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

**Section 2.1 Gate**:
- [ ] Inertia table with `flags_raised(lifecycle)`; no file counts or achievement statuses; resolved flags; stale table; velocity

#### 2.2 -- Health Phase (severity order: critical -> warning -> healthy)

Current state only. No trajectory claims, momentum language, or flag names.

```
### topic: {topic_path} [severity: {critical/warning/healthy}]
Health -- Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {N}/9

| Achievement | Status | Evidence / Unlock Path |
|---|---|---|
| First Signal  | EARNED/LOCKED | ... |
| Signal Depth  | EARNED/LOCKED | ... |
| Full Sweep    | EARNED/LOCKED | ... |
| Solo Pioneer  | EARNED/LOCKED | ... |
| Team Topic    | EARNED/LOCKED | ... |
```

When Solo Pioneer EARNED + Team Topic NOT YET: `[TENSION: solo hold -- 1 additional contributor with >= 1 signal unlocks Team Topic]`

Team milestones (exact names): `first team signal`, `shared coverage`, `debate starter`. Proximity ladders for all NOT YET milestones.
Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`
Namespace leader table.

#### 2.3 -- Nearest-Miss Assessment

Level 1 (1-unit), ascending. Level 2 (2-unit) only when no Level 1 for type; state `Level 1: no topics are 1 unit away` first.

#### 2.4 -- Echo Detection

Rule A: `healthy-momentum` + Solo Pioneer EARNED -> retract. Rule B: any flag + First Signal LOCKED -> retract.

Echo Detection Table (5 columns). `| none | -- | -- | -- | -- |` if clean.

**Section 2.2-2.4 Gate**:
- [ ] Severity order; exact achievement names; LOCKED with unlock paths; contamination check; proximity ladders for all NOT YET; nearest-miss; echo table

**Analyst Handoff** to Reconciler: 8 evaluation artifacts.

---

### ROLE 3: RECONCILER

**Responsibility**: Cross-dimensional synthesis (ss3.1), flag lifecycle summary (ss3.2), achievement co-occurrence matrix (ss3.3), echo contributor detection (ss3.4), and contributor onboarding paths (ss3.5). Does NOT perform discrepancy checks, compute ARS, rank contributors, write insights, or write actions.

#### 3.1 -- Cross-Dimensional Reconciliation

```
## Reconciliation
| Health observation | Inertia observation | Interaction |
|---|---|---|
| {specific finding} | {specific finding} | {connection} |
```

#### 3.2 -- Flag Lifecycle Summary

- `Persistent flags (resisted last cycle): {count} -- {list}`
- `New flags (appeared this run): {count} -- {list}`
- `Resolved flags (cleared since last run): {count} -- {list}`

If no baseline: `Baseline not found -- all flags marked new; lifecycle tracking begins this run.`

#### 3.3 -- Achievement Co-Occurrence Matrix

5x5 symmetric count table. Diagonal = solo earns.

```
## Achievement Co-Occurrence Matrix
|   | First Signal | Signal Depth | Full Sweep | Solo Pioneer | Team Topic |
|---|---|---|---|---|---|
| First Signal | {N} | {N} | {N} | {N} | {N} |
| Signal Depth | -- | {N} | {N} | {N} | {N} |
| Full Sweep   | -- | -- | {N} | {N} | {N} |
| Solo Pioneer | -- | -- | -- | {N} | {N} |
| Team Topic   | -- | -- | -- | -- | {N} |
```

All 15 cells populated. `Co-occurrence interpretation: {pair} -- {implication}`

#### 3.4 -- Echo Contributor Detection

For each contributor pair, compute `{topic_path, namespace}` pair overlap:

```
## Echo Contributor Table
| contributor_A | contributor_B | shared_pairs | total_union | overlap_pct | echo_classification |
|---|---|---|---|---|---|
```

`echo_classification`: `full-echo` (100%), `partial-echo` (>= 80%), `independent` (< 80%).

Single contributor: `Echo Contributor Table: single contributor -- not applicable`.

`Echo summary: {N} full-echo, {N} partial-echo, {N} independent.`
`[ECHO RISK: {description}]` if any echo pairs; else `Echo risk: none.`

#### 3.5 -- Contributor Onboarding Paths

Per Solo Pioneer EARNED + Team Topic NOT YET:
`Onboarding path -- {topic_path}: {contributor} holds solo. Fastest unlock: 1 file in {namespace} from any new contributor.`
If none: `Onboarding paths: none.`

**Reconciler Gate**:

- [ ] Reconciliation pairing with Health + Inertia observation and interaction
- [ ] Flag lifecycle summary with counts and lists (or baseline-not-found note)
- [ ] Co-occurrence matrix with all 15 cells and interpretive note
- [ ] Echo Contributor Table; echo summary; echo risk advisory
- [ ] Onboarding paths (or "none" statement)

**Reconciler Handoff** to Inspector:

1. Reconciliation pairing
2. Flag lifecycle summary
3. Co-occurrence matrix and interpretive note
4. Echo Contributor Table, echo summary, echo risk
5. Contributor onboarding paths
6. All Analyst Handoff artifacts (pass-through)

---

### ROLE 4: INSPECTOR

**Responsibility**: Adversarial discrepancy check (ss4.1) and ARS ranking (ss4.2). Structurally distinct from Analyst (flag producer) and Reconciler. Does NOT rank contributors, synthesize observations, write insights, or write actions.

#### 4.1 -- Discrepancy Check

Compare Analyst's inertia flags against Health Phase achievement tables:

| Flag | Contradiction if |
|---|---|
| `stuck-at-first` | Signal Depth: EARNED |
| `solo-hold` | >= 2 contributors |
| `namespace-thin` | Full Sweep: EARNED |

```
## Discrepancy Table
| topic_path | Flag raised | Health Phase evidence | Contradiction? | Disposition |
|---|---|---|---|---|
```

`DISCREPANCY RETRACTION: {flag-name} on {topic_path} retracted -- Health Phase shows {evidence}.` for each contradiction.
No contradictions: `| none | -- | -- | no | -- |`.

`Effective open flags: {list}` (Analyst flags minus echo-retracted minus discrepancy-retracted)
`Discrepancy-retracted flags: {list or "none"}`

#### 4.2 -- Achievement Readiness Score

`ARS = earned / 5`. Rank ascending:

```
## Achievement Readiness Score
| rank | topic_path | earned | ARS | intervention_priority |
|---|---|---|---|---|
```

`intervention_priority`: `immediate` (0.00), `high` (0.20-0.39), `medium` (0.40-0.59), `low` (0.60-0.79), `minimal` (0.80-1.00).

`ARS distribution: {N} immediate, {N} high, {N} medium, {N} low, {N} minimal`

**Inspector Gate**:

- [ ] Discrepancy Table; retractions; "none" row if clean; effective open flag list; discrepancy-retracted list
- [ ] ARS table sorted ascending; intervention_priority assigned; distribution summary

**Inspector Handoff** to Publisher:

1. Discrepancy Table and retraction statements
2. Effective open flag list
3. ARS table and distribution
4. All Reconciler Handoff artifacts (pass-through)

---

### ROLE 5: PUBLISHER

**Responsibility**: Leaderboard (ss5.1), namespace momentum vector (ss5.2), milestone regression risk + coalition analysis (ss5.3), cross-namespace pairing pattern (ss5.4), Team Insight with falsifiability contract (ss5.5), Pre-Write Check (ss5.6), and 2D Round x Tier actions (ss5.7). Does NOT re-evaluate achievements or re-run any prior analysis.

#### 5.1 -- Contributor Leaderboard

Rank descending by signal count. Per contributor:
- `rate`: `achievements / signals` (`--` if 0)
- `rate_tier`: `high-converter` (>= 0.50), `mid-converter` (0.25-0.49), `low-converter` (< 0.25), `--`
- `cohort`: `specialist` / `generalist` / `focused`
- `gap_debt`: `9 - distinct_namespaces`

Print: `rank | contributor | signals | topics | achievements | rate | rate_tier | cohort | gap_debt`

If no metadata: `| 1 | no contributor metadata found | -- | -- | -- | -- | -- | -- | -- |`

Rate Tier Distribution Summary: `high-converter: {N} | mid-converter: {N} | low-converter: {N}` plus interpretive note.

- `Namespace leader: {contributor} leads {namespace} with {N} signals` (per active namespace)
- `Solo Pioneer tension:` [from Reconciler onboarding paths]
- `Collaboration signal: {N} multi-contributor topics | Highest: {topic} ({N} contributors)`
- `Persistent flag watch: {count} flag(s) persisted from prior run -- {list}`

#### 5.2 -- Namespace Momentum Vector

Using Archivist's namespace recency index:
- `last_contributor`, `last_signal_recency` (recent/older), `momentum` (active/stalled)

```
## Namespace Momentum Vector
| namespace | last_contributor | last_signal_recency | momentum |
|---|---|---|---|
```

`Active namespaces: {N} active | {N} stalled | {N} empty`

#### 5.3 -- Milestone Regression Risk + Coalition Analysis

**Regression risk**: Per milestone -- `stable` or `fragile: {contributor}`. NOT YET: `N/A`.
Print: `milestone | status | regression_risk | at_risk_contributor`

**Coalition analysis** per NOT YET milestone: `milestone | internal path | external path`

#### 5.4 -- Cross-Namespace Pairing Pattern

Count topics with signals in BOTH namespace A and namespace B (all active namespace pairs).

```
## Cross-Namespace Pairing
| namespace_A | namespace_B | co_occurring_topics | pairing_strength |
|---|---|---|---|
```

Sort descending. Identify:
- `Top-3 co-occurring pairs: {ns_A}+{ns_B}: {N} topics`
- `Bottom-3 co-occurring pairs: {ns_A}+{ns_B}: {N} topics`

`Pairing interpretation: {top pair} naturally follows each other across {N} topics; {bottom pair} -- gap may indicate a structural workflow break.`

#### 5.5 -- Team Insight + Falsifiability Contract

**Skeptic gate**: A Skeptic who has read all prior output already knows: every achievement status (Health Phase tables), every milestone row (including all proximity ladder per-topic deficit breakdowns and coalition paths), every inertia flag with lifecycle annotations (new, persistent, resolved, echo-retracted with reasons, discrepancy-retracted with reasons), effective open flag list, every severity tier, trajectory note, stale status, velocity trend, nearest-miss entries, leaderboard fields (rate, rate_tier, cohort, gap_debt), rate tier distribution with interpretive note, namespace leaders, solo pioneer tension (from onboarding paths), collaboration signal, persistent flag watch, Namespace Momentum Vector (per-namespace fields and summary), flag lifecycle summary (counts and lists), co-occurrence matrix (all 15 cells + interpretation), Echo Contributor Table (shared pairs, overlap, echo_classification, echo summary, echo risk), reconciliation pairing, ARS ranking (all rows, intervention priorities, distribution), regression risk assignments, coalition paths, cross-namespace pairing (all pairs sorted, top-3, bottom-3, pairing interpretation), and contributor onboarding paths. An insight restating any field from any prior artifact fails. A passing insight surfaces a second-order inference visible only by synthesizing across at least three distinct analysis layers simultaneously -- an inference that none of the five prior roles individually produced.

Write one Team Insight sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor or topic name.

Append:
```
[holds if: {specific entity -- topic path, contributor, or numeric threshold}]
[falsified by: {specific entity -- topic path, contributor, or numeric threshold}]
```

#### 5.6 -- Pre-Write Check

Effective open flags from Inspector. Zero-score conditions. Discrepancy-retracted and echo-retracted excluded from `resolves:`. `persistent` flags are higher-priority. Stalled namespace actions: `[reactivates: {namespace}]`.

**prevents: prefix rule** (first of two independent enforcement points).

#### 5.7 -- Next Actions -- 2D Round x Tier Matrix

Both Round AND Tier simultaneously per action row.

- Round 1: 1 signal closes the gap
- Round 2: 2-3 signals
- Round 3: 4+ or multi-contributor
- Tier: `[CRITICAL]`, `[WARNING]`, `[ADVANCING]`

At least 3 actions total.

**prevents: prefix rule** (second of two independent enforcement points).

```
## Next Actions

### Round 1 (1 signal closes the gap)
1. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] `{namespace}/{topic}` -> unlocks **{exact name}**
   [resolves: {flag}] [closes: {gap}] [flag_lifecycle: persistent/new] [stabilizes: {milestone}] [reactivates: {ns}]

### Round 2 (2-3 signals needed)
2. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] `{namespace}/{topic}` -> unlocks **{exact name}**

### Round 3 (4+ or coordination)
3. [CRITICAL/WARNING/ADVANCING] [prevents: or omit] `{namespace}/{topic}` -> unlocks **{exact name}**
```

Empty rounds: `Round {N}: no actions at this gap distance.`

`ACTIONS GATE: prevents: prefix used for {N} zero-score conditions`

**Publisher Gate**:

- [ ] Leaderboard nine columns; rate tier distribution with interpretive note; namespace leaders, tension (from onboarding paths), collaboration signal, persistent flag watch
- [ ] Namespace Momentum Vector; all active namespaces; active/stalled/empty summary
- [ ] Regression risk per milestone; coalition analysis for NOT YET milestones
- [ ] Cross-Namespace Pairing table sorted descending; top-3 and bottom-3 identified; pairing interpretation present
- [ ] Team Insight one sentence; Skeptic gate verified -- Skeptic context explicitly includes all five analysis layers (flag lifecycle, co-occurrence, echo contributor, ARS, cross-namespace pairing); no restatement of any prior field; cross-topic inference with concrete number and specific name
- [ ] Falsifiability contract with entity-specific `holds if` and `falsified by` conditions
- [ ] Pre-Write Check: effective open flags; persistent flags higher-priority; stalled namespaces noted
- [ ] Actions in Round x Tier 2D; every action has BOTH Round header AND tier prefix; empty rounds stated; at least 3 total; `resolves:` on effective-open-flag-resolving actions; `flag_lifecycle:`, `stabilizes:`, `reactivates:` where applicable; `prevents:` two independent locations (ss5.6 and ss5.7)
- [ ] ACTIONS GATE with actual N

---

## Summary Table

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **Axis** | Phrasing register | Output format | Role sequence | Combination | Full integration |
| **Roles** | 3 | 3 | 4 | 4 | 5 |
| **C-35 mechanism** | Publisher ss3.0 | Publisher ss3.0 | Dedicated ROLE 3: Inspector | Strategist ss3.0 | Dedicated ROLE 4: Inspector |
| **New seed** | AD (rate tier) | AE (echo contributor) | AF (ARS per topic) | AG (namespace momentum) | AD+AE+AF+AG+AH |
| **v13 expected** | 28/28 -> 100.00 | 28/28 -> 100.00 | 28/28 -> 100.00 | 28/28 -> 100.00 | 28/28 -> 100.00 |

**Seeds entering R18** (candidates for v14 criteria):
- **Seed AD** (rate tier): `high-converter / mid-converter / low-converter` + distribution summary. Changes team reading from volume to conversion efficiency. Candidate C-37.
- **Seed AE** (echo contributor): contributor-pair overlap table with echo_classification. Reveals redundant coverage patterns. Candidate C-38.
- **Seed AF** (ARS per topic): `ARS = earned/5` ranked ascending -- intervention priority orthogonal to severity tiers. Candidate C-39.
- **Seed AG** (namespace momentum): per-namespace active/stalled from recency index. Surfaces namespaces with historic but no recent coverage. Candidate C-40.
- **Seed AH** (cross-namespace pairing): top-3/bottom-3 co-occurring namespace pairs with pairing interpretation. Reveals structural workflow breaks. Candidate C-41.
