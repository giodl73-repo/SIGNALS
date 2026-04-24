---
skill: quest-variate
skill_target: draft-brainstorm
round: 3
date: 2026-03-15
rubric_version: 3
r2_best: V-02 = 115, V-03 = 115, V-01 = 112.5 (V-04 unvalidated)
r3_target: 120 -- close all four R3 aspirational gaps (C-15..C-18)
---

# Variate R3 -- draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R3 focuses on closing the four R3 aspirational criteria introduced in rubric v3:
- **C-15** Structural Spine Guarantee -- dimensions mandated as output sections, not advisory scaffolding
- **C-16** Generation-Phase Sequential Guard -- anti-sequential prohibition placed in generation phase as imperative
- **C-17** Peer-Comparison Defensibility Test -- specific sentence-completion peer test embedded in top-5 selection
- **C-18** Self-Review Phase Integration -- dedicated review phase with explicit feedback connections to output decisions

R2 gap analysis (each base variation and what it already passes):
- V-02 (115): passes C-15 (7 mandatory sections), C-18 (artifact order + preliminary = feedback loop); fails C-16 (guard in selection step, not gen phase), C-17 (no peer sentence)
- V-03 (115): passes C-16 ("do not mark top-5 yet" in gen phase), C-18 (Phase 2/3 structure); fails C-15 (scaffolding, not mandate), C-17 (Check B interrogative, not imperative peer test)
- V-01 (112.5): passes C-17 ("Why these five and not the unmarked idea in same category?"); fails C-15 (no structural mandate), C-16 (single-phase), C-18 (no review phase)
- V-04 (unvalidated): expected to fail C-15 (scaffolding), C-16 (guard in B-2 not Phase A), C-17 (no peer sentence)

---

## Variation Axes Selected

| Axis | New in R3? | Used In | R3 Criterion |
|------|-----------|---------|--------------|
| Structural mandate vs advisory scaffolding | Yes | V-01 | C-15 |
| Embedded peer-comparison sentence test | Yes | V-02 | C-17 |
| Generation-phase placement of sequential guard | Yes | V-03 | C-16 |
| Full combination: all four R3 criteria (V-02 base evolved) | Combo | V-04 | C-15+C-16+C-17+C-18 |
| Full combination: all four R3 criteria (table format base) | Combo | V-05 | C-15+C-16+C-17+C-18 |

---

## V-01 -- Structural Spine Guarantee (C-15 focus)

**Axis**: Structural mandate -- dimensions as required output sections, not advisory scaffolding
**Base**: R2-V-03 (passes C-16 via "do not mark top-5 yet" in gen phase; passes C-18 via Phase 2/3 feedback loop)
**Hypothesis**: R2-V-03 names 6 dimension types as "category scaffolding" -- advisory hints the model
may collapse into fewer actual sections. Upgrading these to mandatory output sections (C-15) changes
the constraint from "try to cover these" to "your artifact must contain a labeled section for each."
By construction, the model cannot produce fewer than 6 dimensional groups. C-16 and C-18 are inherited
from R2-V-03. C-17 is not added (single-axis isolation) -- Check B remains interrogative to expose the
C-15 improvement in isolation.

**Expected**: C-15 pass + C-16 pass (inherited) + C-17 fail (intentional) + C-18 pass (inherited) = 117.5

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in two phases: GENERATE, then VERIFY. Do not finalize the artifact
until you have completed the verification step.

---

## PHASE 1 -- GENERATE

### 1a. Inertia Frame

Write a framing paragraph (3-5 sentences) for {{topic}}: What is the current
trajectory? What does the team inherit if no decision is made? What accumulates --
technically, organizationally, or for users?

This paragraph appears at the top of the final artifact and precedes all ideas.

### 1b. Idea Pool

Generate 20-40 candidates for {{topic}}. Your artifact must contain one labeled
section per required dimension below. These are **not suggestions or scaffolding** --
each dimension is a required `##` section in your output. Do not collapse them into
a flat list. Do not omit any listed dimension. You may add additional dimension
sections beyond the six listed.

**Required dimensions (each must appear as a `## [Dimension Name]` section):**

- **Scope** -- how much of {{topic}}'s problem space is addressed
- **Timing** -- when the intervention lands in the product lifecycle
- **Integration** -- how it connects to existing systems or teams
- **Audience** -- who benefits most
- **Build vs. Buy** -- internal build, external adoption, or extension of existing
- **Status Quo** -- the inertia option (exactly one idea: Do Nothing)

**Do not mark top-5 yet.** Complete the full pool across all sections before selecting.

For each idea:

```
## [Dimension Name]

### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this serves {{topic}} specifically -- cite a real constraint,
user need, or opportunity. No generic reasoning.
```

**Required**: Include **Do Nothing** in the Status Quo section. Its rationale
must continue the framing paragraph from 1a -- what the current trajectory
concretely produces for {{topic}}.

### 1c. AMEND Draft

Write a draft AMEND section with 3 pool-shift directions. Label each direction
and describe what changes. Do not finalize yet -- the verification step will check
these.

---

## PHASE 2 -- VERIFY

Before writing the final artifact, answer these 4 checks:

**Check A -- Sequential Default**
Look at the 5 ideas you are considering for top-5. Are they the first 5 ideas
you generated? If yes, rescan the full pool -- the best ideas are rarely the
first ones written. Select the 5 most immediately actionable, not the 5 most
recently visible.

**Check B -- Top-5 Defensibility**
For each of your 5 picks, can you complete this sentence: "I chose this over
[unmarked peer in same dimension] because ___"? If you cannot, the selection
is not defensible. Adjust if needed.

**Check C -- AMEND Re-Invocability**
For each of your 3 AMEND items: if a reader took only that directive and
re-ran this brainstorm, would they get a noticeably different pool? If the
answer is "probably the same pool with different labels," the directive is
not re-invocable. Sharpen until each amendment produces a clearly different
candidate distribution.

**Check D -- Inertia Paragraph**
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. The paragraph is not optional and must precede alternatives.

---

## PHASE 3 -- FINALIZE

Mark exactly 5 ideas with `**` on their heading (informed by Check A and B).
Update AMEND items if Check C required changes.

Write the final artifact to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Inertia paragraph, then dimension sections (with top-5 marked),
then AMEND. Total ideas (including Do Nothing): 20-40.

---

## V-02 -- Peer-Comparison Defensibility Test (C-17 focus)

**Axis**: Peer-comparison sentence test -- a specific named peer required in the defensibility check
**Base**: R2-V-02 (passes C-15 via 7 mandatory dimension sections; passes C-18 via artifact order feedback loop)
**Hypothesis**: R2-V-02's top-5 selection says "each marked idea should be more actionable today than
its unmarked peers" -- aspirational quality framing without an executable test. Adding a required
peer-comparison sentence ("Why [Idea Name] and not [name one specific unmarked idea in the same
Dimension]?") forces the model to surface a specific alternative and articulate a distinction rather
than assert confidence. C-15 and C-18 are inherited. C-16 is not added (guard remains in selection
step, not generation phase) -- isolating the C-17 improvement.

**Expected**: C-15 pass (inherited) + C-16 fail (intentional) + C-17 pass + C-18 pass (inherited) = 117.5

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

Your job: map the full option space across 6 required dimensions, then evaluate.

---

### Preliminary: Status Quo Trajectory

Before opening any dimension, write a paragraph that describes the current state
of {{topic}}: What is in motion today? What does the team inherit if no explicit
decision is made? What risks or missed opportunities compound over time by default?

This paragraph is the baseline against which every idea that follows is measured.

---

### Axis Map

You will generate ideas across the following 6 required dimensions. Each dimension
must produce at least 3 ideas (and may produce more). Label each section with the
dimension name as a header.

**Dimension 1 -- Scope**
Ideas in this axis vary *how much* of {{topic}}'s problem space is addressed --
from the minimal viable slice to the comprehensive overhaul.

**Dimension 2 -- Timing**
Ideas in this axis vary *when* intervention happens -- early bets, staged rollouts,
deferred commitments, and just-in-time decisions.

**Dimension 3 -- Integration**
Ideas in this axis vary *how* the solution connects to existing systems, platforms,
or external dependencies relevant to {{topic}}.

**Dimension 4 -- Audience**
Ideas in this axis vary *who* the primary beneficiary is -- different user segments,
internal teams, or downstream consumers of {{topic}}'s output.

**Dimension 5 -- Build vs. Buy**
Ideas in this axis vary *how* capability is acquired -- built internally, adopted
from outside, extended from existing components, or delegated.

**Dimension 6 -- Risk Profile**
Ideas in this axis vary *how much uncertainty* is accepted -- conservative,
incremental bets vs. high-variance, high-ceiling bets.

**Dimension 7 -- Status Quo (mandatory)**
This dimension contains exactly one idea: **Do Nothing**. Write the pitch and
rationale as a description of the current trajectory from the Preliminary section --
not as a placeholder. What does the team concretely get (and give up) by staying
the course on {{topic}}?

---

### Idea Format

For every idea in every dimension:

```
## [Dimension Name]

### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this option specifically serves {{topic}} -- name a real
constraint, user need, or opportunity. Must be topic-specific, not generic.
```

Total ideas across all 7 dimensions: 20-40. Trim or expand to stay in range.

---

### Top-5 Selection

After completing all 7 dimensions, review the full pool. Mark exactly 5 ideas
with `**` on their heading. These are your immediate-viability picks.

Rules for selection:
- Do not mark ideas in the order you generated them -- finish the full pool first
- Distribute marks across at least 2 different dimensions if the pool supports it
- For each marked idea, apply the peer test: "Why [Idea Name] and not [name one
  specific unmarked idea in the same Dimension]?" You must name a specific
  alternative and articulate the distinction. If you cannot complete this sentence
  for a candidate, that candidate does not belong in the top-5 -- either replace
  it or sharpen its rationale until the comparison holds.

---

### AMEND

Write an AMEND section with exactly 3 pool-shift adjustments. Each adjustment must:
(a) name a specific shift axis, (b) describe which ideas would enter, exit, or
re-rank, and (c) be re-invocable -- a reader must be able to re-run this brainstorm
using only that directive and produce a noticeably different pool. Vague directions
("think bigger") do not meet the re-invocability bar.

```
## AMEND

1. **[Direction]** -- [What changes in the pool. What enters, exits, re-ranks.
   Re-runnable: a reader with this directive produces a different pool.]
2. **[Direction]** -- [...]
3. **[Direction]** -- [...]
```

---

### Artifact

Save to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Preliminary paragraph -> 7 dimension sections -> AMEND.

---

## V-03 -- Generation-Phase Sequential Guard (C-16 focus)

**Axis**: Generation-phase placement -- sequential guard moved from selection step into generation instructions
**Base**: R2-V-02 (passes C-15 via 7 mandatory dimension sections; passes C-18 via artifact order feedback loop)
**Hypothesis**: Sequential bias fires at generation time, not selection time. R2-V-02 places the guard
in Top-5 Selection ("do not mark in order generated -- finish pool first") -- after the pool already
exists. This catches the bias retrospectively. Moving the prohibition INTO the Axis Map (generation
phase) as an imperative prevents the bias from forming rather than correcting it post-hoc. The
prohibition in the generation phase also signals to the model that marking and generating are
cognitively separate acts, not a single pass. C-15 and C-18 are inherited. C-17 is not added
(selection step retains quality framing without peer sentence) -- isolating the C-16 improvement.

**Expected**: C-15 pass (inherited) + C-16 pass + C-17 fail (intentional) + C-18 pass (inherited) = 117.5

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

Your job: map the full option space across 6 required dimensions, then evaluate.

---

### Preliminary: Status Quo Trajectory

Before opening any dimension, write a paragraph that describes the current state
of {{topic}}: What is in motion today? What does the team inherit if no explicit
decision is made? What risks or missed opportunities compound over time by default?

This paragraph is the baseline against which every idea that follows is measured.

---

### Axis Map

You will generate ideas across the following 6 required dimensions. Each dimension
must produce at least 3 ideas. Label each section with the dimension name as a header.

**Do not mark any idea with `**` in this section.** Top-5 marking happens after
the full pool is complete, in the Top-5 Selection section below. Marking during
generation introduces sequential bias -- the first ideas written are the most
available, not the best. Generate the entire pool before evaluating any of it.

**Dimension 1 -- Scope**
Ideas in this axis vary *how much* of {{topic}}'s problem space is addressed --
from the minimal viable slice to the comprehensive overhaul.

**Dimension 2 -- Timing**
Ideas in this axis vary *when* intervention happens -- early bets, staged rollouts,
deferred commitments, and just-in-time decisions.

**Dimension 3 -- Integration**
Ideas in this axis vary *how* the solution connects to existing systems, platforms,
or external dependencies relevant to {{topic}}.

**Dimension 4 -- Audience**
Ideas in this axis vary *who* the primary beneficiary is -- different user segments,
internal teams, or downstream consumers of {{topic}}'s output.

**Dimension 5 -- Build vs. Buy**
Ideas in this axis vary *how* capability is acquired -- built internally, adopted
from outside, extended from existing components, or delegated.

**Dimension 6 -- Risk Profile**
Ideas in this axis vary *how much uncertainty* is accepted -- conservative,
incremental bets vs. high-variance, high-ceiling bets.

**Dimension 7 -- Status Quo (mandatory)**
This dimension contains exactly one idea: **Do Nothing**. Its rationale must
describe the current trajectory from the Preliminary section -- what the team
concretely gets (and gives up) by staying the course on {{topic}}.

---

### Idea Format

For every idea in every dimension:

```
## [Dimension Name]

### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this option specifically serves {{topic}} -- name a real
constraint, user need, or opportunity. Topic-specific, not generic.
```

Total ideas across all 7 dimensions: 20-40.

---

### Top-5 Selection

Review the complete pool. Mark exactly 5 ideas with `**` on their heading.

Rules:
- Distribute marks across at least 2 different dimensions if the pool supports it
- Each marked idea should be more actionable today than its unmarked peers in the
  same dimension
- The selection is defensible if, for each marked idea, you can identify a weaker
  unmarked candidate in the same dimension that you chose not to mark

---

### AMEND

Write an AMEND section with exactly 3 pool-shift adjustments. Each adjustment must:
(a) name a specific shift axis, (b) describe which ideas would enter, exit, or
re-rank, and (c) be re-invocable -- a reader must be able to re-run this brainstorm
using only that directive and produce a noticeably different pool.

```
## AMEND

1. **[Direction]** -- [What changes. Re-runnable: produces different pool.]
2. **[Direction]** -- [...]
3. **[Direction]** -- [...]
```

---

### Artifact

Save to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Preliminary paragraph -> 7 dimension sections -> AMEND.

---

## V-04 -- Combination: All Four R3 Criteria (V-02 base evolved)

**Axes**: C-15 (structural mandate) + C-16 (generation-phase guard) + C-17 (peer-comparison sentence) + C-18 (explicit review phase with named feedback)
**Base**: R2-V-02 (passes C-15, C-18)
**Hypothesis**: R2-V-02 is the cleanest base for R3 because it already has mandatory dimensional
sections (C-15) and an artifact-order feedback loop (C-18). Two gaps remain: C-16 (guard in selection
step, not gen phase) and C-17 (no peer sentence). R3-V-04 closes both gaps and upgrades C-18 from an
implicit artifact-order feedback loop to an explicit named Self-Review Phase with connections to
specific output decisions. The result should pass all four R3 criteria within a familiar architecture
that makes each mechanism independently auditable.

**Expected**: C-15 pass + C-16 pass + C-17 pass + C-18 pass = 120

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

Your job: map the full option space across 6 required dimensions, then evaluate.

---

### Preliminary: Status Quo Trajectory

Before opening any dimension, write a paragraph that describes the current state
of {{topic}}: What is in motion today? What does the team inherit if no explicit
decision is made? What risks or missed opportunities compound over time by default?

This paragraph is the baseline against which every idea that follows is measured.
It must appear first in the final artifact, before any alternatives.

---

### Axis Map

You will generate ideas across the following 6 required dimensions. Each dimension
must produce at least 3 ideas. Label each section with the exact dimension name
as a `##` header.

**Do not mark any idea with `**` in this section.** Selection happens after the
full pool is complete. Marking ideas as you generate them introduces sequential
bias -- the first ideas written are the most available, not the best.

**Dimension 1 -- Scope**
Ideas in this axis vary *how much* of {{topic}}'s problem space is addressed --
from the minimal viable slice to the comprehensive overhaul.

**Dimension 2 -- Timing**
Ideas in this axis vary *when* intervention happens -- early bets, staged rollouts,
deferred commitments, and just-in-time decisions.

**Dimension 3 -- Integration**
Ideas in this axis vary *how* the solution connects to existing systems, platforms,
or external dependencies relevant to {{topic}}.

**Dimension 4 -- Audience**
Ideas in this axis vary *who* the primary beneficiary is -- different user segments,
internal teams, or downstream consumers of {{topic}}'s output.

**Dimension 5 -- Build vs. Buy**
Ideas in this axis vary *how* capability is acquired -- built internally, adopted
from outside, extended from existing components, or delegated.

**Dimension 6 -- Risk Profile**
Ideas in this axis vary *how much uncertainty* is accepted -- conservative,
incremental bets vs. high-variance, high-ceiling bets.

**Dimension 7 -- Status Quo (mandatory)**
This dimension contains exactly one idea: **Do Nothing**. Write the pitch and
rationale as a description of the current trajectory from the Preliminary section.
What does the team concretely get (and give up) by staying the course on {{topic}}?

---

### Idea Format

For every idea in every dimension:

```
## [Dimension Name]

### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this option specifically serves {{topic}} -- name a real
constraint, user need, or opportunity. Must be topic-specific, not generic.
```

Total ideas across all 7 dimensions: 20-40.

---

### Self-Review Phase

Run the following reviews before marking top-5 or finalizing AMEND. Each review
is connected to a specific output decision -- do not skip.

**Review A -- Sequential Default** (feeds top-5 marking)
Look at the 5 ideas you are considering for top-5. Are they the first 5 you
generated? If yes, rescan the full pool. The pool was built across 7 dimensions
for a reason -- the strongest ideas may be concentrated in later sections. This
review determines which candidates move forward.

**Review B -- Peer-Comparison Test** (feeds top-5 marking)
For each top-5 candidate, apply the peer test: "Why [Idea Name] and not [name
one specific unmarked idea in the same Dimension]?" You must name a specific peer
and articulate the distinction. If you cannot complete this sentence for a
candidate, that candidate does not belong in the top-5 -- replace it or sharpen
its rationale until the comparison holds. This review determines final top-5 marks.

**Review C -- AMEND Re-Invocability** (feeds AMEND finalization)
For each of your 3 AMEND items: would a reader who took only that directive and
re-ran this brainstorm produce a noticeably different pool? If not, sharpen the
directive. The bar is a different candidate distribution, not different labels on
the same pool. This review determines final AMEND content.

**Review D -- Artifact Order** (feeds final write)
Does the Preliminary paragraph appear before the first idea? Confirm. This
review gates the artifact write.

---

### Top-5 Selection (output of Review A and B)

Mark exactly 5 ideas with `**` on their heading. Distribute marks across at least
2 different dimensions if the pool supports it. The marks are the output of
Review A (not sequential) and Review B (peer-defensible) -- not a fresh pass.

---

### AMEND (output of Review C)

Write an AMEND section with exactly 3 pool-shift adjustments, updated based on
Review C if any items required sharpening. Each item must meet all three conditions:
(a) names a specific shift axis,
(b) describes which ideas enter, exit, or re-rank and why the pool looks different,
(c) is re-invocable -- a reader can re-run the brainstorm from this directive and
    obtain a noticeably different pool without needing further clarification.

```
## AMEND

1. **[Direction]** -- [Entries, exits, re-ranks. Why pool looks different. Re-invocable.]
2. **[Direction]** -- [...]
3. **[Direction]** -- [...]
```

---

### Artifact

Save to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Preliminary paragraph -> 7 dimension sections (top-5 marked) -> AMEND.
Total ideas (including Do Nothing): 20-40.

---

## V-05 -- Combination: All Four R3 Criteria (Table Format Base)

**Axes**: C-15 + C-16 + C-17 + C-18 applied to table format base
**Base**: R2-V-05 (table format + scoring self-check; targets all C-11..C-14)
**Hypothesis**: R2-V-05 demonstrated that table format can carry all four C-11..C-14 criteria.
R3-V-05 extends this to C-15..C-18 by: (a) mandating dimension names as required structural sections
in the Category View, making dimensional coverage a property of output shape rather than model
compliance (C-15); (b) moving the anti-sequential instruction from Step 2 into Step 1 during table
construction (C-16); (c) upgrading the Self-Check to require a named peer-comparison sentence before
filling the Top-5? column (C-17); and (d) labeling Step 2 as an explicit Self-Review Phase with
named connections to the top-5 marking step and AMEND finalization (C-18). The table format
maintains its C-02 anatomy auditability advantage throughout.

**Expected**: C-15 pass + C-16 pass + C-17 pass + C-18 pass = 120

---

You are running the `draft-brainstorm` skill for the topic: {{topic}}

---

### Preamble: Inertia Frame

Before generating any ideas, write a paragraph (3-5 sentences) describing the
current trajectory for {{topic}}: What happens if the team makes no deliberate
decision? What is already in motion? What does the path of least resistance produce?

This paragraph must appear before the idea table in the final artifact.

---

### Step 1 -- Build the Table

Generate a markdown table with exactly these columns:

| # | Name | Pitch | Dimension | Rationale | Top-5? |
|---|------|-------|-----------|-----------|--------|

Column rules:
- **#**: Sequential number
- **Name**: 2-5 words
- **Pitch**: One sentence -- what the idea is
- **Dimension**: One of the required dimension types below. You must produce at
  least 3 rows per required Dimension (Status Quo: exactly 1 row):
  - `Scope` -- how much of {{topic}}'s problem is addressed
  - `Timing` -- when the intervention occurs in the lifecycle
  - `Integration` -- how it connects to existing systems or external dependencies
  - `Audience` -- who the primary beneficiary is
  - `Build vs. Buy` -- internal vs. external acquisition
  - `Risk Profile` -- conservative to aggressive bets
  - `Status Quo` -- the inertia option (exactly 1 row, named **Do Nothing**)
- **Rationale**: Why this serves {{topic}} -- cite a specific constraint, user
  need, or opportunity. "This provides value" is not a rationale.
- **Top-5?**: Leave this column **blank during Step 1.** Do not fill in Top-5?
  values as you build the table. You will fill this column only after completing
  the Self-Review Phase (Step 2). Marking during construction introduces sequential
  bias -- the ideas in the first rows are not the best ideas; they are the first
  ones written.

Required row: **Do Nothing** with Dimension = `Status Quo`. Its Rationale must
describe what the current trajectory from the Preamble produces -- not "doing
nothing is an option."

Volume: 20-40 rows total.

---

### Step 2 -- Self-Review Phase

Before filling in the Top-5? column or writing AMEND, run the following reviews.
Each review is explicitly connected to a downstream output decision.

**Review A -- Sequential Default** (determines top-5 marking in Step 3)
Look at rows 1-5. Are you planning to mark these because they are the strongest
rows, or because they are the first? If the five strongest ideas are scattered
throughout the table, the selection is honest. If they are rows 1-5, rescan the
full table. The output of this review determines which rows receive marks.

**Review B -- Peer-Comparison Test** (determines top-5 marking in Step 3)
For each candidate row you plan to mark, apply the peer test: "Why [Idea Name]
and not [name one specific unmarked row in the same Dimension]?" You must name
a specific alternative row and articulate the distinction. If you cannot complete
this sentence, that row is not yet defensible -- either choose a different row
or revise its rationale until the comparison holds. The output of this review
determines final top-5 marks.

**Review C -- AMEND Re-Invocability** (determines AMEND content in Step 5)
For each AMEND directive you plan to write: if a reader took only that directive
and re-ran the brainstorm, would they produce a table with different rows?
If not, sharpen the directive. The bar is a different candidate distribution,
not different labels on the same rows. The output of this review determines
final AMEND content.

**Review D -- Dimension Coverage** (determines Category View completeness in Step 4)
Do your Dimension values cover all 7 required dimension types? If any required
type is missing, add rows before proceeding. The output of this review determines
whether the Category View is complete.

---

### Step 3 -- Mark Top-5 (output of Review A and B)

Fill in `**YES**` in exactly 5 rows' Top-5? column. These are the ideas with
highest immediate viability given typical resource and risk constraints. The marks
reflect the findings of Review A (not sequential) and Review B (peer-defensible).

---

### Step 4 -- Category View (required output structure)

After the table, produce a Category View grouping ideas under their Dimension
names. Each Dimension that appeared in the table must have its own
`## [Dimension Name]` section. This is a **required structural output** -- the
Category View is not optional and must contain a section for every Dimension
present in the table. The model cannot satisfy this step with a flat list.

```
## [Dimension Name]

- **[Idea Name]** -- [Pitch]  [**TOP-5**] (if marked)
```

---

### Step 5 -- AMEND (output of Review C)

Write an AMEND section with exactly 3 adjustments, incorporating any sharpening
from Review C. Each must meet all three bars:
(a) names a specific shift axis,
(b) describes which rows enter, exit, or re-rank and why the pool looks different,
(c) is re-invocable -- a reader can re-run the brainstorm from this directive and
    produce a noticeably different table without additional clarification.

```
## AMEND

1. **[Direction label]** -- [Rows that enter, exit, or re-rank. Why table looks
   different. Re-runnable with this directive alone.]
2. **[Direction label]** -- [...]
3. **[Direction label]** -- [...]
```

---

### Step 6 -- Write Artifact

Save to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Preamble paragraph, table, Category View, AMEND.

---

## Rubric Coverage Analysis -- R3

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 volume (20-40) | Stated | Stated | Stated | Stated | Stated (20-40 rows) |
| C-02 idea anatomy (4 fields) | Per-idea block | Per-idea block | Per-idea block | Per-idea block | Table columns |
| C-03 top-5 marker (**) | `**` heading prefix | `**` heading prefix | `**` heading prefix | `**` heading prefix | Table column YES |
| C-04 inertia check | Status Quo required section + rationale rules | Status Quo dim 7 mandatory + trajectory description | Status Quo dim 7 mandatory + trajectory description | Status Quo dim 7 + trajectory | Status Quo row + Preamble |
| C-05 AMEND (3 items) | 1c draft + Phase 2 Check C | AMEND section, 3 items | AMEND section, 3 items | AMEND section, Review C informed | Step 5, Review C informed |
| C-06 category grouping | Required ## sections per dimension | Dimension headers | Dimension headers | Dimension headers | Category View (Step 4) |
| C-07 rationale specificity | "cite real constraint" | "topic-specific, not generic" | "topic-specific, not generic" | "topic-specific, not generic" | "cite specific constraint" |
| C-08 category diversity (4+) | 6 required dimensions | 7 dimensions (6+SQ) | 7 dimensions (6+SQ) | 7 dimensions (6+SQ) | 7 required dimension types |
| C-09 AMEND actionability | Check C tests re-inv. | Re-invocability bar stated | Re-invocability bar stated | Sub-conditions (a)(b)(c) + Review C | Sub-conditions (a)(b)(c) + Review C |
| C-10 top-5 defensibility | Check A+B (C-17 gap isolates C-15) | Finish pool + peer comparison | Finish pool; actionable>peers | Review A+B explicit | Review A+B explicit |
| C-11 sequential-default guard | "Do not mark top-5 yet" in Phase 1b (gen phase) | "Do not mark in order generated" in selection | "Do not mark any idea in this section" in Axis Map | "Do not mark in this section" in Axis Map | "Leave blank during Step 1" in table building |
| C-12 re-runnability bar | Check C tests re-inv. | Re-invocability bar stated | Re-invocability bar stated | Sub-condition (c) + Review C | "Re-runnable with this directive alone" |
| C-13 category dimension taxonomy | 6 named dimensions | 7 named dimensions with descriptions | 7 named dimensions with descriptions | 7 named dimensions with descriptions | 7 named dimension types |
| C-14 inertia-first framing paragraph | Phase 1a paragraph precedes all ideas | Preliminary paragraph precedes dimensions | Preliminary paragraph precedes dimensions | Preliminary "appears first in artifact" | Preamble "before table" |
| **C-15 structural spine guarantee** | **PASS**: 6 named dims each = required `##` section; "Do not collapse into flat list; do not omit" | Fail (inherits R2-V-02 gap: dim types listed with descriptions but not mandated as structural sections) | Fail (inherits R2-V-02 gap) | **PASS**: 7 named dims each = required `##` section by Axis Map; categorical requirement explicit | **PASS**: Category View "required structural output" mandates section per Dimension; "model cannot satisfy with flat list" |
| **C-16 generation-phase sequential guard** | **PASS** (inherits R2-V-03: "Do not mark top-5 yet" in Phase 1b gen phase, imperative) | Fail (guard in Top-5 Selection step, not gen phase -- isolates C-17) | **PASS**: "Do not mark any idea with ** in this section" in Axis Map = generation phase imperative | **PASS**: "Do not mark any idea with ** in this section" in Axis Map = generation phase imperative | **PASS**: "Leave blank during Step 1. Do not fill in Top-5? values as you build the table" = generation-phase imperative |
| **C-17 peer-comparison defensibility test** | Fail (Check B remains "can you complete" interrogative -- intentional C-15 isolation) | **PASS**: "Why [Idea Name] and not [name one specific unmarked idea in the same Dimension]?" in top-5 rules | Fail (selection step retains "more actionable than peers" quality framing -- intentional C-16 isolation) | **PASS**: Review B requires naming specific peer + distinction; "candidate does not belong" if cannot complete | **PASS**: Review B requires naming specific peer + distinction before any Top-5? mark |
| **C-18 self-review phase integration** | **PASS** (inherits R2-V-03: Phase 2 checks explicitly feed Phase 3 marks and AMEND update) | **PASS** (inherits R2-V-02: Preliminary + artifact order = feedback loop) | **PASS** (inherits R2-V-02: Preliminary + artifact order = feedback loop) | **PASS**: Self-Review Phase names Review A->top-5, Review B->top-5, Review C->AMEND, Review D->artifact order | **PASS**: Self-Review Phase names Review A->Step 3, Review B->Step 3, Review C->Step 5, Review D->Step 4 |

**Projected scores:**

| Variation | C-01..C-14 | C-15 | C-16 | C-17 | C-18 | Projected |
|-----------|-----------|------|------|------|------|-----------|
| R3-V-01 | 110 | pass | pass (inh) | fail | pass (inh) | 117.5 |
| R3-V-02 | 110 | pass (inh) | fail | pass | pass (inh) | 117.5 |
| R3-V-03 | 110 | pass (inh) | pass | fail | pass (inh) | 117.5 |
| R3-V-04 | 110 | pass (inh) | pass | pass | pass (upgraded) | 120 |
| R3-V-05 | 110 | pass | pass | pass | pass | 120 |

**Observations:**

- V-01 isolates C-15 by holding all other axes constant (R2-V-03 base with structural mandate added).
  The Check B interrogative form is intentional -- if V-01 scores 117.5 as projected, the delta
  confirms C-15 is worth 2.5 points independently.

- V-02 isolates C-17 by holding all other axes constant (R2-V-02 base with peer sentence added).
  The generation-phase guard stays in the selection step -- if V-02 scores 117.5, the delta from
  R2-V-02's 115 confirms C-17 is worth 2.5 points independently.

- V-03 isolates C-16 by holding all other axes constant (R2-V-02 base with guard moved to gen phase).
  No peer sentence added -- if V-03 scores 117.5, confirms C-16 is worth 2.5 points independently.

- V-04 is the direct synthesis path: R2-V-02 + C-16 guard moved to Axis Map + C-17 peer sentence added
  + C-18 upgraded from implicit artifact-order to explicit named review phase. Cleanest upgrade path
  to 120 for operators who want to evolve an existing V-02 prompt.

- V-05 is the table-format path to 120. The Category View as mandatory structural output (C-15)
  is a natural fit for the table format -- the table already tracks Dimension as a column, so
  requiring a section per Dimension in the Category View is architecturally consistent.
  Best choice when downstream scoring pipelines benefit from machine-parseable tabular output.

**Key R3 insight**: All three single-axis variations (V-01, V-02, V-03) project to 117.5 because
each inherits two R3 passes from their base. The combination variations (V-04, V-05) close the
remaining gaps. The differentiation question between V-04 and V-05 is format preference and
downstream use case, not rubric score -- both target 120.

---

## Change Log

| Version | Round | Change |
|---------|-------|--------|
| R1 | 1 | Initial 5 variations -- output format, inertia framing, phrasing register, role sequence, lifecycle emphasis |
| R2 | 2 | 5 variations targeting C-11..C-14; all R2 variations projected at 110 |
| R3 | 3 | 5 variations targeting C-15..C-18; V-01/02/03 project at 117.5 (single-axis), V-04/05 project at 120 (combinations) |
