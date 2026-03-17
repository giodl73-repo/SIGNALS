---
skill: quest-variate
skill_target: mock-accept
date: 2026-03-16
round: 2
rubric_version: v2
status: VARIATE
---

# mock-accept Variate — Round 2

**Date:** 2026-03-16
**Skill:** mock-accept
**Rubric:** v2 (C-01 through C-13; essential C-01–C-05; aspirational C-11–C-13 added this round)
**Baseline:** R1 converged prompt (mock-review.t3/SKILL.md)
**Round:** R2 — 3 single-axis passes (V-01 through V-03), 2 combinations (V-04, V-05)

---

## Axis-Assignment Plan

R1 converged on: DO-NOT imperative gates (V-04), numbered steps (V-03), auto-flag phase gate
(V-01). The baseline already passes C-01 through C-10. R2 targets the three new aspirational
criteria extracted from R1 excellence signals.

| Plan | Axis | Source criterion | What changes | Predicted |
|------|------|-----------------|--------------|-----------|
| V-01 | phrasing-register | C-12: Slot 2 before Slot 1 | MOCK-ACCEPTED template reordered; "WRITE CONTRAST SLOT FIRST" imperative + SLOT-ORDER-INVERSION error name | C-12 pass; C-05 maintained (both slots still required) |
| V-02 | output-format | C-13: SKIP cells | Evaluation restructured as a table; auto-flagged rows get Arch=SKIP / Strategy=SKIP / PM=SKIP; column rules reference AUTO-RULE CONTAMINATION | C-13 pass for table-format output; C-01/C-02 maintained |
| V-03 | lifecycle-emphasis | C-11: Named bypass error codes | Each step-transition guard adds explicit `bypass-error-code:` field to blocked-list record; codes become parseable output rather than prose instructions | C-11 pass; C-07 maintained (lists still required) |
| V-04 | phrasing-register + output-format | C-12 + C-13 | Combines V-01 Slot 2 first + V-02 SKIP table; two non-overlapping changes | Both C-12 and C-13 pass simultaneously; no mutual interference |
| V-05 | output-format + phrasing-register + lifecycle-emphasis | C-11 + C-12 + C-13 | Full R2 integration: SKIP table + Slot 2 first + bypass error code fields + R1 named-phase scaffold carried forward | All three aspirational criteria pass; composite >= 80 |

---

## V-01 — Phrasing Register: MOCK-ACCEPTED Template Mandates Slot 2 First

**axis:** phrasing-register
**hypothesis:** Adding an explicit "WRITE CONTRAST SLOT FIRST — DO NOT write Slot 1 before
Slot 2" imperative at the MOCK-ACCEPTED template entry, and reordering the template itself so
the Contrast label precedes the Structural position label, prevents SLOT-ORDER-INVERSION by
making the correct order structural rather than advisory. The current baseline template lists
Slot 1 first; a model filling in the template in order produces Slot 1 first and may omit
Slot 2 once the block reads complete. Reversing the label order in the template forces
Contrast to be filled before Structural position is reachable. Failure condition: if C-12
pass rate does not improve despite the reordering, Slot 2 omission is driven by evaluation
failure (C-05 would also fail), not ordering ambiguity.

---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring
  a positive argument against inertia. Absence of disqualification is not positive evidence.
  The inertia structure forces a genuine contrastive argument — confirmation that nothing
  is wrong does not earn MOCK-ACCEPTED.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category field, and Status field from each
namespace section. Read TOPICS.md; record tier for {topic} and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Fire before role evaluation. Not role-overridable.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE

Output two lists:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (3 rules, all required — verify all 3 before proceeding):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels present. A two-of-three set does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD:
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Any verdict applied to an auto-flagged namespace is void.

DO NOT proceed to STEP 3 until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions using entity-naming grammar.
Yes/no answers do not satisfy entity-naming sub-question requirements.

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to Strategy:
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply Strategy Evaluation (STEP 4) to these namespaces.
  Named error: ARCH-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Strategy Evaluation: [{list}]

DO NOT proceed to STEP 4 until Architect verdicts and guard assignments are complete
for all remaining namespaces.

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only)

Entry condition: STEP 4 applies ONLY to namespaces not on the Arch-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.] |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM:
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation: [{list}]

DO NOT proceed to STEP 5 until Strategy verdicts and guard assignments are complete
for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces not on the Arch-blocked or
Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

DO NOT proceed to STEP 6 until PM verdicts are written for every qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field: named, parseable artifact field at fixed position (second line of every block).
  Values: trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                    STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  *** WRITE CONTRAST SLOT FIRST ***
  DO NOT write Slot 1 (Structural position) before Slot 2 (Contrast).
  Named error: SLOT-ORDER-INVERSION. Both slots must be structurally separate.

  Contrast (SLOT 2 — WRITE THIS SLOT FIRST):
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.]

  Structural position (SLOT 1 — Strategy SQ-1 anchor, written AFTER Slot 2):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. ERROR — VERDICT-ECHO: role as subject.]
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 until all decision blocks are complete.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-accept-{date}.md.
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement:
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"
    Include urgency grouping commentary for each priority group if more than one namespace.

DO NOT proceed to STEP 8 until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place using Edit tool. Replace Status fields only. Do not
rewrite any other content.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY OUTPUT:
  After completing all edits, verify before confirming.
  CANARY ASSERTION (write only when condition is verified true):
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK (awaiting review).
  Named error: CANARY-FALSE-POSITIVE.
  If condition not met: output "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-02 — Output Format: Evaluation Table with SKIP Cells for Auto-Flagged Rows

**axis:** output-format
**hypothesis:** Restructuring Steps 3–5 around a single evaluation table — where auto-flagged
namespaces receive Arch=SKIP / Strategy=SKIP / PM=SKIP in all three role columns, and the
table column rules explicitly name AUTO-RULE CONTAMINATION as the reason any non-SKIP value
in an auto-flagged row constitutes a violation — enforces C-13 without requiring prose DO-NOT
gates per evaluation. The structural check is: inspect any row in the table; if the namespace
is auto-flagged and any role column is not SKIP, the contamination error is visible by
inspection without reading evaluation prose. Partial SKIP (e.g., Arch=SKIP but Strategy
blank) is itself an AUTO-RULE CONTAMINATION error. Failure condition: if models produce
non-SKIP values in auto-flagged rows despite the table structure, enforcement must return
to prose DO-NOT gates.

---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring
  a positive argument against inertia. Absence of disqualification is not positive evidence.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category field, and Status field from each
namespace section. Read TOPICS.md; record tier for {topic} and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Fire before role evaluation. Not role-overridable.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE

Output two lists:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting role evaluation): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (3 rules, all required — verify all 3 before proceeding):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels present. A two-of-three set does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD:
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  The evaluation table structurally enforces this: auto-flagged rows MUST show SKIP in all
  three role columns. Any non-SKIP value in an auto-flagged row = AUTO-RULE CONTAMINATION.

DO NOT proceed to STEP 3 until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — BUILD EVALUATION TABLE

Construct the evaluation table for ALL namespaces.

Column rules — AUTO-RULE CONTAMINATION structural enforcement:
  - Auto-flagged rows: Arch = SKIP, Strategy = SKIP, PM = SKIP (all three simultaneously).
    Partial SKIP (any single column SKIP while others blank or filled) = AUTO-RULE CONTAMINATION.
  - Non-auto rows: fill Arch, Strategy, PM from Steps 3a–3c below.

| Namespace | Category | Auto-Flag | Arch | Strategy | PM | Preliminary Decision |
|-----------|----------|-----------|------|----------|----|----------------------|
| {auto-ns} | {cat}    | {trigger} | SKIP | SKIP | SKIP | REAL-REQUIRED |
| {other}   | {cat}    | —         | {pending} | {pending} | {pending} | TBD |

**3a — Architect column** (non-auto namespaces only):
For each namespace, entity-naming grammar required:
  SQ-A1: Name the system component, dependency, or interface confirming plausibility —
         or "Contradiction: {specific element}".
  SQ-A2: Name the data flow, state transition, or API shape the mock implies —
         or "Inconsistency: {specific element}".
  SQ-A3: Name the architectural fact this mock most directly depends on; state consistency.
  Verdict: CONSISTENT-WITH-ARCHITECTURE  or  CONTRADICTS-ARCHITECTURE

  Arch-blocked list (CONTRADICTS-ARCHITECTURE): [{list — may be empty, must be stated}]
  Named error: ARCH-GUARD-BYPASS if any Arch-blocked namespace enters Strategy column.
  Update table: fill Arch column. DO NOT fill Strategy or PM for Arch-blocked rows.

**3b — Strategy column** (non-auto, non-Arch-blocked namespaces only):
  SQ-S1: Name the specific Tier {tier} decision this namespace supports. [SLOT 1 anchor.]
  SQ-S2: Name the belief the team would form — state whether correct or incorrect.
  SQ-S3: Name the coverage gap — or "No gap — coverage adequate for Tier {tier}."
  Verdict: ADEQUATE FOR TIER {tier}  or  INSUFFICIENT FOR TIER {tier}

  Strategy-blocked list (INSUFFICIENT): [{list — may be empty, must be stated}]
  Named error: STRATEGY-TO-PM-GUARD-BYPASS if any Strategy-blocked namespace enters PM column.
  Update table: fill Strategy column. DO NOT fill PM for Strategy-blocked rows.

**3c — PM column** (qualifying namespaces only):
  SQ-P1: Name the required sections present in the mock artifact.
  SQ-P2: Name the enforcement gate, decision table, or required structure —
         or "Absent: {element} — defined in {section}".
  SQ-P3: Name one structural gap — or "No gap — structural completeness demonstrated."
  Verdict: STRUCTURALLY ADEQUATE  or  STRUCTURALLY INCOMPLETE

  Update table: fill PM column.

Verify: auto-flagged rows show SKIP in all three columns. Any deviation = AUTO-RULE CONTAMINATION.
DO NOT proceed to STEP 4 until evaluation table is complete and SKIP enforcement verified.

---

STEP 4 — DECISIONS WITH CITATION

Trigger field values: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                      STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)
  Structural position (SLOT 1 — SQ-S1 anchor):
    Feeds tier decision: [name the specific Tier {tier} decision. Generic = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]
  Contrast (SLOT 2 — structurally separate from Slot 1):
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. No named contrasting type = CONTRAST-INCOMPLETE.]

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict: [artifact as subject, present-tense. VERDICT-ECHO = role as subject.]
  Artifact state: [artifact as subject, present-tense — propagates to next-steps]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 5 until all decision blocks are complete.

---

STEP 5 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-accept-{date}.md.
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement:
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"
    Include urgency grouping commentary for each priority group if more than one namespace.

DO NOT proceed to STEP 6 until review artifact is confirmed written.

---

STEP 6 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place using Edit tool. Replace Status fields only.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY OUTPUT:
  CANARY ASSERTION (write only when verified true):
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  Named error: CANARY-FALSE-POSITIVE.
  If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-03 — Lifecycle Emphasis: Guard-Bypass Error Codes as Explicit Parseable Output Fields

**axis:** lifecycle-emphasis
**hypothesis:** Elevating guard-bypass error codes from prose instructions to explicit
`bypass-error-code:` fields in the blocked-list output record makes C-11 checkable as an
output property rather than an instruction-compliance property. The current baseline names
ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS in the guard sections as named errors
in instruction prose — not as parseable fields the model must emit. C-11 tests whether
each gate *output* explicitly names its bypass error code. V-03 adds a mandatory
`bypass-error-code:` field to every blocked-list record. It also requires an explicit
"not triggered" statement when the blocked list is empty, making the code checkable in
both the triggered and untriggered case. Failure condition: if C-11 pass rate does not
improve, the current prose placement already produces the codes in model output at
sufficient fidelity.

---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring
  a positive argument against inertia. Absence of disqualification is not positive evidence.
  The inertia structure forces a genuine contrastive argument — confirmation that nothing
  is wrong does not earn MOCK-ACCEPTED.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category field, and Status field from each
namespace section. Read TOPICS.md; record tier for {topic} and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Fire before role evaluation. Not role-overridable.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE

Output two lists:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (3 rules, all required — verify all 3 before proceeding):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels present. A two-of-three set does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD:
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Any verdict applied to an auto-flagged namespace is void.

DO NOT proceed to STEP 3 until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions using entity-naming grammar.
Yes/no answers do not satisfy entity-naming sub-question requirements.

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GATE — Architect to Strategy (gate bypass error code: ARCH-GUARD-BYPASS):
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE

  Record each blocked namespace using the bypass-error-code field format:
    Arch-blocked:
    - namespace: {namespace}
      architect-verdict: CONTRADICTS-ARCHITECTURE
      bypass-error-code: ARCH-GUARD-BYPASS
      preliminary-decision: REAL-REQUIRED / trigger = ARCH-IMPLAUSIBLE

  If no namespaces are blocked, write:
    Arch-blocked: none
    bypass-error-code: ARCH-GUARD-BYPASS — not triggered

  Proceeding to Strategy Evaluation: [{non-blocked list}]
  GUARD-BYPASS CONTAMINATION fires if any namespace with bypass-error-code: ARCH-GUARD-BYPASS
  appears in the Strategy Evaluation input. Any such evaluation is void.

DO NOT proceed to STEP 4 until Architect verdicts and bypass-error-code records are written.

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only)

Entry condition: STEP 4 applies ONLY to namespaces NOT on the Arch-blocked list.
Violation of this condition = GUARD-BYPASS CONTAMINATION.

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.] |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GATE — Strategy to PM (gate bypass error code: STRATEGY-TO-PM-GUARD-BYPASS):
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE

  Record each blocked namespace using the bypass-error-code field format:
    Strategy-blocked:
    - namespace: {namespace}
      strategy-verdict: INSUFFICIENT FOR TIER {tier}
      bypass-error-code: STRATEGY-TO-PM-GUARD-BYPASS
      preliminary-decision: REAL-REQUIRED / trigger = STRATEGY-INADEQUATE

  If no namespaces are blocked, write:
    Strategy-blocked: none
    bypass-error-code: STRATEGY-TO-PM-GUARD-BYPASS — not triggered

  Proceeding to PM Evaluation: [{non-blocked list}]
  GUARD-BYPASS CONTAMINATION fires if any namespace with bypass-error-code:
  STRATEGY-TO-PM-GUARD-BYPASS appears in the PM Evaluation input. Any such evaluation is void.

DO NOT proceed to STEP 5 until Strategy verdicts and bypass-error-code records are written.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces NOT on the Arch-blocked or
Strategy-blocked lists. Violation = GUARD-BYPASS CONTAMINATION.

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

DO NOT proceed to STEP 6 until PM verdicts are written for every qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field: named, parseable artifact field at fixed position (second line of every block).
  Values: trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                    STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE:
| Row # | REAL-REQUIRED evaluation field             | MOCK-ACCEPTED structural analog                      |
|-------|--------------------------------------------|------------------------------------------------------|
| 1     | Decision: REAL-REQUIRED                    | Decision: MOCK-ACCEPTED                              |
| 2     | trigger = {rule label}                     | trigger = n/a                                        |
| 3     | Failing evaluation: {role name}            | reason-code: [exact code from enumeration]           |
| 4     | Failing verdict: {full verdict string}     | Structural position: [SQ-1 anchor — tier decision]  |
| 5     | SQ answer driving verdict:                 | Contrast: [contrasting namespace type +              |
|       |   {artifact-as-subject form}               |   structural factor distinguishing it]               |
| 6     | Artifact state: {art-subj, pres-tense}     | (no analog)                                          |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                          |

Row 5 grammar: artifact as subject, present-tense. ERROR — VERDICT-ECHO: role as subject.

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)
  Structural position (SLOT 1 — Strategy SQ-1 anchor):
    Feeds tier decision: [name the specific Tier {tier} decision. Generic = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]
  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1):
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. No named contrasting type = CONTRAST-INCOMPLETE.
    Single-slot rationale = RATIONALE-INCOMPLETE.]

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. ERROR — VERDICT-ECHO: role as subject.]
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 until all decision blocks are complete.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-accept-{date}.md.
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement:
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"
    Include urgency grouping commentary for each priority group if more than one namespace.

DO NOT proceed to STEP 8 until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place using Edit tool. Replace Status fields only.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY OUTPUT:
  CANARY ASSERTION (write only when verified true):
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  Named error: CANARY-FALSE-POSITIVE.
  If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-04 (Combined) — Output Format + Phrasing Register: SKIP Table + Slot 2 First

**axes:** output-format + phrasing-register
**hypothesis:** C-12 (Slot 2 before Slot 1) and C-13 (SKIP cells) target non-overlapping
output regions: SKIP cells appear in the evaluation table (Steps 3–4), while Slot 2 ordering
appears in the MOCK-ACCEPTED decision template (Step 5). Combining both simultaneously tests
whether two structural improvements apply without mutual interference. V-04 predicts: SKIP
cells eliminate AUTO-RULE CONTAMINATION in the table; Slot 2 first eliminates CONTRAST-
INCOMPLETE omission in decision blocks; neither change degrades the other. Failure condition:
if essential criterion pass rates degrade despite both changes targeting separate output
regions, prompt length overhead is the cause — individual application in separate steps is
preferred.

---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring
  a positive argument against inertia. Absence of disqualification is not positive evidence.
  The inertia structure forces a genuine contrastive argument — confirmation that nothing
  is wrong does not earn MOCK-ACCEPTED.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category field, and Status field from each
namespace section. Read TOPICS.md; record tier for {topic} and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Fire before role evaluation. Not role-overridable.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE

Output two lists:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting role evaluation): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (3 rules, all required — verify all 3 before proceeding):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels present. A two-of-three set does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD:
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Structural enforcement: auto-flagged rows in the evaluation table MUST show SKIP in ALL
  THREE role columns. Partial SKIP = AUTO-RULE CONTAMINATION.

DO NOT proceed to STEP 3 until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — BUILD EVALUATION TABLE

Build the evaluation table. AUTO-RULE CONTAMINATION column rule applies to all auto-flagged rows.

Column rules:
  - Auto-flagged rows: Arch = SKIP, Strategy = SKIP, PM = SKIP simultaneously.
    Any non-SKIP value in any role column for an auto-flagged row = AUTO-RULE CONTAMINATION.
  - Non-auto rows: fill Arch, Strategy, PM using Steps 3a–3c.

| Namespace | Category | Auto-Flag | Arch | Strategy | PM |
|-----------|----------|-----------|------|----------|----|
| {auto-ns} | {cat}    | {trigger} | SKIP | SKIP | SKIP |
| {other}   | {cat}    | — | {pending} | {pending} | {pending} |

**3a — Architect verdicts** (non-auto namespaces only):
Entity-naming grammar required:
  SQ-A1: Name the system component, dependency, or interface confirming plausibility —
         or "Contradiction: {element}".
  SQ-A2: Name the data flow, state transition, or API shape the mock implies —
         or "Inconsistency: {element}".
  SQ-A3: Name the architectural fact this mock most directly depends on; state consistency.
  Verdict: CONSISTENT-WITH-ARCHITECTURE  or  CONTRADICTS-ARCHITECTURE

  Arch-blocked list (CONTRADICTS-ARCHITECTURE): [{list — empty if none, must be stated}]
  Named error: ARCH-GUARD-BYPASS if any Arch-blocked namespace enters Strategy column.
  Update table: fill Arch column. DO NOT fill Strategy or PM for Arch-blocked rows.

**3b — Strategy verdicts** (non-auto, non-Arch-blocked namespaces only):
  SQ-S1: Name the specific Tier {tier} decision this namespace supports. [Becomes SLOT 1 anchor.]
  SQ-S2: Name the belief the team would form — state whether correct or incorrect.
  SQ-S3: Name the coverage gap — or "No gap — coverage adequate."
  Verdict: ADEQUATE FOR TIER {tier}  or  INSUFFICIENT FOR TIER {tier}

  Strategy-blocked list (INSUFFICIENT): [{list — empty if none, must be stated}]
  Named error: STRATEGY-TO-PM-GUARD-BYPASS if any Strategy-blocked namespace enters PM column.
  Update table: fill Strategy column. DO NOT fill PM for Strategy-blocked rows.

**3c — PM verdicts** (qualifying namespaces only):
  SQ-P1: Name the required sections present.
  SQ-P2: Name the enforcement gate, decision table, or required structure —
         or "Absent: {element} — defined in {section}".
  SQ-P3: Name one structural gap — or "No gap — completeness demonstrated."
  Verdict: STRUCTURALLY ADEQUATE  or  STRUCTURALLY INCOMPLETE

  Update table: fill PM column.

Verify: auto-flagged rows show SKIP in all three columns. Any deviation = AUTO-RULE CONTAMINATION.
DO NOT proceed to STEP 4 until evaluation table is complete.

---

STEP 4 — DECISIONS WITH CITATION

Trigger field values: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                      STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  *** WRITE CONTRAST SLOT FIRST — Named error: SLOT-ORDER-INVERSION if Slot 1 precedes Slot 2 ***

  Contrast (SLOT 2 — WRITE THIS ENTRY FIRST, structurally separate from Slot 1):
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. No named contrasting namespace type = CONTRAST-INCOMPLETE.
    Single-slot rationale = RATIONALE-INCOMPLETE.]

  Structural position (SLOT 1 — WRITE AFTER SLOT 2, Strategy SQ-S1 anchor):
    Feeds tier decision: [name the specific Tier {tier} decision this namespace supports.
    Generic adequacy statement = SLOT-VIOLATION. Classify: STRUCTURAL-FORM | TIER-GATING.]

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict: [artifact as subject, present-tense. VERDICT-ECHO = role as subject.]
  Artifact state: [artifact as subject, present-tense — propagates to next-steps]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 5 until all decision blocks are complete.

---

STEP 5 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-accept-{date}.md.
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement:
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"
    Include urgency grouping commentary for each priority group if more than one namespace.

DO NOT proceed to STEP 6 until review artifact is confirmed written.

---

STEP 6 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place using Edit tool. Replace Status fields only.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY OUTPUT:
  CANARY ASSERTION (write only when verified true):
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  Named error: CANARY-FALSE-POSITIVE.
  If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-05 (Combined) — Full R2 Integration: SKIP Table + Slot 2 First + Bypass Error Code Fields + Named Phase Scaffold

**axes:** output-format + phrasing-register + lifecycle-emphasis
**hypothesis:** Full integration of all three R2 targets stacked on R1's proven phase scaffold.
R1 V-03 (named phases with STOP gates) was a strong contributor to C-03 and C-04 pass rates;
V-05 carries it forward as the outer structure. Inside that structure: SKIP cells enforce C-13
without prose; Slot 2 first enforces C-12 structurally; bypass error code fields emit C-11 as
parseable output properties. All three changes target separate output regions and should be
non-interfering. Failure condition: if essential criterion pass rates degrade, the combined
prompt length exceeds clean execution capacity and improvements should be applied incrementally.

---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring
  a positive argument against inertia. Absence of disqualification is not positive evidence.
  The inertia structure forces a genuine contrastive argument — confirmation that nothing
  is wrong does not earn MOCK-ACCEPTED.

---

### PHASE 1 — READ AND CLASSIFY

Read {mock-artifact-path}. For each namespace section extract: namespace name, Category, Status.
Read TOPICS.md: tier for {topic}, compliance tags.

Output:
  Tier: {N} (source: TOPICS.md | --tier flag | default)
  Namespace inventory:
  | Namespace | Category | Current Status |

STOP. Complete the namespace inventory before entering Phase 2.

---

### PHASE 2 — AUTO-FLAG

Apply all three rules to every namespace. Each rule is mandatory. None is optional.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE

Output two lists:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (awaiting Phase 3): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (3 rules, all required — verify all 3 before proceeding):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels present. A two-of-three set does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD:
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Structural enforcement via Phase 3 table: auto-flagged rows show SKIP in ALL THREE role
  columns simultaneously. Partial SKIP = AUTO-RULE CONTAMINATION.

===================================================================

STOP. Two-list partition confirmed and FORBIDDEN OUTPUTS TRIAD complete (3 of 3) before Phase 3.

---

### PHASE 3 — ROLE EVALUATION (table format with SKIP enforcement)

Build the evaluation table for ALL namespaces.

Column rule — AUTO-RULE CONTAMINATION structural enforcement:
  Auto-flagged rows: Arch = SKIP / Strategy = SKIP / PM = SKIP (simultaneously, all three).
  Any non-SKIP value in any role column for an auto-flagged row = AUTO-RULE CONTAMINATION.
  Non-auto rows: fill each column from 3a–3c.

| Namespace | Category | Auto-Flag | Arch | Strategy | PM |
|-----------|----------|-----------|------|----------|----|
| {auto-ns} | {cat}    | {trigger} | SKIP | SKIP | SKIP |
| {other}   | {cat}    | — | {pending} | {pending} | {pending} |

**Phase 3a — Architect column** (non-auto namespaces only):
Entity-naming grammar required. Yes/no answers do not satisfy.
  SQ-A1: Name the system component, dependency, or interface that confirms plausibility —
         or "Contradiction: {specific element}".
  SQ-A2: Name the data flow, state transition, or API shape the mock implies —
         or "Inconsistency: {specific element}".
  SQ-A3: Name the architectural fact this mock most directly depends on; state consistency.
  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE  or  CONTRADICTS-ARCHITECTURE

  Arch gate output (bypass-error-code field mandatory):
    Arch-blocked:
    - namespace: {namespace}
      architect-verdict: CONTRADICTS-ARCHITECTURE
      bypass-error-code: ARCH-GUARD-BYPASS
      preliminary-decision: REAL-REQUIRED / trigger = ARCH-IMPLAUSIBLE
    If none: "Arch-blocked: none — bypass-error-code: ARCH-GUARD-BYPASS not triggered"

    Proceeding to Strategy: [{non-blocked list}]
    GUARD-BYPASS CONTAMINATION fires if any Arch-blocked namespace appears in Strategy input.

  Update table: fill Arch column. DO NOT fill Strategy or PM for Arch-blocked rows.

**Phase 3b — Strategy column** (non-auto, non-Arch-blocked namespaces only):
  SQ-S1: Name the specific Tier {tier} decision this namespace supports. [SLOT 1 anchor.]
  SQ-S2: Name the belief the team would form — state whether correct or incorrect.
  SQ-S3: Name the coverage gap — or "No gap — coverage adequate for Tier {tier}."
  Strategy Verdict: ADEQUATE FOR TIER {tier}  or  INSUFFICIENT FOR TIER {tier}

  Strategy gate output (bypass-error-code field mandatory):
    Strategy-blocked:
    - namespace: {namespace}
      strategy-verdict: INSUFFICIENT FOR TIER {tier}
      bypass-error-code: STRATEGY-TO-PM-GUARD-BYPASS
      preliminary-decision: REAL-REQUIRED / trigger = STRATEGY-INADEQUATE
    If none: "Strategy-blocked: none — bypass-error-code: STRATEGY-TO-PM-GUARD-BYPASS not triggered"

    Proceeding to PM: [{non-blocked list}]
    GUARD-BYPASS CONTAMINATION fires if any Strategy-blocked namespace appears in PM input.

  Update table: fill Strategy column. DO NOT fill PM for Strategy-blocked rows.

**Phase 3c — PM column** (qualifying namespaces only):
  SQ-P1: Name the required sections present in the mock artifact.
  SQ-P2: Name the enforcement gate, decision table, or required structure —
         or "Absent: {element} — defined in {section}".
  SQ-P3: Name one structural gap — or "No gap — structural completeness demonstrated."
  PM Verdict: STRUCTURALLY ADEQUATE  or  STRUCTURALLY INCOMPLETE

  Update table: fill PM column.

Verify: auto-flagged rows show SKIP in all three columns. Any deviation = AUTO-RULE CONTAMINATION.

STOP. Evaluation table complete and SKIP enforcement verified before Phase 4.

---

### PHASE 4 — DECISIONS WITH CITATION

Trigger field values: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                      STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes; no paraphrase; no invented codes)

  *** SLOT ORDER RULE: WRITE SLOT 2 (CONTRAST) BEFORE SLOT 1 (STRUCTURAL POSITION) ***
  *** Named error: SLOT-ORDER-INVERSION if Slot 1 precedes Slot 2 in any block ***

  Contrast (SLOT 2 — WRITE FIRST, structurally separate):
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. No named contrasting namespace = CONTRAST-INCOMPLETE.
    Merged with Slot 1 into single block = RATIONALE-INCOMPLETE.]

  Structural position (SLOT 1 — WRITE AFTER SLOT 2, Strategy SQ-S1 anchor):
    Feeds tier decision: [name the specific Tier {tier} decision this namespace supports.
    Generic adequacy statement = SLOT-VIOLATION. Classify: STRUCTURAL-FORM | TIER-GATING.]

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict: [artifact as subject, present-tense. VERDICT-ECHO = role as subject.]
  Artifact state: [artifact as subject, present-tense — propagates to next-steps entry]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

STOP. All decision blocks complete before Phase 5.

---

### PHASE 5 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-accept-{date}.md.
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement:
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"
    Include urgency grouping commentary for each priority group if more than one namespace.

STOP. Review artifact confirmed written before Phase 6.

---

### PHASE 6 — WRITE STATUS BACK (mandatory, non-skippable)

This is the defining action of /mock:accept. It cannot be skipped.

Edit {mock-artifact-path} in-place using Edit tool. Replace Status fields only.
Do not rewrite any other content in the source artifact.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

The decision written to the source artifact MUST match the review table from Phase 5.

CANARY OUTPUT:
  After completing all edits, verify before confirming.
  CANARY ASSERTION (write only when condition is verified true):
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK (awaiting review).
  Named error: CANARY-FALSE-POSITIVE.
  If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-accept-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## Variation Map Summary

| V | Axes | What Changed from Baseline | Target Criteria | Hypothesis |
|---|------|---------------------------|-----------------|------------|
| V-01 | phrasing-register | MOCK-ACCEPTED template reordered: Slot 2 (Contrast) label precedes Slot 1 (Structural position); "WRITE CONTRAST SLOT FIRST" imperative added; SLOT-ORDER-INVERSION named as the error | C-12 | Structural ordering of template slots prevents CONTRAST-INCOMPLETE omission more reliably than advisory language; Slot 2 cannot be dropped after Slot 1 reads complete if it must be written first |
| V-02 | output-format | Role evaluation restructured as a table with Arch/Strategy/PM columns; auto-flagged rows receive SKIP in all three columns simultaneously; column rules name AUTO-RULE CONTAMINATION as the enforcement reason; partial SKIP is itself a contamination error | C-13 | SKIP cells make contamination violations structurally detectable by inspection without prose DO-NOT gates; visually self-evident invariant at zero extra prose cost |
| V-03 | lifecycle-emphasis | Each step-transition gate records blocked namespaces with explicit `bypass-error-code:` field; ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS appear as parseable output fields; empty-blocked case requires explicit "not triggered" statement | C-11 | Named error codes as output fields are checkable by inspection; prose-embedded codes may not appear in model output even if named in instructions |
| V-04 | phrasing-register + output-format | V-02 SKIP table + V-01 Slot 2 first; two non-overlapping structural changes applied simultaneously (table region vs decision template region) | C-12 + C-13 | Non-overlapping target regions allow both changes to coexist without mutual interference; simultaneous application tests additive scoring benefit |
| V-05 | output-format + phrasing-register + lifecycle-emphasis | Full R2 integration: SKIP cells (C-13) + Slot 2 first (C-12) + bypass error code fields (C-11) + R1 named-phase scaffold (STOP gates, PHASE headers) carried forward as outer structure | C-11 + C-12 + C-13 | Maximum-coverage variation; all three aspirational criteria addressed simultaneously; R1 phase scaffold preserved to maintain C-03/C-04 essential pass rates |

**Top priority for Round 3 (predict before scoring):**
If V-05 passes all essential criteria and reaches composite >= 80, it becomes the new golden.
If V-05 degrades essential criteria (most likely C-03 or C-04 due to prompt length), test
V-04 as the minimal safe combination. If V-04 also degrades, apply the single-axis improvement
with the highest individual C-11/C-12/C-13 yield and iterate from there.
