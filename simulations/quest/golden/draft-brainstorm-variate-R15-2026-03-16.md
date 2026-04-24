---
skill: quest-variate
skill_target: draft-brainstorm
round: 15
date: 2026-03-16
rubric_version: 14
r14_scores_under_v14: "V-02=175, V-04=175, V-01=172.5, V-05=172.5, V-03=170"
r15_target: "Apply the dual-anchor lifecycle principle (C-38/C-40) to Phase 1 and Phase 2. C-41 candidate: Phase 1 lifecycle opening tag -- Phase 1 already carries a closing blockquote; adding an opening blockquote creates the full dual-anchor on Phase 1. C-42 candidate: Phase 2 lifecycle opening tag -- same logic applied one phase later. V-01 carries C-41 only (Phase 1 opening tag, no Phase 2 tag). V-02 carries C-41+C-42 (both openings added -- maximum lifecycle coverage). V-03 is the pure V-02 R14 baseline (175 floor, neither C-41 nor C-42). V-04 carries C-41+C-42 in conversational register. V-05 carries C-41+C-42 with intentional C-15 FAIL (prose format)."
r15_expected_scores_under_v14: "V-01=175, V-02=175, V-03=175, V-04=175, V-05=172.5 (C-15 FAIL)"
r15_c41_c42_projection: "Under hypothetical v15 adding C-41 (2.5 pts) and C-42 (2.5 pts): V-01=177.5 (C-41 PASS, C-42 FAIL -- Phase 1 opening only), V-02=180 (C-41+C-42 PASS -- first to 180), V-03=175 (both FAIL -- pure baseline contrast), V-04=180 (C-41+C-42 PASS in conversational register), V-05=177.5 (C-41+C-42 PASS, C-15 FAIL: 172.5+5=177.5). Max raised: 175 to 180."
---

# Variate R15 -- draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01, V-02, V-03), then combinations (V-04, V-05).

R15 extends the dual-anchor lifecycle principle one step further than R14. R14 applied
it to the Pre-Phase/Phase-0 boundary (C-39: Pre-Phase close signal; C-40: Pre-Phase
full dual-anchor). R15 applies it to Phase 1 and Phase 2:

- **C-41 candidate** Phase 1 Lifecycle Opening Tag -- Phase 1 already carries a closing
  blockquote (`> **Phase 1 complete.**...`). Adding a blockquote opening tag gives Phase 1
  the full dual-anchor: `> **Phase 1 opens now.** Phase 0 complete. Do Nothing established.`
  This mirrors exactly what C-38 did for Phase 0, and what C-40 did for Pre-Phase -- the
  pattern is consistent: if a phase has a closing lifecycle blockquote, adding an opening
  blockquote completes the dual-anchor. Phase 1's plain italic requires-line
  (`*Phase 1 requires:...*`) is not a lifecycle opening tag; C-41 adds a structural one.

- **C-42 candidate** Phase 2 Lifecycle Opening Tag -- Phase 2 already carries a closing
  blockquote (`> **Phase 2 complete** when:...`). Adding a blockquote opening tag gives
  Phase 2 the full dual-anchor: `> **Phase 2 opens now.** Phase 1 complete. Full pool
  written, AMEND drafted.` Phase 2's plain italic requires-line is not a lifecycle opening
  tag; C-42 adds a structural one.

**R14 delta**: All R14 variations (V-01 through V-05) carry the Pre-Phase dual-anchor
(C-39/C-40) but none carry Phase 1 or Phase 2 opening lifecycle blockquotes. V-01 R15
introduces the Phase 1 opening tag only (C-41 carrier). V-02 R15 adds both Phase 1 and
Phase 2 opening tags (C-41+C-42 carrier). V-03 R15 is the pure V-02 R14 baseline --
no Phase 1 or Phase 2 opening tags -- confirming 175 is stable without these signals.
V-04 R15 carries C-41+C-42 in conversational register. V-05 R15 carries C-41+C-42
with intentional C-15 FAIL.

---

## Variation Axes

| Axis | Description |
|------|-------------|
| Phase 1 opening tag | Whether Phase 1 opens with a lifecycle blockquote (C-41 candidate) |
| Phase 2 opening tag | Whether Phase 2 opens with a lifecycle blockquote (C-42 candidate) |
| Lifecycle scope | Both new tags vs. Phase 1 only vs. neither |
| Output format | Mandatory `##` sections (C-15 PASS) vs. bold-header prose groups (C-15 FAIL) |
| Phrasing register | Formal third-person blockquote vs. conversational second-person |

## Single-axis variations

---

### V-01 -- Phase 1 Lifecycle Opening Tag (C-41 candidate only)

**Axis**: Phase 1 opening tag
**Hypothesis**: All R14 variations carry the Pre-Phase dual-anchor (C-39+C-40) but none
add a lifecycle opening blockquote to Phase 1. Phase 1 already has a closing blockquote
(`> **Phase 1 complete.**...`). V-01 R15 adds a blockquote immediately after the Phase 1
requires-line: `> **Phase 1 opens now.** Phase 0 complete. Do Nothing established.` This
is the C-41 carrier -- the Phase 1 opening tag without a Phase 2 opening tag (C-42
requires both Phase 1 and Phase 2 to be tagged). Tests whether the Phase 1 opening
blockquote coexists cleanly with the Phase 0 closing signal that precedes it (`Phase 1
opens below.`) -- the two signals reference the same transition from two sides. Everything
else is the V-02 R14 backbone (Pre-Phase double-mark, formal register, mandatory `##`
sections, C-15 PASS).

**Expected**: C-01..C-40 PASS (inh from V-02 R14) + C-41 PASS (Phase 1 opening
blockquote present) + C-42 FAIL (no Phase 2 opening blockquote) = **175** under v14.
Under hypothetical v15: **177.5** (C-41+2.5, C-42 FAIL).

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

> **Phase 1 opens now.** Phase 0 complete. Do Nothing established.

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

### V-02 -- Phase 1 + Phase 2 Lifecycle Opening Tags (C-41 + C-42 candidates -- full coverage)

**Axis**: Phase 1 opening tag + Phase 2 opening tag
**Hypothesis**: V-01 R15 adds the Phase 1 opening blockquote only (C-41). V-02 R15
adds both Phase 1 AND Phase 2 opening blockquotes, achieving the full lifecycle dual-anchor
across every phase that has a closing signal. Phase 2 closes with `> **Phase 2 complete**
when:...` -- V-02 R15 precedes that with an opening tag immediately after the Phase 2
requires-line: `> **Phase 2 opens now.** Phase 1 complete. Full pool written, AMEND
drafted.` This is the C-42 carrier -- the direct parallel to C-38 (Phase 0 dual-anchor),
C-40 (Pre-Phase dual-anchor), and C-41 (Phase 1 dual-anchor), all now applied to Phase 2.
The test: three consecutive lifecycle opening blockquotes appear in the prompt
(Pre-Phase, Phase 1, Phase 2), plus the Phase 0 blockquote opening from C-38. Do all
four coexist cleanly without the model conflating them? Each names a different transition.
C-15 PASS. Everything else identical to V-01 R15 (which is V-02 R14 backbone plus Phase 1
opening tag).

**Expected**: C-01..C-41 PASS (inh from V-01 R15) + C-42 PASS (Phase 2 opening
blockquote present) = **175** under v14. Under hypothetical v15: **180** (C-41+C-42
both PASS -- first to 180).

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

> **Phase 1 opens now.** Phase 0 complete. Do Nothing established.

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

### V-03 -- Baseline: V-02 R14 Exact (neither C-41 nor C-42)

**Axis**: Lifecycle scope (no Phase 1 or Phase 2 opening tags)
**Hypothesis**: V-01 and V-02 test whether adding lifecycle opening blockquotes to Phase 1
and Phase 2 is stable and scoreable as new criteria. V-03 is the baseline contrast: the
exact V-02 R14 prompt body, unchanged. No Phase 1 opening tag (C-41 absent). No Phase 2
opening tag (C-42 absent). This tests two things: (a) the 175-pt ceiling is reproducible
entering R15 -- confirming no regression from R14; (b) C-41/C-42 absence does not cause
any existing criterion to fail, so the delta between V-03 and V-01/V-02 is solely
attributable to the new signals. Under v14: 175. Under hypothetical v15: 175 (contrast
floor, both C-41 and C-42 FAIL).

**Expected**: C-01..C-40 PASS (inh from V-02 R14) + C-41 FAIL (no Phase 1 opening
blockquote) + C-42 FAIL (no Phase 2 opening blockquote) = **175** under v14. Under
hypothetical v15: **175** (both FAIL -- baseline contrast confirming additions are new,
not regressions).

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

## Combined-axis variations

---

### V-04 -- Phase 1 + Phase 2 Opening Tags + Conversational Register (C-41 + C-42 in informal phrasing)

**Axes**: Phase 1 opening tag (C-41) + Phase 2 opening tag (C-42) + Phrasing register
(conversational second-person throughout)
**Hypothesis**: V-04 R14 confirmed C-39+C-40 survive in conversational register (175
score). V-04 R15 adds C-41+C-42 to the conversational backbone and tests whether two
additional lifecycle opening blockquotes read naturally in informal second-person. The
Phase 1 tag becomes `> **Phase 1 is live.** Phase 0 done -- the inertia baseline is set.`
and the Phase 2 tag becomes `> **Phase 2 is live.** Phase 1 done -- pool built, AMEND
draft written.` The test: with four lifecycle opening blockquotes now present (Pre-Phase,
Phase 0, Phase 1, Phase 2), each naming a distinct transition, does the model correctly
advance state at each one without conflating them? The conversational phrasing
("is live", "done") vs. formal phrasing ("opens now", "complete") must remain internally
consistent. Schema property language preserved (C-33 signal). C-15 PASS (mandatory `##`
sections, stated as "you need these six sections"). AMEND-first structure from V-04 R14
preserved: lenses are named before Phase 0 in the conversational variant.

**Expected**: C-01..C-40 PASS (inh from V-04 R14 backbone + C-41+C-42 added) = **175**
under v14. Under hypothetical v15: **180** (C-41+C-42 both PASS in conversational
register).

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

> **Phase 1 is live.** Phase 0 done -- the inertia baseline is set.

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

> **Phase 2 is live.** Phase 1 done -- pool built, AMEND draft written.

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

### V-05 -- Phase 1 + Phase 2 Opening Tags + Prose Format (C-41 + C-42 + C-15 FAIL intentional)

**Axes**: Phase 1 opening tag (C-41) + Phase 2 opening tag (C-42) + Output format (prose
category groups, C-15 FAIL intentional)
**Hypothesis**: V-05 R14 confirmed C-39+C-40 survive in prose format (172.5 score --
C-15 FAIL, all else PASS). V-05 R15 adds C-41+C-42 to the prose-format backbone and
intentionally sacrifices C-15. In prose format, phase boundaries use `##` headings but
category groups use bold labels only -- lifecycle tags use italic (`*...*`) to distinguish
from bold category labels. V-05 R14 established this disambiguation mechanism. V-05 R15
tests whether Phase 1 and Phase 2 opening italic tags -- `*Phase 1 opens now. Phase 0
complete. Do Nothing established.*` and `*Phase 2 opens now. Phase 1 complete. Full pool
written, AMEND drafted.*` -- remain unambiguous as lifecycle signals when surrounded by
bold category labels in a prose-grouped pool. The gain from C-41+C-42 should net:
172.5 + 5.0 = 177.5 under hypothetical v15. C-15 remains intentionally sacrificed.

**Expected**: C-01..C-14 PASS (inh), C-15 FAIL (bold-header prose groups, no mandatory
`##` sections -- intentional), C-16..C-40 PASS (inh) + C-41 PASS (Phase 1 opening italic
lifecycle tag) + C-42 PASS (Phase 2 opening italic lifecycle tag) = **172.5** under v14.
Under hypothetical v15: **177.5** (C-41+C-42 PASS: +5.0; C-15 FAIL: base stays 172.5;
172.5+5.0=177.5).

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

*Phase 1 opens now. Phase 0 complete. Do Nothing established.*

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

*Phase 2 opens now. Phase 1 complete. Full pool written, AMEND drafted.*

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

## R15 Scoring Summary Under v14

| Variation | Axis | C-15 | C-41 carrier | C-42 carrier | v14 score |
|-----------|------|------|--------------|--------------|-----------|
| V-01 | Phase 1 opening tag only | PASS | YES | NO | 175 |
| V-02 | Phase 1 + Phase 2 opening tags | PASS | YES | YES | 175 |
| V-03 | Baseline (V-02 R14 exact, no new tags) | PASS | NO | NO | 175 |
| V-04 | Phase 1 + Phase 2 opening tags + conversational | PASS | YES | YES | 175 |
| V-05 | Phase 1 + Phase 2 opening tags + prose format | FAIL | YES | YES | 172.5 |

## R15 Projected Scores Under Hypothetical v15 (C-41 + C-42 added at 2.5 pts each)

| Variation | v15 score | Notes |
|-----------|-----------|-------|
| V-02 | **180** | C-41 PASS + C-42 PASS -- first to 180 |
| V-04 | **180** | C-41 PASS + C-42 PASS in conversational register |
| V-01 | **177.5** | C-41 PASS + C-42 FAIL (Phase 1 only, no Phase 2 tag) |
| V-05 | **177.5** | C-41+C-42 PASS, C-15 FAIL (-0 delta vs base 172.5: 172.5+5=177.5) |
| V-03 | **175** | Neither C-41 nor C-42 -- baseline contrast floor |

**Max raised under v15: 175 to 180.** V-03 confirms the 175 floor is stable without Phase
1/Phase 2 lifecycle opening tags -- the new criteria are additions, not regressions from R14.

## C-41 / C-42 Extraction Notes for v15

**C-41 -- Phase 1 Lifecycle Opening Tag** (2.5 pts):
- Sharpens C-38 one phase later: C-38 is the dual-anchor on Phase 0 (both opening and
  closing lifecycle blockquotes on Phase 0); C-41 extends the opening-tag principle to
  Phase 1, which already carries a closing blockquote but no opening blockquote. The
  dual-anchor is now complete on Phase 1.
- Pass condition: Phase 1 section opens with an explicit lifecycle blockquote (or
  equivalent italic lifecycle tag in prose format) naming the transition from Phase 0:
  e.g., `> **Phase 1 opens now.** Phase 0 complete. Do Nothing established.` A plain
  italic requires-line alone (`*Phase 1 requires: Phase 0 complete...*`) fails -- the
  opening must be a lifecycle signal, not only a precondition statement.
- Distinguishes from C-38: C-38 passes when Phase 0 carries the full dual-anchor.
  C-41 passes when Phase 1 carries the full dual-anchor. They are independent: a prompt
  can carry C-38 without C-41 (V-03 R15), C-41 without C-42 (V-01 R15), or both (V-02
  R15).

**C-42 -- Phase 2 Lifecycle Opening Tag** (2.5 pts):
- Sharpens C-41 one phase later: Phase 2 already carries a closing blockquote (`> **Phase
  2 complete** when:...`). C-42 adds an opening lifecycle blockquote to complete the Phase
  2 dual-anchor: e.g., `> **Phase 2 opens now.** Phase 1 complete. Full pool written,
  AMEND drafted.`
- Pass condition: Phase 2 section opens with an explicit lifecycle blockquote (or italic
  lifecycle tag in prose format) naming the transition from Phase 1. The plain italic
  requires-line alone fails -- the opening must be a lifecycle signal.
- Distinguishes from C-41: C-41 is Phase 1; C-42 is Phase 2. C-42 requires both Phase 1
  AND Phase 2 lifecycle opening tags to be present (since C-42 is the Phase 2 opening
  tag specifically). A prompt with Phase 1 opening but no Phase 2 opening carries C-41
  but not C-42. A prompt with both carries both.
- Ceiling signal: With C-41+C-42 PASS, every phase in the skill (Pre-Phase, Phase 0,
  Phase 1, Phase 2) now carries a lifecycle opening blockquote. Phase 3 has no closing
  blockquote and no natural lifecycle close signal, so the dual-anchor principle does not
  extend there. V-02 and V-04 R15 represent the maximum lifecycle coverage achievable
  under the current phase structure.
