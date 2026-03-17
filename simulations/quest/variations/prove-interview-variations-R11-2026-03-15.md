## prove-interview Variations — Round 11

---

## V-01
**Variation axis:** Role sequence — Skeptic-first cascade with explicit objection lifecycle tracking
**Hypothesis:** Running the skeptic first creates a durable objection surface that subsequent subjects must engage, making the cross-interview synthesis structurally richer than advocate-first ordering.

```markdown
# prove-interview — Skeptic-First Cascade

You are running a simulated stakeholder interview investigation for the topic: **{{topic}}**

Interview subjects appear in skeptic-first order: the challenger runs first to establish the
objection surface; the neutral subject second to provide an undistorted baseline; the
advocate last, having implicitly absorbed what the skeptic established. This ordering
is deliberate and must be named in a sequence-justification note before Phase 0 begins.

---

## SEQUENCE JUSTIFICATION

Before any setup work begins, write a one-paragraph note naming:
- Which subject holds the skeptic disposition, which holds the neutral, which holds the
  advocate disposition
- Why skeptic-first ordering serves this investigation (objection surface before validation,
  cascade tracking, avoiding advocate priming)
- What the expected objection lifecycle is: predict whether the skeptic's core objection
  will persist, transform, or be resolved by the time the final subject closes

---

## PHASE 0 — PRE-INTERVIEW STRUCTURE

### 0-A: MOMENT-LABEL DECISION TAXONOMY

Declare the complete three-label system before any subject card is written.

| Label | Decision Rule |
|-------|---------------|
| SURPRISING | Prior expectation from the register is violated — the subject said something
the interviewer explicitly did not predict |
| CONFIRMING | Prior expectation from the register is upheld — the subject said exactly or
directionally what the register predicted |
| INCONCLUSIVE | A signal is present but directionally ambiguous — cannot be assigned to
either prior-expectation category without additional evidence |

This taxonomy governs every moment label in every interview transcript. All three rules
are declared regardless of whether all three labels are exercised.

---

### 0-B: SUBJECT CARDS

Write one subject card per interview subject. Minimum three subjects (skeptic, neutral, advocate).
Cards appear in the declared interview order (skeptic first).

Each card must contain:
- **Role / Title / Function** — specific enough that vocabulary can be predicted
- **Prior Knowledge Map** — what they know, what they don't know, what they care about
  (3 items minimum per dimension)
- **Disposition** — skeptic / neutral / advocate, with a one-sentence rationale
- **Vocabulary Signature** — 2–3 role-specific terms distinctive enough to spot-check
  answers against (generic descriptors like "uses technical language" fail; must name
  actual terms)
- **Evidential Function** — what this subject's position in the investigation *does* for
  the evidence structure (e.g., "establishes the objection surface that subsequent
  subjects are measured against"; "feasibility probe for implementation realities")

**Subject card template (instantiate for each subject):**
```
### Subject N — [Name/Role]
**Role:** [title or function]
**Disposition:** [skeptic / neutral / advocate] — [rationale sentence]
**Prior Knowledge Map:**
  - Knows: [item], [item], [item]
  - Does not know: [item], [item]
  - Cares about: [item], [item]
**Vocabulary Signature:** [term-1], [term-2], [term-3]
**Evidential Function:** [structural contribution to the evidence chain]
```

SUBJECT CARD GATE: [ ] Three subject cards present
[ ] Each card has role, prior knowledge map, disposition, vocabulary signature, evidential function
[ ] Ordering matches declared sequence (skeptic first)

---

### 0-C: EXPECTATION REGISTER

For each subject, declare what the interviewer expects them to say and why — before any
transcript begins. The register is the structural source for the "expected:" slot in every
SURPRISING and CONFIRMING label.

| Subject | Expected Position | Expected Concern | Expected Vocabulary | Basis for Expectation |
|---------|-------------------|-----------------|--------------------|-----------------------|
| [Skeptic name] | | | | |
| [Neutral name] | | | | |
| [Advocate name] | | | | |

Populate every cell. Basis for Expectation names why this prediction was made (role logic,
domain knowledge, declared prior-knowledge map).

EXPECTATION REGISTER GATE: [ ] All subjects have entries
[ ] Expected Vocabulary column references the vocabulary signature from the subject card
[ ] Basis column is populated for every row

---

### 0-D: SUBJECT FRAMEWORK

For **{{topic}}**, declare the analytical framework used to evaluate evidence across subjects.
This framework must have discrete named dimensions (minimum 3) that evidence items can be
mapped to in the extraction phase.

Example frameworks: adoption readiness model (awareness / motivation / capability);
feasibility grid (technical / timeline / resource); risk register (probability / impact / owner).

Name the framework and list its dimensions explicitly. These dimensions become a required
column in the evidence table.

**Framework name:** ______
**Dimensions:**
- D1: ______
- D2: ______
- D3: ______

FRAMEWORK GATE: [ ] Framework named
[ ] At least 3 discrete dimensions declared with names
[ ] Dimensions are distinct and non-overlapping

---

### PRE-INTERVIEW MASTER GATE

Before Phase 1 begins, confirm all setup prerequisites are collectively satisfied:

**PRE-INTERVIEW MASTER GATE:**
[ ] Sequence Justification (0-Seq): written, names skeptic/neutral/advocate and predicted objection lifecycle
[ ] Moment-Label Decision Taxonomy (0-A): all three labels declared with decision rules
[ ] Subject Cards (0-B): GATE passed — three cards present, all fields complete
[ ] Expectation Register (0-C): GATE passed — all subjects populated, basis column complete
[ ] Subject Framework (0-D): GATE passed — framework named, dimensions declared

Phase 1 begins only when all five items above are confirmed.

---

## PHASE 1 — INTERVIEWS (Run in Skeptic-First Order)

For each subject, run the following structure in sequence. Do not begin the next subject
until the current subject's extraction phase is complete.

### Interview Structure per Subject

**[Subject N] — [Role]**

*Vocabulary check: declared terms for this subject are [term-1], [term-2], [term-3].
These terms must appear naturally in this subject's answers.*

**Opening question:** Anchor to declared role and prior-knowledge map. Do not ask a
question whose answer would be identical regardless of who was asked.

**[Q1]** [Question text]
> **[Subject's answer — written in declared persona voice, vocabulary signature terms
> present naturally. Answer reflects what this persona knows and does not know.
> Generic AI-voice answers fail.]]**

**Follow-up:** Each follow-up must cite a specific moment from the preceding answer.
Format: `Triggered by: "[exact phrase from prior answer]"` — then the question.

`Triggered by: "[exact phrase]"`
**[Q2]** [Follow-up question]
> **[Subject's answer]**

*(Continue for 3–5 questions total, each follow-up citing its trigger)*

---

**Extraction — [Subject N]**

*C-22 prerequisite confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE (Vocabulary
Signatures item). C-13 prerequisite confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(Expectation Register item).*

| Evidence Item | Signal Type | Strength | Rationale | Basis | Experience-Proximity | Framework Dimension |
|---------------|-------------|----------|-----------|-------|---------------------|---------------------|
| [claim] | [adoption risk / feasibility concern / requirement gap / scope signal / constraint] | strong / moderate / weak | [why this rating] | verbatim / inferred / corroborated | GROUNDED / CONDITIONAL / INFERRED | [D1 / D2 / D3] |

*Experience-proximity key: GROUNDED = subject has direct operational experience of the
claim; CONDITIONAL = subject is adjacent but not direct; INFERRED = subject is reasoning
about a situation they have not encountered.*

*Origin-of-claim key: verbatim = directly quoted from transcript; inferred = implied but
not stated; corroborated = consistent signal across two or more subjects.*

**Moment labels:**

`SURPRISING (expected: [Expectation Register → Subject N row, Expected Position / Expected Concern], got: [what emerged])`
or
`CONFIRMING (validates: [Expectation Register → Subject N row, Expected Position])`
or
`INCONCLUSIVE: [signal present, directionally ambiguous, reason]`

*(List all labeled moments. At least one label per subject.)*

**Vocabulary check:** [Confirm which declared terms appeared in transcript, or note gap]

PHASE 1 SUBJECT GATE — [Subject N]:
[ ] Questions anchored to declared role and prior-knowledge map
[ ] At least one follow-up with cited trigger phrase
[ ] Evidence table populated with all 7 columns
[ ] At least one moment label with Expectation Register citation
[ ] Vocabulary signature terms exercised in transcript

---

*(Repeat full Phase 1 structure for each subject in sequence)*

---

## PHASE 2 — CROSS-INTERVIEW SYNTHESIS

*C-36 confirmed: Framework dimensions column was present in all evidence tables.
C-37 confirmed: Moment-label citations accommodated both Expectation Register and
Framework Dimension as named sources.*

**SYNTHESIS ARTIFACT — {{topic}} Interview Round**

Deliver as a named, schema-instantiated table:

| Subject | Framework Dimension | Testimony Direction | Key Evidence Item | Implication |
|---------|---------------------|---------------------|-------------------|-------------|
| [Skeptic] | [D1] | supports / challenges / inconclusive | [specific item] | [downstream meaning] |
| [Neutral] | [D1] | | | |
| [Advocate] | [D1] | | | |
| [Skeptic] | [D2] | | | |
| ... | | | | |

Populate all rows. Every subject appears at least once per framework dimension.

**Objection Lifecycle:**
State explicitly whether the skeptic's initial objection (declared in Sequence Justification)
*persisted*, *transformed*, or *was resolved* by the time the advocate's interview closed.
Cite the specific evidence items that support this reading.

**Convergence / Contradiction summary:** Name at least one cross-subject pattern and one
cross-subject contradiction by framework dimension.

PHASE 2 GATE:
[ ] Synthesis artifact table present with all 5 columns
[ ] All subjects appear at each framework dimension
[ ] Objection lifecycle statement present with evidence citations
[ ] At least one convergence and one contradiction named by dimension

---

## PHASE 3 — META-ANNOTATIONS

**Simulation fidelity note:** Name at least one specific basis for grounded claims (documented
persona knowledge, domain context, declared prior-knowledge map) and at least one point where
the simulation constructed plausibility rather than drawing from documented evidence.

**Voice divergence acknowledgment:** Name at least one concrete contrast in how two subjects
were made to sound different — citing a specific vocabulary choice, framing preference, or
concern priority (e.g., "the skeptic defaulted to unit-cost framing while the advocate used
adoption-velocity language").
```

---

## V-02
**Variation axis:** Output format — Schema-dominant; tables enforce structure throughout every phase
**Hypothesis:** Making every phase schema-bound (tables with named columns) rather than template-embedded makes the structural contract more auditable and harder to satisfy partially.

```markdown
# prove-interview — Schema-Dominant Format

You are running a simulated stakeholder interview investigation for the topic: **{{topic}}**

Every phase of this output is schema-bound. Tables are the primary format for setup,
extraction, and synthesis. Prose appears only for interview transcripts and brief
phase-transition notes. All table schemas are declared at document head and must be
instantiated without omitted columns.

---

## DOCUMENT-HEAD FORMAT CONTRACT

The following schemas govern this output. Every table of the named type must use exactly
these columns — no omissions, no column reordering without annotation.

| Table Type | Required Columns |
|------------|-----------------|
| Subject Card | Subject / Role / Disposition / Prior-Knows / Prior-Blind-Spots / Cares-About / Vocabulary-Signature / Evidential-Function |
| Expectation Register | Subject / Expected-Position / Expected-Concern / Expected-Vocabulary / Basis |
| Framework Dimensions | ID / Dimension-Name / Description / What-Evidence-Maps-Here |
| Evidence Extraction | Item / Signal-Type / Strength / Strength-Rationale / Origin-of-Claim / Experience-Proximity / Framework-Dimension-ID |
| Moment Labels | Subject / Label / Expected (from) / Got / Register-Row / Register-Column |
| Synthesis Artifact | Subject / Framework-Dimension-ID / Testimony-Direction / Key-Item | Implication |

Schemas instantiated per C-29: a populated example row appears in the first table of each type.

---

## PHASE 0 — PRE-INTERVIEW STRUCTURE

### 0-A: Moment-Label Decision Taxonomy

| Label | Condition for Application | Disqualifying Condition |
|-------|--------------------------|------------------------|
| SURPRISING | Prior expectation from register is violated | Signal is directionally ambiguous |
| CONFIRMING | Prior expectation from register is upheld | Signal differs from expectation in any direction |
| INCONCLUSIVE | Signal present but directionally ambiguous | Signal can be cleanly assigned to prior expectation |

All three rules declared. Govern all moment labels in all transcripts.

---

### 0-B: Subject Cards

*(Using Subject Card schema from Document-Head Format Contract. Example row instantiated first.)*

| Subject | Role | Disposition | Prior-Knows | Prior-Blind-Spots | Cares-About | Vocabulary-Signature | Evidential-Function |
|---------|------|-------------|-------------|-------------------|-------------|---------------------|---------------------|
| **[Example]** | **Engineering Lead** | **skeptic** | **existing pipeline costs, latency reqs** | **end-user adoption patterns** | **system reliability** | **throughput, SLA, blast radius** | **surfaces implementation constraints that adoption estimates must account for** |
| [Subject 1] | | | | | | | |
| [Subject 2] | | | | | | | |
| [Subject 3] | | | | | | | |

Minimum three subjects. All cells populated. Disposition options: skeptic / neutral / advocate.
Vocabulary-Signature: 2–3 specific terms, not general descriptors.

SUBJECT CARD GATE: [ ] 3+ rows present
[ ] All columns populated, no blank cells
[ ] Vocabulary-Signature contains named terms (not descriptors)

---

### 0-C: Expectation Register

*(Using Expectation Register schema from Document-Head Format Contract.)*

| Subject | Expected-Position | Expected-Concern | Expected-Vocabulary | Basis |
|---------|-------------------|-----------------|--------------------|-----------------------|
| **[Example]** | **will challenge migration cost** | **timeline slippage risk** | **"rollback plan," "blast radius"** | **declared prior-knowledge: knows existing pipeline costs** |
| [Subject 1] | | | | |
| [Subject 2] | | | | |
| [Subject 3] | | | | |

Expected-Vocabulary references terms from the subject's Vocabulary-Signature column.

EXPECTATION REGISTER GATE: [ ] All subjects have rows
[ ] Expected-Vocabulary references vocabulary signatures
[ ] Basis column populated for all rows

---

### 0-D: Subject Framework

*(Using Framework Dimensions schema from Document-Head Format Contract.)*

| ID | Dimension-Name | Description | What-Evidence-Maps-Here |
|----|----------------|-------------|------------------------|
| **D1** | **[example: Adoption Readiness]** | **whether the feature can be adopted without friction** | **concerns about onboarding, training, change management** |
| D2 | | | |
| D3 | | | |

Minimum 3 dimensions. Dimensions are distinct, non-overlapping.

FRAMEWORK GATE: [ ] 3+ rows present
[ ] All columns populated
[ ] Dimensions are non-overlapping

---

### SEQUENCE JUSTIFICATION

| Item | Value |
|------|-------|
| Interview order | [Subject 1] → [Subject 2] → [Subject 3] |
| Ordering rationale | [one sentence naming why this sequence serves the investigation] |
| Expected objection lifecycle | [predict: persist / transform / resolve — one sentence] |

---

### PRE-INTERVIEW MASTER GATE

| Prerequisite | Section | Status |
|-------------|---------|--------|
| Moment-Label Decision Taxonomy | 0-A | GATE PASSED / FAIL |
| Subject Cards | 0-B | GATE PASSED / FAIL |
| Expectation Register | 0-C | GATE PASSED / FAIL |
| Subject Framework | 0-D | GATE PASSED / FAIL |
| Sequence Justification | 0-Seq | PRESENT / ABSENT |

Phase 1 begins only when all rows show GATE PASSED or PRESENT.

---

## PHASE 1 — INTERVIEWS

For each subject, run the full structure. Transcripts are the only prose-primary phase.
Extraction returns to schema.

### Subject N — [Role] ([Disposition])

*Vocabulary check: declared terms are [term-1], [term-2], [term-3]. At least one must
appear naturally in this subject's answers.*

**Q1:** [Question anchored to declared role and prior-knowledge map]
> [Answer in persona voice. Vocabulary signature terms present naturally. Answer reflects
> declared Prior-Knows and Cares-About — generic voice fails.]

**Q2 (follow-up):**
`Triggered by: "[exact phrase from Q1 answer]"`
[Follow-up question]
> [Answer]

**Q3 (follow-up):**
`Triggered by: "[exact phrase from Q2 answer]"`
[Follow-up question]
> [Answer]

*(Continue 3–5 questions. Each follow-up must cite its trigger phrase.)*

---

**Extraction — Subject N**

*C-22 FULLY SATISFIED (PRE-INTERVIEW MASTER GATE, Subject Cards row). C-13 FULLY
SATISFIED (PRE-INTERVIEW MASTER GATE, Expectation Register row). Proceeding to
extraction with dual-source citation available.*

*(Using Evidence Extraction schema from Document-Head Format Contract.)*

| Item | Signal-Type | Strength | Strength-Rationale | Origin-of-Claim | Experience-Proximity | Framework-Dimension-ID |
|------|-------------|----------|-------------------|-----------------|---------------------|----------------------|
| **[Example]** | **adoption risk** | **moderate** | **stated as concern, not observed in practice** | **inferred** | **CONDITIONAL** | **D1** |
| [Item 1] | | | | | | |
| [Item 2] | | | | | | |

Signal-Type options: adoption risk / feasibility concern / requirement gap / scope signal / constraint / validation
Strength options: strong / moderate / weak (rationale sentence required)
Origin-of-Claim: verbatim / inferred / corroborated
Experience-Proximity: GROUNDED (direct operational experience) / CONDITIONAL (adjacent) / INFERRED (reasoning from no direct experience)

*(Using Moment Labels schema from Document-Head Format Contract.)*

| Subject | Label | Expected (from) | Got | Register-Row | Register-Column |
|---------|-------|-----------------|-----|--------------|-----------------|
| **[Example]** | **SURPRISING** | **migration cost objection** | **raised adoption fatigue instead** | **Subject 1** | **Expected-Position** |
| [Subject N] | [SURPRISING / CONFIRMING / INCONCLUSIVE] | [what was expected] | [what emerged] | [register row] | [register column] |

At least one labeled moment per subject. INCONCLUSIVE is used when applicable or an
explicit note states all moments were unambiguously one or the other.

**Vocabulary check:**
| Term | Appeared in transcript? | Where |
|------|------------------------|-------|
| [term-1] | yes / no | [quote or "absent"] |
| [term-2] | yes / no | |
| [term-3] | yes / no | |

SUBJECT N GATE:
[ ] Transcript: 3+ questions, all follow-ups with trigger phrases
[ ] Evidence table: all 7 columns populated, no blank cells
[ ] Moment labels table: at least one row, register citation present
[ ] Vocabulary check: at least one declared term confirmed present

---

*(Repeat Phase 1 structure for all subjects)*

---

## PHASE 2 — CROSS-INTERVIEW SYNTHESIS

*C-36 confirmed (PHASE 1 GATE passed for all subjects — Framework-Dimension-ID column
present in all extraction tables). C-37 confirmed (Moment Labels schema accommodates
both Expectation Register and Framework Dimension as named sources).*

**SYNTHESIS ARTIFACT — {{topic}}**

*(Using Synthesis Artifact schema from Document-Head Format Contract.)*

| Subject | Framework-Dimension-ID | Testimony-Direction | Key-Item | Implication |
|---------|------------------------|---------------------|----------|-------------|
| **[Example]** | **D1** | **challenges** | **"adoption fatigue with third migration in 18 months"** | **phased rollout required before full deployment** |
| [Subject 1] | D1 | supports / challenges / inconclusive | | |
| [Subject 2] | D1 | | | |
| [Subject 3] | D1 | | | |
| [Subject 1] | D2 | | | |
| ... | | | | |

Populate all rows: every subject × every framework dimension.

| Synthesis Finding | Type | Supporting Evidence Items |
|------------------|------|--------------------------|
| [pattern or convergence] | convergence / contradiction | [item refs] |
| [pattern or contradiction] | | |

**Objection Lifecycle:**
| Initial Objection | Source Subject | Final Status | Evidence |
|-------------------|---------------|--------------|----------|
| [stated in Sequence Justification] | [Skeptic name] | persisted / transformed / resolved | [cite items] |

PHASE 2 GATE:
[ ] Synthesis artifact table: all 5 columns, all subjects × all dimensions populated
[ ] Synthesis findings table: at least one convergence and one contradiction
[ ] Objection lifecycle table: present with evidence citations

---

## PHASE 3 — META-ANNOTATIONS

| Annotation Type | Content |
|----------------|---------|
| Simulation fidelity | [name one grounded basis; name one constructed-plausibility point] |
| Voice divergence | [name one concrete contrast between two subjects: specific vocabulary choice, framing, or concern priority] |
```

---

## V-03
**Variation axis:** Phrasing register — Conversational and directive; instructions address the author as "you" and explain the *purpose* of each phase rather than issuing structural mandates
**Hypothesis:** A conversational register reduces the cognitive load of parsing the format, letting the author focus on persona quality, but risks under-specifying the structural requirements that produce rubric-compliant outputs.

```markdown
# prove-interview — Conversational Directive

You're going to run a simulated interview investigation for: **{{topic}}**

Think of this as three things in sequence: getting ready, running the interviews, and then
making sense of what you learned. The getting-ready part is actually the most important —
if you skip it or rush it, the interviews won't be grounded and the evidence will feel
made up. Take the setup seriously.

Here's how to move through it.

---

## GETTING READY (Phase 0)

Before you write a single interview question, do four things.

**First: decide who your subjects are and what order you'll interview them.**

Pick at least three people. Give each one a real role — not "a stakeholder" or "a user"
but something specific like "engineering lead on the existing pipeline" or "head of
adoption for enterprise accounts." Then pick their disposition: is this person skeptical
about the feature, neutral and curious, or an advocate?

Once you've picked them, decide the order and say why. A common choice: put the skeptic
first so their objection establishes a surface that later subjects can confirm or dissolve.
Write a sentence explaining your choice.

Also predict the fate of the skeptic's objection: will it persist across all three
interviews? Will it transform into something different? Will the advocate's answers make
it go away? Write that prediction down — you'll close it out at the end.

---

**Second: write subject cards for each person.**

For each subject, you need five things: their role, what they already know about the
problem space (and what they don't), what they care most about, two or three specific
words or phrases that this kind of person actually uses (not "uses technical language" —
actual terms like "throughput" or "CAC" or "rollback plan"), and a sentence about what
their presence in this investigation *does for you* structurally (what would you miss if
they weren't here?).

That last one is easy to skip but worth writing. "The skeptic challenges assumptions" is
not what we're after — we want something like "they give us the constraint surface that
the adoption estimate has to be tested against." That's an evidential function.

---

**Third: write down what you expect each person to say before they say it.**

This is your expectation register. For each subject, predict: what position will they take
on the feature? What concern will they raise? Which of their vocabulary terms will show up?
And why do you think that — what about their role or prior knowledge leads you to this prediction?

If you can't fill this in, you don't know your subjects well enough yet. Go back and sharpen
the subject cards.

---

**Fourth: declare a small analytical framework.**

The interviews will generate a lot of content. You need something to sort it against.
Pick a framework with three or four named dimensions — things like "adoption readiness /
technical feasibility / organizational fit" or "probability / impact / reversibility."
Give each dimension an ID (D1, D2, D3) so you can reference them later without
writing the full name every time.

These dimensions matter because every evidence item you extract will need to map to one
of them. If you can't map it, either the evidence item isn't real evidence or your
framework is missing a dimension.

---

**Before you start the interviews, do a quick check:**

Go through this list and confirm each item is done:
- [ ] Sequence justification written (order + rationale + objection-fate prediction)
- [ ] Three-label taxonomy declared (SURPRISING / CONFIRMING / INCONCLUSIVE — all three,
  with decision rules for each, even if you think INCONCLUSIVE won't come up)
- [ ] Subject cards complete for all subjects (role, knows/doesn't know, cares about,
  vocabulary signature, evidential function)
- [ ] Expectation register complete (position, concern, vocabulary, basis for each subject)
- [ ] Framework declared (3+ named dimensions with IDs)

Don't start the interviews until everything is checked. This isn't bureaucratic — each of
these feeds directly into what makes an interview simulation credible rather than generic.

---

## THE INTERVIEWS (Phase 1)

Run one subject at a time, start to finish, before moving to the next.

**Writing the transcript**

Start with a question that could only be asked of this person — something that depends on
what they know and care about. If the question would make equal sense asked of your other
subjects, rewrite it.

After each answer, write a follow-up. But don't just ask the next question on your list —
actually respond to what the subject just said. Pick a specific phrase from their answer
and make your follow-up visibly triggered by it. Write: `Triggered by: "[exact phrase]"` —
then the question. This keeps the interview feeling like a real conversation rather than
a survey.

Run three to five questions per subject.

**The most important thing: make them sound different.**

The skeptic shouldn't sound like the advocate with a different opinion. They should use
different words, reach for different analogies, focus on different aspects of the same
question. Check your vocabulary signatures — those terms should show up naturally in
their answers, not crammed in, but there.

---

**After each transcript: extract the evidence**

Don't leave the evidence implicit in the transcript. Pull it out explicitly into a table.
For each item you extract, give it:

- a **signal type** (adoption risk? feasibility concern? requirement gap? scope signal?
  constraint? validation?)
- a **strength** (strong / moderate / weak) with a sentence saying why — what makes this
  signal reliable, hedged, or ambiguous?
- an **origin-of-claim** — was this *verbatim* (you're quoting the transcript directly),
  *inferred* (you read it between the lines), or *corroborated* (the same signal came up
  in more than one subject)?
- an **experience-proximity** — is this subject speaking from *direct operational
  experience* of the claim (GROUNDED), adjacent experience (CONDITIONAL), or reasoning
  about something they haven't personally encountered (INFERRED)?
- the **framework dimension** it maps to (D1, D2, D3...)

Then label your moments. For each notable moment in the interview, write:

`SURPRISING (expected: [what the register said], got: [what actually came up])`
or
`CONFIRMING (validates: [register entry])`
or
`INCONCLUSIVE: [signal present, can't determine direction, reason]`

The "expected:" slot pulls from your expectation register — not from general intuition.
If you can't cite the register, go back and add the expectation that should have been there.

At least one labeled moment per subject. If every moment was unambiguously SURPRISING or
CONFIRMING, say so — don't silently drop INCONCLUSIVE; acknowledge it doesn't apply here.

---

## MAKING SENSE OF IT (Phase 2)

After all interviews are done, build a synthesis grid. Make it a real table, not prose —
prose synthesis is hard to audit and tends to hide contradictions.

Your grid columns: Subject / Framework Dimension / Testimony Direction (supports / challenges
/ inconclusive) / Key Evidence Item / Implication. Put every subject at every framework
dimension. Fill every cell. This forces you to face any gaps rather than skip around them.

Then close the loop on your earlier prediction: did the skeptic's objection persist,
transform, or get resolved? Cite the specific evidence items that support your answer.

Name at least one convergence (multiple subjects landed in the same place on a dimension)
and at least one contradiction (subjects pointed in opposite directions).

---

## ONE LAST THING (Phase 3)

Two short annotations to close:

**Fidelity note.** Name one place in the interviews where your claims are grounded in
documented persona knowledge or domain context you can point to — and one place where
you constructed plausibility because you didn't have that anchor. Be honest about both.
The simulation is more useful when it names its own uncertainty.

**Voice note.** Name one concrete moment where two subjects sounded genuinely different —
not "one was skeptical and one was positive" but a specific vocabulary choice or framing
pattern that separates them. This helps you check whether the persona work actually landed.
```

---

## V-04
**Variation axis (combined):** Lifecycle emphasis × Inertia framing — Explicit named checklist gate blocks throughout; status-quo competitor is a first-class structural element that every subject must address
**Hypothesis:** Treating inertia (the current approach the feature would replace) as a named structural element creates a consistent objection surface across all subjects and makes the synthesis more directly actionable for the feature decision.

```markdown
# prove-interview — Gated Phases with Inertia Threading

Topic under investigation: **{{topic}}**

## INERTIA DECLARATION

Before any setup work begins, name the inertia: the current approach, workaround, or
competing solution that **{{topic}}** would displace. Every interview subject must be
asked about their relationship to the inertia — what they currently do, how it works for
them, and what it would cost them to move away from it.

**Inertia name:** ______
**What it is:** [one sentence describing the current approach]
**Who depends on it:** [roles or teams currently relying on the inertia]
**Why it persists:** [cost, familiarity, or capability that keeps it in place]

The Inertia Declaration is a prerequisite for the Expectation Register. Expectations about
inertia attachment must appear for each subject.

---

## PHASE 0 — PRE-INTERVIEW STRUCTURE

### STEP 0-A: Moment-Label Decision Taxonomy

Declare before any subject card.

```
MOMENT-LABEL DECISION TAXONOMY
─────────────────────────────────────────────────────
SURPRISING   → Prior expectation from register is violated.
               The subject said something the interviewer did not predict.
CONFIRMING   → Prior expectation from register is upheld.
               The subject said what was predicted, directionally or exactly.
INCONCLUSIVE → Signal is present but directionally ambiguous.
               Cannot be assigned to either prior-expectation category.
─────────────────────────────────────────────────────
Governing rule: All three labels are available for all subjects.
If INCONCLUSIVE is not exercised, state explicitly why.
```

**STEP 0-A GATE:**
```
[ ] SURPRISING: decision rule declared
[ ] CONFIRMING: decision rule declared
[ ] INCONCLUSIVE: decision rule declared
[ ] Governing rule stated
```

---

### STEP 0-B: Subject Cards

Minimum three subjects. Each card declares:

```
SUBJECT CARD — [Role / Title]
─────────────────────────────────────────────────────
Role:              [title or function, specific]
Disposition:       [skeptic / neutral / advocate] — [rationale sentence]
Prior Knowledge:
  Knows:           [item 1], [item 2], [item 3]
  Does not know:   [item 1], [item 2]
  Cares about:     [item 1], [item 2]
Vocabulary Sig.:   [term-1], [term-2], [term-3]
Inertia Stance:    [how this subject currently uses the inertia; cost to change]
Evidential Fn.:    [structural contribution to the evidence chain]
─────────────────────────────────────────────────────
```

Inertia Stance is a mandatory field. It names how this subject relates to the declared
inertia — what they currently use it for and what they perceive as the switching cost.

**STEP 0-B GATE:**
```
[ ] 3+ subject cards present
[ ] Each card: role present
[ ] Each card: disposition + rationale present
[ ] Each card: prior knowledge (knows / doesn't know / cares about) present
[ ] Each card: vocabulary signature (2–3 named terms) present
[ ] Each card: Inertia Stance present and specific
[ ] Each card: evidential function present
```

---

### STEP 0-C: Expectation Register

| Subject | Expected-Position | Inertia-Attachment | Expected-Vocabulary | Basis |
|---------|-------------------|-------------------|--------------------|-----------------------|
| [S1] | | [predict: will defend / acknowledge / minimize inertia] | | |
| [S2] | | | | |
| [S3] | | | | |

Inertia-Attachment column is mandatory. Predict each subject's posture toward the current
approach before they speak.

**STEP 0-C GATE:**
```
[ ] All subjects have register entries
[ ] Inertia-Attachment column populated for all subjects
[ ] Expected-Vocabulary references vocabulary signatures
[ ] Basis column populated for all subjects
```

---

### STEP 0-D: Subject Framework

| Dimension ID | Dimension Name | Description |
|-------------|----------------|-------------|
| D1 | | |
| D2 | | |
| D3 | | |

Minimum 3 dimensions. At least one dimension must address inertia transition
(e.g., "switching cost", "migration readiness", "status-quo attachment").

**STEP 0-D GATE:**
```
[ ] 3+ dimensions declared
[ ] At least one dimension addresses inertia transition
[ ] Dimension names are distinct and non-overlapping
```

---

### STEP 0-E: Sequence Justification

| Field | Value |
|-------|-------|
| Interview order | [Subject 1] → [Subject 2] → [Subject 3] |
| Ordering rationale | [why this sequence serves the investigation] |
| Predicted objection lifecycle | [persist / transform / resolve — one sentence] |
| Inertia threading note | [how the inertia question will be raised across subjects] |

---

### PRE-INTERVIEW MASTER GATE

Confirm all setup prerequisites before Phase 1.

```
PRE-INTERVIEW MASTER GATE
─────────────────────────────────────────────────────
[ ] Inertia Declaration: present, fields complete
[ ] STEP 0-A GATE: PASSED — three-label taxonomy declared
[ ] STEP 0-B GATE: PASSED — all subject cards complete with Inertia Stance
[ ] STEP 0-C GATE: PASSED — register complete, Inertia-Attachment column populated
[ ] STEP 0-D GATE: PASSED — framework declared with inertia-transition dimension
[ ] STEP 0-E: present — sequence and inertia threading noted
─────────────────────────────────────────────────────
Phase 1 begins only when all items above are confirmed PASSED or PRESENT.
```

---

## PHASE 1 — INTERVIEWS

Run subjects in declared order. Complete each subject's extraction before starting the next.

### INTERVIEW — [Subject N: Role (Disposition)]

*C-22 FULLY SATISFIED: PRE-INTERVIEW MASTER GATE, STEP 0-B GATE.*
*C-13 FULLY SATISFIED: PRE-INTERVIEW MASTER GATE, STEP 0-C GATE.*
*Proceeding: dual-source citation available (Register and Framework).*

*Vocabulary to exercise: [term-1], [term-2], [term-3]*

**Q1:** [Question anchored to declared role, prior knowledge, and inertia stance]
> [Answer in persona voice. Vocabulary terms appear naturally. Answer reflects declared
> Inertia Stance — does this subject defend the current approach, acknowledge its limits,
> or minimize its relevance? Answer is specific to this persona, not generic.]

**Q2 (follow-up):**
`Triggered by: "[exact phrase from Q1 answer]"`
[Follow-up question — probes role-specific concern surfaced in Q1]
> [Answer]

**Inertia probe** (required once per subject):
`Triggered by: [reference to inertia-relevant content in prior answer, or introduce directly]`
What would it take for you to move away from [declared inertia]? What would you need to see?
> [Answer that reflects declared Inertia Stance and vocabulary signature]

**Q4 (follow-up):**
`Triggered by: "[exact phrase from inertia probe answer]"`
[Follow-up]
> [Answer]

---

**Extraction — [Subject N]**

| Item | Signal-Type | Strength | Strength-Rationale | Origin-of-Claim | Experience-Proximity | Framework-Dim | Inertia-Relevant? |
|------|-------------|----------|-------------------|-----------------|---------------------|---------------|------------------|
| [claim] | [type] | strong / moderate / weak | [sentence] | verbatim / inferred / corroborated | GROUNDED / CONDITIONAL / INFERRED | D1/D2/D3 | yes / no |

Inertia-Relevant column: mark "yes" for items that speak directly to the subject's
relationship with or resistance to the current approach.

**Moment labels** (source: PRE-INTERVIEW MASTER GATE–confirmed Register or Framework Dimension):

`SURPRISING (expected: [Register → Subject N, Expected-Position or Inertia-Attachment], got: [what emerged])`
`CONFIRMING (validates: [Register → Subject N, field name])`
`INCONCLUSIVE: [signal present, ambiguous direction, reason]`

**Vocabulary check:**
| Term | In transcript? | Note |
|------|---------------|------|
| [term-1] | yes / no | |
| [term-2] | yes / no | |
| [term-3] | yes / no | |

**PHASE 1 SUBJECT GATE — [Subject N]:**
```
[ ] Transcript: 4+ questions, all follow-ups cite trigger phrases
[ ] Inertia probe: present and generates substantive answer
[ ] Evidence table: all 8 columns populated (including Inertia-Relevant)
[ ] Moment labels: at least one with Register citation
[ ] Vocabulary: at least one term confirmed in transcript
```

---

*(Repeat Phase 1 for all subjects)*

---

## PHASE 2 — CROSS-INTERVIEW SYNTHESIS

*C-36 CONFIRMED: Framework-Dim column present in all Phase 1 extraction tables.*
*C-37 CONFIRMED: Moment-label template names both Register and Framework Dimension as valid sources.*

**SYNTHESIS ARTIFACT — {{topic}} × Inertia Assessment**

| Subject | Framework-Dim | Testimony-Direction | Key-Item | Inertia-Signal | Implication |
|---------|---------------|---------------------|----------|----------------|-------------|
| | D1 | supports / challenges / inconclusive | | high / medium / low attachment | |
| | D2 | | | | |
| | D3 | | | | |

Inertia-Signal column: rate each subject's attachment to the current approach at each
dimension (high / medium / low). This makes the displacement difficulty visible per dimension.

**Inertia Displacement Map:**

| Dimension | Aggregate Inertia Signal | Implication for Feature Adoption |
|-----------|------------------------|----------------------------------|
| D1 | | |
| D2 | | |
| D3 | | |

**Objection Lifecycle:**

| Skeptic's Initial Objection | Inertia-Grounded? | Final Status | Evidence Trail |
|----------------------------|------------------|--------------|----------------|
| [state from Sequence Justification] | yes / no | persisted / transformed / resolved | [cite items] |

**PHASE 2 GATE:**
```
[ ] Synthesis artifact table: all 6 columns, all subjects × all dimensions
[ ] Inertia Displacement Map: all dimensions assessed
[ ] Objection Lifecycle: final status declared with evidence citations
[ ] At least one convergence and one contradiction named across subjects
```

---

## PHASE 3 — META-ANNOTATIONS

**PHASE 3 GATE:**
```
[ ] Simulation fidelity note: names one grounded basis, one constructed-plausibility point
[ ] Voice divergence note: names one specific vocabulary or framing contrast between subjects
[ ] Inertia threading closure: confirms inertia probe appeared in every subject's transcript
```
```

---

## V-05
**Variation axis (combined):** Role sequence (influence-map order: most-informed to least-informed) × Schema-instantiated synthesis as primary output goal
**Hypothesis:** Ordering subjects from most to least operationally experienced ensures the synthesis table has a natural epistemic gradient — the first subject's testimony sets the reliability baseline and later subjects' deviations are readable as conditional signals rather than equal-weight inputs.

```markdown
# prove-interview — Influence-Map Order with Schema Synthesis

Topic: **{{topic}}**

Subjects are ordered by epistemic proximity to the feature's operational reality —
most directly experienced first, least experienced last. This creates an epistemic gradient:
the first subject's testimony is the reliability baseline; subsequent subjects' agreements
or deviations are interpretable against that baseline rather than treated as equal-weight
inputs. The gradient must be declared before Phase 0 begins and must inform synthesis
weight adjustments in Phase 2.

---

## EPISTEMIC GRADIENT DECLARATION

Before any setup, declare the influence map:

| Position | Subject Role | Proximity Basis | Expected Reliability |
|----------|-------------|-----------------|---------------------|
| 1 (most proximate) | | [why this subject has direct operational experience] | GROUNDED |
| 2 (adjacent) | | [why this subject has adjacent but not direct experience] | CONDITIONAL |
| 3 (reasoned) | | [why this subject reasons from general knowledge, not direct experience] | INFERRED |

*Experience-proximity key: GROUNDED = direct operational experience of the domain;
CONDITIONAL = works adjacent to the operational domain; INFERRED = reasoning about
a domain they have not directly operated in.*

The Epistemic Gradient governs synthesis weighting in Phase 2. Evidence from Subject 1
is the baseline; deviations from Subject 2 or 3 are named as conditional or inferred
signals, not as equal counter-evidence.

---

## PHASE 0 — PRE-INTERVIEW STRUCTURE

### 0-A: Three-Label Moment Taxonomy

```
DECISION TAXONOMY — declared before transcripts
───────────────────────────────────────────────
SURPRISING   : Prior expectation (from register) is violated.
CONFIRMING   : Prior expectation (from register) is upheld.
INCONCLUSIVE : Signal present but directionally ambiguous.
               Apply when the moment cannot be cleanly assigned to either
               prior-expectation category.
───────────────────────────────────────────────
All three labels govern all interviews.
INCONCLUSIVE is explicitly invoked when applicable, or explicitly noted as N/A
with reason when every labeled moment was unambiguously one of the other two.
```

**0-A GATE:** [ ] All three labels declared with decision rules

---

### 0-B: Subject Cards (ordered by epistemic gradient, most proximate first)

For each subject (minimum three), declare:

```
SUBJECT CARD — Position [N]: [Role]
─────────────────────────────────────────────────────
Role:             [title / function]
Epistemic Pos.:   [GROUNDED / CONDITIONAL / INFERRED] — [basis sentence]
Disposition:      [skeptic / neutral / advocate] — [rationale]
Prior Knows:      [item], [item], [item]
Prior Blind-Spots:[item], [item]
Cares About:      [item], [item]
Vocabulary Sig.:  [term-1], [term-2], [term-3]
Evidential Fn.:   [what this subject's position does for the evidence structure]
─────────────────────────────────────────────────────
```

Epistemic Position must match the Epistemic Gradient Declaration.

**0-B GATE:**
```
[ ] 3+ cards present in gradient order (GROUNDED → CONDITIONAL → INFERRED)
[ ] Each card: all fields populated
[ ] Epistemic Position consistent with gradient declaration
[ ] Vocabulary Signature: named terms (not descriptors)
```

---

### 0-C: Expectation Register

| Subject | Expected Position | Expected Concern | Expected Vocabulary | Epistemic Adjustment | Basis |
|---------|------------------|-----------------|--------------------|--------------------|-------|
| [S1, GROUNDED] | | | | This subject's claims treated as reliability baseline | |
| [S2, CONDITIONAL] | | | | Agreements with S1 treated as corroboration; deviations noted as conditional signals | |
| [S3, INFERRED] | | | | Agreements treated as weak corroboration; objections treated as conditional risk, not blocker | |

Epistemic Adjustment column is pre-populated with the gradient-derived weighting rule
for each subject. This makes the synthesis weighting structural rather than authorial.

**0-C GATE:**
```
[ ] All subjects have register rows
[ ] Epistemic Adjustment column populated for all subjects
[ ] Expected Vocabulary references vocabulary signatures
[ ] Basis column populated
```

---

### 0-D: Analytical Framework

| ID | Dimension | What Evidence Maps Here |
|----|-----------|------------------------|
| D1 | | |
| D2 | | |
| D3 | | |

Minimum 3 non-overlapping dimensions. These become columns in the synthesis artifact.

**0-D GATE:** [ ] 3+ dimensions, all distinct, Evidence-Maps-Here populated

---

### PRE-INTERVIEW MASTER GATE

```
PRE-INTERVIEW MASTER GATE
─────────────────────────────────────────────────────────────────
[ ] Epistemic Gradient Declaration: PRESENT — gradient table populated
[ ] 0-A GATE: PASSED — three-label taxonomy with decision rules
[ ] 0-B GATE: PASSED — subject cards in gradient order, all fields complete
[ ] 0-C GATE: PASSED — register complete, Epistemic Adjustment column populated
[ ] 0-D GATE: PASSED — framework 3+ dimensions
─────────────────────────────────────────────────────────────────
Phase 1 begins only when all items above are confirmed PASSED or PRESENT.
```

---

## PHASE 1 — INTERVIEWS (Run in epistemic gradient order)

### INTERVIEW — Subject [N]: [Role] ([Epistemic Pos.])

*C-22 FULLY SATISFIED (PRE-INTERVIEW MASTER GATE, 0-B GATE).*
*C-13 FULLY SATISFIED (PRE-INTERVIEW MASTER GATE, 0-C GATE).*

*Vocabulary: [term-1], [term-2], [term-3] — at least one must appear naturally.*

**Q1:** [Opening question anchored to declared role, prior knowledge, epistemic position]
> [Answer in persona voice. Subject 1 (GROUNDED) speaks from operational experience —
> specific, concrete, friction-aware. Subject 2 (CONDITIONAL) speaks with some directness
> but qualifies from adjacent vantage. Subject 3 (INFERRED) reasons carefully but lacks
> specificity. Voice must match epistemic position.]

**Q2 (follow-up):**
`Triggered by: "[exact phrase from Q1 answer]"`
[Question]
> [Answer]

**Q3 (follow-up):**
`Triggered by: "[exact phrase from Q2 answer]"`
[Question]
> [Answer]

*(3–5 questions total. All follow-ups cite trigger phrases.)*

---

**Extraction — Subject [N] ([Epistemic Pos.])**

*C-22 confirmed via PRE-INTERVIEW MASTER GATE. C-13 confirmed via PRE-INTERVIEW MASTER GATE.
Dual-source citation available: Register row + Framework dimension.*

| Item | Signal-Type | Strength | Strength-Rationale | Origin-of-Claim | Experience-Proximity | Framework-Dim |
|------|-------------|----------|-------------------|-----------------|---------------------|---------------|
| [claim] | [type] | strong/moderate/weak | [sentence] | verbatim/inferred/corroborated | [matches subject's declared epistemic position] | D1/D2/D3 |

*Note: Experience-proximity tags should match the subject's declared epistemic position
unless there is a specific reason to deviate — document any deviation.*

**Moment labels:**

`SURPRISING (expected: [Register → Subject N, Expected Position / Epistemic Adjustment],`
`            got: [what emerged])`
`CONFIRMING (validates: [Register → Subject N, Expected Position])`
`INCONCLUSIVE: [ambiguous signal, cannot assign to prior-expectation category, reason]`

**Vocabulary check:**
| Term | Present? | Location |
|------|----------|----------|
| [term-1] | yes/no | |
| [term-2] | yes/no | |
| [term-3] | yes/no | |

**SUBJECT [N] GATE:**
```
[ ] Transcript: 3+ questions, all follow-ups with trigger phrases
[ ] Voice matches declared epistemic position (GROUNDED = concrete/specific; CONDITIONAL
    = adjacent/qualified; INFERRED = reasoned/hedged)
[ ] Evidence table: all 7 columns populated
[ ] Moment labels: at least one with Register citation
[ ] Vocabulary: at least one term confirmed present
```

---

*(Repeat Phase 1 for all subjects)*

---

## PHASE 2 — SCHEMA-INSTANTIATED CROSS-INTERVIEW SYNTHESIS

The synthesis is the primary output of this investigation. It is delivered as a named
artifact with explicit schema — not prose. The schema makes the epistemic gradient's
effect on synthesis weighting auditable column by column.

*C-36 CONFIRMED (all extraction tables carry Framework-Dim column).*
*C-37 CONFIRMED (moment-label template accommodates Register and Framework Dimension).*

### SYNTHESIS ARTIFACT — {{topic}} Interview Evidence Grid

| Subject | Epistemic-Pos | Framework-Dim | Testimony-Direction | Key-Item | Synthesis-Weight | Implication |
|---------|--------------|---------------|---------------------|----------|-----------------|-------------|
| **[Example]** | **GROUNDED** | **D1** | **challenges** | **"three failed migrations in 18 months"** | **Baseline** | **adoption timeline must account for fatigue** |
| [S1, GROUNDED] | GROUNDED | D1 | supports/challenges/inconclusive | | Baseline | |
| [S2, CONDITIONAL] | CONDITIONAL | D1 | | | Corroborates baseline / Conditional signal | |
| [S3, INFERRED] | INFERRED | D1 | | | Weak corroboration / Conditional risk | |
| [S1] | GROUNDED | D2 | | | Baseline | |
| [S2] | CONDITIONAL | D2 | | | | |
| [S3] | INFERRED | D2 | | | | |
| [S1] | GROUNDED | D3 | | | Baseline | |
| [S2] | CONDITIONAL | D3 | | | | |
| [S3] | INFERRED | D3 | | | | |

*Synthesis-Weight column values:*
- *Baseline: subject is GROUNDED; this is the reliability anchor*
- *Corroborates baseline: CONDITIONAL subject agrees with GROUNDED — mild strengthening*
- *Conditional signal: CONDITIONAL subject disagrees — flag as risk, not blocker*
- *Weak corroboration: INFERRED subject agrees — adds breadth but not depth*
- *Conditional risk: INFERRED subject disagrees — monitor, not block*

### Epistemic Weight Summary

| Finding | Supporting Subjects | Highest Epistemic Source | Confidence |
|---------|--------------------|--------------------------|----|
| [cross-subject pattern] | [S1, S2] | GROUNDED | high/medium/low |
| [cross-subject contradiction] | [S2 vs S3] | CONDITIONAL | |

At least one convergence and one contradiction named, with highest-epistemic-source called out.

### Objection Lifecycle

| Initial Objection | Subject | Epistemic Pos | Final Status | Epistemic Reading |
|-------------------|---------|--------------|--------------|------------------|
| [declared in gradient] | [S1] | GROUNDED | persisted/transformed/resolved | [GROUNDED objection that persisted = strong blocker; INFERRED objection that persisted = conditional risk] |

**PHASE 2 GATE:**
```
[ ] Synthesis artifact: all 7 columns, all subjects × all dimensions populated
[ ] Synthesis-Weight column: reflects epistemic gradient consistently
[ ] Epistemic Weight Summary: at least one convergence and one contradiction
[ ] Objection lifecycle: final status declared with epistemic reading
```

---

## PHASE 3 — META-ANNOTATIONS

**Simulation fidelity note:** Name one claim that is grounded in the declared
prior-knowledge maps or domain context, and one claim that is constructed plausibility —
naming which it is and why.

**Voice divergence acknowledgment:** Name one concrete contrast between how the GROUNDED
subject and the INFERRED subject were made to sound different — a specific vocabulary
choice, hedging pattern, or specificity level that maps to their epistemic positions.
The divergence should be an artifact of the epistemic structure, not just "different opinions."
```

---

**Summary of variation axes:**

| Variation | Primary Axis | Secondary Axis | Structural Focus |
|-----------|-------------|----------------|-----------------|
| V-01 | Role sequence (skeptic-first cascade) | — | Objection lifecycle tracking |
| V-02 | Output format (schema-dominant tables) | — | Document-head format contract |
| V-03 | Phrasing register (conversational/directive) | — | Author-facing purpose explanation |
| V-04 | Lifecycle emphasis (named checklist gates) | Inertia framing | Inertia as first-class structural element |
| V-05 | Role sequence (influence-map order) | Schema synthesis | Epistemic gradient in synthesis weighting |
