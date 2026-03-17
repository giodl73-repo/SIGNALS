---
skill: quest-variate
skill_target: draft-brainstorm
round: 6
date: 2026-03-16
rubric_version: 6
r5_best: V-03 = 132.5 (C-23 PASS, C-24 pending), V-04 = 135 projected, V-05 = 135 projected
r6_target: 135 -- confirm C-23 (marking-prohibition-led gate) and C-24 (rationalization block) in isolation and combination
---

# Variate R6 -- draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R6 focuses on closing the two R6 aspirational criteria introduced in rubric v6:
- **C-23** Selection-Phase Marking Prohibition -- the batch-completion gate (C-21)
  must name the forbidden output action (placing `**` marks) explicitly, not only
  specify write order; "write all five before marking" satisfies C-21 but not C-23
  unless the instruction frames the MARKING ACTION ITSELF as the thing that is banned
- **C-24** Post-Comparison Rationalization Block -- the consequence clause (C-22)
  must explicitly close the escape route where a model rewrites the marked idea's
  rationale post-comparison to manufacture a distinction that makes the swap unnecessary;
  fixing the replacement source (C-22) does not block this; the rationalization
  escape must be named and prohibited as a distinct action

R5 gap analysis going into R6:

| Variation | C-23 | C-24 | R5 Score (under v6) |
|-----------|------|------|---------------------|
| R5-V-01 (125) | PASS ("do not place any `**` marks anywhere until all five Check B sentences appear in your output" -- marks the forbidden action) | FAIL (no consequence clause; C-20 prerequisite absent) | 125 |
| R5-V-02 (125) | FAIL (interrogative form; C-19 prerequisite absent) | PASS ("Do not revise the marked idea's rationale to manufacture a distinction") | 125 |
| R5-V-03 (132.5) | PASS ("the Top-5? column cannot contain any entry until all 5 rows of this Registry are filled" -- column-level marking prohibition) | PENDING ("Do not revise the original candidate's rationale to manufacture a distinction" present in prose; pending validation whether column-schema context satisfies C-24's named prohibition requirement) | 132.5 |
| R5-V-04 (135 projected) | PASS ("do not place any `**` marks until all five Check B sentences appear in your output") | PASS ("Do not revise the pick's rationale to manufacture a distinction") | 135 |
| R5-V-05 (135 projected) | PASS ("do not place any `**` marks -- until the full batch of five sentences appears in your output") | PASS ("Do not revise the candidate's rationale to manufacture a distinction") | 135 |

R6 axes selected:

| Axis | New in R6? | Used In | R6 Criterion |
|------|-----------|---------|--------------|
| Phrasing register: marking-prohibition-led (name the forbidden action as the opening frame, not a subordinate clause) | Yes | V-01 | C-23 only |
| Lifecycle emphasis: two-step prohibition block (Source Lock + Rationalization Block as labeled anti-patterns with explicit escape-route naming) | Yes | V-02 | C-24 only |
| Phrasing register + lifecycle emphasis: dedicated Prohibition Battery within Check B (two named prohibitions as standalone titled blocks) | Combo | V-03 | C-23+C-24 |
| Output format: schema architecture with marking-action prohibition and post-registry rationalization lock as named schema rules | Combo | V-04 | C-23+C-24 in schema (fixes R5-V-03 C-24 ambiguity) |
| Role sequence: clean 5-layer architecture with marking prohibition and rationalization block named as the two governing rules of the batch gate | Combo | V-05 | C-23+C-24, full stack |

Root cause of R5-V-03 C-24 gap: R5-V-03 includes "Do not revise the original
candidate's rationale to manufacture a distinction" in the substitution-rules block.
However, the schema context embeds this as the final clause of a multi-sentence
rule block, and the phrase is preceded by structural rules about column values.
C-24 requires the rationalization escape to be explicitly named and closed as its
own prohibition. In schema context, a prohibition embedded as "and also do not"
at the end of a structural rule may not satisfy "explicitly prohibits rationale
revision as a mechanism to avoid a mandated swap." R6-V-04 fixes this by adding a
named **Rationalization Block** rule as a standalone labeled item after the Registry.

---

## V-01 -- Phrasing Register: Marking-Prohibition-Led Gate (C-23 isolation)

**Axis**: Phrasing register -- restructure Check B so the marking prohibition is the
LEAD sentence and primary frame, not a subordinate clause inside the batch instruction;
batch sequencing is stated as the mechanism that enforces the prohibition
**Base**: R5-V-01 (passes C-15..C-19, C-21, C-23; fails C-20)
**Hypothesis**: R5-V-01 states: "Phase 3 is gated by batch completion: do not place
any `**` marks anywhere until all five Check B sentences appear in your output."
The prohibition on marks IS present, but it arrives after the batch instruction --
"write the batch, then the prohibition follows." The C-23 pattern asks whether the
prohibition can be even more explicit when it LEADS the check: "Marking is prohibited
during this check. Do not place any `**` marks... The marking action is the thing
that is prohibited." This makes the forbidden action the first thing named, and the
sequencing requirement the mechanism rather than the primary instruction. Consequence
clause is deliberately absent to isolate C-23; if marking-prohibition-led language
passes C-23 without consequence, the prohibition alone is sufficient.

**Expected**: C-15..C-19 PASS (inh) + C-20 FAIL (no consequence) + C-21 PASS +
C-22 FAIL (C-20 prerequisite absent) + C-23 PASS + C-24 FAIL (C-20 prerequisite absent) = **125**

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
and describe what changes. Do not finalize yet -- the verification step will
check these.

---

## PHASE 2 -- VERIFY

Before writing the final artifact, complete all 4 checks in order. Each check is
explicitly connected to a downstream output decision -- do not skip.

**Check A -- Sequential Default** (determines top-5 candidates for Check B)
Look at the 5 ideas you are considering for top-5. Are they the first 5 ideas
you generated? If yes, rescan the full pool -- the best ideas are rarely the
first ones written. Select the 5 most immediately actionable. The output of
Check A is the set of 5 candidates that advance to Check B.

**Check B -- Top-5 Defensibility** (determines top-5 marks in Phase 3)

**Marking is prohibited during this entire check.** Do not place any `**` marks
anywhere in your output -- on headings, inline, in notes, or in any other form --
until all five Check B sentences are written. The marking action is the thing
that is prohibited. This is not a sequencing instruction that permits marks after
completing individual sentences; no mark of any kind may appear until the complete
numbered batch of five sentences exists in your output.

For each of your 5 picks from Check A, complete this sentence and write it in
your output:

  "I chose [Idea Name] over [name one specific unmarked idea in the same section]
   because ___."

The peer must be an existing idea from the same `##` section, named exactly. The
reason must be specific to {{topic}} -- a difference in scope, implementation cost,
user group served, or risk accepted. "It is more actionable" or "better aligned"
do not satisfy the requirement.

Write all five completed sentences as a numbered Check B Batch. The batch is the
gate: Phase 3 may begin and marks may be placed only when all five sentences are
present.

**Check C -- AMEND Re-Invocability** (determines final AMEND content)
For each of your 3 AMEND items: if a reader took only that directive and re-ran
this brainstorm, would they get a noticeably different pool? If the answer is
"probably the same ideas with different labels," sharpen the directive until each
amendment produces a clearly different candidate distribution. The output of
Check C determines final AMEND content.

**Check D -- Inertia Paragraph** (gates artifact write)
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. The paragraph is not optional and must precede alternatives.
This check gates the artifact write.

---

## PHASE 3 -- FINALIZE

Mark exactly 5 ideas with `**` on their heading (informed by Check A and B).
Update AMEND items if Check C required changes.

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
then Check B Batch sentences, then AMEND. Total ideas (including Do Nothing): 20-40.
```

---

## V-02 -- Lifecycle Emphasis: Two-Step Prohibition Block (C-24 isolation)

**Axis**: Lifecycle emphasis -- restructure the consequence clause into two explicitly
named prohibition blocks: (1) Source Lock (C-22) and (2) Rationalization Block (C-24);
the rationalization escape route is named as the thing being closed, not an afterthought;
interrogative form preserved to isolate C-24 from C-19/C-21/C-23
**Base**: R5-V-02 (passes C-15..C-18, C-20, C-22, C-24; fails C-19)
**Hypothesis**: R5-V-02's C-24 language is "Do not revise the marked idea's rationale
to manufacture a distinction." This is present and correct, but the phrase arrives
at the end of a single-block consequence paragraph. C-24 requires the escape route
to be explicitly named and closed. The two-step prohibition block makes both the
source lock and the rationalization block visually and structurally distinct --
each has a label and a complete statement. "**Prohibition 2 -- Rationalization Block**:
...Rationale revision is not a valid alternative to the replacement; it is the escape
route that this prohibition closes." This framing makes the escape route the primary
subject of the prohibition rather than an embedded qualifier. Interrogative form is
preserved ("can you complete") to isolate C-24: source-specificity + rationalization-
block must pass C-24 regardless of whether the sentence form is imperative.

**Expected**: C-15..C-18 PASS (inh) + C-19 FAIL (interrogative) + C-20 PASS (inh) +
C-21 FAIL (C-19 prerequisite absent) + C-22 PASS + C-23 FAIL (C-19 prerequisite absent)
+ C-24 PASS = **125**

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

**Do not mark top-5 yet.** Complete the full pool across all sections before selecting.

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

**Check A -- Sequential Default** (determines top-5 candidates for Check B)
Look at the 5 ideas you are considering for top-5. Are they the first 5 ideas
you generated? If yes, rescan the full pool -- the best ideas are rarely the
first ones written. The output of Check A is the set of 5 candidates that advance
to Check B.

**Check B -- Top-5 Defensibility** (determines top-5 marks in Phase 3)
For each of your 5 picks, can you complete this sentence: "I chose this over
[name one specific unmarked idea in the same section] because ___"?

Name the alternative by its exact idea name from the same `##` section. State
the reason specifically -- a different scope, risk profile, implementation
requirement, or user group. Generic quality framing ("it is more aligned") does
not pass the test.

If you cannot name a specific peer or state a specific reason for any marked idea,
apply the following two prohibitions without exception:

**Prohibition 1 -- Source Lock**: That idea must be replaced. The replacement
source is fixed: it is the specific peer you attempted to name in this comparison --
not a different idea you prefer after reconsidering the pool, not the next most
viable candidate from another section, not a fresh selection from the full list.
The peer you attempted to name in this specific Check B test for this specific
candidate is the only permissible replacement source.

**Prohibition 2 -- Rationalization Block**: Do not revise the failing idea's
rationale to manufacture a distinction that was not already present at the time of
comparison. If you want to rewrite the rationale to make the comparison hold, that
impulse is evidence the replacement obligation applies. Once Check B is applied to
a candidate, the comparison stands on what was written at comparison time. Rationale
revision is not a valid alternative to the replacement -- it is the escape route
that this prohibition closes.

**Check C -- AMEND Re-Invocability** (determines final AMEND content)
For each of your 3 AMEND items: if a reader took only that directive and re-ran
this brainstorm, would they get a noticeably different pool? If the answer is
"probably the same ideas with different labels," sharpen the directive. The output
of Check C determines final AMEND content.

**Check D -- Inertia Paragraph** (gates artifact write)
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. This check gates the artifact write.

---

## PHASE 3 -- FINALIZE

Mark exactly 5 ideas with `**` on their heading (informed by Check A and B, with
any substitutions from Check B applied). Update AMEND items if Check C required
changes.

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
then AMEND. Total ideas (including Do Nothing): 20-40.
```

---

## V-03 -- Phrasing Register + Lifecycle: Named Prohibition Battery (C-23+C-24 combined)

**Axes**: Phrasing register (marking prohibition as named Prohibition A) + lifecycle
emphasis (rationalization block as named Prohibition B) -- both prohibitions stated
as standalone labeled blocks within a dedicated Prohibition Battery; each prohibition
is a complete statement with a label, the thing prohibited, and the reason the
prohibition exists
**Base**: R5-V-04 (passes C-15..C-22; projected 130)
**Hypothesis**: R5-V-04 passes C-23 ("do not place any `**` marks until all five
Check B sentences appear in your output") and C-24 ("Do not revise the pick's rationale
to manufacture a distinction") but both prohibitions are embedded within a continuous
prose paragraph in Check B. The risk: under scoring, the evaluator may note both are
present but both are subordinate clauses rather than primary-named constraints. V-03
isolates each prohibition as its own titled block within a Prohibition Battery section,
making each a structurally distinct constraint: "**Marking Ban** (Prohibition A):..."
and "**Rationalization Block** (Prohibition B):..." This removes all ambiguity about
whether the prohibited actions are named -- each block's subject is the action being
forbidden, stated as its label.

**Expected**: C-15..C-22 PASS (inh) + C-23 PASS (Marking Ban block names the action)
+ C-24 PASS (Rationalization Block names the escape route) = **135**

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

**Prohibition Battery -- the following two prohibitions govern Check B and apply
without exception:**

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
revision is the escape route this prohibition closes; if the comparison does not
hold on the rationale as written, the replacement is mandatory.

**Check C -- AMEND Re-Invocability** (determines final AMEND content)
For each of your 3 AMEND items: if a reader took only that directive and re-ran
this brainstorm, would they get a noticeably different pool? If the answer is
"probably the same ideas with different labels," sharpen the directive until each
amendment produces a clearly different candidate distribution. The output of
Check C determines final AMEND content.

**Check D -- Inertia Paragraph** (gates artifact write)
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. The paragraph is not optional and must precede alternatives.
This check gates the artifact write.

---

## PHASE 3 -- FINALIZE

Mark exactly 5 ideas with `**` on their heading (informed by Check A and B, with
any substitutions from Check B applied). Update AMEND items if Check C required
changes.

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

## V-04 -- Output Format: Schema Registry with Named Prohibition Blocks (C-23+C-24 in schema)

**Axes**: Output format -- upgrade R5-V-03's Pre-Selection Batch Registry to close
both the C-23 ambiguity (column-gate present but marking action not explicitly named
as forbidden) and the C-24 gap (rationalization prohibition embedded in prose as a
final clause, not a named standalone rule); fix by adding a labeled **Marking Ban**
statement and a labeled **Rationalization Block** as named schema rules after the
Registry
**Base**: R5-V-03 (passes C-15..C-23; C-24 pending -- "Do not revise the original
candidate's rationale" present but may be ambiguous as an embedded final clause)
**Hypothesis**: R5-V-03's C-24 gap: the phrase "Do not revise the original candidate's
rationale to manufacture a distinction" appears as the last clause of the substitution
rules block ("...and the replacement source is the Attempted Peer named here"). In schema
context, this trailing clause may not satisfy C-24's requirement that the rationalization
escape route is named and closed as a distinct prohibition. V-04 adds a **Rationalization
Block** as its own labeled rule after the Registry, making the escape route the explicit
subject of a named prohibition. Additionally, the marking prohibition is upgraded from
the column-gate description ("Top-5? column cannot contain any entry") to an explicit
named-action prohibition that covers any form of selection mark, not just the column.

**Expected**: C-15..C-23 PASS (inh/upgrade) + C-24 PASS (named Rationalization Block)
= **135**

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
- **Top-5?**: Leave this column **blank during Step 1.** Do not fill in Top-5?
  values as you build the table. The Top-5? column will be filled only after the
  Pre-Selection Batch Registry (Step 2b) is fully complete. Marking during
  construction introduces sequential bias.

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

**Review B -- AMEND Re-Invocability** (determines AMEND content in Step 5)
For each of your 3 AMEND directives: if a reader took only that directive and
re-ran the brainstorm, would they produce a table with different rows? If not,
sharpen the directive. This review determines final AMEND content.

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

**If the Attempted Peer column cannot be filled** for any row (no unmarked row
exists in the same Dimension), that candidate is not eligible for a top-5 mark.
Remove it and add the next strongest candidate from a Dimension with an available
peer.

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
`## [Dimension Name]` section. This is required structural output -- a flat list
fails.

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
(c) is re-invocable -- a reader can re-run the brainstorm from this directive and
    produce a noticeably different table without additional clarification.

```
## AMEND

1. **[Direction label]** -- [Rows that enter, exit, or re-rank. Why table looks
   different. Re-runnable with this directive alone.]
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

## V-05 -- Role Sequence: Clean 5-Layer Architecture with Prohibition Gates (full stack)

**Axes**: Role sequence -- organize the prompt as 5 distinct layers where each gate
is a named phase boundary; C-23 and C-24 are named governing rules of the Layer 3
batch gate, not subordinate clauses; every criterion from C-01 through C-24 is
implemented by design at the correct layer
**Base**: R5-V-05 (passes C-15..C-22; projects 130 without explicit C-23/C-24 framing;
has the language but embedded in prose)
**Hypothesis**: R5-V-05 has "do not place any `**` marks -- until the full batch of
five sentences appears" (C-23 present) and "Do not revise the candidate's rationale
to manufacture a distinction" (C-24 present). V-05 in R6 reorganizes these as the
two named governing rules of the batch gate, with each rule labeled and leading its
own paragraph. The layered architecture makes the prohibition phase a distinct named
stage (Layer 3 -- Verification Gate) rather than a VERIFY phase with embedded checks.
The five layers: (0) Status Quo Baseline, (1) Idea Generation, (2) AMEND Draft,
(3) Verification Gate, (4) Finalize. The Verification Gate names Check B's two
governing rules as its primary constraints, making C-23 and C-24 the architectural
center of the gate rather than addenda to a check description.

**Expected**: C-01..C-22 PASS + C-23 PASS (Marking Prohibition named as governing rule)
+ C-24 PASS (Rationalization Prohibition named as governing rule) = **135**

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

**Check B -- Peer-Comparison Batch** (determines final top-5 marks; governed by
two named prohibitions below)

For each of the 5 candidates from Check A, complete this sentence and write it in
your output:

  "I chose [Idea Name] over [name one specific unmarked idea in the same dimension]
   because ___."

Name the peer by exact idea name from the same `##` section. State the reason
specifically -- what makes this candidate more actionable for {{topic}} given real
constraints: different scope, lower execution risk, more immediate user benefit, or
clearer ownership path. "It is better" or "more viable" do not count.

Write all five completed sentences as a numbered batch.

**The following two rules govern Check B and apply without exception:**

**Marking Prohibition**: No `**` marks may appear anywhere in your output until
all five Check B sentences are written. The marking action is prohibited -- not
deferred sentence by sentence. This prohibition covers `**` in headings, inline
marks, and any other notation that indicates selection. The selection phase (Layer 4)
begins only when all five sentences are present in your output.

**Rationalization Prohibition**: If you cannot complete the sentence for any
candidate -- no specific peer comes to mind or no specific reason holds -- that
candidate must be replaced with the specific peer you attempted to name in this
Check B comparison. The replacement source is fixed: it is the peer you attempted
to name here, not a different idea you prefer after reconsidering the pool. Do not
revise the candidate's rationale after Check B to manufacture a distinction that
was not present at comparison time. Rationale revision is the escape route this
prohibition closes. If you want to edit the rationale, treat that impulse as
confirmation that the replacement obligation applies. Once Check B is applied to a
candidate, the comparison stands.

**Check C -- AMEND Re-Invocability** (determines final AMEND content)
For each AMEND item: if a reader took only that directive and re-ran this brainstorm,
would they get a noticeably different pool? The bar is a different candidate
distribution, not different labels on the same ideas. Sharpen any item that fails
this test. The output of Check C determines final AMEND content.

**Check D -- Artifact Order** (gates the final write)
Does the Layer 0 paragraph appear before the first idea in the artifact? Confirm.
This check gates the artifact write.

---

## Layer 4 -- Finalize

Only after all four checks in Layer 3 are complete:

**Top-5**: Mark exactly 5 ideas with `**` on their heading -- the candidates
confirmed in Check B, with any substitutions applied. Distribute marks across at
least 2 different dimensions if the pool supports it.

**AMEND**: Write the AMEND section with exactly 3 adjustments updated from Layer 2
based on Check C. Each item must: (a) name a specific shift axis, (b) describe
which ideas enter, exit, or re-rank and why the pool looks different, (c) be
re-invocable without additional clarification.

```
## AMEND

1. **[Direction]** -- [Entries, exits, re-ranks. Pool looks different because ___. Re-invocable.]
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
Check B sentences -> AMEND. Total ideas (including Do Nothing): 20-40.
```

---

## Rubric Coverage Analysis -- R6

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 volume (20-40) | "20-40 candidates" | same (inh) | same (inh) | "20-40 rows total" | "20-40" |
| C-02 idea anatomy (4 fields) | Per-idea block (4 fields) | same (inh) | same (inh) | Table columns (Name/Pitch/Dimension/Rationale) | Per-idea block |
| C-03 top-5 marker (**) | `**` heading prefix (Phase 3) | same (inh) | same (inh) | `**YES**` in Top-5? col (gated by Step 2b) | `**` heading (Layer 4) |
| C-04 inertia check | Status Quo required section + trajectory rationale | same (inh) | same (inh) | Status Quo row + Preamble | Dim 7 mandatory + Layer 0 trajectory |
| C-05 AMEND (3 items) | 1c draft + Check C (determines AMEND) | same (inh) | same (inh) | Step 5, output of Review B | Layer 2 draft + Check C |
| C-06 category grouping | Required `##` sections per dimension | same (inh) | same (inh) | Category View (Step 4, required structural output) | 7 dimension `##` headers |
| C-07 rationale specificity | "cite real constraint; no generic reasoning" | same (inh) | same (inh) | "cite specific constraint; 'provides value' not a rationale" | "name real constraint; topic-specific" |
| C-08 category diversity (4+) | 6 required dimensions | same (inh) | same (inh) | 7 required dimension types | 7 named dimensions |
| C-09 AMEND actionability | Check C re-invocability test | same (inh) | same (inh) | "Re-runnable with this directive alone" + Review B | Check C: "different candidate distribution" |
| C-10 top-5 defensibility | Check A + Check B sentences + batch gate | Check A + Check B with replacement | Check A + Check B + Prohibition Battery | Review A + Registry + substitution rules | Check A + Check B + both governing rules |
| C-11 sequential-default guard | "Do not mark top-5 yet" in Phase 1b | same (inh) | same (inh) | "Leave Top-5? blank during Step 1" -- construction phase | "Do not mark... in this layer" -- Layer 1, generation phase |
| C-12 re-runnability bar | Check C: "noticeably different pool" | same (inh) | same (inh) | Review B: "produce a table with different rows" | Check C: "different candidate distribution, not different labels" |
| C-13 category dimension taxonomy | 6 named dimensions with descriptions | same (inh) | same (inh) | 7 named dimension types with descriptions | 7 named dimensions with descriptions |
| C-14 inertia-first framing paragraph | 1a: "appears at top... precedes all ideas" | same (inh) | same (inh) | Preamble: "must appear before the idea table" | Layer 0: "must appear first... before any alternatives" |
| **C-15 structural spine guarantee** | **PASS** (inh): 6 required `##` sections; "do not collapse; do not omit" | **PASS** (inh): same | **PASS** (inh): same | **PASS** (inh): Category View "required structural output... must contain a section for every Dimension" | **PASS** (inh): 7 dimension `##` headers; each dimension mandated |
| **C-16 generation-phase sequential guard** | **PASS** (inh): "Do not mark top-5 yet" in Phase 1b, imperative | **PASS** (inh): same | **PASS** (inh): same | **PASS** (inh): "Leave Top-5? blank during Step 1" in construction phase | **PASS** (inh): "Do not mark any idea with `**` in this layer" in Layer 1, imperative |
| **C-17 peer-comparison defensibility test** | **PASS** (inh): "complete this sentence and write it in your output: 'I chose [Name] over [peer] because ___'" | **PASS** (inh): "can you complete this sentence: 'I chose this over [peer] because ___'" | **PASS** (inh): "complete this sentence and write it in your output" | **PASS** (inh): Registry "I chose [Candidate] over [Peer] because ___" column | **PASS** (inh): "complete this sentence and write it in your output" |
| **C-18 self-review phase integration** | **PASS** (inh): Check A "determines candidates for Check B"; Check B "determines marks in Phase 3"; Check C "determines AMEND content"; Check D "gates artifact write" | **PASS** (inh): same | **PASS** (inh): same (all four links named) | **PASS** (inh): Review A -> Step 2b; Review B -> Step 5; Review C -> table completeness; Step 2b -> Step 3 | **PASS** (inh): Check A -> "candidates that advance"; Check B -> "final top-5 marks"; Check C -> "final AMEND content"; Check D -> "gates artifact write" |
| **C-19 peer-test imperative form** | **PASS** (inh): "complete this sentence and write it in your output" -- imperative + materialization | **FAIL**: "can you complete" -- interrogative (intentional isolation) | **PASS** (inh): "complete this sentence and write it in your output" | **PASS** (inh): Registry schema -- row completion enforces sentence materialization | **PASS** (inh): "complete this sentence and write it in your output" |
| **C-20 peer-test consequence clause** | **FAIL**: no consequence clause (intentional isolation) | **PASS** (inh): "Prohibition 1 -- Source Lock: That idea must be replaced" | **PASS** (inh): "Prohibition B -- Rationalization Block: ...that pick must be replaced" | **PASS** (inh): "Rule 1 -- Source Lock: the `**YES**` mark for that candidate must go to the idea named in the Attempted Peer column" | **PASS** (inh): "that candidate must be replaced with the specific peer you attempted to name" |
| **C-21 peer-test batch-completion gate** | **PASS** (inh): "Write all five completed sentences as a numbered Check B Batch. The batch is the gate: Phase 3 may begin... only when all five sentences are present." | **FAIL**: no batch gate (C-19 prerequisite absent) | **PASS** (inh): "Write all five completed sentences as a numbered batch" + Prohibition A gate | **PASS** (inh): Registry row-completion gate: "no selection marks of any kind may appear before all 5 rows exist" | **PASS** (inh): "Write all five completed sentences as a numbered batch" + Marking Prohibition gate |
| **C-22 consequence replacement source specificity** | **FAIL**: no consequence clause (C-20 prerequisite absent) | **PASS** (inh): "the specific peer you attempted to name in this comparison... The peer you attempted to name in this specific Check B test for this specific candidate is the only permissible replacement source" | **PASS** (inh): "the specific peer you attempted to name in this comparison. The replacement source is fixed as that peer" | **PASS** (inh): "Rule 1 -- Source Lock: The replacement source is fixed: it is the Attempted Peer from this row -- not a different idea you prefer after reconsidering" | **PASS** (inh): "The replacement source is fixed: it is the peer you attempted to name here, not a different idea you prefer after reconsidering" |
| **C-23 selection-phase marking prohibition** | **PASS**: Lead frame: "Marking is prohibited during this entire check. Do not place any `**` marks anywhere in your output... The marking action is the thing that is prohibited." -- names the marking action as the forbidden behavior, not write-order | **FAIL**: no batch gate (C-19 prerequisite absent) | **PASS**: "**Prohibition A -- Marking Ban**: Do not place any `**` marks anywhere in your output while Check B is in progress. The marking action is what is prohibited -- not just deferred." -- explicit named prohibition on the marking action | **PASS**: "**Marking ban**: Do not place any `**YES**` values, `**` marks, or any other selection notation... The marking action is prohibited until all 5 rows of this Registry are complete." -- names marking action explicitly | **PASS**: "**Marking Prohibition**: No `**` marks may appear anywhere in your output until all five Check B sentences are written... The marking action is prohibited -- not deferred sentence by sentence." -- naming marking as the prohibited action |
| **C-24 post-comparison rationalization block** | **FAIL**: no consequence clause (C-20 prerequisite absent) | **PASS**: "**Prohibition 2 -- Rationalization Block**: Do not revise the failing idea's rationale to manufacture a distinction... Rationale revision is not a valid alternative to the replacement -- it is the escape route that this prohibition closes." -- names the escape route explicitly | **PASS**: "**Prohibition B -- Rationalization Block**: Do not revise the pick's rationale after completing Check B to manufacture a distinction that was not already present at comparison time. Rationale revision is the escape route this prohibition closes." | **PASS**: "**Rule 2 -- Rationalization Block**: Do not revise the original Candidate row's Rationale field in the idea table after completing the Registry... Rationale revision is the escape route this rule closes." -- explicitly named prohibition | **PASS**: "**Rationalization Prohibition**: ...Do not revise the candidate's rationale after Check B to manufacture a distinction that was not present at comparison time. Rationale revision is the escape route this prohibition closes." |

**Projected scores:**

| Variation | C-01..C-18 | C-19 | C-20 | C-21 | C-22 | C-23 | C-24 | Projected |
|-----------|-----------|------|------|------|------|------|------|-----------|
| R6-V-01 | 120 | pass (inh) | fail | pass (inh) | fail | pass | fail | 125 |
| R6-V-02 | 120 | fail | pass (inh) | fail | pass (inh) | fail | pass | 125 |
| R6-V-03 | 120 | pass (inh) | pass (inh) | pass (inh) | pass (inh) | pass | pass | 135 |
| R6-V-04 | 120 | pass (inh) | pass (inh) | pass (inh) | pass (inh) | pass | pass | 135 |
| R6-V-05 | 120 | pass (inh) | pass (inh) | pass (inh) | pass (inh) | pass | pass | 135 |

**C-23/C-24 mechanism comparison:**

| Variation | C-23 Mechanism | C-24 Mechanism |
|-----------|---------------|----------------|
| V-01 | Lead frame: "Marking is prohibited during this entire check... The marking action is the thing that is prohibited" | None (C-20 absent) |
| V-02 | None (C-19 absent; interrogative prevents batch gate) | Named prohibition block: "Prohibition 2 -- Rationalization Block... Rationale revision is the escape route that this prohibition closes" |
| V-03 | Named block: "Prohibition A -- Marking Ban: Do not place any `**` marks... The marking action is what is prohibited -- not just deferred" | Named block: "Prohibition B -- Rationalization Block: Do not revise the pick's rationale... Rationale revision is the escape route this prohibition closes" |
| V-04 | Named schema rule: "Marking ban: Do not place any `**YES**` values, `**` marks, or any other selection notation... The marking action is prohibited" | Named schema rule: "Rule 2 -- Rationalization Block: Do not revise the original Candidate row's Rationale field... Rationale revision is the escape route this rule closes" |
| V-05 | Governing rule: "Marking Prohibition: No `**` marks may appear... The marking action is prohibited -- not deferred sentence by sentence" | Governing rule: "Rationalization Prohibition: Do not revise the candidate's rationale... Rationale revision is the escape route this prohibition closes" |

**R6 design insight:** V-04 and V-05 from R5 likely already score 135 under rubric v6 --
both have the C-23 and C-24 language present in their prose. R6's work is threefold:
(1) isolate each prohibition in single-axis tests (V-01, V-02) to confirm the minimal
pattern; (2) fix R5-V-03's schema C-24 ambiguity with an explicitly named rule block
(V-04); (3) demonstrate two additional architectures (prose with Prohibition Battery
in V-03; layered with governing rules in V-05) where C-23 and C-24 are named primary
constraints rather than embedded qualifiers. The Prohibition Battery (V-03) and
Governing Rules (V-05) approaches serve different models: V-03 is compact and
check-based; V-05 is layered and architecture-first. Both hit 135 via different
structural decisions.
