---
skill: quest-variate
skill_target: draft-brainstorm
round: 5
date: 2026-03-16
rubric_version: 5
r4_best: V-03 = 125, V-05 = 125, V-04 = 122.5, V-01 = 122.5, V-02 = 122.5 (all before C-21/C-22 validation)
r5_target: 130 -- close C-21 (peer-test batch-completion gate) and C-22 (consequence replacement source specificity)
---

# Variate R5 -- draft-brainstorm

5 complete prompt body variations for the `draft-brainstorm` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R5 focuses on closing the two R5 aspirational criteria introduced in rubric v5:
- **C-21** Peer-Test Batch-Completion Gate -- all five peer-comparison sentences written as
  a batch BEFORE any selection or output-finalization phase begins; "before moving to Check C"
  is not sufficient -- the gate must explicitly block top-5 marking until the full batch is
  in output
- **C-22** Consequence Replacement Source Specificity -- the consequence clause (C-20) must
  name the specific peer from the failed test as the replacement source; "replace with a
  better idea" or even "replace with the specific peer you named" may satisfy C-20 but not
  C-22 if the phrasing does not close the free-swap loophole

R4 gap analysis going into R5:

| Variation | C-19 | C-20 | C-21 | C-22 | R4 Score |
|-----------|------|------|------|------|----------|
| R4-V-01 (122.5) | PASS (imperative + "Write all five before Check C") | FAIL (no consequence -- intentional isolation) | FAIL (batch present but "before Check C" not "before selection"; pending) | FAIL (no consequence, prerequisite missing) | 122.5 |
| R4-V-02 (122.5) | FAIL (interrogative -- intentional isolation) | PASS ("must be replaced with the specific peer you attempted to name") | FAIL (no imperative form, C-21 requires C-19 as prerequisite) | PASS pending ("specific peer you attempted to name" -- core pattern present; shown FAIL pending validation run) | 122.5 |
| R4-V-03 (125) | PASS (table row = structural materialization) | PASS ("remove mark and move to Peer column -- substitution mandatory") | FAIL (Step 3 marks BEFORE Step 3b sentences -- batch follows selection, not precedes it) | PASS pending ("idea named in the Peer column" -- but order issue with C-21 may affect C-22 evaluation) | 125 |
| R4-V-04 (122.5) | PASS | PASS ("replaced with the specific peer you named") | FAIL pending (batch present but "before proceeding to Check C" not "before selection mark placed") | PASS pending ("specific peer you named" -- may not specify "attempted to name") | 122.5 |
| R4-V-05 (125) | PASS | PASS ("replaced with the specific peer you named") | FAIL pending ("Do not advance to the Top-5 Selection step" is present but batch-as-gate phrasing unclear) | PASS pending ("specific peer you named" -- same as V-04) | 125 |

R5 axes selected:

| Axis | New in R5? | Used In | R5 Criterion |
|------|-----------|---------|--------------|
| Phrasing register: "before Check C" -> explicit selection-phase advance gate | Yes | V-01 | C-21 only |
| Lifecycle emphasis: replacement source explicitly traced to attempted peer from this comparison | Yes | V-02 | C-22 only |
| Output format: Pre-Selection Batch Registry precedes Top-5? column (swaps R4-V-03's order) | Yes | V-03 | C-21+C-22 via schema |
| Phrasing register + lifecycle emphasis combined; C-18 feedback links made explicit | Combo | V-04 | C-21+C-22 + C-18 fix |
| Full stack: R4-V-05 with both R5 patches | Combo | V-05 | C-21+C-22 in R4-V-05 architecture |

Root cause of R4-V-03's C-21 failure: In R4-V-03, the order is Step 3 (fill Top-5? column) ->
Step 3b (Peer Justification Table). The sentences appear AFTER the marks, not before. C-21
requires all sentences as a batch BEFORE the selection decision. R5-V-03 fixes this by
introducing a Pre-Selection Batch Registry at Step 2b (between Self-Review Phase and Step 3),
making the sentence batch a prerequisite for the Top-5? column.

Root cause of R4 C-22 gaps: Variations use "the specific peer you named" (V-04, V-05) or
leave the replacement source implicit (V-03). C-22 requires the phrasing to trace the
replacement explicitly to the peer from the failed test -- "attempted to name" is the key
signal. Generic "better idea" and even "peer you named" allow free-swap interpretations.

---

## V-01 -- Phrasing Register: Selection-Phase Advance Gate (C-21 isolation)

**Axis**: Phrasing register -- convert the batch-write sequencing in Check B from
"before moving to Check C" to an explicit selection-phase advance gate; no consequence
clause added
**Base**: R4-V-01 (passes C-15, C-16, C-17, C-18, C-19; fails C-20)
**Hypothesis**: R4-V-01's Check B says "Write all five completed sentences before moving to
Check C." The loophole: "before Check C" sequences the sentences relative to the next
check, not relative to the selection step. A model can write all five sentences, run
Check C and Check D inline, and then begin placing marks -- with the batch technically
preceding marking but the instruction not framing it as a gate on selection. The fix:
explicitly state "Phase 3 is gated by batch completion -- do not place any `**` marks
until all five sentences appear in your output." This makes the batch a phase-advance
gate on the selection decision, not just a sequencing instruction between checks.
Consequence clause is deliberately absent to isolate C-21: if the batch must precede
selection but no swap is mandated on failure, this tests whether the advance gate alone
passes C-21 without C-20/C-22.

**Expected**: C-15..C-19 PASS (inh) + C-20 FAIL (no consequence) + C-21 PASS + C-22 FAIL
(no consequence, prerequisite missing) = 122.5 + 2.5 = **125**

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

Write all five completed sentences as a numbered batch (Check B Batch) before
advancing to Check C. **Phase 3 is gated by batch completion: do not place any
`**` marks anywhere until all five Check B sentences appear in your output.**
Writing one sentence and deciding that candidate clearly passes is not acceptable --
the full batch must be present before any selection mark is placed.

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
then Check B Batch sentences, then AMEND. Total ideas (including Do Nothing): 20-40.
```

---

## V-02 -- Lifecycle Emphasis: Replacement Source Trace (C-22 isolation)

**Axis**: Lifecycle emphasis -- explicitly trace the replacement source in the consequence
clause to the peer from this specific comparison, not any convenient alternative;
interrogative form preserved to isolate C-22 from C-19/C-21
**Base**: R4-V-02 (passes C-15, C-16, C-17, C-18, C-20; fails C-19; C-22 pending)
**Hypothesis**: R4-V-02's consequence says "that idea must be replaced with the specific peer
you attempted to name." The C-22 gap: "attempted to name" is present but the surrounding
context may allow a model to interpret the replacement source loosely -- "the peer I was
trying to name" vs. "the peer named in this specific test for this specific candidate." The
fix: add explicit language that the replacement source is fixed as the peer from this
particular comparison, not a peer selected after reconsidering the pool. "The replacement
source is fixed: the peer you named here, not a different idea you might prefer after
reconsidering" closes the free-swap interpretation. Interrogative form is preserved ("can
you complete") to isolate C-22: if source specificity alone passes C-22 without the
imperative form of C-19, this variation demonstrates that C-22 is a standalone concern
independent of sentence-form framing.

**Expected**: C-15..C-18 PASS (inh) + C-19 FAIL (interrogative) + C-20 PASS (inh) + C-21
FAIL (C-19 prerequisite absent) + C-22 PASS = 122.5 + 2.5 = **125**

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
that idea must be replaced with the specific peer you attempted to name in this
comparison. The replacement source is fixed: it is the peer you named here, for
this specific candidate, in this specific check -- not a different idea you might
prefer after reconsidering the pool, and not the next most viable candidate from
another section. Do not revise the marked idea's rationale to manufacture a
distinction that was not already present -- if the comparison does not hold on
inspection, the replacement is mandatory and the peer from this check is the
only permissible replacement source.

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

## V-03 -- Output Format: Pre-Selection Batch Registry (C-21+C-22 via schema, order fixed)

**Axis**: Output format -- redesign R4-V-03's table approach so the sentence registry
PRECEDES the Top-5? column (fixing the order inversion where R4-V-03 marked first at
Step 3, then justified at Step 3b); encode both C-21 (registry must be fully complete
before any Top-5? column value is written) and C-22 (Attempted Peer column is the fixed
replacement source) as structural schema constraints
**Base**: R4-V-03 (passes C-15, C-16, C-17, C-18, C-19, C-20; C-21 FAIL due to order
inversion; C-22 pending)
**Hypothesis**: R4-V-03's order inversion (Step 3 marks Top-5?, then Step 3b produces
justification) means the batch appears after the selection, not before. C-21 requires
the batch to PRECEDE the selection decision. Moving the registry to Step 2b (after
Self-Review, before Top-5? marking) closes the order gap. The schema encodes C-21 via
the gate rule: "The Top-5? column (Step 3) cannot be filled until this Registry is fully
complete." C-22 is encoded via the Attempted Peer column rule: "The replacement source
is the idea in the Attempted Peer column of the same row -- not a different idea from the
table." Schema encoding makes both constraints structural properties of output shape rather
than prose instructions the model can soft-skip.

**Expected**: C-15..C-20 PASS (inh, with order fix) + C-21 PASS (registry gates selection)
+ C-22 PASS (Attempted Peer = fixed source) = 125 + 2.5 + 2.5 = **130**

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
  values as you build the table. You will fill this column only after the
  Pre-Selection Batch Registry (Step 2b) is fully complete. Marking during
  construction introduces sequential bias -- ideas in the first rows are the
  first ones written, not the best.

Required row: **Do Nothing** with Dimension = `Status Quo`. Its Rationale must
describe what the current trajectory from the Preamble produces -- not "doing
nothing is an option."

Volume: 20-40 rows total.

---

### Step 2 -- Self-Review Phase

Before filling in the Top-5? column, run the following reviews. Each review
feeds a named downstream output decision -- do not skip.

**Review A -- Sequential Default** (determines top-5 candidates for Step 2b)
Look at rows 1-5. Are you planning to mark these because they are the strongest
rows, or because they are the first? If the five strongest ideas are scattered
throughout the table, the selection is honest. If they are rows 1-5, rescan the
full table. The output of this review is the set of 5 candidates that advance
to the Pre-Selection Batch Registry.

**Review B -- AMEND Re-Invocability** (determines AMEND content in Step 5)
For each of your 3 AMEND directives: if a reader took only that directive and
re-ran the brainstorm, would they produce a table with different rows? If not,
sharpen the directive. The bar is a different candidate distribution, not
different labels on the same ideas. This review determines final AMEND content.

**Review C -- Dimension Coverage** (determines Category View completeness in Step 4)
Do your Dimension values cover all 7 required dimension types? If any required
type is missing, add rows before proceeding to Step 2b.

---

### Step 2b -- Pre-Selection Batch Registry (required output; gates Step 3)

This section must be fully complete before any Top-5? column value is written.
**Step 3 is gated by this section: the Top-5? column cannot contain any entry
until all 5 rows of this Registry are filled.**

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
Remove it from the candidate list before completing the Registry and add the next
strongest candidate from a different Dimension.

**If the sentence column cannot be completed** with a specific reason for any row,
the `**YES**` mark for that candidate must go to the idea named in the Attempted
Peer column of that row. The replacement source is fixed: it is the idea in the
Attempted Peer column, not a different idea from the table. Do not revise the
original candidate's rationale to manufacture a distinction -- if the comparison
cannot be stated, the substitution is mandatory and the replacement source is
the Attempted Peer named here.

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
`## [Dimension Name]` section. This is a required structural output -- the
Category View is not optional and must contain a section for every Dimension
present in the table. A flat list fails.

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

## V-04 -- Combination: Batch Gate + Source Trace, C-18 Explicit (C-21+C-22 combined)

**Axes**: V-01 (explicit selection-phase advance gate) + V-02 (fixed replacement source
trace) combined in a single Check B; Phase 2 feedback connections made explicit to
ensure C-18 passes reliably
**Base**: R4-V-04 (passes C-15, C-16, C-17, C-18 marginal, C-19, C-20; projected 122.5
due to C-18 marginal -- inherited R3-V-01 structure lacks explicit feedback-loop labels)
**Hypothesis**: R4-V-04 scored 122.5 (not 125) because its self-review phase inherited
R3-V-01's structure, which has 4 checks but does not explicitly name the downstream
output decision each check feeds. C-18 requires "at least one review-to-output feedback
link is named." R4-V-01's Check A is labeled "sequential default" but doesn't say "the
output of Check A determines candidates for Check B." Adding explicit labels ("determines
top-5 candidates for Check B", "determines top-5 marks in Phase 3", "determines AMEND
finalization", "gates artifact write") converts the feedback links from implicit to named,
satisfying C-18 unambiguously. The combination test is whether C-21 (batch gate) +
C-22 (source trace) + C-18 (explicit feedback) can coexist in a single coherent Check B
without the instruction becoming cluttered. If the combination is readable, expected 130;
if it creates instruction overload, a single criterion may regress.

**Expected**: C-15..C-20 PASS + C-21 PASS + C-22 PASS = 120 + 5 + 5 = **130**

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

Before writing the final artifact, complete all 4 checks in order. Each check is
explicitly connected to a downstream output decision -- do not skip.

**Check A -- Sequential Default** (determines top-5 candidates for Check B)
Look at the 5 ideas you are considering for top-5. Are they the first 5 ideas
you generated? If yes, rescan the full pool -- the best ideas are rarely the
first ones written. Select the 5 most immediately actionable, not the 5 most
recently visible. The output of Check A is the set of 5 candidates that advance
to Check B.

**Check B -- Top-5 Defensibility** (determines top-5 marks in Phase 3)
For each of your 5 picks from Check A, complete this sentence and write it in
your output:

  "I chose [Idea Name] over [name one specific unmarked idea in the same section]
   because ___."

The peer must be an existing idea from the same `##` section, named exactly. The
reason must be specific to {{topic}} -- a difference in scope, implementation cost,
user group served, or risk accepted. "It is more actionable" or "better aligned"
do not satisfy the requirement.

Write all five completed sentences as a numbered batch before advancing to Check C.
**Phase 3 is gated by batch completion: do not place any `**` marks until all five
Check B sentences appear in your output.** Writing one sentence and deciding that
candidate clearly passes is not acceptable -- all five must be present before any
selection mark is placed.

If you cannot complete the sentence for any pick -- no specific peer comes to mind
or no specific reason holds -- that pick must be replaced with the specific peer
you attempted to name in this comparison. The replacement source is fixed: it is
the peer from this specific Check B comparison for this specific candidate, not a
different idea you might prefer after reconsidering the pool. Do not revise the
pick's rationale to manufacture a distinction; if the comparison does not hold on
inspection, the replacement is mandatory and the replacement source is the peer
named here.

**Check C -- AMEND Re-Invocability** (determines final AMEND content in Phase 3)
For each of your 3 AMEND items: if a reader took only that directive and re-ran
this brainstorm, would they get a noticeably different pool? If the answer is
"probably the same ideas with different labels," sharpen the directive until each
amendment produces a clearly different candidate distribution. The output of Check
C determines final AMEND content.

**Check D -- Inertia Paragraph** (gates the artifact write)
Does the framing paragraph from 1a appear before the first idea in the artifact?
If not, move it. The paragraph is not optional and must precede alternatives.
This check gates the final artifact write.

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

## V-05 -- Full Stack: All 22 Criteria (target 130)

**Axes**: All R3+R4+R5 criteria; C-15 (structural mandate) + C-16 (generation-phase
guard) + C-17 (peer comparison) + C-18 (self-review with feedback links) + C-19
(imperative + materialization) + C-20 (named consequence) + C-21 (batch advance gate
explicitly blocks top-5 selection) + C-22 (replacement source traced to attempted peer)
**Base**: R4-V-05 (passes C-15..C-20; C-21/C-22 pending due to "specific peer you named"
phrasing and "do not advance" language that may not form an explicit batch-as-gate
constraint)
**Hypothesis**: R4-V-05 has two gaps that C-21 and C-22 expose:
(1) C-21: "Do not advance to the Top-5 Selection step until all five sentences are
written" is present in Review B, but the batch-as-gate framing is implicit -- a model
could write sentences one-by-one, check each inline, and advance when the fifth appears.
The fix: "Write all five sentences as a numbered batch before advancing to Review C. Do
not advance to the Top-5 Selection step -- do not place any `**` marks -- until the full
batch appears in your output." The explicit "do not place any `**` marks" closes the
inline-check loophole.
(2) C-22: "that candidate must be replaced with the specific peer you named" does not
close the free-swap loophole -- "you named" refers to the peer in the sentence, but
"after reconsidering the pool" may produce a different name. The fix: "the specific peer
you attempted to name in this review -- not a different idea you might prefer after
reconsidering." "Attempted to name" makes the replacement source the peer from the failed
test, not a post-hoc selection.

**Expected**: C-15..C-20 PASS (inh) + C-21 PASS + C-22 PASS = 125 + 2.5 + 2.5 = **130**

---

```
You are running the `draft-brainstorm` skill for the topic: {{topic}}

Your job: map the full option space across 7 required dimensions, then evaluate.

---

### Preliminary: Status Quo Trajectory

Before opening any dimension, write a paragraph that describes the current state
of {{topic}}: What is in motion today? What does the team inherit if no explicit
decision is made? What risks or missed opportunities compound over time by default?

This paragraph is the baseline against which every idea that follows is measured.
It must appear first in the final artifact, before any alternatives.

---

### Axis Map

You will generate ideas across the following 7 required dimensions. Each dimension
must produce at least 3 ideas (Status Quo: exactly 1). Label each section with the
exact dimension name as a `##` header.

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
for a reason -- the strongest ideas may be concentrated in later sections. The
output of this review determines which candidates are eligible for the peer test.

**Review B -- Peer-Comparison Test** (determines final top-5 marks)
For each of your top-5 candidates, complete this sentence and write it in your
output:

  "I chose [Idea Name] over [name one specific unmarked idea in the same Dimension]
   because ___."

Name the peer by their exact idea name from the same `##` section. State the
reason specifically -- what makes this idea more actionable for {{topic}} given
real constraints: different scope, lower execution risk, more immediate user
benefit, or clearer ownership path. "It is better" or "more viable" do not count.

Write all five completed sentences as a numbered batch before advancing to Review C.
**Do not advance to the Top-5 Selection step -- do not place any `**` marks --
until the full batch of five sentences appears in your output.** Writing one sentence
and deciding that candidate clearly passes is not acceptable; the full batch must
be present before any selection mark is placed.

If you cannot complete the sentence for any candidate -- no specific peer comes
to mind or no specific reason holds -- that candidate must be replaced with the
specific peer you attempted to name in this review. The replacement source is
fixed: it is the peer you attempted to name here, not a different idea you might
prefer after reconsidering the pool. Do not revise the candidate's rationale to
manufacture a distinction; if the comparison does not hold on inspection, the
replacement is mandatory and the replacement source is the peer named in this
review.

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
Review A (not sequential) and Review B (peer-defensible, with any substitutions
applied) -- not a fresh pass.

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

## Rubric Coverage Analysis -- R5

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 volume (20-40) | "20-40 candidates" (PHASE 1) | same (inh) | "20-40 rows total" | "20-40 candidates" (PHASE 1) | "20-40" |
| C-02 idea anatomy (4 fields) | Per-idea block (4 fields) | same (inh) | Table columns (Name, Pitch, Dimension, Rationale) | Per-idea block | Per-idea block |
| C-03 top-5 marker (**) | `**` heading prefix | same (inh) | `**YES**` in Top-5? col (gated by Step 2b) | `**` heading prefix | `**` heading prefix |
| C-04 inertia check | Status Quo required section + trajectory rationale from 1a | same (inh) | Status Quo row + Preamble | same (inh) | Status Quo dim 7 mandatory + Preliminary trajectory |
| C-05 AMEND (3 items) | 1c draft + Check C (determines final AMEND) | same (inh) | Step 5, output of Review B | 1c draft + Check C (labeled "determines AMEND") | AMEND section, output of Review C |
| C-06 category grouping | Required `##` sections per dimension | same (inh) | Category View (Step 4, required structural output) | same (inh) | Dimension `##` headers (7 required) |
| C-07 rationale specificity | "cite real constraint; no generic reasoning" | same (inh) | "cite specific constraint; 'provides value' not a rationale" | same (inh) | "name real constraint; topic-specific, not generic" |
| C-08 category diversity (4+) | 6 required dimensions | same (inh) | 7 required dimension types | same (inh) | 7 named dimensions |
| C-09 AMEND actionability | Check C re-invocability test ("noticeably different pool") | same (inh) | "Re-runnable alone" condition (c) + Review B | Check C re-invocability + "determines final AMEND" | sub-conditions (a)(b)(c) + Review C re-invocability |
| C-10 top-5 defensibility | Check A + Check B sentences + batch gate | Check A + Check B with replacement | Review A + Pre-Selection Registry + substitution rule | Check A + Check B sentences + replacement | Review A + Review B sentences + substitution |
| C-11 sequential-default guard | "Do not mark top-5 yet" in Phase 1b (generation phase) | same (inh) | "Leave blank during Step 1. Do not fill in Top-5? values as you build the table." -- construction phase | same (inh) | "Do not mark any idea with `**` in this section." -- Axis Map, generation phase |
| C-12 re-runnability bar | Check C: "re-ran... would they get a noticeably different pool" | same (inh) | "Re-runnable with this directive alone" (condition c) | Check C re-invocability test | Review C: "different candidate distribution" |
| C-13 category dimension taxonomy | 6 named dimensions with descriptions | same (inh) | 7 named dimension types with descriptions | same (inh) | 7 named dimensions with descriptions |
| C-14 inertia-first framing paragraph | Phase 1a: "appears at top of the final artifact and precedes all ideas" | same (inh) | Preamble: "must appear before the idea table in the final artifact" | same (inh) | Preliminary: "must appear first in the final artifact, before any alternatives" |
| **C-15 structural spine guarantee** | **PASS** (inh): 6 required `##` sections; "Do not collapse; do not omit" | **PASS** (inh): same | **PASS** (inh): Category View "required structural output... must contain a section for every Dimension. A flat list fails." | **PASS** (inh): same as V-01 | **PASS** (inh): 7 dimensions each `##` header; Axis Map mandates one per dimension |
| **C-16 generation-phase sequential guard** | **PASS** (inh): "Do not mark top-5 yet" in Phase 1b (generation block), imperative | **PASS** (inh): same | **PASS** (inh): "Leave blank during Step 1" in construction phase, imperative | **PASS** (inh): same | **PASS** (inh): "Do not mark any idea with `**` in this section" in Axis Map, generation phase, imperative |
| **C-17 peer-comparison defensibility test** | **PASS** (inh): "complete this sentence: 'I chose [Name] over [peer] because ___'" in Check B | **PASS** (inh): "can you complete: 'I chose this over [peer] because ___'" | **PASS** (inh): Registry "I chose [Candidate] over [Peer] because ___" column | **PASS**: "complete this sentence: 'I chose [Name] over [peer] because ___'" in Check B | **PASS** (inh): "complete this sentence: 'I chose [Name] over [peer] because ___'" in Review B |
| **C-18 self-review phase integration** | **PASS** (inh): Phase 2 checks A-D; Check A -> "candidates for Check B"; Check B -> "marks in Phase 3"; Check C -> "AMEND content"; Check D -> "artifact write" | **PASS** (inh): same (Check labels unchanged) | **PASS**: Self-Review Phase -- Review A -> "candidates for Step 2b"; Review B -> "AMEND content in Step 5"; Review C -> "Category View completeness in Step 4"; Step 2b -> gates Step 3 | **PASS**: Check A "determines candidates for Check B"; Check B "determines marks in Phase 3"; Check C "determines final AMEND content"; Check D "gates artifact write" -- all four links named | **PASS** (inh): Review A -> "eligible for peer test"; Review B -> "final top-5 marks"; Review C -> "AMEND finalization"; Review D -> "gates artifact write" |
| **C-19 peer-test imperative form** | **PASS** (inh): "complete this sentence and write it in your output" + batch gate | **FAIL**: "can you complete" -- interrogative (intentional isolation) | **PASS** (inh): Registry schema -- each row is the completed sentence; "All 5 rows must be complete before any Top-5? entry" -- cannot be skipped structurally | **PASS**: "complete this sentence and write it in your output" + "all five as numbered batch before advancing to Check C" | **PASS** (inh): "complete this sentence and write it in your output" + "full batch of five sentences" |
| **C-20 peer-test consequence clause** | **FAIL**: no consequence clause (intentional isolation) | **PASS** (inh): "must be replaced... replacement is mandatory... peer from this check is the only permissible replacement source" | **PASS** (inh): "substitution is mandatory and the replacement source is the Attempted Peer named here" -- named action: substitution to named peer | **PASS**: "must be replaced with the specific peer you attempted to name in this comparison... replacement is mandatory... replacement source is the peer named here" | **PASS** (inh): "must be replaced with the specific peer you attempted to name in this review... replacement is mandatory" |
| **C-21 peer-test batch-completion gate** | **PASS**: "Write all five sentences as a numbered batch (Check B Batch) before advancing to Check C. Phase 3 is gated by batch completion: do not place any `**` marks anywhere until all five Check B sentences appear in your output." -- explicit selection-phase advance gate | **FAIL**: no batch gate (C-19 prerequisite absent; interrogative) | **PASS**: "Step 3 is gated by this section: the Top-5? column cannot contain any entry until all 5 rows of this Registry are filled" -- structural gate; marking column physically cannot be filled until Registry complete | **PASS**: "Write all five sentences as a numbered batch before advancing to Check C. Phase 3 is gated by batch completion: do not place any `**` marks until all five Check B sentences appear in your output." | **PASS**: "Write all five sentences as a numbered batch before advancing to Review C. Do not advance to the Top-5 Selection step -- do not place any `**` marks -- until the full batch of five sentences appears in your output." |
| **C-22 consequence replacement source specificity** | **FAIL**: no consequence clause (prerequisite C-20 absent) | **PASS**: "The replacement source is fixed: it is the peer you named here, for this specific candidate, in this specific check -- not a different idea you might prefer after reconsidering the pool" -- source is the peer from this comparison, not a free pick | **PASS**: "The replacement source is fixed: it is the idea in the Attempted Peer column of that row -- not a different idea from the table" -- Attempted Peer column = structural anchor for replacement source | **PASS**: "The replacement source is fixed: it is the peer from this specific Check B comparison for this specific candidate, not a different idea you might prefer after reconsidering the pool" | **PASS**: "The replacement source is fixed: it is the peer you attempted to name here, not a different idea you might prefer after reconsidering the pool" |

**Projected scores:**

| Variation | C-01..C-18 | C-19 | C-20 | C-21 | C-22 | Projected |
|-----------|-----------|------|------|------|------|-----------|
| R5-V-01 | 120 | pass (inh) | fail | pass | fail | 125 |
| R5-V-02 | 120 | fail | pass (inh) | fail | pass | 125 |
| R5-V-03 | 120 | pass (inh) | pass (inh) | pass (order fixed) | pass | 130 |
| R5-V-04 | 120 | pass | pass | pass | pass | 130 |
| R5-V-05 | 120 | pass (inh) | pass (inh) | pass | pass | 130 |

**C-21/C-22 mechanism comparison:**

| Variation | C-21 Mechanism | C-22 Mechanism |
|-----------|---------------|----------------|
| V-01 | "Write all five as numbered batch (Check B Batch) before advancing to Check C. Phase 3 gated: do not place any ** marks until all five appear in output." | None (C-20 absent) |
| V-02 | None (C-19 absent; interrogative prevents batch gate) | "Replacement source is fixed: peer you named here, for this specific candidate, in this specific check -- not a different idea after reconsidering" |
| V-03 | Structural gate: "Step 3 is gated by this section: Top-5? column cannot contain any entry until all 5 Registry rows filled" | Schema: "Attempted Peer column... replacement source is fixed: idea in Attempted Peer column of that row" |
| V-04 | "All five as numbered batch before advancing to Check C. Phase 3 gated: do not place any ** marks until all five appear in output." | "Replacement source is fixed: peer from this specific Check B comparison for this specific candidate, not a different idea after reconsidering" |
| V-05 | "All five as numbered batch before advancing to Review C. Do not advance to Top-5 Selection -- do not place any ** marks -- until full batch appears in output." | "Replacement source is fixed: peer you attempted to name here, not a different idea you might prefer after reconsidering the pool" |

**R5 design insight:** V-03's order fix is the primary structural change from R4-V-03.
R4-V-03's Step 3 (mark) -> Step 3b (justify) sequence made C-21 impossible by design.
R5-V-03 moves the Registry to Step 2b (pre-selection), making the batch a structural
prerequisite for the marking step. V-04 and V-05 both target 130 via different
architectures (6-dimension prose vs. 7-dimension self-review); if one regresses due to
instruction density, the other provides coverage. V-02's C-22 isolation (interrogative,
no batch gate) tests whether source-specificity language alone passes C-22 or whether
the full consequence mechanism (C-20 + C-22) requires imperative form to be effective.
