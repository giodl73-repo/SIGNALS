---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 11
rubric_version: v11
status: VARIATE
---

# mock-review Variate — Round 11

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v11 (C-01 through C-32; aspirational denominator = 25)
**Round:** R11 — targeting v11 new criteria: C-32, C-33

---

## What R10 Left Open

R10 V-05 (the ceiling) achieved C-30 (SQ-1 citation sub-field in Structural position slot),
C-31 (TRIAD cardinality "(3 rules, all required)" in header), and C-25 fix (RATIONALE TEMPLATE
numbered declaration with two-slot cardinality assertion). The R9 C-26/C-27/C-28/C-29 criteria
were all preserved. Two residual partials drive C-32/C-33:

| Criterion | R10 ceiling coverage | Gap |
|-----------|---------------------|-----|
| C-21 partial → C-32 | R10 V-05 has VERDICT-ECHO named in two preamble sections: "Artifact state citation grammar" (names VERDICT-ECHO, gives detection rule) and "SQ-answer citation form" (names VERDICT-ECHO, structural rule, examples). C-21 PASSES. But C-32 requires the named error to be IN the SQ citation template field definition (`SQ answer driving verdict`), not only in surrounding preamble sections. The R10 V-05 field definition says "not a restatement" without embedding the error label. Preamble guidance is advisory; the field definition is structural. C-32 requires the violation to be classifiable from the template definition alone — cross-referencing preamble guidance does not satisfy this. | C-32 deepens C-21: C-21 requires a positive structural signal and a named prohibition in preamble; C-32 requires the named error label to appear within the SQ citation template field definition itself, with a classification rule embedded in the field — enabling classification at the field site without cross-referencing prior sections. A field that says "not a restatement" without naming the error type cannot classify a violation by type; it can only detect that something may be wrong. |
| C-24 partial → C-33 | R10 V-05 STEP 7 shows evaluation-driven next-steps entries as: `/{skill-id} {topic} — {Artifact state from STEP 6 decision block}` and adds: "An evaluation-driven entry that omits the Artifact state is a traceability break." The artifact state propagates (C-24 PASSES in V-05). But C-33 requires the format to DECLARE the `{Artifact state}` slot as structurally required with a named error label — converting the omission from a described consequence ("traceability break" as a noun phrase) into a classifiable named violation. | C-33 deepens C-24: C-24 requires the Artifact state field to propagate into next-steps entries; C-33 requires the next-steps entry format to explicitly declare the slot as required with a named error (e.g., TRACEABILITY-BREAK) so that an omission is identifiable by type at the format definition site. A format that shows the slot and notes its importance without naming the omission error does not satisfy C-33 — the error must be a declared type, not a described consequence. |

R10 recommendation for R11: (1) Test VERDICT-ECHO label IN the `SQ answer driving verdict`
field definition (C-32 axis) in isolation — no next-steps REQUIRED-SLOT declaration, no
Architect-first, no step-name anchors. (2) Test next-steps entry format REQUIRED-SLOT
declaration with named error TRACEABILITY-BREAK (C-33 axis) in isolation — no VERDICT-ECHO
in field definition, no Architect-first. (3) Test C-32 with boundary structural placement:
VERDICT-ECHO as a standalone labeled block within STEP 6, adjacent to templates but outside
the field definition — prediction: C-32 PARTIAL (concept at step level, not in template field).
(4) Combine C-32 + C-33 (Strategy-first, all structural features). (5) Ceiling: add C-32 + C-33
to R10 V-05 (Architect-first, PHASE GATE, step-name anchors, all prior preserved).

---

## Axis-Assignment Plan

| Var | Axis | Source signal | Target | Predicted |
|-----|------|--------------|--------|-----------|
| V-01 | output-format | R10 V-01 PHASE GATE base. VERDICT-ECHO error label embedded IN `SQ answer driving verdict` field definition with tense+subject classification test. TRIAD cardinality (C-31 PASS). SQ-1 citation sub-field (C-30 PASS). RATIONALE TEMPLATE 2-slot declaration (C-25 PASS). No next-steps REQUIRED-SLOT declaration (C-33 FAIL). No step-name anchors (C-28 FAIL). Role order: Strategy → PM → Arch (C-26 FAIL). | C-32 | C-32 PASS. C-29 PASS (PHASE GATE). C-31 PASS (TRIAD cardinality). C-30 PASS (SQ-1 sub-field). C-25 PASS (2-slot declaration). C-33 FAIL. C-28 FAIL. C-26 FAIL. Failure condition: VERDICT-ECHO label present in preamble only, not in field definition — confirmed by contrast with V-03. |
| V-02 | lifecycle-emphasis | R10 V-02 step-name-anchor base (inline TRIAD distributed — C-29 FAIL; Strategy-first — C-26 FAIL; SQ-1 citation sub-field — C-30 PASS; no PHASE GATE). Next-steps entry format adds REQUIRED SLOT declaration for {Artifact state} with named error TRACEABILITY-BREAK. No VERDICT-ECHO in field definition (C-32 FAIL). No TRIAD cardinality (C-31 FAIL). | C-33 | C-33 PASS. C-28 PASS (step-name anchors). C-30 PASS (SQ-1 sub-field). C-24 PASS (propagation + declared slot). C-32 FAIL. C-29 FAIL. C-31 FAIL. C-26 FAIL. Failure condition: TRACEABILITY-BREAK named as a noun phrase in surrounding text rather than as a declared type in the format slot definition — does not satisfy C-33. |
| V-03 | phrasing-register | Minimal base (Strategy-first, inline TRIAD distributed, no PHASE GATE, no step-name anchors, no SQ-1 sub-field, no next-steps REQUIRED-SLOT). VERDICT-ECHO CLASSIFICATION BLOCK placed as a labeled standalone subsection within STEP 6 — above the templates, after trigger field notation, but NOT inside the `SQ answer driving verdict` field definition. Tests whether VERDICT-ECHO at step-level (adjacent to templates) satisfies "template carries" in C-32. Predicted: C-32 PARTIAL — concept present at step level, violations detectable via block reference, but classification requires cross-referencing the block rather than reading the template field definition alone. | C-32 (boundary) | C-32 PARTIAL predicted. C-21 PASS (named error present at step level). C-26 FAIL. C-28 FAIL. C-29 FAIL. C-30 FAIL. C-31 FAIL. C-33 FAIL. Contrast case: demonstrates that co-location with the template section is insufficient; the label must be structurally embedded in the field definition for C-32 to pass. |
| V-04 | lifecycle-emphasis + output-format | C-32 + C-33 combined. PHASE GATE (C-29 PASS) with TRIAD header "(3 rules, all required)" (C-31 PASS) + VERDICT-ECHO IN field definition (C-32 PASS) + next-steps REQUIRED SLOT declaration with TRACEABILITY-BREAK (C-33 PASS) + RATIONALE TEMPLATE (2 required slots) (C-25 PASS) + SQ-1 citation sub-field (C-30 PASS). Step-name anchors in all gates (C-28 PASS). Role order: Strategy → PM → Arch (C-26 FAIL). | C-32, C-33 | C-32 PASS. C-33 PASS. C-25 PASS. C-28 PASS. C-29 PASS. C-30 PASS. C-31 PASS. C-26 FAIL (no Architect-first). Confirms C-32 and C-33 are structurally independent of role sequence. |
| V-05 | role-sequence + lifecycle-emphasis + output-format | Ceiling: R10 V-05 (Architect-first + PHASE GATE + step-name anchors + TRIAD cardinality + SQ-1 citation sub-field + RATIONALE TEMPLATE declaration + all prior criteria) + VERDICT-ECHO IN field definition (C-32) + next-steps REQUIRED SLOT declaration with TRACEABILITY-BREAK (C-33). All R10 V-05 criteria preserved: DEFAULT DECISION POSITION, entity-naming SQ grammar, canary false-positive prohibition, SQ answer driving verdict, artifact state propagation. | C-32, C-33 + all prior | C-26 PASS. C-27 PASS. C-28 PASS. C-29 PASS. C-30 PASS. C-31 PASS. C-32 PASS. C-33 PASS. All essential and recommended preserved. Full criterion set satisfied. |

---

## V-01 — Output Format (VERDICT-ECHO classification label in SQ template field; C-32 axis)

**axis:** output-format
**hypothesis:** Embedding the VERDICT-ECHO error label WITH a classification test (tense +
grammatical subject rule) INSIDE the `SQ answer driving verdict` field definition — not only
in surrounding preamble sections — satisfies C-32 independently of next-steps REQUIRED-SLOT
declaration (C-33 FAIL), step-name anchors (C-28 FAIL), or Architect-first ordering (C-26 FAIL).
The field definition must carry the label so violations are classifiable at the field site
without cross-referencing prior sections. Base: PHASE GATE (C-29 PASS), TRIAD "(3 rules, all
required)" (C-31 PASS), SQ-1 citation sub-field (C-30 PASS), RATIONALE TEMPLATE (2 required
slots) (C-25 PASS), Strategy → PM → Arch (C-26 FAIL), no step-name anchors (C-28 FAIL).
Expected: C-32 PASS; C-29 PASS; C-31 PASS; C-30 PASS; C-25 PASS; C-33 FAIL; C-28 FAIL;
C-26 FAIL.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is earned, not the default.
  A namespace earns MOCK-ACCEPTED only when all three role evaluations actively confirm
  it positively demonstrates what is required. Absence of disqualification is not positive
  evidence. REAL-REQUIRED is the null result; MOCK-ACCEPTED is the earned result.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract from each namespace section: namespace name, Category
field, current Status field. Read TOPICS.md. Record tier for {topic} and compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  content depth, or any role evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED. The critical designation
  applies at the structural level and cannot be waived by evaluation quality.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED. Compliance signals require
  real evidence; mock artifacts do not produce them.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting evaluation — default: REAL-REQUIRED): [{namespace}: Category = {value}]

DO NOT proceed to PHASE GATE until every namespace is placed in exactly one list.

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

All namespaces in the auto-flagged list are DECIDED. Their decisions are final and
unconditional. Role evaluation does not apply to them.
Namespaces in the remaining list proceed to role evaluation below.

FORBIDDEN OUTPUTS TRIAD (3 rules, all required — verified at this gate):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] must
  be present at this gate. A two-of-three set does not satisfy this gate requirement.

AUTO-RULE CONTAMINATION GUARD:
  Applying evaluation to any auto-flagged namespace is the named error AUTO-RULE
  CONTAMINATION. The automatic decision stands unconditionally. Any evaluation verdict
  applied to an auto-flagged namespace is void.
  DO NOT apply evaluation to auto-flagged namespaces.

DO NOT proceed to STEP 3 until:
  — two-list partition is confirmed
  — FORBIDDEN OUTPUTS TRIAD is verified complete (3 of 3 labels present at this gate)

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Strategy verdict.
Evaluation question: does this namespace positively demonstrate coverage adequacy for
Tier {tier}? Sub-questions require named artifacts — not yes/no answers.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates coverage adequacy").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 4 until Strategy verdicts are written for every remaining namespace.

---

STEP 4 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the PM verdict.
Evaluation question: does this namespace positively demonstrate structural completeness?
Sub-questions require named artifacts — not yes/no answers.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 until PM verdicts are written for every remaining namespace.

---

STEP 5 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Architect verdict.
Evaluation question: does this namespace positively demonstrate technical plausibility?
Sub-questions require named artifacts — not yes/no answers.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact that most directly confirms or challenges
        this namespace's escape from its REAL-REQUIRED default.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 until Architect verdicts are written for every remaining namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field notation: `trigger` field at fixed position in every decision block.
Values from this enumeration only:
  Auto-flagged:       EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven:  PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED:      n/a
Field uses lowercase `trigger` and equals-sign notation in all positions.

Artifact state citation grammar: Present-tense, artifact as grammatical subject,
observable state as object. Verdict echo (role as subject) is the named error
VERDICT-ECHO — DO NOT USE.
  Correct: "Section 3.2 lists no fallback path."
  Verdict echo (error): "Architect found no fallback path."

MOCK-ACCEPTED template (requires all three verdicts positive):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  RATIONALE TEMPLATE (2 required slots — both must be populated; one slot = RATIONALE INCOMPLETE):
  (1) Structural position (Strategy SQ-1 tier decision):
        Feeds tier decision: [Copy the Tier {tier} decision label from Strategy SQ-1 answer
          verbatim. A generic adequacy statement without this citation = SLOT VIOLATION.]
        Classify: STRUCTURAL-FORM (structural mock sufficient; no tier-boundary validation
          required) or TIER-GATING (real evidence required).
  (2) Contrast: [Name a namespace type that WOULD require real evidence and name the structural
        factor it has that this namespace does not. Must name BOTH a namespace type AND the
        distinguishing structural factor.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    Form: [Present-tense artifact-state form. Artifact as grammatical subject. Observable
      state as predicate. Name the specific artifact, section, or element whose observed
      state drove the failing evaluation.
      Example valid: "Section 4.1 contains no tier-boundary gate."]
    ERROR — VERDICT ECHO [classification label]: A sub-question answer in which the
      grammatical subject is a role name or evaluation noun rather than an artifact name.
      Classification test: if the field's grammatical subject is "Architect," "PM,"
      "Strategy," or any other role label, the field contains a VERDICT ECHO — a named
      violation. Example VERDICT ECHO: "Architect found no tier-boundary gate." — role
      as subject = VERDICT ECHO. A VERDICT ECHO in this field is void; rewrite using
      artifact-state form before this decision block is complete. This classification
      applies at the field site from the template definition alone — no cross-reference
      to prior sections required.
  Artifact state: [Present-tense artifact-state form — artifact as subject.]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

Complete all namespace decision templates.
DO NOT proceed to STEP 7 until every namespace has a completed decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Next Steps — fill all four sections; write "(none)" if empty; do not reorder.
  Ordering rule stated explicitly: "Critical namespaces first (trace, scout-feasibility,
  listen), evidence-heavy last."

  Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    Evaluation-driven: /{skill-id} {topic} — {Artifact state from STEP 6 decision block}
    Auto-flagged:      /{skill-id} {topic} — trigger: {trigger value}
  Priority 2 — Non-critical REAL-REQUIRED:
    Same entry formats as Priority 1.
  Priority 3 — Evidence-heavy REAL-REQUIRED:
    /{skill-id} {topic} — trigger: EVIDENCE-HEAVY
  Cross-namespace risk statement:
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 until the review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place. Replace every Status field.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [code]  OR  Status: REAL-REQUIRED [trigger]

Canary Confirmation — output protocol:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  This line is an assertion. Writing it when any Status field remains MOCK is
  the named error CANARY-FALSE-POSITIVE. DO NOT write it unless the condition is verified.
  If any field was not updated: suppress the canary; output:
    "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"
  Attempt remaining edits. Re-verify. Write canary only when condition is met.

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-02 — Lifecycle Emphasis (next-steps REQUIRED-SLOT declaration with named error; C-33 axis)

**axis:** lifecycle-emphasis
**hypothesis:** Structurally declaring `{Artifact state}` as a REQUIRED SLOT in the next-steps
entry format — with a named error class (TRACEABILITY-BREAK) for entries that omit the slot —
satisfies C-33 independently of VERDICT-ECHO in the SQ template field definition (C-32 FAIL),
PHASE GATE (C-29 FAIL), TRIAD cardinality (C-31 FAIL), or Architect-first ordering (C-26 FAIL).
The declaration must name the omission as a classified error type, not merely describe it as a
consequence. Base: R10 V-02 (step-name anchors in all inter-step gates — C-28 PASS; inline
TRIAD distributed — C-29 FAIL; SQ-1 citation sub-field — C-30 PASS; Strategy-first — C-26 FAIL;
no TRIAD cardinality — C-31 FAIL). Expected: C-33 PASS; C-24 PASS; C-28 PASS; C-30 PASS;
C-32 FAIL; C-29 FAIL; C-31 FAIL; C-26 FAIL.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is earned, not the default.
  A namespace earns MOCK-ACCEPTED only when all three role evaluations actively confirm
  it positively demonstrates what is required. Absence of disqualification is not positive
  evidence. REAL-REQUIRED is the null result; MOCK-ACCEPTED is the earned result.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract from each namespace section: namespace name, Category
field, current Status field. Read TOPICS.md. Record tier for {topic} and compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  content depth, or any role evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED. The critical designation
  applies at the structural level and cannot be waived by evaluation quality.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED. Compliance signals require
  real evidence; mock artifacts do not produce them.

DO NOT apply Strategy, PM, or Architect evaluation to any auto-flagged namespace.
Applying role evaluation to a namespace already decided by an automatic rule is the
named error AUTO-RULE CONTAMINATION. The automatic decision stands unconditionally.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting evaluation — default: REAL-REQUIRED): [{namespace}: Category = {value}]

DO NOT proceed to STEP 3 (Strategy Evaluation) until every namespace is placed in exactly
one list.

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Strategy verdict.
Evaluation question: does this namespace positively demonstrate coverage adequacy for
Tier {tier}? Sub-questions require named artifacts — not yes/no answers.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates coverage adequacy").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 4 (PM Evaluation) until Strategy verdicts are written for every
remaining namespace.

---

STEP 4 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the PM verdict.
Evaluation question: does this namespace positively demonstrate structural completeness?
Sub-questions require named artifacts — not yes/no answers.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 (Architect Evaluation) until PM verdicts are written for every
remaining namespace.

---

STEP 5 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Architect verdict.
Evaluation question: does this namespace positively demonstrate technical plausibility?
Sub-questions require named artifacts — not yes/no answers.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact that most directly confirms or challenges
        this namespace's escape from its REAL-REQUIRED default.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 (Decisions with Citation) until Architect verdicts are written
for every remaining namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field notation: `trigger` field at fixed position. Values from enumeration only:
  Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED: n/a

Artifact state citation grammar: Present-tense, artifact as grammatical subject.
Verdict echo (role as subject) is the named error VERDICT-ECHO — DO NOT USE.
  Correct: "Section 3.2 lists no fallback path."
  Verdict echo (error): "Architect found no fallback path."

MOCK-ACCEPTED template (requires all three verdicts positive):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)
  Structural position (Strategy SQ-1 tier decision):
    Feeds tier decision: [Copy the Tier {tier} decision label from Strategy SQ-1 answer
      verbatim. A generic adequacy statement without this citation = SLOT VIOLATION.]
    Classify: STRUCTURAL-FORM (structural mock sufficient; no tier-boundary validation
      required) or TIER-GATING (real evidence required).
  Contrast: [Name a namespace type that WOULD require real evidence and name the structural
    factor it has that this namespace does not. Must name BOTH a namespace type AND the
    distinguishing structural factor.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [full verdict string]
  Artifact state: [Present-tense artifact-state — artifact as subject.]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

Complete all namespace decision templates.
DO NOT proceed to STEP 7 (Write Review Artifact) until every namespace has a completed
decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Next Steps — fill all four sections; write "(none)" if empty; do not reorder.
  Ordering rule stated explicitly: "Critical namespaces first (trace, scout-feasibility,
  listen), evidence-heavy last."

  Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* namespaces first, then scout-feasibility, then listen-*, scout-competitors]

    Evaluation-driven entry format — REQUIRED SLOTS: {skill-id}, {topic}, {Artifact state}:
      /{skill-id} {topic} — {Artifact state}
      Slot declaration: `{Artifact state}` is a REQUIRED SLOT propagated from the STEP 6
      decision block. An evaluation-driven entry that names only skill-id and topic without
      the `{Artifact state}` slot is the named error TRACEABILITY-BREAK. A TRACEABILITY-BREAK
      entry is structurally incomplete and does not satisfy this format requirement — it must
      be corrected before the review artifact is considered complete.

    Auto-flagged entry format:
      /{skill-id} {topic} — trigger: {trigger value}

  Priority 2 — Non-critical REAL-REQUIRED:
    Same entry formats and slot declaration as Priority 1.

  Priority 3 — Evidence-heavy REAL-REQUIRED:
    /{skill-id} {topic} — trigger: EVIDENCE-HEAVY

  Cross-namespace risk statement:
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place. Replace every Status field.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [code]  OR  Status: REAL-REQUIRED [trigger]

Canary Confirmation: DO NOT write confirmation unless zero Status fields remain MOCK.
Writing it unverified is CANARY-FALSE-POSITIVE. Suppress and list unupdated namespaces.
Re-verify. Write canary only when condition is met.

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-03 — Phrasing Register (VERDICT-ECHO adjacent block, not in field def; C-32 boundary)

**axis:** phrasing-register
**hypothesis:** Placing a labeled VERDICT-ECHO CLASSIFICATION BLOCK as a standalone section
within STEP 6 — between trigger field notation and the decision templates, but structurally
OUTSIDE the `SQ answer driving verdict` field definition — does NOT satisfy C-32. C-32 requires
the error to be IN the template (the field definition); an adjacent block makes violations
detectable via block reference, but classification still requires cross-referencing the block
rather than reading the field definition alone. This is the contrast case establishing the
boundary between C-21 PASS (named error present at step level) and C-32 PASS (named error
inside the template field). Minimal base: Strategy-first, inline TRIAD distributed in rule
bodies (C-29 FAIL), no PHASE GATE, no step-name anchors (C-28 FAIL), no SQ-1 citation
sub-field (C-30 FAIL), no next-steps REQUIRED-SLOT declaration (C-33 FAIL).
Expected: C-32 PARTIAL; C-21 PASS; C-26 FAIL; C-28 FAIL; C-29 FAIL; C-30 FAIL; C-31 FAIL;
C-33 FAIL.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. This is the starting state, not a finding.
  MOCK-ACCEPTED is an earned escape from the default. The inertia structure requires a
  positive argument — a namespace earns MOCK-ACCEPTED only when all three role evaluations
  actively confirm it positively demonstrates what is required. Confirmation that nothing
  is wrong is not a positive argument.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract from each namespace section: namespace name, Category
field, current Status field. Read TOPICS.md. Record tier for {topic} and compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  content depth, or any role evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED. The critical designation
  applies at the structural level and cannot be waived.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED. Compliance signals require
  real evidence; mock artifacts do not produce them.

DO NOT apply Strategy, PM, or Architect evaluation to any auto-flagged namespace.
Applying role evaluation to an already-decided namespace is the named error AUTO-RULE
CONTAMINATION. The automatic decision stands unconditionally.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting evaluation — default: REAL-REQUIRED): [{namespace}: Category = {value}]

DO NOT proceed to STEP 3 until every namespace is placed in exactly one list.

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Strategy verdict.
Evaluation question: does this namespace positively demonstrate coverage adequacy for
Tier {tier}? Sub-questions require named artifacts — not yes/no answers.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates coverage adequacy").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 4 until Strategy verdicts are written for every remaining namespace.

---

STEP 4 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the PM verdict.
Evaluation question: does this namespace positively demonstrate structural completeness?
Sub-questions require named artifacts — not yes/no answers.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 until PM verdicts are written for every remaining namespace.

---

STEP 5 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Architect verdict.
Evaluation question: does this namespace positively demonstrate technical plausibility?
Sub-questions require named artifacts — not yes/no answers.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact that most directly confirms or challenges
        this namespace's escape from its REAL-REQUIRED default.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 until Architect verdicts are written for every remaining namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field notation: `trigger` field at fixed position in every decision block.
Values from this enumeration only:
  Auto-flagged:       EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven:  PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED:      n/a

VERDICT-ECHO CLASSIFICATION BLOCK:
  A sub-question answer that restates the evaluation verdict rather than citing an artifact
  is the named error VERDICT-ECHO. This error is classifiable by form:
    — Required form: present-tense, artifact as grammatical subject, observable state as
      predicate. Example: "Section 4.1 contains no tier-boundary gate."
    — VERDICT-ECHO form: role or evaluation noun as grammatical subject, past-tense
      assessment. Example: "Architect found no tier-boundary gate." — role as subject
      = VERDICT-ECHO.
  A VERDICT-ECHO in any citation field is a named violation. Rewrite in required form
  before the decision block is complete.
  [Note: this classification block is positioned at the step level, adjacent to the
  decision templates but not within any individual field definition.]

MOCK-ACCEPTED template (requires all three verdicts positive):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)
  Structural position (Strategy SQ-1 tier decision): [Name the specific Tier {tier}
    decision from Strategy SQ-1. Classify: STRUCTURAL-FORM or TIER-GATING.]
  Contrast: [Name a namespace type that WOULD require real evidence and the structural
    factor distinguishing it from this namespace.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [full verdict string]
  Artifact state: [Present-tense artifact-state — artifact as subject; not a restatement
    of the verdict. See VERDICT-ECHO CLASSIFICATION BLOCK above for error form.]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

Complete all namespace decision templates.
DO NOT proceed to STEP 7 until every namespace has a completed decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Next Steps — fill all four sections; write "(none)" if empty; do not reorder.
  Ordering rule stated explicitly: "Critical namespaces first (trace, scout-feasibility,
  listen), evidence-heavy last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {trigger or artifact state}
  Priority 2 — Non-critical REAL-REQUIRED: /{skill-id} {topic} — {trigger or artifact state}
  Priority 3 — Evidence-heavy REAL-REQUIRED: /{skill-id} {topic} — trigger: EVIDENCE-HEAVY
  Cross-namespace risk statement:
    "Highest-risk gap: {namespace} — {Tier {tier} decision at risk} — urgency: {level}"

DO NOT proceed to STEP 8 until the review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place. Replace every Status field.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [code]  OR  Status: REAL-REQUIRED [trigger]

Canary Confirmation: DO NOT write confirmation unless zero Status fields remain MOCK.
Writing it unverified is CANARY-FALSE-POSITIVE. Suppress and list unupdated namespaces.

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-04 — Lifecycle Emphasis + Output Format (C-32 + C-33 combined; Strategy-first)

**axis:** lifecycle-emphasis + output-format
**hypothesis:** C-32 (VERDICT-ECHO label IN field definition with classification test) and
C-33 (next-steps REQUIRED-SLOT declaration with named error TRACEABILITY-BREAK) can both
be achieved together before introducing the role-sequence change (C-26). PHASE GATE (C-29
PASS). Step-name anchors in all inter-step gates (C-28 PASS). TRIAD "(3 rules, all required)"
(C-31 PASS). SQ-1 citation sub-field (C-30 PASS). RATIONALE TEMPLATE (2 required slots)
(C-25 PASS). Role order: Strategy → PM → Arch (C-26 FAIL). Tests whether the two new
template structural changes are independent of role ordering. Expected: C-32 PASS; C-33 PASS;
C-25 PASS; C-28 PASS; C-29 PASS; C-30 PASS; C-31 PASS; C-26 FAIL; all prior essential
and recommended criteria preserved.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is earned, not the default.
  A namespace earns MOCK-ACCEPTED only when all three role evaluations actively confirm
  it positively demonstrates what is required. Absence of disqualification is not positive
  evidence. REAL-REQUIRED is the null result; MOCK-ACCEPTED is the earned result.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract from each namespace section: namespace name, Category
field, current Status field. Read TOPICS.md. Record tier for {topic} and compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  content depth, or any role evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED. The critical designation
  applies at the structural level and cannot be waived by evaluation quality.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED. Compliance signals require
  real evidence; mock artifacts do not produce them.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting evaluation — default: REAL-REQUIRED): [{namespace}: Category = {value}]

DO NOT proceed to PHASE GATE until every namespace is placed in exactly one list.

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

All namespaces in the auto-flagged list are DECIDED. Their decisions are final and
unconditional. Role evaluation does not apply to them.
Namespaces in the remaining list proceed to role evaluation below.

FORBIDDEN OUTPUTS TRIAD (3 rules, all required — single verification point at this gate,
independent of role sequence):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] must
  be present. A two-of-three set does not satisfy this gate requirement.
  This co-location design enables independent satisfaction of C-26 (role ordering) and
  C-27 (enumerable triad): verified here, at the gate, before any role step runs.

AUTO-RULE CONTAMINATION GUARD:
  Applying evaluation to any auto-flagged namespace is the named error AUTO-RULE
  CONTAMINATION. The automatic decision stands unconditionally.
  DO NOT apply evaluation to auto-flagged namespaces.

DO NOT proceed to STEP 3 (Strategy Evaluation) until:
  — two-list partition is confirmed
  — FORBIDDEN OUTPUTS TRIAD is verified complete (3 of 3 labels present at this gate)

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Strategy verdict.
Evaluation question: does this namespace positively demonstrate coverage adequacy for
Tier {tier}? Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates coverage adequacy").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 4 (PM Evaluation) until Strategy verdicts are written for every
remaining namespace.

---

STEP 4 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the PM verdict.
Evaluation question: does this namespace positively demonstrate structural completeness?
Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 (Architect Evaluation) until PM verdicts are written for every
remaining namespace.

---

STEP 5 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Architect verdict.
Evaluation question: does this namespace positively demonstrate technical plausibility?
Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact that most directly confirms or challenges
        this namespace's escape from its REAL-REQUIRED default.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 (Decisions with Citation) until Architect verdicts are written
for every remaining namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field notation: `trigger` at fixed position. Values from enumeration only:
  Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED: n/a

Artifact state citation grammar: Present-tense, artifact as grammatical subject,
observable state as object. Verdict echo (role as subject) is the named error
VERDICT-ECHO — DO NOT USE.

MOCK-ACCEPTED template (requires all three verdicts positive):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  RATIONALE TEMPLATE (2 required slots — both must be populated; one slot = RATIONALE INCOMPLETE):
  (1) Structural position (Strategy SQ-1 tier decision):
        Feeds tier decision: [Copy the Tier {tier} decision label from Strategy SQ-1 answer
          verbatim — name the specific decision this namespace supports. Generic adequacy
          statement without this citation = SLOT VIOLATION.]
        Classify: STRUCTURAL-FORM (structural mock sufficient; no tier-boundary validation
          required) or TIER-GATING (real evidence required; decision depends on live system
          state at tier boundaries).
  (2) Contrast: [Name a namespace type that WOULD require real evidence and name the structural
        factor it has that this namespace does not. Must name BOTH a namespace type AND the
        distinguishing structural factor. Form: "Unlike {namespace type}, which carries
        {structural factor}, this namespace's outputs are fully determined by {structural form}."]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    Form: [Present-tense artifact-state form. Artifact as grammatical subject. Observable
      state as predicate. Name the specific artifact, section, or element whose observed
      state drove the failing evaluation.
      Example valid: "Section 4.1 contains no tier-boundary gate."]
    ERROR — VERDICT ECHO [classification label]: A sub-question answer in which the
      grammatical subject is a role name or evaluation noun rather than an artifact name.
      Classification test: if the grammatical subject is "Architect," "PM," "Strategy,"
      or any role label, the field contains a VERDICT ECHO — a named violation. Example
      VERDICT ECHO: "Architect found no tier-boundary gate." — role as subject = VERDICT ECHO.
      A VERDICT ECHO in this field is void; rewrite using artifact-state form before this
      decision block is complete. Classifiable at the field site from this template
      definition alone.
  Artifact state: [Present-tense artifact-state — artifact as subject.]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

Complete all namespace decision templates.
DO NOT proceed to STEP 7 (Write Review Artifact) until every namespace has a completed
decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Next Steps — fill all four sections; write "(none)" if empty; do not collapse or reorder.
  Ordering rule stated explicitly: "Critical namespaces first (trace, scout-feasibility,
  listen), evidence-heavy last."

  Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* namespaces first, then scout-feasibility, then listen-*, scout-competitors]

    Evaluation-driven entry format — REQUIRED SLOTS: {skill-id}, {topic}, {Artifact state}:
      /{skill-id} {topic} — {Artifact state}
      Slot declaration: `{Artifact state}` is a REQUIRED SLOT propagated from the STEP 6
      decision block (field: `Artifact state`). An evaluation-driven entry that names only
      skill-id and topic without the `{Artifact state}` slot is the named error
      TRACEABILITY-BREAK. A TRACEABILITY-BREAK entry does not satisfy this format requirement
      and must be corrected before the review artifact is complete.

    Auto-flagged entry format:
      /{skill-id} {topic} — trigger: {trigger value}

  Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    Same entry formats and slot declaration as Priority 1.

  Priority 3 — Evidence-heavy REAL-REQUIRED:
    /{skill-id} {topic} — trigger: EVIDENCE-HEAVY

  Cross-namespace risk statement (required output):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place. Replace every Status field.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [code]  OR  Status: REAL-REQUIRED [trigger]

Canary Confirmation: DO NOT write confirmation unless zero Status fields remain MOCK.
Writing it unverified is CANARY-FALSE-POSITIVE. Suppress and list unupdated namespaces.
Re-verify. Write canary only when condition is met.

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-05 — Full Integration (C-32 + C-33 + all R10 V-05 criteria; Architect-first)

**axis:** role-sequence + lifecycle-emphasis + output-format
**hypothesis:** Adding VERDICT-ECHO classification label IN the `SQ answer driving verdict`
field definition (C-32) and next-steps REQUIRED-SLOT declaration with named error
TRACEABILITY-BREAK (C-33) to the R10 V-05 ceiling design achieves the full v11 criterion set.
The PHASE GATE + TRIAD at gate (C-29) preserves the decoupling between C-26 (role ordering)
and C-27 (enumerable triad). Architect-first + cross-step guard naming `architect-verdict =
CONTRADICTS-ARCHITECTURE` and PM Evaluation as the suppressed step (C-26). Step-name anchors
in all inter-step gates (C-28). All R10 V-05 criteria preserved: DEFAULT DECISION POSITION,
entity-naming SQ grammar, VERDICT-ECHO named error in preamble (C-21), SQ answer driving
verdict in REAL-REQUIRED template, SQ-1 citation sub-field (C-30), RATIONALE TEMPLATE
2-slot declaration (C-25), TRIAD cardinality (C-31), canary false-positive prohibition (C-16).
C-32 adds the classification label INSIDE the field definition. C-33 adds the REQUIRED-SLOT
declaration with TRACEABILITY-BREAK in next-steps. Expected: C-25 PASS, C-26 PASS, C-27 PASS,
C-28 PASS, C-29 PASS, C-30 PASS, C-31 PASS, C-32 PASS, C-33 PASS; all prior essential and
recommended criteria preserved. Full criterion set satisfied.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. This is the starting state — not a finding,
  not a judgment. MOCK-ACCEPTED is an earned outcome that requires an argument against
  the default. A namespace earns MOCK-ACCEPTED only when all three role evaluations
  actively confirm it positively demonstrates what is required. Absence of disqualification
  is not positive evidence. The inertia structure forces a genuine contrastive argument —
  confirmation that nothing is wrong does not earn escape from REAL-REQUIRED.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract from each namespace section: namespace name, Category
field, current Status field. Read TOPICS.md. Record tier for {topic} and compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  content depth, or any role evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED. The critical designation
  applies at the structural level and cannot be waived.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED. Compliance signals require
  real evidence; mock artifacts do not produce them.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting evaluation — default: REAL-REQUIRED): [{namespace}: Category = {value}]

DO NOT proceed to PHASE GATE until every namespace is placed in exactly one list.

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

All namespaces in the auto-flagged list are DECIDED. Their decisions are final and
unconditional. Role evaluation does not apply to them.
Namespaces in the remaining list proceed to role evaluation below.

FORBIDDEN OUTPUTS TRIAD (3 rules, all required — single verification point at this gate,
independent of role sequence):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] must
  be present. A two-of-three set does not satisfy this gate requirement.
  This co-location design enables independent satisfaction of C-26 (role ordering) and
  C-27 (enumerable triad): the triad is verified here, at the gate, before any role
  step runs — making it independent of which role runs first.

AUTO-RULE CONTAMINATION GUARD:
  Applying evaluation (Architect, Strategy, or PM) to any auto-flagged namespace is the
  named error AUTO-RULE CONTAMINATION. The automatic decision stands unconditionally.
  Any evaluation verdict applied to an auto-flagged namespace is void and must be discarded.
  DO NOT apply evaluation to auto-flagged namespaces.

DO NOT proceed to STEP 3 (Architect Evaluation) until:
  — two-list partition is confirmed
  — FORBIDDEN OUTPUTS TRIAD is verified complete (3 of 3 labels present at this gate)

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions then write the Architect verdict.
Evaluation question: does this namespace positively demonstrate technical plausibility?
Sub-questions use "Name X" or "What specific X" grammar — a yes/no answer does not satisfy.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this namespace's escape from its REAL-REQUIRED default position.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

Complete Architect evaluation for ALL remaining namespaces.

CROSS-STEP GUARD — Architect to PM (C-26):
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
    Strategy Evaluation (STEP 4) may still run for all namespaces — coverage gap synthesis.
  Record the cross-step guard lists:
    Blocked from PM Evaluation (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to PM Evaluation (architect-verdict = CONSISTENT-WITH-ARCHITECTURE): [{list}]

  This guard fires on the specific verdict value `architect-verdict = CONTRADICTS-ARCHITECTURE`
  and blocks the specific downstream step PM Evaluation (STEP 5). It is distinct from the
  AUTO-RULE CONTAMINATION GUARD at the PHASE GATE — that guard blocks evaluation of
  auto-flagged namespaces; this guard fires on a verdict value within the evaluation phase.
  DO NOT conflate the two guards.

DO NOT proceed to STEP 4 (Strategy Evaluation) until Architect verdicts and cross-step
guard assignments are complete for all remaining namespaces.

---

STEP 4 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace (including cross-step-blocked — for coverage gap synthesis),
answer sub-questions then write the Strategy verdict.
Evaluation question: does this namespace positively demonstrate coverage adequacy for
Tier {tier}? Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates coverage adequacy").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts are written for every
remaining namespace.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces where architect-verdict =
CONSISTENT-WITH-ARCHITECTURE. Namespaces on the cross-step-blocked list DO NOT proceed
to PM evaluation — their decision is already determined. Applying PM evaluation to a
cross-step-blocked namespace is the named error GUARD-BYPASS CONTAMINATION.

For each qualifying namespace, answer sub-questions then write the PM verdict.
Evaluation question: does this namespace positively demonstrate structural completeness?
Sub-questions use "Name X" or "What specific X" grammar — yes/no not sufficient.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL qualifying namespaces.
DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for every
qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field notation: The `trigger` field is a named artifact field at fixed position.
  Second line of every REAL-REQUIRED block; third line of every MOCK-ACCEPTED block.
  Values from this enumeration only (lowercase, equals-sign notation):
    Auto-flagged:      EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
    Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
    MOCK-ACCEPTED:     n/a

Artifact state citation grammar: Present-tense, artifact as grammatical subject, observable
state as object. Verdict echo is the named error VERDICT-ECHO — detectable when grammatical
subject is a role name or evaluation noun rather than an artifact name.
  Correct: "Section 3.2 lists no fallback path for this namespace."
  Verdict echo (named error): "Architect found no fallback path."

SQ-answer citation form: The sub-question answer field names a specific artifact in
present-tense artifact-state form. It is structurally distinguished from a verdict restatement
by having the artifact as subject, not the role. "Section 4.1 contains no tier-boundary gate"
is an SQ answer. "Architect found no gate" is a verdict echo. This distinction is a structural
rule — the named error is VERDICT-ECHO.

MOCK-ACCEPTED template (requires all three verdicts positive; PM-qualified namespaces only):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes; both when both apply)

  RATIONALE TEMPLATE (2 required slots — both must be populated; one slot = RATIONALE INCOMPLETE):
  (1) Structural position (Strategy SQ-1 tier decision):
        Feeds tier decision: [Copy the Tier {tier} decision label from Strategy SQ-1 answer
          verbatim — name the specific decision this namespace supports. A generic adequacy
          statement without this SQ-1 citation = SLOT VIOLATION. Example of SLOT VIOLATION:
          "this namespace has limited scope." Example of valid field: "Tier 1 scope gate:
          whether {topic} requires trace-level signal before proceeding."]
        Classify: STRUCTURAL-FORM (structural mock sufficient; no tier-boundary validation
          required) or TIER-GATING (real evidence required; decision depends on live system
          state at tier boundaries). The slot requires the SQ-1 decision citation AND the
          type classification. Generic adequacy without both = SLOT VIOLATION.
  (2) Contrast: [Name a namespace type that WOULD require real evidence and state the
        structural factor it has that this namespace does not. Must name BOTH a namespace
        type AND the distinguishing structural factor. Form: "Unlike {namespace type}, which
        carries {structural factor} that requires real evidence because {reason}, this
        namespace's outputs are fully determined by {structural form property}."]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    Form: [Present-tense artifact-state form. Artifact as grammatical subject. Observable
      state as predicate. Name the specific artifact, section, or element whose observed
      state drove the failing evaluation.
      Example valid: "Section 4.1 contains no tier-boundary gate."]
    ERROR — VERDICT ECHO [classification label]: A sub-question answer in which the
      grammatical subject is a role name or evaluation noun rather than an artifact name.
      Classification test: if the grammatical subject is "Architect," "PM," "Strategy,"
      or any role label, the field contains a VERDICT ECHO — a named violation. Example
      VERDICT ECHO: "Architect found no tier-boundary gate." — role as subject = VERDICT ECHO.
      Tense and subject together distinguish the forms: past-tense assessment with role as
      subject = VERDICT ECHO (void; rewrite required). Present-tense observable state with
      artifact as subject = valid SQ citation. Classifiable at the field site from this
      template definition alone — no cross-reference to prior sections required.
  Artifact state: [Present-tense artifact-state — artifact as subject]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

Complete all namespace decision templates.
DO NOT proceed to STEP 7 (Write Review Artifact) until every namespace has a completed
decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |
    One row per namespace; all namespaces from the PHASE GATE partition and STEP 6.

  Next Steps — fill all four sections; write "(none)" if empty; do not collapse or reorder.
  Ordering rule stated explicitly: "Critical namespaces first (trace, scout-feasibility,
  listen), evidence-heavy last."

  Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* namespaces first, then scout-feasibility, then listen-*, scout-competitors]

    Evaluation-driven entry format — REQUIRED SLOTS: {skill-id}, {topic}, {Artifact state}:
      /{skill-id} {topic} — {Artifact state}
      Slot declaration: `{Artifact state}` is a REQUIRED SLOT propagated from the STEP 6
      decision block (field: `Artifact state`). An evaluation-driven next-steps entry that
      names only skill-id and topic without the `{Artifact state}` slot is the named error
      TRACEABILITY-BREAK. A TRACEABILITY-BREAK entry is structurally incomplete — it breaks
      the end-to-end traceability chain (SQ answer driving verdict → Artifact state field →
      next-steps entry) and must be corrected before the review artifact is complete.

    Auto-flagged entry format:
      /{skill-id} {topic} — trigger: {trigger value}
      An auto-flagged entry that omits the trigger value is a traceability break.

  Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    Same entry formats and REQUIRED SLOTS declaration as Priority 1.

  Priority 3 — Evidence-heavy REAL-REQUIRED (sequence after Priority 1 and 2):
    /{skill-id} {topic} — trigger: EVIDENCE-HEAVY

  Cross-namespace risk statement (required output):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

This is the defining action of /mock:review. It is not optional.

Edit {mock-artifact-path} in-place using Edit tool. In-place replacement only.
Do not rewrite any other content.

For each namespace:
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  OR:      Status: REAL-REQUIRED [{trigger value from canonical field}]

After completing all edits, verify before confirming.

Canary Confirmation — output protocol:
  The following line is a CANARY OUTPUT:
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  This line is an assertion that the stated condition is true. Writing this line when any
  Status field remains as MOCK (awaiting review) is the named error CANARY-FALSE-POSITIVE.
  This error is not recoverable — the canary's value is that its presence asserts the
  condition is met; a false-positive canary destroys the assertion's meaning.

  Protocol:
    — Write the canary ONLY after confirming zero Status fields remain as MOCK.
    — If any Status field was not updated: suppress the canary. Output instead:
        "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"
      Attempt remaining edits. Re-verify. Write canary only when condition is met.
    — DO NOT write the canary confirmation if the stated condition is not verified.

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
