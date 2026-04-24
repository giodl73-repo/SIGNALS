---
skill: quest-variate
skill_target: draft-brainstorm
round: 12
date: 2026-03-16
rubric_version: 12
r11_scores_under_v12: "V-03 R11 = 165 (C-35 PASS -- Phase 0 hard boundary; C-36 PASS -- '19-39 additional...total 20-40'), V-05 R11 = 160 (C-15 FAIL cancels C-35+C-36 gain), V-01 R11 = 160 (C-35 FAIL -- inertia in Stage 1a not Phase 0; C-36 FAIL -- total only), V-04 R11 = 160 (same as V-01), V-02 R11 = 155 (C-15 FAIL + C-35 FAIL + C-36 FAIL)"
r12_target: "165 -- confirm C-35 (Phase-0 hard boundary before Phase 1) and C-36 (net-new count alongside total: '19-39 additional...total 20-40') are structurally stable across: (a) AMEND-first with lenses as Pre-Phase and inertia as Phase 0, (b) prose-category format with bold-header groups instead of ## sections (C-15 FAIL intentional), (c) maximal lifecycle emphasis with explicit close/open gate announcements at every phase boundary, (d) AMEND-first + conversational register combined, (e) prose-categories + lifecycle emphasis combined (C-15 FAIL intentional)"
---

# Variate R12 -- draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01, V-02, V-03), then combinations (V-04, V-05).

R12 targets two new criteria extracted from the V-03 R11 excellence signal:

- **C-35** Phase-0 Inertia Prefacing -- the inertia baseline (Do Nothing + Pitch +
  Rationale + framing paragraph) occupies a phase labeled "Phase 0" (or equivalent
  pre-generation phase label) that is architecturally closed before Phase 1 opens.
  A framing paragraph that precedes the idea pool _within_ Phase 1a satisfies C-14
  but fails C-35 -- the hard phase boundary must be present, not just paragraph
  ordering within a shared phase.

- **C-36** Net-Count Volume Specification -- the volume instruction states both the
  net-new count ("19-39 additional") AND the total count ("20-40 total") in a coupled
  statement, making explicit that Do Nothing is counted in the total and preventing
  the model from generating 20+ net-new ideas plus Do Nothing and overshooting the
  range. A total count alone ("Generate 20-40") fails C-36.

---

## Variation Axes

| Axis | Description |
|------|-------------|
| Role sequence | Whether AMEND (lenses) precedes or follows inertia baseline; whether it is a pre-numbered Pre-Phase or an embedded step |
| Output format | Mandatory `##` dimension sections vs bold-header prose category groups (C-15 tradeoff) |
| Lifecycle emphasis | How explicitly phase boundaries are announced -- minimal (one heading) vs maximal (close + open gate text at every transition) |
| Phrasing register | Formal third-person imperative vs conversational second-person throughout |
| Inertia framing | Phase 0 as minimal baseline entry vs Phase 0 as full competitive analysis block |

## Single-axis variations

---

### V-01 -- Role Sequence: AMEND-First with Pre-Phase Lenses + Phase 0 Inertia

**Axis**: Role sequence
**Hypothesis**: In R11, AMEND-first (V-01) placed lenses in Stage 0 and embedded inertia
in Stage 1a -- passing C-14 but failing C-35 because no hard phase boundary separated the
inertia block from generation. This variation retains AMEND-first sequencing but extracts
lenses into an unnumbered Pre-Phase, freeing Phase 0 to serve exclusively as the inertia
baseline. Tests whether C-35 and C-36 survive when: (a) a Pre-Phase label precedes Phase 0
rather than starting at Phase 0, and (b) the pool generation phase (Phase 1) explicitly
references both the Pre-Phase lenses and the Phase 0 baseline as production inputs. The
AMEND-first discipline (lenses as constraints, not post-hoc filters) must survive the
Pre-Phase → Phase 0 → Phase 1 sequencing.

**Expected**: C-01..C-34 PASS (inh from V-03 R11 backbone) + C-35 PASS (Phase 0 closes
explicitly before Phase 1 opens, hard boundary present) + C-36 PASS ("19-39 additional
candidates...total 20-40 including Do Nothing") = **165**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in five phases: Pre-Phase (lenses), Phase 0 (inertia baseline),
Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalize). Complete each in order.
Do not advance to the next phase until the current phase is complete.

---

## Pre-Phase -- Generative Lenses

Before writing a single idea or establishing the inertia baseline, define 3 directions
that will actively pull the pool away from its center of gravity. These are production
constraints -- they determine which ideas appear in Phase 1, not which ideas survive
a post-hoc filter.

For each lens:
- **Lens name**: one phrase (e.g., "More Ambitious", "Audience Shift", "Incremental")
- **Direction**: one sentence describing the shift axis
- **Pool impact**: what kinds of ideas appear under this lens that would not appear in a
  default brainstorm? Name candidate types, not framing differences.
- **Re-run test**: if a reader took only this lens and re-ran the brainstorm, would the
  resulting pool contain ideas not in the current pool? Different candidates, not the same
  candidates under different labels. If not, sharpen the lens before proceeding.

Write all 3 lenses. Do not begin Phase 0 until all 3 lenses pass the re-run test.

---

## Phase 0 -- Inertia Baseline

Before generating any candidate ideas, fully specify the Do Nothing option for {{topic}}.
This is the most important entry in the pool: it is already in play, and every other
candidate exists to displace it.

Write the following four fields:

**Current Trajectory**: What is happening to {{topic}} right now with no deliberate
intervention? Name the specific direction the system, team, or product is already moving.
(2-3 sentences.)

**Accumulated Cost**: What concretely accumulates -- technically, organizationally, or for
users -- if this trajectory continues for 12 months? Be specific: what is delayed,
degraded, or foreclosed? (2-3 sentences.)

**Displacement Target**: What must a competing idea change about the trajectory to beat
this baseline? State the minimum threshold: "A candidate beats Do Nothing if and only if
it [specific condition]." (1 sentence.)

**Do Nothing** (pool entry):
```
**Pitch**: [One sentence summarizing the status quo trajectory from the analysis above]
**Rationale**: [The Accumulated Cost, compressed to one sentence]
```

Phase 0 is now complete. The Do Nothing entry from Phase 0 will occupy the Status Quo
section of Phase 1. All other candidates will be evaluated against the Displacement Target.
Phase 1 opens below.

---

## Phase 1 -- Idea Pool

### 1a. Inertia Frame

Write a paragraph (3-5 sentences) expanding on the Phase 0 baseline for a general reader:
What is the current trajectory for {{topic}}? What does the team inherit if no deliberate
decision is made? What does the path of least resistance produce -- technically,
organizationally, or for users?

This paragraph must appear as the first element in the final artifact, before any ideas.

### 1b. Idea Pool

Using the 3 Pre-Phase lenses as active generation constraints, produce **19-39 additional
candidates** for {{topic}} -- for a total of 20-40 ideas including the Phase 0 Do Nothing
entry. Your output must contain one labeled section per required dimension. Each is a
**mandatory `##` section** -- do not collapse into a flat list, do not omit any. You may
add sections beyond the six required.

**Required dimensions (each must appear as a `##` section):**
- **Scope** -- how much of {{topic}}'s problem space is addressed
- **Timing** -- when the intervention lands in the product lifecycle
- **Integration** -- how it connects to existing systems or teams
- **Audience** -- who benefits most
- **Build vs. Buy** -- internal build, external adoption, or extension of existing
- **Status Quo** -- contains exactly the Do Nothing entry from Phase 0

**Lens attribution**: Tag at least 2 ideas per lens inline (e.g., `[Lens: Audience Shift]`).
Aim for at least 6 lens-attributed ideas total. Center-of-gravity ideas are permitted but
must not dominate the pool.

**Do not mark top-5 yet.** Generate the complete pool before selecting. Do not place any
`**` markers on any idea during Phase 1. Marking as you write introduces sequential bias --
finish the pool first.

For each idea (other than Do Nothing):
```
### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this serves {{topic}} specifically -- cite a real constraint, user need,
or opportunity. Include one sentence naming how this idea changes the Phase 0 trajectory:
what specifically does it displace or prevent?
```

### 1c. AMEND Draft

Write a draft AMEND section with 3 pool-shift directions. For each:
- Name the shift axis
- Describe what kinds of ideas would appear or disappear
- Apply the distribution-shift test: re-running with only this directive must produce
  candidate ideas not in the current pool. Different candidates, not the same candidates
  under different framing. A direction that shifts only emphasis or category labels without
  introducing different underlying candidates fails this test.

Do not finalize AMEND yet -- it will be verified in Phase 2 Check C.

---

## Phase 2 -- Peer-Comparison

**Check A -- Sequential Default**
Identify 5 top-5 candidates. Are they the first 5 ideas generated? If yes, rescan the
full pool -- the strongest ideas surface across the whole run, not only at the start.
Output of Check A: 5 candidates advancing to the Registry.

**Check B -- Peer-Comparison Registry**

For each of the 5 candidates, write one row. Do not fill in Selected? during construction.

| # | Candidate (exact name from pool) | Peer (exact name, same ## section, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|----------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

Write all five "I chose ... because ___" sentences before evaluating any of them.
Do not evaluate whether a candidate passes while other rows are still blank.

**Column rules:**
- **Candidate**: exact idea name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same `##` section; cannot
  be blank
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

**Prohibition A -- Marking Ban**: Do not place any `**` marks anywhere in your output
while Phase 2 Check B is in progress -- not on headings, inline, in notes, or in any
other form. No `**` marks may appear until the complete 5-row Registry is written.

**Prohibition B -- Rationalization Block**: If you cannot complete the comparison
sentence for any row -- no specific peer holds or no specific reason applies -- that
candidate must be replaced by the peer named in the Peer column. The replacement source
is fixed: it is the peer from this row, not an alternative selected after reconsidering.
Do not revise the candidate's rationale to manufacture a distinction that was not present
at comparison time. If editing the candidate's rationale would make the comparison sentence
completable, that desire confirms the replacement obligation applies -- the impulse to
revise so the comparison can pass is not permission to reopen the comparison; it is the
signal the swap is mandatory.

**Check C -- AMEND Distribution-Shift Test**
For each of the 3 AMEND directions from 1c, verify: re-running with only this directive
must surface candidate ideas not in the current pool. Sharpen any that would produce the
same candidates under different framing. Output of Check C: final AMEND content.

**Check D -- Inertia Placement**
Does the Phase 1a paragraph appear as the first element in the artifact? If not, reorder.

---

## Phase 3 -- Finalize

> **GATE PRECONDITIONS -- both must hold before Phase 3 may begin:**
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
Displacement Target), dimension sections (top-5 marked, lens tags removed), Peer-
Comparison Registry, AMEND (3 directions, distribution-shift-verified). Total ideas
including Do Nothing: 20-40.
```

---

### V-02 -- Output Format: Prose Category Groups (No ## Dimension Sections)

**Axis**: Output format
**Hypothesis**: R11 V-02 (prose categories) failed both C-15 and C-35 -- it had no
structural spine guarantee (intentional) and embedded inertia in Phase 1a (C-35 failure).
This variation retains the prose-category format (bold-header groups, no `##` sections)
but adds the Phase 0 hard boundary (C-35) and net-count volume specification (C-36).
Tests whether the Phase 0 architectural signal is readable when the output format uses
bold-header groups: the `##` phase headings for Phase 0/Phase 1 are distinct from the
idea-grouping headers, so Phase 0 can close as a `##`-headed phase even when idea groups
use bold text. C-15 is intentionally sacrificed (no mandatory `##` dimension sections).
Expected to isolate the formatting tradeoff: C-15 costs 2.5 pts, C-35+C-36 recover 5 pts.

**Expected**: C-01..C-14 PASS (inh), C-15 FAIL (bold-header groups, no mandatory ##
sections -- intentional), C-16..C-34 PASS (inh) + C-35 PASS (## Phase 0 heading closes
before ## Phase 1 opens; idea grouping uses bold not ##) + C-36 PASS ("19-39 additional...
total 20-40") = **162.5**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in four phases: Phase 0 (inertia baseline), Phase 1 (pool), Phase 2
(peer-comparison), Phase 3 (finalize). Complete each phase in order.

---

## Phase 0 -- Inertia Baseline

Before generating any candidate ideas, fully specify the Do Nothing option for {{topic}}.
This is the most important entry in the pool: it is already in play, and every other
candidate exists to displace it.

Write the following four fields:

**Current Trajectory**: What is happening to {{topic}} right now with no deliberate
intervention? Name the specific direction the system, team, or product is already moving.
(2-3 sentences.)

**Accumulated Cost**: What concretely accumulates -- technically, organizationally, or for
users -- if this trajectory continues for 12 months? Be specific: what is delayed,
degraded, or foreclosed? (2-3 sentences.)

**Displacement Target**: What must a competing idea change about the trajectory to beat
this baseline? State the minimum threshold: "A candidate beats Do Nothing if and only if
it [specific condition]." (1 sentence.)

**Do Nothing** (pool entry):
```
**Pitch**: [One sentence summarizing the status quo trajectory from the analysis above]
**Rationale**: [The Accumulated Cost, compressed to one sentence]
```

Phase 0 is complete. Phase 1 opens below.

---

## Phase 1 -- Idea Pool

### 1a. Inertia Frame

Write a paragraph (3-5 sentences) expanding on the Phase 0 baseline for a general reader:
What is the current trajectory for {{topic}}? What does the team inherit if no deliberate
decision is made? What does the path of least resistance produce?

This paragraph must appear as the first element in the final artifact, before any ideas.

### 1b. Idea Pool

Generate **19-39 additional candidates** for {{topic}} -- for a total pool of 20-40
including the Phase 0 Do Nothing entry. Present ideas as flowing prose-grouped entries
under bold category headers. Use 4-7 distinct categories that represent genuinely
different dimensions (e.g., scope, timing, integration approach, audience, build vs. buy,
risk tolerance) -- do not use `##` headings for categories; bold labels only.

**Do not mark top-5 yet.** Generate the complete pool before selecting. Do not place any
`**` markers on any idea during Phase 1. Marking as you write introduces sequential bias --
finish the pool first.

Format each group as:

```
**[Category Name]**

**[Idea Name]**: [one-sentence pitch] -- [rationale: one to two sentences citing a real
constraint, user need, or opportunity specific to {{topic}}. No generic reasoning. Include
one sentence on how this idea displaces or changes the Phase 0 trajectory.]
```

The Do Nothing entry from Phase 0 goes in a **Status Quo** category. Its rationale must
extend the Phase 0 analysis -- what the current trajectory concretely produces for {{topic}}.

### 1c. AMEND Draft

Write a draft AMEND section with 3 pool-shift directions. For each:
- Name the shift axis
- Describe what ideas would appear or disappear
- Apply the distribution-shift test: re-running with only this directive must surface
  candidate ideas not in the current pool. Different candidates, not the same candidates
  under different framing. A directive that shifts only labels or emphasis without changing
  underlying candidate types fails this test.

Do not finalize yet.

---

## Phase 2 -- Peer-Comparison

**Check A -- Sequential Default**
Identify 5 top-5 candidates. Are they the first 5 ideas generated? If yes, rescan the
full pool. The strongest ideas surface across the whole run, not only at the start.
Output: 5 candidates advancing to the Registry.

**Check B -- Peer-Comparison Registry**

For each of the 5 candidates, write one row. Do not fill in Selected? during construction.

| # | Candidate (exact name from pool) | Peer (exact name, same **Category** group, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|------------------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

Write all five "I chose ... because ___" sentences before evaluating any of them.

**Column rules:**
- **Candidate**: exact idea name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same bold **Category** group;
  cannot be blank
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

**Prohibition A -- Marking Ban**: Do not place any `**` marks designating top-5 selection
anywhere in your output while Check B is in progress -- not on idea names, inline, in
notes, or in any other form. No top-5 `**` marks may appear until the complete 5-row
Registry is written.

**Prohibition B -- Rationalization Block**: If you cannot complete the comparison sentence
for any row -- no specific peer holds or no specific reason applies -- that candidate must
be replaced by the peer named in the Peer column. The replacement source is fixed: it is
the peer from this row, not an alternative selected after reconsidering. Do not revise the
candidate's rationale to manufacture a distinction that was not present at comparison time.
If editing the candidate's rationale would make the comparison sentence completable, that
desire confirms the replacement obligation applies -- the impulse to revise so the
comparison can pass is not permission to reopen the comparison; it is the signal the swap
is mandatory.

**Check C -- AMEND Distribution-Shift Test**
For each of the 3 AMEND directions from 1c, verify the distribution-shift test: re-running
with only this directive must surface candidate ideas not in the current pool. Sharpen any
that fail. Output of Check C: final AMEND content.

**Check D -- Inertia Placement**
Does the framing paragraph from 1a appear as the first element in the artifact?
If not, reorder.

---

## Phase 3 -- Finalize

> **GATE PRECONDITIONS -- both must hold before Phase 3 may begin:**
> - **(a)** All 5 rows of the Peer-Comparison Registry are written in your output
> - **(b)** Selected? is blank across all 5 rows of the Registry
>
> A Registry with fewer than 5 rows does not satisfy (a). A Registry where any
> Selected? cell holds any value does not satisfy (b). Both conditions must hold
> simultaneously before any finalization step below may proceed.

Fill Selected? = YES in exactly 5 rows (candidates confirmed by Check B, with any
substitutions from Prohibition B applied). Mark those 5 idea names with `**` in the
prose-grouped list. Use the AMEND content finalized in Check C.

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
Displacement Target), prose category groups (top-5 marked), Peer-Comparison Registry,
AMEND. Total ideas including Do Nothing: 20-40.
```

---

### V-03 -- Lifecycle Emphasis: Maximal Gate Verbosity at Every Phase Boundary

**Axis**: Lifecycle emphasis
**Hypothesis**: V-03 R11 used a single `##` heading to demarcate each phase -- Phase 0
opened with a heading and Phase 1 opened with its heading, with no explicit closure
announcement. This variation adds an explicit close statement at the bottom of every phase
("Phase N is complete. Phase N+1 begins below.") and an explicit precondition reminder at
the top of every phase ("This phase requires Phase N-1 to be complete."). The hypothesis is
that maximal gate verbosity makes the Phase 0 → Phase 1 hard boundary (C-35) structurally
inescapable: the model sees a close statement for Phase 0 before any Phase 1 instruction
appears. Tests whether redundant gate announcements are neutral (no quality change) or
positive (stronger constraint enforcement). May also produce measurable improvements in
C-14 and C-35 compliance variance across model runs.

**Expected**: C-01..C-34 PASS (inh) + C-35 PASS (explicit close statement at bottom of
Phase 0 + explicit open at top of Phase 1; hard boundary doubly-marked) + C-36 PASS
("19-39 additional candidates...total 20-40 including Do Nothing") = **165**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in four phases: Phase 0 (inertia baseline), Phase 1 (pool), Phase 2
(peer-comparison), Phase 3 (finalize). Each phase has explicit open and close signals.
Do not begin a phase until the previous phase is complete and its close signal is written.

---

## Phase 0 -- Inertia Baseline

*Phase 0 requires: no preconditions. This is the first phase.*

Before generating any candidate ideas, fully specify the Do Nothing option for {{topic}}.
This is the most important entry in the pool: it is already in play, and every other
candidate exists to displace it.

Write the following four fields:

**Current Trajectory**: What is happening to {{topic}} right now with no deliberate
intervention? Name the specific direction the system, team, or product is already moving.
(2-3 sentences.)

**Accumulated Cost**: What concretely accumulates -- technically, organizationally, or for
users -- if this trajectory continues for 12 months? Be specific: what is delayed,
degraded, or foreclosed? (2-3 sentences.)

**Displacement Target**: What must a competing idea change about the trajectory to beat
this baseline? State the minimum threshold: "A candidate beats Do Nothing if and only if
it [specific condition]." (1 sentence.)

**Do Nothing** (pool entry):
```
**Pitch**: [One sentence summarizing the status quo trajectory from the analysis above]
**Rationale**: [The Accumulated Cost, compressed to one sentence]
```

> **Phase 0 is now complete.** All four fields are written. The Do Nothing entry is
> established. Phase 1 may begin.

---

## Phase 1 -- Idea Pool

*Phase 1 requires: Phase 0 complete (all four fields + Do Nothing entry written).*

### 1a. Inertia Frame

Write a paragraph (3-5 sentences) expanding on the Phase 0 baseline for a general reader:
What is the current trajectory for {{topic}}? What does the team inherit if no deliberate
decision is made? What does the path of least resistance produce -- technically,
organizationally, or for users?

This paragraph must appear as the first element in the final artifact, before any ideas.

### 1b. Idea Pool

Generate **19-39 additional candidates** for {{topic}} -- for a total pool of 20-40
including the Phase 0 Do Nothing entry. Your output must contain one labeled section per
required dimension. Each is a **mandatory `##` section** -- do not collapse into a flat
list, do not omit any. You may add sections beyond the six required.

**Required dimensions (each must appear as a `##` section):**
- **Scope** -- how much of {{topic}}'s problem space is addressed
- **Timing** -- when the intervention lands in the product lifecycle
- **Integration** -- how it connects to existing systems or teams
- **Audience** -- who benefits most
- **Build vs. Buy** -- internal build, external adoption, or extension of existing
- **Status Quo** -- contains exactly the Do Nothing entry from Phase 0

**Do not mark top-5 yet.** Generate the complete pool before selecting. Do not place any
`**` markers on any idea during Phase 1. Marking as you write introduces sequential bias --
finish the pool first.

For each idea (other than Do Nothing):
```
### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this serves {{topic}} specifically -- cite a real constraint, user need,
or opportunity. No generic reasoning. Include one sentence naming how this idea changes
the Phase 0 trajectory: what specifically does it displace or prevent?
```

### 1c. AMEND Draft

Write a draft AMEND section with 3 pool-shift directions. For each:
- Name the shift axis
- Describe what kinds of ideas would appear or disappear
- Apply the distribution-shift test: re-running with only this directive must surface
  candidate ideas not in the current pool. Different candidates, not the same candidates
  under different framing. If a directive would produce the same candidates under different
  labels, it fails the test -- sharpen it.

Do not finalize yet.

> **Phase 1 is now complete.** The full pool (19-39 net-new ideas + Do Nothing = 20-40
> total) is written. The AMEND draft is written. Phase 2 may begin.

---

## Phase 2 -- Peer-Comparison

*Phase 2 requires: Phase 1 complete (full pool written, AMEND draft written, no top-5
marks in output).*

**Check A -- Sequential Default**
Identify 5 top-5 candidates. Are they the first 5 ideas generated? If yes, rescan the
full pool -- the strongest ideas surface across the whole run, not only at the start.
Output of Check A: 5 candidates advancing to the Registry.

**Check B -- Peer-Comparison Registry**

For each of the 5 candidates, write one row. Do not fill in Selected? during construction.

| # | Candidate (exact name from pool) | Peer (exact name, same ## section, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|----------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

Write all five "I chose ... because ___" sentences before evaluating any. Do not assess
whether a row passes while other rows remain blank.

**Column rules:**
- **Candidate**: exact idea name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same `##` section; cannot
  be blank
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

**Prohibition A -- Marking Ban**: Do not place any `**` marks anywhere in your output
while Phase 2 Check B is in progress -- not on headings, inline, in notes, or in any
other form. No `**` marks may appear until the complete 5-row Registry is written.

**Prohibition B -- Rationalization Block**: If you cannot complete the comparison sentence
for any row -- no specific peer holds or no specific reason applies -- that candidate must
be replaced by the peer named in the Peer column. The replacement source is fixed: it is
the peer from this row, not an alternative selected after reconsidering. Do not revise the
candidate's rationale to manufacture a distinction that was not present at comparison time.
If editing the candidate's rationale would make the comparison sentence completable, that
desire confirms the replacement obligation applies -- the impulse to revise so the
comparison can pass is not permission to reopen the comparison; it is the signal the swap
is mandatory.

**Check C -- AMEND Distribution-Shift Test**
For each of the 3 AMEND directions from 1c, verify: re-running with only this directive
must surface candidate ideas not in the current pool. Sharpen any that would produce the
same candidates under different framing.

**Check D -- Inertia Placement**
Does the Phase 1a paragraph appear as the first element in the artifact? If not, reorder.

> **Phase 2 is now complete** when: all 5 Registry rows are written, Selected? is blank
> in every row, Checks A/C/D are done, and no `**` marks are present in the output. Phase
> 3 may begin only when all four conditions are met.

---

## Phase 3 -- Finalize

*Phase 3 requires: Phase 2 complete (5-row Registry written, Selected? blank in all rows).*

> **GATE PRECONDITIONS -- both must hold before Phase 3 may begin:**
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

### V-04 -- AMEND-First + Conversational Register + Phase-0 + Net-Count

**Axes**: Role sequence (AMEND as Pre-Phase before inertia) + Phrasing register
(conversational second-person throughout)
**Hypothesis**: In R11, conversational V-04 passed C-33 (verbatim schema element names
survived register change) and C-34 ("so the comparison can pass" survived informality)
but failed C-35 (inertia in Step 1 not Phase 0) and C-36 (total count only). This
variation carries the conversational register forward while adding Phase 0 hard boundary
and net-count specification. The key tension: conversational phrasing tends toward
contractions and approximations ("around 20-40") that could dilute the precision of
"19-39 additional... total 20-40" required by C-36. Tests whether the net-count phrase
survives register informality, and whether "Phase 0 is done" closure language reads
naturally in a conversational register without sounding awkward. C-33 must survive:
conversational phrasing of the Selected? column rule must still name schema elements
verbatim ("Schema property of the Registry") while feeling natural.

**Expected**: C-01..C-34 PASS (inh) + C-35 PASS (Phase 0 closes with explicit "Phase 0
is done" signal; Phase 1 opens with "here's your pool phase") + C-36 PASS ("19-39
additional... total 20-40" precision survives conversational register) = **165**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

Here's how this works: you'll name your lenses first, then anchor the inertia baseline,
then build the pool against both, then stress-test your top picks, then write the
artifact. Five phases -- don't skip ahead.

---

### Pre-Phase -- Name Your Lenses

Before anything else, define 3 directions that will intentionally pull the pool somewhere
it wouldn't naturally go. Use these as active constraints while you generate ideas in
Phase 1 -- not as a filter you apply after the pool is already written.

For each lens, answer three things:
- **What's the shift?** One phrase: "More Aggressive Scope", "Different Primary User", etc.
- **What changes?** One sentence: what kinds of ideas appear under this lens that wouldn't
  show up in a default brainstorm? Name candidate types, not framing differences.
- **Does it pass the re-run test?** If a reader took only this lens and re-ran the
  brainstorm, would they get ideas that aren't in your current pool? Different candidates,
  not the same candidates in different wording. If not, sharpen the lens.

Write all 3 lenses. Don't move to Phase 0 until they're done.

---

### Phase 0 -- Anchor the Inertia Baseline

Before you write a single alternative idea, nail down what doing nothing actually looks
like for {{topic}}. This is the most important entry in the pool -- it's already in play,
and everything else in Phase 1 exists to beat it.

Write these four things:

**Current Trajectory**: What is {{topic}} doing right now with no deliberate intervention?
Name the specific direction things are already moving. (2-3 sentences.)

**Accumulated Cost**: What piles up -- technically, organizationally, or for users -- if
this trajectory runs for 12 more months? Be concrete: what gets delayed, degraded, or
foreclosed? (2-3 sentences.)

**Displacement Target**: One sentence naming the minimum bar: "A candidate beats Do
Nothing if and only if it [specific condition]."

**Do Nothing** (your pool entry):
```
**Pitch**: [One sentence summarizing the trajectory above]
**Rationale**: [The Accumulated Cost, one sentence]
```

Phase 0 is done. The Do Nothing entry goes in the Status Quo section of Phase 1. Every
other idea you generate will be held against the Displacement Target. Phase 1 opens now.

---

### Phase 1 -- Build the Pool

#### 1a. Inertia Frame

Write a paragraph (3-5 sentences) translating the Phase 0 baseline into plain language:
What's the current trajectory for {{topic}}? What does the team inherit if no decision
is made? What does the path of least resistance actually produce -- for users, the team,
or the product?

This paragraph goes first in the artifact, before any ideas.

#### 1b. Idea Pool

Generate **19-39 additional ideas** for {{topic}} -- for a total of 20-40 including Do
Nothing from Phase 0. You need these sections in your output -- each as a `##` heading,
not collapsed into a flat list:

- `## Scope` -- how much of {{topic}}'s problem space this addresses
- `## Timing` -- when the intervention lands in the product lifecycle
- `## Integration` -- how it connects to existing systems or teams
- `## Audience` -- who benefits most
- `## Build vs. Buy` -- internal build, external adoption, or extension of existing
- `## Status Quo` -- exactly the Do Nothing entry from Phase 0

Use your Pre-Phase lenses while you generate. Tag at least 2 ideas per lens inline
(e.g., `[Lens: More Aggressive Scope]`). Center-of-gravity ideas are fine -- just
don't let them crowd out the lens-influenced ones.

**Don't mark top-5 yet.** Finish the whole pool before picking. Don't put `**` on
anything during Phase 1 -- you'll introduce sequential bias if you mark as you go.

Each idea (other than Do Nothing):
```
### [Idea Name]
**Pitch**: One sentence.
**Rationale**: Why this specifically for {{topic}}. Real constraint, user need, or
opportunity -- no generic reasoning. One sentence on how it changes the Phase 0
trajectory: what does it displace or prevent?
```

#### 1c. Draft AMEND

Write a draft AMEND section: 3 directions for a future run of this brainstorm. For each,
name the shift and say what kinds of ideas would appear or disappear -- not different
framing, different candidates. Apply the re-run test: a reader who took only this
direction and re-ran should get ideas that aren't in your current pool. You'll sharpen
these in Phase 2 after a distribution check.

Don't finalize yet.

---

### Phase 2 -- Verify

#### Check A -- Sequential Default

Pick your 5 top-5 candidates. Are they the first 5 you wrote? If yes, that's sequential
default -- scan the full pool again. The strongest candidates surface across the whole
run, not just at the start.

Output: 5 candidates going to the Registry.

#### Check B -- Peer-Comparison Registry

For each of the 5 candidates, write one row. Leave Selected? blank while you're building.

| # | Candidate (exact name from pool) | Peer (exact name, same ## section, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|----------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

Write all five "I chose ... because ___" sentences before you evaluate any of them.

**Column rules:**
- **Candidate**: exact idea name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same `##` section; can't be blank
- **"I chose ... because ___"**: complete the sentence with a real reason tied to
  {{topic}}'s constraints -- scope, user group, cost, risk; "it is better" doesn't count
- **Selected?**: Phase-advance gate. This column can't hold any value, and Phase 3 can't
  begin, until both hold simultaneously: (a) all 5 rows of this Registry are written in
  your output, AND (b) Selected? is blank across all 5 rows. An incomplete Registry has
  no valid Selected? entries. A Registry where any Selected? cell carries a value -- even
  a preliminary one -- doesn't satisfy the gate. Phase 3 opens only when the Registry has
  all 5 rows written AND every Selected? cell is blank. This is a schema property of the
  Registry.

**Two rules that apply without exception while Check B is in progress:**

**Rule 1 -- No marking**: Don't put any `**` marks anywhere while you're working on the
Registry -- not on headings, not inline, not as notes. No `**` marks appear until the
complete 5-row Registry is in your output.

**Rule 2 -- No rationalization**: If you can't complete the comparison sentence for a
row -- no peer works, or no real reason applies -- replace that candidate with the peer
you named in the Peer column. The swap source is fixed: it's the peer from that row,
not a different idea you pick after going back to reconsider. Don't rewrite the
candidate's rationale to manufacture a distinction that wasn't there at comparison time.
If editing the rationale would make the comparison sentence completable, that desire
confirms the replacement applies -- the impulse to revise so the comparison can pass is
not permission to reopen the comparison; it is the signal the swap is mandatory.

#### Check C -- AMEND Distribution-Shift Test

For each AMEND direction from 1c, verify: re-running with only this direction must surface
ideas not in the current pool. Sharpen any that would produce the same candidates under
different framing. Output: final AMEND content.

#### Check D -- Inertia Placement

Does the 1a paragraph appear first in the artifact? If not, reorder.

---

### Phase 3 -- Finalize

> **GATE: Phase 3 begins only after both conditions hold simultaneously:**
> - **(a)** All 5 rows of the Peer-Comparison Registry are written in your output
> - **(b)** Selected? is blank across all 5 rows of that Registry
>
> A Registry with fewer than 5 rows doesn't satisfy (a). Any value in any Selected?
> cell doesn't satisfy (b). Verify both before proceeding.

Fill Selected? = YES in exactly 5 rows (confirmed candidates from Check B, with any
swaps from Rule 2 applied). Mark those 5 idea names with `**` on their `##` headings.
Use the AMEND content finalized in Check C.

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
Displacement Target), dimension sections (top-5 marked, lens tags removed), Peer-
Comparison Registry, AMEND. Total ideas including Do Nothing: 20-40.
```

---

### V-05 -- Prose-Categories + Maximal Lifecycle Emphasis + Phase-0 + Net-Count

**Axes**: Output format (bold-header prose groups, no `##` dimension sections) + lifecycle
emphasis (explicit close/open announcements at every boundary)
**Hypothesis**: R11 V-05 (prose categories + lifecycle) passed C-35 and C-36 but failed
C-15 and, under v12, the net score was 160 (C-15 FAIL offset by C-35+C-36 PASS). This
variation confirms that the same tradeoff holds when lifecycle gate verbosity is maximized:
explicit close/open announcements at Phase 0→1 and Phase 1→2 transitions reinforce the
C-35 boundary signal even without `##` section headers on ideas. C-15 is intentionally
sacrificed. Tests whether maximal gate verbosity can substitute for `##` structural spine
as a boundary-enforcement mechanism, and whether the Phase 0 closure announcement in
prose format is unambiguous when idea-grouping also uses bold text (distinguishing phase
headers from category headers becomes critical).

**Expected**: C-01..C-14 PASS (inh), C-15 FAIL (bold-header groups, no mandatory ##
idea-category sections -- intentional), C-16..C-34 PASS (inh) + C-35 PASS (explicit
"Phase 0 complete" close text before Phase 1 open; ## used only for phase headings, not
idea categories, so boundary is unambiguous) + C-36 PASS ("19-39 additional...total 20-40")
= **162.5**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in four phases: Phase 0 (inertia baseline), Phase 1 (pool), Phase 2
(peer-comparison), Phase 3 (finalize). Each phase has a written close signal. Do not
begin a phase until the previous phase's close signal is in your output.

---

## Phase 0 -- Inertia Baseline

*Phase 0 opens now. No preconditions.*

Before generating any candidate ideas, fully specify the Do Nothing option for {{topic}}.
This is the most important entry in the pool: it is already in play, and every other
candidate exists to displace it.

Write the following four fields:

**Current Trajectory**: What is happening to {{topic}} right now with no deliberate
intervention? Name the specific direction things are already moving. (2-3 sentences.)

**Accumulated Cost**: What concretely accumulates -- technically, organizationally, or for
users -- if this trajectory continues for 12 months? Be specific: what is delayed,
degraded, or foreclosed? (2-3 sentences.)

**Displacement Target**: What must a competing idea change about the trajectory to beat
this baseline? State the threshold: "A candidate beats Do Nothing if and only if it
[specific condition]." (1 sentence.)

**Do Nothing** (pool entry):
```
**Pitch**: [One sentence summarizing the trajectory above]
**Rationale**: [The Accumulated Cost, one sentence]
```

> **Phase 0 complete.** All four fields written. Do Nothing established. Phase 1 opens
> below.

---

## Phase 1 -- Idea Pool

*Phase 1 requires: Phase 0 complete ("Phase 0 complete." signal written above).*

### 1a. Inertia Frame

Write a paragraph (3-5 sentences) expanding the Phase 0 baseline for a general reader:
What is the current trajectory for {{topic}}? What does the team inherit if no deliberate
decision is made? What does the path of least resistance produce?

This paragraph must appear as the first element in the final artifact.

### 1b. Idea Pool

Generate **19-39 additional candidates** for {{topic}} -- for a total pool of 20-40
including the Phase 0 Do Nothing entry. Present ideas as flowing prose-grouped entries
under bold category headers (not `##` headings). Use 4-7 distinct categories that
represent genuinely different dimensions of the problem space -- choose from: scope of
coverage, timing of delivery, integration approach, target audience, build/buy/extend
decision, risk tolerance, organizational change required, or other genuine axes that
apply to {{topic}}.

**Do not mark top-5 yet.** Generate the complete pool before selecting. Do not place any
`**` markers on any idea during Phase 1. Marking as you write introduces sequential
bias -- finish the pool first.

Format each group as:

```
**[Category Name]**

**[Idea Name]**: [one-sentence pitch] -- [rationale: one to two sentences citing a real
constraint, user need, or opportunity specific to {{topic}}. No generic reasoning. Include
one sentence on how this idea changes the Phase 0 trajectory: what does it displace or
prevent?]
```

The Do Nothing entry from Phase 0 goes in a **Status Quo** category. Its rationale must
extend the Phase 0 analysis -- what the current trajectory concretely produces for
{{topic}}.

### 1c. AMEND Draft

Write a draft AMEND section with 3 pool-shift directions. For each:
- Name the shift axis
- Describe what kinds of ideas would appear or disappear
- Apply the distribution-shift test: re-running with only this directive must surface
  candidate ideas not in the current pool. Different candidates, not the same candidates
  under different framing. If the directive only relabels or re-emphasizes the same
  underlying candidates, sharpen it.

Do not finalize yet.

> **Phase 1 complete.** Pool of 19-39 net-new ideas + Do Nothing (total 20-40) written.
> AMEND draft written. No `**` marks in output. Phase 2 opens below.

---

## Phase 2 -- Peer-Comparison

*Phase 2 requires: Phase 1 complete ("Phase 1 complete." signal written above).*

**Check A -- Sequential Default**
Identify 5 top-5 candidates. Are they the first 5 ideas generated? If yes, rescan the
full pool. The strongest candidates surface across the whole run.
Output: 5 candidates advancing to the Registry.

**Check B -- Peer-Comparison Registry**

For each of the 5 candidates, write one row. Do not fill in Selected? during construction.

| # | Candidate (exact name from pool) | Peer (exact name, same **Category** group, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|------------------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

Write all five "I chose ... because ___" sentences before evaluating any of them.

**Column rules:**
- **Candidate**: exact idea name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same bold **Category** group;
  cannot be blank
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

**Prohibition A -- Marking Ban**: Do not place any `**` marks designating top-5 selection
anywhere in your output while Check B is in progress. No top-5 `**` marks appear until
the complete 5-row Registry is written.

**Prohibition B -- Rationalization Block**: If you cannot complete the comparison sentence
for any row -- no specific peer holds or no specific reason applies -- that candidate must
be replaced by the peer named in the Peer column. The replacement source is fixed: it is
the peer from this row, not an alternative selected after reconsidering. Do not revise the
candidate's rationale to manufacture a distinction that was not present at comparison time.
If editing the candidate's rationale would make the comparison sentence completable, that
desire confirms the replacement obligation applies -- the impulse to revise so the
comparison can pass is not permission to reopen the comparison; it is the signal the swap
is mandatory.

**Check C -- AMEND Distribution-Shift Test**
For each of the 3 AMEND directions from 1c, verify: re-running with only this directive
must surface candidate ideas not in the current pool. Sharpen any that would produce the
same candidates under different framing. Output: final AMEND content.

**Check D -- Inertia Placement**
Does the 1a paragraph appear as the first element in the artifact? If not, reorder.

> **Phase 2 complete** when: all 5 Registry rows are written, Selected? blank in every
> row, Checks A/C/D done, no `**` marks in output. Verify all four before Phase 3.

---

## Phase 3 -- Finalize

*Phase 3 requires: Phase 2 complete ("Phase 2 complete." signal written above, 5-row
Registry written, Selected? blank in all rows).*

> **GATE PRECONDITIONS -- both must hold before Phase 3 may begin:**
> - **(a)** All 5 rows of the Peer-Comparison Registry are written in your output
> - **(b)** Selected? is blank across all 5 rows of the Registry
>
> A Registry with fewer than 5 rows does not satisfy (a). A Registry where any
> Selected? cell holds any value does not satisfy (b). Both conditions must hold
> simultaneously before any finalization step below may proceed.

Fill Selected? = YES in exactly 5 rows (candidates confirmed by Check B, with any
substitutions from Prohibition B applied). Mark those 5 idea names with `**` in the
prose-grouped list. Use the AMEND content finalized in Check C.

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
Displacement Target), prose category groups (top-5 marked), Peer-Comparison Registry,
AMEND. Total ideas including Do Nothing: 20-40.
```

---

## R12 Projected Scores Under v12

| Variation | C-15 | C-35 | C-36 | v12 Score | Delta vs R11 |
|-----------|------|------|------|-----------|--------------|
| V-01 | PASS (## sections) | PASS (Pre-Phase → Phase 0 hard boundary) | PASS ("19-39 additional...total 20-40") | **165** | +5 vs R11 V-01 |
| V-02 | FAIL (bold headers, intentional) | PASS (## phase headings close Phase 0 before Phase 1) | PASS ("19-39 additional...total 20-40") | **162.5** | +7.5 vs R11 V-02 |
| V-03 | PASS (## sections) | PASS (explicit "Phase 0 complete" close + "Phase 1 opens" open) | PASS ("19-39 additional...total 20-40") | **165** | +5 vs R11 ceiling |
| V-04 | PASS (## sections) | PASS ("Phase 0 is done...Phase 1 opens now") | PASS (net-count precision survives register) | **165** | +5 vs R11 V-04 |
| V-05 | FAIL (bold headers, intentional) | PASS ("Phase 0 complete" signal before Phase 1) | PASS ("19-39 additional...total 20-40") | **162.5** | +7.5 vs R11 V-05 |

**Key R12 finding to confirm**: V-01 R12 is the critical test -- AMEND-first sequencing
failed C-35 in R11 because lenses occupied Stage 0 and inertia was embedded in Stage 1a.
Moving lenses to an unnumbered Pre-Phase should recover C-35. If V-01 scores 165, the
Pre-Phase label is a valid C-35 solution. If V-01 scores 160 (C-35 FAIL), the scoring
reveals that C-35 requires the inertia block to be numbered Phase 0 specifically, not just
any pre-generation phase.

**C-36 survival test**: The net-count phrase "19-39 additional candidates...total 20-40
including Do Nothing" must survive conversational register (V-04) and prose-category format
(V-02, V-05) without being softened to "about 20-40" or "between 19 and 39." The rubric
requires both counts to be present and the Do Nothing relationship to be derivable from
the stated numbers. Approximation language fails C-36.
