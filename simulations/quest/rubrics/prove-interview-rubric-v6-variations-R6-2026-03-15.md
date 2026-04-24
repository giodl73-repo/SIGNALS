# prove-interview — Rubric v6 Variations — Round 6

_Date: 2026-03-15 · Rubric: v6 (C-01–C-18) · Ceiling: 100_

---

## Context

Round 5 produced 5 variations scored against the v5 rubric (C-01–C-15). V-04 scored 99.09–100.00
under v6 retroactive scoring; V-01 and V-03 scored 97.27; V-02 scored 94.55. The v6 rubric adds
three new aspirational criteria:

- **C-16** — Subjects selected for structural epistemic opposition (explicit pairing rationale
  naming the opposition axis, before any transcript)
- **C-17** — Synthesis elevated to arc-level signal (explicitly stated arc question wider than
  feature scope, answered by arc inference the feature evidence alone cannot support)
- **C-18** — Phase gate enforces hypothesis quality, not just hypothesis existence (gate condition
  must state "each H-ID carries a falsification condition", not merely "at least one")

Aspirational denominator: 11. Each criterion worth approximately 0.91 points. Ceiling stays 100.

**R5 coverage gaps for C-16, C-17, C-18:**

| Variation | C-16 | C-17 | C-18 | Aspirational | Composite |
|-----------|------|------|------|--------------|-----------|
| V-01 R5 (Output Format) | FAIL | FAIL | FAIL | 8/11 | 97.27 |
| V-02 R5 (Phrasing Register) | FAIL | FAIL | FAIL | 5/11 | 94.55 |
| V-03 R5 (Lifecycle Emphasis) | FAIL | FAIL | PASS | 8/11 | 97.27 |
| V-04 R5 (Lifecycle + Inertia) | PASS | PASS | PASS | 10–11/11 | 99.09–100.00 |
| V-05 R5 (Output Format + Inertia) | FAIL | FAIL | FAIL | 8/11 | 97.27 |

Round 6 goals:
1. Three single-axis variations: Role Sequence (targeting C-16), Output Format / Arc Section
   (targeting C-17), Phrasing Register (targeting all three via researcher-voice prompts)
2. Two combination variations: Role Sequence + Lifecycle (C-16 + C-18, C-17 absent as gap test);
   Inertia + Arc + Quality Gates + H-ID anchors (full combination, all three + C-12 resolution)
3. Each single-axis variation leaves the other two new criteria absent to isolate the contribution

---

## Variation Axes

| Axis | R5 result | R6 focus |
|------|-----------|----------|
| Role sequence | SECONDARY in V-04/V-05 | PRIMARY — opposition axis as STEP 0 structural section |
| Output format | PRIMARY in V-01/V-05 | Add Arc Signal section as mandatory format element |
| Lifecycle emphasis | PRIMARY in V-03 (C-18 PASS via "at least one") | Strengthen to per-hypothesis quality gate |
| Phrasing register | PRIMARY in V-02 — C-16/17/18 all fail | Add three researcher-voice prompts, one per new criterion |
| Inertia framing | PRIMARY in V-04/V-05 | Full combination with arc question + universal quality gate |

---

## V-01 — Single axis: Role Sequence

**Axis:** An "OPPOSITION AXIS DECLARATION" section precedes the Hypothesis Register and Roster.
This is a pre-interview design artifact — it names the epistemic tension axis, describes both
poles, explains what evidence requires hearing from Pole B, and assigns each roster subject to a
declared pole. The Roster references the poles. Everything else follows R5 V-01 (tabular, 5 steps).

**Hypothesis:** Elevating the pairing rationale to a first-class structural section (not a Roster
column annotation) enforces C-16 by construction — the section is a gate prerequisite for STEP 1.
C-17 and C-18 are not addressed, keeping this a single-axis test. The opposition axis column added
to the Roster makes pole assignment visible per-subject before any transcript. Predicted: C-16
PASS, C-17 FAIL, C-18 FAIL. C-12 PASS (tabular structure from R5 V-01 maintained). Aspirational
9/11, composite 98.18.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Simulate stakeholder or customer interviews about this topic. The interviews are not real — but
every persona answer must be anchored in the persona's documented identity, expertise, and prior
experience. The output is a signal artifact: structured evidence toward or against the signal
hypothesis.

---

### STEP 0 — Opposition Axis Declaration

Write this section before the Hypothesis Register. It commits the interview design before any
subjects are selected, questions are written, or hypotheses are declared.

This section is not a persona introduction. It is an epistemic design choice: the decision to
interview two subjects at opposite poles of a relevant tension axis rather than two subjects who
might agree.

| Field | Declaration |
|-------|-------------|
| **Axis name** | [Name the tension axis — e.g., "incumbent investment vs. greenfield adoption" / "adoption resistance vs. adoption readiness" / "risk-first vs. capability-first prioritization"] |
| **Why this axis for {SIGNAL}** | [One sentence: why tension on this axis produces more informative evidence for {SIGNAL} than agreement on this axis would. What question about {SIGNAL} can only be answered by hearing from both poles?] |
| **Pole A — resistant / skeptical** | [Describe the position at this pole: what does a subject here believe, what have they invested in, what would adoption of {SIGNAL} cost them?] |
| **Pole B — receptive / innovative** | [Describe the position at this pole: what does a subject here want, what have they not yet invested in, what adoption benefit would they prioritize?] |
| **Evidence requiring Pole B** | [What specific finding type cannot be obtained from a Pole A subject alone? Name the evidence the feature team would miss if both subjects occupied the same pole.] |

**Declaration rules:**
- The axis must be epistemic (a dimension of belief, practice, or expertise), not demographic
  (age, company size, geography).
- Pole A and Pole B must be genuine opposites on the named axis, not variations of the same
  position.
- "Evidence requiring Pole B" must name a specific finding type — "we would miss a perspective"
  fails; "we could not determine whether S-01's adoption conditions are specific to their
  deployment context or universal across the workflow category" passes.

**Gate**: STEP 1 (Hypothesis Register) cannot be written until this section is complete. STEP 2
(Roster) must assign each subject to a pole declared here.

---

### STEP 1 — Hypothesis Register

Write this register before any interview question or persona answer. The register is locked once
written. No question may be written without citing at least one hypothesis ID from this register.

| ID   | Hypothesis                                               | Category                    | Falsification Condition                                                         |
|------|----------------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL] | assumption / risk / unknown | [what a subject would have to say to force rejection — name the answer type]    |
| H-02 | [a specific risk or concern you expect to surface]       | risk                        | [what answer would show this risk does not apply or is overstated]              |
| H-03 | [a design question these interviews should resolve]      | unknown                     | [what finding would resolve this against your expectation]                      |
| H-04 | [add additional hypotheses — aim for at least 4]         |                             |                                                                                 |

**Register rules:**
- Minimum 4 hypotheses.
- At least one hypothesis must have a non-empty Falsification Condition naming the specific answer
  type or evidence that would force rejection. "If most people disagree" fails.
- Register is locked once written.

---

### STEP 2 — Human Subjects Roster

Assign each subject to a pole declared in STEP 0. A subject with no axis assignment is not
correctly positioned — replace them with a subject at one of the declared poles.

| ID   | Name   | Role   | Seniority | Axis Pole (STEP 0)         | Key Concern                                                     |
|------|--------|--------|-----------|----------------------------|-----------------------------------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0) | [What this persona is most likely to push back on or champion — grounded in their pole] |
| S-02 | [Name] | [Role] | [Level]   | Pole A / Pole B (from STEP 0) | [Key concern meaningfully distinct from S-01 — grounded in their pole] |

Minimum 2 subjects, one from each declared pole. If both subjects occupy the same pole, return
to STEP 0 and revise the axis declaration.

---

### STEP 3 — Interviews

**Do not write any interview table row until Steps 0, 1, and 2 are complete.** This is a
structural gate: interview rows cannot exist before the Opposition Axis, Hypothesis Register,
and Roster are committed.

For each subject in the roster:

#### [S-nn] — Identity

[2–3 sentences: company type or context, relevant prior experience, at least one concrete concern
or known event. The identity must make the subject's pole assignment legible — a reader should
understand which axis pole this subject occupies from the Identity alone.]

Swap test: substitute another persona's name into this paragraph. If the interview answers would
still read as plausible, revise before writing the table.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn]   | Answer (persona voice)                                 | Evidence Signal [type: ...]                                                           | Surprise?                        |
|-----|-------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------|----------------------------------|
| Q1  | [Question] [H-01] | [Answer — vocabulary and concerns drawn from Identity] | [risk: …] / [preference: …] / [constraint: …] / [validation: …] / [invalidation: …] — [one-sentence signal] | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn] |                                                        |                                                                                       |                                  |
| Q3  | [Question] [H-nn] |                                                        |                                                                                       |                                  |

**Table rules:**
- Every question cites at least one H-ID in brackets.
- Every answer fails the swap test — no other persona can be substituted and have the answer
  remain plausible. Generic answers that could belong to any persona fail.
- Every Evidence Signal carries a type tag followed by a one-sentence signal interpretation.
- At least one "Yes" in the Surprise column per subject, with explanation of expected vs. found.
- Minimum 3 rows per subject.

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after all subject tables are complete.

**Completion rules:**
- Every row compares at least two subjects on a shared dimension.
- Rows recording agreement must explain why the agreement is meaningful given the Hypothesis
  Register and the opposition axis declared in STEP 0.
- At least one row records an open, unresolved tension. Leave it open.
- Note whether each tension or agreement was predicted by the STEP 0 opposition axis (expected)
  or was a surprise.

| Dimension [H-ID if applicable]       | S-01 position | S-02 position | Tension or Agreement [explained]                    | Axis-predicted? | Unresolved? |
|--------------------------------------|---------------|---------------|-----------------------------------------------------|-----------------|-------------|
| [topic / concern / H-ID / axis pole] | [S-01 view]   | [S-02 view]   | TENSION: [describe] / AGREEMENT: [what it signals]  | Expected / Surprise | Yes / No |

---

### STEP 5 — Composite Signal

This section synthesizes — it does not restate. If removing this section would leave the artifact
unchanged, the section has failed. The Composite Signal must add integrated judgment beyond what
a reader can derive from the Interview Tables and Tensions Matrix row by row.

Answer all three of the following in 4–6 sentences:

1. **Integrated verdict**: Does the overall evidence strengthen, weaken, or complicate the
   original SIGNAL hypothesis? State directly.

2. **Dominant finding**: What single finding across all subjects is most decision-relevant?
   Name it specifically — a finding, not a theme.

3. **Key open question**: What is the most important thing these interviews did not resolve?
   What would the feature team need to do next?

Cite subjects by ID (S-01, S-02) and hypothesis IDs (H-nn) where relevant.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-02 — Single axis: Output Format (Arc Signal section)

**Axis:** An "ARC SIGNAL" section is appended after the Composite Signal. This section has two
required fields: (1) an arc question that explicitly names a scope wider than {SIGNAL}, and (2)
an arc inference that adds a conclusion the feature-level evidence alone cannot support. The rest
of the prompt is identical to R5 V-01 (tabular, 5 steps with no pairing rationale and no quality
gate).

**Hypothesis:** Structuring the arc synthesis as a mandatory format section with explicit arc
question and arc inference fields enforces C-17 by construction — the fields state scope and
anti-restatement tests that cannot be satisfied at feature scope. C-16 and C-18 are deliberately
absent as the single-axis test. Predicted: C-16 FAIL, C-17 PASS, C-18 FAIL. C-12 PASS (tabular
structure maintained). Aspirational 9/11, composite 98.18.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Simulate stakeholder or customer interviews about this topic. The interviews are not real — but
every persona answer must be anchored in the persona's documented identity, expertise, and prior
experience. The output is a signal artifact: structured evidence toward or against the signal
hypothesis.

---

### STEP 1 — Hypothesis Register

Write this register before any interview question or persona answer. The register is locked once
written.

| ID   | Hypothesis                                               | Category                    | Falsification Condition                                                      |
|------|----------------------------------------------------------|-----------------------------|------------------------------------------------------------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL] | assumption / risk / unknown | [what a subject would have to say to force rejection — name the answer type] |
| H-02 | [a specific risk or concern you expect to surface]       | risk                        | [what answer would show this risk does not apply]                            |
| H-03 | [a design question these interviews should resolve]      | unknown                     | [what finding would resolve this against your expectation]                   |
| H-04 | [add additional hypotheses — aim for at least 4]         |                             |                                                                              |

**Register rules:**
- Minimum 4 hypotheses.
- At least one hypothesis must have a non-empty, specific Falsification Condition.
- Register is locked once written. Do not revise after any interview table row is written.

---

### STEP 2 — Human Subjects Roster

| ID   | Name   | Role   | Seniority | Domain Expertise | Key Concern                                                     |
|------|--------|--------|-----------|------------------|-----------------------------------------------------------------|
| S-01 | [Name] | [Role] | [Level]   | [Domain]         | [What this persona is most likely to push back on or champion]  |
| S-02 | [Name] | [Role] | [Level]   | [Domain]         | [Key concern meaningfully distinct from S-01]                   |

Minimum 2 subjects with meaningfully different roles, domains, or concerns.

---

### STEP 3 — Interviews

**Do not write any interview table row until Steps 1 and 2 are complete.**

For each subject in the roster:

#### [S-nn] — Identity

[2–3 sentences: company type or context, relevant prior experience, at least one concrete concern
or known event that makes this persona specific.]

Swap test: substitute another persona's name into this paragraph. If the interview answers would
still read as plausible, revise before writing the table.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn]   | Answer (persona voice)                                 | Evidence Signal [type: ...]                                                           | Surprise?                        |
|-----|-------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------|----------------------------------|
| Q1  | [Question] [H-01] | [Answer — vocabulary and concerns drawn from Identity] | [risk: …] / [preference: …] / [constraint: …] / [validation: …] / [invalidation: …] — [one-sentence signal] | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn] |                                                        |                                                                                       |                                  |
| Q3  | [Question] [H-nn] |                                                        |                                                                                       |                                  |

**Table rules:**
- Every question cites at least one H-ID in brackets.
- Every answer fails the swap test.
- Every Evidence Signal carries a type tag followed by a one-sentence signal interpretation.
- At least one "Yes" in the Surprise column per subject with explanation.
- Minimum 3 rows per subject.

---

### STEP 4 — Cross-Subject Tensions Matrix

Write after all subject tables are complete.

| Dimension [H-ID if applicable]  | S-01 position | S-02 position | Tension or Agreement [explained]                   | Unresolved? |
|---------------------------------|---------------|---------------|-----------------------------------------------------|-------------|
| [topic / concern / H-ID]        | [S-01 view]   | [S-02 view]   | TENSION: [describe] / AGREEMENT: [what it signals]  | Yes / No    |

Completion rules:
- At least one unresolved tension row.
- Agreement rows explain why the agreement matters or is surprising.

---

### STEP 5 — Composite Signal

This section synthesizes — it does not restate. If removing this section would leave the artifact
unchanged, the section has failed.

Answer all three of the following in 4–6 sentences:

1. **Integrated verdict**: Does the evidence strengthen, weaken, or complicate the original
   SIGNAL hypothesis? State directly.
2. **Dominant finding**: What single finding is most decision-relevant? Name it specifically.
3. **Key open question**: What did these interviews not resolve? What would the feature team
   need to do next?

---

### STEP 6 — Arc Signal

**Write this section after the Composite Signal. It is required. It must not restate
feature-level conclusions from STEP 5.**

The Arc Signal answers a question whose scope is wider than {SIGNAL}. It addresses what this
interview run reveals about the adoption pattern, the workflow category, or the class of features
{SIGNAL} belongs to — not whether {SIGNAL} specifically is viable.

| Field | Content |
|-------|---------|
| **Arc question** | [State an explicit question whose scope exceeds {SIGNAL} — e.g., "What does this run tell us about how [user type] navigates [workflow category]?" Scope test: if the same question could only be answered by studying {SIGNAL} specifically, it is not an arc question. If a different but adjacent signal in the same category would generate the same arc question, the scope is correct.] |
| **Arc inference** | [State a conclusion that answers the arc question and that a reader could not reconstruct by reading the Composite Signal alone. The inference adds meaning that derives from the evidence but points beyond this specific feature.] |

**Arc scope test**: substitute a different but adjacent signal into the arc question. If the arc
question and inference would apply equally to that signal, the scope is arc-level. If rewriting
for the adjacent signal would require changing the arc question itself, the scope is still
feature-level — revise.

**Anti-restatement test**: if removing the Arc Signal section would leave the feature team with
everything they need to decide about {SIGNAL}, the Arc Signal has not elevated the synthesis.
Revise until removing the section would cost the feature team something they cannot reconstruct.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-03 — Single axis: Phrasing Register

**Axis:** Full conversational register (builds on R5 V-02) with three targeted researcher-voice
prompts — one per new criterion. (1) A "why these two?" declaration before roster selection names
the tension axis and both poles (C-16). (2) A "can I move on?" gate requires a falsification
condition for *every* hypothesis before any interview is written (C-18 — stricter than R5 V-03's
"at least one" gate). (3) A "beyond the feature" reflection after the verdict requires an arc
question and arc inference at wider-than-feature scope (C-17).

**Hypothesis:** A conversational researcher voice carries all three new criteria naturally —
researchers authentically ask "why these specific two people?", "have I tested every belief?",
and "what does this tell me beyond this feature?" The prompts feel like researcher self-checks,
not compliance fields. C-12 (H-IDs as column headers) is the predicted failure — conversational
format resists structural table columns. C-13 (explicit gate sentence) is uncertain — the "can I
move on?" prompt may or may not satisfy the strict gate sentence evaluator test. Predicted:
C-16 PASS, C-17 PASS, C-18 PASS; C-12 FAIL; C-13 UNCERTAIN. Composite 95.45–97.27.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Think of yourself as a field researcher going into a series of structured conversations to find
out what is really true about this signal. These conversations are not real — but they should
read as if they could be. Every answer comes from a specific person with a specific history,
not a generic voice that could fit anyone.

---

**Before I choose who to talk to: what is the tension?**

Before I name a single person, I need to ask: what is the most important dimension of disagreement
for testing this signal? Who would be at one extreme of that dimension, and who would be at the
other? This is not about finding agreeable voices or finding critics. It is about finding the
pair of people whose combined testimony would tell me something neither one alone could.

Write a pre-roster tension declaration:

```
Tension axis: [Name the epistemic dimension — a dimension of practice, belief, or investment
along which two subjects at opposite ends would produce genuinely different evidence about {SIGNAL}]

Why this axis: [One sentence — why does hearing from both ends of this axis matter for this
specific signal? What would I miss if both subjects were at the same end?]

Pole A (resistant / skeptical end): [Who lives here? What have they invested in? What would this
signal disrupt for them?]

Pole B (receptive / innovative end): [Who lives here? What are they looking for? What would this
signal enable for them?]
```

I will not select subjects until I have written this declaration. A subject I cannot assign to a
declared pole has no design rationale for being in this interview run.

---

**Before you talk to anyone — what do you believe right now?**

Write your current beliefs and assumptions before you write a single question. Label them H-01,
H-02, etc.

For each hypothesis, write three lines:
- *What would confirm this*: what an interviewee would have to say to strengthen this belief.
- *What would change my mind*: what you would have to hear — specifically — to conclude this
  belief is wrong. This is your falsification condition.
- *Who tests this*: which pole (Pole A or Pole B from the tension declaration) is most likely
  to surface evidence that confirms or falsifies this hypothesis.

```
H-01: I believe that [type of stakeholder] will ...
      Confirms: If I hear [answer pattern], this belief holds.
      Changes my mind: If [specific answer or finding], I would have to conclude [opposite].
      Who tests this: Pole A / Pole B / Both

H-02: My main risk is that ...
      Confirms: ...
      Changes my mind: ...
      Who tests this: ...

H-03: I expect the adoption barrier to be ...
      Confirms: ...
      Changes my mind: ...
      Who tests this: ...

H-04: I think the biggest surprise will come from ...
      Confirms: ...
      Changes my mind: ...
      Who tests this: ...
```

Write at least 4 hypotheses.

**Can I move on?** I will not write my first question until every single hypothesis — not just
one — has a concrete, non-trivial "Changes my mind" condition. A hypothesis with no falsification
condition is a belief I am not actually testing; I am only confirming it. "If most people
disagree" does not count — the condition must name what specific answer or finding would force
me to change my position on that specific hypothesis. If any H-ID has a blank or generic
falsification condition, I stay in this step until it is filled.

Do not revise these hypotheses after writing the interviews. Contradictions in the conversations
are findings, not reasons to rewrite the prior.

---

**Who are you talking to?**

Assign each person to a pole from the tension declaration before writing their background. If you
cannot assign them to a declared pole, they are not correctly positioned for this run.

For each subject, write a pre-interview note:

```
Name: [realistic invented name]
Role: [title and seniority]
Tension pole: Pole A (resistant) / Pole B (receptive)
Background: [2–3 sentences — industry, what they have worked on, what they worry about,
             a specific past event that shapes their view of this topic]
Why I'm talking to this person: [one sentence — what question only someone at their pole
can answer, that a subject at the other pole could not]
```

Identity check: if you swapped this person's name with someone else's, would the answers still
feel right? If yes, add more specifics before continuing.

Minimum 2 subjects, one at each declared pole.

---

**The conversations**

Write each interview as a flowing transcript in researcher voice. Let each person speak in their
own register — a compliance officer does not talk like a startup founder; a developer who has
been burned by API instability does not answer the same way as one who hasn't.

For each interview:
- Write at least 3 substantive questions
- After each question, note which hypothesis it tests — e.g., *(testing H-02)* — even
  just parenthetically
- When an answer surprises you — something that contradicts what you expected — write a short
  in-flow note: *"I went in expecting [X] based on [H-nn], but [Name] said [Y]. This shifts
  how I think about [Z]."*
- When a "Changes my mind" condition is triggered: *"**[FALSIFIED — H-nn]**: [Name] said [Y].
  I committed to this as my falsification condition. It is triggered."*
- At least one marked moment (surprise or falsification) per person. A conversation with zero
  surprises is a rehearsal, not an interview.

---

**What did this person actually tell you?**

After each interview, write a findings section — 3 to 5 specific things this person said that
could influence a feature decision. Not summaries. Findings — concrete, actionable, specific
enough that someone who did not read the transcript could act on them.

Pole check: each finding should carry the specific color of this person's declared pole. A finding
that could equally come from either pole is not pole-specific evidence — sharpen it.

---

**What do the conversations together tell you?**

After all interviews are written, write a Comparison section. Required table.

| What I examined         | [Pole A subject] | [Pole B subject] | What the difference (or similarity) means                    |
|-------------------------|------------------|------------------|--------------------------------------------------------------|
| [dimension or H-ID]     | [view]           | [view]           | [what this signals for the feature or the hypothesis]        |
| [dimension or H-ID]     |                  |                  |                                                              |

Completion rules:
- Every row references a declared hypothesis (H-nn) or the tension axis.
- At least one row names a contradiction you cannot resolve from the interviews alone. Leave open.
- Agreement rows explain why that agreement matters given the tension axis — "both agreed" fails.

---

**The verdict**

Write a synthesis paragraph — 4–6 sentences. Not a summary of what each person said. An
integration: what do the conversations together tell you about the original signal?

Answer three things:
- Does the evidence strengthen, weaken, or complicate the original {SIGNAL} hypothesis?
- What is the single most important finding — the one a feature team cannot ignore?
- What do you still not know, and what would resolve it?

**Anti-restatement test**: if a reader could derive your verdict by reading the per-person
findings back to back, you have restated rather than synthesized. Point to one sentence in the
verdict that cannot be derived from the findings sections. If you cannot, revise.

---

**Beyond the feature: what does this tell me about something bigger?**

After writing the verdict, step back from {SIGNAL} specifically and ask a wider question.

```
Arc question: [What does this interview run tell me about [user type / workflow category /
feature class] more broadly — not about {SIGNAL} specifically? The arc question names a scope
wider than this feature. Test: if I were studying a different but adjacent signal, would the
same arc question apply? If yes, the scope is arc-level. If the arc question would need to be
rewritten for the adjacent signal, it is still feature-scoped.]

Arc inference: [What conclusion does this pair of conversations produce that I could not have
written from my per-person findings or my verdict? This must be new information — an inference
about the adoption pattern, the workflow category, or the user type that the feature evidence
made visible but that applies beyond this one feature.]
```

**Arc check**: if removing the arc question and inference would leave the feature team with
everything they need to decide about {SIGNAL}, the arc synthesis has not elevated the verdict.
The arc inference must add something the feature team would lose if it were removed.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-04 — Combination: Role Sequence + Lifecycle Emphasis

**Axes:** Opposition Axis Declaration as Phase 0 (from V-01 R6) combined with explicit lifecycle
phase gates from R5 V-03. Phase 0 is a new structural phase: Phase 1 cannot begin until the
opposition axis is declared and each pole is described (C-16). Phase 1 gate is quality-conditioned:
each hypothesis must carry a specific falsification condition before Phase 2 begins (C-18 —
stricter than R5 V-03's "at least one" gate). Phase 3 synthesis uses no arc question — C-17 is
deliberately absent to test whether C-16 + C-18 are stable without it.

**Hypothesis:** Phase 0 (opposition axis declaration) + universal falsifiability gate together
satisfy C-16 and C-18 without arc synthesis. The gap test: does the combination produce maximal
signal quality without C-17, or does the absence of an arc question represent a structural
weakness? C-12 uncertain — H-IDs declared in Phase 1 but Phase 2 interview format may not anchor
them as column headers. Predicted: C-16 PASS, C-17 FAIL, C-18 PASS. Aspirational 10/11,
composite ~99.09.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

This skill runs in four sequential phases. Each phase has a gate condition that must be satisfied
before the next phase begins. Phase gates are structural rules — not implied by step numbering.
A phase is not complete until its stated gate condition is explicitly met.

---

### PHASE 0 — Opposition Axis Design

**Write this phase before declaring any hypothesis, selecting any subject, or writing any
interview question.**

This phase answers: why will hearing from subjects at opposite poles of a relevant tension axis
produce more valuable evidence than hearing from subjects at the same pole?

#### Opposition Axis Declaration

| Field | Declaration |
|-------|-------------|
| **Axis name** | [Name the epistemic dimension — e.g., "incumbent process investment vs. workflow modernization appetite" / "operational risk tolerance vs. capability acquisition drive"] |
| **Why this axis for {SIGNAL}** | [Why tension on this axis is more informative than agreement — what question about {SIGNAL} requires hearing from both poles?] |
| **Pole A — skeptical / resistant** | [Who lives at this pole? What have they built or invested in that this signal would disrupt?] |
| **Pole B — receptive / innovative** | [Who lives at this pole? What adoption motivation do they carry?] |
| **Evidence requiring Pole B** | [What specific finding or evidence type cannot be obtained from Pole A alone?] |

**Phase 0 gate**: Phase 0 is not complete until:
1. The axis is named as an epistemic dimension (not demographic)
2. Pole A and Pole B are described at genuinely opposite ends of the axis
3. The evidence requiring Pole B is specific enough to inform subject selection

**Do not write any hypothesis or select any subject until Phase 0 is complete.**

---

### PHASE 1 — Investigation Brief

Write the Investigation Brief before any interview question. Committed once written.

**Signal under investigation:** {SIGNAL}
**Topic context:** {TOPIC}

#### Hypothesis Set

Declare every assumption, belief, and risk you carry into these interviews. Label each H-01,
H-02, etc. Aim for at least 4 hypotheses.

For each hypothesis, state three things:
- **Belief**: what you currently think is true about how stakeholders will respond to {SIGNAL}
- **Confirmation signal**: what an interview answer would look like if this hypothesis holds
- **Falsification condition**: what a subject would have to say — specifically — to force
  rejection. Must name the evidence type or answer pattern, not general disagreement.

```
H-01:
  Belief: [statement of what you currently think]
  Confirms: [answer pattern that would support this]
  Falsifies: [specific answer or finding that would disprove this hypothesis]

H-02:
  Belief: ...
  Confirms: ...
  Falsifies: ...
```

**Phase 1 gate — universal falsifiability**: Phase 1 is not complete until **each declared
hypothesis** carries a specific, non-trivial falsification condition. This is not an "at least
one" gate. Every H-ID must have a named, testable falsification condition before Phase 2 begins.
A hypothesis with a blank or generic falsification condition ("if people generally disagree") does
not satisfy the gate for that hypothesis. Phase 2 cannot begin while any H-ID has an unsatisfied
falsification condition.

#### Subject Roster (axis-assigned)

Each subject must be assigned to a pole from Phase 0.

| ID   | Name   | Role   | Axis Pole (Phase 0)    | Why relevant to this hypothesis set                                     |
|------|--------|--------|------------------------|-------------------------------------------------------------------------|
| S-01 | [Name] | [Role] | Pole A / Pole B        | [one sentence — what question only someone at this pole can answer]     |
| S-02 | [Name] | [Role] | Pole A / Pole B        | [one sentence — meaningfully different from S-01]                       |

One subject per pole minimum. **Phase 1 is complete when:** every H-ID has a stated falsification
condition and the axis-assigned roster is written. **Do not write any interview question until
all Phase 1 conditions are satisfied.**

---

### PHASE 2 — Interviews

For each subject declared in Phase 1, write Identity, Transcript, and Evidence Extraction in
order. Complete one subject in full before beginning the next.

#### [S-nn] — [Name]

**Identity**

[2–3 sentences: company type or domain context, relevant prior experience, at least one concrete
concern or known prior event. The identity must make the axis pole assignment legible — a reader
should understand which pole this subject occupies from the Identity alone.]

Identity test: substitute another persona's name. If the interview answers would still read as
plausible, add specifics until the answer is no.

**Transcript**

Rules:
- Every question cites at least one H-ID from Phase 1 in brackets: `[H-01]`, `[H-02]`
- Minimum 3 questions per subject, each probing a specific Phase 1 hypothesis
- Answers are in the persona's voice — vocabulary, framing, and concerns drawn from Identity
  and axis pole
- When an answer triggers a Phase 1 Falsification condition, mark it:
  > **[FALSIFICATION — H-nn triggered]:** Condition: [exact stated condition]. Subject said:
  > [answer]. Conclusion: [how this forces revision of H-nn].
- When an answer produces a surprise not covered by any declared falsification condition, mark it:
  > **[SURPRISE — contradicts H-nn]:** Expected: [what Phase 1 said]. Found: [what was said].
  > Impact: [how this shifts the investigation].

At least one marked moment (FALSIFICATION or SURPRISE) per subject.

**Evidence Extraction**

Extract findings from this subject. Decision-relevant signals — not summaries.

1. [finding — specific enough that a feature team could act on it]
2. [finding]
3. [finding]

Minimum 3 findings. A finding must be specific enough to act on and must carry the specific
evidence color of this subject's declared axis pole.

**Phase 2 is complete when all subjects have written Identity, Transcript, and Evidence
Extraction. Do not begin Phase 3 until Phase 2 is complete.**

---

### PHASE 3 — Cross-Subject Analysis

Phase 3 begins only after all Phase 2 content is written.

#### Hypothesis Test Table

| H-ID | Hypothesis (brief) | S-01 response                 | S-02 response                 | Falsification triggered? | Verdict                              |
|------|--------------------|-------------------------------|-------------------------------|--------------------------|--------------------------------------|
| H-01 | [text]             | [how S-01 addressed this]     | [how S-02 addressed this]     | Yes / No / Partial       | Confirmed / Contradicted / Split / Untested |

#### Tensions Table

| Dimension [H-ID / axis]              | S-01 position          | S-02 position          | Tension or Agreement                              | Open signal? |
|--------------------------------------|------------------------|------------------------|---------------------------------------------------|--------------|
| [topic / H-ID / axis pole dimension] | [S-01 stated position] | [S-02 stated position] | TENSION: [describe] / AGREEMENT: [why it matters] | Yes / No     |

Completion rules:
- At least one unresolved tension row. Do not resolve it.
- Note whether each tension or agreement was predicted by the Phase 0 opposition axis or was a
  surprise.

#### Composite Signal

**Phase 3 gate — synthesis quality**: This section is not complete if removing it would leave the
artifact's conclusions unchanged.

Write 4–6 sentences answering all four:

1. **Signal verdict**: Does the Phase 1 signal hypothesis come out strengthened, weakened, or
   complicated? State directly.
2. **Falsification result**: Were any Phase 1 Falsification conditions triggered? If yes, what
   must the team revise? If no, what does the absence of triggers signal?
3. **Dominant finding**: What single finding across all subjects is most decision-relevant?
   Name it — not a theme.
4. **Axis verdict**: Did the Phase 0 opposition axis produce the expected tension, or did
   subjects converge unexpectedly? What does the convergence or divergence signal?

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-05 — Combination: Inertia Framing + Arc Signal + Quality Gates + H-ID Anchors

**Axes:** Full combination targeting all three new criteria plus C-12 resolution. Builds on R5
V-04 (lifecycle + inertia, 99–100) and adds: (1) explicit Inertia Axis Declaration as Phase 0
naming the adoption axis (C-16 — stronger than R5 V-04's implicit roster column); (2) universal
falsifiability gate requiring *each* H-ID to carry a falsification condition (C-18 — stricter
than R5 V-04's "at least one"); (3) dedicated Arc Signal section in Phase 3 with required arc
question and arc inference fields (C-17 by construction); (4) "H-IDs tested" as a structural
column in all interview tables (C-12 resolution — H-IDs are pre-committed row-level anchors,
not retroactive bracket annotations).

**Hypothesis:** The combination produces 100/100 by construction on all 18 criteria. C-16 passes
by the explicit Phase 0 pairing rationale section. C-17 passes by the required Arc Signal section
with arc question + arc inference fields. C-18 passes by the universal every-H-ID gate. C-12
passes by the "H-IDs tested" column that must be filled before each question is written. All R5
V-04 strengths (C-08–C-15) inherited. Predicted: 100/100.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

This skill runs in four sequential phases using inertia-first interview ordering. Each phase has
a gate condition. The first subject interviewed is always the persona with the deepest investment
in the current approach — the person this signal would most disrupt. The inertia barrier they
represent becomes the test battery for all subsequent interviews.

---

### PHASE 0 — Inertia Axis Design

**Write this phase before any hypothesis, subject selection, or interview question. It is the
epistemic foundation for this interview run.**

#### Inertia Axis Declaration

| Field | Declaration |
|-------|-------------|
| **Inertia barrier** | [Name the specific current approach, practice, or investment that {SIGNAL} would disrupt. What does the inertia representative have at stake?] |
| **Adoption axis** | [Name the tension dimension — e.g., "depth of investment in current approach vs. appetite for workflow change" / "incumbent practice loyalty vs. capability acquisition drive"] |
| **Why inertia-first** | [One sentence: why interviewing the inertia representative first produces evidence that interviewing an adopter first would not. What does the inertia subject surface that must be heard before the adopter is interviewed?] |
| **Pole A — Inertia representative (SKEPTIC, S-01)** | [Who lives here? What have they built, what are they responsible for, what would switching cost them in time, risk, or rework?] |
| **Pole B — Adopter / evaluator (CHAMPION or EVALUATOR, S-02+)** | [Who lives here? What adoption motivation do they carry that the inertia representative lacks?] |
| **Pre-interview adoption hypothesis** | [Before any interview: what would the inertia representative need to see or hear to consider adoption viable? This is a testable hypothesis — it will be confirmed, contradicted, or complicated in Phase 2.] |

**Phase 0 gate**: Phase 0 is not complete until the inertia barrier and adoption axis are named,
both poles are described at genuinely opposite ends of the axis, and the pre-interview adoption
hypothesis is stated. **Do not write any hypothesis until Phase 0 is complete.**

---

### PHASE 1 — Investigation Brief

Write the Investigation Brief before any interview question. Committed once written.

**Signal under investigation:** {SIGNAL}
**Topic context:** {TOPIC}
**Inertia barrier (from Phase 0):** [reference]

#### Prior Beliefs

Declare every assumption, belief, and risk. Label H-01, H-02, etc. Aim for at least 4 hypotheses.

For each hypothesis, declare three things. Falsification conditions are anchored to S-01 (the
inertia representative) — what would S-01 need to say to force rejection?

| ID   | Hypothesis                                                          | Falsification condition (what S-01 would have to say to force revision)   |
|------|---------------------------------------------------------------------|---------------------------------------------------------------------------|
| H-01 | [belief about how the inertia representative responds to {SIGNAL}] | [what S-01 would have to say — named evidence or answer type]             |
| H-02 | [expected barrier or risk in the current approach]                  | [what S-01's interview would have to reveal for this barrier to not apply] |
| H-03 | [design question the inertia interview should resolve]              | [what finding would resolve this against your expectation]                |
| H-04 | [add rows — aim for 4+]                                             |                                                                           |

**Phase 1 gate — universal falsifiability**: Phase 1 is not complete until **each declared
hypothesis** carries a specific, non-trivial falsification condition. This is an every-hypothesis
gate, not an "at least one" gate. A condition that could apply to any hypothesis ("if people
generally disagree") does not pass the gate for that hypothesis. Phase 2 cannot begin while any
H-ID has an unsatisfied falsification condition.

#### Subject Roster (inertia-first)

| ID   | Name   | Role   | Axis Pole           | Domain Marker                                                                | H-IDs this subject primarily tests |
|------|--------|--------|---------------------|------------------------------------------------------------------------------|-------------------------------------|
| S-01 | [Name] | [Role] | SKEPTIC (Pole A)    | [specific practice or investment that makes S-01 the inertia representative] | H-01, H-02, ...                    |
| S-02 | [Name] | [Role] | CHAMPION / EVALUATOR (Pole B) | [adoption motivation or perspective that distinguishes S-02 from S-01]| H-03, ...                          |

S-01 is interviewed first. Their stated adoption conditions become the test battery for S-02 and
all subsequent subjects.

**Phase 1 is complete when:** every H-ID has a stated falsification condition and the axis-assigned
roster is written. **Do not begin Phase 2 until both conditions are satisfied.**

---

### PHASE 2 — Interviews (inertia-first)

#### S-01 — SKEPTIC (Inertia Representative)

**Identity**

[3–4 sentences: name, role, company type. Make S-01's investment in the current approach deep and
specific — how long they have used it, what they have built with it, what a switch would cost.
The depth must make S-01's resistance legible as well-founded and role-specific, not generic.]

Swap test: substitute S-02's name. If the interview answers would still read as plausible, add
specifics until the answer is no.

**Interview Table**

| Q#  | H-IDs tested | Question                                                              | Answer (S-01 voice)                                              | Evidence Signal [type: ...]                         | Surprise?     |
|-----|--------------|-----------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------|---------------|
| Q1  | H-nn         | [Current-practice baseline — what do you do today for {TOPIC}?]      | [S-01 answer establishing depth of current investment]           | [constraint: …] / [preference: …] / etc. — [signal] | No (baseline) |
| Q2  | H-nn         | [What is the hardest part about your current approach?]               | [Real friction in S-01's current practice — the crack in inertia] |                                                    |               |
| Q3  | H-nn         | [Signal introduction — S-01's reaction to {SIGNAL}]                  | [Skeptic response with specific objection]                       |                                                    | Yes / No      |
| Q4  | H-nn         | [What would have to be true for you to adopt this?]                   | [S-01's adoption conditions — each is an implicit falsifiable claim about {SIGNAL}'s viability] | | |
| Q5+ | H-nn         | [Additional objection probe]                                          |                                                                  |                                                    |               |

**"H-IDs tested" column rules:**
- Fill this column *before* writing the question in that row. Each question is written to test
  the H-IDs listed.
- This column is a structural pre-commit anchor. A question with a blank H-IDs column may not
  be written.
- The H-IDs tested column makes every question-to-hypothesis link a design decision, not a
  retroactive label.

Minimum 4 rows for S-01 (2 baseline + 2 signal reaction). At least one "Yes" in Surprise column.

**Inertia Profile**

| Concern or Objection | H-ID | Basis in S-01's practice                          | Adoption condition (from Q4)                    |
|----------------------|------|---------------------------------------------------|-------------------------------------------------|
| [stated concern]     | H-nn | [why grounded in S-01's specific role / practice] | [what S-01 said would be needed for adoption]   |

The Inertia Profile becomes the test battery for S-02. Every Phase 2 interview after S-01 must
address at least one row of this profile.

**Evidence Extraction (S-01)**

1. [finding — specific to S-01's role and current-practice context]
2. [finding]
3. [finding]

---

#### S-02+ — Subsequent Interviews

**Identity**

[2–3 sentences: name, role, domain distinction from S-01. Note explicitly what distinguishes
this persona's axis position from S-01's — different adoption motivation, different investment
level, different risk profile.]

**Interview Table**

| Q#  | H-IDs tested | Question                                              | Answer (persona voice)                           | Evidence Signal [type: ...]             | Inertia Profile check (vs. S-01)                                |
|-----|--------------|-------------------------------------------------------|--------------------------------------------------|-----------------------------------------|-----------------------------------------------------------------|
| Q1  | H-nn         | [Current-practice anchor — what do you do today?]    | [S-nn baseline answer]                           |                                         | Baseline — no S-01 comparison yet                              |
| Q2  | H-nn         | [Testing S-01 Inertia Profile concern 1]             | [S-nn response — confirm / reject / qualify]     |                                         | S-01 said [X]; S-nn said [Y] — confirms / rejects / qualifies  |
| Q3  | H-nn         | [Testing S-01 adoption condition or Phase 1 H-ID]    |                                                  |                                         |                                                                 |

"H-IDs tested" column: fill before writing each question. Minimum 3 rows.
"Inertia Profile check" column must reference S-01's stated position specifically.
At least one confirm or reject per subsequent subject.

**Evidence Extraction**

1. [finding — specific to this subject's role and axis pole]
2. [finding]
3. [finding]

**Phase 2 is complete when all subjects have written Identity, Interview Table, and Evidence
Extraction. Do not begin Phase 3 until Phase 2 is complete.**

---

### PHASE 3 — Synthesis

Phase 3 begins only after all Phase 2 content is written.

#### Inertia vs. Adoption Comparison Table

Rows are drawn from the S-01 Inertia Profile — not invented after the fact.

| S-01 Concern / Adoption Condition (H-ID) | S-01 baseline              | S-02 response                              | Resolution status                      |
|------------------------------------------|----------------------------|--------------------------------------------|----------------------------------------|
| [concern from Inertia Profile] (H-nn)    | [S-01 stated position]     | [confirm / reject / qualify + explanation] | Resolved / Unresolved / Context-dependent |

At least one unresolved row. "Same as S-01" without explanation fails.

#### Composite Arc Signal

**Phase 3 gate — synthesis quality**: This section is not complete if it merely restates rows
from the Inertia vs. Adoption Table.

Write 4–6 sentences answering all four:

1. **Arc verdict**: Does the signal have a viable adoption path given S-01's resistance and
   subsequent subjects' reactions? State directly.
2. **Strongest remaining barrier**: Name S-01's strongest concern that subsequent interviews
   did not address or resolve.
3. **Most surprising finding**: What did a subsequent subject reveal that S-01's Inertia Profile
   would not have predicted? Cite subject ID and H-ID.
4. **Next validation step**: What must the feature team validate before treating this signal as
   evidence of adoption viability?

---

#### Arc Signal

**Write this section after the Composite Arc Signal. It is required. It must not restate
feature-level conclusions from the Composite Arc Signal.**

The Arc Signal answers a question whose scope is wider than {SIGNAL} — what this inertia-vs.-
adoption interview run reveals about the adoption pattern, the workflow category, or the class
of features {SIGNAL} belongs to.

| Field | Content |
|-------|---------|
| **Arc question** | [State an explicit question wider than {SIGNAL} — e.g., "What does this inertia-vs.-adoption pairing tell us about how [user type] evaluates [workflow category] signals?" Scope test: if the same question would apply equally to an adjacent signal with the same inertia profile, the scope is arc-level.] |
| **Arc inference** | [State a conclusion that answers the arc question and that a reader could not reconstruct from the Composite Arc Signal alone. The inference points beyond this specific signal to a pattern or principle about adoption, the workflow, or the user category.] |
| **Arc scope confirmation** | [Confirm: substitute an adjacent signal. Does the arc question still apply? If yes, scope is arc-level. If the arc question would need to be rewritten for the adjacent signal, scope is still feature-level — revise the arc question.] |

**Anti-restatement test**: if removing the Arc Signal would leave the feature team with
everything they need to decide about {SIGNAL}, the Arc Signal has not elevated the synthesis.
Revise until removal costs the feature team something they could not reconstruct.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## Axis Coverage Summary

| Axis                           | V-01    | V-02    | V-03      | V-04    | V-05    |
|--------------------------------|---------|---------|-----------|---------|---------|
| Role sequence / opposition axis | PRIMARY | —       | SECONDARY | PRIMARY | PRIMARY |
| Output format (arc section)    | —       | PRIMARY | —         | —       | PRIMARY |
| Lifecycle emphasis (phase gates) | —     | —       | —         | PRIMARY | PRIMARY |
| Phrasing register              | —       | —       | PRIMARY   | —       | —       |
| Inertia framing                | —       | —       | —         | —       | PRIMARY |

---

## Predicted R6 Scores (v6 rubric)

| Variation | C-16 | C-17 | C-18 | C-12 | Aspirational | Composite |
|-----------|------|------|------|------|--------------|-----------|
| V-01 (Role Sequence) | PASS | FAIL | FAIL | PASS | 9/11 | 98.18 |
| V-02 (Output Format — Arc Signal) | FAIL | PASS | FAIL | PASS | 9/11 | 98.18 |
| V-03 (Phrasing Register) | PASS | PASS | PASS | FAIL | 10/11 | 99.09 |
| V-04 (Role Sequence + Lifecycle) | PASS | FAIL | PASS | UNCERTAIN | 10/11 | ~99.09 |
| V-05 (Inertia + Arc + Quality Gates + H-ID anchors) | PASS | PASS | PASS | PASS | 11/11 | 100.00 |

*V-01: Opposition Axis Declaration section enforces C-16 by construction — it is a gate
prerequisite for the Hypothesis Register. C-17 absent (single-axis test; no arc section).
C-18 absent (gate language unchanged from R5 V-01: "at least one hypothesis"). C-12 PASS —
tabular structure maintained; H-IDs in question brackets satisfy evaluator test.*

*V-02: Arc Signal section with required arc question + arc inference fields enforces C-17 by
construction — scope test and anti-restatement test are embedded in the field instructions.
C-16 absent (no pairing rationale; single-axis test). C-18 absent (gate unchanged). C-12 PASS
via tabular structure.*

*V-03: Three researcher-voice prompts address C-16 (tension axis declaration before roster),
C-17 (arc question after verdict), C-18 (every hypothesis needs falsification before proceeding).
C-12 FAIL — conversational register produces parenthetical H-ID notations, not column headers.
C-13 UNCERTAIN — "can I move on?" prompt is a researcher self-check, not a formal gate sentence;
evaluator interpretation of the explicit-gate-sentence test may vary.*

*V-04: Phase 0 (opposition axis declaration) enforces C-16. Universal Phase 1 gate (every H-ID
must carry falsification condition) enforces C-18. C-17 absent — no arc section (deliberate gap
test). C-12 uncertain — Phase 2 interview format uses question-text H-ID citations but no
dedicated H-IDs column.*

*V-05: All four targeted criteria pass by construction. Phase 0 inertia axis declaration (C-16
— stronger than R5 V-04's implicit roster annotation). Arc Signal section with required arc
question and arc inference fields (C-17). Universal every-hypothesis falsifiability gate (C-18).
"H-IDs tested" column pre-committed before each question is written (C-12 — H-IDs are structural
row anchors, not retroactive bracket labels). All R5 V-04 strengths for C-08 through C-15
inherited.*
