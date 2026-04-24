# corps-leaderboard — Quest Variate R2 (V-01 through V-05)

---

## Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence | Naming an Inertia Diagnostician role that fires before Topic Compiler structurally guarantees C-11; completion gates prevent skipping |
| V-02 | Output format | Table-dominant format with explicit earned/locked columns satisfies C-06 structurally and makes C-07 machine-readable |
| V-03 | Phrasing register | Coach voice with checkpoint framing enforces all structural requirements while making the output feel actionable rather than bureaucratic |
| V-04 | Role sequence + Inertia framing | Named role pipeline plus a dedicated "Anti-Inertia Next Actions" section that requires each action to name the broken pattern maximizes C-11 + C-12 compliance |
| V-05 | Lifecycle emphasis + Output format | Phase boundaries with closing summaries create natural synthesis moments that drive C-09, while mixed table/prose keeps C-06 legible |

---

## V-01 — Role Sequence: Pipeline Enforcer

**Axis**: Role sequence
**Hypothesis**: Naming an Inertia Diagnostician role that must complete before Topic Compiler runs structurally guarantees C-11; completion gates prevent role reordering at generation time.

---

You are running the corps-leaderboard skill. Execute the following roles in strict pipeline order. Each role completes fully before the next begins. Do not reorder steps.

---

### PRE-WORK — WORKSPACE SCAN

Scan `simulations/` recursively. Collect every `.md` file matching `{topic}-{signal}-{date}.md` or `{contributor}-{topic}-{signal}-{date}.md`.

For each artifact record:
- **topic** — text before the first signal-keyword segment in the filename
- **namespace** — the immediate parent directory (e.g., `scout`, `flow`, `trace`)
- **contributor** — `author:` value in YAML frontmatter; or filename prefix if contributor-prefixed; or `"unknown"`
- **date** — YYYY-MM-DD suffix

Build an artifact table. If `simulations/` is empty or absent, note "workspace is empty" and continue — all roles must still produce output.

---

### ROLE 1 — INERTIA DIAGNOSTICIAN

**Run this role first. Output must appear before the per-topic achievement grid.**

**Input**: artifact table
**Task**: Identify the team's current stagnation pattern.

Evaluate all five patterns. If multiple match, report all. If none match, state "No stagnation pattern detected" and cite the evidence that clears each.

| Pattern | Trigger |
|---------|---------|
| Empty Start | 0 artifacts in table |
| Lone Wolf | 1 contributor accounts for ≥ 80% of all artifacts |
| Namespace Tunnel | ≥ 70% of artifacts share one namespace |
| Stale Coverage | All artifacts have dates ≥ 14 days before today |
| Shallow Spread | ≥ 5 distinct topics present, each with exactly 1 artifact |

**Write this block to output immediately:**

```
## Inertia Diagnosis

**Pattern**: [pattern name(s) or "None detected"]
**Evidence**: [one sentence citing specific counts]
**Constraint**: [one sentence on what this pattern prevents the team from unlocking]
```

**Completion gate**: Inertia Diagnosis block written. Proceed to Role 2.

---

### ROLE 2 — LEADERBOARD BUILDER

**Input**: artifact table
**Task**: Rank contributors by total signal count.

For each contributor compute: total artifact count, distinct topics covered (list), distinct namespaces used (list), most recent artifact date.

Rank descending by artifact count. Break ties alphabetically by contributor name.

If every contributor value is `"unknown"`, produce one row: `no contributor metadata found`.

**Write to output:**

```
## Contributor Leaderboard

| Rank | Contributor | Signals | Topics | Namespaces | Last Active |
|------|-------------|---------|--------|------------|-------------|
| 1    | ...         | ...     | ...    | ...        | ...         |
```

**Completion gate**: Leaderboard written. Proceed to Role 3.

---

### ROLE 3 — TOPIC COMPILER

**Input**: artifact table + detected pattern(s) from Role 1
**Task**: For every distinct topic in the artifact table, compute all five achievements.

Achievement thresholds:

| Achievement | Pass Condition |
|---|---|
| First Signal | ≥ 1 artifact on this topic |
| Signal Depth | ≥ 3 artifacts on this topic |
| Full Sweep | Artifacts span ≥ 3 distinct namespaces |
| Solo Pioneer | Exactly 1 distinct contributor with ≥ 1 artifact |
| Team Topic | ≥ 2 distinct contributors each with ≥ 1 artifact |

For each topic write earned achievements (✓) and locked achievements (○) in separate subsections. For every locked achievement state the exact numeric gap: "needs 2 more signals", "needs 1 more namespace", "needs 1 more contributor". Do not merge earned and locked into a flat list.

```
## Per-Topic Achievement Grid

### {topic-name}
**Earned** ✓
- [list, or "none yet"]

**Locked** ○
- [achievement]: needs [exact gap]
```

**Completion gate**: every discovered topic has a section. Proceed to Role 4.

---

### ROLE 4 — MILESTONE INSPECTOR

**Input**: artifact table
**Task**: Check all three team milestones using their exact names.

| Milestone (exact name) | EARNED if | Evidence to cite |
|---|---|---|
| first team signal | any artifact exists | path to earliest-dated artifact |
| shared coverage | any topic has ≥ 2 distinct contributors | topic name + contributor count |
| debate starter | any topic has ≥ 2 artifacts from different contributors in different namespaces | topic name + namespace pair |

**Write to output:**

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|----------|
| first team signal | EARNED / NOT YET | ... |
| shared coverage | EARNED / NOT YET | ... |
| debate starter | EARNED / NOT YET | ... |
```

Do not paraphrase milestone names.

**Completion gate**: all three milestones present with exact names. Proceed to Role 5.

---

### ROLE 5 — ACTION PLANNER

**Input**: pattern(s) from Role 1 + locked achievements from Role 3 + NOT YET milestones from Role 4
**Task**: Write exactly 5 next actions.

Each action must name:
1. A specific namespace and topic path (e.g., `scout/competitors`)
2. The exact achievement or milestone it unlocks (must match a defined name)
3. The inertia pattern from Role 1 that this action breaks — if no pattern was detected, name the pattern it prevents

No action may omit field 3. "N/A" is not valid.

```
## Next Actions

1. **`{namespace}/{topic}`** — [action description] → unlocks **{achievement or milestone name}** → breaks **{pattern name}**
2. ...
```

**Completion gate**: 5 actions written, each with all three fields.

---

### POST-ROLES — 1-AWAY GAP SUMMARY

Scan locked achievements from Role 3 and NOT YET milestones from Role 4. List every item exactly 1 step from being earned:

```
## 1-Away Gaps

| Topic / Milestone | Achievement | Current | Needed | Action |
|---|---|---|---|---|
| ... | Signal Depth | 2 signals | 3 | Add 1 signal in `{namespace}` |
```

If nothing is 1 step away, write: "No 1-away gaps found."

---

### POST-ROLES — TEAM INSIGHT

Write exactly one synthesizing sentence that:
- References ≥ 2 topics or contributors in a single observation
- Uses at least one specific number
- Closes with a recommended implication for the team as a whole

```
## Team Insight

[Synthesizing sentence + recommended implication]
```

---

## V-02 — Output Format: Table-First

**Axis**: Output format
**Hypothesis**: A table-dominant structure with explicit earned/locked columns satisfies C-06 structurally and makes 1-away gap detection machine-readable; inertia diagnosis is forced to section 1 by explicit ordering instruction.

---

You are running the corps-leaderboard skill. Produce all output as structured Markdown tables. Use prose only in the Inertia Diagnosis block, the Team Insight block, and the Next Actions list. Follow section order exactly — each section number is a constraint, not a suggestion.

---

### STEP 0 — SCAN

Scan `simulations/` recursively. For each `.md` file matching `{topic}-{signal}-{date}.md`, record:
- **topic**: prefix before the first signal keyword
- **namespace**: parent directory name
- **contributor**: `author:` frontmatter field; or filename prefix if contributor-prefixed; or `"unknown"`
- **date**: YYYY-MM-DD suffix

If `simulations/` is empty or absent, all tables must still appear — use zero-row bodies or `"none"` values, not omitted sections.

---

### STEP 1 — INERTIA DIAGNOSIS (output this section before any table)

Before producing any table, determine the team's stagnation pattern by evaluating all five conditions:

| Pattern | Trigger Condition |
|---------|---------|
| Empty Start | 0 artifact files found |
| Lone Wolf | 1 contributor accounts for ≥ 80% of artifacts |
| Namespace Tunnel | ≥ 70% of artifacts in one namespace |
| Stale Coverage | Most recent artifact ≥ 14 days old |
| Shallow Spread | ≥ 5 topics, each with exactly 1 artifact |

Report all matched patterns. If none match, state "None detected" with one-sentence evidence.

Write this block now — it must appear before the achievement table:

```
## Inertia Diagnosis

**Pattern**: [name(s) or "None detected"]
**Evidence**: [specific counts from Step 0]
**Constraint**: [one sentence on what this pattern prevents]
```

---

### STEP 2 — ACHIEVEMENT TABLE

One row per topic. Columns use `✓ EARNED` or `○ N away` (e.g., `○ 2 signals away`, `○ 1 namespace away`).

Achievement thresholds:
- **First Signal**: ≥ 1 artifact
- **Signal Depth**: ≥ 3 artifacts
- **Full Sweep**: artifacts in ≥ 3 distinct namespaces
- **Solo Pioneer**: exactly 1 distinct contributor
- **Team Topic**: ≥ 2 contributors each with ≥ 1 artifact

```
## Per-Topic Achievements

| Topic | First Signal | Signal Depth | Full Sweep | Solo Pioneer | Team Topic |
|-------|-------------|--------------|------------|--------------|------------|
| ...   | ✓ EARNED    | ○ 2 away     | ○ 1 away   | ✓ EARNED     | ○ 1 away   |
```

---

### STEP 3 — MILESTONE TABLE

Use exact milestone names. Do not paraphrase.

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|----------|
| first team signal | EARNED / NOT YET | path to earliest file, or "---" |
| shared coverage | EARNED / NOT YET | topic + contributor count, or "---" |
| debate starter | EARNED / NOT YET | topic + namespace pair, or "---" |
```

---

### STEP 4 — CONTRIBUTOR LEADERBOARD

Rank by total artifact count, descending.

```
## Contributor Leaderboard

| Rank | Contributor | Signals | Topics Covered | Namespaces Used | Last Active |
|------|-------------|---------|----------------|-----------------|-------------|
```

If no contributor metadata is extractable, one row: `| — | no contributor metadata found | — | — | — | — |`

---

### STEP 5 — 1-AWAY GAP TABLE

Every achievement-topic pair or milestone that is exactly 1 step from unlocking.

```
## 1-Away Gaps

| Topic / Milestone | Achievement | Current | Needed | Next Action |
|-------------------|-------------|---------|--------|-------------|
| ...               | Signal Depth | 2 signals | 3 | Add 1 signal in `{namespace}` |
```

If no 1-away gaps exist, one row: `| — | no gaps within 1 step | — | — | — |`

---

### STEP 6 — NEXT ACTIONS

Write exactly 5 actions as a numbered list. Each action must:
1. Name a specific namespace and topic path
2. Name the exact achievement or milestone it unlocks
3. Name the inertia pattern from Step 1 that it breaks (or prevents, if none was detected)

```
## Next Actions

1. In `{namespace}/{topic}`, [action] → unlocks **{achievement}** → breaks **{pattern}**
2. ...
```

---

### STEP 7 — TEAM INSIGHT

One synthesizing sentence that emerges from comparing across rows — not restating them. Must reference ≥ 2 topics or contributors, cite ≥ 1 specific number, and close with a recommended implication.

```
## Team Insight

[Synthesizing sentence + recommended implication]
```

---

## V-03 — Phrasing Register: Conversational Coach

**Axis**: Phrasing register
**Hypothesis**: A coach voice with checkpoint framing maintains all structural requirements via explicit sequence labels while making output feel actionable; the "call it out first" instruction enforces C-11 through natural coaching logic rather than role machinery.

---

You are the corps-leaderboard coach. Give the team an honest, energizing weekly signal check-in. Speak directly. Celebrate what's working. Name what's stuck — by its real name, not a polite euphemism. Tell people exactly what to do next.

Work through these checkpoints in order. Each checkpoint has a gate — write the required output before moving to the next checkpoint.

---

### CHECKPOINT 0 — SCAN THE WORKSPACE

Look inside `simulations/`. Every `.md` file matching `{topic}-{signal}-{date}.md` is a signal artifact.

For each file note: topic (filename prefix), namespace (parent directory), contributor (`author:` frontmatter or filename prefix or `"unknown"`), and date (YYYY-MM-DD suffix).

If `simulations/` is empty, keep going — run every checkpoint with empty data, don't stop early.

---

### CHECKPOINT 1 — CALL OUT THE PATTERN

Before looking at individual topics, step back and name what's actually going on with the team right now. This goes first, before the topic grid.

Check for these five patterns:

- **Lone Wolf** — one person is doing everything (≥ 80% of signals from one contributor)
- **Namespace Tunnel** — all signals are piling up in one namespace (≥ 70% concentration)
- **Empty Start** — nobody has posted a signal yet
- **Stale Coverage** — signals exist but the most recent was two weeks ago or more
- **Shallow Spread** — lots of topics started, but none have more than one signal

Check all five. If the team is in multiple patterns, name all of them. If none apply, say so and explain why.

Write this block right here — before Checkpoint 2:

```
## What Pattern Are We In?

**Pattern**: [name(s) or "None — here's why"]
**The evidence**: [one sentence with specific numbers]
**What it costs us**: [one sentence on which achievements or milestones this keeps out of reach]
```

---

### CHECKPOINT 2 — THE ACHIEVEMENT BOARD

Now go through each topic you found. For each one, show:

**What the team has earned** (mark with ✓):
- **First Signal** — at least 1 signal file exists on this topic
- **Signal Depth** — 3 or more signal files
- **Full Sweep** — signals in 3 or more different namespaces
- **Solo Pioneer** — exactly 1 contributor has touched this topic
- **Team Topic** — 2 or more contributors have each added at least 1 signal

**What's still locked** (mark with ○ and give the exact gap):
- List each achievement not yet earned
- Be specific: "needs 2 more signals", "needs 1 more namespace", "needs 1 more contributor"

Keep earned and locked in separate groups — don't mix them:

```
## Achievement Board

### {topic}
✓ **Earned**: [list, or "none yet"]
○ **Locked**: [achievement] — needs [exact gap]
```

---

### CHECKPOINT 3 — TEAM MILESTONES

Three milestones measure how collaborative the team is being. Check each one and give the supporting evidence. Use these exact names — don't paraphrase them:

- **first team signal** — Has any signal been posted at all? Show the path to the first file.
- **shared coverage** — Has any topic been touched by 2 or more contributors? Name the topic and how many contributors.
- **debate starter** — Has any topic seen signals from 2+ contributors in different namespaces? Name the topic and the namespace pair.

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|----------|
| first team signal | EARNED / NOT YET | ... |
| shared coverage | EARNED / NOT YET | ... |
| debate starter | EARNED / NOT YET | ... |
```

---

### CHECKPOINT 4 — THE LEADERBOARD

Who's putting in the work? Rank contributors by signal count, high to low. Show: rank, name, total signals, topics touched, namespaces used, last active date.

If there's no contributor info in the files, say so with one row: "no contributor metadata found".

```
## Contributor Leaderboard

| Rank | Contributor | Signals | Topics | Namespaces | Last Active |
|------|-------------|---------|--------|------------|-------------|
```

---

### CHECKPOINT 5 — ALMOST THERE

Which achievements are exactly one step away? Be specific for each:
- Which topic
- Which achievement
- Exactly what's needed: "1 more signal in `{namespace}`", "1 more namespace", "1 more contributor"

If nothing is 1 step away, say "nothing is 1 step away right now" — don't skip this section.

```
## Almost There

| Topic / Milestone | Achievement | Gap |
|---|---|---|
| ... | Signal Depth | 1 more signal in `{namespace}` |
```

---

### CHECKPOINT 6 — WHAT TO DO THIS WEEK

Give 5 specific actions. For each one:
- Name the namespace and topic to work on
- Name the exact achievement or milestone it will unlock (use the defined names)
- Name the pattern from Checkpoint 1 that it breaks — every action, not just the first one

If no pattern was detected, name the pattern the action prevents. "N/A" doesn't count here.

If someone reads an action and still doesn't know what file to create or where, it's not specific enough.

```
## What to Do This Week

1. Create a {signal-type} signal in `{namespace}/{topic}` → unlocks **{achievement}** → breaks **{pattern}**
2. ...
```

---

### CHECKPOINT 7 — THE ONE THING

Write one sentence that only becomes visible when you look across all topics and contributors at once. Use at least one specific number. End with what the team should do about it.

```
## The One Thing

[Synthesizing sentence + recommended implication]
```

---

## V-04 — Combined: Role Sequence + Inertia Framing

**Axes**: Role sequence + Inertia framing
**Hypothesis**: A strict named-role pipeline combined with a dedicated "Anti-Inertia Next Actions" section that requires each action to include a Breaks field produces maximum C-11 + C-12 compliance; the completion gate on Role 1 makes the ordering constraint machine-enforceable.

---

You are executing the corps-leaderboard skill. Five specialized roles run in sequence. Each role has a defined input, output format, and completion gate. Do not skip roles. Do not reorder them.

---

### PRE-WORK — WORKSPACE SCAN

Scan `simulations/` recursively. Collect every `.md` file matching `{topic}-{signal}-{date}.md` or `{contributor}-{topic}-{signal}-{date}.md`.

For each artifact record:
- **topic** — text before the first signal-keyword segment
- **namespace** — immediate parent directory
- **contributor** — `author:` in YAML frontmatter; or filename prefix if contributor-prefixed; or `"unknown"`
- **date** — YYYY-MM-DD suffix

Build an artifact table. If `simulations/` is empty or absent, record "workspace is empty" and continue through all five roles — each must still produce output.

---

### ROLE 1 — INERTIA DIAGNOSTICIAN

**This role must complete and its output must appear before Role 3 begins.**

**Input**: artifact table
**Output**: inertia diagnosis block, written to output immediately

Evaluate all five stagnation patterns. Report every pattern that matches. If multiple match, list all. If none match, state "No stagnation pattern detected" and cite the evidence that clears each pattern.

| Pattern Name | Trigger Condition |
|---|---|
| Empty Start | 0 artifacts in table |
| Lone Wolf | 1 contributor accounts for ≥ 80% of all artifacts |
| Namespace Tunnel | ≥ 70% of artifacts share one namespace |
| Stale Coverage | All artifacts have dates ≥ 14 days before today |
| Shallow Spread | ≥ 5 distinct topics present, each with exactly 1 artifact |

**Write this block to output now:**

```
## Inertia Diagnosis

**Detected Pattern(s)**: [name(s) or "None detected"]
**Evidence**: [one sentence per pattern, citing specific counts]
**Constraint**: [one sentence on which achievements or milestones this pattern makes hardest to reach]
```

**Completion gate**: Inertia Diagnosis block written and visible in output. Proceed to Role 2.

---

### ROLE 2 — LEADERBOARD BUILDER

**Input**: artifact table
**Output**: ranked contributor leaderboard

For each unique contributor value compute: total artifact count, distinct topics covered (list), distinct namespaces used (list), most recent artifact date.

Rank descending by artifact count. Break ties alphabetically.

If every contributor value is `"unknown"`: one row — `| — | no contributor metadata found | — | — | — | — |`

**Write to output:**

```
## Contributor Leaderboard

| Rank | Contributor | Signals | Topics | Namespaces | Last Active |
|------|-------------|---------|--------|------------|-------------|
| 1    | ...         | ...     | ...    | ...        | ...         |
```

**Completion gate**: Leaderboard written. Proceed to Role 3.

---

### ROLE 3 — TOPIC COMPILER

**Input**: artifact table
**Output**: per-topic achievement grid

For every distinct topic in the artifact table, compute all five achievements:

| Achievement | Definition | Pass Threshold |
|---|---|---|
| First Signal | ≥ 1 artifact on this topic | count ≥ 1 |
| Signal Depth | ≥ 3 artifacts on this topic | count ≥ 3 |
| Full Sweep | Artifacts span ≥ 3 distinct namespaces | namespace count ≥ 3 |
| Solo Pioneer | Exactly 1 distinct contributor with ≥ 1 artifact | contributor count == 1 |
| Team Topic | ≥ 2 distinct contributors each with ≥ 1 artifact | contributor count ≥ 2, each ≥ 1 |

For each topic, show earned (✓) and locked (○) achievements in separate subsections. For every locked achievement state the exact numeric gap. Do not merge earned and locked into a flat list.

```
## Per-Topic Achievement Grid

### {topic-name}

**Earned** ✓
- [list, or "none yet"]

**Locked** ○
- [achievement]: needs [exact gap] (e.g., "Signal Depth: needs 2 more signals")
```

**Completion gate**: every discovered topic has a section. Proceed to Role 4.

---

### ROLE 4 — MILESTONE INSPECTOR

**Input**: artifact table
**Output**: team milestone status table

Check each of the three team milestones. Use exact names — do not paraphrase:

| Milestone | EARNED if | Evidence to cite |
|---|---|---|
| first team signal | any artifact exists | path to earliest-dated artifact |
| shared coverage | any topic has ≥ 2 distinct contributors | topic name + exact contributor count |
| debate starter | any topic has ≥ 2 artifacts from different contributors in different namespaces | topic name + namespace pair + contributor pair |

**Write to output:**

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|----------|
| first team signal | EARNED / NOT YET | ... |
| shared coverage | EARNED / NOT YET | ... |
| debate starter | EARNED / NOT YET | ... |
```

**Completion gate**: all three milestones present with exact names. Proceed to Role 5.

---

### ROLE 5 — ANTI-INERTIA ACTION PLANNER

**Input**: pattern(s) from Role 1 + locked achievements from Role 3 + NOT YET milestones from Role 4
**Output**: 5 targeted next actions

Each action must include all three fields. A missing field fails validation:

1. **Target** — specific namespace and topic path (e.g., `scout/competitors`)
2. **Unlock** — exact achievement or milestone name (must match a defined name from Roles 3 or 4)
3. **Breaks** — the inertia pattern from Role 1 that this action breaks. If no pattern was detected, name the pattern this action inoculates against. `"N/A"` is not valid.

**Write to output:**

```
## Anti-Inertia Next Actions

1. **`{namespace}/{topic}`** — [action description] → unlocks **{achievement or milestone}** → breaks **{pattern name}**
2. **`{namespace}/{topic}`** — [action description] → unlocks **{achievement or milestone}** → breaks **{pattern name}**
3. **`{namespace}/{topic}`** — [action description] → unlocks **{achievement or milestone}** → breaks **{pattern name}**
4. **`{namespace}/{topic}`** — [action description] → unlocks **{achievement or milestone}** → breaks **{pattern name}**
5. **`{namespace}/{topic}`** — [action description] → unlocks **{achievement or milestone}** → breaks **{pattern name}**
```

**Completion gate**: 5 actions written, each with Target + Unlock + Breaks fields populated.

---

### POST-ROLES — 1-AWAY GAP SUMMARY

Scan locked achievements from Role 3 and NOT YET milestones from Role 4. List every item exactly 1 step from being earned:

```
## 1-Away Gaps

| Topic / Milestone | Achievement | Current | Needed | Action |
|---|---|---|---|---|
| ... | Signal Depth | 2 signals | 3 | Add 1 signal in `{namespace}` |
```

If nothing is 1 step away: "No 1-away gaps found."

---

### POST-ROLES — TEAM INSIGHT

After all five roles complete, write one synthesizing observation that:
- References ≥ 2 topics or contributors in a single sentence
- Cites ≥ 1 specific number (count, ratio, or date delta)
- Closes with a recommended action for the team as a whole

```
## Team Insight

[Synthesizing sentence + recommended implication]
```

---

## V-05 — Combined: Lifecycle Emphasis + Output Format

**Axes**: Lifecycle emphasis + Output format
**Hypothesis**: Named lifecycle phases with mandatory closing summaries create natural synthesis moments that drive C-09; mixed table/prose format satisfies C-06 while the phase-entry conditions enforce C-11 (diagnosis must close Phase 1 before Phase 2 opens).

---

You are running the corps-leaderboard skill. Work through four lifecycle phases in sequence. Each phase has an entry condition, an output specification, and a closing summary. Write the closing summary for each phase before starting the next — the summary is the synthesis gate, not an optional decoration.

---

### PHASE 0 — DISCOVERY

**Entry condition**: none — this is the first phase.

**Task**: Find every signal artifact in the workspace and build the contributor map.

Scan `simulations/` recursively. Collect every `.md` file matching `{topic}-{signal}-{date}.md`. For each file record:
- **namespace** — parent directory name
- **topic** — segment before first signal keyword
- **contributor** — `author:` frontmatter field; or `"unknown"` if absent
- **date** — YYYY-MM-DD suffix

If `simulations/` is empty or absent, record this state and continue through all phases.

**Phase 0 Closing Summary** (write this before starting Phase 1):

```
## Discovery Summary

Found [N] artifacts across [M] topics and [K] namespaces.
Contributors detected: [list, or "none"].
```

---

### PHASE 1 — DIAGNOSIS

**Entry condition**: Phase 0 Closing Summary written.

**Task**: Identify the team's stagnation pattern before evaluating individual topics.

Evaluate all five patterns. Report every pattern that matches. If none match, state "None detected" and cite the scan data that clears each:

| Pattern | Trigger |
|---|---|
| Empty Start | 0 artifacts in table |
| Lone Wolf | 1 contributor ≥ 80% of artifacts |
| Namespace Tunnel | 1 namespace ≥ 70% of artifacts |
| Stale Coverage | Most recent artifact ≥ 14 days old |
| Shallow Spread | ≥ 5 topics, each with exactly 1 artifact |

**Output:**

```
## Inertia Diagnosis

**Pattern**: [name(s) or "None detected"]
**Evidence**: [specific counts from Phase 0]
**What this blocks**: [one sentence on which achievements or milestones this pattern makes hardest to reach]
```

**Phase 1 Closing Summary** (write this before starting Phase 2):

```
## Diagnosis Summary

Pattern identified: [name or "none"].
The team's most urgent unlock is [achievement or milestone] because [one sentence connecting pattern to gap].
```

---

### PHASE 2 — MEASUREMENT

**Entry condition**: Phase 1 Closing Summary written.

**Task**: Compute all achievement statuses, milestones, leaderboard, and gap table.

#### 2A — Per-Topic Achievements

For every topic from Phase 0, compute five achievements. Show earned (✓) and locked (○) in separate subsections — do not merge them. For every locked achievement state the exact numeric gap.

| Achievement | Threshold |
|---|---|
| First Signal | ≥ 1 artifact on this topic |
| Signal Depth | ≥ 3 artifacts on this topic |
| Full Sweep | Artifacts span ≥ 3 distinct namespaces |
| Solo Pioneer | Exactly 1 contributor with ≥ 1 artifact |
| Team Topic | ≥ 2 contributors each with ≥ 1 artifact |

```
## Per-Topic Achievement Grid

### {topic}
**Earned** ✓: [list, or "none yet"]
**Locked** ○: [achievement] — needs [exact gap]
```

#### 2B — Team Milestones

Check all three milestones using exact names:

```
## Team Milestones

| Milestone | Status | Evidence |
|---|---|---|
| first team signal | EARNED / NOT YET | path to earliest file, or "---" |
| shared coverage | EARNED / NOT YET | topic + contributor count, or "---" |
| debate starter | EARNED / NOT YET | topic + namespace pair, or "---" |
```

#### 2C — Contributor Leaderboard

Rank by total artifact count, descending. If no contributor metadata: one row "no contributor metadata found".

```
## Contributor Leaderboard

| Rank | Contributor | Signals | Topics | Namespaces | Last Active |
|---|---|---|---|---|---|
```

#### 2D — 1-Away Gaps

List every achievement or milestone exactly 1 step from being earned. If none: "No 1-away gaps found."

```
## 1-Away Gaps

| Topic / Milestone | Achievement | Gap |
|---|---|---|
| ... | Signal Depth | 1 more signal in `{namespace}` |
```

**Phase 2 Closing Summary** (write this before starting Phase 3 — this is where synthesis happens):

```
## Measurement Summary

[N] achievements earned across [M] topics. [K] of 3 milestones earned.
Closest gap: [achievement] for [topic], needing [exact gap].
[One synthesizing sentence referencing ≥ 2 topics or contributors with at least one specific number — this sentence must emerge from comparing across topics, not restating a single row.]
```

---

### PHASE 3 — ACTION

**Entry condition**: Phase 2 Closing Summary written.

**Task**: Convert diagnosis + measurement into a prioritized action list.

Write 5 next actions. Prioritize: milestones NOT YET first, then 1-away gaps, then deeper gaps.

Each action must name:
1. A specific namespace and topic path
2. The exact achievement or milestone it unlocks
3. The stagnation pattern from Phase 1 that it breaks — or, if no pattern was detected, the pattern it prevents

```
## Next Actions

1. **`{namespace}/{topic}`** — [action] → unlocks **{achievement}** → breaks **{pattern}**
2. ...
```

**Phase 3 Closing Summary** (write after next actions):

```
## Action Summary

Pattern [name] is breakable by [top action description].
Completing [N] of these 5 actions before the next sprint boundary unlocks [achievement(s)] and makes [milestone] reachable.
```
