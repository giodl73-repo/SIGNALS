## prove-interview — V-01 through V-05

---

## V-01 — Axis: Role Sequence
**Hypothesis:** Forcing an explicit sequence rationale (skeptic-first → neutral → advocate) before any interview begins surfaces objections structurally early. The objection lifecycle (C-21) becomes mandatory rather than authorial because the skeptic's position is established before advocates ever speak — the synthesis section has no choice but to trace what happened to those objections.

---

```markdown
# prove-interview

Simulate a set of stakeholder interviews for the topic under investigation.
The simulation is fictional but grounded: each subject's answers must be
consistent with their declared role, knowledge scope, and stated concerns.
Do not invent knowledge the subject would not plausibly have.

---

## PHASE 0 — SEQUENCE DECLARATION

Before creating any subject, declare the interview sequence and its rationale.

Write a SEQUENCE RATIONALE block:

```
SEQUENCE RATIONALE
Order: [Subject A role] → [Subject B role] → [Subject C role]
Logic: [One sentence explaining why this order was chosen]
Objection-surface goal: [Name the first subject's expected challenge]
```

Required ordering principle: place the most skeptical or highest-inertia
subject first. The skeptic's objections become the baseline that subsequent
interviews must respond to. If no natural skeptic exists among the subjects,
place the highest-uncertainty subject first and name that as the rationale.

---

## PHASE 0B — SUBJECT CARDS

For each interview subject, produce a Subject Card before any transcript begins.

Subject Card fields (all required):
- **Role / Title**: explicit function or title — no anonymous subjects
- **Prior Knowledge**: what this subject knows, has seen, or has operated
- **Blind Spots**: what this subject has not experienced or is reasoning
  about abstractly
- **Disposition**: one of ADVOCATE / SKEPTIC / NEUTRAL / CHALLENGER
- **Evidential Function**: the structural role this subject plays in the
  investigation — not who they are, but what their testimony *does* for
  the evidence chain (e.g., "establishes the adoption baseline that
  subsequent subjects validate or contest")
- **Vocabulary Signature**: 2–3 terms this subject would use that others
  would not — specific enough to spot-check any answer against

PHASE 0B GATE:
[ ] Subject card present for every subject
[ ] Disposition declared for every subject
[ ] Evidential function declared for every subject (not a restatement of role)
[ ] Vocabulary signature names 2+ specific terms per subject
[ ] At least one SKEPTIC or CHALLENGER disposition is assigned

---

## PHASE 0C — EXPECTATION REGISTER

Before any transcript begins, populate a register of prior expectations —
what you expect each subject to say, and why.

Format:

```
EXPECTATION REGISTER

Subject: [Role]
Expected claim 1: [What you expect them to say]  Basis: [Why]
Expected claim 2: [What you expect them to say]  Basis: [Why]
```

Produce one register entry per subject. The register entries must appear
in the same order declared in Phase 0 (skeptic first).

PHASE 0C GATE:
[ ] Register entry present for every subject
[ ] Each entry names at least 2 prior expectations with basis
[ ] Register appears before the first transcript line

---

## PHASE 0D — MOMENT-LABEL DECISION TAXONOMY

Declare the three-label system before any interview:

```
MOMENT-LABEL TAXONOMY
SURPRISING  = prior expectation violated — the subject said something
              inconsistent with what the register predicted
CONFIRMING  = prior expectation upheld — the subject said something
              consistent with what the register predicted
INCONCLUSIVE = signal present but directionally ambiguous — cannot be
              assigned to either prior-expectation category
```

This taxonomy governs every labeled moment in every transcript.
PARTIAL credit: if every labeled moment was unambiguously SURPRISING or
CONFIRMING, state explicitly: "No INCONCLUSIVE moments arose; every
labeled moment resolved against the register."

PHASE 0D GATE:
[ ] All three label definitions declared
[ ] Decision rule stated for each label (not just the label name)
[ ] Taxonomy appears before the first transcript

---

## PRE-INTERVIEW MASTER GATE

Before Phase 1 begins, confirm:

```
PRE-INTERVIEW MASTER GATE
[ ] Phase 0  — Sequence rationale declared, skeptic-first order confirmed
[ ] Phase 0B — Subject cards complete for all N subjects
[ ] Phase 0C — Expectation register populated for all N subjects
[ ] Phase 0D — Moment-label decision taxonomy declared (all 3 rules)
Phase 1 authorized: YES / NO
```

If any box is unchecked, complete the missing item before proceeding.
Cross-reference each completed gate by name, not by assertion.

---

## PHASE 1 — INTERVIEWS (run in declared sequence)

Run subjects in the order established in Phase 0.

For each subject, produce:

**1. Interview Header**
State the subject's role, their position in the sequence, and the
sequence logic that placed them here (one line).

**2. Interview Transcript**
Write 5–8 exchanges (Q/A pairs). Rules:
- Questions must probe the subject's declared prior knowledge and concerns
- At least one question must follow up on a specific prior answer
  (mark it: `FOLLOW-UP: triggered by "[exact phrase from prior answer]"`)
- Answers must use at least one declared vocabulary signature term naturally
- Answers must sound distinct from other subjects' answers

**3. Moment Labels**
After the transcript, label notable moments:

```
SURPRISING (expected: [Expectation Register → "exact expected claim"],
            got: [what the subject actually said])

CONFIRMING (validates: [Expectation Register → "exact expected claim"])

INCONCLUSIVE: [what was said] — ambiguous because [reason]
```

At least one labeled moment per subject. All labels must cite the
Expectation Register as source.

**4. Evidence Extraction**
Extract 2–4 evidence items. For each item:

| # | Evidence Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity |
|---|--------------|-------------|----------|--------------------|-----------------|----------------------|
| 1 | [finding] | [adoption risk / feasibility concern / requirement gap / scope signal / constraint / other] | strong / moderate / weak | [one sentence] | verbatim / inferred / corroborated | GROUNDED / CONDITIONAL / INFERRED |

- **Origin-of-Claim**: how the claim was derived from the transcript
  (verbatim = quoted directly; inferred = implied; corroborated = consistent
  across 2+ subjects)
- **Experience-Proximity**: how close the subject is to direct operational
  experience (GROUNDED = has operated it; CONDITIONAL = partial exposure;
  INFERRED = reasoning without direct experience)
- Do not conflate the two dimensions. They are orthogonal.

PHASE 1 GATE (per subject):
[ ] Follow-up question present with trigger citation
[ ] Vocabulary signature term appears in transcript
[ ] At least one labeled moment cites the Expectation Register
[ ] Evidence table complete with both taxonomy dimensions

---

## PHASE 2 — CROSS-INTERVIEW SYNTHESIS

Required when N ≥ 2 subjects.

**2A. Objection Lifecycle**
The first subject (skeptic) opened with specific objections.
For each objection: did it PERSIST, TRANSFORM, or RESOLVE across
the full interview sequence? Name which subject's testimony caused
the movement, and quote the moment.

```
Objection: [Initial claim from skeptic transcript]
Lifecycle: PERSIST / TRANSFORM / RESOLVE
Movement evidence: [Subject name] — "[quoted line that moved it]"
```

**2B. Synthesis Grid**

| Subject | Key Evidence Item | Framework Dimension | Testimony Direction | Implication |
|---------|------------------|--------------------|--------------------|-------------|
| [role] | [item] | [dimension] | supports / challenges / inconclusive | [so what] |

Synthesis weight note: for any item where Experience-Proximity differs
across subjects — name which item, identify the subject with GROUNDED
standing, and state explicitly how that affects the synthesis weight.

**2C. Composite Signal**
Write one paragraph: what do the signals together say? Name patterns,
contradictions, or convergences. Reference at least two evidence items
by their row number.

PHASE 2 GATE:
[ ] Objection lifecycle tracked for every opening skeptic objection
[ ] Synthesis grid complete
[ ] Epistemic weight adjustment stated at least once
[ ] Composite signal names at least two evidence items

---

## PHASE 3 — SIMULATION FIDELITY NOTE

Write a brief (3–5 sentence) meta-note. Name at least one specific basis
for a grounded claim (documented domain knowledge, named persona source,
prior research) and distinguish it from at least one constructed plausibility
claim (no documented basis — invented for the simulation but within role).

---

END OF SKILL
```

---

## V-02 — Axis: Output Format
**Hypothesis:** Mandating named schema tables for every structural component — subject cards, evidence, synthesis — enforces the dual evidence taxonomy (C-27) and framework-dimension mapping (C-36) as column constraints rather than authorial choices. When the schema demands two separate columns, dimension conflation is detectable at a glance.

---

```markdown
# prove-interview

Simulate stakeholder interviews using schema-bound output throughout.
Every structural element — subject profiles, evidence extraction, synthesis —
must be delivered as a named table artifact with explicit column schema.
Prose is permitted only for transcript bodies and the fidelity note.

---

## SCHEMA CONTRACT (document-level)

The following column sets govern all non-transcript output.

**Subject Card Schema**
| Role | Prior Knowledge | Blind Spots | Disposition | Evidential Function | Vocab Term 1 | Vocab Term 2 |

**Evidence Row Schema**
| # | Finding | Signal Type | Strength | Rationale | Origin-of-Claim | Experience-Proximity |

**Synthesis Row Schema**
| Subject | Finding | Evidence-Category | Testimony Direction | Weight Note | Implication |

Any table that omits a declared column or substitutes a column with a
different name fails the schema contract.

---

## STEP 1 — SUBJECT TABLE

Produce the Subject Card table. One row per subject.
Minimum 2 rows. Maximum 5 rows.

| Role | Prior Knowledge | Blind Spots | Disposition | Evidential Function | Vocab Term 1 | Vocab Term 2 |
|------|----------------|------------|-------------|--------------------|--------------| ------------|
| [role] | ... | ... | ADVOCATE/SKEPTIC/NEUTRAL/CHALLENGER | [structural contribution to evidence chain] | [specific term] | [specific term] |

Rules:
- Disposition must be one of the four listed values
- Evidential Function must name a structural contribution, not restate the role
- Vocab terms must be specific enough to spot-check transcript answers

---

## STEP 2 — EXPECTATION REGISTER TABLE

Produce a register of prior expectations. One block per subject, in subject order.

| Subject | Expected Claim | Basis |
|---------|---------------|-------|
| [role] | [what you expect them to say] | [why you expect it] |
| [role] | [second expectation] | [why] |

Minimum 2 expected claims per subject. The register must be complete
before any transcript begins.

---

## STEP 3 — MOMENT-LABEL TAXONOMY TABLE

| Label | Decision Rule |
|-------|--------------|
| SURPRISING | Prior expectation violated — the subject said something inconsistent with the Expectation Register |
| CONFIRMING | Prior expectation upheld — the subject said something consistent with the Expectation Register |
| INCONCLUSIVE | Signal present but directionally ambiguous — cannot be assigned to either register category |

This table governs all labels in Steps 4–6.

---

## PRE-INTERVIEW CHECKPOINT

Before Step 4:

```
PRE-INTERVIEW CHECKPOINT
Subject Table: [N rows / schema complete Y/N]
Expectation Register: [N subjects covered Y/N]
Moment-Label Taxonomy: [3 rules declared Y/N]
PROCEED: YES / NO
```

---

## STEPS 4–N — INTERVIEWS (one step per subject)

For each subject, run:

### Step [N]: Interview — [Subject Role]

**Sequence note:** One sentence stating why this subject appears at this
position (first, second, third...) in the interview order.

**Transcript**
Write 5–8 Q/A pairs. Follow-up requirements:
- At least one Q must be marked: `FOLLOW-UP (triggered by: "[exact prior phrase]")`
- At least one of the subject's declared vocab terms must appear naturally

**Moment Labels**
Immediately after the transcript, produce a Moment Labels table:

| Turn # | Transcript Phrase | Label | Register Source (expected: "...") | What Emerged |
|--------|------------------|-------|-----------------------------------|-------------|
| [Q3 A3] | "[phrase]" | SURPRISING | [Expectation Register row] | [what was said] |

Every SURPRISING and CONFIRMING label must cite a specific Expectation
Register row in the "Register Source" column.
At least one INCONCLUSIVE label must appear across the full simulation,
OR include an explicit note: "No INCONCLUSIVE moments arose; every
labeled moment resolved unambiguously against the register."

**Evidence Table**
Produce the evidence table using the declared Evidence Row Schema.

| # | Finding | Signal Type | Strength | Rationale | Origin-of-Claim | Experience-Proximity |
|---|---------|------------|---------|-----------|-----------------|---------------------|
| 1 | [finding] | adoption risk / feasibility concern / requirement gap / scope signal / constraint | strong/moderate/weak | [one sentence] | verbatim/inferred/corroborated | GROUNDED/CONDITIONAL/INFERRED |

Signal types: adoption risk, feasibility concern, requirement gap,
scope signal, constraint. Label assignment must match column values exactly.

Origin-of-Claim governs how the claim was derived from the transcript.
Experience-Proximity governs how close the subject is to direct operational
experience. These are orthogonal dimensions. Do not conflate them.

---

## STEP N+1 — CROSS-INTERVIEW SYNTHESIS TABLE

Required when N ≥ 2 subjects.

**Objection Lifecycle Table**

| Objection (from Subject 1) | Final State | Movement Evidence | Moving Subject |
|---------------------------|-------------|------------------|---------------|
| "[quoted claim]" | PERSISTED / TRANSFORMED / RESOLVED | "[quoted line]" | [subject role] |

One row per distinct objection raised in the first (skeptic/challenger) interview.
If no subject held a SKEPTIC or CHALLENGER disposition, note N/A and skip.

**Synthesis Grid**

Use the Synthesis Row Schema declared at document head.

| Subject | Finding | Evidence-Category | Testimony Direction | Weight Note | Implication |
|---------|---------|------------------|--------------------|------------|-------------|
| [role] | [item # from evidence table] | [category] | supports/challenges/inconclusive | [epistemic weight note if applicable] | [implication] |

Weight Note rule: when two subjects' experience-proximity differs on the
same finding, the row for the lower-proximity subject must state:
"CONDITIONAL — subject has not operated [X]; treat as risk, not blocker."

**Composite Signal (prose)**
One paragraph. Name at least two evidence items by row number.
Name at least one convergence and one contradiction if N ≥ 3 subjects.

---

## STEP N+2 — SIMULATION FIDELITY NOTE

3–5 sentences. Name:
1. At least one grounded claim and its specific documented basis
2. At least one constructed plausibility claim with no documented source

---

END OF SKILL
```

---

## V-03 — Axis: Lifecycle Emphasis
**Hypothesis:** Leading every phase transition with a named PROHIBITED/REQUIRED gate block, and decomposing multi-concern setup into numbered sub-phases with independent exit gates, makes the master gate closure structurally inevitable. The gate hierarchy enforces prerequisite traceability without author effort.

---

```markdown
# prove-interview

Simulate stakeholder interviews for the topic under investigation.
Each structural phase closes with a named gate block before the next
phase begins. Gates lead with PROHIBITED content before REQUIRED content.
Multi-concern setup phases are decomposed into independent sub-phases.

---

## PHASE 0A — SUBJECT REGISTRATION

Register each interview subject. One subject card per subject.

For each subject, declare:
- **Role**: explicit title or function
- **Prior Knowledge**: what they have seen, operated, or built
- **Blind Spots**: what they are reasoning about without direct experience
- **Disposition**: ADVOCATE / SKEPTIC / NEUTRAL / CHALLENGER
- **Evidential Function**: the structural role this subject's testimony
  plays in the evidence chain — not a restatement of their role

```
PHASE 0A EXIT GATE
PROHIBITED: No interview transcripts. No questions. No prior expectations.
REQUIRED:
[ ] Subject card produced for every intended subject
[ ] Every card has role, prior knowledge, blind spots, disposition
[ ] Every card has a non-redundant evidential function statement
[ ] At least 2 subjects registered
```

---

## PHASE 0B — VOCABULARY SIGNATURES

For each registered subject, declare 2–3 role-specific vocabulary terms.
Terms must be specific enough to spot-check any transcript answer.

```
PHASE 0B EXIT GATE
PROHIBITED: No transcript content. No answer simulation.
REQUIRED:
[ ] Vocabulary signature present for every subject
[ ] Each signature names 2+ specific terms (not general traits)
[ ] No two subjects share all vocabulary terms
```

---

## PHASE 0C — EXPECTATION REGISTER

For each subject, declare prior expectations: what you expect the
subject to say and why. Minimum 2 expectations per subject.

Format per subject:
```
EXPECTATIONS — [Subject Role]
E1: [expected claim]  Basis: [reason]
E2: [expected claim]  Basis: [reason]
```

```
PHASE 0C EXIT GATE
PROHIBITED: No moment labels. No evidence extraction. No transcripts.
REQUIRED:
[ ] Register entry present for every subject
[ ] Each entry has minimum 2 expectations with explicit basis
[ ] Register is complete before first transcript
```

---

## PHASE 0D — MOMENT-LABEL TAXONOMY

Declare all three label rules before any interview.

```
MOMENT-LABEL TAXONOMY
SURPRISING  = prior expectation violated
CONFIRMING  = prior expectation upheld
INCONCLUSIVE = signal present but directionally ambiguous; cannot
               resolve against either register category
```

State explicitly: this taxonomy governs all labels in all transcripts.

```
PHASE 0D EXIT GATE
PROHIBITED: No transcript content.
REQUIRED:
[ ] All three labels declared with decision rules
[ ] Taxonomy states it governs all downstream labeling
```

---

## PHASE 0E — SEQUENCE DECLARATION

Declare the order in which subjects will be interviewed.
State the rationale: why this order, what it achieves.

```
SEQUENCE: [Role 1] → [Role 2] → [Role 3]
RATIONALE: [one sentence]
```

```
PHASE 0E EXIT GATE
PROHIBITED: No transcripts.
REQUIRED:
[ ] Sequence declared with all subjects named
[ ] Rationale sentence present
[ ] If SKEPTIC disposition exists: skeptic appears at position 1 or 2
```

---

## PRE-INTERVIEW MASTER GATE

```
PRE-INTERVIEW MASTER GATE

Sub-gate completions (cite by gate name, not assertion):
[ ] PHASE 0A EXIT GATE: PASSED
[ ] PHASE 0B EXIT GATE: PASSED
[ ] PHASE 0C EXIT GATE: PASSED
[ ] PHASE 0D EXIT GATE: PASSED
[ ] PHASE 0E EXIT GATE: PASSED

PHASE 1 AUTHORIZED: YES / NO
```

Do not assert readiness. Cross-reference each sub-gate by name.
If any sub-gate is not passed, complete it before checking this gate.

---

## PHASE 1 — INTERVIEW TRANSCRIPTS

Run subjects in the declared sequence order. For each subject:

**1. Subject Header**
State: role, sequence position, one sentence on why they appear here.

**2. Transcript**
5–8 Q/A exchanges.
- At least one follow-up: `FOLLOW-UP (triggered by: "[exact prior phrase]")`
- At least one declared vocabulary term must appear in the subject's answers

**3. Moment Labels**
After the transcript, label each notable moment using the Phase 0D taxonomy.
Required format:
- `SURPRISING (expected: [Expectation Register → "exact phrase"], got: [what emerged])`
- `CONFIRMING (validates: [Expectation Register → "exact phrase"])`
- `INCONCLUSIVE: [moment] — ambiguous because [reason]`
Every label must cite the Expectation Register as source.
Minimum one labeled moment per subject.

```
PHASE 1 EXIT GATE (repeat per subject)
PROHIBITED: No evidence extraction. No synthesis.
REQUIRED:
[ ] Follow-up question present with exact trigger phrase
[ ] At least one vocab term appears in subject answers
[ ] At least one labeled moment with register citation
[ ] Transcript voice is distinct from other subjects' transcripts
```

---

## PHASE 2 — EVIDENCE EXTRACTION

For each subject, extract 2–4 evidence items.

Per item, declare:

| # | Evidence Item | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity |
|---|--------------|-------------|----------|--------------------|-----------------|----------------------|

- **Signal Type**: adoption risk / feasibility concern / requirement gap / scope signal / constraint
- **Strength**: strong / moderate / weak
- **Strength Rationale**: one sentence naming why
- **Origin-of-Claim**: verbatim / inferred / corroborated (how claim was derived from transcript)
- **Experience-Proximity**: GROUNDED / CONDITIONAL / INFERRED (how close subject is to operational experience)

These two dimensions are orthogonal. Do not merge them into one column.

```
PHASE 2 EXIT GATE
PROHIBITED: No synthesis across subjects yet.
REQUIRED:
[ ] Evidence table present for every subject
[ ] Signal type, strength, rationale, both taxonomy dimensions present per row
[ ] Origin-of-Claim and Experience-Proximity appear in separate columns
[ ] At least one corroborated item if N ≥ 2 subjects
```

---

## PHASE 3 — CROSS-INTERVIEW SYNTHESIS

Required for N ≥ 2 subjects.

**3A. Objection Lifecycle** (required if any subject held SKEPTIC or CHALLENGER)
For each objection the first skeptic/challenger raised:
- State: PERSISTED / TRANSFORMED / RESOLVED
- Quote the specific moment that caused movement
- Name the subject whose testimony caused it

**3B. Synthesis Grid**

| Subject | Evidence Item | Evidence Category | Testimony Direction | Weight Note | Implication |
|---------|--------------|------------------|---------------------|-------------|-------------|
| [role] | [#] | [category] | supports/challenges/inconclusive | [epistemic adjustment if applicable] | [so what] |

Where Experience-Proximity differs across subjects on the same finding:
name the lower-proximity subject's row as "CONDITIONAL — not yet
encountered [X]; treat as risk, not blocker."

**3C. Composite Signal**
One paragraph. Name at least two evidence items by row number.

```
PHASE 3 EXIT GATE
PROHIBITED: No new transcript content.
REQUIRED:
[ ] Objection lifecycle complete for every skeptic objection (or N/A stated)
[ ] Synthesis grid complete with all five columns
[ ] Epistemic weight note present where proximity differs
[ ] Composite signal paragraph cites at least two evidence items
```

---

## PHASE 4 — SIMULATION FIDELITY NOTE

3–5 sentences. Name:
- At least one claim that is GROUNDED in documented knowledge, naming the specific source
- At least one claim that is CONSTRUCTED PLAUSIBILITY with no documented basis

```
PHASE 4 EXIT GATE
REQUIRED:
[ ] At least one grounded claim with named source
[ ] At least one constructed plausibility claim named as such
```

---

END OF SKILL
```

---

## V-04 — Combination: Role Sequence + Inertia Framing
**Hypothesis:** Naming the status-quo solution as a formal `INCUMBENT ANCHOR` in Phase 0C and placing the highest-inertia subject first forces every subsequent interview to declare position relative to that anchor. The anchor propagates through downstream phase gates (C-43), and subjects who have not yet encountered the alternative are explicitly marked CONDITIONAL — producing inertia-weighted synthesis (C-24) as a structural necessity rather than an authorial choice.

---

```markdown
# prove-interview

Simulate stakeholder interviews investigating a proposed change against
an incumbent status-quo solution. Every subject must declare their
proximity to the incumbent, and every evidence item must declare its
relationship to inertia (does it reinforce or break from the status quo?).

The interview sequence runs highest-inertia first. The status-quo
defender produces the baseline that all subsequent subjects respond to.

---

## PHASE 0 — INCUMBENT ANCHOR DECLARATION

Before any subject card, declare the status-quo solution this interview
is probing against.

```
INCUMBENT ANCHOR: [Name of the existing solution, approach, or behavior]
Why incumbents stay: [One sentence on why the status quo is defensible]
Why change is proposed: [One sentence on the proposed alternative's case]
```

This anchor is a formal output of Phase 0. Downstream phases must
reference it by name. Any phase gate that closes without confirming
the anchor was carried forward fails propagation.

```
PHASE 0 GATE
[ ] INCUMBENT ANCHOR named explicitly
[ ] Defense rationale stated (why incumbents stay)
[ ] Change rationale stated (why change is proposed)
```

---

## PHASE 0B — SUBJECT CARDS

Register each subject. One card per subject.

Required fields:
- **Role / Title**
- **Prior Knowledge**: what they have operated or built
- **Blind Spots**: what they are reasoning about without direct experience
- **Disposition**: ADVOCATE / SKEPTIC / NEUTRAL / CHALLENGER
- **Inertia Stance**: one of INCUMBENT DEFENDER / CHANGE ADVOCATE / UNDECIDED
  — their stated or probable position on the INCUMBENT ANCHOR
- **Evidential Function**: what their testimony *does* for the evidence chain
- **Vocabulary Signature**: 2–3 role-specific terms

Sequence rule: subjects must be ordered by inertia. The strongest
INCUMBENT DEFENDER runs first. CHANGE ADVOCATE runs last.
UNDECIDED and NEUTRAL subjects run in middle positions.

```
PHASE 0B GATE
[ ] Subject card complete for every subject
[ ] Inertia Stance declared for every subject (one of three values)
[ ] Sequence ordered by inertia (INCUMBENT DEFENDER first)
[ ] Evidential function present for every subject
[ ] Vocabulary signature present for every subject
[ ] INCUMBENT ANCHOR cited in at least one subject's card
```

---

## PHASE 0C — EXPECTATION REGISTER

For each subject, declare prior expectations about what they will say
about the INCUMBENT ANCHOR and the proposed change.

Format:
```
EXPECTATIONS — [Subject Role] (Inertia Stance: [INCUMBENT DEFENDER/...])
E1: [expected claim about the incumbent]  Basis: [why]
E2: [expected claim about the change]     Basis: [why]
E3: [expected concern or risk]            Basis: [why]
```

At least 2 expectations per subject, with at least one expectation
per subject that references the INCUMBENT ANCHOR by name.

```
PHASE 0C GATE
[ ] Register entry present for every subject
[ ] At least one expectation per subject references INCUMBENT ANCHOR
[ ] Basis stated for every expectation
[ ] Register complete before any transcript
```

---

## PHASE 0D — MOMENT-LABEL TAXONOMY

```
MOMENT-LABEL TAXONOMY
SURPRISING  = prior expectation violated
CONFIRMING  = prior expectation upheld
INCONCLUSIVE = directionally ambiguous; cannot resolve against register
```

---

## PRE-INTERVIEW MASTER GATE

```
PRE-INTERVIEW MASTER GATE
[ ] PHASE 0 GATE: PASSED — INCUMBENT ANCHOR: "[anchor name]"
[ ] PHASE 0B GATE: PASSED — Subjects ordered highest-inertia first
[ ] PHASE 0C GATE: PASSED — Expectations reference anchor
[ ] PHASE 0D: Taxonomy declared
PHASE 1 AUTHORIZED: YES / NO
```

The INCUMBENT ANCHOR value must be copied into the master gate check.
This is the anchor propagation point.

---

## PHASE 1 — INTERVIEWS (inertia-first sequence)

For each subject, in the declared sequence:

**Subject Header**
State: role, inertia stance, position in sequence, one sentence on
why they interview at this position.

**Incumbent Framing** (required)
One sentence per subject: how does this subject's testimony relate to
the INCUMBENT ANCHOR? Are they defending it, challenging it, or
reasoning about it from outside?

**Transcript**
5–8 Q/A exchanges. Requirements:
- At least one question must directly probe the subject's position on
  the INCUMBENT ANCHOR (name it in the question)
- At least one follow-up: `FOLLOW-UP (triggered by: "[exact prior phrase]")`
- At least one declared vocabulary term must appear in answers

**Moment Labels**
```
SURPRISING (expected: [Register → "exact phrase"], got: [what emerged])
CONFIRMING (validates: [Register → "exact phrase"])
INCONCLUSIVE: [moment] — ambiguous because [reason]
```

**Evidence Extraction**

| # | Finding | Inertia Relationship | Signal Type | Strength | Rationale | Origin-of-Claim | Experience-Proximity |
|---|---------|---------------------|------------|---------|-----------|-----------------|---------------------|
| 1 | [finding] | REINFORCES INCUMBENT / CHALLENGES INCUMBENT / NEUTRAL | [type] | strong/moderate/weak | [sentence] | verbatim/inferred/corroborated | GROUNDED/CONDITIONAL/INFERRED |

The **Inertia Relationship** column is required for every row.
It declares whether the finding strengthens the case for staying
(REINFORCES INCUMBENT), weakens it (CHALLENGES INCUMBENT),
or is independent (NEUTRAL).

---

## PHASE 2 — CROSS-INTERVIEW SYNTHESIS

**2A. Inertia Map**
Produce a brief table showing where each subject landed relative to
the INCUMBENT ANCHOR after their interview:

| Subject | Inertia Stance (declared) | Testimony Direction on INCUMBENT | Movement from baseline |
|---------|--------------------------|--------------------------------|----------------------|
| [role] | INCUMBENT DEFENDER / ... | supports incumbent / challenges / inconclusive | held / shifted / reversed |

**2B. Objection Lifecycle**
The first subject (INCUMBENT DEFENDER) opened with specific objections
to the proposed change. For each:
- State: PERSISTED / TRANSFORMED / RESOLVED
- Name the subject whose testimony caused movement
- Quote the specific moment

**2C. Synthesis Grid**

| Subject | Finding | Evidence Category | Testimony Direction | Inertia Relationship | Epistemic Weight Note | Implication |
|---------|---------|-----------------|---------------------|---------------------|----------------------|-------------|

Weight note: where Experience-Proximity is CONDITIONAL or INFERRED,
state explicitly: "subject has not operated [X]; inertia objection is
anticipatory, not experiential — treat as risk to monitor, not blocker."

**2D. Composite Signal**
One paragraph. State what the full interview sequence says about the
INCUMBENT ANCHOR — is the case for change sufficient to overcome
observed inertia? Name at least three evidence items by row number.

---

## PHASE 3 — SIMULATION FIDELITY NOTE

3–5 sentences. Name:
- At least one grounded claim (specific documented basis)
- At least one constructed plausibility claim
- One sentence on how the inertia framing was calibrated
  (what was known about incumbents vs. what was invented)

---

END OF SKILL
```

---

## V-05 — Combination: Output Format + Lifecycle Emphasis + Document-Head Format Contract
**Hypothesis:** Declaring a single format contract at document head that simultaneously governs gate block layout, evidence schema column sets, and moment-label taxonomy makes the entire output self-enforcing. Any section that violates the contract fails against a declared rule (C-33), not a section-local expectation. This collapses authorial overhead across the 40+ criteria by reducing each section's job to "follow the contract" rather than "remember what the rules were."

---

```markdown
# prove-interview

Simulate stakeholder interviews for the topic under investigation.

This prompt operates under a document-level FORMAT CONTRACT declared in
Section 0. Every section must conform to the contract. Deviations are
detectable violations of the named contract, not authorial judgment calls.

---

## SECTION 0 — FORMAT CONTRACT (document-level authority)

This contract governs all non-transcript content in this document.

### 0.1 Gate Block Format
Every phase gate must appear as a named block in this format:
```
[GATE NAME]
PROHIBITED: [category of out-of-scope content]
REQUIRED:
[ ] [item one]
[ ] [item two]
STATUS: OPEN / PASSED
```
Gates with missing PROHIBITED clauses, missing STATUS fields,
or items distributed in prose rather than collected in a named block
violate this contract.

### 0.2 Evidence Row Schema
Every evidence table must carry exactly these columns in this order:
`# | Finding | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity`

- **Signal Type** values: adoption risk / feasibility concern /
  requirement gap / scope signal / constraint
- **Strength** values: strong / moderate / weak
- **Origin-of-Claim** values: verbatim / inferred / corroborated
- **Experience-Proximity** values: GROUNDED / CONDITIONAL / INFERRED

Columns may not be merged. Origin-of-Claim and Experience-Proximity
are orthogonal — they answer different questions and must not be
treated as synonyms.

### 0.3 Moment-Label Format
All moment labels must use this format:
- `SURPRISING (expected: [Register → "exact expected phrase"], got: [what emerged])`
- `CONFIRMING (validates: [Register → "exact expected phrase"])`
- `INCONCLUSIVE: [moment description] — ambiguous because [reason]`

Labels that omit the Register citation in the "expected" slot violate
this contract.

### 0.4 Subject Card Schema
Every subject card must carry these fields:
`Role | Prior Knowledge | Blind Spots | Disposition | Evidential Function | Vocab Term 1 | Vocab Term 2`

Disposition values: ADVOCATE / SKEPTIC / NEUTRAL / CHALLENGER.
Evidential Function must name a structural contribution to the evidence
chain — not a restatement of the role.

### CONTRACT AUTHORITY NOTE
All downstream sections derive their format requirements from this
contract. Individual section notes may amplify but never contradict it.
When a section check cites this contract (e.g., "per 0.2"), the check
is against Section 0 as authority, not against the section's local text.

---

## SETUP PHASE A — SUBJECT CARDS

Produce the subject table using the Section 0.4 schema.

| Role | Prior Knowledge | Blind Spots | Disposition | Evidential Function | Vocab Term 1 | Vocab Term 2 |
|------|----------------|------------|-------------|--------------------|--------------| ------------|

Minimum 2 rows. Maximum 5 rows.

```
[SETUP PHASE A GATE]
PROHIBITED: Interview transcripts, questions, expectations.
REQUIRED:
[ ] Subject table present with all Section 0.4 columns
[ ] Minimum 2 subjects registered
[ ] Evidential Function is non-redundant with Role for every subject
[ ] Vocabulary signature names 2+ specific terms per subject
STATUS: OPEN / PASSED
```

---

## SETUP PHASE B — EXPECTATION REGISTER

Produce a register of prior expectations per subject.
One block per subject:

```
EXPECTATIONS — [Subject Role]
E1: [expected claim]  Basis: [reason]
E2: [expected claim]  Basis: [reason]
```

Minimum 2 expectations with basis per subject.

```
[SETUP PHASE B GATE]
PROHIBITED: Transcripts, moment labels, evidence.
REQUIRED:
[ ] Register entry present for every subject
[ ] Minimum 2 expectations per subject, each with explicit basis
[ ] Register appears before first transcript line
STATUS: OPEN / PASSED
```

---

## SETUP PHASE C — MOMENT-LABEL TAXONOMY

Declare the three-label decision taxonomy per Section 0.3.

| Label | Decision Rule |
|-------|--------------|
| SURPRISING | Prior expectation violated |
| CONFIRMING | Prior expectation upheld |
| INCONCLUSIVE | Signal present but directionally ambiguous — cannot resolve against register |

State: this taxonomy governs all labels in all transcripts.

```
[SETUP PHASE C GATE]
PROHIBITED: Any transcript content.
REQUIRED:
[ ] All three labels declared with decision rules
[ ] Governing authority statement present
STATUS: OPEN / PASSED
```

---

## SETUP PHASE D — SEQUENCE DECLARATION

Declare interview order and rationale.

```
SEQUENCE: [Role 1] → [Role 2] → [Role 3...]
RATIONALE: [one sentence]
```

Ordering principle: if any subject holds SKEPTIC or CHALLENGER
disposition, that subject runs no later than position 2.

```
[SETUP PHASE D GATE]
PROHIBITED: Transcript content.
REQUIRED:
[ ] Sequence declared with all subjects named
[ ] Rationale sentence present
[ ] SKEPTIC/CHALLENGER subjects appear at position 1 or 2 (or N/A)
STATUS: OPEN / PASSED
```

---

## PRE-INTERVIEW MASTER GATE

```
[PRE-INTERVIEW MASTER GATE]
PROHIBITED: Phase 1 may not begin until this gate passes.
REQUIRED (cite sub-gate status, not assertion):
[ ] SETUP PHASE A GATE: [PASSED / OPEN]
[ ] SETUP PHASE B GATE: [PASSED / OPEN]
[ ] SETUP PHASE C GATE: [PASSED / OPEN]
[ ] SETUP PHASE D GATE: [PASSED / OPEN]
STATUS: OPEN / PASSED
```

Do not assert readiness. Copy each sub-gate status directly.
If any sub-gate reads OPEN, close it before setting this gate to PASSED.

---

## PHASE 1 — INTERVIEWS (run in declared sequence)

For each subject, repeat this structure:

### Interview — [Subject Role] (Position [N] of [Total])

**Sequence note:** One sentence on why this subject interviews here.

**Incumbent/Context framing:** One sentence on this subject's relationship
to the existing approach or status quo.

**Transcript**
5–8 Q/A exchanges.
- At least one follow-up: `FOLLOW-UP (triggered by: "[exact prior phrase]")`
- At least one declared vocabulary term must appear naturally in answers

**Moment Labels** (per Section 0.3 format contract)
Apply labels using the exact formats declared in Section 0.3.
Every SURPRISING and CONFIRMING label must cite the Expectation Register.
At least one labeled moment per subject.

**Evidence Table** (per Section 0.2 schema)

| # | Finding | Signal Type | Strength | Strength Rationale | Origin-of-Claim | Experience-Proximity |
|---|---------|------------|---------|-------------------|-----------------|---------------------|

All columns from Section 0.2 must appear. Do not merge columns.

```
[PHASE 1 GATE — [Subject Role]]
PROHIBITED: Cross-subject synthesis, comparison claims.
REQUIRED:
[ ] Follow-up question present with trigger citation
[ ] At least one vocab term in transcript (per 0.4 contract)
[ ] Moment labels in format per 0.3 contract, Register cited
[ ] Evidence table complete with all 0.2 columns
STATUS: OPEN / PASSED
```

---

## PHASE 2 — CROSS-INTERVIEW SYNTHESIS

Required when N ≥ 2 subjects.

**2A. Objection Lifecycle** (required if SKEPTIC or CHALLENGER present)

| Objection | Final State | Moving Subject | Evidence Moment |
|-----------|-------------|---------------|----------------|
| "[quoted skeptic claim]" | PERSISTED/TRANSFORMED/RESOLVED | [role] | "[quoted line]" |

**2B. Synthesis Grid**

| Subject | Finding (#) | Evidence Category | Testimony Direction | Epistemic Weight Note | Implication |
|---------|------------|------------------|---------------------|----------------------|-------------|

Epistemic weight rule: when Origin-of-Claim or Experience-Proximity
differs across subjects on the same finding, the lower-proximity row
must carry a weight note. Do not omit the column.

**2C. Composite Signal**
One paragraph. Cite at least two evidence items by row number.
Name at least one convergence and one contradiction if N ≥ 3 subjects.

```
[PHASE 2 GATE]
PROHIBITED: New transcript content, new evidence items.
REQUIRED:
[ ] Objection lifecycle table complete (or N/A with reason)
[ ] Synthesis grid complete with all five columns
[ ] Epistemic weight notes present where proximity differs
[ ] Composite signal paragraph cites ≥2 evidence items
STATUS: OPEN / PASSED
```

---

## PHASE 3 — SIMULATION FIDELITY NOTE

3–5 sentences. Name:
- At least one GROUNDED claim with specific documented basis
- At least one CONSTRUCTED PLAUSIBILITY claim named as such

```
[PHASE 3 GATE]
REQUIRED:
[ ] Grounded claim present with named source
[ ] Constructed plausibility claim named as such
STATUS: OPEN / PASSED
```

---

END OF SKILL
```
