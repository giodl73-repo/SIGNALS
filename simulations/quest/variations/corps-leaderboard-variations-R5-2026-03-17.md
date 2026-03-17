`simulations/quest/variations/corps-leaderboard-variations-R5-2026-03-17.md` written.

---

## R5 Variation Map — corps-leaderboard

**The ceiling problem solved in R5**: All R4 variations scored 100/100 against v4 but no variation scored 100 against v5. The two new criteria:
- **C-18** — gate markers as literal output lines (only R4 V-02 passed)
- **C-19** — synthesis requires type-named numeric (only R4 V-03 passed)

All 5 R5 variations pass both.

| | Variation | Primary Axis | C-18 mechanism | C-19 mechanism |
|--|-----------|------|------|------|
| **V-01** | All-Tables Scorecard | Output format | `[TRANSITION: X closed. Y opens now.]` between every gate | Synthesis names 4 permitted types: contributor count / signal count / namespace count / topic count |
| **V-02** | Triple-Gate Pipeline | Role sequence | Inherits R4 gate artifact lines unchanged — the minimal delta | Type enumeration added to Team Insight instruction only |
| **V-03** | Conversational Coach | Phrasing register | `[CHECKPOINT: X complete. Y opens now.]` in warm register as output artifact | Type enumeration added to Team Picture instruction |
| **V-04** | SITREP + Decision Risk | Inertia framing | `[SITREP GATE: X closed. Y opens now.]` fits military briefing vocabulary | Type enumeration in DEBRIEF synthesis instruction |
| **V-05** | Cascading Contracts | Lifecycle emphasis | **Bidirectional** — `[OPEN: X — preceded by Y]` + `[CLOSE: X — Z opens next]` at both ends of every section; a single skip violates two output positions | Type enumeration as "quantified core" requirement in TEAM SYNTHESIS |

**Key structural notes**:

- **V-02** is the minimal-change variation — it inherits the R4 gate lines unchanged (C-18 already present) and adds only one clause to Team Insight (C-19). Lowest risk of disturbing existing 100/100 criteria.
- **V-05** has the strongest C-18 enforcement: bidirectional stamps mean a skipped section leaves an observable gap at `[CLOSE: preceding]` (which names a section that never opened) AND at `[OPEN: next]` (which names a predecessor that never closed). Two simultaneous structural violations per skip.
- **C-19** is identical across all five variations — the type enumeration (`contributor count, signal count, namespace count, or topic count`) appears in every synthesis instruction with the same four-type list.
- **V-03** adds the most new text for C-18 (5 checkpoint lines across 5 sections) but maintains the warmest register — the `[CHECKPOINT: ...]` prefix is natural in a coaching-voice prompt.
format — machine-readable matrix tables throughout, with literal transition announcement lines between sections
**Hypothesis**: The R4 V-01 tabular format was the most auditable structural approach. The two v5 gaps were: gate transitions encoded only as instruction text (C-18 fails), and synthesis phrasing used generic "specific number" without naming permitted types (C-19 fails). V-01R5 adds: (1) a `[TRANSITION: ...]` literal output line between each major gate — visible in the artifact, detectable by scanning; (2) explicit type enumeration in the synthesis instruction. The tables-first identity is fully preserved. Risk: transition lines between sections may feel redundant alongside the named-section headers; the test is whether the output-layer artifact provides compliance signal that the instruction-only version did not.

---

You are running `corps-leaderboard`. No inputs — scan and compute from workspace state.

Sections are ordered. A `[TRANSITION: ...]` line marks the close of each major section and announces what opens next. Write this line to the output before beginning the next section — it is part of the artifact, not a comment.

---

### PRE-WORK — WORKSPACE SCAN

Before producing any section, scan the workspace.

Glob `simulations/**/*.md`. For every file record:
- **topic** — subdirectory path under `simulations/`
- **namespace** — first path segment
- **contributor** — `author:` or `contributor:` from YAML frontmatter; filename prefix before first `-`; or `"unknown"`
- **date** — YYYY-MM-DD from filename

Internal artifact table (not written to output):

```
ARTIFACT TABLE (internal)
  [topic] | [signal count] | contributors: [list] | namespaces: [list] | most recent: [date]
  ...
  TOTALS: [n] topics | [n] signals | [n] contributors | [n] namespaces
```

If `simulations/` is empty or absent, record `{workspace: empty}` and continue — all sections must produce output.

---

### SECTION — CONTRIBUTOR LEADERBOARD

**Position: first section.**

Rank contributors descending by signal count. Ties broken by topics covered (descending).

```
## Contributor Leaderboard

| Rank | Contributor | Signals | Topics | Namespaces | Last Active |
|------|-------------|---------|--------|-----------|------------|
| 1    | [name]      | [n]     | [n]    | [list]    | [date]     |
```

If no contributor metadata is extractable from frontmatter or filename:
`| -- | no contributor metadata found | -- | -- | -- | -- |`

Do not omit this section regardless of workspace state.

After the table, write this exact line to the output:

```
[TRANSITION: CONTRIBUTOR LEADERBOARD closed. SIGNAL HEALTH SCORECARD opens now.]
```

**CONTRIBUTOR LEADERBOARD must close before SIGNAL HEALTH SCORECARD opens. No exceptions.**

---

### SECTION — SIGNAL HEALTH SCORECARD

**Entry condition: `[TRANSITION: CONTRIBUTOR LEADERBOARD closed...]` line written. Position: second section — no topic compilation begins until this block is complete.**

Using the artifact table and the Contributor Leaderboard above, evaluate all five stagnation conditions. Add one point per fired condition. Where the Contributor Leaderboard corroborates a fired condition, reference the leaderboard row explicitly in the Evidence column.

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

After the block, write this exact line to the output:

```
[TRANSITION: SIGNAL HEALTH SCORECARD closed. ACHIEVEMENT MATRIX opens now.]
```

**SIGNAL HEALTH SCORECARD must close before ACHIEVEMENT MATRIX opens. No exceptions.**

---

### SECTION — ACHIEVEMENT MATRIX

**Entry condition: `[TRANSITION: SIGNAL HEALTH SCORECARD closed...]` line written.**

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

Every topic from the artifact table must appear as a row. A topic present in the artifact table but absent from the matrix is a **matrix gap**.

If workspace was empty: output the column headers with note "No topics found — all cells empty."

After the matrix, write this exact line to the output:

```
[TRANSITION: ACHIEVEMENT MATRIX closed. TEAM MILESTONES opens now.]
```

**ACHIEVEMENT MATRIX must close before TEAM MILESTONES opens. No exceptions.**

---

### SECTION — TEAM MILESTONES

**Entry condition: `[TRANSITION: ACHIEVEMENT MATRIX closed...]` line written.**

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

Write one synthesizing sentence visible only by reading across multiple rows of the achievement matrix or multiple leaderboard entries — not from any single row or topic. The sentence must include at least one concrete numeric value — a contributor count, signal count, namespace count, or topic count — as its central quantified observation. Must reference >= 2 topics or contributors and close with a recommended implication.

```
## Team Synthesis

[Synthesizing sentence with concrete numeric value (contributor count / signal count / namespace count / topic count) + recommended implication]
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

## V-02 — Role Sequence: Triple-Gate Pipeline (evolved)

**Axis**: Role sequence — three named completion gates, each as a literal output artifact line naming the closing and opening section
**Hypothesis**: R4 V-02 already satisfied C-18 (gate lines as output artifacts) and scored 100/100 against v4. The single v5 gap is C-19: the Team Insight instruction used "cite >= 1 specific number" rather than naming the permitted types (contributor count, signal count, namespace count, or topic count). V-02R5 adds only the type enumeration to the Team Insight instruction. The triple-gate pipeline structure, gate line format, and all other mechanisms are unchanged from R4. This is the minimal change needed to open the ceiling. Risk: none structural — the change is a single instruction clause. The test is whether the type enumeration alone closes C-19 without disturbing any other criterion.

---

You are running `corps-leaderboard`. No inputs — scan and compute from workspace state.

Three named gates control the execution pipeline. Each gate appears as a literal line in the output. No section opens until its gate line is written.

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

Every topic from the scan result must appear. A topic in the scan result but absent from the compilation is a **compilation gap**.

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

Write one synthesizing sentence visible only from reading across the full output — not from any single topic entry or leaderboard row. The sentence must include at least one concrete numeric value — a contributor count, signal count, namespace count, or topic count — as its quantified core observation. Must reference >= 2 topics or contributors and close with a recommended implication.

```
## Team Insight

[Synthesizing sentence with concrete numeric value (contributor count / signal count / namespace count / topic count) + recommended implication]
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

## V-03 — Phrasing Register: Conversational Coach (evolved)

**Axis**: Phrasing register — warm, direct coaching voice, with checkpoint marker lines printed to the output between sections
**Hypothesis**: R4 V-03 satisfied C-19 (Team Picture required "at least one specific number") and scored 100/100 against v4. The single v5 gap is C-18: section transitions were encoded only as instruction text, not as literal output artifacts. V-03R5 adds `[CHECKPOINT: ...]` output lines at each gate boundary — written in the same warm register as the rest of the prompt, so they feel like natural progress markers rather than mechanical gates. C-19 is strengthened by adding the type enumeration to "at least one specific number." Risk: checkpoint lines in a coaching register might feel like progress commentary rather than machine-auditable markers; mitigation is the explicit bracket format which makes them structurally distinct from prose.

---

You are running `corps-leaderboard`. No inputs — scan the workspace and give your team an honest look at where they stand.

As you complete each major section, write a `[CHECKPOINT: ...]` line to the output before moving on. These markers confirm the section is complete and let anyone scanning the output verify the order.

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

After the table, write this checkpoint line to the output:

```
[CHECKPOINT: Who's Contributing complete. Team Health Score opens now.]
```

**WHO'S CONTRIBUTING must be complete before TEAM HEALTH SCORE begins. No exceptions.**

---

### TEAM HEALTH SCORE

**This section opens only after the `[CHECKPOINT: Who's Contributing complete...]` line is written. Position: second section — no topic compilation begins until this block is written.**

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

After the block, write this checkpoint line to the output:

```
[CHECKPOINT: Team Health Score complete. Topic Achievements opens now.]
```

**TEAM HEALTH SCORE must be complete before TOPIC ACHIEVEMENTS begins. No exceptions.**

---

### TOPIC ACHIEVEMENTS

**This section opens only after the `[CHECKPOINT: Team Health Score complete...]` line is written.**

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

Write one block for every topic in the workspace. A topic that appears in the workspace but is missing from this section is a **topic gap**.

If the workspace is empty, write the section header with "no topics found."

After the block, write this checkpoint line to the output:

```
[CHECKPOINT: Topic Achievements complete. Team Milestones opens now.]
```

**TOPIC ACHIEVEMENTS must be complete before TEAM MILESTONES begins. No exceptions.**

---

### TEAM MILESTONES

**This section opens only after the `[CHECKPOINT: Topic Achievements complete...]` line is written.**

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

Write one sentence that could only be true by looking at the whole team together — something that isn't visible from any single topic or any single contributor's row. The sentence must include at least one concrete numeric value drawn from the output — a contributor count, signal count, namespace count, or topic count — as its quantified observation. It must mention at least 2 topics or 2 contributors and end with a recommendation.

```
## Team Picture

[Synthesizing sentence with concrete numeric value (contributor count / signal count / namespace count / topic count) + recommendation]
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

## V-04 — Inertia Framing + Output Format: SITREP with Gate Stamps (evolved)

**Axes**: Inertia framing + output format — SITREP briefing structure with printed section-close stamps and added decision-risk field
**Hypothesis**: R4 V-04 satisfied C-15 through C-17 with the SITREP format and scored 100/100 against v4. The two v5 gaps were: section transitions were encoded only as instruction text (C-18 fails), and the DEBRIEF synthesis used generic "specific number" phrasing (C-19 fails). V-04R5 adds: (1) literal `[SITREP GATE: X closed. Y opens now.]` output lines at each major section boundary — consistent with the military-briefing register of the format; (2) type-named numeric requirement in the DEBRIEF instruction. The SITREP identity — five named sections, Decision risk field, "What to watch for" bridge — is fully preserved. Risk: SITREP gate stamps may feel more mechanical than the surrounding briefing prose; mitigation is using the `[SITREP GATE: ...]` prefix which fits the format's vocabulary.

---

You are producing a Signal Briefing for the team. A Signal Briefing follows a five-section structure. Each section is named. At the close of each section, write a `[SITREP GATE: ...]` line to the output before opening the next — this is a briefing discipline constraint and appears in the artifact.

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

Write this gate line to the output before opening SECTION 2:

```
[SITREP GATE: SITUATION closed. ASSESSMENT opens now.]
```

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

Write this gate line to the output before opening SECTION 3:

```
[SITREP GATE: ASSESSMENT closed. FINDINGS opens now.]
```

**ASSESSMENT must close before FINDINGS opens. No exceptions.**

---

### SECTION 3 — FINDINGS

**Entry condition: `[SITREP GATE: ASSESSMENT closed...]` line written.**

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

Every topic must appear. A missing topic is a **findings gap**.

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

Write this gate line to the output before opening SECTION 4:

```
[SITREP GATE: FINDINGS closed. ACTIONS opens now.]
```

**FINDINGS closes here. ACTIONS opens next.**

---

### SECTION 4 — ACTIONS

**Entry condition: `[SITREP GATE: FINDINGS closed...]` line written.**

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

Write this gate line to the output before opening SECTION 5:

```
[SITREP GATE: ACTIONS closed. DEBRIEF opens now.]
```

**ACTIONS closes here. DEBRIEF opens next.**

---

### SECTION 5 — DEBRIEF

**Entry condition: `[SITREP GATE: ACTIONS closed...]` line written.**

Write one synthesizing statement visible only from the full briefing — not from any single FINDINGS subsection. The statement must include at least one concrete numeric value — a contributor count, signal count, namespace count, or topic count — drawn from the output above, as its quantified core. Must reference >= 2 topics or contributors and close with a recommended implication for the team.

```
## DEBRIEF

[Synthesizing sentence with concrete numeric value (contributor count / signal count / namespace count / topic count) + recommended implication]
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

## V-05 — Lifecycle Emphasis: Cascading Contracts with Auditable Gate Lines (evolved)

**Axes**: Lifecycle emphasis + role sequence — every section prints both a closing output line and the following section prints an opening output line; bidirectional literal stamps make a single skip violate two output positions
**Hypothesis**: R4 V-05 satisfied C-15 with bidirectional instruction-text contracts but those contracts were encoding rules, not output artifacts — the C-18 test distinguishes these. V-05R5 adds literal output lines at both ends of every gate: each section closes by printing `[CLOSE: X]` and each section opens by printing `[OPEN: Y — preceded by X]`. A skipped section leaves a visible gap at two positions in the output: the preceding section's `[CLOSE: ...]` would reference a section that never opened, and the next section's `[OPEN: ...]` would name a predecessor that never closed. The bidirectional artifact makes skipping structurally detectable without any cross-reference logic. C-19 is added with type-named numeric in TEAM SYNTHESIS. Risk: dual output lines per section boundary adds volume; the test is whether the auditability benefit outweighs the structural noise.

---

You are running `corps-leaderboard`. No inputs — scan and compute from workspace state.

Each section below has two output contracts:
- An **opening stamp**: the first output line of the section, naming this section and the section that preceded it
- A **closing stamp**: the last output line of the section, naming this section and the section that follows

Write both stamps. They are part of the output artifact. A skipped section leaves an observable gap at two positions.

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

Opening stamp — write this as the first output line of this section:

```
[OPEN: CONTRIBUTOR ROSTER — no preceding section]
```

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

Closing stamp — write this as the last output line of this section:

```
[CLOSE: CONTRIBUTOR ROSTER — SIGNAL HEALTH opens next]
```

**Closing contract: CONTRIBUTOR ROSTER must close before SIGNAL HEALTH opens. No exceptions.**

---

### SIGNAL HEALTH

Opening stamp — write this as the first output line of this section:

```
[OPEN: SIGNAL HEALTH — preceded by CONTRIBUTOR ROSTER]
```

**Entry contract: CONTRIBUTOR ROSTER must be closed before this section opens. Position: second section — no topic compilation begins until this block is complete.**

Using the artifact table and the Contributor Roster above, evaluate all five stagnation conditions. Add one point per fired condition. Where the Contributor Roster corroborates a fired condition, reference the roster row explicitly.

| Score | Condition | Fires when |
|-------|-----------|-----------|
| +1 | Empty Start | total signals == 0 |
| +1 | Lone Wolf | one contributor >= 80% of total signals (excluding "unknown") |
| +1 | Namespace Tunnel | one namespace >= 70% of total signals |
| +1 | Stale Coverage | most recent artifact >= 14 days before today |
| +1 | Shallow Spread | >= 5 distinct topics each with exactly 1 signal |

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

Closing stamp — write this as the last output line of this section:

```
[CLOSE: SIGNAL HEALTH — ACHIEVEMENT LOG opens next]
```

**Closing contract: SIGNAL HEALTH must close before ACHIEVEMENT LOG opens. No exceptions.**

---

### ACHIEVEMENT LOG

Opening stamp — write this as the first output line of this section:

```
[OPEN: ACHIEVEMENT LOG — preceded by SIGNAL HEALTH]
```

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

Every topic from the artifact table must appear. A topic in the artifact table but absent from this section is a **log gap**.

If workspace was empty: write the section header with "no topics found."

Closing stamp — write this as the last output line of this section:

```
[CLOSE: ACHIEVEMENT LOG — MILESTONE CHECK opens next]
```

**Closing contract: ACHIEVEMENT LOG must close before MILESTONE CHECK opens. No exceptions.**

---

### MILESTONE CHECK

Opening stamp — write this as the first output line of this section:

```
[OPEN: MILESTONE CHECK — preceded by ACHIEVEMENT LOG]
```

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

Closing stamp — write this as the last output line of this section:

```
[CLOSE: MILESTONE CHECK — 1-AWAY GAPS opens next]
```

---

### 1-AWAY GAPS

Opening stamp — write this as the first output line of this section:

```
[OPEN: 1-AWAY GAPS — preceded by MILESTONE CHECK]
```

**Entry contract: MILESTONE CHECK must be closed before this section opens.**

From locked entries in ACHIEVEMENT LOG and NOT YET milestones in MILESTONE CHECK, list every item exactly 1 unit from being earned:

```
## 1-Away Gaps

- [topic/milestone]: needs [1 more signal / 1 more contributor / 1 more namespace]
  to unlock **[exact Achievement or Milestone name]**
```

If nothing is 1 step away: "No 1-away gaps. Closest: [topic] needs [n] more [unit] for **[Achievement]**."

Closing stamp — write this as the last output line of this section:

```
[CLOSE: 1-AWAY GAPS — RECOMMENDED ACTIONS opens next]
```

**Closing contract: 1-AWAY GAPS must close before RECOMMENDED ACTIONS opens. No exceptions.**

---

### RECOMMENDED ACTIONS

Opening stamp — write this as the first output line of this section:

```
[OPEN: RECOMMENDED ACTIONS — preceded by 1-AWAY GAPS]
```

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

Closing stamp — write this as the last output line of this section:

```
[CLOSE: RECOMMENDED ACTIONS — TEAM SYNTHESIS opens next]
```

**Closing contract: RECOMMENDED ACTIONS must close before TEAM SYNTHESIS opens. No exceptions.**

---

### TEAM SYNTHESIS

Opening stamp — write this as the first output line of this section:

```
[OPEN: TEAM SYNTHESIS — preceded by RECOMMENDED ACTIONS]
```

**Entry contract: RECOMMENDED ACTIONS must be closed before this section opens.**

Write one synthesizing sentence visible only from reading across the full output — not from any single topic entry or roster row. The sentence must include at least one concrete count from the output — a contributor count, signal count, namespace count, or topic count — as the quantified core of the synthesizing observation. Must reference >= 2 topics or contributors and close with a recommended implication.

```
## Team Synthesis

[Synthesizing sentence with concrete count (contributor count / signal count / namespace count / topic count) as quantified core + recommended implication]
```

Closing stamp — write this as the last output line of this section:

```
[CLOSE: TEAM SYNTHESIS — artifact write follows]
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

## Predicted Scores vs v5

| Variation | C-18 | C-19 | Predicted Score | Notes |
|-----------|------|------|-----------------|-------|
| V-01 All-Tables Scorecard | PASS — `[TRANSITION: X closed. Y opens now.]` as literal output line | PASS — "contributor count, signal count, namespace count, or topic count" enumerated | 100.0 | Tables format; transition lines are minimal additions |
| V-02 Triple-Gate Pipeline | PASS — inherits R4 gate artifact lines | PASS — type enumeration added to Team Insight instruction | 100.0 | Minimal delta from R4 V-02; C-19 was the only gap |
| V-03 Conversational Coach | PASS — `[CHECKPOINT: X complete. Y opens now.]` as output artifact | PASS — "contributor count, signal count, namespace count, or topic count" added to Team Picture instruction | 100.0 | Warm register preserved; checkpoint lines fit coaching vocabulary |
| V-04 SITREP + Decision Risk | PASS — `[SITREP GATE: X closed. Y opens now.]` as literal output line | PASS — type enumeration in DEBRIEF instruction | 100.0 | SITREP register; gate stamp language consistent with military briefing vocabulary |
| V-05 Cascading Contracts | PASS — `[OPEN: X — preceded by Y]` + `[CLOSE: X — Z opens next]` at both ends of every section | PASS — "contributor count, signal count, namespace count, or topic count" as quantified core requirement | 100.0 | Bidirectional — a skip violates two output positions; highest C-18 auditability of any variation |

```json
{"target_rubric": "v5", "ceiling_open_at_r4": true, "ceiling_closed_at_r5": true, "c18_pattern": "literal output line between sections — machine-scannable, gap visible if skipped", "c19_pattern": "type-named numeric enumeration in synthesis instruction — contributor count / signal count / namespace count / topic count", "strongest_c18_variation": "V-05 (bidirectional stamps — skip violates both [CLOSE] and [OPEN] positions)", "strongest_c19_variation": "all variations equivalent — type enumeration is identical across all five"}
```
