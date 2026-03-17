## prove-interview Variations — Round 4 (v4 Rubric)

---

## V-01 — Axis: Role Sequence
**Hypothesis:** Declaring sequence strategy as a named architectural decision (SKEPTIC → NEUTRAL → CHAMPION) forces the author to commit before writing, making C-19 structurally inevitable and producing richer objection evidence.

```markdown
# prove-interview

Simulate structured stakeholder interviews for the feature or topic in context.
This skill produces a signal artifact grounded in persona knowledge and concern — not a real
conversation, but a disciplined simulation of one.

---

## Sequence Strategy (declare before writing)

Your first output line must be:

> **Interview sequence**: SKEPTIC → NEUTRAL → CHAMPION.
> Rationale: skeptic-first surfaces objections before advocates can anchor the narrative.
> Neutral follows to calibrate without the skeptic's shadow. Champion closes to complete
> the evidence range and test whether early objections were addressed.

This declaration is non-negotiable. If you cannot identify a clear skeptic, label the most
resistant subject SKEPTIC and explain the classification.

---

## Step 1 — Expectation Register

Before any interview: write down what you expect each subject to say.

For each subject:

```
SUBJECT: [Role/Title]
DISPOSITION: [SKEPTIC | NEUTRAL | CHAMPION]
EXPECTED POSITION: [one sentence — what do you expect them to say about this feature?]
EXPECTED CONCERNS: [the objections or questions you anticipate]
EXPECTED SURPRISES: [what would genuinely surprise you coming from this role?]
```

Do not begin any interview transcript until all subject rows are complete.
The register is the proof that C-05 labels are honest, not retroactive.

---

## Step 2 — Subject Cards (ordered SKEPTIC → NEUTRAL → CHAMPION)

For each subject, in declared sequence:

```
SUBJECT: [Name or role title]
SEQUENCE POSITION: [1 of N — SKEPTIC | 2 of N — NEUTRAL | 3 of N — CHAMPION]
PRIOR KNOWLEDGE: [what they know about this feature domain]
BLIND SPOTS: [what they don't know or haven't considered]
CORE CONCERN: [the single thing they care most about]
VOCABULARY SIGNATURE: [2–3 words or phrases that belong to this role's lexicon]
```

VOCABULARY SIGNATURE is mandatory. It becomes the constraint on answer voice in Step 3.

---

## Step 3 — Interview Transcripts (run in declared sequence)

For each subject:

**Opening question**: Probe the subject's declared core concern directly — not a generic
opener. The question should be answerable only by someone in this role.

**Follow-up questions**: Each follow-up must show its trigger:

> triggered by: "[exact phrase from the subject's preceding answer]"

If you cannot cite a trigger, the follow-up was pre-planned. Rewrite it or cut it.

**Answers**: Write answers using the subject's VOCABULARY SIGNATURE. If an answer could
belong to any of your three subjects without edits, rewrite it.

**Moment labels**: After each notable moment, attach:

- `SURPRISING (expected: [from register], got: [what actually emerged])`
- `CONFIRMING (validates: [from register])`
- `INCONCLUSIVE (ambiguous because: [name the ambiguity])`

Every interview needs at least one labeled moment. Unlabeled "interesting" moments fail.

---

## Step 4 — Evidence Extraction (after each interview)

Extract evidence items explicitly. Do not leave them implicit in the transcript.

```
[E-NN] [Signal type]: [finding in one sentence]
  Basis: verbatim | inferred | corroborated
  Strength: strong | moderate | weak
  Rationale: [one sentence naming why — what makes this reliable, hedged, or ambiguous?]
```

Signal types: adoption risk / feasibility concern / requirement gap / scope signal /
constraint / champion signal / contradiction.

Minimum one evidence item per subject. Items without basis and strength fail C-17/C-18.

---

## Step 5 — Cross-Interview Synthesis

After all three interviews, write a synthesis section.

Name at minimum:
- One convergence (two or more subjects pointing the same direction)
- One contradiction (subjects pointing in opposite directions)
- One cascade observation (how the skeptic's objection did or did not change by the time
  you reached the champion)

Connect individual E-NN items into a composite signal statement for the topic narrative.

---

## Step 6 — Simulation Fidelity Note

Close with:

> **Simulation fidelity**: [name one claim grounded in documented persona knowledge or domain
> context — cite the basis] / [name one element constructed for plausibility — acknowledge it]

---

## Step 7 — Voice Divergence Note

Close with:

> **Voice divergence**: Between [Subject A] and [Subject B], the concrete difference was
> [cite a specific word, phrase, or framing preference]. [Subject A] said [X]; [Subject B]
> would have said [Y].

Generic observations ("they had different roles") fail. Cite specific language.
```

---

## V-02 — Axis: Output Format (Table-Driven)
**Hypothesis:** Anchoring evidence extraction in a structured table with explicit columns for signal type, basis, and strength makes C-08/C-17/C-18 structurally unavoidable and produces artifacts directly consumable by `/topic:` skills.

```markdown
# prove-interview

Simulate structured stakeholder interviews for the feature or topic in context.
Produce all structured outputs in table format. Tables are the primary artifact.
Prose appears only in transcripts and meta-notes.

---

## Table 1 — Expectation Register

Populate before any interview begins.

| Subject | Role | Disposition | Expected Position | Expected Concerns | Expected Surprise |
|---------|------|-------------|------------------|-------------------|--------------------|
| [name]  | [title] | SKEPTIC / NEUTRAL / CHAMPION | [one sentence] | [key objections] | [what would surprise you] |

Gate: do not proceed to interviews until this table has one complete row per subject.
"Complete" means all six columns filled with non-placeholder content.

---

## Table 2 — Subject Registry

For each subject:

| Field | Value |
|-------|-------|
| Name / Role | [title] |
| Disposition | SKEPTIC / NEUTRAL / CHAMPION |
| Prior Knowledge | [what they know] |
| Blind Spots | [what they don't know] |
| Core Concern | [the one thing they care most about] |
| Vocabulary Signature | [2–3 role-specific terms] |
| Interview Order | [N of M — justify the position] |

Repeat Table 2 for each subject. Order justification (last row) must name *why* this
subject appears at this position in the sequence, not just state the position.

---

## Interview Transcripts

Prose section — one per subject, in declared registry order.

Interview structure:
1. **Q1**: Probe the subject's Core Concern. Write the question as if only this role
   could answer it.
2. **Q2+**: Each follow-up prefixed with `triggered by: "[exact phrase]"` from the
   subject's prior answer.
3. **Answers**: Use Vocabulary Signature terms. If an answer is interchangeable across
   subjects, rewrite it.
4. **Moment labels** (inline after relevant exchange):
   - `SURPRISING (expected: [register entry], got: [actual])`
   - `CONFIRMING (validates: [register entry])`
   - `INCONCLUSIVE (ambiguous because: [named ambiguity])`

---

## Table 3 — Evidence Register

Populate after all interviews are complete.

| ID | Signal Type | Finding | Basis | Strength | Rationale | Subject |
|----|-------------|---------|-------|----------|-----------|---------|
| E-01 | adoption risk / feasibility concern / requirement gap / scope signal / constraint / champion signal / contradiction | [one-sentence finding] | verbatim / inferred / corroborated | strong / moderate / weak | [one sentence: why this rating?] | [subject name] |

Rules:
- Minimum one row per subject.
- Every row must have Signal Type, Basis, Strength, and Rationale.
- Rows missing any column are counted as failing C-08, C-17, or C-18 respectively.

---

## Table 4 — Synthesis Matrix

After all interviews:

| Dimension | Finding | Evidence IDs |
|-----------|---------|--------------|
| Convergence | [two+ subjects pointing same direction] | E-XX, E-XX |
| Contradiction | [subjects pointing opposite directions] | E-XX, E-XX |
| Dominant signal | [the strongest single composite signal for the topic] | E-XX, E-XX |
| Composite confidence | strong / moderate / weak | — |

---

## Table 5 — Voice Divergence Audit

| Subject A | Subject B | Concrete Difference | A's phrase | B's equivalent phrase |
|-----------|-----------|--------------------|-----------|-----------------------|
| [name]    | [name]    | [what distinguishes them] | "[exact words]" | "[exact words]" |

One row minimum. Generic role differences ("they had different priorities") fail.
Cite exact language from the transcripts above.

---

## Simulation Fidelity Note

Close with one prose paragraph:

> **Simulation fidelity**: [name one grounded claim with basis] / [name one constructed
> element, acknowledged as constructed]
```

---

## V-03 — Axis: Lifecycle Emphasis (Explicit Phase Gates)
**Hypothesis:** Making phase completion gates explicit as pass/fail checklists prevents phase-skipping under pressure and makes C-20 structurally inevitable without adding prose overhead.

```markdown
# prove-interview

Simulate structured stakeholder interviews for the feature or topic in context.
This skill runs in phases. Each phase ends with an explicit completion gate.
Do not advance to the next phase until the gate conditions are met.

---

## PHASE 1 — Expectation Register
*Phase criterion: C-13 (expectation pre-population) + C-05 (surprise labels)*

For each planned interview subject, write an expectation entry:

```
SUBJECT: [Role/Title]
DISPOSITION: [SKEPTIC | NEUTRAL | CHAMPION | NEUTRAL-LEANING]
EXPECTED TO SAY: [one sentence — their anticipated position]
EXPECTED CONCERNS: [objections or friction you anticipate]
EXPECTED SURPRISE: [what outcome would genuinely surprise you from this role]
```

**PHASE 1 GATE — check before continuing:**
- [ ] Every planned subject has an expectation entry
- [ ] Every entry has DISPOSITION, EXPECTED TO SAY, EXPECTED CONCERNS, EXPECTED SURPRISE
- [ ] No placeholder values ("TBD", "various concerns") remain
- [ ] Subject sequence is declared and justified (one sentence: why this order?)

Do not write subject cards or transcripts until all boxes above are checked.

---

## PHASE 2 — Subject Cards
*Phase criterion: C-01 (identity declared) + C-02 (prior knowledge scoped)*

For each subject (in declared sequence):

```
SUBJECT: [Name or role title]
SEQUENCE POSITION: [N of M] — [justify: why does this subject appear at this position?]
PRIOR KNOWLEDGE: [what they know about this feature domain — be specific]
BLIND SPOTS: [what they haven't considered or don't know they don't know]
CORE CONCERN: [the single question this subject needs answered]
VOCABULARY SIGNATURE: [2–3 words/phrases that belong to this person's lexicon]
```

**PHASE 2 GATE — check before continuing:**
- [ ] Every subject has a complete card
- [ ] Every card has PRIOR KNOWLEDGE and BLIND SPOTS (not combined into one field)
- [ ] Every card has a VOCABULARY SIGNATURE
- [ ] Subject sequence order matches Phase 1 declaration

---

## PHASE 3 — Interview Transcripts
*Phase criterion: C-03 (persona voice) + C-05 (moment labels) + C-06 (probing questions) + C-12 (follow-up origin)*

For each subject, in declared sequence:

**Opening question**: Must probe the subject's CORE CONCERN from their card.
If the opening question could be answered by any role generically, rewrite it.

**Follow-up questions**: Prefix every follow-up with:
> triggered by: "[exact phrase from the subject's preceding answer]"

If you cannot cite a trigger, the question was not a genuine follow-up. Cut or rewrite.

**Answers**: Use the subject's VOCABULARY SIGNATURE. Answers that don't use any signature
vocabulary should be flagged and revised.

**Moment labels** (attach inline to each notable exchange):
- `SURPRISING (expected: [from Phase 1 entry], got: [what emerged])`
- `CONFIRMING (validates: [from Phase 1 entry])`
- `INCONCLUSIVE (ambiguous because: [name the ambiguity])`

Every interview must have at least one labeled moment.

**PHASE 3 GATE — check before continuing:**
- [ ] Every subject has an opening question anchored to their CORE CONCERN
- [ ] Every follow-up shows its trigger citation
- [ ] Every answer uses at least one VOCABULARY SIGNATURE term
- [ ] Every interview has at least one labeled moment (SURPRISING / CONFIRMING / INCONCLUSIVE)
- [ ] SURPRISING and CONFIRMING labels reference Phase 1 expectation entries, not new ones

---

## PHASE 4 — Evidence Extraction
*Phase criterion: C-04 (explicit extraction) + C-08 (signal typed) + C-17 (strength rated) + C-18 (basis declared)*

After each interview, extract evidence items. Do not leave evidence implicit in the
transcript — it must appear here as a discrete item.

```
[E-NN] [Signal type]: [finding]
  Basis: verbatim | inferred | corroborated
  Strength: strong | moderate | weak
  Rationale: [one sentence — why this strength rating? what makes it reliable or hedged?]
```

Signal types: adoption risk / feasibility concern / requirement gap / scope signal /
constraint / champion signal / contradiction.

**PHASE 4 GATE — check before continuing:**
- [ ] Every subject has at least one evidence item
- [ ] Every evidence item has Signal Type
- [ ] Every evidence item has Basis (verbatim / inferred / corroborated)
- [ ] Every evidence item has Strength AND a Rationale sentence
- [ ] No evidence item is referenced only within the transcript (it must appear here explicitly)

---

## PHASE 5 — Cross-Interview Synthesis
*Phase criterion: C-09 (cross-interview synthesis)*

Write a synthesis section covering:
1. Convergence — two or more subjects pointing the same direction (cite E-NN items)
2. Contradiction — subjects pointing in opposite directions (cite E-NN items)
3. Composite signal — the single strongest takeaway for the topic narrative
4. Composite confidence — strong / moderate / weak, with one-sentence justification

**PHASE 5 GATE — check before continuing:**
- [ ] Synthesis cites specific E-NN items, not paraphrases
- [ ] At least one convergence and one contradiction are named
- [ ] Composite signal is a single declarative statement
- [ ] (N/A for single-subject runs — skip Phase 5)

---

## PHASE 6 — Closing Meta-Notes
*Phase criterion: C-10 (fidelity) + C-11 (voice divergence)*

**Simulation fidelity**:
> [Name one claim grounded in documented persona knowledge or domain context — cite the
> source or basis. Name one element constructed for plausibility — acknowledge it explicitly.]

**Voice divergence**:
> Between [Subject A] and [Subject B], the concrete voice difference was: [Subject A]
> used "[exact phrase]" — [Subject B] would have said "[contrasting phrase]" because
> [one sentence explaining the role-based reason].

**PHASE 6 GATE:**
- [ ] Fidelity note names both a grounded claim and a constructed element
- [ ] Voice divergence cites exact language from the transcripts, not role labels
```

---

## V-04 — Combined: Skeptic-First + Table Format
**Hypothesis:** The combination of skeptic-first sequencing (V-01) with table-driven evidence extraction (V-02) produces the highest-density skepticism signal in a machine-consumable form — the skeptic's objections become E-NN rows that the champion must then address or contradict.

```markdown
# prove-interview

Simulate structured stakeholder interviews for the feature or topic in context.
Output format: tables for structure, prose for transcripts.
Subject sequence: SKEPTIC → NEUTRAL → CHAMPION, declared and justified.

---

## Sequence Declaration (write this first)

> **Interview sequence**: SKEPTIC → NEUTRAL → CHAMPION.
> [One sentence justifying this choice for this specific feature context — not generic.]

If you cannot identify a clear skeptic, assign the most resistant available role and note it.

---

## Table 1 — Expectation Register

Populate before any interview begins. Columns are mandatory.

| Subject | Role | Disposition | Expected Position | Expected Objections | What Would Surprise You |
|---------|------|-------------|------------------|---------------------|------------------------|
| [name]  | [title] | SKEPTIC | [one sentence] | [specific objections] | [genuine surprise] |
| [name]  | [title] | NEUTRAL  | … | … | … |
| [name]  | [title] | CHAMPION | … | … | … |

Gate: do not begin transcripts until all three rows are complete with non-placeholder content.

---

## Table 2 — Subject Registry

One table per subject, in sequence order (SKEPTIC first).

| Field | SKEPTIC | NEUTRAL | CHAMPION |
|-------|---------|---------|----------|
| Name / Role | | | |
| Prior Knowledge | | | |
| Blind Spots | | | |
| Core Concern | | | |
| Vocabulary Signature | | | |
| Sequence Justification | [why first?] | [why second?] | [why third?] |

Vocabulary Signature: 2–3 role-specific terms that must appear in that subject's answers.

---

## Interview Transcripts (SKEPTIC → NEUTRAL → CHAMPION)

For each subject:

**Opening question**: Anchored to that subject's Core Concern. Not a generic opener.

**Follow-up rule** — every follow-up prefixed with:
> triggered by: "[exact phrase from subject's prior answer]"

**Answer voice rule** — each answer must use at least one Vocabulary Signature term.
If an answer is interchangeable across subjects, flag it: `[VOICE CHECK: revise]`

**Moment labels** (inline):
- `SURPRISING (expected: [Table 1 entry], got: [actual])`
- `CONFIRMING (validates: [Table 1 entry])`
- `INCONCLUSIVE (ambiguous because: [named ambiguity])`

---

## Table 3 — Skeptic Objection Tracker

Populate after the SKEPTIC interview. Used to track whether objections are addressed,
softened, or confirmed by subsequent subjects.

| Objection | E-NN | NEUTRAL response | CHAMPION response | Resolution |
|-----------|------|-----------------|-------------------|------------|
| [skeptic's objection] | E-XX | addressed / silent / contradicts | addressed / silent / confirms | resolved / open / escalated |

---

## Table 4 — Evidence Register

Populate after all interviews.

| ID | Signal Type | Finding | Subject | Basis | Strength | Rationale |
|----|-------------|---------|---------|-------|----------|-----------|
| E-01 | adoption risk / feasibility concern / requirement gap / scope signal / constraint / champion signal / contradiction | [finding] | [SKEPTIC / NEUTRAL / CHAMPION] | verbatim / inferred / corroborated | strong / moderate / weak | [why this rating?] |

Every row needs all seven columns. Rows with gaps in Signal Type, Basis, or Strength fail.

---

## Table 5 — Synthesis Matrix

| Dimension | Finding | E-IDs | Confidence |
|-----------|---------|-------|------------|
| SKEPTIC anchor objection | [the objection that mattered most] | E-XX | strong / moderate / weak |
| Cross-subject convergence | [what all three agreed on] | E-XX, E-XX | |
| Cross-subject contradiction | [where they diverged] | E-XX, E-XX | |
| Composite signal | [single takeaway for topic narrative] | all | |

---

## Table 6 — Voice Divergence Audit

| Pair | Concrete difference | Subject A phrase | Subject B phrase |
|------|--------------------|--------------------|------------------|
| SKEPTIC vs CHAMPION | [what distinguishes them] | "[exact words]" | "[exact words]" |
| SKEPTIC vs NEUTRAL | (optional) | | |

---

## Simulation Fidelity Note (prose)

> **Simulation fidelity**: [one grounded claim + its basis] / [one constructed element,
> acknowledged as constructed]
```

---

## V-05 — Combined: Conversational Register + Inertia Framing
**Hypothesis:** Foregrounding what subjects are doing *today* (status-quo framing) before asking about the feature surfaces adoption risk signals naturally, because the persona's attachment to existing solutions shapes every answer — this is the inertia frame. A conversational register makes persona voice easier to maintain across multiple turns.

```markdown
# prove-interview

Simulate structured stakeholder interviews for the feature or topic in context.

These interviews are not surveys. They are conversations. Start with what the subject
does today — not what they think of the new feature. Their attachment to the current
solution is the signal you're hunting for.

---

## Before You Start — Three Things to Write Down

**1. The status-quo picture**
What is each subject doing today to solve the problem this feature addresses?
Name the tool, workaround, or manual step they would be replacing.
One line per subject. No subject may enter the interview without this.

```
[Subject / Role]: today they use [X] to [do Y]. They've been doing it this way [since / because Z].
```

**2. The inertia assumption**
How attached do you expect each subject to be to their current approach?
Rate: high attachment / moderate attachment / low attachment — and say why.

**3. The surprise threshold**
What would it take to genuinely surprise this subject — not impress them, but actually
catch them off-guard? One sentence per subject.

These three items are your expectation register. Write them all before any interview begins.

---

## Subject Introductions

For each subject, a short card written the way you'd brief someone before a meeting:

```
You're about to talk to [Name / Role].
They know: [prior knowledge, in plain language]
They don't know: [blind spots — what they haven't thought about]
They care most about: [core concern — what's their actual job worry]
They'll probably say: [expected position — from expectation register]
They sound like: [vocabulary note — 2–3 phrases you'll hear from them]
```

Note the interview sequence and why: why is this person going first / second / last?
One sentence per position. Arbitrary or unexplained ordering fails.

---

## The Conversations

Run each interview in declared sequence.

Start every interview the same way: ask what they're doing today.

> "Walk me through how you handle [the problem domain] right now."

Let them establish their current solution before introducing anything new.
Their investment in the current answer shapes everything they say next.

**Follow-up rule**: every question after the first one must come from something they just said.
Write it this way:

> You said "[exact phrase]" — [your follow-up question]

If a follow-up doesn't come from a specific phrase they said, it's a pre-planned question
dressed up as a follow-up. Cut it or rewrite it.

**Answer rule**: write answers in the subject's voice — their vocabulary, their worry level,
their way of framing risk. If you could swap the answer between two subjects without anyone
noticing, the voice has collapsed. Use the vocabulary note from the subject card as a constraint.

**Moment labels** (attach after the exchange that triggers them):

- `SURPRISING (expected: [from register], got: [what actually came up])`
- `CONFIRMING (validates: [from register])`
- `INCONCLUSIVE (still unclear whether [X] — because [name the ambiguity])`

Every interview needs at least one label. If every moment is either SURPRISING or CONFIRMING
and nothing is INCONCLUSIVE, explain why — don't just omit the third category.

---

## What Did You Learn?

After each interview, write a short evidence extraction. Not a summary — a list of
discrete findings that the topic narrative can use.

For each finding:

```
[E-NN] [type]: [finding in one sentence]
  Basis: verbatim (I quoted it) | inferred (I read between lines) | corroborated (two people said it)
  Strength: strong | moderate | weak
  Why this rating: [one sentence — what makes this finding reliable, hedged, or ambiguous]
```

Types: adoption risk / feasibility concern / requirement gap / scope signal /
constraint / champion signal / contradiction.

One finding minimum per subject. Findings that stay inside the transcript and aren't
extracted here are invisible to the topic narrative.

---

## Putting It Together

After all interviews, two things:

**1. The pattern read** — what do the interviews say together that no single interview said alone?
Name one convergence (subjects agreed), one contradiction (subjects disagreed), and what you
would tell the feature team right now as the single most important composite signal.

**2. The inertia verdict** — looking at the status-quo picture you wrote before you started:
how strongly did each subject defend their current solution? Did the interviews surface more
or less attachment than you expected? Name the most stubborn inertia signal found.

---

## Two Closing Notes

**Simulation fidelity**: what in these interviews is grounded in documented knowledge about
these roles or this domain, and what did you construct for plausibility? Name one of each.
Don't blend them — call them out separately.

**Voice check**: pick two subjects and name one concrete thing that made them sound different.
Not their roles — specific language. What did one say that the other would never have said?
Quote both.
```

---

### Variation Summary

| # | Primary Axis | Secondary Axis | Core Structural Bet |
|---|-------------|---------------|---------------------|
| V-01 | Role sequence (SKEPTIC → NEUTRAL → CHAMPION) | — | Sequence declared as architecture; C-19 structurally inevitable |
| V-02 | Output format (tables) | — | Evidence columns enforce C-08/C-17/C-18 without separate instruction |
| V-03 | Lifecycle emphasis (explicit phase gates) | — | Checklists prevent phase-skipping; C-20 structurally enforced |
| V-04 | Skeptic-first + table format | — | Skeptic objection tracker connects skeptic evidence to champion response |
| V-05 | Conversational register | Inertia framing | Status-quo attachment surfaces adoption risk before feature framing anchors the subject |
