---
skill: quest-variate
skill_target: draft-brainstorm
round: 7
date: 2026-03-16
rubric_version: 7
r6_scores_under_v7: "V-03 = 137.5 (C-26 borderline -- 'same ideas with different labels' present; C-25 absent), V-04 = 137.5 (C-25 PASS schema lock, C-26 FAIL no distribution-shift named), V-05 = 137.5 (C-26 PASS 'not different labels', C-25 FAIL prose batch only)"
r7_target: "140 -- achieve both C-25 (schema lock) and C-26 (distribution-shift) in isolation and in combination"
---

# Variate R7 -- draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01 through V-02), then combinations (V-03, V-04, V-05).

R7 focuses on closing the two R7 aspirational criteria introduced in rubric v7:
- **C-25** Marking-Gate Schema Lock -- the batch-completion gate (C-23) names the
  forbidden output action; C-25 closes the next loophole: a prose prohibition still
  relies on the model choosing to honor it; the schema lock encodes the selection-mark
  slot as a structural column that physically cannot be populated until all batch rows
  exist -- the gate is an output-schema property, not a behavioral instruction
- **C-26** AMEND Pool-Composition Constraint -- the re-invocability bar (C-12) requires
  a noticeably different pool when a directive is re-run; C-26 closes the label-shift
  loophole: a directive can satisfy C-12 by changing category taxonomy, emphasis, or
  framing -- producing a "different" pool in presentation but the same underlying
  candidate ideas; C-26 requires the prompt to name the distribution-shift test as the
  criterion: different IDEAS must appear, not just different labels on the same ideas

R6 gap analysis under rubric v7:

| Variation | R6 Score (v6) | C-25 under v7 | C-26 under v7 | Score under v7 |
|-----------|--------------|---------------|---------------|----------------|
| R6-V-01 (125) | 125 | FAIL (prose prohibition only; C-23 lead-frame but no schema) | FAIL | 125 |
| R6-V-02 (125) | 125 | FAIL (interrogative; C-19/C-21/C-23 absent) | FAIL | 125 |
| R6-V-03 (135) | 135 | FAIL (prose Prohibition Battery; no structural column) | BORDERLINE ("same ideas with different labels" present but distribution-shift not named as the test criterion) | 135-137.5 |
| R6-V-04 (135) | 135 | PASS (Registry Top-5? column gated by Step 2b completion -- schema lock present) | FAIL ("different rows" is not "different ideas"; distribution-shift test not named) | 137.5 |
| R6-V-05 (135) | 135 | FAIL (prose batch with governing rules; no structural column) | PASS ("different candidate distribution, not different labels on the same ideas") | 137.5 |

R7 axes selected:

| Axis | New in R7? | Used In | R7 Criterion |
|------|-----------|---------|--------------|
| Output format: structural Registry with null-gated Selected? column (schema lock) | Yes | V-01, V-03, V-05 | C-25 only (V-01); C-25+C-26 (V-03, V-05) |
| Phrasing register: AMEND distribution-shift test named as the criterion (not just re-invocability bar) | Yes | V-02, V-03, V-04, V-05 | C-26 only (V-02); C-25+C-26 (V-03, V-04, V-05) |

Root cause of R6-V-04 C-26 gap: Review B asks "would they produce a table with
different rows?" -- this satisfies C-12's re-invocability bar (noticeably different
pool) but does not name the distribution-shift test. "Different rows" could mean the
same ideas under different framing. C-26 requires the prompt to explicitly state
that "different" means different candidate ideas, not different labels on the same ideas.

Root cause of R6-V-05 C-25 gap: Check B uses numbered prose sentences ("Write all
five completed sentences as a numbered batch") with a Marking Prohibition governing
rule. The marking action is prohibited in prose, but no structural output column exists
that is null-gated by batch completeness. The gate is behavioral (model must honor the
prohibition), not architectural (schema slot cannot accept a value until rows exist).

---

## V-01 -- Output Format: Schema-Lock Registry (C-25 isolation, C-26 absent)

**Axis**: Output format -- Check B peer-comparison batch becomes a structured Registry
table with a `Selected?` column that carries a structural null condition until all 5
rows are complete; the gate is a schema property of the Registry, not a prose prohibition;
Prohibition Battery (C-23/C-24) is preserved alongside the schema lock
**Base**: R6-V-03 (prohibition battery, 135 under v6)
**Hypothesis**: R6-V-03 passes C-23/C-24 via named Prohibition Battery but uses prose
sentences for the batch. Upgrading Check B to a structural Registry table with a
null-gated Selected? column achieves C-25: the marking action is blocked by schema
completeness, not by instruction. Check C intentionally keeps basic re-invocability
language (no "different ideas" distribution-shift test) to isolate C-25. If this
variation scores 137.5, schema lock alone contributes 2.5 points independently of C-26.

**Expected**: C-01..C-24 PASS (inh) + C-25 PASS (schema Registry) + C-26 FAIL (Check C: no distribution-shift test) = **137.5**

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
Registry below. Do not fill in the Selected? column during Registry construction.

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
to manufacture a distinction that was not present at comparison time. Rationale
revision is the escape route this prohibition closes.

**Check C -- AMEND Re-Invocability** (determines final AMEND content)
For each of your 3 AMEND items: if a reader took only that directive and re-ran
this brainstorm, would they get a noticeably different pool? If not, sharpen the
directive. The output of Check C determines final AMEND content.

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

## V-02 -- Phrasing Register: Distribution-Shift AMEND Test (C-26 isolation, C-25 absent)

**Axis**: Phrasing register -- Check C is renamed and restructured as a Distribution-Shift
Test; the prompt explicitly names the criterion: AMEND directives must shift which
candidate IDEAS appear, not only how existing ideas are labeled, framed, or grouped;
the prose Prohibition Battery is preserved without structural column (C-25 absent,
intentional); the distribution-shift requirement is the only new language
**Base**: R6-V-03 (prohibition battery, 135 under v6)
**Hypothesis**: R6-V-03 passes C-12 via "noticeably different pool" re-invocability
bar and gestures toward C-26 with "same ideas with different labels" language, but
does not name the distribution-shift test as the governing criterion for AMEND
validity. V-02 replaces Check C with an explicit distribution-shift test: "different
candidate ideas, not different labels on the same ideas." This closes the loophole
C-12 leaves open without changing the batch architecture. If this variation scores
137.5, the distribution-shift test alone contributes 2.5 points independently of C-25.

**Expected**: C-01..C-24 PASS (inh) + C-25 FAIL (prose batch; no structural column) + C-26 PASS (Check C: distribution-shift named as criterion) = **137.5**

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
selecting. Marking ideas as you write them introduces sequential bias.

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
For each of your 5 picks from Check A, complete this sentence and write it in
your output:

  "I chose [Idea Name] over [name one specific unmarked idea in the same section]
   because ___."

The peer must be an existing idea from the same `##` section, named exactly. The
reason must be specific to {{topic}} -- a difference in scope, implementation cost,
user group served, or risk accepted. Generic framing does not satisfy the requirement.

Write all five completed sentences as a numbered batch.

**Prohibition Battery -- two prohibitions govern Check B and apply without exception:**

**Prohibition A -- Marking Ban**: Do not place any `**` marks anywhere in your
output while Check B is in progress. The marking action is what is prohibited --
not just deferred. No `**` marks on headings, inline, in notes, or in any other
position may appear until the complete numbered batch of five sentences exists in
your output. Phase 3 may begin only when all five sentences are present.

**Prohibition B -- Rationalization Block**: If you cannot complete the sentence
for any pick -- no specific peer comes to mind or no specific reason holds -- that
pick must be replaced with the specific peer you attempted to name in this
comparison. The replacement source is fixed as that peer, not a different idea
selected after reconsidering. Do not revise the pick's rationale after Check B to
manufacture a distinction that was not already present at comparison time. Rationale
revision is the escape route this prohibition closes.

**Check C -- AMEND Distribution-Shift Test** (determines final AMEND content)

Each AMEND directive must pass the distribution-shift test: re-running this
brainstorm with only this directive must surface candidate ideas that would not
have appeared in the original pool -- different ideas, not different labels on
the same ideas. A directive is valid only if the underlying candidate set changes:
new ideas enter, existing ideas exit, or the pool composition shifts materially.
A directive that changes only category names, emphasis framing, or grouping
taxonomy without introducing different underlying candidates fails this test.

For each of your 3 AMEND items, ask: if a reader took only this directive and
re-ran the brainstorm, would the pool contain ideas that did not appear in the
current pool? If the answer is "probably the same ideas under a different frame,"
sharpen the directive until it passes the distribution-shift test. The output
of Check C determines final AMEND content.

**Check D -- Inertia Paragraph** (gates artifact write)
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. This check gates the artifact write.

---

## PHASE 3 -- FINALIZE

Mark exactly 5 ideas with `**` on their heading (informed by Check A and B, with
any substitutions from Prohibition B applied). Update AMEND items if Check C
required changes.

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
then Check B sentences, then AMEND. Total ideas (including Do Nothing): 20-40.
```

---

## V-03 -- Output Format + Phrasing Register: Schema-Lock Registry + Distribution-Shift (C-25+C-26 combined, Prohibition Battery base)

**Axes**: Output format (schema-lock Registry for Check B, C-25) + phrasing register
(distribution-shift test named as AMEND criterion, C-26); compact prohibition-battery
style preserved; V-01 and V-02 combined into a single variation
**Base**: R6-V-03 (prohibition battery, 135 under v6)
**Hypothesis**: V-01 confirms C-25 at +2.5 and V-02 confirms C-26 at +2.5 independently.
V-03 combines both on the same compact base: Check B becomes the structural Registry
(C-25) and Check C becomes the distribution-shift test (C-26). The Prohibition Battery
is preserved as a named constraint block within Check B. If both pass together, V-03
should score 140.

**Expected**: C-01..C-24 PASS (inh) + C-25 PASS (schema Registry) + C-26 PASS (Check C distribution-shift) = **140**

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
  tied to {{topic}}'s actual constraints; "it is better" or "more viable" do not count
- **Selected?**: Schema null constraint. This column cannot hold any value until
  all 5 rows of this Registry are complete. A partial Registry has no valid Selected?
  entries. Phase 3 may begin and Selected? may be filled only when all 5 rows exist.

**Prohibition Battery -- two prohibitions govern Check B and apply without exception:**

**Prohibition A -- Marking Ban**: Do not place any `**` marks anywhere in your
output while Check B is in progress. The marking action is what is prohibited --
not just deferred. No `**` marks on headings, inline, in notes, or in any form
may appear until the complete 5-row Registry exists in your output.

**Prohibition B -- Rationalization Block**: If you cannot complete the sentence
for any row -- no specific peer or no specific reason holds -- that candidate must
be replaced by the specific peer you attempted to name in the Peer column. The
replacement source is fixed: the peer from this row, not a different idea selected
after reconsidering. Do not revise the candidate's rationale after Check B to
manufacture a distinction that was not present at comparison time. Rationale revision
is the escape route this prohibition closes.

**Check C -- AMEND Distribution-Shift Test** (determines final AMEND content)

Each AMEND directive must pass the distribution-shift test: re-running this
brainstorm with only this directive must surface candidate ideas that would not
have appeared in the original pool -- different ideas, not different labels on
the same ideas. A directive is valid only if the underlying candidate set changes.
A directive that shifts only category names, framing emphasis, or grouping taxonomy
without introducing different underlying candidates fails this test.

For each of your 3 AMEND items, ask: would re-running with this directive produce
ideas that do not appear in the current pool? If the answer is "probably the same
ideas under a different frame," sharpen the directive until re-running produces a
materially different candidate set. The output of Check C determines final AMEND content.

**Check D -- Inertia Paragraph** (gates artifact write)
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. This check gates the artifact write.

---

## PHASE 3 -- FINALIZE

Fill Selected? = YES in exactly 5 rows of the Registry (candidates confirmed, with
any substitutions from Prohibition B applied). Mark those same 5 ideas with `**`
on their headings in the dimension sections. Update AMEND if Check C required changes.

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

## V-04 -- Output Format + Lifecycle Emphasis: Schema Registry + Explicit Distribution-Shift (R6-V-04 lineage + C-26)

**Axes**: Output format (schema Registry already present from R6-V-04, C-25 inherited) +
lifecycle emphasis (AMEND step receives an explicit distribution-shift requirement as a
named criterion in both Review B and Step 5, closing C-26); minimal change -- the single
gap in R6-V-04 is that Review B asks "would they produce different rows" (C-12 only)
rather than "would different candidate ideas appear" (C-26)
**Base**: R6-V-04 (schema registry with named prohibition blocks, 137.5 under v7)
**Hypothesis**: R6-V-04 already scores 137.5 under v7 (C-25 PASS via structural Top-5?
column gated by Step 2b, C-26 FAIL). The only change needed is to update Review B and
Step 5's AMEND conditions with the distribution-shift test: "different candidate ideas,
not different rows under a different label." This is the minimum viable change to reach 140.

**Expected**: C-01..C-24 PASS (inh) + C-25 PASS (inh from R6-V-04 schema Registry) + C-26 PASS (Review B + Step 5 distribution-shift language) = **140**

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
  be filled only after the Pre-Selection Batch Registry (Step 2b) is fully complete.
  Marking during construction introduces sequential bias.

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
prohibited until all 5 rows of this Registry are complete. Step 3 is gated by
this section: no selection marks of any kind may appear before all 5 rows exist.

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

**If the sentence column cannot be completed** with a specific reason for any row,
apply the following two rules:

**Rule 1 -- Source Lock**: The `**YES**` mark for that candidate must go to the
idea named in the Attempted Peer column of that row. The replacement source is
fixed: it is the Attempted Peer from this row -- not a different idea you prefer
after reconsidering, not the next most viable from another Dimension. The Attempted
Peer named here is the only permissible replacement source.

**Rule 2 -- Rationalization Block**: Do not revise the original Candidate row's
Rationale field in the idea table after completing the Registry. Rationale revision
is the escape route this rule closes: if editing the Candidate's Rationale would
make the comparison sentence completable, that desire confirms the substitution
obligation applies. Once a Registry row is written, the comparison is final on the
Rationale as it exists. No post-Registry Rationale edits are permitted as a
mechanism to avoid a mandated substitution.

This Registry is required output. The artifact is incomplete without all 5 rows.

---

### Step 3 -- Mark Top-5 (gated by Step 2b completion)

Only after Step 2b is fully written: fill in `**YES**` in exactly 5 rows' Top-5?
column, using the candidates confirmed in the Registry. If any substitution was
required in Step 2b, the substituted peer's row receives the `**YES**` mark.

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

## V-05 -- Role Sequence + Output Format: Full Stack Architecture with Schema-Lock Registry (R6-V-05 lineage + C-25)

**Axes**: Role sequence (5-layer architecture from R6-V-05 preserved, C-26 inherited
from Check C "not different labels") + output format (Check B batch upgraded from
prose sentences to structural Verification Registry with null-gated Selected? column,
achieving C-25); C-26 already present in R6-V-05's Check C; the only change is the
structural upgrade to the batch format in Layer 3
**Base**: R6-V-05 (layered architecture with governing rules, 137.5 under v7)
**Hypothesis**: R6-V-05 already scores 137.5 under v7 (C-26 PASS via "different
candidate distribution, not different labels on the same ideas" in Check C; C-25 FAIL
because Check B uses numbered prose sentences with prose Marking Prohibition). Upgrading
Check B to a Verification Registry table with a structurally null-gated Selected? column
closes C-25. No changes to AMEND, Layer 0, Layer 1, or Layer 2. The schema upgrade is
the minimum change to reach 140.

**Expected**: C-01..C-24 PASS (inh) + C-25 PASS (Verification Registry schema) + C-26 PASS (inh from R6-V-05) = **140**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

Your task: map the full option space across 7 required dimensions, then select the
5 most viable candidates through a gated verification process. Do not finalize the
artifact until all verification gates are passed.

---

## Layer 0 -- Status Quo Baseline

Before opening any dimension, write a paragraph (3-5 sentences) that describes the
current state of {{topic}}: What is in motion today? What does the team inherit if
no explicit decision is made? What risks or missed opportunities compound by default?

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
addressed -- from the minimal viable slice to the comprehensive overhaul.

**Dimension 2 -- Timing**: Ideas vary when intervention happens -- early bets,
staged rollouts, deferred commitments, just-in-time decisions.

**Dimension 3 -- Integration**: Ideas vary how the solution connects to existing
systems, platforms, or external dependencies relevant to {{topic}}.

**Dimension 4 -- Audience**: Ideas vary who the primary beneficiary is -- different
user segments, internal teams, or downstream consumers of {{topic}}'s output.

**Dimension 5 -- Build vs. Buy**: Ideas vary how capability is acquired -- built
internally, adopted from outside, extended from existing components, or delegated.

**Dimension 6 -- Risk Profile**: Ideas vary how much uncertainty is accepted --
conservative incremental bets vs. high-variance, high-ceiling bets.

**Dimension 7 -- Status Quo (mandatory)**: Contains exactly one idea: **Do Nothing**.
Its pitch and rationale describe the current trajectory from Layer 0. What does the
team concretely get -- and give up -- by staying the course on {{topic}}?

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
governed by two named prohibitions below)

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
- **Selected?**: Structural null constraint. This column cannot hold any value until
  all 5 rows of this Registry are complete. A Registry with fewer than 5 rows has
  no valid Selected? entries -- this is a property of the Registry schema, not a
  deferred instruction. Layer 4 may begin only when all 5 rows exist and Selected?
  is blank across all rows.

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
was not present at comparison time. Rationale revision is the escape route this
prohibition closes. If you want to edit the rationale, treat that impulse as
confirmation that the replacement obligation applies.

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

Only after all four checks in Layer 3 are complete:

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

Artifact order: Layer 0 paragraph -> 7 dimension sections (top-5 marked) ->
Verification Registry -> AMEND. Total ideas (including Do Nothing): 20-40.
```

---

## Rubric Coverage Analysis -- R7

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 volume (20-40) | "20-40 candidates" | same (inh) | same (inh) | "20-40 rows total" | "20-40" |
| C-02 idea anatomy | Per-idea block (4 fields) | same (inh) | same (inh) | Table columns (Name/Pitch/Dimension/Rationale) | Per-idea block |
| C-03 top-5 marker | `**` heading prefix (Phase 3) + Selected?=YES in Registry | same (inh, heading only) | same as V-01 | `**YES**` in Top-5? col (Step 3) | `**` heading + Selected?=YES |
| C-04 inertia check | Status Quo required section + trajectory rationale | same (inh) | same (inh) | Status Quo row + Preamble | Dim 7 mandatory + Layer 0 |
| C-05 AMEND (3 items) | 1c draft + Check C | same (inh) | same (inh) | Step 5 output of Review B | Layer 2 draft + Check C |
| C-06 category grouping | Required `##` sections per dimension | same (inh) | same (inh) | Category View (Step 4, required structural output) | 7 dimension `##` headers |
| C-07 rationale specificity | "cite real constraint; no generic reasoning" | same (inh) | same (inh) | "cite specific constraint; 'provides value' not a rationale" | "name real constraint; topic-specific" |
| C-08 category diversity | 6 required dimensions | same (inh) | same (inh) | 7 required dimension types | 7 named dimensions |
| C-09 AMEND actionability | Check C re-invocability test | Check C distribution-shift test (stronger) | same as V-02 | Review B + Step 5 distribution-shift (stronger) | Check C distribution-shift |
| C-10 top-5 defensibility | Check A + Registry + batch gate | Check A + Check B sentences + batch gate | Check A + Registry + Prohibition Battery | Review A + Registry + Rules 1/2 | Check A + Verification Registry |
| C-11 sequential-default guard | "Do not mark top-5 yet" + Phase 1b imperative | same (inh) | same (inh) | "Leave Top-5? blank during Step 1" | "Do not mark any idea... in this layer" |
| C-12 re-runnability bar | Check C: "noticeably different pool" | Check C: distribution-shift test (exceeds C-12) | same as V-02 | Review B: distribution-shift test (exceeds C-12) | Check C: "different candidate distribution" |
| C-13 category dimension taxonomy | 6 named dimensions with descriptions | same (inh) | same (inh) | 7 named dimension types with descriptions | 7 named dimensions with descriptions |
| C-14 inertia-first framing paragraph | 1a: "appears at top... precedes all ideas" | same (inh) | same (inh) | Preamble: "must appear before the idea table" | Layer 0: "must appear first" |
| C-15 structural spine guarantee | PASS: 6 required `##` sections; "do not collapse; do not omit" | same (inh) | same (inh) | PASS: Category View "required structural output" | PASS: 7 dimension `##` headers mandated |
| C-16 generation-phase sequential guard | PASS: "Do not mark top-5 yet" in Phase 1b, imperative | same (inh) | same (inh) | PASS: "Leave Top-5? blank during Step 1" -- construction phase | PASS: "Do not mark any idea with `**` in this layer" -- Layer 1 |
| C-17 peer-comparison defensibility test | PASS: Registry "I chose [Candidate] over [Peer] because ___" column | PASS (inh): "complete this sentence and write it in your output" | PASS: Registry same as V-01 | PASS (inh): Registry "I chose [Candidate] over [Peer] because ___" | PASS: Registry "I chose [Candidate] over [Peer] because ___" |
| C-18 self-review phase integration | PASS: Check A -> Registry; Registry -> Phase 3; Check C -> AMEND; Check D -> artifact | same (inh) | same (inh) | PASS: Review A -> Step 2b; Review B -> Step 5; Step 2b -> Step 3 | PASS: Check A -> "candidates that advance"; Check B -> "final top-5 marks"; Check C -> "final AMEND content"; Check D -> gates write |
| C-19 peer-test imperative form | PASS: Registry row completion enforces sentence materialization (structural) | PASS (inh): "complete this sentence and write it in your output" | PASS: Registry enforces materialization | PASS (inh): Registry row completion | PASS: Registry row completion |
| C-20 peer-test consequence clause | PASS (inh): Prohibition B: "must be replaced by the specific peer" | PASS (inh): Prohibition B: "must be replaced with the specific peer" | PASS (inh): Prohibition B | PASS (inh): Rule 1: "`**YES**` mark must go to idea named in Attempted Peer column" | PASS (inh): Rationalization Prohibition: "must be replaced with the specific peer" |
| C-21 peer-test batch-completion gate | PASS: "Phase 3 may begin... only when all 5 rows exist in your output" | PASS (inh): "Phase 3 may begin only when all five sentences are present" | PASS: "Phase 3 may begin... only when all 5 rows exist" | PASS (inh): "Step 3 is gated by this section: no selection marks... before all 5 rows exist" | PASS: "Layer 4 may begin only when all 5 rows exist" |
| C-22 consequence replacement source | PASS (inh): Prohibition B: "the peer from this row, not a different idea selected after reconsidering" | PASS (inh): Prohibition B: "replacement source is fixed as that peer" | PASS (inh): Prohibition B | PASS (inh): Rule 1: "The Attempted Peer from this row -- not a different idea you prefer after reconsidering" | PASS (inh): "The replacement source is fixed: it is the peer from this row" |
| C-23 selection-phase marking prohibition | PASS: Prohibition A: "Do not place any `**` marks anywhere... The marking action is what is prohibited -- not just deferred" | PASS (inh): Prohibition A same | PASS: Prohibition A | PASS (inh): "Do not place any `**YES**` values, `**` marks... The marking action is prohibited" | PASS (inh): "Marking Prohibition: No `**` marks may appear... The marking action is prohibited -- not deferred" |
| C-24 post-comparison rationalization block | PASS (inh): Prohibition B: "Do not revise the candidate's rationale after Check B... Rationale revision is the escape route this prohibition closes" | PASS (inh): Prohibition B same | PASS (inh): Prohibition B | PASS (inh): Rule 2: "Rationale revision is the escape route this rule closes" | PASS (inh): "Rationale revision is the escape route this prohibition closes" |
| **C-25 marking-gate schema lock** | **PASS**: Selected? column "cannot hold any value until all 5 rows of this Registry are complete -- this is a schema constraint of the Registry, not a deferred choice" | **FAIL**: prose batch + Prohibition A; no structural column (intentional isolation) | **PASS**: Selected? column "Schema null constraint. This column cannot hold any value until all 5 rows of this Registry are complete" | **PASS** (inh): Top-5? column in idea table gated by Step 2b -- "the Top-5? column will be filled only after the Pre-Selection Batch Registry (Step 2b) is fully complete" | **PASS**: Selected? column "Structural null constraint. This column cannot hold any value until all 5 rows of this Registry are complete -- this is a property of the Registry schema" |
| **C-26 AMEND pool-composition constraint** | **FAIL**: Check C: "noticeably different pool" only; no distribution-shift test (intentional isolation) | **PASS**: Check C Distribution-Shift Test: "must surface candidate ideas that would not have appeared in the original pool -- different ideas, not different labels on the same ideas" | **PASS**: Check C: "different ideas, not different labels on the same ideas... A directive that shifts only category names, framing emphasis, or grouping taxonomy... fails this test" | **PASS**: Review B + Step 5: "different candidate ideas, not different rows under a different label... different ideas enter the pool"; Step 5 (c): "distribution-shift guarantee -- re-running must surface candidate ideas that would not appear in the original table; different ideas, not different labels" | **PASS** (inh): Check C: "different candidate distribution, not different labels on the same ideas... new ideas enter, or existing ideas are clearly displaced by ideas that were absent" |

**Projected scores:**

| Variation | C-01..C-24 | C-25 | C-26 | Projected |
|-----------|-----------|------|------|-----------|
| R7-V-01 | 135 (all pass) | PASS (schema Registry) | FAIL (no distribution-shift) | **137.5** |
| R7-V-02 | 135 (all pass) | FAIL (prose batch) | PASS (distribution-shift named) | **137.5** |
| R7-V-03 | 135 (all pass) | PASS (schema Registry) | PASS (distribution-shift named) | **140** |
| R7-V-04 | 135 (all pass) | PASS (inh R6-V-04) | PASS (Review B + Step 5) | **140** |
| R7-V-05 | 135 (all pass) | PASS (Verification Registry) | PASS (inh R6-V-05) | **140** |

**C-25/C-26 mechanism comparison:**

| Variation | C-25 Mechanism | C-26 Mechanism |
|-----------|---------------|----------------|
| V-01 | Registry Selected? column: "cannot hold any value until all 5 rows complete -- schema constraint, not deferred choice" | None (Check C: basic re-invocability bar only) |
| V-02 | None (prose Prohibition A; no structural column) | Check C Distribution-Shift Test: "different ideas, not different labels... A directive that shifts only category names... fails this test" |
| V-03 | Registry Selected? column: "Schema null constraint. This column cannot hold any value until all 5 rows complete" | Check C: "different ideas, not different labels... shifts only category names... fails this test" |
| V-04 | Idea table Top-5? column gated by Step 2b Registry completion (inh R6-V-04 schema) | Review B + Step 5: "different candidate ideas, not different rows under a different label"; Step 5 (c) "distribution-shift guarantee" |
| V-05 | Verification Registry Selected? column: "Structural null constraint... property of the Registry schema" | Check C: "different candidate distribution, not different labels... new ideas enter, or existing ideas are clearly displaced" (inh R6-V-05) |

**R7 design insight:** R6 demonstrated that C-23 and C-24 can be achieved independently
(V-01 isolated C-23, V-02 isolated C-24) and combined (V-03/V-04/V-05 hit 135). R7
follows the same isolation-then-combination structure for C-25 and C-26. V-01 and V-02
confirm the two criteria are orthogonal: schema lock does not require distribution-shift
language, and distribution-shift language does not require a structural column. V-03
demonstrates the simplest combination (compact, check-based). V-04 demonstrates the
minimum-viable upgrade path from a 137.5 baseline (R6-V-04): one targeted edit to
Review B + Step 5 is sufficient for +2.5. V-05 demonstrates the same for the other
137.5 baseline (R6-V-05): upgrading Check B from prose sentences to a structural
Registry table is sufficient for +2.5. All three combination variations reach 140 via
different architectural paths: Prohibition Battery (V-03), Schema Registry (V-04),
Layered Architecture (V-05).
