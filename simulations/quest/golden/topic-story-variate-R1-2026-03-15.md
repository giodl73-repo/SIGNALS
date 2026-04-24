---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 1
rubric: v1
---

# Variations — topic-story (Round 1)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Rubric v1 design context**: 4 essentials (C-01 synthesis-not-summary,
C-02 five structural elements, C-03 explicit grounded recommendation,
C-04 cross-signal pattern), 3 recommended (C-05 signal coverage, C-06 specific
uncertainty, C-07 recommendation proportionality), 2 aspirational (C-08 narrative
arc, C-09 delta surfacing). The hardest essential is C-04. C-03 and C-07 split the
recommendation into existence vs proportionality. Round 1 axes target the primary
failure modes: summary drift (C-01/C-04) and recommendation without grounding
(C-03/C-07).

---

## V-01

**Variation axis**: Lifecycle emphasis — pre-write synthesis worksheet
**Hypothesis**: The root cause of C-04 failures is that the model begins composing
prose while still reading signals, blending extraction with synthesis in real time.
Requiring a written synthesis worksheet — produced before any narrative prose
begins — forces the cross-signal reasoning step to complete as a discrete
deliverable. A worksheet that must answer "what do two or more signals show
together that no single signal shows alone?" cannot be satisfied by sequential
summaries; satisfying it requires the model to have actually found the pattern.
The worksheet is not in the final artifact, but it is a prerequisite gate. This
tests whether making the cross-signal analysis a written intermediate output
(rather than an implicit internal step) changes what appears in Beat 3.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs in two stages. Stage 1 produces a synthesis worksheet. Stage 2
writes the story. Stage 2 may not begin until Stage 1 is complete and its
worksheet answers are satisfied.

---

### Stage 1 — Synthesis worksheet

**Gather.**
Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if it exists.

**Complete the worksheet.** Answer all four questions before writing the story.
Incomplete answers are not acceptable — if you cannot answer a question, read more
carefully.

```
Worksheet — {topic}

Q1. Original question: In one sentence, what was the team's original question or
    hypothesis? (From strategy.md, or inferred from the topic name if absent.)

Q2. Key findings: For each signal artifact, name the single most important
    finding — the one you would carry forward if you could only keep one.
    Format: {artifact-name}: {finding}

Q3. Cross-signal pattern: What do two or more signals show together that no
    single signal shows alone? Name the convergence, divergence, tension, or gap
    that is only visible when you look across the whole set. Reference at least
    two specific artifacts. If your answer could be derived from any single
    artifact alone, it is not a cross-signal pattern — find the real one.

Q4. Recommendation preview: Given the pattern in Q3, which direction does the
    evidence point — proceed, pause, pivot, or abandon? One sentence. You may
    change this in Stage 2 if the story reveals a better read, but state a
    provisional direction now.
```

Do not begin Stage 2 until the worksheet is complete. The Q3 answer is the load-
bearing piece — it becomes the center of Beat 3.

---

### Stage 2 — Write the story

Write to `simulations/{topic}/{topic}-story-{date}.md`.

The story has five beats. All must be present and distinguishable. The worksheet
answers are your raw material, not a script — use them to write, not to copy.

**Beat 1 — What we set out to understand**
The original question (Q1). One to three sentences. Specific: not "we wanted to
understand X" but what specifically about X was uncertain or at risk.

**Beat 2 — What each signal revealed**
Draw from Q2. One key finding per signal, two sentences maximum. The finding most
relevant to the original question, not a recap of the artifact. Edit ruthlessly —
secondary findings belong nowhere in this document.

**Beat 3 — What the signals say together**
This is the Q3 answer written as narrative. Name the pattern. The claim here must
pass the Q3 test: a reader who saw only one signal could not have arrived at this
conclusion. Reference at least two signals explicitly. Draw a conclusion about
their relationship.

**Beat 4 — What remains uncertain**
Specific open questions not closed by any signal. Scope each: what exactly is
unknown, and why does it matter for the decision? No generic disclaimers.

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
Connect explicitly to the Beat 3 pattern. The Q4 preview was provisional — if the
story has shifted your read, state the new direction and why the signals changed
it.

---

### Voice

Write as an author, not as a reporter. Take positions. The story should read as
a briefing a PM or architect would quote from — not as a status report.

---

### Output

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

Open with:
```
# {Topic} Story
*As of {date}. {N} signals synthesized.*
```

---

## V-02

**Variation axis**: Role sequence — anti-summary prohibition with precise contrast
**Hypothesis**: LLMs default to sequential summarization when asked to "synthesize"
a list of artifacts because "synthesize" is ambiguous — it is compatible with
"read and summarize each one." The prohibition needs to be specific enough to close
that escape route. Placing the prohibition first (primacy anchoring) AND providing
a precise contrast — synthesis answers "what do these say together?", summary
answers "what did each one say?" — creates a more effective barrier than a general
instruction to avoid enumeration. The prohibition appears before the task
description, before the structural instructions, before anything else. This tests
whether primacy + precision changes the C-01/C-04 failure rate.

---

**A synthesis answers: what do the signals say together that no single signal says
alone? A summary answers: what did each signal say?**

These are different tasks. This skill produces a synthesis. If your output
answers the second question sequentially across signals, you have produced a
summary — regardless of whether a recommendation appears at the end.

Hold that distinction. Now read the task.

---

You are running `/topic:story` for a topic. The topic name is provided.

**What you are producing**: a narrative synthesis — the current state of
understanding about a feature, told in the author's voice, ending with an explicit
recommendation. The reader can follow the reasoning from question to conclusion
without consulting the underlying signals.

---

### What to do

**Locate signals.**
Glob `simulations/**/{topic}-*`. Read every artifact.
Also read `simulations/{topic}/strategy.md` if present.

**Find the pattern before writing.**
After reading all signals, identify what two or more signals reveal in combination
that neither reveals alone. Name it privately before you open the output artifact.
This is the pattern. Beat 3 is this pattern, written as narrative.

**Write the story** with five elements — all five must be present:

1. **What we set out to understand** — the original question or hypothesis,
   one to three sentences. What specific uncertainty motivated signal gathering?

2. **What each signal revealed** — one key finding per signal, two sentences
   maximum. The finding most relevant to the original question. Not a recap of
   the artifact — the single piece of evidence you would carry forward.

3. **What the signals say together** — the pattern you identified above.
   Name the convergence, divergence, tension, or gap. Reference at least two
   signals. Draw a conclusion about their relationship.
   This section fails if it could have been written by reading one signal.

4. **What remains uncertain** — specific open questions, scoped. Name what
   exactly is unknown and why it matters for the recommendation.

5. **Recommendation** — one of: **proceed**, **pause**, **pivot**, **abandon**.
   Connected to a specific finding or pattern named in element 3. If you find
   yourself writing "proceed with caution" without saying what the caution is or
   what drove it, stop and rewrite.

---

### Output

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

Write in confident, active voice. Take positions. A reader who has not seen the
individual signals should be able to follow the full reasoning.

---

## V-03

**Variation axis**: Phrasing register — decision memo addressed to a stakeholder
**Hypothesis**: Framing the story as a memo addressed to a named decision-maker
(PM, architect, or team lead — provided by the user or inferred from the topic
context) activates executive communication patterns that naturally suppress
enumeration and sharpen recommendation language. A memo to a decision-maker opens
with what they need to decide, not with what each artifact said. The BLUF
(bottom line up front) structure imposes forward pressure: the recommendation
stakes are established first, then the evidence is presented as justification
rather than as a survey. This directly addresses C-03 (recommendation exists and
is grounded) and C-07 (proportionality) because the memo recipient's decision
context is always visible. The risk is that the BLUF structure produces a lead
recommendation that is then inconsistently supported — this variation tests
whether the structure helps or hurts C-04 when the model must build backward from
a stated conclusion.

---

You are writing a feature decision memo. The topic name is provided.

The memo goes to: the PM or team lead responsible for the feature decision. If a
specific name is available from strategy.md or the topic context, use it. If not,
address it to "Team."

This is not a story or a report. It is a memo a decision-maker reads when they
have three minutes and need to know: what did we learn, and what should we do?

---

**Gather inputs.**
Glob `simulations/**/{topic}-*`. Read every artifact.
Also read `simulations/{topic}/strategy.md` if present — note the original
question and any stated decision gate.

---

### Write the memo

Write to `simulations/{topic}/{topic}-story-{date}.md`.

Use the structure below. Sections should be short — a memo is not a report.
The decision-maker's time is the constraint.

---

```markdown
# {Topic} — Decision Memo
*To: {recipient}*
*As of: {date}. {N} signals synthesized.*

## Bottom Line
{One paragraph. Open with the recommendation: PROCEED / PAUSE / PIVOT / ABANDON.
Then state the one finding that most directly drives it. A reader who reads only
this section should leave knowing what the team recommends and why.}

## What We Set Out to Understand
{One to two sentences. The original question. What decision was this signal
gathering in service of?}

## What the Signals Showed
{One finding per signal — the finding most relevant to the original question.
Two sentences maximum per signal. These are evidence for the Bottom Line, not a
tour of each artifact.}

## The Pattern
{The cross-signal reading — what the signals say together that no single signal
says alone. This is the analytical center of the memo. Name the convergence,
divergence, tension, or gap. Reference at least two signals explicitly. Draw the
conclusion that justifies the Bottom Line.

If the pattern does not justify the Bottom Line, revise one of them — they must
be consistent.}

## What We Don't Know Yet
{Specific open questions that remain after all signals are gathered. Scope each:
what exactly is unknown, and what does it cost the recommendation? If an answer
would change the Bottom Line, say so explicitly.}
```

---

### Voice

Write as the analyst who has seen everything and has a point of view. Declarative
sentences. No hedging unless the hedge is the honest read. If the evidence is
mixed, say so in the Pattern section and let the Bottom Line reflect it.

---

## V-04

**Variation axis**: Combination — output format (explicit scaffold, V-02 style) +
lifecycle emphasis (pre-write pattern identification, V-01 style)
**Hypothesis**: V-01's pre-write worksheet prevents summary drift by making the
cross-signal pattern a required intermediate deliverable. V-02's anti-summary
prohibition creates primacy-anchored resistance to enumeration. These are
orthogonal mechanisms that target the same failure mode at different points: V-01
intervenes before writing begins (analytical gate); V-02 intervenes at the moment
of composition (framing gate). The combination should be more robust than either
alone because it closes the gaps each leaves open. V-01 alone does not prevent
a model from writing the worksheet correctly and then summarizing anyway; V-02
alone does not prevent a model that respects the prohibition from still producing
a thin Beat 3 because the pattern was never properly identified. Together they
enforce both the identification step and the composition step.

---

**Before anything else**: this skill synthesizes signals. It does not summarize.

Synthesis answers: *what do the signals say together?*
Summary answers: *what did each signal say?*

If your output answers the second question across signals in sequence, delete it
and answer the first question instead. The difference is not rhetorical — Beat 3
fails if its claim could be derived from any single signal alone.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Pattern identification (before writing)

Before opening the output artifact, answer privately:

1. What was the original question? (One sentence, from strategy.md or inferred.)
2. What is the single most important finding from each signal artifact?
   ({artifact-name}: {finding})
3. What do two or more signals show together that no single signal shows alone?
   Reference the specific artifact names. If your answer could be derived from
   any single artifact, you have not found the pattern yet.

Do not write the story until you have answered question 3.

---

### Step 3 — Write the story

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

Use the scaffold below. Each section must be present. Conciseness preferred.

---

```markdown
# {Topic} Story
*As of {date}. {N} of {M} signals gathered.*

## What We Set Out to Understand
[1–3 sentences. The original question. What specific uncertainty motivated
signal gathering?]

## What Each Signal Revealed
[One bullet per signal:
`**{artifact-name}** — {one key finding, one to two sentences, the finding most
relevant to the original question.}`
Secondary findings are omitted. Edit ruthlessly.]

## What the Signals Say Together
[The pattern from Step 2, question 3 — written as narrative. One to three
paragraphs. Name the convergence, divergence, tension, or gap. Reference at least
two signals explicitly. Draw the cross-signal conclusion.
This section fails if it restates what individual signals found rather than what
they mean together.]

## What Remains Uncertain
[Bulleted list of specific open questions. Each item: name the gap, scope it
(what exactly is unknown), state why it matters for the recommendation.]

## Recommendation
**{PROCEED | PAUSE | PIVOT | ABANDON}**

[One paragraph. Connect the recommendation to the pattern named above. State
specifically what drives it. If pause or pivot: what would need to change to
move to proceed?]
```

---

### Synthesis check

Before writing "What the Signals Say Together," ask: *Could any single signal
have produced this conclusion?* If yes, the pattern has not been found. Return
to the signal set and look for what multiple signals reveal in combination.

---

## V-05

**Variation axis**: Combination — phrasing register (memo to stakeholder, V-03) +
anti-summary prohibition (V-02)
**Hypothesis**: V-03's BLUF memo format produces strong C-03 and C-07 coverage
(the recommendation is stated first and must be justified by the evidence that
follows) but creates a structural risk: a model that fills each section
independently may produce a Bottom Line recommendation that is not actually
supported by the Pattern section. The anti-summary prohibition from V-02, placed
at the opening, creates a framing that primes the model to find the cross-signal
pattern before committing to the Bottom Line — which is when the recommendation is
written. The combination tests whether leading with the synthesis prohibition and
then using the memo format to enforce recommendation grounding produces better
C-04 + C-07 joint coverage than either mechanism alone.

---

**This memo synthesizes signals. It does not summarize them.**

A synthesis identifies what the signals say together — the pattern only visible
across the full set. A summary recaps what each signal said. The Bottom Line of
this memo must rest on the pattern, not on the summary.

If you have not found the cross-signal pattern before writing the Bottom Line,
the Bottom Line will be a guess. Find the pattern first.

---

You are writing a feature decision memo. The topic name is provided.

**Gather inputs first.**
Glob `simulations/**/{topic}-*`. Read every artifact.
Also read `simulations/{topic}/strategy.md` if present.

**Find the pattern before writing.**
After reading all signals, identify what two or more signals show in combination
that neither shows alone. This is the pattern that will ground the Bottom Line.

**Then write the memo** to `simulations/{topic}/{topic}-story-{date}.md`.

---

```markdown
# {Topic} — Decision Memo
*As of {date}. {N} signals synthesized.*

## Bottom Line
{Open with PROCEED / PAUSE / PIVOT / ABANDON. Then the finding that most directly
drives it. This section rests on the Pattern section below — write them
consistently. A reader who reads only the Bottom Line should know the
recommendation and its primary driver.}

## What We Set Out to Understand
{One to two sentences. The original question. What decision was signal gathering
in service of?}

## What the Signals Showed
{One finding per signal — the finding most relevant to the original question.
Two sentences maximum per signal. These are evidence, not a tour of artifacts.}

## The Pattern
{The cross-signal finding — what the signals say together that no single signal
says alone. Reference at least two signals explicitly. Name the convergence,
divergence, tension, or gap.

Falsifiability test: if your pattern claim could have come from any single signal,
it is not a cross-signal pattern. Find the real one.

This section must justify the Bottom Line. If the pattern does not support the
recommendation, revise one of them — they must be consistent.}

## What We Don't Know Yet
{Specific open questions. Scope each: what is unknown and what would it cost the
recommendation? If an answer would change the Bottom Line, say so.}
```

---

### Voice

Declarative. Opinionated. Write as the analyst who has seen everything and has a
view. If the evidence is genuinely mixed, the Pattern section says so and the
Bottom Line reflects it.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`
