# prove-interview — Prompt Variations V-01 through V-05 (Round 17)

---

## V-01 — Axis: Role Sequence | Hypothesis: Skeptic-first ordering extracts sharper objections before advocates can frame the conversation, producing a richer objection lifecycle to track across the full sequence.

```
## DOCUMENT CONTRACT (declared here, cited throughout)

Sub-schemas assigned handles below. Every gate item with a format requirement cites its handle inline.

**0.1 GATE FORMAT** — Named block: `PHASE N GATE — PROHIBITED: [categories] — REQUIRED: [ ] item (→ 0.N)`
**0.2 EVIDENCE SCHEMA** — Columns: `ID | Claim | Signal Type | Strength (rationale) | Origin-of-Claim | Experience-Proximity | Framework Dimension`
**0.3 MOMENT-LABEL FORMAT** — `SURPRISING (expected: [Expectation Register → field], got: [emergence])` | `CONFIRMING (validates: [Register → field])` | `INCONCLUSIVE (signal: [what appeared], ambiguity: [why undecidable])`
**0.4 SUBJECT CARD SCHEMA** — `Role | Prior Knowledge | Blind Spots | Disposition | Vocabulary Signature (3 terms) | Evidential Function | Sequence Position & Rationale`

**SEQUENCE RULE (enforced, not suggested):** Interview subjects in this order: SKEPTIC → NEUTRAL / CHALLENGER → ADVOCATE. Rationale: objections must surface before advocates can frame the conversation. The final synthesis tracks the skeptic's initial objection across all three interviews to determine whether it persisted, transformed, or was resolved.

---

## PHASE 0A — SUBJECT CARD SET

For each of three subjects (Skeptic, Neutral/Challenger, Advocate), produce a card using schema 0.4.

Each card must declare:
- **Role**: title and function
- **Prior Knowledge**: what they know, what they've seen firsthand
- **Blind Spots**: what they have not encountered or have reasoned about secondhand only
- **Disposition**: their orientation toward the feature (resistant / neutral-questioning / favorable)
- **Vocabulary Signature**: exactly 3 role-specific terms that will appear in their interview answers — terms distinctive enough to spot-check authenticity
- **Evidential Function**: what this subject's position *does* for the evidence structure (not just who they are) — e.g., "establishes the baseline objection surface against which subsequent interviews are measured"
- **Sequence Position & Rationale**: why they appear in position 1, 2, or 3

PHASE 0A GATE — PROHIBITED: interview transcripts, evidence items, expectation entries — REQUIRED:
[ ] Three subject cards fully populated per 0.4 schema
[ ] Vocabulary signatures: 3 terms per subject, terms named (not described)
[ ] Evidential function stated as structural contribution, not role restatement
[ ] Sequence rationale named for each position

---

## PHASE 0B — EXPECTATION REGISTER

Produce a table with columns: `Subject | Expectation ID | What I expect them to say | Basis for expecting this`.

Populate before any transcript. This register is the authoritative source for the "expected:" slot in every 0.3 moment label. Each subject must have at least 2 entries.

PHASE 0B GATE — PROHIBITED: moment labels, interview content — REQUIRED:
[ ] Register table produced with all four columns (→ 0.3)
[ ] Minimum 2 expectations per subject
[ ] Each expectation names an explicit basis (prior literature, persona archetype, domain pattern)

---

## PHASE 0C — MOMENT-LABEL DECISION TAXONOMY

Declare the complete three-label system with decision rules for each label. This declaration governs all moment labels in Phases 1–3.

- **SURPRISING**: prior expectation violated — the subject said something that contradicts a Register entry
- **CONFIRMING**: prior expectation upheld — the subject said something that matches a Register entry
- **INCONCLUSIVE**: signal present but directionally ambiguous — cannot be assigned to either category

Declaration must appear before Phase 1 begins. Any moment labeled without consulting this taxonomy fails.

PHASE 0C GATE — PROHIBITED: interview transcripts — REQUIRED:
[ ] All three labels declared with decision rules (→ 0.3)
[ ] Decision rule for INCONCLUSIVE explicitly names the ambiguity condition (not just "unclear")

---

## PRE-INTERVIEW MASTER GATE

Before Phase 1 begins, confirm collectively:

[ ] Phase 0A Subject Card Set: COMPLETE (3 cards, all fields populated — per 0.4)
[ ] Phase 0B Expectation Register: COMPLETE (register table, min 2 entries per subject — per 0.3)
[ ] Phase 0C Moment-Label Taxonomy: COMPLETE (3-label system declared with decision rules — per 0.3)
[ ] Vocabulary signatures declared for all subjects (will be verified in transcript — per 0.4)

All four gates passed. Phase 1 authorized.

---

## PHASE 1 — SUBJECT 1 INTERVIEW (SKEPTIC)

**Interview opens with**: the skeptic's role, prior knowledge summary (one sentence), and disposition.

Run 4–6 questions. At least one follow-up must reference a specific phrase from the preceding answer — cite the phrase in brackets before the follow-up question: `[triggered by: "exact phrase"] Follow-up: ...`

Answers must be written in the skeptic's vocabulary — at least one of their 3 declared vocabulary signature terms must appear naturally in their answers.

After the transcript, produce the evidence extraction table using 0.2 schema. Then label moments using 0.3 format, citing the Expectation Register by expectation ID in each label's "expected:" slot.

PHASE 1 GATE — PROHIBITED: synthesis content, comparison to other subjects — REQUIRED:
[ ] Transcript: at least one follow-up with `[triggered by: ...]` citation (→ 0.3)
[ ] At least one vocabulary signature term appears in transcript (→ 0.4)
[ ] Evidence table: all 0.2 columns populated for each row (→ 0.2)
[ ] At least one moment labeled using 0.3 format with Register citation
[ ] At least one SURPRISING or INCONCLUSIVE label present (skeptic rarely only confirms)

---

## PHASE 2 — SUBJECT 2 INTERVIEW (NEUTRAL/CHALLENGER)

Same structure as Phase 1. The neutral/challenger's evidential function is to test the skeptic's claims from a less committed position — their testimony either adds texture to the objection or reveals the skeptic's position as more extreme than warranted.

PHASE 2 GATE — PROHIBITED: synthesis, comparison across all three subjects — REQUIRED:
[ ] Transcript: at least one follow-up with `[triggered by: ...]` citation (→ 0.3)
[ ] At least one vocabulary signature term in transcript (→ 0.4)
[ ] Evidence table: 0.2 schema applied (→ 0.2)
[ ] At least one moment labeled per 0.3 format with Register citation

---

## PHASE 3 — SUBJECT 3 INTERVIEW (ADVOCATE)

Same structure. The advocate's evidential function is to provide the strongest case for the feature — their testimony must be tested against the skeptic's opening objections, not treated as standalone validation.

PHASE 3 GATE — REQUIRED:
[ ] Transcript: follow-up with `[triggered by: ...]` citation (→ 0.3)
[ ] Vocabulary signature term in transcript (→ 0.4)
[ ] Evidence table: 0.2 schema applied (→ 0.2)
[ ] At least one moment labeled per 0.3 format

---

## PHASE 4 — CROSS-INTERVIEW SYNTHESIS

Produce a named synthesis artifact: **INTERVIEW SYNTHESIS GRID**

Schema columns: `Subject | Framework Dimension | Testimony Direction (supports / challenges / inconclusive) | Implication for Feature Decision`

After the grid, write the **Objection Lifecycle Trace**: did the skeptic's primary objection (named in Phase 1) *persist*, *transform*, or *get resolved* by the time Phase 3 closed? Name the specific moment in Phase 2 or 3 that determined the outcome.

PHASE 4 GATE — REQUIRED:
[ ] Synthesis grid: named artifact, all four columns, all subjects represented
[ ] Objection lifecycle trace: names outcome (persist / transform / resolve) and cites the specific Phase 2 or 3 moment
[ ] At least one evidence item's weight explicitly adjusted for experience-proximity difference across subjects

---

## PHASE 5 — SIMULATION FIDELITY NOTE

Write a brief meta-note (3–5 sentences) distinguishing grounded claims (based on documented persona knowledge or domain context) from constructed plausibility. Name at least one specific basis (e.g., a known role pattern, a domain constraint, a documented adoption friction category).

Then write a voice divergence acknowledgment: name one concrete vocabulary choice, framing preference, or concern priority that distinguishes the skeptic from the advocate — something a reader could spot-check against the transcripts.
```

---

## V-02 — Axis: Output Format (Schema-First Tables) | Hypothesis: Declaring all schema column contracts before any content is filled forces structural compliance into the output's skeleton, making rubric coverage architecturally inevitable rather than authorial.

```
## FORMAT CONTRACT — SCHEMA REGISTRY

All schemas are declared in this registry before any content is produced. Every section that generates structured output cites the schema ID it instantiates.

---

**SCHEMA A: SUBJECT CARD**
Columns: `Subject ID | Role & Title | Prior Knowledge | Blind Spots | Disposition | Vocabulary Signature [Term 1, Term 2, Term 3] | Evidential Function`

Example row (required before content rows):
| S-01 | [Role] | [what they know firsthand] | [what they lack] | [resistant / neutral / favorable] | [Term 1], [Term 2], [Term 3] | [structural contribution to evidence chain] |

---

**SCHEMA B: EXPECTATION REGISTER**
Columns: `Exp ID | Subject ID | Expected Claim | Basis | Violated? (filled after interview)`

Example row:
| E-01 | S-01 | [what I expect subject to say] | [why I expect this] | [SURPRISING / CONFIRMING / INCONCLUSIVE — filled in Phase N] |

---

**SCHEMA C: EVIDENCE TABLE**
Columns: `Ev ID | Claim | Signal Type | Strength | Strength Rationale | Origin-of-Claim [verbatim / inferred / corroborated] | Experience-Proximity [GROUNDED / CONDITIONAL / INFERRED] | Subject ID`

Example row:
| EV-01 | [claim text] | [adoption risk / feasibility concern / requirement gap / scope signal / constraint] | [strong / moderate / weak] | [one sentence] | [verbatim] | [GROUNDED] | S-01 |

---

**SCHEMA D: MOMENT LABEL**
Format: `LABEL-NN: [SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Exp ID → field], got: [what emerged])` or for INCONCLUSIVE: `LABEL-NN: INCONCLUSIVE (signal: [observed], ambiguity: [why undecidable])`

Three-label decision rules:
- **SURPRISING**: expected claim (Schema B) is violated
- **CONFIRMING**: expected claim (Schema B) is upheld
- **INCONCLUSIVE**: signal present but cannot be assigned to either category

Example instantiation (required before use):
`LABEL-01: SURPRISING (expected: E-01 → "subject will object to complexity", got: "subject focused entirely on integration cost, not complexity")`

---

**SCHEMA E: SYNTHESIS GRID**
Columns: `Subject ID | Evidence Category | Testimony Direction [supports / challenges / inconclusive] | Weight Adjustment [if experience-proximity differs across subjects] | Implication`

Example row:
| S-01 | Adoption risk | challenges | Conditional (no direct operational experience with alternative) | Treat as risk to monitor, not blocker |

---

## SECTION 1 — SUBJECT CARDS (Schema A)

Produce three subject cards. Populate the Schema A table with three content rows (after the example row). Each vocabulary signature must name exactly 3 terms that are distinctive enough to spot-check in the transcript.

**Evidential function** must describe the structural role in the evidence chain — not restate the disposition. Examples of passing evidential functions: "establishes the initial objection surface that subsequent interviews either reinforce or erode", "provides conditional testimony from someone who has reasoned about the feature but not deployed it", "closes the evidence chain with advocacy grounded in direct prior experience".

SECTION 1 COMPLETE WHEN:
[ ] Schema A table: example row present, 3 content rows fully populated
[ ] All vocabulary signatures: exactly 3 named terms per subject
[ ] All evidential functions: structural contribution named, not role-restatement

---

## SECTION 2 — EXPECTATION REGISTER (Schema B)

Produce the Schema B table with at least 2 rows per subject (6 rows minimum). The "Violated?" column is left blank here — it will be filled by moment labels during interviews.

The register is the sole authoritative source for the "expected:" slot in all Schema D moment labels.

SECTION 2 COMPLETE WHEN:
[ ] Schema B table: example row present, min 6 content rows (2 per subject)
[ ] "Violated?" column: blank (not pre-filled)

---

## SECTION 3 — INTERVIEW SEQUENCE

For each subject (S-01, S-02, S-03), produce:

**3.N.1 Interview Transcript**

Open with: subject role (one sentence). Then run 4–6 questions. At least one follow-up question per subject must cite the triggering phrase: `[triggered by: "exact phrase"] Follow-up: ...`

Answers must be in the subject's declared voice — vocabulary signature terms must appear in their answers.

**3.N.2 Evidence Table (Schema C)**

Produce a Schema C table for this subject. Include example row, then content rows. Populate all columns. The Origin-of-Claim and Experience-Proximity columns use the declared taxonomy — do not conflate them (Origin-of-Claim answers "how derived from transcript"; Experience-Proximity answers "how close to direct operational experience").

**3.N.3 Moment Labels (Schema D)**

Produce labeled moments using Schema D format. Each label cites an Expectation Register entry by ID. After labeling, fill in the "Violated?" column in the Schema B table for the expectations triggered.

At least one INCONCLUSIVE label must appear across all subjects, OR an explicit note states that every labeled moment was unambiguously SURPRISING or CONFIRMING.

---

## SECTION 4 — CROSS-INTERVIEW SYNTHESIS (Schema E)

Title this section: **INTERVIEW SYNTHESIS GRID**

Produce the Schema E table. Every evidence item from Sections 3.1–3.3 that bears cross-subject relevance appears as a row. At least one row must name an explicit weight adjustment based on experience-proximity differences.

After the table, write an **Objection Lifecycle Trace** (prose): name the skeptic's primary objection from S-01, then state whether it *persisted*, *transformed*, or *was resolved* across the full sequence, citing the specific row or moment that determined the outcome.

---

## SECTION 5 — SIMULATION FIDELITY

Two named paragraphs:

**Fidelity Note**: Distinguish grounded claims (based on documented role knowledge, domain patterns, or established adoption research) from constructed plausibility. Name at least one specific basis.

**Voice Divergence**: Name one concrete vocabulary choice, framing preference, or concern priority that distinguishes two subjects — cite the specific term or phrase and where in the transcripts it appears.
```

---

## V-03 — Axis: Lifecycle Emphasis (Gate-Heavy Phases) | Hypothesis: Making every phase boundary explicit with PROHIBITED/REQUIRED gate blocks and sub-gate cross-references in the master gate prevents phase bleeding and forces complete setup before interviews begin.

```
You are running a structured interview simulation. The output is divided into named phases. Each phase closes with a gate block. No phase may begin until its predecessor's gate is confirmed.

---

## DOCUMENT-HEAD FORMAT RULE

All gates in this document use the following format, declared once here and propagated:

```
PHASE [N] GATE: [PHASE NAME]
PROHIBITED: [content categories that cannot pass through]
REQUIRED:
[ ] [item description — per 0.N if format-governed]
[ ] [item description]
GATE STATUS: [ ] OPEN / [x] CLOSED
```

Sub-schema handles cited inline at gate items:
- **0.1** = gate format (this rule)
- **0.2** = evidence table schema (ID | Claim | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity)
- **0.3** = moment-label format (`LABEL: SURPRISING (expected: [Reg ID → text], got: [emergence])`)
- **0.4** = subject card schema (Role | Prior Knowledge | Blind Spots | Disposition | Vocabulary [3 terms] | Evidential Function)

---

## PHASE 0A — SUBJECT CARD POPULATION

For 3 subjects, produce full subject cards per 0.4 schema. Each card is a structured block, not prose. Vocabulary signature must name exactly 3 terms. Evidential function must name the structural contribution to the evidence chain (not restate disposition).

```
PHASE 0A GATE: SUBJECT CARD POPULATION
PROHIBITED: expectation entries, interview questions, evidence items, moment labels
REQUIRED:
[ ] Three subject cards structured per 0.4 schema
[ ] Vocabulary signatures: 3 named terms per subject — not descriptors (→ 0.4)
[ ] Evidential function: structural contribution named for each subject (→ 0.4)
[ ] Subject sequence order declared with rationale sentence
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PHASE 0B — EXPECTATION REGISTER POPULATION

Produce a register table: `Exp ID | Subject ID | Expected Claim | Basis`. Minimum 2 entries per subject. This register is the sole source for the "expected:" slot in all 0.3 moment labels. Do not populate the "Violated?" column here.

```
PHASE 0B GATE: EXPECTATION REGISTER POPULATION
PROHIBITED: moment labels, interview transcripts, synthesis content
REQUIRED:
[ ] Register table with columns: Exp ID | Subject ID | Expected Claim | Basis
[ ] Minimum 2 entries per subject (6 rows minimum)
[ ] "Violated?" column: omitted or blank — not pre-filled
[ ] Register declared as authoritative source for 0.3 "expected:" slot (→ 0.3)
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PHASE 0C — MOMENT-LABEL DECISION TAXONOMY DECLARATION

Declare the complete three-label system as a formal decision taxonomy. Rules:

- **SURPRISING**: Register expectation violated
- **CONFIRMING**: Register expectation upheld
- **INCONCLUSIVE**: signal present but directionally ambiguous; cannot be assigned to either prior-expectation category

All three rules must be declared even if INCONCLUSIVE is not ultimately used.

```
PHASE 0C GATE: MOMENT-LABEL TAXONOMY DECLARATION
PROHIBITED: interview transcripts, evidence tables
REQUIRED:
[ ] SURPRISING decision rule declared (→ 0.3)
[ ] CONFIRMING decision rule declared (→ 0.3)
[ ] INCONCLUSIVE decision rule declared — names ambiguity condition explicitly (→ 0.3)
[ ] Taxonomy declared as governing system for Phases 1–3
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PRE-INTERVIEW MASTER GATE

This gate synthesizes closure of all setup phases. It cross-references named phase gates — it does not re-assert contents.

```
PRE-INTERVIEW MASTER GATE
PROHIBITED: interview content of any kind
REQUIRED (evidenced by named phase gate closures):
[ ] Phase 0A GATE: CLOSED — Subject Card Population complete (3 cards, 0.4 schema, vocabulary, evidential function)
[ ] Phase 0B GATE: CLOSED — Expectation Register populated (min 6 entries, authoritative source declared)
[ ] Phase 0C GATE: CLOSED — Moment-Label Taxonomy declared (3 labels, 3 decision rules)
[ ] Cross-check: vocabulary signatures declared for all subjects — transcript verification pending Phase 1–3
MASTER GATE STATUS: [ ] OPEN / [x] CLOSED
```

Phases 1–3 are authorized by master gate closure. If any prerequisite gate is not closed, stop and resolve before proceeding.

---

## PHASE 1 — SUBJECT 1 INTERVIEW

Open with subject identity (role, knowledge scope) drawn from Phase 0A card. Run 4–6 questions. At least one follow-up must cite the triggering phrase using format `[triggered by: "exact phrase"] Follow-up: ...`.

Subject answers must use at least one of their 3 declared vocabulary signature terms naturally.

After transcript, produce evidence table per 0.2 schema (include example row). Then label moments per 0.3 format, citing Register entries by Exp ID in each label.

```
PHASE 1 GATE: SUBJECT 1 INTERVIEW + EVIDENCE EXTRACTION
PROHIBITED: synthesis across subjects, comparison to Phase 2 or 3 content
REQUIRED:
[ ] Transcript: at least one follow-up with `[triggered by: "exact phrase"]` citation (→ 0.3)
[ ] Vocabulary signature: at least 1 of 3 declared terms in transcript (→ 0.4)
[ ] Evidence table: 0.2 schema, example row present, all columns populated per row (→ 0.2)
[ ] Moment labels: 0.3 format, each cites Expectation Register by Exp ID (→ 0.3)
[ ] C-14 check: at least 1 INCONCLUSIVE label, OR explicit note that all moments were unambiguous
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PHASE 2 — SUBJECT 2 INTERVIEW

Same structure. This subject's evidential function (declared in Phase 0A) governs how their testimony relates to Phase 1 output — name the connection in the transcript opening.

```
PHASE 2 GATE: SUBJECT 2 INTERVIEW + EVIDENCE EXTRACTION
PROHIBITED: synthesis, objection lifecycle conclusions
REQUIRED:
[ ] Transcript: follow-up with `[triggered by: ...]` citation (→ 0.3)
[ ] Vocabulary signature: at least 1 declared term in transcript (→ 0.4)
[ ] Evidence table: 0.2 schema, all columns populated (→ 0.2)
[ ] Moment labels: 0.3 format, Register citations (→ 0.3)
[ ] Evidential function: connection to Phase 1 named in transcript opening
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PHASE 3 — SUBJECT 3 INTERVIEW

Same structure.

```
PHASE 3 GATE: SUBJECT 3 INTERVIEW + EVIDENCE EXTRACTION
PROHIBITED: synthesis conclusions
REQUIRED:
[ ] Transcript: follow-up with `[triggered by: ...]` citation (→ 0.3)
[ ] Vocabulary signature: at least 1 declared term in transcript (→ 0.4)
[ ] Evidence table: 0.2 schema, all columns populated (→ 0.2)
[ ] Moment labels: 0.3 format, Register citations (→ 0.3)
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PHASE 4 — CROSS-INTERVIEW SYNTHESIS GRID

Produce a named artifact: **INTERVIEW SYNTHESIS GRID**. Schema: `Subject | Evidence Category | Testimony Direction (supports / challenges / inconclusive) | Experience-Proximity Weight Adjustment | Implication`.

Include an objection lifecycle trace: name the primary objection surfaced in Phase 1, and state whether it *persisted*, *transformed*, or *was resolved* across Phases 2–3. Cite the specific transcript moment that determined the outcome.

```
PHASE 4 GATE: SYNTHESIS GRID
PROHIBITED: new interview content
REQUIRED:
[ ] Synthesis grid: named artifact, all 5 schema columns, all subjects represented
[ ] At least one row: explicit weight adjustment for experience-proximity difference named
[ ] Objection lifecycle trace: outcome (persist / transform / resolve) + moment citation
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PHASE 5 — FIDELITY NOTE + VOICE DIVERGENCE

**Fidelity Note**: Name at least one grounded claim (basis cited) and at least one constructed-plausibility claim.

**Voice Divergence**: Name one concrete vocabulary choice, framing preference, or concern priority that distinguishes two subjects — cite specific term and transcript location.

```
PHASE 5 GATE: SIMULATION CLOSE
REQUIRED:
[ ] Fidelity note: grounded / constructed distinction with specific basis
[ ] Voice divergence: concrete vocabulary or framing contrast, transcript-cited
GATE STATUS: [ ] OPEN / [x] CLOSED
```
```

---

## V-04 — Axes: Phrasing Register (Conversational Imperative) + Inertia Framing (Status-Quo Prominent) | Hypothesis: Conversational imperative lowers cognitive load for prompt execution; forcing every persona to position against current practice produces richer adoption-risk and displacement signals.

```
Run a simulated stakeholder interview. The simulation is fiction built on documented role knowledge — treat it as a disciplined thought experiment, not a transcript.

---

**Your four working formats** — declare them at the top, use them throughout:

- **Subject Card** captures: role, what they know, what they don't, how they feel about the feature, 3 words they'd use that others wouldn't, and what their testimony contributes to the evidence chain.
- **Expectation Register** captures: what you expect each subject to say, and why you expect it — one row per expectation, filled before any interview starts.
- **Moment Label** reads: `SURPRISING (expected: [Reg entry], got: [what emerged])` or `CONFIRMING (validates: [Reg entry])` or `INCONCLUSIVE (signal: [what appeared], ambiguity: [why it won't resolve])`.
- **Evidence Row** captures: claim, signal type, strength with rationale, how it was derived (verbatim / inferred / corroborated), and how close the subject is to direct operational experience (GROUNDED / CONDITIONAL / INFERRED).

---

**STEP 1 — Build your subject cards**

Pick three subjects with genuinely different relationships to the feature. The most important thing: make sure at least one of them is defending the current way of doing things. Their job is to explain why the status quo works well enough, or why changing it is riskier than it looks.

For each subject, write their card. In the "what they know" section, be specific about what experience they have with the current practice — what they've shipped using it, what they've fixed with it, how long they've lived with it. That context is what makes their answers credible.

In the vocabulary signature, name 3 terms they'd reach for that a different role wouldn't. These are your authenticity handles — you'll check them against the transcript later.

In the evidential function field, say what this subject's testimony *does* for the investigation — don't just describe who they are.

---

**STEP 2 — Build your expectation register**

Before you run a single question, write down at least 2 expectations per subject. For the status-quo defender especially, think hard: what objection will they make? What's their best argument for the current approach? Write that down. If you're not surprised later, you want to know you weren't surprised — and if you are surprised, you need the register to name the delta.

Format: table with Exp ID, Subject, Expected Claim, Basis.

---

**STEP 3 — Declare your labeling rules**

Three labels. State when each one applies:
- SURPRISING applies when a register expectation is violated
- CONFIRMING applies when a register expectation is upheld
- INCONCLUSIVE applies when there's a real signal but it won't resolve into either category

Declare all three even if you think INCONCLUSIVE won't come up. The declaration is a contract, not a prediction.

---

**STEP 4 — Run the interviews**

For each subject, in turn:

Open with a one-sentence reminder of who they are and what lens they're bringing.

Ask 4–6 questions. After any answer that contains a phrase you want to follow up on, surface it explicitly: `[triggered by: "exact phrase"] Follow-up: ...` — this keeps the conversation from floating.

Write their answers in their voice. At least one of their 3 vocabulary signature terms should appear naturally. If it doesn't surface organically, ask a question that makes it relevant.

**Status-quo pressure rule**: every interview must include at least one question that asks the subject to compare the feature against current practice. The status-quo defender will welcome this question. The feature advocate should have to work for their answer. The neutral subject will reveal something in the tension.

After the transcript, build the evidence table. For each row: what's the claim, what kind of signal is it (adoption risk, feasibility concern, requirement gap, scope signal, displacement risk, constraint), how strong is it and why, was it verbatim or inferred or corroborated, and how grounded is the subject in direct operational experience.

Then label the moments. Use the register entry ID in every label's "expected:" slot.

---

**STEP 5 — Synthesize**

After all three interviews, produce the **INTERVIEW SYNTHESIS GRID** — a table with columns: Subject | Evidence Category | Testimony Direction | Status-Quo Position (defends / agnostic / critiques current practice) | Implication.

The Status-Quo Position column is required: it tracks whether each subject's testimony ultimately defends, questions, or critiques the current approach. This is the adoption-risk signal in aggregate form.

After the grid, write the objection lifecycle trace: the status-quo defender surfaced an objection in their interview. Did it persist, transform, or get resolved by the time the third interview closed? Name the specific moment that determined the outcome.

Adjust at least one evidence item's weight explicitly for experience-proximity: if the person making the claim has never actually used the current practice in production, say so, and name what that means for how much weight to put on the claim.

---

**STEP 6 — Close with a simulation note**

Two short paragraphs:

First: distinguish what in this simulation is grounded (anchored to documented role patterns, known adoption barriers, established domain knowledge) from what is constructed plausibility. Name one specific anchor.

Second: name one concrete voice difference between two subjects — a specific term, a framing habit, a concern priority — something a reader could verify by skimming the transcripts.
```

---

## V-05 — Axes: Influence-Map Sequence + Artifact-Centric Phase Titles + Evidence Taxonomy Depth | Hypothesis: Ordering interviews by proximity-to-decision (closest influencer first, farthest last) and naming produced artifacts in phase titles makes the master gate's evidenced closure semantically self-describing without body inspection.

```
## DOCUMENT CONTRACT

Sub-schema handles — cited at every gate item with a format requirement:

**0.1 GATE FORMAT**: `PHASE N — [ARTIFACT NAME] GATE — PROHIBITED: [...] — REQUIRED: [ ] item (→ 0.N)`
**0.2 EVIDENCE SCHEMA**: `Ev ID | Claim | Signal Type | Strength [strong/moderate/weak] | Strength Rationale | Origin-of-Claim [verbatim/inferred/corroborated] | Experience-Proximity [GROUNDED/CONDITIONAL/INFERRED]`
**0.3 MOMENT-LABEL FORMAT**: `LABEL-NN: SURPRISING (expected: [Reg ID → text], got: [emergence])` | `LABEL-NN: CONFIRMING (validates: [Reg ID → text])` | `LABEL-NN: INCONCLUSIVE (signal: [observed], ambiguity: [undecidability reason])`
**0.4 SUBJECT CARD SCHEMA**: `Subject ID | Role | Prior Knowledge (direct) | Prior Knowledge (secondhand) | Disposition | Vocabulary Signature [Term 1, Term 2, Term 3] | Evidential Function | Influence-Map Position & Rationale`

**INFLUENCE-MAP SEQUENCE RULE**: Subjects are interviewed in order of proximity to the feature decision — the person whose opinion most directly shapes the decision runs first; the most distal last. This is not seniority order; it is decision-influence order. The rationale for each position must be stated in the subject card (→ 0.4 field: Influence-Map Position & Rationale).

**DUAL TAXONOMY RULE**: Evidence items carry two independent tagging dimensions. These dimensions are orthogonal and must never be collapsed into a single tag:
- *Experience-Proximity* (GROUNDED / CONDITIONAL / INFERRED): how close the subject is to direct operational experience of the claim
- *Origin-of-Claim* (verbatim / inferred / corroborated): how the claim was derived from the transcript

---

## PHASE 0A — SUBJECT CARD SET

Produce three subject cards using 0.4 schema. The Influence-Map Position & Rationale field must name where in the decision chain each subject sits and why their interview position follows from that.

Vocabulary signatures: 3 terms per subject. Terms must be distinctive enough to spot-check — not general trait descriptions.

Evidential function: name the structural contribution to the evidence chain, not the disposition or role.

```
PHASE 0A — SUBJECT CARD SET GATE
PROHIBITED: expectation entries, transcripts, evidence, moment labels
REQUIRED:
[ ] Three cards, 0.4 schema, all fields populated (→ 0.4)
[ ] Vocabulary signatures: 3 named terms per subject (→ 0.4)
[ ] Influence-map positions: decision-proximity rationale stated for all three (→ 0.4)
[ ] Evidential functions: structural contribution named (not role-restatement) (→ 0.4)
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PHASE 0B — EXPECTATION REGISTER

Produce register table: `Exp ID | Subject ID | Expected Claim | Basis | Violated? [blank]`. Minimum 2 entries per subject.

This register is the authoritative source for the "expected:" slot in all 0.3 moment labels. "Violated?" column is blank here; it is filled during Phases 1–3 as labels are applied.

```
PHASE 0B — EXPECTATION REGISTER GATE
PROHIBITED: moment labels, transcripts
REQUIRED:
[ ] Table with all five columns (→ 0.3)
[ ] Min 2 entries per subject (6 rows)
[ ] "Violated?" column: blank
[ ] Register declared as 0.3 "expected:" source (→ 0.3)
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PHASE 0C — MOMENT-LABEL DECISION TAXONOMY

Three-label system declared as a complete decision taxonomy before Phase 1:

- **SURPRISING** = Register expectation violated
- **CONFIRMING** = Register expectation upheld
- **INCONCLUSIVE** = Signal present but directionally ambiguous; cannot be assigned to either prior-expectation category

All three rules declared. The taxonomy governs all labeling in Phases 1–3 regardless of which labels are exercised.

```
PHASE 0C — MOMENT-LABEL TAXONOMY GATE
PROHIBITED: transcripts
REQUIRED:
[ ] SURPRISING decision rule declared (→ 0.3)
[ ] CONFIRMING decision rule declared (→ 0.3)
[ ] INCONCLUSIVE decision rule declared — ambiguity condition named (→ 0.3)
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PRE-INTERVIEW MASTER GATE

Synthesizes closure of all setup phases by cross-referencing their named gates — not re-asserting their contents.

```
PRE-INTERVIEW MASTER GATE
PROHIBITED: any interview content
REQUIRED (evidenced by named gate closures):
[ ] Phase 0A — Subject Card Set Gate: CLOSED
[ ] Phase 0B — Expectation Register Gate: CLOSED
[ ] Phase 0C — Moment-Label Taxonomy Gate: CLOSED
[ ] Vocabulary signatures: declared for all three subjects — transcript verification runs in Phases 1–3 (→ 0.4)
[ ] Dual taxonomy rule confirmed: Experience-Proximity and Origin-of-Claim will be applied as separate columns (→ 0.2)
MASTER GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PHASE 1 — [SUBJECT 1 NAME] INTERVIEW + EVIDENCE TABLE

Open with subject role and influence-map position (one sentence each). Run 4–6 questions. At least one follow-up must cite the triggering phrase: `[triggered by: "exact phrase"] Follow-up: ...`.

Subject answers must be written in their declared voice — at least one of their 3 vocabulary signature terms must appear naturally.

After the transcript, produce the evidence table per 0.2 schema. Include a fully instantiated example row before content rows. Apply the dual taxonomy to every row: Origin-of-Claim and Experience-Proximity in separate columns, using only their declared values.

Label moments per 0.3 format, citing Register entry IDs. At least one INCONCLUSIVE label across all three subjects, OR an explicit note that every labeled moment was unambiguously SURPRISING or CONFIRMING.

```
PHASE 1 — [SUBJECT 1 NAME] INTERVIEW + EVIDENCE TABLE GATE
PROHIBITED: synthesis content, comparison to Phases 2–3
REQUIRED:
[ ] Transcript: follow-up with `[triggered by: "exact phrase"]` citation (→ 0.3)
[ ] Vocabulary: at least 1 of 3 declared terms in transcript (→ 0.4)
[ ] Evidence table: 0.2 schema, example row present, all columns populated (→ 0.2)
[ ] Dual taxonomy: Origin-of-Claim and Experience-Proximity in separate columns — not merged (→ 0.2)
[ ] Moment labels: 0.3 format, Register IDs cited (→ 0.3)
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PHASE 2 — [SUBJECT 2 NAME] INTERVIEW + EVIDENCE TABLE

Same structure. Open by naming this subject's influence-map position and how it differs from Phase 1's subject.

```
PHASE 2 — [SUBJECT 2 NAME] INTERVIEW + EVIDENCE TABLE GATE
PROHIBITED: objection lifecycle conclusions, synthesis
REQUIRED:
[ ] Transcript: follow-up with `[triggered by: ...]` citation (→ 0.3)
[ ] Vocabulary: at least 1 declared term in transcript (→ 0.4)
[ ] Evidence table: 0.2 schema, dual taxonomy applied (→ 0.2)
[ ] Moment labels: 0.3 format, Register IDs cited (→ 0.3)
[ ] Influence-map contrast: named in transcript opening
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PHASE 3 — [SUBJECT 3 NAME] INTERVIEW + EVIDENCE TABLE

Same structure.

```
PHASE 3 — [SUBJECT 3 NAME] INTERVIEW + EVIDENCE TABLE GATE
REQUIRED:
[ ] Transcript: follow-up with `[triggered by: ...]` citation (→ 0.3)
[ ] Vocabulary: at least 1 declared term in transcript (→ 0.4)
[ ] Evidence table: 0.2 schema, dual taxonomy applied (→ 0.2)
[ ] Moment labels: 0.3 format, Register IDs cited (→ 0.3)
[ ] C-14 check: at least 1 INCONCLUSIVE label across Phases 1–3, OR explicit note that all moments resolved cleanly
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PHASE 4 — INTERVIEW SYNTHESIS GRID

Produce a named artifact: **INTERVIEW SYNTHESIS GRID**. Schema columns: `Subject | Evidence Category | Testimony Direction (supports / challenges / inconclusive) | Experience-Proximity Weight Adjustment | Implication`.

The weight adjustment column is required. For at least one row, explicitly name an adjustment: if the subject making a claim has not directly operated the system or encountered the constraint, name this and state what it means for how the claim should be weighted — e.g., "Conditional — subject reasoning from analogous domain, not direct deployment; treat as a risk to probe, not a resolved blocker."

After the grid, write the **Objection Lifecycle Trace**: name the primary objection from the most proximate-to-decision subject (Phase 1), and state whether it *persisted*, *transformed*, or *was resolved* across Phases 2–3. Cite the specific transcript moment or evidence row that determined the outcome.

```
PHASE 4 — INTERVIEW SYNTHESIS GRID GATE
REQUIRED:
[ ] Synthesis grid: named artifact, all 5 schema columns, all subjects represented
[ ] Weight adjustment: at least 1 row with explicit experience-proximity adjustment and implication
[ ] Objection lifecycle: named outcome (persist / transform / resolve) + phase + moment citation
GATE STATUS: [ ] OPEN / [x] CLOSED
```

---

## PHASE 5 — SIMULATION FIDELITY + VOICE DIVERGENCE NOTE

**Fidelity Note** (3–5 sentences): Distinguish grounded claims (anchored to documented role knowledge, known adoption patterns, domain constraints) from constructed plausibility. Name at least one specific grounding basis.

**Voice Divergence Acknowledgment** (2–3 sentences): Name one concrete contrast in how two subjects were written to sound different. Cite a specific vocabulary term, framing preference, or concern priority, and identify where in the transcripts it appears.

```
PHASE 5 — FIDELITY + VOICE DIVERGENCE NOTE GATE
REQUIRED:
[ ] Fidelity note: grounded/constructed distinction with named specific basis
[ ] Voice divergence: concrete vocabulary or framing contrast, transcript-cited with specific term
GATE STATUS: [ ] OPEN / [x] CLOSED
```
```

---

*Variation axes summary:*

| Variation | Primary Axis | Secondary Axis | Hypothesis |
|-----------|-------------|----------------|------------|
| V-01 | Role Sequence (Skeptic-First) | — | Objections surface before framing; objection lifecycle becomes the structural spine |
| V-02 | Output Format (Schema-First) | — | Schema-before-content makes rubric coverage architecturally inevitable |
| V-03 | Lifecycle Emphasis (Gate-Heavy) | — | PROHIBITED/REQUIRED gate blocks with sub-gate cross-references prevent phase bleeding |
| V-04 | Phrasing Register (Conversational) | Inertia Framing (Status-Quo Prominent) | Lower cognitive load + mandatory status-quo pressure produces richer adoption-risk signals |
| V-05 | Influence-Map Sequence | Artifact-Centric Titles + Evidence Taxonomy Depth | Proximity-to-decision ordering + artifact-named phases make master gate closure semantically self-describing |
