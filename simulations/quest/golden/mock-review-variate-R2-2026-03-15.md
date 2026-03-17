---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 2
rubric_version: v2
status: VARIATE
---

# mock-review Variate — Round 2

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v2 (C-01 through C-13; aspirational denominator = 5)
**Round:** R2 — targeting v2 new criteria (C-11, C-12, C-13)

---

## What R1 Left Open

R1 five variations covered the essential and recommended tier well. The three aspirational
criteria added in v2 were only partially addressed:

| Criterion | Best R1 coverage | Gap |
|-----------|-----------------|-----|
| C-11 Forbidden-output enumeration | V-04: DO NOT for EVIDENCE-HEAVY only | TIER-CRITICAL and COMPLIANCE rules had no forbidden-output phrasing |
| C-12 Zero-remaining confirmation gate | V-03: "Zero Status fields may remain" as a closing statement | Statement is not a required verification output — the model can write it once and skip the count |
| C-13 Verifiable role-step separation | V-04: PM/Architect/Strategy as separate STEPs | Steps lack per-role diagnostic sub-questions; combined verdict table may still satisfy the template |

R2 targets each gap with a dedicated single-axis variation, then combines them.

---

## Axis-Assignment Plan

| Plan | Axis | Source signal | Target criteria | Predicted |
|------|------|---------------|-----------------|-----------|
| V-01 | phrasing-register | C-11 gap: only one rule had forbidden-output in R1 | C-11, C-02 | All three auto-rules carry an explicit DO NOT statement naming the forbidden output pattern; C-11 passes cleanly |
| V-02 | lifecycle-emphasis | C-12 gap: statement is not a verification output | C-12, C-04 | Write-back phase ends with a mandatory VERIFY step that produces a count-and-confirm line; C-12 is machine-checkable |
| V-03 | role-sequence | C-13 gap: steps lack sub-questions and individual STOP gates | C-13, C-07 | PM, Architect, Strategy are three separately completable sections each with own heading, diagnostic questions, and Verdict line |
| V-04 | phrasing-register + role-sequence | Combine V-01 forbidden-output with V-03 verifiable steps | C-11, C-13, C-02, C-07 | Both auto-flag phase and evaluation phase enforced at the failure-pattern level simultaneously |
| V-05 | output-format + lifecycle-emphasis + role-sequence | Pre-printed template skeleton targeting C-09, C-12, C-13 as structural guarantees | C-09, C-12, C-13, C-07 | Pre-printing section headers and verification lines removes model-generation dependency; ceiling combination |

---

## V-01 — Forbidden-Output Enumeration for All Three Auto-Rules

**axis:** phrasing-register
**hypothesis:** R1 V-04 named the forbidden output for EVIDENCE-HEAVY but left TIER-CRITICAL
and COMPLIANCE as positive-only trigger statements. When all three rules carry an explicit
DO NOT statement naming the exact forbidden pattern, C-11 passes cleanly because the rubric
criterion requires forbidden-output phrasing to be "present for all three rules." A variation
that has two positive rules and one forbidden-output rule will score C-11 at PARTIAL at best.
The fix is mechanical: add the DO NOT line to each rule independently. Expected improvement:
C-11 PASS (was unrated or PARTIAL in R1); C-02 PASS maintained.
Failure condition: if C-11 scoring is not distinguished from a variation that has the positive
trigger form only, the forbidden-output phrasing is treated as redundant and adds no scoring
signal — in which case the rubric criterion requires recalibration.

---

You are running /mock:review.

**Input**

Topic: {topic}
Mock artifact: {mock-artifact-path}
Tier: {tier} — from --tier flag, TOPICS.md, or default 1

**Setup**

Read {mock-artifact-path}.
For each namespace section, extract from the MOCK ARTIFACT header block:
  Namespace name, Category (HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED), current Status

Read TOPICS.md:
  Tier for {topic} (overridden by --tier if provided)
  Compliance tags (if any)

State the tier at the top of your output:
  "Tier used: {N}  (source: TOPICS.md | --tier flag | default)"

**Phase 1 — Automatic Flagging**

Apply all three rules to every namespace before any role evaluation begins.
These rules are non-overridable. No PM, Architect, or Strategy evaluation can change
a decision made by an automatic rule.

RULE A — EVIDENCE-HEAVY (fires at all tiers):
  Condition: Category == EVIDENCE-HEAVY
  Action: REAL-REQUIRED, trigger label = EVIDENCE-HEAVY
  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED, regardless of mock quality
  or mock content depth. Evidence-heavy namespaces require real skill runs unconditionally.

RULE B — TIER-CRITICAL (fires at Tier 2 and Tier 3 only):
  Condition: tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
  Action: REAL-REQUIRED, trigger label = TIER-CRITICAL
  DO NOT mark any Tier 2+ critical namespace MOCK-ACCEPTED at any tier. The criticality
  designation is not a quality judgment on the mock — it is a structural decision that mock
  content cannot satisfy regardless of how thorough the mock artifact is.

RULE C — COMPLIANCE (fires when compliance context is active):
  Condition: TOPICS.md compliance tags present OR --compliance flag is set
  AND namespace in {scout-compliance, trace-permissions}
  Action: REAL-REQUIRED, trigger label = COMPLIANCE
  DO NOT mark any compliance-tagged namespace MOCK-ACCEPTED when compliance context is
  active. Compliance evidence cannot be fabricated; only real skill runs produce valid
  compliance signals.

After applying all three rules, output two lists before proceeding to Phase 2:

  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

  Remaining (awaiting Phase 2 evaluation):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

Every namespace must appear in exactly one list. Do not begin Phase 2 until both lists
are complete and all namespaces are placed.

**Phase 2 — Three-Role Evaluation (non-auto namespaces only)**

For each namespace in the Remaining list, evaluate across three roles:

PM — Structural completeness:
  Are required sections present? Are enforcement gates present and well-formed?
  Are tables or required output structures present and correctly formed?
  Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Architect — Technical plausibility:
  Does mock content contradict known architectural facts about {topic}?
  Are dependencies, interfaces, or system constraints consistent with {topic}?
  Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Strategy — Coverage adequacy for Tier {tier}:
  Would a team making Tier {tier} decisions be adequately served by this mock?
  Is there any decision the team might make incorrectly if this runs as MOCK-ACCEPTED?
  Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Decision:
  If all three verdicts are positive:
    MOCK-ACCEPTED — must include at least one reason code from this exact set:
      STRUCTURAL-COVERAGE-SUFFICIENT  (when structural completeness drove the verdict)
      DOMAIN-KNOWLEDGE-CONSISTENT     (when content plausibility drove the verdict)
    No paraphrase. No invented codes. Use both when both apply.
  Otherwise:
    REAL-REQUIRED — name the evaluation verdict that drove the decision.

**Phase 3 — Write Review Artifact**

Write simulations/mock/{topic}-review-{date}.md:

Section 1 — Header: Topic | Tier used | Date
Section 2 — Coverage Review table:
  | Namespace | Category | Decision | Trigger / Reason Code |
  One row per namespace. All namespaces from both Phase 1 lists.
Section 3 — Next Steps (numbered, priority order):
  Priority 1 — Critical REAL-REQUIRED: trace-* first, scout-feasibility, then listen-*
  Priority 2 — Non-critical REAL-REQUIRED namespaces
  Priority 3 — Evidence-heavy REAL-REQUIRED namespaces
  Format: /{skill} {topic} — {one-line reason}
  State the ordering rule explicitly: "Ordered by: critical namespaces first, evidence-heavy last."

**Phase 4 — Write Status Back to Source Artifact (mandatory)**

This is the defining action of /mock:review.

For every namespace in {mock-artifact-path}, use Edit to replace the Status line in-place:
  Replace: Status: MOCK (awaiting review)
  With:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  Or:      Status: REAL-REQUIRED [{trigger or evaluation reason}]

Edit the Status line only. Do not rewrite any other content in the source artifact.
This is the only permitted in-place edit in Signal.

Confirm:
  "Annotations updated in: {mock-artifact-path}"
  "Review written: simulations/mock/{topic}-review-{date}.md"

Zero Status fields may remain as MOCK (awaiting review) after Phase 4 completes.

---

## V-02 — Zero-Remaining Confirmation Gate

**axis:** lifecycle-emphasis
**hypothesis:** R1 V-03 closed each phase with a STOP gate and stated "Zero Status fields may
remain as MOCK (awaiting review) after Phase 5 completes" as a rule. This is a normative
statement, not a required output. The C-12 rubric criterion specifies that "The confirmation
is a required output, not implied." A variation that requires the model to produce a count
line ("Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.") as a mandatory
output of the write-back phase provides a machine-checkable signal that the write-back
was actually completed rather than described. Expected improvement: C-12 PASS (was at best
PARTIAL in R1); C-04 PASS maintained. Failure condition: if the count-and-confirm output
appears but the model skips the actual edits, C-12 passes while C-04 fails — which means
C-12 is measuring output production rather than write-back correctness.

---

You are running /mock:review.

Input:
  Topic:         {topic}
  Mock artifact: {mock-artifact-path}
  Tier:          {1|2|3} (--tier flag, or read from TOPICS.md, or default 1)

---

### PHASE 1 — READ AND CLASSIFY

Read {mock-artifact-path}.
For each namespace section, extract: namespace name, Category, current Status.
Read TOPICS.md: tier for {topic}, compliance tags.

Output Phase 1 namespace inventory:
  "Tier: {N} (source: TOPICS.md | --tier | default)"

  | Namespace | Category | Current Status |

STOP. Do not enter Phase 2 until the namespace inventory is complete and all namespaces
have a Category and Status recorded.

---

### PHASE 2 — AUTO-FLAGGING

Apply all three rules to every namespace. Rules are mandatory and not role-overridable.

  EVIDENCE-HEAVY (all tiers):
    Category == EVIDENCE-HEAVY → REAL-REQUIRED, trigger: EVIDENCE-HEAVY

  TIER-CRITICAL (Tier 2+ only):
    tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    → REAL-REQUIRED, trigger: TIER-CRITICAL

  COMPLIANCE (when compliance context active):
    Compliance tags in TOPICS.md OR --compliance flag
    AND namespace in {scout-compliance, trace-permissions}
    → REAL-REQUIRED, trigger: COMPLIANCE

Output Phase 2:
  Auto-flagged (REAL-REQUIRED):
  - {namespace}: trigger = {rule label}

  Remaining (awaiting Phase 3):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

STOP. Every namespace must appear in exactly one list before entering Phase 3.

---

### PHASE 3 — THREE-ROLE EVALUATION

For each namespace in the Remaining list:

  PM: Are required sections present? Gates and tables well-formed?
    Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

  Architect: Does content contradict known architectural facts about {topic}?
    Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

  Strategy: Is coverage adequate for Tier {tier} decisions?
    Verdict: ADEQUATE or INSUFFICIENT FOR TIER {tier}

  Decision:
    All verdicts positive → MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT |
                                          DOMAIN-KNOWLEDGE-CONSISTENT]
    Any verdict negative → REAL-REQUIRED [failed evaluation verdict]

  Reason codes are exact. No paraphrase.

Output Phase 3:
  For each evaluated namespace:
  - PM: [verdict]
  - Architect: [verdict]
  - Strategy: [verdict]
  - Decision: [MOCK-ACCEPTED [code(s)] | REAL-REQUIRED [reason]]

STOP. All remaining namespaces must have decisions before entering Phase 4.

---

### PHASE 4 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.

Section 1 — Header: Topic | Tier | Date
Section 2 — Coverage Review table:
  | Namespace | Category | Decision | Trigger / Reason Code |
  All namespaces from Phases 2 and 3.
Section 3 — Next Steps (numbered, priority order):
  Priority 1: REAL-REQUIRED critical namespaces — trace-* first, then scout-feasibility, then listen-*
  Priority 2: REAL-REQUIRED non-critical namespaces
  Priority 3: REAL-REQUIRED evidence-heavy namespaces
  Ordering rule stated: "Critical first, evidence-heavy last."
  Format: /{skill} {topic} — {one-line reason}

STOP. Review artifact must be written before entering Phase 5.

---

### PHASE 5 — WRITE STATUS BACK (mandatory)

This is the defining action of /mock:review. It cannot be skipped.

For every namespace in {mock-artifact-path}, use Edit to update the Status line in-place:
  Replace: Status: MOCK (awaiting review)
  With one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger or evaluation reason}]

Rules:
  - Edit the Status line only. No other content in the source artifact changes.
  - This is the only permitted in-place edit in Signal.
  - Each written Status must match the Coverage Review table from Phase 4.

**Verification — required output, not implied:**

After all edits complete, count the remaining unresolved Status fields and confirm:

  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

This confirmation line is required. If any Status field was not updated, the confirmation
MUST NOT be written — instead, list each namespace whose Status field was not updated
and state the reason, then attempt the edits again.

---

## V-03 — Verifiable Role-Step Separation

**axis:** role-sequence
**hypothesis:** R1 V-04 structured PM/Architect/Strategy as three separate STEP headings, which
is closer to C-13 than an inline template. However, the steps lacked (a) per-role diagnostic
sub-questions that produce an individually verifiable verdict and (b) a STOP gate after each
role that prevents proceeding until that role's verdict is written. Without sub-questions,
a step can be satisfied with "PM: adequate" and the verdict is present but evidentially
empty. With sub-questions — "Are required sections present? Are enforcement gates present?
Are tables well-formed? Name a specific section." — the model must produce at least one
substantive answer before writing the verdict. Expected improvement: C-13 PASS (step
separation was present but sub-questions were absent in R1 V-04); C-07 improvement because
PM sub-questions reference sections by name.
Failure condition: if sub-questions are present but verdicts are still one-word, the
sub-questions are not sufficient to force substantive evaluation and the criterion requires
a mandatory sentence-count or example-naming requirement.

---

You are running /mock:review.

**Input**

Topic: {topic}
Mock artifact: {mock-artifact-path}
Tier: {tier} — from --tier flag, TOPICS.md, or default 1

**Setup**

Read {mock-artifact-path}. Parse each namespace header block: namespace name, Category, Status.
Read TOPICS.md: tier for {topic}, compliance tags.
State at the top of your output: "Tier: {N} (source: TOPICS.md | --tier | default)"

**Phase 1 — Auto-Flagging**

Apply all three rules before any evaluation. These rules are not overridable.

  EVIDENCE-HEAVY (all tiers): Category == EVIDENCE-HEAVY → REAL-REQUIRED
  TIER-CRITICAL (Tier 2+): tier >= 2 AND critical namespace → REAL-REQUIRED
    Critical namespaces: trace-*, scout-feasibility, listen-*, scout-competitors
  COMPLIANCE: compliance context active AND namespace in {scout-compliance, trace-permissions}
    → REAL-REQUIRED

Auto-flagged list (REAL-REQUIRED):
  - {namespace}: trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

Remaining list (awaiting role evaluation):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

Every namespace in exactly one list. Do not begin Phase 2 until lists are complete.

**Phase 2 — Role Evaluation (non-auto namespaces)**

For each non-auto namespace, complete three separately executable role evaluations.
Each evaluation runs independently — do not merge PM, Architect, and Strategy into
a single paragraph or table row. Each must produce a verdict before the next begins.

---

#### PM Evaluation — Structural Completeness

For each namespace:

  Sub-questions (answer each before writing the verdict):
  1. Are all required sections present in the mock artifact for this namespace?
     Name at least one section that is present and one that would be required.
  2. Are enforcement gates, required output structures, or decision tables present
     and correctly formed? Name the specific gate or table if present.
  3. Would a PM accept this namespace mock as structural coverage for a Tier {tier}
     decision, or would they flag a gap?

  Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Record PM verdict for all namespaces before beginning the Architect evaluation.

---

#### Architect Evaluation — Technical Plausibility

For each namespace:

  Sub-questions (answer each before writing the verdict):
  1. Does the mock content reference any system component, dependency, or interface
     that contradicts known facts about {topic}?
  2. Are the data flows, state transitions, or API shapes described in the mock
     consistent with the actual {topic} architecture?
  3. Name one specific element that confirms plausibility or one that contradicts it.

  Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Record Architect verdict for all namespaces before beginning the Strategy evaluation.

---

#### Strategy Evaluation — Coverage Adequacy for Tier {tier}

For each namespace:

  Sub-questions (answer each before writing the verdict):
  1. What specific Tier {tier} decision depends on this namespace being accurate?
  2. If the team accepted this namespace as MOCK-ACCEPTED, what would they believe
     about {topic} that might not be true? Or: what would they correctly believe?
  3. Is the mock sufficient for the team to proceed to a Tier {tier} commitment?

  Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

Record Strategy verdict for all namespaces before proceeding to Phase 3.

---

**Phase 3 — Decisions**

For each non-auto namespace, combine the three verdicts:

  All three verdicts positive:
    MOCK-ACCEPTED — at least one exact reason code required:
      STRUCTURAL-COVERAGE-SUFFICIENT  (structural completeness drove the verdict)
      DOMAIN-KNOWLEDGE-CONSISTENT     (content plausibility drove the verdict)
    Use both codes when both conditions hold. No paraphrase.

  Any verdict negative:
    REAL-REQUIRED — name the evaluation that failed.

**Phase 4 — Write Review Artifact**

Write simulations/mock/{topic}-review-{date}.md:

  Section 1 — Header: Topic | Tier | Date
  Section 2 — Coverage Review table:
    | Namespace | Category | PM Verdict | Architect Verdict | Strategy Verdict | Decision | Trigger / Reason Code |
    All namespaces. Auto-flagged namespaces: PM/Architect/Strategy columns = "N/A (auto-flagged)"
  Section 3 — Next Steps (numbered, priority order):
    Priority 1: Critical REAL-REQUIRED: trace-* first, scout-feasibility, listen-*
    Priority 2: Non-critical REAL-REQUIRED
    Priority 3: Evidence-heavy REAL-REQUIRED
    Ordering rule: "Critical namespaces first, evidence-heavy last."
    Format: /{skill} {topic} — {reason from the evaluation above}

**Phase 5 — Write Status Back (mandatory)**

For every namespace in {mock-artifact-path}, use Edit to replace the Status line in-place.
Edit Status line only. No other content changed.
  Replace: Status: MOCK (awaiting review)
  With:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  Or:      Status: REAL-REQUIRED [{trigger or evaluation reason}]

This is the defining action of /mock:review.
Confirm: "Annotations updated in: {mock-artifact-path}"
Confirm: "Review written: simulations/mock/{topic}-review-{date}.md"
Zero Status fields may remain as MOCK (awaiting review) after Phase 5 completes.

---

## V-04 (Combined) — Forbidden-Output Enumeration + Verifiable Role-Step Separation

**axes:** phrasing-register + role-sequence
**hypothesis:** V-01 addresses the auto-flag phase with explicit DO NOT phrasing for all three
rules. V-03 addresses the evaluation phase with separately completable role steps and
sub-questions. The two phases address orthogonal failure modes: incorrect auto-flag decisions
(EVIDENCE-HEAVY marked MOCK-ACCEPTED) and collapsed role evaluation (all three roles in one
table cell). Combining them forces correctness at both decision points simultaneously.
Predicted: C-11 PASS (all three DO NOT statements present), C-13 PASS (PM/Architect/Strategy
as separately completable sections with sub-questions and STOP gates), C-02 PASS (DO NOT
gates block auto-rule override), C-07 PASS (sub-questions force substantive verdicts).
Failure condition: length increases reduce compliance with C-04 or C-05 as the model
prioritizes evaluation quality and deprioritizes write-back and priority ordering.

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
  - {namespace}: trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

  Remaining (awaiting evaluation):
  - {namespace}: Category = {HIGH-STRUCTURE | MIXED}

DO NOT proceed until every namespace is placed in exactly one list.

---

STEP 3 — PM EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions and write a PM verdict:

  Sub-question 1: Are all required sections present in the mock artifact?
    Name at least one section that is present.
  Sub-question 2: Are enforcement gates, decision tables, or required output structures
    present and correctly formed? Name the specific gate or structure.
  Sub-question 3: Would a PM accept this as structural coverage for a Tier {tier}
    decision, or would they require a real skill run?

  PM Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE

Complete PM evaluation for ALL remaining namespaces.
DO NOT proceed to Step 4 until PM verdicts are written for every remaining namespace.

---

STEP 4 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions and write an Architect verdict:

  Sub-question 1: Does the mock content reference any system component, dependency, or
    interface that contradicts known facts about {topic}? Name the element.
  Sub-question 2: Are the data flows, state transitions, or structural shapes in the mock
    consistent with the actual {topic} architecture?
  Sub-question 3: What specific architectural fact confirms or challenges plausibility?

  Architect Verdict: PLAUSIBLE or CONTRADICTS KNOWN FACTS

Complete Architect evaluation for ALL remaining namespaces.
DO NOT proceed to Step 5 until Architect verdicts are written for every remaining namespace.

---

STEP 5 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer these sub-questions and write a Strategy verdict:

  Sub-question 1: What specific Tier {tier} decision depends on this namespace being correct?
  Sub-question 2: If accepted as MOCK-ACCEPTED, what would the team believe that might not
    be true? Or: what would they correctly believe that justifies acceptance?
  Sub-question 3: Is the mock sufficient for Tier {tier} decisions, or does it leave a
    coverage gap that would affect a real commitment?

  Strategy Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}

---

STEP 6 — DECISIONS

For each remaining namespace, combine the three verdicts:

  All verdicts positive:
    Decision: MOCK-ACCEPTED
    MUST include at least one reason code from this exact set:
      STRUCTURAL-COVERAGE-SUFFICIENT  (structural completeness drove the verdict)
      DOMAIN-KNOWLEDGE-CONSISTENT     (content plausibility drove the verdict)
    NEVER use any other reason code. NEVER paraphrase these codes. Use both when both apply.

  Any verdict negative:
    Decision: REAL-REQUIRED
    Name the specific evaluation that failed and the sub-question answer that drove it.

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
    Format: /{skill-id} {topic} — {one-line reason citing the evaluation failure}

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

MUST update every Status line in {mock-artifact-path}.
Use Edit tool. In-place replacement only. Do not rewrite any other content.

For each namespace:
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  OR:      Status: REAL-REQUIRED [{trigger or evaluation reason}]

MUST confirm: "Annotations updated in: {mock-artifact-path}"
MUST confirm: "Review written: simulations/mock/{topic}-review-{date}.md"
NEVER leave any Status field as MOCK (awaiting review) after this step.
This is the defining action of /mock:review. It is not optional.

---

## V-05 (Combined) — Pre-Printed Template: Coverage Gap Synthesis + Zero-Remaining Gate + Verifiable Role Steps

**axes:** output-format + lifecycle-emphasis + role-sequence
**hypothesis:** Scout-feasibility R3 demonstrated that pre-printing the output skeleton
(V-02, V-05 in that round) produces stronger structural guarantees than instruction-based
approaches because the model fills fields rather than generating structure. Applied to
mock-review: pre-printing the role evaluation section headers (C-13 guarantee), the
zero-remaining count line (C-12 guarantee), and the cross-namespace risk statement header
(C-09 guarantee) makes all three aspirational criteria dependent on field-filling rather
than on the model remembering to include those elements. The model cannot drop what it did
not generate. Expected: C-09, C-12, C-13 all pass with the lowest model-behavior risk among
all R2 variations. Trade-off: a pre-printed skeleton is longer and less adaptable to
atypical namespace sets; the {N}-namespace count and the verdict cells must be filled
correctly or the skeleton is structurally present but semantically empty.

---

You are running /mock:review.

Input:
  Topic:         {topic}
  Mock artifact: {mock-artifact-path}
  Tier:          {tier} — from --tier flag, TOPICS.md, or default 1

Read {mock-artifact-path}. Parse each namespace: name, Category, Status.
Read TOPICS.md: tier for {topic}, compliance tags.

Fill this skeleton completely. Replace every [FIELD] with the correct value.
Do not remove any header, section label, or structural line.

---

## MOCK REVIEW — {topic}

Tier: [N]  Source: [TOPICS.md | --tier flag | default]
Date: {date}
Namespaces reviewed: [N]

---

## PHASE 1 — AUTO-FLAGGING

Auto-rules are applied before any role evaluation. They are not role-overridable.

EVIDENCE-HEAVY rule (all tiers): Category == EVIDENCE-HEAVY → REAL-REQUIRED
TIER-CRITICAL rule (Tier 2+ only): critical namespace at tier >= 2 → REAL-REQUIRED
  Critical set: trace-*, scout-feasibility, listen-*, scout-competitors
COMPLIANCE rule (when compliance context active): → REAL-REQUIRED

Auto-flagged (REAL-REQUIRED):
| Namespace | Trigger |
|-----------|---------|
| [namespace] | [EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE] |

Remaining (awaiting role evaluation):
| Namespace | Category |
|-----------|----------|
| [namespace] | [HIGH-STRUCTURE | MIXED] |

---

## PHASE 2 — PM EVALUATION

For each remaining namespace:

### PM: [Namespace]

Required sections present: [Yes — name them | No — name what is missing]
Enforcement gates and tables: [Present and well-formed — name the specific gate/table |
                               Absent or malformed — name what is missing]
PM judgment for Tier [N]: [Would accept as structural coverage | Would require a real run]

**PM Verdict: [STRUCTURALLY ADEQUATE | STRUCTURALLY INCOMPLETE]**

---

## PHASE 3 — ARCHITECT EVALUATION

For each remaining namespace:

### Architect: [Namespace]

Contradictions with {topic} architecture: [None found — name the element confirmed |
                                           Contradiction found — name the conflicting element]
Data flows / state transitions consistent: [Yes — name the consistent element |
                                            No — name the inconsistency]
Specific architectural fact: [Name it]

**Architect Verdict: [PLAUSIBLE | CONTRADICTS KNOWN FACTS]**

---

## PHASE 4 — STRATEGY EVALUATION

For each remaining namespace:

### Strategy: [Namespace]

Tier [N] decision at stake: [Name the specific decision]
Belief formed if accepted as MOCK-ACCEPTED: [What the team would believe — correct or incorrect]
Coverage sufficiency for Tier [N]: [Sufficient — state why | Insufficient — state the gap]

**Strategy Verdict: [ADEQUATE FOR TIER N | INSUFFICIENT FOR TIER N]**

---

## PHASE 5 — DECISIONS

For each remaining namespace:

| Namespace | PM Verdict | Architect Verdict | Strategy Verdict | Decision | Reason Code |
|-----------|-----------|------------------|------------------|----------|-------------|
| [namespace] | [ADEQUATE/INCOMPLETE] | [PLAUSIBLE/CONTRADICTS] | [ADEQUATE/INSUFFICIENT] | [MOCK-ACCEPTED / REAL-REQUIRED] | [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT | evaluation failure] |

Valid MOCK-ACCEPTED reason codes (exact, no paraphrase):
  STRUCTURAL-COVERAGE-SUFFICIENT — structural completeness drove the verdict
  DOMAIN-KNOWLEDGE-CONSISTENT — content plausibility drove the verdict

---

## PHASE 6 — COVERAGE REVIEW TABLE

| Namespace | Category | Decision | Trigger / Reason Code |
|-----------|----------|----------|-----------------------|
| [namespace] | [category] | [MOCK-ACCEPTED / REAL-REQUIRED] | [code or trigger] |

---

## PHASE 7 — NEXT STEPS

Ordering rule: Critical REAL-REQUIRED namespaces first (trace-*, then scout-feasibility,
then listen-*), non-critical REAL-REQUIRED second, evidence-heavy REAL-REQUIRED last.

**Coverage gap synthesis:**
[Write one paragraph identifying the cross-namespace risk pattern in this review. Which
 groups of namespaces are REAL-REQUIRED, and what does that combination signal about the
 feature's readiness? Are there interdependencies — e.g., trace-* and listen-* both flagged
 means both runtime behavior and adoption signals are unknown? State the urgency grouping:
 which namespaces are gate-blockers vs. informational gaps vs. evidence-only gaps.]

Priority 1 — Gate-blockers (critical REAL-REQUIRED):
1. /[skill] {topic} — [one-line reason]

Priority 2 — Non-critical REAL-REQUIRED:
2. /[skill] {topic} — [one-line reason]

Priority 3 — Evidence-heavy REAL-REQUIRED:
3. /[skill] {topic} — [one-line reason]

---

## PHASE 8 — WRITE STATUS BACK (mandatory)

Edit {mock-artifact-path}. For each namespace, replace the Status line in-place.
Edit the Status line only. No other content in the source artifact changes.

  Replace: Status: MOCK (awaiting review)
  With:    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  Or:      Status: REAL-REQUIRED [{trigger or evaluation reason}]

This is the defining action of /mock:review.

**Required verification output — do not omit this line:**

  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: [N] of [N]
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

If any Status field was not updated, write instead:
  "[N] Status fields NOT updated: [list namespace names]"
Then attempt the edits again and re-confirm.

---

## Variation Map Summary

| V | Axes | What Changed | Target Criteria | Hypothesis |
|---|------|--------------|-----------------|------------|
| V-01 | phrasing-register | All three auto-rules carry explicit DO NOT forbidden-output statement | C-11, C-02 | Forbidden-output phrasing for all three rules closes the PARTIAL-C-11 gap from R1 V-04 |
| V-02 | lifecycle-emphasis | Write-back phase ends with mandatory count-and-confirm verification output | C-12, C-04 | Required output line makes write-back completion machine-checkable; C-12 passes as output not implication |
| V-03 | role-sequence | PM, Architect, Strategy as separately completable sections with per-role sub-questions and STOP gates | C-13, C-07 | Sub-questions force substantive verdicts; individual STOP gates make each role independently verifiable |
| V-04 | phrasing-register + role-sequence | V-01 DO NOT gates combined with V-03 separately completable role steps | C-11, C-13, C-02, C-07 | Both failure modes blocked simultaneously: auto-rule override (forbidden-output) and collapsed evaluation (step separation) |
| V-05 | output-format + lifecycle-emphasis + role-sequence | Pre-printed skeleton with role section headers, coverage gap synthesis block, and zero-remaining count line | C-09, C-12, C-13 | Pre-printed structure makes aspirational criteria dependent on field-filling rather than model memory; ceiling combination |

**Top combination candidate for Round 3:**
V-04 (forbidden-output + step separation) addresses C-11 and C-13 through enforcement phrasing.
V-05 (pre-printed skeleton) addresses C-09, C-12, C-13 through structural pre-printing.
If V-05 achieves the highest composite, the Round 3 question is whether inertia framing
(from V-05 scout-feasibility R3) can be added to the coverage gap synthesis paragraph
without destabilizing the skeleton format — a focused single-axis test worth isolating.
