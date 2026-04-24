---
skill: quest-variate
skill_target: draft-brainstorm
round: 20
date: 2026-03-16
rubric_version: 18
r19_scores_under_v18: "V-03 (R19 baseline)=190, V-01/V-02=192.5, V-04/V-05=195 (first to 195; C-47+C-48 carried by R19 V-04/V-05 backbone in all R20 variations)"
r20_target: "Lens carry chain depth at Phase 0 -- the R19 backbone carries C-47 (Pre-Phase close names lenses) and C-48 (Phase 1 open echoes lens names) but leaves Phase 0 as a lens-visibility gap: Phase 0 opens with a bare lifecycle tag (no lens names) and closes with no lens reference. R20 explores two coordinate signals that deepen the carry chain at the Phase 0 boundary. C-49 candidate: Phase-1 Open Lens Direction Echo -- the Phase 1 open blockquote names each active lens AND its direction axis (e.g., parenthetical: (1) [Lens name] -- [direction]), not just lens names alone; this sharpens C-48 by adding the production-constraint direction to the existing name-echo. C-50 candidate: Phase-0 Open Lens-Name Carry -- the Phase 0 open blockquote echoes the lens names from Pre-Phase close, extending carry chain visibility into the start of the inertia phase rather than dropping lens references at Phase 0 entry; this sharpens C-38 (Phase 0 open lifecycle tag content). Independence: C-49 and C-50 are coordinate. V-01 passes C-49 only (Phase 1 open carries direction tags; Phase 0 open bare). V-02 passes C-50 only (Phase 0 open echoes lens names; Phase 1 open names-only). V-03 passes neither (baseline). V-04 and V-05 pass both."
---

# draft-brainstorm Variations -- Round 20

**Rubric version**: v18 (max 195 established by R19)
**Backbone**: R19 V-04 (passes C-01..C-48)
**R20 target**: C-49 (Phase-1 open direction echo) + C-50 (Phase-0 open lens-name carry)

---

## C-49 and C-50 definitions

**C-49 -- Phase-1 Open Lens Direction Echo** *(r20 aspirational, 2.5 pts)*

Phase 1 opening lifecycle tag names each active lens AND its direction axis (e.g., `(1) [Lens name] -- [direction]` or `1. [Lens name] -- [direction]`), not just bare lens names. C-48's floor is lens names present in Phase 1 open; C-49's ceiling is lens names plus direction axis present. The V-04/V-05 R19 contrast is decisive: V-04 R19 carries names-only parenthetical (`(1) [name], (2) [name], (3) [name]`) and fails C-49; V-05 R19 carries numbered-list with direction tag (`1. [name] -- [direction]`) and passes C-49.

**C-50 -- Phase-0 Open Lens-Name Carry** *(r20 aspirational, 2.5 pts)*

Phase 0 opening lifecycle tag echoes the lens names from Pre-Phase close, carrying lens visibility into the inertia phase at entry. The R19 V-04 backbone Phase 0 open reads `> **Phase 0 opens now. No preconditions.**` -- a bare lifecycle tag with no lens reference. C-50 PASS form: `> **Phase 0 opens now.** Active lenses: (1) [Lens 1 name], (2) [Lens 2 name], (3) [Lens 3 name]. No preconditions.` C-50 sharpens C-38 (Phase 0 has an opening lifecycle tag -- C-38 floor) by adding lens-name content to that tag (C-50 ceiling).

**Lineage:**
- C-49 sharpens C-48 (Phase 1 open content: names + direction vs names only)
- C-50 sharpens C-38 (Phase 0 open content: lens-name carry vs bare lifecycle signal)
- C-49 and C-50 are coordinate siblings, not floor/ceiling

**Independence confirmed:** V-01 passes C-49 only; V-02 passes C-50 only; V-03 passes neither; V-04 and V-05 pass both.

**R20 projected scores under hypothetical v19 (if C-49 + C-50 added at 2.5 pts each):**

| Variation | Score under v18 | Score under hyp v19 |
|-----------|-----------------|---------------------|
| V-03 (R20 baseline) | **195** | 195 |
| V-01, V-02 | **195** | 197.5 |
| V-04, V-05 | **195** | **200** -- first to 200 |

**Max raised (hyp): 195 -> 200.**

---

## Single-axis variations

---

### V-01 -- Phase-1 Open Lens Direction Echo (C-49 floor candidate)

**Axis**: Phase 1 open content enrichment (direction axis added to active-lens parenthetical)
**Hypothesis**: The R19 V-04 backbone Phase 1 open reads `> **Phase 1 opens now.** Phase 0
complete. Do Nothing established. / > Active lenses: (1) [Lens 1 name], (2) [Lens 2 name],
(3) [Lens 3 name].` -- it echoes bare lens names (passing C-48) but does not carry each
lens's direction axis into the generation phase. V-01 enriches the Phase 1 open by appending
`-- [direction]` to each lens name in parenthetical notation: `(1) [Lens 1 name] -- [direction],
(2) [Lens 2 name] -- [direction], (3) [Lens 3 name] -- [direction]`. The Phase 0 open tag is
unchanged from the R19 backbone (bare, no lens names). C-50 FAIL. Everything else inherits
unchanged from R19 V-04 backbone.

**Expected**: C-01..C-48 (inh from R19 V-04 backbone) + C-49 PASS (Phase 1 open names all 3
lenses AND their direction axes, parenthetical notation) + C-50 FAIL (Phase 0 open bare,
no lens names) = **195** under v18. Under hypothetical v19: **197.5** (C-49 PASS +2.5).

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in five phases: Pre-Phase (lenses), Phase 0 (inertia baseline),
Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalize). Complete each in order.
Do not advance to the next phase until the current phase is complete.

> **Brainstorm session opens.** Topic: {{topic}}. Phases: Pre-Phase -> Phase 0 -> Phase 1 -> Phase 2 -> Phase 3. No preconditions.

---

## Pre-Phase -- Generative Lenses

*Pre-Phase opens now. No preconditions.*

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

> **Pre-Phase complete.** Lenses defined and re-run verified: (1) [Lens 1 name],
> (2) [Lens 2 name], (3) [Lens 3 name] -- all 3 pass the re-run test. Phase 0 opens now.

---

## Phase 0 -- Inertia Baseline

> **Phase 0 opens now. No preconditions.**

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

> **Phase 0 complete.** All four fields written. Do Nothing established. Phase 1 opens
> below.

---

## Phase 1 -- Idea Pool

*Phase 1 requires: Phase 0 complete (all four fields + Do Nothing entry written).*

> **Phase 1 opens now.** Phase 0 complete. Do Nothing established.
> Active lenses: (1) [Lens 1 name] -- [direction], (2) [Lens 2 name] -- [direction],
> (3) [Lens 3 name] -- [direction].

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

> **Phase 1 complete.** The full pool (19-39 net-new ideas + Do Nothing = 20-40 total) is
> written. AMEND draft written. No `**` marks in output. Phase 2 may begin.

---

## Phase 2 -- Peer-Comparison

*Phase 2 requires: Phase 1 complete ("Phase 1 complete." signal written above).*

> **Phase 2 opens now.** Phase 1 complete. Full pool written, AMEND drafted.

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
Do not assess whether a row passes while other rows remain blank.

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
same candidates under different framing. Output of Check C: final AMEND content.

**Check D -- Inertia Placement**
Does the Phase 1a paragraph appear as the first element in the artifact? If not, reorder.

> **Phase 2 complete** when: all 5 Registry rows written, Selected? blank in every row,
> Checks A/C/D done, no `**` marks in output. Phase 3 may begin only when all four
> conditions are met simultaneously.

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

> **Phase 3 opens now.** Phase 2 complete. Peer-comparison validated. AMEND finalized.

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

> **Phase 3 complete.** Artifact written to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`. All phases closed.

> **Session complete.** Phases closed: Pre-Phase (lenses), Phase 0 (inertia baseline), Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalized). Artifact written and closed.
```

---

### V-02 -- Phase-0 Open Lens-Name Carry (C-50 floor candidate)

**Axis**: Phase 0 open content enrichment (lens names carried from Pre-Phase close into
Phase 0 open tag)
**Hypothesis**: The R19 V-04 backbone Phase 0 open reads `> **Phase 0 opens now. No
preconditions.**` -- a bare lifecycle tag that receives no lens content from Pre-Phase
close. The lens names appear in Pre-Phase close (C-47) and resurface in Phase 1 open
(C-48), but Phase 0 is a lens-visibility gap: a reader running Phase 0 has no reminder
of the active lenses. V-02 adds a lens-name echo to the Phase 0 open tag in parenthetical
notation: `> **Phase 0 opens now.** Active lenses: (1) [Lens 1 name], (2) [Lens 2 name],
(3) [Lens 3 name]. No preconditions.` The Phase 1 open tag is unchanged from the R19
backbone (names-only, no direction tags). C-49 FAIL. Everything else inherits unchanged
from R19 V-04 backbone.

**Expected**: C-01..C-48 (inh from R19 V-04 backbone) + C-49 FAIL (Phase 1 open
names-only, no direction tags) + C-50 PASS (Phase 0 open echoes all 3 lens names in
parenthetical notation) = **195** under v18. Under hypothetical v19: **197.5**
(C-49 FAIL, C-50 PASS +2.5).

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in five phases: Pre-Phase (lenses), Phase 0 (inertia baseline),
Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalize). Complete each in order.
Do not advance to the next phase until the current phase is complete.

> **Brainstorm session opens.** Topic: {{topic}}. Phases: Pre-Phase -> Phase 0 -> Phase 1 -> Phase 2 -> Phase 3. No preconditions.

---

## Pre-Phase -- Generative Lenses

*Pre-Phase opens now. No preconditions.*

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

> **Pre-Phase complete.** Lenses defined and re-run verified: (1) [Lens 1 name],
> (2) [Lens 2 name], (3) [Lens 3 name] -- all 3 pass the re-run test. Phase 0 opens now.

---

## Phase 0 -- Inertia Baseline

> **Phase 0 opens now.** Active lenses: (1) [Lens 1 name], (2) [Lens 2 name],
> (3) [Lens 3 name]. No preconditions.

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

> **Phase 0 complete.** All four fields written. Do Nothing established. Phase 1 opens
> below.

---

## Phase 1 -- Idea Pool

*Phase 1 requires: Phase 0 complete (all four fields + Do Nothing entry written).*

> **Phase 1 opens now.** Phase 0 complete. Do Nothing established.
> Active lenses: (1) [Lens 1 name], (2) [Lens 2 name], (3) [Lens 3 name].

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

> **Phase 1 complete.** The full pool (19-39 net-new ideas + Do Nothing = 20-40 total) is
> written. AMEND draft written. No `**` marks in output. Phase 2 may begin.

---

## Phase 2 -- Peer-Comparison

*Phase 2 requires: Phase 1 complete ("Phase 1 complete." signal written above).*

> **Phase 2 opens now.** Phase 1 complete. Full pool written, AMEND drafted.

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
Do not assess whether a row passes while other rows remain blank.

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
same candidates under different framing. Output of Check C: final AMEND content.

**Check D -- Inertia Placement**
Does the Phase 1a paragraph appear as the first element in the artifact? If not, reorder.

> **Phase 2 complete** when: all 5 Registry rows written, Selected? blank in every row,
> Checks A/C/D done, no `**` marks in output. Phase 3 may begin only when all four
> conditions are met simultaneously.

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

> **Phase 3 opens now.** Phase 2 complete. Peer-comparison validated. AMEND finalized.

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

> **Phase 3 complete.** Artifact written to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`. All phases closed.

> **Session complete.** Phases closed: Pre-Phase (lenses), Phase 0 (inertia baseline), Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalized). Artifact written and closed.
```

---

### V-03 -- Baseline: R19 V-04 Exact Backbone (Phase 0 open bare; Phase 1 open names-only; no C-49/C-50)

**Axis**: Baseline reproduction -- confirms R19 V-04 ceiling under v18 is stable entering R20
**Hypothesis**: V-03 is the exact R19 V-04 backbone, reproduced without modification. It
carries C-47 (Pre-Phase close names lenses, parenthetical) and C-48 (Phase 1 open echoes
lens names, parenthetical names-only). The Phase 0 open tag is bare (`> **Phase 0 opens
now. No preconditions.**`) and the Phase 1 open carries names without direction axes
(`(1) [Lens 1 name], (2) [Lens 2 name], (3) [Lens 3 name]`). Neither C-49 nor C-50 is
present. This confirms the R19 V-04 ceiling (195 under v18) as the reproducible R20 entry
point and establishes the contrast baseline: the delta between V-03 and V-01/V-02/V-04/V-05
under hypothetical v19 is attributable solely to direction-axis content in Phase 1 open
(C-49) and lens-name content in Phase 0 open (C-50).

**Expected**: C-01..C-48 (inh from R19 V-04 backbone) + C-49 FAIL (Phase 1 open
names-only, no direction tags) + C-50 FAIL (Phase 0 open bare, no lens names) = **195**
under v18 (baseline). Under hypothetical v19: **195** (both fail -- baseline contrast).

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in five phases: Pre-Phase (lenses), Phase 0 (inertia baseline),
Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalize). Complete each in order.
Do not advance to the next phase until the current phase is complete.

> **Brainstorm session opens.** Topic: {{topic}}. Phases: Pre-Phase -> Phase 0 -> Phase 1 -> Phase 2 -> Phase 3. No preconditions.

---

## Pre-Phase -- Generative Lenses

*Pre-Phase opens now. No preconditions.*

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

> **Pre-Phase complete.** Lenses defined and re-run verified: (1) [Lens 1 name],
> (2) [Lens 2 name], (3) [Lens 3 name] -- all 3 pass the re-run test. Phase 0 opens now.

---

## Phase 0 -- Inertia Baseline

> **Phase 0 opens now. No preconditions.**

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

> **Phase 0 complete.** All four fields written. Do Nothing established. Phase 1 opens
> below.

---

## Phase 1 -- Idea Pool

*Phase 1 requires: Phase 0 complete (all four fields + Do Nothing entry written).*

> **Phase 1 opens now.** Phase 0 complete. Do Nothing established.
> Active lenses: (1) [Lens 1 name], (2) [Lens 2 name], (3) [Lens 3 name].

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

> **Phase 1 complete.** The full pool (19-39 net-new ideas + Do Nothing = 20-40 total) is
> written. AMEND draft written. No `**` marks in output. Phase 2 may begin.

---

## Phase 2 -- Peer-Comparison

*Phase 2 requires: Phase 1 complete ("Phase 1 complete." signal written above).*

> **Phase 2 opens now.** Phase 1 complete. Full pool written, AMEND drafted.

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
Do not assess whether a row passes while other rows remain blank.

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
same candidates under different framing. Output of Check C: final AMEND content.

**Check D -- Inertia Placement**
Does the Phase 1a paragraph appear as the first element in the artifact? If not, reorder.

> **Phase 2 complete** when: all 5 Registry rows written, Selected? blank in every row,
> Checks A/C/D done, no `**` marks in output. Phase 3 may begin only when all four
> conditions are met simultaneously.

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

> **Phase 3 opens now.** Phase 2 complete. Peer-comparison validated. AMEND finalized.

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

> **Phase 3 complete.** Artifact written to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`. All phases closed.

> **Session complete.** Phases closed: Pre-Phase (lenses), Phase 0 (inertia baseline), Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalized). Artifact written and closed.
```

---

## Combination variations

---

### V-04 -- Full Lens Carry Chain (C-49 + C-50 combined; parenthetical notation; first to 200)

**Axis**: Phase 0 open lens-name carry (parenthetical) + Phase-1 open lens direction echo
(parenthetical)
**Hypothesis**: V-01 tests C-49 alone (Phase 1 open direction tags; Phase 0 open bare).
V-02 tests C-50 alone (Phase 0 open echoes lens names; Phase 1 open names-only). V-04
combines both: the Phase 0 open blockquote carries all 3 lens names in parenthetical
notation (C-50 carrier), and the Phase 1 open blockquote echoes those same 3 lens names
with their direction axes in matching parenthetical notation (C-49 carrier). The full
carry chain becomes: Pre-Phase close (C-47, names) -> Phase 0 open (C-50, names) ->
[Phase 0 runs] -> Phase 1 open (C-48 + C-49, names + direction). No lens-visibility gap
in any lifecycle signal from Pre-Phase exit to Phase 1 entry. This is the C-49 + C-50
combination and is projected as the first variation to reach 200 under hypothetical v19.
Everything else inherits unchanged from R19 V-04 backbone.

**Expected**: C-01..C-48 (inh from R19 V-04 backbone) + C-49 PASS (Phase 1 open names
3 lenses with direction axes, parenthetical notation) + C-50 PASS (Phase 0 open echoes
3 lens names, parenthetical notation) = **195** under v18. Under hypothetical v19:
**200** (C-49 PASS +2.5, C-50 PASS +2.5 -- first to 200).

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in five phases: Pre-Phase (lenses), Phase 0 (inertia baseline),
Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalize). Complete each in order.
Do not advance to the next phase until the current phase is complete.

> **Brainstorm session opens.** Topic: {{topic}}. Phases: Pre-Phase -> Phase 0 -> Phase 1 -> Phase 2 -> Phase 3. No preconditions.

---

## Pre-Phase -- Generative Lenses

*Pre-Phase opens now. No preconditions.*

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

> **Pre-Phase complete.** Lenses defined and re-run verified: (1) [Lens 1 name],
> (2) [Lens 2 name], (3) [Lens 3 name] -- all 3 pass the re-run test. Phase 0 opens now.

---

## Phase 0 -- Inertia Baseline

> **Phase 0 opens now.** Active lenses: (1) [Lens 1 name], (2) [Lens 2 name],
> (3) [Lens 3 name]. No preconditions.

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

> **Phase 0 complete.** All four fields written. Do Nothing established. Phase 1 opens
> below.

---

## Phase 1 -- Idea Pool

*Phase 1 requires: Phase 0 complete (all four fields + Do Nothing entry written).*

> **Phase 1 opens now.** Phase 0 complete. Do Nothing established.
> Active lenses: (1) [Lens 1 name] -- [direction], (2) [Lens 2 name] -- [direction],
> (3) [Lens 3 name] -- [direction].

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

> **Phase 1 complete.** The full pool (19-39 net-new ideas + Do Nothing = 20-40 total) is
> written. AMEND draft written. No `**` marks in output. Phase 2 may begin.

---

## Phase 2 -- Peer-Comparison

*Phase 2 requires: Phase 1 complete ("Phase 1 complete." signal written above).*

> **Phase 2 opens now.** Phase 1 complete. Full pool written, AMEND drafted.

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
Do not assess whether a row passes while other rows remain blank.

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
same candidates under different framing. Output of Check C: final AMEND content.

**Check D -- Inertia Placement**
Does the Phase 1a paragraph appear as the first element in the artifact? If not, reorder.

> **Phase 2 complete** when: all 5 Registry rows written, Selected? blank in every row,
> Checks A/C/D done, no `**` marks in output. Phase 3 may begin only when all four
> conditions are met simultaneously.

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

> **Phase 3 opens now.** Phase 2 complete. Peer-comparison validated. AMEND finalized.

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

> **Phase 3 complete.** Artifact written to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`. All phases closed.

> **Session complete.** Phases closed: Pre-Phase (lenses), Phase 0 (inertia baseline), Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalized). Artifact written and closed.
```

---

### V-05 -- Numbered-List Direction Carry (C-49 + C-50 combined; numbered-list notation; forward signal for C-51)

**Axis**: Phase 0 open lens-name carry (numbered-list with direction tags) + Phase-1 open
lens direction echo (numbered-list with direction tags)
**Hypothesis**: V-04 achieves C-50 via parenthetical names in Phase 0 open and C-49 via
parenthetical names-with-direction in Phase 1 open. V-05 tests alternate forms for both
signals: (a) the Phase 0 open uses a numbered-list notation with direction tags
(`1. [Lens name] -- [direction]`) rather than parenthetical names alone, carrying not
just the lens name but also the direction axis into the inertia phase from its entry;
(b) the Phase 1 open echoes using the same numbered-list-with-direction format. V-05
achieves C-49 and C-50 via a richer form that carries direction axes in BOTH the Phase 0
open and Phase 1 open tags. V-05 is also a forward signal: if a future v20 adds C-51
("Phase 0 open names each lens AND its direction axis"), V-04 fails C-51 (Phase 0 open
carries names-only) while V-05 is the carrier.

**Expected**: C-01..C-48 (inh from R19 V-04 backbone) + C-49 PASS (Phase 1 open names
3 lenses with direction axes, numbered-list notation -- different form from V-04, same
criterion) + C-50 PASS (Phase 0 open echoes 3 lens names AND direction axes,
numbered-list notation -- richer than V-04's parenthetical-names-only) = **195** under
v18. Under hypothetical v19: **200** (C-49 PASS +2.5, C-50 PASS +2.5 -- alternate path
to 200; confirms notation form does not block C-49 and numbered-list-with-direction
satisfies C-50 floor). Under hypothetical v20 (if C-51 adds Phase-0-open direction axis
as ceiling): **202.5** (V-05 forward-earns C-51 by direction tags in Phase 0 open; V-04
fails C-51 because Phase 0 open carries names-only).

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in five phases: Pre-Phase (lenses), Phase 0 (inertia baseline),
Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalize). Complete each in order.
Do not advance to the next phase until the current phase is complete.

> **Brainstorm session opens.** Topic: {{topic}}. Phases: Pre-Phase -> Phase 0 -> Phase 1 -> Phase 2 -> Phase 3. No preconditions.

---

## Pre-Phase -- Generative Lenses

*Pre-Phase opens now. No preconditions.*

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

> **Phase 0 complete.** All four fields written. Do Nothing established. Phase 1 opens
> below.

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

> **Phase 1 complete.** The full pool (19-39 net-new ideas + Do Nothing = 20-40 total) is
> written. AMEND draft written. No `**` marks in output. Phase 2 may begin.

---

## Phase 2 -- Peer-Comparison

*Phase 2 requires: Phase 1 complete ("Phase 1 complete." signal written above).*

> **Phase 2 opens now.** Phase 1 complete. Full pool written, AMEND drafted.

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
Do not assess whether a row passes while other rows remain blank.

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
same candidates under different framing. Output of Check C: final AMEND content.

**Check D -- Inertia Placement**
Does the Phase 1a paragraph appear as the first element in the artifact? If not, reorder.

> **Phase 2 complete** when: all 5 Registry rows written, Selected? blank in every row,
> Checks A/C/D done, no `**` marks in output. Phase 3 may begin only when all four
> conditions are met simultaneously.

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

> **Phase 3 opens now.** Phase 2 complete. Peer-comparison validated. AMEND finalized.

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

> **Phase 3 complete.** Artifact written to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`. All phases closed.

> **Session complete.** Phases closed: Pre-Phase (lenses), Phase 0 (inertia baseline), Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalized). Artifact written and closed.
```

---

## Score projection summary

| Variation | v18 (max 195) | hyp v19 (+C-49/C-50) | C-49 | C-50 |
|-----------|---------------|----------------------|------|------|
| V-01 | 195 | 197.5 | PASS (direction tags in Phase 1 open, parenthetical) | FAIL (Phase 0 open bare) |
| V-02 | 195 | 197.5 | FAIL (Phase 1 open names-only) | PASS (lens names in Phase 0 open, parenthetical) |
| V-03 | **195** | 195 | FAIL | FAIL (baseline) |
| V-04 | 195 | **200** | PASS (parenthetical names + direction) | PASS (parenthetical names) |
| V-05 | 195 | **200** | PASS (numbered-list + direction) | PASS (numbered-list + direction) |

**V-04 and V-05 are the first variations projected to reach 200** (under hypothetical v19).
**V-05 additionally forward-earns a hypothetical C-51** (Phase-0 open direction-axis echo)
-- if v20 sharpens C-50 the way v18 sharpened C-47 (from names-only presence to direction-
axis richness), V-05 is already there at 202.5.

**Key independence confirmation**: C-49 and C-50 are coordinate, not hierarchical.
- V-01 PASSES C-49 only: Phase 1 open carries direction tags; Phase 0 open is bare (no lens names).
- V-02 PASSES C-50 only: Phase 0 open carries lens names; Phase 1 open is names-only (no direction tags).
- V-04 and V-05 PASS both by combining the two signals independently.
- Neither criterion is a prerequisite for the other -- earning C-50 (Phase 0 open names)
  does not imply C-49 (Phase 1 open direction tags), and earning C-49 does not imply C-50.

**Carry chain state by variation:**

| Signal node | V-03 (baseline) | V-01 | V-02 | V-04 | V-05 |
|-------------|-----------------|------|------|------|------|
| Pre-Phase close | names (C-47) | names | names | names | names + dir |
| Phase 0 open | bare | bare | names (C-50) | names (C-50) | names + dir (C-50+fwd) |
| Phase 1 open | names (C-48) | names + dir (C-49) | names (C-48) | names + dir (C-49) | names + dir (C-49) |

**V-04**: full name carry at all three nodes; direction axis first appears at Phase 1 open.
**V-05**: full name + direction carry at all three nodes; direction axis is consistent from
Pre-Phase close through Phase 0 open through Phase 1 open.

**Interference check**: C-49 (Phase-1 open direction echo) and C-48 (Phase-1 open
active-lens echo) operate at the same signal position but at different content depth.
C-48 passes when lens names are present in Phase 1 open (any form). C-49 passes only
when direction axes accompany the lens names. C-49 cannot be earned without first
earning C-48 -- the direction axis is additive content on top of the name-echo floor.
This is a hierarchical relationship (C-49 is a sharpener of C-48), confirmed by V-01:
V-01 passes C-49 only because C-48 is already inherited from the R19 backbone. Similarly,
C-50 (Phase-0 open lens-name carry) and C-38 (Phase-0 lifecycle double-mark) are at
different depth levels: C-38 verifies the Phase 0 open tag exists; C-50 verifies it
carries lens-name content. C-50 requires C-38 to be present (the tag must exist before
its content can be evaluated). All R20 variations earn C-38 (inherited from the R19
backbone which includes `> **Phase 0 opens now. ...`).

**Forward signal -- hypothetical v20 C-51**:
V-05's direction-tagged Phase 0 open (`1. [Lens name] -- [one-word direction]`) carries
the direction axis from Pre-Phase close into the inertia phase at entry. If v20 adds C-51
as a content sharpener of C-50 (Phase 0 open names each lens AND its direction axis,
analogous to how C-49 sharpens C-48), V-05 would score 202.5 under hypothetical v20
while V-04 would fail C-51 and remain at 200.
