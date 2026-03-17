---
skill: quest-variate
skill_target: draft-brainstorm
round: 19
date: 2026-03-16
rubric_version: 17
r18_scores_under_v17: "V-03 (R17 baseline)=185, V-01/V-02=187.5, V-04/V-05=190 (first to 190; C-45+C-46 carried by R18 V-04 backbone in all R19 variations)"
r19_target: "Cross-phase lens reference at Pre-Phase/Phase-1 transitions -- the R18 backbone carries all session-level signals (C-45 phase roster in session-open; C-46 named ledger in session-close) but the lens-attribution chain is not explicitly signaled at phase transitions. The Pre-Phase close says 'All 3 lenses pass the re-run test' without naming the lenses; the Phase 1 open says 'Phase 0 complete. Do Nothing established.' without naming the active lenses. R19 explores whether enriching Pre-Phase close with enumerated lens names (C-47 candidate) and Phase 1 open with an active-lens echo of those names (C-48 candidate) represents the next frontier. C-47 candidate: Pre-Phase Close Lens Enumeration -- the Pre-Phase close blockquote enumerates all 3 lens names in sequence (any ordered notation: parenthetical, numbered), not just 'All 3 lenses pass.' C-48 candidate: Phase-1 Open Active-Lens Echo -- the Phase 1 open blockquote names the 3 active lenses (forward-carrying the Pre-Phase lens names into the generation phase), giving the model an explicit attribution roster before it begins generating ideas. Independence: C-47 and C-48 are coordinate. V-01 passes C-47 only (Pre-Phase close names lenses; Phase 1 open unchanged). V-02 passes C-48 only (Phase 1 open echoes active lenses; Pre-Phase close generic). V-03 passes neither (baseline). V-04 and V-05 pass both."
r19_c47_c48_projection: "Under v17 (current rubric, max 190): all R19 variations score 190 (C-45+C-46 from R18 V-04 backbone). Under hypothetical v18 (adds C-47 Pre-Phase close lens enumeration 2.5 pts + C-48 Phase-1 open active-lens echo 2.5 pts): V-03=190 (both FAIL -- baseline), V-01/V-02=192.5 (one PASS, one FAIL), V-04=195 (C-47 PASS parenthetical + C-48 PASS parenthetical -- first to 195), V-05=195 (C-47 PASS numbered-list + C-48 PASS numbered-list -- alternate path to 195). Max raised: 190 -> 195."
---

# Variate R19 -- draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01, V-02, V-03), then combinations (V-04, V-05).

R19 extends the lifecycle signal enrichment established in R18. R18 placed phase-named
content in the outermost session signals (C-45: session-open phase roster; C-46:
session-close named ledger). R19 targets the **lens-attribution chain at the Pre-Phase
to Phase-1 transition** -- the interior lifecycle signals at the point where lens
definitions convert from preparatory work into active generation constraints.

| Phase/Level | Close signal | Open signal (double-mark) | Criteria |
|-------------|-------------|--------------------------|---------|
| Phase 0 | C-37 | C-38 | R13 |
| Pre-Phase | C-39 | C-40 | R14 |
| Phase 1 | C-41 | C-42 | R15 |
| Phase 2 | C-43 | C-44 | R16 (current max before C-45/C-46) |
| Session | C-47* | C-48* | hypothetical v18 (R18's internal naming) |
| Session content | C-46 | C-45 | v17 (current rubric) |
| Pre-Phase close content | C-47 candidate | -- | **R19 targets** (hypothetical v18) |
| Phase-1 open content | -- | C-48 candidate | **R19 targets** (hypothetical v18) |

*Note: R18 internally named the session existence criteria C-47/C-48; those are now C-45/C-46
in v17. R19 proposes new C-47/C-48 for the lens-attribution enrichment layer.

R18 V-04 backbone is the starting point for all R19 variations. It carries every
lifecycle signal through the session level including both C-45 (session-open phase roster,
arrow notation) and C-46 (session-close named-phase ledger) -- confirmed as scoring 190
under v17.

**C-47 candidate** -- Pre-Phase Close Lens Enumeration: The Pre-Phase close blockquote
enumerates all 3 lens names in sequence, rather than only confirming count ("All 3 lenses
pass the re-run test"). Example floor form (parenthetical):
`> **Pre-Phase complete.** Lenses defined and re-run verified: (1) [Lens 1 name],
(2) [Lens 2 name], (3) [Lens 3 name] -- all 3 pass the re-run test. Phase 0 opens now.`

**C-48 candidate** -- Phase-1 Open Active-Lens Echo: The Phase 1 open blockquote
names all 3 active lenses (echoing the Pre-Phase close enumeration), giving the model
an explicit attribution roster before idea generation begins. Example form:
`> **Phase 1 opens now.** Phase 0 complete. Do Nothing established.
Active lenses: (1) [Lens 1 name], (2) [Lens 2 name], (3) [Lens 3 name].`

**Interference check**: C-47 (Pre-Phase close enumeration) and C-40 (Pre-Phase double-mark)
operate on the same signal position but at different depth levels -- C-40 is a structural
presence test (is a Pre-Phase opening lifecycle tag present?) while C-47 is a content test
(does the Pre-Phase close blockquote enumerate the lens names?). Earning C-40 and C-47
simultaneously is valid. Same logic for C-48 and C-42: C-42 requires the Phase 1 open
lifecycle blockquote to exist; C-48 additionally requires it to name the active lenses.

**R19 baseline**: V-03 is the exact R18 V-04 backbone, reproduced without modification.
It carries the session-open phase roster (C-45) and session-close named ledger (C-46)
but with generic Pre-Phase close ("All 3 lenses pass") and generic Phase 1 open
("Phase 0 complete. Do Nothing established.") -- confirming the R18 V-04 ceiling is
reproducible entering R19 and that the delta between V-03 and V-01/V-02/V-04/V-05 under
hypothetical v18 is attributable solely to lens-name content in the transition signals.

---

## Variation Axes

| Axis | Description |
|------|-------------|
| Pre-Phase close lens enumeration | Whether Pre-Phase close names all 3 lenses individually (C-47 candidate) |
| Phase-1 open active-lens echo | Whether Phase 1 open echoes all 3 active lens names (C-48 candidate) |
| Lens enumeration notation | Parenthetical: (1) [name], (2) [name], (3) [name] vs. numbered list |
| Phase-1 open content depth | Lens names only vs. lens names + direction tag |
| Baseline contrast | R18 V-04 exact -- Pre-Phase close and Phase 1 open generic, no lens names |

## Single-axis variations

---

### V-01 -- Pre-Phase Close Lens Enumeration (C-47 floor candidate)

**Axis**: Pre-Phase close content enrichment (parenthetical notation)
**Hypothesis**: The R18 backbone Pre-Phase close reads `> **Pre-Phase complete.** All 3
lenses pass the re-run test. Phase 0 opens now.` -- it confirms count and passage, but
does not name the lenses. V-01 adds a parenthetical enumeration of all 3 lens names to
the Pre-Phase close blockquote, giving the model an explicit record of which lenses were
defined before Phase 0 begins. The Phase 1 open blockquote is unchanged from R18 backbone
(generic: "Phase 0 complete. Do Nothing established."). C-48 FAIL. Everything else is the
R18 V-04 backbone (all lifecycle signals, session-open phase roster, session-close named
ledger, registry, prohibitions, C-01..C-46 as inherited).

**Expected**: C-01..C-46 (inh from R18 V-04 backbone) + C-47 PASS (Pre-Phase close
enumerates lens names in parenthetical notation) + C-48 FAIL (Phase 1 open generic,
no active-lens echo) = **190** under v17. Under hypothetical v18: **192.5**
(C-47 PASS +2.5, C-48 FAIL).

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

### V-02 -- Phase-1 Open Active-Lens Echo (C-48 floor candidate)

**Axis**: Phase 1 open content enrichment (active-lens roster in parenthetical notation)
**Hypothesis**: The R18 backbone Phase 1 open reads `> **Phase 1 opens now.** Phase 0
complete. Do Nothing established.` -- it confirms Phase 0 closure and the inertia
baseline, but does not carry the lens names forward from Pre-Phase. V-02 adds an
active-lens roster to the Phase 1 open blockquote, naming all 3 lenses at the moment
the generation phase begins. The Pre-Phase close blockquote is unchanged from R18 backbone
(generic: "All 3 lenses pass the re-run test."). C-47 FAIL. Everything else is the
R18 V-04 backbone.

**Expected**: C-01..C-46 (inh from R18 V-04 backbone) + C-47 FAIL (Pre-Phase close
generic, no lens enumeration) + C-48 PASS (Phase 1 open names all 3 active lenses in
parenthetical notation) = **190** under v17. Under hypothetical v18: **192.5**
(C-47 FAIL, C-48 PASS +2.5).

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

### V-03 -- Baseline: R18 V-04 Exact Backbone (Pre-Phase close and Phase 1 open generic; no lens enumeration or echo)

**Axis**: Baseline reproduction -- confirms R18 V-04 ceiling under v17 is stable entering R19
**Hypothesis**: V-03 is the exact R18 V-04 backbone, reproduced without modification. It
carries the session-open phase roster (C-45: arrow notation) and session-close named-phase
ledger (C-46: "Phases closed: Pre-Phase (lenses), Phase 0 (inertia baseline)..."). But
the Pre-Phase close is generic ("All 3 lenses pass the re-run test.") and the Phase 1 open
is generic ("Phase 0 complete. Do Nothing established."). Neither C-47 nor C-48 is present.
This confirms the R18 V-04 ceiling (190 under v17) as the reproducible R19 entry point
and establishes the contrast baseline: the delta between V-03 and V-01/V-02/V-04/V-05
under hypothetical v18 is attributable solely to lens-name content in the Pre-Phase close
and Phase 1 open signals.

**Expected**: C-01..C-46 (inh from R18 V-04 backbone) + C-47 FAIL (Pre-Phase close
generic) + C-48 FAIL (Phase 1 open generic) = **190** under v17 (baseline).
Under hypothetical v18: **190** (both fail -- baseline contrast).

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

### V-04 -- Full Cross-Phase Lens Reference (C-47 + C-48 combined; first to 195)

**Axis**: Pre-Phase close lens enumeration (parenthetical) + Phase-1 open active-lens
echo (parenthetical)
**Hypothesis**: V-01 tests C-47 alone (Pre-Phase close names lenses; Phase 1 open generic).
V-02 tests C-48 alone (Phase 1 open echoes active lenses; Pre-Phase close generic). V-04
combines both: the Pre-Phase close blockquote enumerates all 3 lens names in parenthetical
notation (C-47 carrier), and the Phase 1 open blockquote echoes those same 3 lens names
in matching parenthetical notation (C-48 carrier). Both transition signals carry lens
names simultaneously. This is the C-47 + C-48 combination and is projected as the first
variation to reach 195 under hypothetical v18. Everything else inherits unchanged from
R18 V-04 backbone.

**Expected**: C-01..C-46 (inh from R18 V-04 backbone) + C-47 PASS (Pre-Phase close names
3 lenses, parenthetical notation) + C-48 PASS (Phase 1 open echoes same 3 lens names,
parenthetical notation) = **190** under v17. Under hypothetical v18: **195**
(C-47 PASS +2.5, C-48 PASS +2.5 -- first to 195).

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

### V-05 -- Numbered-List Lens Roster + Phase-1 Echo (alternate path to 195)

**Axis**: Pre-Phase close lens enumeration (numbered-list notation) + Phase-1 open
active-lens echo (numbered-list notation with direction tags)
**Hypothesis**: V-04 achieves C-47 via parenthetical notation in Pre-Phase close and
C-48 via matching parenthetical notation in Phase 1 open. V-05 tests alternate forms for
both signals: (a) the Pre-Phase close uses a numbered-list notation ("1. [Lens name] --
[one-word direction]") rather than inline parenthetical, making the lens enumeration a
distinct structured block rather than an inline sequence; (b) the Phase 1 open echoes
using numbered-list notation with direction tags rather than bare names alone. V-05 also
serves as a forward signal: the direction tags in Phase 1 open reinforce the lens
production constraints more explicitly than V-04's name-only echo. If a future v19 adds
C-49 ("Phase 1 open names each lens AND its direction axis"), V-05 is the carrier.

**Expected**: C-01..C-46 (inh from R18 V-04 backbone) + C-47 PASS (Pre-Phase close
enumerates lens names in numbered-list notation -- different form from V-01/V-04,
same criterion) + C-48 PASS (Phase 1 open echoes lens names with direction tags,
numbered-list notation -- richer than V-04's parenthetical-names-only) = **190** under
v17. Under hypothetical v18: **195** (C-47 PASS +2.5, C-48 PASS +2.5 -- alternate path
to 195; confirms notation form does not block C-47 and numbered-list-with-direction
satisfies C-48 floor). Under hypothetical v19 (if C-49 adds direction tag as ceiling):
**197.5** (V-05 forward-earns C-49 by direction tags; V-04 fails C-49 because
names-only echo is briefer than direction-tagged echo).

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

| Variation | v17 (max 190) | hyp v18 (+C-47/C-48) | C-47 | C-48 |
|-----------|--------------|----------------------|------|------|
| V-01 | 190 | 192.5 | PASS (parenthetical names in Pre-Phase close) | FAIL |
| V-02 | 190 | 192.5 | FAIL | PASS (parenthetical names in Phase 1 open) |
| V-03 | **190** | 190 | FAIL | FAIL (baseline) |
| V-04 | 190 | **195** | PASS (parenthetical names) | PASS (parenthetical names) |
| V-05 | 190 | **195** | PASS (numbered-list + direction tag) | PASS (numbered-list + direction tag) |

**V-04 and V-05 are the first variations projected to reach 195** (under hypothetical v18).
**V-05 additionally forward-earns a hypothetical C-49** (Phase-1 open direction-tag echo) --
if v19 sharpens C-48 the way v17 sharpened C-45 (from existence to content specificity),
V-05 is already there at 197.5.

**Key independence confirmation**: C-47 and C-48 are coordinate, not hierarchical.
- V-01 PASSES C-47 only: Pre-Phase close names lenses; Phase 1 open is unchanged (no lens echo).
- V-02 PASSES C-48 only: Phase 1 open names active lenses; Pre-Phase close is generic (no enumeration).
- V-04 and V-05 PASS both by combining the two signals independently.
- Neither criterion is a prerequisite for the other -- earning C-47 does not imply C-48
  (the Phase 1 open could still be generic) and earning C-48 does not imply C-47
  (the lens names could appear first at Phase 1 open, skipping the Pre-Phase close enumeration).

**Interference check**: C-47 (Pre-Phase close lens enumeration) and C-40 (Pre-Phase
lifecycle double-mark -- both Pre-Phase open AND close tags present) operate at the same
signal position but at different depth levels. C-40 is a structural presence test: is a
dedicated opening lifecycle tag present within Pre-Phase? C-47 is a content test: does
the Pre-Phase close blockquote enumerate the lens names? Earning C-40 + C-47 simultaneously
is valid -- C-40 verifies the open tag exists; C-47 verifies the close tag carries lens
names. All R19 variations earn C-40 (inherited from R18 V-04 backbone which carries
`*Pre-Phase opens now. No preconditions.*`). Similarly, C-48 (Phase-1 open lens echo)
and C-42 (Phase-1 lifecycle double-mark) are at different depth levels: C-42 verifies
the Phase 1 open blockquote exists; C-48 verifies it carries the active lens names.

**Forward signal -- hypothetical v19 C-49**:
V-05's direction-tagged Phase 1 open (`1. [Lens 1 name] -- [one-word direction]`) is
richer than V-04's names-only echo. If v19 adds C-49 as a content sharpener of C-48
(Phase 1 open names each lens AND its direction axis, analogous to how C-46's
echo-completion form is richer than the named-ledger floor), V-05 would score 197.5
under hypothetical v19 while V-04 would fail C-49 and remain at 195.
