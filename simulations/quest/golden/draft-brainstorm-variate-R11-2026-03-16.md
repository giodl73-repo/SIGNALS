---
skill: quest-variate
skill_target: draft-brainstorm
round: 11
date: 2026-03-16
rubric_version: 11
r10_scores_under_v11: "V-03 R10 = 160 (C-33 PASS -- both anchors verbatim: Selected? column rule AND Phase 3 GATE block; C-34 PASS -- 'so the comparison can pass' present), V-04 R10 = 160 (C-33 PASS -- Step 5 column rule verbatim AND Step 8 GATE block verbatim; C-34 PASS), V-01 R10 = 155 (C-33 FAIL -- anchor b verbatim but anchor a label-reference; C-34 PASS), V-02 R10 = 150 (C-33 FAIL, C-34 FAIL -- 'the desire to revise' without comparison-goal qualifier)"
r11_target: "160 -- confirm C-33 and C-34 are structurally stable across: (a) AMEND-first role sequence where lenses precede generation, (b) prose-category format where ideas use bold headers instead of ## sections, (c) full inertia-Phase-0 framing where Do Nothing gets a dedicated baseline analysis block, (d) AMEND-first plus conversational register combined, (e) prose-categories plus explicit gate blocks at every transition plus inertia-Phase-0 combined"
---

# Variate R11 -- draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01, V-02, V-03), then combinations (V-04, V-05).

R11 targets the two v11 criteria introduced in rubric v11:
- **C-33** Dual-Anchor Verbatim Full Parity -- C-31 is the floor (phase-entry anchor
  verbatim); C-33 is the ceiling: BOTH anchors verbatim -- the schema-definition
  anchor (Selected? column rule) AND the phase-entry anchor (GATE block) both name
  the full condition text with schema element names. A variation where anchor (a) uses
  label-reference or descriptive language while anchor (b) is verbatim satisfies C-31
  but fails C-33.
- **C-34** Negation Frame Comparison-Goal Qualification -- C-32 is the floor (causally
  specific inversion + dual-frame negation+affirmation); C-34 is the ceiling: the
  negation frame additionally names the goal behind the prohibited impulse -- "so the
  comparison can pass" or equivalent -- narrowing the prohibition to
  comparison-goal-directed revision specifically.

---

## Variation Axes

| Axis | Description |
|------|-------------|
| Role sequence | Which roles run first; whether AMEND precedes or follows pool generation |
| Output format | ## dimension sections vs bold-header prose categories vs numbered list |
| Lifecycle emphasis | How explicitly phase-advance gates are restated at each transition |
| Phrasing register | Formal/imperative vs conversational/second-person throughout |
| Inertia framing | How much structural space the Do Nothing baseline receives |

## Single-axis variations

---

### V-01 -- Role Sequence: AMEND-First

**Axis**: Role sequence
**Hypothesis**: Moving AMEND to Stage 0 -- before pool generation -- converts the
3 pool-shift directions from retrospective filters into production constraints that
actively shape which ideas get generated. Ideas written against explicit lenses should
be more intentionally diverse and less dominated by center-of-gravity candidates. Tests
whether C-33 and C-34 survive when the AMEND role precedes generation rather than
following it, and whether the lens-attribution requirement (ideas tagged to lenses
during generation) alters verification phase behavior.

**Expected**: C-01..C-32 PASS (inh) + C-33 PASS (anchor a: Selected? column rule
verbatim with schema element names AND anchor b: Stage 3 GATE block same verbatim
conditions) + C-34 PASS ("so the comparison can pass" in Prohibition B negation frame)
= **160**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in four stages: AMEND (set lenses), GENERATE (pool using lenses),
VERIFY (peer-comparison), FINALIZE. Complete each stage in order.

---

## Stage 0 -- AMEND: Generative Lenses

Before generating any ideas, state 3 pool-shift directions. These are production
constraints -- they determine which ideas appear in Stage 1, not which ideas survive
a post-hoc filter.

For each lens:
- **Lens name**: one phrase (e.g., "More Ambitious", "Audience Shift", "Incremental")
- **Direction**: one sentence describing the shift axis
- **Pool impact**: what kinds of ideas appear under this lens that would not appear
  without it; name candidate types, not framing differences

A lens is valid only if a reader could re-run the brainstorm with only that lens and
get ideas that do not appear in the current pool -- different candidates, not the same
candidates under different labels.

Write all 3 lenses. Do not begin Stage 1 until all 3 are written.

---

## Stage 1 -- GENERATE

### 1a. Inertia Frame

Write a paragraph (3-5 sentences) describing the current trajectory for {{topic}}:
What is already in motion? What does the team inherit if no deliberate decision is
made? What does the path of least resistance produce -- technically, organizationally,
or for users?

This paragraph appears as the first element in the final artifact, before any ideas.

### 1b. Idea Pool

Generate 20-40 candidates for {{topic}}. Your output must contain one labeled section
per required dimension. Each is a **mandatory `##` section** -- do not collapse into
a flat list, do not omit any. You may add sections beyond the six required.

**Required dimensions (each must appear as a `##` section):**
- **Scope** -- how much of {{topic}}'s problem space is addressed
- **Timing** -- when the intervention lands in the product lifecycle
- **Integration** -- how it connects to existing systems or teams
- **Audience** -- who benefits most
- **Build vs. Buy** -- internal build, external adoption, or extension of existing
- **Status Quo** -- the inertia option (exactly one idea: Do Nothing)

**Lens attribution**: Distribute Stage 0 lenses explicitly. Generate at least 2 ideas
per lens. After writing an idea influenced by a lens, add a parenthetical: `[Lens: X]`.
Aim for at least 6 lens-influenced ideas total; center-of-gravity ideas that belong to
no lens are permitted but must not dominate.

**Do not mark top-5 yet.** Generate the full pool before selecting. Do not place any
`**` markers on any idea during Stage 1. Marking as you write introduces sequential
bias -- finish the pool first.

For each idea:
```
### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this serves {{topic}} specifically -- cite a real constraint, user
need, or opportunity. No generic reasoning.
```

**Required**: Include **Do Nothing** in the Status Quo section. Its rationale must
extend the framing paragraph from 1a -- what the current trajectory concretely
produces for {{topic}}.

---

## Stage 2 -- VERIFY

**Check A -- Sequential Default**
Identify 5 top-5 candidates. Are they the first 5 ideas generated? If yes, rescan the
full pool -- the strongest ideas surface across the whole run, not at the start. Output
of Check A: 5 candidates advancing to the Registry.

**Check B -- Peer-Comparison Registry**

For each of the 5 candidates, write one row. Do not fill in Selected? during
construction.

| # | Candidate (exact name from pool) | Peer (exact name, same ## section, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|----------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Column rules:**
- **Candidate**: exact idea name from Stage 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same `##` section; cannot
  be blank
- **"I chose ... because ___"**: complete the sentence with a specific reason tied to
  {{topic}}'s actual constraints (scope, user group, cost, risk); "it is better" or
  "more viable" do not count
- **Selected?**: Stage-advance gate. This column cannot hold any value, and Stage 3
  cannot begin, until both preconditions hold simultaneously: (a) all 5 rows of this
  Registry are written in your output, AND (b) Selected? is blank across all 5 rows.
  A partial Registry has no valid Selected? entries. A Registry where any Selected?
  cell carries a preliminary value does not satisfy the gate. Stage 3 may begin only
  when the Registry is structurally complete (5 rows) and selection-clean (Selected?
  blank in every row). This is a schema property of the Registry.

**Prohibition Battery:**

**Prohibition A -- Marking Ban**: Do not place any `**` marks anywhere in your output
while Stage 2 Check B is in progress -- not on headings, inline, in notes, or in any
other form. No `**` marks may appear until the complete 5-row Registry is written.

**Prohibition B -- Rationalization Block**: If you cannot complete the comparison
sentence for any row -- no specific peer holds or no specific reason applies -- that
candidate must be replaced by the peer named in the Peer column. The replacement
source is fixed: it is the peer from this row, not an alternative selected after
reconsidering. Do not revise the candidate's rationale to manufacture a distinction
that was not present at comparison time. If editing the candidate's rationale would
make the comparison sentence completable, that desire confirms the replacement
obligation applies -- the impulse to revise so the comparison can pass is not
permission to reopen the comparison; it is the signal the swap is mandatory.

**Check C -- Lens Coverage**
For each Stage 0 lens, confirm at least 2 ideas in the pool carry that lens's
attribution tag. If any lens has fewer than 2 ideas, that lens failed as a production
constraint. Note which lens underperformed. Apply the distribution-shift test to each
AMEND direction: re-running with only that direction must produce ideas not in the
current pool. Sharpen any direction that would produce the same candidates under a
different frame.

**Check D -- Inertia Placement**
Does the Stage 1a paragraph appear as the first element in the artifact? If not,
reorder.

---

## Stage 3 -- FINALIZE

> **GATE PRECONDITIONS -- both must hold before Stage 3 may begin:**
> - **(a)** All 5 rows of the Peer-Comparison Registry are written in your output
> - **(b)** Selected? is blank across all 5 rows of the Registry
>
> A Registry with fewer than 5 rows does not satisfy (a). A Registry where any
> Selected? cell holds any value does not satisfy (b). Both conditions must hold
> simultaneously before any finalization step below may proceed.

Fill Selected? = YES in exactly 5 rows (candidates confirmed in Check B, with any
substitutions from Prohibition B applied). Mark those 5 ideas with `**` on their
headings in the dimension sections. Use the Stage 0 AMEND lenses, sharpened by Check
C findings.

Write the artifact to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Inertia paragraph (1a), dimension sections (top-5 marked, lens
attribution tags removed in final artifact), Peer-Comparison Registry, AMEND (3
lenses from Stage 0, distribution-shift-verified). Total ideas including Do Nothing:
20-40.
```

---

### V-02 -- Output Format: Prose Category Groups (No ## Dimension Sections)

**Axis**: Output format
**Hypothesis**: Replacing mandatory `##` dimension sections with bold-labeled prose
category groups removes the structural spine guarantee (C-15) from the format while
preserving the Registry gate mechanism. Ideas in bold-header groups rather than ##
sections changes how the "same section" Peer rule is interpreted -- "same **Category**
group" replaces "same ## section." Tests whether C-33 and C-34 survive the format
change and whether the loss of ## structural guarantee changes pool quality. Expected
to expose a tradeoff: more flexible pool organization but reduced structural coverage
enforcement.

**Expected**: C-01..C-14 PASS (inh), C-15 FAIL (no ## sections = no structural spine
guarantee), C-16..C-32 PASS (inh) + C-33 PASS (anchor a: Selected? column rule
verbatim AND anchor b: Phase 3 GATE block verbatim) + C-34 PASS ("so the comparison
can pass" present) = **157.5** (C-15 costs 2.5)

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in two phases: GENERATE, then VERIFY. Do not finalize the artifact
until you have completed the verification step.

---

## PHASE 1 -- GENERATE

### 1a. Inertia Frame

Write a paragraph (3-5 sentences) describing the current trajectory for {{topic}}:
What is already in motion? What does the team inherit if no deliberate decision is
made? What does the path of least resistance produce -- technically, organizationally,
or for users?

This paragraph must appear as the first element in the final artifact, before any
ideas.

### 1b. Idea Pool

Generate 20-40 candidates for {{topic}} as a flowing prose-grouped list. Organize
ideas under bold category headers -- not `##` headings. Each group is a thematic
cluster; choose 4-7 distinct categories that represent genuinely different dimensions
(e.g., scope, timing, integration approach, audience, build vs. buy, risk tolerance).

**Do not mark top-5 yet.** Complete the full pool before selecting. Do not place
any `**` markers on any idea during Phase 1. Marking as you write introduces
sequential bias -- finish the pool first.

Format each group as:

```
**[Category Name]**

**[Idea Name]**: [one-sentence pitch] -- [one-to-two sentence rationale citing a
real constraint, user need, or opportunity specific to {{topic}}. No generic reasoning.]
```

**Required**: One idea in this pool must be **Do Nothing** (group it under a
**Status Quo** category). Its rationale must extend the framing paragraph from 1a --
what the current trajectory concretely produces for {{topic}}.

### 1c. AMEND Draft

Write a draft AMEND section with 3 pool-shift directions. For each:
- Name the shift axis
- Describe what ideas would appear or disappear
- Apply the re-run test: if a reader took only this directive and re-ran the brainstorm,
  would the resulting pool contain candidate ideas not in the current pool? Different
  ideas, not the same ideas under different framing. A direction that shifts only
  category labels or emphasis without introducing different underlying candidates fails
  this test.

Do not finalize yet.

---

## PHASE 2 -- VERIFY

**Check A -- Sequential Default**
Identify your 5 top-5 candidates. Are they the first 5 ideas generated? If yes, rescan
the full pool -- the strongest ideas surface across the whole run. Output: 5 candidates
advancing to Check B.

**Check B -- Peer-Comparison Registry**

For each of the 5 candidates, write one row. Do not fill in Selected? during
construction.

| # | Candidate (exact name from pool) | Peer (exact name, same **Category** group, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|------------------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Column rules:**
- **Candidate**: exact idea name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same bold **Category**
  group; cannot be blank
- **"I chose ... because ___"**: complete the sentence with a specific reason tied to
  {{topic}}'s actual constraints (scope, user group, cost, risk); "it is better" or
  "more viable" do not count
- **Selected?**: Phase-advance gate. This column cannot hold any value, and Phase 3
  cannot begin, until both preconditions hold simultaneously: (a) all 5 rows of this
  Registry are written in your output, AND (b) Selected? is blank across all 5 rows.
  A partial Registry has no valid Selected? entries. A Registry where any Selected?
  cell carries a preliminary value does not satisfy the gate. Phase 3 may begin only
  when the Registry is structurally complete (5 rows) and selection-clean (Selected?
  blank in every row). This is a schema property of the Registry.

**Prohibition Battery:**

**Prohibition A -- Marking Ban**: Do not place any `**` marks designating top-5
selection anywhere in your output while Check B is in progress -- not on idea names,
inline, in notes, or in any other form. No top-5 `**` marks may appear until the
complete 5-row Registry is written.

**Prohibition B -- Rationalization Block**: If you cannot complete the comparison
sentence for any row -- no specific peer holds or no specific reason applies -- that
candidate must be replaced by the peer named in the Peer column. The replacement
source is fixed: it is the peer from this row. Do not revise the candidate's rationale
to manufacture a distinction that was not present at comparison time. If editing the
candidate's rationale would make the comparison sentence completable, that desire
confirms the replacement obligation applies -- the impulse to revise so the comparison
can pass is not permission to reopen the comparison; it is the signal the swap is
mandatory.

**Check C -- AMEND Distribution-Shift Test**
For each of the 3 AMEND directions from 1c, verify the re-run test: re-running with
only this directive must surface candidate ideas not in the current pool. A directive
that shifts framing without introducing different underlying candidates fails. Sharpen
any that fail. Output of Check C: final AMEND content.

**Check D -- Inertia Placement**
Does the framing paragraph from 1a appear as the first element in the artifact?
If not, reorder.

---

## PHASE 3 -- FINALIZE

> **GATE PRECONDITIONS -- both must hold before Phase 3 may begin:**
> - **(a)** All 5 rows of the Peer-Comparison Registry are written in your output
> - **(b)** Selected? is blank across all 5 rows of the Registry
>
> A Registry with fewer than 5 rows does not satisfy (a). A Registry where any
> Selected? cell holds any value does not satisfy (b). Both conditions must hold
> simultaneously before any finalization step below may proceed.

Fill Selected? = YES in exactly 5 rows (candidates confirmed by Check B, with any
substitutions from Prohibition B applied). Mark those 5 idea names with `**` in the
prose-grouped idea list. Use the AMEND content finalized in Check C.

Write the artifact to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Inertia paragraph, prose category groups (top-5 marked), Peer-
Comparison Registry, AMEND. Total ideas including Do Nothing: 20-40.
```

---

### V-03 -- Inertia Framing: Full Phase 0 Baseline Analysis

**Axis**: Inertia framing
**Hypothesis**: Elevating "Do Nothing" from a framing paragraph + pool entry into a
full Phase 0 structural block -- with explicit current trajectory, cost analysis, and
displacement target -- creates a comparison anchor that all generated ideas are
positioned against. Ideas generated after writing a detailed inertia baseline should
have sharper rationales that explicitly name what changes relative to the default
trajectory. Tests whether C-33 and C-34 survive when inertia analysis receives its
own phase with output requirements, and whether the displacement target field changes
how Peer-Comparison candidates are selected.

**Expected**: C-01..C-32 PASS (inh) + C-33 PASS (anchor a: Selected? column rule
verbatim AND anchor b: Phase 4 GATE block verbatim) + C-34 PASS ("so the comparison
can pass" present) = **160**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in four phases: BASELINE (inertia), GENERATE (pool), VERIFY
(peer-comparison), FINALIZE. Complete each phase in order.

---

## PHASE 0 -- BASELINE: Define the Inertia Competitor

Before generating any candidate ideas, fully specify what "doing nothing" looks like
for {{topic}}. This is the most important entry in the pool: it is the option already
in play, and every other candidate exists to displace it.

Write the following four fields:

**Current Trajectory**: What is happening to {{topic}} right now with no deliberate
intervention? Name the specific direction the system, team, or product is already
moving. (2-3 sentences.)

**Accumulated Cost**: What concretely accumulates -- technically, organizationally,
or for users -- if this trajectory continues for 12 months? Be specific: what is
delayed, degraded, or foreclosed? (2-3 sentences.)

**Displacement Target**: What must a competing idea change about the trajectory to
beat this baseline? State the minimum threshold: "A candidate beats Do Nothing if
and only if it [specific condition]." (1 sentence.)

**Do Nothing** (pool entry):
```
**Pitch**: [One sentence summarizing the status quo trajectory from the above analysis]
**Rationale**: [The Accumulated Cost, compressed to one sentence]
```

This completes Phase 0. The Do Nothing entry from Phase 0 will appear in the Status
Quo dimension section of Phase 1. All other candidates will be evaluated against the
Displacement Target.

---

## PHASE 1 -- GENERATE: Idea Pool

### 1a. Inertia Frame

Write a paragraph (3-5 sentences) expanding on the Phase 0 baseline for a general
reader: What is the current trajectory for {{topic}}? What does the team inherit if
no deliberate decision is made? What does the path of least resistance produce?

This paragraph must appear as the first element in the final artifact.

### 1b. Idea Pool

Generate 19-39 additional ideas for {{topic}} (for a total pool of 20-40 including
the Phase 0 Do Nothing entry). Your output must contain one labeled section per
required dimension. Each is a **mandatory `##` section** -- do not collapse into a
flat list, do not omit any. You may add sections beyond the six required.

**Required dimensions (each must appear as a `##` section):**
- **Scope** -- how much of {{topic}}'s problem space is addressed
- **Timing** -- when the intervention lands in the product lifecycle
- **Integration** -- how it connects to existing systems or teams
- **Audience** -- who benefits most
- **Build vs. Buy** -- internal build, external adoption, or extension of existing
- **Status Quo** -- contains exactly the Do Nothing entry from Phase 0

For each idea (other than Do Nothing):
```
### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this serves {{topic}} specifically -- cite a real constraint, user
need, or opportunity. Include one sentence naming how this idea changes the Phase 0
trajectory: what specifically does it displace or prevent?
```

**Do not mark top-5 yet.** Generate the complete pool before selecting. Do not place
any `**` markers on any idea during Phase 1. Marking as you write introduces
sequential bias -- finish the pool first.

### 1c. AMEND Draft

Write a draft AMEND section with 3 pool-shift directions. For each:
- Name the shift axis
- Describe what ideas would appear or disappear
- Apply the re-run test: re-running with only this directive must produce candidate
  ideas not in the current pool. Different ideas, not the same ideas under different
  framing.

Do not finalize yet.

---

## PHASE 2 -- VERIFY: Peer-Comparison

**Check A -- Sequential Default**
Identify 5 top-5 candidates. Are they the first 5 ideas generated? If yes, rescan the
full pool. Output: 5 candidates advancing to the Registry.

**Check B -- Peer-Comparison Registry**

For each of the 5 candidates, write one row. Do not fill in Selected? during
construction.

| # | Candidate (exact name from pool) | Peer (exact name, same ## section, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|----------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Column rules:**
- **Candidate**: exact idea name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same `##` section; cannot
  be blank
- **"I chose ... because ___"**: complete the sentence with a specific reason tied to
  {{topic}}'s actual constraints (scope, user group, cost, risk); "it is better" or
  "more viable" do not count
- **Selected?**: Phase-advance gate. This column cannot hold any value, and Phase 4
  cannot begin, until both preconditions hold simultaneously: (a) all 5 rows of this
  Registry are written in your output, AND (b) Selected? is blank across all 5 rows.
  A partial Registry has no valid Selected? entries. A Registry where any Selected?
  cell carries a preliminary value does not satisfy the gate. Phase 4 may begin only
  when the Registry is structurally complete (5 rows) and selection-clean (Selected?
  blank in every row). This is a schema property of the Registry.

**Prohibition Battery:**

**Prohibition A -- Marking Ban**: Do not place any `**` marks anywhere in your output
while Phase 2 Check B is in progress. No `**` marks may appear until the complete
5-row Registry is written.

**Prohibition B -- Rationalization Block**: If you cannot complete the comparison
sentence for any row -- no specific peer holds or no specific reason applies -- that
candidate must be replaced by the peer named in the Peer column. The replacement
source is fixed: it is the peer from this row. Do not revise the candidate's rationale
to manufacture a distinction that was not present at comparison time. If editing the
candidate's rationale would make the comparison sentence completable, that desire
confirms the replacement obligation applies -- the impulse to revise so the comparison
can pass is not permission to reopen the comparison; it is the signal the swap is
mandatory.

**Check C -- AMEND Distribution-Shift Test**
For each of the 3 AMEND directions from 1c, verify: re-running with only this
directive must surface candidate ideas not in the current pool. Sharpen any that
would produce the same candidates under different framing.

**Check D -- Inertia Placement**
Does the Phase 1a paragraph appear as the first element in the artifact? If not,
reorder.

---

## PHASE 4 -- FINALIZE

> **GATE PRECONDITIONS -- both must hold before Phase 4 may begin:**
> - **(a)** All 5 rows of the Peer-Comparison Registry are written in your output
> - **(b)** Selected? is blank across all 5 rows of the Registry
>
> A Registry with fewer than 5 rows does not satisfy (a). A Registry where any
> Selected? cell holds any value does not satisfy (b). Both conditions must hold
> simultaneously before any finalization step below may proceed.

Fill Selected? = YES in exactly 5 rows (candidates confirmed in Check B, with any
substitutions from Prohibition B applied). Mark those 5 ideas with `**` on their
headings in the dimension sections. Use the AMEND content finalized in Check C.

Write the artifact to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Inertia paragraph (1a), Phase 0 baseline block (Trajectory / Cost /
Displacement Target), dimension sections (top-5 marked), Peer-Comparison Registry,
AMEND. Total ideas including Do Nothing: 20-40.
```

---

## Combined-axis variations

---

### V-04 -- AMEND-First + Conversational Register

**Axes**: Role sequence (AMEND before generation) + Phrasing register (conversational
second-person throughout)
**Hypothesis**: Conversational "you" framing reduces the cognitive overhead of parsing
prescriptive instructions, making the structural requirements (Registry construction,
gate conditions, Prohibition Battery) feel less bureaucratic and more like a natural
facilitated session. AMEND-first ensures lenses shape generation rather than retrofit
it. Together these test whether C-33's verbatim-anchor requirement and C-34's
comparison-goal qualifier survive when: (a) the structural order is non-standard and
(b) the register is deliberately informal. A conversational register risks diluting
the precision of the verbatim conditions and dual-frame language -- this variation
confirms whether precision survives informality.

**Expected**: C-01..C-32 PASS (inh) + C-33 PASS (anchor a: Selected? column rule
verbatim in conversational prose AND anchor b: finalize-step GATE block verbatim) +
C-34 PASS ("so the comparison can pass" survives register change) = **160**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

Here's the shape of what you're about to do: name your lenses first, then brainstorm
against them, then stress-test your top picks, then write the artifact. Four steps --
don't skip ahead.

---

### Step 0 -- Name Your Lenses

Before you generate a single idea, define 3 directions that will intentionally pull
the pool somewhere it wouldn't go on its own. You'll use these as active constraints
during generation -- not as a retrospective filter after the pool is already written.

For each lens, answer:
- What's the shift? (one phrase: "More Conservative", "Different Primary User", etc.)
- What changes? (one sentence: what kind of ideas appear under this lens that wouldn't
  appear in a default brainstorm?)
- Does it pass the re-run test? A reader who took only this lens and re-ran the
  brainstorm should get ideas not in your current pool -- different candidates, not
  the same candidates in different wording.

Write all 3 lenses. Don't start Step 1 until they're written.

---

### Step 1 -- Frame the Inertia

Before generating alternatives, write a short paragraph (3-5 sentences) about what
happens to {{topic}} if the team makes no deliberate decision. What's already in
motion? What does the path of least resistance produce -- for users, for the team, or
technically? This paragraph goes first in the artifact, before any ideas.

---

### Step 2 -- Build the Pool

Generate 20-40 candidates for {{topic}}. You need these sections in your output --
each as a `##` heading, not collapsed into a flat list:

**Required sections (all mandatory):**
- `## Scope` -- how much of {{topic}}'s problem space is addressed
- `## Timing` -- when the intervention lands in the product lifecycle
- `## Integration` -- how it connects to existing systems or teams
- `## Audience` -- who benefits most
- `## Build vs. Buy` -- internal build, external adoption, or extension of existing
- `## Status Quo` -- exactly one idea: Do Nothing

**Using your lenses**: Generate at least 2 ideas per lens and tag them inline
(e.g., `[Lens: More Conservative]`). Center-of-gravity ideas are fine too -- just
don't let them crowd out lens-influenced ideas.

**Don't mark top-5 yet.** Finish the whole pool before picking. Don't put `**` on
anything during Step 2 -- you'll introduce sequential bias if you mark as you go.

Each idea:
```
### [Idea Name]
**Pitch**: One sentence.
**Rationale**: Why this serves {{topic}} specifically. Real constraint, user need, or
opportunity -- no generic reasoning.
```

**Do Nothing** goes in `## Status Quo`. Its rationale should extend the Step 1 inertia
paragraph -- what does the current trajectory actually produce for {{topic}}?

---

### Step 3 -- Draft AMEND

Write a draft AMEND section: 3 directions for a future run of this brainstorm. For
each direction, describe what kinds of ideas would appear that aren't in this pool --
different candidate types, not different framing of the same ideas. You'll finalize
this in Step 6 after a distribution check.

---

### Step 4 -- Sequential Check

Look at your 5 candidates for top-5. Are they the first 5 you wrote? If yes, that's
sequential default -- rescan the full pool. The strongest candidates aren't necessarily
the first ones you thought of.

---

### Step 5 -- Build the Registry

For each of your 5 candidates, write one row. Leave the Selected? column blank while
you're building the table.

| # | Candidate (exact name from pool) | Peer (exact name, same ## section, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|----------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Column rules:**
- **Candidate**: exact idea name from Step 2; one of the 5 from Step 4
- **Peer**: exact name of one specific unmarked idea in the same `##` section; can't
  be blank
- **"I chose ... because ___"**: complete the sentence with a real reason tied to
  {{topic}}'s constraints (scope, user group, cost, risk); "it is better" doesn't count
- **Selected?**: Step-advance gate. This column can't hold any value, and Step 6 can't
  begin, until both hold at the same time: (a) all 5 rows of this Registry are written
  in your output, AND (b) Selected? is blank across all 5 rows. An incomplete Registry
  has no valid Selected? entries. A Registry where any Selected? cell has a value --
  even a draft value -- doesn't satisfy the gate. Step 6 opens only when the Registry
  has all 5 rows written AND every Selected? cell is blank. This is a property of the
  Registry schema.

**Two rules that apply without exception while Step 5 is in progress:**

**Rule 1 -- No marking**: Don't put any `**` anywhere while you're working on the
Registry -- not on headings, not inline, not as notes. No `**` marks appear until
the full 5-row Registry is in your output.

**Rule 2 -- No rationalization**: If you can't complete the comparison sentence for
a row -- no peer works, or no real reason applies -- replace that candidate with the
peer you named in the Peer column. The swap source is fixed: it's the peer in that
row, not a different idea you pick after going back to reconsider. Don't rewrite the
candidate's rationale to manufacture a distinction that wasn't there at comparison
time. If editing the rationale would make the comparison sentence completable, that
desire confirms the replacement applies -- the impulse to revise so the comparison
can pass is not permission to reopen the comparison; it is the signal the swap is
mandatory.

---

### Step 6 -- Finalize

> **GATE: Step 6 begins only after both conditions hold simultaneously:**
> - **(a)** All 5 rows of the Peer-Comparison Registry are written in your output
> - **(b)** Selected? is blank across all 5 rows of that Registry
>
> A Registry with fewer than 5 rows doesn't satisfy (a). Any value in any Selected?
> cell doesn't satisfy (b). Verify both before proceeding.

Fill Selected? = YES in exactly 5 rows (confirmed candidates from Step 5, with any
swaps from Rule 2 applied). Mark those 5 ideas with `**` on their `###` headings.

Check your 3 AMEND directions from Step 3: does each pass the re-run test? If any
would produce the same ideas under different framing, sharpen it now.

Write the artifact to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Inertia paragraph (Step 1), dimension sections (top-5 marked, lens
tags removed), Peer-Comparison Registry (Step 5), AMEND (3 finalized directions). Total
ideas including Do Nothing: 20-40.
```

---

### V-05 -- Prose Categories + Explicit Gate Blocks at Every Transition + Inertia Phase 0

**Axes**: Output format (bold-header prose categories, no ## dimension sections) +
Lifecycle emphasis (explicit GATE block at every phase boundary, not only at finalize) +
Inertia framing (full Phase 0 baseline block before generation)
**Hypothesis**: Maximum structural explicitness across all three axes produces the
clearest C-33/C-34 signal: verbatim conditions appear in both anchor positions, every
phase boundary enforces its own explicit gate, and the inertia analysis precedes all
other output. Tests whether C-33 and C-34 survive when: (a) the idea-pool format
changes from ## sections to bold-header prose groups, (b) gate blocks appear at every
transition (not only before finalization), and (c) the inertia analysis is a full
structural phase. The format change (from ## to bold headers) also tests C-15 -- the
structural spine guarantee -- which is expected to fail under this format.

**Expected**: C-01..C-14 PASS (inh), C-15 FAIL (bold headers not ## sections), C-16..
C-32 PASS (inh) + C-33 PASS (anchor a: Selected? column rule verbatim AND anchor b:
Phase 4 GATE block verbatim) + C-34 PASS ("so the comparison can pass" in Prohibition
B) = **157.5** (C-15 costs 2.5)

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in four phases. Each phase opens with an explicit GATE that must be
satisfied before any work in that phase may begin.

---

## PHASE 0 -- BASELINE

> **GATE: Phase 0 begins unconditionally. Complete all fields before Phase 1.**

Define the status quo competitor. This is the most important entry in the pool:
it is the option already in play.

**Current Trajectory**: What is happening to {{topic}} right now with no intervention?
Name the specific direction already in motion. (2-3 sentences.)

**Accumulated Cost**: What concretely accumulates -- technically, organizationally,
or for users -- if this trajectory continues for 12 months? (2-3 sentences.)

**Displacement Target**: What must a competing idea change to beat this baseline?
"A candidate beats Do Nothing if and only if it [specific condition]." (1 sentence.)

**Do Nothing** (pool entry to be placed in the Status Quo category in Phase 1):
- **Pitch**: [One sentence from the Trajectory analysis above]
- **Rationale**: [The Accumulated Cost compressed to one sentence]

Phase 0 is complete when: all four fields are written and non-empty.

---

## PHASE 1 -- GENERATE

> **GATE: Phase 1 may begin only after Phase 0 is complete (all fields written).**

### 1a. Inertia Frame

Write a paragraph (3-5 sentences) expanding the Phase 0 baseline for a general reader:
What is the current trajectory for {{topic}}? What does the team inherit if no
deliberate decision is made? This paragraph appears as the first element in the final
artifact.

### 1b. Idea Pool

Generate 19-39 additional ideas for {{topic}} (total pool including Do Nothing: 20-40).
Organize ideas under bold-labeled category headers -- not `##` headings. Choose 4-7
thematic categories representing genuinely different dimensions (examples: scope,
timing, integration approach, audience, build vs. buy, risk tolerance, organizational
change, tooling). Use a **Status Quo** category to hold the Phase 0 Do Nothing entry.

**Do not mark top-5 yet.** Generate the complete pool before selecting. Do not place
any top-5 `**` markers during Phase 1. Marking as you write introduces sequential
bias -- finish the pool first.

Format each category as:
```
**[Category Name]**

**[Idea Name]**: [one-sentence pitch] -- [one-to-two sentence rationale specific to
{{topic}}; include one sentence naming how this idea changes the Phase 0 trajectory.]
```

Do Nothing goes in the **Status Quo** category with the entry from Phase 0.

### 1c. AMEND Draft

Write a draft AMEND section with 3 pool-shift directions. Each must: (a) name a shift
axis, (b) describe what ideas would appear or disappear, (c) pass the re-run test:
re-running with only this directive must produce candidate ideas not in the current
pool. Different ideas, not different framing of the same ideas.

Phase 1 is complete when: (a) the inertia paragraph is written, (b) the pool has
20-40 ideas in bold-header groups, and (c) 3 draft AMEND directions are written.

---

## PHASE 2 -- VERIFY

> **GATE: Phase 2 may begin only after Phase 1 is complete (20-40 ideas in pool,
> 3 draft AMEND directions written, no top-5 marks placed yet).**

**Check A -- Sequential Default**
Identify 5 top-5 candidates. Are they the first 5 ideas generated? If yes, rescan --
strongest ideas surface across the whole run. Output: 5 candidates for the Registry.

**Check B -- Peer-Comparison Registry**

For each of the 5 candidates, write one row. Do not fill in Selected? during
construction.

| # | Candidate (exact name from pool) | Peer (exact name, same **Category** group, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|------------------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Column rules:**
- **Candidate**: exact idea name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same bold **Category**
  group; cannot be blank
- **"I chose ... because ___"**: complete with a specific reason tied to {{topic}}'s
  actual constraints (scope, user group, cost, risk); "it is better" or "more viable"
  do not count
- **Selected?**: Phase-advance gate. This column cannot hold any value, and Phase 4
  cannot begin, until both preconditions hold simultaneously: (a) all 5 rows of this
  Registry are written in your output, AND (b) Selected? is blank across all 5 rows.
  A partial Registry has no valid Selected? entries. A Registry where any Selected?
  cell carries a preliminary value does not satisfy the gate. Phase 4 may begin only
  when the Registry is structurally complete (5 rows) and selection-clean (Selected?
  blank in every row). This is a schema property of the Registry.

**Prohibition Battery:**

**Prohibition A -- Marking Ban**: Do not place any top-5 `**` marks anywhere in your
output while Check B is in progress. No `**` marks may appear until the complete
5-row Registry is written in your output.

**Prohibition B -- Rationalization Block**: If you cannot complete the comparison
sentence for any row -- no specific peer holds or no specific reason applies -- that
candidate must be replaced by the peer named in the Peer column. The replacement
source is fixed: it is the peer from this row. Do not revise the candidate's rationale
to manufacture a distinction that was not present at comparison time. If editing the
candidate's rationale would make the comparison sentence completable, that desire
confirms the replacement obligation applies -- the impulse to revise so the comparison
can pass is not permission to reopen the comparison; it is the signal the swap is
mandatory.

**Check C -- AMEND Distribution-Shift Test**
For each of the 3 AMEND directions, verify: re-running with only this directive must
produce candidate ideas not in the current pool. A direction that shifts framing
without introducing different underlying candidates fails. Sharpen any that fail.

**Check D -- Inertia Placement**
Does the Phase 1a paragraph appear as the first element in the artifact (after the
Phase 0 baseline block)? If not, reorder.

Phase 2 is complete when: all 4 checks are finished, the 5-row Registry is written,
and Selected? is blank in every row.

---

## PHASE 4 -- FINALIZE

> **GATE: Phase 4 may begin only after both conditions hold simultaneously:**
> - **(a)** All 5 rows of the Peer-Comparison Registry are written in your output
> - **(b)** Selected? is blank across all 5 rows of the Registry
>
> A Registry with fewer than 5 rows does not satisfy (a). A Registry where any
> Selected? cell holds any value does not satisfy (b). Both conditions must hold
> simultaneously before any finalization step below may proceed.

Fill Selected? = YES in exactly 5 rows (candidates confirmed in Check B, with any
substitutions from Prohibition B applied). Mark those 5 ideas with `**` on their bold
idea names in the category groups. Use AMEND content finalized in Check C.

Write the artifact to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Phase 0 baseline block (Trajectory, Cost, Displacement Target),
inertia paragraph (1a), bold-header category groups (top-5 marked), Peer-Comparison
Registry, AMEND. Total ideas including Do Nothing: 20-40.
```

---

## C-33 / C-34 Compliance Summary

| Variation | Anchor (a) location | Anchor (a) verbatim? | Anchor (b) location | Anchor (b) verbatim? | C-33 | C-34 goal qualifier | C-34 |
|-----------|--------------------|-----------------------|--------------------|----------------------|------|---------------------|------|
| V-01 | Stage 2 Check B column rules (Selected?) | YES -- "all 5 rows...AND (b) Selected? is blank across all 5 rows" | Stage 3 GATE PRECONDITIONS block | YES -- same conditions | PASS | "so the comparison can pass" in Prohibition B | PASS |
| V-02 | Phase 2 Check B column rules (Selected?) | YES -- "all 5 rows...AND (b) Selected? is blank across all 5 rows" | Phase 3 GATE PRECONDITIONS block | YES -- same conditions | PASS | "so the comparison can pass" in Prohibition B | PASS |
| V-03 | Phase 2 Check B column rules (Selected?) | YES -- "all 5 rows...AND (b) Selected? is blank across all 5 rows" | Phase 4 GATE PRECONDITIONS block | YES -- same conditions | PASS | "so the comparison can pass" in Prohibition B | PASS |
| V-04 | Step 5 column rules (Selected?) | YES -- "all 5 rows of this Registry...AND (b) Selected? is blank across all 5 rows" | Step 6 GATE block | YES -- same conditions | PASS | "so the comparison can pass" in Rule 2 | PASS |
| V-05 | Phase 2 Check B column rules (Selected?) | YES -- "all 5 rows...AND (b) Selected? is blank across all 5 rows" | Phase 4 GATE PRECONDITIONS block | YES -- same conditions | PASS | "so the comparison can pass" in Prohibition B | PASS |

## Predicted R11 Scores

| Variation | Axes tested | Expected score | Key pass/fail |
|-----------|-------------|----------------|---------------|
| V-01 | Role sequence (AMEND-first) | 160 | C-33 PASS, C-34 PASS; all prior inh |
| V-02 | Output format (prose categories) | 157.5 | C-15 FAIL (-2.5); C-33 PASS, C-34 PASS |
| V-03 | Inertia framing (Phase 0 baseline) | 160 | C-33 PASS, C-34 PASS; all prior inh |
| V-04 | AMEND-first + conversational register | 160 | C-33 PASS, C-34 PASS survive register change |
| V-05 | Prose categories + explicit gates + inertia Phase 0 | 157.5 | C-15 FAIL (-2.5); C-33 PASS, C-34 PASS |

**V-02 and V-05 intentionally drop C-15 to test format independence of C-33/C-34.**
The format change (bold headers instead of ## sections) is the axis being tested, and
the expected C-15 failure confirms the variation is genuinely exercising a different
output structure. The key result is that C-33 and C-34 remain stable even when the
idea-pool format changes.
