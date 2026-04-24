---
skill: quest-variate
skill_target: corps-leaderboard
round: 12
date: 2026-03-17
rubric_version: 11
---

# Variate R12 — corps-leaderboard

5 complete prompt body variations for the `corps-leaderboard` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

**R11 ceiling against v11**: V-02, V-04, V-05 hold 23/23 = 100.00. V-01 = V-03 = 99.13
(21/23 — both fail C-26, C-28 due to no named role pipeline). C-27 is load-bearing for three
criteria (C-27, C-30, C-31). The ceiling is stable; the next opportunity requires patterns
not yet captured in v11.

**R11 seeds entering R12**:
- Seed A (v12-C-32 candidate): `resolves: {flag-name}` annotation on inertia-flag-resolving
  actions. Introduced in R11 V-01 and V-05.
- Seed B (v12-C-33 candidate): pre-synthesis cross-dimensional reconciliation pairing
  (one Health × one Inertia observation with interaction statement). Introduced in R11 V-02
  and V-05.

**R12 design targets**:
- V-01: RFC-style numbered requirements (phrasing register). Carries 3-role Archivist/
  Analyst/Publisher pipeline from R11 (fixes the C-26/C-28 gap that dropped R11 V-01 to
  21/23). Formalizes Seed A. Introduces Seed D (inertia severity tier per topic). Expected:
  23/23.
- V-02: 4-role pipeline with Narrator (role sequence axis). Splits Publisher into Strategist
  (actions) + Narrator (reconciliation + insight). Three handoffs → stronger C-28 coverage.
  Formalizes Seeds A + B. Introduces Seed E (Narrator confidence gate for reconciliation
  pairing). Expected: 23/23.
- V-03: Dashboard-first output format (output format axis). Archivist opens with a compact
  Sprint Velocity Dashboard before the registry table. 3-role pipeline carried forward.
  Introduces Seed F (action dependency chain `requires:` annotation). Expected: 23/23.
- V-04: Inertia-first lifecycle + 4-role pipeline (combination). Fixes R11 V-03's C-26/C-28
  gap with a 4-role Archivist/Assessor/Synthesizer/Publisher structure, inertia-first order
  inside Assessor. Introduces Seeds D + G (co-contribution network map). Expected: 23/23.
- V-05: Full integration — 4-role pipeline + all seeds (A, B, D, E, F, G). Ceiling-holding
  with maximum v12 seeding. Expected: 23/23.

**Expected scoring against v11** (formula: `90 + (passed/23) × 10`):
- V-01: pass all C-22–C-31 (carries C-26/C-28 via 3-role pipeline) → 23/23 → **100.00**
- V-02: pass all C-22–C-31 (4-role, 3 handoffs) → 23/23 → **100.00**
- V-03: pass all C-22–C-31 (dashboard-first, 3-role pipeline) → 23/23 → **100.00**
- V-04: pass all C-22–C-31 (inertia-first 4-role) → 23/23 → **100.00**
- V-05: pass all C-22–C-31 + all seeds → 23/23 → **100.00**

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Phrasing register (RFC numbered requirements) + Seed A + Seed D | V-01 |
| Role sequence (4-role: Archivist/Analyst/Strategist/Narrator) + Seeds A + B + E | V-02 |
| Output format (dashboard-first sprint briefing) + Seed F | V-03 |
| Combination: inertia-first lifecycle + 4-role pipeline + Seeds D + G | V-04 |
| Full integration: 4-role + all seeds A + B + D + E + F + G | V-05 |

---

## V-01 — RFC-Style Numbered Requirements + 3-Role Pipeline + Seed A + Seed D

**Axis**: Phrasing register
**Hypothesis**: All prior variations use role-block imperative phrasing (MUST/SHALL inside
named role sections). An RFC-style format organizes the same structural requirements as
numbered compliance items (REQ-N.M), separating requirement identity from prose framing. This
tests whether the requirement-identifier convention produces tighter output discipline by
making each constraint addressable by number — and whether it surfaces Seed D (inertia
severity tier) more naturally than role framing, since severity tiers appear as a requirement
annotation rather than a role-scope constraint. R11 V-01 failed C-26 and C-28 (no role
pipeline). R12 V-01 carries the 3-role Archivist/Analyst/Publisher structure forward while
replacing role-block prose with RFC requirements, fixing those gaps.

Seed A formalized as REQ-3.5 (`resolves:` annotation). Seed D introduced as REQ-2B.3
(severity tier column in inertia table). These are orthogonal — REQ-3.5 links actions to
trajectory observations; REQ-2B.3 classifies trajectory observations by urgency tier.

---

You are executing the **Corps Leaderboard** skill. This document is the compliance
specification. Satisfy every requirement in section order. A requirement may reference prior
requirements by identifier (REQ-N.M). Emit each Gate checklist verbatim with all items
checked before advancing to the next section.

---

### SECTION 1 — ARCHIVIST REQUIREMENTS

**REQ-1.1** — Glob `simulations/**/*.md`. For every matching file, record:

- `topic_path` — path segment after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path` (e.g., `scout`)
- `contributor` — resolve in priority order: frontmatter `author:` > frontmatter
  `contributor:` > filename prefix before first `-` > literal `unknown`
- `file` — full relative path

**REQ-1.2** — Print the registry as a markdown table: `topic_path | namespace | contributor | file`

**REQ-1.3** — Immediately after the registry table, print a namespace coverage line:
`Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`
The 9 Signal namespaces are: `scout, draft, review, flow, trace, prove, listen, program, topic`.

**REQ-1.4** — Build a contributor index: for each contributor, list every `topic_path` and
file count per topic. Print: `contributor | topic_path | file_count`.

**REQ-1.5** (empty-workspace halt) — WHEN REQ-1.1 finds zero files: write
`REGISTRY: empty — no signal files found in simulations/` and halt. Sections 2 and 3 MUST
NOT execute.

**Archivist Gate** — Emit this checklist and verify all items before proceeding to Section 2:

- [ ] REQ-1.2: registry table printed with all four columns
- [ ] REQ-1.3: namespace coverage line present with active and empty lists
- [ ] REQ-1.4: contributor index table present
- [ ] REQ-1.5: halt confirmed (zero files) or skipped (files found)

**Archivist Handoff** — The following artifacts transfer to Section 2:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Namespace coverage line (active and empty namespace lists)
3. Contributor index table (columns: `contributor`, `topic_path`, `file_count`)

Section 2 operates on these artifacts only. It MUST NOT re-scan the workspace.

---

### SECTION 2 — ANALYST REQUIREMENTS

Section 2 contains two sub-sections that MUST run in order. REQ-2A requirements complete
before any REQ-2B work begins. The sub-sections are structurally distinct: REQ-2A reports
current state only; REQ-2B reports trajectory only. REQ-2A output MUST NOT contain
trajectory language; REQ-2B output MUST NOT restate static counts from REQ-2A.

#### SECTION 2A — Health Requirements

**REQ-2A.1** — For each `topic_path` in the Section 1 registry, print a topic block with
this exact header line:

```
### topic: {topic_path}
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {distinct_ns_count}/9
```

**REQ-2A.2** — For each topic block from REQ-2A.1, evaluate all five achievements using
exact names only (paraphrasing fails). For every LOCKED achievement, state the specific
action required to unlock it in the evidence cell — a cell containing only `LOCKED` without
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

**REQ-2A.3** (solo pioneer tension) — WHEN Solo Pioneer is EARNED AND Team Topic is NOT YET
for any topic, append immediately after that topic's achievement block:
`[TENSION: solo hold — Team Topic unlock requires 1 additional contributor with >= 1 signal]`

**REQ-2A.4** — Evaluate all three team milestones using exact names. Evidence MUST be
non-empty for every row.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file exists in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print as table: `milestone | status | evidence`

**REQ-2A.5** (debate starter proximity) — After the milestones table, print:
`Debate starter: nearest topic is {name} with {N}/3 contributors present ({M} more needed)`

**REQ-2A.6** (namespace leader) — Print a namespace leader table for each active namespace:
`namespace | leader | signal_count`

**Section 2A Gate** — Emit before proceeding to REQ-2B:

- [ ] REQ-2A.1: every topic has a health header with namespace diversity count
- [ ] REQ-2A.2: every topic has all five achievement rows; LOCKED rows include specific
  unlock paths; no trajectory language anywhere in Section 2A
- [ ] REQ-2A.3: solo pioneer tension marker applied to all qualifying topics
- [ ] REQ-2A.4: all three milestone names verbatim with non-empty evidence
- [ ] REQ-2A.5: debate starter proximity line present
- [ ] REQ-2A.6: namespace leader table present

#### SECTION 2B — Inertia Requirements

**REQ-2B.1** (structural constraint) — Section 2B reports trajectory and momentum only.
It MUST NOT restate file counts, achievement statuses, or coverage totals from REQ-2A.
Content belongs in 2B if and only if it describes direction of change.

**REQ-2B.2** — For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor signal present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

**REQ-2B.3** (severity tier) — Append a `severity` column to the inertia table per REQ-2B.2:
- `critical` — 2 or more flags raised (not counting healthy-momentum)
- `warning` — exactly 1 flag raised
- `healthy` — 0 flags, or only healthy-momentum

Print inertia table: `topic_path | flags | trajectory note | severity`
A topic with no flags gets `flags = none`, a brief healthy momentum note, and `severity = healthy`.

**REQ-2B.4** (stale signal detection) — For each topic, determine stale status using file
modification dates where accessible. Print: `topic_path | stale_status`
where `stale_status` is `stale` (all files older than 14 days), `active`, or `date-unknown`.

**REQ-2B.5** (velocity trend) — Print one team-level line:
`Signal velocity: {N_signals} signals / {N_topics} topics | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`
Classification: > 50% topics at `healthy` = increasing; < 25% = stalled; otherwise flat.

**Section 2B Gate** — Emit before proceeding to Section 3:

- [ ] REQ-2B.2: inertia table present; every topic evaluated for all four flags
- [ ] REQ-2B.3: severity column present (`critical` / `warning` / `healthy`) with no static
  counts restated from Section 2A
- [ ] REQ-2B.4: stale signal table present
- [ ] REQ-2B.5: velocity trend line present

**Section 2 Gate** (cross-sub-section) — Emit:

- [ ] Section 2A completed with all REQ-2A requirements satisfied
- [ ] Section 2B completed with all REQ-2B requirements satisfied
- [ ] No trajectory claims in 2A content; no static counts from 2A restated in 2B content

**REQ-2.6** (nearest-miss, closes Section 2) — Identify the topic-achievement pair closest
to earning:

- **Level 1** — every topic exactly 1 unit away from any achievement threshold. State topic
  name + achievement name + exact gap. Sort ascending by gap.
- **Level 2** — closest topic 2 units away. Write Level 2 ONLY when no Level 1 topic exists.
  Explicitly state "Level 1: no topics are 1 unit away" before listing Level 2.

Print: `topic | achievement | gap | level`

**Analyst Handoff** — The following artifacts transfer from Section 2 to Section 3:

1. Per-topic Health Phase achievement tables from REQ-2A.2 (one block per `topic_path`)
2. Team milestone table from REQ-2A.4 (3 rows)
3. Inertia table from REQ-2B.3 (columns: `topic_path`, `flags`, `trajectory note`, `severity`)
4. Stale signal table from REQ-2B.4
5. Velocity trend line from REQ-2B.5
6. Nearest-miss table from REQ-2.6

Section 3 operates on these artifacts only. It MUST NOT re-evaluate achievements or
re-assess inertia.

---

### SECTION 3 — PUBLISHER REQUIREMENTS

**REQ-3.1** (nearest-miss confirmation) — Transcribe and output the nearest-miss assessment
from REQ-2.6. Do not recompute.

**REQ-3.2** (collaboration signal) — Print a table of topics where Team Topic is earned:
`topic_path | contributors | collaboration_type`
where `collaboration_type` is `pair` (exactly 2 contributors) or `ensemble` (3+). If no
topic has earned Team Topic: one row `| none | — | no Team Topic earned yet |`.

**REQ-3.3** (contributor leaderboard) — Rank contributors descending by total signal count.
Ties: alphabetical. WHEN all contributors are `unknown`: write one row
`| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

**REQ-3.4** (team insight — Skeptic gate) — Before writing the Team Insight, verify the
Skeptic gate. A Skeptic who has read all of Section 2 already knows: every achievement
status, every milestone status, every inertia flag, every trajectory note, every severity
tier, the stale signal table, the velocity trend, and the nearest-miss assessment. The insight
MUST contain something the Skeptic would not already know.

An insight that restates an achievement count, milestone status, inertia flag, severity tier,
or velocity category fails. A passing insight surfaces a second-order pattern — a risk,
convergence, or cross-topic trajectory inference — requiring synthesis across health and
inertia in a way no single requirement's output alone reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

**REQ-3.5** (pre-write check) — Before writing any action, identify all zero-score conditions:
topics with 0 files, empty registry, empty leaderboard. Record them.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action whose primary purpose is eliminating a state where the output
would score zero carries the `prevents:` prefix. Advancement actions do not.

Also identify all open inertia flags from REQ-2B.2. An action whose primary purpose is
resolving an inertia flag MUST declare `resolves: {flag-name}` in the action row. Actions
that do not resolve a specific inertia flag leave `resolves:` blank.

**REQ-3.6** (actions) — Write at least 3 actions. Each MUST satisfy all of the following:
1. Names a specific namespace and topic path (e.g., `scout/competitors`)
2. Names the exact achievement or milestone it unlocks (exact names only; paraphrasing fails)
3. Carries `prevents:` prefix if it eliminates a zero-score condition — per REQ-3.5 and this
   rule (the `prevents:` rule appears here inside the action template as the second
   structurally independent enforcement point)
4. Carries `resolves: {flag-name}` if its primary purpose is resolving an inertia flag per
   REQ-3.5; blank otherwise

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag} or blank]
2. ...
3. ...
```

**REQ-3.7** (actions gate) — After all actions, output exactly this line (N = actual count
of `prevents:`-prefixed actions):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Section 3 Gate** — Emit after the ACTIONS GATE line:

- [ ] REQ-3.1: nearest-miss Level 1 present (or Level 2 with explicit "Level 1 empty" note),
  sorted ascending
- [ ] REQ-3.2: collaboration signal table present
- [ ] REQ-3.3: leaderboard present with all four columns, ranked descending
- [ ] REQ-3.4: Team Insight written as one sentence; Skeptic gate verified — Skeptic knew all
  achievement, milestone, inertia flag, severity tier, stale, velocity, and nearest-miss
  data; insight is a new cross-dimensional inference
- [ ] REQ-3.5: pre-write check complete; zero-score conditions and open inertia flags
  identified before any action written
- [ ] REQ-3.6: at least 3 actions; each names namespace + topic + exact achievement or
  milestone; `prevents:` applied per REQ-3.5 and REQ-3.6; `resolves:` applied per REQ-3.5
- [ ] REQ-3.7: ACTIONS GATE line written with actual N count substituted

---

## V-02 — 4-Role Pipeline: Archivist/Analyst/Strategist/Narrator + Seeds A + B + E

**Axis**: Role sequence
**Hypothesis**: R11 split into 3 roles (Archivist/Analyst/Publisher) with the Publisher
handling leaderboard, reconciliation, insight, and actions in one role. Splitting Publisher
into Strategist (actions) + Narrator (reconciliation + insight) creates a 4-role pipeline
with 3 handoffs — strengthening C-28 coverage (3 explicit artifact inventories vs. 2) and
separating the "what to do" from the "what it means." The Narrator writing the insight *after*
seeing the completed action list raises the novelty bar: the insight cannot merely describe
what the actions already address. Seeds A (resolves:) and B (reconciliation pairing) are
carried from R11 as formal Strategist and Narrator requirements. Seed E (Narrator confidence
gate) is new: before the Narrator writes the Team Insight, it emits a confidence annotation
(high/medium/low) for the reconciliation pairing; the insight must then advance beyond both
the pairing and its committed confidence framing.

---

You are running the **Corps Leaderboard** skill in a 4-role pipeline. Execute each role
completely before advancing to the next. No role may perform work assigned to another role.
Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. The Archivist scans the workspace, builds the
signal registry, and constructs the contributor index. The Archivist does NOT evaluate
achievements, assess milestones, assess trajectory or inertia, rank contributors, or write
insights or actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. Record four fields per file:

- `topic_path` — path segment after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > frontmatter `contributor:` > filename prefix
  before first `-` > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. Roles 2, 3, and 4 do not
run.

Print registry as table: `topic_path | namespace | contributor | file`

After the registry, print a namespace coverage line:
`Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`
The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

### 1.2 — Contributor Index

Build a contributor-to-topics index. Print: `contributor | topic_path | file_count`.

**Archivist Gate** — Verify and emit before transferring artifacts:

- [ ] Registry table printed with all four required columns
- [ ] Namespace coverage line printed with active and empty namespace lists
- [ ] Contributor index table printed with all three columns

**Archivist Handoff** — The following artifacts transfer from the Archivist to the Analyst:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
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

Reports current signal state only: file counts, namespace coverage, contributor counts, and
achievement status per topic. Does NOT report trajectory, momentum, direction of change, or
stall indicators.

For each `topic_path`, print:

```
### topic: {topic_path}
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {N}/9
```

Evaluate all five achievements. Use exact names only. For every LOCKED achievement, state
the specific unlock requirement in the evidence cell.

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
| First Signal  | ...     | ...                                 |
| Signal Depth  | ...     | ...                                 |
| Full Sweep    | ...     | ...                                 |
| Solo Pioneer  | ...     | ...                                 |
| Team Topic    | ...     | ...                                 |
```

When Solo Pioneer is EARNED and Team Topic is NOT YET: append
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]` after
that topic block.

Evaluate all three team milestones. Use exact names. Evidence must be non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

After the milestones table, print:
`Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count` for each active namespace.

### 2.2 — Inertia Phase

Reports trajectory and momentum only. Structurally separate from Health Phase. Does NOT
restate file counts or achievement statuses already in the Health Phase.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor signal present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Print inertia table: `topic_path | flags | trajectory note`
A topic with no flags gets `flags = none` with a brief healthy momentum confirmation.

Print stale signal table: `topic_path | stale_status` (`stale`, `active`, or `date-unknown`).

Print velocity summary: `Signal velocity: {N_signals} / {N_topics} topics | Trend: {increasing/flat/stalled}`.

### 2.3 — Nearest-Miss Assessment

Identify the topic-achievement pair closest to earning:

- **Level 1**: every topic 1 unit away (topic + achievement + exact gap). Sort ascending.
- **Level 2**: closest topic 2 units away. Write Level 2 ONLY when no Level 1 exists.
  State "Level 1: no topics are 1 unit away" first.

Print: `topic | achievement | gap | level`

**Analyst Gate** — Verify and emit before transferring artifacts:

- [ ] Every topic has a complete Health Phase block with all five rows; LOCKED rows include
  specific unlock paths; no trajectory language in any Health Phase content
- [ ] All three milestone names verbatim with non-empty evidence; debate starter proximity
  line and namespace leader table present
- [ ] Inertia Phase table present with every topic evaluated; no static counts restated from
  Health Phase
- [ ] Stale signal table and velocity summary present
- [ ] Nearest-miss complete (Level 1, or Level 2 with "Level 1 empty" note)
- [ ] Inertia Phase table present; no static counts restated from Health Phase

**Analyst Handoff** — The following artifacts transfer from the Analyst to the Strategist:

1. Per-topic Health Phase achievement tables (one block per `topic_path`, with tension markers
   and unlock paths)
2. Team milestone table (3 rows: milestone, status, evidence)
3. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`)
4. Stale signal table and velocity summary
5. Nearest-miss assessment table (columns: `topic`, `achievement`, `gap`, `level`)

The Strategist begins with these five artifacts plus the Archivist's three. It does not
re-evaluate achievements or re-assess inertia.

---

## ROLE 3: STRATEGIST

**Responsibility**: Actions and nearest-miss synthesis only. The Strategist works from the
Analyst's output and produces the Next Actions list. The Strategist does NOT produce the
Contributor Leaderboard, the reconciliation pairing, the Team Insight, or the Collaboration
Map — those belong to the Narrator.

### 3.1 — Nearest-Miss Confirmation

Transcribe and output the nearest-miss assessment from the Analyst Handoff. Do not recompute.

### 3.2 — Pre-Write Check

Before writing any action, identify all zero-score conditions: topics with 0 files, empty
registry, empty leaderboard. Record each one explicitly.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action whose primary purpose is eliminating a state where the output
would score zero carries the `prevents:` prefix. Advancement actions do not.

Also identify all open inertia flags from the Analyst's Inertia Phase table. An action whose
primary purpose is resolving an inertia flag MUST declare `resolves: {flag-name}` in the
action row. Actions that do not resolve a specific inertia flag leave `resolves:` blank.

### 3.3 — Next Actions

Write at least 3 actions. Each must name: (1) a specific namespace and topic path,
(2) the exact achievement or milestone it unlocks. The `prevents:` prefix rule is embedded
inside each relevant action row below as the second structurally independent enforcement
point.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag} or blank]
2. ...
3. ...
```

After all actions, output exactly this line (N = actual count of `prevents:`-prefixed
actions):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Strategist Gate** — Verify and emit after the ACTIONS GATE line:

- [ ] Nearest-miss confirmation present and formatted
- [ ] Pre-write check complete; zero-score conditions and open inertia flags identified
  before any action written
- [ ] At least 3 actions written; each names namespace + topic + exact achievement or
  milestone
- [ ] `prevents:` prefix applied to all zero-score-condition actions (two independent
  enforcement points: 3.2 and 3.3)
- [ ] `resolves:` annotation applied to all inertia-flag-resolving actions; blank for others
- [ ] ACTIONS GATE line written with actual N count substituted

**Strategist Handoff** — The following artifacts transfer from the Strategist to the Narrator:

1. Nearest-miss assessment (from Analyst, confirmed)
2. Next Actions list (all rows with `prevents:` and `resolves:` annotations as written)
3. Pre-write check results (zero-score conditions and open inertia flags identified)
4. ACTIONS GATE line (with N substituted)

The Narrator begins with all output from the Archivist, Analyst, and Strategist. It does not
re-assess actions, re-evaluate inertia, or modify the action list.

---

## ROLE 4: NARRATOR

**Responsibility**: Synthesis only. The Narrator produces the Contributor Leaderboard, the
Collaboration Map, the cross-dimensional reconciliation pairing with confidence annotation,
and the Team Insight. The Narrator does NOT re-scan the workspace, re-evaluate achievements,
re-assess inertia, or modify the action list.

### 4.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical. If all contributors
are `unknown`: write one row `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 4.2 — Collaboration Map

Print a table of topics where Team Topic is earned:
`topic_path | contributors | collaboration_type`
Types: `pair` (exactly 2 contributors), `ensemble` (3+). If no topic earned Team Topic:
one row `| none | — | no Team Topic earned yet |`.

### 4.3 — Cross-Dimensional Reconciliation with Confidence Annotation

Before writing the Team Insight, emit a reconciliation pairing. Select exactly one
observation from the Health Phase and one from the Inertia Phase that interact with or bear
on each other. State how they interact.

Immediately after the pairing, emit a confidence annotation:

- `confidence: high` — interaction is directly supported by specific evidence in both phases;
  a skeptical reader would accept it without argument
- `confidence: medium` — plausible but requires one inferential step; a skeptical reader
  might ask for clarification
- `confidence: low` — speculative; requires two or more inferential steps beyond the data

State the rationale for the confidence level in one sentence.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase} | {one finding from Inertia Phase} | {how they connect} |

Confidence: {high/medium/low} — {rationale sentence}
```

The Team Insight in 4.4 must advance beyond both the reconciliation pairing and its
confidence framing. An insight that merely restates the reconciliation row fails. An insight
that only adjusts the confidence level without adding new inference also fails.

### 4.4 — Team Insight

**Skeptic gate**: The Skeptic has read all output from the Archivist, Analyst, and Strategist
— every achievement table, every milestone row, every inertia flag, every trajectory note,
the stale signal list, the velocity summary, the nearest-miss assessment, all actions with
`prevents:` and `resolves:` annotations, the leaderboard, the collaboration map, the
reconciliation pairing, and the confidence annotation in 4.3. The insight must contain
something the Skeptic would not already know from all of that material.

An insight that echoes an inertia flag fails. An insight that restates the reconciliation
pairing fails. An insight that only comments on the confidence level fails. An insight that
merely describes what the actions already address fails. A passing insight surfaces a
second-order pattern — a risk, convergence, or trajectory inference — that requires
synthesizing across health and inertia data in a way no single block, the action list, or
the reconciliation pairing with its confidence framing directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic, (4) information the Skeptic acknowledges as new given full knowledge of all prior
output and the reconciliation pairing with its confidence annotation.

**Narrator Gate** — Verify and emit:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Collaboration map present (or "none" row if no Team Topic earned)
- [ ] Reconciliation pairing written with one Health observation, one Inertia observation,
  and interaction note
- [ ] Confidence annotation present (high/medium/low) with one-sentence rationale
- [ ] Team Insight written as one sentence; Skeptic gate verified — Skeptic knew all
  achievement, milestone, inertia flag, trajectory, stale, velocity, action (with
  resolves:/prevents: annotations), leaderboard, collaboration, reconciliation, AND
  confidence data; insight is a new cross-dimensional inference beyond all of that

---

## V-03 — Dashboard-First Output Format + 3-Role Pipeline + Seed F

**Axis**: Output format
**Hypothesis**: All prior variations follow a "data first, synthesis later" structure: scan
→ evaluate → synthesize → act. This variation inverts the opening: the Archivist emits a
compact Sprint Velocity Dashboard as its first output block — before the registry table —
giving the team a one-glance posture read before any detail. The Dashboard functions as a
preview commitment; the Analyst and Publisher phases then justify and update it. This tests
whether front-loading the summary changes how the model reasons about what the analysis
phases need to establish. Seed F (action dependency chain) is new: actions that depend on
a prior action in the sequence declare `requires: {action-N}`, creating DAG structure that
enables sprint-level sequencing.

---

You are running the **Corps Leaderboard** skill in a 3-role sprint briefing pipeline.
Execute each role completely before advancing to the next. No role may perform work assigned
to another role. Output each Gate checklist and Handoff artifact list verbatim before the
next role begins.

The output follows a **sprint briefing format**: the Archivist opens with a compact Sprint
Velocity Dashboard before the registry detail. The Dashboard commits to a preliminary
posture; the subsequent phases justify and refine it.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. The Archivist scans the workspace, emits the Sprint
Velocity Dashboard, builds the registry, and constructs the contributor index. The Archivist
does NOT evaluate achievements, assess trajectory, rank contributors, or write insights or
actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. Record four fields per file:

- `topic_path` — path after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. Roles 2 and 3 do not run.

### 1.2 — Sprint Velocity Dashboard

**Emit this dashboard as the first output block, before the registry table.** Compute from
scan results only — no achievement evaluation, no trajectory assessment.

```
## Sprint Velocity Dashboard

| Metric                    | Value                                          |
|---------------------------|------------------------------------------------|
| Total signals             | {total file count}                             |
| Topics active             | {distinct topic_path count}                    |
| Namespaces active         | {distinct namespace count} / 9                 |
| Empty namespaces          | {list or "none"}                               |
| Contributors              | {distinct non-unknown contributor count}       |
| Solo-held topics          | {topics with exactly 1 contributor}            |
| Multi-contributor topics  | {topics with 2+ contributors}                  |
| Velocity posture          | {expanding / stable / stalled} (preliminary)   |
```

Velocity posture (preliminary, scan-only):
- `expanding` — multi-contributor topics >= 50% of all topics
- `stalled` — multi-contributor < 25% AND solo-held >= 50% of all topics
- `stable` — otherwise

This is a preliminary estimate. The Analyst's Inertia Phase provides the authoritative
trajectory assessment.

### 1.3 — Signal Registry

After the dashboard, print the registry table: `topic_path | namespace | contributor | file`

After the registry, print namespace coverage:
`Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`
The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

### 1.4 — Contributor Index

Print: `contributor | topic_path | file_count`.

**Archivist Gate** — Verify and emit before transferring artifacts:

- [ ] Sprint Velocity Dashboard printed as first output block, before registry table
- [ ] Registry table printed with all four columns
- [ ] Namespace coverage line printed with active and empty lists
- [ ] Contributor index printed with all three columns

**Archivist Handoff** — The following artifacts transfer from the Archivist to the Analyst:

1. Sprint Velocity Dashboard (with preliminary velocity posture)
2. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
3. Namespace coverage line (active and empty namespace lists)
4. Contributor index table (columns: `contributor`, `topic_path`, `file_count`)

The Analyst begins with these four artifacts. It does not re-scan the workspace.

---

## ROLE 2: ANALYST

**Responsibility**: Evaluation only. The Analyst assesses registry data and reports current
state (Health Phase) then trajectory (Inertia Phase). These sub-phases are structurally
separated — Health Phase content must not appear in the Inertia Phase and vice versa. The
Analyst does NOT rank contributors, write insights, or write actions.

### 2.1 — Health Phase

Reports current signal state only. Does NOT report trajectory, momentum, or stall indicators.

For each `topic_path`, print:

```
### topic: {topic_path}
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {N}/9
```

Evaluate all five achievements. Exact names only. For every LOCKED achievement, state the
specific unlock requirement in the evidence cell.

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

When Solo Pioneer is EARNED and Team Topic is NOT YET: append
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]`.

Evaluate all three team milestones. Exact names. Evidence must be non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

Print debate starter proximity:
`Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count` per active namespace.

### 2.2 — Inertia Phase

Reports trajectory and momentum only. Does NOT restate file counts or achievement statuses
from Health Phase.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Print inertia table: `topic_path | flags | trajectory note`

Print stale signal table: `topic_path | stale_status` (`stale`, `active`, or `date-unknown`).

Print velocity summary and Dashboard update in one combined line:
`Velocity posture update: Archivist preliminary was {X} — Inertia Phase assessment: {Y} | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

### 2.3 — Nearest-Miss Assessment

- **Level 1**: every topic 1 unit away (topic + achievement + exact gap). Sort ascending.
- **Level 2**: closest topic 2 units away. Only when no Level 1 exists. State "Level 1: no
  topics are 1 unit away" first.

Print: `topic | achievement | gap | level`

**Analyst Gate** — Verify and emit before transferring artifacts:

- [ ] Every topic has Health Phase block with all five rows; LOCKED rows include unlock paths;
  no trajectory language in Health Phase
- [ ] All three milestone names verbatim with non-empty evidence; debate starter proximity
  and namespace leader table present
- [ ] Inertia Phase table present with every topic evaluated; no static counts restated from
  Health Phase
- [ ] Dashboard posture update line present with velocity distribution
- [ ] Nearest-miss complete (Level 1, or Level 2 with "Level 1 empty" note)
- [ ] Inertia Phase table present; no static counts restated from Health Phase

**Analyst Handoff** — The following artifacts transfer from the Analyst to the Publisher:

1. Per-topic Health Phase achievement tables (one block per `topic_path`)
2. Team milestone table (3 rows)
3. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`)
4. Dashboard posture update line
5. Nearest-miss assessment table

The Publisher begins with these five artifacts plus the Archivist's four. It does not
re-evaluate achievements or re-assess inertia.

---

## ROLE 3: PUBLISHER

**Responsibility**: Synthesis, leaderboard, insight, and actions only. Works from all prior
output. Does NOT re-scan, re-evaluate achievements, or re-assess inertia.

### 3.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical. If all `unknown`:
write `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 3.2 — Collaboration Signal

Print: `topic_path | contributors | collaboration_type` for topics where Team Topic is earned.
Types: `pair` (2 contributors), `ensemble` (3+). If none: `| none | — | no Team Topic earned yet |`.

### 3.3 — Team Insight

**Skeptic gate**: A Skeptic who completed all prior roles already knows every achievement
status, milestone outcome, inertia flag, velocity distribution, Dashboard posture (including
update), stale signal status, and nearest-miss assessment. The insight must contain something
this Skeptic would not already know.

An insight that restates a visible count, flag, velocity category, or Dashboard metric fails.
A passing insight surfaces a second-order pattern requiring synthesis across health and
inertia in a way no single block or the Dashboard directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic name.

### 3.4 — Pre-Write Check

Before writing actions, identify all zero-score conditions: topics with 0 files, empty
registry, empty leaderboard. Actions eliminating a zero-score condition carry `prevents:`.

**prevents: prefix rule** — stated here for the Pre-Write Check AND embedded inside each
relevant action row below: any action whose primary purpose is eliminating a state where the
output would score zero uses the `prevents:` prefix. These are two structurally independent
enforcement points.

Also identify all open inertia flags from the Analyst's Inertia Phase. Actions resolving an
inertia flag declare `resolves: {flag-name}`.

Identify actions that depend on a prior action in the sequence — for example, an action
advancing Signal Depth on a topic that currently has no signals depends on a prior action
that adds the first signal. Such dependencies must be declared using `requires: {action-N}`.

### 3.5 — Next Actions

Write at least 3 actions. Each must name: (1) a specific namespace and topic path,
(2) the exact achievement or milestone it unlocks.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag} or blank] [requires: {action-N} or blank]
2. ...
3. ...
```

After all actions, output exactly this line (N = actual count of `prevents:`-prefixed
actions):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Publisher Gate** — Verify and emit after the ACTIONS GATE line:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Collaboration signal table present
- [ ] Team Insight written as one sentence; Skeptic gate verified (Skeptic knew all
  achievement, milestone, inertia, velocity, Dashboard, stale, and nearest-miss data;
  insight is a new cross-dimensional inference)
- [ ] Nearest-miss Level 1 present (or Level 2 with "Level 1 empty" note), sorted ascending
- [ ] Pre-write check complete; at least 3 actions with namespace + topic + exact achievement;
  `prevents:`, `resolves:`, and `requires:` annotations applied per 3.4
- [ ] ACTIONS GATE line written with actual N count substituted

---

## V-04 — Inertia-First Lifecycle + 4-Role Pipeline + Seeds D + G

**Axis**: Combination — lifecycle emphasis (inertia before health) + role sequence (4-role)
**Hypothesis**: R11 V-03 explored inertia-first lifecycle ordering but scored 99.13 (21/23)
because the phase-based structure had no named role pipeline (failing C-26 and C-28). R12
V-04 restructures as a 4-role pipeline: Archivist → Assessor → Synthesizer → Publisher.
The Assessor role runs Phase 2a (Inertia) before Phase 2b (Health), inverting the standard
order. This tests whether trajectory-first assessment changes what the Synthesizer and
Publisher synthesize — the model has committed to a momentum picture before it knows the
achievement counts, which may surface different second-order patterns than health-first
ordering. Seed D (inertia severity tier) added to the Assessor's inertia table. Seed G
(co-contribution network map) introduced in the Synthesizer role.

---

You are running the **Corps Leaderboard** skill in a 4-role inertia-first pipeline. Execute
each role completely before advancing to the next. No role may perform work assigned to
another role. Output each Gate checklist and Handoff artifact list verbatim before the next
role begins.

In this pipeline, the Assessor runs the **Inertia Phase (Phase 2a) before the Health Phase
(Phase 2b)** — trajectory is assessed before current state. The contamination boundary
enforces in both directions: Phase 2a must not contain static counts belonging to Phase 2b;
Phase 2b must not restate trajectory claims from Phase 2a.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. The Archivist scans the workspace, builds the
signal registry, and constructs the contributor index. The Archivist does NOT evaluate
achievements, assess trajectory, rank contributors, or write insights or actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. Record:

- `topic_path` — path after `simulations/`
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. Roles 2, 3, and 4 do not
run.

Print registry: `topic_path | namespace | contributor | file`

Print namespace coverage:
`Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`
The 9 namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

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

**Responsibility**: Per-topic evaluation only. The Assessor runs the Inertia Phase first
(Phase 2a), then the Health Phase (Phase 2b), then the nearest-miss assessment. These
sub-phases are structurally separate. The Assessor does NOT rank contributors, write insights,
or write actions.

### 2.1 — Phase 2a: Inertia Phase (RUNS FIRST)

Reports trajectory and momentum only. Does NOT report file counts, achievement statuses, or
coverage totals — those are current-state data belonging to Phase 2b.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Append a `severity` column:
- `critical` — 2 or more flags raised (not counting healthy-momentum)
- `warning` — exactly 1 flag raised
- `healthy` — 0 flags or only healthy-momentum

Print inertia table: `topic_path | flags | trajectory note | severity`

After the per-topic rows, print an Inertia Flag Cluster Table:

```
## Inertia Clusters

| Flag             | Topics                                    | Count |
|------------------|-------------------------------------------|-------|
| stuck-at-first   | {comma-separated topic_paths or "none"}   | {N}   |
| solo-hold        | {comma-separated topic_paths or "none"}   | {N}   |
| namespace-thin   | {comma-separated topic_paths or "none"}   | {N}   |
| healthy-momentum | {comma-separated topic_paths or "none"}   | {N}   |
```

Print velocity summary:
`Signal velocity: {N_signals} / {N_topics} | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

Print stale signal table: `topic_path | stale_status` (`stale`, `active`, `date-unknown`).

### 2.2 — Phase 2b: Health Phase (RUNS SECOND)

Reports current signal state only. Does NOT restate inertia flags or trajectory claims from
Phase 2a.

For each `topic_path`, print:

```
### topic: {topic_path}
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {N}/9
```

Evaluate all five achievements. Exact names only. For every LOCKED achievement, state the
specific unlock requirement in the evidence cell.

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

When Solo Pioneer is EARNED and Team Topic is NOT YET: append
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]`.

Evaluate all three team milestones. Exact names. Evidence must be non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

Print debate starter proximity:
`Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count` per active namespace.

### 2.3 — Nearest-Miss Assessment

- **Level 1**: every topic 1 unit away (topic + achievement + exact gap). Sort ascending.
- **Level 2**: closest topic 2 units away. Only when no Level 1 exists. State "Level 1: no
  topics are 1 unit away" first.

Print: `topic | achievement | gap | level`

**Assessor Gate** — Verify and emit before transferring artifacts:

- [ ] Phase 2a: inertia table present with severity column; every topic evaluated; cluster
  table present; velocity trend and stale signal table present
- [ ] Phase 2a: no static file counts or achievement statuses appear (prohibited)
- [ ] Phase 2b: every topic has complete health block with all five rows; LOCKED rows include
  unlock paths; all three milestone names verbatim with non-empty evidence; debate starter
  proximity and namespace leader table present
- [ ] Phase 2b: no trajectory claims or inertia flags restated from Phase 2a (prohibited)
- [ ] Nearest-miss complete (Level 1, or Level 2 with "Level 1 empty" note)
- [ ] Phase 2a gate: inertia table present; no static counts; cluster table present

**Assessor Handoff** — Artifacts to Synthesizer:

1. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`, `severity`)
2. Inertia Flag Cluster Table
3. Velocity summary and stale signal table
4. Per-topic Health Phase achievement blocks (with tension markers and unlock paths)
5. Team milestone table (3 rows)
6. Nearest-miss table (columns: `topic`, `achievement`, `gap`, `level`)

---

## ROLE 3: SYNTHESIZER

**Responsibility**: Team-level synthesis artifacts only. The Synthesizer produces the
Contributor Leaderboard, the Co-Contribution Network Map, and a nearest-miss confirmation.
The Synthesizer does NOT write the Team Insight, the reconciliation pairing, or the Next
Actions — those belong to the Publisher.

### 3.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical. If all `unknown`:
`| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 3.2 — Co-Contribution Network Map

Produce a structured network artifact for all topics where Team Topic is earned. For each
such topic, list all contributors as named nodes and compute the pair count.

```
## Co-Contribution Network

| Topic | Contributor nodes | Pair count |
|-------|-------------------|------------|
| {topic_path} | {comma-separated contributor names} | {N*(N-1)/2} |
```

If no topic earned Team Topic: one row `| none | — | 0 |`.

After the table, identify any contributor appearing in 2 or more Team Topic topics as a
**collaboration bridge**. Name them explicitly. If none qualify, write
`Collaboration bridges: none`.

### 3.3 — Nearest-Miss Confirmation

Transcribe and format the nearest-miss assessment from the Assessor Handoff. Do not recompute.

**Synthesizer Gate** — Verify and emit before transferring artifacts:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Co-Contribution Network Map present (or "none" row)
- [ ] Collaboration bridge identification present
- [ ] Nearest-miss confirmed and formatted

**Synthesizer Handoff** — Artifacts to Publisher:

1. Contributor Leaderboard table
2. Co-Contribution Network Map table with collaboration bridge identification
3. Nearest-miss assessment (from Assessor, confirmed)

The Publisher begins with all output from Archivist, Assessor, and Synthesizer. It does not
re-assess actions or re-evaluate inertia.

---

## ROLE 4: PUBLISHER

**Responsibility**: Cross-dimensional reconciliation, Team Insight, and Next Actions only.
Works from all prior output. Does NOT re-scan, re-evaluate, or re-assess.

### 4.1 — Cross-Dimensional Reconciliation

Before writing the Team Insight, emit a reconciliation pairing. Select one observation from
Phase 2b (Health) and one from Phase 2a (Inertia) that interact with or bear on each other.
State how they interact.

```
## Reconciliation

| Health observation (Phase 2b) | Inertia observation (Phase 2a) | Interaction |
|-------------------------------|-------------------------------|-------------|
| {one finding from Health Phase} | {one finding from Inertia Phase} | {connection} |
```

The Team Insight must advance beyond this reconciliation. An insight that merely restates
the reconciliation row fails.

### 4.2 — Team Insight

**Skeptic gate**: The Skeptic has read all output from the Archivist, Assessor, and
Synthesizer — every inertia flag, every severity tier, every trajectory note, every cluster
table row, every achievement table, every milestone row, the nearest-miss, the leaderboard,
the co-contribution network map, and the reconciliation pairing in 4.1. The insight must
contain something the Skeptic would not already know from all of that.

An insight that echoes an inertia flag, cluster row, or network topology already visible
fails. An insight that restates the reconciliation pairing fails. A passing insight surfaces
a second-order pattern requiring synthesis across inertia-first observations and health data
in a way no single block, the cluster table, the network map, or the reconciliation pairing
directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic.

### 4.3 — Pre-Write Check

Before writing actions, identify all zero-score conditions: topics with 0 files, empty
registry, empty leaderboard.

**prevents: prefix rule** — stated here for the Pre-Write Check AND embedded inside each
relevant action row below: any action whose primary purpose is eliminating a state where the
output would score zero uses the `prevents:` prefix. These are two structurally independent
enforcement points.

Also identify all open inertia flags from Phase 2a. Actions resolving an inertia flag declare
`resolves: {flag-name}`.

### 4.4 — Next Actions

Write at least 3 actions. Each must name: (1) a specific namespace and topic path,
(2) the exact achievement or milestone it unlocks.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag} or blank]
2. ...
3. ...
```

After all actions, output exactly (N = actual count of `prevents:`-prefixed actions):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Publisher Gate** — Verify and emit after the ACTIONS GATE line:

- [ ] Reconciliation pairing written with one Health observation, one Inertia observation,
  and interaction note
- [ ] Team Insight written as one sentence; Skeptic gate verified — Skeptic knew all inertia
  flags, severity tiers, cluster data, achievement tables, milestone rows, nearest-miss,
  leaderboard, co-contribution network, and reconciliation pairing; insight is a new
  cross-dimensional inference
- [ ] At least 3 actions with namespace + topic + exact achievement or milestone
- [ ] `prevents:` applied to zero-score-condition actions (two independent enforcement points)
- [ ] `resolves:` applied to inertia-flag-resolving actions; blank for others
- [ ] ACTIONS GATE line written with actual N count substituted

---

## V-05 — Full Integration: 4-Role + All Seeds A + B + D + E + F + G

**Axis**: Full integration — 4-role pipeline + inertia severity tier + Narrator confidence
gate + action dependency chain + co-contribution network map + `resolves:` annotation +
pre-synthesis reconciliation with confidence
**Hypothesis**: R11 V-05 holds 23/23 = 100.00 and seeds C-32 (resolves:) and C-33
(reconciliation pairing) for v12. R12 V-05 carries all 23 criteria forward, formalizes both
R11 seeds as explicit structural requirements, and introduces four new seeds (D, E, F, G) as
v12 candidates. The 4-role pipeline (Archivist/Analyst/Strategist/Narrator) provides three
handoffs for strong C-28 coverage; each role has a per-role checklist gate (C-29); the
Analyst runs health/inertia structurally separated (C-27, C-30); the Narrator's Skeptic scope
names inertia flags explicitly (C-31). Expected: 23/23 = 100.00. Seeds v12-C-32 through
v12-C-38.

---

You are running the **Corps Leaderboard** skill in a 4-role pipeline. Execute each role
completely before advancing to the next. No role may perform work assigned to another role.
Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. The Archivist scans the workspace, emits the Sprint
Velocity Dashboard, builds the signal registry, and constructs the contributor index. The
Archivist does NOT evaluate achievements, assess trajectory, rank contributors, or write
insights or actions.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. Record four fields per file:

- `topic_path` — path after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. Roles 2, 3, and 4 do not
run.

### 1.2 — Sprint Velocity Dashboard

Emit as the first output block, before the registry table:

```
## Sprint Velocity Dashboard

| Metric                    | Value                                        |
|---------------------------|----------------------------------------------|
| Total signals             | {total file count}                           |
| Topics active             | {distinct topic_path count}                  |
| Namespaces active         | {distinct namespace count} / 9               |
| Empty namespaces          | {list or "none"}                             |
| Contributors              | {distinct non-unknown contributor count}     |
| Solo-held topics          | {topics with exactly 1 contributor}          |
| Multi-contributor topics  | {topics with 2+ contributors}                |
| Velocity posture          | {expanding / stable / stalled} (preliminary) |
```

Velocity posture (preliminary, scan-only):
- `expanding` — multi-contributor >= 50% of topics
- `stalled` — multi-contributor < 25% AND solo-held >= 50%
- `stable` — otherwise

### 1.3 — Signal Registry

After the dashboard, print registry: `topic_path | namespace | contributor | file`

Print namespace coverage:
`Namespaces active: {N} of 9 | Active: {list} | Empty: {list}`
The 9 Signal namespaces: `scout, draft, review, flow, trace, prove, listen, program, topic`.

### 1.4 — Contributor Index

Print: `contributor | topic_path | file_count`.

**Archivist Gate** — Verify and emit:

- [ ] Sprint Velocity Dashboard printed as first output block, before registry
- [ ] Registry table printed with all four columns
- [ ] Namespace coverage line present with active and empty lists
- [ ] Contributor index present with all three columns

**Archivist Handoff** — Artifacts to Analyst:

1. Sprint Velocity Dashboard (with preliminary posture)
2. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
3. Namespace coverage line
4. Contributor index (columns: `contributor`, `topic_path`, `file_count`)

The Analyst begins with these four artifacts. It does not re-scan the workspace.

---

## ROLE 2: ANALYST

**Responsibility**: Evaluation only. The Analyst assesses registry data and reports current
state (Health Phase) then trajectory (Inertia Phase). These sub-phases are structurally
separated — Health Phase content must not appear in the Inertia Phase and vice versa. The
Analyst does NOT rank contributors, write insights, or write actions.

### 2.1 — Health Phase

Reports current signal state only: file counts, namespace coverage, contributor counts,
achievement status. Does NOT report trajectory, momentum, or stall indicators.

For each `topic_path`, print:

```
### topic: {topic_path}
Health — Files: {N} | Namespaces: {list} | Contributors: {list} | Namespace diversity: {N}/9
```

Evaluate all five achievements. Exact names only. For every LOCKED achievement, state the
specific unlock requirement in the evidence cell.

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
| First Signal  | ...     | ...                                 |
| Signal Depth  | ...     | ...                                 |
| Full Sweep    | ...     | ...                                 |
| Solo Pioneer  | ...     | ...                                 |
| Team Topic    | ...     | ...                                 |
```

When Solo Pioneer is EARNED and Team Topic is NOT YET: append
`[TENSION: solo hold — unlock requires 1 additional contributor with >= 1 signal]`.

Evaluate all three team milestones. Exact names. Evidence must be non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Print: `milestone | status | evidence`

Print: `Debate starter: nearest topic is {name} with {N}/3 contributors ({M} more needed)`

Print namespace leader table: `namespace | leader | signal_count` per active namespace.

### 2.2 — Inertia Phase

Reports trajectory and momentum only. Structurally separate from Health Phase. Does NOT
restate file counts or achievement statuses from Health Phase.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Append severity tier:
- `critical` — 2 or more flags raised (not counting healthy-momentum)
- `warning` — exactly 1 flag raised
- `healthy` — 0 flags or only healthy-momentum

Print inertia table: `topic_path | flags | trajectory note | severity`

After the per-topic rows, print an Inertia Flag Cluster Table:

```
## Inertia Clusters

| Flag             | Topics                                    | Count |
|------------------|-------------------------------------------|-------|
| stuck-at-first   | {comma-separated topic_paths or "none"}   | {N}   |
| solo-hold        | {comma-separated topic_paths or "none"}   | {N}   |
| namespace-thin   | {comma-separated topic_paths or "none"}   | {N}   |
| healthy-momentum | {comma-separated topic_paths or "none"}   | {N}   |
```

Print stale signal table: `topic_path | stale_status` (`stale`, `active`, `date-unknown`).

Print velocity summary and Dashboard update:
`Velocity posture update: preliminary was {X} — Inertia Phase confirms {Y} | {Nh} healthy / {Nw} warning / {Nc} critical | Trend: {increasing/flat/stalled}`

### 2.3 — Nearest-Miss Assessment

- **Level 1**: every topic 1 unit away (topic + achievement + exact gap). Sort ascending.
- **Level 2**: closest topic 2 units away. Only when no Level 1 exists. State "Level 1: no
  topics are 1 unit away" first.

Print: `topic | achievement | gap | level`

**Analyst Gate** — Verify and emit before transferring artifacts:

- [ ] Every topic has Health Phase block with all five rows; LOCKED rows include unlock paths;
  no trajectory language in Health Phase output
- [ ] All three milestone names verbatim with non-empty evidence; debate starter proximity
  and namespace leader table present
- [ ] Inertia Phase table present with severity column; every topic evaluated; Cluster Table
  present; stale signal table and velocity summary present
- [ ] Inertia Phase table present; no static counts restated from Health Phase
- [ ] Nearest-miss complete (Level 1, or Level 2 with "Level 1 empty" note)

**Analyst Handoff** — Artifacts to Strategist:

1. Per-topic Health Phase blocks (one block per `topic_path`, with tension markers and unlock
   paths)
2. Team milestone table (3 rows: milestone, status, evidence)
3. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`, `severity`)
4. Inertia Flag Cluster Table
5. Stale signal table and velocity summary with Dashboard posture update
6. Nearest-miss assessment table (columns: `topic`, `achievement`, `gap`, `level`)

The Strategist begins with these six artifacts plus the Archivist's four. It does not
re-evaluate achievements or re-assess inertia.

---

## ROLE 3: STRATEGIST

**Responsibility**: Actions and nearest-miss synthesis only. Works from the Analyst's output.
The Strategist does NOT produce the Contributor Leaderboard, the Co-Contribution Network Map,
the reconciliation pairing, or the Team Insight — those belong to the Narrator.

### 3.1 — Nearest-Miss Confirmation

Transcribe and output the nearest-miss assessment from the Analyst Handoff. Do not recompute.

### 3.2 — Pre-Write Check

Before writing any action, identify all zero-score conditions: topics with 0 files, empty
registry, empty leaderboard. Record each explicitly.

**prevents: prefix rule** — stated here as the first of two structurally independent
enforcement points: any action whose primary purpose is eliminating a state where the output
would score zero carries the `prevents:` prefix. Advancement actions do not.

Also identify all open inertia flags from the Analyst's Inertia Phase table. An action whose
primary purpose is resolving an inertia flag MUST declare `resolves: {flag-name}`. Actions
that do not resolve a specific inertia flag leave `resolves:` blank.

Identify actions that depend on a prior action in the sequence — for example, an action
advancing Signal Depth on a topic that currently has no signals depends on a prior action
that adds the first signal. Declare such dependencies using `requires: {action-N}`.
Independent actions leave `requires:` blank.

### 3.3 — Next Actions

Write at least 3 actions. Each must name: (1) a specific namespace and topic path,
(2) the exact achievement or milestone it unlocks. The `prevents:` prefix rule is embedded
inside each relevant action row below as the second structurally independent enforcement
point.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag} or blank] [requires: {action-N} or blank]
2. ...
3. ...
```

After all actions, output exactly this line (N = actual count of `prevents:`-prefixed
actions):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Strategist Gate** — Verify and emit after the ACTIONS GATE line:

- [ ] Nearest-miss confirmation present and formatted
- [ ] Pre-write check complete; zero-score conditions and open inertia flags identified
  before any action written
- [ ] At least 3 actions written; each names namespace + topic + exact achievement or
  milestone
- [ ] `prevents:` applied to all zero-score-condition actions (two independent enforcement
  points: 3.2 and 3.3)
- [ ] `resolves:` annotation applied to all inertia-flag-resolving actions; blank for others
- [ ] `requires:` annotation applied to all sequentially dependent actions; blank for
  independent actions
- [ ] ACTIONS GATE line written with actual N count substituted

**Strategist Handoff** — Artifacts to Narrator:

1. Nearest-miss assessment (from Analyst, confirmed)
2. Next Actions list (all rows with `prevents:`, `resolves:`, and `requires:` annotations)
3. Pre-write check results (zero-score conditions and open inertia flags identified)
4. ACTIONS GATE line (with N substituted)

The Narrator begins with all output from Archivist, Analyst, and Strategist. It does not
re-assess actions, re-evaluate inertia, or modify the action list.

---

## ROLE 4: NARRATOR

**Responsibility**: Synthesis only. The Narrator produces the Contributor Leaderboard, the
Co-Contribution Network Map, the cross-dimensional reconciliation pairing with confidence
annotation, and the Team Insight. The Narrator does NOT re-scan, re-evaluate achievements,
re-assess inertia, or modify the action list.

### 4.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical. If all `unknown`:
`| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 4.2 — Co-Contribution Network Map

Produce a structured network artifact for all topics where Team Topic is earned:

```
## Co-Contribution Network

| Topic | Contributor nodes | Pair count |
|-------|-------------------|------------|
| {topic_path} | {comma-separated contributor names} | {N*(N-1)/2} |
```

If no topic earned Team Topic: one row `| none | — | 0 |`.

After the table, identify any contributor appearing in 2 or more Team Topic topics as a
**collaboration bridge**. Name them. If none qualify: `Collaboration bridges: none`.

### 4.3 — Cross-Dimensional Reconciliation with Confidence Annotation

Before writing the Team Insight, emit a reconciliation pairing. Select exactly one
observation from the Health Phase and one from the Inertia Phase that interact with or bear
on each other. State how they interact.

Immediately after the pairing, emit a confidence annotation:

- `confidence: high` — interaction directly supported by specific evidence in both phases;
  a skeptical reader accepts it without argument
- `confidence: medium` — plausible but requires one inferential step; skeptical reader may
  ask for clarification
- `confidence: low` — speculative; requires two or more inferential steps

State the rationale in one sentence.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase} | {one finding from Inertia Phase} | {connection} |

Confidence: {high/medium/low} — {rationale sentence}
```

The Team Insight in 4.4 must advance beyond both the reconciliation pairing and its
confidence framing. An insight that restates the reconciliation row fails. An insight that
only adjusts the confidence level fails.

### 4.4 — Team Insight

**Skeptic gate**: The Skeptic has read all output from the Archivist, Analyst, and Strategist
— every achievement table, every milestone row, every inertia flag, every trajectory note,
every severity tier, the Inertia Flag Cluster Table, the stale signal list, the velocity
summary with Dashboard posture update, the nearest-miss assessment, all actions with their
`prevents:`, `resolves:`, and `requires:` annotations, the leaderboard, the co-contribution
network map, the reconciliation pairing, and the confidence annotation in 4.3. The insight
must contain something the Skeptic would not already know from all of that material.

An insight that echoes an inertia flag already in the Inertia Phase fails. An insight that
restates the reconciliation pairing fails. An insight that only comments on the confidence
level fails. An insight that merely recounts co-contribution topology already visible in
the network map fails. An insight that describes what the actions already address fails.
A passing insight surfaces a second-order pattern — a risk, convergence, or cross-topic
trajectory inference — that requires synthesizing across health and inertia in a way no
single block, cluster table, network map, action row, or the reconciliation pairing with its
confidence framing directly reveals.

Write one sentence: (1) cross-topic conclusion, (2) concrete number, (3) specific contributor
or topic, (4) information the Skeptic acknowledges as new given full knowledge of all prior
output and the reconciliation pairing with its confidence annotation.

**Narrator Gate** — Verify and emit:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Co-Contribution Network Map present (or "none" row); collaboration bridges identified
- [ ] Reconciliation pairing written with one Health observation, one Inertia observation,
  and interaction note
- [ ] Confidence annotation present (high/medium/low) with one-sentence rationale
- [ ] Team Insight written as one sentence; Skeptic gate verified — Skeptic knew every
  achievement table, milestone row, inertia flag, severity tier, cluster row, stale status,
  velocity posture, nearest-miss, all action annotations (prevents:/resolves:/requires:),
  leaderboard, network map, reconciliation, and confidence data; insight is a new
  cross-dimensional inference beyond all of that

---

## Seed Pattern Reference

Six patterns introduced or formalized in R12 (distributed across V-01 through V-05).
These are candidates for v12 criteria if they appear in R12 excellence signals.

### Seed A — Inertia Flag-to-Action Traceability (candidate v12-C-32)

`resolves: {flag-name}` annotation in action rows whose primary purpose is resolving an
inertia flag. Formally structured in R12 V-01, V-02, V-03, V-04, V-05.

Orthogonal to: C-20/C-22/C-24 (concern `prevents:` for zero-score); C-05 (requires
achievement name in actions). C-32 tests whether actions are explicitly linked to the
trajectory dimension — not just achievement thresholds. Presupposes C-27.

### Seed B — Pre-Synthesis Cross-Dimensional Reconciliation (candidate v12-C-33)

Named reconciliation pairing (one Health × one Inertia observation) emitted before the Team
Insight. Formally structured in R12 V-02, V-04, V-05.

Orthogonal to: C-25 (novelty constraint); C-31 (Skeptic knowledge scope). C-33 tests whether
a named intermediate artifact is required before synthesis — not just a novelty gate or a
knowledge-scope expansion. Presupposes C-27 and C-31.

### Seed D — Inertia Severity Tier per Topic (candidate v12-C-34)

A `severity` column appended to the inertia table: `critical` (2+ flags), `warning` (1 flag),
`healthy` (0 flags or healthy-momentum only). Introduced in R12 V-01, V-04, V-05.

Orthogonal to: C-07 (momentum indicator, which is flag-existence at topic level); C-17
(velocity trend, which is team-level aggregate). C-34 tests whether the inertia table has an
explicit urgency tier per topic — not just flag names — enabling tier-based prioritization
of attention and actions. Presupposes C-27.

### Seed E — Narrator Confidence Gate for Reconciliation Pairing (candidate v12-C-35)

Before writing the Team Insight, the Narrator emits a confidence annotation (high/medium/low)
for the reconciliation pairing and states the rationale. The insight must advance beyond both
the pairing and its confidence framing. Introduced in R12 V-02 and V-05.

Orthogonal to: C-33 (tests whether the reconciliation pairing exists); C-25 (tests novelty
relative to analysis, not relative to a committed confidence framing). C-35 tests whether
the model must first commit to an epistemic position on its cross-dimensional observation
before writing the insight — raising the bar from "advance beyond the data" to "advance
beyond your own committed framing of the data." Presupposes C-27, C-31, C-33.

### Seed F — Action Dependency Chain (candidate v12-C-36)

Actions that depend on a prior action in the sequence declare `requires: {action-N}`.
Introduced in R12 V-03 and V-05.

Orthogonal to: C-20/C-22/C-24 (concern `prevents:` for zero-score); C-32 (concerns
`resolves:` for inertia flags). C-36 tests whether the action layer carries explicit
sequencing constraints — a DAG structure enabling sprint-level planning — rather than a flat
independent list. A prompt that requires achievement naming and `resolves:` / `prevents:`
annotations but leaves action ordering implicit fails C-36.

### Seed G — Co-Contribution Network Map (candidate v12-C-37)

A structured network artifact listing all topics where Team Topic is earned, with contributor
nodes and pair counts. Collaboration bridges (contributors in 2+ Team Topic topics) named
explicitly. Introduced in R12 V-04 and V-05.

Orthogonal to: C-09 (contributor collaboration signal, which only confirms existence of
multi-contributor topics); C-04 (leaderboard, which ranks by count not network position).
C-37 tests whether the output provides a network topology artifact — nodes, edges, bridges —
not just collaboration presence statistics. The network map enables topology inference that
the leaderboard and collaboration callout alone cannot produce.
