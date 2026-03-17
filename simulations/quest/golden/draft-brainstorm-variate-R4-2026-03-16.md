---
skill: quest-variate
skill_target: draft-brainstorm
round: 4
date: 2026-03-16
rubric_version: 4
r3_best: V-02 = 120, V-01 = 117.5, V-03 = 115 (V-04 and V-05 require validation)
r4_target: 125 -- close C-19 (peer-test imperative form) and C-20 (peer-test consequence clause)
---

# Variate R4 -- draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R4 focuses on closing the two R4 aspirational criteria introduced in rubric v4:
- **C-19** Peer-Test Imperative Form -- peer test stated as imperative command with output-materialization requirement (sentence must appear in output, not be answered silently)
- **C-20** Peer-Test Consequence Clause -- peer test specifies a named output action when the test fails (swap, replace, demote -- not "adjust if needed")

R3 gap analysis going into R4:

| Variation | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | R3 Score |
|-----------|------|------|------|------|------|------|----------|
| R3-V-01 (117.5) | PASS (mandatory sections) | PASS (gen-phase "do not mark yet") | PASS (interrogative peer test -- floor) | PASS (Phase 2 checks feed Phase 3) | FAIL (interrogative) | FAIL (no consequence) | 117.5 |
| R3-V-02 (120) | PASS | FAIL (guard in selection, not gen) | PASS -- per rubric C-19+C-20 also PASS | PASS | PASS | PASS | 120 |
| R3-V-03 (115) | FAIL (advisory, not mandate) | PASS | FAIL (Check B interrogative) | PASS | FAIL | FAIL | 115 |
| R3-V-04 (need validation) | PASS | PASS | PASS | PASS | ? | ? | ~120? |
| R3-V-05 (need validation) | PASS | PASS | PASS | PASS | ? | ? | ~120? |

R4 axes selected:

| Axis | New in R4? | Used In | R4 Criterion |
|------|-----------|---------|--------------|
| Phrasing register: interrogative -> imperative with materialization | Yes | V-01 | C-19 only |
| Lifecycle emphasis: add named consequence gate | Yes | V-02 | C-20 only |
| Output format: peer sentence as required table column | Yes | V-03 | C-19+C-20 via schema |
| Phrasing register + lifecycle emphasis combined | Combo | V-04 | C-19+C-20 |
| Full stack: all R3 criteria + both R4 criteria | Combo | V-05 | C-15+C-16+C-17+C-18+C-19+C-20 |

---

## V-01 -- Phrasing Register: Imperative Peer Test (C-19 isolation)

**Axis**: Phrasing register -- convert the peer-comparison test from interrogative to imperative with explicit output-materialization requirement; no consequence clause added
**Base**: R3-V-01 (passes C-15, C-16, C-17-at-floor, C-18; fails C-19, C-20)
**Hypothesis**: R3-V-01's Check B asks "can you complete this sentence: 'I chose this over [peer] because ___'?" -- the interrogative form allows the model to answer the question silently ("yes, I can") without producing the completed sentence as output. Converting to imperative ("complete this sentence and write it in your output") closes the silent-affirmation gap by making the written sentence a required output artifact, not a self-assessment. Consequence clause is deliberately not added to isolate C-19: if the sentence must appear but no swap is mandated on failure, the variation tests whether output-materialization alone passes C-19.

**Expected**: C-15 PASS (inh) + C-16 PASS (inh) + C-17 PASS + C-18 PASS (inh) + C-19 PASS + C-20 FAIL (no consequence) = 117.5 + 2.5 = **120**

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
and describe what changes. Do not finalize yet -- the verification step will check
these.

---

## PHASE 2 -- VERIFY

Before writing the final artifact, complete all 4 checks in order.

**Check A -- Sequential Default**
Look at the 5 ideas you are considering for top-5. Are they the first 5 ideas
you generated? If yes, rescan the full pool -- the best ideas are rarely the
first ones written. Select the 5 most immediately actionable, not the 5 most
recently visible.

**Check B -- Top-5 Defensibility**
For each of your 5 picks, complete this sentence and write it in your output:

  "I chose [Idea Name] over [name one specific unmarked idea in the same section]
   because ___."

The peer name must be an exact idea name from the same `##` section. The reason
must be specific: a different scope, lower implementation cost, better fit for a
real constraint of {{topic}}, or a distinct user group. "It is stronger" or "more
aligned" do not count as specific reasons.

Write all five completed sentences before moving to Check C.

**Check C -- AMEND Re-Invocability**
For each of your 3 AMEND items: if a reader took only that directive and re-ran
this brainstorm, would they get a noticeably different pool? If the answer is
"probably the same ideas with different labels," sharpen the directive until each
amendment produces a clearly different candidate distribution.

**Check D -- Inertia Paragraph**
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. The paragraph is not optional and must precede alternatives.

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
then Check B sentences, then AMEND. Total ideas (including Do Nothing): 20-40.
```

---

## V-02 -- Lifecycle Emphasis: Consequence Gate (C-20 isolation)

**Axis**: Lifecycle emphasis -- add a named consequence clause to the peer test without changing its phrasing form (interrogative preserved to isolate C-20 from C-19)
**Base**: R3-V-01 (passes C-15, C-16, C-17-at-floor, C-18; fails C-19, C-20)
**Hypothesis**: R3-V-01's consequence for a failed peer test is "the selection is not defensible. Adjust if needed" -- this is advisory, not a gate. A model can acknowledge the deficiency and continue unchanged. Adding a mandatory swap instruction ("must be replaced with the specific peer you named") makes the test a process gate: fail the test, change the output. Interrogative form is preserved ("can you complete") to isolate whether a consequence clause alone passes C-20, without the imperative form of C-19.

**Expected**: C-15 PASS (inh) + C-16 PASS (inh) + C-17 PASS + C-18 PASS (inh) + C-19 FAIL (interrogative) + C-20 PASS (consequence: replace) = 117.5 + 2.5 = **120**

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
and describe what changes. Do not finalize yet -- the verification step will check
these.

---

## PHASE 2 -- VERIFY

Before writing the final artifact, complete all 4 checks in order.

**Check A -- Sequential Default**
Look at the 5 ideas you are considering for top-5. Are they the first 5 ideas
you generated? If yes, rescan the full pool -- the best ideas are rarely the
first ones written. Select the 5 most immediately actionable, not the 5 most
recently visible.

**Check B -- Top-5 Defensibility**
For each of your 5 picks, can you complete this sentence: "I chose this over
[name one specific unmarked idea in the same section] because ___"?

Name the alternative by its exact idea name from the same `##` section. State
the reason specifically -- a different scope, risk profile, implementation
requirement, or user group. Generic quality framing ("it is more aligned") does
not pass the test.

If you cannot name a specific peer or state a specific reason for any marked idea,
that idea must be replaced with the specific peer you attempted to name. Do not
revise the idea's rationale to manufacture a distinction that was not already
present -- if the distinction does not hold on inspection, the replacement is
mandatory.

**Check C -- AMEND Re-Invocability**
For each of your 3 AMEND items: if a reader took only that directive and re-ran
this brainstorm, would they get a noticeably different pool? If the answer is
"probably the same ideas with different labels," sharpen the directive until each
amendment produces a clearly different candidate distribution.

**Check D -- Inertia Paragraph**
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. The paragraph is not optional and must precede alternatives.

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
then AMEND. Total ideas (including Do Nothing): 20-40.
```

---

## V-03 -- Output Format: Peer Justification Table (C-19+C-20 via schema)

**Axis**: Output format -- peer justification is produced as a required named table (not prose embedded in a check phase), making output materialization a structural schema requirement rather than a prose instruction; the table schema carries both the sentence-completion form (C-19) and the swap consequence (C-20) as column rules
**Base**: R3-V-05 (table format; passes C-15, C-16, C-17, C-18; C-19/C-20 status unverified -- R3-V-05's Review B uses "Why [Idea] and not [peer]?" question form with "You must name"; may not satisfy C-19's output-materialization requirement)
**Hypothesis**: R3-V-05's peer test lives inside the Self-Review Phase as prose instructions -- the model can execute it as an internal check without the completed sentence appearing as a distinct output artifact. The fix: require a "Peer Justification Table" as a named output section at Step 3b. The table schema forces: (a) each sentence to be written as a table row (C-19 -- cannot be answered silently), and (b) the consequence to be encoded as a column rule ("if Peer column cannot be filled, remove Top-5? mark and substitute the named peer" -- C-20, specific action: remove/substitute). This tests whether encoding both criteria into output schema structure produces a more structurally stable pass than prose instructions alone.

**Expected**: C-15 PASS (inh) + C-16 PASS (inh) + C-17 PASS (inh) + C-18 PASS (inh) + C-19 PASS (table row = materialization) + C-20 PASS (remove+substitute = named action) = 120 + 5 = **125**

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
  values as you build the table. You will fill this column only after completing
  the Self-Review Phase (Step 2). Marking during construction introduces sequential
  bias -- ideas in the first rows are the first ones written, not the best.

Required row: **Do Nothing** with Dimension = `Status Quo`. Its Rationale must
describe what the current trajectory from the Preamble produces -- not "doing
nothing is an option."

Volume: 20-40 rows total.

---

### Step 2 -- Self-Review Phase

Before filling in the Top-5? column, run the following reviews. Each review
feeds a named downstream output decision -- do not skip.

**Review A -- Sequential Default** (determines top-5 candidates for Step 3)
Look at rows 1-5. Are you planning to mark these because they are the strongest
rows, or because they are the first? If the five strongest ideas are scattered
throughout the table, the selection is honest. If they are rows 1-5, rescan the
full table. The output of this review determines which rows advance to Step 3.

**Review B -- Peer-Comparison Test** (determines top-5 candidates for Step 3b)
For each row you plan to mark, identify one specific unmarked row in the same
Dimension that you are not marking. Hold this pairing -- it is required for
Step 3b. If you cannot identify a specific peer in the same Dimension for any
candidate, that candidate is not yet eligible for a top-5 mark.

**Review C -- AMEND Re-Invocability** (determines AMEND content in Step 5)
For each of your 3 AMEND directives: if a reader took only that directive and
re-ran the brainstorm, would they produce a table with different rows? If not,
sharpen the directive. The bar is a different candidate distribution.

**Review D -- Dimension Coverage** (determines Category View completeness in Step 4)
Do your Dimension values cover all 7 required dimension types? If any required
type is missing, add rows before proceeding.

---

### Step 3 -- Mark Top-5 (output of Review A)

Fill in `**YES**` in exactly 5 rows' Top-5? column. These are the rows with
highest immediate viability. The marks reflect Review A's non-sequential scan.

---

### Step 3b -- Peer Justification Table (required output; output of Review B)

For each of the 5 marked rows, produce one row in this table:

| Marked Idea | Peer (same Dimension, unmarked) | Because (specific reason) |
|-------------|--------------------------------|--------------------------|
| [exact Name] | [exact Name of peer] | [specific reason -- scope, cost, user group, risk -- not "it is better"] |

All 5 rows must be filled before proceeding. Rules:
- Peer must be a row in the same Dimension from Step 1 -- not a hypothetical idea
- Reason must be specific to {{topic}}'s actual constraints; generic reasoning fails
- **If you cannot fill the Peer or Because field for any row**: remove the `**YES**`
  mark from that row and move the mark to the idea named in the Peer column.
  Do not revise the original row's rationale to manufacture a distinction --
  if the comparison cannot be stated, the substitution is mandatory.

The Peer Justification Table is a required output section. The artifact is
incomplete without it.

---

### Step 4 -- Category View (required structural output; output of Review D)

After the table, produce a Category View grouping ideas under their Dimension names.
Each Dimension that appeared in the table must have its own `## [Dimension Name]`
section. This is a **required structural output** -- the Category View is not optional
and must contain a section for every Dimension present in the table. A flat list fails.

```
## [Dimension Name]

- **[Idea Name]** -- [Pitch]  [**TOP-5**] (if marked)
```

---

### Step 5 -- AMEND (output of Review C)

Write an AMEND section with exactly 3 adjustments, incorporating any sharpening
from Review C. Each must meet all three conditions:
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

Artifact order: Preamble paragraph, idea table, Peer Justification Table,
Category View, AMEND.
```

---

## V-04 -- Combination: Phrasing Register + Lifecycle Emphasis (C-19+C-20 combined)

**Axes**: V-01 (imperative form + output-materialization) + V-02 (named consequence clause) combined in a single Check B
**Base**: R3-V-01 (passes C-15, C-16, C-17, C-18; fails C-19, C-20)
**Hypothesis**: V-01 isolates C-19 (imperative + materialization, no consequence) -- expected 120. V-02 isolates C-20 (consequence, no imperative upgrade) -- expected 120. Combining both in a single coherent Check B should close both gaps simultaneously, reaching 122.5. The combination test is whether a single instruction can carry: (1) imperative sentence-completion form, (2) output-materialization requirement, and (3) named swap consequence -- without the instruction becoming cluttered or internally contradictory. If the combination degrades readability to the point that the model executes only the first condition it encounters, the score will fall back to 120. Clean combination should reach 122.5.

**Expected**: C-15 PASS (inh) + C-16 PASS (inh) + C-17 PASS + C-18 PASS (inh) + C-19 PASS + C-20 PASS = 117.5 + 2.5 + 2.5 = **122.5**

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
and describe what changes. Do not finalize yet -- the verification step will check
these.

---

## PHASE 2 -- VERIFY

Before writing the final artifact, complete all 4 checks in order.

**Check A -- Sequential Default**
Look at the 5 ideas you are considering for top-5. Are they the first 5 ideas
you generated? If yes, rescan the full pool -- the best ideas are rarely the
first ones written. Select the 5 most immediately actionable, not the 5 most
recently visible.

**Check B -- Top-5 Defensibility**
For each of your 5 picks, complete this sentence and write it in your output:

  "I chose [Idea Name] over [name one specific unmarked idea in the same section]
   because ___."

The peer must be an existing idea from the same `##` section, named exactly. The
reason must be specific to {{topic}} -- a difference in scope, implementation cost,
user group served, or risk accepted. "It is more actionable" or "better aligned"
do not satisfy the requirement.

Write all five completed sentences in your output before proceeding to Check C.

If you cannot complete the sentence for any pick -- no specific peer comes to mind
or no specific reason holds -- that pick must be replaced with the specific peer
you named. Do not revise the pick's rationale to manufacture a distinction; if the
distinction is not already present in the pool, the replacement is mandatory.

**Check C -- AMEND Re-Invocability**
For each of your 3 AMEND items: if a reader took only that directive and re-ran
this brainstorm, would they get a noticeably different pool? If the answer is
"probably the same ideas with different labels," sharpen the directive until each
amendment produces a clearly different candidate distribution.

**Check D -- Inertia Paragraph**
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. The paragraph is not optional and must precede alternatives.

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
then Check B sentences, then AMEND. Total ideas (including Do Nothing): 20-40.
```

---

## V-05 -- Full Stack: All Six R3+R4 Criteria (target 125)

**Axes**: C-15 (structural mandate) + C-16 (generation-phase guard) + C-17 (peer comparison) + C-18 (self-review with feedback links) + C-19 (imperative + materialization) + C-20 (named consequence)
**Base**: R3-V-04 (passes C-15, C-16, C-17, C-18; projected 120; C-19/C-20 status unverified because Review B uses "Why [Name] and not [peer]?" question form with "You must name" + "does not belong -- replace it")
**Hypothesis**: R3-V-04's Review B contains two elements that might already pass C-19/C-20: (a) "You must name a specific peer" -- imperative; (b) "does not belong in the top-5 -- replace it" -- consequence clause. But C-19 requires not just imperative framing but that the completed sentence APPEARS IN OUTPUT. "You must name" may satisfy the instruction without the model writing the sentence as a visible artifact. V-05 closes this gap by: (1) converting the test from "Why [Name] and not [peer]?" question to "Complete this sentence: 'I chose [Name] over [peer] because ___'" sentence-completion form; (2) requiring all five completed sentences to appear in output before the finalize phase; (3) making the replacement instruction unambiguous ("must be replaced with the peer you named -- do not continue until all five sentences are written"). This should convert C-19/C-20 from uncertain to unambiguous PASS across all five top-5 slots.

**Expected**: C-15 PASS (inh) + C-16 PASS (inh) + C-17 PASS + C-18 PASS (inh) + C-19 PASS + C-20 PASS = 110 + 2.5 + 2.5 + 2.5 + 2.5 + 2.5 + 2.5 = **125**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

Your job: map the full option space across 6 required dimensions, then evaluate.

---

### Preliminary: Status Quo Trajectory

Before opening any dimension, write a paragraph that describes the current state
of {{topic}}: What is in motion today? What does the team inherit if no explicit
decision is made? What risks or missed opportunities compound over time by default?

This paragraph is the baseline against which every idea that follows is measured.
It must appear first in the final artifact, before any alternatives.

---

### Axis Map

You will generate ideas across the following 6 required dimensions. Each dimension
must produce at least 3 ideas. Label each section with the exact dimension name
as a `##` header.

**Do not mark any idea with `**` in this section.** Selection happens after the
full pool is complete. Marking ideas as you generate them introduces sequential
bias -- the first ideas written are the most available, not the best.

**Dimension 1 -- Scope**
Ideas in this axis vary *how much* of {{topic}}'s problem space is addressed --
from the minimal viable slice to the comprehensive overhaul.

**Dimension 2 -- Timing**
Ideas in this axis vary *when* intervention happens -- early bets, staged rollouts,
deferred commitments, and just-in-time decisions.

**Dimension 3 -- Integration**
Ideas in this axis vary *how* the solution connects to existing systems, platforms,
or external dependencies relevant to {{topic}}.

**Dimension 4 -- Audience**
Ideas in this axis vary *who* the primary beneficiary is -- different user segments,
internal teams, or downstream consumers of {{topic}}'s output.

**Dimension 5 -- Build vs. Buy**
Ideas in this axis vary *how* capability is acquired -- built internally, adopted
from outside, extended from existing components, or delegated.

**Dimension 6 -- Risk Profile**
Ideas in this axis vary *how much uncertainty* is accepted -- conservative,
incremental bets vs. high-variance, high-ceiling bets.

**Dimension 7 -- Status Quo (mandatory)**
This dimension contains exactly one idea: **Do Nothing**. Write the pitch and
rationale as a description of the current trajectory from the Preliminary section.
What does the team concretely get (and give up) by staying the course on {{topic}}?

---

### Idea Format

For every idea in every dimension:

```
## [Dimension Name]

### [Idea Name]

**Pitch**: One sentence.
**Rationale**: Why this option specifically serves {{topic}} -- name a real
constraint, user need, or opportunity. Must be topic-specific, not generic.
```

Total ideas across all 7 dimensions: 20-40.

---

### Self-Review Phase

Run all four reviews before marking top-5 or finalizing AMEND. Each review is
explicitly connected to a downstream output decision -- do not skip.

**Review A -- Sequential Default** (determines which candidates proceed to Review B)
Look at the 5 ideas you are considering for top-5. Are they the first 5 you
generated? If yes, rescan the full pool. The pool was built across 7 dimensions
for a reason -- the strongest ideas may be concentrated in later sections. This
review determines which candidates are eligible for the peer test.

**Review B -- Peer-Comparison Test** (determines final top-5 marks)
For each of your top-5 candidates, complete this sentence and write it in your
output:

  "I chose [Idea Name] over [name one specific unmarked idea in the same Dimension]
   because ___."

Name the peer by their exact idea name from the same `##` section. State the
reason specifically -- what makes this idea more actionable for {{topic}} given
real constraints: different scope, lower execution risk, more immediate user
benefit, or clearer ownership path. "It is better" or "more viable" do not count.

Write all five completed sentences in your output before proceeding to Review C.
Do not advance to the Top-5 Selection step until all five sentences are written.

If you cannot complete the sentence for any candidate -- no specific peer comes
to mind or no specific reason holds -- that candidate must be replaced with the
specific peer you named. Do not revise the candidate's rationale to manufacture
a distinction; if the comparison does not hold on inspection, the replacement is
mandatory.

**Review C -- AMEND Re-Invocability** (determines AMEND finalization)
For each of your 3 AMEND items: would a reader who took only that directive and
re-ran this brainstorm produce a noticeably different pool? If not, sharpen the
directive. The bar is a different candidate distribution, not different labels on
the same pool. This review determines final AMEND content.

**Review D -- Artifact Order** (gates the final write)
Does the Preliminary paragraph appear before the first idea? Confirm. This review
gates the artifact write.

---

### Top-5 Selection (output of Review A and B)

Mark exactly 5 ideas with `**` on their heading. Distribute marks across at least
2 different dimensions if the pool supports it. The marks are the output of
Review A (not sequential) and Review B (peer-defensible) -- not a fresh pass.

---

### AMEND (output of Review C)

Write an AMEND section with exactly 3 pool-shift adjustments, updated based on
Review C if any items required sharpening. Each item must meet all three conditions:
(a) names a specific shift axis,
(b) describes which ideas enter, exit, or re-rank and why the pool looks different,
(c) is re-invocable -- a reader can re-run the brainstorm from this directive and
    obtain a noticeably different pool without needing further clarification.

```
## AMEND

1. **[Direction]** -- [Entries, exits, re-ranks. Why pool looks different. Re-invocable.]
2. **[Direction]** -- [...]
3. **[Direction]** -- [...]
```

---

### Artifact

Save to: `simulations/draft/brainstorm/{{topic}}-brainstorm-{{date}}.md`

```yaml
---
skill: draft-brainstorm
topic: {{topic}}
date: {{date}}
---
```

Artifact order: Preliminary paragraph -> 7 dimension sections (top-5 marked)
-> Review B sentences -> AMEND.
Total ideas (including Do Nothing): 20-40.
```

---

## Rubric Coverage Analysis -- R4

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 volume (20-40) | Stated (PHASE 1) | Stated (PHASE 1) | "20-40 rows total" | Stated (PHASE 1) | "20-40" |
| C-02 idea anatomy (4 fields) | Per-idea block | Per-idea block | Table columns | Per-idea block | Per-idea block |
| C-03 top-5 marker (**) | `**` heading prefix | `**` heading prefix | `**YES**` in Top-5? col | `**` heading prefix | `**` heading prefix |
| C-04 inertia check | Status Quo required section + trajectory rationale | Status Quo required section + trajectory rationale | Status Quo row + Preamble | Status Quo required section + trajectory rationale | Status Quo dim 7 mandatory + trajectory |
| C-05 AMEND (3 items) | 1c draft + Check C | 1c draft + Check C | Step 5, Review C | 1c draft + Check C | AMEND section, Review C |
| C-06 category grouping | Required `##` sections per dimension | Required `##` sections per dimension | Category View (Step 4) | Required `##` sections per dimension | Dimension `##` headers |
| C-07 rationale specificity | "cite real constraint; no generic reasoning" | "cite real constraint; no generic reasoning" | "cite specific constraint; generic fails" | "cite real constraint; no generic reasoning" | "name real constraint; topic-specific" |
| C-08 category diversity (4+) | 6 required dimensions | 6 required dimensions | 7 required dimension types | 6 required dimensions | 7 dimensions |
| C-09 AMEND actionability | Check C tests re-invocability | Check C tests re-invocability | "Re-runnable with this directive alone" + Review C | Check C tests re-invocability | Sub-conditions (a)(b)(c) + Review C |
| C-10 top-5 defensibility | Check A + Check B sentences | Check A + Check B with replacement | Review A + Review B + Peer Justification Table | Check A + Check B sentences + replacement | Review A + Review B sentences + replacement |
| C-11 sequential-default guard | "Do not mark top-5 yet" in Phase 1b (generation phase) | "Do not mark top-5 yet" in Phase 1b (generation phase) | "Leave blank during Step 1. Do not fill in Top-5? values as you build the table." | "Do not mark top-5 yet" in Phase 1b (generation phase) | "Do not mark any idea with ** in this section." in Axis Map |
| C-12 re-runnability bar | Check C re-invocability test | Check C re-invocability test | "Re-runnable with this directive alone" | Check C re-invocability test | Review C re-invocability test |
| C-13 category dimension taxonomy | 6 named dimensions with descriptions | 6 named dimensions with descriptions | 7 named dimension types with descriptions | 6 named dimensions with descriptions | 7 named dimensions with descriptions |
| C-14 inertia-first framing paragraph | Phase 1a paragraph "appears at top, precedes all ideas" | Phase 1a paragraph "appears at top, precedes all ideas" | Preamble "must appear before the idea table" | Phase 1a paragraph "appears at top, precedes all ideas" | Preliminary "must appear first in the final artifact, before any alternatives" |
| **C-15 structural spine guarantee** | **PASS**: 6 required dimensions each a required `##` section; "Do not collapse; do not omit" | **PASS**: same as V-01 (inherited from R3-V-01) | **PASS**: Category View "required structural output... must contain a section for every Dimension present in the table. A flat list fails." | **PASS**: same as V-01 (inherited) | **PASS**: 7 dimensions each `##` header; Axis Map mandates one per dimension |
| **C-16 generation-phase sequential guard** | **PASS**: "Do not mark top-5 yet" in Phase 1b (generation block), imperative | **PASS**: same (inherited) | **PASS**: "Leave blank during Step 1. Do not fill in Top-5? values as you build the table." in Step 1 (construction phase), imperative | **PASS**: same (inherited) | **PASS**: "Do not mark any idea with ** in this section." in Axis Map = generation phase, imperative |
| **C-17 peer-comparison defensibility test** | **PASS**: "complete this sentence: 'I chose [Idea Name] over [peer] because ___'" in Check B | **PASS**: "can you complete: 'I chose this over [peer] because ___'" with named peer requirement | **PASS**: Review B "identify one specific unmarked row in the same Dimension" + Peer Justification Table requires sentence completion | **PASS**: "complete this sentence: 'I chose [Idea Name] over [peer] because ___'" in Check B | **PASS**: "complete this sentence: 'I chose [Idea Name] over [peer] because ___'" in Review B |
| **C-18 self-review phase integration** | **PASS**: Phase 2 has 4 checks; Check A -> Phase 3 marks; Check B -> Phase 3 marks; Check C -> AMEND update; Check D -> artifact order | **PASS**: Phase 2 has 4 checks; Check B -> replacement decision; Check C -> AMEND; Check D -> artifact order | **PASS**: Self-Review Phase names Review A -> Step 3; Review B -> Step 3b (Peer Justification Table); Review C -> Step 5; Review D -> Step 4 | **PASS**: Phase 2 has 4 checks; Check A+B -> PHASE 3 marks; Check C -> AMEND; Check D -> order | **PASS**: Self-Review Phase names Review A -> Top-5 Selection; Review B -> Top-5 Selection; Review C -> AMEND; Review D -> artifact write |
| **C-19 peer-test imperative form** | **PASS**: "complete this sentence and write it in your output: 'I chose [Name] over [peer] because ___.' Write all five completed sentences before moving to Check C." -- imperative + explicit output-materialization | **FAIL**: "can you complete this sentence: 'I chose this over [peer] because ___'?" -- interrogative form preserved (intentional isolation) | **PASS**: Peer Justification Table -- each row is the completed sentence; "All 5 rows must be filled before proceeding" -- table structure = structural output materialization | **PASS**: "complete this sentence and write it in your output" + "Write all five completed sentences in your output before proceeding to Check C" | **PASS**: "complete this sentence and write it in your output: 'I chose [Name] over [peer] because ___.' Write all five completed sentences in your output before proceeding to Review C." |
| **C-20 peer-test consequence clause** | **FAIL**: no consequence clause present (intentional isolation) | **PASS**: "that idea must be replaced with the specific peer you attempted to name. Do not revise... the replacement is mandatory." -- specific action: replace | **PASS**: "remove the `**YES**` mark from that row and move the mark to the idea named in the Peer column. Do not revise... the substitution is mandatory." -- specific action: remove + substitute | **PASS**: "that pick must be replaced with the specific peer you named. Do not revise... the replacement is mandatory." -- specific action: replace | **PASS**: "that candidate must be replaced with the specific peer you named. Do not revise... the replacement is mandatory." -- specific action: replace |

**Projected scores:**

| Variation | C-01..C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | Projected |
|-----------|-----------|------|------|------|------|------|------|-----------|
| R4-V-01 | 110 | pass | pass (inh) | pass | pass (inh) | pass | fail | 120 |
| R4-V-02 | 110 | pass | pass (inh) | pass | pass (inh) | fail | pass | 120 |
| R4-V-03 | 110 | pass (inh) | pass (inh) | pass (inh) | pass (inh) | pass | pass | 125 |
| R4-V-04 | 110 | pass (inh) | pass (inh) | pass | pass (inh) | pass | pass | 122.5 |
| R4-V-05 | 110 | pass (inh) | pass (inh) | pass | pass (inh) | pass | pass | 125 |

**C-19/C-20 mechanism comparison:**

| Variation | C-19 Mechanism | C-20 Mechanism |
|-----------|---------------|----------------|
| V-01 | Imperative "complete this sentence... write it in your output" + "Write all five before proceeding" | None (intentional isolation) |
| V-02 | Absent (interrogative preserved) | "must be replaced with the specific peer... the replacement is mandatory" |
| V-03 | Table schema: sentence is a required column value, cannot be skipped structurally | "remove mark and move it to the Peer column... the substitution is mandatory" |
| V-04 | Same as V-01 | Same as V-02 |
| V-05 | Same as V-01 (in Self-Review Phase context) | Same as V-02 (in Self-Review Phase context) |

**R4 insight to watch:** V-04 reaches 122.5 (not 125) because it inherits C-15 and C-16 from R3-V-01 but does not have the full self-review phase structure of R3-V-04. If R3-V-04's self-review structure is needed to reliably pass C-18, V-05 (which inherits R3-V-04's architecture) is the stronger 125 candidate. V-03's structural approach (consequence clause encoded as schema rule, not prose instruction) tests whether output-format encoding is more durable than prose instruction under prompt compression.
