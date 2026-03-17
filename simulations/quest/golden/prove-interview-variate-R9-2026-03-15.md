# prove-interview — Prompt Variations R9
# Date: 2026-03-15
# Rubric: prove-interview-rubric-v9-2026-03-15.md
# Round: 9 (C-31/C-32 primary targets; denominator /24)

---

## Variation Axes Selected

| Axis | Description |
|------|-------------|
| Lifecycle emphasis | PRE-INTERVIEW MASTER GATE naming all 4 prerequisites (Subject Cards, Register, Vocab Signatures, Decision Taxonomy); PHASE N GATE checklist blocks throughout |
| Output format | Schema contract applied to gate blocks; PRE-INTERVIEW MASTER GATE as named schema element; SECTION N GATE as named blocks; C-30 prerequisite confirmations restored (fixing R8 fail) |
| Phrasing register | Conversational framing with explicitly named accountability blocks; fixes R8 PARTIAL losses (C-19, C-20, C-22, C-30) |
| Role sequence + Inertia framing | Skeptic-first x status-quo competitor baseline; master gate names 4 items including Inertia Profile grounding |
| Output format + Lifecycle emphasis | Full combination: schema contract x explicit lifecycle; C-31 4-row prerequisite table; C-32 named PHASE N GATE blocks for every phase |

Single-axis variations: V-01 (lifecycle emphasis), V-02 (output format), V-03 (phrasing register)
Combination variations: V-04 (role sequence + inertia framing), V-05 (output format + lifecycle emphasis)

New v9 territory probed:
- **C-31** (all five): PRE-INTERVIEW MASTER GATE naming all 4 prerequisites before the first transcript. R8 V-01 Step 0D had only 3 items (C-22/C-13/C-28); Subject Cards complete was not explicitly named. V-02 had no master gate equivalent. V-03 had no gate at all.
- **C-32** (all five): Phase gates as consolidated named checklist blocks -- "PHASE N GATE: [ ] item..." -- not scattered inline checkboxes or summary sentences. R8 V-02 had only inline checkboxes (C-20 PARTIAL). R8 V-03 had "do three things after each interview" instruction language (C-20 PARTIAL).

---

## V-01 -- Lifecycle Emphasis: 4-Item Master Gate

**Axis**: Lifecycle emphasis
**Hypothesis**: The single gap between R8 V-01 (100/100 against v8) and v9 C-31 is that Step 0D named C-22/C-13/C-28 but did not explicitly name "Subject Cards complete" as a separate enumerated item. Adding it as item 1 of the master gate closes C-31 -- the gate now names all four required prerequisites. Phase gates were already formatted as named checklist blocks (PHASE N GATE: [ ] ...) in R8 V-01, so C-32 carries forward without modification. V-01 is the minimal delta variation: one item added, maximum coverage maintained.

```
You are running a simulated stakeholder interview investigation for the feature topic: {{topic}}.

This is not a real interview. It is a structured simulation grounded in documented persona
knowledge, producing evidence artifacts for downstream topic narrative decisions.

Complete all phases in order. Do not write any transcript line before Phase 0 is fully closed.

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
- Evidential Function: [what this subject's structural position does for the evidence chain --
  not their disposition, their contribution. Example: "establishes the objection surface
  that the practitioner and advocate must speak to or leave standing"]
- Experience-Proximity: GROUNDED | CONDITIONAL | INFERRED
  Justification: [one sentence -- why does this subject carry this proximity level?]
- Prior Knowledge: [2-3 sentences: what they know, have worked with, care about]
- Blind Spots: [1-2 sentences: what they have NOT encountered -- a separate field from
  Prior Knowledge]
- Vocabulary Signature (auditable contract -- declared before transcript):
  - Term 1: [a specific term this persona uses, distinctive enough to audit against transcript]
  - Term 2: [a second distinctive term]
  - Term 3: [a third distinctive term]

Sequence justification (one sentence): State why skeptic-first, practitioner-second,
advocate-third is the optimal ordering for this specific investigation.

GATE 0A:
  [ ] Subject 1 (Skeptic): Role, Evidential Function, Experience-Proximity + justification
      sentence, Prior Knowledge, Blind Spots, three vocabulary terms -- all six fields populated
  [ ] Subject 2 (Practitioner): same six fields all populated
  [ ] Subject 3 (Advocate): same six fields all populated
  [ ] Sequence justification sentence present

---

STEP 0B -- Moment-Label Decision System

IMPORTANT: This step declares a complete decision system governing all moment labels
in this simulation. Individual labels without this declared system fail C-28 at rubric
scoring. This is not a format reminder -- it is the rule set that governs label selection.

## Moment-Label Decision System

Three labels are available. The decision rule for each is declared here. These rules
govern every label applied in Phases 1, 2, and 3.

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
  signal. The validation must be traceable to a named register field -- not inferred.
  Required format: CONFIRMING (validates: [Expectation Register -> Subject: {name},
    Field: "{field}"])

LABEL: INCONCLUSIVE
  Decision rule: Apply when a notable signal is present -- something happened worth
  marking -- but the direction is genuinely ambiguous and cannot be cleanly assigned to
  either the SURPRISING or CONFIRMING category without additional evidence. Use this
  label rather than forcing an unclear moment into SURPRISING or CONFIRMING.
  Required format: INCONCLUSIVE (closest register field: [Expectation Register ->
    Subject: {name}, Field: "{field}"], ambiguity: [why the direction cannot be resolved])

Every labeled moment section in Phases 1-3 must also end with one of these two statements:
  Option A: "All labeled moments in this phase are unambiguously SURPRISING or CONFIRMING.
             No INCONCLUSIVE moments were present."
  Option B: [Apply INCONCLUSIVE label to the ambiguous moment]
Silence -- applying only SURPRISING and CONFIRMING with no acknowledgment of Option A -- fails C-14.

C-28 STATUS CHECK:
  [ ] Decision system complete -- all three labels declared with decision rules,
      including INCONCLUSIVE. If any label is missing a decision rule, stop and
      complete it before proceeding.

---

STEP 0C -- Expectation Register

Declare prior expectations for each subject before any transcript begins. This register
is the mandatory structural source for all SURPRISING/CONFIRMING labels -- the "expected:"
slot in the moment-label format must point to a named row and field here.

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [Skeptic name] | | | | |
| [Practitioner name] | | | | |
| [Advocate name] | | | | |

The Expected Surprise column is mandatory. An empty cell means you have not formed a
prior model that can be violated -- fill it before proceeding.

C-13 STATUS CHECK:
  [ ] Register fully populated -- all cells have content for all three subjects and
      all five columns. If any cell is empty, C-13 is PARTIAL -- fix before proceeding.
      A PARTIAL C-13 cannot activate the C-25 bridge in evidence extraction.

---

PRE-INTERVIEW MASTER GATE

Before the first interview transcript begins, this gate confirms that all structural
prerequisites for the interview phase are collectively and fully satisfied.
All four items must be checked before Phase 1 can begin.

[ ] SUBJECT CARDS COMPLETE: All three subject cards have all six fields populated --
    Role, Evidential Function, Experience-Proximity (with one-sentence justification),
    Prior Knowledge, Blind Spots, and Vocabulary Signature (3 specific auditable terms).
    A card with any empty field fails. Vocabulary fields with trait descriptors instead
    of specific terms ("uses technical language") fail. Confirmed by GATE 0A above.

[ ] EXPECTATION REGISTER POPULATED: The register in Step 0C has content in every cell --
    all three subjects, all five columns. Confirmed by C-13 STATUS CHECK above.
    If any cell is empty, C-13 is PARTIAL -- fix before proceeding. A PARTIAL register
    cannot activate the C-25 bridge; deploying it against a PARTIAL register produces
    a C-30 failure, not a C-25 pass.

[ ] VOCABULARY SIGNATURES DECLARED FOR ALL SUBJECTS: All three subjects have 3 specific
    vocabulary terms each, declared in their Subject Cards. Terms must be specific enough
    to audit against transcript text -- not trait descriptors. Confirmed by GATE 0A above.

[ ] MOMENT-LABEL DECISION TAXONOMY DECLARED: The three-label decision system in Step 0B
    is complete -- SURPRISING, CONFIRMING, and INCONCLUSIVE each have a declared decision
    rule. Confirmed by C-28 STATUS CHECK above. If any label lacks a decision rule,
    fix before proceeding.

Phase 1 begins only when all four boxes are checked.
Proceeding with three of four boxes checked scores C-31 PARTIAL -- the master gate is
incomplete if any of the four required items is omitted.

---

PHASE 1 -- INTERVIEW: THE SKEPTIC

Transcript

Opening question: [A question anchored in the Skeptic's declared prior knowledge and
blind spots -- probing what specifically grounds their resistance.]

[Skeptic]: [Answer in this subject's distinct voice. Vocabulary Signature terms must
appear naturally -- at least one of the three declared terms must surface in this transcript.]

Follow-up (triggered by: "[exact phrase from the preceding answer that prompted this]"):
[follow-up question anchored to the prior answer]

[Skeptic]: [answer]

[Continue 2-3 additional exchanges. The Skeptic's primary objection must be clearly and
explicitly stated by the end of this transcript -- it becomes the objection whose lifecycle
is tracked in Phase 4.]

---

Vocabulary Audit -- Skeptic:

Prerequisite check: C-22 for Skeptic was confirmed FULLY SATISFIED in the PRE-INTERVIEW
MASTER GATE (item 3). Proceeding with audit. (If NOT confirmed: stop, fix master gate first.)

- "[Term 1]": FOUND in A[N] -- "[brief quote]" | NOT FOUND (open contract -- elicit before Phase 2)
- "[Term 2]": FOUND | NOT FOUND
- "[Term 3]": FOUND | NOT FOUND

At least 1 of 3 terms must be FOUND. Closing status: [ ] vocabulary contract closed

---

Moment Label -- Skeptic:

Prerequisite check: C-13 was confirmed FULLY SATISFIED in the PRE-INTERVIEW MASTER GATE
(item 2). Expectation Register is available as source for "expected:" slot. Proceeding.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Expectation Register -> Subject: Skeptic,
  Field: "{field_name}"], ...)

C-25 bridge status: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE -- bridge
active. (If C-13 were PARTIAL, deploying the bridge would score C-30 FAIL, not C-25 PASS.)

Ambiguity check: [Apply Option A or Option B from Step 0B -- name which applies]

---

Evidence Extraction -- Skeptic:

Prerequisite check: C-27 requires two orthogonal dimensions. Both are defined here with
distinct definitions before any row is filled.

  Experience-Proximity: GROUNDED | CONDITIONAL | INFERRED
    Answers: "How close is this subject to direct operational experience of this claim?"
    GROUNDED = firsthand experience; CONDITIONAL = adjacent but not direct;
    INFERRED = reasoning from no direct operational experience.

  Origin-of-Claim: verbatim | inferred | corroborated
    Answers: "How was this claim derived from the transcript?"
    verbatim = stated directly; inferred = implied but not said;
    corroborated = consistent signal across two or more subjects.

  ORTHOGONALITY RULE: Do not use one dimension's tags to fill the other's slot.
  A GROUNDED source can produce inferred evidence (they know it but did not say it directly).
  A CONDITIONAL source can produce verbatim evidence (they stated it, but their blind spot
  limits how much weight it carries). The dimensions answer different questions.

Example row (schema instantiation -- fill this before the real data rows):
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| "Integration with legacy audit trail is non-negotiable -- any workaround adds a sprint." | feasibility concern | GROUNDED -- subject has operated the audit trail process for 3 years | verbatim -- stated directly in A2: "non-negotiable" | strong | GROUNDED source stating it explicitly with operational specificity; no hedging language |

Real data:
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| | | | | | |

---

PHASE 1 GATE
  [ ] At least one vocabulary term FOUND in Skeptic's transcript -- contract closed
  [ ] Moment label references Expectation Register by subject name and field name
  [ ] Experience-Proximity and Origin-of-Claim both populated for every evidence row (not conflated)
  [ ] Skeptic's primary objection explicitly stated and identifiable in transcript

---

PHASE 2 -- INTERVIEW: THE PRACTITIONER

Transcript

Opening question: [Anchored in the Practitioner's declared prior knowledge and the
operational ground truth this subject uniquely carries]

[Practitioner]: [Answer in this subject's distinct voice -- vocabulary distinct from Skeptic's]

Follow-up (triggered by: "[exact phrase from the preceding answer that prompted this]"):
[follow-up anchored to prior answer]

[Practitioner]: [answer]

[Continue 2-3 more exchanges. At least one question must probe whether the Practitioner's
operational reality speaks to -- or is silent about -- the Skeptic's primary objection
from Phase 1.]

---

Vocabulary Audit -- Practitioner:

Prerequisite check: C-22 for Practitioner confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 3). Proceeding.

- "[Term 1]": FOUND in A[N] -- "[quote]" | NOT FOUND
- "[Term 2]": FOUND | NOT FOUND
- "[Term 3]": FOUND | NOT FOUND

Closing status: [ ] vocabulary contract closed

---

Moment Label -- Practitioner:

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE (item 2).
Proceeding.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Expectation Register -> Subject:
  Practitioner, Field: "{field_name}"], ...)

C-25 bridge status: active (C-13 FULLY SATISFIED -- confirmed master gate item 2).

Ambiguity check: [Option A or Option B]

---

Evidence Extraction -- Practitioner:

[Same table format as Phase 1, including example row before real data.
"corroborated" is now available for Origin-of-Claim when a signal matches Phase 1.]

Example row (schema instantiation):
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| [fill with a real example from practitioner context] | | | | | |

Real data:
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| | | | | | |

---

PHASE 2 GATE
  [ ] At least one vocabulary term FOUND in Practitioner's transcript
  [ ] Moment label references Expectation Register by subject and field
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Practitioner's response to (or silence about) Skeptic's primary objection is visible

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

Vocabulary Audit -- Advocate:

Prerequisite check: C-22 for Advocate confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 3). Proceeding.

- "[Term 1]": FOUND | NOT FOUND
- "[Term 2]": FOUND | NOT FOUND
- "[Term 3]": FOUND | NOT FOUND

Closing status: [ ] vocabulary contract closed

---

Moment Label -- Advocate:

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE (item 2).
Proceeding.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Expectation Register -> Subject:
  Advocate, Field: "{field_name}"], ...)

C-25 bridge status: active (C-13 FULLY SATISFIED -- confirmed master gate item 2).

Ambiguity check: [Option A or Option B]

---

Evidence Extraction -- Advocate:

[Same table format. "corroborated" available from Phases 1+2.]

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
  [ ] Advocate's response to (or evasion of) Skeptic's primary objection is visible

---

PHASE 4 -- CROSS-INTERVIEW SYNTHESIS

Prerequisite confirmation: PHASE 1, 2, and 3 GATES are all closed. Proceeding.

Patterns and Contradictions

Name at least one convergence or contradiction across the three subjects. Reference
subjects by name and cite the specific evidence items (by subject and response number)
that produce it -- do not summarize without citation.

Objection Lifecycle

Trace the Skeptic's primary objection from Phase 1 through Phases 2 and 3.
  - Initial objection (Phase 1): [state it as declared in the transcript]
  - Practitioner's response (Phase 2): [addressed? transformed? silent? -- cite the moment]
  - Advocate's response (Phase 3): [persisted? transformed? resolved? -- cite the moment]
  - Final verdict: PERSISTED | TRANSFORMED | RESOLVED
    [one sentence naming the evidence that determines the verdict]

Epistemic Weight Adjustment

Explicitly adjust the weight of at least one evidence item based on Experience-Proximity.
Required format: "Item [evidence text] is CONDITIONAL -- [subject] has not experienced
[specific blind spot from their Subject Card]. Treat as a risk to monitor, not a confirmed
blocker, until a GROUNDED source who has encountered the alternative confirms or refutes it."
If all evidence items are GROUNDED, state that explicitly and explain why no reduction applies.

PHASE 4 GATE
  [ ] Objection lifecycle traced with PERSISTED / TRANSFORMED / RESOLVED verdict and citation
  [ ] At least one named epistemic weight adjustment present
  [ ] Convergence or contradiction cited with specific subject and evidence references

---

PHASE 5 -- META-OBSERVATIONS

PHASE 5A -- Simulation Fidelity Note

Include a brief meta-note identifying at least one specific grounding basis for claims
made in this simulation -- naming a piece of documented persona knowledge, domain context,
or structural role constraint that anchored a specific answer. Also name at least one
place where the simulation exercised constructed plausibility (not derived from documented
prior knowledge but from role logic). The note distinguishes grounded claims from constructed ones.

PHASE 5B -- Voice Divergence Note

Include a meta-observation naming at least one concrete contrast in how two subjects were
made to sound different -- citing a specific vocabulary choice, framing preference, or
concern priority that distinguishes them. Example: "[Subject A] used the term '[Term X]'
while [Subject B] used '[Term Y]' -- signaling different conceptual frames for the same
feature." Generic statements ("they had different roles") without a specific cited voice
difference fail this criterion.
```

---

## V-02 -- Output Format: Schema Contract with Named Gate Blocks

**Axis**: Output format
**Hypothesis**: R8 V-02 introduced the Schema Contract Rule effectively (C-29 PASS) but failed C-30 (no explicit prerequisite confirmations before dependent mechanisms) and scored C-20 PARTIAL (no named gate blocks -- only inline checkboxes). For v9, the schema contract is extended to gate blocks: every phase gate is formatted as a named "SECTION N GATE:" block with enumerated items, and the PRE-INTERVIEW MASTER GATE is itself a schema element. Prerequisite confirmations are added explicitly before each dependent mechanism, recovering C-30. Together these changes should recover C-30 FAIL and C-20 PARTIAL from R8 while adding C-31/C-32 for v9.

```
You are running a simulated stakeholder interview investigation for the feature topic: {{topic}}.

This is a structured simulation -- not a real interview -- grounded in documented persona
knowledge and producing evidence artifacts for downstream topic decisions.

---

SCHEMA CONTRACT RULE (applies throughout this document):

Every table in this document that declares column headers as a structural template must
include at least one fully instantiated example row before any real data appears. A table
with headers but no example row is an open schema contract -- incomplete until closed with
an instance. This rule enforces itself: if you see a table with only headers and real data
rows, an example row is missing.

GATE BLOCK RULE (applies throughout this document):

Every section in this document ends with a named gate block in this format:

  SECTION N GATE
    [ ] item one description
    [ ] item two description

A gate with no named header is not a gate. Items embedded in prose are not gate items.
Consolidated named blocks with enumerated checkboxes are required throughout.

---

SECTION 1 -- SUBJECT CARDS

For each subject, complete the Subject Card table. The schema row is the example;
the real data rows follow it.

Schema declaration + instantiation:

| Field | Skeptic | Practitioner | Advocate |
|-------|---------|--------------|----------|
| Role | [e.g., "Senior Compliance Analyst, 8 years in regulated pipeline environments"] | | |
| Evidential Function | [e.g., "Establishes the compliance objection surface -- subsequent subjects must address it or leave it standing"] | | |
| Experience-Proximity | [e.g., "GROUNDED -- has personally managed audit trail failures in two production incidents"] | | |
| Prior Knowledge | [e.g., "Knows the current manual workaround, has seen two failed migration attempts, understands the compliance clock constraint"] | | |
| Blind Spots | [e.g., "Has not used the new API-driven approach -- all resistance is grounded in the two prior failures, not the current alternative"] | | |
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

Sequence justification (one sentence): State why the chosen interview order is the optimal
ordering for this specific investigation -- name the structural reason, not just the role names.

C-22 STATUS CHECK: [ ] All three subjects have 3 specific vocabulary terms declared in the
real data table. Trait descriptors instead of specific auditable terms fail. If any subject
has fewer than 3 specific terms, stop and fix before proceeding.

SECTION 1 GATE
  [ ] All three subject cards have all eight rows populated in the real data table
  [ ] Sequence justification sentence is present
  [ ] C-22 STATUS CHECK passed -- all vocabulary signatures are specific and auditable

---

SECTION 2 -- EXPECTATION REGISTER

Declare prior expectations before any transcript begins. This table is the mandatory
source for all moment labels in Sections 4-6.

Schema declaration + instantiation (example row):

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [e.g., "Skeptic -- Compliance Analyst"] | [e.g., "Will require audit immutability guarantee before any positive signal"] | [e.g., "Will object that no API-driven approach has survived a compliance audit in this org"] | [e.g., "If a compliance guarantee exists, will confirm the workflow-reduction benefit is real"] | [e.g., "May acknowledge the current workaround creates compliance risk too -- turning the objection against the status quo"] |
| Practitioner | | | | |
| Advocate | | | | |

Real data:

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [Skeptic] | | | | |
| [Practitioner] | | | | |
| [Advocate] | | | | |

C-13 STATUS CHECK: [ ] Register fully populated -- all cells have content for all three
subjects and all five columns. Empty cells mean C-13 is PARTIAL. A PARTIAL C-13 cannot
activate the C-25 bridge (deploying against PARTIAL scores C-30 FAIL, not C-25 PASS).

SECTION 2 GATE
  [ ] All cells in the real data table are populated
  [ ] C-13 STATUS CHECK passed

---

SECTION 3 -- MOMENT-LABEL DECISION SYSTEM

This section declares the complete labeling system governing all moment labels in Sections 4-6.
This is a rule-governed decision system, not a format guide. Each label has a decision rule.

Schema declaration + instantiation:

| Label | Decision Rule | When to Apply | What "Not Applicable" Looks Like | Required Format |
|-------|--------------|---------------|----------------------------------|-----------------|
| [e.g., SURPRISING] | [e.g., "Prior expectation from the Register was violated -- subject responded in a meaningfully different direction, intensity, or framing"] | [e.g., "Register entry exists and the response departs from it"] | [e.g., "Response differs from a vague general assumption with no register entry -- fix the register first, then apply"] | [e.g., "SURPRISING (expected: [Register -> Skeptic, Field: 'Expected Objection': '...'], got: [...])"] |
| CONFIRMING | Prior expectation from the Register was upheld -- subject said what was expected, validating a prior signal. Must trace to a named register field. | Register entry exists and the response matches it | Response is consistent with an undeclared general assumption rather than a specifically declared expectation | CONFIRMING (validates: [Register -> Practitioner, Field: "Expected Confirmation": "..."]) |
| INCONCLUSIVE | Notable signal present but direction is genuinely ambiguous -- cannot be assigned to SURPRISING or CONFIRMING without additional evidence | Signal present; direction cannot be resolved by any register field | One of the above labels clearly fits -- do not use INCONCLUSIVE as a hedge | INCONCLUSIVE (closest register field: [Register -> Advocate, Field: "Expected Surprise"], ambiguity: [...]) |

Every labeled-moment section must end with one of:
  Option A: "All moments in this section are unambiguously SURPRISING or CONFIRMING --
             no INCONCLUSIVE moments observed."
  Option B: [Apply INCONCLUSIVE label to the ambiguous moment using the format above]

C-28 STATUS CHECK: [ ] Decision system complete -- all three labels have declared decision
rules and "What Not Applicable Looks Like" for each. INCONCLUSIVE is fully specified.

SECTION 3 GATE
  [ ] All three labels have decision rules, When-to-Apply, negative condition, and Required Format
  [ ] C-28 STATUS CHECK passed

---

PRE-INTERVIEW MASTER GATE

Before the first interview transcript begins, this gate confirms that all structural
prerequisites are collectively and fully satisfied. All four items must be checked.

PRE-INTERVIEW MASTER GATE
  [ ] SUBJECT CARDS COMPLETE: Section 1 GATE passed -- all three subject cards fully
      populated, sequence justification present, vocabulary signatures specific and
      auditable (C-22 STATUS CHECK confirmed).
  [ ] EXPECTATION REGISTER POPULATED: Section 2 GATE passed -- all register cells filled,
      C-13 STATUS CHECK confirmed. A PARTIAL register cannot activate the C-25 bridge.
  [ ] VOCABULARY SIGNATURES DECLARED FOR ALL SUBJECTS: C-22 STATUS CHECK passed in
      Section 1 -- all three subjects have 3 specific vocabulary terms declared.
  [ ] MOMENT-LABEL DECISION TAXONOMY DECLARED: Section 3 GATE passed -- C-28 STATUS
      CHECK confirmed, all three labels have declared decision rules including INCONCLUSIVE.

Section 4 begins only when all four items are checked.
Proceeding with a PARTIAL item checked scores C-31 PARTIAL -- do not advance.

---

SECTION 4 -- INTERVIEW: THE SKEPTIC

Transcript

Opening question: [Anchored in the Skeptic's declared prior knowledge and register --
probe what specifically grounds their resistance]

[Skeptic]: [Answer in distinct Skeptic voice. Declared vocab terms must appear naturally.]

Follow-up (triggered by: "[exact phrase from preceding answer]"):
[follow-up anchored to prior answer]

[Skeptic]: [answer]

[2-3 more exchanges. Skeptic's primary objection must be explicitly stated -- it becomes
the objection whose lifecycle is tracked in Section 7.]

---

Vocabulary Audit -- Skeptic

Prerequisite check: C-22 for Skeptic confirmed FULLY SATISFIED -- Section 1 GATE passed
and PRE-INTERVIEW MASTER GATE item 3 checked. Proceeding with audit.

Schema declaration + instantiation:

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

Prerequisite check: C-13 confirmed FULLY SATISFIED -- Section 2 GATE passed and
PRE-INTERVIEW MASTER GATE item 2 checked. Register is source for "expected:" slot.
C-25 bridge is authorized to deploy. (If Register were PARTIAL, deploying the bridge
scores C-30 FAIL -- the confirmed COMPLETE status in the master gate authorizes it.)

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Register -> Subject: Skeptic,
  Field: "{field_name}"], ...)

Ambiguity check: [Option A or Option B from Section 3 decision system]

---

Evidence Extraction -- Skeptic

Prerequisite check: C-18/C-27 taxonomy prerequisites confirmed -- Section 3 GATE passed,
C-28 STATUS CHECK confirmed, both dimensions defined and distinct. Proceeding.

Schema declaration + instantiation:

| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Strength Rationale |
|---------------|-------------|---------------------|-----------------|----------|--------------------|
| [e.g., "Integration with legacy audit trail is non-negotiable -- any workaround adds a sprint."] | [e.g., feasibility concern] | [e.g., GROUNDED -- subject has operated the audit trail process for 3 years] | [e.g., verbatim -- stated directly in A2: "non-negotiable"] | [e.g., strong] | [e.g., GROUNDED source stating it explicitly with operational specificity; no hedging language] |

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

Transcript

[Same structure as Section 4. At least one vocab term must appear naturally. Questions probe
operational ground truth. At least one question must probe whether the Practitioner's
operational reality speaks to -- or is silent about -- the Skeptic's primary objection.]

---

Vocabulary Audit -- Practitioner

Prerequisite check: C-22 for Practitioner confirmed FULLY SATISFIED -- PRE-INTERVIEW MASTER
GATE item 3 checked. Proceeding.

Schema + instantiation + real data: [same format as Section 4 Vocabulary Audit]

---

Moment Label -- Practitioner

Prerequisite check: C-13 confirmed FULLY SATISFIED -- PRE-INTERVIEW MASTER GATE item 2
checked. C-25 bridge authorized.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Register -> Subject: Practitioner,
  Field: "{field_name}"], ...)

Ambiguity check: [Option A or Option B]

---

Evidence Extraction -- Practitioner

Prerequisite check: C-18/C-27 taxonomy confirmed -- PRE-INTERVIEW MASTER GATE item 4 checked.
"corroborated" now available for Origin-of-Claim when a signal is consistent with Section 4 evidence.

Schema + instantiation + real data: [same format as Section 4 Evidence Extraction]

SECTION 5 GATE
  [ ] Vocabulary contract closed -- at least 1 declared term FOUND in Practitioner's transcript
  [ ] Moment label references Register by subject name and field name
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Practitioner's response to (or silence about) Skeptic's primary objection is visible

---

SECTION 6 -- INTERVIEW: THE ADVOCATE

Transcript

[Same structure. At least one vocab term must appear naturally. Opening question anchored
in the Advocate's declared evidential function. At least one question probes the Advocate's
awareness of and response to the Skeptic's primary objection.]

---

Vocabulary Audit -- Advocate

Prerequisite check: C-22 for Advocate confirmed FULLY SATISFIED -- PRE-INTERVIEW MASTER
GATE item 3 checked. Proceeding.

Schema + instantiation + real data: [same format]

---

Moment Label -- Advocate

Prerequisite check: C-13 confirmed FULLY SATISFIED -- PRE-INTERVIEW MASTER GATE item 2.
C-25 bridge authorized.

Ambiguity check: [Option A or Option B]

---

Evidence Extraction -- Advocate

Prerequisite check: C-18/C-27 taxonomy confirmed -- PRE-INTERVIEW MASTER GATE item 4.
"corroborated" available from Sections 4+5.

Schema + instantiation + real data: [same format]

SECTION 6 GATE
  [ ] Vocabulary contract closed -- at least 1 declared term FOUND in Advocate's transcript
  [ ] Moment label references Register by subject name and field name
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Advocate's response to Skeptic's primary objection is visible

---

SECTION 7 -- SYNTHESIS

Prerequisite confirmation: Sections 4, 5, and 6 GATES are all closed. Proceeding.

Patterns and Contradictions: Name 2-3 patterns or contradictions across all three subjects.
Cite specific evidence items by subject and response number -- no uncited conclusions.

Objection Lifecycle: Trace the Skeptic's primary objection.
  - Initial (Section 4): [state it]
  - Practitioner's response (Section 5): [addressed? transformed? silent? -- cite]
  - Advocate's response (Section 6): [persisted? transformed? resolved? -- cite]
  - Final verdict: PERSISTED | TRANSFORMED | RESOLVED
    [one sentence naming the evidence that determines the verdict]

Epistemic Weight Adjustment: For at least one evidence item, name when an objection or
validation comes from a GROUNDED source versus CONDITIONAL/INFERRED, and adjust synthesis
weight accordingly. Required format: "Item [citation] is CONDITIONAL -- [subject] has not
experienced [specific gap]. Treat as a risk to monitor, not a blocker."

SECTION 7 GATE
  [ ] Objection lifecycle traced with verdict and citation
  [ ] At least one named epistemic weight adjustment present
  [ ] Patterns or contradictions cited with specific evidence references

---

SECTION 8 -- META-OBSERVATIONS

8A -- Simulation Fidelity: Name at least one specific grounding basis (documented persona
knowledge that anchored a specific answer) and at least one place where constructed
plausibility was exercised. Distinguish the two.

8B -- Voice Divergence: Name one concrete contrast between two subjects -- cite a specific
vocabulary choice, framing preference, or concern priority. Generic role-level statements
without specific cited differences fail.
```

---

## V-03 -- Phrasing Register: Conversational with Named Accountability Blocks

**Axis**: Phrasing register
**Hypothesis**: R8 V-03's conversational framing lost C-19 PARTIAL (sequence justification guidance without required output statement), C-20 PARTIAL (no named gate blocks -- only "do three things after each interview"), C-22 PARTIAL (vocabulary field guidance without dedicated structure), and C-30 FAIL (no explicit prerequisite confirmation before dependent mechanisms). For v9, the test is whether C-31 and C-32 can be achieved in a conversational register by adding a named "BEFORE-INTERVIEW CHECKLIST" with explicit enumerated items and named "INTERVIEW N COMPLETE" accountability blocks. The hypothesis is that conversational phrasing and structural enforcement are not mutually exclusive -- the key is whether the named blocks are present and enumerate discrete items, regardless of whether the language surrounding them is formal or friendly.

```
You are running a simulated stakeholder interview investigation for the feature topic: {{topic}}.

This is a simulation -- the interviews are not real, but the voices, knowledge, and
concerns you give each subject should be grounded in their documented role and experience.
Your job is to produce evidence, not theatre: every answer should carry information that
could genuinely change how you think about the feature.

Take this in order. The structure is here to help you produce stronger evidence, not to
bureaucratize the work. Each phase has a purpose; don't skip ahead.

---

PART 1 -- SET UP YOUR SUBJECTS

Before you write a single interview line, you need three things per subject: who they are,
what they already know (and don't know), and what you expect them to say.

For each subject, write a Subject Card. Here is what belongs in each card:

  - Their role -- job title or function, specific enough to anchor their vocabulary
  - Their evidential function -- not just their disposition, but what their structural
    position in the investigation does for the evidence. Are they the baseline skeptic
    whose objection defines the problem? The operational ground-truth carrier? The
    adoption advocate whose optimism either gets confirmed or tempered?
  - Their experience-proximity -- how close are they to direct operational experience
    of what you're investigating?
      GROUNDED: they've done it firsthand
      CONDITIONAL: adjacent experience, not direct -- they've seen it but not run it
      INFERRED: they're reasoning about something they haven't encountered
    Write one sentence explaining why this label fits.
  - Their prior knowledge -- what they know, what they've worked with, what they care
    about. Two to three sentences.
  - Their blind spots -- what they have NOT encountered. Keep this as a separate field
    from prior knowledge. Knowing what a subject doesn't know is as important as knowing
    what they do.
  - Their vocabulary signature -- give each subject 2-3 specific terms they would
    naturally use in their role. Not general traits like "uses technical language" --
    actual terms like "compliance window" or "rollback surface." You will check whether
    these terms appear in their answers, so they need to be specific enough to look for
    by name.

Once you have your three Subject Cards, write one sentence explaining why you are
interviewing them in this specific order. The sequence should serve the investigation --
starting with the hardest objection usually produces stronger evidence than starting with
the most agreeable voice -- but name the reason for your specific ordering, not just the
role names.

Now populate the Expectation Register before any interview begins:

What do you expect each subject to say? Fill in all five columns for all three subjects
before you write any dialogue. The Expected Surprise column is especially important --
if you cannot imagine what would surprise you from this subject, you may not have formed
a real model of their position yet.

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [Skeptic name] | | | | |
| [Practitioner name] | | | | |
| [Advocate name] | | | | |

---

BEFORE THE FIRST INTERVIEW -- CONFIRM THESE FOUR THINGS

Before you write any dialogue, work through this checklist. Each item is a hard stop.

BEFORE-INTERVIEW CHECKLIST
  [ ] SUBJECT CARDS COMPLETE: All three Subject Cards have all six fields -- Role,
      Evidential Function, Experience-Proximity (with justification), Prior Knowledge,
      Blind Spots, and Vocabulary Signature (at least 2-3 specific auditable terms per
      subject, not traits). A card with a missing field or with vocabulary traits instead
      of specific terms is incomplete. Fix it before moving on.
  [ ] EXPECTATION REGISTER POPULATED: All five columns are filled for all three subjects
      in the register table above. Empty cells mean the register is not ready. The moment-
      labeling in Part 2 depends on it being fully populated -- a partially filled register
      cannot serve as the structural source for the "expected:" slot in your moment labels.
      Deploying that mechanism against a partial register does not earn you credit for the
      bridge; it earns a structural failure instead.
  [ ] VOCABULARY SIGNATURES DECLARED FOR ALL SUBJECTS: You have at least 2-3 specific
      auditable vocabulary terms per subject in their Subject Cards. Not traits. Specific
      terms you can look for by name in the transcript.
  [ ] MOMENT-LABEL DECISION RULES DECLARED: The labeling system in Part 2 has decision
      rules for all three labels -- SURPRISING, CONFIRMING, and INCONCLUSIVE. If any label
      is missing a rule, the labeling is authorial, not governed. Fix it before continuing.

---

PART 2 -- YOUR LABELING SYSTEM

Before the interviews begin, establish a complete rule system for labeling notable moments.
This system governs everything in Part 3.

SURPRISING: The subject said something that violates a prior expectation you registered
  in the Expectation Register. The violation has to be directional -- not just different,
  but meaningfully departing from what you expected in position, intensity, or framing.
  If there's no register entry to serve as the "expected:" reference, don't apply
  SURPRISING -- fix the register first.
  Format: SURPRISING (expected: [Register -> Subject: {name}, Field: "{field}"],
    got: [what actually emerged])

CONFIRMING: The subject said what you expected, validating a prior signal. The
  validation needs to trace to a named register field -- not a vague general assumption.
  Format: CONFIRMING (validates: [Register -> Subject: {name}, Field: "{field}"])

INCONCLUSIVE: Something notable happened but you genuinely cannot tell which direction
  it points. Do not force it into SURPRISING or CONFIRMING -- use this label when the
  direction is ambiguous and additional evidence is needed to resolve it.
  Format: INCONCLUSIVE (closest register field: [Register -> Subject: {name},
    Field: "{field}"], ambiguity: [why the direction cannot be resolved])

At the end of each interview's labeled-moment section, you must explicitly do one of:
  A. State: "All labeled moments in this interview are unambiguously SURPRISING or
     CONFIRMING -- no INCONCLUSIVE moments were present."
  B. Apply the INCONCLUSIVE label to the ambiguous moment.
Silence on this choice fails C-14 -- the decision must be visible.

---

PART 3 -- THE INTERVIEWS

Run the interviews in the order you justified in Part 1. For each interview:

1. Write the transcript. Opening question anchored in the subject's declared prior
   knowledge and blind spots. Follow-up questions triggered by specific things the
   subject just said -- use the format:
     Follow-up (triggered by: "you mentioned X" or "[exact phrase] -- can you say more?")
   Let their declared vocabulary terms surface naturally in their answers.

2. Vocabulary check. Go through the vocabulary terms you declared for this subject and
   check whether each one appeared. Before running this check, confirm that the vocabulary
   signature for this subject was declared as fully complete in the BEFORE-INTERVIEW
   CHECKLIST -- specific, auditable terms, not traits.

   Vocabulary Audit -- [Subject Name]:
   - "[Term 1]": FOUND in A[N] -- "[brief quote]" | NOT FOUND -- open contract
   - "[Term 2]": FOUND | NOT FOUND
   - "[Term 3]": FOUND | NOT FOUND
   Closing status: [ ] at least one term FOUND -- vocabulary contract closed

3. Moment label. Apply the most notable moment using the decision system from Part 2.
   Reference the register by subject name and field name. Before applying moment labels,
   confirm that the Expectation Register was fully populated in the BEFORE-INTERVIEW
   CHECKLIST -- if any register cell was empty when you started Part 3, the "expected:"
   slot has no structural source. Deploying the label format anyway does not earn credit
   for the bridge mechanism.

   [SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Register -> Subject: {name},
     Field: "{field}"], ...)
   Ambiguity check: [Apply Option A or Option B from Part 2 -- name which applies]

4. Extract the evidence. For each notable claim, record:
   - What they said (or implied)
   - What type of signal it is (adoption risk, feasibility concern, requirement gap, etc.)
   - Their experience-proximity to the claim (GROUNDED / CONDITIONAL / INFERRED -- same
     labels as in their Subject Card)
   - How the claim was derived from the transcript (Origin-of-Claim: verbatim = stated
     directly; inferred = implied but not said; corroborated = consistent across subjects)
   - How strong the evidence is (strong / moderate / weak) and why

   These two dimensions are orthogonal -- experience-proximity answers "how close is this
   person to the experience?"; origin-of-claim answers "how did this come out of the
   transcript?" A GROUNDED person can produce inferred evidence. A CONDITIONAL person can
   produce verbatim evidence. Do not conflate them.

   Example evidence row:
   | Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
   |---------------|-------------|---------------------|-----------------|----------|-----------|
   | "The approval queue backs up to 48 hours every sprint end -- this would eliminate that." | adoption signal | CONDITIONAL -- observed but not owned the approval process | verbatim -- stated in A3: "48-hour delay" | moderate | Conditional proximity limits weight; verbatim basis is direct; moderate for not being the queue owner |

   Your evidence table:
   | Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
   |---------------|-------------|---------------------|-----------------|----------|-----------|
   | | | | | | |

5. Check off before moving to the next interview:

   INTERVIEW [N] COMPLETE -- BEFORE MOVING ON
     [ ] Vocabulary contract closed -- at least one declared term FOUND in transcript
     [ ] Moment label references Register by subject name and field name
     [ ] Both taxonomy dimensions (Experience-Proximity and Origin-of-Claim) populated
         for every evidence row and not conflated
     [ ] [Interview 1 only:] Skeptic's primary objection explicitly stated in transcript
     [ ] [Interview 2 only:] Practitioner's position on Skeptic's objection is visible
     [ ] [Interview 3 only:] Advocate's response to Skeptic's objection is visible

Run all three interviews using this structure before moving to Part 4.

---

PART 4 -- SYNTHESIS

Once all three INTERVIEW COMPLETE checklists are closed, pull the threads together.

Patterns and contradictions: What appears across multiple subjects? What do subjects agree
on or contradict each other about? Cite specific evidence items (by subject and response
number) -- do not summarize without reference.

The objection's fate: The Skeptic raised a primary objection in Interview 1. What happened
to it? Trace the objection's movement and name a verdict:
  PERSISTED -- still standing after all three interviews, no subject resolving it
  TRANSFORMED -- changed form, narrowed scope, or reframed by Interviews 2 or 3
  RESOLVED -- explicitly addressed and closed by Interview 2 or 3 testimony
Cite the moments that support your verdict.

Epistemic weighting: At least one evidence item should have its synthesis weight adjusted
based on experience-proximity. When an objection comes from someone who has never
encountered the alternative (CONDITIONAL or INFERRED), it is a risk to monitor, not a
confirmed blocker. Name it explicitly: "This claim is CONDITIONAL -- [subject] has not
experienced [specific gap from their blind spots]. Treat as a risk to monitor until a
GROUNDED source confirms or refutes it."

SYNTHESIS COMPLETE -- BEFORE PART 5
  [ ] Objection lifecycle traced with PERSISTED / TRANSFORMED / RESOLVED verdict and citation
  [ ] At least one named epistemic weight adjustment with CONDITIONAL/GROUNDED framing
  [ ] Patterns or contradictions cited with specific evidence references

---

PART 5 -- CLOSING OBSERVATIONS

5A -- Where is the simulation grounded and where is it constructed? Name at least one
specific piece of documented persona knowledge or domain context that anchored an answer,
and at least one place where you exercised constructed plausibility (role logic rather than
documented knowledge). Distinguish the two explicitly.

5B -- How are the voices actually different? Name one concrete contrast between two subjects:
a specific vocabulary choice, a framing preference, a concern priority -- something a reader
could use to tell Subject A's answer apart from Subject B's. "They had different roles" is
not a voice observation. Name a specific term, phrase, or framing that belongs to one
subject and not the other.
```

---

## V-04 -- Role Sequence + Inertia Framing: Master Gate with Inertia Grounding

**Axis**: Role sequence + inertia framing (combination)
**Hypothesis**: R8 V-04 scored 100/100 against v8. Its distinctive contribution was the Inertia Profile -- profiling the current-state workflow as a named structural artifact before any subject testimony begins, giving SURPRISING/CONFIRMING/INCONCLUSIVE labels a shared referent independent of any individual subject's prior knowledge. For v9, the PRE-INTERVIEW MASTER GATE must name all four required prerequisites. R8 V-04's Step 0D had C-22/C-13/C-28 but not "Subject Cards complete" explicitly. The fix: add Subject Cards complete as item 1. The Inertia Profile is confirmed as a structural prerequisite through the Subject Card completeness check (the Inertia Stance field grounds each subject's relationship to the current-state workflow). Phase gates were already named PHASE N GATE blocks in R8 V-04; C-32 carries forward.

```
You are running a simulated stakeholder interview investigation for the feature topic: {{topic}}.

This is not a real interview. It is a structured simulation grounded in documented persona
knowledge, producing evidence artifacts for downstream topic narrative decisions.

Complete all phases in order. Do not write any transcript line before the Inertia Profile
and Phase 0 setup are fully closed.

---

INERTIA PROFILE -- THE STATUS-QUO BASELINE

Before any subject speaks, profile the current-state workflow that the feature under
investigation would replace, augment, or challenge. This is the baseline against which
every label, objection, and evidence item is measured. Without a named baseline, SURPRISING
and CONFIRMING labels are measured only against each subject's individual priors -- weakening
label comparability across interviews.

Current-state workflow name: [Name the workflow as it is known in the org or domain]

Schema declaration + instantiation:

| Dimension | Current-State Description |
|-----------|--------------------------|
| [e.g., Workflow steps] | [e.g., "Manual approval queue -> spreadsheet audit log -> weekly compliance export -> legal sign-off every sprint"] |
| Cost / Friction | [e.g., "48-hour approval delay at sprint end; 3 FTE hours per export; two failed migration attempts in two years"] |
| Risk surface | [e.g., "Audit trail lives in a spreadsheet owned by one analyst; no backup; compliance clock starts on export date, not event date"] |
| Why it persists | [e.g., "Familiar; legal has approved it before; alternatives have failed; changing it requires re-certification"] |

Real data:

| Dimension | Current-State Description |
|-----------|--------------------------|
| Workflow steps | |
| Cost / Friction | |
| Risk surface | |
| Why it persists | |

INERTIA PROFILE GATE
  [ ] All four dimension rows in the real data table are populated
  [ ] "Why it persists" is named -- this is the inertia anchor for skeptic objections

The Inertia Profile is the shared baseline. Every SURPRISING label should note whether
the subject's response shifts their relationship to the Inertia Profile's cost or risk
rows. A skeptic defending the current-state is defending a specific row -- name it.

---

PHASE 0 -- PRE-INTERVIEW STRUCTURE

Do not begin Phase 1 until the PRE-INTERVIEW MASTER GATE at the end of Phase 0 is
explicitly satisfied.

---

STEP 0A -- Subject Roster and Sequence Justification

Select three subjects. Sequence them: SKEPTIC -> PRACTITIONER -> ADVOCATE.
The Skeptic runs first because their objection is anchored in defending the Inertia Profile.

For each subject, complete the Subject Card template:

## Subject Card: [Role/Name]
- Role: [job title or function]
- Evidential Function: [what this subject's structural position does for the evidence
  chain. Example: "establishes the inertia objection surface; determines whether the
  Inertia Profile's risk row is disputed or confirmed by someone with direct operational
  experience"]
- Experience-Proximity: GROUNDED | CONDITIONAL | INFERRED
  Justification: [one sentence -- note their proximity to the Inertia Profile's
  workflow specifically, not just general domain experience]
- Prior Knowledge: [2-3 sentences: what they know, have worked with, care about]
- Blind Spots: [1-2 sentences: what they have NOT encountered -- kept as a separate field]
- Inertia Stance: DEFENDER | NEUTRAL | CHALLENGER
  [One sentence explaining their relationship to the current-state workflow]
- Vocabulary Signature (auditable contract -- declared before transcript):
  - Term 1: [a specific term this persona uses, auditable against transcript]
  - Term 2: [a second specific term]
  - Term 3: [a third specific term]

Sequence justification (one sentence): State why Skeptic-first, Practitioner-second,
Advocate-third is the optimal ordering for this investigation -- specifically how the
Inertia Profile grounds the sequence logic.

GATE 0A
  [ ] Subject 1 (Skeptic): all seven fields populated (Role, Evidential Function,
      Experience-Proximity + justification, Prior Knowledge, Blind Spots, Inertia Stance,
      three vocabulary terms)
  [ ] Subject 2 (Practitioner): all seven fields populated
  [ ] Subject 3 (Advocate): all seven fields populated
  [ ] Sequence justification sentence present and references the Inertia Profile

---

STEP 0B -- Expectation Register

Declare prior expectations for each subject before any transcript begins. The "Expected
Position" column should reference the Inertia Profile explicitly -- how does each
subject's position relate to the current-state workflow's costs, risks, and persistence?

| Subject | Expected Position (re: Inertia Profile) | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|----------------------------------------|--------------------|----------------------|-------------------|
| [Skeptic name] | | | | |
| [Practitioner name] | | | | |
| [Advocate name] | | | | |

The Expected Surprise column includes an inertia sub-question: could the Skeptic's
objection be undermined by the Inertia Profile itself -- could they acknowledge that the
current-state's costs create the risk they claim to be protecting against?

C-13 STATUS CHECK:
  [ ] Register fully populated -- all cells have content for all three subjects and
      all five columns. If any cell is empty, C-13 is PARTIAL -- fix before proceeding.
      A PARTIAL C-13 cannot activate the C-25 bridge.

GATE 0B
  [ ] All register cells populated
  [ ] C-13 STATUS CHECK passed
  [ ] Expected Position column references the Inertia Profile for each subject

---

STEP 0C -- Moment-Label Decision System

IMPORTANT: This step declares a complete decision system governing all moment labels.

## Moment-Label Decision System

LABEL: SURPRISING
  Decision rule: Apply when a subject's response violates an expectation pre-registered
  in the Expectation Register. The violation must be directional.
  Inertia note: The most valuable surprises occur when a Defender of the current-state
  acknowledges one of the Inertia Profile's own cost or risk rows as a problem -- turning
  the baseline against the defending position.
  Required format: SURPRISING (expected: [Register -> Subject: {name}, Field: "{field}"],
    got: [what emerged], inertia relevance: [does this shift the Inertia Profile's weight?])

LABEL: CONFIRMING
  Decision rule: Apply when a response upholds a pre-registered expectation, validating a
  prior signal traceable to a named register field.
  Inertia note: A Confirming moment for an Advocate that confirms Inertia Profile cost rows
  as motivation carries more weight than one confirming an abstract benefit claim.
  Required format: CONFIRMING (validates: [Register -> Subject: {name}, Field: "{field}"])

LABEL: INCONCLUSIVE
  Decision rule: Apply when a notable signal is present but direction is genuinely
  ambiguous -- cannot be assigned to SURPRISING or CONFIRMING without additional evidence.
  Inertia note: When a subject's stance on the Inertia Profile is unclear, INCONCLUSIVE
  may be appropriate even if the register entry is present.
  Required format: INCONCLUSIVE (closest register field: [Register -> Subject: {name},
    Field: "{field}"], ambiguity: [why the direction cannot be resolved])

Every labeled-moment section must end with Option A or Option B:
  Option A: "All moments are unambiguously SURPRISING or CONFIRMING -- no INCONCLUSIVE
             moments observed."
  Option B: [Apply INCONCLUSIVE label using the format above]

C-28 STATUS CHECK:
  [ ] All three labels declared with decision rules (including inertia notes).
      INCONCLUSIVE rule present.

GATE 0C
  [ ] Decision system complete -- all three labels declared with decision rules
  [ ] C-28 STATUS CHECK passed

---

PRE-INTERVIEW MASTER GATE

Before the first interview transcript begins, this gate confirms that all structural
prerequisites for the interview phase are collectively and fully satisfied.
All four items must be checked before Phase 1 can begin.

PRE-INTERVIEW MASTER GATE
  [ ] SUBJECT CARDS COMPLETE: GATE 0A passed -- all three Subject Cards have all seven
      fields populated (Role, Evidential Function, Experience-Proximity + justification,
      Prior Knowledge, Blind Spots, Inertia Stance, three specific vocabulary terms).
      A card with any empty field is incomplete. Fix before proceeding.
  [ ] EXPECTATION REGISTER POPULATED: GATE 0B passed -- all register cells filled,
      C-13 STATUS CHECK confirmed, Expected Position column references Inertia Profile
      for each subject. A PARTIAL register cannot activate the C-25 bridge.
  [ ] VOCABULARY SIGNATURES DECLARED FOR ALL SUBJECTS: GATE 0A confirmed three specific
      vocabulary terms per subject. Terms must be auditable against transcript text.
  [ ] MOMENT-LABEL DECISION TAXONOMY DECLARED: GATE 0C passed -- C-28 STATUS CHECK
      confirmed, all three labels have declared decision rules including INCONCLUSIVE.

Phase 1 begins only when all four items are checked.
Note: The Inertia Profile is confirmed complete by the INERTIA PROFILE GATE above. It
feeds the "Expected Position" column (GATE 0B item 3) and the Inertia Stance field in each
Subject Card (GATE 0A) -- so its completeness is confirmed indirectly through items 1 and 2.

---

PHASE 1 -- INTERVIEW: THE SKEPTIC (INERTIA DEFENDER)

The Skeptic's objection is anchored in defending the Inertia Profile. Their opening question
should probe the specific workflow step or risk row they are most invested in preserving.

Transcript

Opening question: [Anchored in the Skeptic's Prior Knowledge and the Inertia Profile's
risk surface -- what workflow cost or risk are they defending?]

[Skeptic]: [Answer in distinct Skeptic voice. Vocabulary Signature terms must appear
naturally. The answer should touch a specific Inertia Profile row.]

Follow-up (triggered by: "[exact phrase from the preceding answer]"):
[follow-up anchored to prior answer]

[Skeptic]: [answer]

[2-3 more exchanges. The Skeptic's primary objection must be explicitly stated and
traceable to a specific Inertia Profile row.]

---

Vocabulary Audit -- Skeptic:

Prerequisite check: C-22 for Skeptic confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER
GATE (item 3). Proceeding.

- "[Term 1]": FOUND in A[N] -- "[brief quote]" | NOT FOUND (open contract)
- "[Term 2]": FOUND | NOT FOUND
- "[Term 3]": FOUND | NOT FOUND

Closing status: [ ] vocabulary contract closed

---

Moment Label -- Skeptic:

Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE (item 2).
Register is source for "expected:" slot. C-25 bridge authorized.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Register -> Subject: Skeptic,
  Field: "{field}"], got: [...], inertia relevance: [shift in Inertia Profile weight?])

Ambiguity check: [Option A or Option B from Step 0C]

---

Evidence Extraction -- Skeptic:

  Experience-Proximity: GROUNDED | CONDITIONAL | INFERRED
    Note: Proximity is to the Inertia Profile's workflow specifically.
  Origin-of-Claim: verbatim | inferred | corroborated
  ORTHOGONALITY RULE: These dimensions are orthogonal. Do not conflate them.

Example row (schema instantiation):
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| "The compliance window resets if the export is late -- we've had three resets this year." | feasibility concern | GROUNDED -- subject owns the compliance export process | verbatim -- stated in A3: "three resets this year" | strong | GROUNDED operational owner; specific count; directly traceable to Inertia Profile's "risk surface" row |

Real data:
| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Rationale |
|---------------|-------------|---------------------|-----------------|----------|-----------|
| | | | | | |

PHASE 1 GATE
  [ ] At least one vocabulary term FOUND in Skeptic's transcript
  [ ] Moment label references Register by subject name and field name
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Skeptic's primary objection explicitly stated and traceable to an Inertia Profile row

---

PHASE 2 -- INTERVIEW: THE PRACTITIONER (GROUND-TRUTH CARRIER)

The Practitioner carries operational ground truth. Their value is in confirming or
complicating the Inertia Profile's cost and workflow rows from direct experience --
without the Skeptic's defensive investment or the Advocate's adoption interest.

[Same transcript structure as Phase 1. At least one declared vocabulary term must appear.
At least one question must ask how the Practitioner's operational reality compares to the
Inertia Profile row(s) touched by the Skeptic's primary objection.]

Vocabulary Audit -- Practitioner:
Prerequisite check: C-22 for Practitioner confirmed FULLY SATISFIED in PRE-INTERVIEW
MASTER GATE (item 3). Proceeding.
[same audit format]

Moment Label -- Practitioner:
Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE (item 2).
C-25 bridge authorized.
[label format with inertia relevance note + ambiguity check]

Evidence Extraction -- Practitioner:
[Same table format with example row. "corroborated" now available for Origin-of-Claim.]

PHASE 2 GATE
  [ ] At least one vocabulary term FOUND in Practitioner's transcript
  [ ] Moment label references Register by subject and field
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Practitioner's testimony speaks to or is silent about the Inertia Profile row(s)
      touched by the Skeptic's objection

---

PHASE 3 -- INTERVIEW: THE ADVOCATE (INERTIA CHALLENGER)

The Advocate challenges the Inertia Profile -- they see its costs as motivation, not
justification for caution. Their opening question should probe whether they understand
the specific Inertia Profile row the Skeptic is defending.

[Same transcript structure. At least one vocab term must appear naturally.
At least one question probes the Advocate's awareness of and response to the Skeptic's
primary objection, specifically the Inertia Profile row it defends.]

Vocabulary Audit -- Advocate:
Prerequisite check: C-22 for Advocate confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER
GATE (item 3). Proceeding.
[same audit format]

Moment Label -- Advocate:
Prerequisite check: C-13 confirmed FULLY SATISFIED in PRE-INTERVIEW MASTER GATE (item 2).
C-25 bridge authorized.
[label format with inertia relevance note + ambiguity check]

Evidence Extraction -- Advocate:
[Same table format. "corroborated" available from Phases 1+2.]

PHASE 3 GATE
  [ ] At least one vocabulary term FOUND in Advocate's transcript
  [ ] Moment label references Register by subject and field
  [ ] Both taxonomy dimensions populated for every evidence row (not conflated)
  [ ] Advocate's response to Skeptic's Inertia-grounded objection is visible

---

PHASE 4 -- CROSS-INTERVIEW SYNTHESIS

Prerequisite confirmation: PHASE 1, 2, and 3 GATES all closed. Proceeding.

Patterns and Contradictions: Name 2-3 patterns or contradictions. For each, trace it to the
Inertia Profile where possible -- is it about a cost the current-state creates, a risk it
carries, or a reason it persists?

Objection Lifecycle (with Inertia dimension):
  - Initial objection (Phase 1): [state it and name the Inertia Profile row it defends]
  - Practitioner's response (Phase 2): [spoke to it? silent? transformed? -- cite moment]
  - Advocate's response (Phase 3): [persisted? transformed? resolved? -- cite moment]
  - Final verdict: PERSISTED | TRANSFORMED | RESOLVED
    [If PERSISTED: does the Inertia Profile row remain intact?
     If RESOLVED: did the Advocate address the specific row or only the abstract position?]

Epistemic Weight Adjustment:
  For at least one evidence item, name the Experience-Proximity to the Inertia Profile
  workflow specifically and adjust synthesis weight:
  "Item [citation] is CONDITIONAL -- [subject] has observed [Inertia Profile row] but has
  not owned it. Their claim is a risk to monitor, not a confirmed blocker, until a GROUNDED
  owner confirms or refutes it."

PHASE 4 GATE
  [ ] Objection lifecycle traced with verdict, citation, and Inertia Profile row named
  [ ] At least one named epistemic weight adjustment referencing Inertia Profile proximity
  [ ] Patterns or contradictions traced to Inertia Profile rows where applicable

---

PHASE 5 -- META-OBSERVATIONS

PHASE 5A -- Simulation Fidelity Note: Name at least one grounded claim (anchored in a
documented role constraint or Inertia Profile dimension) and at least one place where
constructed plausibility was exercised. Distinguish the two explicitly.

PHASE 5B -- Voice Divergence Note: Name one concrete contrast between two subjects.
Cite a specific vocabulary choice, framing preference, or stance toward the Inertia Profile
that distinguishes them. Structural observations ("they had different inertia stances")
without a specific term or framing that belongs to one subject and not the other fail.
```

---

## V-05 -- Output Format + Lifecycle Emphasis: 4-Row Master Gate Table

**Axis**: Output format + lifecycle emphasis (combination)
**Hypothesis**: R8 V-05 scored 100/100 against v8 using a master gate table (Section 0-D) mapping prerequisite -> dependent mechanism -> binary status with 3 rows (C-22, C-13, C-18/C-27). For v9, the table is extended to 4 rows by adding Subject Cards complete as a named row. This changes Section 0-D from a prerequisite-to-mechanism map into the PRE-INTERVIEW MASTER GATE that names all four required items. The section is renamed accordingly. Every phase gate continues to use the named PHASE N GATE: [ ] ... checklist block format. Section-level STATUS CHECKs within each declaring section (C-22 STATUS in 0-A, C-28 STATUS in 0-B, C-13 STATUS in 0-C) are maintained -- creating double-layer verification. V-05 is the most densely structural variation: schema contract throughout, inline status checks, and the 4-row master gate table as a single auditable confirmation surface.

```
You are running a simulated stakeholder interview investigation for the feature topic: {{topic}}.

This is not a real interview. It is a structured simulation grounded in documented persona
knowledge, producing evidence artifacts for downstream topic narrative decisions.

Complete all phases in order. Do not write any transcript line before Phase 0 is fully closed.

---

SCHEMA CONTRACT RULE (applies throughout this document):

Every table that declares column headers as a structural template includes at least one
fully instantiated example row before any real data appears. A table with headers but no
example row is an open schema contract -- incomplete until instantiated.

---

PHASE 0 -- PRE-INTERVIEW STRUCTURE

---

SECTION 0-A -- SUBJECT CARDS

Schema declaration + instantiation:

| Field | Skeptic | Practitioner | Advocate |
|-------|---------|--------------|----------|
| Role | [e.g., "Senior Compliance Analyst -- 8 years managing regulated data pipelines"] | | |
| Evidential Function | [e.g., "Establishes the compliance objection surface; subsequent subjects must address it or leave it standing"] | | |
| Experience-Proximity + Justification | [e.g., "GROUNDED -- has personally owned the audit trail export process through two production incidents"] | | |
| Prior Knowledge | [e.g., "Knows the manual workaround, has seen two failed API migrations, understands the compliance clock constraint"] | | |
| Blind Spots | [e.g., "Has not used the new API-driven approach -- all objection grounded in prior failures, not the current alternative"] | | |
| Vocab Term 1 | [e.g., "audit immutability"] | | |
| Vocab Term 2 | [e.g., "compliance window"] | | |
| Vocab Term 3 | [e.g., "chain-of-custody"] | | |

Real data:

| Field | Skeptic | Practitioner | Advocate |
|-------|---------|--------------|----------|
| Role | | | |
| Evidential Function | | | |
| Experience-Proximity + Justification | | | |
| Prior Knowledge | | | |
| Blind Spots | | | |
| Vocab Term 1 | | | |
| Vocab Term 2 | | | |
| Vocab Term 3 | | | |

Sequence justification (one sentence): State why the chosen interview order is the optimal
ordering for this specific investigation -- name the structural reason.

C-22 STATUS CHECK:
  [ ] All three subjects have 3 specific vocabulary terms declared in the real data table.
      Trait descriptors ("uses technical language") instead of specific auditable terms fail.
      If any subject has fewer than 3 specific terms, C-22 is PARTIAL -- stop and fix
      before proceeding to Section 0-B.

---

SECTION 0-B -- MOMENT-LABEL DECISION SYSTEM

This section declares a complete three-label decision system. It governs all moment labels
in Phases 1, 2, and 3. It is a rule set, not a format guide.

Schema declaration + instantiation:

| Label | Decision Rule | When to Apply | What "Not Applicable" Looks Like | Required Format |
|-------|--------------|---------------|----------------------------------|-----------------|
| [e.g., SURPRISING] | [e.g., "Prior expectation from the Register was violated -- subject responded in a meaningfully different direction, intensity, or framing"] | [e.g., "Register entry exists and the response departs from it"] | [e.g., "Response differs from a vague general assumption with no register entry -- fix the register first"] | [e.g., "SURPRISING (expected: [Register -> Skeptic, Field: 'Expected Objection': '...'], got: [...])"] |
| CONFIRMING | Prior expectation from the Register was upheld -- subject said what was expected, validating a prior signal. Must trace to a named register field. | Register entry exists and the response matches it | Response is consistent with an undeclared general assumption -- must trace to a specific named field to count | CONFIRMING (validates: [Register -> Practitioner, Field: "Expected Confirmation": "..."]) |
| INCONCLUSIVE | Notable signal present but direction is genuinely ambiguous -- cannot be assigned to SURPRISING or CONFIRMING without additional evidence | Signal present; direction cannot be resolved by any register field | One of the above labels clearly fits -- do not use INCONCLUSIVE as a hedge | INCONCLUSIVE (closest register field: [Register -> Advocate, Field: "Expected Surprise"], ambiguity: [...]) |

Every labeled-moment section ends with one of:
  Option A: "All moments in this phase are unambiguously SURPRISING or CONFIRMING --
             no INCONCLUSIVE moments observed."
  Option B: [Apply INCONCLUSIVE label to the ambiguous moment using the format above]

C-28 STATUS CHECK:
  [ ] Decision system complete -- all three labels have declared decision rules AND
      "What Not Applicable Looks Like" for each. INCONCLUSIVE is fully specified.
      If any label is missing either the decision rule or the negative condition,
      C-28 is PARTIAL -- stop and complete before proceeding to Section 0-C.

---

SECTION 0-C -- EXPECTATION REGISTER

Declare prior expectations before any transcript begins. This register is the mandatory
structural source for all SURPRISING/CONFIRMING labels -- the "expected:" slot in each
moment label must name a row and field from this table.

Schema declaration + instantiation:

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [e.g., Skeptic -- Compliance Analyst] | [e.g., "Will require explicit compliance guarantee before any positive signal"] | [e.g., "Will object that no API-driven approach has cleared a compliance audit in this org"] | [e.g., "If compliance guarantee exists, will confirm workflow-reduction benefit is real"] | [e.g., "May admit current workaround generates its own compliance risk -- undercutting the status-quo defense"] |
| Practitioner | | | | |
| Advocate | | | | |

Real data:

| Subject | Expected Position | Expected Objection | Expected Confirmation | Expected Surprise |
|---------|------------------|--------------------|-----------------------|-------------------|
| [Skeptic] | | | | |
| [Practitioner] | | | | |
| [Advocate] | | | | |

C-13 STATUS CHECK:
  [ ] Register fully populated -- all cells in the real data table have content for all
      three subjects and all five columns. If any cell is empty, C-13 is PARTIAL -- stop
      and fix before proceeding. A PARTIAL C-13 cannot activate the C-25 bridge.
      Deploying the bridge against a PARTIAL register scores C-30 FAIL, not C-25 PASS.

---

SECTION 0-D -- PRE-INTERVIEW MASTER GATE

Before the first interview transcript begins, this table confirms that all structural
prerequisites for the interview phase are collectively and fully satisfied.
All four rows must show STATUS: COMPLETE before Phase 1 begins.

Schema declaration + instantiation:

| Prerequisite | What "COMPLETE" Means | Dependent Mechanisms | Status |
|--------------|----------------------|---------------------|--------|
| [e.g., Subject Cards complete] | [e.g., All three Subject Cards have all eight rows populated in the real data table; vocabulary terms are specific and auditable (C-22 STATUS CHECK passed)"] | [e.g., All phase transcripts (persona voice); vocabulary audits per phase; sequence justification"] | [e.g., "COMPLETE -- C-22 STATUS CHECK passed in Section 0-A"] |
| Expectation Register populated | All cells in the real data table filled; C-13 STATUS CHECK passed | Moment labels in all phases; C-25 bridge mechanism; objection lifecycle synthesis | [COMPLETE -- C-13 STATUS CHECK passed in Section 0-C / PARTIAL -- stop] |
| Vocabulary signatures declared for all subjects | Three specific auditable terms per subject in real data table; C-22 STATUS CHECK passed | Vocabulary audits per phase; voice divergence note | [COMPLETE / PARTIAL -- stop] |
| Moment-label decision taxonomy declared | All three labels have decision rules AND negative conditions; C-28 STATUS CHECK passed | Moment labels in all phases; INCONCLUSIVE acknowledgment; prerequisite confirmation before labels deploy | [COMPLETE -- C-28 STATUS CHECK passed in Section 0-B / PARTIAL -- stop] |

Real data:

| Prerequisite | What "COMPLETE" Means | Dependent Mechanisms | Status |
|--------------|----------------------|---------------------|--------|
| Subject Cards complete | All three cards fully populated in 0-A real data table; C-22 STATUS CHECK passed | All transcripts; vocabulary audits; sequence justification | [fill: COMPLETE / PARTIAL -- stop] |
| Expectation Register populated | All register cells filled; C-13 STATUS CHECK passed | Moment labels; C-25 bridge; objection lifecycle | [fill: COMPLETE / PARTIAL -- stop] |
| Vocabulary signatures declared | 3 specific auditable terms per subject; C-22 STATUS CHECK passed | Vocabulary audits; voice divergence | [fill: COMPLETE / PARTIAL -- stop] |
| Decision taxonomy declared | All 3 labels with rules + negative conditions; C-28 STATUS CHECK passed | Moment labels; INCONCLUSIVE check; C-30 gate | [fill: COMPLETE / PARTIAL -- stop] |

IMPORTANT: A PARTIAL status in any row means the dependent mechanisms that row activates
cannot deploy. Checking COMPLETE against a PARTIAL prerequisite scores C-30 FAIL for
every mechanism it activates. All four rows must show COMPLETE before Phase 1 begins.

---

PHASE 1 -- INTERVIEW: THE SKEPTIC

Transcript

Opening question: [Anchored in the Skeptic's declared prior knowledge and blind spots --
probe what specifically grounds their resistance]

[Skeptic]: [Answer in distinct Skeptic voice. Declared vocabulary terms must appear
naturally in their answers -- at least one of the three declared terms must surface.]

Follow-up (triggered by: "[exact phrase from the preceding answer that prompted this]"):
[follow-up anchored to prior answer]

[Skeptic]: [answer]

[Continue 2-3 additional exchanges. The Skeptic's primary objection must be clearly and
explicitly stated by the end of this transcript -- its lifecycle is tracked in Phase 4.]

---

Vocabulary Audit -- Skeptic

Prerequisite check: Subject Cards confirmed COMPLETE in PRE-INTERVIEW MASTER GATE
(row 1: C-22 STATUS CHECK passed in Section 0-A). Vocabulary signatures are fully
declared. Proceeding with audit.

Schema declaration + instantiation:

| Term | Status | Evidence |
|------|--------|----------|
| [e.g., "audit immutability"] | [e.g., FOUND] | [e.g., A2: "...the audit immutability requirement isn't negotiable..."] |
| [Term 2] | | |
| [Term 3] | | |

Real data:

| Term | Status | Evidence |
|------|--------|----------|
| [Vocab Term 1 from 0-A] | | |
| [Vocab Term 2] | | |
| [Vocab Term 3] | | |

At least 1 of 3 terms must be FOUND. [ ] vocabulary contract closed

---

Moment Label -- Skeptic

Prerequisite check: Register confirmed COMPLETE in PRE-INTERVIEW MASTER GATE (row 2:
C-13 STATUS CHECK passed in Section 0-C). C-25 bridge is authorized to deploy.
(If Register were PARTIAL, deploying the bridge would score C-30 FAIL -- the COMPLETE
status in the master gate is what authorizes it, not just the presence of the register.)

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Register -> Subject: Skeptic,
  Field: "{field_name}"], ...)

Ambiguity check: [Option A or Option B from Section 0-B]

---

Evidence Extraction -- Skeptic

Prerequisite check: Decision taxonomy confirmed COMPLETE in PRE-INTERVIEW MASTER GATE
(row 4: C-28 STATUS CHECK passed in Section 0-B). Both C-18/C-27 dimensions defined and
distinct. Proceeding with dual-taxonomy tagging.

  Experience-Proximity: GROUNDED | CONDITIONAL | INFERRED
    "How close is this subject to direct operational experience of this claim?"
  Origin-of-Claim: verbatim | inferred | corroborated
    "How was this claim derived from the transcript?"
  ORTHOGONALITY: These answer different questions. Do not substitute one for the other.

Schema declaration + instantiation:

| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Strength Rationale |
|---------------|-------------|---------------------|-----------------|----------|--------------------|
| [e.g., "Integration with legacy audit trail is non-negotiable -- any workaround adds a sprint."] | [e.g., feasibility concern] | [e.g., GROUNDED -- subject has operated the audit trail process for 3 years, firsthand] | [e.g., verbatim -- stated directly in A2: "non-negotiable"] | [e.g., strong] | [e.g., GROUNDED source stating it explicitly with operational specificity; no hedging language; "a sprint" adds count-based specificity] |

Real data:

| Evidence Item | Signal Type | Experience-Proximity | Origin-of-Claim | Strength | Strength Rationale |
|---------------|-------------|---------------------|-----------------|----------|--------------------|
| | | | | | |

---

PHASE 1 GATE
  [ ] Vocabulary contract closed -- at least 1 declared term FOUND in Skeptic's transcript
  [ ] Moment label references Register by subject name and field name
  [ ] Experience-Proximity and Origin-of-Claim both populated for every evidence row -- not conflated
  [ ] Skeptic's primary objection explicitly stated and identifiable in transcript

---

PHASE 2 -- INTERVIEW: THE PRACTITIONER

Transcript

[Same structure as Phase 1. At least one declared vocabulary term must appear naturally.
Questions probe operational ground truth. At least one question must probe whether the
Practitioner's operational reality speaks to -- or is silent about -- the Skeptic's
primary objection from Phase 1.]

---

Vocabulary Audit -- Practitioner

Prerequisite check: Subject Cards confirmed COMPLETE in PRE-INTERVIEW MASTER GATE
(row 1 -- C-22 STATUS CHECK passed). Proceeding.

Schema + instantiation + real data: [same format as Phase 1 Vocabulary Audit]

---

Moment Label -- Practitioner

Prerequisite check: Register confirmed COMPLETE in PRE-INTERVIEW MASTER GATE (row 2).
C-25 bridge authorized.

[SURPRISING / CONFIRMING / INCONCLUSIVE] (expected: [Register -> Subject: Practitioner,
  Field: "{field_name}"], ...)

Ambiguity check: [Option A or Option B from Section 0-B]

---

Evidence Extraction -- Practitioner

Prerequisite check: Decision taxonomy confirmed COMPLETE in PRE-INTERVIEW MASTER GATE
(row 4). Both dimensions kept distinct. "corroborated" now available for Origin-of-Claim
when a signal is consistent with Phase 1 evidence.

Schema + instantiation + real data: [same format as Phase 1 Evidence Extraction]

---

PHASE 2 GATE
  [ ] Vocabulary contract closed -- at least 1 declared term FOUND in Practitioner's transcript
  [ ] Moment label references Register by subject name and field name
  [ ] Both taxonomy dimensions populated for every evidence row -- not conflated
  [ ] Practitioner's response to (or silence about) Skeptic's primary objection is visible

---

PHASE 3 -- INTERVIEW: THE ADVOCATE

Transcript

[Same structure. At least one vocabulary term must appear naturally. Opening question
anchored in the Advocate's declared evidential function. At least one question probes the
Advocate's awareness of and response to the Skeptic's primary objection.]

---

Vocabulary Audit -- Advocate

Prerequisite check: Subject Cards confirmed COMPLETE in PRE-INTERVIEW MASTER GATE (row 1).
Proceeding.

Schema + instantiation + real data: [same format]

---

Moment Label -- Advocate

Prerequisite check: Register confirmed COMPLETE in PRE-INTERVIEW MASTER GATE (row 2).
C-25 bridge authorized.

Ambiguity check: [Option A or Option B from Section 0-B]

---

Evidence Extraction -- Advocate

Prerequisite check: Decision taxonomy confirmed COMPLETE in PRE-INTERVIEW MASTER GATE (row 4).
"corroborated" available from Phases 1+2.

Schema + instantiation + real data: [same format]

---

PHASE 3 GATE
  [ ] Vocabulary contract closed -- at least 1 declared term FOUND in Advocate's transcript
  [ ] Moment label references Register by subject name and field name
  [ ] Both taxonomy dimensions populated for every evidence row -- not conflated
  [ ] Advocate's response to (or evasion of) Skeptic's primary objection is visible

---

PHASE 4 -- CROSS-INTERVIEW SYNTHESIS

Prerequisite confirmation: PHASE 1, 2, and 3 GATES all closed. Proceeding to synthesis.

Patterns and Contradictions: Name at least one convergence or contradiction across the
three subjects. Cite the specific evidence items (by subject and response number) -- do
not summarize without reference.

Objection Lifecycle: Trace the Skeptic's primary objection from Phase 1.
  - Initial objection (Phase 1): [state it as declared in the transcript]
  - Practitioner's response (Phase 2): [addressed? transformed? silent? -- cite the moment]
  - Advocate's response (Phase 3): [persisted? transformed? resolved? -- cite the moment]
  - Final verdict: PERSISTED | TRANSFORMED | RESOLVED
    [one sentence naming the evidence that determines the verdict]

Epistemic Weight Adjustment: Adjust the weight of at least one evidence item based on
Experience-Proximity. Required format:
  "Item [evidence text] is CONDITIONAL -- [subject] has not experienced [specific blind
  spot from their Subject Card]. Treat as a risk to monitor, not a confirmed blocker,
  until a GROUNDED source who has encountered the alternative confirms or refutes it."

PHASE 4 GATE
  [ ] Objection lifecycle traced with PERSISTED / TRANSFORMED / RESOLVED verdict and citation
  [ ] At least one named epistemic weight adjustment with explicit CONDITIONAL/GROUNDED framing
  [ ] Convergence or contradiction cited with specific subject and evidence references

---

PHASE 5 -- META-OBSERVATIONS

SECTION 5-A -- Simulation Fidelity Note

Name at least one specific grounding basis: a documented persona knowledge claim, domain
context, or structural role constraint that anchored a specific simulated answer.
Also name at least one place where constructed plausibility was exercised -- not derived
from documented prior knowledge, but from role logic. Distinguish the two explicitly.

SECTION 5-B -- Voice Divergence Note

Name one concrete contrast in how two subjects were made to sound different.
Cite a specific vocabulary choice, framing preference, or concern priority that distinguishes
them. Example: "[Subject A] used '[Term X]' to frame the problem as a compliance boundary,
while [Subject B] used '[Term Y]' to frame it as an efficiency trade-off -- signaling
different priority hierarchies for the same constraint." Generic role statements without
a specific cited voice difference fail this criterion.
```
