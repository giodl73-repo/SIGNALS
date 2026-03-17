---
skill: quest-variate
skill_target: draft-brainstorm
round: 9
date: 2026-03-16
rubric_version: 9
r8_scores_under_v9: "V-03 = 145 (C-29 FAIL -- Phase 3 opens 'Fill Selected?=YES', no restatement; C-30 FAIL -- general inversion only), V-04 = 147.5 (C-29 FAIL -- Step 3 opens 'Only after both Step 2b gate conditions are satisfied' -- references but does not restate specific conditions; C-30 PASS -- Rule 2 names comparison-sentence incompletability), V-05 = 147.5 (C-29 PASS -- Layer 4 opens 'Only after both Layer 3 gate conditions are satisfied (all 5 Registry rows written AND Selected? blank across all rows)'; C-30 FAIL -- general inversion only)"
r9_target: "150 -- achieve both C-29 (phase-advance gate restated at entry of gated phase, dual-anchor) and C-30 (inversion trigger names comparison-sentence incompletability as causal mechanism) in isolation and in combination"
---

# Variate R9 -- draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01 through V-02), then combinations (V-03, V-04, V-05).

R9 focuses on the two R9 aspirational criteria introduced in rubric v9:
- **C-29** Phase-Gate Entry-Point Restatement -- C-27 is the floor (schema gate explicitly
  coupled to a named phase-advance condition in a single statement); C-29 is the ceiling:
  the gate is restated at the entry of the phase it guards -- the prompt contains two anchors:
  (a) gate at the schema level (column definition, Registry spec) and (b) gate restated as a
  pre-condition at the gated phase's opening; "Layer 4 may begin only when..." written inside
  Layer 4 itself satisfies C-29; a single coupled statement at the schema level (C-27) does not
- **C-30** Inversion Trigger Causal Specificity -- C-28 is the floor (rationalization impulse
  inverted as a positive enforcement trigger: "if you want to revise, treat that impulse as
  confirmation"); C-30 is the ceiling: the inversion names the specific causal mechanism --
  the inability to complete the comparison sentence -- as what produces the revision desire;
  "if editing the rationale would make the comparison sentence completable, that desire confirms
  the obligation applies" satisfies C-30; "if you want to revise, that confirms the obligation"
  (general impulse inversion) satisfies C-28 only

R8 gap analysis under rubric v9:

| Variation | R8 Score (v8) | C-29 under v9 | C-30 under v9 | Score under v9 |
|-----------|--------------|---------------|---------------|----------------|
| R8-V-01 (142.5) | 142.5 | FAIL (Phase 3 opens without restatement; C-27 FAIL means C-29 moot) | FAIL (inversion present but general: "If you want to revise...") | 142.5 |
| R8-V-02 (142.5) | 142.5 | FAIL (Phase 3 opens without restatement; C-27 PASS but no restatement at Phase 3 entry) | FAIL (no inversion at all -- prohibition-only Prohibition B) | 142.5 |
| R8-V-03 (145) | 145 | FAIL (Phase 3 opens "Fill Selected? = YES..." -- no restatement of gate conditions at phase entry) | FAIL (inversion present but general: "If you want to revise the rationale, treat that impulse as confirmation...") | 145 |
| R8-V-04 (145) | 145 | FAIL (Step 3 opens "Only after both Step 2b gate conditions are satisfied: fill in..." -- references conditions by label, does not restate specific preconditions) | PASS (Rule 2: "if editing the Candidate's Rationale **would make the comparison sentence completable**, that desire confirms the substitution obligation applies" -- names comparison-sentence incompletability as causal mechanism) | 147.5 |
| R8-V-05 (145) | 145 | PASS (Layer 4 opens "Only after both Layer 3 gate conditions are satisfied **(all 5 Registry rows written AND Selected? blank across all rows)**:" -- conditions restated in full at Layer 4 entry) | FAIL (Rationalization Prohibition: "If you want to edit the rationale, treat that impulse as confirmation that the replacement obligation applies" -- general impulse inversion, no causal mechanism named) | 147.5 |

R9 axes selected:

| Axis | New in R9? | Used In | R9 Criterion |
|------|-----------|---------|--------------|
| Phrasing register: causal specificity in inversion clause | Yes | V-01, V-03 | C-30 (V-01 isolated; V-03 combined) |
| Lifecycle emphasis: gate restatement at gated phase entry | Yes | V-02, V-03 | C-29 (V-02 isolated; V-03 combined) |
| Output format: table architecture with Step 3 restatement repair | Repair of R8-V-04 C-29 gap | V-04 | C-29 repair + C-30 inherited |
| Role sequence: layered architecture with causal inversion repair | Repair of R8-V-05 C-30 gap | V-05 | C-29 inherited + C-30 repair |

Root cause of R8-V-04 C-29 gap: Step 3 opens "Only after both Step 2b gate conditions
are satisfied: fill in `**YES**`..." -- this names Step 3 as the gated phase and
references the conditions by label ("Step 2b gate conditions"), but does not restate
the specific preconditions at the entry point of Step 3. C-29 requires the conditions
to be spelled out at the phase transition: "Only after both preconditions hold --
(a) all 5 rows of the Registry are written AND (b) Top-5? is blank across all rows
of the idea table -- fill in `**YES**`..." restates both conditions explicitly.

Root cause of R8-V-05 C-30 gap: Rationalization Prohibition reads "If you want to
edit the rationale, treat that impulse as confirmation that the replacement obligation
applies -- the desire to revise is not permission to reopen the comparison; it is
evidence the swap is mandatory." This inverts the general revision impulse (C-28
PASS) but does not name the causal mechanism. C-30 requires the trigger to be
specific: the revision desire arises because the rationale gap is what prevented
the comparison sentence from being completable. The fix names the cause: "if editing
the rationale would make the comparison sentence completable, that desire confirms
the obligation applies" -- the "would make completable" clause is the causal link.

---

## V-01 -- Phrasing Register: C-30 Causal Specificity (C-29 intentionally absent)

**Axis**: Phrasing register -- Prohibition B is restructured so the inversion clause
names comparison-sentence incompletability as the specific causal mechanism: "if
editing the candidate's rationale would make the comparison sentence completable,
that desire confirms the replacement obligation applies"; C-29 is intentionally
absent (Phase 3 opens without restating gate conditions -- the dual-anchor property
is not present, only the single-statement gate in the Selected? column rule)
**Base**: R8-V-03 (145 under v8 -- C-27 PASS single-statement, C-28 PASS general
inversion, C-29 FAIL no entry restatement, C-30 FAIL general inversion)
**Hypothesis**: R8-V-03's Prohibition B reads "if you want to revise the rationale,
treat that impulse as confirmation" -- this passes C-28 (general impulse inversion)
but fails C-30 (no causal mechanism named). V-01 replaces this with the causally
specific formula from R8-V-04's Rule 2: "if editing the rationale would make the
comparison sentence completable, that desire confirms the obligation applies." Phase
3 is unchanged -- it opens without restating gate conditions, so C-29 intentionally
fails. If V-01 scores 147.5, the causal-specificity change alone contributes 2.5
points independently of C-29.

**Expected**: C-01..C-28 PASS (inh) + C-29 FAIL (Phase 3 entry: no restatement of
gate conditions) + C-30 PASS (Prohibition B: inversion trigger names
comparison-sentence incompletability) = **147.5**

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
to manufacture a distinction that was not present at comparison time. If editing
the candidate's rationale would make the comparison sentence completable, that
desire confirms the replacement obligation applies -- the impulse to revise so the
comparison can pass is not permission to reopen the comparison; it is the signal
the swap is mandatory.

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

## V-02 -- Lifecycle Emphasis: C-29 Phase-Gate Entry Restatement (C-30 intentionally absent)

**Axis**: Lifecycle emphasis -- Phase 3 gains an explicit entry-point restatement of
the gate conditions: Phase 3 opens with a pre-condition block that names both required
preconditions verbatim before any finalization instruction, creating the dual-anchor
property; C-30 is intentionally absent (Prohibition B retains the general impulse
inversion -- "if you want to revise, treat that impulse as confirmation" -- without
naming comparison-sentence incompletability as the causal mechanism)
**Base**: R8-V-03 (145 under v8 -- C-27 PASS, C-28 PASS general, C-29 FAIL, C-30 FAIL)
**Hypothesis**: R8-V-03's Phase 3 opens "Fill Selected? = YES..." with no restatement
of the gate conditions that were established in the Selected? column rule. A model
beginning Phase 3 does not re-encounter the gate constraint at the transition point.
V-02 prepends a gate restatement to Phase 3: "Only after both preconditions hold --
(a) all 5 rows of this Registry are written in your output, AND (b) Selected? is blank
across all 5 rows -- may Phase 3 begin." This is the minimum change for C-29: the gate
appears at schema definition (Selected? column rule) AND at the phase transition (Phase
3 opening). Prohibition B is unchanged -- general inversion, C-30 intentionally absent.
If V-02 scores 147.5, the entry-restatement change alone contributes 2.5 points.

**Expected**: C-01..C-28 PASS (inh) + C-29 PASS (Phase 3 entry: gate conditions
restated verbatim at phase opening) + C-30 FAIL (Prohibition B: general inversion;
causal mechanism not named) = **147.5**

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

Only after both preconditions hold simultaneously -- (a) all 5 rows of this
Registry are written in your output, AND (b) Selected? is blank across all 5
rows -- may Phase 3 begin. Both conditions must hold before proceeding to any
finalization step below.

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

## V-03 -- Lifecycle + Phrasing: C-29 + C-30 Combined (Prohibition Battery base)

**Axes**: Lifecycle emphasis (C-29 entry restatement from V-02) + phrasing register
(C-30 causal specificity from V-01); compact Prohibition Battery architecture
preserved; both changes applied to the R8-V-03 base
**Base**: R8-V-03 (145 under v8 -- C-27 PASS, C-28 PASS general, C-29 FAIL, C-30 FAIL)
**Hypothesis**: V-01 confirms C-30 at +2.5 (causally specific inversion) and V-02
confirms C-29 at +2.5 (entry-point restatement) independently on the same base.
V-03 combines both: Phase 3 gains the entry restatement (C-29) and Prohibition B
gains the causal-mechanism formula (C-30). If both pass together, V-03 scores 150.

**Expected**: C-01..C-28 PASS (inh) + C-29 PASS (Phase 3 opens with gate restatement)
+ C-30 PASS (Prohibition B: inversion names comparison-sentence incompletability)
= **150**

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
to manufacture a distinction that was not present at comparison time. If editing
the candidate's rationale would make the comparison sentence completable, that
desire confirms the replacement obligation applies -- the impulse to revise so the
comparison can pass is not permission to reopen the comparison; it is the signal
the swap is mandatory.

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

Only after both preconditions hold simultaneously -- (a) all 5 rows of this
Registry are written in your output, AND (b) Selected? is blank across all 5
rows -- may Phase 3 begin. Both conditions must hold before proceeding to any
finalization step below.

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

## V-04 -- Output Format: Table Architecture + C-29 Entry Restatement (C-30 inherited from R8-V-04 Rule 2)

**Axis**: Output format -- table architecture with minimum-viable repair of R8-V-04's
C-29 gap: Step 3 opening is restructured to restate both preconditions explicitly
rather than referencing them by label ("Step 2b gate conditions"); C-30 is inherited
from R8-V-04 Rule 2 which already names comparison-sentence incompletability
**Base**: R8-V-04 (147.5 under v9 -- C-27 PASS, C-28 PASS Rule 2 causal, C-29 FAIL
step-reference only, C-30 PASS Rule 2)
**Hypothesis**: R8-V-04 Step 3 opens "Only after both Step 2b gate conditions are
satisfied: fill in `**YES**`..." -- this names Step 3 as gated and defers to a label
("Step 2b gate conditions") rather than restating the specific conditions. A model
beginning Step 3 encounters "after both Step 2b gate conditions are satisfied" without
seeing those conditions spelled out again. V-04 repairs this by replacing the
label-reference with an explicit restatement: "Only after both preconditions hold --
(a) all 5 rows of the Pre-Selection Batch Registry are written in your output, AND
(b) Top-5? is blank across all rows of the idea table above -- fill in `**YES**`..."
This creates the dual-anchor: conditions at the Step 2b column definition AND
restated at Step 3 entry. Rule 2 is unchanged -- already causally specific.

**Expected**: C-01..C-28 PASS (inh) + C-29 PASS (Step 3 opens with explicit
restatement of both preconditions) + C-30 PASS (inh from R8-V-04 Rule 2)
= **150**

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
desire confirms the substitution obligation applies -- the impulse to revise so
the comparison can pass is not an exit; it is the signal the swap is mandatory.
No post-Registry Rationale edits are permitted as a mechanism to avoid a mandated
substitution.

This Registry is required output. The artifact is incomplete without all 5 rows.

---

### Step 3 -- Mark Top-5 (gated by Step 2b completion and idea table state)

Only after both preconditions hold -- (a) all 5 rows of the Pre-Selection Batch
Registry are written in your output, AND (b) Top-5? is blank across all rows of
the idea table above -- fill in `**YES**` in exactly 5 rows' Top-5? column, using
the candidates confirmed in the Registry. If any substitution was required in Step
2b, the substituted peer's row receives the `**YES**` mark.

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

## V-05 -- Role Sequence + Phrasing: C-29 Inherited + C-30 Causal Specificity (Layered Architecture)

**Axes**: Role sequence (7-layer architecture from R8-V-05; Layer 4 entry restatement
preserved, C-29 inherited) + phrasing register (Rationalization Prohibition gains the
causally specific formula: "if editing the rationale would make the comparison sentence
completable, that desire confirms..." replacing the general inversion; C-30 repaired)
**Base**: R8-V-05 (147.5 under v9 -- C-29 PASS Layer 4 restatement, C-30 FAIL general
inversion, all other criteria inherited)
**Hypothesis**: R8-V-05 already passes C-29 via Layer 4 opening: "Only after both
Layer 3 gate conditions are satisfied (all 5 Registry rows written AND Selected? blank
across all rows):" -- the conditions are spelled out in full at the phase transition.
The only gap is C-30: the Rationalization Prohibition reads "If you want to edit the
rationale, treat that impulse as confirmation that the replacement obligation applies"
-- general impulse inversion, no causal mechanism. V-05 repairs this with the
causally specific formula: "if editing the rationale would make the comparison
sentence completable, that desire confirms the replacement obligation applies --
the impulse to revise so the comparison can pass is the signal the swap is mandatory."
C-29 inheritance is verified as unchanged -- the Layer 4 opening is untouched.

**Expected**: C-01..C-28 PASS (inh) + C-29 PASS (inh from R8-V-05 Layer 4 opening)
+ C-30 PASS (Rationalization Prohibition: causal mechanism named)
= **150**

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
was not present at comparison time. If editing the candidate's rationale would
make the comparison sentence completable, that desire confirms the replacement
obligation applies -- the impulse to revise so the comparison can pass is not
permission to reopen the comparison; it is the signal the swap is mandatory.

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

## Rubric Coverage Analysis -- R9

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 volume (20-40) | "20-40 candidates" | same (inh) | same (inh) | "20-40 rows total" | "20-40" |
| C-02 idea anatomy | Per-idea block (4 fields) | same (inh) | same (inh) | Table columns (Name/Pitch/Dimension/Rationale) | Per-idea block |
| C-03 top-5 marker | `**` heading + Selected?=YES | same (inh) | same (inh) | `**YES**` in Top-5? col | `**` heading + Selected?=YES |
| C-04 inertia check | Status Quo required section | same (inh) | same (inh) | Status Quo row + Preamble | Dim 7 mandatory + Layer 0 |
| C-05 AMEND (3 items) | 1c draft + Check C | same (inh) | same (inh) | Step 5 output of Review B | Layer 2 draft + Check C |
| C-06 category grouping | Required `##` sections | same (inh) | same (inh) | Category View (Step 4) | 7 dimension `##` headers |
| C-07 rationale specificity | "cite real constraint; no generic" | same (inh) | same (inh) | "cite specific constraint" | "name real constraint; topic-specific" + trajectory-cost anchor |
| C-08 category diversity | 6 required dimensions | same (inh) | same (inh) | 7 required dimension types | 7 named dimensions |
| C-09 AMEND actionability | Check C distribution-shift | same (inh) | same (inh) | Review B + Step 5 | Check C distribution-shift |
| C-10 top-5 defensibility | Check A + Registry + batch gate | same (inh) | same (inh) | Review A + Registry + Rules 1/2 | Check A + Verification Registry |
| C-11 sequential-default guard | "Do not mark top-5 yet" imperative | same (inh) | same (inh) | "Leave Top-5? blank during Step 1" | "Do not mark any idea... in this layer" |
| C-12 re-runnability bar | Check C distribution-shift | same (inh) | same (inh) | Review B + Step 5 | Check C distribution-shift |
| C-13 category dimension taxonomy | 6 named dimensions with descriptions | same (inh) | same (inh) | 7 named dimension types | 7 named dimensions with descriptions |
| C-14 inertia-first framing paragraph | 1a: "appears at top... precedes all ideas" | same (inh) | same (inh) | Preamble: "must appear before idea table" | Layer 0: "must appear first" |
| C-15 structural spine guarantee | PASS: 6 required `##` sections mandated | same (inh) | same (inh) | PASS: Category View "required structural output" | PASS: 7 dimension `##` headers mandated |
| C-16 generation-phase sequential guard | PASS: "Do not mark top-5 yet" in Phase 1b, imperative | same (inh) | same (inh) | PASS: "Leave Top-5? blank during Step 1" | PASS: "Do not mark any idea with `**` in this layer" |
| C-17 peer-comparison defensibility test | PASS: Registry sentence column | same (inh) | same (inh) | PASS: Registry "I chose [Candidate] over [Peer] because ___" | PASS: Registry sentence column |
| C-18 self-review phase integration | PASS: Check A->Registry; Registry->Phase 3; Check C->AMEND; Check D->artifact | same (inh) | same (inh) | PASS: Review A->Step 2b; Review B->Step 5; Step 2b->Step 3 | PASS: Check A->Check B; Check B->Layer 4; Check C->AMEND; Check D->gates write |
| C-19 peer-test imperative form | PASS: Registry row completion enforces sentence materialization | same (inh) | same (inh) | PASS: Registry row completion | PASS: Registry row completion |
| C-20 peer-test consequence clause | PASS: Prohibition B: "must be replaced by the specific peer" | same (inh) | same (inh) | PASS: Rule 1: "`**YES**` mark must go to Attempted Peer" | PASS: "must be replaced with the specific peer" |
| C-21 peer-test batch-completion gate | PASS: "Phase 3 may begin only when all 5 rows exist" (via Selected? rule) | PASS (inh) | PASS (inh) | PASS: "Step 3 may begin only when (a) all 5 rows AND (b) Top-5? blank" | PASS: "Layer 4 may begin only when all 5 rows exist and Selected? blank" |
| C-22 consequence replacement source | PASS: "peer from this row, not a different idea" | same (inh) | same (inh) | PASS: "Attempted Peer from this row -- not a different idea after reconsidering" | PASS: "peer from this row, not a different idea you prefer after reconsidering" |
| C-23 selection-phase marking prohibition | PASS: Prohibition A: "The marking action is what is prohibited, not merely deferred" | same (inh) | same (inh) | PASS: "The marking action is prohibited until all 5 rows are complete" | PASS: "The marking action is prohibited -- not deferred row by row" |
| C-24 post-comparison rationalization block | PASS: Prohibition B: "Do not revise the candidate's rationale... to manufacture a distinction" | same (inh) | same (inh) | PASS: Rule 2: "Once a Registry row is written, the comparison is final on the Rationale as it exists" | PASS: "Do not revise the candidate's rationale after Check B" |
| C-25 marking-gate schema lock | PASS (inh): Selected? "cannot hold any value until all 5 rows complete -- schema constraint" | PASS (inh) | PASS (inh) | PASS (inh): Top-5? gated by Step 2b | PASS (inh): Selected? "property of the Registry schema" |
| C-26 AMEND pool-composition constraint | PASS (inh): Check C: "different ideas, not different labels on the same ideas" | PASS (inh) | PASS (inh) | PASS (inh): Step 5 (c): "distribution-shift guarantee -- different ideas, not different labels" | PASS (inh): Check C: "different candidate distribution, not different labels" |
| C-27 schema-gate phase-advance coupling | PASS (inh): Selected? rule: "Phase 3 cannot begin until both preconditions hold simultaneously: (a) all 5 rows AND (b) Selected? blank" | PASS (inh): same | PASS (inh) | PASS (inh): "Step 3 may begin only when (a) all 5 rows AND (b) Top-5? blank -- structural gate on Step 3" | PASS (inh): "Layer 4 may begin only when all 5 rows exist and Selected? blank" |
| C-28 rationalization-impulse trigger inversion | PASS (inh): Prohibition B: "if editing the candidate's rationale would make the comparison sentence completable, that desire confirms..." (also satisfies C-30) | PASS (inh): Prohibition B: "If you want to revise the rationale, treat that impulse as confirmation..." (general inversion; C-30 FAIL intentional) | PASS (inh): same causal formula as V-01 | PASS (inh from R8-V-04 Rule 2): "if editing the Candidate's Rationale would make the comparison sentence completable, that desire confirms..." | PASS (inh): "If editing the candidate's rationale would make the comparison sentence completable, that desire confirms..." |
| **C-29 phase-gate entry-point restatement** | **FAIL** (intentional): Phase 3 opens "Fill Selected? = YES in exactly 5 rows..." -- no restatement of gate conditions at phase entry; Selected? column rule is the only anchor | **PASS**: Phase 3 opens "Only after both preconditions hold simultaneously -- (a) all 5 rows of this Registry are written in your output, AND (b) Selected? is blank across all 5 rows -- may Phase 3 begin" -- conditions spelled out verbatim at phase entry | **PASS**: same Phase 3 restatement as V-02 | **PASS**: Step 3 opens "Only after both preconditions hold -- (a) all 5 rows of the Pre-Selection Batch Registry are written in your output, AND (b) Top-5? is blank across all rows of the idea table above -- fill in `**YES**`..." -- specific conditions restated at phase entry | **PASS** (inh from R8-V-05): Layer 4 opens "Only after both Layer 3 gate conditions are satisfied (all 5 Registry rows written AND Selected? blank across all rows):" -- dual-anchor present |
| **C-30 inversion trigger causal specificity** | **PASS**: Prohibition B: "If editing the candidate's rationale would make the comparison sentence completable, that desire confirms the replacement obligation applies -- the impulse to revise so the comparison can pass is not permission to reopen the comparison; it is the signal the swap is mandatory" | **FAIL** (intentional): Prohibition B: "If you want to revise the rationale, treat that impulse as confirmation that the replacement obligation applies" -- general impulse inversion; comparison-sentence incompletability not named as causal mechanism | **PASS**: same causal formula as V-01 | **PASS** (inh from R8-V-04 Rule 2): "If editing the Candidate's Rationale would make the comparison sentence completable, that desire confirms the substitution obligation applies" | **PASS**: Rationalization Prohibition: "If editing the candidate's rationale would make the comparison sentence completable, that desire confirms the replacement obligation applies -- the impulse to revise so the comparison can pass is the signal the swap is mandatory" |

**Projected scores:**

| Variation | C-01..C-28 | C-29 | C-30 | Projected |
|-----------|-----------|------|------|-----------|
| R9-V-01 | 145 (all pass) | FAIL (no Phase 3 restatement) | PASS (causal mechanism named) | **147.5** |
| R9-V-02 | 145 (all pass) | PASS (Phase 3 entry restatement) | FAIL (general inversion; no causal mechanism) | **147.5** |
| R9-V-03 | 145 (all pass) | PASS (Phase 3 entry restatement) | PASS (causal mechanism named) | **150** |
| R9-V-04 | 145 (all pass) | PASS (Step 3 entry restatement) | PASS (inh from R8-V-04 Rule 2) | **150** |
| R9-V-05 | 145 (all pass) | PASS (inh from R8-V-05 Layer 4) | PASS (causal mechanism named) | **150** |
