---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 9
rubric_version: v9
status: VARIATE
---

# mock-review Variate — Round 9

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v9 (C-01 through C-29; aspirational denominator = 21)
**Round:** R9 — targeting v9 new criteria: C-28, C-29

---

## What R8 Left Open

R8 V-05 (the ceiling) attempted C-26 (Architect-first) and C-27 (enumerable triad) but the
scoring revealed two residual gaps that drive C-28/C-29:

| Criterion | R8 ceiling coverage | Gap |
|-----------|---------------------|-----|
| C-18 partial → C-28 | All R8 variants hit the same C-18 partial for the same reason: forward reference gates named a step number ("DO NOT proceed to STEP 5 until...") but not the step's descriptive label. "STEP 5" requires counting from the current position to resolve; "STEP 5 (PM Evaluation)" resolves in place. Every R8 variant carried this gap — it appeared as a consistent partial, not a variant-specific miss. | C-28 deepens C-18: the forward reference must carry both step number AND descriptive label. The label is the structural property; "Step N" alone is the gap. |
| C-26/C-27 mutual exclusivity | V-01 passes C-26 (Architect-first + named cross-step guard naming `architect-verdict = CONTRADICTS-ARCHITECTURE`) but fails C-27. V-02 and V-03 pass C-27 (enumerable triad block) but fail C-26 (Strategy-first, no cross-step guard). V-05 attempted both: Architect-first ordering was present, and a TRIAD block was placed after RULE 3 in STEP 2. However, the mutual exclusivity held. The structural cause: the TRIAD block was not positioned at a named PHASE GATE element — it was appended to the auto-flag step without the gate being a first-class structural component. When the triad is distributed or attached inline to the step rather than to an explicit gate, verifying C-27 requires scanning the step rather than scanning the gate. This ties C-27 verification to structural position within a step, creating implicit coupling to C-26's ordering constraint. | C-29 names the unlock: a FORBIDDEN OUTPUTS TRIAD block co-located at an explicit PHASE GATE element that separates automatic rules from role evaluation decouples C-27 from role ordering. The gate is a named structural boundary — not a prose separator at the end of a step. The TRIAD sits at the gate, not inside a step. Any role sequence satisfies C-27 at the gate scan; Architect-first is free to satisfy C-26 without constraint. No R8 variate had this structural design. |

R8 recommendation for R9: (1) Test explicit PHASE GATE section with TRIAD block at the gate
(C-29 axis) in isolation — no role sequence change, no step-name anchors. (2) Test step-name
anchors (C-28 axis) in isolation — no PHASE GATE, no role sequence change. (3) Test
Architect-first in isolation (reproduce R8 V-01 baseline to confirm C-26 still passes without
C-29). (4) Combine C-28 + C-29, Strategy-first. (5) Ceiling: C-28 + C-29 + Architect-first —
confirm that co-located TRIAD enables C-26 + C-27 + C-28 + C-29 simultaneously.

---

## Axis-Assignment Plan

| Var | Axis | Source signal | Target | Predicted |
|-----|------|--------------|--------|-----------|
| V-01 | lifecycle-emphasis | R8: PHASE GATE concept absent; TRIAD either inline in rule bodies (V-01/V-03) or at end of STEP 2 as appended block (V-02/V-05). V-01 R9 adds an explicit named PHASE GATE section between STEP 2 and first role step. TRIAD block positioned at the gate. Role order: Strategy → PM → Architect (C-26 fails). Forward refs: step numbers only, no labels (C-28 fails). | C-29 | C-29 PASS (TRIAD at named PHASE GATE, one-scan completeness, independent of role order). C-26 FAIL (no Architect-first). C-28 FAIL (no labels). Failure condition: PHASE GATE present but TRIAD placed inside first role step rather than at the gate boundary — C-29 requires immediate adjacency to the gate, not position within a role step. |
| V-02 | lifecycle-emphasis (gate labels) | R8 C-18 partial: every variant uses "DO NOT proceed to STEP N+1 until..." without labels. V-02 R9 adds descriptive labels to every forward reference: "DO NOT proceed to STEP N+1 (Step Name) until...". Role order: Strategy → PM → Architect. TRIAD stays inline in rule bodies (distributed; C-29 fails). | C-28 | C-28 PASS (all inter-step gate forward references carry step number + label). C-29 FAIL (no PHASE GATE; distributed TRIAD). C-26 FAIL (Strategy-first). Failure condition: labels present in some gates but not all — C-28 requires all inter-step gates to carry labels. A single unlabeled gate fails the criterion. |
| V-03 | role-sequence | R8 V-01 had Architect-first + named cross-step guard for C-26, no TRIAD block. V-03 R9 reproduces this design to confirm C-26 still passes in isolation and to document the unresolved C-26/C-27 coupling. No PHASE GATE section; TRIAD distributed inline in rule bodies. No step-name anchors. | C-26 (isolated) | C-26 PASS (Architect-first; guard names `architect-verdict = CONTRADICTS-ARCHITECTURE` as trigger and PM Evaluation as suppressed step). C-27 FAIL (inline distributed DO NOTs satisfy C-11 but are not an enumerable one-scan set). C-29 FAIL. C-28 FAIL. Confirms the R8 V-01 baseline; makes the C-26/C-27 isolation explicit. |
| V-04 | lifecycle-emphasis + output-format | C-28 + C-29 combined. PHASE GATE with TRIAD (C-29). Step-name anchors in all gates (C-28). Role order: Strategy → PM → Architect (C-26 fails — no Architect-first guard). Tests whether both new criteria can be achieved together before introducing the role-sequence change. | C-28, C-29 | C-28 PASS, C-29 PASS. C-26 FAIL (no Architect-first). C-27 PASS via C-29 mechanism. Confirms the two new criteria are structurally independent of role sequence: C-29 co-location works regardless of which role runs first; C-28 step labels work regardless of TRIAD position. |
| V-05 | role-sequence + lifecycle-emphasis + output-format | Ceiling: V-03 Architect-first + C-26 named guard + V-01 PHASE GATE with TRIAD + V-02 step-name anchors. All R8 V-05 criteria preserved: DEFAULT DECISION POSITION, entity-naming SQ grammar, trigger field notation, two-slot MOCK-ACCEPTED template (Structural position + Contrast), artifact state citation grammar, canary with prohibition. | C-26, C-28, C-29 + all prior | C-26 PASS, C-28 PASS, C-29 PASS, C-27 PASS (TRIAD at gate is C-29's mechanism). The R8 mutual exclusivity between C-26 and C-27 is resolved: TRIAD sits at the PHASE GATE, independent of role order, so Architect-first satisfies C-26 without disturbing C-27 verification. Failure condition: cross-step guard at Architect boundary conflates with the PHASE GATE contamination guard — these are distinct structures and must not collapse. |

---

## V-01 — Lifecycle Emphasis (PHASE GATE with TRIAD at gate boundary)

**axis:** lifecycle-emphasis
**hypothesis:** An explicit named PHASE GATE section between STEP 2 (AUTO-FLAG) and the first
role evaluation step places the FORBIDDEN OUTPUTS TRIAD at the gate boundary as a first-class
structural element rather than an appended block inside a step. This satisfies C-29 independent
of role sequence. Role order: Strategy → PM → Architect (C-26 fails). Forward references carry
step numbers only, no descriptive labels (C-28 fails). Expected: C-29 PASS; C-26 FAIL; C-28 FAIL.

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

FORBIDDEN OUTPUTS TRIAD (complete enumerable set — verified at this gate):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all three labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE]
  must be present at this gate. A two-of-three set does not satisfy this gate requirement.

AUTO-RULE CONTAMINATION GUARD:
  Applying evaluation to any auto-flagged namespace is the named error AUTO-RULE
  CONTAMINATION. The automatic decision stands unconditionally. Any evaluation verdict
  applied to an auto-flagged namespace is void.

DO NOT proceed to STEP 3 until:
  — two-list partition is confirmed
  — FORBIDDEN OUTPUTS TRIAD is verified complete at this gate

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
        position (or: "No gap — namespace positively demonstrates coverage adequacy").

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
state as object. Verdict echo (role as subject) is a named error — DO NOT USE.
  Correct: "Section 3.2 lists no fallback path."
  Verdict echo (error): "Architect found no fallback path."

MOCK-ACCEPTED template (requires all three verdicts positive):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)
  Structural position (Strategy SQ-1 tier decision): [Name the specific Tier {tier}
    decision from SQ-1. Classify: STRUCTURAL-FORM decision (structural mock sufficient)
    or TIER-GATING decision (real evidence required). Generic adequacy statement = SLOT VIOLATION.]
  Contrast: [Name a namespace type that WOULD require real evidence and name the structural
    factor it has that this namespace does not. Must name BOTH a namespace type AND the
    distinguishing structural factor.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS-ARCHITECTURE | INSUFFICIENT FOR TIER N]
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

## V-02 — Lifecycle Emphasis / Gate Labels (C-28 axis: step-name anchors in all forward references)

**axis:** lifecycle-emphasis (gate label depth)
**hypothesis:** Adding a descriptive label to every inter-step forward reference gate —
"DO NOT proceed to STEP N+1 (Step Name) until..." — satisfies C-28 independently of TRIAD
placement or role sequence. TRIAD stays inline in rule bodies (distributed; C-29 fails).
Role order: Strategy → PM → Architect (C-26 fails). Expected: C-28 PASS; C-29 FAIL; C-26 FAIL.

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

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
  Structural position (Strategy SQ-1 tier decision): [Name the Tier {tier} decision from
    SQ-1. Classify: STRUCTURAL-FORM or TIER-GATING. Generic adequacy = SLOT VIOLATION.]
  Contrast: [Name a namespace type that WOULD require real evidence and the structural
    factor it has that this namespace does not — both required.]

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
  Ordering rule stated explicitly: "Critical namespaces first, evidence-heavy last."

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

## V-03 — Role Sequence (Architect-first, C-26 isolated; no PHASE GATE, no step labels)

**axis:** role-sequence
**hypothesis:** Reproduces R8 V-01's Architect-first design to confirm C-26 still passes in
isolation. No PHASE GATE section; TRIAD inline in rule bodies (distributed; C-29 fails).
Forward references carry step numbers only (C-28 fails). Cross-step guard at Architect
boundary names `architect-verdict = CONTRADICTS-ARCHITECTURE` as trigger and PM Evaluation
as the suppressed step. Expected: C-26 PASS; C-27 FAIL (distributed, not enumerable set);
C-29 FAIL; C-28 FAIL. Documents R8 mutual exclusivity baseline for R9 contrast.

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
  content depth, or any evaluation outcome.

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

DO NOT apply Architect, Strategy, or PM evaluation to any auto-flagged namespace.
Applying role evaluation to an auto-flagged namespace is the named error AUTO-RULE
CONTAMINATION. The automatic decision stands unconditionally.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting evaluation — default: REAL-REQUIRED): [{namespace}: Category = {value}]

DO NOT proceed to STEP 3 until every namespace is placed in exactly one list.

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

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

CROSS-STEP GUARD — Architect to PM:
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
    Strategy Evaluation (STEP 4) may still run for coverage gap synthesis.
  Record the cross-step guard lists:
    Blocked from PM (architect-verdict = CONTRADICTS-ARCHITECTURE): [{namespace list}]
    Proceeding to PM (architect-verdict = CONSISTENT-WITH-ARCHITECTURE): [{namespace list}]

  Note: this guard is distinct from the AUTO-RULE CONTAMINATION GUARD in STEP 2. The
  contamination guard blocks evaluation of auto-flagged namespaces. This cross-step guard
  fires on a specific architect verdict value and blocks a specific downstream role step.
  DO NOT conflate these two guards.

DO NOT proceed to STEP 4 until Architect verdicts and cross-step guard assignments are complete.

---

STEP 4 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace (including cross-step-blocked — for coverage gap synthesis),
answer sub-questions then write the Strategy verdict.
Evaluation question: does this namespace positively demonstrate coverage adequacy for
Tier {tier}? Sub-questions require named artifacts — not yes/no answers.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates coverage adequacy").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 until Strategy verdicts are written for every remaining namespace.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces where architect-verdict =
CONSISTENT-WITH-ARCHITECTURE. Namespaces on the cross-step-blocked list DO NOT proceed
to PM evaluation — their decision is already determined. Applying PM evaluation to a
cross-step-blocked namespace is the named error GUARD-BYPASS CONTAMINATION.

For each qualifying namespace, answer sub-questions then write the PM verdict.
Evaluation question: does this namespace positively demonstrate structural completeness?
Sub-questions require named artifacts — not yes/no answers.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        (or: "No gap — namespace positively demonstrates structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL qualifying namespaces.
DO NOT proceed to STEP 6 until PM verdicts are written for every qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field notation: `trigger` at fixed position. Values from enumeration only:
  Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED: n/a

Artifact state citation grammar: Present-tense, artifact as grammatical subject.
Verdict echo (role as subject) is the named error VERDICT-ECHO — DO NOT USE.

MOCK-ACCEPTED template (requires all three verdicts positive; PM-qualified namespaces only):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
  Structural position (Strategy SQ-1 tier decision): [Name Tier {tier} decision from SQ-1.
    Classify: STRUCTURAL-FORM or TIER-GATING. Generic adequacy statement = SLOT VIOLATION.]
  Contrast: [Name a namespace type that WOULD require real evidence and the structural
    factor it has that this namespace does not — both required.]

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
DO NOT proceed to STEP 7 until every namespace has a completed decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Next Steps — Ordering rule: "Critical namespaces first, evidence-heavy last."
  Priority 1 — Critical REAL-REQUIRED | Priority 2 — Non-critical REAL-REQUIRED
  Priority 3 — Evidence-heavy REAL-REQUIRED | Cross-namespace risk statement

DO NOT proceed to STEP 8 until review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place. Replace every Status field.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [code]  OR  Status: REAL-REQUIRED [trigger]

Canary Confirmation: DO NOT write the confirmation line unless zero Status fields remain
MOCK. Writing it unverified is CANARY-FALSE-POSITIVE. Suppress and list unupdated
namespaces if any field was not updated. Re-verify. Write canary only when condition is met.

Full confirmation block (canary condition verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-04 — Lifecycle Emphasis + Output Format (C-28 + C-29 combined; Strategy-first)

**axis:** lifecycle-emphasis + output-format
**hypothesis:** C-28 (step-name anchors) and C-29 (PHASE GATE with TRIAD) can be achieved
together before introducing the role-sequence change. Role order: Strategy → PM → Architect
(C-26 fails). Both new criteria are structurally independent of role ordering: C-29 co-location
is verified at the gate regardless of which role runs first; C-28 labels are a gate property
independent of TRIAD position. Expected: C-28 PASS; C-29 PASS; C-26 FAIL; C-27 PASS (via C-29).

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

FORBIDDEN OUTPUTS TRIAD (complete enumerable set — verified at this gate):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all three labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE]
  must be present at this gate. A two-of-three set does not satisfy this gate requirement.
  This block is the single verification point for triad completeness — independent of
  which role step runs first.

AUTO-RULE CONTAMINATION GUARD:
  Applying evaluation to any auto-flagged namespace is the named error AUTO-RULE
  CONTAMINATION. The automatic decision stands unconditionally.
  DO NOT apply evaluation to auto-flagged namespaces.

DO NOT proceed to STEP 3 (Strategy Evaluation) until:
  — two-list partition is confirmed
  — FORBIDDEN OUTPUTS TRIAD is verified complete at this gate

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

Trigger field notation: `trigger` at fixed position. Values from enumeration only:
  Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED: n/a

Artifact state citation grammar: Present-tense, artifact as grammatical subject.
Verdict echo (role as subject) is the named error VERDICT-ECHO — DO NOT USE.

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
  Structural position (Strategy SQ-1 tier decision): [Name Tier {tier} decision from SQ-1.
    Classify: STRUCTURAL-FORM or TIER-GATING. Generic adequacy statement = SLOT VIOLATION.]
  Contrast: [Name a namespace type that WOULD require real evidence and the structural
    factor it has that this namespace does not — both required.]

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

  Next Steps — Ordering rule stated explicitly: "Critical namespaces first, evidence-heavy last."
  Priority 1 — Critical REAL-REQUIRED | Priority 2 — Non-critical REAL-REQUIRED
  Priority 3 — Evidence-heavy REAL-REQUIRED | Cross-namespace risk statement

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

## V-05 — Full Integration (C-26 + C-28 + C-29; Architect-first + PHASE GATE + step labels)

**axis:** role-sequence + lifecycle-emphasis + output-format
**hypothesis:** Co-locating the FORBIDDEN OUTPUTS TRIAD at the PHASE GATE (C-29) decouples
C-27 from role ordering, enabling Architect-first (C-26) and enumerable triad (C-27)
simultaneously — the R8 mutual exclusivity resolved. Step-name anchors (C-28) applied to all
inter-step gates including the cross-step guard. All R8 V-05 criteria preserved. Expected:
C-26 PASS, C-27 PASS, C-28 PASS, C-29 PASS; all prior criteria preserved.

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

FORBIDDEN OUTPUTS TRIAD (complete enumerable set — single verification point at this gate,
independent of role sequence):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all three labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE]
  must be present. A two-of-three set does not satisfy this gate requirement.
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
  — FORBIDDEN OUTPUTS TRIAD is verified complete at this gate

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
  Structural position (Strategy SQ-1 tier decision): [Name the specific Tier {tier}
    decision from Strategy SQ-1. Classify as STRUCTURAL-FORM (structural mock sufficient;
    no tier-boundary validation required) or TIER-GATING (real evidence required; decision
    depends on live system state at tier boundaries). The slot requires the SQ-1 decision
    name AND the type classification. A generic adequacy statement is a SLOT VIOLATION.]
  Contrast: [Name a namespace type that WOULD require real evidence and state the
    structural factor it has that this namespace does not. Must name BOTH a namespace
    type AND the distinguishing structural factor. Form: "Unlike {namespace type}, which
    carries {structural factor} that requires real evidence because {reason}, this namespace's
    outputs are fully determined by {structural form property}."]

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
