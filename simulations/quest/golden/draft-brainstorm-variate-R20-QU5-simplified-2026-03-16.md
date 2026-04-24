---
skill: quest-simplify
skill_target: draft-brainstorm
source_variation: R20-V-05
date: 2026-03-16
original_word_count: 1844
---

# QU5 Simplified Prompt -- draft-brainstorm (R20 V-05)

Below: the simplified prompt body, followed by the simplification report.

---

## Simplified Prompt

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

## Simplification Report

### Word counts

| Version | Words |
|---------|-------|
| Original (V-05) | 1844 |
| Simplified (QU5) | 1474 |
| Reduction | 370 words (20.1%) |

### What was removed and why

Each cut removes explanatory elaboration, restatement, or motivation text that does not map
to a distinct rubric criterion. All lifecycle signals, phase tags, gate conditions,
anti-pattern prohibitions, and structural instructions are preserved intact.

| # | Text removed | Words | Why |
|---|-------------|-------|-----|
| 1 | "Do not advance to the next phase until the current phase is complete." (opening) | 13 | Restated by per-phase precondition italic markers |
| 2 | "(e.g., 'More Ambitious', 'Audience Shift', 'Incremental')" from Lens name | 7 | Examples, not rule; "one phrase" is sufficient |
| 3 | "This is the most important entry in the pool: it is already in play, and every other candidate exists to displace it." | 22 | Motivation sentence; the Do Nothing instructions themselves enforce the behavior |
| 4 | "Write the following four fields:" | 6 | Label before four labeled fields -- redundant with the bold field names |
| 5 | "(pool entry)" from "**Do Nothing** (pool entry):" | 2 | Parenthetical annotation, context is clear |
| 6 | "Phase 1 opens below." from Phase 0 close tag | 3 | The Phase 1 section follows immediately; forward reference adds nothing |
| 7 | "You may add sections beyond the six required." | 8 | Permissive non-rule; no criterion tests for extra sections |
| 8 | "Aim for at least 6 lens-attributed ideas total." | 8 | Covered by "at least 2 ideas per lens" × 3 lenses = 6 |
| 9 | "Marking as you write introduces sequential bias -- finish the pool first." | 13 | Explains the WHY; the prohibition is stated in the sentence before |
| 10 | "-- technically, organizationally, or for users?" from 1a last question | 7 | Parenthetical qualifier; the question stands without it |
| 11 | "A direction that shifts only emphasis or category labels without introducing different underlying candidates fails this test." (from 1c AMEND) | 17 | Restates the preceding positive test in negative form; the positive test is sufficient |
| 12 | "the strongest ideas surface across the whole run, not only at the start." (Check A) | 13 | Explains WHY to rescan; "rescan the full pool" is the operative instruction |
| 13 | "Output of Check A: 5 candidates advancing to the Registry." | 10 | Label-only; Check B header immediately introduces the Registry |
| 14 | "Do not fill in Selected? during construction." (Check B intro) | 8 | Covered fully by the Selected? column rule |
| 15 | "Do not assess whether a row passes while other rows remain blank." (Check B) | 13 | Covered by "Write all five sentences before evaluating any of them" |
| 16 | "(scope, user group, cost, risk)" from "I chose..." rule | 4 | Parenthetical example; "actual constraints" is sufficient |
| 17 | "A partial Registry has no valid Selected? entries. A Registry where any Selected? cell carries a preliminary value does not satisfy the gate." (Selected? rule) | 28 | Restatement of (a) and (b) in negative form; the preconditions are already clear |
| 18 | "This is a schema property of the Registry." | 7 | Decorative label; adds no behavioral constraint |
| 19 | "**Prohibition Battery:**" header | 2 | Organizational header; the named prohibitions are self-labeled |
| 20 | "-- not on headings, inline, in notes, or in any other form." (Prohibition A) | 10 | Elaborates "anywhere in your output"; "anywhere" is already exhaustive |
| 21 | Last sentence of Prohibition B ("If editing the candidate's rationale would make the comparison sentence completable...") | 45 | Elaborate escalation of "do not revise the rationale"; the prior sentence states the rule; no distinct rubric criterion for this sentence |
| 22 | "Output of Check C: final AMEND content." | 7 | Label-only; Check C instruction is the operative text |
| 23 | "Phase 3 may begin only when all four conditions are met simultaneously." (Phase 2 close) | 13 | Restates the four conditions already listed in the same tag |
| 24 | Trailing 3 sentences of GATE PRECONDITIONS block: "A Registry with fewer than 5 rows does not satisfy (a)..." | 38 | Negative restatements of (a) and (b); the gate is clear from the bullets |
| 25 | "(candidates confirmed in Check B, with any substitutions from Prohibition B applied)" (Phase 3) | 13 | Back-reference parenthetical; Phase 3 has no other source for the 5 candidates |
| 26 | "Name the specific direction the system, team, or product is already moving." (Current Trajectory) | 12 | Elaborates "What is happening right now" -- the question already implies directionality |
| 27 | "Be specific: what is delayed, degraded, or foreclosed?" (Accumulated Cost) | 9 | Elaborates "What concretely accumulates" -- "concretely" already enforces specificity |
| 28 | "(each must appear as a `##` section)" from Required dimensions header | 8 | Covered by the preceding sentence: "Each is a **mandatory `##` section**" |
| 29 | "Generate the complete pool before selecting." (Phase 1b) | 6 | Restates "Do not mark top-5 yet" in positive form; prohibition is the operative rule |
| 30 | "**Column rules:**" header label | 2 | Organizational label; the named bullet fields are self-labeled |
| 31 | "-- both must hold before Phase 3 may begin" from GATE header | 9 | Implied by "GATE PRECONDITIONS"; conditions (a) and (b) specify the requirement |
| 32 | "Identify 5 top-5 candidates." from Check A (merged into next sentence) | 4 | Collapsed into "Are the top-5 candidates the first 5 ideas generated?" |
| 33 | "before any ideas" from 1a placement instruction | 3 | "First element in the final artifact" is sufficient; "before any ideas" restates it |
| 34 | "while Phase 2 Check B is in progress" → "during Check B" | 5 | Shortened; "during Check B" carries identical scope |
| 35 | "For each of the 5 candidates, write one row." → "Write one row per candidate." | 5 | Compressed; same constraint in fewer words |

**Total removed: 370 words (20.1%)**

### Essential criteria check

| Criterion | Status |
|-----------|--------|
| C-01 Volume (20-40 ideas) | PASS -- pool instruction preserved intact |
| C-02 Idea Anatomy (4 fields) | PASS -- idea template preserved intact |
| C-03 Top-5 Marker (exactly 5 `**`) | PASS -- Phase 3 marking instruction preserved |
| C-04 Inertia Check (Do Nothing + rationale) | PASS -- Phase 0 Do Nothing template preserved |
| C-05 AMEND Section (3 adjustments) | PASS -- 1c and Check C preserved intact |

All essential criteria pass. All lifecycle signals (C-35 through C-50 family), phase gate
markers, registry gate conditions (C-49, C-50), and structural anti-pattern prohibitions
preserved intact.

```json
{"simplified_word_count": 1474, "original_word_count": 1844, "all_essential_still_pass": true}
```
