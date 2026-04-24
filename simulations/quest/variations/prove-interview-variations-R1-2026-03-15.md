# prove-interview — Variations V-01 through V-05

---

## V-01 — Output Format Axis
**Hypothesis**: Structuring the evidence extraction as a typed table (rather than prose) forces explicit signal labeling and makes C-04/C-08 mechanically impossible to fail. The table becomes a first-class output artifact, not an afterthought.

```
You are simulating stakeholder interviews for a feature. Your output is a
Signal artifact used downstream by the /topic: namespace.

## Setup

Topic: $TOPIC
Feature under consideration: $FEATURE_DESCRIPTION

Select 2–3 interview subjects. For each, choose a role that has a meaningfully
different relationship to this feature — different knowledge domain, different
risk exposure, different success definition.

---

## For each subject, produce the following sections in order:

### SUBJECT: [Role Title]

**Identity**
- Role: [title and organizational context]
- Stakes: [what this person gains or loses if the feature ships well or badly]
- Prior knowledge: [what they know about the problem domain, this team, this feature]
- Blind spots: [what they don't know or don't prioritize]

**Interview Transcript**

Write the interview as a Q&A exchange. The interviewer asks role-specific
questions anchored to the subject's stated concerns. At least one follow-up
question must respond directly to a prior answer — not a pre-scripted pivot.

Answers must be written in the subject's distinct voice. Use their vocabulary,
their framing, their level of technical fluency. A developer and a compliance
officer should sound nothing alike.

Mark at least one exchange with one of:
- [SURPRISING — expected: X, got: Y]
- [CONFIRMING — validates: Z]

**Evidence Table**

After the transcript, extract all signal-bearing content into this table.
Do not leave evidence implicit inside the transcript.

| # | Evidence | Signal Type | Source Turn |
|---|----------|-------------|-------------|
| 1 | [concrete insight, concern, requirement, or contradiction] | [adoption risk / feasibility concern / requirement gap / scope signal / constraint / validation] | Q[n] |

Every row must have a Signal Type. Rows without a type are invalid.

---

## After all subjects: Cross-Interview Synthesis

Write a synthesis section with:
1. **Convergences** — where multiple subjects independently raised the same concern
2. **Contradictions** — where subjects disagreed, and what the disagreement reveals
3. **Dominant signal** — one sentence naming the strongest aggregate signal from all interviews

---

## Simulation Fidelity Note

Close with a single paragraph distinguishing:
- Claims grounded in the subject's documented role knowledge or domain context
- Claims constructed for plausibility

Name at least one specific basis (e.g., "The compliance officer's framing of
audit trail requirements reflects standard SOX/HIPAA language, not documented
knowledge of this organization's specific requirements").
```

---

## V-02 — Phrasing Register Axis
**Hypothesis**: A conversational, imperative register primes the model for dialogue mode, producing more natural-sounding persona voices (C-03) because the instructions feel like stage directions rather than a formal spec.

```
Run three stakeholder interviews for this feature. Make them feel real.

Topic: $TOPIC
Feature: $FEATURE_DESCRIPTION

---

Pick three people who would actually be in the room for a decision like this.
Give each a different job, a different level of technical depth, and a different
reason to care. The most interesting interviews come from someone who's nervous
about it, someone who's excited, and someone who's skeptical for a reason they
haven't fully articulated yet.

---

For each person, do this in order:

**Who are you talking to?**
Write a short bio — not a formal persona card, just enough that the reader
knows who's in the chair: job, what they work on, what they've heard about this
feature, what they'd lose if it went wrong. Include what they *don't* know —
every real stakeholder has blind spots.

**The conversation**
Have the interview. Ask questions that come out of that specific person's
situation. Listen to their answers and follow up — at least once per interview,
let their answer take you somewhere you didn't plan to go.

Write their answers in their voice. If they're an engineer, they'll say things
engineers say. If they're a product manager, they'll talk in outcomes and
timelines. Don't let them all sound like the same AI wrote them.

Somewhere in the conversation, label one moment explicitly:

  SURPRISING — you expected [X], they said [Y]
  or
  CONFIRMING — this validates [Z]

**What did you learn?**
After the conversation, write out what you actually learned — not a summary of
what was said, but the concrete things you're taking forward:

- A specific concern that changes how you'd scope something
- A requirement you didn't know existed
- A signal that the feature is or isn't the right solution

Tag each item with what kind of signal it is:
adoption risk | feasibility concern | requirement gap | scope signal | constraint | validation

---

After all three interviews, step back. What do the conversations add up to?
Where did multiple people land on the same thing? Where did they contradict
each other, and what does that contradiction mean? Write one sentence that
names the strongest single signal from the whole set.

---

One last thing: note briefly which parts of these interviews are grounded in
real domain knowledge or documented context, and which parts are plausible
constructions. The reader should know what to trust and what to verify.
```

---

## V-03 — Lifecycle Emphasis Axis
**Hypothesis**: Hard, numbered phase gates with explicit "do not proceed" instructions prevent the most common failures — skipping prior knowledge (C-02) and leaving evidence implicit in the transcript (C-04). Gate friction is load-bearing.

```
Simulate stakeholder interviews for the following feature.

Topic: $TOPIC
Feature: $FEATURE_DESCRIPTION

This skill runs in five mandatory phases. Complete each phase fully before
starting the next. Do not merge phases. Each phase has a defined output
boundary — stop writing one phase's content when you hit the next header.

---

### PHASE 1 — SUBJECT SELECTION

Select 2–3 interview subjects. For each, declare:
- Role and organizational level
- Relationship to this feature (user, gatekeeper, downstream consumer, sponsor)
- Why this role produces a meaningfully different signal than the others

Do not write any interview content in this phase.

**Gate**: All subjects declared → proceed to Phase 2.

---

### PHASE 2 — PRE-INTERVIEW BRIEFING

For each subject, write their pre-interview profile:

1. **Prior knowledge**: What do they know about the problem domain? About this team? About this specific feature (if anything)?
2. **Blind spots**: What are they likely unaware of or indifferent to?
3. **Stakes**: What does success or failure of this feature mean for their work?
4. **Expected concerns**: Based on their role and knowledge, what do you predict they will raise?

Write the expected concerns explicitly — they will be referenced in Phase 5 when labeling SURPRISING vs. CONFIRMING moments.

**Gate**: Pre-interview profiles complete for all subjects → proceed to Phase 3.

---

### PHASE 3 — INTERVIEW TRANSCRIPTS

For each subject, write the full interview transcript.

Rules:
- Questions must be anchored to the subject's declared role and prior knowledge — not generic feature questions
- At least one follow-up question per interview must respond directly to a prior answer
- Answers must be written in the subject's distinct voice — vocabulary, technical fluency, and framing must match their profile
- Answers that could belong to any role fail the voice test

Do not extract evidence in this phase. Do not label moments in this phase.
Write only the dialogue.

**Gate**: All transcripts complete → proceed to Phase 4.

---

### PHASE 4 — EVIDENCE EXTRACTION

For each subject, return to the transcript and extract every signal-bearing item.
This is a dedicated extraction pass — do not assume the reader will find evidence
inside the dialogue.

For each item:
- State the evidence concretely (not a paraphrase of the question — the actual insight, concern, or finding)
- Assign a signal type: adoption risk | feasibility concern | requirement gap | scope signal | constraint | validation
- Reference the transcript turn it came from

Minimum one evidence item per subject. Unlabeled items are invalid.

**Gate**: Evidence extracted and typed for all subjects → proceed to Phase 5.

---

### PHASE 5 — SYNTHESIS AND CALIBRATION

**Moment labeling**: Return to each interview transcript and mark at least one moment per subject:
- SURPRISING — expected: [predicted concern], got: [actual response]
- CONFIRMING — validates: [predicted concern]

**Cross-interview synthesis**:
- Convergences: Where did multiple subjects raise the same concern independently?
- Contradictions: Where did subjects disagree? What does the disagreement reveal?
- Dominant signal: One sentence. The strongest aggregate signal from all interviews combined.

**Simulation fidelity note**: Identify which claims are grounded in documented domain knowledge or role context, and which are plausible constructions. Name at least one specific basis for a grounded claim.
```

---

## V-04 — Combined: Role Sequence (Skeptic-First) + Inertia Framing
**Hypothesis**: Leading with the most skeptical subject and explicitly framing the status-quo competitor (what people are doing today without this feature) surfaces more SURPRISING moments and adversarial concerns, improving C-05 depth and producing richer C-09 synthesis.

```
Simulate stakeholder interviews for the following feature.

Topic: $TOPIC
Feature: $FEATURE_DESCRIPTION

---

## Status-Quo Baseline (establish this first)

Before running any interview, define what stakeholders are doing today without
this feature. This is the inertia baseline — the incumbent workflow, tool, or
workaround that this feature must displace.

Write 2–4 sentences:
- What is the current approach?
- What does it cost (time, error rate, coordination overhead)?
- What would it take for a stakeholder to abandon it?

Every interview question and every evidence item should be read against this
baseline. A feature that doesn't beat the status quo won't get adopted.

---

## Interview Order: Skeptic First

Run interviews in this sequence:

1. **The Skeptic** — someone with the most to lose or the most reasons to doubt
2. **The Champion** — someone who wants this feature to exist
3. **The Uninformed** — someone adjacent who hasn't formed an opinion yet

Starting with the Skeptic surfaces adversarial concerns early. The Champion's
enthusiasm becomes more meaningful when it follows the Skeptic's objections.
The Uninformed subject reveals what the feature looks like without context.

---

## For each subject:

**Identity and Stakes**
- Role and organizational context
- Position relative to the status-quo baseline: Do they benefit from the current approach? Are they neutral? Have they already invented a workaround?
- Prior knowledge of the problem domain and this feature
- Blind spots

**Interview Transcript**

Lead with questions that probe their relationship to the status quo:
- Why do they use the current approach?
- What would have to be true for them to switch?
- What have they already tried?

At least one question per interview must directly compare this feature to the
incumbent approach. Answers in the subject's distinct voice.

Mark at least one exchange:
- [SURPRISING — expected: X against status quo, got: Y]
- [CONFIRMING — validates: Z about adoption barrier or benefit]

**Evidence Extraction**

Extract all signal-bearing items with signal type tags:
adoption risk | feasibility concern | requirement gap | scope signal | constraint | validation | inertia barrier

The `inertia barrier` type is specific to this skill run — it marks evidence
that reveals why the status quo is sticky and what threshold this feature must
clear.

---

## Cross-Interview Synthesis

After all three interviews:

1. **Inertia map**: What are the top 2–3 reasons stakeholders might not switch?
   For each, which subject raised it and what would overcome it?

2. **Champion / Skeptic gap**: What did the Champion believe that the Skeptic
   directly contradicted? Who is more likely right and why?

3. **Uninformed signal**: What did the Uninformed subject reveal that the
   Champion and Skeptic both missed?

4. **Adoption readiness verdict**: Based on aggregate signals, is this feature
   positioned to displace the status quo? Name the single biggest blocker.

---

## Simulation Fidelity Note

Note which parts of the interviews are grounded in documented domain knowledge
and which are constructed for plausibility. Flag any place where the skeptic's
objections are generic rather than role-specific — generic skepticism is a
simulation failure mode for this variation.
```

---

## V-05 — Combined: Output Format (Structured) + Phrasing Register (Technical/Formal)
**Hypothesis**: Formal technical language combined with structured section headers and labeled fields produces the most consistently signal-typed evidence (C-08) while enforcing persona declaration (C-01/C-02). The structured format makes rubric criteria mechanically checkable.

```
## Skill: prove-interview
## Version: structured-formal
## Topic: $TOPIC
## Feature: $FEATURE_DESCRIPTION

This skill produces a set of simulated stakeholder interviews. Each interview
is a grounded simulation: answers are constructed in the declared persona's
voice based on documented role knowledge and domain context, not generic
stakeholder approximations.

Output format is structured. Each section is labeled. Downstream consumers
(primarily /topic: skills) should parse evidence tables directly.

---

## Section 1: Subject Registry

Declare all interview subjects before running any interview.

For each subject:

```
SUBJECT-ID: [S-01, S-02, ...]
ROLE: [title, team, organizational level]
RELATIONSHIP-TO-FEATURE: [primary user | gatekeeper | downstream consumer |
  budget owner | compliance reviewer | technical reviewer | other]
PRIOR-KNOWLEDGE:
  - Domain knowledge: [what they know about the problem space]
  - Feature awareness: [what they know about this specific feature, if anything]
  - Team knowledge: [what they know about the team building it]
BLIND-SPOTS: [what they are likely unaware of or indifferent to]
PREDICTED-CONCERNS: [2–3 specific concerns this subject is expected to raise,
  based on their role and knowledge — these will be referenced in moment labeling]
```

Minimum 2 subjects required. Subjects must have meaningfully different roles,
knowledge levels, or success criteria. Near-identical subjects are invalid.

---

## Section 2: Interview Transcripts

For each subject (in declared order):

```
INTERVIEW: [S-ID] — [Role Title]

TRANSCRIPT:
Q1: [question anchored to subject's declared role and prior knowledge]
A1: [answer in subject's distinct voice — vocabulary and framing must match
    declared role; generic answers fail]

Q2: [question anchored to subject's stated role and knowledge]
A2: [answer]

[Follow-up question]: [at least one Q must explicitly follow from a prior A
within this interview; label it FU-Q[n] to indicate its origin]
FU-Q[n]: [follow-up question]
A: [answer]

[Continue until the interview is substantively complete]

MOMENT-LABELS:
  [SURPRISING — expected: {predicted concern from Section 1}, got: {actual response}, turn: Q[n]]
  or
  [CONFIRMING — validates: {predicted concern from Section 1}, turn: Q[n]]
  (minimum one label per subject; both types permitted)
```

---

## Section 3: Evidence Registry

For each subject, extract all signal-bearing content into the evidence registry.
This is a mandatory extraction phase — evidence not listed here is not evidence.

```
EVIDENCE-REGISTRY: [S-ID] — [Role Title]

| EV-ID | Evidence Statement | Signal Type | Confidence | Source Turn |
|-------|-------------------|-------------|------------|-------------|
| EV-01 | [concrete insight, concern, requirement, or contradiction — not a
          paraphrase of the question] | [signal type] | [high / medium / speculative] | Q[n] |

Signal Type taxonomy:
  adoption-risk       — evidence that adoption will be lower than expected
  feasibility-concern — evidence that the feature is harder to build than assumed
  requirement-gap     — evidence that a requirement is missing or misspecified
  scope-signal        — evidence that scope is too large, too small, or misaligned
  constraint          — a hard limit (regulatory, technical, organizational)
  validation          — evidence that confirms a design assumption
```

Minimum 1 evidence item per subject. All items require Signal Type. Items
without Signal Type are invalid and must be corrected before output is complete.

---

## Section 4: Cross-Interview Synthesis

```
SYNTHESIS:

CONVERGENCES:
  [List topics where ≥2 subjects independently raised similar concerns.
   For each: name the topic, the subjects, and the aggregate strength.]

CONTRADICTIONS:
  [List topics where subjects held opposing positions.
   For each: name the disagreement and what it reveals about the feature risk.]

COMPOSITE-SIGNAL:
  [One sentence. The strongest aggregate signal from all interviews combined.
   Format: "The interviews indicate [finding], driven by [evidence IDs].]"
```

---

## Section 5: Simulation Fidelity Annotation

```
FIDELITY:

GROUNDED-CLAIMS:
  [List specific claims that are anchored in documented role knowledge or
   domain context. For each, name the basis.]

CONSTRUCTED-CLAIMS:
  [List specific claims that are plausible constructions without a documented
   basis. These require downstream verification before being treated as evidence.]

FIDELITY-VERDICT: [high / partial / low]
  [One sentence justification]
```
```

---

## Variation Summary

| ID | Primary Axis | Secondary Axis | Key Hypothesis |
|----|-------------|----------------|----------------|
| V-01 | Output format (table-first evidence) | — | Table structure makes C-04/C-08 mechanically enforceable |
| V-02 | Phrasing register (conversational) | — | Dialogue-mode priming improves C-03 persona voice naturalness |
| V-03 | Lifecycle emphasis (hard phase gates) | — | Gate friction prevents C-02/C-04 skip failures |
| V-04 | Role sequence (skeptic-first) | Inertia framing (status-quo explicit) | Adversarial ordering + incumbent baseline surfaces more SURPRISING moments |
| V-05 | Output format (structured/labeled) | Phrasing register (formal/technical) | Formal structure + typed fields maximizes C-08 compliance and downstream parseability |
