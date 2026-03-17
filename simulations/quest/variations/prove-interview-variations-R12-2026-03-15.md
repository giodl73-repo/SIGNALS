# prove-interview Variations — Round 12 (V-01 through V-05)

---

## V-01 — Single Axis: Role Sequence (Skeptic-First Ordering)

**Hypothesis**: Leading with the skeptic surfaces objections before advocates can frame the narrative, and makes the objection lifecycle (C-21) structurally visible because every subsequent interview is measured against the opening challenge.

---

```markdown
Simulate a set of stakeholder interviews about {{topic}}. Run the interviews in
skeptic-first order: the most resistant or challenge-prone subject interviews first,
followed by practitioners, then advocates last. This ordering is deliberate — name
it explicitly in a one-sentence sequence justification before the first interview.

---

## SETUP PHASE

### Document-Head Format Contract
All phase gates use the named checklist block format:
  PHASE N GATE: [ ] item one  [ ] item two  ...
All evidence tables carry these columns:
  Evidence Item | Signal Type | Strength (strong/moderate/weak) | Origin-of-Claim
  (verbatim/inferred/corroborated) | Experience-Proximity (GROUNDED/CONDITIONAL/INFERRED)
This contract applies uniformly to every gate block and every evidence table in this document.

### Moment-Label Decision Taxonomy (declared before any transcript)
| Label | Applies When |
|-------|-------------|
| SURPRISING | A prior expectation from the Expectation Register is violated by the subject's answer |
| CONFIRMING | A prior expectation from the Expectation Register is upheld by the subject's answer |
| INCONCLUSIVE | A signal is present but directionally ambiguous — cannot be assigned to either category |
This taxonomy governs all labeled moments. Use all three labels as needed; note explicitly
if every moment is unambiguously one or the other.

### Subject Sequence Justification
[One sentence naming why subjects run in the declared order — what the ordering accomplishes
for the evidence structure.]

### Subject Cards

**Subject A — [Role / Title]**
- Prior knowledge: [what they know, what they've experienced firsthand]
- Blind spots: [what they haven't encountered or reasoned about only abstractly]
- Disposition: [skeptic / neutral / advocate — name it]
- Evidential function: [what this subject's position in the sequence does for the evidence
  chain — e.g., "establishes the primary objection surface that subsequent interviews address"]
- Vocabulary signature (2–3 specific terms this persona uses):
  - Term 1: [exact term or phrase]
  - Term 2: [exact term or phrase]
  - Term 3: [exact term or phrase, optional]
- Experience-proximity: GROUNDED / CONDITIONAL / INFERRED [choose one; brief rationale]

**Subject B — [Role / Title]**
[same fields as Subject A]

**Subject C — [Role / Title]** *(add as needed)*
[same fields]

### Expectation Register
*Populated before any transcript begins. Names what the interviewer expects each subject
to say and why. The extraction phase draws SURPRISING/CONFIRMING labels from this register.*

| Subject | Expected to say | Reason for expectation |
|---------|-----------------|------------------------|
| A | [expected statement] | [why] |
| B | [expected statement] | [why] |
| C | [expected statement, if applicable] | [why] |

### Pre-Interview Master Gate
Confirms all structural prerequisites are collectively satisfied before Phase 1 begins.
Draws from named sub-gate completions above.

PRE-INTERVIEW MASTER GATE:
[ ] Subject Cards complete — role, prior knowledge, disposition, evidential function,
    vocabulary signature (2–3 terms), experience-proximity declared for all subjects
[ ] Expectation Register populated — at least one row per subject, declared before transcripts
[ ] Vocabulary signatures declared for all subjects (Section: Subject Cards)
[ ] Moment-label decision taxonomy declared — SURPRISING / CONFIRMING / INCONCLUSIVE
    with decision rules for all three labels (Section: Moment-Label Decision Taxonomy)
[ ] Sequence justification present — one sentence explaining skeptic-first ordering

---

## INTERVIEW PHASE

*Run interviews in the declared sequence. Subject A (skeptic) first.*

### Interview — Subject A: [Role]

**Questions:**
1. [Opening question anchored to Subject A's declared concerns]
2. [Follow-up triggered by Subject A's answer to Q1 — quote or point to the exact phrase
   that prompted this question: triggered by: "[exact phrase]"]
3. [Continue as needed]

**Transcript:**
[Subject A answers in their declared voice. Vocabulary signature terms must appear
naturally at least once. Write answers using the specific vocabulary, framing preferences,
and concern priorities that distinguish this persona from others.]

**Moment Labels:**
- [Label: SURPRISING / CONFIRMING / INCONCLUSIVE]
  (expected: [Expectation Register → Subject A row, "Expected to say" field], got: [what emerged])
  *C-22 vocabulary confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE (item 1).*
  *C-13 register confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE (item 2).*

**Evidence Extraction — Subject A:**
| Evidence Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity |
|--------------|-------------|----------|-------------------|-----------------|---------------------|
| [item] | [adoption risk / feasibility concern / requirement gap / scope signal / constraint] | strong/moderate/weak | [why this rating] | verbatim/inferred/corroborated | GROUNDED/CONDITIONAL/INFERRED |

PHASE 1 GATE (Subject A):
[ ] Role, prior knowledge, disposition declared before transcript
[ ] At least one question anchored to declared concerns
[ ] At least one follow-up with triggered-by citation
[ ] Vocabulary signature exercised (at least one term appeared in transcript)
[ ] At least one moment labeled SURPRISING, CONFIRMING, or INCONCLUSIVE with register citation
[ ] Evidence table populated with all required columns

---

### Interview — Subject B: [Role]
[Same structure as Subject A. Note any cross-reference to Subject A's objection —
does Subject B's testimony address, reinforce, or sidestep the skeptic's challenge?]

PHASE 2 GATE (Subject B):
[ ] [same checklist as Phase 1]
[ ] Cross-reference to Subject A's objection noted (if applicable)

---

### Interview — Subject C: [Role] *(if present)*
[Same structure.]

PHASE 3 GATE (Subject C):
[ ] [same checklist as Phase 1]

---

## SYNTHESIS PHASE

### Objection Lifecycle
*Track Subject A's initial objection across the full sequence.*

Subject A raised: [state the objection].
By the final interview, this objection: persisted / transformed / was resolved.
Evidence trail: [name which interviews moved the objection, in what direction, and why].

### Cross-Interview Synthesis Artifact

| Subject | Framework Dimension | Testimony Direction | Implication |
|---------|--------------------|--------------------|-|
| A | [dimension from prior knowledge map] | supports / challenges / inconclusive | [what this means downstream] |
| B | [dimension] | supports / challenges / inconclusive | [implication] |
| C | [dimension] | supports / challenges / inconclusive | [implication] |

*Epistemic weight note: Name at least one item where experience-proximity adjusts synthesis
weight — e.g., "Subject A's objection is CONDITIONAL; they have not yet encountered the
alternative. Treat as a risk to monitor, not a blocker."*

### Simulation Fidelity Note
[Brief meta-note distinguishing grounded claims from constructed plausibility. Name at
least one specific basis — e.g., "Subject A's pricing concern is grounded in documented
enterprise procurement friction. Subject C's adoption timeline is constructed plausibility
based on comparable rollout patterns."]

### Voice Divergence Observation
[Name at least one concrete contrast in how two subjects sound different — cite a specific
vocabulary choice, framing preference, or concern priority. Generic statements about role
differences do not count.]
```

---

## V-02 — Single Axis: Output Format (Schema-Heavy Tables Throughout)

**Hypothesis**: Delivering every structural element as a named table — subject cards, registers, evidence, synthesis — makes each criterion independently auditable without parsing prose, and makes schema-instantiation (C-29) a natural consequence of the format rather than an add-on.

---

```markdown
Simulate stakeholder or customer interviews about {{topic}}. Every structural
element — setup, questions, evidence, synthesis — is delivered as a named table
or named schema block. No criterion is satisfied through prose narrative alone
when a table can carry it.

---

## SECTION 0: DOCUMENT SCHEMA CONTRACT

The following table schemas are in force for this entire document.

**Subject Card Schema:**
| Field | Required | Notes |
|-------|----------|-------|
| Role / Title | YES | Specific, not generic |
| Prior Knowledge | YES | What they know from direct experience |
| Blind Spots | YES | What they have not encountered |
| Disposition | YES | skeptic / neutral / advocate |
| Evidential Function | YES | Structural contribution to evidence chain |
| Vocabulary Signature | YES | 2–3 exact terms or phrases |
| Experience-Proximity | YES | GROUNDED / CONDITIONAL / INFERRED + one-sentence rationale |

**Expectation Register Schema:**
| Subject | Expected Claim | Basis for Expectation |

**Evidence Table Schema:**
| Evidence Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity | Framework Dimension |

**Moment Label Format (inline):**
  [SURPRISING / CONFIRMING / INCONCLUSIVE]
  (expected: [Expectation Register → Subject X → "Expected Claim" field], got: [actual])

**Synthesis Artifact Schema:**
| Subject | Framework Dimension | Testimony Direction | Epistemic Weight Adjustment | Implication |

*Instantiated examples for each schema appear at their first point of use.*

---

## SECTION 1: SUBJECT CARDS

*One row per subject. The table schema above applies. This section constitutes Sub-Gate 1.*

| Subject ID | Role / Title | Prior Knowledge | Blind Spots | Disposition | Evidential Function | Vocabulary Sig. (term 1, term 2, term 3) | Experience-Proximity |
|------------|-------------|-----------------|-------------|-------------|--------------------|-----------------------------------------|---------------------|
| A | [role] | [knowledge] | [blind spots] | [disposition] | [function in evidence chain] | [term], [term], [term] | [GROUNDED/COND/INF] — [rationale] |
| B | [role] | [knowledge] | [blind spots] | [disposition] | [function] | [term], [term], [term] | [GROUNDED/COND/INF] — [rationale] |

SUB-GATE 1 — Subject Cards:
[ ] All required schema fields populated for every subject
[ ] Vocabulary signature: 2–3 specific terms (not trait descriptions) per subject
[ ] Evidential function distinguishes structural role from mere description

---

## SECTION 2: MOMENT-LABEL DECISION TAXONOMY

| Label | Decision Rule |
|-------|--------------|
| SURPRISING | Prior expectation (from Expectation Register) is violated by subject's answer |
| CONFIRMING | Prior expectation (from Expectation Register) is upheld by subject's answer |
| INCONCLUSIVE | Signal present; directionally ambiguous; cannot assign to either prior-expectation category |

SUB-GATE 2 — Moment-Label Taxonomy:
[ ] All three labels declared with decision rules
[ ] INCONCLUSIVE decision rule present (even if no instance appears)

---

## SECTION 3: EXPECTATION REGISTER

*Schema instantiation example (first row):*
| Subject | Expected Claim | Basis for Expectation |
|---------|---------------|----------------------|
| A (example) | "Will object to migration cost before asking about feature value" | Prior encounters with enterprise ops teams in deployment contexts |

*Populate all subjects:*
| Subject | Expected Claim | Basis for Expectation |
|---------|---------------|----------------------|
| A | [expected claim] | [basis] |
| B | [expected claim] | [basis] |

SUB-GATE 3 — Expectation Register:
[ ] One or more rows per subject
[ ] All rows populated before any transcript begins

---

## SECTION 4: SUBJECT SEQUENCE JUSTIFICATION

| Sequence | Rationale |
|----------|-----------|
| A → B [→ C] | [One sentence: why this order; what it does for the evidence structure] |

---

## PRE-INTERVIEW MASTER GATE

Evidenced closure — each item cross-references its named sub-gate.

PRE-INTERVIEW MASTER GATE:
[ ] Subject Cards complete — SUB-GATE 1: PASSED
[ ] Expectation Register populated — SUB-GATE 3: PASSED
[ ] Vocabulary signatures declared for all subjects — SUB-GATE 1 (Vocabulary Sig. column): PASSED
[ ] Moment-label decision taxonomy declared — SUB-GATE 2: PASSED
[ ] Sequence justification present — Section 4: PASSED
[ ] Document Schema Contract declared — Section 0: PASSED

---

## SECTION 5: INTERVIEWS

### Interview — Subject A: [Role]

**Question Table:**
| Q# | Question | Anchor (declared concern or prior answer) |
|----|---------|------------------------------------------|
| Q1 | [question] | [Subject A prior knowledge: specific item] |
| Q2 | [follow-up question] | triggered by: "[exact phrase from A's answer to Q1]" |

**Transcript:**
[Subject A's answers. Vocabulary signature terms must appear at least once.
Write in this subject's declared voice — vocabulary, concerns, framing.]

**Moment Label Table:**
| Moment Summary | Label | Expected (→ Register) | Actual | Expectation Register Authorization |
|---------------|-------|----------------------|--------|-------------------------------------|
| [brief summary] | SURPRISING/CONFIRMING/INCONCLUSIVE | [Register → Subject A "Expected Claim"] | [what emerged] | C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE |

**Evidence Table (Subject A):**

*Schema instantiation example (first evidence item for Subject A):*
| Evidence Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity | Framework Dimension |
|--------------|-------------|----------|-------------------|-----------------|---------------------|---------------------|
| Example: "Migration cost front-loaded before value discussion" | adoption risk | strong | Verbatim quote; subject has direct procurement authority | verbatim | GROUNDED — subject has signed 3 enterprise migration contracts | Prior Knowledge: cost sensitivity |

*All evidence items for Subject A:*
| Evidence Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity | Framework Dimension |
|--------------|-------------|----------|-------------------|-----------------|---------------------|---------------------|
| [item 1] | [type] | [rating] | [rationale] | [origin] | [proximity] | [framework dim.] |
| [item 2] | [type] | [rating] | [rationale] | [origin] | [proximity] | [framework dim.] |

*C-22 vocabulary exercise check: [list which declared terms appeared in transcript — cite
the PRE-INTERVIEW MASTER GATE as authorization authority for C-22 being fully satisfied.]*

PHASE 1 GATE — Subject A Interview:
[ ] Q table populated; at least one follow-up with triggered-by citation
[ ] Transcript written in declared persona voice; vocabulary terms exercised
[ ] Moment Label Table: all columns populated; Register citation present
[ ] Evidence Table: all schema columns populated; at least one row

---

### Interview — Subject B: [Role]

[Same table structure as Subject A. Include cross-interview observation: does Subject B
address, reinforce, or sidestep Subject A's signaled concerns?]

**Cross-Interview Observation:**
| From Subject | Concern Raised | Subject B's Response | Direction |
|-------------|---------------|---------------------|-----------|
| A | [concern] | [what B said] | addresses / reinforces / sidesteps |

PHASE 2 GATE — Subject B Interview:
[ ] [same checklist as Phase 1]
[ ] Cross-interview observation table populated

---

## SECTION 6: SYNTHESIS

### Objection Lifecycle Table *(N/A if no skeptic subject)*
| Subject | Initial Objection | Fate (persisted/transformed/resolved) | Evidence Trail |
|---------|------------------|--------------------------------------|----------------|
| A | [objection] | [fate] | [which interviews moved it and how] |

### Cross-Interview Synthesis Artifact

*Schema instantiation — first row as example:*
| Subject | Framework Dimension | Testimony Direction | Epistemic Weight Adjustment | Implication |
|---------|--------------------|--------------------|-----------------------------|-------------|
| A (ex.) | Cost sensitivity | challenges | CONDITIONAL — has not used the alternative; treat as risk, not blocker | Budget objection requires pre-sales cost modeling |

*All subjects:*
| Subject | Framework Dimension | Testimony Direction | Epistemic Weight Adjustment | Implication |
|---------|--------------------|--------------------|-----------------------------|-------------|
| A | [dim.] | supports/challenges/inconclusive | [adjustment or "none — GROUNDED"] | [implication] |
| B | [dim.] | supports/challenges/inconclusive | [adjustment] | [implication] |

### Simulation Fidelity Table
| Claim | Type (grounded/constructed) | Basis |
|-------|---------------------------|-------|
| [claim 1] | grounded | [specific documented source or domain context] |
| [claim 2] | constructed | [comparable pattern used as basis] |

### Voice Divergence Table
| Subject Pair | Vocabulary Contrast | Framing Contrast | Concern Priority Contrast |
|-------------|--------------------|-----------------|-----------------------------|
| A vs B | [specific term A uses vs term B uses] | [how A frames vs how B frames] | [what A prioritizes vs what B prioritizes] |
```

---

## V-03 — Single Axis: Lifecycle Emphasis (Explicit Phase Gates as Named Checklist Blocks)

**Hypothesis**: Making phase completion gating the structural spine of the prompt — with every phase ending in an unambiguous named checklist block — removes authorial discretion about when a phase is "done" and makes criterion coverage auditable at each transition point.

---

```markdown
Simulate stakeholder or customer interviews about {{topic}}. This prompt is
structured as a phased process: each phase has a named gate that must be
cleared before the next phase begins. Gate items enumerate the rubric concerns
that phase satisfies. No phase skips its gate.

---

## DOCUMENT-HEAD FORMAT CONTRACT

Rule 1 (Gate Format): Every phase gate is a named checklist block in this form:
  ╔═ GATE: [Phase Name] ═╗
  [ ] item one
  [ ] item two
  ╚══════════════════════╝

Rule 2 (Evidence Format): Every evidence table carries columns:
  Evidence Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity

Rule 3 (Moment Label Format — self-replicating template):
  [LABEL] (expected: [Register → Subject X "Expected Claim"], got: [actual])
  where LABEL ∈ {SURPRISING, CONFIRMING, INCONCLUSIVE}
  *C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE before this template activates.*

Rule 4 (Follow-up Citation Format): triggered by: "[exact phrase from prior answer]"

These rules are declared once here and apply to every occurrence throughout.

---

## PHASE 0: TAXONOMY DECLARATION

### Moment-Label Decision Taxonomy
| Label | Decision Rule | Applies When |
|-------|--------------|-------------|
| SURPRISING | Prior expectation violated | Subject's answer diverges from Register entry |
| CONFIRMING | Prior expectation upheld | Subject's answer matches Register entry |
| INCONCLUSIVE | Signal present, direction ambiguous | Cannot assign to SURPRISING or CONFIRMING |

╔═ GATE: Phase 0 — Taxonomy Declaration ═╗
[ ] All three labels declared with explicit decision rules
[ ] INCONCLUSIVE decision rule present (tests governance, not occurrence)
╚═════════════════════════════════════════╝

---

## PHASE 1: SUBJECT CARDS

*One card per subject. Vocabulary signatures are auditable contracts — name exact terms.*

**Subject A — [Role / Title]**
- Prior knowledge: [what they know from direct experience]
- Blind spots: [what they have not encountered directly]
- Disposition: skeptic / neutral / advocate
- Evidential function: [structural contribution to evidence chain — not just "the skeptic"]
- Vocabulary signature:
  - [exact term 1]: [brief note on when/why this persona uses it]
  - [exact term 2]: [note]
  - [exact term 3 (optional)]: [note]
- Experience-proximity: GROUNDED / CONDITIONAL / INFERRED — [one sentence rationale]

**Subject B — [Role / Title]**
[same fields]

**Subject C — [Role / Title]** *(add as needed)*
[same fields]

╔═ GATE: Phase 1 — Subject Cards ═╗
[ ] Role/title declared for all subjects
[ ] Prior knowledge declared (experience-based) for all subjects
[ ] Blind spots declared for all subjects
[ ] Disposition declared for all subjects
[ ] Evidential function declared (structural, not role-restatement) for all subjects
[ ] Vocabulary signature: 2–3 exact terms (not trait descriptions) for all subjects
[ ] Experience-proximity declared with one-sentence rationale for all subjects
╚══════════════════════════════════╝

---

## PHASE 2: EXPECTATION REGISTER

*Populated entirely before any interview transcript. The SURPRISING/CONFIRMING template
(Rule 3) draws from this register — this is the "expected:" source.*

| Subject | Expected Claim | Basis for Expectation |
|---------|---------------|----------------------|
| A | [what interviewer expects A to say] | [why — prior context, role pattern, domain knowledge] |
| B | [expected claim] | [basis] |
| C | [expected claim, if applicable] | [basis] |

╔═ GATE: Phase 2 — Expectation Register ═╗
[ ] One or more rows per subject
[ ] All rows populated before Phase 4 (transcripts) begins
[ ] Basis column present and non-empty for every row
╚══════════════════════════════════════════╝

---

## PHASE 3: SEQUENCE JUSTIFICATION

Subject interview order: A → B [→ C]
Rationale: [one sentence — why this order; what it does for the evidence structure]

╔═ GATE: Phase 3 — Sequence Justification ═╗
[ ] Order declared explicitly
[ ] Rationale present (minimum one sentence)
╚════════════════════════════════════════════╝

---

## PRE-INTERVIEW MASTER GATE

Evidenced by cross-referencing named sub-gate completions:

╔═ PRE-INTERVIEW MASTER GATE ═╗
[ ] Subject Cards complete — GATE Phase 1: PASSED
[ ] Expectation Register populated — GATE Phase 2: PASSED
[ ] Vocabulary signatures declared for all subjects — GATE Phase 1, item 6: PASSED
[ ] Moment-label decision taxonomy declared — GATE Phase 0: PASSED
[ ] Sequence justification present — GATE Phase 3: PASSED
All structural prerequisites confirmed. Phase 4 (Interviews) may begin.
╚══════════════════════════════╝

---

## PHASE 4: INTERVIEWS

### Interview — Subject A: [Role]

**Questions**
Q1: [anchored to Subject A's declared prior knowledge or concern]
Q2: [follow-up] triggered by: "[exact phrase from A's Q1 answer]"
Q3: [continue as needed]

**Transcript**
*Write answers in Subject A's declared voice. Vocabulary signature terms must appear
at least once naturally within the answers.*

[A answers Q1 in their voice]

[A answers Q2 in their voice]

**Moment Labels**
[LABEL] (expected: [Register → Subject A "Expected Claim" field], got: [what emerged])
*C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE — Rule 3 template activates.*

*If a moment is INCONCLUSIVE: name the specific ambiguity preventing SURPRISING/CONFIRMING.*

**Evidence Extraction — Subject A**

| Evidence Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity |
|--------------|-------------|----------|-------------------|-----------------|---------------------|
| [item] | [type] | [rating] | [why this rating] | verbatim/inferred/corroborated | GROUNDED/CONDITIONAL/INFERRED |

*Vocabulary exercise check: [name which declared terms appeared in Subject A's answers.
C-22 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE (item 3) — this check is
a traceable pointer to that record, not a free-standing assertion.]*

╔═ GATE: Phase 4a — Subject A Interview ═╗
[ ] At least one question anchored to declared concern
[ ] At least one follow-up with triggered-by citation (Rule 4 format)
[ ] Transcript written in persona voice
[ ] Declared vocabulary terms exercised in transcript
[ ] At least one moment labeled using Rule 3 format with Register citation
[ ] Evidence table populated (all columns, at least one row)
[ ] Both taxonomy dimensions applied: Origin-of-Claim AND Experience-Proximity
╚══════════════════════════════════════════╝

---

### Interview — Subject B: [Role]

[Same structure. Include a note if Subject B's answers touch on Subject A's signals.]

╔═ GATE: Phase 4b — Subject B Interview ═╗
[ ] [same checklist as Phase 4a]
[ ] Cross-reference to Subject A's evidence noted where applicable
╚═════════════════════════════════════════╝

---

### Interview — Subject C: [Role] *(if present)*

[Same structure.]

╔═ GATE: Phase 4c — Subject C Interview ═╗
[ ] [same checklist as Phase 4a]
╚═════════════════════════════════════════╝

---

## PHASE 5: SYNTHESIS

*N/A for single-subject interviews. Proceed to Phase 6.*

### Objection Lifecycle *(if a skeptic subject is present)*
Subject A raised: [state the objection].
By the final interview, this objection: persisted / transformed / was resolved.
Evidence trail: [name which interview moved it, in what direction, why].

### Cross-Interview Synthesis Artifact

| Subject | Evidence Category | Testimony Direction | Epistemic Weight Adjustment | Implication |
|---------|--------------------|--------------------|-----------------------------|-------------|
| A | [category from prior knowledge] | supports/challenges/inconclusive | [name if CONDITIONAL/INFERRED subject; "none" if GROUNDED] | [implication] |
| B | [category] | supports/challenges/inconclusive | [adjustment or "none"] | [implication] |

╔═ GATE: Phase 5 — Synthesis ═╗
[ ] Objection lifecycle named (persisted/transformed/resolved) with evidence trail
[ ] Synthesis delivered as named artifact with schema columns
[ ] At least one epistemic weight adjustment named explicitly
╚══════════════════════════════╝

---

## PHASE 6: META-OBSERVATIONS

### Simulation Fidelity Note
[Distinguish grounded claims from constructed plausibility. Name at least one specific
basis — what documented knowledge or domain context grounds the grounded claim.]

### Voice Divergence Observation
[Name at least one concrete vocabulary, framing, or concern-priority contrast between
two subjects. Generic role-difference statements do not count.]

╔═ GATE: Phase 6 — Meta-Observations ═╗
[ ] Simulation fidelity note present with at least one named specific basis
[ ] Voice divergence observation names a specific term, phrase, or framing contrast
╚═════════════════════════════════════╝
```

---

## V-04 — Combination: Conversational Register + Prominent Inertia Framing

**Hypothesis**: A conversational register reduces the structural overhead feel while keeping criterion coverage intact; leading with the status-quo competitor as the implicit subject of the skeptic's concerns makes the inertia dimension visceral rather than abstract.

---

```markdown
Run a round of stakeholder interviews about {{topic}}. The goal is to surface
real signal about whether people will move to this, and what's standing in the
way — which usually means: what they're already using, how well it works for
them, and why switching feels risky.

Set up the interviews with care before you start talking to anyone.

---

### Before You Begin: What You Expect

Write a short Expectation Register — before any interview — naming what you
think each person is going to say and why. This is what makes the SURPRISING
and CONFIRMING labels meaningful later. Use this format:

| Person | What you expect them to say | Why you expect it |
|--------|----------------------------|------------------|
| [Name or Role] | "[specific expected claim]" | [context or prior pattern] |

Populate all subjects here, before the transcripts.

Also declare upfront how you'll label moments:
- **SURPRISING**: You expected one thing; they said something that violated that expectation.
- **CONFIRMING**: They said exactly what you expected.
- **INCONCLUSIVE**: Something interesting came out, but you can't tell if it confirms or
  surprises — name what made it ambiguous.

These three labels cover the space. Use all of them as needed.

---

### Who You're Talking To

For each person, write a short profile before their interview. Be specific:

- **Role**: What do they actually do?
- **What they know**: What have they experienced firsthand that's relevant here?
- **What they don't know yet**: Where are their blind spots — things they're reasoning
  about abstractly, not from lived experience?
- **Their relationship to the status quo**: Are they comfortable with what they have now?
  Skeptical of switching? Actively frustrated? Be honest about this — it shapes
  everything they say.
- **Why they're in this interview**: What does their position in this conversation
  *do* for the evidence? (Not just "they're a skeptic" — what does the skeptic's
  testimony give us that the advocate's doesn't?)
- **Their vocabulary**: List 2–3 specific words or phrases this person reaches for.
  Not "uses technical language" — actual terms. You'll use these in their answers.
- **How grounded they are**: GROUNDED (direct operational experience), CONDITIONAL
  (relevant experience but not this exact situation), or INFERRED (reasoning from
  analogies, no direct experience).

**Important**: Think about the order you're talking to people in, and say why.
A skeptic first? A neutral baseline first? The ordering shapes how each subsequent
interview reads against the ones before it. Name the sequence logic.

---

### Before the First Interview: Confirm You're Ready

Before you write a single transcript line, confirm:

PRE-INTERVIEW MASTER GATE:
[ ] All subject profiles complete (role, knowledge, blind spots, status-quo relationship,
    evidential function, vocabulary terms, groundedness)
[ ] Expectation Register done — one row per person, all rows above
[ ] Vocabulary listed for every subject (2–3 specific terms each)
[ ] Moment-label rules declared (SURPRISING / CONFIRMING / INCONCLUSIVE — all three)
[ ] Interview order stated with one-sentence rationale

---

### The Interviews

For each subject, run through:

**1. Questions**
Ask questions that are actually about this person — rooted in their specific concerns
and what they know (or don't). When one answer surprises you or opens something up,
follow it with a question triggered directly by what they just said.
Format follow-ups like this: *triggered by: "[exact phrase they just used]"*

**2. Their Answers**
Write in their voice. If they said "migration risk" and "replatforming budget" in their
profile, those words show up in their answers. Don't give everyone the same consultese.
The status-quo framing should come through naturally in answers from hesitant subjects —
they're not just worried about the new thing, they're implicitly defending something
that works well enough right now.

**3. Label the Moments**
For anything notable, label it using the declared format:
[SURPRISING / CONFIRMING / INCONCLUSIVE]
(expected: [Expectation Register → "[their expected claim]"], got: [what they actually said])

If a moment is INCONCLUSIVE, say what made it hard to call.

**4. Pull the Evidence**
After the transcript, extract what you learned. Use this table:

| What they said or implied | Signal type | How strong? | Why that strength? | Verbatim/inferred/corroborated? | How grounded is this person? |
|--------------------------|-------------|-------------|-------------------|---------------------------------|------------------------------|
| [evidence item] | adoption risk / feasibility concern / requirement gap / scope signal / constraint | strong / moderate / weak | [reason] | verbatim / inferred / corroborated | GROUNDED / CONDITIONAL / INFERRED |

After each interview, pause and check:

INTERVIEW GATE — [Subject Name/Role]:
[ ] Questions were anchored to their specific profile, not generic
[ ] At least one follow-up cited what they said (triggered-by format)
[ ] Answers are in their voice (vocabulary terms appeared)
[ ] At least one labeled moment with Register citation
[ ] Evidence table populated with all columns

---

### After All the Interviews

**Track the skeptic's objection** (if one was present): What did they open with?
By the end, did that objection persist, transform into something else, or get resolved?
Walk through the evidence trail that shows how it moved.

**Cross-interview synthesis — as a table:**
| Person | Main concern or signal | Their testimony direction | How grounded? | What this means |
|--------|----------------------|--------------------------|---------------|----------------|
| [A] | [concern] | supports / challenges / inconclusive | GROUNDED/CONDITIONAL/INFERRED | [implication] |
| [B] | [concern] | supports / challenges / inconclusive | [groundedness] | [implication] |

Note: If two people said similar things but one is CONDITIONAL (hasn't lived it yet) and
the other is GROUNDED (has), say so and adjust how much weight you give each claim.

**A note on what was real vs constructed**
Be honest: which claims in these interviews are grounded in documented knowledge or
observable patterns, and which are plausible-but-constructed? Name at least one from each
category and say why.

**One concrete voice difference**
Pick two subjects and name something specific — a term, a way of framing a concern,
a priority ordering — that makes them sound different from each other. Not "different
roles," but an actual linguistic or rhetorical difference you made a deliberate choice about.
```

---

## V-05 — Combination: Role Sequence + Schema-Instantiated Synthesis + Expectation Register Prominence

**Hypothesis**: Combining a deliberate role sequence with a fully schema-instantiated synthesis artifact and a prominent, forward-referenced Expectation Register creates structural closure across the document: setup is grounded by the register, transcripts are grounded by the register, and synthesis is grounded by the schema — making every evidence item traceable from setup to conclusion.

---

```markdown
Simulate a structured set of stakeholder interviews about {{topic}}.

The prompt has three layers: SETUP (structure before speaking), INTERVIEWS (transcript
plus extraction per subject), and SYNTHESIS (cross-subject grid plus meta-observations).
Each layer closes with a named gate block before the next begins.

---

## LAYER 0: FORMAT CONTRACT (Document-Head)

All gates use this format:
  ╔═ GATE: [name] ═╗  [ ] item ... ╚══════════╝

All evidence tables use this schema:
  | Evidence Item | Signal Type | Strength | Rationale | Origin (verbatim/inferred/corroborated) |
  Experience-Proximity (GROUNDED/CONDITIONAL/INFERRED) | Framework Dimension |

All SURPRISING/CONFIRMING/INCONCLUSIVE labels use this template:
  [LABEL] (expected: [Expectation Register → Subject X → "Expected Claim"], got: [actual])

All follow-up questions use this citation:
  triggered by: "[exact phrase from prior answer]"

Moment-label decision rules (declared once, govern all transcripts):
| Label | Decision Rule |
|-------|-------------|
| SURPRISING | Expectation Register claim violated |
| CONFIRMING | Expectation Register claim upheld |
| INCONCLUSIVE | Signal present but directionally ambiguous; cannot assign to prior-expectation category |

---

## LAYER 1: SETUP

### 1A. Subject Sequence Decision
*Name the interview order and the structural reason for it.*

| Order | Subject Role | Rationale for Position |
|-------|-------------|------------------------|
| 1st | [role] | [why this subject runs first — e.g., establishes objection surface; provides neutral baseline] |
| 2nd | [role] | [why second — e.g., challenges or extends the first subject's framing] |
| 3rd | [role, if present] | [why last] |

### 1B. Subject Cards

| Field | Subject A: [Role] | Subject B: [Role] | Subject C: [Role, if present] |
|-------|------------------|------------------|-------------------------------|
| Prior Knowledge | [direct experience] | [direct experience] | [direct experience] |
| Blind Spots | [what they haven't encountered] | [blind spots] | [blind spots] |
| Disposition | skeptic/neutral/advocate | skeptic/neutral/advocate | skeptic/neutral/advocate |
| Evidential Function | [structural contribution to evidence chain] | [function] | [function] |
| Vocabulary Term 1 | [exact term] | [exact term] | [exact term] |
| Vocabulary Term 2 | [exact term] | [exact term] | [exact term] |
| Vocabulary Term 3 | [exact term, optional] | [optional] | [optional] |
| Experience-Proximity | GROUNDED/CONDITIONAL/INFERRED — [rationale] | [rating — rationale] | [rating — rationale] |

### 1C. Expectation Register
*The forward anchor for all moment labels. Populated before any transcript.*
*The SURPRISING/CONFIRMING template draws "expected:" from this exact table.*

| Subject | Expected Claim | Basis for Expectation | Linked Interview Moment (to be filled during extraction) |
|---------|---------------|----------------------|----------------------------------------------------------|
| A | "[expected statement]" | [why — role pattern, domain knowledge, prior behavior] | *(fill during Phase 2)* |
| B | "[expected statement]" | [basis] | *(fill during Phase 2)* |
| C | "[expected statement]" | [basis] | *(fill during Phase 2)* |

*Note: The "Linked Interview Moment" column closes the forward reference — connecting
setup expectations to actual moments in the transcripts, making the register auditable
end-to-end.*

╔═ GATE: Layer 1 — Setup Complete ═╗
[ ] Subject sequence declared with per-position rationale
[ ] Subject Cards: all schema fields populated for all subjects
[ ] Vocabulary signature: 2–3 exact terms per subject (not trait descriptions)
[ ] Evidential function declared (structural, not role-restatement)
[ ] Expectation Register: one or more rows per subject, all rows before transcripts
[ ] Moment-label decision taxonomy: all three rules declared (Layer 0)
[ ] Document-head format contract: all four format rules declared (Layer 0)
╚══════════════════════════════════╝

---

## PRE-INTERVIEW MASTER GATE

╔═ PRE-INTERVIEW MASTER GATE ═╗
[ ] Subject Cards complete — GATE Layer 1, item 2: PASSED
[ ] Expectation Register populated — GATE Layer 1, item 5: PASSED
[ ] Vocabulary signatures declared for all subjects — GATE Layer 1, item 3: PASSED
[ ] Moment-label decision taxonomy declared — GATE Layer 1, item 6 (Layer 0): PASSED
[ ] Sequence justification present — GATE Layer 1, item 1: PASSED
All prerequisites confirmed. Layer 2 (Interviews) authorized.
╚══════════════════════════════╝

---

## LAYER 2: INTERVIEWS

### Interview 1 — Subject A: [Role]

**Questions**
Q1: [anchored to Subject A's prior knowledge or declared concern]
Q2: triggered by: "[exact phrase from A's Q1 answer — quote it before asking Q2]"
Q3: [additional questions as needed]

**Transcript**
*Write in Subject A's declared voice. At least one vocabulary signature term must
appear naturally in the answers. The status-quo orientation (if skeptic) should
surface through framing choices, not just assertions.*

[A answers in their voice]

**Moment Labels — Subject A**
*Template activated: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE.*

| Moment Summary | Label | Expected (→ Register) | Actual | Register Row Updated? |
|---------------|-------|----------------------|--------|----------------------|
| [brief description] | SURPRISING/CONFIRMING/INCONCLUSIVE | [Register → Subject A "Expected Claim"] | [what emerged] | ✓ Link added to Register |

*Vocabulary exercise: [list which declared terms appeared. C-22 confirmed FULLY
SATISFIED in PRE-INTERVIEW MASTER GATE — this is a traceable pointer, not a
free-standing assertion.]*

**Evidence Extraction — Subject A**

*Schema instantiation (first row is a fully populated example):*
| Evidence Item | Signal Type | Strength | Rationale | Origin | Experience-Proximity | Framework Dimension |
|--------------|-------------|----------|-----------|--------|---------------------|---------------------|
| [e.g., "Insists on parallel-run period before cutover"] | adoption risk | strong | Verbatim; Subject A has authority over adoption timeline | verbatim | GROUNDED — has managed 2 prior migrations | Prior Knowledge: migration risk sensitivity |
| [next item] | [type] | [rating] | [rationale] | [origin] | [proximity] | [dimension from Subject A's card] |

╔═ GATE: Layer 2a — Subject A Interview ═╗
[ ] At least one question anchored to declared concern
[ ] At least one follow-up with triggered-by citation
[ ] Transcript in declared persona voice
[ ] Declared vocabulary terms exercised
[ ] Moment label table: all columns; Register citation; Register row marked linked
[ ] Evidence table: all schema columns; at least one row
[ ] Both taxonomy dimensions applied per evidence item (Origin-of-Claim + Experience-Proximity)
╚══════════════════════════════════════════╝

---

### Interview 2 — Subject B: [Role]

[Same structure. Include cross-reference observation: how does Subject B's framing
engage with or diverge from Subject A's signals?]

**Cross-Reference Observation**
| Subject A Signal | Subject B Response | Direction |
|-----------------|---------------------|-----------|
| [signal from A] | [what B said about it, explicitly or implicitly] | reinforces / challenges / sidesteps |

╔═ GATE: Layer 2b — Subject B Interview ═╗
[ ] [same checklist as Layer 2a]
[ ] Cross-reference observation table populated
╚═════════════════════════════════════════╝

---

### Interview 3 — Subject C: [Role] *(if present)*

[Same structure.]

╔═ GATE: Layer 2c — Subject C Interview ═╗
[ ] [same checklist as Layer 2a]
╚═════════════════════════════════════════╝

---

## LAYER 3: SYNTHESIS

### 3A. Objection Lifecycle *(N/A if no skeptic present)*

| Subject | Opening Objection | Final Status | Evidence Trail |
|---------|------------------|-------------|----------------|
| [skeptic] | [stated objection from their transcript] | persisted / transformed into [X] / resolved by [Y] | [Interview 2: ...; Interview 3: ...] |

### 3B. Cross-Interview Synthesis Artifact

*Schema columns declared:*
*Subject | Framework Dimension | Testimony Direction | Epistemic Weight Adjustment | Implication*

*Instantiated example row (first entry):*
| Subject | Framework Dimension | Testimony Direction | Epistemic Weight Adjustment | Implication |
|---------|--------------------|--------------------|-----------------------------|-------------|
| A (example) | Migration risk sensitivity | challenges | GROUNDED — direct migration authority; objection is load-bearing, not conditional | Parallel-run requirement must appear in implementation plan |

*All subjects:*
| Subject | Framework Dimension | Testimony Direction | Epistemic Weight Adjustment | Implication |
|---------|--------------------|--------------------|-----------------------------|-------------|
| A | [from Subject A card] | supports / challenges / inconclusive | [explicit adjustment or "none — GROUNDED, full weight"] | [implication] |
| B | [from Subject B card] | supports / challenges / inconclusive | [adjustment] | [implication] |
| C | [from Subject C card, if present] | | | |

*Pattern note: Name any convergence, contradiction, or cascade across subjects —
where does the evidence point together, and where does it split?*

### 3C. Expectation Register — Closure Review
*Back-reference: confirm the Register's "Linked Interview Moment" column is filled for
all subjects. Name any Register row where reality diverged from expectation — these
are the highest-value findings.*

| Subject | Expected | Actual | Divergence? | Finding value |
|---------|---------|--------|------------|---------------|
| A | [Register entry] | [what emerged] | yes/no | [if yes: name the insight] |
| B | [Register entry] | [what emerged] | yes/no | [if yes: name the insight] |

### 3D. Simulation Fidelity Note
[Distinguish grounded from constructed claims. Name at least one specific basis
for a grounded claim — documented knowledge, observable domain pattern, or
stated prior experience.]

### 3E. Voice Divergence Observation
[Cite a specific term, framing preference, or concern priority that makes two
subjects demonstrably different in voice. Name the subjects and the exact contrast.]

╔═ GATE: Layer 3 — Synthesis Complete ═╗
[ ] Objection lifecycle table: fate declared (persisted/transformed/resolved) with trail
[ ] Synthesis artifact: all schema columns; all subjects; example row instantiated
[ ] Epistemic weight adjustment named for at least one item
[ ] Register closure review: "Linked Interview Moment" filled; divergences named
[ ] Simulation fidelity note: grounded vs constructed; at least one specific basis
[ ] Voice divergence: specific term or framing contrast named (not role-description)
╚═══════════════════════════════════════╝
```

---

## Summary Table

| Variation | Axis | Primary Hypothesis | Key Differentiators |
|-----------|------|--------------------|---------------------|
| V-01 | Role sequence (skeptic-first) | Skeptic-first order makes objection lifecycle structurally visible across interviews | Sequence justification table, objection lifecycle as primary synthesis spine |
| V-02 | Output format (schema-heavy) | Full table delivery makes each criterion independently auditable without prose parsing | Schema contract in Section 0, instantiation examples at first point of use, every element in table form |
| V-03 | Lifecycle emphasis (named gate blocks) | Phase gates as the structural spine remove authorial discretion about phase completion | Named checklist blocks with ╔═ ═╗ frame, gate at every phase transition, criteria ownership per gate |
| V-04 | Conversational register + inertia framing | Lower structural overhead feel while keeping coverage; status-quo competition surfaced through subject voice | Plain-language instructions, "relationship to the status quo" as explicit profile field, inertia surfaces in transcript framing |
| V-05 | Role sequence + schema synthesis + register prominence | Setup → transcript → synthesis traceable end-to-end through forward/back references | Register has "Linked Interview Moment" column, synthesis has instantiated example row, master gate cites sub-gates by name |
