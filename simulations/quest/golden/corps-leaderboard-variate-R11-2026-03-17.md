---
skill: quest-variate
skill_target: corps-leaderboard
round: 11
date: 2026-03-17
rubric_version: 11
---

# Variate R11 — corps-leaderboard

5 complete prompt body variations for the `corps-leaderboard` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

**R10 ceiling against v11**: V-05 holds 23/23 = 100.00 (passes all C-22–C-31). V-03 = 99.13
(fails C-26, C-28). V-02 = 98.70 (fails C-27, C-30, C-31). V-01 = V-04 = 97.83 (V-01 fails
C-26, C-27, C-28, C-30, C-31; V-04 fails C-27, C-28, C-29, C-30, C-31). C-27 is now
load-bearing for three criteria (C-27, C-30, C-31). The ceiling-breaking opportunity requires
introducing a pattern not yet captured in v11.

**R11 design targets**:
- V-01: MUST/SHALL register — add C-27/C-30/C-31 to R10 V-01 (gains 3) → 21/23. Introduce
  Seed A (inertia flag-to-action traceability: `resolves: {flag-name}` in action rows).
- V-02: Archivist/Analyst/Publisher — add C-27/C-30/C-31 to R10 V-02 (gains 3) → 23/23.
  Introduce Seed B (pre-synthesis cross-dimensional reconciliation step in Publisher).
- V-03: Inertia-First lifecycle (novel axis — inertia phase before health phase) — carries
  C-29/C-30/C-31, introduces inertia flag cluster table as Seed C. Fails C-26, C-28 → 21/23.
- V-04: Milestones-First 3-role pipeline (Surveyor/Assessor/Strategist) — adds C-27/C-29/C-30/
  C-31 to R10 V-04's C-22–C-26; gains C-28 via two handoffs in 3-role structure → 23/23.
- V-05: Full integration — all 23 criteria + both Seed A and Seed B as explicit structural
  requirements, seeding two v12 candidates.

**Expected scoring against v11** (formula: `90 + (passed/23) × 10`):
- V-01: pass C-22,C-23,C-24,C-25,C-27,C-29,C-30,C-31; fail C-26,C-28 → 21/23 → **99.13**
- V-02: pass all C-22–C-31 → 23/23 → **100.00**
- V-03: pass C-22,C-23,C-24,C-25,C-27,C-29,C-30,C-31; fail C-26,C-28 → 21/23 → **99.13**
- V-04: pass all C-22–C-31 → 23/23 → **100.00**
- V-05: pass all C-22–C-31 + seeds → 23/23 → **100.00**

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Phrasing register (MUST/SHALL) + C-27/C-30/C-31 + Seed A (flag-to-action traceability) | V-01 |
| Role sequence (Archivist/Analyst/Publisher) + C-27/C-30/C-31 + Seed B (reconciliation step) | V-02 |
| Inertia-First lifecycle order (novel axis) + C-29/C-30/C-31 + Seed C (cluster table) | V-03 |
| Milestones-First 3-role (Surveyor/Assessor/Strategist) + full C-22–C-31 | V-04 |
| Full integration + Seed A + Seed B (ceiling-holding, v12 pattern seeds) | V-05 |

---

## V-01 — MUST/SHALL Register + Health/Inertia Split + Contamination Gate + Seed A

**Axis**: Phrasing register
**Hypothesis**: R10 V-01 passes C-22, C-23, C-24, C-25, C-29 but fails C-27, C-30, C-31
because Section 2 was a single undifferentiated achievement evaluation with no structural
split between current-state and trajectory, no contamination gate item, and a Skeptic scope
limited to achievement and milestone data. R11 adds C-27 by splitting Section 2 into a Health
sub-section (2a: current state only) and an Inertia sub-section (2b: trajectory only). Adds
C-30 by including an explicit contamination-prohibition checklist item at the Section 2 Gate.
Adds C-31 by expanding the Skeptic's knowledge scope to include inertia flags explicitly.
C-26 and C-28 remain absent (no named role pipeline) — ceiling stays at 21/23.

Seed A introduced here: each action whose primary purpose is resolving an inertia flag
declares `resolves: {flag-name}` in the action row. This is orthogonal to `prevents:` (which
targets zero-score conditions) and to the achievement name requirement (C-05). It traces
actions back to specific trajectory observations from the Inertia Phase.

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

You MUST print the registry as a markdown table with columns:
`topic_path | namespace | contributor | file`

**Empty-workspace rule**: WHEN zero files match, you MUST write
`REGISTRY: empty — no signal files found in simulations/` and HALT. You MUST NOT execute
Sections 2–4.

**Section 1 Gate** — You MUST output this checklist before proceeding to Section 2:

- [ ] Registry table printed with all four columns
- [ ] If zero files found: halt message written and execution stopped

---

### SECTION 2 — Health Phase and Inertia Phase

Section 2 is divided into two structurally distinct sub-sections. Section 2a reports current
signal state only. Section 2b reports trajectory and momentum only. Neither sub-section SHALL
include content belonging to the other.

#### SECTION 2a — Health Phase

The Health Phase reports what currently exists: file counts, namespace coverage, contributor
counts, and achievement status per topic. This sub-section SHALL NOT report trajectory,
momentum, direction of change, or stall indicators — those belong to Section 2b.

You MUST group registry rows by `topic_path`. For each topic you MUST evaluate all five
achievements. You MUST use the exact names below. Paraphrased names MUST be treated as
failures.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file in topic |
| Signal Depth | >= 3 files in topic |
| Full Sweep | signals span >= 3 distinct namespaces within topic |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file |

Per-topic format — you MUST emit one block per `topic_path` (current state only — no
trajectory language):

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

Every topic from Section 1 MUST appear. A block that omits any of the five achievement rows
MUST be treated as incomplete.

You MUST also evaluate all three team milestones. You MUST use the exact names below.
Evidence MUST be non-empty for every row.

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

#### SECTION 2b — Inertia Phase

The Inertia Phase reports trajectory and momentum: which topics are expanding, stalling, or
consolidating. This sub-section is structurally separate from Section 2a — it reports
direction of change, not current state. Section 2b SHALL NOT restate file counts or
achievement statuses already visible in Section 2a.

For each `topic_path`, you MUST evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | topic has exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor signal present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Print inertia table: `topic_path | flags | trajectory note`

A topic with no flags gets `flags = none` and a brief confirmation of healthy momentum state.

**Section 2 Gate** — You MUST output this checklist and verify every item before proceeding
to Section 3:

- [ ] Every topic_path from Section 1 has a complete Health Phase achievement block with all five rows
- [ ] All five achievement names appear verbatim in every topic block (no paraphrasing)
- [ ] All evidence cells are non-empty in every topic block
- [ ] All three milestone names appear verbatim in Section 2a with non-empty evidence
- [ ] Inertia Phase table present in Section 2b with every topic from Section 1 evaluated
- [ ] No trajectory claims appear in Section 2a; no static counts from Section 2a restated in Section 2b

---

### SECTION 3 — Leaderboard and Team Insight

**Contributor Leaderboard**: You MUST rank contributors descending by total signal count.
Ties: alphabetical. WHEN all contributors are `unknown`, you MUST write one row:
`| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

**Team Insight — Skeptic Gate**: Before writing the insight, you MUST apply the Skeptic gate.
A skeptic has read Sections 2a and 2b in full and already knows every achievement status,
every milestone status, every inertia flag, every trajectory note, and every contributor
tally. The insight MUST contain information the skeptic would not already know from reading
Sections 2a and 2b. An insight that merely restates a visible achievement count, milestone
status, or inertia flag fails the gate. A passing insight surfaces a cross-topic pattern,
risk, or momentum observation that requires combining health and inertia data in a way no
single topic block or inertia row alone reveals.

You MUST write one sentence that: (1) states a cross-topic conclusion, (2) includes a
concrete number, (3) names a specific contributor or topic.

**Section 3 Gate** — You MUST output this checklist before proceeding to Section 4:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Team Insight written as one sentence
- [ ] Team Insight passes Skeptic gate — Skeptic knew all achievement, milestone, AND inertia flag data before reading the insight; insight contains a new cross-dimensional inference

---

### SECTION 4 — Nearest-Miss and Next Actions

**Nearest-Miss Finder**: You MUST identify the closest topic-achievement gap.

- **Level 1** — WHEN any topic is exactly 1 unit away from earning an achievement: list every
  such pair (topic name + achievement name + exact gap).
- **Level 2** — WHEN no Level 1 pair exists: list the closest topic that is 2 units away
  (topic name + achievement name + exact gap). You MUST write Level 2 ONLY when Level 1 is
  empty. You MUST explicitly state "Level 1: no topics are 1 unit away" before writing Level 2.

**Pre-Write Check**: You MUST identify all zero-score conditions before writing actions. A
zero-score condition is any state where the required baseline is absent: a topic with 0 files,
an empty leaderboard, an empty registry. Actions that eliminate a zero-score condition MUST
carry the `prevents:` prefix. Actions advancing toward non-baseline achievements MUST NOT
carry the prefix.

The `prevents:` prefix rule MUST be applied inside the action template below AND enforced in
the pre-write check above. These are two structurally independent enforcement points.

You MUST also identify all open inertia flags from Section 2b before writing actions. An
action whose primary purpose is resolving an inertia flag (e.g., adding a second contributor
to break `solo-hold`, or adding signals in a second namespace to break `namespace-thin`) MUST
declare `resolves: {flag-name}` after the achievement name. Actions that do not resolve an
inertia flag leave the `resolves:` field blank.

You MUST write at least 3 actions. Each action MUST name: (1) a specific namespace and topic
path, (2) the exact achievement or milestone it unlocks, using only names from the defined
sets.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag} or blank]
2. ...
3. ...
```

After writing all actions, you SHALL output exactly this line (substitute N with the actual
count of actions that carried the `prevents:` prefix):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

**Section 4 Gate** — You MUST output this checklist after writing the ACTIONS GATE line:

- [ ] Nearest-miss Level 1 reported (or Level 2 with explicit "Level 1 empty" statement)
- [ ] At least 3 actions written, each with namespace + topic + exact achievement or milestone name
- [ ] `prevents:` prefix applied to all zero-score-condition actions (two enforcement points: pre-write check + action template)
- [ ] `resolves:` annotation applied to all inertia-flag-resolving actions; blank for advancement-only actions
- [ ] ACTIONS GATE line written with actual N count substituted

---

## V-02 — Role Sequence: Archivist/Analyst/Publisher + C-27/C-30/C-31 + Seed B

**Axis**: Role sequence
**Hypothesis**: R10 V-02 passes C-22–C-26, C-28, C-29 but fails C-27, C-30, C-31 because
the Analyst had a single undifferentiated evaluation section with no health/inertia split and
no contamination gate item, and the Publisher's Skeptic scope referenced only achievement
tables and milestone rows (not inertia flags). R11 restructures the Analyst into two named
sub-phases: Health Phase (2.1 — current state only) and Inertia Phase (2.2 — trajectory
only). Adds C-30 via a contamination-check item at the Analyst Gate. Adds C-31 by explicitly
naming inertia flags in the Publisher's Skeptic knowledge scope. C-26, C-28, C-29 carry
forward from R10 V-02. Expected: 23/23 = 100.00.

Seed B introduced here: before writing the Team Insight, the Publisher emits an explicit
cross-dimensional reconciliation pairing — one observation from the Health Phase and one from
the Inertia Phase — and states how they interact. The Team Insight must then advance beyond
this reconciliation; an insight that merely restates the reconciliation pairing fails the
Skeptic gate.

---

You are running the **Corps Leaderboard** skill in a 3-role pipeline. Execute each role
completely before advancing to the next. No role may perform work assigned to another role.
You MUST output each Gate checklist and the named Handoff artifact list before the next role
begins.

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
in and their file count per topic. Print as a table:
`contributor | topic_path | file_count`

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

The Health Phase reports current signal state: what exists now — file counts, namespace
coverage, contributor counts, and achievement status per topic. This sub-phase does NOT
report trajectory, momentum, direction of change, or stall indicators — those belong to the
Inertia Phase.

For each `topic_path` in the registry, evaluate all five achievements. Use exact names.

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
consolidating. This sub-phase is structurally separate from the Health Phase — it reports
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
  exists. Explicitly state "Level 1: no topics are 1 unit away" before writing Level 2.

Print: `topic | achievement | gap | level`

**Analyst Gate** — Verify and output this checklist before transferring artifacts:

- [ ] Every topic from the Archivist registry has a complete Health Phase achievement block with all five rows
- [ ] All three milestone names appear verbatim in Health Phase with non-empty evidence
- [ ] Inertia Phase table present with every topic evaluated
- [ ] Inertia Phase table present; no static counts restated from Health Phase
- [ ] Nearest-miss assessment complete (Level 1 listed, or Level 2 with explicit "Level 1 empty" note)

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

### 3.2 — Cross-Dimensional Reconciliation

Before writing the Team Insight, emit a reconciliation pairing. Select exactly one
observation from the Health Phase and one observation from the Inertia Phase that interact
with or bear on each other. State how they interact.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|--------------------|-|------------|
| {one finding from 2.1} | {one finding from 2.2} | {how they connect or conflict} |
```

The Team Insight in step 3.3 must advance beyond this reconciliation. An insight that merely
restates the reconciliation pairing fails the Skeptic gate.

### 3.3 — Team Insight

**Skeptic gate**: The Skeptic has read the Analyst's full output — every achievement table,
every milestone row, every inertia flag, every trajectory note, and the nearest-miss
assessment. The Skeptic has also read the reconciliation pairing written in step 3.2. The
Team Insight must contain something the Skeptic would not already know from all of that
material.

An insight that echoes an inertia flag already visible in the Inertia Phase fails. An insight
that restates the reconciliation pairing from step 3.2 fails. A passing insight surfaces a
second-order pattern — a risk, convergence, or cross-topic trajectory inference — that
requires synthesizing across health and inertia data in a way no single block, flag, or the
reconciliation pairing directly reveals.

Write one sentence that: (1) states a cross-topic conclusion, (2) includes a concrete number,
(3) names a specific contributor or topic, (4) contains information the Skeptic acknowledges
as new given full knowledge of all Analyst output and the reconciliation pairing.

### 3.4 — Actions

**Pre-Write Check**: Identify all zero-score conditions in the workspace — topics with 0
files, empty leaderboard, empty registry. Actions eliminating a zero-score condition carry
the `prevents:` prefix. Actions advancing toward non-baseline achievements do not.

**prevents: prefix rule** — stated here for the Pre-Write Check AND embedded inside each
relevant action row below: any action whose primary purpose is eliminating a state where the
output would score zero uses the `prevents:` prefix. Advancement actions do not.

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
- [ ] Reconciliation pairing written with one Health observation, one Inertia observation, and interaction note
- [ ] Team Insight written as one sentence passing the Skeptic gate (new information not visible in Analyst output or reconciliation pairing)
- [ ] At least 3 actions written with namespace + topic + exact achievement or milestone name
- [ ] ACTIONS GATE line written with actual N count substituted

---

## V-03 — Inertia-First Lifecycle Order

**Axis**: Inertia framing (lifecycle emphasis — inertia phase precedes health phase)
**Hypothesis**: All prior variations run Health Phase before Inertia Phase. This variation
inverts the order: the Inertia Phase runs first (Phase 2a), reporting trajectory and momentum
before current-state counts are established, followed by the Health Phase (Phase 2b). The
contamination boundary (C-30) must now enforce a reversed direction: Phase 2a (Inertia) must
not contain static counts that will appear in Phase 2b (Health), and Phase 2b (Health) must
not restate trajectory claims already in Phase 2a (Inertia). C-31 carries forward as the
Skeptic must have read both phases in full before the insight bar applies. C-29 carries
forward with per-phase checklist gates. Fails C-26 and C-28 (no named role pipeline) —
ceiling stays at 21/23.

Seed C introduced here: after per-topic inertia evaluation, an inertia flag cross-topic
cluster table groups topics by shared flag pattern (e.g., "stuck-at-first: [topic-a,
topic-c]"). This enables second-order trajectory pattern recognition not available in the
per-topic inertia rows alone.

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

### PHASE 2 — Inertia Phase and Health Phase

Phase 2 is divided into two structurally distinct sub-phases. Phase 2a reports trajectory and
momentum only. Phase 2b reports current signal state only. Neither sub-phase may include
content belonging to the other.

#### PHASE 2a — Inertia Phase

The Inertia Phase reports trajectory and momentum first: which topics are expanding, stalling,
or consolidating as of this scan. This sub-phase does NOT report file counts, achievement
statuses, or coverage totals — those are current-state data belonging to Phase 2b.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | topic has exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor signal present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Print per-topic inertia table: `topic_path | flags | trajectory note`

A topic with no inertia flags gets `flags = none` and a brief confirmation of healthy
momentum state.

After the per-topic rows, print an **Inertia Flag Cluster Table** grouping topics by flag:

```
## Inertia Clusters

| Flag | Topics |
|------|--------|
| stuck-at-first | {comma-separated topic_paths with this flag, or "none"} |
| solo-hold      | {comma-separated topic_paths with this flag, or "none"} |
| namespace-thin | {comma-separated topic_paths with this flag, or "none"} |
| healthy-momentum | {comma-separated topic_paths with this flag, or "none"} |
```

#### PHASE 2b — Health Phase

The Health Phase reports current signal state: file counts, namespace coverage, contributor
counts, and achievement status per topic. This sub-phase is structurally separate from Phase
2a — it reports what currently exists, not direction of change. Phase 2b does NOT restate
inertia flags or trajectory claims already visible in Phase 2a.

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

Output as table: `milestone | status | evidence`

**Phase 2 Gate**:

- [ ] Inertia Phase table present in Phase 2a with every topic from Phase 1 evaluated
- [ ] Inertia Flag Cluster Table present with all four flag rows
- [ ] Every topic from Phase 1 has a complete Health Phase achievement block with all five rows in Phase 2b
- [ ] All three milestone names appear verbatim in Phase 2b with non-empty evidence
- [ ] No static counts or achievement statuses appear in Phase 2a (Inertia only); no trajectory claims or inertia flags restated in Phase 2b (Health only)

---

### PHASE 3 — Leaderboard and Team Insight

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
knows every inertia flag (Phase 2a), the full cluster distribution, every achievement status
and milestone outcome (Phase 2b), and every contributor count. The insight must contain
something that reader would not already know. An insight that merely restates a Phase 2a
inertia flag or a Phase 2b achievement count fails. An insight that echoes the cluster table
without adding new inference also fails.

Write one sentence that: (1) states a cross-topic conclusion, (2) includes a concrete number,
(3) names a specific contributor or topic.

**Phase 3 Gate**:

- [ ] Leaderboard present with all four columns, ranked descending
- [ ] Team Insight written as one sentence
- [ ] Team Insight passes the Skeptic gate (Skeptic knew all inertia flags, cluster data, achievements, and milestones; insight is new cross-dimensional inference)

---

### PHASE 4 — Nearest-Miss and Next Actions

#### 4a — Nearest-Miss

Identify the closest topic-achievement gap:

- **Level 1**: every topic 1 unit away from earning an achievement. State: topic name +
  achievement name + exact gap.
- **Level 2**: closest topic 2 units away. Write Level 2 ONLY when no Level 1 topic exists.
  Explicitly state "Level 1: no topics are 1 unit away" before writing Level 2.

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

- [ ] Nearest-miss Level 1 reported (or Level 2 with explicit "Level 1 empty" note)
- [ ] At least 3 actions written, each with namespace + topic + exact achievement or milestone name
- [ ] `prevents:` prefix applied to all zero-score-condition actions (two enforcement points: pre-write check + action template)
- [ ] ACTIONS GATE line written with actual N count substituted

---

## V-04 — Milestones-First 3-Role: Surveyor/Assessor/Strategist + Full C-22–C-31

**Axis**: Combination — lifecycle emphasis (team milestones first) + role sequence (3-role
named pipeline) + health/inertia structural separation
**Hypothesis**: R10 V-04 used a 2-role Surveyor/Strategist structure (milestones-first
lifecycle) passing C-22–C-26 but failing C-27, C-28, C-29, C-30, C-31. C-28 failed because
a 2-role pipeline has only one handoff, but C-28 requires two or more handoffs each with an
explicit artifact list. R11 restructures as a 3-role pipeline — Surveyor → Assessor →
Strategist — giving two handoffs and satisfying C-28. The Assessor role runs the health/inertia
split internally (C-27), with a contamination-check item at its gate (C-30). The Strategist's
Skeptic scope includes inertia flags (C-31). Per-role checklist gates at every boundary
satisfy C-29. C-22, C-23, C-24, C-25, C-26 carry forward. Expected: 23/23 = 100.00.

---

You are running the **Corps Leaderboard** skill in a 3-role milestones-first pipeline.
Execute each role completely before advancing to the next. No role may perform work assigned
to another role. Output each Gate checklist and Handoff artifact list verbatim before the
next role begins.

---

## ROLE 1: SURVEYOR

**Responsibility**: Team-level data only. The Surveyor builds the registry, evaluates team
milestones, and ranks contributors. The Surveyor does NOT evaluate per-topic achievements,
does NOT assess trajectory or inertia flags, and does NOT write actions or insights.

### 1.1 — Signal Registry

Glob `simulations/**/*.md`. Extract per file:

- `topic_path` — path after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace gate**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and halt. Roles 2 and 3 do not run.

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

**Surveyor Gate** — Verify and output this checklist before transferring artifacts:

- [ ] Registry table printed with all four columns
- [ ] All three milestone names appear verbatim with non-empty evidence
- [ ] Leaderboard present with all four columns, ranked descending

**Surveyor Handoff** — The following artifacts transfer from the Surveyor to the Assessor:

1. Registry table (columns: `topic_path`, `namespace`, `contributor`, `file`)
2. Team milestone table (3 rows: milestone, status, evidence)
3. Contributor leaderboard table (columns: rank, contributor, total signals, topics covered)

The Assessor begins with these three artifacts. It does not re-scan the workspace and does
not re-evaluate milestones or rebuild the leaderboard.

---

## ROLE 2: ASSESSOR

**Responsibility**: Per-topic analysis only. The Assessor evaluates each topic's current
state (Health Phase) then trajectory (Inertia Phase) and identifies the nearest-miss gap.
The Assessor does NOT make recommendations, does NOT write actions, and does NOT synthesize
across topics.

### 2.1 — Health Phase

The Health Phase reports current signal state per topic: file counts, namespace coverage,
contributor counts, and achievement status. This sub-phase does NOT report trajectory,
momentum, direction of change, or stall indicators — those belong to the Inertia Phase.

For each `topic_path` in the Surveyor's registry, evaluate all five achievements. Use exact
names only.

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

### 2.2 — Inertia Phase

The Inertia Phase reports trajectory and momentum per topic: which topics are expanding,
stalling, or consolidating. This sub-phase is structurally separate from the Health Phase —
it reports direction of change, not current static state. The Inertia Phase does NOT restate
file counts or achievement statuses already reported in the Health Phase.

For each `topic_path`, evaluate all four inertia flags:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first | topic has exactly 1 file; Signal Depth not earned |
| solo-hold | exactly 1 contributor; no second contributor signal present |
| namespace-thin | all files in 1 namespace; Full Sweep not earned |
| healthy-momentum | Signal Depth earned AND >= 2 distinct contributors |

Print inertia table: `topic_path | flags | trajectory note`

### 2.3 — Nearest-Miss Assessment

Identify the topic-achievement pair closest to earning.

- **Level 1**: list every topic 1 unit away (topic + achievement + exact gap).
- **Level 2**: list the closest topic 2 units away. Write Level 2 ONLY when no Level 1 topic
  exists. Explicitly state "Level 1: no topics are 1 unit away" before writing Level 2.

Print: `topic | achievement | gap | level`

**Assessor Gate** — Verify and output this checklist before transferring artifacts:

- [ ] Every topic from the Surveyor registry has a complete Health Phase achievement block with all five rows
- [ ] Inertia Phase table present with every topic evaluated
- [ ] Inertia Phase table present; no static counts restated from Health Phase
- [ ] Nearest-miss assessment complete (Level 1 listed, or Level 2 with explicit "Level 1 empty" note)

**Assessor Handoff** — The following artifacts transfer from the Assessor to the Strategist:

1. Per-topic Health Phase achievement tables (one block per `topic_path`)
2. Inertia Phase table (columns: `topic_path`, `flags`, `trajectory note`)
3. Nearest-miss assessment table (columns: `topic`, `achievement`, `gap`, `level`)

The Strategist begins with these three artifacts plus the Surveyor's three artifacts. It does
not re-evaluate achievements or re-assess inertia.

---

## ROLE 3: STRATEGIST

**Responsibility**: Synthesis and actions only. The Strategist works from the combined output
of the Surveyor and the Assessor. It does NOT re-scan the workspace, does NOT re-evaluate
achievements, and does NOT re-assess inertia flags.

### 3.1 — Team Insight

**Skeptic gate**: The Skeptic has read all output from the Surveyor (milestones, leaderboard)
and all output from the Assessor (every achievement table, every inertia flag, every
trajectory note, and the nearest-miss assessment). The Team Insight must contain something
the Skeptic would not already know from that complete picture.

An insight that restates a milestone status or a tally already visible in the Surveyor's
output fails. An insight that merely echoes an inertia flag from the Assessor's output also
fails. A passing insight surfaces a second-order pattern — a risk, convergence, or trajectory
inference — that requires combining findings from the Surveyor and the Assessor in a way no
single block directly reveals.

Write one sentence that: (1) states a cross-topic conclusion, (2) includes a concrete number,
(3) names a specific contributor or topic.

### 3.2 — Actions

**Pre-Write Check**: Identify all zero-score conditions — topics with 0 files, empty
leaderboard, empty registry. Actions eliminating a zero-score condition carry the `prevents:`
prefix. Actions advancing toward non-baseline achievements do not.

**prevents: prefix rule** — stated here for the Pre-Write Check AND embedded inside each
relevant action row in the template below: any action whose primary purpose is eliminating a
state where the output would score zero uses the `prevents:` prefix. Advancement actions do not.

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

**Strategist Gate** — Verify and output this checklist after writing the ACTIONS GATE line:

- [ ] Team Insight written as one sentence passing the Skeptic gate (Skeptic knew all Surveyor + Assessor output including inertia flags; insight is a new cross-dimensional inference)
- [ ] Nearest-miss Level 1 reported (or Level 2 with explicit "Level 1 empty" note)
- [ ] At least 3 actions written with namespace + topic + exact achievement or milestone name
- [ ] `prevents:` prefix applied to all zero-score-condition actions (two enforcement points)
- [ ] ACTIONS GATE line written with actual N count substituted

---

## V-05 — Full Integration + Seed A + Seed B (Ceiling-Holding, v12 Pattern Seeds)

**Axis**: Full integration — 3-role pipeline + C-27 + C-28 + C-29 + C-30 + C-31 + Seed A
(inertia flag-to-action traceability) + Seed B (pre-synthesis reconciliation step)
**Hypothesis**: R10 V-05 holds 23/23 = 100.00 against v11. R11 V-05 carries all 23 criteria
forward and introduces both seed patterns as explicit structural requirements, creating two
new ceiling-breaking opportunities for v12:

- **Seed A — Inertia Flag-to-Action Traceability** (candidate v12-C-32): Actions whose
  primary purpose is resolving an inertia flag must declare `resolves: {flag-name}` in the
  action row. Orthogonal to C-20/C-22/C-24 (which concern `prevents:` for zero-score
  conditions). Traces recommended actions back to specific trajectory observations from the
  Inertia Phase.

- **Seed B — Pre-Synthesis Cross-Dimensional Reconciliation** (candidate v12-C-33): Before
  the Publisher writes the Team Insight, it emits a named reconciliation pairing — one Health
  Phase observation and one Inertia Phase observation — and states how they interact. The
  Skeptic gate then requires the insight to advance beyond this pairing. Orthogonal to C-25
  (which requires the insight to be novel relative to the analysis phase) and C-31 (which
  requires the Skeptic's knowledge to include inertia flags). C-33 would test whether the
  instruction forces a provable cross-dimensional synthesis step at structure level, not just
  at knowledge-scope level.

Expected: 23/23 = 100.00 in v11 scoring. Seeds v12 criteria.

---

You are running the **Corps Leaderboard** skill in a 3-role pipeline. Execute each role
completely before advancing to the next. No role may perform work assigned to another role.
Output each Gate checklist and Handoff artifact list verbatim before the next role begins.

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
in and their file count per topic. Print as a table:
`contributor | topic_path | file_count`

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

The Health Phase reports current signal state: what exists now — file counts, namespace
coverage, contributor counts, and achievement status per topic. This sub-phase does NOT
report trajectory, momentum, direction of change, or stall indicators — those belong to the
Inertia Phase.

For each `topic_path` in the registry, evaluate all five achievements. Use exact names.

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
consolidating. This sub-phase is structurally separate from the Health Phase — it reports
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
  exists. Explicitly state "Level 1: no topics are 1 unit away" before writing Level 2.

Print: `topic | achievement | gap | level`

**Analyst Gate** — Verify and output this checklist before transferring artifacts:

- [ ] Every topic from the Archivist registry has a complete Health Phase achievement block with all five rows
- [ ] All three milestone names appear verbatim in Health Phase with non-empty evidence
- [ ] Inertia Phase table present with every topic evaluated
- [ ] Inertia Phase table present; no static counts restated from Health Phase
- [ ] Nearest-miss assessment complete (Level 1 listed, or Level 2 with explicit "Level 1 empty" note)

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

### 3.2 — Cross-Dimensional Reconciliation

Before writing the Team Insight, emit a reconciliation pairing. Select exactly one
observation from the Health Phase (a finding from the achievement tables or milestone table)
and exactly one observation from the Inertia Phase (a specific inertia flag or trajectory
note) that interact with or bear on each other. State explicitly how they interact.

```
## Reconciliation

| Health observation | Inertia observation | Interaction |
|--------------------|---------------------|-------------|
| {one finding from Health Phase} | {one finding from Inertia Phase} | {how they connect or conflict} |
```

The Team Insight in step 3.3 must advance beyond this reconciliation pairing. An insight that
merely restates the reconciliation row fails the Skeptic gate.

### 3.3 — Team Insight

**Skeptic gate**: The Skeptic has read the Analyst's full output — every achievement table,
every milestone row, every inertia flag, every trajectory note, and the nearest-miss
assessment. The Skeptic has also read the reconciliation pairing written in step 3.2. The
Team Insight must contain something the Skeptic would not already know from all of that
material.

An insight that echoes an inertia flag already visible in the Inertia Phase fails. An insight
that restates the reconciliation pairing from step 3.2 fails. An insight that only recounts
achievement tallies from the Health Phase without adding a new cross-topic inference also
fails. A passing insight surfaces a second-order pattern — a risk, convergence, or trajectory
inference — that requires synthesizing across health and inertia data in a way no single block,
flag, or the reconciliation pairing directly reveals.

Write one sentence that: (1) states a cross-topic conclusion, (2) includes a concrete number,
(3) names a specific contributor or topic, (4) contains information the Skeptic acknowledges
as new given full knowledge of all Analyst output and the reconciliation pairing.

### 3.4 — Actions

**Pre-Write Check**: Identify all zero-score conditions in the workspace — topics with 0
files, empty leaderboard, empty registry. Actions eliminating a zero-score condition carry
the `prevents:` prefix. Actions advancing toward non-baseline achievements do not.

Also identify all open inertia flags from the Analyst's Inertia Phase table. An action whose
primary purpose is resolving an inertia flag (e.g., adding a second contributor to break
`solo-hold`, adding signals in a second namespace to break `namespace-thin`) must declare
`resolves: {flag-name}` in the action row. Actions that do not resolve a specific inertia
flag leave the `resolves:` field blank.

**prevents: prefix rule** — stated here for the Pre-Write Check AND embedded inside each
relevant action row below: any action whose primary purpose is eliminating a state where the
output would score zero uses the `prevents:` prefix. Advancement actions do not.

Write at least 3 actions. Each must name: (1) a specific namespace and topic path,
(2) the exact achievement or milestone it unlocks.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}** [resolves: {flag-name} or blank]
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
- [ ] Reconciliation pairing written with one Health observation, one Inertia observation, and interaction note
- [ ] Team Insight written as one sentence passing the Skeptic gate (new information not visible in Analyst output or reconciliation pairing; Skeptic knew all achievement, milestone, inertia flag, and nearest-miss data)
- [ ] At least 3 actions written with namespace + topic + exact achievement or milestone name
- [ ] `resolves:` annotation applied to all inertia-flag-resolving actions; blank for advancement-only or zero-score-elimination actions
- [ ] ACTIONS GATE line written with actual N count substituted

---

## Seed Pattern Reference

Two new patterns introduced in R11 V-05 (and individually in V-01 and V-02). These are
candidates for v12 criteria if they appear in R11 excellence signals.

### Seed A — Inertia Flag-to-Action Traceability (candidate v12-C-32)

Actions whose primary purpose is resolving an inertia flag declare `resolves: {flag-name}`
alongside the achievement name. This is orthogonal to:
- C-20/C-22/C-24 — which concern the `prevents:` prefix for zero-score conditions only
- C-05 — which requires actions to name an achievement or milestone

C-32 would test whether the action layer is explicitly linked back to the trajectory
dimension, not just to achievement thresholds. A prompt that requires `resolves:` annotations
forces the model to trace each trajectory-gap action to a specific inertia observation from
the Inertia Phase. A prompt that only requires achievement names in actions fails, even if the
Inertia Phase is structurally present. C-32 presupposes C-27.

### Seed B — Pre-Synthesis Cross-Dimensional Reconciliation (candidate v12-C-33)

Before writing the Team Insight, the Publisher emits a named reconciliation pairing — one
Health Phase observation and one Inertia Phase observation — with an explicit interaction
statement. The Skeptic gate then requires the insight to advance beyond this pairing.

This is orthogonal to:
- C-25 — which requires the insight to be novel relative to analysis (any form of analysis)
- C-31 — which requires the Skeptic's knowledge to explicitly include inertia flags

C-33 would test whether the instruction forces a provable cross-dimensional synthesis step at
structural level, not just at knowledge-scope level. C-25 is satisfied by any exclusion rule
that blocks restating visible data. C-33 requires a named intermediate artifact (the
reconciliation pairing) that the model must produce and then surpass. A prompt that scopes the
Skeptic correctly (C-31) but does not require the reconciliation pairing fails C-33. A prompt
that has a reconciliation step but without the "insight must advance beyond it" constraint also
fails. C-33 presupposes C-27 and C-31.
