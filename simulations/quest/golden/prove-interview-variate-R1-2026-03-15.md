# prove-interview — Prompt Variations R1
# Date: 2026-03-15
# Rubric: prove-interview-rubric-v1-2026-03-15.md
# Round: 1 (first generation, single-axis + combination)

---

## Variation Axes Selected

| Axis | Description |
|------|-------------|
| Role sequence | Which persona runs first; whether disposition ordering is prescribed |
| Output format | Table vs. prose vs. list for evidence extraction |
| Phrasing register | Imperative/technical vs. conversational/descriptive |
| Lifecycle emphasis | How much structural scaffolding each phase receives |
| Inertia framing | How prominently the status-quo competitor / current practice anchors the interview |

Single-axis variations: V-01 (role sequence), V-02 (output format), V-03 (phrasing register)
Combination variations: V-04 (lifecycle emphasis + inertia framing), V-05 (role sequence + output format + inertia framing)

---

## V-01 — Role Sequence / Disposition-Ordered

**Axis**: Role sequence
**Hypothesis**: Opening with the skeptic forces the simulation to generate resistance before
confirmation. When the champion speaks second, the artifact earns C-04 (surprising/confirming
moment) structurally — the champion either overcomes the skeptic's objections or doesn't. The
signal distinction arrives from the *order*, not just the *presence* of two voices.

---

You are simulating a series of stakeholder interviews. The topic and hypothesis are provided
below. Your job is to inhabit each interview subject fully — their role, their domain knowledge,
their concerns, and their blind spots — and produce a transcript that reads as if the interview
actually happened.

**Topic**: {Topic}
**Hypothesis under investigation**: {Signal}

### Interview order

Run interviews in this exact sequence:

1. **SKEPTIC first** — the subject most likely to resist, question, or push back on the hypothesis
2. **NEUTRAL second** — the subject with the most to gain or lose, but no strong prior position
3. **CHAMPION last** — the subject most likely to confirm or validate the hypothesis

This ordering matters. The skeptic's objections become the prior evidence the champion must
address. If the champion confirms the hypothesis without engaging the skeptic's specific concerns,
that is a weaker signal than if the champion directly overturns them.

### For each interview subject, produce

**Identity block** (before any questions):
- Role and title
- What this person knows (their domain, their experience level)
- What they do not know or have not seen
- Their primary concern entering this conversation

**Interview transcript**:
- 4–6 questions from the interviewer
- Answers in the subject's voice — their vocabulary, their framing, their specific knowledge
- At least one follow-up question that responds to a prior answer (not from the prepared list)
- One moment where the subject says something that surprises the interviewer or explicitly
  confirms / contradicts a prior assumption — label this moment **[SIGNAL MOMENT]**

**Evidence extraction** (after the transcript):
- List 1–3 concrete evidence items extracted from this interview
- Each item states: what was said, why it matters to the hypothesis

### After all interviews

Write a **Cross-Interview Synthesis**:
- What did the skeptic's concerns and the champion's confirmation have in common, if anything?
- What is the dominant arc — did the champion overcome the skeptic's objections, echo them, or
  introduce new ones?
- Does the combined evidence shift confidence in the hypothesis up, down, or sideways?

---

## V-02 — Output Format / Structured Table Extract

**Axis**: Output format
**Hypothesis**: Requiring a three-column evidence table (Quote | Signal Type | Strength) forces
explicit extraction (C-03) and signal-type tagging (C-09) as a structural consequence of the
format itself. A table row cannot be left vague — it must commit to a quote, a classification,
and a judgment. This format pressure should eliminate implicit-only evidence.

---

Simulate {N} stakeholder interviews on the topic and hypothesis below. For each subject, produce
a transcript and a structured evidence table. Synthesis follows all interviews.

**Topic**: {Topic}
**Hypothesis**: {Signal}

### Subjects to interview

For each subject you select (or that is specified), establish:

- **Role**: their title or function
- **Context**: 2–3 sentences on what they know, what they care about, and what lens they bring
  to this topic

### Transcript format

Write each interview as a Q&A exchange:

> **Q**: [question text]
> **[Subject name]**: [answer in subject's voice]

Include 4–6 exchanges. The subject's answers should sound like *them* — not like a product
description or a neutral summary. They have opinions, blind spots, and vocabulary that
matches their role.

Mark one exchange per subject with **>> NOTABLE** where something unexpected, confirming,
or contradictory surfaces.

### Evidence table (per subject)

After each transcript, fill in this table:

| Quote (verbatim from transcript) | Signal Type | Strength |
|----------------------------------|-------------|----------|
| "..." | [risk / preference / constraint / validation / invalidation] | [strong / moderate / weak] |
| "..." | ... | ... |

- Minimum 1 row per subject. Maximum 3 rows.
- **Quote** must be verbatim text from the transcript above, not a paraphrase.
- **Signal Type** must be one of: `risk`, `preference`, `constraint`, `validation`, `invalidation`.
- **Strength** must be one of: `strong`, `moderate`, `weak`.

### Cross-Interview Synthesis

After all subjects:

1. What signal types dominate across subjects? (Tally by type)
2. Where do subjects contradict each other? Name the specific quotes that conflict.
3. Net verdict: does the evidence support, refute, or leave the hypothesis unresolved?
   State your confidence as: `high`, `medium`, or `low`, with one sentence of rationale.

---

## V-03 — Phrasing Register / Conversational-Descriptive

**Axis**: Phrasing register
**Hypothesis**: A descriptive register — describing what a *good* interview looks like rather
than commanding outputs — activates richer persona voice (C-02) because it primes for
naturalism rather than compliance. Imperative prompts ("produce a transcript") invite
list-shaped outputs. Descriptive prompts ("a good interview feels like...") invite voice.

---

Think of this as running a real discovery session — except the interviewees are simulated, and
you're playing all of them. Your goal is to find out what people at different vantage points
actually think about the hypothesis below. Some of them will surprise you. Some will confirm
what you already suspected. A few will say something that reframes the whole question.

**Topic**: {Topic}
**What you're investigating**: {Signal}

Here is how a good simulation of this goes:

You pick 2–4 people to talk to. You know something about each of them before the conversation
starts — their role, what they've seen, what they're worried about, what they don't know yet.
You write that down before you put any words in their mouths.

The conversation itself has a texture. It doesn't start with the hypothesis. It starts with where
they are today — what they do now, what the current setup looks like to them. The hypothesis
comes in as a question, not a declaration. They react to it from where they stand, not from
where you wish they stood.

Each conversation produces at least one moment worth noting — a place where the person said
something that changed the direction of the next question, or confirmed something you'd been
wondering about, or introduced a concern you hadn't considered. You mark that moment.

After all the conversations, you step back and look at what you have. Not just individual quotes,
but the pattern across conversations. Where did people agree despite coming at it from different
angles? Where did they contradict each other in ways that tell you something real about the
tension in the hypothesis? What's the most honest thing you can say about what the interviews
revealed?

---

**For each person you interview, write:**

*Before you begin:* their role, what they know, and what they care about most in this area.

*The conversation:* a Q&A exchange that sounds like them. Their vocabulary. Their specific
concerns. The place where they surprised you — label it.

*What you extracted:* 1–3 specific items of evidence from this conversation, stated plainly.

---

**After all interviews, write the synthesis.** What did this set of conversations actually tell
you about the hypothesis? What did you expect to hear that you didn't? What does the pattern
across subjects say that no single subject said alone?

---

## V-04 — Lifecycle Emphasis + Inertia Framing

**Axes**: Lifecycle emphasis, Inertia framing
**Hypothesis**: Giving the *setup* phase substantial structural space — requiring subjects to
describe what they *do today* before any feature or change is introduced — produces a natural
incumbent baseline. The contrast between the Q1 current-practice answer and the later
feature-reaction answer is itself the evidence. Inertia is not background; it is the first signal.

---

Simulate stakeholder interviews for the investigation below. Before any feature or proposed
change is introduced to a subject, establish their current practice. The gap between current
practice and their reaction to the proposal is where the evidence lives.

**Topic**: {Topic}
**Hypothesis**: {Signal}

---

### Phase 1 — Subject Setup (complete before any interview begins)

For each subject, document:

**Subject card:**
- Role and title
- Current practice: what does this person do today in the area the hypothesis touches?
  (2–4 sentences, specific to their role — not general description)
- Known concerns: what are they watching out for, what has gone wrong before in this area?
- Blind spots: what are they likely *not* to know or consider?
- Disposition: are they more likely to be a champion, skeptic, or neutral party on this
  hypothesis? Explain briefly why.

Do not begin any transcript until all subject cards are written.

---

### Phase 2 — Interview Transcripts

For each subject, run the interview in two parts:

**Part A — Current practice questions** (2–3 questions)
These questions must not mention the hypothesis, the proposed feature, or any change. They
establish how the subject operates today. A good Q1 asks what the subject does, not what they
think about a change.

**Part B — Hypothesis probe questions** (3–4 questions)
Now introduce the hypothesis. Ask the subject to react from the position established in Part A.
A subject whose Part B answer ignores their Part A current practice is a warning sign — mark it.

Mark one exchange per interview **[SIGNAL MOMENT]** — the point where the subject said
something that surprised, confirmed, or contradicted an expectation.

---

### Phase 3 — Evidence Extraction

After each interview, extract:

- 1–3 evidence items, each stated as: *what the subject said* → *what this means for the
  hypothesis*
- For each item, note whether the Part A current-practice context amplifies or changes
  how you read the Part B answer

---

### Phase 4 — Synthesis

After all interviews:

- What did the current-practice baselines reveal about the inertia the hypothesis has to
  overcome? Name it specifically.
- Where did subjects' current practices diverge enough that the hypothesis means different
  things to different subjects?
- Cross-subject signal: convergence, contradiction, or split verdict?
- Does the combined evidence support, refute, or leave the hypothesis unresolved?

---

## V-05 — Combined: Role Sequence + Output Format + Inertia Framing

**Axes**: Role sequence, Output format, Inertia framing (all three combined)
**Hypothesis**: The three axes reinforce each other. Skeptic-first ordering exposes incumbent
friction immediately. Tabular evidence extraction forces explicit commitment to quotes and signal
types. Explicit inertia framing makes the incumbent's switching cost the lens through which
champion confirmation is read. The combination should produce maximum signal density and
make C-04 (signal moment), C-03 (explicit extraction), and C-08 (synthesis) structurally
inevitable rather than effortful.

---

Simulate stakeholder interviews on the hypothesis below. Run them in skeptic-first order. Extract
evidence in table form. Anchor every interview in the subject's current practice before
introducing the hypothesis.

**Topic**: {Topic}
**Hypothesis**: {Signal}

---

### Setup — Human Subjects Roster

Before any interview begins, complete this roster:

| # | Subject | Role | Current Practice (today, before any change) | Disposition | Rationale |
|---|---------|------|---------------------------------------------|-------------|-----------|
| S-01 | [name] | [role] | [what they do today in this domain] | SKEPTIC | [why skeptic] |
| S-02 | [name] | [role] | [what they do today in this domain] | NEUTRAL | [why neutral] |
| S-03 | [name] | [role] | [what they do today in this domain] | CHAMPION | [why champion] |

Run interviews in roster order: S-01 → S-02 → S-03. Do not reorder.

---

### Interview Format (repeat for each subject)

**Header**: Subject name, role, disposition from roster.

**Current-practice questions** (2 questions, no mention of hypothesis):
> **Q1**: [what they do today]
> **[Subject]**: [answer in their voice]

> **Q2**: [a specific friction or challenge in current practice]
> **[Subject]**: [answer in their voice]

**Hypothesis probe questions** (3–4 questions):
> **Q3**: [introduce the hypothesis or proposed change]
> **[Subject]**: [reaction grounded in their current practice]
> ...

Mark one exchange **>> [SIGNAL MOMENT]**: the point where the subject said something
unexpected, confirming, or contradictory. One sentence explaining why it is a signal moment.

---

### Evidence Table (after each interview)

| Quote (verbatim) | Signal Type | Strength | Current-Practice Link |
|------------------|-------------|----------|-----------------------|
| "..." | `risk` / `preference` / `constraint` / `validation` / `invalidation` | `strong` / `moderate` / `weak` | How does their Q1/Q2 current-practice answer change how you read this quote? |

Minimum 1 row. Maximum 3 rows.

---

### Cross-Interview Synthesis

After all three interviews:

**Inertia verdict**: What does the skeptic's current-practice baseline reveal about the switching
cost the hypothesis asks subjects to absorb? Did the champion confirm they would absorb it, or
did they implicitly endorse the skeptic's concern?

**Arc signal**: Did the champion's confirmation *overcome* the skeptic's resistance (strong
signal for the hypothesis) or merely restate it from a different angle (weak signal)?

**Signal tally by type**: Count across all evidence table rows.

**Net verdict**: Support / Refute / Unresolved. Confidence: High / Medium / Low.
One sentence of rationale citing the most important evidence item from the table.
