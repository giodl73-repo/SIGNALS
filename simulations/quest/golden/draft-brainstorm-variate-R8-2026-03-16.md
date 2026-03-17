---
skill: quest-variate
skill_target: draft-brainstorm
round: 8
date: 2026-03-16
rubric_version: 8
r7_scores_under_v8: "V-03 = 140 (C-27 FAIL -- phase gate has no 'Selected? blank' precondition; C-28 FAIL -- prohibition only, no inversion), V-04 = 142.5 (C-27 FAIL -- Step 3 gate lacks 'Top-5? blank' schema state; C-28 PASS -- Rule 2 inversion present), V-05 = 145 (C-27 PASS -- 'Layer 4 may begin only when all 5 rows exist and Selected? is blank across all rows'; C-28 PASS -- 'if you want to edit the rationale, treat that impulse as confirmation...')"
r8_target: "145 -- achieve both C-27 (schema-gate phase-advance coupling) and C-28 (rationalization-impulse trigger inversion) in isolation and in combination"
---

# Variate R8 -- draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01 through V-02), then combinations (V-03, V-04, V-05).

R8 focuses on the two R8 aspirational criteria introduced in rubric v8:
- **C-27** Schema-Gate Phase-Advance Coupling -- C-25 is the floor (schema lock present: the
  selection-mark slot cannot be populated until all batch rows exist); C-27 is the ceiling:
  the gate must be explicitly coupled to a named phase-advance condition -- the prompt names
  the downstream phase that cannot begin AND the required schema state as a dual condition;
  "Phase 3 may begin when all 5 rows exist" satisfies C-25 but fails C-27 because the schema
  state is incomplete (Selected? blank is not named as a precondition); only when both the
  blocked phase and "all 5 rows exist AND Selected? is blank" appear as a coupled condition
  does C-27 pass
- **C-28** Rationalization-Impulse Trigger Inversion -- C-24 is the floor (post-comparison
  rationalization explicitly blocked: the prompt prohibits revising the candidate's rationale
  to manufacture a distinction); C-28 is the ceiling: the prohibition is inverted -- the
  prompt names the DESIRE to revise as a positive enforcement signal, not merely prohibiting
  acting on it; "do not revise" closes the door; "if you want to revise, treat that impulse
  as confirmation the replacement obligation applies" closes the reasoning path that leads
  to the door by converting the escape impulse into a trigger

R7 gap analysis under rubric v8:

| Variation | R7 Score (v7) | C-27 under v8 | C-28 under v8 | Score under v8 |
|-----------|--------------|---------------|---------------|----------------|
| R7-V-01 (137.5) | 137.5 | FAIL (phase gate: "Phase 3 may begin... only when all 5 rows exist" -- no "Selected? blank" precondition; C-25 pass but C-27 gap remains) | FAIL (Prohibition B: "do not revise"; no inversion clause) | 137.5 |
| R7-V-02 (137.5) | 137.5 | FAIL (prose batch; no structural column -- C-25 absent, C-27 moot) | FAIL (same prohibition language; no inversion) | 137.5 |
| R7-V-03 (140) | 140 | FAIL (Selected? gate: "Phase 3 may begin and Selected? may be filled only when all 5 rows exist" -- positive-fill framing, not dual-precondition; "Selected? blank" not named as a schema state check) | FAIL (Prohibition B: "do not revise... Rationale revision is the escape route this prohibition closes" -- closes the door, does not invert the impulse) | 140 |
| R7-V-04 (140) | 140 | FAIL ("Step 3 is gated by this section: no selection marks... before all 5 rows exist" -- names Step 3 and row-count condition, but Top-5? blank in idea table is not named as a required schema state; coupling is incomplete) | PASS (Rule 2: "if editing the Candidate's Rationale would make the comparison sentence completable, that desire confirms the substitution obligation applies" -- desire-to-edit inverted as confirmation signal) | 142.5 |
| R7-V-05 (140) | 140 | PASS ("Layer 4 may begin only when all 5 rows exist and Selected? is blank across all rows" -- names Layer 4, names both schema conditions as coupled preconditions) | PASS ("If you want to edit the rationale, treat that impulse as confirmation that the replacement obligation applies" -- impulse explicitly inverted) | 145 |

R8 axes selected:

| Axis | New in R8? | Used In | R8 Criterion |
|------|-----------|---------|--------------|
| Phrasing register: inversion clause in Rationalization Block | Yes | V-01, V-03 | C-28 (V-01 isolated; V-03 combined) |
| Lifecycle emphasis: dual-condition phase-advance gate (phase + schema state) | Yes | V-02, V-03 | C-27 (V-02 isolated; V-03 combined) |
| Output format: table architecture with Top-5? schema gate repair | Repair of R7-V-04 gap | V-04 | C-27 (minimum repair) + C-28 (inh) |
| Inertia framing: expanded status-quo baseline as cost-of-delay anchor | Yes | V-05 | Non-criterion axis; C-27+C-28 maintained from R7-V-05 |

Root cause of R7-V-03 C-27 gap: The Selected? rule reads "Phase 3 may begin and Selected?
may be filled only when all 5 rows exist." This states the positive condition for moving
forward (Selected? may be filled), not a dual precondition check (Selected? must currently
be blank AND all 5 rows present). C-27 requires the gate to name both (a) the blocked phase
and (b) the schema state that must hold -- including that Selected? is blank across all rows
before the gate opens. "May be filled when..." is a permission statement; "may begin only
when all 5 rows exist AND Selected? is blank across all rows" is the required coupled
precondition.

Root cause of R7-V-04 C-27 gap: The Batch Registry in V-04 does not have a Selected?
column -- the selection marker (Top-5?) lives in the idea table. The gate reads "Step 3 is
gated by this section: no selection marks before all 5 rows exist." This names Step 3 and
the row-count condition, but the schema state "Top-5? blank across all rows of the idea
table" is not named as a required precondition. C-27 requires both the blocked phase AND
the required schema state to be named as a coupled condition. The fix: "Step 3 may begin
only when (a) all 5 rows of this Registry are written AND (b) Top-5? is blank across all
rows of the idea table."

---

## V-01 -- Phrasing Register: C-28 Trigger Inversion (C-27 absent -- isolated)

**Axis**: Phrasing register -- Prohibition B is restructured to include an explicit
inversion clause: the desire to revise the candidate's rationale is named as a positive
confirmation signal that the replacement obligation applies, not merely as a prohibited
action; the escape-route reasoning path is closed, not just the door; C-27 is intentionally
absent (Selected? gate retains the positive-fill framing without the dual precondition)
**Base**: R7-V-03 (Prohibition Battery + schema Registry + distribution-shift, 140 under v7)
**Hypothesis**: R7-V-03 passes C-24 via "Rationale revision is the escape route this
prohibition closes" -- the door is closed. C-28 requires inversion: the impulse to revise
must be named as a trigger. V-01 adds precisely that inversion to Prohibition B while
leaving the Selected? gate unchanged ("Phase 3 may begin... only when all 5 rows exist" --
no dual precondition, C-27 intentionally fails). If V-01 scores 142.5, the inversion clause
alone contributes 2.5 points independently of C-27.

**Expected**: C-01..C-26 PASS (inh) + C-27 FAIL (Selected? gate: positive-fill only, no
"Selected? blank" dual precondition) + C-28 PASS (Prohibition B: inversion clause present)
= **142.5**

---

```
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

**Do not mark top-5 yet.** Complete the full pool across all sections before
selecting. Marking ideas as you write them introduces sequential bias -- the first
ideas generated are not the best, only the most recently visible.

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
and describe what changes. Do not finalize yet.

---

## PHASE 2 -- VERIFY

Before writing the final artifact, complete all 4 checks in order. Each check is
explicitly connected to a downstream output decision -- do not skip.

**Check A -- Sequential Default** (determines candidates for Check B)
Look at the 5 ideas you are considering for top-5. Are they the first 5 ideas
you generated? If yes, rescan the full pool -- the best ideas are rarely the
first ones written. The output of Check A is the set of 5 candidates advancing
to Check B.

**Check B -- Top-5 Defensibility** (determines final top-5 marks)

For each of the 5 candidates from Check A, write one row in the Peer-Comparison
Registry. Do not fill in the Selected? column during Registry construction.

| # | Candidate (exact name from pool) | Peer (exact name, same ## section, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|----------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Column rules:**
- **Candidate**: exact idea name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same `##` section; cannot be blank
- **"I chose ... because ___"**: complete the sentence -- state a specific reason
  tied to {{topic}}'s actual constraints (scope, user group, cost, risk); "it is
  better" or "more viable" do not count
- **Selected?**: This column is structurally null throughout Registry construction.
  The Selected? column cannot hold any value until all 5 rows of this Registry are
  complete. A Registry with fewer than 5 rows has no valid Selected? entries -- this
  is a schema constraint of the Registry, not a deferred choice. Phase 3 may begin
  and Selected? may be populated only when all 5 rows exist in your output.

**Prohibition Battery -- two prohibitions govern Check B and apply without exception:**

**Prohibition A -- Marking Ban**: Do not place any `**` marks anywhere in your
output while Check B is in progress -- not on headings, inline, in notes, or in any
other form. The marking action is what is prohibited, not merely deferred. No `**`
marks may appear until the complete 5-row Registry is written in your output.

**Prohibition B -- Rationalization Block**: If you cannot complete the sentence
for any row -- no specific peer or no specific reason holds -- that candidate must
be replaced by the specific peer you attempted to name in the Peer column. The
replacement source is fixed: it is the peer from this row, not a different idea
selected after reconsidering. Do not revise the candidate's rationale after Check B
to manufacture a distinction that was not present at comparison time. If you want to
revise the rationale, treat that impulse as confirmation that the replacement
obligation applies -- the desire to revise is not permission to reopen the
comparison, it is evidence the swap is mandatory.

**Check C -- AMEND Distribution-Shift Test** (determines final AMEND content)

Each AMEND directive must pass the distribution-shift test: re-running this
brainstorm with only this directive must surface candidate ideas that would not
have appeared in the original pool -- different ideas, not different labels on
the same ideas. A directive is valid only if the underlying candidate set changes.
A directive that shifts only category names, framing emphasis, or grouping taxonomy
without introducing different underlying candidates fails this test.

For each of your 3 AMEND items, ask: would re-running with this directive produce
ideas that do not appear in the current pool? If the answer is "probably the same
ideas under a different frame," sharpen the directive. The output of Check C
determines final AMEND content.

**Check D -- Inertia Paragraph** (gates artifact write)
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. This check gates the artifact write.

---

## PHASE 3 -- FINALIZE

Fill Selected? = YES in exactly 5 rows of the Registry (candidates confirmed by
Check B, with any substitutions from Prohibition B applied). Mark those same 5
ideas with `**` on their headings in the dimension sections. Update AMEND items
if Check C required changes.

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
then Peer-Comparison Registry, then AMEND. Total ideas (including Do Nothing): 20-40.
```

---

## V-02 -- Lifecycle Emphasis: C-27 Phase-Advance Coupling (C-28 absent -- isolated)

**Axis**: Lifecycle emphasis -- the Selected? gate is restructured as an explicit
dual-condition phase-advance lock: Phase 3 is named as the blocked phase AND the required
schema state is stated as a coupled dual precondition: "all 5 rows exist AND Selected?
is blank across all rows"; C-28 is intentionally absent (Rationalization Block retains
the standard prohibition without the inversion clause)
**Base**: R7-V-03 (140 under v7)
**Hypothesis**: R7-V-03's Selected? rule reads "Phase 3 may begin and Selected? may be
filled only when all 5 rows exist" -- this names Phase 3 and the row-count condition, but
Selected? blank is not stated as a required precondition; it is named as a permission to
fill, not a state that must hold before the gate opens. V-02 replaces this with an explicit
dual-condition lock: "Phase 3 may begin only when (a) all 5 rows exist in your output AND
(b) Selected? is blank across all 5 rows -- both conditions must hold simultaneously." This
is the minimum change to achieve C-27. C-28 is intentionally omitted; Prohibition B retains
"do not revise" without the inversion. If V-02 scores 142.5, the dual-condition gate alone
contributes 2.5 points independently of C-28.

**Expected**: C-01..C-26 PASS (inh) + C-27 PASS (Selected? dual-condition phase lock:
"Phase 3 may begin only when all 5 rows exist AND Selected? is blank across all rows")
+ C-28 FAIL (Prohibition B: "do not revise" prohibition; no inversion clause)
= **142.5**

---

```
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

**Do not mark top-5 yet.** Complete the full pool across all sections before
selecting. Marking ideas as you write them introduces sequential bias -- the first
ideas generated are not the best, only the most recently visible.

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
and describe what changes. Do not finalize yet.

---

## PHASE 2 -- VERIFY

Before writing the final artifact, complete all 4 checks in order. Each check is
explicitly connected to a downstream output decision -- do not skip.

**Check A -- Sequential Default** (determines candidates for Check B)
Look at the 5 ideas you are considering for top-5. Are they the first 5 ideas
you generated? If yes, rescan the full pool -- the best ideas are rarely the
first ones written. The output of Check A is the set of 5 candidates advancing
to Check B.

**Check B -- Top-5 Defensibility** (determines final top-5 marks)

For each of the 5 candidates from Check A, write one row in the Peer-Comparison
Registry. Do not fill in the Selected? column during Registry construction.

| # | Candidate (exact name from pool) | Peer (exact name, same ## section, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|----------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Column rules:**
- **Candidate**: exact idea name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same `##` section; cannot be blank
- **"I chose ... because ___"**: complete the sentence -- state a specific reason
  tied to {{topic}}'s actual constraints (scope, user group, cost, risk); "it is
  better" or "more viable" do not count
- **Selected?**: Phase-advance gate. This column cannot hold any value, and Phase 3
  cannot begin, until both preconditions hold simultaneously: (a) all 5 rows of this
  Registry are written in your output, AND (b) Selected? is blank across all 5 rows.
  A partial Registry has no valid Selected? entries. A Registry where any Selected?
  cell holds a preliminary value does not satisfy this gate. Phase 3 may begin only
  when the Registry is both structurally complete (5 rows present) and selection-clean
  (Selected? blank in every row). This is a schema property of the Registry.

**Prohibition Battery -- two prohibitions govern Check B and apply without exception:**

**Prohibition A -- Marking Ban**: Do not place any `**` marks anywhere in your
output while Check B is in progress -- not on headings, inline, in notes, or in any
other form. The marking action is what is prohibited, not merely deferred. No `**`
marks may appear until the complete 5-row Registry is written in your output.

**Prohibition B -- Rationalization Block**: If you cannot complete the sentence
for any row -- no specific peer or no specific reason holds -- that candidate must
be replaced by the specific peer you attempted to name in the Peer column. The
replacement source is fixed: it is the peer from this row, not a different idea
selected after reconsidering. Do not revise the candidate's rationale after Check B
to manufacture a distinction that was not present at comparison time. Rationale
revision is the escape route this prohibition closes.

**Check C -- AMEND Distribution-Shift Test** (determines final AMEND content)

Each AMEND directive must pass the distribution-shift test: re-running this
brainstorm with only this directive must surface candidate ideas that would not
have appeared in the original pool -- different ideas, not different labels on
the same ideas. A directive is valid only if the underlying candidate set changes.
A directive that shifts only category names, framing emphasis, or grouping taxonomy
without introducing different underlying candidates fails this test.

For each of your 3 AMEND items, ask: would re-running with this directive produce
ideas that do not appear in the current pool? If the answer is "probably the same
ideas under a different frame," sharpen the directive. The output of Check C
determines final AMEND content.

**Check D -- Inertia Paragraph** (gates artifact write)
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. This check gates the artifact write.

---

## PHASE 3 -- FINALIZE

Fill Selected? = YES in exactly 5 rows of the Registry (candidates confirmed by
Check B, with any substitutions from Prohibition B applied). Mark those same 5
ideas with `**` on their headings in the dimension sections. Update AMEND items
if Check C required changes.

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
then Peer-Comparison Registry, then AMEND. Total ideas (including Do Nothing): 20-40.
```

---

## V-03 -- Lifecycle Emphasis + Phrasing Register: C-27 + C-28 Combined (Prohibition Battery base)

**Axes**: Lifecycle emphasis (dual-condition phase-advance gate from V-02, C-27) + phrasing
register (inversion clause from V-01, C-28); compact Prohibition Battery architecture
preserved; V-01 and V-02 combined into a single variation on the R7-V-03 base
**Base**: R7-V-03 (140 under v8 -- C-27/C-28 absent)
**Hypothesis**: V-01 confirms C-28 at +2.5 and V-02 confirms C-27 at +2.5 independently.
V-03 combines both on the same compact base: Selected? gate becomes the dual-condition
phase lock (C-27) and Prohibition B gains the inversion clause (C-28). The Prohibition
Battery is preserved as the named constraint block within Check B. If both pass together,
V-03 should score 145.

**Expected**: C-01..C-26 PASS (inh) + C-27 PASS (Selected? dual-condition: "Phase 3 may
begin only when all 5 rows exist AND Selected? is blank across all rows") + C-28 PASS
(Prohibition B: inversion clause -- desire to revise = confirmation the swap applies)
= **145**

---

```
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

**Do not mark top-5 yet.** Complete the full pool across all sections before
selecting. Marking ideas as you write them introduces sequential bias -- the first
ideas generated are not the best, only the most recently visible.

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
and describe what changes. Do not finalize yet.

---

## PHASE 2 -- VERIFY

Before writing the final artifact, complete all 4 checks in order. Each check is
explicitly connected to a downstream output decision -- do not skip.

**Check A -- Sequential Default** (determines candidates for Check B)
Look at the 5 ideas you are considering for top-5. Are they the first 5 ideas
you generated? If yes, rescan the full pool -- the best ideas are rarely the
first ones written. The output of Check A is the set of 5 candidates advancing
to Check B.

**Check B -- Top-5 Defensibility** (determines final top-5 marks)

For each of the 5 candidates from Check A, write one row in the Peer-Comparison
Registry. Do not fill in the Selected? column during Registry construction.

| # | Candidate (exact name from pool) | Peer (exact name, same ## section, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|----------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Column rules:**
- **Candidate**: exact idea name from Phase 1b; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same `##` section; cannot be blank
- **"I chose ... because ___"**: complete the sentence -- state a specific reason
  tied to {{topic}}'s actual constraints (scope, user group, cost, risk); "it is
  better" or "more viable" do not count
- **Selected?**: Phase-advance gate. This column cannot hold any value, and Phase 3
  cannot begin, until both preconditions hold simultaneously: (a) all 5 rows of this
  Registry are written in your output, AND (b) Selected? is blank across all 5 rows.
  A partial Registry has no valid Selected? entries. A Registry where any Selected?
  cell carries a preliminary value does not satisfy the gate. Phase 3 may begin only
  when the Registry is both structurally complete (5 rows) and selection-clean
  (Selected? blank in every row). This is a schema property of the Registry.

**Prohibition Battery -- two prohibitions govern Check B and apply without exception:**

**Prohibition A -- Marking Ban**: Do not place any `**` marks anywhere in your
output while Check B is in progress -- not on headings, inline, in notes, or in any
other form. The marking action is what is prohibited, not merely deferred. No `**`
marks may appear until the complete 5-row Registry is written in your output.

**Prohibition B -- Rationalization Block**: If you cannot complete the sentence
for any row -- no specific peer or no specific reason holds -- that candidate must
be replaced by the specific peer you attempted to name in the Peer column. The
replacement source is fixed: it is the peer from this row, not a different idea
selected after reconsidering. Do not revise the candidate's rationale after Check B
to manufacture a distinction that was not present at comparison time. If you want
to revise the rationale, treat that impulse as confirmation that the replacement
obligation applies -- the desire to revise is not permission to reopen the
comparison; it is evidence the swap is mandatory.

**Check C -- AMEND Distribution-Shift Test** (determines final AMEND content)

Each AMEND directive must pass the distribution-shift test: re-running this
brainstorm with only this directive must surface candidate ideas that would not
have appeared in the original pool -- different ideas, not different labels on
the same ideas. A directive is valid only if the underlying candidate set changes.
A directive that shifts only category names, framing emphasis, or grouping taxonomy
without introducing different underlying candidates fails this test.

For each of your 3 AMEND items, ask: would re-running with this directive produce
ideas that do not appear in the current pool? If the answer is "probably the same
ideas under a different frame," sharpen the directive. The output of Check C
determines final AMEND content.

**Check D -- Inertia Paragraph** (gates artifact write)
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. This check gates the artifact write.

---

## PHASE 3 -- FINALIZE

Fill Selected? = YES in exactly 5 rows of the Registry (candidates confirmed by
Check B, with any substitutions from Prohibition B applied). Mark those same 5
ideas with `**` on their headings in the dimension sections. Update AMEND items
if Check C required changes.

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
then Peer-Comparison Registry, then AMEND. Total ideas (including Do Nothing): 20-40.
```

---

## V-04 -- Output Format: Table Architecture + C-27 Repair (C-28 inherited from R7-V-04 Rule 2)

**Axis**: Output format -- table architecture with Top-5? column in idea table + Batch
Registry; minimum-viable repair of R7-V-04's C-27 gap: Step 3 gate updated to name both
the blocked step AND the dual schema state (all 5 Batch Registry rows + Top-5? blank across
all idea table rows); C-28 is inherited from R7-V-04 Rule 2 which already inverts the
rationalization impulse
**Base**: R7-V-04 (142.5 under v8 -- C-27 FAIL, C-28 PASS via Rule 2)
**Hypothesis**: R7-V-04 already scores 142.5 under v8 (C-27 FAIL: Step 3 gate names row
count but not "Top-5? blank" schema state; C-28 PASS: Rule 2 "that desire confirms the
substitution obligation applies"). The only change needed is to repair the Step 3 gate:
"Step 3 may begin only when (a) all 5 rows of this Registry are written AND (b) Top-5?
is blank across all rows of the idea table." This names Step 3 as blocked and the dual
schema state as precondition. This is the minimum viable change to reach 145.

**Expected**: C-01..C-26 PASS (inh) + C-27 PASS (Step 3 gate: "all 5 Registry rows AND
Top-5? blank in idea table") + C-28 PASS (inh from R7-V-04 Rule 2 inversion) = **145**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

---

### Preamble: Inertia Frame

Before generating any ideas, write a paragraph (3-5 sentences) describing the
current trajectory for {{topic}}: What happens if the team makes no deliberate
decision? What is already in motion? What does the path of least resistance produce?

This paragraph must appear before the idea table in the final artifact.

---

### Step 1 -- Build the Idea Table

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
- **Top-5?**: Leave this column **blank during Step 1.** The Top-5? column will
  be filled only after the Pre-Selection Batch Registry (Step 2b) is fully complete
  and its gate conditions are satisfied. Marking during construction introduces
  sequential bias.

Required row: **Do Nothing** with Dimension = `Status Quo`. Its Rationale must
describe what the current trajectory from the Preamble produces -- not "doing
nothing is an option."

Volume: 20-40 rows total.

---

### Step 2 -- Self-Review Phase

Before filling in the Top-5? column, run the following reviews. Each review
feeds a named downstream output decision -- do not skip.

**Review A -- Sequential Default** (determines candidates for Step 2b)
Look at rows 1-5. Are you planning to mark these because they are the strongest
rows, or because they are the first? The output of this review is the set of 5
candidates that advance to the Pre-Selection Batch Registry.

**Review B -- AMEND Distribution-Shift** (determines AMEND content in Step 5)
For each of your 3 AMEND directives, apply the distribution-shift test: if a
reader took only this directive and re-ran the brainstorm, would the resulting
table contain candidate ideas that do not appear in the current table? The test
is whether different ideas enter the pool -- not whether the same ideas appear
under different labels, different Dimension headings, or different framing emphasis.
A directive that shifts only category taxonomy or presentation without introducing
new candidate ideas fails this test. If any directive fails, sharpen it until
re-running produces a materially different candidate set. This review determines
final AMEND content.

**Review C -- Dimension Coverage** (determines table completeness)
Do your Dimension values cover all 7 required dimension types? If any required
type is missing, add rows before proceeding to Step 2b.

---

### Step 2b -- Pre-Selection Batch Registry (required output; gates Step 3)

**Marking ban**: Do not place any `**YES**` values, `**` marks, or any other
selection notation -- in the Top-5? column, on row headings, or anywhere else in
your output -- until this entire Registry is written. The marking action is
prohibited until all 5 rows of this Registry are complete.

For each of the 5 candidates from Review A, complete one row:

| # | Candidate (exact Name from table) | Attempted Peer (same Dimension, unmarked) | "I chose [Candidate] over [Peer] because ___" |
|---|----------------------------------|------------------------------------------|-----------------------------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

Column rules:
- **Candidate**: exact Name from the idea table; must be one of the 5 from Review A
- **Attempted Peer**: exact Name of one specific unmarked row in the same Dimension;
  must exist as a row in the table; cannot be blank
- **"I chose ... because ___"**: complete the sentence -- state a specific reason
  tied to {{topic}}'s actual constraints (scope, user group, cost, risk profile);
  "it is better" or "more viable" do not count

**Step 3 Phase-Advance Gate**: Step 3 may begin only when both preconditions hold
simultaneously: (a) all 5 rows of this Registry are written in your output, AND
(b) Top-5? is blank across all rows of the idea table above. A partial Registry
does not satisfy condition (a). Any preliminary Top-5? value in the idea table
does not satisfy condition (b). Both conditions must hold before Step 3 is
permitted to start. This is a structural gate on Step 3, not a deferred reminder.

**If the sentence column cannot be completed** with a specific reason for any row,
apply the following two rules:

**Rule 1 -- Source Lock**: The `**YES**` mark for that candidate must go to the
idea named in the Attempted Peer column of that row. The replacement source is
fixed: it is the Attempted Peer from this row -- not a different idea you prefer
after reconsidering, not the next most viable from another Dimension. The Attempted
Peer named here is the only permissible replacement source.

**Rule 2 -- Rationalization Block**: Do not revise the original Candidate row's
Rationale field in the idea table after completing the Registry. Once a Registry
row is written, the comparison is final on the Rationale as it exists. If editing
the Candidate's Rationale would make the comparison sentence completable, that
desire confirms the substitution obligation applies -- the impulse to revise is
not an exit; it is confirmation the swap is mandatory. No post-Registry Rationale
edits are permitted as a mechanism to avoid a mandated substitution.

This Registry is required output. The artifact is incomplete without all 5 rows.

---

### Step 3 -- Mark Top-5 (gated by Step 2b completion and idea table state)

Only after both Step 2b gate conditions are satisfied: fill in `**YES**` in
exactly 5 rows' Top-5? column, using the candidates confirmed in the Registry.
If any substitution was required in Step 2b, the substituted peer's row receives
the `**YES**` mark.

---

### Step 4 -- Category View (required structural output; output of Review C)

After the table and Registry, produce a Category View grouping ideas under their
Dimension names. Each Dimension that appeared in the table must have its own
`## [Dimension Name]` section. This is required structural output -- a flat list fails.

```
## [Dimension Name]

- **[Idea Name]** -- [Pitch]  [**TOP-5**] (if marked)
```

---

### Step 5 -- AMEND (output of Review B)

Write an AMEND section with exactly 3 adjustments, incorporating any sharpening
from Review B. Each must meet all three conditions:
(a) names a specific shift axis,
(b) describes which rows enter, exit, or re-rank and why the pool looks different,
(c) is re-invocable with a distribution-shift guarantee -- re-running with this
    directive must surface candidate ideas that would not appear in the original
    table; different ideas, not different labels on the same ideas.

```
## AMEND

1. **[Direction label]** -- [Rows that enter, exit, or re-rank. Why the candidate
   set is different -- not just the framing. Re-runnable with this directive alone.]
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

Artifact order: Preamble paragraph, idea table, Pre-Selection Batch Registry,
Category View, AMEND.
```

---

## V-05 -- Role Sequence + Inertia Framing: Layered Architecture with Cost-of-Delay Baseline (C-27+C-28 maintained)

**Axes**: Role sequence (7-layer architecture; Layer 0 expanded as mandatory cost-of-delay
baseline that every alternative must address explicitly) + inertia framing (Status Quo
is introduced as a live calibrated competitor with a named "trajectory cost" that anchors
the pool, not a checkbox entry); C-27 and C-28 from R7-V-05 are structurally preserved
**Base**: R7-V-05 (145 under v8 -- both C-27 and C-28 pass)
**Hypothesis**: R7-V-05 already achieves 145. V-05 explores whether the inertia-framing
axis can shift output quality: by requiring the model to characterize the status quo as
a "trajectory cost" before generating alternatives, every idea is implicitly competing
against a named baseline rather than against an abstract "do nothing" checkbox. The new
role-sequence axis: Layer 0 now produces a named trajectory cost (e.g., technical debt
rate, user-friction accumulation, competitive gap widening) that each idea in Layer 1
must reference. This is not a new criterion; it tests whether expanded inertia framing
produces more specific rationales (C-07) and a more defensible top-5 (C-10) without
introducing any regressions. C-27 and C-28 are maintained verbatim from R7-V-05.

**Expected**: All 28 criteria pass; no regressions from R7-V-05; C-27 PASS (inh) +
C-28 PASS (inh) = **145**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

Your task: map the full option space across 7 required dimensions, then select the
5 most viable candidates through a gated verification process. Do not finalize the
artifact until all verification gates are passed.

---

## Layer 0 -- Status Quo Baseline (trajectory cost)

Before opening any dimension, characterize the current state of {{topic}} with
enough specificity that a reader could measure whether an alternative is better.

Write a paragraph (3-5 sentences) that answers:
- What is in motion today for {{topic}}? What compounds by default?
- What is the trajectory cost -- the specific technical, organizational, or user
  burden that accumulates if the team makes no explicit decision?
- What does the team concretely give up by staying the course for the next quarter?

Name the trajectory cost explicitly (e.g., "debt rate", "coverage gap", "friction
accumulation", "competitive lag"). This named cost becomes the calibration anchor
for Layer 1: every idea must be better than doing nothing on at least one dimension
of this cost. Label the trajectory cost you name with the tag [TRAJECTORY COST: ___].

This paragraph is the baseline against which every alternative is measured. It must
appear first in the final artifact, before any alternatives.

---

## Layer 1 -- Idea Generation

Generate ideas across the following 7 required dimensions. Each dimension must
produce at least 3 ideas (Status Quo: exactly 1). Label each section with the exact
dimension name as a `##` header.

**Do not mark any idea with `**` in this layer.** The selection gate is Layer 3.
Do not mark as you generate -- finish every dimension first. Marking during
generation introduces sequential bias: ideas written first are most available,
not necessarily strongest.

**Dimension 1 -- Scope**: Ideas vary how much of {{topic}}'s problem space is
addressed -- from the minimal viable slice to the comprehensive overhaul. For each
idea, note which part of the [TRAJECTORY COST] it reduces.

**Dimension 2 -- Timing**: Ideas vary when intervention happens -- early bets,
staged rollouts, deferred commitments, just-in-time decisions. For each idea, note
whether it arrests the [TRAJECTORY COST] early or accepts some accumulation.

**Dimension 3 -- Integration**: Ideas vary how the solution connects to existing
systems, platforms, or external dependencies relevant to {{topic}}.

**Dimension 4 -- Audience**: Ideas vary who the primary beneficiary is -- different
user segments, internal teams, or downstream consumers of {{topic}}'s output.

**Dimension 5 -- Build vs. Buy**: Ideas vary how capability is acquired -- built
internally, adopted from outside, extended from existing components, or delegated.

**Dimension 6 -- Risk Profile**: Ideas vary how much uncertainty is accepted --
conservative incremental bets vs. high-variance, high-ceiling bets. For each idea,
note where on the [TRAJECTORY COST] the risk concentrates.

**Dimension 7 -- Status Quo (mandatory)**: Contains exactly one idea: **Do Nothing**.
Its pitch and rationale must describe the trajectory from Layer 0 in concrete terms:
what the team inherits next quarter if no action is taken on {{topic}}. The rationale
is not "doing nothing is an option" -- it is the full articulation of the [TRAJECTORY
COST] as the outcome of this choice.

For each idea:

```
## [Dimension Name]

### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this specifically serves {{topic}} -- name a real constraint,
user need, or opportunity. Must be topic-specific, not generic.
```

Total ideas across all 7 dimensions: 20-40.

---

## Layer 2 -- AMEND Draft

Write a draft AMEND section with 3 pool-shift directions. Label each direction and
describe what would change in the pool. Do not finalize -- Layer 3 will verify
re-invocability before AMEND is written into the artifact.

---

## Layer 3 -- Verification Gate

Run all four checks in order before placing any top-5 marks or finalizing AMEND.
Each check is explicitly connected to a downstream output decision -- do not skip.

**Check A -- Sequential Default** (determines which candidates enter Check B)
Identify the 5 ideas you are considering for top-5. Are they the first 5 you
generated? If yes, rescan the full pool. The strongest ideas may appear in any
dimension, not just the first sections. The output of Check A is the 5 candidates
that advance to Check B.

**Check B -- Peer-Comparison Verification Registry** (determines final top-5 marks;
governed by two named rules below)

For each of the 5 candidates from Check A, write one row in the Verification Registry.
Do not fill in the Selected? column during Registry construction.

| # | Candidate (exact name from pool) | Peer (exact name, same dimension, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|---------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Column rules:**
- **Candidate**: exact idea name from Layer 1; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same `##` section;
  must exist in the pool; cannot be blank
- **"I chose ... because ___"**: complete the sentence -- state a specific reason
  tied to {{topic}}'s actual constraints (scope, execution risk, user benefit,
  ownership path); "it is better" or "more viable" do not count
- **Selected?**: Structural phase-advance gate. This column cannot hold any value,
  and Layer 4 cannot begin, until both preconditions hold simultaneously:
  (a) all 5 rows of this Registry are written in your output, AND
  (b) Selected? is blank across all 5 rows.
  A Registry with fewer than 5 rows does not satisfy condition (a). Any preliminary
  Selected? value inserted before all 5 rows exist does not satisfy condition (b).
  Layer 4 may begin only when the Registry is structurally complete (5 rows present)
  and selection-clean (Selected? blank in every row). This is a property of the
  Registry schema, not a deferred instruction.

**The following two rules govern Check B and apply without exception:**

**Marking Prohibition**: No `**` marks may appear anywhere in your output until
all five Registry rows are written. The marking action is prohibited -- not
deferred row by row. This prohibition covers `**` in headings, inline marks, and
any other notation that indicates selection. Layer 4 begins only when all five rows
are present in your output.

**Rationalization Prohibition**: If you cannot complete the sentence for any
candidate -- no specific peer comes to mind or no specific reason holds -- that
candidate must be replaced with the specific peer you attempted to name in the
Peer column for that row. The replacement source is fixed: it is the peer from
this row, not a different idea you prefer after reconsidering the pool. Do not
revise the candidate's rationale after Check B to manufacture a distinction that
was not present at comparison time. If you want to edit the rationale, treat that
impulse as confirmation that the replacement obligation applies -- the desire to
revise is not permission to reopen the comparison; it is evidence the swap is
mandatory.

**Check C -- AMEND Distribution-Shift Test** (determines final AMEND content)
For each AMEND item: if a reader took only that directive and re-ran this brainstorm,
would they get a noticeably different pool? The bar is a different candidate
distribution, not different labels on the same ideas. Re-running with the directive
must surface candidate ideas that would not have appeared in the original pool --
new ideas enter, or existing ideas are clearly displaced by ideas that were absent.
A directive that changes only framing emphasis, category naming, or grouping taxonomy
without shifting which underlying ideas appear fails this test. Sharpen any item
that fails. The output of Check C determines final AMEND content.

**Check D -- Artifact Order** (gates the final write)
Does the Layer 0 paragraph appear before the first idea in the artifact? Confirm.
This check gates the artifact write.

---

## Layer 4 -- Finalize

Only after both Layer 3 gate conditions are satisfied (all 5 Registry rows written
AND Selected? blank across all rows):

**Top-5**: Fill Selected? = YES in exactly 5 rows of the Verification Registry
(candidates confirmed in Check B, with any substitutions applied). Mark those same
5 ideas with `**` on their headings in the dimension sections.

**AMEND**: Write the AMEND section with exactly 3 adjustments updated from Layer 2
based on Check C. Each item must: (a) name a specific shift axis, (b) describe
which ideas enter, exit, or re-rank and why the pool looks different, (c) be
re-invocable with a distribution-shift guarantee -- different ideas must appear,
not the same ideas under a different frame.

```
## AMEND

1. **[Direction]** -- [Ideas that enter or exit. Pool is different because ___. Re-invocable.]
2. **[Direction]** -- [...]
3. **[Direction]** -- [...]
```

**Artifact**: Save to `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Layer 0 paragraph (with [TRAJECTORY COST] named) -> 7 dimension
sections (top-5 marked) -> Verification Registry -> AMEND.
Total ideas (including Do Nothing): 20-40.
```

---

## Rubric Coverage Analysis -- R8

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 volume (20-40) | "20-40 candidates" | same (inh) | same (inh) | "20-40 rows total" | "20-40" |
| C-02 idea anatomy | Per-idea block (4 fields) | same (inh) | same (inh) | Table columns (Name/Pitch/Dimension/Rationale) | Per-idea block |
| C-03 top-5 marker | `**` heading prefix (Phase 3) + Selected?=YES | same (inh) | same (inh) | `**YES**` in Top-5? col (Step 3) | `**` heading + Selected?=YES |
| C-04 inertia check | Status Quo required section + trajectory rationale | same (inh) | same (inh) | Status Quo row + Preamble | Dim 7 mandatory + Layer 0 |
| C-05 AMEND (3 items) | 1c draft + Check C | same (inh) | same (inh) | Step 5 output of Review B | Layer 2 draft + Check C |
| C-06 category grouping | Required `##` sections per dimension | same (inh) | same (inh) | Category View (Step 4, required structural output) | 7 dimension `##` headers |
| C-07 rationale specificity | "cite real constraint; no generic reasoning" | same (inh) | same (inh) | "cite specific constraint" | "name real constraint; topic-specific" + trajectory-cost anchor |
| C-08 category diversity | 6 required dimensions | same (inh) | same (inh) | 7 required dimension types | 7 named dimensions |
| C-09 AMEND actionability | Check C distribution-shift test | same (inh) | same (inh) | Review B + Step 5 distribution-shift | Check C distribution-shift |
| C-10 top-5 defensibility | Check A + Registry + batch gate | same (inh) | same (inh) | Review A + Registry + Rules 1/2 | Check A + Verification Registry |
| C-11 sequential-default guard | "Do not mark top-5 yet" + Phase 1b imperative | same (inh) | same (inh) | "Leave Top-5? blank during Step 1" | "Do not mark any idea... in this layer" |
| C-12 re-runnability bar | Check C distribution-shift (exceeds C-12) | same (inh) | same (inh) | Review B + Step 5 distribution-shift | Check C distribution-shift |
| C-13 category dimension taxonomy | 6 named dimensions with descriptions | same (inh) | same (inh) | 7 named dimension types | 7 named dimensions with descriptions |
| C-14 inertia-first framing paragraph | 1a: "appears at top... precedes all ideas" | same (inh) | same (inh) | Preamble: "must appear before the idea table" | Layer 0: "must appear first" |
| C-15 structural spine guarantee | PASS: 6 required `##` sections; "do not collapse; do not omit" | same (inh) | same (inh) | PASS: Category View "required structural output" | PASS: 7 dimension `##` headers mandated |
| C-16 generation-phase sequential guard | PASS: "Do not mark top-5 yet" in Phase 1b, imperative | same (inh) | same (inh) | PASS: "Leave Top-5? blank during Step 1" -- construction phase | PASS: "Do not mark any idea with `**` in this layer" -- Layer 1 |
| C-17 peer-comparison defensibility test | PASS: Registry "I chose [Candidate] over [Peer] because ___" column | same (inh) | same (inh) | PASS: Registry "I chose [Candidate] over [Peer] because ___" | PASS: Registry sentence column |
| C-18 self-review phase integration | PASS: Check A -> Registry; Registry -> Phase 3; Check C -> AMEND; Check D -> artifact | same (inh) | same (inh) | PASS: Review A -> Step 2b; Review B -> Step 5; Step 2b -> Step 3 | PASS: Check A -> Check B; Check B -> Layer 4; Check C -> AMEND; Check D -> gates write |
| C-19 peer-test imperative form | PASS: Registry row completion enforces sentence materialization | same (inh) | same (inh) | PASS: Registry row completion | PASS: Registry row completion |
| C-20 peer-test consequence clause | PASS: Prohibition B: "must be replaced by the specific peer" | same (inh) | same (inh) | PASS: Rule 1: "`**YES**` mark must go to Attempted Peer" | PASS: "must be replaced with the specific peer" |
| C-21 peer-test batch-completion gate | PASS: "Phase 3 may begin... only when all 5 rows exist" | PASS: "Phase 3 may begin only when... (a) all 5 rows... AND (b) Selected? blank" | PASS: same as V-02 | PASS: "Step 3 may begin only when (a) all 5 rows... AND (b) Top-5? blank" | PASS: "Layer 4 may begin only when all 5 rows exist and Selected? is blank" |
| C-22 consequence replacement source | PASS: Prohibition B: "peer from this row, not a different idea" | same (inh) | same (inh) | PASS: Rule 1: "Attempted Peer from this row -- not a different idea after reconsidering" | PASS: "peer from this row, not a different idea you prefer after reconsidering" |
| C-23 selection-phase marking prohibition | PASS: Prohibition A: "The marking action is what is prohibited, not merely deferred" | same (inh) | same (inh) | PASS: "The marking action is prohibited until all 5 rows are complete" | PASS: "The marking action is prohibited -- not deferred row by row" |
| C-24 post-comparison rationalization block | PASS: Prohibition B: "Do not revise the candidate's rationale... Rationale revision is the escape route this prohibition closes" | PASS (inh): same Prohibition B language | PASS: Prohibition B (both door closed + inversion) | PASS: Rule 2: "Once a Registry row is written, the comparison is final on the Rationale as it exists" | PASS: "Do not revise the candidate's rationale after Check B to manufacture a distinction" |
| **C-25 marking-gate schema lock** | **PASS** (inh): Selected? "cannot hold any value until all 5 rows complete -- schema constraint of the Registry" | **PASS** (inh): "Phase-advance gate. This column cannot hold any value... a schema property of the Registry" | **PASS**: same as V-02 | **PASS** (inh): Top-5? column gated by Step 2b -- "Step 3 may begin only when... (a) all 5 rows written AND (b) Top-5? blank" | **PASS** (inh): Selected? "Structural phase-advance gate... a property of the Registry schema" |
| **C-26 AMEND pool-composition constraint** | **PASS** (inh): Check C: "different ideas, not different labels on the same ideas" | **PASS** (inh): same Check C language | **PASS** (inh): same | **PASS** (inh): Review B + Step 5 (c): "distribution-shift guarantee -- different ideas, not different labels" | **PASS** (inh): Check C: "different candidate distribution, not different labels" |
| **C-27 schema-gate phase-advance coupling** | **FAIL** (intentional): Selected? gate: "Phase 3 may begin and Selected? may be populated only when all 5 rows exist" -- names Phase 3 and row-count; "Selected? blank" not stated as dual precondition | **PASS**: "Phase 3 cannot begin until both preconditions hold: (a) all 5 rows written, AND (b) Selected? is blank across all 5 rows" -- names Phase 3 + dual schema state as coupled condition | **PASS**: same as V-02 | **PASS**: "Step 3 may begin only when (a) all 5 rows of this Registry are written AND (b) Top-5? is blank across all rows of the idea table" -- names Step 3 + dual schema state | **PASS** (inh from R7-V-05): "Layer 4 may begin only when all 5 rows exist and Selected? is blank across all rows" + reinforced: "Layer 4 cannot begin until both preconditions hold" |
| **C-28 rationalization-impulse trigger inversion** | **PASS**: Prohibition B: "If you want to revise the rationale, treat that impulse as confirmation that the replacement obligation applies -- the desire to revise is not permission to reopen the comparison, it is evidence the swap is mandatory" | **FAIL** (intentional): Prohibition B: "Do not revise... Rationale revision is the escape route this prohibition closes" -- closes the door; no inversion clause | **PASS**: Prohibition B: "If you want to revise the rationale, treat that impulse as confirmation that the replacement obligation applies -- the desire to revise is not permission to reopen the comparison; it is evidence the swap is mandatory" | **PASS** (inh from R7-V-04 Rule 2): "if editing the Candidate's Rationale would make the comparison sentence completable, that desire confirms the substitution obligation applies" | **PASS** (inh from R7-V-05): "If you want to edit the rationale, treat that impulse as confirmation that the replacement obligation applies -- the desire to revise is not permission to reopen the comparison; it is evidence the swap is mandatory" |

**Projected scores:**

| Variation | C-01..C-26 | C-27 | C-28 | Projected |
|-----------|-----------|------|------|-----------|
| R8-V-01 | 140 (all pass) | FAIL (no dual precondition) | PASS (inversion clause present) | **142.5** |
| R8-V-02 | 140 (all pass) | PASS (dual precondition gate) | FAIL (prohibition only; no inversion) | **142.5** |
| R8-V-03 | 140 (all pass) | PASS (dual precondition gate) | PASS (inversion clause) | **145** |
| R8-V-04 | 140 (all pass) | PASS (Step 3 dual gate: Registry rows + Top-5? blank) | PASS (inh Rule 2 inversion) | **145** |
| R8-V-05 | 140 (all pass) | PASS (inh R7-V-05: Layer 4 dual precondition) | PASS (inh R7-V-05: impulse inversion) | **145** |

**C-27/C-28 mechanism comparison:**

| Variation | C-27 Mechanism | C-28 Mechanism |
|-----------|---------------|----------------|
| V-01 | None (positive-fill framing: "Phase 3 may begin... only when all 5 rows exist" -- row count only) | Inversion: "If you want to revise the rationale, treat that impulse as confirmation that the replacement obligation applies -- the desire to revise is evidence the swap is mandatory" |
| V-02 | Dual precondition: "Phase 3 cannot begin until (a) all 5 rows written AND (b) Selected? is blank across all 5 rows" -- phase named + schema state named | None (prohibition only: "do not revise... Rationale revision is the escape route this prohibition closes") |
| V-03 | Dual precondition (same as V-02): "Phase 3 cannot begin until (a) all 5 rows written AND (b) Selected? is blank" | Inversion (same as V-01): "If you want to revise... treat that impulse as confirmation" |
| V-04 | Dual precondition (table architecture): "Step 3 may begin only when (a) all 5 Registry rows written AND (b) Top-5? blank across all idea table rows" -- step named + dual schema state across two tables | Inversion (inh Rule 2): "if editing Rationale would make the sentence completable, that desire confirms the substitution obligation applies" |
| V-05 | Dual precondition (layered): "Layer 4 cannot begin until (a) all 5 rows exist AND (b) Selected? is blank across all rows" -- strengthened from R7-V-05 | Inversion (inh + expanded): "If you want to edit the rationale, treat that impulse as confirmation... the desire to revise is not permission to reopen the comparison; it is evidence the swap is mandatory" |

**R8 design insight:** The structural signal for C-27 is that the gate must be a DUAL
PRECONDITION -- both the blocked phase and the required schema state must appear together.
R7-V-03's gate ("Phase 3 may begin and Selected? may be filled only when all 5 rows exist")
names Phase 3 and the row-count condition, but "Selected? may be filled" is a permission
statement for going forward, not a state that must currently hold for the gate to open. C-27
requires both: the blocked phase name AND the schema state (all rows present AND Selected?
blank). The language shift is from "may begin when X" to "may begin only when X AND Y" where
Y explicitly names the blank-column precondition. V-01 confirms C-28 is independently worth
2.5 points (inversion alone, no dual gate). V-02 confirms C-27 is independently worth 2.5
points (dual gate alone, no inversion). V-03 demonstrates the minimum combination on the
compact battery base. V-04 demonstrates the minimum repair on the table architecture base
(one targeted change to the Step 3 gate description). V-05 demonstrates the layered
architecture path with an expanded inertia-framing axis that makes the status quo a
cost-of-delay calibration anchor rather than a checkbox -- testing whether more prominent
inertia framing improves output specificity without introducing regressions.
