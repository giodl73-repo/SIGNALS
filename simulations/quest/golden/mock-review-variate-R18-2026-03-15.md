---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 18
rubric_version: v18
status: VARIATE
---

# mock-review Variate — Round 18

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v18 (C-01 through C-43; aspirational denominator = 37)
**Round:** R18 — targeting v18 new criteria: C-42 (universal structural labeling) and C-43
(dedicated leftmost Row # column in all evaluation-step tables)

---

## What R17 Left Open

R17 achieved a ceiling across all five variants with two aspirational criteria unreachable per
variant due to the C-35/C-36 mutual exclusion constraint. The two new R18 criteria emerge from
patterns observed across the full R16/R17 corpus: one about the completeness of criterion-ID
labeling across all named structural elements (not only the 4 C-40 core blocks), the other
about whether the Row # column form extends from the CROSS-TEMPLATE RELATIONSHIP BLOCK into
the evaluation-step sub-question tables themselves.

| Criterion | R17 ceiling coverage | Gap |
|-----------|---------------------|-----|
| **C-42** | R17 V-03/V-05 carry criterion-ID labels on template slots (`Structural position`, `Contrast`), cross-step guard headers, and step completion gates — but the TRIAD header itself received labels inconsistently across variants. C-42 now formally requires: TRIAD header, AUTO-RULE guard header, inline SQ rows (when using inline format), step headings, slot headers, and canary block ALL carry `[C-NN]` labels. The TRIAD header is the single element that divides PASS from PARTIAL: a skill with TRIAD header unlabeled while all other elements are labeled is PARTIAL; a skill that labels only the C-40 core decision/template blocks is FAIL. | C-42 requires universal criterion-ID labeling at every named structural element's definition site. "Named structural element" means: any block, header, slot, guard, gate, or canary output that carries criterion-specific semantics. The 4 C-40 core blocks are a required subset; the full set extends to TRIAD header, guard headers, step headings, template slot headers, and canary block. A skill that labels only the C-40 decision blocks satisfies C-40 but not C-42 — and leaves C-42 FAIL regardless of inline SQ labeling. A skill that labels everything except the TRIAD header is PARTIAL. |
| **C-43** | R17 V-02/V-05 use the dedicated leftmost `Row #` column in the CROSS-TEMPLATE RELATIONSHIP BLOCK. V-01/V-04 use inline `Row N:` prefix in that same block. But all R17 variants use inline `SQ-N (C-15):` prefix in the evaluation-step sub-question lists (Strategy, Architect, PM). C-43 requires the dedicated column form to appear in all three evaluation-step sub-question tables — not only in the CROSS-TEMPLATE block. | C-43 requires that Strategy, Architect, and PM sub-question presentations each use a table with a dedicated leftmost `Row #` column, making row position a first-class scannable field independent of sub-question content width. A skill that uses inline `SQ-N:` prefix in evaluation steps satisfies neither C-41 (the CROSS-TEMPLATE inline row form) nor C-43; it requires its own `Row #` column in every evaluation step to satisfy C-43. |

Denominator: 35 active → adding C-41 (baseline, no scoring weight), C-42, C-43 → 37 denominator.

---

## Variation Axes and Hypotheses

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | C-42-PARTIAL (TRIAD header unlabeled), C-43-FAIL (inline SQ-N prefix), Strategy-first | A skill that labels every named structural element — guard headers, step headings, slot headers, canary block — except the TRIAD header sits at the PARTIAL/PASS boundary: the TRIAD block's criterion IDs are already carried in its per-rule DO NOT line labels, making the header label partially redundant. Inline SQ-N prefix with per-SQ criterion labels is sufficient traceability without column separation. Strat→Arch→PM: C-35 ✓, C-36 N/A. |
| V-02 | C-42-FAIL (C-40 core blocks only), C-43-PASS (Row # column in all eval steps), Arch-first | Labeling only the core output templates (REAL-REQUIRED / MOCK-ACCEPTED decision blocks) and the CROSS-TEMPLATE RELATIONSHIP BLOCK keeps the skill body uncluttered for readers focused on decision outputs rather than criterion tracing. A dedicated Row # column in all three evaluation-step tables provides navigational identity without full criterion-label coverage. Arch→Strat→PM: C-36 ✓, C-35 N/A. |
| V-03 | C-42-PASS (universal labeling), C-43-FAIL (inline SQ-N prefix), Strategy-first | Universal criterion-ID labeling on every named structural element including the TRIAD header makes the skill fully self-referential: any criterion can be located by ID scan. Row # column separation adds positional overhead without semantic gain when sub-questions already carry their row ordinal inline. Strat→Arch→PM: C-35 ✓, C-36 N/A. |
| V-04 | C-42-PARTIAL (TRIAD header unlabeled), C-43-PASS (Row # column in all eval steps), Arch-first | Combines the strongest navigational form (Row # column in evaluation step tables) with the near-maximum labeling scope (TRIAD header only unlabeled). The TRIAD's per-rule inline labels already encode rule identity, making the header label less load-bearing than guard or canary block labels. Arch→Strat→PM: C-36 ✓, C-35 N/A. |
| V-05 | C-42-PASS (universal labeling), C-43-PASS (Row # column in all eval steps), Strategy-first | Ceiling variant: every named structural element carries a criterion-ID label (TRIAD header included), every evaluation step uses a dedicated `Row #` column, and Strategy-first role ordering establishes the tier anchor before structural checking. The two structural mechanisms (label completeness and row-position separability) are complementary: labels give semantic identity, columns give positional identity. Strat→Arch→PM: C-35 ✓, C-36 N/A. |

---

## V-01 — C-42 PARTIAL (TRIAD header unlabeled) + C-43 FAIL (inline SQ-N) + Strategy-first

**axis:** C-42-partial-triad-unlabeled, C-43-fail-inline-SQ, role-sequence-strat-first
**hypothesis:** All named structural elements carry criterion-ID labels at definition sites
(guard headers, step headings, completion gates, slot headers, canary block) except the TRIAD
header, which relies on its per-rule inline labels for criterion traceability. Inline SQ-N
prefix with per-SQ criterion annotations is sufficient for sub-question traceability without
column separation. Strat→Arch→PM: C-35 ✓, C-36 N/A.
**C-42:** PARTIAL — TRIAD header carries no `[C-NN]` labels; all other criterion-bearing
structural elements (guard header, step headings, completion gate headers, slot headers,
canary block) carry labels at definition sites.
**C-43:** FAIL — sub-questions in Strategy, Architect, and PM evaluation steps use
`SQ-N (C-15):` inline prefix; row number is embedded in cell content, not a dedicated column.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION (C-22):
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape that requires
  a positive argument against inertia. Absence of disqualification is not positive evidence.
  The inertia structure forces a genuine contrastive argument — confirmation that nothing is
  wrong does not earn escape from REAL-REQUIRED.

---

STEP 1 — READ (C-08)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->

Read {mock-artifact-path}. Extract namespace name, Category field, and current Status field
from each namespace section. Read TOPICS.md; record tier for {topic} and compliance tags.

Output at the top of your response: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG (C-01, C-02, C-06)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Apply all three rules. Rules are mandatory and not role-overridable. Fire before evaluation.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY

  RULE 2 — TIER-CRITICAL (Tier 2 and Tier 3):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL

  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present OR --compliance flag
    AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE

Output two lists:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED): [{namespace}: Category = {value}]

DO NOT proceed until every namespace is in exactly one list.

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (3 rules, all required):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] present.
  A two-of-three set does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  DO NOT apply evaluation to any auto-flagged namespace. Doing so is the named error
  AUTO-RULE CONTAMINATION. Any verdict applied to an auto-flagged namespace is void.

DO NOT proceed to STEP 3 (Strategy Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD is verified complete (3 of 3 labels present at this gate).

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only) (C-07, C-13, C-35)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

For each remaining namespace, answer sub-questions using entity-naming grammar (C-15).
Yes/no answers do not satisfy entity-naming sub-question requirements.

  SQ-1 (C-15): Name the specific Tier {tier} decision this namespace is intended to support.
        [This answer propagates forward into the Structural position SQ-1 anchor slot
        in every MOCK-ACCEPTED rationale block produced for this namespace.]
  SQ-2 (C-15): Name the belief the team would form about {topic} if this runs as
        MOCK-ACCEPTED (state whether that belief would be correct or incorrect).
  SQ-3 (C-15): Name the coverage gap that would keep this namespace in its REAL-REQUIRED
        default — or: "No gap — namespace positively demonstrates coverage adequacy for
        Tier {tier}".

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to Architect (C-35, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply Architect Evaluation (STEP 4) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names Architect
  Evaluation (STEP 4) as the suppressed step. Strategy-first design (C-35): tier anchoring
  established before structural contradiction checking begins.
  Named error: STRATEGY-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to Architect Evaluation: [{list}]

STEP 3 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 4 (Architect Evaluation) until Strategy verdicts and cross-step
  guard assignments are complete for all remaining namespaces.

---

STEP 4 — ARCHITECT EVALUATION (non-auto, non-Strategy-blocked namespaces only) (C-07, C-13)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Entry condition (C-17, C-26, C-35): STEP 4 applies only to namespaces not on the
Strategy-blocked list. Applying Architect evaluation to a Strategy-blocked namespace
is the named error GUARD-BYPASS CONTAMINATION.

For each qualifying namespace, answer sub-questions using entity-naming grammar (C-15).

  SQ-1 (C-15): Name the system component, dependency, or interface in the mock that confirms
        plausibility — or: "Contradiction found — name the specific element".
  SQ-2 (C-15): Name the data flow, state transition, or API shape the mock implies for
        {topic} — or: "Inconsistency found — name the specific element".
  SQ-3 (C-15): Name the architectural fact about {topic} this namespace's mock most directly
        depends on. State whether the mock is consistent with that fact.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM (C-26, C-40, C-42):
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

STEP 4 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 5 (PM Evaluation) until Architect verdicts and guard assignments
  are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Entry condition (C-17, C-26, C-35, C-40): STEP 5 applies ONLY to namespaces not on the
Strategy-blocked or Arch-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.

For each qualifying namespace, answer sub-questions using entity-naming grammar (C-15).

  SQ-1 (C-15): Name the required sections present in the mock artifact for this namespace.
  SQ-2 (C-15): Name the enforcement gate, decision table, or required output structure
        present — or: "Absent — name the missing element and which section defines it".
  SQ-3 (C-15): Name one structural gap that would keep this namespace in its REAL-REQUIRED
        default — or: "No gap — namespace positively demonstrates structural completeness".

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for
  every qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Trigger field: named, parseable artifact field at fixed position in every decision block.
  Position: second line of every decision block; "trigger = n/a" line of MOCK-ACCEPTED.
  Values (C-06, C-19): trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                                  STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-43):
<!-- C-38: Cross-template structural relationship encoded at template definition site.
  C-40: Criterion-ID label in block header.
  C-41 + C-43: Dedicated leftmost Row # column — row position is a first-class scannable
  field independent of content width. C-43 extends this column form to all evaluation-step
  tables in STEPS 3-5; the column form here is unified with those tables. -->
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
  Requires all three role verdicts positive; PM-qualified namespaces only.
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes — C-03)

  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30, C-42):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION. Classify:
    STRUCTURAL-FORM | TIER-GATING.]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1, C-20, C-25, C-42):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. A confirmatory sentence without a named contrasting namespace type =
    CONTRAST-INCOMPLETE. A single-slot rationale = RATIONALE-INCOMPLETE.]

REAL-REQUIRED template — evaluation-driven (C-06, C-14, C-19, C-21, C-24):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. Observable state as predicate.]
    ERROR — VERDICT-ECHO: grammatical subject is role name (named violation; rewrite required).
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry (C-24)]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 (Write Review Artifact) until all decision blocks complete.

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in the artifact):
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

This is the defining action of /mock:review. Edit {mock-artifact-path} in-place using Edit
tool. Replace Status fields only. Do not rewrite any other content.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY OUTPUT (C-12, C-16, C-40, C-42):
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

## V-02 — C-42 FAIL (C-40 core blocks only) + C-43 PASS (Row # column in all eval steps) + Arch-first

**axis:** C-42-fail-minimal-labeling, C-43-pass-row-column-all-eval-steps, role-sequence-arch-first
**hypothesis:** Stripping criterion-ID labels from all structural elements except the core
decision/template output blocks (REAL-REQUIRED template, MOCK-ACCEPTED template, CROSS-TEMPLATE
RELATIONSHIP BLOCK) keeps the skill body clean for practitioners focused on decision outputs.
Dedicated Row # columns in all three evaluation-step tables provide positional traceability
independent of content width — a reader navigates to "Row 2 (Architect)" without parsing label
text. Arch→Strat→PM: C-36 ✓, C-35 N/A.
**C-42:** FAIL — only the C-40 core decision and template blocks carry criterion-ID labels
(CROSS-TEMPLATE RELATIONSHIP BLOCK header, MOCK-ACCEPTED template fields, REAL-REQUIRED
template fields); all other structural elements (TRIAD header, guard headers, step headings,
completion gate headers, canary block) carry no `[C-NN]` annotations.
**C-43:** PASS — Strategy, Architect, and PM evaluation steps each present sub-questions in
a `| Row # | Sub-question |` table with a dedicated leftmost Row # column; row position is
first-class and independently scannable in all three evaluation steps.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION (C-22):
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring a
  positive argument against the default. The inertia structure forces a genuine contrastive
  argument — confirmation that nothing is wrong does not earn MOCK-ACCEPTED.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category field, and Status field from each
namespace section. Read TOPICS.md for tier and compliance tags.

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
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels present. A two-of-three set does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD:
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.

DO NOT proceed to STEP 3 (Architect Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only)

For each remaining namespace, answer sub-questions using entity-naming grammar.
Yes/no answers do not satisfy entity-naming sub-question requirements.
Table format with dedicated Row # column provides row-position scannability (C-43).

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
  Evaluation (STEP 4) as the suppressed step. Arch-first design: C-36 fires; C-35 N/A.
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
Table format with dedicated Row # column provides row-position scannability (C-43).

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
  Evaluation (STEP 5) as the suppressed step. Independent of the Arch-to-Strategy guard
  in STEP 3 — fires on a distinct verdict value.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation: [{list}]

DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and guard assignments
are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces not on the Arch-blocked or Strategy-blocked
lists. Named error: GUARD-BYPASS CONTAMINATION.
Table format with dedicated Row # column provides row-position scannability (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for every
qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field: named, parseable field at fixed position (second line of every block).
  Values: trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                    STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-43):
<!-- C-38: Cross-template structural relationship at template definition site.
  C-40: Criterion-ID label in block header.
  C-41 + C-43: Dedicated leftmost Row # column — row position is a first-class scannable
  field. C-43 unifies this column form with the evaluation-step tables in STEPS 3-5. -->
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
  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement = SLOT-VIOLATION. Classify: STRUCTURAL-FORM | TIER-GATING.]
  Contrast (SLOT 2 — dedicated, C-20, C-25):
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence because
    {reason}, this namespace's outputs are fully determined by {structural form property}.
    Confirmatory sentence without named contrasting namespace type = CONTRAST-INCOMPLETE.]

REAL-REQUIRED template — evaluation-driven (C-06, C-14, C-19, C-21, C-24):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict: [present-tense, artifact as subject]
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 (Write Review Artifact) until all decision blocks complete.

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
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk} — urgency: {BLOCKING | HIGH | MEDIUM}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place. Replace Status fields only.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [...] or Status: REAL-REQUIRED [...]

CANARY OUTPUT (C-12, C-16, C-40):
  After all edits, verify then confirm:
  CANARY ASSERTION: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK. Named error: CANARY-FALSE-POSITIVE.
  If not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

---

## V-03 — C-42 PASS (universal labeling) + C-43 FAIL (inline SQ-N) + Strategy-first

**axis:** C-42-pass-universal-labeling, C-43-fail-inline-SQ, role-sequence-strat-first
**hypothesis:** Labeling every named structural element — including the TRIAD header —
makes the skill fully self-referential: any criterion can be located by ID scan without
consulting the rubric. The TRIAD header carries its full criterion set because it is the
definition site for C-27 (completeness), C-29 (co-location), C-31 (cardinality), C-39
(independence), and C-40 (ID label). Inline SQ-N prefix with per-SQ criterion annotations
is sufficient traceability without column separation overhead. Strat→Arch→PM: C-35 ✓.
**C-42:** PASS — every criterion-bearing structural element carries a `[C-NN]` label at its
definition site: TRIAD header, AUTO-RULE guard header, inline SQ rows (via per-SQ criterion
annotations), step headings, slot headers, completion gate headers, and canary block.
**C-43:** FAIL — sub-questions in Strategy, Architect, and PM evaluation steps use
`SQ-N (C-15):` inline prefix; row number is embedded in cell content, not a dedicated column.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION (C-22):
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring
  a positive argument against inertia. Confirmation that nothing is wrong does not earn
  MOCK-ACCEPTED — the inertia structure demands a genuine contrastive argument.

---

STEP 1 — READ (C-08)
<!-- C-42: Step heading carries C-08 label at definition site. -->

Read {mock-artifact-path}. Extract namespace name, Category field, Status field per namespace.
Read TOPICS.md; record tier for {topic} (C-08) and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until extraction is complete.

---

STEP 2 — AUTO-FLAG (C-01, C-02, C-06)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Three rules. Mandatory. Fire before role evaluation. Not role-overridable (C-02).

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

FORBIDDEN OUTPUTS TRIAD (C-27, C-29, C-31, C-39, C-40, C-42):
<!-- C-39 independence declaration: TRIAD satisfies C-27, C-29, C-31, C-39, C-40, C-42
  independently of role sequence. C-42: TRIAD header carries full criterion-ID label set,
  making this block the definition site for each of these criteria simultaneously. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required):
  [EVIDENCE-HEAVY / C-27]   DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                             of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL / C-27]    DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                             of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE / C-27]       DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                             of mock quality, structural depth, or any role evaluation outcome.
  Completeness check [C-27]: all 3 labels present. A two-of-three set does not satisfy.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Any verdict applied to an auto-flagged namespace is void.

DO NOT proceed to STEP 3 (Strategy Evaluation) until partition confirmed and TRIAD verified.

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only) (C-07, C-13, C-35)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

For each remaining namespace, answer sub-questions using entity-naming grammar (C-15).
Yes/no answers do not satisfy entity-naming sub-question requirements (C-15).

  SQ-1 (C-15): Name the specific Tier {tier} decision this namespace is intended to support.
        [C-42: SQ-1 carries entity-naming criterion label at usage site.]
        [This answer propagates to Structural position SQ-1 anchor in MOCK-ACCEPTED template.]
  SQ-2 (C-15): Name the belief the team would form about {topic} if this runs as
        MOCK-ACCEPTED (state whether that belief would be correct or incorrect).
        [C-42: SQ-2 carries entity-naming criterion label at usage site.]
  SQ-3 (C-15): Name the coverage gap that would keep this namespace in its REAL-REQUIRED
        default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}".
        [C-42: SQ-3 carries entity-naming criterion label at usage site.]

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to Architect (C-35, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply Architect Evaluation (STEP 4) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names Architect
  Evaluation (STEP 4) as the suppressed step. Strategy-first design satisfies C-35.
  Named error: STRATEGY-GUARD-BYPASS.
  Record:
    Strategy-blocked: [{list}]
    Proceeding to Architect Evaluation: [{list}]

STEP 3 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 4 (Architect Evaluation) until Strategy verdicts and guard
  assignments are complete for all remaining namespaces.

---

STEP 4 — ARCHITECT EVALUATION (non-auto, non-Strategy-blocked namespaces only) (C-07, C-13, C-26)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Entry condition (C-17, C-26, C-35): STEP 4 applies only to namespaces not on the
Strategy-blocked list. Named error: GUARD-BYPASS CONTAMINATION.

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

CROSS-STEP GUARD — Architect to PM (C-26, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names PM Evaluation
  (STEP 5) as the suppressed step. Distinct from Strategy-to-Arch guard in STEP 3.
  Named error: ARCH-GUARD-BYPASS.
  Record:
    Arch-blocked: [{list}]
    Proceeding to PM Evaluation: [{list}]

STEP 4 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 5 (PM Evaluation) until Architect verdicts and guard assignments
  are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Entry condition (C-17, C-26, C-35, C-40): STEP 5 applies ONLY to namespaces not on the
Strategy-blocked or Arch-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.

  SQ-1 (C-15): Name the required sections present in the mock artifact for this namespace.
        [C-42: SQ-1 carries entity-naming criterion label at usage site.]
  SQ-2 (C-15): Name the enforcement gate, decision table, or required output structure
        present — or: "Absent — name the missing element and which section defines it".
        [C-42: SQ-2 carries entity-naming criterion label at usage site.]
  SQ-3 (C-15): Name one structural gap that would keep this namespace in its REAL-REQUIRED
        default — or: "No gap — namespace positively demonstrates structural completeness".
        [C-42: SQ-3 carries entity-naming criterion label at usage site.]

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for
  every qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Trigger field: named, parseable artifact field at fixed position in every decision block.
  Position: second line of every decision block; "trigger = n/a" for MOCK-ACCEPTED.
  Values (C-06, C-19): trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                                  STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-43):
<!-- C-38: Cross-template structural relationship encoded at template definition site.
  C-40: Criterion-ID label in block header.
  C-41 + C-43: Dedicated leftmost Row # column. C-43: this column form is the standard
  in this skill; evaluation-step sub-questions use inline SQ-N prefix (C-43 FAIL axis
  for this variant), while the correspondence table retains the column form. -->
| Row # | REAL-REQUIRED evaluation field             | MOCK-ACCEPTED structural analog                     |
|-------|--------------------------------------------|-----------------------------------------------------|
| 1     | Decision: REAL-REQUIRED                    | Decision: MOCK-ACCEPTED                             |
| 2     | trigger = {rule label}                     | trigger = n/a                                       |
| 3     | Failing evaluation: {role name}            | reason-code: [exact code from enumeration]          |
| 4     | Failing verdict: {full verdict string}     | Structural position: [SQ-1 anchor — tier decision] |
| 5     | SQ answer driving verdict:                 | Contrast: [contrasting namespace type +             |
|       |   {artifact-as-subject form}               |   structural factor distinguishing it]              |
| 6     | Artifact state: {art-subj, pres-tense}     | (no analog — exits before next-steps)               |
| 7     | /{skill} {topic} — {Artifact state}        | (no analog)                                         |

Row 5 grammar constraint (C-21, C-32):
  SQ answer: present-tense, artifact as grammatical subject. ERROR — VERDICT-ECHO: role as subject.

MOCK-ACCEPTED template (C-03, C-10, C-20, C-22, C-23, C-25, C-30):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]

  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30, C-42):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision.
    Generic adequacy statement = SLOT-VIOLATION. Classify: STRUCTURAL-FORM | TIER-GATING.]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1, C-20, C-25, C-42):
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
  Artifact state: [present-tense, artifact as subject — propagates to next-steps (C-24)]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 (Write Review Artifact) until all decision blocks complete.

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
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

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable) (C-04)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->

Edit {mock-artifact-path} in-place. Replace Status fields only. Do not rewrite other content.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [...] or Status: REAL-REQUIRED [...]

CANARY OUTPUT (C-12, C-16, C-40, C-42):
<!-- C-42: Canary output block carries criterion-ID labels at definition site. -->
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

## V-04 — C-42 PARTIAL (TRIAD header unlabeled) + C-43 PASS (Row # column in all eval steps) + Arch-first

**axis:** C-42-partial-triad-unlabeled, C-43-pass-row-column-all-eval-steps, role-sequence-arch-first
**hypothesis:** Combining dedicated Row # columns in all evaluation-step tables with near-maximum
criterion-ID labeling (all elements labeled except the TRIAD header) produces the strongest
navigational and semantic coverage short of the ceiling. The TRIAD block's per-rule inline
labels ([EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE]) already encode criterion identity at
the rule level; the header label is additive but redundant with those inline labels.
Arch→Strat→PM: C-36 ✓, C-35 N/A.
**C-42:** PARTIAL — TRIAD header carries no `[C-NN]` labels; all other criterion-bearing
structural elements (AUTO-RULE guard header, step headings, completion gate headers, template
slot headers, canary block) carry criterion-ID labels at definition sites.
**C-43:** PASS — Strategy, Architect, and PM evaluation steps each use a `| Row # | Sub-question |`
table with a dedicated leftmost Row # column; row position is independently scannable.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION (C-22):
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape that requires
  a positive argument against inertia. Absence of disqualification is not positive evidence.
  The inertia structure forces a genuine contrastive argument.

---

STEP 1 — READ (C-08)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->

Read {mock-artifact-path}. Extract namespace name, Category field, Status field per namespace.
Read TOPICS.md; record tier and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG (C-01, C-02, C-06)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Three rules. All mandatory. Fire before role evaluation. Not role-overridable.

  RULE 1 — EVIDENCE-HEAVY: IF Category == EVIDENCE-HEAVY THEN REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL:  IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
                            THEN REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE:     IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
                            THEN REAL-REQUIRED, trigger = COMPLIANCE

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

AUTO-RULE CONTAMINATION GUARD (C-17, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Any verdict applied to an auto-flagged namespace is void.

DO NOT proceed to STEP 3 (Architect Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only) (C-07, C-13, C-36)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

For each remaining namespace, answer sub-questions. Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to Strategy (C-36, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply Strategy Evaluation (STEP 4) to these namespaces.
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names Strategy
  Evaluation (STEP 4) as the first suppressed step. Arch-first design: C-36 ✓, C-35 N/A.
  Named error: ARCH-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Strategy Evaluation: [{list}]

STEP 3 COMPLETION GATE (C-18, C-28, C-40, C-42):
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

CROSS-STEP GUARD — Strategy to PM (C-36, C-40, C-42):
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

STEP 4 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and guard assignments
  are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Entry condition: STEP 5 applies ONLY to namespaces not on the Arch-blocked or Strategy-blocked
lists. Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column (C-43).

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE (C-18, C-28, C-40, C-42):
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
  C-41 + C-43: Dedicated leftmost Row # column — unified column form across STEPS 3-5
  evaluation tables and this correspondence table. -->
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
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]

  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30, C-42):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision.
    Generic adequacy statement = SLOT-VIOLATION. Classify: STRUCTURAL-FORM | TIER-GATING.]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1, C-20, C-25, C-42):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
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
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 (Write Review Artifact) until all decision blocks complete.

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
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

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable) (C-04)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->

Edit {mock-artifact-path} in-place. Replace Status fields only.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [...] or Status: REAL-REQUIRED [...]

CANARY OUTPUT (C-12, C-16, C-40, C-42):
<!-- C-42: Canary output block carries criterion-ID labels at definition site. -->
  After all edits, verify then confirm:
  CANARY ASSERTION: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK. Named error: CANARY-FALSE-POSITIVE.
  If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-05 — C-42 PASS (universal labeling) + C-43 PASS (Row # column in all eval steps) + Strategy-first

**axis:** C-42-pass-universal, C-43-pass-row-column-all-eval-steps, role-sequence-strat-first
**hypothesis:** Universal criterion-ID labeling at every named structural definition site and
a dedicated Row # column in every evaluation-step sub-question table are complementary
mechanisms: labels give semantic identity (what criterion a field satisfies), columns give
positional identity (where it lives in the output independent of content). Combined with
Strategy-first tier anchoring (C-35), this is the ceiling variant: C-42 PASS + C-43 PASS +
C-35 ✓ + C-36 N/A. Every structural element is labeled, positioned, and traceable.
**C-42:** PASS — every criterion-bearing structural element carries a `[C-NN]` label at its
definition site: TRIAD header, AUTO-RULE guard header, sub-question table column headers
(carrying entity-naming criterion), step headings, slot headers, completion gate headers,
and canary block.
**C-43:** PASS — Strategy, Architect, and PM evaluation steps each use a `| Row # | Sub-question |`
table with a dedicated leftmost Row # column; row position is first-class and independently
scannable in all three evaluation steps.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION (C-22):
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring a
  positive argument against inertia. Absence of disqualification is not positive evidence.
  The inertia structure forces a genuine contrastive argument — confirmation that nothing is
  wrong does not earn escape from REAL-REQUIRED.

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

Three rules. Mandatory. Fire before role evaluation. Not role-overridable (C-02).

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

DO NOT proceed until every namespace is in exactly one list.

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (C-27, C-29, C-31, C-39, C-40, C-42):
<!-- C-39 independence declaration: TRIAD satisfies C-27, C-29, C-31, C-39, C-40, C-42
  independently of role sequence. C-42: TRIAD header carries full criterion-ID label set,
  making this block the definition site for all six criteria simultaneously. A TRIAD header
  without criterion-ID labels is a C-42 gap even when all other elements are labeled —
  the PARTIAL/PASS boundary for C-42. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required):
  [EVIDENCE-HEAVY / C-27]   DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                             of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL / C-27]    DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                             of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE / C-27]       DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                             of mock quality, structural depth, or any role evaluation outcome.
  Completeness check [C-27]: all 3 labels present. A two-of-three set does not satisfy.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Any verdict applied to an auto-flagged namespace is void.

DO NOT proceed to STEP 3 (Strategy Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD is verified complete (3 of 3 labels present at this gate).

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only) (C-07, C-13, C-35)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

For each remaining namespace. Table with dedicated Row # column (C-43). Entity-naming
grammar required (C-15); yes/no answers do not satisfy.

| Row # | Sub-question (C-15, C-43) |
|-------|--------------------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. [This answer propagates to Structural position SQ-1 anchor in every MOCK-ACCEPTED block for this namespace.] |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to Architect (C-35, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply Architect Evaluation (STEP 4) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names Architect
  Evaluation (STEP 4) as the suppressed step. Strategy-first design (C-35): tier anchoring
  established before structural contradiction checking begins.
  Named error: STRATEGY-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to Architect Evaluation: [{list}]

STEP 3 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 4 (Architect Evaluation) until Strategy verdicts and cross-step
  guard assignments are complete for all remaining namespaces.

---

STEP 4 — ARCHITECT EVALUATION (non-auto, non-Strategy-blocked namespaces only) (C-07, C-13, C-26)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Entry condition (C-17, C-26, C-35): STEP 4 applies only to namespaces not on the
Strategy-blocked list. Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column (C-43). Entity-naming grammar required (C-15).

| Row # | Sub-question (C-15, C-43) |
|-------|--------------------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM (C-26, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID labels at definition site. -->
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names PM Evaluation
  (STEP 5) as the suppressed step. Distinct from Strategy-to-Arch guard in STEP 3:
  fires on a different verdict value and suppresses a different step.
  Named error: ARCH-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to PM Evaluation: [{list}]

STEP 4 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 5 (PM Evaluation) until Architect verdicts and guard assignments
  are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Entry condition (C-17, C-26, C-35, C-40): STEP 5 applies ONLY to namespaces not on the
Strategy-blocked or Arch-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.
Table with dedicated Row # column (C-43). Entity-naming grammar required (C-15).

| Row # | Sub-question (C-15, C-43) |
|-------|--------------------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Gate header carries criterion-ID labels at definition site. -->
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for
  every qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Trigger field: named, parseable artifact field at fixed position in every decision block.
  Position: second line of every decision block; "trigger = n/a" for MOCK-ACCEPTED.
  Values (C-06, C-19): trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                                  STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-43):
<!-- C-38: Cross-template structural relationship encoded at template definition site.
  C-40: Criterion-ID label in block header.
  C-41 + C-43: Dedicated leftmost Row # column — row position is a first-class scannable
  field independent of content width. C-43 unifies this column form with evaluation-step
  tables in STEPS 3-5: a reader scanning Row 2 finds the same positional contract in every
  sub-question table and in this correspondence table. -->
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
  Requires all three role verdicts positive; PM-qualified namespaces only.
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes — C-03)

  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30, C-42):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION. Classify:
    STRUCTURAL-FORM | TIER-GATING.]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1, C-20, C-25, C-42):
  <!-- C-42: Template slot header carries criterion-ID labels at definition site. -->
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. A confirmatory sentence without a named contrasting namespace type =
    CONTRAST-INCOMPLETE. A single-slot rationale = RATIONALE-INCOMPLETE.]

REAL-REQUIRED template — evaluation-driven (C-06, C-14, C-19, C-21, C-24):
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. Observable state as predicate.]
    ERROR — VERDICT-ECHO: grammatical subject is role name (named violation; rewrite required).
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry (C-24)]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 (Write Review Artifact) until every namespace has a completed
decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24)
<!-- C-42: Step heading carries criterion-ID labels at definition site. -->

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in the artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED (trace-*, scout-feasibility, listen-*, scout-competitors):
    Entry format (evaluation-driven):   /{skill-id} {topic} — {Artifact state}
    Entry format (auto-flagged):        /{skill-id} {topic} — trigger: {trigger value}
    ERROR — TRACEABILITY-BREAK: entry with 2 components only (missing Artifact state).

  Priority 2 — Non-critical evaluation-driven REAL-REQUIRED:
    Entry format: /{skill-id} {topic} — {Artifact state}

  Priority 3 — Evidence-heavy and compliance REAL-REQUIRED:
    Entry format: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement (required output — C-09):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"
    Include urgency grouping commentary for each priority group if more than one namespace.

DO NOT proceed to STEP 8 (Write Status Back) until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable) (C-04)
<!-- C-42: Step heading carries criterion-ID label at definition site. -->

This is the defining action of /mock:review. Edit {mock-artifact-path} in-place using Edit
tool. Replace Status fields only. Do not rewrite any other content.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY OUTPUT (C-12, C-16, C-40, C-42):
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

## C-42 / C-43 Pattern Summary

| Variation | C-42 | C-43 | TRIAD header | Guard headers | Step headings | Slot headers | Canary block | Eval SQ format | Role order |
|-----------|------|------|-------------|--------------|---------------|-------------|-------------|----------------|-----------|
| V-01 | PARTIAL | FAIL | unlabeled | labeled | labeled | labeled | labeled | inline SQ-N | Strat→Arch→PM |
| V-02 | FAIL | PASS | unlabeled | unlabeled | unlabeled | unlabeled | unlabeled | Row # table | Arch→Strat→PM |
| V-03 | PASS | FAIL | labeled | labeled | labeled | labeled | labeled | inline SQ-N | Strat→Arch→PM |
| V-04 | PARTIAL | PASS | unlabeled | labeled | labeled | labeled | labeled | Row # table | Arch→Strat→PM |
| V-05 | PASS | PASS | labeled | labeled | labeled | labeled | labeled | Row # table | Strat→Arch→PM |
