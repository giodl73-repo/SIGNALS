# prove-interview — Rubric v2 Variations — Round 2

_Date: 2026-03-15 · Rubric: v2 (C-01–C-11) · Ceiling: 100_

---

## Context

Round 1 produced 5 variations scored against the v1 rubric (C-01–C-09). V-04 (Format +
Lifecycle combination) scored 100. The v2 rubric adds two new aspirational criteria:

- **C-10** — Hypotheses pre-declared before interview begins (lifecycle ordering criterion)
- **C-11** — Structural cross-subject artifact that cannot be completed by recording agreement alone

Under v2, V-04 from Round 1 would still score 100 because it had both the Investigation Brief
(C-10) and the Phase 3 Tensions Table (C-11). But V-01, V-02, and V-05 have known gaps:
- V-01: Cross-Subject Note accepts agreement → C-11 FAIL; no hypothesis pre-declaration → C-10 FAIL
- V-02: No type tags → C-09 FAIL; no hypothesis declaration → C-10 FAIL; no structural artifact → C-11 FAIL
- V-05: No type tags → C-09 FAIL; no hypothesis declaration → C-10 FAIL

Round 2 goals:
1. Isolate each axis cleanly (single-axis first)
2. Confirm which single-axis changes alone can satisfy C-10 and/or C-11
3. Combine the strongest single-axis patterns into a maximum-coverage variation

---

## Variation Axes

| Axis | Round 1 result | Round 2 focus |
|------|---------------|---------------|
| Output format | V-01 (95) — C-09 PASS, C-10 FAIL, C-11 FAIL | Can table structure alone satisfy C-10 and C-11? |
| Phrasing register | V-02 (90) — richest voice, weakest structure | Can minimal structural anchors close the aspirational gaps without losing voice quality? |
| Lifecycle emphasis | V-03 (~90) — C-10 covered, C-11 gap, C-05 partial | Can explicit phase gates fully satisfy C-11 and repair C-05? |
| Role sequence | V-05 (95) — C-08 via sequencing, C-09/C-10/C-11 gaps | Can skeptic-first + incumbent framing serve as implicit hypothesis pre-declaration? |
| Inertia framing | Untested alone | Can status-quo baseline framing drive C-10 and C-11 by making inertia the prior signal? |

---

## V-01 — Single axis: Output Format

**Axis:** Tabular per-question structure with mandatory typed columns and a required Tensions Matrix
**Hypothesis:** Adding a Hypothesis Register section before any interview table, and replacing the
Cross-Subject Note with a Tensions Matrix that structurally requires comparison, will satisfy
C-10 and C-11 by construction while preserving C-09 (typed evidence tags already forced by
column structure). The key change from Round 1 V-01: (1) hypothesis register is declared first
and locked before any Q# row is written; (2) the cross-subject section is a matrix, not a note,
and its completion rules explicitly prohibit agreement-only rows.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Simulate stakeholder or customer interviews about this topic. This is a grounded simulation —
not a real interview — but every answer must be anchored in the persona's documented identity and
expertise. The output is a signal artifact: evidence toward or against the signal hypothesis.

---

### STEP 1 — Hypothesis Register

Write this before any interview. This register is locked once written.
No question may be written without citing at least one hypothesis ID from this register.

| ID   | Hypothesis                                                        | Category   |
|------|-------------------------------------------------------------------|------------|
| H-01 | [a belief you hold about how stakeholders will react to SIGNAL]  | assumption |
| H-02 | [a risk you expect to surface]                                    | risk       |
| H-03 | [a design question you expect the interviews to resolve]          | unknown    |
| ...  | [add rows as needed — aim for at least 4 hypotheses]              |            |

---

### STEP 2 — Human Subjects Roster

| ID   | Name    | Role              | Seniority | Domain Expertise | Key Concern                          |
|------|---------|-------------------|-----------|-----------------|--------------------------------------|
| S-01 | [Name]  | [Role]            | [Level]   | [Domain]        | [What this persona is most likely to push back on or champion] |
| S-02 | [Name]  | [Role]            | [Level]   | [Domain]        | [Key concern distinct from S-01]    |

Minimum 2 subjects. Subjects must have meaningfully different roles, domains, or concerns.
If two subjects would give the same answers, differentiate them before proceeding.

---

### STEP 3 — Interviews

For each subject in the roster:

#### [S-nn] — Identity

Write a 2–3 sentence Identity paragraph. Include: company type or context, relevant prior
experience, and at least one concrete concern or known event that makes this persona specific.

**Swap test:** If another persona's name could be substituted here and the answers would still
read as plausible, the identity is not specific enough. Revise before writing the interview table.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn]                           | Answer (persona voice)                          | Evidence Signal [type: ...]                                    | Surprise?                             |
|-----|-------------------------------------------|-------------------------------------------------|----------------------------------------------------------------|---------------------------------------|
| Q1  | [Question] [H-01]                         | [Answer — vocabulary and concerns from Identity] | [risk: …] / [preference: …] / [constraint: …] / [validation: …] / [invalidation: …] — [one-sentence signal] | Yes — assumed [X], found [Y] / No    |
| Q2  | [Question] [H-02]                         |                                                 |                                                                |                                       |
| Q3  | [Question] [H-nn]                         |                                                 |                                                                |                                       |

**Table rules:**
- Every question must cite at least one H-ID from the Hypothesis Register in brackets.
- Every answer must fail the swap test — a different persona's name cannot be substituted and
  still ring true. Generic AI-sounding answers fail regardless of how long they are.
- Every Evidence Signal must carry a type tag from the set:
  `[risk: …]`, `[preference: …]`, `[constraint: …]`, `[validation: …]`, `[invalidation: …]`
- At least one row per subject must have "Yes" in the Surprise column with explanation.
- Minimum 3 question rows per subject.

---

### STEP 4 — Cross-Subject Tensions Matrix

Write this section after all subject tables are complete. It is required.

This matrix structurally requires comparison. It cannot be completed by recording agreement alone.
Completion rules:
- Every row must compare at least two subjects against a shared dimension.
- A row where both subjects hold identical views must still state what that agreement signals and
  why it is not trivially expected.
- At least one row must record an open, unresolved tension. Do not resolve it in this artifact.
  Leave it as an open signal for the feature team.

| Dimension                 | S-01 position          | S-02 position          | Tension or Agreement [explain]               | Unresolved? |
|---------------------------|------------------------|------------------------|----------------------------------------------|-------------|
| [topic / concern / H-ID]  | [S-01 view]            | [S-02 view]            | TENSION: [describe] / AGREEMENT: [what it signals] | Yes / No |
|                           |                        |                        |                                              |             |

---

### STEP 5 — Composite Signal

3–5 sentences. What do the interviews together say about the signal hypothesis? Cite subjects by
ID (S-01, S-02, etc.). Name the single most important unresolved tension. State whether the
interviews strengthen, weaken, or leave ambiguous the original signal hypothesis.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-02 — Single axis: Phrasing Register

**Axis:** Conversational researcher-notebook register — warm, narrative, no imperative columns
**Hypothesis:** A conversational prompt produces richer persona voice (C-02) than a tabular one
because it invites inference rather than dictating cell contents. The test is whether two minimal
structural anchors — (1) a "what do I believe right now?" pre-interview checklist (C-10) and (2)
a required side-by-side Comparison section (C-11) — can satisfy the new aspirational criteria
without collapsing the register into bureaucratic table-filling. C-09 (typed evidence tags) is
the expected sacrifice: prose findings resist tagging, and the hypothesis is that losing C-09
is acceptable if C-10 and C-11 both pass. If both pass and C-09 also passes, the variation
succeeds beyond expectation.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Think of yourself as a researcher sitting down with a few people to find out what they actually
think about this topic. These conversations are not real — but they should feel like they could
be. Every answer should come from a specific person with a specific background, not from a
generic AI response that could fit anyone.

---

**Before you talk to anyone: what do you believe right now?**

Write down the beliefs and assumptions you are carrying into these interviews before you write
a single question. Label them H-01, H-02, etc. These are your priors. The interviews test them.
Write at least 4.

```
H-01: I believe that [type of stakeholder] will ...
H-02: My main concern is that ...
H-03: I expect the adoption barrier to be ...
H-04: I think the biggest surprise will come from ...
```

Do not revise these after you write the interviews. If an answer contradicts a prior, that is
the finding — not a reason to rewrite the prior.

---

**Who are you talking to?**

Choose at least 2 people to interview. They should have different jobs, different expertise, and
different reasons to care (or not care) about this signal. Before each interview, write a short
pre-interview note:

```
Name: [realistic invented name]
Role: [title and seniority]
Background: [2–3 sentences — industry, what they have seen, what they worry about, a past
experience that shapes their perspective]
Why I chose this person: [one sentence — what question only they can answer]
```

Identity check: could someone with a different role give the same answers if you swapped names?
If yes, add more specifics until the answer is no.

---

**The conversations**

Write each interview as a transcript. Let each person speak in their own voice. A compliance
officer at a regulated bank does not talk like a startup CTO. A developer who has been burned
by API instability does not answer the same way as one who hasn't.

For each interview:
- Write at least 3 substantive questions
- After each question, note which prior hypothesis it tests — e.g., *(testing H-02)* —
  even if only parenthetically
- When an answer surprises you — something that contradicts what you expected — write a short
  note in the flow: *"I expected [X], but [Name] said [Y]. This shifts how I think about [Z]."*
  At least one moment per person should surprise you.

---

**What did you find?**

After each interview, write a short extraction — 3 to 5 concrete findings. Not summaries of
what was said. Findings. Something specific this person told you that could influence a feature
decision. If you are struggling to write findings, the interview is not specific enough — go
back and sharpen the answers.

---

**What do both conversations tell you together?**

This is required. After both interviews, step back and look at them side by side.

Write a **Comparison section** that explicitly contrasts the two subjects on at least 3 dimensions.
The format must be a table — prose is not sufficient here because prose can avoid the comparison:

| What I examined        | [Name 1]     | [Name 2]     | What the difference (or similarity) signals |
|------------------------|-------------|-------------|---------------------------------------------|
| [dimension 1]          | [view]      | [view]      | [what it means for the feature or hypothesis] |
| [dimension 2]          |             |             |                                              |
| [dimension 3]          |             |             |                                              |

Completion rules for this table:
- You must fill every cell with something specific to that person — not "N/A" or "same as above."
- At least one row must name a contradiction between the two subjects that you cannot resolve
  from the interviews alone. Leave it unresolved. It is a signal, not a problem to fix.
- A row where both subjects agree must explain why that agreement is (or is not) surprising.

---

**Composite Signal**

End with 3–5 sentences. What do both conversations together tell you about the signal
hypothesis? Which prior hypothesis was most strongly tested? What is the most important thing
you still do not know?

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-03 — Single axis: Lifecycle Emphasis

**Axis:** Three explicit phases with hard gate rules between them
**Hypothesis:** Making the lifecycle structure visible as named phases — with a rule that Phase 2
cannot begin until Phase 1 is complete, and Phase 3 cannot begin until all Phase 2 interviews
are written — structurally prevents post-hoc hypothesis declaration (C-10 by gate), separates
evidence accumulation from synthesis (fixing Round 1 C-05 partial by making surprises detectable
against the declared prior), and creates a Phase 3 artifact that cannot be completed without
comparison (C-11). The key Round 1 gap was that V-03 had the Investigation Brief but no
explicit requirement that Phase 3 be a structural table rather than a prose summary. This
variation fixes that gap while keeping the lifecycle-first emphasis as the single axis.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

This skill runs in three sequential phases. Do not begin Phase 2 until Phase 1 is fully written.
Do not begin Phase 3 until all Phase 2 interviews and evidence extractions are complete.
The phase gate is the core discipline of this skill.

---

### PHASE 1 — Investigation Brief

Write the Investigation Brief before any interview question is written. This is a committed
declaration of your current state of belief. It cannot be revised after Phase 2 begins.

**Signal under investigation:** {SIGNAL}
**Topic context:** {TOPIC}

**Hypothesis set:**

State every assumption, belief, and risk you carry into these interviews. Label each H-01,
H-02, etc. Aim for at least 4 hypotheses.

For each hypothesis, state:
- What you believe now
- What kind of answer would **confirm** it
- What kind of answer would **contradict** it (this is how you will recognize surprises)

```
H-01: [statement of belief]
  Confirms: [what an answer looks like if H-01 is true]
  Contradicts: [what an answer looks like if H-01 is false]

H-02: ...
```

**Interview subjects:**

Declare who you will interview and why their perspective is relevant to this hypothesis set.
Minimum 2 subjects. Subjects should cover meaningfully different roles, knowledge levels, or
positions on the topic.

| ID   | Name   | Role    | Why relevant to this hypothesis set |
|------|--------|---------|-------------------------------------|
| S-01 | [Name] | [Role]  | [one sentence]                      |
| S-02 | [Name] | [Role]  | [one sentence]                      |

Phase 1 is complete when the hypothesis set and subject roster are written.
**Do not write any interview questions until Phase 1 is complete.**

---

### PHASE 2 — Interviews

For each subject declared in the Investigation Brief, write their interview in order.
Complete each subject's full interview and evidence extraction before beginning the next subject.

#### [S-nn] — [Name]

**Identity**

Write the Identity section before the transcript. Include:
- Full name, role, and seniority
- Company type or domain context
- Relevant prior experience or expertise
- At least one concrete concern or documented prior event that makes this persona distinct

Identity test: if you substituted another persona's name into this identity paragraph, would it
still read as plausible? If yes, add specifics until the answer is no.

**Transcript**

Write the Q&A transcript. Rules:
- Every question must cite at least one hypothesis by ID from Phase 1: e.g., `[H-01]`, `[H-02]`
- Minimum 3 questions per subject, each probing a specific hypothesis or design risk
- Answers must be in the persona's voice — vocabulary, concerns, and framing from the Identity
- When an answer contradicts a Phase 1 hypothesis, mark it immediately:
  > **[SURPRISE — contradicts H-nn]:** Expected: [what Phase 1 said would confirm/contradict].
  > Found: [what the subject actually said]. Impact: [how this shifts the investigation].

At least one SURPRISE must be marked per subject. A subject who confirms every hypothesis
without contradiction is not plausible — revise the answers to include genuine friction.

**Evidence Extraction**

After the transcript, extract findings from this subject. These are not summaries —
they are decisions-relevant signals:

1. [finding: a specific fact, preference, concern, or constraint that could influence the feature]
2. [finding]
3. [finding]
...

Minimum 3 findings. A finding must be specific enough that a reader could act on it.
"Users want simplicity" is not a finding. "S-01 requires that the feature produce no additional
IAM role configuration — their security team has a 6-week review cycle and a new role blocks
every release" is a finding.

Phase 2 is complete when all subjects are interviewed and all evidence extractions are written.
**Do not begin Phase 3 until Phase 2 is complete.**

---

### PHASE 3 — Cross-Subject Analysis

Phase 3 begins only after all Phase 2 interviews and evidence extractions are written.
Phase 3 has two required artifacts.

#### Hypothesis Test Table

For each hypothesis declared in Phase 1, record how each subject spoke to it:

| H-ID | Hypothesis (abbreviated)     | S-01 response (brief)        | S-02 response (brief)        | Verdict             |
|------|------------------------------|------------------------------|------------------------------|---------------------|
| H-01 | [hypothesis text]            | [how S-01 addressed this]    | [how S-02 addressed this]    | Confirmed / Contradicted / Split / Untested |
| H-02 |                              |                              |                              |                     |
| ...  |                              |                              |                              |                     |

#### Tensions Table

This is a required structural artifact. It cannot be completed by recording agreement alone.

**Completion rules:**
- Each row must compare subjects on a specific dimension. Generic rows ("both subjects were
  positive about the feature") fail — identify the specific aspect of the feature or hypothesis.
- At least one row must record a tension that remains unresolved after Phase 2. Do not resolve
  it here. Note it as an open signal for the feature team.
- A row where subjects agree must explain why that agreement is or is not surprising given the
  Phase 1 hypotheses.

| Dimension                        | S-01 position            | S-02 position            | Tension or Agreement                          | Open signal? |
|----------------------------------|--------------------------|--------------------------|-----------------------------------------------|-------------|
| [specific topic or hypothesis]   | [S-01 stated position]   | [S-02 stated position]   | TENSION: [describe] / AGREEMENT: [explain why it matters] | Yes / No |
|                                  |                          |                          |                                               |             |

#### Composite Signal

3–5 sentences. What do the interviews together tell you about the signal hypothesis? Cite
subjects by ID. Name the most important unresolved tension from the Tensions Table. State
whether the interview evidence strengthens, weakens, or complicates the original signal.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-04 — Combination: Lifecycle Emphasis + Output Format

**Axes:** Phase gates (V-03) + per-question table with typed columns (V-01)
**Hypothesis:** The combination of (1) a locked Investigation Brief in Phase 1 with H-ID
declarations before any transcript, (2) per-question interview tables with mandatory H-nn
reference and typed evidence signal columns in Phase 2, and (3) a mandatory Phase 3 Tensions
Table that structurally requires comparison will satisfy all 11 v2 criteria by structural
necessity. C-10 passes because the Investigation Brief is a Phase 1 gate — no table row can
be written before hypotheses exist. C-11 passes because the Tensions Table has explicit
completion rules that prohibit agreement-only rows. C-09 passes because typed evidence tags
are required in every table row. The combination is the Round 1 V-04 pattern, now retargeted
explicitly at the v2 criteria by naming C-10 and C-11 as construction targets.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

This skill runs in three phases. The phase structure is not optional. Phase 2 tables cannot
be written before Phase 1 is complete. Phase 3 cannot be written before all Phase 2 tables
are complete. The phase gate is the core structural guarantee of this skill.

---

### PHASE 1 — Investigation Brief

Write the Investigation Brief before any interview table row.

**Signal under investigation:** {SIGNAL}
**Topic context:** {TOPIC}

**Hypothesis Register:**

| ID   | Hypothesis                                                            | Category              |
|------|-----------------------------------------------------------------------|-----------------------|
| H-01 | [a belief about how stakeholders will react to this signal]          | assumption / risk / unknown |
| H-02 | [a specific risk you expect to surface]                              |                       |
| H-03 | [a design question you expect these interviews to resolve]            |                       |
| H-04 | [add additional hypotheses as needed — aim for at least 4]            |                       |

This register is locked once written. Every Q# cell in every interview table must cite at least
one hypothesis ID from this register. A question with no H-ID citation is structurally visible
as a hypothesis-free question — it fails the rubric regardless of how well-formed it is.

**Human Subjects Roster:**

| ID   | Name    | Role              | Seniority | Domain Expertise | Key Concern                               |
|------|---------|-------------------|-----------|-----------------|-------------------------------------------|
| S-01 | [Name]  | [Role]            | [Level]   | [Domain]        | [What makes this persona's view relevant to the hypothesis set] |
| S-02 | [Name]  | [Role]            | [Level]   | [Domain]        | [Key concern distinct from S-01]         |

Minimum 2 subjects with meaningfully different roles, expertise, or positions.

Phase 1 is complete when the Hypothesis Register and Human Subjects Roster are written.
**Do not write any interview table row until Phase 1 is complete.**

---

### PHASE 2 — Interviews

For each subject in the Phase 1 roster, write their Identity section and interview table in
full before moving to the next subject.

#### [S-nn] — [Name] — [Role]

**Identity**

[2–3 sentences: company type, domain expertise, relevant prior experience, and one concrete
concern or known prior event that distinguishes this persona. Swap test: if another persona's
name replaced this one and the interview answers still read as plausible, the identity fails.]

**Interview Table**

| Q#  | Question [H-nn]               | Answer (persona voice)                                   | Evidence Signal [type: ...]                                       | Surprise?                              |
|-----|-------------------------------|----------------------------------------------------------|-------------------------------------------------------------------|----------------------------------------|
| Q1  | [Question] [H-01]             | [Answer specific to this persona's identity and concerns] | [risk: …] / [preference: …] / [constraint: …] / [validation: …] / [invalidation: …] — [one-sentence signal] | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn]             |                                                          |                                                                   |                                        |
| Q3  | [Question] [H-nn]             |                                                          |                                                                   |                                        |

**Table rules:**
- Q# cells: every question cites at least one H-ID from the Phase 1 Hypothesis Register.
- Answer cells: persona voice only — specific vocabulary, concerns, and framing from Identity.
  Generic answers that could belong to any persona fail the swap test.
- Evidence Signal cells: required for every row. Type tag must be one of:
  `[risk: …]`, `[preference: …]`, `[constraint: …]`, `[validation: …]`, `[invalidation: …]`
  followed by a one-sentence signal interpretation.
- Surprise cells: at least one "Yes" per subject, with explanation of what was expected (which
  Phase 1 hypothesis) and what was found instead.
- Minimum 3 rows per subject.

Phase 2 is complete when all subjects have full Identity sections and interview tables with all
evidence signal cells filled.
**Do not begin Phase 3 until Phase 2 is complete.**

---

### PHASE 3 — Cross-Subject Analysis

Phase 3 begins only after all Phase 2 interview tables are complete.

#### Tensions Table

This is the required Phase 3 structural artifact.

**Completion rules (these are not optional):**
1. Every row must compare at least two subjects against a shared dimension. The comparison must
   reference specific content from the Phase 2 interview tables — not inferred or invented.
2. A row where subjects agree is permitted only if it explains why that agreement is
   meaningful or surprising given the Phase 1 hypotheses. "Both agreed" alone fails.
3. At least one row must record an unresolved tension between subjects. Do not resolve it here.
   The tension is the signal. Leave it open for the feature team.
4. Rows may reference hypothesis IDs from Phase 1 to connect the comparison to the prior belief.

| Dimension [H-ID if applicable] | S-01 position                  | S-02 position                  | Tension / Agreement [explained]                         | Unresolved? |
|--------------------------------|--------------------------------|--------------------------------|---------------------------------------------------------|-------------|
| [specific topic or H-ID]       | [S-01 stated view, Phase 2 ref] | [S-02 stated view, Phase 2 ref] | TENSION: [describe] / AGREEMENT: [why it signals what it does] | Yes / No |
|                                |                                |                                |                                                         |             |

#### Composite Signal

3–5 sentences. What do the interviews together say about the signal hypothesis, as stated in
Phase 1? Reference which hypotheses were confirmed, which were contradicted, and which remain
open. Cite subjects by ID. Name the single most important unresolved tension from the Tensions
Table and state what a feature team would need to do to resolve it.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-05 — Combination: Role Sequence + Inertia Framing

**Axes:** Skeptic-first ordering + prominent status-quo / incumbent baseline framing
**Hypothesis:** Framing the first interview as the "inertia interview" — the person who has the
most to lose from adoption, with deep expertise in the current approach — creates a structural
prior-signal baseline that functions as an implicit C-10 hypothesis declaration. The inertia
subject's stated concerns and objections become the hypotheses that later subjects test. The
cross-subject artifact is then naturally the "Inertia vs. Adoption" comparison table, which
structurally cannot be completed by agreement alone (because the first subject's position is
by definition resistant). This variation tests whether role-sequence and inertia framing can
satisfy C-10 and C-11 without an explicit Investigation Brief or tabular interview format —
relying instead on the structural logic of the role order to enforce the lifecycle discipline.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

This skill structures stakeholder interviews using an inertia-first framing. The first subject
is always the person with the most to lose from this signal being true — the defender of the
current approach, the holder of the status quo. Their concerns and objections become the
baseline against which all subsequent subjects are measured.

The logic: a new signal is worth trusting only if it can account for the inertia it will face.
Interview the inertia first.

---

### SUBJECT ROSTER

Before writing any interview, declare the subjects in inertia-first order:

| ID   | Name    | Role             | Stance   | Why they hold this stance                          | Key concern or prior                        |
|------|---------|------------------|----------|----------------------------------------------------|---------------------------------------------|
| S-01 | [Name]  | [Role]           | SKEPTIC  | [What about their role or experience makes them the natural defender of the status quo] | [Their central objection or concern about this signal] |
| S-02 | [Name]  | [Role]           | CHAMPION | [What makes them the natural adopter or proponent] | [What they are hoping this signal enables]  |
| S-03 | [Name]  | [Role — optional] | NEUTRAL  | [Their position]                                   | [What they need to see before deciding]     |

S-01 must be the SKEPTIC and must be interviewed first. The SKEPTIC is not a villain — they are
the person with the deepest investment in the existing approach. Their objections are
well-founded, not irrational. Answering them well is what makes the signal credible.

---

### INERTIA BASELINE (S-01 — SKEPTIC)

#### Identity

[3–4 sentences: name, role, company type. Focus on what makes this person's expertise in the
current approach deep and specific. Include: how long they have used the current approach, what
they have built with it, and what a switch would cost them — in time, rework, or risk.]

#### Current-Practice Questions

Begin with the status quo. Ask at least 2 questions about what S-01 does today, before
introducing the signal. These establish the baseline that makes their later reactions credible.

- Q1: [What do you currently use for [topic]? Walk me through how it works in your context.]
  > [S-01 Answer — specific to their expertise and domain. Establish the depth of investment.]

- Q2: [What is the biggest pain point in your current approach?]
  > [S-01 Answer — a real friction point, not a generic complaint. This is the crack in the
  > inertia that the signal might address — or might not.]

#### Signal Reaction Questions

Now introduce the signal and probe S-01's response:

- Q3: [Question about the signal] [directly tests a concern surfaced in Q1 or Q2]
  > [S-01 Answer — skeptic voice. Concrete objection, not abstract doubt.]

- Q4: [What would have to be true for you to seriously consider adopting this?]
  > [S-01 Answer — this is the most important answer in the interview. It states the conditions
  > under which inertia yields. Mark any condition that surprises you.]

- [Add Q5+ as needed to surface S-01's key objections]

#### S-01 Inertia Profile

After the transcript, write the Inertia Profile — the structured summary of S-01's resistance:

| Concern             | Basis                                       | Adoption condition (from Q4)                        | Signal strength |
|---------------------|---------------------------------------------|-----------------------------------------------------|-----------------|
| [stated objection]  | [why this concern is grounded in S-01's role] | [what S-01 said would need to be true for adoption] | High / Medium / Low |
| ...                 |                                             |                                                     |                 |

The Inertia Profile becomes the hypothesis set for subsequent interviews. Every question to S-02
(and S-03) should test at least one row of this profile.

---

### SUBSEQUENT INTERVIEWS (S-02, S-03, ...)

For each subsequent subject:

#### Identity

[2–3 sentences: name, role, company type, and relevant experience. Note what distinguishes
this persona's perspective from S-01's — different domain, different stage of adoption, different
risk profile.]

#### Interview

- Q1: [Current-practice anchor — what do you do today?]
  > [Answer — establish their baseline before the signal is discussed]

- Q2: [Question testing S-01 Inertia Profile concern 1]
  > [Answer — their reaction to the concern S-01 raised. Does this concern apply to them?]
  > **[SURPRISE — expected [X] based on S-01 profile, found [Y]]** _(if applicable)_

- Q3: [Question testing S-01 Inertia Profile concern 2 or adoption condition]
  > [Answer]

- [Add questions as needed — at least 3 per subject]

Mark surprises when an answer contradicts what S-01's Inertia Profile would predict. At least
one surprise per subsequent subject.

#### Evidence Extraction

After each transcript, extract 3–5 findings — specific signals that could influence a feature
decision:

1. [finding]
2. [finding]
3. [finding]

---

### INERTIA vs. ADOPTION COMPARISON TABLE

This is the required cross-subject structural artifact. It is organized around the S-01
Inertia Profile — each row tests one concern or adoption condition from that profile against
all subsequent subjects.

**Completion rules:**
- Rows come from the S-01 Inertia Profile — not invented post-hoc.
- Each subsequent subject's column must state whether their interview confirms, rejects, or
  modifies S-01's concern for their context. "Same as S-01" without explanation fails.
- At least one row must record an unresolved tension — a concern or adoption condition where
  subjects hold irreconcilable positions. Leave it unresolved.

| S-01 Concern / Adoption Condition | S-01 baseline              | S-02 position                  | S-03 position (if present)   | Resolution status            |
|-----------------------------------|----------------------------|--------------------------------|------------------------------|------------------------------|
| [concern or condition from S-01 Inertia Profile] | [S-01's stated position] | [does S-02 confirm, reject, or modify this? cite their answer] | [S-03's position if applicable] | Resolved / Unresolved / Context-dependent |
|                                   |                            |                                |                              |                              |

---

### ARC SIGNAL

3–5 sentences. The arc signal answers: given the inertia evidence from S-01 and the reaction
evidence from subsequent subjects, does this signal have a viable path to adoption? State the
strongest inertia barrier. State whether any subsequent subject's interview evidence addresses
that barrier. Name the single most important unresolved tension from the comparison table.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## Axis Coverage Summary

| Axis                  | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------------------|------|------|------|------|------|
| Output format         | PRIMARY | — | — | SECONDARY | — |
| Phrasing register     | — | PRIMARY | — | — | SECONDARY |
| Lifecycle emphasis    | — | — | PRIMARY | PRIMARY | — |
| Role sequence         | — | — | — | — | PRIMARY |
| Inertia framing       | — | — | — | — | PRIMARY |

## Predicted C-10 / C-11 Coverage

| Variation | C-10 (pre-declared hypotheses) | C-11 (structural cross-subject artifact) | Notes |
|-----------|-------------------------------|------------------------------------------|-------|
| V-01 | PASS — Hypothesis Register locked before table rows | PASS — Tensions Matrix with explicit anti-agreement rules | Both by structural rule; no authorial discipline required |
| V-02 | PASS — "What do I believe right now?" checklist declared before interviews | PASS — Comparison table with completion rules; at least one unresolved row required | C-10 depends on format of the checklist; PARTIAL risk if H-IDs not cited in questions |
| V-03 | PASS — Phase 1 gate prevents any question before hypothesis set is written | PASS — Phase 3 Tensions Table with explicit completion rules | Strongest C-10 mechanism (hard gate); C-11 repairs Round 1 V-03 gap |
| V-04 | PASS — Phase 1 Hypothesis Register + table H-ID citation column | PASS — Phase 3 Tensions Table; structurally unreachable without comparison | Both criteria satisfied by construction; highest confidence |
| V-05 | PARTIAL RISK — S-01 Inertia Profile functions as implicit hypotheses but may not satisfy "committed in writing before any transcript" letter of C-10 if S-01 transcript is written before profile | PASS — Inertia vs. Adoption Comparison Table organized around S-01 profile rows; cannot be completed by agreement | C-10 risk: the profile is extracted from S-01's interview rather than declared before it; evaluators may score PARTIAL |

## Round 2 Prediction

V-04 is predicted to score 100/100 again by construction. V-01 and V-03 are predicted to score
97–100 with C-10 and C-11 passing. V-05 is the high-risk/high-reward variation: if C-10 passes
based on the Inertia Profile serving as the pre-declared hypothesis baseline, V-05 scores 100
and introduces a richer inertia architecture. If C-10 is scored PARTIAL (because the profile
is extracted from the transcript rather than declared before it), V-05 scores 92–95.
V-02 is predicted to score 90–95 depending on whether the prose checklist format is treated as
satisfying C-10's "committed in writing" requirement.
