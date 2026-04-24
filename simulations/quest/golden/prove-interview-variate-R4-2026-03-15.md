# prove-interview — Prompt Variations R4
# Date: 2026-03-15
# Rubric: prove-interview-rubric-v4-2026-03-15.md
# Round: 4 (first generation targeting v4 criteria C-16, C-17, C-18)

---

## Variation Axes Selected

| Axis | Description |
|------|-------------|
| Output format | Subject card as parallel-row table with required "Doesn't know" field (C-16) |
| Lifecycle emphasis | Named Anchor Statement step inserted between Part A and Part B (C-17) |
| Phrasing register | Verdict-inverted goal frame: terminal output declared at opening (C-18) |
| Output format + Lifecycle | Epistemic Weight column in evidence table + Part A Anchor combined (C-16 + C-17) |
| All three combined | Blind-spot cards + Anchor mechanism + verdict-inverted goal frame (C-16 + C-17 + C-18) |

Single-axis variations: V-01 (output format / C-16), V-02 (lifecycle emphasis / C-17),
V-03 (phrasing register / C-18)
Combination variations: V-04 (output format + lifecycle / C-16 + C-17), V-05 (all three /
C-16 + C-17 + C-18)

---

## V-01 — Output Format / Blind-Spot-Forward Subject Card

**Axis**: Output format
**Hypothesis**: Elevating blind spots to a required, parallel field in the subject card —
placed immediately after "What they know" as a structurally coequal row, not as a sub-bullet
in concerns — enforces C-16 by construction. A card table with an empty "Doesn't know" row
is visibly broken on inspection; a subject whose blind spot field reads "they can't know
everything" fails the field's specificity requirement on its face. The parallel structure
(Knows / Doesn't know) forces the declaration to be specific to the hypothesis domain. Because
the card is written before any transcript begins, the epistemic standing of each subject is
fully declared before any question is posed — enabling downstream evidence re-weighting at
the extraction phase without requiring any changes to the transcript format itself.

---

You are simulating a series of stakeholder interviews. The topic and hypothesis are provided
below. Your job is to inhabit each interview subject fully — their role, their domain
knowledge, their blind spots, and their concerns — and produce transcripts grounded in each
persona's plausible knowledge and vocabulary.

**Topic**: {Topic}
**Hypothesis under investigation**: {Signal}

### Subject Cards (complete all before any transcript begins)

For each subject, fill in this card exactly as structured. Every field is required.

---

**Subject [N] Card**

| Field | Content |
|-------|---------|
| **Role** | [job title and organizational context] |
| **Knows** | [what this person has seen, done, or been briefed on — specific to the hypothesis domain; 2–3 sentences] |
| **Doesn't know** | [what this person has NOT seen, NOT experienced, or NOT been briefed on — specific to the hypothesis domain; 2–3 sentences. A generic entry ("they can't know everything") fails this field. Name at least one thing directly relevant to the hypothesis.] |
| **Primary concerns** | [the 2–3 things they care most about given their role and history in this area] |
| **Disposition** | [skeptic / neutral / champion] — [one sentence explaining why their background places them here] |

---

The "Doesn't know" field is a required evidence-weighting dimension. A strong objection from a
subject whose "Doesn't know" field names a gap directly relevant to that objection carries
different downstream weight than the same objection from a subject with no relevant blind spot.
Fill this field with specifics before writing a single line of transcript.

**Setup gate**: Do not begin any transcript until all subject cards are complete, including a
populated and specific "Doesn't know" field for each subject.

---

### For each subject, produce

**Interview transcript** (Q&A exchange, 4–6 exchanges):

The opening question must not name the hypothesis. Establish the subject's current experience
or practice first. Answers must be in the subject's voice — using the vocabulary, concerns,
and knowledge declared in their card. A subject cannot answer from knowledge they declared as
absent in their "Doesn't know" field without the artifact marking it as an inconsistency.

Mark one exchange per subject **[SIGNAL MOMENT]** — the point where the subject said something
unexpected, confirming, or contradictory — with one sentence on why it matters.

**Evidence extraction** (after the transcript):

For each evidence item (1–3 per subject):

- Verbatim quote or close paraphrase
- Signal type: `risk` / `preference` / `constraint` / `validation` / `invalidation`
- Strength: `strong` / `moderate` / `weak`
- Strength rationale: one sentence naming *why* this rating (source type, circumstance, or
  specificity — not "strong because it is strong")
- **Epistemic note**: does this subject's "Doesn't know" field name a gap relevant to this
  evidence item? If yes, say how it changes how you read the item. If no, write "no relevant
  blind spot declared."

---

### Cross-Interview Synthesis (after all subjects)

1. **Signal type tally** across all subjects
2. **Contradiction surface**: Where do subjects' evidence items conflict? Name the specific
   quotes or items in tension. State the nature of the conflict.
3. **Epistemic weighting pass**: Which evidence items carry reduced weight because the subject
   who stated them has a declared relevant blind spot? Name them. Does re-weighting change the
   direction of the verdict?
4. **Net verdict**: Support / Refute / Unresolved — confidence high / medium / low — one
   sentence citing the highest-strength evidence item and whether any epistemic discounting
   applies to it.

---

## V-02 — Lifecycle Emphasis / Part A Anchor Statement

**Axis**: Lifecycle emphasis
**Hypothesis**: Inserting a named structural step — "Part A Anchor" — between Part A and Part
B for each subject enforces C-17 by construction. The anchor is a 1–2 sentence statement
written by the interviewer in summary voice, capturing the position the subject established
in Part A. Part B questions are then required to reference this anchor explicitly. Without the
anchor step, the transition from current-reality questions to hypothesis-probe questions is a
topic change: the subject reacts to the hypothesis fresh rather than from an established
stance. With the anchor, the transition is an evidence progression: the subject reacts from
a declared position. A Part B question that makes no contact with the anchor — that could be
asked of any subject regardless of their Part A answers — is marked UNANCHORED, making the
binding failure visible rather than silent.

---

You are simulating a series of stakeholder interviews on the hypothesis below. For each
subject, the interview runs in two labeled parts with a required Anchor Statement between
them. The Anchor Statement is written before any Part B question is composed, and each Part
B question must reference it.

**Topic**: {Topic}
**Hypothesis under investigation**: {Signal}

---

### For each interview subject

**Identity block** (before any questions):
- Role and title
- Prior knowledge: what they know about the problem domain — stated before any questions
- Blind spots: what they have not seen or have not been briefed on — specific to the hypothesis
  domain, declared before any questions
- Primary concerns: the 2–3 things they care most about in this area
- Disposition: skeptic / neutral / champion — briefly explained

---

**Part A — Current Reality questions** (2–3 questions)

Establish the subject's current experience and practice. These questions must not name the
hypothesis, the proposed feature, or any change under consideration. The subject answers from
where they stand today.

Good Part A openers: "How do you handle [X] today?", "What does the current process look like
from your seat?", "Where does this break down most often for you right now?"

A Part A question that names or implies the hypothesis fails this section's format.

---

**Part A Anchor** (written by the interviewer — not a question)

After the subject's final Part A answer, write the Anchor Statement before proceeding:

> **Anchor**: [Subject name] has established that: [1–2 sentences summarizing the position the
> subject took in Part A — their current practice, their key concern, or the framing they
> brought to the problem domain. This is the stance from which they will now react to the
> hypothesis.]

This is not a question. It is the interviewer's written record of what the subject has
established. Do not begin Part B until this anchor is written.

---

**Part B — Hypothesis probe questions** (3–4 questions)

Introduce the hypothesis. Each Part B question must explicitly reference the Anchor Statement
— asking the subject to react from the position they established in Part A, not from a generic
starting point.

Acceptable anchoring language: "Given what you described about [anchor content]...", "You
said [anchor summary] — with that as your starting point...", "React from where you are: if
[anchor content] is your current reality, what changes when..."

A Part B question that could be asked of any subject with no reference to the anchor is a
generic probe. Mark such questions **[UNANCHORED]**.

Mark one exchange per interview (Part A or Part B) **[SIGNAL MOMENT]** — the point where the
subject said something unexpected, confirming, or contradictory — with one sentence on why
it matters.

---

**Evidence extraction** (after the transcript):

- 1–3 evidence items per subject
- Each item: verbatim quote → signal type (`risk` / `preference` / `constraint` /
  `validation` / `invalidation`) → strength (`strong` / `moderate` / `weak`) → strength
  rationale (one sentence naming the source, circumstance, or specificity)
- For each item: was it surface in Part A or Part B? Does the Anchor Statement change how you
  read a Part B item that builds directly on Part A context?

---

### Cross-Interview Synthesis (after all subjects)

1. **Anchoring quality**: For each subject, did Part B questions make genuine contact with the
   Anchor Statement, or were they generic probes? Name any [UNANCHORED] exchanges and note
   whether they appear in the extraction as evidence items — an UNANCHORED item has reduced
   evidential standing because its grounding in the subject's established position cannot be
   verified.
2. **Contradiction surface**: Where do subjects' evidence items conflict? Name the specific
   quotes or items in tension. State the nature of the conflict.
3. **Arc signal**: If subjects span dispositions, what changed from first to last? Did
   hypothesis-phase reactions build on the reality-phase baselines the anchors captured?
4. **Net verdict**: Support / Refute / Unresolved — confidence high / medium / low — one
   sentence. If an UNANCHORED exchange is a key evidence item, note its reduced standing in
   the rationale.

---

## V-03 — Phrasing Register / Verdict-Inverted Goal Frame

**Axis**: Phrasing register
**Hypothesis**: When the prompt opens by declaring the terminal output — "your job ends with
a net verdict; everything before it is evidence scaffolding" — the goal-orientation of the
simulation shifts from sequence-following to destination-building. The model generates subject
cards, transcripts, and extraction *toward* a declared destination rather than as a series of
tasks to complete in order. This framing enforces C-18 structurally (the verdict cannot be
omitted without the simulation being incomplete by its own stated terms) while activating C-03
and C-04 as instruments of a verdict rather than checklist checkboxes. The register is
descriptive and goal-centered rather than imperative and phase-centered. C-10 (tabular phase
gates) and C-12/C-13/C-17 (structured annotation and Part A Anchor) are N/A for this format
by design — an intentional tradeoff: goal orientation and persona voice fidelity in exchange
for structural annotation verifiability.

---

The purpose of this simulation is a net verdict on the hypothesis below. One or two sentences.
A declared direction: the evidence supports the hypothesis, challenges it, contradicts it, or
the case is genuinely inconclusive. That verdict is what makes everything that follows worth
doing. Build toward it.

**Topic**: {Topic}
**Hypothesis you are investigating**: {Signal}

---

Here is what building toward a trustworthy verdict actually requires:

You need more than one person. They should have different vantage points on the problem —
not just different opinions on the hypothesis, but different *experiences* with the domain it
touches. A practitioner who has lived the problem and a buyer who hasn't seen it up close.
Someone who would benefit from the hypothesis being true and someone who would be indifferent.

Before you put words in any of their mouths, write down who they are. Their role. What they've
seen. What they haven't seen — the specific things relevant to this hypothesis that they
simply don't have access to yet. A strong objection from someone who has never encountered the
problem your hypothesis addresses is a different kind of evidence than the same objection from
someone who has worked around it for years. The difference matters when you weigh what they
say. Write down the blank spots before the conversation starts.

Also write down whether each person is likely to be skeptical, neutral, or sympathetic to the
hypothesis — and why their background puts them there. A person whose stance you haven't
thought about before the conversation will tend to say whatever fits the moment.

The interviews themselves follow a direction. They start with where each person is today, not
with the hypothesis. "Walk me through what you actually do" before "what do you think of this
idea." The hypothesis enters as a question, not a declaration — and when it does, it enters
*from* where each person has already established themselves. If you ask someone to evaluate
the hypothesis in the abstract, you get an opinion. If you ask them to react from their current
practice, you find out what changes and what doesn't. That difference is the signal.

Each interview has at least one moment worth marking. A place where the person said something
that mattered — unexpected, or confirming, or reframing. Mark it.

After each interview, extract what actually matters for the verdict. Not the full transcript —
the 1–3 items that move the needle. What kind of signal each one is (risk, preference,
constraint, validation, or invalidation). How strong you'd rate it. And *why* — not just
"strong" but what makes it strong: was it unprompted? Verbatim? Does it come from someone
who has a declared knowledge gap about the very thing they're commenting on? The why is what
makes the rating defensible.

The synthesis is where the verdict gets built. Don't start with where everyone agreed.
Start with where they conflicted — the specific items or claims that stand in tension. Name
them. Name what kind of conflict it is. Agreement is signal; conflict is stronger signal,
and easier to miss if left unnamed.

Then issue the verdict.

It is one or two sentences. It names a direction: supports, challenges, contradicts, or
inconclusive. It cites the weight that determined the direction. It does not say "there are
factors on both sides." It commits. The team reads it and knows what to do next.

Note: this format is conversational by design. Tabular phase gates, per-item annotation
tables, and the Part A Anchor mechanism are N/A for this register — an intentional tradeoff
for voice fidelity and goal orientation. C-10, C-12, C-13, and C-17 are N/A.

---

**For each person you interview, write:**

*Before the conversation:* role, what they know, their blind spots specific to this hypothesis
domain, their disposition on the hypothesis and why.

*The conversation itself:* Q&A that sounds like them — their vocabulary, their specific
concerns. It starts with their current reality. The hypothesis enters later. The moment that
mattered, labeled.

*What you extracted:* 1–3 items. For each: what was said, what kind of signal, how strong,
and *why* that strength rating. Does any declared blind spot change how you read this item?

---

*After all conversations:* Start with where subjects conflict — name the specific claims in
tension. Then name what holds across subjects despite that tension. Then issue the verdict.
One or two sentences. A direction. The simulation is not complete without it.

---

## V-04 — Combined: Output Format + Lifecycle Emphasis / Epistemic Weight + Part A Anchor

**Axes**: Output format (Epistemic Weight column in evidence table, C-16), Lifecycle emphasis
(Part A Anchor step between Part A and Part B, C-17)
**Hypothesis**: Two of the three new v4 criteria can be enforced simultaneously by structural
mechanisms that are fully independent — neither requires the other to function. The Part A
Anchor enforces C-17 at the transcript phase without touching the evidence table format. The
Epistemic Weight column enforces C-16 at the extraction phase by operationalizing the subject
card's "Doesn't know" field into a per-row table annotation. Together, they close two gaps
that prior rounds left open: the gap between *declaring* blind spots (identity block) and
*using* blind spots (extraction), and the gap between *ordering* questions (C-15) and
*binding* the second phase to the first (C-17). Neither gap is closed by the other axis;
removal of either axis leaves its criterion at risk. The combination produces a simulation
where epistemic standing is declared upfront, carried through the interview structure as
an Anchor, and operationalized in extraction as an evidence weight.

---

Simulate stakeholder interviews on the hypothesis below. For each subject, an Anchor Statement
is required between Part A and Part B, and the evidence table includes an Epistemic Weight
column referencing the subject's declared blind spots.

**Topic**: {Topic}
**Hypothesis**: {Signal}

---

### Phase 1 — Subject Setup

Complete all subject cards before any transcript begins.

**Subject card format:**

- **Role and title**
- **Knows**: what this person knows about the domain, the product, or the problem — 2–3
  sentences, stated before any questions
- **Doesn't know (blind spots)**: what this person has NOT seen, experienced, or been briefed
  on — specific to the hypothesis domain. Generic entries ("they can't know everything") do
  not pass. Name at least one specific thing directly relevant to the hypothesis.
- **Primary concerns**: 2–3 things they care most about in this area, given their role
- **Disposition**: skeptic / neutral / champion — one sentence explaining why their background
  places them here

**Phase 1 gate**: Do not begin any transcript until all subject cards carry a populated,
specific "Doesn't know" field. Blind spots declared here will be referenced in the evidence
table at Phase 3.

---

### Phase 2 — Interview Transcripts

For each subject, run two labeled parts with an Anchor Statement between them.

**Part A — Current Reality** (2–3 questions)

Do not name the hypothesis, the proposed feature, or any change. Establish the subject's
current experience and practice. A Part A question that names or implies the hypothesis fails
this section.

**Part A Anchor** (written by the interviewer — not a question)

After the final Part A answer, write this before proceeding to Part B:

> **Anchor**: [Subject name] has established that: [1–2 sentences — the interviewer's summary
> of the current position, practice, or concern the subject named in Part A. This is the stance
> from which they will now react to the hypothesis.]

Do not begin Part B until the Anchor is written.

**Part B — Hypothesis Probe** (3–4 questions)

Introduce the hypothesis. Each Part B question must reference the Anchor Statement — asking
the subject to react from their established position, not a generic stance.

If any Part B question makes no contact with the Anchor, mark it **[UNANCHORED]**.

Mark one exchange per interview **[SIGNAL MOMENT]** with one sentence on why it matters.

**Phase 2 gate**: Every subject must have a complete Part A, a written Anchor Statement, and
at least one Part B exchange before Phase 3 begins.

---

### Phase 3 — Evidence Extraction

After each interview, fill in this table:

| Quote (verbatim) | Signal Type | Strength | Strength Rationale | Epistemic Weight |
|------------------|-------------|----------|--------------------|-----------------|
| "..." | `risk` / `preference` / `constraint` / `validation` / `invalidation` | `strong` / `moderate` / `weak` | Why this rating? Name source type, circumstance, or specificity. | `full` / `discounted` / `amplified` |

**Epistemic Weight definitions:**
- `full`: no relevant blind spot declared for this subject on this item; evidence accepted at
  full strength
- `discounted`: the subject's "Doesn't know" field names a gap directly relevant to this item;
  the evidence is present but carries reduced weight because the subject lacks direct experience
  with what they are commenting on — name which blank spot applies
- `amplified`: the subject's "Knows" field declares direct relevant experience that strengthens
  this item beyond role alone — name what experience applies

Rules:
- Epistemic Weight must reference the "Doesn't know" or "Knows" field from the Phase 1 card —
  not a fresh claim invented at extraction
- Strength Rationale is required on every row and must name the *why*
- Minimum 1 row per subject, maximum 3 rows

**Phase 3 gate**: Every subject must have at least one complete evidence table row with all
five columns populated before Phase 4 begins.

---

### Phase 4 — Synthesis

1. **Contradiction surface**: Where do subjects' evidence items conflict? Name at least one
   pair of specific quotes or table rows in tension. State the nature of the conflict:
   factual disagreement, priority inversion, or irreconcilable constraint.
2. **Epistemic weighting pass**: Which evidence items are discounted due to a relevant blind
   spot? Which are amplified? Does re-weighting the discounted items change the direction of
   the verdict?
3. **Anchor quality check**: For each subject, did Part B questions make genuine contact with
   the Anchor Statement? Name any [UNANCHORED] exchanges. An UNANCHORED evidence item has
   reduced standing because its grounding in the subject's established position cannot be
   verified.
4. **Arc signal**: If subjects span dispositions, trace what changed across the arc.
5. **Net verdict**: Support / Refute / Unresolved — confidence high / medium / low — one
   sentence citing the highest-weight evidence item (accounting for epistemic discounting and
   anchor quality) and its signal type.

---

## V-05 — Combined: All Three New v4 Criteria / C-16 + C-17 + C-18

**Axes**: Output format (blind-spot-forward subject card + Epistemic Weight column, C-16),
Lifecycle emphasis (Part A Anchor mechanism, C-17), Phrasing register (verdict-inverted
opening, C-18)
**Hypothesis**: The three new v4 criteria form a causal chain that prior rounds did not close:
declaring blind spots (C-16) enables evidence weighting at extraction; anchoring Part B to
Part A (C-17) makes hypothesis-phase reactions falsifiable rather than free-floating; issuing
a terminal net verdict (C-18) makes the artifact actionable rather than merely informative.
Each criterion does independent structural work — the card format enforces C-16, the Anchor
Statement enforces C-17, the verdict-inverted opening enforces C-18. No criterion depends on
the others; removal of any one axis leaves its criterion at risk. Combined, they close three
gaps simultaneously: the epistemic standing gap (who is qualified to say what they said), the
anchoring gap (are hypothesis reactions grounded in declared reality), and the actionability
gap (does the artifact produce a decision or just a report). The verdict-inverted opening is
the register choice that makes C-18 feel like a destination rather than a checklist item — it
reframes the entire simulation as scaffolding toward a committed output.

---

Your terminal output is a net verdict on the hypothesis below. One or two sentences. A
declared direction: the evidence supports the hypothesis, challenges it, contradicts it, or
the case is genuinely inconclusive. That verdict is the purpose of this simulation.
Everything that follows — subject cards, transcripts, evidence tables, synthesis — is evidence
scaffolding. The simulation is not complete until the verdict is issued.

**Topic**: {Topic}
**Hypothesis**: {Signal}

---

### Phase 1 — Subject Setup

Complete all subject cards before any transcript begins.

**Subject card format:**

- **Role and title**
- **Knows**: 2–3 sentences on what this person has seen, done, or been briefed on — specific
  to the hypothesis domain
- **Doesn't know (blind spots)**: 2–3 sentences on what this person has NOT seen, has NOT
  experienced, or has NOT been told — specific to the hypothesis domain. Name at least one
  thing directly relevant to the hypothesis. Generic entries do not pass this field.
- **Primary concerns**: 2–3 things they care most about given their role
- **Disposition**: skeptic / neutral / champion — one sentence explaining why their background
  places them here

**Phase 1 gate**: Do not begin any transcript until all subject cards carry a populated,
specific "Doesn't know" field. A strong objection from a subject with a declared relevant
blind spot carries different downstream weight than the same objection from a fully informed
expert. This distinction must be established before any question is posed.

---

### Phase 2 — Interview Transcripts

For each subject, the interview runs in two labeled parts with a required Anchor Statement
between them.

**Part A — Current Reality** (2–3 questions)

These questions establish where the subject is today. They must not name the hypothesis, the
proposed feature, or any change. A Part A question that names or implies the hypothesis fails
this section.

Good Part A openers: "Walk me through how you handle [problem domain] today," "What does the
current setup look like from your perspective," "Where does this break down most often for
you right now?"

---

**Part A Anchor** (written by the interviewer — not a question)

After the final Part A answer, write the Anchor Statement before beginning Part B:

> **Anchor**: [Subject name] has established that: [1–2 sentences summarizing the position,
> practice, or concern the subject named in Part A. This is the stance from which they will
> now react to the hypothesis.]

**Do not begin Part B until this anchor is written.** The anchor is what makes the transition
from Part A to Part B an evidence progression rather than a topic change. Without it, Part B
is hypothesis evaluation in the abstract — the subject's current-reality context is lost the
moment the hypothesis enters.

---

**Part B — Hypothesis Probe** (3–4 questions)

Introduce the hypothesis. Every Part B question must reference the Anchor Statement —
explicitly asking the subject to react from the position they established in Part A.

Acceptable anchoring language: "Given what you described about [anchor content]...", "You
said [anchor summary] — with that as your starting point...", "React from where you are: if
[anchor content] is your current reality, what changes when..."

A Part B question that could be asked of any subject with no reference to their specific
anchor is a generic probe. Mark such questions **[UNANCHORED]**.

Mark one exchange per interview **[SIGNAL MOMENT]** — something unexpected, confirming, or
contradictory — with one sentence on why it matters.

**Phase 2 gate**: Every subject must have a complete Part A, a written Anchor Statement, and
at least one Part B exchange before Phase 3 begins.

---

### Phase 3 — Evidence Extraction

After each interview, fill in this table:

| Quote (verbatim) | Signal Type | Strength | Strength Rationale | Epistemic Weight |
|------------------|-------------|----------|--------------------|-----------------|
| "..." | `risk` / `preference` / `constraint` / `validation` / `invalidation` | `strong` / `moderate` / `weak` | Why this rating? Name the source type, circumstance, or specificity — not "strong because important." | `full` / `discounted` / `amplified` |

**Epistemic Weight:**
- `full`: no declared relevant blind spot on this item; evidence accepted at full strength
- `discounted`: the subject's "Doesn't know" field names a gap directly relevant to this item;
  weight reduced because the subject lacks direct experience with what they are asserting —
  name which specific blank spot applies
- `amplified`: the subject's "Knows" field declares direct relevant experience that strengthens
  this item beyond role alone — name what experience makes this stronger

Rules:
- Strength Rationale is required; must name *why* — source type, circumstance, or specificity
- Epistemic Weight must reference the "Doesn't know" or "Knows" field from Phase 1 — not a
  new claim invented at extraction
- Minimum 1 row per subject, maximum 3 rows

**Phase 3 gate**: Every subject must have at least one complete table row with all five columns
populated before Phase 4 begins.

---

### Phase 4 — Synthesis

Write sections in this order. Do not skip or reorder.

**4A — Contradiction Surface** (required before 4B)

Name at least one point where subjects' evidence items directly conflict. For each:
- Quote or reference the specific table rows in tension (by subject and partial quote)
- State the nature of the conflict: factual disagreement, priority inversion, or
  irreconcilable constraint

A synthesis with no Contradiction Surface entry has not completed Phase 4A. Move to 4B only
after at least one contradiction is named.

**4B — Signal Patterns**

- What evidence items converged across subjects despite different dispositions? Name them.
- Which evidence items are discounted by epistemic weighting? Does discounting change the
  pattern? An item that seemed to establish consensus may not survive re-weighting if the
  subject who stated it has a declared relevant blind spot.
- Were any UNANCHORED Part B exchanges among the strongest evidence items? If so, note their
  reduced evidential standing — an UNANCHORED item cannot be verified as grounded in the
  subject's declared current-reality position.

**4C — Net Verdict** (terminal output)

Issue the net verdict: one or two sentences declaring whether the aggregate interview evidence:

- **Supports** the hypothesis — evidence is predominantly validating; contradictions resolve
  in favor; discounted items do not reverse the direction
- **Challenges** the hypothesis — evidence is mixed; significant risks or constraints are named
  and not resolved by champion statements; discounting may be a factor
- **Contradicts** the hypothesis — evidence is predominantly invalidating; key assumptions
  are falsified; champion statements do not survive re-weighting
- **Is inconclusive** — evidence is insufficient or irreconcilably conflicting even after
  epistemic weighting; the contradiction surface names a tension the evidence cannot resolve

State confidence: high / medium / low.

Include: the single highest-weight evidence item (accounting for epistemic discounting), its
signal type, and whether any named contradiction from 4A changes the verdict direction.

**The simulation is not complete until this verdict is issued.** A synthesis that produces
signal patterns without committing to a direction is informative but not actionable. Issue
the verdict.

---

*End of R4 variations.*
