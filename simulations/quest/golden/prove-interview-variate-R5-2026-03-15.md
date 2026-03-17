# prove-interview — Prompt Variations R5
# Date: 2026-03-15
# Rubric: prove-interview-rubric-v5-2026-03-15.md
# Round: 5 (first generation targeting v5 criteria C-19, C-20)

---

## Variation Axes Selected

| Axis | Description |
|------|-------------|
| Role sequence | Champion -> Skeptic -> Implementer arc, disposition declared per subject |
| Output format | Full table matrix: subject cards, evidence, synthesis, verdict all in structured tables |
| Lifecycle emphasis | Hard phase gates with explicit gate-condition language between every phase |
| Inertia framing | Status-quo incumbent user required as first subject; friction as evidence baseline |
| Phrasing register + verdict-frame-first | Coaching voice + verdict question posed before any subject design begins |

Single-axis variations: V-01 (role sequence), V-02 (output format), V-03 (lifecycle emphasis)
Combination variations: V-04 (inertia framing + role sequence), V-05 (coaching register + verdict-frame-first)

---

## V-01 -- Role Sequence: Disposition Arc (Champion -> Skeptic -> Implementer)

**Axis**: Role sequence
**Hypothesis**: Prescribing a champion-first, skeptic-second, implementer-last sequence forces an
explicit disposition arc (C-11) and prevents the simulation from collapsing to a uniform neutral
panel. The arc also creates a natural evidence tension: the champion establishes the upside case,
the skeptic stress-tests it, and the implementer grounds both in operational reality. Declaring the
verdict frame before any subject work begins (C-20) then lets readers evaluate whether the arc
resolved toward a decision or surfaced a genuine open question.

```
You are running a simulated stakeholder interview series to investigate a hypothesis.

STEP 0 -- VERDICT FRAME
Before designing any subject, declare the verdict frame for this investigation.
State the hypothesis you are investigating. Then answer:
- What would SUPPORT this hypothesis look like in interview evidence?
- What would CHALLENGE it?
- What would CONTRADICT it?
- What would leave the question INCONCLUSIVE?

This frame is the decision target. All subject design, question sequencing, and evidence
extraction must orient toward it.

---

STEP 1 -- SUBJECT ROSTER (three subjects, fixed sequence)

Interview exactly three subjects in this order:

1. THE CHAMPION
   A stakeholder who has already formed a positive view of or is predisposed toward
   this direction. They may be an early adopter, an internal advocate, or someone
   whose role benefits most directly from the hypothesis being true.

2. THE SKEPTIC
   A stakeholder whose role, experience, or incentives give them substantive reasons
   to doubt. Not a straw-man objector -- they have legitimate concerns grounded in
   their domain knowledge.

3. THE IMPLEMENTER
   A practitioner who will execute or operate the result. They are not primarily
   concerned with whether the hypothesis is right; they care whether it is feasible,
   maintainable, and compatible with their current workload.

For each subject, write a Subject Card before any questions:
- Role: job title and domain
- Prior knowledge: what they have seen, done, or worked with relevant to this topic
- Blind spots: what they have NOT seen, NOT done, or do NOT know yet -- a separate,
  explicit field, not a sub-bullet of concerns
- Disposition: champion / skeptic / neutral / resistant / curious -- declare one
- Primary concern: the one thing that would make this decision easy or hard for them

---

STEP 2 -- INTERVIEWS (run in sequence: champion first, then skeptic, then implementer)

For each subject, run two phases:

PART A -- REALITY PHASE
Open with 3-4 questions establishing this subject's current experience, practice, or
pain. No reference to the hypothesis or feature framing. Anchor in their current world.
Listen for the authentic shape of what they are doing today.

PART B -- HYPOTHESIS PHASE
Ask 2-3 questions that react directly from Part A answers. Each Part B question must
name a specific Part A answer as its anchor (e.g., "You mentioned that [X] -- given
that, here is what I want to ask..."). Do not issue generic hypothesis questions that
could have been asked before the Part A interview.

Write every answer in the subject's voice -- vocabulary, concerns, and framing
consistent with their declared role, background, and disposition. If an answer could
have come from any of the three subjects interchangeably, rewrite it.

---

STEP 3 -- EXTRACTION (immediately after each transcript, before moving to next subject)

Extract evidence items for this subject. For each item:
- [Type]: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
- [Strength]: STRONG / MODERATE / WEAK
- [Rationale]: one sentence explaining why this item earns that strength rating
  (name the source type, circumstance, or specificity -- e.g., "strong: verbatim
  objection from the buyer, unprompted"; "weak: inferred from tone, not stated")
- Flag one item per subject as SURPRISING MOMENT or CONFIRMING MOMENT and label it

---

STEP 4 -- SYNTHESIS

Write synthesis covering all three subjects and their arc:

1. DISPOSITION ARC
   How did the evidence move across champion -> skeptic -> implementer? What did the
   champion assert that the skeptic challenged? What did the implementer reveal that
   neither anticipated? Name what was reinforced, what shifted, and what was only
   visible from the implementer's position.

2. CONVERGENCE
   Where do all three subjects agree, even from different dispositions?

3. CONTRADICTION
   Name at least one specific conflict between subjects' extracted items -- name the
   subjects and the specific items that contradict each other. Do not suppress
   contradictions in favor of a clean narrative.

4. EPISTEMIC RE-WEIGHTING
   Revisit each subject's extracted items against their declared blind spots.
   Flag any item where the blind spot reduces evidential standing (mark as
   CONDITIONAL). Credit items from fully-informed subjects accordingly (mark as
   GROUNDED). A strong objection from a subject who has not seen the alternative is
   not equivalent to a strong objection from a subject who has.

---

STEP 5 -- NET VERDICT

Issue a verdict. One or two sentences. Declare whether the aggregate interview evidence
SUPPORTS, CHALLENGES, CONTRADICTS, or is genuinely INCONCLUSIVE about the hypothesis.
Reference the verdict frame from Step 0: did the arc resolve the question or leave it
open? This is the decision-ready output -- not a summary, a direction.
```

---

## V-02 -- Output Format: Annotated Evidence Matrix

**Axis**: Output format
**Hypothesis**: Moving all extraction to structured tables maximizes composability with
downstream /topic: evidence aggregation. Tables enforce annotation completeness by
construction: an empty cell is visible; a missing inline tag is not. The evidence matrix
format also makes epistemic re-weighting (C-19) explicit -- a separate column for
epistemic standing prevents it from being absorbed into prose. The verdict frame table
at the top (C-20) gives the artifact a decision target that readers can verify against
the final verdict table.

```
You are running a simulated interview investigation. All output follows structured table
format for composability with downstream /topic: evidence aggregation.

---

VERDICT FRAME TABLE
State the hypothesis, then complete this table before any subject work:

| Signal Type | Would Look Like in Evidence |
|-------------|-----------------------------|
| SUPPORT     |                             |
| CHALLENGE   |                             |
| CONTRADICT  |                             |
| INCONCLUSIVE|                             |

---

SUBJECT CARDS TABLE
Complete all subject cards before writing any transcript.

| Field              | Subject 1 | Subject 2 | Subject 3 |
|--------------------|-----------|-----------|-----------|
| Name / Role        |           |           |           |
| Domain             |           |           |           |
| Disposition        |           |           |           |
| Prior Knowledge    |           |           |           |
| Blind Spots        |           |           |           |
| Primary Concern    |           |           |           |

Minimum: 2 subjects. Each must be meaningfully distinct in role or concern level.
A second subject who echoes the first adds no coverage -- redesign them.

---

TRANSCRIPTS

For each subject:

**[Subject Name / Role] -- [Disposition]**

PART A -- REALITY (no hypothesis framing)
Q1: [question]
A1: [answer in subject's voice]
Q2: [question]
A2: [answer]
Q3: [question]
A3: [answer]

PART B -- HYPOTHESIS (each question anchored to a named Part A answer)
Q4 [anchored to A{N}]: [question]
A4: [answer]
Q5 [anchored to A{N}]: [question]
A5: [answer]

---

EVIDENCE MATRIX
Fill immediately after each transcript. One row per evidence item.

| # | Subject | Evidence Item | Type | Strength | Rationale | Epistemic Standing | Moment Flag |
|---|---------|---------------|------|----------|-----------|--------------------|-------------|
| 1 |         |               |      |          |           |                    |             |
| 2 |         |               |      |          |           |                    |             |

Column definitions:
- Type: RISK / PREF / CONSTRAINT / VALID / INVALID / SIGNAL
- Strength: STRONG / MOD / WEAK
- Rationale: one sentence naming source type, circumstance, or specificity
- Epistemic Standing: GROUNDED (subject has direct experience) / CONDITIONAL (subject
  has declared blind spot relevant to this item) / INFERRED (stance not directly stated)
- Moment Flag: SURPRISING / CONFIRMING / --

---

SYNTHESIS TABLE

| Dimension                                    | Finding |
|----------------------------------------------|---------|
| Convergence (where subjects agree)            |         |
| Contradiction (named items, named subjects)   |         |
| Disposition arc trajectory                    |         |
| Epistemic re-weighting: CONDITIONAL items     |         |
| Epistemic re-weighting: GROUNDED credits      |         |
| Blind-spot-affected evidence (flagged)        |         |

---

NET VERDICT TABLE

| Verdict                                              | Statement |
|------------------------------------------------------|-----------|
| SUPPORTS / CHALLENGES / CONTRADICTS / INCONCLUSIVE   |           |

One or two sentences. Decision-ready output referenced against the Verdict Frame Table.
```

---

## V-03 -- Lifecycle Emphasis: Hard Phase Gates

**Axis**: Lifecycle emphasis
**Hypothesis**: Hard gate conditions between phases prevent the most common simulation failure
modes: persona knowledge discovered through answers rather than declared before them (C-05/C-16
gap), hypothesis questions issued before the subject's reality is established (C-15 gap), and
synthesis written without all evidence items carrying complete annotation (C-09/C-12/C-13 gap).
Each gate is a binary checkpoint -- a written condition that must be true before the next phase
begins. Gates are not stylistic; they are structural enforcement.

```
You are running a simulated interview investigation organized into PHASES with explicit GATE
CONDITIONS. Do not begin a later phase until the stated gate condition is satisfied.

================================================================================
PHASE 0 -- INVESTIGATION FRAMING
================================================================================

Write:
1. The hypothesis under investigation (one sentence)
2. The verdict frame: what SUPPORT, CHALLENGE, CONTRADICTION, and INCONCLUSIVE look like
   for this specific hypothesis -- not generic descriptions, specific evidence signatures

GATE 0 -> PHASE 1: Do not begin subject design until the verdict frame is written in full
with all four signal types populated. An empty INCONCLUSIVE row does not pass.

================================================================================
PHASE 1 -- SUBJECT DESIGN
================================================================================

Design all subject cards before writing any transcript. For each subject:

- Role and domain
- Prior knowledge: what they have seen, done, or worked with (positive declaration)
- Blind spots: what they have NOT seen, NOT done, or do NOT know -- a separate field,
  not implied by their knowledge scope
- Disposition: champion / skeptic / neutral / resistant / curious -- one declared value
- Primary concern: the one thing that most shapes their evaluation

Minimum: 2 subjects. Each must be meaningfully distinct in role, knowledge level, or
concern -- not a minor variation of the same profile.

GATE 1 -> PHASE 2: Verify all subject cards before proceeding. Checklist:
  [ ] Every subject has a distinct role from every other subject
  [ ] Every subject has an explicit Blind Spots field (not blank, not "none known")
  [ ] Every subject has a declared Disposition value
  [ ] No two subjects share the same primary concern
Do not proceed to transcripts until all four checks pass.

================================================================================
PHASE 2 -- REALITY-PHASE TRANSCRIPTS
================================================================================

For each subject, run Part A only. Do NOT mention the hypothesis, the feature, or the
direction being investigated. Ask about current experience, current practice, current pain.
3-4 questions per subject. Write all answers in subject's voice.

Run Part A for ALL subjects before writing a single Part B question.

GATE 2 -> PHASE 3: Verify Part A completeness. For each subject:
  [ ] Part A contains at least one concrete description of current-state experience
  [ ] No Part A question names or directly invites reaction to the hypothesis
  [ ] All answers are written in the subject's voice (distinct vocabulary and concerns)
Do not proceed to Part B until all checks pass for all subjects.

================================================================================
PHASE 3 -- HYPOTHESIS-PHASE TRANSCRIPTS
================================================================================

For each subject, run Part B. Each Part B question must explicitly anchor to a specific
Part A answer from that subject -- name the anchor by referencing what the subject said
(e.g., "You mentioned in Part A that [X] -- given that, ...").

2-3 questions per subject. Generic hypothesis questions with no named Part A anchor
are not permitted.

GATE 3 -> PHASE 4: For every Part B question, confirm:
  [ ] The anchor reference names a specific Part A answer (not "in general" or "earlier")
  [ ] The question reacts from the subject's stated reality, not from generic hypothesis
      framing
Any unanchored Part B question must be revised before extraction begins.

================================================================================
PHASE 4 -- EVIDENCE EXTRACTION
================================================================================

For each subject, extract evidence items immediately after their transcript.
Every item must carry all three annotations before proceeding:

- [Type]: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
- [Strength]: STRONG / MODERATE / WEAK
- [Rationale]: one sentence -- name the source type, circumstance, or specificity
  (e.g., "strong: direct operational experience, unprompted"; "weak: speculative,
  no direct exposure")

Flag one item per subject as SURPRISING MOMENT or CONFIRMING MOMENT.

GATE 4 -> PHASE 5: Verify the evidence table:
  [ ] Every item has a Type annotation
  [ ] Every item has a Strength rating
  [ ] Every item has a Rationale (not blank, not "see above")
  [ ] Every subject has exactly one flagged Moment
Any item missing any of these fields must be completed before synthesis begins.

================================================================================
PHASE 5 -- SYNTHESIS AND VERDICT
================================================================================

Write synthesis:
1. Cross-subject convergence: where do subjects agree despite different roles?
2. Contradiction: name at least one specific conflict between extracted items from
   different subjects -- name the subjects and the items
3. Epistemic re-weighting: review each subject's extracted items against their declared
   blind spots; flag conditional items explicitly; credit fully-informed subjects
4. Disposition arc: if subjects have distinct dispositions, name what changed or held
   across the arc

Issue NET VERDICT: one or two sentences declaring whether the aggregate evidence
SUPPORTS, CHALLENGES, CONTRADICTS, or is INCONCLUSIVE about the hypothesis.
Reference the verdict frame from Phase 0.

GATE 5 (terminal): The verdict must name a direction -- it must not resolve to
"more research needed" without also naming what specific evidence type would close
the question.
```

---

## V-04 -- Inertia Framing + Role Sequence: Status-Quo Incumbent First

**Axis**: Inertia framing (combined with role sequence)
**Hypothesis**: Making a status-quo user the required first interview subject grounds all
subsequent evidence against realistic switching cost. Without an incumbent voice, simulated
panels systematically underweight inertia -- the most common reason good hypotheses fail in
practice. Naming the current solution explicitly in Step 0 and requiring the first subject
to be its power user forces evidence against the real alternative, not an abstract "old way."
The role sequence (incumbent -> pain-holder -> pragmatist) produces an inertia-to-friction-to-
neutral arc that surfaces both the strength of the status quo and the conditions under which
it would be abandoned.

```
You are running a simulated interview series investigating a hypothesis. This simulation uses
an inertia-first structure: the first subject is always someone deeply invested in the current
solution, process, or competitor. Their friction is the evidential baseline all subsequent
interviews are measured against.

---

STEP 0 -- VERDICT FRAME AND INERTIA ANCHOR

State the hypothesis you are investigating.

Declare the verdict frame:
- SUPPORT: what would interview evidence look like if the hypothesis is correct?
- CHALLENGE: what would partial or conditional evidence look like?
- CONTRADICT: what would strong disconfirmation look like?
- INCONCLUSIVE: what would leave the question genuinely open?

Then name the status-quo / incumbent / current solution that this hypothesis displaces
or competes with. This is the INERTIA ANCHOR. Every subsequent interview and evidence
item must be evaluated against what adoption requires leaving behind.

---

STEP 1 -- SUBJECT ROSTER (three subjects, fixed sequence)

Subject 1 -- THE INCUMBENT USER (required first)
This person is a power user, advocate, or owner of the current solution named in Step 0.
They may be skeptical of the hypothesis specifically because they have invested in the
status quo, have it working well, or face real switching costs. Do NOT make them a
straw-man objector -- they have legitimate reasons for their current-state preference.
Their resistance, where it exists, is evidence, not noise.

Subject 2 -- THE PAIN-HOLDER
This person suffers a specific, documented limitation of the current solution. They are
not necessarily an early adopter of the new direction, but they have friction the
incumbent user either ignores or has learned to tolerate.

Subject 3 (optional) -- THE PRAGMATIST
This person does not have strong attachment to either the current or proposed direction.
They evaluate primarily on practical fit: cost, effort, compatibility, risk to their
existing commitments.

For each subject, write a Subject Card:
- Role and domain
- What they use today and why it works for them (or does not)
- Blind spots: what they have not seen about the alternative or the current solution's
  failure modes -- declared explicitly, not implied
- Disposition: champion / skeptic / neutral / resistant / curious
- Primary decision criterion: what would actually change their position?

---

STEP 2 -- INTERVIEWS (incumbent first, then pain-holder, then pragmatist)

For each subject, two phases:

PART A -- CURRENT REALITY
Ask about the subject's relationship to the current solution: what works, what costs
them, what they have tried to fix, what they have learned to live with. No hypothesis
framing. Minimum 3 questions.

PART B -- HYPOTHESIS PROBE
Each question anchors to a specific Part A answer. Name the anchor explicitly (e.g.,
"You said the current process takes three days -- if that were reduced to same-day,
would that change [X]?"). Do not genericize to the hypothesis without the anchor.

Write every answer in the subject's voice. The incumbent user and the pain-holder will
have different vocabularies for describing the same limitation -- that difference is
evidence.

---

STEP 3 -- EXTRACTION (per subject)

For each extracted evidence item:
- [Type]: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
- [Strength]: STRONG / MODERATE / WEAK
- [Rationale]: one sentence naming source type, circumstance, or specificity
- [Epistemic Standing]: GROUNDED (direct experience) / CONDITIONAL (blind spot affects
  this item -- name the blind spot) / INFERRED (stance not directly stated)
- Flag one item per subject as SURPRISING MOMENT or CONFIRMING MOMENT

---

STEP 4 -- SYNTHESIS

1. INERTIA ACCOUNTING
   What would it actually take to move Subject 1 (the Incumbent User)? Name the
   specific friction items from their extraction. Is that friction fatal to the
   hypothesis, solvable by design, or irrelevant given Subject 2's pain?

2. CONVERGENCE AND CONTRADICTION
   Where do subjects agree despite different starting positions? Where do Subject 1
   and Subject 2 diverge on the same limitation -- name the specific items.

3. EPISTEMIC RE-WEIGHTING
   Apply each subject's declared blind spots to their extracted evidence:
   - Items flagged CONDITIONAL carry reduced evidential standing until the blind
     spot is resolved
   - Items flagged GROUNDED from subjects with direct relevant experience carry
     full evidential standing
   The incumbent user's reliability objection about a system they have not used is
   CONDITIONAL; the same objection from a practitioner who has piloted it is GROUNDED.
   Name the difference in the synthesis.

4. DISPOSITION ARC
   Did the arc (incumbent -> pain-holder -> pragmatist) reveal any pathway under
   which the incumbent's resistance could weaken? Or did the pain-holder's evidence
   leave the inertia barrier intact?

---

STEP 5 -- NET VERDICT

One or two sentences. Does the aggregate evidence -- including the inertia baseline --
SUPPORT, CHALLENGE, CONTRADICT, or leave INCONCLUSIVE the hypothesis?

Name specifically whether incumbent friction is a fatal barrier, a solvable switching
cost, or an objection neutralized by the pain-holder's evidence. A verdict that ignores
the inertia anchor does not close the investigation.
```

---

## V-05 -- Coaching Register + Verdict-Frame-First

**Axis**: Phrasing register (coaching voice) combined with verdict-frame-first structure
**Hypothesis**: Addressing the LLM as a practitioner being coached through a decision
investigation -- "before you write a single question, answer this..." -- keeps the simulation
oriented toward a verdict rather than toward transcript completeness. The coaching register
creates a sequence of self-verification moments that substitute for hard phase gates while
preserving flow. Opening with the verdict question (C-20) and closing with the verdict output
(C-18) creates a frame-and-resolve structure that makes it structurally difficult to produce
an artifact that collects evidence without deciding.

```
Before you interview anyone, answer this question:

What would it take to be convinced?

State the hypothesis you are investigating. Then write one or two sentences for each:
- What would SUPPORT this hypothesis look like if you heard it in an interview?
- What would CHALLENGE it?
- What would CONTRADICT it?
- What would leave the evidence INCONCLUSIVE?

This is your verdict frame. Hold it in mind throughout. Every subject you design, every
question you ask, and every evidence item you extract will be evaluated against it.

---

Now design your subjects.

You need at least two. Each subject should give you a genuinely different angle --
different role, different knowledge level, different concerns about this domain. If your
second subject is a quieter version of your first, redesign them. A second subject who
agrees with the first without adding new perspective wastes an interview slot.

For each subject, write their card before you write a single question. The card has
five parts:

1. Who they are -- their role, domain, and what they have been doing in this space

2. What they know -- their prior experience and relevant context; things they have
   actually seen or done, not things you wish they knew

3. What they do not know -- their blind spots: what they have not encountered, not
   used, not been exposed to. Be honest here. If they have not seen the alternative
   in production, say so. If they have no experience with the failure mode your
   hypothesis addresses, name it. Blind spots are not weaknesses -- they are
   evidence-weighting information.

4. How they are disposed -- champion, skeptic, neutral, resistant, or curious.
   Pick one and declare it. Neutral is a valid answer but it should be a choice,
   not a default.

5. What they care about most -- the one thing that would make this decision easy
   or hard for them. Their decision criterion, not their job description.

Do not write a single transcript line until all subject cards are complete.

---

Now run the interviews.

For each subject, start in their current reality. Ask about what they are doing today,
what is working, what is not, what they have tried to fix. Do not mention your hypothesis
yet. You are listening for the authentic shape of their world before you introduce your
question. Three to four questions in their current reality.

After those questions, transition to the hypothesis -- but anchor the transition. Do not
just start asking about the new thing. Connect it explicitly to something the subject
just said. "You mentioned [X] -- given that, here is what I want to ask you..." If you
cannot find a Part A answer to anchor to, it means your Part A questions did not
establish enough of their reality. Add a question.

Write every answer in the subject's voice. If you catch yourself writing an answer that
could have come from any of your subjects -- same vocabulary, same concerns, same framing
-- stop and rewrite it from this subject's specific background and disposition. The
interviews should sound different from each other.

---

After each transcript, extract the evidence.

For each item you extract:
- Tag its type: is it a risk, a preference, a constraint, a validation, an invalidation,
  or a signal?
- Rate its strength: strong, moderate, or weak
- Justify the rating in one sentence: why does this item earn that strength? Name the
  source type, the circumstance, or what makes it specific. "Strong" without a rationale
  is not a rating -- it is a guess.
- Note whether this item is grounded (the subject has direct relevant experience) or
  conditional (their declared blind spot affects how much weight this item carries).
  A conditional item is not worthless -- it is evidence that needs to be held lightly
  until the blind spot is resolved.

Mark one item per subject as a SURPRISING MOMENT (something you did not expect given
their declared disposition) or a CONFIRMING MOMENT (something that landed exactly where
you expected it, and is valuable because of that).

---

Now synthesize.

Look at what these interviews say together. You are not summarizing -- you are comparing.
Find:
- Where subjects converge, even from different angles and different dispositions
- Where they contradict each other -- name the specific items and which subjects hold
  them. Do not average contradictions away. A contradiction is the highest-signal output
  of a multi-persona investigation.
- How the arc of dispositions moved. Did the skeptic surface something the champion
  missed? Did the neutral subject reveal a constraint neither anticipated?

Then revisit your evidence items against each subject's declared blind spots. Take the
CONDITIONAL items: what are they conditional on? Could that condition be resolved by
design, by demonstration, or by new information? The synthesis must show that blind-spot
declarations are load-bearing -- that they changed how you read the evidence, not just
that they were recorded.

Go back to your verdict frame. For each major evidence item, place it: does it land in
SUPPORT, CHALLENGE, CONTRADICT, or INCONCLUSIVE? Do not treat all items as equal.
Evidence from a subject with direct experience in the specific failure mode outweighs
evidence from a subject who is reasoning about it theoretically. Say so.

---

Close with your verdict.

One or two sentences. Declare whether the aggregate evidence supports, challenges,
contradicts, or is genuinely inconclusive about your hypothesis. Reference your verdict
frame from the opening: did the interviews answer the question you started with, or did
they reveal that you were asking the wrong question?

This is the decision-ready output. Do not summarize the interviews. Decide.
```
