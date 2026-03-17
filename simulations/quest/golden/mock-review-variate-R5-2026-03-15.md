---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 5
rubric_version: v5
status: VARIATE
---

# mock-review Variate — Round 5

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v5 (C-01 through C-21; aspirational denominator = 13)
**Round:** R5 — targeting v5 new criteria: C-20, C-21

---

## What R4 Left Open

R4 V-05 (the ceiling) combined four structural guarantees: named contamination error
(C-17), all-gate forward naming (C-18), unified trigger field notation (C-19), and
pre-printed next-steps skeleton with mandatory cross-namespace risk statement (C-09).
Two new aspirational criteria were introduced in v5 based on patterns visible in R4
V-05 and the bottom of the R4 variation map:

| Criterion | Best R4 V-05 coverage | Gap |
|-----------|----------------------|-----|
| C-20 Contrastive MOCK-ACCEPTED rationale | STEP 6 MOCK-ACCEPTED template: "Rationale: [One sentence: why this code applies to this specific namespace]" | Instructional text only — no structural guarantee that the sentence is contrastive. A model can write "STRUCTURAL-COVERAGE-SUFFICIENT: Structural coverage is sufficient for this namespace." and satisfy the Rationale slot while producing a confirmatory sentence. C-20 requires the sentence to CONTRAST the namespace's structural state against the threshold that would require real evidence — naming a namespace type that WOULD cross the threshold and the structural factor this namespace lacks. A confirmatory sentence ("sufficient here") does not satisfy; a contrastive sentence ("unlike trace-*, which carries tier-gating decisions that structural mock cannot validate...") does. |
| C-21 SQ answer structural signal | STEP 6 REAL-REQUIRED template: "Sub-question answer that drove this verdict: [The exact SQ answer — name the specific section, element, gap, or decision; not a restatement of the verdict]" | The negative prohibition ("not a restatement of the verdict") is present but the positive structural signal is absent. C-21 requires a FORM — a present-tense artifact-naming pattern that mechanically distinguishes a genuine SQ answer from a verdict echo. R4 V-05 instructs the model not to restate; it does not give the model the distinguishing form. Present-tense artifact naming ("Section 3.2 lists no fallback path") is structurally different from past-tense verdict restatement ("Architect found no fallback path") — but the distinction is not named in the template. The error is not named either. A template slot that only says "not a restatement" leaves the model without a positive rule to apply. |

R4 recommendation for R5 (bottom of R4 file): "A focused R5 test would add a rationale
adequacy check to the MOCK-ACCEPTED template: the rationale sentence must explain why the
reason code applies to _this_ namespace compared to a namespace that would require real
evidence, making the distinction explicit rather than just stating the code applies."
This maps directly to C-20. The R4 recommendation did not anticipate C-21's form
requirement — R5 must address the positive structural signal in the citation slot
separately, as C-21 is structurally different from C-20.

---

## Axis-Assignment Plan

| Plan | Axis | Source signal | Target criteria | Predicted |
|------|------|---------------|-----------------|-----------|
| V-01 | role-sequence | Strategy first: SQ-1 for Strategy names the specific Tier decision the namespace supports — running Strategy before PM means the evaluator is already framing the namespace in terms of its decision purpose when they write the MOCK-ACCEPTED rationale, which is the context that produces contrastive sentences ("unlike trace-*, which validates tier-gating decisions..."). No template change. | C-20 partial, C-07 | Strategy-first framing produces rationale sentences that reference tier-critical namespaces by contrast. Expected: C-20 PARTIAL at best — the framing helps but no structural guarantee forces the contrast slot. Validates whether sequence alone is sufficient or template change is required. |
| V-02 | output-format | Contrastive rationale template: MOCK-ACCEPTED template gains two required slots — Structural position (what property this namespace has that keeps it below the real-evidence threshold) and Contrast (name a namespace type that WOULD require real evidence and the structural factor it has that this namespace lacks). Names the confirmatory echo error. | C-20 | Template with two required slots makes confirmatory-only rationale structurally unsatisfiable — filling the Contrast slot requires naming a contrasting namespace type. Expected: C-20 PASS. Failure condition: model fills Contrast with "unlike evidence-heavy namespaces" without naming the specific structural factor. |
| V-03 | phrasing-register | Present-tense artifact grammar: SQ citation slot label rewritten to specify present-tense artifact-naming form ("Section X lists...", "Table Y contains..."), distinguishes this from verdict echo ("Role found...", "Evaluation showed..."), names "verdict echo" as a detectable error with its structural pattern. | C-21 | Positive structural signal (present-tense form) + named error (verdict echo) makes the distinction mechanically applicable. Expected: C-21 PASS. Failure condition: model uses hybrid form ("Section X was found to contain no Y") that is syntactically past-tense but references an artifact — ambiguous on the criterion. |
| V-04 | role-sequence + inertia-framing | Strategy first (V-01 axis) + REAL-REQUIRED default framing: all namespaces begin as REAL-REQUIRED; MOCK-ACCEPTED is earned, not presumed. Inertia framing changes the evaluator's posture — the question becomes "what is it about this namespace that escapes the REAL-REQUIRED default?" which is inherently contrastive. | C-20 framing benefit, C-09 | Inertia framing makes the MOCK-ACCEPTED rationale naturally explain the escape from default, which is the contrastive logic C-20 requires. Expected: C-20 PARTIAL — framing aids without structural guarantee. Primary target: whether inertia framing produces better urgency grouping in C-09 cross-namespace risk statement. |
| V-05 | output-format + phrasing-register + inertia-framing | V-02 contrastive template + V-03 present-tense grammar + V-04 inertia framing. The triad is mutually reinforcing: inertia framing changes the decision context (MOCK-ACCEPTED must escape default); contrastive template forces the escape argument to name the threshold boundary; present-tense grammar ensures the SQ citation is artifact-anchored not verdict-restated. | C-20, C-21 | Ceiling combination: both new criteria addressed through structural guarantees rather than instructions; inertia framing provides the motivating context that makes C-20's contrastive requirement feel coherent rather than arbitrary. Preserves all prior ceiling criteria C-09 through C-19. |

---

## V-01 — Strategy-First Role Sequence

**axis:** role-sequence
**hypothesis:** R4 V-05 runs PM → Architect → Strategy. Strategy's SQ-1 requires naming
the specific Tier N decision the namespace is intended to support. Running Strategy before
PM means the evaluator must anchor to the namespace's decision purpose BEFORE examining
structure. When the evaluator subsequently writes the MOCK-ACCEPTED rationale, they are
already thinking "this namespace supports Decision D, not a tier-gating decision" — the
framing that produces a contrastive sentence without a template forcing it. The test: does
role sequence alone produce C-20-quality rationale, or is the contrastive template (V-02)
required? If V-01 achieves C-20 PARTIAL, the sequence helps but does not guarantee the
contrast. If V-01 achieves C-20 PASS, sequence alone is sufficient and V-02 adds redundant
structure. Expected: C-20 PARTIAL (sequence aids, template required for guarantee). Failure
condition: Strategy-first sequence produces C-09 regression — coverage gaps identified early
in the sequence cause the evaluator to skip PM/Architect for already-REAL-REQUIRED namespaces
before the auto-flag phase has formally decided them.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

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
  mock content depth, or PM/Architect/Strategy evaluation outcome.

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

DO NOT apply PM, Architect, or Strategy evaluation to any auto-flagged namespace.
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

  Remaining (awaiting evaluation):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

DO NOT proceed to STEP 3 until every namespace is placed in exactly one list.

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Strategy verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would affect a Tier {tier} commitment (or: "No gap identified").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 4 until Strategy verdicts are written for every remaining namespace.

---

STEP 4 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the PM verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would prevent a PM from accepting this as Tier {tier}
        coverage (or: "No gap identified").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 until PM verdicts are written for every remaining namespace.

---

STEP 5 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Architect verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms or
        challenges this mock's plausibility.

  Architect Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 until Architect verdicts are written for every remaining namespace.

---

STEP 6 — DECISIONS WITH CITATION

**Trigger field notation:** The `trigger` field is a named artifact field in a fixed
position — the second line of every REAL-REQUIRED decision block and the third line of every
MOCK-ACCEPTED decision block (where it is `trigger = n/a`). Its value is always drawn from
this enumeration:
  Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED: n/a
The field uses lowercase `trigger` and equals-sign notation (`trigger = {value}`) in all
positions. This is the canonical format. Free-form text mentioning the rule name outside this
field position does not satisfy the trigger field requirement.

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Rationale: [One sentence: why this code applies to this specific namespace, drawing on
    the Strategy SQ-1 answer from STEP 3 — the Tier decision this namespace supports
    should inform why structural coverage is sufficient for that decision]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Sub-question answer that drove this verdict: "[The exact SQ answer — name the specific
    section, element, gap, or decision; not a restatement of the verdict]"

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
    The `trigger` column uses the same canonical notation as decision blocks.

  Next Steps — use this pre-printed skeleton. Fill all four sections. Do not collapse or
  reorder the sections. If a section has no entries, write "(none)" — do not omit the section.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [List trace-* namespaces first, then scout-feasibility, then listen-* and scout-competitors.
     Format: /{skill-id} {topic} — {one-line reason citing sub-question answer if evaluation-driven}]

    Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    [List all non-critical, non-evidence-heavy REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — {one-line reason citing sub-question answer if evaluation-driven}]

    Priority 3 — Evidence-heavy REAL-REQUIRED (sequence after Priority 1 and 2):
    [List all EVIDENCE-HEAVY REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — {one-line reason}]

    Cross-namespace risk statement:
    [Required output. Name the single highest-risk coverage gap — the REAL-REQUIRED namespace
     whose absence most threatens a Tier {tier} decision. State the specific Tier {tier}
     decision at risk. Assign urgency: BLOCKING (must resolve before any Tier {tier} work
     begins) | HIGH (resolve within current sprint) | MEDIUM (resolve before Tier {tier}
     commit). Format: "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
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

---

## V-02 — Contrastive Rationale Template

**axis:** output-format
**hypothesis:** R4 V-05 STEP 6 instructs the model to write "One sentence: why this code
applies to this specific namespace." This instruction can be satisfied with a confirmatory
sentence: "STRUCTURAL-COVERAGE-SUFFICIENT: The mock artifact contains the required sections
and gates for this namespace." The sentence is namespace-specific and explains why the code
applies — but it does not contrast the namespace's structural state against the threshold
that would require real evidence. C-20 requires the contrast. A pre-printed template with
two required named slots makes a confirmatory-only rationale structurally unsatisfiable: the
Structural-position slot alone can be filled with a confirmatory sentence, but the Contrast
slot requires naming a different namespace type and the structural factor it has that this
namespace lacks. A model cannot fill the Contrast slot with "this namespace is adequate"
because the slot grammar requires naming an external namespace type. Names the confirmatory
echo error: writing a confirmatory sentence in the Contrast slot is a named structural error.
Expected: C-20 PASS (two-slot template forces contrast). C-10 improvement (rationale becomes
substantive by definition). Failure condition: model fills Contrast with "unlike evidence-heavy
namespaces" without naming the specific structural factor those namespaces have — the contrast
names a category without naming the differentiating property, satisfying slot syntax while
remaining semantically generic.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

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
  mock content depth, or PM/Architect/Strategy evaluation outcome.

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

DO NOT apply PM, Architect, or Strategy evaluation to any auto-flagged namespace.
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

  Remaining (awaiting evaluation):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

DO NOT proceed to STEP 3 until every namespace is placed in exactly one list.

---

STEP 3 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the PM verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would prevent a PM from accepting this as Tier {tier}
        coverage (or: "No gap identified").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 4 until PM verdicts are written for every remaining namespace.

---

STEP 4 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Architect verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms or
        challenges this mock's plausibility.

  Architect Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 until Architect verdicts are written for every remaining namespace.

---

STEP 5 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Strategy verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would affect a Tier {tier} commitment (or: "No gap identified").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 until Strategy verdicts are written for every remaining namespace.

---

STEP 6 — DECISIONS WITH CITATION

**Trigger field notation:** The `trigger` field is a named artifact field in a fixed
position — the second line of every REAL-REQUIRED decision block and the third line of every
MOCK-ACCEPTED decision block (where it is `trigger = n/a`). Its value is always drawn from
this enumeration:
  Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED: n/a
The field uses lowercase `trigger` and equals-sign notation (`trigger = {value}`) in all
positions. This is the canonical format.

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Structural position: [Name the structural property this namespace has that places it BELOW
    the threshold for requiring real evidence. Name the specific property, not a general
    adequacy judgment. E.g.: "This namespace has no tier-gating decisions, no architecture-
    pattern dependencies enforced at tier boundaries, and no compliance-signal obligations."]
  Contrast: [Name a namespace type that WOULD require real evidence, and state the structural
    factor it has that this namespace does not. The contrast must name BOTH a namespace type
    AND a structural factor. E.g.: "Unlike trace-* namespaces, which carry tier-gating
    decisions that structural mock cannot validate, this namespace's outputs are fully
    determined by their structural form and do not depend on live architectural state."]

  Confirmatory echo error: A Structural position sentence that says only "structural coverage
  is sufficient here" is a CONFIRMATORY sentence — it confirms the code without contrasting.
  A Contrast field that says "unlike evidence-heavy namespaces, this is structural" names a
  category but not a structural factor. Both are named errors; neither satisfies this template.

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Sub-question answer that drove this verdict: "[The exact SQ answer — name the specific
    section, element, gap, or decision; not a restatement of the verdict]"

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
    The `trigger` column uses the same canonical notation as decision blocks.

  Next Steps — use this pre-printed skeleton. Fill all four sections. Do not collapse or
  reorder the sections. If a section has no entries, write "(none)" — do not omit the section.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [List trace-* namespaces first, then scout-feasibility, then listen-* and scout-competitors.
     Format: /{skill-id} {topic} — {one-line reason citing sub-question answer if evaluation-driven}]

    Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    [List all non-critical, non-evidence-heavy REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — {one-line reason citing sub-question answer if evaluation-driven}]

    Priority 3 — Evidence-heavy REAL-REQUIRED (sequence after Priority 1 and 2):
    [List all EVIDENCE-HEAVY REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — {one-line reason}]

    Cross-namespace risk statement:
    [Required output. Name the single highest-risk coverage gap — the REAL-REQUIRED namespace
     whose absence most threatens a Tier {tier} decision. State the specific Tier {tier}
     decision at risk. Assign urgency: BLOCKING | HIGH | MEDIUM.
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

This line is an assertion that the stated condition is true. Writing this line when any Status
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

---

## V-03 — Present-Tense Artifact Grammar

**axis:** phrasing-register
**hypothesis:** R4 V-05 STEP 6 REAL-REQUIRED template says: "The exact SQ answer — name the
specific section, element, gap, or decision; not a restatement of the verdict." This is a
negative prohibition: it tells the model what not to produce. C-21 requires a positive
structural signal — a form that mechanically distinguishes a genuine SQ answer from a verdict
echo, plus a named error for the echo. The positive form is present-tense artifact naming:
"Section 3.2 lists no fallback path" is in present tense and names an artifact in an
observable state. "Architect found no fallback path" is in past tense and names a role action,
not an artifact state — this is a verdict echo. The distinction is grammatically testable:
present-tense subject-is-artifact form vs past-tense subject-is-role form. Adding a template
instruction that specifies the positive form ("present tense: 'Section X lists...'") and names
the error form ("verdict echo: 'Role found...'") gives the model a rule to apply rather than
only a prohibition to observe. Expected: C-21 PASS (positive form specified, error named,
distinction grammatically testable). C-14 improvement (citation template now produces
genuinely traceable output, not just template-slot-filled output). Failure condition: model
uses hybrid past-tense artifact form — "Section 3.2 was found to contain no fallback path"
— which names an artifact but uses past tense. This is borderline; the criterion requires the
prompt to address this case explicitly or risk ambiguous scoring.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

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
  mock content depth, or PM/Architect/Strategy evaluation outcome.

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

DO NOT apply PM, Architect, or Strategy evaluation to any auto-flagged namespace.
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

  Remaining (awaiting evaluation):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

DO NOT proceed to STEP 3 until every namespace is placed in exactly one list.

---

STEP 3 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the PM verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would prevent a PM from accepting this as Tier {tier}
        coverage (or: "No gap identified").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 4 until PM verdicts are written for every remaining namespace.

---

STEP 4 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Architect verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms or
        challenges this mock's plausibility.

  Architect Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 until Architect verdicts are written for every remaining namespace.

---

STEP 5 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Strategy verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would affect a Tier {tier} commitment (or: "No gap identified").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 until Strategy verdicts are written for every remaining namespace.

---

STEP 6 — DECISIONS WITH CITATION

**Trigger field notation:** The `trigger` field is a named artifact field in a fixed
position — the second line of every REAL-REQUIRED decision block and the third line of every
MOCK-ACCEPTED decision block (where it is `trigger = n/a`). Its value is always drawn from
this enumeration:
  Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED: n/a
The field uses lowercase `trigger` and equals-sign notation (`trigger = {value}`) in all
positions. This is the canonical format.

**SQ answer citation grammar:** The sub-question answer citation slot requires present-tense
artifact-state form. The artifact (a section, table, field, or element) is the grammatical
subject. The verb is present tense. The observable state is the object.

  Correct form (artifact state, present tense):
    "Section 3.2 lists no fallback path."
    "Table Y contains no tier-boundary gate for this namespace."
    "The mock artifact shows no compliance-signal field."

  Verdict echo (role action, past tense) — named error — DO NOT USE:
    "Architect found no fallback path."
    "PM evaluation showed the table is absent."
    "Strategy determined coverage is insufficient."

  Verdict echo error: A verdict echo restates the evaluation conclusion as a past-tense
  role action with the evaluating role as subject. It may be true but it names what the
  role did, not what the artifact shows. A verdict echo fills the slot syntax while
  defeating its purpose — the slot exists to cite observable artifact state, not to
  summarize a role's finding. Verdict echos are detectable: subject is a role name
  (Architect, PM, Strategy) or evaluation noun (evaluation, assessment, review).

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Rationale: [One sentence: why this code applies to this specific namespace]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Artifact state: ["[Present-tense artifact-state form — the artifact as subject, present
    tense verb, observable state as object. Not verdict echo — do not name the role or the
    evaluation as subject. E.g.: 'Section 3.2 lists no fallback path for this namespace.'"]

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
    The `trigger` column uses the same canonical notation as decision blocks.

  Next Steps — use this pre-printed skeleton. Fill all four sections. Do not collapse or
  reorder the sections. If a section has no entries, write "(none)" — do not omit the section.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* first, then scout-feasibility, then listen-* and scout-competitors.
     Format: /{skill-id} {topic} — {artifact state from citation slot if evaluation-driven}]

    Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    [All non-critical, non-evidence-heavy REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — {artifact state from citation slot if evaluation-driven}]

    Priority 3 — Evidence-heavy REAL-REQUIRED (sequence after Priority 1 and 2):
    [All EVIDENCE-HEAVY REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — {one-line reason}]

    Cross-namespace risk statement:
    [Required output. Name the single highest-risk coverage gap — the REAL-REQUIRED namespace
     whose absence most threatens a Tier {tier} decision. State the specific Tier {tier}
     decision at risk. Assign urgency: BLOCKING | HIGH | MEDIUM.
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

---

## V-04 — Role Sequence + Inertia Framing

**axes:** role-sequence + inertia-framing
**hypothesis:** The inertia framing axis reframes the default decision position: instead of
treating MOCK-ACCEPTED and REAL-REQUIRED as symmetric outcomes to be discovered by evaluation,
inertia framing makes REAL-REQUIRED the starting position for every namespace. MOCK-ACCEPTED
is an earned state, not the default for well-formed mocks. This framing change affects how
the evaluator writes rationale sentences: the question shifts from "why is this adequate?" to
"what is it about this namespace that escapes the REAL-REQUIRED default?" — the escape
question is inherently contrastive, because the answer must distinguish this namespace from
namespaces that remain REAL-REQUIRED. Combined with Strategy-first evaluation (V-01 axis),
the framing produces a context where the Strategy verdict names the tier decision (SQ-1),
the PM verdict confirms structure, the Architect verdict confirms plausibility, and the
MOCK-ACCEPTED rationale explains the escape from default by contrasting with namespaces that
cannot escape. Expected: C-20 PARTIAL improvement from framing; C-09 improvement because
inertia framing makes urgency grouping natural (REAL-REQUIRED is the norm, urgency describes
how urgently each namespace needs to be evaluated to escape the default). Full C-20 PASS may
require the two-slot template from V-02 — this variation tests whether framing alone closes
the gap. Failure condition: inertia framing introduces negative bias — evaluators become
reluctant to award MOCK-ACCEPTED, increasing false REAL-REQUIRED decisions and distorting
Coverage Review tables toward REAL-REQUIRED even for clearly adequate mocks.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  All namespaces in this review begin as REAL-REQUIRED. MOCK-ACCEPTED is not the default.
  A namespace becomes MOCK-ACCEPTED only when all three role evaluations (Strategy, PM,
  Architect) actively confirm it as adequate. A namespace that cannot be positively confirmed
  through all three evaluations remains REAL-REQUIRED. The evaluation question for each role
  is not "does anything disqualify this namespace?" — it is "does this namespace positively
  demonstrate what is required?" REAL-REQUIRED is the null result; MOCK-ACCEPTED is the
  earned result.

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
  mock content depth, or PM/Architect/Strategy evaluation outcome.

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

DO NOT apply PM, Architect, or Strategy evaluation to any auto-flagged namespace.
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
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        position (or: "No gap — namespace has positively demonstrated coverage adequacy").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 4 until Strategy verdicts are written for every remaining namespace.

---

STEP 4 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the PM verdict.
The evaluation question is: does this namespace positively demonstrate structural completeness?
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        position (or: "No gap — namespace has positively demonstrated structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 until PM verdicts are written for every remaining namespace.

---

STEP 5 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Architect verdict.
The evaluation question is: does this namespace positively demonstrate technical plausibility?
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms or
        challenges this namespace's escape from REAL-REQUIRED default.

  Architect Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 until Architect verdicts are written for every remaining namespace.

---

STEP 6 — DECISIONS WITH CITATION

**Trigger field notation:** The `trigger` field is a named artifact field in a fixed
position — the second line of every REAL-REQUIRED decision block and the third line of every
MOCK-ACCEPTED decision block (where it is `trigger = n/a`). Its value is always drawn from
this enumeration:
  Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED: n/a
The field uses lowercase `trigger` and equals-sign notation (`trigger = {value}`) in all
positions. This is the canonical format.

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Rationale: [One sentence explaining what this namespace demonstrated that earned escape
    from its REAL-REQUIRED default. The sentence should name what this namespace has (or
    lacks) compared to namespaces that remain REAL-REQUIRED — including the tier decision
    it supports (from Strategy SQ-1) and whether that decision type requires structural
    validation only vs tier-boundary validation.]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Sub-question answer that drove this verdict: "[The exact SQ answer — name the specific
    section, element, gap, or decision; not a restatement of the verdict]"

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
    The `trigger` column uses the same canonical notation as decision blocks.

  Next Steps — use this pre-printed skeleton. Fill all four sections. Do not collapse or
  reorder the sections. If a section has no entries, write "(none)" — do not omit the section.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* first, then scout-feasibility, then listen-* and scout-competitors.
     Format: /{skill-id} {topic} — {one-line reason}]

    Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    [All non-critical, non-evidence-heavy REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — {one-line reason}]

    Priority 3 — Evidence-heavy REAL-REQUIRED (sequence after Priority 1 and 2):
    [All EVIDENCE-HEAVY REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — {one-line reason}]

    Cross-namespace risk statement:
    [Required output. Name the single highest-risk coverage gap — the REAL-REQUIRED namespace
     whose absence most threatens a Tier {tier} decision. State the specific Tier {tier}
     decision at risk. Assign urgency: BLOCKING | HIGH | MEDIUM.
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

---

## V-05 (Ceiling) — Contrastive Template + Present-Tense Grammar + Inertia Framing

**axes:** output-format + phrasing-register + inertia-framing
**hypothesis:** V-02 (contrastive template) addresses C-20 structurally: the two-slot
MOCK-ACCEPTED template forces the contrast by making a Contrast field that requires naming
an external namespace type and structural factor. V-03 (present-tense grammar) addresses
C-21 structurally: the Artifact state field in the REAL-REQUIRED template specifies present-
tense artifact-naming form and names the verdict echo error as detectable by grammatical
pattern. V-04's inertia framing provides the motivating context that makes both C-20 and
C-21 feel coherent rather than arbitrary constraints: when MOCK-ACCEPTED is an earned escape
from the default, the contrast field explains the escape, and the artifact-state citation
grounds the escape in observable evidence rather than role-action summaries.

The triad is mutually reinforcing:
- Inertia framing changes the decision context: MOCK-ACCEPTED must argue against the default.
- Contrastive template channels that argument into a named structural threshold claim.
- Present-tense grammar ensures the evidence cited in REAL-REQUIRED decisions is artifact-
  anchored, not verdict-restated — making the REAL-REQUIRED decision traceable to the same
  observable artifact layer that the contrastive rationale references.

All prior ceiling criteria preserved:
- C-09: pre-printed next-steps skeleton with mandatory cross-namespace risk statement
- C-11: forbidden-output enumeration in all three rules
- C-12: zero-remaining confirmation
- C-13: separately completable role steps with STOP gates
- C-14: SQ citation slot (now with positive form specification — C-21)
- C-15: entity-naming sub-question grammar
- C-16: canary output with CANARY-FALSE-POSITIVE
- C-17: named contamination error
- C-18: all gates forward-name next step
- C-19: unified trigger = notation

Expected: C-20 PASS (contrastive two-slot template), C-21 PASS (present-tense form + verdict
echo named). Failure conditions: (1) model fills Contrast slot with "unlike evidence-heavy
namespaces" without naming the specific structural factor — satisfies slot syntax, defeats
semantic purpose; (2) model uses hybrid past-tense artifact form ("Section X was found to
list no...") that names an artifact but remains past tense — prompt must address this or
C-21 scoring is ambiguous; (3) inertia framing produces systematic MOCK-ACCEPTED undercount
— the framing creates evaluator reluctance to award MOCK-ACCEPTED, distorting results.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  All namespaces in this review begin as REAL-REQUIRED. MOCK-ACCEPTED is not the default.
  A namespace becomes MOCK-ACCEPTED only when all three role evaluations (Strategy, PM,
  Architect) actively confirm it as adequate. A namespace that cannot be positively confirmed
  through all three evaluations remains REAL-REQUIRED. The evaluation question for each role
  is not "does anything disqualify this namespace?" — it is "does this namespace positively
  demonstrate what is required?" REAL-REQUIRED is the null result; MOCK-ACCEPTED is the
  earned result.

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
  mock content depth, or PM/Architect/Strategy evaluation outcome.

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

DO NOT apply PM, Architect, or Strategy evaluation to any auto-flagged namespace.
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
  SQ-3: Name the coverage gap that would keep this namespace in its REAL-REQUIRED default
        position (or: "No gap — namespace has positively demonstrated coverage adequacy").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 4 until Strategy verdicts are written for every remaining namespace.

---

STEP 4 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the PM verdict.
The evaluation question is: does this namespace positively demonstrate structural completeness?
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the required sections present in the mock artifact for this namespace.
  SQ-2: Name the enforcement gate, decision table, or required output structure present
        (or: "Absent — name what is missing").
  SQ-3: Name one structural gap that would keep this namespace in its REAL-REQUIRED default
        position (or: "No gap — namespace has positively demonstrated structural completeness").

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 5 until PM verdicts are written for every remaining namespace.

---

STEP 5 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Architect verdict.
The evaluation question is: does this namespace positively demonstrate technical plausibility?
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the system component, dependency, or interface in the mock that confirms
        plausibility (or: "Contradiction found — name the element").
  SQ-2: Name the data flow, state transition, or API shape consistent with {topic}
        architecture (or: "Inconsistency found — name it").
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms or
        challenges this namespace's escape from REAL-REQUIRED default.

  Architect Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 until Architect verdicts are written for every remaining namespace.

---

STEP 6 — DECISIONS WITH CITATION

**Trigger field notation:** The `trigger` field is a named artifact field in a fixed
position — the second line of every REAL-REQUIRED decision block and the third line of every
MOCK-ACCEPTED decision block (where it is `trigger = n/a`). Its value is always drawn from
this enumeration:
  Auto-flagged: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE
  Evaluation-driven: PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE
  MOCK-ACCEPTED: n/a
The field uses lowercase `trigger` and equals-sign notation (`trigger = {value}`) in all
positions. This is the canonical format. Free-form text mentioning the rule name outside this
field position does not satisfy the trigger field requirement.

**SQ answer citation grammar:** The Artifact state field requires present-tense artifact-state
form. The artifact is the grammatical subject. The verb is present tense. The observable state
is the object.

  Correct form (artifact state, present tense):
    "Section 3.2 lists no fallback path for this namespace."
    "Table Y contains no tier-boundary gate."
    "The mock artifact shows no compliance-signal field."

  Verdict echo (named error) — DO NOT USE:
    "Architect found no fallback path." [subject = role, not artifact]
    "PM evaluation showed the table is absent." [subject = evaluation, not artifact]
    "Strategy determined coverage is insufficient." [subject = role action, not artifact state]

  Verdict echo is detectable: the grammatical subject is a role name or evaluation noun
  (Architect, PM, Strategy, evaluation, assessment, review) rather than an artifact name.
  A verdict echo fills the Artifact state slot syntax while defeating its purpose: the slot
  exists to cite observable artifact state so the decision is traceable to the mock artifact
  independent of the role that reviewed it.

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Structural position: [Name the structural property this namespace has that places it BELOW
    the threshold for requiring real evidence. Name the specific property — not a general
    adequacy judgment. The tier decision this namespace supports (from Strategy SQ-1) should
    appear here: a namespace supporting a structural-form decision does not need tier-boundary
    validation; one supporting a tier-gating decision does. E.g.: "This namespace supports
    {SQ-1 tier decision}, which requires structural form validation only — it has no tier-
    gating decisions, no architecture-pattern dependencies enforced at tier boundaries, and
    no compliance-signal obligations."]
  Contrast: [Name a namespace type that WOULD require real evidence and state the structural
    factor it has that this namespace does not. The contrast must name BOTH a namespace type
    AND a structural factor. E.g.: "Unlike trace-* namespaces, which carry tier-gating
    decisions that structural mock cannot validate because those decisions depend on live
    architectural state at tier transition, this namespace's outputs are fully determined
    by their structural form and do not require runtime architectural evidence."]

  Confirmatory echo error: Filling Structural position with "structural coverage is sufficient
  here" is a confirmatory sentence — it confirms the code without naming the structural
  property. Filling Contrast with "unlike evidence-heavy namespaces, this is structural"
  names a category but not a structural factor. Both are named template errors; neither
  satisfies this template.

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Artifact state: ["[Present-tense artifact-state form. The artifact is the grammatical
    subject. The verb is present tense. The observable state is the object. E.g.: 'Section
    3.2 lists no fallback path for this namespace.' NOT verdict echo: 'Architect found no
    fallback path.' — that form names the role action, not the artifact state.]"

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
    The `trigger` column uses the same canonical notation as decision blocks.

  Next Steps — use this pre-printed skeleton. Fill all four sections. Do not collapse or
  reorder the sections. If a section has no entries, write "(none)" — do not omit the section.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* first, then scout-feasibility, then listen-* and scout-competitors.
     Format: /{skill-id} {topic} — {artifact state from Artifact state field if eval-driven}]

    Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    [All non-critical, non-evidence-heavy REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — {artifact state from Artifact state field if eval-driven}]

    Priority 3 — Evidence-heavy REAL-REQUIRED (sequence after Priority 1 and 2):
    [All EVIDENCE-HEAVY REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — {one-line reason}]

    Cross-namespace risk statement:
    [Required output. Name the single highest-risk coverage gap — the REAL-REQUIRED namespace
     whose absence most threatens a Tier {tier} decision. State the specific Tier {tier}
     decision at risk. Assign urgency: BLOCKING | HIGH | MEDIUM.
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

---

## Variation Map Summary

| V | Axes | What Changed from R4 V-05 | Target Criteria | Hypothesis |
|---|------|--------------------------|-----------------|------------|
| V-01 | role-sequence | Strategy moved to STEP 3 (before PM and Architect); PM to STEP 4; Architect to STEP 5; Strategy SQ-3 reframed as "coverage gap that would affect a Tier N commitment" | C-20 partial, C-07 | Strategy-first evaluation frames the evaluator in terms of tier-decision purpose before structural/technical evaluation; MOCK-ACCEPTED rationale naturally references the tier decision from SQ-1, which is the context for contrastive sentences — but no structural guarantee forces the contrast |
| V-02 | output-format | MOCK-ACCEPTED template gains two required named slots: Structural position (what property this namespace has that keeps it below the real-evidence threshold) and Contrast (name a namespace type AND structural factor that would require real evidence); Confirmatory echo error named in template | C-20 | Two-slot template makes confirmatory-only rationale structurally unsatisfiable; Contrast slot requires naming an external namespace type, which is the contrast C-20 requires; confirmatory echo error named so failure mode is diagnosable |
| V-03 | phrasing-register | REAL-REQUIRED evaluation-driven template field renamed from "Sub-question answer that drove this verdict" to "Artifact state"; field grammar specified: present-tense, artifact as grammatical subject; "verdict echo" named as detectable error with pattern description (role/evaluation as subject) | C-21 | Positive structural signal (present-tense artifact-subject form) + named error (verdict echo with grammatical detection pattern) gives the model a rule to apply rather than a prohibition to observe; verdict echo is detectable by grammatical subject inspection |
| V-04 | role-sequence + inertia-framing | REAL-REQUIRED default position block added after INPUTS; Strategy moved to STEP 3; SQ-3 for all three roles reframed as "gap that would keep this namespace in its REAL-REQUIRED default position"; MOCK-ACCEPTED rationale instructed to explain "escape from default" | C-20 framing benefit, C-09 | Inertia framing makes MOCK-ACCEPTED an earned escape from default; the escape question is inherently contrastive; Strategy-first ordering names the tier decision before structure is examined; tests whether framing alone produces contrastive rationale without two-slot template |
| V-05 | output-format + phrasing-register + inertia-framing | V-02 two-slot contrastive template + V-03 present-tense artifact grammar + V-04 inertia framing; Structural position slot references Strategy SQ-1 tier decision explicitly; Contrast slot names both namespace type and structural factor; Artifact state field carries full grammar specification and verdict echo detection pattern; all prior ceiling criteria preserved | C-20, C-21 | Ceiling combination: both new v5 criteria addressed through structural guarantees; inertia framing provides the motivating context; contrastive template channels the escape argument into a named structural threshold claim; present-tense grammar ensures REAL-REQUIRED citations are artifact-anchored |

**Top combination candidate for Round 6:**
If V-05 achieves the highest composite and both C-20 and C-21 PASS, the residual open
criteria are the C-11 through C-16 block (which was fully closed in R3 V-05 but may have
partial regressions under the inertia framing context) and C-09 (whether the cross-namespace
risk statement is a genuine cross-namespace synthesis or a per-namespace restatement). A
focused R6 scan should verify that the inertia framing does not introduce evaluator reluctance
to award MOCK-ACCEPTED — if the MOCK-ACCEPTED rate drops significantly under V-04/V-05 compared
to V-01/V-02/V-03, the framing is introducing bias and should be decoupled from the ceiling.
The C-20 contrastive template and C-21 present-tense grammar axes are independent of the
inertia framing — either can be carried forward to R6 without it.
