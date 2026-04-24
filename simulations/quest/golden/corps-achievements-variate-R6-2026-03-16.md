---
skill: quest-variate
skill_target: corps-achievements
round: 6
date: 2026-03-16
rubric_version: 6
---

# Variate R6 — corps-achievements

5 complete prompt body variations for the `corps-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | New Criteria Targeted | Used In |
|------|-----------------------|---------|
| Correction-loop gate — formula mismatch triggers table correction, not just display | C-21 | V-01, V-04, V-05 |
| Derivability elimination test — insight tested against each topic individually before writing | C-22 | V-02, V-04, V-05 |
| Numbered sub-step gate language — all multi-condition gates enumerate conditions as (1)…(2)…(3)… | C-23 | V-03, V-05 |
| Correction-loop + derivability (combination) | C-21, C-22 | V-04 |
| All three new criteria simultaneously | C-21, C-22, C-23 | V-05 |

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

## V-01 — C-21: Correction-Loop Gate (Stop-and-Fix)

**Axis**: Formula verification as active correction loop
**Hypothesis**: C-21's defining requirement is that a formula mismatch must trigger a table
correction — not just flag it. This variation implements the correction loop as the skill's
final gate before writing, with a strict two-step protocol: (a) render the worked example
inline, (b) compare it to the table entry, and if they diverge, correct the table before
proceeding. The gate is labeled `[C-19/C-21]` and the correction instruction is imperative.
C-22 is included with basic cross-topic scope checking (not full derivability elimination).
C-23 is applied only to the formula gate (the primary multi-condition gate).

---

You are running `corps-achievements`. No arguments — scan and compute from workspace state.

---

### STEP 1 — Scan [C-01]

Glob `simulations/**/*.md`. For each `.md` file:
- Extract the topic path (subdirectory under `simulations/`, e.g. `scout/competitors`)
- Extract contributor identity from frontmatter (`author:`, `contributor:`) or filename prefix
- Record the namespace (first path segment under `simulations/`)

Build this internal working record before proceeding:

```
SCAN RECORD (internal — not part of final output):
  Topics: [list of unique topic paths]
  Contributors: [deduplicated list, or "not detectable"]
  Namespaces active: [list]
  Total signals: [n]
```

**SCAN GATE [C-01/C-15]**: Confirm before proceeding:
> "SCAN GATE [C-01]: [n] signals found across [n] topics, [n] namespaces.
> Contributors: [list or 'not detectable']. Every topic listed here will appear in Step 2."

If `simulations/` is absent or empty, write:
> "SCAN GATE [C-01]: No signals found — workspace is empty. All achievements: unearned.
> All milestones: NOT YET. Proceeding with empty data."

Then continue. Do not halt on empty workspace.

---

### STEP 2 — Compute Achievements [C-02/C-06/C-07]

For each topic in the scan record, compute earned and available achievements.

Achievement definitions:
- **First Signal** — >= 1 signal file for this topic
- **Signal Depth** — >= 3 signal files for this topic
- **Full Sweep** — signals span >= 3 distinct namespaces for this topic
- **Solo Pioneer** — exactly 1 contributor for this topic and >= 1 signal
- **Team Topic** — 2+ contributors each with >= 1 signal for this topic

Output two named sections (C-06, C-07):

```markdown
## Earned Achievements — Sprint {{date}}

**[topic path]** ([n] signals)
  - **[Achievement name]**: [brief evidence — file count, contributor names, etc.]

## Available Achievements — Locked

**[topic path]** ([n] signals)
  - o [Achievement name]: needs [specific gap — e.g., "2 more signals", "1 more contributor"]
```

**COMPUTE GATE [C-02/C-15]**: After listing all topics, state:
> "COMPUTE GATE [C-02]: [n] topics from scan record processed in Earned or Available sections.
> If this count differs from the scan record count, name the missing topic(s) here before proceeding."

A topic present in the scan record but absent from Step 2 output is a gate failure.
Name the specific missing topic: "COMPUTE GATE FAIL [C-02]: topic '[path]' missing from output."

---

### STEP 3 — Team Milestones [C-03]

Report all three milestones by their exact names. Do not abbreviate or rephrase.

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap (if not earned) |
|-----------|--------|----------|---------------------|
| first team signal | EARNED / NOT YET | [file path or "—"] | [what is needed or "—"] |
| shared coverage | EARNED / NOT YET | [2+ contributors each in 2+ topics, or "—"] | [contributor/topic gap or "—"] |
| debate starter | EARNED / NOT YET | [topic path + namespaces, or "—"] | [namespace or topic needed or "—"] |
```

**MILESTONES GATE [C-03/C-15]**: State:
> "MILESTONES GATE [C-03]: [n/3] milestones earned."
> If any milestone name in the table was written differently than the exact names above, name
> which milestone was misnamed: "MILESTONES GATE FAIL [C-03]: '[written name]' should be '[exact name]'."

---

### STEP 4 — Contributor Leaderboard with Worked Example [C-04/C-16/C-19/C-21]

**Pre-write self-test [C-11]**: Before building this section, answer:
> "Does every contributor in the scan record appear in this table? Does the top-ranked
> contributor's row show a score consistent with the formula Score = (Signals×1) + (Topics×3) + (Milestones×5)?"
> If you cannot answer both yes, resolve the gap before generating the table.

Build the leaderboard table:

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | [name or "unknown"] | [n] | [n] | [n] | [Score] |
| 2 | ... | ... | ... | ... | ... |
```

Formula applied: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**FORMULA VERIFICATION GATE [C-19/C-21]**: Render the worked example for Rank 1:
> "Rank-1 calculation: Score = {Signals}×1 + {Topics}×3 + {Milestones}×5 = {total}"

Then compare: does this total match the Score column entry for Rank 1?

- If YES: "FORMULA GATE [C-19/C-21]: Verified. Rank-1 score confirmed."
- If NO: "FORMULA GATE [C-21]: Mismatch detected. Calculated total = {total},
  table entry = {table value}. Correcting the Score column for Rank 1 to {total}
  before proceeding. Check whether adjacent rows are also affected."

**Correction is required before this gate passes.** Do not proceed to Step 5 until the
Score column matches the worked example.

If contributor metadata is unavailable, write one row:
`| — | (no contributor metadata found) | — | — | — | — |`

---

### STEP 5 — 1-Away Gaps [C-09/C-18]

Scan for achievements or milestones requiring exactly 1 more action to unlock.

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
| [topic or milestone name] | [Achievement name] | [1 more signal / 1 more contributor / 1 more namespace] | [specific file to create or action to take] |
```

If no gaps within 1 step: write "No single-step unlocks available." in a single row spanning
all columns. Do not leave the table empty — one row must always appear.

---

### STEP 6 — Next Actions (Anti-Inertia) [C-05/C-12/C-14/C-17]

**Pre-write self-test [C-11]**: Before writing this section, answer:
> "Does each action below name a specific namespace and topic (not generic advice)?
> Does each action name the exact achievement or milestone it unlocks?
> Does each action reference a pattern label from the registry (not an invented label)?"
> If you cannot answer yes to all three, revise before outputting.

Identify the stagnation pattern this workspace shows (from the registry below).
Carry the pattern label forward into every action row.

**Stagnation Pattern Registry:**
- `SOLO_ISLAND` — one contributor owns all signals
- `NAMESPACE_MOAT` — all signals from one namespace
- `SPRINT_FREEZE` — no new signals in current sprint
- `SHALLOW_POOL` — multiple topics, none reaching Signal Depth
- `ORPHAN_TOPIC` — topics with no contributor metadata

Write at least 3 next actions:

```markdown
## Next Actions

1. **[Specific action — namespace, topic, contributor target]**
   → Unlocks **[Achievement or Milestone name]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence why this action disrupts the pattern]

2. ...

3. ...
```

---

### STEP 7 — Team Insight [C-10/C-13]

Write one named cross-topic insight. The insight must:
- Span topics or contributors (not derivable from a single topic view)
- Be stated as a named artifact using this format:
  `**TEAM INSIGHT — [descriptive name]:** [insight sentence with specific numbers and names]`

Example format (not content):
> **TEAM INSIGHT — Namespace Concentration:** Three contributors each cover distinct namespaces with
> no overlap — pairing any two on a shared topic would unlock Team Topic and Shared Coverage simultaneously.

---

### WRITE ARTIFACT [C-08]

Write the complete output to:
`simulations/corps/achievements-{{date}}.md`

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [label]
---
```

---

## V-02 — C-22: Derivability Elimination Protocol

**Axis**: Single-topic-derivability test as explicit elimination protocol for the cross-topic insight
**Hypothesis**: C-22's key requirement is that the insight must not be derivable from any single
topic view alone — not merely cross-topic "in scope." This variation implements the test as a
3-step elimination check that the model must pass before writing the insight: (1) state the
candidate insight, (2) test it against each topic individually, (3) confirm none yields the
insight alone. If any single topic does yield it, the candidate is discarded and a new one
is found. C-21 is included with a standard correction-loop gate. C-23 applies only to
the derivability gate (the primary multi-condition gate in this axis).

---

You are running `corps-achievements`. No arguments — scan and compute from workspace state.

---

### SCAN [C-01]

Glob `simulations/**/*.md`. For each file, extract:
- Topic path (subdirectory under `simulations/`)
- Namespace (first path segment)
- Contributor identity (frontmatter `author:`/`contributor:` or filename prefix)

Build internal scan record before proceeding.

**SCAN GATE [C-01]**: Confirm:
> "SCAN GATE [C-01]: [n] signals, [n] topics, [n] namespaces, contributors: [list or 'not detectable'].
> Every topic listed will appear in the Achievements section."

If empty workspace: state this, continue with empty data, do not halt.

---

### ACHIEVEMENTS BY TOPIC [C-02/C-06/C-07]

**Earned Achievements** (group label: "Earned") and **Available Achievements** (group label: "Locked")
must appear as separate labeled sections.

Achievement definitions:
- **First Signal** — >= 1 signal
- **Signal Depth** — >= 3 signals
- **Full Sweep** — signals span >= 3 distinct namespaces
- **Solo Pioneer** — exactly 1 contributor, >= 1 signal
- **Team Topic** — 2+ contributors with >= 1 signal each

```markdown
## Earned Achievements — {{date}}

**[topic]** ([n] signals)
  - **[Achievement]**: [evidence]

## Locked Achievements

**[topic]** ([n] signals)
  - o [Achievement]: needs [specific gap]
```

Every topic from the scan record appears in one section.

**COMPUTE GATE [C-02/C-15]**:
> "COMPUTE GATE [C-02]: [n] topics in scan record, [n] topics in output. Match: [YES/NO].
> If NO: missing topic '[path]' must be added before proceeding."

---

### TEAM MILESTONES [C-03]

```markdown
## Team Milestones

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [file path or "—"] | [gap or "—"] |
| shared coverage | EARNED / NOT YET | [contributors + topics or "—"] | [gap or "—"] |
| debate starter | EARNED / NOT YET | [topic + namespaces or "—"] | [gap or "—"] |
```

Use exact milestone names. Renamed milestones fail C-03.

---

### CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

```markdown
## Contributor Leaderboard — {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

**FORMULA GATE [C-19/C-21]**: After building the table:
> "Rank-1 calculation: Score = {Signals}×1 + {Topics}×3 + {Milestones}×5 = {total}"
> Compare to table entry. If mismatch: correct the Score column to the calculated total
> before proceeding to the next section.

No gate passage without confirmed match (or explicit correction applied).

---

### 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There

| Topic / Milestone | Achievement | Gap | Exact Action |
|-------------------|-------------|-----|--------------|
```

If nothing within 1 step: one row stating "No single-step unlocks available."

---

### NEXT ACTIONS (ANTI-INERTIA) [C-05/C-12/C-14/C-17]

Identify the matching stagnation pattern from the registry:
- `SOLO_ISLAND` / `NAMESPACE_MOAT` / `SPRINT_FREEZE` / `SHALLOW_POOL` / `ORPHAN_TOPIC`

```markdown
## Next Actions

1. **[action — namespace, topic]**
   → Unlocks **[Achievement/Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]

2. ...
3. ...
```

**Pre-write self-test [C-11]**:
> "Does each action name a specific namespace and topic? Does each name an exact achievement?
> Does each reference a pattern label from the registry (not an invented label)?"
> Resolve any NO before writing.

---

### TEAM INSIGHT — Derivability Elimination Protocol [C-10/C-13/C-22]

The cross-topic insight must satisfy the single-topic-derivability test.
Execute this 3-step elimination protocol before writing the final insight:

**Step A — Candidate**: State the candidate insight in one sentence.
> "Candidate: [insight]"

**Step B — Elimination test**: For each topic in the workspace, ask:
> "Could I reach this conclusion from [topic X] data alone, without any other topic?"
> List each topic tested and the answer (YES / NO).
> Example: "scout/competitors: NO | flow/lifecycle: NO | listen/support: NO"

**Step C — Verdict**:
- If all tests return NO: the insight passes. Proceed to write it.
- If any test returns YES: the candidate is derivable from a single topic.
  Discard it. Return to Step A with a new candidate.

**DERIVABILITY GATE [C-22/C-15]**: After passing the elimination protocol:
> "DERIVABILITY GATE [C-22]: Candidate tested against [n] topics. No single topic yields
> this conclusion alone. Insight approved."

If you cannot find a passing insight after 2 attempts: write:
> "DERIVABILITY GATE [C-22]: No cross-topic insight available with current data volume.
> Minimum cross-topic insight requires signals from 2+ topics."

Write the approved insight as a named artifact:

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence with specific numbers and names]
```

---

### WRITE ARTIFACT [C-08]

`simulations/corps/achievements-{{date}}.md`

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [label]
derivability_tested: true
---
```

---

## V-03 — C-23: Numbered Sub-Step Gate Language

**Axis**: All multi-condition gates use numbered sub-steps throughout the skill
**Hypothesis**: Applying numbered sub-steps to every multi-condition gate — not just the formula
gate — creates uniform gate discipline. A gate is either passed condition-by-condition or it
fails with a specific condition number cited. This prevents a gate from being treated as
satisfied when only some conditions are met. The variation establishes the gate language in a
preamble so it applies consistently. C-21 and C-22 are present at baseline (standard correction
loop + scope check), but C-23 is the structural differentiator applied universally.

---

You are running `corps-achievements`. No arguments — scan and compute from workspace state.

**Gate language**: All multi-condition gates in this skill use numbered sub-steps. A gate passes
only when every numbered condition is confirmed. If any condition fails, cite the condition number
in the gate failure message before halting or correcting.

---

### SCAN [C-01]

Glob `simulations/**/*.md`. Extract for each file:
- Topic path (subdirectory under `simulations/`)
- Namespace (first path segment)
- Contributor identity (frontmatter `author:`/`contributor:` or filename prefix)

**SCAN GATE [C-01]** — numbered sub-steps:
> "(1) `simulations/` is accessible.
>  (2) At least one `.md` file was found.
>  (3) Each file was assigned to a topic path.
>  (4) Each topic path is a real directory path from the glob results — not inferred or assumed."
>
> Confirm each condition. If condition (1) or (2) fails: "SCAN GATE FAIL [C-01]: condition ([n]) —
> workspace empty or inaccessible. Continuing with empty data."
> If condition (3) or (4) fails: name the specific file that could not be assigned.

State the final tally:
> "SCAN GATE [C-01]: Passed. [n] signals, [n] topics, [n] namespaces, contributors: [list]."

---

### ACHIEVEMENTS [C-02/C-06/C-07]

Achievement definitions:
- **First Signal** — >= 1 signal
- **Signal Depth** — >= 3 signals
- **Full Sweep** — signals span >= 3 distinct namespaces
- **Solo Pioneer** — exactly 1 contributor, >= 1 signal
- **Team Topic** — 2+ contributors with >= 1 signal each

Two labeled sections: **Earned Achievements** and **Locked Achievements**.
Every topic from the scan record appears in one section.

```markdown
## Earned Achievements — {{date}}

**[topic]** ([n] signals)
  - **[Achievement]**: [evidence]

## Locked Achievements

**[topic]** ([n] signals)
  - o [Achievement]: needs [gap]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps:
> "(1) Every topic I listed in the SCAN GATE appears in Earned or Locked Achievements.
>  (2) No topic from the scan record was omitted from the output.
>  (3) Every achievement entry names specific evidence (file count, contributor name, or namespace list)."
>
> If condition (1) or (2) fails: "COMPUTE GATE FAIL [C-02]: condition (1/2) — topic '[path]'
> missing from output. Adding before proceeding."
> If condition (3) fails: cite the specific entry missing evidence.

---

### TEAM MILESTONES [C-03]

```markdown
## Team Milestones

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [file path or "—"] | [gap or "—"] |
| shared coverage | EARNED / NOT YET | [contributors + topics or "—"] | [gap or "—"] |
| debate starter | EARNED / NOT YET | [topic + namespaces or "—"] | [gap or "—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps:
> "(1) The milestone named 'first team signal' appears in the table using that exact name.
>  (2) The milestone named 'shared coverage' appears in the table using that exact name.
>  (3) The milestone named 'debate starter' appears in the table using that exact name."
>
> If any condition fails: "MILESTONES GATE FAIL [C-03]: condition ([n]) — milestone
> '[written name]' must be renamed to '[exact name]' before proceeding."

---

### CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

**FORMULA GATE [C-19/C-21]** — numbered sub-steps:
> "(1) I will render the worked example: Score = {Signals}×1 + {Topics}×3 + {Milestones}×5 = {total}
>  (2) I will compare the calculated total to the Score column entry for Rank 1.
>  (3) If the calculated total does not match the Score column entry, I will correct the Score column
>      before proceeding.
>  (4) I will confirm that the corrected (or verified) value is now consistent with the formula."
>
> Execute each step. If condition (2) reveals a mismatch: correct the table per condition (3).
> Do not pass this gate until condition (4) is satisfied.
> State: "FORMULA GATE [C-19/C-21]: Passed. Rank-1 score = {total} (verified/corrected)."

If no contributor metadata: one row indicating this; gate passes with note "no formula applicable."

---

### 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There

| Topic / Milestone | Achievement | Gap | Exact Action |
|-------------------|-------------|-----|--------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps:
> "(1) I have checked every topic for achievements exactly 1 signal away from earning.
>  (2) I have checked every topic for achievements exactly 1 contributor away from earning.
>  (3) I have checked every team milestone for gaps exactly 1 namespace or contributor away.
>  (4) Each row in the table has all four columns populated: topic/target, achievement, gap, action."
>
> If any row is missing a column, cite the specific row: "1-AWAY GATE FAIL: row '[topic]'
> missing column '[column name]'."

If nothing within 1 step: single row "No single-step unlocks available."

---

### NEXT ACTIONS (ANTI-INERTIA) [C-05/C-12/C-14/C-17]

Stagnation Pattern Registry:
- `SOLO_ISLAND` / `NAMESPACE_MOAT` / `SPRINT_FREEZE` / `SHALLOW_POOL` / `ORPHAN_TOPIC`

```markdown
## Next Actions

1. **[action — namespace, topic]**
   → Unlocks **[Achievement/Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]
```

**ACTIONS GATE [C-05/C-12/C-14]** — numbered sub-steps:
> "(1) Each action names a specific namespace and topic — not generic advice.
>  (2) Each action names the exact achievement or milestone it unlocks.
>  (3) Each action references a pattern label from the registry (not an invented label).
>  (4) At least 3 actions are written."
>
> If any condition fails, cite the action number and condition:
> "ACTIONS GATE FAIL [C-05]: action 2, condition (1) — action does not name a specific topic."

**Pre-write self-test [C-11]** (runs before ACTIONS GATE):
> "Do I know the stagnation pattern from the scan? Do I have 3+ specific topics and namespaces
> ready to name? If not, review the scan record before writing."

---

### TEAM INSIGHT [C-10/C-13/C-22]

The insight must be cross-topic in scope. Apply a scope check before writing:
> "Does this insight span 2+ topics or 2+ contributors? If no, revise."

Write the approved insight as:

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight with specific numbers and names]
```

**INSIGHT GATE [C-10/C-13]** — numbered sub-steps:
> "(1) The insight is formatted as **TEAM INSIGHT — [name]:** making it a named, referenceable artifact.
>  (2) The insight names specific topics, contributors, or counts — not vague patterns.
>  (3) The insight draws a conclusion not derivable from any single topic view alone."
>
> If condition (3) fails: "INSIGHT GATE FAIL [C-10]: insight is derivable from topic '[path]' alone.
> Revise to require data from 2+ topics."

---

### WRITE ARTIFACT [C-08]

`simulations/corps/achievements-{{date}}.md`

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [label]
gate_language: numbered-substeps
---
```

---

## V-04 — C-21 + C-22: Correction Loop + Derivability Test (Combination)

**Axis**: Formula correction loop (C-21) combined with derivability elimination protocol (C-22)
**Hypothesis**: The correction loop and derivability test address the two most consequential synthesis
outputs — the contributor ranking and the team insight. Together they ensure: (a) the leaderboard
can be verified from raw counts and the formula, and (b) the insight genuinely requires cross-signal
reasoning. The two gates reinforce each other because both demand the model close a verification
loop rather than assert correctness. C-23 is applied selectively (formula gate only) to avoid
diluting the primary two axes with structural changes.

---

You are running `corps-achievements`. No arguments — scan and compute from workspace state.

---

### STEP 1 — Scan [C-01]

Glob `simulations/**/*.md`. Extract topic paths, namespaces, contributor identities.

**SCAN GATE [C-01]**:
> "SCAN GATE [C-01]: [n] signals, [n] topics, [n] namespaces, contributors: [list or 'not detectable'].
> If any topic path was inferred rather than found in glob results, name it here before proceeding."

Empty workspace: state and continue.

---

### STEP 2 — Achievements [C-02/C-06/C-07]

Compute earned and available achievements for each topic.

Definitions:
- **First Signal** — >= 1 signal
- **Signal Depth** — >= 3 signals
- **Full Sweep** — signals span >= 3 namespaces
- **Solo Pioneer** — exactly 1 contributor, >= 1 signal
- **Team Topic** — 2+ contributors, >= 1 signal each

```markdown
## Earned Achievements — {{date}}
[topic and earned achievements with evidence]

## Locked Achievements
[topic and locked achievements with specific gaps]
```

**COMPUTE GATE [C-02/C-15]**:
> "COMPUTE GATE [C-02]: [n] topics in scan, [n] topics in output.
> If any scan topic is absent from output: 'Missing topic: [path]. Adding before proceeding.'"

---

### STEP 3 — Team Milestones [C-03]

```markdown
## Team Milestones

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [evidence or "—"] | [gap or "—"] |
| shared coverage | EARNED / NOT YET | [evidence or "—"] | [gap or "—"] |
| debate starter | EARNED / NOT YET | [evidence or "—"] | [gap or "—"] |
```

Use exact milestone names. A renamed milestone fails C-03.

---

### STEP 4 — Contributor Leaderboard with Correction Loop [C-04/C-16/C-19/C-21]

**Pre-write self-test [C-11]**:
> "Do I have signal counts, topic counts, and milestone evidence for each contributor?
> Will I be able to render a worked example for Rank 1? If no, extract this data from
> the scan record before building the table."

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

**FORMULA CORRECTION GATE [C-19/C-21]** — numbered sub-steps:
> "(1) Render worked example: Score = {Signals}×1 + {Topics}×3 + {Milestones}×5 = {total}
>  (2) Compare to Score column entry for Rank 1.
>  (3) If calculated total does not match the Score column entry, correct the Score column
>      to the calculated total before proceeding.
>  (4) Confirm: 'Rank-1 score = {total} — verified/corrected.'"
>
> This gate does not pass until condition (4) is met.

---

### STEP 5 — 1-Away Gaps [C-09/C-18]

```markdown
## Almost There

| Topic / Milestone | Achievement | Gap | Exact Action |
|-------------------|-------------|-----|--------------|
```

Scan each topic for exactly-1-step unlocks. If none: single row "No single-step unlocks available."

---

### STEP 6 — Next Actions (Anti-Inertia) [C-05/C-12/C-14/C-17]

Identify stagnation pattern from registry:
- `SOLO_ISLAND` / `NAMESPACE_MOAT` / `SPRINT_FREEZE` / `SHALLOW_POOL` / `ORPHAN_TOPIC`

```markdown
## Next Actions

1. **[action — namespace, topic]**
   → Unlocks **[Achievement/Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]
```

At least 3 actions. Each names a specific namespace and topic.

---

### STEP 7 — Team Insight with Derivability Elimination [C-10/C-13/C-22]

Execute the derivability elimination protocol before writing the insight.

**Step A — Candidate**: State the candidate insight in one sentence.
> "Candidate: [insight]"

**Step B — Topic-by-topic elimination test**:
For each topic discovered in the scan, answer:
> "Can this insight be reached from [topic path] data alone? YES / NO"

List every topic with its verdict.

**Step C — Verdict and gate**:
- If all topics return NO:
  > "DERIVABILITY GATE [C-22]: All [n] topics tested. No single topic yields this conclusion.
  > Insight approved."
- If any topic returns YES:
  > "DERIVABILITY GATE [C-22]: Candidate derivable from topic '[path]' alone. Discarding.
  > Returning to Step A."
  Find a new candidate and repeat. Maximum 2 attempts. If no passing candidate is found:
  > "DERIVABILITY GATE [C-22]: Insufficient data for a non-derivable cross-topic insight.
  > Minimum requires signals from 2+ topics."

Write approved insight as named artifact:

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight with specific numbers and topic/contributor names]
```

---

### WRITE ARTIFACT [C-08]

`simulations/corps/achievements-{{date}}.md`

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [label]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
---
```

---

## V-05 — C-21 + C-22 + C-23: Full Combination (All Three New Criteria)

**Axis**: Correction loop (C-21) + derivability elimination (C-22) + numbered sub-step gate language throughout (C-23)
**Hypothesis**: All three new criteria together create a self-auditing skill where: (a) every
multi-condition gate enumerates its conditions as individually-checkable steps (C-23), (b) the
leaderboard formula has an active correction path (C-21), and (c) the team insight is tested
against every topic for single-topic derivability (C-22). C-23 applied universally makes the
C-21 and C-22 gates structurally consistent with all other gates — the skill reads as having
one gate language, not two ad-hoc verification patterns. This is the strongest structural
variation and the most auditable against the full rubric.

---

You are running `corps-achievements`. No arguments — scan and compute from workspace state.

**Gate standard**: Every multi-condition gate in this skill enumerates its conditions as numbered
sub-steps. Format: "(1) [condition]. (2) [condition]. (n) [condition]." A gate passes only when
every numbered condition is satisfied. Gate failure messages cite the specific condition number
and the specific instance (topic name, contributor name, or row) that triggered the failure.

---

### PHASE 1 — SCAN [C-01]

Glob `simulations/**/*.md`. For each file:
- Extract topic path (subdirectory under `simulations/`)
- Extract namespace (first path segment)
- Extract contributor (frontmatter `author:`/`contributor:` or filename prefix)

**SCAN GATE [C-01]** — numbered sub-steps:
> "(1) `simulations/` directory is accessible and the glob returned results.
>  (2) Every `.md` file found is assigned to a topic path from actual glob results —
>      no topic paths are inferred or assumed.
>  (3) Topics, namespaces, and contributors are recorded in an internal scan record.
>  (4) The scan record is complete — no file was skipped."
>
> State which conditions are satisfied. If condition (1) or (2) fails:
> "SCAN GATE FAIL [C-01]: condition ([n]) — [specific file or directory issue]. Continuing
> with empty data."
>
> Confirmation: "SCAN GATE [C-01]: Passed. [n] signals, [n] topics, [n] namespaces,
> contributors: [list or 'not detectable']."

---

### PHASE 2 — ACHIEVEMENTS [C-02/C-06/C-07]

Achievement definitions:
- **First Signal** — >= 1 signal
- **Signal Depth** — >= 3 signals
- **Full Sweep** — signals span >= 3 distinct namespaces
- **Solo Pioneer** — exactly 1 contributor, >= 1 signal
- **Team Topic** — 2+ contributors with >= 1 signal each

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement]**: [specific evidence — count, names, or namespace list]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement]: needs [specific gap — "2 more signals", "1 more contributor", etc.]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps:
> "(1) Every topic I listed in Phase 1 (SCAN GATE) appears in either Earned or Locked
>      Achievements — no topic is omitted.
>  (2) Every achievement entry in Earned names specific evidence (file count, contributor
>      name, or namespace list) — no bare achievement names without evidence.
>  (3) Every gap in Locked is quantified with a specific count or name — no vague 'needs
>      more signals.'"
>
> If condition (1) fails: "COMPUTE GATE FAIL [C-02]: condition (1) — topic '[path]' absent
> from output. Adding before proceeding."
> If condition (2) or (3) fails: cite the specific entry missing evidence or quantification.

---

### PHASE 3 — TEAM MILESTONES [C-03]

```markdown
## Team Milestones

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [file path or "—"] | [gap or "—"] |
| shared coverage | EARNED / NOT YET | [contributors + topics or "—"] | [gap or "—"] |
| debate starter | EARNED / NOT YET | [topic + namespaces or "—"] | [gap or "—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps:
> "(1) The milestone named 'first team signal' appears in the table with that exact name.
>  (2) The milestone named 'shared coverage' appears in the table with that exact name.
>  (3) The milestone named 'debate starter' appears in the table with that exact name.
>  (4) No milestone row is missing an Evidence cell — either a file path or explicit 'none found.'"
>
> If any condition fails: "MILESTONES GATE FAIL [C-03]: condition ([n]) — milestone
> '[written name]' must match '[exact name]' / row '[milestone]' missing Evidence cell."

---

### PHASE 4 — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**Pre-write self-test [C-11]**:
> "Do I have Signals, Topics, and Milestones counts for each contributor from the scan record?
> If no, I cannot compute scores — extract these counts now before building the table."

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

**FORMULA CORRECTION GATE [C-19/C-21]** — numbered sub-steps:
> "(1) Render worked example for Rank 1:
>      Score = {Signals}×1 + {Topics}×3 + {Milestones}×5 = {total}
>  (2) Compare the calculated total to the Score column entry for Rank 1 in the table above.
>  (3) If the calculated total does not match the Score column entry, correct the Score column
>      to the calculated total before proceeding. State: 'Score corrected from {old} to {new}.'
>  (4) Confirm consistency: the Score column entry for Rank 1 now equals the calculated total."
>
> This gate does not pass until condition (4) is confirmed.
> "FORMULA GATE [C-19/C-21]: Passed. Rank-1 score = {total} (verified / corrected from {old})."

If no contributor metadata: one row indicating this; gate passes with note "formula not applicable."

---

### PHASE 5 — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps:
> "(1) I have checked every topic for achievements exactly 1 signal away from earning.
>  (2) I have checked every topic for achievements exactly 1 contributor away from earning.
>  (3) I have checked every team milestone for gaps exactly 1 namespace, contributor, or
>      topic away.
>  (4) Every row in the Almost There table has all four columns populated: topic/target,
>      achievement, gap (exact count), exact action needed."
>
> If condition (4) fails: "1-AWAY GATE FAIL: row '[topic]' missing column '[column name]'.
> Adding before proceeding."
> If nothing is within 1 step: one row stating "No single-step unlocks available."

---

### PHASE 6 — NEXT ACTIONS (ANTI-INERTIA) [C-05/C-12/C-14/C-17]

Stagnation Pattern Registry:
- `SOLO_ISLAND` — one contributor owns all signals
- `NAMESPACE_MOAT` — all signals from one namespace
- `SPRINT_FREEZE` — no new signals in current sprint
- `SHALLOW_POOL` — multiple topics, none reaching Signal Depth
- `ORPHAN_TOPIC` — topics with no contributor metadata

Identify the pattern this workspace shows. Carry the label forward.

```markdown
## Next Actions

Stagnation pattern detected: **[PATTERN_LABEL from registry]**

1. **[action — specific namespace and topic]**
   → Unlocks **[Achievement or Milestone name]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence why this action disrupts the pattern]

2. ...
3. ...
```

**ACTIONS GATE [C-05/C-12/C-14/C-17]** — numbered sub-steps:
> "(1) Each action names a specific namespace and topic — not generic advice like 'add signals.'
>  (2) Each action names the exact achievement or milestone it unlocks — not a category.
>  (3) Each action references a pattern label from the Stagnation Pattern Registry using
>      the exact label syntax — no invented labels.
>  (4) At least 3 actions are written.
>  (5) The pattern label in each action row is the same label identified at the top of this
>      phase — no label drift between actions."
>
> If any condition fails: "ACTIONS GATE FAIL [C-05]: action [n], condition ([n]) —
> [specific issue: missing topic, unlocked achievement not named, invented label, etc.]"

---

### PHASE 7 — TEAM INSIGHT WITH DERIVABILITY ELIMINATION [C-10/C-13/C-22]

Execute the derivability elimination protocol. Do not skip to writing the insight.

**Step A — Candidate**: State the candidate insight in one sentence.
> "Candidate: [insight sentence with specific numbers and names]"

**Step B — Elimination test**: Test the candidate against each topic individually.
For each topic path in the scan record:
> "Can this insight be reached from [topic path] data alone, without any other topic?
> Answer: YES / NO"

List every topic path and its answer.

**Step C — Verdict**:
- If all answers are NO: the candidate passes.
  > "DERIVABILITY GATE [C-22]: [n] topics tested. No single topic yields this conclusion alone.
  > Candidate approved."
- If any answer is YES: the candidate is derivable from a single topic. Discard it.
  > "DERIVABILITY GATE [C-22]: Candidate derivable from topic '[path]' alone. Discarding.
  > Returning to Step A with a new candidate."
  Repeat Steps A–C with a new candidate. Maximum 2 attempts. If no passing candidate:
  > "DERIVABILITY GATE [C-22]: Insufficient cross-topic data. Requires signals from 2+ topics."

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps (applies after Step C passes):
> "(1) The insight is written as **TEAM INSIGHT — [name]:** making it a named, referenceable artifact.
>  (2) The insight names specific topics, contributors, or numeric values — not only pattern labels.
>  (3) The insight passed the derivability elimination test in Step C — confirmed not derivable
>      from any single topic alone."
>
> If any condition fails: cite the condition number and specific issue before revising.

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence with specific numbers and topic/contributor names]
```

---

### WRITE ARTIFACT [C-08]

`simulations/corps/achievements-{{date}}.md`

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [label]
gate_language: numbered-substeps
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
c23_gate_language: numbered-substeps-universal
---
```
