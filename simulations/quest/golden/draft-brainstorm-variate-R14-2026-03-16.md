---
skill: quest-variate
skill_target: draft-brainstorm
round: 14
date: 2026-03-16
rubric_version: 13
r13_scores_under_v13: "V-01=170, V-02=167.5 (C-15 FAIL), V-03=170, V-04=170, V-05=167.5 (C-15 FAIL)"
r14_target: "Extend the dual-anchor lifecycle principle (C-38) to the Pre-Phase/Phase-0 boundary. C-39 candidate: Pre-Phase closing blockquote only (close signal, no opening tag). C-40 candidate: Pre-Phase double-mark -- both opening lifecycle tag AND closing blockquote, the full C-38 pattern applied one phase earlier. V-01 carries C-39 only; V-02 and V-04 carry C-40 (which subsumes C-39); V-03 carries neither (baseline contrast); V-05 carries C-40 + C-15 FAIL."
r14_expected_scores_under_v13: "V-01=170, V-02=170, V-03=170, V-04=170, V-05=167.5 (C-15 FAIL)"
r14_c39_c40_projection: "Under hypothetical v14 adding C-39 (2.5 pts) and C-40 (2.5 pts, requiring BOTH opening tag + closing blockquote on Pre-Phase): V-01=172.5 (C-39 PASS, C-40 FAIL -- close signal only, no opening tag), V-02=175 (C-39+C-40 PASS), V-03=170 (both FAIL -- no Pre-Phase lifecycle signals), V-04=175 (C-39+C-40 PASS in conversational register), V-05=172.5 (C-39+C-40 PASS, C-15 FAIL cancels 2.5 pts: 167.5+5=172.5). Max raised: 170 to 175."
---

# Variate R14 -- draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01, V-02, V-03), then combinations (V-04, V-05).

R14 extracts two candidate criteria from R13 excellence signals by applying the
dual-anchor lifecycle principle (C-38) one phase earlier -- to the Pre-Phase/Phase-0
boundary:

- **C-39 candidate** Pre-Phase Lifecycle Close Signal -- the Pre-Phase section ends
  with an explicit blockquote close signal naming the gate condition: all 3 lenses
  passed the re-run test, Phase 0 opens. C-38 applied the closing-tag principle to
  Phase 0; C-39 extends it to the boundary immediately preceding Phase 0.
  A Pre-Phase that ends with a prose gate instruction ("Do not begin Phase 0 until...")
  without a blockquote signal fails C-39 -- the gate must be signaled as a lifecycle
  event, not only as a conditional instruction.

- **C-40 candidate** Pre-Phase Lifecycle Double-Mark -- the Pre-Phase is doubly-marked:
  an explicit opening lifecycle tag (e.g., "*Pre-Phase opens now. No preconditions.*")
  AND an explicit closing blockquote, making the Pre-Phase activation state unambiguous
  for its full duration. Directly parallels C-38 (Phase-0 Lifecycle Double-Mark).
  A Pre-Phase with a closing blockquote but no opening lifecycle tag satisfies C-39 but
  fails C-40 -- the double-mark requires both.

**R13 delta**: All R13 variations carry a plain-text gate at the end of Pre-Phase
("Do not begin Phase 0 until all 3 lenses pass the re-run test") but none carry a
blockquote close signal on Pre-Phase, and none carry an opening lifecycle tag on
Pre-Phase. V-01 R14 introduces the close signal (C-39 carrier). V-02 R14 adds both
the opening tag and close signal (C-40 carrier). V-03 R14 is the baseline -- no
Pre-Phase at all, confirming that the 170-point ceiling is stable without these
signals. V-04 R14 carries C-40 in conversational register. V-05 R14 carries C-40
with intentional C-15 FAIL (prose format).

---

## Variation Axes

| Axis | Description |
|------|-------------|
| Pre-Phase close signal | Whether Pre-Phase ends with blockquote close (C-39 candidate) |
| Pre-Phase double-mark | Whether Pre-Phase has opening lifecycle tag + closing blockquote (C-40 candidate) |
| Lifecycle scope | Pre-Phase present vs. absent entirely |
| Output format | Mandatory `##` dimension sections (C-15 PASS) vs. bold-header prose groups (C-15 FAIL) |
| Phrasing register | Formal third-person imperative vs. conversational second-person |

## Single-axis variations

---

### V-01 -- Pre-Phase Lifecycle Close Signal (C-39 candidate only)

**Axis**: Pre-Phase close signal
**Hypothesis**: All R13 variations end the Pre-Phase with a prose gate instruction
("Do not begin Phase 0 until all 3 lenses pass the re-run test") but none use a
blockquote close signal. V-01 R14 adds a blockquote immediately after the lens
gate instruction: `> **Pre-Phase complete.** All 3 lenses pass the re-run test.
Phase 0 opens now.` This is the C-39 carrier signal -- the close signal without
an opening lifecycle tag on Pre-Phase (C-40 requires both). Tests whether the
blockquote close signal at Pre-Phase end is a naturally stable addition under the
formal AMEND-first register of V-01 R13, and whether it produces any interference
with the Phase 0 opening tag (which says "No preconditions" -- the Pre-Phase is
not a formal precondition to Phase 0 under C-38 framing, so the two signals must
coexist cleanly). Everything else is the V-01 R13 backbone.

**Expected**: C-01..C-38 PASS (inh from V-01 R13) + C-39 PASS (Pre-Phase closing
blockquote present) + C-40 FAIL (no Pre-Phase opening lifecycle tag -- close signal
only) = **170** under v13. Under hypothetical v14: **172.5** (C-39+2.5, C-40 FAIL).

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

> **Pre-Phase complete.** All 3 lenses pass the re-run test. Phase 0 opens now.

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

### V-02 -- Pre-Phase Lifecycle Double-Mark (C-40 candidate -- full dual-anchor)

**Axis**: Pre-Phase double-mark
**Hypothesis**: V-01 R14 carries only the Pre-Phase closing blockquote (C-39 candidate).
V-02 R14 adds the opening lifecycle tag on Pre-Phase as well -- `*Pre-Phase opens now.
No preconditions.*` -- creating the full C-40 double-mark pattern: an unambiguous opening
signal at the start of Pre-Phase AND a closing blockquote when all lenses pass. This
directly mirrors C-38 (Phase-0 Lifecycle Double-Mark) applied one phase earlier. The test:
does the Pre-Phase opening tag coexist cleanly with the Phase 0 opening tag that follows?
Both say "opens now" -- the model must not conflate them. The Phase 0 tag says "No
preconditions" (accurate: Phase 0 has no preconditions in the rubric-structural sense
since Pre-Phase is not a formal gate on Phase 0 within the rubric, only within the skill
instruction). C-15 PASS. Everything else identical to V-01 R14 (which is the V-01 R13
backbone plus Pre-Phase close signal).

**Expected**: C-01..C-38 PASS (inh) + C-39 PASS (closing blockquote present) + C-40 PASS
(opening lifecycle tag + closing blockquote on Pre-Phase) = **170** under v13. Under
hypothetical v14: **175** (C-39+C-40 both PASS).

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in five phases: Pre-Phase (lenses), Phase 0 (inertia baseline),
Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalize). Complete each in order.
Do not advance to the next phase until the current phase is complete.

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

> **Pre-Phase complete.** All 3 lenses pass the re-run test. Phase 0 opens now.

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

### V-03 -- Baseline: No Pre-Phase, Terse Register (Neither C-39 nor C-40)

**Axis**: Lifecycle scope (no Pre-Phase at all)
**Hypothesis**: V-01 and V-02 test whether adding lifecycle signals to Pre-Phase is
stable. V-03 is the baseline contrast: no Pre-Phase section, no lenses, direct Phase 0
open. This tests two things: (a) the 170-pt ceiling holds without a Pre-Phase entirely,
confirming C-39/C-40 absence does not break any existing criterion; (b) a terse/technical
phrasing register -- instructions written as minimal directives, not explanatory prose --
is stable at 170. Terse register strips elaboration from every phase: "Write four fields."
not "Write the following four fields, which serve the purpose of..." The register shift
tests whether brevity breaks any criterion that depends on explanatory framing. C-15 PASS
(mandatory `##` sections preserved despite terse language). Neither C-39 nor C-40 carrier.
Under v13: 170. Under v14: 170 (contrast point confirming both signals are new additions,
not regression from R13).

**Expected**: C-01..C-38 PASS = **170** under v13. Under hypothetical v14: **170**
(C-39 FAIL -- no Pre-Phase, no closing blockquote; C-40 FAIL -- no Pre-Phase at all).

---

```
Run `draft-brainstorm` for topic: {{topic}}

Phases: Phase 0 (inertia) -> Phase 1 (pool) -> Phase 2 (peer-comparison) ->
Phase 3 (finalize). Complete in sequence. Do not advance until the current phase
signals complete.

---

## Phase 0 -- Inertia Baseline

> **Phase 0 opens now. No preconditions.**

Write four fields for the Do Nothing option on {{topic}}. This entry is already in play.
Every other idea in Phase 1 exists to displace it.

**Current Trajectory**: Direction {{topic}} is moving with no intervention. (2-3 sentences.)

**Accumulated Cost**: What accumulates -- technically, organizationally, for users -- if
this trajectory runs 12 more months. Specific: what is delayed, degraded, or foreclosed.
(2-3 sentences.)

**Displacement Target**: Minimum bar for a competing idea: "A candidate beats Do Nothing
if and only if it [specific condition]." (1 sentence.)

**Do Nothing** (pool entry):
```
**Pitch**: One sentence -- the trajectory above compressed.
**Rationale**: The Accumulated Cost compressed to one sentence.
```

> **Phase 0 complete.** All four fields written. Do Nothing established. Phase 1 opens.

---

## Phase 1 -- Idea Pool

*Phase 1 requires: Phase 0 complete.*

### 1a. Inertia Frame

Write a paragraph (3-5 sentences) for a general reader: current trajectory for {{topic}},
what the team inherits with no decision, what the path of least resistance produces.
This paragraph goes first in the artifact, before any ideas.

### 1b. Idea Pool

Generate **19-39 additional candidates** for {{topic}} -- total pool 20-40 including
Do Nothing. One **mandatory `##` section** per required dimension. Do not collapse.
You may add sections beyond the six required.

**Required `##` sections:**
- `## Scope` -- how much of {{topic}}'s problem space is addressed
- `## Timing` -- when the intervention lands in the product lifecycle
- `## Integration` -- how it connects to existing systems or teams
- `## Audience` -- who benefits most
- `## Build vs. Buy` -- internal build, external adoption, or extension of existing
- `## Status Quo` -- the Do Nothing entry from Phase 0 exactly

**Do not mark top-5 yet.** Finish the full pool before selecting. No `**` markers
during Phase 1. Sequential marking introduces bias -- complete the pool first.

Each idea (except Do Nothing):
```
### [Idea Name]
**Pitch**: One sentence.
**Rationale**: Specific to {{topic}} -- real constraint, user need, or opportunity.
One sentence on how this idea changes the Phase 0 trajectory: what it displaces or
prevents.
```

### 1c. AMEND Draft

Three pool-shift directions. Each must:
- Name the shift axis
- State what kinds of ideas appear or disappear
- Pass the distribution-shift test: re-running with this directive alone must produce
  candidate ideas not in the current pool -- different candidates, not different labels
  for the same candidates. Label-shift fails the test.

Do not finalize -- verified in Phase 2 Check C.

> **Phase 1 complete.** The full pool (19-39 net-new ideas + Do Nothing = 20-40 total)
> is written. AMEND draft written. No `**` marks in output. Phase 2 may begin.

---

## Phase 2 -- Peer-Comparison

*Phase 2 requires: Phase 1 complete ("Phase 1 complete." written above).*

**Check A -- Sequential Default**
Name 5 top-5 candidates. Are they the first 5 ideas written? If yes, rescan -- strongest
candidates appear across the full run, not only at the start. Output: 5 candidates for
the Registry.

**Check B -- Peer-Comparison Registry**

Write one row per candidate. Leave Selected? blank throughout construction.

| # | Candidate (exact name) | Peer (exact name, same ## section, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|------------------------|----------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

Write all five sentences before evaluating any. Do not assess a row while others are blank.

**Column rules:**
- **Candidate**: exact name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same `##` section; not blank
- **"I chose ... because ___"**: specific reason tied to {{topic}}'s constraints (scope,
  user group, cost, risk). "better" or "more viable" do not satisfy the requirement.
- **Selected?**: gate column. Cannot hold any value, and Phase 3 cannot begin, until:
  (a) all 5 rows written, AND (b) Selected? blank across all 5 rows -- simultaneously.
  Partial Registry: no valid Selected? entries. Any preliminary value: gate not satisfied.
  Phase 3 may begin only when the Registry is structurally complete (5 rows) and
  selection-clean (Selected? blank in every row). This is a schema property of the Registry.

**Prohibition Battery:**

**Prohibition A -- Marking Ban**: No `**` marks anywhere in output while Check B is in
progress. Not on headings, inline, in notes. No marks until the complete 5-row Registry
is written.

**Prohibition B -- Rationalization Block**: If the comparison sentence cannot be completed
for any row -- no specific peer holds, no specific reason -- replace that candidate with
the peer named in the Peer column. Replacement source is fixed: the peer from this row, not
an alternative chosen after reconsidering. Do not revise the candidate's rationale to
manufacture a distinction not present at comparison time. If editing the rationale would
make the comparison sentence completable, that desire confirms the replacement obligation
applies -- the impulse to revise so the comparison can pass is not permission to reopen the
comparison; it is the signal the swap is mandatory.

**Check C -- AMEND Distribution-Shift Test**
For each of the 3 AMEND directions: re-running with only this directive must surface
candidate ideas not in the current pool. Sharpen any that produce the same candidates
under different framing. Output of Check C: final AMEND content.

**Check D -- Inertia Placement**
Does the 1a paragraph appear as the first element in the artifact? Reorder if not.

> **Phase 2 complete** when: all 5 Registry rows written, Selected? blank in every row,
> Checks A/C/D done, no `**` marks in output. Phase 3 may begin only when all four
> conditions hold simultaneously.

---

## Phase 3 -- Finalize

*Phase 3 requires: Phase 2 complete (5-row Registry written, Selected? blank in all rows).*

> **GATE PRECONDITIONS -- both must hold before Phase 3 may begin:**
> - **(a)** All 5 rows of the Peer-Comparison Registry are written in your output
> - **(b)** Selected? is blank across all 5 rows of the Registry
>
> Registry fewer than 5 rows: (a) fails. Any Selected? value in any row: (b) fails.
> Both must hold simultaneously.

Fill Selected? = YES in exactly 5 rows. Mark those 5 ideas with `**` on their headings
in the dimension sections. Use AMEND content from Check C.

Write the artifact to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Inertia paragraph (1a), Phase 0 baseline block, dimension sections
(top-5 marked), Peer-Comparison Registry, AMEND. Total including Do Nothing: 20-40.
```

---

## Combined-axis variations

---

### V-04 -- Pre-Phase Double-Mark + Conversational Register (C-40 in informal phrasing)

**Axes**: Pre-Phase double-mark (C-40 candidate) + Phrasing register (conversational
second-person throughout)
**Hypothesis**: V-02 R13 confirmed C-40's sibling signals (C-37/C-38) survive in formal
register. V-04 R13 confirmed conversational register is stable at 170. V-04 R14 combines
C-40 (Pre-Phase double-mark) with conversational register to test whether the two lifecycle
signals -- "*Pre-Phase is live now. No preconditions.*" and "> **Pre-Phase done.** All 3
lenses clear. Phase 0 is up." -- read naturally in informal second-person and whether the
schema property language ("This is a schema property of the Registry") survives informality
(C-33 signal). The AMEND-first structure from V-04 R13 is preserved: lenses are named
before Phase 0 even in the conversational variant. C-15 PASS (mandatory `##` sections,
stated as "you need these six sections").

**Expected**: C-01..C-38 PASS (inh from V-04 R13 backbone + Pre-Phase double-mark added)
+ C-39 PASS (Pre-Phase closing blockquote) + C-40 PASS (opening lifecycle tag + closing
blockquote on Pre-Phase) = **170** under v13. Under hypothetical v14: **175**.

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

Here's the flow: you'll name your lenses first, anchor the inertia baseline, build the
pool against both, stress-test your top picks, then write the artifact. Five phases --
complete each before moving to the next.

---

### Pre-Phase -- Name Your Lenses

*Pre-Phase is live now. No preconditions.*

Before anything else, define 3 directions that will intentionally pull the pool somewhere
it wouldn't naturally go. Use these as active constraints while you generate in Phase 1 --
not as a filter you apply after the pool is already written.

For each lens, answer three things:
- **What's the shift?** One phrase: "More Aggressive Scope", "Different Primary User", etc.
- **What changes?** One sentence: what kinds of ideas appear under this lens that wouldn't
  show up in a default brainstorm? Name candidate types, not framing differences.
- **Does it pass the re-run test?** If a reader took only this lens and re-ran the
  brainstorm, would they get ideas that aren't in your current pool? Different candidates,
  not the same candidates in different wording. If not, sharpen the lens.

Write all 3 lenses before moving on.

> **Pre-Phase done.** All 3 lenses pass the re-run test. Phase 0 is up.

---

### Phase 0 -- Anchor the Inertia Baseline

> **Phase 0 is live now. No preconditions to clear.**

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

> **Phase 0 done.** The Do Nothing entry goes in the Status Quo section of Phase 1.
> Every other idea you generate will be held against the Displacement Target. Phase 1
> opens now.

---

### Phase 1 -- Build the Pool

*Phase 1 requires: Phase 0 done (all four fields + Do Nothing entry above).*

#### 1a. Inertia Frame

Write a paragraph (3-5 sentences) translating the Phase 0 baseline into plain language:
what's the current trajectory for {{topic}}, what does the team inherit with no decision,
what does the path of least resistance produce.

This paragraph goes first in the artifact, before any ideas.

#### 1b. Idea Pool

Generate **19-39 additional ideas** for {{topic}} -- total of 20-40 including Do Nothing.
You need these six sections as `##` headings -- mandatory, do not collapse into a flat
list:

- `## Scope` -- how much of {{topic}}'s problem space this addresses
- `## Timing` -- when the intervention lands in the product lifecycle
- `## Integration` -- how it connects to existing systems or teams
- `## Audience` -- who benefits most
- `## Build vs. Buy` -- internal build, external adoption, or extension of existing
- `## Status Quo` -- the Do Nothing entry from Phase 0 exactly

Use your Pre-Phase lenses while you generate. Tag at least 2 ideas per lens inline
(e.g., `[Lens: More Aggressive Scope]`). Center-of-gravity ideas are fine -- just
don't let them crowd out the lens-influenced ones.

**Don't mark top-5 yet.** Finish the whole pool before picking. No `**` marks during
Phase 1 -- marking as you go introduces sequential bias, and you'll get a better pool
if you complete it first.

Each idea (other than Do Nothing):
```
### [Idea Name]
**Pitch**: One sentence.
**Rationale**: Specific to {{topic}} -- real constraint, user need, or opportunity.
One sentence on how it changes the Phase 0 trajectory: what it displaces or prevents.
```

#### 1c. Draft AMEND

Write a draft AMEND section: 3 directions for a future run of this brainstorm. Each must
name the shift and say what kinds of ideas would appear or disappear -- not different
framing, different candidates. The re-run test: a reader who took only this direction and
re-ran should get ideas not in your current pool. You'll sharpen these in Phase 2.

Don't finalize yet.

> **Phase 1 done.** The full pool (19-39 net-new ideas + Do Nothing = 20-40 total) is
> built. AMEND draft written. No `**` marks anywhere. Phase 2 opens now.

---

### Phase 2 -- Verify

*Phase 2 requires: Phase 1 done (full pool written, AMEND draft written, no `**` marks).*

#### Check A -- Sequential Default

Pick your 5 top-5 candidates. Are they the first 5 you wrote? If yes, that's sequential
default -- scan the full pool again. Strongest candidates surface across the whole run,
not just at the start.

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
- **Candidate**: exact name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same `##` section; not blank
- **"I chose ... because ___"**: a specific reason tied to {{topic}}'s actual constraints
  -- scope, users, cost, risk. "Better" or "more viable" don't count.
- **Selected?**: gate column. Can't hold any value, and Phase 3 can't start, until:
  (a) all 5 rows are written, AND (b) Selected? is blank across all 5 rows -- both
  at the same time. A partial Registry has no valid Selected? entries. Any preliminary
  value anywhere means the gate isn't satisfied. Phase 3 opens only when the Registry
  is structurally complete (5 rows) and selection-clean (Selected? blank in all rows).
  This is a schema property of the Registry.

**Prohibition Battery:**

**Prohibition A -- Marking Ban**: No `**` marks in your output while Check B is in
progress -- not on headings, not inline, not in notes. No marks until the complete 5-row
Registry is written.

**Prohibition B -- Rationalization Block**: If you can't complete the comparison sentence
for any row -- no specific peer holds, no specific reason applies -- that candidate gets
replaced by the peer in the Peer column. Replacement source is fixed: the peer from this
row, not a different one you pick after reconsidering. Don't revise the candidate's
rationale to manufacture a distinction that wasn't there at comparison time. If editing
the rationale would make the comparison completable, that desire confirms the replacement
obligation applies -- the impulse to revise so the comparison can pass is not permission
to reopen the comparison; it is the signal the swap is mandatory.

#### Check C -- AMEND Distribution-Shift Test

For each of the 3 AMEND directions: does re-running with only that directive surface
candidate ideas not in the current pool? Different candidates, not different framing.
Sharpen any that don't pass. Output: final AMEND content.

#### Check D -- Inertia Placement

Does the 1a paragraph appear as the first element in the artifact? Move it if not.

> **Phase 2 done** when: all 5 Registry rows written, Selected? blank in every row,
> Checks A/C/D complete, no `**` marks in the output. Phase 3 opens only when all
> four conditions hold at the same time.

---

### Phase 3 -- Finalize

*Phase 3 requires: Phase 2 done (5-row Registry written, Selected? blank in all rows).*

> **GATE PRECONDITIONS -- both must hold before Phase 3 may begin:**
> - **(a)** All 5 rows of the Peer-Comparison Registry are written in your output
> - **(b)** Selected? is blank across all 5 rows of the Registry
>
> Registry with fewer than 5 rows: (a) fails. Any Selected? value anywhere: (b) fails.
> Both must hold at the same time.

Fill Selected? = YES in exactly 5 rows. Mark those 5 ideas with `**` on their `##`
headings in the dimension sections. Use the AMEND content from Check C.

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
Comparison Registry, AMEND. Total including Do Nothing: 20-40.
```

---

### V-05 -- Pre-Phase Double-Mark + Prose Format (C-40 + C-15 FAIL intentional)

**Axes**: Pre-Phase double-mark (C-40 candidate) + Output format (prose category
groups, C-15 FAIL intentional)
**Hypothesis**: V-05 R13 confirmed C-37/C-38 survive in prose format (167.5 score --
C-15 FAIL, all else PASS). V-05 R14 adds the C-40 pattern (Pre-Phase double-mark) to
the prose-format backbone and intentionally sacrifices C-15. Test: does the Pre-Phase
opening lifecycle tag maintain its signal clarity in prose format, where phase boundaries
use `##` headings but category groups use bold labels only? The risk: with bold labels
used for both phase openings and category names, the distinction between `*Pre-Phase is
live now.*` (a lifecycle tag) and `**Scope**` (a category label) must remain unambiguous.
The italic lifecycle tag vs bold category label is the signal disambiguation mechanism.
C-15 remains intentionally sacrificed -- the gain from C-40 should net: 167.5 + 5.0 =
172.5 under hypothetical v14.

**Expected**: C-01..C-14 PASS (inh), C-15 FAIL (bold-header category groups, no mandatory
`##` sections -- intentional), C-16..C-38 PASS (inh) + C-39 PASS (Pre-Phase closing
blockquote) + C-40 PASS (opening lifecycle tag + closing blockquote on Pre-Phase) =
**167.5** under v13. Under hypothetical v14: **172.5** (C-39+C-40 PASS: +5.0; C-15 FAIL:
-2.5 from base 170; 170+5.0-2.5=172.5).

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in five phases: Pre-Phase (lenses), Phase 0 (inertia baseline),
Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalize). Complete each in order.
Do not advance to the next phase until the current phase is complete.

---

## Pre-Phase -- Generative Lenses

*Pre-Phase opens now. No preconditions.*

Before writing a single idea or establishing the inertia baseline, define 3 directions
that will actively pull the pool away from its center of gravity. These are production
constraints -- they determine which ideas that appear in Phase 1, not which ideas survive
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

> **Pre-Phase complete.** All 3 lenses pass the re-run test. Phase 0 opens now.

---

## Phase 0 -- Inertia Baseline

*Phase 0 opens now. No preconditions.*

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

### 1a. Inertia Frame

Write a paragraph (3-5 sentences) expanding on the Phase 0 baseline for a general reader:
What is the current trajectory for {{topic}}? What does the team inherit if no deliberate
decision is made? What does the path of least resistance produce -- technically,
organizationally, or for users?

This paragraph must appear as the first element in the final artifact, before any ideas.

### 1b. Idea Pool

Using the 3 Pre-Phase lenses as active generation constraints, generate **19-39 additional
candidates** for {{topic}} -- for a total pool of 20-40 including the Phase 0 Do Nothing
entry. Present ideas as flowing prose-grouped entries under bold category headers. Use
4-7 distinct categories that represent genuinely different dimensions (e.g., scope,
timing, integration approach, audience, build vs. buy, risk tolerance) -- do not use
`##` headings for categories; bold labels only.

**Do not mark top-5 yet.** Generate the complete pool before selecting. Do not place any
`**` markers on any idea during Phase 1. Marking as you write introduces sequential bias --
finish the pool first.

Format each group as:

```
**[Category Name]**

**[Idea Name]**: [one-sentence pitch] -- [rationale: one to two sentences citing a real
constraint, user need, or opportunity specific to {{topic}}. Include one sentence naming
how this idea changes the Phase 0 trajectory.]
```

The Do Nothing entry from Phase 0 goes in a **Status Quo** category. Its rationale must
extend the Phase 0 analysis -- what the current trajectory concretely produces for {{topic}}.

**Lens attribution**: Tag at least 2 ideas per lens inline (e.g., `[Lens: Audience Shift]`).
Aim for at least 6 lens-attributed ideas total.

### 1c. AMEND Draft

Write a draft AMEND section with 3 pool-shift directions. For each:
- Name the shift axis
- Describe what kinds of ideas would appear or disappear
- Apply the distribution-shift test: re-running with only this directive must surface
  candidate ideas not in the current pool. Different candidates, not the same candidates
  under different framing. A direction that shifts only labels or emphasis without changing
  underlying candidate types fails this test.

Do not finalize yet.

> **Phase 1 complete.** The full pool (19-39 net-new ideas + Do Nothing = 20-40 total) is
> written. AMEND draft written. No `**` marks in output. Phase 2 may begin.

---

## Phase 2 -- Peer-Comparison

*Phase 2 requires: Phase 1 complete ("Phase 1 complete." signal written above).*

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

> **Phase 2 complete** when: all 5 Registry rows written, Selected? blank in every row,
> Checks A/C/D done, no `**` marks in output. Phase 3 may begin.

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
Displacement Target), prose category groups (top-5 marked, lens tags removed),
Peer-Comparison Registry, AMEND. Total ideas including Do Nothing: 20-40.
```

---

## R14 Scoring Summary Under v13

| Variation | Axis | C-15 | C-39 carrier | C-40 carrier | v13 score |
|-----------|------|------|--------------|--------------|-----------|
| V-01 | Pre-Phase close blockquote only | PASS | YES | NO | 170 |
| V-02 | Pre-Phase double-mark (full) | PASS | YES | YES | 170 |
| V-03 | No Pre-Phase, terse register | PASS | NO | NO | 170 |
| V-04 | Pre-Phase double-mark + conversational | PASS | YES | YES | 170 |
| V-05 | Pre-Phase double-mark + prose format | FAIL | YES | YES | 167.5 |

## R14 Projected Scores Under Hypothetical v14 (C-39 + C-40 added at 2.5 pts each)

| Variation | v14 score | Notes |
|-----------|-----------|-------|
| V-02 | **175** | C-39 PASS + C-40 PASS -- first to 175 |
| V-04 | **175** | C-39 PASS + C-40 PASS in conversational register |
| V-01 | **172.5** | C-39 PASS + C-40 FAIL (close only, no opening tag) |
| V-05 | **172.5** | C-39+C-40 PASS, C-15 FAIL (-2.5): 170+5-2.5 |
| V-03 | **170** | Neither C-39 nor C-40 -- baseline contrast |

**Max raised under v14: 170 to 175.** V-03 confirms the 170 floor is stable without
Pre-Phase lifecycle signals -- the new criteria are additions, not regressions.

## C-39 / C-40 Extraction Notes for v14

**C-39 -- Pre-Phase Lifecycle Close Signal** (2.5 pts):
- Sharpens C-35: C-35 is the floor (Phase 0 is a dedicated pre-generation phase);
  C-39 is the ceiling (the Pre-Phase -- the phase that precedes Phase 0 -- also carries
  an explicit closing lifecycle signal, extending the blockquote-boundary principle
  to the earliest addressable phase boundary in the skill).
- Pass condition: The Pre-Phase section ends with an explicit blockquote close signal
  naming the gate condition (e.g., "> **Pre-Phase complete.** All 3 lenses pass the
  re-run test. Phase 0 opens now."). A prose gate instruction alone ("Do not begin
  Phase 0 until all 3 lenses pass") fails -- the signal must be a lifecycle blockquote.
- Distinguishes from C-38: C-38 passes when Phase 0 carries both an opening and closing
  lifecycle signal. C-39 passes when the phase immediately preceding Phase 0 (the Pre-Phase
  or lenses phase) carries a closing blockquote. C-38 and C-39 can coexist; neither
  subsumes the other.

**C-40 -- Pre-Phase Lifecycle Double-Mark** (2.5 pts):
- Sharpens C-39: C-39 is the floor (Pre-Phase closing blockquote present); C-40 is the
  ceiling (Pre-Phase is doubly-marked with BOTH an opening lifecycle tag AND a closing
  blockquote -- the full C-38 double-mark pattern applied one phase earlier).
- Pass condition: The Pre-Phase section carries (a) an opening lifecycle tag (e.g.,
  "*Pre-Phase opens now. No preconditions.*" or "*Pre-Phase is live now.*") AND (b) a
  closing blockquote (C-39 requirement). A Pre-Phase with only a closing blockquote (no
  opening tag) satisfies C-39 but fails C-40. A Pre-Phase with only an opening tag (no
  closing blockquote) satisfies neither. Both must be present.
- Distinguishes from C-39: C-39 passes when the closing blockquote is present in any
  form. C-40 passes only when both the opening lifecycle tag and the closing blockquote
  are present -- the Pre-Phase activation state is unambiguous at both entry and exit.
