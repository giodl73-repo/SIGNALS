# prove-interview — Prompt Variations R7
# Date: 2026-03-15
# Rubric: prove-interview-rubric-v7-2026-03-15.md
# Round: 7 (C-23/C-24 baseline; primary targets: C-25 template-register bridge, C-26 vocabulary enforcement, C-27 dual taxonomy)

---

## Variation Axes Selected

| Axis | Description |
|------|-------------|
| Role sequence | Skeptic-first ordering — objection arc as structural spine, lifecycle earned not retrofitted |
| Output format | Table-dominant — separate Experience-Proximity and Origin-of-Claim columns enforce C-27 by construction |
| Lifecycle emphasis | Explicit phase gates — C-25/C-26/C-27 encoded as binary gate preconditions, not authorial reminders |
| Role sequence + phrasing register | Skeptic-first × investigative reporter voice — source credibility framing naturalizes dual taxonomy |
| Output format + lifecycle + inertia framing | Tables + gates + artifact-level Inertia Profile — full structural enforcement stack |

Single-axis variations: V-01 (role sequence), V-02 (output format), V-03 (lifecycle emphasis)
Combination variations: V-04 (role sequence + phrasing register), V-05 (output format + lifecycle + inertia framing)

New v7 territory probed:
- **C-25 bridge enforcement** (all five): the SURPRISING/CONFIRMING template names the Expectation Register as the structural source for "expected:", referencing by subject row and field name — not authored inline
- **C-26 vocabulary close** (V-01, V-02, V-03, V-05): a per-subject vocabulary audit table after each transcript declares FOUND / NOT FOUND per term; NOT FOUND blocks proceeding
- **C-27 column separation** (V-02, V-04, V-05): evidence table has two named columns — Experience-Proximity and Origin-of-Claim — with enforcement rule prohibiting tag substitution between them
- **C-27 definitional clarity** (V-01, V-03): inline column definitions establish the orthogonality contract in the prompt body so it is self-replicating for the author

---

## V-01 — Role Sequence: Skeptic-First with Objection Arc

**Axis**: Role sequence
**Hypothesis**: Prescribing a skeptic-first sequence makes the objection lifecycle (C-21) structurally
earned rather than retrofitted. When the hardest objection is on record before the advocate speaks,
the synthesis must trace whether it was answered — silence on the objection becomes visible evidence,
not an authorial omission. The sequence also enforces C-25 by creating a prior expectation structure
that must be declared before the skeptic interview begins: the register cannot be populated after
the fact when the skeptic runs first.

```
You are running a simulated stakeholder interview investigation for the feature topic: {{topic}}.

This is not a real interview. It is a structured simulation grounded in documented persona
knowledge, producing evidence artifacts for downstream topic narrative decisions.

All phases complete in order. Do not write any transcript before Phase 0 is done.

---

PHASE 0 — PRE-INTERVIEW STRUCTURE

Complete the following before writing any transcript line.

STEP 0A — Subject Roster and Sequence Justification

Select three subjects. Sequence them in this fixed order:

  1. THE SKEPTIC
     A subject with legitimate grounds for doubt or resistance — based on their role,
     experience, or what they have at stake. Not a straw-man. Their objection must be
     coherent and grounded in their declared prior knowledge. Running them first puts
     the hardest objection on the table before any advocate speaks.

  2. THE PRACTITIONER
     A subject whose knowledge is operational and procedural. They work in the domain
     the feature addresses. They neither strongly advocate nor strongly resist — they
     represent what the work actually looks like at ground level.

  3. THE ADVOCATE
     A subject with grounded reasons to want the feature direction to succeed. Their
     enthusiasm connects to their declared role and experience, not generic optimism.
     Running them last means their advocacy must address what the skeptic put on record.

Sequence justification (one sentence): Explain why skeptic-first, practitioner-second,
advocate-third is the optimal ordering for this specific investigation.

---

STEP 0B — Subject Cards (complete all three before any transcript)

For each subject, complete this card in full:

## Subject Card: [Role/Name]

- Role: [job title or function]
- Evidential Function: [what this subject's position does for the evidence structure —
  not their disposition, their structural contribution. Example: "establishes the objection
  surface that the practitioner and advocate must address or leave standing"]
- Experience-Proximity: GROUNDED | CONDITIONAL | INFERRED
  Justification: [one sentence — why does this subject have this proximity level?]
- Prior Knowledge: [2-3 sentences: what they know, have worked with, care about in this domain]
- Blind Spots: [1-2 sentences: what they have NOT experienced or seen — a separate field,
  not a sub-bullet of prior knowledge]
- Vocabulary Signature (auditable contract — declared before transcript):
  - Term 1: [a specific term this persona would use — distinctive enough to audit against
    the transcript. General trait descriptors ("uses technical language") fail.]
  - Term 2: [a second distinctive term]
  - Term 3: [a third distinctive term]
  NOTE: At least one of these three terms must appear naturally in this subject's transcript.
  Declaration without use is an open contract — the audit in Step 2 will catch it.

GATE 0B: Do not proceed to Step 0C until all three subject cards have:
  role, evidential function, experience-proximity with justification, prior knowledge
  (positive), blind spots (separate), and three auditable vocabulary terms.

---

STEP 0C — Expectation Register

The expectation register is the mandatory source for all SURPRISING/CONFIRMING labels in
this simulation. It must be complete before any transcript is written.

| Subject     | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|-------------|-------------------|--------------------|-----------------------|-------------------|
| [Skeptic]   |                   |                    |                       |                   |
| [Practitioner] |                |                    |                       |                   |
| [Advocate]  |                   |                    |                       |                   |

The Expected Surprise column is mandatory. Leaving it blank means you have not thought
about what would violate your prior model. Fill it.

FORMAT TEMPLATE — embed this template once here; reference it in every extraction section:

  SURPRISING  (expected: [Expectation Register → Subject: {name}, Field: "Expected
               Position / Objection / Surprise"], got: [what actually emerged])

  CONFIRMING  (validates: [Expectation Register → Subject: {name}, Field: "Expected
               Position / Confirmation"])

  INCONCLUSIVE (closest register field: [Expectation Register → Subject: {name},
                Field: "{field}"], ambiguity: [why it fits neither category cleanly])

The "expected:" slot must reference the register by subject row and field name. An
expectation authored inline — without pointing to a pre-declared register cell — fails
C-25. If the label cannot point to a filled register cell, fix the register first.

GATE 0C: Do not begin Phase 1 until all three expectation register rows are complete
with content in every column, and the format template is present in this document.

---

PHASE 1 — INTERVIEW: THE SKEPTIC

Transcript

Opening question: [A question anchored in this subject's declared prior knowledge and
blind spots — probing what grounds their skepticism specifically.]

[Skeptic]: [Answer in this subject's distinct voice. At least one declared vocabulary
term must appear naturally in this answer or in a subsequent answer. If the term does
not arise naturally, choose a question where it would.]

Follow-up (triggered by: "[exact phrase from the preceding answer that prompted this]"):
[follow-up question]

[Skeptic]: [answer]

[Continue 2-3 additional exchanges. The skeptic's primary objection must be clearly
and explicitly stated by the end of this interview — it becomes the objection whose
lifecycle is tracked in Phase 4.]

After the transcript, complete both of the following before proceeding.

VOCABULARY AUDIT — Skeptic:
- "[Term 1]": FOUND in A[N] — "[brief quote]" | NOT FOUND (open contract — revise
  a question to elicit this term naturally before continuing)
- "[Term 2]": FOUND / NOT FOUND
- "[Term 3]": FOUND / NOT FOUND

At least 1 of 3 terms must be FOUND. If none are found, the vocabulary contract is
entirely open — add a natural exchange before proceeding.

MOMENT LABEL — using the Phase 0C format template:

  [SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Expectation Register →
    Subject: Skeptic, Field: "{field_name}"], ...)

EVIDENCE EXTRACTION — Skeptic:

For each extracted item:
- Evidence Item: [what was said or implied]
- Signal Type: adoption risk | feasibility concern | requirement gap | scope signal | constraint
- Experience-Proximity: GROUNDED | CONDITIONAL | INFERRED
  [If CONDITIONAL, name the blind spot that limits this subject's standing on this item]
- Origin-of-Claim: verbatim | inferred | corroborated
  [verbatim = stated or closely paraphrased in transcript; inferred = implied but not said;
  corroborated = consistent signal from two or more subjects — available from Phase 2 onward]
- Strength: strong | moderate | weak
- Strength Rationale: [one sentence: why does this item earn this rating?]

ORTHOGONALITY RULE:
  Experience-Proximity answers: "How close is this subject to direct operational experience
  of this claim?" — GROUNDED means they have experienced it firsthand.

  Origin-of-Claim answers: "How was this claim derived from the transcript?" — verbatim
  means they explicitly stated it.

  These are independent dimensions. A GROUNDED source can produce inferred evidence
  (they know it well but did not say it directly). A CONDITIONAL source can produce
  verbatim evidence (they stated it, but a blind spot limits how much weight it carries).
  Do not use one dimension's tags to fill the other's slot.

PHASE 1 GATE: Before proceeding to Phase 2, confirm:
  [ ] At least one declared vocabulary term appears in the Skeptic's transcript
  [ ] Moment label references Expectation Register by subject name and field name
  [ ] Every evidence item has both Experience-Proximity and Origin-of-Claim populated
  [ ] The skeptic's primary objection is explicitly stated in the transcript

---

PHASE 2 — INTERVIEW: THE PRACTITIONER

[Same transcript structure as Phase 1. At least one declared vocabulary term must appear
naturally. Questions probe operational ground truth — what the work actually looks like,
not what it ideally looks like.]

Required: At least one question must probe whether the practitioner's operational reality
speaks to — or is silent about — the skeptic's primary objection from Phase 1.

VOCABULARY AUDIT — Practitioner: [same format as Phase 1]

MOMENT LABEL — using the Phase 0C format template:
  [SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Expectation Register →
    Subject: Practitioner, Field: "{field_name}"], ...)

EVIDENCE EXTRACTION — Practitioner:
[Same format as Phase 1. "corroborated" is now available for Origin-of-Claim when an
item matches a Phase 1 extraction from the Skeptic.]

PHASE 2 GATE: Before proceeding to Phase 3, confirm:
  [ ] At least one vocabulary term FOUND in Practitioner's transcript
  [ ] Moment label references Expectation Register by subject and field
  [ ] Both taxonomy dimensions populated for every evidence row
  [ ] Note whether the Skeptic's Phase 1 objection was addressed, transformed, or ignored

---

PHASE 3 — INTERVIEW: THE ADVOCATE

[Same transcript structure. At least one declared vocabulary term must appear naturally.
The advocate's opening question should be anchored in their declared evidential function.]

Required: At least one question probes whether the advocate is aware of the skeptic's
primary objection and what their answer to it is.

VOCABULARY AUDIT — Advocate: [same format]

MOMENT LABEL — using the Phase 0C format template:
  [SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Expectation Register →
    Subject: Advocate, Field: "{field_name}"], ...)

EVIDENCE EXTRACTION — Advocate: [same format; "corroborated" available from Phase 1+2]

PHASE 3 GATE: Before proceeding to Phase 4, confirm:
  [ ] At least one vocabulary term FOUND in Advocate's transcript
  [ ] Moment label references Expectation Register by subject and field
  [ ] Both taxonomy dimensions populated for every evidence row
  [ ] The advocate's response to (or avoidance of) the Skeptic's objection is visible

---

PHASE 4 — CROSS-INTERVIEW SYNTHESIS

Convergences and Contradictions

Identify at least one pattern, contradiction, or convergence across the three subjects.
Name the subjects and the specific evidence items — do not summarize without reference.

Objection Lifecycle

Trace the Skeptic's primary objection from Phase 1:
- Initial objection (Phase 1): [state it as declared]
- Practitioner's response (Phase 2): [addressed it? transformed it? passed in silence?
  Quote or reference the specific transcript moment]
- Advocate's response (Phase 3): [persisted? transformed? resolved? Quote or reference]
- Final status: PERSISTED | TRANSFORMED | RESOLVED
  [one sentence explaining why — what evidence moved it or left it standing]

Epistemic Weight Adjustment

Name at least one evidence item where Experience-Proximity explicitly adjusts synthesis weight:

  "Item [N] is CONDITIONAL — [subject] has not experienced [specific gap named in their
  blind spots]. Treat this objection as a risk to monitor, not a blocker, until verified
  by a GROUNDED source who has seen the alternative."

The weight adjustment must be named. Treating CONDITIONAL and GROUNDED items as
equivalently weighted without acknowledgment fails C-24.

PHASE 4 GATE:
  [ ] Objection lifecycle traced with PERSISTED / TRANSFORMED / RESOLVED status
  [ ] At least one named epistemic weight adjustment present
  [ ] Convergence or contradiction named with specific evidence item references

---

PHASE 5 — SIMULATION FIDELITY NOTE

Brief meta-note:
1. Grounded claim: name at least one claim based on documented persona knowledge or domain context
2. Constructed plausibility: name at least one claim extrapolated beyond direct evidence
3. Voice contrast: name one specific vocabulary term or framing choice that made two subjects
   sound genuinely different — not "they had different roles" without a specific citation

---

Artifact: {{topic}}-prove-interview-{{date}}.md
```

---

## V-02 — Output Format: Table-Dominant with Dual Taxonomy Columns

**Axis**: Output format
**Hypothesis**: A table with separate columns for Experience-Proximity and Origin-of-Claim makes
C-27 impossible to collapse — the column headers are the structural enforcement. An author cannot
substitute one tag set for the other when both columns are present and labeled. Similarly, the
Expectation Register as a named pre-interview table makes C-25 enforcement mechanical: the format
template can reference the register by row and column rather than by memory. Table structure makes
compliance binary and auditable; prose structure makes omission invisible.

```
You are running a simulated stakeholder interview investigation for the feature topic: {{topic}}.

Output follows structured table format throughout. All pre-interview declarations and
evidence extraction are expressed in tables. Complete all preflight tables before writing
any transcript.

---

PREFLIGHT TABLES (complete all before any transcript)

---

TABLE 1 — SUBJECT REGISTRY

Complete all subject fields before writing any interview.

| Field                         | Subject 1     | Subject 2     | Subject 3     |
|-------------------------------|---------------|---------------|---------------|
| Role / Title                  |               |               |               |
| Evidential Function           |               |               |               |
| Experience-Proximity          | GROUNDED /    | GROUNDED /    | GROUNDED /    |
|                               | CONDITIONAL / | CONDITIONAL / | CONDITIONAL / |
|                               | INFERRED      | INFERRED      | INFERRED      |
| Proximity Justification       |               |               |               |
| Prior Knowledge               |               |               |               |
| Blind Spots (separate field)  |               |               |               |
| Disposition                   |               |               |               |
| Primary Concern               |               |               |               |
| Vocab Term 1                  |               |               |               |
| Vocab Term 2                  |               |               |               |
| Vocab Term 3                  |               |               |               |

Rules:
- Minimum 2 subjects. Each must be meaningfully distinct in role, knowledge level, or concern.
- Experience-Proximity must be filled for every subject — blank cells fail.
- Vocab Terms must be specific enough to audit: "uses technical language" fails;
  "migration cadence" or "data lineage" passes.
- At least one vocab term per subject must appear naturally in that subject's transcript.
  A term declared here but absent from the transcript is an open contract — the vocabulary
  audit table (Table 3A) catches this.

---

TABLE 2 — EXPECTATION REGISTER

Complete before any transcript. This table is the mandatory source for all
SURPRISING/CONFIRMING labels. The "expected:" slot in every moment label must reference
this table by subject row and column name — not authored from memory.

| Subject      | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|--------------|-------------------|--------------------|-----------------------|-------------------|
| [Subject 1]  |                   |                    |                       |                   |
| [Subject 2]  |                   |                    |                       |                   |
| [Subject 3]  |                   |                    |                       |                   |

FORMAT TEMPLATE — embed this in the document and reference it for every moment label:

  SURPRISING  (expected: [Expectation Register → Subject: {name},
               Column: "Expected Position / Objection / Surprise"],
               got: [what actually emerged from the transcript])

  CONFIRMING  (validates: [Expectation Register → Subject: {name},
               Column: "Expected Position / Confirmation"])

  INCONCLUSIVE (closest match: [Expectation Register → Subject: {name},
                Column: "{column}"],
                ambiguity: [why neither SURPRISING nor CONFIRMING fits cleanly])

A moment label whose "expected:" slot does not name this table by subject and column
was authored from memory — the register bridge (C-25) is broken. Fix the register
entry first, then label.

---

TABLE 3 — SEQUENCE JUSTIFICATION

| Position | Subject       | Rationale                                           |
|----------|---------------|-----------------------------------------------------|
| First    |               | [what this subject surfaces by running first]       |
| Second   |               | [what their position adds relative to the first]    |
| Third    |               | [what they resolve, confirm, or challenge]          |

---

PREFLIGHT GATE: Do not begin any transcript until:
  [ ] Table 1 fully populated — no blank cells in required rows
  [ ] Table 2 fully populated — all four columns filled for every subject
  [ ] Table 3 sequence rationale present for all subjects
  [ ] Every subject has 3 specific, auditable vocabulary terms declared

---

INTERVIEW TRANSCRIPTS (one subject at a time)

For each subject, the transcript follows this structure, then Tables 3A/3B/3C immediately after.

---

[Subject 1 — Role] ([Disposition])

Q1: [opening question anchored in Subject 1's declared prior knowledge]
A1: [answer in Subject 1's distinct voice — at least one vocab term must appear here
    or in a subsequent answer]

Q2 (triggered by: "[exact phrase from A1 that prompted this]"): [follow-up question]
A2: [answer]

Q3: [question]
A3: [answer]

[Add Q4/A4 if needed to surface the primary concern or a labelable moment]

---

TABLE 3A — VOCABULARY AUDIT: [Subject 1]

| Declared Term | Status                        | Transcript Evidence                  |
|---------------|-------------------------------|--------------------------------------|
| "[Term 1]"    | FOUND in A[N] / NOT FOUND     | "[brief quote, or blank if not found]"|
| "[Term 2]"    | FOUND in A[N] / NOT FOUND     |                                      |
| "[Term 3]"    | FOUND in A[N] / NOT FOUND     |                                      |

Minimum 1 of 3 terms must be FOUND. If none found: add a natural exchange that elicits
a declared term, then update the audit table before proceeding.

---

TABLE 3B — MOMENT LABEL: [Subject 1]

Using the Table 2 format template:

  [SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Expectation Register →
    Subject: {Subject 1 name}, Column: "{column}"], ...)

---

TABLE 3C — EVIDENCE EXTRACTION: [Subject 1]

| #  | Evidence Item | Signal Type  | Experience-Proximity   | Proximity Note         | Origin-of-Claim                  | Strength | Rationale       |
|----|---------------|--------------|------------------------|------------------------|----------------------------------|----------|-----------------|
| 1  |               |              | GROUNDED /             | [if CONDITIONAL:       | verbatim /                       | strong / |                 |
|    |               |              | CONDITIONAL /          | name the blind spot]   | inferred /                       | moderate /|                |
|    |               |              | INFERRED               |                        | corroborated                     | weak     |                 |
| 2  |               |              |                        |                        |                                  |          |                 |

COLUMN DEFINITIONS — these are two orthogonal dimensions; apply them independently:

  Experience-Proximity (left taxonomy column):
    Answers: "How close is this subject to direct operational experience of this claim?"
    - GROUNDED:    subject has experienced this specific situation firsthand
    - CONDITIONAL: a declared blind spot limits their standing — name it in Proximity Note
    - INFERRED:    subject's stance on this was not directly stated

  Origin-of-Claim (right taxonomy column):
    Answers: "How was this claim derived from the transcript?"
    - verbatim:     directly stated or closely paraphrased in the transcript
    - inferred:     implied by the answer but not explicitly said
    - corroborated: consistent signal from 2+ subjects [available Subject 2 onward]

  THESE COLUMNS ARE ORTHOGONAL. A claim can be GROUNDED yet inferred (experienced
  subject whose stance was implied, not stated). A claim can be CONDITIONAL yet verbatim
  (subject stated it directly, but a blind spot limits its weight). Do NOT use one
  column's tags to fill the other. A row where "inferred" appears in the
  Experience-Proximity column — or "GROUNDED" appears in the Origin-of-Claim column —
  has collapsed the taxonomy. Fix it.

---

INTERVIEW GATE (per subject): Before proceeding to the next subject (or to Synthesis):
  [ ] Table 3A shows at least 1 FOUND vocabulary term
  [ ] Table 3B moment label references Expectation Register by subject and column name
  [ ] Table 3C has both Experience-Proximity and Origin-of-Claim columns populated for all rows
  [ ] No row has Experience-Proximity tags (GROUNDED/CONDITIONAL/INFERRED) in the
      Origin-of-Claim column, or vice versa

---

[Repeat transcript + Tables 3A/3B/3C for Subject 2 and Subject 3]

"corroborated" is available for Origin-of-Claim from Subject 2 onward, when a Subject 2
or Subject 3 item consistently signals the same finding as a prior subject's item.

---

SYNTHESIS TABLES

---

TABLE 4 — CROSS-INTERVIEW EVIDENCE SUMMARY

Compile all items from all Table 3C instances:

| #  | Evidence Item | Subject | Signal Type | Experience-Proximity | Origin-of-Claim | Strength |
|----|---------------|---------|-------------|---------------------|-----------------|----------|
|    |               |         |             |                     |                 |          |

---

TABLE 5 — SYNTHESIS FINDINGS

| Dimension                                              | Finding                                    |
|--------------------------------------------------------|--------------------------------------------|
| Convergence (where subjects agree despite diff. roles) |                                            |
| Primary contradiction (named subjects + items)         |                                            |
| Objection lifecycle: initial objection                 | [subject, phrased as stated in transcript] |
| Objection lifecycle: intermediate response             | [Subject 2's response or silence]          |
| Objection lifecycle: final status                      | PERSISTED / TRANSFORMED / RESOLVED         |
| Epistemic weight adjustment (named item + rationale)   |                                            |
| Subject sequence: what the ordering revealed           |                                            |

Epistemic weight adjustment format:
  "Item #[N] from [Subject] is CONDITIONAL — they have not experienced [blind spot].
  Treat as a risk to monitor, not a blocker, until corroborated by a GROUNDED source."

---

TABLE 6 — VOICE DIVERGENCE AUDIT

| Subject Pair   | Specific Vocabulary / Framing Contrast           | Effect on Evidence Reading |
|----------------|--------------------------------------------------|---------------------------|
| [S1] vs [S2]   | [specific term or framing — not "different roles"]|                           |
| [S1] vs [S3]   |                                                  |                           |
| [S2] vs [S3]   |                                                  |                           |

At least one row must name a specific vocabulary term or framing choice — not a generic
role observation.

---

TABLE 7 — SIMULATION FIDELITY NOTE

| Type                | Item                                                          |
|---------------------|---------------------------------------------------------------|
| Grounded claim      |                                                               |
| Constructed         |                                                               |
| Taxonomy verified   | [confirm Experience-Proximity and Origin-of-Claim applied as  |
|                     | separate dimensions in all Table 3C instances]                |

---

Artifact: {{topic}}-prove-interview-{{date}}.md
```

---

## V-03 — Lifecycle Emphasis: Explicit Phase Gates with C-25/C-26/C-27 Checks

**Axis**: Lifecycle emphasis
**Hypothesis**: Encoding C-25/C-26/C-27 as binary gate preconditions rather than authorial reminders
changes their status from aspirational to structural. Without gates, each criterion depends on the
author remembering it; with gates, the output cannot advance without satisfying it. The gate after
the Expectation Register phase specifically confirms the template-register bridge before any
interview begins, making C-25 a sequencing constraint rather than an aspirational addition. The
per-interview gate confirms vocabulary use (C-26) and taxonomy separation (C-27) for each subject
before the next interview starts.

```
You are running a simulated stakeholder interview investigation for the feature topic: {{topic}}.

This simulation is organized into PHASES with explicit GATE CONDITIONS. Do not begin a
later phase until the stated gate is satisfied. Gates are not suggestions — they are
preconditions for proceeding.

Three v7 structural requirements are encoded directly into gate checklists:
- C-25: The SURPRISING/CONFIRMING format template explicitly names the Expectation
  Register as its source for the "expected:" slot — reference by subject and field name,
  not authored inline
- C-26: At least one declared vocabulary term per subject appears naturally in that
  subject's transcript — declaration without use is an open contract, caught at Gate 2
- C-27: Evidence items carry two separate taxonomy columns — Experience-Proximity
  and Origin-of-Claim — applied independently, never collapsed into one tag set

---

================================================================================
PHASE 0 — SUBJECT DESIGN
================================================================================

Design 2-3 interview subjects. For each, complete a subject card before any transcript:

  Subject Card: [Role/Name]
  ├─ Role: [title or function]
  ├─ Evidential Function: [what this subject's position does for the evidence structure
  │   — not their disposition, their structural contribution to the investigation.
  │   Example: "provides the implementation-level reality that the executive's framing
  │   cannot capture; serves as the feasibility probe"]
  ├─ Experience-Proximity: GROUNDED | CONDITIONAL | INFERRED
  │   Justification: [one sentence]
  ├─ Prior Knowledge: [what they know, have worked with, have seen — 2-3 sentences;
  │   positive declaration only]
  ├─ Blind Spots: [what they have NOT seen or done — a separate explicit field,
  │   not implied by the scope of their prior knowledge]
  ├─ Disposition: skeptic | practitioner | advocate | evaluator | neutral
  ├─ Primary Concern: [the one thing that most shapes their evaluation of this topic]
  └─ Vocabulary Signature (auditable contract):
       - Term 1: [specific term — auditable, not a trait descriptor]
       - Term 2: [specific term]
       - Term 3: [specific term]

GATE 0 → PHASE 1: Verify all subject cards before proceeding.
  [ ] Every subject has a declared Evidential Function (not just role or disposition)
  [ ] Every subject has an Experience-Proximity value with a justification sentence
  [ ] Every subject has a separate Blind Spots field (not blank, not implied)
  [ ] Every subject has 3 vocabulary terms specific enough to audit
  [ ] No two subjects share the same Primary Concern
  [ ] Minimum 2 subjects, meaningfully distinct in role and knowledge level

Do not begin Phase 1 until all six checks pass.

---

================================================================================
PHASE 1 — EXPECTATION REGISTER
================================================================================

Populate this register in full before writing any interview transcript.

| Subject   | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|-----------|-------------------|--------------------|-----------------------|-------------------|
| [S1]      |                   |                    |                       |                   |
| [S2]      |                   |                    |                       |                   |
| [S3]      |                   |                    |                       |                   |

The Expected Surprise column is mandatory for every row. Leaving it blank means the
prior model has not been pushed to its edge — fill it.

FORMAT TEMPLATE — declare this template once in Phase 1 and reference it in every
subsequent extraction section. The "expected:" slot must name this register by subject
and field:

  SURPRISING  (expected: [Expectation Register → Subject: {name}, Field: "{Expected
               Position / Objection / Surprise}"],
               got: [what actually emerged from the transcript])

  CONFIRMING  (validates: [Expectation Register → Subject: {name}, Field: "{Expected
               Position / Confirmation}"])

  INCONCLUSIVE (closest register field: [Expectation Register → Subject: {name},
                Field: "{field}"],
                ambiguity: [why it fits neither category cleanly])

An expectation authored inline — not pointing to a pre-populated register cell — fails
C-25. If a label cannot point to a register cell, fix the register first, then label.

GATE 1 → PHASE 2: Verify before any interview begins.
  [ ] All subject rows populated — no empty columns
  [ ] Expected Surprise column filled for every subject (no blanks)
  [ ] Format template is present in this document
  [ ] Format template explicitly names the Expectation Register in the "expected:" slot
      (not just "[what you expected]" — the register is named as the structural source)
  [ ] Format template uses subject-and-field reference syntax, not inline authoring

Do not begin Phase 2 until all five checks pass.

---

================================================================================
PHASE 2 — INTERVIEW TRANSCRIPTS (run one subject at a time)
================================================================================

For each subject, complete the full transcript + extraction before moving to the next.

TRANSCRIPT: [Subject Role] ([Disposition])

Opening question: [anchored in this subject's declared prior knowledge]

[Subject]: [answer in this subject's distinct voice]

Follow-up (triggered by: "[exact phrase from the preceding answer]"): [question]

[Subject]: [answer]

[Continue 2-4 exchanges. At least one exchange must probe the subject's declared
Primary Concern. At least one declared vocabulary term must appear naturally in
the answers — if none arise, add a question that creates a natural opportunity.]

---

VOCABULARY AUDIT — [Subject]:

After the transcript, before extraction:

  "[Term 1]": FOUND in A[N] — "[phrase from answer]"  |  NOT FOUND (open contract)
  "[Term 2]": FOUND in A[N] — "[phrase]"               |  NOT FOUND
  "[Term 3]": FOUND in A[N] — "[phrase]"               |  NOT FOUND

Minimum 1 of 3 must be FOUND. If none found: revise or add an exchange that naturally
surfaces a declared term, then update this audit before proceeding to extraction.

---

MOMENT LABEL — using the Phase 1 format template:

  [SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Expectation Register →
    Subject: {name}, Field: "{field}"], ...)

---

EVIDENCE EXTRACTION — [Subject]:

| # | Evidence Item | Signal Type | Experience-Proximity | Proximity Note | Origin-of-Claim | Strength | Rationale |
|---|---------------|-------------|---------------------|----------------|-----------------|----------|-----------|
| 1 |               |             | GROUNDED /          | [if CONDITIONAL:| verbatim /     | strong / |           |
|   |               |             | CONDITIONAL /       | name the blind  | inferred /     | moderate /|          |
|   |               |             | INFERRED            | spot]           | corroborated   | weak     |           |
| 2 |               |             |                     |                 |                |          |           |

Column definitions — apply independently, never substitute one for the other:

  Experience-Proximity (how close is this subject to direct operational experience
  of this claim?):
    GROUNDED    — has experienced this specific situation firsthand
    CONDITIONAL — a declared blind spot limits standing; name it in Proximity Note
    INFERRED    — subject's stance was not directly stated

  Origin-of-Claim (how was this claim derived from the transcript?):
    verbatim     — stated or closely paraphrased directly in the transcript
    inferred     — implied by the answer, not explicitly said
    corroborated — consistent signal from 2+ subjects [available 2nd subject onward]

ORTHOGONALITY CONTRACT: A GROUNDED source can produce inferred evidence. A CONDITIONAL
source can produce verbatim evidence. These dimensions are independent. If "GROUNDED"
appears in the Origin-of-Claim column, or "verbatim" appears in the Experience-Proximity
column, the taxonomy has been collapsed — fix it before proceeding.

---

GATE 2 — Per-Interview Check (run after each interview, before the next):
  [ ] Vocabulary Audit shows at least 1 FOUND term for this subject
  [ ] Moment label is present and references Expectation Register by subject and field name
  [ ] Every evidence row has Experience-Proximity populated (GROUNDED/CONDITIONAL/INFERRED)
  [ ] Every evidence row has Origin-of-Claim populated (verbatim/inferred/corroborated)
  [ ] No row uses Experience-Proximity tags in the Origin-of-Claim column (taxonomy collapse)
  [ ] No row uses Origin-of-Claim tags in the Experience-Proximity column (taxonomy collapse)
  [ ] Follow-up questions cite the exact phrase that triggered them

Repeat Phase 2 for each remaining subject. Run Gate 2 after each before starting the next.

---

================================================================================
PHASE 3 — CROSS-INTERVIEW SYNTHESIS
================================================================================

After all interviews and Gate 2 checks are complete:

CONVERGENCE
Where do subjects agree despite different roles, knowledge levels, or concerns?
Name the specific evidence items — do not summarize without reference.

CONTRADICTION
Name at least one conflict between subjects' extracted items. Name the subjects
and the specific items that conflict.

OBJECTION LIFECYCLE (required when at least one subject holds a skeptic or challenger
disposition; N/A only for single-subject investigations):
- Initial objection: [which subject stated it, what was it as stated in the transcript]
- Mid-sequence: [was it addressed, transformed, or passed in silence by subsequent subjects?
  Reference the specific transcript exchange]
- Final status: PERSISTED | TRANSFORMED | RESOLVED
  [one sentence: what evidence moved it to this status, or what kept it standing]

EPISTEMIC WEIGHT ADJUSTMENT
Name at least one evidence item where Experience-Proximity explicitly adjusts synthesis weight:

  "[Item] from [Subject] is CONDITIONAL — [subject] has not encountered [specific blind
  spot named in their subject card]. Weight this objection as a monitor-level risk, not a
  blocker, until verified by a GROUNDED source who has direct experience with the alternative."

Items from CONDITIONAL subjects must not be treated as equivalent to GROUNDED items
without naming the distinction. Synthesis that does not acknowledge epistemic standing
differences fails C-24.

GATE 3 → PHASE 4:
  [ ] Convergence or contradiction named with specific evidence item references
  [ ] Objection lifecycle includes a PERSISTED/TRANSFORMED/RESOLVED status label
      (or explicit N/A justification)
  [ ] At least one named epistemic weight adjustment present
  [ ] Synthesis does not treat CONDITIONAL and GROUNDED items as equivalently weighted
      without acknowledgment

---

================================================================================
PHASE 4 — SIMULATION FIDELITY NOTE
================================================================================

Brief meta-note addressing:

1. Grounded claim: name at least one claim based on documented persona knowledge or domain context
2. Constructed plausibility: name at least one claim extrapolated beyond direct evidence
3. Voice contrast: name one specific vocabulary term or framing choice that made two subjects
   sound genuinely different — a specific citation, not "they had different roles"

GATE 4 — ARTIFACT COMPLETENESS:
  [ ] Phase 0 subject cards complete with evidential function, experience-proximity,
      and 3 auditable vocabulary terms per subject
  [ ] Phase 1 expectation register complete; format template present and references
      the register by name and field in the "expected:" slot
  [ ] Phase 2 vocabulary audits show ≥1 confirmed term per subject
  [ ] Phase 2 moment labels reference Expectation Register by subject and field
  [ ] Phase 2 evidence tables have Experience-Proximity and Origin-of-Claim as
      separate populated columns (not collapsed)
  [ ] Phase 3 synthesis includes objection lifecycle with status label and epistemic
      weight adjustment
  [ ] Phase 4 fidelity note names grounded claim, constructed claim, and voice contrast

---

Artifact: {{topic}}-prove-interview-{{date}}.md
```

---

## V-04 — Combined: Skeptic-First × Investigative Reporter Register

**Combination**: Role sequence × Phrasing register
**Hypothesis**: An investigative reporter frames subjects as "sources" with declared credibility and
motivation — naturalizing the dual taxonomy as source-credibility hygiene rather than a structural
constraint. Reporter vocabulary ("source dossier", "on-the-record", "credibility basis") makes the
Origin-of-Claim dimension feel like standard verification practice, not a rubric annotation. Skeptic-
first ordering ensures the lead paragraph is built from the hardest objection — reporters build leads
on the hardest evidence they have. The C-25 bridge is enforced by a "prior model" register filed
before the first interview, because reporters always declare their angle before going into the field.

```
You are running a simulated interview investigation for the feature topic: {{topic}}.

This simulation uses an investigative reporter frame. You are a journalist assigned to
investigate a hypothesis. Your sources have documented knowledge and agendas. Your job:
gather evidence, weight it by source credibility, surface contradictions, and file a
verdict paragraph.

Reporter conventions:
- Subjects are sources with declared credibility and motivation
- Testimony is on-the-record, attributed, or background (affects Origin-of-Claim)
- Evidence items are findings with source credibility ratings
- The skeptic runs first — leads are built on the hardest evidence, not the softest
- The synthesis is the lead paragraph: one to two sentences, decision-ready

---

PREFLIGHT — Before Any Interview

SOURCE DOSSIERS (file all before entering the field)

File a dossier for each source before writing a single interview line.

  Source Dossier: [Name / Role]
  ├─ Beat / Expertise: [domain or operational area this source knows]
  ├─ Source Credibility: PRIMARY (direct operational experience with the specific
  │   thing being investigated) | SECONDARY (adjacent experience — has seen it from
  │   nearby, not directly) | BACKGROUND (evaluative, theoretical, or observational;
  │   no direct experience)
  ├─ Credibility Justification: [one sentence explaining why this source has this
  │   credibility level on this specific topic]
  ├─ Standing on This Story: [what structural role this source plays in the investigation —
  │   their evidential function, not just their disposition]
  ├─ What They Know: [documented knowledge relevant to the topic — 2-3 sentences]
  ├─ What They Don't Know: [blind spots — a separate field; what they haven't
  │   encountered that is relevant]
  ├─ Motivation: [why would they talk? What do they have to gain or lose?]
  └─ Vocabulary Signature (for quote verification — declared before interview):
       - Term 1: [a specific term this source uses in their domain]
       - Term 2: [a specific term]
       - Term 3: [a specific term]
       NOTE: At least one term must appear on-the-record in this source's interview.
       A term declared in the dossier that never appears in the transcript is an
       unverified contract — the vocabulary audit after each transcript will flag it.

Source credibility maps to evidence weighting:
  PRIMARY source on direct experience → GROUNDED evidence (highest weight)
  SECONDARY source on adjacent experience → CONDITIONAL (named blind spot limits weight)
  BACKGROUND source → weight requires corroboration before acting on

SEQUENCE PLANNING: Run sources in this order:
  1. The source with the hardest objection or most grounds for skepticism (runs first)
  2. The source with operational ground truth (runs second)
  3. The source with the strongest advocacy position (runs last)

  Sequence rationale (one sentence): Name why this specific ordering builds the
  strongest evidentiary foundation for the verdict.

---

PRIOR MODEL — File Before the Field

This is your declared angle. File it before any interview. It becomes the mandatory
source for all SURPRISING/CONFIRMING labels.

| Source        | Expected Position | Expected Objection | Expected Confirmation | What Would Surprise You |
|---------------|-------------------|--------------------|-----------------------|------------------------|
| [Skeptic]     |                   |                    |                       |                        |
| [Source 2]    |                   |                    |                       |                        |
| [Source 3]    |                   |                    |                       |                        |

Quote label format — embed this template and reference it for every labeled moment:

  SURPRISING  (expected: [Prior Model → Source: {name},
               Column: "Expected Position / Objection / Surprise"],
               got: [what the source actually said])

  CONFIRMING  (validates: [Prior Model → Source: {name},
               Column: "Expected Position / Confirmation"])

  INCONCLUSIVE (closest declared expectation: [Prior Model → Source: {name},
                Column: "{column}"],
                ambiguity: [what made it neither clearly surprising nor confirming])

A quote label whose "expected:" slot does not reference the Prior Model by source and
column was not grounded in your declared angle — you sourced the expectation from memory
after the fact. Fix the Prior Model entry first, then label.

PREFLIGHT GATE: All dossiers filed and Prior Model complete before going into the field.
  [ ] Every source has a declared credibility level with a justification sentence
  [ ] Every source has a Standing on This Story (evidential function, not just disposition)
  [ ] Every source has a Blind Spots field (separate from What They Know)
  [ ] Every source has 3 specific vocabulary terms declared
  [ ] Prior Model has all four columns filled for every source
  [ ] Sequence rationale stated

---

INTERVIEW 1: [Skeptic Source — Role] (PRIMARY / SECONDARY / BACKGROUND)

Reporter's note: This source has the hardest objections. Running them first puts their
testimony on record before any advocate speaks. The lead is built on the hardest evidence
available, not the softest.

Q: [Opening question anchored in this source's declared expertise and motivation]

[Source]: "[Answer in this source's distinct voice — on-the-record. At least one declared
vocabulary term must appear here or in a subsequent answer. Use quotation marks to mark
on-the-record testimony distinctly from background context.]"

Q (triggered by: "[exact phrase from the preceding answer]"): [follow-up]

[Source]: "[answer]"

[Continue 2-3 more exchanges. The skeptic's primary objection must be explicitly
on-the-record by the end of this interview — it is the objection whose fate is
tracked in the story lead.]

VOCABULARY VERIFICATION — Source 1:
  "[Term 1]": on-the-record in Q[N]/A[N] — "[phrase]"  |  NOT ON RECORD (open contract)
  "[Term 2]": on-the-record  |  NOT ON RECORD
  "[Term 3]": on-the-record  |  NOT ON RECORD

At least 1 of 3 terms must be on record. If none: add a natural exchange before continuing.

QUOTE LABEL — using Prior Model template:

  [SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Prior Model → Source: {skeptic name},
    Column: "{column}"], ...)

---

FINDINGS: Source 1

| # | Finding | Type | Source Credibility | Origin-of-Claim | Credibility Basis Sentence | Strength |
|---|---------|------|--------------------|-----------------|---------------------------|----------|
| 1 |         |      | GROUNDED /         | verbatim /      | [one sentence: what makes  | strong / |
|   |         |      | CONDITIONAL /      | inferred /      | this finding reliable,      | moderate /|
|   |         |      | INFERRED           | corroborated    | hedged, or speculative]    | weak     |

COLUMN DEFINITIONS:

  Source Credibility (maps from source dossier to finding weight):
    GROUNDED    — PRIMARY source testifying on direct experience of the specific claim
    CONDITIONAL — SECONDARY source OR a declared blind spot limits their standing;
                  name the limiting condition in the Credibility Basis Sentence
    INFERRED    — BACKGROUND source, or stance not directly stated; requires corroboration

  Origin-of-Claim (how was this finding derived from the transcript?):
    verbatim     — stated or closely paraphrased in the interview
    inferred     — implied by the answer, not explicitly said
    corroborated — same signal from 2+ sources [available from Interview 2 onward]

  These are orthogonal dimensions. A GROUNDED source can have an inferred finding.
  A CONDITIONAL source can have a verbatim finding. Do not use one column's tags
  to fill the other. If "GROUNDED" appears under Origin-of-Claim, the taxonomy
  has collapsed — fix it.

Source 1 gate before Interview 2:
  [ ] ≥1 vocabulary term on-the-record in Source 1's transcript
  [ ] Quote label references Prior Model by source and column name
  [ ] All findings have Source Credibility and Origin-of-Claim as separate columns
  [ ] No taxonomy collapse (credibility tags ≠ origin tags)

---

INTERVIEW 2: [Source 2 — Role] (PRIMARY / SECONDARY / BACKGROUND)

Reporter's note: [One sentence — what does this source's position add relative to Source 1?
What does their angle surface that the skeptic's testimony could not?]

[Same interview structure. At least one vocabulary term on-the-record. At least one
question probes whether this source's operational reality addresses or is silent about
the skeptic's primary objection.]

QUOTE LABEL — using Prior Model template:
  [SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Prior Model → Source: {Source 2
    name}, Column: "{column}"], ...)

FINDINGS: Source 2 [same table; "corroborated" available for Origin-of-Claim]

Source 2 gate: [same checklist]

---

INTERVIEW 3: [Source 3 — Role] (if present)

[Same structure. Reporter's note naming what this source's position adds.]

[Same vocabulary verification, quote label, findings table, and gate]

---

STORY LEAD — Cross-Source Synthesis

OBJECTION FATE
Name the skeptic's primary objection (from Interview 1, verbatim). Then:
- What did Source 2's testimony say about it (directly or by implication)?
- What did Source 3's testimony say about it?
- Final status: PERSISTED | TRANSFORMED | RESOLVED
  [one sentence: what evidence moved it to this status]

SOURCE CONVERGENCE
Where do sources agree despite different agendas? Name the specific findings.

SOURCE CONTRADICTION
Name at least one specific conflict — which sources, which findings, exactly what they
conflict on. Do not average contradictions away.

CREDIBILITY-WEIGHTED VERDICT
Apply source credibility to adjust synthesis weight on at least one finding:

  "Finding #[N] from [Source] is CONDITIONAL — [source] has not encountered [specific
  blind spot named in their dossier]. This objection carries monitor-level weight, not
  blocker weight, until verified by a PRIMARY source with direct experience."

Sources' findings are not equally weighted when their credibility levels differ.
Name the difference explicitly — synthesis that treats PRIMARY and BACKGROUND sources
as equivalent without acknowledgment has not closed the investigation.

---

LEAD PARAGRAPH (verdict)

One to two sentences. Decision-ready. The lead names:
1. Whether aggregate findings SUPPORT, CHALLENGE, CONTRADICT, or are INCONCLUSIVE
   about the feature direction
2. The strongest single testimony and its source credibility
3. Whether the skeptic's primary objection was neutralized, stands, or was transformed

A lead that does not address the skeptic's objection has not filed the story.

---

REPORTER'S NOTE (simulation fidelity)

On-the-record, attributable: name one claim grounded in documented source knowledge
Constructed for plausibility: name one claim extrapolated beyond evidence
Voice divergence: name one specific vocabulary term or framing choice that made two
  sources sound genuinely different — a specific citation, not "they had different agendas"

---

Artifact: {{topic}}-prove-interview-{{date}}.md
```

---

## V-05 — Combined: Inertia Profile + Table-Dominant + Full Phase Gates

**Combination**: Output format × Lifecycle emphasis × Inertia framing
**Hypothesis**: Naming the Inertia Profile as an artifact-level section before any subject is designed
creates a named reference point that tables can mechanically tag against. Combined with table-dominant
format (C-27 enforced by column separation) and phase gates (C-25/C-26/C-27 encoded as binary
preconditions), this variation produces the highest structural enforcement density: the three new
v7 criteria cannot be satisfied partially — the gates make partial compliance fail the same as
absence. The Inertia Profile also guarantees at least one INCUMBENT subject is designed, making
C-21 (objection lifecycle) available without additional instruction.

```
You are running a simulated stakeholder interview investigation for the feature topic: {{topic}}.

This simulation uses three compounding structural mechanisms:
  1. INERTIA PROFILE: a named artifact-level section declaring the ground state the
     feature would displace — established before any subject is designed
  2. TABLE-DOMINANT FORMAT: all pre-interview declarations and evidence extraction
     expressed in tables, enforcing dual taxonomy as non-collapsible columns
  3. EXPLICIT PHASE GATES: C-25, C-26, and C-27 encoded as binary preconditions;
     an output that cannot point to a passed gate has not completed the phase

All phases run in order. Do not skip ahead.

---

================================================================================
PHASE 0 — INERTIA PROFILE
================================================================================

Declare the current practice, tool, workflow, or established behavior that this feature
would displace, replace, or improve upon. Complete this table before designing any subject.

| Field                    | Value                                                     |
|--------------------------|-----------------------------------------------------------|
| Practice Name            | [specific name — not generic; "spreadsheet tracking"     |
|                          | fails; "manually maintained Excel tracker synced weekly   |
|                          | to SharePoint, owned by the ops team" passes]             |
| Current Users            | [who depends on it, in what operational context]          |
| Stickiness Factors       | [what makes this practice hard to leave: habit, trust,    |
|                          | integration, ownership, investment]                       |
| Known Limitations        | [friction or gaps that drive interest in alternatives]    |
| Switching Cost Estimate  | [what it would cost to move: workflow, learning,          |
|                          | migration, retraining]                                    |
| Displacement Target      | [what specifically the feature must replace or improve    |
|                          | to be considered successful]                              |

Every evidence item in this investigation carries an Inertia Relevance tag:
  INERTIA  — measures switching cost, friction, or resistance relative to this profile
  ADOPTION — measures openness, fit, or pull toward the new direction
  NEUTRAL  — neither directly measures inertia or adoption

GATE 0: Do not proceed to Phase 1 until the Inertia Profile table has no empty cells.

---

================================================================================
PHASE 1 — SUBJECT REGISTRY
================================================================================

Complete all subject tables before writing any transcript.

TABLE 1A — SUBJECT PROFILES

| Field                    | Subject 1        | Subject 2        | Subject 3        |
|--------------------------|------------------|------------------|------------------|
| Role / Title             |                  |                  |                  |
| Evidential Function      | [structural       | [structural       | [structural       |
|                          | contribution to   | contribution]     | contribution]     |
|                          | evidence chain,   |                  |                  |
|                          | not just disposition]|               |                  |
| Experience-Proximity     | GROUNDED /        | GROUNDED /        | GROUNDED /        |
|                          | CONDITIONAL /     | CONDITIONAL /     | CONDITIONAL /     |
|                          | INFERRED          | INFERRED          | INFERRED          |
| Proximity Justification  | [one sentence]    |                  |                  |
| Prior Knowledge          |                  |                  |                  |
| Blind Spots              | [separate field — |                  |                  |
|                          | what they haven't |                  |                  |
|                          | seen]             |                  |                  |
| Disposition              |                  |                  |                  |
| Inertia Relationship     | INCUMBENT /       | INCUMBENT /       | INCUMBENT /       |
|                          | FRICTION-HOLDER / | FRICTION-HOLDER / | FRICTION-HOLDER / |
|                          | EVALUATOR /       | EVALUATOR /       | EVALUATOR /       |
|                          | ADVOCATE          | ADVOCATE          | ADVOCATE          |
| Primary Concern          |                  |                  |                  |

Inertia Relationship definitions:
  INCUMBENT       — currently uses or owns the practice declared in the Inertia Profile
  FRICTION-HOLDER — has experienced the Profile's known limitations directly
  EVALUATOR       — assesses options against organizational criteria, no deep investment
  ADVOCATE        — positioned to benefit from the feature direction succeeding

---

TABLE 1B — VOCABULARY SIGNATURE REGISTRY

| Subject    | Vocab Term 1 | Vocab Term 2 | Vocab Term 3 |
|------------|-------------|-------------|-------------|
| [S1]       |             |             |             |
| [S2]       |             |             |             |
| [S3]       |             |             |             |

Terms must be auditable — general traits ("domain expert") fail; specific terms
("schema migration", "rollback window") pass. At least one term per subject must
appear naturally in that subject's transcript (verified at Phase 2 gate).

---

TABLE 1C — SEQUENCE JUSTIFICATION

| Position | Subject   | Rationale                                                      |
|----------|-----------|----------------------------------------------------------------|
| First    |           | [what this subject surfaces by running first]                  |
| Second   |           | [what their position adds relative to the first]               |
| Third    |           | [what they resolve, confirm, or challenge — optional if N=2]   |

GATE 1: Do not proceed to Phase 2 until:
  [ ] Table 1A fully populated — no blank cells in required rows
  [ ] Table 1A has Evidential Function (not just disposition) for every subject
  [ ] Table 1A has Blind Spots as a separate field (not implied by Prior Knowledge)
  [ ] Table 1B has 3 specific, auditable vocabulary terms per subject
  [ ] Table 1C has sequence rationale for all subjects
  [ ] At least one subject carries Inertia Relationship = INCUMBENT

---

================================================================================
PHASE 2 — EXPECTATION REGISTER
================================================================================

Complete before any transcript.

| Subject    | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|------------|-------------------|--------------------|-----------------------|-------------------|
| [S1]       |                   |                    |                       |                   |
| [S2]       |                   |                    |                       |                   |
| [S3]       |                   |                    |                       |                   |

The Expected Surprise column is mandatory. Leaving it blank means no prior model
edge was declared — fill it.

FORMAT TEMPLATE — this template is the mandatory form for all moment labels in
Phases 3 through 5. Declare it here; the "expected:" slot must reference this
register by subject row and field name:

  SURPRISING  (expected: [Expectation Register → Subject: {name},
               Field: "{Expected Position / Objection / Surprise}"],
               got: [what emerged in the transcript])

  CONFIRMING  (validates: [Expectation Register → Subject: {name},
               Field: "{Expected Position / Confirmation}"])

  INCONCLUSIVE (closest match: [Expectation Register → Subject: {name},
                Field: "{field}"],
                ambiguity: [what made this moment fit neither category cleanly])

A moment label that authors the expectation inline — without pointing to a
pre-populated register cell — fails C-25. If a label cannot point to a cell
in this table, fix the register first.

GATE 2: Do not begin any interview until:
  [ ] All subject rows complete — no empty columns
  [ ] Expected Surprise populated for every subject
  [ ] Format template is present in this document
  [ ] Format template names the Expectation Register as the source for "expected:",
      using subject-and-field reference syntax

---

================================================================================
PHASE 3 — INTERVIEW TRANSCRIPTS (one subject at a time)
================================================================================

For each subject, complete transcript + all Phase 3 tables before moving to the next.

TRANSCRIPT: [Subject Role] ([Disposition]) — [Inertia Relationship]

Opening question: [anchored in this subject's declared prior knowledge]

[Subject]: [answer in this subject's distinct voice]

Follow-up (triggered by: "[exact phrase from preceding answer]"): [question]

[Subject]: [answer]

[Continue 2-4 exchanges. At least one exchange must probe this subject's Primary Concern.
For INCUMBENT subjects: at least one exchange must anchor in the Inertia Profile — their
specific relationship to the declared practice, not the feature direction.]

---

TABLE 3A — VOCABULARY AUDIT: [Subject]

| Declared Term | Status                            | Transcript Evidence                      |
|---------------|-----------------------------------|------------------------------------------|
| "[Term 1]"    | FOUND in A[N] / NOT FOUND         | "[brief quote, or blank if not found]"   |
| "[Term 2]"    | FOUND / NOT FOUND                 |                                          |
| "[Term 3]"    | FOUND / NOT FOUND                 |                                          |

Minimum 1 of 3 must be FOUND. If none: add a natural exchange that elicits a declared
term, update this table, then proceed to Table 3B.

---

TABLE 3B — MOMENT LABEL: [Subject]

Using the Phase 2 format template:

  [SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Expectation Register →
    Subject: {name}, Field: "{field}"], ...)

---

TABLE 3C — EVIDENCE EXTRACTION: [Subject]

| # | Evidence Item | Signal Type   | Inertia Rel. | Experience-Proximity   | Proximity Note         | Origin-of-Claim          | Strength  | Rationale         |
|---|---------------|---------------|--------------|------------------------|------------------------|--------------------------|-----------|-------------------|
| 1 |               |               | INERTIA /    | GROUNDED /             | [if CONDITIONAL:       | verbatim /               | strong /  | [one sentence:    |
|   |               |               | ADOPTION /   | CONDITIONAL /          | name blind spot]       | inferred /               | moderate /| why this rating?] |
|   |               |               | NEUTRAL      | INFERRED               |                        | corroborated             | weak      |                   |
| 2 |               |               |              |                        |                        |                          |           |                   |

COLUMN DEFINITIONS — enforce all four independently:

  Inertia Relevance: does this item measure cost-to-change relative to the Inertia Profile
    (INERTIA), pull toward the new direction (ADOPTION), or neither (NEUTRAL)?

  Experience-Proximity: how close is this subject to direct operational experience of
    this specific claim?
    GROUNDED    — has experienced this specific situation firsthand
    CONDITIONAL — a declared blind spot limits their standing; name it in Proximity Note
    INFERRED    — subject's stance on this was not directly stated

  Origin-of-Claim: how was this claim derived from the transcript?
    verbatim     — stated or closely paraphrased in the transcript
    inferred     — implied by the answer, not explicitly said
    corroborated — consistent signal from 2+ subjects [available from Subject 2 onward]

  ORTHOGONALITY CONTRACT: Experience-Proximity and Origin-of-Claim are independent
  dimensions. A GROUNDED subject can produce inferred evidence. A CONDITIONAL subject
  can produce verbatim evidence. Do not use one dimension's tags to fill the other's
  column. Taxonomy collapse failures:
    — "GROUNDED" or "CONDITIONAL" appearing in Origin-of-Claim column
    — "verbatim" or "inferred" appearing in Experience-Proximity column
  Fix any such rows before proceeding.

---

GATE 3 (run after each interview, before the next):
  [ ] Table 3A shows ≥1 FOUND vocabulary term for this subject
  [ ] Table 3B moment label references Expectation Register by subject and field name
  [ ] All Table 3C rows have Inertia Relevance, Experience-Proximity, and
      Origin-of-Claim populated
  [ ] No taxonomy collapse: Experience-Proximity column contains only
      GROUNDED/CONDITIONAL/INFERRED; Origin-of-Claim column contains only
      verbatim/inferred/corroborated
  [ ] INCUMBENT subjects' transcripts include ≥1 exchange anchored in the Inertia Profile

Repeat Phase 3 for each remaining subject. Run Gate 3 after each before starting the next.

---

================================================================================
PHASE 4 — SYNTHESIS TABLES
================================================================================

TABLE 4A — INERTIA/ADOPTION PARTITION

Compile all items from all Table 3C instances and partition them:

| Category | Evidence Item | Subject    | Strength  | Inertia Profile Mapping                    |
|----------|---------------|------------|-----------|-------------------------------------------|
| INERTIA  |               |            |           | [maps to: Stickiness Factor / Switching   |
|          |               |            |           | Cost from Profile table]                  |
| INERTIA  |               |            |           |                                           |
| ADOPTION |               |            |           | [maps to: Known Limitation / Displacement |
|          |               |            |           | Target from Profile table]                |
| ADOPTION |               |            |           |                                           |
| NEUTRAL  |               |            |           |                                           |

ADOPTION DELTA (one sentence below table): What does aggregate adoption evidence say
relative to aggregate inertia evidence? Is the inertia load dominant, balanced, or marginal?

---

TABLE 4B — SYNTHESIS FINDINGS

| Dimension                                              | Finding                                   |
|--------------------------------------------------------|-------------------------------------------|
| Convergence (where subjects agree)                     |                                           |
| Primary contradiction (named subjects + items)         |                                           |
| Objection lifecycle: initial objection                 | [subject, phrased as stated in transcript]|
| Objection lifecycle: intermediate response             | [next subject's response or silence]       |
| Objection lifecycle: final status                      | PERSISTED / TRANSFORMED / RESOLVED        |
| Epistemic weight adjustment (named item + rationale)   | [item, blind spot, treatment]             |
| Displacement verdict: is switching cost fatal,         |                                           |
| solvable, or neutralized by adoption evidence?         |                                           |

Epistemic weight adjustment format:
  "Item [N] from [Subject] is CONDITIONAL — [subject] has not experienced [blind spot
  named in their Table 1A card]. Treat this as a risk to monitor, not a blocker, until
  verified by a GROUNDED source with direct experience of the alternative."

GATE 4:
  [ ] Table 4A has ≥1 item under INERTIA and ≥1 under ADOPTION (or explicit statement
      of why a category is empty)
  [ ] Adoption delta is stated (one sentence minimum)
  [ ] Table 4B objection lifecycle row has PERSISTED/TRANSFORMED/RESOLVED status label
  [ ] Table 4B has a named epistemic weight adjustment with rationale
  [ ] Table 4B displacement verdict addresses the Inertia Profile directly

---

================================================================================
PHASE 5 — SIMULATION FIDELITY NOTE
================================================================================

| Type                        | Item                                                         |
|-----------------------------|--------------------------------------------------------------|
| Grounded claim              | [one claim based on documented persona knowledge or domain   |
|                             | context — name the source]                                   |
| Constructed plausibility    | [one claim extrapolated beyond direct evidence — name why    |
|                             | it was constructed, not grounded]                            |
| Voice contrast              | [one specific vocabulary term or framing choice that made    |
|                             | two subjects sound genuinely different — specific citation,  |
|                             | not "they had different roles"]                              |
| Taxonomy verification       | [confirm that Experience-Proximity and Origin-of-Claim were  |
|                             | applied as separate dimensions in all Table 3C instances;    |
|                             | note any row where the distinction was closest to collapsing]|

FINAL GATE:
  [ ] All four rows in Phase 5 table are populated
  [ ] Taxonomy verification row confirms separation, not just asserts it

---

Artifact: {{topic}}-prove-interview-{{date}}.md
```
