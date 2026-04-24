# topic-story Variations V-01 through V-05 (Rubric v6)

---

## V-01 — Role Sequence (Signal Analyst → Bridge Builder → Narrator, strict order)

**Variation axis**: Role sequence  
**Hypothesis**: Enforcing three named roles in strict completion order prevents the narrator from composing prose before the pattern and delta have been analytically determined, satisfying C-10, C-15, C-18 structurally rather than by instruction.

---

```
You are producing a `topic-story` signal artifact for the Signal plugin.

A topic-story is NOT a summary of individual signals. It is an editorial synthesis
in the author's voice that interprets what the signals say TOGETHER. You will produce
this output in two mandatory parts. Part 1 is analytic pre-composition. Part 2 is the
narrative. A role may not begin until the role before it has fully completed its block.

---

# PART 1 — ANALYTIC PRE-COMPOSITION

## Role: Signal Analyst

Read the available signals. Produce only labeled outputs — no narrative prose.

### Signal Inventory
List each distinct signal by namespace and artifact type. You must identify at least
three distinct namespaces. If fewer than three are available, name what is missing.

### Evidence Posture
One phrase. Choose exactly one: strong positive / mixed / conflicting / weak / negative.
No hedges. This label will be required again in Beat 5 of Part 2.

### Key Finding per Signal
For each signal: one sentence naming the finding that matters most for the decision.
Not a summary — the one thing that changes or confirms what we know.

---

## Role: Bridge Builder

Read the Signal Analyst's block. Produce only labeled outputs — no narrative prose.

### Pattern Block
State the cross-signal pattern as a single, self-contained sentence. It must:
- Name a relationship, tension, or gap that no single signal reveals alone
- Stand without the surrounding narrative (C-14)
- Be labeled: `The pattern: [sentence]`

This block is produced here in Part 1. It is also required in Beat 3 of Part 2.
Production here does NOT satisfy the Beat 3 requirement. Both placements must be
independently satisfied. (C-19)

### Delta Block
State the contrastive discovery as a single sentence: "We expected X but found Y."
This must reflect a genuine surprise, not a reformulation of the pattern.
Label it: `The delta: [sentence]`

This block is produced here in Part 1. It is also required in Beat 2 of Part 2.
Production here does NOT satisfy the Beat 2 requirement. Both placements must be
independently satisfied. (C-19)

### Recommendation Verb
One word: proceed / pause / pivot / abandon. No hedging.

### Bridge Sentence
State the explicit connection in this form:
"Because [the named pattern], the recommendation is [verb]."

This sentence is produced here in Part 1. It is also required in Beat 5 of Part 2.
Production here does NOT satisfy the Beat 5 requirement. Both placements must be
independently satisfied. (C-19)

---

# PART 2 — NARRATIVE

The Narrator writes the five-beat story. All analytic artifacts from Part 1 must be
restated at their designated positions in Part 2. Prior placement in Part 1 does not
satisfy Part 2 placement requirements. (C-19)

The story must open with the recommendation — not build toward it. A story that opens
with context-setting or hedging fails. (C-01)

## Role: Narrator

---

**BLUF** (before Beat 1)
One sentence stating the recommendation directly, before any labeled section begins.
Example: "The evidence recommends [verb]: [one-sentence rationale]."

---

**Beat 1 — What we set out to understand**
State the question the team needed to answer. One short paragraph. The intent must
be clear enough that a reader unfamiliar with the topic can follow what follows.

---

**Beat 2 — What the signals revealed**
Cover each signal with its key finding — one finding per signal, not a full summary.
Include the Delta Block from Part 1 as a stated contrast at a natural point in this
beat. The delta must appear as an explicit "we expected X but found Y" statement, not
as an inference from surrounding context. (C-09, C-15)

---

**Beat 3 — What the signals say together**
Open this beat with the Pattern Block from Part 1, restated verbatim or nearly so.
The pattern must appear as a discrete, labeled statement — not embedded in flowing
prose. (C-10, C-14) This restatement is independent of the Part 1 placement. (C-19)
Continue the beat by explaining what the pattern means for the decision.

---

**Beat 4 — What remains uncertain**
Name at least one specific open question. For each, state explicitly:
"If [this question] resolves to [X], the recommendation moves from [current verb]
to [alternate verb]." Generic hedges without a direction fail. (C-06, C-12)

---

**Beat 5 — The recommendation**
This beat must contain all three of the following, in this order:

1. Evidence posture restatement: "The overall signal posture is [posture from Part 1],
   which produces a [verb] recommendation." (C-16)
   Note: posture named in Part 1 AND here — inconsistency between placements is
   self-revealing. (C-20)

2. Bridge sentence from Part 1, restated: "Because [the named pattern], the
   recommendation is [verb]." (C-17) This restatement is independent of the Part 1
   placement. (C-19) Note: pattern and verb both named in Part 1 AND here —
   inconsistency is self-revealing. (C-20)

3. Decision-grounded close: name who is making this decision and under what
   constraint. State it as a decision ("a team deciding X should do Y") not as a
   finding ("the signals suggest X"). (C-13)

---

Topic: {{topic}}
Available signals: {{signals}}
```

---

## V-02 — Output Format (Pre-composition as a structured table)

**Variation axis**: Output format  
**Hypothesis**: Collecting all pre-composition artifacts in a single named table with explicit columns — Artifact / Content / Required Again In — makes the non-substitution rule visible at a glance and the Part 1 → Part 2 gate structurally verifiable without per-artifact instruction.

---

```
You are producing a `topic-story` signal artifact for the Signal plugin.

A topic-story synthesizes what signals say TOGETHER — not what each signal says
individually. The output is structured in two mandatory parts separated by a visible
gate. Do not write Part 2 until Part 1 is complete.

---

# PART 1 — PRE-COMPOSITION TABLE

Complete this table before writing any narrative prose. Every cell must be filled.
Leaving a cell empty is equivalent to not producing the artifact.

| Artifact | Content | Required Again In |
|---|---|---|
| **Signal inventory** | List each signal namespace and artifact type present. Minimum 3 distinct namespaces. | Beat 2 (coverage) |
| **Evidence posture** | One of: strong positive / mixed / conflicting / weak / negative. One phrase only. | Beat 5 (C-16) |
| **Pattern** | `The pattern: [one self-contained sentence naming a relationship, tension, or gap that no single signal shows alone]` | Beat 3, opening sentence (C-10) |
| **Delta** | `The delta: We expected [X] but found [Y].` One sentence. Must be a genuine surprise. | Beat 2, as stated contrast (C-09) |
| **Recommendation verb** | proceed / pause / pivot / abandon. One word. | Beat 5 (C-07) |
| **Bridge sentence** | `Because [the named pattern], the recommendation is [verb].` | Beat 5 (C-17) |

### Non-substitution rule
Each artifact in the "Required Again In" column must be restated independently at the
named beat. The table is an analytic record, not a reusable reference. Pointing a
reader to the table does not satisfy a beat-level placement requirement. (C-19)

### Multi-stage consistency rule
The evidence posture, pattern, and bridge sentence appear in this table AND in the
narrative beats named above. If the content differs between the table and the beat,
the output is inconsistent. Inconsistency between the two placements is structurally
visible and constitutes a failure. (C-20)

---

# PART 2 — NARRATIVE

The five beats below constitute the topic-story. Each beat has a required label.
Do not rename beats. Do not merge beats. Do not omit beats.

The story must open with the recommendation before the first labeled beat. A story
that builds to the recommendation fails. (C-01)

---

**BLUF**
One sentence. State the recommendation directly: "The evidence recommends [verb]:
[brief rationale]." This appears before Beat 1.

---

**Beat 1 — What we set out to understand**
The question the team needed to answer. One short paragraph. State the intent so a
reader unfamiliar with the topic can follow the reasoning that follows.

---

**Beat 2 — What the signals revealed**
For each signal: one sentence stating the key finding that matters most for the
decision. Include the delta from the pre-composition table as an explicit "we expected
X but found Y" statement. The delta must be stated, not implied. (C-09)

---

**Beat 3 — What the signals say together**
Open with the pattern from the pre-composition table, restated verbatim or nearly so
as a discrete labeled statement: `The pattern: [sentence]`. Do not bury the pattern
in flowing prose. (C-10, C-14) Explain what the pattern means for the decision.

---

**Beat 4 — What remains uncertain**
Name at least one specific open question. For each, state the decision cost:
"If [this] resolves to [X], this moves from [current verb] to [alternate verb]."
No generic hedges. (C-06, C-12)

---

**Beat 5 — The recommendation**
Include all three in order:

1. **Posture statement** (C-16): "The overall signal posture is [posture], which
   produces a [verb] recommendation." Posture must match the pre-composition table.

2. **Bridge sentence** (C-17): "Because [the named pattern], the recommendation is
   [verb]." Pattern and verb must match the pre-composition table. This restatement
   is independent of the table. (C-19)

3. **Decision close** (C-13): Name the decision-maker role and constraint. State this
   as a decision, not a finding. "A [role] deciding [question] should [action]."

---

Topic: {{topic}}
Available signals: {{signals}}
```

---

## V-03 — Lifecycle Emphasis (Explicit gate, per-placement non-substitution)

**Variation axis**: Lifecycle emphasis  
**Hypothesis**: Stating the non-substitution rule at every individual placement point — rather than once globally — prevents any placement from being treated as satisfying another, satisfying C-19 through instruction density rather than structural form.

---

```
You are producing a `topic-story` signal artifact for the Signal plugin.

The topic-story interprets what signals say together. It is NOT a signal summary.
It has a mandatory two-part structure. Part 1 must be complete before Part 2 begins.

---

# PART 1 — ANALYTIC STAGE

Produce the following labeled outputs. No narrative prose in Part 1.

**[A] Signal coverage**
List all signal namespaces and artifact types represented in the available signals.
At least three distinct namespaces must be identifiable. This list informs Beat 2
coverage — it is not a reusable reference; Beat 2 must name coverage independently.

**[B] Evidence posture**
Label: `Posture: [phrase]`
Choose exactly one: strong positive / mixed / conflicting / weak / negative.
— This posture is first named here.
— It is required again in Beat 5.
— The placement here does not satisfy Beat 5. Beat 5 must state posture independently.
— If Beat 5 posture differs from this, the output is inconsistent. (C-20)

**[C] Pattern**
Label: `The pattern: [sentence]`
One self-contained sentence naming a relationship, tension, or gap that no single
signal alone reveals. The sentence must be readable without surrounding context.
— This pattern is first named here.
— It is required again as the opening statement of Beat 3.
— The placement here does not satisfy Beat 3. Beat 3 must restate it independently.
— If Beat 3 pattern differs from this, the output is inconsistent. (C-20)

**[D] Delta**
Label: `The delta: We expected [X] but found [Y].`
One sentence. A genuine surprise from the signals — not a restatement of the pattern.
— This delta is first identified here.
— It is required again in Beat 2 as an explicit stated contrast.
— The placement here does not satisfy Beat 2. Beat 2 must include it independently.

**[E] Recommendation verb**
Label: `Verb: [word]`
One of: proceed / pause / pivot / abandon. One word only.
— This verb is first named here.
— It is required in Beat 5 as part of the posture statement and the bridge sentence.
— The placement here does not satisfy Beat 5. Both Beat 5 uses must be independent.

**[F] Bridge sentence**
Label: `Because [the named pattern from C], the recommendation is [verb from E].`
— This sentence is first constructed here.
— It is required again in Beat 5.
— The placement here does not satisfy Beat 5. Beat 5 must include it independently.
— If Beat 5 bridge sentence differs from this, the output is inconsistent. (C-20)

---

⬇ GATE — Part 2 begins only after all six analytic outputs above are complete ⬇

---

# PART 2 — NARRATIVE STAGE

Write the topic-story. The story opens with the recommendation — not with context,
not with hedging, not with the question being studied. A story that builds to the
recommendation fails. (C-01)

---

**BLUF**
Before Beat 1, state the recommendation in one sentence:
"The evidence recommends [verb]: [brief rationale]."

---

**Beat 1 — What we set out to understand**
State the question the team needed to answer. Short paragraph. Clear enough that a
reader unfamiliar with the topic can follow the reasoning that follows.

---

**Beat 2 — What the signals revealed**
For each signal: one sentence on the key finding. Include the delta from [D] here as
a stated contrast — "We expected X but found Y" — not as an inference.
This is an independent restatement of [D]. The Part 1 placement does not satisfy this
requirement. (C-09, C-19)

---

**Beat 3 — What the signals say together**
Open with the pattern from [C] as a discrete labeled statement:
`The pattern: [sentence]`
This is an independent restatement of [C]. The Part 1 placement does not satisfy this
requirement. (C-10, C-14, C-19) Explain what the pattern means for the decision.

---

**Beat 4 — What remains uncertain**
Name at least one specific open question with an explicit decision cost:
"If [X] resolves to [Y], this moves from [current verb] to [alternate verb]."
Hedges without a stated direction fail. (C-06, C-12)

---

**Beat 5 — The recommendation**
This beat must contain the following three elements, each independently placed here.
Prior occurrence in Part 1 does not satisfy any of these requirements. (C-19)

1. Posture statement (independent of [B]):
   "The overall signal posture is [posture], which produces a [verb] recommendation."
   Posture must match [B]. If it differs, the output is inconsistent. (C-16, C-20)

2. Bridge sentence (independent of [F]):
   "Because [the named pattern], the recommendation is [verb]."
   Pattern and verb must match [C] and [E]. If they differ, the output is
   inconsistent. (C-17, C-20)

3. Decision close (C-13):
   Name who is deciding and under what constraint. State it as a decision:
   "A [role] deciding [question] should [action]." Not: "the signals suggest X."

---

Topic: {{topic}}
Available signals: {{signals}}
```

---

## V-04 — Role Sequence + Phrasing Register (conversational directive)

**Variation axis**: Role sequence + phrasing register  
**Hypothesis**: Directive second-person conversational language with named roles reduces friction and ambiguity in following the analytic sequence, at the cost of formality — testing whether tone affects compliance with the structural requirements.

---

```
You are producing a topic-story for the Signal plugin.

Here's what it is: not a summary. A story that tells what the signals mean TOGETHER —
the pattern that only appears when you put them side by side. Your job is to find that
pattern analytically, then write the story from it.

You'll do this in two stages. Don't start Stage 2 until Stage 2 is done. I mean it —
the story should come from the analysis, not the other way around.

---

# STAGE 1 — FIGURE IT OUT FIRST

Run through these three steps in order.

---

## Step 1: Survey (you are the Analyst)

Don't synthesize yet. Just take stock.

**What signals do you have?**
List them by namespace and artifact type. You need at least three distinct namespaces.
If you don't have three, name what's missing.

**What does each signal show?**
For each signal: one sentence, the finding that matters most for the decision. Not
everything the signal says — just the one thing that moves the needle.

**What's the overall posture?**
Name it: strong positive / mixed / conflicting / weak / negative. Pick one.
You'll need to state this again in your recommendation. If you change your mind later,
that's a problem — the two statements must match.

---

## Step 2: Synthesize (you are the Bridge Builder)

Now put the signals together.

**Name the pattern.**
Write this sentence: `The pattern: [what the signals show TOGETHER that no single
signal shows alone]`

The sentence has to stand on its own. If it only makes sense after reading the story
around it, rewrite it. This sentence will appear again — verbatim or close to it —
as the first sentence of Beat 3. Writing it here does not satisfy that requirement;
you'll need to include it again there.

**Name the delta.**
Write this sentence: `The delta: We expected [X] but found [Y].`

This is the biggest surprise — the place where the evidence contradicted what you
would have assumed going in. It can't be a restatement of the pattern. This sentence
will appear again in Beat 2 as an explicit contrast. Writing it here does not satisfy
that requirement.

**Pick your verb.**
One word: proceed / pause / pivot / abandon.

**Write the bridge.**
`Because [the named pattern], the recommendation is [verb].`

This sentence must appear in your recommendation beat. Writing it here does not
satisfy that requirement.

---

## Step 3: Sanity check (still the Bridge Builder)

Before you start writing the story:
- Does your verb match your posture? Strong positive → proceed. Mixed → pause.
  Conflicting → pivot. Weak or negative → abandon. If the verb and posture don't
  match, fix one of them.
- Does your bridge sentence actually name the pattern? If it gestures at the pattern
  without naming it, rewrite it.
- Is your delta genuinely surprising, or is it just the pattern in different words?
  If the latter, find the real surprise.

---

# STAGE 2 — WRITE THE STORY

Now write the topic-story. Lead with the recommendation — do not build toward it.
A story that saves the recommendation for the end fails.

---

**The short version** (before any labeled section)
One sentence: "The evidence recommends [verb]: [brief rationale]."

---

**Beat 1 — What we set out to understand**
What question was the team trying to answer? One short paragraph. Write it so that
someone who hasn't seen the signals can follow what comes next.

---

**Beat 2 — What the signals revealed**
One key finding per signal. Then, somewhere in this beat, include your delta — stated
as "we expected X but found Y," not implied by the surrounding text. This is a
separate placement from Step 2; the delta must appear here independently.

---

**Beat 3 — What the signals say together**
Start with your pattern sentence: `The pattern: [sentence]`
Don't bury it in a paragraph. Lead with it. This is a separate placement from Step 2;
write it here as if the reader hasn't seen it yet. Then explain what it means for the
decision.

---

**Beat 4 — What remains uncertain**
Name at least one specific open question. For each one, say what happens to the verb
if it resolves one way or the other: "If X turns out to be Y, this moves from [verb]
to [alternate verb]." No generic "more research is needed" without naming the research
and what it changes.

---

**Beat 5 — The recommendation**
Three things, in this order. All three must appear in this beat — prior occurrences
elsewhere don't count.

First: "The overall signal posture is [posture], which produces a [verb]
recommendation." The posture must match Step 1. If it doesn't, go back and fix it.

Second: "Because [the named pattern], the recommendation is [verb]." The pattern and
verb must match Step 2. If they don't, go back and fix them.

Third: Name who is deciding and under what constraint. Write it as a decision, not a
finding. "A [role] deciding [question] should [action]" — not "the signals suggest X."

---

Topic: {{topic}}
Available signals: {{signals}}
```

---

## V-05 — Output Format + Inertia Framing (table + status-quo competitor)

**Variation axis**: Output format + inertia framing  
**Hypothesis**: Combining the pre-composition table format with explicit "without this story, the team would default to X" framing forces the recommendation to name and defeat the counterfactual default, strengthening C-13 while using table structure to satisfy C-18.

---

```
You are producing a `topic-story` signal artifact for the Signal plugin.

A topic-story answers one question: given everything the signals show together, what
should this team do? It is not a signal summary. It is an editorial synthesis that
finds the cross-signal pattern and delivers a recommendation that a decision-maker
can act on — not a finding they have to interpret.

The output has two mandatory parts. Complete Part 1 before beginning Part 2.

---

# PART 1 — PRE-COMPOSITION TABLE

Fill every row. Incomplete rows constitute an incomplete analysis.

| # | Artifact | Your Output |
|---|---|---|
| 1 | **Signal inventory** | [List each signal by namespace and artifact type. Min 3 distinct namespaces.] |
| 2 | **Evidence posture** | `Posture: [strong positive / mixed / conflicting / weak / negative — one only]` |
| 3 | **Key finding per signal** | [One sentence per signal. The finding that matters most for the decision.] |
| 4 | **Pattern** | `The pattern: [one self-contained sentence — relationship, tension, or gap that no single signal shows alone]` |
| 5 | **Delta** | `The delta: We expected [X] but found [Y].` |
| 6 | **Status quo default** | `Without this story, the team would [default action or assumption].` |
| 7 | **Recommendation verb** | `Verb: [proceed / pause / pivot / abandon]` |
| 8 | **Bridge sentence** | `Because [row 4 pattern], the recommendation is [row 7 verb].` |
| 9 | **Decision-maker + constraint** | `A [role] deciding [question] under [constraint].` |

### Table rules

**Non-substitution** (C-19): Each artifact in the table is required at its designated
beat in Part 2. The table is an analytic record — not a reusable source. Citing the
table does not satisfy a beat-level placement. Each beat placement must be
independently stated.

**Multi-stage consistency** (C-20): Rows 2, 4, 7, and 8 appear in both the table and
in designated beats. If the content differs between the table and the beat, the output
is inconsistent. Inconsistency between the two placements is structurally visible and
constitutes a failure.

**Verb-posture calibration** (C-07): Row 7 must follow from row 2. Strong positive →
proceed. Mixed → pause. Conflicting → pivot. Weak or negative → abandon. A verb that
contradicts the posture fails.

---

# PART 2 — NARRATIVE

The story opens with the recommendation. It does not build toward the recommendation.
A story that saves the recommendation for a final section fails. (C-01)

---

**BLUF** (before any labeled beat)
"The evidence recommends [verb]: [brief rationale]."

---

**Beat 1 — What we set out to understand**
The question the team needed to answer. One paragraph. Clear enough that a reader
unfamiliar with the topic can follow the reasoning from here to the recommendation.

---

**Beat 2 — What the signals revealed**
One key finding per signal. Include the delta from row 5 as an explicit stated
contrast. Must appear as "we expected X but found Y" — not implied from context.
This is independent of the table. (C-09, C-19)

---

**Beat 3 — What the signals say together**
Open with the pattern from row 4 as a discrete, labeled statement:
`The pattern: [sentence]`
Do not embed the pattern in flowing prose. (C-10, C-14) This is independent of the
table. (C-19) Follow with what the pattern means for the decision.

---

**Beat 4 — What remains uncertain**
Name at least one specific open question with explicit decision cost:
"If [X] resolves to [Y], this moves from [current verb] to [alternate verb]."
Hedges without a direction fail. (C-06, C-12)

---

**Beat 5 — The recommendation**
Must contain all five elements below. Each is independent of the table. (C-19)

1. **Posture statement** (C-16): "The overall signal posture is [posture from row 2],
   which produces a [verb] recommendation." Must match row 2. (C-20)

2. **Bridge sentence** (C-17): "Because [the named pattern from row 4], the
   recommendation is [verb from row 7]." Must match rows 4 and 7. (C-20)

3. **Inertia displacement** (C-13): Name and directly address the status-quo default
   from row 6: "Without this evidence, the team would [default]. The signals change
   this because [specific reason]." The recommendation must defeat the counterfactual,
   not merely state a verdict.

4. **Decision-grounded close** (C-13): Use row 9 to frame the decision: "A [role]
   deciding [question] under [constraint] should [action]." State as a decision, not
   a finding.

5. **Consistency checkpoint** (C-20): After writing this beat, confirm that posture,
   pattern, and bridge sentence in this beat match rows 2, 4, and 8 respectively. If
   any differ, return to the table and reconcile before submitting.

---

Topic: {{topic}}
Available signals: {{signals}}
```

---

## Summary

| Variation | Axis | Core Innovation | Primary Criteria Targeted |
|---|---|---|---|
| V-01 | Role sequence | Three named roles in strict completion order; roles are the structural gate | C-10, C-15, C-18 |
| V-02 | Output format | Single pre-composition table with explicit "Required Again In" column | C-18, C-19, C-20 |
| V-03 | Lifecycle emphasis | Non-substitution stated at every individual placement point | C-19, C-20 |
| V-04 | Role sequence + phrasing register | Same three-role sequence but in directive conversational language | C-01, C-07, C-16, C-17 |
| V-05 | Output format + inertia framing | Table format with status-quo competitor row forcing counterfactual defeat | C-13, C-17, C-19, C-20 |

**Recommended test order**: V-01 and V-02 are the sharpest single-axis tests. Run them first to isolate whether role-sequence or table-format does more work on C-18/C-19. V-05 is the strongest candidate for C-13 compliance if that criterion is currently the gap.
