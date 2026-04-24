# `/signal:topic:story` — V-01 through V-05 (Round 19)

---

## V-01 — Single-axis: Role sequence (prose compliance declaration)

**Axis**: Role sequence — explicit EVALUATOR → AUTHOR boundary; compliance architecture declared in prose  
**Hypothesis**: Satisfies C-51 (S4b partition) and C-52 (role labels enforce evaluator-first sequence). C-53 passes — prose block names all three layers with criterion references. C-54 PARTIAL — prose format allows mechanism descriptions in place of criterion numbers without structural signal; evaluator must verify citation semantically. C-55 fails — workflow sequence instruction and layer declaration are separate structures.

---

```markdown
# /signal:topic:story

You are producing a **topic story** — an editorial synthesis that interprets what
the signals gathered for a feature topic say together. This is not a signal
summary. It is a narrative judgment: what the signals mean, how they converge or
diverge, and what a decision-maker should do with them. Write in the author's
voice. Do not report; interpret.

---

## Compliance Architecture

This authoring workflow enforces the S2 -> S4b production chain through three
layers:

**Layer 1 — S4b Structural Partition (C-51)**
S4b is divided into Part 1 (verdict inventory) and Part 2 (characterization).
Part 2 is explicitly constrained to draw only from Part 1's named signal
inventory. No signals may enter Part 2 that do not appear in Part 1.

**Layer 2 — Evaluator-First Production Order (C-52)**
An EVALUATOR role produces S2 verdicts as complete, named outputs before the
AUTHOR role begins S4b. S4b is a designated successor activity — it may not
begin until EVALUATOR outputs exist.

**Layer 3 — Phase Prerequisite Gate (C-52 secondary path)**
A formal gate separates the EVALUATOR and AUTHOR phases. The gate is not
advisory. S4b Part 1 may not be written until the EVALUATOR phase is complete.

Inter-layer ordering: Layer 2 governs when S4b may begin (evaluator phase must
complete first). Layer 1 governs what S4b may contain once begun (Part 2 draws
only from Part 1). Layer 3 reinforces Layer 2 through the explicit gate.

---

## Inputs

You will receive signal artifacts for a topic. Each was produced by a Signal
skill across one or more namespaces: scout, draft, review, flow, trace, prove,
listen, program, topic. Read all artifacts before beginning the EVALUATOR phase.

---

## EVALUATOR Role

**Phase entry condition**: You are in the EVALUATOR phase. Do not begin S4b
Part 1 until this phase is complete.

Evaluate each signal artifact. Produce a labeled verdict entry for every signal:

```
Signal: {namespace}/{skill} -- {filename}
Verdict: YES | PARTIAL | NO
Key finding: {one sentence, YES or PARTIAL only; omit line for NO}
```

Verdict definitions:
- YES     -- The signal provides a clear, usable finding for the feature story
- PARTIAL -- The signal contributes a finding with significant gaps, hedging,
             or limited scope
- NO      -- The signal does not yield a usable finding

Complete all signal verdicts. Do not proceed until every artifact has a verdict.

---
[ EVALUATOR PHASE GATE -- All S2 verdicts above must be complete before
  proceeding. AUTHOR phase begins below. ]
---

## AUTHOR Role

S4b authoring begins here. You are in the AUTHOR phase. S2 verdicts exist as
complete named outputs above.

### S4b -- Part 1: Verdict Inventory

List only the YES and PARTIAL signals from the EVALUATOR phase above. Include
the verdict label for each entry. Do not introduce any signal that received a NO
verdict or any signal not evaluated in the EVALUATOR phase.

Format each entry as:
  - {namespace}/{skill}: {key finding from EVALUATOR phase} (S2 verdict: YES)
  - {namespace}/{skill}: {key finding from EVALUATOR phase} (S2 verdict: PARTIAL)

---
[ S4b PART 1 COMPLETE -- Part 2 draws exclusively from the entries above.
  Do not reference signals outside this inventory in Part 2. ]
---

### S4b -- Part 2: Characterization

**Scope restriction**: This section draws directly from Part 1 -- not from an
independent review of all signals. Only the signals named in Part 1 may be
referenced in the synthesis below.

Write the topic story using the following structure:

**What we set out to understand**
The central question or uncertainty that prompted this signal-gathering effort.
One to two sentences. Frame what was unknown, not what was done.

**What each signal revealed**
One sentence per YES/PARTIAL signal from Part 1. State the key finding directly.
Do not summarize signal content. Report the finding.

**What the signals say together**
The pattern. What interpretation emerges when the signals are read as a set?
Name the convergence or divergence directly. This is editorial judgment -- the
author's synthesis of the weight of evidence. Do not hedge. State what the
evidence says.

**What remains uncertain**
The open questions the signals did not answer. Name them specifically. Identify
why each gap matters for the decision. "Further research needed" is not a
finding.

**Recommendation**
State one of: proceed / pause / pivot / abandon

Follow with two to three sentences of reasoning grounded in "What the signals
say together." The recommendation must follow from Part 1's signals -- not from
signals outside the verdict inventory, and not from reasoning not anchored in
named evidence.

---

## Output

Produce the full artifact in this order:

1. S2 -- EVALUATOR verdicts (all signals, complete)
2. S4b Part 1 -- Verdict inventory (YES/PARTIAL only, labeled)
3. S4b Part 2 -- Characterization (the topic story)

File naming: {topic}-story-{YYYY-MM-DD}.md
Storage: simulations/topic/story/
```

---

## V-02 — Single-axis: Output format (schema-constrained 3-column table for compliance declaration)

**Axis**: Output format — compliance architecture declared as a 3-column table with a dedicated "Governing Criterion" column  
**Hypothesis**: C-54 passes — the "Governing Criterion" column is a mandatory schema component; a row without a criterion number is structurally apparent (empty column cell vs. prose that may omit criterion numbers without visual signal). C-51, C-52, C-53 carry over from V-01. C-55 still fails — the table (layer declaration) and the role-sequence instruction (workflow sequence) remain separate structures.

---

```markdown
# /signal:topic:story

You are producing a **topic story** — an editorial synthesis that interprets
what the signals gathered for a feature topic say together. This is not a signal
summary. It is a narrative judgment: what the signals mean, how they converge or
diverge, and what a decision-maker should do with them. Write in the author's
voice. Do not report; interpret.

---

## Compliance Architecture

The authoring workflow enforces the S2 -> S4b production chain through three
layers. Each layer is declared below with its governing criterion. A row with no
criterion number in column 3 is an incomplete declaration -- the table schema
requires a criterion reference for every layer.

| Layer | Mechanism | Governing Criterion |
|-------|-----------|---------------------|
| Layer 1 | S4b structural partition: Part 1 (verdict inventory) feeds Part 2 (characterization). Part 2 is explicitly constrained to draw only from Part 1's named inventory -- no signals may enter Part 2 that do not appear in Part 1. | C-51 |
| Layer 2 | Evaluator-first production order: EVALUATOR role completes S2 verdicts as named outputs before AUTHOR role begins S4b. S4b is a designated successor activity and may not begin until EVALUATOR outputs exist as complete labeled artifacts. | C-52 |
| Layer 3 | Phase prerequisite gate: an explicit gate between EVALUATOR and AUTHOR phases enforces the Layer 2 production order. The gate is not advisory -- S4b Part 1 entry is blocked until S2 verdicts are complete. | C-52 |

Inter-layer ordering:
- Layer 2 governs WHEN S4b may begin (evaluator phase must complete first)
- Layer 1 governs WHAT S4b may contain once begun (Part 2 constrained to Part 1)
- Layer 3 reinforces Layer 2 through the explicit phase gate

---

## Inputs

You will receive signal artifacts for a topic. Each was produced by a Signal
skill across one or more namespaces: scout, draft, review, flow, trace, prove,
listen, program, topic. Read all artifacts before beginning the EVALUATOR phase.

---

## EVALUATOR Role

**Phase entry condition**: You are in the EVALUATOR phase. S4b authoring (AUTHOR
role) may not begin until this phase is complete. The Layer 2 production order
applies -- the phase gate below is not advisory.

For each signal artifact, produce a labeled verdict entry:

```
Signal: {namespace}/{skill} -- {filename}
Verdict: YES | PARTIAL | NO
Key finding: {one sentence, YES or PARTIAL only; omit line for NO}
```

Verdict definitions:
- YES     -- Clear, usable finding contributing to the feature story
- PARTIAL -- Contributes a finding with significant gaps, hedging, or limited
             scope
- NO      -- No usable finding

Complete all verdicts before proceeding. Every artifact must have a verdict.

---
[ EVALUATOR PHASE GATE (Layer 3 / Layer 2) -- S2 verdicts complete.
  AUTHOR phase begins below. ]
---

## AUTHOR Role

S4b authoring begins here. S2 verdicts exist as complete named outputs above
(Layer 2 satisfied). Part 2 draws only from Part 1 (Layer 1 applies).

### S4b -- Part 1: Verdict Inventory
*(Layer 1 [C-51]: enumerates only YES/PARTIAL signals; constrains Part 2)*

List only the YES and PARTIAL signals from the EVALUATOR phase. Include the
verdict label for each entry. Do not introduce signals with NO verdicts or
signals not evaluated above.

  - {namespace}/{skill}: {key finding} (S2 verdict: YES)
  - {namespace}/{skill}: {key finding} (S2 verdict: PARTIAL)

---
[ S4b PART 1 COMPLETE -- Part 2 input constrained to the entries above.
  (Layer 1 [C-51] -- Part 2 draws exclusively from Part 1.) ]
---

### S4b -- Part 2: Characterization
*(Layer 1 [C-51]: draws exclusively from Part 1 -- not from an independent
review of all signals)*

**What we set out to understand**
The central question or uncertainty this signal-gathering effort was meant to
resolve. One to two sentences. Frame what was unknown, not what was done.

**What each signal revealed**
One sentence per YES/PARTIAL signal from Part 1. State the key finding directly.
Do not summarize signal content; report the finding.

**What the signals say together**
The pattern. What interpretation emerges when these signals are read as a set?
Name the convergence or divergence directly. This is editorial judgment -- the
author's synthesis of the weight of evidence. Do not hedge. State what the
evidence says.

**What remains uncertain**
Open questions the signals did not answer. Named specifically. State why each
gap matters for the decision. "Further research needed" is not a finding.

**Recommendation**
State one of: proceed / pause / pivot / abandon

Two to three sentences of reasoning grounded in Part 1. The recommendation must
follow from "What the signals say together" -- not from signals outside the
verdict inventory and not from reasoning not anchored in named evidence.

---

## Output

Produce the full artifact in this order:

1. S2 -- EVALUATOR verdicts (all signals, labeled)
2. S4b Part 1 -- Verdict inventory (YES/PARTIAL only, with verdict labels)
3. S4b Part 2 -- Characterization (the topic story)

File naming: {topic}-story-{YYYY-MM-DD}.md
Storage: simulations/topic/story/
```

---

## V-03 — Single-axis: Lifecycle emphasis (annotated phase diagram as criterion-coupled artifact)

**Axis**: Lifecycle emphasis — a single annotated phase diagram co-locates the workflow sequence (C-52) and the layer declaration (C-53) in one structure  
**Hypothesis**: C-55 passes — the diagram's phase arrows satisfy C-52 (evaluator-first production order) and the diagram's legend satisfies C-53 (named layers, criterion references, inter-layer ordering) through the same artifact; workflow sequence and layer declaration cannot diverge. C-54 tested — legend annotations use structured label slots that may or may not constitute a schema-constrained format; evaluators should check whether the criterion-reference fields are schema-enforced or merely author-disciplined.

---

```markdown
# /signal:topic:story

You are producing a **topic story** -- an editorial synthesis that interprets
what the signals gathered for a feature topic say together. This is not a signal
summary. It is a narrative judgment: what the signals mean, how they converge or
diverge, and what a decision-maker should do with them. Write in the author's
voice. Do not report; interpret.

---

## Authoring Workflow and Compliance Architecture

The diagram below is the authoritative declaration of this workflow's production
sequence and enforcement layer architecture. It simultaneously specifies:
  (a) the evaluator-first production sequence [C-52] -- read the phase arrows
  (b) the compliance layer declaration [C-53] -- read the legend

Both requirements are properties of the same artifact. An evolution to the
workflow sequence necessarily modifies the layer declaration. Divergence between
the production order and the layer declaration is architecturally impossible.

```
+---------------------------------------------------------------------+
|              TOPIC STORY PRODUCTION WORKFLOW                        |
|                                                                     |
|  +--------------------+   S2 verdicts    +----------------------+  |
|  |  EVALUATOR PHASE   |  (named outputs) |    AUTHOR PHASE      |  |
|  |                    | ---------------> |                      |  |
|  |  For each signal:  |  prerequisite    |  S4b Part 1:         |  |
|  |  - Assign verdict  |  satisfied       |  Verdict inventory   |  |
|  |    YES/PARTIAL/NO  |                  |  (YES/PARTIAL only)  |  |
|  |  - Name key        |                  |          |           |  |
|  |    finding for     |                  |          | only      |  |
|  |    YES/PARTIAL     |                  |          v           |  |
|  |                    |                  |  S4b Part 2:         |  |
|  |  Output: complete  |                  |  Characterization    |  |
|  |  labeled verdict   |                  |  (draws from Part 1  |  |
|  |  set               |                  |   exclusively)       |  |
|  +--------------------+                  +----------------------+  |
+---------------------------------------------------------------------+

LEGEND -- Compliance Layers:

  [C-52] Layer 2: Evaluator-first production order
    Phase arrow (-->) enforces that S2 verdicts are named artifacts before
    AUTHOR phase begins. S4b authoring is the designated successor activity.
    Governs WHEN S4b authoring may begin.

  [C-51] Layer 1: S4b structural partition
    Part 1 enumerates only YES/PARTIAL verdicts from EVALUATOR phase.
    Part 2 input arrow (|only v) constrains characterization to Part 1 outputs.
    Governs WHAT S4b may contain once authoring begins.

  [C-52] Layer 3: Predecessor requirement (secondary enforcement path)
    AUTHOR phase entry requires S2 verdicts as complete labeled artifacts.
    Reinforces Layer 2 through an explicit phase entry prerequisite.

  Inter-layer ordering: Layer 2 and Layer 3 govern sequence entry.
  Layer 1 governs content once entry is permitted.
```

---

## Inputs

You will receive signal artifacts for a topic. Each was produced by a Signal
skill across one or more namespaces: scout, draft, review, flow, trace, prove,
listen, program, topic. Read all artifacts before beginning the EVALUATOR phase.

---

## EVALUATOR Phase
*(Diagram: left box -- produces S2 verdicts as named outputs)*

**Phase entry condition**: You are in the EVALUATOR phase. The phase arrow has
not yet been traversed. AUTHOR phase (S4b) may not begin until this phase is
complete (Layer 2 [C-52], Layer 3 [C-52]).

For each signal artifact, produce:

```
Signal: {namespace}/{skill} -- {filename}
Verdict: YES | PARTIAL | NO
Key finding: {one sentence, YES or PARTIAL only; omit line for NO}
```

Verdicts:
  YES     -- Clear, usable finding contributing to the feature story
  PARTIAL -- Contributes a finding with gaps, hedging, or limited scope
  NO      -- No usable finding

Complete all verdicts before proceeding. Every artifact must have a verdict.

---
[ EVALUATOR PHASE COMPLETE -- Phase arrow traversed. S2 verdicts exist as
  named artifacts. AUTHOR phase begins below. (Layers 2+3 [C-52] satisfied) ]
---

## AUTHOR Phase
*(Diagram: right box -- S4b Part 1 then Part 2)*

S4b authoring begins here. The diagram's phase arrow has been traversed.

### S4b -- Part 1: Verdict Inventory
*(Diagram: "YES/PARTIAL only" -- Layer 1 [C-51] input constraint)*

List only YES and PARTIAL signals from the EVALUATOR phase. Include the verdict
label for each entry. Do not introduce signals with NO verdicts or signals not
in the EVALUATOR output above.

  - {namespace}/{skill}: {key finding} (S2 verdict: YES)
  - {namespace}/{skill}: {key finding} (S2 verdict: PARTIAL)

---
[ S4b PART 1 COMPLETE -- Diagram's "| only v" arrow applies.
  Part 2 input constrained to Part 1 entries. (Layer 1 [C-51]) ]
---

### S4b -- Part 2: Characterization
*(Diagram: "draws from Part 1 exclusively" -- Layer 1 [C-51] scope restriction)*

**Scope restriction**: This section draws directly from Part 1 -- not from an
independent review of all signals.

**What we set out to understand**
The central question or uncertainty this signal-gathering effort was meant to
resolve. One to two sentences. Frame what was unknown, not what was done.

**What each signal revealed**
One sentence per YES/PARTIAL signal from Part 1. Key finding stated directly.

**What the signals say together**
The pattern. Name the convergence or divergence directly. Editorial judgment --
the author's synthesis. Do not hedge. State what the weight of evidence says.

**What remains uncertain**
Open questions the signals did not answer. Named specifically with decision
relevance stated.

**Recommendation**
proceed / pause / pivot / abandon

Two to three sentences of reasoning grounded in Part 1. Recommendation follows
from "What the signals say together" -- not from signals outside the inventory.

---

## Output

1. S2 -- EVALUATOR verdicts (all signals, complete)
2. S4b Part 1 -- Verdict inventory (YES/PARTIAL only, labeled)
3. S4b Part 2 -- Characterization (the topic story)

File naming: {topic}-story-{YYYY-MM-DD}.md
Storage: simulations/topic/story/
```

---

## V-04 — Combination: Role sequence + Lifecycle emphasis + Schema-constrained table

**Axes combined**: Explicit EVALUATOR/AUTHOR role labels (V-01) + annotated phase diagram as criterion-coupled artifact (V-03) + 3-column schema-constrained table for compliance declaration (V-02)  
**Hypothesis**: C-51 (partition), C-52 (role labels + diagram arrows), C-53 (diagram legend declaration), C-54 (table schema enforces criterion citation in the supplementary layer table), C-55 (diagram couples C-52 + C-53). Passes all five. The diagram handles C-55 while the table handles C-54 — both structures coexist, with the diagram as the primary criterion-coupled artifact and the table as a cross-reference layer index.

---

```markdown
# /signal:topic:story

You are producing a **topic story** -- an editorial synthesis that interprets
what the signals gathered for a feature topic say together. This is not a signal
summary. It is a narrative judgment: what the signals mean, how they converge or
diverge, and what a decision-maker should do with them. Write in the author's
voice. Do not report; interpret.

---

## Authoring Workflow and Compliance Architecture

### Primary Declaration: Criterion-Coupled Phase Diagram

The diagram below simultaneously specifies the production sequence [C-52] and
the enforcement layer architecture [C-53]. Both are properties of the same
artifact: the phase arrows define the evaluator-first order; the legend names
the layers with criterion annotations and inter-layer ordering statements. The
two requirements cannot diverge.

```
+---------------------------------------------------------------------+
|              TOPIC STORY PRODUCTION WORKFLOW                        |
|                                                                     |
|  +--------------------+   S2 verdicts    +----------------------+  |
|  |  EVALUATOR PHASE   |  (named outputs) |    AUTHOR PHASE      |  |
|  |  [C-52 Layer 2]    | ---------------> |                      |  |
|  |                    |  predecessor     |  S4b Part 1:         |  |
|  |  Evaluate signals  |  satisfied       |  Verdict inventory   |  |
|  |  YES / PARTIAL / NO|  [C-52 Layer 3]  |  (YES/PARTIAL only)  |  |
|  |  Name key finding  |                  |  [C-51 Layer 1 in]   |  |
|  |  per YES/PARTIAL   |                  |          |           |  |
|  |                    |                  |  only    |           |  |
|  |                    |                  |          v           |  |
|  |                    |                  |  S4b Part 2:         |  |
|  |                    |                  |  Characterization    |  |
|  |                    |                  |  [C-51 Layer 1 out]  |  |
|  +--------------------+                  +----------------------+  |
+---------------------------------------------------------------------+

LEGEND:
  [C-52] Layer 2 -- Evaluator-first production order
    Phase arrow: S2 verdicts are named outputs before AUTHOR phase begins.
    S4b is the designated successor activity.
    Governs WHEN S4b may begin.

  [C-51] Layer 1 -- S4b structural partition
    Part 1 input: YES/PARTIAL verdicts from EVALUATOR phase only.
    Part 2 constrained to Part 1 outputs ("|only v" arrow).
    Governs WHAT S4b may contain once begun.

  [C-52] Layer 3 -- Phase prerequisite (secondary enforcement)
    AUTHOR phase entry blocked until S2 verdicts are complete labeled artifacts.
    Reinforces Layer 2. Governs sequence entry alongside Layer 2.
```

### Supplementary Declaration: Schema-Constrained Layer Index

The table below cross-references each compliance layer with its governing
criterion. The "Governing Criterion" column is a mandatory schema component --
a row without a criterion number is structurally incomplete.

| Layer | Mechanism | Governing Criterion |
|-------|-----------|---------------------|
| Layer 1 | S4b structural partition: Part 1 (verdict inventory) constrains Part 2 (characterization). Part 2 may only draw from Part 1's named signal inventory. | C-51 |
| Layer 2 | Evaluator-first production order: EVALUATOR role produces S2 verdicts as named outputs before AUTHOR role begins S4b. | C-52 |
| Layer 3 | Phase prerequisite gate: explicit entry condition on AUTHOR phase requires S2 verdicts as complete labeled artifacts. Reinforces Layer 2. | C-52 |

Inter-layer ordering (declared in both diagram legend and table):
  Layer 2 and Layer 3: govern WHEN S4b authoring may begin
  Layer 1: governs WHAT S4b may contain once authoring begins

---

## Inputs

You will receive signal artifacts for a topic. Each was produced by a Signal
skill across one or more namespaces: scout, draft, review, flow, trace, prove,
listen, program, topic. Read all artifacts before beginning the EVALUATOR phase.

---

## EVALUATOR Phase
*(Diagram: left box [C-52 Layer 2 + Layer 3])*

**Phase entry condition**: You are in the EVALUATOR phase. The diagram's phase
arrow has not been traversed. AUTHOR phase and S4b Part 1 are gated until this
phase is complete.

For each signal artifact, produce a labeled verdict entry:

```
Signal: {namespace}/{skill} -- {filename}
Verdict: YES | PARTIAL | NO
Key finding: {one sentence, YES or PARTIAL only; omit line for NO}
```

Verdicts:
  YES     -- Clear, usable finding contributing to the feature story
  PARTIAL -- Contributes a finding with gaps, hedging, or limited scope
  NO      -- No usable finding

Complete every artifact. Do not proceed until all verdicts are labeled.

---
[ EVALUATOR PHASE COMPLETE -- Phase arrow traversed (diagram).
  S2 verdicts exist as named artifacts. Layers 2+3 [C-52] satisfied.
  AUTHOR phase begins. ]
---

## AUTHOR Phase
*(Diagram: right box -- S4b Part 1 then Part 2)*

S4b authoring begins here. S2 verdicts exist as complete named outputs above.

### S4b -- Part 1: Verdict Inventory
*(Layer 1 [C-51] -- receives EVALUATOR outputs; constrains Part 2)*

List only YES and PARTIAL signals from the EVALUATOR phase above. Include the
verdict label per entry. No signals outside YES/PARTIAL may appear here.

  - {namespace}/{skill}: {key finding} (S2 verdict: YES)
  - {namespace}/{skill}: {key finding} (S2 verdict: PARTIAL)

---
[ S4b PART 1 COMPLETE -- Layer 1 [C-51] input constraint logged.
  Part 2 draws exclusively from the entries above. ]
---

### S4b -- Part 2: Characterization
*(Layer 1 [C-51] -- scope restricted to Part 1. Not an independent review.)*

**Scope restriction**: This section draws directly from Part 1 -- not from an
independent review of all signals.

**What we set out to understand**
The central question or uncertainty this signal-gathering effort was meant to
resolve. One to two sentences. Frame what was unknown, not what was done.

**What each signal revealed**
One sentence per Part 1 signal. Key finding stated directly. Do not summarize
signal content; report the finding as a fact.

**What the signals say together**
The pattern. What interpretation emerges when the Part 1 signals are read as a
set? Name the convergence or divergence directly. This is editorial judgment.
Do not hedge. State what the weight of evidence says.

**What remains uncertain**
Open questions the signals did not answer. Named specifically. State why each
gap matters for the decision.

**Recommendation**
proceed / pause / pivot / abandon

Two to three sentences grounded in "What the signals say together." The
recommendation must follow from Part 1's evidence set -- not from signals
outside the inventory and not from reasoning not anchored in named findings.

---

## Output

1. S2 -- EVALUATOR verdicts (all signals, complete)
2. S4b Part 1 -- Verdict inventory (YES/PARTIAL only, labeled)
3. S4b Part 2 -- Characterization (the topic story)

File naming: {topic}-story-{YYYY-MM-DD}.md
Storage: simulations/topic/story/
```

---

## V-05 — Combination: All mechanisms + Conversational register + Inertia framing

**Axes combined**: All C-51–C-55 mechanisms (V-04 base) + conversational/imperative phrasing register + inertia framing (status-quo competitor named and positioned throughout — what would we build, ship, or decide if these signals didn't exist?)  
**Hypothesis**: Conversational register reduces friction without sacrificing any compliance mechanism. Inertia framing sharpens the recommendation section by forcing the author to name what the signals changed vs. the default assumption — a common failure mode is a recommendation that would have been the same without the signals. All five criteria pass.

---

```markdown
# /signal:topic:story

Write a **topic story** -- the synthesis that says what you actually learned and
what you should do with it. Not a recap. Not a summary of each signal. An
editorial call: what do all these signals say together, and does that change
what you would have done by default?

The inertia competitor is always present: the team had a prior assumption
before gathering signals. If the topic story doesn't name what changed vs. that
assumption, it hasn't done its job. Keep that in mind throughout.

---

## How This Works

Here is the production chain -- read this before you start:

```
+---------------------------------------------------------------------+
|              TOPIC STORY PRODUCTION WORKFLOW                        |
|                                                                     |
|  +--------------------+   S2 verdicts    +----------------------+  |
|  | YOU: EVALUATOR     |  (named outputs) |  YOU: AUTHOR         |  |
|  | [C-52 Layer 2]     | ---------------> |                      |  |
|  |                    |  don't skip this |  S4b Part 1:         |  |
|  | Read every signal. |  [C-52 Layer 3]  |  Verdict inventory   |  |
|  | Assign YES/PARTIAL |                  |  (YES/PARTIAL only)  |  |
|  | /NO. Name the      |                  |  [C-51 Layer 1 in]   |  |
|  | finding.           |                  |          |           |  |
|  |                    |                  |  only    |           |  |
|  |                    |                  |          v           |  |
|  |                    |                  |  S4b Part 2:         |  |
|  |                    |                  |  The story           |  |
|  |                    |                  |  [C-51 Layer 1 out]  |  |
|  +--------------------+                  +----------------------+  |
+---------------------------------------------------------------------+

Legend:
  [C-52] Layer 2 -- Evaluator-first: verdicts exist as artifacts before
    authoring begins. Governs WHEN you may start Part 2.
  [C-51] Layer 1 -- S4b partition: Part 1 constrains Part 2. You write
    characterization only from what you named in Part 1. Governs WHAT Part 2
    may contain.
  [C-52] Layer 3 -- Gate: the evaluator phase must be complete before you
    open Part 1. Reinforces Layer 2.
```

Cross-reference table (criterion-indexed, for audit):

| Layer | What It Does | Governing Criterion |
|-------|--------------|---------------------|
| Layer 1 | S4b structural partition -- Part 1 feeds Part 2; Part 2 draws from Part 1 only | C-51 |
| Layer 2 | Evaluator-first production order -- verdicts are named artifacts before authoring begins | C-52 |
| Layer 3 | Phase prerequisite gate -- AUTHOR entry blocked until EVALUATOR outputs are complete | C-52 |

Inter-layer ordering: Layers 2 and 3 control when authoring begins. Layer 1
controls what authoring may use.

---

## What You'll Receive

Signal artifacts for a topic -- produced by skills across one or more namespaces
(scout, draft, review, flow, trace, prove, listen, program, topic). Read all of
them before starting.

---

## Step 1: EVALUATOR
*(Don't start Step 2 until this is done -- Layer 2 [C-52])*

Go through every signal. For each one, decide: does this give you something
usable for the story?

```
Signal: {namespace}/{skill} -- {filename}
Verdict: YES | PARTIAL | NO
Key finding: {one sentence -- what did this signal actually tell you?}
             (YES and PARTIAL only; skip this line for NO)
```

- YES means the signal gives you a clear finding you can use
- PARTIAL means it gives you something but with real gaps or hedging
- NO means nothing usable

Don't move on until every signal has a verdict.

---
[ STEP 1 COMPLETE -- verdicts exist as labeled artifacts. Step 2 opens. ]
---

## Step 2: AUTHOR
*(Part 2 draws from Part 1 only -- Layer 1 [C-51])*

### Part 1 -- What you're working with

List the YES and PARTIAL signals only. Include the verdict label. This list is
your exclusive input for Part 2 -- you don't get to reach back to NO signals
or add new ones.

  - {namespace}/{skill}: {key finding} (S2 verdict: YES)
  - {namespace}/{skill}: {key finding} (S2 verdict: PARTIAL)

---
[ PART 1 COMPLETE -- Part 2 draws from these entries only. ]
---

### Part 2 -- The story
*(From Part 1 only -- not from re-reading all signals. [C-51])*

**What we set out to understand**
One to two sentences on the question that motivated this signal-gathering. What
was the team uncertain about before these signals existed? Frame the unknown,
not the activity.

**What each signal revealed**
One sentence per Part 1 signal. State the finding as a fact. Don't summarize
the artifact -- give the finding.

**What the signals say together**
This is the editorial call. What pattern emerges across the Part 1 signals?
Name it directly. Convergence? Divergence? A surprising gap between what was
assumed and what was found? Don't average the signals; read them as a set and
say what they say. If the signals confirm the prior assumption, say so and say
why. If they challenge it, say where.

**What the signals changed** *(inertia check)*
Before gathering these signals, the team had a working assumption -- an inertia
position about whether and how to proceed. State that assumption explicitly.
Then state what, if anything, the signals changed about it. If the signals
confirmed the assumption entirely, say so. If they shifted it, name the shift.
A topic story that would recommend the same thing without the signals hasn't
earned its recommendation.

**What remains uncertain**
What did the signals not answer? Name the specific open questions, not a generic
hedge. State why each gap matters for the decision.

**Recommendation**
proceed / pause / pivot / abandon

Two to three sentences. Ground the recommendation in "What the signals say
together" and "What the signals changed." It should be legible why this is the
recommendation given the evidence, and legible what the default would have been
without it.

---

## Output

Write the full artifact in order:

1. Step 1 -- EVALUATOR verdicts (every signal, labeled)
2. Part 1 -- Verdict inventory (YES/PARTIAL only, with verdict labels)
3. Part 2 -- The topic story (full synthesis)

File naming: {topic}-story-{YYYY-MM-DD}.md
Storage: simulations/topic/story/
```

---

## Variation Summary

| Variation | Single Axis / Combination | Key Structural Bets | Expected C-51 | Expected C-52 | Expected C-53 | Expected C-54 | Expected C-55 |
|-----------|--------------------------|---------------------|:---:|:---:|:---:|:---:|:---:|
| V-01 | Role sequence | Prose compliance declaration; explicit EVALUATOR/AUTHOR labels | PASS | PASS | PASS | PARTIAL | FAIL |
| V-02 | Output format | 3-column table with "Governing Criterion" column | PASS | PASS | PASS | PASS | FAIL |
| V-03 | Lifecycle emphasis | Annotated phase diagram couples C-52+C-53 in one artifact | PASS | PASS | PASS | PARTIAL | PASS |
| V-04 | Role + Lifecycle + Format | Diagram (C-55) + table (C-54) coexist as primary and cross-reference | PASS | PASS | PASS | PASS | PASS |
| V-05 | All + Register + Inertia | V-04 base + conversational register + inertia framing in recommendation | PASS | PASS | PASS | PASS | PASS |

**C-54 in V-03**: The legend annotations use structured label slots but the format is ASCII art, not a true column schema — evaluators should check whether the `[C-xx]` bracket notation constitutes a schema-enforced citation field or author-disciplined placement.

**C-55 in V-04**: The diagram handles C-55; the table is a supplementary cross-reference. Both exist independently, which means an evaluator must confirm that the diagram alone satisfies both C-52 and C-53 pass conditions — the table does not undermine C-55 but also doesn't contribute to it.
