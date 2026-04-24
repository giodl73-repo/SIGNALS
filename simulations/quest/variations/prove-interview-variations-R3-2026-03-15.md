# prove-interview — Round 3 Variations (V-01 through V-05)

---

## V-01 — Phase-Criterion Ownership

**Axis:** Lifecycle emphasis — each structural section is labeled with the single rubric concern it owns. No phase bundles multiple criteria.

**Hypothesis:** When phases own exactly one criterion, the author cannot skip a criterion by accident. The structure demands compliance; the author only has to follow the structure.

---

```markdown
You are running the prove-interview skill for topic: {topic}

Simulate stakeholder or customer interviews for this topic. Each interview is a simulation —
grounded in the persona's documented knowledge and concerns, not a real conversation.

Run at least two subjects with meaningfully different roles. For each subject, complete all
phases below in order. Each phase owns exactly one structural purpose — do not merge phases.

---

### PHASE 1 — PERSONA IDENTITY [owns: C-01]

Declare the subject's identity before anything else.

Required fields:
- Name (or role label if unnamed)
- Title and function
- Organizational context (what team, company type, or domain they operate in)

A subject with no declared identity fails Phase 1. Do not proceed to Phase 2 until
identity is complete.

---

### PHASE 2 — PRIOR KNOWLEDGE SCOPE [owns: C-02]

Declare what this subject knows, what they do not know, and what they care about —
before any questions are asked or answers given.

Required fields:
- What they know about {topic}
- What blind spots or gaps they carry
- Their primary concern or stake in this decision

A subject with no prior knowledge section fails Phase 2.

---

### PHASE 3 — EXPECTATION REGISTER [owns: C-13]

Before the interview transcript begins, write a register of what you expect this subject
to say and why. This register makes SURPRISING / CONFIRMING / INCONCLUSIVE labels
structurally mandatory — you cannot retroactively decide what was surprising.

Format (copy this template for each expectation):

```
Expectation E-[N]: [What you expect them to say]
Basis: [Why — their role, their blind spot, or their declared concern]
```

Write at least two expectations per subject. The register closes before the transcript opens.

---

### PHASE 4 — INTERVIEW TRANSCRIPT [owns: C-03, C-06, C-12]

Write the interview as a transcript. Questions must:
- Probe the concerns declared in Phase 2, not generic topics
- Include at least one follow-up question triggered by a specific prior answer

For each follow-up, embed the trigger inline using this template:

```
Q [follow-up, triggered by: "[exact phrase from their last answer]"]: [question text]
```

Answers must be written in the persona's distinct voice — vocabulary, framing, and
concern level must match the role declared in Phase 1. Answers that could belong to
any persona fail.

---

### PHASE 5 — MOMENT LABELING [owns: C-05, C-14]

After the transcript, label at least one moment per subject using one of three labels:

```
SURPRISING (expected: [E-N from register], got: [what actually happened])
CONFIRMING (validates: [E-N from register])
INCONCLUSIVE (moment: [what was said], reason: [why neither label fits])
```

INCONCLUSIVE is not a failure — it is evidence of honest reading. If every moment was
unambiguously one of the other two labels, write: "All labeled moments were unambiguous —
no INCONCLUSIVE cases in this interview."

Do not label a moment SURPRISING or CONFIRMING without a reference to the expectation
register from Phase 3.

---

### PHASE 6 — EVIDENCE EXTRACTION [owns: C-04, C-08]

Extract at least one concrete evidence item per subject. Evidence must not be left
implicit in the transcript. Each item requires:

```
Evidence [N]:
  Type: [adoption risk | feasibility concern | requirement gap | scope signal | constraint | other]
  Finding: [the concrete insight, concern, requirement, or contradiction]
  Source: [quote or paraphrase from transcript that grounds it]
```

Evidence embedded only inside the transcript without a dedicated extraction section fails.

---

### PHASE 7 — VOICE DIVERGENCE NOTE [owns: C-11]

After all subjects, write one meta-observation naming a concrete contrast in how two
subjects were made to sound different. Cite a specific vocabulary choice, framing
preference, or concern priority. Generic observations ("they had different roles")
without citing a specific voice difference fail.

---

### PHASE 8 — CROSS-INTERVIEW SYNTHESIS [owns: C-09]

Aggregate findings across all subjects. Name at least one of:
- A pattern visible across multiple subjects
- A contradiction between subjects
- A convergence that strengthens a signal

Connect individual evidence items from Phase 6 into a composite signal for {topic}.

(Skip Phase 8 and note N/A if only one subject was run.)

---

### PHASE 9 — SIMULATION FIDELITY NOTE [owns: C-10]

Close with a brief meta-note distinguishing grounded claims from constructed plausibility.
Name at least one specific basis for a grounded claim. Example framing:

"One last thing about this simulation: [subject]'s concern about [X] is grounded in
[documented basis]. Their position on [Y] is constructed plausibility — there is no
direct evidence for it, only role-consistent inference."
```

---

## V-02 — Expectation Register Axis

**Axis:** Lifecycle emphasis — the expectation register is foregrounded as the primary architectural constraint. All downstream labels derive from it.

**Hypothesis:** When the register is the structural anchor, SURPRISING / CONFIRMING labels become a verification pass against a committed prediction, not an authorial judgment applied after reading.

---

```markdown
You are running the prove-interview skill for topic: {topic}

Simulate stakeholder or customer interviews. The interview is a simulation — grounded
in each persona's documented knowledge and concerns.

The organizing principle of this skill is the EXPECTATION REGISTER. Before a single
question is asked, you commit to predictions. After the interview, you verify against
them. This structure prevents retroactive labeling.

---

## STEP 1 — ROSTER

List all subjects you will interview. For each:
- Role and title
- Organizational context
- One sentence on their stake in {topic}

Minimum: two subjects with meaningfully different roles.

---

## STEP 2 — EXPECTATION REGISTER (run before all transcripts)

For each subject in the roster, write their prior knowledge scope and your predictions
before opening any transcript.

### [Subject name] — Pre-Interview Profile

**What they know:** [domain knowledge, prior exposure to {topic}]
**What they don't know:** [blind spots, gaps in their context]
**What they care about:** [their primary concern or stake]

**Predictions before this interview:**

| ID | Prediction | Basis |
|----|-----------|-------|
| [S1-E1] | [What you expect them to say or reveal] | [Their role, blind spot, or declared concern] |
| [S1-E2] | [Second prediction] | [Basis] |
| [S1-E3] | [Optional third] | [Basis] |

Repeat for every subject. Close the register with a horizontal rule before opening
the first transcript. Nothing written after this line counts toward the register.

---

## STEP 3 — INTERVIEW TRANSCRIPTS

Run one transcript per subject. For each:

**Voice rule:** Every answer must sound like this specific person — vocabulary, level
of technical fluency, and concern priority must match their declared profile. If an
answer could belong to any of your subjects, rewrite it.

**Question rule:** Questions must probe the concerns declared in Step 2. Include at
least one follow-up per interview. Mark follow-ups with their trigger:

  Q [follow-up]: [question text]
  ↑ triggered by: "[exact phrase from the previous answer]"

**Moment labeling rule:** As you write the transcript (or immediately after), label
at least one moment per subject using the register predictions as reference:

  SURPRISING (expected: [prediction ID], got: [what actually happened])
  CONFIRMING (validates: [prediction ID])
  INCONCLUSIVE (moment: [what was said], reason: [why neither label fits cleanly])

If every labeled moment was unambiguous, note it explicitly. Do not skip labeling
because a moment was "interesting" — every notable moment gets a label or an
explanation of why no label fits.

---

## STEP 4 — EVIDENCE LOG

After all transcripts, extract evidence per subject. Do not leave evidence implicit.

For each item:
  Signal type: [adoption risk | feasibility concern | requirement gap | scope signal |
                constraint | behavior gap | other — name it]
  Finding: [the concrete insight or concern]
  Grounded in: [transcript quote or paraphrase]

At least one item per subject.

---

## STEP 5 — SYNTHESIS

Aggregate across subjects. Name:
- At least one pattern, contradiction, or convergence visible across subjects
- What the combined evidence says about {topic} readiness or risk

Connect evidence items from Step 4 into a composite signal.

(Mark N/A if only one subject ran.)

---

## STEP 6 — VOICE DIVERGENCE CHECK

Name one concrete contrast between two subjects' voices. Cite a specific word,
phrase, framing, or concern priority that makes them sound different. Example:

  "[Subject A] uses the word 'compliance' where [Subject B] says 'policy overhead' —
  the same concept, but [A]'s framing reflects legal training while [B]'s reflects
  operational friction."

Generic role-difference observations do not satisfy this step.

---

## STEP 7 — FIDELITY NOTE

Close with a sentence or two distinguishing what is grounded (based on documented
persona knowledge or domain context) from what is constructed plausibility.
Name at least one specific grounding basis.
```

---

## V-03 — INCONCLUSIVE Label Axis

**Axis:** Role sequence + output format — INCONCLUSIVE is introduced as a peer label with its own structural section. All three labels (SURPRISING, CONFIRMING, INCONCLUSIVE) are treated as equally valid outcomes, with explicit guidance for distinguishing them.

**Hypothesis:** Making INCONCLUSIVE a required option removes the forcing function that produces false SURPRISING labels. When authors have an honest exit, SURPRISING and CONFIRMING become more trustworthy.

---

```markdown
You are running the prove-interview skill for topic: {topic}

Simulate interviews with at least two stakeholders or customers who have meaningfully
different roles, knowledge, and concerns. The simulation is grounded in each persona's
declared profile — it is not a real interview, but it is not a generic one either.

---

### Labeling System

Every notable moment in an interview must carry one of three labels. All three are
valid. Choosing the right one is the work.

**SURPRISING** — the moment contradicted a prior expectation.
  Required form: `SURPRISING (expected: X, got: Y)`
  Use when: the answer went against something you predicted before the interview.

**CONFIRMING** — the moment validated a prior expectation.
  Required form: `CONFIRMING (validates: Z)`
  Use when: the answer landed exactly or approximately where you expected.

**INCONCLUSIVE** — the moment was notable but fits neither label cleanly.
  Required form: `INCONCLUSIVE (moment: [what was said], reason: [why it doesn't resolve])`
  Use when: the subject said something significant, but you cannot honestly say
  whether it surprised you or confirmed you. Ambiguity is real evidence.

Before any transcript begins, write your prior expectations per subject.
This is required — labels cannot be applied honestly without a committed prediction.

---

### Run Order

For each subject:

1. **IDENTITY** — Declare role, title, and organizational context.

2. **PRIOR KNOWLEDGE** — State what they know, what they don't, and what they
   care about. Be specific to this role.

3. **EXPECTATION REGISTER** — List 2–3 predictions with their basis before the
   transcript opens. Format:
   ```
   Prediction [N]: [what you expect them to say]
   Basis: [role, blind spot, or declared concern]
   ```

4. **TRANSCRIPT** — Write the interview. Answers must be in this persona's voice —
   vocabulary and framing must match the declared profile. Questions must probe
   their declared concerns. At least one follow-up must show what triggered it:
   ```
   Q (follow-up, triggered by: "[their exact phrase]"): [question text]
   ```

5. **MOMENT LOG** — After the transcript, label at least one moment:
   ```
   SURPRISING (expected: [prediction N], got: [what happened])
   CONFIRMING (validates: [prediction N])
   INCONCLUSIVE (moment: [quote or paraphrase], reason: [why it doesn't resolve])
   ```
   If you find no INCONCLUSIVE moments: write "All labeled moments in this
   interview were unambiguous — no INCONCLUSIVE cases." This statement is
   required if INCONCLUSIVE is absent.

6. **EVIDENCE** — Extract evidence items explicitly. For each:
   ```
   Type: [adoption risk | feasibility concern | requirement gap | scope signal |
          constraint | other]
   Finding: [concrete insight]
   Source: [quote or paraphrase from transcript]
   ```

---

### After All Subjects

**Voice divergence note:** Name one concrete vocabulary, framing, or concern-priority
contrast between two subjects. Specific words or phrases required.

**Synthesis:** Aggregate patterns, contradictions, or convergences across subjects.
Connect evidence items into a composite signal. (N/A if one subject only.)

**Fidelity note:** Distinguish grounded claims from constructed plausibility. Name
at least one specific grounding basis.
```

---

## V-04 — Inline Format Templates (Combination: Phase Ownership + Templates)

**Axis:** Output format + lifecycle emphasis — every format template is embedded inline the first time it appears, making the form self-replicating for subsequent sections without external documentation.

**Hypothesis:** When the first interview uses a template explicitly, subsequent interviews inherit the form by example. The author follows a pattern rather than reconstructing a requirement.

---

```markdown
You are running the prove-interview skill for topic: {topic}

Simulate stakeholder or customer interviews grounded in each persona's documented
knowledge and concerns. Run at least two subjects.

This prompt embeds a format template the first time each structure appears.
Copy and adapt the template for every subsequent subject — the form propagates itself.

---

## PRE-INTERVIEW SETUP

Before any transcript, complete setup for all subjects.

### Subject Roster

List every subject you will interview:

```
Subject A: [Name or role label] — [Title, organization type]
Subject B: [Name or role label] — [Title, organization type]
[Add more as needed]
```

### Expectation Register (all subjects, before all transcripts)

For each subject, write their profile and your predictions. The register closes
before the first transcript opens — predictions cannot be added after reading answers.

**[TEMPLATE — copy for each subject]**

```
Subject: [Name/role]

Prior knowledge:     [What they know about {topic}]
Blind spots:         [What they don't know or misunderstand]
Primary concern:     [What they care about most]

Predictions:
  P-[A1]: [What you expect them to say] — basis: [their role/blind spot/concern]
  P-[A2]: [Second prediction] — basis: [...]
  P-[A3]: [Optional third] — basis: [...]
```

---

## INTERVIEW TRANSCRIPTS

Run one transcript per subject. Use the templates embedded below.

---

### INTERVIEW: [Subject A name/role]

**Voice contract:** [Subject A] sounds like [1-sentence voice description — 
vocabulary level, domain framing, emotional register]. Answers that could belong 
to any subject will be rewritten before this section closes.

**[TRANSCRIPT TEMPLATE — copy this structure for subsequent interviews]**

```
Q: [Opening question anchored to Subject A's declared concern]

A (Subject A): [Answer in persona voice]

Q (follow-up, triggered by: "[exact phrase from A's previous answer]"): [question]

A (Subject A): [Answer]

[Continue as needed — minimum 3 exchanges]
```

**Moment log:**

```
[MOMENT TEMPLATE — copy for every labeled moment in this and all subsequent interviews]

SURPRISING (expected: P-[A1], got: [what actually happened])
  OR
CONFIRMING (validates: P-[A1])
  OR
INCONCLUSIVE (moment: "[quote from transcript]", reason: [why neither label fits])

If no INCONCLUSIVE moments: "All labeled moments were unambiguous — no INCONCLUSIVE cases."
```

---

### INTERVIEW: [Subject B name/role]

**Voice contract:** [Subject B] sounds like [voice description — must name at least
one contrast with Subject A: where A says "[word]", B says "[different word]"].

[Copy the transcript template from Subject A's section. Adapt to Subject B's
declared concerns and voice contract.]

[Copy the moment log template. Apply to Subject B's transcript.]

---

## EVIDENCE LOG (all subjects)

Extract evidence after all transcripts.

**[EVIDENCE TEMPLATE — copy for each item]**

```
Evidence [N] — Subject [A/B/...]:
  Signal type: [adoption risk | feasibility concern | requirement gap | 
                scope signal | constraint | behavior gap | other]
  Finding:     [concrete insight, concern, requirement, or contradiction]
  Grounded in: "[direct quote or close paraphrase from transcript]"
```

Minimum: one item per subject. Evidence that remains implicit in the transcript
without a dedicated extraction entry fails.

---

## POST-INTERVIEW ANALYSIS

### Voice Divergence Note

Name one concrete contrast between two subjects. Cite specific vocabulary, framing,
or concern priority — not role difference.

Example form: "Where [A] reaches for [word/phrase], [B] uses [different word/phrase].
This reflects [A's] [domain/background] versus [B's] [domain/background]."

### Synthesis

Aggregate findings across subjects. Name patterns, contradictions, or convergences.
Connect evidence items from the log into a composite signal for {topic}.

(Mark N/A if only one subject was run.)

### Fidelity Note

Close with one paragraph distinguishing grounded claims from constructed plausibility.
Name at least one specific grounding basis.

Example: "One last thing: [Subject A]'s concern about [X] is grounded in [specific basis].
Their position on [Y] is constructed plausibility — role-consistent inference without
direct evidence."
```

---

## V-05 — Phrasing Register Shift + Role Sequence Rationale

**Axis:** Phrasing register (descriptive/conversational) + role sequence (explicit sequencing rationale). Instructions are written in plain descriptive prose rather than imperative commands. Role order is motivated.

**Hypothesis:** A conversational register reduces template-following anxiety, producing more natural persona voice. Making role sequence explicit and motivated encourages authors to think about what each subject adds before writing them, leading to more distinct profiles.

---

```markdown
You are running the prove-interview skill for topic: {topic}

The goal is to simulate interviews with stakeholders or customers — not to produce
a real conversation, but to produce a grounded one. Each subject has a documented
profile, a set of concerns, and a way of talking about the world. The interview
surfaces what they would actually say.

---

### Who to interview and why the order matters

Choose at least two subjects with genuinely different relationships to {topic}.
The sequence matters: start with the subject closest to the decision, then move
toward subjects with increasing distance or skepticism. This order lets skepticism
challenge what you learned from the first interview.

Before writing any interview, write a short note explaining your sequence:

  "I'm starting with [Subject A] because [their relationship to the decision].
   Then moving to [Subject B] because [what their distance or skepticism adds].
   The sequence matters because [what the second interview can challenge or 
   complicate from the first]."

If you're running more than two subjects, extend this reasoning for each.

---

### Before any interview begins

For each subject, write a profile and a set of predictions. This happens before
any questions are asked.

The profile covers three things: what they know about {topic}, what they don't
know or haven't thought about, and what they're most concerned with. Be specific
to this person's role and context — a profile that could describe anyone doesn't
help you write answers in their voice.

The predictions are your honest guesses about what they'll say. Write them down
before you start. You need them because the labeling system below requires a
committed prior — without it, you're just deciding after the fact what was
interesting.

A good prediction format looks like this:

  Prediction P-[S1-1]: I expect them to push back on [X] because [their role
  means they've seen Y fail before].

Write two or three predictions per subject. Then close the prediction section.
Nothing added after the transcript starts counts as a prior expectation.

---

### Writing the interviews

When you write the transcript, keep three things in mind:

**Voice.** Each subject sounds like themselves. That means their vocabulary, their
level of technical fluency, and how much they trust the framing you bring to them.
A skeptical operations person doesn't say "the implementation vector is unclear" —
they say "I don't know how this actually gets rolled out." If an answer could have
come from anyone, it came from no one. Rewrite it.

**Questions that follow.** Good questions in a simulated interview don't just move
the topic forward — they respond to what was just said. When you write a follow-up,
show what triggered it:

  Q (follow-up, triggered by: "[their exact phrase]"): [your question]

If a follow-up could have appeared at any point in the interview, it wasn't really
a follow-up. It was a question you planned ahead of time.

**Labeling moments as you go.** When something notable happens in the transcript —
an answer that surprised you, confirmed your prediction, or didn't resolve either
way — label it. You have three options:

  SURPRISING (expected: [prediction ID], got: [what actually happened])
    — when the answer contradicted your prediction

  CONFIRMING (validates: [prediction ID])
    — when the answer landed where you expected

  INCONCLUSIVE (moment: "[quote]", reason: [why it doesn't settle either way])
    — when the answer was significant but you can't honestly say whether it
      surprised you or didn't. Ambiguity is real. An INCONCLUSIVE moment is
      evidence, not a failure.

If you find no INCONCLUSIVE moments in an interview, write: "All labeled moments
in this interview were unambiguous — no INCONCLUSIVE cases."

---

### After the transcript: pulling evidence out

After each interview, extract the evidence explicitly. Don't leave it sitting inside
the dialogue. For each item you extract, name what kind of signal it is — that's
what makes it usable downstream.

  Signal type: [adoption risk | feasibility concern | requirement gap | scope signal |
                constraint | behavior gap | or name your own]
  Finding: [what you learned]
  Grounded in: [quote or paraphrase from the transcript]

At least one item per subject.

---

### After all interviews

A few things to close with:

**Voice divergence.** Name one specific contrast between how two subjects sound.
Not "they had different roles" — point to a word, a phrase, a framing preference,
or a concern priority. The contrast should be something you made intentional.

**Synthesis.** Look across subjects. What patterns appeared in more than one
interview? What did one subject say that another contradicted? What does the
combined picture say about {topic}? Connect the individual evidence items into
something composite. (Skip this if you only ran one subject.)

**Fidelity note.** Close with a brief observation about the simulation itself.
Something like: "One thing worth naming about this simulation: [Subject X]'s
concern about [Y] is grounded in [specific basis]. Their position on [Z] is
constructed — role-consistent plausibility, not direct evidence." This helps
the reader know what to weight and what to hold lightly.
```

---

## Variation Summary

| Variation | Primary Axis | Key Structural Bets | New v3 Criteria Targeted |
|-----------|-------------|---------------------|--------------------------|
| V-01 | Phase-criterion ownership | Each phase labeled with single rubric concern it owns; phases cannot be merged | C-13, C-14, C-15, C-16 |
| V-02 | Expectation register as anchor | Register closes before transcripts open; table format enforces prediction commitment | C-13 (primary), C-05 |
| V-03 | INCONCLUSIVE as peer label | All three labels introduced with equal weight; INCONCLUSIVE absence requires explicit acknowledgment | C-14 (primary), C-05 |
| V-04 | Inline format templates | First instance of every structure embeds copy-paste template; subsequent sections inherit form | C-16 (primary), C-15 |
| V-05 | Phrasing register + role sequence | Descriptive prose register; role sequence motivated before writing begins | C-13, C-14 via natural framing |
