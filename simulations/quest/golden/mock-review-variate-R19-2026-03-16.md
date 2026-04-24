---
skill: quest-variate
skill_target: mock-review
date: 2026-03-16
round: 19
rubric_version: v19
status: VARIATE
---

# mock-review Variate — Round 19

**Date:** 2026-03-16
**Skill:** mock-review
**Rubric:** v19 (C-01 through C-43; aspirational denominator = 37)
**Round:** R19 — targeting v19 C-42 and C-43 redefinitions as named PASS/PARTIAL/FAIL levels

---

## What R18 Left Open

R18 achieved C-42 PASS in V-03 (inline SQ-N + TRIAD labeled) and C-42 PARTIAL in V-01/V-04
(TRIAD header unlabeled). R18 combined C-42 PASS + C-43 PASS only in V-05. The v19 rubric
crystallizes the observed patterns into named levels with explicit boundary conditions. R19
tests these boundaries with a full 5-variant matrix covering every combination of C-42 level
× C-43 level × role sequence.

| Criterion | R18 ceiling | R19 target |
|-----------|-------------|-----------|
| C-42 | PASS in V-03/V-05 (TRIAD header labeled) | Confirm PASS boundary is the TRIAD header label; test PARTIAL and FAIL floors |
| C-43 | PASS in V-02/V-04/V-05 (Row # column) | Confirm independence from C-42; test FAIL with inline SQ-N: prefix |

---

## Variation Axes and Hypotheses

| Variation | C-42 | C-43 | Role sequence | Hypothesis |
|-----------|------|------|---------------|-----------|
| V-01 | PARTIAL (TRIAD header unlabeled) | PASS | Strategy-first (C-35 ✓) | The PARTIAL boundary: per-rule inline labels inside the TRIAD carry criterion identity without block-level [C-NN]; TRIAD header is the sole unlabeled element. C-43 PASS achieved via Row # column in all eval tables. |
| V-02 | FAIL (only decision-block slots) | PASS | Arch-first (C-36 ✓) | The FAIL floor: labeling only core decision-block template slots (reason-code, Structural position, Contrast, Artifact state) is insufficient for C-42; guard headers, step headings, canary all unlabeled. C-43 PASS independent of labeling level. |
| V-03 | PASS (all labeled, TRIAD included) | PASS | Strategy-first (C-35 ✓) | The single-element gap: adding [C-11][C-27] to the TRIAD header closes the PARTIAL pattern and achieves PASS. All other elements already labeled; TRIAD header is the boundary element. |
| V-04 | PASS (all labeled, TRIAD included) | FAIL (inline SQ-N:) | Arch-first (C-36 ✓) | Independence test: C-42 PASS and C-43 FAIL coexist. Full criterion-ID labeling on all structural elements achieves C-42 independently; SQ row number encoding (prefix vs column) is a separate dimension. |
| V-05 | PASS (all labeled + per-row [C-15]) | PASS | Arch-first (C-36 ✓) | Ceiling: C-42 PASS achieved with per-SQ-row [C-15] annotations inside table cells (redundant with column header, belt-and-suspenders); C-43 PASS via Row # column; Arch-first establishes that ceiling is reachable under C-36 as well as C-35. |

---

## V-01 — C-42 PARTIAL (TRIAD header unlabeled) + C-43 PASS (Row # column) + Strategy-first

**axis:** C-42-partial-triad-unlabeled, C-43-pass-row-column-all-eval-steps, role-sequence-strat-first
**hypothesis:** The PARTIAL boundary per the v19 rubric definition. TRIAD header carries no
`[C-NN]` labels; all other criterion-bearing structural elements carry labels at definition
sites (AUTO-RULE guard header, cross-step guard headers, step headings, completion gate headers,
template slot headers, canary block). The TRIAD block's per-rule inline labels ([EVIDENCE-HEAVY],
[TIER-CRITICAL], [COMPLIANCE]) provide criterion identity at the rule level; the block-level
label is the one missing element. C-43 PASS: all three evaluation-step sub-question tables use
`| Row # | Sub-question |` format with dedicated leftmost column.
Strategy-first (Strat→Arch→PM): C-35 ✓, C-36 N/A.
**C-42:** PARTIAL — TRIAD header carries no `[C-NN]` labels; all other criterion-bearing
structural elements (AUTO-RULE guard header, cross-step guard headers, step headings, completion
gate headers, template slot headers, canary block) carry labels at definition sites.
**C-43:** PASS — Strategy, Architect, and PM evaluation steps each present sub-questions in
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
  The inertia structure forces a genuine contrastive argument; confirmation that nothing is
  wrong does not earn MOCK-ACCEPTED.

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

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active):
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

DO NOT proceed to STEP 3 (Strategy Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only) (C-07, C-13, C-35)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

For each remaining namespace, answer sub-questions using entity-naming grammar (C-15).
Yes/no answers do not satisfy entity-naming sub-question requirements.
Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.] |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to Architect (C-35, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply Architect Evaluation (STEP 4) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names Architect
  Evaluation (STEP 4) as the suppressed step. Strategy-first design satisfies C-35.
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

Entry condition (C-17, C-26, C-35): STEP 4 applies ONLY to namespaces not on the
Strategy-blocked list. Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM (C-26, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names PM Evaluation
  (STEP 5) as the suppressed step. Distinct from the Strategy-to-Arch guard in STEP 3.
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

Trigger field: named, parseable artifact field at fixed position (second line of every block).
  Values (C-06, C-19): trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                                  STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-43):
<!-- C-38: Cross-template structural relationship at template definition site.
  C-40: Criterion-ID label in block header.
  C-41 + C-43: Dedicated leftmost Row # column. C-43: column form unified across STEPS 3-5
  evaluation tables and this correspondence table. -->
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

## V-02 — C-42 FAIL (only decision-block slots labeled) + C-43 PASS (Row # column) + Arch-first

**axis:** C-42-fail-decision-slots-only, C-43-pass-row-column-all-eval-steps, role-sequence-arch-first
**hypothesis:** The FAIL floor per the v19 rubric definition. Only the core decision-block
template slot headers carry criterion-ID labels (reason-code, Structural position, Contrast,
Artifact state fields in the MOCK-ACCEPTED and REAL-REQUIRED templates). All structural
scaffolding elements — TRIAD header, guard headers, step headings, completion gate headers,
canary block — are unlabeled. C-43 PASS is independent of labeling level: Row # column
in all three evaluation tables still provides positional scannability regardless of which
structural elements carry criterion annotations.
Arch-first (Arch→Strat→PM): C-36 ✓, C-35 N/A.
**C-42:** FAIL — only core decision-block template slot headers carry criterion-ID labels;
TRIAD header, AUTO-RULE guard header, step headings, completion gate headers, and canary
block all carry no `[C-NN]` annotations.
**C-43:** PASS — all three evaluation-step sub-question tables use `| Row # | Sub-question |`
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
  argument; confirmation that nothing is wrong does not earn MOCK-ACCEPTED.

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

DO NOT proceed to STEP 3 (Architect Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions using entity-naming grammar.
Yes/no answers do not satisfy entity-naming sub-question requirements.
Table with dedicated Row # column provides row-position scannability.

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
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names Strategy
  Evaluation (STEP 4) as the suppressed step. Arch-first design: C-36 ✓, C-35 N/A.
  Named error: ARCH-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Strategy Evaluation: [{list}]

DO NOT proceed to STEP 4 (Strategy Evaluation) until Architect verdicts and guard assignments
are complete for all remaining namespaces.

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only)

Entry condition: STEP 4 applies ONLY to namespaces not on the Arch-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column provides row-position scannability.

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
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM
  Evaluation (STEP 5) as the suppressed step.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked: [{list}]
    Proceeding to PM Evaluation: [{list}]

DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and guard assignments
are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces not on the Arch-blocked or Strategy-blocked
lists. Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column provides row-position scannability.

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
| 6     | Artifact state: {art-subj, pres-tense}     | (no analog — exits before next-steps)                |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                          |

Row 5 grammar constraint (C-21, C-32):
  SQ answer: present-tense, artifact as grammatical subject. ERROR — VERDICT-ECHO: role as subject.

MOCK-ACCEPTED template (C-03, C-10, C-20, C-22, C-23, C-25, C-30):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code [C-03]: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]

  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision.
    Generic adequacy statement = SLOT-VIOLATION. Classify: STRUCTURAL-FORM | TIER-GATING.]

  Contrast (SLOT 2 — dedicated, C-20, C-25):
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE.]

REAL-REQUIRED template — evaluation-driven (C-06, C-14, C-19, C-21, C-24):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict: [present-tense, artifact as subject]
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

## V-03 — C-42 PASS (all labeled, TRIAD header included) + C-43 PASS (Row # column) + Strategy-first

**axis:** C-42-pass-triad-header-labeled, C-43-pass-row-column-all-eval-steps, role-sequence-strat-first
**hypothesis:** The single-element gap between PARTIAL and PASS is the TRIAD header label.
Adding `[C-11] [C-27]` to the TRIAD block header closes the gap: the block becomes the named
definition site for C-11 (forbidden-output enumeration), C-27 (triad DO NOT coverage), and
the co-location rule (C-29). All other elements carry labels as established in R18; the TRIAD
header label is the sole addition that moves C-42 from PARTIAL to PASS. Row # column in all
three evaluation tables (C-43 PASS). Strategy-first: C-35 ✓, C-36 N/A.
**C-42:** PASS — every criterion-bearing structural element carries a `[C-NN]` label at its
definition site: TRIAD header [C-11][C-27], AUTO-RULE guard header [C-17], cross-step guard
headers [C-35][C-26], step headings, completion gate headers [C-18][C-28], template slot
headers, and canary block [C-12][C-16].
**C-43:** PASS — all three evaluation-step sub-question tables use `| Row # | Sub-question |`
format with dedicated leftmost Row # column.

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

Read {mock-artifact-path}. Extract namespace name, Category field, Status field per namespace.
Read TOPICS.md; record tier for {topic} (C-08) and compliance tags.

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

DO NOT proceed to STEP 3 (Strategy Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only) (C-07, C-13, C-35)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

For each remaining namespace, answer sub-questions using entity-naming grammar (C-15).
Yes/no answers do not satisfy entity-naming sub-question requirements (C-15).
Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. [This answer propagates to the Structural position SQ-1 anchor slot in every MOCK-ACCEPTED block produced for this namespace.] |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to Architect (C-35, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply Architect Evaluation (STEP 4) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names Architect
  Evaluation (STEP 4) as the suppressed step. Strategy-first design satisfies C-35: tier
  anchoring is established before structural contradiction checking begins.
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

Entry condition (C-17, C-26, C-35): STEP 4 applies ONLY to namespaces not on the
Strategy-blocked list. Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM (C-26, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names PM Evaluation
  (STEP 5) as the suppressed step. Distinct from the Strategy-to-Arch guard in STEP 3:
  fires on a different verdict value and suppresses a different step.
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

Trigger field: named, parseable artifact field at fixed position (second line of every block).
  Values (C-06, C-19): trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                                  STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-43):
<!-- C-38: Cross-template structural relationship encoded at template definition site.
  C-40: Criterion-ID label in block header.
  C-41 + C-43: Dedicated leftmost Row # column — column form unified with STEPS 3-5 tables. -->
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

  Cross-namespace risk statement (C-09):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

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
  If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-04 — C-42 PASS (all labeled, TRIAD included) + C-43 FAIL (inline SQ-N: prefix) + Arch-first

**axis:** C-42-pass-triad-header-labeled, C-43-fail-inline-SQ-prefix, role-sequence-arch-first
**hypothesis:** Independence test: C-42 PASS and C-43 FAIL coexist. Criterion-ID labeling on
all structural elements (TRIAD header, guard headers, step headings, slot headers, canary block)
achieves C-42 PASS independently of the SQ row number encoding format. Inline SQ-N (C-15):
prefix provides per-SQ criterion annotations at the usage site; the row number is embedded in
cell content rather than a dedicated column, which is the C-43 FAIL condition. Arch-first
(Arch→Strat→PM): C-36 ✓, C-35 N/A.
**C-42:** PASS — every criterion-bearing structural element carries a `[C-NN]` label at its
definition site including the TRIAD header [C-11][C-27]; guard headers, step headings,
completion gate headers, template slot headers, and canary block all carry labels.
**C-43:** FAIL — Strategy, Architect, and PM evaluation steps use `SQ-N (C-15):` inline prefix
format; row number is embedded inside cell content, not a dedicated leftmost column.

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

Read {mock-artifact-path}. Extract namespace name, Category field, Status field per namespace.
Read TOPICS.md; record tier for {topic} (C-08) and compliance tags.

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
  C-11: forbidden-output enumeration for all 3 rules.
  C-27: individually labeled DO NOT statements form enumerable set.
  C-29: block positioned at phase gate, independent of role sequence. -->
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check [C-27]: all 3 labels present. Two-of-three does not satisfy.

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
Inline SQ-N prefix format (C-43 FAIL axis for this variant: row number in cell content).

  SQ-1 (C-15): Name the system component, dependency, or interface in the mock that confirms
        plausibility — or: "Contradiction found — name the specific element".
        [C-42: SQ-1 carries entity-naming criterion label at usage site.]
  SQ-2 (C-15): Name the data flow, state transition, or API shape the mock implies for
        {topic} — or: "Inconsistency found — name the specific element".
        [C-42: SQ-2 carries entity-naming criterion label at usage site.]
  SQ-3 (C-15): Name the architectural fact about {topic} this namespace's mock most directly
        depends on. State whether the mock is consistent with that fact.
        [C-42: SQ-3 carries entity-naming criterion label at usage site.]

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
Inline SQ-N prefix format (C-43 FAIL axis: row number in cell content).

  SQ-1 (C-15): Name the specific Tier {tier} decision this namespace is intended to support.
        [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.]
        [C-42: SQ-1 carries entity-naming criterion label at usage site.]
  SQ-2 (C-15): Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED
        (state whether that belief would be correct or incorrect).
        [C-42: SQ-2 carries entity-naming criterion label at usage site.]
  SQ-3 (C-15): Name the coverage gap that would keep this namespace in its REAL-REQUIRED
        default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}".
        [C-42: SQ-3 carries entity-naming criterion label at usage site.]

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM (C-36, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM
  Evaluation (STEP 5) as the suppressed step. Independent of the Arch-to-Strategy guard.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked: [{list}]
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
Inline SQ-N prefix format (C-43 FAIL axis: row number in cell content).

  SQ-1 (C-15): Name the required sections present in the mock artifact for this namespace.
        [C-42: SQ-1 carries entity-naming criterion label at usage site.]
  SQ-2 (C-15): Name the enforcement gate, decision table, or required output structure
        present — or: "Absent — name the missing element and which section defines it".
        [C-42: SQ-2 carries entity-naming criterion label at usage site.]
  SQ-3 (C-15): Name one structural gap that would keep this namespace in its REAL-REQUIRED
        default — or: "No gap — namespace positively demonstrates structural completeness".
        [C-42: SQ-3 carries entity-naming criterion label at usage site.]

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
<!-- C-38: Cross-template structural relationship encoded at template definition site.
  C-40: Criterion-ID label in block header.
  C-41 + C-43: Dedicated leftmost Row # column in this block. Note: evaluation-step
  sub-questions use inline SQ-N prefix (C-43 FAIL axis); this correspondence table retains
  the column form as an independent block-level design decision. -->
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

  Cross-namespace risk statement (C-09):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable) (C-04)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->

Edit {mock-artifact-path} in-place using Edit tool. Replace Status fields only.

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
  Named error: CANARY-FALSE-POSITIVE.
  If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-05 — C-42 PASS (all labeled + per-row [C-15]) + C-43 PASS (Row # column) + Arch-first

**axis:** C-42-pass-triad-header-labeled-per-row-annotations, C-43-pass-row-column-all-eval-steps,
role-sequence-arch-first, lifecycle-depth-maximum
**hypothesis:** Ceiling combination with Arch-first role ordering (C-36 ✓). Adds redundant
per-row [C-15] annotations inside each SQ table cell — belt-and-suspenders on top of the
column header label — establishing that C-42 PASS is fully confirmed when both the table
structure and the cell content carry criterion identity. Maximum lifecycle depth: every
completion gate names both the step number and step descriptive label in the forward reference
(C-28). Arch-first: C-36 ✓, C-35 N/A. Establishes that the ceiling is reachable under C-36
as well as C-35 (V-03).
**C-42:** PASS — every criterion-bearing structural element carries a `[C-NN]` label. TRIAD
header carries [C-11][C-27]. SQ table rows carry [C-15] inside cell content (per-row belt-and-
suspenders beyond column header). All guard headers, step headings, gate headers, slot headers,
and canary block carry labels at definition sites.
**C-43:** PASS — all three evaluation-step sub-question tables use `| Row # | Sub-question [C-15] |`
format; dedicated leftmost Row # column present in all evaluation steps.

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

Read {mock-artifact-path}. Extract namespace name, Category field, Status field per namespace.
Read TOPICS.md; record tier for {topic} (C-08) and compliance tags.

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
  C-11: forbidden-output enumeration present for all 3 rules individually.
  C-27: each rule has its own [RULE-LABEL] DO NOT statement — individually labeled,
  enumerable, mechanically verifiable set. Three-of-three required; two-of-three fails.
  C-29: TRIAD block co-located at phase gate, independent of role sequence. -->
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check [C-27]: all 3 labels present. Two-of-three does not satisfy.

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
Table with dedicated Row # column (C-43). Per-row [C-15] cell annotation (C-42 belt-and-suspenders).

| Row # | Sub-question [C-15] |
|-------|---------------------|
| 1     | [C-15] Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | [C-15] Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | [C-15] Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

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
Table with dedicated Row # column (C-43). Per-row [C-15] cell annotation (C-42 belt-and-suspenders).

| Row # | Sub-question [C-15] |
|-------|---------------------|
| 1     | [C-15] Name the specific Tier {tier} decision this namespace is intended to support. [This answer propagates to the Structural position SQ-1 anchor slot in every MOCK-ACCEPTED block produced for this namespace.] |
| 2     | [C-15] Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | [C-15] Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM (C-36, C-40):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM
  Evaluation (STEP 5) as the suppressed step. Independent of the Arch-to-Strategy guard.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked: [{list}]
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
Table with dedicated Row # column (C-43). Per-row [C-15] cell annotation (C-42 belt-and-suspenders).

| Row # | Sub-question [C-15] |
|-------|---------------------|
| 1     | [C-15] Name the required sections present in the mock artifact for this namespace. |
| 2     | [C-15] Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | [C-15] Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

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
<!-- C-38: Cross-template structural relationship encoded at template definition site.
  C-40: Criterion-ID label in block header.
  C-41 + C-43: Dedicated leftmost Row # column — column form unified with STEPS 3-5 tables.
  Per-row annotation: [C-NN] labels in cell content mirror the belt-and-suspenders pattern
  used in the evaluation-step tables above. -->
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

## Design Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-42 | PARTIAL | FAIL | PASS | PASS | PASS |
| C-43 | PASS | PASS | PASS | FAIL | PASS |
| C-35 (Strategy-first) | PASS | FAIL | PASS | FAIL | FAIL |
| C-36 (Arch-first) | FAIL | PASS | FAIL | PASS | PASS |
| TRIAD header labeled | No | No | Yes | Yes | Yes |
| SQ row format | `\| Row # \|` table | `\| Row # \|` table | `\| Row # \|` table | `SQ-N (C-15):` inline | `\| Row # \| SQ [C-15] \|` + per-row `[C-15]` |
| Guard headers labeled | Yes | No | Yes | Yes | Yes |
| Step headings labeled | Yes | No | Yes | Yes | Yes |
| Canary block labeled | Yes | No | Yes | Yes | Yes |

**C-42 discriminator:** V-01 vs V-03 — the sole difference is the TRIAD header label `[C-11][C-27]`.
V-02 vs V-01 — V-02 strips labels from guard headers, step headings, and canary (the full FAIL pattern).
**C-43 discriminator:** V-04 vs V-03 — identical except SQ format. Confirms C-42 and C-43 are independent.
**C-35/C-36 split:** V-01/V-03 satisfy C-35; V-02/V-04/V-05 satisfy C-36. Both are reachable at the C-42 PASS level.

```json
{"rubric_version": "v19", "round": 19, "new_criteria": ["C-42", "C-43"],
 "c42_boundary": "TRIAD header label is the sole element separating PARTIAL from PASS",
 "c43_boundary": "dedicated leftmost Row # column vs SQ-N: prefix inside cell content",
 "independence_confirmed": "C-42 PASS achievable with C-43 FAIL (V-04); C-43 PASS achievable with C-42 FAIL (V-02)",
 "ceiling_variants": ["V-03 (Strategy-first)", "V-05 (Arch-first)"]}
```
