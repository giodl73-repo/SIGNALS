Good. I have R1's full text and the v2 rubric changes. The three failure points driving R2:

1. **C-05** — R1 universally used `[SIGNAL MOMENT]`; v2 requires exact format `SURPRISING (expected: X, got: Y)` / `CONFIRMING (validates: Z)`
2. **C-11** — new criterion: meta-observation naming a concrete voice difference between subjects
3. **C-12** — new criterion: follow-up origin visible in the question text (must cite what triggered it)

Axis selection for R2:
- Single-axis: V-01 (output format → expectation register), V-02 (phrasing register → follow-up attribution language), V-03 (lifecycle emphasis → pre-interview expectation declaration)
- Combination: V-04 (inertia framing + role sequence), V-05 (phrasing register + voice divergence meta-layer)

---

# prove-interview — Skill Body Variations R2
**Skill:** prove-interview
**Round:** 2
**Rubric version:** v2
**Date:** 2026-03-15

---

## R2 Axis Map

| Variation | Single/Combined | Axis | Hypothesis |
|---|---|---|---|
| V-01 | Single | Output format — Expectation Register | Requiring an explicit pre-interview Expectation Register (what the interviewer expects each persona to say) makes SURPRISING/CONFIRMING labels structurally inevitable: every labeled moment must reference a specific register entry. C-05 compliance becomes a format consequence, not an authorial judgment call. |
| V-02 | Single | Phrasing register — Follow-up attribution language | A conversational register that models follow-up attribution inside the prompt text ("because you just said X, I want to ask...") primes the simulation to produce C-12-compliant follow-ups. The prompt's own sentence patterns become the template the simulation inherits. |
| V-03 | Single | Lifecycle emphasis — Expectation declaration phase | A dedicated Phase 0 where the interviewer writes what they expect each persona to say before any transcript begins creates the prior expectations that SURPRISING/CONFIRMING labels must reference. Lifecycle space dedicated to expectation-setting makes C-05 prior-expectation links traceable rather than invented after the fact. |
| V-04 | Combined | Inertia framing + Role sequence | Current-practice questions (inertia framing) generate natural per-question priors at the transcript level; skeptic-first ordering ensures those priors are tested under adversarial conditions first. The Q1 current-practice answer becomes the explicit prior that Q3's SURPRISING/CONFIRMING label references — making C-05 traceable to interview content, not to a pre-interview register. |
| V-05 | Combined | Phrasing register + Voice divergence meta-layer | A conversational register that names voice management as an explicit craft problem — asking the author to notice one concrete contrast in how two subjects sound different — activates C-11 as authorial awareness rather than compliance. When the prompt frames voice as a problem to solve, the meta-observation is the natural deliverable, not an afterthought. |

Single-axis: V-01, V-02, V-03  
Combination: V-04, V-05

---

## V-01 — Output Format / Expectation Register

**Axis**: Output format
**Hypothesis**: Requiring an explicit Expectation Register — a table filled before any transcript
begins, with one row per persona stating what the interviewer expects to hear — makes the
`SURPRISING (expected: X, got: Y)` / `CONFIRMING (validates: Z)` format structurally inevitable.
Each labeled moment must name a register entry. The format removes the authorial judgment call
of "what counts as surprising?" — the interviewer has already committed to an expectation, so
every deviation is auditable.

---

You are simulating stakeholder interviews. Produce the Expectation Register first, then the
transcripts, then evidence extraction, then synthesis.

**Topic**: {Topic}
**Hypothesis**: {Signal}

---

### Step 1 — Expectation Register (complete before any transcript)

For each subject you will interview, fill in one row. Do not write any transcript until this
table is complete.

| Subject | Role | Prior knowledge (what they know) | Blind spots (what they don't know) | Expected answer to the hypothesis — write what you think they will say before the interview starts |
|---------|------|-----------------------------------|------------------------------------|-----------------------------------------------------------------------------------------------------|
| [name] | [role] | [2–3 sentences] | [1–2 sentences] | [1–2 sentences: what position do you expect them to take?] |

Minimum 2 subjects. Maximum 4.

---

### Step 2 — Interview Transcripts (one per subject, in any order)

**Header for each interview:**
```
Subject: [name] | Role: [role] | Register row: [paste the expected-answer cell verbatim]
```

**Interview body:**

Write a Q&A exchange of 4–6 questions. The subject's answers must sound like them — their
vocabulary, their frame of reference, the things they would and wouldn't know to worry about.

One question per interview must be a **follow-up** triggered by the previous answer. Mark it:

> **Q [follow-up, triggered by: "[quote the exact phrase from the previous answer that prompted this question]"]**: [question text]

After the full transcript, identify the moment where the subject either confirmed or overturned
your register expectation. Label it using one of these two forms — no other form is accepted:

```
SURPRISING (expected: [paste your register entry], got: [what the subject actually said])
```
```
CONFIRMING (validates: [paste your register entry])
```

If the subject neither confirmed nor surprised the expectation — if you cannot point to a
register entry — write:

```
INCONCLUSIVE (expected: [paste your register entry] — interview did not resolve this)
```

---

### Step 3 — Evidence Extraction (after each transcript)

Extract 1–3 evidence items. For each item:

- **Quote**: verbatim text from the transcript
- **Signal type**: one of `adoption-risk`, `feasibility-concern`, `requirement-gap`, `scope-signal`, `constraint`, `validation`
- **What it means**: one sentence on why this quote matters to the hypothesis

---

### Step 4 — Cross-Interview Synthesis

After all interviews:

1. **Register audit**: For each subject, did the expectation hold? List: SURPRISING / CONFIRMING / INCONCLUSIVE by subject name.
2. **Expectation delta**: Which expectation was most wrong? What does that gap tell you about the hypothesis?
3. **Signal pattern**: What signal types dominate across all evidence items?
4. **Net verdict**: Support / Refute / Unresolved. Confidence: High / Medium / Low. One sentence of rationale.

---

### Step 5 — Simulation Note

Before you finish: name one specific thing you grounded in documented domain knowledge or
real-world context (a practice, a constraint, a concern that is real in this domain) versus one
thing you constructed from plausibility alone.

---

### Step 6 — Voice Observation

Name one concrete difference in how two subjects sounded different. Not "they had different
roles" — cite a specific word choice, framing habit, or concern priority that distinguishes
their voice. Example form: "[Subject A] used the phrase '...' where [Subject B] would have
said '...' — the difference reflects [role/priority contrast]."

---

## V-02 — Phrasing Register / Follow-up Attribution Language

**Axis**: Phrasing register
**Hypothesis**: A conversational register that models follow-up attribution inside the prompt
text — where the prompt itself says "because you just said X, I want to ask..." — primes the
simulation to produce follow-ups that cite what triggered them. The prompt's sentence patterns
become the default template. If the instruction shows C-12 rather than describing it, the
simulation inherits the pattern without requiring a rule.

---

Think of this as a real discovery conversation you are running simultaneously with several
people. You are not reading from a script. You are listening, and what you hear changes what
you ask next.

**Topic**: {Topic}
**What you're testing**: {Signal}

---

Before you talk to anyone, write down what you expect to hear from each person. You've worked
with people in these roles before. You have a guess. Write it down — a sentence or two per
person: what position do you think they'll take on this hypothesis, and why? This is your
expectation record. You will need it later.

Pick 2–4 people to interview. For each one, before you write a single word of their answer,
write what you know about them: their role, what they've seen, what they care about, what
they've probably never had to think about in this area.

---

Here is how a good follow-up works in this kind of conversation:

> You ask about their current workflow. They say: "We actually just rebuilt the whole thing
> last quarter because the old approach kept failing at boundaries."
> Because they mentioned rebuilding at boundaries specifically, you ask: "What did that
> boundary failure look like in practice — was it a data problem or a timing problem?"

The follow-up comes from what they said. It quotes or echoes a phrase from their answer. A
follow-up that could have been asked before the answer — one that doesn't reflect what was
just said — is not a follow-up, it's the next question on a list.

Mark your follow-up questions like this:
> **[Follow-up, from: "[exact phrase from their previous answer]"]**: [your question]

---

Each interview should include one moment where the person either surprised you or confirmed
something you were already thinking. When that moment arrives, label it this way:

If they said something you didn't expect:
```
SURPRISING (expected: [what you wrote in your expectation record], got: [what they actually said])
```

If they confirmed what you expected:
```
CONFIRMING (validates: [what you wrote in your expectation record])
```

The expectation reference must point back to what you wrote before the interview. You cannot
mark something as surprising if you didn't write an expectation first.

---

After the transcript, pull out what you actually learned. Not a summary — specific items.
What did this person say that you could bring back as evidence? Each item should have a signal
type on it: is it an adoption risk, a feasibility concern, a requirement gap, a validation,
or a constraint? The signal type is what makes the evidence usable by someone who didn't sit
in on the interview.

---

After all the interviews, step back. Look at what surprised you versus what confirmed your
expectations. Where were you most wrong? What does that tell you about the hypothesis? Where
did two people agree from completely different vantage points — and is that convergence more
meaningful than either individual answer?

---

One last thing: at the end, write a sentence about how two of the people you interviewed
sounded different from each other. Not their roles — their actual voice. A word they would
use versus a word the other wouldn't. A concern that sits at the front of one person's mind
and nowhere in the other's. Something concrete that proves you were managing two distinct
voices, not one voice playing two parts.

---

## V-03 — Lifecycle Emphasis / Expectation Declaration Phase

**Axis**: Lifecycle emphasis
**Hypothesis**: A dedicated pre-interview phase that requires the interviewer to write explicit
prior expectations for each persona — before any transcript begins — creates the precondition
for C-05 compliance. The SURPRISING/CONFIRMING label requires a "prior expectation" to
reference: if the expectation is written in a visible phase, the label's reference is
traceable. If no pre-interview phase exists, the expectation has to be invented retroactively,
which degrades to unlabeled interesting moments. Phase sequencing generates C-05 compliance
structurally.

---

Simulate stakeholder interviews for the topic and hypothesis below. Follow the four phases in
order. Do not begin a later phase until the earlier phase is complete.

**Topic**: {Topic}
**Hypothesis**: {Signal}

---

### Phase 0 — Expectation Declaration

Before any interview, declare your expectations. For each subject you plan to interview:

```
Subject: [role or name]
What I expect this person to say about the hypothesis: [1–2 sentences — write this now,
before you know what they will say]
What I expect them not to know or not to mention: [1 sentence]
```

Complete one block per subject. Minimum 2 subjects. Do not begin Phase 1 until all
expectation blocks are written.

These expectations are the prior you are testing. Everything labeled SURPRISING or CONFIRMING
in Phase 1 must reference one of these blocks by subject name.

---

### Phase 1 — Interview Transcripts

For each subject:

**Subject header:**
- Role and title
- Prior knowledge: what they know in this domain, what they care about
- Blind spots: what they haven't had to think about in this area
- (Expectation: already written in Phase 0 — do not rewrite, reference by subject name)

**Transcript:**

Write a Q&A exchange of 4–6 questions. Answers must reflect the subject's specific role
vocabulary, concerns, and knowledge level. Generic answers that any subject could give fail.

One question must be a follow-up triggered by the previous answer. Show what triggered it:

> **Follow-up** [because subject said: "[quote]"]: [question]

Immediately after the transcript, label the moment where the subject's answer confirmed or
overturned your Phase 0 expectation:

```
SURPRISING (expected: [quote from Phase 0 expectation block], got: [what the subject said])
```
or
```
CONFIRMING (validates: [quote from Phase 0 expectation block])
```

The quoted text in parentheses must come from Phase 0. If you cannot reference a Phase 0
entry, the label is invalid.

---

### Phase 2 — Evidence Extraction

After each transcript, extract 1–3 evidence items.

Format per item:
- **Finding**: what the subject said (verbatim or close paraphrase)
- **Signal type**: `adoption-risk` / `feasibility-concern` / `requirement-gap` / `scope-signal` / `constraint` / `validation`
- **Hypothesis relevance**: one sentence — why does this finding matter to the hypothesis?

---

### Phase 3 — Cross-Interview Synthesis

After all interviews:

**Expectation audit**: For each subject, state whether Phase 0 expectation held (CONFIRMING),
was overturned (SURPRISING), or was not tested in the interview (NOT REACHED). List by
subject.

**Pattern**: What is the dominant signal type across all evidence items? Where do subjects
converge or contradict each other?

**Prior-expectation delta**: Which of your Phase 0 expectations was most wrong? What does
that tell you about the hypothesis?

**Net verdict**: Support / Refute / Unresolved. Confidence: High / Medium / Low.
One sentence citing the most important evidence item.

---

### Phase 4 — Simulation Fidelity and Voice Note

**Fidelity note**: Name one claim in the interviews grounded in specific domain knowledge
(a real constraint, practice, or behavior in this area) versus one claim constructed from
plausibility alone.

**Voice divergence**: Name one concrete difference in how two subjects were made to sound
distinct. Cite a specific word, concern priority, or framing habit — not just role difference.
Example: "Subject A said '...' where Subject B would have said '...' because [role contrast]."

---

## V-04 — Combined: Inertia Framing + Role Sequence

**Axes**: Inertia framing + Role sequence
**Hypothesis**: Running current-practice questions before introducing the hypothesis generates
per-question prior expectations at the transcript level — the Q1 current-practice answer is
the prior; the Q3 hypothesis-reaction answer is the test. When the skeptic runs first, those
priors form under resistance conditions: the skeptic's current practice is where inertia lives.
The champion's confirmation must then explicitly engage the skeptic's Q1 baseline to produce
a strong signal. C-05 compliance is traceable to Q1/Q3 pairs within each transcript rather
than to a separate register.

---

Simulate stakeholder interviews on the hypothesis below. Run the skeptic first. Anchor every
interview in the subject's current practice before introducing the hypothesis. The gap between
current practice and hypothesis reaction is where your evidence lives.

**Topic**: {Topic}
**Hypothesis**: {Signal}

---

### Preparation — Subject Roster

Before any interview, list your subjects in this order. Do not reorder during the interviews.

| # | Subject | Role | Current practice (what they do today in the area this hypothesis touches) | Expected reaction to the hypothesis |
|---|---------|------|---------------------------------------------------------------------------|--------------------------------------|
| S-01 | [name] | [role/title] | [2–3 sentences — what is their day-to-day relationship to this domain] | [1 sentence — how do you expect them to respond?] |
| S-02 | [name] | [role/title] | ... | ... |

The subject most likely to resist or question the hypothesis goes first (S-01). The subject
most likely to validate goes last.

---

### Interview Format (repeat for each subject, in roster order)

**Interview header**: Subject name, role, disposition (SKEPTIC / NEUTRAL / CHAMPION), and
expected-reaction sentence from the roster.

**Part A — Current practice questions** (2–3 questions, no mention of the hypothesis)

These questions establish the baseline. A good Part A question asks what the subject does,
not what they think about a change. The hypothesis must not appear in Part A.

> **Q1**: [what do they do today]
> **[Subject]**: [answer in their voice — specific to their role and experience]

> **Q2**: [what friction or limitation do they encounter in current practice]
> **[Subject]**: [answer in their voice]

**Part B — Hypothesis probe questions** (3–4 questions)

Introduce the hypothesis. The subject reacts from the position established in Part A. A
Part B answer that ignores the subject's own Part A current practice is a consistency
warning — note it in brackets.

One Part B question must be a follow-up triggered by a previous answer. Mark it:

> **[Follow-up, triggered by: "[phrase from previous answer]"]**: [question]

After the full transcript, place the SURPRISING or CONFIRMING label. The prior-expectation
reference must come from the roster's expected-reaction cell for this subject:

```
SURPRISING (expected: [paste expected-reaction from roster], got: [what they actually said])
```
or
```
CONFIRMING (validates: [paste expected-reaction from roster])
```

---

### Evidence Extraction (after each interview)

Extract 1–3 items:

- **Quote**: verbatim from the transcript
- **Signal type**: `adoption-risk` / `feasibility-concern` / `requirement-gap` / `scope-signal` / `constraint` / `validation`
- **Part A link**: Does the subject's current-practice baseline (Part A) amplify or reframe this evidence? One sentence.

---

### Cross-Interview Synthesis

After all interviews:

**Inertia verdict**: What does the skeptic's current-practice baseline reveal about the
switching cost the hypothesis requires? Did the champion's confirmation acknowledge that
cost, or sidestep it?

**Expectation arc**: Did the champion's validation *overcome* the skeptic's specific
concerns (strong signal) or affirm the hypothesis without engaging those concerns (weak signal)?

**Signal tally**: Count evidence items by signal type across all interviews.

**Net verdict**: Support / Refute / Unresolved. Confidence: High / Medium / Low.
One sentence citing the evidence item with the strongest Part A link.

---

### Voice and Fidelity Note

**Voice divergence**: Name one concrete difference in how S-01 and the final subject sounded
distinct — a specific word, concern, or framing contrast. Generic role difference does not
count; cite the actual language.

**Fidelity note**: Name one claim grounded in real domain knowledge versus one constructed
from plausibility.

---

## V-05 — Combined: Phrasing Register + Voice Divergence Meta-Layer

**Axes**: Phrasing register + Voice divergence meta-layer (targeting C-11 + C-12)
**Hypothesis**: A conversational register frames persona voice as a craft problem the author
is actively managing. When the prompt explicitly names voice management as a deliberate task
— "you are the author of these voices, and they should not all sound like the same person" —
the meta-observation (C-11) becomes the natural deliverable of that task rather than a
compliance requirement added at the end. Combining this with attribution-modeled follow-up
language (C-12) in the same conversational register produces both aspirational criteria from
a single framing shift.

---

You are running a simulated discovery session, but you are also the author of everyone in it.
That second role matters. Your job is not just to produce interviews — it is to produce people
who sound like themselves, not like each other. If you read back the transcripts and they
could be swapped with no loss, you have not done the harder half of the work.

**Topic**: {Topic}
**What you're testing**: {Signal}

---

Start by writing what you expect. Before the first interview begins, write a sentence for each
person: what do you think they will say? You need this written down because later you will
mark the moments where they confirmed or overturned that expectation — and the label requires
you to cite what you expected before you heard the answer.

For each person you plan to interview, write:

- Their role and title
- What they know in this domain — specifically, not generically
- What they have probably never had to think about in this area
- What you expect them to say about the hypothesis (write it now, before the interview)

---

Now run the interviews. The conversations should feel like the subject is talking from their
actual vantage point, not from a neutral summary of that vantage point. A finance person and
an engineering person are not just different roles — they have different language, different
things they lose sleep over, different definitions of the word "feasible." When you write their
answers, you are the author of a character, not a transcriptionist.

For each exchange, write the Q&A. When you ask a follow-up, show what triggered it:

> [Follow-up — they just said "[exact phrase from their previous answer]"]: [your question]

This is how a real follow-up works: it comes from what was said, not from a list. If you can
show what phrase prompted the question, the follow-up is real. If you can't, it's a prepared
question wearing a follow-up label.

---

Mark the moment in each interview where something changed for you — where the subject either
confirmed what you expected or said something that shifted the question. Use exactly one of
these two forms:

```
SURPRISING (expected: [what you wrote before the interview], got: [what they actually said])
```
```
CONFIRMING (validates: [what you wrote before the interview])
```

The thing in the parentheses must come from what you wrote before the interview. Surprising
yourself after the fact, without a prior expectation on record, does not count.

---

After each transcript, extract 1–3 things you would bring back as evidence. Each item needs
a signal type — adoption risk, feasibility concern, requirement gap, validation, constraint —
so that someone who didn't sit in the interview knows what kind of signal it is and where to
use it.

---

After all the interviews, step back and look at the full picture. Where did people from
different vantage points land in the same place — and does that convergence mean something?
Where did they contradict each other in ways that reveal a real tension in the hypothesis?
What is the most honest thing you can say about what the interviews, taken together, showed?

---

Now the author's note: write a brief observation about how you managed these voices as
a craft problem. Name one concrete difference between two subjects — a specific word, a
specific concern that was front of mind for one person and absent in the other, a different
relationship to the word "risk." Not their roles. The actual language. Something a reader
could use to tell them apart on a blind test.

Then name one thing you grounded in real domain knowledge versus one thing you built from
plausibility. The simulation is not a real interview — but grounded plausibility is worth
more than pure invention, and naming where the boundary sits is the honest move.

---
