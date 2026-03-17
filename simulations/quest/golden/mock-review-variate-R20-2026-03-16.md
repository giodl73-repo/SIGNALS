---
skill: quest-variate
skill_target: mock-review
date: 2026-03-16
round: 20
rubric_version: v20
status: VARIATE
---

# mock-review Variate — Round 20

**Date:** 2026-03-16
**Skill:** mock-review
**Rubric:** v20 (C-01 through C-43; aspirational denominator = 37)
**Round:** R20 — testing v20 C-42 three-tier level stability across variation axes and C-43
belt-and-suspenders ceiling per explicit v20 definition

---

## What R19 Left Open

R19 achieved C-42 PASS in V-03/V-04/V-05 (TRIAD header labeled), C-42 PARTIAL in V-01
(TRIAD header unlabeled — the PARTIAL boundary case), and C-42 FAIL in V-02 (only decision-block
slots labeled — the FAIL floor). The v20 rubric crystallizes these patterns into named levels
with explicit boundary conditions. R19 established the levels; R20 tests whether the v20
three-tier definition is stable across the remaining variation axes (role sequence, phrasing
register, lifecycle emphasis, inertia framing) and confirms the belt-and-suspenders ceiling
as explicitly documented in v20.

| Criterion | R19 ceiling | R20 target |
|-----------|-------------|-----------|
| C-42 | PASS in V-03/V-04/V-05 (TRIAD header labeled) | Confirm PARTIAL boundary holds under Arch-first; confirm FAIL floor holds under Strategy-first; test belt-and-suspenders ceiling as named PASS case |
| C-43 | PASS in V-01/V-02/V-03/V-05 (Row # column) | Confirm independence from C-42 variation axes; test PASS stability under inertia-heavy and conversational-register variants |

---

## Variation Axes and Hypotheses

| Variation | C-42 | C-43 | Role sequence | Primary axes | Hypothesis |
|-----------|------|------|---------------|--------------|-----------|
| V-01 | PARTIAL (TRIAD header unlabeled) | PASS | Arch-first (C-36 ✓) | C-42 level × role sequence | PARTIAL boundary holds under Arch-first: TRIAD header remains the sole unlabeled element regardless of whether Arch or Strategy runs first; C-43 PASS independent of role ordering. |
| V-02 | FAIL (only decision-block slots labeled) | PASS | Strategy-first (C-35 ✓) | C-42 level × role sequence | FAIL floor holds under Strategy-first: unlabeled guards, step headings, TRIAD header, and canary constitute the FAIL pattern independent of role ordering; C-43 Row # column satisfies C-43 independent of labeling level. |
| V-03 | PASS (all labeled, TRIAD included) | PASS | Arch-first (C-36 ✓) | Inertia framing (heavy) | Inertia framing axis is independent of labeling level: a named RESISTANCE METRIC block and explicit inertia argument checklist achieve stronger C-22 signal without altering labeling behavior; C-42 PASS and C-43 PASS are stable. |
| V-04 | PASS (all labeled, TRIAD included) | PASS | Strategy-first (C-35 ✓) | Phrasing register (conversational) | Conversational phrasing register preserves all mechanical requirements: C-42 PASS and C-43 PASS survive register shift from imperative to descriptive/explanatory; criterion-ID labels and Row # column are formatting elements that coexist with any register. |
| V-05 | PASS + belt-and-suspenders (per-row [C-15] in SQ cells) | PASS | Arch-first (C-36 ✓) | Lifecycle emphasis + belt-and-suspenders ceiling | Belt-and-suspenders test: per-row [C-15] labels inside SQ table cells are redundant with the column header but explicitly classified as still-PASS by v20 C-42 definition; lifecycle emphasis axis (expanded phase boundaries) is compatible with full criterion coverage. |

---

## V-01 — C-42 PARTIAL (TRIAD header unlabeled) + C-43 PASS (Row # column) + Arch-first

**axis:** C-42-partial-triad-unlabeled, C-43-pass-row-column-all-eval-steps, role-sequence-arch-first
**hypothesis:** PARTIAL boundary holds under Arch-first: the TRIAD header remains the sole
unlabeled criterion-bearing structural element. All other structural elements — AUTO-RULE
contamination guard header, cross-step guard headers, step headings, completion gate headers,
template slot headers, canary block — carry `[C-NN]` labels at definition sites. The TRIAD
block's per-rule inline labels ([EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE]) provide
criterion identity at the rule level without the block-level `[C-NN]` label. Role sequence
change (Arch-first) does not affect the labeling pattern; C-43 PASS via Row # column in all
three evaluation-step tables.
**C-42:** PARTIAL — TRIAD header carries no `[C-NN]` labels; all other criterion-bearing
structural elements (AUTO-RULE guard header, cross-step guard headers, step headings,
completion gate headers, template slot headers, canary block) carry labels at definition
sites. The boundary element is the TRIAD block header.
**C-43:** PASS — Architect, Strategy, and PM evaluation steps each present sub-questions in
a `| Row # | Sub-question |` table with dedicated leftmost Row # column.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION (C-22):
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring
  a positive argument against inertia. Absence of disqualification is not positive evidence.
  The inertia structure forces a genuine contrastive argument — confirmation that nothing
  is wrong does not earn MOCK-ACCEPTED.

---

STEP 1 — READ (C-08)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->

Read {mock-artifact-path}. Extract namespace name, Category field, and Status field from each
namespace section. Read TOPICS.md; record tier for {topic} (C-08) and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG (C-01, C-02, C-06)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Three rules. All mandatory. Fire before role evaluation. Not role-overridable (C-02).

  RULE 1 — EVIDENCE-HEAVY (all tiers) [C-06]:
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+) [C-06, C-08]:
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active) [C-06]:
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE

Output two lists (C-01):
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

AUTO-RULE CONTAMINATION GUARD (C-17, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Any verdict applied to an auto-flagged namespace is void.

DO NOT proceed to STEP 3 (Architect Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only) (C-07, C-13, C-36)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

For each remaining namespace, answer sub-questions using entity-naming grammar (C-15).
Yes/no answers do not satisfy entity-naming sub-question requirements (C-15).
Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to Strategy (C-36, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply Strategy Evaluation (STEP 4) to these namespaces.
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names Strategy
  Evaluation (STEP 4) as the suppressed step. Arch-first design: C-36 ✓, C-35 N/A.
  Named error: ARCH-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Strategy Evaluation: [{list}]

STEP 3 COMPLETION GATE (C-18, C-28, C-40):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 4 (Strategy Evaluation) until Architect verdicts and guard
  assignments are complete for all remaining namespaces.

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only) (C-07, C-13)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Entry condition (C-17, C-36): STEP 4 applies ONLY to namespaces not on the Arch-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.] |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM (C-40):
<!-- C-42: Named guard header carries criterion-ID label at definition site. -->
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM
  Evaluation (STEP 5) as the suppressed step.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation: [{list}]

STEP 4 COMPLETION GATE (C-18, C-28, C-40):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and guard assignments
  are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Entry condition (C-17, C-36, C-40): STEP 5 applies ONLY to namespaces not on the Arch-blocked
or Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE (C-18, C-28, C-40):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for
  every qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Trigger field: named, parseable artifact field at fixed position (second line of every block).
  Values (C-06, C-19): trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                                  STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-43):
<!-- C-38: Cross-template structural relationship at template definition site.
  C-40: Criterion-ID label in block header.
  C-41 + C-43: Dedicated leftmost Row # column. -->
| Row # | REAL-REQUIRED evaluation field             | MOCK-ACCEPTED structural analog                      |
|-------|--------------------------------------------|------------------------------------------------------|
| 1     | Decision: REAL-REQUIRED                    | Decision: MOCK-ACCEPTED                              |
| 2     | trigger = {rule label}                     | trigger = n/a                                        |
| 3     | Failing evaluation: {role name}            | reason-code: [exact code from enumeration]           |
| 4     | Failing verdict: {full verdict string}     | Structural position: [SQ-1 anchor — tier decision]  |
| 5     | SQ answer driving verdict:                 | Contrast: [contrasting namespace type +              |
|       |   {artifact-as-subject form}               |   structural factor distinguishing it]               |
| 6     | Artifact state: {art-subj, pres-tense}     | (no analog — MOCK-ACCEPTED exits before next-steps)  |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                          |

Row 5 grammar constraint (C-21, C-32):
  SQ answer: present-tense, artifact as grammatical subject. ERROR — VERDICT-ECHO: role as subject.
  "Section 4.1 contains no tier-boundary gate" = valid. "Architect found no gate" = VERDICT-ECHO.

MOCK-ACCEPTED template (C-03, C-10, C-20, C-22, C-23, C-25, C-30):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes — C-03)

  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1, C-20, C-25):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.]

REAL-REQUIRED template — evaluation-driven (C-06, C-14, C-19, C-21, C-24):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. ERROR — VERDICT-ECHO: role as subject.]
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry (C-24)]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 (Write Review Artifact) until all decision blocks are complete.

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement (required output — C-09):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"
    Include urgency grouping commentary for each priority group if more than one namespace.

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable) (C-04)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->

Edit {mock-artifact-path} in-place using Edit tool. Replace Status fields only. Do not
rewrite any other content.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY OUTPUT (C-12, C-16, C-40):
<!-- C-42: Canary output block carries criterion-ID labels at definition site. -->
  After completing all edits, verify before confirming.
  CANARY ASSERTION (write only when condition is verified true):
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK (awaiting review).
  Named error: CANARY-FALSE-POSITIVE — writing the canary when the condition is not met.
  If condition not met: output "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-02 — C-42 FAIL (only decision-block slots labeled) + C-43 PASS (Row # column) + Strategy-first

**axis:** C-42-fail-decision-slots-only, C-43-pass-row-column-all-eval-steps, role-sequence-strat-first
**hypothesis:** FAIL floor holds under Strategy-first: only core decision-block template slot
headers carry criterion-ID labels (reason-code, Structural position, Contrast, Artifact state
in the MOCK-ACCEPTED and REAL-REQUIRED templates). All structural scaffolding — TRIAD header,
TRIAD per-rule inline labels, AUTO-RULE contamination guard header, cross-step guard headers,
step headings, completion gate headers, canary block — are unlabeled. This is the FAIL floor
pattern per v20 C-42 definition: labeling only at template slot level, not at guard/step/
canary level. Role sequence change (Strategy-first vs R19 V-02 Arch-first) confirms the FAIL
floor is a labeling property, not an ordering property. C-43 PASS is independent of labeling
level: Row # column in all three evaluation tables.
**C-42:** FAIL — only core decision-block template slot headers carry criterion-ID labels
(reason-code, Structural position, Contrast, Artifact state); TRIAD header, per-rule inline
labels, AUTO-RULE guard header, cross-step guard headers, step headings, completion gate
headers, and canary block all carry no `[C-NN]` annotations.
**C-43:** PASS — Strategy, Architect, and PM evaluation steps each use `| Row # | Sub-question |`
format with dedicated leftmost Row # column.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION (C-22):
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring
  a positive argument against the default. The inertia structure forces a genuine contrastive
  argument — confirmation that nothing is wrong does not earn MOCK-ACCEPTED.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category field, and Status field from
each namespace section. Read TOPICS.md for tier and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace fields are extracted and listed.

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

DO NOT proceed to STEP 3 (Strategy Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions using entity-naming grammar.
Yes/no answers do not satisfy entity-naming sub-question requirements.
Table with dedicated Row # column.

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.] |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to Architect:
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply Architect Evaluation (STEP 4) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names Architect
  Evaluation (STEP 4) as the suppressed step. Strategy-first design: C-35 ✓, C-36 N/A.
  Named error: STRATEGY-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to Architect Evaluation: [{list}]

DO NOT proceed to STEP 4 (Architect Evaluation) until Strategy verdicts and guard assignments
are complete for all remaining namespaces.

---

STEP 4 — ARCHITECT EVALUATION (non-auto, non-Strategy-blocked namespaces only)

Entry condition: STEP 4 applies ONLY to namespaces not on the Strategy-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column.

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM:
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names PM Evaluation
  (STEP 5) as the suppressed step.
  Named error: ARCH-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to PM Evaluation: [{list}]

DO NOT proceed to STEP 5 (PM Evaluation) until Architect verdicts and guard assignments
are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces not on the Strategy-blocked or
Arch-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column.

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for
every qualifying namespace.

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
| 6     | Artifact state: {art-subj, pres-tense}     | (no analog — exits before next-steps)                |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                          |

Row 5 grammar constraint:
  SQ answer: present-tense, artifact as grammatical subject. ERROR — VERDICT-ECHO: role as subject.

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code [C-03]: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]

  Structural position (SLOT 1 — Strategy SQ-1 anchor) [C-23, C-30]:
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision.
    Generic adequacy statement = SLOT-VIOLATION. Classify: STRUCTURAL-FORM | TIER-GATING.]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1) [C-20, C-25]:
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.]

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict: [present-tense, artifact as subject — C-21]
  Artifact state [C-24]: [present-tense, artifact as subject — propagates to next-steps]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 (Write Review Artifact) until all decision blocks are complete.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
  Coverage Review table: | Namespace | Category | Decision | trigger |
  Ordering rule (state explicitly): "Critical namespaces first, non-critical evaluation-driven
  next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement (C-09):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place. Replace Status fields only.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [...] or Status: REAL-REQUIRED [...]

CANARY OUTPUT (C-12, C-16, C-40):
  After completing all edits, verify before confirming.
  CANARY ASSERTION: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK (awaiting review).
  Named error: CANARY-FALSE-POSITIVE.
  If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-03 — C-42 PASS (all labeled, TRIAD included) + C-43 PASS (Row # column) + Arch-first + Inertia-heavy

**axis:** C-42-pass-triad-header-labeled, C-43-pass-row-column, role-sequence-arch-first, inertia-framing-heavy
**hypothesis:** Inertia framing axis is independent of labeling level and column format.
A named RESISTANCE METRIC block at the skill level — giving the inertia argument a
mechanical structure with named slots — provides stronger C-22 signal without disturbing
labeling or Row # column behavior. The DEFAULT DECISION POSITION expands from a short
statement to a multi-slot checklist requiring the author to explicitly name the positive
argument before MOCK-ACCEPTED is permitted. C-42 PASS and C-43 PASS are stable across
this axis change. Arch-first (Arch→Strat→PM): C-36 ✓, C-35 N/A.
**C-42:** PASS — every criterion-bearing structural element carries a `[C-NN]` label: TRIAD
header [C-11][C-27], AUTO-RULE contamination guard [C-17], cross-step guard headers
[C-36][C-40], step headings, completion gate headers [C-18][C-28], template slot headers
[C-23][C-25][C-30], and canary block [C-12][C-16].
**C-43:** PASS — all three evaluation-step sub-question tables use `| Row # | Sub-question |`
format with dedicated leftmost Row # column.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION (C-22):
  REAL-REQUIRED is the default and starting position for every namespace.
  MOCK-ACCEPTED requires passing the RESISTANCE CHECK below before it may be written.

  RESISTANCE CHECK — required before writing any MOCK-ACCEPTED decision:
    [ ] Positive argument named: state the specific positive property — not merely the
        absence of disqualification — that demonstrates this namespace is appropriate for mock.
    [ ] Contrastive argument present: name a namespace type that would require real evidence
        and state the structural factor distinguishing this namespace from that type.
    [ ] SQ-1 anchor confirmed: the tier decision this namespace feeds is STRUCTURAL-FORM
        (not TIER-GATING); a TIER-GATING namespace cannot pass the resistance check.
  A MOCK-ACCEPTED decision that has not passed all three resistance-check items is invalid.
  Writing MOCK-ACCEPTED when any item is unchecked = named error: RESISTANCE-CHECK-BYPASS.

---

STEP 1 — READ (C-08)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->

Read {mock-artifact-path}. Extract namespace name, Category field, and Status field from each
namespace section. Read TOPICS.md; record tier for {topic} (C-08) and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG (C-01, C-02, C-06)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Three rules. All mandatory. Fire before role evaluation. Not role-overridable (C-02).

  RULE 1 — EVIDENCE-HEAVY (all tiers) [C-06]:
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+) [C-06, C-08]:
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active) [C-06]:
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE

Output two lists (C-01):
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD [C-11] [C-27] (3 rules, all required — C-29: co-located at phase gate):
<!-- C-42: TRIAD header carries full criterion-ID label set at definition site.
  C-11: forbidden-output enumeration present for all 3 rules.
  C-27: individually labeled DO NOT statements form enumerable, mechanically verifiable set.
  C-29: block positioned at phase gate, independent of role sequence. -->
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check [C-27]: all 3 labels present. A two-of-three set does not satisfy.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Any verdict applied to an auto-flagged namespace is void.

DO NOT proceed to STEP 3 (Architect Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only) (C-07, C-13, C-36)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

For each remaining namespace, answer sub-questions using entity-naming grammar (C-15).
Yes/no answers do not satisfy entity-naming sub-question requirements (C-15).
Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to Strategy (C-36, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply Strategy Evaluation (STEP 4) to these namespaces.
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names Strategy
  Evaluation (STEP 4) as the suppressed step. Arch-first design: C-36 ✓, C-35 N/A.
  Named error: ARCH-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Strategy Evaluation: [{list}]

STEP 3 COMPLETION GATE (C-18, C-28, C-40):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 4 (Strategy Evaluation) until Architect verdicts and guard
  assignments are complete for all remaining namespaces.

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only) (C-07, C-13)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Entry condition (C-17, C-36): STEP 4 applies ONLY to namespaces not on the Arch-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column (C-43).

Note: RESISTANCE CHECK from DEFAULT DECISION POSITION applies here — Strategy SQ-1 must
classify the namespace's tier decision as STRUCTURAL-FORM before MOCK-ACCEPTED is available.

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support, and classify it: STRUCTURAL-FORM or TIER-GATING. [TIER-GATING classification blocks MOCK-ACCEPTED regardless of other verdicts. This answer propagates to the Structural position SQ-1 anchor and to the RESISTANCE CHECK SQ-1 item.] |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM (C-40):
<!-- C-42: Named guard header carries criterion-ID label at definition site. -->
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM
  Evaluation (STEP 5) as the suppressed step.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation: [{list}]

STEP 4 COMPLETION GATE (C-18, C-28, C-40):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and guard assignments
  are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Entry condition (C-17, C-36, C-40): STEP 5 applies ONLY to namespaces not on the
Arch-blocked or Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE (C-18, C-28, C-40):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for
  every qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Trigger field: named, parseable artifact field at fixed position (second line of every block).
  Values (C-06, C-19): trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                                  STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-43):
<!-- C-38: Cross-template structural relationship at template definition site.
  C-40: Criterion-ID label in block header.
  C-41 + C-43: Dedicated leftmost Row # column. -->
| Row # | REAL-REQUIRED evaluation field             | MOCK-ACCEPTED structural analog                      |
|-------|--------------------------------------------|------------------------------------------------------|
| 1     | Decision: REAL-REQUIRED                    | Decision: MOCK-ACCEPTED                              |
| 2     | trigger = {rule label}                     | trigger = n/a                                        |
| 3     | Failing evaluation: {role name}            | reason-code: [exact code from enumeration]           |
| 4     | Failing verdict: {full verdict string}     | Structural position: [SQ-1 anchor — tier decision]  |
| 5     | SQ answer driving verdict:                 | Contrast: [contrasting namespace type +              |
|       |   {artifact-as-subject form}               |   structural factor distinguishing it]               |
| 6     | Artifact state: {art-subj, pres-tense}     | (no analog — MOCK-ACCEPTED exits before next-steps)  |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                          |

Row 5 grammar constraint (C-21, C-32):
  SQ answer: present-tense, artifact as grammatical subject. ERROR — VERDICT-ECHO: role as subject.

MOCK-ACCEPTED template (C-03, C-10, C-20, C-22, C-23, C-25, C-30):
  [RESISTANCE CHECK must be complete before writing this block.]
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes — C-03)

  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Classify: STRUCTURAL-FORM (required to pass RESISTANCE CHECK).
    Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1, C-20, C-25):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.
    This slot satisfies RESISTANCE CHECK item 2 (contrastive argument present).]

REAL-REQUIRED template — evaluation-driven (C-06, C-14, C-19, C-21, C-24):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. ERROR — VERDICT-ECHO: role as subject.]
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry (C-24)]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 (Write Review Artifact) until all decision blocks are complete.

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement (required output — C-09):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"
    Include urgency grouping commentary for each priority group if more than one namespace.

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable) (C-04)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->

Edit {mock-artifact-path} in-place using Edit tool. Replace Status fields only. Do not
rewrite any other content.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY OUTPUT (C-12, C-16, C-40):
<!-- C-42: Canary output block carries criterion-ID labels at definition site. -->
  After completing all edits, verify before confirming.
  CANARY ASSERTION (write only when condition is verified true):
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK (awaiting review).
  Named error: CANARY-FALSE-POSITIVE — writing the canary when the condition is not met.
  If condition not met: output "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-04 — C-42 PASS (all labeled, TRIAD included) + C-43 PASS (Row # column) + Strategy-first + Conversational register

**axis:** C-42-pass-triad-header-labeled, C-43-pass-row-column, role-sequence-strat-first, phrasing-register-conversational
**hypothesis:** Phrasing register (conversational/descriptive vs imperative/prescriptive) is
orthogonal to labeling level and column format. The criterion-ID comment annotations and Row #
column are formatting elements that survive a shift to explanatory/descriptive phrasing: the
skill body reads as a teaching document that explains *why* each step exists rather than purely
commanding what to do, while all mechanical requirements (TRIAD, contamination guard, gates,
templates) remain present. C-42 PASS and C-43 PASS are stable under register shift.
Strategy-first (Strat→Arch→PM): C-35 ✓, C-36 N/A.
**C-42:** PASS — every criterion-bearing structural element carries a `[C-NN]` label including
TRIAD header [C-11][C-27]; register shift does not remove comment annotations.
**C-43:** PASS — all three evaluation-step sub-question tables use `| Row # | Sub-question |`
format with dedicated leftmost Row # column.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION (C-22):
  The skill treats REAL-REQUIRED as the ground state for every namespace. MOCK-ACCEPTED
  is not a symmetric alternative — it is an earned release from that ground state. To earn
  release, the author must construct a positive argument: name what is structurally true
  about this namespace that distinguishes it from namespaces that need real evidence. The
  absence of obvious problems is not a positive argument; it is simply the absence of a
  negative finding, which leaves the namespace in its ground state.

---

STEP 1 — READ (C-08)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->

The first task is to establish the operating context. Read {mock-artifact-path} and extract
three fields from each namespace section: the namespace name, its Category field (which
determines auto-flag eligibility), and its Status field (which will be rewritten in Step 8).
Then read TOPICS.md to determine the tier for {topic} — tier governs which TIER-CRITICAL
namespaces apply — and check for any compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG (C-01, C-02, C-06)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Before any human role evaluates anything, three automatic rules must run to exhaustion. These
rules are not overridable by any role evaluation: a namespace that trips an auto-rule is
decided before evaluation begins (C-02). Running evaluation on an auto-flagged namespace
contaminates the output.

  RULE 1 — EVIDENCE-HEAVY (all tiers) [C-06]:
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
    Rationale: evidence-heavy namespaces carry outcome-determining information that a mock
    cannot plausibly replicate.
  RULE 2 — TIER-CRITICAL (Tier 2+) [C-06, C-08]:
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
    Rationale: at Tier 2+, these namespaces gatekeep decisions whose accuracy cannot be
    validated from structural form alone.
  RULE 3 — COMPLIANCE (when active) [C-06]:
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE
    Rationale: regulatory or legal requirements cannot be satisfied by a mock artifact.

After applying all three rules, produce two lists (C-01):
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD [C-11] [C-27] (3 rules, all required — C-29: co-located at phase gate):
<!-- C-42: TRIAD header carries full criterion-ID label set at definition site.
  C-11: forbidden-output enumeration present for all 3 rules.
  C-27: individually labeled DO NOT statements form enumerable, mechanically verifiable set.
  C-29: block positioned at phase gate, independent of role sequence. -->
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check [C-27]: all 3 labels present. A two-of-three set does not satisfy.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  Role evaluation is only appropriate for namespaces that have not been decided by an
  automatic rule. Applying evaluation to an auto-flagged namespace is the AUTO-RULE
  CONTAMINATION error. Any verdict produced by evaluation of an auto-flagged namespace
  is void and must not appear in the decision output.

DO NOT proceed to STEP 3 (Strategy Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only) (C-07, C-13, C-35)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Strategy runs first because tier anchoring must be established before structural analysis
begins (C-35). The Strategy role asks: does running this namespace as mock give the team
a false sense of coverage for the tier decision it supports? Sub-questions use entity-naming
grammar (C-15) — answers must name a specific artifact, section, or decision, not produce
a yes/no or general assessment. Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.] |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to Architect (C-35, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  A namespace whose coverage is insufficient for the tier decision it supports does not
  need an architectural plausibility check — the coverage failure is disqualifying on its
  own. For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}: assign
  preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE, and DO NOT apply
  Architect Evaluation (STEP 4) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names Architect
  Evaluation (STEP 4) as the suppressed step. Strategy-first design satisfies C-35: the
  tier anchor is the prerequisite input for structural contradiction checking.
  Named error: STRATEGY-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to Architect Evaluation: [{list}]

STEP 3 COMPLETION GATE (C-18, C-28, C-40):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 4 (Architect Evaluation) until Strategy verdicts and guard
  assignments are complete for all remaining namespaces.

---

STEP 4 — ARCHITECT EVALUATION (non-auto, non-Strategy-blocked namespaces only) (C-07, C-13, C-26)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

The Architect role checks whether the mock's structural claims are consistent with what is
actually known about the system. A structurally complete mock that contradicts known
architecture is not a useful starting point for real evidence gathering — it would need to
be redesigned before real investigation could begin. Entry condition (C-17, C-26, C-35):
STEP 4 applies ONLY to namespaces not on the Strategy-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM (C-26, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  A namespace whose mock contradicts known architecture cannot produce a structurally
  adequate output regardless of what the PM finds. For any namespace where
  architect-verdict = CONTRADICTS-ARCHITECTURE: assign preliminary decision =
  REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE, and DO NOT apply PM Evaluation (STEP 5).
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names PM
  Evaluation (STEP 5) as the suppressed step. Distinct from the Strategy-to-Arch guard:
  fires on a different verdict value and suppresses a different downstream step.
  Named error: ARCH-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to PM Evaluation: [{list}]

STEP 4 COMPLETION GATE (C-18, C-28, C-40):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 5 (PM Evaluation) until Architect verdicts and guard assignments
  are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

The PM role asks whether the structural form of the mock is complete enough to support a
MOCK-ACCEPTED decision. A mock that passes Strategy and Architect checks but lacks required
sections or enforcement gates is incomplete in a way that evaluation cannot fix — the mock
artifact itself would need revision before the namespace can earn MOCK-ACCEPTED.
Entry condition (C-17, C-26, C-35, C-40): STEP 5 applies ONLY to namespaces not on the
Strategy-blocked or Arch-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE (C-18, C-28, C-40):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for
  every qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Each namespace now receives a final decision block. The trigger field appears at fixed
position (second line) and is machine-readable (C-19). The cross-template table below shows
the structural relationship between REAL-REQUIRED and MOCK-ACCEPTED fields: each row maps
a REAL-REQUIRED field to its MOCK-ACCEPTED analog, making the template correspondence
explicit (C-38).

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-43):
<!-- C-38: Cross-template structural relationship at template definition site.
  C-40: Criterion-ID label in block header.
  C-41 + C-43: Dedicated leftmost Row # column. -->
| Row # | REAL-REQUIRED evaluation field             | MOCK-ACCEPTED structural analog                      |
|-------|--------------------------------------------|------------------------------------------------------|
| 1     | Decision: REAL-REQUIRED                    | Decision: MOCK-ACCEPTED                              |
| 2     | trigger = {rule label}                     | trigger = n/a                                        |
| 3     | Failing evaluation: {role name}            | reason-code: [exact code from enumeration]           |
| 4     | Failing verdict: {full verdict string}     | Structural position: [SQ-1 anchor — tier decision]  |
| 5     | SQ answer driving verdict:                 | Contrast: [contrasting namespace type +              |
|       |   {artifact-as-subject form}               |   structural factor distinguishing it]               |
| 6     | Artifact state: {art-subj, pres-tense}     | (no analog — MOCK-ACCEPTED exits before next-steps)  |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                          |

Row 5 grammar constraint (C-21, C-32):
  SQ answer must use present-tense with the artifact as grammatical subject, not the role.
  "Section 4.1 contains no tier-boundary gate" is valid (artifact as subject).
  "Architect found no gate" is the VERDICT-ECHO error (role as subject).

MOCK-ACCEPTED template (C-03, C-10, C-20, C-22, C-23, C-25, C-30):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only — C-03; paraphrase or invented code = REASON-CODE-VIOLATION)

  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1, C-20, C-25):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. A sentence that only confirms the namespace is adequate — without naming
    a contrasting namespace type and the factor that distinguishes it — is the
    CONTRAST-INCOMPLETE error. A single Rationale slot that combines both Structural
    position and Contrast without the dedicated SLOT 2 structure = RATIONALE-INCOMPLETE.]

REAL-REQUIRED template — evaluation-driven (C-06, C-14, C-19, C-21, C-24):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. The specific SQ answer — not the role's conclusion —
    that produced the failing verdict. ERROR — VERDICT-ECHO: role as subject.]
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry (C-24)]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 (Write Review Artifact) until all decision blocks are complete.

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Write simulations/mock/{topic}-review-{date}.md. The artifact serves as the persistent
record of the coverage review and the action list for the next cycle of work.

  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  The ordering rule governs the next-steps list priority:
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."
  State this rule explicitly in the artifact so the ordering is traceable (C-05).

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement (required output — C-09):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"
    Include urgency grouping commentary for each priority group if more than one namespace.

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable) (C-04)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->

The in-place edit is what makes this skill's decisions durable. Edit {mock-artifact-path}
using the Edit tool. Replace Status fields only — do not rewrite any other content. The
in-place edit is the defining behavior of this skill (C-04).

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY OUTPUT (C-12, C-16, C-40):
<!-- C-42: Canary output block carries criterion-ID labels at definition site. -->
  After completing all edits, verify the condition before writing the canary assertion.
  The canary is a truth-conditional output: writing it when the condition is not met is
  the CANARY-FALSE-POSITIVE error.
  CANARY ASSERTION (write only when condition is verified true):
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK (awaiting review).
  If condition not met: output "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-05 — C-42 PASS + belt-and-suspenders (per-row [C-15] in SQ cells) + C-43 PASS + Arch-first + Lifecycle emphasis

**axis:** C-42-pass-belt-and-suspenders-per-row-C15, C-43-pass-row-column, role-sequence-arch-first, lifecycle-emphasis-expanded
**hypothesis:** Ceiling test per v20 C-42 definition. Adding per-row `[C-15]` labels inside
SQ table cells — redundant with the column-level `| Row # |` header since C-43 already
provides row-position scannability — is belt-and-suspenders redundancy. Per v20 C-42:
"it does not earn above PASS, but it does not fail the criterion." The ceiling is PASS;
the belt-and-suspenders cells are informative at the usage site but do not constitute a
labeling failure. Lifecycle emphasis axis: expanded per-step phase rationale commentary
— each step includes a brief rationale sentence explaining its role in the overall lifecycle
before the operational content. This axis tests compatibility of narrative enrichment with
full criterion coverage. Arch-first (Arch→Strat→PM): C-36 ✓, C-35 N/A.
**C-42:** PASS (belt-and-suspenders ceiling) — every criterion-bearing structural element
carries a `[C-NN]` label: TRIAD header [C-11][C-27], AUTO-RULE contamination guard [C-17],
cross-step guard headers [C-36][C-26], step headings, completion gate headers [C-18][C-28],
template slot headers [C-23][C-25][C-30], canary block [C-12][C-16]. Per-row [C-15]
annotations inside SQ table cells are redundant belt-and-suspenders; they are still PASS.
**C-43:** PASS — all three evaluation-step sub-question tables use `| Row # | Sub-question |`
format with dedicated leftmost Row # column; per-row cell annotations do not replace
the column structure.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION (C-22):
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring
  a positive argument against inertia. Absence of disqualification is not positive evidence.
  The inertia structure forces a genuine contrastive argument — confirmation that nothing
  is wrong does not earn MOCK-ACCEPTED.

---

STEP 1 — READ (C-08)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->
Lifecycle role: establishes the operating inputs (namespace fields, tier, compliance tags)
that all subsequent steps consume. No decisions are produced here.

Read {mock-artifact-path}. Extract namespace name, Category field, and Status field from each
namespace section. Read TOPICS.md; record tier for {topic} (C-08) and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
Namespace extraction table:
  | Namespace | Category | Status |
  (One row per namespace section in the mock artifact.)

DO NOT proceed to STEP 2 (Auto-Flag) until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG (C-01, C-02, C-06)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->
Lifecycle role: applies the three categorical rules that decide namespaces without
evaluation. Produces the two-list partition that governs the entire evaluation phase.
Rule application is the only activity in this step; no evaluation, no role verdicts.

Three rules. All mandatory. Fire before role evaluation. Not role-overridable (C-02).

  RULE 1 — EVIDENCE-HEAVY (all tiers) [C-06]:
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+) [C-06, C-08]:
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active) [C-06]:
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE

Output two lists (C-01):
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED): [{namespace}: Category = {value}]

Two-list partition summary:
  Auto-flagged count: {N}
  Remaining for evaluation: {N}
  (These counts must sum to total namespace count from STEP 1.)

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================
Lifecycle role: hard boundary between categorical decisions and evaluative decisions.
Both the FORBIDDEN OUTPUTS TRIAD and the AUTO-RULE CONTAMINATION GUARD are positioned
here so that they govern the entire evaluation phase independent of role sequence.

FORBIDDEN OUTPUTS TRIAD [C-11] [C-27] (3 rules, all required — C-29: co-located at phase gate):
<!-- C-42: TRIAD header carries full criterion-ID label set at definition site.
  C-11: forbidden-output enumeration present for all 3 rules.
  C-27: individually labeled DO NOT statements form enumerable, mechanically verifiable set.
  C-29: block positioned at phase gate, independent of role sequence. -->
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check [C-27]: all 3 labels present. A two-of-three set does not satisfy.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Any verdict applied to an auto-flagged namespace is void.

DO NOT proceed to STEP 3 (Architect Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only) (C-07, C-13, C-36)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->
Lifecycle role: structural plausibility gate. Runs first so that architectural contradictions
are identified before tier-coverage analysis begins (C-36). Namespaces that contradict
architecture do not proceed to Strategy or PM evaluation.

For each remaining namespace, answer sub-questions using entity-naming grammar (C-15).
Yes/no answers do not satisfy entity-naming sub-question requirements (C-15).
Table with dedicated Row # column (C-43). Per-row [C-15] annotations inside cells are
belt-and-suspenders — they label the entity-naming requirement at the usage site, redundant
with the column-header approach but not failing C-42 or C-43 per v20 definition.

| Row # | Sub-question |
|-------|-------------|
| 1 [C-15] | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2 [C-15] | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3 [C-15] | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to Strategy (C-36, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply Strategy Evaluation (STEP 4) to these namespaces.
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names Strategy
  Evaluation (STEP 4) as the suppressed step. Arch-first design: C-36 ✓, C-35 N/A.
  Named error: ARCH-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Strategy Evaluation: [{list}]

STEP 3 COMPLETION GATE (C-18, C-28, C-40):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 4 (Strategy Evaluation) until Architect verdicts and guard
  assignments are complete for all remaining namespaces.

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only) (C-07, C-13)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->
Lifecycle role: coverage adequacy gate. Assesses whether the namespace's mock coverage
is sufficient for the tier decision it supports. Runs after Architect to consume the
architectural plausibility check as prerequisite context (C-36 arc: Arch result informs
Strategy's plausibility baseline).

Entry condition (C-17, C-36): STEP 4 applies ONLY to namespaces not on the Arch-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column (C-43). Per-row [C-15] annotations as belt-and-suspenders.

| Row # | Sub-question |
|-------|-------------|
| 1 [C-15] | Name the specific Tier {tier} decision this namespace is intended to support. [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.] |
| 2 [C-15] | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3 [C-15] | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM (C-40):
<!-- C-42: Named guard header carries criterion-ID label at definition site. -->
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM
  Evaluation (STEP 5) as the suppressed step.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation: [{list}]

STEP 4 COMPLETION GATE (C-18, C-28, C-40):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and guard assignments
  are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->
Lifecycle role: structural completeness gate. The final evaluation role. Only namespaces
that have passed both Architect and Strategy gates reach PM. PM verifies that the mock
artifact has the sections, gates, and output structures required to support the decision.

Entry condition (C-17, C-36, C-40): STEP 5 applies ONLY to namespaces not on the Arch-blocked
or Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column (C-43). Per-row [C-15] annotations as belt-and-suspenders.

| Row # | Sub-question |
|-------|-------------|
| 1 [C-15] | Name the required sections present in the mock artifact for this namespace. |
| 2 [C-15] | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3 [C-15] | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE (C-18, C-28, C-40):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for
  every qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->
Lifecycle role: decision assembly. Combines auto-flag results, evaluation-driven verdicts,
and the inertia structure (C-22) into per-namespace decision blocks. Each block is a
complete, independently parseable record of the decision and its justification.

Trigger field: named, parseable artifact field at fixed position (second line of every block).
  Values (C-06, C-19): trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                                  STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-43):
<!-- C-38: Cross-template structural relationship at template definition site.
  C-40: Criterion-ID label in block header.
  C-41 + C-43: Dedicated leftmost Row # column. -->
| Row # | REAL-REQUIRED evaluation field             | MOCK-ACCEPTED structural analog                      |
|-------|--------------------------------------------|------------------------------------------------------|
| 1     | Decision: REAL-REQUIRED                    | Decision: MOCK-ACCEPTED                              |
| 2     | trigger = {rule label}                     | trigger = n/a                                        |
| 3     | Failing evaluation: {role name}            | reason-code: [exact code from enumeration]           |
| 4     | Failing verdict: {full verdict string}     | Structural position: [SQ-1 anchor — tier decision]  |
| 5     | SQ answer driving verdict:                 | Contrast: [contrasting namespace type +              |
|       |   {artifact-as-subject form}               |   structural factor distinguishing it]               |
| 6     | Artifact state: {art-subj, pres-tense}     | (no analog — MOCK-ACCEPTED exits before next-steps)  |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                          |

Row 5 grammar constraint (C-21, C-32):
  SQ answer: present-tense, artifact as grammatical subject. ERROR — VERDICT-ECHO: role as subject.
  "Section 4.1 contains no tier-boundary gate" = valid. "Architect found no gate" = VERDICT-ECHO.

MOCK-ACCEPTED template (C-03, C-10, C-20, C-22, C-23, C-25, C-30):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes — C-03)

  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1, C-20, C-25):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.]

REAL-REQUIRED template — evaluation-driven (C-06, C-14, C-19, C-21, C-24):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. ERROR — VERDICT-ECHO: role as subject.]
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry (C-24)]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 (Write Review Artifact) until all decision blocks are complete.

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->
Lifecycle role: persistence of the coverage review. The artifact written here becomes
the durable record of decisions and the authoritative action list. Its ordering rule is
not advisory — it establishes which real-evidence work is blocking vs. non-blocking.

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in artifact — C-05):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement (required output — C-09):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"
    Include urgency grouping commentary for each priority group if more than one namespace.

  Lifecycle state summary (expanded — lifecycle emphasis axis):
    "Phase complete: coverage review decisions assembled.
     Auto-flagged: {N} namespaces (trigger = {list}).
     Evaluation-driven REAL-REQUIRED: {N} namespaces.
     MOCK-ACCEPTED: {N} namespaces.
     Proceeding to: write-back (STEP 8)."

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable) (C-04)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->
Lifecycle role: persistence of decisions into the source artifact. The in-place edit
is the action that makes this skill's decisions durable — it closes the review cycle
by propagating the coverage decisions back into the mock artifact's Status fields.

Edit {mock-artifact-path} in-place using Edit tool. Replace Status fields only. Do not
rewrite any other content.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

  Edit sequence:
    1. Identify all Status fields containing "MOCK (awaiting review)".
    2. For each: apply the decision from STEP 6 decision blocks.
    3. Verify: scan the artifact for any remaining "MOCK (awaiting review)" strings.

CANARY OUTPUT (C-12, C-16, C-40):
<!-- C-42: Canary output block carries criterion-ID labels at definition site. -->
  After completing all edits, verify before confirming.
  CANARY ASSERTION (write only when condition is verified true):
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK (awaiting review).
  Named error: CANARY-FALSE-POSITIVE — writing the canary when the condition is not met.
  If condition not met: output "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

  Lifecycle state summary (expanded — lifecycle emphasis axis):
    "Skill complete.
     Status fields updated: {N} of {N}.
     Review artifact: simulations/mock/{topic}-review-{date}.md.
     Mock artifact: {mock-artifact-path} — all Status fields resolved.
     Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
