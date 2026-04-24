# prove-interview — Rubric v5 Variations — Round 5

_Date: 2026-03-15 · Rubric: v5 (C-01–C-15) · Ceiling: 100_

---

## Context

Round 4 produced 5 variations scored against the v4 rubric (C-01–C-13). V-01 scored 100; V-02
(conservative) scored 93.75 under v5 retroactive scoring. The v5 rubric adds two new aspirational
criteria:

- **C-14** — At least one hypothesis is explicitly falsifiable (depth/aspirational)
- **C-15** — Composite signal produced synthesizing all evidence across subjects (format/aspirational)

Aspirational denominator: 8. Each aspirational criterion worth 1.25 points. Ceiling stays 100.

**R4 coverage gaps for C-14 and C-15:**

| Variation | C-14 | C-15 | Aspirational | Note |
|-----------|------|------|--------------|------|
| V-01 R4 | PASS | PASS | 8/8 | Both satisfied by structural necessity |
| V-02 R4 (conservative) | FAIL | FAIL | 3/8 | No falsification condition declared; composite restatement only |

Round 5 goals:
1. Three single-axis variations isolating each of: Output Format, Phrasing Register, Lifecycle Emphasis
2. Two combination variations covering: Lifecycle + Inertia Framing; Output Format + Inertia Framing
3. Every variation satisfies C-14 and C-15 either by structural enforcement or by explicit instruction

---

## Variation Axes

| Axis | Round 4 result | Round 5 focus |
|------|---------------|---------------|
| Output format | V-01 (100) — all criteria by construction | Preserve C-14 via Falsification column; isolate from other axes |
| Phrasing register | V-02 (93.75 retro) — richest voice; C-14/C-15 gaps | Add "what would change my mind?" and anti-restatement verdict gate |
| Lifecycle emphasis | V-03/V-04 (~100) — strong phase gates for C-10/C-13 | Add falsifiability as Phase 1 gate condition; synthesis as Phase 3 gate |
| Role sequence + inertia | V-05 (~95) — inertia profile as implicit hypothesis set | Inertia adoption conditions as falsifiable hypotheses; arc synthesis as C-15 |
| Output format + inertia | Not yet combined | Tables + inertia-first ordering; synthesis via Composite Signal table |

---

## V-01 — Single axis: Output Format

**Axis:** Tabular structure throughout with a mandatory Falsification Condition column in the
Hypothesis Register and a synthesis-quality gate on the Composite Signal section.

**Hypothesis:** Adding a mandatory Falsification Condition column to the Hypothesis Register forces
C-14 by construction — the column cannot be left blank without making the omission structurally
visible. A synthesis gate on the Composite Signal — requiring answers to three integration questions
that cannot be derived by reading the findings list — forces C-15 by structural necessity. All other
criteria (C-09 via typed evidence columns, C-10 via locked register, C-11 via required Tensions Matrix,
C-12 via H-ID column headers, C-13 via explicit phase sentence) carry forward from R4 V-01.
Prediction: 100/100 by construction.

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
written. No question in any subsequent interview table may be written without citing at least one
hypothesis ID from this register.

| ID   | Hypothesis                                                                    | Category                      | Falsification Condition                                                                            |
|------|-------------------------------------------------------------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------|
| H-01 | [a belief about how stakeholders will respond to SIGNAL]                     | assumption / risk / unknown   | [what a subject would have to say — specifically — to force rejection of this hypothesis]           |
| H-02 | [a specific risk or concern you expect to surface]                           | risk                          | [what answer would show this risk does not apply or is substantially overstated]                   |
| H-03 | [a design question these interviews should resolve]                           | unknown                       | [what finding would mean this question resolves against your expectation]                          |
| H-04 | [add additional hypotheses — aim for at least 4]                             |                               |                                                                                                     |

**Register rules:**
- Minimum 4 hypotheses.
- At least one hypothesis must have a non-empty Falsification Condition stating what specific
  interview evidence would disprove it. "If most people disagree" is not a falsification condition —
  it must name the type of answer or evidence that would force hypothesis rejection.
- The register is locked once written. Do not revise hypotheses after any interview table row is written.

---

### STEP 2 — Human Subjects Roster

| ID   | Name    | Role              | Seniority | Domain Expertise | Key Concern                                                         |
|------|---------|-------------------|-----------|-----------------|----------------------------------------------------------------------|
| S-01 | [Name]  | [Role]            | [Level]   | [Domain]        | [What this persona is most likely to push back on or champion]      |
| S-02 | [Name]  | [Role]            | [Level]   | [Domain]        | [Key concern meaningfully distinct from S-01]                       |

Minimum 2 subjects. Subjects must have meaningfully different roles, domains, or concerns.
If two subjects would give the same answers to the same questions, differentiate them before
proceeding.

---

### STEP 3 — Interviews

**Do not write any interview table row until Steps 1 and 2 are complete.** This is a structural
gate: interview rows cannot exist before the Hypothesis Register and Roster are committed.

For each subject in the roster:

#### [S-nn] — Identity

[2–3 sentences: company type or context, relevant prior experience, and at least one concrete
concern or known event that makes this persona specific.]

Swap test: substitute another persona's name into this paragraph. If the interview answers would
still read as plausible, the identity is not specific enough — revise before writing the table.

#### [S-nn] — Interview Table

| Q#  | Question [H-nn]        | Answer (persona voice)                                    | Evidence Signal [type: ...]                                                           | Surprise?                               |
|-----|------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------|-----------------------------------------|
| Q1  | [Question] [H-01]      | [Answer — vocabulary and concerns drawn from Identity]    | [risk: …] / [preference: …] / [constraint: …] / [validation: …] / [invalidation: …] — [one-sentence signal] | Yes — assumed [X], found [Y] / No |
| Q2  | [Question] [H-nn]      |                                                           |                                                                                      |                                         |
| Q3  | [Question] [H-nn]      |                                                           |                                                                                      |                                         |

**Table rules:**
- Every question cites at least one H-ID from the Hypothesis Register in brackets.
- Every answer fails the swap test — no other persona's name can be substituted and have the
  answer remain plausible. Generic answers that could belong to any persona fail.
- Every Evidence Signal carries a type tag from:
  `[risk: …]`, `[preference: …]`, `[constraint: …]`, `[validation: …]`, `[invalidation: …]`
  followed by a one-sentence signal interpretation.
- At least one row per subject has "Yes" in the Surprise column, with explanation of what was
  expected (which hypothesis) and what was found instead.
- Minimum 3 rows per subject.

---

### STEP 4 — Cross-Subject Tensions Matrix

Write this section after all subject tables are complete. It is required.

**Completion rules:**
- Every row compares at least two subjects on a shared dimension.
- Rows recording agreement must explain why the agreement is meaningful or surprising given the
  Hypothesis Register. "Both agreed" alone fails.
- At least one row records an open, unresolved tension. Do not resolve it — leave it as an open
  signal for the feature team.
- Rows may reference H-IDs from the register to connect comparisons to prior beliefs.

| Dimension [H-ID if applicable]  | S-01 position           | S-02 position           | Tension or Agreement [explained]                          | Unresolved? |
|----------------------------------|-------------------------|-------------------------|-----------------------------------------------------------|-------------|
| [topic / concern / H-ID]         | [S-01 view]             | [S-02 view]             | TENSION: [describe] / AGREEMENT: [what it signals]        | Yes / No    |
|                                  |                         |                         |                                                           |             |

---

### STEP 5 — Composite Signal

This section synthesizes — it does not restate. If removing this section would leave the artifact
unchanged, the section has failed. The Composite Signal must add integrated judgment beyond what
a reader can derive by reading the Interview Tables and Tensions Matrix row by row.

Answer all three of the following. Write 4–6 sentences covering all three.

1. **Integrated verdict**: Does the overall evidence from this interview run strengthen, weaken,
   or complicate the original SIGNAL hypothesis? State this directly. Do not hedge.

2. **Dominant finding**: What single finding across all subjects is most decision-relevant for the
   feature team? Name it specifically — this must be a finding, not a topic or theme.

3. **Key open question**: What is the most important thing these interviews did not resolve?
   What would the feature team need to do next to resolve it?

Cite subjects by ID (S-01, S-02, etc.) and hypothesis IDs (H-nn) where relevant.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-02 — Single axis: Phrasing Register

**Axis:** Conversational researcher-notebook register throughout — warm, first-person, narrative.
Falsifiability introduced as a "what would change my mind?" prompt per hypothesis. Composite Signal
framed as a verdict paragraph with an explicit anti-restatement guard.

**Hypothesis:** A conversational register produces richer persona voice (C-02) than a tabular one
because it invites authentic inference rather than cell-filling. The test is whether two quality
prompts — (1) "what would I have to hear to abandon this belief?" per hypothesis (C-14) and
(2) a verdict paragraph instruction that explicitly prohibits restatement (C-15) — can satisfy
both new criteria without collapsing the register into bureaucratic compliance checklists.
Predicted weaknesses: C-12 (H-IDs may not structurally anchor evidence columns) and C-13
(gate sentence may not satisfy the explicit-sentence test). C-14 and C-15 both predicted PASS
if the author follows the register format. Predicted score: 93.75–100 depending on C-12/C-13.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

Think of yourself as a field researcher going into a series of structured conversations to find
out what is really true about this signal. These conversations are not real — but they should
read as if they could be. Every answer comes from a specific person with a specific history,
not a generic voice that could fit anyone.

---

**Before you talk to anyone — what do you believe right now?**

Write down your current beliefs and assumptions before you write a single question. Label them
H-01, H-02, etc. For each one, add two more lines:

- *What would confirm this*: what an interviewee would have to say to strengthen this belief.
- *What would change my mind*: what you would have to hear — specifically — to conclude this
  belief is wrong. This is your falsification condition. At least one hypothesis must have a
  concrete, non-trivial answer to this question.

```
H-01: I believe that [type of stakeholder] will ...
      Confirms: If I hear [answer pattern], this belief holds.
      Changes my mind: If [specific answer or finding], I would have to conclude [opposite].

H-02: My main risk is that ...
      Confirms: ...
      Changes my mind: ...

H-03: I expect the adoption barrier to be ...
      Confirms: ...
      Changes my mind: ...

H-04: I think the biggest surprise will come from ...
      Confirms: ...
      Changes my mind: ...
```

Write at least 4 hypotheses. Do not revise these after you write the interviews. If a conversation
contradicts a hypothesis, that is the finding — not a reason to rewrite the prior.

---

**Who are you talking to?**

Choose at least 2 people with different jobs, different expertise, and different reasons to care
(or not care) about this signal. Before each conversation, write a short pre-interview note:

```
Name: [realistic invented name]
Role: [title and seniority]
Background: [2–3 sentences — industry, what they have worked on, what they worry about,
             a specific past event that shapes their view of this topic]
Why I'm talking to this person: [one sentence — what question only they can answer]
```

Identity check: if you swapped this person's name with someone else's, would the answers still
feel right? If yes, add more specifics before continuing.

---

**The conversations**

Write each interview as a flowing transcript in first-person researcher voice. Let each person
speak in their own register — a senior compliance officer does not talk like a startup founder;
a developer who has been burned by API instability does not answer the same way as one who hasn't.

For each interview:
- Write at least 3 substantive questions
- After each question, note which prior hypothesis it tests — e.g., *(testing H-02)* — even
  just parenthetically
- When an answer surprises you — something that genuinely contradicts what you expected — write
  a short in-flow note: *"I went in expecting [X], but [Name] said [Y]. This shifts how I think
  about [Z]."*
- At least one moment per person should surprise you. A conversation with zero surprises is a
  rehearsal, not an interview.

---

**What did this person actually tell you?**

After each interview, write a findings section — 3 to 5 specific things this person said that
could influence a feature decision. Not summaries of their general views. Findings — concrete,
actionable, specific enough that someone who did not read the transcript could act on them.

If you are struggling to write findings, the interview answers were not specific enough — go back
and sharpen them before continuing.

---

**What do the conversations together tell you?**

After all interviews are written, write a Comparison section. This is required and must be a
table — prose comparisons can avoid the hard parts; tables force specificity.

| What I examined        | [Name 1]     | [Name 2]     | What the difference (or similarity) means                  |
|------------------------|-------------|--------------|------------------------------------------------------------|
| [dimension 1]          | [view]      | [view]       | [what this signals for the feature or the hypothesis]      |
| [dimension 2]          |             |              |                                                            |
| [dimension 3]          |             |              |                                                            |

Completion rules:
- Fill every cell specifically — no "N/A" or "same as above."
- At least one row names a contradiction between the two subjects that you cannot resolve from
  the interviews alone. Leave it unresolved. It is a signal, not a problem to fix.
- Agreement rows must explain why that agreement matters or why it is surprising.

---

**The verdict**

End with a synthesis paragraph — 4–6 sentences. This is not a summary of what each person said.
It is an integration: what do the conversations together tell you about the original signal?

The synthesis must answer three things:
- Does the evidence collected strengthen, weaken, or complicate the original SIGNAL hypothesis?
- What is the single most important finding across all subjects — the one a feature team cannot
  ignore?
- What do you still not know, and what would resolve it?

**Anti-restatement test**: if a reader could derive your verdict by reading the per-person findings
back to back, you have restated rather than synthesized. The verdict must add a judgment that
is not already visible in the parts list. If you cannot point to a sentence in the verdict that
could not be derived from the findings sections, revise the verdict.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-03 — Single axis: Lifecycle Emphasis

**Axis:** Three explicit phases with hard gate rules. Phase 1 gate requires at least one
falsifiable hypothesis before any question is written. Phase 3 synthesis gate requires the
Composite Signal to answer four integration questions and explicitly prohibits restatement.

**Hypothesis:** Making falsifiability a Phase 1 gate condition — Phase 1 is structurally
incomplete until at least one H-ID carries a stated falsification condition — enforces C-14 by
construction. A Phase 3 synthesis gate requiring answers to four integration questions, with an
explicit "could a reader derive this from the tables?" check, enforces C-15 by construction.
C-10 and C-13 are both satisfied by the phase gate mechanism. C-12 (H-IDs as table structure
anchors) is the predicted gap if the transcript format does not require H-ID column headers.
Predicted score: 96.25–100 depending on C-12 column-anchor strictness.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

This skill runs in three sequential phases. Phase 2 cannot begin until Phase 1 is complete and
all gate conditions are satisfied. Phase 3 cannot begin until all Phase 2 interviews and
evidence extractions are written. The phase gate is the structural discipline of this skill —
it is not optional and not implied by step numbering. It is a stated rule.

---

### PHASE 1 — Investigation Brief

Write the Investigation Brief before any interview question or persona answer. The brief is
committed once written and cannot be revised after Phase 2 begins.

**Signal under investigation:** {SIGNAL}
**Topic context:** {TOPIC}

#### Hypothesis Set

Declare every assumption, belief, and risk you carry into these interviews. Label each H-01,
H-02, etc. Aim for at least 4 hypotheses.

For each hypothesis, state three things:
- **Belief**: what you currently think is true about how stakeholders will respond to {SIGNAL}
- **Confirmation signal**: what an interview answer would look like if this hypothesis holds
- **Falsification condition**: what a subject would have to say — specifically — to force you
  to reject this hypothesis. Must be a named evidence type or answer pattern, not general
  disagreement.

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

**Phase 1 gate — falsifiability**: Phase 1 is not complete until at least one H-ID has a
non-empty, specific Falsification condition. A condition that could apply to any hypothesis
("if most people disagree") does not pass this gate. A passing condition names the type of
evidence or answer that would force rejection of that specific hypothesis.

#### Subject Roster

Declare who you will interview and why their perspective is relevant to this hypothesis set.

| ID   | Name   | Role    | Why relevant to this hypothesis set                      |
|------|--------|---------|----------------------------------------------------------|
| S-01 | [Name] | [Role]  | [one sentence — what question only this persona can answer] |
| S-02 | [Name] | [Role]  | [one sentence — meaningfully different from S-01]        |

Minimum 2 subjects with meaningfully different roles, domains, or stances on the signal.

**Phase 1 is complete when:**
1. Hypothesis set is written with at least 4 H-IDs
2. At least one H-ID has a specific, non-trivial Falsification condition
3. Subject roster is declared with at least 2 subjects

**Do not write any interview question until all Phase 1 gate conditions are satisfied.**

---

### PHASE 2 — Interviews

For each subject declared in the Investigation Brief, write their Identity section, transcript,
and Evidence Extraction in order. Complete one subject in full before beginning the next.

#### [S-nn] — [Name]

**Identity**

[2–3 sentences: company type or domain context, relevant prior experience, at least one
concrete concern or known prior event that distinguishes this persona.]

Identity test: substitute another persona's name into this paragraph. If the interview answers
would still read as plausible, add specifics until the answer is no.

**Transcript**

Rules:
- Every question cites at least one hypothesis ID from Phase 1 in brackets: `[H-01]`, `[H-02]`
- Minimum 3 questions per subject, each probing a specific Phase 1 hypothesis or design risk
- Answers are in the persona's voice — vocabulary, framing, and concerns drawn from the Identity
- When an answer contradicts a Phase 1 Falsification condition, mark it immediately:
  > **[FALSIFICATION — H-nn triggered]:** Falsification condition stated: [exact condition].
  > What this subject said: [answer]. Conclusion: [how this forces revision of H-nn].
- When an answer produces a surprise that was not a declared falsification condition, mark it:
  > **[SURPRISE — contradicts H-nn]:** Expected: [what Phase 1 said]. Found: [what was said].
  > Impact: [how this shifts the investigation].

At least one marked moment (FALSIFICATION or SURPRISE) per subject.

**Evidence Extraction**

Extract findings from this subject. These are decisions-relevant signals — not summaries of
what was said.

1. [finding: specific enough that a feature team could act on it]
2. [finding]
3. [finding]

Minimum 3 findings. A finding must be specific enough to act on. "Users want simplicity" is not
a finding. "S-01 requires zero additional IAM roles — their security team runs a 6-week review
cycle that blocks every release" is a finding.

**Phase 2 is complete when all subjects have written Identity, Transcript, and Evidence Extraction.**
**Do not begin Phase 3 until Phase 2 is complete.**

---

### PHASE 3 — Cross-Subject Analysis

Phase 3 begins only after all Phase 2 interviews and evidence extractions are written.

#### Hypothesis Test Table

For each hypothesis declared in Phase 1, record how each subject spoke to it. Note whether
the Falsification condition was triggered.

| H-ID | Hypothesis (brief)     | S-01 response               | S-02 response               | Falsification triggered? | Verdict                             |
|------|------------------------|-----------------------------|-----------------------------|--------------------------|-------------------------------------|
| H-01 | [text]                 | [how S-01 addressed this]   | [how S-02 addressed this]   | Yes / No / Partial       | Confirmed / Contradicted / Split / Untested |
| H-02 |                        |                             |                             |                          |                                     |

#### Tensions Table

| Dimension                      | S-01 position               | S-02 position               | Tension or Agreement                              | Open signal? |
|--------------------------------|-----------------------------|-----------------------------|---------------------------------------------------|-------------|
| [specific topic or H-ID]       | [S-01 stated position]      | [S-02 stated position]      | TENSION: [describe] / AGREEMENT: [why it matters] | Yes / No    |

Completion rules:
- At least one row records an unresolved tension. Do not resolve it.
- Agreement rows explain why the agreement is or is not surprising given Phase 1 hypotheses.

#### Composite Signal

**Phase 3 gate — synthesis quality**: This section is not complete if removing it would leave
the artifact's conclusions unchanged. The Composite Signal must add integrated judgment that
cannot be derived by reading the Hypothesis Test Table and Tensions Table row by row.

Write 4–6 sentences answering all four of the following:

1. **Signal verdict**: Does the Phase 1 signal hypothesis come out of these interviews
   strengthened, weakened, or complicated? State this as a direct claim.

2. **Falsification result**: Were any Phase 1 Falsification conditions triggered? If yes,
   what does that force the team to revise? If no, what does the absence of triggers signal?

3. **Dominant finding**: What single finding across all subjects is most decision-relevant?
   Name it specifically — not a theme, a finding.

4. **Key open question**: What is the most important unresolved tension from the Tensions Table
   and what would the feature team need to do to close it?

Cite subjects by ID (S-01, S-02) and hypothesis IDs (H-nn) where relevant.

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-04 — Combination: Lifecycle Emphasis + Inertia Framing

**Axes:** Phase gates (V-03) + skeptic-first role ordering where the inertia subject's stated
adoption conditions serve as the falsifiable hypothesis set.

**Hypothesis:** The combination of phase gating and inertia-first ordering creates a system
where the Phase 1 gate is naturally satisfied by the SKEPTIC's expected adoption conditions
(each condition is inherently falsifiable — it states what would need to be true for adoption to
be possible, and subsequent interviews either confirm or falsify it). The Phase 3 Arc Signal
is naturally an integrated synthesis rather than a restatement because it must answer: given
everything from Phase 2, does the signal have a viable path past the inertia barrier? C-14 is
satisfied because adoption conditions are falsifiable by construction; C-15 is satisfied because
the arc question cannot be answered by listing per-subject evidence. C-13 is satisfied by
explicit gate sentences. Predicted score: 100/100 by construction on all 15 criteria.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

This skill runs in three sequential phases using inertia-first interview ordering. Phase 2
cannot begin until Phase 1 is complete. Phase 3 cannot begin until all Phase 2 interviews are
complete. The first subject interviewed is always the persona with the deepest investment in
the current approach — the person this signal would most disrupt. Their stated adoption
conditions become the falsifiable hypothesis set that subsequent interviews test.

---

### PHASE 1 — Investigation Setup

Write the Investigation Setup before any interview question is written.

**Signal under investigation:** {SIGNAL}
**Topic context:** {TOPIC}

#### Prior Beliefs

State the beliefs and risks you carry into this investigation. Label H-01, H-02, etc.

For each hypothesis, declare its falsification condition — specifically, what the inertia
subject (S-01) would have to say to force you to revise or reject it:

| ID   | Hypothesis                                                     | Falsification condition                                                                        |
|------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| H-01 | [belief about how the inertia subject will respond to SIGNAL] | [what S-01 would have to say to force revision of this belief — named evidence or answer type] |
| H-02 | [expected barrier or risk in the current approach]            | [what S-01's interview would have to reveal for this barrier to not apply]                     |
| H-03 | [design question the inertia interview should resolve]        | [what finding would resolve this against your expectation]                                     |
| H-04 | [add rows — aim for 4+]                                        |                                                                                                |

**Gate — falsifiability**: Phase 1 is not complete until at least one H-ID has a specific,
non-trivial falsification condition. Generic conditions ("if everyone disagrees") fail this gate.

#### Subject Roster (inertia-first order)

| ID   | Name    | Role   | Stance     | Why this order                                                                          |
|------|---------|--------|------------|-----------------------------------------------------------------------------------------|
| S-01 | [Name]  | [Role] | SKEPTIC    | interviewed first; deepest investment in current approach; concerns become test battery |
| S-02 | [Name]  | [Role] | CHAMPION or EVALUATOR | interviewed after S-01; reactions tested against S-01's inertia profile    |

S-01 must be the persona whose current practice the signal would most disrupt. Their objections
are well-founded and domain-specific, not generic resistance. The goal is to surface what
adoption would actually require, not to defeat them rhetorically.

**Phase 1 is complete when:** prior beliefs with at least one falsifiable H-ID and subject roster
are written. **Do not write any interview question until Phase 1 is complete.**

---

### PHASE 2 — Interviews (inertia-first)

#### S-01 — SKEPTIC

**Identity**

[3–4 sentences: name, role, company type or domain. Focus specifically on what makes S-01's
expertise in the current approach deep and specific — how long they have used it, what they
have built with it, what a switch would cost them in time, rework, or risk.]

**Current-Practice Baseline**

Begin with at least 2 questions about S-01's current approach before introducing the signal.
These establish the baseline that makes their later reactions credible.

- Q1 [H-nn]: [What do you currently do for {TOPIC}? Walk me through your approach.]
  > [S-01 answer — establish depth and specificity of existing investment]

- Q2 [H-nn]: [What is the hardest part about your current approach?]
  > [S-01 answer — a real friction point, not a generic complaint. This is the crack in
  > the inertia that the signal might address — or might fail to address.]

**Signal Reaction**

- Q3 [H-nn]: [Question directly testing a Phase 1 hypothesis]
  > [S-01 answer — skeptic voice with specific objection]
  > **[FALSIFICATION — H-nn triggered]:** *(if applicable — record exact triggering condition)*

- Q4 [H-nn]: [What would have to be true for you to seriously consider adopting this approach?]
  > [S-01 answer — the adoption conditions. This is the most important answer in the interview.
  > Each stated condition is an implicit falsifiable hypothesis: if the signal cannot satisfy it,
  > that condition falsifies the signal's viability for this persona.]

- [Add Q5+ to surface remaining S-01 objections. Minimum 5 questions total for S-01.]

**Inertia Profile**

| Concern or Objection       | Basis in S-01's practice                         | Adoption condition (from Q4)                    | Phase 1 H-ID |
|---------------------------|--------------------------------------------------|-------------------------------------------------|--------------|
| [stated concern]           | [why grounded in S-01's specific role/practice] | [what S-01 said would need to be true]          | H-nn         |

The Inertia Profile becomes the test battery for S-02. Every question asked of S-02 must
address at least one row of this profile.

**Evidence Extraction (S-01)**

1. [finding — specific enough to act on]
2. [finding]
3. [finding]

---

#### S-02+ — Subsequent Interviews

**Identity**

[2–3 sentences: name, role, domain context. Note explicitly what distinguishes this persona
from S-01 — different domain, different adoption stage, different risk profile.]

**Interview**

Questions for S-02 must test the S-01 Inertia Profile:

- Q1 [H-nn]: [Current-practice anchor — what do you currently do for {TOPIC}?]
  > [Answer — establish their baseline before the signal is discussed]

- Q2 [H-nn]: [Question testing S-01 Inertia Profile concern or adoption condition]
  > [Answer — confirm, reject, or qualify S-01's concern for this persona's context]
  > **[SURPRISE — expected [X] based on S-01 Inertia Profile, found [Y]]** *(if applicable)*

- Q3 [H-nn]: [Question testing another S-01 adoption condition or Phase 1 hypothesis]
  > [Answer]

- [Add questions as needed — minimum 3 per subsequent subject]

**Evidence Extraction**

1. [finding]
2. [finding]
3. [finding]

**Phase 2 is complete when all subjects have written Identity, Interview, and Evidence Extraction.**
**Do not begin Phase 3 until Phase 2 is complete.**

---

### PHASE 3 — Synthesis

Phase 3 begins only after all Phase 2 content is written.

#### Inertia vs. Adoption Comparison Table

Rows are drawn from the S-01 Inertia Profile — not invented after the fact.

**Completion rules:**
- Each row corresponds to a concern or adoption condition from the S-01 Inertia Profile.
- Each subsequent subject column states whether their interview confirms, rejects, or qualifies
  S-01's concern for their context. "Same as S-01" without explanation fails.
- At least one row records an unresolved tension. Do not resolve it.

| S-01 Concern / Adoption Condition          | S-01 baseline              | S-02 position                              | Resolution status              |
|--------------------------------------------|----------------------------|--------------------------------------------|--------------------------------|
| [concern from S-01 Inertia Profile]        | [S-01 stated position]     | [confirm / reject / qualify + explanation] | Resolved / Unresolved / Context-dependent |

#### Composite Arc Signal

**Phase 3 gate — synthesis quality**: This section is not complete if it merely restates rows
from the Inertia vs. Adoption Table. It must answer the arc question: given everything from
Phase 2, does this signal have a viable path past the inertia barrier S-01 represents?

Write 4–6 sentences that:

1. **Arc verdict**: Does the signal have a viable adoption path given S-01's resistance and
   subsequent subjects' reactions? State this directly.
2. **Strongest remaining barrier**: Name S-01's strongest concern that subsequent interviews
   did not address or resolve. This is the signal's most important open risk.
3. **Most surprising finding**: What did a subsequent subject reveal that S-01's Inertia Profile
   would not have predicted? Cite subject ID and Phase 1 H-ID if applicable.
4. **Next validation step**: What would the feature team need to validate next before treating
   this signal as evidence of adoption viability?

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## V-05 — Combination: Output Format + Inertia Framing

**Axes:** All-table structure (V-01) + inertia-first interview ordering. The Hypothesis Register
includes a Falsification Condition column and an Inertia Link column predicting which subject
type will most directly test each hypothesis. The Composite Signal is a structured synthesis
table — not a prose paragraph — with a required "Integrated verdict" row that must add judgment
not visible in the per-row evidence.

**Hypothesis:** Combining tables and inertia ordering creates two independent paths to C-14:
(1) the Falsification Condition column in the Hypothesis Register forces it structurally, and
(2) the S-01 adoption conditions in the Inertia Profile are inherently falsifiable hypotheses.
C-15 is forced by the Composite Signal table format: the "Integrated verdict" row cannot be
populated by copying from the comparison table — it requires a synthesized judgment. C-13 is
provided by an explicit gate sentence between each major table. C-12 is provided by H-ID column
references in every interview table. Predicted score: 100/100.

---

You are running /prove:interview for the Signal plugin.

Topic: {TOPIC}
Signal: {SIGNAL}

This skill structures interviews in inertia-first order and uses tabular output for all phases.
The first subject is always the persona most invested in the current approach. The tabular
structure ensures every hypothesis, every finding, and every cross-subject comparison is
captured structurally — not embedded in prose where gaps can hide.

---

### TABLE 1 — Hypothesis Register

Write before any interview. Locked once written. No interview table row may be written before
this table is complete.

| ID   | Hypothesis                                                     | Category                    | Falsification Condition                                                                            | Inertia Link                                                     |
|------|----------------------------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| H-01 | [belief about how stakeholders will respond to SIGNAL]        | assumption / risk / unknown | [what a subject would have to say to force rejection of this hypothesis — named answer type]       | SKEPTIC / CHAMPION / Either — [which subject type tests this most directly] |
| H-02 | [specific risk or barrier you expect to surface]              | risk                        | [what answer would show this risk does not apply or is overstated]                                 |                                                                  |
| H-03 | [design question these interviews should resolve]             | unknown                     | [what finding would resolve this against your expectation]                                         |                                                                  |
| H-04 | [add rows — aim for 4+]                                        |                             |                                                                                                    |                                                                  |

**Register rules:**
- Minimum 4 hypotheses.
- At least one H-ID must have a non-empty, specific Falsification Condition. Generic conditions
  ("if people disagree") fail — must name the evidence type or answer pattern that forces rejection.
- Inertia Link is strongly encouraged — predicting which subject tests which hypothesis makes
  cross-subject analysis structurally grounded.
- Register is locked. Do not revise after any interview table row is written.

**Gate**: TABLE 2 cannot be written until TABLE 1 is complete and the falsifiability gate passes.

---

### TABLE 2 — Subject Roster (inertia-first)

| ID   | Name    | Role   | Stance     | Domain Marker                                                               | Predicted H-IDs tested    |
|------|---------|--------|------------|-----------------------------------------------------------------------------|---------------------------|
| S-01 | [Name]  | [Role] | SKEPTIC    | [what makes them the natural defender of current approach — specific practice or investment] | H-01, H-02, ... |
| S-02 | [Name]  | [Role] | CHAMPION or EVALUATOR | [what distinguishes their perspective from S-01]               | H-03, ...                 |

S-01 is interviewed first. Their stated objections and adoption conditions become the test
battery for S-02.

---

### TABLE 3 — S-01 Interview (SKEPTIC)

**Gate**: TABLE 3 cannot be written until TABLEs 1 and 2 are complete.

#### S-01 Identity

[3–4 sentences: name, role, company type, specific prior practice. Make the depth of S-01's
investment in the current approach visible — how long, what built, what at risk if they switch.
Swap test: substitute S-02's name. If the interview answers would still read as plausible,
revise until the answer is no.]

#### S-01 Interview Table

| Q#  | Question [H-nn]                                             | Answer (S-01 voice)                                               | Evidence Signal [type: ...]                                   | Surprise?              | Inertia Weight      |
|-----|-------------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------|------------------------|---------------------|
| Q1  | [Current-practice baseline — no signal yet] [H-nn]          | [S-01 answer establishing baseline investment and practice]       | [constraint: …] / [preference: …] / etc.                     | No (baseline)          | —                   |
| Q2  | [Pain point in current approach] [H-nn]                     | [real friction specific to S-01's domain — the crack in inertia]  |                                                               |                        | High / Medium / Low |
| Q3  | [Signal introduction — S-01's reaction] [H-nn]              | [skeptic response with specific objection]                        |                                                               | Yes — / No             | High / Medium / Low |
| Q4  | [What would have to be true for you to adopt this?] [H-nn]  | [S-01's stated adoption conditions — each one is a falsifiable claim] |                                                           |                        | High                |
| Q5+ | [Additional objection probe] [H-nn]                         |                                                                   |                                                               |                        |                     |

Inertia Weight: High = condition that blocks adoption entirely; Medium = concern that slows;
Low = preference that could be negotiated.

Minimum 4 rows for S-01 (2 baseline + 2 signal reaction). At least one "Yes" in Surprise column.
Inertia Weight required for signal-reaction rows (Q3 onward).

#### S-01 Inertia Profile Table

| Concern          | H-ID  | Basis in S-01's practice                          | Adoption condition                                   | Inertia Weight      |
|------------------|-------|---------------------------------------------------|------------------------------------------------------|---------------------|
| [objection]      | H-nn  | [why this is a real concern for this specific role] | [what S-01 said would be needed for adoption]       | High / Medium / Low |

---

### TABLE 4 — S-02+ Interviews

For each subsequent subject:

#### [S-nn] Identity

[2–3 sentences: name, role, domain distinction from S-01.]

#### [S-nn] Interview Table

| Q#  | Question [H-nn]                                      | Answer (persona voice)                                  | Evidence Signal [type: ...]                        | Surprise vs. S-01 profile?                                      |
|-----|------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------|
| Q1  | [Current-practice anchor] [H-nn]                    | [S-nn baseline answer]                                  |                                                    | No (baseline)                                                   |
| Q2  | [Testing S-01 Inertia Profile concern 1] [H-nn]     | [S-nn response — confirm / reject / qualify]            |                                                    | Yes — S-01 said [X], [S-nn] said [Y] / No                      |
| Q3  | [Testing S-01 adoption condition or Phase 1 H-ID] [H-nn] |                                                    |                                                    |                                                                 |

Minimum 3 rows. "Surprise vs. S-01 profile?" column must reference S-01's stated position, not
just flag a generic surprise. At least one "Yes" per subsequent subject.

#### Evidence Extraction [S-nn]

1. [finding]
2. [finding]
3. [finding]

---

### TABLE 5 — Cross-Subject Comparison

Rows must come from the S-01 Inertia Profile or the Hypothesis Register — not invented post-hoc.

| Dimension [H-ID]                                    | S-01 (SKEPTIC)          | S-02                                                   | Tension or Agreement                               | Unresolved? |
|-----------------------------------------------------|-------------------------|--------------------------------------------------------|----------------------------------------------------|-------------|
| [S-01 Inertia Profile concern or H-ID]              | [S-01 stated position]  | [confirm / reject / qualify — with specific answer ref] | TENSION: [describe] / AGREEMENT: [why meaningful]  | Yes / No    |

Completion rules:
- At least one unresolved tension row.
- Agreement rows must explain why that agreement matters — not just record that it occurred.

---

### TABLE 6 — Composite Signal

**Gate**: TABLE 6 cannot be written until TABLE 5 is complete. It synthesizes across all evidence
— it does not restate per-row findings.

The Integrated Verdict row must add judgment not derivable from reading TABLE 5 in sequence.
If a reader can reconstruct the verdict by summarizing the Tension or Agreement column, the
synthesis has restated rather than integrated. Revise.

| Signal dimension            | Verdict                                                                                                  |
|-----------------------------|----------------------------------------------------------------------------------------------------------|
| **Integrated verdict**      | [Strengthened / Weakened / Complicated — and why, in one sentence that could not be derived from TABLE 5 alone] |
| **Strongest inertia barrier** | [The S-01 concern that subsequent interviews did not resolve — cite H-ID and S-01 adoption condition] |
| **Most surprising finding** | [Something a subsequent subject revealed that S-01's Inertia Profile would not have predicted — cite S-nn] |
| **Falsification result**    | [Were any H-ID Falsification Conditions triggered? Yes/No — if yes, what must the team revise?]        |
| **Key open question**       | [What the feature team needs to resolve before acting on this signal]                                   |
| **Recommended next signal** | [Which /prove, /scout, or /draft skill should run next and why this signal directs to it]              |

---

Write the completed artifact to:
`simulations/prove/investigations/{topic}-interview-{date}.md`

---

## Axis Coverage Summary

| Axis                  | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------------------|------|------|------|------|------|
| Output format         | PRIMARY | — | — | — | PRIMARY |
| Phrasing register     | — | PRIMARY | — | — | — |
| Lifecycle emphasis    | — | — | PRIMARY | PRIMARY | — |
| Role sequence         | — | — | — | SECONDARY | SECONDARY |
| Inertia framing       | — | — | — | PRIMARY | PRIMARY |

---

## Predicted C-14 / C-15 Coverage

| Variation | C-14 mechanism | C-15 mechanism | Predicted score |
|-----------|---------------|----------------|-----------------|
| V-01 | PASS by construction — Falsification Condition column in Hypothesis Register cannot be left blank | PASS by construction — synthesis gate requires 3 integration questions not derivable from findings list | 100/100 |
| V-02 | PASS by instruction — "what would change my mind?" per hypothesis; predicted FAIL risk if author skips this line | PASS by instruction — anti-restatement test is explicit; predicted FAIL risk if author writes summary not verdict | 91.25–100 |
| V-03 | PASS by gate — Phase 1 gate explicitly requires at least one falsifiable H-ID before Phase 2 unlocks | PASS by gate — Phase 3 synthesis gate requires 4 integration answers; "could a reader derive this?" check stated | 96.25–100 |
| V-04 | PASS by construction — adoption conditions in S-01 Inertia Profile are inherently falsifiable (each states a condition the signal must satisfy); Phase 1 gate also requires explicit falsification condition | PASS by construction — Arc verdict requires answering whether signal has viable adoption path; this cannot be restated from comparison table rows | 100/100 |
| V-05 | PASS by dual-path construction — Falsification Condition column (TABLE 1) and S-01 adoption conditions (TABLE 3 Inertia Profile) are independent paths to C-14 | PASS by construction — TABLE 6 Integrated Verdict row has explicit anti-restatement gate; synthesized judgment must add content not in TABLE 5 | 100/100 |

---

## Round 5 Prediction

V-01, V-04, and V-05 are predicted to score 100 by structural enforcement of all 15 criteria.
V-03 is predicted to score 96.25–100 depending on whether the transcript format includes H-ID
column anchors meeting C-12 strictness (interview is in freeform transcript style with H-ID
citations, not a structured table with H-ID column headers). V-02 is the intentional C-12/C-13
sacrifice: the conversational register trades structural rigor for voice quality; the predicted
gap is that prose transcripts with parenthetical H-ID citations do not satisfy C-12's requirement
for H-IDs as structural table anchors, and the "before you talk to anyone" section may not
contain the explicit gate sentence required by C-13. V-02's value is confirming whether
instruction-driven compliance (anti-restatement test, "what would change my mind?") outperforms
structural enforcement for a skilled author who follows the instructions.

The single-axis result to watch: if V-02 scores 100 in Round 5 despite the structural gaps, it
means the phrasing register axis drives sufficient author discipline to satisfy C-12 and C-13
even without structural enforcement — which would expand the design space for future variations.
