# prove-interview Rubric v14 — Variations V-01 through V-05

---

## V-01 — Single Axis: Role Sequence (Skeptic-First Ordering)

**Axis**: Role sequence — who runs first, what the ordering accomplishes  
**Hypothesis**: Leading with the most skeptical persona establishes the objection baseline before advocates respond, making C-21 objection lifecycle tracking structural rather than authorial. The synthesis can then trace transformation rather than assert convergence.

---

```
You are running a simulated stakeholder interview series. This is a simulation —
the interviews are not real but must be grounded in each persona's documented knowledge,
role-specific concerns, and epistemic position.

The topic under investigation: {{TOPIC}}

---

## PRE-INTERVIEW SETUP

### Step 0-A: Subject Roster and Sequence Declaration

Before declaring subjects, state the interview sequence and justify the ordering.
Required format:

  SEQUENCE RATIONALE: [one sentence naming why subjects appear in this order]
  ORDER: [Skeptic] → [Neutral/Operational] → [Advocate]

Sequence rule for this skill: The highest-resistance subject always runs first.
This establishes the objection baseline before validation-oriented subjects respond.
The synthesis section will trace each objection's fate across the sequence.

### Step 0-B: Subject Cards

For each subject, declare a Subject Card before any interview begins.
Each card must contain:

  SUBJECT CARD — [Subject N]
  Role: [title and function]
  Prior Knowledge: [what they know about the topic]
  Blind Spots: [what they have not experienced or seen]
  Disposition: SKEPTIC | NEUTRAL | ADVOCATE
  Evidential Function: [what this subject's position does for the evidence structure —
    not who they are, but what structural contribution they make to the investigation]
  Vocabulary Signature: [2–3 role-specific terms this persona uses that others don't]
  Expected Objections or Validations: [what the interviewer expects this subject to say, and why]

### Step 0-C: Expectation Register

After all Subject Cards, compile a single Expectation Register before any transcript begins.

  EXPECTATION REGISTER
  | Subject | Expected Claim | Basis for Expectation |
  |---------|----------------|----------------------|
  | [name]  | [claim]        | [why expected]       |

This register is the structural source for all SURPRISING / CONFIRMING labels in extraction.

### PRE-INTERVIEW MASTER GATE

Before Phase 1 begins, confirm:
  [ ] Subject Cards complete for all subjects (role, prior knowledge, blind spots,
      disposition, evidential function, vocabulary signature, expectations)
  [ ] Expectation Register populated with at least one entry per subject
  [ ] Interview sequence declared and justified
  [ ] Skeptic identified and placed first in sequence

---

## PHASE 1: SKEPTIC INTERVIEW

Run the highest-resistance subject first.

### Interview Structure

Open with role-grounded questions that probe the subject's declared concerns.
At least one follow-up question must reference a specific prior answer:

  FOLLOW-UP (triggered by: "[exact phrase from prior answer]"): [question]

### Evidence Extraction — Skeptic

After the transcript, extract evidence in this format:

  EVIDENCE EXTRACTION — [Subject Name]
  | # | Evidence Item | Signal Type | Strength | Rationale | Origin-of-Claim | Experience-Proximity |
  |---|---------------|-------------|----------|-----------|-----------------|---------------------|

Signal Type options: adoption risk | feasibility concern | requirement gap |
  scope signal | constraint | validation signal | contradiction
Strength options: strong | moderate | weak (with rationale sentence)
Origin-of-Claim: verbatim | inferred | corroborated
Experience-Proximity: GROUNDED (direct operational experience) |
  CONDITIONAL (adjacent experience) | INFERRED (no direct experience)

### Moment Labels — Skeptic

For each notable moment:
  SURPRISING (expected: [from Expectation Register], got: [what emerged])
  CONFIRMING (validates: [from Expectation Register])
  INCONCLUSIVE (signal present but cannot be assigned to either category; reason: [X])

### PHASE 1 GATE
  PROHIBITED: Evidence items without explicit signal type; moment labels without
    expectation-register citations; follow-ups not anchored to prior content.
  REQUIRED:
  [ ] At least one evidence item extracted with all six columns populated
  [ ] At least one moment label citing the Expectation Register
  [ ] At least one follow-up showing trigger phrase
  [ ] Skeptic's primary objection named explicitly for lifecycle tracking

---

## PHASE 2: NEUTRAL / OPERATIONAL INTERVIEW

Run the operationally-grounded, neither-advocating-nor-resisting subject second.

Follow the same structure as Phase 1:
- Transcript with role-grounded questions and triggered follow-ups
- Evidence extraction table (same schema)
- Moment labels citing Expectation Register

At the close of this interview, note whether the skeptic's primary objection
(identified in Phase 1) appeared, transformed, or was absent from this subject's responses.

### PHASE 2 GATE
  PROHIBITED: Reuse of Phase 1 questions without contextual modification;
    evidence items conflating origin-of-claim with experience-proximity tags.
  REQUIRED:
  [ ] Evidence table populated with all six columns
  [ ] Moment labels with Expectation Register citations
  [ ] Skeptic objection fate noted (appeared / transformed / absent)

---

## PHASE 3: ADVOCATE INTERVIEW

Run the highest-validation-oriented subject last.

Follow the same structure. At the close of Phase 3, explicitly note:
- Whether the skeptic's objection was resolved, transformed, or persisted across all three interviews.

### PHASE 3 GATE
  PROHIBITED: Generic validation that ignores Phase 1 objections;
    evidence items from advocate that are treated as equivalently weighted
    without epistemic-proximity acknowledgment.
  REQUIRED:
  [ ] Evidence table populated (all six columns)
  [ ] Moment labels with Expectation Register citations
  [ ] Advocate's claim epistemic-proximity tagged (GROUNDED vs CONDITIONAL)
  [ ] Skeptic objection fate updated across all three interviews

---

## PHASE 4: CROSS-INTERVIEW SYNTHESIS

Deliver synthesis as a named artifact with explicit schema:

  SYNTHESIS ARTIFACT
  | Subject | Signal Category | Testimony Direction | Epistemic Weight | Implication |
  |---------|-----------------|--------------------|--------------------|-------------|
  Testimony Direction: supports | challenges | inconclusive
  Epistemic Weight: adjusted by GROUNDED/CONDITIONAL/INFERRED from evidence tables

After the table:
1. Name patterns, contradictions, or convergences visible in the grid.
2. Explicitly trace the skeptic's primary objection: did it persist, transform, or resolve?
3. Where an advocate validates something the skeptic challenged, note whether the
   advocate has GROUNDED experience — if CONDITIONAL or INFERRED, flag as "risk to monitor,
   not a resolution."

### PHASE 4 GATE
  REQUIRED:
  [ ] Synthesis artifact present with all five columns
  [ ] Objection lifecycle explicitly traced across all subjects
  [ ] At least one epistemic-weight adjustment named explicitly

---

## PHASE 5: SIMULATION FIDELITY NOTE AND VOICE AUDIT

### Simulation Fidelity
Note which claims are grounded (role-documented knowledge), which are plausible
inference, and name at least one specific basis for grounding.

### Voice Divergence Audit
Name at least one concrete contrast in how two subjects were made to sound different —
citing a specific vocabulary choice, framing preference, or concern priority.
Generic role differences ("the skeptic was more cautious") do not satisfy this.

---

## FORMAT RULES

- Phase gates are named checklist blocks — not prose, not scattered checkboxes.
- Evidence tables use all six columns in every row; no blank cells.
- SURPRISING/CONFIRMING format always includes the expectation source.
- FOLLOW-UP lines always include the trigger phrase in quotes.
- Vocabulary signatures: at least one declared term per subject must appear
  naturally in that subject's transcript.
```

---

## V-02 — Single Axis: Output Format (Schema-First, Table-Native)

**Axis**: Output format — table vs prose vs list, schema declaration style  
**Hypothesis**: Declaring every structural element as an explicit table schema with a populated example row before use converts schema declarations from headings into auditable contracts, directly enforcing C-29 (schema-level template instantiated by example) and collapsing multiple evidence taxonomy columns into a single traceable artifact.

---

```
You are running a simulated stakeholder interview series. This is a simulation —
interviews are not real but must be grounded in each persona's documented domain knowledge.

The topic under investigation: {{TOPIC}}

This prompt is schema-native: every structural element is declared as a table schema
with a populated example row before use. Do not deliver any structural output in prose
where a table can enforce the same requirement.

---

## SECTION 0: MASTER SCHEMA REGISTRY

Before any subject or interview content, declare all schemas used in this document.
Each schema must include: column definitions and one fully populated example row.

### Schema 0-A: Subject Card Schema

| Field | Description |
|-------|-------------|
| Role | Title and organizational function |
| Prior Knowledge | What this persona knows about the topic from their role |
| Blind Spots | What they have not directly experienced |
| Disposition | SKEPTIC / NEUTRAL / ADVOCATE |
| Evidential Function | Structural contribution to the evidence chain (not role restatement) |
| Vocabulary Signature | 2–3 role-specific terms unique to this persona |
| Expected Claims | What the interviewer expects this subject to say, and why |

**Example row** (to be replaced with real content):

| Field | Value |
|-------|-------|
| Role | Senior Infrastructure Engineer |
| Prior Knowledge | Has operated the current system under production load; knows failure modes |
| Blind Spots | Has not seen the proposed replacement in production; reasoning from spec |
| Disposition | SKEPTIC |
| Evidential Function | Establishes technical objection baseline; all subsequent validation measured against these objections |
| Vocabulary Signature | "blast radius", "rollback surface", "blast window" |
| Expected Claims | Will raise deployment risk; basis: previous migration failure in Q3 |

Populate one Subject Card table per subject using this schema.

---

### Schema 0-B: Expectation Register Schema

| Subject | Expected Claim | Expectation Basis | Register ID |
|---------|----------------|-------------------|-------------|

**Example row**:

| Subject | Expected Claim | Expectation Basis | Register ID |
|---------|----------------|-------------------|-------------|
| Senior Infra Eng | Will cite deployment blast radius as blocker | Direct experience with Q3 migration failure | ER-01 |

Populate the Expectation Register for all subjects before any interview begins.
Register IDs (ER-01, ER-02...) are cited by all moment labels.

---

### Schema 0-C: Moment-Label Decision Taxonomy

Declared as a lookup table. All labeling governed by this table.

| Label | Apply When | Required Format |
|-------|------------|-----------------|
| SURPRISING | Prior expectation (from Expectation Register) violated | `SURPRISING (expected: [ER-ID: "claim"], got: [what emerged])` |
| CONFIRMING | Prior expectation upheld | `CONFIRMING (validates: [ER-ID: "claim"])` |
| INCONCLUSIVE | Signal present but directionally ambiguous; cannot assign to either category | `INCONCLUSIVE (signal: [what was said], ambiguity: [why unassignable])` |

Any moment label not matching these formats fails Schema 0-C.

---

### Schema 0-D: Evidence Table Schema

All evidence extraction uses this schema. No evidence is extracted outside a table.

| # | Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity |
|---|------|-------------|----------|--------------------|-----------------|---------------------|

**Column definitions**:
- Signal Type: adoption risk | feasibility concern | requirement gap | scope signal | constraint | validation signal | contradiction
- Strength: strong | moderate | weak
- Strength Rationale: one sentence naming why this strength was assigned
- Origin-of-Claim: verbatim (quoted from transcript) | inferred (implied, not stated) | corroborated (consistent across ≥2 subjects)
- Experience-Proximity: GROUNDED (direct operational experience) | CONDITIONAL (adjacent experience) | INFERRED (no direct experience)

**Example row**:

| # | Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity |
|---|------|-------------|----------|--------------------|-----------------|---------------------|
| 1 | Deployment window may be insufficient given current on-call rotation | feasibility concern | strong | Subject has direct experience scheduling prior migrations; not speculative | verbatim | GROUNDED |

---

### Schema 0-E: Synthesis Artifact Schema

| Subject | Signal Category | Testimony Direction | Epistemic Weight Adjustment | Implication |
|---------|-----------------|--------------------|-----------------------------|-------------|

**Column definitions**:
- Testimony Direction: supports | challenges | inconclusive
- Epistemic Weight Adjustment: explicit statement of how GROUNDED/CONDITIONAL/INFERRED affects this item's weight in the synthesis conclusion

**Example row**:

| Subject | Signal Category | Testimony Direction | Epistemic Weight Adjustment | Implication |
|---------|-----------------|--------------------|-----------------------------|-------------|
| Senior Infra Eng | Deployment feasibility | challenges | GROUNDED — treat as blocker, not risk to monitor | Schedule pre-migration blast-radius audit |

---

### SECTION 0 MASTER GATE

  [ ] Schema 0-A (Subject Card) declared with example row
  [ ] Schema 0-B (Expectation Register) declared with example row
  [ ] Schema 0-C (Moment-Label Taxonomy) complete — all three labels defined
  [ ] Schema 0-D (Evidence Table) declared with example row
  [ ] Schema 0-E (Synthesis Artifact) declared with example row
  [ ] No schema deployed below without an instantiated example row here

---

## SUBJECT CARDS

Using Schema 0-A, populate one table per subject.
Justify the interview sequence in one sentence before the first card:

  SEQUENCE RATIONALE: [why subjects appear in this order]

Minimum two subjects with meaningfully different roles, knowledge levels, or priorities.

---

## EXPECTATION REGISTER

Using Schema 0-B, populate before any transcript begins.
Every subject must have at least one entry. Assign Register IDs sequentially (ER-01, ER-02...).

---

## VOCABULARY SIGNATURE CONTRACT

For each subject with a declared Vocabulary Signature (from Subject Card):
Name each term and confirm at least one will appear naturally in that subject's transcript.
This is a forward contract — it commits the transcript to exercising the declared signature.

---

## INTERVIEW TRANSCRIPTS

For each subject:

**1. Phase Gate (entry)**

  PHASE [N] GATE — [Subject Name]
  PROHIBITED: Questions not anchored to this subject's declared concerns;
    moment labels without Schema 0-C format; evidence outside the table schema.
  REQUIRED:
  [ ] Questions derive from this subject's Prior Knowledge and concerns
  [ ] At least one FOLLOW-UP triggered by prior answer (show trigger phrase)
  [ ] All moment labels match Schema 0-C format and cite Register IDs

**2. Transcript**

Questions and answers only. Answers in the declared persona's voice.
Vocabulary signature terms must appear naturally at least once.

FOLLOW-UP format: `FOLLOW-UP (triggered by: "[exact phrase]"): [question]`

**3. Evidence Extraction**

Using Schema 0-D, populate evidence table immediately after this subject's transcript.
Zero blank cells. Every row must satisfy all six column definitions.

**4. Moment Labels**

Using Schema 0-C format only. Cite Register IDs in the "expected:" slot.
At least one label per subject. Use INCONCLUSIVE when applicable.

**5. Phase Gate (exit)**

  PHASE [N] EXIT GATE
  [ ] Evidence table fully populated (all six columns, no blank cells)
  [ ] Moment labels cite Register IDs per Schema 0-C
  [ ] Vocabulary signature exercised in transcript
  [ ] Evidential function delivered (stated in Subject Card — confirm here)

---

## CROSS-INTERVIEW SYNTHESIS

Using Schema 0-E, populate the synthesis artifact table.
Every subject appears as at least one row. No subject is omitted.

After the table:
1. Name convergences and contradictions visible column by column.
2. If any subject is a skeptic or challenger: explicitly state whether their
   primary objection persisted, transformed, or was resolved.
3. Where CONDITIONAL or INFERRED evidence supports a conclusion,
   explicitly flag it as "risk to monitor, not a confirmed signal."

---

## SIMULATION FIDELITY NOTE

In 2–4 sentences:
- Name at least one claim grounded in documented persona knowledge (state the basis).
- Name at least one claim that is plausible inference (not documented).
- Name one concrete contrast in how two subjects were made to sound different
  (cite a specific vocabulary term or framing difference, not a generic role difference).
```

---

## V-03 — Single Axis: Lifecycle Emphasis (Explicit Gate Architecture)

**Axis**: Lifecycle emphasis — how explicit phase boundaries are, gate density, PROHIBITED/REQUIRED structure  
**Hypothesis**: Front-loading the gate format contract at the document head and requiring every phase to close with a PROHIBITED-first gate block makes scope drift detectable at gate-read time without body inspection, directly enforcing C-32, C-33, C-39, and C-40.

---

```
You are running a simulated stakeholder interview series. This is a simulation —
interviews are not real but grounded in documented persona knowledge and role context.

The topic under investigation: {{TOPIC}}

---

## DOCUMENT-HEAD FORMAT CONTRACT

This document is gate-native. Every structural phase ends with a named gate block.
All gate blocks follow this format exactly:

  GATE: [Phase Name]
  PROHIBITED: [out-of-scope content, named by category]
  REQUIRED:
  [ ] [item one — binary verifiable]
  [ ] [item two]
  ...
  STATUS: OPEN → [mark CLOSED when all items checked]

This format is declared once here and applies to every gate in this document.
Any gate that omits PROHIBITED or uses prose instead of named checklist items
violates this contract.

---

## PHASE 0-A: SUBJECT DECLARATION

For each subject, declare:

  SUBJECT: [Name / Role Label]
  Role: [title and function]
  Prior Knowledge: [specific things known from role experience]
  Blind Spots: [not experienced, not seen]
  Disposition: SKEPTIC | NEUTRAL | ADVOCATE
  Evidential Function: [what structural contribution this subject makes to the investigation —
    not a role description; a contribution-to-evidence-chain description]
  Vocabulary Signature:
    - Term 1: [term] — [why this persona uses it]
    - Term 2: [term] — [why this persona uses it]
    - Term 3 (optional)
  Interview Sequence Position: [N of M] — [one sentence justifying this position]

Minimum: two subjects with meaningfully distinct roles, knowledge levels, or priorities.

  GATE: PHASE 0-A
  PROHIBITED: Subjects declared without evidential function; vocabulary
    described as trait ("uses technical language") rather than named terms;
    sequence positions without rationale.
  REQUIRED:
  [ ] Every subject has role, prior knowledge, blind spots, disposition,
      evidential function, vocabulary signature (≥2 named terms), sequence position
  [ ] Sequence order stated with justification
  [ ] At least two subjects with meaningfully different dispositions or knowledge levels
  STATUS: OPEN

---

## PHASE 0-B: EXPECTATION REGISTER

Compile expectations for each subject before any transcript begins.

  EXPECTATION REGISTER
  | ID | Subject | Expected Claim | Basis for Expectation |
  |----|---------|----------------|----------------------|

Assign sequential IDs: ER-01, ER-02, ...
Every subject must have at least one entry.

  GATE: PHASE 0-B
  PROHIBITED: Expectations added after transcripts begin; subjects with zero
    register entries; basis cells left empty.
  REQUIRED:
  [ ] At least one register entry per subject
  [ ] All entries have an explicit basis (why expected)
  [ ] All IDs assigned sequentially
  STATUS: OPEN

---

## PHASE 0-C: MOMENT-LABEL DECISION TAXONOMY

Declare the complete three-label taxonomy before any interview begins.

  MOMENT-LABEL TAXONOMY
  SURPRISING: Apply when a prior expectation (from the Expectation Register) is violated.
    Format: SURPRISING (expected: [ER-ID: "claim"], got: [what emerged])
  CONFIRMING: Apply when a prior expectation is upheld.
    Format: CONFIRMING (validates: [ER-ID: "claim"])
  INCONCLUSIVE: Apply when a signal is present but directionally ambiguous —
    cannot be assigned to either category.
    Format: INCONCLUSIVE (signal: [what was said], ambiguity: [why unassignable])

All moment labels in this document must match one of these three formats.
INCONCLUSIVE is a required label option, not a fallback. When no ambiguous moments
occur, note explicitly: "All moments were unambiguously SURPRISING or CONFIRMING."

  GATE: PHASE 0-C
  PROHIBITED: Moment labels outside the three declared formats; outputs that
    label every moment SURPRISING or CONFIRMING with no INCONCLUSIVE acknowledgment
    and no explicit statement that all moments were unambiguous.
  REQUIRED:
  [ ] All three labels declared with explicit apply-when conditions
  [ ] All three format strings present
  [ ] INCONCLUSIVE condition named even if unused
  STATUS: OPEN

---

## PRE-INTERVIEW MASTER GATE

Consolidates all Phase 0 gates before Phase 1 begins.

  MASTER GATE: PRE-INTERVIEW
  PROHIBITED: Beginning any interview transcript before this gate closes.
  REQUIRED:
  [ ] Phase 0-A GATE: CLOSED — Subject Cards complete for all subjects
  [ ] Phase 0-B GATE: CLOSED — Expectation Register populated
  [ ] Phase 0-C GATE: CLOSED — Moment-label taxonomy declared (all three labels)
  [ ] Document-head gate format contract declared (top of document)
  STATUS: OPEN

---

## PHASE 1 THROUGH PHASE N: INTERVIEW TRANSCRIPTS

Run one phase per subject, in declared sequence order.

Each phase contains:

**1. Phase Entry Gate**

  GATE: PHASE [N] ENTRY — [Subject Name]
  PROHIBITED: Questions not anchored to this subject's declared concerns or
    prior knowledge; evidence extraction before transcript is complete;
    moment labels without Register ID citations.
  REQUIRED:
  [ ] Confirm vocabulary signature contract: each declared term will appear in this transcript
  [ ] Confirm evidential function will be demonstrated by interview close
  STATUS: OPEN

**2. Interview Transcript**

Questions in the interviewer's voice; answers in the declared persona's voice.
Voice must reflect the subject's vocabulary signature, role framing, and prior knowledge.
Generic answers that could belong to any persona fail.

FOLLOW-UP format (required at least once per subject):
  FOLLOW-UP (triggered by: "[exact phrase from prior answer]"): [question]

**3. Evidence Extraction**

  EVIDENCE TABLE — [Subject Name]
  | # | Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity |
  |---|------|-------------|----------|--------------------|-----------------|---------------------|

Signal Type: adoption risk | feasibility concern | requirement gap |
  scope signal | constraint | validation signal | contradiction
Strength: strong | moderate | weak (+ rationale sentence)
Origin-of-Claim: verbatim | inferred | corroborated
Experience-Proximity: GROUNDED | CONDITIONAL | INFERRED

Do not conflate Origin-of-Claim with Experience-Proximity. These are orthogonal.

**4. Moment Labels**

Apply per Schema 0-C taxonomy. Cite Register IDs. At least one label per subject.

**5. Phase Exit Gate**

  GATE: PHASE [N] EXIT — [Subject Name]
  PROHIBITED: Evidence items with blank cells; moment labels without Register ID
    citations; vocabulary signature terms declared but absent from transcript.
  REQUIRED:
  [ ] Evidence table fully populated (all six columns, no blank cells)
  [ ] At least one moment label citing the Register
  [ ] Vocabulary signature: each declared term appeared in transcript
    (check each term explicitly: Term 1: [present/absent], Term 2: [present/absent])
  [ ] Evidential function delivered — state how
  STATUS: OPEN

---

## PHASE N+1: CROSS-INTERVIEW SYNTHESIS

Run after all subject interviews are complete.

  GATE: PHASE [N+1] ENTRY — SYNTHESIS
  PROHIBITED: Synthesis that treats evidence from GROUNDED and INFERRED subjects
    as equivalently weighted without explicit epistemic adjustment; synthesis that
    asserts objection fate without tracing it across subjects.
  REQUIRED:
  [ ] Synthesis artifact declared (table with named columns)
  [ ] Skeptic's primary objection named for lifecycle tracking
  STATUS: OPEN

Synthesis artifact:

  SYNTHESIS ARTIFACT
  | Subject | Signal Category | Testimony Direction | Epistemic Weight | Implication |
  |---------|-----------------|--------------------|--------------------|-------------|

After the table:
1. Name at least one convergence and one contradiction.
2. Trace the skeptic's objection: persisted | transformed | resolved.
   Where "resolved": confirm the resolving subject's experience-proximity.
   CONDITIONAL or INFERRED resolution → "risk to monitor, not a confirmed resolution."
3. Where testimony directions diverge across subjects with different epistemic weights,
   name the weight adjustment explicitly.

  GATE: PHASE [N+1] EXIT — SYNTHESIS
  PROHIBITED: Synthesis prose in place of the named artifact table; objection fate
    asserted without tracing across subjects by name.
  REQUIRED:
  [ ] Synthesis artifact table present with all five columns populated
  [ ] Objection lifecycle explicitly traced (persisted / transformed / resolved)
  [ ] At least one epistemic weight adjustment named
  STATUS: OPEN

---

## PHASE N+2: SIMULATION FIDELITY AND VOICE AUDIT

  Simulation Fidelity: Name one claim grounded in documented knowledge (state basis).
  Name one claim that is plausible inference (not documented). Distinguish them explicitly.

  Voice Divergence: Name one concrete contrast in how two subjects sound different.
  Cite a specific vocabulary term, framing preference, or concern priority.
  "They had different roles" does not satisfy this — cite the specific linguistic difference.

  GATE: PHASE [N+2] — FINAL
  REQUIRED:
  [ ] Simulation fidelity note distinguishes grounded from inferred claims
  [ ] Voice divergence names a specific vocabulary or framing contrast
  STATUS: OPEN
```

---

## V-04 — Combination: Role Sequence + Lifecycle Emphasis

**Axis**: Role sequence (skeptic-first, objection lifecycle prominent) × lifecycle emphasis (explicit gate architecture)  
**Hypothesis**: Combining skeptic-first ordering with a PROHIBITED-first gate architecture makes the objection lifecycle structurally mandatory — the skeptic's primary objection is captured at Phase 1's exit gate, referenced at Phase 2's entry gate, and resolved or persisted at Phase N's exit gate, converting C-21 from an authorial act to a structural contract.

---

```
You are running a simulated stakeholder interview series. This is a simulation —
not real interviews, but grounded in each persona's documented knowledge and concerns.

Topic under investigation: {{TOPIC}}

---

## DOCUMENT-HEAD CONTRACT

Gate format for this document:

  GATE: [name]
  PROHIBITED: [out-of-scope content by category]
  REQUIRED: [ ] [items]
  STATUS: OPEN → CLOSED

Objection lifecycle contract: The skeptic subject runs first. Their primary objection
is named at Phase 1 exit and carried forward — every subsequent phase gate confirms
whether the objection appeared, transformed, or remained unaddressed. The synthesis
closes the lifecycle with an explicit fate declaration.

---

## PHASE 0-A: SUBJECT CARDS AND SEQUENCE DECLARATION

Declare the interview sequence before subject cards:

  INTERVIEW SEQUENCE
  Position 1 (SKEPTIC): [name] — highest-resistance subject
  Position 2 (NEUTRAL/OPERATIONAL): [name] — grounded-in-operations subject
  Position N (ADVOCATE): [name] — validation-oriented subject
  Sequence Rationale: [one sentence — why skeptic leads]

Then declare Subject Cards:

  SUBJECT CARD
  Role:
  Prior Knowledge:
  Blind Spots:
  Disposition: SKEPTIC | NEUTRAL | ADVOCATE
  Evidential Function: [structural contribution to evidence chain — not role restatement]
  Vocabulary Signature: [2–3 named terms unique to this persona]
  Expected Claims: [what the interviewer expects + why]

  GATE: PHASE 0-A
  PROHIBITED: Subjects without named evidential functions; vocabulary declared as
    trait rather than named terms; sequence positions without rationale.
  REQUIRED:
  [ ] All subject cards complete (all seven fields)
  [ ] Skeptic identified and placed at Position 1
  [ ] Sequence rationale present
  STATUS: OPEN

---

## PHASE 0-B: EXPECTATION REGISTER

  EXPECTATION REGISTER
  | ID | Subject | Expected Claim | Basis |
  |----|---------|----------------|-------|

Minimum one entry per subject. IDs: ER-01, ER-02, ...

  GATE: PHASE 0-B
  PROHIBITED: Register entries added after transcripts begin.
  REQUIRED:
  [ ] At least one entry per subject with basis stated
  [ ] All entries have Register IDs
  STATUS: OPEN

---

## PHASE 0-C: MOMENT-LABEL TAXONOMY

  SURPRISING: Prior expectation violated. Format: SURPRISING (expected: [ER-ID: "..."], got: [...])
  CONFIRMING: Prior expectation upheld. Format: CONFIRMING (validates: [ER-ID: "..."])
  INCONCLUSIVE: Signal present, directionally ambiguous. Format: INCONCLUSIVE (signal: [...], ambiguity: [...])
  If no INCONCLUSIVE moments occur: state explicitly "All moments were unambiguously classified."

  GATE: PHASE 0-C
  PROHIBITED: Labeling systems that omit the INCONCLUSIVE option or its condition.
  REQUIRED:
  [ ] All three labels declared with apply-when conditions
  [ ] All three format strings present
  STATUS: OPEN

---

## PRE-INTERVIEW MASTER GATE

  GATE: PRE-INTERVIEW MASTER
  PROHIBITED: Any interview transcript before this gate closes.
  REQUIRED:
  [ ] Phase 0-A GATE: CLOSED
  [ ] Phase 0-B GATE: CLOSED
  [ ] Phase 0-C GATE: CLOSED
  [ ] Document-head contract declared
  STATUS: OPEN

---

## PHASE 1: SKEPTIC INTERVIEW

  GATE: PHASE 1 ENTRY
  PROHIBITED: Questions not anchored to the skeptic's declared concerns;
    softening the skeptic's resistance to ease the interview.
  REQUIRED:
  [ ] Questions derive from skeptic's Prior Knowledge and Blind Spots
  [ ] Vocabulary signature terms will appear in transcript
  STATUS: OPEN

Transcript: Questions and answers in the skeptic's voice.
At least one FOLLOW-UP (triggered by: "[exact phrase]"): [question]

Evidence Extraction:

  EVIDENCE TABLE — [Skeptic Name]
  | # | Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity |

Moment Labels (per Phase 0-C taxonomy, citing Register IDs).

  GATE: PHASE 1 EXIT
  PROHIBITED: Evidence items with blank cells; moment labels without Register IDs.
  REQUIRED:
  [ ] Evidence table fully populated (six columns)
  [ ] At least one moment label citing a Register ID
  [ ] Vocabulary signature exercised (Term 1: ✓/✗, Term 2: ✓/✗)
  [ ] SKEPTIC PRIMARY OBJECTION NAMED: "[exact statement]"
      This objection is tracked in all subsequent gates.
  STATUS: OPEN

---

## PHASE 2: NEUTRAL / OPERATIONAL INTERVIEW

  GATE: PHASE 2 ENTRY
  PROHIBITED: Questions generic to the topic (not tailored to this subject's operational
    context); ignoring the skeptic's primary objection.
  REQUIRED:
  [ ] Skeptic primary objection from Phase 1 exit gate carried forward
  [ ] Questions anchored to this subject's operational prior knowledge
  STATUS: OPEN

Transcript, Evidence Table, and Moment Labels (same schema as Phase 1).

  GATE: PHASE 2 EXIT
  PROHIBITED: Evidence table with blank cells; transition to Phase 3 without
    noting skeptic objection fate.
  REQUIRED:
  [ ] Evidence table fully populated
  [ ] Moment labels cite Register IDs
  [ ] Vocabulary signature exercised
  [ ] SKEPTIC OBJECTION FATE (Phase 2): appeared | transformed | absent
      Note how (or that) this subject's testimony affected the objection
  STATUS: OPEN

---

## PHASE N: ADVOCATE INTERVIEW (and any additional subjects)

Follow Phase 2 structure.

  GATE: PHASE N EXIT
  PROHIBITED: Advocate claims treated as equivalent in weight to GROUNDED skeptic
    claims without explicit epistemic adjustment; objection lifecycle left untraced.
  REQUIRED:
  [ ] Evidence table fully populated
  [ ] Moment labels cite Register IDs
  [ ] Vocabulary signature exercised
  [ ] SKEPTIC OBJECTION FATE (Phase N): appeared | transformed | resolved | persisted
  [ ] If "resolved": advocate's experience-proximity stated
      (CONDITIONAL or INFERRED resolution → flag "risk to monitor, not confirmed")
  STATUS: OPEN

---

## PHASE N+1: SYNTHESIS

  GATE: SYNTHESIS ENTRY
  PROHIBITED: Prose-only synthesis without named artifact and column schema;
    objection fate declared without cross-subject tracing.
  REQUIRED:
  [ ] Synthesis artifact schema declared before populating
  STATUS: OPEN

  SYNTHESIS ARTIFACT
  | Subject | Signal Category | Testimony Direction | Epistemic Weight | Implication |

After the table:
1. Name convergences and contradictions visible column by column.
2. Objection lifecycle closure:
   SKEPTIC OBJECTION: "[original claim from Phase 1 exit]"
   Phase 1: [stated] → Phase 2: [appeared/transformed/absent] → Phase N: [fate]
   CONCLUSION: persisted | transformed to [X] | resolved by [subject] ([experience-proximity])
3. Epistemic weight adjustments: where CONDITIONAL or INFERRED evidence contributed
   to the conclusion, name the adjustment explicitly.

  GATE: SYNTHESIS EXIT
  REQUIRED:
  [ ] Synthesis artifact populated (all five columns)
  [ ] Objection lifecycle closure written with phase-by-phase trace
  [ ] At least one explicit epistemic weight adjustment
  STATUS: OPEN

---

## PHASE N+2: FIDELITY AND VOICE AUDIT

Simulation Fidelity: Grounded claims (basis stated) vs. plausible inference.
Voice Divergence: One specific vocabulary or framing contrast between two subjects.
  (Cite the term or phrase — not "they had different roles.")
```

---

## V-05 — Combination: Document-Head Sub-Schema Citation System + Gate Architecture

**Axis**: Document-head contract sub-schemas numbered as navigable citation system × gate architecture  
**Hypothesis**: Numbering sub-schemas at the document head (0.1 gate format, 0.2 evidence schema, 0.3 moment-label format, 0.4 subject schema) and requiring downstream sections to cite `per 0.3 contract` or `per 0.2 schema` converts the head contract from a flat declaration into a resolvable pointer target — making C-33 fully satisfiable and closing C-35's citation gap by making the master gate the single authorization authority for all point-of-use checks.

---

```
You are running a simulated stakeholder interview series. This is a simulation —
not real interviews, but grounded in each persona's documented knowledge and concerns.

Topic under investigation: {{TOPIC}}

---

## SECTION 0: DOCUMENT-HEAD CONTRACT

This section is the single source of truth for all format requirements in this document.
Every downstream section cites this section by sub-schema number.
Violations of downstream format requirements are violations of the specific sub-schema
named here — not of section-local conventions.

---

### 0.1 — Gate Format Contract

All gates in this document conform to this format:

  GATE: [phase name] | SCOPE: [single concern this gate validates]
  PROHIBITED: [out-of-scope content by category, named specifically]
  REQUIRED:
  [ ] [item — binary verifiable, one concern per item]
  STATUS: OPEN → CLOSED

Deviations: any gate missing PROHIBITED, using prose instead of checklist items,
or omitting SCOPE fails against Section 0.1.

---

### 0.2 — Evidence Schema Contract

All evidence extraction tables in this document conform to this schema:

  | # | Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity |

Column constraints:
- Signal Type: adoption risk | feasibility concern | requirement gap | scope signal |
    constraint | validation signal | contradiction  (no other values)
- Strength: strong | moderate | weak  (no other values)
- Strength Rationale: one sentence minimum — names what makes the rating warranted
- Origin-of-Claim: verbatim | inferred | corroborated  (origin taxonomy — how derived from transcript)
- Experience-Proximity: GROUNDED | CONDITIONAL | INFERRED  (proximity taxonomy — subject's experience closeness)

These two final columns are orthogonal and must not be conflated.
Origin-of-Claim answers: "was this quoted?" — Experience-Proximity answers: "has this subject lived it?"

**Section 0.2 example row** (demonstrates schema fully instantiated):

| # | Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity |
|---|------|-------------|----------|--------------------|-----------------|---------------------|
| 1 | Rollback procedure has never been tested under load | feasibility concern | strong | Subject has run production deployments; this gap is direct observation, not speculation | verbatim | GROUNDED |

Any evidence table row that deviates from this schema fails against Section 0.2.

---

### 0.3 — Moment-Label Format Contract

All moment labels in this document conform to this taxonomy (complete decision system):

  SURPRISING: Prior expectation violated by what emerged.
    Apply when: what the subject said contradicts a Register entry.
    Format: SURPRISING (expected: [ER-ID: "claim from register"], got: [what emerged])

  CONFIRMING: Prior expectation upheld by what emerged.
    Apply when: what the subject said matches or reinforces a Register entry.
    Format: CONFIRMING (validates: [ER-ID: "claim from register"])

  INCONCLUSIVE: Signal present but directionally ambiguous.
    Apply when: notable content exists but cannot be assigned to either prior-expectation category.
    Format: INCONCLUSIVE (signal: [what was said], ambiguity: [why unassignable])

If no INCONCLUSIVE moments arise: note explicitly "All moments assigned per 0.3 contract —
no ambiguous cases identified."

Deviations: moment labels without Register IDs, labels in non-declared formats, or
labels that omit the INCONCLUSIVE option without acknowledgment fail against Section 0.3.

---

### 0.4 — Subject Schema Contract

All Subject Cards conform to this schema:

  SUBJECT CARD — [Subject N of M]
  Role: [title and function]
  Prior Knowledge: [specific things known from role experience — not generic]
  Blind Spots: [what this subject has not experienced or seen directly]
  Disposition: SKEPTIC | NEUTRAL | ADVOCATE
  Evidential Function: [structural contribution to evidence chain — not role restatement;
    names what this subject's position *does* for the investigation]
  Vocabulary Signature:
    Term 1: [exact term] — [why this persona uses it]
    Term 2: [exact term] — [why this persona uses it]
    Term 3 (optional): [exact term] — [why]
  Expected Claims: [what the interviewer expects + basis]
  Sequence Position: [N of M — one sentence justifying this position in the interview order]

Deviations: missing Evidential Function, vocabulary described as trait rather than named terms,
or sequence positions without rationale fail against Section 0.4.

---

### SECTION 0 MASTER GATE

  GATE: SECTION 0 | SCOPE: Document-head contract completeness
  PROHIBITED: Proceeding to any subject card, expectation register, or interview
    transcript before this gate closes. Any section that deploys a format requirement
    before Section 0 is fully closed violates the document-head contract.
  REQUIRED:
  [ ] 0.1 Gate Format Contract declared with SCOPE, PROHIBITED, REQUIRED, STATUS fields
  [ ] 0.2 Evidence Schema Contract declared with all six column constraints
      and one fully instantiated example row
  [ ] 0.3 Moment-Label Contract declared with all three labels, apply-when conditions,
      format strings, and INCONCLUSIVE acknowledgment rule
  [ ] 0.4 Subject Schema Contract declared with all eight fields
  STATUS: OPEN

---

## SECTION 1: SUBJECT CARDS AND SEQUENCE

*Per Section 0.4 schema and Section 0.1 gate format.*

Declare interview sequence before subject cards:

  INTERVIEW SEQUENCE DECLARATION
  Order: [Subject 1] → [Subject 2] → ... → [Subject N]
  Rationale: [one sentence — why this specific ordering serves the investigation]

Then populate one Subject Card per subject using the Section 0.4 schema.
Minimum: two subjects with meaningfully distinct roles, knowledge levels, or priorities.

  GATE: SECTION 1 | SCOPE: Subject setup completeness (per 0.4 schema)
  PROHIBITED: Advancing to Section 2 before all Subject Cards are complete
    per 0.4 schema; vocabulary described as trait rather than named terms.
  REQUIRED:
  [ ] All Subject Cards complete (all eight fields per 0.4)
  [ ] At least two subjects with distinct dispositions
  [ ] Sequence order declared with rationale
  STATUS: OPEN

---

## SECTION 2: EXPECTATION REGISTER

*Structural source for all "expected:" slots per Section 0.3 moment-label contract.*

  EXPECTATION REGISTER
  | ID | Subject | Expected Claim | Basis for Expectation |
  |----|---------|----------------|----------------------|

IDs: ER-01, ER-02, ... (assigned sequentially; cited by all moment labels per 0.3)
Every subject must have at least one entry.

  GATE: SECTION 2 | SCOPE: Expectation Register completeness
  PROHIBITED: Register entries added after any transcript begins;
    any subject with zero register entries.
  REQUIRED:
  [ ] At least one entry per subject with basis stated
  [ ] All entries have sequential IDs
  [ ] Register is fully populated before Section 3 opens
  STATUS: OPEN

---

## SECTION 3: VOCABULARY SIGNATURE FORWARD CONTRACT

*Derived from Subject Cards per 0.4; closing mechanism for vocabulary audit.*

For each subject: list each declared vocabulary term and confirm it will appear
naturally in that subject's transcript. This is a forward contract against which
transcripts will be audited at each interview's exit gate.

  VOCABULARY FORWARD CONTRACT
  | Subject | Term | Committed to appear in transcript |
  |---------|------|-----------------------------------|

---

## PRE-INTERVIEW MASTER GATE

*Consolidates Sections 1–3 before Phase 1 can open.*
*All point-of-use prerequisite confirmations in interview phases cite this gate
as authorization authority — per Section 0.1 and the citation contract below.*

  GATE: PRE-INTERVIEW MASTER | SCOPE: All pre-interview structural prerequisites
  PROHIBITED: Opening any interview transcript (Phase 1 or later) before this gate closes.
  REQUIRED:
  [ ] Section 1 GATE: CLOSED — Subject Cards complete (per 0.4 schema)
  [ ] Section 2 GATE: CLOSED — Expectation Register populated
  [ ] Section 3 forward contract: populated for all subjects
  [ ] Section 0.3 Moment-Label Contract: all three labels declared
  [ ] Section 0.2 Evidence Schema: example row present
  STATUS: OPEN

*Authorization note: All point-of-use prerequisite checks in Phases 1–N
cite this gate as their authority. Format: "[prerequisite] confirmed FULLY SATISFIED
in PRE-INTERVIEW MASTER GATE, [item N]."*

---

## PHASES 1–N: INTERVIEW TRANSCRIPTS

Run one phase per subject in declared sequence order.

Each phase contains five elements:

**Element A: Phase Entry Gate**

  GATE: PHASE [N] ENTRY — [Subject Name] | SCOPE: Interview readiness for this subject
  PROHIBITED: Questions not anchored to this subject's declared prior knowledge
    and concerns; evidence extraction before transcript complete.
  REQUIRED:
  [ ] Vocabulary signature forward contract reviewed
      (confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE, item 3)
  [ ] Subject's Evidential Function carried into this phase
      (confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE, item 1)
  STATUS: OPEN

**Element B: Interview Transcript**

Questions in the interviewer's voice. Answers in the declared persona's voice —
vocabulary, concerns, and framing must match the Section 0.4 Subject Card.
Generic answers that could belong to any persona fail against 0.4.

Follow-up format (at least one required per subject):
  FOLLOW-UP (triggered by: "[exact phrase from prior answer]"): [question]

**Element C: Evidence Extraction**

*Per Section 0.2 schema.*

  EVIDENCE TABLE — [Subject Name] (per 0.2 schema)
  | # | Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity |

All six column constraints per 0.2 apply. No blank cells.
Origin-of-Claim and Experience-Proximity are orthogonal — do not conflate per 0.2.

**Element D: Moment Labels**

*Per Section 0.3 contract.*

Apply SURPRISING, CONFIRMING, or INCONCLUSIVE per 0.3 decision rules.
Cite Register IDs in "expected:" and "validates:" slots (per 0.3 format strings).
At least one label per subject.
If INCONCLUSIVE applies: use it. If not: note "All moments unambiguously classified per 0.3."

**Element E: Phase Exit Gate**

  GATE: PHASE [N] EXIT — [Subject Name] | SCOPE: Interview completeness for this subject
  PROHIBITED: Evidence items with blank cells (fails 0.2); moment labels
    without Register IDs (fails 0.3); vocabulary terms declared in 0.4 but
    absent from transcript (fails forward contract).
  REQUIRED:
  [ ] Evidence table: all rows complete per 0.2 schema
  [ ] Moment labels: all cite Register IDs per 0.3 contract
  [ ] Vocabulary audit: Term 1 [appeared/absent], Term 2 [appeared/absent]
      (Terms declared in 0.4, committed in Section 3 forward contract)
  [ ] Evidential Function delivery confirmed: [how this subject's testimony
      fulfilled the function declared in 0.4]
  STATUS: OPEN

---

## SECTION N+1: CROSS-INTERVIEW SYNTHESIS

*Per Section 0.2 schema extended to synthesis dimensions.*

  GATE: SYNTHESIS ENTRY | SCOPE: Synthesis setup
  PROHIBITED: Prose-only synthesis without schema artifact; epistemic weight
    assertions without cross-referencing 0.2 Experience-Proximity column.
  REQUIRED:
  [ ] Synthesis artifact schema declared before populating
  STATUS: OPEN

Synthesis artifact:

  SYNTHESIS ARTIFACT (per 0.2 Experience-Proximity for weighting)
  | Subject | Signal Category | Testimony Direction | Epistemic Weight Adjustment | Implication |
  Testimony Direction: supports | challenges | inconclusive
  Epistemic Weight Adjustment: cites Experience-Proximity from 0.2 evidence tables

After the table:

1. Name convergences and contradictions visible column by column.
2. If a skeptic/challenger subject is present: trace their primary objection's fate
   across all phases — persisted | transformed | resolved.
   Resolution by CONDITIONAL/INFERRED subject → "risk to monitor per 0.2 experience-proximity."
3. At least one item where epistemic weight adjustment is named explicitly and changes
   the implication from what a face-value reading would produce.

  GATE: SYNTHESIS EXIT | SCOPE: Synthesis completeness
  PROHIBITED: Synthesis that leaves epistemic weight unaddressed for divergent items.
  REQUIRED:
  [ ] Artifact table populated (all five columns)
  [ ] Objection lifecycle traced if applicable
  [ ] At least one explicit epistemic weight adjustment
  STATUS: OPEN

---

## SECTION N+2: SIMULATION FIDELITY NOTE AND VOICE AUDIT

Simulation Fidelity (per 0.4 prior knowledge fields):
- Grounded: [claim] — basis: [which field in which Subject Card grounds this]
- Inferred: [claim] — plausible given role, not documented

Voice Divergence (per 0.4 vocabulary signatures):
Cite one specific term or framing preference that distinguishes two subjects.
Format: "Subject A uses '[term]' where Subject B uses '[term]' — this reflects [role-specific framing]."
Generic role differences fail this section.

  GATE: FINAL | SCOPE: Document closure
  REQUIRED:
  [ ] Simulation fidelity note distinguishes grounded from inferred per 0.4
  [ ] Voice divergence cites a specific term per 0.4 vocabulary signatures
  [ ] All phase gates marked CLOSED
  STATUS: OPEN
```

---

## Variation Summary

| Variation | Axis | Predicted Highest Gains | Predicted Gaps |
|-----------|------|------------------------|----------------|
| V-01 | Role sequence (skeptic-first) | C-19, C-21 structural | C-33, C-35 still authorial |
| V-02 | Output format (schema-native tables) | C-29, C-36, C-38 | Gate architecture underdeveloped |
| V-03 | Lifecycle emphasis (PROHIBITED-first gates) | C-32, C-39, C-40 | Citation system absent — C-35 stays FAIL |
| V-04 | Sequence + lifecycle | C-19, C-21, C-32, C-39 | Sub-schema citation still absent |
| V-05 | Document-head sub-schemas + citation | C-33 PASS, C-35 PARTIAL→PASS, C-41 PARTIAL→PASS; all prior gains preserved via gate architecture | C-40 sub-phase decomposition requires multi-concern gate identification |
