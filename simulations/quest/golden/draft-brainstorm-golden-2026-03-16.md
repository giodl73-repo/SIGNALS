---
skill: quest-golden
skill_target: draft-brainstorm
date: 2026-03-16
rounds: 20
rubric_final: draft-brainstorm-rubric-v19-2026-03-16.md
score: 200
simplification: QU5-PASS (20.1% reduction, 1844 → 1474 words)
status: GOLDEN
---

# Golden Prompt — draft-brainstorm

Source: R20 V-05 → QU5 simplified (simplification PASS)
Rubric: v19 (50 criteria, max 205 pts)
Score: 200 / 205 (v19 projected)

---

## Prompt Body

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in five phases: Pre-Phase (lenses), Phase 0 (inertia baseline),
Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalize). Complete each in order.

> **Brainstorm session opens.** Topic: {{topic}}. Phases: Pre-Phase -> Phase 0 -> Phase 1 -> Phase 2 -> Phase 3. No preconditions.

---

## Pre-Phase -- Generative Lenses

*Pre-Phase opens now. No preconditions.*

Before writing a single idea or establishing the inertia baseline, define 3 directions
that will actively pull the pool away from its center of gravity. These are production
constraints -- they determine which ideas appear in Phase 1, not which ideas survive
a post-hoc filter.

For each lens:
- **Lens name**: one phrase
- **Direction**: one sentence describing the shift axis
- **Pool impact**: what kinds of ideas appear under this lens that would not appear in a
  default brainstorm? Name candidate types, not framing differences.
- **Re-run test**: if a reader took only this lens and re-ran the brainstorm, would the
  resulting pool contain ideas not in the current pool? Different candidates, not the same
  candidates under different labels. If not, sharpen the lens before proceeding.

Write all 3 lenses. Do not begin Phase 0 until all 3 lenses pass the re-run test.

> **Pre-Phase complete.** Lenses defined and re-run verified:
> 1. [Lens 1 name] -- [one-word direction]
> 2. [Lens 2 name] -- [one-word direction]
> 3. [Lens 3 name] -- [one-word direction]
> All 3 pass the re-run test. Phase 0 opens now.

---

## Phase 0 -- Inertia Baseline

> **Phase 0 opens now.** No preconditions. Active lenses:
> 1. [Lens 1 name] -- [one-word direction]
> 2. [Lens 2 name] -- [one-word direction]
> 3. [Lens 3 name] -- [one-word direction]

Before generating any candidate ideas, fully specify the Do Nothing option for {{topic}}.

**Current Trajectory**: What is happening to {{topic}} right now with no deliberate
intervention? (2-3 sentences.)

**Accumulated Cost**: What concretely accumulates -- technically, organizationally, or for
users -- if this trajectory continues for 12 months? (2-3 sentences.)

**Displacement Target**: What must a competing idea change about the trajectory to beat
this baseline? State the minimum threshold: "A candidate beats Do Nothing if and only if
it [specific condition]." (1 sentence.)

**Do Nothing**:
```
**Pitch**: [One sentence summarizing the status quo trajectory from the analysis above]
**Rationale**: [The Accumulated Cost, compressed to one sentence]
```

> **Phase 0 complete.** All four fields written. Do Nothing established.

---

## Phase 1 -- Idea Pool

*Phase 1 requires: Phase 0 complete (all four fields + Do Nothing entry written).*

> **Phase 1 opens now.** Phase 0 complete. Do Nothing established. Active lenses:
> 1. [Lens 1 name] -- [one-word direction]
> 2. [Lens 2 name] -- [one-word direction]
> 3. [Lens 3 name] -- [one-word direction]

### 1a. Inertia Frame

Write a paragraph (3-5 sentences) expanding on the Phase 0 baseline for a general reader:
What is the current trajectory for {{topic}}? What does the team inherit if no deliberate
decision is made? What does the path of least resistance produce?

This paragraph must appear as the first element in the final artifact.

### 1b. Idea Pool

Using the 3 Pre-Phase lenses as active generation constraints, produce **19-39 additional
candidates** for {{topic}} -- for a total of 20-40 ideas including the Phase 0 Do Nothing
entry. Your output must contain one labeled section per required dimension. Each is a
**mandatory `##` section** -- do not collapse into a flat list, do not omit any.

**Required dimensions:**
- **Scope** -- how much of {{topic}}'s problem space is addressed
- **Timing** -- when the intervention lands in the product lifecycle
- **Integration** -- how it connects to existing systems or teams
- **Audience** -- who benefits most
- **Build vs. Buy** -- internal build, external adoption, or extension of existing
- **Status Quo** -- contains exactly the Do Nothing entry from Phase 0

**Lens attribution**: Tag at least 2 ideas per lens inline (e.g., `[Lens: Audience Shift]`).
Center-of-gravity ideas are permitted but must not dominate the pool.

**Do not mark top-5 yet.** Do not place any `**` markers on any idea during Phase 1.

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
  under different framing.

Do not finalize AMEND yet -- it will be verified in Phase 2 Check C.

> **Phase 1 complete.** The full pool (19-39 net-new ideas + Do Nothing = 20-40 total) is
> written. AMEND draft written. No `**` marks in output. Phase 2 may begin.

---

## Phase 2 -- Peer-Comparison

*Phase 2 requires: Phase 1 complete ("Phase 1 complete." signal written above).*

> **Phase 2 opens now.** Phase 1 complete. Full pool written, AMEND drafted.

**Check A -- Sequential Default**
Are the top-5 candidates the first 5 ideas generated? If yes, rescan the full pool.

**Check B -- Peer-Comparison Registry**

Write one row per candidate.

| # | Candidate (exact name from pool) | Peer (exact name, same ## section, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|----------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

Write all five "I chose ... because ___" sentences before evaluating any of them.

- **Candidate**: exact idea name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same `##` section; cannot
  be blank
- **"I chose ... because ___"**: complete the sentence with a specific reason tied to
  {{topic}}'s actual constraints; "it is better" or "more viable" do not count
- **Selected?**: Phase-advance gate. This column cannot hold any value, and Phase 3
  cannot begin, until both preconditions hold simultaneously: (a) all 5 rows of this
  Registry are written in your output, AND (b) Selected? is blank across all 5 rows.
  Phase 3 may begin only when the Registry is structurally complete (5 rows) and
  selection-clean (Selected? blank in every row).

**Prohibition A -- Marking Ban**: Do not place any `**` marks anywhere in your output
during Check B. No `**` marks may appear until the complete 5-row Registry is written.

**Prohibition B -- Rationalization Block**: If you cannot complete the comparison sentence
for any row -- no specific peer holds or no specific reason applies -- that candidate must
be replaced by the peer named in the Peer column. The replacement source is fixed: it is
the peer from this row, not an alternative selected after reconsidering. Do not revise the
candidate's rationale to manufacture a distinction that was not present at comparison time.

**Check C -- AMEND Distribution-Shift Test**
For each of the 3 AMEND directions from 1c, verify: re-running with only this directive
must surface candidate ideas not in the current pool. Sharpen any that would produce the
same candidates under different framing.

**Check D -- Inertia Placement**
Does the Phase 1a paragraph appear as the first element in the artifact? If not, reorder.

> **Phase 2 complete** when: all 5 Registry rows written, Selected? blank in every row,
> Checks A/C/D done, no `**` marks in output.

---

## Phase 3 -- Finalize

*Phase 3 requires: Phase 2 complete (5-row Registry written, Selected? blank in all rows).*

> **GATE PRECONDITIONS:**
> - **(a)** All 5 rows of the Peer-Comparison Registry are written in your output
> - **(b)** Selected? is blank across all 5 rows of the Registry

> **Phase 3 opens now.** Phase 2 complete. Peer-comparison validated. AMEND finalized.

Fill Selected? = YES in exactly 5 rows. Mark those 5 ideas with `**` on their headings
in the dimension sections. Use the AMEND content finalized in Check C.

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

> **Phase 3 complete.** Artifact written to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`. All phases closed.

> **Session complete.** Phases closed: Pre-Phase (lenses), Phase 0 (inertia baseline), Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalized). Artifact written and closed.
```

---

## What Made It Golden

The V-05 → QU5 prompt closes three gaps that the baseline V-03 leaves open. Each
gap was discovered empirically across R01–R20 and codified as a rubric criterion.

### 1. Lens carry chain spans all three nodes (C-47 + C-48 + C-49 + C-50)

V-03 carries lens names only at Pre-Phase close and Phase 1 open — two nodes, one gap.
V-05 closes the gap: lens names with direction axes appear at every phase boundary where
the model transitions into generative work:

```
Pre-Phase close  →  Phase 0 open  →  Phase 1 open
  [name+dir]           [name+dir]      [name+dir]
     C-47                C-50            C-48+C-49
```

The model sees its active lenses at exactly the moment it writes the inertia baseline
(Phase 0) and at the moment it begins generating the pool (Phase 1). Neither is a post-hoc
reminder.

### 2. Numbered-list notation over parenthetical (structural, not cosmetic)

V-03 uses `(1) [Lens 1 name], (2) [Lens 2 name], (3) [Lens 3 name]` — a flat
parenthetical string. V-05 uses:

```
> 1. [Lens 1 name] -- [one-word direction]
> 2. [Lens 2 name] -- [one-word direction]
> 3. [Lens 3 name] -- [one-word direction]
```

Each lens occupies its own line with a fixed `[name] -- [direction]` slot. The form
is consistent across all three tags (Pre-Phase close, Phase 0 open, Phase 1 open),
making the carry chain visually scannable and structurally parallel. A model completing
the template cannot drop the direction axis without breaking the list structure.

### 3. Direction axis at Phase 0 entry (C-50) closes the inertia-lens visibility gap

The Do Nothing entry is the only idea that predates the lens-generated pool. In V-03,
Phase 0 opens with no lens signal — the inertia baseline is written without a visible
reminder of the directions the pool will later pull toward. V-05 carries all three
lens names and directions into the Phase 0 opening tag, so the displacement target
("a candidate beats Do Nothing if and only if it...") is written with the pull directions
already visible. This tightens the connection between inertia baseline and the lens-
driven pool that follows.

### 4. Direction axis at Phase 1 entry (C-49) constrains generation from the first idea

V-03's Phase 1 open carries lens names only: `Active lenses: (1) [name], (2) [name],
(3) [name]`. V-05 adds the direction axis: `1. [name] -- [direction]`. The difference
is whether the model sees a label or a constraint at the moment it begins generating
candidates. A direction axis (`Audience Shift`, `Aggressive`, `Incremental`) immediately
limits which candidates are on-lens. Names-only defers that constraint to when the model
assigns lens tags.

### 5. 20.1% simplification with zero essential criterion loss (QU5)

370 words removed across 35 targeted cuts. Every cut removes elaboration, restatement,
or motivation text — no rule bearing on a rubric criterion was removed. The simplified
form has a higher signal-to-word ratio: each sentence maps more directly to a criterion.
This matters for long-context generation: a leaner prompt reduces the risk of the model
treating explanatory text as instructional weight.

---

## Final Rubric Criteria Summary (v19)

**50 criteria total. Max: 205 pts.**

### Essential (5 criteria — any fail blocks golden)

| ID | Name | Test |
|----|------|------|
| C-01 | Volume | 20–40 distinct ideas inclusive |
| C-02 | Idea Anatomy | Every idea: name + pitch + category + rationale |
| C-03 | Top-5 Marker | Exactly 5 ideas marked `**` |
| C-04 | Inertia Check | Do Nothing entry with trajectory rationale |
| C-05 | AMEND Section | Labeled section, exactly 3 directional adjustments |

### Recommended (20 criteria — weight 30%)

C-06 Category Grouping · C-07 Pitch Quality · C-08 Rationale Depth · C-09 AMEND Quality ·
C-10 No Overlap · C-11 Lens Attribution · C-12 Displacement Sentence · C-13 Inertia Frame ·
C-14 Peer-Comparison Registry · C-15 Registry Sentence Quality · C-16 Marking Ban ·
C-17 Rationalization Block · C-18 Sequential-Default Check · C-19 AMEND Distribution-Shift ·
C-20 Inertia Placement · C-21 Phase-Tag Lifecycle · C-22 Dimension Coverage ·
C-23 Lens Re-Run Test · C-24 Net-Count Spec · C-25 Phase-Entry Verbatim

### Aspirational (25 criteria — weight 10%)

C-26 Dual-Anchor Gate · C-27 Causal Trigger · C-28 Dual-Frame Conclusion ·
C-29 Dual-Anchor Parity · C-30 Negation-Frame · C-31 Phase-0 Inertia Prefacing ·
C-32 Net-Count Phase-Close Echo · C-33 Phase-0 Lifecycle Double-Mark ·
C-34 Pre-Phase Lifecycle Close Signal · C-35 Pre-Phase Lifecycle Double-Mark ·
C-36 Phase-1 Lifecycle Close Signal · C-37 Phase-1 Lifecycle Double-Mark ·
C-38 Phase-2 Lifecycle Close Signal · C-39 Phase-2 Lifecycle Double-Mark ·
C-40 Phase-3 GATE Close Signal · C-41 Phase-3 GATE Double-Mark ·
C-42 Pre-Phase Close Lens Enumeration (C-47) · C-43 Phase-1 Open Active-Lens Echo (C-48) ·
C-44 Phase-1 Open Lens Direction Echo (C-49) · C-45 Phase-0 Open Lens-Name Carry (C-50) ·
C-46 AMEND Direction-Shift Specificity · C-47 Registry Peer Same-Section Rule ·
C-48 Prohibition-B Replacement Source Fixed · C-49 Phase-0 Displacement Target One-Sentence ·
C-50 Session-Close Signal

### R20 Score (V-05 / QU5 simplified)

| Rubric | Score | Max |
|--------|-------|-----|
| v18 (scoring rubric at run time) | 195 | 195 |
| v19 (projected — C-49 + C-50 added) | **200** | 205 |
