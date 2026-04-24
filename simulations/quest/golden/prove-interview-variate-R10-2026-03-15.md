# prove-interview -- Prompt Variations R10
# Date: 2026-03-15
# Rubric: prove-interview-rubric-v10-2026-03-15.md
# Round: 10 (C-33/C-34/C-35 primary targets; denominator /27)

---

## Variation Axes Selected

| Axis | Description |
|------|-------------|
| Lifecycle emphasis | Skeptic-first gate architecture; minimal delta from V-01 R9; add C-33 unified document-head contract and C-34 evidenced master gate |
| Output format | Table-heavy, section-numbered; unify two existing R9 rules into single DOCUMENT-HEAD FORMAT CONTRACT (C-33); strengthen C-35 point-of-use citations |
| Phrasing register | Conversational voice; C-33 in friendly language; BEFORE-INTERVIEW CHECKLIST evidenced by named step completions (C-34); C-35 citation in prose |
| Role sequence + Inertia framing | Neutral-first sequence; Inertia Profile as shared baseline; C-33 + C-34 via INERTIA PROFILE GATE and sub-gate named completions |
| Output format + Inertia framing | Table-heavy x Inertia Profile; new combination not in R9; C-33/34/35 across both structural registers |

Single-axis variations: V-01 (lifecycle emphasis), V-02 (output format), V-03 (phrasing register)
Combination variations: V-04 (role sequence + inertia framing), V-05 (output format + inertia framing)

New v10 territory probed:
- **C-33** (all five): A unified DOCUMENT-HEAD FORMAT CONTRACT block declares all four
  structural rules for the whole document at the top -- Gate Block Rule, Schema
  Instantiation Rule, Vocabulary Exercise Rule, Dual Taxonomy Rule -- as a single named
  contract rather than scattered per-section reminders. R9 V-01 had no document-head
  block at all. R9 V-02 had two separate rule declarations (SCHEMA CONTRACT RULE + GATE
  BLOCK RULE) but not unified, missing Vocabulary Exercise and Dual Taxonomy rules. All
  R10 variations address this with a single named block at document head.
- **C-34** (all five): Master gate closure is evidenced by explicitly naming completed
  sub-gates -- "GATE 0A: PASSED", "C-28 STATUS CHECK: PASSED" -- not merely pointing
  to them ("Confirmed by GATE 0A above"). The distinction: a named completed sub-gate
  is proof; a pointer is an assertion. R9 V-01 said "Confirmed by GATE 0A above" --
  syntactically a reference but not the named-completion form C-34 requires. All R10
  variations promote these references to explicit named-completion labels.
- **C-35** (all five): Point-of-use prerequisite confirmations cite the master gate as
  the explicit authorization authority -- "confirmed FULLY SATISFIED in PRE-INTERVIEW
  MASTER GATE (item N -- GATE 0A: PASSED)". R9 V-01 had this pattern; R9 V-02 had
  "PRE-INTERVIEW MASTER GATE item N checked" (close but without the "FULLY SATISFIED"
  and named sub-gate form); R9 V-03 had no citation pattern. R10 standardizes the
  exact C-35 form across all variations.

---

## V-01 -- Lifecycle Emphasis: Document-Head Format Contract + Evidenced Master Gate

**Axis**: Lifecycle emphasis
**Hypothesis**: Minimal delta from V-01 R9, which scored strongest overall. Two
additions close C-33 and C-34. (1) A unified DOCUMENT-HEAD FORMAT CONTRACT block at
document top declares all four structural rules in a single named contract, satisfying
C-33. (2) The PRE-INTERVIEW MASTER GATE promotes "Confirmed by GATE 0A above" to
explicit "GATE 0A: PASSED" named-completion labels, satisfying C-34. V-01 R9's
point-of-use citation pattern ("confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item N)") carries forward unchanged, covering C-35.

```
You are running a simulated stakeholder interview investigation for the feature
topic: {{topic}}.

This is not a real interview. It is a structured simulation grounded in documented
persona knowledge, producing evidence artifacts for downstream topic narrative decisions.

Complete all phases in order. Do not write any transcript line before Phase 0 is
fully closed.

---

DOCUMENT-HEAD FORMAT CONTRACT (applies throughout this document)

Every structural format requirement for this document is declared here as a single
named contract. Any section that violates a rule below fails against this declared
contract -- not against a section-local expectation. The contract propagates; it does
not need to be re-stated per section.

RULE 1 -- GATE BLOCK FORMAT: Every phase gate in this document appears as a
consolidated named checklist block with this structure:
  PHASE N GATE
    [ ] item one description
    [ ] item two description
Gate items embedded in prose, scattered as isolated checkboxes, or appearing without
a named header block violate this rule.

RULE 2 -- SCHEMA INSTANTIATION: Every table that declares column headers as a
structural template includes at least one fully instantiated example row before any
real data rows. A headers-only table is an open schema contract -- it is not closed
until an example instance demonstrates how the columns apply to real content.

RULE 3 -- VOCABULARY EXERCISE: Each subject's declared vocabulary signature terms
appear at least once in that subject's interview transcript. A term declared pre-
interview that never surfaces in the transcript constitutes declaration-without-
enforcement: the auditable contract was created but never closed.

RULE 4 -- DUAL TAXONOMY INDEPENDENCE: Every evidence item carries two separate
orthogonal tags applied independently: (1) experience-proximity (GROUNDED /
CONDITIONAL / INFERRED -- how close the subject is to direct operational experience
of the claim), and (2) origin-of-claim (verbatim / inferred / corroborated -- how
the claim was derived from the transcript). These dimensions answer different
questions and must not be collapsed into a single tag set.

---

PHASE 0 -- PRE-INTERVIEW STRUCTURE

Do not begin Phase 1 until the PRE-INTERVIEW MASTER GATE at the end of Phase 0 is
explicitly satisfied.

---

STEP 0A -- Subject Roster and Sequence Justification

Select three subjects. Sequence them: SKEPTIC -> PRACTITIONER -> ADVOCATE.

For each subject, complete the Subject Card template in full:

## Subject Card: [Role/Name]
- Role: [job title or function]
- Evidential Function: [what this subject's structural position does for the evidence
  chain -- not their disposition, their contribution. Example: "establishes the
  objection surface that the practitioner and advocate must address or leave standing"]
- Experience-Proximity: GROUNDED | CONDITIONAL | INFERRED
  Justification: [one sentence -- why does this subject carry this proximity level?]
- Prior Knowledge: [2-3 sentences: what they know, have worked with, care about]
- Blind Spots: [1-2 sentences: what they have NOT encountered -- separate field from
  Prior Knowledge. Knowing a subject's blind spots is as important as their knowledge.]
- Vocabulary Signature (auditable contract -- declared before transcript):
  - Term 1: [a specific term distinctive enough to audit against transcript text]
  - Term 2: [a second specific term]
  - Term 3: [a third specific term]

Sequence justification (one sentence): State why skeptic-first, practitioner-second,
advocate-third is the optimal ordering for this specific investigation.

GATE 0A
  [ ] Subject 1 (Skeptic): all six fields populated -- Role, Evidential Function,
      Experience-Proximity with one-sentence justification, Prior Knowledge, Blind
      Spots, three vocabulary terms specific enough to audit against transcript text
  [ ] Subject 2 (Practitioner): same six fields all populated
  [ ] Subject 3 (Advocate): same six fields all populated
  [ ] Sequence justification sentence present

---

STEP 0B -- Moment-Label Decision System

IMPORTANT: This step declares a complete decision system governing all moment labels
in this simulation. Individual labels without this declared system fail C-28. This is
not a format reminder -- it is the rule set governing label selection.

## Moment-Label Decision System

Three labels are available. The decision rule for each is declared here and governs
every label applied in Phases 1, 2, and 3.

LABEL: SURPRISING
  Decision rule: Apply when a subject's response violates an expectation pre-registered
  in the Expectation Register (Step 0C). The violation must be directional: the subject
  said something meaningfully different from what was expected -- in position, intensity,
  or framing. If no register entry is available to serve as the "expected:" reference,
  do not apply SURPRISING; fix the register first.
  Required format: SURPRISING (expected: [Expectation Register -> Subject: {name},
    Field: "{field}"], got: [what actually emerged])

LABEL: CONFIRMING
  Decision rule: Apply when a subject's response upholds an expectation pre-registered
  in the Expectation Register. The subject said what was expected, validating a prior
  signal. The validation must trace to a named register field -- not a vague general
  assumption.
  Required format: CONFIRMING (validates: [Expectation Register -> Subject: {name},
    Field: "{field}"])

LABEL: INCONCLUSIVE
  Decision rule: Apply when a notable signal is present but direction is genuinely
  ambiguous and cannot be cleanly assigned to SURPRISING or CONFIRMING without
  additional evidence. Use this label rather than forcing an unclear moment.
  Required format: INCONCLUSIVE (closest register field: [Expectation Register ->
    Subject: {name}, Field: "{field}"], ambiguity: [why direction cannot be resolved])

Every labeled moment section in Phases 1-3 must end with one of:
  Option A: "All labeled moments in this phase are unambiguously SURPRISING or
             CONFIRMING. No INCONCLUSIVE moments were present."
  Option B: [Apply INCONCLUSIVE label to the ambiguous moment]
Silence -- applying only SURPRISING and CONFIRMING with no acknowledgment of Option A
-- fails C-14.

C-28 STATUS CHECK
  [ ] Decision system complete -- all three labels declared with decision rules,
      including INCONCLUSIVE. If any label is missing a decision rule, stop and
      complete it before proceeding.

---

STEP 0C -- Expectation Register

Declare prior expectations for each subject before any transcript begins. This
register is the mandatory structural source for all moment labels -- the "expected:"
slot must point to a named row and field here.

Example row (schema instantiation per Document-Head Format Contract Rule 2):

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [e.g., Skeptic -- Compliance Lead] | [e.g., Will block on audit immutability guarantee] | [e.g., No API-driven workflow has survived compliance review in this org] | [e.g., If guarantee exists, will confirm the approval-delay pain is real] | [e.g., May acknowledge current workaround creates compliance risk too] |

Real data:

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [Skeptic] | | | | |
| [Practitioner] | | | | |
| [Advocate] | | | | |

C-13 STATUS CHECK
  [ ] Register fully populated -- all cells have content for all three subjects and
      all five columns. If any cell is empty, C-13 is PARTIAL -- fix before proceeding.
      A PARTIAL C-13 cannot activate the C-25 bridge. Deploying the bridge against a
      PARTIAL register scores C-30 FAIL, not C-25 PASS.

---

PRE-INTERVIEW MASTER GATE

Before the first interview transcript begins, this gate confirms that all structural
prerequisites for the interview phase are collectively and fully satisfied, evidenced
by named completed sub-gate statuses. All four items must be checked.

PRE-INTERVIEW MASTER GATE
  [ ] SUBJECT CARDS COMPLETE -- GATE 0A: PASSED
      All three subject cards have all six fields populated. Vocabulary signatures
      contain specific auditable terms, not trait descriptors. Sequence justification
      sentence is present.

  [ ] EXPECTATION REGISTER POPULATED -- C-13 STATUS CHECK: PASSED
      All three subjects, all five columns filled. A PARTIAL register cannot activate
      the C-25 bridge. If any cell was empty at C-13 STATUS CHECK, stop here.

  [ ] VOCABULARY SIGNATURES DECLARED FOR ALL SUBJECTS -- GATE 0A: PASSED (item 3)
      Confirmed closed at GATE 0A: all subjects have 3 specific auditable vocabulary
      terms. Trait descriptors ("uses technical language") fail.

  [ ] MOMENT-LABEL DECISION TAXONOMY DECLARED -- C-28 STATUS CHECK: PASSED
      All three labels -- SURPRISING, CONFIRMING, and INCONCLUSIVE -- have declared
      decision rules. Confirmed closed at C-28 STATUS CHECK above.

Phase 1 begins only when all four boxes are checked.
Proceeding with a PARTIAL item checked scores C-31 PARTIAL -- do not advance.

---

PHASE 1 -- INTERVIEW: THE SKEPTIC

Transcript

Opening question: [A question anchored in the Skeptic's declared prior knowledge and
blind spots -- probing what specifically grounds their resistance]

[Skeptic]: [Answer in this subject's distinct voice. Vocabulary Signature terms must
appear naturally -- at least one of the three declared terms must surface in this
transcript, per Document-Head Format Contract Rule 3.]

Follow-up (triggered by: "[exact phrase from the preceding answer that prompted this]"):
[follow-up question anchored to the prior answer]

[Skeptic]: [answer]

[Continue 2-3 additional exchanges. The Skeptic's primary objection must be clearly
and explicitly stated by the end of this transcript -- it becomes the objection whose
lifecycle is tracked in Phase 4.]

---

Vocabulary Audit -- Skeptic

Prerequisite check: C-22 for Skeptic confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 3 -- GATE 0A: PASSED). Proceeding with audit.

- "[Term 1]": FOUND in A[N] -- "[brief quote]" | NOT FOUND (open contract)
- "[Term 2]": FOUND | NOT FOUND
- "[Term 3]": FOUND | NOT FOUND

At least 1 of 3 terms must be FOUND. [ ] vocabulary contract closed

---

Moment Label -- Skeptic

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item 2 -- C-13 STATUS CHECK: PASSED). Expectation Register is available as source
for "expected:" slot. Proceeding.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Expectation Register ->
  Subject: Skeptic, Field: "{field_name}"], ...)

C-25 bridge status: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE --
bridge active. (If C-13 were PARTIAL, deploying the bridge would score C-30 FAIL,
not C-25 PASS.)

Ambiguity check: [Apply Option A or Option B from Step 0B -- name which applies]

---

Evidence Extraction -- Skeptic

Prerequisite check: C-27 dual taxonomy confirmed -- Document-Head Format Contract
Rule 4 in force; GATE 0A: PASSED and C-28 STATUS CHECK: PASSED confirmed in PRE-
INTERVIEW MASTER GATE. Proceeding.

Dimension definitions (declared in Document-Head Format Contract, Rule 4):
  Experience-Proximity: "How close is this subject to direct operational experience?"
    GROUNDED = firsthand; CONDITIONAL = adjacent but not direct;
    INFERRED = reasoning from no direct operational experience.
  Origin-of-Claim: "How was this claim derived from the transcript?"
    verbatim = stated directly; inferred = implied but not said;
    corroborated = consistent signal across two or more subjects.

Example row (schema instantiation per Rule 2):
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| "The audit trail integration is non-negotiable -- any workaround adds a sprint minimum." | feasibility concern | GROUNDED -- has operated the audit trail process for 3 years | verbatim -- stated in A2: "non-negotiable" | strong | GROUNDED source, explicit operational claim, no hedging; directness and specificity warrant strong |

Real data:
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| | | | | | |

---

PHASE 1 GATE
  [ ] At least one vocabulary term FOUND in Skeptic's transcript -- contract closed
  [ ] Moment label references Expectation Register by subject name and field name
  [ ] Experience-Proximity and Origin-of-Claim both populated for every evidence row
      and not conflated
  [ ] Skeptic's primary objection explicitly stated and identifiable in transcript

---

PHASE 2 -- INTERVIEW: THE PRACTITIONER

Transcript

Opening question: [Anchored in the Practitioner's declared prior knowledge and the
operational ground truth this subject uniquely carries]

[Practitioner]: [Answer in this subject's distinct voice -- vocabulary distinct from
Skeptic's]

Follow-up (triggered by: "[exact phrase from the preceding answer that prompted this]"):
[follow-up anchored to prior answer]

[Practitioner]: [answer]

[Continue 2-3 more exchanges. At least one question must probe whether the
Practitioner's operational reality speaks to -- or is silent about -- the Skeptic's
primary objection from Phase 1.]

---

Vocabulary Audit -- Practitioner

Prerequisite check: C-22 for Practitioner confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 3 -- GATE 0A: PASSED). Proceeding.

- "[Term 1]": FOUND in A[N] -- "[quote]" | NOT FOUND
- "[Term 2]": FOUND | NOT FOUND
- "[Term 3]": FOUND | NOT FOUND

Closing status: [ ] vocabulary contract closed

---

Moment Label -- Practitioner

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item 2 -- C-13 STATUS CHECK: PASSED). Proceeding.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Expectation Register ->
  Subject: Practitioner, Field: "{field_name}"], ...)

C-25 bridge status: active -- C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER
GATE (item 2 -- C-13 STATUS CHECK: PASSED).

Ambiguity check: [Option A or Option B]

---

Evidence Extraction -- Practitioner

Prerequisite check: C-27 dual taxonomy confirmed -- Document-Head Format Contract
Rule 4 in force; confirmed in PRE-INTERVIEW MASTER GATE. "corroborated" is now
available for Origin-of-Claim when a signal matches Phase 1 evidence.

Example row (schema instantiation):
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| [fill with a real example from practitioner context -- distinct from Skeptic's example] | | | | | |

Real data:
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| | | | | | |

---

PHASE 2 GATE
  [ ] At least one vocabulary term FOUND in Practitioner's transcript
  [ ] Moment label references Expectation Register by subject and field
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Practitioner's response to (or silence about) Skeptic's primary objection visible

---

PHASE 3 -- INTERVIEW: THE ADVOCATE

Transcript

Opening question: [Anchored in the Advocate's declared evidential function -- what
structural role do they play in this evidence chain?]

[Advocate]: [Answer in this subject's distinct voice -- vocabulary and framing distinct
from both Skeptic and Practitioner]

Follow-up (triggered by: "[exact phrase from the preceding answer that prompted this]"):
[follow-up anchored to prior answer]

[Advocate]: [answer]

[Continue 2-3 more exchanges. At least one question probes whether the Advocate is
aware of the Skeptic's primary objection and what their response to it is.]

---

Vocabulary Audit -- Advocate

Prerequisite check: C-22 for Advocate confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 3 -- GATE 0A: PASSED). Proceeding.

- "[Term 1]": FOUND | NOT FOUND
- "[Term 2]": FOUND | NOT FOUND
- "[Term 3]": FOUND | NOT FOUND

Closing status: [ ] vocabulary contract closed

---

Moment Label -- Advocate

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item 2 -- C-13 STATUS CHECK: PASSED). Proceeding.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Expectation Register ->
  Subject: Advocate, Field: "{field_name}"], ...)

C-25 bridge status: active -- C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER
GATE (item 2 -- C-13 STATUS CHECK: PASSED).

Ambiguity check: [Option A or Option B]

---

Evidence Extraction -- Advocate

Prerequisite check: C-27 dual taxonomy confirmed -- Document-Head Format Contract
Rule 4 in force. "corroborated" available from Phases 1 and 2.

Example row (schema instantiation):
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| [fill with a real example from advocate context] | | | | | |

Real data:
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| | | | | | |

---

PHASE 3 GATE
  [ ] At least one vocabulary term FOUND in Advocate's transcript
  [ ] Moment label references Expectation Register by subject and field
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Advocate's response to (or evasion of) Skeptic's primary objection visible

---

PHASE 4 -- CROSS-INTERVIEW SYNTHESIS

Prerequisite confirmation: PHASE 1 GATE: PASSED, PHASE 2 GATE: PASSED, PHASE 3 GATE:
PASSED -- all three interview phases closed. Proceeding to synthesis.

Patterns and Contradictions

Name at least one convergence or contradiction across the three subjects. Reference
subjects by name and cite the specific evidence items (by subject and response number)
that produce it -- do not summarize without citation.

Objection Lifecycle

Trace the Skeptic's primary objection from Phase 1 through Phases 2 and 3.
  - Initial objection (Phase 1): [state it as declared in the transcript]
  - Practitioner's response (Phase 2): [addressed? transformed? silent? -- cite]
  - Advocate's response (Phase 3): [persisted? transformed? resolved? -- cite]
  - Final verdict: PERSISTED | TRANSFORMED | RESOLVED
    [one sentence naming the evidence that determines the verdict]

Epistemic Weight Adjustment

Explicitly adjust the weight of at least one evidence item based on Experience-Proximity.
Required format: "Item [evidence text] is CONDITIONAL -- [subject] has not experienced
[specific blind spot from their Subject Card]. Treat as a risk to monitor, not a
confirmed blocker, until a GROUNDED source who has encountered the alternative confirms
or refutes it."
If all evidence items are GROUNDED, state that explicitly and explain why no reduction
applies.

PHASE 4 GATE
  [ ] Objection lifecycle traced with PERSISTED / TRANSFORMED / RESOLVED verdict
      and specific citation
  [ ] At least one named epistemic weight adjustment present
  [ ] Convergence or contradiction cited with specific subject and evidence references

---

PHASE 5 -- META-OBSERVATIONS

PHASE 5A -- Simulation Fidelity Note

Include a brief meta-note identifying at least one specific grounding basis for claims
made in this simulation -- naming a piece of documented persona knowledge, domain
context, or structural role constraint that anchored a specific answer. Also name at
least one place where the simulation exercised constructed plausibility (not derived
from documented prior knowledge but from role logic). Distinguish grounded from
constructed.

PHASE 5B -- Voice Divergence Note

Include a meta-observation naming at least one concrete contrast in how two subjects
were made to sound different -- citing a specific vocabulary choice, framing preference,
or concern priority. Example: "[Subject A] used '[Term X]' while [Subject B] used
'[Term Y]' -- signaling different conceptual frames for the same feature." Generic
statements ("they had different roles") without a specific cited difference fail.
```

---

## V-02 -- Output Format: Unified Document-Head Contract + Evidenced Section Gates

**Axis**: Output format
**Hypothesis**: V-02 R9 had two separate document-head rules (SCHEMA CONTRACT RULE +
GATE BLOCK RULE) -- close to C-33 but not a single unified contract, and missing the
VOCABULARY EXERCISE and DUAL TAXONOMY rules. Fix: merge all four rules into one named
DOCUMENT-HEAD FORMAT CONTRACT block (C-33). R9 V-02's master gate already used "Section
N GATE passed" phrasing -- promoting to explicit "SECTION N GATE: PASSED" completion
labels closes C-34. R9 V-02's point-of-use said "PRE-INTERVIEW MASTER GATE item N
checked" -- strengthening to "confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item N -- SECTION N GATE: PASSED)" closes C-35.

```
You are running a simulated stakeholder interview investigation for the feature
topic: {{topic}}.

This is a structured simulation -- not a real interview -- grounded in documented
persona knowledge and producing evidence artifacts for downstream topic decisions.

---

DOCUMENT-HEAD FORMAT CONTRACT (applies throughout this document)

All structural format requirements for this document are declared in this single
named contract. Sections downstream do not re-declare these rules; violations fail
against this contract.

RULE 1 -- GATE BLOCK FORMAT: Every section ends with a named gate block:
  SECTION N GATE
    [ ] item one
    [ ] item two
Items embedded in prose or appearing outside a named block violate this rule.

RULE 2 -- SCHEMA INSTANTIATION: Every table with structural column headers includes
at least one fully instantiated example row before real data rows appear. A table
that transitions directly from headers to real data is an open schema contract.

RULE 3 -- VOCABULARY EXERCISE: Each subject's declared vocabulary signature terms
appear at least once in that subject's interview transcript. Declared terms that
never surface in the transcript constitute declaration-without-enforcement.

RULE 4 -- DUAL TAXONOMY INDEPENDENCE: Evidence items carry two orthogonal tags --
experience-proximity (GROUNDED/CONDITIONAL/INFERRED) and origin-of-claim
(verbatim/inferred/corroborated) -- applied separately and non-interchangeably.

---

SECTION 1 -- SUBJECT CARDS

Complete the Subject Card table. The schema row is the required instantiation
example; real data follows.

Schema + instantiation:

| Field | Skeptic | Practitioner | Advocate |
|-------|---------|--------------|----------|
| Role | [e.g., "Senior Compliance Analyst, 8 years in regulated pipeline environments"] | | |
| Evidential Function | [e.g., "Establishes the compliance objection surface -- subsequent subjects must speak to it or leave it standing"] | | |
| Experience-Proximity | [e.g., "GROUNDED -- has personally managed two audit trail failures in production"] | | |
| Prior Knowledge | [e.g., "Knows current manual workaround; seen two failed migrations; understands compliance clock constraint"] | | |
| Blind Spots | [e.g., "Has not used the new API-driven approach -- resistance grounded in prior failures, not the current alternative"] | | |
| Vocab Term 1 | [e.g., "audit immutability"] | | |
| Vocab Term 2 | [e.g., "compliance window"] | | |
| Vocab Term 3 | [e.g., "chain-of-custody"] | | |

Real data:

| Field | Skeptic | Practitioner | Advocate |
|-------|---------|--------------|----------|
| Role | | | |
| Evidential Function | | | |
| Experience-Proximity | | | |
| Prior Knowledge | | | |
| Blind Spots | | | |
| Vocab Term 1 | | | |
| Vocab Term 2 | | | |
| Vocab Term 3 | | | |

Sequence justification (one sentence): State why the chosen interview order is the
optimal ordering for this investigation -- name the structural reason.

C-22 STATUS CHECK: [ ] All three subjects have 3 specific vocabulary terms in the
real data table. Trait descriptors instead of specific auditable terms fail.

SECTION 1 GATE
  [ ] All eight rows populated in the real data table for all three subjects
  [ ] Sequence justification sentence is present
  [ ] C-22 STATUS CHECK passed

---

SECTION 2 -- EXPECTATION REGISTER

Declare prior expectations before any transcript begins. This table is the mandatory
source for all moment labels in Sections 4-6.

Schema + instantiation (example row):

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [e.g., Skeptic -- Compliance Analyst] | [e.g., Will require audit immutability guarantee] | [e.g., No API-driven approach has survived a compliance audit here] | [e.g., If guarantee exists, will confirm the workflow-reduction benefit is real] | [e.g., May acknowledge the current workaround creates compliance risk too] |
| Practitioner | | | | |
| Advocate | | | | |

Real data:

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [Skeptic] | | | | |
| [Practitioner] | | | | |
| [Advocate] | | | | |

C-13 STATUS CHECK: [ ] Register fully populated -- all cells have content for all
three subjects and all five columns. Empty cells mean C-13 is PARTIAL. A PARTIAL
C-13 cannot activate the C-25 bridge -- deploying against PARTIAL scores C-30 FAIL,
not C-25 PASS.

SECTION 2 GATE
  [ ] All cells in the real data table are populated
  [ ] C-13 STATUS CHECK passed

---

SECTION 3 -- MOMENT-LABEL DECISION SYSTEM

This section declares the complete labeling system governing all moment labels in
Sections 4-6. Each label has a declared decision rule. The system is a rule-governed
taxonomy, not a format guide.

Schema + instantiation:

| Label | Decision Rule | When to Apply | Not Applicable When | Required Format |
|-------|--------------|---------------|---------------------|-----------------|
| [e.g., SURPRISING] | [e.g., Prior expectation from the Register was violated -- subject responded in a meaningfully different direction, intensity, or framing] | [e.g., Register entry exists and response departs from it] | [e.g., Response differs from a vague general assumption with no register entry -- fix the register first] | [e.g., SURPRISING (expected: [Register -> Skeptic, Field: "Expected Objection": "..."], got: [...])] |
| CONFIRMING | Prior expectation from the Register was upheld -- subject said what was expected, validating a prior signal | Register entry exists and response matches it | Response consistent with undeclared assumption rather than specifically declared expectation | CONFIRMING (validates: [Register -> Practitioner, Field: "Expected Confirmation": "..."]) |
| INCONCLUSIVE | Notable signal present but direction genuinely ambiguous -- cannot be assigned to SURPRISING or CONFIRMING without additional evidence | Signal present; direction cannot be resolved by any register field | One of the above labels clearly fits -- do not use INCONCLUSIVE as a hedge | INCONCLUSIVE (closest register field: [Register -> Advocate, Field: "Expected Surprise"], ambiguity: [...]) |

Every labeled-moment section must end with one of:
  Option A: "All moments in this section are unambiguously SURPRISING or CONFIRMING --
             no INCONCLUSIVE moments observed."
  Option B: [Apply INCONCLUSIVE label to the ambiguous moment using the format above]

C-28 STATUS CHECK: [ ] Decision system complete -- all three labels have declared
decision rules and Not-Applicable conditions. INCONCLUSIVE fully specified.

SECTION 3 GATE
  [ ] All three labels have Decision Rule, When-to-Apply, Not-Applicable, and Required Format
  [ ] C-28 STATUS CHECK passed

---

PRE-INTERVIEW MASTER GATE

Before the first interview transcript begins, all structural prerequisites are
confirmed collectively satisfied, evidenced by named completed section gate statuses.
All four items must be checked.

PRE-INTERVIEW MASTER GATE
  [ ] SUBJECT CARDS COMPLETE -- SECTION 1 GATE: PASSED
      All three subject cards fully populated; sequence justification present;
      vocabulary signatures specific and auditable (C-22 STATUS CHECK confirmed at
      SECTION 1 GATE).

  [ ] EXPECTATION REGISTER POPULATED -- SECTION 2 GATE: PASSED
      All register cells filled; C-13 STATUS CHECK confirmed at SECTION 2 GATE.
      A PARTIAL register cannot activate the C-25 bridge.

  [ ] VOCABULARY SIGNATURES DECLARED FOR ALL SUBJECTS -- SECTION 1 GATE: PASSED
      (item 3 -- C-22 STATUS CHECK confirmed at SECTION 1 GATE). All three subjects
      have 3 specific vocabulary terms declared.

  [ ] MOMENT-LABEL DECISION TAXONOMY DECLARED -- SECTION 3 GATE: PASSED
      C-28 STATUS CHECK confirmed at SECTION 3 GATE. All three labels have declared
      decision rules including INCONCLUSIVE.

Section 4 begins only when all four items are checked.

---

SECTION 4 -- INTERVIEW: THE SKEPTIC

Transcript

Opening question: [Anchored in the Skeptic's declared prior knowledge and register --
probe what specifically grounds their resistance]

[Skeptic]: [Answer in distinct Skeptic voice. Declared vocab terms must appear
naturally per Document-Head Format Contract Rule 3.]

Follow-up (triggered by: "[exact phrase from preceding answer]"):
[follow-up anchored to prior answer]

[Skeptic]: [answer]

[2-3 more exchanges. Skeptic's primary objection must be explicitly stated -- it
becomes the objection whose lifecycle is tracked in Section 7.]

---

Vocabulary Audit -- Skeptic

Prerequisite check: C-22 for Skeptic confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 3 -- SECTION 1 GATE: PASSED). Proceeding with audit.

Schema + instantiation:

| Term | Status | Evidence |
|------|--------|----------|
| [e.g., "audit immutability"] | [e.g., FOUND] | [e.g., A2: "...the audit immutability requirement isn't negotiable here..."] |
| [Term 2] | | |
| [Term 3] | | |

Real data:

| Term | Status | Evidence |
|------|--------|----------|
| [Vocab Term 1 from Section 1] | | |
| [Vocab Term 2] | | |
| [Vocab Term 3] | | |

At least 1 of 3 terms must be FOUND. [ ] vocabulary contract closed

---

Moment Label -- Skeptic

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item 2 -- SECTION 2 GATE: PASSED). Register is source for "expected:" slot.
C-25 bridge is authorized to deploy.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Register -> Subject: Skeptic,
  Field: "{field_name}"], ...)

Ambiguity check: [Option A or Option B from Section 3 decision system]

---

Evidence Extraction -- Skeptic

Prerequisite check: C-27 dual taxonomy confirmed in PRE-INTERVIEW MASTER GATE --
SECTION 3 GATE: PASSED. Both dimensions defined per Document-Head Format Contract
Rule 4. Proceeding.

Schema + instantiation:

| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Strength Rationale |
|---------------|-------------|---------------------|-----------------|----------|--------------------|
| [e.g., "Integration with legacy audit trail is non-negotiable -- any workaround adds a sprint."] | [e.g., feasibility concern] | [e.g., GROUNDED -- has operated the audit trail process for 3 years] | [e.g., verbatim -- stated directly in A2: "non-negotiable"] | [e.g., strong] | [e.g., GROUNDED source stating explicitly with operational specificity; no hedging] |

Real data:

| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Strength Rationale |
|---------------|-------------|---------------------|-----------------|----------|--------------------|
| | | | | | |

SECTION 4 GATE
  [ ] Vocabulary contract closed -- at least 1 declared term FOUND in Skeptic's transcript
  [ ] Moment label references Register by subject name and field name
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Skeptic's primary objection explicitly stated and identifiable

---

SECTION 5 -- INTERVIEW: THE PRACTITIONER

[Same structure as Section 4, adapted for Practitioner persona. At least one question
must probe whether the Practitioner's operational reality speaks to -- or is silent
about -- the Skeptic's primary objection.]

Vocabulary Audit -- Practitioner

Prerequisite check: C-22 for Practitioner confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 3 -- SECTION 1 GATE: PASSED). Proceeding.

[Schema + instantiation + real data: same 3-column format as Section 4 Vocabulary Audit]

Moment Label -- Practitioner

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item 2 -- SECTION 2 GATE: PASSED). C-25 bridge authorized.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Register -> Subject: Practitioner,
  Field: "{field_name}"], ...)

Ambiguity check: [Option A or Option B]

Evidence Extraction -- Practitioner

Prerequisite check: C-27 dual taxonomy confirmed in PRE-INTERVIEW MASTER GATE --
SECTION 3 GATE: PASSED. "corroborated" now available for Origin-of-Claim when signal
matches Section 4 evidence.

[Schema + instantiation + real data: same 6-column format, fresh example row required
per Document-Head Format Contract Rule 2]

SECTION 5 GATE
  [ ] Vocabulary contract closed -- at least 1 declared term FOUND
  [ ] Moment label references Register by subject name and field name
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Practitioner's response to (or silence about) Skeptic's primary objection visible

---

SECTION 6 -- INTERVIEW: THE ADVOCATE

[Same structure. At least one vocab term must appear naturally. Opening question
anchored in the Advocate's declared evidential function. At least one question probes
the Advocate's response to the Skeptic's primary objection.]

Vocabulary Audit -- Advocate

Prerequisite check: C-22 for Advocate confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 3 -- SECTION 1 GATE: PASSED). Proceeding.

[Schema + instantiation + real data: same format]

Moment Label -- Advocate

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item 2 -- SECTION 2 GATE: PASSED). C-25 bridge authorized.

Ambiguity check: [Option A or Option B]

Evidence Extraction -- Advocate

Prerequisite check: C-27 dual taxonomy confirmed in PRE-INTERVIEW MASTER GATE --
SECTION 3 GATE: PASSED. "corroborated" available from Sections 4 and 5.

[Schema + instantiation + real data: same format]

SECTION 6 GATE
  [ ] Vocabulary contract closed -- at least 1 declared term FOUND
  [ ] Moment label references Register by subject name and field name
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Advocate's response to Skeptic's primary objection visible

---

SECTION 7 -- SYNTHESIS

Prerequisite confirmation: SECTION 4 GATE: PASSED, SECTION 5 GATE: PASSED,
SECTION 6 GATE: PASSED -- all three interview sections closed. Proceeding.

Patterns and Contradictions: Name 2-3 patterns or contradictions across all three
subjects. Cite specific evidence items by subject and response number.

Objection Lifecycle: Trace the Skeptic's primary objection.
  - Initial (Section 4): [state it]
  - Practitioner's response (Section 5): [addressed? transformed? silent? -- cite]
  - Advocate's response (Section 6): [persisted? transformed? resolved? -- cite]
  - Final verdict: PERSISTED | TRANSFORMED | RESOLVED
    [one sentence naming the evidence that determines the verdict]

Epistemic Weight Adjustment: For at least one evidence item, name when an objection
or validation comes from a GROUNDED source versus CONDITIONAL/INFERRED and adjust
synthesis weight accordingly. Required format: "Item [citation] is CONDITIONAL --
[subject] has not experienced [specific gap]. Treat as a risk to monitor, not a
blocker."

SECTION 7 GATE
  [ ] Objection lifecycle traced with verdict and citation
  [ ] At least one named epistemic weight adjustment present
  [ ] Patterns or contradictions cited with specific evidence references

---

SECTION 8 -- META-OBSERVATIONS

8A -- Simulation Fidelity: Name at least one specific grounding basis (documented
persona knowledge that anchored a specific answer) and at least one place where
constructed plausibility was exercised. Distinguish the two.

8B -- Voice Divergence: Name one concrete contrast between two subjects -- cite a
specific vocabulary choice, framing preference, or concern priority. Generic
role-level statements without specific cited differences fail.
```

---

## V-03 -- Phrasing Register: Conversational Voice with Named Format Contract

**Axis**: Phrasing register
**Hypothesis**: V-03 R9's conversational framing had BEFORE-INTERVIEW CHECKLIST
(C-31 PASS) and INTERVIEW N COMPLETE blocks (C-32 PASS), but its checklist items
referenced prerequisites by description rather than by named completed step status --
"all five columns are filled" rather than "STEP 1: COMPLETE". This fails C-34's
named-completion requirement. Fix: promote each checklist item to "STEP N: COMPLETE"
explicit named-completion form (C-34). For C-33, declare the four format rules in a
friendly-register preamble. C-35 point-of-use is added as "confirmed complete at
BEFORE-INTERVIEW CHECKLIST (item N -- STEP N: COMPLETE)" in conversational voice.

```
You are running a simulated stakeholder interview investigation for the feature
topic: {{topic}}.

This is a simulation -- the interviews are not real, but the voices, knowledge, and
concerns you give each subject should be grounded in their documented role and
experience. Your job is to produce evidence, not theatre: every answer should carry
information that could genuinely change how you think about the feature.

Take this in order. The structure is here to produce stronger evidence, not to
bureaucratize the work. Each part has a purpose; do not skip ahead.

---

HOW THIS DOCUMENT WORKS -- FOUR FORMAT RULES IN EFFECT THROUGHOUT

Before you start, here are four format rules that govern this entire document.
They apply in every section; you do not need to re-read them per section, but you
will be expected to follow them throughout.

1. GATE BLOCK FORMAT: Every time you finish a major section, end it with a named
   checklist block. Gate items belong inside that block -- not scattered in prose.
   Named block + enumerated items. If you finish a section and your gate is a
   paragraph, it is not a gate.

2. SCHEMA INSTANTIATION: Any table you declare with column headers needs at least one
   fully filled example row before your real data rows. A headers-only table is an
   open contract -- the reader cannot tell what a well-formed row looks like.

3. VOCABULARY EXERCISE: You will declare specific vocabulary terms for each subject
   in Step 1. Those terms need to appear naturally in that subject's transcript --
   at least one per subject. If you declare a term and it never appears in that
   subject's answers, the contract is open. Close it.

4. DUAL TAXONOMY: When you extract evidence, tag each item with two separate
   dimensions: (a) how close the subject is to the experience (GROUNDED/CONDITIONAL/
   INFERRED), and (b) how the claim came out of the transcript (verbatim/inferred/
   corroborated). These answer different questions and must be kept separate.

---

STEP 1 -- SET UP YOUR SUBJECTS

Before you write a single interview line, you need three things per subject: who they
are, what they already know (and do not know), and what you expect them to say.

For each subject, write a Subject Card with these fields:

  - Their role -- job title or function, specific enough to anchor their vocabulary
  - Their evidential function -- not their disposition, but what their structural
    position does for the evidence. Are they the baseline skeptic whose objection
    defines the problem space? The operational ground-truth carrier? The adoption
    advocate whose optimism either gets confirmed or tempered?
  - Their experience-proximity:
      GROUNDED: they have done this firsthand
      CONDITIONAL: adjacent experience, not direct
      INFERRED: reasoning about something they have not encountered
    Write one sentence explaining why this label fits.
  - Their prior knowledge -- what they know, what they have worked with. 2-3 sentences.
  - Their blind spots -- what they have NOT encountered. Keep this separate from prior
    knowledge. A subject's blind spots tell you how much weight to give their objections.
  - Their vocabulary signature -- 2-3 specific terms they would naturally use.
    Not general traits like "uses technical language" -- actual terms like "compliance
    window" or "rollback surface." Specific enough to look for by name in the transcript.

Once you have three Subject Cards, write one sentence explaining why you are running
the interviews in this specific order. Name the structural reason for your sequence.

Now populate the Expectation Register before any interview begins. Fill all five
columns for all three subjects before writing any dialogue. The Expected Surprise
column is important -- if you cannot imagine what would surprise you, you may not
have a real model of their position yet.

One filled example row before your real data (Schema Rule -- Format Contract Rule 2):

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [e.g., Skeptic -- Compliance Lead] | [e.g., Will require audit immutability guarantee before any green light] | [e.g., No API-driven approach has passed compliance review in this org] | [e.g., If guarantee exists, will confirm approval delay pain is real] | [e.g., Might concede current workaround creates compliance risk too -- turning objection back on status quo] |

Your data:

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [Skeptic name] | | | | |
| [Practitioner name] | | | | |
| [Advocate name] | | | | |

STEP 1 COMPLETE -- BEFORE MOVING ON
  [ ] All three Subject Cards have all six fields (Role, Evidential Function,
      Experience-Proximity with justification, Prior Knowledge, Blind Spots,
      Vocabulary Signature with 2-3 specific auditable terms per subject, not traits)
  [ ] Sequence justification sentence is present
  [ ] Expectation Register table is fully filled -- all five columns, all three subjects

---

STEP 2 -- YOUR LABELING SYSTEM

Before the interviews begin, establish a complete rule system for labeling notable
moments. This system governs everything in Step 3. All three labels need decision
rules declared here.

SURPRISING: Apply when the subject said something that violates a prior expectation
  you registered in the Expectation Register. The violation needs to be directional.
  If there is no register entry to serve as the "expected:" reference, do not apply
  SURPRISING -- fix the register first.
  Format: SURPRISING (expected: [Register -> Subject: {name}, Field: "{field}"],
    got: [what actually emerged])

CONFIRMING: Apply when the subject said what you expected, validating a prior signal.
  The validation traces to a named register field -- not a vague general assumption.
  Format: CONFIRMING (validates: [Register -> Subject: {name}, Field: "{field}"])

INCONCLUSIVE: Apply when something notable happened but you genuinely cannot tell
  which direction it points. Do not force it into SURPRISING or CONFIRMING.
  Format: INCONCLUSIVE (closest register field: [Register -> Subject: {name},
    Field: "{field}"], ambiguity: [why the direction cannot be resolved])

At the end of each interview's labeled-moment section, do one of:
  A. State: "All labeled moments in this interview are unambiguously SURPRISING or
     CONFIRMING -- no INCONCLUSIVE moments were present."
  B. Apply the INCONCLUSIVE label to the ambiguous moment.
The choice must be visible -- silence fails the ambiguity criterion.

STEP 2 COMPLETE -- BEFORE MOVING ON
  [ ] All three labels have decision rules declared -- SURPRISING, CONFIRMING,
      and INCONCLUSIVE. If any label is missing a rule, fix it before proceeding.

---

BEFORE THE FIRST INTERVIEW -- CONFIRM THESE FOUR THINGS

Before you write any dialogue, work through this checklist. Each item is a hard stop.

BEFORE-INTERVIEW CHECKLIST
  [ ] SUBJECT CARDS COMPLETE -- STEP 1: COMPLETE
      All three Subject Cards have all six fields. Vocabulary signatures contain
      specific auditable terms, not traits. Confirmed by STEP 1 COMPLETE above.

  [ ] EXPECTATION REGISTER POPULATED -- STEP 1: COMPLETE
      All five columns filled for all three subjects. The moment-labeling in Step 3
      depends on a fully populated register. A partially filled register cannot serve
      as the structural source for the "expected:" slot -- deploying it against a
      partial register does not earn credit for the bridge. Confirmed by STEP 1
      COMPLETE above.

  [ ] VOCABULARY SIGNATURES DECLARED FOR ALL SUBJECTS -- STEP 1: COMPLETE
      At least 2-3 specific auditable vocabulary terms per subject. Confirmed by
      STEP 1 COMPLETE above.

  [ ] MOMENT-LABEL DECISION RULES DECLARED -- STEP 2: COMPLETE
      All three labels have decision rules including INCONCLUSIVE. Confirmed by
      STEP 2 COMPLETE above.

If any item shows INCOMPLETE, return to the referenced step and fix it. All four
must be confirmed before writing any interview dialogue.

---

STEP 3 -- THE INTERVIEWS

Run the interviews in the order you justified in Step 1. For each interview:

1. Write the transcript. Opening question anchored in the subject's declared prior
   knowledge and blind spots. Follow-up questions triggered by specific things the
   subject just said:
     Follow-up (triggered by: "[exact phrase from their answer]")
   Let their declared vocabulary terms surface naturally in their answers.

2. Vocabulary check.

   Before running: vocabulary signatures for this subject were confirmed complete at
   BEFORE-INTERVIEW CHECKLIST (item 3 -- STEP 1: COMPLETE). Specific, auditable terms
   are in place. Proceeding with audit.

   Vocabulary Audit -- [Subject Name]:
   - "[Term 1]": FOUND in A[N] -- "[brief quote]" | NOT FOUND -- open contract
   - "[Term 2]": FOUND | NOT FOUND
   - "[Term 3]": FOUND | NOT FOUND
   Closing status: [ ] at least one term FOUND -- vocabulary contract closed

3. Moment label. Apply the decision system from Step 2. Reference the register by
   subject name and field name.

   Before applying: confirm that the Expectation Register was fully populated at
   BEFORE-INTERVIEW CHECKLIST (item 2 -- STEP 1: COMPLETE). The "expected:" slot has
   a structural source. C-25 bridge is authorized to deploy.

   [SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Register -> Subject: {name},
     Field: "{field}"], ...)
   Ambiguity check: [Apply Option A or Option B from Step 2 -- name which applies]

4. Extract the evidence. For each notable claim, record these five things:
   - What they said (or implied) -- the specific claim
   - What type of signal it is (adoption risk, feasibility concern, requirement gap, etc.)
   - Their experience-proximity to the claim (GROUNDED / CONDITIONAL / INFERRED)
   - How the claim came out of the transcript (Origin-of-Claim: verbatim / inferred /
     corroborated)
   - How strong the evidence is (strong / moderate / weak) and in one sentence, why

   Remember: experience-proximity and origin-of-claim are orthogonal -- Format Contract
   Rule 4 is in force. Keep them in separate columns.

   One filled example row before your real data (Format Contract Rule 2):
   | Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
   |---------------|-------------|---------------------|-----------------|----------|-----------|
   | "The approval queue backs up to 48 hours every sprint end -- this would eliminate that." | adoption signal | CONDITIONAL -- observed but has not owned the approval process | verbatim -- stated in A3: "48-hour delay" | moderate | Conditional proximity limits weight; verbatim basis is direct; moderate for not being the queue owner |

   Your evidence table:
   | Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
   |---------------|-------------|---------------------|-----------------|----------|-----------|
   | | | | | | |

5. Before moving to the next interview:

   INTERVIEW [N] COMPLETE -- BEFORE MOVING ON
     [ ] Vocabulary contract closed -- at least one declared term FOUND in transcript
     [ ] Moment label references Register by subject name and field name
     [ ] Both taxonomy dimensions (Experience-Proximity and Origin-of-Claim) populated
         for every evidence row and not conflated
     [ ] [Interview 1 only:] Skeptic's primary objection explicitly stated in transcript
     [ ] [Interview 2 only:] Practitioner's position on Skeptic's objection is visible
     [ ] [Interview 3 only:] Advocate's response to Skeptic's objection is visible

Run all three interviews before moving to Step 4.

---

STEP 4 -- SYNTHESIS

Once all three INTERVIEW COMPLETE checklists are closed, pull the threads together.

Patterns and contradictions: What appears across multiple subjects? Cite specific
evidence items (by subject and response number) -- do not summarize without reference.

The objection's fate: The Skeptic raised a primary objection in Interview 1. Trace
its movement and name a verdict:
  PERSISTED -- still standing after all three interviews
  TRANSFORMED -- changed form, narrowed, or reframed by Interviews 2 or 3
  RESOLVED -- explicitly addressed and closed by Interview 2 or 3 testimony
Cite the moments that support your verdict.

Epistemic weighting: Adjust the weight of at least one evidence item based on
experience-proximity. Name it explicitly: "This claim is CONDITIONAL -- [subject]
has not experienced [specific gap from their blind spots]. Treat as a risk to monitor
until a GROUNDED source confirms or refutes it."

SYNTHESIS COMPLETE -- BEFORE STEP 5
  [ ] Objection lifecycle traced with PERSISTED / TRANSFORMED / RESOLVED verdict
      and specific citation
  [ ] At least one named epistemic weight adjustment with CONDITIONAL/GROUNDED framing
  [ ] Patterns or contradictions cited with specific evidence references

---

STEP 5 -- CLOSING OBSERVATIONS

5A -- Where is the simulation grounded and where is it constructed? Name at least one
specific piece of documented persona knowledge or domain context that anchored an
answer, and at least one place where you exercised constructed plausibility. Distinguish
the two explicitly.

5B -- How are the voices actually different? Name one concrete contrast between two
subjects: a specific vocabulary choice, framing preference, or concern priority that
a reader could use to tell Subject A's answer apart from Subject B's. "They had
different roles" is not a voice observation. Name the specific term or framing.
```

---

## V-04 -- Role Sequence + Inertia Framing: Neutral-First with Inertia Baseline

**Axis**: Role sequence + inertia framing (combination)
**Hypothesis**: V-04 R9 used skeptic-first with Inertia Profile. This variation tests
neutral-first (NEUTRAL -> SKEPTIC -> ADVOCATE) where the neutral practitioner establishes
an unanchored operational baseline before the skeptic's objection frame arrives. The
Inertia Profile still grounds the shared baseline, but the neutral interview precedes
the skeptic, testing whether objection-lifecycle tracking (C-21) is achievable when
the initial objection state is established mid-sequence. R10 additions: unified
DOCUMENT-HEAD FORMAT CONTRACT (C-33); master gate evidenced by "INERTIA PROFILE GATE:
PASSED", "GATE 0A: PASSED", "C-28 STATUS CHECK: PASSED", "C-13 STATUS CHECK: PASSED"
(C-34); C-35 point-of-use throughout.

```
You are running a simulated stakeholder interview investigation for the feature
topic: {{topic}}.

This is not a real interview. It is a structured simulation grounded in documented
persona knowledge, producing evidence artifacts for downstream topic narrative decisions.

Complete all phases in order. Do not write any transcript line before the Inertia
Profile and Phase 0 setup are fully closed.

---

DOCUMENT-HEAD FORMAT CONTRACT (applies throughout this document)

All structural format requirements are declared here once. Any section that violates
a rule below fails against this declared contract.

RULE 1 -- GATE BLOCK FORMAT: Every phase gate is a consolidated named checklist block:
  PHASE N GATE
    [ ] item description
Items scattered in prose or appearing as isolated checkboxes outside a named block
violate this rule.

RULE 2 -- SCHEMA INSTANTIATION: Every table with structural column headers includes
at least one fully instantiated example row before any real data rows. Headers-only
tables are open schema contracts.

RULE 3 -- VOCABULARY EXERCISE: Each subject's declared vocabulary signature terms
appear at least once in that subject's interview transcript. Declared terms that
never surface in the transcript are declaration-without-enforcement.

RULE 4 -- DUAL TAXONOMY INDEPENDENCE: Evidence items carry two orthogonal tags --
experience-proximity (GROUNDED/CONDITIONAL/INFERRED) and origin-of-claim (verbatim/
inferred/corroborated) -- applied separately and non-interchangeably.

---

INERTIA PROFILE -- THE STATUS-QUO BASELINE

Before any subject speaks, profile the current-state workflow the feature would
replace, augment, or challenge. This is the shared baseline against which all labels,
objections, and evidence items are measured. Without a named baseline, SURPRISING and
CONFIRMING labels are measured only against individual priors -- weakening cross-
interview comparability.

Current-state workflow name: [Name the workflow as known in the org or domain]

Schema + instantiation (example row per Document-Head Format Contract Rule 2):

| Dimension | Current-State Description |
|-----------|--------------------------|
| [e.g., Workflow steps] | [e.g., "Manual approval queue -> spreadsheet audit log -> weekly compliance export -> legal sign-off every sprint"] |
| Cost / Friction | [e.g., "48-hour approval delay at sprint end; 3 FTE hours per export cycle"] |
| Risk surface | [e.g., "Audit trail lives in a single spreadsheet; no backup; compliance clock starts on export date, not event date"] |
| Why it persists | [e.g., "Familiar; legal has approved it before; alternatives have failed; changing requires re-certification"] |

Real data:

| Dimension | Current-State Description |
|-----------|--------------------------|
| Workflow steps | |
| Cost / Friction | |
| Risk surface | |
| Why it persists | |

INERTIA PROFILE GATE
  [ ] All four dimension rows in the real data table are populated
  [ ] "Why it persists" is named -- this is the inertia anchor for subject objections

---

PHASE 0 -- PRE-INTERVIEW STRUCTURE

Do not begin Phase 1 until the PRE-INTERVIEW MASTER GATE at the end of Phase 0 is
explicitly satisfied.

---

STEP 0A -- Subject Roster and Sequence Justification

Select three subjects. Sequence them: NEUTRAL -> SKEPTIC -> ADVOCATE.

The neutral practitioner runs first to establish an unanchored operational baseline
before the skeptic's objection frame arrives. This tests whether the operational
ground truth is independent of the skeptic's position, or already shaped by the same
inertia dynamics.

For each subject, complete the Subject Card template:

## Subject Card: [Role/Name]
- Role: [job title or function]
- Evidential Function: [what this subject's structural position does for the evidence
  chain. Examples: "establishes unanchored operational baseline that the Skeptic's
  objection is measured against"; "provides the primary objection surface after
  baseline is known"; "closes the sequence knowing both baseline and objection".]
- Experience-Proximity: GROUNDED | CONDITIONAL | INFERRED
  Justification: [one sentence -- note their proximity to the Inertia Profile workflow]
- Prior Knowledge: [2-3 sentences: what they know, have worked with, care about]
- Blind Spots: [1-2 sentences: what they have NOT encountered -- separate field]
- Inertia Stance: DEFENDER | NEUTRAL | CHALLENGER
  [One sentence explaining their relationship to the current-state workflow]
- Vocabulary Signature (auditable contract -- declared before transcript):
  - Term 1: [specific auditable term]
  - Term 2: [second specific term]
  - Term 3: [third specific term]

Sequence justification (one sentence): State why neutral-first, skeptic-second,
advocate-third is the optimal ordering for this specific investigation.

GATE 0A
  [ ] Subject 1 (Neutral): all seven fields populated -- Role, Evidential Function,
      Experience-Proximity with justification, Prior Knowledge, Blind Spots,
      Inertia Stance, three specific auditable vocabulary terms
  [ ] Subject 2 (Skeptic): same seven fields all populated
  [ ] Subject 3 (Advocate): same seven fields all populated
  [ ] Sequence justification sentence present

---

STEP 0B -- Moment-Label Decision System

Three labels govern all moment labels in this simulation. All decision rules are
declared here before any interview begins.

LABEL: SURPRISING
  Decision rule: Apply when a subject's response violates an expectation pre-registered
  in the Expectation Register (Step 0C) or violates an expectation grounded in the
  Inertia Profile. Note which source the "expected:" slot draws from.
  Required format: SURPRISING (expected: [Expectation Register -> Subject: {name},
    Field: "{field}"] OR [Inertia Profile -> Dimension: "{row}"], got: [what emerged])

LABEL: CONFIRMING
  Decision rule: Apply when a subject's response upholds an expectation pre-registered
  in the Expectation Register, or validates a dimension of the Inertia Profile.
  Required format: CONFIRMING (validates: [Expectation Register -> Subject: {name},
    Field: "{field}"] OR [Inertia Profile -> Dimension: "{row}"])

LABEL: INCONCLUSIVE
  Decision rule: Apply when a notable signal is present but direction is genuinely
  ambiguous and cannot be cleanly assigned to SURPRISING or CONFIRMING.
  Required format: INCONCLUSIVE (closest source: [Register/Inertia Profile -> ...],
    ambiguity: [why the direction cannot be resolved])

Every labeled moment section must end with Option A (no INCONCLUSIVE moments present)
or Option B (apply INCONCLUSIVE). Silence fails C-14.

C-28 STATUS CHECK
  [ ] All three labels declared with decision rules including INCONCLUSIVE

---

STEP 0C -- Expectation Register

Schema + instantiation (example row):

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [e.g., Neutral -- Operations Manager] | [e.g., Will report approval-delay pain as real but not their problem to solve] | [e.g., Will note any change requires change-management budget they do not have] | [e.g., Will confirm the Inertia Profile's Cost/Friction row is accurate] | [e.g., May reveal an undocumented workaround that partially solves the problem already] |
| Skeptic | | | | |
| Advocate | | | | |

Real data:

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [Neutral] | | | | |
| [Skeptic] | | | | |
| [Advocate] | | | | |

C-13 STATUS CHECK
  [ ] Register fully populated -- all cells have content for all three subjects and
      all five columns. A PARTIAL register cannot activate the C-25 bridge.

---

PRE-INTERVIEW MASTER GATE

Before the first interview transcript begins, all structural prerequisites are
confirmed collectively and fully satisfied, evidenced by named completed sub-gate
statuses. All five items must be checked.

PRE-INTERVIEW MASTER GATE
  [ ] INERTIA PROFILE COMPLETE -- INERTIA PROFILE GATE: PASSED
      All four dimension rows populated. "Why it persists" anchor named.

  [ ] SUBJECT CARDS COMPLETE -- GATE 0A: PASSED
      All three subject cards have all seven fields populated including Inertia Stance
      and three specific auditable vocabulary terms per subject.

  [ ] EXPECTATION REGISTER POPULATED -- C-13 STATUS CHECK: PASSED
      All three subjects, all five columns filled. PARTIAL register cannot activate
      C-25 bridge.

  [ ] VOCABULARY SIGNATURES DECLARED FOR ALL SUBJECTS -- GATE 0A: PASSED (item 3)
      Confirmed closed at GATE 0A: all subjects have 3 specific auditable terms.

  [ ] MOMENT-LABEL DECISION TAXONOMY DECLARED -- C-28 STATUS CHECK: PASSED
      All three labels with decision rules declared including INCONCLUSIVE.

Phase 1 begins only when all five boxes are checked.

---

PHASE 1 -- INTERVIEW: THE NEUTRAL PRACTITIONER

Transcript

Opening question: [Anchored in the Neutral Practitioner's prior knowledge and the
Inertia Profile -- probe whether their operational experience validates or complicates
the current-state description]

[Neutral Practitioner]: [Answer in this subject's distinct observational voice.
Vocabulary terms must appear naturally per Document-Head Format Contract Rule 3.
This subject's framing should be operational and factual, not advocacy or resistance.]

Follow-up (triggered by: "[exact phrase from the preceding answer that prompted this]"):
[follow-up anchored to prior answer]

[Neutral Practitioner]: [answer]

[Continue 2-3 more exchanges. This interview produces a factual operational baseline
-- what the current workflow actually costs or enables in practice. The Neutral's
testimony is the reference point that both the Skeptic and Advocate depart from.]

---

Vocabulary Audit -- Neutral Practitioner

Prerequisite check: C-22 for Neutral Practitioner confirmed FULLY SATISFIED in
PRE-INTERVIEW MASTER GATE (item 2 -- GATE 0A: PASSED). Proceeding.

- "[Term 1]": FOUND in A[N] -- "[quote]" | NOT FOUND
- "[Term 2]": FOUND | NOT FOUND
- "[Term 3]": FOUND | NOT FOUND

At least 1 of 3 terms must be FOUND. [ ] vocabulary contract closed

---

Moment Label -- Neutral Practitioner

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item 3 -- C-13 STATUS CHECK: PASSED). Expectation Register available. Proceeding.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Register -> Subject: Neutral
  Practitioner, Field: "{field}"] OR [Inertia Profile -> Dimension: "{row}"], ...)

C-25 bridge status: active -- C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER
GATE (item 3 -- C-13 STATUS CHECK: PASSED).

Ambiguity check: [Option A or Option B from Step 0B]

---

Evidence Extraction -- Neutral Practitioner

Prerequisite check: C-27 dual taxonomy confirmed -- Document-Head Format Contract
Rule 4 in force; confirmed in PRE-INTERVIEW MASTER GATE items 2 and 5.

Example row (schema instantiation per Rule 2):
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| [e.g., "We spend three hours every sprint end on the export -- but that time is already budgeted."] | [e.g., scope signal] | [e.g., GROUNDED -- owns the export process weekly] | [e.g., verbatim -- stated in A2: "three hours"] | [e.g., moderate] | [e.g., GROUNDED but scope signal, not adoption signal; cost is known but acceptance implied, not stated] |

Real data:
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| | | | | | |

---

PHASE 1 GATE
  [ ] At least one vocabulary term FOUND in Neutral Practitioner's transcript
  [ ] Moment label references Register or Inertia Profile by name and field/row
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Neutral Practitioner's operational baseline is established and identifiable

---

PHASE 2 -- INTERVIEW: THE SKEPTIC

Transcript

Opening question: [Anchored in the Skeptic's declared prior knowledge and Inertia
Stance -- probe what specifically grounds their defense of the current-state workflow,
knowing the neutral baseline from Phase 1]

[Skeptic]: [Answer in distinct Skeptic voice. Note the contrast with Neutral
Practitioner's observational framing -- the Skeptic should sound like someone
defending a position.]

Follow-up (triggered by: "[exact phrase from preceding answer]"):
[follow-up anchored to prior answer]

[Skeptic]: [answer]

[Continue 2-3 more exchanges. At least one question must probe whether the Skeptic's
objection is consistent with, contradicts, or extends the Neutral's baseline from
Phase 1. The Skeptic's primary objection must be explicitly stated -- this starts
the objection lifecycle tracked in Phase 4.]

---

Vocabulary Audit -- Skeptic

Prerequisite check: C-22 for Skeptic confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 2 -- GATE 0A: PASSED). Proceeding.

[Same audit format as Phase 1]

---

Moment Label -- Skeptic

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item 3 -- C-13 STATUS CHECK: PASSED). C-25 bridge authorized.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Register -> Subject: Skeptic,
  Field: "{field}"] OR [Inertia Profile -> Dimension: "{row}"], ...)

Ambiguity check: [Option A or Option B]

---

Evidence Extraction -- Skeptic

Prerequisite check: C-27 dual taxonomy confirmed -- Document-Head Format Contract
Rule 4 in force. "corroborated" now available for Origin-of-Claim when signal is
consistent with Phase 1 Neutral evidence.

[Same table format as Phase 1. Fresh example row required per Rule 2.]

PHASE 2 GATE
  [ ] At least one vocabulary term FOUND in Skeptic's transcript
  [ ] Moment label references Register or Inertia Profile
  [ ] Both taxonomy dimensions populated for every evidence row
  [ ] Skeptic's primary objection explicitly stated -- objection lifecycle begins here

---

PHASE 3 -- INTERVIEW: THE ADVOCATE

Transcript

Opening question: [Anchored in the Advocate's declared evidential function, knowing
both the Neutral's operational baseline and the Skeptic's primary objection]

[Advocate]: [Answer in distinct voice -- framing and vocabulary distinct from both
prior subjects]

Follow-up (triggered by: "[exact phrase from preceding answer]"):
[follow-up anchored to prior answer]

[Advocate]: [answer]

[Continue 2-3 more exchanges. At least one question probes the Advocate's response to
the Skeptic's objection. At least one question references the Neutral's operational
baseline from Phase 1.]

---

Vocabulary Audit -- Advocate

Prerequisite check: C-22 for Advocate confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 2 -- GATE 0A: PASSED). Proceeding.

[Same audit format]

---

Moment Label -- Advocate

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item 3 -- C-13 STATUS CHECK: PASSED). C-25 bridge authorized.

[Format with Register and/or Inertia Profile sources]

Ambiguity check: [Option A or Option B]

---

Evidence Extraction -- Advocate

Prerequisite check: C-27 dual taxonomy confirmed -- Document-Head Format Contract
Rule 4 in force. "corroborated" available from Phases 1 and 2.

[Same table format. Fresh example row required per Rule 2.]

PHASE 3 GATE
  [ ] At least one vocabulary term FOUND in Advocate's transcript
  [ ] Moment label references Register or Inertia Profile
  [ ] Both taxonomy dimensions populated for every evidence row
  [ ] Advocate's response to Skeptic's primary objection visible

---

PHASE 4 -- CROSS-INTERVIEW SYNTHESIS

Prerequisite confirmation: PHASE 1 GATE: PASSED, PHASE 2 GATE: PASSED, PHASE 3 GATE:
PASSED -- all three interview phases closed. Proceeding.

Patterns and Contradictions

Name at least one convergence or contradiction across the three subjects, citing
specific evidence items by subject and response number. Note whether the Neutral
Practitioner's baseline was corroborated or contradicted by the Skeptic or Advocate.

Objection Lifecycle

Note: in this variation, the objection lifecycle begins at Phase 2 (Skeptic). Phase 1
(Neutral) establishes the baseline before the objection appears.

  - Neutral baseline (Phase 1): [state the operational baseline established]
  - Initial objection (Phase 2): [state the Skeptic's primary objection]
  - Advocate's response (Phase 3): [persisted? transformed? resolved? -- cite]
  - Final verdict: PERSISTED | TRANSFORMED | RESOLVED
    [one sentence naming the evidence]

Inertia Resistance Assessment

Compare the Neutral and Skeptic positions against the Inertia Profile:
  - Does the Neutral Practitioner's testimony validate or complicate the "Why it
    persists" row? Name the finding.
  - Does the Skeptic's objection map to a specific Inertia Profile dimension?
    Name the row.

Epistemic Weight Adjustment

Adjust the weight of at least one evidence item based on Experience-Proximity and
Inertia Stance. Required format: "Item [citation] is CONDITIONAL -- [subject] is a
[Inertia Stance] who has not experienced [specific blind spot]. Treat as [risk to
monitor | conditional blocker | inertia anchor] rather than confirmed evidence."

PHASE 4 GATE
  [ ] Objection lifecycle traced with verdict and citation (starting from Phase 2)
  [ ] Inertia Profile assessed against at least one subject's testimony
  [ ] At least one epistemic weight adjustment referencing Experience-Proximity
      and Inertia Stance
  [ ] Convergence or contradiction cited with specific evidence references

---

PHASE 5 -- META-OBSERVATIONS

PHASE 5A -- Simulation Fidelity: Name at least one specific grounding basis and at
least one place where constructed plausibility was exercised. Note whether the Inertia
Profile was grounded in documented workflow knowledge or constructed from role logic.

PHASE 5B -- Voice Divergence: Name one concrete contrast between two subjects. The
Neutral/Skeptic contrast is particularly diagnostic -- name what the observational
framing sounds like versus the defensive framing, citing specific terms.
```

---

## V-05 -- Output Format + Inertia Framing: Table-Heavy Evidence with Inertia Baseline

**Axis**: Output format + inertia framing (combination)
**Hypothesis**: V-04 R9 showed the Inertia Profile adds structural grounding to
SURPRISING/CONFIRMING labels. V-02 R9 showed table-heavy output enforces dual taxonomy
by column structure. This variation combines both: the Inertia Profile is declared as
a structured table (not prose), and all evidence, vocabulary audits, and subject cards
are in table format. The combination tests whether the Inertia Profile table can serve
as a named sub-gate that the master gate closes against -- giving C-34 a fourth named
completion source beyond Subject Cards, Register, and Taxonomy. Evidence tables include
an Inertia Profile Row column, making the connection between individual claims and the
shared baseline structurally explicit.

```
You are running a simulated stakeholder interview investigation for the feature
topic: {{topic}}.

This is a structured simulation -- not a real interview -- grounded in documented
persona knowledge and producing evidence artifacts for downstream topic decisions.

---

DOCUMENT-HEAD FORMAT CONTRACT (applies throughout this document)

All structural format requirements are declared in this single named contract.
Downstream sections execute against these rules; they do not re-declare them.

RULE 1 -- GATE BLOCK FORMAT: Every section ends with a named gate block:
  SECTION N GATE
    [ ] item description
Gate items in prose or isolated checkboxes outside a named block violate this rule.

RULE 2 -- SCHEMA INSTANTIATION: Every table with structural column headers includes
at least one fully instantiated example row before real data rows. A headers-only
table is an open contract.

RULE 3 -- VOCABULARY EXERCISE: Each subject's declared vocabulary signature terms
appear at least once in that subject's interview transcript.

RULE 4 -- DUAL TAXONOMY INDEPENDENCE: Evidence items carry two orthogonal tags
applied separately: experience-proximity (GROUNDED/CONDITIONAL/INFERRED) and
origin-of-claim (verbatim/inferred/corroborated). Must not be conflated.

---

SECTION 0 -- INERTIA PROFILE

Before any subject speaks, document the current-state workflow in structured table
form. This is the shared baseline for all SURPRISING/CONFIRMING/INCONCLUSIVE labels.
Label resonance is only comparable across interviews when all subjects are measured
against the same named baseline.

Schema + instantiation:

| Dimension | Description | Inertia Weight |
|-----------|-------------|----------------|
| [e.g., Workflow steps] | [e.g., "Manual approval queue -> spreadsheet log -> weekly export -> legal sign-off every sprint"] | [e.g., high -- embedded in legal workflow] |
| Cost / Friction | [e.g., "48-hour sprint-end delay; 3 FTE hours per export cycle"] | [e.g., medium -- known but accepted as normal] |
| Risk surface | [e.g., "Audit trail in one analyst's spreadsheet; compliance clock tied to export date not event date"] | [e.g., high -- compliance exposure not widely known] |
| Why it persists | [e.g., "Legal has approved it; alternatives have failed twice; change requires re-certification"] | [e.g., very high -- institutional memory and sunk cost] |

Real data:

| Dimension | Description | Inertia Weight |
|-----------|-------------|----------------|
| Workflow steps | | |
| Cost / Friction | | |
| Risk surface | | |
| Why it persists | | |

SECTION 0 GATE
  [ ] All four dimension rows in the real data table are populated
  [ ] "Why it persists" names a specific institutional or structural anchor
  [ ] Inertia Weight column populated for all four rows

---

SECTION 1 -- SUBJECT CARDS AND SEQUENCE

Complete the Subject Card table. Schema row is required instantiation example.

Schema + instantiation:

| Field | Skeptic | Practitioner | Advocate |
|-------|---------|--------------|----------|
| Role | [e.g., "Senior Compliance Analyst, 8 years in regulated environments"] | | |
| Evidential Function | [e.g., "Establishes the compliance objection surface -- subsequent subjects must address it or leave it standing"] | | |
| Experience-Proximity | [e.g., "GROUNDED -- has personally managed two audit trail failures in production"] | | |
| Prior Knowledge | [e.g., "Knows current workaround; seen two failed migrations; understands compliance clock"] | | |
| Blind Spots | [e.g., "Has not used the new API-driven approach -- resistance grounded in prior failures"] | | |
| Inertia Stance | [e.g., "DEFENDER -- explicitly defends the 'Why it persists' row: re-certification risk"] | | |
| Vocab Term 1 | [e.g., "audit immutability"] | | |
| Vocab Term 2 | [e.g., "compliance window"] | | |
| Vocab Term 3 | [e.g., "chain-of-custody"] | | |

Real data:

| Field | Skeptic | Practitioner | Advocate |
|-------|---------|--------------|----------|
| Role | | | |
| Evidential Function | | | |
| Experience-Proximity | | | |
| Prior Knowledge | | | |
| Blind Spots | | | |
| Inertia Stance | | | |
| Vocab Term 1 | | | |
| Vocab Term 2 | | | |
| Vocab Term 3 | | | |

Sequence justification (one sentence): State why the chosen interview order is
optimal for this investigation, naming the structural reason.

C-22 STATUS CHECK: [ ] All three subjects have 3 specific vocabulary terms in the
real data table. Trait descriptors fail.

SECTION 1 GATE
  [ ] All nine rows populated in the real data table for all three subjects
  [ ] Sequence justification present
  [ ] C-22 STATUS CHECK passed

---

SECTION 2 -- EXPECTATION REGISTER

Schema + instantiation (example row):

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise | Inertia Profile Row |
|---------|------------------|--------------------|-----------------------|-------------------|---------------------|
| [e.g., Skeptic -- Compliance Analyst] | [e.g., Will require audit immutability before green light] | [e.g., No API-driven approach has passed compliance review here] | [e.g., If guarantee exists, will confirm approval-delay pain is real] | [e.g., May acknowledge current workaround creates compliance risk -- turning objection back on status quo] | [e.g., "Why it persists": re-certification risk] |
| Practitioner | | | | | |
| Advocate | | | | | |

Real data:

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise | Inertia Profile Row |
|---------|------------------|--------------------|-----------------------|-------------------|---------------------|
| [Skeptic] | | | | | |
| [Practitioner] | | | | | |
| [Advocate] | | | | | |

The Inertia Profile Row column names which dimension each subject's position is most
tethered to -- making label resonance structurally comparable across interviews.

C-13 STATUS CHECK: [ ] All cells populated including Inertia Profile Row column.
PARTIAL register cannot activate the C-25 bridge.

SECTION 2 GATE
  [ ] All cells in real data table populated including Inertia Profile Row
  [ ] C-13 STATUS CHECK passed

---

SECTION 3 -- MOMENT-LABEL DECISION SYSTEM

Schema + instantiation:

| Label | Decision Rule | When to Apply | Not Applicable When | Required Format |
|-------|--------------|---------------|---------------------|-----------------|
| [e.g., SURPRISING] | [e.g., Prior expectation violated -- departed from Register or Inertia Profile expectation in direction, intensity, or framing] | [e.g., Register or Inertia Profile entry exists and response departs from it] | [e.g., No register entry or Inertia Profile row names the violated expectation -- fix the source first] | [e.g., SURPRISING (expected: [Register -> Skeptic, Field: "..."] OR [Inertia Profile -> Dimension: "..."], got: [...])] |
| CONFIRMING | Prior expectation upheld -- validates a Register entry or Inertia Profile dimension | Register or Inertia Profile entry exists and response matches it | Response consistent with undeclared general assumption rather than a named source | CONFIRMING (validates: [Register -> Practitioner, Field: "..."] OR [Inertia Profile -> Dimension: "..."]) |
| INCONCLUSIVE | Notable signal present but direction genuinely ambiguous -- cannot be assigned to SURPRISING or CONFIRMING | Signal present; direction unresolvable by any named source | One of the above labels clearly fits | INCONCLUSIVE (closest source: [Register/Inertia Profile -> ...], ambiguity: [...]) |

All labeled-moment sections must end with Option A (no INCONCLUSIVE) or Option B
(apply INCONCLUSIVE). Silence fails C-14.

C-28 STATUS CHECK: [ ] All three labels declared with decision rules. INCONCLUSIVE
fully specified.

SECTION 3 GATE
  [ ] All three labels have Decision Rule, When-to-Apply, Not-Applicable, Required Format
  [ ] C-28 STATUS CHECK passed

---

PRE-INTERVIEW MASTER GATE

Before the first interview transcript begins, all structural prerequisites are
confirmed collectively satisfied, evidenced by named completed section gate statuses.
All five items must be checked.

PRE-INTERVIEW MASTER GATE
  [ ] INERTIA PROFILE COMPLETE -- SECTION 0 GATE: PASSED
      All four dimension rows populated including Inertia Weight; "Why it persists"
      anchor named.

  [ ] SUBJECT CARDS COMPLETE -- SECTION 1 GATE: PASSED
      All three subject cards fully populated with all nine rows including Inertia
      Stance and vocabulary signatures. C-22 STATUS CHECK confirmed at SECTION 1 GATE.

  [ ] EXPECTATION REGISTER POPULATED -- SECTION 2 GATE: PASSED
      All cells filled including Inertia Profile Row column. C-13 STATUS CHECK
      confirmed at SECTION 2 GATE. PARTIAL register cannot activate C-25 bridge.

  [ ] VOCABULARY SIGNATURES DECLARED FOR ALL SUBJECTS -- SECTION 1 GATE: PASSED
      (item 3 -- C-22 STATUS CHECK confirmed at SECTION 1 GATE).

  [ ] MOMENT-LABEL DECISION TAXONOMY DECLARED -- SECTION 3 GATE: PASSED
      All three labels with decision rules. INCONCLUSIVE fully specified.

Section 4 begins only when all five items are checked.

---

SECTION 4 -- INTERVIEW: THE SKEPTIC

Transcript

Opening question: [Anchored in the Skeptic's declared Inertia Stance and prior
knowledge -- probe which row of the Inertia Profile grounds their resistance]

[Skeptic]: [Answer in distinct Skeptic voice. Vocabulary terms must appear naturally
per Document-Head Format Contract Rule 3. Skeptic's framing should map to a specific
Inertia Profile row -- named in the evidence extraction.]

Follow-up (triggered by: "[exact phrase from preceding answer]"):
[follow-up anchored to prior answer]

[Skeptic]: [answer]

[2-3 more exchanges. Skeptic's primary objection must be explicitly stated and tied
to an Inertia Profile row.]

---

Vocabulary Audit -- Skeptic

Prerequisite check: C-22 for Skeptic confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 2 -- SECTION 1 GATE: PASSED). Proceeding.

Schema + instantiation:

| Term | Status | Evidence | Inertia Profile Row |
|------|--------|----------|---------------------|
| [e.g., "audit immutability"] | [e.g., FOUND] | [e.g., A2: "...audit immutability requirement isn't negotiable..."] | [e.g., Risk surface] |
| [Term 2] | | | |
| [Term 3] | | | |

Real data:

| Term | Status | Evidence | Inertia Profile Row |
|------|--------|----------|---------------------|
| [Vocab Term 1] | | | |
| [Vocab Term 2] | | | |
| [Vocab Term 3] | | | |

[ ] vocabulary contract closed -- at least 1 term FOUND

---

Moment Label -- Skeptic

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item 3 -- SECTION 2 GATE: PASSED). Register and Inertia Profile available as sources
for "expected:" slot. C-25 bridge authorized.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Register -> Subject: Skeptic,
  Field: "{field}"] OR [Inertia Profile -> Dimension: "{row}"], ...)

Ambiguity check: [Option A or Option B from Section 3 decision system]

---

Evidence Extraction -- Skeptic

Prerequisite check: C-27 dual taxonomy confirmed in PRE-INTERVIEW MASTER GATE --
SECTION 3 GATE: PASSED. Document-Head Format Contract Rule 4 in force.

Schema + instantiation:

| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Strength Rationale | Inertia Profile Row |
|---------------|-------------|---------------------|-----------------|----------|--------------------|---------------------|
| [e.g., "Any API-driven workaround still needs to pass the same re-certification -- three months minimum."] | [e.g., feasibility concern] | [e.g., GROUNDED -- has run re-certification twice] | [e.g., verbatim -- A3: "three months minimum"] | [e.g., strong] | [e.g., GROUNDED, verbatim, specific operational experience; directness warrants strong] | [e.g., Why it persists] |

Real data:

| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Strength Rationale | Inertia Profile Row |
|---------------|-------------|---------------------|-----------------|----------|--------------------|---------------------|
| | | | | | | |

SECTION 4 GATE
  [ ] Vocabulary contract closed -- at least 1 declared term FOUND
  [ ] Moment label references Register or Inertia Profile by name and field/row
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Inertia Profile Row column populated for each evidence item
  [ ] Skeptic's primary objection explicitly stated

---

SECTION 5 -- INTERVIEW: THE PRACTITIONER

[Same structure as Section 4. At least one question probes whether the Practitioner's
operational experience validates, complicates, or is silent about the Skeptic's
primary objection and its associated Inertia Profile row.]

Vocabulary Audit -- Practitioner

Prerequisite check: C-22 for Practitioner confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 2 -- SECTION 1 GATE: PASSED). Proceeding.

[Schema + instantiation + real data: same 4-column format as Section 4 Vocabulary Audit]

Moment Label -- Practitioner

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item 3 -- SECTION 2 GATE: PASSED). C-25 bridge authorized. "corroborated" available
for Origin-of-Claim when signal matches Section 4 evidence.

Ambiguity check: [Option A or Option B]

Evidence Extraction -- Practitioner

Prerequisite check: C-27 dual taxonomy confirmed in PRE-INTERVIEW MASTER GATE --
SECTION 3 GATE: PASSED. Document-Head Format Contract Rule 4 in force.

[Same 7-column format as Section 4. Fresh example row required per Document-Head
Format Contract Rule 2.]

SECTION 5 GATE
  [ ] Vocabulary contract closed -- at least 1 declared term FOUND
  [ ] Moment label references Register or Inertia Profile
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Inertia Profile Row column populated for each evidence item
  [ ] Practitioner's response to Skeptic's primary objection visible

---

SECTION 6 -- INTERVIEW: THE ADVOCATE

[Same structure. At least one question probes the Advocate's response to the Skeptic's
primary objection and whether it maps to the same Inertia Profile row.]

Vocabulary Audit -- Advocate

Prerequisite check: C-22 for Advocate confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 2 -- SECTION 1 GATE: PASSED). Proceeding.

[Same 4-column audit format]

Moment Label -- Advocate

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE
(item 3 -- SECTION 2 GATE: PASSED). C-25 bridge authorized.

Ambiguity check: [Option A or Option B]

Evidence Extraction -- Advocate

Prerequisite check: C-27 dual taxonomy confirmed in PRE-INTERVIEW MASTER GATE --
SECTION 3 GATE: PASSED. "corroborated" available from Sections 4 and 5.

[Same 7-column format. Fresh example row required per Rule 2.]

SECTION 6 GATE
  [ ] Vocabulary contract closed -- at least 1 declared term FOUND
  [ ] Moment label references Register or Inertia Profile
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Inertia Profile Row column populated for each evidence item
  [ ] Advocate's response to Skeptic's primary objection visible

---

SECTION 7 -- SYNTHESIS

Prerequisite confirmation: SECTION 4 GATE: PASSED, SECTION 5 GATE: PASSED,
SECTION 6 GATE: PASSED -- all three interview sections closed. Proceeding.

Patterns and Contradictions: Name 2-3 patterns or contradictions. Cite specific
evidence items by subject and response number. For at least one pattern, name which
Inertia Profile row it maps to.

Inertia Resistance Map:

Schema + instantiation:

| Subject | Inertia Profile Row | Testimony Direction | Implication |
|---------|---------------------|---------------------|-------------|
| [e.g., Skeptic] | [e.g., Why it persists] | [e.g., VALIDATES -- confirms re-certification risk is real and active] | [e.g., Inertia anchor: treat as constraint, not objection to overcome with better framing] |
| Practitioner | | | |
| Advocate | | | |

Real data:

| Subject | Inertia Profile Row | Testimony Direction | Implication |
|---------|---------------------|---------------------|-------------|
| Skeptic | | | |
| Practitioner | | | |
| Advocate | | | |

Objection Lifecycle:
  - Initial objection (Section 4): [state it and name the Inertia Profile row]
  - Practitioner's response (Section 5): [addressed? transformed? silent? -- cite]
  - Advocate's response (Section 6): [persisted? transformed? resolved? -- cite]
  - Final verdict: PERSISTED | TRANSFORMED | RESOLVED
    [one sentence naming the evidence]

Epistemic Weight Adjustment: For at least one evidence item, adjust synthesis weight
based on Experience-Proximity and Inertia Stance. Required format: "Item [citation]
is CONDITIONAL -- [subject] is a [Inertia Stance] who has not experienced [specific
blind spot]. The objection maps to Inertia Profile '[row]'. Treat as [inertia anchor
/ risk to monitor / conditional blocker] until a GROUNDED source confirms or refutes."

SECTION 7 GATE
  [ ] Objection lifecycle traced with verdict and Inertia Profile row reference
  [ ] Inertia Resistance Map complete for all three subjects (schema instantiation
      + real data)
  [ ] At least one epistemic weight adjustment referencing Inertia Stance
  [ ] Patterns cited with specific evidence references

---

SECTION 8 -- META-OBSERVATIONS

8A -- Simulation Fidelity: Name at least one specific grounding basis -- documented
persona knowledge, domain context, or Inertia Profile dimension -- that anchored a
specific answer. Name at least one place where constructed plausibility was exercised.
Distinguish the two.

8B -- Voice Divergence: Name one concrete contrast between two subjects, citing a
specific vocabulary choice, framing preference, or concern priority. Note whether the
contrast maps to different Inertia Stances -- e.g., a DEFENDER using compliance
terminology versus a CHALLENGER using efficiency terminology for the same workflow.
```
