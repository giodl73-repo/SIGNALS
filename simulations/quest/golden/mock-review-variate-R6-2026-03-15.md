---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 6
rubric_version: v6
status: VARIATE
---

# mock-review Variate — Round 6

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v6 (C-01 through C-24; aspirational denominator = 16)
**Round:** R6 — targeting v6 new criteria: C-22, C-23, C-24

---

## What R5 Left Open

R5 V-05 (the ceiling) combined three structural guarantees: DEFAULT DECISION POSITION
inertia block (V-04 axis), two-slot contrastive MOCK-ACCEPTED template (V-02 axis), and
Artifact state field with present-tense grammar + verdict-echo detection (V-03 axis). Three
new aspirational criteria were introduced in v6 based on patterns visible in R5 V-04/V-05
and structural gaps not yet closed at the slot-label level:

| Criterion | R5 V-05 coverage | Gap |
|-----------|-----------------|-----|
| C-22 Decision inversion framing | DEFAULT DECISION POSITION block present in V-04 and V-05; REAL-REQUIRED as null result; MOCK-ACCEPTED as earned result stated in block | R5 V-01/V-02/V-03 fail C-22 (no inversion block). The R6 rubric formalizes C-22 as the criterion that V-04/V-05 introduced. Single-axis R6 test: does the inversion block alone (without the contrastive template) produce C-20-quality rationale, or does the inversion require the template to be effective? R5 left this open: V-04 has inertia framing without the two-slot template and was expected to yield C-20 PARTIAL — confirming that framing and template are not redundant. |
| C-23 Strategy SQ-1 anchor in structural position | STEP 6 MOCK-ACCEPTED Structural position: "The tier decision this namespace supports (from Strategy SQ-1) should appear here" | The SQ-1 reference is embedded in the slot's instructional text as "should appear here" — not a named slot label. C-23 requires "the anchor must be a named slot requirement, not an example." A slot whose label is `Structural position (Strategy SQ-1 tier decision):` makes the SQ-1 answer a named field requirement. R5 V-05's instruction is still advisory; the slot label change makes it structural. This is a narrow output-format change that a model cannot satisfy by ignoring the label. |
| C-24 Artifact state field propagation | STEP 7 Priority 1/2 format: "/{skill-id} {topic} — {artifact state from Artifact state field if eval-driven}" | The `if eval-driven` conditional is correct but ambiguous — the author must select format based on entry type, and a missed conditional produces an entry naming only the skill and topic. C-24 requires unconditional propagation for eval-driven entries. Providing two explicit format sub-templates (eval-driven: Artifact state required; auto-flagged: trigger required) removes the conditional and makes propagation a named format requirement, not an optional instruction. |

R5 recommendation for R6: Verify C-22 in isolation (inertia framing without contrastive
template). Close C-23 with a labeled slot change. Close C-24 with two explicit format
sub-templates in STEP 7.

---

## Axis-Assignment Plan

| Plan | Axis | Source signal | Target criteria | Predicted |
|------|------|--------------|-----------------|-----------|
| V-01 | inertia-framing | R5 V-04 established DEFAULT DECISION POSITION combined with Strategy-first ordering — two variables changed simultaneously. V-01 isolates the inertia block from role ordering: PM-first with DEFAULT DECISION POSITION only. Does the inversion block alone (no two-slot template) produce C-20-quality rationale? | C-22 | C-22 PASS (named block present). C-20 PARTIAL — inertia framing changes evaluator posture but single Rationale slot still allows confirmatory escape. C-23/C-24 FAIL (no labeled slot, no explicit sub-templates). Failure condition: C-20 behaves identically to R5 V-01 (no improvement from framing alone), confirming the two-slot template is the load-bearing structure for C-20. |
| V-02 | output-format | R5 V-05 Structural position slot label is generic. V-02 changes it to `Structural position (Strategy SQ-1 tier decision):`, making the SQ-1 answer a named slot requirement. No inertia framing. PM-first. Two-slot contrastive template with C-23 label change. | C-23 | C-23 PASS (labeled slot requirement). C-22 FAIL (no inversion block). C-20 improvement: labeled slot forces SQ-1 decision name and type classification before Contrast slot is written. Failure condition: author fills labeled slot with SQ-1 answer verbatim without classifying it as STRUCTURAL-FORM vs TIER-GATING — satisfying slot syntax without the type discrimination C-23 requires. |
| V-03 | lifecycle-emphasis | R5 V-05 STEP 7 uses a single conditional format template. V-03 replaces it with two explicit format sub-templates: eval-driven entries require Artifact state field (unconditional); auto-flagged entries use trigger value. Removes the `if eval-driven` conditional entirely. | C-24 | C-24 PASS (explicit eval-driven sub-template with no conditional). C-22/C-23 FAIL. Failure condition: author applies the auto-flagged format to an evaluation-driven entry — the two sub-templates help but cannot prevent selection errors. |
| V-04 | output-format + lifecycle-emphasis | V-02 labeled SQ-1 anchor slot (C-23) + V-03 explicit propagation sub-templates (C-24). Strategy-first ordering (SQ-1 answer available before MOCK-ACCEPTED decision is written). Contrastive two-slot template. Artifact state field with grammar spec. No DEFAULT DECISION POSITION. | C-23, C-24 | C-23 PASS, C-24 PASS, C-22 FAIL. C-20 improvement: labeled SQ-1 + Strategy-first means decision is named before rationale is written. Failure condition: no inertia framing — author may name the SQ-1 decision correctly and still write a confirmatory Contrast sentence. |
| V-05 | inertia-framing + output-format + lifecycle-emphasis | V-01 DEFAULT DECISION POSITION + V-02 labeled SQ-1 anchor + V-03 explicit sub-templates. Strategy-first. All R5 V-05 ceiling criteria preserved. The three axes are mutually reinforcing: inertia framing establishes the escape context; labeled SQ-1 slot anchors the escape to a specific decision; explicit sub-templates carry the decision evidence into next-steps unconditionally. | C-22, C-23, C-24 | All three new criteria PASS. C-20 and C-21 inherited from R5 V-05. All prior ceiling criteria preserved. Failure condition: labeled SQ-1 + inertia framing produces category-level contrast rather than specific-decision-level contrast. |

---

## V-01 — Inertia Framing Isolation

**axis:** inertia-framing
**hypothesis:** R5 V-04 introduced DEFAULT DECISION POSITION combined with Strategy-first
ordering — both changed simultaneously, making the effects inseparable. V-01 uses PM-first
ordering and adds only the DEFAULT DECISION POSITION block. The test: does the inversion
block alone (no two-slot template) change MOCK-ACCEPTED rationale from confirmatory to
contrastive? If V-01 achieves C-20 PARTIAL, framing aids but the two-slot template is
required for the guarantee. If V-01 achieves C-20 PASS, the inversion block alone is
sufficient. Expected: C-20 PARTIAL; C-22 PASS. Secondary question: does the REAL-REQUIRED
default framing in SQ-3s produce more diagnosis-specific answers than standard SQ-3 phrasing?

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace in this review begins as REAL-REQUIRED. This is the starting state —
  not a finding, not a judgment. MOCK-ACCEPTED is an earned outcome. A namespace earns
  MOCK-ACCEPTED only when all three role evaluations (PM, Architect, Strategy) actively
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

STEP 3 — PM EVALUATION (non-auto namespaces only)

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
DO NOT proceed to STEP 4 until PM verdicts are written for every remaining namespace.

---

STEP 4 — ARCHITECT EVALUATION (non-auto namespaces only)

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
DO NOT proceed to STEP 5 until Architect verdicts are written for every remaining namespace.

---

STEP 5 — STRATEGY EVALUATION (non-auto namespaces only)

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
DO NOT proceed to STEP 6 until Strategy verdicts are written for every remaining namespace.

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
positions. This is the canonical format. Free-form text mentioning the rule name outside
this field position does not satisfy the trigger field requirement.

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Rationale: [One sentence stating what this namespace demonstrated that earned escape
    from its REAL-REQUIRED default position. Name what this namespace has (or lacks)
    compared to a namespace that remains REAL-REQUIRED — include the tier decision it
    supports (from Strategy SQ-1) and explain why that decision type does not require
    real evidence. A sentence that only confirms sufficiency without explaining the
    escape from default is a confirmatory echo and does not satisfy this slot.]

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

  Next Steps — use this pre-printed skeleton. Fill all four sections. Do not collapse
  or reorder the sections. If a section has no entries, write "(none)" — do not omit.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* namespaces first, then scout-feasibility, then listen-* and scout-competitors.
     Format: /{skill-id} {topic} — {one-line reason citing sub-question answer if eval-driven}]

    Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    [All non-critical, non-evidence-heavy REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — {one-line reason citing sub-question answer if eval-driven}]

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

## V-02 — Strategy SQ-1 Labeled Slot Anchor

**axis:** output-format
**hypothesis:** R5 V-05's Structural position slot contains "(from Strategy SQ-1) should
appear here" as embedded instructional text inside the slot body. C-23 requires the anchor
to be a named slot requirement — the slot LABEL must name Strategy SQ-1 as the source,
not the body text. Changing the label from `Structural position:` to `Structural position
(Strategy SQ-1 tier decision):` makes SQ-1 a structural field requirement: the label
tells the author exactly what to fill in (the SQ-1 answer and its decision type
classification), making a generic structural adequacy statement structurally unsatisfiable.
No inertia framing. PM-first ordering. Expected: C-23 PASS (labeled slot requirement);
C-22 FAIL (no inversion block); C-20 improvement (labeled slot forces decision-specific
Structural position sentence, anchoring the Contrast sentence). Failure condition: author
fills the labeled slot with the SQ-1 answer verbatim without classifying it as STRUCTURAL-
FORM vs TIER-GATING — satisfying slot syntax while missing the type discrimination C-23
requires.

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
  SQ-3: Name one structural gap that would prevent a PM from accepting this as Tier
        {tier} coverage (or: "No gap identified").

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
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this mock's plausibility.

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
  SQ-3: Name the coverage gap that would affect a Tier {tier} commitment
        (or: "No gap identified").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 until Strategy verdicts are written for every remaining namespace.

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
positions. This is the canonical format. Free-form text mentioning the rule name outside
this field position does not satisfy the trigger field requirement.

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Structural position (Strategy SQ-1 tier decision): [State the specific Tier {tier}
    decision from Strategy SQ-1 that this namespace supports. Classify it: state whether
    it is a STRUCTURAL-FORM decision (structural mock is sufficient; no tier-boundary
    validation required) or a TIER-GATING decision (real evidence required; mock cannot
    validate). Do not write a general adequacy statement — the slot label names Strategy
    SQ-1 as the required input and type classification as the required output.
    E.g.: "SQ-1: {decision name} — type: STRUCTURAL-FORM — this namespace supports a
    decision about the artifact's form, not about live system behavior at tier boundaries."]
  Contrast: [Name a namespace type that WOULD require real evidence and state the structural
    factor it has that this namespace does not. Must name BOTH a namespace type AND a
    structural factor. E.g.: "Unlike trace-* namespaces, which carry tier-gating decisions
    that require live architectural evidence at tier transitions, this namespace's outputs
    are fully determined by their structural form."]

  Template errors:
  - Structural position (Strategy SQ-1 tier decision) filled with a generic adequacy
    statement without the SQ-1 decision name and type classification is a SLOT-LABEL
    VIOLATION — the slot label names SQ-1 as the required input.
  - Contrast filled with "unlike evidence-heavy namespaces" without naming a structural
    factor is a CATEGORY ECHO. Both are named template errors.

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

  Next Steps — use this pre-printed skeleton. Fill all four sections. Do not collapse
  or reorder the sections. If a section has no entries, write "(none)" — do not omit.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* namespaces first, then scout-feasibility, then listen-* and scout-competitors.
     Format: /{skill-id} {topic} — {one-line reason citing sub-question answer if eval-driven}]

    Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    [All non-critical, non-evidence-heavy REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — {one-line reason citing sub-question answer if eval-driven}]

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

## V-03 — Explicit Artifact State Propagation Sub-Templates

**axis:** lifecycle-emphasis
**hypothesis:** R5 V-05 STEP 7 uses a single conditional format template: "/{skill-id}
{topic} — {artifact state from Artifact state field if eval-driven}". The conditional
`if eval-driven` is correct but ambiguous — the author must decide which format to apply
based on the entry's decision type, and a missed conditional produces an entry naming only
the skill and topic. C-24 requires unconditional propagation for eval-driven entries.
Replacing the conditional with two explicit format sub-templates — eval-driven (Artifact
state required, no conditional) and auto-flagged (trigger required, no artifact state) —
removes the ambiguity. No inertia framing. No labeled SQ-1 slot. PM-first ordering.
Expected: C-24 PASS (explicit eval-driven sub-template); C-22/C-23 FAIL. Failure condition:
author applies the auto-flagged format to an evaluation-driven entry — the sub-templates
help but cannot prevent entry-type selection errors when the entry is in a critical namespace
that happens to be evaluation-driven rather than auto-flagged.

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
  SQ-3: Name one structural gap that would prevent a PM from accepting this as Tier
        {tier} coverage (or: "No gap identified").

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
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this mock's plausibility.

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
  SQ-3: Name the coverage gap that would affect a Tier {tier} commitment
        (or: "No gap identified").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Complete Strategy evaluation for ALL remaining namespaces.
DO NOT proceed to STEP 6 until Strategy verdicts are written for every remaining namespace.

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
positions. This is the canonical format. Free-form text mentioning the rule name outside
this field position does not satisfy the trigger field requirement.

**Artifact state citation grammar:** The `Artifact state` field requires present-tense
artifact-state form. The artifact is the grammatical subject. The verb is present tense.
The observable state is the object.

  Correct form (artifact as subject, present tense):
    "Section 3.2 lists no fallback path for this namespace."
    "Table Y contains no tier-boundary gate."
    "The mock artifact shows no compliance-signal field."

  Verdict echo (role as subject) — named error — DO NOT USE:
    "Architect found no fallback path." [subject = role, not artifact]
    "PM evaluation showed the table is absent." [subject = evaluation, not artifact]
    "Strategy determined coverage is insufficient." [subject = role action, not artifact]

  Verdict echo is detectable: the grammatical subject is a role name or evaluation noun
  (Architect, PM, Strategy, evaluation, assessment, review) rather than an artifact name.
  A verdict echo fills the Artifact state slot syntax while defeating its traceability
  purpose — the slot exists to cite observable artifact state independent of the role.

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Rationale: [One sentence: why this code applies to this specific namespace — name the
    tier decision it supports and explain why that decision type does not require real
    evidence from this namespace specifically]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Artifact state: [Present-tense artifact-state form — artifact as subject, present tense
    verb, observable state as object. Not verdict echo: do not use the evaluating role
    or evaluation noun as subject. E.g.: "Section 3.2 lists no fallback path." NOT:
    "Architect found no fallback path."]

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

  Next Steps — use this pre-printed skeleton. Fill all four sections. Do not collapse
  or reorder the sections. If a section has no entries, write "(none)" — do not omit.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* namespaces first, then scout-feasibility, then listen-* and scout-competitors.
     TWO required entry formats — select by decision type:
       Evaluation-driven entry: /{skill-id} {topic} — {Artifact state field from STEP 6 decision block}
       Auto-flagged entry:      /{skill-id} {topic} — trigger: {trigger value}
     An evaluation-driven entry that omits the Artifact state field is a traceability break.
     An auto-flagged entry that includes an Artifact state field is a format error.]

    Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    [All non-critical, non-evidence-heavy REAL-REQUIRED namespaces.
     TWO required entry formats — select by decision type:
       Evaluation-driven entry: /{skill-id} {topic} — {Artifact state field from STEP 6 decision block}
       Auto-flagged entry:      /{skill-id} {topic} — trigger: {trigger value}]

    Priority 3 — Evidence-heavy REAL-REQUIRED (sequence after Priority 1 and 2):
    [All EVIDENCE-HEAVY REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — trigger: EVIDENCE-HEAVY]

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

## V-04 — SQ-1 Anchor Slot + Explicit Propagation Sub-Templates

**axes:** output-format + lifecycle-emphasis
**hypothesis:** V-02 addresses C-23 with a labeled SQ-1 slot. V-03 addresses C-24 with
explicit eval-driven vs auto-flagged format sub-templates. Neither variation has inertia
framing. V-04 combines both structural changes. Strategy-first ordering is added because
the labeled SQ-1 slot benefits from having the Strategy SQ-1 answer recorded before the
MOCK-ACCEPTED decision is written. Combined effect: the labeled slot forces the SQ-1 answer
and type classification; the Artifact state field forces traceable evidence; the explicit
sub-templates ensure the Artifact state propagates unconditionally. No DEFAULT DECISION
POSITION block. Expected: C-23 PASS, C-24 PASS, C-22 FAIL. C-20 improvement: SQ-1 answer
in labeled slot makes the Contrast sentence more specific. Failure condition: no inertia
framing means the MOCK-ACCEPTED rationale may still be confirmatory — the author names
the SQ-1 decision correctly and classifies it, then writes "structural coverage is adequate
for this decision type" without contrasting against namespaces that would require real
evidence.

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
  SQ-3: Name the coverage gap that would affect a Tier {tier} commitment
        (or: "No gap identified").

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
  SQ-3: Name one structural gap that would prevent a PM from accepting this as Tier
        {tier} coverage (or: "No gap identified").

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
  SQ-3: Name the specific architectural fact about {topic} that most directly confirms
        or challenges this mock's plausibility.

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
positions. This is the canonical format. Free-form text mentioning the rule name outside
this field position does not satisfy the trigger field requirement.

**Artifact state citation grammar:** The `Artifact state` field requires present-tense
artifact-state form. The artifact is the grammatical subject. The verb is present tense.
The observable state is the object.

  Correct form (artifact as subject, present tense):
    "Section 3.2 lists no fallback path for this namespace."
    "Table Y contains no tier-boundary gate."
    "The mock artifact shows no compliance-signal field."

  Verdict echo (role as subject) — named error — DO NOT USE:
    "Architect found no fallback path." [subject = role]
    "PM evaluation showed the table is absent." [subject = evaluation]
    "Strategy determined coverage is insufficient." [subject = role action]

  Verdict echo is detectable: the grammatical subject is a role name or evaluation noun.
  A verdict echo defeats the traceability purpose of the Artifact state field.

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Structural position (Strategy SQ-1 tier decision): [State the specific Tier {tier}
    decision from Strategy SQ-1 that this namespace supports. Classify it: state whether
    it is a STRUCTURAL-FORM decision (structural mock is sufficient; no tier-boundary
    validation required) or a TIER-GATING decision (real evidence required). Do not write
    a general adequacy statement — the slot label names Strategy SQ-1 as the required
    input and type classification as the required output. A general statement that does
    not name the SQ-1 decision and classify its type is a SLOT-LABEL VIOLATION.]
  Contrast: [Name a namespace type that WOULD require real evidence and state the structural
    factor it has that this namespace does not. Must name BOTH a namespace type AND a
    structural factor. E.g.: "Unlike trace-* namespaces, which carry tier-gating decisions
    requiring live architectural evidence at tier transitions, this namespace's outputs are
    fully determined by their structural form."]

  Template errors:
  - Structural position filled with generic adequacy statement without SQ-1 decision name
    and type classification = SLOT-LABEL VIOLATION.
  - Contrast filled with category name without structural factor = CATEGORY ECHO.

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Artifact state: [Present-tense artifact-state form — artifact as subject, present tense,
    observable state as object. Not verdict echo: subject must be an artifact name, not a
    role name or evaluation noun. E.g.: "Section 3.2 lists no fallback path." NOT:
    "Architect found no fallback path."]

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

  Next Steps — use this pre-printed skeleton. Fill all four sections. Do not collapse
  or reorder the sections. If a section has no entries, write "(none)" — do not omit.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* namespaces first, then scout-feasibility, then listen-* and scout-competitors.
     TWO required entry formats — select by decision type:
       Evaluation-driven entry: /{skill-id} {topic} — {Artifact state field from STEP 6 decision block}
       Auto-flagged entry:      /{skill-id} {topic} — trigger: {trigger value}
     An evaluation-driven entry that omits the Artifact state field is a traceability break.
     An auto-flagged entry that includes an Artifact state field is a format error.]

    Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    [All non-critical, non-evidence-heavy REAL-REQUIRED namespaces.
     TWO required entry formats — select by decision type:
       Evaluation-driven entry: /{skill-id} {topic} — {Artifact state field from STEP 6 decision block}
       Auto-flagged entry:      /{skill-id} {topic} — trigger: {trigger value}]

    Priority 3 — Evidence-heavy REAL-REQUIRED (sequence after Priority 1 and 2):
    [All EVIDENCE-HEAVY REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — trigger: EVIDENCE-HEAVY]

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

## V-05 (Ceiling) — Inertia Framing + SQ-1 Anchor Slot + Explicit Propagation

**axes:** inertia-framing + output-format + lifecycle-emphasis
**hypothesis:** V-01 DEFAULT DECISION POSITION establishes the escape context (C-22). V-02
labeled SQ-1 anchor anchors the escape to a specific decision (C-23). V-03 explicit sub-
templates carry the decision evidence into next-steps unconditionally (C-24). The three axes
are mutually reinforcing: inertia framing asks "what does this namespace have that earns
escape from REAL-REQUIRED?"; the labeled SQ-1 slot forces the answer to name the specific
tier decision and classify its type; the Contrast slot then explains why that decision type
does not require real evidence while naming namespace types that do; the Artifact state field
grounds REAL-REQUIRED decisions in observable artifact state; the explicit sub-templates
propagate that observable state into the next-steps entries unconditionally.

All R5 V-05 ceiling criteria preserved:
- C-09: pre-printed next-steps skeleton with mandatory cross-namespace risk statement
- C-11: forbidden-output enumeration in all three auto-rules
- C-12: zero-remaining confirmation gate
- C-13: separately completable role steps with inter-step STOP gates
- C-14: SQ citation slot (now Artifact state field with positive form — C-21)
- C-15: entity-naming sub-question grammar
- C-16: canary output with CANARY-FALSE-POSITIVE named error
- C-17: named contamination error (auto-rule contamination)
- C-18: all gates forward-name next step (DO NOT proceed to STEP N+1)
- C-19: unified trigger = notation in canonical format

New ceiling criteria added in R6:
- C-22: DEFAULT DECISION POSITION block at skill level (V-01 axis)
- C-23: Structural position slot labeled with SQ-1 anchor as named slot requirement (V-02 axis)
- C-24: Explicit eval-driven format sub-template in STEP 7 (V-03 axis)

Expected: C-22 PASS, C-23 PASS, C-24 PASS. C-20 and C-21 inherited from R5 V-05.
Failure conditions: (1) labeled SQ-1 slot + inertia framing produces category-level Contrast
("unlike tier-gating namespaces") rather than specific-decision-level Contrast ("unlike
trace-* whose SQ-1 names a Tier 2 adoption gate that mock cannot validate because it
depends on live component state at the tier boundary"); (2) inertia framing introduces
MOCK-ACCEPTED reluctance — MOCK-ACCEPTED rate drops significantly vs V-02/V-03 under the
same mock artifact, indicating evaluator bias rather than genuine coverage gaps.

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
positions. This is the canonical format. Free-form text mentioning the rule name outside
this field position does not satisfy the trigger field requirement.

**Artifact state citation grammar:** The `Artifact state` field requires present-tense
artifact-state form. The artifact (a section, table, field, or element in the mock) is
the grammatical subject. The verb is present tense. The observable state is the object.

  Correct form (artifact as subject, present tense):
    "Section 3.2 lists no fallback path for this namespace."
    "Table Y contains no tier-boundary gate."
    "The mock artifact shows no compliance-signal field."

  Verdict echo (role as subject) — named error — DO NOT USE:
    "Architect found no fallback path." [subject = role, not artifact]
    "PM evaluation showed the table is absent." [subject = evaluation, not artifact]
    "Strategy determined coverage is insufficient." [subject = role action, not artifact]

  Verdict echo is detectable: the grammatical subject is a role name or evaluation noun
  (Architect, PM, Strategy, evaluation, assessment, review) rather than an artifact name.
  A verdict echo fills the Artifact state slot syntax while defeating its traceability
  purpose — the slot exists to cite observable artifact state so the decision is traceable
  to the mock artifact independent of the role that reviewed it.

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
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
    required output. Do not write a general adequacy statement ("structural coverage is
    sufficient here") — that is a SLOT-LABEL VIOLATION: the slot label requires the SQ-1
    decision name and its type classification.
    E.g.: "SQ-1: {specific decision name} — type: STRUCTURAL-FORM — this namespace
    supports a decision about the artifact's structural form; no tier-boundary validation
    is required because the decision does not depend on live architectural state."]
  Contrast: [Name a namespace type that WOULD require real evidence and state the structural
    factor it has that this namespace does not. Must name BOTH a namespace type AND a
    structural factor — not merely a category. E.g.: "Unlike trace-* namespaces, which
    carry tier-gating decisions that require live architectural evidence because those
    decisions depend on component state at tier transitions, this namespace's outputs are
    fully determined by their structural form and do not depend on runtime state."]

  Template errors:
  - Structural position (Strategy SQ-1 tier decision) filled with generic adequacy
    statement without the SQ-1 decision name and type classification is a SLOT-LABEL
    VIOLATION.
  - Contrast filled with "unlike evidence-heavy namespaces, this namespace is structural"
    names a category but not a structural factor. Both are named template errors; neither
    satisfies this template.

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}
  Failing evaluation: [Strategy | PM | Architect]
  Failing verdict: [INSUFFICIENT FOR TIER N | STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS]
  Artifact state: [Present-tense artifact-state form. The artifact is the grammatical
    subject. The verb is present tense. The observable state is the object.
    E.g.: "Section 3.2 lists no fallback path for this namespace."
    NOT verdict echo: "Architect found no fallback path." — that form names the role
    action, not the artifact state. Verdict echo is detectable: the subject is a role
    name or evaluation noun, not an artifact name.]

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

  Next Steps — use this pre-printed skeleton. Fill all four sections. Do not collapse
  or reorder the sections. If a section has no entries, write "(none)" — do not omit.

    Ordering rule: "Critical first, evidence-heavy last."

    Priority 1 — Critical REAL-REQUIRED (blocker for Tier {tier} commit):
    [trace-* namespaces first, then scout-feasibility, then listen-* and scout-competitors.
     TWO required entry formats — select by decision type:
       Evaluation-driven entry: /{skill-id} {topic} — {Artifact state field from STEP 6 decision block}
       Auto-flagged entry:      /{skill-id} {topic} — trigger: {trigger value}
     An evaluation-driven entry that omits the Artifact state field is a traceability break.
     An auto-flagged entry that includes an Artifact state field is a format error.]

    Priority 2 — Non-critical REAL-REQUIRED (required before Tier {tier} commit):
    [All non-critical, non-evidence-heavy REAL-REQUIRED namespaces.
     TWO required entry formats — select by decision type:
       Evaluation-driven entry: /{skill-id} {topic} — {Artifact state field from STEP 6 decision block}
       Auto-flagged entry:      /{skill-id} {topic} — trigger: {trigger value}]

    Priority 3 — Evidence-heavy REAL-REQUIRED (sequence after Priority 1 and 2):
    [All EVIDENCE-HEAVY REAL-REQUIRED namespaces.
     Format: /{skill-id} {topic} — trigger: EVIDENCE-HEAVY]

    Cross-namespace risk statement:
    [Required output. Name the single highest-risk coverage gap — the REAL-REQUIRED namespace
     whose absence most threatens a Tier {tier} decision. State the specific Tier {tier}
     decision at risk. Assign urgency: BLOCKING (must resolve before any Tier {tier} work
     begins) | HIGH (resolve within current sprint) | MEDIUM (resolve before Tier {tier}
     commit).
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

## Variation Map Summary

| V | Axes | What Changed from R5 V-05 | Target Criteria | Hypothesis |
|---|------|--------------------------|-----------------|------------|
| V-01 | inertia-framing | DEFAULT DECISION POSITION block preserved from R5 V-04/V-05; PM-first ordering (removes role-sequence variable); SQ-3 for all three roles framed as "gap that would keep in REAL-REQUIRED default position"; MOCK-ACCEPTED Rationale slot framed as "earned escape from REAL-REQUIRED default"; single Rationale slot (no two-slot template); no Artifact state field | C-22 | Tests whether inversion block alone (without two-slot template) produces C-20-quality rationale; isolates inertia framing from role ordering; expected C-22 PASS, C-20 PARTIAL — framing aids but single Rationale slot allows confirmatory escape |
| V-02 | output-format | Structural position slot label changed from generic to `Structural position (Strategy SQ-1 tier decision):`; SLOT-LABEL VIOLATION named as a detectable error; CATEGORY ECHO named for Contrast slot; two-slot template preserved from R5 V-02/V-05; no DEFAULT DECISION POSITION; PM-first ordering; no Artifact state field | C-23 | Tests whether slot-label SQ-1 anchor (named slot requirement rather than instructional text) closes C-23; expected C-23 PASS, C-22 FAIL; failure condition: author fills labeled slot with SQ-1 answer verbatim without type classification |
| V-03 | lifecycle-emphasis | STEP 7 conditional format template replaced with two explicit sub-templates (eval-driven: Artifact state required; auto-flagged: trigger required); traceability break named as detectable error for misapplied format; Artifact state field with present-tense grammar spec inherited from R5 V-03; no DEFAULT DECISION POSITION; no labeled SQ-1 slot; PM-first ordering | C-24 | Tests whether explicit sub-templates (no conditional) close C-24; expected C-24 PASS, C-22/C-23 FAIL; failure condition: author applies auto-flagged format to eval-driven entry in critical namespace |
| V-04 | output-format + lifecycle-emphasis | V-02 labeled SQ-1 anchor slot + V-03 explicit sub-templates; Strategy-first ordering added (SQ-1 answer available before MOCK-ACCEPTED decision is written); Artifact state field with grammar spec; full two-slot contrastive template; no DEFAULT DECISION POSITION | C-23, C-24 | Tests C-23 + C-24 together; Strategy-first ordering provides SQ-1 answer before MOCK-ACCEPTED decision; expected C-23/C-24 PASS, C-22 FAIL; failure condition: no inertia framing means MOCK-ACCEPTED rationale may still be confirmatory despite correct SQ-1 answer in slot |
| V-05 | inertia-framing + output-format + lifecycle-emphasis | DEFAULT DECISION POSITION block (C-22) + labeled SQ-1 anchor slot (C-23) + explicit sub-templates (C-24); Strategy-first ordering; all R5 V-05 ceiling criteria preserved (C-09 through C-21); SLOT-LABEL VIOLATION and CATEGORY ECHO named; traceability break named in STEP 7; Artifact state grammar spec with verdict-echo detection; inertia framing in all three role SQ-3s; inertia escape framing in MOCK-ACCEPTED rationale guidance | C-22, C-23, C-24 | Ceiling combination: all three new v6 criteria addressed through structural guarantees; inertia framing establishes the escape context; labeled SQ-1 slot anchors the escape to a specific decision with type classification; explicit sub-templates carry the decision evidence into next-steps unconditionally; failure conditions: (1) category-level Contrast despite labeled slot; (2) MOCK-ACCEPTED reluctance bias under inertia framing |

**Top combination candidate for Round 7:**
If V-05 achieves the expected composite (C-22/C-23/C-24 all PASS), the residual open
question is the C-20 Contrast quality under the labeled SQ-1 slot: does the type
classification requirement ("STRUCTURAL-FORM vs TIER-GATING") in the Structural position
slot produce Contrast sentences that name the specific architectural property that makes
a TIER-GATING namespace incompatible with mock, or does it produce generic type-label
contrasts ("unlike TIER-GATING namespaces")? A focused R7 test would target the type
classification grammar in the Structural position slot — requiring the author to name
not just the type label but the architectural property that determines the type (e.g.,
"TIER-GATING because the decision requires observing component state at the tier boundary,
which mock cannot produce"). This would close any remaining C-20 gap at the type-
specificity level and complete the traceability chain from SQ-1 decision name through
type classification through Contrast through Artifact state into next-steps.
