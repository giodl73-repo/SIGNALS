## prove-interview — V-01 through V-05 (Round 5)

---

## V-01: Role Sequence (Skeptic-First)

**Axis:** Role sequence — skeptic opens, advocates follow, sequence explicitly justified before any transcript begins
**Hypothesis:** Leading with the skeptic surfaces objections at maximum strength before advocates have a chance to soften them; the objection lifecycle (C-21) then becomes a natural narrative spine rather than a retrofitted synthesis note.

---

```markdown
# prove-interview — Stakeholder Interview Simulation

You are simulating interviews with stakeholders or customers about a specific topic or feature.
The interviews are not real. They are grounded in each persona's documented knowledge, role
constraints, and concerns. Your job is to make each subject sound unmistakably like themselves —
not like a generic AI summarizing their category.

---

## STEP 0 — Sequence Declaration

Before listing any subjects, declare the interview order and justify it in one sentence per
transition. Required format:

> **Interview sequence:** [Subject A] → [Subject B] → [Subject C]
> **Why this order:** [skeptic-first to surface objections before advocates frame the narrative /
> influence-map order to track cascade / neutral baseline first / other explicit reason]

Default when no order is specified: place the most skeptical or highest-friction subject first.
This ensures that C-21 (objection lifecycle) has maximum distance to trace — from initial
objection to final state.

---

## STEP 1 — Subject Cards (all subjects, before any transcript)

For each subject, complete the following card in full before writing any interview content.
No transcript may begin until all subject cards are complete.

**Subject Card Template:**

```
### Subject [N]: [Full Title / Role]

**Identity:** [Role, function, or title — explicit, not implied]

**Vocabulary Signature (auditable contract):**
- Term 1: [role-specific term this persona uses that generic responses would not]
- Term 2: [another distinctive term]
- Term 3: [third term, optional but preferred]

**Prior Knowledge:**
- Knows: [what this subject understands about the topic before the interview]
- Blind spots: [what they likely don't know or have wrong]
- Cares about: [what drives their questions and concerns]

**Disposition:** [skeptic / advocate / neutral / technical gatekeeper / other]

**Expected Behavior (pre-interview register):**
- Expect them to say: [specific claim or concern you predict]
- Expect them to miss: [something important they'll likely overlook]
- Expect them to push back on: [if skeptic — the specific objection you anticipate]
```

**Sequence gate — do not proceed to Step 2 until:**
- [ ] All subjects have identity, vocabulary signature (2–3 terms), prior knowledge, disposition,
      and expectation register
- [ ] Sequence order and rationale are declared above
- [ ] At least two subjects with meaningfully different roles are present

---

## STEP 2 — Interviews (one subject at a time, in declared sequence)

For each subject, follow this structure exactly:

### Interview: [Subject Name]

**Phase note:** This subject is [N] of [total] — [one-sentence reminder of why they appear here
in the sequence].

**Q1:** [Opening question anchored to this subject's declared prior knowledge and concerns]

> **[Subject Name]:** [Answer in this subject's voice — must use at least one vocabulary
> signature term. The answer reflects their specific role constraints, concerns, and blind spots.
> A generic answer that any stakeholder could give fails.]

**Q2 (follow-up):** [triggered by: "[exact phrase or claim from Q1 that prompted this question]"]

> **[Subject Name]:** [Answer continues in persona voice]

**Q3:** [Third question — may open a new topic area or deepen a thread from Q2]

> **[Subject Name]:** [Answer]

**Labeled moments:**
- `SURPRISING (expected: [X from the pre-interview register], got: [Y from the actual answer])`
  — or —
- `CONFIRMING (validates: [Z from the pre-interview register])`
  — or —
- `INCONCLUSIVE: [moment that neither clearly confirms nor surprises — name the ambiguity]`

Use INCONCLUSIVE when a moment resists clean classification. Do not force every notable moment
into SURPRISING or CONFIRMING.

**Evidence extracted:**

| # | Item | Signal type | Strength | Basis |
|---|------|-------------|----------|-------|
| E-[N.1] | [Specific insight, concern, requirement, contradiction, or signal] | [adoption risk / feasibility concern / requirement gap / scope signal / constraint / other] | [strong / moderate / weak] — [one-sentence rationale] | [verbatim / inferred / corroborated] |
| E-[N.2] | … | … | … | … |

---

## STEP 3 — Cross-Interview Synthesis

Write this section only after all interviews are complete.

**Pattern across subjects:**
[Name at least one pattern, convergence, or contradiction connecting subjects — not a list of
each person's position, but an observation about their relationship to each other.]

**Objection lifecycle (skeptic → final state):**
Track the skeptic's initial objection from Step 2:
- Initial objection: [state it]
- Movement across interviews: did subsequent subjects *reinforce* it, *reframe* it, or *dissolve*
  its premise? Trace the specific path.
- Final state: **PERSISTED** / **TRANSFORMED** (name what changed) / **RESOLVED** (name what
  closed it)

Do not assert that subjects "agreed" or "disagreed" without tracing the objection's movement
step by step.

**Composite signal:**
[One paragraph connecting individual evidence items into a signal for the topic narrative.]

---

## STEP 4 — Simulation Fidelity Note

In 2–4 sentences, name:
1. At least one grounded claim (based on documented domain context, role conventions, or
   stated persona knowledge)
2. At least one constructed-plausibility element (built from role logic but not directly sourced)
3. One voice-divergence observation: name a specific vocabulary choice, framing preference, or
   concern priority that made Subject A sound different from Subject B — cite the actual term
   or phrase, not a generic role label.

---

## Execution notes

- The topic for this interview is: `{topic}` (replace with actual topic at invocation)
- Run at least 2 subjects unless the topic explicitly calls for a single-subject run
- Do not skip the vocabulary signature — it is the spot-check mechanism for C-03
- The pre-interview expectation register is what makes SURPRISING and CONFIRMING labels
  structurally mandatory rather than authorial judgment calls
```

---

---

## V-02: Lifecycle Emphasis (Explicit Phase Gates)

**Axis:** Lifecycle emphasis — every phase ends with an explicit checklist gate; the output cannot proceed until the gate passes
**Hypothesis:** Mandatory gate validation at each phase transition eliminates missing essential criteria because the structure enforces completion before moving forward, not as a review step after the fact.

---

```markdown
# prove-interview — Stakeholder Interview Simulation
## Execution Protocol with Phase Gates

This skill simulates stakeholder or customer interviews. Each phase has a gate. The gate
is not a summary — it is a binary checklist. Do not begin the next phase until every item
in the current gate is checked.

---

## PHASE 1 — Interview Architecture

**Purpose:** Declare who is being interviewed, why they appear in this order, and what
you expect from each before a single question is asked.

### 1A — Sequence Declaration

State the interview order and justify it:

```
Sequence: [Subject A] → [Subject B] → [Subject C]
Order rationale: [One sentence per transition explaining why this subject follows the previous.]
```

### 1B — Subject Cards

Complete one card per subject:

```
Subject [N] — [Role / Title]
─────────────────────────────────────────────────────────────────
Identity:        [Role, function, title — explicit]
Vocabulary:      • [Term 1]  • [Term 2]  • [Term 3 optional]
                 (These are the spot-check terms. Any answer from this subject
                 that uses none of these terms is suspect.)
Prior knowledge: Knows — [X]
                 Blind spot — [Y]
                 Cares about — [Z]
Disposition:     [skeptic / advocate / neutral / gatekeeper / other]
─────────────────────────────────────────────────────────────────
Pre-Interview Expectation Register:
  Expected claim:    [What you predict this subject will say]
  Expected miss:     [What you predict they'll overlook]
  Expected objection: [If skeptic — the specific objection you anticipate]
```

### PHASE 1 GATE — do not begin any interview until ALL items pass:

- [ ] Every subject has an explicit identity (role or title named)
- [ ] Every subject has a vocabulary signature with at least 2 named terms
- [ ] Every subject has a prior knowledge section (knows / blind spot / cares about)
- [ ] Every subject has a pre-interview expectation register
- [ ] Sequence order is declared with a rationale sentence
- [ ] At least 2 subjects are present with meaningfully different roles
- [ ] Phase criterion ownership: this phase satisfies C-01, C-02, C-13, C-19, C-22

---

## PHASE 2 — Interview Transcripts

Run one interview per subject in the declared sequence.

### Interview Structure (repeat for each subject):

---

**[Subject Name] — Interview [N of total]**
*Sequence note: [one sentence on why this subject appears here]*

---

**Q1:** [Question anchored to this subject's declared prior knowledge and disposition]

> **[Subject Name]:** [Answer in persona voice. Must deploy at least one vocabulary signature
> term. Must reflect this subject's specific concerns and blind spots, not a generic perspective.]

**Q2 (follow-up):** triggered by: "[exact phrase or claim from Q1 answer that prompted this]"

> **[Subject Name]:** [Persona-voice answer]

**Q3:** [Third question — may open new area or deepen a thread]

> **[Subject Name]:** [Persona-voice answer]

---

**Labeled moments for [Subject Name]:**

For each notable moment, apply exactly one label:

- `SURPRISING (expected: [from expectation register], got: [from actual answer])`
- `CONFIRMING (validates: [specific expectation from register])`
- `INCONCLUSIVE: [name the ambiguity — why it fits neither category cleanly]`

At least one label per subject is required. Do not label every moment SURPRISING or CONFIRMING
without acknowledging any ambiguity — use INCONCLUSIVE where the evidence resists clean
classification.

---

**Evidence Table for [Subject Name]:**

| ID | Evidence item | Signal type | Strength | Rationale | Basis |
|----|---------------|-------------|----------|-----------|-------|
| E-[N.1] | [Specific insight, concern, req, contradiction, or signal] | [adoption risk / feasibility concern / requirement gap / scope signal / constraint] | strong / moderate / weak | [why this rating — one sentence] | verbatim / inferred / corroborated |

Minimum 1 evidence item per subject.

---

### PHASE 2 GATE — do not begin synthesis until ALL items pass for EVERY subject:

- [ ] Each subject's answers use at least one vocabulary signature term
- [ ] Each subject has at least one labeled moment (SURPRISING, CONFIRMING, or INCONCLUSIVE)
      with an explicit expectation link
- [ ] Each evidence item has: signal type, strength + rationale, basis declaration
- [ ] At least one Q2 or Q3 is explicitly triggered by a prior answer (trigger phrase quoted)
- [ ] Phase criterion ownership: this phase satisfies C-03, C-04, C-05, C-06, C-07, C-08,
      C-12, C-14, C-16, C-17, C-18

---

## PHASE 3 — Cross-Interview Synthesis

**Composite pattern:**
[Name the dominant pattern across subjects — convergence, contradiction, or cascade.]

**Contradictions and agreements:**
[Where subjects diverged — name the specific claim each held and why they diverged.]

**Objection lifecycle:**

If a skeptic subject was present:
- Initial objection: [state it verbatim or paraphrase closely]
- Trace its movement: [which subsequent subjects reinforced / reframed / challenged it]
- Final state: PERSISTED / TRANSFORMED → [name what changed] / RESOLVED → [name what closed it]

An assertion that subjects "agreed" or "disagreed" without tracing the objection's movement
across subjects fails this criterion.

**Composite signal for topic narrative:**
[Single paragraph connecting individual evidence items into an actionable composite signal.]

### PHASE 3 GATE:

- [ ] Synthesis names at least one pattern, convergence, or contradiction
- [ ] If a skeptic was present: objection lifecycle declares PERSISTED / TRANSFORMED / RESOLVED
      with trace evidence
- [ ] Composite signal connects evidence to a topic narrative conclusion
- [ ] Phase criterion ownership: this phase satisfies C-09, C-21

---

## PHASE 4 — Fidelity and Voice Audit

**Simulation fidelity note:**
- Grounded: [at least one claim traceable to documented domain context or role conventions]
- Constructed plausibility: [at least one element built from role logic but not directly sourced]

**Voice divergence observation:**
Name one concrete contrast between two subjects:
> "[Subject A] used '[term or phrase]' to frame [concern]; [Subject B] framed the same concern
> as '[different term or phrase]' — this reflects [role difference or priority difference]."

Generic role labels ("they had different backgrounds") without citing a specific term fail.

### PHASE 4 GATE:

- [ ] Fidelity note names at least one grounded and one constructed element
- [ ] Voice divergence observation cites a specific term or phrase from each subject
- [ ] Phase criterion ownership: this phase satisfies C-10, C-11

---

## Execution

Topic for this run: `{topic}`
Default to 2–3 subjects unless otherwise specified.
Embed all format templates as shown — the template is the contract, not metadata.
```

---

---

## V-03: Output Format (Table-First Setup)

**Axis:** Output format — subject setup is entirely table-driven; interviews are prose; evidence is structured
**Hypothesis:** Tables for the pre-interview setup force vocabulary signatures, expectation registers, and evidence columns to be populated before any transcript begins, making C-13, C-22, C-08, C-17, and C-18 spot-checkable without prose interpretation.

---

```markdown
# prove-interview — Stakeholder Interview Simulation

Simulate interviews with stakeholders or customers about `{topic}`. The simulation is grounded
in each persona's role, documented knowledge, and concerns. Answers must sound like that specific
person — not a generic representative of their category.

Output is organized in four tables and a transcript block. Fill all tables before writing any
interview content.

---

## TABLE 1 — Subject Registry

Fill completely before any interview begins.

| # | Name / Title | Disposition | Interview position | Sequence rationale |
|---|--------------|-------------|--------------------|--------------------|
| S1 | [Role or title] | skeptic / advocate / neutral / gatekeeper | 1st / 2nd / 3rd | [Why this subject appears here in the sequence] |
| S2 | … | … | … | … |
| S3 | … | … | … | … |

**Minimum requirements:** 2 subjects, meaningfully different roles, sequence rationale populated.

---

## TABLE 2 — Subject Setup Cards

One row per subject. Fill all columns. This table is the spot-check mechanism for C-03 and C-22.

| Subject | Prior knowledge (knows) | Blind spots | Cares about | Vocabulary term 1 | Vocabulary term 2 | Vocabulary term 3 |
|---------|------------------------|-------------|-------------|-------------------|-------------------|-------------------|
| S1 | … | … | … | [exact term] | [exact term] | [optional] |
| S2 | … | … | … | [exact term] | [exact term] | [optional] |

**Vocabulary contract:** Any answer from a subject that uses none of that subject's declared
vocabulary terms is suspect and should be revised. The terms must be role-specific — not generic
descriptors.

---

## TABLE 3 — Pre-Interview Expectation Register

Declare what you expect from each subject before any transcript begins.
SURPRISING / CONFIRMING labels in the transcript will reference this table by row.

| Subject | Expected claim | Expected miss | Expected objection (if skeptic) |
|---------|---------------|---------------|----------------------------------|
| S1 | [Specific claim you predict they'll make] | [Something they'll likely overlook] | [If skeptic: the specific objection] |
| S2 | … | … | … |

---

## INTERVIEWS

Write one interview block per subject, in the sequence declared in Table 1.

---

### Interview — [Subject N]: [Title]

*Subject is [N] of [total]. [One sentence reminding why they appear at this position.]*

**Q1:** [Question anchored to this subject's declared prior knowledge from Table 2]

> **[Subject]:** [Persona-voice answer. Must use at least one term from Table 2 vocabulary
> columns. Must reflect this subject's specific concerns and blind spots, not generic expertise.]

**Q2:** triggered by: "[exact phrase from Q1 answer]"

> **[Subject]:** [Persona-voice answer]

**Q3:** [Third question — new thread or deeper follow-up]

> **[Subject]:** [Persona-voice answer]

**Labeled moments:**

```
SURPRISING (expected: [row from Table 3], got: [what the answer actually said])
   — or —
CONFIRMING (validates: [row from Table 3])
   — or —
INCONCLUSIVE: [name the ambiguity]
```

Apply at least one label per subject. Use INCONCLUSIVE rather than forcing a moment into
SURPRISING or CONFIRMING when the evidence genuinely resists classification.

---

*(Repeat interview block for each additional subject)*

---

## TABLE 4 — Evidence Registry

Populate after all interviews are complete. One row per evidence item.

| ID | Subject | Evidence item | Signal type | Strength | Strength rationale | Basis |
|----|---------|---------------|-------------|----------|--------------------|-------|
| E-1.1 | S1 | [Specific insight, concern, requirement, contradiction, or signal] | adoption risk / feasibility concern / requirement gap / scope signal / constraint | strong / moderate / weak | [Why this rating — one sentence] | verbatim / inferred / corroborated |
| E-1.2 | S1 | … | … | … | … | … |
| E-2.1 | S2 | … | … | … | … | … |

**Minimum:** 1 evidence item per subject. All seven columns required per row.

---

## SYNTHESIS

**Pattern observation:**
[Name the dominant pattern across subjects — convergence, contradiction, or cascade. Not a
per-subject summary — an observation about their relationship to each other.]

**Objection lifecycle (required when a skeptic subject is present):**

> Initial objection (S[N], [their exact objection]):
> Movement: [how subsequent subjects reinforced, reframed, or challenged it]
> Final state: **PERSISTED** / **TRANSFORMED** → [what changed] / **RESOLVED** → [what closed it]

**Composite signal:**
[Connect evidence rows from Table 4 into a topic-narrative signal. Reference evidence IDs.]

---

## FIDELITY AND VOICE AUDIT

**Simulation fidelity:**
- Grounded: [specific claim traceable to domain context or role conventions]
- Constructed: [element built from role logic, not directly sourced]

**Voice divergence:**
> [Subject A] used "[exact term from their vocabulary]" to frame [concern].
> [Subject B] framed the same concern as "[their term]" — reflecting [role/priority difference].

---

## Execution notes

- Topic: `{topic}`
- All four tables must be complete before any interview transcript begins
- Vocabulary terms in Table 2 are the spot-check contract for C-03
- Evidence rows in Table 4 must have all seven columns — partial rows fail
```

---

---

## V-04: Combined (Role Sequence + Inertia Framing)

**Axes:** Role sequence (skeptic = status-quo/incumbent defender, runs first) + inertia framing (one subject explicitly represents the existing solution or competitor position)
**Hypothesis:** Grounding the skeptic in a concrete inertia position — defending an existing tool, workflow, or competitor approach — makes their vocabulary signature specific and their objection traceable, producing a richer lifecycle arc (C-21) and a natural fidelity basis (C-10).

---

```markdown
# prove-interview — Stakeholder Interview Simulation

Simulate interviews about `{topic}` with stakeholders or customers who hold different
relationships to the *status quo* — the existing tools, workflows, or approaches that the
topic would change or replace.

The key structural principle: one subject represents **inertia** — the person whose current
solution is working well enough and who has the most to lose from change. That subject
interviews first. Their objection becomes the narrative thread that all subsequent subjects
either reinforce, reframe, or resolve.

---

## STEP 1 — Status Quo Mapping

Before declaring subjects, name the status quo:

```
Current solution / incumbent: [What exists today — tool, workflow, process, or approach]
Who it serves well: [Which roles benefit from it as-is]
Who it serves poorly: [Which roles are underserved or constrained by it]
What would change: [What the topic would displace or transform]
```

This mapping determines which subject holds the inertia position and which subjects have
motivation to change.

---

## STEP 2 — Subject Declarations

Declare all subjects before any interview begins. The inertia holder must be Subject 1.

For each subject, complete the following:

```
### Subject [N]: [Role / Title]

Status-quo relationship: [inertia holder / change driver / neutral evaluator / technical gatekeeper]

Vocabulary Signature:
  • [Term 1 — specific to this role's relationship with the current solution]
  • [Term 2 — specific to how this role describes the problem space]
  • [Term 3 — optional but preferred]

Prior Knowledge:
  Knows: [What this subject understands about the current solution and the topic]
  Blind spots: [What they likely underestimate or haven't considered]
  Cares about: [Their primary concern — stability, efficiency, risk, adoption, cost, other]

Disposition toward change: [resistant / cautiously open / eager / pragmatic / other]

Pre-Interview Expectations:
  They will likely defend: [specific aspect of the status quo they'll protect]
  They will likely miss: [something the new approach offers that they haven't seen yet]
  Their core objection: [state the objection you predict — this becomes the tracked objection]
```

**Sequence rationale:**
> Subject 1 ([inertia holder]) opens because their objection, at maximum strength, sets the
> stakes for every subsequent interview. [Add one sentence per remaining transition explaining
> why subjects follow in the declared order.]

---

## STEP 3 — Interviews

Run one interview per subject in declared sequence.

---

### Interview — Subject [N]: [Title]
*[Their status-quo relationship] — interview [N] of [total]*
*Sequence position: [one sentence on why they appear here]*

**Q1:** [Opening question that engages this subject's specific relationship to the status quo]

> **[Subject]:** [Persona-voice answer. Must use at least one vocabulary signature term.
> The answer should reflect how this subject's status-quo relationship shapes their
> perception — the inertia holder defends, the change driver criticizes, the neutral
> evaluator weighs. A generic answer fails.]

**Q2:** triggered by: "[exact phrase from Q1 that raised a thread worth following]"

> **[Subject]:** [Persona-voice answer]

**Q3:** [Third question — probe their relationship to the status quo's limitations or strengths]

> **[Subject]:** [Persona-voice answer]

---

**Labeled moments:**

- `SURPRISING (expected: [from pre-interview expectation], got: [from actual answer])`
- `CONFIRMING (validates: [from pre-interview expectation])`
- `INCONCLUSIVE: [moment that fits neither — name the ambiguity]`

At least one label per subject. The inertia holder's labeled moment is the starting point
for the objection lifecycle in synthesis.

---

**Evidence extracted:**

| ID | Item | Signal type | Strength | Rationale | Basis |
|----|------|-------------|----------|-----------|-------|
| E-[N.1] | [Specific evidence item] | [adoption risk / feasibility concern / requirement gap / scope signal / constraint / inertia signal] | strong / moderate / weak | [why this rating] | verbatim / inferred / corroborated |

Add `inertia signal` as a valid signal type — use it when evidence reflects the gravitational
pull of the existing solution rather than a specific technical or adoption concern.

---

*(Repeat for each additional subject)*

---

## STEP 4 — Cross-Interview Synthesis

**Status-quo narrative arc:**
Trace what happened to the existing solution's position across the interview sequence:
> At the start, the status quo was defended as: [inertia holder's position]
> By the end, the status quo appeared: [stronger / weaker / reframed / still contested]

**Objection lifecycle (required):**
> Subject 1's core objection: "[state it]"
> — Subject 2's response: [reinforced / reframed / challenged] because [specific claim]
> — Subject 3's response: [reinforced / reframed / challenged] because [specific claim]
> Final state: **PERSISTED** / **TRANSFORMED** → [what changed and why] / **RESOLVED** → [what closed it]

Do not summarize each subject's position as independent findings. Trace the objection's movement
as a single thread through the sequence.

**Composite signal:**
[One paragraph connecting evidence items into a signal about the topic's viability given the
status-quo landscape. Reference specific evidence IDs.]

---

## STEP 5 — Fidelity and Voice Audit

**Simulation fidelity:**
> Grounded claim: [cite a specific role convention, domain norm, or documented context that
> makes this subject's position realistic]
> Constructed plausibility: [identify one element built from role logic rather than direct source]
> Status-quo specificity: [name the current tool, workflow, or approach that grounded the
> inertia holder's vocabulary — this is the primary fidelity anchor for this variation]

**Voice divergence:**
> [Inertia holder] used "[term from vocabulary signature]" to characterize [X].
> [Change driver or other subject] used "[their term]" for the same [X].
> The contrast reflects [their different relationships to the current solution].

---

## Execution notes

- Topic: `{topic}`
- The inertia holder must be Subject 1 — this is not optional in this variation
- `inertia signal` is a valid evidence signal type specific to this framing
- The objection lifecycle trace in synthesis is required whenever an inertia holder is present
  (which is by design in all runs of this variation)
- Default to 2–3 subjects unless the topic specifies otherwise
```

---

---

## V-05: Combined (Phrasing Register + Lifecycle Emphasis)

**Axes:** Phrasing register (conversational, second-person imperative) + lifecycle emphasis (compressed phases with embedded templates, directive language)
**Hypothesis:** Second-person directives ("Before you write a single answer, do this") with inline format templates cause essential and recommended criteria to be met habitually rather than by deliberate structural awareness — reducing the friction cost of compliance.

---

```markdown
# prove-interview — Stakeholder Interview Simulation

You're going to simulate a set of stakeholder or customer interviews about `{topic}`.

These interviews aren't real — they're grounded simulations. Your job is to make each person
sound like *themselves*, not like a generic representative of their job title. That's the
whole game. Everything else serves that goal.

Here's how to do it well.

---

## Before you write a single answer — set up your subjects

Don't start the interview. Not yet.

For each person you're going to interview, fill in this card:

```
Who they are: [Role or title — explicit. "a senior engineer" not "a technical stakeholder."]

Their vocabulary (this is the spot-check):
  • [Word or phrase this specific person would use that a generic answer wouldn't]
  • [Another one]
  • [Third one, optional]

What they already know: [Their actual familiarity with the topic — not their job description]
What they don't know: [The blind spot most relevant to this topic]
What they care about: [The one or two things driving their questions and concerns]
Their disposition: [skeptic / advocate / neutral / gatekeeper / something else — name it]

What you expect them to say: [A specific prediction]
What you expect them to miss: [Another specific prediction]
What you expect them to push back on: [If they're a skeptic: name the exact objection]
```

Do this for every subject. All cards must be complete before the first question is asked.

Also: decide the interview order *before* you start, and say why in one sentence per transition.
If you're not sure, put the most skeptical person first — their objection becomes the thread
everything else responds to.

---

## For each interview

Start with a reminder of where this person sits in the sequence and why they're here now.

Then run the interview like this:

**Ask a first question** that engages what this specific person knows and cares about.
A question that could be asked of anyone isn't doing its job.

**Let them answer** — in their voice. If any word from their vocabulary signature doesn't show
up at least once in their answers, go back and fix it. The signature is the contract.

**Ask a follow-up** — and say what triggered it. The format is:

> triggered by: "[exact phrase from their last answer]"

If your follow-up could appear in any order, it's not a real follow-up. Real follow-ups are
locked to a specific moment.

**Ask a third question** — either deepen the thread or open a new one relevant to their concerns.

After the transcript for this person, do two things:

**Label the moment that stands out:**
Pick the most notable moment and label it exactly like this:
```
SURPRISING (expected: [what your pre-interview card predicted], got: [what they actually said])
```
or:
```
CONFIRMING (validates: [which prediction it confirmed])
```
or:
```
INCONCLUSIVE: [name what made it ambiguous — why it didn't land cleanly in either category]
```

Don't force everything into SURPRISING or CONFIRMING. If a moment genuinely resists
classification, INCONCLUSIVE is the honest call.

**Extract what you learned:**

| # | What you learned | What kind of signal is it | How strong | Why that rating | Where it came from |
|---|-----------------|--------------------------|------------|-----------------|-------------------|
| E-[N.1] | [Concrete insight, concern, requirement, or contradiction] | adoption risk / feasibility concern / requirement gap / scope signal / constraint | strong / moderate / weak | [one sentence on why] | verbatim / inferred / corroborated |

Minimum one row per person. All columns required.

---

## After all the interviews — synthesize

Now you've heard from everyone. Write one synthesis section.

**The pattern:** What did you actually learn across the group? Name a convergence, a contradiction,
or a cascade — not a list of each person's position.

**The objection arc** (required if any subject was a skeptic):

Walk through what happened to their core objection step by step:
> They started with: "[the objection]"
> Subject 2 responded by: [reinforcing it / reframing it / challenging it] — because [specific claim]
> Subject 3 responded by: [same structure]
> Where it ended: PERSISTED / TRANSFORMED (what changed: [name it]) / RESOLVED (what closed it: [name it])

Don't say they "agreed" or "disagreed" without showing the movement.

**The composite signal:** What does all of this mean for the topic? One paragraph. Reference
specific evidence items by their IDs.

---

## One last thing — the fidelity check

Before you're done, write two to four sentences covering:

1. One claim in these interviews that's grounded — based on something you know about this
   domain, these roles, or this type of decision.
2. One thing you constructed from role logic rather than direct knowledge — where you built
   plausibility without a source.
3. One concrete way two of your subjects sound different from each other. Not "they had different
   roles" — name an actual word or phrase each one used that the other wouldn't.

That third one is the proof that you were managing voice intentionally.

---

## The essentials

- Topic: `{topic}`
- Minimum 2 subjects with meaningfully different roles
- All subject cards must be complete before any transcript starts
- Vocabulary signature is the spot-check — if an answer never uses any of their terms, revise it
- The SURPRISING/CONFIRMING/INCONCLUSIVE format above is the required form — not optional style
- The objection arc in synthesis is required whenever a skeptic subject is present
```

---

## Variation Summary

| # | Axis | Core bet | Primary criteria targeted |
|---|------|----------|--------------------------|
| V-01 | Role sequence (skeptic-first) | Skeptic-first ordering makes C-21 a natural narrative spine | C-19, C-21, C-09, C-13 |
| V-02 | Lifecycle emphasis (explicit gates) | Gate checklists prevent essential criteria from being skipped | C-15, C-20, C-01–C-05 |
| V-03 | Output format (table-first setup) | Tables force C-13/C-22/C-08/C-17/C-18 to be column-complete before transcript | C-22, C-13, C-08, C-17, C-18 |
| V-04 | Role sequence + inertia framing | Grounding skeptic in status-quo position makes vocabulary specific and lifecycle traceable | C-21, C-22, C-10, C-19 |
| V-05 | Phrasing register + lifecycle emphasis | Second-person directives + inline templates reduce compliance friction | C-03, C-05, C-12, C-16, C-11 |
