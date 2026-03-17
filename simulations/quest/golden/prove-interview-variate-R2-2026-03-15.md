# prove-interview — Prompt Variations R2
# Date: 2026-03-15
# Rubric: prove-interview-rubric-v2-2026-03-15.md
# Round: 2 (first generation targeting v2 criteria C-10, C-11, C-12)

---

## Variation Axes Selected

| Axis | Description |
|------|-------------|
| Role sequence | Disposition arc declared and run in order; synthesis traces what changed across arc |
| Output format | Strength-tiered table (Quote / Signal Type / Strength / Rationale) |
| Phrasing register | Conversational-naturalistic; C-10 and C-12 N/A by design |
| Lifecycle emphasis | Named phases with quality-checked gate sentences |
| Inertia framing | Current practice established before hypothesis introduced; baseline as first signal |

Single-axis variations: V-01 (role sequence / disposition arc), V-02 (output format), V-03 (phrasing register)
Combination variations: V-04 (lifecycle emphasis + inertia framing), V-05 (role sequence + output format + lifecycle emphasis)

---

## V-01 — Role Sequence / Disposition-Arc Explicit

**Axis**: Role sequence
**Hypothesis**: Declaring the disposition arc (e.g., skeptic → neutral → champion) before any
transcript begins, and requiring the synthesis to *trace what changed across each transition*
rather than aggregate what each subject said, produces C-11 structurally. The arc is the
argument — "the skeptic said X; by the champion, X had become Y" is a stronger signal than
"Persona 1 said X, Persona 2 said Y." C-10 and C-12 are not targeted by this variation.

---

You are simulating a series of stakeholder interviews to investigate the hypothesis below. Your
job is to inhabit each interview subject fully — their role, their domain knowledge, their
concerns, and their blind spots — and produce transcripts grounded in each persona's plausible
knowledge and vocabulary.

**Topic**: {Topic}
**Hypothesis under investigation**: {Signal}

### Step 1 — Disposition Arc Declaration

Before writing any identity block or transcript, name the disposition arc this simulation
will run:

- **Arc**: the ordered sequence of stances (e.g., skeptic → neutral → champion; resistant →
  curious → advocate)
- **Arc rationale**: one sentence on why this ordering is the most epistemically revealing
  sequence for this hypothesis

Do not begin any identity block until the arc is declared.

---

### For each interview subject (in arc order)

**Identity block** (before the transcript):
- Role and title
- Disposition: their stance entering this conversation — their arc position — and why they
  hold it (prior experience, role constraints, organizational history)
- Prior knowledge: what they know, what they don't know, what they care about most entering
  this conversation

**Interview transcript**:
- 4–6 questions from the interviewer
- Answers in the subject's voice — their vocabulary, their framing, their specific knowledge
- At least one follow-up question that responds directly to a prior answer (not from a
  prepared list)
- One moment per subject labeled **[SIGNAL MOMENT]**: something unexpected, confirming, or
  contradictory, followed by one sentence on why it matters

**Evidence extraction** (after each transcript):
- 1–3 concrete evidence items extracted from this interview
- Each item states: what was said, what signal type it represents
  (`risk` / `preference` / `constraint` / `validation` / `invalidation`), and why it matters
  for the hypothesis

---

### Cross-Interview Synthesis (after all subjects)

The synthesis must trace the arc — not simply list what each subject said.

1. **Arc trajectory**: What changed from the first subject to the last? Did the champion's
   confirmation engage the skeptic's specific objections, echo them without addressing them,
   or introduce new concerns the skeptic hadn't named?
2. **Sustained signals**: What did subjects across the arc agree on despite their different
   stances? Name the shared concern or shared validation.
3. **Shifted signals**: Name the specific exchange — by quote or reference — where a concern
   resolved, escalated, or changed shape across the arc.
4. **Arc verdict**: Does the arc support, challenge, or leave the hypothesis unresolved?
   One sentence.

---

## V-02 — Output Format / Strength-Tiered Evidence Table

**Axis**: Output format
**Hypothesis**: Requiring a four-column evidence table (Quote | Signal Type | Strength |
Strength Rationale) satisfies C-12 and C-09 as a structural consequence of the format — a
table row cannot remain vague, it must commit to a verbatim quote, a type classification, a
strength judgment, and a one-sentence rationale for that judgment. The rationale column makes
strength ratings non-arbitrary and enables `/topic:` aggregation to prioritize with
confidence rather than just categorize. C-10 (lifecycle phases) and C-11 (disposition arc
traced in synthesis) are not primary targets of this variation.

---

Simulate stakeholder interviews on the topic and hypothesis below. For each subject, produce
a transcript followed by a structured evidence table. Synthesis follows all interviews.

**Topic**: {Topic}
**Hypothesis**: {Signal}

---

### For each subject

**Setup block** (before the transcript):
- Role and title
- Prior knowledge and context: 2–3 sentences on what they know, what they care about, and
  what lens they bring to this topic — stated before any questions are asked
- Disposition: their likely stance on the hypothesis (skeptic / neutral / champion),
  briefly explained

**Transcript** (Q&A exchange):

> **Q**: [question text]
> **[Subject name]**: [answer in subject's voice — their vocabulary, their concerns, their
> specific knowledge]

Include 4–6 exchanges. Mark one exchange per subject **>> NOTABLE** where something
unexpected, confirming, or contradictory surfaces.

**Evidence table** (after each transcript):

| Quote (verbatim) | Signal Type | Strength | Strength Rationale |
|------------------|-------------|----------|--------------------|
| "..." | `risk` / `preference` / `constraint` / `validation` / `invalidation` | `strong` / `moderate` / `weak` | One sentence: why this strength level? |

Rules:
- **Quote** must be verbatim text from the transcript above — not a paraphrase or summary
- **Signal Type** must be one of the five listed options
- **Strength** must be one of the three listed options
- **Strength Rationale** is required and must explain the rating: `strong` because it would
  shift a team's decision; `moderate` because it is consistent but not decisive; `weak`
  because it is suggestive but could be dismissed without strong counter-evidence
- Minimum 1 row per subject, maximum 3 rows

---

### Cross-Interview Synthesis (after all subjects)

1. **Signal type tally**: Count evidence items by Signal Type across all subjects
2. **Strength tally**: Count strong / moderate / weak across all subjects
3. **Top-weight evidence**: Name the single highest-Strength item and explain why it carries
   the most weight for the hypothesis
4. **Contradiction surface**: Where do subjects' evidence items conflict? Name the specific
   quotes that stand in tension
5. **Net verdict**: Support / Refute / Unresolved — confidence `high` / `medium` / `low` —
   one sentence of rationale citing the highest-strength evidence item and its signal type

---

## V-03 — Phrasing Register / Conversational-Naturalistic

**Axis**: Phrasing register
**Hypothesis**: A descriptive, conversational register — describing what a good interview
simulation produces rather than commanding structured outputs — activates richer persona voice
(C-02) because it primes for naturalism rather than compliance. Imperative prompts ("produce
a transcript") invite list-shaped outputs. Descriptive prompts ("a good interview feels
like...") invite voice. C-10 (lifecycle phase gates) and C-12 (strength table annotation)
are explicitly N/A for this format by design — an intentional tradeoff: richer voice fidelity
and more natural C-04 signal moments, at the cost of mechanical verifiability.

---

Run a discovery session — except the people you're talking to are simulated, and you're
playing all of them. Your goal is to find out what people at different vantage points actually
think about the hypothesis below. Some of them will surprise you. Some will confirm what you
already suspected.

**Topic**: {Topic}
**What you're investigating**: {Signal}

---

Here is how this goes well:

Before any conversation starts, write down what you know about each person — their role,
what they've seen, what they worry about, what they don't know yet. Also write down their
*disposition*: are they likely to push back, sit somewhere in the middle, or come in
sympathetic to the hypothesis? Say why. A person whose stance you haven't thought about
before you start talking tends to say whatever is convenient.

The conversations don't start with the hypothesis. They start with where each person is
today — what they actually do, what the current reality looks like to them. The hypothesis
enters as a question, not a declaration. Each person reacts from where they stand.

Every conversation has at least one moment worth marking — a place where the person said
something that changed the direction of the next question, confirmed something you'd been
wondering about, or introduced a concern you hadn't considered. Mark that moment.

After each conversation, write down what you extracted — not the whole transcript, but the
1–3 things that actually matter for the investigation. For each item, say what kind of signal
it is: a risk, a preference, a constraint, a validation, or an invalidation. And say how much
weight you'd give it: a strong signal would shift a team's decision, a moderate one is worth
tracking, a weak one is suggestive but not yet decisive.

After all conversations, step back. Don't just list what each person said — trace what
changed across the conversations. If your subjects ran from skeptic to champion, say what the
champion's confirmation does to the skeptic's objections: does it overcome them, echo them
without addressing them, or reframe the concern entirely? What's the most honest thing you
can say about what these conversations revealed?

Note: this format is conversational by design. Tabular phase gates and per-item annotation
tables are not used here — that is an intentional tradeoff for voice fidelity, not an
omission.

---

**For each person, write:**

*Before the conversation:* role, what they know, what they care about, their disposition
on the hypothesis and why.

*The conversation itself:* Q&A that sounds like them — their vocabulary, their specific
concerns. The moment that mattered, labeled.

*What you extracted:* 1–3 items. For each: what was said, what kind of signal it is, how
strong.

---

*After all conversations:* The synthesis. What arc ran across the conversations? What did you
expect to hear that you didn't? What does the pattern across subjects say that no single
subject said alone?

---

## V-04 — Lifecycle Emphasis + Inertia Framing

**Axes**: Lifecycle emphasis, Inertia framing
**Hypothesis**: Forcing each subject to describe their current practice before any feature or
hypothesis is introduced establishes the inertia the feature must overcome as the *first
signal*, not background context. When paired with four named phases and explicit gate
language — "do not begin transcripts until all subject cards are complete" — this produces
C-10 structurally and makes the synthesis's inertia-vs-adoption signal more specific and
falsifiable than a baseline-free simulation. The current-practice baseline is not setup; it
is evidence.

---

Simulate stakeholder interviews for the investigation below. The first thing each subject
does is describe what they do today — before any proposed change or feature is named. The gap
between current practice and reaction to the hypothesis is where the evidence lives.

**Topic**: {Topic}
**Hypothesis**: {Signal}

---

### Phase 1 — Subject Setup

Document every subject card before any transcript begins.

**Subject card format:**
- **Role and title**
- **Current practice**: what does this person do today in the area the hypothesis touches?
  (2–4 sentences, specific to their role — no hypotheticals, no feature names)
- **Prior concerns**: what has gone wrong in this area before? What are they watching out
  for?
- **Blind spots**: what are they likely not to consider or have access to?
- **Disposition**: champion / skeptic / neutral — and one sentence explaining why their
  current practice places them at this position

**Phase 1 gate**: Do not begin any transcript until all subject cards are written and each
carries a current-practice description, a prior-concerns entry, and a disposition statement.

---

### Phase 2 — Interview Transcripts

For each subject, run the interview in two parts:

**Part A — Current practice questions** (2–3 questions)
Do not mention the hypothesis, the proposed feature, or any change. Establish what this
person does today. A good Part A question asks what the subject does, not what they think
about a change.

**Part B — Hypothesis probe questions** (3–4 questions)
Introduce the hypothesis. Ask the subject to react from the position established in Part A.
If the subject's Part B answer ignores their Part A current practice entirely, mark it
**[BREAK]** — a persona whose reaction floats free of their own baseline is a warning sign.

Mark one exchange per interview **[SIGNAL MOMENT]** — the point where the subject said
something unexpected, confirming, or contradictory, with a one-line note on why it matters.

**Phase 2 gate**: Every subject's transcript must contain at least one Part A exchange and
one Part B exchange, and at least one exchange must be marked [SIGNAL MOMENT], before Phase
3 begins.

---

### Phase 3 — Evidence Extraction

After each interview, extract:

- 1–3 evidence items per subject
- Each item: *what was said* → *what this means for the hypothesis* → signal type
  (`risk` / `preference` / `constraint` / `validation` / `invalidation`) → strength
  (`strong` / `moderate` / `weak`)
- For each item, note whether the Part A current-practice baseline amplifies or changes
  how you read the Part B evidence — a Part B answer that contradicts Part A is stronger
  evidence of real friction than one that floats free of any baseline

**Phase 3 gate**: Every subject must have at least one extracted evidence item with a signal
type and strength rating before Phase 4 begins.

---

### Phase 4 — Synthesis

After all interviews and extractions:

1. **Inertia named**: What specific current practice does the hypothesis have to displace?
   Name it from the subject cards, not from the hypothesis statement.
2. **Inertia delta**: Which subjects' current practices diverge enough that the hypothesis
   means different things to different people? Where does adoption cost the most?
3. **Disposition arc**: If subjects span skeptic to champion, trace what ran across the
   transcripts. Did the champion's stance engage or ignore the skeptic's current-practice
   concerns?
4. **Cross-subject signal**: Where did subjects converge despite different current practices?
   Where did they contradict?
5. **Verdict**: Support / Refute / Unresolved — confidence high / medium / low — one
   sentence citing the single most important evidence item from Phase 3.

---

## V-05 — Combined: Role Sequence + Output Format + Lifecycle Emphasis

**Axes**: Role sequence, Output format, Lifecycle emphasis
**Hypothesis**: Combining skeptic-first ordering (which forces falsifying pressure before
confirming evidence), strength-tiered evidence tables (which make C-12 a structural
consequence of the format), and four named phases with quality-checked gate sentences (which
make C-10 structurally enforced) should reliably produce all three new rubric criteria
together. Each axis does independent work: the arc is declared before transcripts begin (C-11
structurally reachable), the tables force strength ratings (C-12), and the phases enforce
completion sequencing (C-10). No criterion depends on author intention — all three are
artifacts of structure.

---

Simulate stakeholder interviews on the hypothesis below. Run subjects in skeptic-first order.
Extract evidence in a strength-tiered table. Organize the simulation into four named phases
with explicit gate conditions.

**Topic**: {Topic}
**Hypothesis**: {Signal}

---

### Phase 1 — Disposition Arc and Subject Setup

**Step 1a — Declare the disposition arc**

Name the sequence of stances this simulation will run:
- **Arc label**: the ordered sequence (e.g., skeptic → neutral → champion)
- **Arc rationale**: one sentence explaining why this ordering maximizes the epistemic
  value of the session for this particular hypothesis

**Step 1b — Subject cards** (one per subject, in arc order)

For each subject:
- Role and title
- Disposition: arc position, and what places them there (prior experience, role constraints,
  organizational history)
- Prior knowledge: what they know, what they don't know, what they care about most
- Current practice: what do they do today in the area this hypothesis touches?

**Phase 1 gate**: Do not begin any transcript until the arc is declared and every subject
card carries a disposition statement and a current-practice entry. Write "Phase 1 complete"
before proceeding to Phase 2.

---

### Phase 2 — Interview Transcripts (in arc order)

For each subject, complete their transcript before starting the next subject.

> **Q[n]**: [question text]
> **[Subject]**: [answer in subject's voice — role-grounded vocabulary, specific concerns]

Include 4–6 exchanges per subject. At least one question per subject must engage the
subject's current practice (from Phase 1) before or alongside the hypothesis probe. Mark one
exchange per subject **[SIGNAL MOMENT]** — something unexpected, confirming, or
contradictory — with a one-line note on why it is a signal moment.

**Phase 2 gate**: Every subject's transcript must be complete and carry at least one
[SIGNAL MOMENT] before Phase 3 begins. Write "Phase 2 complete" before proceeding.

---

### Phase 3 — Evidence Tables

After each transcript, produce an evidence table for that subject:

| Quote (verbatim) | Signal Type | Strength | Strength Rationale |
|------------------|-------------|----------|--------------------|
| "..." | `risk` / `preference` / `constraint` / `validation` / `invalidation` | `strong` / `moderate` / `weak` | One sentence: why this strength level? |

Rules:
- **Quote** must be verbatim text from the transcript above — not a paraphrase
- **Signal Type** must use the listed vocabulary
- **Strength** must use the listed vocabulary
- **Strength Rationale** is required: `strong` means it would shift a team's decision;
  `moderate` means consistent but not decisive; `weak` means suggestive but dismissible
- Minimum 1 row, maximum 3 rows per subject

**Phase 3 gate**: Every subject must have at least one evidence table row with all four
columns populated before Phase 4 begins. Write "Phase 3 complete" before proceeding.

---

### Phase 4 — Cross-Interview Synthesis

The synthesis must address the arc — not simply summarize each subject.

1. **Arc trajectory**: What changed from the skeptic to the champion? Did the champion's
   confirmation engage the skeptic's specific concerns, echo them without addressing them,
   or introduce new ones the skeptic hadn't named?
2. **Sustained signals**: What evidence items converged across the arc despite different
   dispositions? Name them by quote or phase reference.
3. **Shifted signals**: Name the specific exchange where a concern resolved, escalated, or
   changed shape across the arc.
4. **Strength tally**: Count strong / moderate / weak evidence items across all subjects
5. **Verdict**: Support / Refute / Unresolved — confidence high / medium / low — one
   sentence citing the highest-strength evidence item and its signal type

---

*End of R2 variations.*
