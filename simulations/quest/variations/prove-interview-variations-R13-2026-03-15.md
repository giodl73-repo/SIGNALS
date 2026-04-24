# prove-interview Rubric v12 — Skill Variations V-01 through V-05

---

## V-01 — Role Sequence Axis

**Variation axis**: Role sequence (fixed Skeptic → Baseline → Advocate ordering)
**Hypothesis**: Opening with the skeptic puts objections on the record before corroboration is claimed. C-21 (objection lifecycle) becomes structurally mandatory rather than authorial — the synthesis cannot declare convergence without tracing the skeptic's objection through every subsequent subject.

---

```markdown
You are running the Signal **prove-interview** skill.

Topic: {topic}
Date: {date}
Output: simulations/prove/{topic}-interview-{date}.md

---

## ROLE SEQUENCE CONTRACT

Subjects are always interviewed in this order:

1. **Skeptic** — a subject with reason to doubt, challenge, or resist the topic claim
2. **Baseline** — a subject with neutral standing and operational exposure but no strong prior position
3. **Advocate** — a subject with direct experience or institutional stake aligned with the topic claim

This order is not negotiable. The skeptic must open because their objections must exist on
the record before any later subject can be said to address them. The baseline anchors
operational reality between challenge and validation. The advocate closes because their
validation is structurally stronger when it arrives after objection, not before it.

If a two-subject interview is appropriate, use Skeptic → Advocate with a note explaining
why a neutral baseline is absent. A single-subject interview is permitted only when no
meaningful role contrast exists — note the reason in the output header.

---

## PHASE 0 — PRE-INTERVIEW SETUP

### Subject Cards

For each subject, produce a Subject Card before any transcript begins:

```
SUBJECT CARD
Subject: [name or label]
Role: [title or function]
Prior Knowledge: [what they know, what they have seen firsthand]
Blind Spots: [what they systematically underweight or lack direct exposure to]
Disposition: Skeptic / Baseline / Advocate — and one sentence explaining why
Vocabulary Signature: [2–3 role-specific terms distinctive enough to spot-check
                        transcript answers — not general descriptors]
Evidential Function: [one sentence naming what this subject's position does for
                      the evidence structure — e.g., "establishes the objection
                      baseline that subsequent subjects must address or sustain"]
```

Produce Subject Cards for all subjects before moving to the Expectation Register.

### Expectation Register

After all Subject Cards, produce the Expectation Register:

```
EXPECTATION REGISTER
Subject: [name/label]
  Expectation 1: [specific claim or concern the interviewer predicts this subject will raise]
    Basis: [why — role logic, domain pattern, or prior-knowledge inference]
  Expectation 2: [...]
    Basis: [...]
```

At minimum one expectation per subject. The register is the structural source for all
SURPRISING and CONFIRMING labels in Phases 1–3. Labels that cite no register entry fail.

### Moment-Label Decision Taxonomy

After the Expectation Register, declare the complete labeling taxonomy:

```
MOMENT-LABEL TAXONOMY
SURPRISING  = prior expectation explicitly violated — something the Expectation Register
              predicted would not happen, happened (or vice versa)
CONFIRMING  = prior expectation explicitly upheld — what the register predicted, the
              subject delivered
INCONCLUSIVE = signal present but directionally ambiguous — cannot be assigned to either
               prior-expectation category with confidence
```

All three decision rules are declared even if INCONCLUSIVE does not occur — the taxonomy
governs the system, not only the cases that arise.

**PHASE 0 GATE**
PROHIBITED: interview transcripts, evidence extraction, cross-subject comparison
REQUIRED:
[ ] Subject Card complete for every subject (all six fields present)
[ ] Expectation Register populated for every subject (at least one expectation with basis)
[ ] Moment-Label Taxonomy declared in full (all three labels with decision rules)
[ ] Subjects sequenced Skeptic → Baseline → Advocate (or Skeptic → Advocate with note)

---

## PHASE 1 — SKEPTIC INTERVIEW

Open with the Skeptic's Subject Card (cross-reference by label; do not re-produce unless
this is the first appearance).

Conduct the interview:

1. **Opening** — broad framing question inviting the Skeptic to characterize the topic in
   their own terms
2. **Follow-ups (2–4)** — each opens with a trigger citation: quote or paraphrase the
   specific phrase from the preceding answer that prompted this question, using the format:
   `[triggered by: "exact phrase or paraphrase"] Follow-up: ...`
3. **Closing** — what would have to be true for the Skeptic to revise their position?

Write answers in the Skeptic's declared voice. At least one answer must use a Vocabulary
Signature term naturally.

After the transcript, produce the Skeptic Evidence Table:

| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Strength Rationale |
|---|---|---|---|---|---|
| [claim] | adoption risk / feasibility concern / requirement gap / scope signal / constraint | GROUNDED / CONDITIONAL / INFERRED | verbatim / inferred / corroborated | strong / moderate / weak | [one sentence] |

Signal Type labels the downstream use. Experience-Proximity (GROUNDED/CONDITIONAL/INFERRED)
labels how close the subject is to direct operational experience. Origin-of-Claim
(verbatim/inferred/corroborated) labels how the claim was derived from the transcript.
These two dimensions are orthogonal — do not collapse them into a single tag.

After the evidence table, label all notable moments:

```
MOMENT LABELS — SKEPTIC
Moment: [description of what was said]
Label: SURPRISING (expected: [cite Expectation Register entry], got: [what emerged])
  — OR —
Label: CONFIRMING (validates: [cite Expectation Register entry])
  — OR —
Label: INCONCLUSIVE (signal: [what was said], ambiguity: [why direction is unclear])
```

Every SURPRISING or CONFIRMING label must cite a specific Expectation Register entry.

**PHASE 1 GATE**
PROHIBITED: Baseline or Advocate testimony, synthesis, objection resolution claims
REQUIRED:
[ ] Skeptic transcript complete (opening + follow-ups with trigger citations + closing)
[ ] At least one follow-up cites triggering phrase using `[triggered by: "..."]` format
[ ] At least one Vocabulary Signature term appears in transcript
[ ] Evidence Table complete (all six columns filled for every row)
[ ] At least one moment labeled
[ ] Every SURPRISING/CONFIRMING label cites Expectation Register

---

## PHASE 2 — BASELINE INTERVIEW

Same structure as Phase 1, applied to the Baseline subject.

The Baseline's questions should probe what the subject has *directly observed* in operational
context — not predictions or beliefs. At least one question should probe a topic dimension
that the Skeptic raised as a concern, without explicitly attributing it to the Skeptic.

Produce the Baseline Evidence Table (same schema as Phase 1).

Produce Baseline Moment Labels (same format as Phase 1).

**PHASE 2 GATE**
PROHIBITED: Advocate testimony, synthesis, composite signal declaration
REQUIRED:
[ ] Baseline transcript complete (follow-ups with trigger citations present)
[ ] At least one question probes a topic dimension raised by the Skeptic
[ ] Evidence Table complete (all six columns)
[ ] Moment labels present with Expectation Register citations

---

## PHASE 3 — ADVOCATE INTERVIEW

Same structure as Phases 1–2, applied to the Advocate subject.

The interviewer holds the Skeptic's primary objection from Phase 1. At least one question
must directly probe whether the Advocate is aware of or can address that objection — quote
or paraphrase the Skeptic's objection when asking. Do not force resolution: the Advocate
may validate, deflect, or be unaware.

Produce the Advocate Evidence Table (same schema).

Produce Advocate Moment Labels.

**PHASE 3 GATE**
PROHIBITED: Synthesis, objection verdict, composite signal declaration
REQUIRED:
[ ] Advocate transcript complete
[ ] At least one question references Skeptic's primary objection (quoted or paraphrased)
[ ] Evidence Table complete
[ ] Moment labels present with Expectation Register citations

---

## PHASE 4 — SYNTHESIS

### Objection Lifecycle Trace

State the Skeptic's primary objection as recorded in Phase 1. Then trace its fate
through each subsequent phase:

- Baseline (Phase 2): Did the Baseline subject sustain, transform, or fail to address it?
- Advocate (Phase 3): Did the Advocate sustain, transform, or resolve it?

Final verdict: **PERSISTED** / **TRANSFORMED** / **RESOLVED** — one sentence of evidence.

### Cross-Interview Synthesis Table

| Subject | Evidence Category | Testimony Direction | Implication |
|---|---|---|---|
| Skeptic | [category] | supports / challenges / inconclusive | [one sentence] |
| Baseline | [category] | supports / challenges / inconclusive | [one sentence] |
| Advocate | [category] | supports / challenges / inconclusive | [one sentence] |

### Composite Signal

One sentence: the signal produced by these interviews. Name which subjects corroborate it,
which challenge it, and whether the evidence is sufficient to act or requires further
investigation.

**PHASE 4 GATE**
PROHIBITED: New evidence items not derived from Phases 1–3, subject recasts
REQUIRED:
[ ] Objection Lifecycle Trace present (Skeptic objection named, fate traced through
    Baseline and Advocate, final verdict declared)
[ ] Cross-Interview Synthesis Table complete (all subjects, all rows populated)
[ ] Composite Signal declared

---

## SIMULATION FIDELITY NOTE

After Phase 4, include one paragraph naming: (1) at least one claim that is grounded in
documented domain knowledge or established persona logic, and (2) at least one claim that
is constructed plausibility — reasonable given the role but not derivable from a named
source. Distinguish simulation fidelity from simulation confabulation.
```

---

## V-02 — Output Format Axis

**Variation axis**: Output format (document-head schema registry with instantiated example rows)
**Hypothesis**: Declaring all table schemas — column headers plus a fully populated example row — in a document-head registry before any interview content closes the schema-without-instance failure (C-29). Every table in the body is a named instance of a declared schema; a table that misses a column is detectable against the registry without reading the prose.

---

```markdown
You are running the Signal **prove-interview** skill.

Topic: {topic}
Date: {date}
Output: simulations/prove/{topic}-interview-{date}.md

---

## DOCUMENT-HEAD SCHEMA REGISTRY

The following schemas govern all tabular output in this artifact. Each schema is
declared once here with column definitions and a fully instantiated example row.
Every table in Phases 1–N must reproduce the exact schema for its type. A table
that omits a column or leaves a cell blank violates the declared contract.

---

### Schema S-1: Evidence Table

Applies to: one table per interview subject, produced immediately after the transcript.

| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Strength Rationale |
|---|---|---|---|---|---|
| **EXAMPLE** — "Existing tooling already handles this at lower cost" | adoption risk | GROUNDED (subject has deployed the alternative) | verbatim (direct quote from transcript) | strong | Subject has firsthand operational experience; claim is not hedged |

Column definitions:
- **Evidence Item**: a specific claim extracted from the transcript, stated as a discrete assertion
- **Signal Type**: adoption risk / feasibility concern / requirement gap / scope signal / constraint
- **Experience-Proximity**: GROUNDED (direct operational experience) / CONDITIONAL (indirect or secondhand) / INFERRED (no direct exposure; reasoning from analogy)
- **Origin-of-Claim**: verbatim (quoted directly) / inferred (implied but not stated) / corroborated (consistent signal across ≥2 subjects)
- **Strength**: strong / moderate / weak
- **Strength Rationale**: one sentence naming what makes the evidence reliable, hedged, or ambiguous

Experience-Proximity and Origin-of-Claim are orthogonal dimensions — do not collapse into a single tag.

---

### Schema S-2: Moment Labels Table

Applies to: one table per interview subject, produced after the Evidence Table.

| Moment | Label | Expected (from Register) | What Emerged | Ambiguity Note |
|---|---|---|---|---|
| **EXAMPLE** — Subject dismisses implementation timeline concern | SURPRISING | Register: "Expected cost objection, not timeline concern" | Subject shifted to schedule risk | — |

Column definitions:
- **Moment**: brief description of what was said or happened
- **Label**: SURPRISING / CONFIRMING / INCONCLUSIVE
- **Expected (from Register)**: cite the specific Expectation Register entry this label resolves; required for SURPRISING and CONFIRMING; write "—" for INCONCLUSIVE
- **What Emerged**: what the subject actually said that triggered the label
- **Ambiguity Note**: required for INCONCLUSIVE (name the ambiguity); write "—" for SURPRISING and CONFIRMING

---

### Schema S-3: Cross-Interview Synthesis Table

Applies to: Phase N+1 synthesis, once after all subjects.

| Subject | Role | Evidence Category | Testimony Direction | Epistemic Weight | Implication |
|---|---|---|---|---|---|
| **EXAMPLE** — Alex (CTO) | Skeptic | Feasibility | challenges | High — direct prior implementation | Treat as blocker until timeline is renegotiated |

Column definitions:
- **Subject**: label used throughout the artifact
- **Role**: Skeptic / Baseline / Advocate (or custom)
- **Evidence Category**: the topic dimension this subject's evidence addresses
- **Testimony Direction**: supports / challenges / inconclusive
- **Epistemic Weight**: High (direct experience) / Medium (indirect) / Low (no direct exposure) — with a brief note
- **Implication**: one sentence on what this subject's position means for the topic narrative

---

### Schema S-4: Objection Lifecycle Table

Applies to: Phase N+1 synthesis, covering one row per subject response to the primary skeptic objection.

| Phase | Subject | Objection Response | Lifecycle Status |
|---|---|---|---|
| **EXAMPLE** — Phase 2 | Morgan (Baseline) | "We've seen timeline slippage before; it's real but manageable with phasing" | TRANSFORMED — from blocker to risk-to-manage |

Column definitions:
- **Phase**: Phase number where this response appears
- **Subject**: subject label
- **Objection Response**: what the subject said about the Skeptic's primary objection (verbatim or close paraphrase)
- **Lifecycle Status**: SUSTAINED (objection stands as stated) / TRANSFORMED (objection reframed or scoped differently) / RESOLVED (objection addressed with countervailing evidence) / NOT ADDRESSED (subject did not engage with it)

---

## PHASE 0 — SETUP

### Subject Cards

For each subject, produce a Subject Card in this format:

```
SUBJECT CARD — [Subject Label]
Role: [title or function]
Prior Knowledge: [what they know and have experienced directly]
Blind Spots: [what they systematically underweight or lack exposure to]
Disposition: [Skeptic / Baseline / Advocate] — [one-sentence rationale]
Vocabulary Signature: [2–3 specific terms — auditable, not descriptive]
Evidential Function: [one sentence: what structural role this subject plays in the
                      evidence chain, not merely who they are]
```

### Expectation Register

After Subject Cards, produce the Expectation Register as a table:

| Subject | Expected Claim | Basis | Register ID |
|---|---|---|---|
| [label] | [specific prediction] | [why — role logic or domain inference] | ER-[N] |

At least one row per subject. Register IDs (ER-1, ER-2, ...) are used in Schema S-2
citations.

### Moment-Label Decision Taxonomy

```
MOMENT-LABEL TAXONOMY
SURPRISING  = prior expectation violated (Register entry was not matched)
CONFIRMING  = prior expectation upheld (Register entry was matched)
INCONCLUSIVE = signal present, direction ambiguous, cannot resolve to either category
```

**PHASE 0 GATE**
REQUIRED:
[ ] All Subject Cards complete (all six fields)
[ ] Expectation Register table populated (all subjects, all columns, Register IDs assigned)
[ ] Moment-Label Taxonomy declared (all three labels)
[ ] Schema Registry declared at document head (S-1 through S-4 present with example rows)

---

## PHASE 1 THROUGH N — INTERVIEWS

For each subject, conduct one interview following this structure. Produce all tables
using the exact declared schemas — reference schemas by name (e.g., "Evidence Table —
Schema S-1") above each table.

**Interview Structure**

1. Opening question (broad framing)
2. Follow-ups (2–4) — each begins with `[triggered by: "..."]` citing the specific phrase
   from the preceding answer that prompted the question
3. Closing question (what would change the subject's assessment?)

Answers are written in the subject's declared voice. At least one Vocabulary Signature
term must appear naturally in the transcript.

**After each transcript**:

- Produce Evidence Table (Schema S-1) — every column filled
- Produce Moment Labels Table (Schema S-2) — every row cites Expectation Register by ID

**PHASE [N] GATE** (one per subject interview)
REQUIRED:
[ ] Transcript complete (opening + follow-ups with trigger citations + closing)
[ ] Vocabulary Signature term appears in transcript
[ ] Evidence Table present using Schema S-1 (all columns filled)
[ ] Moment Labels Table present using Schema S-2 (all rows cite Register IDs)

---

## PHASE N+1 — SYNTHESIS

**Objection Lifecycle Table** (Schema S-4)

Before the synthesis table, identify the Skeptic's primary objection in one sentence.
Then populate Schema S-4 for every subject from Phase 2 onward.

Declare the final objection verdict: **PERSISTED / TRANSFORMED / RESOLVED** with
one sentence of evidence drawn from the table.

**Cross-Interview Synthesis Table** (Schema S-3)

Populate Schema S-3 for all subjects. Epistemic Weight column must name the basis for
the weight assignment (experience-proximity, not just role).

**Composite Signal**

One sentence stating the topic signal produced by these interviews. Reference
specific Testimony Direction entries from Schema S-3 as evidence.

**PHASE N+1 GATE**
REQUIRED:
[ ] Objection Lifecycle Table (Schema S-4) complete
[ ] Objection verdict declared with evidence sentence
[ ] Cross-Interview Synthesis Table (Schema S-3) complete (all subjects, all columns)
[ ] Composite Signal declared

---

## SIMULATION FIDELITY NOTE

One paragraph naming: (1) one grounded claim (documented domain knowledge or
established persona logic as basis), and (2) one constructed-plausibility claim
(reasonable for the role, but no named source). Name the specific basis for the
grounded claim — generic "domain expertise" does not qualify.
```

---

## V-03 — Lifecycle Emphasis Axis

**Variation axis**: Lifecycle emphasis (heavy pre-interview setup with sub-phase decomposition)
**Hypothesis**: Decomposing the pre-interview phase into 0A, 0B-I, and 0B-II — each scoped to a single concern and each closing with its own independent exit gate — makes setup failures identifiable at sub-concern granularity (C-40). A PRE-INTERVIEW MASTER GATE that cross-references sub-gate completions by name (C-34) makes the master gate evidenced rather than asserted.

---

```markdown
You are running the Signal **prove-interview** skill.

Topic: {topic}
Date: {date}
Output: simulations/prove/{topic}-interview-{date}.md

---

## SETUP PHASES

The pre-interview structure is decomposed into three sub-phases, each covering a distinct
concern, each closing with an independent exit gate. No phase may begin before its
predecessor's gate is confirmed passed.

---

### Phase 0A — Subject Cards and Sequencing

For each subject, produce a Subject Card:

```
SUBJECT CARD — [Label]
Role: [title or function]
Prior Knowledge: [direct experience, domain exposure]
Blind Spots: [systematic gaps or non-exposures]
Disposition: [Skeptic / Baseline / Advocate / other] — [one-sentence rationale]
Vocabulary Signature: [2–3 specific terms — not descriptors; terms the transcript
                       can be spot-checked against]
Evidential Function: [one sentence naming what this subject's position does for the
                      evidence structure — not a restatement of role or disposition]
```

After all Subject Cards, provide one sentence naming the interview sequence and
why subjects appear in this order (e.g., skeptic-first to surface objections before
validation, neutral-first to establish an operational baseline).

**PHASE 0A GATE**
PROHIBITED: Expectation register, vocabulary taxonomy, moment-label rules, transcripts
REQUIRED:
[ ] Subject Card complete for every subject (all six fields populated)
[ ] Sequence order declared (subjects listed in interview order)
[ ] Subject sequence rationale present (one sentence naming the ordering logic)

---

### Phase 0B-I — Expectation Register

This sub-phase is scoped to one concern: documenting prior expectations before any
interview transcript begins. It does not cover vocabulary contracts or labeling rules —
those belong to Phase 0B-II.

Produce the Expectation Register:

```
EXPECTATION REGISTER
Subject: [label]
  ER-[N]: Expected claim: [specific prediction]
           Basis: [role logic, domain inference, or documented knowledge]
  ER-[N]: ...
```

Assign a Register ID (ER-1, ER-2, ...) to every expectation entry. These IDs are the
structural source for SURPRISING and CONFIRMING labels in Phases 1–N.

**PHASE 0B-I GATE**
PROHIBITED: Vocabulary contracts, labeling taxonomy, interview transcripts
REQUIRED:
[ ] Expectation Register present for every subject
[ ] At least one expectation per subject (with basis)
[ ] Every expectation assigned a Register ID

---

### Phase 0B-II — Vocabulary Contracts and Moment-Label Taxonomy

This sub-phase is scoped to two items: (1) vocabulary enforcement contracts per subject,
and (2) the complete moment-label decision taxonomy. These are treated together because
both function as auditable pre-declared contracts that transcript content is checked
against.

For vocabulary contracts, confirm that every Subject Card's Vocabulary Signature (from
Phase 0A) contains specific terms (not descriptors). Then declare the enforcement rule:

```
VOCABULARY ENFORCEMENT CONTRACT
Subject [Label]: Vocabulary Signature terms — [term 1], [term 2], [term 3]
  Contract: at least one of these terms must appear naturally in this subject's
            transcript answers. Answers that use only generic language and never
            deploy a Vocabulary Signature term violate this contract.
```

Produce one contract block per subject.

For the moment-label taxonomy:

```
MOMENT-LABEL DECISION TAXONOMY
SURPRISING  = prior expectation (from Expectation Register) explicitly violated
CONFIRMING  = prior expectation (from Expectation Register) explicitly upheld
INCONCLUSIVE = signal present but cannot be assigned to either prior-expectation
               category with confidence — direction is ambiguous
```

Vocabulary term values are: GROUNDED / CONDITIONAL / INFERRED (for experience-proximity).
These terms are declared here as the vocabulary set for the Experience-Proximity column
that appears in every Evidence Table. Any value outside this set in an Evidence Table
violates this gate's vocabulary contract.

**PHASE 0B-II GATE**
PROHIBITED: Interview transcripts, evidence extraction, cross-subject comparison
REQUIRED:
[ ] Vocabulary Enforcement Contract present for every subject (specific terms confirmed)
[ ] Moment-Label Taxonomy declared in full (all three labels with decision rules)
[ ] Experience-Proximity vocabulary set declared: GROUNDED / CONDITIONAL / INFERRED

---

### PRE-INTERVIEW MASTER GATE

Before Phase 1 begins, confirm that all three setup sub-phases are closed:

```
PRE-INTERVIEW MASTER GATE

Phase 0A GATE: PASSED
  — Subject Cards complete for [N] subjects; sequence order declared and justified

Phase 0B-I GATE: PASSED
  — Expectation Register populated; [N] entries across [M] subjects; IDs ER-1 through ER-[N]

Phase 0B-II GATE: PASSED
  — Vocabulary Enforcement Contracts active for all subjects; Moment-Label Taxonomy declared;
    Experience-Proximity vocabulary set locked

AUTHORIZATION: Phase 1 may begin. All pre-interview prerequisites confirmed satisfied.
```

The master gate closes by cross-referencing each sub-gate's named completion — it does not
re-assert readiness independently. If any sub-gate is incomplete, do not proceed to Phase 1;
state which sub-gate failed and what is missing.

---

## PHASE 1 THROUGH N — INTERVIEWS

For each subject (in the declared sequence order from Phase 0A):

**Confirm activation**:
> C-22 (Vocabulary Signature) confirmed FULLY SATISFIED per PRE-INTERVIEW MASTER GATE (Phase 0B-II)
> C-13 (Expectation Register) confirmed FULLY SATISFIED per PRE-INTERVIEW MASTER GATE (Phase 0B-I)

**Conduct the interview**:

1. Opening question
2. Follow-up questions (2–4) — each opens with `[triggered by: "..."]` citing the
   triggering phrase from the preceding answer
3. Closing question — what would change the subject's assessment?

Write answers in the subject's declared voice. Vocabulary Signature terms must appear
naturally in at least one answer.

**After the transcript — Evidence Table**:

| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Strength Rationale |
|---|---|---|---|---|---|
| [claim] | [type] | GROUNDED/CONDITIONAL/INFERRED | verbatim/inferred/corroborated | strong/moderate/weak | [one sentence] |

Experience-Proximity values must be drawn from the vocabulary set declared in Phase 0B-II.
Origin-of-Claim is a separate dimension — do not collapse.

**After the Evidence Table — Moment Labels**:

```
MOMENT LABELS — [Subject]
[moment description]
Label: SURPRISING (expected: [cite Register ID], got: [what emerged])
  — OR —
Label: CONFIRMING (validates: [cite Register ID])
  — OR —
Label: INCONCLUSIVE (signal: [what was said], ambiguity: [why])
```

All SURPRISING and CONFIRMING labels cite Register IDs from Phase 0B-I.

**PHASE [N] GATE**
REQUIRED:
[ ] Prerequisite confirmation statement present (citing Master Gate)
[ ] Transcript complete (opening + follow-ups with trigger citations + closing)
[ ] Vocabulary Signature term appears in transcript (per Phase 0B-II contract)
[ ] Evidence Table complete (all columns; Experience-Proximity uses declared vocabulary)
[ ] Moment labels present (all SURPRISING/CONFIRMING cite Register IDs)

---

## PHASE N+1 — SYNTHESIS

### Objection Lifecycle

Identify the primary skeptic objection (from Phase 1 or the first skeptic-disposition
subject). Trace its fate through each subsequent subject: SUSTAINED / TRANSFORMED /
RESOLVED / NOT ADDRESSED. Declare a final verdict with one sentence of evidence.

### Cross-Interview Synthesis Table

| Subject | Evidence Category | Testimony Direction | Implication |
|---|---|---|---|
| [label] | [category] | supports / challenges / inconclusive | [one sentence] |

### Composite Signal

One sentence. Name which subjects corroborate, which challenge, and whether evidence
is sufficient to act or requires further investigation.

**PHASE N+1 GATE**
REQUIRED:
[ ] Objection lifecycle traced (if skeptic-disposition subject present)
[ ] Synthesis table complete (all subjects)
[ ] Composite signal declared

---

## SIMULATION FIDELITY NOTE

One paragraph. Name one grounded claim (specific basis) and one constructed-plausibility
claim (reasonable but no named source). Distinguish simulation fidelity from confabulation.
```

---

## V-04 — Combined: Role Sequence + Lifecycle Emphasis

**Variation axes**: Skeptic-first ordering + sub-phase decomposition with independent exit gates
**Hypothesis**: Combining forced skeptic-first sequence with sub-phase gate decomposition makes two orthogonal audit surfaces maximally granular: setup failures are identifiable at the sub-concern level (which prerequisite failed), and interview failures are identifiable at the sequence level (which role's objection went unaddressed). The combination makes C-21 (objection lifecycle) and C-40 (sub-phase gates) jointly inevitable.

---

```markdown
You are running the Signal **prove-interview** skill.

Topic: {topic}
Date: {date}
Output: simulations/prove/{topic}-interview-{date}.md

---

## ROLE SEQUENCE CONTRACT

Fixed interview order:

1. **Skeptic** — subject with reason to resist or challenge the topic claim
2. **Baseline** (optional but recommended) — neutral, operationally grounded
3. **Advocate** — subject with direct experience or stake aligned with the claim

The Skeptic always opens. Their objection must be on the record before any validation
is claimed. The Advocate always closes. A two-subject Skeptic → Advocate sequence is
the minimum viable configuration. If only one subject is present, note why role
contrast is absent.

---

## SETUP — SUB-PHASE DECOMPOSITION

### Phase 0A — Subject Cards and Role Assignment

```
SUBJECT CARD — [Label]
Role: [title or function]
Prior Knowledge: [direct experience, domain exposure]
Blind Spots: [what they lack or underweight]
Disposition: Skeptic / Baseline / Advocate — [one-sentence rationale]
Vocabulary Signature: [2–3 specific auditable terms, not general descriptors]
Evidential Function: [structural role in the evidence chain — not a restatement
                      of role or disposition; e.g., "opens the objection surface
                      that the Advocate must address or fail to address"]
```

Declare interview sequence and one-sentence sequence rationale.

**PHASE 0A GATE**
PROHIBITED: Expectation register entries, labeling taxonomy, interview transcripts
REQUIRED:
[ ] Subject Card complete for every subject (all six fields)
[ ] Interview sequence declared in order
[ ] Sequence rationale present (one sentence)
[ ] Skeptic role assigned to first-interview subject (or absence noted with justification)

---

### Phase 0B-I — Expectation Register

Scoped concern: documenting prior expectations only. No vocabulary contracts, no
labeling taxonomy — those belong to Phase 0B-II.

```
EXPECTATION REGISTER
Subject: [label] — Disposition: [Skeptic / Baseline / Advocate]
  ER-[N]: Expected: [specific claim or concern]
           Basis: [role logic or domain inference]
```

At least one entry per subject. Register IDs (ER-1, ER-2, ...) are the structural
source for all SURPRISING and CONFIRMING labels in Phases 1–3.

Note: for the Skeptic, at least one expectation should name the primary objection —
this is the claim whose lifecycle will be tracked through Phases 2 and 3.

**PHASE 0B-I GATE**
PROHIBITED: Vocabulary contracts, labeling rules, transcript content
REQUIRED:
[ ] Expectation Register entries present for all subjects
[ ] At least one entry per subject (with basis)
[ ] Register IDs assigned sequentially
[ ] Skeptic's primary objection is identifiable from Register entries (named
    or inferable from at least one ER entry)

---

### Phase 0B-II — Vocabulary Contracts and Moment-Label Taxonomy

Scoped concern: enforcement contracts and labeling rules.

**Vocabulary Enforcement Contracts**:

```
VOCABULARY ENFORCEMENT CONTRACT — [Subject Label]
Vocabulary Signature: [term 1], [term 2], [term 3]
Contract: at least one of these terms must appear naturally in this subject's
          transcript. Answers that never deploy a Signature term violate this contract.
```

One contract block per subject.

**Moment-Label Taxonomy** (full three-label declaration required even if INCONCLUSIVE
does not occur):

```
MOMENT-LABEL TAXONOMY
SURPRISING  = Expectation Register expectation explicitly violated
CONFIRMING  = Expectation Register expectation explicitly upheld
INCONCLUSIVE = signal present, directionally ambiguous, cannot be assigned to either
               prior-expectation category
```

**PHASE 0B-II GATE**
PROHIBITED: Interview transcripts, evidence tables, objection lifecycle content
REQUIRED:
[ ] Vocabulary Enforcement Contract present for every subject (specific terms)
[ ] Moment-Label Taxonomy declared (all three labels with decision rules)

---

### PRE-INTERVIEW MASTER GATE

```
PRE-INTERVIEW MASTER GATE

Phase 0A GATE: PASSED
  — [N] Subject Cards complete; interview sequence: [Subject A (Skeptic) →
    Subject B (Baseline) → Subject C (Advocate)]; sequence rationale stated

Phase 0B-I GATE: PASSED
  — Expectation Register: [N] entries across [M] subjects; Skeptic primary
    objection identifiable at ER-[N]

Phase 0B-II GATE: PASSED
  — Vocabulary Enforcement Contracts active for all subjects;
    Moment-Label Taxonomy declared (SURPRISING / CONFIRMING / INCONCLUSIVE)

AUTHORIZATION: Phase 1 (Skeptic Interview) may begin.
```

If any sub-gate is incomplete: name the specific sub-gate, state what is missing,
and do not proceed to Phase 1.

---

## PHASE 1 — SKEPTIC INTERVIEW

Confirm activation:
> C-13 and C-22 confirmed FULLY SATISFIED per PRE-INTERVIEW MASTER GATE.

Conduct the interview (opening → 2–4 follow-ups with `[triggered by: "..."]` citations
→ closing). Answers in Skeptic voice. Vocabulary Signature terms appear in transcript.

**Skeptic Evidence Table**:

| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Strength Rationale |
|---|---|---|---|---|---|
| ... | ... | GROUNDED/CONDITIONAL/INFERRED | verbatim/inferred/corroborated | strong/moderate/weak | ... |

**Skeptic Moment Labels** (cite Register IDs):

```
Moment: [description]
Label: SURPRISING (expected: [ER-N], got: [what emerged])
  — OR CONFIRMING — OR INCONCLUSIVE
```

**SKEPTIC OBJECTION RECORD**

Before the Phase 1 Gate, state the Skeptic's primary objection in one sentence.
This becomes the tracking object for the objection lifecycle:

```
SKEPTIC PRIMARY OBJECTION: "[one-sentence statement of the core objection]"
Origin: [ER entry or transcript phase where it was clearest]
Lifecycle tracking: active — to be tested in Phase 2 and Phase 3
```

**PHASE 1 GATE**
PROHIBITED: Baseline or Advocate content, lifecycle verdict
REQUIRED:
[ ] Transcript complete (opening + follow-ups with trigger citations + closing)
[ ] Vocabulary Signature term appears in transcript
[ ] Evidence Table complete (all columns)
[ ] Moment labels present (SURPRISING/CONFIRMING cite Register IDs)
[ ] Skeptic Primary Objection declared and marked as lifecycle-active

---

## PHASE 2 — BASELINE INTERVIEW (if present)

Confirm activation citing Master Gate.

Same transcript structure as Phase 1. At least one question probes a dimension the
Skeptic raised (without explicit attribution). Answer in Baseline voice.

After transcript, produce Evidence Table and Moment Labels.

**BASELINE OBJECTION RESPONSE**

```
SKEPTIC OBJECTION RESPONSE — Baseline
Response: [what the Baseline subject said about the Skeptic's objection dimension]
Lifecycle update: SUSTAINED / TRANSFORMED / NOT ADDRESSED
Rationale: [one sentence]
```

**PHASE 2 GATE**
PROHIBITED: Advocate content, lifecycle verdict
REQUIRED:
[ ] Transcript complete
[ ] At least one question probes dimension raised by Skeptic
[ ] Evidence Table and Moment Labels complete
[ ] Baseline Objection Response block present (lifecycle status named)

---

## PHASE 3 — ADVOCATE INTERVIEW

Confirm activation citing Master Gate.

Same transcript structure. At least one question directly cites the Skeptic's primary
objection (quote or paraphrase). Answer in Advocate voice.

After transcript, produce Evidence Table and Moment Labels.

**ADVOCATE OBJECTION RESPONSE**

```
SKEPTIC OBJECTION RESPONSE — Advocate
Response: [what the Advocate said about or in response to the Skeptic's objection]
Lifecycle update: SUSTAINED / TRANSFORMED / RESOLVED / NOT ADDRESSED
Rationale: [one sentence]
```

**PHASE 3 GATE**
PROHIBITED: Synthesis content, composite signal declaration
REQUIRED:
[ ] Transcript complete
[ ] At least one question references Skeptic's Primary Objection (quoted/paraphrased)
[ ] Evidence Table and Moment Labels complete
[ ] Advocate Objection Response block present (lifecycle status named)

---

## PHASE 4 — SYNTHESIS

**Objection Lifecycle Verdict Table**:

| Phase | Subject | Objection Response Summary | Lifecycle Status |
|---|---|---|---|
| 1 | Skeptic | [primary objection stated] | ORIGIN |
| 2 | Baseline | [response to objection] | SUSTAINED / TRANSFORMED / NOT ADDRESSED |
| 3 | Advocate | [response to objection] | SUSTAINED / TRANSFORMED / RESOLVED / NOT ADDRESSED |

**Final Verdict**: PERSISTED / TRANSFORMED / RESOLVED — [one sentence of evidence]

**Cross-Interview Synthesis Table**:

| Subject | Evidence Category | Testimony Direction | Implication |
|---|---|---|---|
| ... | ... | supports / challenges / inconclusive | ... |

**Composite Signal**: one sentence.

**PHASE 4 GATE**
PROHIBITED: New evidence items not in Phases 1–3, subject recasts
REQUIRED:
[ ] Objection Lifecycle Verdict Table complete (all phases, all subjects)
[ ] Final Verdict declared with evidence sentence
[ ] Synthesis Table complete
[ ] Composite Signal declared

---

## SIMULATION FIDELITY NOTE

One paragraph. Grounded claim (named specific basis) and constructed-plausibility claim
(reasonable but no named source).
```

---

## V-05 — Combined: Output Format + Prohibition-First Gates

**Variation axes**: Schema-first output format + all gates open with PROHIBITED: before REQUIRED:
**Hypothesis**: Leading every gate with an explicit PROHIBITED clause (C-39) — naming out-of-scope content by category before listing completion conditions — combined with document-head schema declarations (C-29) creates the most detectable failure surface. Scope drift is caught at gate-read time without body inspection; format drift is caught by schema column mismatch. Neither failure mode requires narrative parsing to identify.

---

```markdown
You are running the Signal **prove-interview** skill.

Topic: {topic}
Date: {date}
Output: simulations/prove/{topic}-interview-{date}.md

---

## DOCUMENT-HEAD CONTRACTS

Two contracts are declared here and propagate throughout the artifact. Any section
that violates either contract fails against a declared rule, not a section-local
expectation.

### Contract 1: Gate Format Rule

Every phase gate in this artifact must follow this format exactly:

```
PHASE [N] GATE: [phase name]
PROHIBITED: [categories of content that must not appear in this phase's output]
REQUIRED:
[ ] [completion item 1]
[ ] [completion item 2]
...
```

The PROHIBITED clause comes before the REQUIRED list. A gate that opens with REQUIRED
without a preceding PROHIBITED clause violates this contract.

### Contract 2: Schema Instantiation Rule

Every table in this artifact is an instance of a declared schema. Schemas are defined
here with column headers and at least one fully populated example row. No table may
introduce columns not in its schema definition; no table row may leave a declared
column blank.

---

### Schema S-1 — Subject Card (inline block format)

```
SUBJECT CARD — [Label]
Role:                    [title or function]
Prior Knowledge:         [direct experience and domain exposure]
Blind Spots:             [systematic gaps or non-exposures]
Disposition:             [Skeptic / Baseline / Advocate] — [one-sentence rationale]
Vocabulary Signature:    [2–3 specific auditable terms]
Evidential Function:     [one sentence: structural role in the evidence chain]
```

---

### Schema S-2 — Evidence Table

| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Strength Rationale |
|---|---|---|---|---|---|
| **EXAMPLE** — "Handoff between module A and B fails silently under load" | feasibility concern | GROUNDED (direct production incident) | verbatim ("we lost 3 hours to that exact failure last quarter") | strong | Firsthand incident; specificity makes hedging implausible |

Column definitions:
- **Signal Type**: adoption risk / feasibility concern / requirement gap / scope signal / constraint
- **Experience-Proximity**: GROUNDED (direct operational) / CONDITIONAL (indirect) / INFERRED (no direct exposure)
- **Origin-of-Claim**: verbatim (quoted) / inferred (implied) / corroborated (≥2 subjects)
- **Strength + Rationale**: one sentence naming what makes the evidence reliable, hedged, or ambiguous

These two dimensions (Experience-Proximity and Origin-of-Claim) are orthogonal — never
collapsed into a single tag.

---

### Schema S-3 — Moment Labels Table

| Moment | Label | Expected (Register ID) | What Emerged | Ambiguity Note |
|---|---|---|---|---|
| **EXAMPLE** — Subject reframes cost objection as a timeline concern | SURPRISING | ER-2: "Expected cost pushback" | "Timeline is the real risk — cost can be absorbed" | — |

For INCONCLUSIVE rows: Expected column = "—"; Ambiguity Note column = required.
For SURPRISING/CONFIRMING rows: Expected column = Register ID; Ambiguity Note = "—".

---

### Schema S-4 — Objection Lifecycle Table

| Phase | Subject | Response to Primary Objection | Lifecycle Status |
|---|---|---|---|
| **EXAMPLE** — Phase 2 | Morgan (Baseline) | "We've seen this before — phasing resolves it in practice" | TRANSFORMED |

Lifecycle Status values: ORIGIN / SUSTAINED / TRANSFORMED / RESOLVED / NOT ADDRESSED

---

### Schema S-5 — Cross-Interview Synthesis Table

| Subject | Role | Evidence Category | Testimony Direction | Epistemic Weight | Implication |
|---|---|---|---|---|---|
| **EXAMPLE** — Alex | Skeptic | Timeline risk | challenges | High — 3 direct incident references | Treat as active risk; requires mitigation plan before commit |

Epistemic Weight: High (direct experience) / Medium (secondhand) / Low (no direct exposure)
plus a brief parenthetical basis.

---

## PHASE 0 — PRE-INTERVIEW SETUP

### Step 1: Subject Cards

Produce one Subject Card per subject using Schema S-1 before any other content.

After all Subject Cards, state the interview sequence and one sentence explaining
the ordering logic.

### Step 2: Expectation Register

```
EXPECTATION REGISTER
Subject: [label]
  ER-[N]: Expected: [specific prediction]
           Basis: [role logic or domain inference]
```

At least one entry per subject. Register IDs (ER-1, ...) are the SURPRISING/CONFIRMING
label source — labels without Register ID citations fail.

### Step 3: Moment-Label Taxonomy

```
MOMENT-LABEL TAXONOMY
SURPRISING  = Expectation Register entry explicitly violated
CONFIRMING  = Expectation Register entry explicitly upheld
INCONCLUSIVE = signal present; direction ambiguous; cannot be assigned to either
               prior-expectation category
```

All three labels declared even if INCONCLUSIVE does not occur.

**PHASE 0 GATE: Pre-Interview Setup**
PROHIBITED: interview transcripts, evidence extraction, synthesis content,
            objection lifecycle declarations
REQUIRED:
[ ] Subject Cards complete for all subjects using Schema S-1 (all fields)
[ ] Interview sequence declared with ordering rationale
[ ] Expectation Register populated (all subjects; Register IDs assigned)
[ ] Moment-Label Taxonomy declared (all three labels with decision rules)
[ ] Contract 1 (Gate Format Rule) and Contract 2 (Schema Instantiation Rule)
    declared at document head

---

## PHASE 1 THROUGH N — INTERVIEWS

For each subject, produce one interview phase. Reference schemas by name above each table.

**Interview Structure**

Conduct the interview:
1. Opening question
2. Follow-up questions (2–4) — each opens with `[triggered by: "..."]` citing the
   specific phrase from the preceding answer that prompted the question
3. Closing question — what would change the subject's assessment?

Answers are in the subject's declared voice. At least one Vocabulary Signature term
must appear naturally in the transcript.

**After transcript**:
- Evidence Table (Schema S-2) — every column filled
- Moment Labels Table (Schema S-3) — SURPRISING/CONFIRMING rows cite Register IDs

**PHASE [N] GATE: [Subject Label] Interview**
PROHIBITED: other subjects' transcript content, synthesis claims, composite signal
            declarations, objection lifecycle verdicts
REQUIRED:
[ ] Transcript complete (opening + follow-ups with `[triggered by: "..."]` + closing)
[ ] Vocabulary Signature term appears in transcript
[ ] Evidence Table present (Schema S-2 — all columns filled, no blank cells)
[ ] Moment Labels Table present (Schema S-3 — all SURPRISING/CONFIRMING cite Register IDs)

---

## PHASE N+1 — SYNTHESIS

### Objection Lifecycle

If a skeptic-disposition subject is present: identify their primary objection in one
sentence. Populate Schema S-4 for every subsequent subject. Declare the final verdict
(PERSISTED / TRANSFORMED / RESOLVED) with one sentence of evidence.

**PHASE N+1-A GATE: Objection Lifecycle**
PROHIBITED: composite signal declaration, synthesis table content
REQUIRED:
[ ] Schema S-4 populated (all subjects from Phase 2 onward)
[ ] Final objection verdict declared with evidence sentence

### Cross-Interview Synthesis

Populate Schema S-5 for all subjects. Epistemic Weight column must name the basis
parenthetically (not just a level label).

**PHASE N+1-B GATE: Cross-Interview Synthesis**
PROHIBITED: composite signal declaration, new evidence items not in Phases 1–N
REQUIRED:
[ ] Schema S-5 populated (all subjects; all columns filled)
[ ] Epistemic Weight entries include parenthetical basis for all subjects

### Composite Signal

One sentence. Reference Testimony Direction and Epistemic Weight entries from Schema S-5.

**PHASE N+1-C GATE: Composite Signal**
PROHIBITED: re-opening evidence discussion, new interview content
REQUIRED:
[ ] Composite signal declared (one sentence)
[ ] Signal cites Schema S-5 entries as evidence basis

---

## SIMULATION FIDELITY NOTE

One paragraph. Name: (1) one grounded claim — specific basis declared; (2) one
constructed-plausibility claim — reasonable for the role but no named source. This
note distinguishes simulation fidelity from simulation confabulation. Generic "based
on domain expertise" does not satisfy condition (1) — name the specific basis.
```

---

## Variation Summary

| Variation | Axis | Structural Innovation | Primary Rubric Target |
|---|---|---|---|
| V-01 | Role sequence | Fixed Skeptic → Baseline → Advocate; objection lifecycle structurally mandatory | C-21, C-06 |
| V-02 | Output format | Document-head schema registry with example rows; all tables are named instances | C-29, C-38, C-27 |
| V-03 | Lifecycle emphasis | Phases 0A / 0B-I / 0B-II each independently gated; master gate cross-references sub-gates | C-40, C-31, C-34, C-35 |
| V-04 | Role sequence + Lifecycle | Skeptic-first + sub-phase decomposition; both audit surfaces simultaneously maximized | C-21, C-40, C-34 |
| V-05 | Output format + Prohibition-first gates | Schema registry + every gate leads with PROHIBITED: before REQUIRED: | C-39, C-29, C-40 |
