---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 2
rubric: v2
---

# Variations — topic-story (Round 2)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Rubric v2 design context**: Adds three new aspirational criteria to v1's 9.
C-10 (pre-composition pattern artifact) — the cross-signal pattern must exist as
a discrete, labeled claim that stands independently of narrative prose. C-11
(pattern-to-recommendation traceability) — an explicit logical bridge must cite
the pattern as the reason for the recommendation verb. C-12 (decision-cost
annotated uncertainty) — each uncertainty item must state which direction the
recommendation verb would shift if resolved. N_aspirational rises from 2 to 5.
Round 2 axes target the new ceiling: C-10 requires structural separation between
analysis and composition; C-11 requires visible derivation not just co-presence;
C-12 requires directional conditionals not generic acknowledgment of uncertainty.

The winning mechanisms from Round 1 are preserved: audience pressure (V-04 at
100/100), trailing tone instruction (cost-near-zero lift), and causal contrast
framing. The question is what single-axis mechanism reliably produces each new
criterion, and how those mechanisms combine without collision.

---

## V-01

**Variation axis**: Output format -- labeled block template for C-10/C-11/C-12
**Hypothesis**: C-10 requires a discrete labeled pattern statement; C-11 requires
a visible bridge from pattern to verb; C-12 requires directional conditionals per
uncertainty. All three share a root cause: the model embeds analysis inside prose
rather than producing it as a named, separable artifact. A template that provides
explicit labeled blocks -- "The pattern:", "This pattern produces:", "Uncertainty:
/ If resolved:" -- converts these from behaviors-to-infer into format slots to
fill. The template does not ask the model to discover the structure; it supplies
the structure and asks the model to fill it correctly. This tests whether format
prescription alone achieves what behavioral instruction cannot reliably elicit.

---

You are running `/topic:story` for a topic. The topic name is provided.

**What this skill produces**: A signal story -- an editorial synthesis for a team
lead who has 10 minutes and needs to know whether to proceed, pause, pivot, or
abandon. Not a summary of each signal. An interpretation of what the signals say
together, in the author's voice.

**Gather all signals.**
Glob `simulations/**/{topic}-*`. Read every artifact found.
Read `simulations/{topic}/strategy.md` if it exists.

---

### Step 1 -- Pre-composition pattern block

Before writing any narrative prose, complete this block. It is included verbatim
in the output as the opening of Beat 3.

```
The pattern: [one sentence naming the cross-signal pattern -- what two or more
signals show together that no single signal shows alone. If this sentence could
be derived from any single artifact, it is wrong. Name the convergence,
divergence, tension, or gap that is only visible across the set.]

This pattern produces a [proceed / pause / pivot / abandon] recommendation
because: [one sentence connecting the pattern directly to the recommendation
verb. The verb must follow from the pattern, not from individual findings.]
```

---

### Step 2 -- Uncertainty table

Before writing the narrative, complete this table. Each row covers one specific
open question that, if answered, could change the recommendation.

| # | Uncertainty | If resolved [direction A] | If resolved [direction B] |
|---|-------------|--------------------------|--------------------------|
| 1 | [name the open question] | recommendation shifts to [verb] | recommendation stays [verb] |

Minimum one row. Generic hedges ("more research needed") without naming the
question and the directional shift fail.

---

### Step 3 -- Signal story

Write the story now, using the pattern block and uncertainty table as anchors.
Structure:

1. **What we set out to understand** -- one sentence stating the original
   question.
2. **What the signals revealed** -- for each signal, one to two sentences: the
   key finding (not a summary) and why it matters for the pattern. Not
   exhaustive.
3. **What the signals say together** -- the pattern block from Step 1, verbatim,
   then the editorial synthesis in the author's voice: what the pattern means,
   why it matters, what it implies for the decision.
4. **What remains uncertain** -- the uncertainty table from Step 2, with editorial
   commentary on the most consequential item.
5. **The recommendation** -- restate the verb from the pattern block. Confirm that
   the pattern, not just the individual findings, is what drives this call.

Tone: editorial, not neutral. The author has a view. The story defends it.

---

## V-02

**Variation axis**: Lifecycle emphasis -- mandatory analysis pass before composition
**Hypothesis**: C-10's "pre-composition" qualifier means the pattern must exist
before narrative writing begins -- not be arrived at during composition. The
model's default is to discover the pattern while writing, which means the pattern
is embedded in prose rather than stated as a discrete artifact. A two-pass
structure with a hard gate between passes -- where Pass 1 produces a named
analysis document and Pass 2 writes from it -- enforces this sequencing. Unlike
V-01's template (which provides slots), this variation structures the process:
the model cannot start writing the story until it has completed a pattern
identification step and a directional uncertainty step as separate deliverables.
This tests whether process gates produce more reliable C-10 pass rates than
format slots alone, and whether the gate forces C-11 traceability as a
consequence.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs in two mandatory passes. Pass 1 is the analysis pass. Pass 2 is
the composition pass. Pass 2 does not begin until Pass 1 is fully complete.
Incomplete Pass 1 outputs are not acceptable.

---

### Pass 1 -- Signal analysis

**Gather.**
Glob `simulations/**/{topic}-*`. Read every artifact found.
Read `simulations/{topic}/strategy.md` if it exists.

**Produce the following three outputs in order:**

**Output 1.1 -- Key findings register**
For each artifact, one sentence: the single most important finding to carry
forward. Format: `{artifact-name}: {finding}`. If you would need to write more
than one sentence, you have not identified the key finding -- cut until one
sentence remains.

**Output 1.2 -- Cross-signal pattern statement**
Label: `The pattern:`
One sentence naming what two or more signals show together that no single
signal shows alone. Requirements: (a) it references at least two artifact
names from Output 1.1; (b) if the sentence could be derived by reading any
single artifact, it does not pass -- find the actual cross-signal result;
(c) it names a convergence, divergence, tension, or gap.

**Output 1.3 -- Decision-cost uncertainty register**
For each specific open question that, if resolved, would change the
recommendation:
- Name the question.
- State: if resolved [direction A], recommendation shifts to [verb].
- State: if resolved [direction B], recommendation remains [verb].
Minimum one entry. Generic uncertainty acknowledgments without directional
conditionals do not qualify.

---

### Pass 2 -- Story composition

Write the signal story from the three outputs above. The pattern statement from
Output 1.2 must appear verbatim in the story -- labeled "The pattern:" -- before
the recommendation. The recommendation verb must cite the pattern by name as its
basis. The uncertainty items from Output 1.3 must appear with their directional
conditionals intact.

Structure:

1. **What we set out to understand** -- the original question.
2. **What the signals revealed** -- key finding per signal, why it matters for
   the pattern. Not exhaustive.
3. **What the signals say together** -- begin with the verbatim pattern statement
   from Output 1.2. Then: editorial synthesis interpreting what the pattern means
   and why it is the right read of the evidence.
4. **What remains uncertain** -- the items from Output 1.3 with their directional
   conditionals. Name the most consequential.
5. **The recommendation** -- proceed, pause, pivot, or abandon. State explicitly:
   "The pattern -- [restate it] -- produces this call because [one sentence of
   logical connection]."

Tone: editorial, not neutral. A team lead has 10 minutes. Give them a view.

---

## V-03

**Variation axis**: Phrasing register -- formal conditional framing for C-12
**Hypothesis**: C-12's failure mode is that uncertainty items are stated in
descriptive terms ("we do not know X") rather than conditional terms ("if X
resolves to Y, the recommendation shifts"). The fix is a phrasing register
that treats uncertainty as a decision variable: each unknown is framed as an
if-then proposition with a stated directional consequence. This is a phrasing
discipline, not a structural one. It does not require a template or a process
gate -- it requires that the model learn the conditional form through explicit
instruction and example. This variation tests whether a phrasing-register
instruction with a single concrete example reliably elicits C-12 compliance
without imposing a template or process overhead, and whether that register also
improves C-11 by making the pattern-to-recommendation connection feel more
formally traceable.

---

You are running `/topic:story` for a topic. The topic name is provided.

**Gather all signals.**
Glob `simulations/**/{topic}-*`. Read every artifact found.
Read `simulations/{topic}/strategy.md` if it exists.

**What this skill produces**: An editorial synthesis for a team lead who has 10
minutes and must decide: proceed, pause, pivot, or abandon. Not a summary of
what each signal found. An interpretation of what the signals say together.

---

### Synthesis, not summary

The difference: summary reports what each signal found. Synthesis identifies
the pattern that only becomes visible when you look across all signals together.
If your story could be generated by reading one signal at a time and collecting
findings, it is a summary. The story you write cannot be generated that way.

---

### Pattern identification

Before writing the narrative, name the cross-signal pattern. Write it as a
labeled claim:

> **The pattern:** [one sentence naming what two or more signals show together
> that no single signal shows alone -- convergence, divergence, tension, or gap
> that is invisible in any single artifact.]

This sentence must appear verbatim in Beat 3 of the story. It is the analytical
claim the story defends.

---

### Uncertainty framing -- conditional register

For uncertainty, use the conditional register throughout:

Do not write: *"There is uncertainty about user adoption rate."*
Write instead: *"If adoption rate reaches threshold X, this moves from pause
to proceed. If it stays below threshold, the pause holds."*

Every uncertainty item must follow this form: name the question, then state
what direction the recommendation verb moves if resolved. An uncertainty that
does not affect the recommendation is not worth naming -- omit it. An
uncertainty that affects the recommendation but does not state the directional
consequence is incomplete -- add it.

---

### Story structure

1. **What we set out to understand** -- one sentence.
2. **What the signals revealed** -- one to two sentences per signal: the key
   finding and why it matters for the pattern. Not exhaustive enumeration.
3. **What the signals say together** -- the labeled pattern statement, then
   the editorial synthesis: why this is the right read, what it implies.
4. **What remains uncertain** -- each item in conditional register. Name the
   one that most threatens the recommendation.
5. **The recommendation** -- proceed, pause, pivot, or abandon. Connect it
   explicitly to the pattern: "The pattern -- [restate] -- points to [verb]
   because [one sentence of reasoning]."

Tone: editorial, not neutral. The author has a position. State it and defend it.
Do not hedge where the evidence is clear.

---

## V-04

**Variation axis**: Combination -- output format template (V-01) + analysis-first
lifecycle (V-02 Pass 1)
**Hypothesis**: V-01 provides labeled slots that structurally require C-10/C-11/
C-12 artifacts. V-02 provides the process gate that ensures C-10 is genuinely
pre-composition (not post-hoc insertion into a template slot). Neither alone
guarantees both properties: V-01's template could be filled during composition;
V-02's pass structure could produce a pattern statement without forcing it to be
a discrete labeled artifact in the story. Combined, the process gate ensures
sequencing and the template ensures the artifact's structural independence.
This also inherits the strongest R1 mechanism -- audience pressure from R1 V-04
(team lead, 10 minutes, accountable for the call).

---

You are running `/topic:story` for a topic. The topic name is provided.

A team lead has 10 minutes and must decide whether to proceed, pause, pivot,
or abandon this topic. Your job: give them a view they can act on. Not a
summary of what was found. An editorial synthesis of what the signals say
together, in the author's voice.

This skill runs in two passes. Pass 1 is analysis. Pass 2 is composition.
Pass 2 does not begin until Pass 1 is complete.

---

### Pass 1 -- Analysis

**Gather.**
Glob `simulations/**/{topic}-*`. Read every artifact.
Read `simulations/{topic}/strategy.md` if it exists.

**Complete the following three outputs:**

**Output A -- Key findings register**
`{artifact-name}: {single most important finding}` per artifact.
One sentence. If you need two, cut until one remains.

**Output B -- Pattern block** (appears verbatim in Pass 2, Beat 3)
```
The pattern: [what two or more signals show together that no single signal
shows alone -- convergence, divergence, tension, or gap invisible in any
single artifact. Reference at least two artifact names. If this sentence
could come from reading one artifact, find the real pattern.]

This pattern produces a [proceed / pause / pivot / abandon] recommendation
because: [one sentence connecting pattern to verb directly.]
```

**Output C -- Uncertainty register** (rows appear in Pass 2, Beat 4)
For each uncertainty that, if resolved, would change the recommendation:

| # | Uncertainty | If [direction A] | If [direction B] |
|---|-------------|-----------------|-----------------|
| 1 | [question]  | shifts to [verb] | stays [verb]    |

Minimum one row. Generic hedges without directional conditionals are rejected.

---

### Pass 2 -- Composition

Write the story from Pass 1 outputs. The pattern block from Output B must appear
verbatim, labeled "The pattern:", before the recommendation. The uncertainty
rows from Output C must appear with their directional conditionals intact.

Structure:

1. **What we set out to understand** -- one sentence.
2. **What the signals revealed** -- key finding per signal from Output A, plus
   one sentence on why it matters for the pattern. Not a catalog.
3. **What the signals say together** -- verbatim pattern block from Output B,
   followed by editorial synthesis: what the pattern means for this decision
   and why it is the right read.
4. **What remains uncertain** -- uncertainty rows from Output C with directional
   conditionals. Name the most consequential.
5. **The recommendation** -- restate the verb from the pattern block. Cite the
   pattern explicitly: "The pattern -- [restate] -- produces this call because
   [one sentence]."

Tone: editorial, not neutral. The team lead needs a view, not a report.
The author has read all the signals. The author has a position. State it.

---

## V-05

**Variation axis**: Combination -- phrasing register (V-03) + audience pressure
(R1 V-04) + explicit pattern-to-recommendation bridge instruction (C-11)
**Hypothesis**: V-03 establishes the conditional register for C-12 through phrasing
discipline. R1's V-04 mechanism (audience pressure: named decision-maker, 10
minutes) is the strongest single lift for editorial voice (C-05/C-08). Neither
addresses C-11 directly: pattern and recommendation can both be present but
unconnected. C-11 requires not just co-presence but a visible logical derivation
-- the story must contain the sentence "The pattern -- [restate] -- produces this
call because [X]." Adding a single explicit bridge instruction with revision
pressure ("if you cannot write this sentence, your pattern and recommendation are
not actually connected -- revise one of them") targets C-11 as a behavioral
instruction rather than a structural slot. The combination tests whether three
behavioral instructions (conditional register + audience pressure + bridge
instruction with revision pressure) produce the same reliability as structural
templates, with less format overhead.

---

You are running `/topic:story` for a topic. The topic name is provided.

**Gather all signals.**
Glob `simulations/**/{topic}-*`. Read every artifact found.
Read `simulations/{topic}/strategy.md` if it exists.

**The reader**: A principal engineer or team lead who has 10 minutes and is
accountable for the proceed/pause/pivot/abandon call on this topic. They have
not read the signals. They need a view, not a bibliography. Give them yours.

---

### Rule 1 -- Synthesis, not summary

Do not write: *"The scout signal found competitive alternatives in the
enterprise tier. The draft signal proposed a three-tier architecture."*
Write instead: *"The competitive landscape and the architecture proposal
converge on the same constraint -- time-to-first-value determines adoption --
a gap neither signal named but both expose."*

The first form reports what each signal found. The second form states what
the signals show together. Write the second form throughout.

---

### Rule 2 -- Name the pattern before you write

Before composing the narrative, write this labeled claim:

> **The pattern:** [one sentence -- what two or more signals show together that
> no signal shows alone. Reference artifact names. Name the convergence,
> divergence, tension, or gap that only appears at the intersection.]

This sentence is the thesis of your story. Everything in the story either
supports, qualifies, or applies it. It must appear verbatim in Beat 3.

---

### Rule 3 -- Uncertainty as decision variables

For each thing you do not yet know:
- Name it precisely.
- State: if this resolves [direction A], the recommendation shifts to [verb].
- State: if this resolves [direction B], the recommendation holds at [verb].

Do not name an uncertainty that has no directional consequence -- it is noise.
Do not name an uncertainty without stating its directional consequence -- it is
incomplete.

Example: *"If the API rate-limit constraint is lifted, this moves from pause
to proceed. If confirmed as permanent, it moves toward pivot or abandon."*

---

### Rule 4 -- Make the derivation visible

The recommendation must be visibly derived from the pattern, not from the
accumulation of individual findings. Write the bridge explicitly:

> "The pattern -- [restate it] -- produces a [verb] call because [one sentence
> of logical connection between pattern and verb]."

If you cannot write this sentence, your pattern and recommendation are not
actually connected. Revise one of them.

---

### Story structure

1. **What we set out to understand** -- one sentence.
2. **What the signals revealed** -- key finding per signal plus why it matters
   for the pattern. Synthesis register throughout (Rule 1). Not exhaustive.
3. **What the signals say together** -- verbatim pattern statement (Rule 2),
   then editorial synthesis: why this is the right read of the evidence.
4. **What remains uncertain** -- each item in decision-variable form (Rule 3).
   Name which uncertainty most threatens the recommendation.
5. **The recommendation** -- verb, followed by the explicit derivation bridge
   (Rule 4). The pattern, not the individual findings, drives this call.

Tone: editorial, not neutral. The author has read everything. The author has
a position. The team lead does not have time for equivocation.

---

## Design notes -- Round 2

### What each variation targets

| Variation | C-10 mechanism | C-11 mechanism | C-12 mechanism |
|-----------|---------------|----------------|----------------|
| V-01 | Template slot "The pattern:" | Template slot "This pattern produces:" | Uncertainty table with direction columns |
| V-02 | Process gate -- Output 1.2 before Pass 2 | Recommendation step requires pattern cite | Decision-cost register (Output 1.3) |
| V-03 | Labeled claim instruction + verbatim requirement | Bridge sentence at recommendation step | Conditional register + example + omit-if-no-consequence |
| V-04 | V-01 slot + V-02 gate (double enforcement) | V-01 slot + V-02 step instruction | V-01 table + V-02 register |
| V-05 | Named rule + verbatim requirement | Rule 4 + revision pressure | Rule 3 + example + omit-if-noise |

### Predicted discriminators

**C-10**: V-04 most reliable (template slot + process gate). V-02 and V-01 likely
pass. V-03 and V-05 depend on behavioral compliance -- may produce labeled claims
still embedded in prose rather than structurally independent.

**C-11**: V-04 and V-05 have the strongest mechanisms. V-04 provides slot +
step instruction. V-05's Rule 4 adds revision pressure ("if you cannot write
this sentence, revise"). V-01 provides a slot but no revision pressure if the
slot is filled weakly.

**C-12**: V-01's table format is most explicit -- column headers force direction.
V-03 and V-05 use the conditional example which may be sufficient. V-02's
register is explicit but prose-form and may produce inconsistent conditionals.

### R1 mechanism preservation

All variations preserve the anti-summary distinction (rule or explicit framing).
V-04 and V-05 preserve audience pressure (team lead / principal engineer, 10
minutes, accountable). Trailing tone instruction ("editorial, not neutral")
appears in V-01, V-02, V-04, V-05. V-03 closes with an equivalent ("the author
has a position -- state it and defend it").

### Highest-probability golden candidate

**V-04**: inherits R1's strongest mechanism (audience pressure), doubles down on
C-10 (template slot + process gate), strongest C-11 (slot + step), most
explicit C-12 (table with direction columns). Expected composite: 95-100.

**V-05**: strongest C-11 framing (Rule 4 includes revision pressure absent in
V-04). If C-11 is the hardest new criterion, V-05 may outperform on that
specific criterion. Expected composite: 90-100 depending on C-12 consistency.
