# Quest Variate — `topic-story` Round 12 (Rubric v11)

---

## V-01 — Axis: Role Sequence
**Hypothesis:** Making the EXTRACTOR → ANALYST → AUTHOR tri-role gate explicit and one-directional, with named completion checks, enforces pre-composition more reliably than structural separators alone and directly satisfies C-24/C-26.

---

```
You are running the `topic-story` skill.

Synthesize all available signals for the topic into a coherent editorial narrative.
NOT a summary of each signal — an authored interpretation of what the signals say together.

You will execute in three named roles in strict sequence.
A role may not begin until the prior role is marked COMPLETE.
Completing a role after beats have begun is a visible protocol violation.

---

## ROLE 1: EXTRACTOR [must complete before ANALYST begins]

Read each signal artifact. For each, produce a one-line digest:

  [artifact-name] → [key finding in one sentence]

List every artifact. Group by namespace (scout / draft / review / flow / trace / prove / listen / program / topic).

When all artifacts are listed, write:

  EXTRACTOR: COMPLETE — [N] artifacts across [K] namespaces

Do not analyze. Do not synthesize. Do not name patterns. Record only.

---

## ROLE 2: ANALYST [begins only after EXTRACTOR: COMPLETE]

Using EXTRACTOR output only (not raw artifacts), produce four analytic blocks.
Each block is a named, discrete output. Each must be self-contained.
Producing a block in a later stage does not satisfy its requirement here.

### BLOCK A — FALSIFIABLE HYPOTHESIS (Inertia Baseline)

State the starting hypothesis as a falsifiable claim — the proposition the team held
before signals were gathered. Format:

  HYPOTHESIS: [We believed / Our hypothesis: specific falsifiable claim]
  INERTIA VERB: [PROCEED | PAUSE | PIVOT | ABANDON]

The INERTIA VERB is the verdict implied by the prior belief, not by the signals.
This is S0 — the state before evidence.

### BLOCK B — PER-SIGNAL CONFIRMATION/CHALLENGE LEDGER

For each artifact from EXTRACTOR output, classify its relationship to the hypothesis:

  | Artifact | Namespace | Confirms | Challenges | Neutral | Key finding |
  |----------|-----------|----------|------------|---------|-------------|

Complete the ledger. Every artifact must appear. Do not aggregate or skip.

### BLOCK C — CROSS-SIGNAL PATTERN

State the pattern as a discrete, labeled, self-contained sentence:

  PATTERN: [A claim that references what two or more signals show together
            that no single signal shows alone. Name a relationship, tension,
            or gap — not a collection of findings.]

The pattern sentence must be readable without the surrounding narrative.
It must not forward-reference or backward-reference prose.

### BLOCK D — DELTA (S0 → S3)

State what changed from the inertia baseline:

  DELTA: We believed [HYPOTHESIS restated concisely].
         The signals [confirmed / challenged / partially refuted] this because [reason].
         Confidence [increased / decreased / inverted] because [named mechanism].

The delta must show substantive mutation. "The signals confirmed what we believed"
without naming how confidence changed fails. If S0 = S3, that is a pattern failure
and must be reported as such.

When all four blocks are written, write:

  ANALYST: COMPLETE — Pattern identified, delta computed, ledger closed

---

## ROLE 3: AUTHOR [begins only after ANALYST: COMPLETE]

Using ANALYST output only, write the five-beat narrative.
Producing an analytic claim inside a narrative beat does not satisfy its ANALYST block requirement.
Each block produced by ANALYST must also appear in its designated beat — prior-stage presence is not credit.

### BOTTOM LINE UP FRONT

Before Beat 1, state the verdict in one sentence:

  VERDICT: [PROCEED | PAUSE | PIVOT | ABANDON] — [one-sentence reason derived from PATTERN]

This sentence is the entry point. The narrative that follows explains it; it does not build to it.

### Beat 1 — What we set out to understand

Restate the falsifiable hypothesis from BLOCK A.
Name the inertia verb that represented the prior belief.
Do not soften into a vague intent statement.

### Beat 2 — What the signals revealed

Write one paragraph per signal namespace represented.
For each: name the key finding, state whether it confirmed or challenged the hypothesis
(drawn from the BLOCK B ledger), and name the artifact it comes from.
At least three namespaces must appear.

### Beat 3 — What the signals say together

Open with the PATTERN sentence from BLOCK C verbatim. Then expand in prose.
The expansion may add context, but the expansion cannot be the only place
the pattern appears. The BLOCK C sentence must open this beat.

### Beat 4 — What remains uncertain

Name at least one specific open question. For each uncertainty, state:

  If [X resolves to Y], this verdict moves from [current verb] to [shifted verb].

Generic hedges without a stated directional change fail.

### Beat 5 — The recommendation

State the final verdict verb. Then:

1. Cite PATTERN by reference: "Because [pattern restated], the recommendation is [verb]."
2. State the evidence posture: "The signal posture is [strong positive / mixed / conflicting / weak] — [verb] follows."
3. Compare to inertia: "The inertia baseline was [INERTIA VERB from BLOCK A]. The signals [moved / held / reversed] this to [final verb] because [DELTA summary from BLOCK D]."
4. Name the decision context: who is deciding and under what constraint.

If the final verb contradicts any intermediate verdict from prior beats,
name the override explicitly: "This departs from [prior verdict] because [reason]."

---

## TERMINAL CHECKLIST [must be completed before submission]

Mark each item. Unmarked items = submission gate not cleared.

- [ ] EXTRACTOR: COMPLETE written and artifact count stated
- [ ] ANALYST: COMPLETE written and all four blocks present
- [ ] BLOCK A: falsifiable hypothesis with INERTIA VERB
- [ ] BLOCK B: per-signal ledger with every artifact classified
- [ ] BLOCK C: self-contained pattern sentence
- [ ] BLOCK D: delta showing substantive mutation (S0 ≠ S3 or failure reported)
- [ ] VERDICT sentence present before Beat 1
- [ ] Beat 1 restates falsifiable hypothesis and inertia verb
- [ ] Beat 2 covers at least three namespaces with confirm/challenge labels
- [ ] Beat 3 opens with BLOCK C sentence verbatim
- [ ] Beat 4 names at least one uncertainty with a directional verb shift
- [ ] Beat 5 contains: pattern citation, evidence posture, inertia-to-final comparison, decision context
- [ ] No beat contains analytic work that belongs in ANALYST blocks
- [ ] Any contradiction between beats has an explicit named override

---

Topic: {{topic}}
Signal directory: simulations/{{topic}}/
```

---

## V-02 — Axis: Output Format
**Hypothesis:** Structuring synthesis as a table-led artifact (ledger → pattern table → beat prose) makes cross-signal claims directly verifiable, satisfies C-31's ledger requirement, and enables C-20 multi-stage consistency checks by placing critical claims in named table cells that can be compared across sections.

---

```
You are running the `topic-story` skill.

Synthesize all signals for topic {{topic}} into an editorial story.
NOT a per-signal summary — a structured synthesis where tables carry the analytic
weight and prose carries the interpretation.

Follow the output schema below exactly. Named tables are structural requirements.
A table that is absent or reformatted as prose fails its criterion.

---

## PART 1 — SIGNAL INVENTORY TABLE

List every signal artifact. One row per artifact.

| # | Artifact | Namespace | Key finding (one sentence) | Confirms H | Challenges H | Neutral |
|---|----------|-----------|---------------------------|------------|--------------|---------|

Columns:
- Namespace: scout / draft / review / flow / trace / prove / listen / program / topic
- Key finding: what this artifact's primary output was, in one sentence
- Confirms H / Challenges H / Neutral: mark exactly one with ✓

Do not write prose in this section. Complete the table. Every artifact gets a row.

After the table:

  INVENTORY CLOSED: [N] artifacts, [K] namespaces, [C] confirm, [X] challenge, [N0] neutral

---

## PART 2 — ANALYTIC TABLES

### Table 2-A: Hypothesis Register

| Field | Value |
|-------|-------|
| Initial hypothesis | [The falsifiable claim the team held before signals] |
| Inertia verb | [PROCEED / PAUSE / PIVOT / ABANDON] |
| Basis for inertia | [Why this verb before evidence] |
| Post-signal hypothesis | [How the hypothesis is now stated] |
| Final verdict verb | [PROCEED / PAUSE / PIVOT / ABANDON] |
| Delta summary | [What changed, in one sentence] |

The initial hypothesis must be falsifiable — a specific claim, not a vague intent.
The delta must show substantive mutation; if inertia verb = final verb, explain what changed in confidence or scope.

### Table 2-B: Pattern Synthesis

| Field | Value |
|-------|-------|
| Pattern claim | [Self-contained sentence: what 2+ signals show together that none shows alone] |
| Signals supporting pattern | [List artifact names] |
| Pattern type | [tension / gap / convergence / contradiction / amplification] |
| Pattern-to-verdict bridge | [Because PATTERN, the verdict is VERB] |

The pattern claim must be readable without surrounding prose.
The bridge sentence must name the pattern and name the verb.

### Table 2-C: Uncertainty Register

| Uncertainty | If resolves to | Verdict shifts to | Priority |
|-------------|---------------|-------------------|----------|
| [Specific open question] | [specific outcome] | [verb] | [high/med/low] |

At least one row required. Generic hedges ("more research needed") without a named directional shift fail.

---

## PART 3 — BOTTOM LINE UP FRONT

State before any narrative beat:

  VERDICT: [PROCEED / PAUSE / PIVOT / ABANDON]
  POSTURE: [strong positive / mixed / conflicting / weak]
  BECAUSE: [Pattern claim from Table 2-B, restated in one sentence]

---

## PART 4 — NARRATIVE BEATS

Write using Tables 2-A, 2-B, 2-C as source material.
Do not introduce analytic claims in beats that do not appear in Part 2 tables.
Each table value cited in a beat must match its table value exactly — inconsistency is a correctness error.

### Beat 1 — What we set out to understand

Restate the initial hypothesis from Table 2-A (field: Initial hypothesis).
Name the inertia verb. Explain briefly why the team held this belief.

### Beat 2 — What the signals revealed

For each namespace with at least one signal, write one paragraph:
- Name the namespace
- State the key finding
- State explicitly whether the signals from this namespace confirmed or challenged the hypothesis
  (drawn from Part 1, Confirms H / Challenges H columns)

Minimum three namespaces.

### Beat 3 — What the signals say together

Open with the exact pattern claim from Table 2-B (field: Pattern claim).
Expand in prose to explain the pattern's significance.
Close by naming the pattern type (Table 2-B, Pattern type field).

### Beat 4 — What remains uncertain

Convert each row of Table 2-C into prose. For each:
name the uncertainty, state what it would take to resolve it,
and name the verdict it would shift to.

### Beat 5 — The recommendation

1. State the final verdict verb (must match Table 2-A, Final verdict verb).
2. Write the bridge sentence (must match Table 2-B, Pattern-to-verdict bridge).
3. State the evidence posture (must match Part 3, POSTURE).
4. Write the inertia comparison:
   "The team entered with [inertia verb] (Table 2-A). The signals [moved / held] this to [final verb] because [delta summary from Table 2-A]."
5. Name the decision context: who is deciding, under what constraint.

---

## CONSISTENCY AUDIT

Before submission, verify:

| Check | Expected value | Actual value in Beat 5 | Match? |
|-------|---------------|----------------------|--------|
| Final verdict verb | [from Table 2-A] | | [ ] |
| Pattern-to-verdict bridge | [from Table 2-B] | | [ ] |
| Evidence posture | [from Part 3 POSTURE] | | [ ] |
| Delta summary matches | [from Table 2-A] | | [ ] |

All Match? columns must be [ ✓ ] before submission.

---

Topic: {{topic}}
Signal directory: simulations/{{topic}}/
```

---

## V-03 — Axis: Inertia Framing
**Hypothesis:** Foregrounding the initial hypothesis as an explicit VERDICT-class inertia verb — and computing the S0 → S3 trajectory as the structural spine of the story — produces a more defensible recommendation because the final verdict is measurable against a named starting state, not asserted from scratch.

---

```
You are running the `topic-story` skill.

This skill produces a signal story structured as an inertia trajectory:
the team held a verdict before signals were gathered (S0),
the signals moved, held, or reversed that verdict (S1–S2),
and the story culminates in the final adjudicated verdict (S3).

The recommendation is not a conclusion reached at the end.
It is a named starting state that the evidence either confirms or overturns.

---

## STEP 1 — ESTABLISH INERTIA (S0)

Before reading signals, state the prior verdict:

  S0 HYPOTHESIS: [Falsifiable claim the team held before evidence gathering]
  S0 VERDICT: [PROCEED | PAUSE | PIVOT | ABANDON]
  S0 BASIS: [One sentence: why this verb before signals]

The hypothesis must be falsifiable — specific enough that a signal could refute it.
A vague intent statement ("we set out to understand X") is not a hypothesis.
The S0 VERDICT is the inertia: what the team would have done if no signals were gathered.

---

## STEP 2 — READ SIGNALS AND BUILD LEDGER

Read all signal artifacts in simulations/{{topic}}/.

For each artifact, record:

  [artifact] | [namespace] | [key finding] | CONFIRMS S0 | CHALLENGES S0 | NEUTRAL

Label each entry with its inertia relationship. Do not skip artifacts.

When complete:
  LEDGER CLOSED: [N] artifacts. Confirms: [C]. Challenges: [X]. Neutral: [N0].
  PRELIMINARY POSTURE: [strong positive / mixed / conflicting / weak]

---

## STEP 3 — COMPUTE DELTA (S0 → S3)

Name what changed:

  DELTA:
  - We entered with: [S0 HYPOTHESIS restated]
  - The signals showed: [what the ledger pattern reveals]
  - Confidence [increased to / decreased from / inverted from]: [reason named]
  - The hypothesis [was confirmed / was partially refuted / was overturned] because: [named mechanism]
  - S3 VERDICT: [PROCEED | PAUSE | PIVOT | ABANDON]

If S0 VERDICT = S3 VERDICT, the delta must show *how* confidence or scope changed.
"The signals confirmed what we believed" without naming the mechanism fails.
S0 = S3 with no mechanism is a stagnation error — report it as such.

---

## STEP 4 — SYNTHESIZE PATTERN

State the cross-signal pattern as a discrete, labeled, self-contained block:

  PATTERN: [What two or more signals show together that no single signal shows alone.
            Name a relationship, tension, or gap — not a collection of findings.
            This sentence is readable without surrounding prose.]

Then write the bridge:

  BRIDGE: Because [PATTERN restated], the S3 VERDICT is [verb].

The BRIDGE sentence must appear in Step 4 and again verbatim in Beat 5.
Prior-stage presence does not satisfy Beat 5 requirement.

---

## STEP 5 — WRITE THE STORY

### VERDICT LINE [required before Beat 1]

  VERDICT: [S3 VERDICT verb] — [BRIDGE reason in one clause]

This is the first substantive output the reader encounters.
The story explains this verdict; it does not build to it.

### Beat 1 — What we set out to understand

Restate S0 HYPOTHESIS from Step 1 as the opening claim.
Name S0 VERDICT (the inertia verb). Explain briefly why the team held it.
The reader must understand what prior belief the signals were testing.

### Beat 2 — What the signals revealed

One paragraph per namespace with at least one artifact. Minimum three namespaces.
For each namespace: name the key finding, state whether it confirmed or challenged S0,
and cite the artifact by name.
Use the ledger from Step 2 as the source — do not introduce findings not in the ledger.

### Beat 3 — What the signals say together

Open Beat 3 with the PATTERN sentence from Step 4 verbatim.
Expand: explain what makes this pattern significant, why it is not visible in any single signal,
and what it means for the decision.
Close by naming whether the pattern was an expected finding or a surprise relative to S0.

### Beat 4 — What remains uncertain

Name at least one specific open question.
For each:

  UNCERTAINTY: [Specific question]
  IF RESOLVED TO: [specific outcome]
  VERDICT SHIFTS TO: [PROCEED / PAUSE / PIVOT / ABANDON]
  DIRECTION: [moves toward / away from S3 verdict]

Generic hedges without a named direction fail.

### Beat 5 — The recommendation

Structure this beat as a four-part adjudication:

1. **VERDICT STATEMENT**: State S3 VERDICT verb. This must match Step 3 S3 VERDICT exactly.

2. **BRIDGE** (from Step 4, copied verbatim):
   "Because [PATTERN], the recommendation is [S3 VERDICT]."
   This is required here in addition to Step 4. Step 4 presence is not credit.

3. **POSTURE CERTIFICATION**:
   "The signal posture is [strong positive / mixed / conflicting / weak], drawn from [N] artifacts across [K] namespaces. This posture produces the [verb] verdict."

4. **INERTIA-TO-FINAL COMPARISON** (C-32):
   "The team entered with [S0 VERDICT] based on [S0 HYPOTHESIS restated].
    The signals [confirmed / challenged / overturned] this.
    [DELTA summary from Step 3 restated in one sentence.]
    The verdict moves from [S0 VERDICT] to [S3 VERDICT]."
    If S0 = S3: "The verdict holds at [verb]; confidence [increased/decreased] because [mechanism]."

5. **DECISION CONTEXT**: Name who is making this decision and under what constraint.
   A recommendation stated as a finding ("signals suggest X") rather than a decision ("a team deciding Y should Z") fails.

---

## TERMINAL GATE

Before submitting, mark each:

- [ ] S0 HYPOTHESIS is falsifiable (specific claim, not vague intent)
- [ ] S0 VERDICT named
- [ ] Ledger closed with artifact count and posture
- [ ] DELTA shows mechanism, not just outcome
- [ ] PATTERN is self-contained and opens Beat 3
- [ ] BRIDGE appears in Step 4 and Beat 5 (two independent placements)
- [ ] VERDICT LINE appears before Beat 1
- [ ] Beat 2 covers 3+ namespaces with confirm/challenge labels from ledger
- [ ] Beat 4 has at least one uncertainty with named directional verb shift
- [ ] Beat 5 contains all four adjudication parts
- [ ] S3 VERDICT in Beat 5 matches Step 3 S3 VERDICT
- [ ] Inertia-to-final comparison explicitly names S0 verb, S3 verb, and mechanism

---

Topic: {{topic}}
Signal directory: simulations/{{topic}}/
```

---

## V-04 — Combined Axes: Role Sequence + Phrasing Register
**Hypothesis:** A conversational register inside a strict tri-role gate produces more authentic editorial synthesis than either pure formalism (which can produce mechanical output) or pure prose (which loses structural integrity). The roles enforce rigor; the register produces voice.

---

```
You are running the `topic-story` skill.

Your job is to tell the story of what the signals say together about {{topic}}.
Not a debrief. Not a summary. An editorial — your interpretation of the pattern
the evidence reveals, written for someone who has to make a decision.

Before you write, you do the analytic work. Separately. In order.

Here's how this works: three roles, executed in sequence.
Each role has one job. No role starts until the prior one is done.

---

## ROLE 1: READER

Your only job here: read the signals and record what you saw.

Go through every signal artifact in simulations/{{topic}}/.
For each one, write a one-liner:

  [artifact-name] → [what this signal actually showed, in plain English]

Group them by namespace (scout / draft / review / flow / trace / prove / listen / program / topic).
Don't editorialize. Don't connect dots yet. Just read and record.

When you've read everything, write:

  READER DONE — [N] signals read across [K] namespaces

Don't start the next role until you've written that line.

---

## ROLE 2: ANALYST

You've read the signals. Now figure out what they mean together.

Before you do that: what did the team believe before they gathered evidence?
State it as a falsifiable claim — specific enough to be wrong.

  PRIOR BELIEF: [We thought / Our assumption was: specific claim]
  PRIOR VERDICT: [PROCEED / PAUSE / PIVOT / ABANDON]
  (This is the inertia — what they would have done without running signals.)

Now go through your READER notes and build a ledger.
For each signal: does it confirm the prior belief, challenge it, or neither?

  | Signal | Namespace | Finding | Confirms prior | Challenges prior |
  |--------|-----------|---------|----------------|------------------|

Complete this table. Every signal gets a row.

Now: what's the pattern? What do two or more signals show together that you wouldn't
see from any single one? Write it as one standalone sentence:

  THE PATTERN: [Cross-signal claim. Readable on its own. Doesn't reference the prose around it.]

Now: what changed from the prior belief to what you found?

  WHAT CHANGED: We believed [prior belief restated briefly].
                The signals [confirmed / challenged / overturned] this because [mechanism].
                Confidence [went up / went down / flipped] because [specific reason].
                The signals point to: [PROCEED / PAUSE / PIVOT / ABANDON]

If the prior verdict and the signals point to the same verb — that's fine,
but you still need to name why confidence changed. "Confirmed" without a mechanism
is not a delta; it's a shrug.

Write this before moving on:

  ANALYST DONE — Pattern named, prior belief compared, verdict direction established

---

## ROLE 3: AUTHOR

Now you write the story. Use what the ANALYST produced — don't re-derive anything.
If a claim isn't in your analytic notes, it doesn't go in the story.

The story has five beats and one opening line.

### Opening line (before Beat 1)

One sentence. The verdict, plain:

  [PROCEED / PAUSE / PIVOT / ABANDON] — [the reason in a clause, drawn from the pattern]

The rest of the story explains this. It doesn't lead up to it.

### Beat 1 — What we set out to understand

Start here: what was the prior belief? What verdict did it imply?
Make it concrete. The reader should feel what was at stake before the signals ran.

### Beat 2 — What the signals revealed

Walk through the namespaces. One paragraph per namespace that produced something meaningful.
For each: name the finding, say whether it confirmed or pushed back on the prior belief
(pull from the ledger), and name where it came from.
Cover at least three namespaces.

### Beat 3 — What the signals say together

Open with the pattern sentence from your ANALYST notes — word for word.
Then explain it: why does this pattern matter, and why couldn't you see it from any
single signal? Does it align with what you expected or did it catch you off guard?

### Beat 4 — What's still uncertain

What questions remain open? For each one, tell the reader what's at stake:
"If we find out X, this moves from [verb] to [verb]."
Don't hedge generically. Name the question and name the directional shift.

### Beat 5 — The recommendation

This beat does four things:

1. States the verdict verb (must match the ANALYST's final direction)
2. Connects to the pattern: "Because [pattern], the recommendation is [verb]"
   — write this sentence out fully, even if the reader can already see it
3. Names the evidence posture: "The signals are [strong positive / mixed / conflicting / weak]
   — [verb] follows from that"
4. Shows where the verdict moved from: "Going in, the team held [prior verdict].
   The signals [confirmed it with stronger backing / partially shifted it / reversed it]
   because [mechanism from ANALYST's delta]. The recommendation lands at [final verb]."
5. Names who's making this call and what their constraint is

If anything in Beat 5 contradicts something said in an earlier beat, say so explicitly
and name why the final take overrides it.

---

## Before you submit

Run through this list. Mark each yes or no:

- [ ] READER DONE written with signal count
- [ ] ANALYST DONE written
- [ ] Prior belief is a specific falsifiable claim (not vague intent)
- [ ] Ledger covers every signal with confirm/challenge labels
- [ ] Pattern sentence is present and standalone
- [ ] Delta shows a mechanism, not just an outcome
- [ ] Opening verdict line precedes Beat 1
- [ ] Beat 2 covers 3+ namespaces
- [ ] Beat 3 opens with the exact pattern sentence from ANALYST
- [ ] Beat 4 names at least one uncertainty with a named directional shift
- [ ] Beat 5 has all four elements: bridge, posture, inertia comparison, decision context
- [ ] Verdict verb in Beat 5 matches ANALYST's final direction

If any item is no, fix it before submitting.

---

Topic: {{topic}}
Signal directory: simulations/{{topic}}/
```

---

## V-05 — Combined Axes: Inertia Framing + Output Format + Lifecycle Emphasis
**Hypothesis:** Unifying the S0→S3 inertia trajectory as the structural spine, enforcing it through table-based multi-stage consistency checks, and scaling lifecycle section length to evidence density (more space where evidence is richer) will produce the most rubric-complete output while remaining proportional to what the signals actually contain.

---

```
You are running the `topic-story` skill.

Produce a signal story for topic: {{topic}}

The story's structural spine is an inertia trajectory:
the team held a prior verdict (S0), the signals moved it (S1, S2), and the story
closes with an adjudicated final verdict (S3).

Output is organized in four parts. Parts 1 and 2 are analytic (pre-composition).
Parts 3 and 4 are narrative. Analytic parts must be completed before narrative parts begin.

---

## PART 1 — INVENTORY AND INERTIA REGISTER

### 1-A: Signal Inventory

Read all artifacts in simulations/{{topic}}/.

| # | Artifact | Namespace | Key finding (one sentence) | Inertia relation |
|---|----------|-----------|---------------------------|-----------------|
| | | scout/draft/review/flow/trace/prove/listen/program/topic | | CONFIRMS / CHALLENGES / NEUTRAL |

Complete every row. After the table:

  INVENTORY CLOSED: [N] artifacts | [K] namespaces | [C] confirm | [X] challenge | [N0] neutral

### 1-B: Inertia Register

| Field | Value |
|-------|-------|
| S0 Hypothesis | [Falsifiable prior claim — specific, not vague intent] |
| S0 Verdict | [PROCEED / PAUSE / PIVOT / ABANDON] |
| S0 Basis | [One sentence: why this verdict before evidence] |

This register is the reference baseline for the S0→S3 delta.
The S0 Verdict is what the team would have done without running signals.

---

## PART 2 — ANALYTIC SYNTHESIS

### 2-A: Pattern Block

  PATTERN: [Discrete, self-contained sentence. What two or more signals show together
            that no single signal shows alone. Name a relationship, tension, or gap.
            Readable without surrounding prose. No forward or backward references.]

  PATTERN TYPE: [tension / gap / convergence / contradiction / amplification]
  SUPPORTING SIGNALS: [List artifact names]

### 2-B: Delta Register (S0 → S3)

| Stage | Verdict | Evidence state | Mechanism |
|-------|---------|---------------|-----------|
| S0 | [from 1-B] | Prior belief only | [S0 Basis from 1-B] |
| S1 | [PROCEED/PAUSE/PIVOT/ABANDON] | After first namespace cluster | [What shifted and why] |
| S2 | [PROCEED/PAUSE/PIVOT/ABANDON] | After second namespace cluster | [What shifted and why] |
| S3 | [PROCEED/PAUSE/PIVOT/ABANDON] | Full signal integration | [Pattern mechanism] |

Rules:
- S1 and S2 represent intermediate evidence states — fill with the verdict that would have been
  reached if the signals were read in that order. They need not be distinct from S0 or S3.
- If S0 = S3, explain in the Mechanism column how confidence or scope changed.
  A stagnant delta (no mechanism named) fails.
- The S3 Verdict is the final adjudicated verdict. It must be consistent with Part 3 content.

### 2-C: Uncertainty Register

| Uncertainty | Resolves to (scenario) | Verdict shifts | Direction |
|-------------|----------------------|----------------|-----------|
| [Specific open question] | [specific outcome] | [verb] | toward / away from S3 |

Minimum one row. Generic hedges ("more research needed") without a named shift fail.

### 2-D: Pre-Submission Consistency Seed

Fill these four values now. They will be checked against Part 3 content.

| Seed | Value |
|------|-------|
| SEED-PATTERN | [Pattern sentence from 2-A verbatim] |
| SEED-S3 | [S3 Verdict from 2-B] |
| SEED-POSTURE | [strong positive / mixed / conflicting / weak, derived from inventory ratios] |
| SEED-BRIDGE | Because [SEED-PATTERN], the recommendation is [SEED-S3]. |

ANALYTIC PARTS COMPLETE. NARRATIVE PARTS MAY NOW BEGIN.

---

## PART 3 — VERDICT LINE AND NARRATIVE BEATS

### VERDICT LINE [required before Beat 1]

  VERDICT: [SEED-S3] — [SEED-BRIDGE reason in one clause]

### Beat 1 — What we set out to understand

*Lifecycle weight: concise. Establish inertia, no more.*

Restate S0 Hypothesis from 1-B as a falsifiable opening claim.
Name S0 Verdict. Explain briefly why the team held it.
One paragraph.

### Beat 2 — What the signals revealed

*Lifecycle weight: substantial. This is where evidence density lives.*

One paragraph per namespace with at least one artifact. Minimum three namespaces.
For each namespace:
- Name the key finding (from inventory)
- State whether signals from this namespace confirmed or challenged S0 (from inventory, Inertia relation column)
- Cite the artifact by name

Scale paragraph length to namespace evidence density:
a namespace with one weak signal gets a shorter paragraph than one with three strong signals.

### Beat 3 — What the signals say together

*Lifecycle weight: focused. The pattern must be stated first.*

Open with SEED-PATTERN verbatim. Do not paraphrase.
Expand: why is this pattern visible only in combination? What does it mean for the decision?
Was this pattern consistent with S0 or did it surprise?
Reference S1/S2 from the delta table to show how the pattern emerged across stages.

### Beat 4 — What remains uncertain

*Lifecycle weight: proportional to uncertainty count. No padding.*

Convert each row of the Uncertainty Register (2-C) into prose.
For each: name the uncertainty, state the resolution scenario, name the verdict shift,
and state the direction relative to S3.

### Beat 5 — The recommendation

*Lifecycle weight: deliberate. Four required elements, stated fully.*

**Element 1 — Verdict**
State SEED-S3 verdict. Must match 2-B S3 exactly.

**Element 2 — Bridge** (non-substitution: this is a new instance, not a reference to 2-D)
Write: "Because [SEED-PATTERN], the recommendation is [SEED-S3]."
This sentence is required here. Its presence in 2-D does not satisfy this requirement.

**Element 3 — Posture certification**
Write: "The signal posture is [SEED-POSTURE], drawn from [N] artifacts across [K] namespaces. This posture produces the [verb] verdict."
Must match SEED-POSTURE exactly.

**Element 4 — Inertia-to-final comparison** (C-32)
Write: "The team entered with [S0 Verdict] ([S0 Hypothesis restated in one clause]).
The signals moved this to [S3 Verdict] because [S3 Mechanism from 2-B].
[If S0 = S3: The verdict holds at [verb]; confidence [increased/decreased] because [S3 Mechanism].]"

**Element 5 — Decision context**
Name who makes this decision and under what constraint.
State as a decision, not a finding: "A [role] deciding [X] under [constraint] should [verb]."

---

## PART 4 — CONSISTENCY AUDIT AND TERMINAL GATE

### Consistency Audit Table

| Seed | Seed value | Beat 5 actual value | Match |
|------|-----------|-------------------|-------|
| SEED-PATTERN | [from 2-D] | [exact text in Beat 5 Element 2] | [ ] |
| SEED-S3 | [from 2-D] | [verdict in Beat 5 Element 1] | [ ] |
| SEED-POSTURE | [from 2-D] | [posture in Beat 5 Element 3] | [ ] |
| SEED-BRIDGE | [from 2-D] | [bridge sentence in Beat 5 Element 2] | [ ] |

All Match columns must be ✓ before submission.
A mismatch between a seed value and its Beat 5 placement is a correctness failure.

### Terminal Gate

- [ ] Inventory closed with counts
- [ ] 1-B S0 Hypothesis is falsifiable
- [ ] Delta table shows S0/S1/S2/S3 with mechanisms — no stagnant delta
- [ ] Pattern block (2-A) is self-contained and standalone
- [ ] 2-D seeds filled before narrative began
- [ ] VERDICT LINE precedes Beat 1
- [ ] Beat 2 covers 3+ namespaces with confirm/challenge labels from inventory
- [ ] Beat 3 opens with SEED-PATTERN verbatim
- [ ] Beat 4 names 1+ uncertainties with directional verb shifts
- [ ] Beat 5 contains all five elements
- [ ] Consistency audit table completed and all rows match
- [ ] Any contradiction between beats has a named override

---

Topic: {{topic}}
Signal directory: simulations/{{topic}}/
```

---

## Variation Summary

| Variation | Primary Axis | Secondary Axes | Key Mechanism | New v11 Coverage |
|-----------|-------------|----------------|---------------|-----------------|
| V-01 | Role sequence | — | Named one-way EXTRACTOR→ANALYST→AUTHOR gate with completion lines | C-24, C-26 (structural gate); C-31 (ledger in BLOCK B); C-30, C-32 (inertia verb + comparison in Beat 5) |
| V-02 | Output format | — | Table-led: all analytic claims live in named tables; prose references tables | C-31 (Table 2-B ledger); C-20 (consistency audit table); C-30, C-32 (Hypothesis Register table) |
| V-03 | Inertia framing | — | S0→S3 trajectory as structural spine; VERDICT-class inertia verb as opening baseline | C-30 (S0 VERDICT as inertia verb); C-31 (ledger Step 2); C-32 (Beat 5 Element 4 comparison) |
| V-04 | Role sequence + phrasing register | Conversational | Tri-role (READER/ANALYST/AUTHOR) in plain language; rigor without jargon | All three v11 criteria via ANALYST prior belief + ledger table + Beat 5 inertia comparison |
| V-05 | Inertia framing + output format + lifecycle emphasis | Lifecycle scaling | S0→S1→S2→S3 staged delta table; seed-based consistency audit; lifecycle weight annotations per beat | C-30 (staged delta with S0 verdict); C-31 (inventory table with inertia relation column); C-32 (Beat 5 Element 4 with explicit S0→S3 language) |
