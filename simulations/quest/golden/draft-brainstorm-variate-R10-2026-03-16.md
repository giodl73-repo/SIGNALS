---
skill: quest-variate
skill_target: draft-brainstorm
round: 10
date: 2026-03-16
rubric_version: 10
r9_scores_under_v10: "V-03 = 155 (C-31 PASS -- Phase 3 opens 'Only after both preconditions hold simultaneously -- (a) all 5 rows of this Registry are written in your output, AND (b) Selected? is blank across all 5 rows'; C-32 PASS -- 'the impulse to revise so the comparison can pass is not permission to reopen the comparison; it is the signal the swap is mandatory'), V-01 = 150 (C-29 FAIL -> C-31 FAIL -- Phase 3 has no restatement at all; C-30 PASS + dual-frame -> C-32 PASS), V-02 = 150 (C-29 PASS verbatim -> C-31 PASS -- Phase 3 opens with conditions restated; C-30 FAIL -> C-32 FAIL -- general impulse inversion, no causal mechanism named)"
r10_target: "155 -- confirm C-31 and C-32 are structurally stable across: (a) conversational register with weak C-29 label-reference (C-31 isolated FAIL), (b) formal register with prominent gate-block (C-31 isolated PASS), (c) combined 155 via gate-block + dual-frame, (d) numbered-step format architecture, (e) inertia-first pool ordering"
---

# Variate R10 -- draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01, V-02), then combinations (V-03, V-04, V-05).

R10 targets the two v10 criteria introduced in rubric v10:
- **C-31** Phase-Entry Restatement Verbatim Condition Expansion -- C-29 is the floor
  (gate restated at phase entry, dual-anchor); C-31 is the ceiling: the restatement
  uses verbatim schema element names -- "(a) all 5 rows AND (b) Selected? blank" --
  not a label-reference like "once the gate conditions hold." A weak C-29 pass
  (label-reference at phase entry) fails C-31. C-31 requires the strong form with
  actual column names and row counts written at the transition point.
- **C-32** Inversion Dual-Frame Negation-Affirmation -- C-30 is the floor (inversion
  trigger names comparison-sentence incompletability as causal mechanism); C-32 is the
  ceiling: after naming the causal mechanism, the prompt closes both escape paths --
  denying one interpretation explicitly ("not permission to reopen the comparison") AND
  affirming the mandate explicitly ("the signal the swap is mandatory"). C-30 names why
  the impulse arises; C-32 eliminates interpretive latitude by stating what it is not
  AND what it is. C-30 alone leaves the model to infer the consequence; C-32 removes
  that inference gap.

R9 gap analysis under rubric v10:

| Variation | R9 Score (v9) | C-31 under v10 | C-32 under v10 | Score under v10 |
|-----------|--------------|----------------|----------------|-----------------|
| R9-V-01 (147.5) | 147.5 | FAIL (Phase 3 has no restatement -- C-29 already failed; no entry anchor at all) | PASS (Prohibition B: "if editing the rationale would make the comparison sentence completable... the impulse to revise so the comparison can pass is not permission to reopen the comparison; it is the signal the swap is mandatory" -- causal mechanism + dual-frame both present) | 150 |
| R9-V-02 (147.5) | 147.5 | PASS (Phase 3 opens "Only after both preconditions hold simultaneously -- (a) all 5 rows of this Registry are written in your output, AND (b) Selected? is blank across all 5 rows" -- verbatim schema element names at transition) | FAIL (Prohibition B: "If you want to revise the rationale, treat that impulse as confirmation that the replacement obligation applies" -- general impulse inversion, no causal mechanism for C-30; C-32 requires C-30 as prerequisite) | 150 |
| R9-V-03 (150) | 150 | PASS (Phase 3 opens "Only after both preconditions hold simultaneously -- (a) all 5 rows of this Registry are written in your output, AND (b) Selected? is blank across all 5 rows" -- verbatim schema names at transition) | PASS ("the impulse to revise so the comparison can pass is not permission to reopen the comparison; it is the signal the swap is mandatory" -- causal mechanism named + negation stated + affirmation stated) | 155 |
| R9-V-04 (150) | 150 | PASS (Step 3 opens "Only after both preconditions hold -- (a) all 5 rows of the Pre-Selection Batch Registry are written in your output, AND (b) Top-5? is blank across all rows of the idea table above" -- verbatim) | PASS (Rule 2: "the impulse to revise so the comparison can pass is not an exit; it is the signal the swap is mandatory" -- "not an exit" is the negation; "the signal the swap is mandatory" is the affirmation) | 155 |
| R9-V-05 (150) | 150 | PASS (Layer 4 opens "Only after both Layer 3 gate conditions are satisfied (all 5 Registry rows written AND Selected? blank across all rows)" -- conditions restated in full at Layer 4 entry) | FAIL (Rationalization Prohibition: "If you want to edit the rationale, treat that impulse as confirmation that the replacement obligation applies -- the desire to revise is not permission to reopen the comparison; it is evidence the swap is mandatory" -- dual-frame present but C-30 fails; "if you want to edit" is general impulse, not "if editing would make the comparison sentence completable") | 150 |

R10 axes selected:

| Axis | New in R10? | Used In | R10 Criterion |
|------|------------|---------|---------------|
| Phrasing register: conversational throughout, weak C-29 label-reference | Yes | V-01 | C-31 FAIL isolated (C-32 PASS inherited) |
| Lifecycle emphasis: Phase 3 gate as dedicated PRECONDITIONS callout block | Yes | V-02 | C-31 PASS isolated (C-32 absent) |
| Combination: callout gate block + dual-frame | Yes | V-03 | C-31 + C-32 both PASS |
| Output format: numbered steps with verbatim gate at Step 8 entry | Repair of R9-V-05 C-32 gap in numbered-step architecture | V-04 | C-31 + C-32 both PASS |
| Inertia framing: Status Quo section elevated to first position, Phase 0 treatment | Yes | V-05 | C-31 + C-32 both PASS |

Root cause of R9-V-05 C-32 gap: Rationalization Prohibition reads "If you want to
edit the rationale, treat that impulse as confirmation that the replacement obligation
applies -- the desire to revise is not permission to reopen the comparison; it is
evidence the swap is mandatory." The dual-frame words are present ("not permission to
reopen... evidence the swap is mandatory") but the causal trigger is the general impulse
("if you want to edit"), not the specific mechanism ("if editing would make the comparison
sentence completable"). C-32 requires C-30 as prerequisite: the dual-frame closes both
sides of the interpretation that the causal mechanism opens. Without C-30's causal
specificity, C-32 cannot pass even when dual-frame language is present.

---

## V-01 -- Phrasing Register: Conversational C-32 (C-31 intentionally absent via weak label-reference)

**Axis**: Phrasing register -- the entire prompt is rewritten in a conversational,
advisory tone ("your job is to", "here's the key", "once the conditions hold"). The
essential mechanism changes are: Prohibition B retains the C-30 causal specificity
and adds the C-32 dual-frame negation+affirmation. Phase 3 opens with a label-reference
("Once both gate conditions from Check B hold, proceed here") -- the specific schema
element names (Selected?, 5 rows) are not restated at the phase transition, so C-31
intentionally fails. C-29 passes weakly (label-reference at phase entry, dual-anchor
present) but C-31 requires the strong form.
**Base**: R9-V-01 (150 under v10 -- C-29 FAIL, C-30 PASS, C-31 FAIL, C-32 PASS)
**Hypothesis**: C-32's dual-frame negation+affirmation is register-stable -- it
survives conversion from formal/technical to conversational tone. The key clause
("not permission to reopen... the signal the swap is mandatory") is structural, not
stylistic. If V-01 scores 150 under v10, C-32 is confirmed register-independent.
The conversational label-reference at Phase 3 ("once the conditions hold") is weaker
than R9-V-02's verbatim gate and confirms that C-31 failure is not merely a prose
style issue -- it requires named schema elements, not just a dual-anchor.

**Expected**: C-01..C-30 PASS (inh) + C-31 FAIL (Phase 3 entry: "Once both gate
conditions from Check B hold" -- label-reference, Selected? and row count not named)
+ C-32 PASS (Prohibition B: causal mechanism named + negation "not permission to
reopen" + affirmation "signal the swap is mandatory") = **150**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

Your job is to generate a large pool of ideas, then verify and finalize before writing
the artifact. Work through two phases in order: GENERATE first, then VERIFY. Don't write
the final artifact until verification is complete.

---

## PHASE 1 -- GENERATE

### Step 1a: Set the Scene

Before listing any ideas, write a paragraph (3-5 sentences) that captures the current
trajectory of {{topic}}: What is the team living with right now? What accumulates if
nothing changes -- technically, organizationally, or for users? What does inertia
concretely produce?

This paragraph appears at the top of your final artifact, before any ideas.

### Step 1b: Build the Pool

Generate 20-40 ideas for {{topic}}. Organize them under the required dimensions below.
Each dimension is a **mandatory output section** (a `##` heading in your output) -- not
a scaffolding suggestion. Don't collapse them into a flat list. Don't omit any. You may
add more dimensions beyond the required six.

**Required dimensions -- each must appear as its own `## [Name]` section:**

- **Scope** -- how much of the problem space {{topic}} addresses
- **Timing** -- when in the product lifecycle the intervention lands
- **Integration** -- how it connects to existing systems or teams
- **Audience** -- who benefits most directly
- **Build vs. Buy** -- internal build, external adoption, or extension
- **Status Quo** -- exactly one idea: Do Nothing

For each idea, use this format:

```
## [Dimension Name]

### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this specifically serves {{topic}} -- name a real constraint, user
need, or opportunity. No generic justifications.
```

**One rule for this step**: Don't mark the top-5 yet. Finish the full pool first.
Marking as you write introduces sequential bias -- the first ideas aren't the best,
just the most recently visible. Don't mark until the complete pool is written.

The Do Nothing idea goes in the Status Quo section. Its rationale should continue the
trajectory from Step 1a -- what does inertia concretely produce for {{topic}}?

### Step 1c: Draft AMEND

Write a draft AMEND section with 3 directions that would shift the pool. For each
direction: name it, describe what changes, and check -- if a reader re-ran the
brainstorm with only this directive, would they get ideas that aren't in the current
pool? Each directive must produce different ideas, not the same ideas under different
framing. Don't finalize yet.

---

## PHASE 2 -- VERIFY

Run all four checks in order. Each check connects explicitly to a downstream output
decision -- don't skip any.

**Check A -- Are these the first five?** (feeds candidates to Check B)

Name the 5 ideas you're considering for top-5. Are they the first five you generated?
If yes, rescan the full pool -- the best ideas surface across the whole run, not just
the opening. The output of Check A is the set of 5 candidates advancing to Check B.

**Check B -- Can you defend each one?** (determines final top-5 marks)

For each candidate from Check A, fill one row in the Peer-Comparison Registry. Do not
touch the Selected? column until the Registry is complete.

| # | Candidate (exact name) | Peer (exact name, same ## section, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|------------------------|----------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

Column rules:
- **Candidate**: exact name from Step 1b; one of your 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same ## section; cannot be blank
- **"I chose ... because ___"**: complete the sentence with a specific reason tied to
  {{topic}}'s actual constraints (scope, user group, cost, risk); "it is better" or
  "more viable" don't count
- **Selected?**: Leave blank during Registry construction. Once both gate conditions
  from Check B hold, you may proceed to Phase 3. Until then, no value enters this column.

Two prohibitions apply to Check B without exception:

**Prohibition A -- No ** marks during Check B**: Don't place any `**` markers anywhere
in your output while Check B is in progress -- not on headings, inline text, notes, or
in any other form. No marks until the complete 5-row Registry is written.

**Prohibition B -- No rationale revision**: If you can't complete the sentence for any
row -- no specific peer holds or no specific reason exists -- replace that candidate with
the specific peer you named in the Peer column. Use that peer; don't select a different
idea after reconsidering. Don't revise the candidate's rationale to manufacture a
distinction that wasn't present at comparison time. Here's the key: if editing the
candidate's rationale would make the comparison sentence completable, that desire
confirms the replacement obligation applies -- the impulse to revise so the comparison
can pass is not permission to reopen the comparison; it is the signal the swap is
mandatory.

**Check C -- Will each AMEND direction generate different ideas?** (determines final AMEND)

Each AMEND direction must produce ideas that wouldn't appear in the original pool -- not
the same ideas under different labels, but genuinely different candidates. Ask for each:
if I re-ran this brainstorm with only this directive, would different ideas surface? If
the answer is "probably the same under a different frame," sharpen it. Check C determines
final AMEND content.

**Check D -- Does the framing paragraph come first?** (gates artifact write)

Is the Step 1a paragraph the first thing in your artifact, before any ideas? If not,
move it. This check gates writing the artifact.

---

## PHASE 3 -- FINALIZE

Once both gate conditions from Check B hold, proceed here.

Fill Selected? = YES in exactly 5 rows of the Registry (the candidates confirmed by
Check B, with substitutions from Prohibition B applied). Mark those same 5 ideas with
`**` on their headings in the dimension sections. Update AMEND items if Check C
required changes.

Write the artifact to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: framing paragraph, then dimension sections (top-5 marked), then
Peer-Comparison Registry, then AMEND. Total ideas including Do Nothing: 20-40.
```

---

## V-02 -- Lifecycle Emphasis: Dedicated Gate Preconditions Block (C-31 PASS, C-32 intentionally absent)

**Axis**: Lifecycle emphasis -- Phase 3 gains a visually distinct **GATE PRECONDITIONS**
block as a named callout before any finalization instructions, explicitly restating both
preconditions with verbatim schema element names (Selected?, 5 rows of the Registry).
C-32 is intentionally absent: Prohibition B uses the general impulse inversion ("if you
want to revise... treat that impulse as confirmation") without naming comparison-sentence
incompletability as the causal mechanism -- C-30 FAIL, C-32 FAIL.
**Base**: R9-V-02 (150 under v10 -- C-29 PASS verbatim, C-30 FAIL, C-31 PASS, C-32 FAIL)
**Hypothesis**: The dedicated gate block makes C-31 visually unambiguous -- the verbatim
schema element names appear in a labeled block at the transition point, not buried in
column-rule prose. If V-02 scores 150, C-31's pass condition is confirmed as purely
about whether verbatim names appear (not about visual format). Prohibition B's general
inversion confirms C-32 fails without the causal mechanism, even when dual-frame words
("not permission to reopen") appear elsewhere in the text.

**Expected**: C-01..C-30 PASS (inh, with C-30 FAIL and C-29 PASS) + C-31 PASS (Phase 3
GATE PRECONDITIONS block names "Selected?" and "all 5 rows" verbatim at transition) +
C-32 FAIL (Prohibition B: general impulse inversion -- "if you want to revise, treat
that impulse as confirmation" -- no causal mechanism, so C-30 prerequisite absent) = **150**

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
- **Selected?**: Phase-advance gate. This column cannot hold any value while Check B
  is in progress. A partial Registry has no valid Selected? entries. A Registry where
  any Selected? cell carries a preliminary value does not satisfy the gate. This is a
  schema property of the Registry -- the Selected? column exists for Phase 3 only.

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

> **GATE PRECONDITIONS -- both must hold before Phase 3 may begin:**
> - **(a)** All 5 rows of the Peer-Comparison Registry are written in your output
> - **(b)** Selected? is blank across all 5 rows of the Registry
>
> A Registry with fewer than 5 rows does not satisfy (a). A Registry where any
> Selected? cell holds any value does not satisfy (b). Phase 3 may not begin
> until both (a) and (b) hold simultaneously. Verify both conditions before
> proceeding to any finalization step below.

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

## V-03 -- Combination: Gate Callout Block (V-02) + Causal Dual-Frame (V-01) -- targeting 155

**Axes**: Lifecycle emphasis (V-02's dedicated GATE PRECONDITIONS block with verbatim
schema element names) + phrasing register (V-01's conversational Prohibition B with
C-30 causal mechanism and C-32 dual-frame negation+affirmation). V-02's gate block
provides C-31 PASS; V-01's Prohibition B structure provides C-32 PASS. The rest of
the prompt uses the formal/technical register from the R9-V-03 baseline.
**Base**: R9-V-03 (155 under v10 -- C-31 PASS, C-32 PASS)
**Hypothesis**: C-31 can be satisfied by a dedicated callout block (V-02) as well as
inline prose restatement (R9-V-03). C-32's dual-frame survives in any syntactic
arrangement where the causal mechanism precedes the negation+affirmation. Combining
these two axes produces a variation that reaches 155 via different structural choices
than R9-V-03, confirming that the criteria are property-based (schema names present,
dual-frame present) rather than phrase-pattern-based.

**Expected**: C-01..C-30 PASS (inh) + C-31 PASS (GATE PRECONDITIONS block at Phase 3
entry names "Selected?" and "all 5 rows" verbatim) + C-32 PASS (Prohibition B: "if
editing the rationale would make the comparison sentence completable... not permission
to reopen the comparison; it is the signal the swap is mandatory") = **155**

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

> **GATE PRECONDITIONS -- both must hold before Phase 3 may begin:**
> - **(a)** All 5 rows of the Peer-Comparison Registry are written in your output
> - **(b)** Selected? is blank across all 5 rows of the Registry
>
> A Registry with fewer than 5 rows does not satisfy (a). A Registry where any
> Selected? cell holds any value does not satisfy (b). Both conditions must hold
> simultaneously before any finalization step below may proceed.

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

## V-04 -- Output Format: Numbered Steps + C-31 Verbatim at Step 8 + C-32 Dual-Frame

**Axis**: Output format -- replace the Phase/Check hierarchy with sequential numbered
steps (Step 1 through Step 8). Step 8 (Finalize) opens with an explicit GATE
PRECONDITIONS block naming verbatim schema element names (Selected?, all 5 rows of the
Registry), satisfying C-31. The Rationalization Rule in Step 5b retains the C-30
causal mechanism and adds the C-32 dual-frame. This tests whether C-31 and C-32 survive
a complete structural format change -- the semantic content is equivalent, the
hierarchical architecture is different.
**Base**: R9-V-04 (155 under v10 -- C-31 PASS, C-32 PASS with "not an exit; it is
the signal the swap is mandatory")
**Hypothesis**: C-31 and C-32 are format-independent -- the schema element name
requirement and dual-frame requirement hold regardless of whether the prompt uses
Phase/Check or numbered-step architecture. V-04 uses step-labeled organization while
preserving all mandatory mechanisms. If V-04 scores 155, the numbered-step format is
a valid alternative architecture for the full criteria stack.

**Expected**: C-01..C-30 PASS (inh) + C-31 PASS (Step 8 opens with "GATE: only after
(a) all 5 rows of the Registry are written AND (b) Selected? is blank across all 5
rows") + C-32 PASS (Rationalization Rule: "if editing... would make the comparison
sentence completable... not permission to reopen... the signal the swap is mandatory")
= **155**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

---

### Step 1 -- Inertia Frame

Before generating ideas, write a paragraph (3-5 sentences) describing the current
trajectory for {{topic}}: What happens if the team makes no deliberate decision?
What is already in motion? What does the path of least resistance produce --
technically, organizationally, or for users?

This paragraph must appear as the first element in your final artifact, before any
ideas or tables.

---

### Step 2 -- Build the Idea Pool

Generate 20-40 candidates for {{topic}}. Your output must contain one labeled section
per required dimension below. These are **mandatory output sections** -- each must
appear as a `##` heading. Do not collapse them into a flat list and do not omit any.
You may add dimension sections beyond the six required.

**Required dimensions (each must appear as a `## [Dimension Name]` section):**

- **Scope** -- how much of {{topic}}'s problem space is addressed
- **Timing** -- when the intervention lands in the product lifecycle
- **Integration** -- how it connects to existing systems or teams
- **Audience** -- who benefits most
- **Build vs. Buy** -- internal build, external adoption, or extension of existing
- **Status Quo** -- the inertia option (exactly one idea: Do Nothing)

**Do not mark top-5 yet.** Generate the entire pool before selecting. Marking ideas
as you write them introduces sequential bias -- finish the pool first. Do not place
any `**` markers on any idea during Step 2.

For each idea:

```
## [Dimension Name]

### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this serves {{topic}} specifically -- cite a real constraint,
user need, or opportunity. No generic reasoning.
```

**Required**: Include **Do Nothing** in the Status Quo section. Its rationale must
extend the framing paragraph from Step 1 -- what the current trajectory concretely
produces for {{topic}}.

---

### Step 3 -- Sequential Default Check

Before proceeding, identify your 5 candidates for top-5. Are they the first 5 you
generated? If yes, rescan the full pool -- the strongest ideas surface across the
whole run. The output of Step 3 is the set of 5 candidates advancing to Step 4.

---

### Step 4 -- AMEND Draft

Write a draft AMEND section with 3 pool-shift directions. For each direction:
- Name the shift axis
- Describe what ideas would appear or disappear
- Apply the re-run test: if a reader took only this directive and re-ran the
  brainstorm, would the resulting pool contain ideas that are not in the current
  pool? Different candidate ideas, not the same ideas under different framing.

Do not finalize yet. Step 4 output is a draft; finalization happens in Step 8.

---

### Step 5 -- Peer-Comparison Registry (required output; gates Step 8)

For each of the 5 candidates from Step 3, write one row in the Registry. Do not
fill in the Selected? column yet -- it is gated by Step 5 completion.

| # | Candidate (exact name from pool) | Peer (exact name, same ## section, unmarked) | I chose [Candidate] over [Peer] because ___ | Selected? |
|---|----------------------------------|----------------------------------------------|---------------------------------------------|-----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Column rules:**
- **Candidate**: exact idea name from Step 2; one of the 5 from Step 3
- **Peer**: exact name of one specific unmarked idea in the same `##` section; cannot
  be blank; must be an idea from the Step 2 pool
- **"I chose ... because ___"**: complete the sentence -- state a specific reason tied
  to {{topic}}'s actual constraints (scope, user group, cost, risk); "it is better"
  or "more viable" do not count
- **Selected?**: Step-advance gate. This column cannot hold any value until both
  preconditions hold: (a) all 5 rows of this Registry are written in your output,
  AND (b) Selected? is blank across all 5 rows. A partial Registry has no valid
  Selected? entries. Step 8 may begin only when both conditions are satisfied. This
  is a schema property of the Registry.

**Prohibition Battery -- applies without exception:**

**Prohibition A -- Marking Ban**: Do not place any `**` marks anywhere in your
output while Step 5 is in progress -- not on headings, inline, in notes, or in any
other form. No `**` marks may appear until the complete 5-row Registry is written.

**Rationalization Rule**: If you cannot complete the comparison sentence for any row
-- no specific peer holds or no specific reason applies -- that candidate must be
replaced by the peer named in the Peer column. The replacement source is fixed: it
is the peer from this row, not an alternative selected after reconsidering. Do not
revise the candidate's rationale to manufacture a distinction that was not present
at comparison time. If editing the candidate's rationale would make the comparison
sentence completable, that desire confirms the replacement obligation applies -- the
impulse to revise so the comparison can pass is not permission to reopen the
comparison; it is the signal the swap is mandatory.

This Registry is required output. Write all 5 rows before proceeding.

---

### Step 6 -- Inertia Placement Check

Does the Step 1 framing paragraph appear as the first element in your artifact, before
any idea sections? If not, reorder. This check gates the artifact write.

---

### Step 7 -- AMEND Finalization

Review each of the 3 AMEND directions from Step 4. Apply the re-run test: would a
reader who took only this directive and re-ran the brainstorm get candidate ideas
that do not exist in the current pool? If any direction fails, sharpen it. Step 7
determines final AMEND content.

---

### Step 8 -- Finalize

> **GATE: Step 8 may begin only after both conditions hold:**
> - **(a)** All 5 rows of the Peer-Comparison Registry (Step 5) are written in your output
> - **(b)** Selected? is blank across all 5 rows of that Registry
>
> A Registry with fewer than 5 rows does not satisfy (a). Any Selected? value in any
> row does not satisfy (b). Verify both before proceeding.

Fill Selected? = YES in exactly 5 rows of the Registry (the candidates confirmed in
Step 5, with any substitutions from the Rationalization Rule applied). Mark those
same 5 ideas with `**` on their headings in the dimension sections. Use the AMEND
content finalized in Step 7.

Write the artifact to:
`simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Inertia paragraph (Step 1), then dimension sections (top-5 marked),
then Peer-Comparison Registry (Step 5), then AMEND (Step 7). Total ideas including
Do Nothing: 20-40.
```

---

## V-05 -- Inertia Framing Prominence: Status Quo First + C-31 + C-32

**Axis**: Inertia framing -- the Status Quo dimension section is elevated to the first
position in the idea pool (before Scope, Timing, etc.), with Do Nothing as the opening
idea. A dedicated Phase 0 before the main generation phase requires the inertia
trajectory to be written and named before any other ideas are produced. This tests
whether elevating inertia to a structural Phase 0 affects C-14 scoring (inertia-first
framing paragraph) and whether C-31/C-32 survive the structural reorganization. C-31
satisfied via Phase 3 verbatim gate; C-32 satisfied via Prohibition B causal dual-frame.
**Base**: R9-V-03 (155 under v10) with inertia reorganized from 1a (inline with
generation) to Phase 0 (dedicated pre-generation phase)
**Hypothesis**: C-14 requires the framing paragraph to appear before alternatives are
introduced -- Phase 0 placement satisfies this more strongly than 1a placement (which
is within the generation phase). C-31 and C-32 are unaffected by pool-ordering changes.
If V-05 scores 155, inertia promotion to Phase 0 is compatible with the full criteria
stack and represents a stronger C-14 form.

**Expected**: C-01..C-30 PASS (inh) + C-31 PASS (Phase 3 verbatim gate: "Only after
both preconditions hold -- (a) all 5 rows of this Registry written, AND (b) Selected?
blank across all 5 rows") + C-32 PASS (Prohibition B: causal mechanism + "not
permission to reopen... the signal the swap is mandatory") = **155**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

This skill runs in three phases: STATUS QUO, GENERATE, VERIFY. Do not begin GENERATE
until STATUS QUO is complete. Do not finalize the artifact until VERIFY is complete.

---

## PHASE 0 -- STATUS QUO

Before generating any alternatives, establish the inertia baseline.

Write a paragraph (3-5 sentences) for {{topic}}: What is the current trajectory?
What does the team inherit if no decision is made? What accumulates -- technically,
organizationally, or for users? What does the path of least resistance concretely
produce?

Then write exactly one idea entry under a `## Status Quo` heading:

```
## Status Quo

### Do Nothing

**Pitch**: One sentence describing the inertia path.
**Rationale**: What the current trajectory concretely produces for {{topic}} --
extend the paragraph above with specific consequences (not "doing nothing is an
option").
```

This is the only idea produced in Phase 0. Phase 1 may not begin until the Status
Quo framing paragraph and Do Nothing entry are written.

---

## PHASE 1 -- GENERATE

### 1a. Idea Pool

Generate 20-40 candidates for {{topic}} across the required dimensions below. Do not
re-enter the Status Quo section -- Do Nothing is already written. Each dimension is a
**mandatory output section** (`##` heading). Do not collapse them into a flat list and
do not omit any.

**Required dimensions (each must appear as a `## [Dimension Name]` section):**

- **Scope** -- how much of {{topic}}'s problem space is addressed
- **Timing** -- when the intervention lands in the product lifecycle
- **Integration** -- how it connects to existing systems or teams
- **Audience** -- who benefits most
- **Build vs. Buy** -- internal build, external adoption, or extension of existing

**Do not mark top-5 yet.** Complete the full pool before selecting. Marking ideas
as you write them introduces sequential bias -- the first ideas generated are not the
best, only the most recently visible.

For each idea:

```
## [Dimension Name]

### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this serves {{topic}} specifically -- cite a real constraint,
user need, or opportunity. No generic reasoning.
```

Total ideas (including Do Nothing from Phase 0): 20-40.

### 1b. AMEND Draft

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
- **Candidate**: exact idea name from Phase 0 or Phase 1; one of the 5 from Check A
- **Peer**: exact name of one specific unmarked idea in the same `##` section; cannot
  be blank
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
Does the Phase 0 framing paragraph appear as the first element in the artifact,
before the Status Quo section? If not, move it. This check gates the artifact write.

---

## PHASE 3 -- FINALIZE

Only after both preconditions hold -- (a) all 5 rows of this Registry are written
in your output, AND (b) Selected? is blank across all 5 rows -- may Phase 3 begin.
A Registry with fewer than 5 rows does not satisfy (a). A Registry where any
Selected? cell holds a value does not satisfy (b). Both must hold simultaneously.

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

Artifact order: Phase 0 framing paragraph, then Status Quo section (Do Nothing),
then remaining dimension sections (with top-5 marked), then Peer-Comparison Registry,
then AMEND. Total ideas (including Do Nothing): 20-40.
```
