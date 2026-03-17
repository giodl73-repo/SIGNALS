---
skill: quest-variate
skill_target: mock-review
date: 2026-03-15
round: 16
rubric_version: v16
status: VARIATE
---

# mock-review Variate — Round 16

**Date:** 2026-03-15
**Skill:** mock-review
**Rubric:** v16 (C-01 through C-43; aspirational denominator = 35)
**Round:** R16 — targeting v16 new criteria: C-42, C-43

---

## What R15 Left Open

R15 achieved a 99.7 ceiling across all five variants, with a single missed aspirational point
in each variation: C-35 (unreachable in Arch-first designs) or C-36 (unreachable in Strat-first
designs). Two new criteria for R16 derive from patterns observed in R15 V-03/V-05 (extended
labeling beyond 4 blocks) and V-02/V-05 (dedicated row-number column in the CROSS-TEMPLATE
block):

| Criterion | R15 ceiling coverage | Gap |
|-----------|---------------------|-----|
| **C-40 extended → C-42** | R15 V-03/V-05 apply criterion-ID labels beyond the 4 C-40 named blocks — labeling individual template slots (`Structural position`, `Contrast`), cross-step guard headers, step completion gates, and the canary output with criterion IDs. C-40 is satisfied at 4 blocks; the extended labeling in V-03/V-05 is advisory excellence, not a criterion requirement. | C-42 requires criterion-ID labels on ALL named structural elements throughout the skill — not only the 4 C-40 core blocks, but individual template slots, cross-step guard headers, named error classification labels, step completion gate headers, and canary output blocks. A skill that labels only the 4 core blocks satisfies C-40 but not C-42. A named structural element without a criterion-ID parenthetical at its definition site is a C-42 gap, even if the 4 C-40 blocks are fully labeled. |
| **C-41 column form → C-43** | R15 V-02/V-05 use a dedicated leftmost `Row #` column in the CROSS-TEMPLATE RELATIONSHIP BLOCK (satisfying C-41 with the stronger column form). V-01/V-04 use inline `Row N:` prefix — also satisfying C-41. Both forms satisfy C-41; the column form's structural superiority is that row position is a scannable first-class field independent of column width. | C-43 requires the dedicated leftmost `Row #` column form to extend to ALL evaluation sub-question tables (Strategy, Architect, PM evaluation steps) — not only the CROSS-TEMPLATE RELATIONSHIP BLOCK. A skill that uses the dedicated column form in the CROSS-TEMPLATE block but formats evaluation sub-questions as inline `SQ-N: ...` lists satisfies C-41 but not C-43. The column form must be present in all three evaluation step sub-question tables. |

- **C-42**: Universal element labeling — every named structural element throughout the skill
  (individual template slots such as `Structural position` and `Contrast`, cross-step guard
  headers, step completion gate headers, named error classification labels, and canary output
  blocks) carries a criterion-ID parenthetical at its definition site. The 4 C-40 core blocks
  are a required subset; C-42 requires complete coverage of all named structural elements, not
  only those 4. A named element without a criterion-ID parenthetical is a C-42 gap even if all
  4 C-40 core blocks are labeled.
- **C-43**: First-class row-number column in evaluation step sub-question tables — Strategy,
  Architect, and PM evaluation steps present their sub-questions in tables with a dedicated
  leftmost `Row #` column, making row position scannable independently of sub-question label
  or content. A skill that uses the column form only in the CROSS-TEMPLATE RELATIONSHIP BLOCK
  satisfies C-41 but not C-43; the column form must appear in all three evaluation step tables.

Denominator: 33 → 35.

---

## Variation Axes and Hypotheses

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | C-42-scope-extended, Strategy-first, inline SQ format | Applying C-42 labels to individual template slots (Structural position, Contrast), cross-step guard headers, and step completion gate headers — but not to individual SQ sub-question rows or named error inline labels — satisfies C-42 at the pragmatic boundary: structural elements that carry criterion-specific named content are labeled; elements that carry criterion-specific values (individual SQ rows, inline error names) are not. Strategy-first: C-35 ✓, C-36 N/A. |
| V-02 | C-43-evaluation-tables-column, Arch-first, C-40 labeling only | A dedicated leftmost `Row #` column in Strategy, Architect, and PM evaluation sub-question tables makes row position scannable across all evaluation steps — a reader navigates to "Row 2 (Architect)" without parsing inline SQ labels or content cells. C-40 minimal labeling (4 core blocks). Arch-first: C-36 ✓, C-35 N/A. |
| V-03 | C-42-scope-maximum, Strategy-first, inline SQ format | Labeling every named structural element including individual SQ sub-question rows, named error classification labels, canary output fields, and trigger value enumerations creates a fully self-referential skill: any criterion can be verified by label scan alone without consulting the rubric. C-42 maximum. Strategy-first: C-35 ✓. |
| V-04 | C-42-extended + C-43-evaluation-tables + Arch-first + tight lifecycle gates | C-42 extended labeling and C-43 column form complement each other: labels give semantic identity (what a field satisfies), column position gives navigational identity (where it lives). Tight lifecycle emphasis deepens C-18/C-28 with verbose step-name anchors at every gate. Arch-first: C-36 ✓. |
| V-05 | C-42-maximum + C-43-full + Strategy-first + R15 V-05 excellence signals | Maximum C-42 scope + C-43 column form in all evaluation tables + Strategy-first + R15 excellence signals (FIELD SYMMETRY AND POLARITY ASYMMETRY block pair making inversion verifiable from template comparison; SQ-1 annotated at collection site with forward-propagation note). Every structural element is labeled (C-42), positioned (C-43), traceable (SQ-1 propagation), and self-verifying (POLARITY ASYMMETRY block). Ceiling variation. |

---

## V-01 — C-42 Extended Scope + Strategy-first

**axis:** C-42-scope-extended, inline SQ-N format
**hypothesis:** C-42 labels applied to named structural element headers (template slots,
guard headers, gate headers) — beyond the 4 C-40 core blocks — satisfies C-42 at the
boundary between what "carries a criterion-specific name" and what is merely a value instance.
SQ sub-question rows and inline error labels are value instances; named structural element
headers are definition sites. The distinction is deterministic from definition-site vs
instantiation-site grammar. Strategy-first ordering (Strat→Arch→PM): C-35 ✓, C-36 N/A.
All R15 V-01 patterns preserved; C-42 extended labels added to definition-site headers.

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

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category field, and current Status field
from each namespace section. Read TOPICS.md; record tier for {topic} and compliance tags.

Output at the top of your response: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

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

FORBIDDEN OUTPUTS TRIAD (C-27, C-29, C-31, C-39, C-40):
<!-- C-39 independence declaration: This TRIAD block satisfies C-27 (complete per-rule
  DO NOT set), C-29 (phase-gate co-location), C-31 (cardinality header declaration), C-39
  (independence declaration embedded), and C-40 (criterion-ID label in block header)
  independently of role sequence. Position at the phase gate is upstream of all role steps. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                    of mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] present.
  A two-of-three set does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40):
  DO NOT apply evaluation to any auto-flagged namespace. Doing so is the named error
  AUTO-RULE CONTAMINATION. Any verdict applied to an auto-flagged namespace is void.

DO NOT proceed to STEP 3 (Strategy Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD is verified complete (3 of 3 labels present at this gate).

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only) (C-07, C-13)

For each remaining namespace, answer sub-questions using "Name X" / "What specific X" grammar.
Yes/no answers do not satisfy entity-naming sub-question requirements (C-15).

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
<!-- C-42: This guard header is a named structural element carrying criterion-ID label. -->
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
<!-- C-42: This gate header is a named structural element carrying criterion-ID label. -->
  DO NOT proceed to STEP 4 (Architect Evaluation) until Strategy verdicts and cross-step
  guard assignments are complete for all remaining namespaces.

---

STEP 4 — ARCHITECT EVALUATION (non-auto, non-Strategy-blocked namespaces only) (C-07, C-13)

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
<!-- C-42: This guard header is a named structural element carrying criterion-ID label. -->
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names PM Evaluation
  (STEP 5) as the suppressed step. It is distinct from the Strategy-to-Arch guard in STEP 3
  — two independent guards, each firing on a distinct verdict value.
  Named error: ARCH-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to PM Evaluation: [{list}]

STEP 4 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: This gate header is a named structural element carrying criterion-ID label. -->
  DO NOT proceed to STEP 5 (PM Evaluation) until Architect verdicts and guard assignments
  are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13)

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
<!-- C-42: This gate header is a named structural element carrying criterion-ID label. -->
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for
  every qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30)

Trigger field: named, parseable artifact field at fixed position in every decision block.
  Position: second line of every decision block; "trigger = n/a" line of MOCK-ACCEPTED.
  Values (C-06, C-19): trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                                  STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41):
<!-- C-38: Cross-template structural relationship encoded at template definition site.
  C-40: Criterion-ID label in block header.
  C-41: Inline row-position annotations — each field entry labeled Row N: alongside field
  name, making correspondence verifiable by row position. -->
| Row annotation              | REAL-REQUIRED evaluation field             | MOCK-ACCEPTED structural analog                     |
|-----------------------------|---------------------------------------------|-----------------------------------------------------|
| Row 1: Decision             | Decision: REAL-REQUIRED                     | Decision: MOCK-ACCEPTED                             |
| Row 2: trigger              | trigger = {rule label}                      | trigger = n/a                                       |
| Row 3: Failing evaluation   | Failing evaluation: {role name}             | reason-code: [exact code from enumeration]          |
| Row 4: Failing verdict      | Failing verdict: {full verdict string}      | Structural position: [SQ-1 anchor]                  |
| Row 5: SQ answer / Contrast | SQ answer driving verdict:                  | Contrast: [contrasting namespace type +             |
|                             |   {artifact-as-subject form}                |   structural factor distinguishing it]              |
| Row 6: Artifact state       | Artifact state: {art-subj, pres-tense}      | (no analog — exits before next-steps)               |
| Row 7: Next-steps entry     | /{skill} {topic} — {Artifact state}         | (no analog)                                         |

Row 5 grammar constraint (C-21, C-32):
  SQ answer: present-tense, artifact as grammatical subject.
  ERROR — VERDICT-ECHO: role as grammatical subject at Row 5.
  "Section 4.1 contains no tier-boundary gate" = valid. "Architect found no gate" = VERDICT-ECHO.

MOCK-ACCEPTED template (C-03, C-10, C-20, C-22, C-23, C-25, C-30):
  Requires all three role verdicts positive; PM-qualified namespaces only.
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes — C-03)

  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30, C-42):
  <!-- C-42: Individual template slot header carries criterion-ID parenthetical. -->
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION. Classify:
    STRUCTURAL-FORM | TIER-GATING.]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1, C-20, C-25, C-42):
  <!-- C-42: Individual template slot header carries criterion-ID parenthetical. -->
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

Complete all namespace decision blocks.
DO NOT proceed to STEP 7 (Write Review Artifact) until every namespace has a completed
decision block.

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24)

Write simulations/mock/{topic}-review-{date}.md.
  Header: Topic | Tier | Date
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly in the artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED (trace-*, scout-feasibility, listen-*, scout-competitors):
    Entry format (evaluation-driven):
      /{skill-id} {topic} — {Artifact state}
      REQUIRED SLOT: `{Artifact state}` propagates from the STEP 6 decision block.
      ERROR — TRACEABILITY-BREAK: entry with 2 components only (missing Artifact state).
    Entry format (auto-flagged):
      /{skill-id} {topic} — trigger: {trigger value}

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

This is the defining action of /mock:review. Edit {mock-artifact-path} in-place using Edit
tool. Replace Status fields only. Do not rewrite any other content.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY OUTPUT (C-12, C-16, C-40, C-42):
<!-- C-42: Canary output block carries criterion-ID parenthetical at its definition site. -->
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

## V-02 — C-43 Evaluation Tables Column + Arch-first

**axis:** C-43-evaluation-tables-column, output-format-table
**hypothesis:** A dedicated leftmost `Row #` column in Strategy, Architect, and PM
sub-question tables makes row position a first-class scannable field across all evaluation
steps: a reader navigates to "Row 2" in any evaluation step by scanning a single fixed column,
independent of content width or sub-question numbering. C-40 minimal labeling (4 core blocks
only). Role sequence: Arch→Strat→PM (C-26 + C-36 both fire). C-35 N/A.
All R15 V-02 patterns preserved; C-43 column form extended to evaluation step tables.

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

FORBIDDEN OUTPUTS TRIAD (C-27, C-29, C-31, C-39, C-40):
<!-- C-39 independence declaration: TRIAD satisfies C-27, C-29, C-31, C-39, and C-40
  independently of role sequence. Phase-gate position is upstream of all role steps. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required — verify all 3 before proceeding):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels present. A two-of-three set does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40):
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.

DO NOT proceed to STEP 3 (Architect Evaluation) until two-list partition is confirmed
and FORBIDDEN OUTPUTS TRIAD verified complete (3 of 3 labels present).

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only) (C-07, C-13)

For each remaining namespace, answer sub-questions. Table format with dedicated Row # column
satisfies entity-naming grammar requirement (C-15) and row-position scanability (C-43).

| Row # | Sub-question (C-15, C-43) |
|-------|--------------------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to Strategy (C-26, C-36, C-40):
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

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only) (C-07, C-13)

Entry condition: STEP 4 applies ONLY to namespaces not on the Arch-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.

| Row # | Sub-question (C-15, C-43) |
|-------|--------------------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.] |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM (C-36, C-40):
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM
  Evaluation (STEP 5) as the suppressed step. Independent of the Arch-to-Strategy guard in
  STEP 3 — fires on a distinct verdict value.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation: [{list}]

DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and guard assignments
are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13)

Entry condition: STEP 5 applies ONLY to namespaces not on the Arch-blocked or Strategy-blocked
lists. Named error: GUARD-BYPASS CONTAMINATION.

| Row # | Sub-question (C-15, C-43) |
|-------|--------------------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts are written for every
qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30)

Trigger field: named, parseable field at fixed position (second line of every block).
  Values: trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                    STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-43):
<!-- C-38: Cross-template structural relationship at template definition site.
  C-40: Criterion-ID label in block header.
  C-41 + C-43: Dedicated leftmost Row # column — row position is first-class scannable field,
  independent of content width. C-43 extends this column form from the evaluation step tables
  (STEPS 3-5) to the correspondence table here, creating a unified column-form pattern. -->
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

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24)

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

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable) (C-04)

Edit {mock-artifact-path} in-place. Replace Status fields only.
  REPLACE: Status: MOCK (awaiting review)
  WITH:    Status: MOCK-ACCEPTED [...] or Status: REAL-REQUIRED [...]

CANARY OUTPUT (C-12, C-16, C-40):
  After all edits, verify then confirm:
  CANARY ASSERTION: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK. Named error: CANARY-FALSE-POSITIVE.
  If not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

---

## V-03 — C-42 Maximum Scope + Strategy-first

**axis:** C-42-scope-maximum, inline SQ-N format
**hypothesis:** Labeling every named structural element — including individual SQ sub-question
rows with entity-naming criterion (C-15), named error classifications (C-21, C-32) inline
in classification labels, and canary block fields — creates a fully self-referential skill.
A reviewer can validate any criterion by scanning for its ID without consulting the rubric.
Maximum scope makes the label set enumerable and complete: unlabeled elements are not just
ungrouped, they are detectable gaps. Strategy-first: C-35 ✓, C-36 N/A.
All R15 V-03 patterns preserved; C-42 maximum labels applied throughout.

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
<!-- C-42: Step heading carries C-08 label as the criterion this step satisfies. -->

Read {mock-artifact-path}. Extract namespace name, Category field, Status field per namespace.
Read TOPICS.md; record tier for {topic} (C-08) and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"  [C-08]
DO NOT proceed to STEP 2 (Auto-Flag) until extraction is complete.

---

STEP 2 — AUTO-FLAG (C-01, C-02, C-06)
<!-- C-42: Step heading carries criterion labels. -->

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
  independently of role sequence. C-42 extends the labeling to this block header. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required):
  [EVIDENCE-HEAVY / C-27]   DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless
                             of mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL / C-27]    DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless
                             of mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE / C-27]       DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless
                             of mock quality, structural depth, or any role evaluation outcome.
  Completeness check [C-27]: all 3 labels present. A two-of-three set does not satisfy.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40, C-42):
<!-- C-42: Named guard header carries all criterion-ID labels at definition site. -->
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.

DO NOT proceed to STEP 3 (Strategy Evaluation) until partition confirmed and TRIAD verified.

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only) (C-07, C-13, C-35)
<!-- C-42: Step heading carries criterion-ID labels. -->

Entity-naming grammar required (C-15); yes/no answers invalid.

  SQ-1 (C-15, C-23, C-30, C-42): Name the specific Tier {tier} decision this namespace
        is intended to support.
        [This answer propagates into the Structural position SQ-1 anchor (C-23, C-30) in
        all MOCK-ACCEPTED rationale blocks produced for this namespace.]
  SQ-2 (C-15, C-42): Name the belief the team would form about {topic} if this runs as
        MOCK-ACCEPTED (state whether that belief would be correct or incorrect).
  SQ-3 (C-15, C-42): Name the coverage gap keeping this namespace at REAL-REQUIRED default
        — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}".

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to Architect (C-35, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID labels. -->
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply Architect Evaluation (STEP 4) to these namespaces.
  Named error: STRATEGY-GUARD-BYPASS [C-35, C-42].
  Record:
    Strategy-blocked: [{list}]
    Proceeding to Architect Evaluation: [{list}]

STEP 3 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Named gate header carries criterion-ID labels. -->
  DO NOT proceed to STEP 4 (Architect Evaluation) until Strategy verdicts and guard
  assignments complete for all remaining namespaces.

---

STEP 4 — ARCHITECT EVALUATION (qualifying namespaces only) (C-07, C-13, C-26)
<!-- C-42: Step heading carries criterion-ID labels. -->

Entry condition (C-17, C-26, C-35, C-42): STEP 4 applies ONLY to namespaces not on
Strategy-blocked list. Named error: GUARD-BYPASS CONTAMINATION [C-17, C-42].

  SQ-1 (C-15, C-42): Name the system component, dependency, or interface in the mock that
        confirms plausibility — or: "Contradiction found — name the specific element".
  SQ-2 (C-15, C-42): Name the data flow, state transition, or API shape the mock implies
        for {topic} — or: "Inconsistency found — name the specific element".
  SQ-3 (C-15, C-42): Name the architectural fact about {topic} this namespace's mock most
        directly depends on. State whether the mock is consistent with that fact.

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM (C-26, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID labels. -->
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  Named error: ARCH-GUARD-BYPASS [C-26, C-42].
  Record:
    Arch-blocked: [{list}]
    Proceeding to PM Evaluation: [{list}]

STEP 4 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Named gate header carries criterion-ID labels. -->
  DO NOT proceed to STEP 5 (PM Evaluation) until Architect verdicts and guard assignments
  complete.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13)
<!-- C-42: Step heading carries criterion-ID labels. -->

Entry condition (C-17, C-26, C-35, C-42): STEP 5 applies ONLY to namespaces not on
Strategy-blocked or Arch-blocked lists. Named error: GUARD-BYPASS CONTAMINATION [C-17, C-42].

  SQ-1 (C-15, C-42): Name the required sections present in the mock artifact.
  SQ-2 (C-15, C-42): Name the enforcement gate, decision table, or required output structure
        present — or: "Absent — name the missing element and which section defines it".
  SQ-3 (C-15, C-42): Name one structural gap keeping this namespace at REAL-REQUIRED default
        — or: "No gap — namespace positively demonstrates structural completeness".

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Named gate header carries criterion-ID labels. -->
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts complete.

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30, C-42)
<!-- C-42: Step heading carries criterion-ID labels. -->

Trigger field (C-06, C-19, C-42): second line of every decision block; named parseable field.
  Values: trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                    STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-42):
<!-- C-38, C-40, C-41, C-42: Block header carries all criterion-IDs. C-42 extends to block header.
  C-41: Inline row-position annotations in correspondence table. -->
| Row annotation              | REAL-REQUIRED evaluation field             | MOCK-ACCEPTED structural analog                     |
|-----------------------------|---------------------------------------------|-----------------------------------------------------|
| Row 1: Decision [C-42]      | Decision: REAL-REQUIRED                     | Decision: MOCK-ACCEPTED                             |
| Row 2: trigger [C-06, C-19, C-42] | trigger = {rule label}              | trigger = n/a                                       |
| Row 3: Role / code [C-42]   | Failing evaluation: {role name}             | reason-code: [exact code]                           |
| Row 4: Verdict / position [C-42] | Failing verdict: {full verdict}        | Structural position: [SQ-1 anchor]                  |
| Row 5: SQ / Contrast [C-14, C-20, C-21, C-25, C-42] | SQ answer driving verdict: | Contrast: [contrasting ns type + factor] |
| Row 6: Artifact state [C-24, C-42] | Artifact state: {art-subj}          | (no analog)                                         |
| Row 7: Next-steps [C-24, C-42] | /{skill} {topic} — {Artifact state}      | (no analog)                                         |

Row 5 grammar constraint (C-21, C-32, C-42):
  SQ answer: present-tense, artifact as grammatical subject.
  ERROR — VERDICT-ECHO [C-21, C-32, C-42]: role as grammatical subject at Row 5.
  Artifact-as-subject = valid; role-as-subject = VERDICT-ECHO (named violation).

MOCK-ACCEPTED template (C-03, C-10, C-20, C-22, C-23, C-25, C-30, C-42):
  Decision: MOCK-ACCEPTED [C-03, C-42]
  trigger = n/a [C-19, C-42]
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT] [C-03, C-42]

  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30, C-42):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement = SLOT-VIOLATION [C-23, C-30, C-42]. Classify:
    STRUCTURAL-FORM | TIER-GATING [C-42].]

  Contrast (SLOT 2 — dedicated, C-20, C-25, C-42):
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without contrasting namespace type =
    CONTRAST-INCOMPLETE [C-20, C-25, C-42].]

REAL-REQUIRED template — evaluation-driven (C-06, C-14, C-19, C-21, C-24, C-42):
  Decision: REAL-REQUIRED [C-42]
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE} [C-06, C-19, C-42]
  Failing evaluation: [Strategy | Architect | PM] [C-07, C-42]
  Failing verdict: [full verdict string] [C-14, C-42]
  SQ answer driving verdict: [artifact as subject, pres-tense] [C-14, C-21, C-42]
    ERROR — VERDICT-ECHO [C-21, C-42]: role as grammatical subject.
  Artifact state: [art-subj, pres-tense — propagates to next-steps (C-24, C-42)]

REAL-REQUIRED template — auto-flagged (C-02, C-06, C-42):
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

Complete all namespace decision blocks.
DO NOT proceed to STEP 7 (Write Review Artifact) until all blocks complete [C-18, C-28, C-42].

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24, C-42)
<!-- C-42: Step heading carries criterion-ID labels. -->

Write simulations/mock/{topic}-review-{date}.md.
  Ordering rule (C-05, C-42): "Critical namespaces first, non-critical evaluation-driven next,
  evidence-heavy and compliance last." State this rule explicitly in the artifact.

  Priority 1 — Critical REAL-REQUIRED [C-05, C-42]:
    /{skill-id} {topic} — {Artifact state}
    ERROR — TRACEABILITY-BREAK [C-24, C-42]: entry missing Artifact state propagation.
  Priority 2 — Non-critical evaluation-driven [C-05, C-42]: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance [C-05, C-42]: /{skill-id} {topic} — trigger: {trigger}

  Cross-namespace risk statement (C-09, C-42):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk} — urgency: {level}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact written [C-18, C-28, C-42].

---

STEP 8 — WRITE STATUS BACK (C-04, C-42)
<!-- C-42: Step heading carries criterion-ID labels. -->

Edit {mock-artifact-path} in-place (C-04). Replace Status fields only.

CANARY OUTPUT (C-12, C-16, C-40, C-42):
  CANARY ASSERTION: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any field remains (C-16, C-42). Named error: CANARY-FALSE-POSITIVE [C-16, C-42].
  If not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}" [C-16, C-42].

---

## V-04 — C-42 Extended + C-43 Evaluation Tables + Arch-first + Tight Lifecycle Gates

**axis:** C-42-extended + C-43-evaluation-tables, Arch-first, tight lifecycle
**hypothesis:** C-42 extended labeling (template slot headers, guard headers, gate headers)
and C-43 column form in evaluation tables complement each other without creating annotation
noise: labels give semantic identity at definition sites, column positions give navigational
identity at every evaluation row. Together they make the skill mechanically navigable from
two independent access paths. Tight lifecycle gates (verbose step-name anchors deepening
C-18/C-28) eliminate forward-reference ambiguity. Arch-first: C-36 ✓, C-35 N/A.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION (C-22):
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring a
  positive argument against the default position. The inertia structure is architectural:
  REAL-REQUIRED needs no argument; MOCK-ACCEPTED needs a contrastive argument establishing
  that this namespace does not cross the threshold requiring real evidence. Confirmation
  that nothing is wrong is not a positive argument.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract namespace name, Category field, Status field per namespace.
Read TOPICS.md; record tier and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 (Auto-Flag) until all fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Three rules. Mandatory. Not role-overridable. Fire before evaluation.

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
DO NOT proceed until every namespace is in exactly one list.

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (C-27, C-29, C-31, C-39, C-40):
<!-- C-39 independence declaration: TRIAD satisfies C-27, C-29, C-31, C-39, and C-40
  independently of role sequence. C-42 scope extends to guard header below. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED regardless of
                    mock quality, structural depth, or any role evaluation outcome.
  Completeness check: all 3 labels present. Two-of-three does not satisfy.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID parenthetical at its definition site. -->
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.
  Any verdict applied to an auto-flagged namespace is void.

DO NOT proceed to STEP 3 (Architect Evaluation) until two-list partition is confirmed and
FORBIDDEN OUTPUTS TRIAD is verified complete (3 of 3 labels present at this gate).

===================================================================

---

STEP 3 — ARCHITECT EVALUATION (non-auto namespaces only) (C-07, C-13)

For each remaining namespace, answer sub-questions. Table format with dedicated Row # column
(C-43) and entity-naming grammar (C-15).

| Row # | Sub-question (C-15, C-43) |
|-------|--------------------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to Strategy (C-26, C-36, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID parenthetical. -->
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply Strategy Evaluation (STEP 4) to these namespaces.
  This guard fires on `architect-verdict = CONTRADICTS-ARCHITECTURE` and names Strategy
  Evaluation (STEP 4) as the suppressed step. C-36 fires here: Arch-first ordering ensures
  structural contradictions short-circuit tier-coverage analysis before it begins.
  Named error: ARCH-GUARD-BYPASS.
  Record:
    Arch-blocked (architect-verdict = CONTRADICTS-ARCHITECTURE): [{list}]
    Proceeding to Strategy Evaluation: [{list}]

STEP 3 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Named gate header carries criterion-ID parenthetical. -->
  DO NOT proceed to STEP 4 (Strategy Evaluation) until Architect verdicts and guard
  assignments are complete for all remaining namespaces.

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked namespaces only) (C-07, C-13)

Entry condition (C-17, C-26, C-36): STEP 4 applies ONLY to namespaces not on Arch-blocked
list. Named error: GUARD-BYPASS CONTAMINATION.

| Row # | Sub-question (C-15, C-43) |
|-------|--------------------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.] |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap keeping this namespace at REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to PM (C-36, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID parenthetical. -->
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  This guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` and names PM
  Evaluation (STEP 5) as the suppressed step. Independent of the Arch-to-Strategy guard.
  Named error: STRATEGY-TO-PM-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT FOR TIER {tier}): [{list}]
    Proceeding to PM Evaluation: [{list}]

STEP 4 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Named gate header carries criterion-ID parenthetical. -->
  DO NOT proceed to STEP 5 (PM Evaluation) until Strategy verdicts and guard assignments
  are complete for all qualifying namespaces.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13)

Entry condition (C-17, C-26, C-36): STEP 5 applies ONLY to namespaces not on Arch-blocked
or Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.

| Row # | Sub-question (C-15, C-43) |
|-------|--------------------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap keeping this namespace at REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Named gate header carries criterion-ID parenthetical. -->
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts complete for all
  qualifying namespaces.

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30)

Trigger field: named parseable field at fixed position (second line of every block).
  Values: trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                    STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-43):
<!-- C-38: Cross-template structural relationship at template definition site.
  C-40: Criterion-ID label in block header. C-41: Row-position annotations present.
  C-43: Dedicated Row # column — row position first-class scannable field, same column form
  as evaluation step tables (STEPS 3-5), creating a unified navigational pattern. -->
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

Row 5 grammar constraint (C-21, C-32):
  SQ answer: artifact as grammatical subject, present tense.
  ERROR — VERDICT-ECHO: role as grammatical subject. "Section 4.1 contains no gate" = valid.
  "Architect found no gate" = VERDICT-ECHO (named violation; rewrite required).

MOCK-ACCEPTED template (C-03, C-10, C-20, C-22, C-23, C-25, C-30):

  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]

  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30, C-42):
  <!-- C-42: Individual template slot header carries criterion-ID parenthetical. -->
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION. Classify:
    STRUCTURAL-FORM | TIER-GATING.]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1, C-20, C-25, C-42):
  <!-- C-42: Individual template slot header carries criterion-ID parenthetical. -->
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
    ERROR — VERDICT-ECHO: role as grammatical subject (named violation; rewrite required).
  Artifact state: [present-tense, artifact as subject — propagates to next-steps (C-24)]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 (Write Review Artifact) until all decision blocks complete.

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24)

Write simulations/mock/{topic}-review-{date}.md.
  Ordering rule (state explicitly): "Critical namespaces first, non-critical evaluation-driven
  next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
    REQUIRED SLOT: Artifact state propagates from STEP 6 block.
    ERROR — TRACEABILITY-BREAK: entry missing Artifact state (2 components only).
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement (C-09):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk} — urgency: {level}"

DO NOT proceed to STEP 8 (Write Status Back) until review artifact confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable) (C-04)

Edit {mock-artifact-path} in-place. Replace Status fields only.

CANARY OUTPUT (C-12, C-16, C-40, C-42):
<!-- C-42: Canary output block header carries criterion-ID parenthetical. -->
  CANARY ASSERTION: "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any field remains. Named error: CANARY-FALSE-POSITIVE.
  If not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.

---

## V-05 — C-42 Maximum + C-43 Full + Strategy-first + R15 Excellence Signals

**axis:** C-42-maximum + C-43-full + R15-excellence-signals
**hypothesis:** Maximum C-42 scope (every named structural element labeled) combined with
C-43 column form in all evaluation tables and the CROSS-TEMPLATE block creates a unified
navigational structure: any field is findable by (criterion-ID label, row-number column).
R15 V-05 excellence signals — FIELD SYMMETRY AND POLARITY ASYMMETRY block pair making the
inversion verifiable from template comparison alone, plus SQ-1 annotated at collection site
with explicit forward-propagation note — close the last advisory dependencies: C-22 inversion
becomes structurally verifiable, and SQ-1 traceability is bidirectional from origin. Strategy-
first: C-35 ✓, C-36 N/A. Ceiling variation for R16.

---

You are running /mock:review.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION (C-22):
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring
  a positive argument against inertia. The inertia structure forces a genuine contrastive
  argument — confirmation that nothing is wrong does not earn escape.

FIELD SYMMETRY AND POLARITY ASYMMETRY (C-22, C-25, C-38, C-42):
<!-- C-42: This block header carries criterion-ID parenthetical.
  C-22: The POLARITY ASYMMETRY sub-block makes the DEFAULT DECISION POSITION inversion
  verifiable from template comparison alone — without referencing the standalone C-22 block.
  C-38: The FIELD SYMMETRY sub-block encodes cross-template structural relationship here.
  C-25: Dedicated Contrast slot in MOCK-ACCEPTED is the asymmetric field. -->

  FIELD SYMMETRY — REAL-REQUIRED and MOCK-ACCEPTED share field positions 1-4 (Decision,
  trigger, evaluation/reason-code, verdict/Structural position). Row 5 is the pivot field:
  both templates carry content at Row 5 (SQ answer vs Contrast). This symmetry is verifiable
  by comparing the two templates at Row 5 — same position, opposite content type.

  POLARITY ASYMMETRY — Row 5 content flips polarity between templates:
    REAL-REQUIRED Row 5: SQ answer driving FAILURE — artifact state as subject, present tense.
    MOCK-ACCEPTED Row 5: Contrast argument for ESCAPE — contrasting namespace as subject.
  The polarity flip at Row 5 is the structural encoding of the inversion in DEFAULT DECISION
  POSITION: failure evidence at Row 5 signals REAL-REQUIRED; escape argument at Row 5 signals
  MOCK-ACCEPTED. A reviewer confirms the inversion by inspecting Row 5 alone.

---

STEP 1 — READ (C-08, C-42)
<!-- C-42: Step heading carries criterion-ID labels. -->

Read {mock-artifact-path}. Extract namespace name, Category, Status per namespace.
Read TOPICS.md; record tier (C-08) and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)" [C-08, C-42]
DO NOT proceed to STEP 2 (Auto-Flag) until extraction complete.

---

STEP 2 — AUTO-FLAG (C-01, C-02, C-06, C-42)
<!-- C-42: Step heading carries criterion-ID labels. -->

Three rules. Mandatory. Not role-overridable. Fire before evaluation (C-02).

  RULE 1 — EVIDENCE-HEAVY (all tiers) [C-06, C-42]:
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+) [C-06, C-08, C-42]:
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active) [C-06, C-42]:
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE

Output two lists (C-01, C-42):
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (C-27, C-29, C-31, C-39, C-40, C-42):
<!-- C-39 independence declaration: TRIAD satisfies C-27, C-29, C-31, C-39, C-40, and C-42
  independently of role sequence. Phase-gate position is upstream of all role steps. C-42
  extends labeling to this block header and to every labeled element within it. -->
FORBIDDEN OUTPUTS TRIAD (3 rules, all required):
  [EVIDENCE-HEAVY / C-27, C-42]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED
                                  regardless of mock quality, depth, or evaluation outcome.
  [TIER-CRITICAL / C-27, C-42]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED
                                  regardless of mock quality, depth, or evaluation outcome.
  [COMPLIANCE / C-27, C-42]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED
                                  regardless of mock quality, depth, or evaluation outcome.
  Completeness check [C-27, C-42]: all 3 labels present. Two-of-three does not satisfy.

AUTO-RULE CONTAMINATION GUARD (C-17, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID parenthetical. -->
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.

DO NOT proceed to STEP 3 (Strategy Evaluation) until partition confirmed and TRIAD verified.

===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces only) (C-07, C-13, C-35, C-42)
<!-- C-42: Step heading carries criterion-ID labels. -->

Entity-naming grammar required (C-15, C-42). Table format with dedicated Row # column (C-43).

| Row # | Sub-question (C-15, C-43, C-42) |
|-------|---------------------------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. **[C-23, C-30, C-42: This SQ-1 answer propagates forward into the `Feeds tier decision:` slot in every MOCK-ACCEPTED rationale block produced for this namespace — the traceability chain runs from this collection site through the Structural position slot.]** |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap keeping this namespace at REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to Architect (C-35, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID parenthetical. -->
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply Architect Evaluation (STEP 4) to these namespaces.
  C-35 fires: Strategy runs before Architect, establishing tier anchoring first.
  Named error: STRATEGY-GUARD-BYPASS [C-35, C-42].
  Record:
    Strategy-blocked: [{list}]
    Proceeding to Architect Evaluation: [{list}]

STEP 3 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Named gate header carries criterion-ID parenthetical. -->
  DO NOT proceed to STEP 4 (Architect Evaluation) until Strategy verdicts and guard
  assignments complete for all remaining namespaces.

---

STEP 4 — ARCHITECT EVALUATION (qualifying namespaces only) (C-07, C-13, C-26, C-42)
<!-- C-42: Step heading carries criterion-ID labels. -->

Entry condition (C-17, C-26, C-35, C-42): STEP 4 ONLY for namespaces not on Strategy-blocked.
Named error: GUARD-BYPASS CONTAMINATION [C-17, C-42].

| Row # | Sub-question (C-15, C-43, C-42) |
|-------|---------------------------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

CROSS-STEP GUARD — Architect to PM (C-26, C-40, C-42):
<!-- C-42: Named guard header carries criterion-ID parenthetical. -->
  For any namespace where architect-verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT apply PM Evaluation (STEP 5) to these namespaces.
  Named error: ARCH-GUARD-BYPASS [C-26, C-42].
  Record:
    Arch-blocked: [{list}]
    Proceeding to PM Evaluation: [{list}]

STEP 4 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Named gate header carries criterion-ID parenthetical. -->
  DO NOT proceed to STEP 5 (PM Evaluation) until Architect verdicts and guard assignments
  complete.

---

STEP 5 — PM EVALUATION (qualifying namespaces only) (C-07, C-13, C-42)
<!-- C-42: Step heading carries criterion-ID labels. -->

Entry condition (C-17, C-26, C-35, C-42): STEP 5 ONLY for namespaces not on Strategy-blocked
or Arch-blocked lists. Named error: GUARD-BYPASS CONTAMINATION [C-17, C-42].

| Row # | Sub-question (C-15, C-43, C-42) |
|-------|---------------------------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap keeping this namespace at REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

STEP 5 COMPLETION GATE (C-18, C-28, C-40, C-42):
<!-- C-42: Named gate header carries criterion-ID parenthetical. -->
  DO NOT proceed to STEP 6 (Decisions with Citation) until PM verdicts complete.

---

STEP 6 — DECISIONS WITH CITATION (C-03, C-06, C-14, C-19, C-21, C-25, C-30, C-42)
<!-- C-42: Step heading carries criterion-ID labels. -->

Trigger field (C-06, C-19, C-42): second line of every decision block; named parseable field.
  Values: trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                    STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

CROSS-TEMPLATE RELATIONSHIP BLOCK — REAL-REQUIRED / MOCK-ACCEPTED FIELD CORRESPONDENCE (C-38, C-40, C-41, C-43, C-42):
<!-- C-38: Cross-template structural relationship at template definition site.
  C-40: Criterion-ID label in block header. C-41 + C-43: Dedicated leftmost Row # column.
  C-42: Maximum labeling — block header carries all criterion IDs. Row-level labels below. -->
| Row # | REAL-REQUIRED evaluation field                          | MOCK-ACCEPTED structural analog                      |
|-------|---------------------------------------------------------|------------------------------------------------------|
| 1 [C-42] | Decision: REAL-REQUIRED                            | Decision: MOCK-ACCEPTED                              |
| 2 [C-06, C-19, C-42] | trigger = {rule label}              | trigger = n/a                                        |
| 3 [C-42] | Failing evaluation: {role name}                    | reason-code: [exact code — C-03, C-42]               |
| 4 [C-42] | Failing verdict: {full verdict string}             | Structural position: [SQ-1 anchor — C-23, C-30, C-42] |
| 5 [C-14, C-20, C-21, C-25, C-42] | SQ answer driving verdict: | Contrast: [contrasting ns type + factor — C-20, C-25, C-42] |
|         | {artifact-as-subject form — C-21, C-42}            |                                                      |
| 6 [C-24, C-42] | Artifact state: {art-subj, pres-tense}      | (no analog — C-42)                                   |
| 7 [C-24, C-42] | /{skill} {topic} — {Artifact state}         | (no analog — C-42)                                   |

Row 5 grammar constraint (C-21, C-32, C-42):
  SQ answer: present-tense, artifact as grammatical subject (C-21, C-42).
  ERROR — VERDICT-ECHO [C-21, C-32, C-42]: role as grammatical subject at Row 5.
  "Section 4.1 contains no tier-boundary gate" = valid. "Architect found no gate" = VERDICT-ECHO.

MOCK-ACCEPTED template (C-03, C-10, C-20, C-22, C-23, C-25, C-30, C-42):
  Decision: MOCK-ACCEPTED [C-42]
  trigger = n/a [C-19, C-42]
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT] [C-03, C-42]

  Structural position (SLOT 1 — Strategy SQ-1 anchor, C-23, C-30, C-42):
  <!-- C-42: Template slot header carries criterion-ID parenthetical at definition site. -->
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this namespace
    supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION [C-23, C-30,
    C-42]. Classify: STRUCTURAL-FORM | TIER-GATING [C-42].]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1, C-20, C-25, C-42):
  <!-- C-42: Template slot header carries criterion-ID parenthetical at definition site. -->
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE [C-20, C-25, C-42].]

REAL-REQUIRED template — evaluation-driven (C-06, C-14, C-19, C-21, C-24, C-42):
  Decision: REAL-REQUIRED [C-42]
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE} [C-06, C-19, C-42]
  Failing evaluation: [Strategy | Architect | PM] [C-07, C-42]
  Failing verdict: [full verdict string] [C-14, C-42]
  SQ answer driving verdict: [present-tense, artifact as subject] [C-14, C-21, C-42]
    ERROR — VERDICT-ECHO [C-21, C-32, C-42]: role as grammatical subject (rewrite required).
  Artifact state: [art-subj, pres-tense — propagates to next-steps (C-24, C-42)]

REAL-REQUIRED template — auto-flagged (C-02, C-06, C-42):
  Decision: REAL-REQUIRED [C-42]
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE} [C-06, C-42]

Complete all namespace decision blocks.
DO NOT proceed to STEP 7 (Write Review Artifact) until all blocks complete [C-18, C-28, C-42].

---

STEP 7 — WRITE REVIEW ARTIFACT (C-05, C-09, C-24, C-42)
<!-- C-42: Step heading carries criterion-ID labels. -->

Write simulations/mock/{topic}-review-{date}.md.
  Ordering rule (C-05, C-42): state explicitly — "Critical namespaces first, non-critical
  evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED [C-05, C-42]:
    Entry format (evaluation-driven): /{skill-id} {topic} — {Artifact state}
      REQUIRED SLOT: Artifact state propagates from STEP 6 block (C-24, C-42).
      ERROR — TRACEABILITY-BREAK [C-24, C-42]: entry missing Artifact state.
    Entry format (auto-flagged): /{skill-id} {topic} — trigger: {trigger value}
  Priority 2 — Non-critical evaluation-driven [C-05, C-42]: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance [C-05, C-42]: /{skill-id} {topic} — trigger: {trigger}

  Cross-namespace risk statement (C-09, C-42):
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk} — urgency: {level}"
    Urgency grouping commentary per priority group required when more than one namespace (C-09).

DO NOT proceed to STEP 8 (Write Status Back) until review artifact confirmed written
[C-18, C-28, C-42].

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable) (C-04, C-42)
<!-- C-42: Step heading carries criterion-ID labels. -->

Edit {mock-artifact-path} in-place (C-04). Replace Status fields only.
  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY OUTPUT (C-12, C-16, C-40, C-42):
<!-- C-42: Canary output block header carries criterion-ID parenthetical at definition site. -->
  After completing all edits, verify before confirming.
  CANARY ASSERTION [C-12, C-42]:
    "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
  PROHIBITED if any Status field remains as MOCK (awaiting review) [C-16, C-42].
  Named error: CANARY-FALSE-POSITIVE [C-16, C-42] — writing canary when condition not met.
  If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}" [C-16, C-42].

Full confirmation block (C-42):
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
