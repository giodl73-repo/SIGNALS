---
skill: quest-variate
skill_target: corps-achievements
round: 7
date: 2026-03-16
rubric_version: 6
---

# Variate R7 — corps-achievements

5 complete prompt body variations for the `corps-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R6 established C-21/C-22/C-23 as baseline structural requirements. R7 explores phrasing
register, output ordering, and inertia framing as the primary variation axes — all variations
satisfy C-21/C-22/C-23 but differ in HOW they present and sequence the output.

---

## Variation Axes Selected

| Axis | Hypothesis | Used In |
|------|------------|---------|
| Phrasing register: formal/technical (command language, no hedging) | Uniform imperative voice locks every gate into the same enforcement tone — a gate cannot soften into a suggestion | V-01, V-04 |
| Phrasing register: conversational/narrative (team-report voice) | Narrative framing increases weekly adoption while still satisfying all structural criteria | V-02, V-05 |
| Lifecycle ordering: milestone-first (milestones before per-topic achievements) | Computing milestones before per-topic achievements establishes team-level context that frames individual data, reducing the risk of per-topic analysis losing the forest for the trees | V-03, V-04 |
| Formal + milestone-first (combination) | Formal voice + milestone-first order creates the most auditable output: every section names what the team achieved before what any topic achieved | V-04 |
| Conversational + inertia framing prominent throughout (combination) | Humanized narration + explicit cost-of-inertia woven into every section produces the most action-motivating output | V-05 |

---

## Shared Resources (all variations reference these)

### Stagnation Pattern Registry

All variations draw anti-inertia actions from this registry. Use the label syntax
`[PATTERN_LABEL from registry]` in action rows.

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no team breadth or coverage diversity |
| NAMESPACE_MOAT | All signals from one namespace — no cross-namespace synthesis possible |
| SPRINT_FREEZE | No new signals added in the current sprint window — momentum stalled |
| SHALLOW_POOL | Multiple topics with <3 signals each — Signal Depth unreached across the board |
| ORPHAN_TOPIC | Topics exist with no contributor metadata — ownership and accountability unknown |

### Weighted Scoring Formula

All variations use this formula for the contributor leaderboard (C-16):

```
Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)
```

Where:
- **Signals** = total signal files attributed to this contributor
- **Topics** = count of distinct topics the contributor has contributed to
- **Milestones** = count of the three team milestones this contributor's work provided evidence toward

---

## V-01 — Phrasing Register: Formal/Technical Imperative

**Axis**: Phrasing register — formal command language, zero hedging, no conversational prose
**Hypothesis**: Uniform imperative voice (Glob / Compute / Verify / Correct / Write) makes
every gate instruction identical in register to the surrounding content — a gate cannot soften
into a suggestion when all instructions use the same command tone. C-21's correction instruction
("Correct the Score column") carries the same weight as a scan instruction ("Glob
`simulations/`") because both are commands. C-22 and C-23 benefit from the same: "Test each
topic individually" and "(1)…(2)…" are commands, not suggestions.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute each step in sequence. Do not begin a step until the previous gate passes.

---

### STAGNATION PATTERN REGISTRY

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no breadth |
| NAMESPACE_MOAT | All signals from one namespace — no synthesis possible |
| SPRINT_FREEZE | No new signals in current sprint — momentum stalled |
| SHALLOW_POOL | Multiple topics, none reaching Signal Depth |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership unknown |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels.

### SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

---

### STEP 1 — SCAN [C-01]

Glob `simulations/**/*.md`. For each file extract:
- Topic path (subdirectory under `simulations/`, e.g. `scout/competitors`)
- Namespace (first path segment, e.g. `scout`)
- Contributor identity (frontmatter `author:` or `contributor:` field; or filename prefix before
  the first digit-run, e.g. `jsmith` from `jsmith-feature-signal-2026-03-01.md`)

Record an internal scan state (not part of final output):

```
SCAN STATE (internal):
  Topics: [list of unique topic paths]
  Namespaces: [list of unique first segments]
  Contributors: [deduplicated list, or "not detectable"]
  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` is accessible and the glob returned at least one file.
>  (2) Every file in the glob is assigned to a topic path derived from actual glob output — no
>      topic paths are inferred or assumed from context.
>  (3) The scan state record above is complete.
>  (4) No file was skipped."
>
> Every condition must be confirmed before proceeding to Step 2.
> Pass: "SCAN GATE [C-01]: Passed. [n] signals, [n] topics, [n] namespaces, contributors: [list]."
> Fail on condition (1) or (2): "SCAN GATE FAIL [C-01]: condition ([n]) — [specific file or path].
>   Workspace empty or unreadable. Continuing with empty data."
> Fail on condition (3) or (4): "SCAN GATE FAIL [C-01]: condition ([n]) — file '[path]' not
>   assigned. Resolve before proceeding."

---

### STEP 2 — ACHIEVEMENTS [C-02/C-06/C-07]

**Pre-write gate [C-11]**:
> "Do all topics from the scan state appear in either Earned or Locked below?
> If not, identify the missing topic and add it before generating the section."

Achievement definitions:

| Achievement | Condition |
|-------------|-----------|
| First Signal | >= 1 signal for this topic |
| Signal Depth | >= 3 signals for this topic |
| Full Sweep | signals span >= 3 distinct namespaces for this topic |
| Solo Pioneer | exactly 1 contributor, >= 1 signal for this topic |
| Team Topic | >= 2 contributors, >= 1 signal each for this topic |

Render two explicitly labeled sections [C-06, C-07]:

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement name]**: [evidence — file count, contributor names, or namespace list]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement name]: needs [quantified gap — "2 more signals", "1 more namespace", etc.]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every topic in the scan state appears in Earned or Locked — count must match.
>  (2) Every Earned entry names specific evidence (count, names, or namespace list) — no bare
>      achievement names without evidence.
>  (3) Every Locked entry quantifies the gap with a specific count or target — no vague gaps."
>
> Fail on condition (1): "COMPUTE GATE FAIL [C-02]: condition (1) — topic '[path]' absent from
>   output. Adding before proceeding."
> Fail on condition (2) or (3): "COMPUTE GATE FAIL [C-02]: condition ([n]) — entry '[topic /
>   achievement]' lacks [evidence / specific gap]."

---

### STEP 3 — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [file path, or "—"] | [gap, or "—"] |
| shared coverage | EARNED / NOT YET | [2+ contributors × 2+ topics, or "—"] | [gap, or "—"] |
| debate starter | EARNED / NOT YET | [topic path + namespaces, or "—"] | [gap, or "—"] |
```

Use exact milestone names. Any deviation from the names above fails the gate.

Milestone definitions:
- **first team signal**: any signal file exists in `simulations/`
- **shared coverage**: 2+ contributors each contributing signals to 2+ distinct topics
- **debate starter**: 1 topic with signals spanning 3+ distinct namespaces

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) The row name in position 1 is exactly 'first team signal'.
>  (2) The row name in position 2 is exactly 'shared coverage'.
>  (3) The row name in position 3 is exactly 'debate starter'.
>  (4) Every row has an Evidence cell that is either a file path, a contributor+topic pair, or
>      an explicit '—' — no cells are empty."
>
> Fail: "MILESTONES GATE FAIL [C-03]: condition ([n]) — row '[written name]' must be '[exact name]'."

---

### STEP 4 — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

**Pre-write gate [C-11]**:
> "Do I have Signals, Topics, and Milestones counts for each contributor extracted from the scan
> state? If not, derive these counts now from the scan state before building the table."

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | [name or "unknown"] | [n] | [n] | [n] | [Score] |
| 2 | ... | ... | ... | ... | ... |
```

If no contributor metadata: one row `| — | (no contributor metadata found) | — | — | — | — |`

**FORMULA CORRECTION GATE [C-19/C-21]** — numbered sub-steps [C-23]:
> "(1) Render worked example for Rank 1: Score = {Signals}×1 + {Topics}×3 + {Milestones}×5 = {total}
>  (2) Compare {total} to the Score column entry for Rank 1 in the table above.
>  (3) If {total} does not equal the Score column entry, correct the Score column to {total}
>      before proceeding. State: 'Score corrected from {old} to {new}.'
>  (4) Confirm: Score column entry for Rank 1 equals {total}."
>
> Gate does not pass until condition (4) is confirmed.
> Pass: "FORMULA GATE [C-19/C-21]: Passed. Rank-1 score = {total} (verified / corrected)."
> No metadata: "FORMULA GATE [C-19/C-21]: Not applicable — no contributor metadata."

---

### STEP 5 — 1-AWAY GAPS [C-09/C-18]

Scan for achievements or milestones requiring exactly 1 action to unlock.

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
| [topic or milestone] | [Achievement name] | [e.g., "1 more signal"] | [specific file or contributor action] |
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) I have checked every topic against every achievement threshold for exactly-1-step gaps.
>  (2) I have checked every team milestone for exactly-1-step gaps.
>  (3) Every row in the table has all four columns populated: topic/milestone, achievement,
>      gap (exact count or name), exact action needed."
>
> Fail on condition (3): "1-AWAY GATE FAIL [C-09]: row '[topic]' missing column '[name]'.
>   Adding before proceeding."
> No gaps found: single row "No single-step unlocks available."

---

### STEP 6 — NEXT ACTIONS [C-05/C-12/C-14/C-17]

Identify the dominant stagnation pattern from the registry. State the label before writing actions.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[specific action — name namespace and topic explicitly]**
   → Unlocks **[Achievement or Milestone name]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence explaining the disruption]

2. [same format]

3. [same format]
```

Write at least 3 actions. Each must name a specific namespace and topic.

**ACTIONS GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
> "(1) Each action names a specific namespace and topic — not generic advice.
>  (2) Each action names the exact achievement or milestone it unlocks.
>  (3) Each action uses a pattern label from the Stagnation Pattern Registry — no invented labels.
>  (4) At least 3 actions are written.
>  (5) The gate label itself includes criterion IDs: this gate is labeled [C-05/C-12/C-14/C-20]."
>
> Fail: "ACTIONS GATE FAIL [C-05]: action [n], condition ([n]) — [specific issue]."

---

### STEP 7 — TEAM INSIGHT [C-10/C-13/C-22]

Execute the derivability elimination protocol before writing the insight.

**Step A — Candidate**: State the candidate insight in one sentence:
> "Candidate: [insight with specific numbers and topic/contributor names]"

**Step B — Topic elimination test**: For each topic in the scan state, test:
> "Can this insight be reached from [topic path] data alone, without any other topic?
>  Answer: YES / NO"
List every topic and its answer.

**Step C — Verdict**:
- All NO: "DERIVABILITY GATE [C-22]: [n] topics tested. No single topic yields this conclusion
  alone. Candidate approved."
- Any YES: "DERIVABILITY GATE [C-22]: Candidate derivable from topic '[path]' alone. Discarding.
  Returning to Step A."
  Repeat up to 2 times. If no passing candidate after 2 attempts:
  "DERIVABILITY GATE [C-22]: Insufficient cross-topic data for a non-derivable insight."

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Insight is written as **TEAM INSIGHT — [name]:** — a named, referenceable artifact.
>  (2) Insight names specific topics, contributors, or numeric values — not only pattern labels.
>  (3) Insight passed derivability elimination in Step C — no single topic yields it alone."
>
> Fail: cite condition number and specific issue before revising.

Write the approved insight:

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence with specific numbers and names]
```

---

### STEP 8 — WRITE ARTIFACT [C-08]

Write the complete output to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
gate_language: numbered-substeps
---
```

---

## V-02 — Phrasing Register: Conversational/Narrative Team Report

**Axis**: Phrasing register — conversational narration, team-report voice, "we found / here's
what happened" framing
**Hypothesis**: When this skill is run weekly, a conversational voice ("Here's what the team
earned this sprint") increases adoption and reduces the cognitive overhead of parsing the output.
Structural completeness (all 23 criteria) is maintained through the same gates and tables —
only the framing prose changes. The hypothesis is that this variation achieves equivalent
criterion coverage while being more pleasant to read in a recurring team ritual context.

---

You are running `corps-achievements`. Your job is to write a weekly team achievements report
from workspace signal data. Think of this as writing a team digest — factual, specific, and
actionable. Scan the workspace, compute what the team earned and what they're close to, and
write it up.

---

### The Pattern Registry (draw from this, never invent)

| Label | What it means |
|-------|---------------|
| SOLO_ISLAND | One person is carrying the whole topic — no one else has contributed |
| NAMESPACE_MOAT | All signals land in one namespace — the topic looks narrow from the outside |
| SPRINT_FREEZE | Nothing new was added this sprint — the topic has gone quiet |
| SHALLOW_POOL | Lots of topics but none with enough signals to count as depth |
| ORPHAN_TOPIC | Nobody is identified as the owner — the topic has no face |

### The Scoring Formula

Leaderboard scores are computed as: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

---

### Start: Scan the Workspace [C-01]

Open up `simulations/` and look at what's there. Glob `simulations/**/*.md`. For each file,
note: which topic it belongs to (the subdirectory path), which namespace it lives in (first
path segment), and who created it if you can tell (from frontmatter `author:`/`contributor:`
or a recognizable filename prefix).

Keep a working list before you write anything:

```
Workspace tally (working note — not part of output):
  Topics found: [list]
  Namespaces: [list]
  Contributors: [list, or "can't tell from file names"]
  Total signals: [n]
```

**Before going further — scan check [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) I can access `simulations/` and at least one file came back from the glob.
>  (2) Every file I found is connected to a real directory path from the glob — I'm not
>      guessing at topic names.
>  (3) The working list above accounts for every file found.
>  (4) No file was silently skipped."
>
> If the workspace is empty: "Nothing to scan yet — workspace has no signal files.
>   Proceeding with an empty report. All achievements: not yet earned. All milestones: not yet."
> If a file can't be assigned: "Scan check [C-01]: file '[path]' couldn't be assigned to a topic.
>   Noting this before continuing."

Once checked: "Scan check [C-01]: Found [n] signals across [n] topics and [n] namespaces.
Contributors: [list]."

---

### Section 1: What the Team Earned [C-02/C-06/C-07/C-08]

Here's what the team has earned so far, broken out by topic. Two groups: things already
unlocked, and things that are locked but in reach.

**Before writing this section [C-11]**:
> "Is every topic from my working list accounted for below — either in Earned or in Locked?
> If not, find the gap and add it before I write."

Achievement definitions:
- **First Signal** — at least 1 signal file for this topic
- **Signal Depth** — at least 3 signal files for this topic
- **Full Sweep** — signals cover at least 3 distinct namespaces for this topic
- **Solo Pioneer** — exactly 1 contributor has worked on this topic (and at least 1 signal exists)
- **Team Topic** — 2 or more contributors have each contributed at least 1 signal to this topic

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement name]**: [evidence — count, names, or namespace list]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement name]: [what's still needed — specific count or target]
```

**Completeness check [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every topic from my scan working list appears in Earned or Locked above.
>  (2) Every earned achievement names what the evidence is — not just a badge name.
>  (3) Every locked achievement says specifically what's missing."
>
> If condition (1) fails: "Completeness check [C-02]: topic '[path]' got left out — adding now."

---

### Section 2: Team Milestones [C-03/C-08]

These are team-level moments, not per-topic. All three milestone names must appear exactly
as written here.

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [file path, or "—"] | [gap, or "—"] |
| shared coverage | EARNED / NOT YET | [who covered what, or "—"] | [gap, or "—"] |
| debate starter | EARNED / NOT YET | [topic + namespaces, or "—"] | [gap, or "—"] |
```

Milestone definitions:
- **first team signal** — any signal file exists
- **shared coverage** — 2+ contributors each with signals in 2+ distinct topics
- **debate starter** — 1 topic with signals across 3+ distinct namespaces

**Milestone check [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) The first row is named exactly 'first team signal'.
>  (2) The second row is named exactly 'shared coverage'.
>  (3) The third row is named exactly 'debate starter'.
>  (4) Every row has something in Evidence — either a real path/name or an explicit '—'."
>
> If any name is off: "Milestone check [C-03]: row '[written name]' needs to be '[exact name]'."

---

### Section 3: Who's Leading [C-04/C-16/C-19/C-21]

The leaderboard shows who has contributed most, using a formula that weights team breadth
(Topics) and milestone contribution (Milestones) more than raw signal volume.

**Before writing the table [C-11]**:
> "Do I have Signals, Topics, and Milestones counts for each contributor from the scan?
> If not, pull these from my working list before building the table."

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula used: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

If no contributor metadata was found: one row indicating this.

**Score verification check [C-19/C-21]** — numbered sub-steps [C-23]:
> "(1) Worked example for Rank 1: Score = {Signals}×1 + {Topics}×3 + {Milestones}×5 = {total}
>  (2) Does {total} match what's in the Score column for Rank 1?
>  (3) If there's a mismatch, fix the Score column to show {total} and note: 'Score corrected
>      from {old} to {new}.'
>  (4) Confirm the Score column now matches {total}."
>
> "Score check [C-19/C-21]: Rank-1 score = {total} — verified / corrected."

---

### Section 4: One Step Away [C-09/C-18]

These are the things the team is closest to unlocking — exactly one action away.

```markdown
## Almost There

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-away check [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) I checked every topic against every achievement threshold for exactly-1-step gaps.
>  (2) I checked every milestone for exactly-1-step gaps.
>  (3) Every row has all four columns: topic/milestone, achievement name, gap description,
>      and the exact action someone can take."
>
> If condition (3) fails: "1-away check [C-09]: row '[topic]' is missing '[column]' — adding it."
> Nothing within 1 step: "No single-step unlocks available."

---

### Section 5: What to Do Next [C-05/C-12/C-14/C-17]

Here's where the team is stuck (the stagnation pattern) and what to do about it. Each action
names what it unlocks and what inertia pattern it breaks.

Stagnation patterns (from the registry — use these labels exactly):
`SOLO_ISLAND` / `NAMESPACE_MOAT` / `SPRINT_FREEZE` / `SHALLOW_POOL` / `ORPHAN_TOPIC`

```markdown
## Next Actions

Current stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[specific action — namespace and topic named]**
   → Unlocks **[Achievement or Milestone name]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence on why this breaks it]

2. [same format]

3. [same format]
```

**Actions check [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
> "(1) Each action calls out a specific namespace and topic.
>  (2) Each action names the exact achievement or milestone it unlocks.
>  (3) Each action uses a label from the pattern registry, not a made-up label.
>  (4) There are at least 3 actions."
>
> "Actions check [C-05/C-12/C-14/C-20]: [n] actions verified."

---

### Section 6: What This Tells Us About the Team [C-10/C-13/C-22]

Write one observation that requires looking across multiple topics — something you couldn't
conclude from any single topic's data alone. This is the team insight.

Before writing it, run the derivability check:

**Step A — Candidate**: Write a candidate insight:
> "Candidate: [one sentence, naming specific topics, contributors, or counts]"

**Step B — Test it topic-by-topic**: For each topic in the workspace:
> "Could someone reach this conclusion from [topic path] data alone, without any other topic?
>  YES / NO"

**Step C — Verdict**:
- All NO: the insight is genuine cross-topic synthesis. Approved.
  "Derivability check [C-22]: [n] topics tested. Insight not reachable from any one topic.
  Approved."
- Any YES: the insight is derivable from a single topic. Discard and return to Step A.
  "Derivability check [C-22]: Insight reachable from '[topic]' alone. Discarding. New candidate."
  Try up to 2 times. If still no passing insight:
  "Derivability check [C-22]: Not enough cross-topic data yet."

**Insight quality check [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) The insight uses the format **TEAM INSIGHT — [name]:** so it can be referenced by name.
>  (2) The insight names specific topics, people, or numbers.
>  (3) The insight passed the derivability check — not reachable from any single topic alone."
>
> If condition (1) fails: apply the format before publishing.

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence with specific numbers and names]
```

---

### Write the Report [C-08]

Save the output to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
register: conversational
---
```

---

## V-03 — Lifecycle Ordering: Milestone-First

**Axis**: Lifecycle ordering — team milestones are computed before per-topic achievements
**Hypothesis**: Computing milestones first establishes the team-level context (what the team
has achieved together) before individual topic data is presented. This ordering means per-topic
achievement lists are read through a lens already established by the team-level summary —
reducing the risk that the model treats the report as a per-topic audit rather than a
team-level narrative. It also means milestone gaps are visible before the leaderboard,
making the leaderboard score weights feel grounded in team outcomes rather than abstract.

---

You are running `corps-achievements`. No arguments — scan and compute from workspace state.

---

### STAGNATION PATTERN REGISTRY

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no breadth |
| NAMESPACE_MOAT | All signals from one namespace — no cross-namespace synthesis |
| SPRINT_FREEZE | No new signals in current sprint — momentum stalled |
| SHALLOW_POOL | Multiple topics, none reaching Signal Depth |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership unknown |

### SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

---

### PHASE 1 — SCAN [C-01]

Glob `simulations/**/*.md`. Extract for each file:
- Topic path (subdirectory under `simulations/`)
- Namespace (first path segment)
- Contributor identity (frontmatter `author:`/`contributor:`, or filename prefix)

Build internal scan record:

```
SCAN RECORD (internal):
  Topics: [list]
  Namespaces: [list]
  Contributors: [list or "not detectable"]
  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` is accessible and at least one file was found.
>  (2) Every file is assigned to a topic path from actual glob results — no inferred paths.
>  (3) The scan record is complete.
>  (4) No file was skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, [n] namespaces, contributors: [list]."
> Fail: "SCAN GATE FAIL [C-01]: condition ([n]) — [specific file/path]. Continuing with empty data."

---

### PHASE 2 — TEAM MILESTONES (before per-topic data) [C-03/C-08]

Compute team milestones from the scan record before computing per-topic achievements.
This phase establishes the team context that frames all subsequent per-topic data.

Milestone definitions:
- **first team signal**: any signal file exists in `simulations/`
- **shared coverage**: 2+ contributors each with signals in 2+ distinct topics
- **debate starter**: 1 topic with signals spanning 3+ distinct namespaces

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [file path, or "—"] | [gap, or "—"] |
| shared coverage | EARNED / NOT YET | [contributors × topics, or "—"] | [gap, or "—"] |
| debate starter | EARNED / NOT YET | [topic + namespaces, or "—"] | [gap, or "—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 is named exactly 'first team signal'.
>  (2) Row 2 is named exactly 'shared coverage'.
>  (3) Row 3 is named exactly 'debate starter'.
>  (4) Every row has a populated Evidence cell — either a real reference or '—'."
>
> Fail: "MILESTONES GATE FAIL [C-03]: condition ([n]) — row '[written]' → '[exact name]'."

---

### PHASE 3 — ACHIEVEMENTS BY TOPIC [C-02/C-06/C-07]

**Pre-write gate [C-11]**:
> "Does every topic in the scan record appear in either Earned or Locked below?
> Milestone context from Phase 2 is now established — does any milestone gap point to a
> specific topic or achievement that should be highlighted in this section?"

Achievement definitions:
| Achievement | Condition |
|-------------|-----------|
| First Signal | >= 1 signal |
| Signal Depth | >= 3 signals |
| Full Sweep | signals span >= 3 namespaces |
| Solo Pioneer | exactly 1 contributor, >= 1 signal |
| Team Topic | >= 2 contributors, >= 1 signal each |

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement]**: [evidence — count, names, or namespace list]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement]: needs [quantified gap]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every topic in the scan record appears in Earned or Locked — no omissions.
>  (2) Every Earned entry names specific evidence.
>  (3) Every Locked entry quantifies the gap."
>
> Fail: "COMPUTE GATE FAIL [C-02]: condition ([n]) — topic '[path]' / entry '[ref]' [issue]."

---

### PHASE 4 — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

Milestone context from Phase 2 informs the Milestones column — contributors whose work
provided evidence toward earned milestones get milestone credit.

**Pre-write gate [C-11]**:
> "Do I have Signals, Topics, and Milestones counts for each contributor?
> Have I checked which milestone evidence in Phase 2 came from which contributor?"

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

If no contributor metadata: one row indicating this.

**FORMULA CORRECTION GATE [C-19/C-21]** — numbered sub-steps [C-23]:
> "(1) Render worked example: Score = {Signals}×1 + {Topics}×3 + {Milestones}×5 = {total}
>  (2) Compare {total} to the Score column entry for Rank 1.
>  (3) If they differ, correct the Score column to {total} before proceeding. State:
>      'Score corrected from {old} to {new}.'
>  (4) Confirm Score column entry now equals {total}."
>
> "FORMULA GATE [C-19/C-21]: Rank-1 = {total} (verified / corrected)."

---

### PHASE 5 — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked every topic for exactly-1-signal gaps.
>  (2) Checked every topic for exactly-1-contributor gaps.
>  (3) Checked every milestone from Phase 2 for exactly-1-step gaps.
>  (4) Every row has all four columns populated."
>
> Fail: "1-AWAY GATE FAIL [C-09]: row '[topic]' missing '[column]'."
> Nothing: "No single-step unlocks available."

---

### PHASE 6 — NEXT ACTIONS [C-05/C-12/C-14/C-17]

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[specific action — namespace and topic]**
   → Unlocks **[Achievement or Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]

2. ...
3. ...
```

**ACTIONS GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
> "(1) Each action names a specific namespace and topic.
>  (2) Each action names the exact achievement or milestone it unlocks.
>  (3) Each action uses a pattern label from the registry.
>  (4) At least 3 actions are written."
>
> Fail: "ACTIONS GATE FAIL [C-05]: action [n], condition ([n]) — [issue]."

---

### PHASE 7 — TEAM INSIGHT [C-10/C-13/C-22]

Execute the derivability elimination protocol:

**Step A**: State candidate insight in one sentence.

**Step B**: For each topic in the scan record:
> "Can this insight be reached from [topic path] alone? YES / NO"

**Step C**:
- All NO: "DERIVABILITY GATE [C-22]: [n] topics tested. Candidate approved."
- Any YES: discard, retry. Max 2 attempts. If failed:
  "DERIVABILITY GATE [C-22]: Insufficient data for non-derivable insight."

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Written as **TEAM INSIGHT — [name]:** — named artifact.
>  (2) Names specific topics, contributors, or numeric values.
>  (3) Passed derivability elimination."

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight with specific numbers and names]
```

---

### PHASE 8 — WRITE ARTIFACT [C-08]

`simulations/corps/achievements-{{date}}.md`

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
ordering: milestone-first
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
---
```

---

## V-04 — Combined: Formal Register + Milestone-First Ordering

**Axis**: Formal/technical command language (V-01) combined with milestone-first lifecycle
ordering (V-03)
**Hypothesis**: Formal imperative language and milestone-first ordering reinforce each other:
the milestone section, written as a formal command ("Compute / Verify / Record"), cannot be
informally skipped or soft-pedaled before the per-topic section runs. The combination creates
a skill that is both maximally auditable (formal gates with criterion IDs) and maximally
team-oriented (milestones establish context before individual data). The interaction hypothesis
is that these two axes together produce less per-topic tunnel vision and more gate compliance
than either axis alone.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute each phase in the order listed. Do not begin a phase until the previous
gate passes.

---

### STAGNATION PATTERN REGISTRY (reference this registry — do not invent labels)

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no team breadth |
| NAMESPACE_MOAT | All signals from one namespace — no synthesis possible |
| SPRINT_FREEZE | No new signals in current sprint — momentum stalled |
| SHALLOW_POOL | Multiple topics, none reaching Signal Depth |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership unknown |

### SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

---

### PHASE 1 — SCAN [C-01]

Glob `simulations/**/*.md`. Extract per file:
- Topic path (subdirectory under `simulations/`)
- Namespace (first path segment)
- Contributor identity (frontmatter `author:`/`contributor:` or filename prefix)

Record the scan state (internal):

```
SCAN STATE:
  Topics: [list]
  Namespaces: [list]
  Contributors: [list or "not detectable"]
  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` is accessible and glob returned at least one file.
>  (2) Every file is assigned to a topic path from actual glob output — no inferred paths.
>  (3) Scan state record is complete.
>  (4) No file was skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, [n] namespaces. Contributors: [list]."
> Fail: "SCAN GATE FAIL [C-01]: condition ([n]) — [specific file/path]. Continuing with empty data."

---

### PHASE 2 — TEAM MILESTONES (first) [C-03/C-08]

Compute milestones before per-topic achievements. Establish team context.

Definitions:
- **first team signal**: any signal file exists
- **shared coverage**: 2+ contributors × 2+ distinct topics each
- **debate starter**: 1 topic with signals spanning 3+ distinct namespaces

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [file path, or "—"] | [gap, or "—"] |
| shared coverage | EARNED / NOT YET | [contributor × topic list, or "—"] | [gap, or "—"] |
| debate starter | EARNED / NOT YET | [topic + namespaces, or "—"] | [gap, or "—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 name is exactly 'first team signal'.
>  (2) Row 2 name is exactly 'shared coverage'.
>  (3) Row 3 name is exactly 'debate starter'.
>  (4) Every row has an Evidence cell — file path, reference, or explicit '—'."
>
> Fail: "MILESTONES GATE FAIL [C-03]: condition ([n]) — '[written]' → '[exact name]'."

---

### PHASE 3 — ACHIEVEMENTS [C-02/C-06/C-07]

**Pre-write gate [C-11]**:
> "Does every topic in the scan state appear in Earned or Locked?
> Does any milestone gap from Phase 2 identify a topic or contributor not yet in the scan state?"

Achievement definitions:
| Achievement | Condition |
|-------------|-----------|
| First Signal | >= 1 signal |
| Signal Depth | >= 3 signals |
| Full Sweep | signals span >= 3 namespaces |
| Solo Pioneer | exactly 1 contributor, >= 1 signal |
| Team Topic | >= 2 contributors, >= 1 signal each |

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement]**: [evidence]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement]: needs [quantified gap]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every topic in scan state appears in Earned or Locked.
>  (2) Every Earned entry names specific evidence.
>  (3) Every Locked entry quantifies the gap."
>
> Fail: "COMPUTE GATE FAIL [C-02]: condition ([n]) — topic '[path]' missing / entry '[ref]' [issue]."

---

### PHASE 4 — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

**Pre-write gate [C-11]**:
> "Do I have Signals, Topics, and Milestones counts for each contributor from the scan state?
> Have I checked which contributors provided evidence toward the milestones earned in Phase 2?"

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

No contributor metadata: one row `| — | (no contributor metadata) | — | — | — | — |`

**FORMULA CORRECTION GATE [C-19/C-21]** — numbered sub-steps [C-23]:
> "(1) Render worked example: Score = {Signals}×1 + {Topics}×3 + {Milestones}×5 = {total}
>  (2) Compare {total} to Score column entry for Rank 1.
>  (3) If different, correct the Score column to {total} before proceeding.
>      State: 'Score corrected from {old} to {new}.'
>  (4) Confirm: Score column entry for Rank 1 = {total}."
>
> Gate does not pass until condition (4) is confirmed.
> "FORMULA GATE [C-19/C-21]: Passed. Rank-1 = {total} (verified / corrected)."

---

### PHASE 5 — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked every topic for exactly-1-signal achievement gaps.
>  (2) Checked every topic for exactly-1-contributor achievement gaps.
>  (3) Checked all milestones from Phase 2 for exactly-1-step gaps.
>  (4) Every row has all four columns: topic/milestone, achievement, gap, exact action."
>
> Fail: "1-AWAY GATE FAIL [C-09]: row '[topic]' missing '[column]'. Adding before proceeding."
> Nothing within 1 step: "No single-step unlocks available."

---

### PHASE 6 — NEXT ACTIONS [C-05/C-12/C-14/C-17]

Identify the dominant stagnation pattern. Carry the label forward to every action row.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[action — specific namespace and topic]**
   → Unlocks **[Achievement or Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]

2. ...
3. ...
```

**ACTIONS GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
> "(1) Each action names a specific namespace and topic.
>  (2) Each action names the exact achievement or milestone it unlocks.
>  (3) Each action uses a label from the Stagnation Pattern Registry.
>  (4) At least 3 actions are written.
>  (5) The gate label includes criterion IDs: [C-05/C-12/C-14/C-20]."
>
> Fail: "ACTIONS GATE FAIL [C-05]: action [n], condition ([n]) — [specific issue]."

---

### PHASE 7 — TEAM INSIGHT [C-10/C-13/C-22]

Execute derivability elimination protocol.

**Step A**: State candidate insight in one sentence.

**Step B**: For each topic in the scan state:
> "Can this insight be reached from [topic path] alone, without any other topic? YES / NO"

**Step C**:
- All NO: "DERIVABILITY GATE [C-22]: [n] topics tested. No single topic yields this conclusion.
  Approved."
- Any YES: "DERIVABILITY GATE [C-22]: Candidate derivable from '[path]' alone. Discarding."
  Retry. Max 2 attempts. If no passing candidate:
  "DERIVABILITY GATE [C-22]: Insufficient cross-topic data."

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Written as **TEAM INSIGHT — [name]:** — named, referenceable artifact.
>  (2) Names specific topics, contributors, or numeric values.
>  (3) Passed derivability elimination — not derivable from any single topic alone."
>
> Fail: cite condition and specific issue before revising.

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight with specific numbers and names]
```

---

### PHASE 8 — WRITE ARTIFACT [C-08]

`simulations/corps/achievements-{{date}}.md`

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
ordering: milestone-first
register: formal
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
---
```

---

## V-05 — Combined: Conversational Register + Prominent Inertia Framing

**Axis**: Conversational/narrative register (V-02) combined with cost-of-inertia framing
woven into every major section — not only in Next Actions
**Hypothesis**: The standard skill positions inertia cost only in the Next Actions section.
This variation surfaces the cost of inertia at every section: after Achievements ("what the
team missed by not adding a second contributor last sprint"), after Milestones ("the milestone
that lapsed"), after the Leaderboard ("the contributor who is close to unseating the top
rank"). Conversational register makes this framing feel like a coach's commentary rather
than a compliance checklist. The interaction hypothesis: inertia cost framing at each section
raises the perceived stakes of each gap, making the final Next Actions feel inevitable rather
than optional.

---

You are running `corps-achievements`. Write a weekly team achievements digest — specific,
warm, and action-oriented. Your voice is a team coach who knows the data. For each section,
note not just what was earned but what was left on the table.

---

### Pattern Registry (use these labels — no ad hoc patterns)

| Label | What you are seeing |
|-------|---------------------|
| SOLO_ISLAND | One person is doing all the work for a topic — no backup, no breadth |
| NAMESPACE_MOAT | Everything lives in one namespace — the topic looks shallow from any angle |
| SPRINT_FREEZE | The sprint ended with nothing new — momentum has stopped |
| SHALLOW_POOL | Many topics, but none deep enough to matter individually |
| ORPHAN_TOPIC | Topic exists but nobody owns it — will quietly stagnate |

### Scoring Formula

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

---

### Opening: What's in the Workspace [C-01]

Glob `simulations/**/*.md`. For each file, extract the topic path (subdirectory under
`simulations/`), namespace (first path segment), and contributor if detectable (from
frontmatter `author:`/`contributor:` or filename prefix).

Keep a working tally before writing anything:

```
Working tally (not part of output):
  Topics: [list]
  Namespaces: [list]
  Contributors: [list or "can't determine"]
  Signals: [n]
```

**Scan check [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` is accessible and at least one file was found.
>  (2) Every file is assigned to a real directory path from the glob — no assumed topics.
>  (3) The working tally is complete.
>  (4) No file was silently skipped."
>
> If empty: "Workspace is empty — no signals yet. Writing an all-unearned report."
> If a file can't be assigned: "Scan check [C-01]: '[path]' couldn't be assigned. Noting this."
> "Scan check [C-01]: [n] signals across [n] topics, [n] namespaces. Contributors: [list]."

---

### Section 1: What Got Earned — and What Got Left Behind [C-02/C-06/C-07/C-08]

Here's what the team unlocked this sprint, and what was close but didn't cross the line.

**Before writing [C-11]**:
> "Does every topic from my tally appear below — either earned or locked?
> Are there any topics that got zero achievements? They still need a row."

Achievement definitions:
- **First Signal** — at least 1 signal for this topic
- **Signal Depth** — at least 3 signals for this topic
- **Full Sweep** — signals span at least 3 distinct namespaces for this topic
- **Solo Pioneer** — exactly 1 contributor has contributed (>= 1 signal)
- **Team Topic** — 2+ contributors have each contributed at least 1 signal

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement]**: [evidence — specific count, names, or namespaces]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement]: [specific gap — "needs 1 more signal", "needs 1 more contributor"]
```

*Inertia note*: For each locked achievement that was within 1 step of earning, add a brief
parenthetical: "(Would have earned this with one more [action] last sprint.)"

**Completeness check [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every topic from my working tally appears in Earned or Locked.
>  (2) Every earned achievement names its evidence.
>  (3) Every locked achievement names a specific gap."
>
> If condition (1) fails: "Completeness check [C-02]: topic '[path]' is missing. Adding now."

---

### Section 2: Team Milestones — Earned and Overdue [C-03/C-08]

Three milestones mark team-level moments. Here's where the team stands on each one.

Milestone definitions:
- **first team signal**: any signal file exists
- **shared coverage**: 2+ contributors each with signals in 2+ distinct topics
- **debate starter**: 1 topic with signals spanning 3+ distinct namespaces

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [file path, or "—"] | [gap, or "—"] |
| shared coverage | EARNED / NOT YET | [who covered what, or "—"] | [gap, or "—"] |
| debate starter | EARNED / NOT YET | [topic + namespaces, or "—"] | [gap, or "—"] |
```

*Inertia note*: For any NOT YET milestone: "This milestone has been available since the
team added [evidence threshold] — it's been sitting here."

**Milestone check [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 is named exactly 'first team signal'.
>  (2) Row 2 is named exactly 'shared coverage'.
>  (3) Row 3 is named exactly 'debate starter'.
>  (4) Every row has a populated Evidence cell."
>
> If any name is wrong: "Milestone check [C-03]: row '[written]' must be '[exact name]'."

---

### Section 3: Who's Leading — and Who Could Be [C-04/C-16/C-19/C-21]

The leaderboard shows who has contributed most to the team's collective signal coverage.
Scores weight topic breadth and milestone contribution more than raw signal volume —
because one person adding 10 signals to one topic is less valuable than two people each
covering different topics.

**Before writing [C-11]**:
> "Do I have Signals, Topics, and Milestones counts for each contributor?
> If not, pull these from the working tally before building the table."

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

*Inertia note*: If Rank 2 is within 5 points of Rank 1: "Rank 2 is [n] points behind —
one more topic contribution would change the top."

If no contributor metadata: one row indicating this.

**Score check [C-19/C-21]** — numbered sub-steps [C-23]:
> "(1) Worked example: Score = {Signals}×1 + {Topics}×3 + {Milestones}×5 = {total}
>  (2) Does {total} match the Score column for Rank 1?
>  (3) If not, fix the Score column to {total}. Note: 'Score corrected from {old} to {new}.'
>  (4) Confirm the Score column now shows {total}."
>
> "Score check [C-19/C-21]: Rank-1 = {total} (verified / corrected)."

---

### Section 4: One Step Away [C-09/C-18]

The shortest path to the next achievement. These are things the team could unlock this week.

```markdown
## Almost There

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

*Inertia note*: Under the table — "Each row above is a concrete opportunity that will still
be here next week if nobody acts. These are not hypotheticals."

**1-away check [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked every topic for exactly-1-signal achievement gaps.
>  (2) Checked every topic for exactly-1-contributor achievement gaps.
>  (3) Checked every milestone for exactly-1-step gaps.
>  (4) Every row has all four columns populated."
>
> If condition (4) fails: "1-away check [C-09]: row '[topic]' missing '[column]'. Adding now."
> Nothing: "No single-step unlocks available."

---

### Section 5: What to Do Before Next Week [C-05/C-12/C-14/C-17]

The team's stagnation pattern this sprint, and the specific actions that would break it.
Each action below names what it unlocks and which inertia it disrupts.

Stagnation patterns:
`SOLO_ISLAND` / `NAMESPACE_MOAT` / `SPRINT_FREEZE` / `SHALLOW_POOL` / `ORPHAN_TOPIC`

```markdown
## Next Actions

This sprint's stagnation pattern: **[PATTERN_LABEL from registry]**

What this pattern costs the team: [one sentence on what the team is missing by not breaking it]

1. **[specific action — name namespace and topic]**
   → Unlocks **[Achievement or Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence on disruption]

2. [same format]

3. [same format]
```

**Actions check [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
> "(1) Each action names a specific namespace and topic — not 'add more signals.'
>  (2) Each action names the exact achievement or milestone it unlocks.
>  (3) Each action uses a label from the pattern registry — no invented labels.
>  (4) At least 3 actions are written."
>
> "Actions check [C-05/C-12/C-14/C-20]: [n] actions verified."

---

### Section 6: The Pattern Only the Team Can See [C-10/C-13/C-22]

One observation that requires looking across all topics together — something no single topic
tells you on its own.

Before writing it, run the derivability check:

**Step A**: Write a candidate insight — one sentence, specific numbers and names.

**Step B**: For each topic in the working tally, ask:
> "Could someone reach this conclusion from [topic path] data alone? YES / NO"

**Step C**:
- All NO: insight approved.
  "Derivability check [C-22]: [n] topics tested. No single topic tells this story alone."
- Any YES: discard and retry (max 2 times).
  "Derivability check [C-22]: Insight reachable from '[path]' alone. New candidate."
  If no candidate passes after 2 attempts:
  "Derivability check [C-22]: Not enough cross-topic data yet for a genuine synthesis insight."

**Insight check [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Written as **TEAM INSIGHT — [name]:** — a named artifact, not embedded prose.
>  (2) Names specific topics, contributors, or numbers — not only the pattern label.
>  (3) Passed the derivability check above."

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence with specific numbers and names]
```

*Inertia note*: "This insight is only visible now because the team has signals across
multiple topics. One more sprint of concentrated single-topic work would hide it again."

---

### Write the Report [C-08]

`simulations/corps/achievements-{{date}}.md`

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
register: conversational
inertia_framing: section-level
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
---
```
