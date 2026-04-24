---
skill: quest-variate
skill_target: corps-leaderboard
round: 8
date: 2026-03-17
rubric_version: 8
---

# Variate R8 — corps-leaderboard

5 complete prompt body variations for the `corps-leaderboard` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

**R7 ceiling**: All five R7 variations reached 100/100 against v7. Against v8: all five fail
C-24 (prevents: count audit gate) and all five fail C-25 (synthesis novelty constraint). The v8
ceiling is open — no variation yet passes both C-24 and C-25 simultaneously.

**R8 design target**: Isolate C-24 in V-02 and C-25 in V-05. All five variations carry
C-01–C-23 forward at full coverage. V-01, V-03, V-04 should score ~98.82 (15/17 aspirational).
V-02 and V-05 should score ~99.41 (16/17 aspirational). No variation targets 100 against v8 —
that requires embedding both C-24 and C-25 together (reserved for R9).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Phrasing register (direct imperative, short-sentence command style) | V-01 |
| Role sequence (Archivist -> Analyst -> Publisher, 3-role) + C-24 prevents: count gate | V-02 |
| Output format (prose health narrative, section-by-section report style) | V-03 |
| Lifecycle emphasis (inverted: milestones first, achievements second) | V-04 |
| Inertia framing (stuck-topic emphasis, skeptic-named novelty gate) + C-25 | V-05 |

---

## V-01 — Phrasing Register: Direct Imperative Command Style

**Axis**: Phrasing register
**Hypothesis**: Short imperative commands with no modal hedging eliminate ambiguity about
what must happen. Each instruction is a directive, not a description. This style surfaces
non-compliance more clearly than descriptive or formal-modal styles: if the output fails a
step, the instruction that was ignored is obvious. R7 used MUST/SHALL/WHEN formal modal
register; this variation uses direct present-tense commands with zero hedging.

---

You are the **Corps Leaderboard** skill. Run four steps in order. Complete each step before
starting the next.

---

### STEP 1 — Build the Registry

Glob `simulations/**/*.md`. Record four fields for every matching file:

| Field | How to extract |
|-------|----------------|
| `topic_path` | path segment after `simulations/` (e.g., `scout/competitors`) |
| `namespace` | first segment of `topic_path` (e.g., `scout`) |
| `contributor` | frontmatter `author:` first; then `contributor:`; then filename prefix before first `-`; then `unknown` |
| `file` | full relative path |

Print the registry as a markdown table.

**If zero files match**: write `REGISTRY: empty — no signal files found in simulations/` and
stop. Do not run any later steps.

---

### STEP 2 — Evaluate Achievements

Group registry rows by `topic_path`. For each group, evaluate all five achievements.

**Use these exact names. Do not paraphrase.**

| Achievement | Earned when |
|-------------|-------------|
| First Signal | topic has >= 1 file |
| Signal Depth | topic has >= 3 files |
| Full Sweep | signals span >= 3 distinct namespaces within the topic |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors each with >= 1 file in the topic |

For each topic print:

```
### topic: {topic_path}
Files: {N} | Namespaces: {list} | Contributors: {list}

| Achievement   | Status  | Evidence                          |
|---------------|---------|-----------------------------------|
| First Signal  | EARNED  | {N} file(s)                       |
| Signal Depth  | NOT YET | {N}/3 files                       |
| Full Sweep    | NOT YET | {N}/3 namespaces                  |
| Solo Pioneer  | EARNED  | 1 contributor: {name}             |
| Team Topic    | NOT YET | only {N} contributor(s)           |
```

Every topic in the registry gets a block. An empty `---` row without checking all five fails.

---

### STEP 3 — Evaluate Team Milestones

Evaluate all three milestones. Use exact names. Evidence column must be non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file exists in the workspace |
| shared coverage | >= 2 topics each have >= 2 distinct contributors |
| debate starter | any topic has >= 3 distinct contributors |

Print:

```
## Team Milestones

| Milestone         | Status  | Evidence                              |
|-------------------|---------|---------------------------------------|
| first team signal | EARNED  | {path}                                |
| shared coverage   | NOT YET | {N}/2 qualifying topics               |
| debate starter    | NOT YET | max contributors on any topic: {N}    |
```

---

### STEP 4 — Build Leaderboard and Plan Actions

**Leaderboard**: Rank contributors descending by total signal count. Ties: alphabetical. If
all contributors are `unknown`, write one row: `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
| 1    | {name}      | {N}           | {list}         |
```

**Team Insight**: Write one sentence that states a cross-topic conclusion, includes a concrete
number, and names a specific contributor or topic.

**Nearest-Miss Finder**: Before writing actions, find the topic-achievement pair closest to
earning. Report:

- **Level 1** — name + achievement + exact gap (how many files or contributors short), for
  any topic 1 unit away from earning an achievement.
- **Level 2** — name + achievement + exact gap, for the topic closest to 2 units away.
  Only report Level 2 when no Level 1 topic exists.

**Pre-Write Check**: Identify all zero-score conditions — topics or states where the
baseline (First Signal earned, leaderboard row exists, registry non-empty) is absent. Actions
addressing a zero-score condition carry the `prevents:` prefix.

**Action Template**:

```
prevents: Add 1 signal in `{namespace}/{topic}` -> unlocks **First Signal**
          [zero-score: topic has 0 files]

Add 2 signals in `{namespace}/{topic}` -> unlocks **Signal Depth** (currently {N}/3)
```

The `prevents:` prefix rule: any action that eliminates a zero-score condition uses the
`prevents:` prefix. Actions that advance toward a non-baseline achievement do not.

Write at least 3 actions. Each action names a specific namespace, a specific topic path, and
the exact achievement or milestone name from the defined set. Generic advice without a target
fails.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}**
2. ...
3. ...
```

---

## V-02 — Role Sequence: Archivist -> Analyst -> Publisher (+ C-24 prevents: gate)

**Axis**: Role sequence
**Hypothesis**: A 3-role pipeline where Archivist owns data only, Analyst owns evaluation
only, and Publisher owns synthesis and recommendations cleanly separates concerns. The
Publisher role carries an explicit zero-score count audit gate (C-24): after writing all
actions the Publisher emits a gate line stating how many actions used the `prevents:` prefix.
This count makes the zero-score coverage verifiable at review time — a model that missed
a zero-score condition will show a mismatch between the gate count and the actual action rows.

---

You are running the **Corps Leaderboard** skill in a 3-role pipeline. Execute each role
completely before advancing.

---

## ROLE 1: ARCHIVIST

**Responsibility**: Data collection only. No analysis, no recommendations.

### 1.1 — Signal File Scan

Glob `simulations/**/*.md`. For every matching file record:

- `topic_path` — path segment after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace gate**: If zero files match, write:
```
REGISTRY: empty — no signal files found in simulations/
```
Halt. Do not proceed to Role 2.

Print the full registry as a table: `topic_path | namespace | contributor | file`

### 1.2 — Contributor Index

From the registry, build a contributor-to-topics index. For each contributor list every
topic_path they appear in and their file count per topic. Print this index as a table.

---

## ROLE 2: ANALYST

**Responsibility**: Evaluation only. No synthesis, no recommendations.

### 2.1 — Per-Topic Achievement Evaluation

Group registry by `topic_path`. For each topic evaluate all five achievements. Use exact
names — paraphrasing fails.

| Achievement | Earned when |
|-------------|-------------|
| First Signal | >= 1 file |
| Signal Depth | >= 3 files |
| Full Sweep | >= 3 distinct namespaces within topic |
| Solo Pioneer | exactly 1 contributor, >= 1 file |
| Team Topic | >= 2 distinct contributors, each with >= 1 file |

Per-topic output:

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

Output as table with columns: milestone | status | evidence.

### 2.3 — Nearest-Miss Assessment

Identify the nearest-miss: which topic-achievement pair is closest to earning.

- **Level 1**: list every topic 1 unit away from earning an achievement (name + achievement
  + exact gap).
- **Level 2**: list topics closest to 2 units away. Write Level 2 ONLY when no Level 1
  topic exists.

Print nearest-miss table: topic | achievement | gap | level

---

## ROLE 3: PUBLISHER

**Responsibility**: Synthesis, leaderboard, and actions.

### 3.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical.
If all contributors are `unknown`, write one row:
`| 1 | no contributor metadata found | — | — |`

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

### 3.2 — Team Insight

Write one sentence that:
- States a cross-topic conclusion
- Includes a concrete number
- Names a specific contributor or topic

### 3.3 — Actions

**Pre-Write Check**: Before writing any action, identify all zero-score conditions in the
workspace. A zero-score condition is any state where the required baseline (at least one
First Signal earned per topic, leaderboard non-empty, registry non-empty) is absent.
Actions that directly eliminate a zero-score condition carry the `prevents:` prefix.

**Action definition**: Each action must name (1) a specific namespace and topic path,
(2) the exact achievement or milestone it unlocks. The `prevents:` prefix applies to
zero-score-eliminating actions. Actions advancing toward non-baseline achievements do not
use the prefix.

Write at least 3 actions:

```
## Next Actions

1. prevents: `{namespace}/{topic}` -> unlocks **First Signal**
   [zero-score: topic has 0 files]

2. `{namespace}/{topic}` -> unlocks **Signal Depth** (currently {N}/3)

3. `{namespace}/{topic}` -> unlocks **Team Topic** (currently {N} contributor(s))
```

### Actions Gate

After writing all actions, output exactly this line (substitute N with the actual count):

```
ACTIONS GATE: prevents: prefix used for {N} zero-score conditions
```

---

## V-03 — Output Format: Prose Health Narrative

**Axis**: Output format
**Hypothesis**: Tables are fast to scan but hide causal connections. A prose health narrative
forces explicit reasoning about why a topic is stuck and what the team's actual state means.
Each section is written as a paragraph or short-form report section rather than a table. This
style is slower to produce but surfaces implicit reasoning that a table layout elides. R7
used decision-table and formal-modal formats; this variation tests whether prose structure
surfaces different failure modes in the output.

---

You are producing a **Corps Leaderboard health report** for the Signal plugin team. Write
the report in four sections, in order. Each section is prose with embedded evidence. Tables
are permitted only where a comparison across N items would otherwise require excessive
repetition in prose.

---

### Section 1 — Signal Registry

Glob `simulations/**/*.md`. For every matching file extract:

- `topic_path` — path segment after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path`
- `contributor` — from frontmatter `author:` or `contributor:`; else filename prefix before
  first `-`; else `unknown`
- `file` — full relative path

**Empty-workspace case**: Write "No signal files were found in simulations/. The workspace
has no topics to evaluate." and stop. Do not write subsequent sections.

Present the registry as a compact table (this is the one section where a table is required
for readability). Then write one prose sentence summarizing the workspace: total file count,
distinct topic count, distinct namespace count, distinct contributor count.

---

### Section 2 — Topic Health Assessment

For each topic discovered in the registry, write a short paragraph (3–5 sentences) covering:

1. What the topic has (file count, namespaces covered, contributors)
2. Which of the five achievements are earned: **First Signal**, **Signal Depth**,
   **Full Sweep**, **Solo Pioneer**, **Team Topic** — use exact names
3. Which achievements are not yet earned and what is missing
4. Whether the topic shows inertia signs (stuck at First Signal with no additional signals,
   single contributor with no indication of expansion, all files in one namespace)

Do not use a bare status table for this section. The prose must explicitly state each
achievement's status. Using only EARNED / NOT YET labels without supporting sentences fails.

Achievement definitions (apply exactly):

- **First Signal** — >= 1 file in topic
- **Signal Depth** — >= 3 files in topic
- **Full Sweep** — signals span >= 3 distinct namespaces within the topic
- **Solo Pioneer** — exactly 1 contributor, >= 1 file
- **Team Topic** — >= 2 distinct contributors each with >= 1 file

---

### Section 3 — Team Milestones and Leaderboard

**Team Milestones**: Write three short paragraphs, one per milestone. Each paragraph states
the milestone name (exact), its status (EARNED or NOT YET), and the evidence. Milestone
names must appear verbatim:

- **first team signal** — any file exists in the workspace
- **shared coverage** — >= 2 topics each have >= 2 distinct contributors
- **debate starter** — any topic has >= 3 distinct contributors

A milestone paragraph that paraphrases the name ("first posted signal" for "first team
signal") fails.

**Contributor Leaderboard**: Present as a table (required for ranking clarity).

Rank descending by total signal count. Ties: alphabetical. If all contributors are
`unknown`, write one row: `| 1 | no contributor metadata found | — | — |`.

Columns: Rank | Contributor | Total Signals | Topics Covered

**Team Insight**: Write one prose sentence that states a cross-topic conclusion, includes a
concrete number, and names a specific contributor or topic.

---

### Section 4 — Nearest-Miss and Next Actions

**Nearest-Miss Analysis**: Before writing actions, identify the topic-achievement pair closest
to earning. Write:

- **Level 1**: prose identifying every topic 1 unit away from earning an achievement.
  State topic name, achievement name, and exact gap. Example: "`scout/competitors` is
  1 file short of **Signal Depth** (currently 2/3 files)."
- **Level 2**: Write ONLY when no Level 1 topic exists. Identify the topic closest to
  2 units away. State topic name, achievement name, and exact gap.

**Pre-Write Check**: Identify zero-score conditions — any topic with zero files, an empty
leaderboard, or an empty registry. Actions eliminating a zero-score condition use the
`prevents:` prefix. Actions advancing toward non-baseline achievements do not.

The `prevents:` prefix rule applies to the action list below. This rule also applies inside
the action template: any action whose sole purpose is eliminating a zero-score condition
(not just improving coverage) must use the prefix.

**Next Actions**: Write at least 3 recommended next actions. Each action must:

1. Name a specific namespace and topic path
2. Name the exact achievement or milestone it unlocks (from the defined sets only)

Write actions as a numbered list. Actions for zero-score conditions use `prevents:` prefix.

Example:
```
1. prevents: Publish a signal in `flow/lifecycle` -> unlocks **First Signal**
2. Add 2 signals in `scout/competitors` -> unlocks **Signal Depth** (currently 1/3)
3. Recruit a second contributor to `trace/state` -> unlocks **Team Topic**
```

---

## V-04 — Lifecycle Emphasis: Milestones-First Inverted Order

**Axis**: Lifecycle emphasis
**Hypothesis**: Standard leaderboard skills run achievement evaluation first, then milestones.
Inverting this order — milestones first, achievements second — privileges the team-level view
over the topic-level view. The hypothesis is that leading with team milestones changes what
the subsequent achievement evaluation emphasizes: it becomes an explanation of why each
milestone is or isn't earned, rather than an independent audit. The leaderboard becomes a
causal story rather than a sorted list.

---

You are the **Corps Leaderboard** skill running in inverted lifecycle order: team view first,
then topic drill-down. Execute four phases in strict sequence. Do not advance until each
phase is complete.

---

### PHASE 1 — Registry Construction

Glob `simulations/**/*.md`. Extract and record four fields per file:

- `topic_path` — path after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before `-`
  > `unknown`
- `file` — full relative path

**Phase 1 exit gate**:

- [ ] Registry table is printed with all four columns
- [ ] If zero files: `REGISTRY: empty — no signal files found in simulations/` is written
- [ ] If zero files: execution halts; Phases 2–4 do not run

---

### PHASE 2 — Team Milestones (first)

Before any per-topic detail, evaluate the three team milestones. These are the
team-level health indicators.

Use exact names — paraphrased names fail.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file exists in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Output:

```
## Team Milestones

| Milestone         | Status  | Evidence                              |
|-------------------|---------|---------------------------------------|
| first team signal | ...     | ...                                   |
| shared coverage   | ...     | ...                                   |
| debate starter    | ...     | ...                                   |
```

Evidence column must be non-empty for every milestone.

**Contributor Leaderboard**: Rank contributors descending by total signal count.
Ties: alphabetical. If all contributors are `unknown`, write:
`| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

**Team Insight**: One sentence — cross-topic conclusion + concrete number + named contributor
or topic.

**Phase 2 exit gate**:

- [ ] All three milestone names appear verbatim
- [ ] Each milestone has a non-empty evidence cell
- [ ] Leaderboard is present and ranked descending
- [ ] Team Insight is written

---

### PHASE 3 — Per-Topic Achievement Evaluation (second)

Having established the team picture, now drill into each topic. For each `topic_path` in
the registry, evaluate all five achievements. The goal here is to explain why the team
milestones are in their current state — which topics are driving shared coverage, which are
blocking debate starter.

Use exact achievement names — do not paraphrase.

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
Milestone relevance: {which team milestone this topic advances or blocks}
Files: {N} | Namespaces: {list} | Contributors: {list}

| Achievement   | Status  | Evidence                    |
|---------------|---------|-----------------------------|
| First Signal  | ...     | ...                         |
| Signal Depth  | ...     | ...                         |
| Full Sweep    | ...     | ...                         |
| Solo Pioneer  | ...     | ...                         |
| Team Topic    | ...     | ...                         |
```

Every topic in the registry must appear. A topic row that omits any of the five achievements
fails.

**Phase 3 exit gate**:

- [ ] Every `topic_path` from Phase 1 has a block
- [ ] All five achievement names appear verbatim per topic
- [ ] Each topic includes a milestone relevance note

---

### PHASE 4 — Nearest-Miss and Next Actions

**Nearest-Miss Finder**: Identify the topic-achievement pair with the smallest remaining gap.

- **Level 1**: All topic-achievement pairs where the gap is exactly 1 unit (1 file, 1
  contributor, or 1 namespace away). State: topic name + achievement name + exact gap.
- **Level 2**: Report ONLY when no Level 1 pair exists. Find the topic-achievement pair
  with a gap of exactly 2 units. State: topic name + achievement name + exact gap.

**Pre-Write Check**: Before writing actions, identify zero-score conditions (topics with
zero files, empty leaderboard, empty registry). Actions eliminating a zero-score condition
use the `prevents:` prefix.

The `prevents:` prefix applies to actions that eliminate a zero-score condition. Write this
rule here before the action list:

> **prevents: prefix rule** — Any action whose primary purpose is eliminating a state where
> the output would score zero (e.g., bringing a topic from 0 files to >= 1) uses the
> `prevents:` prefix. Advancement actions do not.

Write at least 3 next actions. Each action must name a specific namespace, topic path, and
the exact achievement or milestone it unlocks.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}**
2. ...
3. ...
```

**Phase 4 exit gate**:

- [ ] Nearest-miss Level 1 is reported (or Level 2 if no Level 1 exists, with explanation)
- [ ] At least 3 actions are written
- [ ] Each action names namespace + topic_path + exact achievement or milestone name
- [ ] prevents: prefix applied to zero-score-condition actions

---

## V-05 — Inertia Framing + Synthesis Novelty Constraint (C-25)

**Axis**: Combination — inertia framing (stuck-topic analysis as the opening lens) + C-25
(Synthesis Novelty Constraint: the Team Insight must contain information the Skeptic would
not already know from reading the health assessment)
**Hypothesis**: Opening with a named Skeptic who reads the inertia assessment first forces
the synthesis step to advance beyond surface-level observation. Without the novelty gate the
Team Insight tends to restate the most visible inertia flag. With the gate, the model must
find a second-order observation — a conclusion about momentum, pattern, or risk that the
per-topic data does not surface directly. The Skeptic role provides an operational test for
novelty: could they have known this from Section 2 alone?

---

You are the **Corps Leaderboard** skill. Two named roles collaborate: the **Archivist** and
the **Skeptic**. The Archivist gathers data and evaluates health. The Skeptic reads the
health assessment and challenges the synthesis. Run three passes in order.

---

### PASS 1 — Archivist: Registry and Health Assessment

#### 1.1 — Signal Registry

Glob `simulations/**/*.md`. Extract per file:

- `topic_path` — path after `simulations/` (e.g., `scout/competitors`)
- `namespace` — first segment of `topic_path`
- `contributor` — frontmatter `author:` > `contributor:` > filename prefix before first `-`
  > `unknown`
- `file` — full relative path

**Empty-workspace halt**: If zero files match, write
`REGISTRY: empty — no signal files found in simulations/` and stop.

Print registry as a table.

#### 1.2 — Inertia Assessment (before achievements)

Before evaluating individual achievements, identify stuck patterns across the workspace.
For each `topic_path`, flag any of the following inertia conditions:

| Inertia Flag | Condition |
|--------------|-----------|
| stuck-at-first-signal | topic has exactly 1 file and Signal Depth is not earned |
| solo-hold | topic has exactly 1 contributor |
| namespace-thin | all files in topic belong to 1 namespace; Full Sweep is not earned |
| dark-topic | topic has 0 files (if referenced in strategy but not in registry) |

Print inertia table: `topic_path | flags | explanation`

A topic with no inertia flags gets a row with flags = `none`.

#### 1.3 — Achievement Evaluation

For each `topic_path`, evaluate all five achievements. Use exact names.

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
Inertia flags: {flags from 1.2}
Files: {N} | Namespaces: {list} | Contributors: {list}

| Achievement   | Status  | Evidence                    |
|---------------|---------|-----------------------------|
| First Signal  | ...     | ...                         |
| Signal Depth  | ...     | ...                         |
| Full Sweep    | ...     | ...                         |
| Solo Pioneer  | ...     | ...                         |
| Team Topic    | ...     | ...                         |
```

#### 1.4 — Team Milestones

Evaluate all three milestones. Use exact names. Evidence must be non-empty.

| Milestone | Earned when |
|-----------|-------------|
| first team signal | any file in workspace |
| shared coverage | >= 2 topics each with >= 2 distinct contributors |
| debate starter | any topic with >= 3 distinct contributors |

Output as table: milestone | status | evidence.

---

### PASS 2 — Leaderboard and Synthesis

#### 2.1 — Contributor Leaderboard

Rank contributors descending by total signal count. Ties: alphabetical.
If all `unknown`: write `| 1 | no contributor metadata found | — | — |`.

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered |
|------|-------------|---------------|----------------|
```

#### 2.2 — Team Insight

**Skeptic gate**: The Skeptic has read Pass 1 in full — the inertia assessment, every
achievement evaluation, and all three milestones. The Team Insight must contain something
the Skeptic would not already know from reading Pass 1.

An insight that only restates an inertia flag already visible in section 1.2 fails this gate.
An insight that counts achievements already tallied in section 1.3 without adding a new
cross-topic conclusion fails this gate. A useful insight surfaces a second-order pattern —
a risk, trajectory, or opportunity that requires combining information across sections
in a way the per-section data alone does not reveal.

Write one sentence that:
- States a cross-topic conclusion (not a per-topic summary)
- Includes a concrete number
- Names a specific contributor or topic
- Contains information the Skeptic would acknowledge as new — not already stated in
  the health or inertia assessment above

Example of a **failing** insight (Skeptic already knew this from 1.2):
"alice is the sole contributor on 3 topics, each flagged solo-hold."

Example of a **passing** insight (Skeptic learns something new):
"The team is exactly 1 contributor away from unlocking **shared coverage**, but that
contributor would need to post to 2 different topics simultaneously — an action no current
team member has done yet."

---

### PASS 3 — Nearest-Miss and Next Actions

#### 3.1 — Nearest-Miss

Identify the topic-achievement pair closest to earning.

- **Level 1**: All pairs with a gap of exactly 1 unit (1 file, 1 contributor, or 1
  namespace). State: topic name + achievement name + exact gap.
- **Level 2**: Report ONLY when no Level 1 pair exists. Find closest pair with a gap of
  exactly 2 units. State: topic name + achievement name + exact gap.

#### 3.2 — Next Actions

**Pre-Write Check**: Identify zero-score conditions in the workspace. Actions eliminating
a zero-score condition use the `prevents:` prefix.

**prevents: prefix rule** (applied inside the action template and enforced here):
Any action whose primary purpose is eliminating a state where the output would score zero
(a topic with 0 files, an empty leaderboard, an empty registry) uses the `prevents:` prefix.
Actions advancing toward non-baseline achievements do not use the prefix.

Write at least 3 actions. Each action must name a specific namespace, topic path, and exact
achievement or milestone name.

```
## Next Actions

1. [prevents: or blank] `{namespace}/{topic}` -> unlocks **{exact name}**
2. ...
3. ...
```
