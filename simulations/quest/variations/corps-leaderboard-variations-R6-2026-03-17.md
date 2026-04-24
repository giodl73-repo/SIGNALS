R6 variations written to `simulations/quest/variations/corps-leaderboard-variations-R6-2026-03-17.md`.

---

## Variate R6 — corps-leaderboard

**5 variations targeting 100 against rubric v6.** All R5 variations scored ~99.2 (each failing exactly one of C-20 or C-21). R6 closes both simultaneously.

---

### Variation Map

| | Variation | Primary Axis | C-20 mechanism | C-21 mechanism |
|--|-----------|--------------|----------------|----------------|
| **V-01** | All-Tables Scorecard | Output format | `Breaks` as a table column — cell rule enforces `prevents: {rationale}` when score = 0; worked examples for both cases | `(nearest miss)` row appended to 1-away table when gaps list is empty; names specific topic + numeric gap |
| **V-02** | Cascading Nearest-Miss | C-21 depth | Three-field template; "score = 0 → `prevents:` prefix + rationale; N/A prohibited" | Two-level cascade: Level 1 (closest 1-away) + Level 2 (closest 2-away); both required when list empty |
| **V-03** | Declarative Spec | Phrasing register | "WHEN score = 0: the Breaks field MUST begin with `prevents:` followed by re-entry rationale" — MUST language makes criterion directly keyword-auditable | "WHEN no 1-away gaps exist, the skill MUST output a nearest-miss pointer naming closest candidate and numeric gap" — hard MUST clause |
| **V-04** | 3-Role + Worked Examples | Role sequence + combination | Paired worked examples in compiler role: one active-condition example, one `prevents:` example, side-by-side at point of writing | Two-level cascading fallback in compiler role with Level 1 + Level 2 pointers |
| **V-05** | Bidirectional Stamps + Full | Lifecycle emphasis + combination | Pre-write check table (`score >= 1 → name; score = 0 → prevents:`) + two worked examples; rule stated twice | Hard structural requirement in Section 6: "this clause is required… must name specific topic and numeric gap count" — stated as requirement not suggestion |

---

**Structural notes:**
- **V-01** is strongest on machine-readability — table column layout makes C-20/C-21 auditable by cell content
- **V-02** is strongest on C-21 depth — two-level cascade provides a sprint plan even when no 1-away gaps exist
- **V-03** is strongest on constraint auditability — every criterion has a MUST/SHALL keyword that makes it independently findable by search
- **V-04** is strongest on C-20 clarity — paired worked examples at the point of writing minimize register confusion
- **V-05** is strongest overall — bidirectional stamps (proven R5 V-05 baseline) + C-20 rule stated twice + C-21 stated as a hard requirement; highest combined structural auditability

All five variations cover C-01 through C-19 (all criteria inherited from prior rounds).
ons will still be produced with empty-state values.

Gate line:
```
[SCAN GATE: {n} signals found across {n} topics, {n} namespaces, {n or "unknown"} contributors. Proceeding to Phase 2.]
```
Empty workspace variant:
```
[SCAN GATE: workspace empty — no signals found. Proceeding to Phase 2 with empty registry.]
```

---

### PHASE 2 — CONTRIBUTOR LEADERBOARD

**Entry condition**: SCAN GATE confirmed.

Produce raw contributor evidence before naming any stagnation pattern.

```
## Contributor Leaderboard — {{date}}

| Rank | Contributor | Total Signals | Topics Covered | Namespaces Active |
|------|-------------|---------------|----------------|-------------------|
| 1    | [name]      | [n]           | [n]            | [list]            |
| ...  |             |               |                |                   |
```

Rank descending by total signals. Ties broken by topics covered (descending).

If contributor attribution is not extractable from any frontmatter or filename pattern, produce one row:
`| — | (no contributor metadata found) | — | — | — |`

This section must not be omitted regardless of workspace state.

Gate line:
```
[LEADERBOARD GATE: {n} contributors ranked. Attribution source: frontmatter / filename / not available. Proceeding to Phase 3.]
```

---

### PHASE 3 — SIGNAL HEALTH SCORE

**Entry condition**: LEADERBOARD GATE confirmed.

Score 5 stagnation conditions 0–3 (0 = absent, 1 = minor, 2 = significant, 3 = dominant).
Urgency tiers: score 0 = LOW, score 1 = MEDIUM, score 2–3 = HIGH.

```
## Signal Health Score

| Condition        | Score (0–3) | Urgency | Evidence                            |
|-----------------|-------------|---------|-------------------------------------|
| Empty Start      | [0–3]       | [H/M/L] | [evidence, or "—"]                  |
| Lone Wolf        | [0–3]       | [H/M/L] | [leaderboard row or contributor name, or "—"] |
| Namespace Tunnel | [0–3]       | [H/M/L] | [namespace counts, or "—"]          |
| Stale Coverage   | [0–3]       | [H/M/L] | [date range, or "—"]                |
| Shallow Spread   | [0–3]       | [H/M/L] | [topic/signal ratio, or "—"]        |

Dominant condition: [highest-scoring condition, or "None — workspace is healthy"]
```

When diagnosing Lone Wolf or Stale Coverage, cite the specific leaderboard row or contributor name from Phase 2 as evidence (e.g., "Contributor X holds rank 1 with n% of signals — see leaderboard row 1").

This section must appear before the achievement compilation in Phase 4. SIGNAL HEALTH SCORE must be complete before ACHIEVEMENT GRID opens.

Note conditions with score = 0 (resolved). Actions targeting resolved conditions must use `prevents:` framing in Phase 6. The Priority field of each action must derive from the urgency of its targeted condition: HIGH urgency → Priority: HIGH, MEDIUM → Priority: MEDIUM, LOW → Priority: LOW.

Gate line:
```
[HEALTH GATE: health score computed. Dominant: {condition or "None"}. Proceeding to Phase 4.]
```

---

### PHASE 4 — ACHIEVEMENT GRID

**Entry condition**: HEALTH GATE confirmed.

Build a matrix table. One row per discovered topic. A topic present in the SCAN REGISTRY but absent from this table is a **table gap**.

```
## Achievement Grid — {{date}}

| Topic | Signals | First Signal | Signal Depth | Full Sweep | Solo Pioneer | Team Topic | Top Contributor |
|-------|---------|:------------:|:------------:|:----------:|:------------:|:----------:|:---------------:|
| [path] | [n] | ✓ or ○+[n] | ✓ or ○+[n] | ✓ or ○+[n] | ✓ or ○+[n] | ✓ or ○+[n] | [name or unknown] |
```

Cell notation:
- `✓` = earned
- `○+n` = locked, needs n more [signal / contributor / namespace]
- `—` = cannot determine; append a footnote row with reason

Achievement definitions (exact column header names — paraphrasing fails):
- **First Signal** — file_count >= 1
- **Signal Depth** — file_count >= 3
- **Full Sweep** — namespace_count >= 3 for this topic
- **Solo Pioneer** — contributor_count == 1 AND file_count >= 1
- **Team Topic** — contributor_count >= 2, each with >= 1 signal

If `simulations/` was empty: produce the table header only, then: "No topics discovered — all achievement columns empty."

Gate line:
```
[ACHIEVE GATE: {n} topics compiled. {n} earned achievements. {n} locked. Proceeding to Phase 5.]
```

---

### PHASE 5 — TEAM MILESTONES

**Entry condition**: ACHIEVE GATE confirmed.

```
## Team Milestones

| Milestone          | Status           | Evidence                                      |
|--------------------|-----------------|-----------------------------------------------|
| first team signal  | EARNED / NOT YET | [file path, or "— (none found)"]              |
| shared coverage    | EARNED / NOT YET | [contributor names + topic counts, or "— (none found)"] |
| debate starter     | EARNED / NOT YET | [topic + namespace list, or "— (none found)"] |
```

Milestone names are fixed. Do not rename, abbreviate, or paraphrase: `first team signal`, `shared coverage`, `debate starter`.

Conditions:
- **first team signal** — any signal file present in `simulations/`
- **shared coverage** — >= 2 contributors each present in >= 2 distinct topic paths
- **debate starter** — >= 1 topic with signals from >= 2 distinct namespaces

Gate line:
```
[MILESTONES GATE: {n/3} earned. first team signal: {E/N}. shared coverage: {E/N}. debate starter: {E/N}. Proceeding to Phase 6.]
```

---

### PHASE 6 — 1-AWAY GAPS + ACTION GRID + TEAM SYNTHESIS

**Entry condition**: MILESTONES GATE confirmed.

#### 1-Away Gaps

Scan every achievement and milestone for gaps of exactly 1 unit.

```
## 1-Away Gaps

| Topic or Milestone | Needs                              | To Unlock                    |
|--------------------|------------------------------------|------------------------------|
| [path]             | 1 more [signal/contributor/ns]     | **[Achievement or Milestone]** |
```

When no rows qualify, add one row in the same table:
```
| (nearest miss) | [topic] needs [n] more [unit] | **[Achievement]** — closest to 1-away threshold |
```

The nearest-miss row is required when the gap table would otherwise be empty. It must name a specific topic or milestone and state its numeric gap count. "No 1-away gaps" alone without this row fails.

#### Action Grid

Write at least 3 next actions as a table. Each row must identify a specific namespace and topic.

```
## Next Actions

| Action | Unlocks | Breaks | Priority |
|--------|---------|--------|----------|
| [namespace/topic + what to do] | [exact achievement or milestone name] | [see Breaks rules] | HIGH / MEDIUM / LOW |
```

**Breaks column rules — N/A is prohibited:**

- When the targeted health condition has **score >= 1** (active): write the condition name (e.g., `Shallow Spread`)
- When the targeted health condition has **score = 0** (resolved): write `prevents: {condition name} — {re-entry rationale}` (e.g., `prevents: Namespace Tunnel — filing this namespace keeps topic namespace count at 3+, blocking re-entry into single-namespace concentration`)

The `prevents:` prefix is mandatory when the targeted condition is resolved. An empty Breaks cell, a cell reading "N/A", or a cell that names a resolved condition without the `prevents:` prefix fails.

Priority must derive from the urgency of the targeted condition (Phase 3): HIGH urgency → Priority: HIGH, MEDIUM → Priority: MEDIUM, LOW → Priority: LOW.

Generic actions without a specific namespace and topic fail.

#### Team Synthesis

Write one sentence drawing a cross-topic or cross-contributor conclusion not visible from any single row of the achievement grid. Include at least one concrete number from: **contributor count**, **signal count**, **namespace count**, or **topic count**. Close with a recommended implication.

Gate line:
```
[COMPLETION GATE: corps-leaderboard complete. {n} 1-away gaps (or nearest-miss row). {n} actions. Team synthesis written. Writing artifact.]
```

---

### PHASE 7 — WRITE ARTIFACT

**Entry condition**: COMPLETION GATE confirmed.

Write the complete output to:
`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
dominant_health_condition: [name or "None"]
---
```

---

## V-02 — Cascading Nearest-Miss: Two-Level 1-Away Fallback

**Axis**: 1-away section depth — when no 1-away gaps are found, the if-none clause cascades through two levels: closest 1-away candidate (what would qualify if it gained 1 more) and closest 2-away candidate (what would qualify if it gained 2 more)

**Hypothesis**: C-21 requires the nearest-miss pointer to name the closest qualifying candidate and its numeric gap. This satisfies the minimum. A two-level cascade adds directional depth: the team who finds no 1-away targets learns both the closest gap and the next-closest, enabling a two-sprint plan. If v7 introduces a criterion for multi-level nearest-miss, V-02 is pre-compliant. The risk is that the cascade adds verbosity for sparse workspaces where the 1-away list is populated and the cascade never fires.

---

You are running `corps-leaderboard`. No inputs. Scan and compute from workspace state.
Work through 6 phases in sequence. State each numbered gate line before advancing.

---

### PHASE 1 — SCAN

Glob `simulations/**/*.md`. For each file:
- Record topic path (subdirectory under `simulations/`, e.g., `scout/competitors`)
- Record namespace (first path segment)
- Extract contributor from frontmatter `author:` / `contributor:` fields or filename prefix before first `-`
- Record any date field

Build an internal REGISTRY:
```
REGISTRY:
  topics: [unique topic paths]
  per topic: { file_count, contributor_set, namespace_set }
  all_contributors: [deduplicated]
  all_namespaces: [list]
  total_signals: [n]
```

If `simulations/` is empty or absent, record this and continue with empty data. All sections will still be produced.

```
[GATE 1: SCAN — {n} signals across {n} topics, {n} namespaces, {n or "unknown"} contributors. Registry built. Proceeding to Phase 2.]
```
Empty variant:
```
[GATE 1: SCAN — workspace empty. No signals found. Registry empty. Proceeding to Phase 2 with no data.]
```

---

### PHASE 2 — CONTRIBUTOR LEADERBOARD

**Entry condition**: GATE 1 confirmed.

Present raw contributor evidence before naming any stagnation pattern.

```
## Contributor Leaderboard — {{date}}

| Rank | Contributor | Total Signals | Topics Covered | Namespaces Active |
|------|-------------|---------------|----------------|-------------------|
```

Rank descending by total signals. Ties: break by topics covered (descending). If no attribution is detectable: one row `(no contributor metadata found)` with dashes. Do not omit this section.

After the table, write one leaderboard observation sentence that compares across rows (not a restatement of table values). Include a specific number.

```
[GATE 2: LEADERBOARD — {n} contributors ranked. Proceeding to Phase 3.]
```

---

### PHASE 3 — SIGNAL HEALTH SCORE

**Entry condition**: GATE 2 confirmed.

LEADERBOARD closed. SIGNAL HEALTH SCORE opens now.

Score 5 stagnation conditions 0–3 (0 = absent, 1 = minor, 2 = significant, 3 = dominant). Urgency: 0 = LOW, 1 = MEDIUM, 2–3 = HIGH.

```
## Signal Health Score

| Condition        | Score | Urgency | Evidence |
|-----------------|-------|---------|----------|
| Empty Start      | [0–3] | [H/M/L] | [evidence or "—"] |
| Lone Wolf        | [0–3] | [H/M/L] | [cite leaderboard row or contributor name] |
| Namespace Tunnel | [0–3] | [H/M/L] | [namespace distribution] |
| Stale Coverage   | [0–3] | [H/M/L] | [date range] |
| Shallow Spread   | [0–3] | [H/M/L] | [topic/signal ratio] |

Dominant condition: [highest-scoring, or "None — workspace is healthy"]
```

When Lone Wolf or Stale Coverage scores > 0, cite the specific leaderboard row as evidence (e.g., "As shown above in row 1, contributor X holds {n}% of signals").

This section must be complete before achievement compilation begins. SIGNAL HEALTH SCORE must close before ACHIEVEMENTS opens.

Note which conditions have score = 0 (resolved). Actions targeting a resolved condition must use `prevents:` framing. Priority in each action derives from the urgency tier of its targeted condition.

```
[GATE 3: HEALTH SCORE — dominant condition: {name or "None"}. Proceeding to Phase 4.]
```

---

### PHASE 4 — ACHIEVEMENTS + MILESTONES

**Entry condition**: GATE 3 confirmed.

SIGNAL HEALTH SCORE closed. ACHIEVEMENT COMPILATION opens now.

For each topic in the REGISTRY, evaluate all 5 achievements. A topic present in the REGISTRY but absent from the output is a **pipeline gap**.

```
## Achievements by Topic

### Earned ✓

**{topic path}** ({n} signals)
  - **First Signal** — {evidence}          [if earned]
  - **Signal Depth** — {evidence}          [if earned]
  - **Full Sweep** — {namespaces}          [if earned]
  - **Solo Pioneer** — {contributor count} [if earned]
  - **Team Topic** — {contributor names}   [if earned]

### Locked ○

**{topic path}** ({n} signals)
  - ○ **Signal Depth** — needs [n] more signals      [if locked]
  - ○ **Full Sweep** — needs [n] more namespaces      [if locked]
  - ○ **Team Topic** — needs [n] more contributors   [if locked]
```

Achievement definitions (exact names — paraphrasing fails):
- **First Signal** — file_count >= 1
- **Signal Depth** — file_count >= 3
- **Full Sweep** — namespace_count >= 3 for this topic
- **Solo Pioneer** — contributor_count == 1 AND file_count >= 1
- **Team Topic** — contributor_count >= 2, each with >= 1 signal

```
## Team Milestones

| Milestone          | Status           | Evidence                                       |
|--------------------|-----------------|------------------------------------------------|
| first team signal  | EARNED / NOT YET | [file path or "— (none found)"]                |
| shared coverage    | EARNED / NOT YET | [contributor + topic count, or "— (none found)"] |
| debate starter     | EARNED / NOT YET | [topic + namespace list, or "— (none found)"]  |
```

Milestone names are fixed verbatim: `first team signal`, `shared coverage`, `debate starter`. Renaming or paraphrasing fails.

```
[GATE 4: ACHIEVEMENTS + MILESTONES — {n} earned achievements. {n/3} milestones earned. Proceeding to Phase 5.]
```

---

### PHASE 5 — 1-AWAY GAPS (CASCADING FALLBACK)

**Entry condition**: GATE 4 confirmed.

List every achievement and milestone that is exactly 1 unit away from being earned:
```
## 1-Away Gaps

- **{topic or milestone}**: needs 1 more [signal / contributor / namespace] to unlock **{Achievement}**
```

**Required cascading fallback when the 1-away list is empty:**
```
No 1-away gaps found.

> Level 1 — Closest 1-away candidate: **{topic}** needs {n} more {unit} to unlock **{Achievement}** (gap = {n}, nearest miss at threshold 1).
> Level 2 — Closest 2-away candidate: **{topic}** needs {n} more {unit} to unlock **{Achievement}** (gap = {n}, nearest miss at threshold 2).
```

Both cascade levels are required when the list is empty. Each level must name a specific topic or milestone and state its numeric gap. A statement of absence without the cascading nearest-miss pointer fails this section.

```
[GATE 5: GAPS — {n} 1-away gaps found, or cascading fallback written. Proceeding to Phase 6.]
```

---

### PHASE 6 — NEXT ACTIONS + TEAM SYNTHESIS + ARTIFACT

**Entry condition**: GATE 5 confirmed.

#### Next Actions

Write at least 3 actions. Each must follow this three-field template:
```
{n}. **{action — specific namespace/topic}**
   -> Unlocks: {exact achievement or milestone name}
   -> Breaks: {see field rules below}
   -> Priority: HIGH / MEDIUM / LOW
```

**Breaks field rules — N/A is prohibited:**
- **Condition score >= 1 (active)**: name the condition directly (e.g., `Breaks: Shallow Spread`)
- **Condition score = 0 (resolved)**: write `prevents: {condition name} — {re-entry rationale}` (e.g., `Breaks: prevents: Lone Wolf — adding a second contributor here prevents the topic from reverting to single-contributor coverage if the current contributor pauses`)

Every action must link to a health condition from Phase 3. An action with a blank or N/A Breaks field, or one that names a resolved condition without the `prevents:` prefix, fails.

Priority must derive from the urgency of the targeted condition: HIGH urgency → Priority: HIGH, MEDIUM → Priority: MEDIUM, LOW → Priority: LOW. State the urgency basis in the action if Priority differs from the dominant condition's tier.

Generic advice without a specific namespace and topic fails.

#### Team Synthesis

One sentence. Cross-topic or cross-contributor conclusion not visible from any single topic entry. Include at least one concrete number of type: **contributor count**, **signal count**, **namespace count**, or **topic count**. End with a recommended implication.

```
[COMPLETION GATE: corps-leaderboard complete. {n} actions. {n} 1-away gaps (or cascading fallback). Team synthesis written. Writing artifact.]
```

#### Write Artifact

`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
dominant_health_condition: [name or "None"]
---
```

---

## V-03 — Declarative Requirement Spec (MUST/SHALL Register)

**Axis**: Phrasing register — all constraints written as MUST/SHALL/WHEN requirements in a formal declarative spec, not as imperative prose instructions

**Hypothesis**: MUST/SHALL language makes each constraint independently auditable by scanning the instruction for the keyword. A scorer checking C-20 finds "MUST begin with `prevents:`" in the instruction; a scorer checking C-21 finds "MUST name the closest qualifying candidate and its numeric gap." Imperative prose ("write X if Y") creates ambiguity about whether the instruction is a requirement or a suggestion. MUST/SHALL eliminates that ambiguity. The risk is that declarative phrasing reduces contextual guidance, causing the model to satisfy the letter of a requirement without producing useful output.

---

You are executing the `corps-leaderboard` skill. This document defines the output requirements as a formal specification. All MUST clauses are mandatory. WHEN clauses are conditional requirements that activate under the stated condition.

---

### Requirement 1 — Workspace Scan

The skill MUST glob `simulations/**/*.md` and build a scan registry containing:
- A unique topic path for each subdirectory under `simulations/` that contains at least one `.md` file
- Per topic: file count, contributor set (from frontmatter `author:` / `contributor:` fields or filename prefix before first `-`), and namespace set
- Global: deduplicated contributor list, namespace list, total signal count

WHEN `simulations/` is absent or empty, the skill MUST record this explicitly and produce all output sections in empty state: no topics, all milestones NOT YET, leaderboard with one no-metadata row, next actions bootstrapping the first signal.

The skill MUST output a scan gate line:
```
[SCAN GATE: {n} signals, {n} topics, {n} namespaces, {n or "unknown"} contributors.]
```
WHEN empty:
```
[SCAN GATE: workspace empty — no signals found.]
```

---

### Requirement 2 — Contributor Leaderboard

The skill MUST produce a contributor leaderboard BEFORE evaluating any stagnation condition.

The leaderboard MUST:
- Be structured as a ranked table with columns: Rank, Contributor, Total Signals, Topics Covered, Namespaces Active
- Rank contributors in descending order by total signals
- Break ties by topics covered (descending)

WHEN contributor attribution is not extractable from any frontmatter or filename pattern, the leaderboard MUST contain exactly one row: `(no contributor metadata found)` with dashes in numeric columns. The leaderboard section MUST NOT be omitted.

The skill MUST output:
```
[LEADERBOARD GATE: {n} contributors ranked.]
```

---

### Requirement 3 — Signal Health Score

Requirement 3 MUST execute after Requirement 2 and MUST be complete before Requirement 4 begins. SIGNAL HEALTH SCORE MUST close before ACHIEVEMENT EVALUATION opens.

The skill MUST evaluate the workspace against exactly 5 stagnation conditions:
- **Empty Start** — no signals present
- **Lone Wolf** — one contributor accounts for the majority of signals
- **Namespace Tunnel** — signals concentrated in 1–2 namespaces
- **Stale Coverage** — all signals are old; no recent activity
- **Shallow Spread** — many topics started but none past First Signal

Each condition MUST be scored 0–3 (0 = absent, 1 = minor, 2 = significant, 3 = dominant).

Each condition MUST be assigned an urgency tier: score 0 = LOW, score 1 = MEDIUM, score 2–3 = HIGH.

The skill MUST name the dominant condition (highest-scoring), or state "None — workspace is healthy" when all scores are 0.

WHEN diagnosing Lone Wolf or Stale Coverage, the evidence field MUST cite the specific leaderboard row or contributor name from Requirement 2 (e.g., "As shown above in leaderboard row 1, contributor X holds n% of signals").

The skill MUST output:
```
[HEALTH GATE: dominant condition: {name or "None"}.]
```

---

### Requirement 4 — Achievement Evaluation

Requirement 4 MUST NOT begin before Requirement 3 is complete.

The skill MUST evaluate all 5 named achievements for every topic in the scan registry:
- **First Signal** — file count >= 1
- **Signal Depth** — file count >= 3
- **Full Sweep** — namespace count >= 3 for this topic
- **Solo Pioneer** — contributor count == 1 AND file count >= 1
- **Team Topic** — contributor count >= 2, each with >= 1 signal

Achievement names are fixed. The skill MUST NOT paraphrase, abbreviate, or rename them.

The skill MUST separate earned achievements from locked achievements in the output. Earned and locked MUST NOT appear in the same undifferentiated list.

A topic present in the scan registry but absent from the achievement section is a **spec gap**. The skill MUST ensure no spec gaps exist.

The skill MUST output:
```
[ACHIEVEMENTS GATE: {n} topics evaluated.]
```

---

### Requirement 5 — Team Milestones

The skill MUST evaluate all 3 team milestones using their fixed names:
- **first team signal** — any signal file present in `simulations/`
- **shared coverage** — >= 2 contributors each present in >= 2 distinct topic paths
- **debate starter** — >= 1 topic with signals from >= 2 distinct namespaces

Milestone names MUST NOT be renamed, abbreviated, or paraphrased. Each milestone MUST be given a status (EARNED or NOT YET) and a non-empty evidence field.

WHEN a milestone is NOT YET, the evidence field MUST state exactly what is needed to earn it.

---

### Requirement 6 — 1-Away Gap Detection

The skill MUST identify every achievement and milestone that is exactly 1 unit away from being earned.

For each such gap, the skill MUST state: the topic or milestone name, the exact numeric gap (1 more signal / 1 more contributor / 1 more namespace), and the target achievement or milestone name.

WHEN no 1-away gaps exist, the skill MUST output a nearest-miss pointer:
```
No 1-away gaps found. Closest: {topic} needs {n} more {unit} to unlock **{Achievement}**.
```

The nearest-miss pointer MUST include a specific topic or milestone name and a numeric step count. A statement of absence without a nearest-miss pointer fails this requirement.

---

### Requirement 7 — Next Actions

The skill MUST produce at least 3 recommended next actions.

Each action MUST follow this three-field template:
```
-> Unlocks: {exact achievement or milestone name}
-> Breaks: {see Breaks field rule}
-> Priority: HIGH / MEDIUM / LOW
```

**Breaks field rule — N/A is prohibited:**

WHEN the action targets a health condition with score >= 1 in Requirement 3: the Breaks field MUST name that condition (e.g., `Breaks: Shallow Spread`).

WHEN the action targets a health condition with score = 0 (condition already resolved): the Breaks field MUST begin with `prevents:` followed by a re-entry rationale explaining what regression is blocked (e.g., `Breaks: prevents: Shallow Spread — keeping at least 3 signals per topic prevents regression to single-signal coverage`).

An action with a blank Breaks field, a Breaks field containing "N/A", or a Breaks field naming a resolved condition without the `prevents:` prefix MUST NOT appear in the output.

Each action MUST name a specific namespace and topic path (e.g., `scout/competitors`, `flow/trigger`). Generic advice without a specific target MUST NOT appear.

The Priority field MUST reflect the urgency of the targeted condition: HIGH urgency condition → Priority: HIGH, MEDIUM → Priority: MEDIUM, LOW → Priority: LOW.

The skill MUST output:
```
[ACTIONS GATE: {n} actions written.]
```

---

### Requirement 8 — Team Synthesis

The skill MUST produce one team synthesis sentence that:
1. Draws a conclusion spanning at least two topics or two contributors — not visible from any single-topic evaluation
2. Includes at least one concrete number of type: **contributor count**, **signal count**, **namespace count**, or **topic count**
3. Ends with a recommended implication for the team

---

### Requirement 9 — Completion Gate and Artifact

The skill MUST output:
```
[COMPLETION GATE: corps-leaderboard complete. {n} actions. {n} 1-away gaps (or nearest-miss fallback). Team synthesis recorded.]
```

The skill MUST write the full output to: `simulations/corps/leaderboard-{{date}}.md`

Frontmatter MUST include:
```yaml
---
skill: corps-leaderboard
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
dominant_health_condition: [name or "None"]
---
```

---

## V-04 — Role Sequence + C-20 Worked-Example Pair + C-21 Cascading Near-Miss (Combination)

**Axes**: Role sequence (3-role pipeline: archaeologist → health analyst → achievement compiler) + C-20 worked-example pair (both `Breaks: {active condition}` and `Breaks: prevents: {rationale}` shown as paired side-by-side examples in the compiler role) + C-21 two-level cascading nearest-miss fallback

**Hypothesis**: Embedding paired worked examples for the `prevents:` register directly in the compiler role instruction — with both cases visible at the point of writing — reduces the probability of applying the wrong register more than a rule statement alone. Seeing `prevents: Lone Wolf — adding a second contributor...` immediately above the blank template primes the correct output. Pairing this with a two-level cascading nearest-miss (closest 1-away candidate + closest 2-away candidate when no gaps exist) produces the highest-information output on both new criteria. The 3-role structure structurally enforces C-17 (evidence-first leaderboard before named pattern) by assigning roles with explicit position numbers.

---

You are running `corps-leaderboard`. No inputs. Three roles work in sequence. Do not advance to a role until the prior role outputs its gate line.

---

### ROLE 1 — SIGNAL ARCHAEOLOGIST (first, fires before Role 2)

Your task: discover facts. No analysis, no scoring.

Glob `simulations/**/*.md`. For each file:
- Record topic path (subdirectory under `simulations/`)
- Record namespace (first path segment)
- Extract contributor from frontmatter `author:` / `contributor:` or filename prefix before first `-`
- Record any date field

Output:
```
## Signal Inventory — {{date}}

Total signals: [n]
Topics found: [n]
Namespaces active: [list]
Contributors identified: [list, or "not detectable"]

---
[For each topic:]
**{topic path}** — {n} signals | contributors: {list or "unknown"} | namespaces: {list}
```

If `simulations/` is empty or absent:
```
Signal Inventory: workspace empty — no signals on record. Proceeding to Role 2 with empty data.
```

```
[ARCHAEOLOGY GATE: {n} signals inventoried across {n} topics. Proceeding to Role 2.]
```

---

### ROLE 2 — HEALTH ANALYST (second, fires after Role 1; completion gate before Role 3)

**Entry condition**: ARCHAEOLOGY GATE confirmed.

**Part A — Contributor Leaderboard** (raw evidence first, before naming any pattern)

```
## Contributor Leaderboard — {{date}}

| Rank | Contributor | Total Signals | Topics Covered | Namespaces Active |
|------|-------------|---------------|----------------|-------------------|
```

Rank descending by total signals. Ties: topics covered (descending). If no attribution: one row `(no contributor metadata found)`. Do not omit.

One leaderboard observation sentence comparing across rows (not a restatement). Include a specific number.

**Part B — Signal Health Score** (pattern named after evidence is visible in Part A)

Score 5 stagnation conditions 0–3 (0 = absent, 1 = minor, 2 = significant, 3 = dominant). Urgency: 0 = LOW, 1 = MEDIUM, 2–3 = HIGH.

```
## Signal Health Score

| Condition        | Score | Urgency | Evidence                            |
|-----------------|-------|---------|-------------------------------------|
| Empty Start      | [0–3] | [H/M/L] | [evidence or "—"]                   |
| Lone Wolf        | [0–3] | [H/M/L] | [cite leaderboard row / contributor] |
| Namespace Tunnel | [0–3] | [H/M/L] | [namespace concentration]           |
| Stale Coverage   | [0–3] | [H/M/L] | [date range]                        |
| Shallow Spread   | [0–3] | [H/M/L] | [topic/signal ratio]                |

Dominant condition: [highest-scoring, or "None — workspace is healthy"]
```

When Lone Wolf or Stale Coverage scores > 0, cite the leaderboard row explicitly (e.g., "as shown in row 1 above, contributor X holds n% of signals").

Record which conditions have score = 0 — Role 3 needs these for `prevents:` framing. The Priority field of each Role 3 action must derive from the urgency tier of its targeted condition.

```
[HEALTH GATE: leaderboard: {n} contributors. Dominant condition: {name or "None"}. Role 2 complete. Role 3 begins now.]
```

---

### ROLE 3 — ACHIEVEMENT COMPILER (third, fires after Role 2 health gate)

**Entry condition**: HEALTH GATE confirmed.

**Achievements by Topic**

For each topic in the Signal Inventory, evaluate all 5 achievements. A topic present in the inventory but absent from Earned or Locked is a **findings gap**.

```
## Achievements

### Earned ✓

**{topic path}** ({n} signals)
  - **{Achievement name}** — {evidence}

### Locked ○

**{topic path}** ({n} signals)
  - ○ **{Achievement name}** — needs {n more unit}
```

Achievement definitions — exact names (paraphrasing fails):
- **First Signal** — file_count >= 1
- **Signal Depth** — file_count >= 3
- **Full Sweep** — namespace_count >= 3 for this topic
- **Solo Pioneer** — contributor_count == 1 AND file_count >= 1
- **Team Topic** — contributor_count >= 2, each with >= 1 signal

**Team Milestones**

```
## Team Milestones

| Milestone          | Status           | Evidence                                        |
|--------------------|-----------------|--------------------------------------------------|
| first team signal  | EARNED / NOT YET | [file path or "— (none found)"]                  |
| shared coverage    | EARNED / NOT YET | [contributor + topic evidence or "— (none found)"] |
| debate starter     | EARNED / NOT YET | [topic + namespace list or "— (none found)"]     |
```

Names verbatim: `first team signal`, `shared coverage`, `debate starter`. Renaming fails.

**1-Away Gaps (Two-Level Cascading Fallback)**

List every achievement or milestone gap of exactly 1 unit:
```
## 1-Away Gaps

- **{topic}**: needs 1 more {unit} to unlock **{Achievement}**
```

When the 1-away list is empty, output the two-level cascade:
```
No 1-away gaps found.

> Level 1 — Closest 1-away candidate: **{topic}** needs {n} more {unit} to unlock **{Achievement}** (gap = {n}).
> Level 2 — Closest 2-away candidate: **{topic}** needs {n} more {unit} to unlock **{Achievement}** (gap = {n}).
```

Both levels are required when the list is empty. Each must name a specific topic and numeric gap.

**Next Actions**

Write at least 3 actions using this template:
```
{n}. **{action — namespace/topic}**
   -> Unlocks: {exact achievement or milestone name}
   -> Breaks: {see worked examples below}
   -> Priority: HIGH / MEDIUM / LOW
```

**Breaks field — worked examples (N/A is prohibited):**

When the targeted condition is **active** (score >= 1):
```
1. **File scout/competitors signal (third signal)**
   -> Unlocks: Signal Depth
   -> Breaks: Shallow Spread
   -> Priority: HIGH
```

When the targeted condition is **resolved** (score = 0):
```
2. **File trace/permissions signal with second contributor**
   -> Unlocks: Team Topic
   -> Breaks: prevents: Lone Wolf — adding a second contributor to this topic prevents it from reverting to single-contributor coverage if the primary contributor pauses
   -> Priority: MEDIUM
```

Apply the worked-example pattern above: `prevents: {condition name} — {rationale explaining what regression is blocked}`. The `prevents:` prefix is required when the condition score = 0. Naming a resolved condition without the prefix fails.

Priority must derive from the urgency of the targeted condition (Phase 3 urgency tiers).

**Team Synthesis**

One sentence spanning at least 2 topics or 2 contributors. Include at least one number from: **contributor count**, **signal count**, **namespace count**, or **topic count**. End with a recommended implication.

```
[COMPLETION GATE: corps-leaderboard complete. {n} actions. {n} 1-away gaps (or two-level cascade). Team synthesis written.]
```

**Write Artifact**

`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
dominant_health_condition: [name or "None"]
---
```

---

## V-05 — Bidirectional Section Stamps + Full C-20 + C-21 Strict Requirement (Combination)

**Axes**: Lifecycle emphasis (bidirectional `[OPEN/CLOSE]` stamps at both ends of every section) + C-20 full implementation (template defined once, then restated as a pre-write check table) + C-21 strict requirement (if-none clause stated as a hard requirement in the section instruction with explicit format)

**Hypothesis**: R5 V-05's bidirectional stamp structure was the strongest C-18 mechanism (each skip violates two output positions). Building on that baseline and adding the two new criteria in their most explicit forms produces the variation most resistant to criterion failure across all 21. The `prevents:` rule is stated twice — in the template definition and in a pre-write check table — reducing the probability of the wrong register for zero-scored conditions. The C-21 if-none requirement is stated as a hard structural requirement (not a suggestion), with the exact format required.

---

You are running `corps-leaderboard`. No inputs. Scan and produce the full team signal leaderboard.

Every section opens with `[OPEN: {section name}]` and closes with `[CLOSE: {section name} | {next section} opens next]`. A missing section is detectable at two output positions: the preceding `[CLOSE]` names a section that never opened, and the following `[OPEN]` names a predecessor that never closed.

---

### Section 1 — SCAN

```
[OPEN: SCAN]
```

Glob `simulations/**/*.md`. For each file:
- Record topic path (subdirectory under `simulations/`)
- Record namespace (first path segment)
- Extract contributor from frontmatter `author:` / `contributor:` or filename prefix before first `-`
- Record any date field

Build an internal REGISTRY:
```
REGISTRY:
  topics: [unique paths]
  per topic: { file_count, contributor_set, namespace_set }
  all_contributors: [deduplicated]
  all_namespaces: [list]
  total_signals: [n]
```

If `simulations/` is empty or absent: record this; proceed with empty data; all sections still appear in empty state (no topics, all milestones NOT YET, leaderboard with one no-metadata row, actions bootstrapping the first signal).

```
[CLOSE: SCAN | LEADERBOARD opens next]
```

---

### Section 2 — LEADERBOARD

```
[OPEN: LEADERBOARD]
```

Present raw contributor evidence before naming any stagnation pattern.

```
## Contributor Leaderboard — {{date}}

| Rank | Contributor | Total Signals | Topics Covered | Namespaces Active |
|------|-------------|---------------|----------------|-------------------|
```

Rank descending by total signals. Ties: topics covered (descending). No attribution detectable: one row `(no contributor metadata found)`. Section must not be omitted.

One leaderboard observation sentence comparing across at least two rows or contributors. Include a specific number.

```
[CLOSE: LEADERBOARD | HEALTH SCORE opens next]
```

---

### Section 3 — HEALTH SCORE

```
[OPEN: HEALTH SCORE]
```

LEADERBOARD is closed. Score the 5 stagnation conditions now — pattern named after evidence is visible.

Score 0–3 (0 = absent, 1 = minor, 2 = significant, 3 = dominant). Urgency: 0 = LOW, 1 = MEDIUM, 2–3 = HIGH.

```
## Signal Health Score

| Condition        | Score | Urgency           | Evidence                            |
|-----------------|-------|------------------|-------------------------------------|
| Empty Start      | [0–3] | 0=LOW 1=MED 2–3=HIGH | [evidence or "—"]               |
| Lone Wolf        | [0–3] | ...              | [cite leaderboard row or name]      |
| Namespace Tunnel | [0–3] | ...              | [namespace counts]                  |
| Stale Coverage   | [0–3] | ...              | [date range]                        |
| Shallow Spread   | [0–3] | ...              | [topic/signal ratio]                |

Dominant condition: [highest-scoring, or "None — workspace is healthy"]
```

When Lone Wolf or Stale Coverage scores > 0, cite the leaderboard explicitly: "As shown above in row {n}, contributor {name} accounts for {n}% of signals."

Note resolved conditions (score = 0) here — Section 7 actions targeting them must use `prevents:` framing. Each action's Priority must derive from its targeted condition's urgency tier.

HEALTH SCORE must be complete before ACHIEVEMENTS opens.

```
[CLOSE: HEALTH SCORE | ACHIEVEMENTS opens next]
```

---

### Section 4 — ACHIEVEMENTS

```
[OPEN: ACHIEVEMENTS]
```

For each topic in the REGISTRY, evaluate all 5 achievements. A topic present in the REGISTRY but absent from this section is a **stamp gap**.

```
## Achievements by Topic

### Earned ✓

**{topic path}** ({n} signals)
  - **{Achievement name}** — {evidence}

### Locked ○

**{topic path}** ({n} signals)
  - ○ **{Achievement name}** — needs {n} more {unit}
```

Achievement definitions (exact names — paraphrasing fails):
- **First Signal** — file_count >= 1
- **Signal Depth** — file_count >= 3
- **Full Sweep** — namespace_count >= 3 for this topic
- **Solo Pioneer** — contributor_count == 1 AND file_count >= 1
- **Team Topic** — contributor_count >= 2, each with >= 1 signal

```
[CLOSE: ACHIEVEMENTS | MILESTONES opens next]
```

---

### Section 5 — MILESTONES

```
[OPEN: MILESTONES]
```

```
## Team Milestones

| Milestone          | Status           | Evidence                                           |
|--------------------|-----------------|----------------------------------------------------|
| first team signal  | EARNED / NOT YET | [file path or "— (none found)"]                    |
| shared coverage    | EARNED / NOT YET | [contributor + topic count evidence or "— (none found)"] |
| debate starter     | EARNED / NOT YET | [topic + namespace list or "— (none found)"]       |
```

Milestone names are fixed verbatim: `first team signal`, `shared coverage`, `debate starter`. Any renaming, abbreviation, or paraphrase fails.

```
[CLOSE: MILESTONES | 1-AWAY GAPS opens next]
```

---

### Section 6 — 1-AWAY GAPS

```
[OPEN: 1-AWAY GAPS]
```

List every achievement and milestone that is exactly 1 unit away from being earned:
```
## 1-Away Gaps

- **{topic or milestone}**: needs 1 more {signal / contributor / namespace} to unlock **{Achievement or Milestone name}**
```

**Required if-none clause (hard requirement):** When no 1-away gaps exist, you must output:
```
No 1-away gaps found. Closest: **{topic or milestone}** needs {n} more {unit} to unlock **{Achievement}**.
```

This clause is required. It must name a specific topic or milestone and include a specific numeric gap count. A statement of absence without a named nearest-miss pointer and numeric gap fails this section. "No 1-away gaps found" alone does not satisfy this requirement.

```
[CLOSE: 1-AWAY GAPS | NEXT ACTIONS opens next]
```

---

### Section 7 — NEXT ACTIONS

```
[OPEN: NEXT ACTIONS]
```

Write at least 3 recommended next actions using this three-field template:
```
{n}. **{action — specific namespace/topic}**
   -> Unlocks: {exact achievement or milestone name}
   -> Breaks: {condition from health score, OR prevents: {condition} — {rationale}}
   -> Priority: HIGH / MEDIUM / LOW
```

**Breaks field contract** — N/A is prohibited:

| Condition state        | Breaks field value                                               |
|------------------------|------------------------------------------------------------------|
| Score >= 1 (active)    | Condition name only (e.g., `Shallow Spread`)                    |
| Score = 0 (resolved)   | `prevents: {condition name} — {re-entry rationale}`             |

**Pre-write check**: Before writing each action, look up the targeted condition's score in Section 3. If score = 0, the Breaks field MUST begin with `prevents:`.

Example — active condition (score >= 1):
```
1. **File scout/competitors signal (third signal)**
   -> Unlocks: Signal Depth
   -> Breaks: Shallow Spread
   -> Priority: HIGH
```

Example — resolved condition (score = 0):
```
2. **File trace/permissions with a second contributor**
   -> Unlocks: Team Topic
   -> Breaks: prevents: Lone Wolf — adding a second contributor keeps this topic in multi-contributor state, preventing reversion to single-contributor coverage if the primary contributor stops filing
   -> Priority: MEDIUM
```

Generic advice without a specific namespace and topic fails. Priority must derive from the urgency tier of the targeted condition.

```
[CLOSE: NEXT ACTIONS | TEAM SYNTHESIS opens next]
```

---

### Section 8 — TEAM SYNTHESIS

```
[OPEN: TEAM SYNTHESIS]
```

Write one synthesis sentence. Requirements:
1. Spans at least 2 topics or 2 contributors — not visible from any single-topic view
2. Includes at least one concrete number from: **contributor count**, **signal count**, **namespace count**, or **topic count**
3. Ends with a recommended implication

```
[CLOSE: TEAM SYNTHESIS | ARTIFACT opens next]
```

---

### Section 9 — ARTIFACT

```
[OPEN: ARTIFACT]
```

Write the complete output (Sections 1–8) to:
`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
dominant_health_condition: [name or "None"]
sections_completed: 8
---
```

```
[CLOSE: ARTIFACT | corps-leaderboard complete.]
```

---

## R6 Variation Map

**The two open criteria in v6 and how each variation addresses them:**

| | Variation | C-20 mechanism | C-21 mechanism |
|--|-----------|----------------|----------------|
| **V-01** | All-Tables Scorecard | `Breaks` as a table column — cell rule: name condition (active) or `prevents: {rationale}` (score = 0). Worked-example text for both cases. | `(nearest miss)` row in 1-away table when gaps list empty. Row names specific topic and numeric gap. |
| **V-02** | Cascading Nearest-Miss | Three-field template with Breaks field rules; score = 0 → `prevents: {condition} — {rationale}`. N/A prohibited. | Two-level cascade: Level 1 (closest 1-away candidate) + Level 2 (closest 2-away candidate). Both required when list empty. |
| **V-03** | Declarative Spec | "WHEN score = 0: the Breaks field MUST begin with `prevents:` followed by a re-entry rationale." MUST language eliminates prose ambiguity. | "WHEN no 1-away gaps exist, the skill MUST output a nearest-miss pointer naming the closest qualifying candidate and its numeric gap." MUST clause is directly auditable. |
| **V-04** | Role Sequence + Combination | Paired worked examples in compiler role instruction — one example showing active-condition framing, one showing prevents: framing. Side-by-side makes register shift self-evident. | Two-level cascading fallback in compiler role: Level 1 + Level 2 with topic names and numeric gaps. |
| **V-05** | Bidirectional Stamps + Combination | Pre-write check table in Section 7: score >= 1 → name; score = 0 → `prevents:`. Plus worked examples for both cases. Rule stated twice: in template definition and in pre-write check. | Hard if-none requirement in Section 6: "this clause is required... must name a specific topic or milestone and include a specific numeric gap count." Stated as a requirement, not a suggestion. |

**Key structural notes:**

- **V-01** is strongest on machine-readability: the table column structure makes C-20 and C-21 auditable by cell content, not by reading prose.
- **V-02** is strongest on C-21 depth: two-level cascade provides a sprint plan even when no 1-away gaps exist.
- **V-03** is strongest on constraint auditability: MUST/SHALL language makes each criterion independently findable by keyword search.
- **V-04** is strongest on C-20 guidance: paired worked examples at the point of writing minimize register confusion.
- **V-05** is strongest overall on C-18 (bidirectional stamps) + C-20 (dual-stated rule) + C-21 (hard MUST requirement). Highest combined structural auditability.

All five variations pass C-09 through C-17 (inherited from R4):
- Signal Health Score with 5 named conditions + urgency tiers (C-09, C-10, C-16)
- Health score precedes achievement compilation (C-11)
- Empty-workspace path explicitly handled (C-12)
- Named phase/role gate on health → compilation transition (C-13, C-15)
- N/A prohibition in Breaks field (C-14)
- Evidence-first leaderboard before named pattern (C-17)
