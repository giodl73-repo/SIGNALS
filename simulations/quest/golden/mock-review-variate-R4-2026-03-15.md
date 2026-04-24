---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 4
rubric_version: v4
status: VARIATE
---

# mock-review Variate — Round 4

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v4 (C-01 through C-19; aspirational denominator = 11)
**Round:** R4 — targeting v4 new criteria: C-17, C-18, C-19

---

## What R3 Left Open

R3 V-05 (the ceiling) combined five structural guarantees: entity-naming sub-question grammar
(C-15), sub-question answer citation template (C-14), canary confirmation framing (C-16),
forbidden-output enumeration for all three rules (C-11), and separately completable role steps
with STOP gates (C-13). Three new aspirational criteria were introduced in v4 based on patterns
visible in R3 V-04 and V-01 that were present but not fully formalized:

| Criterion | Best R3 V-05 coverage | Gap |
|-----------|----------------------|-----|
| C-17 Auto-flagged contamination guard | STEP 2: "DO NOT apply PM, Architect, or Strategy evaluation to any auto-flagged namespace." | The prohibition is present but the contamination error has no name. C-17 requires "names the contamination error itself" — separating phases without naming the error does not satisfy the criterion. A reviewer can detect the prohibition but cannot diagnose a violation by label. The gap: R3 V-05 never says "this is a named error: auto-rule contamination." |
| C-18 Inter-step gate with next-step reference | Role steps (3→4, 4→5): "DO NOT proceed to Step 4 until PM verdicts..." — names next step ✓. Auto-flag phase (2): "DO NOT proceed until every namespace is placed in exactly one list" — does not name STEP 3 ✗. Read phase (1): "DO NOT proceed until all namespace fields are extracted" — does not name STEP 2 ✗. | C-18 says "gates name the specific next step being blocked." R3 V-05's role-to-role gates already pass; the READ and AUTO-FLAG gates do not forward-name their next step. Whether C-18 targets all gates or only role-step gates is ambiguous — the conservative reading is all gates must name the next step. R4 V-02 resolves the ambiguity by naming next step in all eight gate positions. |
| C-19 Structured trigger notation | Auto-flag listing uses `trigger = {label}` ✓. Decision block template uses `Trigger: [label]` (colon notation, uppercase T) ✗. | Two notations co-exist: `trigger = ` in listing context, `Trigger: ` in template context. C-19 requires "a named, parseable template field in a fixed position" with a single canonical notation. A parser processing the output would need to handle two formats. R4 V-03 unifies to `trigger = {label}` everywhere and adds a structural field note making the position and enumeration explicit. |

R3 recommendation for R4 (bottom of R3 file): "A focused R4 variation isolating the Next
Steps section — pre-printing the Priority 1/2/3 headers as a skeleton similar to R2 V-05's
PHASE 7 — is worth testing as a single axis against the ceiling combination." This addresses
the C-05 ordering regression risk when evaluation phases are long. Incorporated into V-05 as
a ceiling strengthening; also targets C-09 (coverage gap synthesis with cross-namespace risk
statement).

---

## Axis-Assignment Plan

| Plan | Axis | Source signal | Target criteria | Predicted |
|------|------|---------------|-----------------|-----------|
| V-01 | lifecycle-emphasis | C-17 gap: contamination guard present in R3 V-05 STEP 2 but error has no name | C-17, C-02 | Named error "auto-rule contamination" added; violation is diagnosable by label; C-17 passes as named error not just prohibition |
| V-02 | lifecycle-emphasis | C-18 gap: READ and AUTO-FLAG gates do not forward-name next step; role-step gates do | C-18, C-13 | All eight gate positions updated to name the specific next step; conservative interpretation covered; C-18 passes across all phase transitions |
| V-03 | output-format | C-19 gap: two trigger notations co-exist (`trigger = ` in listing, `Trigger:` in template); field not mechanically verifiable from single format | C-19, C-06 | Unified `trigger = {label}` in all positions; evaluation-driven REAL-REQUIRED template adds `trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}`; structural field note makes enumeration and position explicit |
| V-04 | lifecycle-emphasis × 2 | C-17 + C-18 combined: both named error and all-gate forward naming | C-17, C-18, C-02, C-13 | Named contamination error + all gates name next step; both criteria addressed structurally; the two lifecycle changes do not conflict |
| V-05 | lifecycle-emphasis + output-format + next-steps-skeleton | C-17 + C-18 + C-19 on top of R3 V-05 base; pre-printed next-steps skeleton addresses C-09 and guards against C-05 ordering regression under long evaluation phases | C-17, C-18, C-19, C-09; preserve C-11 through C-16 from R3 V-05 | Ceiling combination: all three new criteria addressed through structural guarantees; C-09 addressed through pre-printed skeleton with mandatory cross-namespace risk statement |

---

## V-01 — Named Contamination Error

**axis:** lifecycle-emphasis
**hypothesis:** R3 V-05 STEP 2 introduced the prohibition "DO NOT apply PM, Architect, or
Strategy evaluation to any auto-flagged namespace." This is a behavioral rule. C-17 requires
more: the contamination scenario must have a name. A named error is diagnosable — a reviewer
auditing the output can ask "is auto-rule contamination present?" and answer by inspection,
because a contaminated decision visibly carries both a trigger label and an evaluation verdict.
R3 V-05's prohibition is a rule; C-17's requirement is that violating the rule constitutes a
named, identifiable error state. The change is minimal: one sentence appended to the guard.
Expected improvement: C-17 PASS (contamination error named with label "auto-rule
contamination"; violation described as detectable by inspection). C-02 improvement (the hard
gate now describes what enforcement failure looks like, not just what the rule is). Failure
condition: if the model produces a REAL-REQUIRED decision that cites both a trigger and an
evaluation verdict but does not label it as auto-rule contamination — the name is present in
the prompt but not applied in the output — the naming alone is insufficient and an output
template field for contamination detection is needed.

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
DO NOT proceed until all namespace header fields are extracted and listed.

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
  - {namespace}: trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

  Remaining (awaiting evaluation):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

DO NOT proceed until every namespace is placed in exactly one list.

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
DO NOT proceed to Step 4 until PM verdicts are written for every remaining namespace.

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
DO NOT proceed to Step 5 until Architect verdicts are written for every remaining namespace.

---

STEP 5 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Strategy verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would affect a Tier {tier} commitment (or: "No gap identified").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

---

STEP 6 — DECISIONS WITH CITATION

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Rationale: [One sentence: why this code applies to this specific namespace]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Sub-question answer that drove this verdict: "[The exact SQ answer — name the specific
    section, element, gap, or decision; not a restatement of the verdict]"

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  Trigger: [EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE]

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md:

  Header: Topic | Tier used | Date
  Coverage Review table:
    | Namespace | Category | Decision | Trigger / Reason Code |
    One row per namespace; all namespaces from Steps 2 and 6.
  Next Steps (numbered, strict priority):
    Priority 1: REAL-REQUIRED critical namespaces: trace-* first, scout-feasibility, listen-*
    Priority 2: REAL-REQUIRED non-critical namespaces
    Priority 3: REAL-REQUIRED evidence-heavy namespaces
    Ordering rule stated: "Critical first, evidence-heavy last."
    Format: /{skill-id} {topic} — {one-line reason; for evaluation-driven: cite the sub-question answer}

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

MUST update every Status line in {mock-artifact-path}.
Use Edit tool. In-place replacement only. Do not rewrite any other content.

For each namespace:
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  OR:      Status: REAL-REQUIRED [{trigger or evaluation reason}]

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

## V-02 — All-Gate Forward Naming

**axis:** lifecycle-emphasis
**hypothesis:** R3 V-05's role-step gates (STEP 3→4, STEP 4→5) already name the specific
next step: "DO NOT proceed to Step 4 until PM verdicts are written." C-18 is satisfied for
those two transitions. The gap is that the READ and AUTO-FLAG completion gates do not name
the next step: STEP 1 says "DO NOT proceed until all namespace fields are extracted" (missing
"to STEP 2"); STEP 2 says "DO NOT proceed until every namespace is placed in exactly one
list" (missing "to STEP 3"). Additionally, STEP 5, STEP 6, and STEP 7 each end without
forward-naming the next step. The conservative reading of C-18 is that every gate must
forward-name — not just role-evaluation gates. This variation applies the forward-naming
pattern to all eight gate positions in the skill. Expected improvement: C-18 PASS (all gate
instructions name the specific next step they block). C-13 improvement (role-step separation
gates are more actionable — a model that misunderstands its current step can identify the
next step from the gate text alone). Failure condition: if C-18 is intended only for
"role-step completion gates" (STEP 3, 4, 5 specifically), then this variation passes C-18
vacuously while R3 V-05 already passed the narrower reading — in which case V-02 and V-01
are the more discriminating tests.

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

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

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

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Rationale: [One sentence: why this code applies to this specific namespace]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Sub-question answer that drove this verdict: "[The exact SQ answer — name the specific
    section, element, gap, or decision; not a restatement of the verdict]"

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  Trigger: [EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE]

Complete all namespace decision templates.
DO NOT proceed to STEP 7 until every namespace has a completed decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md:

  Header: Topic | Tier used | Date
  Coverage Review table:
    | Namespace | Category | Decision | Trigger / Reason Code |
    One row per namespace; all namespaces from Steps 2 and 6.
  Next Steps (numbered, strict priority):
    Priority 1: REAL-REQUIRED critical namespaces: trace-* first, scout-feasibility, listen-*
    Priority 2: REAL-REQUIRED non-critical namespaces
    Priority 3: REAL-REQUIRED evidence-heavy namespaces
    Ordering rule stated: "Critical first, evidence-heavy last."
    Format: /{skill-id} {topic} — {one-line reason; for evaluation-driven: cite the sub-question answer}

DO NOT proceed to STEP 8 until the review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

MUST update every Status line in {mock-artifact-path}.
Use Edit tool. In-place replacement only. Do not rewrite any other content.

For each namespace:
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  OR:      Status: REAL-REQUIRED [{trigger or evaluation reason}]

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

## V-03 — Unified Trigger Field Notation

**axis:** output-format
**hypothesis:** R3 V-05 uses two notations for the trigger field: `trigger = {label}` in the
auto-flag listing context (Step 2 output) and `Trigger: [label]` in the decision block
template (Step 6). C-19 requires "a named, parseable template field in a fixed position" that
"can be mechanically verified." A field that appears in two formats — different capitalization,
different separator character — is not mechanically parseable with a single rule. A parser
processing the output would need to match both `trigger = ` at list positions and `Trigger: `
at template positions. Unifying to `trigger = {label}` in every position, combined with an
explicit structural field note, makes the field canonically parseable: one format, one
position, one enumeration. Additionally, R3 V-05's evaluation-driven REAL-REQUIRED template
has no trigger field at all — it uses "Failing evaluation: [PM | Architect | Strategy]" which
is a different field name. Adding `trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}`
to the evaluation-driven template completes the field coverage across all decision types.
Expected improvement: C-19 PASS (unified `trigger = ` notation; structural field note names
position and enumeration; all decision types carry the trigger field). C-06 improvement
(evaluation-driven REAL-REQUIRED decisions now carry a parseable trigger alongside the
sub-question citation). Failure condition: if the model uses the canonical notation during the
decision blocks but reverts to prose in the coverage review table trigger column, the field is
present in templates but not tables — C-19 requires the field to be in the decision output
block, not just the review table.

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
DO NOT proceed until all namespace header fields are extracted and listed.

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

Output two lists before proceeding:
  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = EVIDENCE-HEAVY
  - {namespace}: trigger = TIER-CRITICAL
  - {namespace}: trigger = COMPLIANCE

  Remaining (awaiting evaluation):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

DO NOT proceed until every namespace is placed in exactly one list.

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
DO NOT proceed to Step 4 until PM verdicts are written for every remaining namespace.

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
DO NOT proceed to Step 5 until Architect verdicts are written for every remaining namespace.

---

STEP 5 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions then write the Strategy verdict.
Each sub-question requires a named artifact in the answer — not a yes/no judgment.

  SQ-1: Name the specific Tier {tier} decision this namespace is intended to support.
  SQ-2: Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether correct or incorrect).
  SQ-3: Name the coverage gap that would affect a Tier {tier} commitment (or: "No gap identified").

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

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
  Rationale: [One sentence: why this code applies to this specific namespace]

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

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md:

  Header: Topic | Tier used | Date
  Coverage Review table:
    | Namespace | Category | Decision | trigger |
    One row per namespace; all namespaces from Steps 2 and 6.
    The `trigger` column uses the same canonical notation as decision blocks.
  Next Steps (numbered, strict priority):
    Priority 1: REAL-REQUIRED critical namespaces: trace-* first, scout-feasibility, listen-*
    Priority 2: REAL-REQUIRED non-critical namespaces
    Priority 3: REAL-REQUIRED evidence-heavy namespaces
    Ordering rule stated: "Critical first, evidence-heavy last."
    Format: /{skill-id} {topic} — {one-line reason; for evaluation-driven: cite the sub-question answer}

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

## V-04 (Combined) — Named Contamination Error + All-Gate Forward Naming

**axes:** lifecycle-emphasis × 2
**hypothesis:** V-01 adds the named error label "auto-rule contamination" to the contamination
guard in STEP 2. V-02 updates all eight gate positions to forward-name the next step. The
combination tests whether these two lifecycle changes are strictly additive or whether their
interaction introduces complexity. The hypothesis: they are orthogonal — V-01's change is
localized to a single sentence appended to the STEP 2 guard; V-02's changes are localized to
gate positions at the end of each step. Neither affects the other's target location, so the
combined prompt should pass both C-17 and C-18 without trade-offs. Expected: C-17 PASS (named
error), C-18 PASS (all gates name next step), no regression on C-11 through C-16 from R3 V-05.
Failure condition: the additional gate text in STEP 2 (forward-naming STEP 3) creates
ambiguity with the contamination guard's "DO NOT proceed" language — a model might interpret
the gate as a completion condition for the contamination guard rather than for the auto-flag
phase, conflating two distinct stopping conditions at the same phase boundary.

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
  - {namespace}: trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

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

For each remaining namespace, produce a decision using the appropriate template:

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  Reason code(s): [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; both when both apply; no paraphrase; NEVER invent codes)
  Rationale: [One sentence: why this code applies to this specific namespace]

REAL-REQUIRED template (evaluation-driven):
  Decision: REAL-REQUIRED
  Failing evaluation: [PM | Architect | Strategy]
  Failing verdict: [STRUCTURALLY INCOMPLETE | CONTRADICTS KNOWN FACTS | INSUFFICIENT FOR TIER N]
  Sub-question answer that drove this verdict: "[The exact SQ answer — name the specific
    section, element, gap, or decision; not a restatement of the verdict]"

REAL-REQUIRED template (auto-flagged):
  Decision: REAL-REQUIRED
  Trigger: [EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE]

Complete all namespace decision templates.
DO NOT proceed to STEP 7 until every namespace has a completed decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md:

  Header: Topic | Tier used | Date
  Coverage Review table:
    | Namespace | Category | Decision | Trigger / Reason Code |
    One row per namespace; all namespaces from Steps 2 and 6.
  Next Steps (numbered, strict priority):
    Priority 1: REAL-REQUIRED critical namespaces: trace-* first, scout-feasibility, listen-*
    Priority 2: REAL-REQUIRED non-critical namespaces
    Priority 3: REAL-REQUIRED evidence-heavy namespaces
    Ordering rule stated: "Critical first, evidence-heavy last."
    Format: /{skill-id} {topic} — {one-line reason; for evaluation-driven: cite the sub-question answer}

DO NOT proceed to STEP 8 until the review artifact is written and confirmed.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

MUST update every Status line in {mock-artifact-path}.
Use Edit tool. In-place replacement only. Do not rewrite any other content.

For each namespace:
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  OR:      Status: REAL-REQUIRED [{trigger or evaluation reason}]

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

## V-05 (Combined) — Ceiling: C-17 + C-18 + C-19 + C-09

**axes:** lifecycle-emphasis + output-format + next-steps-skeleton
**hypothesis:** V-04 combines C-17 (named contamination error) and C-18 (all-gate forward
naming). V-03 adds C-19 (unified trigger field notation). This ceiling combination adds all
three axes. It also addresses C-09 (coverage gap synthesis) — the one unaddressed aspirational
criterion in R3 V-05. C-09 requires "a cross-namespace risk statement and urgency grouping
commentary, not just a flat priority-ordered list." The R3 recommendation for R4 was to
pre-print the Priority 1/2/3 headers as a skeleton to prevent C-05 ordering regressions under
long evaluation phases. The pre-printed skeleton is the vehicle for adding the cross-namespace
risk statement as a required output slot. Expected: C-17 PASS (named error), C-18 PASS (all
gates), C-19 PASS (unified trigger field), C-09 PASS (cross-namespace risk statement via
mandatory pre-printed slot); C-11 through C-16 from R3 V-05 preserved. Failure conditions:
(1) the cross-namespace risk statement slot is filled with a per-namespace restatement rather
than a genuine cross-namespace synthesis — C-09 requires a risk statement that spans
namespaces, not a summary of the highest-scored REAL-REQUIRED namespace; (2) the pre-printed
next-steps skeleton creates rigidity that causes a model to leave urgency groups empty rather
than adapting the skeleton to the actual namespace set.

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
positions. This is the canonical format. Free-form text mentioning the rule name outside this
field position does not satisfy the trigger field requirement.

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

## Variation Map Summary

| V | Axes | What Changed from R3 V-05 | Target Criteria | Hypothesis |
|---|------|--------------------------|-----------------|------------|
| V-01 | lifecycle-emphasis | STEP 2 contamination guard extended: "Applying role evaluation to an auto-flagged namespace is a named error: auto-rule contamination. Detectable by inspection: carries both trigger label and evaluation verdict." | C-17, C-02 | Named error transforms the prohibition from a rule into a diagnosable error state; a reviewer can ask "is auto-rule contamination present?" and answer by inspection |
| V-02 | lifecycle-emphasis | All eight gate positions updated to forward-name the specific next step: "DO NOT proceed to STEP N until..." in STEP 1, STEP 2, STEP 6, STEP 7; role-step gates already named in R3 V-05 | C-18, C-13 | Conservative interpretation of C-18 covered; a model that misidentifies its current step can locate the next step from the gate text; no ambiguity about what blocking means |
| V-03 | output-format | All trigger references unified to `trigger = {label}` notation; MOCK-ACCEPTED template adds `trigger = n/a`; evaluation-driven template adds `trigger = {PM-INCOMPLETE | ARCH-IMPLAUSIBLE | STRATEGY-INADEQUATE}`; structural field note names position and enumeration; coverage review table header renamed to `trigger` | C-19, C-06 | Canonical single-format field; field is mechanically parseable by reading `trigger = ` at a fixed line position in every decision block; two-format ambiguity in R3 V-05 resolved |
| V-04 | lifecycle-emphasis × 2 | V-01 named error + V-02 all-gate forward naming | C-17, C-18, C-02, C-13 | Both lifecycle changes are localized to non-overlapping positions; additive without conflict; tests whether named error + forward gates together introduce any comprehension cost |
| V-05 | lifecycle-emphasis + output-format + next-steps-skeleton | V-01 + V-02 + V-03 changes; pre-printed next-steps skeleton with four mandatory sections (Priority 1, 2, 3, Cross-namespace risk statement); cross-namespace risk statement slot with urgency assignment | C-17, C-18, C-19, C-09 | Ceiling combination; all three new v4 criteria addressed structurally; C-09 closed via mandatory slot in pre-printed skeleton; C-05 ordering regression risk mitigated by skeleton rigidity |

**Top combination candidate for Round 5:**
If V-05 achieves the highest composite, the residual open criteria are C-09 (if skeleton slot
is filled with per-namespace restatement rather than genuine cross-namespace synthesis) and
C-10 (MOCK-ACCEPTED namespace-specific rationale — present in R3 V-05 but not always a full
explanatory sentence). A focused R5 test would add a rationale adequacy check to the MOCK-ACCEPTED
template: the rationale sentence must explain why the reason code applies to _this_ namespace
compared to a namespace that would require real evidence, making the distinction explicit rather
than just stating the code applies.
