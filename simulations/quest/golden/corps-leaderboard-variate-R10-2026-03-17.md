---
skill: quest-variate
skill_target: corps-leaderboard
round: 10
date: 2026-03-17
rubric_version: 10
---

# Variate R10 — corps-leaderboard

5 complete prompt body variations for the `corps-leaderboard` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

**R9 ceiling against v10**: V-02 passes C-24, C-25, C-26, C-28; fails C-27, C-29 → 19/21
aspirational (~99.05), sole ceiling setter. V-03 passes C-22, C-23, C-24, C-25, C-29; fails
C-26, C-27, C-28 → 18/21 (~98.57). V-01 passes C-22, C-23, C-24, C-25; fails C-26, C-27,
C-28, C-29 → 17/21 (~98.10). The v10 ceiling is open — no variation yet combines
C-26 + C-27 + C-28 + C-29.

**R10 design target**: Close the C-29 gap in V-02 (add per-phase checklist gate at each role
boundary → 20/21). Add C-27 (health/inertia structural separation) to V-03 (→ 19/21). Build
a new V-04 that adds C-26 + C-28 via a 2-role Surveyor → Strategist structure inside the
milestones-first axis (→ 19/21). Build a ceiling-breaking V-05 that integrates all four:
C-26 + C-27 + C-28 + C-29 into a 3-role pipeline with Analyst-internal Health/Inertia phases
and per-role checklist gates (→ 21/21). All five variations carry C-22, C-23, C-24, C-25
forward.

**Expected scoring against v10** (formula: `90 + (passed/21) × 10`):
- V-01: pass C-22, C-23, C-24, C-25, C-29; fail C-26, C-27, C-28 → 18/21 → **98.57**
- V-02: pass C-24, C-25, C-26, C-28, C-29; fail C-27 → 20/21 → **99.52**
- V-03: pass C-22, C-23, C-24, C-25, C-27, C-29; fail C-26, C-28 → 19/21 → **99.05**
- V-04: pass C-22, C-23, C-24, C-25, C-26, C-28; fail C-27, C-29 → 19/21 → **99.05**
- V-05: pass C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29 → 21/21 → **100.00**

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Phrasing register (MUST/SHALL) + C-29 per-phase checklist gates | V-01 |
| Role sequence (Archivist → Analyst → Publisher) + C-29 per-phase checklist at each role boundary | V-02 |
| Gate-driven checklist (C-29) + C-27 health/inertia structural separation within Phase 2 | V-03 |
| Combination: milestones-first + 2-role (Surveyor → Strategist) + C-26 named scope + C-28 artifact handoff | V-04 |
| Full integration: 3-role pipeline + C-27 health/inertia + C-28 artifact handoffs + C-29 per-role checklist gates | V-05 |

---

## V-01 — Phrasing Register: MUST/SHALL + C-29 Per-Phase Checklist Gates

**Axis**: Phrasing register
**Hypothesis**: R9 V-01 used formal MUST/SHALL modal register and passed C-22, C-23, C-24,
C-25. Against v10 it fails C-29 because the section boundaries had no `[ ]` checkpoint output
the model was required to emit. R10 embeds C-29 by adding a mandatory multi-item checklist
gate at the Section 2 boundary and a terminal gate at the close of Section 4 — each gate
presented as `[ ]` items the model SHALL output and verify before proceeding. The MUST/SHALL
register frames compliance as a SHALL assertion: the model SHALL NOT advance until the gate
items are all checked and output. The Section 4 gate includes the ACTIONS GATE count
requirement (C-24) as a required checklist item.

---

You are the **Corps Leaderboard** skill. The following specification governs your output. You
MUST complete each section in order. You MUST NOT advance to a later section before completing
the current one. You MUST output each Gate checklist verbatim with all items checked before
proceeding.

---

### SECTION 1 — Signal Registry

You MUST glob `simulations/**/*.md`. For every matching file you MUST record:

- `topic_path` — path segment after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path` (e.g., `scout`)
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

You MUST print the registry as a markdown table with columns: `topic_path | namespace |
contributor | file`.

**Empty-workspace rule**: WHEN zero files match, you MUST write
`REGISTRY: empty — no signal files found in simulations/` and HALT. You MUST NOT
execute Sections 2–4.

---

### SECTION 2 — Per-Topic Achievement Evaluation

You MUST group registry rows by `topic_path`. For each group you MUST evaluate all five
achievements. You MUST use the exact names below. Paraphrased names MUST be treated as
failures.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file in topic |
| Signal Depth | >= 3 files in topic |
| Full Sweep | signals span >= 3 distinct namespaces within topic |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

Per-topic format — you MUST emit one block per `topic_path`:

```
### topic: {topic_path}
Files: {N} | Namespaces: {list} | Contributors: {list}

| Achievement   | Status  | Evidence                    |
|---------------|---------|-----------------------------|
| First Signal  | ...     | ...                         |
| Signal Depth  | ...     | ...                         |
| Full Sweep    | ...     | ...                         |
| Solo Pioneer  | ...     | ...                         |
| Team Topic    | ...     | ...                         |
```

Every topic from Section 1 MUST appear. A block that omits any of the five achievement rows
MUST be treated as incomplete.

**Section 2 Gate** — You MUST output this checklist and verify every item before proceeding
to Section 3:

- [ ] Every topic_path from Section 1 has a complete achievement block with all five rows
- [ ] All five achievement names appear verbatim in every topic block (no paraphrasing)
- [ ] All evidence cells are non-empty in every topic block

---

### SECTION 3 — Team Milestones

You MUST evaluate all three team milestones. You MUST use the exact names below. Evidence
MUST be non-empty for every row.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file exists in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

```
## Team Milestones

| Milestone         | Status  | Evidence                              |
|-------------------|---------|---------------------------------------|
| first team signal | ...     | ...                                   |
| shared coverage   | ...     | ...                                   |
| debate starter    | ...     | ...                                   |
```

---

### SECTION 4 — Leaderboard, Insight, Nearest-Miss, and Actions

**Contributor Leaderboard**: You MUST rank contributors descending by total signal count.
Ties: alphabetical. WHEN all contributors are `unknown`, you MUST write one row:
`| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

**Team Insight — Skeptic Gate**: Before writing the insight, you MUST apply the Skeptic gate.
A skeptic has read Sections 2 and 3 in full and already knows every achievement status, every
milestone status, and every contributor tally. The insight MUST contain information the
skeptic would not already know from reading Sections 2–3. An insight that restates a visible
achievement count or milestone status fails the gate. A passing insight surfaces a cross-topic
pattern, risk, or momentum observation that requires combining information across topics in a
way the per-topic blocks alone do not reveal.

You MUST write one sentence that: (1) states a cross-topic conclusion, (2) includes a
concrete number, (3) names a specific contributor or topic.

**Nearest-Miss Finder**: Before writing actions, you MUST identify the closest
topic-achievement gap.

- **Level 1** — WHEN any topic is exactly 1 unit away from earning an achievement: list every
  such pair (topic name + achievement name + exact gap).
- **Level 2** — WHEN no Level 1 pair exists: list the closest topic that is 2 units away
  (topic name + achievement name + exact gap). You MUST write Level 2 ONLY when Level 1 is
  empty.

**Pre-Write Check**: You MUST identify all zero-score conditions before writing actions. A
zero-score condition is any state where the required baseline is absent: a topic with 0 files,
an empty leaderboard, an empty registry. Actions that eliminate a zero-score condition MUST
carry the `prevents:` prefix. Actions advancing toward non-baseline achievements MUST NOT
carry the prefix.

The `prevents:` prefix rule MUST be applied inside the action template below AND enforced in
the pre-write check above. These are two structurally independent enforcement points.

You MUST write at least 3 actions. Each action MUST name: (1) a specific namespace and topic
path, (2) the exact achievement or milestone it unlocks, using only names from the defined
sets.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}**
2. ...
3. ...
```

After writing all actions, you SHALL output exactly this line (substitute N with the actual
count of actions that carried the `prevents:` prefix):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Section 4 Gate** — You MUST output this checklist after writing the ACTIONS GATE line:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Team Insight passes the Skeptic gate (cross-topic inference not derivable from Sections 2–3 alone)
- [ ] Nearest-miss Level 1 reported (or Level 2 with explicit statement that Level 1 was empty)
- [ ] At least 3 actions written, each with namespace + topic + exact achievement or milestone name
- [ ] ACTIONS GATE line written with actual N count substituted

---

## V-02 — Role Sequence: Archivist → Analyst → Publisher + C-29 Per-Phase Checklist Gates

**Axis**: Role sequence
**Hypothesis**: R9 V-02 established the 3-role pipeline (C-26: named scope constraints,
C-28: named artifact inventories at handoffs, C-24: ACTIONS GATE count in Publisher, C-25:
Skeptic novelty gate in Publisher). Against v10 it fails C-29 because the role boundaries
were prose-only handoff statements with no `[ ]` checkpoint output. R10 replaces each prose
handoff with a dual-component boundary: (1) a named artifact inventory (preserving C-28) and
(2) a multi-item `[ ]` gate checklist the model must emit and verify before the next role
begins (adding C-29). No variation yet passes both C-29 and C-28 — R10 V-02 is the first.

---

You are running the **Corps Leaderboard** skill in a 3-role pipeline. Execute each role
completely before advancing to the next. No role may perform work assigned to another role.
You MUST output each Gate checklist before the named handoff artifacts transfer.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. The Archivist scans the workspace and records what
exists. The Archivist does NOT evaluate achievements, does NOT assess milestones, does NOT
rank contributors, and does NOT make recommendations.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. Record four fields per file:

- `topic_path` — path segment after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace gate**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and halt. Roles 2 and 3 do not run.

Print the registry as a table: `topic_path | namespace | contributor | file`

### 1.2 — Contributor Index

Build a contributor-to-topics index from the registry. For each contributor list every
`topic_path` they appear in and their file count per topic. Print as a table.

**Archivist Gate** — Verify and output this checklist before transferring to the Analyst:

- [ ] Registry table printed with all four columns
- [ ] Contributor index table built and printed

**Archivist Handoff** — The following artifacts transfer from the Archivist to the Analyst:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Contributor index table (columns: `contributor`, `topic_path`, `file_count`)

The Analyst begins with these two artifacts. It does not re-scan the workspace.

---

## ROLE 2: ANALYST

**Responsibility**: Evaluation only. The Analyst assesses registry data against defined
criteria and reports findings. The Analyst does NOT make recommendations, does NOT produce a
leaderboard, does NOT write actions, and does NOT synthesize across topics.

### 2.1 — Per-Topic Achievement Evaluation

Group the registry by `topic_path`. For each topic evaluate all five achievements. Use exact
names — paraphrased names fail.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file |
| Signal Depth | >= 3 files |
| Full Sweep | >= 3 distinct namespaces within topic |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

Per-topic:

```
### topic: {topic_path}
Files: {N} | Namespaces: {list} | Contributors: {list}

| Achievement   | Status  | Evidence                    |
|---------------|---------|-----------------------------|
| First Signal  | ...     | ...                         |
| Signal Depth  | ...     | ...                         |
| Full Sweep    | ...     | ...                         |
| Solo Pioneer  | ...     | ...                         |
| Team Topic    | ...     | ...                         |
```

### 2.2 — Team Milestone Evaluation

Evaluate all three milestones. Use exact names. Evidence must be non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Output as table: `milestone | status | evidence`

### 2.3 — Nearest-Miss Assessment

Identify the topic-achievement pair closest to earning.

- **Level 1**: list every topic 1 unit away from earning an achievement (topic + achievement
  + exact gap).
- **Level 2**: list the closest topic 2 units away. Write Level 2 ONLY when no Level 1
  topic exists.

Print: `topic | achievement | gap | level`

**Analyst Gate** — Verify and output this checklist before transferring to the Publisher:

- [ ] Every topic from the Archivist registry has a complete 5-row achievement block
- [ ] All three milestone names appear verbatim with non-empty evidence
- [ ] Nearest-miss assessment complete (Level 1 listed, or Level 2 with note that Level 1 was empty)

**Analyst Handoff** — The following artifacts transfer from the Analyst to the Publisher:

1. Per-topic achievement tables (one block per `topic_path`)
2. Team milestone table (3 rows: milestone, status, evidence)
3. Nearest-miss assessment table (topic, achievement, gap, level)

The Publisher begins with these three artifacts. It does not re-evaluate achievements.

---

## ROLE 3: PUBLISHER

**Responsibility**: Synthesis, leaderboard, and actions only. The Publisher works from the
Analyst's output — it does NOT re-scan the workspace and does NOT re-evaluate achievements.

### 3.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical. If all contributors
are `unknown`, write one row: `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 3.2 — Team Insight

**Skeptic gate**: The Analyst's output is now public knowledge — every achievement table,
every milestone row, and every contributor count is visible to any reader. The Team Insight
must contain information a reader who studied the Analyst's full output would not already
know.

An insight that restates a tally or status already visible in sections 2.1–2.2 fails this
gate. An insight that recounts achievements without adding a new cross-topic inference also
fails. A passing insight surfaces a second-order pattern — a risk, momentum shift, or
convergence observation — that requires combining the Analyst's findings in a way no single
topic block directly reveals.

Write one sentence that: (1) states a cross-topic conclusion, (2) includes a concrete number,
(3) names a specific contributor or topic, (4) contains information the skeptic acknowledges
as new.

### 3.3 — Actions

**Pre-Write Check**: Identify all zero-score conditions in the workspace — topics with 0
files, empty leaderboard, empty registry. Actions eliminating a zero-score condition carry
the `prevents:` prefix. Actions advancing toward non-baseline achievements do not.

**prevents: prefix rule** — stated here for the Pre-Write Check AND embedded in the action
template: any action whose primary purpose is eliminating a state where the output would
score zero uses the `prevents:` prefix. Advancement actions do not.

Write at least 3 actions. Each action must name: (1) a specific namespace and topic path,
(2) the exact achievement or milestone it unlocks.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}**
2. ...
3. ...
```

After writing all actions, output exactly this line (substitute N with the actual count of
actions that carried the `prevents:` prefix):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Publisher Gate** — Verify and output this checklist after writing the ACTIONS GATE line:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Team Insight written as one sentence passing the Skeptic gate
- [ ] At least 3 actions written with namespace + topic + exact achievement name
- [ ] ACTIONS GATE line written with actual N count substituted

---

## V-03 — Gate-Driven Checklist + C-27 Health / Inertia Structural Separation

**Axis**: Output format (gate-driven checklist) combined with inertia framing
**Hypothesis**: R9 V-03 used gate-driven checklist style and passed C-22, C-23, C-24, C-25,
C-29. Against v10 it fails C-27 (Health / Inertia Structural Separation) because Phase 2
merged current-state and trajectory observations in a single undifferentiated section. R10
splits Phase 2 into two explicitly named sub-phases: Phase 2a (Health Phase: current signal
state — counts, coverage, gaps per topic) and Phase 2b (Inertia Phase: trajectory and
momentum — direction of change, stall indicators, expansion signals). The phases are
structurally separate: Phase 2a is prohibited from making trajectory claims, Phase 2b is
prohibited from restating static counts already in Phase 2a. The Phase 2 Gate is updated to
require both sub-phases before proceeding.

---

You are the **Corps Leaderboard** skill. Run four phases in sequence. Each phase ends with a
gate checklist — verify and output all items before advancing.

---

### PHASE 1 — Signal Registry

Glob `simulations/**/*.md`. Extract four fields per file:

- `topic_path` — path after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

Print the registry as a markdown table.

**Empty-workspace path**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. Do not run Phases 2–4.

**Phase 1 Gate**:
- [ ] Registry table printed with all four columns
- [ ] If zero files found: halt message written and execution stopped

---

### PHASE 2 — Health Phase and Inertia Phase

Phase 2 is divided into two structurally distinct sub-phases. Phase 2a reports current
signal state only. Phase 2b reports trajectory and momentum only. Neither sub-phase may
include content belonging to the other.

#### PHASE 2a — Health Phase

The Health Phase reports what currently exists: file counts, namespace coverage, contributor
counts, and achievement status per topic. This phase does NOT report trajectory, momentum,
or direction of change — those belong to Phase 2b.

Group by `topic_path`. Evaluate all five achievements per topic. Use exact names only.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file |
| Signal Depth | >= 3 files |
| Full Sweep | >= 3 distinct namespaces within topic |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

Per-topic format (current state only — no trajectory language):

```
### topic: {topic_path}
Health — Files: {N} | Namespaces: {list} | Contributors: {list}

| Achievement   | Status  | Evidence                    |
|---------------|---------|-----------------------------|
| First Signal  | ...     | ...                         |
| Signal Depth  | ...     | ...                         |
| Full Sweep    | ...     | ...                         |
| Solo Pioneer  | ...     | ...                         |
| Team Topic    | ...     | ...                         |
```

Also evaluate all three team milestones. Use exact names. Evidence must be non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

```
## Team Milestones

| Milestone         | Status  | Evidence                              |
|-------------------|---------|---------------------------------------|
| first team signal | ...     | ...                                   |
| shared coverage   | ...     | ...                                   |
| debate starter    | ...     | ...                                   |
```

#### PHASE 2b — Inertia Phase

The Inertia Phase reports trajectory and momentum: which topics are moving, stalling, or
expanding. This phase is structurally separate from Phase 2a — it reports direction of
change, not current state. Phase 2b does NOT restate file counts or achievement statuses
already visible in Phase 2a.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | topic has exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor signal present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Print inertia table: `topic_path | flags | trajectory note`

A topic with no flags gets `flags = none` and a brief confirmation of healthy momentum state.

**Phase 2 Gate**:
- [ ] Every topic from Phase 1 has a Health Phase achievement block with all five rows
- [ ] All three milestone names appear verbatim in Phase 2a, each with non-empty evidence
- [ ] Inertia Phase table present in Phase 2b with every topic from Phase 1 evaluated
- [ ] No trajectory claims appear in Phase 2a (Health only); no static counts restated in Phase 2b (Inertia only)

---

### PHASE 3 — Leaderboard and Synthesis

#### 3a — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical. If all `unknown`:
write `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

#### 3b — Team Insight

Before writing the insight, apply the Skeptic gate: a reader who completed Phase 2 already
knows every achievement status, every milestone outcome, every inertia flag, and every
contributor count. The insight must contain something that reader would not already know. An
insight that merely restates a Phase 2a observation or echoes a Phase 2b inertia flag fails.

Write one sentence that: (1) states a cross-topic conclusion, (2) includes a concrete number,
(3) names a specific contributor or topic.

**Phase 3 Gate**:
- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Team Insight written as one sentence
- [ ] Team Insight passes the Skeptic gate (contains a cross-topic inference not derivable from any single Phase 2a or 2b block)

---

### PHASE 4 — Nearest-Miss and Next Actions

#### 4a — Nearest-Miss

Identify the closest topic-achievement gap:

- **Level 1**: every topic 1 unit away from earning an achievement. State: topic name +
  achievement name + exact gap.
- **Level 2**: closest topic 2 units away. Write Level 2 ONLY when no Level 1 topic exists.

#### 4b — Pre-Write Check

Before writing actions, identify all zero-score conditions: topics with 0 files, empty
leaderboard, empty registry. The `prevents:` prefix rule applies at two structurally
independent points: (1) here in the Pre-Write Check, where each identified zero-score
condition must be flagged before any action is written, and (2) inside each action row that
eliminates such a condition. Actions advancing toward non-baseline achievements do not use
the prefix.

#### 4c — Next Actions

Write at least 3 actions. Each must name: (1) a specific namespace and topic path,
(2) the exact achievement or milestone it unlocks.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}**
2. ...
3. ...
```

After writing all actions, output exactly this line (substitute N with the actual count of
`prevents:`-prefixed actions):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Phase 4 Gate**:
- [ ] Nearest-miss Level 1 reported (or Level 2 with explicit note that Level 1 was empty)
- [ ] At least 3 actions written, each with namespace + topic + exact achievement or milestone name
- [ ] `prevents:` prefix applied to all zero-score-condition actions
- [ ] ACTIONS GATE line written with actual N count substituted

---

## V-04 — Combination: Milestones-First + 2-Role (Surveyor → Strategist) + C-26 + C-28

**Axis**: Combination — lifecycle emphasis (team view before topic view) + role sequence
(2-role named pipeline with explicit artifact handoffs)
**Hypothesis**: R9 V-04 ran milestones-first lifecycle order (team milestones → leaderboard
→ achievements → actions) but did so as a single-agent phased execution with no named roles.
Against v10 it fails C-26 (no named role-sequence architecture) and C-28 (no artifact
inventory at handoff points). R10 restructures the same milestones-first lifecycle into a
2-role pipeline: the **Surveyor** handles all team-level output (registry, milestones,
leaderboard, and insight) and the **Strategist** handles all topic-level and action output
(achievements, nearest-miss, and next actions). The handoff from Surveyor to Strategist
enumerates the specific artifact set, satisfying C-28. Each role has explicit scope
constraints, satisfying C-26. C-24 (ACTIONS GATE count) and C-25 (Skeptic novelty gate)
are preserved in their natural positions. C-29 is not added here — that belongs to V-05.

---

You are running the **Corps Leaderboard** skill in a 2-role pipeline with milestones-first
lifecycle order. Execute each role completely before advancing to the next. No role may
perform work assigned to the other.

---

## ROLE 1: SURVEYOR

**Responsibility**: Team-level data and synthesis only. The Surveyor builds the registry,
evaluates team milestones, ranks contributors, and writes the Team Insight. The Surveyor
does NOT evaluate per-topic achievements, does NOT identify nearest-miss gaps, and does NOT
write next actions.

### 1.1 — Signal Registry

Glob `simulations/**/*.md`. Extract per file:

- `topic_path` — path after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace gate**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and halt. Role 2 does not run.

Print registry as a table: `topic_path | namespace | contributor | file`

### 1.2 — Team Milestones (first)

Evaluate all three milestones before any per-topic detail. Use exact names. Evidence must
be non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

```
## Team Milestones

| Milestone         | Status  | Evidence                              |
|-------------------|---------|---------------------------------------|
| first team signal | ...     | ...                                   |
| shared coverage   | ...     | ...                                   |
| debate starter    | ...     | ...                                   |
```

### 1.3 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical. If all `unknown`,
write one row: `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 1.4 — Team Insight

**Skeptic gate**: A reader who has just seen the registry (1.1), milestone table (1.2), and
leaderboard (1.3) already knows which milestones are earned, which contributors lead, and the
total signal count per topic. The Team Insight must contain something that reader would not
already know from sections 1.1–1.3 alone.

Write one sentence that: (1) states a cross-topic conclusion, (2) includes a concrete number,
(3) names a specific contributor or topic.

**Surveyor Handoff** — The following artifacts transfer from the Surveyor to the Strategist:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Team milestone table (3 rows: milestone, status, evidence)
3. Contributor leaderboard table (columns: rank, contributor, total signals, topics covered)
4. Team Insight sentence

The Strategist begins with these four artifacts. It does not re-scan the workspace and does
not re-evaluate milestones or rebuild the leaderboard.

---

## ROLE 2: STRATEGIST

**Responsibility**: Per-topic evaluation, nearest-miss analysis, and next actions only. The
Strategist works from the Surveyor's output. The Strategist does NOT re-evaluate team
milestones and does NOT re-rank contributors.

### 2.1 — Per-Topic Achievement Evaluation

For each `topic_path` in the Surveyor's registry, evaluate all five achievements. Use exact
names — do not paraphrase. For each topic include a milestone relevance note identifying
which team milestone this topic advances or currently blocks.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file |
| Signal Depth | >= 3 files |
| Full Sweep | >= 3 distinct namespaces within topic |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

Per-topic:

```
### topic: {topic_path}
Milestone relevance: {which milestone this topic advances or blocks}
Files: {N} | Namespaces: {list} | Contributors: {list}

| Achievement   | Status  | Evidence                    |
|---------------|---------|-----------------------------|
| First Signal  | ...     | ...                         |
| Signal Depth  | ...     | ...                         |
| Full Sweep    | ...     | ...                         |
| Solo Pioneer  | ...     | ...                         |
| Team Topic    | ...     | ...                         |
```

Every topic in the registry must appear. A topic block that omits any of the five achievement
rows fails.

### 2.2 — Nearest-Miss

Identify the closest topic-achievement gap:

- **Level 1**: every topic 1 unit away from earning an achievement. State: topic name +
  achievement name + exact gap.
- **Level 2**: closest topic 2 units away. Write Level 2 ONLY when no Level 1 topic exists.

### 2.3 — Next Actions

**Pre-Write Check**: Identify all zero-score conditions — topics with 0 files, empty
leaderboard, empty registry. Actions eliminating a zero-score condition carry the `prevents:`
prefix. Actions advancing toward non-baseline achievements do not.

**prevents: prefix rule** — stated here for the Pre-Write Check AND embedded in the action
template below: any action whose primary purpose is eliminating a state where the output
would score zero uses the `prevents:` prefix. Advancement actions do not.

Write at least 3 actions. Each must name: (1) a specific namespace and topic path,
(2) the exact achievement or milestone it unlocks.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}**
2. ...
3. ...
```

After writing all actions, output exactly this line (substitute N with the actual count of
actions that carried the `prevents:` prefix):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

---

## V-05 — Full Integration: 3-Role Pipeline + C-27 + C-28 + C-29 (Ceiling Breaker)

**Axis**: Full integration — role sequence (C-26) + health/inertia structural separation
(C-27) + named artifact handoffs (C-28) + per-phase checklist gates (C-29)
**Hypothesis**: Each of C-26, C-27, C-28, C-29 has been isolated in earlier rounds. R10
V-02 combines C-26 + C-28 + C-29 (fails C-27). R10 V-03 combines C-27 + C-29 (fails C-26,
C-28). R10 V-04 combines C-26 + C-28 (fails C-27, C-29). No variation yet holds all four
simultaneously. V-05 integrates them by placing C-27 inside the Analyst role: the Analyst
runs an explicit Health Phase (C-27a: current state, counts, coverage) then an explicit
Inertia Phase (C-27b: trajectory, momentum, stall flags) as two named, structurally separated
sub-phases before handoff. The role boundaries carry full artifact inventories (C-28). Each
role boundary uses a multi-item `[ ]` gate checklist (C-29). Named scope constraints on all
three roles satisfy C-26. C-24 (ACTIONS GATE count) and C-25 (Skeptic novelty gate) are
preserved in the Publisher. Expected: all 21 aspirational criteria pass.

---

You are running the **Corps Leaderboard** skill in a 3-role pipeline. Execute each role
completely before advancing to the next. No role may perform work assigned to another role.
Output each Gate checklist verbatim with all items verified before transferring artifacts.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. The Archivist scans the workspace and builds the
registry and contributor index. The Archivist does NOT evaluate achievements, does NOT assess
milestones, does NOT assess trajectory or inertia, does NOT rank contributors, and does NOT
make recommendations.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. Record four fields per file:

- `topic_path` — path segment after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop. Roles 2 and 3 do not run.

Print registry as a table: `topic_path | namespace | contributor | file`

### 1.2 — Contributor Index

Build a contributor-to-topics index. For each contributor list every `topic_path` they appear
in and their file count per topic. Print as a table.

**Archivist Gate** — Verify and output this checklist before transferring artifacts:

- [ ] Registry table printed with all four required columns
- [ ] Contributor index table printed with contributor, topic_path, and file_count columns

**Archivist Handoff** — The following artifacts transfer from the Archivist to the Analyst:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Contributor index table (columns: `contributor`, `topic_path`, `file_count`)

The Analyst begins with these two artifacts. It does not re-scan the workspace.

---

## ROLE 2: ANALYST

**Responsibility**: Evaluation only. The Analyst assesses registry data and reports current
state (Health Phase) then trajectory (Inertia Phase). These two sub-phases are structurally
separated — Health Phase content must not appear in the Inertia Phase and vice versa. The
Analyst does NOT make recommendations, does NOT produce a leaderboard, and does NOT write
actions.

### 2.1 — Health Phase

The Health Phase reports current signal state: what exists now, counts, coverage, and
achievement status per topic. This phase does NOT report trajectory, momentum, direction of
change, or stall indicators — those belong to the Inertia Phase.

For each `topic_path`, evaluate all five achievements. Use exact names.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file |
| Signal Depth | >= 3 files |
| Full Sweep | >= 3 distinct namespaces within topic |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

Per-topic format (current state only — no trajectory claims permitted):

```
### topic: {topic_path}
Health — Files: {N} | Namespaces: {list} | Contributors: {list}

| Achievement   | Status  | Evidence                    |
|---------------|---------|-----------------------------|
| First Signal  | ...     | ...                         |
| Signal Depth  | ...     | ...                         |
| Full Sweep    | ...     | ...                         |
| Solo Pioneer  | ...     | ...                         |
| Team Topic    | ...     | ...                         |
```

Also evaluate all three team milestones. Use exact names. Evidence must be non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Output as table: `milestone | status | evidence`

### 2.2 — Inertia Phase

The Inertia Phase reports trajectory and momentum: which topics are expanding, stalling, or
consolidating. This phase is structurally separate from the Health Phase — it reports
direction of change, not current static state. The Inertia Phase does NOT restate file counts
or achievement statuses already reported in the Health Phase.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | topic has exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor signal present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Print inertia table: `topic_path | flags | trajectory note`

A topic with no inertia flags gets `flags = none` with a brief note confirming healthy
momentum state.

### 2.3 — Nearest-Miss Assessment

Identify the topic-achievement pair closest to earning.

- **Level 1**: list every topic 1 unit away from earning an achievement (topic + achievement
  + exact gap).
- **Level 2**: list the closest topic 2 units away. Write Level 2 ONLY when no Level 1 topic
  exists.

Print: `topic | achievement | gap | level`

**Analyst Gate** — Verify and output this checklist before transferring artifacts:

- [ ] Every topic from the Archivist registry has a complete Health Phase achievement block with all five rows
- [ ] All three milestone names appear verbatim in the Health Phase, each with non-empty evidence
- [ ] Inertia Phase table present with every topic evaluated; no static counts restated from Health Phase
- [ ] Nearest-miss assessment complete (Level 1 listed, or Level 2 with explicit note that Level 1 was empty)

**Analyst Handoff** — The following artifacts transfer from the Analyst to the Publisher:

1. Per-topic Health Phase achievement tables (one block per `topic_path`)
2. Team milestone table (3 rows: milestone, status, evidence)
3. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`)
4. Nearest-miss assessment table (columns: `topic`, `achievement`, `gap`, `level`)

The Publisher begins with these four artifacts. It does not re-evaluate achievements or
re-assess inertia.

---

## ROLE 3: PUBLISHER

**Responsibility**: Synthesis, leaderboard, and actions only. The Publisher works from the
Analyst's output. It does NOT re-scan the workspace, does NOT re-evaluate achievements, and
does NOT re-assess inertia flags.

### 3.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical. If all contributors
are `unknown`, write one row: `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 3.2 — Team Insight (Skeptic Gate)

The Skeptic has read the Analyst's full output — every achievement table, every milestone
row, every inertia flag, and the nearest-miss assessment. The Team Insight must contain
something the Skeptic would not already know from reading the Analyst's output in full.

An insight that restates an inertia flag already visible in the Inertia Phase fails. An
insight that recounts achievement tallies from the Health Phase without adding a new
cross-topic inference also fails. A passing insight surfaces a second-order pattern — a risk,
convergence, or trajectory inference — that requires combining health and inertia data in a
way no single topic block directly reveals.

Write one sentence that: (1) states a cross-topic conclusion, (2) includes a concrete number,
(3) names a specific contributor or topic, (4) contains information the Skeptic acknowledges
as new given full knowledge of the Analyst's output.

### 3.3 — Actions

**Pre-Write Check**: Identify all zero-score conditions in the workspace — topics with 0
files, empty leaderboard, empty registry. Actions eliminating a zero-score condition carry
the `prevents:` prefix. Actions advancing toward non-baseline achievements do not.

**prevents: prefix rule** — stated here for the Pre-Write Check AND embedded inside each
relevant action row below: any action whose primary purpose is eliminating a state where the
output would score zero (topic at 0 files, empty leaderboard, empty registry) uses the
`prevents:` prefix. Advancement actions do not.

Write at least 3 actions. Each must name: (1) a specific namespace and topic path,
(2) the exact achievement or milestone it unlocks.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}**
2. ...
3. ...
```

After writing all actions, output exactly this line (substitute N with the actual count of
actions that carried the `prevents:` prefix):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Publisher Gate** — Verify and output this checklist after writing the ACTIONS GATE line:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Team Insight passes the Skeptic gate (new information not visible in Analyst output)
- [ ] At least 3 actions written with namespace + topic + exact achievement or milestone name
- [ ] ACTIONS GATE line written with actual N count substituted
