---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 10
rubric_version: v10
status: VARIATE
---

# mock-review Variate — Round 10

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v10 (C-01 through C-31; aspirational denominator = 23)
**Round:** R10 — targeting v10 new criteria: C-30, C-31

---

## What R9 Left Open

R9 V-05 (the ceiling) achieved C-26 (Architect-first + named cross-step guard), C-27
(enumerable TRIAD at PHASE GATE), C-28 (step-name anchors in all forward references), and
C-29 (TRIAD co-located at PHASE GATE, decoupled from role ordering). The R8 C-26/C-27
mutual exclusivity was resolved. Two residual partials drive C-30/C-31:

| Criterion | R9 ceiling coverage | Gap |
|-----------|---------------------|-----|
| C-23 partial → C-30 | R9 V-05 has `Structural position (Strategy SQ-1 tier decision)` as slot label — SQ-1 named conceptually as the slot's source (C-23 PASS in V-05). But no sub-field encodes the SQ-1 answer as a citation field. The slot instructs "Name the decision from SQ-1" but the author's SQ-1 answer is not mechanically captured in a declared sub-field. | C-30 deepens C-23: the slot must carry `Feeds tier decision: [Strategy SQ-1 answer]` as a required sub-field — mechanically distinguishing a template that mentions SQ-1 from one that structurally captures the SQ-1 answer as a required slot output. C-23 passes when SQ-1 is named as the slot's conceptual source; C-30 requires that source to be a citation field in the template definition. |
| C-25 partial → C-31 | R9 V-01/V-02 scored C-25 PARTIAL ("framing present, mechanical slot not confirmed") — the two-slot structure (`Structural position` + `Contrast:`) exists but the template never declares itself as a two-slot named pair with a cardinality assertion. R9 V-05 has both slots but no `RATIONALE TEMPLATE (2 required slots)` header. The slot pair is present but not declared. | C-31 applies the same cardinality-declaration principle to the TRIAD block. R9 V-05's TRIAD header says "complete enumerable set" but does not state "3 rules" as a verifiable count. A header that declares a count converts a content-completeness check into a header-level assertion. The same gap affects the MOCK-ACCEPTED rationale template: slots exist but cardinality is not declared. |

R9 recommendation for R10: (1) Test cardinality declaration in TRIAD header (C-31 axis) in
isolation — no SQ-1 citation field, no template declaration. (2) Test SQ-1 citation sub-field
(C-30 axis) in isolation — no TRIAD cardinality, no template declaration. (3) Test RATIONALE
TEMPLATE declaration (C-25 fix axis) in isolation — no PHASE GATE, no step labels. (4)
Combine C-30 + C-31 (Strategy-first). (5) Ceiling: add all three to R9 V-05 (Architect-first,
PHASE GATE, step labels, all prior criteria preserved).

---

## Axis-Assignment Plan

| Var | Axis | Source signal | Target | Predicted |
|-----|------|--------------|--------|-----------|
| V-01 | lifecycle-emphasis | R9 V-01 PHASE GATE base. Cardinality declaration added to TRIAD header: "FORBIDDEN OUTPUTS TRIAD (3 rules, all required)". No SQ-1 citation sub-field (C-30 fails). No RATIONALE TEMPLATE declaration (C-25 partial preserved). No step-name anchors (C-28 fails). Role order: Strategy → PM → Arch (C-26 fails). | C-31 | C-31 PASS. C-29 PASS (PHASE GATE preserved). C-30 FAIL. C-28 FAIL. C-26 FAIL. Failure condition: cardinality declared but incorrect count (e.g., "2 rules") — must name exactly "3 rules." |
| V-02 | output-format | R9 V-02 base (step-name anchors, inline distributed TRIAD, Strategy-first). SQ-1 citation sub-field added to Structural position slot: `Feeds tier decision: [...]`. No PHASE GATE (C-29 FAIL). No TRIAD cardinality (C-31 FAIL). No RATIONALE TEMPLATE declaration. | C-30 | C-30 PASS. C-28 PASS (step-name anchors preserved). C-29 FAIL. C-31 FAIL. C-26 FAIL. Failure condition: `Feeds tier decision:` present as instruction/example rather than as a required sub-field in the template definition — C-30 requires the citation field to appear in the template itself, not only in surrounding guidance. |
| V-03 | inertia-framing | Minimal base (Strategy-first, inline TRIAD distributed — no PHASE GATE, no step-name anchors, no SQ-1 citation field). RATIONALE TEMPLATE (2 required slots) declaration added with cardinality assertion on the slot pair. Tests C-25 fix in isolation: does declaring the slot pair with cardinality mechanically close the "confirmatory escape"? | C-25 | C-25 PASS (RATIONALE TEMPLATE (2 required slots) declaration present; slot completeness verifiable at definition site). C-26 FAIL. C-28 FAIL. C-29 FAIL. C-30 FAIL. C-31 FAIL. Failure condition: RATIONALE TEMPLATE declaration present but does not number the slots — a label without a count does not convert the completeness check into a header-level assertion. |
| V-04 | lifecycle-emphasis + output-format | C-30 + C-31 combined. PHASE GATE (C-29 PASS) with TRIAD header "(3 rules, all required)" (C-31 PASS) + `Feeds tier decision:` sub-field (C-30 PASS) + RATIONALE TEMPLATE declaration (C-25 PASS). Step-name anchors (C-28 PASS). Role order: Strategy → PM → Arch (C-26 FAIL). | C-30, C-31 | C-30 PASS, C-31 PASS, C-25 PASS, C-28 PASS, C-29 PASS. C-26 FAIL (no Architect-first). Confirms C-30 and C-31 are structurally independent of role sequence. |
| V-05 | role-sequence + lifecycle-emphasis + output-format | Ceiling: R9 V-05 (Architect-first + PHASE GATE + step-name anchors + all prior) + TRIAD cardinality (C-31) + SQ-1 citation sub-field (C-30) + RATIONALE TEMPLATE declaration (C-25 fix). All R9 V-05 criteria preserved including SQ answer driving verdict, artifact state propagation, canary-false-positive prohibition. | C-30, C-31 + all prior | C-26 PASS, C-27 PASS, C-28 PASS, C-29 PASS, C-30 PASS, C-31 PASS, C-25 PASS; all essential and recommended preserved. Full criterion set satisfied. |

---

## V-01 — Lifecycle Emphasis (TRIAD cardinality declaration; C-31 axis)

**axis:** lifecycle-emphasis
**hypothesis:** Adding "(3 rules, all required)" to the FORBIDDEN OUTPUTS TRIAD block header
converts the completeness check from a content scan into a header-level assertion, satisfying
C-31 independently of SQ-1 citation field or RATIONALE TEMPLATE declaration. Role order:
Strategy → PM → Arch (C-26 fails). No SQ-1 citation sub-field (C-30 fails). No step-name
anchors (C-28 fails). Expected: C-31 PASS; C-29 PASS (PHASE GATE preserved); C-30 FAIL;
C-28 FAIL; C-26 FAIL.

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

Artifact state citation grammar: Present-tense, artifact as grammatical subject, observable
state as object. Verdict echo (role as subject) is the named error VERDICT-ECHO — DO NOT USE.
  Correct: "Section 3.2 lists no fallback path."
  Verdict echo (error): "Architect found no fallback path."

MOCK-ACCEPTED template (requires all three verdicts positive):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)
  Structural position (Strategy SQ-1 tier decision): [Name the specific Tier {tier}
    decision from Strategy SQ-1. Classify: STRUCTURAL-FORM (structural mock sufficient;
    no tier-boundary validation required) or TIER-GATING (real evidence required).
    Generic adequacy statement without SQ-1 decision name = SLOT VIOLATION.]
  Contrast: [Name a namespace type that WOULD require real evidence and name the structural
    factor it has that this namespace does not. Must name BOTH a namespace type AND the
    distinguishing structural factor.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [full verdict string]
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

## V-02 — Output Format (SQ-1 citation sub-field; C-30 axis)

**axis:** output-format
**hypothesis:** Adding a `Feeds tier decision:` sub-field inside the Structural position slot
— capturing the Strategy SQ-1 answer as a named citation field within the template definition
itself — satisfies C-30 independently of TRIAD placement or role sequence. TRIAD stays inline
in rule bodies (distributed; C-29 fails). No TRIAD cardinality declaration (C-31 fails). No
RATIONALE TEMPLATE cardinality declaration (C-25 partial preserved). Step-name anchors in all
inter-step gates (C-28 PASS). Role order: Strategy → PM → Arch (C-26 fails). Expected:
C-30 PASS; C-28 PASS; C-29 FAIL; C-31 FAIL; C-26 FAIL.

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
      verbatim — this is the specific decision this namespace supports. Generic adequacy
      statement without this citation = SLOT VIOLATION. Example of SLOT VIOLATION:
      "this namespace has limited scope." Example of valid field: "Tier 1 scope gate:
      whether {topic} requires trace-level signal before proceeding."]
    Classify: STRUCTURAL-FORM (structural mock sufficient; no tier-boundary validation
      required) or TIER-GATING (real evidence required; decision depends on live system
      state at tier boundaries).
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

  Priority 1 — Critical REAL-REQUIRED: trace-* first, then scout-feasibility, then listen-*
  Priority 2 — Non-critical REAL-REQUIRED
  Priority 3 — Evidence-heavy REAL-REQUIRED: trigger: EVIDENCE-HEAVY
  Cross-namespace risk statement: "Highest-risk gap: {namespace} — {decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place. Replace every Status field.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [code]  OR  Status: REAL-REQUIRED [trigger]

Canary Confirmation — output protocol:
  DO NOT write "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed." unless
  the condition is verified. Writing it unverified is the named error CANARY-FALSE-POSITIVE.
  If any field not updated: suppress canary; output CANARY SUPPRESSED with namespace list.

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-03 — Inertia Framing (RATIONALE TEMPLATE declaration; C-25 axis)

**axis:** inertia-framing
**hypothesis:** Explicitly declaring the MOCK-ACCEPTED rationale template as "RATIONALE
TEMPLATE (2 required slots)" with numbered slot labels — making slot completeness verifiable
at the definition site — satisfies C-25 independently of TRIAD cardinality or SQ-1 citation
field. The declaration makes the inertia structure mechanically enforceable at the template
level: the author must produce both a Structural position and a Contrast to fill the declared
pair; a single filled slot is structurally visible as incomplete. Base: Strategy-first, inline
TRIAD distributed in rule bodies (C-29 FAIL), no step-name anchors (C-28 FAIL), no PHASE
GATE. No `Feeds tier decision:` sub-field (C-30 FAIL). No TRIAD cardinality (C-31 FAIL).
Expected: C-25 PASS; C-26 FAIL; C-28 FAIL; C-29 FAIL; C-30 FAIL; C-31 FAIL.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. This is the starting position — not a
  finding, not a judgment. MOCK-ACCEPTED is an earned escape from the default.
  The inertia structure requires a positive argument: a namespace earns MOCK-ACCEPTED
  only when all three role evaluations actively confirm it demonstrates what is required.
  Confirmation that nothing is wrong is not a positive argument. REAL-REQUIRED is the
  null result; MOCK-ACCEPTED requires affirmative demonstration.

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

Artifact state citation grammar: Present-tense, artifact as grammatical subject.
Verdict echo (role as subject) is the named error VERDICT-ECHO — DO NOT USE.
  Correct: "Section 3.2 lists no fallback path."
  Verdict echo (error): "Architect found no fallback path."

MOCK-ACCEPTED template (requires all three verdicts positive):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  RATIONALE TEMPLATE (2 required slots — both must be populated; one slot does not satisfy):
  (1) Structural position (Strategy SQ-1 tier decision): [Name the specific Tier {tier}
    decision from Strategy SQ-1 that this namespace supports. Classify: STRUCTURAL-FORM
    (structural mock sufficient) or TIER-GATING (real evidence required). A generic adequacy
    statement without the named SQ-1 decision = SLOT VIOLATION.]
  (2) Contrast: [Name a namespace type that WOULD require real evidence and name the
    structural factor it has that this namespace does not. Must name BOTH a namespace type
    AND the distinguishing structural factor. A confirmatory sentence that does not name
    a contrasting namespace type = SLOT VIOLATION.]

  Slot completeness check: both slot (1) and slot (2) must be written. A template with only
  one slot populated does not satisfy this rationale requirement and is a RATIONALE INCOMPLETE
  error — the MOCK-ACCEPTED decision is void until both slots are filled.

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
DO NOT proceed to STEP 7 until every namespace has a completed decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Next Steps — fill all four sections; write "(none)" if empty; do not reorder.
  Ordering rule stated explicitly: "Critical namespaces first (trace, scout-feasibility,
  listen), evidence-heavy last."

  Priority 1 — Critical REAL-REQUIRED | Priority 2 — Non-critical REAL-REQUIRED
  Priority 3 — Evidence-heavy REAL-REQUIRED | Cross-namespace risk statement

DO NOT proceed to STEP 8 until review artifact is written and confirmed.

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

## V-04 — Lifecycle Emphasis + Output Format (C-30 + C-31 combined; Strategy-first)

**axis:** lifecycle-emphasis + output-format
**hypothesis:** C-30 (SQ-1 citation sub-field in Structural position), C-31 (cardinality
declaration in TRIAD header), and C-25 fix (RATIONALE TEMPLATE numbered declaration) can
all be achieved together before introducing the role-sequence change. PHASE GATE (C-29 PASS).
Step-name anchors (C-28 PASS). Role order: Strategy → PM → Arch (C-26 FAIL). Tests whether
the three template structural changes are independent of role ordering. Expected: C-30 PASS;
C-31 PASS; C-25 PASS; C-28 PASS; C-29 PASS; C-26 FAIL; all prior criteria preserved.

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

Artifact state citation grammar: Present-tense, artifact as grammatical subject.
Verdict echo (role as subject) is the named error VERDICT-ECHO — DO NOT USE.

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
  Artifact state: [Present-tense — artifact as subject.]

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
    Evaluation-driven: /{skill-id} {topic} — {Artifact state from STEP 6 decision block}
    Auto-flagged:      /{skill-id} {topic} — trigger: {trigger value}
  Priority 2 — Non-critical REAL-REQUIRED: same entry formats as Priority 1.
  Priority 3 — Evidence-heavy REAL-REQUIRED: /{skill-id} {topic} — trigger: EVIDENCE-HEAVY
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

## V-05 — Full Integration (C-30 + C-31 + C-25 fix + all R9 V-05 criteria; Architect-first)

**axis:** role-sequence + lifecycle-emphasis + output-format
**hypothesis:** Adding TRIAD cardinality declaration (C-31), SQ-1 citation sub-field (C-30),
and RATIONALE TEMPLATE numbered declaration (C-25 fix) to the R9 V-05 ceiling design achieves
the full v10 criterion set. The PHASE GATE + TRIAD at gate (C-29) preserves the decoupling
between C-26 (role ordering) and C-27 (enumerable triad). Architect-first + cross-step guard
naming `architect-verdict = CONTRADICTS-ARCHITECTURE` and PM Evaluation as the suppressed step
(C-26). Step-name anchors in all inter-step gates (C-28). All R9 V-05 criteria preserved:
DEFAULT DECISION POSITION, entity-naming SQ grammar, VERDICT-ECHO named error, SQ answer
driving verdict field, artifact state propagation in next-steps, canary prohibition. Expected:
C-25 PASS, C-26 PASS, C-27 PASS, C-28 PASS, C-29 PASS, C-30 PASS, C-31 PASS; all prior
criteria preserved.

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

DO NOT proceed to STEP 4 (Strategy Evaluation) until Architect verdicts and cross-step guard
assignments are complete for all remaining namespaces.

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
  SQ answer driving verdict: [present-tense artifact-state form — artifact as subject;
    names the specific sub-question answer that drove the failing verdict; not a restatement]
  Artifact state: [present-tense artifact-state — artifact as subject]

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
    Evaluation-driven: /{skill-id} {topic} — {Artifact state from STEP 6 decision block}
    Auto-flagged:      /{skill-id} {topic} — trigger: {trigger value}
    An evaluation-driven entry that omits the Artifact state is a traceability break.

  Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    Same entry formats as Priority 1.

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
