---
skill: quest-variate
skill_target: corps-leaderboard
round: 7
date: 2026-03-17
rubric_version: 7
---

# Variate R7 — corps-leaderboard

5 complete prompt body variations for the `corps-leaderboard` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

**R6 ceiling**: All five R6 variations scored 100/100 against v6. Against v7: V-02 and V-04
scored ~99.33 (pass C-23, fail C-22); V-05 scored ~99.33 (pass C-22, fail C-23); V-01 and V-03
scored ~98.67 (fail both). The v7 ceiling is open — no variation yet passes both C-22 and C-23.

**R7 design target**: Embed BOTH C-22 (dual-statement `prevents:` rule) AND C-23 (two-level
nearest-miss cascade) in all five variations while carrying C-01–C-21 coverage forward. Every
variation should reach 100 against v7.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Output format (structured pre-write decision table as primary format for action section) | V-01, V-04 |
| Phrasing register (MUST/SHALL/WHEN formal modal spec) | V-02, V-04 |
| Lifecycle emphasis (forward-only phase gates, each gated by prior completion) | V-03 |
| Role sequence (4-role pipeline: Archaeologist → Health Analyst → Compiler → Narrator) | V-04 |
| Inertia framing (cost-of-inertia named before actions; skeptic role before compiler) | V-05 |

---

## V-01 — Output Format: Decision-Table Layout Throughout

**Axis**: Output format
**Hypothesis**: Expressing the action section as a two-stage decision-table workflow (pre-write
lookup table first, then action table) makes C-22 structurally unavoidable: the pre-write table
is an independent output construct, not a parenthetical note, and the action table restates the
`prevents:` rule in its column header definition. The two-level cascade (C-23) is expressed as
two mandatory rows appended to the 1-away table when empty — the row format constrains the model
to supply both levels rather than choosing one. Risk: action rows in a table may elide the
rationale sentence. Mitigation: a required "Why" column holds one sentence per action.

---

You are running `corps-leaderboard`. No arguments needed — scan and compute from workspace state.

---

### Phase 1 — Scan

Glob `simulations/**/*.md`. For every `.md` file discovered:

- Record its topic path (subdirectory under `simulations/`, e.g., `scout/competitors`)
- Record the namespace (first path segment)
- Extract contributor identity from frontmatter `author:` or `contributor:` fields, or from
  filename prefix conventions (name before the first `-` in the filename)
- Note any detectable date field

Build an internal registry:

```
REGISTRY (internal)
  topics: [unique topic paths, deduplicated]
  per topic: { file_count, contributor_set, namespace_set }
  contributors_all: [deduplicated across all topics]
  namespaces_active: [deduplicated list]
  total_signals: [n]
```

Gate line (emit as literal output):
```
SCAN GATE: [n] signals across [n] topics — [n or "unknown"] contributors — [n] namespaces active. Registry complete.
```

If `simulations/` is empty or absent, emit:
```
SCAN GATE: workspace empty — 0 signals, 0 topics. All achievement and milestone sections will show empty or NOT YET. Proceeding with empty registry.
```

---

### Phase 2 — Contributor Leaderboard

Rank all contributors descending by total signals. Ties broken by topics covered.

```
## Contributor Leaderboard — {{date}}

| Rank | Contributor | Total Signals | Topics Covered | Namespaces Active |
|------|-------------|---------------|----------------|-------------------|
| 1    | [name]      | [n]           | [n]            | [list]            |
```

If contributor metadata is not extractable (no `author:`/`contributor:` fields, no parseable
filename prefixes), emit one explicit row:

`| — | (no contributor metadata found) | — | — | — |`

Do not omit this section under any workspace state.

After the table, one observation sentence comparing across rows (not a restatement of a single row).

Gate line:
```
LEADERBOARD GATE: [n] contributors ranked. Attribution: [source or "not available"]. Proceeding to Phase 3.
```

---

### Phase 3 — Signal Health Score

Evaluate all 5 stagnation conditions. Score each 0–3 (0 = absent, 1 = emerging, 2 = active,
3 = dominant). Assign urgency by score: 0 = LOW, 1 = MED, 2–3 = HIGH.

| Condition | Score (0–3) | Urgency | Evidence |
|-----------|-------------|---------|----------|
| Empty Start | [0–3] | [LOW/MED/HIGH] | [evidence or "—"] |
| Lone Wolf | [0–3] | [LOW/MED/HIGH] | [evidence or "—"] |
| Namespace Tunnel | [0–3] | [LOW/MED/HIGH] | [evidence or "—"] |
| Stale Coverage | [0–3] | [LOW/MED/HIGH] | [evidence or "—"] |
| Shallow Spread | [0–3] | [LOW/MED/HIGH] | [evidence or "—"] |

**Dominant condition**: [name of highest-scoring condition, or "none" if all score 0]

Condition definitions:
- **Empty Start** — workspace has 0 signals or 0 topics
- **Lone Wolf** — one contributor accounts for > 60% of all signals
- **Namespace Tunnel** — signals concentrated in <= 2 distinct namespaces across all topics
- **Stale Coverage** — all signals are > 90 days old (or no date field detectable, assume unknown)
- **Shallow Spread** — >= 3 topics present but none has reached Signal Depth (3+ signals)

N/A is not a valid score value. If evidence is unavailable, score 0 and note "insufficient data."

Gate line:
```
HEALTH GATE: dominant condition = [name or "none"] — urgency = [LOW/MED/HIGH]. Proceeding to Phase 4 (achievements).
```

---

### Phase 4 — Achievement Evaluation

For each topic in the registry, evaluate all 5 achievements:

| Achievement | Condition |
|-------------|-----------|
| First Signal | file_count >= 1 |
| Signal Depth | file_count >= 3 |
| Full Sweep | namespace_set size >= 3 |
| Solo Pioneer | contributor_set size == 1 AND file_count >= 1 |
| Team Topic | contributor_set size >= 2, each contributor has >= 1 signal |

Output as two sections — earned and locked — within each topic:

```
## Achievements by Topic

### Earned ✓
**[topic path]** ([n] signals)
  ✓ First Signal — [file count] signal(s)
  ✓ [any other earned achievement] — [evidence]

### Locked ○
**[topic path]** ([n] signals)
  ○ Signal Depth — needs [n] more signal(s)
  ○ [any other locked achievement] — needs [specific gap]
```

Every topic from the scan must appear in one or both sections. No topic may be omitted silently.
If `simulations/` was empty, write both sections as empty with note: "(no topics to evaluate)."

Gate line:
```
ACHIEVEMENTS GATE: [n] topics evaluated — [n] achievements earned — [n] locked. Proceeding to Phase 5.
```

---

### Phase 5 — Team Milestones

Evaluate and report the three team milestones using their exact names as shown here.
Do not rename, abbreviate, or paraphrase any milestone name.

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|----------|
| first team signal | EARNED / NOT YET | [file path, or "(none found)"] |
| shared coverage | EARNED / NOT YET | [contributor names + topic counts, or "(none found)"] |
| debate starter | EARNED / NOT YET | [topic path + namespace list, or "(none found)"] |
```

Milestone definitions:
- **first team signal** — any signal file exists in `simulations/`
- **shared coverage** — >= 2 contributors each present in >= 2 distinct topic paths
- **debate starter** — >= 1 topic has signals from >= 2 distinct namespaces

For any NOT YET milestone, append one sentence: what must happen to earn it.

Gate line:
```
MILESTONES GATE: [n/3] milestones earned (first team signal: [E/N], shared coverage: [E/N], debate starter: [E/N]). Proceeding to Phase 6.
```

---

### Phase 6 — 1-Away Gap Detection

Scan every achievement and milestone for gaps of exactly 1 unit (1 more signal, 1 more
contributor, or 1 more namespace).

```
## 1-Away Gaps

| Topic / Milestone | Gap | Unlocks |
|-------------------|-----|---------|
| [topic path] | needs 1 more [signal / contributor / namespace] | **[Achievement name]** |
```

If no gaps are within 1 unit of any threshold, the table must still be present with two
mandatory fallback rows:

```
| Topic / Milestone | Gap | Unlocks |
|-------------------|-----|---------|
| Level 1 — closest to 1-away: [specific topic or milestone name] | needs [n] more [unit] | **[Achievement]** |
| Level 2 — closest to 2-away: [specific topic or milestone name] | needs [n] more [unit] | **[Achievement]** |
```

Both Level 1 and Level 2 rows are required when the 1-away list is empty. Each must name a
specific topic or milestone (not a category) and a specific numeric step count. "No 1-away
gaps found" alone does not satisfy this section.

Gate line:
```
GAPS GATE: [n] 1-away gaps identified (or: 0 gaps — Level 1 and Level 2 fallback rows written). Proceeding to Phase 7.
```

---

### Phase 7 — Next Actions

**Pre-write check — consult this table before writing each Breaks field value:**

| Health condition score from Phase 3 | Breaks field value to write |
|--------------------------------------|-----------------------------|
| score >= 1 (condition active) | [condition name] — [one phrase: what this action dissolves] |
| score = 0 (condition already resolved) | prevents: [condition name] — [re-entry rationale: why this action keeps the condition from returning] |

Do not write N/A in the Breaks field under any circumstances.

Write at least 3 recommended next actions using this template for each:

```
**Action**: [namespace/topic path — specific verb phrase]
**Unlocks**: [exact achievement or milestone name from defined set]
**Breaks**: [determined by pre-write check above:
  — if condition score >= 1: condition name — what it dissolves
  — if condition score = 0: prevents: condition name — re-entry rationale]
**Why**: [one sentence grounded in Phase 4 or Phase 5 gap data]
```

Generic advice ("add more signals", "increase coverage") without a specific namespace and
topic fails. Every action must name a namespace (e.g., `scout`, `flow`, `trace`) and topic
(e.g., `scout/competitors`).

---

### Phase 8 — Team Insight

Write one sentence that draws a cross-topic or cross-contributor conclusion not visible from any
single-topic row in Phase 4. Include at least one concrete number and one specific name (topic
or contributor). Close with a recommended implication for the team.

---

### Phase 9 — Write Artifact

Write the complete output (Phases 1–8) to:
`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
dominant_health_condition: [name or "none"]
---
```

---

## V-02 — Phrasing Register: Formal MUST/SHALL/WHEN Modal Spec

**Axis**: Phrasing register
**Hypothesis**: Encoding every behavioral requirement as a MUST/SHALL/WHEN clause makes each
criterion independently keyword-auditable: C-22 becomes two independently-located MUST clauses
(one in the pre-write check definition, one in the action template body), C-23 becomes a
WHEN/THEN conditional that names Level 1 and Level 2 as separate MUST items. The formal
register minimizes ambiguity between instructions and examples. Risk: formal prose is less
engaging for a team audience; the tool is used weekly, so the dry register is acceptable for
a workflow artifact.

---

You are running `corps-leaderboard`. No arguments. You MUST scan and compute from workspace state.

---

**Requirement 1 — Signal Registry**

The skill MUST glob `simulations/**/*.md` and build a structured registry. For each file, the
registry MUST record: topic path (subdirectory under `simulations/`), namespace (first path
segment), contributor identity (from frontmatter `author:` / `contributor:` fields or filename
prefix), and file count per topic. The registry MUST deduplicate contributors and namespaces
across topics.

The skill MUST handle the empty-workspace case explicitly. WHEN `simulations/` is absent or
contains no `.md` files, the skill MUST emit:

```
SCAN GATE: workspace empty — 0 signals detected. All sections proceed with empty state.
```

WHEN signals exist, the skill MUST emit:
```
SCAN GATE: [n] signals — [n] topics — [n] namespaces — [n or "unknown"] contributors. Registry built.
```

---

**Requirement 2 — Contributor Leaderboard**

The skill MUST produce a contributor leaderboard table. The table MUST be ranked in descending
order by total signals. Ties MUST be broken by topics covered.

Required columns: Rank | Contributor | Total Signals | Topics Covered | Namespaces Active.

WHEN contributor metadata is not extractable from any frontmatter field or filename pattern,
the skill MUST emit one explicit row:
`| — | (no contributor metadata found) | — | — | — |`

The leaderboard section MUST NOT be omitted regardless of workspace state.

The skill MUST follow the leaderboard table with one observation sentence comparing across
rows. The sentence MUST NOT restate a single-row value — it MUST draw a cross-row comparison.

The skill MUST emit:
```
LEADERBOARD GATE: [n] contributors ranked. Source: [frontmatter / filename / not available]. Proceeding.
```

---

**Requirement 3 — Signal Health Score**

The skill MUST evaluate all 5 stagnation conditions. Each condition MUST be scored 0–3.
Urgency tiers MUST be assigned as follows: score 0 = LOW, score 1 = MED, score 2–3 = HIGH.
N/A MUST NOT appear as a score value.

The 5 conditions MUST be named exactly as listed:
- **Empty Start** — 0 signals anywhere in workspace
- **Lone Wolf** — one contributor > 60% of all signals
- **Namespace Tunnel** — signals in <= 2 namespaces across all topics
- **Stale Coverage** — all signals older than 90 days (or date undetectable: score 0, note "date undetectable")
- **Shallow Spread** — >= 3 topics with file_count < 3

The skill MUST name the dominant condition (highest-scoring). WHEN all conditions score 0,
the skill MUST write: "dominant condition: none."

The skill MUST emit:
```
HEALTH GATE: dominant = [name or "none"] | urgency = [LOW/MED/HIGH]. Health section closed. Proceeding to achievements.
```

---

**Requirement 4 — Achievement Evaluation**

The skill MUST evaluate all 5 achievements for every discovered topic. The 5 achievement names
are fixed and MUST NOT be renamed, abbreviated, or paraphrased:

- **First Signal** — file_count >= 1
- **Signal Depth** — file_count >= 3
- **Full Sweep** — topic's namespace_set size >= 3
- **Solo Pioneer** — contributor_set size == 1 AND file_count >= 1
- **Team Topic** — contributor_set size >= 2, each contributor with >= 1 signal

For each topic, the skill MUST produce an Earned list and a Locked list. Every topic from the
registry MUST appear in the output. A topic present in the registry but absent from the
achievement section is a spec gap.

The skill MUST separate earned achievements from locked achievements per topic. WHEN a topic
has no earned achievements, the Earned list MUST read "none" — the topic row MUST NOT be omitted.

The skill MUST emit:
```
ACHIEVEMENTS GATE: [n] topics evaluated — [n] earned — [n] locked. Proceeding to milestones.
```

---

**Requirement 5 — Team Milestones**

The skill MUST report all three team milestones. The milestone names are fixed and MUST NOT be
renamed, abbreviated, or paraphrased:

- **first team signal**
- **shared coverage**
- **debate starter**

For each milestone, the skill MUST produce: status (EARNED or NOT YET), evidence (file path,
contributor names, or namespace list), and — WHEN NOT YET — one sentence stating exactly what
must happen to earn it.

WHEN the workspace is empty, all three milestones MUST show NOT YET with "workspace is empty"
as evidence.

The skill MUST emit:
```
MILESTONES GATE: [n/3] milestones earned. Proceeding to 1-away gaps.
```

---

**Requirement 6 — 1-Away Gap Detection**

The skill MUST identify every achievement or milestone gap of exactly 1 unit. Each gap entry
MUST name the specific topic or milestone, the exact gap count and unit, and the exact achievement
or milestone name it unlocks.

WHEN 1-away gaps exist, the skill MUST list each as:
`- [topic / milestone]: needs 1 more [signal / contributor / namespace] → unlocks **[Achievement name]**`

WHEN no 1-away gaps exist, the skill MUST output two cascade levels. Both levels are required:

```
No 1-away gaps found.
Level 1 — Closest to 1-away threshold: [specific topic or milestone name] needs [n] more [unit] to unlock **[Achievement]**.
Level 2 — Closest to 2-away threshold: [specific topic or milestone name] needs [n] more [unit] to unlock **[Achievement]**.
```

The Level 1 and Level 2 statements are not optional. Each MUST name a specific topic or
milestone (not a category) and a specific numeric step count. An absence statement without
both levels fails this requirement.

The skill MUST emit:
```
GAPS GATE: [n] 1-away gaps (or: 0 gaps — Level 1 and Level 2 cascade written). Proceeding to actions.
```

---

**Requirement 7 — Recommended Next Actions**

Before writing any action, the skill MUST consult this pre-write decision table to determine
the correct Breaks field value:

```
Pre-write check — Breaks field:
  WHEN health condition score >= 1 (condition is active):
    WRITE: [condition name] — [what this action dissolves]
  WHEN health condition score = 0 (condition is already resolved):
    WRITE: prevents: [condition name] — [re-entry rationale]
  N/A MUST NOT appear in the Breaks field.
```

The skill MUST write at least 3 recommended actions. Each action MUST use this three-field template:

```
**Action**: [specific namespace and topic — exact verb phrase]
**Unlocks**: [exact achievement or milestone name]
**Breaks**: [WHEN score >= 1: condition name — what it dissolves |
           WHEN score = 0: prevents: condition name — re-entry rationale]
**Why**: [one sentence grounded in Requirement 4 or Requirement 5 gap data]
```

The `prevents:` prefix MUST appear in the Breaks field WHEN the targeted health condition
scores 0. A Breaks value that names a condition without the `prevents:` prefix WHEN score = 0
fails this requirement.

Generic advice ("add signals", "improve coverage") without a specific namespace and topic MUST NOT appear.

The skill MUST emit:
```
ACTIONS GATE: [n] actions written. Prevents: prefix used for [n] zero-score conditions.
```

---

**Requirement 8 — Team Synthesis**

The skill MUST produce one synthesis sentence. The sentence MUST:
1. Draw a conclusion spanning >= 2 topics or contributors (not a per-topic statistic)
2. Include at least one concrete number from: contributor count, signal count, namespace count,
   or topic count
3. Close with a recommended implication for the team

---

**Requirement 9 — Write Artifact**

The skill MUST write the complete output to:
`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
topics_scanned: [n]
milestones_earned: [n]/3
dominant_health_condition: [name or "none"]
contributors_detected: [n or "unknown"]
---
```

The skill MUST emit a completion gate:
```
COMPLETION GATE: artifact written — [n] topics — [n/3] milestones — [n] actions — dominant: [condition].
```

---

## V-03 — Lifecycle Emphasis: Strict Forward-Only Phase Gates

**Axis**: Lifecycle emphasis
**Hypothesis**: A strict forward-only gate structure — each phase is a named gate that must
be confirmed before the next phase opens — forces completeness by construction. Phases cannot
be skipped because each phase's output is named as the entry condition of the next. C-22 is
addressed by requiring the pre-write check table to produce a decision before the action
template is reached — the two locations (check table and template definition) are structurally
upstream of each other in the gate chain. C-23 is addressed by a PHASE 6 gate that cannot
close unless both Level 1 and Level 2 are written.

---

You are running `corps-leaderboard`. Proceed through phases in strict order.
Do not open a phase until its entry condition is satisfied.
State the gate confirmation text before advancing to each new phase.

---

### PHASE 1 — SIGNAL SCAN

**Entry condition**: None. Phase 1 is always the starting phase.

Glob `simulations/**/*.md`. Build an internal registry:

```
REGISTRY:
  topics: [unique subdirectory paths under simulations/]
  per topic: { file_count, contributor_set, namespace_set }
  contributors_all: [deduplicated]
  namespaces_active: [deduplicated]
  total_signals: [n]
```

Contributor identity: extracted from frontmatter `author:` or `contributor:` fields, or from
filename prefix (the string before the first `-` in the base filename, if it matches a name pattern).

WHEN `simulations/` is absent or empty:
- Set total_signals = 0, topics = [], contributors_all = [], namespaces_active = []
- Proceed normally; all downstream phases produce empty or NOT YET output

**Gate**: State before Phase 2 opens:
```
[PHASE 1 CLOSED: [n] signals — [n] topics — [n] namespaces — [n or "unknown"] contributors]
[PHASE 2 OPENS: contributor leaderboard]
```

---

### PHASE 2 — CONTRIBUTOR LEADERBOARD

**Entry condition**: PHASE 1 gate confirmed.

Rank all registry contributors by total signals descending. Ties broken by topics covered count.

```
## Contributor Leaderboard — {{date}}

| Rank | Contributor | Total Signals | Topics Covered | Namespaces Active |
|------|-------------|---------------|----------------|-------------------|
```

WHEN contributor metadata is not extractable: one row — `| — | (no contributor metadata found) | — | — | — |`

After the table: one cross-row observation sentence (not a restatement of a single cell).

**Gate**: State before Phase 3 opens:
```
[PHASE 2 CLOSED: leaderboard — [n] contributors ranked]
[PHASE 3 OPENS: signal health score]
```

---

### PHASE 3 — SIGNAL HEALTH SCORE

**Entry condition**: PHASE 2 gate confirmed.

Score each of the 5 stagnation conditions 0–3. Urgency: 0 = LOW, 1 = MED, 2–3 = HIGH.
N/A is not a valid score.

| Condition | Score | Urgency | Evidence |
|-----------|-------|---------|----------|
| Empty Start | | | |
| Lone Wolf | | | |
| Namespace Tunnel | | | |
| Stale Coverage | | | |
| Shallow Spread | | | |

Name the dominant condition (highest score). If multiple conditions share the highest score,
list all. If all score 0, state: "no dominant condition."

**Gate**: State before Phase 4 opens:
```
[PHASE 3 CLOSED: health — dominant = [name or "none"] — [LOW/MED/HIGH] urgency]
[PHASE 4 OPENS: per-topic achievements]
```

---

### PHASE 4 — ACHIEVEMENT EVALUATION

**Entry condition**: PHASE 3 gate confirmed. Health score must have been produced and a
dominant condition named (or "none") before achievement evaluation opens.

For each topic in the REGISTRY, evaluate all 5 achievements:

- **First Signal**: file_count >= 1
- **Signal Depth**: file_count >= 3
- **Full Sweep**: namespace_set size >= 3
- **Solo Pioneer**: contributor_set size == 1 AND file_count >= 1
- **Team Topic**: contributor_set size >= 2, each with >= 1 signal

```
## Achievements by Topic

### Earned
**[topic path]** ([n] signals)
  ✓ [Achievement name] — [evidence]

### Locked
**[topic path]** ([n] signals)
  ○ [Achievement name] — needs [specific gap]
```

Every topic from the REGISTRY must appear in one or both groups. A missing topic is a PHASE 4
gate failure — do not advance to PHASE 5 if any topic is absent.

**Gate**: State before Phase 5 opens:
```
[PHASE 4 CLOSED: achievements — [n] topics evaluated — [n] earned — [n] locked]
[PHASE 5 OPENS: team milestones]
```

---

### PHASE 5 — TEAM MILESTONES

**Entry condition**: PHASE 4 gate confirmed.

Evaluate all three milestones. Milestone names are fixed verbatim. Do not rename.

```
## Team Milestones

| Milestone | Status | Evidence | To earn (if NOT YET) |
|-----------|--------|----------|----------------------|
| first team signal | EARNED / NOT YET | [file path or "(none)"] | [what must happen] |
| shared coverage | EARNED / NOT YET | [contributor names + topic counts] | [what must happen] |
| debate starter | EARNED / NOT YET | [topic + namespace list] | [what must happen] |
```

WHEN workspace is empty, all three show NOT YET with "workspace is empty" as evidence.

**Gate**: State before Phase 6 opens:
```
[PHASE 5 CLOSED: milestones — [n/3] earned]
[PHASE 6 OPENS: 1-away gap detection]
```

---

### PHASE 6 — 1-AWAY GAP DETECTION

**Entry condition**: PHASE 5 gate confirmed.

Scan every achievement and milestone for gaps of exactly 1 unit.

For each 1-away gap found:
`- [topic / milestone]: needs 1 more [signal / contributor / namespace] → **[Achievement name]**`

WHEN no 1-away gaps exist, this phase MUST NOT close until both cascade levels are written:

```
No 1-away gaps detected.
Level 1 — Closest to 1-away threshold: [specific topic or milestone name] needs [n] more [unit] to unlock **[Achievement]**.
Level 2 — Closest to 2-away threshold: [specific topic or milestone name] needs [n] more [unit] to unlock **[Achievement]**.
```

The Level 1 and Level 2 rows are a gate condition. PHASE 6 cannot close if either level is
absent, vague ("a topic"), or lacks a specific numeric step count.

**Gate**: State before Phase 7 opens:
```
[PHASE 6 CLOSED: [n] 1-away gaps (or: 0 gaps — L1 and L2 cascade written)]
[PHASE 7 OPENS: next actions]
```

---

### PHASE 7 — NEXT ACTIONS

**Entry condition**: PHASE 6 gate confirmed.

Before writing any action, check the health condition score from PHASE 3 to determine
the Breaks field. The following pre-write check MUST be consulted before each Breaks value
is written:

```
Pre-write check — Breaks field determination:
  Condition score >= 1 → write: [condition name] — [what this action dissolves]
  Condition score = 0  → write: prevents: [condition name] — [re-entry rationale explaining
                                what keeps the condition from returning]
  N/A → not permitted; do not write N/A in any Breaks field
```

Write at least 3 actions using this template:

```
**Action**: [namespace/topic — specific verb phrase]
**Unlocks**: [exact achievement or milestone name]
**Breaks**: [from pre-write check above:
  score >= 1: condition name — dissolution phrase
  score = 0:  prevents: condition name — re-entry rationale]
**Why**: [one sentence from PHASE 4 or PHASE 5 gap data]
```

Generic advice without a specific namespace and topic fails. Each action must name both.

**Gate**: State before Phase 8 opens:
```
[PHASE 7 CLOSED: [n] actions written — prevents: used for [n] zero-score conditions]
[PHASE 8 OPENS: team synthesis]
```

---

### PHASE 8 — TEAM SYNTHESIS

**Entry condition**: PHASE 7 gate confirmed.

One sentence drawing a cross-topic or cross-contributor conclusion not visible from any single
topic in PHASE 4. Must include at least one concrete number and one specific name. Close with
a recommended implication.

**Gate**: State before Phase 9:
```
[PHASE 8 CLOSED: synthesis written]
[PHASE 9 OPENS: write artifact]
```

---

### PHASE 9 — WRITE ARTIFACT

**Entry condition**: PHASE 8 gate confirmed.

Write the complete output (all phases) to:
`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
phases_completed: 9
topics_scanned: [n]
milestones_earned: [n]/3
dominant_health_condition: [name or "none"]
contributors_detected: [n or "unknown"]
---
```

Emit the completion gate:
```
[COMPLETION GATE: artifact written — [n] signals — [n] topics — [n/3] milestones — dominant: [condition]]
```

---

## V-04 — Role Sequence + Phrasing Register: 4-Role Pipeline with MUST Spec

**Axis**: Role sequence (4 discrete roles: Archaeologist → Health Analyst → Achievement Compiler
→ Report Narrator) + Phrasing register (MUST/SHALL/WHEN within each role)
**Hypothesis**: Clean role boundaries prevent scope bleed (C-11 satisfied by design: Health
Analyst closes before Achievement Compiler opens). MUST language within each role makes each
criterion independently auditable. C-22 is strongest in this variation: the Achievement Compiler
role is explicitly split into a pre-write decision step and a template-filling step, placing the
`prevents:` rule in two structurally distinct locations within that role. C-23 is embedded in
the Compiler's 1-away section as a two-level MUST requirement. The Narrator role writes the
synthesis and artifact, allowing the Compiler to focus on mechanical correctness.

---

You are running `corps-leaderboard`. No arguments. Work through four roles in strict sequence.
Do not start a role until the previous role's output is confirmed complete.

---

### ROLE 1 — SIGNAL ARCHAEOLOGIST

Your job in this role: discover and record what exists. No analysis. Only facts.

Glob `simulations/**/*.md`. For each file, record:
- Topic path (subdirectory of `simulations/`, e.g., `scout/competitors`)
- Namespace (first path segment after `simulations/`)
- Contributor identity (from frontmatter `author:` / `contributor:` fields, or filename prefix)
- Date field if present

Produce a Signal Inventory:

```
## Signal Inventory — {{date}}

Topics: [n]
Namespaces active: [list]
Contributors identified: [list or "(not detectable)"]
Total signals: [n]

[For each topic:]
  [topic path] — [n] signals — contributors: [list or "unknown"] — namespaces: [list]
```

WHEN `simulations/` is absent or empty, write:
```
Signal Inventory: workspace empty — 0 signals. Inventory is empty.
```
Proceed to Role 2 with empty inventory.

Gate line:
```
[ARCHAEOLOGY GATE: inventory complete — [n] topics — [n] signals — [n or "unknown"] contributors]
```

---

### ROLE 2 — HEALTH ANALYST

Your job in this role: assess signal-gathering discipline. Consume the Signal Inventory from
Role 1. Do not compute achievements — that is Role 3's job.

**Part A — Contributor Leaderboard**

Rank all contributors from the Inventory by total signals descending. Ties broken by topics covered.

```
## Contributor Leaderboard — {{date}}

| Rank | Contributor | Total Signals | Topics Covered | Namespaces Active |
|------|-------------|---------------|----------------|-------------------|
```

WHEN attribution is unavailable: one row — `| — | (no contributor metadata found) | — | — | — |`

Follow the table with one cross-row observation sentence.

**Part B — Signal Health Score**

Evaluate the 5 stagnation conditions. Score each 0–3. Urgency: 0 = LOW, 1 = MED, 2–3 = HIGH.
N/A is not a valid score value.

Condition names are fixed. Use exact names:
- **Empty Start**, **Lone Wolf**, **Namespace Tunnel**, **Stale Coverage**, **Shallow Spread**

| Condition | Score | Urgency | Evidence |
|-----------|-------|---------|----------|
| Empty Start | | | |
| Lone Wolf | | | |
| Namespace Tunnel | | | |
| Stale Coverage | | | |
| Shallow Spread | | | |

**Dominant condition**: [name of highest-scoring condition or "none"]

Gate line:
```
[HEALTH GATE: leaderboard ranked — health scored — dominant = [name or "none"] — [LOW/MED/HIGH]. Achievement Compiler may open.]
```

---

### ROLE 3 — ACHIEVEMENT COMPILER

Your job in this role: compute achievements and produce the action plan. Consume the Signal
Inventory (Role 1) and the Health Assessment (Role 2). You have three tasks.

**Task A — Achievement Evaluation**

For each topic in the inventory, evaluate all 5 achievements:

- **First Signal** — file_count >= 1
- **Signal Depth** — file_count >= 3
- **Full Sweep** — topic's namespace_set size >= 3
- **Solo Pioneer** — contributor_set size == 1 AND file_count >= 1
- **Team Topic** — contributor_set size >= 2, each with >= 1 signal

Achievement names are fixed verbatim. Do not rename or paraphrase.

```
## Achievements

### Earned ✓
**[topic path]** ([n] signals)
  ✓ [Achievement name] — [evidence]

### Locked ○
**[topic path]** ([n] signals)
  ○ [Achievement name] — needs [specific gap: n more signals / contributor / namespace]
```

Every topic in the inventory must appear. A missing topic is a Compiler error.

**Task B — Team Milestones and 1-Away Gaps**

Evaluate team milestones using their exact fixed names:

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|----------|
| first team signal | EARNED / NOT YET | [evidence] |
| shared coverage | EARNED / NOT YET | [evidence] |
| debate starter | EARNED / NOT YET | [evidence] |
```

Renaming, paraphrasing, or abbreviating any milestone name is a Compiler error.

**1-Away Gaps**

List every achievement or milestone gap of exactly 1 unit.

WHEN 1-away gaps exist:
`- [topic / milestone]: 1 more [unit] → **[Achievement name]**`

WHEN no 1-away gaps exist, the following two levels are BOTH required:

```
No 1-away gaps detected.
Level 1 — Closest to 1-away: [specific topic or milestone name] needs [n] more [unit] → **[Achievement]**
Level 2 — Closest to 2-away: [specific topic or milestone name] needs [n] more [unit] → **[Achievement]**
```

Both levels must carry a specific name (not "a topic") and a specific numeric step count.

**Task C — Recommended Actions**

Before writing the Breaks value for any action, apply this pre-write decision check:

```
Pre-write decision check — Breaks field:
  Health condition score >= 1 → Breaks: [condition name] — [what this action dissolves]
  Health condition score = 0  → Breaks: prevents: [condition name] — [re-entry rationale]
  Do not write N/A.
```

Write at least 3 actions using this template:

```
**Action**: [namespace/topic — specific verb phrase what to file or do]
**Unlocks**: [exact achievement or milestone name]
**Breaks**: [
  if condition score >= 1: condition name — dissolution phrase
  if condition score = 0:  prevents: condition name — re-entry rationale
]
**Why**: [one sentence from Task A or Task B gap data]
```

The `prevents:` prefix is required when the targeted condition scores 0. Writing the condition
name without the `prevents:` prefix when score = 0 is a Compiler error.

Generic advice without namespace and topic is a Compiler error.

Gate line:
```
[COMPILER GATE: [n] topics evaluated — [n] earned — [n] locked — [n/3] milestones — [n] actions — Level 1 and Level 2: [written / not needed]]
```

---

### ROLE 4 — REPORT NARRATOR

Your job in this role: produce the synthesis sentence and write the artifact. Consume all
Role 1, 2, and 3 outputs.

**Team Insight**

Write one sentence drawing a cross-topic or cross-contributor conclusion not visible from any
single topic in Role 3. Include at least one concrete number and one specific name. Close with
a recommended implication.

**Write Artifact**

Assemble the complete output (all roles) and write to:
`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
roles_completed: 4
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
dominant_health_condition: [name or "none"]
---
```

Emit completion gate:
```
[COMPLETION GATE: artifact written — [n] topics — [n/3] milestones — dominant: [condition] — synthesis: written]
```

---

## V-05 — Inertia Framing + Role Sequence: Skeptic-First Pipeline

**Axis**: Inertia framing (name the cost of doing nothing before compiling wins) + Role sequence
(Skeptic opens, Archaeologist provides facts, Compiler builds outputs, all three consumed by Writer)
**Hypothesis**: Leading with a Skeptic role forces the model to name what the team is flying blind
on before it ever writes an achievement list — this primes the Breaks field (C-20) with authentic
cost language grounded in a named inertia problem, making the `prevents:` construct (C-22) more
meaningful because it states what prevents a real named cost from returning, not a generic label.
The 1-away cascade (C-23) is framed as a skeptic-vs-compiler debate: the skeptic says "nothing
is close," the compiler must prove it wrong with two specific levels. Risk: inertia framing adds
prose that may crowd out mechanical correctness — each role has a strict output structure to prevent
this.

---

You are running `corps-leaderboard`. No arguments. Work through three roles in sequence.
Do not start a role until the previous role output is complete.

---

### ROLE 1 — SKEPTIC

Your job: represent the voice that says "we don't know enough to ship." Before any achievement
is counted, name what the team is flying blind on. Then produce the evidence base.

**Part A — Signal Scan**

Glob `simulations/**/*.md`. Record for each file:
- Topic path (subdirectory under `simulations/`)
- Namespace (first path segment)
- Contributor identity (frontmatter `author:` / `contributor:` or filename prefix)
- Date field if detectable

Produce a Signal Inventory (internal — used by all roles):

```
SIGNAL INVENTORY
Total signals: [n] | Topics: [n] | Namespaces: [list] | Contributors: [list or "not detectable"]

[topic path] — [n] signals — contributors: [list or "unknown"]
...
```

WHEN workspace is empty: "Signal Inventory: empty — 0 signals." Proceed with empty data.

**Part B — Inertia Assessment**

Using the inventory, answer in 3 sentences maximum:

1. What does the current signal pattern tell us about team discipline? (Is coverage concentrated?
   Are signals old? Is one person doing everything?)
2. What decisions is the team making without enough signal? (Name specific topic areas.)
3. What is the cost of another sprint at this rate?

Then name the **Dominant Inertia Pattern**. Select the best match:
- **Empty Start** — 0 signals; team has not started signal-gathering discipline
- **Lone Wolf** — one contributor > 60% of signals; single point of knowledge failure
- **Namespace Tunnel** — signals in <= 2 namespaces; blind to flow/trace/prove risks
- **Stale Coverage** — all signals > 90 days old; coverage exists but may be outdated
- **Shallow Spread** — topics started but none past Signal Depth; breadth without evidence

Output:
```
## Inertia Assessment

Dominant Inertia Pattern: [name]
Urgency: [LOW / MED / HIGH] (LOW = no active signals, MED = some but concentrated, HIGH = multiple conditions)
Decision blindspot: [one sentence — what area the team would commit to without knowing enough]
Cost: [one sentence — what stays broken if nothing changes]
```

Gate line:
```
[SKEPTIC GATE: inventory complete — dominant inertia = [name] — [LOW/MED/HIGH]]
```

---

### ROLE 2 — COMPILER

Your job: produce the structured outputs. Consume the Signal Inventory from Role 1.
The Inertia Assessment from Role 1 informs every Breaks value you write.

**Section A — Contributor Leaderboard**

Rank all contributors by total signals descending. Ties broken by topics covered.

```
## Contributor Leaderboard — {{date}}

| Rank | Contributor | Total Signals | Topics Covered | Namespaces Active |
|------|-------------|---------------|----------------|-------------------|
```

WHEN attribution unavailable: `| — | (no contributor metadata found) | — | — | — |`

Follow with one cross-row observation sentence.

Gate line:
```
[LEADERBOARD GATE: [n] contributors ranked]
```

**Section B — Achievement Evaluation**

For each topic in the inventory, evaluate all 5 achievements.
Achievement names are fixed verbatim — do not rename:

- **First Signal** — file_count >= 1
- **Signal Depth** — file_count >= 3
- **Full Sweep** — topic namespace_set size >= 3
- **Solo Pioneer** — contributor_set size == 1 AND file_count >= 1
- **Team Topic** — contributor_set size >= 2 with >= 1 signal each

```
## Achievements by Topic

### Earned ✓
**[topic path]** ([n] signals)
  ✓ [name] — [evidence]

### Locked ○
**[topic path]** ([n] signals)
  ○ [name] — needs [n more signals / contributor / namespace]
```

Every topic from the inventory must appear. Omission is a Compiler error.

**Section C — Team Milestones**

The three milestone names are fixed. Do not rename them:

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|----------|
| first team signal | EARNED / NOT YET | [file path or "(none)"] |
| shared coverage | EARNED / NOT YET | [contributor names + topic counts] |
| debate starter | EARNED / NOT YET | [topic + namespace list] |
```

**Section D — 1-Away Gaps**

The Skeptic said nothing is close. Prove it — or prove them wrong.

List every gap of exactly 1 unit:
`- [topic / milestone]: 1 more [unit] → **[Achievement]**`

WHEN no 1-away gaps exist (the Skeptic is right about the near term), write:

```
No 1-away gaps detected. Nearest targets:

Level 1 — Closest to 1-away threshold: [specific topic or milestone name] needs [n] more [unit] to unlock **[Achievement]**
Level 2 — Closest to 2-away threshold: [specific topic or milestone name] needs [n] more [unit] to unlock **[Achievement]**
```

Both levels are required. Each must name a specific topic or milestone and a specific numeric
step count. If only one level is written, the Skeptic wins — the team has no two-sprint plan.

**Section E — Anti-Inertia Actions**

Before writing each action, consult the inertia scoring from Role 1 to determine the Breaks value.

Pre-write check table (resolve before writing each Breaks field):

| Inertia condition score | Breaks field to write |
|-------------------------|-----------------------|
| Score >= 1 (condition is active) | [condition name] — [what this action dissolves or weakens] |
| Score = 0 (condition is already resolved) | prevents: [condition name] — [re-entry rationale: what this action does to ensure the condition does not return] |

Do not write N/A in any Breaks field.

Write at least 3 anti-inertia actions. Each must name the inertia it fights:

```
**Action**: [namespace/topic — specific verb phrase]
**Unlocks**: [exact achievement or milestone name]
**Breaks**: [use pre-write check table above:
  active condition → condition name — dissolution phrase
  resolved condition → prevents: condition name — re-entry rationale]
**Why this sprint**: [one sentence from Section B or C gap data, connecting to the Dominant
  Inertia Pattern from Role 1]
```

The `prevents:` prefix is required when the targeted condition scores 0. An action that names
a resolved condition without `prevents:` is a Compiler error.

Gate line:
```
[COMPILER GATE: achievements — [n] earned / [n] locked | milestones — [n/3] | 1-away — [n] or Level 1+Level 2 written | actions — [n]]
```

---

### ROLE 3 — REPORT WRITER

Your job: produce the team insight and write the artifact. Consume all Role 1 and Role 2 outputs.

**Team Insight**

Synthesize a cross-topic or cross-contributor conclusion not visible from any single section in
Role 2. The insight must be something the Skeptic (Role 1) would acknowledge as new information —
not a restatement of the inertia assessment. Include at least one concrete number and one specific
name. Close with a recommended implication.

**Write Artifact**

Assemble all sections in order:
1. Inertia Assessment (Role 1)
2. Contributor Leaderboard (Role 2 Section A)
3. Achievements by Topic (Role 2 Section B)
4. Team Milestones (Role 2 Section C)
5. 1-Away Gaps (Role 2 Section D)
6. Anti-Inertia Actions (Role 2 Section E)
7. Team Insight (Role 3)

Write to: `simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
dominant_inertia_pattern: [name from Role 1]
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
---
```

Emit:
```
[COMPLETION GATE: artifact written — [n] topics — [n/3] milestones — dominant: [pattern] — anti-inertia actions: [n]]
```
