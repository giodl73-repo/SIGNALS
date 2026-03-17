# prove-interview — Prompt Variations R3
# Date: 2026-03-15
# Rubric: prove-interview-rubric-v3-2026-03-15.md
# Round: 3 (first generation targeting v3 criteria C-13, C-14, C-15)

---

## Variation Axes Selected

| Axis | Description |
|------|-------------|
| Role sequence | Whether current-reality questions are structurally separated from hypothesis-probe questions per subject |
| Output format | Five-column evidence table with mandatory Strength Rationale column (vs. four-column) |
| Phrasing register | Contradiction-seeking discovery framing vs. structured imperative |
| Lifecycle emphasis | Named phases with a dedicated Contradiction Surface gate step |
| Inertia framing | Status-quo practice as the opening anchor, established before any hypothesis is named |

Single-axis variations: V-01 (role sequence / C-15), V-02 (output format / C-13 + C-14), V-03 (phrasing register / C-14 + C-15)
Combination variations: V-04 (lifecycle emphasis + contradiction surface / C-14 + C-15), V-05 (role sequence + output format + contradiction surface / C-13 + C-14 + C-15 combined)

---

## V-01 — Role Sequence / Reality-First Split

**Axis**: Role sequence
**Hypothesis**: Labeling the first block of questions for each subject "Part A — Current Reality" and
prohibiting any mention of the hypothesis or proposed change in that block enforces C-15 structurally.
The label is the constraint — a Part A question that names the hypothesis fails the Part A format test
on inspection. The split forces the model to find two questions about the subject's current experience
*before* framing the investigation, which produces authentic baseline context unavailable if the
hypothesis is introduced first.

---

You are simulating a series of stakeholder interviews. The topic and hypothesis are provided below.
Your job is to inhabit each interview subject fully — their role, their domain knowledge, their
concerns, and their blind spots — and produce a transcript that reads as if the interview actually
happened.

**Topic**: {Topic}
**Hypothesis under investigation**: {Signal}

### Interview order

Run interviews in this exact sequence:

1. **SKEPTIC first** — the subject most likely to resist, question, or push back on the hypothesis
2. **NEUTRAL second** — the subject with the most to gain or lose, but no strong prior position
3. **CHAMPION last** — the subject most likely to confirm or validate the hypothesis

### For each interview subject, produce

**Identity block** (before any questions):
- Role and title
- What this person knows (their domain, their experience level, their prior history with the
  problem area)
- What they do not know or have not seen
- Their primary concern entering this conversation

**Part A — Current Reality questions** (2–3 questions):

These questions establish where the subject is *today*. They must not name the hypothesis, the
proposed feature, or any specific change under consideration. A Part A question asks what the
subject does, sees, or experiences now — not what they think about a change.

Good Part A openers: "Walk me through how you handle X today," "What does the current process
look like from your perspective," "What's the part of X that works least well for you right now."

A Part A question that names the hypothesis fails the format. Do not write one.

**Part B — Hypothesis probe questions** (3–4 questions):

Only after Part A is complete, introduce the hypothesis. Ask the subject to react from the
position they established in Part A. A subject whose Part B reaction makes no reference to
what they said in Part A — as if Part A never happened — is a warning sign. Mark such a
response **[FLOAT]**.

Mark one exchange per subject (Part A or Part B) **[SIGNAL MOMENT]** — the point where the
subject said something unexpected, confirming, or contradictory — with one sentence on why it
matters.

**Evidence extraction** (after the transcript):
- List 1–3 concrete evidence items extracted from this interview
- Each item states: what was said, what signal type it represents
  (`risk` / `preference` / `constraint` / `validation` / `invalidation`), and why it matters
  for the hypothesis

### After all interviews

Write a **Cross-Interview Synthesis**:
- What did the skeptic's Part A current-reality baseline reveal that the champion's Part A
  either confirmed or contradicted?
- Where do the subjects' evidence items conflict? Name at least one specific contradiction
  between what two subjects said — not just that they disagreed, but which specific claims are
  in tension.
- Does the combined evidence shift confidence in the hypothesis up, down, or sideways?

---

## V-02 — Output Format / Five-Column Evidence Table

**Axis**: Output format
**Hypothesis**: Requiring a five-column evidence table (Quote | Signal Type | Strength | Strength
Rationale | Basis) makes C-13 a structural consequence of the format. A table row with an empty
Rationale column is visibly broken — it cannot be left blank without the incompleteness being
immediately apparent on inspection. Requiring the Rationale to name the *source type* (verbatim vs.
inferred), *circumstance* (prompted vs. unprompted), or *specificity* (domain-specific vs. generic)
closes the gap that R2's four-column table left open: strength ratings that name no reason for the
rating are arbitrary. The synthesis step explicitly requires a contradiction surface (C-14) as a
numbered substep.

---

Simulate {N} stakeholder interviews on the topic and hypothesis below. For each subject, produce
a transcript followed by a structured evidence table. Synthesis follows all interviews.

**Topic**: {Topic}
**Hypothesis**: {Signal}

### For each subject

**Setup block** (before the transcript):
- Role and title
- Prior knowledge and context: 2–3 sentences on what they know, what they care about, and
  what lens they bring to this topic — stated before any questions are asked
- Disposition: their likely stance on the hypothesis (skeptic / neutral / champion), briefly
  explained

**Transcript** (Q&A exchange):

> **Q**: [question text]
> **[Subject name]**: [answer in subject's voice — their vocabulary, their concerns, their
> specific knowledge]

Include 4–6 exchanges. The first question for each subject must establish their current practice
or experience before the hypothesis is named. Mark one exchange per subject **>> NOTABLE** where
something unexpected, confirming, or contradictory surfaces.

**Evidence table** (after each transcript):

| Quote (verbatim) | Signal Type | Strength | Strength Rationale | Basis |
|------------------|-------------|----------|--------------------|-------|
| "..." | `risk` / `preference` / `constraint` / `validation` / `invalidation` | `strong` / `moderate` / `weak` | One sentence: *why* this strength? Name the source type, circumstance, or specificity. | verbatim / inferred / corroborated |

Rules:
- **Quote** must be verbatim text from the transcript — not a paraphrase or summary
- **Signal Type** must be one of the five listed options
- **Strength** must be one of the three listed options
- **Strength Rationale** is required and must name *why* the item earns this rating. Acceptable
  rationale forms: "strong: verbatim objection raised unprompted, before any question about this
  concern"; "moderate: subject stated this but hedged with 'probably' — not a firm commitment";
  "weak: inferred from tone, not explicitly stated." A Strength Rationale that merely restates
  the strength label ("strong because it is a strong signal") fails.
- **Basis** must be one of: `verbatim` (item is a direct quote), `inferred` (item is read from
  subtext or tone), `corroborated` (item echoes a prior subject's statement)
- Minimum 1 row per subject, maximum 3 rows

### Cross-Interview Synthesis (after all subjects)

1. **Signal type tally**: Count evidence items by Signal Type across all subjects
2. **Strength tally**: Count strong / moderate / weak across all subjects
3. **Top-weight evidence**: Name the single highest-Strength item and its Rationale; explain
   why it carries the most weight for the hypothesis
4. **Contradiction surface**: Where do subjects' evidence items directly conflict? Name at least
   one pair of specific quotes or table rows that stand in tension. State the nature of the
   conflict (factual disagreement, priority inversion, or irreconcilable constraint). A synthesis
   that finds only convergence without examining divergence does not pass this step.
5. **Net verdict**: Support / Refute / Unresolved — confidence `high` / `medium` / `low` —
   one sentence of rationale citing the highest-strength evidence item and its Basis

---

## V-03 — Phrasing Register / Contradiction-Seeking Discovery

**Axis**: Phrasing register
**Hypothesis**: A descriptive, conversational register that explicitly frames *contradiction as the
prize* — describing what a good multi-subject interview is actually trying to find — activates C-14
more reliably than an imperative checklist. An imperative prompt that says "name a contradiction in
synthesis" produces a rote step. A descriptive prompt that says "the most interesting thing in a
multi-subject session is where subjects who should agree don't" reorients the model's goal. C-15 is
served by describing how good interviews begin ("you start with where people actually are today,
not with the hypothesis") rather than mandating it as a format rule. C-10 and C-12/C-13 are
explicitly N/A for this format by design.

---

Think of this as running a discovery session — except the people you're talking to are simulated,
and you're playing all of them. Your goal is not to validate the hypothesis. Your goal is to find
out what these people actually think, which may confirm it, challenge it, or make it irrelevant.

**Topic**: {Topic}
**What you're investigating**: {Signal}

---

Here is how a good session of this kind goes:

You pick 2–4 people to talk to. They should have different vantage points on the problem — not
different opinions on the hypothesis, but different *experiences*. A buyer and an end-user. A
long-tenured practitioner and someone who just encountered this problem for the first time.

Before you put any words in their mouths, write down who each person is: their role, what
they've seen, what they worry about, what they don't know yet. Also write down whether they're
likely to be skeptical, neutral, or sympathetic to the hypothesis — and why. A person whose
stance you haven't thought about before the conversation starts will tend to say whatever fits
the narrative.

Every conversation starts in the same place: where the person is today. Not with the hypothesis.
Not with "what do you think of this idea." With "walk me through what you actually do." The
hypothesis enters later, as a question — "what would it mean for you if X worked differently."
When you start with the hypothesis, you're asking people to react to your assumptions. When you
start with their current reality, you find out what they actually experience. The difference
in what surfaces is significant.

Each conversation has at least one moment worth marking — somewhere in the exchange, the person
said something that mattered. It might be unexpected. It might confirm something you'd been
wondering about. It might introduce a concern you hadn't considered. Mark that moment and note
why it matters.

After each conversation, write down what you extracted — not the whole transcript, but the 1–3
things that actually matter. For each item: say what kind of signal it is (risk, preference,
constraint, validation, or invalidation). Say how strong you'd rate it, and say *why* — not
just "strong" but what makes it strong: is it a verbatim unprompted objection from the person
most likely to push back? Is it something inferred from how they answered, not stated directly?
Is it a point three different subjects made without coordinating? The why is what makes the
rating useful to anyone who reads this later.

After all conversations, the most valuable thing you can write is not the list of what each
person said. It is where they *conflict*. Two people who came at the same question from
different angles and landed in the same place is signal. Two people who came at it from
different angles and ended up at different places is a stronger signal — it names a real
tension in the hypothesis that agreement obscures. When you write the synthesis, make your
first move toward the contradiction, not the consensus.

Note: this format is conversational by design. Tabular phase gates and per-item annotation
tables are not used here — that is an intentional tradeoff for voice fidelity, not an
omission. C-10 (phase gates) and C-12/C-13 (strength tables) are N/A for this format.

---

**For each person, write:**

*Before the conversation:* role, what they know, what they care about, their disposition and
why.

*The conversation itself:* Q&A that sounds like them — their vocabulary, their specific
concerns. It starts with their current reality. The moment that mattered, labeled.

*What you extracted:* 1–3 items. For each: what was said, what kind of signal, how strong,
and *why* that strength rating (name the source, the circumstance, or the specificity).

---

*After all conversations:* The synthesis. Start with where subjects conflict — name the
specific claims or concerns that stand in tension. Then name the pattern that holds across all
of them despite that tension. What's the most honest thing you can say about what these
conversations revealed?

---

## V-04 — Lifecycle Emphasis + Contradiction Surface

**Axes**: Lifecycle emphasis, Contradiction surface
**Hypothesis**: When synthesis is split into two named phases — "Convergence" and "Contradiction
Surface" — and the Contradiction Surface is a required gate step with a minimum entry count, C-14
becomes structurally enforced regardless of whether the author is inclined to look for conflict.
The gate makes omission impossible: a synthesis with no Contradiction Surface entries cannot pass
the Phase 4 gate. Reality-first framing in Phase 2 (Part A questions prohibited from naming the
hypothesis) enforces C-15 by construction.

---

Simulate stakeholder interviews for the investigation below. Organize the work into four named
phases. Before any feature or hypothesis is introduced to a subject, establish their current
practice. After all interviews, the synthesis produces a dedicated Contradiction Surface step
before any convergence or verdict is written.

**Topic**: {Topic}
**Hypothesis**: {Signal}

---

### Phase 1 — Subject Setup

Document every subject card before any transcript begins.

**Subject card format:**
- **Role and title**
- **Current practice**: what does this person do today in the area the hypothesis touches?
  (2–4 sentences, specific to their role — no hypotheticals, no feature names)
- **Prior concerns**: what has gone wrong in this area before? What are they watching out for?
- **Blind spots**: what are they likely not to consider or have access to?
- **Disposition**: champion / skeptic / neutral — and one sentence explaining why their current
  practice places them at this position

**Phase 1 gate**: Do not begin any transcript until all subject cards are written, each carrying
a current-practice description, a prior-concerns entry, and a disposition statement.

---

### Phase 2 — Interview Transcripts

For each subject, run the interview in two labeled parts:

**Part A — Current Practice questions** (2–3 questions)

Do not mention the hypothesis, the proposed feature, or any change. Establish what this person
does today. Good Part A questions: "How do you handle [X] right now?", "What does that process
look like from your seat?", "What's the friction point you run into most often here?"

A Part A question that names or implies the hypothesis fails the Part A format. Do not write one.

**Part B — Hypothesis probe questions** (3–4 questions)

Introduce the hypothesis only after Part A is complete. Ask the subject to react from the
position established in Part A. If the subject's Part B answer is disconnected from what they
said in Part A — as if the baseline never happened — mark it **[FLOAT]**.

Mark one exchange per interview **[SIGNAL MOMENT]** — the point where the subject said
something unexpected, confirming, or contradictory — with a one-line note on why it matters.

**Phase 2 gate**: Every subject's transcript must contain at least one Part A exchange and
one Part B exchange, and at least one exchange must be marked [SIGNAL MOMENT], before Phase 3
begins.

---

### Phase 3 — Evidence Extraction

After each interview, extract:

- 1–3 evidence items per subject
- Each item: *what was said* → *what this means for the hypothesis* → signal type
  (`risk` / `preference` / `constraint` / `validation` / `invalidation`) → strength
  (`strong` / `moderate` / `weak`) → strength rationale (one sentence naming the source type,
  circumstance, or specificity: e.g., "strong: unsolicited, raised in Part A before hypothesis
  was introduced"; "weak: inferred from a hedge, not an explicit statement")
- A strength rationale that only restates the strength level fails. Name the *why*.

**Phase 3 gate**: Every subject must have at least one extracted evidence item with a signal
type, strength rating, and strength rationale before Phase 4 begins.

---

### Phase 4 — Synthesis

Phase 4 has two required sections. Write them in this order:

**4A — Contradiction Surface** (write this first)

Before writing any convergence or verdict, identify where subjects' evidence items conflict.
For each contradiction:
- Name the two (or more) specific items or quotes in tension
- State the nature of the conflict: factual disagreement (subjects assert incompatible facts),
  priority inversion (both acknowledge the same concern but weight it differently), or
  irreconcilable constraint (one subject's baseline makes the other's preference impossible)
- Minimum one entry required. A synthesis that produces only convergence has not completed
  this section.

**4B — Convergence and Verdict**

After naming the contradictions:
- What did subjects agree on despite their different dispositions or practices? Name the shared
  concern or shared validation.
- What does the current-practice baseline from Phase 1 reveal about the inertia the hypothesis
  has to overcome? Name it specifically from the subject cards.
- **Verdict**: Support / Refute / Unresolved — confidence high / medium / low — one sentence
  citing the single most important evidence item from Phase 3, including its strength rationale.

---

## V-05 — Combined: Role Sequence + Output Format + Contradiction Surface

**Axes**: Role sequence (C-15), Output format (C-13), Lifecycle emphasis (C-14 gate)
**Hypothesis**: Three axes, each targeting one new v3 criterion: the Part A / Part B question split
enforces C-15 structurally (a Part A question that names the hypothesis fails the format); the
five-column evidence table with mandatory Strength Rationale column enforces C-13 (a row with no
rationale is visibly incomplete); and a named Contradiction Surface gate step in synthesis enforces
C-14 (the synthesis cannot close without naming at least one conflict). No criterion depends on
author intent — all three are consequences of structure. The skeptic-first role ordering presses
C-11 and C-04 as structural bonuses. Each axis does independent work; removal of any one axis
leaves its criterion at risk.

---

Simulate stakeholder interviews on the hypothesis below. Run subjects in skeptic-first order.
For each subject, separate current-reality questions from hypothesis-probe questions into labeled
parts. Extract evidence in a five-column table with mandatory strength rationale. Close synthesis
with a dedicated Contradiction Surface section before any convergence verdict.

**Topic**: {Topic}
**Hypothesis**: {Signal}

---

### Setup — Subject Roster

Before any interview begins, complete this roster:

| # | Subject | Role | Current Practice (today, before any change) | Disposition | Rationale |
|---|---------|------|---------------------------------------------|-------------|-----------|
| S-01 | [name] | [role] | [what they do today in this domain] | SKEPTIC | [why skeptic] |
| S-02 | [name] | [role] | [what they do today in this domain] | NEUTRAL | [why neutral] |
| S-03 | [name] | [role] | [what they do today in this domain] | CHAMPION | [why champion] |

Run interviews in roster order: S-01 → S-02 → S-03. Complete each subject's transcript and
evidence table before beginning the next subject.

**Roster gate**: Do not begin any transcript until all three rows carry a current-practice
entry and a disposition rationale.

---

### Interview Format (repeat for each subject)

**Header**: Subject name, role, disposition from roster.

**Part A — Current Reality questions** (2 questions; hypothesis must not appear):

> **Q1**: [what they do today in the problem area]
> **[Subject]**: [answer in their voice — vocabulary, framing, specific experience]

> **Q2**: [a specific friction, challenge, or constraint in current practice]
> **[Subject]**: [answer in their voice]

A Part A question that names or implies the hypothesis, the proposed feature, or any change
fails the Part A format. Write the two Part A questions, then stop. Do not begin Part B until
both Part A answers are complete.

**Part B — Hypothesis probe questions** (3–4 questions):

> **Q3**: [introduce the hypothesis or proposed change; ask subject to react from Part A]
> **[Subject]**: [reaction grounded in their current practice]
> ...

Mark one exchange **>> [SIGNAL MOMENT]**: the point where the subject said something
unexpected, confirming, or contradictory — one sentence explaining why it is a signal moment.

---

### Evidence Table (after each interview)

| Quote (verbatim) | Signal Type | Strength | Strength Rationale | Basis |
|------------------|-------------|----------|--------------------|-------|
| "..." | `risk` / `preference` / `constraint` / `validation` / `invalidation` | `strong` / `moderate` / `weak` | One sentence naming *why* this rating: source type (verbatim vs. inferred), circumstance (prompted vs. unprompted), or specificity (domain-specific vs. generic claim). | `verbatim` / `inferred` / `corroborated` |

Rules:
- **Quote** must be verbatim text from the transcript — not a paraphrase
- **Strength Rationale** is required on every row. It must name the *why* — source type,
  circumstance, or specificity. "Strong because it directly addresses the hypothesis" fails;
  "strong: verbatim statement from the buyer role, unprompted, in Part A before hypothesis was
  named" passes.
- **Basis** classifies the evidential form: `verbatim` (direct quote), `inferred` (subtext or
  tone), `corroborated` (echoed by another subject)
- Minimum 1 row, maximum 3 rows per subject

---

### Cross-Interview Synthesis

Write sections in this order. Do not skip or reorder.

**Section 1 — Contradiction Surface** (required before convergence)

Name at least one point where subjects' evidence items directly conflict. For each:
- Quote or reference the specific table rows in tension (by subject and partial quote)
- State the nature of the conflict: factual disagreement, priority inversion, or irreconcilable
  constraint
- State what the contradiction tells you that agreement alone cannot: what decision would look
  different depending on which subject you believed?

A synthesis with no Contradiction Surface entry has not completed this section. Move to Section
2 only after at least one contradiction is named.

**Section 2 — Arc Signal**

- **Arc trajectory**: What changed from the skeptic (S-01) to the champion (S-03)? Did the
  champion's confirmation engage the skeptic's specific Part A concerns, or float free of them?
- **Sustained signals**: What evidence items converged across subjects despite different
  dispositions? Name them.
- **Inertia question**: What does the current-practice baseline from the roster reveal about
  the switching cost the hypothesis asks subjects to absorb? Did the champion acknowledge it?

**Section 3 — Net Verdict**

- **Signal tally**: Count by Signal Type across all evidence tables; count strong / moderate /
  weak
- **Verdict**: Support / Refute / Unresolved
- **Confidence**: high / medium / low
- **Rationale**: one sentence citing the single highest-Strength evidence item, its Strength
  Rationale, and its Basis. If the Contradiction Surface named a conflict that affects the
  verdict, name it here.
