Written to `simulations/quest/variations/corps-leaderboard-variations-R4-2026-03-17.md`.

---

## R4 Variation Map

All 5 carry **C-15 + C-16 + C-17** as the shared new baseline. Primary differentiating axis per variation:

| | Variation | Axis | C-15 mechanism | C-16 mechanism | C-17 mechanism |
|--|-----------|------|---------------|---------------|---------------|
| **V-01** | All-Tables Scorecard | Output format | `SIGNAL HEALTH SCORECARD must close before ACHIEVEMENT MATRIX opens. No exceptions.` | Scorecard table with Score/Tier summary rows + `Priority: [Tier] — score [n]/5` in actions | CONTRIBUTOR LEADERBOARD is first named section |
| **V-02** | Triple-Gate Pipeline | Role sequence | GATE 2 line: `[GATE 2: SIGNAL HEALTH SCORE closed. ACHIEVEMENT COMPILATION opens now.]` + `SIGNAL HEALTH SCORE must close before ACHIEVEMENT COMPILATION opens. No exceptions.` | Health score table with tier labels + `Priority: [Tier]` in actions | CONTRIBUTOR LEADERBOARD runs before SIGNAL HEALTH SCORE; GATE 1 is explicit |
| **V-03** | Conversational Coach | Phrasing register | `TEAM HEALTH SCORE must be complete before TOPIC ACHIEVEMENTS begins. No exceptions.` | "Team Health Score" table with health levels + `Health: [level] — score [n]/5` in actions | WHO'S CONTRIBUTING is first section; health score explicitly references it |
| **V-04** | SITREP + Health Score | Inertia framing + format | `ASSESSMENT must close before FINDINGS opens. No exceptions.` (inherited from R3 V-05) | Signal Health Score table added to ASSESSMENT + `Priority: [Tier] — score [n]/5` in ACTIONS | SITUATION contains Contributor Leaderboard; ASSESSMENT follows and cites it |
| **V-05** | Cascading Contracts | Lifecycle emphasis | Closing contract on SIGNAL HEALTH: `SIGNAL HEALTH must close before ACHIEVEMENT LOG opens. No exceptions.` | Health score in SIGNAL HEALTH section + `Priority: [Tier] — score [n]/5` in RECOMMENDED ACTIONS | CONTRIBUTOR ROSTER is first section; closing contract explicitly gates SIGNAL HEALTH |

**Key design decisions for R4:**

1. **C-15 in every variation** — Each uses named section labels (not role/step numbers) in its gate language. The gate text always names the closing section AND the opening section by their heading label.

2. **C-16 in every variation** — Every health score table includes both the 0-5 numeric score and a tier definition block (Healthy / Monitor / Alert / Critical). Every action template includes a `Priority: [Tier] — score [n]/5` field, making tier reference mandatory in actions.

3. **C-17 in every variation** — The leaderboard section runs before the health/pattern diagnosis section in every variation. The health/pattern section explicitly references the leaderboard data (e.g., "cite Contributor Leaderboard row if applicable").

4. **V-02 differentiator** — Gate lines appear as literal output text `[GATE N: X closed. Y opens now.]`, making the gate artifact visible in the output rather than just in the instruction. This is the strongest possible enforcement — a skipped gate leaves a visible gap in the output.

5. **V-05 differentiator** — Bidirectional contracts (every section names both its predecessor and its successor) mean each transition is enforced twice. A single section skip would violate both the preceding section's closing contract and the skipped section's entry contract.
 covered (descending).

```
## Contributor Leaderboard

| Rank | Contributor | Signals | Topics | Namespaces | Last Active |
|------|-------------|---------|--------|-----------|------------|
| 1    | [name]      | [n]     | [n]    | [list]    | [date]     |
```

If no contributor metadata is extractable from frontmatter or filename:
`| -- | no contributor metadata found | -- | -- | -- | -- |`

Do not omit this section regardless of workspace state.

**CONTRIBUTOR LEADERBOARD must close before SIGNAL HEALTH SCORECARD opens. No exceptions.**

---

### SECTION — SIGNAL HEALTH SCORECARD

**Position: second section. Completion gate: this block must appear before ACHIEVEMENT MATRIX begins.**

Using the artifact table and the leaderboard from the preceding section, evaluate all five stagnation conditions. Add one point for each condition that fires. Where the Contributor Leaderboard corroborates a fired condition, reference the leaderboard row explicitly in the Evidence column.

| Score | Condition | Fires when |
|-------|-----------|-----------|
| +1 | Empty Start | total signals == 0 |
| +1 | Lone Wolf | one contributor >= 80% of total signals (excluding "unknown") |
| +1 | Namespace Tunnel | one namespace >= 70% of total signals |
| +1 | Stale Coverage | most recent artifact >= 14 days before today |
| +1 | Shallow Spread | >= 5 distinct topics each with exactly 1 signal |

```
## Signal Health Scorecard

| Condition | Fires? | Evidence |
|-----------|--------|---------|
| Empty Start | YES / NO | [total signal count, or --] |
| Lone Wolf | YES / NO | [contributor name + % — cite Contributor Leaderboard row if applicable] |
| Namespace Tunnel | YES / NO | [namespace name + % or --] |
| Stale Coverage | YES / NO | [most recent date or --] |
| Shallow Spread | YES / NO | [topic count + single-signal topic count or --] |

| | |
|-|-|
| **Score** | [n]/5 |
| **Tiers** | 0 — Healthy \| 1-2 — Monitor \| 3-4 — Alert \| 5 — Critical |
| **Current Tier** | [Healthy / Monitor / Alert / Critical] |
| **Active Conditions** | [comma-separated list of fired condition names, or "none"] |
| **What this blocks** | [which achievement or milestone is most at risk — one phrase] |
```

**SIGNAL HEALTH SCORECARD must close before ACHIEVEMENT MATRIX opens. No exceptions.**

---

### SECTION — ACHIEVEMENT MATRIX

**Entry condition: SIGNAL HEALTH SCORECARD closed.**

One row per topic from the artifact table. Five achievement columns. Cell notation:
- `*` — earned
- `-N sig` — locked, needs N more signals
- `-N ns` — locked, needs N more namespaces
- `-N contrib` — locked, needs N more contributors
- `?` — indeterminate (metadata unavailable — add footnote)

Achievement definitions (use exact column names — paraphrasing fails):

| Column | Earned when |
|--------|------------|
| First Signal | signals >= 1 |
| Signal Depth | signals >= 3 |
| Full Sweep | distinct namespaces >= 3 |
| Solo Pioneer | contributors == 1 AND signals >= 1 |
| Team Topic | contributors >= 2, each with >= 1 signal |

```
## Achievement Matrix

| Topic | First Signal | Signal Depth | Full Sweep | Solo Pioneer | Team Topic |
|-------|-------------|-------------|-----------|-------------|-----------|
| [path] | * | -2 sig | -1 ns | * | -1 contrib |
| **EARNED TOTAL** | [n] | [n] | [n] | [n] | [n] |
```

Every topic from the artifact table must appear as a row. A topic present in the artifact table but absent from the matrix is a matrix gap.

If workspace was empty: output the column headers with note "No topics found — all cells empty."

**ACHIEVEMENT MATRIX must close before TEAM MILESTONES opens. No exceptions.**

---

### SECTION — TEAM MILESTONES

**Entry condition: ACHIEVEMENT MATRIX closed.**

Use exact milestone names — paraphrasing or abbreviation fails:

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|---------|
| first team signal | EARNED / NOT YET | [path or "none"] |
| shared coverage | EARNED / NOT YET | [topic + contributor count or "none"] |
| debate starter | EARNED / NOT YET | [topic + namespace list or "none"] |
```

---

### SECTION — 1-AWAY GAPS

From locked matrix cells and NOT YET milestones, list every item exactly 1 unit from being earned:

```
## 1-Away Gaps

| Topic / Milestone | Achievement | Current | Needed | To Unlock |
|-------------------|-------------|---------|--------|-----------|
| [path] | Signal Depth | 2 signals | 3 | Add 1 signal in `{namespace}` |
```

If nothing is 1 step away: "No 1-away gaps found. Closest: [topic] needs [n] more [unit] for **[Achievement]**."

**TEAM MILESTONES + 1-AWAY GAPS must close before NEXT ACTIONS opens. No exceptions.**

---

### SECTION — NEXT ACTIONS

**Entry condition: TEAM MILESTONES closed.**
**Input: Active Conditions from SIGNAL HEALTH SCORECARD + locked matrix cells + NOT YET milestones.**

Write at least 3 actions. Each uses this three-field template — all fields required:

```
## Next Actions

1. **`{namespace}/{topic}`** — [action description]
   -> Unlocks: **{exact achievement or milestone name}**
   -> Breaks: **{condition name from Signal Health Scorecard Active Conditions}**
   -> Priority: [Current Tier from Signal Health Scorecard] — score [n]/5

2. ...

3. ...
```

**No action may omit the Breaks field. "N/A" is not valid.** If Signal Health Scorecard shows no active conditions (score = 0, tier = Healthy), the Breaks field writes `prevents: {condition name}` and states the prevention rationale in one clause.

Order actions by health tier: Alert or Critical tier means address all fired conditions, not just the easiest.

---

### SECTION — TEAM SYNTHESIS

Write one synthesizing sentence visible only by reading across multiple rows of the achievement matrix or multiple leaderboard entries — not from any single row. Must reference >= 2 topics or contributors, cite >= 1 specific number, and close with a recommended implication.

```
## Team Synthesis

[Synthesizing sentence + recommended implication]
```

---

### WRITE ARTIFACT

`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
health_score: [n]/5
health_tier: [Healthy / Monitor / Alert / Critical]
active_conditions: [list or "none"]
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
---
```

---

## V-02 — Role Sequence: Triple-Gate Pipeline

**Axis**: Role sequence — three named completion gates, each gate written as an explicit output line naming the closing section and the opening section by label
**Hypothesis**: Making each gate a visible output artifact (not just an instruction) means the gate cannot be silently skipped — it either appears in the output or it is missing. Three sequential gates (LEADERBOARD closes / SIGNAL HEALTH SCORE opens, SIGNAL HEALTH SCORE closes / ACHIEVEMENT COMPILATION opens, ACHIEVEMENT COMPILATION closes / TEAM MILESTONES opens) each satisfy C-15 independently, making the section ordering triply enforced. The leaderboard as the first role satisfies C-17. The health score with urgency tiers satisfies C-16. Risk: three visible gate lines could feel mechanical; the test is whether structure-as-output is cleaner or noisier than structure-as-instruction.

---

You are running `corps-leaderboard`. No inputs — scan and compute from workspace state.

Three named gates control the execution pipeline. Each gate appears as a line in the output. No section opens until its gate line is written.

---

### PRE-WORK — WORKSPACE SCAN

Glob `simulations/**/*.md`. For every file record:
- **topic** — subdirectory path under `simulations/`
- **namespace** — first path segment
- **contributor** — `author:` or `contributor:` from YAML frontmatter; filename prefix before first `-`; or `"unknown"`
- **date** — YYYY-MM-DD from filename

Internal scan result:

```
SCAN RESULT (internal)
  topics: [list — per-topic: signal_count, contributors, namespaces, most_recent_date]
  all_contributors: [deduplicated]
  all_namespaces: [deduplicated]
  total_signals: [n]
  most_recent_date: [date or "none"]
```

If `simulations/` is empty or absent, record `{workspace: empty}` and continue — all sections must still produce output.

---

### CONTRIBUTOR LEADERBOARD

Rank contributors descending by signal count. Ties broken by topics covered (descending).

```
## Contributor Leaderboard

| Rank | Contributor | Signals | Topics | Namespaces | Last Active |
|------|-------------|---------|--------|-----------|------------|
| 1    | [name]      | [n]     | [n]    | [list]    | [date]     |
```

If no contributor metadata extractable from frontmatter or filename:
`| -- | no contributor metadata found | -- | -- | -- | -- |`

Do not omit this section regardless of workspace state.

---

```
[GATE 1: CONTRIBUTOR LEADERBOARD closed. SIGNAL HEALTH SCORE opens now.]
```

**CONTRIBUTOR LEADERBOARD must close before SIGNAL HEALTH SCORE opens. No exceptions.**

---

### SIGNAL HEALTH SCORE

**Entry condition: GATE 1 written. This section may not begin until GATE 1 appears in output.**

Using the scan result and the Contributor Leaderboard above, evaluate all five stagnation conditions. Add one point per fired condition. Where the leaderboard corroborates a fired condition, cite the leaderboard row explicitly.

| Score | Condition | Fires when |
|-------|-----------|-----------|
| +1 | Empty Start | total_signals == 0 |
| +1 | Lone Wolf | one contributor >= 80% of total_signals (excluding "unknown") |
| +1 | Namespace Tunnel | one namespace >= 70% of total_signals |
| +1 | Stale Coverage | most_recent_date >= 14 days before today |
| +1 | Shallow Spread | >= 5 topics each with exactly 1 signal |

```
## Signal Health Score

| Condition | Fires? | Evidence |
|-----------|--------|---------|
| Empty Start | YES / NO | [count or --] |
| Lone Wolf | YES / NO | [contributor + % — reference Contributor Leaderboard row if applicable] |
| Namespace Tunnel | YES / NO | [namespace + % or --] |
| Stale Coverage | YES / NO | [most recent date or --] |
| Shallow Spread | YES / NO | [topic count + single-signal count or --] |

**Score: [n]/5**
**Tiers:**
- 0 -> Healthy — no stagnation detected
- 1-2 -> Monitor — patterns emerging; address within the sprint
- 3-4 -> Alert — signal discipline breaking down; prioritize intervention
- 5 -> Critical — full stagnation; team has lost signal momentum

**Current Tier: [Healthy / Monitor / Alert / Critical]**
**Active Conditions: [list of fired condition names, or "none"]**
**What this blocks: [one sentence — which achievement or milestone is hardest to reach given active conditions]**
```

---

```
[GATE 2: SIGNAL HEALTH SCORE closed. ACHIEVEMENT COMPILATION opens now.]
```

**SIGNAL HEALTH SCORE must close before ACHIEVEMENT COMPILATION opens. No exceptions.**

---

### ACHIEVEMENT COMPILATION

**Entry condition: GATE 2 written. This section may not begin until GATE 2 appears in output.**

For every topic in the scan result, evaluate all five achievements. Show earned and locked in separate subsections. State the exact numeric gap for every locked achievement.

Achievement definitions (exact names required — paraphrasing fails):

| Achievement | Earned when |
|-------------|-----------|
| First Signal | signals >= 1 |
| Signal Depth | signals >= 3 |
| Full Sweep | distinct namespaces >= 3 |
| Solo Pioneer | contributors == 1 AND signals >= 1 |
| Team Topic | contributors >= 2, each with >= 1 signal |

```
## Achievement Compilation

### [topic path]

**Earned**
- [Achievement name] — [evidence: signal count / namespace count / contributor count]

**Locked**
- [Achievement name] — needs [exact gap, e.g., "2 more signals", "1 more namespace"]
```

Every topic from the scan result must appear. A topic in the scan result but absent from the compilation is a compilation gap.

If workspace was empty: write all section headers with "no topics found."

---

```
[GATE 3: ACHIEVEMENT COMPILATION closed. TEAM MILESTONES opens now.]
```

---

### TEAM MILESTONES

**Entry condition: GATE 3 written.**

Use exact milestone names — paraphrasing or abbreviation fails:

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|---------|
| first team signal | EARNED / NOT YET | [path or "none"] |
| shared coverage | EARNED / NOT YET | [topic + contributor count or "none"] |
| debate starter | EARNED / NOT YET | [topic + namespace list or "none"] |
```

---

### 1-AWAY GAPS

From locked achievement entries (ACHIEVEMENT COMPILATION) and NOT YET milestones (TEAM MILESTONES), extract every item exactly 1 step from being earned:

```
## 1-Away Gaps

- [topic/milestone]: needs [1 more signal / 1 more contributor / 1 more namespace]
  to unlock **[exact Achievement or Milestone name]**
```

If nothing is 1 step away: "No 1-away gaps. Closest: [topic] needs [n] more [unit] for **[Achievement]**."

---

### NEXT ACTIONS

**Input: Active Conditions from SIGNAL HEALTH SCORE + locked entries from ACHIEVEMENT COMPILATION + NOT YET milestones.**

Write at least 3 actions. Each uses this three-field template — all fields required:

```
## Next Actions

1. **`{namespace}/{topic}`** — [action description]
   -> Unlocks: **{exact achievement or milestone name}**
   -> Breaks: **{condition name from Signal Health Score Active Conditions}**
   -> Priority: [Current Tier from Signal Health Score] — score [n]/5

2. ...

3. ...
```

**No action may omit the Breaks field. "N/A" is not valid.** If Signal Health Score shows no active conditions (score = 0), Breaks writes `prevents: {condition name}` with one-clause prevention rationale.

---

### TEAM INSIGHT

Write one synthesizing sentence visible only from reading across the full output — not from any single topic entry or leaderboard row. Must reference >= 2 topics or contributors, cite >= 1 specific number, and close with a recommended implication.

```
## Team Insight

[Synthesizing sentence + recommended implication]
```

---

### WRITE ARTIFACT

`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
health_score: [n]/5
health_tier: [Healthy / Monitor / Alert / Critical]
active_conditions: [list or "none"]
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
---
```

---

## V-03 — Phrasing Register: Conversational Coach

**Axis**: Phrasing register — warm, direct coaching voice ("your team", "almost there", "what to do next")
**Hypothesis**: A conversational register makes the output accessible to team leads who are not familiar with formal skill vocabulary. Structural completeness criteria can still be satisfied when the mechanism is correct — section-boundary language still names sections, the health score table still uses exact condition labels, the leaderboard still runs first. The question is whether warm phrasing degrades precision in any criterion that requires exact terminology (C-02 achievement names, C-03 milestone names, C-10 pattern names). Risk mitigation: exact names appear in tables and field templates even when surrounding prose is casual.

---

You are running `corps-leaderboard`. No inputs — scan the workspace and give your team an honest look at where they stand.

---

### SCAN THE WORKSPACE

Read every signal artifact in the workspace.

Glob `simulations/**/*.md`. For each file, note:
- **topic** — the subdirectory path under `simulations/`
- **namespace** — the first path segment
- **contributor** — from `author:` or `contributor:` in frontmatter; or the part of the filename before the first `-`; or mark as `"unknown"`
- **date** — the YYYY-MM-DD from the filename

Keep an internal summary:

```
WORKSPACE SUMMARY (internal)
  topics: [list — one per distinct subdirectory path]
  per topic: { signal_count, contributors, namespaces, most_recent_date }
  all_contributors: [deduplicated]
  total_signals: [n]
  most_recent_date: [date or "none"]
```

If `simulations/` is empty or absent, note `workspace empty` and keep going — every section still needs to appear.

---

### WHO'S CONTRIBUTING

Your first job: show the team who is putting in signal work. Rank contributors by how many signals they've filed.

```
## Who's Contributing

| Rank | Contributor | Signals | Topics | Namespaces | Last Signal |
|------|-------------|---------|--------|-----------|------------|
| 1    | [name]      | [n]     | [n]    | [list]    | [date]     |
```

If you can't find contributor names in the frontmatter or filenames:
`| -- | no contributor metadata found | -- | -- | -- | -- |`

Don't skip this section even if the workspace is empty — write the table header with one empty row.

**WHO'S CONTRIBUTING must be complete before TEAM HEALTH SCORE begins. No exceptions.**

---

### TEAM HEALTH SCORE

**This section opens only after WHO'S CONTRIBUTING is complete. Position: second section — no topic compilation begins until this block is written.**

Take an honest look at your team's signal health. Check whether any of these five warning signs apply — add one point for each that does. When you check the Lone Wolf warning, look at the WHO'S CONTRIBUTING table above and cite the top contributor's share directly if it's relevant.

| Points | Condition | Warning sign |
|--------|-----------|-------------|
| +1 | Empty Start | The workspace has zero signals |
| +1 | Lone Wolf | One contributor holds 80% or more of all signals (not counting "unknown") |
| +1 | Namespace Tunnel | One namespace holds 70% or more of all signals |
| +1 | Stale Coverage | The most recent signal is 14 or more days old |
| +1 | Shallow Spread | Five or more topics each have exactly one signal and no more |

```
## Team Health Score

| Warning Sign | Active? | What we see |
|--------------|---------|-------------|
| Empty Start | Yes / No | [signal count, or --] |
| Lone Wolf | Yes / No | [top contributor name + share — reference Who's Contributing if applicable] |
| Namespace Tunnel | Yes / No | [namespace name + share, or --] |
| Stale Coverage | Yes / No | [most recent date, or --] |
| Shallow Spread | Yes / No | [how many topics with exactly 1 signal, or --] |

**Score: [n] out of 5**
**Health levels:**
- 0 — Healthy: your team's signal practice is working
- 1-2 — Monitor: warning signs are appearing; address this sprint
- 3-4 — Alert: signal discipline is breaking down; intervene now
- 5 — Critical: the team has lost signal momentum entirely

**Your team's health: [Healthy / Monitor / Alert / Critical]**
**Active warnings: [list of active condition names, or "none"]**
**What this puts at risk: [which achievement or milestone is hardest to reach right now]**
```

**TEAM HEALTH SCORE must be complete before TOPIC ACHIEVEMENTS begins. No exceptions.**

---

### TOPIC ACHIEVEMENTS

**This section opens only after TEAM HEALTH SCORE is complete.**

Go topic by topic. For each topic your team has started, check which achievements they've earned and which are still locked. Keep earned and locked achievements in separate sections — don't mix them.

These are the five achievements to check (use these exact names — any other phrasing fails):

| Achievement | When it's earned |
|-------------|-----------------|
| First Signal | 1 or more signals filed |
| Signal Depth | 3 or more signals filed |
| Full Sweep | signals spanning 3 or more distinct namespaces |
| Solo Pioneer | exactly 1 contributor with at least 1 signal |
| Team Topic | 2 or more contributors, each with at least 1 signal |

```
## Topic Achievements

### [topic path]

**Earned**
- [Achievement name] — [brief evidence]

**Locked**
- [Achievement name] — needs [exact gap: "2 more signals", "1 more namespace", "1 more contributor"]
```

Write one block for every topic in the workspace. A topic that appears in the workspace but is missing from this section is a topic gap.

If the workspace is empty, write the section header with "no topics found."

**TOPIC ACHIEVEMENTS must be complete before TEAM MILESTONES begins. No exceptions.**

---

### TEAM MILESTONES

**This section opens only after TOPIC ACHIEVEMENTS is complete.**

These are the three milestones your whole team earns together. Check each one using its exact name — don't rename or abbreviate:

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|---------|
| first team signal | EARNED / NOT YET | [path to earliest file, or "none"] |
| shared coverage | EARNED / NOT YET | [topic path + number of contributors, or "none"] |
| debate starter | EARNED / NOT YET | [topic path + which namespaces, or "none"] |
```

---

### ALMOST THERE

From the locked achievements and NOT YET milestones above, pick out every item exactly one step away from being unlocked:

```
## Almost There

- [topic or milestone]: add [1 signal / 1 contributor / 1 namespace] to unlock **[exact Achievement or Milestone name]**
```

If nothing is that close: "Nothing is one step away right now. The closest is: [topic] needs [n] more [unit] to reach **[Achievement]**."

---

### WHAT TO DO NEXT

**Input: active warnings from TEAM HEALTH SCORE + locked achievements from TOPIC ACHIEVEMENTS + NOT YET milestones.**

Write at least 3 specific next moves. Fill in all three fields — they're all required:

```
## What to Do Next

1. **`{namespace}/{topic}`** — [what to do and why it matters]
   -> Unlocks: **{exact achievement or milestone name}**
   -> Breaks: **{condition name from Team Health Score active warnings}**
   -> Health: [your team's current health level from Team Health Score] — score [n]/5

2. ...

3. ...
```

**Don't leave the Breaks field blank. "N/A" is not valid.** If the health score is 0 and there are no active warnings, the Breaks field writes `prevents: {condition name}` and explains in one phrase why that condition is worth preventing now.

Prioritize moves that address the most urgent health level first.

---

### TEAM PICTURE

Write one sentence that could only be true by looking at the whole team together — something that isn't visible from any single topic or any single contributor's row. It must mention at least 2 topics or 2 contributors, include at least one specific number, and end with a recommendation.

```
## Team Picture

[Synthesizing sentence + recommendation]
```

---

### SAVE TO FILE

Write to: `simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
health_score: [n]/5
health_tier: [Healthy / Monitor / Alert / Critical]
active_warnings: [list or "none"]
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
---
```

---

## V-04 — Inertia Framing + Output Format: SITREP with Health Score

**Axes**: Inertia framing + output format — directly combines R3 V-05 (SITREP briefing structure) with R3 V-02 (Signal Health Score). ASSESSMENT adds a 0-5 quantified score with urgency tiers to the pattern diagnosis. SITUATION retains the contributor leaderboard as its primary table. The section-boundary gate "ASSESSMENT must close before FINDINGS opens. No exceptions." is preserved from R3 V-05.
**Hypothesis**: The SITREP format already satisfies C-15 (named section boundary) and C-17 (leaderboard in SITUATION, before ASSESSMENT). Adding the health score table to ASSESSMENT fills the only R3 V-05 gap (C-16). The resulting variation inherits the R3 V-05 strengths — format-level section ordering constraint, military briefing discipline — and adds quantified severity. Risk: ASSESSMENT becomes longer; the test is whether the added score table disrupts the briefing register or complements it.

---

You are producing a Signal Briefing for the team. A Signal Briefing follows a five-section structure. Each section is named. Each section closes before the next opens — this is a briefing discipline constraint, not a formatting suggestion.

Work through the sections in order.

---

### PRE-BRIEF — WORKSPACE SCAN

Before producing any briefing section, scan the workspace.

Glob `simulations/**/*.md`. For each file record:
- **topic** — subdirectory path under `simulations/`
- **namespace** — first path segment
- **contributor** — `author:` or `contributor:` from YAML frontmatter; or filename prefix before first `-`; or `"unknown"`
- **date** — YYYY-MM-DD from filename

Internal inventory:

```
INVENTORY (internal)
  topics: [list]
  per topic: { signals, contributors, namespaces, most_recent_date }
  all_contributors: [deduplicated]
  total_signals: [n]
  most_recent_date: [date or "none"]
```

If `simulations/` is empty or absent, record `{workspace: empty}` and produce all sections with empty state.

---

### SECTION 1 — SITUATION

Open the briefing. State the scan results and the contributor picture.

**Paragraph 1**: State the scan results in plain declarative language — how many topics, signals, contributors, namespaces. If workspace is empty, state this explicitly.

**Paragraph 2**: State what the contributor picture looks like. Produce the ranked contributor leaderboard:

```
## SITUATION — Contributor Leaderboard

| Rank | Contributor | Signals | Topics | Namespaces | Last Active |
|------|-------------|---------|--------|-----------|------------|
| 1    | [name]      | [n]     | [n]    | [list]    | [date]     |
```

Rank descending by signal count. Ties broken by topics covered. If no contributor metadata:
`| -- | no contributor metadata found | -- | -- | -- | -- |`

**SITUATION closes here. ASSESSMENT opens next.**

---

### SECTION 2 — ASSESSMENT

**Position: second section. ASSESSMENT must close before FINDINGS opens. No exceptions.**

Assess the team's signal-gathering health. Compute a Signal Health Score (0-5) and name the stagnation pattern — or confirm there is none. When the SITUATION leaderboard corroborates a fired condition, cite it explicitly.

Evaluate all five conditions. Add one point for each that fires:

| Score | Condition | Fires when |
|-------|-----------|-----------|
| +1 | Empty Start | total_signals == 0 |
| +1 | Lone Wolf | one contributor >= 80% of total_signals (excluding "unknown") |
| +1 | Namespace Tunnel | one namespace >= 70% of total_signals |
| +1 | Stale Coverage | most_recent_date >= 14 days before today |
| +1 | Shallow Spread | >= 5 topics each with exactly 1 signal |

Write this assessment block:

```
## ASSESSMENT

| Condition | Fires? | Evidence |
|-----------|--------|---------|
| Empty Start | YES / NO | [count or --] |
| Lone Wolf | YES / NO | [contributor + % — cite SITUATION Contributor Leaderboard row if applicable] |
| Namespace Tunnel | YES / NO | [namespace + % or --] |
| Stale Coverage | YES / NO | [most recent date or --] |
| Shallow Spread | YES / NO | [topic count + single-signal count or --] |

**Signal Health Score: [n]/5**
**Tier:**
- 0 -> Healthy — no stagnation detected; deepen existing coverage
- 1-2 -> Monitor — patterns emerging; address within the sprint
- 3-4 -> Alert — signal discipline breaking down; prioritize intervention now
- 5 -> Critical — full stagnation; team has lost signal momentum entirely

**Current Tier: [Healthy / Monitor / Alert / Critical]**
**Active Patterns: [list of fired condition names, or "None detected"]**
**Decision risk: [one sentence — which commitment or decision the team cannot safely make at current signal coverage]**
**What to watch for in FINDINGS: [one sentence — which locked achievements or milestones are most explained by the active patterns]**
```

If no condition fires, state "None detected" and cite the specific counts that clear each condition.

**ASSESSMENT closes here. FINDINGS opens next.**

---

### SECTION 3 — FINDINGS

**Entry condition: ASSESSMENT closed.**

Report achievements per topic, team milestones, and 1-away gaps.

#### 3A — Per-Topic Achievements

For every topic from the inventory, evaluate all five achievements. Earned and locked in separate subsections — do not merge. State exact gap for every locked achievement.

Achievement definitions (exact names required):

| Achievement | Earned when |
|-------------|-----------|
| First Signal | signals >= 1 |
| Signal Depth | signals >= 3 |
| Full Sweep | distinct namespaces >= 3 |
| Solo Pioneer | contributors == 1, signals >= 1 |
| Team Topic | contributors >= 2, each >= 1 signal |

```
## FINDINGS — Per-Topic Achievements

### [topic path]
**Earned** (check): [list or "none"]
**Locked** (circle): [Achievement name] — needs [exact gap]
```

Every topic must appear. A missing topic is a findings gap.

#### 3B — Team Milestones

Use exact milestone names. Do not paraphrase.

```
## FINDINGS — Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|---------|
| first team signal | EARNED / NOT YET | [path or "none"] |
| shared coverage | EARNED / NOT YET | [topic + contributor count or "none"] |
| debate starter | EARNED / NOT YET | [topic + namespace list or "none"] |
```

#### 3C — 1-Away Gaps

Every achievement or milestone exactly 1 step from being earned:

```
## FINDINGS — 1-Away Gaps

- [topic/milestone]: needs [1 more X] to unlock **[Achievement name]**
```

If none: "No 1-away gaps. Closest: [topic] needs [n] more [unit] for **[Achievement]**."

**FINDINGS closes here. ACTIONS opens next.**

---

### SECTION 4 — ACTIONS

**Entry condition: FINDINGS closed.**

Write at least 3 prioritized actions. Each uses this template — all three fields required:

```
## ACTIONS

1. **`{namespace}/{topic}`** — [action description]
   -> Unlocks: **{exact achievement or milestone name}**
   -> Breaks: **{pattern name from ASSESSMENT Active Patterns}**
   -> Priority: [ASSESSMENT Current Tier] — score [n]/5

2. ...

3. ...
```

**No action may omit the Breaks field. "N/A" is not valid.** If ASSESSMENT detected no active patterns, Breaks states `prevents: {pattern name}` and explains the prevention rationale in one clause.

Order actions by health tier: Alert or Critical tier means address all fired conditions, not just the easiest.

**ACTIONS closes here. DEBRIEF opens next.**

---

### SECTION 5 — DEBRIEF

**Entry condition: ACTIONS closed.**

Write one synthesizing statement visible only from the full briefing — not from any single FINDINGS subsection. Must reference >= 2 topics or contributors, cite >= 1 specific number, and close with a recommended implication for the team.

```
## DEBRIEF

[Synthesizing sentence + recommended implication]
```

---

### WRITE ARTIFACT

Write the complete briefing to: `simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
health_score: [n]/5
health_tier: [Healthy / Monitor / Alert / Critical]
active_patterns: [list or "none"]
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
sections_completed: 5
---
```

---

## V-05 — Lifecycle Emphasis: Cascading Contracts

**Axes**: Lifecycle emphasis + role sequence — every section states both an opening contract (entry requires X closed) and a closing contract (this section must close before Y opens). All section-boundary transitions are bidirectionally explicit.
**Hypothesis**: Making each transition bidirectional — the closing section names the next, and the opening section names its predecessor — creates two redundant enforcement points per gate. A model that skips a section would need to omit both the closing contract of the preceding section AND the opening contract of the skipped section, making skipping visibly double-violating. C-15 is satisfied by the closing contract of SIGNAL HEALTH (which names both sections). C-16 by the health score within SIGNAL HEALTH. C-17 by CONTRIBUTOR ROSTER running before SIGNAL HEALTH. Risk: bidirectional contracts make the skill longer; the test is whether the added lifecycle explicitness produces cleaner compliance or just noise.

---

You are running `corps-leaderboard`. No inputs — scan and compute from workspace state.

Each section below has two contracts: an entry contract stating what must be closed before this section opens, and a closing contract stating what must close before the next section opens. Both contracts are binding.

---

### PRE-WORK — WORKSPACE SCAN

Scan before any section begins.

Glob `simulations/**/*.md`. For every file record:
- **topic** — subdirectory path under `simulations/`
- **namespace** — first path segment
- **contributor** — `author:` or `contributor:` from YAML frontmatter; filename prefix before first `-`; or `"unknown"`
- **date** — YYYY-MM-DD from filename

Internal artifact table:

```
ARTIFACT TABLE (internal)
  [topic] | [signal count] | contributors: [list] | namespaces: [list] | most recent: [date]
  ...
  TOTALS: [n] topics | [n] signals | [n] contributors | [n] namespaces
```

If `simulations/` is empty or absent, record `{workspace: empty}` and produce all sections with empty state.

---

### CONTRIBUTOR ROSTER

**Entry contract**: No preceding section required — this is the first section.

Rank contributors descending by signal count. Ties broken by topics covered (descending).

```
## Contributor Roster

| Rank | Contributor | Signals | Topics | Namespaces | Last Active |
|------|-------------|---------|--------|-----------|------------|
| 1    | [name]      | [n]     | [n]    | [list]    | [date]     |
```

If no contributor metadata extractable from frontmatter or filename:
`| -- | no contributor metadata found | -- | -- | -- | -- |`

Do not omit this section regardless of workspace state.

**Closing contract: CONTRIBUTOR ROSTER must close before SIGNAL HEALTH opens. No exceptions.**

---

### SIGNAL HEALTH

**Entry contract: CONTRIBUTOR ROSTER must be closed before this section opens. Position: second section — no topic compilation begins until this block is complete.**

Using the artifact table and the Contributor Roster above, evaluate all five stagnation conditions. Add one point per fired condition. Where the Contributor Roster corroborates a fired condition, reference the roster row explicitly.

| Score | Condition | Fires when |
|-------|-----------|-----------|
| +1 | Empty Start | total signals == 0 |
| +1 | Lone Wolf | one contributor >= 80% of total signals (excluding "unknown") |
| +1 | Namespace Tunnel | one namespace >= 70% of total signals |
| +1 | Stale Coverage | most recent artifact >= 14 days before today |
| +1 | Shallow Spread | >= 5 distinct topics each with exactly 1 signal |

Write all fired conditions with evidence. Sum the score. If the Contributor Roster shows a dominant contributor, note it as corroborating evidence for the Lone Wolf condition where applicable.

```
## Signal Health

| Condition | Fires? | Evidence |
|-----------|--------|---------|
| Empty Start | YES / NO | [total signal count, or --] |
| Lone Wolf | YES / NO | [contributor name + % — cite Contributor Roster row if applicable] |
| Namespace Tunnel | YES / NO | [namespace name + % or --] |
| Stale Coverage | YES / NO | [most recent date or --] |
| Shallow Spread | YES / NO | [topic count + single-signal count or --] |

**Health Score: [n]/5**
**Severity Tiers:**
- 0 -> Healthy — no stagnation; deepen and diversify
- 1-2 -> Monitor — early warning; correct within the sprint
- 3-4 -> Alert — degrading signal discipline; intervene now
- 5 -> Critical — signal practice has stalled; escalate immediately

**Current Tier: [Healthy / Monitor / Alert / Critical]**
**Active Conditions: [list of fired condition names, or "none"]**
**What this blocks: [one sentence — which achievement or milestone is most at risk given active conditions]**
```

**Closing contract: SIGNAL HEALTH must close before ACHIEVEMENT LOG opens. No exceptions.**

---

### ACHIEVEMENT LOG

**Entry contract: SIGNAL HEALTH must be closed before this section opens.**

For every topic in the artifact table, evaluate all five achievements. Show earned and locked in separate subsections. State the exact numeric gap for every locked achievement.

Achievement definitions (exact names required — paraphrasing fails):

| Achievement | Earned when |
|-------------|-----------|
| First Signal | signals >= 1 |
| Signal Depth | signals >= 3 |
| Full Sweep | distinct namespaces >= 3 |
| Solo Pioneer | contributors == 1 AND signals >= 1 |
| Team Topic | contributors >= 2, each with >= 1 signal |

```
## Achievement Log

### [topic path]

**Earned**
- [Achievement name] — [evidence: e.g., "3 signals across scout and flow"]

**Locked**
- [Achievement name] — needs [exact gap, e.g., "2 more signals", "1 more namespace"]
```

Every topic from the artifact table must appear. A topic in the artifact table but absent from this section is a log gap.

If workspace was empty: write the section header with "no topics found."

**Closing contract: ACHIEVEMENT LOG must close before MILESTONE CHECK opens. No exceptions.**

---

### MILESTONE CHECK

**Entry contract: ACHIEVEMENT LOG must be closed before this section opens.**

Use exact milestone names. Do not paraphrase or abbreviate.

```
## Milestone Check

| Milestone | Status | Evidence |
|-----------|--------|---------|
| first team signal | EARNED / NOT YET | [path or "none"] |
| shared coverage | EARNED / NOT YET | [topic + contributor count or "none"] |
| debate starter | EARNED / NOT YET | [topic + namespace list or "none"] |
```

---

### 1-AWAY GAPS

**Entry contract: MILESTONE CHECK must be closed before this section opens.**

From locked entries in ACHIEVEMENT LOG and NOT YET milestones in MILESTONE CHECK, list every item exactly 1 unit from being earned:

```
## 1-Away Gaps

- [topic/milestone]: needs [1 more signal / 1 more contributor / 1 more namespace]
  to unlock **[exact Achievement or Milestone name]**
```

If nothing is 1 step away: "No 1-away gaps. Closest: [topic] needs [n] more [unit] for **[Achievement]**."

**Closing contract: 1-AWAY GAPS must close before RECOMMENDED ACTIONS opens. No exceptions.**

---

### RECOMMENDED ACTIONS

**Entry contract: 1-AWAY GAPS must be closed before this section opens.**
**Input: Active Conditions from SIGNAL HEALTH + locked entries from ACHIEVEMENT LOG + NOT YET milestones from MILESTONE CHECK.**

Write at least 3 actions. Each uses this three-field template — all fields required:

```
## Recommended Actions

1. **`{namespace}/{topic}`** — [action description]
   -> Unlocks: **{exact achievement or milestone name}**
   -> Breaks: **{condition name from Signal Health Active Conditions}**
   -> Priority: [Signal Health Current Tier] — score [n]/5

2. ...

3. ...
```

**No action may omit the Breaks field. "N/A" is not valid.** If Signal Health shows no active conditions (score = 0), Breaks writes `prevents: {condition name}` with one-clause prevention rationale.

Order actions by health tier: Alert or Critical tier means address all fired conditions before lower-priority items.

**Closing contract: RECOMMENDED ACTIONS must close before TEAM SYNTHESIS opens. No exceptions.**

---

### TEAM SYNTHESIS

**Entry contract: RECOMMENDED ACTIONS must be closed before this section opens.**

Write one synthesizing sentence visible only from reading across the full output — not from any single topic entry or roster row. Must reference >= 2 topics or contributors, cite >= 1 specific number, and close with a recommended implication.

```
## Team Synthesis

[Synthesizing sentence + recommended implication]
```

---

### WRITE ARTIFACT

`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
health_score: [n]/5
health_tier: [Healthy / Monitor / Alert / Critical]
active_conditions: [list or "none"]
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
---
```
