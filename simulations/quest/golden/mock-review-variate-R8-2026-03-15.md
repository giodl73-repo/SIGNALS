---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 8
rubric_version: v8
status: VARIATE
---

# mock-review Variate — Round 8

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v8 (C-01 through C-27; aspirational denominator = 19)
**Round:** R8 — targeting v8 new criteria: C-26, C-27

---

## What R7 Left Open

R7 V-05 (the ceiling) closed C-25 by adding a structurally separate `Contrast:` sub-slot to
the MOCK-ACCEPTED template, making it mechanically impossible to satisfy the rationale with a
confirmatory sentence alone. Two new patterns surface in R7's scorecard and drive C-26/C-27:

| Criterion | R7 V-05 coverage | Gap |
|-----------|-----------------|-----|
| C-26 Role-sequence gate as contamination control | R7 V-05 uses Strategy → PM → Architect ordering. Architect runs last; no cross-step guard is possible because PM has already evaluated all namespaces before Architect runs. A guard at the Architect boundary cannot suppress PM because PM is complete. | Requires Architect-first ordering. The guard must name `architect-verdict = CONTRADICTS-ARCHITECTURE` as the trigger and PM evaluation as the suppressed step. Ordering change from Strategy-first to Architect-first conflicts with C-23 (Strategy SQ-1 must be available before MOCK-ACCEPTED decision is written) unless Strategy runs between Architect and PM: Architect → Strategy → PM. |
| C-27 Triad DO NOT coverage | R7 V-05 has per-rule DO NOT statements inline in each rule's body. These pass C-11 (three rules carry forbidden-output statements) but are distributed across three rule blocks. A mechanical verifier must scan each block individually; there is no one-scan completeness check. | C-27 requires the three DO NOT statements to form an enumerable, mechanically verifiable set — either a dedicated FORBIDDEN OUTPUTS TRIAD section or per-rule `forbidden-output:` field notation (fixed position within each rule block). The inline prose form fails the "enumerable set" requirement. |

R7 recommendation for R8: (1) Test Architect → Strategy → PM ordering with named cross-step
guard for C-26. Verify C-23 is preserved (Strategy runs before STEP 6 decisions). (2) Test
two structural mechanisms for C-27: dedicated TRIAD section (one-scan completeness) vs.
per-rule `forbidden-output:` field notation (distributed but labeled). (3) Combine both in
ceiling variation.

---

## Axis-Assignment Plan

| Var | Axis | Source signal | Target | Predicted |
|-----|------|--------------|--------|-----------|
| V-01 | role-sequence | R7 V-05 fails C-26 by placing Architect last. Reorder to Architect → Strategy → PM. Cross-step guard at Architect boundary names `architect-verdict = CONTRADICTS-ARCHITECTURE` and suppresses PM (STEP 5). Strategy still runs for all remaining namespaces — C-23 preserved. | C-26 | C-26 PASS (guard names verdict value + downstream step). C-23 preserved. C-27 FAIL (no triad section). Failure condition: guard fires but names role boundary rather than verdict value ("after Architect, before PM" without `architect-verdict = CONTRADICTS-ARCHITECTURE`). |
| V-02 | output-format | R7 V-05 inline DO NOT statements pass C-11 but are not an enumerable set. V-02 adds a dedicated FORBIDDEN OUTPUTS TRIAD block after RULE 3 in STEP 2: three labeled entries collected in one location. Individual per-rule DO NOT statements retained. Strategy-first ordering preserved. | C-27 | C-27 PASS (triad block with three labeled entries in one scannable location). C-26 FAIL (Strategy-first). Failure condition: triad block is present but individual per-rule DO NOT statements are removed — C-11 degrades if the inline statements are the C-11 evidence and the triad section replaces rather than supplements them. |
| V-03 | phrasing-register | V-02 uses a dedicated prose triad section. V-03 uses per-rule field notation: `forbidden-output: "DO NOT mark {rule} MOCK-ACCEPTED..."` as a fixed-position labeled field within each rule block, mirroring the `trigger = {value}` convention used in decision blocks. Distributed but labeled and in fixed position. Strategy-first ordering preserved. | C-27 | C-27 PASS (per-rule labeled field in fixed position satisfies "individually labeled"). C-26 FAIL (Strategy-first). Comparison with V-02: V-03 distributed-labeled vs. V-02 one-scan-set — which mechanism better satisfies "mechanically verifiable"? Failure condition: distributed fields satisfy C-27's "individually labeled" but fail "enumerable set" because the set is not co-located. |
| V-04 | role-sequence + lifecycle-emphasis | V-01 Architect-first with C-26 guard + explicit named completion gates at each role step boundary (C-18). Each gate block names the specific next step being blocked: "DO NOT proceed to STEP N+1 (name) until condition." Tests whether C-26 guard + explicit lifecycle gates are mutually reinforcing or independent. | C-26, C-18 | C-26 PASS (Architect-first + named guard). C-18 deepened (each gate names next step explicitly). C-27 FAIL (no triad section). C-23 preserved (Strategy before STEP 6). Failure condition: lifecycle gate at Architect boundary conflates the phase-completion gate with the contamination guard — the guard fires on a verdict value; the gate fires on completion. These are structurally different and should not collapse into one block. |
| V-05 | role-sequence + output-format + lifecycle-emphasis | Ceiling: V-01 Architect-first + C-26 guard + V-02 FORBIDDEN OUTPUTS TRIAD + explicit step gates. All R7 V-05 criteria preserved: DEFAULT DECISION POSITION, labeled SQ-1 slot, explicit eval-driven sub-templates in STEP 7, two-slot MOCK-ACCEPTED template, Artifact state grammar, canary confirmation. The guard and triad are mutually reinforcing: the guard fires on the same verdict values that the triad lists as forbidden outputs. | C-26, C-27 + all prior | C-26 PASS, C-27 PASS. All R7 ceiling criteria preserved. Failure condition: (1) Architect-first ordering breaks C-23 if Strategy SQ-1 answer is not available before STEP 6 — avoided by Architect → Strategy → PM ordering. (2) Triad section and per-rule inline DO NOT statements become redundant and one is dropped — both must be present for C-11 + C-27 simultaneously. |

---

## V-01 — Role Sequence (Architect-first, C-26 cross-step guard)

**axis:** role-sequence
**hypothesis:** R7 V-05 uses Strategy → PM → Architect; Architect runs last, making C-26
impossible. V-01 changes to Architect → Strategy → PM. The cross-step guard at the Architect
boundary names `architect-verdict = CONTRADICTS-ARCHITECTURE` as the trigger and suppresses PM
evaluation for those namespaces. Strategy still runs for all remaining namespaces, so SQ-1 is
available when MOCK-ACCEPTED decisions are written in STEP 6. Expected: C-26 PASS; C-27 FAIL;
C-23 preserved. Failure condition: guard names role boundary ("after Architect") without naming
the verdict value — does not satisfy C-26's verdict-value-trigger requirement.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace in this review begins as REAL-REQUIRED. This is the starting state —
  not a finding, not a judgment. MOCK-ACCEPTED is an earned outcome. A namespace earns
  MOCK-ACCEPTED only when all three role evaluations (Architect, Strategy, PM) actively
  confirm that it positively demonstrates what is required. The evaluation question for
  each role is not "does anything disqualify this namespace?" — it is "does this namespace
  positively demonstrate what is needed?" Absence of disqualification is not positive
  evidence. REAL-REQUIRED is the null result. MOCK-ACCEPTED is the earned result.

---

STEP 1 — READ

Read {mock-artifact-path}.
Extract from each namespace section: namespace name, Category field, current Status field.
Read TOPICS.md. Record: tier for {topic}, compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is optional or role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  mock content depth, or Architect/Strategy/PM evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any Tier 2+ critical namespace MOCK-ACCEPTED. The critical designation
  applies at the structural level and cannot be waived by evaluation quality.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any compliance-tagged namespace MOCK-ACCEPTED when compliance context
  is active. Compliance signals require real evidence; mock artifacts do not produce them.

DO NOT apply Architect, Strategy, or PM evaluation to any auto-flagged namespace.
Applying role evaluation to a namespace already decided by an automatic rule is a named
error: **auto-rule contamination**. This error is detectable by inspection: an auto-flagged
namespace that carries both a trigger label and an evaluation verdict has been contaminated.
The automatic rule verdict stands unconditionally; any evaluation verdict applied to an
auto-flagged namespace is void.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = EVIDENCE-HEAVY
  - {namespace}: trigger = TIER-CRITICAL
  - {namespace}: trigger = COMPLIANCE

  Remaining (awaiting evaluation — default: REAL-REQUIRED):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

DO NOT proceed to STEP 3 until every namespace is placed in exactly one list.

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Architect verdict.
The evaluation question is: does this namespace positively demonstrate technical
plausibility? Each sub-question requires a named artifact in the answer — not a yes/no.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this namespace's escape from its REAL-REQUIRED default position.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

Complete Architect evaluation for ALL remaining namespaces.

CROSS-STEP GUARD — Architect to PM:
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED
    trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM evaluation (STEP 5) to these namespaces.
    Strategy evaluation (STEP 4) may still run for coverage gap synthesis.
  Record the cross-step guard list:
    Blocked from PM: [{namespace list with architect-verdict = CONTRADICTS-ARCHITECTURE}]
    Proceeding to PM: [{namespace list with architect-verdict = CONSISTENT-WITH-ARCHITECTURE}]

DO NOT proceed to STEP 4 until Architect verdicts and cross-step guard assignments are complete.

---

STEP 4 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace (including cross-step-blocked namespaces — for coverage gap
synthesis), answer these sub-questions then write the Strategy verdict.
The evaluation question is: does this namespace positively demonstrate coverage adequacy
for Tier {tier}? Each sub-question requires a named artifact in the answer — not a yes/no.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED
        default position (or: "No gap — namespace positively demonstrates coverage
        adequacy and earns escape from default").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 until Strategy verdicts are written for every remaining namespace.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces where architect-verdict =
CONSISTENT-WITH-ARCHITECTURE. Namespaces on the cross-step-blocked list (architect-verdict =
CONTRADICTS-ARCHITECTURE) DO NOT proceed to PM evaluation — their decision is already
determined. Applying PM evaluation to a cross-step-blocked namespace is a named error:
**guard-bypass contamination**.

For each qualifying namespace, answer these sub-questions then write the PM verdict.
The evaluation question is: does this namespace positively demonstrate structural
completeness? Each sub-question requires a named artifact in the answer — not a yes/no.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED
        default position (or: "No gap — namespace positively demonstrates structural
        completeness and earns escape from default").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL qualifying namespaces.
DO NOT proceed to STEP 6 until PM verdicts are written for every qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION

**Trigger field notation:** The `trigger` field is a named artifact field in a fixed
position — the second line of every REAL-REQUIRED decision block and the third line of
every MOCK-ACCEPTED decision block (where it is `trigger = n/a`). Its value is always
drawn from this enumeration:
  Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED: n/a
The field uses lowercase `trigger` and equals-sign notation (`trigger = {value}`) in all
positions. This is the canonical format.

**Artifact state citation grammar:** The `Artifact state` field requires present-tense
artifact-state form. The artifact (a section, table, field, or element in the mock) is
the grammatical subject. The verb is present tense. The observable state is the object.

  Correct form (artifact as subject, present tense):
    "Section 3.2 lists no fallback path for this namespace."
    "Table Y contains no tier-boundary gate."

  Verdict echo (role as subject) — named error — DO NOT USE:
    "Architect found no fallback path." [subject = role, not artifact]
    "PM evaluation showed the table is absent." [subject = evaluation, not artifact]

  Verdict echo is detectable: the grammatical subject is a role name or evaluation noun
  rather than an artifact name. A verdict echo defeats the traceability purpose of the
  Artifact state field.

For each namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template (only for namespaces with all three verdicts positive):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Structural position (Strategy SQ-1 tier decision): [State the specific Tier {tier}
    decision from Strategy SQ-1 that this namespace supports. Classify it: state whether
    it is a STRUCTURAL-FORM decision (structural mock is sufficient; no tier-boundary
    validation required) or a TIER-GATING decision (real evidence required; mock cannot
    validate because the decision depends on live system state at tier boundaries). The
    slot label names Strategy SQ-1 as the required input and type classification as the
    required output. A general adequacy statement without the SQ-1 decision name and
    type classification is a SLOT-LABEL VIOLATION.]
  Contrast: [Name a namespace type that WOULD require real evidence and state the
    structural factor it has that this namespace does not. Must name BOTH a namespace
    type AND a structural factor. E.g.: "Unlike trace-* namespaces, which carry
    tier-gating decisions that require live architectural evidence because those decisions
    depend on component state at tier transitions, this namespace's outputs are fully
    determined by their structural form."]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS-ARCHITECTURE | INSUFFICIENT FOR TIER N]
  Artifact state: [Present-tense artifact-state form — artifact as grammatical subject,
    present tense, observable state as object. Not verdict echo.]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

Complete all namespace decision templates.
DO NOT proceed to STEP 7 until every namespace has a completed decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md:

  Header: Topic | Tier used | Date

  Coverage Review table:
    | Namespace | Category | Decision | trigger |
    One row per namespace; all namespaces from Steps 2 and 6.

  Next Steps — use this pre-printed skeleton. Fill all four sections. Do not collapse
  or reorder. If a section has no entries, write "(none)" — do not omit.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* namespaces first, then scout-feasibility, then listen-* and scout-competitors.
     TWO required entry formats — select by decision type:
       Evaluation-driven: /{skill-id} {topic} — {Artifact state field from STEP 6 block}
       Auto-flagged:      /{skill-id} {topic} — trigger: {trigger value}
     An evaluation-driven entry that omits the Artifact state field is a traceability break.]

    Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    [All non-critical, non-evidence-heavy REAL-REQUIRED namespaces.
     TWO required entry formats — select by decision type:
       Evaluation-driven: /{skill-id} {topic} — {Artifact state field from STEP 6 block}
       Auto-flagged:      /{skill-id} {topic} — trigger: {trigger value}]

    Priority 3 — Evidence-heavy REAL-REQUIRED (sequence after Priority 1 and 2):
    [All EVIDENCE-HEAVY REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — trigger: EVIDENCE-HEAVY]

    Cross-namespace risk statement:
    [Required output. Name the single highest-risk coverage gap — the REAL-REQUIRED
     namespace whose absence most threatens a Tier {tier} decision. State the specific
     Tier {tier} decision at risk. Assign urgency: BLOCKING | HIGH | MEDIUM.
     Format: "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
     — urgency: {BLOCKING | HIGH | MEDIUM}"]

DO NOT proceed to STEP 8 until the review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

MUST update every Status line in {mock-artifact-path}.
Use Edit tool. In-place replacement only. Do not rewrite any other content.

For each namespace:
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  OR:      Status: REAL-REQUIRED [{trigger value from canonical field}]

After completing all edits, verify before confirming.

**Canary Confirmation — output protocol:**

The following line is a CANARY OUTPUT:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

This line is an assertion that the stated condition is true. Writing this line when any
Status field remains as MOCK (awaiting review) is a protocol error named CANARY-FALSE-POSITIVE.

Protocol:
  - Write the canary ONLY after confirming that zero Status fields remain as MOCK.
  - If any Status field was not updated: suppress the canary. Output instead:
      "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"
    Attempt the remaining edits. Re-verify. Then write the canary when condition is met.

Full confirmation block (only when canary condition is verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

This is the defining action of /mock:review. It is not optional.

---

## V-02 — Output Format (FORBIDDEN OUTPUTS TRIAD as enumerable set, C-27)

**axis:** output-format
**hypothesis:** R7 V-05 has per-rule DO NOT statements inline in each rule's body. A
mechanical verifier must scan three separate rule blocks to confirm all three are present.
V-02 adds a dedicated FORBIDDEN OUTPUTS TRIAD block immediately after RULE 3 in STEP 2,
collecting all three DO NOT statements in one scannable location with labeled identifiers
[1][2][3]. The per-rule inline DO NOT statements are retained (C-11 preserved). The triad
adds one-scan completeness verification. Strategy-first ordering preserved (C-23 strongest
form). Expected: C-27 PASS (labeled enumerable triad). C-26 FAIL (Strategy-first, no
cross-step guard). Failure condition: triad present but inline statements removed — C-11
degrades if the triad was intended to replace rather than supplement the inline DO NOTs.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace in this review begins as REAL-REQUIRED. This is the starting state —
  not a finding, not a judgment. MOCK-ACCEPTED is an earned outcome. A namespace earns
  MOCK-ACCEPTED only when all three role evaluations (Strategy, PM, Architect) actively
  confirm that it positively demonstrates what is required. The evaluation question for
  each role is not "does anything disqualify this namespace?" — it is "does this namespace
  positively demonstrate what is needed?" Absence of disqualification is not positive
  evidence. REAL-REQUIRED is the null result. MOCK-ACCEPTED is the earned result.

---

STEP 1 — READ

Read {mock-artifact-path}.
Extract from each namespace section: namespace name, Category field, current Status field.
Read TOPICS.md. Record: tier for {topic}, compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is optional or role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  mock content depth, or Strategy/PM/Architect evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any Tier 2+ critical namespace MOCK-ACCEPTED. The critical designation
  applies at the structural level and cannot be waived by evaluation quality.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any compliance-tagged namespace MOCK-ACCEPTED when compliance context
  is active. Compliance signals require real evidence; mock artifacts do not produce them.

FORBIDDEN OUTPUTS TRIAD (complete enumerable set — mechanically verifiable):
  [1] EVIDENCE-HEAVY: DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
      of mock quality, structural depth, or any evaluation outcome.
  [2] TIER-CRITICAL: DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
      of mock quality, structural depth, or any evaluation outcome.
  [3] COMPLIANCE: DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
      of mock quality, structural depth, or any evaluation outcome.
  Verification: all three labels [1][2][3] must appear. A skill that carries [1] and [2]
  but not [3] — or any other two-of-three combination — does not satisfy this triad.

DO NOT apply Strategy, PM, or Architect evaluation to any auto-flagged namespace.
Applying role evaluation to a namespace already decided by an automatic rule is a named
error: **auto-rule contamination**. This error is detectable by inspection: an auto-flagged
namespace that carries both a trigger label and an evaluation verdict has been contaminated.
The automatic rule verdict stands unconditionally; any evaluation verdict applied to an
auto-flagged namespace is void.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = EVIDENCE-HEAVY
  - {namespace}: trigger = TIER-CRITICAL
  - {namespace}: trigger = COMPLIANCE

  Remaining (awaiting evaluation — default: REAL-REQUIRED):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

DO NOT proceed to STEP 3 until every namespace is placed in exactly one list.

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Strategy verdict.
The evaluation question is: does this namespace positively demonstrate coverage adequacy
for Tier {tier}? Each sub-question requires a named artifact in the answer — not a yes/no.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED
        default position (or: "No gap — namespace positively demonstrates coverage
        adequacy and earns escape from default").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 4 until Strategy verdicts are written for every remaining namespace.

---

STEP 4 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the PM verdict.
The evaluation question is: does this namespace positively demonstrate structural
completeness? Each sub-question requires a named artifact in the answer — not a yes/no.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED
        default position (or: "No gap — namespace positively demonstrates structural
        completeness and earns escape from default").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 until PM verdicts are written for every remaining namespace.

---

STEP 5 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Architect verdict.
The evaluation question is: does this namespace positively demonstrate technical
plausibility? Each sub-question requires a named artifact in the answer — not a yes/no.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this namespace's escape from its REAL-REQUIRED default position.

  Architect Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 until Architect verdicts are written for every remaining namespace.

---

STEP 6 — DECISIONS WITH CITATION

**Trigger field notation:** The `trigger` field is a named artifact field in a fixed
position — the second line of every REAL-REQUIRED decision block and the third line of
every MOCK-ACCEPTED decision block (where it is `trigger = n/a`). Its value is always
drawn from this enumeration:
  Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED: n/a
The field uses lowercase `trigger` and equals-sign notation (`trigger = {value}`) in all
positions. This is the canonical format.

**Artifact state citation grammar:** The `Artifact state` field requires present-tense
artifact-state form. The artifact is the grammatical subject. The verb is present tense.
The observable state is the object. Verdict echo (role as grammatical subject) is a named
error. A verdict echo defeats the traceability purpose of the Artifact state field.

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Structural position (Strategy SQ-1 tier decision): [State the specific Tier {tier}
    decision from Strategy SQ-1 that this namespace supports. Classify it as STRUCTURAL-FORM
    or TIER-GATING. The slot label names Strategy SQ-1 as the required input; a general
    adequacy statement without the SQ-1 decision name and type classification is a
    SLOT-LABEL VIOLATION.]
  Contrast: [Name a namespace type that WOULD require real evidence and state the structural
    factor it has that this namespace does not. Must name BOTH a namespace type AND a
    structural factor.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Artifact state: [Present-tense artifact-state form — artifact as grammatical subject.]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

Complete all namespace decision templates.
DO NOT proceed to STEP 7 until every namespace has a completed decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md:

  Header: Topic | Tier used | Date

  Coverage Review table:
    | Namespace | Category | Decision | trigger |

  Next Steps — pre-printed skeleton. Fill all four sections. Write "(none)" for empty sections.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* first, then scout-feasibility, then listen-* and scout-competitors.
     Evaluation-driven: /{skill-id} {topic} — {Artifact state field from STEP 6 block}
     Auto-flagged:      /{skill-id} {topic} — trigger: {trigger value}]

    Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    [Evaluation-driven: /{skill-id} {topic} — {Artifact state field from STEP 6 block}
     Auto-flagged:      /{skill-id} {topic} — trigger: {trigger value}]

    Priority 3 — Evidence-heavy REAL-REQUIRED:
    [/{skill-id} {topic} — trigger: EVIDENCE-HEAVY]

    Cross-namespace risk statement:
    ["Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
     — urgency: {BLOCKING | HIGH | MEDIUM}"]

DO NOT proceed to STEP 8 until the review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

MUST update every Status line in {mock-artifact-path}.
Use Edit tool. In-place replacement only.

For each namespace:
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  OR:      Status: REAL-REQUIRED [{trigger value from canonical field}]

Canary Confirmation — output protocol:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  Write ONLY after verifying zero remain. If any remain: suppress canary, output
  "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}".
  Writing the canary when the condition is not met is protocol error: CANARY-FALSE-POSITIVE.

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-03 — Phrasing Register (per-rule field notation for C-27)

**axis:** phrasing-register
**hypothesis:** V-02 satisfies C-27 via a dedicated TRIAD section (one-scan co-location).
V-03 tests an alternative structural mechanism: per-rule `forbidden-output:` field notation
within each rule block, mirroring the `trigger = {value}` convention already established in
decision blocks. The labeled field in fixed position within each rule block satisfies
C-27's "individually labeled" requirement. The question is whether distributed-but-labeled
fields satisfy "enumerable set" or whether co-location is required. Strategy-first ordering
preserved. Expected: C-27 PASS (labeled field per rule, fixed position). C-26 FAIL.
Comparison with V-02: if V-03 also PASSES C-27, then co-location is not required —
labeled fields in fixed positions are sufficient. Failure condition: distributed fields
satisfy "individually labeled" but fail "enumerable set" (no single-scan completeness
check across all three rules).

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace in this review begins as REAL-REQUIRED. This is the starting state —
  not a finding, not a judgment. MOCK-ACCEPTED is an earned outcome. A namespace earns
  MOCK-ACCEPTED only when all three role evaluations (Strategy, PM, Architect) actively
  confirm that it positively demonstrates what is required. The evaluation question for
  each role is not "does anything disqualify this namespace?" — it is "does this namespace
  positively demonstrate what is needed?" Absence of disqualification is not positive
  evidence. REAL-REQUIRED is the null result. MOCK-ACCEPTED is the earned result.

---

STEP 1 — READ

Read {mock-artifact-path}.
Extract from each namespace section: namespace name, Category field, current Status field.
Read TOPICS.md. Record: tier for {topic}, compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 until all namespace header fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is optional or role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  trigger-condition: Category == EVIDENCE-HEAVY
  decision:          REAL-REQUIRED
  trigger:           EVIDENCE-HEAVY
  forbidden-output:  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                     of mock quality, content depth, or any evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  trigger-condition: tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*,
                     scout-competitors}
  decision:          REAL-REQUIRED
  trigger:           TIER-CRITICAL
  forbidden-output:  DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED. The critical
                     designation applies at the structural level and cannot be waived by
                     evaluation quality.

RULE 3 — COMPLIANCE (when compliance context is active):
  trigger-condition: compliance tags in TOPICS.md OR --compliance flag set AND namespace
                     in {scout-compliance, trace-permissions}
  decision:          REAL-REQUIRED
  trigger:           COMPLIANCE
  forbidden-output:  DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED when
                     compliance context is active. Compliance signals require real evidence.

Each rule carries a `forbidden-output:` field in fixed position (fourth line of the rule
block). The three `forbidden-output:` fields form the complete forbidden-output set for
automatic rules. A rule block missing its `forbidden-output:` field is incomplete.

DO NOT apply Strategy, PM, or Architect evaluation to any auto-flagged namespace.
Applying role evaluation to a namespace already decided by an automatic rule is a named
error: **auto-rule contamination**. The automatic rule verdict stands unconditionally.

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = EVIDENCE-HEAVY
  - {namespace}: trigger = TIER-CRITICAL
  - {namespace}: trigger = COMPLIANCE

  Remaining (awaiting evaluation — default: REAL-REQUIRED):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

DO NOT proceed to STEP 3 until every namespace is placed in exactly one list.

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Strategy verdict.
The evaluation question is: does this namespace positively demonstrate coverage adequacy
for Tier {tier}? Each sub-question requires a named artifact — not a yes/no.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED
        default position (or: "No gap — earns escape from default").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 4 until Strategy verdicts are written for every remaining namespace.

---

STEP 4 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the PM verdict.
The evaluation question is: does this namespace positively demonstrate structural
completeness? Each sub-question requires a named artifact — not a yes/no.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED
        default position (or: "No gap — earns escape from default").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 until PM verdicts are written for every remaining namespace.

---

STEP 5 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Architect verdict.
The evaluation question is: does this namespace positively demonstrate technical
plausibility? Each sub-question requires a named artifact — not a yes/no.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this namespace's escape from its REAL-REQUIRED default position.

  Architect Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 until Architect verdicts are written for every remaining namespace.

---

STEP 6 — DECISIONS WITH CITATION

**Trigger field notation:** `trigger = {value}` in fixed position (second line of
REAL-REQUIRED block; third line of MOCK-ACCEPTED block). Enumeration:
  Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED: n/a

**Artifact state citation grammar:** Artifact as grammatical subject. Present tense.
Observable state as object. Verdict echo (role as subject) is a named error.

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
  Structural position (Strategy SQ-1 tier decision): [SQ-1 decision name + type
    classification: STRUCTURAL-FORM or TIER-GATING. SLOT-LABEL VIOLATION if generic.]
  Contrast: [Namespace type + structural factor that would require real evidence.
    Must name BOTH. Category echo without structural factor is a named error.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Artifact state: [Present-tense, artifact as subject.]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 until every namespace has a completed decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md with Coverage Review table and Next Steps.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED:
    [Evaluation-driven: /{skill-id} {topic} — {Artifact state field}
     Auto-flagged:      /{skill-id} {topic} — trigger: {trigger value}]

    Priority 2 — Non-critical REAL-REQUIRED:
    [Evaluation-driven: /{skill-id} {topic} — {Artifact state field}
     Auto-flagged:      /{skill-id} {topic} — trigger: {trigger value}]

    Priority 3 — Evidence-heavy REAL-REQUIRED:
    [/{skill-id} {topic} — trigger: EVIDENCE-HEAVY]

    Cross-namespace risk statement:
    ["Highest-risk gap: {namespace} — {Tier {tier} decision at risk} — urgency: {level}"]

DO NOT proceed to STEP 8 until the review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit in-place. Update every Status: MOCK (awaiting review) to final decision.
Canary: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
Write only after zero-remaining verified. CANARY-FALSE-POSITIVE if written prematurely.

---

## V-04 — Role Sequence + Lifecycle Emphasis (Architect-first + explicit step gates)

**axis:** role-sequence + lifecycle-emphasis
**hypothesis:** V-01 establishes Architect-first with the C-26 guard but uses terse
inter-step gates ("DO NOT proceed to STEP N+1 until..."). V-04 adds explicit named
completion gates at every role-step boundary — each gate names the specific next step
being blocked and the completion condition required. This tests whether C-26 and C-18
are structurally independent (V-01 already passes C-26; V-04 adds C-18 depth) or whether
the gate structure at the Architect boundary reinforces C-26 by making the guard more
prominent. C-27 not addressed (Strategy-first → Architect ordering; no triad section).
Expected: C-26 PASS; C-18 deepened; C-27 FAIL.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace in this review begins as REAL-REQUIRED. This is the starting state —
  not a finding, not a judgment. MOCK-ACCEPTED is an earned outcome. A namespace earns
  MOCK-ACCEPTED only when all three role evaluations (Architect, Strategy, PM) actively
  confirm that it positively demonstrates what is required. REAL-REQUIRED is the null result.
  MOCK-ACCEPTED is the earned result.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category, Status from each section.
Read TOPICS.md. Record tier for {topic} and compliance tags.
WRITE: "Tier: {N} (source: TOPICS.md | --tier | default)"

STEP 1 COMPLETION GATE:
  DO NOT proceed to STEP 2 (Auto-Flag) until every namespace header field is extracted
  and listed. Incomplete extraction before proceeding is a named error: premature-advance.

---

STEP 2 — AUTO-FLAG

Apply these three rules. Each is mandatory. None is role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of mock quality,
  content depth, or any evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless of evaluation quality.

RULE 3 — COMPLIANCE (when compliance context is active):
  IF compliance tags in TOPICS.md OR --compliance flag set
  AND namespace in {scout-compliance, trace-permissions}
  THEN: REAL-REQUIRED, trigger = COMPLIANCE
  DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED when compliance context
  is active.

DO NOT apply any role evaluation to auto-flagged namespaces.
Named error: **auto-rule contamination** — detectable by inspection.

Output:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting evaluation — default: REAL-REQUIRED): [{namespace}: Category = {type}]

STEP 2 COMPLETION GATE:
  DO NOT proceed to STEP 3 (Architect Evaluation) until every namespace is placed in
  exactly one list. Unplaced namespaces before proceeding is a named error: premature-advance.

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer then write Architect verdict.
The evaluation question: does this namespace positively demonstrate technical plausibility?
Each sub-question requires naming a specific artifact — not a yes/no.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this namespace's escape from its REAL-REQUIRED default position.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

CROSS-STEP CONTAMINATION GUARD — Architect to PM:
  This guard fires on a specific verdict value — it is not a phase-completion gate.
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM evaluation (STEP 5) to these namespaces.
    Strategy evaluation (STEP 4) may still run for coverage gap synthesis purposes.
  Guard output (required):
    Cross-step blocked (PM suppressed): [{namespace} — architect-verdict = CONTRADICTS-ARCHITECTURE]
    Cleared for PM (STEP 5): [{namespace} — architect-verdict = CONSISTENT-WITH-ARCHITECTURE]

STEP 3 COMPLETION GATE:
  DO NOT proceed to STEP 4 (Strategy Evaluation) until: (a) Architect verdicts written for
  all remaining namespaces, AND (b) cross-step guard assignments recorded. Incomplete
  guard output before proceeding is a named error: guard-bypass.

---

STEP 4 — STRATEGY EVALUATION (non-auto namespaces only)

Strategy runs for ALL remaining namespaces, including cross-step-blocked namespaces.
Cross-step-blocked namespaces contribute Strategy SQ-1 answers to the coverage gap
synthesis in STEP 7. Their final decision is already REAL-REQUIRED; Strategy does not
change it.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED
        default position (or: "No gap — earns escape from default").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

STEP 4 COMPLETION GATE:
  DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts are written for every
  remaining namespace (including cross-step-blocked ones).

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: applies ONLY to namespaces where architect-verdict =
CONSISTENT-WITH-ARCHITECTURE. Cross-step-blocked namespaces (architect-verdict =
CONTRADICTS-ARCHITECTURE) DO NOT enter STEP 5. Applying PM to a cross-step-blocked
namespace is a named error: **guard-bypass contamination**.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED
        default position (or: "No gap — earns escape from default").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE:
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for
  all qualifying namespaces. Verify the entry-condition list was respected: no
  cross-step-blocked namespace should carry a PM verdict.

---

STEP 6 — DECISIONS WITH CITATION

**Trigger field notation:** `trigger = {value}` in fixed position.
  EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE | PM-INCOMPLETE | ARCH-IMPLAUSIBLE |
  STRATEGY-INADEQUATE | n/a (MOCK-ACCEPTED)

**Artifact state:** Artifact as grammatical subject. Present tense. Not verdict echo.

MOCK-ACCEPTED template (requires all three positive verdicts):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
  Structural position (Strategy SQ-1 tier decision): [SQ-1 decision + STRUCTURAL-FORM
    or TIER-GATING classification. SLOT-LABEL VIOLATION if generic adequacy statement.]
  Contrast: [Namespace type + structural factor that would require real evidence.
    Must name BOTH. Category echo without structural factor is a named error.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [verdict text]
  Artifact state: [Artifact as subject, present tense.]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

STEP 6 COMPLETION GATE:
  DO NOT proceed to STEP 7 (Write Review Artifact) until every namespace has a completed
  decision block. Verify: no namespace is missing a trigger field.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.

  Coverage Review table: | Namespace | Category | Decision | trigger |

  Next Steps skeleton — fill all four sections; write "(none)" if empty:

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* first, then scout-feasibility, then listen-* and scout-competitors.
     Evaluation-driven: /{skill-id} {topic} — {Artifact state field from STEP 6}
     Auto-flagged:      /{skill-id} {topic} — trigger: {trigger value}]

    Priority 2 — Non-critical REAL-REQUIRED:
    [Evaluation-driven: /{skill-id} {topic} — {Artifact state field}
     Auto-flagged:      /{skill-id} {topic} — trigger: {trigger value}]

    Priority 3 — Evidence-heavy REAL-REQUIRED:
    [/{skill-id} {topic} — trigger: EVIDENCE-HEAVY]

    Cross-namespace risk statement:
    ["Highest-risk gap: {namespace} — {Tier {tier} decision at risk} — urgency: {level}"]

STEP 7 COMPLETION GATE:
  DO NOT proceed to STEP 8 (Write Status Back) until review artifact is written and
  all four next-steps sections are present (including "(none)" entries where applicable).

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit in-place. Replace every Status: MOCK (awaiting review) with final decision.

Canary Confirmation:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  Write ONLY after verifying zero remain. Writing prematurely is CANARY-FALSE-POSITIVE.
  If any remain: "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"

Full confirmation block (when verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-05 — Ceiling (Role Sequence + Output Format + Lifecycle Emphasis)

**axes:** role-sequence + output-format + lifecycle-emphasis
**hypothesis:** V-01 Architect-first + C-26 cross-step guard establishes C-26. V-02
FORBIDDEN OUTPUTS TRIAD establishes C-27. V-04 lifecycle gates deepen C-18. The three
axes are mutually reinforcing for C-26 and C-27: the guard fires on the same verdict values
that the triad lists as forbidden outputs, making the contamination control and the
forbidden-output set semantically coherent. All R7 V-05 ceiling criteria preserved:
DEFAULT DECISION POSITION (C-22), labeled SQ-1 slot (C-23), explicit eval-driven
sub-templates in STEP 7 (C-24), two-slot MOCK-ACCEPTED template with Contrast: sub-slot
(C-25), Artifact state grammar (C-21), canary with CANARY-FALSE-POSITIVE (C-16).
Ordering: Architect → Strategy → PM (C-26 requires Architect before PM; C-23 requires
Strategy before STEP 6 decisions — both preserved). Expected: C-26 PASS, C-27 PASS,
all prior criteria preserved. Failure conditions: (1) triad section and per-rule inline
DO NOT statements become redundant and one is dropped; both required simultaneously for
C-11 + C-27; (2) Architect-first breaks C-23 if Strategy SQ-1 unavailable before STEP 6
— avoided because Strategy runs in STEP 4 before STEP 6.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace in this review begins as REAL-REQUIRED. This is the starting state —
  not a finding, not a judgment. MOCK-ACCEPTED is an earned outcome. A namespace earns
  MOCK-ACCEPTED only when all three role evaluations (Architect, Strategy, PM) actively
  confirm that it positively demonstrates what is required. The evaluation question for
  each role is not "does anything disqualify this namespace?" — it is "does this namespace
  positively demonstrate what is needed?" Absence of disqualification is not positive
  evidence. REAL-REQUIRED is the null result. MOCK-ACCEPTED is the earned result.

---

STEP 1 — READ

Read {mock-artifact-path}.
Extract from each namespace section: namespace name, Category field, current Status field.
Read TOPICS.md. Record: tier for {topic}, compliance tags.

WRITE at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"

STEP 1 COMPLETION GATE:
  DO NOT proceed to STEP 2 (Auto-Flag) until all namespace header fields are extracted
  and listed. Incomplete extraction before proceeding is a named error: premature-advance.

---

STEP 2 — AUTO-FLAG

Apply these three rules in order. Each rule is mandatory. None is optional or role-overridable.

RULE 1 — EVIDENCE-HEAVY (all tiers):
  trigger-condition: Category == EVIDENCE-HEAVY
  decision:          REAL-REQUIRED
  trigger:           EVIDENCE-HEAVY
  forbidden-output:  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                     of mock quality, content depth, or any evaluation outcome.

RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3 only):
  trigger-condition: tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*,
                     scout-competitors}
  decision:          REAL-REQUIRED
  trigger:           TIER-CRITICAL
  forbidden-output:  DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                     of mock quality, content depth, or any evaluation outcome.

RULE 3 — COMPLIANCE (when compliance context is active):
  trigger-condition: compliance tags in TOPICS.md OR --compliance flag set AND namespace
                     in {scout-compliance, trace-permissions}
  decision:          REAL-REQUIRED
  trigger:           COMPLIANCE
  forbidden-output:  DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                     of mock quality, content depth, or any evaluation outcome.

FORBIDDEN OUTPUTS TRIAD (complete enumerable set — all three labels required):
  [1] EVIDENCE-HEAVY: DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
      of mock quality, structural depth, or any evaluation outcome.
  [2] TIER-CRITICAL: DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
      of mock quality, structural depth, or any evaluation outcome.
  [3] COMPLIANCE: DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
      of mock quality, structural depth, or any evaluation outcome.
  Verification: all three labels [1][2][3] must appear. A triad missing any one label is
  incomplete and does not satisfy the enumerable-set requirement.

DO NOT apply Architect, Strategy, or PM evaluation to any auto-flagged namespace.
Applying role evaluation to a namespace already decided by an automatic rule is a named
error: **auto-rule contamination**. Detectable by inspection: an auto-flagged namespace
that carries both a trigger label and an evaluation verdict has been contaminated. The
automatic rule verdict stands unconditionally; any evaluation verdict on an auto-flagged
namespace is void.

Output two lists:
  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = EVIDENCE-HEAVY
  - {namespace}: trigger = TIER-CRITICAL
  - {namespace}: trigger = COMPLIANCE

  Remaining (awaiting evaluation — default: REAL-REQUIRED):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

STEP 2 COMPLETION GATE:
  DO NOT proceed to STEP 3 (Architect Evaluation) until every namespace is placed in
  exactly one list.

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Architect verdict.
The evaluation question is: does this namespace positively demonstrate technical
plausibility? Each sub-question requires a named artifact — not a yes/no.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this namespace's escape from its REAL-REQUIRED default position.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE or CONTRADICTS-ARCHITECTURE

CROSS-STEP CONTAMINATION GUARD — Architect to PM:
  This guard fires on a specific verdict value. It is distinct from the STEP 3 completion
  gate: the completion gate fires when the step is done; this guard fires on a verdict value
  and suppresses a specific downstream step.

  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM evaluation (STEP 5) to these namespaces.
    Strategy evaluation (STEP 4) still runs for these namespaces — for coverage gap synthesis.
    Applying PM to a cross-step-blocked namespace is a named error: **guard-bypass contamination**.

  Guard output (required before proceeding):
    Cross-step blocked (PM suppressed): [{namespace} — architect-verdict = CONTRADICTS-ARCHITECTURE]
    Cleared for PM (STEP 5):            [{namespace} — architect-verdict = CONSISTENT-WITH-ARCHITECTURE]

STEP 3 COMPLETION GATE:
  DO NOT proceed to STEP 4 (Strategy Evaluation) until: (a) Architect verdicts written for
  all remaining namespaces, AND (b) cross-step guard output recorded.

---

STEP 4 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace (including cross-step-blocked namespaces), answer and write
Strategy verdict. The evaluation question is: does this namespace positively demonstrate
coverage adequacy for Tier {tier}? Each sub-question requires a named artifact — not a yes/no.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED
        default position (or: "No gap — namespace positively demonstrates coverage
        adequacy and earns escape from default").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Note: For cross-step-blocked namespaces, Strategy SQ-1 feeds the coverage gap synthesis
in STEP 7. Their final decision remains REAL-REQUIRED regardless of Strategy verdict.

STEP 4 COMPLETION GATE:
  DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts written for every
  remaining namespace (including cross-step-blocked ones).

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: applies ONLY to namespaces where architect-verdict =
CONSISTENT-WITH-ARCHITECTURE. Cross-step-blocked namespaces DO NOT enter STEP 5.

For each qualifying namespace, answer and write PM verdict.
The evaluation question is: does this namespace positively demonstrate structural
completeness? Each sub-question requires a named artifact — not a yes/no.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED
        default position (or: "No gap — namespace positively demonstrates structural
        completeness and earns escape from default").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE:
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts written for all
  qualifying namespaces. Verify: no cross-step-blocked namespace carries a PM verdict.

---

STEP 6 — DECISIONS WITH CITATION

**Trigger field notation:** The `trigger` field is a named artifact field in a fixed
position — second line of every REAL-REQUIRED block; third line of every MOCK-ACCEPTED
block (where it is `trigger = n/a`). Enumeration:
  Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED: n/a
Lowercase `trigger`, equals-sign notation (`trigger = {value}`). Free-form text naming
the rule outside this field position does not satisfy the trigger field requirement.

**Artifact state citation grammar:** The `Artifact state` field requires present-tense
artifact-state form. The artifact (a section, table, field, or element in the mock) is
the grammatical subject. The verb is present tense. The observable state is the object.

  Correct: "Section 3.2 lists no fallback path."  "Table Y contains no tier-boundary gate."
  Verdict echo — named error: "Architect found no fallback path." [role as subject]
    "PM evaluation showed the table is absent." [evaluation noun as subject]

  Verdict echo is detectable: grammatical subject is a role name or evaluation noun rather
  than an artifact name. A verdict echo satisfies slot syntax while defeating traceability.

For each namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template (requires CONSISTENT-WITH-ARCHITECTURE + ADEQUATE + STRUCTURALLY ADEQUATE):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Structural position (Strategy SQ-1 tier decision): [State the specific Tier {tier}
    decision from Strategy SQ-1 that this namespace supports. Classify it: STRUCTURAL-FORM
    (structural mock is sufficient; no tier-boundary validation required) or TIER-GATING
    (real evidence required; decision depends on live system state at tier boundaries).
    The slot label names Strategy SQ-1 as the required input and type classification as
    the required output. A generic adequacy statement without SQ-1 decision name and
    type classification is a SLOT-LABEL VIOLATION.]
  Contrast: [Name a namespace type that WOULD require real evidence and state the structural
    factor it has that this namespace does not. Must name BOTH a namespace type AND a
    structural factor. E.g.: "Unlike trace-* namespaces, which carry tier-gating decisions
    that require live architectural evidence because those decisions depend on component
    state at tier transitions, this namespace's outputs are fully determined by their
    structural form and do not depend on runtime state."
    A sentence naming only a category without a structural factor is a CATEGORY ECHO —
    a named template error that does not satisfy this slot.]

  Template errors (both are named and detectable):
  - SLOT-LABEL VIOLATION: Structural position slot filled with generic adequacy statement.
  - CATEGORY ECHO: Contrast slot names category without structural factor.

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS-ARCHITECTURE | INSUFFICIENT FOR TIER N]
  Artifact state: [Present-tense, artifact as grammatical subject. Not verdict echo.]

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

STEP 6 COMPLETION GATE:
  DO NOT proceed to STEP 7 (Write Review Artifact) until every namespace has a completed
  decision block with trigger field present.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md:

  Header: Topic | Tier used | Date

  Coverage Review table:
    | Namespace | Category | Decision | trigger |
    One row per namespace; all namespaces from Steps 2 and 6.

  Next Steps — use this pre-printed skeleton. Fill all four sections. Write "(none)" for
  empty sections. Do not collapse or reorder sections.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* namespaces first, then scout-feasibility, then listen-* and scout-competitors.
     TWO required entry formats — select by decision type:
       Evaluation-driven: /{skill-id} {topic} — {Artifact state field from STEP 6 decision block}
       Auto-flagged:      /{skill-id} {topic} — trigger: {trigger value}
     An evaluation-driven entry that omits the Artifact state field is a traceability break.
     An auto-flagged entry that includes an Artifact state field is a format error.]

    Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    [All non-critical, non-evidence-heavy REAL-REQUIRED namespaces.
     TWO required entry formats — select by decision type:
       Evaluation-driven: /{skill-id} {topic} — {Artifact state field from STEP 6 decision block}
       Auto-flagged:      /{skill-id} {topic} — trigger: {trigger value}]

    Priority 3 — Evidence-heavy REAL-REQUIRED (sequence after Priority 1 and 2):
    [All EVIDENCE-HEAVY REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — trigger: EVIDENCE-HEAVY]

    Cross-namespace risk statement:
    [Required output. Name the single highest-risk coverage gap — the REAL-REQUIRED namespace
     whose absence most threatens a Tier {tier} decision. State the specific Tier {tier}
     decision at risk. Assign urgency: BLOCKING | HIGH | MEDIUM.
     Format: "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
     — urgency: {BLOCKING | HIGH | MEDIUM}"]

STEP 7 COMPLETION GATE:
  DO NOT proceed to STEP 8 (Write Status Back) until review artifact is written and all
  four next-steps sections are present (including "(none)" entries).

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

MUST update every Status line in {mock-artifact-path}.
Use Edit tool. In-place replacement only. Do not rewrite any other content.

For each namespace:
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  OR:      Status: REAL-REQUIRED [{trigger value from canonical field}]

After completing all edits, verify before confirming.

**Canary Confirmation — output protocol:**

The following line is a CANARY OUTPUT:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

This line is an assertion that the stated condition is true. Its presence claims that every
Status field in {mock-artifact-path} has been updated. Writing this line when any Status
field remains as MOCK (awaiting review) is a protocol error named CANARY-FALSE-POSITIVE.
This error is detectable by inspection of {mock-artifact-path}.

Protocol:
  - Write the canary ONLY after confirming that zero Status fields remain as MOCK.
  - If any Status field was not updated: suppress the canary. Output instead:
      "CANARY SUPPRESSED: {N} Status field(s) not updated — {namespace list}"
    Attempt the remaining edits. Re-verify. Then write the canary when condition is met.

Full confirmation block (only when canary condition is verified):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

This is the defining action of /mock:review. It is not optional.
