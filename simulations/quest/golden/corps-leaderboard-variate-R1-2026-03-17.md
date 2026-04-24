---
skill: quest-variate
skill_target: corps-leaderboard
round: 1
date: 2026-03-17
rubric_version: 1
---

# Variate R1 — corps-leaderboard

5 complete prompt body variations for the `corps-leaderboard` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Output format (achievement grid table vs badge list vs prose dashboard) | V-01, V-05 |
| Phrasing register (technical-imperative vs conversational/game-sprint framing) | V-02 |
| Lifecycle emphasis (implicit flow vs explicit named phase gates) | V-03, V-05 |
| Role sequence (archaeologist first vs skeptic before leaderboard) | V-04 |
| Inertia framing (stagnation pattern named before recommendations; cost of no signal discipline) | V-04 |

---

## V-01 — Output Format: Achievement Grid Table

**Axis**: Output format
**Hypothesis**: A matrix layout — rows = topics, columns = achievement types — makes C-01 and
C-02 mechanically auditable: every discovered topic is a row by construction, so omissions
are visible as missing rows rather than silent gaps, and every achievement column is checked
per row. The grid also satisfies C-06 (earned vs locked) through column-level cell markers
(checkmark vs circle) without requiring separate sections. The risk is that C-09 and C-10
synthesizing insights are harder to produce from a grid — a closing team-insight paragraph
is required to compensate.

---

You are running `corps-leaderboard` for this workspace. No inputs — scan and compute from
workspace state.

**Step 1 — Scan**

Glob `simulations/` recursively. List every subdirectory that contains at least one `.md`
file as a discovered topic. For each topic, record:

- File count (total `.md` files in that path)
- Namespace (first path segment under `simulations/`)
- Contributor identities, if extractable from frontmatter (`author:`, `contributor:`) or
  filename prefixes before the first `-`
- Any date fields detectable in frontmatter or filename

Produce an internal working record (not written to final output):

```
SCAN RECORD (internal)
Topics found: [n]
  - [topic path] — [n] signals — contributors: [list or "unknown"] — namespace: [ns]
Contributors found (deduplicated): [list or "not detectable"]
Namespaces active: [list]
Total signals: [n]
```

If `simulations/` is empty or absent, record this explicitly and proceed with no data.
All output sections will still be produced.

**Step 2 — Achievement Grid**

Build a Markdown table. One row per discovered topic.

| Topic | Signals | First Signal | Signal Depth | Full Sweep | Solo Pioneer | Team Topic | Top Contributor |
|-------|---------|-------------|-------------|-----------|-------------|-----------|----------------|

Column rules:
- **Topic**: Path relative to `simulations/`, e.g. `scout/competitors`
- **Signals**: Count of `.md` files in that topic path
- **First Signal** through **Team Topic**: Each is one of:
  - `[name]` (earned — badge name only, no extra text)
  - `○` (locked — condition not met)
  - `—` (cannot determine — metadata unavailable; note why)
- **Top Contributor**: Contributor with most signals for this topic, or `unknown`

Achievement definitions applied to each cell:
- **First Signal** — earned when signal count >= 1
- **Signal Depth** — earned when signal count >= 3
- **Full Sweep** — earned when signals span >= 3 distinct namespaces for this topic
- **Solo Pioneer** — earned when contributor count == 1 AND signal count >= 1
- **Team Topic** — earned when contributor count >= 2 with >= 1 signal each

Every discovered topic must appear as a row. A topic present in the scan but absent from
the table fails C-01. If `simulations/` is empty, produce the table header only and note:
"No topics discovered — all achievement columns empty."

**Step 3 — Team Milestones**

Write a milestones section using this exact structure:

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|----------|
| first team signal | [EARNED / NOT YET] | [file path or "—"] |
| shared coverage | [EARNED / NOT YET] | [2+ contributors each with 2+ topics, or "—"] |
| debate starter | [EARNED / NOT YET] | [topic with signals from 2+ namespaces, or "—"] |
```

Use the milestone names verbatim as shown above. Renaming, abbreviating, or paraphrasing any
milestone name is an error. Each evidence cell must be non-empty — "—" without explanation
counts as a gap only if no evidence exists; in that case append "(none found)".

**Step 4 — Contributor Leaderboard**

```
## Contributor Leaderboard — {{date}}

| Rank | Contributor | Total Signals | Topics Covered | Namespaces Active |
|------|-------------|---------------|----------------|-------------------|
| 1 | [name] | [n] | [n] | [list] |
| 2 | ... |
```

Rank in descending order by total signals. If contributor metadata is not extractable from
any frontmatter or filename patterns, produce one explicit row:

`| — | (no contributor metadata found) | — | — | — |`

Do not omit this section regardless of workspace state.

**Step 5 — 1-Away Gap Detection**

Scan for any achievement or milestone that is exactly one step away from being earned:

```
## Almost There

- [Topic or Milestone]: needs [exact count] more [signal / contributor / namespace] to unlock **[Achievement name]**
```

If no gap is within 1 step, write: "No single-step unlocks available."
Do not write generic advice ("keep adding signals"). Name the topic and the target achievement.

**Step 6 — Next Actions**

Write at least 3 recommended next actions. Each must name:
1. A specific namespace and topic (e.g., `scout/competitors`)
2. The exact achievement or milestone name it unlocks (from the defined set)

```
## Next Actions

1. **[Action — specific namespace/topic]** → unlocks **[Achievement or Milestone name]**
   _Why_: [one sentence — what gap this closes, grounded in Step 2 or Step 3 data]

2. ...

3. ...
```

"Add more signals" or "increase namespace coverage" without a specific target fails.

**Step 7 — Team Insight**

Write one sentence that draws a cross-topic or cross-contributor conclusion not visible from
any single-topic row. Use at least one specific number and one specific name (topic or
contributor). Close with a recommended implication.

Example: "Alice spans 4 topics — highest breadth on the team — suggesting she is the natural
owner of any unlock requiring multi-namespace coverage."

**Step 8 — Write Artifact**

Write the complete output to:
`simulations/corps/leaderboard-{{date}}.md`

Frontmatter:
```yaml
---
skill: corps-leaderboard
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
---
```

---

## V-02 — Phrasing Register: Conversational Sprint-Board

**Axis**: Phrasing register
**Hypothesis**: Framing the leaderboard as a weekly sprint-board readout — with playful badge
language and first-person team framing ("here's how we did") — increases engagement for a
team audience while preserving the structural completeness required by C-01 through C-05.
Conversational language naturally produces C-09 insights as closing remarks. The risk is
C-02 precision: badge names must still match the defined set exactly. This variation front-
loads the leaderboard (C-04) as the hook, then walks through topic achievements, milestones,
and actions — mimicking a standup readout rather than a structured audit.

---

You are running `corps-leaderboard`. No inputs needed — you will scan the workspace yourself
and produce this week's team signal report.

Start by globbing `simulations/` for all `.md` files. Collect every topic path (subdirectories
with at least one `.md` file), note signal counts, and extract any contributor attribution
available in frontmatter (`author:`, `contributor:`) or filename prefixes. If the workspace
is empty, say so up front and still produce all sections — just with empty or "NOT YET" values.

---

**Sprint Signal Report — {{date}}**

Open with one sentence: "Scanned on {{date}} — [n] active topics, [n] contributors identified."

Then jump straight to the leaderboard. The team wants to see who contributed first.

```
## Who's Leading

| Rank | Contributor | Signals This Sprint | Topics | Active Namespaces |
|------|-------------|---------------------|--------|-------------------|
| 1 | [name] | [n] | [n] | [list] |
...
```

Rank by total signals descending. If no contributor metadata is in the workspace, write one
row: `1. (no attribution found) — signals counted, names not available`. Never omit this table.

---

**What the Team Has Unlocked**

Show the badge board. Group topics into two buckets:

```
### Earned Badges ✓

**[topic path]** — [n] signals
  ✓ First Signal
  ✓ Signal Depth  (if earned)
  [list all earned badges]

**[topic path]** — [n] signals
  ✓ ...

### Locked Badges ○

**[topic path]** — [n] signals
  ○ Signal Depth — need [n] more signals
  ○ Team Topic — need 1 more contributor
  [list locked badges and exact gap]
```

Every topic from the scan must appear in one group. A topic with no earned badges goes in
the Locked group with a note explaining what is needed. Do not omit any discovered topic.

Badge definitions (use these exact names — do not paraphrase):
- **First Signal** — 1+ signal files for this topic
- **Signal Depth** — 3+ signal files for this topic
- **Full Sweep** — signals span 3+ distinct namespaces for this topic
- **Solo Pioneer** — exactly 1 contributor with 1+ signal for this topic
- **Team Topic** — 2+ contributors each with 1+ signal for this topic

---

**Team Milestones**

Has the team as a whole hit these three? Use their exact names — do not rename them:

- **first team signal**: Has any signal been filed at all? ✓ earned / ○ not yet — evidence: [file path or "none"]
- **shared coverage**: Have 2+ contributors each touched 2+ topics? ✓ earned / ○ not yet — evidence: [contributor names + topic counts, or "none"]
- **debate starter**: Has any topic gotten signals from 2+ namespaces? ✓ earned / ○ not yet — evidence: [topic path + namespace list, or "none"]

For any NOT YET milestone, say what it would take to earn it.

---

**Unlock These Next**

Pick the 3 highest-leverage things the team could do. For each, name exactly what to do
and which badge or milestone it unlocks:

> **Do this**: [Specific action — which namespace, which topic, who could do it]
> **Unlocks**: [Exact badge or milestone name]
> **Gap**: [One sentence on why this move has the highest payoff right now]

No vague advice. "File a signal" needs a namespace and topic: `scout/competitors`, `flow/trigger`, etc.

---

**Almost There**

Any badge or milestone that needs just one more action? List each with the exact gap:

- [Topic or Milestone] — needs [1 more signal / 1 more contributor / 1 more namespace] to unlock **[Badge name]**

If nothing is 1 step away, write: "Nothing on the 1-away list right now."

---

**One thing the numbers tell us**

Close with one sentence drawing a conclusion that spans topics or contributors — something
you can only see from the full scan, not from any single topic. Name specific numbers and names.
End with a recommended implication.

Example: "Three topics each have exactly 2 signals — a single sprint focused on depth rather
than breadth could unlock Signal Depth across all three simultaneously."

---

**Write the artifact**

Save to: `simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
---
```

---

## V-03 — Lifecycle Emphasis: Explicit Phase Gates

**Axis**: Lifecycle emphasis
**Hypothesis**: Requiring explicit gate confirmation statements before advancing to the next
phase forces completeness on C-01 (scan gate ensures no silent omissions), C-03 (milestones
gate requires all three before advancing), and C-04 (leaderboard gate rejects omitted sections).
Each gate produces a checkpoint the subsequent phase consumes, making it mechanically hard
to advance with incomplete data. This variation is strongest on sparse workspaces where the
model might otherwise produce a leaderboard with no underlying topic scan.

---

You are running `corps-leaderboard`. No arguments — the skill scans and computes from
workspace state.

Work through the phases in order. State the gate confirmation before advancing to the next
phase. If an entry condition is not met, output a diagnostic and halt rather than proceeding
with incomplete data.

---

### PHASE 1 — SCAN

**Entry condition**: `simulations/` directory accessible.

Glob `simulations/**/*.md`. For every file found:
- Note the topic path (subdirectory under `simulations/`, e.g. `scout/competitors`)
- Record the namespace (first path segment)
- Extract contributor identity from frontmatter `author:` or `contributor:` fields, or from
  filename prefix patterns (contributor name before the first `-`)
- Note any date field

Build an internal registry:
```
REGISTRY (internal):
  topics: [list of unique topic paths]
  per topic: { file_count, contributor_set, namespaces }
  contributors_all: [deduplicated across all topics]
  namespaces_active: [list]
  total_signals: [n]
```

**SCAN GATE**: If `simulations/` is empty or absent, output:
> "SCAN GATE: workspace is empty — no signal artifacts found. All achievement sections will
> show as empty. All milestones NOT YET. Proceeding with empty registry."
Then continue with empty data. Do not halt.

**SCAN GATE**: If files are found, output:
> "SCAN GATE: [n] signals found across [n] topics, [n] namespaces, [n or 'unknown'] contributors.
> Registry built. Proceeding to Phase 2."

---

### PHASE 2 — COMPUTE ACHIEVEMENTS

**Entry condition**: SCAN GATE confirmed.

For each topic in the registry, evaluate all 5 achievements:

| Achievement | Condition |
|-------------|-----------|
| First Signal | topic file_count >= 1 |
| Signal Depth | topic file_count >= 3 |
| Full Sweep | len(topic namespaces) >= 3 |
| Solo Pioneer | len(topic contributor_set) == 1 AND file_count >= 1 |
| Team Topic | len(topic contributor_set) >= 2 AND each contributor has >= 1 signal |

Output:

```
## Achievements by Topic

### Earned

[For each topic with >= 1 earned achievement:]
**[topic path]** ([n] signals)
  - [Achievement name]: [evidence — file count, contributor count, namespace list]

### Locked

[For each topic with >= 1 locked achievement:]
**[topic path]** ([n] signals)
  - ○ [Achievement name]: needs [specific gap]

[Topics that appear in neither — no achievements earned, none locked — should not exist;
every topic has at least First Signal either earned or locked. If truly nothing to show,
write: "[topic path] — (n = 0 signals)"]
```

Every topic from the registry must appear. Omitting a topic is a PHASE 2 gate failure.

**COMPUTE GATE**: Output:
> "COMPUTE GATE: [n] topics evaluated. [n] achievements earned across all topics. [n] achievements
> locked. Proceeding to Phase 3."

---

### PHASE 3 — TEAM MILESTONES

**Entry condition**: COMPUTE GATE confirmed.

Evaluate all three milestones against the full registry. Use their exact names as shown here:

```
## Team Milestones

**first team signal**
  Status: [EARNED / NOT YET]
  Condition: any signal file present anywhere in simulations/
  Evidence: [file path of any signal, or "none"]
  To earn: [what must happen, or "—"]

**shared coverage**
  Status: [EARNED / NOT YET]
  Condition: >= 2 contributors each present in >= 2 distinct topic paths
  Evidence: [contributor names + topic lists, or "none"]
  To earn: [what must happen, or "—"]

**debate starter**
  Status: [EARNED / NOT YET]
  Condition: >= 1 topic with signals from >= 2 distinct namespaces
  Evidence: [topic path + namespace list, or "none"]
  To earn: [what must happen, or "—"]
```

Milestone name renaming, abbreviation, or paraphrase fails C-03.

**MILESTONES GATE**: Output:
> "MILESTONES GATE: [n/3] milestones earned (first team signal: [E/N], shared coverage: [E/N],
> debate starter: [E/N]). Proceeding to Phase 4."

---

### PHASE 4 — CONTRIBUTOR LEADERBOARD

**Entry condition**: MILESTONES GATE confirmed.

```
## Contributor Leaderboard — {{date}}

| Rank | Contributor | Total Signals | Topics Covered | Namespaces Active |
|------|-------------|---------------|----------------|-------------------|
| 1 | [name] | [n] | [n] | [list] |
| 2 | ...
```

Rank descending by total signals. Ties broken by topics covered.

If contributor attribution is unavailable from frontmatter and filenames, write one explicit row:
`| — | (no contributor metadata found) | — | — | — |`

Do not omit this section.

**LEADERBOARD GATE**: Output:
> "LEADERBOARD GATE: [n] contributors ranked. Attribution source: [frontmatter / filename /
> not available]. Proceeding to Phase 5."

---

### PHASE 5 — RECOMMENDATIONS AND GAPS

**Entry condition**: LEADERBOARD GATE confirmed.

**1-Away Gaps**

Check every achievement and milestone for gaps of exactly 1 unit:

```
## Almost There (1-Away)

- [Topic or Milestone]: needs [1 more signal / 1 more contributor / 1 more namespace]
  to unlock **[Achievement name]**

[If nothing is within 1 step:]
No single-step unlocks detected. Closest gap: [topic] needs [n] more [unit] for **[Achievement]**.
```

**Next Actions**

Write at least 3 actions. Each must pass this test before being written:
- Does it name a specific namespace and topic?
- Does it name the exact achievement or milestone (by defined name) it unlocks?

```
## Recommended Next Actions

1. **[Action — namespace/topic]**
   → Unlocks: **[Achievement or Milestone name]**
   Rationale: [one sentence grounded in Phase 2 or Phase 3 gaps]

2. ...

3. ...
```

**Team Insight**

One sentence, cross-topic or cross-contributor. Not a per-topic statistic — a conclusion
drawn from comparing across topics or contributors. Use a specific number and name. Close
with a recommended implication.

**RECOMMENDATIONS GATE**: Output:
> "RECOMMENDATIONS GATE: [n] next actions written. [n] 1-away gaps identified. Team insight recorded."

---

### PHASE 6 — WRITE ARTIFACT

**Entry condition**: RECOMMENDATIONS GATE confirmed.

Write the complete output (all phases) to:
`simulations/corps/leaderboard-{{date}}.md`

Frontmatter:
```yaml
---
skill: corps-leaderboard
date: {{date}}
phases_completed: 6
topics_scanned: [n]
milestones_earned: [n]/3
contributors_detected: [n or "unknown"]
---
```

---

## V-04 — Role Sequence + Inertia Framing (Combination)

**Axis**: Role sequence (archaeologist first, inertia diagnostician second, compiler third)
+ inertia framing (stagnation pattern named before leaderboard; actions explicitly anti-inertia)
**Hypothesis**: Running a signal archaeologist role first produces a grounded inventory that
the compiler draws from, preventing fabricated topic paths. Inserting an inertia diagnostician
role between archaeology and compilation forces the model to name the stagnation pattern before
it builds the leaderboard — this primes C-10 (stagnation pattern + anti-inertia action) as a
natural output of the middle role rather than an afterthought. C-05 action quality is highest
in this variation because each action must cite the stagnation pattern it breaks.

---

You are running `corps-leaderboard`. No inputs. Scan and compute from workspace state.

Work through three roles in sequence. Do not advance to a role until the prior role's output
is complete.

---

### ROLE 1 — SIGNAL ARCHAEOLOGIST

Your job: find what exists. No analysis, no judgment — only facts.

Glob `simulations/**/*.md`. For every file:
- Extract the topic path (subdirectory under `simulations/`)
- Note the namespace (first path segment)
- Extract contributor identity from frontmatter `author:` or `contributor:`, or from
  filename prefix conventions
- Note any detectable date

Output an inventory:

```
## Signal Archaeology — {{date}}

Topics discovered: [n]
Namespaces active: [list]
Contributors identified: [list, or "not detectable"]
Total signals: [n]

Signal inventory:
[For each topic:]
  [topic path] — [n] signals — contributors: [list or "unknown"] — namespaces: [list]
```

If `simulations/` is empty or absent:
> "Signal Archaeology: workspace is empty — no signals on record."
Proceed to Role 2 with empty data.

---

### ROLE 2 — INERTIA DIAGNOSTICIAN

Before computing any achievements, assess the team's signal-gathering discipline.

Using the Signal Archaeology inventory, answer these questions in 3-4 sentences:

1. What does the team's current signal activity pattern look like? (One contributor doing
   everything? All signals in one namespace? Almost nothing filed? Broad but shallow?)
2. What decisions are the team flying blind on at current coverage levels?
3. What is the cost of another sprint at this rate — what will remain unknown?

Then state the **Stagnation Pattern** for this workspace. Choose the best match or define
your own if none fits:

- **Empty Start** — no signals yet; team is pre-signal-discipline
- **Lone Wolf** — one contributor accounts for the majority of all signals
- **Namespace Tunnel** — signals exist but are concentrated in 1-2 namespaces; topic coverage
  is narrow
- **Stale Coverage** — signals exist but all are old; no recent activity visible
- **Shallow Spread** — many topics started but none past First Signal; breadth without depth

Output:

```
## Inertia Assessment

Stagnation Pattern: [name]
Evidence: [what in the archaeology supports this — specific numbers, contributor ratio, namespace concentration]
Decision blindspot: [one sentence — what the team doesn't know that signals would reveal]
Cost of inertia: [one sentence — what stays broken if nothing changes this sprint]
```

This assessment will inform Role 3's recommendations. Every next action must tie back to
breaking this named pattern.

---

### ROLE 3 — ACHIEVEMENT COMPILER

Your job: produce the leaderboard and achievement dashboard from the archaeology inventory.
Every recommendation must name the stagnation pattern from Role 2 that it breaks.

**Achievements by Topic**

For each topic in the Signal Archaeology inventory:

```
## Achievements

### Earned ✓

[topic path] ([n] signals)
  ✓ [Achievement name] — [evidence]
  ✓ [Achievement name] — [evidence]

### Locked ○

[topic path] ([n] signals)
  ○ [Achievement name] — needs [specific gap]
  ○ [Achievement name] — needs [specific gap]
```

Every topic from Role 1 must appear. No topic may be omitted.

Achievement definitions (use exact names):
- **First Signal** — >= 1 signal file for this topic
- **Signal Depth** — >= 3 signal files for this topic
- **Full Sweep** — signals span >= 3 distinct namespaces for this topic
- **Solo Pioneer** — exactly 1 contributor, >= 1 signal for this topic
- **Team Topic** — 2+ contributors each with >= 1 signal for this topic

**Contributor Leaderboard — {{date}}**

```
## Contributor Leaderboard

| Rank | Contributor | Total Signals | Topics Covered | Namespaces Active |
|------|-------------|---------------|----------------|-------------------|
```

Rank descending by total signals. If no metadata available: one row stating this explicitly.
Do not omit the section.

**Team Milestones**

Use exact milestone names — no renaming or paraphrasing:

```
## Team Milestones

| Milestone | Status | Evidence |
|-----------|--------|----------|
| first team signal | EARNED / NOT YET | [file path or "—"] |
| shared coverage | EARNED / NOT YET | [evidence or "—"] |
| debate starter | EARNED / NOT YET | [evidence or "—"] |
```

**1-Away Gaps**

```
## Almost There

[Any achievement or milestone gap of exactly 1 unit:]
- [Topic/Milestone]: needs [1 more X] to unlock **[Achievement]**

[If none:]
No single-step unlocks detected.
```

**Anti-Inertia Next Actions**

Write at least 3 actions. Each must:
- Name a specific namespace and topic
- Name the exact achievement or milestone it unlocks
- Include one sentence tying the action back to the **Stagnation Pattern** from Role 2

```
## Anti-Inertia Next Actions

1. **[Action — namespace/topic]**
   → Unlocks: **[Achievement or Milestone name]**
   → Breaks: **[Stagnation Pattern]** because [one sentence]

2. ...

3. ...
```

**Team Insight**

One sentence drawing a cross-topic or cross-contributor conclusion that is not visible from
any single topic. Must differ from the stagnation pattern statement — this is a structural
or positive finding, not a problem statement. Use specific numbers and names.

**Write artifact**

`simulations/corps/leaderboard-{{date}}.md`

```yaml
---
skill: corps-leaderboard
date: {{date}}
stagnation_pattern: [name from Role 2]
topics_scanned: [n]
milestones_earned: [n]/3
---
```

---

## V-05 — Output Format + Lifecycle Emphasis (Combination)

**Axis**: Output format (prose dashboard with required section skeleton) + lifecycle emphasis
(section headers as implicit phase checkpoints that are unfailable to skip)
**Hypothesis**: Providing an explicit section skeleton — every section labeled and required —
forces completeness by construction on C-01 through C-05: each section maps directly to a rubric
criterion, so a missing section requires actively deleting a header, not passively skipping it.
Prose sections (rather than a rigid table) enable richer C-09 cross-contributor insights because
each section ends with a synthesizing sentence rather than a cell value. The combination is
strongest on overall completeness and insight depth; weakest on C-02 auditability (a missing
achievement type is less visible in prose than in a column). To compensate, the achievements
section requires an explicit checklist confirmation before the skill writes the artifact.

---

You are running `corps-leaderboard`. No arguments. Scan the workspace and produce a
team signal dashboard.

Fill every section below in order. Every section is required. A missing or empty section
that is not justified by workspace state is an error.

---

### Section 1 — Scan Summary _({{date}})_

Glob `simulations/**/*.md`. Open with two sentences stating:
1. How many topics were discovered (subdirectories with at least one `.md` file)
2. How many contributors are identifiable and how many signals total

Then list every discovered topic as a flat bullet, one line each:
```
- simulations/[topic path] — [n] signals — contributors: [list or "unknown"] — namespace: [ns]
```

If `simulations/` is empty or absent:
> "Scan complete: no signal artifacts found. Workspace is empty. All sections will show
> empty or NOT YET state."

Every topic listed here must appear in Section 2. A topic present in this list but absent
from Section 2 is a section-2 completeness error.

---

### Section 2 — Achievements by Topic

Write one subsection per discovered topic. Use `####` headers: `#### simulations/[topic path]`.

Each subsection has two labeled paragraphs:

**Earned**: Name every earned achievement as inline bold text with brief evidence.
Check all five: **First Signal**, **Signal Depth**, **Full Sweep**, **Solo Pioneer**, **Team Topic**.
If none earned: "No achievements earned yet."

**Locked**: Name every locked achievement preceded by ○, with the gap quantified (not vague).
Example: "○ Signal Depth — needs 2 more signals". If all earned: "No locked achievements."

Achievement definitions (use exact names — paraphrasing fails):
- **First Signal** — earned when signal count >= 1
- **Signal Depth** — earned when signal count >= 3
- **Full Sweep** — earned when signals span >= 3 distinct namespaces for this topic
- **Solo Pioneer** — earned when contributor count == 1 AND signal count >= 1
- **Team Topic** — earned when contributor count >= 2, each with >= 1 signal

Before closing this section, add a checklist confirmation (not part of the artifact output —
used only internally to verify completeness before writing):
```
[internal] Achievement check:
  [ ] First Signal evaluated for every topic
  [ ] Signal Depth evaluated for every topic
  [ ] Full Sweep evaluated for every topic
  [ ] Solo Pioneer evaluated for every topic
  [ ] Team Topic evaluated for every topic
  [ ] Every topic from Section 1 has a subsection here
```
If any box is unchecked, complete the evaluation before proceeding.

---

### Section 3 — Team Milestones

Write a prose paragraph for each of the three named milestones. Use the exact milestone name
as a bold inline label at the start of each paragraph:

**first team signal**: State earned or not-yet-earned. Give the evidence (file path or "none
found"). If not yet: state exactly what must happen to earn it.

**shared coverage**: State earned or not-yet-earned. Evidence: contributor names and their
topic counts. If not yet: name how many more contributors or topics are needed.

**debate starter**: State earned or not-yet-earned. Evidence: topic path and namespace list
where multiple angles are present. If not yet: name which topic is closest and what is needed.

All three milestones must be present. Do not rename or abbreviate. If `simulations/` is empty,
write all three as NOT YET with "Workspace is empty" as evidence.

---

### Section 4 — Contributor Leaderboard _(week of {{date}})_

Open with one sentence naming the most active contributor (or "no contributor metadata
available" if attribution is not extractable).

Then a table, ranked descending by total signals:

```
| Rank | Contributor | Total Signals | Topics Covered | Namespaces Active |
|------|-------------|---------------|----------------|-------------------|
```

After the table, write one sentence drawing a leaderboard-level observation — not a restatement
of table values but a comparison across rows. Example: "The gap between first and second place
is [n] signals, suggesting [tight competition / one dominant contributor]."

If no attribution is available: one row stating "(no contributor metadata found)", plus:
"Attribution data is unavailable; signal counts are topic-level only."

---

### Section 5 — Almost There (1-Away Gaps)

Write one paragraph naming every achievement or milestone that requires exactly one more action
to unlock. Quantify each gap precisely: "1 more signal", "1 more contributor", "1 more namespace".

If no gaps are within 1 step: "No single-step unlocks available. Closest gap: [topic] needs
[n] more [unit] for **[Achievement]**."

Name every achievement target by its exact defined name.

---

### Section 6 — Next Actions

Write at least 3 next actions as a numbered list. Each must follow this format:

> **[Verb phrase — specific namespace and topic]** → unlocks **[Achievement or Milestone name]**
> [One sentence rationale linking the action to the specific gap from Section 2 or Section 3.]

No generic actions. "File a signal" must be followed by a namespace (`scout`, `flow`, `trace`,
etc.) and a topic name. An action without a specific target fails.

---

### Section 7 — Team Insight

Write one paragraph (2-4 sentences) drawing a cross-topic or cross-contributor conclusion.
This must be a synthesizing statement — not visible from any single-topic subsection in
Section 2. Draw it from patterns across the full scan.

Open with a named insight (one sentence using specific numbers and names). Follow with
supporting evidence (one sentence). Close with a recommended implication for the team.

---

### Section 8 — Write Artifact

Write the complete output (Sections 1-7) to:
`simulations/corps/leaderboard-{{date}}.md`

Frontmatter:
```yaml
---
skill: corps-leaderboard
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
sections_completed: 7
---
```
