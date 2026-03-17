# prove-interview — Prompt Variations R6
# Date: 2026-03-15
# Rubric: prove-interview-rubric-v6-2026-03-15.md
# Round: 6 (first generation targeting v6 criteria C-21, C-22)

---

## Variation Axes Selected

| Axis | Description |
|------|-------------|
| Role sequence | Incumbent -> Adopter -> Evaluator arc, incumbent designation required in subject card |
| Output format | Extended table matrix with Incumbent/Inertia Baseline columns and partition synthesis rows |
| Lifecycle emphasis | Hard phase gates — Gate 1 checks incumbent designation, Gate 5 checks partition |
| Inertia framing + role sequence | Inertia anchor named in Step 0 before any subject design; synthesis partition as named accounting step |
| Coaching register + verdict-frame-first | Coaching voice surfaces incumbent identification and partition as natural investigation hygiene |

Single-axis variations: V-01 (role sequence), V-02 (output format), V-03 (lifecycle emphasis)
Combination variations: V-04 (inertia framing + role sequence), V-05 (coaching register + verdict-frame-first)

---

## V-01 -- Role Sequence: Incumbent -> Adopter -> Evaluator Arc

**Axis**: Role sequence
**Hypothesis**: Prescribing a three-slot roster where the first slot is explicitly labeled INCUMBENT
(not "skeptic" or "power user") forces the inertia baseline declaration to appear in the subject
card rather than emerge from answers. When the incumbent slot is named and required first, the
artifact cannot avoid establishing the ground state being displaced before the hypothesis enters.
The adopter-second, evaluator-third sequence produces an inertia-to-openness arc whose delta is
directly legible in synthesis without additional instruction.

```
You are running a simulated stakeholder interview series to investigate a hypothesis.

STEP 0 -- VERDICT FRAME
Before designing any subject, declare the verdict frame for this investigation.
State the hypothesis you are investigating. Then write one to two sentences for each:
- What would SUPPORT this hypothesis look like in interview evidence?
- What would CHALLENGE it?
- What would CONTRADICT it?
- What would leave the question INCONCLUSIVE?

This frame is the decision target. All subject design, question sequencing, and evidence
extraction must orient toward it.

---

STEP 1 -- SUBJECT ROSTER (three subjects, fixed sequence)

Interview exactly three subjects in this order:

1. THE INCUMBENT
   A current practitioner who is already doing something in this space -- using an existing
   tool, following an established workflow, or deeply invested in the current approach your
   hypothesis would displace or improve upon. They are not defined by skepticism; they are
   defined by having an established practice. They may be satisfied, moderately frustrated,
   or highly frustrated -- but they are working within the current solution, not evaluating
   alternatives.

2. THE ADOPTER
   A stakeholder who has experienced a specific pain or gap with the current approach and
   is actively looking for a better path. They are not necessarily familiar with your
   specific hypothesis -- they have friction, and they want it resolved.

3. THE EVALUATOR
   A practitioner whose role requires them to assess fit, cost, compatibility, and risk.
   They are not primarily a user of the current approach or the proposed direction; they
   evaluate options against organizational or operational criteria.

For each subject, write a Subject Card before any questions. The card must include:

- Role: job title and domain
- Prior knowledge: what they have seen, done, or worked with relevant to this topic
- Blind spots: what they have NOT seen, NOT done, or do NOT know yet -- a separate explicit
  field, not a sub-bullet of prior knowledge
- Disposition: champion / skeptic / neutral / resistant / curious -- declare one
- Primary concern: the one thing that most shapes their evaluation
- Incumbent Designation: INCUMBENT or NON-INCUMBENT
- Inertia Baseline [required when Incumbent Designation = INCUMBENT]: Name the specific
  current practice, tool, workflow, or behavior this subject is invested in. One to two
  sentences. This is the ground state the hypothesis would displace. Declare it in the
  subject card -- do not let it emerge from answers.

---

STEP 2 -- INTERVIEWS (run in sequence: incumbent first, then adopter, then evaluator)

For each subject, run two phases:

PART A -- REALITY PHASE
Open with 3-4 questions establishing this subject's current experience, practice, or
pain. No reference to the hypothesis or feature framing. Anchor in their current world.
For the INCUMBENT: anchor deeply in their existing tool or workflow -- what works, what
costs them, what they have learned to live with.

PART B -- HYPOTHESIS PHASE
Ask 2-3 questions that react directly from Part A answers. Each Part B question must
name a specific Part A answer as its anchor (e.g., "You mentioned that [X] -- given
that, here is what I want to ask..."). Do not issue generic hypothesis questions that
could have been asked before the Part A interview.

Write every answer in the subject's voice -- vocabulary, concerns, and framing
consistent with their declared role, background, and disposition. The INCUMBENT and the
ADOPTER will describe the same limitation differently; that difference is evidence.

---

STEP 3 -- EXTRACTION (immediately after each transcript, before moving to next subject)

Extract evidence items for this subject. For each item:
- [Type]: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
- [Strength]: STRONG / MODERATE / WEAK
- [Rationale]: one sentence explaining why this item earns that strength rating
  (name the source type, circumstance, or specificity)
- [Epistemic Standing]: GROUNDED (subject has direct relevant experience) /
  CONDITIONAL (subject has a declared blind spot that affects this item -- name it) /
  INFERRED (stance not directly stated)
- Flag one item per subject as SURPRISING MOMENT or CONFIRMING MOMENT and label it

---

STEP 4 -- SYNTHESIS

Write synthesis covering all three subjects and their arc:

1. INERTIA / ADOPTION PARTITION
   Separate all extracted evidence into two named categories:

   INERTIA SIGNALS -- items that represent switching cost, workflow disruption, habit
   lock-in, or resistance to change from the incumbent's declared baseline. Include items
   from any subject that measure friction against leaving the current approach.

   ADOPTION SIGNALS -- items that represent openness to change, fit with the new direction,
   willingness to move, or enthusiasm for the hypothesis. Include items from any subject
   that measure pull toward the new approach.

   List the items under each category. Then state the adoption delta: what does the
   aggregate adoption evidence say relative to the aggregate inertia evidence?

2. CONVERGENCE
   Where do all three subjects agree, even from different roles and concerns?

3. CONTRADICTION
   Name at least one specific conflict between subjects' extracted items -- name the
   subjects and the specific items that contradict each other.

4. EPISTEMIC RE-WEIGHTING
   Revisit each subject's extracted items against their declared blind spots.
   Flag CONDITIONAL items and state what would resolve the condition. Credit GROUNDED
   items from subjects with direct relevant experience accordingly.

5. DISPOSITION ARC
   How did the evidence move across incumbent -> adopter -> evaluator? What did the
   incumbent's inertia baseline reveal that was not visible from the adopter's perspective?
   What did the evaluator surface that neither anticipated?

---

STEP 5 -- NET VERDICT

One or two sentences. Declare whether the aggregate interview evidence SUPPORTS,
CHALLENGES, CONTRADICTS, or is genuinely INCONCLUSIVE about the hypothesis.

Name specifically whether the inertia baseline is a fatal barrier, a solvable switching
cost, or an objection neutralized by the adopter's evidence. Reference the verdict frame
from Step 0. A verdict that does not address the inertia partition does not close the
investigation.
```

---

## V-02 -- Output Format: Inertia/Adoption Partition Matrix

**Axis**: Output format
**Hypothesis**: Adding an Incumbent Designation column and an Inertia Baseline row to the subject
cards table enforces C-21 by construction -- an empty Incumbent Designation cell is visible in a
way that an omitted prose declaration is not. Adding an explicit INERTIA SIGNALS / ADOPTION SIGNALS
row pair to the synthesis table enforces C-22 by construction -- the partition cannot be skipped
when it is a named, visually distinct table row. Table structure makes compliance binary and
auditable; prose structure makes omission easy to miss.

```
You are running a simulated interview investigation. All output follows structured table
format for composability with downstream /topic: evidence aggregation.

---

VERDICT FRAME TABLE
State the hypothesis, then complete this table before any subject work:

| Signal Type  | Would Look Like in Evidence |
|--------------|-----------------------------|
| SUPPORT      |                             |
| CHALLENGE    |                             |
| CONTRADICT   |                             |
| INCONCLUSIVE |                             |

---

SUBJECT CARDS TABLE
Complete all subject cards before writing any transcript.

| Field                     | Subject 1     | Subject 2     | Subject 3     |
|---------------------------|---------------|---------------|---------------|
| Name / Role               |               |               |               |
| Domain                    |               |               |               |
| Disposition               |               |               |               |
| Prior Knowledge           |               |               |               |
| Blind Spots               |               |               |               |
| Primary Concern           |               |               |               |
| Incumbent Designation     | INCUMBENT /   | INCUMBENT /   | INCUMBENT /   |
|                           | NON-INCUMBENT | NON-INCUMBENT | NON-INCUMBENT |
| Inertia Baseline          | [Required if  | [Required if  | [Required if  |
| (current practice named)  | INCUMBENT]    | INCUMBENT]    | INCUMBENT]    |

Rules:
- Minimum: 2 subjects. At least one must carry Incumbent Designation = INCUMBENT.
- The Inertia Baseline cell must name a specific current practice, tool, workflow, or
  behavior -- not a generic description. "Uses spreadsheets" is not sufficient.
  "Maintains a manually updated Excel tracker synced to SharePoint weekly, owns the
  template, and has built macros to automate reporting" is sufficient.
- A second subject who echoes the first without adding distinct role, knowledge level,
  or concern must be redesigned.

---

TRANSCRIPTS

For each subject:

**[Subject Name / Role] -- [Disposition] -- [Incumbent Designation]**

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
- Epistemic Standing: GROUNDED / CONDITIONAL (name the blind spot) / INFERRED
- Moment Flag: SURPRISING / CONFIRMING / --

---

SYNTHESIS TABLE

| Dimension                                              | Finding |
|--------------------------------------------------------|---------|
| INERTIA SIGNALS (aggregate, from all subjects)         |         |
| ADOPTION SIGNALS (aggregate, from all subjects)        |         |
| Adoption delta (inertia vs adoption balance)           |         |
| Convergence (where subjects agree)                     |         |
| Contradiction (named items, named subjects)            |         |
| Disposition arc trajectory                             |         |
| Epistemic re-weighting: CONDITIONAL items flagged      |         |
| Epistemic re-weighting: GROUNDED credits               |         |

Partition rule: INERTIA SIGNALS and ADOPTION SIGNALS rows must each contain at least
one evidence item from the extraction matrix. An empty inertia row means the incumbent
baseline produced no friction evidence -- state that explicitly rather than leaving the
cell blank.

---

NET VERDICT TABLE

| Verdict                                            | Statement |
|----------------------------------------------------|-----------|
| SUPPORTS / CHALLENGES / CONTRADICTS / INCONCLUSIVE |           |

One or two sentences. Decision-ready output referenced against the Verdict Frame Table
and the adoption delta row in Synthesis.
```

---

## V-03 -- Lifecycle Emphasis: Gates with Incumbent and Partition Checks

**Axis**: Lifecycle emphasis
**Hypothesis**: Adding two targeted gate checks -- one at subject design requiring at least one
INCUMBENT designation with a named inertia baseline, and one at synthesis requiring a named
inertia/adoption partition before verdict -- enforces C-21 and C-22 as binary preconditions.
Without gates, both criteria depend on the LLM voluntarily including them; with gates, the
output cannot advance to the next phase without satisfying them. The gate language does not
need to be elaborate -- the binary check is the mechanism.

```
You are running a simulated interview investigation organized into PHASES with explicit GATE
CONDITIONS. Do not begin a later phase until the stated gate condition is satisfied.

================================================================================
PHASE 0 -- INVESTIGATION FRAMING
================================================================================

Write:
1. The hypothesis under investigation (one sentence)
2. The verdict frame: what SUPPORT, CHALLENGE, CONTRADICTION, and INCONCLUSIVE evidence
   looks like for this specific hypothesis -- not generic descriptions, specific signatures

GATE 0 -> PHASE 1: Do not begin subject design until the verdict frame is written in full
with all four signal types populated. An empty INCONCLUSIVE row does not pass.

================================================================================
PHASE 1 -- SUBJECT DESIGN
================================================================================

Design all subject cards before writing any transcript. For each subject:

- Role and domain
- Prior knowledge: what they have seen, done, or worked with (positive declaration)
- Blind spots: what they have NOT seen, NOT done, or do NOT know yet -- a separate
  explicit field, not implied by their knowledge scope
- Disposition: champion / skeptic / neutral / resistant / curious -- one declared value
- Primary concern: the one thing that most shapes their evaluation
- Incumbent Designation: INCUMBENT or NON-INCUMBENT
  - If INCUMBENT: also declare the Inertia Baseline -- the specific current practice,
    tool, workflow, or behavior this subject is invested in. This is the ground state
    the hypothesis would displace. Name it explicitly in the subject card.

Minimum: 2 subjects. Each must be meaningfully distinct in role, knowledge level, or
concern -- not a minor variation of the same profile.

GATE 1 -> PHASE 2: Verify all subject cards before proceeding. Checklist:
  [ ] Every subject has a distinct role from every other subject
  [ ] Every subject has an explicit Blind Spots field (not blank, not "none known")
  [ ] Every subject has a declared Disposition value
  [ ] No two subjects share the same primary concern
  [ ] At least one subject carries Incumbent Designation = INCUMBENT
  [ ] Every INCUMBENT subject has a named Inertia Baseline (not blank, not generic)
Do not proceed to transcripts until all six checks pass.

================================================================================
PHASE 2 -- REALITY-PHASE TRANSCRIPTS
================================================================================

For each subject, run Part A only. Do NOT mention the hypothesis, the feature, or the
direction being investigated. Ask about current experience, current practice, current pain.
For INCUMBENT subjects: anchor firmly in their declared Inertia Baseline -- what works,
what costs them, what they have learned to live with.
3-4 questions per subject. Write all answers in subject's voice.

Run Part A for ALL subjects before writing a single Part B question.

GATE 2 -> PHASE 3: Verify Part A completeness. For each subject:
  [ ] Part A contains at least one concrete description of current-state experience
  [ ] No Part A question names or directly invites reaction to the hypothesis
  [ ] All answers are written in the subject's voice (distinct vocabulary and concerns)
  [ ] INCUMBENT subjects' answers reflect their declared Inertia Baseline specifically
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
Every item must carry all four annotations before proceeding:

- [Type]: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
- [Strength]: STRONG / MODERATE / WEAK
- [Rationale]: one sentence -- name the source type, circumstance, or specificity
- [Epistemic Standing]: GROUNDED / CONDITIONAL (name the blind spot) / INFERRED

Flag one item per subject as SURPRISING MOMENT or CONFIRMING MOMENT.

GATE 4 -> PHASE 5: Verify the evidence table:
  [ ] Every item has Type, Strength, Rationale, and Epistemic Standing annotations
  [ ] No Rationale field is blank or reads "see above"
  [ ] Every subject has exactly one flagged Moment
Any item missing any field must be completed before synthesis begins.

================================================================================
PHASE 5 -- SYNTHESIS AND VERDICT
================================================================================

Write synthesis in this order:

1. INERTIA / ADOPTION PARTITION (required; name this heading explicitly)
   Collect all extracted evidence items. Assign each to one of two categories:

   INERTIA SIGNALS -- switching cost, workflow disruption, habit lock-in, resistance
   to change from the incumbent's declared baseline. List the items.

   ADOPTION SIGNALS -- openness, fit, willingness to move, enthusiasm. List the items.

   State the adoption delta: what does the aggregate adoption evidence say relative to
   the aggregate inertia evidence? Is inertia dominant, balanced, or marginal?

2. CONVERGENCE -- where do subjects agree despite different roles?

3. CONTRADICTION -- name at least one specific conflict between extracted items from
   different subjects; name the subjects and the items

4. EPISTEMIC RE-WEIGHTING -- flag CONDITIONAL items and credit GROUNDED ones; show
   that blind-spot declarations changed how evidence is weighted

5. DISPOSITION ARC -- name what changed or held across the subject sequence

Issue NET VERDICT: one or two sentences declaring SUPPORTS / CHALLENGES / CONTRADICTS
/ INCONCLUSIVE. Address the inertia partition explicitly: is incumbent friction fatal,
solvable, or neutralized?

GATE 5 -> PHASE 1: Verify synthesis before treating the artifact as complete:
  [ ] Synthesis contains a named INERTIA / ADOPTION PARTITION section
  [ ] Partition lists at least one item under each category (or explicitly names why
      one category is empty)
  [ ] Adoption delta is stated
  [ ] NET VERDICT names a direction and addresses the inertia partition
An artifact that issues a verdict without a named partition does not satisfy GATE 5.
```

---

## V-04 -- Inertia Framing + Role Sequence: Named Baseline in Step 0

**Axis**: Inertia framing (combined with role sequence)
**Hypothesis**: Naming the inertia anchor as a top-level Step 0 declaration -- before any subject
cards are written -- creates the strongest possible C-21 signal: the ground state being displaced
is established before any interview subject exists. The incumbent designation in the subject card
then refers back to an already-declared artifact-level anchor, making the baseline a first-class
artifact element rather than a subject-specific annotation. C-22's partition follows naturally:
when the artifact has already named the ground state at the opening, the synthesis partition is
accounting against an established reference rather than a retrospective inference.

```
You are running a simulated interview series investigating a hypothesis. This simulation
uses an inertia-first structure: the inertia anchor -- the current solution, practice, or
behavior the hypothesis would displace -- is named at the artifact level before any
interview subject is designed.

---

STEP 0 -- VERDICT FRAME AND INERTIA ANCHOR

State the hypothesis you are investigating.

Declare the verdict frame:
- SUPPORT: what would interview evidence look like if the hypothesis is correct?
- CHALLENGE: what would partial or conditional evidence look like?
- CONTRADICT: what would strong disconfirmation look like?
- INCONCLUSIVE: what would leave the question genuinely open?

Then name the INERTIA ANCHOR:
The specific current practice, tool, workflow, or established behavior that this hypothesis
would displace, replace, improve upon, or compete against. This is the ground state.
One to three sentences. Be specific: name the tool or process by type, the users who
depend on it, and what makes it sticky. Generic descriptions ("the current approach") do
not constitute an inertia anchor.

Every subsequent interview, evidence item, and synthesis step will be evaluated against
this anchor.

---

STEP 1 -- SUBJECT ROSTER (required sequence)

Design at least two subjects. The first subject must be an INCUMBENT USER of the
Inertia Anchor named in Step 0. At least one subsequent subject must hold a meaningfully
different relationship to that anchor.

Subject 1 -- THE INCUMBENT (required first)
This person is a current practitioner of the Inertia Anchor -- a power user, advocate,
or owner of the current solution. They are not defined by skepticism; they are defined
by having an established practice. Their investment in the current approach is what makes
their evidence meaningful: they represent the realistic switching cost.

Subsequent subjects -- design at least one of the following:
- THE FRICTION HOLDER: someone who experiences a specific limitation of the Inertia
  Anchor and is actively aware of the gap
- THE EVALUATOR: someone who assesses options against organizational or operational
  criteria without deep investment in either the current or proposed direction
- THE SKEPTICAL ADOPTER: someone who is attracted to the new direction but has unresolved
  concerns about whether it can replace what they currently rely on

For each subject, write a Subject Card:
- Role and domain
- Prior knowledge: what they have seen, done, or worked with (positive declaration)
- Blind spots: what they have NOT seen or NOT done -- a separate explicit field
- Disposition: champion / skeptic / neutral / resistant / curious -- one declared value
- Incumbent Designation: INCUMBENT or NON-INCUMBENT
  - INCUMBENT subjects must explicitly state their relationship to the Inertia Anchor
    declared in Step 0 (e.g., "owns and maintains the process named in Step 0,
    has used it for 4 years, has customized it for team needs")
- Primary concern: the one thing that most shapes their evaluation

---

STEP 2 -- INTERVIEWS (incumbent first)

For each subject, two phases:

PART A -- CURRENT REALITY
Ask about the subject's relationship to the Inertia Anchor (for incumbents) or to the
problem space the anchor addresses (for others). No hypothesis framing. Minimum 3
questions. For the INCUMBENT: go deep on what works, what costs them, what they have
tried to fix, what they have learned to live with.

PART B -- HYPOTHESIS PROBE
Each question anchors to a specific Part A answer. Name the anchor explicitly. Do not
genericize to the hypothesis without the anchor. 2-3 questions per subject.

Write every answer in the subject's voice. The INCUMBENT and the FRICTION HOLDER will
describe the same limitation differently -- that vocabulary difference is evidence.

---

STEP 3 -- EXTRACTION (per subject)

For each extracted evidence item:
- [Type]: RISK / PREFERENCE / CONSTRAINT / VALIDATION / INVALIDATION / SIGNAL
- [Strength]: STRONG / MODERATE / WEAK
- [Rationale]: one sentence naming source type, circumstance, or specificity
- [Epistemic Standing]: GROUNDED (direct experience with the specific thing being
  evaluated) / CONDITIONAL (declared blind spot affects this item -- name it) /
  INFERRED (stance not directly stated)
- [Inertia Relevance]: INERTIA (this item measures switching cost, friction, or
  resistance relative to the Inertia Anchor) / ADOPTION (this item measures openness,
  fit, or pull toward the new direction) / NEUTRAL (neither directly)
- Flag one item per subject as SURPRISING MOMENT or CONFIRMING MOMENT

---

STEP 4 -- SYNTHESIS

1. INERTIA / ADOPTION PARTITION
   Using the [Inertia Relevance] tags from extraction, compile two named lists:

   INERTIA SIGNALS -- all items tagged INERTIA across all subjects. These represent
   the aggregate weight of the status quo: switching cost, workflow disruption, habit
   lock-in, resistance to change from the declared Inertia Anchor.

   ADOPTION SIGNALS -- all items tagged ADOPTION across all subjects. These represent
   the aggregate pull toward the new direction: openness, fit, willingness, enthusiasm.

   State the adoption delta: is the inertia load dominant, balanced with adoption pull,
   or marginal? Name the two or three specific items with the greatest weight on each
   side.

2. INERTIA ACCOUNTING
   Return to the INCUMBENT's extracted items specifically. What would it actually take
   to move them? Is the friction fatal to the hypothesis, solvable by design, or
   irrelevant given what the other subjects revealed?

3. CONVERGENCE AND CONTRADICTION
   Where do subjects agree despite different starting positions? Where do subjects
   diverge on the same limitation -- name the specific items and subjects.

4. EPISTEMIC RE-WEIGHTING
   Apply each subject's declared blind spots to their extracted evidence. Flag CONDITIONAL
   items and state what would resolve them. Credit GROUNDED items with full standing.
   The INCUMBENT's objection about the new direction (which they may not have seen) is
   CONDITIONAL; the same objection from a subject who has piloted the alternative is
   GROUNDED. Name the difference.

5. DISPOSITION ARC
   Name what changed or held across the subject sequence. Did the arc reveal any pathway
   under which the incumbent's inertia would weaken? Or did the inertia barrier hold?

---

STEP 5 -- NET VERDICT

One or two sentences. Does the aggregate evidence -- including the full inertia load --
SUPPORT, CHALLENGE, CONTRADICT, or leave INCONCLUSIVE the hypothesis?

Name specifically whether the Inertia Anchor represents a fatal barrier, a solvable
switching cost, or an objection neutralized by other subjects' evidence. A verdict
that ignores the adoption delta from Step 4 does not close the investigation.
```

---

## V-05 -- Coaching Register + Verdict-Frame-First + Incumbent Hygiene

**Axis**: Phrasing register (coaching voice) combined with verdict-frame-first
**Hypothesis**: In a coaching register, the incumbent identification and inertia baseline emerge
from a natural preflight question ("before you design anyone, tell me: who is already doing
something in this space, and what are they using?") rather than from a structural requirement.
The partition emerges from a coaching checkpoint before synthesis ("before you read across the
evidence, separate what you heard about the cost of changing from what you heard about the pull
toward something new"). These are self-directed investigation steps, not compliance requirements.
The coaching frame makes C-21/C-22 feel like obvious decision hygiene -- natural next moves for
someone who wants to produce a useful verdict rather than an interesting transcript.

```
Before you interview anyone, answer two questions.

First: What would it take to be convinced?

State the hypothesis you are investigating. Then write one to two sentences for each:
- What would SUPPORT this hypothesis look like if you heard it in an interview?
- What would CHALLENGE it?
- What would CONTRADICT it?
- What would leave the evidence INCONCLUSIVE?

This is your verdict frame. Every subject you design, every question you ask, and every
evidence item you extract will be evaluated against it.

Second: Who is already doing something in this space?

Before you design a single interview subject, name the current practice, tool, or workflow
your hypothesis would displace or improve upon. Be specific: what is it called, who uses it,
and what makes it sticky? If you cannot name it, your hypothesis may be more theoretical
than you realize. Name it here -- this is your inertia anchor, and it shapes everything
that follows.

---

Now design your subjects.

You need at least two. Your first subject should be someone who is already invested in
the current practice you just named -- a user, owner, or advocate of it. Not a straw-man
objector: someone who has the current approach working for them, or at least has adapted
to it. Their relationship to the status quo is the evidence baseline. Everyone else gets
measured against it.

Your second subject should give you a genuinely different angle -- different friction,
different role, different relationship to the problem. If your second subject is just a
quieter version of your first, redesign them.

For each subject, write their card before you write a single question. The card has
six parts:

1. Who they are -- their role, domain, and what they have been doing in this space

2. What they know -- their prior experience and relevant context; things they have
   actually seen or done, not things you wish they knew

3. What they do not know -- their blind spots: what they have not encountered, not
   used, not been exposed to. Be honest here. Blind spots are evidence-weighting
   information, not weaknesses.

4. How they are disposed -- champion, skeptic, neutral, resistant, or curious.
   Pick one and declare it. Neutral is valid but must be a choice, not a default.

5. What they care about most -- their primary decision criterion, not their job description

6. Their relationship to the inertia anchor -- are they an INCUMBENT (invested in the
   current practice you named above, dependent on it, shaped by it) or NON-INCUMBENT?
   If INCUMBENT: describe their specific relationship to that practice in one or two
   sentences. What specifically do they use, own, or depend on? This is the ground state
   your hypothesis would ask them to leave behind.

Do not write a single transcript line until all subject cards are complete.

---

Now run the interviews. Start with your incumbent subject.

For each subject, start in their current reality. Ask about what they are doing today,
what is working, what is not, what they have tried to fix. For your incumbent: go deep
on the current practice -- what makes it work for them, what the rough edges are, what
they have adapted around. Do not mention your hypothesis yet. Three to four questions
in their current reality.

After those questions, transition to the hypothesis -- but anchor the transition to
something the subject just said. Connect it explicitly: "You mentioned [X] -- given
that, here is what I want to ask you..." If you cannot find a Part A answer to anchor
to, your Part A questions did not establish enough of their reality. Add a question.

Write every answer in the subject's voice. If you catch yourself writing an answer that
could have come from any of your subjects -- same vocabulary, same concerns, same framing
-- stop and rewrite it from this subject's specific background and relationship to the
inertia anchor.

---

After each transcript, extract the evidence.

For each item:
- Tag its type: risk, preference, constraint, validation, invalidation, or signal
- Rate its strength: strong, moderate, or weak
- Justify the rating in one sentence: why does this item earn that strength? Name the
  source type, the circumstance, or what makes it specific
- Note whether this item is grounded (the subject has direct relevant experience) or
  conditional (their declared blind spot affects how much weight this item carries)
- Note whether this item speaks to INERTIA (cost of changing, friction, lock-in,
  disruption to current practice) or ADOPTION (openness, fit, pull toward the new
  direction). One label per item.

Mark one item per subject as a SURPRISING MOMENT or CONFIRMING MOMENT.

---

Before you synthesize, do one thing first.

Take all the evidence you have extracted and separate it into two piles:

INERTIA pile -- everything that measures the cost or friction of leaving the current
practice behind. Switching cost. Workflow disruption. Habit lock-in. Resistance.
Anything that says "the current approach has gravity."

ADOPTION pile -- everything that measures openness or pull toward the new direction.
Fit. Willingness. Enthusiasm. Anything that says "there is a reason to move."

State what the two piles say, in aggregate. Is the inertia load dominant, balanced, or
marginal relative to the adoption evidence? This is your adoption delta -- the signal
your multi-subject investigation is designed to surface. If you skip this step and go
straight to synthesis, you will produce an interesting summary but not a useful verdict.

---

Now synthesize.

Look at what these interviews say together. You are not summarizing -- you are comparing.
Find:
- Where subjects converge, even from different starting positions
- Where they contradict each other -- name the specific items and which subjects hold
  them. Do not average contradictions away.
- What the arc of dispositions revealed: did your incumbent surface something the other
  subjects underweighted? Did another subject reveal a condition under which the
  incumbent's inertia would weaken?

Then revisit your evidence items against each subject's declared blind spots. The CONDITIONAL
items: what are they conditional on? Could that condition be resolved by design, by
demonstration, or by new information? Show that the blind-spot declarations changed how
you read the evidence.

Go back to your verdict frame. For each major evidence item, place it: does it land in
SUPPORT, CHALLENGE, CONTRADICT, or INCONCLUSIVE? Evidence from a subject with direct
experience in the specific failure mode outweighs evidence from a subject who is
reasoning about it theoretically. Say so.

---

Close with your verdict.

One or two sentences. Declare whether the aggregate evidence supports, challenges,
contradicts, or is genuinely inconclusive about your hypothesis.

Address the inertia anchor directly: is the inertia load fatal to the hypothesis, a
solvable switching cost, or an objection that the adoption evidence neutralizes? A
verdict that does not address what would have to change for the incumbent to move is
not a decision-ready output.

Reference your verdict frame from the opening: did the interviews answer the question
you started with, or did they reveal that you were asking the wrong question?
```
